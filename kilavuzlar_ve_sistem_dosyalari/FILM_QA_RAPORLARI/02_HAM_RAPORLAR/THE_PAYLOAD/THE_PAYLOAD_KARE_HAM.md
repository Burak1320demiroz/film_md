# THE PAYLOAD — ① KARE QA · HAM RAPOR

> Model çıktısı, OLDUĞU GİBİ (kural ④). Düzeltilmez, kısaltılmaz.
> Koşu: 01.09.2026'da sahip tarafından yapıştırıldı · Gemini · rubrik `1_KARE_QA_CRITIQUE_PROMPT.md` · MOD V
> ⛔ Film klasöründe `THE_PAYLOAD_QA_SPEC.md` VARDIR → bu koşu ÖN KOŞU'dur, tekrarlanır [D129].
> ⚠️ Raporun künyesindeki film adı "(not supplied)" · başlık kartından okunan ad: THE LAST CUSTODIAN
> Değerlendirme: `01_FILM_RAPORLARI/THE_PAYLOAD.md`

---

INPUT MODE: V
FORMAT: YATAY

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

MATERIAL
What you were given: compilation edit · duration 245s
Cuts you can see: 24 · 0:10, 0:19, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00
Aspect ratio: 16:9

THE CHARACTER — as first clearly seen
Face / hair / marks: Dark hair, beard. First frame fully visible: 0:10
Suit / wardrobe: Blue-grey base, orange accents, "PHASE 1" text on chest.
Wear / dirt: Mild dust on shoulders and knees.
Equipment: White dome helmet, dark visor, thick gloves.

THE WORLD — as the footage shows it
Gravity read: 1g (initial dust/walking), changing to 0g (orbit).
Atmosphere read: Dense dust storm on surface, vacuum in space.
Light sources: Distant sun (soft directional), internal practicals.
Location: Mars-like desert, ship interior, orbital space.

MOTION
Camera: Static lockoffs, slow pushes.
Subject: Slow, deliberate walking and reaching.

FILM: (not supplied)
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation (observed)
VIDEO DURATION: 245s MEASURED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 24 · 0:10, 0:19, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00
NON-SCENE MATERIAL: 4:00-4:06 Title card
LINES HEARD: 4 · 1:11 "I'm stepping down to the pad now." · 1:15 "Setting the first case down on the regolith." · 1:18 "Turning back for the next one." · 2:51 "Control, this is..."

SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      36.0
DIVISION:           36.0 ÷ 8 = 4.5

OVERALL SCORE: 4.5/10 (3 categories marked N/A, 1 marked UNVERIFIABLE excluded)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    3/10    −2 · 0:10 (F1) · −2 · 1:20 (F2) · −2 · 1:40 (F3)
Scale & Physics    3/10    −4 · 2:30 (F4)
Camera    6/10    no in-scope source
Lighting    6/10    −1 · 2:00 (F5)
Environment    5/10    −2 · 0:19 (F6)
Creatures    N/A    no in-scope source
Particles & Materials    4/10    −1 · 0:40 (F7) · −2 · 2:00 (F8)
Dialogue & Audio    6/10    no in-scope source
Frame Anchor Fidelity    UNVERIFIABLE    no in-scope source
Negative Violations    5 count    −
Motion Quality    3/10    −4 · 2:30 (F9)
Vertical Format (9:16)    N/A    format yatay
Safe Zone    N/A    format yatay
Hook Timing    N/A    format yatay

SCENE INVENTORY
See BASELINE block above.

PRESENCE STRING
111111111111-111-1-1--1-

SEVERITY TALLY
🔴 BLOCKER: 4    🟠 MAJOR: 3    🟡 MINOR: 2

TOP 3 CRITICAL ERRORS (most impactful)
2:30 — 🔴 BLOCKER — Cylinder displays mixed physics; falls at 1g then randomly hovers in 0g.
1:40 — 🔴 BLOCKER — Duplicate human character walks past identical stationary character.
0:10 — 🔴 BLOCKER — Clear, legible text ("PHASE 1") burned into the character's suit.

DETAILED ERROR LOG
0:10 — 🔴 BLOCKER — Character — Text "PHASE 1" clearly printed on chest plate.
0:19 — 🟡 MINOR — Environment — Ground terrain texture swims slightly as subject walks.
0:40 — 🟡 MINOR — Particles — Sand pouring from strut exhibits liquid/gel viscosity.
1:18 — 🔴 BLOCKER — Character — Text "EVA" printed on suit back.
1:20 — 🟠 MAJOR — Character — Thumb merges into the metal strut upon contact.
1:40 — 🔴 BLOCKER — Character — Clone character walks past the main subject.
2:00 — 🟠 MAJOR — Particles — Rocket exhaust plumes are weightless CGI spray, no ground interaction.
2:00 — 🟡 MINOR — Lighting — Slight AI bloom on the engine ignition flares.
2:30 — 🔴 BLOCKER — Scale & Physics — Cylinder object falls fast, hits chest, then suspends in zero-g micro-motion.
2:30 — 🔴 BLOCKER — Motion Quality — Conflicting speed/vectors in one frame (fast fall vs. weightless float).

WHAT WORKED WELL
Deep atmospheric dust rendering creates excellent mood.
Space exterior lighting is generally sharp and high-contrast.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "solo character, isolated, lone figure" → prevents duplicate clones.
REMOVE from image prompt: "logos, text, decals, patches" → causes Negative Bible text violations.
ADD to video prompt: "rigid body collision, solid metal interaction" → prevents hand-phasing on struts.

🔴 DERS 1: MIXED GRAVITY VECTORS
Kaynak: (not supplied) QA — Fizik: 3/10 — 2:30 — cylinder displays mixed physics
Sorun: Nesneler aynı kare içinde hem Dünya yerçekimine hem de sıfır yerçekimine göre hareket ediyor.
ÇÖZÜM — PROMPT GÜNCELLEMESİ:
uniform zero-gravity physics, all objects floating slowly, continuous low-g momentum

NEGATIVE BIBLE VIOLATIONS
[x] Text visible on screen (0:10, 1:18)
[x] Duplicate characters (1:40)
[x] Object phasing/clipping (1:20)
[x] Low-density CGI particle spray on impacts (2:00)
[x] Mixed gravity / vectors in one frame (2:30)

NEGATIVE BOX COUNT: 5 · LINKED FINDINGS: 5 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 5 · TICKED: 5 · MISSED: 0

OUT-OF-SCOPE FLAGS
Suit design, details, and color shift entirely between cuts → CONTINUITY lens.

FLAGS FOR DOCUMENT CHECK
0:30 — Cuts observed — Were compilation scene boundaries intended at these timecodes?
2:30 — Zero-g motion — Was the scene set for 1g or 0g? (Clip mixes both).

QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 3/10 | 3/10 | 6/10 | 6/10 | 5/10 |  | 4/10 | 6/10 |  | 3/10 |  |  |  | 5 | 4.5/10 |
