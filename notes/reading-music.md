# Reading music — Rugby Has No Class

## Selection rules

- Work in book order. Aim for approximately 20 minutes per generation.
- Every selection must be listed on Spotify, with track name, performing artist and a link to the track itself.
- **The one hard rule: no vocals.** Every track is instrumental, in any language, including wordless singing and a choir. A sung line is read, and a reader cannot read two things at once. Everything else below is judgement.
- **First test: the people in the chapter.** Build each set from music that generation's own rugby people knew and liked — their country, their city, their class, their decade; what they sang, played at home and heard on the radio. It need not be the nation's own music: where the story is British or Irish (an enclave, the Christian Brothers), use that, and once the chapter leaves the enclave, go local. Prefer fine playing by serious musicians over karaoke or "relaxing piano" filler. The test is whether a Uruguayan gentleman who loves the game and loves reading would enjoy it. Adopted 22 September 2026, when the concert-music Uruguay sets proved too academic. Argentina was rebuilt on the same basis; Chile still follows the older basis of each nation's concert and salon music.
- **Second test: the mood of what the section tells.** Match the weight of the story. Grief takes grave music; defiance can take fire; a decade of committee work takes something plain. Nothing bright over a disaster — no cheerful music over the Andes crash or over a humiliation, which is disrespectful to the people it happened to — and nothing funereal over a section that is proud or funny. The set may change character inside a generation if the story does.
- **No blanket bans.** Judge a track by the two tests above and by whether it drags a reader off the page — not by its genre, instrument or rhythm. Folk dances, strummed guitar, tango, a band and drums are all allowed where the people and the mood call for them. The flat rule against beat and percussion was dropped on 22 September 2026: it had excluded the zamba, the chacarera and the malambo, the very music of the chapters it was policing. Apart from vocals, what stays out is what genuinely distracts: a hard dance-floor pulse, sudden level jumps, a soloist showing off, and modernism that keeps demanding attention.
- **When the story names a piece of music, play it.** Where a section turns on a song — *Hen Wlad Fy Nhadau* answering the haka at Cardiff Arms Park on 16 December 1905, a hymn on the terraces, a club's own march — that piece belongs in the generation's set, in an instrumental version. See "Pieces earmarked for later chapters" below.
- **Check what a piece carries before using it, in two steps.** First, the quick one: **is the piece in ordinary entertainment use today** — played at concerts and weddings, recorded by working musicians, on the radio? If it is, it is not a regime relic or a museum specimen, and that clears most of what looks alarming from outside. Suliko is sung at Georgian tables, Tsintsadze is concert repertoire, Violeta Parra and Víctor Jara are on Chilean radio daily; none of them needs agonising over. If a piece is *not* in living use, ask why not, because a fallen state's anthem usually isn't.
  Second, the part living use cannot settle: **does the piece belong to people who have not given it, and would someone on the wrong side of its history be jarred to hear it here?** *Die Stem van Suid-Afrika* is still performed and recorded, and would still jar under a South Africa chapter. "Ka Mate" is used in entertainment constantly and is still Ngāti Toa's, with attribution protected in New Zealand law. "Delilah" is a Tom Jones hit the WRU stopped its choirs from playing. Popularity is not permission.
  A reading soundtrack is background, and background cannot explain itself: if a piece needs a paragraph of justification, leave it out; if the chapter is *about* that history and the note can say so in one line, it can stay; where the association is real but contested, say so in the set's text rather than hoping no reader notices. The list under "Music to handle with care" below is the running record; add to it whenever one turns up.
- **Choose by sound before titles.** Within those tests, a track earns its place by what a reader will hear: texture, pace, weight, density. A title that happens to fit the story is a bonus, never the reason. (The September 2026 rebuild removed a dozen tracks that had been picked for their names, including four that were the busiest pieces on their albums.)
- Vary the sound across a chapter. No single instrument family should carry most of a chapter, and a composer should normally have one set per chapter.
- Say whether a set is period repertoire or a later portrait, and give dates where they are known.
- Never reuse a composition anywhere in the book, including another performance, arrangement, cover or remaster. Artists may recur.
- Superseded selections stay reserved against reuse. Check every new selection against the active sets and against the reservation index at the end of this file.
- **Check that every track actually plays, with `python3 tools/spotify_playlists.py check`.** It asks Spotify's embed endpoint, which answers `isPlayable` and `playabilityReason` for each track, and that is the only answer worth trusting. The `restrictions:country:allowed` meta tags on a track page are a trap: plenty of perfectly playable tracks print none at all, so **an empty market list means nothing was printed, not that the track plays everywhere.** Seventeen Georgian tracks were chosen on that misreading in September 2026 and none of them played; the reader found it before the notes did. Where a market list does exist, prefer 180+ markets, and check the chapter's own country is among them.
- Timings refer to the specified recordings; other performances may differ.
- These are listening suggestions, not evidence of music played at the historical events.

**How to build the playlists (September 2026).** Use `tools/spotify_playlists.py`, which reads the track ids straight out of the tables below. Nothing needs to be matched by title, so no recording can be mistaken for another — the Ripa and Falú duplicates that this file keeps warning about cannot happen.

One playlist per chapter, its generations in book order, is the default; `--per set` gives a playlist per generation instead.

- `python3 tools/spotify_playlists.py list` — the playlists and the sets inside them, with track counts and running times. It checks each "Total" line above against the durations in its table, and reports any track used in two sets, which the reuse rule forbids.
- `python3 tools/spotify_playlists.py uris --copy Uruguay` — writes `spotify:track:` lines to `notes/playlist-uris/`, one file per chapter, and puts the named one on the clipboard. Make an empty playlist in the Spotify desktop app, click the track area (not the search box) and press Cmd-V. **This is the route that works.** No account setup, no third-party service, no quota.
- `python3 tools/spotify_playlists.py push --only Uruguay --into <playlist link>` — fills a playlist you made by hand, through Spotify's own Web API, and replaces its contents on later runs so the link keeps working. It needs a free developer app, and it may not work at all: since February 2026 a Development Mode app requires the owner to hold Spotify Premium, and developers report that creating a playlist now answers 403 for unverified apps. Extended Quota Mode, which would lift that, is granted only to organisations with 250,000 monthly users. Treat the API as a convenience that may already be closed; the paste route is the one to rely on.

As of 22 September 2026 that is three playlists: Uruguay (41 tracks, 2:28:14), Argentina (42, 2:48:35) and Chile (44, 2:25:23).

The "Spotlistr input" blocks under each set are kept as a plain reading list and a fallback. Spotlistr itself is no longer the route: it charges tokens for work the ids make unnecessary.

**How sets were checked (September 2026).** Every track, credit and duration below was read from Spotify's own pages on 21 September 2026 (the rebuilt Uruguay and Argentina chapters on 22 September 2026); account playback was not tested. Where Spotify offers a 30-second preview, it was profiled with ffmpeg for loudness range and spectral flux (a rough count of how often the sound jumps in level). Calibration: quiet solo piano scores about 0.5; calm solo guitar 0.65–0.95, because plucked notes read as attacks; candombe drumming 1.1–1.4. **The flux figures quoted below are background, not a gate.** They measure attack density, not calm: a slow zamba on guitar scores like a drum group, while a sweeping orchestral album scores lowest of all, and a 30-second excerpt says little about a 21-minute piece. Used as a threshold on 22 September 2026, the figure quietly removed most of the Argentine folk repertoire; that use was abandoned the same day. Selection is by the two tests at the top of this file. Where a track had no preview, the set says so and relies on published descriptions.

---

## Chapter 1 — Uruguay

Rebuilt on 22 September 2026 around the popular music of the people in each generation, in calm instrumental versions. The sets run:
- Victorian drawing-room pieces and folk songs for the British enclave.
- Edwardian favourites, Remembrance and Gardel for the clubs that organised.
- An Irish air, an O'Carolan lament and the Beatles for the Christian Brothers' schoolboys.
- Uruguay's own songwriters for the mountain generation.
- Jaime Roos for the years Uruguay got on the map.
- Fernando Cabrera's songs, and a Zitarrosa milonga, for the plan's years.
- For today, the songs both banks of the River Plate grew up on.

Every set is instrumental. The earlier concert-music sets (Fabini, Tosar, Cervetti, Santórsola, Storm and others) proved too academic under the page and are archived under "Superseded selections". The candombe sets (Hugo Fattoruso with Barrio Sur) stay archived too, and not because percussion is now allowed elsewhere: candombe drumming was the specific thing that broke the reading in the first place. Uruguay's drums belong in the prose.

### Generation 0: The British Enclave (1842–1900)

Total: **20:39**. The music of a Victorian drawing room, as the British merchants, bankers and railwaymen of Montevideo knew it from home. Mendelssohn's *Songs Without Words* were the piano pieces every Victorian parlour played; the English titles ("Sweet Remembrance", "Consolation", "May Breeze") were added by publishers for that market. Daniel Barenboim's complete recording from the 1970s (Spotify dates it 1974) is quiet and unhurried. Two folk songs of the British Isles on cello frame it: "Blow the Wind Southerly", a Northumbrian song of waiting for a ship, and "Scarborough Fair". These are songs and pieces of the enclave's own time and culture, in modern recordings. The profiles are calm throughout (flux 0.48–0.53).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Blow The Wind Southerly (Arr. Kanneh-Mason for Cello) | Traditional (Northumbrian) | Sheku Kanneh-Mason | 2:22 | [Track](https://open.spotify.com/track/5NHQ6e1JkQ5zsvzIRkqDhh) |
| 2 | Lieder ohne Worte I, Op. 19b: I. Andante con moto "Sweet Remembrance" | Felix Mendelssohn | Daniel Barenboim | 3:08 | [Track](https://open.spotify.com/track/5UXuTmNmSOOERjw0vcWYfy) |
| 3 | Lieder ohne Worte II, Op. 30: III. Adagio non troppo "Consolation" | Felix Mendelssohn | Daniel Barenboim | 2:13 | [Track](https://open.spotify.com/track/6TdPuNGzRtcA4OqrFduiEg) |
| 4 | Scarborough Fair (Arr. Parkin for Cello and Guitar) | Traditional (English) | Sheku Kanneh-Mason, Plínio Fernandes | 3:15 | [Track](https://open.spotify.com/track/4wlNPczIullwvmwb4x0ltz) |
| 5 | Lieder ohne Worte V, Op. 62: I. Andante espressivo "May Breeze" | Felix Mendelssohn | Daniel Barenboim | 2:03 | [Track](https://open.spotify.com/track/6jLpnmzqY0IX3aMEVIMAql) |
| 6 | Lieder ohne Worte III, Op. 38: VI. Andante con moto "Duetto" | Felix Mendelssohn | Daniel Barenboim | 2:17 | [Track](https://open.spotify.com/track/2sSGkbWNsiP70AS3SPpfkJ) |
| 7 | Lieder ohne Worte VII, Op. 85: IV. Andante sostenuto "Elegy" | Felix Mendelssohn | Daniel Barenboim | 2:51 | [Track](https://open.spotify.com/track/4CpvRWwhu1Ei649SAOQZCU) |
| 8 | Lieder ohne Worte VIII, Op. 102: VI. Andante "Belief" | Felix Mendelssohn | Daniel Barenboim | 2:30 | [Track](https://open.spotify.com/track/3Tk9fXZwJaLIYgq4r02UBL) |

Why each track:

- Blow the Wind Southerly — a song of waiting on the shore for a ship: a small British community at the end of a long sea route, and the first organised sport in Montevideo.
- Sweet Remembrance — the parlour at its most typical: expatriates building institutions while looking back across the Atlantic.
- Consolation — slow and plain: a very small membership keeping a club alive through political disruption.
- Scarborough Fair — the old country's own folk tune, on cello and guitar.
- May Breeze and Duetto — two short, even pieces for routine and continuity: the patient work of the club year.
- Elegy — the quietest turn: the land and the wider society beyond the gate, which football would reach first.
- Belief — a steady close without triumph. Rugby survives, but it stays behind the gate as football moves into public life.

Spotify albums: [Mendelssohn: Songs without Words (Barenboim)](https://open.spotify.com/album/6kTJByn4wdXsUtdswvpxUq), [Sheku Kanneh-Mason — Elgar](https://open.spotify.com/album/3PwJLGFcKrecmaRbJQYMSg). The Barenboim tracks play in 169 markets, including Uruguay, the UK and South Africa. The "Venetian Gondola Song", Op. 19b No. 6, is reserved from the first pass and is not used.

Spotlistr input:

```text
Sheku Kanneh-Mason - Blow The Wind Southerly (Arr. Kanneh-Mason for Cello)
Daniel Barenboim - Lieder ohne Worte I, Op. 19b: I. Andante con moto, MWV U86 "Sweet Remembrance"
Daniel Barenboim - Lieder ohne Worte II, Op. 30: III. Adagio non troppo, MWV U104 "Consolation"
Sheku Kanneh-Mason - Scarborough Fair (Arr. Parkin for Cello and Guitar)
Daniel Barenboim - Lieder ohne Worte V, Op. 62: I. Andante espressivo, MWV U185 "May Breeze"
Daniel Barenboim - Lieder ohne Worte III, Op. 38: VI. Andante con moto, MWV U119 "Duetto"
Daniel Barenboim - Lieder ohne Worte VII, Op. 85: IV. Andante sostenuto, MWV U190 "Elegy"
Daniel Barenboim - Lieder ohne Worte VIII, Op. 102: VI. Andante, MWV U172 "Belief"
```

### Generation 1: The Enclave Organizes (1900–1951)

Total: **19:42**. Two worlds that met in Anglo-Uruguayan Montevideo. The British side is Edwardian and between the wars: Elgar's "Salut d'amour", the most popular English salon piece of its day; "Nimrod", the music of British Remembrance after the First World War; and Vaughan Williams's *Fantasia on Greensleeves* (1934). The Río de la Plata side is Carlos Gardel, whom Uruguay claims as a son of Tacuarembó, with two songs from 1935: "Por una cabeza", in the arrangement John Williams wrote for Itzhak Perlman, and "El día que me quieras", played by Daniel Barenboim with Rodolfo Mederos on bandoneón and Héctor Console on bass. "Mi Buenos Aires querido" from the same Barenboim sessions is left out because its tango pulse is too strong (flux 1.15). The others profile calm (0.47–0.65). The Greensleeves recording has the widest swells, so set the volume there.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Salut d'amour, Op. 12 (Arr. Cullen for Cello & Orchestra) | Edward Elgar | Julian Lloyd Webber, Royal Philharmonic Orchestra, James Judd | 3:19 | [Track](https://open.spotify.com/track/1HzbcdmakyZlBh0Oscx3Jg) |
| 2 | Variations on an Original Theme, Op. 36 "Enigma": 9. Nimrod (Arr. Parkin for Cello Ensemble) | Edward Elgar | Sheku Kanneh-Mason and cello ensemble | 4:00 | [Track](https://open.spotify.com/track/5Fjh9jRPL7qqQG7dEtHAOP) |
| 3 | Fantasia on Greensleeves | Ralph Vaughan Williams | Academy of St. Martin in the Fields, Sir Neville Marriner | 4:15 | [Track](https://open.spotify.com/track/1UwDkO3SpbJtmbBkwiEJu6) |
| 4 | Scent of a Woman: Tango (Por Una Cabeza) | Carlos Gardel | Itzhak Perlman, Pittsburgh Symphony Orchestra, John Williams | 3:51 | [Track](https://open.spotify.com/track/3mGkPsZbHEBf8ZT1ExZnww) |
| 5 | Gardel / Arr. Carli: El día que me quieras | Carlos Gardel | Daniel Barenboim, Rodolfo Mederos, Héctor Console | 4:17 | [Track](https://open.spotify.com/track/5leigMI5hG2X8pjv3aSNGb) |

Why each track:

- Salut d'amour — the clubhouse piano of the new century: rugby's long institutional quiet inside the British clubs.
- Nimrod — slow and grave: the long quiet of the war years.
- Fantasia on Greensleeves — the old tune made new between the wars: isolated clubs edging toward a union.
- Por una cabeza — Gardel enters, the voice of the city outside the enclave: a continental competition begins.
- El día que me quieras — the most tender close: half a century of organising, ending with a national side.

Spotify albums: [Cello Moods (Lloyd Webber)](https://open.spotify.com/album/7i83TEHhrYpSdiemOVqajE), [Sheku Kanneh-Mason — Elgar](https://open.spotify.com/album/3PwJLGFcKrecmaRbJQYMSg), [Music for Remembrance (Marriner)](https://open.spotify.com/album/2baxUCy8C5UvnOdtVWLpWt), [Cinema Serenade (Perlman)](https://open.spotify.com/album/7fYlJ1HNLfs6JIvJCJ2rqq), [Tangos from Buenos Aires (Barenboim)](https://open.spotify.com/album/6SgVRRbPmjc4WuoPwm8hue). Other copies of the Salut d'amour and Greensleeves recordings play in far fewer markets; use the links above.

Spotlistr input (several of these recordings exist in more than one copy; check that each lands on the linked track):

```text
Julian Lloyd Webber - Salut d'amour, Op. 12 (Arr. Cullen for Cello & Orchestra)
Sheku Kanneh-Mason - Variations on an Original Theme, Op. 36 "Enigma": 9. Nimrod. Adagio (Arr. Parkin for Cello Ensemble)
Academy of St. Martin in the Fields - Fantasia on Greensleeves
Itzhak Perlman - Scent of a Woman: Tango (Por Una Cabeza)
Daniel Barenboim - Gardel / Arr. Carli: El día que me quieras
```

### Generation 2: The Irish Brothers (1955–1971)

Total: **22:08**. The Christian Brothers came from Ireland; the boys they taught at Stella Maris grew up in the 1960s with the Beatles. This set gives both, on classical guitar. The Japanese composer Toru Takemitsu arranged a set of popular songs for solo guitar (*12 Songs for Guitar*). This set takes the Irish "Londonderry Air", the hymn "What a Friend We Have in Jesus" (words by the Irish-born Joseph Scriven) and four Lennon–McCartney songs, all played by Shin-ichi Fukuda (2009). Between them comes the harp of Turlough O'Carolan, the blind Irish harper, in "Carolan's Farewell to Music", said to be his last tune, played by Patrick Ball (1982). The profiles are calm (flux 0.47–0.72; "Hey Jude" is the liveliest at 0.85). **Availability:** Fukuda's album plays in 166 markets, including Uruguay and South Africa but *not* the United Kingdom or parts of the Caribbean.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Twelve Songs For Guitar: I. Londonderry Air | Traditional (Irish), arr. Toru Takemitsu | Shin-ichi Fukuda | 3:07 | [Track](https://open.spotify.com/track/1uNqzVqytzs7R5yiVX8l3P) |
| 2 | Twelve Songs For Guitar: VI. What A Friend | Charles Converse (words Joseph Scriven), arr. Toru Takemitsu | Shin-ichi Fukuda | 2:39 | [Track](https://open.spotify.com/track/3AakPZjdORbLxltOaEtVzY) |
| 3 | Carolan's Farewell to Music | Turlough O'Carolan | Patrick Ball (Celtic harp) | 5:00 | [Track](https://open.spotify.com/track/3fFC3rnIPXE9UkN32IQrBa) |
| 4 | Twelve Songs For Guitar: VIII. Here, There And Everywhere | Lennon–McCartney, arr. Toru Takemitsu | Shin-ichi Fukuda | 2:57 | [Track](https://open.spotify.com/track/4RxSS1c1C1JdgYMny8gOoU) |
| 5 | Twelve Songs For Guitar: IX. Michelle | Lennon–McCartney, arr. Toru Takemitsu | Shin-ichi Fukuda | 2:53 | [Track](https://open.spotify.com/track/5qF0ssuBnxJtCVvW64bUy5) |
| 6 | Twelve Songs For Guitar: X. Hey Jude | Lennon–McCartney, arr. Toru Takemitsu | Shin-ichi Fukuda | 2:38 | [Track](https://open.spotify.com/track/5R5DrS5oSawVgjxyIhSpWt) |
| 7 | Twelve Songs For Guitar: XI. Yesterday | Lennon–McCartney, arr. Toru Takemitsu | Shin-ichi Fukuda | 2:54 | [Track](https://open.spotify.com/track/5MogW9lALozKiywSjL7m0k) |

Why each track:

- Londonderry Air — the Brothers' Ireland, arriving in Carrasco in 1955.
- What a Friend — a hymn for a school run on routine and faith.
- Carolan's Farewell to Music — the longest and quietest: the Brothers' reasoning that rugby formed character where football made stars.
- Here, There and Everywhere — the boys' own music: a school turning out teams year after year.
- Michelle — gentle and a little wistful: Old Christians, founded so that leaving school would not mean leaving the game.
- Hey Jude — the one song with some lift: the club finding its feet.
- Yesterday — the generation closes darkening toward October 1972.

Spotify albums: [Takemitsu: Guitar Works "In Memoriam" (Fukuda)](https://open.spotify.com/album/2PerdnaxwyTxawfC4jWdmd), [Celtic Harp, Vol. I: The Music of Turlough O'Carolan (Ball)](https://open.spotify.com/album/60Z4t3pEdOxaBBNlUGmxGR). The Irish songs reserved from the first pass (The South Wind, Down by the Salley Gardens, Women of Ireland, Lord Mayo) are not used.

Spotlistr input:

```text
Shin-ichi Fukuda - Twelve Songs For Guitar: I. Londonderry Air
Shin-ichi Fukuda - Twelve Songs For Guitar: VI. What A Friend
Patrick Ball - Carolan's Farewell to Music
Shin-ichi Fukuda - Twelve Songs For Guitar: VIII. Here, There And Everywhere
Shin-ichi Fukuda - Twelve Songs For Guitar: IX. Michelle
Shin-ichi Fukuda - Twelve Songs For Guitar: X. Hey Jude
Shin-ichi Fukuda - Twelve Songs For Guitar: XI. Yesterday
```

### Generation 3: The Mountain (1972–1988)

Total: **21:00**. Uruguay's own songwriters, the music the survivors' generation grew up with and came home to: Eduardo Mateo, the founding figure of modern Uruguayan popular song; Daniel Viglietti; and Leo Maslíah. The versions are by the Uruguayan guitarist Gustavo Ripa, whose albums of Uruguayan songs for solo guitar are titled *Calma*. These come from *Calma Nueva* (2024). Composer credits are from Apple Music. The profiles are calm (flux 0.57–0.77) and the level is even.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Negrita Martina - solo guitarra | Daniel Viglietti | Gustavo Ripa | 3:01 | [Track](https://open.spotify.com/track/3GE90Osbeaj7GiPlrsBUNO) |
| 2 | Quien te viera - solo guitarra | Eduardo Mateo | Gustavo Ripa | 3:05 | [Track](https://open.spotify.com/track/5CesQ7QunQm95Py88LDSwa) |
| 3 | Canción para renacer - solo guitarra | Eduardo Mateo | Gustavo Ripa | 5:22 | [Track](https://open.spotify.com/track/4bsbcZab7LGyp91slDRjx8) |
| 4 | Gurisito - solo guitarra | Daniel Viglietti | Gustavo Ripa | 2:23 | [Track](https://open.spotify.com/track/2pp4ahawpAZMroeUXOeNBq) |
| 5 | Principe azul - solo guitarra | Eduardo Mateo, Horacio Buscaglia | Gustavo Ripa | 3:02 | [Track](https://open.spotify.com/track/1sDlXCtrkKcpsu15GBESA1) |
| 6 | Biromes y servilletas - solo guitarra | Leo Maslíah | Gustavo Ripa | 4:07 | [Track](https://open.spotify.com/track/3OpujOsA4QpK7ahawGhpA7) |

Why each track:

- Negrita Martina — a gentle opening: the team and their friends flying to Chile.
- Quien te viera — the fuselage and the waiting.
- Canción para renacer — the longest and steadiest: the days counted, and the trek. The title ("song for being reborn") fits, but the track is here for its length and calm.
- Gurisito — a lullaby, the quietest in the set: the dead on the mountain.
- Príncipe azul — the return home.
- Biromes y servilletas — Maslíah's song of café poets with ballpoints and napkins, and the one piece with a little more motion: the club rebuilding in the years after.

Spotify album: [Calma Nueva (solo guitarra)](https://open.spotify.com/album/4GcWiTGk0VL2WE7f5JM1YO). Composer credits: [Apple Music — Calma Nueva](https://music.apple.com/us/album/calma-nueva-solo-guitarra/1768067059).

Spotlistr input:

```text
Gustavo Ripa - Negrita Martina - solo guitarra
Gustavo Ripa - Quien te viera - solo guitarra
Gustavo Ripa - Canción para renacer - solo guitarra
Gustavo Ripa - Gurisito - solo guitarra
Gustavo Ripa - Principe azul - solo guitarra
Gustavo Ripa - Biromes y servilletas - solo guitarra
```

### Generation 4: Getting on the Map (1989–2003)

Total: **21:01**. Jaime Roos, the most popular Uruguayan songwriter of the 1980s and 1990s and the voice of Montevideo in those years, in solo piano versions by Gonzalo Gravina (*Jaime Roos para Piano*, 2016). The tracks are the calmest on the album (flux 0.46–0.54). The recording is mastered very loud and very even (around −6 to −8 LUFS in the previews), so lower the volume relative to the other sets.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Te Acordás Hermano | Jaime Roos | Gonzalo Gravina | 3:29 | [Track](https://open.spotify.com/track/0olcB9NFuZGTJTvmyrNi8c) |
| 2 | Quince Abriles | Jaime Roos | Gonzalo Gravina | 6:20 | [Track](https://open.spotify.com/track/4ZdRKKUHtEfdDsClFX6emu) |
| 3 | El Beso | Jaime Roos | Gonzalo Gravina | 4:02 | [Track](https://open.spotify.com/track/18vAsJ9FmgNqxY2SYkDWqf) |
| 4 | Nocturno | Jaime Roos | Gonzalo Gravina | 3:13 | [Track](https://open.spotify.com/track/5aqGEvdqqzZ0YDxSBRjTuJ) |
| 5 | Si Piensas en Mí | Jaime Roos | Gonzalo Gravina | 3:57 | [Track](https://open.spotify.com/track/2yzPI718egve7jSegPYMbn) |

Why each track:

- Te Acordás Hermano — "do you remember, brother": a small country handed, at last, a qualifying pathway.
- Quince Abriles — the longest and most even: Diego Ormaechea, forty years old, playing since 1979, scoring Uruguay's first World Cup try.
- El Beso — warm and steady: the wins over Spain in 1999 and Georgia in 2003, ground out through the forwards.
- Nocturno — the darkest: the reckoning with the professional game, the 111–13 in Brisbane.
- Si Piensas en Mí — "if you think of me": Pablo Lemoine signing for Bristol, and the road abroad.

Spotify album: [Jaime Roos para Piano](https://open.spotify.com/album/66rz1OnWxh38pRXO2nlUoN).

Spotlistr input:

```text
Gonzalo Gravina - Te Acordás Hermano
Gonzalo Gravina - Quince Abriles
Gonzalo Gravina - El Beso
Gonzalo Gravina - Nocturno
Gonzalo Gravina - Si Piensas en Mí
```

### Generation 5: The Plan (2007–2019)

Total: **21:55**. Uruguayan songs in Gustavo Ripa's solo-guitar versions: four by Fernando Cabrera, the Montevideo songwriter, and Alfredo Zitarrosa's "Milonga en do". Three of the recordings (2012 and 2014) fall inside this generation's dates; the other two are Ripa's 2024 re-recordings. The profiles are calm (flux 0.63–0.79). Ripa's albums are mastered at different levels, up to about 9 dB apart, so the set runs from the quietest recording to the loudest. Ripa's first *Calma* album (2010) also has "El tiempo está después" and "Por ejemplo", but it is country-restricted in every market; use the recordings linked below. Composer credits are from Apple Music.

Revised 22 September 2026. This set replaces Coldplay for string quartet. The chapter's British thread belongs to the enclave generations, and the plan was Uruguay's own.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Paso Molino | Fernando Cabrera | Gustavo Ripa | 4:09 | [Track](https://open.spotify.com/track/2PEWgFPH5rF1fuOdfShEfT) |
| 2 | La casa de al lado | Fernando Cabrera | Gustavo Ripa | 5:37 | [Track](https://open.spotify.com/track/2pERrlJ82Z0wRpByJA0WYw) |
| 3 | Milonga en do | Alfredo Zitarrosa | Gustavo Ripa | 4:20 | [Track](https://open.spotify.com/track/5zK0qA2kr30QrX6RTzduUn) |
| 4 | Por ejemplo - solo guitarra | Fernando Cabrera | Gustavo Ripa | 4:00 | [Track](https://open.spotify.com/track/6yo5BkZAVBgBaWt61NsYNO) |
| 5 | El tiempo está después | Fernando Cabrera | Gustavo Ripa | 3:49 | [Track](https://open.spotify.com/track/0pi69EaSwRXkXN8KURxPXu) |

Why each track:

- Paso Molino — the quietest opening, named for a Montevideo neighbourhood: two failures, in 2007 and 2010, and a union starting again.
- La casa de al lado — the longest and most even: the unglamorous work of building the Charrúa base and a full-time squad.
- Milonga en do — Zitarrosa's milonga, a Uruguayan standard: qualification cycles, and the climb past Russia and then Canada.
- Por ejemplo — steady and plain: the growing belief that the plan works.
- El tiempo está después — "time comes afterwards": Kamaishi, and the Fiji upset.

Spotify albums: [Más Calma](https://open.spotify.com/album/43rD04k0mML8Ccvjr4SRHy), [Calma 3](https://open.spotify.com/album/74R1YVC61eIz5EDVszTWSX), [Calma Nueva (solo guitarra)](https://open.spotify.com/album/4GcWiTGk0VL2WE7f5JM1YO). Composer credits: [Apple Music — Más Calma](https://music.apple.com/us/album/m%C3%A1s-calma/1747742407), [Apple Music — Calma 3](https://music.apple.com/us/album/calma-3/1747759578), [Apple Music — Calma Nueva](https://music.apple.com/us/album/calma-nueva-solo-guitarra/1768067059).

Spotlistr input (Ripa recorded some of these songs more than once; check that each lands on the linked track):

```text
Gustavo Ripa - Paso Molino
Gustavo Ripa - La casa de al lado
Gustavo Ripa - Milonga en do
Gustavo Ripa - Por ejemplo - solo guitarra
Gustavo Ripa - El tiempo está después
```

### Generation 6: The Branches Rejoin (2020–2026)

Total: **21:49**. The songs Uruguayans of today grew up on, from both banks of the River Plate, in Gustavo Ripa's solo-guitar versions (2024–25). Emiliano Brancciari of No Te Va Gustar, one of the biggest Uruguayan bands of this century, opens the set. The rest is the Argentine rock and song that belongs as much to Montevideo as to Buenos Aires: Gustavo Cerati, León Gieco and Luis Alberto Spinetta. Ripa called his 2025 album of these songs *El río que nos une*, "the river that unites us". The profiles are calm (flux 0.55–0.73). The opening track is about 4 dB louder than the rest.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Ese maldito momento - solo guitarra | Emiliano Brancciari | Gustavo Ripa | 5:00 | [Track](https://open.spotify.com/track/7HKvnDpcEQBYMi0rRZInMl) |
| 2 | Ay! este azul - Solo Guitarra | Adolfo Cabral | Gustavo Ripa | 4:02 | [Track](https://open.spotify.com/track/3GJR0bLoqqbPhZQyNsvBCf) |
| 3 | Crimen - Solo Guitarra | Gustavo Cerati | Gustavo Ripa | 3:23 | [Track](https://open.spotify.com/track/4AsDQ4YUXrEPOXkBpPvdB2) |
| 4 | Todos los días un poco - Solo Guitarra | León Gieco | Gustavo Ripa | 3:48 | [Track](https://open.spotify.com/track/2J93UHSRv0GX5K28mQzm17) |
| 5 | Plegaria para un niño dormido - Solo Guitarra | Luis Alberto Spinetta | Gustavo Ripa | 5:36 | [Track](https://open.spotify.com/track/1YC8oO5JWE9enqPVc7KnCY) |

Why each track:

- Ese maldito momento — a modern Uruguayan rock song turned quiet: Peñarol's black and gold, and the railwaymen's club putting a professional rugby team on the field.
- Ay! este azul — the calmest in the set: weekly professional competition at last, and three Super Rugby Americas titles.
- Crimen — steady, with a little more motion: the comeback against Namibia in Lyon, and a sixth consecutive World Cup qualification.
- Todos los días un poco — "a little every day": homegrown players, raised at home rather than abroad.
- Plegaria para un niño dormido — the longest and quietest close: the mid-2026 snapshot.

Spotify albums: [Calma Nueva (solo guitarra)](https://open.spotify.com/album/4GcWiTGk0VL2WE7f5JM1YO), [El río que nos une](https://open.spotify.com/album/7Gwu6zMvBp5IBJLHjAKYGi). Revised 22 September 2026: Cabrera's "El tiempo está después" and "Por ejemplo" moved to Generation 5, so that Cabrera has one set, and "Ay! este azul" and "Crimen" replace them. Composer credits: [Apple Music — Calma Nueva](https://music.apple.com/us/album/calma-nueva-solo-guitarra/1768067059), [Apple Music — El río que nos une](https://music.apple.com/us/album/el-r%C3%ADo-que-nos-une/1810264664).

Spotlistr input:

```text
Gustavo Ripa - Ese maldito momento - solo guitarra
Gustavo Ripa - Ay! este azul - Solo Guitarra
Gustavo Ripa - Crimen - Solo Guitarra
Gustavo Ripa - Todos los días un poco - Solo Guitarra
Gustavo Ripa - Plegaria para un niño dormido - Solo Guitarra
```

Uruguay complete: Generations 0–6.

---

## Chapter 2 — Argentina

Rebuilt on 22 September 2026 on the same basis as Uruguay: the music of the people in each generation, matched to the mood of what the section tells. The sets run:
- British favourites for the Anglo-Argentine clubs.
- Piazzolla's 1965 quintet for the breakout.
- Eduardo Falú's *Suite Argentina*, recorded in 1972, for the Porta years.
- Rock nacional and two zambas, kept low, for the worst decade.
- Litoral piano for the team that didn't exist.
- Santaolalla for the Jaguares.
- Fito Páez's orchestral Arlt album for the diaspora.
- Juan Falú's cuecas and chacareras, recorded months after the naranjazo, for Tucumán.

Every set is instrumental. Re-checked against mood later the same day: the Argentine folk repertoire — the suite, the zambas, the chacareras — had been thrown out by a rule against percussive sound that no longer exists, and came back. One gap remains: the best-loved Argentine rock of the 1990s (Soda Stereo, Charly García, Fito Páez's hits) has no good instrumental versions on Spotify, so the 1987–1999 set uses older rock and folk standards instead.

### Generation 0: The British Enclave (1873–1964)

Total: **21:12**. The music the Anglo-Argentine clubs brought from home and kept: British favourites of the late Victorian and Edwardian years. Elgar's "Chanson de nuit" (1897) and "Sospiri" (1914) were salon and concert favourites across the British world. Delius's "On Hearing the First Cuckoo in Spring" (1912) is a country idyll built on a Norwegian folk song. George Butterworth's "The Banks of Green Willow" (1913) is built on English folk songs; Butterworth, a folk-song collector, was killed on the Somme in 1916. The recordings are by Pinchas Zukerman with the Royal Philharmonic, and by the Academy of St Martin in the Fields under Sir Neville Marriner. The profiles are calm (flux 0.46–0.59), but these are orchestral recordings with swells (a loudness range of 11–15 LU) and different levels. Set the volume on the second track, the quietest.

Revised 22 September 2026. This set replaces the Argentine concert piano of Julián Aguirre and Carlos Guastavino. The enclave's own music was British, not the conservatory music of the Buenos Aires elite.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Chanson de Nuit, Op. 15, No. 1 | Edward Elgar | Royal Philharmonic Orchestra, Pinchas Zukerman | 4:26 | [Track](https://open.spotify.com/track/2V7cruKHOiq39zIfgKRErF) |
| 2 | On hearing the first Cuckoo in Spring | Frederick Delius | Academy of St. Martin in the Fields, Sir Neville Marriner | 5:47 | [Track](https://open.spotify.com/track/1F0F9swIwGmhl7LWdAOjr0) |
| 3 | The Banks of Green Willow | George Butterworth | Academy of St. Martin in the Fields, Sir Neville Marriner | 6:07 | [Track](https://open.spotify.com/track/3H6W49dq60DjOkuftHbsRj) |
| 4 | Sospiri, Op. 70 | Edward Elgar | Academy of St. Martin in the Fields, Sir Neville Marriner | 4:52 | [Track](https://open.spotify.com/track/28m8QKREnoxsQwzOI3qwsi) |

Why each track:

- Chanson de nuit — a Victorian evening piece: the Buenos Aires Football Club arguing for seven years over which rules to play, in a game kept inside the Anglo community.
- On Hearing the First Cuckoo in Spring — pastoral and unhurried: the institution-building, from the 1899 union to the clubs that quit football when it turned professional.
- The Banks of Green Willow — a folk song set by a composer who died in the war: ninety-one years without beating a touring side, and the settled sense of inferiority.
- Sospiri — "sighs", slow and grave: the Campeonato Argentino and the Catholic orders carrying the game beyond the capital, until the turn of 1964.

Spotify album: [Music for Remembrance](https://open.spotify.com/album/2baxUCy8C5UvnOdtVWLpWt). These tracks carry no country restriction. The same recordings appear on several other compilations; use the links above.

Spotlistr input (check that each lands on the linked track):

```text
Pinchas Zukerman - Chanson de Nuit, Op. 15, No. 1
Academy of St. Martin in the Fields - On hearing the first Cuckoo in Spring
Academy of St. Martin in the Fields - The Banks of Green Willow
Academy of St. Martin in the Fields - Sospiri, Op. 70
```

### Generation 1: The Breakout (1965–1973)

Total: **22:35**. Instrumental nuevo tango from Astor Piazzolla's 1965 concert at Philharmonic Hall in New York. It is period music: Piazzolla's break with tango tradition happened in the same years Argentina broke out of ninety-two years of losing. This is the chapter's only Piazzolla set, and it now keeps only the quintet's slower music. Revised in September 2026: "Bandoneón, Guitarra y Bajo" was dropped (flux 1.45) for "Tango Diablo". Revised again on 22 September 2026: "Tango Diablo", angular and driving, is replaced by "La Mufa" from the same concert (flux 0.43). The *Serie del Ángel* opens and closes the set, with "La Mufa" and "Romance del Diablo" between.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Milonga Del Angel - Instrumental | Astor Piazzolla | Astor Piazzolla | 5:25 | [Track](https://open.spotify.com/track/67FF3iasOjQRgxub0hJsL8) |
| 2 | La Mufa - Instrumental | Astor Piazzolla | Astor Piazzolla | 6:01 | [Track](https://open.spotify.com/track/4ZoRoktqDXZ793WmQ3yF7K) |
| 3 | Romance Del Diablo - Instrumental | Astor Piazzolla | Astor Piazzolla | 5:16 | [Track](https://open.spotify.com/track/6o5XER808VMm03MBQbbXuI) |
| 4 | Resurrección Del Angel - Instrumental | Astor Piazzolla | Astor Piazzolla | 5:53 | [Track](https://open.spotify.com/track/34l0RjdwAC4RZ3YZ2qwizP) |

Why each track:

- Milonga Del Angel — reflective and spacious, the calmest track in the set (flux 0.37): the invitation, and a bow-tied schoolmaster arriving from Durban.
- La Mufa — slow and brooding: the long preparation and a tour of 46,252 kilometres.
- Romance Del Diablo — lyrical tension: apartheid South Africa, and the debt incurred in gratitude.
- Resurrección Del Angel — an expansive close: Ellis Park, the palomita, and a name born of a journalist's error.

Spotify album: [Concierto De Tango En El Philarmonic Hall De New York](https://open.spotify.com/album/3mNbSw2E37Kx6DQ2Xellzf). Select this edition to match the timings. The original 1965 LP: [Discogs — Concierto De Tango En El Philharmonic Hall De Nueva York](https://www.discogs.com/master/1361705-Astor-Piazzolla-Y-Su-Quinteto-Nuevo-Tango-Concierto-De-Tango-En-El-Philharmonic-Hall-De-Nueva-York). "La Mufa" appears in Discogs' tracklist for the 1965 LP as returned by search on 22 September 2026; Discogs blocked direct access that day, so confirm it by hand.

Spotlistr input:

```text
Astor Piazzolla - Milonga Del Angel - Instrumental
Astor Piazzolla - La Mufa - Instrumental
Astor Piazzolla - Romance Del Diablo - Instrumental
Astor Piazzolla - Resurrección Del Angel - Instrumental
```

### Generation 2: The Porta Generation (1971–1987)

Total: **21:18**. One continuous piece: Eduardo Falú's *Suite Argentina*, for guitar, strings, horn and harpsichord, which Falú recorded in 1972 with the Camerata Bariloche. Falú (1923–2013) was the most famous guitarist in the country and a household name in exactly these years, so this is period repertoire, cut in the first years of the government's bans. Its six dances, listed in other recordings as Carnavalito, Misachico, Bailecito, Zamba, Estilo and Malambo, are the forms of the northwest, and it ends on the malambo, the dance men dance one against another. The chapter describes the era as "not a team so much as a genius, wrapped in a very good pack" — a solo guitar carried by an ensemble is that shape exactly, and the music carries the era's pride and its grievance at once. The sound is unlike anything else in the chapter: no bandoneón, no tango.

Restored 22 September 2026, hours after being replaced by Leguizamón zambas on two grounds that do not survive the rules at the top of this file: that a suite is concert music rather than popular music, and that Falú's guitar was too strummed to read over. Falú *was* the popular music of this generation, and the strumming objection came from the discarded flux gate.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Suite Argentina | Eduardo Falú | Eduardo Falú, Camerata Bariloche | 21:18 | [Track](https://open.spotify.com/track/71nNVIHo47bR4wSclKjZUF) |

Why each movement:

- Carnavalito — a bright opening: the boy who turned down Boca Juniors and debuted in 1971.
- Misachico — slower and processional (the misachico is a devotional procession of the northwest): the bans of 1971–73, and the union's federal committee forced to resign.
- Bailecito and Zamba — the dance centre: the shadow Jaguars in white striped blue, red and gold, Australia beaten in 1979, England held at Twickenham.
- Estilo — the long slow movement: one man scoring every point, and the thinness underneath.
- Malambo — the competitive close: Bloemfontein, the 21–21 against the All Blacks, and the series win over Australia in 1987.

The track plays in 185 markets. Spotify album: [GUITAR WORKS](https://open.spotify.com/album/7DucSHS4sbKrignJbrCcK9) (Spotify dates it 1970; the recording is documented as 1972). Source: [Rosa Incaica — Centenario de Eduardo Falú](https://rosaincaica.com/centenario-de-eduardo-falu).

Spotlistr input:

```text
Eduardo Falú, Camerata Bariloche - Suite Argentina
```

### Generation 3: The Self-Inflicted Wound (1987–1999)

Total: **19:46**. The worst decade Argentine rugby ever had, and the set is kept low and sad for it. Three rock nacional and canción standards the players of these years grew up with — Luis Alberto Spinetta, Litto Nebbia and María Elena Walsh — in Gustavo Ripa's solo-guitar versions (2025); one Leguizamón zamba played by Pablo Márquez, who was raised in Salta (ECM, recorded Lugano 2012, released 2015); and a folk standard on Carlos Aguirre's piano to close. Nothing here lifts until the last track, because nothing in the story does. The best-loved Argentine rock of the nineties itself (Soda Stereo, Charly García, Fito Páez's hits) has no good instrumental versions on Spotify — the ones found were strummed self-releases without proper credits. Composer credits are from Apple Music. Every track plays in 182 markets or more.

Revised twice on 22 September 2026. The set replaced Dino Saluzzi and Anja Lechner's *Ojos Negros*, chamber music too academic for this list; it then lost Eduardo Falú's "Vidala del regreso" when *Suite Argentina* returned to Generation 2, and gained "Zamba de Lozano" from what had briefly been the Generation 2 set.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Todas las hojas son del viento - Solo Guitarra | Luis Alberto Spinetta | Gustavo Ripa | 2:39 | [Track](https://open.spotify.com/track/3v3ocwAiDRRj7oZlAELFgH) |
| 2 | Zamba de Lozano | Gustavo "Cuchi" Leguizamón | Pablo Márquez | 4:47 | [Track](https://open.spotify.com/track/0qe364Ne2IDOoYv26nPy5Q) |
| 3 | Solo se trata de vivir - Solo Guitarra [remastered] | Litto Nebbia | Gustavo Ripa | 3:58 | [Track](https://open.spotify.com/track/4JrNSMsz0pQdloKy0OGRNn) |
| 4 | Serenata para la tierra de uno - Solo Guitarra [remastered] | María Elena Walsh | Gustavo Ripa | 3:40 | [Track](https://open.spotify.com/track/2zAaxgJ59VosOLdxvkd4Ep) |
| 5 | Zamba para no morir | Alfredo Rosales, Norberto Ambrós, Hamlet Lima Quintana | Carlos Aguirre | 4:42 | [Track](https://open.spotify.com/track/64fjbklDFgy8fjot7c4O0b) |

Why each track:

- Todas las hojas son del viento — short, quiet, over before it settles: Porta walks off in November 1987 and everything he carried goes with him.
- Zamba de Lozano — a zamba for the rule that barred professionals from the national side: Noriega gone to Australia, Méndez to South Africa, and a union forbidding itself its own best players.
- Solo se trata de vivir — "it's only about living": pool exits in 1991 and 1995, and 93–8 at Athletic Park.
- Serenata para la tierra de uno — Walsh's song of the pull between staying and leaving, and the plainest playing in the set: a squad scattered through France, England and Italy.
- Zamba para no morir — piano, the one change of instrument and the only warmth: Wyllie's nine-fifty, Stradey Park, and Lens.

Spotify albums: [El río que nos une (Ripa)](https://open.spotify.com/album/7Gwu6zMvBp5IBJLHjAKYGi), [Gustavo Leguizamón: El Cuchi bien temperado (Márquez)](https://open.spotify.com/album/2bzQKVNP1gsAw7JhdPXdgE), [Caminos (Aguirre)](https://open.spotify.com/album/6SFkAYs6D86IRcfbgOSyNH). Sources: [ECM — El Cuchi bien temperado](https://ecmrecords.com/product/gustavo-leguizamon-el-cuchi-bien-temperado-pablo-marquez/). Composer credits: [Apple Music — El río que nos une](https://music.apple.com/us/album/el-r%C3%ADo-que-nos-une/1810264664), [Apple Music — Caminos](https://music.apple.com/us/album/caminos/1573032570).

Spotlistr input:

```text
Gustavo Ripa - Todas las hojas son del viento - Solo Guitarra
Pablo Marquez - Zamba de Lozano
Gustavo Ripa - Solo se trata de vivir - Solo Guitarra [remastered]
Gustavo Ripa - Serenata para la tierra de uno - Solo Guitarra [remastered]
Carlos Aguirre - Zamba para no morir
```

### Generation 4: The Team That Didn't Exist (2000–2011)

Total: **20:58**. Solo piano from the Litoral: Carlos Aguirre's *Caminos* (Shagrada Medra, Paraná, 2006), the solo-piano album of his discography, recorded inside this generation's dates. Aguirre works in Paraná, Entre Ríos, and *La Nación* calls him a reference voice of Litoral music. Five of the pieces are his. "Llovizna" is by Gari Di Pietro, and "Canción de cuna costera" is a Litoral lullaby by Linares Cardoso (composer credits from Apple Music). The set keeps the chapter's northeast, the region Spasiuk's chamamé stood for, but trades an accordion band over cajón for one piano. The pieces are short and quiet (flux 0.47–0.56), and even in level (−11 to −15 LUFS).

Revised 22 September 2026. This set replaces Chango Spasiuk's *Pynandí – Los Descalzos* (2009), whose chamamé is played over cajón, udu and other hand percussion.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Un pueblo de paso | Carlos Aguirre | Carlos Aguirre | 2:37 | [Track](https://open.spotify.com/track/362WTOLqAeEnHpZjRjiCqO) |
| 2 | Vuls a Lais | Carlos Aguirre | Carlos Aguirre | 2:15 | [Track](https://open.spotify.com/track/0pyhr1clHbuiFbX8aInMhd) |
| 3 | Mai | Carlos Aguirre | Carlos Aguirre | 1:54 | [Track](https://open.spotify.com/track/0s2pbGtlP0AclFlPu0zkHa) |
| 4 | Llovizna | Gari Di Pietro | Carlos Aguirre | 2:17 | [Track](https://open.spotify.com/track/6tAN7zdOVtVUFerk1tA6yv) |
| 5 | Gallo | Carlos Aguirre | Carlos Aguirre | 1:44 | [Track](https://open.spotify.com/track/4nwZmhaUISHg8KqH5RVG41) |
| 6 | Milonga gris | Carlos Aguirre | Carlos Aguirre | 3:59 | [Track](https://open.spotify.com/track/5XWaesA0oOPY4gpdjPZlh1) |
| 7 | Canción de cuna costera | Linares Cardoso | Carlos Aguirre | 6:12 | [Track](https://open.spotify.com/track/6fOiFInlBHRfZpxj1yDDOa) |

Why each track:

- Un pueblo de paso — an unhurried opening for the road Argentina's best players took into France, England and Ireland, where the national team was effectively professionalised in exile.
- Vuls a Lais — a light waltz: Loffreda gathering players shaped by different foreign clubs into a coherent side.
- Mai — short and still: 2003–2006, good enough to beat almost anyone and given no competition to do it in.
- Llovizna — soft and even: from the 16–15 against Ireland to a handful of Tests a year.
- Gallo — brief, with a little more lift: Argentina emerging from outsider status.
- Milonga gris — a River Plate milonga, quiet and grey: the 2007 semi-final.
- Canción de cuna costera — the longest and calmest piece to close: the second victory over France, Contepomi's bow and third place in the world, kept intimate rather than triumphant.

Spotify album: [Caminos](https://open.spotify.com/album/6SFkAYs6D86IRcfbgOSyNH). The tracks carry no country restriction on Spotify. Sources: [Carlos Aguirre — Caminos on Bandcamp (label, city, year)](https://carlosaguirre.bandcamp.com/album/caminos), [Quinto Elemento — *Caminos* as his solo-piano album](https://quintoelementoweb.com.ar/carlos-aguirre-lanzamiento-y-presentacion-de-su-disco-la-musica-del-agua.html), [La Nación — Carlos Aguirre](https://www.lanacion.com.ar/espectaculos/musica/carlos-aguirre-una-voz-de-referencia-para-la-musica-litoralena-nid2085033/), [Apple Music — Caminos (composer credits)](https://music.apple.com/us/album/caminos/1573032570), [FolkloreCLUB — *Pynandí* credits (percussion in the replaced set)](https://www.folkloreclub.com.ar/nota.asp?idnota=1859).

Spotlistr input:

```text
Carlos Aguirre - Un pueblo de paso
Carlos Aguirre - Vuls a Lais
Carlos Aguirre - Mai
Carlos Aguirre - Llovizna
Carlos Aguirre - Gallo
Carlos Aguirre - Milonga gris
Carlos Aguirre - Canción de cuna costera
```

### Generation 5: The Jaguares (2009–2022)

Total: **20:07**. Instrumental music by Gustavo Santaolalla from *Camino*, thirteen original pieces built on the ronroco (a ten-string Andean lute) and other plucked strings. Sony's release notes also list pipes, pump organ, keyboards and percussion on some tracks. Sony Masterworks released it in 2014 (Spotify lists 2012), inside this generation's dates either way. It is spare and patient but never static, the sound of something built from very little, and it is unlike anything else in the chapter: no bellows and no tango. This set replaces Escalandrum's *Piazzolla Plays Piazzolla*, whose four tracks were Astor Piazzolla compositions and made a third Piazzolla set. "The Maze", the busiest track on *Camino* (flux 0.99), is left out. Revised 22 September 2026: "Seguir", the most driven track in the set, is replaced by the quieter "Through the Rainwall" (flux 0.38).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Alma | Gustavo Santaolalla | Gustavo Santaolalla | 2:36 | [Track](https://open.spotify.com/track/4TKIm82qgyDWDHizsayzs1) |
| 2 | Vamos | Gustavo Santaolalla | Gustavo Santaolalla | 3:00 | [Track](https://open.spotify.com/track/5mCROvT27Sgasq1GEBf4PH) |
| 3 | Parana | Gustavo Santaolalla | Gustavo Santaolalla | 3:28 | [Track](https://open.spotify.com/track/1ywfgHVjdmnwAFjmQek2WY) |
| 4 | Cordon de Plata | Gustavo Santaolalla | Gustavo Santaolalla | 3:00 | [Track](https://open.spotify.com/track/2PGqbsSYbNYhfqEOtiH4k7) |
| 5 | Through the Rainwall | Gustavo Santaolalla | Gustavo Santaolalla | 2:36 | [Track](https://open.spotify.com/track/1492l40u2s9XK7FGBO5JlE) |
| 6 | Requiem | Gustavo Santaolalla | Gustavo Santaolalla | 1:51 | [Track](https://open.spotify.com/track/3gGvo7Xa8fol73wEDS6hrL) |
| 7 | Returning | Gustavo Santaolalla | Gustavo Santaolalla | 3:36 | [Track](https://open.spotify.com/track/0AtgoHl7RDAGk4wpXMIn6o) |

Why each track:

- Alma — the opening: Pichot stops playing and starts Pampas XV.
- Vamos — steady and even: a team with no home league winning other people's leagues, the Vodacom Cup and the Pacific Rugby Cup.
- Parana — the most even-flowing track in the set (the narrowest loudness range): the long grind of 29 defeats in the first 33 Rugby Championship matches.
- Cordon de Plata — Durban in 2015, with the 1965 Pumas in the stands.
- Through the Rainwall — spacious, with long resonance: the Jaguares' run to the 2019 Super Rugby final, and the All Blacks beaten in 2020.
- Requiem — the quietest track on the album (flux 0.37): July 2020, the whole squad released. The title fits, but the track is here because it is the quietest.
- Returning — a calm, unresolved close: the players scattering back to Europe, and the Jaguares split into Pampas and Dogos.

Spotify album: [Camino](https://open.spotify.com/album/6ZYBjNB7SqYvsbAs9F78CN). Source: [PR Newswire — Sony Music Masterworks releases Gustavo Santaolalla's Camino](https://www.prnewswire.com/news-releases/sony-music-masterworks-releases-gustavo-santaolallas-camino-263326391.html). The *Ronroco* compositions reserved from the superseded Uruguay Generation 3 are different works.

Spotlistr input:

```text
Gustavo Santaolalla - Alma
Gustavo Santaolalla - Vamos
Gustavo Santaolalla - Parana
Gustavo Santaolalla - Cordon de Plata
Gustavo Santaolalla - Through the Rainwall
Gustavo Santaolalla - Requiem
Gustavo Santaolalla - Returning
```

### Generation 6: The Diaspora (2020–2026)

Total: **21:53**. Fito Páez, one of Argentina's best-loved songwriters, from *Futurología Arlt* (2022). It is an orchestral album inspired by Roberto Arlt's novel *Los siete locos*, composed by Páez with Diego Olivero and recorded with the Czech National Symphony Orchestra. It is instrumental apart from its opening track, which is not used. An Argentine score recorded abroad suits a national team built almost entirely abroad. The set closes with Páez's own "11 y 6" on Gustavo Ripa's guitar (2025). The orchestral tracks profile calm (flux 0.36–0.54), and "11 y 6" slightly busier (0.84). *La Nación* describes the album as "tango-pop-futurista" with Piazzolla references, so expect bandoneón and some swells between the calm passages.

Revised 22 September 2026. This set replaces Osvaldo Golijov's string quartets, which are contemporary concert music.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Buenos Aires 20/30 | Fito Páez, Diego Olivero | Fito Páez, Czech National Symphony Orchestra | 4:40 | [Track](https://open.spotify.com/track/429Lgl9cm5ppaJ208RvLWn) |
| 2 | Tema de Amor de Elsa y Remo | Fito Páez, Diego Olivero | Fito Páez, Czech National Symphony Orchestra | 3:23 | [Track](https://open.spotify.com/track/2PIS0R6hCwwuhVPskF7N0E) |
| 3 | Amor y Redención / Nostalgia Argentina | Fito Páez, Diego Olivero | Fito Páez, Czech National Symphony Orchestra | 5:15 | [Track](https://open.spotify.com/track/7fs1BWDgUFPq2amkccYLIs) |
| 4 | La Rosa de Cobre | Fito Páez, Diego Olivero | Fito Páez, Czech National Symphony Orchestra | 2:58 | [Track](https://open.spotify.com/track/6DPD6XeHd59QjWiXIfED4l) |
| 5 | El Ángel de la Avenida de Mayo | Fito Páez, Diego Olivero | Fito Páez, Czech National Symphony Orchestra | 1:46 | [Track](https://open.spotify.com/track/40ghsNVYg0GRV1jXn5QHQD) |
| 6 | 11 y 6 - Solo Guitarra | Fito Páez | Gustavo Ripa | 3:51 | [Track](https://open.spotify.com/track/1gaGjwqmPF18vd7f0rl6SL) |

Why each track:

- Buenos Aires 20/30 — the city the players left: no franchise, no domestic league, and 31 of Cheika's 33 players abroad.
- Tema de Amor de Elsa y Remo — a love theme: Cheika rebuilding from a dispersed squad and carrying Argentina to another World Cup semi-final.
- Amor y Redención / Nostalgia Argentina — the longest and calmest: Contepomi's wins in 2024–25 in Wellington, the Triple Crown, and the British & Irish Lions beaten in Dublin.
- La Rosa de Cobre — quieter again: the mixed balance sheet of mid-2026 and the cool mood at home.
- El Ángel de la Avenida de Mayo — short and bright: Vélez, August 2025.
- 11 y 6 — Páez's own early song on one guitar: the road to 2027.

Spotify albums: [Futurología Arlt](https://open.spotify.com/album/3ohXbHtGxu0wDg70yOjeCn), [El río que nos une](https://open.spotify.com/album/7Gwu6zMvBp5IBJLHjAKYGi). Source: [La Nación — Futurología Arlt (instrumental, the Czech orchestra, the Arlt novel)](https://www.lanacion.com.ar/revista-rolling-stone/como-es-el-disco-sinfonico-de-fito-paez-inspirado-en-la-obra-de-roberto-arlt-nid04032022/).

Spotlistr input:

```text
Fito Paez - Buenos Aires 20/30
Fito Paez - Tema de Amor de Elsa y Remo
Fito Paez - Amor y Redención / Nostalgia Argentina
Fito Paez - La Rosa de Cobre
Fito Paez - El Ángel de la Avenida de Mayo
Gustavo Ripa - 11 y 6 - Solo Guitarra
```

### The Interior: Tucumán (1915–2026)

Total: **20:46**. Solo guitar by Juan Falú, born in San Miguel de Tucumán in 1948 and nephew of Eduardo Falú (Generation 2). He came back from exile in Brazil in 1984, and *Con la guitarra que tengo* was his first album, released in 1985–86 (Konex gives 1985; Spotify lists April 1986) — months after Tucumán beat Buenos Aires 13–9. The forms are the province's own: the cueca, the gato and, above all, the chacarera. This is the book's most passionate section, so it gets the chapter's liveliest set. It is still one guitar, with no percussion and no voice, and it opens with the album's calmest tracks before the dances arrive with 1985. The tracks play in 185 markets.

Restored 22 September 2026, hours after being replaced by vidalas from Falú's *Tucumano soy* (2025) on the grounds that dance rhythms pull attention off the page. The mood of this section is defiance — a provincial side beating the capital's twelve Pumas, fifty men screaming in an away stand, flags burning on the terraces — and in Tucumán that sounds like a chacarera, not a lament.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | De la raíz a la copa | Juan Falú | Juan Falú | 1:48 | [Track](https://open.spotify.com/track/6QpNEofgxJ31Z9VXxZQ9Si) |
| 2 | Por lo fino y por lo grueso | Juan Falú | Juan Falú | 4:03 | [Track](https://open.spotify.com/track/1DcYMF06fBN5b0K9yPt22A) |
| 3 | Del buen riego | Juan Falú | Juan Falú | 1:45 | [Track](https://open.spotify.com/track/5ywAelF02V2DOfCEeJ4PVs) |
| 4 | El cauce y el agua | Juan Falú | Juan Falú | 3:19 | [Track](https://open.spotify.com/track/4cydUnPGv2EQDGYgExwsFH) |
| 5 | Buena yunta | Juan Falú | Juan Falú | 2:26 | [Track](https://open.spotify.com/track/0gxCTfk3nvOdDk8sGq9ezh) |
| 6 | Cueca la diagonal | Juan Falú | Juan Falú | 2:24 | [Track](https://open.spotify.com/track/4qIWbIPyFpSqS2OXLrSQJI) |
| 7 | Chacarera ututa | Juan Falú | Juan Falú | 2:31 | [Track](https://open.spotify.com/track/61G0lQiAnVLOLWSxkNO3aB) |
| 8 | Chacarera tenebrosa | Juan Falú | Juan Falú | 2:30 | [Track](https://open.spotify.com/track/1H1871K4V4vhYyxo6ogSn0) |

Why each track:

- De la raíz a la copa — "from the root to the treetop", the shortest and calmest: English students at the sugar mills, and a game that twice fell apart.
- Por lo fino y por lo grueso — the longest and most patient: 1941–44, Natación y Gimnasia, Tucumán Rugby, Universitario, and four clubs founding a union.
- Del buen riego — a brief, steady interlude: the Anual Tucumano from 1944.
- El cauce y el agua — flowing, persistent: the long apprenticeship of coming south every year and losing.
- Buena yunta — a *yunta* is a yoke of oxen and, in the River Plate, a trusted partner: *más que un club, una amistad*.
- Cueca la diagonal — the dances begin: 5 October 1985 at Sáenz Peña, and nineteen years of Buenos Aires ended in one afternoon.
- Chacarera ututa — the northwest's signature dance at full tilt: *la mística naranja* and the flood of titles.
- Chacarera tenebrosa — a darker second chacarera to close: the ceiling Tucumán was never allowed to break, and the nine and the ten steering Argentina at Vélez in 2025.

Spotify album: [Con La Guitarra Que Tengo](https://open.spotify.com/album/1nUJS4anKBdMEcHZ5SpJ1A). Source: [Fundación Konex — Juan Falú](https://www.fundacionkonex.org/b4294-juan-falu).

Spotlistr input:

```text
Juan Falú - De la raíz a la copa
Juan Falú - Por lo fino y por lo grueso
Juan Falú - Del buen riego
Juan Falú - El cauce y el agua
Juan Falú - Buena yunta
Juan Falú - Cueca la diagonal
Juan Falú - Chacarera ututa
Juan Falú - Chacarera tenebrosa
```

Argentina complete: Generations 0–6 and the Tucumán coda.

---

## Chapter 3 — Chile

Built on 22 September 2026 on the people-and-mood rules, Generations 2 to 6 first and then 0 and 1. The sets run:
- Scottish fiddle, English light music and a Chilean quartet for the scattered ports.
- Allende's tonadas on piano for the union and the first Tests.
- Violeta Parra's 1957 guitar instrumentals, with a Scottish lament for the Campbell brothers, for the second nation.
- Chilean guitar music for the mountain, the silent years and the 1983 tour.
- Horacio Salinas's 1990s film and television cues for the wilderness.
- His *Suite Patagonia* for Selknam and the first World Cup.
- Jorge González and a viola for the house on the hill.

Every set is instrumental. Two decisions are worth knowing before reading the sets: no Selk'nam ceremonial recording appears anywhere, for the reasons in Generation 5 and in "Music to handle with care"; and the chapter's music stays off the politics of 1973–89, because the prose deliberately declines to link Chilean rugby to the regime, and a soundtrack of the murdered and the exiled would make that claim for it.

### Generation 0: The Ports and the Saltpetre (1892–1934)

Total: **21:50**. Rebuilt on 22 September 2026, the last Chile set to be re-checked against the two tests at the top of this file. This generation has no single people and no founding club, so it has no single music either: the game came off the decks of ships into scattered ports over forty years, and the set is assembled the same way. Scottish fiddle for the Argyll schoolmaster and the craftsmen of the port, English light music for the ten thousand English of Valparaíso, a colonial's piano piece for the schools, and a Chilean string quartet for the country all of it landed in. Everything here was written between 1892 and 1930 except the recordings themselves.

The level runs from −11 to −17 LUFS, so the set moves from its fullest sound to its quietest; play it in the order given. The French colony's Stade Français, which took up rugby in 1930, goes unrepresented: the obvious pieces are Fauré's *Pavane* ([track](https://open.spotify.com/track/13KYgHAybnAfCnBUPjZcs2), −20.8 LUFS) and Satie's first Gymnopédie, and both sit ten to twenty decibels below the rest of this set, which would put them under the page rather than beneath it.

This set replaces three movements of Enrique Soro's *Cuarteto en La Mayor*, which carried the generation on the old concert-music basis. The Andante stays; the Allegro and the Minueto are reserved.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | The Auld Brig O' Don | Traditional Scottish | Alasdair Fraser & Paul Machlis | 2:49 | [Track](https://open.spotify.com/track/6PzslAfQ9OxA59n2fNouLh) |
| 2 | Cuarteto en La Mayor III Andante | Enrique Soro | Cuarteto Terral | 6:04 | [Track](https://open.spotify.com/track/50tY3aQ7sBGjFF65TFyMsz) |
| 3 | By the Sleepy Lagoon | Eric Coates | BBC Philharmonic, John Wilson | 4:04 | [Track](https://open.spotify.com/track/3t3IDdytTc3ZGWghDEKysi) |
| 4 | Mrs. Jamieson's Favourite | Traditional Scottish | Alasdair Fraser & Paul Machlis | 2:13 | [Track](https://open.spotify.com/track/0sTDyxDyneHm84GgZ2ZxR7) |
| 5 | Colonial Song | Percy Grainger | Martin Jones | 6:40 | [Track](https://open.spotify.com/track/1Q80Ifw9cJgKCh86PrxhHU) |

Why each track:

- The Auld Brig O' Don — a plain, unsentimental fiddle tune to open: 16 June 1892 at Coronel, a coal town on the Gulf of Arauco where every Pacific steamer had to fill her bunkers, and a match recovered from *The Chilean Times*. The coast was worked by Scottish engineers and seafaring men, and HMS *Warspite*'s crew were playing Concepción the following year.
- Cuarteto en La Mayor III Andante — the country the game kept landing in. Soro was born in Concepción, close to the first documented match, and wrote the quartet in 1903 while finishing his training in Milan. It is lyrical and it does not resolve, which is the shape of forty unconnected years.
- By the Sleepy Lagoon — English light music of 1930 for the English quarter: ten thousand of them in a Valparaíso of a hundred and ninety thousand, with Cerro Alegre, the Union Club's reading room, their own newspapers and the Sporting Club running the Chilean Derby from 1885.
- Mrs. Jamieson's Favourite — a slow air for Peter Mackay of Argyll, who opened the Valparaíso Artizan School in 1857 for the children of English, American and above all Scottish craftsmen of limited resources. It is the standing reminder that the game did not have to become the property of a class.
- Colonial Song — Grainger wrote it in 1911, an Australian in London writing about a place that was not England, and this is the quietest and longest track in the set. It carries the Grange School from 1928 and John Jackson offering the bank "the men I am shaping for Chile's future", and the clubs of the 1920s that put the house up before the union arrived to roof it.

The Scottish tracks play in 181 markets, Grainger and Soro in 185, and Coates carries no country restriction. Spotify albums: [Legacy Of The Scottish Fiddle, Volume One](https://open.spotify.com/album/7dnRrLZZ30yIZCVxAO8Bho), [Obras de Enrique Soro y Jorge Peña Hen](https://open.spotify.com/album/4ZylkScqtEFR9h7yPidloT), [Coates: Orchestral Works, Vol. 1](https://open.spotify.com/album/3bj8QSPi8FZMhg6nvDlPMw), [Grainger: The Complete Piano Music](https://open.spotify.com/album/5dF1Bd8Vlod0CcpUOPfTwo). Sources: [Fundación Enrique Soro — work page](https://fundacionenriquesoro.cl/obra/cuarteto-en-la-menor/) (the address says "la menor"; the page gives A major, 1903), [Fundación Enrique Soro — biography](https://fundacionenriquesoro.cl/fundacion/biografia/).

Spotlistr input:

```text
Alasdair Fraser & Paul Machlis - The Auld Brig O' Don
Enrique Soro, Cuarteto Terral - Cuarteto en La Mayor III Andante
Eric Coates, BBC Philharmonic - By the Sleepy Lagoon
Alasdair Fraser & Paul Machlis - Mrs. Jamieson's Favourite
Percy Grainger, Martin Jones - Colonial Song
```

### Generation 1: The Union and the First Tests (1935–1950)

Total: **20:00**. Re-checked on 22 September 2026 against the two tests and kept: five of Pedro Humberto Allende's *Doce Tonadas de Carácter Popular Chileno*, followed by one *Dolora* by Alfonso Leng, played by the Chilean pianist Oscar Gacitúa. The tonada is the popular song of the Chilean countryside, and these are its piano versions by the composer who took Chilean rural music into concert form — Allende won the National Art Prize in 1945, inside this generation. The actual popular music of these years is sung and therefore out: Los Huasos Quincheros formed in 1937, the boleros and tangos were on every radio, and none of it can go under a page. This is the same solution Uruguay's list reaches for, a generation's own music in the hands of a serious player.

The set is quiet — −19 to −22 LUFS, the softest in the book — and wide in dynamic range, so it wants a higher volume than the Chile sets around it. The tracks are calm (flux 0.50–0.62), the level is even between them, and all six play in 185 markets.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Tonada 1 | Pedro Humberto Allende | Oscar Gacitúa | 3:07 | [Track](https://open.spotify.com/track/6Zc4d1WhxbaZHRareuWYQA) |
| 2 | Tonada 2 | Pedro Humberto Allende | Oscar Gacitúa | 2:59 | [Track](https://open.spotify.com/track/5f9KlxNcjffKt115wR7hcn) |
| 3 | Tonada 3 | Pedro Humberto Allende | Oscar Gacitúa | 3:30 | [Track](https://open.spotify.com/track/146EYPAMnzUhCl1MhvkNfs) |
| 4 | Tonada 10 | Pedro Humberto Allende | Oscar Gacitúa | 4:09 | [Track](https://open.spotify.com/track/7iyXqX7I3yRZ5QSqIlM9UV) |
| 5 | Tonada 11 | Pedro Humberto Allende | Oscar Gacitúa | 4:42 | [Track](https://open.spotify.com/track/6ISt1UHxQADnQ0XFK92XaU) |
| 6 | Dolora 1 | Alfonso Leng | Oscar Gacitúa | 1:33 | [Track](https://open.spotify.com/track/25K3vc7CfqwdRMlusfRYdJ) |

Why each track:

- Tonada 1 — unhurried and searching: 20 September 1936 at Playa Ancha, Valparaíso four hundred years old, three thousand people up the hill, and a union one year old with four clubs in it.
- Tonada 2 — its quiet stretches against its livelier ones: 29–0, then 31–3, then two more defeats in Buenos Aires in 1938, and a decision to keep going anyway.
- Tonada 3 — warmer and more sure of itself: 15 June 1941, students at the Universidad de Chile founding Chunchos, the first rugby club in the country with no foreign parentage, who won their first match against the French colony's side and went up in their first season.
- Tonada 10 — broader and more developed: the inter-university championship of 1946 and the first national club championship in 1948. The ordinary furniture of a sport, arriving fifty-six years after Coronel.
- Tonada 11 — the longest and most expansive: 5 August 1948 in Buenos Aires, Chile 21, Uruguay 3, a first win at the fifth attempt, and the start of the argument that would define both countries.
- Dolora 1 — ninety seconds, sober, unfinished: a governing body founded in 1935, renamed in 1948, refounded in 1953 and not ratified until 1963, which had taken thirty years to finish being born and has since forgotten who its first president was.

Spotify album: [Tonadas de Pedro Humberto Allende, Doloras de Alfonso Leng](https://open.spotify.com/album/3LSbfKn580PZQeFzpNyva5). Sources: [Memoria Chilena — Pedro Humberto Allende](https://www.memoriachilena.gob.cl/602/w3-article-768.html), [Memoria Chilena — Allende and Chilean musical nationalism](https://www.memoriachilena.gob.cl/602/w3-article-96691.html).

Spotlistr input:

```text
Oscar Gacitúa - Tonada 1
Oscar Gacitúa - Tonada 2
Oscar Gacitúa - Tonada 3
Oscar Gacitúa - Tonada 10
Oscar Gacitúa - Tonada 11
Oscar Gacitúa - Dolora 1
```

### Generation 2: The Second Nation (1951–1971)

Total: **19:42**. Violeta Parra's guitar instrumentals, recorded for Odeón in 1957 — period repertoire, cut in the middle of this generation — with one Scottish lament placed inside it for the Campbell brothers. Parra is the Chilean music of these years that exists without a voice on it: the schools-and-country-club world that ran Chilean rugby had Los Huasos Quincheros, Pedro Messone and Lucho Gatica's boleros on the radio, and every one of those is sung, so they fail the one hard rule. Her anticuecas take the cueca, the national dance, apart and rebuild it slowly on one guitar, which suits a generation that got as far as second and no further. The level is even (−13 to −16 LUFS) and the recordings are 1957 mono, quiet and close.

Added 22 September 2026, the first Chile set built on the people-and-mood rules. Generations 0 and 1 are still on the older concert-music basis and need re-checking.

A note on Parra, since the name carries more now than it did then: she was a folklorist collecting rural song, and she died in 1967, before the coup. The nueva canción politics that later attached to the family name belong mostly to her children. Nothing in this set is a political song, and none of the sung tracks on the same compilation are used.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | El Joven Sergio | Violeta Parra | Violeta Parra | 1:36 | [Track](https://open.spotify.com/track/2ZAykQEeLLbnh37lcm1uR7) |
| 2 | Anticueca 1 | Violeta Parra | Violeta Parra | 2:19 | [Track](https://open.spotify.com/track/2KbRFKDKWu2PZVDNE6SETg) |
| 3 | Niel Gow's Lament For The Death Of His Second Wife | Niel Gow (1727–1807) | Alasdair Fraser & Paul Machlis | 4:22 | [Track](https://open.spotify.com/track/4jiF5nqQknH7qjrHHt4C9W) |
| 4 | Anticueca 2 | Violeta Parra | Violeta Parra | 4:06 | [Track](https://open.spotify.com/track/4W2e9BhYvN0UjQBHWEfhQF) |
| 5 | Anticueca 5 | Violeta Parra | Violeta Parra | 4:02 | [Track](https://open.spotify.com/track/5xzYU3MAMGGs7TF0p4fev7) |
| 6 | El Pingüino | Violeta Parra | Violeta Parra | 3:17 | [Track](https://open.spotify.com/track/7uTLLugyJ3gZVRRl5Diotg) |

Why each track:

- El Joven Sergio — the shortest and plainest opening: Ian Campbell at twenty-three, captain at the first South American Championship, and the first Chilean player this chapter can tell a story through.
- Anticueca 1 — the calmest piece on the record: Buenos Aires in 1951, and the record correcting the memory — Uruguay second, Chile third.
- Niel Gow's Lament — fiddle and piano, the one break in the guitar and the one British thread in the set. Gow wrote it for his wife in the 1800s; it is here for Donald Campbell, Ian's older brother, who played centre for Chile from 1938, volunteered as a pilot in 1941, and was killed flying with RAF Bomber Command on 12 September 1944. The chapter's empty decade sits between the two brothers, and this is the only place in it where the music stops to say why.
- Anticueca 2 — steady and unhurried: Ireland in 1952, France in 1954, the Junior Springboks in 1959, all hosted on one club's field.
- Anticueca 5 — the longest span of the five: 1958 in Santiago, Peru and Uruguay beaten, and second place behind an Argentina that was beating everyone else by fifty.
- El Pingüino — restless, and it does not resolve: the sealed roof, 54–0 at home in 1969, and the aeroplane that comes over the mountains in October 1972.

Spotify albums: [Obras para Guitarra (Parra)](https://open.spotify.com/album/5E1JJI1TdNkyDvx8ajAaoE), [Legacy Of The Scottish Fiddle, Volume One](https://open.spotify.com/album/7dnRrLZZ30yIZCVxAO8Bho). The Parra tracks play in 185 markets and the lament in 181. Several tracks on *Obras para Guitarra* are sung ("El Gavilán", "Cueca Larga", "Canto a Lo Divino", "Qué Dirá el Santo Padre") — use only the six linked above. Sources: [Museo Violeta Parra — discografía](https://www.museovioletaparra.cl/violeta-parra/obras/discografia/) (the 1957 Odeón release, MSOD/E 51020), [Memoria Chilena — Violeta Parra (1917–1967)](https://www.memoriachilena.gob.cl/602/w3-article-7683.html).

Spotlistr input:

```text
Violeta Parra - El Joven Sergio
Violeta Parra - Anticueca 1
Alasdair Fraser & Paul Machlis - Niel Gow's Lament For The Death Of His Second Wife
Violeta Parra - Anticueca 2
Violeta Parra - Anticueca 5
Violeta Parra - El Pingüino
```

### Generation 3: The Mountain and the Map (1972–1989)

Total: **21:01**. Chilean guitar music, played by José Antonio Escobar on *Guitar Music of Chile* (Naxos, recorded 2008). This is a later portrait, not period repertoire, and it is chosen deliberately. The composers — Antonio Restucci, Javier Contreras and Juan Antonio Sánchez — write from the tonada and the cueca, so the sound is Chilean and rural rather than Andean-picturesque, and the level is even (−13 to −15 LUFS) and warm.

Why not the records of the years themselves: the Chilean music of 1972–89 that would fit is either sung, which the one hard rule excludes, or unplayable. Inti-Illimani's instrumentals, the obvious candidates, are country-restricted on Spotify (the "Alturas" copies show 20 markets and 1). Illapu's *Música Andina* plays everywhere, but it is bright panpipe-and-charango music, and that is the wrong sound over an aeroplane in the mountains.

The set stays off the political axis on purpose. The same album carries Horacio Salinas's guitar suite (Salinas wrote for Inti-Illimani in exile) and Contreras's "Sentido y razón", an homage to Víctor Jara. Both are fine pieces, and neither is used. The chapter is careful to say that no rugby player appears among the dead and the disappeared and that no club has a documented political history of those years; a soundtrack of the murdered and the exiled would make a claim the prose deliberately refuses to make.

Added 22 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Arrayanes | Antonio Restucci | José Antonio Escobar | 2:46 | [Track](https://open.spotify.com/track/4VgDpAWxsU1o6MpBv7l26I) |
| 2 | Tonada del Retorno | Javier Contreras | José Antonio Escobar | 3:26 | [Track](https://open.spotify.com/track/7CjZ7hbc6fYzAzSqZfw9Vy) |
| 3 | Tonada a mi madre | Javier Contreras | José Antonio Escobar | 3:03 | [Track](https://open.spotify.com/track/7BN2JTO653GLPUmTYOB9bo) |
| 4 | La disyuntiva | Antonio Restucci | José Antonio Escobar | 4:03 | [Track](https://open.spotify.com/track/2LJJd2cRqfjWZxTA58La1i) |
| 5 | Coihues | Antonio Restucci | José Antonio Escobar | 3:35 | [Track](https://open.spotify.com/track/5lXwgTWh7vVC0kEuIIBUz1) |
| 6 | Tonada por despedida | Juan Antonio Sánchez | José Antonio Escobar | 4:08 | [Track](https://open.spotify.com/track/4l8xFXJEgrHvT2ElXlan62) |

Why each track:

- Arrayanes — the quietest opening in the chapter, named for the southern myrtle: the upper valley of the Río Azufre on 21 December 1972, an arriero moving cattle in country where almost nobody goes.
- Tonada del Retorno — a tonada of the return: the pencil and the paper wrapped round a stone, Sergio Catalán's day-long ride to the telephone at Puente Negro, and sixteen survivors coming off the mountain on the 22nd and 23rd.
- Tonada a mi madre — plain and even, and it makes no argument: the years the record goes quiet, which the chapter refuses to fill in with things it cannot source.
- La disyuntiva — "the dilemma", the piece with the most weight in it: 1983 at Newlands and Loftus, two isolated states with use for each other, and a Chilean captain who called the tour both the reason his rugby grew and a thing that happened only because the world had shut the door on both countries.
- Coihues — named for the southern beech of the timber country: forestry engineers founding Los Troncos near Concepción in 1978, San Bartolomé in La Serena in 1980, and clubs in Valdivia, Temuco and Antofagasta. The game leaves the two cities.
- Tonada por despedida — a farewell tonada to close: the founding seat at CONSUR in Asunción in October 1988, and the amateur order that produced it about to be swept away everywhere else.

All six play with no country restriction. Spotify album: [Escobar: Guitar Music of Chile](https://open.spotify.com/album/2Ju011gzftNb1PdBTXHpoj). The same album's five Violeta Parra Anticuecas are reserved to Generation 2 in Parra's own 1957 recordings, and must not be used here. Sources: [Naxos 8.570341 — Guitar Music of Chile](https://www.naxos.com/CatalogueDetail/?id=8.570341), [MusicaPopular.cl — Juan Antonio Sánchez](https://www.musicapopular.cl/artista/juan-antonio-sanchez/).

Spotlistr input:

```text
José Antonio Escobar - Arrayanes
José Antonio Escobar - Tonada del Retorno
José Antonio Escobar - Tonada a mi madre
José Antonio Escobar - La disyuntiva
José Antonio Escobar - Coihues
José Antonio Escobar - Tonada por despedida
```

### Generation 4: The Wilderness (1990–2017)

Total: **20:02**. Horacio Salinas's music for Chilean film and television, written between 1990 and 1997 and reissued digitally by Aula Records, the Universidad de Santiago's label, as *Música Imaginada vol. 2*. Salinas (born Lautaro, 1951) composed for Inti-Illimani and directs Inti-Illimani Histórico; this is the other half of his working life, the music Chileans heard for years behind other people's pictures without being told whose it was. Nine short cues, none longer than three minutes, which is the right shape for thirty years in which very little happened and it kept happening. The level moves about, as film cues do — most sit at −16 to −18 LUFS, "Soledad" and "La cueca" are 3 dB louder — but nothing here is bright or busy.

This is also the reason the Generation 3 set left Salinas's guitar suite alone. There he would have been Inti-Illimani in exile, which is a claim about rugby the chapter refuses to make. Here he is a working composer scoring Chilean television in the nineties, which is simply what the country was listening to. All nine tracks play in 185 markets.

Added 22 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Trazos de cielo sur | Horacio Salinas | Horacio Salinas | 2:24 | [Track](https://open.spotify.com/track/6WjA653Dxf2zaSe5PnGbx7) |
| 2 | Escenas mudas | Horacio Salinas | Horacio Salinas | 2:37 | [Track](https://open.spotify.com/track/2RG26tkG6h2Ivl8r3BWQNr) |
| 3 | Araucarias | Horacio Salinas | Horacio Salinas | 2:55 | [Track](https://open.spotify.com/track/49cZfw9sepPMhfBRPYZGc2) |
| 4 | La lluvia del sur | Horacio Salinas | Horacio Salinas | 2:18 | [Track](https://open.spotify.com/track/6kME4BBDPcR7JcBKqWh11F) |
| 5 | Abtao | Horacio Salinas | Horacio Salinas | 2:27 | [Track](https://open.spotify.com/track/6TgeVCJQ5n4Ce8A2ELDDkd) |
| 6 | Soledad | Horacio Salinas | Horacio Salinas | 1:46 | [Track](https://open.spotify.com/track/3bwbSlqQg2OT5JjYQyAVfG) |
| 7 | Construcción | Horacio Salinas | Horacio Salinas | 1:33 | [Track](https://open.spotify.com/track/6C8zV7MG1InQ5QGCIdNZRM) |
| 8 | La cueca | Horacio Salinas | Horacio Salinas | 2:08 | [Track](https://open.spotify.com/track/74yXFB845E7sIslXplc1pM) |
| 9 | Bicicletas | Horacio Salinas | Horacio Salinas | 1:54 | [Track](https://open.spotify.com/track/0gq3aMqf1jonX8vRm8OKNX) |

Why each track:

- Trazos de cielo sur — a short, open beginning: full membership in November 1991, which bought a seat at the qualifying table and nothing else.
- Escenas mudas — "silent scenes": eight World Cups, 1991 to 2019, all of them watched from home.
- Araucarias — the monkey puzzles of the south, for the base that was there the whole time — clubs from La Serena to Concepción, players nobody had ever trained properly.
- La lluvia del sur — patient and unhurried: amateurs with jobs and degrees to finish, assembling a few times a year.
- Abtao — steady and plain: the Americas Rugby Championship arrives in 2016 and Chile win the first match they play in it, 25–22 over Brazil.
- Soledad — nineteen consecutive defeats, and a side the others used to measure their form.
- Construcción — training twice a week for two months a year, on dirt courts sometimes too hard to use.
- La cueca — the national dance and the one bright afternoon: Parque Mahuida in 2015, Uruguay beaten 30–15, champions of South America. It is the loudest track in the set, which is the point.
- Bicicletas — ordinary movement to close: six in the morning, weights and field work before work, and a Uruguayan coach asking amateurs to change their lives.

Spotify album: [Música Imaginada vol. 2: Música para cine y televisión (1990-1997)](https://open.spotify.com/album/4tRds7vthmZG8hSWcsBgAK). Source: [Universidad de Santiago — Aula Records reissues Horacio Salinas's solo discography](https://extension.usach.cl/musica-imaginada-aula-records-reedita-la-discografia-solista-de-horacio-salinas-director-de-inti-illimani-historico/) (five volumes, two of them theatre, cinema and television music composed between 1980 and 1997).

Spotlistr input:

```text
Horacio Salinas - Trazos de cielo sur
Horacio Salinas - Escenas mudas
Horacio Salinas - Araucarias
Horacio Salinas - La lluvia del sur
Horacio Salinas - Abtao
Horacio Salinas - Soledad
Horacio Salinas - Construcción
Horacio Salinas - La cueca
Horacio Salinas - Bicicletas
```

### Generation 5: Selknam (2018–2023)

Total: **23:40**. One work, complete: Horacio Salinas's *Suite Patagonia*, six movements for orchestra, written for a ballet, premiered at the Teatro Municipal and released by Aula Records in November 2023 — two months after Chile played its first World Cup. It is about the far south: the steppe, the light, the ice, and the peoples of Tierra del Fuego. Its second movement is called "Selknam" and its last is called "Los pueblos ya no están", which is a sentence this generation has to answer for. Salinas writes tonal, melodic, folk-rooted music, not concert modernism; the movements are calm (flux 0.45–0.61) but recorded with orchestral dynamics, so set the volume on a loud passage. "La paz kawéskar" is much quieter than the rest.

**Why there is no Selk'nam music here.** The obvious move would be a recording of Hain ceremonial chant, and it is the wrong one. The Selk'nam were hunted for bounties in the nineteenth century, their descendants in the Corporación Selk'nam are still here, and their objection to the rugby franchise was precisely about being spoken for and sold rather than asked. Putting their ceremony under a reader's page as background would repeat the thing the chapter criticises. This suite is a Chilean composer's own work about the south, which is a different act.

Salinas also has Generation 4, which breaks the usual one-set-per-composer rule. The exception is deliberate: no other Chilean instrumental music of these years takes the far south as its subject, and no other work has a movement named after the franchise in the year the franchise reached a World Cup.

All six movements play in 185 markets. Added 22 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Suite Patagonia: La luz austral | Horacio Salinas | Orquesta Usach, David del Pino Klinge | 4:34 | [Track](https://open.spotify.com/track/6GnjQOgp4x3nxAckCf3vV4) |
| 2 | Suite Patagonia: Selknam | Horacio Salinas | Orquesta Usach, David del Pino Klinge | 4:23 | [Track](https://open.spotify.com/track/6aupBxZswx8CZ9JD6E1KKm) |
| 3 | Suite Patagonia: El viento y el agua | Horacio Salinas | Orquesta Usach, David del Pino Klinge | 2:27 | [Track](https://open.spotify.com/track/2tsIe6E1JpjcVAH3HOSgzj) |
| 4 | Suite Patagonia: Queulat | Horacio Salinas | Orquesta Usach, Francisco Núñez Palacios | 3:30 | [Track](https://open.spotify.com/track/14vsb8XwaOWe7H3UpBfUOd) |
| 5 | Suite Patagonia: La paz kawéskar, barcarola | Horacio Salinas | Orquesta Usach, Francisco Núñez Palacios | 4:12 | [Track](https://open.spotify.com/track/3iqB1K39VxaoVU6T9G6c8H) |
| 6 | Suite Patagonia: Los pueblos ya no están | Horacio Salinas | Orquesta Usach, David del Pino Klinge | 4:34 | [Track](https://open.spotify.com/track/4j0moGtOrRFIHjEcRTZ5lf) |

Why each movement:

- La luz austral — the southern light, and the widest opening in the chapter: November 2019, a salaried side at last, men training in daylight instead of at six in the morning before work.
- Selknam — the name and the Hain figure on the crest, worn by a sport that had answered to the Grange, Mackay and the Prince of Wales for a century; and the Corporación Selk'nam saying they were told rather than asked.
- El viento y el agua — short and moving: 4 March 2020 at the Estadio Charrúa, Peñarol beaten 15–13 away in the competition's first match, and then COVID closing the season.
- Queulat — named for the cold rainforest park in Aysén: Canada beaten 33–24 at Valparaíso in October 2021, the eighth attempt and the first win, in the port where the game came ashore.
- La paz kawéskar, barcarola — the quietest movement, a boat song for another Fuegian people: ten thousand in freezing rain at Santa Laura for a one-point defeat, and a week later a one-point win in the Colorado dusk.
- Los pueblos ya no están — "the peoples are no longer there". It carries the argument the chapter refuses to settle, and under it sits the 2023 tournament: Rodrigo Fernández's try after six minutes, thirty of the thirty-three men from a four-year-old franchise, and Ian Campbell, who saw them qualify in July 2022 and died that November without seeing them play.

Spotify album: [Música Imaginada vol. 6: Suite Patagonia (2023) + Demos en el agua](https://open.spotify.com/album/3enqBI3wb5qntrcn5l0ZwJ) — the suite is tracks 1–6; the rest of the album is demos and live takes and is not used. Sources: [Fundación Teatro a Mil — Suite Patagonia](https://teatroamil.cl/catalogo-obras/suite-patagonia/en/) (written for a ballet, premiered at the Teatro Municipal, the steppe and the ice), [Universidad de Santiago — Aula Records reissues Horacio Salinas's solo discography](https://extension.usach.cl/musica-imaginada-aula-records-reedita-la-discografia-solista-de-horacio-salinas-director-de-inti-illimani-historico/).

Spotlistr input:

```text
Horacio Salinas - Suite Patagonia: La luz austral
Horacio Salinas - Suite Patagonia: Selknam
Horacio Salinas - Suite Patagonia: El viento y el agua
Horacio Salinas - Suite Patagonia: Queulat
Horacio Salinas - Suite Patagonia: La paz kawéskar, barcarola
Horacio Salinas - Suite Patagonia: Los pueblos ya no están
```

### Generation 6: The House on the Hill (2023–2026)

Total: **19:08**. The whole of *Ale y Jorge*, a six-track EP released on 5 June 2026 — six weeks before the last scene in this chapter. It is Jorge González, the songwriter of Los Prisioneros and the defining voice of modern Chilean popular music, working with Alejandra Tapia, a viola player from the Orquesta Usach: she recorded compositions and free improvisations, he expanded and processed them. The viola carries it. Aula Records, the Universidad de Santiago's label, pressed forty ten-inch copies and put it on the platforms. The record's stated points of departure are Violeta Parra's anticuecas — which open Generation 2 of this chapter in Parra's own 1957 recordings — and Stravinsky, so the chapter's modern era begins and ends in the same place, sixty-nine years apart.

Nothing here resolves, which is why it closes a chapter that ends mid-stride. The tracks are calm (flux 0.42–0.87) and the level moves about four decibels; "Alejandra" is the loudest and busiest, "Jorge" the longest and stillest. All six play in 185 markets.

**The one set in this chapter that should be listened to before it is final.** Tapia told *La Tercera* that they were not trying to make it sound pretty, and the previews suggest processed viola drones rather than tunes. It is the right record for this generation by every other test, but if it proves abrasive under the page, the fallback is on the same label and equally current: Constanza Fuentes Landaeta's *Suite chilena*, premiered by the Orquesta Usach in 2025 and issued live in August 2026 — folk dances in orchestral form, "I. Un poco de tonada" (8:14, [track](https://open.spotify.com/track/51zWf1jpXeQJNS6NRvGbKW)) and "II. Chamamé" (4:59, [track](https://open.spotify.com/track/3VfaBJ4JuMfbFwlzXFIrCt)), with Eleonora Coloma's *Cóndor* (16:29) beside them.

Added 22 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Alejandra | Jorge González, Alejandra Tapia | Jorge González, Alejandra Tapia | 3:04 | [Track](https://open.spotify.com/track/3dGkOQk5Ac81hpd03M7egy) |
| 2 | Desazón | Jorge González, Alejandra Tapia | Jorge González, Alejandra Tapia | 1:16 | [Track](https://open.spotify.com/track/3oDvT7020igJIM0EbOTvZr) |
| 3 | Cabalgata coja | Jorge González, Alejandra Tapia | Jorge González, Alejandra Tapia | 1:56 | [Track](https://open.spotify.com/track/5vZFSEXAFVg5Y5LIJBbshO) |
| 4 | En puntillas tras de ti | Jorge González, Alejandra Tapia | Jorge González, Alejandra Tapia | 3:04 | [Track](https://open.spotify.com/track/1W5rVxwo98IrgCMa7Mmb41) |
| 5 | Sur | Jorge González, Alejandra Tapia | Jorge González, Alejandra Tapia | 2:48 | [Track](https://open.spotify.com/track/3PT4yj5ydkblpu3VTEqxnH) |
| 6 | Jorge | Jorge González, Alejandra Tapia | Jorge González, Alejandra Tapia | 7:00 | [Track](https://open.spotify.com/track/30i3vjlbRHa5BCC9WaUCjd) |

Why each track (the EP is one continuous piece of work, so these are markers rather than settings):

- Alejandra — the widest and most present: the house on the hillside at Parque Mahuida, an artificial pitch, floodlights and a permanent stand, the first home Chilean rugby has had in a hundred and thirty years.
- Desazón — a minute and a quarter of unease: September 2025, Uruguay winning the decider 46–37 on aggregate and taking the automatic berth, as they always had.
- Cabalgata coja — the quietest: the back door, and the first leg drawn 32–32 in Salt Lake City.
- En puntillas tras de ti — "on tiptoe behind you", which is what eighty years of chasing Uruguay sounds like: 27 September 2025 at the Estadio Sausalito, 21,754 people, Samoa beaten 31–12, a second World Cup.
- Sur — 18 July 2026, Georgia winning 49–22 in heavy rain in the new building, the heaviest defeat of the good new era in the house that symbolised it.
- Jorge — seven minutes that do not settle: mid-2026, fifty-odd professionals, a second franchise expected in the south, a bill for Pablo Lemoine's citizenship sitting unvoted in committee, and children for whom playing rugby for Chile is an ordinary thing to want.

Spotify album: [Ale y Jorge](https://open.spotify.com/album/7zb9sinj9BiroZKNso7IHG). Fallback album: [Cóndor / Suite Chilena (En vivo)](https://open.spotify.com/album/3cCr5HqdneR1Ok9WhItKQF). Source: [Universidad de Santiago — Alejandra Tapia and Jorge González's Aula Records album](https://www.usach.cl/news/alejandra-tapia-violista-la-orquesta-usach-colabora-jorge-gonzalez-nuevo-disco-aula-records).

Spotlistr input:

```text
Jorge González, Alejandra Tapia - Alejandra
Jorge González, Alejandra Tapia - Desazón
Jorge González, Alejandra Tapia - Cabalgata coja
Jorge González, Alejandra Tapia - En puntillas tras de ti
Jorge González, Alejandra Tapia - Sur
Jorge González, Alejandra Tapia - Jorge
```

Chile complete: Generations 0–6, all on the people-and-mood rules.

---

## Chapter 4 — Georgia

Built on 22–23 September 2026. The chapter's music problem is stated once and then worked around all the way through: **Georgia's great art is its polyphonic singing, and singing is out.** What is left is the instruments — panduri, chuniri, salamuri, duduki — and the Georgian composers who wrote the village tunes into chamber forms. The sets run:
- Taktakishvili's flute sonata, and a Paliashvili elegy, for lelo burti.
- The Armenian duduk for the Armenian from Marseille.
- Tsintsadze's miniatures on Georgian folk tunes for the Soviet machine.
- Kancheli's *Mourned by the Wind* for independence and ruin.
- Kancheli's film themes on piano for the players sent to France.
- A Georgian pianist playing the European repertoire for the billionaire's years.
- Nasidze's muted quartet for the locked door and the scandal.

Every set is instrumental. Two chapter-wide decisions: **"Suliko" is not used anywhere**, although Georgians sing it and it is not taboo there, because Stalin's fondness for it is the first thing a foreign reader will think of; and **availability was checked in Georgia itself**, which cost the chapter Lisa Batiashvili's excellent Tsintsadze arrangements, listed in 145 markets that do not include her own country.

Generations 0 and 4 were built twice. The first versions used two albums of Georgian folk instruments that turned out to be country-restricted — they do not play in South Africa, and the reader found it before the notes did. Both are archived under "Superseded selections" with the reason. The lesson is in "How sets were checked" below: an empty market list is not a promise of anything.

### Generation 0: Lelo Burti (c.1200–1928)

Total: **18:52**. Rebuilt on 23 September 2026, because the first version did not play. Otar Taktakishvili's Sonata for Flute and Piano (1968), played by Manuela Wiesler and Roland Pöntinen for BIS, with Zakaria Paliashvili's *Elegy* on Shorena Tsintsabadze's piano to open.

The flute is the reason. The village instrument of this chapter is the salamuri, the Georgian pipe, and Taktakishvili — who ran Georgian music for a generation — wrote this sonata out of Georgian folk material for the concert flute. Paliashvili is the father of Georgian national music, and the *Elegy* is the sound of the thing the chapter's first scene turns on: the winning side carrying the ball up to the cemetery and setting it on the grave of a villager who died that year.

The sonata's three movements are played in the order given, which is the composer's. The Paliashvili is about six decibels louder than the BIS recording and is placed first for that reason; the set runs from its fullest sound to its quietest. All four tracks are confirmed playable.

**The first version of this set is gone and the reason is worth keeping.** It was eleven instrumental tracks by the Mediator Duo from *Play, Panduri* (Antonovka Records, a Russian label), and every one of them is country-restricted: they will not play in South Africa, and the check that missed it — Spotify's `restrictions:country:allowed` meta tags — prints nothing at all for such tracks, which is not the same as printing "everywhere". Use `python3 tools/spotify_playlists.py check`, which asks the embed endpoint whether a track is playable and gets a straight answer.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | The Elegy | Zakaria Paliashvili | Shorena Tsintsabadze | 3:02 | [Track](https://open.spotify.com/track/1DLZlcEVqfAZcumTgwCftb) |
| 2 | Flute Sonata: I. Allegro cantabile | Otar Taktakishvili | Manuela Wiesler, Roland Pöntinen | 5:32 | [Track](https://open.spotify.com/track/4BqjhyvzF3bWCs0seQgMg8) |
| 3 | Flute Sonata: II. Aria. Moderato con moto | Otar Taktakishvili | Manuela Wiesler, Roland Pöntinen | 4:54 | [Track](https://open.spotify.com/track/2Ss4aXheaV2BVA2UbhsABT) |
| 4 | Flute Sonata: III. Allegro scherzando | Otar Taktakishvili | Manuela Wiesler, Roland Pöntinen | 5:24 | [Track](https://open.spotify.com/track/6FRMoB2C4vLVW15FjqJlNw) |

Why each track:

- The Elegy — the frame the chapter puts around everything else: a game that ends at a graveside, where the prize is not the ball but the right to give it away.
- Allegro cantabile — a pipe in the wet green hills above the Black Sea on Easter morning, and a ball packed with earth, sand, sawdust and wine, sewn shut and blessed by a priest.
- Aria — the slow middle: several hundred men locked together, the mass moving a few metres in an hour, into the stream and out of it.
- Allegro scherzando — the quickest and the most dance-like, for eight hundred documented years of it, and for the thing this generation actually hands forward: not an institution but a disposition.

Spotify albums: [The Russian Flute](https://open.spotify.com/album/1LN9gzZ5Krlbe0ghCAEXNb) (BIS, 1990), [Georgian Project](https://open.spotify.com/album/3gM9Q1aXV73shZRYeHeIlJ) (Shorena Tsintsabadze, 2024).

Spotlistr input:

```text
Shorena Tsintsabadze - The Elegy
Manuela Wiesler - Flute Sonata: I. Allegro cantabile
Manuela Wiesler - Flute Sonata: II. Aria. Moderato con moto
Manuela Wiesler - Flute Sonata: III. Allegro scherzando
```

### Generation 1: The Armenian from Marseille (1928–1963)

Total: **19:17**. The duduk, played by Djivan Gasparyan, from *I Will Not Be Sad In This World* — recorded for the Soviet label Melodiya in 1983 and reissued in the West by Brian Eno, who called it one of the most beautiful recordings he had heard. It is one double-reed pipe over a held drone, and it is the saddest patient sound in the Caucasus.

The instrument is the point. This generation is named for **Jako Haspekian**, an Armenian from Marseille who is credited with teaching Georgians the game in the first years it was politically possible; the duduk is Armenia's national instrument and, as the *duduki*, a Tbilisi one too, played in the city's urban ensembles. A Melodiya recording also puts the sound inside the state that had banned the sport in 1949 as "a game not relevant to the principles of the Soviet people". All four tracks are unrestricted.

Added 23 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | A Cool Wind Is Blowing | Traditional Armenian | Djivan Gasparyan | 4:04 | [Track](https://open.spotify.com/track/0evhabxKRo28moFOrw185S) |
| 2 | Brother Hunter | Traditional Armenian | Djivan Gasparyan | 4:06 | [Track](https://open.spotify.com/track/63FFNb1L2j9uau5VNruEuv) |
| 3 | The Ploughman | Traditional Armenian | Djivan Gasparyan | 4:49 | [Track](https://open.spotify.com/track/2ljqdI91b1PKDfO7PXjog4) |
| 4 | I Will Not Be Sad In This World | Traditional Armenian | Djivan Gasparyan | 6:18 | [Track](https://open.spotify.com/track/1lZnub6m7fBPcguZKoi7Wj) |

Why each track:

- A Cool Wind Is Blowing — 1949, and a state deciding that an English game had no place in it.
- Brother Hunter — three attempts at a club, in 1928, 1940 and 1948, each landing in a year with no use for it: the first Five-Year Plan, the eve of the invasion, the lip of the ban.
- The Ploughman — patient work in hard ground: Stalin dies in 1953, rugby is played in front of a full Luzhniki at the 1957 World Youth Games, and the category quietly changes.
- I Will Not Be Sad In This World — the longest and the turn: twenty men at a meeting in Tbilisi in October 1959, a club out of the Polytechnic, and ten clubs in five years, going up like dry grass.

Spotify album: [I Will Not Be Sad In This World](https://open.spotify.com/album/6Nnn9UWgOOKgIpoXQcQU7e). Sources: chapter text on Haspekian and the 1949 decree; [Antonovka Records](https://antonovkarecords.bandcamp.com/album/play-panduri-georgian-music-from-tbilisi) for the Tbilisi instrument names used above.

Spotlistr input:

```text
Djivan Gasparyan - A Cool Wind Is Blowing
Djivan Gasparyan - Brother Hunter
Djivan Gasparyan - The Ploughman
Djivan Gasparyan - I Will Not Be Sad In This World
```

### Generation 2: The Soviet Machine (1964–1988)

Total: **19:22**. Sulkhan Tsintsadze's *Miniatures on Georgian Folk Tunes*, played by the **Georgian State String Quartet** — the ensemble Tsintsadze himself played cello in, and the ensemble he wrote the first of them for. Georgian village melodies, written into a European chamber form, performed inside the Soviet system by Georgians: that is this generation's whole situation, stated in music. A man from Kutaisi could be among the best players in the Union and reach an international field only in a red jersey with CCCP on the chest. The tunes stayed Georgian; the frame was somebody else's.

Nine tracks from two of the quartet's recordings (1994 and 2004); they play in 182 and 185 markets, Georgia included. Two deliberate omissions. **"Suliko" is not here** — it is a love poem of 1895 that Georgians still sing, but Stalin liked it and had it broadcast, and background music cannot explain that. And Lisa Batiashvili's fine violin-and-orchestra arrangements of six of these miniatures are left alone because Spotify lists them in 145 markets, **not including Georgia**, which is no way to score a Georgian chapter.

Added 23 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | 12 Miniatures: Khasanbegura | Sulkhan Tsintsadze | Georgian State String Quartet | 1:40 | [Track](https://open.spotify.com/track/4P4YaoywJyw9mBFQQ4qQNn) |
| 2 | Miniatures: Shepherd's Dance | Sulkhan Tsintsadze | Georgian State String Quartet | 1:33 | [Track](https://open.spotify.com/track/7jgyelDTmrtAwIxUHBm4Ho) |
| 3 | 12 Miniatures: Didavoi Nana | Sulkhan Tsintsadze | Georgian State String Quartet | 2:53 | [Track](https://open.spotify.com/track/6QeNTo2n1YQvNEP5xDmayY) |
| 4 | Miniatures: Sisatura | Sulkhan Tsintsadze | Georgian State String Quartet | 3:16 | [Track](https://open.spotify.com/track/2MD9owR0AzCR7tvnbS36aM) |
| 5 | 12 Miniatures: Spring | Sulkhan Tsintsadze | Georgian State String Quartet | 3:49 | [Track](https://open.spotify.com/track/1gM3ftuYoLIdoCmyjcr9Oq) |
| 6 | Miniatures: Rural Dance | Sulkhan Tsintsadze | Georgian State String Quartet | 1:14 | [Track](https://open.spotify.com/track/2bk07GwXJjkwHl0UZegavQ) |
| 7 | 12 Miniatures: Khorumi | Sulkhan Tsintsadze | Georgian State String Quartet | 1:29 | [Track](https://open.spotify.com/track/31ee4GtkdSvhxjJiU7VcBE) |
| 8 | 12 Miniatures: Firefly - Eldfluga | Sulkhan Tsintsadze | Georgian State String Quartet | 2:27 | [Track](https://open.spotify.com/track/6aaqw2owwNAuWjQ0ziAgEl) |
| 9 | 17 Miniatures: Dance Tune | Sulkhan Tsintsadze | Georgian State String Quartet | 1:01 | [Track](https://open.spotify.com/track/2nBZ8pTB0zC3Trx6K4c3FA) |

Why each track:

- Khasanbegura — a Gurian song about a battle, to open: one republic with under two per cent of the Soviet population supplying half the Soviet XV within two years of organising.
- Shepherd's Dance — short and light-footed: the clubs multiplying under an all-Union competition.
- Didavoi Nana — a lullaby, and the quietest thing here: no Georgian anthem before a match, no Georgian selectors, no Georgian record for a man's caps to enter.
- Sisatura — the longest and most inward: twenty-five years of achievements filed under somebody else's name.
- Spring — Kutaisi, factories and river fog, and Aia coming second in the Soviet championship in 1984.
- Rural Dance — seventy-four seconds: Lokomotivi Tbilisi, a railway workers' club, lifting the Soviet Cup in 1978.
- Khorumi — the Adjaran war dance, danced by men in a line: Aia champions of the Soviet Union in 1987, and again in 1988.
- Firefly — small, bright, brief, gone.
- Dance Tune — a minute to finish on, because the finish is the point: by 1988 Georgia was a rugby nation by every measure a rugby nation uses, and had never played a match.

Spotify albums: [Shostakovich: String Quartets Nos. 2 and 3 / Tsintsadze: Miniatures](https://open.spotify.com/album/72wfm1MsfdTKj1JfZAJ8Lc), [Nasidze / Tsintsadze](https://open.spotify.com/album/0Rtv00fq7GAgwyXm4gdm2P). Both albums also carry miniatures not used here; "Firefly" appears on both, and only the 2004 recording is used.

Spotlistr input:

```text
Georgian State String Quartet - 12 Miniatures: Khasanbegura
Georgian State String Quartet - Miniatures for String Quartet: Shepherd's Dance
Georgian State String Quartet - 12 Miniatures: Didavoi Nana
Georgian State String Quartet - Miniatures for String Quartet: Sisatura
Georgian State String Quartet - 12 Miniatures: Spring
Georgian State String Quartet - Miniatures for String Quartet: Rural Dance
Georgian State String Quartet - 12 Miniatures: Khorumi
Georgian State String Quartet - 12 Miniatures: Firefly - Eldfluga
Georgian State String Quartet - 17 Miniatures: Dance Tune
```

### Generation 3: Independence and Ruin (1989–1996)

Total: **21:49**. Two movements of Giya Kancheli's *Vom Winde beweint* — "Mourned by the Wind" — a liturgy for solo viola and orchestra written in 1989, the year of the first Georgia Test, and recorded for ECM in 1992 by Kim Kashkashian with Dennis Russell Davies. Kancheli is Georgia's greatest composer and he left the country in 1991, in the middle of what this generation describes: he wrote this music on the edge of it and spent the war years abroad.

It is the most severe music in this book and it is chosen on the mood test, not for national colour. Long held string tones, silence used as material, and sudden violence in the middle of quiet — which is the decade the chapter has to tell: a first Test won in Kutaisi in September 1989, and then a coup, a civil war, a president dead at Khibula, thirteen months of war in Abkhazia and 265,000 people displaced. A reader will need the volume set on a loud passage; the dynamic range is enormous.

Movements II and III are left out to keep the set near twenty minutes. The whole work runs 37:56 and is worth hearing in one piece away from the page. Both tracks play in 184 markets, Georgia included.

Added 23 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Vom Winde beweint: I. Largo molto | Giya Kancheli | Kim Kashkashian, Orchester der Beethovenhalle Bonn, Dennis Russell Davies | 9:46 | [Track](https://open.spotify.com/track/3KKDEqhYujDNv2pKf03oPm) |
| 2 | Vom Winde beweint: IV. Andante maestoso | Giya Kancheli | Kim Kashkashian, Orchester der Beethovenhalle Bonn, Dennis Russell Davies | 12:03 | [Track](https://open.spotify.com/track/1DHAB6cfPyD0MZOkVKGrk9) |

Why each movement:

- I. Largo molto — a solo viola alone in a very large space: September 1989 in Kutaisi, Zimbabwe beaten 16–3, every one of the sixteen points scored by David Dzagnidze, and a country that had never had a team suddenly having one. The quiet is not peace; it is a held breath, and the orchestra keeps interrupting it.
- IV. Andante maestoso — the longest movement and the one that will not resolve: independence in April 1991, Gamsakhurdia overthrown by December, two years of civil war, Abkhazia, and a national side training against denim sacks and shoving old Soviet tractors because the country had nothing else to give it.

Spotify album: [Kancheli: Vom Winde beweint / Schnittke: Viola Concerto](https://open.spotify.com/album/6SK2lyszJJXMS9O6WFMS6o) (ECM New Series, 1992). Source: [ECM Records — Giya Kancheli](https://ecmrecords.com/artists/giya-kancheli/).

Spotlistr input:

```text
Kim Kashkashian - Vom Winde beweint: I. Largo molto
Kim Kashkashian - Vom Winde beweint: IV. Andante maestoso
```

### Generation 4: The French Connection (1997–2006)

Total: **20:00**. Rebuilt on 23 September 2026, because the first version did not play — see Generation 0 for the mistake and the fix. Georgian piano music from Shorena Tsintsabadze's *Georgian Project* (2024): eight of Giya Kancheli's *33 Piano Miniatures*, which are his themes for Georgian films, with Vaja Azarashvili's *Nostalgia* to open and Sandro Nebieridze's *Allegroba* to close.

Kancheli also has Generation 3, and the repetition is deliberate. There he is the concert composer whose elegy for viola and orchestra describes a country coming apart. Here he is the other thing he was, and the thing most Georgians actually knew him for: the man who wrote the tunes in *Mimino*, *Kin-dza-dza!* and *Don't Grieve*, films every Georgian household could quote. A generation of young men leaving for Montpellier and Toulon and Brive did not take a viola concerto with them. They took the music from the films.

All ten tracks are confirmed playable and play in 185 markets. The level sits between −11 and −15 LUFS, with the wide dynamic range of solo piano recorded closely.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Nostalgia | Vaja Azarashvili | Shorena Tsintsabadze | 3:05 | [Track](https://open.spotify.com/track/5XoypYe0nj81XlCFoStXQH) |
| 2 | 33 Piano Miniatures: No. 8, Mimino | Giya Kancheli | Shorena Tsintsabadze | 2:40 | [Track](https://open.spotify.com/track/77S62deltJFFt8leqbxDzK) |
| 3 | 33 Piano Miniatures: No. 22, Don't Grieve | Giya Kancheli | Shorena Tsintsabadze | 1:02 | [Track](https://open.spotify.com/track/6sT9IJUDguj8kgs005lopD) |
| 4 | 33 Piano Miniatures: No. 1, King Lear | Giya Kancheli | Shorena Tsintsabadze | 0:56 | [Track](https://open.spotify.com/track/5naY8tGZ2aC223repSIc5l) |
| 5 | 33 Piano Miniatures: No. 26, Earth, This Is Your Son | Giya Kancheli | Shorena Tsintsabadze | 1:40 | [Track](https://open.spotify.com/track/2D4Bh5EbEQv9ULe6QOIG99) |
| 6 | 33 Piano Miniatures: No. 3, When Almonds Blossomed | Giya Kancheli | Shorena Tsintsabadze | 1:56 | [Track](https://open.spotify.com/track/1T2Y5BcdS9wmKYoOIO3qxC) |
| 7 | 33 Piano Miniatures: No. 23, Bear's Kiss | Giya Kancheli | Shorena Tsintsabadze | 1:24 | [Track](https://open.spotify.com/track/1q6j0QmM6KA6TCdD4C8zTo) |
| 8 | 33 Piano Miniatures: No. 31, Sunny Night | Giya Kancheli | Shorena Tsintsabadze | 1:05 | [Track](https://open.spotify.com/track/6XhPykxlsQrVx0EpbShmpU) |
| 9 | 33 Piano Miniatures: No. 33, Romeo and Juliet | Giya Kancheli | Shorena Tsintsabadze | 2:46 | [Track](https://open.spotify.com/track/74UwSlPNr142OaqEQ7D8Qk) |
| 10 | Allegroba | Sandro Nebieridze | Shorena Tsintsabadze | 3:26 | [Track](https://open.spotify.com/track/796Vzb0uk9xTlxE8cueVfp) |

Why each track:

- Nostalgia — Claude Saurel's decision, stated in one word: the fastest way to make Georgia good was to send the players away and let French clubs make them.
- Mimino — Kancheli's theme for the film about a Georgian who leaves home to fly somewhere else and cannot settle. There is no better two and a half minutes for this generation.
- Don't Grieve — a minute, for the 1999 repechage: beaten in Nuku'alofa, 28–27 up in Tbilisi, and out on aggregate.
- King Lear — short and dark: a union with no money, in a country still recovering.
- Earth, This Is Your Son — 2001, the European championship, the first trophy Georgia ever won.
- When Almonds Blossomed — 2003 in Australia: four matches against the best on earth, one try, minus 154 points, and a better problem than the one they had in 1993.
- Bear's Kiss — the defeat by Uruguay, the one they might have won.
- Sunny Night — sixty-five seconds: a colony of Georgian professionals settling into the French leagues.
- Romeo and Juliet — two households: the Yachvili brothers, a grandfather who fought at Stalingrad and settled in Corrèze, and two grandsons who chose different countries.
- Allegroba — a young Georgian composer, born long after all of it, to close on what the pipeline was for.

Spotify album: [Georgian Project](https://open.spotify.com/album/3gM9Q1aXV73shZRYeHeIlJ). The album also carries Tsintsadze's piano preludes and Machavariani's "Khorumi", both left alone: Tsintsadze has Generation 2, and the khorumi is already danced there.

Spotlistr input:

```text
Shorena Tsintsabadze - Nostalgia
Shorena Tsintsabadze - 33 Piano Miniatures: No. 8, Mimino
Shorena Tsintsabadze - 33 Piano Miniatures: No. 22, Don't Grieve
Shorena Tsintsabadze - 33 Piano Miniatures: No. 1, King Lear
Shorena Tsintsabadze - 33 Piano Miniatures: No. 26, Earth, This Is Your Son
Shorena Tsintsabadze - 33 Piano Miniatures: No. 3, When Almonds Blossomed
Shorena Tsintsabadze - 33 Piano Miniatures: No. 23, Bear's Kiss
Shorena Tsintsabadze - 33 Piano Miniatures: No. 31, Sunny Night
Shorena Tsintsabadze - 33 Piano Miniatures: No. 33, Romeo and Juliet
Shorena Tsintsabadze - Allegroba
```

### Generation 5: The Billionaire (2007–2018)

Total: **19:44**. Khatia Buniatishvili's *Motherland* (Sony Classical, 2014), recorded inside this generation by the Georgian pianist who had become one of the most visible classical musicians in the world. The album is mostly other people's music — Brahms, Liszt, Grieg, Pärt — with one Georgian folk song she arranged herself, and that proportion is the point.

This is the generation in which a Georgian could reach the very top of European rugby as an individual while his country stayed locked out of it. Mamuka Gorgodze won the European Champions Cup with Toulon in May 2015 and went back in the autumn to a national side that was not allowed to play any of the countries whose clubs he had just beaten. A Georgian at the centre of the European repertoire, with her own country's tune sitting in the middle of the programme, is the same shape. Bidzina Ivanishvili's £80 million and fourteen high-performance centres bought everything except a fixture list.

All five tracks play in 185 markets. Kancheli's "When Almonds Blossomed", also on this album, is left for Generation 3's composer.

Added 23 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Vagiorko mai / Don't You Love Me? | Traditional Georgian, arr. Buniatishvili | Khatia Buniatishvili | 2:37 | [Track](https://open.spotify.com/track/5OtDFCLmKXeAnCYPOFwPTb) |
| 2 | Wiegenlied, S. 198 | Franz Liszt | Khatia Buniatishvili | 3:10 | [Track](https://open.spotify.com/track/57LKrlkcjnnu7xr8BtYbcX) |
| 3 | Intermezzo in B-Flat Minor, Op. 117/2 | Johannes Brahms | Khatia Buniatishvili | 5:10 | [Track](https://open.spotify.com/track/47A9aMuFvuUGvELlMh1gpL) |
| 4 | Lyric Piece in E Minor, Op. 57/6: Homesickness | Edvard Grieg | Khatia Buniatishvili | 3:44 | [Track](https://open.spotify.com/track/6pMdVwcO9Dqr3O9AqAIqNB) |
| 5 | Für Alina in B Minor | Arvo Pärt | Khatia Buniatishvili | 5:03 | [Track](https://open.spotify.com/track/6ZQcMXyYlQlBr9kqjiL6KR) |

Why each track:

- Vagiorko mai — the Georgian song, played by a Georgian, first: Bordeaux in September 2007, seventy-eight minutes gone, the maul over the Irish line and Denis Leamy's body under the ball.
- Wiegenlied — Liszt's cradle song, small and even: eleven days later at Lens, Namibia beaten 30–0, the first World Cup win in the country's history.
- Intermezzo in B flat minor — Brahms at his most withheld: the money arriving, fourteen high-performance centres in a country of under four million, and nothing to spend it on but the same opponents.
- Homesickness — Grieg's title, and Gorgodze's situation: sixteen years of international rugby, 168 games for Montpellier, 110 for Toulon, a Champions Cup, and a national side nobody would play.
- Für Alina — Pärt, two hands, almost nothing, no resolution: the locked door. Winning the second tier of Europe earns the right to win it again.

Spotify album: [Motherland](https://open.spotify.com/album/1QlwdrB0YycnoWOH1JqCqh).

Spotlistr input:

```text
Khatia Buniatishvili - Vagiorko mai
Khatia Buniatishvili - Wiegenlied, S. 198
Khatia Buniatishvili - Intermezzo in B-Flat Minor, Op. 117/2
Khatia Buniatishvili - Lyric Piece in E Minor, Op. 57/6: Homesickness
Khatia Buniatishvili - Für Alina
```

### Generation 6: The Locked Door and the Scandal (2019–2026)

Total: **20:04**. One work: **Sulkhan Nasidze's String Quartet No. 5, "Con Sordino"**, played by the Georgian State String Quartet. Nasidze (1927–1996) is the other great Georgian quartet composer of the Soviet century, and the title is the instruction that governs the piece — *with the mute on*, the whole way through. Muted strings for twenty minutes: the sound is there, the players are working, and something is stopping it reaching full voice.

Nothing else in the chapter's music is as exact about this generation. Georgia beat Wales in Cardiff in November 2022, on a Luka Matkava penalty at seventy-eight minutes, and Sky Sports called it one of the greatest upsets in the sport's history — and the reward was the same as always. A presidential election settled by a state registry agency and a single approved candidate. A World Cup in France with no wins and a draw against Portugal. Then Operation Obsidian: seven people banned, up to eleven years, sample substitution before the 2023 tournament, and a national anti-doping agency implicated in it. A generation that produced the country's finest result and could not make itself heard.

The piece plays in 182 markets, Georgia included. It is a single track, so there is nothing to shuffle; it is also the most demanding set in this chapter, and a reader who wants an easier twenty minutes should take Generation 4 instead.

Added 23 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | String Quartet No. 5: "Con Sordino" | Sulkhan Nasidze | Georgian State String Quartet | 20:04 | [Track](https://open.spotify.com/track/0vUt8SVq1IjnN6D7WcG6j7) |

Spotify album: [Nasidze / Tsintsadze (String Quartet No. 5 / String Quartet No. 6)](https://open.spotify.com/album/0Rtv00fq7GAgwyXm4gdm2P). The same performance was reissued in July 2025 on [Georgian Classical Visions](https://open.spotify.com/album/2DRlr5CowXHbL0viLqzbKB), which also carries Nasidze's Quartet No. 3, "Epitaphie" — the obvious alternative if this one is wanted for another purpose, and a fair description of the same events.

Spotlistr input:

```text
Georgian State String Quartet - String Quartet No. 5: Con Sordino
```

Georgia complete: Generations 0–6. Next chapter: Romania.

---

## Chapter 5 — Romania

Built on 23 September 2026. This chapter has the opposite problem to Georgia's. Georgia's great music is choral and the rule put it out of reach; Romania's is instrumental almost all the way down — the lăutari bands, the doina on a shepherd's pipe, the cimbalom — so the no-vocals rule costs the chapter almost nothing. What it costs instead is variety of source. Romania's concert tradition runs through one man to a degree no other chapter in this book has to deal with, and the sets say so rather than pretend otherwise. **George Enescu appears in three of the seven** — the violin sonata of 1926, the last string quartet of 1953, the Rhapsody transcribed for one piano — and the reason is that the chapter's own thesis is a cord running to Paris and back, and Enescu's life is that cord: a Romanian in Paris writing village music into a French form, then a Romanian in Paris with no Romania to go back to, then his showpiece played alone by a woman who also left. Three different compositions, so the reuse rule holds; the one-composer preference is bent on purpose, as it was for Salinas in Chile and Kancheli in Georgia.

The sets run:

- Enescu's Third Violin Sonata, played by Enescu's pupil, for the ball that came from Paris.
- Lipatti — Bucharest bourgeoisie, dead at thirty-three — for the class the state abolished.
- Toni Iordache's cimbalom for the years the state paid for everything.
- Zamfir's panpipes for the door that did not open, closing on a funeral lament for the five dead of December 1989.
- Enescu's last quartet, finished in exile, recorded in Iași and released in 2001, for the delay.
- The Romanian Rhapsody as one woman at one piano, for the ranking that lied.
- A Romanian, an Englishman and an American playing Transylvanian village songs, for a squad less than half of which was born in the country.

Three chapter-wide decisions. **The Ceaușescu-era mass songs and the *Cântarea României* repertoire are not used anywhere**, per the care list; nothing in these seven sets comes from that machinery, although Generations 2 and 3 both come from state labels and state-approved artists, which is said in the sets themselves rather than hidden. **Availability was checked in South Africa**, as everywhere since Georgia: all thirty-one tracks return `isPlayable` and play in ZA. And **the sets are ordered loudest to quietest** where the music allows; inside a single multi-movement work, score order wins, as it did for the Taktakishvili sonata in Georgia.

Rejected on the rules, and worth recording because two of them were nearly written in:

- **Balanescu Quartet, *Luminitza* (Mute, 1994).** The obvious record for Generation 4 and the most painful loss in the chapter: Alexander Bălănescu is a Romanian émigré in London and the album is *about* December 1989 and the decade after it. It carries spoken word. Bălănescu speaks over "Democracy" and "Revolution", there are fragments of all four players talking on "Still With Me", and "Link" is a recorded Romanian speech that reviewers take to be Ceaușescu himself. The instrumental remainder — "East", the sixteen-minute title track, "Mother" — does not hold together on level (−13.1 against −18.6 and −19.7), and "Mother" could not be cleared. Out under the no-vocals rule. See the care list.
- **Lucian Ban & Mat Maneri, *Oedipe Redux* (2023).** Enescu's opera remade by a Romanian and an American, which would have bookended the chapter perfectly against Generation 0. Spotify credits two musicians; the record is a septet with two vocalists, Jen Shyu and Theo Bleckmann. Out, and a reminder that a Spotify credit is not a personnel list.
- **Trei parale.** A Bucharest group reviving near-extinct lăutari instruments, thematically ideal for Generation 6. They have a singer, and which tracks he is on cannot be established from titles. Held back rather than risked.
- **Zamfir, *The Lonely Shepherd* (the album).** Easy-listening covers of Albinoni, Bach and Puccini, not Romanian repertoire. The Cellier recordings on *Les flûtes roumaines* are the real thing and are what Generation 3 uses.
- **Constantin Brăiloiu's field recordings.** Mostly sung, lo-fi, and wildly variable in level.

### Generation 0: The Ball from Paris (c.1900–1930)

Total: **23:55**. One work: **Enescu's Violin Sonata No. 3 in A minor, Op. 25, "dans le caractère populaire roumain" (1926)**, played by **Yehudi Menuhin** with his sister **Hephzibah Menuhin** at the piano, recorded 1966.

The generation's founding fact is that the ball came overland in a student's luggage from Paris, and that there is not one Englishman anywhere in the story. This sonata is the same journey, made by a musician instead of a ball. Enescu was a Romanian in Paris; what he wrote in 1926 is a recital sonata — the most French of forms, the thing you play in a salon — filled with a lăutar's improvising, the drone of a village band, a doina stretched out over a piano that behaves like a cimbalom. He marked the score *in the Romanian folk character* so that nobody could mistake what it was. That is Stadiul Român in 1913 exactly: not an English club copied, but the French copy of an English game, brought home and admired.

The performers close the circle. Menuhin became Enescu's pupil in Paris in 1927, the year after the piece was written, and spent the rest of his life saying that Enescu was the most extraordinary human being he had known. He is playing his teacher's music, with his own sister, forty years later.

Two notes for whoever builds the playlist. The first movement is marked *Moderato malinconico*, and the whole sonata is darker and slower than a reader expecting folk-fiddle colour will assume — which suits a generation whose first international was a 21–0 defeat and whose trophy is a bronze medal for finishing third of three. And the album link is a surprise: these three movements sit as tracks 4–6 of **Ravi Shankar's *West Meets East* (1966)**, the Shankar–Menuhin record. Click it and you land on a sitar album. The tracks are the tracks; the playlist is built from ids, so it does not matter.

Levels are close and low: −18.3, −17.0, −17.2 LUFS.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Violin Sonata No. 3 in A Minor, Op. 25: I. Moderato malinconico | George Enescu | Yehudi Menuhin, Hephzibah Menuhin | 8:23 | [Track](https://open.spotify.com/track/36inPmRSmlMluAEjFWjPE7) |
| 2 | Violin Sonata No. 3 in A Minor, Op. 25: II. Andante sostenuto e misterioso | George Enescu | Yehudi Menuhin, Hephzibah Menuhin | 8:19 | [Track](https://open.spotify.com/track/5rBKvKoe12AUZo09oxYvfE) |
| 3 | Violin Sonata No. 3 in A Minor, Op. 25: III. Allegro con brio, ma non troppo mosso | George Enescu | Yehudi Menuhin, Hephzibah Menuhin | 7:13 | [Track](https://open.spotify.com/track/0mk3o9BFDCA7pASvZvmw7A) |

Why each track:

- I. Moderato malinconico — the suitcase. Village material inside a Parisian form, and the movement is marked melancholy, not festive.
- II. Andante sostenuto e misterioso — the thin paper trail: play around 1900, a club in 1913, and nothing anyone can date properly in between.
- III. Allegro con brio — Colombes, 4 May 1924. Thirteen tries against them, four to a Stade Français winger, and a medal anyway.

Spotify album: [West Meets East](https://open.spotify.com/album/6KPrm39h0YHIisL8sBkYhC) (EMI/Angel, 1966) — tracks 4–6.

Spotlistr input:

```text
Yehudi Menuhin - Enescu: Violin Sonata No. 3 in A Minor, Op. 25: I. Moderato malinconico
Yehudi Menuhin - Enescu: Violin Sonata No. 3 in A Minor, Op. 25: II. Andante sostenuto e misterioso
Yehudi Menuhin - Enescu: Violin Sonata No. 3 in A Minor, Op. 25: III. Allegro con brio, ma non troppo mosso
```

### Generation 1: The Works Team (1931–1948)

Total: **21:19**. **Dinu Lipatti**, played by **Luiza Borac** on *Piano Music of Dinu Lipatti* (Avie, 2012). Solo piano throughout.

This generation ends with a class ceasing to exist, and Lipatti is that class. Born in Bucharest in 1917 into a wealthy musical family, godson of Enescu, finished in Paris with Cortot and Dukas, the exact social material that founded Stadiul Român and sent its sons to France. He left Romania in 1943, never returned, and died in Geneva in 1950 at thirty-three. Everything his family had was taken by the government that, in the same years, decided to keep the rugby clubs running.

The pieces carry the generation's dates without being asked to. The **Piano Sonata in D minor** is from 1932, the year after Caracostea's commission became a federation, written by a boy of fifteen — a whole Romantic sonata composed in a Bucharest drawing room in the last decade in which such a room existed. The **Sonatine for the Left Hand** is from 1941, with Romania in the Axis and its armies going east; a sonatina for one hand, written while a country fought a war it would later fight on the other side. The **Nocturne in A minor** is *On a Moldovan Theme* — and northern Bukovina and Bessarabia had been taken by the Soviet Union in 1940, which is one of the things the war was presented at home as recovering. The **Nocturne in F-sharp minor** is dedicated to **Clara Haskil**, Romanian-born, Jewish, who also left and also became somebody else's pianist.

Mood: nothing here celebrates, and nothing here is about a factory. That is deliberate. The works team at Brașov is the fact this generation turns on, but it is a fact with no music attached to it — a claim thinner than its importance, as the chapter says — and the sound of the generation is the drawing room going quiet.

The set is ordered by level and ends very soft: −18.7, −20.0, −23.9, −22.4, −22.2, then −28.2 for the closing nocturne, which is the quietest track in the chapter. It is the closer for exactly that reason; a reader who finds it too far down should stop after the Moldovan nocturne, at 16:22.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Piano Sonata in D Minor (1932): II. Andante | Dinu Lipatti | Luiza Borac | 3:57 | [Track](https://open.spotify.com/track/6IMIzFiJDp8inTouReip5k) |
| 2 | Sonatine for the Left Hand (1941): I. Allegro | Dinu Lipatti | Luiza Borac | 2:28 | [Track](https://open.spotify.com/track/3TlG2R4gI7RwjD5imMaQI0) |
| 3 | Sonatine for the Left Hand (1941): II. Andante espressivo | Dinu Lipatti | Luiza Borac | 3:17 | [Track](https://open.spotify.com/track/48IEbldS6HWQAKgh90SVWj) |
| 4 | Sonatine for the Left Hand (1941): III. Allegro | Dinu Lipatti | Luiza Borac | 3:01 | [Track](https://open.spotify.com/track/3PEQcbCj0ejBa1qbvCal8B) |
| 5 | Nocturne in A Minor (On a Moldovan Theme): Moderato | Dinu Lipatti | Luiza Borac | 3:39 | [Track](https://open.spotify.com/track/3W7ak9v17aZjamoY6kDSnp) |
| 6 | Nocturne in F-sharp Minor, Op. 6 (Dedicated to Clara Haskil): Andante, ma non troppo | Dinu Lipatti | Luiza Borac | 4:57 | [Track](https://open.spotify.com/track/0lPzDNUWgPzUr5eSHI8TRk) |

Why each track:

- Piano Sonata, II. Andante — 1932. A federation with a stamp and an address, governing one city, and a fifteen-year-old writing a sonata in it.
- Sonatine, I–III — 1941, one hand. The war Romania fought on both sides, and what the country did in it.
- Nocturne on a Moldovan Theme — the provinces lost in the summer of 1940, played as a tune rather than a grievance.
- Nocturne in F-sharp Minor — dedicated to Clara Haskil. Two Romanian pianists who left and did not come back, and the set ends on the quieter of them.

Spotify album: [Piano Music of Dinu Lipatti](https://open.spotify.com/album/26j9kFfnGorArwGMGwS0KC) (Avie, 2012). If the whole **Piano Sonata in D minor** is wanted instead — one work, 22:13, level-consistent at −15.1/−18.7/−15.8 — it is [I. Allegro moderato](https://open.spotify.com/track/74nRegmeUlo2LY6UNFRVHB) and [III. Allegro](https://open.spotify.com/track/5z4BXS5YUwI2eScg6lusLP) either side of the Andante above. It is the better-built set and the worse-fitting one: it says nothing about the war.

Spotlistr input:

```text
Luiza Borac - Piano Sonata in D Minor (1932): II. Andante
Luiza Borac - Sonatine for the Left Hand (1941): I. Allegro
Luiza Borac - Sonatine for the Left Hand (1941): II. Andante espressivo
Luiza Borac - Sonatine for the Left Hand (1941): III. Allegro
Luiza Borac - Nocturne in A Minor (On a Moldovan Theme): Moderato
Luiza Borac - Nocturne in F-sharp Minor, Op. 6 (Dedicated to Clara Haskil): Andante, ma non troppo
```

### Generation 2: Because It Was Amateur (1949–1969)

Total: **19:48**. **Toni Iordache**, cimbalom, from *Toni Iordache — țambal, Vol. 1* (Electrecord, compiled 1996).

This is the one bright set in the chapter, and it should be. The generation is the world-record crowd — ninety-five thousand in Bucharest in May 1957 — and the first win over France in 1960, and a country deliberately organised: works clubs, army clubs, railway clubs, a pathway that cost a schoolboy nothing.

Toni Iordache (1942–1988) is that system's other product. A Roma lăutar from a family of lăutari, he became the greatest cimbalom player Romania has produced, and he became it inside the same machinery that was giving prop forwards jobs at the aircraft works so they could remain amateurs on paper: state conservatoire training, a state orchestra, and Electrecord, the state label, recording him. The parallel is exact and it is not flattering to either side. A government decided which folk music was national, paid for it, and pointed at the results; a government decided rugby was worth keeping, paid for it, and pointed at the results.

Two honesties. The recordings are from the 1960s and 1970s rather than from 1957, so this is the sound of the radio across the whole state period rather than a document of the crowd; and the hore and sârbe here are dance tunes, which makes this the closest the chapter comes to a beat. At cimbalom volume the fast playing reads as ornament rather than pulse, but a reader who wants stillness should take Generation 4 instead. Levels sit tightly around −14 LUFS, which is the loudest even block in the chapter after the quartet.

The political check is clean and worth stating, because the care list flags this chapter. Iordache is not *Cântarea României*: he is a working lăutar playing repertoire that predates the regime by a century, and Romanian television still plays him. He died in 1988, a year before the revolution, and his reputation survived it intact.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Horă | Traditional | Toni Iordache | 4:45 | [Track](https://open.spotify.com/track/1T4FegRfDdSO1jZiqyqfSV) |
| 2 | Sârba de la Medgidia | Traditional | Toni Iordache | 3:24 | [Track](https://open.spotify.com/track/3FjzIMLjYqdmOPr21zt75V) |
| 3 | Cântec de ascultare și Breaza | Traditional | Toni Iordache | 2:36 | [Track](https://open.spotify.com/track/68R5gPSw4rdiHHUrgiwg34) |
| 4 | Călușul | Traditional | Toni Iordache | 2:26 | [Track](https://open.spotify.com/track/0MUCySUID2idc6LNaHytzv) |
| 5 | Horă moldovenească | Traditional | Toni Iordache | 2:22 | [Track](https://open.spotify.com/track/00BvcTOIQrXSykPuLNgVAH) |
| 6 | Hora de la Rudari | Traditional | Toni Iordache | 2:19 | [Track](https://open.spotify.com/track/5YFYwJiLdeuvxRr7wc44nG) |
| 7 | Hora lăutarilor | Traditional | Toni Iordache | 1:56 | [Track](https://open.spotify.com/track/3gJG6JcR116R7bLmb9DO1X) |

Why each track:

- Horă — the longest and the fullest, and the horă is the round dance everybody is in. Ninety-five thousand people.
- Sârba de la Medgidia — a Dobrudja tune. The game left one city in this generation and went where the factories were.
- Cântec de ascultare și Breaza — a *cântec de ascultare* is a listening song, the slow half of a lăutar's set. The 5–5 draw at Bayonne, the 3–0, the 6–6 at Toulouse: the years of holding on.
- Călușul — the men's stamping dance, done in a line, and the oldest thing on the record. A pack.
- Horă moldovenească — Penciu's points and Barbu's try, 11–5, the first time in forty-seven years of trying.
- Hora de la Rudari — *rudari* were the woodworkers. A works team.
- Hora lăutarilor — the players' own tune, and the shortest. Irimescu kicking every one of Romania's fifteen points against France in 1968, and then the machine's forty-year bargain running out.

Spotify album: [Toni Iordache — țambal, Vol. 1](https://open.spotify.com/album/2cnqAnopgTfocRuwEgHP10) (Electrecord).

Spotlistr input:

```text
Toni Iordache - Horă
Toni Iordache - Sârba de la Medgidia
Toni Iordache - Cântec de ascultare și Breaza
Toni Iordache - Călușul
Toni Iordache - Horă moldovenească
Toni Iordache - Hora de la Rudari
Toni Iordache - Hora lăutarilor
```

### Generation 3: The Door That Did Not Open (1970–1989)

Total: **20:43**. **Gheorghe Zamfir** and **Simion Stanciu**, nai and panpipes, from *Les flûtes roumaines* (1986) — the Marcel Cellier recordings.

Zamfir is the one Romanian the world let in during precisely the years the Five Nations would not. Cellier, a Swiss organist, recorded him; the records sold across Western Europe; the nai turned up in films and on television until a Romanian shepherd's instrument was something a French or German household could hum. In the same two decades Romania beat France seven times, beat Scotland's Grand Slam champions in Bucharest and Wales at Cardiff Arms Park, and was never once asked into the tournament. The country could export a panpipe player. It could not get a fixture list.

The instrument is right for a second reason. The nai is what the doina is played on — the long, unmeasured, wandering lament of the Romanian countryside, which does not have a beat and does not resolve. That is the sound of a generation that was good enough for thirty years and spent them waiting.

And the set ends where the generation ends. **"Bocet"** is a *bocet*: the funeral lament, the form performed over a body at a Romanian village wake. It is here for the last week of December 1989 — Petre Astafei, Bogdan Stan, Florin Butirii, Radu Durbac, Florică Murariu. Five players in three days, three from the railwaymen's club and two from the army club, one of them a serving major shot by the army that employed him so that he could remain, on paper, an amateur. The lament is the closer and nothing follows it.

Levels: −17.4, −19.9, −20.8, −18.5, −19.0. The order is not a clean descent, because the closer is fixed by the story rather than by the meter.

The political note this set needs: Zamfir toured the West with the state's permission, and the regime was pleased to have him there. He is not regime repertoire — he is a virtuoso on a peasant instrument playing music older than the party — but he got out because it suited Bucharest to let him, and that is the same arrangement the rugby team was under.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Suita de melodii din maramureș | Traditional | Gheorghe Zamfir, Simion Stanciu | 6:38 | [Track](https://open.spotify.com/track/5ZEhKl6IkZqA2b8FACZ92l) |
| 2 | Cîntecul jianului | Traditional | Gheorghe Zamfir, Simion Stanciu | 3:11 | [Track](https://open.spotify.com/track/3UOwt8nxy2mUAF4VSzmwsW) |
| 3 | Doina oltului și hora | Traditional | Gheorghe Zamfir, Simion Stanciu | 3:04 | [Track](https://open.spotify.com/track/6i2T8OZNherF07M1r5Gsit) |
| 4 | Piatra, piatra | Traditional | Gheorghe Zamfir, Simion Stanciu | 4:17 | [Track](https://open.spotify.com/track/0A6prCrUYcu3nFpP4xnt9u) |
| 5 | Bocet | Traditional | Gheorghe Zamfir, Simion Stanciu | 3:33 | [Track](https://open.spotify.com/track/4RhBJrpUPIZpgwWwy6Ktu4) |

Spotify lists tracks 2 and 4 as "Cintecul jianvlui" and "Piatra, piatra de: E piatra…", which are mistranscriptions; the names above are the tunes. Search by id.

Why each track:

- Suita de melodii din maramureș — Maramureș, the far north. The generation the state built reaching its furthest point.
- Cîntecul jianului — Iancu Jianu was an outlaw who robbed boyars, and every lăutar in Romania has played his song. The rumour about the winter break, and the grievance under it that was entirely real.
- Doina oltului și hora — a doina and then a horă: the lament and then the dance. The two tries disallowed against the All Blacks, and the hundred points at Burgas.
- Piatra, piatra — a stone. Full membership of the game's governing body, arriving in November 1987, five months after the invitation that made it necessary.
- Bocet — the funeral lament, for the five. 22–24 December 1989.

Spotify album: [Les flûtes roumaines](https://open.spotify.com/album/7aSj6r81q7H9XWRTsln4O2) (1986).

Spotlistr input:

```text
Gheorghe Zamfir - Suita de melodii din maramures
Gheorghe Zamfir - Cintecul jianvlui
Gheorghe Zamfir - Doina oltului si hora
Gheorghe Zamfir - Piatra, piatra de: E piatra...
Gheorghe Zamfir - Bocet
```

### Generation 4: The Delay (1990–2001)

Total: **19:19**. Three movements of **Enescu's String Quartet No. 2 in G major, Op. 22 No. 2**, played by the **Ad Libitum Quartet** (Naxos, released March 2001).

This is the last thing Enescu finished. He completed it in Paris in 1953, having left Romania in 1946 and understanding that he would not be going back; he died in Paris in 1955, while the house he had lived in in Bucharest became a state museum. A man on the wrong side of a closed border, still writing his country's music, with no country to send it to. The generation is eighty-odd players draining west along the same channel the game had come east on — the cord that fed it becoming the cord that bled it — and this is what that sounds like from the far end.

The recording belongs to the generation too, which is the part that settled it. The Ad Libitum Quartet is four players out of the Enescu academy in **Iași**; they recorded the two quartets for Naxos in the late 1990s, in the decade the chapter describes, and the disc was issued in **March 2001** — eight months before Twickenham. Romanian musicians doing careful work on Romanian music, in a country that could not heat its hospitals.

Three movements of four. The fourth is the *Con moto — Energico* finale: it is the loudest thing on the disc and it resolves, and neither is right for a generation whose whole point is that nothing arrived on time and nothing was concluded. The set stops before it. A reader who wants the complete quartet should add [IV. Con moto — Molto moderato, Energico](https://open.spotify.com/track/3TK5sI7mHsNeahDuBDWpMb), 8:11, which takes the set to 27:30.

One warning. At −10.3, −9.8 and −12.3 LUFS this is by a long way the loudest set in the chapter, mastered close, and it follows a panpipe set that sits nine decibels below it. Do not run Generation 3 into Generation 4 without touching the volume.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | String Quartet No. 2 in G Major, Op. 22, No. 2: I. Molto moderato | George Enescu | Ad Libitum Quartet | 5:57 | [Track](https://open.spotify.com/track/3W0CQOEK2riW1yxfq2GzXc) |
| 2 | String Quartet No. 2 in G Major, Op. 22, No. 2: II. Andante molto sostenuto ed espressivo | George Enescu | Ad Libitum Quartet | 9:20 | [Track](https://open.spotify.com/track/2Ingzuv1p9DKBsdkoWTGH8) |
| 3 | String Quartet No. 2 in G Major, Op. 22, No. 2: III. Allegretto non troppo mosso | George Enescu | Ad Libitum Quartet | 4:02 | [Track](https://open.spotify.com/track/2Oxop6rz9OFlzucTpJKWcK) |

Why each track:

- I. Molto moderato — the afterglow. Scotland beaten 18–12 at the Dinamo stadium in August 1991, twenty months after the revolution, by men out of academies that no longer existed.
- II. Andante molto sostenuto ed espressivo — nine minutes of the slow movement, which is the generation. The pipeline dies immediately and the results do not show it for a decade.
- III. Allegretto non troppo mosso — Newlands, 30 May 1995, and the vote in Paris three months later that made the game professional. The set stops here, unresolved, because so does the generation.

Spotify album: [Enescu: String Quartets Nos. 1 and 2](https://open.spotify.com/album/5xBiDHyW3TaRyVhuc9CVSX) (Naxos 8.554721, 2001).

Spotlistr input:

```text
Ad Libitum Quartet - String Quartet No. 2 in G Major, Op. 22, No. 2: Molto moderato
Ad Libitum Quartet - String Quartet No. 2 in G Major, Op. 22, No. 2: Andante molto sostenuto ed espressivo
Ad Libitum Quartet - String Quartet No. 2 in G Major, Op. 22, No. 2: Allegretto non troppo mosso
```

### Generation 5: The Ranking That Lied (2002–2017)

Total: **22:46**. **Mihaela Ursuleasa**, piano, from *Romanian Rhapsody* (Berlin Classics, 2011): Enescu's **Romanian Rhapsody No. 1** in the solo-piano version, then **Paul Constantinescu's Suite for Piano**.

The Rhapsody is the national showpiece. It is the piece every Romanian knows, an orchestra's worth of village tunes piled up and set off like a firework, and the version here is one woman at one piano doing all of it herself. That is this generation to the decimal place. Thirteenth in the world in October 2003, twenty-three months after conceding a hundred and thirty-four points — a number that sounded like a rugby nation and was in fact a handful of very good men with nothing whatever behind them. Florin Vlaicu played 129 Tests and kicked 1,030 points for a country with no league and no academies. Cătălin Fercu scored thirty-three tries for a side that spent most of its life defending. A record-breaking career held together that long is usually a tribute; here it is a diagnosis, and so is a transcription that makes one pianist do the work of a hundred players.

Ursuleasa makes it sharper than any argument could. She was born in **Brașov** in 1978 — the aircraft-works city where the first club outside Bucharest was formed in 1939, the town this chapter's whole social claim rests on — left for Vienna at seventeen, built a career there, and died in Vienna in 2012, aged thirty-three. A Romanian who went west because that was where the work was, held up alone, and gone early.

Then the set falls off a cliff on purpose. After the Rhapsody comes Constantinescu's Suite — *Joc*, *Cântec*, *Joc Dobrogean*, small dry village material, three movements and no fireworks — and the levels drop from −18.0 to −24.5, −23.3 and −21.4. That is the convention working for once as an argument: the showpiece first, then what was actually there. It also means the volume set for track 1 is wrong for tracks 2–4, which is the honest experience of this generation and is stated here so nobody thinks it is a mastering fault.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Romanian Rhapsody No. 1, Op. 11/1 | George Enescu | Mihaela Ursuleasa | 11:56 | [Track](https://open.spotify.com/track/1iOtgmRK2A6YnxQJAPUWnz) |
| 2 | Suite for Piano: I. Joc | Paul Constantinescu | Mihaela Ursuleasa | 2:29 | [Track](https://open.spotify.com/track/4oGgMBvsTCHZILWKMft2fs) |
| 3 | Suite for Piano: II. Cântec | Paul Constantinescu | Mihaela Ursuleasa | 4:22 | [Track](https://open.spotify.com/track/6iV52bKQPgqLgLh1lpiYZw) |
| 4 | Suite for Piano: III. Joc Dobrogean | Paul Constantinescu | Mihaela Ursuleasa | 3:59 | [Track](https://open.spotify.com/track/2kiNwmkYW0EMTEqb2ioSbU) |

Why each track:

- Romanian Rhapsody No. 1 — thirteenth in the world. Everything a country has, played by one person, sounding like far more than it is.
- Joc — a dance. Three European titles, in 2001–02, 2010 and 2016–17, won in the gaps a rival left.
- Cântec — a song, and the quiet middle. The Antim Cup going one way from 2002 onward, and the apprentice taking everything.
- Joc Dobrogean — a Dobrudja dance, the plainest thing on the record. Eight World Cups, no quarter-final, and two men playing a decade past the point at which a working system would have replaced them.

Spotify album: [Enescu, Constantinescu, Schubert & Bartók: Romanian Rhapsody](https://open.spotify.com/album/7IE9Z31Ov3fOz0yDoJ77RC) (Berlin Classics, 2011). The same disc has **Bartók's Two Romanian Dances, Op. 8a** ([I](https://open.spotify.com/track/6XE8iWIPB43EUBvOdRO1PR), [II](https://open.spotify.com/track/2TniG0IfB91Dle0g7gOHHb), 9:45 together) — reserved rather than used, because Generation 6 is built on Bartók's field collecting and two Bartók sets in a row would flatten the end of the chapter.

Spotlistr input:

```text
Mihaela Ursuleasa - Romanian Rhapsody No. 1, Op. 11/1
Mihaela Ursuleasa - Suite for Piano: I. Joc
Mihaela Ursuleasa - Suite for Piano: II. Cantec
Mihaela Ursuleasa - Suite for Piano: III. Joc Dobrogean
```

### Generation 6: Not Here as a Tourist (2018–2026)

Total: **21:44**. **Lucian Ban, John Surman and Mat Maneri**, from *Transylvanian Folk Songs — The Béla Bartók Field Recordings* (Sunnyside, 15 May 2020). Piano, soprano saxophone and bass clarinet, viola.

A Romanian, an Englishman and an American, playing songs Bartók wrote down in Transylvanian villages between 1908 and 1917.

That is the set's whole argument, because this is the generation in which twelve of the twenty-three Romanians named in Montevideo were born in Romania, and four of the five tries that afternoon were scored by men born on other continents. The most deliberately national rugby project in European history is now held together by heritage recruitment, and there is nothing improper in it — those players are giving what they have to a country they have chosen, and a French coach is doing what a serious coach must with the tools available.

What makes the record the right one is the standard it meets. Ban brought this material to Surman and Maneri; they are not visiting it, decorating it, or playing at being Romanian. They are three musicians taking village songs entirely seriously, for their own sake, at length. That is David Gérard's line — *I'm not here as a tourist* — passing its own test, and it is the honest version of what Romania now does with a Tongan-born flanker and a South African lock.

One note on the credit, since it will look odd in a table. Bartók is named as collector, not composer: these are anonymous village tunes, and his part was to walk into Transylvania with a phonograph and write them down. He did it when Transylvania was still Hungary, which is an argument in both countries to this day, and the record's sleeve is careful about where each tune came from. Worth saying in a set that is otherwise about borrowed men.

Levels descend cleanly: −12.0, −13.0, −13.4. This is a loud, close, spacious recording and it will sound bigger than everything before it except Generation 4.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Violin Song | Traditional, collected by Béla Bartók | Lucian Ban, John Surman, Mat Maneri | 8:02 | [Track](https://open.spotify.com/track/1z7NFoZMj44TLAt1O39Vxo) |
| 2 | Transylvanian Dance | Traditional, collected by Béla Bartók | Lucian Ban, John Surman, Mat Maneri | 6:03 | [Track](https://open.spotify.com/track/7zTlKzmGd8Dps7GIRw0pkv) |
| 3 | The Dowry Song | Traditional, collected by Béla Bartók | Lucian Ban, John Surman, Mat Maneri | 7:39 | [Track](https://open.spotify.com/track/5FikOgKIGL9zhYIJd3s7TL) |

Why each track:

- Violin Song — eight minutes of a village tune taken apart by three men from three countries. The team sheet.
- Transylvanian Dance — the disqualification of 2018, the 287 points conceded in France in 2023, twenty-second in the world, and fourth in Europe behind Portugal and Spain. Not a straight line and not a recovery arc.
- The Dowry Song — a song for what a family gives away, and the closer. Montevideo, 11 July 2026: Uruguay 36, Romania 36, and the set-piece that could not be taken away.

Spotify album: [Transylvanian Folk Songs](https://open.spotify.com/album/4OWELiqYaDmLFx0J6UG0VV) (Sunnyside, 2020). Four further tracks sit at the same level and are reserved rather than used — "Carol" (6:53), "The Mighty Sun" (5:29), and, much quieter at around −19, "The Return" and "Up There", which are the ones to reach for if a reader wants this record at reading volume rather than at its own.

Spotlistr input:

```text
Lucian Ban - Violin Song
Lucian Ban - Transylvanian Dance
Lucian Ban - The Dowry Song
```

Romania complete: Generations 0–6. Next chapter: South Africa.

---

## Chapter 6 — South Africa

Built on 23 September 2026. **Eight sets, not seven**: this chapter runs Generation 0 to Generation 7.

The music problem here is the worst in the book, and it is the opposite of Romania's. South Africa's great popular music is overwhelmingly *sung* — isicathamiya, the Malay choirs, mbube and mbaqanga, gospel, the struggle songs, the Afrikaans volkslied, the church singing that is the real music of half the households in the chapter. The no-vocals rule takes all of it. What is left is a single thin instrumental line, and the good news is that it runs the whole length of the story: goema and Cape jazz at one end, marabi and township swing in the middle, the boeremusiek concertina off to one side, the exiles' jazz after 1960, and a Cape Town piano trio playing in 2024. Eight sets came out of it, and every one of them is a real record rather than a compromise.

The sets run:

- A Cape Town piano trio playing the oldest creole music in the country, for a homemade code named after a headmaster's handwriting.
- The concertina of the platteland, for the Volk taking the conqueror's game.
- Sophiatown's big-band swing, for the generation that told you only half of its own years.
- *Yakhal' Inkomo* — the bellowing of the bull — for no normal sport in an abnormal society.
- An exile's record about home, made in New Jersey in 1985, for the decade the invitations stopped.
- A Soweto string quartet, closing on *Nkosi Sikelel' iAfrika*, for one jersey.
- Zim Ngqawana's "Transformation", for the generation that argued about the word.
- A Cape Town trio in 2024, closing on "Liberation Movements", for the inheritance.

**The braid is the organising decision.** The chapter's argument is that there were two rugby histories in one country, founded three years apart, and that both were real. So the sets alternate sides deliberately, and each one says which side of the line it comes from — Generation 1's concertina and Generation 2's swing band are the same twenty years heard from opposite ends of the same city. No set is asked to be neutral, because nothing in this chapter was.

**The political check is heavier here than anywhere else in the book, and the care list governs.** *Die Stem van Suid-Afrika* is not used, in any arrangement, however instrumental, anywhere in this book — and Generation 5, where the chapter's whole hinge is two anthems, says so on the page rather than leaving a reader to wonder. "De la Rey" is out. Old South African Defence Force marching repertoire is out. Struggle songs calling for violence are out. What is in, once: *Nkosi Sikelel' iAfrika*, instrumental, played by four strings from Soweto, as the closer of Generation 5 — because the rule says that where the story names a piece of music you play it, and the story names it.

Availability was checked in South Africa, as everywhere since Georgia: all thirty-seven tracks return `isPlayable` and play in ZA.

Rejected on the rules:

- **The Hilton Schilder Goema Club, *Hottie Kulture* (2021).** The first choice for Generation 0 and the better goema record — a nine-piece Cape ensemble, Khoisan mouthbow, klopse whistles, Malay choral song, the whole creole inheritance in one album. It has a dedicated vocalist, Candice Thornton, and per-track vocal status cannot be established. Out, and the same call as *Luminitza* in Romania. Schilder's own piano trio record is used instead.
- **The Paul Simon *Graceland* medley, the Dave Grusin and the Sting** on the Soweto String Quartet album. Not South African compositions, and *Graceland* carries its own boycott argument, which a reading playlist is not the place to relitigate.
- **The national-anthem library recordings.** Several exist — French Republican Guard bands, Italian "national pride" brass, KPM production music — and all of them pair *Nkosi Sikelel' iAfrika* with Die Stem in one track, which puts them out twice over: the anthem question and the cheap-master question at the same time.

### Generation 0: Gog's Game and the Two Beginnings (1861–1889)

Total: **21:41**. **Hilton Schilder**, *Rukma Vimana* (2016): Schilder on piano, **Eldred Schilder** on bass, **Claude Cozens** on drums. A Cape Town piano trio.

Nothing from the 1860s was recorded, so this generation gets the oldest music in the country that is still being played, and in the Cape that means **goema** — the creole of Khoi and slave rhythm, Dutch and Malay dance tune, mission hymn and garrison brass, assembled at the bottom of the town by whoever was standing in it. There were never any written rules for it either.

That is not a decorative parallel. The chapter's first fifteen years are a game with no written rules, invented by one man out of two English schools' playground laws, named after the only legible letters of his signature, and refereed by his presence. Cape rules football was a negotiation between men from Eton, Rugby, Winchester and Marlborough. Goema is the same kind of object, made by people with far less to negotiate with, and it outlasted Gog's game by a century and a half.

Hilton Schilder is the tradition's leading keeper — a Cape Flats musical dynasty, a multi-instrumentalist who plays the **!Xaru**, the Khoisan mouthbow, and one of very few people alive who does. The record used here is his straight piano trio, which is the reason it is used: it is unambiguously instrumental, and the bigger, better goema record with his nine-piece Goema Club is out under the rule (see above).

Be honest about the stretch. This is a 2016 recording standing in for 1861–1889, which is a longer reach than Toni Iordache made for Romania's 1950s. It is here because the alternative was a Victorian brass compilation with no connection to the Cape at all, and because a reader who wants to know what the two beginnings had in common should be listening to something that came out of both of them.

Levels descend cleanly: −12.7, −13.1, −13.5, −14.6.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Intro to Alex | Hilton Schilder | Hilton Schilder | 3:57 | [Track](https://open.spotify.com/track/4b4CbIsNGAKkhWPRfStrY5) |
| 2 | Birsigstrasse 90 (Trio Version) | Hilton Schilder | Hilton Schilder | 5:11 | [Track](https://open.spotify.com/track/5N1AwMBB4zPMZzQNsIZ4Gz) |
| 3 | Duiwepiek 1+2 | Hilton Schilder | Hilton Schilder | 7:19 | [Track](https://open.spotify.com/track/0qOtkMYc5VJ8LOAscG9U94) |
| 4 | Rukma Vimana | Hilton Schilder | Hilton Schilder | 5:14 | [Track](https://open.spotify.com/track/3AnmhDYf2KFCpnZMEH58YB) |

Why each track:

- Intro to Alex — an opening that is barely an opening. Green Point Common, 23 August 1862: a garrison side, the Colonial Civil Service, a governor watching, nobody scoring.
- Birsigstrasse 90 — a street address in Europe, in a Cape Town record. Ogilvie brought Winchester and Bradfield to Rondebosch and made something that was neither.
- Duiwepiek 1+2 — pigeon racing, which is what the Cape Flats does on a Saturday. The game escaping the schools: Stellenbosch farm boys, mission students in Grahamstown, miners at Kimberley, all of them inside a decade.
- Rukma Vimana — the quietest, and the closer. Kimberley, 1889, and the older union of 1886 that the record forgot.

Spotify album: [Rukma Vimana](https://open.spotify.com/album/1mmT75X1eC3Y24LqaOz492) (Sharp-Flat, 2016).

Spotlistr input:

```text
Hilton Schilder - Intro to Alex
Hilton Schilder - Birsigstrasse 90 - Trio Version
Hilton Schilder - Duiwepiek 1+2
Hilton Schilder - Rukma Vimana
```

### Generation 1: The Conqueror's Game (1890–1948)

Total: **20:34**. **Nico Van Rensburg**, concertina, from *Speel tradisionele Boeremusiek, Vol. 1* (2019). Waltzes and seties, not the fast vastraps.

This is the generation in which Afrikaners took an English game and used it to beat the English, and the historian's sentence the chapter quotes is the whole of it: they adopted "a most 'imperial game' in order to achieve" autonomy from British rule. So the set is their own music and nobody else's — **boeremusiek**, the concertina dance music of the platteland the packs came off, from the same wheat and wine districts that Stellenbosch carried the game into.

It needs saying what this music sat next to. Between October 1899 and May 1902 the empire whose game these people played burned their farms and put their families in camps, and some twenty-six thousand Boer women and children died in them, twenty thousand of them under sixteen. This is the dance music of the people who buried those children. It is the right music for this generation precisely because it is theirs — not despite what happened to them, and not as a comment on it. A waltz is a waltz.

The political check is clean and short. Boeremusiek is dance music, not regime repertoire; it is played at Afrikaans festivals today and has been recorded continuously for ninety years. Die Stem is a different object and is out everywhere in this book. Nothing here is anthem material, and nothing here is *volkspele* pageantry from the 1938 Great Trek centenary either.

Two honesties. The recording is from 2019, playing the traditional repertoire — the album's own title says *speel*, plays — so this is the tunes of the generation rather than a document of it, the same arrangement Romania's Generation 2 has with Toni Iordache. And the album's mastering is wild, running from −9.1 to −18.7 LUFS across eighteen tracks; the eight here were picked for level consistency (−15.3 down to −17.4, a 2.1 dB descent) as much as for mood, and swapping any of the others in will make a reader reach for the volume.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Magoebaskloof Wals | Traditional | Nico Van Rensburg | 2:45 | [Track](https://open.spotify.com/track/5HiRj0HT7GPHytNrEx99ln) |
| 2 | Oom Louw se Polka | Traditional | Nico Van Rensburg | 2:31 | [Track](https://open.spotify.com/track/2AF6UJ1hzEoGhgcB1zSh4A) |
| 3 | Soutpansberg Polka | Traditional | Nico Van Rensburg | 2:15 | [Track](https://open.spotify.com/track/5P4fAwm7dsBpsCWJxn9xpa) |
| 4 | Stellenbosch Verlange | Traditional | Nico Van Rensburg | 2:49 | [Track](https://open.spotify.com/track/5Ej4Cia8pPPcNZH5h1vslN) |
| 5 | Lettie se Wals | Traditional | Nico Van Rensburg | 2:43 | [Track](https://open.spotify.com/track/6osv3Wdk96p2OCwxqgSROa) |
| 6 | Resiesbaan Seties | Traditional | Nico Van Rensburg | 2:17 | [Track](https://open.spotify.com/track/487MTs7GuS6lDXiwnOnNty) |
| 7 | Klipbank Seties | Traditional | Nico Van Rensburg | 2:29 | [Track](https://open.spotify.com/track/4mB1ldmxKyjEc2d0KHAQ10) |
| 8 | Onder die Kremetartboom | Traditional | Nico Van Rensburg | 2:45 | [Track](https://open.spotify.com/track/2geJVQQ6DhVG00ix5jBVnB) |

Why each track:

- Magoebaskloof Wals — a Northern Transvaal pass, and the fullest sound here. 1891, and the tour Rhodes paid for after Onze Jan talked him into it.
- Oom Louw se Polka — somebody's uncle. A jersey out of a dead club's cupboard, worn twice to beat the British.
- Soutpansberg Polka — the far north. 1906, a team of Boers and Britons sent abroad to unify a broken country, naming itself overnight so Fleet Street could not.
- Stellenbosch Verlange — *longing for Stellenbosch*. Founded in the winter of 1875, months old, riding into town to challenge the Civil Service, and by the 1920s the seminary of the whole game.
- Lettie se Wals — a waltz for somebody's wife, and the quiet middle of the set. The war, and the camps.
- Resiesbaan Seties — the racecourse. The line going abroad: Tureia and Wilson dropped in 1919, the Blackett cable in 1921, Nēpia left at home in 1928.
- Klipbank Seties — a stone bank. The 1930s: Blood River, the ox-wagons, the sacred history, and a game about to be bolted to it.
- Onder die Kremetartboom — under the baobab, and the quietest. 1937 in Auckland, "scrum, scrum, scrum" by telegram, and then 1948.

Spotify album: [Speel tradisionele Boeremusiek, Vol. 1](https://open.spotify.com/album/09PS0hicjOTzrkm8gbvVc5) (2019).

Spotlistr input:

```text
Nico Van Rensburg - Magoebaskloof Wals
Nico Van Rensburg - Oom Louw se Polka
Nico Van Rensburg - Soutpansberg Polka
Nico Van Rensburg - Stellenbosch Verlange
Nico Van Rensburg - Lettie se Wals
Nico Van Rensburg - Resiesbaan Seties
Nico Van Rensburg - Klipbank Seties
Nico Van Rensburg - Onder die Kremetartboom
```

### Generation 2: The Machinery (1948–1969)

Total: **20:07**. **African Jazz Pioneers**, self-titled (Gallo) — Ntemi Piliso's band, recreating the big-band marabi and township swing of the 1950s.

The chapter says it plainly at the end of this generation: it "has told you only half of its own years." This set is the other half.

The cold open is Ellis Park, 6 August 1955, a hundred thousand people, the biggest rugby crowd in the world — and a thirty-seven-year-old Soweto lawyer somewhere inside it, invisible. Hold 1955 still for a second. In February of that year the bulldozers started on **Sophiatown**, and the freehold suburb that had produced the best music in Africa was cleared and renamed Triomf. The white machine was at its height in 1955; so was the thing it was demolishing. Both were in Johannesburg, eight kilometres apart, in the same winter.

This is what that sounded like: alto and tenor saxophones, two trumpets, trombone, and a rhythm section playing marabi through Count Basie's grammar. **Edmund "Ntemi" Piliso** had been a marabi player in the real thing before it was cleared, and the band he led from the late 1980s existed to put the sound back — which makes this, like Generation 1's concertina, the tunes of the generation rather than a document of it.

Then notice the loudness, because it is the set's whole character. This is the loudest block in the chapter by six decibels — a Gallo master cut for a township jukebox and a shebeen wall, mixed to be heard over people. Generation 4, the exile's record made in a New Jersey studio, sits fourteen decibels below it. The two masters tell you as much about who these records were for as any of the prose does.

Levels: −8.2, −8.5, −8.6, −9.4, which is as tight as anything in the book.

One verification note, because this is the least-documented record in the chapter: no vocalist appears in any account of the band's line-up, and it is a saxophone-and-brass swing orchestra. Spotify dates the album 1989; discographies also give 1991.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Ten Ten Special | African Jazz Pioneers | African Jazz Pioneers | 4:08 | [Track](https://open.spotify.com/track/53yhMARSUqDQK79durJl6q) |
| 2 | Mzabalazo (Home Town) | African Jazz Pioneers | African Jazz Pioneers | 4:41 | [Track](https://open.spotify.com/track/27mdjwx1WZNJAP04gGRukn) |
| 3 | Nonto Sangoma | African Jazz Pioneers | African Jazz Pioneers | 4:53 | [Track](https://open.spotify.com/track/2ZTM6SYLGuGTtW69c9qdB8) |
| 4 | Riverside Special | African Jazz Pioneers | African Jazz Pioneers | 6:25 | [Track](https://open.spotify.com/track/2bZFzuPcwI5Tcs1B0C1NmA) |

Why each track:

- Ten Ten Special — a band's shorthand, the way "Ten Ten" was a beer or a bus. The machine at full power: four straight over the All Blacks in 1949, two Grand Slams, the dive pass.
- Mzabalazo (Home Town) — *mzabalazo* is the struggle. Sharpeville, March 1960, and the All Blacks arriving three months later with their Māori players left at home.
- Nonto Sangoma — a healer's name. The courtroom and the golfer: Brandsma in 1962, and Papwa Sewgolum beating a hundred and thirteen white men at the Natal Open with a back-to-front grip.
- Riverside Special — the longest and the last. Verwoerd at Loskopdam on the same afternoon the Springboks won in Christchurch, and the friendship cracking for good.

Spotify album: [African Jazz Pioneers](https://open.spotify.com/album/3ynjWhGod8kcPho0ax2wpE) (Gallo).

Spotlistr input:

```text
African Jazz Pioneers - Ten Ten Special
African Jazz Pioneers - Mzabalazo (Home Town)
African Jazz Pioneers - Nonto Sangoma
African Jazz Pioneers - Riverside Special
```

### Generation 3: No Normal Sport (1959–1979)

Total: **23:12**. **Winston Mankunku Ngozi**, *Yakhal' Inkomo* (1968) — tenor saxophone, with Lionel Pillay, Agrippa Magwaza and Early Mabuza.

*Yakhal' inkomo* means **the bellowing of the bull** — the cry of cattle at the moment of slaughter. Mongane Wally Serote took the phrase for a poem. Mankunku put it on the front of a record, and then did not say another word about it for forty minutes.

There is no better music in this chapter for the generation whose title is a slogan. Mankunku was a Cape Town man, from Retreat, and in the venues where he could be booked at all he sometimes had to play **behind a curtain**, so that a white audience could hear him without the inconvenience of seeing him. That is *no normal sport in an abnormal society* in one stage direction, and it is why this set belongs to the generation of Abass and Loriston rather than to any of the white game's afternoons.

What the record also does is answer the generation's argument on its own terms. "Dedication" is Mankunku's, written for Coltrane and Wayne Shorter; "Bessie's Blues" is Coltrane's. A Black South African in 1968 playing the Americans' language in his own mouth is a man choosing what to do with a world that will not have him — which is exactly the choice Loriston and Abass made differently, and it is worth noticing that Mankunku's answer was neither of theirs. He played.

One thing the generation's politics cannot tidy away: the album was a hit for Gallo, and the state did not stop it. A machinery that would cancel a cricket tour rather than admit Basil D'Oliveira sold this record in its shops. Both are true; the chapter has been saying so all the way through.

Levels are close, at −13.5, −13.8 and −15.1, so the set keeps the record's own order rather than running loudest to quietest — the title track is the reason the set exists and it goes first.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Yakhal' Inkomo | Winston Mankunku Ngozi | Winston Mankunku Ngozi | 8:53 | [Track](https://open.spotify.com/track/2wad01jbW8ngGLtjyPycqF) |
| 2 | Dedication (To Daddy Trane & Brother Shorter) | Winston Mankunku Ngozi | Winston Mankunku Ngozi | 6:44 | [Track](https://open.spotify.com/track/0WytJb941FN2ichvOfM6je) |
| 3 | Bessie's Blues | John Coltrane | Winston Mankunku Ngozi | 7:35 | [Track](https://open.spotify.com/track/77WlPqT2YbaVm69tgHm8SX) |

Why each track:

- Yakhal' Inkomo — the cry of the bull. The Rhodes Cup retired in 1969 because of whose name was on it; Athlone Stadium in 1971 playing for a trophy with nobody's; a nineteen-year-old exile shutting England's cricket down; twenty-two nations walking out of an Olympics over a rugby tour.
- Dedication — a man deciding what to do with a world that will not have him. Normal sport in an abnormal society, and its negation, and both held by serious men for serious reasons.
- Bessie's Blues — Coltrane's tune, played in Johannesburg in 1968. The Double Standards Resolution, and a movement that held the line and sent its own players the bill.

Spotify album: [Yakhal' Inkomo](https://open.spotify.com/album/1i86qAAz2KeNbBtgJUgnmk) (Gallo/World Record Co., 1968; this edition 2007). "Doodlin'" — the Horace Silver tune, and the fourth piece on the original LP — is reserved rather than used; the set stops at three.

Spotlistr input:

```text
Winston Mankunku Ngozi - Yakhal' Inkomo
Winston Mankunku Ngozi - Dedication (To Daddy Trane & Brother Shorter)
Winston Mankunku Ngozi - Bessie's Blues
```

### Generation 4: Barbed Wire (1980–1989)

Total: **19:02**. **Abdullah Ibrahim & Ekaya**, *Water from an Ancient Well* — recorded October 1985 at Van Gelder Studio, Englewood Cliffs, New Jersey; released 1986. Ibrahim on piano with Carlos Ward, Ricky Ford, Charles Davis, Dick Griffin, David Williams and Ben Riley. All eight pieces are Ibrahim's own.

This is the decade in which nobody expelled South Africa and nobody invited it either — the invitations simply stopped, and the Springboks ended up playing a Test on a private polo field in New York State in front of thirty-five people. The music is the same condition from the other end: a Cape Town man who left in 1962 and would not come home until 1990, in a New Jersey studio, with seven Americans, writing about a city he could not go to.

**"Mandela"** was written while the man was on Robben Island. It was recorded in October 1985 — three years before Craven and Luyt flew to Harare to ask a banned organisation for a blessing, and nine years before its subject became president. **"Tuang Guru"** is named for the exiled Indonesian prince brought to the Cape as a political prisoner in 1780, who founded Islam at the Cape while imprisoned on Robben Island. The same island, two hundred years apart, on a record made by a third exile. Nobody had to arrange that.

This is the quietest set in the chapter by a distance — around −22 LUFS, fourteen decibels below Generation 2's township masters. Put the two side by side and the difference is not taste: it is who each record was made for, and with whose money.

One omission to explain. **"Manenberg Revisited"** is on this album, and it is the most famous thing on it — the Cape Flats township tune that became the unofficial anthem of a generation without a word in it. It is left out on level: −15.2 against the set's −21.0, −23.2, −22.9 and −23.3, which is a volume change in the middle of twenty minutes. It is [here](https://open.spotify.com/track/7oJpfT2cGrOwxwuFRunY9i), 6:11, for anyone who would rather have it than a level-consistent set, and that is a defensible trade.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Mandela | Abdullah Ibrahim | Abdullah Ibrahim, Ekaya | 4:59 | [Track](https://open.spotify.com/track/1pnikkS6BPGfjHd77L61m2) |
| 2 | Tuang Guru | Abdullah Ibrahim | Abdullah Ibrahim, Ekaya | 5:26 | [Track](https://open.spotify.com/track/66o2PgV2oToTjsY6E18dDe) |
| 3 | The Wedding | Abdullah Ibrahim | Abdullah Ibrahim, Ekaya | 2:41 | [Track](https://open.spotify.com/track/2tzlso3uBmyYc3WGx6oZd6) |
| 4 | Sameeda | Abdullah Ibrahim | Abdullah Ibrahim, Ekaya | 5:56 | [Track](https://open.spotify.com/track/6R3tvKimOQq1W3BBW09RS0) |

Why each track:

- Mandela — written for a prisoner, in 1985. Hamilton, 25 July 1981: four hundred people tearing down the wire, a match abandoned live on South African television, and a man in a cell who said it was as if the sun had come out.
- Tuang Guru — the Cape's first political exile, two centuries early. Errol Tobias at Newlands on 30 May 1981, carrying an argument in both directions at once.
- The Wedding — short, and the only celebration in the set. Six Tests, six wins, and by 1984 simply the best fly-half on the field.
- Sameeda — the longest and the quietest, a name for a woman who is not in the story. Harare, 15 and 16 October 1988, and a president calling the game's patriarch a traitor.

Spotify album: [Water from an Ancient Well](https://open.spotify.com/album/5EQkSknw8twG8oiukc55la) (BlackHawk, 1986). **Use this edition and no other.** Spotify also carries a 2021 reissue of the same eight pieces (album `7baHK0NyFxnTiTAoIRjZs2`), and every track on it is licensed for **Japan only** — `isPlayable` returns true and the market list shows one country, JP. It was the first edition this chapter used, and the ZA check caught it. Exactly the Georgia lesson again: a short market list is a restriction, and only a country check settles it.

Spotlistr input:

```text
Abdullah Ibrahim - Mandela
Abdullah Ibrahim - Tuang Guru
Abdullah Ibrahim - The Wedding
Abdullah Ibrahim - Sameeda
```

### Generation 5: One Jersey (1990–1995)

Total: **20:21**. **Soweto String Quartet**, *Zebra Crossing* (30 September 1994): Sandile, Reuben and Thami Khemese with Makhosini Mnguni. The set closes on their **Nkosi Sikelel' iAfrika**.

This generation's two great afternoons are both about anthems, at the same ground, three years apart. On 15 August 1992, at Ellis Park, fifty thousand people sang *Die Stem* unaccompanied through a minute's silence held for the dead of Boipatong — and Louis Luyt then played it over the loudspeakers in breach of the agreement his own game had made. On 24 June 1995, at Ellis Park, sixty-three thousand people sang both anthems back to back, neither against the other.

The rule in this file says that where the story names a piece of music you play it, instrumental. So the set ends on *Nkosi Sikelel' iAfrika* — Enoch Sontonga's 1897 hymn, written by a mission schoolteacher, played here by four strings. Its partner is not here, and will not be anywhere in this book. Die Stem is the apartheid state's anthem and stays out in any arrangement, however instrumental; its opening lines were folded into the post-1994 national anthem, which is a different piece and is not the problem. The crowd of 1995 sang both, and had earned the right to. A reading playlist has not, and it cannot explain itself in the time it takes to play.

The quartet is the right body to carry it. Three brothers and a fourth man, classically trained in Soweto, whose debut album came out in the country's first year and who played at the inauguration; a string quartet from Soweto in 1994 was itself an argument, and the music is village and township tune played with a Western bow, which is what half this chapter is about.

Levels run −15.2 down to −17.8, and the anthem at −16.5 breaks the descent by sitting last on purpose. Same decision as the *Bocet* that closes Romania's Generation 3: the closer is fixed by the story, not the meter.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Kwela | Soweto String Quartet | Soweto String Quartet | 3:41 | [Track](https://open.spotify.com/track/0frk5x4MtPG7HV3LiYda9r) |
| 2 | Zebra Crossing | Sandile Khemese | Soweto String Quartet | 4:10 | [Track](https://open.spotify.com/track/6n1DBFVfWZpAp94xBEqx7H) |
| 3 | Kadeni Kwazulu | Makhosini Mnguni | Soweto String Quartet | 3:40 | [Track](https://open.spotify.com/track/4FOdO5okZa0XNAPiXC8Jr5) |
| 4 | Mbayi Mbayi | Soweto String Quartet | Soweto String Quartet | 2:41 | [Track](https://open.spotify.com/track/4A6Z8lez1YEEKMner40laV) |
| 5 | Zulu Lullaby | Sandile Khemese | Soweto String Quartet | 1:32 | [Track](https://open.spotify.com/track/4sT9S30N4eWdmUDsYx0qZY) |
| 6 | Where were you taking me to? (Uno'Ntsonkisa Kae?) | Soweto String Quartet | Soweto String Quartet | 2:03 | [Track](https://open.spotify.com/track/6PqaIu5N9KPnMCCBBGHWlI) |
| 7 | Nkosi Sikelel' iAfrica — God Bless Africa | Enoch Sontonga | Soweto String Quartet | 2:34 | [Track](https://open.spotify.com/track/2NrsCZ9QignEDNaYk4RNFb) |

Why each track:

- Kwela — the pennywhistle music of the 1950s streets, played on strings in 1994. Two rugby histories becoming one body in March 1992.
- Zebra Crossing — the album's title and its joke: black and white, in stripes, and everybody has to cross somewhere.
- Kadeni Kwazulu — a long time ago in KwaZulu. The ledger the non-racial movement kept: unity at speed, and a takeover with a few faces of colour on boards.
- Mbayi Mbayi — the record's own theme, brief this time. A 747 over Ellis Park with GOOD LUCK BOKKE on its belly.
- Zulu Lullaby — ninety seconds, the smallest thing in the chapter. Mandela in the changing room telling Chester Williams to go and make the rest of South Africa proud too.
- Where were you taking me to? — the question the title asks, and the one Chester Williams asked afterwards. A week of unity is a week.
- Nkosi Sikelel' iAfrika — the closer. Sung at Ellis Park on 24 June 1995 beside the song it had spent a century being sung against.

Spotify album: [Zebra Crossing](https://open.spotify.com/album/0VCI2e7eMg8d3DIzhpMwjd) (Teal/Gallo, 1994). Not used: the Paul Simon *Graceland* medley, the Dave Grusin and the Sting — see the rejected list above.

Spotlistr input:

```text
Soweto String Quartet - Kwela
Soweto String Quartet - Zebra Crossing
Soweto String Quartet - Kadeni Kwazulu
Soweto String Quartet - Mbayi Mbayi
Soweto String Quartet - Zulu Lullaby
Soweto String Quartet - Where were you taking me to? (Uno'Ntsonkisa Kae?)
Soweto String Quartet - Nkosi Sikelel' iAfrica - God Bless Africa
```

### Generation 6: The Professionals (1995–2017)

Total: **20:29**. **Zim Ngqawana**, *Zimology* (1998) — tenor and alto saxophone and flute, with Andile Yenana on piano, recorded in Oslo with Ingebrigt Håker Flaten and Paal Nilssen-Love.

This generation's entire politics is one word, and Ngqawana put it on a record in 1998, as the last movement of a suite. **"Transformation"** closes this set, and the set is here for that.

Ngqawana came from **New Brighton, Port Elizabeth** — the same Eastern Cape township world that produces this chapter's last captain, one generation early. He did not touch a saxophone until he was twenty-one, went to Boston on a scholarship, came home, and made this album in the fourth year of the new country: a Xhosa musician from a Black township recording South African material in Norway with two Norwegians, which is what the professional era looked like from the side of it nobody televised.

The rest of the titles do work too. **"Qula Kwedini"** is the call in a Xhosa stick fight — *fight, boy* — which is the most rugby sentence in this chapter's music, and it opens the set. **"Hymn for the War Orphans"** is exactly what it says, in 1998.

Mood: this is the generation of the seventeen-Test streak and Kamp Staaldraad, of 36–0 and 57–0 against the same two rivals inside a decade, of a second star and then Brighton. Elegies are the right register. A serious man playing carefully, in the years when the money arrived first and the meaning did not arrive at all.

Levels descend from −12.0 to −14.4. Dropped: **"Baby Angelina"**, the Four Part Suite's third movement, which sits at −27.2 LUFS — sixteen decibels below its own neighbours, and unusable in a set at any position.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Elegies in C minor (Opus #1): Qula Kwedini | Zim Ngqawana | Zim Ngqawana | 4:22 | [Track](https://open.spotify.com/track/4k2ffDFB36WBvzP2f7jlW5) |
| 2 | Four Part Suite (Opus #20): Hymn for the War Orphans | Zim Ngqawana | Zim Ngqawana | 4:33 | [Track](https://open.spotify.com/track/3ueWJJu6FdrgoZ37UG8ePN) |
| 3 | Elegies in C minor (Opus #1): Uyangantathu | Zim Ngqawana | Zim Ngqawana | 4:43 | [Track](https://open.spotify.com/track/4RFXhMAkLa5KoGCCg0ypPT) |
| 4 | Four Part Suite (Opus #20): Transformation | Zim Ngqawana | Zim Ngqawana | 6:51 | [Track](https://open.spotify.com/track/3GHB2VcjliHSz1uRquf0e3) |

Why each track:

- Qula Kwedini — *fight, boy*, the stick-fighter's call. Two days before the 1995 final, a television deal worth five hundred and fifty-five million dollars; nine weeks after it, the game professional.
- Hymn for the War Orphans — 1998, and a squad in a pit being taught that the anthem was a weapon.
- Uyangantathu — the quiet third. Bryan Habana's eight tries in France in 2007, and the end of the era in which Black excellence in that jersey could be called symbolic.
- Transformation — the word itself, and the longest track. Brighton, Albany, sixth in the world, and a question that winning could no longer defer.

Spotify album: [Zimology](https://open.spotify.com/album/5Fi1jbxQ29INXpFGvz3zxh) (Sheer Sound, 1998).

Spotlistr input:

```text
Zim Ngqawana - Elegies in C minor: (Opus #1) Qula Kwedini
Zim Ngqawana - Four Part Suite: (Opus #20) Hymn for the War Orphans
Zim Ngqawana - Elegies in C minor: (Opus #1) Uyangantathu
Zim Ngqawana - Four Part Suite: (Opus #20) Transformation
```

### Generation 7: The Inheritance (2018–2026)

Total: **22:28**. **Kyle Shepherd Trio**, *A Dance More Sweetly Played* (18 November 2024). The set — and the chapter — ends on **"Liberation Movements"**.

Kyle Shepherd was born in Cape Town in 1987, which makes him this generation's own: four years younger than Siya Kolisi, from the same country and the same decade, and the leading pianist of it. His music comes out of the **goema** that opened this chapter — the Cape's creole inheritance, the same well Hilton Schilder draws from — and the two sets are deliberately cousins.

The distance between them is the whole distance this chapter measures. In 1889 that music had no name in the record anybody read; in 2024 it is a concert trio's own repertoire, recorded on its own terms, needing nobody's permission and nobody's patronage. That is the same journey as the one from two rugby boards founded three years apart to a captain from Zwide lifting the Webb Ellis Cup twice, and it took the same hundred and sixty-five years.

The closer is not a coincidence, but it is not a stunt either. "Liberation Movements" is the record's own title for its own piece, and it happens to be the quietest of the three, so it closes the set on the meter as well as on the argument. Levels: −14.5, −15.1, −15.6.

Reserved rather than used: **"Neo Marabi"** (5:49), which would have tied the last set in the chapter to Generation 2's marabi, and is left out only on level — it sits at −11.1, four decibels above the rest. It is [here](https://open.spotify.com/track/3xjAqUsU1bw5IyiPYd4SJv) for anyone who wants the circle closed twice.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | A Dance More Sweetly Played | Kyle Shepherd | Kyle Shepherd Trio | 8:09 | [Track](https://open.spotify.com/track/1ehmyB6T84EelDdpchaGdF) |
| 2 | Theme from a Film | Kyle Shepherd | Kyle Shepherd Trio | 7:12 | [Track](https://open.spotify.com/track/14IrHNPy0CK3WJBliQF2jI) |
| 3 | Liberation Movements | Kyle Shepherd | Kyle Shepherd Trio | 7:07 | [Track](https://open.spotify.com/track/4VUHvLclG28u4YBSyZN5p1) |

Why each track:

- A Dance More Sweetly Played — Ellis Park, 9 June 2018, and a Black captain of South Africa for the first time since 1889. Then Yokohama: a try in a World Cup final, scored by a man who walked twenty kilometres a day to school.
- Theme from a Film — which is what 1995 has become, and what 2019 and 2023 were careful not to be. A Lions series in empty stadiums, a sixty-two-minute video, and one point three times over.
- Liberation Movements — the last piece in the chapter. A captain's armband, a fourth star, an argument about equity votes and a ground in Auckland, conducted by a country that owns the game together.

Spotify album: [A Dance More Sweetly Played](https://open.spotify.com/album/46foYmXHYg5B9s8F1tg9J7) (2024).

Spotlistr input:

```text
Kyle Shepherd Trio - A Dance More Sweetly Played
Kyle Shepherd Trio - Theme from a Film
Kyle Shepherd Trio - Liberation Movements
```

South Africa complete: Generations 0–7. Next chapter: England.

---

## Pieces earmarked for later chapters

Noted as they come up, so that the sets are not built without them.

- **Wales, the golden era (1905).** *Hen Wlad Fy Nhadau*, instrumental. The chapter's hinge is 16 December 1905 at Cardiff Arms Park, where the Welsh side answered the haka with it and some forty thousand people took it up — the first anthem sung at an international fixture. A colliery or town brass band would carry the chapter twice over, since the valleys that filled the Arms Park had their own bands; a harp version is the quieter alternative. No choir and no crowd recording — the no-vocals rule holds even here, where the story is people singing.

## Music to handle with care

A running list of pieces that carry more than their tune, kept so that no set walks into one by accident. Everything here is a flag to check before use, not a finding: verify the history before a piece goes in or stays out, and where a set does use something contested, say why in the set's own text.

- **South Africa.** *Die Stem van Suid-Afrika* is the apartheid state's anthem: out, in any arrangement, however instrumental. (Its opening lines were folded into the post-1994 national anthem, which is a different piece and is not the problem; a standalone "Die Stem" recording is.) Also out: "De la Rey" (Bok van Blerk, 2006), a hit that became a rallying song for a strand of Afrikaner nationalism, and any struggle song calling for violence against Boers. Old South African Defence Force marching repertoire carries the border war with it — check what an arrangement of "Sarie Marais" is actually drawing on. Safe and good: Abdullah Ibrahim, instrumental "Shosholoza", township jazz and marabi, mission-hymn arrangements. **Settled when Chapter 6 was built, 23 September 2026.** *Nkosi Sikelel' iAfrika* is used once, instrumental, as the closer of Generation 5, because the chapter's hinge is the two anthems sung back to back at Ellis Park in 1995 and the rule says to play what the story names; Die Stem is not used beside it, and the set says on the page why not. Three further findings. **Boeremusiek clears the check** — it is concertina dance music, still played at Afrikaans festivals, not regime repertoire, and Generation 1 uses it as the Afrikaner's own music rather than as a comment on him; *volkspele* pageantry from the 1938 Great Trek centenary is a different object and stays out. **The anthem library recordings are all out twice over**: every one found pairs *Nkosi Sikelel' iAfrika* with Die Stem inside a single track, and they are cheap production masters besides. And **the Paul Simon *Graceland* material is out** — it carries its own boycott argument, and background music is not the place to reopen it, which cost the Soweto String Quartet set three tracks.
- **New Zealand.** "Ka Mate" is a taonga of Ngāti Toa, whose attribution rights are recognised in New Zealand law. A haka is not background music — it belongs in the prose, where the chapter can treat it properly. Do not substitute a "haka-style" instrumental pastiche either.
- **Wales.** "Delilah" was a terrace standard until the WRU stopped its choirs performing it at the Principality in 2023, over lyrics describing a man killing a woman. Leave it out, brass band or not. *Hen Wlad Fy Nhadau* is the piece the chapter wants; see the earmark above.
- **England.** "Swing Low, Sweet Chariot" is an African-American spiritual that became an England terrace song; the RFU reviewed it in 2020 and the argument is live. If it is used at all, it has to be as the spiritual, with its origin stated in the set's text.
- **Ireland.** The anthem question is itself part of the chapter (*Amhrán na bhFiann* for the state, "Ireland's Call" for the all-island team) — choose by period and say which and why. Rebel repertoire and Orange marching repertoire are both out.
- **Argentina and Uruguay.** "Marcha de las Malvinas" and the 1982 broadcast repertoire are out, and especially around the Falklands passages in Generation 2. The Marcha Peronista is a party song. The opposite case also needs a line rather than silence: Zitarrosa and Viglietti wrote from exile, so name them as what they were rather than passing them off as neutral guitar music.
- **Chile (next to build).** Víctor Jara was murdered in the days after the 1973 coup, in the stadium the chapter will almost certainly have to mention. His music can be used, but never as wallpaper — one line of context is the minimum. "Venceremos" and "El pueblo unido jamás será vencido" are Popular Unity anthems: out as background. Anything the Pinochet government used for itself: out. And no Selk'nam ceremonial recording under the Selknam generation: the Hain is the ceremony of a people hunted for bounties, whose descendants in the Corporación Selk'nam objected to the rugby franchise for using their name without asking. Background music made of their ceremony would repeat what the chapter criticises. The same reasoning as Ka Mate, and the Generation 5 set says so on the page.
- **Georgia.** Soviet state repertoire is out. "Suliko" is a much-loved love song and also, famously, Stalin's favourite, an association that has not faded in the region — check the framing before using it. It turns up where you would not expect: Sulkhan Tsintsadze's *Miniatures on Georgian Folk Tunes*, the obvious source for this chapter, sets it as No. 2 of the six, and Lisa Batiashvili's recording includes it. Use the other five. To be fair to the song: it is a love poem of 1895 by Akaki Tsereteli, Georgians sing it still, and it is not taboo in Georgia — Stalin simply liked it and had it broadcast. The reason to skip it is that a reader who knows that hears Stalin, and background music cannot explain itself. Tsintsadze himself is a national figure and carries none of this; Soviet *state* repertoire is the thing to avoid, not Soviet-era Georgian composers. Two further Georgian sensitivities, both live: Abkhazian and Ossetian tunes are part of Georgia's own folk inheritance and are normal repertoire for Georgian players, but they name the breakaway regions of the 1992–93 and 2008 wars, so say so rather than let a reader trip over it; and Russian labels and Russian-released recordings sit badly with many Georgians after 2008 and 2022. Georgian polyphony is choral, so the no-vocals rule already points to panduri and chonguri instrumentals.
- **Romania.** The Ceaușescu-era mass songs, and the *Cântarea României* festival repertoire built around them, are state propaganda music: out. Doina and lăutari instrumental playing are the honest choices, and Chapter 5 uses them — but the distinction needs care rather than a rule, because in this country the good folk music and the propaganda came out of the same ministry. Toni Iordache was a state-trained virtuoso on the state label; Zamfir toured the West because it suited Bucharest to let him. Both are used, and both sets say so on the page. What is out is repertoire *written for* the regime, not artists the regime paid. Two further notes. **Balanescu Quartet's *Luminitza* (Mute, 1994)** is the trap in this chapter: it is a Romanian émigré's album about December 1989, it looks instrumental, Spotify credits no vocalist, and it carries spoken word on at least four of its nine tracks — Bălănescu speaking over "Democracy" and "Revolution", four voices on "Still With Me", and a Romanian speech on "Link" that reviewers take to be Ceaușescu. It is out under the no-vocals rule, and it is the reason the rule is checked against a review rather than a credit list. And **Bartók in Transylvania** is not neutral in either Romania or Hungary: he collected there when it was Hungarian territory, so where his field material is used (Generation 6), say that he was the collector and the villagers were the source.
- **Italy.** Fascist-era songs ("Giovinezza" and the rest) are out, including band arrangements.
- **Fiji, Samoa, Tonga.** Church singing is the real popular music of these chapters, but it is singing, so only instrumental arrangements qualify. Avoid tourist-market "island medley" compilations, check that a piece is not a specific chiefly or funerary item being borrowed as background, and keep coup-era political songs out.
- **Australia.** "Advance Australia Fair" is contested with Indigenous Australians; if it appears, say so. Do not reach for a didgeridoo record as generic Australian colour — it is a particular people's instrument, and the chapter's subject is a British-descended code.

## Superseded selections — reserved against reuse

### Reservation index

Every composition below is out of use and reserved: no other performance, arrangement or remaster of it may be used anywhere in the book.

**Uruguay, first pass (superseded July–September 2026)**
- Gen 0: Mendelssohn, Venetian Gondola Song Op. 19b No. 6; Chopin, Nocturne Op. 9 No. 2; Aguado, Andante; Tárrega, Capricho árabe; Tárrega, Recuerdos de la Alhambra; Tárrega, Adelita.
- Gen 1: Debussy, Rêverie; Debussy, La fille aux cheveux de lin; Barrios, Julia Florida; Barrios, Chôro da saudade; Matos Rodríguez, La Cumparsita.
- Gen 2: The South Wind; Down by the Salley Gardens; Women of Ireland; Lord Mayo; Ramírez, Alfonsina y el mar (Spotify spells it "Alfosina").
- Gen 3: Santaolalla, *Ronroco* — Gaucho, Jardín, Lela, Iguazú, Coyita, De Ushuaia a La Quiaca.
- Gen 4: Penguin Cafe Orchestra, Perpetuum Mobile; Nyman, The Heart Asks Pleasure First and The Promise; Tiersen, Comptine d'un autre été, l'après-midi; Sakamoto, Energy Flow; Einaudi, Le onde.
- Gen 5: O'Halloran, We Move Lightly; Arnalds, Near Light; Arnalds, Happiness Does Not Wait; Einaudi, Divenire; The Cinematic Orchestra, Arrival of the Birds.
- Gen 6: Hania Rani, Letter to Glass; Beving, Ab Ovo; Beving, Losar; Arnalds, re:member; Arnalds, saman.

**Uruguay, first revision (superseded 21 September 2026)**
- Gen 2: Carlevaro, Aires de Vidalita; Milonga Oriental; Aire de Malambo; Improvisación por Milonga; El Orillero; Milonga del Negro Hilario; Campamento; Milonga de Bachicha; Dos de a caballo.
- Gen 3: Fattoruso, La Reunión; Recorriendo; Dos Orientales, Ten More Miles; Dos Orillas.
- Gen 3, second revision (superseded 22 September 2026, unavailable in every Spotify market): Cervetti, Guitar Music (The Bottom of the Iceberg); El Río de los Pájaros Pintados.
- Gen 4: Casenave, Balance; Visible; Noble; Universal.
- Gen 5 (tracks dropped): Supervielle, Sabelo.
- Gen 6 (tracks dropped): Fattoruso/Barrio Sur, Batuk 2; Candombe en Tres; Madera y Lonja.

**Uruguay, 22 September 2026 (superseded as too rhythmic to read over)**

Reserved under the flat rule against beat, which was dropped later the same day. These stay out on the reading test itself, not on a genre ban, but any of them can be reopened if a section's mood asks for it.
- Gen 4, second revision: Lamarque Pons, Sonatina (all three movements); Tosar, Gandhara (Diferencias sobre si bemol-mi); Sávio, Batucada.
- Gen 5, first revision: Supervielle, Sublimación; Resiliencia; Rondó Rodó; Otro Día en Uruguay; Pasaje Nocturno; La Edad del Cielo; Trébol de Cinco Hojas.
- Gen 6, first revision: Fattoruso/Barrio Sur, Palmereanas; Years Ago; 4 del 6; Afrocandombe de Octubre.

**Uruguay, Coldplay set (superseded 22 September 2026: no Uruguayan connection)**
- Gen 5: Coldplay (as recorded by Vitamin String Quartet), Lost!; Cemeteries of London; Strawberry Swing; Lovers in Japan; The Scientist.

**Uruguay, concert-music sets (superseded 22 September 2026, when the chapter moved to popular songs of each generation)**
- Gen 0: Fabini, Intermezzo; Triste Nº 1; Estudio Arpegiado; Triste Nº 2; Carlevaro, Preludios Americanos No. 1 "Evocación"; No. 3 "Campo".
- Gen 1: Broqua, Evocaciones Criollas No. 1 "Ecos del Paisaje"; Fabini, Campo.
- Gen 2: Tosar, Sonatina No. 2 (all three movements); Cuatro piezas para piano: Íntima; Dramática.
- Gen 3: Cervetti, … From the Earth …; Ofrenda para Guyunusa.
- Gen 4: Santórsola, Three Airs of Court: Prelude; Aria; Suite antiga: Preludio; Sarabanda; Sonata No. 4: Reverie.
- Gen 5: Lamarque Pons, Fuga a 3 voces; Storm, Quartet in F, Op. 7 (all three movements).
- Gen 6: Pazos Conde, Bajo Este Cielo; La Inundación de Cardozo Grande; Caja de Cartón I–V; Rincón de las Penas – Aire de Vidalita.

**Argentina (superseded 21 September 2026)**
- Gen 0: Troilo–Grela, Palomita Blanca; Mi Refugio; A Pedro Maffia; Nunca Tuvo Novio; Un Placer; Sobre el Pucho; La Cachila.
- Gen 1 (track dropped): Piazzolla, Bandoneón, Guitarra y Bajo.
- Gen 2: Piazzolla, Oblivion; Invierno Porteño; Libertango; Soledad.
- Gen 4 (track dropped): Spasiuk, Suite Nordeste, Pt. 3 & 4.
- Gen 5: Piazzolla (as recorded by Escalandrum), Buenos Aires Hora Cero; Lunfardo; Tanguedia 1 (as titled on Escalandrum's album); Vayamos al Diablo.
- Gen 6 (tracks dropped): Schissi, Árbol; Riel; Mirador.

**Argentina (superseded 22 September 2026 under the reading-first rule, since dropped)**

Same caveat: these were removed for having a beat or a band, not for failing the two tests at the top of the file. Spasiuk's chamamé, Santaolalla's "Seguir" and the Schissi quintet are the candidates worth reopening if a section wants them.
- Gen 1 (track dropped): Piazzolla, Tango Diablo.
- Gen 3: Saluzzi, Tango a mi padre (as "Tango A Mi Padre: Nocturno - Elegia"); Mundos; Lustrin.
- Gen 4: Spasiuk, El Camino; Suite Nordeste, Pt. 1 & 2; Tristeza; Panambí (Mariposa); Mejillas Coloradas.
- Gen 5 (track dropped): Santaolalla, Seguir.
- Gen 6: Schissi, Hijo; Aproximación; Salto; Hoja; Luz.

(The Tucumán reservation made under that rule — Juan Falú's eight pieces from *Con la guitarra que tengo* — was lifted on 22 September 2026 when the set was restored. The rule itself is gone; see the Selection rules.)

**Argentina, concert and chamber sets (superseded 22 September 2026, when the chapter moved to popular music of each generation)**
- Gen 0: Julián Aguirre, Aires nacionales argentinos, Op. 17, Vol. 1: Tristes Nos. 1–5; Guastavino, Sonatina in G minor: II; III.
- Gen 3: Saluzzi, Duetto; Carretas; Serenata.
- Gen 6: Golijov, Yiddishbbuk: L.B.; Tenebrae.

(Eduardo Falú's *Suite Argentina* was reserved here and is no longer: it is back in the active Generation 2.)

**Chile, 22 September 2026 (Generation 0 rebuilt on the people-and-mood rules)**
- Gen 0: Soro, Cuarteto en La Mayor: I. Allegro; II. Minueto. (The III. Andante is still in the active set.)

**Argentina, sets replaced on 22 September 2026 when the chapter was re-checked against the mood of each section**
- Gen 2/3: Leguizamón, La cantora de Yala; Zamba para la Viuda; Zamba soltera; Zamba del pañuelo. ("Zamba de Lozano", from the same set, is in the active Generation 3.)
- Gen 3 (track dropped): Gómez Carrillo and Falú, Vidala del Regreso — dropped only because Falú now has Generation 2.
- Tucumán: Juan Falú, Vidala del que no está; Vidalita del viento frío; Ayer es siempre; La memoria cuenta; Vida la de Lucho.

Only the compositions listed are reserved. Other tracks on the same albums were never selected and remain available. For example, "La Mufa" from the Philharmonic Hall concert is now in the active Argentina Generation 1, and the rest of *Ojos Negros* stays open apart from the four compositions now reserved.

### Superseded write-ups

The full write-ups of wholly replaced sets are kept below for the record, with their original headings demoted. Partial revisions are recorded only in the index above.

#### Georgia Gen 0, Mediator Duo set — Lelo Burti (c.1200–1928) · withdrawn 23 September 2026

Withdrawn for availability, not for taste: every track is country-restricted and does not play in South Africa. The Antonovka release is Russian. Kept for the record because the reasoning about Gurian polyphony still stands.

Total: **17:43**. Eleven short instrumental pieces for Georgian folk instruments, played by the Mediator Duo — Anri Karchava and Giorgi Tabatadze, two students recorded at the Georgian Technical University in Tbilisi on 28 February 2018 and released by the Russian label Antonovka Records in 2020. The instruments are the village ones: the chunduri played in panduri mode (plucked) and in chuniri mode (bowed), and the salamuri, the Georgian flute. The tunes are regional — Tushetian, Svanetian, Ossetian, Abkhazian, a shepherd's tune twice.

This is the generation with no institution and no recordings, so every choice is a later portrait; what it can be faithful to is the sound of a village rather than a concert hall. Georgia's famous music is its polyphonic singing, and Guria, where the chapter opens, has the most demanding polyphony in the country — but it is singing, so it is out under the one hard rule, and a rugby book cannot put a Gurian trio under a reader's page. What is left, honestly, is the instruments those singers' neighbours played.

The album's other eleven tracks are sung, by Keti Askilashvili and Gogi Miqeladze; do not use them. None of the tracks has a Spotify preview, so there are no profiles here: the label's own credits are the evidence for the instrumentation, and the pieces are short, quiet and unaccompanied by design. No track carries a country restriction.

Sulkhan Tsintsadze's *Miniatures on Georgian Folk Tunes* would also have fitted this generation, and are deliberately held back for Generation 2, where a Soviet Georgian composer writing his nation's tunes into a Soviet form is the whole point.

**Two things in this set that a Georgian reader will hear differently from an English one, and neither is a reason to drop them.** Track 5 is "Ossetian Tunes" and track 6 "Abkhazian Tunes", and Abkhazia and South Ossetia are the breakaway regions of the 1992–93 and 2008 wars that Generation 3 has to tell. This is not provocation: Georgian folk song is performed in six languages, Abkhazian and Ossetian among them, and those traditions are counted as part of Georgia's own musical inheritance because the peoples lived inside the Georgian kingdom for centuries. Cutting them would be editing a shared tradition for political neatness, which is not what this book does elsewhere. Second, Antonovka Records is a Russian label, which after 2008 and 2022 some Georgians would rather the music were not on; the recordings are Georgian musicians playing in Tbilisi, and there is no other release of them.

Added 22 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Intro (Shepherd's Tune) | Traditional Georgian | Giorgi Tabatadze, Anri Karchava | 0:44 | [Track](https://open.spotify.com/track/4uFSZSM8mezyHDaceMovCf) |
| 2 | Roots | Traditional Georgian | Giorgi Tabatadze, Anri Karchava | 1:55 | [Track](https://open.spotify.com/track/33gwqGC0fbCBXi8q3MD3Rl) |
| 3 | Record / Svan | Traditional Georgian | Giorgi Tabatadze, Anri Karchava | 1:57 | [Track](https://open.spotify.com/track/2Vf3oKzLs2SzTJRJT0QREc) |
| 4 | Tushetian Tunes 1 | Traditional Georgian | Anri Karchava | 2:31 | [Track](https://open.spotify.com/track/7yj0eq4Zsd0jbXDOulrZdc) |
| 5 | Ossetian Tunes | Traditional Georgian | Anri Karchava | 3:01 | [Track](https://open.spotify.com/track/1cpTrN4oPrqXhgVqUGUEDz) |
| 6 | Abkhazian Tunes | Traditional Georgian | Anri Karchava | 1:34 | [Track](https://open.spotify.com/track/545ppbYZApz041e1rMoCUO) |
| 7 | Tushetian Tune 2 | Traditional Georgian | Giorgi Tabatadze | 0:48 | [Track](https://open.spotify.com/track/3MZMMvINoIxZ0KiUegkBz3) |
| 8 | Bayati | Traditional Georgian | Anri Karchava | 1:30 | [Track](https://open.spotify.com/track/2jRGvA5C5waAm7gKMCIaJ2) |
| 9 | Tangerines | Traditional Georgian | Anri Karchava | 1:02 | [Track](https://open.spotify.com/track/4O1hr1eWhX1KLr4Si3Fdsn) |
| 10 | Shepherd's Tune | Traditional Georgian | Giorgi Tabatadze, Anri Karchava | 1:10 | [Track](https://open.spotify.com/track/3pbl0XLbr1BE2DFWWoWEC3) |
| 11 | Svanetian Nanila | Traditional Georgian | Anri Karchava | 1:31 | [Track](https://open.spotify.com/track/7iFi7l6cJwnmStIZi9QE2i) |

Why each track:

- Intro (Shepherd's Tune) — forty-four seconds of salamuri: Easter morning in the wet green hills above the Black Sea, before anything has started.
- Roots — plucked panduri, plain and repeating: eight hundred documented years, the ball-play in Rustaveli's epic, and a game nobody had to be taught.
- Record / Svan — the ball is carried in, blessed, and a shotgun goes off.
- Tushetian Tunes 1 — several hundred men take hold of it.
- Ossetian Tunes — the longest piece in the set, going almost nowhere: the mass moving a few metres in an hour.
- Abkhazian Tunes — into the stream, and out of it.
- Tushetian Tune 2 — a lone flute, three-quarters of a minute: a breath in the middle of the shoving.
- Bayati — the bowed chuniri, dark and pressing: the shove is the whole of the contest, and this is the sound the rest of Europe will one day be reluctant to face.
- Tangerines — the coast, the harvest, and a belief held long past the point anyone would defend it: that the winning half would have the better year.
- Shepherd's Tune — the whisper of the British, sailors at Batumi in the 1890s and dockers at Poti in the 1920s, plausible and unevidenced. It is the shortest thread in the chapter and gets the plainest tune.
- Svanetian Nanila — a lullaby on the bowed chuniri to close, because of where the ball goes when the game ends: carried to the cemetery and set on the grave of a villager who died that year. The prize is the right to give it away.

Spotify album: [Play, Panduri. Georgian Music from Tbilisi](https://open.spotify.com/album/3MxNQaFK052HzTox5u6llx). The same record is also listed under the duo's own name as [Play, Panduri: Georgian Music from Tbilisi](https://open.spotify.com/album/0lRHraKKxNMlrzE6C0QtCn); the track links above are the ones checked. Source: [Antonovka Records — Play, Panduri](https://antonovkarecords.bandcamp.com/album/play-panduri-georgian-music-from-tbilisi) (per-track instrument credits, the recording dates and places, and the line about Georgian urban folk music played by a younger generation of Tbilisi musicians).

Spotlistr input:

```text
Giorgi Tabatadze, Anri Karchava - Intro (Shepherd's Tune)
Giorgi Tabatadze, Anri Karchava - Roots
Giorgi Tabatadze, Anri Karchava - Record / Svan
Anri Karchava - Tushetian Tunes 1
Anri Karchava - Ossetian Tunes
Anri Karchava - Abkhazian Tunes
Giorgi Tabatadze - Tushetian Tune 2
Anri Karchava - Bayati
Anri Karchava - Tangerines
Giorgi Tabatadze, Anri Karchava - Shepherd's Tune
Anri Karchava - Svanetian Nanila
```

#### Georgia Gen 4, Kipiani set — The French Connection (1997–2006) · withdrawn 23 September 2026

Withdrawn for the same reason as the Generation 0 set above: every track is country-restricted.

Total: **20:14**. *Georgian National Instrumental Music*, played by David Kipiani and released in September 2006 — the last months of this generation. Panduri, salamuri and the rest, playing the regional repertoire: a Tushetian melody for panduri, an Adjaran melody, a highland women's dance, a travelling song from Imereti.

The reasoning is the generation's own. Claude Saurel's decision was to stop trying to build the game in Georgia and send the players into French clubs instead — big, cheap, technically excellent scrummagers, developed at somebody else's expense. What went to Montpellier and Toulon and Brive was not a system but a stream of young men, and what they took with them was this: the music of Tusheti and Adjara and Imereti, in a suitcase, a long way from home. The Yachvili household is the same story with the ends reversed — a grandfather who fought at Stalingrad, escaped a camp and settled in Corrèze, one grandson playing for Georgia and one for France.

All six tracks are unrestricted. Traditional tunes are named by region rather than by composer, so an exact overlap with the Generation 0 and Generation 2 sets cannot be ruled out; the obvious collisions ("Sachidao", "Khorumi", the shepherd's tunes, the Ossetian melodies) are avoided here on purpose.

Added 23 September 2026.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Dzveli Kartuli Sacekvao (Old Georgian Dance Music) | Traditional Georgian | David Kipiani | 2:52 | [Track](https://open.spotify.com/track/6YmRIGLy6n4MuvgWXuNt54) |
| 2 | Tushuri Safanduro (Tushetian Melody for Panduri) | Traditional Georgian | David Kipiani | 3:37 | [Track](https://open.spotify.com/track/5ih6KSwJ4jYCTPsjTV4KqB) |
| 3 | Ajaruli (Ajarian Melody) | Traditional Georgian | David Kipiani | 4:40 | [Track](https://open.spotify.com/track/3rvVPAepzfs7NWG50MFufV) |
| 4 | Mtiel Kalta Sacekvao (Highlander Women's Dance Music) | Traditional Georgian | David Kipiani | 2:51 | [Track](https://open.spotify.com/track/0hofi14LWZGVT2t63xhXbg) |
| 5 | Popuri Tushur Melodiebze (Tushetian Instrumental Melodies) | Traditional Georgian | David Kipiani | 4:13 | [Track](https://open.spotify.com/track/7aNh1cadtldLUrDFQnTo4x) |
| 6 | Imeruli Mgzavruli | Traditional Georgian | David Kipiani | 2:01 | [Track](https://open.spotify.com/track/6sj2YQmIYf3rPfpmyeCqNN) |

Why each track:

- Dzveli Kartuli Sacekvao — an old dance to open: 1997, a union with nothing, and a French adviser who had arrived in the ruins two years earlier.
- Tushuri Safanduro — one panduri, patient: the repechage against Tonga in 1999, lost in Nuku'alofa and won 28–27 in Tbilisi, and not enough.
- Ajaruli — the longest and warmest: 2001, the European championship, the first trophy the country ever won.
- Mtiel Kalta Sacekvao — a highland dance: 2003 in Australia, four matches against the best in the world, one try, and a defeat by Uruguay that stung more than the others.
- Popuri Tushur Melodiebze — a medley, one tune handed to the next: the pipeline into the French clubs, a generation of forwards made at somebody else's expense.
- Imeruli Mgzavruli — a travelling song from Imereti, two minutes, to close: the Yachvili brothers, one country each, and a border between them that was a matter of which passport a young man reached for.

Spotify album: [Georgian National Instrumental Music](https://open.spotify.com/album/2LyBaILC1R4d2pcFo3du2I).

Spotlistr input:

```text
David Kipiani - Dzveli Kartuli Sacekvao
David Kipiani - Tushuri Safanduro
David Kipiani - Ajaruli
David Kipiani - Mtiel Kalta Sacekvao
David Kipiani - Popuri Tushur Melodiebze
David Kipiani - Imeruli Mgzavruli
```

#### Chile Gen 0, Soro quartet set — The Ports and the Saltpetre (1892–1934) · superseded 22 September 2026

Replaced when Chile Generations 0 and 1 were re-checked against the people-and-mood rules. The Andante remains in the active set; the Allegro and Minueto are reserved.

Total: **19:52**. Unchanged. Three instrumental movements from Chilean composer Enrique Soro's *Cuarteto en La Mayor*, performed by the Chilean Cuarteto Terral. Soro wrote the quartet in 1903, inside this generation's dates, while completing his musical training in Milan. Its Chilean authorship and European Romantic form mirror a rugby culture carried into Chile through British shipping, commerce, clubs and schools before local institutions joined the scattered pieces together. This is the model for enclave generations elsewhere in the list. Profiles are calm (flux 0.41–0.50).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Cuarteto en La Mayor I Allegro | Enrique Soro | Cuarteto Terral | 8:32 | [Track](https://open.spotify.com/track/1UZF5wRDNpXmI13unyR0V5) |
| 2 | Cuarteto en La Mayor II Minueto | Enrique Soro | Cuarteto Terral | 5:16 | [Track](https://open.spotify.com/track/2r9qzNvfHKCMrSKgMW2QtI) |
| 3 | Cuarteto en La Mayor III Andante | Enrique Soro | Cuarteto Terral | 6:04 | [Track](https://open.spotify.com/track/50tY3aQ7sBGjFF65TFyMsz) |

Why each track:

- Allegro — vigorous but orderly, for rugby arriving repeatedly through Coronel, Iquique, Valparaíso and Concepción. Four independent string voices evoke the scattered ports before Chile had one institution to connect them.
- Minueto — formal and socially contained, matching the Union Club, the Prince of Wales Country Club and the imported codes of conduct that gave the game a narrow institutional home.
- Andante — lyrical and unresolved, for the schools and small clubs slowly preserving the game through forty years of delay. It closes without the quartet's finale because this generation ends before Chile's rugby structure is complete; the union arrives in 1935.

Soro was born in Concepción, close to the site of Chile's earliest documented match. Spotify album: [Obras de Enrique Soro y Jorge Peña Hen](https://open.spotify.com/album/4ZylkScqtEFR9h7yPidloT). Sources: [Fundación Enrique Soro — work page](https://fundacionenriquesoro.cl/obra/cuarteto-en-la-menor/) (the page's address says "la menor", but the page itself gives A major, 1903), [Fundación Enrique Soro — biography](https://fundacionenriquesoro.cl/fundacion/biografia/).

Spotlistr input:

```text
Enrique Soro, Cuarteto Terral - Cuarteto en La Mayor I Allegro
Enrique Soro, Cuarteto Terral - Cuarteto en La Mayor II Minueto
Enrique Soro, Cuarteto Terral - Cuarteto en La Mayor III Andante
```

#### Argentina Gen 2, Leguizamón zambas — The Porta Generation (1971–1987) · superseded 22 September 2026

In place for a few hours on 22 September 2026, between the first *Suite Argentina* set and its restoration. "Zamba de Lozano" moved into Generation 3.

Total: **22:20**. Zambas by Gustavo "Cuchi" Leguizamón (1917–2000), the Salta composer whose zambas are standards of Argentine folk song. They are played on solo guitar by Pablo Márquez, who was raised in Salta. ECM calls Leguizamón "a popular artist and a highly sophisticated musician". The album was recorded in Lugano in May 2012 and released in 2015: a later recording of songs the Porta generation grew up singing. The profiles are calm (flux 0.63–0.75), and the level is even. The tracks play in 182 markets.

Revised 22 September 2026. This set replaces Eduardo Falú's *Suite Argentina*, a concert suite. Falú's own zamba recordings were tried as well, but they are too strongly strummed to read over (flux 0.68–1.32).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | La cantora de Yala | Gustavo "Cuchi" Leguizamón | Pablo Márquez | 4:24 | [Track](https://open.spotify.com/track/5zn8DmjhA8OLOPYz4dN1vE) |
| 2 | Zamba de Lozano | Gustavo "Cuchi" Leguizamón | Pablo Márquez | 4:47 | [Track](https://open.spotify.com/track/0qe364Ne2IDOoYv26nPy5Q) |
| 3 | Zamba para la Viuda | Gustavo "Cuchi" Leguizamón | Pablo Márquez | 4:29 | [Track](https://open.spotify.com/track/60ugBB9j7Nlq1s6qMASnOU) |
| 4 | Zamba soltera | Gustavo "Cuchi" Leguizamón | Pablo Márquez | 4:06 | [Track](https://open.spotify.com/track/5ZOfDYFXsX4Q8QyuWrZenX) |
| 5 | Zamba del pañuelo | Gustavo "Cuchi" Leguizamón | Pablo Márquez | 4:34 | [Track](https://open.spotify.com/track/1x4aWiBvYVaJswiHMjtkoQ) |

Why each track:

- La cantora de Yala — the boy who turned down Boca Juniors and made his debut in 1971.
- Zamba de Lozano — the bans of 1971–73, and the union's committee forced to resign.
- Zamba para la viuda — the shadow Jaguars, Australia beaten in 1979, England held at Twickenham.
- Zamba soltera — the calmest: the loneliness of one man scoring every point.
- Zamba del pañuelo — the zamba is danced with a handkerchief. A warm close for Bloemfontein, the 21–21 against the All Blacks, and the series win over Australia in 1987.

Spotify album: [Gustavo Leguizamón: El Cuchi bien temperado](https://open.spotify.com/album/2bzQKVNP1gsAw7JhdPXdgE). Source: [ECM — El Cuchi bien temperado (recording, release, Leguizamón)](https://ecmrecords.com/product/gustavo-leguizamon-el-cuchi-bien-temperado-pablo-marquez/).

Spotlistr input:

```text
Pablo Marquez - La cantora de Yala
Pablo Marquez - Zamba de Lozano
Pablo Marquez - Zamba para la Viuda
Pablo Marquez - Zamba soltera
Pablo Marquez - Zamba del pañuelo
```

#### Argentina, The Interior: Tucumán, *Tucumano soy* set (1915–2026) · superseded 22 September 2026

In place for a few hours on 22 September 2026, between the first *Con la guitarra que tengo* set and its restoration.

Total: **20:53**. Solo guitar by Juan Falú, born in Tucumán in 1948 and nephew of Eduardo Falú (Generation 2), from *Tucumano soy* (Spotify dates it November 2025). The album goes with a book of his Tucumán works published by the Universidad Nacional de Tucumán's press, EDUNT. Several of its pieces appear twice, once sung by a guest singer and once by Falú alone; this set uses only tracks credited to Falú alone. The slow song forms of the northwest, the vidala and the vidalita, replace the dances. Profiles are calm (flux 0.40–0.65) and even (−13 to −15 LUFS). Vocals were not checked by ear; the solo credits point to guitar alone.

Revised 22 September 2026. This set replaces Falú's first album, *Con la guitarra que tengo* (1985–86). That set was the chapter's liveliest on purpose, cuecas and chacareras for the book's most passionate section, but dance rhythms pull attention off the page. The passion stays in the prose.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Vidala del que no está | Juan Falú | Juan Falú | 4:31 | [Track](https://open.spotify.com/track/7CnOX0q4tWXM92djX8LlBz) |
| 2 | Vidalita del viento frio | Juan Falú | Juan Falú | 5:09 | [Track](https://open.spotify.com/track/2GoBoOCIEMgpwPFdFnEBth) |
| 3 | Ayer es siempre | Juan Falú | Juan Falú | 3:23 | [Track](https://open.spotify.com/track/5pkfbcefan5RrGUIyDKJFq) |
| 4 | La memoria cuenta | Juan Falú | Juan Falú | 4:26 | [Track](https://open.spotify.com/track/5HeZ6FLYIHkfoaxenrrUr3) |
| 5 | Vida la de Lucho | Juan Falú | Juan Falú | 3:24 | [Track](https://open.spotify.com/track/6xcbKeNj9WDwIhHKUuWp6y) |

Why each track:

- Vidala del que no está — the calmest track in the set (flux 0.40): English students at the sugar mills, and a game that twice fell apart.
- Vidalita del viento frio — the longest, slow and steady: 1941–44, Natación y Gimnasia, Tucumán Rugby, Universitario and the new union, then the Anual Tucumano from 1944.
- Ayer es siempre — quiet and even: the long apprenticeship of coming south every year and losing, and *más que un club, una amistad*.
- La memoria cuenta — the most even in level: 5 October 1985 at Sáenz Peña, *la mística naranja* and the flood of titles, told as memory rather than celebration.
- Vida la de Lucho — a warm close: the ceiling Tucumán could never break, and the nine and the ten steering Argentina at Vélez in 2025.

Spotify album: [Tucumano soy](https://open.spotify.com/album/2uQikYRzQy7Gn7AMEyfJKI). "Vidala del que no está" and "Vida la de Lucho" each appear twice on the album; use the solo versions linked above (tracks 25 and 39), not the sung ones. Sources: [Fundación Konex — Juan Falú](https://www.fundacionkonex.org/b4294-juan-falu), [La Gaceta — *Tucumano soy* (EDUNT book of his Tucumán works)](https://www.lagaceta.com.ar/nota/1143970/espectaculos/tucumano-soy-testimonio-juan-falu-sobre-pertenencia.html).

Spotlistr input (the solo and sung versions share titles; check that each lands on the solo track):

```text
Juan Falú - Vidala del que no está
Juan Falú - Vidalita del viento frio
Juan Falú - Ayer es siempre
Juan Falú - La memoria cuenta
Juan Falú - Vida la de Lucho
```

#### Uruguay Gen 5, Coldplay set — The Plan (2007–2019) · superseded 22 September 2026

Total: **20:06**. Coldplay, the British band whose songs filled these years, in string-quartet versions by the Vitamin String Quartet (2008). It keeps the chapter's British thread running into the professional era: the players of the plan grew up with these songs, and many went on to play in Europe. The set uses the quartet's calmest tracks (flux 0.51–0.68). "The Scientist" comes from a second album and is mastered about 5 dB louder, so it closes the set.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Lost! | Coldplay | Vitamin String Quartet | 3:23 | [Track](https://open.spotify.com/track/0mbd46xBYSJFy3tmUlmI9u) |
| 2 | Cemeteries of London | Coldplay | Vitamin String Quartet | 3:05 | [Track](https://open.spotify.com/track/3VYqUFO5rtWrcQe9XxW4OJ) |
| 3 | Strawberry Swing | Coldplay | Vitamin String Quartet | 4:12 | [Track](https://open.spotify.com/track/2H5fBZHeaju4J3yw6WO7hs) |
| 4 | Lovers In Japan | Coldplay | Vitamin String Quartet | 4:33 | [Track](https://open.spotify.com/track/4VORn1Ec643DiJtZ8GqdU6) |
| 5 | The Scientist | Coldplay | Vitamin String Quartet | 4:53 | [Track](https://open.spotify.com/track/1pPHILjqSi7V6VCTVqh0wL) |

Why each track:

- Lost! — two failures, in 2007 and 2010, and a union starting again.
- Cemeteries of London — even and low: the long, unglamorous work of building the Charrúa base and a full-time squad.
- Strawberry Swing — light and steady: qualification cycles, and the climb past Russia and then Canada.
- Lovers in Japan — the World Cup in Japan: Kamaishi, and the Fiji upset. The title is a bonus; the track is here for its calm.
- The Scientist — the most familiar melody to close: the plan working.

Spotify albums: [Vitamin String Quartet Performs Coldplay's Viva La Vida](https://open.spotify.com/album/6QIK648ES8MNvYpqZF8Zy3), [Vitamin String Quartet Performs Coldplay, Vol. 02](https://open.spotify.com/album/3yYphIIgKsilhw1zVJaMCA).

Spotlistr input:

```text
Vitamin String Quartet - Lost!
Vitamin String Quartet - Cemeteries of London
Vitamin String Quartet - Strawberry Swing
Vitamin String Quartet - Lovers In Japan
Vitamin String Quartet - The Scientist
```

#### Uruguay Gen 0, concert-music set — The British Enclave (1842–1900) · superseded 22 September 2026

Total: **22:12**. Instrumental piano and guitar by Uruguayan composers Eduardo Fabini and Abel Carlevaro. Reflective, intimate music for distance, belonging and the world outside the enclave. These are later musical portraits of Uruguay, not compositions from 1842–1900. The compositions are unchanged from the earlier revision. The four Fabini pieces now come from modern studio recordings by Elida Gencarelli (*Música de Uruguay*, 2023) in place of the historical recordings, so the set is one clean-sounding pianist throughout. Fabini's use of Uruguayan folk idioms is documented by [Uruguay Educa](https://uruguayeduca.anep.edu.uy/sites/default/files/exelearning/06-2026/14578/su_obra.html); Carlevaro's background is documented by [GHA Records](https://www.gharecords.com/en/catalogue/evocacion/).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Intermezzo | Eduardo Fabini | Elida Gencarelli | 2:58 | [Track](https://open.spotify.com/track/5IBBqFZ3jaoxzp7cBPpev1) |
| 2 | Triste Nº 1 | Eduardo Fabini | Elida Gencarelli | 4:17 | [Track](https://open.spotify.com/track/0obCbkjFZr2XuKS6ULzTUR) |
| 3 | No. 1 - Evocación | Abel Carlevaro | Marcelo Cornut | 4:31 | [Track](https://open.spotify.com/track/2h6Wy2H7zlb2nMUBWgozRy) |
| 4 | Estudio Arpegiado | Eduardo Fabini | Elida Gencarelli | 1:48 | [Track](https://open.spotify.com/track/6rpppKIh7QhaDiz4S1ZeUT) |
| 5 | No. 3 - Campo | Abel Carlevaro | Marcelo Cornut | 3:37 | [Track](https://open.spotify.com/track/5GeWJejlm6aPi5YvBm12wh) |
| 6 | Triste Nº 2 | Eduardo Fabini | Elida Gencarelli | 5:01 | [Track](https://open.spotify.com/track/7Gp6Sr11NQ3tKPjUMDGZlh) |

Why each track:

- Intermezzo — a restrained piano opening for the small, inward-looking British enclave and the quiet beginnings of organised sport in Montevideo.
- Triste Nº 1 — Fabini wrote his early *Tristes* from memories of Uruguay while studying in Europe. That feeling of distance and attachment mirrors expatriates building institutions while looking back across the Atlantic.
- No. 1 - Evocación — a solitary guitar voice that gradually brings a Uruguayan musical identity into a generation dominated by British customs.
- Estudio Arpegiado — repeated arpeggios suggest routine, continuity and the patient work of sustaining a club through political disruption and a very small membership.
- No. 3 - Campo — shifts the imagination outside the enclave toward the land and the wider society that football would enter more readily than rugby.
- Triste Nº 2 — closes without triumph, and Gencarelli takes it slowly. Rugby survives, but remains behind the gate as football moves into public life.

Spotify albums: [Música de Uruguay](https://open.spotify.com/album/4KbuDEl0JCaM5lueiQ4t12), [Abel Carlevaro - Preludios Americanos](https://open.spotify.com/album/1K5kJfh1sXib0j1gDvAEtZ). Carlevaro's Campo is distinct from Fabini's orchestral work of the same name in Generation 1.

Spotlistr input:

```text
Elida Gencarelli - Intermezzo
Elida Gencarelli - Triste Nº 1
Marcelo Cornut - No. 1 - Evocación
Elida Gencarelli - Estudio Arpegiado
Marcelo Cornut - No. 3 - Campo
Elida Gencarelli - Triste Nº 2
```

#### Uruguay Gen 1, concert-music set — The Enclave Organizes (1900–1951) · superseded 22 September 2026

Total: **19:39**. Unchanged. A quiet guitar opening by Alfonso Broqua, followed by Eduardo Fabini's orchestral portrait of the country's landscape. Both are period works by Uruguayan composers: Broqua lived from 1876 to 1946, and *Campo* premiered in Montevideo in 1922 ([Uruguay Educa](https://uruguayeduca.anep.edu.uy/efemerides/se-estrena-campo-de-eduardo-fabini)). Broqua's national and folk context: [Uruguay Educa](https://uruguayeduca.anep.edu.uy/recursos/primaria-5o/alfonso-broqua-ecos-del-paisaje). The historical Shavitch recording stays in preference to the 2003 Montevideo Philharmonic recording under Federico García Vigil ([track](https://open.spotify.com/track/159e2gTeesAfbX8lu68eNP), 16:01). The older recording has a much narrower loudness range (about 5 LU against 12 in the previews), so its swells sit more evenly under reading. Choose the 2003 recording if surface noise bothers you more than the swells.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Broqua: Evocaciones Criollas: No. 1, Ecos del Paisaje | Alfonso Broqua | Oscar Cáceres | 3:25 | [Track](https://open.spotify.com/track/3bako0BFejdUOXFths7tWT) |
| 2 | Campo | Eduardo Fabini | Orquesta Sinfónica del Sodre, Vladimir Shavitch | 16:14 | [Track](https://open.spotify.com/track/39vbCM0tOtWUDxIPoCUqtu) |

Why each track:

- Ecos del Paisaje — solo guitar provides a modest opening for rugby's long institutional quiet, while Broqua's *Evocaciones criollas* place the sound in Uruguay rather than inside the old European enclave.
- Campo — the small guitar voice gives way to a full Uruguayan orchestra, matching the generation's slow change from isolated clubs toward a union, a continental competition and a national side. Its long, slow development suits a generation that takes half a century to organise. It is the one orchestral set in the Uruguay list.

Spotlistr input:

```text
Oscar Cáceres - Broqua: Evocaciones Criollas: No. 1, Ecos del Paisaje
Eduardo Fabini - Campo
```

#### Uruguay Gen 2, concert-music set — The Irish Brothers (1955–1971) · superseded 22 September 2026

Total: **19:14**. Solo piano by Héctor Tosar (1923–2002), the leading Uruguayan composer of the Brothers' generation, played by Leo Maslíah (2023). This is period repertoire: the Sonatina No. 2 dates from 1953, two years before Stella Maris opened, and the *Cuatro piezas para piano* from 1961–63, the years Old Christians took shape. Tosar's neoclassicism is music of formation. Clear forms, counterpoint and everything in its place suit an order that chose rugby as a curriculum. This set replaces Carlevaro's milongas and malambos, whose rural gaucho forms belonged to the countryside rather than to a Catholic school in Carrasco. Profiles are calm throughout (flux 0.50–0.63).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Sonatina nº 2 / I. Allegro Moderato - 1953 | Héctor Tosar | Leo Maslíah | 3:48 | [Track](https://open.spotify.com/track/6AiVy9D3WEcA25zK2VWFh5) |
| 2 | Sonatina nº 2 / II. Lento - Poco più animato e rubato - 1953 | Héctor Tosar | Leo Maslíah | 4:05 | [Track](https://open.spotify.com/track/4vJKRfWz3Or9koLr9bSMew) |
| 3 | Sonatina nº 2 / III. Presto / Allegro giocoso / … - 1953 | Héctor Tosar | Leo Maslíah | 5:28 | [Track](https://open.spotify.com/track/6QPvSrqnoeEMsCwSnFQ8Wv) |
| 4 | Cuatro piezas para piano 1961-1963 / Íntima | Héctor Tosar | Leo Maslíah | 1:56 | [Track](https://open.spotify.com/track/6FZRN4W6yAI53SfFwDq85k) |
| 5 | Cuatro piezas para piano 1961-1963 / Dramática | Héctor Tosar | Leo Maslíah | 3:57 | [Track](https://open.spotify.com/track/4XUs2WSFeLNOToDUkv409y) |

Why each track:

- Sonatina, I — a clear, orderly opening for a school built on routine and a small group of Brothers beginning their work.
- Sonatina, II — the reflective centre: the Brothers' reasoning that rugby formed character where football made stars.
- Sonatina, III — quick, playful and made of many short sections: boys in quantity, a school turning out teams year after year.
- Íntima — the shortest and quietest piece, for the modest purpose of Old Christians: leaving school should not mean leaving the game.
- Dramática — the widest dynamic range in the set, so the generation closes darkening toward October 1972. The title fits, but the piece is here for its weight.

Spotify album: [Héctor Tosar por Leo Maslíah](https://open.spotify.com/album/4qjltwt2lZ8d14sLoqQd52). Composition dates: [Centro de Documentación Musical — Tosar chronological catalogue](https://cdm.gub.uy/el-acervo/catalogos/partituras-de-hector-tosar/partituras-tosar-cronologico).

Spotlistr input:

```text
Leo Maslíah - Sonatina nº 2 / I. Allegro Moderato - 1953
Leo Maslíah - Sonatina nº 2 / II. Lento - Poco più animato e rubato - 1953
Leo Maslíah - Sonatina nº 2 / III. Presto / Allegro giocoso / Semplice e tranquillo / Non troppo mosso / Più mosso / Allegro giocoso - 1953
Leo Maslíah - Cuatro piezas para piano 1961-1963 / Íntima
Leo Maslíah - Cuatro piezas para piano 1961-1963 / Dramática
```

#### Uruguay Gen 3, concert-music set — The Mountain (1972–1988) · superseded 22 September 2026

Total: **20:15**. Two works by the Uruguayan composer Sergio Cervetti (born Dolores, 1940; studied in Montevideo with Carlos Estrada and Guido Santórsola; in New York from 1970). *…from the earth…*, for chamber ensemble, was composed in 1972, the year of the crash. It was Cervetti's first minimalist piece: a five-note passage from Mahler's *Das Lied von der Erde* drawn out slowly into new melodies and harmonies. *High Fidelity* called it "a straightforward and touching composition". *Ofrenda para Guyunusa*, for harpsichord, is a later portrait from 2011, premiered in Montevideo in 2012. It is an offering to Guyunusa, a Charrúa woman taken from Uruguay in the 19th century who died far from home. Both profile calm (flux 0.40–0.59) and are available in 185 Spotify markets.

Revised 22 September 2026. The first Cervetti pairing (*Guitar Music* and *El Río de los Pájaros Pintados*, from the album *Transits*) turned out to be country-restricted in every market, which is also why neither had a preview. Both are reserved against reuse.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | … From the Earth … | Sergio Cervetti | Chamber ensemble conducted by Sergio Cervetti | 14:50 | [Track](https://open.spotify.com/track/3twrDVM4M6xmeDwDLYYt6J) |
| 2 | Ofrenda para Guyunusa | Sergio Cervetti | María Teresa Chenlo (harpsichord) | 5:25 | [Track](https://open.spotify.com/track/4MTmuJUa2yKQNjWhmUfYR8) |

The ensemble is flute (Jon Gibson), oboe, two clarinets, bassoon, trombone, viola and double bass, with Cervetti on electric organ. It is fully instrumental.

Why each track:

- … From the Earth … — fifteen minutes of a few notes slowly turned over, low and steady with no beat: the fuselage, the waiting, the days counted, the trek. It draws on Mahler's song of farewell, but it is here for its stillness.
- Ofrenda para Guyunusa — a quiet harpsichord lament to close: the dead on the mountain, and the story the world took away with it.

Spotify albums: [Cervetti: Unbridled](https://open.spotify.com/album/0xhKwuyUvF6dNOmUFwz2hf), [Sergio Cervetti: Sunset at Noon](https://open.spotify.com/album/6IJTjA1yvQTEX3F8W1rEEw). Sources: [Navona Records — Unbridled (premiere 1973; the High Fidelity quotation)](https://www.navonarecords.com/catalog/nv5958/), [Unbridled booklet (instrumentation and 1972 date; notes on *Ofrenda para Guyunusa*)](https://www.navonarecords.com/legacy-catalog/unbridled/booklet.html), [Encyclopedia.com — Cervetti biography](https://www.encyclopedia.com/arts/dictionaries-thesauruses-pictures-and-press-releases/cervetti-sergio).

Spotlistr input:

```text
Sergio Cervetti - … From the Earth …
María Teresa Chenlo - Ofrenda para Guyunusa
```

#### Uruguay Gen 4, concert-music set — Getting on the Map (1989–2003) · superseded 22 September 2026

Total: **21:10**. Solo guitar music by Guido Santórsola (1904–1994), played by the Argentine guitarist María Isabel Siewers on an album Spotify dates July 2003, the year of Uruguay's second World Cup. Santórsola was born in Italy and grew up in Brazil. In 1931 the SODRE orchestra hired him as principal viola, and he settled in Montevideo for good; he is counted as "uruguayo por adopción". He taught musicians who took Uruguayan music abroad, among them the guitarist Eduardo Fernández and Sergio Cervetti (Generation 3). The works date from 1945 to 1977: the *Three Airs of Court* (1966), the Sonata No. 4 (1977) and the *Suite antiga* (1945, revised 1975). The recording falls inside this generation's dates. All five pieces are slow or moderate and written in an old courtly manner: two preludes, an aria, a reverie and a sarabande. Profiles are calm for the guitar (flux 0.65–0.81; plucked strings score higher than piano at the same calm).

Revised 22 September 2026. This set replaces Eduardo Fernández's 1989 recording of Lamarque Pons, Tosar and Sávio. It fitted the story, but "Ritmico", "Batucada" and the spiky ten-minute *Gandhara* kept pulling attention off the page.

This is a quiet recording (−24 to −27 LUFS in the previews), so raise the volume relative to the other sets.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | I. Prelude (*Three Airs of Court*, 1966) | Guido Santórsola | María Isabel Siewers | 4:35 | [Track](https://open.spotify.com/track/1rNv1CkvISviJS9FH0MhDn) |
| 2 | II. Aria (*Three Airs of Court*, 1966) | Guido Santórsola | María Isabel Siewers | 2:36 | [Track](https://open.spotify.com/track/5j66HJ6Q2pt0FLZmDLWo8d) |
| 3 | I. Preludio (*Suite antiga*, 1945, revised 1975) | Guido Santórsola | María Isabel Siewers | 5:07 | [Track](https://open.spotify.com/track/3Sr6nKsyIJtwYok2z6ZUE7) |
| 4 | II. Reverie (Sonata No. 4, 1977) | Guido Santórsola | María Isabel Siewers | 5:43 | [Track](https://open.spotify.com/track/7lByjjqh0LSKXH4g91TR2d) |
| 5 | IV. Sarabanda (*Suite antiga*) | Guido Santórsola | María Isabel Siewers | 3:09 | [Track](https://open.spotify.com/track/3Ksdx5ext5hPappH4Qz21h) |

Why each track:

- Prelude — measured and unhurried: a small union admitted to the IRB in 1989 and handed, at last, a qualifying pathway.
- Aria — short and singing, for Diego Ormaechea: forty years old, playing since 1979, scoring Uruguay's first World Cup try.
- Preludio — even, patient figuration with the narrowest loudness range in the set: the wins over Spain in 1999 and Georgia in 2003, ground out through the forwards.
- Reverie — the longest and most inward piece: the reckoning with the professional game, the 111–13 in Brisbane.
- Sarabanda — a slow, dignified dance to close. Santórsola came to Uruguay from abroad and stayed; Pablo Lemoine took the road the other way when he signed for Bristol.

Spotify album: [Santorsola: Guitar Music](https://open.spotify.com/album/3bnBJqaj7sPI98yp3zqTIv) (BIS-CD-1178). Spotify also carries a second copy of this album with fuller track titles (album ID 4t07vOglzp5xVwEXg7V8Gv). Do not use it: its Aria is country-restricted. Sources: [María Isabel Siewers — recordings (composition dates, BIS catalogue number)](https://www.isabelsiewers.com/recordings/recordings_128k.html), [María Isabel Siewers — profile](https://www.isabelsiewers.com/profile/profile.html), [Historia de la Sinfonía — Santórsola](http://www.historiadelasinfonia.es/naciones/uruguay/santorsola/), [Orquesta Filarmónica de Montevideo — Eduardo Fernández](https://orquestafilarmonica.montevideo.gub.uy/evento/eduardo-fernandez-sus-50-anos-de-actividad-artistica).

Spotlistr input (Spotify's short titles can match the wrong copy; check that each lands on the album linked above, or use the track links):

```text
Guido Santorsola - I. Prelude
Guido Santorsola - II. Aria
Guido Santorsola - I. Preludio
Guido Santorsola - II. Reverie
Guido Santorsola - IV. Sarabanda
```

#### Uruguay Gen 5, concert-music set — The Plan (2007–2019) · superseded 22 September 2026

Total: **19:35**. A Montevideo string quartet plays Uruguayan composers. Cuarteto Aramis was formed in 2011: violinists Carolina Hasaj and Silvia Blanco, violist Bruno González and cellist Matías Fernández. Its album *Compositores Uruguayos* was presented at the Centro Cultural de España in Montevideo in June 2018, and Spotify dates the release May 2019, so the recording belongs to this generation. A short fugue by Jaurés Lamarque Pons (1917–1982) opens, and Ricardo Storm's complete Quartet in F, Op. 7, follows. Storm (1930–2000) studied composition in Montevideo with the Spanish composer Enrique Casal Chapí, and his style is described as "universalist … sober in its musical language". Neither work's date appears in the sources checked, so treat them as twentieth-century repertoire in a recording from the generation itself. Four players, each with a distinct part, build one structure: the sound of a system rather than a star. It is the only string quartet in the Uruguay list. Profiles are calm (flux 0.42–0.61). The Largo has the widest swells (a loudness range of about 15 LU in the preview), so set the volume during it.

Revised 22 September 2026. This set replaces Luciano Supervielle's *Suite para Piano & Pulso Velado*. Its electronic pulse ran under every track, and Spotify lists the album for Uruguay only.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Fuga a 3 Voces | Jaurés Lamarque Pons | Cuarteto Aramis | 2:59 | [Track](https://open.spotify.com/track/5deLpqsju2p9BzCQ1luKvX) |
| 2 | Cuarteto en Fa Op. 7: Allegro non troppo | Ricardo Storm | Cuarteto Aramis | 5:38 | [Track](https://open.spotify.com/track/53i5GrQTXscghNmgWkZp23) |
| 3 | Cuarteto en Fa Op. 7: Largo | Ricardo Storm | Cuarteto Aramis | 5:40 | [Track](https://open.spotify.com/track/14qj7DxSdLbWtlErhtGd0A) |
| 4 | Cuarteto en Fa Op. 7: Allegro vivace | Ricardo Storm | Cuarteto Aramis | 5:18 | [Track](https://open.spotify.com/track/7GQ3txtfP1UYTrEVitg4m4) |

Why each track:

- Fuga a 3 Voces — three voices enter one after another and lock together: rebuilding after the failures of 2007 and 2010, one layer at a time.
- Allegro non troppo — steady and moderate: the long, unglamorous work of building the Charrúa base and a full-time squad.
- Largo — the slow centre, with the widest dynamic range in the set: the qualification cycles, and the climb past Russia and then Canada.
- Allegro vivace — the liveliest movement, still restrained: the growing belief, then Kamaishi and the Fiji upset.

Spotify album: [Compositores Uruguayos](https://open.spotify.com/album/4iqCAMmtKX5lmsFElkzj2y). Its other works (Lamarque Pons's miniature quartets and *Tema de Tango*, Alberto Viña's flamenco suite, Felipe Ortiz's quartet) are not used. Sources: [Centro Cultural de España en Montevideo — album presentation](https://ccemontevideo.aecid.es/-/-compositores-uruguayos-de-cuarteto-aramis.), [Encyclopedia.com — Ricardo Storm](https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/storm-ricardo-1930-2000).

Spotlistr input:

```text
Cuarteto Aramis - Fuga a 3 Voces
Cuarteto Aramis - Cuarteto en Fa Op. 7: Allegro non troppo
Cuarteto Aramis - Cuarteto en Fa Op. 7: Largo
Cuarteto Aramis - Cuarteto en Fa Op. 7: Allegro vivace
```

#### Uruguay Gen 6, concert-music set — The Branches Rejoin (2020–2026) · superseded 22 September 2026

Total: **21:03**. Solo guitar by the Uruguayan guitarist Gustavo Pazos Conde, from *Rincón de las Penas*, the third volume of his *Guitar Works from Uruguay* (Saphrane). Spotify dates it October 2023, so this is contemporary music recorded inside the generation's dates. Apple Music's credits list all eight tracks used here as his own compositions. The album's Peruvian yaraví and its pieces by the Argentines Ernesto Snajer and Dino Saluzzi are not used. The music grows out of the gaucho guitar forms of the Uruguayan and Argentine countryside: the estilo, the milonga, the vidalita. The label calls the album a vision of "several musical traditions of the Gaucho". *Songlines* described his first album as "quietly intense, rippling with fragile minor chords and unafraid of silence". The chapter ends where Generation 0 began, with a single guitar. There the guitar looked out from the enclave toward the campo. Here it plays the country's own forms: the national game and the national music, on the same side of the gate at last. Level and density are even throughout (−14 to −16 LUFS; flux 0.68–0.92, the same range as the other guitar sets).

Revised 22 September 2026. This set replaces the candombe of Hugo Fattoruso, Albana Barrocas and Barrio Sur. Candombe fitted the story, but its drums and jazz-fusion keyboard made it the hardest music in the list to read over.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Bajo Este Cielo | Gustavo Pazos Conde | Gustavo Pazos Conde | 3:48 | [Track](https://open.spotify.com/track/3VYALSvdMZFIVRWmdgf6ru) |
| 2 | La Inundacion de Cardozo Grande | Gustavo Pazos Conde | Gustavo Pazos Conde | 3:25 | [Track](https://open.spotify.com/track/2WUSmTkZV9xJp49lfPMJM5) |
| 3 | Caja de Carton I | Gustavo Pazos Conde | Gustavo Pazos Conde | 1:38 | [Track](https://open.spotify.com/track/6sY3Be0fQhW5aZGh1rGqQZ) |
| 4 | Caja de Carton II | Gustavo Pazos Conde | Gustavo Pazos Conde | 1:47 | [Track](https://open.spotify.com/track/2jbk9HONlZfnAvY3pcshAC) |
| 5 | Caja de Carton III | Gustavo Pazos Conde | Gustavo Pazos Conde | 2:29 | [Track](https://open.spotify.com/track/6qsmXFY18CZPIOJlkbbdy2) |
| 6 | Caja de Carton IV | Gustavo Pazos Conde | Gustavo Pazos Conde | 1:59 | [Track](https://open.spotify.com/track/5uVsBmwd0MfeaqQU8Qqzh3) |
| 7 | Caja de Carton V | Gustavo Pazos Conde | Gustavo Pazos Conde | 2:36 | [Track](https://open.spotify.com/track/54cXSd1XTnm1KdkyvMFBjQ) |
| 8 | Rincon de Las Penas - Aire de Vidalita | Gustavo Pazos Conde | Gustavo Pazos Conde | 3:21 | [Track](https://open.spotify.com/track/52Ibu3F30qV0i4bI13ikih) |

Why each track:

- Bajo Este Cielo — an estilo, the slowest and most song-like of the rural forms, and the album's opening track: the black-and-gold jersey, and the railwaymen's club putting a professional rugby team on the field.
- La Inundacion de Cardozo Grande — a milonga, a form that town and countryside share: weekly professional competition at last, and three Super Rugby Americas titles.
- Caja de Carton I–V — a suite of five short pieces, played complete: many small parts making one whole, as a squad is built from its clubs. It carries the comeback against Namibia in Lyon and a sixth consecutive World Cup qualification.
- Aire de Vidalita — the vidalita is a plaintive song form, and this is a quiet close: homegrown players and the mid-2026 snapshot.

Spotify album: [Rincon de las Penas](https://open.spotify.com/album/7BbQzMnZLQp9tLqEdu6tEL). "Bajo Este Cielo" appears twice on the album; use the opening track (the closing one is spelled "Bajo Esta Cielo" on Spotify). Sources: [Apple Music — Rincón de las Penas (composer credits)](https://music.apple.com/us/album/rincon-de-las-penas/1708391923), [Sonic Rendezvous — track list with forms](https://www.sonicrendezvous.com/product/pazos-conde-gustavo/rincon-de-las-penas-guitar-works-from-uruguay-iii/585386), [Proper Music — album description](https://propermusic.com/products/gustavopazosconde-rincondelaspenas), [Proper Music — *Estación Edén* (the *Songlines* quotation)](https://propermusic.com/products/gustavopazosconde-estacionedenguitarworksfromuruguayii).

Spotlistr input:

```text
Gustavo Pazos Conde - Bajo Este Cielo
Gustavo Pazos Conde - La Inundacion de Cardozo Grande
Gustavo Pazos Conde - Caja de Carton I
Gustavo Pazos Conde - Caja de Carton II
Gustavo Pazos Conde - Caja de Carton III
Gustavo Pazos Conde - Caja de Carton IV
Gustavo Pazos Conde - Caja de Carton V
Gustavo Pazos Conde - Rincon de Las Penas - Aire de Vidalita
```

#### Uruguay Gen 4, second revision — Getting on the Map (1989–2003) · superseded 22 September 2026

Total: **20:20**. A period recording: Uruguayan guitarist Eduardo Fernández playing Uruguayan-born composers, on an album from his Decca years that Spotify dates October 1989, the year the chapter gives for Uruguay joining the IRB. Fernández studied with Abel Carlevaro, Guido Santórsola and Héctor Tosar, won the Segovia competition in 1975, and his 1983 Wigmore Hall debut led to an exclusive Decca contract. He was a Uruguayan making his career on the international stage in exactly the years Uruguay's rugby tried to. All three composers were born in Uruguay: Jaurés Lamarque Pons (1917–1982); Héctor Tosar, who wrote *Gandhara* for Fernández in 1984; and Isaías Sávio (1900–1977), who built his career in Brazil. This set replaces Gustavo Casenave's *Balance* (2019). Every one of that album's eleven tracks has a one-word abstract title, and four were chosen for their words.

This is a quiet recording (−22 to −28 LUFS in the previews), so raise the volume relative to the other sets. Tosar recurs from Generation 2 with a different work.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Sonatina: 1. Lento: Allegro moderato | Jaurés Lamarque Pons | Eduardo Fernández | 2:17 | [Track](https://open.spotify.com/track/2mytGP2DXyewbuNYRhSLgN) |
| 2 | Sonatina: 2. Lento | Jaurés Lamarque Pons | Eduardo Fernández | 2:36 | [Track](https://open.spotify.com/track/34nISryrxKSAF8VjRDDgG2) |
| 3 | Sonatina: 3. Ritmico | Jaurés Lamarque Pons | Eduardo Fernández | 2:12 | [Track](https://open.spotify.com/track/2g104iIPJFojVUSSwO3B0B) |
| 4 | Gandhara (Diferencias sobre si bemol-mi) | Héctor Tosar | Eduardo Fernández | 10:26 | [Track](https://open.spotify.com/track/31jVb0GGbV0oaUVl9sjdG4) |
| 5 | Batucada | Isaías Sávio | Eduardo Fernández | 2:49 | [Track](https://open.spotify.com/track/2ZswwpEoUJWaM5e4xGAcxw) |

Why each track:

- Sonatina, 1 — compact and forward-moving: a small country handed, at last, a qualifying pathway.
- Sonatina, 2 — the slow centre, for Diego Ormaechea: forty years old, playing since 1979, scoring Uruguay's first World Cup try.
- Sonatina, 3 — the most rhythmic piece in the set: the win over Spain in 1999 and the win over Georgia in 2003, ground out through the forwards.
- Gandhara — ten minutes of variations on two notes a tritone apart: searching, modern and unresolved. It stands for the reckoning with the professional game, the 111–13 in Brisbane. It is the most demanding piece in the Uruguay list, so lower the volume if it intrudes.
- Batucada — a brief, bright close by a Uruguayan-born guitarist who made his career abroad. That was the road Pablo Lemoine took when he signed for Bristol.

Spotify album: [Ponce: Variations & Fugue On "La Folia" / Brouwer / Lamarque-Pons: Sonatina etc](https://open.spotify.com/album/4uDOLx4jPD2XguZaKhKi14); the Ponce and Brouwer works are not used. Sources: [Orquesta Filarmónica de Montevideo — Eduardo Fernández](https://orquestafilarmonica.montevideo.gub.uy/evento/eduardo-fernandez-sus-50-anos-de-actividad-artistica), [Library of Congress — Isaías Sávio](https://guides.loc.gov/latin-american-composers-primary-sources/brazil/savio), [Tosar chronological catalogue](https://cdm.gub.uy/el-acervo/catalogos/partituras-de-hector-tosar/partituras-tosar-cronologico).

Spotlistr input:

```text
Eduardo Fernandez - Sonatina: 1. Lento: Allegro moderato
Eduardo Fernandez - Sonatina: 2. Lento
Eduardo Fernandez - Sonatina: 3. Ritmico
Eduardo Fernandez - Gandhara (Diferencias sobre si bemol-mi)
Eduardo Fernandez - Batucada
```

#### Uruguay Gen 5, first revision — The Plan (2007–2019) · superseded 22 September 2026

Total: **19:44**. Piano and restrained electronic pulse by Uruguay-based musician Luciano Supervielle, from a 2016 album released inside this generation's dates. Acoustic piano over programmed rhythm matches the chapter's combination of an old amateur culture with a new high-performance system. Uruguay's Ministry of Education and Culture describes the work as piano with a "veiled pulse" of electronic instruments. Revised in September 2026: "Sabelo" is dropped. It is the one track on the album where the pulse takes over, bright and percussive, and it profiled busier than the candombe drums (flux 1.50). "Pasaje Nocturno" and "La Edad del Cielo" replace it, both calm (0.61–0.66). **Availability warning:** Spotify's page metadata lists this album for Uruguay only, although its player reported the tracks as playable when checked. If they will not play in your region, this is why.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Sublimación | Luciano Supervielle | Luciano Supervielle | 3:17 | [Track](https://open.spotify.com/track/1Hu7I367lhkXMcvJ1SMCst) |
| 2 | Resiliencia | Luciano Supervielle | Luciano Supervielle | 3:28 | [Track](https://open.spotify.com/track/0Ve9CDieP4JMaFLItLlDta) |
| 3 | Rondó Rodó | Luciano Supervielle | Luciano Supervielle | 3:19 | [Track](https://open.spotify.com/track/0dyYcHHEYoqSnhvv9stZle) |
| 4 | Otro Día en Uruguay | Luciano Supervielle | Luciano Supervielle | 2:15 | [Track](https://open.spotify.com/track/2s6rybY8HMqBrdrznuluw6) |
| 5 | Pasaje Nocturno | Luciano Supervielle | Luciano Supervielle | 2:32 | [Track](https://open.spotify.com/track/0cZ4qkSrInx9k44GyBTpsW) |
| 6 | La Edad del Cielo | Luciano Supervielle | Luciano Supervielle | 2:37 | [Track](https://open.spotify.com/track/415gbOBoFXFZRTHd0w52cz) |
| 7 | Trébol de Cinco Hojas | Luciano Supervielle | Luciano Supervielle | 2:16 | [Track](https://open.spotify.com/track/0TjFQGYI9a43oZXo55khYv) |

Why each track:

- Sublimación — piano with the pulse present from the first bars: two failures, in 2007 and 2010, turned into structure.
- Resiliencia — one of the steadiest tracks on the album: the long, unglamorous work of building the Charrúa base and a full-time squad.
- Rondó Rodó — a rondo keeps coming back to its theme, as training and qualification cycles did. The nod to the writer José Enrique Rodó is a bonus.
- Otro Día en Uruguay — short and quiet: ordinary days of preparation, not a single miracle.
- Pasaje Nocturno — even and low-lit: the climb, with qualification past Russia and then Canada.
- La Edad del Cielo — quieter, with more lift: the growing belief that the plan works.
- Trébol de Cinco Hojas — a light, brief close for Kamaishi and the Fiji upset.

Spotify album: [Suite para Piano & Pulso Velado](https://open.spotify.com/album/5DVBeIh33EmNJq5JvcYuRI). Sources: [Uruguay MEC description](https://www.gub.uy/ministerio-educacion-cultura/comunicacion/noticias/arte-2016), [Supervielle interview about the piano and electronic pulse](https://enperspectiva.uy/enperspectiva-uy/entrevista-central-martes-22-de-noviembre-luciano-supervielle/6/).

Spotlistr input:

```text
Luciano Supervielle - Sublimación
Luciano Supervielle - Resiliencia
Luciano Supervielle - Rondó Rodó
Luciano Supervielle - Otro Día en Uruguay
Luciano Supervielle - Pasaje Nocturno
Luciano Supervielle - La Edad del Cielo
Luciano Supervielle - Trébol de Cinco Hojas
```

#### Uruguay Gen 6, first revision — The Branches Rejoin (2020–2026) · superseded 22 September 2026

Total: **19:46**. Contemporary instrumental candombe by a Uruguayan ensemble led by Hugo Fattoruso with Albana Barrocas and Barrio Sur. The linked album is *Barrio Sur (Remezclado)*, a remixed edition of an earlier album released in October 2021, inside this generation's dates. Candombe is the right genre for the chapter's ending. It carries the national portrait beyond the elite institutions that held rugby for most of the chapter, into the popular Montevideo that Peñarol belongs to. UNESCO identifies it as a Uruguayan musical celebration and collective practice rooted in Montevideo's Barrio Sur, Palermo and Cordón. It is the one deliberately rhythmic set in the Uruguay list. Revised in September 2026: the tracks were re-chosen from the less dense end of the album. "Batuk 2" and "Candombe en Tres" (the album's two busiest tracks, flux 1.34–1.39) and "Madera y Lonja" are dropped.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Palmereanas | Hugo Fattoruso and ensemble | Hugo Fattoruso, Albana Barrocas, Barrio Sur | 2:46 | [Track](https://open.spotify.com/track/5Jqc7YBvlqYADAmxiRYGEt) |
| 2 | Years Ago | Hugo Fattoruso and ensemble | Hugo Fattoruso, Albana Barrocas, Barrio Sur | 5:00 | [Track](https://open.spotify.com/track/27t8HfxHu2pQy7EcLrbXBO) |
| 3 | 4 del 6 | Hugo Fattoruso and ensemble | Hugo Fattoruso, Albana Barrocas, Barrio Sur | 5:17 | [Track](https://open.spotify.com/track/046eZVHb0NT5oWodV1MfJe) |
| 4 | Afrocandombe de Octubre | Hugo Fattoruso and ensemble | Hugo Fattoruso, Albana Barrocas, Barrio Sur | 6:43 | [Track](https://open.spotify.com/track/4eYKtdgAiPAMYIM3wrY67n) |

Why each track:

- Palmereanas — the quietest track on the album, and short: the black-and-gold jersey, and the railwaymen's club putting a professional rugby team on the field.
- Years Ago — steady and even (the narrowest loudness range on the album): weekly professional competition at last, and three Super Rugby Americas titles.
- 4 del 6 — tightly coordinated parts, a system working as one. It fits the comeback against Namibia in Lyon and a sixth consecutive World Cup qualification.
- Afrocandombe de Octubre — the longest and fullest piece: homegrown players, the mid-2026 snapshot, and the collective sound of the city the game finally reached.

Spotify album: [Barrio Sur (Remezclado)](https://open.spotify.com/album/3zG8VWhHhk8ww3iiOxzpSP). Source on national tradition: [UNESCO — Candombe and its socio-cultural space](https://ich.unesco.org/en/RL/candombe-and-its-socio-cultural-space-a-community-practice-00182).

Spotlistr input:

```text
Hugo Fattoruso, Albana Barrocas, Barrio Sur - Palmereanas
Hugo Fattoruso, Albana Barrocas, Barrio Sur - Years Ago
Hugo Fattoruso, Albana Barrocas, Barrio Sur - 4 del 6
Hugo Fattoruso, Albana Barrocas, Barrio Sur - Afrocandombe de Octubre
```

#### Uruguay Gen 2, first revision — The Irish Brothers (1955–1971) · superseded 21 September 2026

Total: **19:46**. Uruguayan guitarist Abel Carlevaro moves from solo guitar into duos and a trio. The changing ensemble mirrors the generation's story: the Brothers build a school, the school produces a team, and the team becomes a club. Milonga and other Río de la Plata forms keep the sound rooted in Uruguay; the Irish identity belongs to the institution and does not replace the country's musical voice.

All recordings come from [Música Popular del Río de la Plata](https://open.spotify.com/album/1uIVo1zrQbY2ujZXIW8Iqq). All nine compositions are new to the master list. Spotify titles, credits and durations checked; account playback not tested.

| Order | Track | Performing artist | Duration |
|---|---|---|---|
| 1 | Aires de Vidalita | Abel Carlevaro | 3:12 |
| 2 | Milonga Oriental | Abel Carlevaro | 2:07 |
| 3 | Aire de Malambo | Abel Carlevaro | 1:50 |
| 4 | Improvisación por Milonga - Dúo de Guitarras | Abel Carlevaro, Agustín Carlevaro | 3:08 |
| 5 | El Orillero - Dúo de Guitarras | Abel Carlevaro | 1:46 |
| 6 | Milonga del Negro Hilario - Dúo de Guitarras | Abel Carlevaro | 2:49 |
| 7 | Campamento - Dúo de Guitarras | Abel Carlevaro | 2:08 |
| 8 | Milonga de Bachicha - Trío de Guitarras | Abel Carlevaro | 1:30 |
| 9 | Dos de a caballo - Dúo de Guitarras | Abel Carlevaro | 1:16 |

Why each track:

- Aires de Vidalita — a gentle, distinctly regional opening for the Brothers arriving and beginning their work quietly.
- Milonga Oriental — “Oriental” connects directly to Uruguay's formal name and national identity; the steady pulse suits the school taking shape.
- Aire de Malambo — adds disciplined movement for rugby becoming part of the Brothers' curriculum.
- Improvisación por Milonga — the first duet marks the change from individual formation to cooperation; the two Carlevaro brothers also echo the generation's brotherhood theme without pretending to be Irish music.
- El Orillero — compact, alert ensemble playing for the game moving beyond its old British custodians.
- Milonga del Negro Hilario — a warmer duet that broadens the sound toward the Río de la Plata rather than returning to European enclave music.
- Campamento — the title and closely linked guitars suggest a group learning, working and staying together.
- Milonga de Bachicha — the trio expands the texture as Stella Maris begins producing teams and a lasting rugby community.
- Dos de a caballo — a brief paired-guitar coda for Old Christians emerging from the school and carrying the game forward.

Spotlistr input:

```text
Abel Carlevaro - Aires de Vidalita
Abel Carlevaro - Milonga Oriental
Abel Carlevaro - Aire de Malambo
Abel Carlevaro, Agustín Carlevaro - Improvisación por Milonga - Dúo de Guitarras
Abel Carlevaro - El Orillero - Dúo de Guitarras
Abel Carlevaro - Milonga del Negro Hilario - Dúo de Guitarras
Abel Carlevaro - Campamento - Dúo de Guitarras
Abel Carlevaro - Milonga de Bachicha - Trío de Guitarras
Abel Carlevaro - Dos de a caballo - Dúo de Guitarras
```

#### Uruguay Gen 3, first revision — The Mountain (1972–1988) · superseded 21 September 2026

Total: **20:08**. Uruguayan musician Hugo Fattoruso provides the accordion opening, then joins Japanese percussionist Tomohiro Yahiro as Dos Orientales. The sparse duo format preserves space for reading and reflects the chapter's central truth: survival depended on people moving and working together. These are later musical reflections, not period recordings from 1972–1988.

| Order | Track | Performing artist | Duration | Spotify source |
|---|---|---|---|---|
| 1 | La Reunión | Hugo Fattoruso | 2:50 | [Recorriendo Uruguay](https://open.spotify.com/album/1Wqdt8ROzmMc3eD7ssJVhO) |
| 2 | Recorriendo | Hugo Fattoruso | 1:39 | [Recorriendo Uruguay](https://open.spotify.com/album/1Wqdt8ROzmMc3eD7ssJVhO) |
| 3 | Ten More Miles | Hugo Fattoruso, Tomohiro Yahiro, Dos Orientales | 7:37 | [Dos Orientales](https://open.spotify.com/album/2UpGPrXaPQBHLAUpFrXDbo) |
| 4 | Dos Orillas | Hugo Fattoruso, Tomohiro Yahiro, Dos Orientales | 8:02 | [Dos Orientales](https://open.spotify.com/album/2UpGPrXaPQBHLAUpFrXDbo) |

Why each track:

- La Reunión — begins with the group rather than the disaster: teammates, relatives and friends gathered for an ordinary rugby journey.
- Recorriendo — a short transition into movement and uncertainty, representing the flight and the chapter's sudden passage away from home.
- Ten More Miles — the longest inward journey in the sequence, chosen for Parrado and Canessa's ten-day trek and the endurance required to keep walking without knowing the distance.
- Dos Orillas — two musicians sustaining one piece mirrors mutual dependence. Its title suggests separated places and the passage between Uruguay and Chile, while its spacious ending allows the rescue and return to land quietly.

The titles align unusually closely with the narrative, but the selection is based on the music's restrained accordion, keyboard and percussion textures as well as those associations. Dos Orientales unites an “Oriental” from the República Oriental del Uruguay with an “Oriental” from Japan; the cross-cultural partnership keeps Uruguay at the centre while reflecting a story that crossed borders. All four compositions are new to the master list. Spotify titles, credits and durations checked; account playback not tested.

Spotlistr input:

```text
Hugo Fattoruso - La Reunión
Hugo Fattoruso - Recorriendo
Hugo Fattoruso, Tomohiro Yahiro, Dos Orientales - Ten More Miles
Hugo Fattoruso, Tomohiro Yahiro, Dos Orientales - Dos Orillas
```

#### Uruguay Gen 4, first revision — Getting on the Map (1989–2003) · superseded 21 September 2026

Total: **20:11**. Solo piano by Montevideo-born Uruguayan composer Gustavo Casenave. The music is modern and outward-looking, fitting a generation in which Uruguay enters the international system, reaches two World Cups and discovers the scale of professional rugby. This 2019 album is a later musical portrait of the era. Casenave's official site identifies Balance as a piano-solo instrumental album, and Uruguay's country-brand agency describes his work in tango as part of the country's musical identity.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | Balance | Gustavo Casenave | 8:29 | [Album](https://open.spotify.com/album/3cFPzd2VeXVTEuCjeR9hAL) |
| 2 | Visible | Gustavo Casenave | 2:50 | [Album](https://open.spotify.com/album/3cFPzd2VeXVTEuCjeR9hAL) |
| 3 | Noble | Gustavo Casenave | 5:15 | [Album](https://open.spotify.com/album/3cFPzd2VeXVTEuCjeR9hAL) |
| 4 | Universal | Gustavo Casenave | 3:37 | [Album](https://open.spotify.com/album/3cFPzd2VeXVTEuCjeR9hAL) |

Why each track:

- Balance — a long, searching opening for Uruguay trying to balance an amateur domestic game against a sport turning professional around it.
- Visible — short and brighter, marking the 1999 qualification, the win over Spain and the moment Los Teros became known for their rugby rather than only the Andes story.
- Noble — dignified rather than triumphant, for Ormaechea's long service, the 2003 win over Georgia and the resolve shown even in heavy defeats.
- Universal — opens the sound outward for Uruguay's arrival on the world stage, while its brevity leaves the unresolved professional gap hanging at the generation's end.

The close match between several titles and the narrative is useful, but the selection also rests on the album's solo-piano restraint and its blend of jazz, tango and contemporary writing. All four compositions are new to the master list. Spotify titles and durations checked; account playback not tested.

Sources: [Casenave — Balance piano solo](https://www.casenave.com/piano-solo), [Uruguay XXI profile](https://www.uruguayxxi.gub.uy/es/marca-pais/embajador/gustavo-casenave/).

Spotlistr input:

```text
Gustavo Casenave - Balance
Gustavo Casenave - Visible
Gustavo Casenave - Noble
Gustavo Casenave - Universal
```

#### Uruguay Gen 0, first pass — The British Enclave (1842–1900) · superseded

Total: **20:05**, in the order below. All instrumental.

Quiet nineteenth-century piano and guitar for a chapter about a port city, homesickness, commercial life and the separation of two sporting institutions. The European repertoire evokes the enclave's world; it is not offered as a survey of Uruguayan music. The sequence follows the broad mood, not individual passages timed to the reader.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | Mendelssohn: Venetian Gondola Song, Op. 19b No. 6 | Jamina Gerl | 2:02 | [Track](https://open.spotify.com/track/1vy8IFWlmLcvn3LRg6IAbn) |
| 2 | Chopin: Nocturne No. 2 in E-flat major, Op. 9 No. 2 | Idil Biret | 4:31 | [Track](https://open.spotify.com/track/60xSkGGtWECQZX3OEEa0xC) |
| 3 | Aguado: Andante | Norbert Kraft | 3:46 | [Album, track 12](https://open.spotify.com/album/7nZZx2AnjWe740rLUWm9uJ) |
| 4 | Tárrega: Capricho Árabe: Capricho arabe | Ana Vidović | 4:13 | [Track](https://open.spotify.com/track/3rxIrxZYW9Dl7Td4TofOjU) |
| 5 | Tárrega: Recuerdos de la Alhambra | Norbert Kraft | 4:14 | [Track](https://open.spotify.com/track/5sWJabG0oYxkHVrKOtOCBN) |
| 6 | Tárrega: No. 1, Adelita | Norbert Kraft | 1:19 | [Album, track 22](https://open.spotify.com/album/7nZZx2AnjWe740rLUWm9uJ) |

Why each track:

- Mendelssohn, Venetian Gondola Song — a gentle opening movement for Montevideo's port, carrying the sense of water, distance and British expatriate life without becoming melancholy.
- Chopin, Nocturne No. 2 — intimate, nocturnal piano for the inward-looking enclave and the social world that kept its sporting institutions apart.
- Aguado, Andante — a restrained Spanish guitar colour that begins to shift the sound away from Europe and towards the wider River Plate.
- Tárrega, Capricho Árabe — warmer and more ornamented guitar writing for the city's mixed commercial life and the older world carried inside it.
- Tárrega, Recuerdos de la Alhambra — sustained tremolo gives the generation its longest, most wistful breath: memory, distance and an institution surviving by looking backwards.
- Tárrega, Adelita — a brief, lucid coda for the fork at the end of the generation, where football joins the national life and rugby remains behind the gate.

Durations above follow the linked Spotify listings. Listings checked on 21 September 2026; playback in the user's account was not tested.

Recording and duration sources:

- [Mendelssohn — Naxos track listing](https://www.naxos.com/CatalogueDetail/?id=8.571040)
- [Chopin — Naxos track listing](https://www.naxos.com/CatalogueDetail/?id=8.571023) (use the track-level Biret credit; the page's top-level artist metadata is inconsistent).
- [19th Century Guitar Favourites — Naxos track listing](https://www.naxos.com/CatalogueDetail/?id=8.553007)
- [Ana Vidović — Naxos track listing](https://www.naxos.com/CatalogueDetail/?id=8.554563)

#### Uruguay Gen 1, first pass — The Enclave Organizes (1900–1951) · superseded

Total: **19:22**, in the order below.

Reflective piano for the long institutional quiet, then Latin American guitar and a River Plate tango as the national game begins to organise. This is a mood-based accompaniment using modern releases; it does not reconstruct a historical concert or imply every work originated in Uruguay.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | Debussy: Rêverie | Pascal Rogé | 4:22 | [Track](https://open.spotify.com/track/1qCnKMys9XTB0MyrfBLeKh) |
| 2 | Debussy: La fille aux cheveux de lin | Pascal Rogé | 2:24 | [Album, track 8](https://open.spotify.com/album/5IvEIuvOWm9NsSDsmKvj0d) |
| 3 | Barrios: Julia Florida (Barcarola) | John C. Williams | 4:29 | [Track](https://open.spotify.com/track/1aXVgy4ScPOCAqQ3VKAxcl) |
| 4 | Barrios: Chôro da saudade | David Russell | 4:54 | [Album, track 8](https://open.spotify.com/album/2wag2RMIehuYKxjbg2VWI7) |
| 5 | La Cumparsita | Francisco Canaro | 3:13 | [Track](https://open.spotify.com/track/3NrRHeVsfcZeFKVObKKfwy) |

Why each track:

- Debussy, Rêverie — a soft, suspended beginning for the long quiet in which the enclave exists without yet becoming a national institution.
- Debussy, La fille aux cheveux de lin — lighter and more transparent, suggesting the first small signs of organisation without forcing a triumph too early.
- Barrios, Julia Florida — the guitar brings the sound closer to South America and gives the emerging game a more local warmth.
- Barrios, Chôro da saudade — its gentle rhythmic undercurrent suits a community building patiently through schools, clubs and repeated fixtures.
- La Cumparsita — the decisive River Plate arrival: public, urban and rhythmically confident, marking the moment the institution finally enters its national setting.

Spotify listings and displayed durations checked on 21 September 2026. Account playback was not tested. All five compositions differ from Generation 0; reserve them against future reuse.

#### Uruguay Gen 2, first pass — The Irish Brothers (1955–1971) · superseded

Total: **20:48**. Instrumental Irish whistle and guitar: Irish melodies for the Brothers' arrival and school community, ending with a South American guitar arrangement. These are modern recordings chosen for the chapter's cultural connections and mood, not recordings from 1955–1971.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | The South Wind | Joanie Madden | 4:57 | [Album, track 11](https://open.spotify.com/album/7a1dHDKISc2zmM8Pk3Jjeb) |
| 2 | Down By the Salley Gardens | Joanie Madden | 3:49 | [Album, track 2](https://open.spotify.com/album/7a1dHDKISc2zmM8Pk3Jjeb) |
| 3 | Women of Ireland | Joanie Madden | 4:19 | [Album, track 6](https://open.spotify.com/album/7a1dHDKISc2zmM8Pk3Jjeb) |
| 4 | Lord Mayo | Joanie Madden | 3:23 | [Album, track 12](https://open.spotify.com/album/7a1dHDKISc2zmM8Pk3Jjeb) |
| 5 | Alfosina y el Mar | David Russell | 4:20 | [Album, track 6](https://open.spotify.com/album/2wag2RMIehuYKxjbg2VWI7) |

Why each track:

- The South Wind — a flowing whistle melody for the Christian Brothers arriving by sea and carrying a new communal rhythm into Stella Maris.
- Down By the Salley Gardens — pastoral and reflective, suited to school grounds, memory and the quiet formation of a generation.
- Women of Ireland — gives the Irish inheritance a firmer identity as rugby moves from an imported game towards a community's own possession.
- Lord Mayo — more buoyant and processional, for the Brothers' schools becoming clubs and the shamrock taking root.
- Alfonsina y el mar — a South American lament at the end, bringing the Irish formation back into Uruguay's landscape and the generation's darker final turn.

The final title is spelled “Alfosina y el Mar” in Spotify's listing for this release; the composition is Ariel Ramírez's “Alfonsina y el mar”. Reserve both spellings as the same work. All selections are new to this master list. Spotify listings checked; account playback not tested.

Spotlistr input:

```text
Joanie Madden - The South Wind
Joanie Madden - Down By the Salley Gardens
Joanie Madden - Women of Ireland
Joanie Madden - Lord Mayo
David Russell - Alfosina y el Mar
```

#### Uruguay Gen 3, first pass — The Mountain (1972–1988) · superseded

Total: **20:07**. Instrumental selections from Gustavo Santaolalla's *Ronroco (2024 Remaster)*: restrained plucked strings for the Andes, loss and endurance. This is a modern mood-based accompaniment, not period music or the disaster's film soundtrack. Use the specified remaster: other releases have materially different timings, especially Iguazu.

All tracks and timings verified against [Spotify's album listing](https://open.spotify.com/album/7F6NXrhiawGgkkRrItLOxB). No composition repeats from Generations 0–2. Account playback was not tested.

| Order | Track | Performing artist | Duration |
|---|---|---|---|
| 1 | Gaucho - 2024 Remaster | Gustavo Santaolalla | 3:11 |
| 2 | Jardin - 2024 Remaster | Gustavo Santaolalla | 3:02 |
| 3 | Lela - 2024 Remaster | Gustavo Santaolalla | 2:56 |
| 4 | Iguazu - 2024 Remaster | Gustavo Santaolalla | 4:49 |
| 5 | Coyita - 2024 Remaster | Gustavo Santaolalla | 3:19 |
| 6 | De Ushuaia a La Quiaca - 2024 Remaster | Gustavo Santaolalla | 2:50 |

Why each track:

- Gaucho — dry, open plucked strings for the Andes journey and the stark physical world surrounding the Old Christians.
- Jardin — a quieter, more sheltered texture for the human closeness of the survivors and the community that formed around the disaster.
- Lela — fragile and suspended, holding grief and endurance together without turning the generation into a memorial score.
- Iguazu — broader motion and flowing repetition for the passage from catastrophe back into ordinary life and public recognition.
- Coyita — warmer and more rhythmic, suggesting the survivors' return to movement, friendship and the game.
- De Ushuaia a La Quiaca — the widest landscape of the sequence, carrying Uruguay's name out from the mountain and back onto the map.

Spotlistr input:

```text
Gustavo Santaolalla - Gaucho - 2024 Remaster
Gustavo Santaolalla - Jardin - 2024 Remaster
Gustavo Santaolalla - Lela - 2024 Remaster
Gustavo Santaolalla - Iguazu - 2024 Remaster
Gustavo Santaolalla - Coyita - 2024 Remaster
Gustavo Santaolalla - De Ushuaia a La Quiaca - 2024 Remaster
```

#### Uruguay Gen 4, first pass — Getting on the Map (1989–2003) · superseded

Approximately **19½ minutes**, depending on the matched releases. Instrumental piano and chamber music, with a stronger pulse for qualification and the first World Cups, settling into reflection for the gap between amateurs and professionals. Mood-based international repertoire, including later performances; not a reconstruction of Uruguayan listening habits.

| Order | Track | Performing artist | Spotify |
|---|---|---|---|
| 1 | Perpetuum Mobile | Penguin Cafe Orchestra | [Track, 4:29](https://open.spotify.com/track/1MIwRUsj23h7cYn6mNiqHw) |
| 2 | The Heart Asks Pleasure First / The Promise - Edit | Michael Nyman | [Track, 3:11](https://open.spotify.com/track/1QkIPICRTOdc5NhEocZe9k) |
| 3 | Comptine d'un autre été, l'après-midi | Yann Tiersen | [Track](https://open.spotify.com/track/14rZjW3RioG7WesZhYESso) |
| 4 | Energy Flow | Yoshihiro Kondo | [Track, 3:52](https://open.spotify.com/track/6ZJyioxZJcv0nawnCip3Qn) |
| 5 | Le onde | Johannes Bornlöf | [Track, 5:30](https://open.spotify.com/track/1CnQ4lV6GtvoOF3ehcvzLy) |

Why each track:

- Perpetuum Mobile — its light, repeating motion suits a small nation beginning to move through qualifying campaigns and international fixtures.
- The Heart Asks Pleasure First / The Promise — the two-part arc moves from urgency into reassurance, matching the first fragile sense that Uruguay might belong on the wider map.
- Comptine d'un autre été, l'après-midi — intimate and understated for the years of effort that happen away from the stadium lights.
- Energy Flow — a measured electronic pulse for systems, planning and the professional structures beginning to replace improvisation.
- Le onde — spacious and reflective, leaving the generation with the feeling of a country still building towards a future it cannot yet quite see.

All compositions are new to this list. Reserve both The Heart Asks Pleasure First and The Promise, including standalone versions. Energy Flow is composed by Ryuichi Sakamoto; Le onde by Ludovico Einaudi. Performing artists above identify the selected recordings. Spotify listings checked; account playback not tested.

Spotlistr input:

```text
Penguin Cafe Orchestra - Perpetuum Mobile
Michael Nyman - The Heart Asks Pleasure First / The Promise - Edit
Yann Tiersen - Comptine d'un autre été, l'après-midi
Yoshihiro Kondo - Energy Flow
Johannes Bornlöf - Le onde
```

#### Uruguay Gen 5, first pass — The Plan (2007–2019) · superseded

Total: **20:11** for the linked recordings. Instrumental piano, strings and gentle electronics: quiet rebuilding, growing momentum, then a hopeful finish for the 2019 Fiji victory. Mood-based international selections. All five compositions are new to the master list.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | We Move Lightly | Dustin O'Halloran | 3:10 | [Track](https://open.spotify.com/track/6ja7nWdka0hns78E29qUXV) |
| 2 | Near Light | Ólafur Arnalds | 3:28 | [Track](https://open.spotify.com/track/5ykXsKJqx0GE0dsogxjylG) |
| 3 | Happiness Does Not Wait | Ólafur Arnalds | 4:11 | [Track](https://open.spotify.com/track/65FDlW5ADEo7EpKaC8N31I) |
| 4 | Divenire | Ludovico Einaudi | 6:44 | [Track](https://open.spotify.com/track/4O0Yww5OIWyfBvWn6xN3CM) |
| 5 | Arrival of the Birds | The Cinematic Orchestra, London Metropolitan Orchestra | 2:38 | [Track](https://open.spotify.com/track/1xRCmlU2GyzGem2vw4glxK) |

Why each track:

- We Move Lightly — a modest first step for rebuilding institutions after years of absence and disappointment.
- Near Light — suspended strings and piano reflect the uncertainty of a plan that is not yet fully visible.
- Happiness Does Not Wait — introduces forward motion and guarded optimism as the national system begins to produce results.
- Divenire — the central expansion of the sequence, for professional structures, confidence and the 2019 Fiji victory.
- Arrival of the Birds — a brief, luminous release for the generation's closing sense that Uruguay has finally re-entered the international conversation.

Spotify listings and durations checked. Account playback not tested; alternate releases can differ by a few seconds. Choose the original We Move Lightly, not the Pataphysical Remix, and Arnalds' own Near Light performance, not the Blockbuster Orchestra cover.

Spotlistr input:

```text
Dustin O'Halloran - We Move Lightly
Ólafur Arnalds - Near Light
Ólafur Arnalds - Happiness Does Not Wait
Ludovico Einaudi - Divenire
The Cinematic Orchestra - Arrival of the Birds
```

#### Uruguay Gen 6, first pass — The Branches Rejoin (2020–2026) · superseded

Total: **20:16** using the album version of re:member (6:04). Instrumental piano, strings and restrained electronics: a contemporary sound for professional rugby taking root at home, with a quiet ending to the Uruguay chapter. Selected for mood, not as a survey of Uruguayan musicians. All five compositions are new to the master list.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | Letter to Glass | Hania Rani | 3:32 | [Home, track 4](https://open.spotify.com/album/0lCjdc69ig4VmMzExMcCmA) |
| 2 | Ab Ovo | Joep Beving | 4:48 | [Track](https://open.spotify.com/track/1G0gPuaIFKB8Ua6mFUh2pu) |
| 3 | Losar | Joep Beving | 3:41 | [Track](https://open.spotify.com/track/0bCSGdS5SRvzoz4IBTD55W) |
| 4 | re:member | Ólafur Arnalds | 6:04 | [re:member, track 1](https://open.spotify.com/album/6JpQGIi2he6iskzR4aLwPG) |
| 5 | saman | Ólafur Arnalds | 2:11 | [re:member, track 3](https://open.spotify.com/album/6JpQGIi2he6iskzR4aLwPG) |

Why each track:

- Letter to Glass — clear, delicate piano for the professional game taking root at home without losing its small-country vulnerability.
- Ab Ovo — patient repetition and gradual development suit the branches of Uruguayan rugby beginning to reconnect.
- Losar — slightly more expansive and grounded, for Peñarol Rugby, the regional competitions and a domestic structure with real weight.
- re:member — the generation's fullest statement: layered but restrained, representing the old enclave and the new professional pathway meeting again.
- saman — a quiet closing piece for the dated present-day snapshot and the sense that the story is continuing rather than concluding.

Spotify listings and durations checked. Account playback not tested. The single version of re:member has a different duration.

Spotlistr input:

```text
Hania Rani - Letter to Glass
Joep Beving - Ab Ovo
Joep Beving - Losar
Ólafur Arnalds - re:member
Ólafur Arnalds - saman
```

#### Argentina Gen 0, concert-music set — The British Enclave (1873–1964) · superseded 22 September 2026

Total: **21:50**. Period concert piano from Buenos Aires, played by Mirian Conti (*Panorama Argentino*, 2014). This is the conservatory culture of the same Europe-facing elite that founded the clubs. Julián Aguirre's first book of *Aires nacionales argentinos*, Op. 17, dates from 1898, the year before the River Plate Rugby Union was founded. Carlos Guastavino's Sonatina in G minor dates from the mid-1940s (sources give 1945 or 1946), when the Campeonato Argentino began pushing the game into the provinces. Three of Aguirre's five *tristes* carry the names of interior provinces, Jujuy and Córdoba. This follows the Chile Generation 0 model. It replaces the Troilo–Grela tangos, because tango was the music of the popular city the enclave stood apart from. The tristes profile as calm as any solo piano in the list (flux 0.44–0.50).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Aires nacionales, Vol. 1: Triste No. 1, "Jujuy" | Julián Aguirre | Mirian Conti | 2:54 | [Track](https://open.spotify.com/track/4eAgBarT0D6qEcU1svRriV) |
| 2 | Aires nacionales, Vol. 1: Triste No. 2 | Julián Aguirre | Mirian Conti | 2:58 | [Track](https://open.spotify.com/track/6wTpsLnQ09zTdc7eRBU1ju) |
| 3 | Aires nacionales, Vol. 1: Triste No. 3 | Julián Aguirre | Mirian Conti | 3:39 | [Track](https://open.spotify.com/track/4UknM0gWZytRfTNfVrnlsA) |
| 4 | Aires nacionales, Vol. 1: Triste No. 4, "Cordoba" | Julián Aguirre | Mirian Conti | 3:03 | [Track](https://open.spotify.com/track/54Lkbtwzl8XICHyt5MIdmG) |
| 5 | Aires nacionales, Vol. 1: Triste No. 5, "Cordoba" | Julián Aguirre | Mirian Conti | 2:48 | [Track](https://open.spotify.com/track/2Mnfeg6WDiuEuT2gywnnBl) |
| 6 | Piano Sonatina in G Minor: II. Lento muy espressivo | Carlos Guastavino | Mirian Conti | 3:52 | [Track](https://open.spotify.com/track/0cFIqkc2QMQAZPIrs9d4sY) |
| 7 | Piano Sonatina in G Minor: III. Presto | Carlos Guastavino | Mirian Conti | 2:36 | [Track](https://open.spotify.com/track/51v3pXpf6qg1DV1ORCVCZq) |

Why each track:

- Triste No. 1 — a calm, measured opening: the Buenos Aires Football Club arguing for seven years over which rules to play.
- Triste No. 2 — inward and slow: a game kept inside the Anglo community, where natives were admitted rarely and as exceptions.
- Triste No. 3 — the longest and most developed of the five: the institution-building, from the 1899 union to the clubs that quit football when it turned professional.
- Triste No. 4 — steady and unhurried: ninety-one years without beating a touring side.
- Triste No. 5 — the quietest close to the book: the settled sense of inferiority.
- Sonatina, II — broader, warmer romantic writing: the Campeonato Argentino and the Catholic orders carrying the game beyond the capital.
- Sonatina, III — the only fast piece, and short: the turn of 1964, when South Africa sent belief and a method.

Spotify album: [Panorama Argentino](https://open.spotify.com/album/7m1fNeeh7erEHH2YpodOvL). Sources: [Aguirre piano catalogue (pianolatinoamerica.org)](http://pianolatinoamerica.org/e_aguirre/e_aguirrearti.html), [A Sonatina em Sol Menor de Carlos Guastavino (1945)](https://www.academia.edu/116014600/A_Sonatina_em_Sol_Menor_de_Carlos_Guastavino_1945).

Spotlistr input:

```text
Mirian Conti - Aires nacionales, Vol. 1: Triste No. 1, "Jujuy"
Mirian Conti - Aires nacionales, Vol. 1: Triste No. 2
Mirian Conti - Aires nacionales, Vol. 1: Triste No. 3
Mirian Conti - Aires nacionales, Vol. 1: Triste No. 4, "Cordoba"
Mirian Conti - Aires nacionales, Vol. 1: Triste No. 5, "Cordoba"
Mirian Conti - Piano Sonatina in G Minor: II. Lento muy espressivo
Mirian Conti - Piano Sonatina in G Minor: III. Presto
```

#### Argentina Gen 3, chamber set — The Self-Inflicted Wound (1987–1999) · superseded 22 September 2026

Total: **21:10**. Bandoneón and cello: Dino Saluzzi with the German cellist Anja Lechner, from *Ojos Negros* (ECM 1991, recorded in 2006 at Götzis, Austria, and released in March 2007). Saluzzi was born in Salta, and his music draws on northwestern Argentine roots. ECM calls the album "chamber music with inspirational roots in Argentinean traditions". All three pieces are Saluzzi's own. This is a later portrait, recorded seven years after the generation ends. Two instruments passing one line between them, an Argentine and a European musician recorded abroad, suits a generation divided between an amateur union at home and players learning professionalism in Europe. The profiles are among the calmest in the chapter (flux 0.28–0.39). ECM records a wide dynamic range, though (12–20 LU in the previews), so set the volume on a loud passage.

Revised 22 September 2026. This set replaces the Dino Saluzzi Group's *Mojotoro* (1991), whose line-up included tenor and soprano saxophone, electric bass and drums: a jazz rhythm section under the page. Saluzzi stays as this generation's composer. "Tango a mi padre", which opens *Ojos Negros*, was used in the *Mojotoro* set and stays reserved.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Duetto | Dino Saluzzi | Dino Saluzzi, Anja Lechner | 6:01 | [Track](https://open.spotify.com/track/4zGiztLWGfFtqgN2geT9Mf) |
| 2 | Carretas | Dino Saluzzi | Dino Saluzzi, Anja Lechner | 6:26 | [Track](https://open.spotify.com/track/0C5Jfb2rUBJUxYyrSw8Vze) |
| 3 | Serenata | Dino Saluzzi | Dino Saluzzi, Anja Lechner | 8:43 | [Track](https://open.spotify.com/track/70ttf96SxQTFsy30FtMp6B) |

Why each track:

- Duetto — two voices trading one line: the end of Porta's era, and a structure that had leaned so heavily on one player.
- Carretas — the quietest track on the album (flux 0.28), slow and low: a rigid amateur union at home while the players' careers moved to Europe.
- Serenata — the longest, warm and unresolved: Wyllie's new habits, the 1999 World Cup and the breakthrough against Ireland at Lens. The professional structure still exists only elsewhere.

Spotify album: [Ojos Negros](https://open.spotify.com/album/5DKWH8gggqW8fJr9ZlQ9JG). Sources: [ECM — Ojos Negros (recording, release, line-up)](https://ecmrecords.com/product/ojos-negros-dino-saluzzi-anja-lechner/), [ECM — Mojotoro (line-up of the replaced set)](https://ecmrecords.com/product/mojotoro-dino-saluzzi-group/), [National University of San Martín biography](https://www2.unsam.edu.ar/dinosaluzzi/dino.asp).

Spotlistr input:

```text
Dino Saluzzi, Anja Lechner - Duetto
Dino Saluzzi, Anja Lechner - Carretas
Dino Saluzzi, Anja Lechner - Serenata
```

#### Argentina Gen 6, concert-music set — The Diaspora (2020–2026) · superseded 22 September 2026

Total: **19:11**. String quartets by Osvaldo Golijov, the Argentine composer of the diaspora. Born in La Plata in 1960, he grew up surrounded by "classical chamber music, Jewish liturgical and klezmer music, and the new tango of Astor Piazzolla", and studied composition with Gerardo Gandini. He moved to Israel in 1983 and to the United States in 1986. *Yiddishbbuk* (1992) is a set of commemorations, and its last movement carries the initials of Leonard Bernstein. *Tenebrae* (2002), heard here in its version for string quartet, loops melismas from Couperin's *Leçons de ténèbres* into a slow, shimmering texture. Golijov wrote that heard "from afar" it offers a "beautiful" surface, with pain beneath it when heard close. Both works are older than this generation, in recordings from 2011 and 2018, and were chosen for a country whose national team is built almost entirely abroad. Profiles are calm (flux 0.38–0.54). The Calidore recording of *Tenebrae* is very quiet (about −26 LUFS in the preview), so raise the volume when it starts.

Revised 22 September 2026. This set replaces the Diego Schissi Quinteto's *Te* (2021), contemporary tango whose writing draws on jazz and whose surges were among the busiest music left in the chapter.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Yiddishbbuk: L.B. | Osvaldo Golijov | Cuarteto Latinoamericano | 4:40 | [Track](https://open.spotify.com/track/51vzC3F1uYjsCFMoi7t43q) |
| 2 | Tenebrae | Osvaldo Golijov | Calidore String Quartet | 14:31 | [Track](https://open.spotify.com/track/5rJGaL1lM5NKORCpKIiOnp) |

Why each track:

- Yiddishbbuk: L.B. — slow and spare: the paradox of a team with no franchise and no domestic league, 31 of Cheika's 33 players abroad.
- Tenebrae — fourteen minutes of one slow, luminous surface: Cheika carrying a dispersed squad to another World Cup semi-final; Contepomi's wins in Wellington, the Triple Crown and the British & Irish Lions beaten in Dublin; the cool mood at home in mid-2026; Vélez in August 2025 and the road to 2027. It is calm from afar, with the strain underneath, as its composer intended.

Spotify albums: [Encores (Cuarteto Latinoamericano)](https://open.spotify.com/album/5Kkz3k5DKB9E6QPY6lSkYO), [Resilience (Calidore String Quartet)](https://open.spotify.com/album/0LVMDlL3lPy2YUz7XmXbxj). Kronos Quartet's premiere recording of *Tenebrae* is also on Spotify, split into two tracks, but the copy that also carries *Last Round* plays in only 54 markets. Sources: [Boosey & Hawkes — Golijov biography](https://www.boosey.com/composer/Osvaldo+Golijov?ttype=BIOGRAPHY), [Boosey & Hawkes — Tenebrae](https://www.boosey.com/cr/music/Osvaldo-Golijov-Tenebrae/55630), [Boosey & Hawkes — Yiddishbbuk](https://www.boosey.com/cr/music/Osvaldo-Golijov-Yiddishbbuk/55638).

Spotlistr input:

```text
Cuarteto Latinoamericano - Yiddishbbuk: L.B.
Calidore String Quartet - Tenebrae
```

#### Argentina Gen 3 — The Self-Inflicted Wound (1987–1999) · superseded 22 September 2026

Total: **20:09**. Unchanged. Instrumental music from the 1992 album *Mojotoro* by the Dino Saluzzi Group. Saluzzi was born in Salta, and his music draws on northwestern Argentine roots while crossing tango, folk music, improvisation and chamber jazz. That combination fits a generation divided between a rigid amateur system at home and players learning professionalism abroad. The recording itself belongs to the generation's dates. It profiles calm (flux 0.34–0.89).

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Tango A Mi Padre: Nocturno - Elegia | Dino Saluzzi | Dino Saluzzi Group | 2:45 | [Track](https://open.spotify.com/track/4QuVL60iYaXeMxqBPkmx75) |
| 2 | Mundos: Exposición - Desarollo - Cadensia - Imitación - Marcha - Recapitulación | Dino Saluzzi | Dino Saluzzi Group | 11:00 | [Track](https://open.spotify.com/track/4J9YhqQTm08fMsUqXzyThR) |
| 3 | Lustrin | Dino Saluzzi | Dino Saluzzi Group | 6:24 | [Track](https://open.spotify.com/track/1he5KkOo4iZTYo8gr56tiW) |

Why each track:

- Tango A Mi Padre — a restrained elegy for the end of Porta's era and the loss of a structure that had depended so heavily on one player.
- Mundos — its sections pass through exposition, development, imitation, march and return. That fractured but connected design suits players scattered between Argentina and professional clubs overseas, learning in different rugby worlds while remaining part of one national story.
- Lustrin — more mobile and assertive, for Wyllie's new habits, the 1999 World Cup and the breakthrough against Ireland at Lens. It ends with momentum rather than resolution because the professional structure still exists elsewhere.

Spotify album: [Mojotoro](https://open.spotify.com/album/6ehB5k0AF4qvvaspSdd4hc). Sources: [National University of San Martín biography](https://www2.unsam.edu.ar/dinosaluzzi/dino.asp), [ECM artist profile](https://ecmrecords.com/artists/dino-saluzzi/).

Spotlistr input:

```text
Dino Saluzzi Group - Tango A Mi Padre: Nocturno - Elegia
Dino Saluzzi Group - Mundos: Exposición - Desarollo - Cadensia - Imitación - Marcha - Recapitulación
Dino Saluzzi Group - Lustrin
```

#### Argentina Gen 4 — The Team That Didn't Exist (2000–2011) · superseded 22 September 2026

Total: **20:16**. Instrumental chamamé led by accordionist Chango Spasiuk, born in Apóstoles, Misiones. The 2009 album falls inside this generation and brings northeastern Argentina into the soundtrack. The album's title, *Pynandí – Los Descalzos*, means "the barefoot ones", which suits a world-class team from a country with no professional rugby of its own. Chamamé's interlocking European and Guaraní inheritance suits a team assembled from players living in several countries but carrying one Argentine identity. UNESCO recognises chamamé as part of Argentina's intangible cultural heritage. Revised in September 2026: "Suite Nordeste, Pt. 3 & 4" is dropped. It was the busiest track on the album (flux 1.50), and the slower "Tristeza" (0.43) replaces it.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | El Camino | Chango Spasiuk | Chango Spasiuk | 5:18 | [Track](https://open.spotify.com/track/2UR4zblTaKZEi8c67Y30Yc) |
| 2 | Suite Nordeste, Pt. 1 & 2 | Chango Spasiuk | Chango Spasiuk | 4:20 | [Track](https://open.spotify.com/track/5Tb7qh5MBN1jy1e74VCQ5N) |
| 3 | Tristeza | Chango Spasiuk | Chango Spasiuk | 4:27 | [Track](https://open.spotify.com/track/6jAL6cak4Mu8azAkb7SK44) |
| 4 | Panambí (Mariposa) | Chango Spasiuk | Chango Spasiuk | 3:34 | [Track](https://open.spotify.com/track/3DXu5zNLz4iNLTlH5dBV0k) |
| 5 | Mejillas Coloradas | Chango Spasiuk | Chango Spasiuk | 2:37 | [Track](https://open.spotify.com/track/1Rdot7wkVWczg1pbb1tjLw) |

Why each track:

- El Camino — a spacious opening for the road Argentina's best players took into France, England and Ireland, where the national team was effectively professionalised in exile.
- Suite Nordeste, Pt. 1 & 2 — separate movements beginning to form one larger work: Loffreda gathering players shaped by different foreign clubs into a coherent side.
- Tristeza — slow and dark, one of the calmest tracks on the album: 2003–2006, good enough to beat almost anyone and given no competition to do it in, from the 16–15 against Ireland to a handful of Tests a year.
- Panambí (Mariposa) — *panambí* is Guaraní for butterfly. The lighter transformation fits Argentina emerging from outsider status into a World Cup semi-finalist.
- Mejillas Coloradas — warm, quick and celebratory for the second victory over France, Contepomi's bow and third place in the world, while keeping the intimacy of regional folk music rather than turning into stadium bombast.

Spotify album: [Pynandí - Los Descalzos](https://open.spotify.com/album/2L9gLuWayqTZHUZGXXlQFH). National context: [UNESCO — El chamamé](https://ich.unesco.org/es/RL/el-chamame-01600).

Spotlistr input:

```text
Chango Spasiuk - El Camino
Chango Spasiuk - Suite Nordeste, Pt. 1 & 2
Chango Spasiuk - Tristeza
Chango Spasiuk - Panambí (Mariposa)
Chango Spasiuk - Mejillas Coloradas
```

#### Argentina Gen 6 — The Diaspora (2020–2026) · superseded 22 September 2026

Total: **19:17**. Contemporary instrumental tango by Diego Schissi Quinteto, released in 2021 inside this generation's dates. Piano, bandoneón, violin, guitar and double bass behave as distinct voices inside one ensemble, an apt sound for a national team assembled from players scattered across foreign clubs. Schissi's writing keeps the heat of Argentine popular music while drawing on jazz and chamber music. Revised in September 2026: the tracks were re-chosen by sound. "Árbol" and "Riel", the two busiest tracks on the album (flux 1.24–1.37), were opening the set, and they are dropped along with "Mirador". "Hijo" and "Hoja" replace them.

| # | Track | Composer | Performer | Duration | Spotify |
|---|---|---|---|---|---|
| 1 | Hijo | Diego Schissi | Diego Schissi Quinteto | 4:29 | [Track](https://open.spotify.com/track/6Oe12Boaa2GheIfuWgEjvB) |
| 2 | Aproximación | Diego Schissi | Diego Schissi Quinteto | 3:54 | [Track](https://open.spotify.com/track/4oE8f0ClKAozQ1xKkJIrK2) |
| 3 | Salto | Diego Schissi | Diego Schissi Quinteto | 5:36 | [Track](https://open.spotify.com/track/6kt0KqD6wMyumitWNdqdB6) |
| 4 | Hoja | Diego Schissi | Diego Schissi Quinteto | 3:14 | [Track](https://open.spotify.com/track/7hqOIoUHC1lAGOmVWBdHPQ) |
| 5 | Luz | Diego Schissi | Diego Schissi Quinteto | 2:04 | [Track](https://open.spotify.com/track/5v0cav937KqEIzEuiAK7S1) |

Why each track:

- Hijo — the calmest track on the album (flux 0.34): the paradox of a team with no franchise and no domestic league, 31 of Cheika's 33 players abroad.
- Aproximación — patient, exploratory movement for Cheika rebuilding from a dispersed squad and carrying Argentina to another World Cup semi-final.
- Salto — the set's one surge: Contepomi's wins in 2024–25 in Wellington, the Triple Crown, and the British & Irish Lions beaten in Dublin.
- Hoja — quieter again: the mixed balance sheet of mid-2026 and the cool mood at home.
- Luz — a short, clear close: Vélez, August 2025, and the road to 2027.

Spotify album: [Te](https://open.spotify.com/album/4lbHMi22NGhpCIKAZrrV5V). Sources: [Fundación Konex profile](https://www.fundacionkonex.org/b4737-diego_schissi_quinteto), [Diego Schissi's description of his contemporary tango approach](https://diegoschissi.bandcamp.com/album/tongos).

Spotlistr input:

```text
Diego Schissi Quinteto - Hijo
Diego Schissi Quinteto - Aproximación
Diego Schissi Quinteto - Salto
Diego Schissi Quinteto - Hoja
Diego Schissi Quinteto - Luz
```

#### Argentina Gen 0 — The British Enclave (1873–1964) · superseded 21 September 2026

Total: **20:06**. Instrumental tango with bandoneon and guitar, for the Buenos Aires setting and the later decades of this generation. All seven compositions are new to the master list.

Use the recordings on [Esto Es Tango! Troilo y Grela](https://open.spotify.com/album/41GdyVd6LGWbbnDKPItWdn), performed by Aníbal Troilo and Roberto Grela. Spotify listings and durations checked; account playback not tested. Other releases have different durations.

| Order | Track | Duration |
|---|---|---|
| 1 | Palomita Blanca | 2:51 |
| 2 | Mi Refugio | 2:42 |
| 3 | A Pedro Maffia | 2:49 |
| 4 | Nunca Tuvo Novio | 3:38 |
| 5 | Un Placer | 2:44 |
| 6 | Sobre el Pucho | 2:05 |
| 7 | La Cachila | 3:17 |

Why each track:

- Palomita Blanca — an elegant, measured tango for the British commercial world of early Buenos Aires and the first enclosed clubs.
- Mi Refugio — intimate and inward, for a sport still living inside a narrow expatriate social world.
- A Pedro Maffia — a more purposeful tribute, giving the generation a sense of individual craft and emerging local identity.
- Nunca Tuvo Novio — its wistful character suits the long delay before Argentina can turn participation into international authority.
- Un Placer — warmer and more conversational, for rugby spreading through relationships, schools and clubs.
- Sobre el Pucho — darker and more tense, reflecting the pressures and exclusions beneath the apparently orderly amateur game.
- La Cachila — a lively closing turn that leaves the generation ready for Argentina's breakout rather than ending in stasis.

Spotlistr input:

```text
Aníbal Troilo, Roberto Grela - Palomita Blanca
Aníbal Troilo, Roberto Grela - Mi Refugio
Aníbal Troilo, Roberto Grela - A Pedro Maffia
Aníbal Troilo, Roberto Grela - Nunca Tuvo Novio
Aníbal Troilo, Roberto Grela - Un Placer
Aníbal Troilo, Roberto Grela - Sobre el Pucho
Aníbal Troilo, Roberto Grela - La Cachila
```

#### Argentina Gen 2 — The Porta Generation (1971–1987) · superseded 21 September 2026

Total: **about 20 minutes** (19:53 using the 3:34 Oblivion, 6:37 Invierno Porteño, 2:48 Libertango and 6:54 Soledad versions). Instrumental Argentine tango, moving from reflection through tension and confidence to a quiet ending. All four compositions are new to the master list. Spotify listings checked; alternate releases vary in duration; account playback not tested.

| Order | Track | Artist | Spotify |
|---|---|---|---|
| 1 | Oblivion | Astor Piazzolla | [Track](https://open.spotify.com/track/0CShxQaSFFKXY2PxrJIhrB) |
| 2 | Invierno Porteño | Astor Piazzolla | [Track, 6:37](https://open.spotify.com/track/0Q0iMh6Ng08OHsBI5hrDVo) |
| 3 | Libertango | Astor Piazzolla | [Track](https://open.spotify.com/track/3qaD0pGadl1ZGmmsI2dxVU) |
| 4 | Soledad | Astor Piazzolla | [Track, 6:54](https://open.spotify.com/track/7HsdZDeYdbDIHnHrZw5P12) |

Why each track:

- Oblivion — a solemn opening for the generation's political isolation and the loneliness carried by Hugo Porta's brilliance.
- Invierno Porteño — colder, more deliberate and rhythmically unsettled, for the long winter in which Argentina's rugby is cut off from the world.
- Libertango — its famous forward drive gives the sequence its moment of defiance as Argentina begins to insist on its own modernity.
- Soledad — a spacious, unresolved ending for the years of talent, political distance and unrealised possibility before the next generation's self-inflicted wound.

Spotlistr input:

```text
Astor Piazzolla - Oblivion
Astor Piazzolla - Invierno Porteño
Astor Piazzolla - Libertango
Astor Piazzolla - Soledad
```

#### Argentina Gen 5 — The Jaguares (2009–2022) · superseded 21 September 2026

Total: **20:00** exactly. Instrumental tango-jazz by the Buenos Aires sextet Escalandrum, led by drummer Daniel “Pipi” Piazzolla. The album was released in 2011, as Argentina entered the Rugby Championship and began building professional structures at home. Its fusion of inherited tango with modern improvisation mirrors Argentine rugby finally keeping its identity while changing how it worked.

| Order | Track | Performing artist | Duration | Spotify |
|---|---|---|---|---|
| 1 | Buenos Aires Hora Cero | Escalandrum | 5:17 | [Album](https://open.spotify.com/album/7diNDlf9w2zeZKKbKIUlME) |
| 2 | Lunfardo | Escalandrum | 6:26 | [Album](https://open.spotify.com/album/7diNDlf9w2zeZKKbKIUlME) |
| 3 | Tanguedia 1 | Escalandrum | 4:37 | [Album](https://open.spotify.com/album/7diNDlf9w2zeZKKbKIUlME) |
| 4 | Vayamos al Diablo | Escalandrum | 3:40 | [Album](https://open.spotify.com/album/7diNDlf9w2zeZKKbKIUlME) |

Why each track:

- Buenos Aires Hora Cero — “zero hour” marks the reset: Pampas XV, Rugby Championship entry and the beginning of a professional pathway based in Argentina.
- Lunfardo — rooted in Buenos Aires language and identity, it represents the players coming home from European clubs and building a professional team without surrendering their Argentine character.
- Tanguedia 1 — disciplined ensemble passages and improvisation fit the Jaguares learning structure, developing young players and reaching the 2019 Super Rugby final.
- Vayamos al Diablo — fast, daring and slightly unstable for the generation's sharp final turn: the All Blacks beaten in 2020 even as COVID and competition restructuring destroy the Jaguares underneath them.

Escalandrum's connection is direct rather than decorative: the group was formed in Buenos Aires by Astor Piazzolla's grandson and developed a distinctly local fusion of tango and jazz. The same balance of inheritance and reinvention drives this generation's rugby story. All four compositions are new to the master list; other Piazzolla works already reserved were excluded. Spotify titles and durations checked; account playback not tested.

Sources: [Escalandrum official history](https://www.escalandrum.com/), [City of Buenos Aires profile](https://turismo.buenosaires.gob.ar/en/article/escalandrum-%E2%80%93-fusing-sound-buenos-aires).

Spotlistr input:

```text
Escalandrum - Buenos Aires Hora Cero
Escalandrum - Lunfardo
Escalandrum - Tanguedia 1
Escalandrum - Vayamos al Diablo
```
