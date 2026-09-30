FORMAT: YATAY

INPUT MODE: D — documented
BASELINE: AGAINST DOCUMENT
FILM: THE_SIGNAL_KEEPERS
FORMAT: YATAY        ASPECT MEASURED: 16:9
LENGTH CLASS: 2 dk
SCENE: Compilation
VIDEO DURATION: 124 s (measured)
MATERIAL TYPE: FILM
CUTS COUNTED: 12 cuts — 0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00
NON-SCENE MATERIAL: 2:00-2:04 title card graphic ("THE STATIC VEIL")
LINES HEARD: none — room tone / ambient music present
SPEC BLOCK PROVIDED: yes

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 9/10 | High suit and visor consistency across cuts |
| Scale & Physics | 8/10 | −2 · 1:13 Atmospheric smoke/haze during welding arc in vacuum |
| Camera | 9/10 | Stable lockoff execution throughout montage |
| Lighting | 8/10 | −2 · 1:13, 1:33 AI bloom and scattering around sparks |
| Environment | 9/10 | Rigid crater rim, structure anchor, and terrain geometry |
| Creatures | — | no in-scope source |
| Particles & Materials | 8/10 | −2 · 1:33 Spark particles show atmospheric drag |
| Dialogue & Audio | 3/10 | −7 · 2:00 (F1) Burned-in title card text on screen |
| Frame Anchor Fidelity | — | no in-scope source |
| Negative Violations | 2 | Text title card (2:00), AI bloom (1:13) |
| Motion Quality | 9/10 | Believable suit weight and low-gravity locomotion |
| Vertical Format (9:16) | N/A | Format is YATAY |
| Safe Zone | N/A | Format is YATAY |
| Hook Timing | N/A | Format is YATAY |

VERDICT: REGENERATE

NEGATIVE BOX COUNT: 2 · LINKED FINDINGS: 2 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 2 · TICKED: 2 · MISSED: 0

## PRESENCE STRING

111111111111

## TOP 3 CRITICAL ERRORS

1. 2:00 — 🔴 BLOCKER — Burned-in title card text "THE STATIC VEIL" violates the 0.0s screen text specification.
2. 1:13 — 🟠 MAJOR — Electrical spark arc generates atmospheric smoke and volumetric haze in a vacuum environment.
3. 1:33 — 🟡 MINOR — Electrical sparks exhibit atmospheric drag and air resistance instead of parabolic vacuum arcs.

## DETAILED ERROR LOG

* 1:13 — 🟠 — Lighting — Volumetric bloom and smoke surrounding electrical arc in vacuum.
* 1:33 — 🟡 — Particles & Materials — Spark particles lose velocity mid-air due to atmospheric drag emulation.
* 2:00 — 🔴 — Dialogue & Audio — Burned-in graphic title card text "THE STATIC VEIL" displayed.

## WHAT WORKED WELL

* Visor reflections, glove anatomy, and suit materials remain consistent across close-up cuts.
* Background crater geometry, beacon framing, and regolith terrain stay locked across setup transitions.

## PROMPT IMPROVEMENT SUGGESTIONS

* ADD to video prompt: "hard vacuum physics, zero atmospheric haze, ballistic particle arcs" → prevents smoke and volumetric scattering
* REMOVE "cinematic glow, soft haze"
* REPLACE "welding smoke" with "clean high-contrast electrical arc flash in vacuum"

## NEW LESSON CANDIDATE

No new lesson — all errors map to patterns 3 (AI bloom), 5 (particle physics), and 11 (unrequested text).

## OUT-OF-SCOPE FLAGS

* Title mismatch: Video title card reads "THE STATIC VEIL" while SPEC title is "THE_SIGNAL_KEEPERS" → STORY lens.

## FLAGS FOR DOCUMENT CHECK

* none

## QUALITY TABLE ROW

| THE_STATIC_VEIL Ⓥ | YATAY | Compilation | 9/10 | 8/10 | 9/10 | 8/10 | 9/10 | | 8/10 | 3/10 | | 9/10 | | | | [Negatif: 2] | — |
