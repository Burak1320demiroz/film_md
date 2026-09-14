# THE SKYLIGHT — ① KARE QA · HAM RAPOR

> Model çıktısı, OLDUĞU GİBİ (kural ④). Düzeltilmez, kısaltılmaz.
> Koşu: 29.08.2026'da sahip tarafından yapıştırıldı · Gemini · rubrik `1_KARE_QA_CRITIQUE_PROMPT.md` · MOD V
> Dosya (raporun künyesi): `the skylight.mp4`
> ⛔ Film klasöründe `THE_SKYLIGHT_QA_SPEC.md` VARDIR → bu koşu ÖN KOŞU'dur, tekrarlanır [D129].
> Değerlendirme: `01_FILM_RAPORLARI/THE_SKYLIGHT.md`

---

FORMAT: YATAY
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 315 s ESTIMATED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 30 (0:10, 0:20, 0:29, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:49, 2:00, 2:09, 2:20, 2:29, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 3:59, 4:09, 4:19, 4:29, 4:39, 4:49, 4:59)
NON-SCENE MATERIAL: 5:10-5:15 Title Card
LINES HEARD: none — nothing audible to me
SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES: 5
SUM OF SCORES: 34.0
DIVISION: 34.0 ÷ 5 = 6.8

OVERALL SCORE: 6.8/10 (9 categories excluded: 5 unverifiable/no in-scope source, 1 count, 3 N/A)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    4/10    −4 · 2:07 (F1) · −1 · 0:14 (F2) · −1 · 4:16 (F3)
Scale & Physics    6/10    −3 · 4:24 (F1) · −1 · 4:52 (F2)
Camera    —    no in-scope source
Lighting    8/10    −2 · 1:31 (F1)
Environment    —    no in-scope source
Creatures    —    no in-scope source
Particles & Materials    8/10    −2 · 2:14 (F1)
Dialogue & Audio    —    no in-scope source
Frame Anchor Fidelity    —    no in-scope source
Negative Violations    6 count    LINKED FINDINGS: 6 · UNLINKED: 0
Motion Quality    8/10    −2 · 3:39 (F1)
Vertical Format (9:16)    N/A    [FORMAT: YATAY]
Safe Zone    N/A    [FORMAT: YATAY]
Hook Timing    N/A    [FORMAT: YATAY]
SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 315 s
Cuts you can see: 30 (0:10, 0:20, 0:29, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:49, 2:00, 2:09, 2:20, 2:29, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 3:59, 4:09, 4:19, 4:29, 4:39, 4:49, 4:59)
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Caucasian female, auburn hair, light freckles, small scar on right eyebrow. First frame fully visible: 1:20
Suit / wardrobe: Cream/white spacesuit, tan accents, grey rectangular chest panel, waist harness.
Wear / dirt: Heavy dust accumulation on knees, shins, and lower boots.
Equipment: White helmet with clear visor, small hand lantern, silver baton tool on lower back.

THE WORLD
Gravity read: Sub-1g to 1g (dust falls steadily, footfalls appear weighted).
Atmosphere read: Vacuum on surface (black sky), thin atmosphere in caves (dust hangs in light beams).
Light sources: Stark directional sun (harsh shadows, high contrast), portable lantern (warm, diffuse).
Location: Mars-like rocky surface, deep impact craters, and subterranean cave network.

MOTION
Camera: Predominantly slow, stable push-ins and static lockoffs.
Subject: Slow, deliberate walking, kneeling, and interacting with environmental rocks and dust.

PRESENCE STRING
111111111111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 2    🟠 MAJOR: 4    🟡 MINOR: 1

TOP 3 CRITICAL ERRORS
2:07 — 🔴 BLOCKER — A duplicate astronaut inexplicably spawns on the left side of the frame alongside the original subject.

4:24 — 🔴 BLOCKER — Rocket exhaust flames clip entirely through the solid metal landing legs of the vehicle during liftoff.

4:52 — 🟠 MAJOR — The floating bolt indicates a zero-g environment, but the character remains perfectly rigid in the seat with zero limb drift or micro-motion.

DETAILED ERROR LOG
0:14 — 🟠 MAJOR — Character — Fingers morph and fuse into the rock texture upon contact.
1:23 — 🟡 MINOR — Character — Slight waxy/plastic skin smoothing on the facial close-up.
1:31 — 🟠 MAJOR — Lighting — The hand lantern emits a diffuse AI bloom rather than directional optical light.
2:07 — 🔴 BLOCKER — Character — Duplicate character appears mid-shot.
2:14 — 🟠 MAJOR — Particles & Materials — Falling dust floats and phases through the character's glove instead of colliding.
3:39 — 🟠 MAJOR — Motion Quality — Character glides/moonwalks over the terrain without visibly planting feet.
4:16 — 🟠 MAJOR — Character — Hands morph and blend seamlessly into the seatbelt straps.
4:24 — 🔴 BLOCKER — Scale & Physics — Exhaust clips through solid objects.
4:52 — 🟠 MAJOR — Scale & Physics — Rigid 1g character model suspended in zero-g environment.

NEGATIVE BIBLE VIOLATIONS
[x] Airbrushed, waxy, or plastic skin texture
[x] AI bloom / soft glow filter / dreamy haze on light sources
[x] Object phasing/clipping (any solid passing through another solid)
[x] Duplicate characters (clone of the solo character appearing)
[x] Rigid floating character (no limb drift or axis rotation)
[x] Hand-surface fusion
NEGATIVE BOX COUNT: 6 · LINKED FINDINGS: 6 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 6 · TICKED: 6 · MISSED: 0
NO BOX EXISTS FOR: character moonwalking

WHAT WORKED WELL
Excellent continuity of the spacesuit design across a very high number of separate scenes.

The cave environment's lighting contrast and scale are highly cinematic.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to video prompt: "perfect collision physics, solid objects block exhaust flames" → prevents object phasing/clipping

REMOVE from image prompt: "cinematic lighting" → causes AI bloom and plastic skin smoothing

REPLACE "floating in space" with "continuous micro-motion, free-floating axis rotation, limbs drifting naturally" → prevents rigid floating character

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above [2, 3, 4, 8, 10].

OUT-OF-SCOPE FLAGS
None

FLAGS FOR DOCUMENT CHECK
none

QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 4/10 | 6/10 | | 8/10 | | | 8/10 | | | 8/10 | | | | 6 | 6.8/10 |
