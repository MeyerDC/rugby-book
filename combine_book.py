#!/usr/bin/env python3
"""
Reassemble chapters/*.md (in filename order) into a single book.md.

This is the inverse of split_book.py. Edit the per-chapter files, then run
this to regenerate the combined book.md used for building the PDF.

Usage:
    python3 combine_book.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHAPTERS = HERE / "chapters"
BOOK = HERE / "book.md"


def main():
    files = sorted(CHAPTERS.glob("*.md"))
    if not files:
        sys.exit(f"error: no chapter files in {CHAPTERS}/")

    parts = [f.read_text(encoding="utf-8").rstrip() for f in files]
    BOOK.write_text("\n\n".join(parts) + "\n", encoding="utf-8")

    print(f"Combined {len(files)} files -> {BOOK}", file=sys.stderr)
    for f in files:
        print(f"  {f.name}", file=sys.stderr)


if __name__ == "__main__":
    main()
