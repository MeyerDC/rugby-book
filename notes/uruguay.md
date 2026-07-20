# Uruguay — research notes

Fact + source cache for continuing the Uruguay chapter. Research adds to this file;
write prose *from* here so sources are never re-fetched. Sources also live at the end
of `chapters/01-uruguay.md`.

## Thesis
Rugby marooned as an elite **Carrasco enclave** while football (Peñarol vs Nacional) is the
national religion. Class is institutional: British cricket clubs incubated both codes; the
Montevideo Cricket Club's refusal to be governed by non-British men (~1900) stranded rugby socially.

## REWRITE DESIGN (agreed with author, July 2026) — binding for the new draft

Mirrors the South Africa, England and Wales rewrites (`drafts/06-south-africa.md`,
`drafts/07-england.md`, `drafts/08-wales.md`).

1. **New file**: draft at `drafts/01-uruguay.md` (NOT in `chapters/` — combine_book.py bundles every
   .md there). Write ONLY from this notes file. The old `chapters/01-uruguay.md` returns at the end
   as a **fact-checklist, never as text**; on approval the draft replaces it.
2. **Spine unchanged**: keep the **Gen 0–6** map and year ranges in "Generation map (LOCKED)" below.
   The rewrite changes voice, sourcing and *depth of history*, NOT which eras the story is cut into.
   - **No up-front bulleted generation list** (matching SA/England/Wales). Short framing intro only.
   - **Chapter 1 problem**: Uruguay opens the book, so the old draft made it carry the whole thesis
     out loud. It no longer has to. `00-front.md` sets up the book; this chapter tells Uruguay's
     history and lets the reading emerge.
3. **Narration — the new voice** (retire the old one):
   - **Out**: the direct-address conversational voice, which runs through every generation of the old
     draft — "Hold onto that image", "Notice what has happened here", "Read that again", "Sit with
     that for a moment", "Look at the jersey", "be careful before calling this a democratisation".
     Not trimmable; those paragraphs are built on the address and get rewritten.
   - **Out — thesis-first framing**: the old chapter announces the argument ("There is the thesis of
     this book, stated in its first chapter, on its first country") and closes on a peroration
     ("Rugby has no class. Uruguay spent a hundred and forty-six years proving it"). Both go. The
     institutional reading must be *produced by events*, never declared.
   - **In**: composed, novelistic **third-person** narration, still immersive, still cold-open dated
     scenes. Every generation opens on a dated scene — Gens 1, 2, 5 and 6 currently open undated.
4. **Perspectives from inside, no villains** (the Latham model, per [[sa-chapter-latham-tone-model]]).
   The old draft narrates institutions from outside, as verdicts ("it walked away rather than share
   the committee room"; "none of those buildings had a door that opened outward"). Replace with rooms:
   - **The MVCC gentlemen** — from inside their world: a club founded in 1861 by men who expected to
     go home, running their own affairs in their own language for forty years; the 1900 question put
     to them as *they* would have understood it, not as a class crime. Explained, not excused.
   - **The CURCC railwaymen** — 72 British, 45 Uruguayan, 1 German in 1891; why football was the game
     that a mixed-language workforce could actually play together, told from the yard, not from above.
   - **The Christian Brothers** — the teamwork-over-stars philosophy as a sincere moral curriculum
     (Ryan), from inside the order, not as a plot device for the crash's foreshadowing.
   - **The Carrasco families** — the schools and country clubs reproducing a world without experiencing
     themselves as excluding anyone. No conspiracy; no villains.
   - **The Andes survivors** — from inside, in their own words (Parrado, Canessa, Vierci). Never
     softened, never relished, never sainted.
   - **The modern URU** — the administrators who named the 2011 failure as the turning point; and the
     players who had to leave for France and England to earn a living.
5. **Sourcing — the strong part; keep and extend.** The old chapter already carries Brown and Ryan by
   name in the flow and hedges wiki-only micro-facts in prose (British Schools 1908, Carrasco Polo
   1933, Old Christians 1962/1965). Preserve that discipline. No wiki citations; no fabricated
   attributions. Two open gaps:
   - The **1880 reporter's quote** ("heads without shoulders…") is used as the chapter's cold open but
     its provenance is unconfirmed outside Wikipedia. Attribute openly as a transmitted account or
     find the paper; do not present it as a verified contemporary citation.
   - **THE 1900 MVCC REFUSAL — see the flagged decision below.** Chapter-critical and wiki-only.
   - **Cornerstone sources**: Matthew Brown (*Sports in South America*, Yale 2023; the *Soccer &
     Society* informal-empire paper), Hugh FitzGerald Ryan (SILAS 2008), Evelise Amgarten Quitzau
     (IJHS 2021), the Andes memoirs (Read, Parrado, Canessa, Vierci), Americas Rugby News,
     Sudamérica Rugby, club/institution sites.
6. **Lead with the history — the biggest content job.** The old chapter is 57KB, the shortest in the
   book by a distance (Georgia 74KB, Scotland 98KB, the SA rewrite 119KB), because it substitutes
   argument for events. Between 1900 and 1989 it names perhaps five matches. **Gens 1 and 3 need the
   deepest new research**: Gen 1 is currently narrated as "there was almost nothing to report" across
   fifty years; Gen 3's rugby content outside the crash is a single hedged 1981 title. Find the
   matches, players, tours, clubs and administrators that are actually there.
7. **Dated-snapshot fix (house style)**: Gen 6 currently says "As this is written, in the middle of
   2026" and leaves a fixture pending ("Hong Kong still to come on 18 July"). Rewrite the present-day
   edge as a fixed, closed, explicitly dated snapshot in the past tense, looking toward RWC 2027 in
   Australia.
8. **Motifs still thread** (SUMMARY §4): the **informal empire** and **cricket clubs as incubators of
   both codes**; the **amateur ideology**; the Uruguay/Argentina contrast (same British origin, opposite
   outcome — the counter-case that Chapter 2 answers). **Peñarol stays demoted** as a class-marker per
   the LOCKED framing decision below; the institutional fork is the engine, and Peñarol Rugby's return
   remains Gen 6's closing irony.
9. **Facts are the main focus**: every claim traceable to this notes file with a named source; one
   generation researched + written per turn (haiku Explore subagent for retrieval → adjudicated here →
   prose from the brief). See [[rugby-book-workflow]].

### ⚠ FLAGGED FOR AUTHOR — the 1900 MVCC refusal is wiki-only
The refusal is the chapter's thesis engine, and per the Gen 0 sourcing audit below it **could not be
corroborated anywhere outside Wikipedia** (MVCC's own history page is dead). The repo bans wiki
citations, and this rewrite makes facts the main focus — so a chapter built on it needs a decision.
Three options, in order of preference:
- **(a) Re-source it.** One targeted retrieval pass at AUF centenary material, MVCC club publications,
  Uruguayan press archives and the Quitzau/Brown literature before drafting Gen 0. Try this first.
- **(b) Reframe onto sourced ground.** Make Brown's documented elite-retreat thesis the engine (the
  country-club retreat; rugby's bodily contact "a step too far") and carry the 1900 refusal as a
  club tradition, openly hedged — the story the enclave tells about itself.
- **(c) Keep it, hedged hard** ("by the account handed down…"), as the old chapter does at l.47.
Recommendation: **(a), falling back to (b).** (b) is arguably the stronger chapter anyway — a sourced
structural argument rather than a single decisive committee-room moment.

**RESOLVED 2026-07-18 → (b).** Option (a) was attempted (targeted retrieval pass, Spanish + English,
AUF centenary material, MVCC club/archive material, Uruguayan press and academic literature). The
refusal story **remains uncorroborated outside Wikipedia**. Going with (b), strengthened by a genuinely
useful find: the AUF's 30 March 1900 founding membership is documented non-wiki, and **MVCC is simply
not on it**. So the chapter can carry the *documented absence* as fact — when Uruguayan football
organised itself, the country's oldest and grandest sporting club was not part of it — and carry the
*refusal anecdote* as the story the enclave tells about itself, openly hedged. That is a better and
more honest hinge than the committee-room moment, and it lands the same point.

## Established facts
- Origins in British cricket clubs: **CURCC** (→ Peñarol) and **Montevideo Cricket Club (MVCC)**.
- Christian Brothers / **Stella Maris** school → **Old Christians** club (the 1972 Andes crash side).
- Modern rise of **Los Teros**; **Peñarol Rugby** professional arm in Super Rugby Americas.

## Current chapter shape
Currently a raw research/conversation dump: **Prologue: The Setting** + one arc
**"The amateur wilderness (1948–1980s)."** NOT in story mode and NOT in the Gen 0–6 format.
**REWORK IN PROGRESS** — converting to the generation map below, one generation per turn.
- [x] **Gen 0 — The British Enclave** written (story mode) at top of chapter. Raw research kept
  below an HTML-comment marker (`RAW RESEARCH BELOW`) for converting into Gen 1–6.
- [x] **Gen 1 — The Enclave Organizes (1900–1951)** written. Cite Ryan 2008 (SILAS) + hedge the
  Wikipedia-only club dates (British Schools 1908, Carrasco Polo 1933) — done in prose.
- [x] **Gen 2 — The Irish Brothers (1955–1971)** written. Stella Maris 1955, Brothers chose rugby
  (Ryan), CB=rugby/Jesuit=football, Old Christians (1962/1965 hedged), shamrock, 1968 & 1970 titles.
- [x] **Gen 3 — The Mountain (1972–1988)** written. Flight 571 (Fairchild FH-227D, 13 Oct 1972),
  45 aboard/19 team, 16 survivors/72 days, avalanche killed captain Marcelo Pérez, Eucharist framing
  tied to CB formation, Parrado/Canessa trek + Sergio Catalán, rescue 22–23 Dec 1972. Afterlife:
  Alive (1974), Society of the Snow (2023/Netflix 2024, Oscar nom). 1981 SA title HEDGED (Wiki-only).
  Sources: Guardian (Parrado 2023), Viven Foundation, Parrado/Canessa/Vierci/Read books.
- [x] **Gen 4 — Getting on the Map (1989–2003)** written. IRB 1989; RWC 1999 (beat Spain 27–15,
  Ormaechea try aged 40 — "oldest" hedged); Flight 571 press thread; RWC 2003 (beat Georgia 24–12,
  England 111–13 / Lewsey 5, Lemoine's try 1 of 2 England conceded in pool); Lemoine pro (Bristol
  1998 → Stade Français/Montauban). "Third most popular sport" hedged. Amateur base = the problem.
- [x] **Gen 5 — The Plan (2007–2019)** written. Missed 2007 (Portugal, Bado red) & 2011 (Bucharest
  39–12) = the pivot the URU names as defining; Estadio Charrúa + High Performance + Americas Rugby
  Championship = the system; 2015 (beat Russia 57–49 agg), 2018 (beat Canada H&A), 2019 Kamaishi
  beat Fiji 30–27 (Arata/Diana/Cat tries, Berchesi 15). Charrúa refurb date hedged. Tees up Gen 6.
- [x] **Gen 6 — The Branches Rejoin (2020–2026)** written (FINALE). Peñarol Rugby (SLAR→Super Rugby
  Americas; corrected titles: SLAR 2021 + SRA 2023 + 2025); RWC 2023 Namibia 36–26 comeback;
  homegrown-only pride; thesis close; 2024 Ambrosio turnover; 2025 Sudamérica title over Chile →
  RWC 2027 qual (6th straight); DATED mid-July 2026 Nations Cup snapshot (beat Georgia, drew Romania
  36–36, HK still to come 18 July).

## ✅ ALL GENERATIONS 0–6 WRITTEN + CHAPTER FINALISED (2026-07)
1. [x] Raw-research block DELETED (backup at /tmp/uruguay.bak for the session).
2. [x] `## Sources` REBUILT — dropped Wikipedia/Grokipedia/aggregator/football-table clutter;
   curated non-Wiki set (Brown/Toynbee, Ryan/SILAS, Quitzau, the Andes books, club/institution
   official sites, Guardian, Americas Rugby News, Sudamérica Rugby, World Rugby).
3. [x] `python3 combine_book.py` run to rebuild book.md.

## Generation map (LOCKED — Step 0 done; Gen 1/2 revised & ADOPTED 2026-07)
- **Gen 0 — The British Enclave (1842–1900):** Victoria CC → MVCC (1861); rugby ~1865/1880; the
  fork — CURCC joins the AUF and assimilates (→ football/Peñarol), MVCC *refuses to be governed by
  Uruguayans* (1900) → rugby stays British.
- **Gen 1 — The Enclave Organizes (1900–1951):** after MVCC's refusal, rugby drifts for half a
  century as an Anglophile schools/clubs pastime (British Schools of Montevideo ~1908, Carrasco
  Polo ~1933), then finally organizes: first Test 1948 (lost 21–3 to Chile), first Campeonato 1950
  (MVCC v Carrasco Polo), URU founded 31 Jan 1951 (Carlos Cat; hon. sec. D. McCormack). Theme: the
  game gets a structure — but only for the enclave.
- **Gen 2 — The Irish Brothers (1955–1971):** Cardenal Newman (1948) → Stella Maris (1955); Brothers
  chose rugby (teamwork over stars); Jesuit schools played football; Old Christians (1965), the
  shamrock, national titles 1968 & 1970; amateur Test struggles (Argentina hammerings) threaded in.
- **Gen 3 — The Mountain (1972–1988):** the Andes crash welds Uruguay's global identity to Old
  Christians; 1981 South American title.
- **Gen 4 — Getting on the Map (1989–2003):** IRB entry; Ormaechea's 1999 WC; Lemoine; 111–13 England.
- **Gen 5 — The Plan (2007–2019):** the Bucharest pivot; Estadio Charrúa; High Performance; Fiji win.
- **Gen 6 — The Branches Rejoin (2020–2026):** Super Rugby Americas; Peñarol Rugby; Namibia 2023;
  Nations Cup 2026.

## ⚠ MAP CORRECTION (from Gen 1 non-Wikipedia research — Ryan 2008, SILAS)
The raw notes wrongly placed the Irish Christian Brothers in the "early 20th century." The academic
source corrects this: **Stella Maris College opened MAY 1955** (offshoot of Cardenal Newman College,
Buenos Aires, 1948 — the first Christian Brothers school in South America); **Old Christians Club
founded 1965** (not 1962). So the Irish-Brothers story is a **1950s–60s** phenomenon, not 1900–1950.
PROPOSED revised map (Gen 0–6 preserved):
- **Gen 1 — The Enclave Organizes (1900–1951):** after MVCC's refusal, rugby drifts for half a
  century as an Anglophile schools/clubs pastime — British Schools of Montevideo (rep. 1908),
  Carrasco Polo (rep. 1933) — then finally organizes: first Test 1948 (lost 21–3 to Chile), first
  Campeonato Uruguayo 1950 (MVCC v Carrasco Polo), URU founded 31 Jan 1951 (Carlos "Charlie" Cat
  first president; hon. sec. D. McCormack). Theme: the game gets a structure — but only for the enclave.
- **Gen 2 — The Irish Brothers (1948/1955–1971):** Cardenal Newman (1948) → Stella Maris (1955);
  Christian Brothers deliberately chose rugby (teamwork over stars); Jesuit schools played football;
  Old Christians (1965), the shamrock, first national titles 1968 & 1970; amateur Test struggles
  (Argentina hammerings) threaded through.
- **Gen 3 — The Mountain (1972–1988):** the Andes crash. (unchanged)
- Gen 4–6 unchanged.

## Gen 1 research brief (non-Wikipedia) — Ryan 2008, SILAS
Source: **Hugh FitzGerald Ryan, "The Development of Rugby in the River Plate Region: Irish
Influences,"** Irish Migration Studies in Latin America 6:1 (March 2008), 29–37 —
https://www.irlandeses.org/0803ryan1.htm (the only substantial non-Wikipedia academic source found
on Uruguay rugby 1900–1950).
VERIFIED (non-Wiki): Cardenal Newman College BA opened 1948 (first CB school in S. America); Stella
Maris opened May 1955 (Carrasco), petitioned by Uruguayan Catholic parents; Christian Brothers chose
rugby on a teamwork-over-stars philosophy; CB schools = rugby, Jesuit schools = football; MVCC 1861 /
first certain rugby match 1880 (corroborated in Ryan); Campeonato Uruguayo 1950 (MVCC v Carrasco
Polo); URU founded Jan 1951, Carlos Cat first president, first hon. sec. D. McCormack (Irish name);
Uruguay's first Test 1948 v Chile, lost 21–3; 1951 South American Champ — lost 62–0 to Argentina,
beat Chile; Old Christians founded 1965, shamrock crest, national titles 1968 & 1970.
WIKIPEDIA-ONLY (hedge/attribute, don't state flat): British Schools of Montevideo founded 8 Oct 1908
& "first to play rugby"; Carrasco Polo founded 1933 (equestrian; new facilities 1949–52; "rugby
criollo" 1949); MVCC moved to Carrasco 1955; founding Stella Maris brothers (Doorley, Ryan, Kelly);
MVCC 1865 rugby claim.
DISCREPANCY: Old Christians founding — Ryan 1965 vs Wikipedia 1962. Prefer Ryan (non-Wiki) or hedge.

## Framing decisions (LOCKED)
- **Peñarol: DEMOTED as a class-marker.** Its class coding is contested in the sources and the lived
  class divide dissolved long ago — do NOT lean on "rugby marooned against working-class Peñarol."
  The thesis engine is the **institutional fork**: CURCC assimilates into the AUF (→ football) while
  MVCC refuses Uruguayan governance in 1900 (→ rugby stays a British enclave). Peñarol football is
  ambient "national religion" backdrop only; **Peñarol Rugby's modern return is the closing irony**
  of Gen 6 ("the two branches of 1891 finally rejoin"), well-sourced and kept.
- **Andes crash = its own generation (Gen 3 — The Mountain).**

## To research / open threads
- Facts are largely already gathered in the existing chapter body (to be rewritten into prose).
- Modern era detail (2015/2019/2023 WCs, pro timeline, current squad) already in notes/chapter.

## Gen 4–6 verification pass (Option A) — 2026-07
**CORRECTION FOUND & FIXED (Peñarol titles):** raw block/notes wrongly said "runners-up 2021,
champions 2022/2023/2025." NON-WIKI (Americas Rugby News) confirms Peñarol Rugby are **THREE-time**
champions: **SLAR 2021 (inaugural) + Super Rugby Americas 2023 + 2025.** They did NOT win 2022; Dogos
XV won 2024; Pampas/Dogos contested 2026 (ending Peñarol's reign). Gen 6 prose corrected to
"SLAR 2021, SRA 2023 & 2025."
- 2023 final: "Peñarol outlast Dogos to become Super Rugby Americas Champions," 9 Jun 2023, Estadio
  Charrúa — https://www.americasrugbynews.com/2023/06/09/penarol-outlast-dogos-to-become-super-rugby-americas-champions/
- "Three-Time SRA Champions Peñarol" (Jan 2026) — https://www.americasrugbynews.com/2026/01/15/three-time-sra-champions-penarol-confirm-2026-roster/

**VERIFIED (non-Wiki, Americas Rugby News / Sudamérica Rugby):**
- 2025 Sudamérica title → RWC 2027 qualification (6th straight): https://sudamerica.rugby/espanol/ (6 Sep 2025).
- July 2026 Nations Cup at Estadio Charrúa; Uruguay 36–36 Romania (11 Jul 2026):
  https://www.americasrugbynews.com/2026/07/11/uruguay-and-romania-ends-in-a-draw/ ; beat Georgia
  round 1 & new-blood squad: americasrugbynews.com 2026/06/21 & 07/02 (already in chapter Sources).

**NOT INDEPENDENTLY VERIFIED (retrieval limit, NOT refutation) — well-documented but automated search
could not reach non-Wiki confirmation (World Rugby/ESPN archives dynamic/paywalled):**
- RWC 1999 (Spain 27–15; Ormaechea try aged 40; "oldest" superlative — keep HEDGED), RWC 2003
  (Georgia 24–12; England 111–13/Lewsey 5; Lemoine try), Lemoine's clubs; RWC 2007/2011 playoff
  scores; Estadio Charrúa refurb date (kept vague in prose); RWC 2015 Russia agg; 2018 Canada; RWC
  2019 Fiji 30–27 (Arata/Diana/Cat, Berchesi 15); RWC 2023 Namibia 36–26 (Amaya/Kessler/Arata/Basso).
  → These are widely reported results; prose keeps them but superlatives/soft facts are hedged.

## Gen 0 research brief (British Enclave, 1842–1900) — cached from Explore pass

**VERIFIED (high confidence)**
- **Victoria Cricket Club, 1842** — founded by Samuel Lafone + British immigrants; dissolved soon
  after the **Great Siege of Montevideo (1843–1851)**. Lafone's exact business = UNCERTAIN.
- **Montevideo Cricket Club (MVCC), 18 July 1861** — founded at the Confitería Oriental by English
  immigrants. First ground "La Blanqueada"/the "English ground" (Military Hospital site today).
  **8th-oldest rugby club in the world, oldest outside Europe** (World Rugby Museum, Twickenham).
- **Central Uruguay Railway Co.** — registered London 1876, operating from **1 Jan 1878**; eventually
  ~1,665 km (~half the national network).
- **CURCC, 28 Sept 1891** — founded by railway employees: **72 British, 45 Uruguayan, 1 German**.
  Charter names cricket, rugby football, "other male sports." By **1892** shifted to association
  football (first match 1892, 2–0 vs English high-school students).
- **AUF founded 1900**; CURCC a charter member (→ later Peñarol, renamed 13 Dec 1913; CURCC dissolved
  22 Jan 1915). First AUF match 10 June 1900 (CURCC 2–1 Albion); first Clásico 15 July 1900
  (CURCC 2–0 Nacional) — football backdrop only.
- **The 1900 fork:** MVCC was invited to join the AUF and **REFUSED** — did not want to be governed
  by a non-British body. This is the thesis engine (assimilation vs refusal).
- **First CERTAIN rugby match: 1880**, Uruguayan vs British members of MVCC, at the MVCC ground;
  contemporary newspaper described the scrum as "sublime and ridiculous… heads without shoulders,
  legs without bodies, hands without arms." → the Gen 0 cold-open scene.

**DISPUTED / UNCERTAIN — do NOT invent around these**
- **1865 rugby claim** at MVCC = a *claim*, not confirmed; no contemporary record.
- **MVCC vs Buenos Aires FC** (Buenos Aires FC founded 1864) billed as the first international rugby
  match, but **NO confirmed date** (some BAFC records suggest ~1881). Played at Montevideo.
- **No verifiable match/fixture record survives for 1880–1900** — internal, inter-club, or
  international. Write the enclave era AROUND this gap; do not fabricate fixtures/scores.
- **Samuel Lafone** — named founder, but career details thin.

**Matthew Brown scholarship (from existing chapter body — keep, well-cited there)**
- "British informal empire and the origins of association football in South America," *Soccer &
  Society* 15, no. 2–3 (2015), 167–182 — argues the "British brought sport" story rests on assertion,
  not evidence (narrow English-language source base, only Brazil/Argentina case studies).
- *Sports in South America: A History* (Yale UP, 2023) — pre-existing local sporting cultures.
- Use as the revisionist counterpoint texturing Gen 0's "informal empire" motif.

**Gen 0 source URLs (add to chapter Sources on write):**
- https://en.wikipedia.org/wiki/Montevideo_Cricket_Club
- https://en.wikipedia.org/wiki/Rugby_union_in_Uruguay
- https://en.wikipedia.org/wiki/Central_Uruguay_Railway
- https://en.wikipedia.org/wiki/Buenos_Aires_Football_Club
- https://en.wikipedia.org/wiki/Pe%C3%B1arol
  (Brown citations already in chapter Sources / body.)

## Gen 0 — NON-WIKIPEDIA sourcing (per repo rule: don't cite Wikipedia)

**Matthew Brown, *Sports in South America: A History* (Yale UP, 2023)** — via the Toynbee Prize
Foundation interview (authoritative, citable): https://toynbeeprize.org/posts/the-history-of-modern-sports-in-south-america-an-interview-with-matthew-brown/
Direct, usable points (Brown's own words / argument):
- **Revisionism / why the early record is thin & British-authored:** the "fathers of football"
  (Watson Hutton, Charles Miller) narrative rests on British-community newspapers — "The British
  sportsmen organised the games, played them, wrote up the articles, and published them in English
  newspapers. They were the protagonists and the historians at the same time." → justifies writing
  AROUND the 1880–1900 gap.
- **The enclave thesis (sourced!):** "by the early 20th century, liberal elites would retreat their
  leisure time to country clubs with exclusive memberships and less popular sports, like riding,
  tennis, fencing, golf, and rugby. The high class did not want to engage in football games with
  people from working-class neighbourhoods." + rugby's close bodily contact made it "a step too far"
  in multi-ethnic societies → why football went national and rugby stayed elite.
- **Railways/Peñarol (non-Wiki corroboration):** "teams created around train stations or railway
  workers, like Peñarol, in Uruguay."
- **National leagues developed only in the second half of the 20th c.** → supports sparse early record.
- Context: War of the Triple Alliance (1864–70), War of the Pacific (1879–83); elites' "civilising"
  project (Elias/Sarmiento "Civilización y Barbarie").
- Also: Brown, "British informal empire and the origins of association football in South America,"
  *Soccer & Society* 15, no. 2–3 (2015), 167–182.

**rugbyfootballhistory.com** — authoritative non-Wiki for the general codification background (Rugby
School, RFU 1871, by 1880 Scotland/Ireland/Wales had unions). Not Uruguay-specific.
http://www.rugbyfootballhistory.com/originsofrugby.htm

**WIKIPEDIA-ONLY — NOT independently verified (do NOT cite as fact; hedge or attribute in prose):**
- MVCC founding date 18 July 1861; Confitería Oriental; "8th-oldest rugby club" ranking.
- The 1865 rugby claim; the 1880 first-certain match + "heads without shoulders" quote (provenance
  of the quote unconfirmed in any non-Wiki source found).
- MVCC vs Buenos Aires FC "first international" (no confirmed date anywhere).
- **The 1900 MVCC refusal to join the AUF** — central to the chapter but only found on Wikipedia;
  could NOT corroborate via MVCC's own site (history page dead) or other sources. Attribute carefully
  ("by most accounts") rather than stating flatly, OR frame via Brown's sourced elite-retreat thesis.
- CURCC founding 28 Sept 1891 (72/45/1) — Wikipedia/Grokipedia only.

## GEN 0 BRIEF — REWRITE PASS (1842–1900), adjudicated 2026-07-18
Supersedes the two older Gen 0 blocks above where they conflict. Haiku Explore retrieval, then
adjudicated here — **several of the agent's own "VERIFIED" tags were downgraded**; trust this block's
tags, not the agent's.

### NEW — VERIFIED non-wiki, usable as fact
- **AUF founded 30 March 1900**, by four clubs: **Albion FC, CURCC, Deutscher Fussball Klub, Uruguay
  Athletic Club.** First president **Pedro Charter** (CURCC); driving force **Enrique Cándido
  Lichtemberger** (Albion); HQ at Calle Solís 15, the offices of El Siglo.
  Sources: [FIFA, AUF 120th anniversary](https://inside.fifa.com/news/auf-celebrates-120th-anniversary-3069452);
  [efdeportes on Albion FC](https://www.efdeportes.com/efd120/albion-football-club-profetas-del-sport-en-uruguay.htm).
  → **THE KEY FIND.** MVCC is not among the four. The chapter states the documented *absence*, not the
  undocumented refusal. (Charter/Lichtemberger names: FIFA-sourced, fine to use; keep light.)
- **Victoria Cricket Club founded 29 October 1842** by Samuel Lafone and British immigrants, at Pueblo
  Victoria on the Pantanoso stream (La Teja). Siege began Feb 1843 — the club did not survive it.
  Source: [Americas Rugby News, July 2023](https://www.americasrugbynews.com/2023/07/19/the-older-rugby-club-in-the-americas-turns-162/).
  → More precise than the old notes ("1842"). ARN is a legitimate non-wiki source.
- **MVCC founding detail (same ARN piece)**: founded at the **Confitería Oriental** (Gran Hotel
  Oriental, Solís & Piedras); founders included **John Pickering** (first president/secretary),
  **Harold Hughes**, **Robert MacLean** — all ex-Victoria CC. → The Victoria→MVCC continuity is now
  carried by named men, which is exactly what the from-inside voice needs.
- **MVCC = 8th-oldest rugby club in the world, oldest outside Europe**, per the World Rugby Museum
  roll, reported by ARN (non-wiki). Attribute to the museum in flow.
- **MVCC v Buenos Aires CC, 1868 — first international CRICKET match.** (ARN.) Useful: the Río de la
  Plata axis predates the rugby fixture. Do NOT conflate with the disputed rugby "first international."

### DOWNGRADED — the agent tagged these VERIFIED; they are not
- **The "sublime and ridiculous / heads without shoulders" quote — WIKI-ONLY.** The agent labelled it
  "VERIFIED existence" then conceded the newspaper, date and original Spanish wording are unconfirmed
  outside Wikipedia. That is wiki-only. **The old chapter opens the entire book on this quote.**
  Handle: keep the scene, attribute openly as a transmitted account ("the line that has come down…"),
  or open Gen 0 on different ground. Do NOT present it as a verified contemporary citation.
- **British community population figures** (~4,000 in Uruguay, ~1,200 in Montevideo, c.1889): the
  agent's own note says the source PDF was **inaccessible** and the title was inferred from a search
  result. **Unsourced — do not use.**
- **"Players & individuals 1880–1900: Diego Magno, Diego Arbelo, Juan Andrés Zuccarino" — REJECT.**
  These are modern MVCC/Los Teros players lifted from a 2023 club-anniversary article and misfiled
  into the nineteenth century. Not Gen 0 people. A good reminder to check agent output by hand.

### NEW PROBLEM — CURCC's charter and rugby
- **"CURCC's 1891 charter named rugby football" — NOT FOUND.** Targeted search returned only cricket
  and "other male sports" in accessible sources.
- **This matters well beyond Gen 0.** The old chapter states it flatly (l.45) and **Gen 6's entire
  closing irony rests on it** — "the club whose charter in 1891 actually named *rugby football* before
  it dropped the game within a year." If the charter can't be sourced, that line cannot stand as
  written. Options: re-source it in the Gen 6 pass (Peñarol's own centenary/heritage material is the
  best bet — the club is proud of CURCC and publishes on it); or rebuild the Gen 6 irony on the
  sourced ground that CURCC was **a cricket club founded by railwaymen that became a football club**,
  which is documented and carries nearly the same weight.
- **CURCC membership 72 British / 45 Uruguayan / 1 German** — still only blog/wiki-tier sourcing
  (Gottfried Fuchs blog). Hedge, or attribute as the received tally.
- **CURCC's first football match score is contested**: old notes say 2–0 vs English high-school
  students; this pass returned 3–2, sourced to Wikipedia/**Grokipedia** (banned as clutter per the
  Sources rebuild). Use neither score; say they took up football in 1892 and leave it.

### CONFIRMED GAP — write around it
- **No fixture or match record survives for Uruguayan rugby 1880–1900.** Two retrieval passes have now
  failed to find one. This is a real archival silence, not a research failure, and Brown explains why
  (the British were "the protagonists and the historians at the same time"). Gen 0 must be built
  around the gap — do not fabricate fixtures, scores or players.
- **MVCC v Buenos Aires FC "first international rugby match" — still NO confirmed date.** Unchanged.
- **El Nacional, 11 September 1880** — an account of a "foot-ball" match, Uruguayan-Argentine combined
  v a British team at the cricket ground, ~1,000 spectators, 15 a side. Traced to RSSSF, not to the
  paper itself. **Possibly the same event as the "first rugby match," possibly not** — 15 a side is
  suggestive but "foot-ball" in 1880 is ambiguous. Promising lead; NOT yet usable. Worth one archive
  attempt (Anáforas / Biblioteca Nacional) if the cold open needs firmer ground.

## ARCHIVE PASS — the 1880 quote (2026-07-18). VERDICT: NOT FOUND. Cold open changed.

**The "sublime and ridiculous / heads without shoulders" quote is unusable as a citation.** A dedicated
archive hunt (Anáforas, Biblioteca Nacional de Uruguay, El Nacional / El Siglo / La Razón 1880,
Internet Archive, HathiTrust, Google Books; Spanish phrasings "sublime y ridículo", "cabezas sin
hombros", "manos sin brazos") returned nothing. Wikipedia carries it attributed only to "one
observer" — **no newspaper, no date, no author**. The original Spanish was never located. Two passes
have now failed.
- **El Nacional, 11 Sept 1880** also could not be reached; it traces to RSSSF and blogs, never to the
  paper. Whether it even describes rugby rather than association football is still unknown. Dead end
  unless someone works the physical archive.
- **Decision: the book no longer opens on this quote.** It may appear later in Gen 0, if at all, only
  as an openly-flagged piece of transmitted lore ("the line that has come down about that first
  match, though no one has produced the paper it appeared in…"). Never as a sourced contemporary quote.

### ⚠ AGENT OUTPUT CONTAMINATION — noted so the next pass isn't fooled
The retrieval agent tagged large amounts of **Wikipedia** material as "VERIFIED", in direct violation
of its instructions. Rejected from that pass: Lafone's biography, the La Teja etymology, Holy Trinity
Church 1843, the Confitería Oriental description, "La Blanqueada"/Military Hospital, the 1868 match,
Peñarol's colours/Stephenson's Rocket, the CUR network figures. All wiki-tier; none usable as cited
fact. **Most seriously, it re-reported the 1900 MVCC refusal as "CRITICAL FACT: not anecdote,
documented fact" and cited Wikipedia in the same line.** That is the exact claim already ruled
wiki-only above. The resolution stands: refusal = hedged tradition, absence = fact.
**Date conflict**: Victoria CC founding — ARN (non-wiki) says **29 October 1842**; Wikipedia says 12
September 1842. Prefer ARN; hedge the exact day in prose if it carries weight.

### NEW — genuinely usable, non-wiki
- **Enrique Cándido Lichtemberger** (Albion FC; the driving force behind the AUF): born 1873 in
  Montevideo, **English mother, Alsatian father**, educated at the English High School under
  **William Leslie Poole**, a Cambridge graduate. Source:
  [efdeportes, "Albion Football Club: profetas del sport en Uruguay"](https://www.efdeportes.com/efd120/albion-football-club-profetas-del-sport-en-uruguay.htm).
  → Valuable: the man who organised Uruguayan football was himself a product of the British schooling
  network — half-English, taught by a Cambridge man. The fork wasn't British vs Uruguayan; it ran
  *through* the Anglo-Uruguayan world. Good material for the from-inside voice.
- **CURCC charter naming rugby football: NOT FOUND, second independent pass.** Treat as unverified.
  Gen 6's closing irony must be rebuilt (see the Gen 0 brief above).

### COLD OPEN — DECISION (recommended, pending author sign-off)
No verified *rugby* scene exists anywhere in Gen 0 — the 1880–1900 archival silence is total. The cold
open must therefore be an institutional/cricket scene, which suits the book's core motif anyway
(**cricket clubs as the incubators of both codes**).
- **CHOSEN: 18 July 1861, the Confitería Oriental**, Solís & Piedras — **John Pickering**, **Harold
  Hughes** and **Robert MacLean**, all former Victoria CC men, founding the Montevideo Cricket Club in
  a café where the city's high society and businessmen gathered. Named men, a dated day, a specific
  address, a social register — and it founds the institution that carries the whole chapter.
  Source: Americas Rugby News (July 2023), non-wiki.
  Then pull back in house style to **Samuel Lafone and Victoria CC in 1842** on the Pantanoso stream,
  and to the **Great Siege from February 1843** that killed it — nineteen years of interruption
  standing behind the men in the café. Keep Lafone's colour thin: only the saladero/merchant outline
  is safely non-wiki.
- **Runner-up if a harder opening is wanted:** 1842 Victoria CC founded on the stream, four months
  before the Siege closes over the city. Chronological, but strands the chapter's real institution.

## GEN 1 BRIEF — REWRITE PASS (1900–1951), adjudicated 2026-07-18

**Method note:** two haiku Explore passes underdelivered on this generation (the second did no fresh
searching — it re-read this notes file and returned it as "findings"). The material below was
gathered by **fetching the primary sources directly** (URU's own site, Sudamérica Rugby, Carrasco
Polo's own site). Lesson for later generations: for a small number of known, named institutional
sources, fetch them directly rather than dispatching an agent.

### ⚠ CORRECTION TO THE OLD CHAPTER — "three clubs in one suburb" is WRONG
The old chapter says the 1950 championship was "contested between a cricket club, a polo club, and a
scatter of old-boy sides, all within a few miles of the Carrasco seafront" and that "the talent pool
was three clubs deep." **The URU's own institutional page contradicts this.** Do not reproduce it.

### VERIFIED non-wiki — the URU's own site (uru.org.uy/institucional-2)
- **First Campeonato de Clubes, 1950**, organised by **Carlos E. Cat**, contested by: *"Montevideo
  Cricket, Carrasco Polo (dos equipos), Old Boys y Colonia Rugby."*
  → **FOUR clubs, five teams — and Colonia Rugby is NOT in Montevideo.** Colonia del Sacramento is
  ~180 km west, on the river opposite Buenos Aires. The claim that Uruguayan rugby never left
  Carrasco in this era is false, and the chapter must say so. This is the single most valuable find
  of the pass.
- **URU founded 31 January 1951**: *"el 31 de enero de 1951 se creara la Unión de Rugby del Uruguay
  (U.R.U.); Cat fue su primer presidente."*
- **Full founding committee** (the era's first real cast of named human beings):
  President **Carlos E. Cat** · Vice-President **H. Bowles** · Hon. Secretary **D. Mac Cormack** ·
  Hon. Treasurer **J.J. Nery** · Board: **R. Sedgfield**, **D. Tricánico**, **J. Yorston**.
  → Note the mixture: Bowles/Mac Cormack/Sedgfield/Yorston are British and Irish; **Nery** and
  **Tricánico** are not. The founding committee of Uruguayan rugby was already not purely British.
  Excellent material for the from-inside, no-villains voice — the enclave was porous at the top from
  its first day of formal existence.
- URU's own framing: rugby arrived via British immigrants in the second half of the 19th century and
  "remained confined to British colonial circles, particularly the Montevideo Cricket Club, for many
  decades." The enclave reading is the *union's own*, not an outsider's accusation. Use this.

### VERIFIED non-wiki — Sudamérica Rugby, "El Panamericano de 1951"
https://www.sudamerica.rugby/english/el-panamericano-de-1951-3?nid=363
- Tournament called **"ABCU"** after its four participants (Argentina, Brazil, Chile, Uruguay), played
  as part of the **first Pan American Games, Buenos Aires, September 1951**.
- Organised by the **Unión de Rugby del Río de la Plata** (shortly renamed Unión Argentina de Rugby).
  Quoted rationale: *"In Argentina there were capable leaders who thought the best way to promote
  rugby in the region was by organizing a championship."*
- All matches at **Gimnasia y Esgrima de Buenos Aires**, Maldonado.
- **Results:** 9 Sept — Chile 68–0 Brazil; **Argentina 62–0 Uruguay**. 13 Sept — Argentina 72–0
  Brazil; **Uruguay 8–3 Chile**. 16 Sept — **Uruguay 17–10 Brazil**; Argentina 17–10 Chile.
- **FINAL STANDINGS: 1. Argentina · 2. URUGUAY · 3. Chile · 4. Brazil.**
  → **This changes the shape of the generation's ending.** The old chapter uses only the 62–0 and
  frames 1951 as humiliation ("taken apart"). In fact Uruguay finished **second of four**, in their
  first tournament, three weeks after founding their union.
- Uruguay were *"the surprise of the first regional tournament"*; the win over Chile was *"considered
  the finest match of the tournament."*
- **NAMED PLAYERS AT LAST:** the winning try v Chile scored by **Federico Armas**, *"converted by
  Nigel Davies, seconds before the final whistle."*
  → A Uruguayan scores, a Welsh/British name converts, in the last seconds. The composition of the
  enclave in a single passage of play. This is the generation's closing scene.
- Confirms "encounters in 1948" between these nations — corroborates the 1948 Chile Test.

### VERIFIED non-wiki — Carrasco Polo Club's own site (carrascopolo.com.uy/about-us-2/)
- *"En 1930 se forma 'Montevideo Polo Club', una Institución Deportiva la cual fue disuelta tan solo
  tres años más tarde"* — dissolved 1933; **Carrasco Polo founded by 40 of its former members.**
  (So the 1933 founding is now effectively confirmed from the club itself.)
- First president **Dr. Pedro Barcia**; handed over to **Carlos Stajano in 1945** (club's own site says
  1945; a search summary said 1944 — prefer the club).
- Moved to the **Hotel Miramar in 1939**, *"donde consigue por primera vez la personería jurídica."*
- *"En 1949 comienzan los trabajos de construcción en el predio"* — clubhouse, riding ring and polo
  fields first; current headquarters inaugurated after three years (~1952).
- **STILL WIKI-ONLY:** the "rugby criollo introduced 1949" claim. The club's own history page does
  **not** mention it; it lists rugby only among pitches built later. Hedge or omit.

### STILL NOT FOUND (write around honestly)
- Venue, occasion, players or captain for the **1948 first Test v Chile (lost 21–3)**.
- Who won the 1950 Campeonato, and the scores.
- Biography of **Carlos E. Cat** or **D. Mac Cormack** beyond the offices they held.
- **British Schools of Montevideo**: the 1908 founding and "first to play rugby" claim remain
  wiki-only; no school heritage page found.
- Any fixture record at all between 1900 and 1948, and any touring side visiting Montevideo.
- Carrasco's development as a suburb — no non-wiki social history located.

## GEN 2 BRIEF — REWRITE PASS (1955–1971), adjudicated 2026-07-18
Direct fetching again (Ryan's paper is paginated: 0803ryan1/2/3.htm; Old Christians' own site
`oldchristians.org/club.php` returns **HTTP 400 — dead**, so club history came via viven.com.uy and
search summaries and is weaker).

### VERIFIED non-wiki — Ryan 2008 (irlandeses.org), pages 2–3
- Irish Christian Brothers founded in **County Waterford by Edmund Ignatius Rice**, "a devout Roman
  Catholic and philanthropic businessman."
- *"Cardenal Newman, founded in 1948, was their first school in South America, followed by schools in
  Uruguay, Peru and Paraguay."*
- Stella Maris was an **offshoot of Cardenal Newman after Catholic parents in Uruguay petitioned the
  Brothers**; *"a small group of Irish Christian Brothers opened a school at Carrasco, a leafy suburb
  on the outskirts of the city."*
- *"Moreover, physical education and sport would play a major role in the life of the college."*
- **KEY NUANCE — the Brothers took up rugby "despite the Brothers' historical aversion to British
  sports."** This is the best single detail in the generation: an Irish nationalist teaching order,
  historically hostile to British games, adopting the most British game of all. Do not flatten it.
- Old Christians **founded 1965 by Stella Maris graduates**; *"Reflecting the Irish link, they adopted
  the shamrock as the club's crest."* *"In 1968 they won their first Uruguayan National championship,
  and their second in 1970."*
- Andes: *"They attributed their survival to a great extent to the attitudes and discipline inculcated
  in them by the Brothers."* → carries straight into Gen 3.
- Canessa later "Uruguay's leading paediatric cardiologist," played for a South American XV.
- **BONUS for Gen 0:** Ryan independently corroborates the Confitería Oriental — MVCC *"reappeared
  under its present name at a meeting in 1861 of the original founders, at the fashionable Confitería
  Oriental."* A second, academic, non-wiki source for the cold-open scene. Note Ryan treats Victoria
  CC (1842) and MVCC (1861) as one club reappearing, not two clubs.

### ⚠ OLD CHRISTIANS FOUNDING — THREE conflicting dates; hedge openly in prose
- **Ryan 2008 (academic, non-wiki): 1965.**
- **Club tradition (wiki-tier / viven / search summaries): December 1962**, a mass in the garden of one
  of the club's two "godmothers"; formally constituted during **1963** with statutes; **1965** was the
  "return of all the players," and their first B-division match was won **105–0**.
- **fundacionadastra.uy says 1951 — DEMONSTRABLY IMPOSSIBLE** and self-contradicting: the same page
  says the club was founded by Stella Maris alumni, and Stella Maris did not open until 1955. Reject,
  and treat that site as unreliable generally.
- **Resolution for prose:** the dates are probably different milestones of one process (mass 1962 →
  statutes 1963 → competitive club 1965) rather than a true contradiction. Say so, name Ryan for 1965,
  attribute the early-1960s dating to club tradition, and do not pick a winner.
- **Crest:** Ryan says shamrock. Club tradition describes a **Celtic cross on blue, the emblem of the
  Christian Brothers' congregation, bearing the "Stella Maris" star**. Both are probably right (shield
  vs worn emblem). Describe both; assert neither as the single official account.
- Purpose is uncontested: *"El club 'Old Christians' de Carrasco se fundó para que los alumnos que
  terminasen sus estudios en el colegio 'Stella Maris' de Montevideo, no abandonasen el Rugby"* (viven).
- Titles **1968 and 1970** confirmed by both Ryan and viven (*"hazaña que se volvió a repetir dos años
  mas tarde"*).

### VERIFIED non-wiki — Sudamérica Rugby, the 1950s–60s championships
**1958, the first official Campeonato Sudamericano** (sudamerica.rugby, nid=365): held in **Chile,
October 1958**; Argentina, Chile, Peru, Uruguay; venues Stade Français and Prince of Wales Country
Club (Santiago) and Everton's ground (Viña del Mar).
- 11 Oct: Argentina 44–0 Peru; **Chile 34–9 Uruguay**. 15 Oct: **Argentina 50–3 Uruguay**; Chile 31–3
  Peru. 18 Oct: **Uruguay 10–6 Peru**; Chile 0–14 Argentina.
- Standings: 1 Argentina, 2 Chile, **3 Uruguay**, 4 Peru. Uruguay "mas fuerte en el primer tiempo" v
  Chile; the Peru win "no una buena exhibición de rugby."
- **Named Uruguayans: Guy Furest (kicker), Pedro Blanco, Hugh Ruggeroni.**

**1961, the second — HELD IN MONTEVIDEO** (sudamerica.rugby, nid=368; fetched directly):
- Played **entirely at the Carrasco Polo Club**, matchdays **7, 12 and 14 October 1961**. Four teams;
  *"fue invitado Brasil en lugar de Perú."*
- 7 Oct: Argentina 11–3 Chile; **Uruguay 11–8 Brazil**. 12 Oct: Argentina 66–0 Brazil; **Uruguay 5–28
  Chile**. 14 Oct: Chile 34–5 Brazil; **Uruguay 3–36 Argentina**.
- Standings: 1 Argentina, 2 Chile, **3 Uruguay**, 4 Brazil. *"hubo una notoria mejoría de los
  seleccionados de Uruguay y de Brasil."*
- **Named Uruguayans: Ricardo Moore-Davie, Charles Hughes.**
- → Lovely thread: the polo club the horsemen built in Gen 1 hosts a continental championship.

**1964** São Paulo (Brazil's only runner-up finish); **1967** Buenos Aires — Argentina 1st, Chile 2nd,
**Uruguay 3rd**, and the first edition contested by only three teams. *(Both from a search summary
aggregating Sudamérica Rugby and portaldorugby — weaker than the 1958/1961 pages; hedge or verify
before leaning on detail.)*
- **Argentina won every South American championship from 1958 to 1979** (11 editions 1958–73).
  Same caveat — search-summary sourced; hedge as "every edition" without the precise count.

### ⚠ REJECTED — search-engine artifact
A search summary claimed the 1961 Montevideo tournament saw *"the international debut of Hugo Porta."*
**False.** Porta was born in 1951 and debuted in 1971; a direct fetch of the 1961 article confirms
**Porta is not mentioned anywhere on it.** The engine blended two articles. Do not use.
*(Worth a check in a later pass: whether Porta actually did debut at a Montevideo Sudamericano in 1971
— if so it is a fine cross-chapter thread to Argentina Gen 2. Unverified either way.)*

### STILL NOT FOUND / unverified
- **France XV 61–0 in Montevideo, 1960** (asserted in the old chapter) — not verified in this pass.
  Hedge hard or cut.
- Stella Maris's exact opening date (**May 1955** is the received reading of Ryan) and the founding
  Brothers' names (Doorley, Ryan, Kelly) remain wiki-tier.
- Who won the 1950 Campeonato; Cat's and Mac Cormack's biographies (still open from Gen 1).

## GEN 3 BRIEF — REWRITE PASS (1972–1988), adjudicated 2026-07-18
The crash itself is the best-documented thing in the chapter (Read, Parrado, Canessa, Vierci, Viven,
Guardian) — retrieval effort went instead into the **rugby history around it**, where the old chapter
had almost nothing.

### VERIFIED non-wiki — Sudamérica Rugby, "Triunfo histórico" (nid=950)
- **3 April 1982, Bloemfontein: Sudamérica XV 21 – Springboks 12.**
- **Hugo Porta scored every point**: *"un try convertido, un drop y cuatro penales."*
- **THE URUGUAY LINE — and it verifies the 1981 title non-wiki:** *"cuatro eran de Uruguay, que había
  sido campeón sudamericano el año anterior"* — four of that South American side were Uruguayans, and
  Uruguay **had been South American champion the previous year (1981)**. The old chapter could only
  hedge the 1981 title as wiki-only; it is now carried by Sudamérica Rugby.
- **John Bird**, a Uruguayan prop, described as *"el primer uruguayo en jugar contra los Springboks"* —
  on the **1984** tour.
- ⚠ **TENSION to handle honestly:** four Uruguayans in the 1982 party, yet Bird is called the first
  Uruguayan to *play* against the Springboks in 1984. Most likely the four were squad members who did
  not take the field in the Tests. Do not resolve it silently — hedge, or say only what is safe.
- **CROSS-CHAPTER THREAD (valuable):** this is apartheid-era isolation from the other side. The
  Springboks played whoever would tour, and the South American XV was one of the few who came —
  Uruguayans included. Ties Gen 3 directly to the **South Africa chapter (Gen 4, Barbed Wire)**.
- Ryan separately records **Canessa** — an Andes survivor — playing for "a South American rugby XV."
  Whether that is this side is unconfirmed. Hedge; do not place him at Bloemfontein.

### WIKI-TIER (es.wikipedia, Selección de rugby de Uruguay) — hedge or attribute, do not state flat
- **1981, Montevideo: Uruguay won the XII Sudamericano**, beating Paraguay, Brazil and Chile — **with
  Argentina absent.** Described as the only time before 2014 that anyone but Argentina won it.
  → **The "Argentina absent" qualifier is essential for honesty** and the old chapter omits it. The
  title is real (now non-wiki verified above); the asterisk must travel with it.
- **"Teros"**: the name used by journalists **from 1973**, after the native lapwing. → Striking that
  the national side acquired its name the year after the crash.
- **1979 v Argentina: lost 19–16** — close.
- **1983**: Argentina ended a Uruguayan winning streak; the 1980s opened with **54–14 v Paraguay**.
- **1985: France in Montevideo, beat Uruguay 34–6** — described as France's **second** visit, which
  indirectly supports the old chapter's unverified **1960 France 61–0** claim. Still hedge both.

### NOT relevant to Gen 3 but worth keeping for GEN 6
"Uruguay, un gran finalista" (sudamerica.rugby nid=335) is about the **2020 HSBC Sevens Challenger
Series final at Estadio Charrúa** — Japan beat Uruguay 5–0 after extra time, Matsui's try 2:28 into
the second period of extra time. Uruguayans named: **Felipe Etcheverry (captain), Baltazar Amaya,
Mateo Viñals, Diego García, Guillermo Lietjenstein.** Uruguay beat Hong Kong 12–0 in the semi.

### TONE — the Latham test applies hardest here
Per [[sa-chapter-latham-tone-model]] and the design: the survivors told **from inside, in their own
words**; the anthropophagy **stated plainly, once, without relish and without euphemism**; the dead
kept as people, not material (name **Marcelo Pérez**); and **no sanctification** — the survivors
themselves have consistently resisted being made saints. Avoid instrumentalising the disaster as
proof of the book's argument; the Brothers-formation connection is real and the survivors made it
themselves, but it should be carried in their voice, not asserted as authorial cleverness.

## GEN 4 BRIEF — REWRITE PASS (1989–2003), adjudicated 2026-07-18
The earlier pass listed this generation's facts as "widely reported, not independently verified."
Most are now verified from **World Rugby's own pages**, and two long-standing errors are corrected.

### VERIFIED — World Rugby Hall of Fame, Diego Ormaechea (inductee no. 148, 2019)
https://www.world.rugby/halloffame/inductees/706697
- **Number eight; played for Uruguay 1979–2001; 54 caps, 31 tries; captained in 37 Tests.**
  → ⚠ **CORRECTION.** A search summary gave "73 caps and 16 tries." **Wrong — do not use.** World
  Rugby's own Hall of Fame page is authoritative: 54 and 31. (The page is internally inconsistent by
  one try — "31 tries" then "30 tries from his position"; say 54 caps and leave the try count loose or
  cite 31.)
- *"The last of Ormaechea's 54 caps came against South Africa at Rugby World Cup 1999 when he became
  the oldest player, aged 40 years and 26 days, to appear in the tournament, a record he still holds
  to this day."* (v South Africa, Hampden Park, Glasgow, 15 October 1999.)
- **The Spain try — venue CONFIRMED as the old chapter had it:** he scored *"Uruguay's first in a Rugby
  World Cup match, against Spain at Netherdale in Galashiels in 1999."* Also the oldest try-scorer in
  RWC history. Guinness World Records corroborates the age record.
- **A racehorse veterinary surgeon by profession** (more specific than the old chapter's "veterinarian").
- **MAJOR ARC THE OLD CHAPTER MISSES: Ormaechea then COACHED Uruguay.** Under his direction Uruguay
  qualified for RWC 2003 and *"achieved their second tournament win, 24-12 against Georgia."*
  → Player-captain at the first World Cup, coach at the second. Use this; it restructures the
  generation around one man.
- **Dynasty:** three sons — **Iñaki, Agustín and Juan Diego** — have all represented Uruguay.
- First Uruguayan in the World Rugby Hall of Fame (Americas Rugby News, Sept 2019).

### VERIFIED — RWC 2003
- **England 111 – Uruguay 13, pool stage, Brisbane. Josh Lewsey scored 5 tries.** (world.rugby /
  rugbyworldcup.com, news id 57695.)
- **Pablo Lemoine's try v England is real** — RWC's own video: he *"bundles over"*, through **Danny
  Grewcock** and past a **Joe Worsley** tackle. Also covered by Americas Rugby News, "RWC Rewind
  Uruguay: Lemoine in 2003" (Aug 2019).
- Lemoine scored **two** tries at RWC 2003 — v **Samoa** (60–13, 15 Oct 2003) and v England.
- **Lemoine → Bristol Shoguns ahead of the 1998–99 Allied Dunbar Premiership Two season; the first
  Uruguayan professional rugby player.**

### ⚠ REJECTED / STILL UNVERIFIED
- **"Lemoine was the first Uruguayan to score a try in a Rugby World Cup match" — FALSE.** A search
  summary asserted it; **World Rugby's Hall of Fame page states Ormaechea's 1999 try v Spain was
  Uruguay's first.** Prefer World Rugby. (Lemoine may be first to score against a Tier 1 side — not
  verified, do not assert.)
- **"England conceded only two tries in the whole pool stage, one of them Uruguay's"** (old chapter) —
  still **unverified**. Soften or drop; the Lemoine try stands on its own without the superlative.
- **IRB entry 1989** — still not independently verified. Keep, hedged.
- **"Third most popular sport in Uruguay" after 1999** — still wiki/soft. Keep hedged as reported.
- The 1999 Spain match **date** not confirmed; use "October 1999" not a specific day.

## GEN 5 BRIEF — REWRITE PASS (2007–2019), adjudicated 2026-07-18

### ⚠ SCORE DISPUTE RESOLVED — Bucharest was 39–12, and the old chapter's DATE is wrong
A search summary claimed the second leg was **32–12** and "corrected" my notes. It was wrong. A
contemporary report (TimesLive/Reuters, filed 27 Nov 2010) confirms **Romania 39 – Uruguay 12**.
- **CORRECTION TO THE OLD CHAPTER: the match was 27 November 2010, not 2011.** The old chapter opens
  Gen 5 "on a cold night in Bucharest in 2011." It was late November **2010**, qualifying *for* the
  2011 tournament. Fix this.
- First leg **21–21 in Montevideo**; Romania took the last berth at RWC 2011 on aggregate.
- Romania's five tries: **Csaba Gal, Alexandru Manta, Catalin Fercu, Madalin Lemnaru**, plus a penalty
  try. **Uruguay's two tries: Martin Crosa and Emiliano Caffera.**
- Usable quoted line: *"Romania brushed aside a game but lightweight Uruguay to score five tries in a
  39-12 victory on Saturday that gave them the last berth at the 2011 Rugby World Cup."*
  → **"game but lightweight"** is the perfect contemporary verdict on pre-plan Uruguay. Use it.
- **CROSS-CHAPTER:** this is the mirror of the Romania chapter (Ch. 5) — the same fixture from the
  other side, in Romania's post-communist decline. Worth a nod.
- New detail: Uruguay beat **Kazakhstan 44–7** in the repechage before meeting Romania.

### VERIFIED — the 2007 failure
Two-legged repechage v **Portugal**: lost the first leg in **Lisbon**, won the second in **Montevideo**,
went out on aggregate. (Old chapter: home leg 18–12, aggregate 24–23 — consistent, not independently
re-verified; keep as is or hedge lightly.) Portugal took the place, becoming the only wholly amateur
side at RWC 2007.

### VERIFIED — Kamaishi, 25 September 2019: Uruguay 30 – Fiji 27
Sources: Rugby World, TheSouthAfrican, Hot Springs Sentinel Record (AP).
- Played at the **Kamaishi Recovery Memorial Stadium**, with **a minute's silence before kick-off for
  those killed in the 2011 earthquake and tsunami**. → The scene of the generation: a stadium built in
  a town the sea destroyed, hosting the tournament's first upset.
- **The first upset of RWC 2019**; Uruguay's **first ever win over Fiji**; only their **third World Cup
  win** and first since 2003. (So Namibia 2023 is correctly the fourth.)
- Tries: **Santiago Arata** — team pounced on a loose ball, he darted in and out of defenders and
  crossed under the posts; **Manuel Diana** — drove over low from close range after the pack's build-up;
  **Juan Manuel Cat** — the backs interlinked down the far side.
- **Felipe Berchesi kicked 15 points**, a "nerveless display from the tee."

### STILL UNVERIFIED (keep hedged)
- The URU administrators' framing of **the 2011 failure + Estadio Charrúa as "the two defining events"**
  in the sport's history — asserted in the old chapter, source not located. Attribute loosely
  ("administrators have since described…") or drop the "two defining events" formulation.
- Estadio Charrúa refurbishment date and capacity (~14,000) — keep vague, as the old chapter did.
- 2015 qualification v **Russia** (57–49 agg) and 2018 v **Canada** home and away — not re-verified
  this pass; widely reported, keep.

## GEN 6 BRIEF — REWRITE PASS (2020–2026), adjudicated 2026-07-18

### ✅ THE CURCC CHARTER QUESTION — RESOLVED. Rugby is NOT in it. Rebuild the closing irony.
Third and final pass. **Club Atlético Peñarol's own official history page** (xn--pearol-xwa.org) gives
the founding in detail but **does not quote the charter's list of sports at all**. Secondary accounts
consistently give the purpose as **"cricket, football and other male sports."** *Rugby football is
nowhere attested.*
- **VERDICT: the old chapter's Gen 6 closing irony is WRONG and must not be reproduced.** It reads
  "the club whose charter in 1891 actually named *rugby football* before it dropped the game within a
  year." Delete. Do not hedge it — the positive evidence points the other way.
- **THE REBUILT IRONY IS STRONGER AND TRUE:** the club was founded as, and literally named, a
  **Cricket Club** by railwaymen; it became a football club within a year and then the greatest
  football institution in South America; and 130 years later that same body fields Uruguay's first
  professional **rugby** team. Gen 0 already established **cricket clubs as the incubators of both
  codes** — so the motif closes on documented ground without needing the charter.
- **VERIFIED from Peñarol's own page** (excellent Gen 0 corroboration too):
  **118 founders — 45 Uruguayans, 1 German, the rest English or British** (the club's own tally, which
  upgrades what was previously blog-tier); charter signed **at the company's offices in Villa Peñarol
  near Montevideo, at 8 p.m.**, **written in English**, constituted as a civil association without
  lucrative purpose; **Mr. Roland Moor** presided over the meeting. On **13 April 1914** the Executive
  Power approved new statutes as *"Club Atlético Peñarol, antes denominado 'Central Uruguay Railway
  Cricket Club'"*, establishing legal continuity with 1891.
  *(A secondary source names a "Mr. Henderson" as elected president — possibly distinct from Moor, who
  chaired. Don't name the president; the 8 p.m. meeting detail is safe and better.)*

### ⚠ MY OWN NOTES WERE WRONG ABOUT PEÑAROL RUGBY'S TITLES — corrected here
The earlier session recorded, as a "CORRECTION FOUND & FIXED", that Peñarol won **SLAR 2021
(inaugural) + SRA 2023 + 2025**. **That is incorrect.** The **URU's own franchise page** settles it:
- Peñarol **entered** the competition in 2021 — *"Peñarol representará a Uruguay en la SLAR 2021"*
  (29 Jan 2021) — but did **not** win that year.
- **Titles: SLAR 2022 · Super Rugby Americas 2023 · Super Rugby Americas 2025.** The 2025 final beat
  **Dogos XV**, *"se coronó Campeón del certamen continental por tercera vez en su historia"*
  (16 June 2025).
- **2021 was won by Jaguares XV** (since disbanded); **2024 by Dogos XV**. Five editions, Peñarol three.
- 2023 final: Peñarol beat Dogos XV **23–17**. 2025 final: Peñarol beat Dogos XV **35–34**.
- → **Say "2022, 2023 and 2025", never "2021".** Fix anywhere this appears.

### CARRIED FORWARD (from earlier sessions; not re-verified this pass — keep as previously hedged)
- RWC 2023, Lyon: Uruguay went 14–0 down and beat **Namibia 36–26**; scorers **Baltazar Amaya**,
  **Germán Kessler**, **Santiago Arata**, **Bautista Basso**. Fourth World Cup win (Spain 1999,
  Georgia 2003, Fiji 2019, Namibia 2023 — consistent with Fiji being verified as the third).
- 2021: qualified for RWC 2023 as the top side in the Americas, ahead of the **United States**.
- Homegrown-only playing squad — no residency or heritage call-ups. Keep as the point of pride.
- 2024: **Rodolfo Ambrosio** took over as head coach and turned the squad over deliberately.
- 2025: won the **Sudamérica Rugby Championship** over **Chile** — 28–16 in Santiago, lost the return
  21–18 in Montevideo, through **46–37 on aggregate** → **RWC 2027 qualification, a sixth straight.**
- **2020 HSBC Sevens Challenger final** at Estadio Charrúa: Japan 5–0 after extra time (Matsui, 2:28
  into the second period of extra time). Uruguayans: **Felipe Etcheverry (capt), Baltazar Amaya,
  Mateo Viñals, Diego García, Guillermo Lietjenstein.** Optional colour for the generation's opening.
- July 2026 **World Rugby Nations Cup** hosted at the Estadio Charrúa: beat **Georgia**; drew **36–36
  with Romania** (11 July 2026). Ranked ~15th in the world, second in the Americas behind Argentina.

### ⚠ DATED-SNAPSHOT RULE — the old chapter breaks it; the rewrite must not
Old chapter: *"As this is written, in the middle of 2026"* and *"a match against Hong Kong still to
come on 18 July."* **Both banned by house style.** Close on a fixed, past-tense, explicitly dated
snapshot — **as of mid-July 2026, after the Romania draw** — and do **not** mention any pending
fixture. Point forward only to **RWC 2027 in Australia**, which is dated and settled.

## Sources
(add new links here as you research; existing ones in the chapter's `## Sources`)
- [Club Atlético Peñarol — Our History (CURCC 1891)](https://www.xn--pearol-xwa.org/El-club/Our-History-uc7043)
- [Unión de Rugby del Uruguay — Franquicia Peñarol](https://uru.org.uy/espanol/franquicia-penarol-98)
- [TimesLive/Reuters — "Romania crush Uruguay to reach World Cup" (27 Nov 2010)](https://www.timeslive.co.za/sport/rugby/2010-11-27-romania-crush-uruguay-to-reach-world-cup/)
- [Rugby World — "2019 Rugby World Cup: Fiji 27-30 Uruguay"](https://www.rugbyworld.com/tournaments/rugby-world-cup/2019-rugby-world-cup-fiji-v-uruguay-101598)
- [World Rugby Hall of Fame — Diego Ormaechea](https://www.world.rugby/halloffame/inductees/706697)
- [World Rugby — England v Uruguay, RWC 2003](https://www.world.rugby/news/57695/england-v-uruguay)
- [Americas Rugby News — "Ormaechea becomes Uruguay's first World Rugby Hall of Famer" (2019)](https://www.americasrugbynews.com/2019/09/13/diego-ormaechea-becomes-first-uruguayan-in-world-rugby-hall-of-fame/)
- [Americas Rugby News — "RWC Rewind Uruguay: Lemoine in 2003"](https://www.americasrugbynews.com/2019/08/20/rwc-rewind-uruguay-lemoine-in-2003/)
- [Sudamérica Rugby — "Triunfo histórico" (Sudamérica XV 21–12 Springboks, 1982)](https://www.sudamerica.rugby/english/triunfo-historico-3?nid=950)
- [Hugh FitzGerald Ryan, "The Development of Rugby in the River Plate Region: Irish Influences"](https://www.irlandeses.org/0803ryan1.htm) — SILAS 6:1 (2008); paginated ryan1/2/3
- [Sudamérica Rugby — "El primer sudamericano, en 1958"](https://www.sudamerica.rugby/english/el-primer-sudamericano-en-1958-3?nid=365)
- [Sudamérica Rugby — "1961: El rugby se traslada a Montevideo"](https://www.sudamerica.rugby/english/1961-el-rugby-se-traslada-a-montevideo-3?nid=368)
- [Fundación Viven — Old Christians Club](https://www.viven.com.uy/old-christians-club/)
- [FIFA — AUF 120th anniversary](https://inside.fifa.com/news/auf-celebrates-120th-anniversary-3069452)
- [efdeportes — Albion FC, "profetas del sport en Uruguay"](https://www.efdeportes.com/efd120/albion-football-club-profetas-del-sport-en-uruguay.htm)
- [Americas Rugby News — "The oldest rugby club in the Americas turns 162" (July 2023)](https://www.americasrugbynews.com/2023/07/19/the-older-rugby-club-in-the-americas-turns-162/)
- [Unión de Rugby del Uruguay — Institucional](https://uru.org.uy/institucional-2)
- [Sudamérica Rugby — "El Panamericano de 1951"](https://www.sudamerica.rugby/english/el-panamericano-de-1951-3?nid=363)
- [Carrasco Polo Club — El Club](https://carrascopolo.com.uy/about-us-2/)
