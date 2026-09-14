INPUT MODE: V

FILM: THE SILENT PERIHELION

RUNTIME: 02:04 measured

FRAME RATE ASSUMED: 24 fps

GRID GIVEN: none (mode V)

SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none

NON-SCENE MATERIAL: 02:00–02:04 (Title card / promotional poster graphic)

PRESENCE STRING: 11111111-1-1

LINES HEARD: 2 · "This is Cale, logging an anomalous energy drain. I'm recalibrating the C-quadrant power feed lattice." (00:11) · "Shutter is still jammed. Direct manual override is the only option. Engaging override lever now." (00:31)

SETUPS REGISTERED: 8 distinct camera positions

LOCKOFF HELD: 8 / 12 clips

ARITHMETIC GATE — write these three numbers BEFORE the score

SCORED CATEGORIES:  6

SUM OF SCORES:      51.0

DIVISION:           51.0 ÷ 6 = 8.5

OVERALL SCORE: 8.5/10

VERDICT: RHYME BROKEN

## SETUP LEDGER

S1 | 00:00 | - | MWS / eye-level 3/4 right / wide-normal / cockpit right interior | A | MATCH | starboard pillar & console lower rim | 0

S2 | 00:10 | - | MWS / eye-level 3/4 right / wide-normal / cockpit right interior | A | MATCH | starboard pillar & console lower rim | 0

S3 | 00:20 | - | CU / high angle 45° / normal-macro / upper console face | B | MATCH | upper dual rotary knobs | creep starting at 00:26

S4 | 00:30 | - | MS / low angle 3/4 left / normal / pilot seat front-left | C | MATCH | left vertical handrail | 0

S5 | 00:40 | - | CU / high angle 45° / normal-macro / lower console face | D | MATCH | TEMP SELECT dial top-left | 0

S6 | 00:50 | - | MS / low angle profile / normal / left of pilot seat | E | MATCH | override lever spring bracket | wobble starting at 00:54

S7 | 01:00 | - | ECU / eye-level frontal / tight portrait / directly in front of visor | F | MATCH | helmet visor outer circular frame | 0

S8 | 01:10 | - | ECU / eye-level frontal / tight portrait / directly in front of visor | F | MATCH | helmet visor outer circular frame | 0

S9 | 01:20 | - | EWS / eye-level space / wide / trailing shuttle craft in orbit | G | MATCH | monolith vertical edge right frame | trailing pan starting at 01:22

S10 | 01:30 | - | ECU / eye-level frontal / tight portrait / directly in front of visor | F | MATCH | helmet visor outer circular frame | 0

S11 | 01:40 | - | EWS / eye-level space / wide / facing megastructure face | H | MATCH | dark octahedron facet symmetry | push starting at 01:42

S12 | 01:50 | - | ECU / eye-level frontal / tight portrait / directly in front of visor | F | MATCH | helmet visor outer circular frame | 0

## SETUP STRING

```
OBSERVED:   AABCDEFGFHF
PLAN:       (not supplied — mode V)
DIFFERS AT: none (mode V)

```

## PRESENCE STRING

```
11111111-1-1

```

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / MWS / eye-level 3/4 right / starboard canopy pillar / open cockpit view | F / ECU / eye-level frontal / circular helmet visor rim / dark cockpit interior | NO |

Verdict line: `PAIR FAILS` — The film opens on a cockpit-wide environmental shot (Setup A) and closes on an extreme close-up of the pilot's helmet visor (Setup F), failing to return to its opening frame setup.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S3 | Locked off | Creep / subtle breathing | 00:26 | MINOR DRIFT |
| S6 | Locked off | Camera wobble / drift | 00:54 | MINOR DRIFT |
| S9 | Locked off | Trailing pan / drift | 01:22 | MINOR DRIFT |
| S11 | Locked off | Forward push / drift | 01:42 | MINOR DRIFT |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V — no written specification supplied |
| 2 | Lockoff Integrity | 8/10 | Unplanned drift/creep in S3 (00:26), S6 (00:54), S9 (01:22), S11 (01:42) |
| 3 | Rhyme Pair | 4/10 | S1 (00:00) and S12 (01:50) fail setup symmetry; film ends on Setup F instead of returning to Setup A |
| 4 | Return Consistency | 9/10 | Setup F returns consistently across S7, S8, S10, S12 with locked anchor geometry |
| 5 | Cluster Seams | 10/10 | S1–S2 seam holds camera anchor and angle perfectly across HUD overlay transition |
| 6 | Angle Arc & Deliberate Shocks | 10/10 | Clean scale progression (MWS → CU → MS → ECU → EWS) without chaotic unmotivated jump cuts |
| 7 | Screen Geometry | 10/10 | Anchor positions, screen direction, and horizon alignment remain strictly coherent across scenes |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 0   🟡 MINOR: 4

## THE THREE THAT MATTER

1. **01:50 (S12) — Failed Rhyme Pair**: The final scene ends on Setup F (ECU frontal visor) rather than returning to Setup A (MWS cockpit interior), breaking closing framing symmetry. Fix: Replace S12 with a return to Setup A showing the darkened cockpit with the pilot motionless in the seat.
2. **00:26 (S3) & 00:54 (S6) — Interior Lockoff Drift**: Camera creeps and wobbles during panel interaction and lever pull. Fix: Apply post-production software stabilization to lock down S3 and S6 frames.
3. **01:22 (S9) & 01:42 (S11) — Exterior Space Pan/Push Drift**: Unplanned drifting movement on external wide shots. Fix: Stabilize external frames in post-production to maintain lockoffs.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Fixable in Post**: The camera drift in S3, S6, S9, and S11 can be locked down via 2D image stabilization in NLE editing software with a minor 2–4% frame crop penalty.
* **Requires Regeneration**: Resolving the broken Rhyme Pair in S12 requires generating a new shot returning to Setup A (cockpit MWS) at 01:50–02:00 to match S1 framing.

## FLAGS FOR DOCUMENT CHECK

* Does the plan call for a circular bookend (Rhyme Pair) returning to Setup A at the finale, or was ending on the Setup F ECU blackout intentional?

## OUT-OF-SCOPE FLAGS

* **CONTINUITY**: Glove texture and suit harness details vary slightly between CU panel shots (S3, S5) and MS body shots (S4, S6).
* **FRAME LENS**: Red electrical arc effects in S7 (01:00) exhibit minor AI rendering flickering artifacts around the visor edge.
* **LIGHT LENS**: High-contrast red key light intensity shifts sharply between S6 (00:50) interior cockpit lighting and S7 (01:00) helmet close-up.
