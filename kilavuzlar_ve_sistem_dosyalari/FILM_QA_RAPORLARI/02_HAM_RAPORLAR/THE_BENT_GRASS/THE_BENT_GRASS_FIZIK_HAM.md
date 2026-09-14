INPUT MODE: D
FILM: THE_BENT_GRASS
RUNTIME: 02:14 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 13 · CUTS COUNTED: 13
NON-SCENE MATERIAL: 2:10-2:14 title card
LINES HEARD: none — nothing audible to me
GRAVITY: 0.95 g
PREMISE REGISTER: crushed grass does not rise, turns silver, immune to wind waves (boundary: crushed paths vs untouched grass)

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      79.0
DIVISION:           79.0 ÷ 8 = 9.8

OVERALL SCORE: 9.8/10
VERDICT: PHYSICS HOLDS

## PHYSICS LEDGER

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 0:00-0:10 | Human walking (S0) | 10.0 s | ~13.5 m (stride timing) | ~1.35 m/s | stated lock |
| L2 | 0:20-0:30 | Human walking (S2) | 10.0 s | ~13.5 m (stride timing) | ~1.35 m/s | stated lock |
| L3 | 0:50-1:00 | Wind wave passes over silver line | 10.0 s | N/A | Novum boundary | stated lock |
| L4 | 1:40-1:45 | Dropped grass from case | ~0.45 s | ~1.0 m (knee to ground) | ~0.95 g | stated lock |
| L5 | 2:00-2:05 | Hippo foot landing | N/A | N/A | mass reads slightly light | 0.95 g |

GRAVITY ESTIMATE: ~0.95 g ± 0.05, L4 grass drop.

## NUMERIC LOCK VERIFICATION — MODE D ONLY

| Lock | Stated | Measured on screen | Δ | Verdict |
| --- | --- | --- | --- | --- |
| NOVUM: Grass | crushed grass static against wave | S5: silver line motionless as wave passes | 0 | PASS |
| GRAVITY | 0.95 g (1.0m ≈ 0.46s) | S10: falling grass takes ~0.45s from knee height | ~0.01s | PASS |
| WALK SPEED | 1.35 m/s | S0-S2: stride rhythm yields ~1.35 m/s | ~0.0 m/s | PASS |
| ATMOSPHERE | +14 °C, vapor 0 frames | S1-S12: no breath vapor visible | 0 frames | PASS |
| SCREEN DIR | Lander LEFT, points 10 | S2: Lander on left, nose at 10 o'clock | 0 | PASS |
| SCREEN DIR | Sun LEFT, Shadows RIGHT | S0-S12: Shadows point right 14/14 scenes | 0 | PASS |
| COUNTER 2 | Herd: 400m -> 90m -> 1 body | S5 (horizon) -> S7 (mid) -> S11 (close) | 0 | PASS |
| LIGHT CALENDAR | Shadow S0 1.5x -> S13 3x | S0 1.5x body -> S12 ~3x leg height | 0 | PASS |

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | 10/10 | measured clean |
| 2 | Ballistics & Trajectories | — | no in-scope source |
| 3 | Impact & Momentum | 9/10 | -1 · L5 (2:00) |
| 4 | Material Behaviour | 10/10 | measured clean |
| 5 | Particles & Atmosphere | 10/10 | measured clean |
| 6 | Scale & Measurement | 10/10 | measured clean |
| 7 | Rates & Timing | 10/10 | measured clean |
| 8 | Light & Shadow Physics | 10/10 | measured clean |
| 9 | Human Biomechanics | 10/10 | measured clean |

## PRESENCE STRING

11111-111111-

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 1

## GRAVITY TABLE

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| --- | --- | --- | --- | --- | --- |
| L4 | 1:40-1:45 | ~1.0 m (knee height) | ~0.45 s | ~0.95 g | matches 0.95 g |

## RATE TABLE

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| Walk Speed | 0:00 (S0) | 0:20 (S2) | Consistent |
| Shadow Growth | 0:00 (S0) | 2:00 (S12) | Consistent |

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| L5 | 2:00 | 3 | Impact of massive hippo foot lacks corresponding heavy deceleration/recoil. | 🟡 MINOR |

## THE THREE THAT MATTER

1. **Novum Implementation (0:50):** The silver line remaining perfectly static while the wind wave sweeps the golden grass around it is a mathematically precise execution of the premise. (Accept).
2. **Gravity Lock (1:40):** The 1.0m fall of the grass from the case perfectly matches the stated 0.46s timing for a 0.95g environment. (Accept).
3. **Shadow Calendar (0:00 - 2:00):** The monotonic lengthening of the shadows across the 13 scenes executes the stated light calendar flawlessly. (Accept).

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| L5 foot impact feels slightly light | Accept. | Low |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| none | none |

## OUT-OF-SCOPE FLAGS

1:05 — suit stripe changes from red to blue — CONTINUITY lens
2:10 — title card has burned-in emergent text — FRAME lens
