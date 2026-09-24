#!/usr/bin/env python3
"""Check that every quote in a research dossier really appears on its page.

Retrieval agents fabricate citations: a correctly formatted URL with a quote
the page does not contain. This script checks each quote against the page text
directly, so fabrication is caught mechanically and no model tokens are spent on
the pages that check out. Only the failures need a human (or a WebFetch retry).

Dossier format (SUMMARY.md §7): each quote follows the url it belongs to.

    - **fact:** Tonga beat Australia 16–11 at Ballymore on 30 June 1973.
      - url: https://example.org/page
      - quote: "Tonga 16 Australia 11"
      - quote: "at Ballymore … on June 30"
      - status: VERIFIED

A quote may contain an ellipsis (… or ...): each piece must be on the page, in
order. Matching ignores case, whitespace, curly-vs-straight quotes, dash types
and markdown emphasis.

Usage (stdlib only):

    python3 tools/verify_quotes.py notes/tonga/gen3-ballymore.md [more files or dirs]
    python3 tools/verify_quotes.py --url URL --quote "exact text"

Results, one line per quote:
    FOUND      the text is on the page
    NOT FOUND  the page loaded and the text is not on it — treat as fabricated
    BLOCKED    bot wall, JS shell or near-empty page — retry with WebFetch
    SKIPPED    a PDF that could not be read (no pypdf, or a scan) — check by hand
    BANNED     a site the book does not cite (Wikipedia and the rest) — never fetched
    ERROR      the fetch failed (HTTP error, timeout, DNS)

Exit status is 0 only when every quote is FOUND.
"""

import argparse
import html
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Hosts disagree on which user agent they serve: ESPN answers a full Chrome
# string with an empty 202 but serves a bare one; others want the full one.
# Each is tried in turn, through curl and then urllib (they fail on different
# sites), until one returns a readable page.
USER_AGENTS = (
    "Mozilla/5.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
)

# Phrases that mean we got a challenge page, not the article. Papers Past and
# Trove both answer 200 with one of these as the body; so does Gallica (Altcha).
WALLS = ("just a moment", "enable javascript", "verify you are human",
         "checking your browser", "captcha", "access denied",
         "please turn javascript on", "vérification de sécurité", "altcha")

# The book cites none of these (SUMMARY.md §6, "Sourcing"). A quote from one is
# rejected before any fetch, however accurate it is.
BANNED = ("wikipedia.org", "wikimedia.org", "wikiwand.com", "grokipedia.com",
          "facebook.com", "keithprowse.co.uk")

URL_RE = re.compile(r"^\s*[-*]?\s*\**url:?\**:?\s*<?(\S+?)>?\s*$", re.I)
QUOTE_RE = re.compile(r"^\s*[-*]?\s*\**quote:?\**:?\s*(.+?)\s*$", re.I)
ELLIPSIS_RE = re.compile(r"\s*(?:…|\.\.\.|\[\s*…\s*\]|\[\s*\.\.\.\s*\])\s*")


def normalise(text):
    text = html.unescape(text).lower()
    text = re.sub(r"[‘’‚‛′`´]", "'", text)
    text = re.sub(r"[“”„‟″«»]", '"', text)
    text = re.sub(r"[‐‑‒–—―−]", "-", text)
    text = text.replace(" ", " ").replace("­", "")
    return re.sub(r"\s+", " ", text).strip()


def page_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<!--.*?-->", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return normalise(raw)


def get_curl(url, ua):
    marker = "\n@@STATUS@@"
    out = subprocess.run(
        ["curl", "-sL", "--compressed", "--max-time", "25", "-A", ua,
         "-H", "Accept-Language: en,*;q=0.5",
         "-w", marker + "%{http_code} %{content_type}", url],
        capture_output=True)
    if out.returncode != 0:
        raise OSError(f"curl exit {out.returncode}")
    body, _, tail = out.stdout.rpartition(marker.encode())
    code, _, ctype = tail.decode(errors="replace").partition(" ")
    if not code.startswith("2"):
        raise urllib.error.HTTPError(url, int(code or 0), "", None, None)
    return ctype, body


def get_urllib(url, ua):
    req = urllib.request.Request(url, headers={"User-Agent": ua,
                                               "Accept-Language": "en,*;q=0.5"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.headers.get("Content-Type", ""), resp.read()


def pdf_text(body):
    """Text of a PDF via pypdf, or None when pypdf is not installed."""
    try:
        import io
        import pypdf
    except ImportError:
        return None
    reader = pypdf.PdfReader(io.BytesIO(body))
    return normalise(" ".join(p.extract_text() or "" for p in reader.pages))


def read_page(ctype, body):
    if "pdf" in ctype.lower() or body[:5] == b"%PDF-":
        text = pdf_text(body)
        if text is None:
            return ("SKIPPED", "PDF; install pypdf to check it")
        if len(text) < 200:
            return ("SKIPPED", "PDF with no text layer; check by hand")
        return ("OK", text)
    charset = re.search(r"charset=([\w-]+)", ctype)
    text = page_text(body.decode(charset.group(1) if charset else "utf-8",
                                 errors="replace"))
    if len(text) < 800 or any(w in text[:3000] for w in WALLS):
        return ("BLOCKED", f"{len(text)} chars of text")
    return ("OK", text)


def banned(url):
    host = re.sub(r"^[a-z]+://", "", url.lower()).split("/")[0].split(":")[0]
    return any(host == d or host.endswith("." + d) for d in BANNED)


def fetch(url, cache):
    if banned(url):
        return ("BANNED", "not citable in this book")
    if url not in cache:
        result = None
        for getter in (get_curl, get_urllib):
            for ua in USER_AGENTS:
                try:
                    attempt = read_page(*getter(url, ua))
                except urllib.error.HTTPError as e:
                    attempt = ("ERROR", f"HTTP {e.code}")
                except Exception as e:  # timeouts, DNS, TLS, no curl
                    attempt = ("ERROR", type(e).__name__)
                # Keep a BLOCKED over an ERROR: it says more about the page.
                if result is None or attempt[0] != "ERROR":
                    result = attempt
                if attempt[0] in ("OK", "SKIPPED"):
                    break
            if result[0] in ("OK", "SKIPPED"):
                break
        cache[url] = result
    return cache[url]


def clean_quote(q):
    q = q.strip().strip("*_").strip()
    if len(q) >= 2 and q[0] in "\"“'‘" and q[-1] in "\"”'’":
        q = q[1:-1]
    return normalise(q.replace("*", "").replace("_", " "))


def found(text, quote):
    pos = 0
    for piece in ELLIPSIS_RE.split(quote):
        piece = piece.strip(" .,;:")
        if not piece:
            continue
        hit = text.find(piece, pos)
        if hit < 0:
            return False
        pos = hit + len(piece)
    return True


def pairs_from(path):
    url = None
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = URL_RE.match(line)
        if m:
            url = m.group(1).rstrip(").,")
            continue
        m = QUOTE_RE.match(line)
        if m:
            if url is None:
                print(f"{path}:{n}: quote with no url above it", file=sys.stderr)
            else:
                yield f"{path}:{n}", url, m.group(1)


def check(pairs):
    cache, failures, total = {}, 0, 0
    for where, url, quote in pairs:
        total += 1
        status, payload = fetch(url, cache)
        if status == "OK":
            status = "FOUND" if found(payload, clean_quote(quote)) else "NOT FOUND"
            detail = ""
        else:
            detail = f" ({payload})"
        if status != "FOUND":
            failures += 1
        short = quote if len(quote) <= 70 else quote[:67] + "..."
        print(f"{status:<9} {where}  {url}{detail}\n          {short}")
    print(f"\n{total - failures}/{total} quotes found.")
    return failures == 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*", help="dossier files or directories")
    ap.add_argument("--url")
    ap.add_argument("--quote")
    args = ap.parse_args()

    if args.url or args.quote:
        if not (args.url and args.quote):
            ap.error("--url and --quote go together")
        pairs = [("cli", args.url, args.quote)]
    else:
        if not args.paths:
            ap.error("give dossier files, or --url and --quote")
        files = []
        for p in map(Path, args.paths):
            files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
        pairs = [pair for f in files for pair in pairs_from(f)]
        if not pairs:
            sys.exit("no url/quote pairs found — check the dossier format")
    sys.exit(0 if check(pairs) else 1)


if __name__ == "__main__":
    main()
