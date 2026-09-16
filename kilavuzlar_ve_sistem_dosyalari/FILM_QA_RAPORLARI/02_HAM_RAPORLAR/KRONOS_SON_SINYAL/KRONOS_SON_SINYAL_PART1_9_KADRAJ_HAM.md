INPUT MODE: V
FILM: KRONOS: SON SİNYAL
RUNTIME: 04:00 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
SETUPS REGISTERED: 24 distinct camera positions
LOCKOFF HELD: 11 / 24 clips

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S1 | Locked off | Pan right | 00:02 | DRIFT |
| S2 | Locked off | Breathing / drift | 00:13 | DRIFT |
| S5 | Locked off | Breathing | 00:43 | DRIFT |
| S6 | Locked off | Re-centre right | 00:52 | RE-CENTRE |
| S7 | Locked off | Push-in / re-centre | 01:03 | PUSH |
| S9 | Locked off | Truck right | 01:23 | DRIFT |
| S11 | Locked off | Tilt down / re-centre | 01:43 | RE-CENTRE |
| S12 | Locked off | Tilt left | 01:53 | DRIFT |
| S14 | Locked off | Creep forward | 02:12 | CREEP |
| S16 | Locked off | Track back / re-centre | 02:33 | RE-CENTRE |
| S18 | Locked off | Breathing | 02:54 | DRIFT |
| S22 | Locked off | Pan right | 03:37 | PAN |
| S24 | Locked off | Push-in | 03:52 | PUSH |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V run (no spec supplied) |
| 2 | Lockoff Integrity | 5/10 | Unplanned movement/drift in 13 clips (S1 00:02, S2 00:13, S5 00:43, S6 00:52, S7 01:03, S9 01:23, S11 01:43, S12 01:53, S14 02:12, S16 02:33, S18 02:54, S22 03:37, S24 03:52) 🟠 |
| 3 | Rhyme Pair | 1/10 | Opening frame S1 (exterior WS) and closing frame S24 (interior MS) share no setup or scale alignment 🔴 |
| 4 | Return Consistency | N/A | No setup letters repeat across the 24 scenes |
| 5 | Cluster Seams | N/A | No split-shot clusters present in footage |
| 6 | Angle Arc & Deliberate Shocks | 6/10 | Abrupt multi-step scale jumps across cuts without setup transition (S1->S2, S8->S9, S12->S14) 🟡 |
| 7 | Screen Geometry | N/A | No setup returns exist to measure anchor drift |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **00:00 vs 03:59 — Unrhymed Opening and Closing Frames**: Opening shot is a wide orbital exterior while closing shot is an interior cabin view through a portal. *Fix*: Regenerate either S1 or S24 so both share identical camera setup, scale, and anchor framing.
2. **00:02 / 01:03 / 01:43 / 02:33 — Widespread Lockoff Drift and Re-centering**: 13 out of 24 clips exhibit camera creep, panning, or re-centering instead of holding static lockoffs. *Fix*: Apply 2D digital stabilization in post or re-render affected clips with fixed camera keyframes.
3. **01:20 (S8->S9) & 01:50 (S12->S14) — Unannounced Extreme Scale Jumps**: Direct cuts between ECU UI details and WS exterior space views create jarring scale shocks. *Fix*: Insert intermediate MS transition shots in edit.
