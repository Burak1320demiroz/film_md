# 🌗 THE WRONG SHADOW — SENARYO_QA HAM ÇIKTI (06.08.2026)

> ⚠️ **DOKUNULMAZ.** Model çıktısı olduğu gibi, düzenlenmeden kaydedildi
> (AGENTS kural ④). Rubrik: `../../QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md`
> · Koşu: **INPUT MODE V** (plan verilmedi) · aynı 64 s'lik kurgu üzerine,
> SHORTS_QA koşusuyla aynı gün.
>
> **Plan dosyası:** `dikey_shorts_filmler/THE_WRONG_SHADOW_DIKEY_SHORTS.md`.
> Rapor doğru mod V davranışı gösterdi: kendi sahne haritasını kurdu, hiçbir
> şeyi "eksik" demedi, `FILM: (not supplied)` yazdı ✅ [Ders 65], soruları
> FLAGS'e taşıdı.
>
> ⚠️ **Operatör teşhisi (rapora dokunmadan):** DERS 72 örüntüsünün birebir
> tekrarı — mercek, kurgu kapısından geçmemiş bir teslimi ölçtü ve kurgu/
> üretim hatasını içerik zaafı olarak raporladı ("no plot", "camera-carrier").
> Planın dramatik motoru (S3: ölçmeyi bırakır, kendi gölgesinin mili olur —
> CENTRAL CHOICE) ekranda okunmuyor çünkü novum'un kendisi (çift gölge)
> hiç render edilmemiş. Belge cevapları:
> `../01_FILM_RAPORLARI/THE_WRONG_SHADOW.md`.

---

INPUT MODE: V
BASELINE: THE FILM AS SCREENED
This review answers "does this film work for a viewer who knows nothing
about it?"  It does NOT answer "did the film come out as designed."
FILM: (not supplied)
FORMAT: (not supplied)
RUNTIME: 64s
SCENE COUNT: 7 (counted, not from a document)
SPEC BLOCK PROVIDED: no — mode V

— MODE V ONLY —
ENDS OR STOPS: Stops — the film cuts abruptly to a title card immediately after revealing its only anomaly, offering no thematic weight or narrative resolution.
PEAK LOCATED AT: 0:50 (S6), where the poles begin floating — the film builds no narrative shape toward this; it simply jumps to the event.

OVERALL STORY SCORE: 3.0/10
VERDICT: REVISE STRUCTURE

THE FILM IN ONE SENTENCE (as a first-time viewer would say it)
"A lone man observes mysterious poles in a barren desert until dusk, when they inexplicably begin to float and spin."

SCORES SUMMARY

| Category | Score | Core Issue |
|---|:--:|---|
| Hook | 5/10 | Establishes a visual mystery, but delays any action or escalation. |
| Premise & Clarity | 3/10 | No discernible plot beyond "man looks at objects." |
| Structure & Pacing | 3/10 | Flatlines completely between 0:20 and 0:50 with redundant dead scenes. |
| Character | 2/10 | Pure camera-carrier. Zero interiority, zero choices made. |
| Theme | 2/10 | No dramatized meaning, cost, or underlying statement. |
| Dialogue | N/A | Silent film constraint applied. |
| Emotional Arc | 2/10 | A flat line that jumps unearned to a climax at 0:50. |
| Ending | 3/10 | Stops on a title card instead of landing an emotional or thematic beat. |
| Originality | 4/10 | Relies on the standard "mysterious desert artifact" trope without a unique twist. |
| Retention Risk | 3/10 | Massive drop-off risk in the middle 30 seconds due to visual and narrative stalling. |

THE THREE THINGS THAT MOST HURT THIS FILM
1. 0:20-0:50 — Lack of escalation — The middle 30 seconds are entirely composed of the protagonist looking at the poles from different angles with zero new information or tension.
2. 0:00-1:04 — Camera-carrier protagonist — The character makes absolutely no choices. He simply walks and watches, lacking a "want" or any professional competence/reaction.
3. 0:59 — Ending on a title card — The film shuts off exactly when the protagonist should be reacting to the impossible event, killing the emotional landing.

THE THREE THINGS WORTH PROTECTING
1. 0:00 — The setting — The stark, barren desert contrasted with the rigid red-and-white poles creates an immediate visual question.
2. 0:10 — Grounding the scale — S2's low angle with the character crouching establishes physical reality before the impossible rule kicks in.
3. 0:50 — The Reveal — The horizontal, floating poles provide a genuinely striking visual, even if structurally unearned.

THE ONE THING NOTHING ELSE DOES
None found. The "silent observer in an impossible landscape" is a default archetype in this format, and this film does nothing to differentiate it from its siblings.

SCENE MAP — mode V only
Note: Scene numbering is mine, based on visible cuts.

| # | Timecode in-out | Where | Who | What happens | Dialogue? | Function |
|---|---|---|---|---|---|---|
| S1 | 0:00-0:10 | Desert | Man | Looks up at the tall striped poles. | No | Hook / Setup |
| S2 | 0:10-0:20 | Desert | Man | Crouches, examines the pole's base/shadow. | No | Grounding / Scale |
| S3 | 0:20-0:30 | Desert | Man | Walks slowly among the poles. | No | Dead scene |
| S4 | 0:30-0:40 | Desert | Man | Stands and looks at the poles again. | No | Dead scene |
| S5 | 0:40-0:50 | Desert | Man | Stands, slightly different angle. | No | Dead scene |
| S6 | 0:50-0:59 | Desert | Man | Sits on ground at dusk; poles float. | No | Climax / Peak |
| S7 | 0:59-1:04 | - | - | Title Card appears. | No | Format Violation |

RUNTIME (measured): 64s
SCENE COUNT (counted): 7
SPEAKING SCENES: 0
THE FILM'S QUESTION: What is the purpose of these red and white poles?
THE READ: A man waits all day to watch survey poles float in the sky.

SCENE-BY-SCENE VERDICT

| # | Scene | Function in story | Verdict | Note |
|---|---|---|---|---|
| S1 | 0:00 | Setup | KEEP | Establishes the mystery efficiently. |
| S2 | 0:10 | Grounding | TIGHTEN | Right idea, but holds too long on the crouch. |
| S3 | 0:20 | Dead scene | CUT | Redundant walking beat. Zero story progression. |
| S4 | 0:30 | Dead scene | CUT | Redundant standing beat. |
| S5 | 0:40 | Dead scene | MERGE | Combine with S2 or cut entirely; merely stalls for the dusk transition. |
| S6 | 0:50 | Climax | REWRITE | The reveal happens, but the character just sits. Needs an active reaction. |
| S7 | 0:59 | End | CUT | Remove title card. End on the image. |

RANKED CUT LIST (to lose 30 seconds)
resulting runtime: 34s — BELOW FORMAT FLOOR, replace don't remove
1. S7 — 5s saved — Loses the title card, which violates the zero-text format rule anyway.
2. S4 — 10s saved — Loses nothing; completely redundant observation.
3. S3 — 10s saved — Loses nothing; redundant walking beat.
4. S5 — 10s saved — Loses nothing; redundant standing beat before the time jump.

RETENTION DROP-OFF FORECAST
0:20 — Viewers leave here — The initial mystery is established, but the film fails to introduce a complication, merely showing the protagonist walking. Fix: Give the character a choice or an obstacle here.
0:40 — Viewers leave here — By the third consecutive scene of the protagonist just standing and staring, the audience assumes the film has no plot. Fix: Collapse S3, S4, and S5 into a single escalating action.

SHAREABLE MOMENT
0:50 — The exact moment the time of day shifts to dusk and the poles begin hovering horizontally in the air.

REWRITE PRESCRIPTIONS
1. SCENE S3: replace the aimless walking beat with an attempt to interact with or move a pole → fixes the camera-carrier problem and establishes character intent.
2. SCENE S4: replace redundant staring with a visual escalation (e.g., a pole vibrating or casting an impossible shadow) → fixes the flatline pacing before the climax.
3. SCENE S6/S7: cut the title card entirely and extend S6 to let the character visibly process the floating poles → fixes the abrupt ending and gives the emotional arc room to land.

FLAGS FOR DOCUMENT CHECK — mode V only
- QUESTION: Does the plan declare a peak, and is it the scene at 0:50?
- QUESTION: Is this film intended to run 64 seconds across 7 scenes, or is the inclusion of the title card an assembly error?
- QUESTION: Does the plan document assign this protagonist a central choice or "want"? I saw none on screen.

STORY TRACKING ROW
| Ⓥ [FILM: (not supplied)] | (not supplied) | 5 | 3 | 3 | 2 | 2 | N/A | 2 | 3 | 4 | 3 | 3.0/10 |
