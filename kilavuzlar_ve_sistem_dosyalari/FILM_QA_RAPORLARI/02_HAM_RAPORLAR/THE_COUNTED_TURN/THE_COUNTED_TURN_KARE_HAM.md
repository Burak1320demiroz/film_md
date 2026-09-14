INPUT MODE: D
FORMAT: YATAY

BASELINE: AGAINST DOCUMENT (mode D)
FILM: THE_COUNTED_TURN
ASPECT MEASURED: 16:9 (measured from file)
LENGTH CLASS: 3-5dk
SCENE: Compilation
VIDEO DURATION: 254.0s measured
MATERIAL TYPE: FILM
CUTS COUNTED: 24 cuts — 0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00
NON-SCENE MATERIAL: 4:10-4:14 title card
LINES HEARD: none — nothing audible to me
SPEC BLOCK PROVIDED: partial — PIPELINE, CHARACTER, SUIT, CHARACTER HEIGHT, LOCOMOTION MODE, LENS, CAMERA DISTANCE, LIGHT SOURCES, FILL LIGHT ALLOWED, VEHICLE/STRUCTURE, AUDIO LAYERS missing

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      52.0
DIVISION:           52.0 ÷ 8 = 6.5

OVERALL SCORE: 6.5/10 (3 categories excluded: Creatures, Frame Anchor Fidelity, Vertical Format, Safe Zone, Hook Timing. Wait, that's 5 excluded categories. Scored: 1, 2, 3, 4, 5, 7, 8, 11).
VERDICT: REGENERATE

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 1/10 | −3 · 0:27 (F1) <br> −3 · 0:35 (F1) <br> −3 · 3:25 (F1) |
| Scale & Physics | 7/10 | −3 · 2:44 (F2) |
| Camera | 10/10 | none |
| Lighting | 10/10 | none |
| Environment | 9/10 | −1 · 2:54 (F5) |
| Creatures | — | no in-scope source |
| Particles & Materials | 1/10 | −3 · 1:26 (F7) <br> −3 · 1:44 (F7) <br> −3 · 3:05 (F7) |
| Dialogue & Audio | 7/10 | −3 · 4:10 (F8) |
| Frame Anchor Fidelity | — | no in-scope source |
| Negative Violations | 4 count | BOX 4 · LINKED 4 · UNLINKED 0 |
| Motion Quality | 7/10 | −3 · 1:17 (F11) |
| Vertical Format (9:16) | N/A | none |
| Safe Zone | N/A | none |
| Hook Timing | N/A | none |

FINDINGS WITH A MATCHING BOX: 4 · TICKED: 4 · MISSED: 0
NO BOX EXISTS FOR: stiff/mechanical motion, texture swimming

## PRESENCE STRING

1111110111111111101111110

## SEVERITY TALLY

🔴 BLOCKER: 8    🟠 MAJOR: 1    🟡 MINOR: 1

## TOP 3 CRITICAL ERRORS (most impactful)

1. 0:27 — 🔴 BLOCKER — Left hand fingers severely morph and melt, fusing completely with the strap geometry.
2. 0:35 — 🔴 BLOCKER — The right thumb phases entirely through the solid metal of the orange carabiner.
3. 2:44 — 🔴 BLOCKER — The orange carabiner phases completely through the solid metal of the rail as it is pressed down.

## DETAILED ERROR LOG

0:27 — 🔴 BLOCKER — Character — Left hand fingers severely morph and melt, fusing completely with the strap geometry.
0:35 — 🔴 BLOCKER — Character — The right thumb phases entirely through the solid metal of the orange carabiner.
1:17 — 🟠 MAJOR — Motion Quality — The astronaut's upward movement as they rise from the spool is unusually stiff, rigid, and mechanical.
1:26 — 🔴 BLOCKER — Particles & Materials — The grey fabric strap passes directly through the palm of the right glove.
1:44 — 🔴 BLOCKER — Particles & Materials — The fabric strap phases through the solid metal floor pin as tension is applied.
2:44 — 🔴 BLOCKER — Scale & Physics — The orange carabiner phases completely through the solid metal of the rail as it is pressed down.
2:54 — 🟡 MINOR — Environment — Subtle texture swimming and shadow shifting on the metal rail during the empty tracking shot.
3:05 — 🔴 BLOCKER — Particles & Materials — The grey strap becomes embedded inside the geometry of the right glove.
3:25 — 🔴 BLOCKER — Character — The fingers of the right hand merge into and fuse with the orange carabiner metal.
4:10 — 🔴 BLOCKER — Dialogue & Audio — A burned-in title card ("THE COUNTED TURN") appears on screen, violating the strict 0.0s screen text lock.

## WHAT WORKED WELL (keep these in future prompts)

* Excellent lighting consistency; the high-contrast, harsh directional lighting accurately simulates a deep-space environment without AI bloom.
* Strong adherence to the fixed camera constraint; the locked-off angles remain perfectly steady without drift or wobble across all 25 clips.
* The suit design and helmet reflections maintain a very high degree of physical plausibility and temporal stability.

## PROMPT IMPROVEMENT SUGGESTIONS

1. ADD to video prompt: "Solid objects maintain strict collision boundaries; hands push against surfaces without penetrating them." → prevents object phasing and hand-surface fusion.
2. ADD to video prompt: "Fabric straps rest on top of gloves and metal pins, obeying physical collision." → prevents rope/tether clipping through surfaces.
3. REMOVE from image/video prompt: Any text prompts calling for "title card," "cinematic titles," or "ending text." → prevents burned-in on-screen text.

## NEW LESSON CANDIDATE

No new lesson — all errors map to the failure patterns listed above (4, 7, 11).

## OUT-OF-SCOPE FLAGS

4:10 — Hook scene was not trimmed to 9.0s; all cuts land perfectly on a 10.0s grid, pushing the total footage runtime to 250s instead of the budgeted 249s. → CONTINUITY lens
2:40 — Presence string is 1111110111111111101111110 (S16 has a human, S17 is empty), which contradicts the stated plan sequence of 1111110111111111011111110. → CONTINUITY lens

## FLAGS FOR DOCUMENT CHECK

none

## QUALITY TABLE ROW

| THE_COUNTED_TURN | YATAY | Compilation | 1/10 | 7/10 | 10/10 | 10/10 | 9/10 | — | 1/10 | 7/10 | — | 7/10 |  |  |  | 4 | **6.5/10** |
