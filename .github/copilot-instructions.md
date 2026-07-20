# Copilot instructions — Rugby book project

This repo is a **book** assembled from a long rugby-history conversation: *Rugby Has No Class — A
Generational History of the Game, Country by Country.* It is prose, not software.

## Read this first
**Always read `SUMMARY.md` before doing anything.** It holds the thesis, the house style, the
recurring motifs, the chapter-by-chapter map, and the full workflow. Do not read the whole book to
get oriented — `SUMMARY.md` exists so you don't have to.

## Project layout
- `chapters/NN-country.md` — **source of truth**; hand-edit these. Chapter = `#`, generation = `##`,
  subheads = `###`. Each chapter ends with a `## Sources` list.
- `notes/<country>.md` — per-country research cache (facts + sources). **Write prose from here.**
- `book.md` — generated combined output (for the eventual PDF). Do not hand-edit.
- `combine_book.py` — rebuilds `book.md` from `chapters/`. Run after editing.
- `build_book.py` — original extractor from the Claude JSON export. **Retired — do NOT run it**; it
  regenerates `book.md` from the JSON and would overwrite hand-edits.

## How to write a new generation (token-efficient loop)
Attach only: `SUMMARY.md`, the one `notes/<country>.md`, and the previous generation's closing
paragraphs. Never add the whole folder. Do **one generation per turn.**

0. **Map the generations first (new & expanded countries only)** — before any deep research, for a
   *new* country or one being *expanded* past its current last generation, identify the generation
   map: the named eras with year ranges (Gen 0 = origins/enclave, Gen 1+ forward; see `SUMMARY.md`
   §2). Do this as an **Explore** subagent digest. Then research each generation in-depth, one per
   turn. Skip this step for the existing countries already mapped in `SUMMARY.md` §5.
1. **Research (digest only)** — run it as an **Explore** or **investigator** subagent so raw search
   output stays out of the main thread. Ask for a compact fact brief (events, dates, people, turning
   points) + source links, no prose. Append the brief + links to `notes/<country>.md`.
2. **Write from the notes** — compose the generation in **story mode**, matching the house style in
   `SUMMARY.md` §2 and threading the motifs in §4. Open with a cinematic dated scene; close with a
   tease for the next generation.
3. Append new sources to the chapter's `## Sources`, then run `python3 combine_book.py`.

## Style rules (see SUMMARY.md §2 for detail)
- Novelistic "story mode," not bullet summaries.
- Bold date cold opens; generations as named eras with year ranges.
- Thread cross-country motifs (informal empire, cricket-club incubators, the amateur ideology, the
  coalfield thesis, the messiah reflex). One recurring lens — **rugby has no class; institutions do**
  — but **lead with the history** (matches, players, tours, tactics, institutions); class is a motif,
  not the subject.

## Status
Draft. No PDF yet. When leaving draft:
`pandoc book.md -o book.pdf --toc --top-level-division=chapter` (styling still TBD).

## Do not
- Do not run `build_book.py`.
- Do not add markdown files documenting your changes.
- Do not load the whole book or whole folder into context just to make a local edit.
