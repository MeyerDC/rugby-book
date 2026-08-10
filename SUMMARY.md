# Book Summary & Continuation Guide

A reference primer for *Rugby Has No Class: A Generational History of the Game, Country by Country*.
Purpose: let a future session extend the book **without re-reading the whole thing**. Read this file
first, then open only the specific chapter you're editing.

---

## 1. What the book is

Assembled from a long Claude conversation tracing the generational history of rugby union,
country by country, told in long-form narrative **"story mode."** Only the assistant's prose is
included — the human prompts, model thinking, and tool calls were stripped out. Each country is a
**chapter**; each chapter is divided into **generations** (discrete eras with a year range).

**Purpose — lead with the history.** The book tells the **history of rugby in each country**: how the
game arrived, who carried it, the landmark matches, players, tours, rivalries, tactics and
institutions, and how each national game found its character. That history is the point.

**A recurring lens (one of several motifs — §4 — not the spine):**
> **Rugby has no class — institutions do.**
> A sport's class character in any country is not inherited from its founders; it is *produced* by
> the institutions that carry it and the communities those institutions define themselves against.

Class is a strong through-line and worth threading where it earns its place, but it is **a lens, not
the subject.** Lead with the history and let the class reading emerge from events — not the other way
round. (Several early chapters were written thesis-first; that's a legacy of the book's origin as a
class-question conversation, not a rule to keep repeating.)

---

## 2. House style — MATCH THIS when writing new material

- **Story mode:** immersive, novelistic narrative history, not bullet-point summary.
- **Cinematic cold open:** most generations open with a **bold date + a single scene**
  (e.g. "**5 October 1985.** A quiet Saturday in Buenos Aires…"), then pull back: "now let's go
  back and see where it came from."
- **Generations as discrete eras:** each has a year range and a *named theme* in the heading
  (e.g. "Generation 2: The Great Schism (1893–1895)").
- **Recurring cross-references:** thread comparisons between countries — the "informal empire,"
  cricket clubs as incubators of both codes, the amateur ideology, the coalfield thesis. New
  chapters should reference the established motifs (§4).
- **"What this generation leaves behind":** each generation closes by teasing the next.
- **Devices:** **bold** for emphasis, em-dashes, occasional *italics*, parenthetical asides that
  draw cross-country comparisons.
- **Dated snapshot, never relative time (must read the same in 2 years):** anchor every statement to
  an explicit date or year ("In July 2026…", "By 2023…", "As of the 2026 season…"), never to
  relative time ("currently", "right now", "yesterday", "this year", "recently"). Treat even the
  newest events as fixed points in a history, written in the past tense. Close a chapter's present-day
  edge on an explicitly dated snapshot ("Where things stood in mid-2026…") so it reads as a deliberate
  cutoff, not a claim about "now." Date forward-looking references ("toward RWC 2027 in Australia",
  not "next year's World Cup"). Avoid volatile facts (live league positions, this-window squad churn)
  unless hard-dated.
- **Heading levels:** chapter = `#`, generation = `##`, in-generation subheads = `###`.
- Each chapter ends with a `## Sources` list (deduped Markdown links).

**Generation numbering convention:** **Gen 0** = origins / pre-breakout era (usually the British
enclave phase). Then Gen 1+ move forward. Most countries run to Gen 6; South Africa, England, and
Wales run to Gen 7.

---

## 3. Files & workflow

```
rugby-book/
  book.md            # combined output (generated; used for the eventual PDF)
  chapters/          # SOURCE OF TRUTH — hand-edit these
    00-front.md      # title page + intro
    01-uruguay.md  02-argentina.md  03-chile.md  04-georgia.md
    05-romania.md  06-south-africa.md  07-england.md  08-wales.md
  notes/             # per-country research cache (facts + sources); write prose FROM here
    uruguay.md  argentina.md  chile.md  georgia.md
    romania.md  south-africa.md  england.md  wales.md  scotland.md
  drafts/            # rewrites-in-progress + archived pre-rewrite chapters
    NN-country.md                          # a rewrite being drafted (NOT in chapters/ —
                                           #   combine_book.py bundles every .md there)
    NN-country-superseded-old-chapter.md   # the pre-rewrite chapter, kept for fact-checking
  split_book.py      # book.md  -> chapters/   (one-time; already run)
  combine_book.py    # chapters/ -> book.md    (run after editing)
  build_book.py      # ORIGINAL extractor from the Claude JSON export (retired)
```

- **To edit:** change files in `chapters/`, then run `python3 combine_book.py` to rebuild `book.md`.
- **Do NOT re-run `build_book.py`** for edits — it regenerates `book.md` from the JSON export and
  would overwrite hand-edits. It's kept only as the extraction record. (It reads the export at an
  absolute path and can fold in follow-up conversations via its `CONT_FILES` list — that's how
  Wales Gen 6/7 got added.)
- Status: **draft, no PDF built yet.** When ready: `pandoc book.md -o book.pdf --toc
  --top-level-division=chapter` (styling still TBD).

---

## 4. Recurring motifs (reuse these threads)

- **Informal empire / cricket-club incubators:** British commerce (railways, nitrate, sugar, ports)
  seeded sport abroad; **cricket clubs were the incubators of both football and rugby** across South
  America.
- **The amateur ideology:** "amateurism" as a class weapon — used in England to exclude working-class
  players; inverted elsewhere (communist Romania *embraced* rugby *because* it was amateur).
- **The coalfield thesis (Wales):** Welsh rugby results track coal-employment graphs — the same shape.
- **The "messiah reflex" (Wales):** no durable system, only a recurring hope for a saviour coach.
- **Class is institutional, not inherent:** the same British origin produced an elite enclave in
  Uruguay and a Tier 1 national obsession in Argentina.

---

## 5. Chapter-by-chapter map

### 1. Uruguay — `01-uruguay.md`  (Gen 0–6)
(**Rewritten July 2026** — inside-out/no-villain voice matching the other rewrites, and the only
rewrite that *expanded* the chapter (398 → 1,124 lines) because the original was the book's thinnest;
`notes/uruguay.md` holds the REWRITE DESIGN and the per-generation adjudicated briefs.)
**Trap for future editors:** the old chapter opened on an **1880 newspaper quote** — the scrum as
"heads without shoulders, legs without bodies" — which the July 2026 archive pass recorded as
**NOT FOUND**. It is gone; the cold open is now the verified **18 July 1861 Confitería Oriental**
scene (Pickering, Hughes, MacLean founding the Montevideo Cricket Club). Do not reinstate the quote.

The **institutional thesis in its purest form**: the same British origin as Argentina, but rugby
stayed a marooned **elite Carrasco enclave**. Central engine is the 1900 fork — CURCC joins the AUF
and assimilates (→ football/Peñarol) while **MVCC refuses to be governed by non-British men** (→
rugby stays British). (Peñarol is *demoted* as a class-marker — its class coding is contested; the
fork does the work. Peñarol Rugby's modern return is kept only as Gen 6's closing irony.)
- **Gen 0 — The British Enclave (1842–1900):** Victoria CC → MVCC (1861); the 1880 first match; the
  fork. Sourced to Matthew Brown's elite-retreat thesis (the record is thin & British-authored).
- **Gen 1 — The Enclave Organizes (1900–1951):** half a century of drift among Carrasco schools/clubs;
  the game finally builds a skeleton (first Test 1948, Campeonato 1950, URU 1951).
- **Gen 2 — The Irish Brothers (1955–1971):** Stella Maris (1955); the Christian Brothers *choose*
  rugby (CB=rugby / Jesuit=football); Old Christians & the shamrock. Ethnicity broadens, class doesn't.
- **Gen 3 — The Mountain (1972–1988):** the Andes disaster (Flight 571); the Eucharist framing ties
  back to the Brothers' formation; the world learns Uruguay's name for the crash, not the rugby.
- **Gen 4 — Getting on the Map (1989–2003):** IRB entry; 1999 WC (Ormaechea); the 111–13 England
  reckoning — amateur base can't survive the pro era.
- **Gen 5 — The Plan (2007–2019):** the two missed World Cups → Estadio Charrúa + High Performance +
  Americas Rugby Championship = a system; the 30–27 Fiji win.
- **Gen 6 — The Branches Rejoin (2020–2026):** Peñarol Rugby pro (SLAR 2021, SRA 2023 & 2025);
  Namibia 2023; homegrown-only pride; RWC 2027 qual; dated mid-2026 Nations Cup snapshot.
- **Sourcing note:** Wikipedia is NOT cited (repo rule) — built on Brown/Toynbee, Ryan/SILAS, the
  Andes memoirs, club/institution sites, Americas Rugby News, Sudamérica Rugby. Wiki-only micro-facts
  are hedged in the prose.

### 2. Argentina — `02-argentina.md`  (Gen 0–6, + Tucumán coda)
Same British-enclave origin as Uruguay, but rugby became **Tier 1**. The counter-case that opens the
thesis.
- **The messy birth (1867–1874)** → institutionalisation.
- **Gen 0 — The British Enclave (1873–1964):** 91 years, no win over a touring side.
- **Gen 1:** the breakout; the "Pumas"; South African coaching influence (Izak van Heerden).
- **Gen 2 — the Porta generation:** Hugo Porta; deepening isolation (1971 political ban on tours).
- **Gen 3:** decline via the amateur "self-inflicted wound."
- **Gen 4:** the 2007 **World Cup bronze** "team that didn't exist" (no domestic pro league).
- **Gen 5:** the **Jaguares** and entry to the Rugby Championship — "the trap they were still in."
- **Gen 6:** the **diaspora** side; beating the giants; 2023 semi-final.
- **The Interior: Tucumán** (coda) — sugar mills not railways → **working-class, flag-burning** rugby;
  climax: Tucumán beats Buenos Aires' 19-title streak **13–9 (5 Oct 1985)**.

### 3. Chile — `03-chile.md`  (Gen 0–6)
Most **elite-coded** origin (nitrate mines, Valparaíso ports, **three English private schools**), yet
the **fastest transformation** in the sport. (**Rewritten July 2026** — inside-out/no-villain voice
matching SA/England/Wales/Scotland/Argentina; 1,050 → 468 lines; `notes/chile.md` holds the REWRITE
DESIGN, the per-generation briefs and the audit trail.)
- **Gen 0** The Ports and the Saltpetre (1892–1934) · **Gen 1** The Union and the First Tests
  (1935–1950) · **Gen 2** The Second Nation (1951–1971) · **Gen 3** The Mountain and the Map
  (1972–1989) · **Gen 4** The Wilderness (1990–2017) · **Gen 5** Selknam (2018–2023) · **Gen 6** The
  House on the Hill (2023–2026) — RWC 2023, the CARR, RWC 2027 qualification, the 18 Jul 2026 Georgia
  defeat, dated mid-2026 snapshot.
- **Traps for future editors** (corrected in the rewrite, do not reinstate): the first documented match
  is **Coronel–Concepción, 16 June 1892** (Sebastián Núñez, *The Chilean Times* 9 Jul 1892) — the
  traditional **1894 Iquique** origin has no document and is told as tradition, not record, so Gen 0 is
  **1892–**, not 1894–; **Mackay was the Valparaíso Artizan School (1857), founded for craftsmen of
  limited means** — do not flatten it into the "three expensive schools"; **Stade Français is
  French-colony, not British**; **Sporting (Viña, 1963) is a Universidad Católica de Valparaíso side**,
  not a British-school club; the **"sleeping giant" / "make rugby Chile's #2 sport" lines are
  unverified as Lemoine quotes** — never attribute them.

### 4. Georgia — `04-georgia.md`  (Gen 0–6)
The **control case**: the one country in this book where rugby did *not* arrive as a foreign
gentleman's possession, because the ground was not empty when it landed. (**Rewritten August 2026** —
the last chapter to get the treatment; 1,051 → 474 lines, 50 `###` subheads → 24, 8 first-person
intrusions → 0, 6 Wikipedia/Grokipedia citations → 0. `notes/georgia.md` holds the REWRITE DESIGN, the
per-generation briefs and the audit trail.)
- **Gen 0** Lelo Burti (**c.1200–1928**) · **Gen 1** The Armenian from Marseille (1928–1963) ·
  **Gen 2** The Soviet Machine (1964–1988) · **Gen 3** Independence and Ruin (1989–1996) · **Gen 4**
  The French Connection (1997–2006) · **Gen 5** The Billionaire (2007–2018) · **Gen 6** The Locked Door
  and the Scandal (2019–2026), closing on a dated mid-2026 snapshot.
- **Generation ranges fixed:** Gen 0 was "Antiquity–1927", a category rather than a range. Both bounds
  are now real — **c.1200** is Rustaveli's *Knight in the Panther's Skin*, the earliest datable
  reference to *burtaoba*; **1928** is the first failed attempt to introduce organised rugby.
- **The two set-pieces, and do not break the pair:** Gen 5 opens at **Bordeaux, 2007, 78 minutes** —
  Georgia four points down, over the Irish line, Denis Leamy getting his body under the ball, TMO "held
  up". Gen 6 opens at **Cardiff, 19 Nov 2022, 78 minutes** — Luka Matkava's penalty beating Wales
  13–12. Same minute, opposite outcome, fifteen years apart. Both are exact from the sources.
- **Traps for future editors — deliberately absent, do NOT reinstate:**
  - **"15 October 1959" and the "Tbilisi racecourse" founding scene.** The only source for the day and
    the racecourse is a **Geocities mirror**. Two better accounts describe *different* events — a
    session at the Hippodrome (*The Rugby Journal*) and a twenty-man club-forming meeting at the
    **Georgian Polytechnic Institute** producing **Qochebi** (Newport–Kutaisi; RugbyNetwork). Safe:
    **1959**, **~20 attendees**, **Jacques "Jako" Haspekian**, an Armenian from Marseille and a
    professional cyclist.
  - **"12 September 1989"** — Campion gives only "September 1989" for the first Test (Kutaisi, Georgia
    **16–3** Zimbabwe, **Liparteliani** captain, **Dzagnidze** scoring all the points).
  - **The 1999 Tonga repechage first leg "37–6"** — World Rugby's official match page gives the date
    and Teufaiva Stadium but renders **no score**.
  - The **1967 French trade-union XV**, the **1988 Tbilisi sevens** (the old chapter's turning point —
    nothing confirms it happened), and the **July 2022 win over Italy** (Wikipedia-only).
- **The European championship title total is deliberately uncounted** and this is settled, not
  deferred: **Rugby Europe's own championship page carries no honours list at all.** State the **2001**
  first win and the post-2006 pattern; give no total.
- **Gorgodze's caps: use World Rugby's 75.** It's Rugby says 52 (counting from a 2007 debut), other
  reports 71–72. The chapter uses the governing body's own figure and flags the discrepancy.
- **The 1949 Soviet ban is the key to Gen 1.** Rugby was declared "a game not relevant to the
  principles of the Soviet people" under the campaign against cosmopolitanism. The old chapter framed
  1928/1940/1948 as an inexplicable triple failure; each simply landed where there was no room for it.
- **The doping case has CONCLUDED** — outcomes published **12 May 2026**, seven banned (up to 11 years,
  incl. the team doctor at 9), and the **Georgian Rugby Union itself accepted a misconduct charge**.
  The GADA-collusion detail is **Planet Rugby's**, not in World Rugby's own statements.

### 5. Romania — `05-romania.md`  (Gen 0–6)
The **"Oaks" (Stejarii).** The communist state embraced rugby **because it was amateur** — inverting
England's logic.
(**Rewritten July 2026** — inside-out/no-villain voice matching the other rewrites; 1,222 → 643 lines;
`notes/romania.md` holds the REWRITE DESIGN, the no-wiki re-verification passes and the audit trail.)
- **Gen 0** The Ball from Paris (c.1900–1930) · **Gen 1** The Works Team (1931–1948) · **Gen 2**
  Because It Was Amateur (1949–1969) — the real breakthrough, **5 June 1960, Romania 11–5 France**,
  the reigning Five Nations champions (wins also 1962, 1968) · **Gen 3** The Door That Did Not Open
  (1970–1989) — the Oaks at full height (24–6 Wales 1983; 28–22 Scotland's 1984 Grand Slam side; 15–9
  at Cardiff 1988), closing on the **literal two bullets — Durbac 23 Dec 1989, Murariu 24 Dec 1989**,
  both Steaua, both shot in the revolution · **Gen 4** The Delay (1990–2001) — the regime's fall +
  1995 professionalism → 134–0 · **Gen 5** The Ranking That Lied (2002–2017) · **Gen 6** Not Here as a
  Tourist (2018–2026).
- ⚠️ **Sourcing debt:** the Romania `## Sources` block still carries **7 Wikipedia links** (two of them
  legitimately cited as *negative* evidence for the debunked unbeaten record; the other five need
  replacing). See `notes/romania.md` "STILL WIKI-ONLY OR UNSOURCED" for the facts that are hedged on
  purpose — do not harden them.
- **Fact-checked July 2026** — see `notes/romania.md` for the verified brief and the errors corrected.
  Two traps for future editors: **1974 was NOT the first win over France** (1960 was), and the
  **"25-match unbeaten world record" is fabricated** (wiki-only; real record Cyprus 24 / NZ 23). The
  chapter now debunks it in Gen 3 — do not reinstate it.
- **Ceaușescu did not take power until March 1965.** The decision to keep rugby was **Gheorghiu-Dej's**
  (led 1947–65). Do not attribute the late-1940s adoption to Ceaușescu — the chapter used to, in four
  places.

### 6. South Africa — `06-south-africa.md`  (Gen 0–7)
The state used rugby to build **not a class but a race** — until a boy from the township of Zwide lifted
the trophy twice. (Rewritten from scratch July 2026 — no-wiki sourcing, perspectives braided from
inside; `notes/south-africa.md` holds the full fact base and audit trail.)
- **Gen 0** Gog's Game and the Two Beginnings (1861–1889) · **Gen 1** The Conqueror's Game (1890–1948)
  · **Gen 2** The Machinery (1948–1969) · **Gen 3** No Normal Sport (1959–1979; the non-racial game,
  same clock re-run) · **Gen 4** Barbed Wire (1980–1989) · **Gen 5** One Jersey (1990–1995; the
  convergence) · **Gen 6** The Professionals (1995–2017) · **Gen 7** The Inheritance (2018–2026):
  **Siya Kolisi**, back-to-back World Cups.

### 7. England — `07-england.md`  (Gen 0–7)
The birthplace; where **"amateur" was invented as a class weapon** — told as **two unions, each from
inside**: the Southern (RFU) view and the Northern (league) view. (Rewritten from scratch July 2026 —
no-wiki sourcing, both codes braided as parallel histories; `notes/england.md` holds the full fact
base, the binding REWRITE DESIGN, and the per-generation audit trail.)
- **Gen 0** The Boys' Game, and the Story They Told About It (1820s–1870): folk football legislated
  off the streets, the 1845 written rules, the 1863 Blackheath walkout — and the **Webb Ellis myth
  told as a myth** (Bloxam's hearsay, certified by the Old Rugbeian inquiry appointed **July 1895**,
  a month before the schism) · **Gen 1** One Game, Two Englands (1871–1892): the RFU's 21 southern
  founding clubs, Raeburn Place, the North's cup boom, **Dicky Lockwood**, the 1886 amateur laws,
  the 1888 tour and **Jack Clowes** · **Gen 2 — The Great Schism (1893–1895)**: the two hotel rooms
  told from inside — Westminster Palace (broken-time voted down 282–136; **Arthur Budd's** creed)
  and the **George Hotel, 29 Aug 1895** · **Gen 3** Two Games Behind One Wall (1895–1945): league
  builds a complete game (Challenge Cup, 13-a-side 1906, the All Golds, Wembley 1929) beside union's
  (Twickenham, the 1920s Slams, France expelled 1931) — and the **1943/44 service matches league won
  under union rules** · **Gen 4** The Long Cold War (1946–1994): **Odsal 1954 (102,569)**, boot
  money, **Beaumont exiled over his own book**, the amateur-league bans (**Pilgrim 1993, Ady Spencer
  1994** → Parliament) · **Gen 5 — Open: The Hundred-Year Debt (1995–2003)**: Paris, **26 Aug 1995**,
  99 years and 3 days after the George Hotel; the club-vs-country war and Richmond's collapse; **Jason
  Robinson**, a Wigan league man, scores England's only try in the 2003 final · **Gen 6** All the
  Money in the World (2004–2019): 2007 & 2019 finals lost, 2011 Queenstown, the 2015 host-pool exit
  and **Sam Burgess** (the cross-code switch that didn't take), Eddie Jones, the Premiership
  inflating · **Gen 7 — The Bill (2020–2026)**: **Steve Thompson**, the CTE litigation with **1,000+
  players suing both codes at once**, Worcester/Wasps/London Irish dead, the RFU crisis — and
  **Beaumont returning as interim chairman**; dated mid-2026 snapshot (SA 45–21 England, 4 July 2026)
  toward RWC 2027 in Australia.

### 8. Wales — `08-wales.md`  (Gen 0–7)
**The answer to England** — started identically, but the **coalfield** made it the people's game.
(**Rewritten July 2026** — same Gen 0–7 spine, new no-wiki sourcing and inside-out/no-villain narration,
matching the South Africa and England rewrites; `notes/wales.md` holds the full per-generation fact base,
the "REWRITE DESIGN" rules and the audit trail.)
- **Gen 0** the vicar, the village game, the colleges (1603–1880) · **Gen 1** the union, the coalfield,
  the Gould affair (1881–1899) · **Gen 2** first golden era & the song (1900–1914) · **Gen 3** the long
  winter (1919–1968) · **Gen 4** the second golden era (1969–1979) · **Gen 5** the pits close
  (1980–2002) · **Gen 6 — The Bargain (2003–2019)** (regional cull vs golden decade) · **Gen 7 — The
  Deepest Valley (2020–2026)** (governance crisis, the record 18-Test losing run, regions cut 4→3;
  dated mid-2026 snapshot toward RWC 2027).
- **Traps for future editors** (corrected in the rewrite, do not reinstate): the **four three-quarter
  system is a mid-1880s Cardiff/Frank Hancock innovation**, not a 1900s one; the **"six shillings a
  match"** league figure is unverifiable — dropped; **Phil Bennett's 1977 speech is disputed/possibly
  apocryphal** — never quote it as fact; the **Ruddock "player power" revolt is unsupported** by
  reliable sources; the **2015 "kick for the corner" was England's decision**, not Wales's; Wales's
  first win over South Africa was **29–19** (1999); Wales took **no wooden spoons in the 1980s** (the
  bottom-place years were 1989–95).

### 9. Scotland — `09-scotland.md`  (Gen 0–7)
The **establishment-vs-Borders** case: the same 1871 origin that gave England a class weapon gave
Scotland **two rugbies inside one union** — the elite FP-club/private-school/university game, and the
mill-town **Border** counter (Melrose = Sevens 1883; the Border League = world's oldest, 1901). The
Borders are the chapter's engine (a *region within*, parallel to Wales's coalfield and Argentina's
Tucumán). Runs the 7-gen tier.
- **Gen 0** the school game in embryo (1854–1872) · **Gen 1** the challenge issued — first-ever
  international 1871, the union, Sevens (1871–1883) · **Gen 2 — The Border Rising** (1884–1924) · **Gen
  3** Murrayfield & the golden twenties — 1925 Grand Slam (1925–1945) · **Gen 4** the amateur hangover
  (1946–1979) · **Gen 5 — The Walk** — 1984 & 1990 Grand Slams, Sole's walk (1980–1994) · **Gen 6 — The
  Two-Club Trap** (1995–2019): professionalism guts the club/district base; 1998 & 2007 culls leave the
  Borders with **no pro team**; 1999 last Five Nations title; Glasgow's 2015 Pro12; RWC pool exits.
- **Gen 7 — The Reboot (2020–2026)**: the "golden generation" (Russell, Duhan van der Merwe, Tuipulotu)
  beats England at will (7 Calcutta Cups in 9 years; 2021 Twickenham) and Glasgow win the 2024 URC — yet
  three straight RWC pool exits and no Six Nations title expose the **two-club ceiling** (vs Ireland's
  four provinces). Dated mid-2026 cutoff toward RWC 2027 in Australia.

---

### 10. Ireland — `10-ireland.md`  (Gen 0–6)
**The institution that refused to divide when the country did.** The IRFU's remit predates the 1921
partition by forty-two years, and after partition it kept a single team for all thirty-two counties.
Rugby is the **only major Irish team sport organised on an all-island basis**. (Written from scratch
August 2026 — the book's tenth chapter and its first new country since Scotland; 496 lines of prose.
`notes/ireland.md` holds the fact base, the chapter design block and the verification log.)
- **Gen 0** Dublin University and the Two Unions (1854–1879) · **Gen 1** The Four Provinces (1879–1920)
  · **Gen 2** Partition, and the Union That Did Not Split (1921–1947) · **Gen 3** Ravenhill, and the
  Anthem Wars (1948–1969) · **Gen 4** The Troubles (1970–1994) · **Gen 5** Professionalism and the
  Provinces (1995–2008) · **Gen 6** The Best Team in the World, and the Quarter-Final (2009–2026),
  closing on a dated mid-2026 snapshot.
- **⭐ THE BOOK'S ONLY CONTROLLED EXPERIMENT (Gen 1).** Liam O'Callaghan's *Rugby in Munster* gives two
  cities in one province, same sport, same decade, same British-derived origin, diverging permanently
  on one variable. **Limerick** got **Sunday junior fixtures from the late 1880s** (Saturday being a
  working day), which "facilitated the expansion of rugby in the parishes and working class areas of
  Limerick's inner city." **Cork** did not: "Sunday rugby could have taken off in Cork too **if there
  had been Godfathers in the senior clubs to organise it; but there were not**." A century later
  Limerick's game is inner-city and Cork's belongs to the professions in the wealthy suburbs. *Not the
  founders — the fixture list.* Sits alongside **Tucumán** and the **Borders**.
- **⭐ THE ANSWER TO SCOTLAND AND WALES (Gen 5).** Both chapters measure their failures against
  "Ireland's four provinces." In fact the **IRFU drew up advanced plans to disband Connacht** at the end
  of 2002/03 and was **stopped from outside** by the *March on Lansdowne Road*, January 2003. Scotland
  cut four districts to two; Wales went five regions → four → three; **Ireland attempted the identical
  economy at the identical moment and lost.** Its four provinces have since won **seven European Cups**
  (Ulster 1999, Munster 2006/2008, Leinster 2009/2011/2012/2018). The model world rugby admires began
  as an **underfunded default** — "In 1996 the provinces were an also ran."
- **The all-island spine, and its cost.** 1874's split was about **selection**, not religion — Belfast
  formed a rival *union*, not a rival country. Ravenhill bought 1923 (**£2,380**, nine acres); Ulster
  given **two of five** selection seats; a 1930s anthem protocol of deferring to the local anthem. Then
  **1954**: Republic-based players refused to take the field until *God Save the Queen* finished, the
  IRFU moved all internationals to Dublin, and **no senior international was played in Northern Ireland
  from 1954 until 2007** — **fifty-three years**. The union kept one team by removing half the island
  from its fixture list. The chapter refuses both sentimental readings.
- **Gen 4 is the strongest section.** April 1987: **Nigel Carr, David Irwin and Philip Rainey**, driving
  Belfast→Dublin for Ireland training, were caught by the IRA landmine at **Killeen** that killed **Lord
  Justice Maurice Gibson and his wife Cecily**; Carr never played again. **That bombing is why Ireland
  had no anthem at RWC 1987** — *Amhrán na bhFiann* "wasn't deemed a suitable song" — which produced the
  **Rose of Tralee** farce at Athletic Park, which produced **Ireland's Call** (Phil Coulter, 1995).
  Also: the **1972 Five Nations abandoned**, the only time ever, after Scotland and Wales refused to
  travel; and England turning up in **1973** to a five-minute ovation, with **John Pullin**'s "We may
  not be any good, but at least we turn up."
- **⚠️ VERIFY BEFORE PRINT — see the verification log at the end of the chapter.** Chiefly: the **2026
  Triple Crown scoreline** (draft uses **41–21** to agree with `09-scotland.md`; one summary says
  43–21 — **correct both chapters together** if wrong); the **1948 try-scorers**; the **Croke Park
  43–13**; and the **2006 Munster final date**. Deliberately omitted as unverified: the 1954 names
  (McCarthy, Hogan, "the Salute", "eleven players") and the **1982 Triple Crown**.

---

## 6. How to add a new generation or chapter

**For a new country (or one expanded past its current last generation): map the generations first** —
establish the full generation outline (named eras + year ranges) before researching, then work
generation-by-generation (see §7 Step 0).

1. Write it in the matching `chapters/NN-*.md` file (or a new `NN-country.md`), matching the house
   style in §2 and threading the motifs in §4.
2. Keep the `## Sources` block at the very end of the chapter; add new links to it.
3. Run `python3 combine_book.py` to rebuild `book.md`.
4. If a new country: use the next `NN` prefix and add it in reading order.

**Rewrite protocol** (used for SA, England, Wales, Argentina, Uruguay, Chile, Romania — and next for
Georgia): record a **REWRITE DESIGN** block in `notes/<country>.md` → draft into
`drafts/NN-country.md` → fact-checklist the draft against the old chapter (the old chapter is a
checklist, never a source of text) → `git mv` the old chapter to
`drafts/NN-country-superseded-old-chapter.md` and the draft into `chapters/` → `python3
combine_book.py` → update this file's §5 entry.

**Open threads:**
- ✅ **Georgia is done** (August 2026) — all nine chapters are now in the rewritten voice.
- ✅ **Ireland is written** (August 2026) — see §5.10. The book now has **ten chapters** and no unwritten country on its list.
- **Sourcing: the book is now at ONE Wikipedia citation**, down from **20** before the August 2026
  no-wiki pass. The survivor is deliberate — a records page in Romania cited *against itself* as
  negative evidence for the debunked unbeaten streak, and labelled as such in its Sources block.
  **Do not remove it**; deleting it would delete the evidence for the debunk. Grokipedia, Keith Prowse
  and Facebook are gone repo-wide. The passes are recorded in `notes/scotland.md`, `notes/romania.md`
  and `notes/georgia.md`.
- **Facts left knowingly unsourced by that pass** (hedge in prose, do not re-harden):
  - the **£20m SRU debt** figure (Scotland Gen 6) — no non-wiki source exists at all;
  - the **Caledonia Reds' 1996 formation** as the North & Midlands district;
  - Romania's **13–12 / Gareth Davies drop goal** in 1979 — the *uncapped "Wales XV" billing* is now
    sourced to a contemporary matchday programme, but the score is not;
  - the **Antim Cup's 2002** start date;
  - Georgia's **1999 Tonga first leg "37–6"** — World Rugby's official match page renders no score;
  - Georgia's **Haspekian date and venue** — see §5.4.
- Argentina's **Belgrano Athletic** Gen 0 facts remain wiki-only with no working citation (hedge or
  re-source).

---

## 7. Research workflow (keep context, spend few tokens)

The AI does **not** need the whole book to write the next generation. Each turn only needs:
**(a)** this `SUMMARY.md` (style + motifs), **(b)** the previous generation's closing paragraphs
(the handoff), and **(c)** a compact research brief. That's a few thousand tokens, not the whole book.

**Golden rules**
- Attach *specific files* (`SUMMARY.md`, the one chapter, the one `notes/` file) — never the whole
  folder. Every file in context is re-paid every turn.
- Do **one generation per turn.**
- **Separate research from writing** (below) so web searches don't fire mid-composition.
- **Cache research in `notes/<country>.md`** so you never look the same thing up twice; write prose
  from the notes, not from live search.

**Step 0 — map the generations (new & expanded countries only).** Before any per-generation
research, for a *new* country or one being *expanded* past its current last generation, identify the
generation map first: the named eras with year ranges, following the Gen 0 = origins/enclave → Gen 1+
convention in §2 (most countries run to Gen 6/7). Run this as an **Explore / investigator** subagent
and record the outline at the top of `notes/<country>.md`. Then work the two-step loop below one
generation per turn, researching each generation in-depth. **Skip this step for the existing eight
countries already mapped in §5.**

**Two-step loop per generation**
1. **Research (digest only).** "Research [country] rugby [year range]. Return a compact bullet brief —
   events, dates, people, turning points — plus source links. No prose." Run this as an **Explore /
   investigator subagent** so the raw search dumps stay out of the main thread; it returns only the
   brief. Append the brief + links to `notes/<country>.md`.
2. **Write (from the brief).** "Using `notes/<country>.md` and the house style in `SUMMARY.md`, write
   Gen N in story mode. Thread the motifs; end with a tease for Gen N+1." No searching this turn.
3. Append the new sources to the chapter's `## Sources`, then `python3 combine_book.py`.

**Prompt template**
```
# New/expanded country only — do this first:
Step 0: map the generations for <Country> as a subagent — return the named eras + year ranges only
(Gen 0 = origins/enclave, Gen 1+ forward). Record the outline atop notes/<country>.md.

# Then, one generation per turn:
Context: SUMMARY.md (style + motifs) + notes/<country>.md. Continuing <Country>, writing Gen N.
Previous gen ended: "<paste last 1–2 paragraphs of Gen N-1>"

Step 1: research Gen N (<year range>) as a subagent — return a compact fact brief + source links only.
Then I'll say "write it" and you compose Gen N from the brief, matching the house style.
```
