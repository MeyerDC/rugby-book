# Chile — research notes

Fact + source cache for the Chile chapter. Write prose *from* here. Sources also at the end of
`chapters/03-chile.md`.

## Thesis
Most **elite-coded** origin (nitrate mines, Valparaíso ports, three English private schools), yet the
**fastest transformation** in the sport (amateur → World Cup in ~4 years).

## Generations (established)
- **Gen 0** nitrate/ports — "white gold," Valparaíso; clubs Wanderers, Everton.
- **Gen 1** Chile Rugby Union founded **1935**; first Tests vs Argentina 1936.
- **Gen 2** the **three English schools** (Grange, Craighouse, Mackay) & tours (Ireland 1952, France 1954).
- **Gen 3** the amateur decades.
- **Gen 4** "the tormentor."
- **Gen 5** building the pro thing — **Selknam** (Super Rugby Americas).
- **Gen 6** amateur-to-**RWC 2023** in ~4 years; **Pablo Lemoine** (coach), captain **Martín Sigren**.

## To research / open threads
- Post-RWC 2023 trajectory; 2027 qualification; Selknam results.

## REWRITE DESIGN (July 2026) — binding for the new draft

Mirrors the South Africa, England and Wales rewrites (`drafts/06-south-africa.md`,
`drafts/07-england.md`, `drafts/08-wales.md`). Triggered by the 2026-07-19 audit, which found the
chapter still in the book's original conversational voice (14 authorial "I" intrusions vs 0 in the
rewritten chapters), 2.3× South Africa's length for one generation fewer, anonymous attribution
throughout, and three hard factual errors.

1. **New file**: draft at `drafts/03-chile.md` (NOT in `chapters/` — combine_book.py bundles every
   .md there). Write ONLY from this notes file. The old `chapters/03-chile.md` returns at the end as
   a **fact-checklist, never as text**; on approval the draft replaces it and the old chapter moves
   to `drafts/03-chile-superseded-old-chapter.md`.
2. **Spine**: keep the established **Gen 0–6** map. Two range fixes the audit forced:
   - **Gen 0 → (1892–1934)**, not 1894–1934. The section's own centrepiece is Núñez's
     Coronel–Concepción find of 16 June 1892, which displaces the traditional 1894 Iquique date.
     The heading must not contradict the text beneath it.
   - **Gen 6 → (2023–2026)**, not 2024–2026. The CARR opens in 2023 and is load-bearing for the gen.
   - Target length **~500–550 lines** total (SA is 460 for Gen 0–7).
3. **Narration — the new voice** (retire the old one):
   - **Out**: the chatty first-person research voice — no "I want to be precise about this", "what I
     called their Gen 0", "I have not found sources that directly document", "one detail that I
     love", "I'm not going to soften them". No "Stop and appreciate that", "Hold that", "Read that
     again", "Think about that inversion for a moment" — the reader is not to be instructed how to
     feel about a fact.
   - **In**: composed, novelistic **third-person**, still immersive, still bold-dated cold opens.
     **Lead with the history.**
   - **Cut the thesis-first ending.** Gen 6 currently steps outside the story to restate the book's
     lens ("Return to the question this book keeps circling… **Institutions make the class. Not the
     founders.** Chile just proved it faster than anyone"). Per `SUMMARY.md` §1 that construction is
     a legacy of the book's origin, not a pattern to repeat. Let the reading emerge from events.
4. **Perspectives from inside, no villains** (the Latham model, per [[sa-chapter-latham-tone-model]]):
   - The **Anglo-Chilean school world** told from within, not sneered at. The old draft's register —
     "nobody else was much invited", "an old boys' network in Las Condes and Reñaca, and everybody in
     the room knew it" — is condescension standing in for explanation. These men built the only
     durable institution the sport had for eighty years; the closure is shown as institutions doing
     what closed institutions do, not as snobbery to be mocked.
   - **Mackay is the honest complication, not a fourth wall in the "three expensive schools" frame.**
     Founded 1857 as the Valparaíso Artizan School for children of British craftsmen *of limited
     means*. The old draft flattens it into the elite trio. Keep the seam visible.
   - **Lemoine is a hinge, not a messiah.** The old draft runs hagiography — "The tormentor became the
     liberator", the Wyllie/Van Heerden "same revolution" refrain twice. No hero people. His own
     framing (professionalism as a social upheaval players pay for personally; "you have to pay them")
     is the interesting part and survives; the saviour arc does not. Guard against the Wales
     **messiah reflex** motif — Chile's turn is a *system* (franchise, contracts, a building), and
     the draft should say so rather than credit one man.
   - **Selk'nam: hold both halves.** A settler state's sport named its first professional team after a
     people that state's own frontier expansion helped destroy, and put a Hain initiation spirit on
     the chest. The old draft takes this as uncomplicated uplift ("a sport announcing that it intends
     to belong to Chile"). Keep the power of the gesture AND the discomfort in it. Do not resolve it.
5. **Sourcing — no wiki**: this is the biggest lift. The existing fact base is sound but was verified
   largely *against Wikipedia*; the new format needs **named sources carried in the flow of the
   prose** (the way SA carries Winch, Difford, Dobson, Odendaal, Van der Merwe). Per-generation
   retrieval passes required to find nameable Chilean/Argentine sources. "The sources put it plainly",
   "one writer", "one report drily put it", "a Chilean rugby writer" are all banned.
   - Known nameable so far: **Sebastián Núñez** (the 1892 Coronel–Concepción research, from *The
     Chilean Times*, 9 July 1892), *The Rugby Journal*, Sudamérica Rugby, Rugby Chile, Americas Rugby
     News, La Tercera.

### Corrections the redraft MUST carry (2026-07-19 audit)

- **Chile's only South American title is 2015, not 1995.** The 2026-07-15 pass fixed the body but left
  two leftovers in the old chapter (Gen 3 tease, "What Gen 4 left"). Do not reinstate 1995.
- **The 1952 jet line is wrong and inverted.** Old text: 1952 was "three years before the first
  commercial jet crossed the Atlantic." First transatlantic commercial jet service was **4 Oct 1958**
  (BOAC Comet 4) — six years *after*. And **1952 was itself the year commercial jet service began at
  all** (Comet, London–Johannesburg, 2 May 1952). If the beat is kept, it inverts: the Irish tour
  coincided with the opening weeks of the jet age.
- **The 400% boom is UNVERIFIABLE outside Wikipedia** and cannot be stated as fact. It is currently
  the entire engine of Gen 3 and is re-invoked in Gen 4 ("a 400% boom whose fruit had never been
  picked"). Same trap as Romania's fabricated "25-match unbeaten record."
  → **Gen 3 gets a new engine**: the verifiable club-spread evidence — **Los Troncos** and **Old
  John's** in **Concepción**, ~400km south of the Santiago–Viña axis — plus whatever a retrieval pass
  can name. The percentage may only appear, if at all, openly hedged as an unsourced claim.
- **The 1986 IRFB centenary congress** attendance is wiki-only; a non-wiki citation offered by a
  retrieval agent did not hold up. It currently carries a whole section ("The last act: sitting at the
  top table"). Re-source or cut.
- **Larenas's "50 caps / 11 tries"** specifics remain unverified — use the verified description
  (most-capped player and record try-scorer, debut 2012) without the numbers.
- **Gen 6's ending is falsified and must be rewritten.** The old chapter ends on Chile "hunting that
  scalp" v Georgia "in La Serena on 18 July." Played **18 July 2026** at the **CARR, Parque Mahuida,
  La Reina, Santiago** — behind closed doors, heavy rain — **Georgia won 49–22**, ending Chile's
  Nations Cup unbeaten start. Tries: Georgia through Tchumbadze, Jincharadze, Ivanishvili,
  Shvangiradze; Chile through Manuel Bustamante and Santiago Videla; 28–15 at half-time. New dated
  cutoff = **19 July 2026**. Note the venue irony: the defeat happened in the building Gen 6 holds up
  as the sport's first real home.
- **Watch for cross-code conflation.** The notes already caught one (a 2024 rugby *league* title read
  as union). A 2026-07-19 retrieval agent produced another: "Argentina's first international was v
  Uruguay, July 1902, lost 6–0" — that is **football** (16 May 1902), impossible for rugby since
  Uruguay's first rugby international was 1948 v Chile. **Chile 1936 as the first match between two
  South American national sides STANDS.**

### Repetition to eliminate (old chapter counts)

Sigren's "amateur club / twice a week" quote appears **4×** (L481, L599, L727, L893); Garafulic's
"dirt" **8×**; Lemoine's "either them or us" **3×**; "sleeping giant" **2×**. Gen 4's closing "2018"
section and Gen 5's opening narrate the **same Lemoine arrival twice**. Each quote gets **one**
placement. This alone accounts for much of the 2.3× length over South Africa.

## GEN 0 REWRITE BRIEF (1892–1934) — named-source retrieval, 2026-07-19

Gathered for the no-wiki redraft. **Headline: the old chapter's "forty years of silence" framing is
wrong** and must go — see §"The 1920s club scene" below.

### Named sources now available for in-flow attribution
- **Sebastián Núñez** — researcher; collaborated on *Toda la Historia de la 'U'* (2017) and
  *Universidad de Chile: Su deporte y protagonistas en el Siglo XX* (2018). His find is the 1892 match.
- ***The Chilean Times*** (Valparaíso, **1876–1907**) — the British community's main paper in
  19th-c Valparaíso; printed by Imprenta Universo. **The 9 July 1892 chronicle is the primary document.**
- ***The South Pacific Mail*** (from **6 Nov 1909**, founded by **Henry Hill**) — successor to *The
  Chilean Times* / *The Anglo-Chilian Times* (1907–08); "official organ of the English-speaking
  communities in Chile and Bolivia" by 1914; reached 30 Chilean cities within 3 months.
- ***The Illustrated Sporting and Dramatic News*** — **1893** edition carries the HMS *Warspite* match.
- **Harold Blakemore** — English historian of Chile; the standard authority on British nitrate capital
  and John T. North.
- **"Traces of Nitrate"** — Univ. of Brighton research project (Xavier Ribas; Dr Louise Purbrick) on
  British investment in the nitrate mines, 1879–1914.

### The 1892 find (displaces 1894 Iquique)
- **16 June 1892, Coronel v Concepción.** Reported in *The Chilean Times*, **9 July 1892**.
  **Concepción won by 4 tries + a conversion to 2 tries.**
- **Coronel was a compulsory coaling stop** for European ships in the Pacific before the Panama Canal
  — that is *why* there was rugby there. Coal, not nitrate.
- **HMS *Warspite*** (RN cruiser, built 1884): *The Illustrated Sporting and Dramatic News*, 1893,
  records her crew playing a Concepción side "very probably constituted by mariners of the locality."
- Source: [Se reescribe la historia del origen](https://www.rugbychile.cl/2020/05/05/en-la-semana-del-rugby-chileno-se-reescribe-la-historia-de-su-origen/) — Rugby Chile

### The 1894 Iquique story
- **NO ORIGINAL SOURCE LOCATED.** The claim (English cargo crew v a saltpetre-companies team) recurs
  in modern accounts but nobody has produced the document. → **Treat explicitly as folklore/received
  tradition in the prose**, which is also better Latham-model practice than asserting it.

### British Valparaíso — the world the game arrived in
- **~10,000 English residents in Valparaíso by 1890**, of ~190,000 total; ~32,000 settled in the
  region across the period. Cerro Alegre as the British quarter.
- **Union Club, 1842** — library and reading room.
- **Valparaíso Sporting Club, 1882** (British origin); hosted the Chilean Derby from 1885.
- **Santiago Wanderers, 1892** ✓ (already verified). **Everton, 24 June 1909** ✓.
- Source: [British and Anglo-Saxon presence in Chile — Valparaíso](https://www.anglochileansociety.org/single-post/british-and-anglo-saxon-presence-in-chile-during-the-19th-century-valparaiso) — Anglo-Chilean Society

### The schools — official histories
- **The Mackay School — 8 October 1857**, by **Peter Mackay** (from Argyll; MA Univ. of Glasgow; maths
  tutor at the Free Church Normal Seminary, Glasgow; emigrated 1857). Founded as the **Valparaíso
  Artizan School**, for "quality education for the children of English, American and especially
  Scottish **craftsmen of limited resources** who worked in the **factories and railroads** of
  Valparaíso." 140+ pupils by 1866; **1871** first course for Chilean children. Mackay and **George
  Sutherland** split on religious grounds 1877; renamed for Peter Mackay on his death (**1905**);
  later moved to Reñaca. → **The "railroads" detail ties Mackay straight into the informal-empire
  motif. This is the school that does NOT fit the "three expensive schools" frame — keep the seam.**
- **The Grange School — 4 June 1928**, by **John A. S. Jackson** (b. 1898 Valparaíso, British-descended;
  Cheltenham College + Cambridge). Began with **12 pupils** in a private house, "Villa Angela," Av.
  Pedro de Valdivia. Founding principles: *Fair Play, All Rounder, Good Manners, Spirit of Service.*
  300 pupils (120 boarders) by 1938. After the 1929 crash, families kept sons in Chile → hybrid
  British/Chilean model. Jackson d. 13 Mar 1958. Quotable: seeking a 1936 bank guarantee, he offered
  as security "the men I am shaping for Chile's future."
- **Craighouse — 16 March 1959**, by **Charles T. Darling** and **Joan Gibson-Craig-Carmichael**.
  **Played hockey and rugby from the start.**
- ⚠️ **Rugby-adoption dates for Mackay and Grange NOT documented** — founding ≠ start of rugby. Do not
  assert that either school played rugby from its founding year.

### The 1920s club scene — KILLS the "forty years of nothing" framing
The old chapter says the game had "almost no documented history at all" for forty years and that Chile
got "only matches: scattered, sporadic." Not so. A real club scene assembles in the 1920s, and it is
what the 1935 union is actually built on:
- **Badminton Sports Club — 1920, Viña del Mar.** First Viña club to compete in Santiago tournaments;
  fielded English players just back from England (e.g. **William Kinnear**). Beat Old Grangonians 32–8.
- **Prince of Wales Country Club** — named for the Prince of Wales (later Edward VIII); **rugby section
  1927**. A founding member of the federation. ⚠️ club founding date conflicts (1908 vs 1925).
- **Green Cross** — club founded 1916, **rugby section 1927**.
- **Stade Français — 14 July 1929** (Bastille Day), merging Lawn Tenis Francés (1917) + Sport Français;
  **rugby section 1930**, begun "with just a ball and a blackboard." Beat Badminton 6–3 on 21 Aug 1932;
  **46 members by 1934.** ✓ (French colony, not British — already noted.)
- → By the early 1930s there are roughly **four or five rugby-playing clubs** in Santiago and Viña.
  **1935 is the roof going on a house that got built in the 1920s**, not a sudden act of creation.
- ⚠️ WIKI-ONLY / SHAKY, do not use: "Santiago Football Club (1885) transitioned to rugby in the 1890s."

### Old-boys clubs — real founding dates (later than the old chapter implies)
- **Old Boys / Old Grangonian Club (Santiago) — 1938**, by former Grange pupils. Most-decorated Santiago
  club (20 Central Championship titles). → **Postdates the 1935 union.** The old chapter's Gen 0/Gen 2
  framing implies the old-boys clubs built the game *before* the union; the dates say otherwise.
- **Old Mackayans (Viña) — rugby section 28 April 1956** (first match that day; name fixed by William
  Pérez H.'s letter of 18 Apr 1956; Pérez the first coach, later Mackay's rector in the 1980s). Parent
  Old Boys Association 19 Aug 1952 (legally recognised 1 Oct 1939). Incorporated 1957.
  [Old Mackayans — historia](https://oldmackayans.cl/historia/)
- **Old John's (Concepción) — 1991**, ex-pupils of Saint John's School. Debut **14 April 1991**, beat
  Los Canguros de Chillán 31–6.
- **Los Troncos (Concepción) — 1978**, founded by **forestry engineers from Santiago and Valdivia, led
  by John Scott.** → **IMPORTANT for Gen 3**: Los Troncos *predates* the claimed 1980s boom. It is a
  dated, named, occupational-diffusion instance of the game leaving the two cities — forestry doing in
  the south what nitrate did in the north. **This is the replacement engine for the unverifiable 400%
  figure.** [Los Troncos celebra su 45 aniversario](https://www.rugbychile.cl/2023/06/16/los-troncos-celebra-su-45-aniversario/)

## Gen 0 — verified facts (fact-checked 2026-07-15)

- **Everton de Viña del Mar founded 24 June 1909** (NOT 19th century) by Anglo-Chilean youths;
  named after Everton FC (Liverpool), then touring South America. (Chapter previously said "since
  the nineteenth century" — corrected.)
- **Santiago Wanderers founded 15 Aug 1892**, Barrio Puerto, Valparaíso — oldest football club in
  Chile. (19th-century club, correct.)
- **The Grange School** — Santiago, founded **1928** by Anglo-Chilean John A. S. Jackson. Fits the
  "1920s" schools framing.
- **The Mackay School** — founded **1857** in Valparaíso by Peter Mackay (Scottish) as the
  *Valparaíso Artizan School*, to educate children of English/American/Scottish **craftsmen of
  limited means**. Moved toward Reñaca/Viña after a 1946 land purchase. (NB: artisan origins sit
  awkwardly with the "three *expensive* schools" framing — Mackay is the weak leg. Left as light
  shorthand in prose; date added.)
- **Craighouse** — founded **1959** in Santiago (Darling family). NOT a 1920s school — chapter fixed
  so Craighouse is flagged as the later third leg, not part of the 1920s founding.
- **Origin dating is genuinely contested.** Traditional story: first game **1894 at Iquique**,
  English cargo crew vs a nitrate-companies team, then spread to Valparaíso/Santiago. Newer research
  (**Sebastián Núñez**, from *The Chilean Times*, 9 July 1892): a match **Coronel vs Concepción on
  16 June 1892** — two years earlier, in the **coal** south, likely a Royal Navy crew (HMS Warspite
  appears in an 1893 account). Chapter now presents 1894/Iquique as the traditional account and the
  1892 Coronel find as the complication.
- Union dating stays contested (1935 / 1948 / 1953) — handled in Gen 1; Gen 0 uses 1935.

## GEN 1 REWRITE BRIEF (1935–1950) — named-source retrieval, 2026-07-19

**Headline: the "decade of nothing" (1938–48) is wrong — but not for the reason a retrieval agent
claimed.** There was no *international* rugby; domestically the decade is when the game stopped being
foreign. See "The 1940s" below.

⚠️ **CONFLATION CAUGHT (third of its kind).** A retrieval agent "verified" a continuous domestic
championship 1938–48 with an RSSSF table listing Magallanes, Colo Colo, Audax Italiano, Unión Española,
Santiago Morning, Universidad de Chile. That is the **Chilean FOOTBALL first division**. Discarded.
(Prior conflations: a 2024 rugby *league* title read as union; a 1902 Argentina–Uruguay *football*
result read as rugby.) **Always check club names against the code before accepting a table.**

### The 1936 tour — World Rugby Museum, "Crossing the Andes" (citable, non-wiki, rich)
- Argentine delegation flew in two batches, **15 and 18 September 1936**, aboard the PANAGRA aeroplane
  **"Santa Lucía"**. ~12 days in Chile.
- **20 Sept 1936, Playa Ancha, Valparaíso: Argentina 29–0 Chile. ~3,000 spectators.** Valparaíso's
  400th anniversary. First match between two South American national sides; **Argentina's first-ever
  match abroad**.
- **23 Sept 1936, Stade Français ground, Santiago: Argentina 66–0 Prince of Wales Country Club**
  (~2,000 spectators).
- **27 Sept 1936, Playa Ancha: Argentina 31–3 Chile.**
- **Tour aggregate: 126 points to 3**, three matches.
- **Argentina captain: Arturo Rodríguez Jurado (San Isidro Club), at No. 8.** Manager/president **Luis
  Cilley** (SIC). 18 players from 9 clubs. Wing **Emilio Schiavio** "the try man". Referee for the first
  two matches: PL Sormani.
- **Chile captain: J. G. Hopkins**, who was *also* the union's secretary and treasurer. Union president:
  **David Blair**. **Chile had 4 rugby clubs.**
- Source: [Crossing the Andes: Los Pumas to Chile](https://worldrugbymuseum.com/from-the-vaults/international-rugby/crossing-the-andes) — World Rugby Museum (cites *El Gráfico*)

### Rodríguez Jurado — VERIFIED, and a gift of a detail
- **Olympic heavyweight BOXING gold medallist, Amsterdam 1928**, beating Sweden's **Nils Ramm** in the
  final (stoppage). Nicknamed **"el Mono."** b. San Luis, 1907. Captain of the Argentine XV later known
  as Los Pumas; a founder of **San Isidro Club**. (His son and namesake, also a Puma, d. June 2025 —
  don't confuse them.) So the man who captained the side that beat Chile 29–0 in Chile's first
  international was a reigning-era Olympic boxing champion.

### 1938 — thin
- August 1938, Buenos Aires: Chile lost **33–3** and **25–3**; also played Olivos RC and Old Georgian.
  ⚠️ **WIKI-ONLY** — no Spanish-language confirmation found. Keep the scores (they match the earlier
  pass) but do not invent detail around them.
- Four Tests total 1936–38, all v Argentina, all lost: **Chile 9 – Argentina 118**. ✓

### The 1940s — what actually happened (this is the new spine of Gen 1)
**Chunchos — Universidad de Chile Rugby Club — VERIFIED via two Rugby Chile articles:**
- Founded **15 June 1941** by **Alberto Zamorano** and a group of students, under the presidency of
  **Benjamín Claro Velasco**; consolidated under **Aníbal Bascuñán Valdés**.
- **"The first rugby team formed in Chile without foreign origins."** ← the key sentence
- **First official match: beat Stade Français 11–3.**
- **1941: champions of the Second Division**, promoted to the División de Honor — in their first year.
- Describes itself as **the oldest federated club in the country** (PWCC and Stade Français are older
  as *clubs*; the claim is about federation — phrase carefully).
- **Precursor to the founding of Club Universidad Católica rugby, 1942.**
- Organised the **first Inter-University Championship, 1946**; promoted the **Chile–Mendoza exchange,
  1952**; ran the **first youth-category competition, 1956**.
- Sources: [Chunchos: 85 años de historia y legado](https://www.rugbychile.cl/2026/06/16/chunchos-85-anos-de-historia-y-legado-en-el-rugby-chileno/) and [U. de Chile RC y sus 79 años de vida](https://www.rugbychile.cl/2020/06/18/u-de-chile-rc-y-sus-79-anos-de-vida/) — Rugby Chile

**First national club championship: 1948, won by Prince of Wales Country Club** (7 titles to 1971).
PWCC: club founded 1925, opened by the Prince of Wales (later Edward VIII); **rugby section 1927**.
[pwcc.cl historia](https://www.pwcc.cl/page/historia)

→ **REFRAME FOR THE DRAFT:** the ten years without a Test are the ten years the game acquired a
domestic competition and its first Chilean-origin clubs. The counter-current to the English schools
does not arrive in the 1980s, as the old chapter implies — it arrives in **1941, from the state
university**, and it wins promotion in its first season by beating the French colony's club. The old
chapter's Gen 2 line that Chilean rugby had "no friction at all… no provincial rebellion of any kind"
is overstated and must go.

### 1948 — the first win
- **5 August 1948, Buenos Aires: Chile 21–3 Uruguay** — Uruguay's first-ever international, Chile's
  first-ever win. Part of a Chilean tour of Argentina; Chile also played **Hindú Club**. ✓
- ⚠️ Scorers/player names NOT found.

### Still missing after this pass (do not invent)
- The union's founding members and first president (federation's own site lacks it; only Blair/Hopkins
  from 1936 are named). Chile 1936 squad beyond Hopkins. 1938 detail. 1948 scorers.

## Gen 1 — verified facts (fact-checked 2026-07-15)

- **1936 debut vs Argentina was in VALPARAÍSO, not Santiago.** 20 Sept 1936, Estadio Playa Ancha,
  staged for the **400th anniversary of Valparaíso**, ~3,000 spectators. Also the **first match ever
  between two South American national teams**. (Chapter previously said "Santiago" and mis-framed
  Valparaíso as an Argentine-source variant — corrected.)
- **First-Test score was 0–29** (both Chilean & Argentine records), NOT 0–20. Second Test, a week
  later, **31–3**. (Corrected.)
- **1938 = TWO Tests vs Argentina in Buenos Aires (Aug), lost 33–3 and 25–3** — so **four** Tests
  across 1936–38, all vs Argentina, all lost, combined ≈ **Chile 9 – Argentina 118**. (Chapter had
  said three Tests / "6–84" — corrected.)
- **It was Argentina's first-ever away Test** (63 years of rugby, never left home). ✓ kept.
- **"Second South American nation to play international rugby" = CORRECT.** Argentina played
  internationally from 1910; Chile 1936 is the second nation. Brazil later (1951). ✓ kept.
- **1948 first win: Chile 21–3 Uruguay, Buenos Aires, 5 Aug 1948** — Uruguay's first-ever
  international, Chile's first win. On the same 1948 tour Chile also played Hindú Club. ✓ confirmed.
- Union founding **1935** (Unión de Rugby de Chile) confirmed; later renamings (1948 / 4 May 1953
  Federación Chilena de Rugby, statutes 1963) left as the chapter's contested-dates note.

## GEN 2 REWRITE BRIEF (1951–1971) — named-source retrieval, 2026-07-19/20

**Two headline findings: the chapter finally has named Chileans, and the old "third in South America"
conclusion is wrong.**

⚠️ **CONFLATION CAUGHT (fourth).** A retrieval agent offered the "**Copa del Generalísimo Juvenil**,
1956" as Chile's first youth competition. That is **Spain's** youth cup (*Generalísimo* = Franco).
Discarded. Chunchos' own history is the source for Chilean youth rugby (see Gen 1 brief).

### ⭐ THE CAMPBELL BROTHERS — the human centre Gen 0–2 was missing
**VERIFIED at World Rugby's own Hall of Fame** (non-wiki, authoritative):
[World Rugby Hall of Fame — Ian Campbell](https://www.world.rugby/halloffame/inductees/706493)
- **Ian Campbell** (15 May 1928 – 11 November 2022), of Scottish descent. **Centre**, **Prince of Wales
  Club, Santiago**, international career **1948–1961**. **16 matches, 43 points** (6 tries, 7 penalties,
  2 conversions) — also the side's kicker.
- **Debut aged 20 in "Chile's first post-war international, against Uruguay, in 1948"** — i.e. the
  **21–3 first-ever win**. He then **appeared in every single international Chile played until 1961**.
- **Captained Chile at the inaugural South American Championship, 1951.**
- Called **"the father of modern Chilean rugby."** Served Prince of Wales ~30 years.
- **Inducted into the IRB Hall of Fame in 2012, alongside his brother Donald.**
- Photographed with the Webb Ellis Cup in Santiago **aged 91** (2019, Rugby World Cup social media).
- **He died 11 November 2022 — four months after Chile qualified for their first World Cup (16 July
  2022), and ten months before they played in it.** ← thread this to Gen 5/6. He lived to see it.
- **Donald Campbell**, Ian's older brother. Also a **centre**, also **Prince of Wales**. **Debut 1938
  v Argentina.** **Volunteered as an RAF pilot in 1941; died in action 12 September 1944** (Bomber
  Command, over Germany).
- → The two brothers bracket the "silent decade" exactly: Donald debuts in the 1938 defeats and is
  killed in 1944; Ian debuts in the 1948 first win. **The war did not merely suspend Chile's fixtures;
  it killed one of its internationals.**

### ⭐ CORRECTION: Chile was SECOND in South America, not third
The old chapter's Gen 2 conclusion — "A permanent position: third in South America, occasionally
second" — is **backwards for this era**. Tournament record:
- **1951** (inaugural, Buenos Aires, 9–16 Sept; Estadio GEBA & Ferrocarril Oeste): **Chile 3rd.**
  Chile 68–0 Brazil; **Uruguay 8–3 Chile**; Argentina beat Chile (**13–3 per Chilean records / 17–10
  per the tournament source — unresolved**). Uruguay 2nd. ✓ (matches earlier pass)
- **1958** (hosted by Chile): Chile 34–9 Uruguay, 31–3 Peru, lost 0–14 Argentina → **2nd**
- **1961** (Montevideo, 8–14 Oct): lost 11–3 Argentina; beat Uruguay 28–5; beat Brazil 34–5 → **2nd**
- **1967** (Buenos Aires, 28 Sept–1 Oct): lost 18–0 Argentina; beat Uruguay 16–11 → **2nd**
- **1969** (hosted, Santiago, 4–11 Oct, Prince of Wales CC): beat Uruguay 13–6; **lost 54–0 Argentina**
  → **2nd**
- **1971**: beat Uruguay 11–6, Paraguay 40–0, Brazil 45–3; lost 20–3 Argentina → **2nd**
- Runner-up also in **1975 and 1981** — seven second places in all.
- ⚠️ **WIKI-CORROBORATED ONLY** (consistent across five separate tournament pages, but no non-wiki
  source located). **Hedge lightly in prose**; do not cite wiki.
- → **Also note**: Chile beat Uruguay in 1958, 1961, 1967, 1969 AND 1971. The "grinding rivalry for
  second" the old chapter dates to 1948 does **not** describe this era — in the fifties and sixties
  Chile was simply the better of the two. The rivalry turns later.

### The visitors
- **Ireland, 1952, Santiago: Ireland 30–0 Chile.** Non-cap match; tour captain **Des O'Brien**, manager
  G. P. S. Hogan; 21 players incl. Jim McCarthy, Ronnie Kavanagh, John O'Meara, Mick Lane.
  ⚠️ **DATE UNRESOLVED — 9 August 1952 (this pass) vs 18 September 1952 (earlier pass).** Both
  wiki-derived. **Use "1952" without a day** until settled.
- **France, 18 September 1954, at the Prince of Wales Country Club, Santiago: France 34–3 Chile.**
  (The 42–3 variant remains unresolved; 34–3 retained per the dedicated tour page.) 12-match tour, all
  won; 2 Tests v Argentina (22–8, 30–3). The 1960 France tour was of Argentina and Uruguay — Chile got
  exhibition matches only, no Test.
- **Junior Springboks, 30 September 1959, Prince of Wales Country Club, Santiago: South Africa 73–0
  Chile.** Referee C. Ackermann. ⚠️ WIKI-ONLY but consistent with the documented 1959 tour. **The old
  chapter omits this entirely** — it is the heaviest defeat of the era and belongs in.
- Note the venue pattern: Prince of Wales CC hosts France 1954, the Junior Springboks 1959 and the 1969
  championship. **One club's ground was effectively the national stadium.**

### The domestic machine
- **Craighouse — 1959** (Charles T. Darling; Joan Gibson-Craig-Carmichael), **rugby from the start**;
  **Craighouse Old Boys founded 1972.** → the third school arrives only at the end of Gen 2.
- **Old Mackayans** — first match **28 April 1956**; joined the ARUSA Central Championship **1957**;
  first coach **William Pérez H.** [oldmackayans.cl/historia]
- **Sporting, Viña del Mar — 1963**, by architecture students of the Universidad Católica de Valparaíso;
  **the first rugby club in the V Region**; joined the first division 1972. [sportingrugby.cl]
- **Universidad Católica rugby — May 1942**, founded by **Jorge Jhohnson, Mauricio Wainer, Sergio
  Urrejola**; champions **1949 and 1954**. ⚠️ founders/titles WIKI-ONLY.
- **Campeonato Central** from 1948; **ARUSA** (Asociación de Rugby de Santiago) formalised 1948.
- **PWCC centenary piece** (useful, non-wiki): [Prince of Wales Country Club celebra 100 años de
  historia y 90 años de rugby](https://www.rugbychile.cl/2025/03/11/prince-of-wales-country-club-celebra-100-anos-de-historia-y-90-anos-de-rugby/) — Rugby Chile. Confirms **rugby section 1935**.

### ✂️ CUT: the 1986 IRFB centenary congress
The old chapter gives this a whole section ("The last act: sitting at the top table"). Three reasons to
delete it outright:
1. **No non-wiki source exists.**
2. **Chile was not an IRFB member in 1986** — the board had eight members (the four Home Unions,
   France, Australia, New Zealand, South Africa). Chile joined only in **1991**.
3. **It is anachronistic to the generation anyway** — 1986 sits fifteen years outside Gen 2's
   1951–1971 range, which nobody appears to have noticed.
**Do not reinstate.**

### Still missing (do not invent)
Chilean players of the era beyond the Campbells; national-championship winners through the 1950s–60s;
the Ireland 1952 date; the 1954 and 1951 score variants; crowd figures for 1958.

## Gen 2 — verified facts (fact-checked 2026-07-15)

- **1951 South American Championship** (first Sudamericano, staged around the 1951 Pan-American
  Games): final standings **Argentina 1, Uruguay 2, Chile 3, Brazil 4**. Argentina beat Uruguay
  62–0, Brazil 72–0, Chile (13–3 per Chilean records / 17–10 per tournament source). **Uruguay beat
  Chile 8–3**; Chile beat Brazil 68–0. → Chile were NOT "the best of the rest" in 1951 (Uruguay
  finished above them). Chapter corrected.
- **1952 Ireland tour:** real — 1952 Ireland tour of South America; opened in Santiago, **Ireland XV
  beat Chile 30–0** (18 Sept 1952), then Buenos Aires (first full Ireland–Argentina internationals).
- **1954 France tour of Argentina & Chile:** **12 matches, all won by France**; 11 in Argentina + 1
  in Chile. **2 Tests vs Argentina** (France 22–8 and 30–3), NOT three. **France beat Chile 34–3**
  (Chile match-list gives 42–3 — discrepancy; used 34–3 from the dedicated tour page). The **1960**
  France tour was of **Argentina and Uruguay** (not Chile). Chapter corrected ("fourteen matches,
  three vs Pumas" was wrong).
  - ✅ RESOLVED (cross-chapter): the 1954 tour match list is 11 in Argentina + 1 in Chile = 12 total,
    2 Tests vs Pumas (22–8, 30–3). The Argentina chapter said "fourteen matches in the country" —
    CORRECTED to "all eleven of their matches in Argentina … a twelve-match tour that also crossed to
    Chile … both Tests, 22–8 and 30–3." Both chapters now consistent.
- **1958 South American Championship (hosted by Chile):** Chile beat **Uruguay 34–9** and **Peru
  31–3**, lost to **Argentina 0–14**, finished **2nd**. ✓ confirmed.
- **Argentina–Chile scoreline list (1958–1967) all check out:** 1958 14–0 (Santiago), 1961 11–3
  (Carrasco, Montevideo), 1964 30–8 (São Paulo), 1965 23–11, 1967 18–0 (Buenos Aires). Chile's
  25-point total across the six listed defeats is correct.
- **1986 IRB centenary congress — Chile attended:** ✅ VERIFIED. "Chilean delegates were amongst
  those who went to the centenary congress of the International Rugby Football Board in 1986"
  (Wikipedia, Rugby union in Chile). IRFB centenary = 1886→1986; centenary match 19 Apr 1986. Chapter
  claim stands, no change.

## GEN 3 REWRITE BRIEF (1972–1989) — named-source retrieval, 2026-07-20

**Three headline findings:** (1) the crash has a named Chilean human centre — **Sergio Catalán**;
(2) the Pinochet-rugby question is NOT silence — the answer is the **1983 South Africa tour**, in a
named player's own words; (3) the 400% figure is replaced by **dated, named regional clubs**.

### The crash, from the Chilean side
- Flight 571, 13 Oct 1972, Mendoza→Santiago, Old Christians (Stella Maris alumni) coming to play
  **Old Boys Club** in Santiago (the established, cross-chapter-consistent name; a retrieval agent
  offered "Old Grangonian Club" — plausibly the same Grange-alumni club's formal name, but keep "Old
  Boys" for consistency with the Uruguay chapter and the wider record). **A return for Old Christians'
  1971 tour of Chile** (they won 1, lost 1 in 1971).
- **Sergio Catalán** — Chilean **arriero** (muleteer). On **21 Dec 1972**, after Parrado & Canessa's
  ~10-day trek, he saw the two across the **Río Barroso/San José**, could not hear them over the water,
  **threw across a stone wrapped with pencil and paper**; Parrado wrote the note ("Vengo de un avión que
  cayó en las montañas…"). Catalán then **rode ~10 hours / a long distance to Puente Negro** to raise
  the alarm → rescue **22–23 Dec 1972**. Survivors called him **"Papá Sergio"**; later funded his
  medical care. **Died Feb 2020, aged ~91.**
- Survivor **Gustavo Zerbino**: "Thanks to our great friend, Sergio Catalán, in an example of
  solidarity he went [a great distance] on a horse to notify authorities that he had found two
  survivors." (Americas Rugby News obituary)
- No documented **Chilean Air Force (SAR)** role in the actual find — the rescue flowed from Catalán's
  alarm. (SAR flights had searched earlier and failed.)
- Sources: [Sergio Catalán obituary (2020)](https://www.americasrugbynews.com/2020/02/12/sergio-catalan-who-helped-save-uruguayans-in-andes-in-1972-passes-away/) — Americas Rugby News;
  [Miracle in the Andes, 50 years on](https://www.world.rugby/news/770898/a-story-of-tragedy-and-disaster-hope-and-survival-the-miracle-in-the-andes-remembered-50-years-on) — World Rugby

### ⭐ THE PINOCHET QUESTION — answered, honestly, via the 1983 South Africa tour
The regime's direct effect on rugby is genuinely undocumented (no rugby victims/exiles/associates
traced; the Estadio Nacional detention centre of 1973 has no located rugby connection). BUT the era's
real link is the **1983 Chile tour of South Africa**, and it is exactly the no-villains / no-sugar
material:
- **VERIFIED, non-wiki, in a named player's words** ([Rugby World, Sept 2023](https://www.rugbyworld.com/news/meet-the-chile-legend-who-blazed-the-trail-for-team-taking-on-england-159719)):
  **Francisco "Pancho" Planella** — fly-half, Chile international **1975–1988**, **captain for seven
  years** in the 1980s, a **Grange** man (now the Grange School First XV manager). On the 1983 tour:
  **10 matches, won 3**, playing at **Newlands and Loftus Versfeld.**
- **Planella, verbatim:** *"Because of apartheid in South Africa, nobody wanted to play them. Chile had
  relations with the government and many teams came to play."* And: *"That helped Chile to start growing
  with rugby."*
- → This is the honest frame: **two internationally isolated states — apartheid South Africa and
  Pinochet's Chile — playing each other because the world would not play either.** Chile got its
  highest-level exposure of the era from a partnership of pariahs. State it from inside (Planella
  valued the rugby education; it did help), keep the stain visible (why the fixture existed at all),
  no editorialising verdict. **Threads directly to the SA chapter's Gen 4 "Barbed Wire" (1980–89).**
- Planella on watching Chile's 2023 World Cup debut: *"Singing the national anthem, of course, I was
  crying. My generation put something there and it has grown."* → lovely Gen 3→5/6 bridge.

### ⭐ THE GROWTH — the verifiable version (replaces the unusable 400%)
Dated, named, occupational/regional diffusion — the game leaving the Santiago–Viña axis:
- **Los Troncos — June 1978**, Concepción/Arauco region. Founded by **forestry engineers led by John
  Scott** (a Scot with New Zealand rugby background), who had come from Santiago and Valdivia for the
  timber industry. Joined the Arauco association 1979; 36 adult titles by 2022; won the 2007 Central
  Championship. → **forestry in the south doing what nitrate did in the north.**
  [Los Troncos 45 años](https://www.rugbychile.cl/2023/06/16/los-troncos-celebra-su-45-aniversario/)
- **San Bartolomé — 1980, La Serena**, founded by Alberto Viada (U. de Chile) & Enrique Barrios;
  named for the city's patron saint; built the Parque Pedro de Valdivia municipal ground 1985; fed
  players to the Cóndores. → **"rugby in the neighbourhoods of La Serena"** (the article's own frame —
  neighbourhood/municipal, NOT school/old-boy). [San Bartolomé](https://www.rugbychile.cl/2020/08/14/la-historia-de-san-bartolome-rugby-en-los-barrios-de-la-serena/)
- Also: **Deportes Valdivia (1983)**; Temuco (Rucamanque); Antofagasta association active. ⚠️ these
  three thinner-sourced — name Los Troncos and San Bartolomé as the anchors.
- **~20 active clubs nationally by the mid-1980s** (approx; hedge).
- **DROP the "400%" entirely.** Do not cite it, even hedged — the named clubs carry the point better.

### CONSUR — 1988
- **Founded 14 October 1988, Asunción**: Argentina, Brazil, Chile, Paraguay, Uruguay; ratified Punta
  del Este, Jan 1989. Chile a **founding member**. Chile's federation president at the time / delegate:
  **Sergio Bascuñán Martínez** (fed president 1988–89; also 1980–82). ⚠️ Bascuñán name is
  Grokipedia-sourced — hedge or attribute loosely; the founding facts are on
  [consur.org / Sudamérica Rugby](https://www.consur.org/index_php/institucional/).
- Renamed **Sudamérica Rugby, 2015**.

### National-team results 1972–1989
- Broadly **2nd or 3rd** in the Sudamericano (Argentina always 1st; Uruguay now rising to contest 2nd
  — the rivalry the old chapter mis-dated to the 1950s is really turning HERE, in the 70s–80s).
- **1989 Sudamericano (Uruguay, 7–14 Oct), 5 teams; Argentina won; Argentina 47–9 Chile (10 Oct).**
  ⚠️ WIKI/Grokipedia — hedge.
- **Francisco Planella** is the era's nameable spine (see above).

### Honest gaps (do not invent)
Exact placings year-by-year; a firm second-vs-third trend line; the Estadio Nacional↔rugby question
(genuinely no source — do NOT imply a connection the old chapter was right to avoid); Bascuñán detail.

## Gen 3 — verified facts (fact-checked 2026-07-15)

- **Old Christians Club founded 1962** (alumni of Stella Maris College, Christian Brothers, Carrasco).
  ✓ correct.
- **Flight 571 itinerary CORRECTED.** The team did **not** play matches in Argentina. Departed
  Montevideo (Carrasco) 12 Oct 1972 → storm forced an overnight stop in **Mendoza** → took off again
  and crashed 13 Oct 1972 en route to **Santiago**, where they were to play **Old Boys Club** (an
  English club; a return visit — Old Christians had toured Chile in 1971). Chapter previously said
  "already played several matches in Argentina" (wrong, and contradicted the Uruguay chapter).
- **45 aboard (40 passengers + 5 crew); 16 survivors, 72 days.** ✓ Parrado & Canessa's ~10-day trek;
  Chilean huaso (Sergio Catalán) raised the alarm. *Alive* (Piers Paul Read) pub. 1974. ✓
- **1980s "400%" participation boom:** ✅ VERIFIED verbatim — "During the 1980s, Chilean rugby
  participation increased by 400%, and whereas it was previously confined to the cities of Santiago
  and Valparaíso, it began to spread throughout the country" (Wikipedia, Rugby union in Chile).
- **CONSUR founded 14 October 1988** in Asunción (Argentina, Brazil, Chile, Paraguay, Uruguay),
  ratified by member unions at Punta del Este Jan 1989. Chapter said "1989" — CORRECTED to Oct 1988
  (ratified Jan 1989); "two years later → 1991" changed to "three years later."
- **Chile full IRB member 1991** ✓ (chapter says November 1991; year confirmed, month not
  independently checked). Called "IRB" not "World Rugby" for the 1991 period (matches Uruguay ch).
- **World Cup absence count CORRECTED nine → EIGHT.** 1991–2019 = eight tournaments Chile did not
  reach (debut 2023). "Nine" appeared 6× across Gen 3–5; all changed to eight for consistency with
  the chapter's own 1991–2019 list. (Nb: nine editions total 1987–2019 if you count the invitational
  1987, but the chapter's framing is the 1991-membership era = eight.)

## GEN 4 REWRITE BRIEF (1990–2017) — named-source retrieval, 2026-07-20

**Headline: two of the old chapter's most-repeated Lemoine quotes CANNOT be sourced and must be
dropped.** This is a feature, not a loss — they were the lines repeated 3× that the redesign wanted
gone.

### ⚠️ SOURCING PROBLEM — the "tormentor" quotes
- **"Uruguay always needed to beat Chile to advance… it was either them or us"** — attributed to
  Lemoine throughout the old chapter (repeated **3×**). **NOT FOUND** in the RugbyPass interview it was
  pinned to, nor by targeted search. **Do NOT quote as Lemoine's words.**
- **"lost to Chile only three times in a 25-year career (2002 player / 2011 assistant / 2015)"** —
  **UNVERIFIED**, and partly contradicted: under Lemoine as Uruguay coach, Uruguay beat Chile **23–9
  (2013)** and **55–13 (2014)**, and lost **30–15 (2015)**. The lifetime "three losses" tally is
  plausible for the whole 1995–2015 span but has no located source. **Drop the specific count.**
- **"sleeping giant"** — associated with the 2018 Lemoine hire (World Rugby framing) but **not
  verbatim-sourceable to Lemoine** in accessible text. Do not place in quotation marks as his words.
  → Reconsider for Gen 6 (old chapter used it as the Gen 6 title); if kept, frame as the phrase used
  *about* Chile, not a Lemoine quote.
- **VERBATIM-CONFIRMED Lemoine quote (RugbyPass, "South America is the best region"):** professionalism
  as upheaval — *"There's a big social change in their lives. They have to make changes to their work,
  school, family, and leisure agendas to adapt to the needs of the national team."* ✓ USE THIS ONCE
  (fits Gen 4 arrival or Gen 5).
- **NEW FRAME for the gatekeeper story:** carry it on the STRUCTURAL facts, which are solid — eight
  straight World Cups missed; the South American pathway repeatedly resolving into a Chile–Uruguay
  decider that **Uruguay won** (2007: Uruguay 43–15 Chile, Montevideo). No invented quote needed.

### VERBATIM PLAYER QUOTES — confirmed, use ONCE each
- **Martín Sigren** (debut v South Korea, **13 Nov 2016**, as replacement for captain Benjamín Soto;
  captain from 2020): *"The national team was treated like an amateur club. We would train twice a
  week, for a couple of months before a tournament."* — [RugbyPass](https://www.rugbypass.com/news/chile-and-martin-sigren-are-already-dreaming-of-making-rugby-world-cup-history/)
  Also (Rugby World): *"…lots of moments when it really felt uphill, where we kept receiving nothing
  in return."*
- **Matías Garafulic:** *"trained on dirt courts until the World Cup"*; *"there were days when we
  simply could not train because the field was too hard, and many players suffered injuries due to
  overload."* — [Sports Gazette](https://sportsgazette.co.uk/the-revolutionary-rise-of-chilean-rugby-from-adversity-to-the-world-stage/)
- **Ignacio Silva** (veteran flanker): *"Pablo changed Chilean rugby, how we see things, our vision,
  our ambition, and we embraced high performance. He worked on the players' commitment; those who
  joined the training programme were those who really wanted to be there."* — [Rugby World](https://www.rugbyworld.com/tournaments/rugby-world-cup/the-rise-of-rugby-in-chile-144308)

### The wilderness — facts
- **Eight straight RWCs missed: 1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019** (debut 2023). Rugby
  World confirms Chile's absence list (non-wiki). 2007 pathway: **Uruguay 43–15 Chile, Montevideo.** ✓
- **2015 Sudamericano "A" — Chile's ONLY title:** beat Brazil and Paraguay, then **Uruguay 30–15 at
  Parque Mahuida, Santiago** — 3–0. Argentina had left for the Rugby Championship (2012). Captain
  **Benjamín Soto** (Stade Français); **Juan Pablo Perrotta** among the try-scorers; **José Ignacio
  Larenas** in the centres. [Americas Rugby News full-match](https://www.americasrugbynews.com/2020/03/22/full-match-chile-vs-uruguay-2015/)
  → gives the "one bright day" real Chilean names for the first time.
- **2016 ARC:** beat **Brazil 25–22** (Feb 2016), then **19 consecutive ARC defeats** (2016–2019).
  2017: lost all five (Brazil 3–17, Canada 15–36, Argentina XV 10–45, USA 9–57, Uruguay 14–45).
  [2017 ARC preview](https://www.americasrugbynews.com/2017/01/31/2017-arc-preview-chile/) — Americas Rugby News
- **José Ignacio Larenas:** **first Chilean to reach 50 caps** — now NON-WIKI CONFIRMED by
  [Americas Rugby News (28 Sep 2023)](https://www.americasrugbynews.com/2023/09/28/jose-ignacio-larenas-becomes-first-player-to-50-caps-for-chile/). Debut **2012 v Portugal**. Record try-scorer
  (~11) — keep "record try-scorer" without asserting the exact number.

### The 2018 hire
- **31 August 2018:** Chile appoint **Pablo Lemoine** (Uruguayan), replacing NZ coach **Mark Cross**.
  [Americas Rugby News](https://www.americasrugbynews.com/2018/08/31/chile-name-pablo-lemoine-as-new-head-coach/)
- **The federation was broke; the Chilean Olympic Committee secured emergency funding to hire him.**
  (Rugby World) — good, previously-unused detail.
- **6 a.m. training:** two-hour early-morning sessions (weights + field) *before* players' regular work,
  to fit around jobs and university. (Rugby World) ✓
- **No professional players at all** in 2016; squad gradually filtered to the committed. ✓
- ⚠️ **CUT the old chapter's Grizz Wyllie / Van Heerden "same revolution, different continent" refrain**
  (appears twice). It is cross-chapter cleverness that reads as authorial editorialising and belongs
  to the messiah-reflex trap the redesign warns against. One clean cross-reference at most.

### The Campbell bridge (from Gen 2 brief)
Ian Campbell — the father of modern Chilean rugby — was still alive through all of this, dying **11 Nov
2022**. Do not spend him here; he pays off in Gen 5/6 (lived to see qualification).

## Gen 4 — verified facts (fact-checked 2026-07-15)

- **Chile's ONLY South American Championship (union) title = 2015**, NOT 1995. (Wikipedia champions
  list: "Chile 1 title — 2015"; Argentina won 1995.) In 2015 Chile beat Brazil & Paraguay and beat
  **Uruguay 30–15** at home. By 2015 Argentina (senior) had left for the Rugby Championship (2012),
  so the "championship of everyone-except-Argentina" framing is TRUE for 2015 — it was just mis-dated
  to 1995 (where it's false). Chapter's "one bright day" REWRITTEN 1995 → 2015.
- **"CONSUR Cup in 2009 and 2012" — dropped.** That development competition wasn't launched until
  2014; Chile's around-then honours were divisional/phase wins. Removed the shaky claim.
- **Pablo Lemoine born 1 March 1975; joined Bristol 1998 aged ~23**, first Uruguayan pro. "Bristol at
  nineteen" was WRONG — fixed in THREE chapters: Chile Gen 4, Uruguay (line ~265), Georgia (line
  ~668). All now omit the age.
- **England 111–13 Uruguay (Brisbane, 2 Nov 2003):** Lemoine scored Uruguay's only try (Menchaca
  2 pen + conv). ✓ "Only two tries England conceded in the entire pool" = CONFIRMED (Samoa's Semo
  Sititi + Lemoine; Georgia and South Africa scored none). ✓
- **ARC 2016:** Chile beat **Brazil 25–22** (6 Feb 2016, home) then **19 consecutive tournament
  losses**. ✓ Six-team 2016 ARC = Argentina XV, USA, Canada, Brazil, Uruguay, Chile. ✓
- Sigren 2016 debut / "amateur club" quote; Garafulic "dirt courts"; 2018 Lemoine hire; Nov 2019
  Selknam — all consistent with earlier passes.

### ✅ GEN 6 2024 ISSUE — RESOLVED (was a rugby-league/union conflation)
- The "**2024 South American Championship, lose to Argentina 32–30, win on points**" was a **RUGBY
  LEAGUE** result: 2024 South American Rugby LEAGUE Championship (3 teams) — Chile 44–22 Brazil,
  Argentina 32–30 Chile, Chile won on points difference. NOT rugby union.
- Chile has **one** union South American title (2015). The union champs list doesn't credit a 2024
  title; the 2024 union Sudamericano was disrupted; in the 2025 union final **Uruguay beat Chile
  46–35** (agg). So Gen 6's "2024 title / second or third ever" was FALSE.
- REWROTE Gen 6 "The results" on the real facts:
  - **Chile 31–12 Samoa, 27 Sep 2025, Estadio Sausalito, Viña del Mar** (~20k crowd) → **qualified for
    RWC 2027**; first leg Salt Lake City **32–32**. First-ever win over Samoa / any major Pacific side.
    Sigren watched injured. Second consecutive World Cup (after 2023 debut).
  - **Ranking: record 17th in Nov 2025** (climbed 4 places in 2025); ~18th in 2026. Changed "gone past
    Uruguay / ahead" → "drawn level with Uruguay" (Uruguay won the 2025 union final, so "ahead" was
    too strong).
  - Also fixed a leftover here: "1936, Santiago, Argentina 20 Chile 0" → "1936, Valparaíso, 29–0."

## GEN 5 REWRITE BRIEF (2018–2023) — named-source retrieval, 2026-07-20

**Headline: the Selk'nam naming has a living objection the old chapter erased, and the winning penalty
now has a name (Videla).**

### ⭐ THE SELK'NAM NAMING — hold BOTH halves (the old chapter only held one)
- Selknam founded **Nov 2019**, Chile's team in the World-Rugby-backed **Súper Liga Americana de Rugby
  (SLAR)**. Named for the **Selk'nam (Ona)** of Tierra del Fuego; crest = a **hooded Hain-ceremony
  spirit figure** with body-paint patterns; Umbro kit (2021–22) carried the ceremonial graphics.
- **THE CORRECTION:** the old chapter calls the Selk'nam "a genocided indigenous people… hunted to
  near-extinction" and treats the naming as uncomplicated homage ("a sport announcing it intends to
  belong to Chile"). But **the Selk'nam are NOT gone** — descendants organised as the **Corporación
  Selk'nam** publicly objected to the team, and the erasure of that living objection is itself part of
  the problem.
- **What they objected to** (Chile Today; corroborated by search): the club's slogan **"Vamos Selk'nam,
  la cacería no ha terminado" — "the hunt is not over yet"** — which echoes the literal bounty-**hunts**
  by which settlers destroyed the Selk'nam. **Corporación Selk'nam, verbatim:** *"We responded and
  expressed our feelings over the use of the name of our people and our discontent with how they were
  teaching our culture, making it clear that we did not approve of their actions. After that, there was
  silence, so we decided to make our discontent public."* They distinguish inspiration-with-consultation
  (which they welcome) from someone who *"tries to speak for us and commercializes it"* without asking.
- **Club response:** initially promised dialogue; reportedly did not substantively follow through. **No
  mainstream rugby/Chilean sports source grapples with the discomfort** — only the *Chile Today*
  investigative piece names it. World Rugby/SLAR framed the name only as "honouring resilience."
- **HOW TO WRITE IT (Latham model, do not resolve):** the gesture's real power (a settler-state's first
  pro team putting a Selk'nam Hain spirit on its chest, after a century of English school-names) AND the
  living Selk'nam saying *you did not ask us, and your "hunt" slogan is our genocide* — both true, held
  together, unresolved. Correct the "extinct/near-extinct" framing explicitly: **the point is that they
  survived to object.**
- Source: [What's Behind the Selk'nam's Struggle Against a Rugby Team?](https://chiletoday.cl/whats-behind-the-selknams-struggle-against-a-rugby-team/) — Chile Today (site was DNS-unreachable on 2026-07-20; the quote is corroborated via search snippet — attribute as "Chile Today reported" and hedge if the URL stays dead at final check).

### SLAR opener & Selknam progression — CONFIRMED
- **4 Mar 2020, Estadio Charrúa, Montevideo: Selknam 15–13 Peñarol**, AWAY — first-ever SLAR match;
  **five penalties by fly-half Santiago Videla**; coach **Pablo Lemoine** (running franchise + national
  team). [Sudamérica Rugby](https://www.sudamerica.rugby/english/exitoso-comienzo-de-slar-con-triunfo-de-selknam-3?nid=345)
- **2020** cut short by COVID after the opener. **2021** semi-finalists under **Nicolás Bruzzone**
  (ex-Argentina Sevens, promoted from assistant); lost SF to Peñarol 17–14. **2022** beat **Jaguares XV**
  (Argentine franchise) in the regular season and the semi (20 May), reached the **SLAR final, 27 May
  2022, Estadio Charrúa — lost to Peñarol 24–13.** **2023** squad became **all-Chilean** to prep for RWC.
  [Bruzzone hire](https://www.americasrugbynews.com/2021/01/07/nicolas-bruzzone-becomes-head-coach-of-selknam/) · [2022 final](https://www.americasrugbynews.com/2022/05/27/penarol-defeat-selknam-for-slar-2022-glory/)

### Qualifiers — CONFIRMED non-wiki
- **Canada repechage, Oct 2021, first-ever win over Canada at the 8th attempt.** Leg 1 **2 Oct 2021,
  Starlight Stadium, Langford BC: Canada 22–21** (last-min Rob Povey penalty). Leg 2 **9 Oct 2021,
  Estadio Elías Figueroa, Valparaíso: Chile 33–24.** **Aggregate 54–46.** Knocked Canada out of a World
  Cup for the first time ever (1987–2019 ever-present). [Rugby Canada](https://rugby.ca/en/news/2021/10/canada-fall-to-chile-to-miss-out-on-rugby-world-cup-2023-qualification) · [CBC](https://www.cbc.ca/sports/rugby/canada-world-cup-qualifiers-1.6206498)
- **USA play-off, July 2022.** Leg 1 **9 Jul 2022, Estadio Santa Laura, Santiago: USA 22–21 Chile**
  (~10,000, rain, ~5°C, a second-half power cut). Leg 2 **16 Jul 2022, Infinity Park, Glendale,
  Colorado: Chile 31–29 USA. ⭐ WINNING PENALTY, 75th minute, SANTIAGO VIDELA.** **Aggregate 52–51.**
  Chile's first-ever World Cup qualification. [World Rugby recap](https://www.world.rugby/news/733127/rugby-world-cup-2023-americas-2-play-off-recap) · [Americas Rugby News](https://www.americasrugbynews.com/2022/07/16/chile-shock-usa-to-quality-for-rugby-world-cup-2023/)
- → **Videla is the human thread**: 5 penalties in the SLAR opener (Mar 2020) → the 75th-min qualifier
  winner (Jul 2022). Name him both times.

### RWC 2023, Pool D — CONFIRMED
- Losses: **Japan 42–12, Samoa 43–10, England 71–0, Argentina 59–5.** Fifth in the pool.
- **Rodrigo Fernández scored Chile's first-ever RWC try, 6th min v Japan** (Toulouse, 8 Sep 2023). ✓
- **Captain Martín Sigren** (blindside; had played Doncaster Knights in the English Championship 2022–23).
  **José Ignacio Larenas reached his 50th cap during the tournament (v Argentina).** **~30 of the 33-man
  squad from Selknam.** [RWC review](https://www.rugbyworldcup.com/2023/news/873872/rwc-2023-review-chile)

### ⭐ THE CAMPBELL PAYOFF (set up in Gen 2)
- **Ian Campbell** — "father of modern Chilean rugby," the 1948–1961 centre — **died 11 November 2022,
  aged 94.** That is **four months after** the Colorado penalty (16 Jul 2022) sent Chile to their first
  World Cup, and about **ten months before** they played in it (Sep 2023). **He lived to see them
  qualify; he did not live to see them play.** Photographed with the Webb Ellis Cup in Santiago, aged
  91, on the 2019 Trophy Tour.
- Sources: [La Tercera obituary](https://www.latercera.com/el-deportivo/noticia/el-rugby-chileno-pierde-a-su-mayor-leyenda-de-la-historia-ian-campbell-fallece-a-los-94-anos/) · [24 Horas](https://www.24horas.cl/deportes/mas-deportes/fallecio-ian-campbell-maclean-maximo-referente-del-rugby-chileno)
- → **Close Gen 5 on Campbell.** He debuted in the 1948 first win and never missed a cap to 1961; he
  died having watched the country qualify at last. Bracket the chapter with him.

### DE-DUP DISCIPLINE
- **Do NOT re-quote** Sigren "amateur club / twice a week" or Garafulic "dirt courts" (both spent in
  Gen 4). Reference the transformation, don't re-run the lines.
- **Videla** and **the SLAR opener** were the old Gen 5 cold open; keeping the opener but the CHAPTER
  cold open moves to the Colorado penalty (climax-first), pulling back to the founding.

## Gen 5 — verified facts (fact-checked 2026-07-15)

- **SLAR opener venue was MONTEVIDEO, not Santiago.** 4 Mar 2020, **Estadio Charrúa, Montevideo**;
  Selknam beat Peñarol **15–13 AWAY** (5 penalties, Santiago Videla) — the first pro match in SLAR
  history. Cold open corrected (Santiago → Montevideo; noted the away win).
- **Canada repechage = OCTOBER 2021**, not after the May-2022 SLAR final. Leg 1 **2 Oct 2021**
  Langford (Canada 22–21); Leg 2 **9 Oct 2021** Estadio Elías Figueroa, Valparaíso (Chile 33–24);
  agg **54–46**; first win over Canada at the 8th attempt. Chronology fixed (Canada 2021 flashback →
  USA July 2022 = the "six weeks after the final" decider).
- **USA playoff:** Leg 1 **9 Jul 2022** Santa Laura, Santiago (Chile 21–22); Leg 2 **16 Jul 2022**
  **Glendale, Colorado** (Chile 31–29); agg **52–51**; 75th-min penalty. Venue Glendale confirmed
  (dropped the San Antonio / 32–29 hedge; 31–29 is forced by the aggregate).
- **2023 RWC Pool D scores all CONFIRMED:** Japan 42–12, Samoa 43–10, England 71–0 (Arundell 5
  tries), Argentina 59–5 (8 tries).
- **Rodrigo Fernández** scored Chile's first RWC try — 6 min vs Japan, briefly ahead. ✓
- **José Ignacio Larenas:** verified as Chile's **most-capped player & record try-scorer** (debut
  2012). "Fly-half / first to 50 caps" NOT verified — replaced with the verified description.
- Selknam supplied 30 of the 33-man 2023 squad; Peñarol won SLAR/SRA 3× (2021, 2023, 2025). ✓
- Unverified but left (low-risk): first-squad names (Vesi Rarawa/Johnny Ika/Latiume Fosita),
  Nicolás Bruzzone as former Argentina international coach.

## Sources

- [2023 Rugby World Cup – Americas qualification (Canada Oct 2021, USA Jul 2022 dates)](https://en.wikipedia.org/wiki/2023_Rugby_World_Cup_%E2%80%93_Americas_qualification) — Wikipedia
- [2023 Rugby World Cup Pool D (all four Chile scores)](https://en.wikipedia.org/wiki/2023_Rugby_World_Cup_Pool_D) — Wikipedia
- [Exitoso comienzo de SLAR con triunfo de Selknam (Charrúa, Montevideo, 15–13 away)](https://www.sudamerica.rugby/english/exitoso-comienzo-de-slar-con-triunfo-de-selknam-3?nid=345) — Sudamérica Rugby
- [Chile shock USA to qualify for RWC 2023 (16 Jul 2022, Glendale)](https://www.americasrugbynews.com/2022/07/16/chile-shock-usa-to-quality-for-rugby-world-cup-2023/) — Americas Rugby News
- [South American Rugby Championship — champions list (Chile: 1 title, 2015)](https://en.wikipedia.org/wiki/South_American_Rugby_Championship) — Wikipedia
- [Pablo Lemoine (b. 1 Mar 1975; Bristol 1998)](https://en.wikipedia.org/wiki/Pablo_Lemoine) — Wikipedia
- [2016 Americas Rugby Championship (Chile 25–22 Brazil; 19-loss streak)](https://en.wikipedia.org/wiki/2016_Americas_Rugby_Championship) — Wikipedia
- [2003 Rugby World Cup Pool C (England tries conceded)](https://en.wikipedia.org/wiki/2003_Rugby_World_Cup_Pool_C) — Wikipedia
- [Old Christians Club](https://en.wikipedia.org/wiki/Old_Christians_Club) — Wikipedia
- [Uruguayan Air Force Flight 571 (itinerary: Montevideo → Mendoza → Santiago)](https://en.wikipedia.org/wiki/Uruguayan_Air_Force_Flight_571) — Wikipedia
- [CONSUR / Sudamérica Rugby (founded 14 Oct 1988)](https://en.wikipedia.org/wiki/CONSUR) — Wikipedia
- [Rugby union in Chile (400% 1980s boom; 1991 IRB membership)](https://en.wikipedia.org/wiki/Rugby_union_in_Chile) — Wikipedia
- [Sudamericano de Rugby 1951 — standings & results](https://es.wikipedia.org/wiki/Sudamericano_de_Rugby_1951) — Wikipedia ES
- [El Panamericano de 1951 — Sudamérica Rugby](https://www.sudamerica.rugby/english/el-panamericano-de-1951-3?nid=363)
- [1952 Ireland rugby union tour of South America](https://en.wikipedia.org/wiki/1952_Ireland_rugby_union_tour_of_South_America) — Wikipedia
- [1954 France rugby union tour of Argentina and Chile](https://en.wikipedia.org/wiki/1954_France_rugby_union_tour_of_Argentina_and_Chile) — Wikipedia
- [Anexo:Partidos de la selección de rugby de Chile (full match list)](https://es.wikipedia.org/wiki/Anexo:Partidos_de_la_selecci%C3%B3n_de_rugby_de_Chile) — Wikipedia ES
- [Selección de rugby de Chile — early history (1936 Valparaíso, 1938, 1948)](https://es.wikipedia.org/wiki/Selecci%C3%B3n_de_rugby_de_Chile) — Wikipedia ES
- [Chile y Uruguay: más de 80 años de rivalidad (1948 first meeting) — Rugby Chile](https://www.rugbychile.cl/2025/08/28/mas-de-80-anos-de-historia-y-una-rivalidad-escrita-en-la-cancha-chile-y-uruguay-mas-que-un-partido/)
- [Everton cumple 116 años (founded 24 June 1909) — Campeonato Chileno](https://www.campeonatochileno.cl/aniversario/mas-de-un-siglo-de-pasion-ruletera-everton-cumple-116-anos/)
- [Everton: origen del nombre y sus colores — Asifuch](https://asifuch.cl/everton-origen-del-nombre-y-sus-colores/)
- [Se reescribe la historia del origen del rugby chileno (Coronel–Concepción, 16 June 1892) — Rugby Chile](https://www.rugbychile.cl/2020/05/05/en-la-semana-del-rugby-chileno-se-reescribe-la-historia-de-su-origen/)
- [¿Cuándo se jugó por primera vez el rugby en Chile? — Sudamérica Rugby](https://www.sudamerica.rugby/english/cuando-se-jugo-por-primera-vez-el-rugby-en-chile-3?nid=404)
- [The Grange School history — Anglo-Chilean Society](https://www.anglochileansociety.org/single-post/the-grange-school)
- [The Mackay School — historia (1857)](https://www.mackay.cl/historia/)
- Craighouse founded 1959 — Colegio Craighouse (school history)
- Santiago Wanderers founded 15 Aug 1892 — club history

## GEN 6 REWRITE BRIEF (2023–2026) — named-source retrieval, 2026-07-20

**Cutoff = 19 July 2026.** **Retitle the generation** (old title "The Sleeping Giant" rested on an
unsourceable Lemoine quote). Proposed: **"The House on the Hill (2023–2026)"** — the CARR at Parque
Mahuida, La Reina, the first real home the sport ever had. **CUT the old thesis-first ending**
("Institutions make the class. Not the founders. Chile just proved it faster than anyone").

### ⭐ THE FALSIFIED ENDING — FIXED
Old chapter ended on Chile "hunting that scalp" v Georgia "in La Serena on 18 July." **Played 18 July
2026; Georgia won 49–22.** Venue **moved from La Serena to the CARR, Parque Mahuida, La Reina** under a
red-alert storm. → **The venue is the irony**: their heaviest recent defeat happened in the very
high-performance home this generation celebrates. Chile tries: Manuel Bustamante, Santiago Videla;
28–15 Georgia at half-time. [World Rugby venue statement](https://www.world.rugby/nations-cup/en/news/1045662/statement-on-the-nations-cup-match-between-chile-and-georgia)

### RWC 2027 qualification — the FULL sequence (both halves)
The old chapter's "drawn level with Uruguay" is too rosy — **Uruguay beat Chile again for the DIRECT
spot; Chile took the hard road via the repechage.** Both must be told:
- **Direct South American qualifier, Sept 2025: URUGUAY beat CHILE 46–37 on aggregate** (first leg
  Uruguay 28–16 in Santiago). Uruguay took the automatic RWC 2027 place. **The tormentor relationship
  persists into the present** — do not claim Chile has drawn level on the field.
  [Americas Rugby News](https://www.americasrugbynews.com/2025/09/06/uruguay-successfully-qualify-for-rugby-world-cup-2027/)
- **South America/Pacific repechage: Chile qualified anyway.** Leg 1 **32–32** (20 Sep 2025, Salt Lake
  City). Leg 2 **Chile 31–12 Samoa, 27 Sep 2025, Estadio Sausalito, Viña del Mar, crowd 21,754** —
  **Chile's first-ever win over Samoa / any major Pacific Island nation.** Tries Benjamín Videla, Iñaki
  Ayarza, Nicolás Saab; **Santiago Videla 16 pts.** **Sigren injured, watched from the sideline.**
  Second straight World Cup. [Sublime Chile write history](https://www.americasrugbynews.com/2025/09/27/sublime-chile-write-history-by-beating-samoa-in-rwc-qualifier/) · [Chile the 23rd team to qualify for RWC 2027](https://www.world.rugby/news/1016675/chile-become-the-23rd-team-to-qualify-for-mens-rugby-world-cup-2027)

### Rankings — CORRECTED
- **Chile: a record-high 16th** by mid-July 2026 (up from 17th, Sept 2025). **Georgia: 13th.** → **three
  places apart, NOT five** (old chapter said "five places behind Georgia" — fix to three). Rugby Chile
  announced the record on 20 July 2026.
  [Rugby Chile — nuevo récord en el ranking](https://www.rugbychile.cl/2026/07/20/chile-vuelve-a-hacer-historia-y-alcanza-un-nuevo-record-en-el-ranking-mundial-de-world-rugby/)

### The 2026 Nations Cup (inaugural; July + November windows)
- **Format:** 12 teams, two pools, 3 matches each July (Americas) + 3 November (Europe/Asia).
- **Chile 48–31 Romania** — 4 Jul 2026, **Estadio Nacional, Santiago.**
- **Chile 38–17 Hong Kong China** — 11 Jul 2026, **Estadio Sausalito, Viña del Mar.**
- **Georgia 49–22 Chile** — 18 Jul 2026, CARR, La Reina (moved from La Serena; storm).
- **November European leg upcoming** (note as forward-looking, no results).
- Uruguay in the same competition (hosting the same visitors at the Charrúa — per earlier pass, lost to
  Georgia 34–41 on 4 Jul; drew Romania 36–36 on 11 Jul). Keep the Uruguay parallel light.
- [Chile v Romania report](https://www.americasrugbynews.com/2026/07/04/chile-celebrate-solid-victory-over-romania/) · [Nations Cup official](https://www.world.rugby/nations-cup/en)

### Lemoine honorary-citizenship bill — the cold open
- **Proposed 21 April 2026** by deputies led by **Pier Karlezi** (Libertarian Party); sent to the
  Nationality/Interior commission; **still in committee, unvoted, as of July 2026.** *Nacionalidad por
  gracia.* Cites Lemoine taking Chile to two straight World Cups (2023, 2027).
- **Lemoine, verbatim (BioBioChile):** *"I want to give enormous thanks because truly making me part of
  your culture, your people, granting me a citizenship, being really part of a country I already feel as
  my own… hopefully it happens."*
- [La Tercera](https://www.latercera.com/el-deportivo/noticia/el-head-coach-de-los-condores-puede-ser-chileno-diputados-piden-nacionalizar-por-gracia-a-pablo-lemoine/) · [BioBioChile](https://www.biobiochile.cl/noticias/deportes/mas-deportes/2026/04/23/la-emocion-de-pablo-lemoine-tras-propuesta-de-nacionalizacion-por-gracia-propuesta-ingreso-a-congreso.shtml)

### The CARR (the house)
- **Parque Mahuida, La Reina.** Rebuilt as **"CARR 2.0" in 2023**; **remodel inaugurated 8 July 2026**
  ahead of the **World Rugby Challenger Cup M20 (Santiago, Oct 2026)** — Santiago is hosting a World
  Rugby U20-tier tournament. Artificial turf, floodlights, a stand; Santiago municipality invested
  (~$1.5 bn pesos). First purpose-built home in the sport's ~130-year Chilean history.
  [Rugby Chile — CARR remodel](https://www.rugbychile.cl/2026/07/08/chile-rugby-inaugura-las-obras-de-remodelacion-del-centro-de-alto-rendimiento-de-rugby-de-cara-al-world-rugby-challenger-cup-m20-santiago-2026/)

### Second franchise, players, Sigren, 2035
- **Second Chilean Super Rugby Americas team expected from 2027** (speculated **Concepción** — fitting,
  given Los Troncos/Old John's history there). Not yet named. ~50–70 pros (ballpark, hedge).
  [ARN](https://www.americasrugbynews.com/2025/09/30/second-chilean-pro-team-could-enter-super-rugby-americas-2027/)
- **Sigren:** now at the **New England Free Jacks (USA)**; recovered from the knee injury, captain again
  by mid-2026; b. 14 May 1996 (age 30).
- **RWC 2035:** **Argentina-led South American bid** (Sudamérica Rugby — Brazil, Chile, Uruguay in it),
  **Agustín Pichot** driving it; **Spain also bidding.** Host chosen ~2027. → closing forward-look.
- ⚠️ **"sleeping giant"** and **"make rugby the #2 sport in Chile"** — still **UNVERIFIED as Lemoine
  quotes.** Do NOT quote. Convey growth ambition without fragile attribution. Same for the old
  chapter's Sigren "kids wearing Selknam/Chile jerseys instead of the All Blacks" — nice but unverified
  this pass; make the observation generically or drop.

## Gen 6 — verified facts (fact-checked 2026-07-15)

- **Lemoine honorary-citizenship bill — CONFIRMED.** A cross-party bill (led by Pier Karlezi, PNL)
  for *nacionalidad por gracia* for Lemoine entered the Chilean Congress ~21–23 April 2026, sent to
  the Nationality/Interior Commission; Lemoine responded emotionally on video. Chapter cold open now
  dated "April 2026." Cites his role in qualifying Chile for two straight World Cups (2023, 2027).
- **CARR:** at **Parque Mahuida, La Reina**. The "**CARR 2.0 / nueva casa del rugby chileno**"
  (synthetic pitch, "piedra angular del desarrollo") dates to **2023**; a further remodel was
  inaugurated **8 July 2026** ahead of the World Rugby U20 tournament (Challenger Cup M20) in
  Santiago. Chapter reframed "opens" → "rebuilt … new home" + Parque Mahuida + the 2026 upgrade.
  REMOVED unverified specifics ("2,900 capacity", "Selknam's home ground since 2025") → "a permanent
  stand."
- **2026 World Rugby Nations Cup — CONFIRMED real & inaugural (July + November 2026).** Pool A
  (Americas/Pacific): Canada, Chile, Samoa, Tonga, Uruguay, USA. Pool B (Europe/Asia/Africa): Georgia,
  Hong Kong China, Portugal, Romania, Spain, Zimbabwe. Cross-pool round robin; opener 4 Jul Montevideo
  (Uruguay v Georgia); July window in the Americas (incl. Santiago), November in Europe/Asia.
- Ranking: Chile peaked **17th (Nov 2025)**, ~18th in 2026.

### ✅ GEN 6 Nations Cup — VERIFIED (2026-07-16)
- Chile's July-2026 home fixtures CONFIRMED (opponents were right): **Chile 48–31 Romania** (4 Jul,
  Santiago), **Chile 38–17 Hong Kong** (11 Jul, Viña del Mar), **Chile v Georgia** (18 Jul, La
  Serena — upcoming as of the book's 16 Jul cutoff). So Chile hosts the trio across THREE cities, not
  just Santiago — chapter corrected ("to Santiago" → Santiago/Viña del Mar/La Serena) and the two
  results added. Uruguay hosts the same three at the Charrúa (lost to Georgia 34–41 on 4 Jul; 36–36 v
  Romania 11 Jul; Hong Kong 18 Jul). "Five places behind Georgia" left as-is (plausible; not
  precisely re-checked).

### Club-name corrections (Gen 0 & Gen 2) — user catches, 2026-07-16
- **Stade Français (Santiago) is FRENCH, not British.** Founded 14 Jul 1929 (Bastille Day) by merging
  two French-colony clubs (Lawn Tenis Francés 1917 + Sport Français); rugby from 1930. Was wrongly
  cited as "British influence" in Gen 0.
- **Sporting (Viña del Mar) is a Catholic-University side, not a British-school club.** Founded **1963**
  by architecture students of the Pontificia Universidad Católica de Valparaíso. English name comes
  from the British-founded Valparaíso Sporting Club venue, but the rugby club is Chilean-university.
- **The clean British-school old-boys clubs** (kept in Gen 0's British-stamp line): **Old Boys**,
  **Old Mackayans** (Mackay School OB assoc., 1956), **Old John's** (Saint John's School, Concepción,
  1991). Gen 0 rewritten; Stade Français/Sporting reframed as French-colony & university exceptions.
- Gen 2 usage left (its claim is only "not one of those names is in Spanish" — true; intro softened
  from "the whole thing" to "the game's foreign, well-heeled character").
