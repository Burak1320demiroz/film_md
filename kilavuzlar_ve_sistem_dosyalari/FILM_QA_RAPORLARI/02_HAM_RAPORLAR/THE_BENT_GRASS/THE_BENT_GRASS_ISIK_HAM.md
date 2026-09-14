INPUT MODE: D
FILM: THE_BENT_GRASS
RUNTIME: 02:16 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0 · 10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100 · 110 · 120 · 130
SCENES OBSERVED: 13 · CUTS COUNTED: 12 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 2:10-2:16 title card
PRESENCE STRING: 11111-111111-
LINES HEARD: none — room tone present
ZONES REGISTERED: 1 · MEDIUM: air, 0.90 atm, soft shadow, fill allowed
LIGHT JUMPS: 3 · CLEAN CUTS: 9

SCORED CATEGORIES:  7
SUM OF SCORES:      46.0
DIVISION:           46.0 ÷ 7 = 6.5

OVERALL SCORE: 6.5/10
VERDICT: KEY WALKS

## ZONE REGISTER

· zone            [PLAIN · S0 to S13]
· sources         [1 · sun, descending]
· key direction   [9 clock as seen from camera · descending elevation]
· key quality     [hard]
· shadow          [lifted · edge soft]
· temperature     [warm]
· fill            [ambient sky]
· medium          [air — soft shadow and distant haze allowed]
· change allowed  [monotonic descent of sun angle only, -0.9° per scene]

## LIGHT LEDGER

S0 | 0:00 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S1 | 0:10 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S2 | 0:20 | PLAIN | ? (flat) | soft | soft edge | neutral | sun lit | mid | dark | 0
S3 | 0:30 | PLAIN | 3 (high) | hard | soft edge | warm | sun lit | bright | dark | 0
S4 | 0:40 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S5 | 0:50 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | - | dark | 0
S6 | 1:00 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S7 | 1:10 | PLAIN | ? (flat) | soft | soft edge | neutral | sun lit | mid | dark | 0
S8 | 1:20 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S9 | 1:30 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S10 | 1:40 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S11 | 1:50 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | bright | dark | 0
S12 | 2:00 | PLAIN | 9 (low) | hard | soft edge | warm | sun lit | - | dark | 0

## KEY DIRECTION STRING

OBSERVED:  9 9 ? 3 9 9 9 ? 9 9 9 9 9
ZONES:     A A A A A A A A A A A A A

## PRESENCE STRING

11111-111111-

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| S1 → S2 | PLAIN | Key direction lost (9 → ?); temperature cools (warm → neutral); subject exposure drops (bright → mid) | no | 🟠 MAJOR |
| S2 → S3 | PLAIN | Key direction returns but flips sides (3); temperature warms back up; exposure rises | no | 🔴 BLOCKER |
| S6 → S7 | PLAIN | Key direction lost (9 → ?); temperature cools; exposure drops | no | 🟠 MAJOR |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 3/10 | -7 · Key lost at S2 (0:20), S7 (1:10); key flips sides at S3 (0:30) (Pattern ①, ⑫) |
| 2 | Shadow Quality & Fill | 10/10 | no in-scope source |
| 3 | Colour Temperature | 6/10 | -4 · Temperature wobbles from warm to neutral at S2 (0:20), S7 (1:10) and back (Pattern ③) |
| 4 | Practical Sources | N/A | only source is the sun (environmental) |
| 5 | Exposure at Cuts | 5/10 | -5 · Subject exposure drops mid-zone at S2 (0:20) and S7 (1:10) (Pattern ⑤) |
| 6 | In-Clip Stability | 10/10 | no in-scope source |
| 7 | Zone Boundaries | 2/10 | -8 · Unplanned shifts in key, temperature, and exposure inside a single continuous zone |
| 8 | Atmosphere Honesty | 10/10 | no in-scope source |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 0

## THE THREE THAT MATTER

1. 0:30 — S3 flips the sun to the right side of the frame (3 o'clock). Fix: Regenerate S3 with prompt locked to "sun from screen left".
2. 0:20 — S2 loses the key light entirely, rendering a flat, neutrally lit shot in the middle of a golden-hour sequence. Fix: Regenerate S2 enforcing the strong directional key light.
3. 1:10 — S7 suffers the same flat-light reset as S2. Fix: Regenerate S7 with the correct sun position.

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

**FIXABLE IN THE GRADE:**

* The temperature shifts (neutral instead of warm) and exposure drops in S2 and S7 could partially be warmed and lifted in the grade.

**REQUIRES REGENERATION:**

* S3's flipped key direction (shadows falling left instead of right) is baked into the geometry and must be regenerated.
* The complete absence of modelling (flat lighting) in S2 and S7 cannot be fully corrected in post; dodging and burning will not replace a missing key shadow.

## FLAGS FOR DOCUMENT CHECK

* The sun descent arc (-0.9° per scene) is not visually readable on screen; the sun angle appears constant when it is present.

## OUT-OF-SCOPE FLAGS

* SETUP: The scenes with the worst lighting errors (S2, S3, S7) are the same scenes that broke the setup locks in the Kadraj report.
