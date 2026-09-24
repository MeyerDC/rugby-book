# Copilot instructions — Rugby book project

This repo is a **book** assembled from a long rugby-history conversation: *Rugby Has No Class — A
Generational History of the Game, Country by Country.* It is prose, not software.

## Read this first
**Read `SUMMARY.md` §1–4, §6 and §7 before doing anything. Open §5 only at the entry for your
chapter.** `SUMMARY.md` holds the thesis, the house style, the recurring motifs, the chapter-by-chapter
map and the writing process. Do not read the whole book to get oriented: `SUMMARY.md` exists so you
don't have to.

## Project layout
- `chapters/NN-country.md`: **source of truth**; hand-edit these. Chapter = `#`, generation = `##`,
  subheads = `###`. Each chapter ends with a `## Sources` list.
- `notes/<country>.md`: per-country research. **The top of the file is the index**: the generation
  map and the status table. Older research sits below it; grep it, don't read it whole.
- `notes/<country>/genN-<slug>.md`: one research dossier per subplot. **Prose is written from these.**
- `drafts/NN-country.md`: the generation being drafted. Never draft in `chapters/`.
- `tools/verify_quotes.py`: checks that every dossier quote is really on its page.
- `book.md`: generated combined output (for the eventual PDF). Do not hand-edit.
- `combine_book.py`: rebuilds `book.md` from `chapters/`. Run after editing.
- `build_book.py`: original extractor from the Claude JSON export. **Retired; do NOT run it.** It
  regenerates `book.md` from the JSON and would overwrite hand-edits.

## How to write: the gated process (full detail in `SUMMARY.md` §7)
**Map the generations → plan the subplots → one subplot at a time → stitch → proofread → promote.**
Each ✋ gate is the author's to pass. Stop and wait at every one.

0. **Generation map → ✋ Gate 0.** A generation is the span in which one arrangement carries the game
   (who plays it, runs it, pays for it, and who it's played against). It begins and ends at **dated,
   hand-verified hinge events**. Generations are contiguous, with no overlaps and no silent gaps.
   Needed only for new or expanded countries.
1. **Subplot plan → ✋ Gate 1.** Each generation gets 3–5 subplots (the `###` sections). Each one
   answers part of the generation's question. Plan them all before researching any.
2. **For each subplot, one per session:**
   - **S1: research.** A **Sonnet** agent writes the dossier file (fact, url, exact quote, status). Then
     run `python3 tools/verify_quotes.py <dossier>` and retry only the failures by hand. It must pass
     the readiness test: a scene, a contemporary voice, the institution verified. **→ ✋ Gate 2.**
   - **S2: draft** into `drafts/` from the dossier only, with no searching. Gaps become `[TK: …]` and
     go back to S1.
   - **S3: claims check.** A **Sonnet** agent returns only the sentences that no dossier entry
     supports. **→ ✋ Gate 3**, and the subplot is LOCKED.
3. **Stitch** (cold open, joins, closing tease). Then an **Opus** proofread of the whole generation,
   then promote: add Sources, run `python3 combine_book.py`, and update the `SUMMARY.md` §5 entry.

**World Cups (from 1987):** every tournament the country played is its own subplot, covering its
preparation and every result, written in prose. Missed tournaments are accounted for too. The last
generation ends on a dated road to RWC 2027 in Australia, and predicts nothing. Detail in `SUMMARY.md` §2.

**Token budget:** load only the `SUMMARY.md` core, the notes index, the one dossier and the last two
paragraphs. Start a fresh session per subplot. The author approves by reading the files, so don't paste
them into chat. Run one agent at a time, and never resume a crashed one.

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
