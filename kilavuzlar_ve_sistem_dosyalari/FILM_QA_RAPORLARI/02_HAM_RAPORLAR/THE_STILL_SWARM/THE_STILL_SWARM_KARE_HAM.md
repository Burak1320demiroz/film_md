# HAM RAPOR — THE STILL SWARM · ① KARE (T1)

```
KÜNYE (operatör tarafından doldurulmadı — D160 ihlali)
girdi: <tam yol YOK> · <süre YOK> · <çözünürlük YOK>
işlendiği tarih: 02.09.2026 · işleyen kart: qa-isle
⛔ ⑪ ölçüm kapısı KOŞULAMADI (master verilmedi) → bu raporun süre ve
   sahne sayıları HİÇBİR KAPIYA girmedi.
⛔ ① SPEC kapısı: film klasöründe THE_STILL_SWARM_QA_SPEC.md VAR, rapor
   mod V koşuldu → koşu TEKRARLANIR, T tablosuna satır YAZILMAZ [D129].
```

---

FORMAT: YATAY
INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?" It does NOT answer "does this clip match its design document."

FILM: (not supplied)
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 2:15 MEASURED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 12 (0:10, 0:19, 0:30, 0:39, 0:49, 0:59, 1:09, 1:19, 1:29, 1:39, 1:49, 1:59)
NON-SCENE MATERIAL: 2:09-2:15 title card
LINES HEARD: none — music tone present
SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES:  7
SUM OF SCORES:      27.0
DIVISION:           27.0 ÷ 7 = 3.8

OVERALL SCORE: 3.8/10 (7 categories excluded: Creatures, Dialogue, Frame Anchor, Vertical, Safe Zone, Hook Timing, Negative Violations)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    3/10    −3 · 1:42 (F1) · 2:00 (F2) · 2:01 (F3)
Scale & Physics    3/10    −2 · 0:39 (F4) · 2:01 (F5)
Camera    4/10    −3 · 0:59 (F6)
Lighting    5/10    −2 · 0:49 (F7)
Environment    5/10    −2 · 0:20 (F8)
Creatures    —    no in-scope source
Particles & Materials    3/10    −4 · 0:19 (F9) · 0:58 (F10) · 1:40 (F11)
Dialogue & Audio    —    no in-scope source
Frame Anchor Fidelity    —    no in-scope source
Negative Violations    7 count    linked below
Motion Quality    4/10    −2 · 1:25 (F12) · 1:42 (F13)
Vertical Format (9:16)    N/A    horizontal media
Safe Zone    N/A    horizontal media
Hook Timing    N/A    horizontal media

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 135s
Cuts you can see:    12 (0:10, 0:19, 0:30, 0:39, 0:49, 0:59, 1:09, 1:19, 1:29, 1:39, 1:49, 1:59)
Aspect ratio:        16:9

THE CHARACTER
Face / hair / marks: Female, short dark hair, no visible scars. First frame fully visible: 0:10
Suit / wardrobe:     Light gray space suit, canvas belt, metal clips, clear helmet.
Wear / dirt:         Clean, minimal smudges on shoulder/back.
Equipment:           Belt tools, grey box, metal clamp.

THE WORLD
Gravity read:        Zero-g / microgravity.
Atmosphere read:     Vacuum.
Light sources:       Single hard directional source (sun), stark shadows.
Location:            Giant spherical panel structure, cylindrical airlock.

MOTION
Camera:              Slow pushes, tracks, slight orbits.
Subject:             Floating, tether pulling, slow hand movements.

PRESENCE STRING
1111111111111

SEVERITY TALLY
🔴 BLOCKER: 6    🟠 MAJOR: 4    🟡 MINOR: 3

TOP 3 CRITICAL ERRORS
2:00 — 🔴 BLOCKER — Duplicate character phases out of structure behind main subject.

2:01 — 🔴 BLOCKER — Extra limbs/arms appear holding the wall.

1:40 — 🔴 BLOCKER — Background debris particles are entirely static/frozen.

DETAILED ERROR LOG
1:42 — 🟠 MAJOR — Character — Hand melting/morphing when interacting with clamp.
2:00 — 🔴 BLOCKER — Character — Duplicate head/body spawns in background.
2:01 — 🔴 BLOCKER — Character — Three arms visible on subject.
0:39 — 🟠 MAJOR — Scale & Physics — Tool removal physics rigid, minor hand clipping.
2:01 — 🔴 BLOCKER — Scale & Physics — Floating canvas belt clips completely through torso.
0:59 — 🔴 BLOCKER — Camera — Hidden cut/jump inside scene; pose shifts instantly.
0:49 — 🟠 MAJOR — Lighting — AI bloom on emitted gas and suit back.
0:20 — 🟠 MAJOR — Environment — Floating panels exhibit texture swimming.
0:19 — 🟠 MAJOR — Particles & Materials — Floating panels lack continuous momentum.
0:58 — 🔴 BLOCKER — Particles & Materials — Gas emission freezes into static 2D plane.
1:40 — 🔴 BLOCKER — Particles & Materials — Surrounding debris frozen in space.
1:25 — 🟡 MINOR — Motion Quality — Slight jello warping on tether.
1:42 — 🟡 MINOR — Motion Quality — Rigid, dragged model movement rather than drift.

NEGATIVE BOX COUNT: 7 · LINKED FINDINGS: 7 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 7 · TICKED: 7 · MISSED: 0
NO BOX EXISTS FOR: texture swimming on non-geological props, missing particle momentum (macro scale).

WHAT WORKED WELL
Consistent light direction across most cuts.

Suit details remain relatively stable across varying focal lengths.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to video prompt: "Continuous physical momentum, drifting limbs, axis rotation" → prevents rigid dragged movement.

REMOVE from image prompt: "cinematic glowing smoke" → causes AI bloom and 2D freezing.

REPLACE "complex background action" with "solo subject, empty background" → prevents duplicate spawning near structures.

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above 1, 3, 5, 8, 10.

OUT-OF-SCOPE FLAGS
none

FLAGS FOR DOCUMENT CHECK
2:09 — Title card appears — QUESTION: Was text permitted for this compilation?
0:00 — Zero-g environment observed — QUESTION: Was zero-g specified?
1:09 — Unmotivated fill in shadows — QUESTION: Was fill light allowed?

QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 3 | 3 | 4 | 5 | 5 | — | 3 | — | — | 4 |  |  |  | 7 | 3.8/10 |
