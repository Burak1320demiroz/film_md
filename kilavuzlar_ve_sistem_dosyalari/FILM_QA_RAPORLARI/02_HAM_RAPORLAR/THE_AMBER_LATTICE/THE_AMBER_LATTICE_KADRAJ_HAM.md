INPUT MODE: V
FILM: THE_AMBER_LATTICE
RUNTIME: 01:45 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 10 · CUTS COUNTED: 9 · CUTS OFF GRID: none (mode V)
NON-SCENE MATERIAL: 01:39.5–01:45 title card slate ("THE AMBER LATTICE")
PRESENCE STRING: 1111111111
LINES HEARD: 1 · 00:55–00:57 "The light is climbing."
SETUPS REGISTERED: 10 distinct camera positions
LOCKOFF HELD: 10 / 10 clips

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  3
SUM OF SCORES:      17.0
DIVISION:           17.0 ÷ 3 = 5.7

OVERALL SCORE: 5.7/10
VERDICT: RHYME BROKEN

## SETUP LEDGER

| Scene | in | plan letter | observed size / angle / lens / position | observed letter | MATCH · NEAR · MISS | anchor position | in-clip movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 00:00 | N/A | EWS / eye-low angle / wide lens / side-front 15m | A (S1) | N/A (mode V) | monolith base right, mountain peak horizon left | 0 |
| S2 | 00:09 | N/A | MCU-MS / eye level / normal lens / profile 2m | B (S2) | N/A (mode V) | door seam bevel right | 0 |
| S3 | 00:19 | N/A | ECU / high-side angle / macro lens / close-up hand 0.3m | C (S3) | N/A (mode V) | scanner nose and wall crack junction | 0 |
| S4 | 00:29 | N/A | MS-WS / low angle upward tilt / wide lens / rear-centered 5m | D (S4) | N/A (mode V) | central vertical monolith door line | 0 |
| S5 | 00:39 | N/A | WS / high angle (~45°) / wide lens / quarter top-down 8m | E (S5) | N/A (mode V) | lower left base corner flange | 0 |
| S6 | 00:49 | N/A | CU / eye level / normal-long lens / front headshot 0.8m | F (S6) | N/A (mode V) | helmet gold visor rim | 0 |
| S7 | 00:59 | N/A | EWS / high angle bird's eye / ultra-wide lens / canyon vista 50m | G (S7) | N/A (mode V) | canyon wall rim outline | 0 |
| S8 | 01:09 | N/A | CU / low ground angle / normal lens / boots & ground 0.5m | H (S8) | N/A (mode V) | right boot heel rim | 0 |
| S9 | 01:19 | N/A | MS-WS / eye level / wide lens / three-quarter front 6m | I (S9) | N/A (mode V) | left monolith base pillar edge | 0 |
| S10 | 01:29 | N/A | EWS / low-eye angle night vista / wide lens / rear-left distant 30m | J (S10) | N/A (mode V) | monolith top apex & left cliff edge | 0 |

## SETUP STRING

OBSERVED:   ABCDEFGHIJ
PLAN:       (none — mode V)
DIFFERS AT: N/A (mode V)

## PRESENCE STRING

1111111111

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / EWS / eye-low angle / monolith base right & horizon peak / daytime lighting | J / EWS / low-eye angle night vista / monolith apex & left cliff / nighttime lighting | No |

`PAIR FAILS` — S10 introduces a brand-new camera position (Setup J) with centered framing and altered background geometry instead of returning to Setup A.

## LOCKOFF VERIFICATION

all held

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | N/A in mode V |
| 2 | Lockoff Integrity | 7/10 | S1–S10 (00:00–01:39): No in-clip drift or breathing detected across all 10 scenes. |
| 3 | Rhyme Pair | 4/10 | S1 (00:00) vs S10 (01:29): Closing frame fails to match opening framing setup, anchor, or scale. |
| 4 | Return Consistency | N/A | No setup letters repeat across scenes; every scene uses a new camera position. |
| 5 | Cluster Seams | N/A | No split shots or declared seams present in footage. |
| 6 | Angle Arc & Deliberate Shocks | 6/10 | S3 (00:19) to S4 (00:29): Abrupt scale jump from hand ECU to low-angle WS without transitional framing. |
| 7 | Screen Geometry | N/A | No setup repeats present to evaluate geometry stability across returns. |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 0   🟡 MINOR: 1

## THE THREE THAT MATTER

1. 🔴 **01:29 (S10)**: Closing shot breaks bookend structure by employing a new camera position (Setup J) instead of returning to Setup A. *Fix:* Regenerate S10 using exact Setup A camera parameters at night.
2. 🟡 **00:29 (S4)**: Scale jump from S3 ECU (00:19) to S4 Low-Angle WS (00:29) creates visual disorientation. *Fix:* Insert a transitional MS or adjust cut order in edit.
3. 🟡 **00:59 (S7)**: Extreme high-angle vista following tight CU in S6 creates harsh perspective shift. *Fix:* Moderate camera elevation in shot generation.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Rhyme Pair Mismatch (S10)**: Requires regeneration. Reframing camera angle and perspective to mirror Setup A cannot be achieved via cropping.
* **Scale Jump (S3 to S4)**: Fixable in edit by adding an intermediary medium shot or trimming cut points.

## FLAGS FOR DOCUMENT CHECK

* Mode V evaluation; verify if SPEC intended setup repeats for S10 (Rhyme pair) or a linear 10-setup sequence.

## OUT-OF-SCOPE FLAGS

* **00:00 vs 01:29 [CONTINUITY / BACKGROUND]**: Atmospheric ground smoke density and crack structures alter significantly between scenes.
* **00:49 vs 00:59 [LIGHTING]**: Key light direction shifts rapidly relative to ground cracks.
