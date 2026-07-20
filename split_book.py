#!/usr/bin/env python3
"""
Split the combined book.md into per-chapter files for easier editing.

- Front matter (title page + intro, everything before the first country
  chapter) -> chapters/00-front.md
- Each top-level chapter ("# Country") -> chapters/NN-slug.md, in order.

After this split, the chapter files are the source of truth you hand-edit.
Rebuild a combined book.md for Pandoc with:  python3 combine_book.py

Usage:
    python3 split_book.py
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK = HERE / "book.md"
CHAPTERS = HERE / "chapters"

H1 = re.compile(r"^# (.+?)\s*$")


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def main():
    if not BOOK.exists():
        sys.exit(f"error: {BOOK} not found")

    lines = BOOK.read_text(encoding="utf-8").splitlines()

    # Indices of all H1 lines. First H1 is the book title (part of front matter);
    # the real chapters start at the second H1.
    h1 = [i for i, ln in enumerate(lines) if H1.match(ln)]
    if len(h1) < 2:
        sys.exit("error: could not find chapter headings in book.md")

    CHAPTERS.mkdir(exist_ok=True)

    segments = []  # (index_prefix, filename, text)

    # Front matter: start .. first chapter H1 (the second H1 overall).
    front = "\n".join(lines[: h1[1]]).rstrip() + "\n"
    segments.append(("00", "front", front))

    chapter_starts = h1[1:]
    for n, start in enumerate(chapter_starts, start=1):
        end = chapter_starts[n] if n < len(chapter_starts) else len(lines)
        title = H1.match(lines[start]).group(1)
        text = "\n".join(lines[start:end]).rstrip() + "\n"
        segments.append((f"{n:02d}", slugify(title), text))

    # Write files (clear stale ones first).
    for old in CHAPTERS.glob("*.md"):
        old.unlink()

    written = []
    for prefix, slug, text in segments:
        fname = f"{prefix}-{slug}.md"
        (CHAPTERS / fname).write_text(text, encoding="utf-8")
        written.append((fname, text.count("\n") + 1))

    print(f"Wrote {len(written)} files to {CHAPTERS}/:", file=sys.stderr)
    for fname, nlines in written:
        print(f"  {fname:28s} {nlines:>6} lines", file=sys.stderr)


if __name__ == "__main__":
    main()
