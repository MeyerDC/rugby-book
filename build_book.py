#!/usr/bin/env python3
"""
Build a book from a Claude conversation export (conversations.json).

- Extracts ONLY Claude's prose (content blocks of type "text").
- Reconstructs the linear thread via parent_message_uuid (drops regen branches).
- Segments into chapters by country and sections by generation.
- Tucuman is folded into the Argentina chapter as a closing section.
- Strips trivial process preambles ("Let me research it properly." etc.).
- Emits book.md (+ prints a segmentation report to stderr).

Usage:
    python3 build_book.py            # writes book.md, prints report
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The Claude export lives in its own download folder; reference it directly so
# this script keeps working from a separate project folder.
EXPORT = Path(
    "/Users/dmeyer1/Downloads/"
    "data-8c25c602-e4bf-49ec-a4c4-cf2562093724-1784103189-f896aa35-batch-0000"
)
SRC = EXPORT / "conversations.json"
OUT_MD = HERE / "book.md"

# Follow-up conversations that extend a chapter (e.g. Wales Gen 6/7 were done
# in a later session exported to a separate folder). Only appended if present.
CONT_FILES = [
    Path("/Users/dmeyer1/Downloads/"
         "data-8c25c602-e4bf-49ec-a4c4-cf2562093724-1784119557-ff9498f7-batch-0000/"
         "conversations.json"),
]

ROOT_PARENT = "00000000-0000-4000-8000-000000000000"

BOOK_TITLE = "Rugby Has No Class"
BOOK_SUBTITLE = "A Generational History of the Game, Country by Country"

# ---------------------------------------------------------------------------
# 1. Load + linearize the conversation
# ---------------------------------------------------------------------------

def load_conversation():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    convo = data[0] if isinstance(data, list) else data
    return convo


def linearize(messages):
    """Return the canonical linear path of messages.

    The export is a tree (branches from regenerations/edits). We take the leaf
    with the latest created_at and walk parent_message_uuid back to the root.
    """
    by_uuid = {m["uuid"]: m for m in messages}
    child_uuids = {m["parent_message_uuid"] for m in messages}

    # Candidate leaves: messages that are nobody's parent.
    leaves = [m for m in messages if m["uuid"] not in child_uuids]
    if not leaves:
        leaves = messages
    leaf = max(leaves, key=lambda m: m.get("created_at", ""))

    path = []
    cur = leaf
    seen = set()
    while cur is not None and cur["uuid"] not in seen:
        seen.add(cur["uuid"])
        path.append(cur)
        parent = cur.get("parent_message_uuid")
        if not parent or parent == ROOT_PARENT:
            break
        cur = by_uuid.get(parent)
    path.reverse()
    return path


def clean_text(message):
    """Join the text-type content blocks of a message into clean prose."""
    parts = []
    for block in message.get("content", []):
        if block.get("type") == "text":
            t = block.get("text", "")
            if t:
                parts.append(t)
    return "\n\n".join(parts).strip()


def extract_sources(message):
    """Pull (title, url, site) from web_search / web_fetch tool results."""
    out = []
    for block in message.get("content", []):
        if block.get("type") != "tool_result":
            continue
        content = block.get("content")
        items = content if isinstance(content, list) else [content]
        for it in items:
            if not isinstance(it, dict):
                continue
            url = it.get("url")
            title = it.get("title")
            if url and title:
                site = (it.get("metadata") or {}).get("site_name") or ""
                out.append({
                    "title": title.strip(),
                    "url": url.strip(),
                    "site": site.strip(),
                })
    return out


# ---------------------------------------------------------------------------
# 2. Prose cleanup
# ---------------------------------------------------------------------------

TOOL_PLACEHOLDER = re.compile(
    r"```\s*\nThis block is not supported on your current device yet\.\s*\n```",
    re.IGNORECASE,
)

# Paragraph is pure process/meta chatter -> drop it (only when leading/trailing).
META_PARA = re.compile(
    r"^(let me\b|i'?ll\b|i need to\b|i'?m going to\b|i'?m organizing\b|i should\b|"
    r"i can'?t reproduce|researched\.?$|right\s*[\u2014-]|okay\b|ok\b)",
    re.IGNORECASE,
)
# Trailing meta sentences to shave off the end of an otherwise-real paragraph.
META_TAIL = re.compile(
    r"\s*(let me (research|pull|look|dig|map|take|get)[^.]*\.|"
    r"let'?s (dig|pull|get) in[^.]*\.|"
    r"here'?s how\.|hold onto (it|that)\.)\s*$",
    re.IGNORECASE,
)


def strip_prose(text):
    text = TOOL_PLACEHOLDER.sub("", text)
    # normalize excessive blank lines
    paras = [p.strip() for p in re.split(r"\n\s*\n", text)]
    paras = [p for p in paras if p]

    # Drop leading pure-meta paragraphs (short ones only, to be safe).
    while paras:
        p = paras[0]
        if len(p) < 400 and META_PARA.match(p) and not p.lstrip("#").strip().lower().startswith("gen"):
            paras.pop(0)
        else:
            break

    # Shave a trailing meta sentence off the first surviving paragraph.
    if paras:
        paras[0] = META_TAIL.sub("", paras[0]).strip()

    return "\n\n".join(paras).strip()


# ---------------------------------------------------------------------------
# 3. Country / section detection
# ---------------------------------------------------------------------------

COUNTRY_PATTERNS = [
    ("uruguay", re.compile(r"\burugua", re.I)),
    ("tucuman", re.compile(r"tucum", re.I)),
    ("argentina", re.compile(r"\bargentin", re.I)),
    ("chile", re.compile(r"\bchile", re.I)),
    ("georgia", re.compile(r"\bgeorgia", re.I)),
    ("romania", re.compile(r"\broman(ia|ian)", re.I)),
    ("south_africa", re.compile(r"south africa|springbok", re.I)),
    ("england", re.compile(r"\bengland\b", re.I)),
    ("wales", re.compile(r"\bwales\b|\bwelsh\b", re.I)),
]

COUNTRY_TITLES = {
    "uruguay": "Uruguay",
    "argentina": "Argentina",
    "chile": "Chile",
    "georgia": "Georgia",
    "romania": "Romania",
    "south_africa": "South Africa",
    "england": "England",
    "wales": "Wales",
}


def detect_country_in_prompt(prompt):
    for name, pat in COUNTRY_PATTERNS:
        if pat.search(prompt):
            return name
    return None


def detect_country_in_headings(body):
    """Detect a country only from markdown heading lines or the first line."""
    lines = body.split("\n")
    candidates = []
    if lines:
        candidates.append(lines[0])
    candidates += [ln for ln in lines if ln.lstrip().startswith("#")]
    # Chilean/Chile appears in the overview heading "The Generations of Chilean Rugby"
    for ln in candidates:
        for name, pat in COUNTRY_PATTERNS:
            if pat.search(ln):
                return name
        if re.search(r"chilean", ln, re.I):
            return "chile"
        if re.search(r"georgian", ln, re.I):
            return "georgia"
    return None


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
GEN_IN_PROMPT = re.compile(r"gen(?:eration)?\s*(\d+)", re.I)


def gen_key(prompt, title):
    m = GEN_IN_PROMPT.search(prompt or "")
    if m:
        return int(m.group(1))
    m = re.search(r"gen(?:eration)?\s*(\d+)", title or "", re.I)
    if m:
        return int(m.group(1))
    return None


def first_heading(body):
    for ln in body.split("\n"):
        m = HEADING_RE.match(ln.strip())
        if m:
            return m.group(2).strip()
    return None


def section_title(prompt, body):
    fh = first_heading(body)
    m = GEN_IN_PROMPT.search(prompt or "")
    if m:
        n = m.group(1)
        if fh and re.search(r"gen", fh, re.I):
            return fh, True  # use heading, it's descriptive
        return f"Generation {n}", False
    if fh:
        return fh, True
    # fallback: first bold phrase or first sentence
    mb = re.search(r"\*\*(.+?)\*\*", body)
    if mb:
        return mb.group(1).strip(), False
    first_line = body.strip().split("\n")[0]
    return (first_line[:60] + ("..." if len(first_line) > 60 else "")), False


def demote_headings(body, levels=1):
    out = []
    for ln in body.split("\n"):
        m = HEADING_RE.match(ln)
        if m:
            hashes = m.group(1)
            new = "#" * min(6, len(hashes) + levels)
            out.append(f"{new} {m.group(2)}")
        else:
            out.append(ln)
    return "\n".join(out)


def remove_first_heading(body):
    lines = body.split("\n")
    for i, ln in enumerate(lines):
        if HEADING_RE.match(ln.strip()):
            del lines[i]
            # also drop an immediately following blank line
            if i < len(lines) and not lines[i].strip():
                del lines[i]
            break
    return "\n".join(lines).strip()


def split_at_first_heading(body):
    """Return (heading_title, text_after_heading), dropping any preamble."""
    lines = body.split("\n")
    for i, ln in enumerate(lines):
        m = HEADING_RE.match(ln.strip())
        if m:
            rest = "\n".join(lines[i + 1:]).strip()
            return m.group(2).strip(), rest
    return None, body


def continuation_sections():
    """Extract generation sections from follow-up conversation files."""
    secs = []
    srcs = []
    for p in CONT_FILES:
        if not p.exists():
            continue
        data = json.loads(p.read_text(encoding="utf-8"))
        convo = data[0] if isinstance(data, list) else data
        thread = linearize(convo["chat_messages"])
        for m in thread:
            if m["sender"] != "assistant":
                continue
            body = strip_prose(clean_text(m))
            if len(body) < 800:
                continue
            title, rest = split_at_first_heading(body)
            if not title or not re.search(r"gen", title, re.I):
                continue
            rest = demote_headings(rest, 1)
            secs.append({
                "title": title,
                "body": rest,
                "prologue": False,
                "used_heading": True,
                "gen": gen_key("", title),
                "meta": False,
            })
            srcs += extract_sources(m)
    return secs, srcs


# ---------------------------------------------------------------------------
# 4. Build the book structure
# ---------------------------------------------------------------------------

STOP_PROMPT = re.compile(
    r"document this conversation|readable book|what kind of document|"
    r"can we some how documen", re.I)

# Pure navigation / meta turns whose answers are not book content.
SKIP_PROMPT = re.compile(
    r"which country|want to continue now|next up|why combine|should we go next",
    re.I)


def is_meta_clarification(body):
    head = body[:400].lower()
    return (
        "you've just had" in head
        or "i suspect one of two things" in head
        or ("you meant" in head and "gen" in head)
    )


def build():
    convo = load_conversation()
    thread = linearize(convo["chat_messages"])

    # Pair each assistant message with the human prompt that preceded it.
    turns = []
    pending_prompt = ""
    for m in thread:
        if m["sender"] == "human":
            pending_prompt = clean_text(m)
        elif m["sender"] == "assistant":
            turns.append((pending_prompt, m))
            pending_prompt = ""

    chapters = []
    current_country = None
    chapter = None
    tucuman_section = None
    uruguay_prologue_done = False

    for prompt, msg in turns:
        if STOP_PROMPT.search(prompt or ""):
            break
        if SKIP_PROMPT.search(prompt or ""):
            continue

        body = strip_prose(clean_text(msg))
        if not body or len(body) < 40:
            continue

        srcs = extract_sources(msg)

        pc = detect_country_in_prompt(prompt or "")
        bc = detect_country_in_headings(body)
        cand = pc or bc

        # --- Tucuman: fold into Argentina as a closing section ---
        # Enter when named, or stay while inside Tucuman AND no real country
        # has surfaced yet. A real country (cand != tucuman/None) exits Tucuman.
        in_tucuman = cand == "tucuman" or (
            current_country == "tucuman" and cand is None
        )
        if in_tucuman:
            current_country = "tucuman"  # sticky until a real country appears
            if chapter is not None:
                chapter.setdefault("sources", []).extend(srcs)
            if tucuman_section is None:
                tucuman_section = {
                    "title": "The Interior: Tucum\u00e1n",
                    "chunks": [],
                }
                chapter["sections"].append(tucuman_section)
            title, used_heading = section_title(prompt, body)
            b = remove_first_heading(body) if used_heading else body
            b = demote_headings(b, 2)  # nest under the Tucuman H2
            sub = f"### {title}\n\n{b}" if used_heading else b
            tucuman_section["chunks"].append(sub)
            continue

        # --- Normal country switch ---
        if cand and cand != current_country:
            current_country = cand
            chapter = {
                "country": cand,
                "title": COUNTRY_TITLES.get(cand, cand.title()),
                "sections": [],
                "sources": [],
            }
            chapters.append(chapter)
            tucuman_section = None
            uruguay_prologue_done = False

        if chapter is None:
            # Nothing detected yet; assume Uruguay (the conversation opener).
            current_country = "uruguay"
            chapter = {"country": "uruguay", "title": "Uruguay",
                       "sections": [], "sources": []}
            chapters.append(chapter)

        chapter.setdefault("sources", []).extend(srcs)

        title, used_heading = section_title(prompt, body)
        b = remove_first_heading(body) if used_heading else body
        b = demote_headings(b, 1)

        # Uruguay prologue grouping: everything before the "continued history"
        # rugby arc goes under a single Prologue section.
        is_prologue = (
            chapter["country"] == "uruguay"
            and not uruguay_prologue_done
            and not re.search(r"continued history", prompt or "", re.I)
            and not re.search(r"amateur wilderness|first test", body, re.I)
        )
        if chapter["country"] == "uruguay" and (
            re.search(r"continued history", prompt or "", re.I)
            or re.search(r"amateur wilderness", body, re.I)
        ):
            uruguay_prologue_done = True

        chapter["sections"].append({
            "title": title,
            "body": b,
            "prologue": is_prologue,
            "used_heading": used_heading,
            "gen": gen_key(prompt, title),
            "meta": is_meta_clarification(body),
        })

    # --- Dedupe re-tried generations and order them ---
    # For each generation number, prefer a substantive (non-meta) answer and,
    # among those, keep the longest (drops truncated branches + clarifications).
    for ch in chapters:
        normal = [s for s in ch["sections"] if "chunks" not in s]
        special = [s for s in ch["sections"] if "chunks" in s]
        none_key = [s for s in normal if s.get("gen") is None and not s.get("meta")]
        buckets = {}
        for s in normal:
            if s.get("gen") is not None:
                buckets.setdefault(s["gen"], []).append(s)
        gens = []
        for k in sorted(buckets):
            cands = buckets[k]
            pool = [c for c in cands if not c.get("meta")] or cands
            gens.append(max(pool, key=lambda s: len(s["body"])))
        ch["sections"] = none_key + gens + special

    # --- Append follow-up continuation sections (e.g. Wales Gen 6/7) ---
    cont_secs, cont_srcs = continuation_sections()
    if cont_secs:
        wales = next((c for c in chapters if c["country"] == "wales"), None)
        if wales is not None:
            existing = {s.get("gen") for s in wales["sections"]
                        if "chunks" not in s}
            for s in sorted(cont_secs, key=lambda x: (x["gen"] is None, x["gen"])):
                if s["gen"] in existing:
                    continue
                wales["sections"].append(s)
                existing.add(s["gen"])
            wales.setdefault("sources", []).extend(cont_srcs)

    return chapters


# ---------------------------------------------------------------------------
# 5. Render markdown
# ---------------------------------------------------------------------------

def render(chapters):
    lines = []
    lines.append(f"% {BOOK_TITLE}")
    lines.append(f"% ")
    lines.append("")
    lines.append(f"# {BOOK_TITLE}")
    lines.append("")
    lines.append(f"*{BOOK_SUBTITLE}*")
    lines.append("")
    lines.append(
        "This book is assembled from a single long conversation exploring the "
        "generational history of rugby union, country by country. It preserves "
        "the narrative answers in the order they were told."
    )
    lines.append("")
    lines.append("\\newpage")
    lines.append("")

    for ch in chapters:
        lines.append(f"# {ch['title']}")
        lines.append("")

        # Uruguay prologue: wrap the prologue sections under one heading.
        prologue_sections = [s for s in ch["sections"] if s.get("prologue")]
        normal_sections = [s for s in ch["sections"] if not s.get("prologue") and "chunks" not in s]
        special_sections = [s for s in ch["sections"] if "chunks" in s]

        if prologue_sections:
            lines.append("## Prologue: The Setting")
            lines.append("")
            for s in prologue_sections:
                if s["used_heading"]:
                    lines.append(f"### {s['title']}")
                    lines.append("")
                lines.append(s["body"])
                lines.append("")

        for s in normal_sections:
            lines.append(f"## {s['title']}")
            lines.append("")
            lines.append(s["body"])
            lines.append("")

        for s in special_sections:
            lines.append(f"## {s['title']}")
            lines.append("")
            lines.append("\n\n".join(s["chunks"]))
            lines.append("")

        # Deduped per-chapter source list.
        seen = set()
        srcs = []
        for s in ch.get("sources", []):
            if s["url"] in seen:
                continue
            seen.add(s["url"])
            srcs.append(s)
        if srcs:
            lines.append("## Sources")
            lines.append("")
            for s in srcs:
                suffix = f" \u2014 {s['site']}" if s["site"] else ""
                lines.append(f"- [{s['title']}]({s['url']}){suffix}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def report(chapters):
    total = 0
    for ch in chapters:
        n = len(ch["sections"])
        chars = 0
        print(f"\n=== {ch['title']} ({n} sections) ===", file=sys.stderr)
        for s in ch["sections"]:
            if "chunks" in s:
                c = sum(len(x) for x in s["chunks"])
                print(f"  [special] {s['title']}  ({len(s['chunks'])} chunks, {c} chars)", file=sys.stderr)
            else:
                c = len(s["body"])
                tag = "PROLOGUE" if s.get("prologue") else "        "
                print(f"  {tag} {s['title'][:70]}  ({c} chars)", file=sys.stderr)
            chars += c
        total += chars
        uniq = len({s["url"] for s in ch.get("sources", [])})
        print(f"  --- chapter chars: {chars}; unique sources: {uniq}", file=sys.stderr)
    print(f"\nTOTAL chapters: {len(chapters)}, total chars: {total}", file=sys.stderr)


def main():
    chapters = build()
    md = render(chapters)
    OUT_MD.write_text(md, encoding="utf-8")
    report(chapters)
    print(f"\nWrote {OUT_MD} ({len(md)} chars)", file=sys.stderr)


if __name__ == "__main__":
    main()
