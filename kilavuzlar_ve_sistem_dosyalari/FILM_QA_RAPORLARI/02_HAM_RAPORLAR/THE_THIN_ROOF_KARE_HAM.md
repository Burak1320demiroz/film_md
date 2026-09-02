# THE THIN ROOF — ① KARE QA · HAM RAPOR

> Model çıktısı, OLDUĞU GİBİ (kural ④). Düzeltilmez, kısaltılmaz.
> Koşu: 28.08.2026 · rubrik `1_KARE_QA_CRITIQUE_PROMPT.md` · MOD V
> ⛔ Film klasöründe `THE_THIN_ROOF_QA_SPEC.md` VARDIR → bu koşu ÖN KOŞU'dur [D129].
> Değerlendirme: `01_FILM_RAPORLARI/THE_THIN_ROOF.md`

---

FORMAT: DİKEY
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: DİKEY
ASPECT MEASURED: 9:16
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 64 seconds measured
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 5 cuts (0:10, 0:20, 0:30, 0:40, 0:50)
NON-SCENE MATERIAL: 1:00-1:04 title card
LINES HEARD: none — no audio information at all
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      65.0
DIVISION:           65.0 ÷ 9 = 7.2

OVERALL SCORE: 7.2/10 (5 categories excluded)
VERDICT: REGENERATE

## SCORES SUMMARY

| Category | Score | Critical Issues |
|---|---|---|
| Character | 3/10 | −7 · 0:30 (F1) |
| Scale & Physics | 7/10 | −3 · 0:52 (F1) |
| Camera | 10/10 | no in-scope source |
| Lighting | 9/10 | −1 · 0:30 (F1) |
| Environment | 9/10 | −1 · 0:15 (F1) |
| Creatures | — | no in-scope source |
| Particles & Materials | 5/10 | −5 · 0:43 (F1) |
| Dialogue & Audio | — | no in-scope source |
| Frame Anchor Fidelity | — | UNVERIFIABLE |
| Negative Violations | 2 count | 0:30 · 0:43 |
| Motion Quality | 6/10 | −4 · 0:52 (F1) |
| Vertical Format (9:16) | 9/10 | −1 · 0:20 (F1) |
| Safe Zone | 7/10 | −3 · 0:30 (F1) |
| Hook Timing | — | no in-scope source |

NEGATIVE BOX COUNT: 2 · LINKED FINDINGS: 2 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 2 · TICKED: 2 · MISSED: 0
NO BOX EXISTS FOR: motion jello, UI occlusion, composition deviation

## SCENE INVENTORY

MATERIAL
What you were given: compilation edit · duration 64s
Cuts you can see: 5 (0:10, 0:20, 0:30, 0:40, 0:50)
Aspect ratio: 9:16

THE CHARACTER — as first clearly seen
Face / hair / marks: Woman, visible through helmet glass. First frame fully visible: 0:00
Suit / wardrobe: White spacesuit, grey/purple accents, chest and back equipment.
Wear / dirt: Clean, some dust on lower boots.
Equipment: Glass dome helmet, gloves, small backpack.

THE WORLD — as the footage shows it
Gravity read: Low gravity, slow movements.
Atmosphere read: Thin atmosphere, dust settles slowly.
Light sources: Single harsh directional sun from upper right, warm color.
Location: cracked black lava plain with yellow/orange canyons.

MOTION
Camera: mostly static and slow push-ins.
Subject: walks, kneels, crawls.

## PRESENCE STRING
111111

## SEVERITY TALLY
🔴 BLOCKER: 1    🟠 MAJOR: 4    🟡 MINOR: 3

## TOP 3 CRITICAL ERRORS (most impactful)
1. 0:30 — 🔴 BLOCKER — Duplicate character (two identical astronaut faces/helmets clip into each other side-by-side at the edge of the cliff).
2. 0:43 — 🟠 MAJOR — Floating particles without gravitational cause (spherical stones levitate and orbit the character like flat CGI assets).
3. 0:52 — 🟠 MAJOR — Motion jello / robotic movement (character stands up with disjointed, physically unnatural momentum).

## DETAILED ERROR LOG
0:15 — 🟡 MINOR — Environment — Slight texture swimming on the canyon cliff edge behind the character.
0:20 — 🟡 MINOR — Vertical Format (9:16) — Character is placed dead center with dead space above and below rather than locked to the lower third.
0:30 — 🔴 BLOCKER — Character — Two identical faces/helmets appear in frame side-by-side, clipping into each other.
0:30 — 🟡 MINOR — Lighting — Slight AI bloom and soft glow on the visors, losing sharp specular highlights.
0:30 — 🟠 MAJOR — Safe Zone — The faces (critical story element) sit in the top 250px UI band.
0:43 — 🟠 MAJOR — Particles & Materials — Spherical stones hover and float around the character without momentum or gravitational cause.
0:52 — 🟠 MAJOR — Scale & Physics — Getting up animation breaks physical weight, character rises with disjointed momentum.
0:52 — 🟠 MAJOR — Motion Quality — Jello effect on the limbs as the character pushes off the ground.

## WHAT WORKED WELL
- The environment lighting remains highly consistent between the separate shots.
- The spacesuit design holds its primary shapes and colors well across multiple angles and cuts.

## PROMPT IMPROVEMENT SUGGESTIONS
1. ADD to image prompt: "solo character, single astronaut, entirely alone" → prevents duplicate character generation at 0:30.
2. REMOVE from image prompt: "floating rocks, mystical anomaly" (if present) → causes spherical stones to hover without gravitational cause.
3. ADD to video prompt: "sharp directional shadows, raw photography, unedited" → prevents AI bloom on the visors.

## NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above (2, 3, 5, 11).

## OUT-OF-SCOPE FLAGS
none

## FLAGS FOR DOCUMENT CHECK
0:43 — stones levitate around the character — QUESTION: is this a scripted zero-gravity anomaly or a particle physics failure?
1:00 — title card text "THE THIN ROOF" — QUESTION: is this burned-in text intentional for the final master, or a generator artifact?

## QUALITY TABLE ROW
| the thın roof.mp4 Ⓥ | DİKEY | Compilation | 3 | 7 | 10 | 9 | 9 | | 5 | | | 6 | 9 | 7 | | 2 | 7.2/10 |
