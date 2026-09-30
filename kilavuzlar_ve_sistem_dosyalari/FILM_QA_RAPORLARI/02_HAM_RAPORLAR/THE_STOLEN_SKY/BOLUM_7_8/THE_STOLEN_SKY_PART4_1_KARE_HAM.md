FORMAT: YATAY
INPUT MODE: V — video-only
BASELINE: SELF-CONSISTENCY + PHYSICS — answers "internally consistent and physically believable?", NOT "matches its design document?"
FILM: (not supplied)
FORMAT: YATAY        ASPECT MEASURED: 16:9
LENGTH CLASS: 2-4 dk
SCENE: Compilation
VIDEO DURATION: 239 s measured
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 23 cuts (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50)
NON-SCENE MATERIAL: none
LINES HEARD: 2 · "Delta 6, status checked" at 1:54, "Recalibrate transit telemetry" at 3:17
SPEC BLOCK PROVIDED: no — mode V

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 6/10 | −4 · 0:02 (F1 duplicate asset), 1:44 (F2 disembodied limb) |
| Scale & Physics | 6/10 | −4 · 0:52 (F1 2D debris), 1:44 (F2 gravity anomaly), 2:24 (F3 unnatural bounce) |
| Camera | 8/10 | −2 · 3:15 (F1 texture tracking drift) |
| Lighting | 7/10 | −3 · 1:33 (F1 haze bloom), 2:30 (F2 unmotivated fill in vacuum) |
| Environment | 6/10 | −4 · 0:50 (F1 grid scale shift), 2:40 (F2 black hole drift), 3:15 (F3 rock swimming) |
| Creatures | 6/10 | −4 · 0:30 (F1 alien ground sliding) |
| Particles & Materials | 6/10 | −4 · 0:03 (F1 floating sparks), 1:15 (F2 steam clipping), 2:24 (F3 low-density ejecta) |
| Dialogue & Audio | 9/10 | −1 · 1:54 (F1 off-screen voice alignment) |
| Frame Anchor Fidelity | UNVERIFIABLE | no in-scope source |
| Negative Violations | 11 count | see detailed log |
| Motion Quality | 6/10 | −4 · 0:42 (F1 lever deformation), 1:44 (F2 float jello warp) |
| Vertical Format (9:16) | N/A | horizontal format |
| Safe Zone | N/A | horizontal format |
| Hook Timing | N/A | horizontal format |

VERDICT: REGENERATE

## SCENE INVENTORY

MATERIAL   given: compilation · duration 239 s · cuts: 23 cuts (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50) · aspect: 16:9
CHARACTER  spacesuits in white/grey and blue · first frame fully visible: 0:00 · suit features: dark reflective visors, shoulder insignia, chest indicators, utility belts · wear/dirt: moderate scuffs on knees and boots · equipment: crowbar, sidearm pistol, control consoles, heavy valve cranks
WORLD      interior steel corridors, airlock hatches, hangars, planetary landing pads under orange grid canopy, deep space with black hole · gravity: 1g interior/surface, zero-g floating room at 1:40 · atmosphere: pressurized interior with steam exhaust, exterior space vacuum · light sources: overhead strip lamps, amber warning beacons, orange atmospheric lattice glow
MOTION     camera: static lockoffs and slow push-ins per 10s shot · subjects: characters walking, pulling levers, operating keyboards, shuttles and rockets in flight

## PRESENCE STRING

11111--11111111----------

## TOP 3 CRITICAL ERRORS

1. 1:44 — 🔴 BLOCKER — Disembodied gloved hand and suit helmet floating in mid-air with missing character torso and arm structure.
2. 0:02 — 🔴 BLOCKER — Duplicate character/suit asset clips through doorway frame without prior entry movement.
3. 0:30 — 🔴 BLOCKER — Alien creature glides backwards across corridor floor without leg articulation or planted weight.

## DETAILED ERROR LOG

0:02 — 🔴 BLOCKER — Character — Duplicate suit asset spawns out of door frame without entry motion.
0:03 — 🟡 MINOR — Particles & Materials — Spark particles linger floating in mid-air without gravity drop in 1g room.
0:30 — 🔴 BLOCKER — Creatures — Alien creature slides across floor without walking locomotion or foot plants.
0:42 — 🟠 MAJOR — Character — Gloved hand phases directly through metallic control lever during push action.
0:52 — 🟠 MAJOR — Scale & Physics — Explosion debris around speeder floats as flat 2D planes lacking mass momentum.
1:15 — 🟡 MINOR — Particles & Materials — Vented steam clips directly through character visor surface.
1:33 — 🟡 MINOR — Lighting & Color — Soft AI bloom haze surrounds warning beacon bulb instead of sharp lens falloff.
1:44 — 🔴 BLOCKER — Character — Gloved hand and helmet float disembodied without torso or arm connection.
2:07 — 🟠 MAJOR — Motion Quality — Glove fingers warp and morph into lever handle during pull motion.
2:24 — 🟠 MAJOR — Scale & Physics — Shuttle ramp closing ejects debris with artificial float and zero-g bounce.
2:40 — 🟠 MAJOR — Environment — Orange sky grid structure changes scale and pattern geometry between shots.
3:15 — 🟠 MAJOR — Environment — Canyon rock walls exhibit visible texture swimming and breathing during pan.

## WHAT WORKED WELL

* Hard-surface sci-fi corridor texturing and suit design maintain continuous aesthetic across static setups.
* Industrial color grading with cool teals and warm amber accents creates a cohesive visual tone.
* Audio design and mechanical Foley effects match lever and airlock door movements cleanly.

## PROMPT IMPROVEMENT SUGGESTIONS

* ADD to video prompt: "anatomically connected human body torso, solid mechanical collisions" → prevents disembodied floating limbs and hand-lever phasing
* REMOVE "cinematic lighting, dreamy haze, soft glow"
* REPLACE "alien creature standing" with "alien creature taking heavy articulated steps with weight on ground"

## NEW LESSON CANDIDATE

No new lesson — all errors map to patterns [1, 2, 3, 4, 5, 6, 7, 10].

## OUT-OF-SCOPE FLAGS

none

## FLAGS FOR DOCUMENT CHECK

* 0:50 — Speeder design on rooftop differs from shuttlecraft at 1:00 — QUESTION: Are these two distinct vehicle classes in the production bible?
* 1:40 — Zero-g floating module appears abruptly between 1g corridor shots — QUESTION: Is Scene 11 intended to take place in an unpressurized orbital chamber?

## QUALITY TABLE ROW

| Film Ⓥ | YATAY | Compilation | 6/10 | 6/10 | 8/10 | 7/10 | 6/10 | 6/10 | 6/10 | 9/10 | | 6/10 | | | | [Negatif: 11] | — |

## REVIEWER NOTES

* [x] miniature/toy look · CGI/game aesthetic → 0:50 · cat. 2 · 🟠
* [x] airbrushed, waxy, plastic skin → 1:40 · cat. 1 · 🟠
* [x] AI bloom / dreamy haze → 1:33 · cat. 4 · 🟡
* [x] solid passing through solid → 0:42 · cat. 1 · 🟠
* [x] creature sliding → 0:30 · cat. 6 · 🔴
* [x] melting terrain / swimming rock texture → 3:15 · cat. 5 · 🟠
* [x] duplicate character → 0:02 · cat. 1 · 🔴
* [x] frozen/static/causeless-floating particles → 0:03 · cat. 7 · 🟡
* [x] hand breakdown near glowing surfaces · hand-surface fusion → 2:07 · cat. 11 · 🟠
* [x] structure proportion shift · tilt drift → 2:40 · cat. 5 · 🟠
* [x] low-density impact spray → 2:24 · cat. 7 · 🟠

COUNT total violations: 11
NEGATIVE BOX COUNT: 11 · LINKED FINDINGS: 11 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 11 · TICKED: 11 · MISSED: 0
