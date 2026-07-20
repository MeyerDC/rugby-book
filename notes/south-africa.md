# South Africa — research notes

Fact + source cache for the South Africa chapter. Write prose *from* here. Sources also at the end of
`chapters/06-south-africa.md`.

## Thesis
The state used rugby to build **not a class but a race** — until a boy from the township of **Zwide**
lifted the trophy twice.

## Generations (established)
- **Gen 0** Winchester football & the two beginnings (1861–1889).
- **Gen 1** Springboks, "the rugby nobody tells you about" (1889–1947).
- **Gen 2** the **Afrikaner capture** & the best team on earth (1948–1969).
- **Gen 3** the split & the word **"collaborator"** (1966–1979).
- **Gen 4** the man in the middle (1980–1991) — isolation / apartheid boycott era.
- **Gen 5** the **No. 6 jersey** (1992–2003) — readmission; **1995** World Cup.
- **Gen 6** the long fall (2004–2017).
- **Gen 7 — Zwide** (2018–2026): **Siya Kolisi**; back-to-back World Cups (2019, 2023).

## Gen 0 — verified brief (checked July 2026)

**Confirmed — do not "correct" these:**
- **George Ogilvie** ("Gog"), b. **1826, Wiltshire**; headmaster of the **Diocesan College**
  (Bishops), Rondebosch, from **1861 until 1885**. Taught **Winchester College football**, not rugby.
  All four details check out.
- **First recorded match: 23 August 1862**, the racecourse at **Green Point**, **0–0**. Officers of
  the **11th Regiment** vs the **Civilians** (Civil Service); reported in the *Cape Argus*.
  ⚠️ rugbyfootballhistory.com says **21 August** — it is the outlier; the 23rd is better attested.
  The chapter's hedge on this is correct, keep it.
- The Winchester game was known at the Cape as **"Gog's Game" / "Gogball"** — *not yet used in the
  prose; free material for Gen 0's "wrong game" section.*
- **Hamilton** (Sea Point) **1875** = first club; **Villagers 1876**. Rugby School code arrives ~1875.
- **William Henry Milton**: England back, capped **1874 and 1875**; arrives **1878**, joins Villagers,
  "playing and preaching the rugby code"; Cape Town abandons the Winchester game within the year.
  Later a colonial administrator in Rhodesia.
- **SARFB founded 21 July 1889, Kimberley** — as the **South African Football Board**. The word
  **"Rugby" was inserted in 1893**, to distinguish it from the **South African Football Association**
  (soccer, founded **1892**). ✅ Genuinely correct and well-attested. Best pub fact in the chapter.
- Unions: **Western Province 1883, Griqualand West 1886, Eastern Province 1888, Transvaal 1889.**
  First inter-provincial tournament, Kimberley **1889**, won by **Western Province**.
- **Western Province Coloured Rugby Union: 1886** ✅ — genuinely predates the white board (1889) by
  three years. This is the load-bearing fact of the chapter's spine and it holds.
- **South African Coloured Rugby Football Board: 1896, Kimberley** ✅.
- **Canon Robert John Mullins**: headmaster of the Kaffir Institution, Grahamstown, **from 1864**;
  the Institution began as a branch of the all-white **St Andrew's College** (separated 1867).
  Son **Cuth Mullins** played forward for the **1896 British touring team** ✅.

**⚠️ Traps and open decisions:**
- **The 1864 date is a conversion, not a source.** Sources say Mullins *became headmaster* in 1864 and
  is "**usually credited** as the first to introduce rugby to blacks" — they do **not** date the rugby
  to 1864. Gen 0 §194 states this correctly and hedged; §186/§192/§196 harden it into a fact.
  §196 is the tell — "eleven years before Hamilton RFC, fourteen years before Milton got off the
  boat" — every clause there is a reason it *cannot* have been the Rugby School code in 1864, since
  the code didn't reach the Cape until ~1875 and didn't win until 1878. **Rugby was first played at
  St Andrew's — the Institution's own parent college — in 1878.** Not yet resolved; recommended fix
  is to shift the weight onto **1886** (verified, institutional, and on-thesis) and keep Mullins as
  the origin story rather than the proof.
- **Stellenbosch: 1883 is contested.** Wikipedia says 1883; Stellenbosch/Maties claim **1875** and
  celebrated 150 years in 2025. The chapter states 1883 flatly and hangs two beats on it ("the
  Afrikaner found it in Stellenbosch in 1883"; "sixteen years before the Anglo-Boer War" — which
  becomes twenty-four if it's 1875). **Undecided.** The Winch thesis or the *Sport in History*
  article should settle it.
- **The Cornish miners have no source** in the chapter's list, and they carry the "Not gentlemen.
  Miners." beat.
- **Unattributed quotes** in Gen 0: "the sources describe" (§123), "the lovely phrase the histories
  use" (§103), and "one historian's brutal phrase — *an opportunity for mauling, rucking, physical
  revenge against an old political foe*" (§137). The last one does real argumentative work and needs
  a name.
- **Club vs union collision:** "The Western Province **club** had ceased to exist entirely" (§87) sits
  70 lines above "**Western Province** — 1883" in the *unions* list. Disambiguate.
- **Boer camp deaths: ~26,000** women and children. Gen 0 and Gen 1 now agree on this figure.

**Fixed on the July 2026 Gen 0 pass:**
- **The chapter-opening generation menu has been cut.** The chapter now opens `# South Africa` →
  `## Generation 0`, matching Uruguay/Argentina/Chile/Georgia/Romania/Scotland. The menu
  (`## The Generations of South African Rugby` + "Researched. And I'll tell you straight away…" +
  a Gen 0–7 list + "Say which one and we begin") was **residue from the source conversation** — the
  assistant's "here's the map, pick one" turn, left behind when `build_book.py` stripped the human
  prompts. It was an H2, so it polluted `pandoc --toc` as a peer of the generations; it spoiled every
  plot point; and as a duplicate surface it had drifted out of sync with the body.
  **Five errors died with it** (all existed *only* in the menu): the 1960 "4–0" v NZ (body: 2–1 with
  a draw); the "seventh" ranking (body: sixth); "four consecutive knockout matches won by a single
  point" (body: **three** — the fourth match was the pool *loss* to Ireland); the Rhodes Cup
  "running from 1898 to 1980… for eighty years"; and the bare "Kaffir Institution" naming.
  ⚠️ **England (`07`) and Wales (`08`) still have the same menu** — same residue, same H2/TOC
  problem. One decision across those two remains open.
  ⚠️ **Gap the cut exposed (did not create):** the menu's Gen 7 line cited "**2021**" — the home
  series win over the **British & Irish Lions**. **Gen 7's body never covers it at all**: it runs
  2018 → 2019 → Bomb Squad → 2023 → 2024 → 2025 → 2026. The 2021 Lions series (and the Erasmus
  refereeing-video saga and ban that came with it) is missing from the chapter entirely. Address on
  the Gen 7 pass.
- "Two beginnings, **four** years apart" (§47, §260) → **two** (1862 → 1864). The frame sentence
  contradicted the body's own "two years later" in three places.
- `## Generation 0` given its theme + year range, matching every other generation heading.
  Range set to **1861–1889** (the body climaxes on the Kimberley board; Gen 1 opens on the same
  hinge year, which matches the book's existing Gen 2/Gen 3 overlap).
- **The Villa Peñarol / Iquique cross-reference was backwards** and has been repointed to
  **Tucumán**. Ch.1 says CURCC *dropped* rugby inside a year and went to football — Villa Peñarol is
  where working-class rugby conspicuously failed to happen. Ch.3's Iquique is the book's **most
  elite-coded** origin ("the game they left behind stayed theirs"). Both were cited as precedents for
  "Not gentlemen. Miners." — i.e. exactly backwards. Tucumán's sugar mills are the real parallel
  ("sugar mills, not polo lawns"). **Do not reinstate the old comparison.**
- Gen 0 and Gen 1 both *revealed* the 1896 Kimberley board with the same "same diamond town / same
  dust" move. Gen 0 keeps the reveal (it closes the "two rugbies" frame and sets up the 1992 tease);
  Gen 1 §382 now calls back rather than re-reveals, and goes straight to the Rhodes Cup.

## Gen 1 — verified brief (checked July 2026)

**Confirmed — do not "correct" these:**
- **1891 tour:** British won **all 20 matches, conceding one point** all tour (224–1). Captain **Bill
  Maclagan**; party invited by the **Western Province union**. Reached the Transvaal (played the
  Wanderers, Johannesburg); series sealed at the Athletic Grounds, Kimberley.
- **1896 series:** British Isles won it **3–1**; SA won the **fourth and final Test, 5 September
  1896, Newlands, 5–0** — the first Test win in SA history (their **7th** Test; 3 in 1891 + 4 in
  1896, having lost the first six).
- **1903 tour:** touring record **11 W, 8 L, 3 D**; SA took the series — sealed by the **third Test,
  12 September 1903, Newlands, 8–0**.
- **Chubb Vigne** = James Talbot Vigne (1868–1955), played **centre in all three Tests of the 1891
  series** — his only caps. Later a furniture-shop owner in Kimberley. ✅
- Anglo-Boer War ends **1902**; ~**26,000** Boer women and children died in the camps. ✅
- **1906–07** first tour of the British Isles; **Springbokken**; captain **Paul Roos**. ✅
- **Sol Plaatje** credentials all check out (founding secretary-general of the SANNC/ANC, *Native Life
  in South Africa*, fought the 1913 Natives Land Act). ✅
- **"the next ninety-six years"** (§234) = 1896 → 1992 exactly. ✅ Keep.
- Jameson Raid "four years away" (Dec 1895) ✅; war "eight years" away (1899) ✅.

**⚠️ OPEN — the Rhodes *and* Kruger claim (§246):**
The chapter calls joint Rhodes/Kruger funding of the 1891 tour "one of the most extraordinary facts
in the history of this game anywhere in the world" and gives it a whole section. **It is a
Wikipedia-only claim, and the Lions' own official history contradicts it:** the party "was invited to
South Africa by the Western Province union and all costs were underwritten by the Cape Colony Prime
Minister, **Cecil Rhodes**" — Kruger unmentioned. The Raeburn Place Foundation agrees. Worse, the
Wikipedia sentence carrying the claim is itself muddled — it is attached to the assertion that 1891
was "the first-ever tour of the British Isles by a team from Southern Africa," which is flatly wrong
(that is 1906, covered later in this same chapter). Not impossible — the tour did reach the Transvaal
— but unsupported. **Dean Allen's *Tours of Reconciliation* (below) is the source most likely to
settle it; the abstract does not, and the full text is paywalled.** Left untouched pending a decision:
either find a real citation or demote to a hedge.

**Fixed on the July 2026 Gen 1 pass:**
- **The green jersey was first worn in 1896, not 1903.** The chapter said "Until the last Test of
  1903, South Africa had no jersey" and told the Heatlie story as a 1903 invention — while, ten lines
  earlier, correctly reporting the 1896 5–0. **They are the same match.** Heatlie left Bishops 1894,
  co-founded **Old Diocesans** 1895; the club's **myrtle green was chosen by Heatlie's wife**,
  reportedly because the dye was cheap and available. He handed out leftover club shirts for the
  **4th Test of 1896** → SA's first-ever Test win (5–0). Recalled as captain in **1903** (Old
  Diocesans had folded; outfitters still had stock) → **8–0**, first series win. The colour stuck
  because it won twice. Section rewritten to join the two halves.
  ⚠️ **Grokipedia says the 1896 jerseys were "borrowed from the Villagers club"** — wrong; it was
  Old Diocesans, per the Old Diocesans Union's own archive. Another reason to distrust that source.
- **1919 was NOT an All Blacks tour.** It was the **New Zealand Army team** (the King's Cup winners)
  touring SA in mid-1919. **Ranji Wilson** — West Indian-descended All Black (1908–14) — was **left
  out of the touring party**, not "sent home," after the SA board required no Māori be included.
  Māori players **Parekura Tureia** and **Charles Tepene** were excluded too (now named in the prose).
  Knock-on fixed: **1928 was the All Blacks' FIRST tour of South Africa**, so "New Zealand tours
  again" was wrong.
- **The 1959 SAARB rename cut from Gen 1** — it was 12 years outside Gen 1's stated range (1889–1947)
  and duplicated almost verbatim in Gen 2 §617, where it belongs (1948–1969). Gen 2's copy kept.
- **The four-boards list de-anachronised** (§410). It claimed "by the 1940s… **four** rugby nations"
  and listed the **South African African Rugby Board** and the **Leopards** — neither of which existed
  under those names until **1959**. Now: **three** boards by the 1940s (SARB, SACRFB 1896, **South
  African Bantu Rugby Board 1935**) plus a fourth later, with the rename signposted forward to Gen 2.
  ⚠️ **The South African Indian Rugby Football Association could not be verified at all** — no
  founding date found in any source. It remains hedged as "later again." (Note: a South African
  Indian **Football** Association was founded in Kimberley in 1902 — that is *soccer*, don't conflate.)
- Residue cut: "Ah — of course. Picking up right where we left off." + orphan rule; "because you
  asked for the real thing"; "Say the word" on the Gen 2 tease.

**⚠️ Still open in Gen 1:**
- **Rhodes Cup** (§364): the count is right (28 tournaments, 1898–1980) but "running parallel to the
  Currie Cup **for the entire lifespan of segregated South Africa**" pre-emptively contradicts Gen 3's
  climax (the 1969 abandonment). Reconcile on the Gen 3 pass.
- **Unattributed:** "I'm going to quote **the historians** plainly" (§312) names no historian;
  "**nearly all former Springboks supported the National Party**" (§320) is a striking claim with no
  source.
- **Insider voice:** "our history" (§256), "our alternate kit" (§270), "the world was always against
  **us**" (§429). Chapter-wide decision, not taken yet.
- §374 still carries the unresolved **1864** Mullins claim (see Gen 0 above).

## Gen 2 — verified brief (checked July 2026)

**Confirmed — do not "correct" these:**
- **Danie Craven**: b. Lindley, Free State, **1910**; **16 Tests, 1931–38**; scrum-half, and also
  capped at centre, fly-half, No. 8 and fullback; SARB president **1956–1993** (longest-serving
  anywhere); IRB chairman **1962, 1973, 1979**; died **4 January 1993**, Stellenbosch. All ✅
- **1949: SA 4–0 New Zealand** ✅. **1951–52 Europe tour: 31 matches, 30 wins, one defeat (London
  Counties)**; Grand Slam; captain **Hennie Muller** ✅. **Scotland 0–44**, Murrayfield, 1951 ✅ —
  and a try really was **3 points** then ✅.
- **1960: SA win the NZ series 2–1 with a draw** (NOT 4–0) ✅; 1960–61 Europe = SA's **fourth** Grand
  Slam ✅. Craven's coaching record **17 from 23 = 74%** ✅.
- **1956**: New Zealand's **first-ever series win** over the Springboks ✅.
- **1958 France tour — the chapter's account at §641 is CORRECT, do not "fix" it:** first Test
  **drawn 3–3, 26 July, Newlands**; second Test **France 9–5, 16 August, Ellis Park**; France take
  the series 1–0. Captain **Lucien Mias**. ⚠️ A web-search summary claims France won on 26 July and
  drew on 16 August — that is garbled; the source page contradicts it.
- **Group Areas Act 1950** ✅; **Reservation of Separate Amenities Act 1953** ✅; NP wins 1948 ✅.
- **Sharpeville: 69 killed** ✅. **Macmillan's "Wind of Change", Cape Town, Feb 1960** ✅ — and
  Macmillan-then-Sharpeville (March 1960) is the **right order**, keep it.
- **SAN-ROC 1963**, a year before Tokyo 1964 ✅; first president **Dennis Brutus**, jailed on Robben
  Island ✅.

**Fixed on the July 2026 Gen 2 pass:**
- **CRAVEN WEEK WAS NOT NON-RACIAL AT ITS FOUNDING.** The chapter claimed (§589, and again in the
  closer §663) that it was "from its founding, non-racial. In 1964." **False, and it flatly
  contradicted Gen 4**, which correctly says Craven forced it open in 1980. Truth: founded **July
  1964, East London, 15 teams — whites only**; opened to all races in **1980**, at Craven's own
  request, a change **first proposed in 1978** that had gone nowhere. Rewritten. This removed Gen 2's
  strongest exhibit for the defence of Craven, which is correct — the credit is real but belongs to
  **1980**, not 1964.
  - **New detail now in the prose:** the idea came from Springbok flanker **Piet Malan in 1949**, to
    mark the **SARB's 75th anniversary** — 1889 (Kimberley) + 75 = **1964**. Ties to the chapter's
    own Kimberley thread.
  - ⚠️ **Dropped:** "His own family calls it, fairly, a **visionary concept**." That quote was
    attached to the false non-racial-founding claim; I could not establish what it actually referred
    to. Re-source before reinstating.
  - ⚠️ **GEN 4 FIX PENDING:** Gen 4 says the first fully open Craven Week was "at **Worcester** in
    1980." The **1980** week was at **Stellenbosch**; **Worcester was 1981**. Year right, venue wrong.
- **The home-series record: 62 years, not 64 — and it had already ended.** §553 claimed, *after* the
  1960 material, that "nobody had beaten South Africa in South Africa in a Test series in sixty-four
  years." Wrong twice: it is **1896 → 1958 = 62 years** (ESPN and Wikipedia both use 62 explicitly),
  and **France had already broken it in 1958** — which the chapter itself says at §641, ninety lines
  later. Rewritten to state the run honestly and tee up the France reveal. Closer (§655) fixed too.
- **Craven's doctorates: THREE, not two.** §517 said "BA, MA, and a PhD in ethnology… then a **third
  doctorate**" — counting the BA and MA toward the total and silently dropping one doctorate. Actual:
  **BA 1932, MA 1933**, then doctorates in **ethnology (1935)**, **psychology (1973)** and **physical
  education (1978)** — 43 years between first and last.
  ⚠️ The old "on the evolution of modern games" descriptor was dropped — could not confirm which
  doctorate it referred to (probably the 1978 physical education one). Re-source if wanted.
- **Rhodes Cup** (§623): "as it had since 1898, **and would until 1980**" — in a generation ending
  1969, pre-empting and contradicting Gen 3. Trimmed to "as it had since 1898." Gen 3 now owns the
  death of the cup.
- "two years before Ellis Park" → **two and a half** (4 Jan 1993 → 24 June 1995), agreeing with Gen 5.
- "30 wins from 31 **in Britain**" → "in Europe" (the 1951–52 tour beat France too, as §541 says).
- Residue: "Say the word" cut from the Gen 3 tease.

**⚠️ Still open in Gen 2:**
- **"Virtually everyone *else* involved in the higher echelons… was a member of the Broederbond"**
  (§495) — "else" has no referent; reads as lifted from a source contrasting with Craven himself
  (who claimed not to be an Afrikaner). Needs a subject or the word goes.
- **Insider voice:** "the most complicated figure in the history of **our** game" (§513).
- **1966 SARU rename** is the Gen 2 tease (§645) *and* the Gen 3 opening beat (§697). Tease→delivery,
  so defensible — but it is the same move twice. Watch on the Gen 3 pass.

## Gen 3 — verified brief (checked July 2026)

**⚠️ THE BIGGEST TRAP IN THE CHAPTER — the split is 1959, not 1966.**
The chapter used to run: *1966 SACRFB renames itself SARU → "that is where the fracture opens" →
Loriston leads the breakaway.* **That is backwards.** Truth:
- **1959: SARFF formed.** **Fourteen unions, 10,000+ players** walked out of the SACRFB under
  **Cuthbert Loriston** (its first president). SARFF existed **1959–1991**.
- **The walkout followed "a bitter power struggle between the Board's general secretary Abdullah
  Abass and Cuthbert Loriston."** It was **not**, at the start, a clash of principle. Personality
  first; principle after.
- **1966: the rump renames itself SARU.** That is what the men who *stayed* (under Abass) did —
  **seven years after** the split, not the cause of it.
- The government's **"multi-nationalism"** offer of the mid-60s is what turned the quarrel into a
  question of conscience. That sequencing is now in the prose.
- **Gen 3's range changed 1966–1979 → 1959–1979**, and **Gen 2's closing tease** re-pointed from the
  1966 rename to the 1959 walkout.
- **1971:** the Proteas became the **first "coloured" team from SA to tour abroad** (2 W, 1 D, 3 L).
  *Deliberately NOT added to Gen 3* — Gen 4 already covers Tobias on that 1971 tour; don't duplicate.

**⚠️ THE RHODES CUP — one timeline, and the chapter had been telling two halves of it.**
Per the National Museum source (already cited), definitive:
- Began **20 August 1898**. **Discontinued 1969.** **South Africa Cup replaced it in 1971.**
  **Reinstated for one year.** **Finally shelved after 1980.** **28 tournaments across 1898–1980.**
- The **28-tournament figure belongs to 1898–1980** — Gen 1 §366 has it right. Gen 3 had borrowed it
  and attached it to **1898–1969** ("Seventy-one years. Twenty-eight tournaments"). Fixed.
- **The reason is specific:** rejection of "the political legacy of Rhodes as an imperialist **and his
  company's exploitation of black workers in the mining sector**" — i.e. **De Beers**. The chapter had
  only "everything he represented." Now in the prose, and it closes the loop to Gen 0's mineral-
  revolution spine (diamonds → Kimberley → both boards → the cup).
- **"They gave up their own history" was wrong and has been cut.** They **replaced** it — the South
  Africa Cup, 1971, nobody's name on it. Killed twice, eleven years apart, on the same principle,
  both times by the people it belonged to. Better than the old version.

**Fixed on the July 2026 Gen 3 pass:**
- The 1959/1966 reversal (above), incl. Gen 2's tease and Gen 3's year range.
- The Rhodes Cup timeline, count, reason, and the 1971 South Africa Cup (above).
- **Montreal:** was "**twenty-eight African nations**… An entire continent walked out." Sources split
  **28 vs 29**, with **29 the more common count** — 22 on the eve, then 8 more African nations plus
  **Guyana and Iraq** (so **not all African**, and Africa has ~50 states, so "an entire continent"
  overstated). Now hedged in-text: "twenty-nine by the most commonly cited count… the sources differ
  on the exact number; they do not differ on the scale."
- **Name standardised to "Abass"** (12 instances, 0 variants) — matching the **AR Abass Stadium**.
  ⚠️ Variants in the wild: **Abass / Abbass / Abbas**. Gen 2's closer had "Abbass"; one source uses
  "Abbas". Do not "correct" it back.
- Residue: "Say the word" cut from the Gen 4 tease.

**Confirmed — do not "correct" these:**
- **November 1977**: SARFF (coloured) + SARA (black) + SARB (white) amalgamate into a nominally
  **non-racial SARB**, IRB-affiliated ✅. SARU under Abass **refused** ✅.
- **Hennie Shields** → Gazelles, and to Argentina ✅. **Timothy Nkonki** → Argentina, plus festival
  matches in France ✅. **Turkey Shields** ✅. All for **CASI's centenary**, 1977 ✅.
- **SARA lineage:** Bantu Rugby Board (1935) → **South African African Rugby Board (1959)** →
  **South African Rugby Association (SARA)** later (year not established in any source found). Team
  is the **Leopards** throughout ✅. (Wikipedia says the African board affiliated with SARB in
  **1978**, vs the Nov 1977 amalgamation — minor conflict, the 1977 source is more specific.)
- **SACOS**: March 1973, nine federations, president **Norman Middleton** ✅. **Gleneagles 1977** ✅.
  **1969–70** Springbok tour demonstrations ✅.

**⚠️ Still open in Gen 3:**
- **Duplication with Gen 5.** Gen 3's "The verdict nobody wants" (§869–873) and Gen 5 (§1150ish) run
  the *same* beat: ANC left apartheid sports structures intact / **May 1990 National Sports Congress**
  / mantra "**turned on its head**" / **SACOS disbanded 2005**. Same facts, same phrasing. One
  generation should own it — editorial call, not taken.
- **Insider voice:** "it mattered most to **us**" (§893).
- ✨ **Unused, and flagged as risky:** a News24 tribute says Loriston's vision was to play "**normal
  sport in an abnormal society**" — the exact inversion of SACOS's slogan, and almost too good for a
  chapter built on two roads. But it appears in a community-newspaper piece and reads like it may be
  the **journalist's** construction echoing SACOS rather than Loriston's own words. **Do not use
  without a better source.**

## Gen 4 — verified brief (checked July 2026)

**⚠️ RUGBY NEVER EXPELLED SOUTH AFRICA — the chapter had this backwards.**
The old text said "**South Africa was banned from the IRB from 1984 to 1992**" and "the 1981 tour was
the last official Test rugby the Springboks played until 1992." Both wrong:
- **South Africa remained a member of the International Rugby Board throughout the apartheid era**
  (Wikipedia's own *Rugby union and apartheid* page says so, contradicting the *Rugby union in South
  Africa* page that the "banned 1984–92" claim comes from — that article has now failed three separate
  checks; see also the 1891 Rhodes/Kruger claim and the green jersey).
- **Contrast:** the **IAAF expelled SA in 1976**; the Olympic movement expelled them. **Rugby did
  not.** Craven had chaired the IRB in 1962, 1973 and 1979 and stayed SARB president to 1993.
- **This strengthens the chapter's own argument** (Gen 1: "For decades, the world simply agreed").
  The isolation was imposed from *outside* rugby — governments, Gleneagles, Montreal, SACOS's veto —
  while rugby's world body kept SA's seat and simply stopped inviting them. Now written that way.
- **The real Test timeline:** **1984 England toured and lost both Tests** (incl. the 35–9 at Ellis
  Park where Tobias scored — the chapter contradicted itself on this). **Eight Springbok–Jaguars
  matches in the early 80s, all SA-capped.** Then **1985–1991: not one Test against an established
  country.** Only makeshift sides — **Cavaliers 1986**, **World XV 1989**.

**Fixed on the July 2026 Gen 4 pass:**
- **Tobias debuted at OUTSIDE CENTRE**, not fly-half (30 May 1981 v Ireland, Newlands). §945 already
  said "in 1984 he moved to fly-half" — the chapter contradicted itself. Fixed.
- **The flour bomb hit All Black PROP GARY KNIGHT** in the head — a **450g bag of flour** — not "the
  All Blacks' fullback." ⚠️ The likely source of the error: **Allan Hewson**, the fullback, kicked
  the injury-time penalty that won it 25–22. Two different men. Do not merge them again.
  - ✨ Added: SA captain **Wynand Claassen** asked whether New Zealand had an air force. Also that
    protesters in the ground fired **flares** onto the grass.
- **The lockout section rewritten** (above).
- **Craven Week venue: 1980 was STELLENBOSCH, not Worcester.** (Worcester was **1981**.) Year was
  right, venue wrong. Also added that the change was first proposed in 1978. This was the fix queued
  by the Gen 2 pass.
- **Harare sequencing was backwards.** The chapter had Harare → "**On 7 May 1988**… Cape Sun". The
  Cape Sun meeting (7 May) came **first**; **Harare was October 1988** (20 Oct). Reordered, and the
  October date added.
  - ✨ Added, verified: the ANC delegation at Harare was led by **Alfred Nzo** and included **Thabo
    Mbeki**. (Fuller sequence found but not used: Craven sent Luyt to **London, Feb 1988** to meet the
    Pahad brothers → **Frankfurt**, ~May 1988, to meet Mbeki → **Harare, Oct 1988**.)
- Gen 3→Gen 4 tease re-pointed off "gets banned from the IRB".
- Residue: "Say the word" cut from the Gen 5 tease.

**Confirmed — do not "correct" these:**
- **Glenville, 25 September 1981**, Schenectady County, NY — **29 spectators**, lowest attendance ever
  at an international ✅. SA won 38–7. Last match of the tour ✅.
- **Eden Park, 12 Sept 1981**: **201 arrests**, **90+ police and protesters injured** ✅. NZ won 25–22.
  Cessna 172, **Marx Jones** and **Grant Cole** ✅.
- **Jaguars, 3 April 1982, Bloemfontein: 21–12, Porta scored all 21** ✅. SA capped those Tests,
  Argentina didn't ✅. **Cavaliers 1986** unsanctioned ✅.
- Tobias: b. **18 March 1950** ✅; **6 caps 1981–84**, 21 games, 22 points ✅; 23–15 then 12–10 v
  Ireland ✅; first Black mayor of Caledon 1995 ✅.

**✅ ADDED July 2026 — the 1989 World XV centenary tour (new `### The centenary` section).**
This was the missing evidence for the IRB point above, and it is stronger than the point itself.
- **Sanctioned by the IRB. Funded by South African Breweries.** Both facts sit on the same Wikipedia
  page (*Rugby union and apartheid*) as the "SA remained an IRB member" fact — mutually reinforcing,
  and that page has been reliable where *Rugby union in South Africa* has failed three times.
- **Two Tests, SA won both: 20–19 at Newlands; 22–16 at Ellis Park, 2 September 1989.**
- **Every traditional rugby nation bar NEW ZEALAND supplied players** (NZ had been through 1981).
- **Willie John McBride** took part and was unrepentant.
- **Desmond Tutu** called the IRFU's support "**obscene**" — "when black children were being beaten,
  tear-gassed and detained without trial."
- **Two existing threads it closes:** (1) SAB is named in **Gen 3** as the big business that backed
  apartheid and starved SACOS of sponsorship — so the brewery that would not fund Black rugby paid
  for the white board's party; (2) the SARB centenary is **1889 + 100**, the Kimberley board from
  Gen 0.
- **Placed AFTER Harare, not inside "Inventing opponents"** — because it is Aug/Sept **1989** and
  Harare was **Oct 1988**, and because the juxtaposition is the point (Craven meets the banned ANC;
  ten months later the IRB blesses his board's birthday party). The new section explicitly corrects
  the "Inventing opponents" premise rather than sitting inside it.
- The lockout section's "It simply stopped inviting them to things" was **cut** — too generous, and
  now contradicted by the tour it sanctioned. Replaced with a forward tease.

**⚠️ Still open in Gen 4:**
- **Cold-open chronology is loose:** the opening scene has Craven phoning Tobias about **New Zealand**
  (tour was July–Sept 1981), then cuts to the **Ireland** debut (**30 May 1981**) — which came first.
  Defensible as written but worth a look.
- **Insider voice:** "it wasn't **ours**… what **our** rugby did to *their* country" (§1086).
- **Unverified:** the **7 May 1988 Cape Sun** date itself (kept; presumably from 2Sides2Everything).

## ⚠️ THE ATTRIBUTION AUDIT (July 2026) — read this before touching the Afrikaner material

**Finding: the chapter had invented its own scholarly authority.** Five characterological claims about
Afrikaners were introduced with "in the words of **the historians**", "I'm going to quote **the
historians** plainly", "**the historians** are blunt", "one **historian's** brutal phrase."

**No historian said any of it.** Traced to the primary sources:
- **South African History Online**, *The Early History of Rugby in South Africa* — verbatim source of:
  "nearly all former Springboks supported the National Party"; "Afrikaners viewed the success of the
  Springboks… as a reflection of their accomplishments as a civilization"; "This effect was surely
  intentional." **SAHO cites no sources anywhere in that article** — confirmed by direct fetch.
- **rugbyfootballhistory.com** — verbatim source of "an opportunity for **mauling, rucking, physical
  revenge against an old political foe**." It is that site's own uncited narrative prose, in its
  "Apartheid" section. **A hobbyist rugby site, called "one historian" by the chapter.**
- Both Wikipedia pages (*Rugby union in South Africa*, *Rugby union and apartheid*) contain **none**
  of these claims — checked directly. So the chapter went *below* Wikipedia for its harshest material
  and then dressed it as scholarship.

**A traceable distortion, too:** SAHO says the Springbok symbolised racial superiority **"to the
hard-line Afrikaner."** The chapter dropped "hard-line" and universalised it to **"Afrikaners"**
(Gen 2 closer, and Gen 5 §1198: "Afrikaners still saw it as a symbol of their racial superiority").
The original menu had kept the qualifier ("in the hard-line reading"). The body lost it.

**⚠️ TWO RULES LEARNED THE HARD WAY ON THIS PASS:**
1. **Never write about the book's own drafts or editing in the prose.** The first rewrite said "which
   is what this chapter did in an earlier draft" and "two accounts this chapter has been leaning on."
   A reader has no idea what that means — it is the same category of residue as "Say the word", just
   editorial instead of conversational. **Source-hedging IS house style** (Uruguay §89 and Chile §43
   both discuss the thinness of the record openly) — but that is about *the historical record*, never
   about our own revisions.
2. **Declining to narrate is not neutrality, it is just a worse chapter.** The first rewrite replaced
   invented claims with a refusal to tell the story at all. The discipline belongs on *claims*
   (no fabricated attributions, no telling a people what it believed), **not on storytelling**.
   The fix was to tell **both sides** properly — see below.

**✅ THE OTHER SIDE — now told (Gen 1, "What the Springbok was becoming", rewritten again):**
The section now opens with what rugby *meant* to Afrikaners before what it *became*, because the
chapter already grants Black rugby its interior life in Gen 0 (identity, the dances, communities
united across religious lines) and had granted Afrikaners only an indictment. Giving both their
interior life is **consistency, not special pleading**.
- 1902: a defeated people — republics gone, farms burned, **26,000** women and children dead in the
  camps, the men who did it now governing them, and within twenty years many off the land and at the
  bottom of the Johannesburg labour market.
- They had taken the game at Stellenbosch **sixteen years before the war** — so when the reason for
  revenge came, there was already somewhere to put it.
- **1937 tour of New Zealand — VERIFIED, newly added, fills a real Gen 1 gap** (the chapter had
  nothing between 1906 and the "other rugby"): SA won the series **2–1**, **13–6 Christchurch**,
  **17–6 Eden Park**. **The only Springbok side ever to win a Test series in New Zealand.** Nicknamed
  **"the Invincibles"**; New Zealanders called them **the best team ever to leave New Zealand**. The
  tactics came by **telegram from Paul Roos** — the 1906 captain, 31 years on — reading **"skrum,
  skrum, skrum."** (Ties 1906 to 1937 through one man; Roos was already in the chapter.)
- Then the second half, unflinching: Broederbond → 1948 → the NP claims the emblem for one nation.
- The hinge is now stated precisely: *"The problem was never that Afrikaners loved rugby. Everybody in
  this book loves rugby… The problem is that the institutions carrying the love were the same
  institutions carrying the ideology, run by the same men."*
- Ends holding both truths: whatever it meant in Stellenbosch, to Black South Africans it meant the
  police, the army and the government. **"Both of those are true, at the same time, about the same
  shirt."**

**Fixed — all five sections rewritten from scratch (July 2026):**
- Gen 0 §95: the "mauling, rucking" phrase **cut** (it is a hobby site's prose, not a historian's).
- Gen 1 "What the Springbok was becoming": **rewritten**. Now states the documented institutional
  record (Broederbond → 1948 vote → NP claims the emblem for one nation) and **explicitly declines**
  to say what Afrikaners believed, naming the sourcing problem in the prose. Keeps the mechanism,
  which never depended on private belief.
- Gen 1 leaves-behind: "Springbok success became evidence of a civilisation's worth" → "by 1948 the
  same men ran the board, the brotherhood and the party."
- Gen 2 §481 "surely intentional": **rewritten** — intent no longer asserted. The stronger argument
  is used instead: the Separate Amenities Act covered public amenities; the fields *were* public
  amenities; no separate intent needs proving.
- Gen 2 closer §665: "in the words of the historians… Afrikaner racial superiority" → "that the
  governing party had claimed for one nation inside the country."
- Gen 5 §1198: "Afrikaners still saw it as a symbol of their racial superiority" → "a section of the
  white crowd was determined to prove them right… it was in the stands, for everyone to see." Claim
  now rests on **observable behaviour** (Die Stem, the old flags), not on inferred belief.

**Also expanded — Des van Jaarsveldt (Gen 2).** Was a data point proving the Broederbond's reach; now
a person. A white, English-speaking Springbok captain who won and was never picked again, for not
speaking Afrikaans and declining the team prayer. **This is thesis-critical**: it shows the
institution breaking its own, which is the book's argument ("institutions do this, not peoples") and
the single best answer to the charge that the chapter is an indictment of one people.

**⚠️ THE REAL SCHOLARSHIP IS UNREAD.** The authority on Afrikaner rugby is **Albert Grundlingh**,
Professor Emeritus of History at **Stellenbosch** — an Afrikaner historian — editor with **André
Odendaal** and **Burridge Spies** of ***Beyond the Tryline: Rugby and South African Society***
(Ravan Press, 1995), and author of *Playing for Power: Rugby, Afrikaner Nationalism and Masculinity
in South Africa*. **He has NOT been consulted.** Added to Sources, flagged as unread.
- If the chapter wants to make characterological claims about Afrikaner rugby culture, **Grundlingh
  is how you earn the right** — and the fact that the sharpest such analysis comes from a Stellenbosch
  Afrikaner makes it self-examination rather than an outsider's indictment. That is a completely
  different book to read if you lived through it.
- **Do not reinstate any "the historians" phrasing** unless a historian is actually named.

## Chapter-wide traps (found July 2026, not yet all fixed)

- **Habana is 2nd all-time on 67 tries — AHEAD of Campese (64), behind Daisuke Ohata (69).**
  Chapter says "behind only David Campese." Wrong.
- **Habana 2007 = 8 tries**, equalling Lomu's *single-tournament* record. The **career 15** was
  equalled in **2015** (hat-trick v USA). Chapter conflates the two.
- **SA 36–0 England, 14 Sept 2007, was at the Stade de France**, not Lens. Lens hosted SA v Tonga.
- **There was no first-ever home defeat to Wales under Coetzee.** Wales's first win in South Africa
  was **2022, Bloemfontein**, under Nienaber. In 2014 SA survived 31–30 at Nelspruit.
- **The flour bomb hit prop Gary Knight**, not "the All Blacks' fullback."
- **No world rankings existed in 1995** — "ranked ninth" going into that World Cup is an anachronism
  (rankings began 2003).
- **The Rhodes Cup has one story, not two.** Begun **20 Aug 1898**; **discontinued 1969** in rejection
  of Rhodes; replaced by the **South Africa Cup in 1971**; briefly reinstated; **finally shelved
  1980**. **28 tournaments across 1898–1980.** The chapter currently says 1980 in two places and 1969
  in another, and attaches the 28-tournament figure to both spans.
- **South Africa was never expelled from the IRB.** It remained a member throughout (Craven *chaired*
  the IRB in 1979). Isolation came via boycott and non-invitation to RWC 1987/1991.
- **England toured SA in 1984 and lost both Tests** — so "the 1981 tour was the last official Test
  rugby the Springboks played until 1992" is wrong, and the chapter itself describes Tobias starring
  in the 35–9 Ellis Park Test of 1984.
- **Tobias debuted at outside centre** (30 May 1981 v Ireland), not fly-half. Fly-half came in the
  **1984** England Tests.
- **France won a series in South Africa in 1958** — so the home unbeaten run is **1896–1958 (62
  years)**, not "sixty-four years" as of 1960. The chapter states both.
- **The 1960 NZ series was won 2–1 with a draw**, not 4–0 (the menu says 4–0; the body is right).
- **Ranking after Albany: sixth** per RugbyPass. Menu and Gen 5 tease say seventh.
- **Mapimpi's try** was genuinely SA's first in a World Cup final — but "**108 years**" corresponds to
  nothing; they had played three finals.

## Verified good — Gen 7 (checked July 2026)
The 2025 end-of-year tour material all checks out: **France 32–17** in Paris (8 Nov 2025, 14 men after
Lood de Jager's red card, **Kolisi's 100th cap**, 9th Springbok centurion); **Italy 32–14** Genoa;
**Ireland 24–13** Dublin (22 Nov); **Wales 0–73** Cardiff (29 Nov) — Wales's record home defeat.

## To research / open threads
- Stellenbosch founding date (1875 vs 1880 vs 1883) — settle via Winch thesis or *Sport in History*.
- A source for the Cornish miners.
- Gens 1–7 have not had a line-by-line verification pass; only the chapter-wide traps above.

## Sources
- [Sir William Milton: a leading figure in public school games, colonial politics and imperial expansion 1877–1914](https://scholar.sun.ac.za/handle/10019.1/79890) — Jonathan R. T. Winch, Stellenbosch University, 2013. **Not yet in the chapter's Sources list; should be.** Real academic source, free full text, covers Milton and the Cape sporting scene; likely settles Stellenbosch.
- [A history of the South African Rugby Football Board (SARFB): early years, 1889–1914](https://www.tandfonline.com/doi/abs/10.1080/17460263.2020.1824165) — *Sport in History* 41(3). The authority for Gen 0/Gen 1 institutional dates.
- [South Africa's Black Rugby Tradition – from the Rhodes Trophy to the South Africa Cup, 1898–1971](https://nationalmuseumpublications.co.za/south-africas-black-rugby-tradition-from-the-rhodes-trophy-to-the-south-africa-cup-1898-1971/) — the authority for the Rhodes Cup timeline.
- [History of South African Rugby](https://www.rugbyfootballhistory.com/south_africa.html) — Ogilvie, Milton, Hamilton/Villagers, WPCRU 1886. (Gives 21 Aug 1862 — outlier.)
- [Sport in pre-union South Africa](https://en.wikipedia.org/wiki/Sport_in_pre-union_South_Africa) — Green Point 1862, 11th Regiment, "Gog's Game".

⚠️ **Sourcing note:** the chapter cites **16 Wikipedia links and 4 Grokipedia links**, against
`SUMMARY.md` §5's "Wikipedia is NOT cited (repo rule)". Grokipedia is AI-generated and should not be
a citation. The strong sources (Winch, *Sport in History*, Project MUSE, the UFS journal, the
Stellenbosch "Barbed-Wire Boks" thesis) are in the bibliography but are **not** the ones the prose
actually rests on. Book-wide issue — Wales (15) and Georgia/England/Scotland have it too.

---

# FROM-SCRATCH NO-WIKI RESEARCH (July 2026) — supersedes earlier per-gen briefs above where they conflict

## GEN 0 BRIEF (1861–1889) — definitive, no-wiki

### FACTS

**Ogilvie**
- Rev. George Ogilvie ("Gog"), b. 1826 Wiltshire; Winchester alumnus; headmaster Diocesan College (Bishops) 1861–1885. Before Bishops: ~3 yrs head of St George's Grammar School, Cape Town; 27 boys followed him (59 pupils on arrival).
- CORRECTION to "taught Winchester football": Winch PhD (citing Dobson, *Bishops Rugby*): Ogilvie introduced **"a mixture of Winchester and Bradfield rules in 1861"** — he had been second master at Bradfield in the early 1850s. A hybrid of his own making, called **"Gog's game / Gogball"** (from the only legible letters of his signature). Never written rules. — Winch thesis pp. 39–40 (scholar.sun.ac.za/handle/10019.1/79890).
- Van der Merwe (peer-reviewed) independently: the Cape game "appears to have been a creation of Canon Ogilvie… and not the traditional Winchester Game as commonly believed."

**First recorded match**
- **23 August 1862** (a Saturday) — Winch p. 38, citing *Cape Argus* 25 Aug 1862 directly. Officers vs Civil Service, Green Point; 0–0 draw confirmed. Governor Wodehouse attended; John X. Merriman played for Civil Service. "21 August" is SAHO/hobbyist error (SAHO cites no sources).
- "11th Regiment" for that match unconfirmed non-wiki → say "officers of the garrison". Venue: Green Point Common (not "racecourse").
- Argus wording suggests it was NOT the first football played — Bishops had its own game from 1861.

**Arrival of the Rugby code**
- 1873: J.J. Graham committee codifies "Cape rules" (15 rules, *Standard and Mail* 7 June 1873) — local code, not rugby.
- **Hamilton RFC founded 14 March 1875** (Hamilton Ross & Co offices, Adderley St; named after Hamilton Academicals). Club's own history: the 1875 game "was not rugby football… the rules did not reach the Cape until 1878."
- **Villagers 1876**: breakaway from Western Province Club when WP members pushed Rugby rules; loyalists under Howard Jones — Winch p. 41.
- Rugby nearly died at first attempt: first Rugby-rules match, WP Club vs Villagers, Rondebosch, **15 July 1876** — *Cape Times*: "not by any means a successful performance… (and we hope for the last time)". WP Club's football section folded early 1877 — Winch pp. 41–42.

**Milton**
- England caps: 23 Feb 1874 vs Scotland (Oval, 20-a-side); 15 Feb 1875 vs Ireland (first England–Ireland international) — Winch pp. 33–34.
- Arrived Cape Town **late 1877** (not 1878); civil service clerkship 4 April 1878.
- Joined **Villagers** winter 1878 — committee refused rugby; found allies at **rival Hamilton's** (Billy Simkins, 21). July 1878 first Milton-organised rugby match; **Aug 1878 Hamilton's adopted RU rules unanimously** (first Cape club); **May 1879** Villagers' AGM switched (Graham moved, Milton seconded); Bishops converted 1879 grudgingly ("Well, if you boys want to kill yourselves, do so!" — Ogilvie, per Dobson). Conversion took TWO seasons (1878–79), Hamilton's before Villagers — Winch pp. 44–46.
- Later: private secretary to Rhodes; Administrator of Southern Rhodesia; SARFB president.

**STELLENBOSCH — SETTLED**
- **1875, not 1883.** Peer-reviewed: F.J.G. van der Merwe (SAJRSPER, AJOL sajrs/25870): founded 1875 "and not in 1880 as formerly believed", on *Daily News* 21 Aug 1875 evidence. Winch p. 41 quotes the same paper. BUT the 1875 club played **Cape rules**; rugby only from 1878–79. The "1883" error likely conflates the WP union/Grand Challenge Cup of 1883 (from rugbyfootballhistory.com). Rewrite: "founded 1875 as a football club; entered Cape Town's rugby competition in the 1880s as the first country club" (Winch p. 48). The "sixteen years before the Anglo-Boer War" line must go (1875 = 24 years before).

**Provincial unions & the Board**
- WP **1883** (Hamilton's called the meeting; Giddy president, Milton VP; Grand Challenge Cup launched; Hamilton's champions 1883, Villagers 1884) — Winch p. 46.
- Griqualand West **1886**, Eastern Province **1888** — Winch p. 49. Transvaal: phrase via the Board's 1889 formation (discrete 1889 union founding is wiki-tier).
- **SARFB founded 1889, Kimberley** (WP, GW, EP, Transvaal) — Winch p. 49; Griquas' own history; *Sport in History* 41:3 (2021) "A history of the SARFB: early years, 1889–1914" (paywalled).
- Name: founding name **lacked "Rugby"**; oldest surviving constitution 28 May 1894 shows "Rugby" inserted (peer-reviewed). SAFA (whites-only soccer) founded **1892** (Bolsmann, Aston repository PDF). The precise "1893" year + explicit motive = WIKI-ONLY. Rewrite accordingly.
- **1889 tournament**: first inter-provincial tournament, Kimberley, won by **Western Province**; silver cup from the Board (predates Currie Cup, first contested 1891/92). Kimberley's 1884 tour of Cape Town = first inter-provincial rugby (Dobson: "the first rugby adventurers…").

**MULLINS — VERDICT: the 1864 rugby claim is a date-conversion error**
- Robert John Mullins (**1833–1913**, per Rhodes Cory Library diary catalogue) became **principal of the Kaffir Institution, Grahamstown, in 1864** — that date is his headmastership, NOT rugby.
- Rugby rules reached the Cape only in **1878**. **St Andrew's first played rugby 13 April 1878** (vs the Public School, later Graeme College; lost one try to one goal) — saschoolsports.co.za; rugby365 (no byline — flag).
- Non-wiki sources linking Mullins to rugby are **undated** ("first aroused Xhosa interest in the game"). NO non-wiki source gives 1864 for rugby.
- **St Andrew's own published history contains NO Mullins-rugby claim** — Mullins appears only as a House name (1921); earliest rugby mentioned is the 1926 XV.
- Earliest documented Black rugby: **1887, first Black adult teams in PE and Grahamstown** (Odendaal/Snyders via Financial Mail 26 Oct 2023); Lily White RFC, Grahamstown, 1894.
- Chapter guidance: Mullins became head in 1864; **from the late 1870s** he is "usually credited" with awakening Xhosa interest; hard evidence of Black clubs from 1887. Institution separated from St Andrew's 1867 (weak sourcing — hedge).
- Son: **Reginald Cuthbert "Cuth" Mullins**, Grahamstown-born, Oxford lock, toured with the **1896 British Isles team**, 2 Tests incl. the Kimberley series-clincher (lionsrugby.com; ESPN).

**WPCRU / Black boards**
- **Western Province Coloured Rugby Union 1886 — CONFIRMED peer-reviewed** (Winch p. 49). Predates the white national Board (1889) by three years.
- **SACRFB founded Savona Café, Kimberley, 19 August 1897** (Snyders, National Museum) — NOT 1896. First Rhodes Cup tournament 20–27 Aug 1898, Kimberley.

**Cornish miners**
- The "Cornish miners introduced rugby" claim exists only on the Cornish Mining WHS page, uncited, contradicted by all scholarship. Winch never mentions Cornish rugby. Defensible weaker version only: Cornish miners numerous at Kimberley (1870s) and Rand (~25% of white miners pre-1899), part of rugby's mining-town constituency — NOT the vector. → The Gen 0 "Tucumán's mechanism… Miners." passage must be rewritten or cut.

**Mission schools**
- Authority: **André Odendaal** — "South Africa's Black Victorians" (Mangan ed., 1988); "'The Thing That is Not Round'" in *Beyond the Tryline* (1995) pp. 24–63; *The Story of an African Game* (2003). Zonnebloem College, post-Cattle-Killing, Sir George Grey; same elite founded sport clubs and the ANC. Xhosa name for rugby: *umbhoxo*, "the thing that is not round". Active specialist: Hendrik Snyders (National Museum, Bloemfontein).

### CONTESTED (Gen 0)
- 1862 date: **23 Aug** (Winch ← Cape Argus) vs 21 Aug (SAHO unsourced). Use 23.
- Stellenbosch: **1875** (Van der Merwe) vs 1880 vs 1883 (hobbyist). Use 1875, Cape-rules club.
- Milton arrival: **late 1877** (Winch definitive).
- "Converted the Cape in one season" = myth-compression; took 1878–79. Milton's own words date "the real beginning" to May 1879.
- Mullins birth: **1833** (Cory Library) vs 1838 (WikiTree). Use 1833–1913.
- SACRFB: **1897** (Snyders archival) vs 1896 (loose secondary). Use 1897.

### WIKI-ONLY (drop/hedge)
- "Founded 21 July 1889" (day precision) → "in 1889, in Kimberley."
- "'Rugby' inserted 1893 to distinguish from SAFA" → rewrite: founded 1889 without "Rugby"; by the 1894 constitution — after soccer's SAFA claimed the name in 1892 — the word had been inserted.
- Mullins-1864-rugby → drop entirely.
- Ogilvie death date/place → omit.
- "11th Regiment" in the 1862 match → "officers of the garrison."

### QUOTES (Gen 0, exact)
- "…the first time within our recollection that so large a party of gentlemen have made a public appearance at Cape Town in this manly English school-game." — *Cape Argus*, 25 Aug 1862 (via Winch p. 38).
- "We have never seen so thoroughly plucky a game…" — *Cape Argus*, 25 Aug 1862.
- "At no time were there written rules for Gog's game…" — Dobson (via Winch p. 39).
- "Rugby Union rules were adopted for the afternoon (and we hope for the last time)." — *Cape Times*, 18 July 1876.
- "John Graham moved and I seconded a resolution that the Villager's should play under Rugby Union rules… the real beginning of the Rugby Union game in the Cape." — William Milton, in Difford p. 457 (via Winch p. 45).
- "Well, if you boys want to kill yourselves, do so!" — Ogilvie on permitting Bishops rugby (Dobson).
- "the young Boers took to the game like ducks to water…" — Difford (via Winch pp. 47–48).
- "They were the first rugby adventurers, the first tourists, the first, really, to play inter-provincial rugby in South Africa." — Dobson on Kimberley 1884.
- "Black rugby has a long, proud and largely forgotten history in South Africa." — Hendrik Snyders (Financial Mail, 26 Oct 2023).

### KEY SOURCES (Gen 0)
1. Winch, *Sir William Milton…*, PhD, Stellenbosch 2013 — FREE PDF, mined in full; carries primary citations. scholar.sun.ac.za/handle/10019.1/79890
2. Van der Merwe, "Oorspronklike voetbal aan die Kaap…", SAJRSPER — ajol.info/index.php/sajrs/article/view/25870
3. "A history of the SARFB: early years, 1889–1914," *Sport in History* 41:3 (2021) — DOI 10.1080/17460263.2020.1824165 (paywalled)
4. Dobson, *Rugby in South Africa 1861–1988* (1989); *Bishops Rugby* (1990) — via Winch
5. Difford, *History of South African Rugby Football 1875–1932* (1933) — via Winch
6. Odendaal — *Beyond the Tryline* (1995); "Black Victorians" (1988); *The Story of an African Game* (2003)
7. Snyders, National Museum Bloemfontein — Bud Mbelle/SACRFB pieces (nationalmuseumpublications.co.za)
8. Hamilton RFC foundation history — hamiltonrfc.co.za (candid about 1875 ≠ rugby)
9. Bolsmann, "White Football in South Africa…" — Aston repository PDF (SAFA 1892)
10. Rhodes Cory Library, Mullins diary record (1833–1913) — commons.ru.ac.za
11. FLAGGED leads only: SAHO (cites nothing; likely origin of "21 August"); rugbyfootballhistory.com (likely origin of "1883 Stellenbosch"); rugby365 St Andrew's profile (no byline).

---

## REWRITE DESIGN (agreed with author, July 2026) — binding for the new draft

1. **New file**: draft at `drafts/06-south-africa.md` (NOT in `chapters/` — combine_book.py bundles every .md there). Write ONLY from this notes file. Do not open the old chapter while drafting; it returns at the end as a fact-checklist, never as text. On approval it replaces `chapters/06-south-africa.md`.
2. **Structure**: keep the book's Gen 0–7 spine. Within it, the story runs as parallel perspectives, EACH TOLD FROM INSIDE:
   - The Afrikaner game — from their side: 1899–1902 defeat, the camps, the poverty; the conqueror's game turned into an act of restoration (Dean Allen's "beating them at their own game" thesis; Grundlingh on meaning-making). The reader must FEEL why the jersey became sacred. The ideology is then shown as institutions doing what closed institutions do — including to their own (Van Jaarsveldt).
   - The Black/Coloured game — from their side: mission schools, the 1886 WPCRU, the 1897 board, Rhodes Cup, SACOS. A complete rugby history, not a footnote to the white one.
   - The English/colonial origins carry Gen 0 and thread through.
3. **No villains, no sugar-coating — both directions**: the Afrikaner strand is explained, never excused (Broederbond capture, whites-only Craven Week, the lockouts all stay). The resistance strand is honoured, never sainted (1959 split began as Loriston–Abass power struggle; SACOS discipline destroyed its own players' careers; post-unity bitterness and Chester Williams's account stay).
4. **Convergence**: Gen 5 (1992 one board, 1995 one jersey) is the hinge — told from BOTH perspectives (what the same day at Ellis Park meant to each side). Gens 6–7 are then written as one stream; Kolisi 2019/2023 is the evidence the braid held, not a second convergence.
5. **Facts are the main focus**: every claim traceable to this notes file with a named source; contested items hedged openly in-line (house style); no fabricated attributions ("the historians say" is banned unless a named historian said it).

## GEN 1 BRIEF (1890–1948) — no-wiki; local-source mining + salvaged agent fetches (July 2026)

### FACTS — settled

**1891 British tour — funding SETTLED: Rhodes alone, via Hofmeyr**
- Lions official site: "The touring party was invited to South Africa by the Western Province union and with all costs underwritten by the Cape Colony prime minister, Cecil Rhodes." Kruger appears nowhere. (lionsrugby.com year-by-year 1888–1899.)
- Winch thesis (pp. ~107–109): the fixer was **Jan Hendrik "Onze Jan" Hofmeyr** (Afrikaner Bond leader), "a devoted follower of the winter game… rarely an important match at Newlands of which he was not a spectator," who "wished to build on increasing Afrikaner enthusiasm for the game" (Stellenbosch crowds 2000+). "His involvement made it a relatively straight-forward task to convince Rhodes to underwrite the tour."
- Billy Simkins: "when they cabled home 'Rhodes, Premier, guarantees expenses' the team came out" (Cape Times, 10 Sept 1891, via Winch).
- RFU's Rowland Hill was obstructive, esp. re Transvaal leg: "Many varsity men in the England team find it impossible to extend their absence…" — players on arrival "unanimously expressed the desire… to admit of a visit to the Transvaal."
- **Match count RESOLVED: 19 official matches, all won, ONE POINT (a try, then worth 1) conceded — in the first match vs Cape Town Clubs** (Difford p. 477 via Winch; World Rugby Museum concurs: 19 matches, 89 tries scored, 1 conceded). Lions site says "20 matches" — the 20th is evidently the **unofficial Stellenbosch fixture**, won only 2–0, M. Daneel tackled just short (Difford via Winch). Use: 19 official + the unofficial Stellenbosch near-upset as story.
- Tourists' only defeat on tour: at CRICKET, Matjesfontein (Winch).
- Milton was on the reception committee and acting private secretary to Rhodes simultaneously (Winch).

**Green jersey — sourced to Greyvenstein, *Springbok Saga* + SARU Board minutes (via Prof Piet van der Schyff; Dan Retief substack)**
- Heatlie a Bishops alumnus. "According to legend, it was Heatlie's wife who decided that the club's [Old Diocesans] jerseys would be dyed myrtle green – perhaps for no other reason that the dye was freely available." → frame as legend; dye "freely available," NOT "cheap."
- 1896: Heatlie "arranged for 'his' South African team to play in the green jerseys he supplied," Newlands, **5 Sept 1896, SA 5–0 British Isles** (SA's first Test win).
- **1903, 12 Sept, third Test, Newlands (SA 8–0, series won)**: Old Diocesans had ceased to exist but outfitters had stock; green jerseys, black shorts, and **Villagers' scarlet socks** (none else available, Heatlie got his club's consent). Green confirmed as national colour thereafter (1906 tour).

**1919 NZ Army team — CORRECTED again**
- Te Ara (govt encyclopedia): NZ Inter-services team won the 1919 King's Cup, invited to tour SA. "The South Africans requested that no 'coloured' players be included, so **Parekura Tureia** of Ngāti Porou and **Nathaniel 'Ranji' Wilson**, a New Zealander with West Indian heritage, **were removed from the team**." → BOTH removed (drop the Tepene claim — not in Te Ara/NZHistory).
- Tureia later captained NZ Maoris vs the Springboks at Napier (1921), "a prospect that didn't please some of the visiting Springboks" (Te Ara).

**1928 and the exclusion series**
- NZHistory: Māori always eligible for the All Blacks, but NZRFU "chose not to select them" for SA tours — **1928, 1949, 1960**; 1928 meant "leaving behind players like the legendary George Nēpia." No identifiably Māori player toured SA until **1970**, then as "honorary whites."
- The first official NZ Māori northern-hemisphere tour (1926, W30 D2 of 40) was organised AFTER Māori were declared ineligible for the 1928 SA tour (NZHistory).
- 1960: ~160,000-signature petition, "No Maoris − No Tour" (NZHistory) — Gen 2/3 material.

**Black rugby institutions (Financial Mail, 26 Oct 2023 — Odendaal/Snyders)**
- SACRFB founded **1897** (Snyders: Savona Café, Kimberley, 19 Aug 1897 — see Gen 0 brief); "formed just 8 years after the whites-only counterpart; preceded ANC formation by 15 years."
- SACRFB constitution: no discrimination by "colour, nationality, language or religion" (Odendaal).
- **Rhodes Cup: initiated 1897 Kimberley; first tournament 20 Aug 1898; "more valuable than the Currie Cup" [as an object]; discontinued 1980 by WP Country Districts (last winners), reason "rejection of the political legacy of Rhodes as an imperialist."**
- **South African Bantu Rugby Board founded 1935**, "response to JBM Hertzog's divide-and-conquer politics."
- Mine owners promoted sport among Black workers as "social control" (Odendaal).
- Quotes banked for later gens: Hannes Marais (1971): "The coloured population does not seem very interested in sport." Dawie de Villiers (1980): "Blacks have only known Western sports for the last 10 years."

**The Afrikaner arc, 1902–1948 — Dean Allen, IJHS (local full text, allen.txt)**
- Camps: Allen p./fn.34: "Tragically, **20,000 of the 26,000 Boers who did die in the concentration camps were less than 16 years old**" (citing Le May; Harrison). 26,000 figure confirmed.
- "The game of rugby had been **appropriated by the Volk** as a means of expression; to fulfil a physical as well as an ideological need to press for autonomy from British rule. The great irony of course, lies in the fact that they chose to adopt a most 'imperial game' in order to achieve this." — Allen.
- 1920s: game reached urbanising young Afrikaners via Stellenbosch-trained administrators; diffusion to the working class "not dissimilar" to the UK.
- 1921 first tour to Australasia; Sydney critic G.V. Portus: the Dutch South Africans "seem to outshine the English South Africans."
- **PERIODIZATION (fairness-critical): "Throughout this period though, rugby was yet to be invested with a narrow nationalistic Afrikaner ethos."** The ideological capture came in the 1930s–40s: Malan's Purified NP + DRC + Broederbond "began… to ideologise Afrikaner identity"; Blood River + wars + camps woven into a "sacred history"/civil religion (Dunbar Moodie); 1938 Great Trek centenary made it mass emotion; 1939 WWII entry the decisive political break; 1948 Malan PM at 74.
- Allen quotes (via line 773): "Springbok rugby carried a thinly disguised anti-imperialist message" — check attribution in allen.txt before use (likely Grundlingh).
- Allen, "Captain Diplomacy" (CPUT abstract, paywalled full text): 1906 tour "only four years after the end of the Anglo-Boer War and was used as an opportunity to unify the divided nation"; Roos "an Afrikaans schoolteacher" of "iconic status… within South African rugby folklore."

### PENDING (Haiku retrieval agent running)
Currie Cup origin (1891 cup → Griqualand West); Springbok name 1906 (Roos/Carden/Daily Mail); 1937 tour details + "best team ever to leave New Zealand" + Roos "skrum" telegram traceability; 1903 series (Heatlie, Newlands 8–0); 1921 series + Napier NZ Maoris match cable scandal.

### GEN 1 — Haiku retrieval results (adjudicated)
- **Currie Cup**: Sir Donald Currie (Union-Castle Lines) gave the gold trophy to the 1891 tourists, "for the local team that produced the best performance against the Lions"; presented after Lions beat Griqualand West 3–0, 20 July 1891, Kimberley; GW handed it on → annual provincial competition; first official Currie Cup 1892, Western Province first winners. (lionsrugby.com "On this day"; ougrote.com.)
- **Springbok name**: manager J.C. "Daddy" Carden's own recollection: "That evening, I spoke to Roos and Carolin and pointed out that the witty London Press would invent some funny name for us, if we did not invent one ourselves. We thereupon agreed to call ourselves 'Springboks'." First print: **Daily Mail, 20 Sept 1906** ("a springbok, a small African antelope" on the jersey). Anglicised from "Springbokken". (rugby365 "How the Springboks got their name".)
- **1937**: Test 1 Wellington 14 Aug L 7–13; Test 2 Christchurch 4 Sep W 13–6; Test 3 Auckland 25 Sep W 17–6 (bokhist.com TourID=20). **"Best team ever to leave New Zealand" is modern editorial framing (ESPN headline), NOT a traceable 1937 quote** — contemporary praise was real but varied (NZ Truth: "on the day they would have beaten any other team in the world"). **Roos telegram confirmed** (ESPN): cable before the third Test, "scrum, scrum, scrum" — sent to **Philip Nel** (the CAPTAIN, a lock — Haiku said scrum-half, wrong; do not state position as scrum-half). Do NOT call the side "the Invincibles" (that's the 1924 All Blacks tag; unverified for 1937). 1937 remains SA's only Test-series win in NZ.
- **1903**: SA's first series win; 3rd Test Newlands 12 Sep 1903, 8–0, Heatlie captain (tries Barry, Reid; Heatlie conversion — via rugby-talk, weak; 8–0 multiply confirmed). Tour overall: British won 11, lost 8, drew 3 (rugbyfootballhistory — hobbyist, flag).
- **1921**: Dunedin 13 Aug NZ 13–5; Auckland 27 Aug SA 9–5; Wellington 17 Sep 0–0 — first SA–NZ series, drawn. **Napier, McLean Park, 7 Sep 1921: SA 9–8 NZ Maori.** Blackett cable VERBATIM (Te Ara, NZ govt): "Most unfortunate match ever played … Bad enough having play team officially designated New Zealand natives but spectacle thousands Europeans frantically cheering on band of coloured men to defeat members of own race was too much for Springboks who frankly disgusted." Journalist **Charles Blackett** (middle initials vary in sources); **leaked by a post office employee to Napier's Daily Telegraph** (NZHistory); Springbok manager Harold Bennett denied involvement.

## GEN 2 BRIEF (1948–1969) — no-wiki; salvaged Opus agent + local Rademeyer/Potgieter mining (July 2026)

### THE NAMED-HISTORIAN REPLACEMENTS (for the fabricated "the historians say" claims)
- **Grundlingh, *Potent Pastimes*** (via Potgieter thesis, Grundlingh-supervised, pp. 21–22): "support for the Springboks was on the same continuum as membership of the National Party" (Potent Pastimes p. 64). Rugby "reinforced values like respect for perceived tradition, rules and authority, integral to the nationalist movement, and at the same time encouraged certain cultural conformity."
- **Nauright & Black, *Rugby and the South African Nation*** p. 61 (via Potgieter): Springbok successes "came to symbolise both the actual and potential achievements of the Afrikaner people." ← the REAL, citable version of SAHO's uncited "civilization" line.
- Potgieter: "it is ignored that a 15-man rugby team beat another 15-man rugby team, but instead one nation has beaten another nation."
- Boycott-era note (Potgieter): the government's sports concessions were largely "born out of a desire to keep the country's rugby going" — rugby the reason SA sport got ANY concessions.

### CRAVEN — the contested quote
- **"There will be a black Springbok over my dead body": ALLEGED, DENIED, UNLOCATABLE.** The Roar (Australian sports site): Craven "allegedly stated" it; "Craven denied the allegation and it is difficult to locate where the statement was made or when and to whom it was made." → Use only as an allegation he denied; never as a stated fact. (It is everywhere in secondary literature; nobody dates it.)
- Broederbond: "Virtually everyone else involved in the higher echelons of South African rugby was a member of the Broederbond, including the referees for Test matches" — The Roar, evidently drawing on **Wilkins & Strydom, *The Super-Afrikaners*** (the standard Broederbond exposé, which Dean Allen also cites). Attribute to Wilkins & Strydom, not to "historians."
- Craven bio (verified earlier, unchanged): b. Lindley 1910; 16 Tests 1931–38; SARB president 1956–1993; IRB chair 1962/1973/1979; three doctorates (1935 ethnology, 1973 psychology, 1978 phys ed); coach 1949–56, 17/23 = 74%; died 4 Jan 1993.

### RADEMEYER (ufs.txt, *Entrenching apartheid in South African sport, 1948–1980*, JCH 39(2) 2014) — the legal/policy spine
- **1948–1956: "not much was done to develop a formal sports policy"** — the NP's first years had NO formal sports policy; the codification came under **Strijdom** (blueprint), then Verwoerd, then Vorster. (Fairness-critical periodization.)
- 1956 declaration: no mixed teams to tour SA; reconfirmed early 1960s.
- **State vs Brandsma and others, Oct 1962**: whites, coloureds and Indians prosecuted over a mixed FOOTBALL match (Durban Indian team vs mixed Pietermaritzburg team) under the Group Areas Act (Act 77 of 1957) + Liquor Act; magistrate's judgment opened a loophole.
- **Papwa Sewgolum**: on the back of that judgment, the Indian golfer entered the 1963 Natal Open and "defeated 113 white golfers to be crowned the provincial champion" — a policy embarrassment. (Later banned; prize-giving-in-the-rain episode is famous but NOT in this paper — do not use without a source.)
- **SASA 1958** (non-racial sports association); **SANROC 1962 per Rademeyer** ("established in 1962 to confront white sporting organisations") vs 1963 in other notes — CONTESTED, Haiku checking. Brutus not a communist (NYT 29 Jan 1962, Rademeyer fn.).
- **1934 Empire Games**: awarded to SA, then RECALLED to London because non-white athletes from other colonies "were not welcome in South Africa."
- **1960 All Blacks tour**: petition **153,000 signatures per Rademeyer** (NZHistory says "nearly 160,000" — write "over 150,000"); PM Nash let the tour proceed without Māori; "Citizen's All Black Tour Association"; "No Maoris, No Tour".
- **VERWOERD'S LOSKOPDAM SPEECH — 4 September 1965**, to the National Youth League of the Transvaal at Loskop Dam, **"the same day that the Springboks achieved an unexpected test win over the All Blacks in Christchurch"** (Rademeyer). Verwoerd (translated): "Our position has not changed. As we behave in other countries, we expect that they will behave here based on our customs — and I want to add: and everyone knows what it is." Context: it was a public REBUKE OF CRAVEN, whose NZ press interview had been "interpreted by the press as tacit approval of Maoris coming to South Africa" with the 1967 All Blacks. The speech "sank the tour" and was "the spark that led to the unraveling of the very strong traditional rugby ties with New Zealand." Contemporary jibe: the speech had "the timing and co-ordination of a camel with four left feet."
- **Vorster's "new" sports policy**: outlined in Parliament **11 April 1967** (Hansard col. 4108); hardliners (Jaap Marais, 2 Oct 1969 speech) fought it — the HNP split context.
- **D'OLIVEIRA 1967–68** (Rademeyer §10, citing Odendaal *Cricket in Isolation*, Murray JSAS 27(4) 2001, D'Oliveira's own book, Hain): 1967 SA declares D'Oliveira (SA-born Coloured cricketer, emigrated 1960) unwelcome with MCC; MCC omit him → "elation" in SA + fierce English criticism + **19 MCC members resign**; Tom Cartwright withdraws with an "injury" (Rademeyer's scare quotes); D'Oliveira called up; **Vorster calls the MCC side "a team of the anti-apartheid movement SANROC"**; Cheetham & Coy fly to London; D'Oliveira "would not be welcome"; tour cancelled. Odendaal: no event in SA cricket history compares "in terms of the intensity of bitterness."

### VAN JAARSVELDT — CORRECTED (he was RHODESIAN)
- springboks.rugby tribute (21 July 2025) + KZN Rugby: b. **1929 Bulawayo, Rhodesia**; Currie Cup debut at 18; **62 appearances for Rhodesia** (wing, then loose forward), 1947–62; **the only Rhodesian ever to captain the Springboks**; captained SA v Scotland at **Port Elizabeth, 30 April 1960, won 18–10, scored a try**; selected as captain never having played a Test; **first cap = last cap**.
- Why never again: not fluent in Afrikaans, gave team talks in English; **declined to deliver the customary captain's prayer**; "his status as a Rhodesian English-speaker in a rugby environment dominated by Afrikaner culture unsettled many"; "easy to believe his limited appearances had more to do with politics than performance."
- Later: coached Rhodesia 1967–70; president of Rhodesian RU through the Zimbabwe transition; handprint at SA Rugby Museum 2013; **died 21 July 2025, aged 96, the oldest living Springbok** (one year almost to the day before the book's July 2026 snapshot).
- Related scholarship: Winch & Parry, "Rhodesia, Rugby and the Afrikaner: 'Working Together to Send this Country Ahead'", IJHS 33(15) 2017 (paywalled; academia.edu copy exists): Southern Rhodesia limited Afrikaner immigration while rugby bound the communities; Afrikaans players strengthened Rhodesian teams via tobacco/copper migration.

### Sports facts (verified earlier pass, unchanged): 1949 SA 4–0 NZ; 1951–52 Grand Slam tour 31 matches/30 wins (London Counties the sole defeat); Scotland 0–44 Murrayfield (try = 3 pts then); 1955 Lions 2–2 (Haiku verifying details); 1956 NZ first-ever series win over SA; 1958 FRANCE take the series (drawn 3–3 Newlands 26 July; France 9–5 Ellis Park 16 Aug; Mias) — ends the 1896–1958 62-year home record; 1960 SA 2–1 NZ (with draw); 1960–61 fourth Grand Slam; Sharpeville 69 dead + Macmillan "Wind of Change" Feb 1960 (Macmillan BEFORE Sharpeville, keep order); Craven Week founded July 1964 East London, 15 teams, WHITES ONLY (open to all races only in 1980).

### PENDING (Haiku): 1955 Lions details/crowd; 1965 season (Scotland/Ireland/Australia losses + Christchurch 19–16 on 4 Sept); SANROC 1962 vs 1963; 1967 tour cancellation mechanics; 1970 honorary-whites names + 3–1; 1949 Māori exclusion + Geffin.

### GEN 2 — Haiku retrieval results (adjudicated)
- **1955 Lions**: series drawn 2–2 (first tied Lions series). First Test **Ellis Park, 6 Aug 1955, Lions 23–22**; "more than 95,000… a then world record for a rugby union international"; "as many as 100,000 – with a certain Nelson Mandela in the crowd" (lionsrugby.com Classic Match; rugbyworld.com).
- **1965 annus horribilis**: Ireland's FIRST win over SA, Dublin **10 April 1965, 9–6**; Scotland 8–5 Murrayfield; Australia 2–0 (18–11 Sydney, 12–8 Brisbane); NZ series lost 1–3. **Third Test Christchurch 4 Sept 1965, SA 19–16 (bokhist) — CONFIRMED same day as Loskopdam.**
- **SANROC: 1962** best-attested (SAHO Brutus bio + African Activist Archive, MSU); Brutus a founder and president. Use 1962.
- **1967 tour cancellation**: PM **Keith Holyoake, 3 Feb 1966**: "In this country we are one people; as such we cannot as a nation be truly represented in any sphere by a group chosen on racial lines." NZRFU formally declined **25 Feb 1966** — "could not under the terms of the invitation see its way clear to send an All Black side in 1967" (e-tangata; nzhistory).
- **1970 tour**: Sid Going, Blair Furlong, Henare "Buff" Milner (+ Bryan Williams, Samoan heritage) as "honorary whites"; SA won 3–1. (rugby-talk — hobbyist, facts well-attested; RNZ on Williams.) → Gen 3/4 use.
- **1949**: SA 4–0. NZRFU's own words: **"In view of the domestic policy of South Africa, the players cannot be other than wholly European."** (e-tangata.) First Test Newlands 15–11: **Okey Geffin kicked a record five penalties**; series total 32 of SA's 47 points (NZ Herald; IOL).

## GEN 3 BRIEF (1959–1979, the non-racial game's generation) — no-wiki; salvaged Opus agent + local mining (July 2026)

### ATTRIBUTION CATCHES (chapter-critical)
- **"No normal sport in an abnormal society" is SACOS's slogan** — Rademeyer fn.1: "A slogan used by the South African Council on Sport (SACOS) in its struggle against apartheid in South African sport." NOT a Loriston line. (Hassan Howa is its most associated voice as SACOS president; JSTOR Daily confirms a related Howa quote per agent progress note.)
- **"Rugby had long since become a second religion" [to the Afrikaner] is Rademeyer's OWN scholarly line** (sacos_jch.txt line 619) — attribute to the historian, not to Norman Middleton or any activist.
- Fredericks's vivid lines on Eric "Bucs" Damons (d. 12 May 2021, Kimberley) — "The AR Abass Stadium in Kimberley stands like a silent tumor that grows with every death of the heroes that once gave it purpose" and the "lifts the burden from his shoulders of having to adorn the cloak of those who denied him" — are **Mark Fredericks's own authorial reflections** (africasacountry, July 2021), NOT eulogy quotes. Attribute to Fredericks.

### SACOS — settled
- Founded **17 March 1973, Himalaya Hotel, Durban**; convened by the ad hoc Committee of National Non-Racial Sports Organisations; **nine federations "from oppressed communities"**; first president **Norman Middleton** (The Conversation "SACOS at 50", 2023; nrshp.co.za brief history; Merrett at fromthethornveld).
- Mission (1973, verbatim): "To strive for non-racial sports structures from school level upwards and to generate opposition to and to expose discrimination in sport, in sport sponsorship and facilities in South Africa." (nrshp)
- **Double Standards Resolution adopted 1977** (nrshp): no member could belong to/participate in multinational or race-based structures. 1978 charter: "single non-racial federations, the outlawing of racially exclusive clubs, and the integration of all school and youth sport" (Merrett).
- Government called SACOS officials **"sports terrorists"** (Merrett); state saw it as "an unholy rebel organisation trying to undermine South Africa in the international sports arena" (Rademeyer, quoting source). **Hassan Howa consistently denied a passport** (Rademeyer).
- Recognition by the **Supreme Council for Sport in Africa, December 1976** — "South Africa's international sports relations were now hostage to SACOS influence exercised through the SCSA."
- Peak: 28 national federations, 1M+ grassroots members (nrshp). Ends CONTESTED: decline 1989–95, last formal meeting 1997, never officially dissolved (nrshp) vs "disbanded 2005" (Conversation) — Gen 5 material.
- Merrett's betrayal thesis (Gen 5 material): 1990s unity "a takeover by the old apartheid federations with a few faces of colour on boards."

### RHODES CUP / SOUTH AFRICA CUP — settled (Snyders, National Museum, 3 July 2020)
- 28 inter-provincial tournaments 1898–1980, biennial, in Kimberley; WP first winner, **WP Country Districts the last**.
- Discontinued **1969**, one-year reinstatement, ended for good after **1980**; reason (verbatim): "a rejection of the political legacy of Rhodes as an imperialist and his company's exploitation of black workers in the mining sector."
- **South Africa Cup**: first tournament 26 June – 3 July **1971**, final at **Athlone Stadium, Cape Town: WP 19–6 EP**; 21 finals 1971–91; WP won 7.

### THE 1977 AMALGAMATION (twosidestoeverything blog — hobbyist, FLAG; Potgieter thesis dates agreement 1977, completion 1978)
- **November 1977**: SARFF (Coloured, Loriston) + SARA (African — the renamed Bantu board) + SARB (white) amalgamate into a nominally non-racial SARB with IRB affiliation. **SARU under Dullah Abass refused**, staying under SACOS: "no normal sport in an abnormal society."
- 1977: all SARB grounds opened to all races; first players of colour in national trials; **Errol Tobias & Turkey Shields in the SA Country XV; Hennie Shields in the Gazelles; Timothy Nkonki & Hennie Shields to Argentina for CASI's centenary** (cross-link to the Argentina chapter!); Nkonki in a festival match in France alongside Morne du Plessis.
- Randy Marinus played against the 1976 All Blacks aged 19, later went to SACOS-affiliated SARU.

### MONTREAL 1976 — settled (Nicolas Bancel, The Conversation, 13 June 2024)
- **22 African countries boycotted**; Côte d'Ivoire and Senegal (French allies) did not. Decision by OAU between 24 June–3 July; many delegations already in Montreal; "just two days" before the 15 July opening.
- Trigger: New Zealand letting the All Blacks tour SA; backdrop: **Soweto, 16 June 1976** (Bancel: police violence killed "approximately 600" — casualty figures CONTESTED, official counts far lower; Haiku fetching range).
- IOC's position: "rugby was not an Olympic sport and that New Zealand's sporting policy was outside its purview."
- Old chapter's "29 nations... Guyana and Iraq" — some counts run higher by including later withdrawals/non-African allies; Bancel's 22-African is the named-scholar figure. Write hedged.

### THE NP SPLITS OVER RUGBY (Rademeyer §9, citing du Pisani + Grundlingh *Potent Pastimes* pp. 93–94)
- **Vorster's new sports policy, April 1967**: Olympic team single & multi-racial on merit (no mixed trials); Canada Cup golf allowed; Davis Cup mixed opponents allowed; **rugby: "Any Maori player would be allowed in South Africa as part of an All Blacks touring squad, provided it is not politically exploited… A mixed Springbok team was still unacceptable"**; same for cricket.
- Right-wing revolt: Jaap Marais "Racial mixing in sport" speech, Oct 1969; **Transvaal NP congress Sept 1969**: of 1,000+ delegates, only **Albert Hertzog + 17** refused the sports motion; ultimatum; **Hertzog, Marais, Stofberg suspended → Reconstituted National Party (HNP) founded, Hertzog first leader**. "The admission or exclusion of Maori players in the 1970 All Black team to South Africa became a central point in this dispute."
- → THE governing party of apartheid split, and rugby was a central fault line. (Use prominently.)

### PENDING (Haiku): 1959 walkout second source; AR Abass full name/dates + stadium; 1966 SARU rename; Stop The Seventy Tour details; 1974 Lions (3–0 + draw, "99"); 1976 ABs tour dates/result + Soweto casualty range.

### GEN 3 — Haiku retrieval results (adjudicated)
- **1959 split**: "14 unions, representing more than 10,000 players, broke away from the South African Coloured Rugby Board in 1959 to form the South African Rugby Federation" (News24 Paarl Post tribute — still the primary source, FLAG); cause: "bitter power struggle between the Board's general secretary Abdullah Abbas and Cuthbert Loriston, who became president of the new body." **Loriston's stated vision: to play "normal sport in an abnormal society"** — the EXACT INVERSE of the SACOS slogan; the split in two phrases. (Quote traces to the News24 tribute, third-person — hedge as "the phrase attached to him".) One source variant "Charles Loriston" — use Cuthbert.
- **AR ABASS**: **Abdul Razzaq Abass**, born Kimberley **10 December 1922**; SARU secretary early 1960s; **president 1966–1983**; Kimberley stadium renamed **AR Abass Stadium on 6 September 1986** (DFA March 2026 series). Death date not found.
- **1966 rename confirmed**: SACRFB → **South African Rugby Union (SARU)**, dropping "Coloured" (ESPN/Firdose Moonda); Abass president from the same year.
- **Stop The Seventy Tour (1969–70)**: Peter Hain, **nineteen years old**, chairman; "demonstrations and direct action were organized at every match" (Global Nonviolent Action Database, Swarthmore); tactics: tacks on the pitch, the Springbok team bus hijacked, grounds ringed with barbed wire; Dublin: 10,000 marched to Lansdowne Road; **consequence: the 1970 South African cricket tour of England cancelled**.
- **1974 Lions**: unbeaten 22-match tour ("The Invincibles"), won first three Tests, fourth drawn **13–13**; mid-May–late July; the **"99" call** = simultaneous retaliation, McBride: "One in, all in"; logic: referee can't send everyone off (lionsrugby.com; rugbydump for the 99 detail — flag).
- **1976 All Blacks tour**: **30 June – 18 September 1976**, began "a fortnight after the Soweto uprising during which South African security forces had killed at least 176 pupils" (Te Ara); **Ian Kirkpatrick tear-gassed in Cape Town, Sept 1976** (Te Ara photo caption); SA won **3–1**.
- **Soweto casualties**: official 10-day count 174 Black + 2 white dead (SAHO); "usually given as 176, with estimates of up to 700" (SABC TRC/SAHA); 600+ countrywide by end of 1976. Write: "at least 176, with estimates running to several hundred."

## GEN 4 BRIEF (1980–1989) — no-wiki; Potgieter thesis ("Barbed-Wire Boks", Stellenbosch MA 2017, supervisor Grundlingh) + salvaged agent (July 2026)

### THE 1981 TOUR — thesis-sourced set pieces (all with primary citations: Die Burger, SARB Archive, player memoirs, interviews)
**Gisborne (opener)**: Māori community gave the Springboks an official welcome at the local marae — but Māori Council president **Graham Latimer** told them: "we [the Maori Council] will not make another such welcome unless your government changes its apartheid policy." Crowd ~20,000 (more than Gisborne's population); 300+ police. Die Burger reported pamphlets teaching petrol bombs/glass-spreading ("Duiwelse plan teen Bokke," 17 July 1981).
**Hamilton, 25 July 1981 (Springboks v Waikato — CANCELLED)**: first-ever LIVE rugby broadcast to South African TV — protestors knew and targeted it. Waikato held the Ranfurly Shield, ten All Blacks, had beaten the Boks in 1956. 27,000 in the ground; barbed wire + farmers' trucks as barricades; police in tracksuits and rugby boots; riot gear thought "a bit too confrontational for New Zealand society." HART's "Operation Everest": ~400 protesters tore down fences, locked arms mid-field; police ordered NOT to use batons (world broadcast); mass one-by-one arrests; crowd "baying for blood," spectators leaping barriers. Match called off (NZHistory via Wayback: ~500 police; Pat McQuarrie's stolen plane threat; **Mandela in prison: hearing it, said it was as if "the sun had come out"** — NZHistory). Dobson: "the vehemence of the opposition shocked many South Africans who believed that rugby men really wanted to play with them."
**Molesworth Street, Wellington, 29 July 1981**: ~2,000 marched on parliament (also home of the SA consulate); regular police away in New Plymouth; trainee/rookie police with short clubbing batons beat the front of the crowd — "many of whom were schoolchildren still in their uniforms" (thesis, citing Meurant *The Red Squad Story*). First police-protester violence of the tour; after it, protesters strapped on pillows and helmets, police donned riot gear.
**Eden Park, 12 September 1981 (3rd Test, the "flour-bomb test")**: **two-thirds of the NZ police force deployed in Auckland** (NOT "40%" — kill that number); ~2,000 protesters, "a riot, rather than a protest"; ~200 arrested, ~45 injured (Die Burger 14 Sept; earlier note's "201 arrests, 90+ injured" — prefer thesis figures, hedge "about"). Cessna low swoops: pamphlets, burning flares, flour parcels; Claassen quote (More Than Just Rugby p.186) on backs watching the plane; **Gary Knight (prop) struck by a flour bomb**; Welsh referee **Clive Norling** called Claassen & Andy Dalton together and suggested calling it off; 22–22 deep in injury time → controversial Norling penalty → **Allan Hewson** kicks it, **NZ 25–22**, series 2–1 NZ. Springboks most aggrieved by the refereeing, not the plane. Stofberg: "you accepted that this was your lot, and then got on with why you had come." The team gave the traditional mounted springbok head to the **New Zealand police**. Rob Louw: the strangest test ever played (For the Love of Rugby).
**Glenville, USA (secret Test v Eagles, 25 Sept 1981)**: decoy squad sent to baseball museum; Test players in match kit under civilian clothes, minibuses lying flat, via Tom Selfridge's house to **Owl Creek polo field, Glenville NY**; 250 State Troopers mostly hidden in bushes; warm-up in horse paddocks; polo field with a **two-metre drop end to end**; goalposts still being erected as teams arrived; **crowd of 35** — "most of whom were substitutes, State Troopers, or friends of the field's owner" — smallest crowd ever at an official Springbok Test (thesis citing Die Burger 28 Sept 1981; earlier note said 29 — prefer 35, or "a few dozen"). 6–4 at half (uphill, into wind); 38–7 final.

### TOBIAS — thesis + Pure Gold (his 2016 memoir)
- "South Africa's first black Springbok" (technically coloured), **a builder from Caledon**; presence "dismissed as political window dressing" by critics; NZ journalists asked whether it was more important for him to wear the jersey or have the vote; cited by management re Pass Laws — which didn't even apply to him ("he was coloured not black"); "a somewhat torrid time on the tour"; **he asked to go home; Craven convinced him to stay** (Pure Gold p. 86).
- 1984: Tobias + **Avril Williams** the only players of colour v England.
- Verified earlier: b. 18 March 1950; 6 caps 1981–84; debut 30 May 1981 v Ireland, Newlands, at OUTSIDE CENTRE (fly-half later).

### ISOLATION MECHANICS
- **RUGBY NEVER EXPELLED SA** (established last pass): IAAF expelled 1976, Olympic movement expelled; the IRB never did — SA kept its seat throughout; isolation imposed from outside rugby (governments, Gleneagles, SACOS veto). Craven chaired the IRB 1962/1973/1979.
- Thesis: "For most of the 1980s, South African rugby was stuck in a rut… player and spectator numbers were diminishing"; by 1987 Craven abandoned "the ineffectual old road (involving propagandist organisations, media congresses, rebel tours, and rugby marketers)".
- 1984 England toured, lost both Tests; then 1985–91 no Tests v established nations except rebel tours; missed RWC 1987 & 1991.

### HARARE & AFTER — thesis, from the SARB ARCHIVE (primary)
- **Harare, 16 October 1988** (joint-statement date): two-day SARB + SARU + ANC meeting. Joint statement verbatim: "The meeting came about because of the common desire on the part of all the participating organisations to ensure that rugby in South Africa is organised according to non-racial principles… agreed that South African rugby should come under one non-racial controlling body."
- Backlash: SARB's own Fritz Eloff (deputy president), Steve Strydom, Ronnie Bauser condemned it; government threatened to seize Craven's and Luyt's passports; **P.W. Botha labelled Craven a traitor — "something which hurt Craven to the end of his days, but seemed to spur him on"**; SAP rugby club furious; Afrikaans press hostile, English press in favour. Die Burger: "Craven kies ANC bo Noltes, Malan" (12 Sept 1988 — NB pre-Harare, re the earlier contacts).
- **1989 World XV via Grundlingh (Potent Pastimes p. 108)**: the centenary exhibition "was largely due to the somewhat more positive mood internationally toward the SARB following the talks with the ANC."
- Craven's ultimatum: those unwilling to abandon racism in rugby should leave; SARB amended constitution; unification "vigorously pursued".
- **Craven's limits (both-sides, thesis)**: "As late as 1990, Craven remained adamant that the government should never give everyone equal vote." His opposition to apartheid "was rooted in the fact that, above all else, it was crippling South African rugby." He did not grasp abolition as universal franchise. Craven & Luyt "had not gone to Harare to negotiate a new settlement for the country, but to negotiate a way through which South African rugby stood a chance of returning to the international domain."
- (Gen 5 material, banked): 1990 De Klerk unbans ANC; talks resume — **Luyt (SARB) v Ebrahim Patel (SARU), chaired by Steve Tshwete**; agreement in "barely a day"; 50/50 merger → **SARFU** ("started functioning in 1991" per thesis — most sources say formally launched March 1992, CONTESTED, hedge); Craven first president to 1993, then Patel; Nauright: black administrators became "ceremonial figureheads"; 1992 All Blacks first back, then first Wallabies Test in 21 years.

### PENDING (Haiku): 1980 Lions 3–1; Tobias Test-by-Test; 1985 tour court case (Finnigan/Recordon); 1986 Cavaliers; 1989 World XV details (matches/IRB sanction/SAB funding/NZ absence/Tutu "obscene"); 1988 meetings sequence (Luyt London Feb, Cape Sun 7 May, Harare delegation: Nzo/Mbeki).

### GEN 4 — Haiku retrieval results (adjudicated)
- **1980 Lions**: SA won 3–1 (26–22 Newlands 31 May; 26–19 Bloemfontein; 12–10 PE; Lions 17–13 Loftus). Beaumont captain. Naas Botha's boot decisive — press dubbed him "Nasty Booter"; career 312 pts/28 Tests, 23 drop goals (World Rugby HOF).
- **Tobias Tests (bokhist player page)**: 6 caps — 30/5/81 Ireland (W 23–15), 6/6/81 Ireland Durban (W 12–10), 2/6/84 England PE (W 33–15), 9/6/84 England Ellis Park (W 35–9), 20/10/84 & 27/10/84 S. America (W 32–15, 22–13). 1981 NZ tour: MIDWEEK GAMES ONLY, no Tests. 1984 v England: fly-half. **Debut position CONTESTED: Irish Times says inside-centre; earlier pass said outside centre; write "at centre" (midfield alongside Danie Gerber)**. Avril Williams (b. 10 Feb 1961, Paarl): 2 caps, both v England 1984 — first time two Black players in a Springbok team.
- **1985 tour cancellation**: Finnigan v NZRFU — lawyers **Patrick Finnigan & Philip Recordon**, members of Auckland-affiliated clubs; grounds: NZRFU constitution's promise to "promote, foster and develop the game"; High Court (CJ Davison) sided with union 6 June 1985; Court of Appeal (Cooke + 4) overturned; **interim injunction 13 July 1985 (Justice Casey)**; NZRFU cancelled within days. (Stuff; NZ Herald on Recordon.)
- **1986 Cavaliers**: all the leading All Blacks **except David Kirk and John Kirwan**; captain Andy Dalton — **jaw broken by a punch in the second match v Northern Transvaal**, Jock Hobbs took over; SA won series 3–1 (Cavaliers' one win 9–8 Durban); "completely without the sanction of the New Zealand rugby authorities"; players faced de facto international bans. (World Rugby Museum; ESPN; Scotsman.)
- **1989 World XV**: TWO matches, **26 Aug & 2 Sept 1989** (scores not retrieved — YouTube full matches exist); **IRB-sanctioned**; squad: **10 Welsh, 8 French, 6 Australians, 4 English, 1 Scot — every traditional nation bar New Zealand, which refused**. **Tutu (Irish Times): the IRFU's support "when black children were being beaten, tear-gassed and detained without trial" was "obscene."** **SAB-funding claim NOT CONFIRMED anywhere — DROP IT** (was wiki-derived). Grundlingh (Potent Pastimes p.108): the tour happened because of the improved mood after the ANC talks.
- **1988 sequence**: Luyt-in-London-Feb-1988 NOT confirmed — drop precision ("in 1988 Luyt, with Tommy Bedford and others, met the exiled ANC leadership"). **Cape Sun, Cape Town, 7 May 1988: SARB–SARU meeting confirmed.** **Harare 15–16 Oct 1988** (joint statement dated 16 Oct, SARB Archive): ANC — **Alfred Nzo (leader), Thabo Mbeki, Barbara Masekela, Steve Tshwete**; SARB — Craven, Luyt; SARU — **Ebrahim Patel, Ismail Jakoet**. (SAHO; LA84/Sporting Traditions.)

## GEN 5 BRIEF (1990–1995) — no-wiki; Rademeyer (sacos_jch) + Potgieter thesis (July 2026)

### Rademeyer (JCH, "No normal sport…1980–1992") — the unification spine
- **Garba's four conditions (1987)**: UNSCAA chairman Maj. Gen. Joseph Garba stipulated for readmission: "the abolition of the homelands, a unitary education system, equal access to public and private sports facilities for every citizen, and the end of economic apartheid" (citing London Times, 18 May 1987). UN Register/"black list" of boycott-breakers (from 1980) preceded it.
- **De Klerk's speech: 2 February 1990** — fell during the Gatting rebel cricket tour, which "was becoming increasingly irrelevant" in the torrent of change. Boycotts ended when the legislative foundations of apartheid were repealed mid-1991 (IOC lifted; UN black list ended).
- **SARFU formed MARCH 1992** — a FOUR-body merger: SARB + SARU + SA Rugby Football Federation + SA Rugby Association. (Thesis's "functioning in 1991" less precise — use March 1992.) 50/50 SARB-SARU basis negotiated by Luyt (SARB) & Ebrahim Patel (SARU), chaired by Steve Tshwete, agreed "in barely a day" (thesis). Craven first SARFU president until his death 4 Jan 1993; Patel succeeded (thesis says "stepped down in 1993, replaced by Patel" — verify succession detail).
- **Ellis Park 1992 (Rademeyer verbatim)**: "Louis Luyt's decision to play 'Die Stem' before the first rugby test after re-admission in 1992, while thousands of 'old' South African flags were waved by the sports-mad and predominantly Afrikaans-speaking crowd of more than 50 000 people at Ellis Park, nearly derailed the unifying process of South African rugby which was still in its infancy." → It was LUYT'S decision; crowd 50,000+; frame as institutional decision + crowd response, NOT "Afrikaners still saw it as..." characterology.
- Nauright (via thesis): post-unity, black administrators became "ceremonial figureheads alongside a core of old established officials"; merged township/white-club leagues had racial tensions on-field.

### PENDING (Haiku): ANC conditions for 15 Aug 1992 (Boipatong silence etc.) + what happened + scores (NZ 27–24; Aus next week); 1995 RWC run + final details + Pienaar quote + 747; Chester Williams (1995 role + 2002 Keohane biography allegations); "ranked ninth 1995" check (expect DELETE); NSC founding + Patel succession.

### GEN 5 — Haiku retrieval results (adjudicated)
- **15 Aug 1992, Ellis Park**: ANC's three conditions — no old flag, no Die Stem, a minute's silence for victims of political violence (Boipatong). What happened: crowd sang **Die Stem a cappella through the silence**; then **Luyt had it played over the PA** (converges with Rademeyer). NZ won **27–24** (first NZ Test in SA since 1976). ANC threatened to withdraw support for the Wallabies leg; relented after tense days; **Newlands 22 Aug: Australia 26–3** in a mudbath (3 tries to 0).
- **1995 RWC**: opener Thu **25 May, Newlands, SA 27–18 Australia**. Pieter Hendricks red-carded in the Battle of Boet Erasmus (v Canada brawl) → **Chester Williams returned** (had withdrawn on the eve with hamstring). QF Ellis Park: **Chester 4 tries v Samoa**. SF **17 June, Kings Park, SA 19–15 France** — kickoff delayed 1hr+, "the wettest game in the tournament's history"; Ruben Kruger try; Stransky/Lacroix kicking duel. **FINAL 24 June, Ellis Park, 15–12 aet**: Stransky ALL 15 (3 pens, 2 drops), winning drop deep in extra time after 12–12; Lomu contained (Joost's low tackle round the calves, 12th min, Andrews finishing); **SAA 747, Captain Laurie Kay** (+ Fourie, Coppard, Thomas), "Good Luck Bokke" on the underside, two passes over 63,000; **Mandela in Pienaar's No. 6 jersey and cap** — visited the changing room pre-match ("he turned around and my number was on his back" — Pienaar); pitch interview EXACT: **"We didn't do it for 60,000 South Africans, but for 43 million South Africans."**
- **"One team, one country" slogan: NOT FOUND in contemporary sources — omit.**
- **"Ranked ninth in the world" 1995: NOT FOUND; rankings began Oct 2003 — DELETE from chapter.**
- **Chester Williams**: only Black player in the '95 squad (third Black Springbok after Tobias and Avril Williams — his uncle). 2002 Keohane biography *Chester: A Biography of Courage*: shunned by white teammates, called "kaffir" by **James Small**; verbatim: "Winning the World Cup in 1995 may have unified the nation for a week. It did not change my standing within South African rugby. I was a black rugby player and that somehow separated me from the squad." **BUT: Williams later modified the accusations multiple times** — sometimes relocating the racism to the Currie Cup, sometimes denying, implying Keohane inflated it (Africa Is a Country, Sept 2019). Present WITH the instability.
- **NSC**: planning April 1988; came into being **1989**; launched **May 1990** as the ANC-aligned sports wing; SACOS's demise began 1988 with the split (SAHO "SACOS vs NSC"). **Patel: JOINT first president of SARFU with Craven from 1992** (World Rugby obituary); Craven died 4 Jan 1993.

## GEN 6 BRIEF (1995–2017) — no-wiki Haiku retrieval (adjudicated)
- **Professionalism**: IRB delegates met in Paris 24–26 Aug 1995, declared the game open **26 August 1995** (world.rugby). **Luyt & Sam Chisholm negotiated the SANZAR–News Corp deal — US$555M over 10 years — and Luyt announced it at a press conference TWO DAYS BEFORE the 1995 final** (Daily Maverick).
- **Mallett**: **17 consecutive Test wins Aug 1997–Dec 1998**, equalling the world record; **first Tri-Nations title 1998, 4–0** (14–13, 29–15 v Aus; 13–3, 24–23 v NZ) (ESPN; super.rugby).
- **Kamp Staaldraad (pre-RWC 2003)**: players stripped naked, pumping balls in a freezing lake, eggs broken on heads, crawling naked, starved; **naked in a pit singing the anthem while "God Save the Queen" and the haka blared**; slaughtered chickens they couldn't eat (IOL). **Straeuli forced to resign** after details emerged; 2003 RWC: first time no semifinal — **QF 8 Nov 2003, Melbourne, NZ 29–9** (allblacks.com).
- **Jake White/2007**: 2004 Tri-Nations won (clincher 23–19 v Aus, two yellow cards) — first since 1998. **Pool: 14 Sept 2007, STADE DE FRANCE, SA 36–0 England** (ESPN match page — Lens is dead). **Final 20 Oct 2007, Stade de France: 15–6**, no tries; **Montgomery 4 penalties + F. Steyn 1**; **Cueto try disallowed 42nd min — foot in touch under Danie Rossouw's tackle**. **Habana 8 tries = Lomu's single-tournament record (1999)**. **Os du Randt: only Springbok with two RWCs, 12 years apart**. Smit captain (83 times, record).
- **Habana career**: 124 Tests, 67 tries (to Jan 2018); **second all-time behind Daisuke Ohata (69 in 58 Tests for Japan)** — Campese (64) NOT the benchmark; **career 15 RWC tries, equalling Lomu, reached at the 2015 tournament** (world.rugby HOF).
- **De Villiers**: appointed **January 2008, "the first ever black coach of the Springboks"** (Al Jazeera). **2009**: Lions series 2–1 (26–21; **28–25 Loftus — Morné Steyn penalty from inside his own half with the last kick**; Lions 28–9 third) + **Tri-Nations won with a 3–0 sweep of the All Blacks** incl. 32–29 Hamilton (ESPN; sweep detail also on a wiki page — the sweep itself is well-attested; write "a clean sweep" without "first and only").
- **Brighton, 19 Sept 2015**: **Japan 34–32**, Pool B, Brighton Community Stadium. Final sequence: penalty inside SA's half in the last minutes, **Japan kicked for touch/scrummed instead of taking the draw — Michael Leitch's decision** (SA down a man); **Karne Hesketh over in the corner with the clock in the red** (rugbyworld.com; planetrugby; rugbyworldcup.com). Recovery: 46–6 Samoa, 34–16 Scotland, 64–0 USA; **QF 23–19 Wales (du Preez try in the left corner, ~5 min left)**; **SF 24 Oct, Twickenham: NZ 20–18**. (2012–15 coach: Heyneke Meyer — background fact only; old chapter's Meyer statistics NOT re-verified, do not reuse.)
- **Coetzee (2016–17)**: **Italy's first-ever win over SA: 20–18, Florence, 19 Nov 2016** (fact universally attested; agent's citation was a wiki URL — flag, but fact safe; BBC alternatives exist); SA dropped to **6th, equal-worst ranking** after the 2016 end-of-year tour (ultimaterugby); **Albany, 16 Sept 2017: NZ 57–0** (record defeat; stats.allblacks.com, crowd 30,021). **CONFIRMED NEGATIVE: no home defeat to Wales in this era — Wales's first win in SA was 9 July 2022, Bloemfontein, 13–12** (wru.wales).

## GEN 7 BRIEF (2018–July 2026) — no-wiki Haiku retrieval (adjudicated)
- **Erasmus unveiled coach 1 March 2018** (TimesLIVE). **Kolisi named captain 28 May 2018 — first Black captain in the team's 126-year history** (SA Rugby mag timeline).
- **Washington: 2 JUNE 2018** (not 7 June), RFK Stadium: **Wales 22–20 SA**. **Seven debutants in the starting XV** (Ismaiel, Mapimpi, Esterhuizen, Van Zyl, Kwagga Smith, Jenkins, Nche) **+ six uncapped on the bench** (Van der Merwe, Du Toit, Orie, Notshe, Papier, R. du Preez) (biznews/SA Rugby). Whether all six bench got on: unresolved — write squad framing ("seven new caps in the XV, six more waiting on the bench"). **Kolisi did NOT play Washington; his captaincy debut: 9 June 2018, Ellis Park, SA 42–39 England** (sarugbymag).
- **Mapimpi**: b. 30 July 1990, **Tsholomnqa village, Eastern Cape**; mother died when he was 14; "walked 20km a day" to school; Test debut at 27 in Washington (Rugby World "ten things").
- **2019**: Rugby Championship won (first title since 2009; shortened format). RWC pool: NZ 23–13 (21 Sept, Yokohama). **FINAL 2 Nov 2019, International Stadium Yokohama: SA 32–12 England** — **Mapimpi then Kolbe: "South Africa's first ever tries in a World Cup final"** (Rugby World). Kolisi lifts as first Black captain.
- **2021 Lions (closed stadiums, COVID)**: Lions 22–17; SA 27–9; **SA 19–16 — Sky headline: "Morne Steyn returns to deny the Lions again"** (12 years after Loftus 2009). Series 2–1.
- **ERASMUS VIDEO/BAN**: 62-minute video criticising the first Test's refereeing went viral; **World Rugby (Nov 2021): banned from ALL rugby activities for two months + banned from matchday activities until October 2022** (coaching, contact with officials, media) (Rugby World; rugbyandthelaw.com case analysis).
- **Wales's first win in SA: 9 July 2022, Toyota Stadium Bloemfontein, 13–12** (springboks.rugby itself).
- **2023 RWC**: pool **Ireland 13–8** (23 Sept, Stade de France); **QF 15 Oct: SA 29–28 France**; **SF 21 Oct: SA 16–15 England** (RG Snyman try; **Pollard last-gasp penalty**); **FINAL 28 Oct 2023: SA 12–11 NZ** — **record FOURTH title; all three knockouts won by ONE POINT**; Kolisi lifts again (Sky; Al Jazeera; Irish Times; TNT).
- **Coaches**: Nienaber head coach Jan 2020–RWC 2023 (→ Leinster); **Erasmus back as HEAD coach from 2024, signed to 2027** (springboks.rugby).
- **2024**: Rugby Championship won (5 of 6; first since 2019); Freedom Cup won 18–12, Cape Town (7 Sept).
- **2025**: **Wellington 43–10 — "New Zealand suffered their heaviest ever defeat"** (RNZ) — Freedom Cup retained; but **Eden Park: NZ 24–17** (streak intact); **SA ends 2025 ranked No. 1 (93.94)** (planetrugby).
- **JULY 2026 SNAPSHOT**: Nations Championship inaugural year. **4 July: SA 45–21 England** (Sky). **11 July: SA 42–28 Scotland, Loftus** (autumn-internationals). **18 July: SA v Wales, Kings Park, Durban, 17:40 SAST — third fixture, result pending as of 17 July 2026** (world.rugby match page). **World ranking No. 1, 93.96 (as of 12 July 2026)**. **Erasmus: record 55th match as head coach (9 July 2026, springboks.rugby)**. **Kolisi captain but withdrew from the England match (hamstring); Pieter-Steph du Toit captained v Scotland**; Kolisi (35) "ready to fight for his place" (The Star, Feb 2026).
- **Equity**: **6 Dec 2024: SARU members voted down the Ackerley Sports Group deal** — US$75M for 20% of the commercial-rights company; 7 of 13 voting unions opposed (News24); ASG pursuing a revival with an "approved South African consortium" (Jan 2025).
