INPUT MODE: V
FILM: the gravıty anchor.mp4
RUNTIME: 01:44
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 10 · CUTS COUNTED: 9 · CUTS OFF GRID: none (mode V)
NON-SCENE MATERIAL: 01:40–01:44 title graphic card
PRESENCE STRING: 1111111111
LINES HEARD: none — sci-fi ambiance and sound effects present
SETUPS REGISTERED: 10 distinct camera positions
LOCKOFF HELD: 10 / 10 clips

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  3
SUM OF SCORES:      17.0
DIVISION:           17.0 ÷ 3 = 5.7      ← this is OVERALL SCORE

OVERALL SCORE: 5.7/10
VERDICT: RHYME BROKEN

## SETUP LEDGER

| Scene | Timestamp | Plan Letter | Observed Size / Angle / Lens / Position | Observed Letter | Match | Anchor Position | In-Clip Movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 00:00 | - | EWS / eye level / wide / frontal terrain & monolith | Setup A (first seen S1) | MATCH | terrain ridge lip | 0 |
| S2 | 00:10 | - | MCU / eye level / normal / helmet & wrist console | Setup B (first seen S2) | MATCH | helmet visor rim | 0 |
| S3 | 00:20 | - | MWS / low angle / wide / looking up at monolith | Setup C (first seen S3) | MATCH | monolith left edge | 0 |
| S4 | 00:30 | - | CU / high angle / normal / over-shoulder wrist display | Setup D (first seen S4) | MATCH | wrist display bezel | 0 |
| S5 | 00:40 | - | CU / low ground / normal / boot level floating rocks | Setup E (first seen S5) | MATCH | boot sole contact | 0 |
| S6 | 00:50 | - | MCU / eye level / normal / side profile monolith touch | Setup F (first seen S6) | MATCH | monolith reflective wall | 0 |
| S7 | 01:00 | - | MS / eye level / normal / side view glowing rings | Setup G (first seen S7) | MATCH | ring focal center | 0 |
| S8 | 01:10 | - | ECU / eye level / telephoto / helmet visor reflection | Setup H (first seen S8) | MATCH | visor inner reflection | 0 |
| S9 | 01:20 | - | EWS / high angle / wide / starry floor reflection path | Setup I (first seen S9) | MATCH | monolith base line | 0 |
| S10 | 01:30 | - | WS / eye level / wide / standing by star path | Setup J (first seen S10) | MATCH | star trail border | 0 |

## SETUP STRING

```
OBSERVED:   ABCDEFGHIJ
PLAN:       none (mode V)
DIFFERS AT: none

```

## PRESENCE STRING

1111111111

## RHYME PAIR

|  | First frame (S1) | Last frame (S10) | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | Setup A / EWS / Eye level / Terrain lip / Monolith unanchored | Setup J / WS / Eye level / Star trail / Reflective path added | No |

Verdict line: `PAIR FAILS` — S10 does not reuse Setup A's framing or position, breaking the closing camera rhyme.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S1–S10 | Locked off | Held locked off | none | all held |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V pass (no written spec supplied) |
| 2 | Lockoff Integrity | 6.5/10 | Minor atmospheric micro-drift in S1 (00:00) |
| 3 | Rhyme Pair | 4.5/10 | S1 (00:00) vs S10 (01:30) setup mismatch |
| 4 | Return Consistency | N/A | No returning setups present |
| 5 | Cluster Seams | N/A | No cluster seams present |
| 6 | Angle Arc & Deliberate Shocks | 6.0/10 | Jarring scale shift S2 to S3 (00:10, 00:20) |
| 7 | Screen Geometry | N/A | No returning setups present |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 0   🟡 MINOR: 1

## THE THREE THAT MATTER

1. **Rhyme Pair Failure (00:00 vs 01:30)**: Closing scene (S10) uses a new camera setup instead of returning to S1. *Fix:* Re-render S10 from Setup A's exact camera position and lens.
2. **Unanchored Scale Shift (00:20)**: Cutting from MCU (S2) to low-angle MWS (S3) creates a sudden jump in perspective. *Fix:* Insert an intermediate medium shot to smooth the scale transition.
3. **Outro Graphic Integration (01:40)**: Title card is appended directly to the main timeline. *Fix:* Separate non-narrative title card into distinct delivery asset.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration**: Aligning S10 to match S1 requires re-rendering the final clip from Setup A's perspective.
* **Fixable in Edit**: Scale jump between S2 and S3 can be softened via minor reframing/cropping in post at resolution cost.

## FLAGS FOR DOCUMENT CHECK

* Confirm if 10 unique camera setups without setup returns was the intended camera plan.
* Verify whether an opening/closing visual rhyme was specified in the narrative spec.

## OUT-OF-SCOPE FLAGS

* [CONTINUITY] Monolith surface texture varies between wide and close-up angles.
* [BACKGROUND] Mountain silhouette and twin sun positions drift across cuts.
* [LIGHTING] Key light angle on helmet visor shifts between frontal and profile setups.
