INPUT MODE: D
FILM: THE_BENT_GRASS
RUNTIME: 02:16 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0 · 10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100 · 110 · 120 · 130
SCENES OBSERVED: 13 · CUTS COUNTED: 12 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 2:10-2:16 title card
PRESENCE STRING: 11111-111111-
LINES HEARD: none — room tone present
SETUPS REGISTERED: 12
LOCKOFF HELD: 13 / 13 clips

SCORED CATEGORIES:  7
SUM OF SCORES:      43.0
DIVISION:           43.0 ÷ 7 = 6.1

OVERALL SCORE: 6.1/10
VERDICT: SETUP BROKEN

## SETUP REGISTER

· A | CU | low | normal | front | anchor: the crushed patch of grass
· B | WS | eye | normal | front | anchor: the horizon line
· D | MS | eye | normal | front | anchor: the astronaut's torso
· E | EWS | eye | wide | side | anchor: the horizon line
· F | MS | eye | normal | front | anchor: kneeling astronaut
· G | WS | eye | normal | side | anchor: the silver path
· ? (S2) | WS | eye | normal | behind | anchor: the lander
· ? (S3) | CU | high | normal | front | anchor: the bundle of grass
· ? (S6) | MS | eye | normal | side | anchor: the astronaut's torso
· ? (S7) | WS | eye | normal | behind | anchor: the path
· ? (S9) | WS | eye | normal | side | anchor: the path
· ? (S11) | WS | eye | normal | front | anchor: the path

## SETUP LEDGER

S0 | 0:00 | A | CU / low / normal / front | A | MATCH | crushed grass patch | 0
S1 | 0:10 | B | WS / eye / normal / front | B | MATCH | horizon line | 0
S2 | 0:20 | A | WS / eye / normal / behind | ? | MISS | lander in background | 0
S3 | 0:30 | A | CU / high / normal / front | ? | MISS | grass bundle | 0
S4 | 0:40 | D | MS / eye / normal / front | D | MATCH | astronaut torso | 0
S5 | 0:50 | E | EWS / eye / wide / side | E | MATCH | horizon line | 0
S6 | 1:00 | D | MS / eye / normal / side | ? | MISS | astronaut torso | 0
S7 | 1:10 | E | WS / eye / normal / behind | ? | MISS | path leading to horizon | 0
S8 | 1:20 | F | MS / eye / normal / front | F | MATCH | kneeling astronaut | 0
S9 | 1:30 | F | WS / eye / normal / side | ? | MISS | path | 0
S10 | 1:40 | G | WS / eye / normal / side | G | MATCH | path | 0
S11 | 1:50 | G | WS / eye / normal / front | ? | MISS | path | 0
S12 | 2:00 | B | CU / low / normal / front | A | MISS | crushed grass patch | 0

## SETUP STRING

OBSERVED:   A B ? ? D E ? ? F ? G ? A
PLAN:       A B A A D E D E F F G G B A
DIFFERS AT: S2, S3, S6, S7, S9, S11, S12, and S13 (missing entirely)
Length of OBSERVED (13) differs from PLAN (14) due to the title card replacing S13's time slot.

## PRESENCE STRING

11111-111111-

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / CU / low / crushed grass / human boot | A / CU / low / crushed grass / creature foot | YES |

PAIR HOLDS — First frame (0:00) and last frame (2:00) perfectly share the "A" setup, with only the planned variable (the foot making the step) changed.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| all held |  |  |  |  |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 0/10 | -10 · S2 (0:20), S3 (0:30), S6 (1:00), S7 (1:10), S9 (1:30), S11 (1:50), S12 (2:00) misses, plus S13 missing |
| 2 | Lockoff Integrity | 10/10 | no in-scope source |
| 3 | Rhyme Pair | 10/10 | no in-scope source |
| 4 | Return Consistency | 3/10 | -7 · D returns from side not front S6 (1:00), E returns from behind not side S7 (1:10) |
| 5 | Cluster Seams | 0/10 | -10 · split broken at S2-S3 (0:20), S8-S9 (1:20), S10-S11 (1:40) |
| 6 | Angle Arc & Deliberate Shocks | 10/10 | no in-scope source |
| 7 | Screen Geometry | 10/10 | no in-scope source |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 0

## THE THREE THAT MATTER

1. 0:20-0:40 — S2 and S3 abandon the "A" setup entirely; S3 flips the angle from low to high (Pattern ②). Fix: Reprompt S2 and S3 enforcing the CU low angle lock.
2. 1:20-1:50 — Cluster seams S8-S9 and S10-S11 break completely; the camera shifts angles mid-scene, ruining the edit's structure. Fix: Regenerate the second halves (S9, S11) using the exact same framing parameters as the first halves.
3. 2:00 — S12 is completely overwritten by S13's content (Setup A instead of B) because the video dropped the 14th clip for the title card. Fix: Restore the missing 10s clip to fulfill the 140s grid before the card.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

**FIXABLE IN THE EDIT:**
None. A wrong setup cannot be moved in post.

**REQUIRES REGENERATION:**
Scenes 2, 3, 6, 7, 9, 11, and 12 must be regenerated to match their planned setups. S13 must be added to respect the 14-scene grid geometry.

## FLAGS FOR DOCUMENT CHECK

* The video runs 13 scenes instead of 14, condensing the final rhyme (S13's Setup A) into S12's time slot to make room for a 6-second title card not requested by the spec.

## OUT-OF-SCOPE FLAGS

* STORY: The final beat arrives 10 seconds early on the grid.
* CONTINUITY: The landing craft changes shape and orientation across the setups that feature it in the background.
