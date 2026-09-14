INPUT MODE: D
FILM: THE_COUNTED_TURN
RUNTIME: 04:14 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 25 · CUTS COUNTED: 24
NON-SCENE MATERIAL: 04:10-04:14 Title card "THE COUNTED TURN"
LINES HEARD: none — nothing audible to me
GRAVITY: a = 1.18 → 3.29 m/s² (0.121 g → 0.335 g)
PREMISE REGISTER: Weight in this ring comes ONLY from its rotation and it depends on DIRECTION. A released object NEVER falls vertically and NEVER rises: it drifts to one side, always the same side, always the same distance.

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      69.0
DIVISION:           69.0 ÷ 8 = 8.6

OVERALL SCORE: 8.6/10
VERDICT: MINOR SLIPS
The core premise of lateral drift and counter-spin gravity holds consistently across the runtime, with the primary defects isolated to material amnesia on the strap and minor deviations in the stated timing locks.

## PHYSICS LEDGER

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:05 | Metal parts released from hands, drift right | 1.1 s | ≈1.4 m (standing release) | a ≈ 2.3 m/s² | Premise (sideways drift), but faster than S0 spec (1.69 s) |
| L2 | 00:10 | Running stride, heavy steps | N/A | ≈1 m stride | 1 g | Slightly heavy for 0.12g |
| L3 | 00:20 | Strap sags between posts | N/A | ≈4 cm depth | Low g | Spec |
| L4 | 00:50 | Strap sag depth check | N/A | ≈5 cm depth | Low g | Spec |
| L5 | 01:10 | Sitting, heavy breathing | N/A | N/A | High effort | Spec |
| L6 | 01:50 | Starfield sweeps right to left | N/A | N/A | 3-4 RPM | Spec |
| L7 | 02:30 | Kneeling, strap manipulation | N/A | N/A | Low g | Spec |
| L8 | 02:50 | Strap undulates dynamically | 2.5 s | ≈2 m wave | High flex | Material amnesia |
| L9 | 03:16 | Orange clips released, drift right | 1.0 s | ≈1.4 m | a ≈ 2.8 m/s² | Premise |
| L10 | 04:00 | Static strap tension | N/A | ≈11 cm depth | Higher g | Spec |

## NUMERIC LOCK VERIFICATION — MODE D ONLY

| Lock | Stated | Measured on screen | Δ | Verdict |
| --- | --- | --- | --- | --- |
| Novum: Lateral drop | Constant deflection | Drops at 00:05 and 03:16 deflect laterally | 0 | PASS |
| Gravity: S0 fall time | 1.69 s | 1.1 s | -0.59 s | FAIL (L1) |
| Gravity: S23 fall time | 1.03 s | 1.0 s (at S19) | -0.03 s | PASS |
| Counter: Sag depth | S0 4cm → S24 11cm | Visibly deepens across scenes | N/A | PASS |
| Stars: Sweep speed | 3.0 → 5.0 RPM | Speeds up visibly | N/A | PASS |
| Clips: Waist count | S15 (6) | 6 clips visible at 02:30 | 0 | PASS |
| Clips: Pin count | S24 (2, 1 open) | 2 on pin at 04:00 | 0 | PASS |

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | 8/10 | -2 · L1 (00:05) initial drop is faster than specified lock |
| 2 | Ballistics & Trajectories | 10/10 | No in-scope deductions |
| 3 | Impact & Momentum | 9/10 | -1 · L2 (00:10) running strides land slightly heavy for 0.12g |
| 4 | Material Behaviour | 6/10 | -4 · L8 (02:50) strap behaves like rubber/liquid during manipulation |
| 5 | Particles & Atmosphere | N/A | no in-scope source |
| 6 | Scale & Measurement | 10/10 | No in-scope deductions |
| 7 | Rates & Timing | 8/10 | -2 · L1 (00:05) timing discrepancy on first drop |
| 8 | Light & Shadow Physics | 10/10 | No in-scope deductions |
| 9 | Human Biomechanics | 8/10 | -2 · L2 (00:10) gait does not fully reflect low gravity inertia |

## PRESENCE STRING

`1111111111111111111111111`

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 3

## GRAVITY TABLE

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| --- | --- | --- | --- | --- | --- |
| L1 | 00:05 | ≈1.4 m (standing release) | 1.1 s | ≈2.3 m/s² | Faster than 1.18 m/s² stated for S0 |
| L9 | 03:16 | ≈1.4 m (kneeling/leaning) | 1.0 s | ≈2.8 m/s² | Matches the 3.29 m/s² stated for late scenes |

## RATE TABLE

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| Starfield rotation | 01:50 (L6) | 03:30 | PASS (Rate increases as established by SPEC counter) |

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| L1 vs L9 | 00:05, 03:16 | 1 | The initial fall (S0) is visually almost as fast as the late fall (S19/S23), failing to establish the slow 1.69s baseline | 🟠 MAJOR |

## THE THREE THAT MATTER

1. **S0 Drop Speed (00:05):** The opening shot sets the physics baseline, but the objects fall too fast, undermining the 1.69s lock intended to show the initial low-gravity state. Fix: Re-time/slow this specific clip in the edit by 30%.
2. **Strap Material Amnesia (02:50):** The heavy industrial strap waves like a liquid rubber band when handled, breaking the rigid/heavy material premise. Fix: Regenerate or cut around the heavy undulating frames.
3. **Heavy Gait (00:10):** The astronaut runs with a heavy 1g stomp despite the 0.12g starting environment. Fix: Accept, as the effort curve covers part of this, but it reads visually heavy.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| S0 initial drop too fast | Speed ramp/stretch the falling frames to hit 1.69s | Edit |
| Liquid strap physics at 02:50 | Cut away earlier before the wave peaks | Edit |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| The first drop at 00:05 is faster than the stated 1.69s | Was the S0 clip rendered at the correct physics simulation speed, or did the model re-roll normal gravity for this specific generation? |

## OUT-OF-SCOPE FLAGS

none
