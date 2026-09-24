#!/usr/bin/env python3
"""Build the reading-music playlists on Spotify from notes/reading-music.md.

The notes already carry an exact Spotify track id for every selection, so no
text-matching service (Spotlistr and the rest) is needed or wanted: the ids go
straight to Spotify and land on the right recording every time.

Three commands, all stdlib only:

    python3 tools/spotify_playlists.py list
        Print every active set, its track count and total running time.

    python3 tools/spotify_playlists.py uris [--out DIR]
        Write one .txt of `spotify:track:...` lines per set. Paste a file into
        an empty playlist in the Spotify desktop app (click in the track area,
        not the search box, then Cmd-V) and the whole set goes in. No account
        setup at all.

    python3 tools/spotify_playlists.py push [--only TEXT] [--into LINK]
        Fill playlists through the Web API. Read the warning below first:
        creating a playlist is reported to be refused for Development Mode
        apps, so make the playlist by hand and pass --into its link.
        Re-running replaces its contents, so it stays in step with the notes.

WARNING about `push` (September 2026). Spotify's February 2026 changes locked
Development Mode down: an app needs the owner to hold Spotify Premium, one
client id per developer, five authorised users — and developers report that
`POST /me/playlists` now answers 403 for unverified apps, whatever the docs
list as available. Extended Quota Mode, which would lift that, is only granted
to organisations with 250k monthly active users. So `push` may not be able to
create anything. If it is refused, make the playlist by hand in the app and
run `push --only Uruguay --into <playlist link>`, which only writes items; if
that is refused too, the `uris` route needs no API at all and always works.

SETUP for `push` (once):
  1. https://developer.spotify.com/dashboard -> Create app. Any name.
     Redirect URI: http://127.0.0.1:8899/callback   (loopback; "localhost"
     is not accepted). Tick "Web API".
  2. export SPOTIFY_CLIENT_ID=<the client id from the dashboard>
  3. Run the command. A browser window asks you to authorise, once.
     The token is cached in ~/.config/rugby-book/spotify.json (chmod 600).

Notes on Spotify's February 2026 rules: a Development Mode app now requires a
Premium account, allows one client id per developer and up to five authorised
users. Playlist creation (POST /me/playlists) and item writes
(POST/PUT /playlists/{id}/items) are on the still-supported list.
"""

import argparse
import base64
import hashlib
import http.server
import json
import os
import pathlib
import re
import secrets
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request

REPO = pathlib.Path(__file__).resolve().parent.parent
NOTES = REPO / "notes" / "reading-music.md"
# Everything after this heading is earmarks, reservations and archived sets.
ACTIVE_ENDS_AT = "## Pieces earmarked for later chapters"
TRACK_LINK = re.compile(r"open\.spotify\.com/track/([A-Za-z0-9]{22})")
DURATION = re.compile(r"^(\d+):(\d{2})$")

REDIRECT_URI = "http://127.0.0.1:8899/callback"
SCOPES = "playlist-modify-private playlist-modify-public"
API = "https://api.spotify.com/v1"
CACHE = pathlib.Path.home() / ".config" / "rugby-book" / "spotify.json"


# ---------------------------------------------------------------- parsing


class Set:
    def __init__(self, chapter, heading):
        self.chapter = chapter
        self.heading = heading
        self.ids = []
        self.seconds = 0

    @property
    def name(self):
        return "Rugby: {} — {}".format(self.chapter, self.heading)[:100]

    @property
    def slug(self):
        text = "{}-{}".format(self.chapter, self.heading).lower()
        return re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:60]

    @property
    def runtime(self):
        return clock(self.seconds)


class Chapter:
    """Every set of one chapter, in book order, as a single playlist."""

    def __init__(self, chapter):
        self.chapter = chapter
        self.headings = []
        self.ids = []
        self.seconds = 0

    def add(self, item):
        self.headings.append(item.heading)
        self.ids.extend(item.ids)
        self.seconds += item.seconds

    @property
    def name(self):
        return "Rugby Has No Class: {}".format(self.chapter)[:100]

    @property
    def slug(self):
        return re.sub(r"[^a-z0-9]+", "-", self.chapter.lower()).strip("-")

    @property
    def runtime(self):
        return clock(self.seconds)

    @property
    def description(self):
        return "Reading music for the {} chapter: {} sets in book order, {} tracks, {}.".format(
            self.chapter, len(self.headings), len(self.ids), self.runtime
        )


def clock(seconds):
    if seconds >= 3600:
        return "{}:{:02d}:{:02d}".format(seconds // 3600, (seconds % 3600) // 60, seconds % 60)
    return "{}:{:02d}".format(seconds // 60, seconds % 60)


def group(sets, per):
    """Playlists to build: one per chapter (the default) or one per generation."""
    if per == "set":
        return sets
    chapters = {}
    order = []
    for item in sets:
        if item.chapter not in chapters:
            chapters[item.chapter] = Chapter(item.chapter)
            order.append(item.chapter)
        chapters[item.chapter].add(item)
    return [chapters[name] for name in order]


def parse(path=NOTES):
    """Read the active sets: chapter, heading and the table's track ids in order."""
    text = path.read_text(encoding="utf-8")
    cut = text.find(ACTIVE_ENDS_AT)
    if cut != -1:
        text = text[:cut]

    sets, chapter, current = [], None, None
    for line in text.splitlines():
        if line.startswith("## Chapter"):
            # "## Chapter 1 — Uruguay" -> "Uruguay"
            chapter = line.split("—")[-1].strip() if "—" in line else line[3:].strip()
            current = None
        elif line.startswith("### "):
            current = Set(chapter or "?", line[4:].strip())
            sets.append(current)
        elif line.startswith("|") and current is not None:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 6:
                continue
            found = TRACK_LINK.search(cells[-1])
            if not found:
                continue  # header row, or a prose link that is not a selection
            current.ids.append(found.group(1))
            stamp = DURATION.match(cells[-2])
            if stamp:
                current.seconds += int(stamp.group(1)) * 60 + int(stamp.group(2))
    return [s for s in sets if s.ids]


# ------------------------------------------------------------------ auth


def load_cache():
    try:
        return json.loads(CACHE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_cache(data):
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    os.chmod(CACHE, 0o600)


def post_form(url, fields):
    body = urllib.parse.urlencode(fields).encode()
    request = urllib.request.Request(url, data=body, method="POST")
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())


def authorise(client_id):
    """Authorization Code with PKCE. No client secret, no third-party service."""
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(64)).decode().rstrip("=")
    digest = hashlib.sha256(verifier.encode()).digest()
    challenge = base64.urlsafe_b64encode(digest).decode().rstrip("=")
    state = secrets.token_urlsafe(16)

    query = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": REDIRECT_URI,
            "scope": SCOPES,
            "code_challenge_method": "S256",
            "code_challenge": challenge,
            "state": state,
        }
    )
    caught = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 - required name
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            caught.update({k: v[0] for k, v in params.items()})
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<p>Authorised. Close this tab and go back to the terminal.</p>")

        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("127.0.0.1", 8899), Handler)
    threading.Thread(target=server.handle_request, daemon=True).start()

    url = "https://accounts.spotify.com/authorize?" + query
    print("Opening the browser to authorise. If nothing opens, visit:\n  " + url)
    try:
        import webbrowser

        webbrowser.open(url)
    except Exception:
        pass

    while not caught:
        pass
    server.server_close()

    if caught.get("state") != state:
        sys.exit("Authorisation state did not match; aborting.")
    if "error" in caught:
        sys.exit("Spotify refused authorisation: " + caught["error"])

    tokens = post_form(
        "https://accounts.spotify.com/api/token",
        {
            "grant_type": "authorization_code",
            "code": caught["code"],
            "redirect_uri": REDIRECT_URI,
            "client_id": client_id,
            "code_verifier": verifier,
        },
    )
    return tokens


def access_token(client_id):
    cache = load_cache()
    refresh = cache.get("refresh_token")
    if refresh:
        try:
            tokens = post_form(
                "https://accounts.spotify.com/api/token",
                {
                    "grant_type": "refresh_token",
                    "refresh_token": refresh,
                    "client_id": client_id,
                },
            )
            cache["refresh_token"] = tokens.get("refresh_token", refresh)
            save_cache(cache)
            return tokens["access_token"], cache
        except urllib.error.HTTPError:
            pass  # expired or revoked; fall through to a fresh sign-in
    tokens = authorise(client_id)
    cache["refresh_token"] = tokens["refresh_token"]
    save_cache(cache)
    return tokens["access_token"], cache


# ------------------------------------------------------------------- api


def api(token, method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(API + path, data=data, method=method)
    request.add_header("Authorization", "Bearer " + token)
    request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as error:
        detail = error.read().decode(errors="replace")
        raise SystemExit("Spotify API {} on {} {}\n{}".format(error.code, method, path, detail))


PLAYLIST_ID = re.compile(r"playlist[/:]([A-Za-z0-9]{22})")


def push(playlists, public, only, into=None):
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    if not client_id:
        sys.exit("Set SPOTIFY_CLIENT_ID first — see SETUP at the top of this file.")
    token, cache = access_token(client_id)
    known = cache.setdefault("playlists", {})

    wanted = [p for p in playlists if not only or only.lower() in p.name.lower()]
    if not wanted:
        sys.exit("Nothing matched --only.")

    if into:
        found = PLAYLIST_ID.search(into)
        if not found:
            sys.exit("--into wants a playlist link or id, e.g. https://open.spotify.com/playlist/…")
        if len(wanted) != 1:
            sys.exit("--into fills one playlist, so pair it with --only, e.g. --only Uruguay.")
        known[wanted[0].slug] = found.group(1)
        save_cache(cache)

    for item in wanted:
        playlist_id = known.get(item.slug)
        if not playlist_id:
            try:
                created = api(
                    token,
                    "POST",
                    "/me/playlists",
                    {
                        "name": item.name,
                        "public": public,
                        "description": getattr(
                            item,
                            "description",
                            "Reading music for Rugby Has No Class. {} tracks, {}.".format(
                                len(item.ids), item.runtime
                            ),
                        ),
                    },
                )
            except SystemExit as refusal:
                if "403" not in str(refusal):
                    raise
                sys.exit(
                    "Spotify refused to create the playlist (403). Development Mode apps are "
                    "reported to be blocked from creating playlists, and Extended Quota needs "
                    "250k monthly users.\n\nMake the playlist by hand in the app, then fill it:\n"
                    "  python3 tools/spotify_playlists.py push --only '{}' --into <playlist link>\n"
                    "If that is refused too, use the paste route: "
                    "python3 tools/spotify_playlists.py uris".format(item.chapter)
                )
            playlist_id = created["id"]
            known[item.slug] = playlist_id
            save_cache(cache)
            action = "created"
        else:
            action = "filled"

        uris = ["spotify:track:" + track for track in item.ids]
        # PUT replaces the contents, so re-runs stay in step with the notes.
        api(token, "PUT", "/playlists/{}/items".format(playlist_id), {"uris": uris[:100]})
        for start in range(100, len(uris), 100):
            api(
                token,
                "POST",
                "/playlists/{}/items".format(playlist_id),
                {"uris": uris[start : start + 100]},
            )
        print(
            "{:8} {:<62} {:>2} tracks  https://open.spotify.com/playlist/{}".format(
                action, item.name[:62], len(item.ids), playlist_id
            )
        )


# ------------------------------------------------------------- commands


def check_playable(sets, only=None):
    """Ask Spotify's embed endpoint whether each track actually plays.

    The track page's `restrictions:country:allowed` meta tags are unreliable: many
    perfectly playable tracks print none at all, so an empty list says nothing. The
    embed entity's isPlayable/playabilityReason is the one that settles it. Georgia
    Generations 0 and 4 were built on the wrong signal in September 2026 and had to
    be rebuilt; run this before trusting a set.
    """
    import concurrent.futures
    import json as jsonlib

    def one(item):
        tid, heading = item
        url = "https://open.spotify.com/embed/track/" + tid
        request = urllib.request.Request(url)
        request.add_header("User-Agent", "Mozilla/5.0")
        try:
            with urllib.request.urlopen(request) as response:
                page = response.read().decode("utf-8", "replace")
        except Exception as error:  # network hiccup, not a verdict
            return (tid, heading, None, "FETCH_FAILED: {}".format(error), "?")
        found = re.search(
            r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', page, re.S
        )
        if not found:
            return (tid, heading, None, "NO_DATA", "?")
        entity = jsonlib.loads(found.group(1))["props"]["pageProps"]["state"]["data"]["entity"]
        return (
            tid,
            heading,
            entity.get("isPlayable"),
            entity.get("playabilityReason"),
            entity.get("name"),
        )

    work = [
        (tid, item.heading if hasattr(item, "heading") else item.chapter)
        for item in sets
        if not only or only.lower() in (item.name or "").lower()
        for tid in item.ids
    ]
    blocked = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for tid, heading, ok, why, name in pool.map(one, work):
            if ok is not True:
                blocked.append((tid, heading, name, why))
    print("Checked {} tracks; {} not playable.".format(len(work), len(blocked)))
    for tid, heading, name, why in blocked:
        print("  {:38} {:34} {}  {}".format(heading[:38], (name or "?")[:34], why, tid))
    return blocked


def duplicates(sets):
    """The notes forbid reusing a composition; a repeated id is a certain breach."""
    seen, repeated = {}, []
    for item in sets:
        for track in item.ids:
            if track in seen:
                repeated.append((track, seen[track], item.heading))
            else:
                seen[track] = item.heading
    return repeated


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in [
        ("list", "print the playlists the notes define"),
        ("check", "ask Spotify whether every track actually plays"),
        ("uris", "write spotify:track: lists for pasting"),
        ("push", "create or update the playlists on Spotify"),
    ]:
        command = sub.add_parser(name, help=help_text)
        command.add_argument(
            "--per",
            choices=("chapter", "set"),
            default="chapter",
            help="one playlist per chapter (default) or one per generation",
        )
        if name == "uris":
            command.add_argument("--out", default=None, help="directory for the .txt files")
            command.add_argument(
                "--copy", help="also copy this playlist's lines to the clipboard, e.g. --copy Chile"
            )
        if name == "check":
            command.add_argument("--only", help="only playlists whose name contains this text")
        if name == "push":
            command.add_argument("--public", action="store_true", help="make them public")
            command.add_argument("--only", help="only playlists whose name contains this text")
            command.add_argument(
                "--into",
                help="fill a playlist you made by hand (its link or id), instead of creating one",
            )
    args = parser.parse_args()

    sets = parse()
    playlists = group(sets, args.per)

    if args.command == "list":
        for item in playlists:
            print(
                "{:<62} {:>3} tracks  {:>8}".format(item.name[:62], len(item.ids), item.runtime)
            )
            if args.per == "chapter":
                for part in sets:
                    if part.chapter == item.chapter:
                        print("    {:<56} {:>3}  {:>8}".format(
                            part.heading[:56], len(part.ids), part.runtime
                        ))
        print("\n{} playlists, {} sets, {} tracks.".format(
            len(playlists), len(sets), sum(len(s.ids) for s in sets)
        ))
        for track, first, second in duplicates(sets):
            print("REUSED {} in both '{}' and '{}'".format(track, first, second))
        return

    if args.command == "check":
        check_playable(sets, getattr(args, "only", None))
        return

    if args.command == "uris":
        out = pathlib.Path(args.out) if args.out else REPO / "notes" / "playlist-uris"
        out.mkdir(parents=True, exist_ok=True)
        for stale in out.glob("*.txt"):
            stale.unlink()
        for item in playlists:
            target = out / (item.slug + ".txt")
            target.write_text(
                "\n".join("spotify:track:" + track for track in item.ids) + "\n",
                encoding="utf-8",
            )
        print("Wrote {} files to {}".format(len(playlists), out))
        if args.copy:
            hits = [p for p in playlists if args.copy.lower() in p.name.lower()]
            if len(hits) != 1:
                sys.exit("--copy matched {} playlists; be more specific.".format(len(hits)))
            lines = "\n".join("spotify:track:" + track for track in hits[0].ids) + "\n"
            import subprocess

            subprocess.run(["pbcopy"], input=lines.encode(), check=True)
            print("Copied {} ({} tracks) to the clipboard.".format(hits[0].name, len(hits[0].ids)))
        print("Paste into an empty playlist in the desktop app: click the track")
        print("area (not the search box), then Cmd-V.")
        return

    push(playlists, args.public, args.only, args.into)


if __name__ == "__main__":
    main()
