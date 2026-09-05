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
- **Proofread each chapter before promotion.** The France pass (Aug 2026) caught **seven** factual or
  logical errors that the per-generation audits missed — a New Zealander implied to be French, three
  arithmetic slips ("eleven years earlier" for twelve, "eighty years" for sixty, "two decades" for
  twelve), a self-contradiction across two generations ("three" knockout wins where an earlier section
  said "the second time"), a statistic inflated by repetition, and a closing line contradicted two
  sentences later. **Automated greps do not find these; reading the whole chapter does.**
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
enclave phase). Then Gen 1+ move forward. **Count the generations, don't read the top number** —
"runs to Gen 7" means *eight* generations, Gen 0 through 7. Seven-generation chapters (Gen 0–6):
Uruguay, Argentina, Chile, Georgia, Romania, Ireland, Tonga. **Eight-generation chapters (Gen 0–7) are the
book's most common tier**: South Africa, England, Wales, Scotland, France, Fiji, Samoa, Italy. **Nine (Gen 0–8):**
New Zealand, and Australia when it lands — the two chapters of Section 4 that answer each other, and
the book's longest spine.

---

## 3. Files & workflow

```
rugby-book/
  book.md            # combined output (generated; used for the eventual PDF)
  chapters/          # SOURCE OF TRUTH — hand-edit these
    00-front.md      # title page + intro
    01-uruguay.md  02-argentina.md  03-chile.md  04-georgia.md
    05-romania.md  06-south-africa.md  07-england.md  08-wales.md
    09-scotland.md  10-ireland.md  11-france.md  12-new-zealand.md
    13-australia.md  14-fiji.md  15-samoa.md  16-tonga.md  17-italy.md
  notes/             # per-country research cache (facts + sources); write prose FROM here
    uruguay.md  argentina.md  chile.md  georgia.md  romania.md
    south-africa.md  england.md  wales.md  scotland.md  ireland.md
    france.md  new-zealand.md  australia.md  fiji.md  samoa.md  tonga.md  italy.md
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
  a hundred years almost to the day after the George Hotel (29 Aug 1895 — three days *short* of the
  century; the chapter itself has this right, this index line had it backwards); the club-vs-country war and Richmond's collapse; **Jason
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

### 11. France — `11-france.md`  (Gen 0–7)
**Where rugby stopped being English and became a region's property.** The game arrived by the same
channel as everywhere else in this book — British commerce, here **wine traders in Bordeaux from 1888**
— then went **up the Garonne into the rural south-west** and was taken over by miners, farmers, tanners
and stockmen. By the 1920s it was working-class, paid under the table, and violent, and the unions that
had invented amateurism as a class weapon **expelled France for it**. (Written August 2026, chapter 11,
opening **Section 4: The Game That Left Home**; 530 lines of prose, the book's longest chapter.
`notes/france.md` holds the fact base, the design block and the proofreading record.)
- **Gen 0** The British in Le Havre and Paris (1872–1892) · **Gen 1** The Parisian Game (1893–1920) ·
  **Gen 2** Up the Garonne (1921–1930) · **Gen 3** Expelled (1931–1946) · **Gen 4** Monsieur Rugby
  (1947–1962) · **Gen 5** Flair and Castagne (1963–1987) · **Gen 6** Open (1988–2007) · **Gen 7** The
  Richest League in the World (2008–2026), closing on a dated mid-2026 snapshot.
- **⭐ THE ORIGIN MYTH IS CONTESTED, AND THE REASON IS INSTITUTIONAL (Gen 0).** What was played at
  **Le Havre from 1872** was not rugby but "**la combination**", a deliberate hybrid of rugby and
  association football — and **Pascal Charitas** (*Études Normandes*, via Persée) shows the club's own
  statutes **marginalised both codes in favour of the hybrid from 1872 to 1894**, to stop the club
  splitting into sections. France's oldest club played neither code cleanly for twenty-two years
  because a committee decided an undivided club was stronger. Charitas quotes **Jean-Pierre Bodis**:
  "rugby arrives in France at Le Havre in 1872. **This is false!**"
- **⭐ THE MECHANISM WAS JOBS, NOT CASH (Gen 2).** **Philip Dine**, via Christopher Thompson's *H-France
  Review*: "teams recruited top players from other towns by **promising them jobs in local businesses
  and industry**". The RFU's 1886 laws banned precisely this, in more detail than they banned cash, and
  drove twenty-two northern clubs out in 1895 — see `07-england.md`. France did it at regional scale,
  in the open, and called itself amateur.
- **⭐⭐ THE FFR HAD RUGBY LEAGUE ABOLISHED BY VICHY (Gen 3).** **Décret n° 5285, signed by Pétain on
  19 December 1941**, dissolved the Ligue française de rugby à XIII, **prohibited the sport entirely**,
  **seized its assets**, and ended **155–159 clubs**. The FFR's own president **Albert Ginesty** and
  honorary president **Paul Voivenel** pushed for it; Dine records that Vichy found union's "**amateur
  and ruralist values**" fitted its programme and acted "**with the ready cooperation of that sport's
  grateful officials**". The code was **forbidden its own name until the Cour de cassation dismissed
  the FFR's case on 4 June 1993 — fifty-two years.** *England's RFU used bylaws in 1895; the FFR used a
  collaborationist state.*
- **⭐ BÉZIERS WAS WON BY RESEARCH, NOT BRUTALITY (Gen 5).** **David Wozniak** (*Études Héraultaises*)
  asks how a team from a town "**plongée dans la grande crise viticole des années 1950**" became the
  world reference, and answers "**la recherche et l'innovation**": touchline movement analysis, a
  physiotherapist, a **1983 altitude camp**, and **players selecting the team by secret ballot**.
  France's **1977 Grand Slam** — same fifteen players, no tries conceded — was won playing Béziers' way.
  **Do not reduce Béziers to *la castagne*.**
- **The chapter's through-line is power:** Béziers' secret ballots and the **1968 Grand Slam won "in
  self-management"** → **Ferrasse** governing the FFR alone for **23 years** → **Laporte** convicted of
  corruption in December 2022. *"French rugby has spent a hundred and thirty years oscillating between
  the most democratic instincts in the sport and the most concentrated power in it."*
- **⚠️ VERIFY BEFORE PRINT — see the verification log at the end of the chapter (11 items).** Chiefly:
  the **2011 final (8–7)** and **2023 quarter-final (29–28)**, carried without a page read; **Stade
  Toulousain's five 1920s titles**; the **Palmié–Clerc case**, corroborated across French rugby media
  but not from an official disciplinary record; and the **AS Lagny** page (the "Nazi Germany and fascist
  Italy" characterisation, attributed rather than asserted).
- **Hedged, never asserted:** **Le Havre 1872** (given as "the standard answer" and immediately
  contested); **Racing (1882)/Stade Français (1883)** — the text says "the early 1880s"; the **USFSA**'s
  founding — "from 1887"; the **four Grand Slams 1997–2004** — a count and a span, not a year list.

### 12. New Zealand — `12-new-zealand.md`  (Gen 0–8)
**The country where rugby had no class — and spent a century and a half arguing about who was holding
it instead.** The game arrived by the same British channel as everywhere else, but was carried by
provincial unions, country clubs and men who moved towns for work, so it never acquired a class
character; the fault lines it did produce were **race** and **ownership**. (Written August 2026, the
book's first nine-generation chapter and its longest spine; 789 lines of prose. `notes/new-zealand.md`
holds the fact base, the design decisions, the retrieval map and the proofreading record.)
- **Gen 0** The Game in Somebody's Luggage (1870–1888) · **Gen 1** The Natives (1888–1902) · **Gen 2**
  The Originals and the All Golds (1903–1919) · **Gen 3** The Invincibles and the Colour Bar
  (1920–1948) · **Gen 4** No Maoris, No Tour (1949–1969) · **Gen 5** The Tour (1970–1986) · **Gen 6**
  Open (1987–2007) · **Gen 7** The Best Team in the World (2008–2019) · **Gen 8** The Bill
  (2019–2026), closing on a dated **18 July 2026** snapshot toward RWC 2027.
- **⭐ THE SPINE IS OWNERSHIP, AND IT RUNS IN EVERY GENERATION** (author decision, August 2026 — the
  class question is settled in a paragraph and cannot carry a chapter). Before 1892 there is no owner
  at all; the **1888 Natives** — a private, largely Māori venture — invent the black jersey, the silver
  fern, the haka and the name before a national union exists; **Ellison** then moves the motion that
  makes the union adopt them (**27 April 1893**); **Baskerville's 1907 professionals** are threatened
  with life bans; the union spends its **Māori players** to keep the South African fixture; the
  **Cavaliers** go anyway in 1986; the **World Rugby Corporation** nearly buys every player in 1995;
  **central contracting** answers it; and in **2022 the twenty-six provinces vote to sell** a share of
  the commercial rights to Silver Lake.
- **⭐⭐ THE ROWLAND HILL THROUGH-LINE — set it up in Gen 1 and land it in Gen 3.** The RFU secretary
  who **refereed the Natives at Blackheath (16 Feb 1889)**, rejected McCausland's first apology and
  **dictated the second** on pain of barring RFU clubs from playing the tourists, is **in the chair at
  the 1924 Imperial Rugby Conference**, refusing to let New Zealand's remit on professionalism be
  discussed at all — while the three colonial unions sit there **affiliated to the RFU rather than to
  the IRB**. Ellison's own words are the chapter's thesis: Hill's real error was **"refereeing at all
  in that game; he being the most important official of the English Rugby Union and the father of the
  team pitted against us."**
- **⭐ THE CLASS ARGUMENT IS A FIXTURE LIST, NOT AN ASSERTION.** Greymouth, 1875: the club's season
  included **"a 'Banks and Lawyers' versus 'All Corners' game, which extended over two days"** and a
  match against the **Fire Brigade**; Auckland, 1873, sorted men by weight and birthplace ("Thirteen
  Colonials" v "Eight Outsiders"; over 10st 10lb counted as heavy). Same rulebook as England's 1886
  laws — no institution with an interest in keeping the two sides apart.
- **⭐ THE CLOSING LOOPS, all verified.** **Otago**, which walked out of the founding meeting in 1892
  rather than accept a central authority, was **lent $200,000 and sent a change manager in 2012**,
  having been unable to pay a **$5,000 entry fee to a tournament it was hosting**. And **David Kirk** —
  one of the two All Blacks who refused the 1986 Cavaliers tour, and the captain who lifted the 1987
  World Cup — is **chair of NZR**, arriving from the **presidency of the Players' Association**, and
  sacked Scott Robertson in January 2026.
- **The women's game is threaded, not appended:** the **women's NPC was cancelled in 2010 to save
  money, in a World Cup year**; the Black Ferns won that World Cup and the competition was reinstated;
  **Farah Palmer** took the **Māori seat** on the NZR board in 2016; and on **12 November 2022** the
  Black Ferns beat England **34–31** at Eden Park before **a record 42,000+**.
- **Sourcing note — the retrieval map is in `notes/new-zealand.md` and will save the next session
  hours.** ✅ **`rugbymuseum.co.nz` is wide open to curl** and reproduces **A. C. Swan's 1948 history**,
  **Greg Ryan's *Forerunners of the All Blacks* (1993)** and contemporary newspaper text, plus a dated
  **"On This Day"** archive (thinning after ~2018). ✅ **RNZ** carries the modern chapter. ❌
  **nzhistory.govt.nz and teara.govt.nz 403 both curl and WebFetch.** ❌ **Papers Past returns HTTP 200
  with an Incapsula block page as the body** — *any agent quoting Papers Past is fabricating.*
- **Traps for future editors — deliberately absent, do NOT reinstate:** the **"All Backs" printer's
  error** (the Museum lists it among "incorrect rumours"; the first published use of "All Blacks" is
  **the Natives, mid-1889**); **Monro as sole founder** (the Museum itself says "introducing the game
  and as co-founder"); and the claim that the Natives were **"the first to play in a black uniform"**
  (the Napier report has them in black three months earlier — only the haka claim is made).
- **⚠️ VERIFY BEFORE PRINT — see the open items at the end of `notes/new-zealand.md`.** Chiefly the
  **2011 final (8–7)**, which `11-france.md` also carries **without a page read**; the **2015 final**,
  the **2019 semi-final** and the **Invincibles' match count**, all deliberately left unstated; the
  **1987 final** given as "by twenty points" per the NZRU's own history; and **two cross-chapter
  conflicts to settle together** — **Bob Deans's age at death** (`08-wales.md` says "twenty-one") and
  the **Originals' record** ("34 of 35" in Wales, "31 of 32 before Paris" in France).

### 13. Australia — `13-australia.md`  (Gen 0–8)
**The control case against New Zealand — same colonial origin, opposite outcome, and the variable is a
schoolmaster.** New Zealand's game was carried by provincial unions and country clubs and acquired no
class character; Australia's was carried by two associations of private schools in two cities and
acquired one immediately. **Both codes are braided the whole length of the chapter** (as `07-england.md`
runs the RFU and the Northern Union), because in Australia **league won** — it is the winter game of the
two states that *are* Australian rugby, and a union-only chapter would describe the smaller code and call
it the country. (Written August 2026; 21,000+ words, the book's longest chapter, and its second
nine-generation spine.)
- **Gen 0** The Oxford Hotel and the Schools (1858–1899) · **Gen 1** Messenger's Wage (1900–1914) ·
  **Gen 2** The Ten-Year Hibernation (1919–1932) · **Gen 3** The Union Forms (1933–1961) · **Gen 4** The
  Tour and the Ceiling (1962–1978) · **Gen 5** The Ella Brothers, and the Origin (1979–1991) · **Gen 6**
  Two Wars in One Year (1992–2003) · **Gen 7** Four Codes, One Market (2004–2019) · **Gen 8** The Host
  (2020–2026), closing on a dated **18 July 2026** snapshot — *the same afternoon `12-new-zealand.md`
  closes on.*
- **⭐⭐⭐ THE SOURCE BASE IS THE AUSTRALIAN DICTIONARY OF BIOGRAPHY, AND IT IS WIDE OPEN TO CURL.**
  `adb.anu.edu.au` — peer-reviewed, authored, dated, and indexed by occupation (35 rugby union players,
  28 league players, administrators of both codes). It carried most of this chapter. **Use it first for
  any Australian chapter work.** See the retrieval map in `notes/australia.md`.
- **⭐⭐⭐ THE SPINE: IN AUSTRALIA THE INSTITUTION IS A HEADMASTER.** The schools chose the code, in four
  cities, and the football followed every time: **Newington** (Sydney, 1860s — its first headmaster
  introduced *Australian rules*); **Hale School** (Perth, 1878–85, which switched *away* and killed rugby
  in WA); the **Queensland GPS** (Brisbane, 1880s, driving out the Victorian game); and the Queensland
  GPS again, **playing rugby league from 1920 to 1928**.
- **⭐⭐ THE RIVAL CODE WAS INVENTED BY A RUGBY SCHOOL OLD BOY IN A CRICKET CLUB (Gen 0).** ADB on
  **Tom Wills** — Rugby School, captain of its cricket XI, secretary of the Melbourne Cricket Club — and
  his letter to *Bell's Life in Victoria*, **10 July 1858**, calling on cricketers to take up a winter
  game, from which Australian Rules was drawn up. **The book's cricket-club-incubator motif produced
  Australia's rival code**, and that is why union is a two-city game.
- **⭐⭐ THE CLASS FACT IS THE INSTITUTION'S OWN (Gen 0).** The AAGPS's own history: "**Sydney Boy's High
  School applied for membership in March 1894, but they were not admitted until 14 February, 1906.**"
  Print the two dates and add nothing.
- **⭐⭐ THE ARC: MESSENGER → ELLA.** 1907, **Dally Messenger** (boatbuilder's son, Double Bay *Public*
  School, no institution behind him) takes **£180** and union expels him — then **fourteen Wallabies**,
  including their Olympic-final captain, are expelled after a **1909** charity series against the
  Kangaroos. 1984, **Mark Ella** (La Perouse, **Matraville High**, a state school, one sportsmaster named
  **Geoff Mould**) turns the money down, scores a try in all four Grand Slam Tests and retires at 25.
- **⭐ AND IT INVERTS IN GEN 8.** Rugby Australia bought **Joseph Suaalii** *out of* rugby league for a
  home World Cup — and Rugby Australia's own announcement says he "made his name in both sports growing
  up, playing for **the Kings School**". **The King's School, Parramatta**, which played Newington in
  **1870** and helped found the AAGPS in **1892**. 154 years, the same pipeline. *This is the chapter's
  last argument — do not blunt it.*
- **Cross-chapter links established:** two Australians in **Scotland's 1925 Grand Slam** three-quarter
  line (Johnny Wallace and Ian Smith — `09-scotland.md` does not mention it); **Ron McAuliffe's
  shift-workers' Sunday football** in Brisbane is the **Limerick mechanism** of `10-ireland.md` Gen 1;
  and the **1949 Bledisloe win** is the other end of New Zealand's "Black Day" (⚠️ Australia's 11–6 win
  came **twelve hours before** the Johannesburg defeat, not after — this was corrected in proof).
- **⚠️ TRAPS — deliberately absent, do NOT reinstate.** **"The first Aboriginal Wallaby"** for **Lloyd
  McDermott** — both the World Rugby Museum and the ABC hedge to "one of the earliest/first", and Cec
  Ramalli is named earlier elsewhere; and the tour he refused was **1963**, not 1962. **"First pool exit
  since 1987"** for 2023 — 1987 was a **semi-final**; 2023 was the **first ever**. **Jack Ross of Nudgee
  and Canon Morris of Churchie** as the named leaders of the 1928 Queensland revival — plausible and
  widely repeated, but sourced only to the bot-blocked `qld.rugby`; the chapter uses **Thomas Welsby**
  and **Tommy Lawton**, who are in the ADB. And the **Bledisloe Cup "from 1931"** — ADB puts Australia's
  first win in **1934**; the cup's inception date is unverified.
- **⚠️ SOURCING DEBT.** **Trove is closed and dangerously so** — HTTP 200 with a bot-challenge body to
  curl, access-denied to WebFetch, while search engines index and quote its article pages. **Any agent
  quoting Trove is fabricating.** The whole Rugby Australia estate (`australia.rugby`, `qld.rugby`,
  `classicwallabies.com.au`, `nsw.rugby`) sat behind a Vercel bot checkpoint throughout; `rugby.com.au`
  itself answers. **Peter Horton's two IJHS articles** — the scholarly spine for Gen 0–3 — are
  **cited from their abstracts only**; both full texts are closed (paywalled, and the JCU repository
  copies are "Restricted to Repository staff only"). The abstracts are open and were worth having:
  Horton 2012 supplies Queensland's first formal match, **27 May 1882**, played "**as an addendum, to a
  game of Melbourne rules football**" between two clubs that "**both primarily played the Victorian
  game**" — and rugby as the colony's premier code seven years later; Horton 2009 dates the first
  formal club to "**circa 1865**", backing this chapter's refusal to name one. Facts hedged on purpose and not to be hardened: the **IRB's 1948
  invitation** as the trigger for the 1949 ARFU; the **first Sydney club** (Sydney FC 1865 v Sydney
  University, the 1863 date unevidenced); the number of clubs at the **Oxford Hotel, 28 July 1874**; and
  the **blue-and-maroon 1899 jerseys**.



### 14. Fiji — `14-fiji.md`  (Gen 0–7)
**The country where a colonial governor tried to install a class and the institutions underneath the
game refused to carry it — and where the sorting happened on race instead, before rugby arrived.**
Opens **Section 5: The Church and the Export**. (Written August 2026, **proofread September 2026**;
743 lines, Gen 0–7, the book's most common tier. `notes/fiji.md` holds the fact base, the spine, the
retrieval map, the hedged-facts list and the proofreading record.)
- **Gen 0** The Constabulary Ground (1874–1912) · **Gen 1** Two Unions, One Colony (1913–1938) ·
  **Gen 2** Barefoot (1939–1954) · **Gen 3** The Colony Leaves (1955–1976) · **Gen 4** The Short Game,
  and the Coup (1977–1991) · **Gen 5** Open, and the Leak (1992–2006) · **Gen 6** The Body Trade
  (2007–2019) · **Gen 7** The Boat (2020–2026), closing on a dated **18 July 2026** snapshot —
  *the same afternoon `12-new-zealand.md` and `13-australia.md` close on.*
- **⭐⭐⭐ THE SPINE IS THE DIRECT CONTROL CASE AGAINST `13-australia.md`.** Governor **Sir Everard Im
  Thurn** "believed that there were **two classes of Fijians** … **the chiefs as thinkers and
  overseers, the commoners as manual labourers**," and built **Queen Victoria School** at Nasinu on the
  English public-school model — gazetted 17 Nov 1905, opened **3 Jan 1907 with 32 boys**, and **by 1910
  admitting only the sons of chiefs**, because headmaster **J. B. Thomson** held that "a chief's son is
  far more intelligent than the son of a commoner." QVS won the **first Deans Trophy in 1939** and
  became one of the two great nurseries — **and no class ever formed**. Australia's headmaster
  succeeded; Fiji's failed. The variable is what stood outside the school gate: in Sydney an old boys'
  club that existed to keep a man among his own kind, in Fiji a **village** where the club, the
  congregation and the kin group are one body of people.
- **⭐⭐⭐ THE DIVISION THAT DID TAKE WAS BUILT BEFORE RUGBY ARRIVED, AND NOT BY RUGBY.** Gordon kept
  indigenous Fijians off the plantations and imported **60,965 indentured labourers, 1879–1916**
  (Close-Barry, ANU Press). The Methodist mission split into **separate Fijian and Indo-Fijian branches
  in 1901**. Rugby then made a European union (**1913**), a "native competition" (**1914**) and a
  **Fiji Native Union (1915), affiliated not merged**; soccer's controlling body was the **Fiji Indian
  Football Association from 1938**. Rugby merged in **1945**, soccer desegregated in **1961–62**, and
  **neither changed who plays what.** *An institution does not have to be a sporting institution to
  give a sport its character* — the chapter's stated correction to the rest of the book.
- **⭐⭐ THE BOOK'S TITLE IS QUOTED BACK AT IT BY A PEER-REVIEWED SOURCE.** Stewart-Withers, Sewabu and
  Richardson (*Journal of Sport for Development*, 2017): "**rugby in Fiji is not bound by class …
  where even the poorest can participate**." Same paper: **up to 500 Fijians on professional contracts
  abroad**; **50+ in France's top two divisions**; **F$18.54m of rugby remittances in 2006 = 11% of all
  workers' remittances**; French academies in Fiji where "**contracts can be poor or non-existent, so
  athletes are vulnerable and at risk of exploitation**"; and "**no regulatory framework**" at home.
- **⭐⭐ RUGBY IS NOT FIJI'S ONLY BODY TRADE AND NOT ITS LARGEST — TELL THEM AS ONE.** Kanemasu et al.,
  *International Migration* (2017): peacekeeping from **1978**, **1,040 a year**, more per capita than
  any nation, **US$300m+ since 1978**; **British Army from 1961/62**, peak intake **490 in 2001/02**,
  suspended **2009** after the coup, **10 in 2014/15**, **2,740 since 1998/99**; PMSCs from **2003** and
  **4,000 Fijians in Iraq in 2006**. Their term: a "**muscle trade**" on core–periphery terms.
- **⭐⭐⭐ THE LANDING — DO NOT BLUNT IT.** In **2026** Fiji reached the top table (the inaugural
  **Nations Championship**, twelve teams) and played **all three of its "home" matches in Britain** —
  Cardiff City Stadium (4 July, Wales 39–24), the Hill Dickinson Stadium (11 July, England 73–8) and
  **Murrayfield (18 July, Scotland 33–17, Fiji leading 17–7 at half-time)**. The FRU's own release
  calls them "home" fixtures on "a unique journey across the Northern Hemisphere." Twelve months
  earlier Fiji had beaten **Scotland 29–14 in Suva**. *The country that exports its players had
  exported its home ground.* The championship's own format sends Europe south in July; Australia's July
  fixtures were in Australia.
- **Cross-chapter links established:** Fiji's **first Test was against Samoa at Apia, 18 Aug 1924**, 7am
  around a tree, 6–0 — hand it to ch. 15, and the Tonga leg to ch. 16; the **Deans Trophy was donated by
  the NZ Māori side that toured in 1938** (`12-new-zealand.md`); **Paddy Sheehan**, a Dunedin plumber and
  former **Otago** captain, founded the union in 1913 (`12-new-zealand.md` Gen 0); the **1987 coup and
  Western Samoa on standby** is already in `12-new-zealand.md` Gen 6; **Nantes 2007** is in
  `08-wales.md` Gen 6; **Kamaishi 2019** is in `01-uruguay.md` Gen 5; and the **1954 drawn series in
  Australia** is the other end of the **69-year** gap closed at Saint-Étienne on 17 Sept 2023.
- **⚠️ THE CRICKET MOTIF IS INVERTED HERE, ON THE UNION'S OWN AUTHORITY.** The FRU explains why no rugby
  was played outside Suva before 1939: "**almost every suitable ground already has a concrete cricket
  pitch at the centre**." Elsewhere the cricket club hatched the winter game; in Fiji the cricket square
  physically blocked it.
- **⚠️ HEDGED ON PURPOSE — see `notes/fiji.md` "STILL UNSOURCED".** The **cibi's** origin story (Ratu
  Bola, 1939) — the FRU's own page has the heading and **no text**, so it is told as a story, not a
  document; the **1987 quarter-final score/date**; the FRU's claim that the **1952 tour saved the ARU
  from bankruptcy** (attributed, not asserted); the **IRB membership year** (1986 vs 1987 — "the
  mid-1980s"); **Deans Trophy title totals** (sources disagree outright — first-win years only); the
  **1939 match count**; and **Kuruvoli's points breakdown** in 2023.
- **Sourcing note — the retrieval map in `notes/fiji.md` will save the next session hours.** ✅
  **`fijirugby.com` is wide open to curl** and its `/corporate/history/` page is a dated chronology
  1884–2006 that carried Gen 0–5. ✅ **ANU Press** (`press-files.anu.edu.au`) serves open-access
  peer-reviewed monographs — **Close-Barry's *A Mission Divided*** is the church spine. ✅
  **`sportanddev.org`** hosts the full JSFD PDF (⚠️ its text layer has lost inter-word spacing —
  quotes must be respaced by hand). ✅ **`eprints.worc.ac.uk`** serves the Kanemasu/Molnar **abstracts**
  even where PDFs are 401, and serves the **PMSC paper in full**. ✅ Frontiers, RNZ, *The Fiji Times*.
  ❌ **`tandfonline.com` 403s** — "Chiefs, warriors and rugby players" (2025) is exactly on topic and
  was never read, so it is **not cited**. ⚠️ **`rugbymuseum.co.nz` has only three Fiji entries and
  does not carry the 1939 tour** — do not assume the New Zealand source base covers Fiji.
- **All 38 source URLs were hand-checked for HTTP status** (August 2026); three BBC `feeds.bbci.co.uk`
  links and an ESPN Scrum link were dead or 403 and were replaced.


### 15. Samoa — `15-samoa.md`  (Gen 0–7)
**The book's cleanest natural experiment: one people, cut in half by three European powers in 1899, and
the two halves now play different football codes.** (Written August 2026, **proofread September 2026**; 584 lines, Gen 0–7.
`notes/samoa.md` holds the fact base, the retrieval map, the hedged-facts list and the proofreading
record.)
- **Gen 0** Lotu (1830–1919) · **Gen 1** The Brothers and the Tree (1920–1938) · **Gen 2** The Long
  Absence (1939–1961) · **Gen 3** Mr Rugby (1962–1986) · **Gen 4** Cardiff (1987–1995) · **Gen 5** The
  Diaspora Team (1996–2010) · **Gen 6** The Union and the Players (2011–2019) · **Gen 7** Twenty-Fourth
  (2020–2026), closing on a dated **18 July 2026** snapshot — *the fourth chapter to close on that
  afternoon.*
- **⭐⭐⭐ THE SPINE IS THE 1899 PARTITION.** The **Tripartite Convention, 2 December 1899**, gave
  **Upolu and Savai'i** to Germany (then New Zealand) and **Tutuila and Manu'a** to the United States,
  for Pago Pago. **No Samoan signed it.** The western half plays rugby; the eastern half plays American
  football. Same people, same language, same *fa'amatai*, same church — everything held constant except
  the flag. **Tighter than Limerick and Cork, tighter than Tucumán, tighter than the Borders.**
- **⭐⭐⭐ AND THE BORDER PROVED ITSELF IN 1918, BEFORE EITHER SPORT ARRIVED.** The **SS *Talune***
  docked at Apia on **7 November 1918** and the New Zealand administration waved it in; **about 8,500
  Samoans died in two months — between a fifth and a quarter of the population** (RNZ, quoting Damon
  Salesa). Forty miles east the US naval commandant quarantined American Sāmoa and **nobody died**.
  Te Papa records the detail that lands it: Apia's requests to Wellington were rejected, "but **the
  Administration also refused American aid when assistance from Eastern Sāmoa was offered**."
- **⭐⭐ THE CARRYING INSTITUTION IS THE VILLAGE, AND ITS PROTOTYPE IS THE PASTOR.** Meleisea: "**When a
  village decided to become Christian they built a church and a house for a teacher or pastor, and
  began to contribute to the church by supporting the pastor with food and services.**" *A Samoan
  village collectively maintains a chosen man so he can act on its behalf* — the *faifeau* in 1830,
  the six Vaiala men on the radio in 1970, the fares to Cardiff in 1991, the boy at a French academy in
  2026. **The section's two words, church and export, name one institution.** And its consequence is
  the chapter's hardest point: **the village's interest and the country's interest are not the same**,
  which is why no reform in Apia can stop the drain.
- **⭐⭐⭐ MICHAEL JONES IS THE SECTION'S PERFECT STORY AND HE BELONGS TO SAMOA.** From **World Rugby's
  own Hall of Fame page**: "**After a solitary cap for Samoa**, Jones switched allegiance to New
  Zealand in time for the inaugural Rugby World Cup in 1987. In the opening match against Italy, his
  debut, **Jones became the first player to score a try**." Then: "his **refusal to play on Sundays on
  religious grounds** restricted him to three appearances" at RWC 1991, and "**he was not considered**"
  for 1995. Then "**he coached Samoa at two Rugby World Cups**." *The first try in World Cup history,
  scored by a Samoan for New Zealand, in a tournament Samoa was not invited to, by a man the church
  cost two World Cups.*
- **⭐⭐ THE MARISTS CHOSE THE CODE.** Two Marist priests reached Falealupo on **25 May 1845**; the
  **Marist Brothers brought rugby in 1920**; the **Apia Rugby Union, Vaiala Ulalei and the first Test
  all landed in 1924** — four years from first ball to first cap. Same motif as Uruguay's Christian
  Brothers and Ted Larkin's Marist schools in `13-australia.md`.
- **⭐⭐⭐ THE LANDING, AND IT IS BRUTAL.** Samoa **lost its RWC 2027 place to Chile** — a 32–32 "home"
  leg at **America First Field, Salt Lake City** and a 31–12 defeat at Viña del Mar (`03-chile.md`
  carries the Chilean side; match its figures) — then took **the twenty-fourth and last place** on a
  **13–13 draw with Belgium in Dubai, 18 November 2025**. In 2026 the world split: Fiji and Japan went
  up into the **Nations Championship**, Samoa and Tonga into the **second-tier World Rugby Nations
  Cup** (the twelve who had to qualify). **All three of Samoa's July 2026 "home" matches were played in
  Chile** — including a "home" fixture against Georgia **in the same stadium where Chile had knocked
  them out ten months earlier**. And the *Samoa Observer* published the squad of 32 by location: **NZ
  13, France 6, Australia 4, UK 2, Japan 2, other 2 — and Samoa 3.** *Two of those three scored two
  tries each in the same match.* Do not blunt it.
- **⚠️ THE BAN IS THE CHAPTER'S BIGGEST SOURCING HOLE AND IT IS FLAGGED IN THE PROSE.** ABC Pacific's
  caption says rugby "was banned in Samoa for several decades … but returned in the 1950s." **A caption
  and a headline are the entire basis.** The chapter says so explicitly and builds nothing on it.
- **⚠️ Also hedged:** **Black Saturday's date** (Te Papa 29 Dec 1929; others 28 Dec — the chapter
  follows Te Papa and says so); the **2017 insolvency** (the Japan Times report is behind a JavaScript
  challenge and was never read — **not cited**); **Poyer's quarantine** (US-side accounts, attributed);
  and the **1920 Marist date** (centenary framing, not a primary document).
- **⚠️ TRAPS — deliberately absent, do NOT reinstate.** **"Peter Fatialofa the piano mover"** — the
  sources say **furniture remover**. **"56 times more likely to reach the NFL"** — folkloric; use
  **Uperesa's 28**, with her own qualification that it is a calculation for a film based on one
  season's rosters. And **no list of Samoan-eligible players capped elsewhere** — every list found was
  wiki-derived; the argument runs on Michael Jones, Pat Lam's testimony and the squad-location table.
- **Sourcing note — retrieval map in `notes/samoa.md`.** ✅ **ABC Pacific's centenary coverage
  (Sept 2024) is the single best Samoan-voiced rugby history online** — Mapusua, Momoisea, Patu, Senio
  and Leilua all quoted; use it first. ✅ **`nus.edu.ws`** serves **Malama Meleisea's** history chapter
  (⚠️ it 403s on repeat requests within the hour). ✅ **Te Papa** and **RNZ** for 1918 and the Mau.
  ✅ **Duke University Press posts a free PDF of Lisa Uperesa's *Gridiron Capital* introduction** — the
  scholarly source for American Sāmoa. ✅ **Sky Sports match pages carry a six-match form guide** that
  reconstructed Samoa's whole 2025–26 record — and mark all three 2026 Nations Cup fixtures "(h)".
  ❌ `samoaglobalnews.com` 403s; `eagles.rugby` sits behind a Vercel checkpoint; `japantimes.co.jp`
  serves a JS challenge.
- **All 23 source URLs hand-checked for HTTP status** (August 2026); a dead Las Vegas Sun link was
  replaced with ESPN.


### 16. Tonga — `16-tonga.md`  (Gen 0–6)
**The country with no coloniser to blame — and the same export anyway.** Closes **Section 5: The Church
and the Export**. (Written and proofread September 2026; 636 lines, 12,700 words, Gen 0–6.
`notes/tonga.md` holds the fact base, the inherited threads, the retrieval map, the hedged-facts list and
the proofreading record.)
- **Gen 0** The Sending Church (1826–1923) · **Gen 1** Three Tests and a Nought–All (1924–1938) ·
  **Gen 2** The Protected State (1939–1969) · **Gen 3** Ballymore (1970–1986) · **Gen 4** The Invitation
  (1987–1998) · **Gen 5** Open, and Gone (1999–2011) · **Gen 6** Twentieth (2012–2026), closing on the
  same **mid-July 2026** snapshot as `12-new-zealand.md`, `13-australia.md`, `14-fiji.md` and `15-samoa.md`.
- **⭐⭐⭐ THE SPINE, FROM THE FLOOR OF THE HOUSE OF COMMONS.** Hansard, **11 May 1970**, the Tonga Bill —
  **Bernard Braine**: "it is not an independence Measure, **since Tonga has never been a British colonial
  dependency**." Britain, winding up its own arrangement, put on the record that it never owned the place.
  ⚠️ **There are TWO treaties — 1879 and 1900.** The 1879 one was "**voluntarily concluded**" by the King
  "to safeguard his people against the possibility of annexation by some other power." Do not collapse them.
- **⭐⭐⭐ THE ANSWER THE CHAPTER GIVES.** Fiji's line was drawn by a land policy, Samoa's by a partition;
  **Tonga has nobody to point at, and the export ran anyway.** The Tongan historian **Amanda SullivanLee**:
  "**although Tonga was never formally colonized … the exploitation and fetishization of Tongan male
  bodies in the interest of warfare is no less present.**" *The export does not need a coloniser — it
  needs a small country good at producing strong young men, a large country that wants them, and an
  institution at home that has been organising the transaction since 1835.*
- **⭐⭐⭐ MOULTON'S TWO SCHOOLS — the bridge to `13-australia.md`.** **James Egan Moulton** helped found
  **Newington College, Sydney, in 1863**, then "sailed to Tonga two years later in order to set up **a
  similar College**" — **Tupou College, 1866**, the oldest secondary school in the Pacific. Newington
  played Australia's first inter-school rugby match in 1870 and joined the **Great Public Schools** on
  12 April 1892. **Same man, same church, same model; opposite countries out of the other end.** Fiji
  compares itself to Sydney through the *model* (Im Thurn); **Tonga compares through the man.**
- **⭐⭐ THE 1941 ASSESSMENT IS THE 2007 COMPLIMENT.** **Lt-Col John McLeod**: Tongans "took to drill and
  manoeuvres **like ducks to water** … the blood of warriors and gentlemen." SullivanLee's reading:
  "strong and brave but also **submissive**", "**needing of white direction in order to be useful**."
  Set against "**the big, sturdy men of Apia**" (1924) and Stephen Jones at Nantes (2007). **Rugby
  inherited that sentence; it did not invent it.**
- **⭐⭐ TWO FAMILIES, AND BOTH SETS OF SONS CAME BACK.** **Faitai Kefu** beat Australia at Ballymore
  (**16–11, 30 June 1973**), moved to Brisbane and **laid bitumen on the roads**; his son **Toutai** won a
  World Cup for Australia and then **coached Tonga**. **Fe'ao Vunipola** captained Tonga at two World Cups,
  signed for Pontypool in **1998**, and raised **Mako (79 England caps)** and **Billy (75)**; their mother
  **Rev. Iesinga Vunipola** is a **Methodist minister** to the UK Tongan diaspora; **Mako is in talks to
  coach Tonga at RWC 2027.** Fiji argues the export with statistics, Samoa with a village institution,
  **Tonga with two households.**
- **⭐ THE UNION ON ITSELF:** "Despite a total population of just 100,000 and **a rugby playing population
  of less than 800 seniors** Tonga is remarkably good at rugby. **Unfortunately rugby is Tonga's main
  export.**" (`tongarugbyunion.net`, a site frozen at 2011.) **The federation states this section's title
  as a complaint about itself.**
- **⭐ THE SECTION'S CLOSING IMAGE.** July 2026: **Fiji** played its "home" fixtures in **Cardiff,
  Liverpool and Edinburgh**; **Samoa** played all three of its in **Chile**; **Tonga** opened in **Denver,
  Colorado** (36–26 v Zimbabwe, 4 July). **Three island nations, one week, not one of them at home.**
- **⚠️ Sourcing note — the hardest chapter so far, and `notes/tonga.md` will save the next session hours.**
  **How rugby arrived in Tonga has no usable source**; the chapter says so and builds nothing on it. The
  **Daito Bunka / abacus** origin of the Japan pipeline rests on **one self-published blog** and is told as
  a story, cited against itself in Sources. **Keith Prowse** (banned repo-wide) is the origin of the
  "sailors and missionaries" account. Still unsourced and **absent from the chapter**: the union's founding
  year, the 1924 Test scores, the Prince Consort Trophy, the 1928 abandoned Test, the 2012 peak ranking,
  and the claim that Aberdeen cost Andy Robinson his job.


### 17. Italy — `17-italy.md`  (Gen 0–7)
**The country the game reached from France, in the luggage of a migrant worker — and the one that founded
the alternative to the British club, won it, and was then let in.** Opens **Section 6**. (Written and
proofread September 2026; 734 lines, 11,600 words, Gen 0–7. `notes/italy.md` holds the fact base, the
inherited threads, the retrieval tool, the hedged-facts list and the proofreading record.)
- **Gen 0** The Man Who Came Back from France (1910–1927) · **Gen 1** Our Sport (1928–1938) · **Gen 2**
  Sport da Combattimento (1939–1948) · **Gen 3** The Downgraded Fixture (1949–1972) · **Gen 4** Every
  November, Moscow (1973–1992) · **Gen 5** Beating France (1993–1999) · **Gen 6** Inside (2000–2015) ·
  **Gen 7** Seven Days in November (2016–2026), closing on the same **mid-July 2026** snapshot as chapters
  12–16.
- **⭐⭐⭐ THE ORIGIN IS UNLIKE ANY OTHER IN THE BOOK.** **Stefano Bellandi**, ***economo del Teatro alla
  Scala***, "**had discovered rugby in France, where he had emigrated**". His US Milanese side lost **15–0
  to Voiron at the Arena on 2 April 1911** and the crowd went home *"entusiasti dello spettacolo"*. No
  Briton, no enclave, no school, no missionary, no governor. **Where Fiji, Samoa and Tonga export men and
  import money, Italy imported a sport inside a returning migrant.**
- **⭐⭐⭐ BRITAIN IS ABSENT FROM THE ENTIRE FOUNDING RECORD.** The first match on Italian soil (**Turin,
  1910**) was **Racing Club de Paris v Servette**; the first Italian side played **Voiron**; and in
  **1933, at Turin, Italy, France, Germany, Romania and Czechoslovakia founded FIRA** — two years after
  the Home Unions expelled France. `11-france.md` tells that from the French side as "making do with Nazi
  Germany and Fascist Italy"; **from Italy's side it is founding something**, and it became **Rugby
  Europe**, the body `04-georgia.md` and `05-romania.md` both depend on without explaining.
- **⭐⭐ THE STATE TOOK IT, AND IT COST.** *Lo sport fascista* called rugby ***"il nostro sport"*** in
  **December 1928**, three months after the federation existed. **Achille Starace**: *"**sport da
  combattimento**, deve essere praticato e largamente diffuso."* Run through the **GIL** and the **GUF**.
  Then **at least ten rugbyists killed — the heaviest loss of any Italian sporting federation**, out of a
  sport whose first championship had six clubs. ⭐ **It rhymes with `16-tonga.md` inverted**: McLeod
  appraised Tongan bodies in 1941, Starace appraised Italian ones. *Section 5 is about bodies being taken;
  this is about bodies being volunteered.*
- **⭐⭐⭐ WHAT EXCLUSION ACTUALLY LOOKED LIKE.** **Sixteen consecutive springs** playing France, 1952–67,
  all lost — but **within two points at Grenoble in 1963** and three at Brescia in 1962. Then **Toulon
  1967, France 60–13**, after which France kept the fixture and **sent 'A' sides and Espoirs for
  twenty-eight years**. ⭐ **The two federations still keep different books — 31 matches on the FIR's
  count, 45 "meetings" on ESPN's** — and the fourteen-match gap *is* the relationship.
- **⭐⭐⭐ AND ITALY HAD A FULL INTERNATIONAL LIFE NOBODY WATCHED.** **Romania 41 times**, **the Soviet
  Union 14** (Italy lost nine), Spain 27, Czechoslovakia 12, Poland 7, Morocco 8. **Twelve of the fourteen
  Soviet matches were decided by nine points or fewer** — one-point games at Rovigo and L'Aquila, a draw
  in Moscow — ending in **Moscow on 3 November 1991, seven weeks before the USSR dissolved**. ⚠️ **No
  player's account of any of it survives**; three Italian-language searches found nothing, and the chapter
  says so rather than inventing atmosphere. ⭐ **Italy is also the opponent Romania played most.**
- **⭐⭐⭐ THE ARC THAT NAMES THE SECTION.** **Grenoble, 22 March 1997: Italy 40 France 32** — the **Coppa
  Europa** won at last, sixty-four years after Turin. **Ten months later, in January 1998, Italy's Six
  Nations election was ratified.** **Italy won the committee it had built and was then admitted to the
  committee that had excluded it.**
- **⭐⭐ THE WEEK THE CHAPTER IS NAMED FOR.** **Florence, 19 Nov 2016: Italy 20, South Africa 18.**
  **Padua, 26 Nov 2016: Tonga 20, Italy 18.** Same score, home both times, seven days apart. Both halves
  are already in this book, in `06-south-africa.md` and `16-tonga.md`. And in **2026 Italy finished fourth
  in the Six Nations, above England** — equalling its best campaign, twenty-six years after being let in.
- **⚠️ Sourcing note.** The constraint here was **language, not scarcity** — the chapter runs on Italian
  sources: the **FIR timeline and head-to-head ledgers**, **Sportmemory**, the **Museo delle Civiltà**,
  the **University of Padua's *Il Bo Live***, and **Nesti** on calcio storico. **Five claims were rejected
  after hand-verification** and are recorded against themselves in the Sources block: a reversed 1929
  scoreline, a misattributed FIR president, invented 1956–57 wins over France, a calcio storico/harpastum
  overreach, and a wooden-spoon total on which two sources disagree (**no number is printed**).

---

## 5A. SCOPE (decided August 2026): **all 24 teams of Rugby World Cup 2027**

The book covers **every nation in the RWC 2027 field** — the first 24-team World Cup, in Australia,
1 October–13 November 2027. This was already latent in the structure: every chapter closes on a dated
mid-2026 snapshot pointing toward RWC 2027, so the book reads as a companion to that tournament.

**The field, from [rugbyworldcup.com](https://www.rugbyworldcup.com/2027/en/teams) (✅ = written):**

| Pool | Teams |
|---|---|
| **A** | ✅ New Zealand · ✅ Australia · ✅ Chile · Hong Kong China |
| **B** | ✅ South Africa · ✅ Italy · ✅ Georgia · ✅ Romania |
| **C** | ✅ Argentina · ✅ Fiji · Spain · Canada |
| **D** | ✅ Ireland · ✅ Scotland · ✅ Uruguay · Portugal |
| **E** | ✅ France · Japan · USA · ✅ Samoa |
| **F** | ✅ England · ✅ Wales · ✅ Tonga · Zimbabwe |

12 qualified automatically from RWC 2023 (France, New Zealand, Italy, Ireland, South Africa, Scotland,
Wales, Fiji, Australia, England, Argentina, Japan); 12 through regional qualifying (Georgia, Spain,
Romania, Portugal, Tonga, Canada, USA, Uruguay, Chile, Samoa, Zimbabwe, Hong Kong China).

**Status: 17 written, 7 to go.**

### ⭐ A structural gift discovered while writing ch. 15 — use it
World Rugby's **inaugural Nations Cup (2026)** is the **second-tier** competition, and its field is
**exactly the twelve teams that had to qualify for RWC 2027 through regional competitions**: USA,
Chile, Samoa, Tonga, Uruguay and Canada in one pool; Georgia, Portugal, Spain, Romania, Hong Kong
China and Zimbabwe in the other. Above it, the **Nations Championship** took the Six Nations, the
Rugby Championship, **Japan and Fiji**.

**Eight of this book's nine unwritten countries are in the Nations Cup** — every remaining chapter
except **Italy** and **Japan**, which went up. In other words, **World Rugby drew a line across world
rugby in 2026 and the book's remaining chapters are, almost exactly, the countries below it.** Every
one of the last nine chapters can close on a dated mid-2026 snapshot that places its country in that
two-tier structure, and their July 2026 results are all reconstructible from the same sources
(`world.rugby/nations-cup/en`, `all.rugby` match sheets, Sky Sports form guides). **Thread it.**

### Section plan — organised by CARRIER MECHANISM, not geography
Each section names **who carried the game and what that did to its character**. That is the book's
organising principle and the new sections follow it. (Chapters are *not* grouped by RWC pool — the pool
table above is a scope checklist only.)

**The headings are institutions, not places** (renamed September 2026). Each one names a room a reader
could walk into, so that the contents page states the book's thesis before a word of prose does: *rugby
has no class — institutions do.* Two earlier names were geographic and have gone. **Note that §3 and §6
are the same institution at two moments** — the committee inventing the bar, then policing the door
seventy years later — and the headings are built to rhyme.

1. **The Clubhouse** (1–3): Uruguay, Argentina, Chile — *commerce built enclaves;
   what happened next depended on the institutions that inherited them.*
2. **The Ministry** (4–6): Georgia, Romania, South Africa — *the state as the carrying
   institution.*
3. **The Committee and the Coalfield** (7–10): England, Wales, Scotland, Ireland — *where the class weapon was invented,
   and what it did at home.*
4. **Out of British Hands** (11–13): ✅ **France**, ✅ **New Zealand**, ✅ **Australia** — *what rugby became once it
   escaped British institutional control.* France made it a **rural, working-class regional identity**
   (the south-west, not Paris); New Zealand made it a **national game with almost no class character**;
   Australia is the **control case** — same colonial origin as New Zealand, neighbouring country, and
   union stayed the **private-school game** while league took the working class, re-running **England's
   1895 schism** on the other side of the world.
   → This section **hinges off section 3**: it opens with the Home Unions **expelling France in 1931**
   for professionalism (already carried in `07-england.md`), and the country they threw out is the one
   that later built the pipeline which made Georgian and Romanian rugby.
5. ✅ **The Church and the Export** (14–16): ✅ **Fiji**, ✅ **Samoa**, ✅ **Tonga** — *missionaries and
   village schools carried it; European and Japanese clubs now extract it.* The sharpest institutional
   argument in the modern game, and it connects directly to **Saurel's Georgian pipeline** (Georgia
   Gen 4) and **Argentina's amateur-rule exodus**. Fiji (ch. 14) establishes the section's mechanism:
   the carrying institutions (**village, chief, Methodist church** — "ratuism, religion and rugby") are
   the same ones that make the players exportable, and the trade runs in parallel with **peacekeeping,
   the British Army and private military contracting**. Samoa (ch. 15) supplies the section's control
   case — **the 1899 partition of one people into a rugby half and an American-football half** — and
   its sharpest formulation of the mechanism: *the village maintains a chosen man so he can act on its
   behalf*, which is the pastor of 1830 and the professional of 2026. **Tonga (ch. 16) completes the
   section and is its hardest case: it was never annexed.** Fiji's division was drawn by a land policy,
   Samoa's by a partition — **Tonga has no coloniser to blame at all**, and the export ran anyway, from
   a District Meeting in 1835 onward. Samoa and Tonga are the harder version of Fiji — **19th and 20th
   in the world in July 2026, against Fiji's 9th**, and in the **second-tier Nations Cup** while Fiji
   went up into the Nations Championship. **Section 5 is complete; Section 6 (Italy, ch. 17) is next.**
6. **At the Committee's Door** (17–19): ✅ **Italy**, **Spain**, **Portugal** — *the same body that invented the
   bar in §3, seventy years on, deciding who is let in.* ⚠️ **PROVISIONAL — do not carve this in stone
   until ch. 17 is researched.** The old name, "the late admissions", was dropped because **two of the
   three were never admitted**: Italy joined the Six Nations in 2000; Spain and Portugal have not. It
   also took the admitting body's point of view, which is the one this book works against. The current
   name is accurate about all three and rhymes with §3 deliberately. **But if Italy's research shows the
   game reached Latin Europe through FRANCE rather than Britain** — plausible, and unchecked — then the
   carrier is French and the heading should name that instead, tying §6 back to §4 the way §4 hinges off
   §3. Sections 1–5 all earned their final names *after* their chapters were written; let this one do
   the same.
7. **Company and Campus** (20–22): **Japan, USA, Canada** — *carried by employers and universities
   rather than by class or nation.*
8. **The Garrison** (23–24): **Hong Kong China, Zimbabwe** — *expatriate and settler rugby after
   the empire that made it.*

### Why France is chapter 11
It is the most overdue chapter in the book by a wide margin. France is mentioned **154 times across all
ten existing chapters** — more than any unwritten country, and approaching the density of one that has
a chapter (Argentina, 220). It is **structurally load-bearing** in two: **Romania** invokes it **64
times** (the whole Oaks golden age is defined by beating France) and **Georgia 37 times** (Saurel's
export pipeline into French clubs *is* Georgia's development model). The book has been using France as
a mechanism without ever explaining it. It also opens Section 4 against the home nations just finished:
France was **expelled from the Five Nations in 1931 for professionalism** — a fact `07-england.md`
already carries — and the country the home unions threw out for paying players is the one that later
built the pipeline that made Georgian and Romanian rugby.

### ⚠️ Sourcing risk, flagged now rather than at chapter 23
The later sections will be far harder to source to this book's standard than anything so far. **Hong
Kong China, Zimbabwe, Canada and Spain** have thin English-language rugby historiography; Georgia — a
Tier 2 nation with a *famous* story — still required hand-verification of nearly every fact and yielded
several NOT FOUNDs that stayed out of the text. Expect the same or worse, budget for it, and hold the
line: **hedge or omit rather than assert**. See the no-Wikipedia rule in §6.

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
- ✅ **Italy is written and proofread** (September 2026) — see §5.17. **Spain (ch. 18) is next.** Italy
  hands it two direct threads: **Italy's first Test was against Spain, at Barcelona on 20 May 1929, lost
  9–0** — and the two have met **twenty-seven times**, Spain winning three. Spain was also in the
  **FIRA/Coppa Europa** field alongside Romania, Poland and Czechoslovakia, so the institution founded at
  Turin in 1933 plausibly carries ch. 18 as well. ⚠️ **AND THE SECTION NAME NOW NEEDS DECIDING.** The
  Italy chapter argues that **Italy won the committee it had built and was then admitted to the committee
  that had excluded it** — which makes "At the Committee's Door" the wrong frame, since the chapter is
  about founding a rival body rather than queuing at anyone's door. **"The Committee They Built"** is the
  candidate. Held only because Spain and Portugal are not yet scoped; **decide it during ch. 18.**
  ⭐ **`notes/italy.md` holds a retrieval tool worth knowing about**: `federugby.it/italia-vs-<paese>-all-time/`
  returns the FIR's complete head-to-head against any opponent, with venue, date, competition and score —
  **but the pages are frozen around 2008–09** and carry nothing modern.
- ✅ **Tonga is written and proofread** (September 2026) — see §5.16. **Section 5 is complete.**
  **Italy (ch. 17) is next and opens Section 6, "At the Committee's Door" — a provisional name; see the section plan.** Tonga hands it one thread: the
  chapter closes pointing at a country "told it did not belong at a table it had been sitting at since
  1929." ⚠️ **Tonga was the hardest chapter to source so far** — the national union's site
  (`tongarugbyunion.net`, not `.to`) has not been updated since 2011 and its whole history is one
  paragraph, and **how rugby arrived in Tonga has no usable source at all**; the chapter says so and
  builds nothing on it. What carried it instead: **Hansard**, the **US State Department**, an
  **open-access MA thesis on the Tongan military**, two **school history pages**, and **Rugby
  Australia's** 1973 retrospectives. Expect Section 6 to be harder still.
- ✅ **Samoa is written** (August 2026) — see §5.15. **Tonga (ch. 16) is next and completes Section 5.**
  Samoa hands it three threads: the **1924 Fijian tour's Tongan leg** (nine matches, seven won), the
  **2024 centenary match against Tonga**, and the **2026 Nations Cup**, in which Samoa and Tonga sat
  19th and 20th in the world in the same second-tier pool. Expect the same source pattern to work —
  the federation's own history, an open-access mission history, the Kanemasu/Uperesa migration
  corpus — and expect the **"never colonised"** fact to be the chapter's spine: Tonga kept its
  monarchy through a British protected-state arrangement, so its rugby cannot be explained by a
  colonial administration the way Fiji's and Samoa's can.
- ✅ **Fiji is written** (August 2026) — see §5.14. Chapter 14 **opens Section 5**, and it is the
  chapter where a peer-reviewed source states the book's own title as settled background. **Samoa
  (ch. 15) is next**, and Fiji hands it two direct threads: Fiji's **first Test was played at Apia on
  18 August 1924** at 7am on a field with a tree on the halfway line, and Samoa was the country **put
  on standby in 1987** in case Fiji could not travel after the coup. Tonga (ch. 16) inherits the 1924
  Tongan leg of the same tour. Both chapters should reuse Fiji's source pattern: **the federation's own
  history page, an open-access ANU Press or JSFD-style monograph on the mission, and the
  Kanemasu/Molnar migration corpus** — and both should expect the migration argument to be sharper and
  the domestic institutions weaker than Fiji's.
- ✅ **Australia is written** (August 2026) — see §5.13. Chapter 13 completes **Section 4**, and is the
  book's longest chapter and its second nine-generation spine.
- ✅ **New Zealand is written** (August 2026) — see §5.12. Chapter 12, the second of Section 4, and the
  book's first nine-generation chapter.
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
- **Open the page. HTTP 200 is not evidence.** This has now cost two chapters. National newspaper
  archives sit behind bot walls that return **200 with a challenge page as the body** — *Papers Past*
  (New Zealand) and **Trove** (Australia) both do it — while search engines happily index and quote the
  article pages behind them. A retrieval agent can therefore hand you a perfectly formatted citation,
  with quoted nineteenth-century newspaper text, for a page nobody has read. **Any agent quoting Papers
  Past or Trove is fabricating.** Try curl *and* WebFetch (they fail on different sites), and if neither
  returns the fact, the fact is not sourced.
- **Start a new country by looking for the national biographical dictionary.** The single biggest
  sourcing win in the Australia chapter was **`adb.anu.edu.au`** — the Australian Dictionary of
  Biography, peer-reviewed, authored, dated, wide open to curl, and **browsable by occupation**
  (35 rugby union players, 28 league players, administrators of both codes). It carried most of a
  22,000-word chapter and it was never designed to make a point about rugby, which is exactly what
  makes it good evidence. Look for the equivalent before trusting a federation's own history page.
- **Cite an abstract as an abstract.** Where a paywalled article's abstract is open, it is often worth
  having on its own — but say so in the Sources block, as `13-australia.md` does for Peter Horton.

**Step 0 — map the generations (new & expanded countries only).** Before any per-generation
research, for a *new* country or one being *expanded* past its current last generation, identify the
generation map first: the named eras with year ranges, following the Gen 0 = origins/enclave → Gen 1+
convention in §2 (most countries run to Gen 6/7). Run this as an **Explore / investigator** subagent
and record the outline at the top of `notes/<country>.md`. Then work the two-step loop below one
generation per turn, researching each generation in-depth. **Skip this step for the thirteen
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
