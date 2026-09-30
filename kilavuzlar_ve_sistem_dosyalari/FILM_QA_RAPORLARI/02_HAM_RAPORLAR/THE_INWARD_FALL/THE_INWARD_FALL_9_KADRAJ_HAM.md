INPUT MODE: D
FILM: THE_INWARD_FALL
RUNTIME: 04:00
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0.0 s + (n−1) × 10.0 s
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: 11111111111111111111111-
LINES HEARD: none — room tone present
SETUPS REGISTERED: 9 distinct camera positions
LOCKOFF HELD: 24 / 24 clips

## SETUP LEDGER

S01 | 00:05 | A | WS / low angle / wide lens / rim floor track | A | MATCH | Curved railing on left | 0
S02 | 00:15 | B | CU / low-eye angle / normal lens / floor grate level | B | MATCH | Floor grate & tumbling pin | 0
S03 | 00:25 | C | MCU / high angle / normal lens / helmet visor | C | MATCH | Top helmet visor rim | 0
S04 | 00:35 | D | WS / eye angle / normal-wide / A-frame corridor | D | MATCH | Central A-frame truss ladder base | 0
S05 | 00:45 | B | CU / low angle / normal lens / boot on track | B | MATCH | Yellow track border plates | 0
S06 | 00:55 | D | MS / low angle / wide lens / corridor rail | D | MATCH | Tubular handrail on left | 0
S07 | 01:05 | C | MCU / high angle / normal lens / helmet visor | C | MATCH | Helmet visor & top ladder rung | 0
S08 | 01:15 | E | WS / worm's eye angle / wide lens / tunnel looking up | E | MATCH | Central circular ladder tunnel ring | 0
S09 | 01:25 | F | MS / high-dutch angle / normal lens / inside truss | F | MATCH | Square truss frame edges | 0
S10 | 01:35 | E | WS / top-down / wide lens / tunnel looking down | E | MATCH | Central ladder axis | 0
S11 | 01:45 | F | MCU / low angle / wide lens / under ladder | F | MATCH | Horizontal ladder rung | 0
S12 | 01:55 | C | EWS / high angle / wide lens / station exterior | ? | MISS | Outer ring & central hub | 0
S13 | 02:05 | G | MS / low-dutch angle / wide lens / truss side | G | MATCH | Yellow hazard stripe on strut | 0
S14 | 02:15 | F | MCU / low angle / normal lens / under ladder | F | MATCH | Guide hoop above helmet | 0
S15 | 02:25 | C | MCU / eye angle / normal lens / visor through rails | C | MATCH | Vertical rail bars | 0
S16 | 02:35 | G | WS / eye-high angle / wide lens / side hub | G | MATCH | Glowing spherical central hub | 0
S17 | 02:45 | F | ECU / side angle / normal lens / tether carabiner | ? | MISS | Orange tether & carabiner loop | 0
S18 | 02:55 | C | MS / low angle / wide lens / under ladder tether | ? | MISS | Dual diagonal tether lines | 0
S19 | 03:05 | G | ECU / top-down / normal lens / shears on cable | ? | MISS | Cutter blade & braided cable | 0
S20 | 03:15 | F | WS / high angle / wide lens / truss push-off | F | NEAR | Spherical hub on right | 0
S21 | 03:25 | E | MS / low angle / wide lens / under truss | E | NEAR | Overhead truss rings | 0
S22 | 03:35 | B | MCU / low angle / normal lens / chest harness | ? | MISS | Chest harness & rungs | 0
S23 | 03:45 | G | MCU / high angle / normal lens / visor close-up | C | MISS | Visor frame rim | 0
S24 | 03:55 | J | EWS / eye angle / wide lens / deep space capsule | J | MATCH | Central hub & drifting capsule | 0

## SETUP STRING

```
OBSERVED:   A B C D B D C E F E F ? G F C G ? ? ? F E ? C J
PLAN:       A B C D B D C E F E F C G F C G F E B G H G H J
DIFFERS AT: S12 (01:50), S17 (02:40), S18 (02:50), S19 (03:00), S22 (03:30), S23 (03:40)
```

## PRESENCE STRING

11111111111111111111111-

## RHYME PAIR

|  | First frame (S01, 00:05) | Last frame (S24, 03:55) | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | Setup A / WS / Low angle / Floor rim rail / Pin tumbling on floor | Setup J / EWS / Eye angle / Central station hub / Capsule drifting away in space | No |

`PAIR FAILS` — S01 (Setup A, low-angle rim floor) and S24 (Setup J, extreme wide shot in deep space) utilize entirely distinct camera setups, focal lengths, and frame anchors rather than sharing a matched camera frame.

## LOCKOFF VERIFICATION

All 24 clips held their lockoff with zero in-clip camera drift, re-centering, or breathing.

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 4/10 | 🔴 S12 (01:50), S17 (02:40), S18 (02:50), S19 (03:00), S22 (03:30), S23 (03:40) reframe away from plan string to unscripted close-ups/wide shots |
| 2 | Lockoff Integrity | 10/10 | All 24 clips maintain 100% rigid lockoff |
| 3 | Rhyme Pair | 2/10 | 🔴 Opening (S01, 00:05) and closing (S24, 03:55) frames fail to match setup, angle, or anchor position |
| 4 | Return Consistency | 6/10 | 🟠 S12 and S18 fail to return to Setup C; S23 returns to Setup C when Setup G was specified |
| 5 | Cluster Seams | N/A | No multi-clip cluster seams defined in SPEC |
| 6 | Angle Arc & Deliberate Shocks | 7/10 | 🟡 Unplanned ECU insert shocks at S17 (02:40) and S19 (03:00) break planned scale progression |
| 7 | Screen Geometry | 8/10 | 🟡 Minor wide-angle perspective distortion on structural struts in S13 (02:05) |

VERDICT: SETUP BROKEN

## THE THREE THAT MATTER

1. **Unscripted Setup Substitutions (S12, S17, S18, S19, S22, S23)**: Regenerate these six clips using the exact camera distance, angle, and anchor points specified by the setup letters in the SPEC.
2. **Rhyme Pair Mismatch between S01 and S24**: Re-render S24 from Setup A's precise camera setup (WS low-angle rim floor) to hold the opening frame geometry while showing the capsule departing.
3. **Unplanned ECU Inserts Disrupting Scale Arc (S17, S19)**: Replace ECU detail shots with the planned MS/WS ladder setups (F and G) to preserve the spatial scale transition during the central choice sequence.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration**: S12, S17, S18, S19, S22, and S23 cannot be fixed in post-production through cropping or stabilization because the underlying camera positions and field of view differ fundamentally from the SPEC setup sequence.
* **Fixable in Edit**: Minor wide-lens geometry curvature in S13 can be corrected using lens distortion correction filters in editing software at a 3–5% crop cost.

## FLAGS FOR DOCUMENT CHECK

* **S12 Setup Ambiguity**: The SPEC specifies Setup C (MCU High Angle Helmet Visor) for S12, but the narrative rhythm at the end of Part 1 suggests an exterior wide shot. Confirm if S12 was mislettered in the plan string.
* **Tether Action Detail Coverage**: The SPEC assigns Setup F (ladder climbing) and Setup G (truss bridge) to S17 and S19 during the tether-cutting sequence, omitting dedicated detail shots for hands and tools. Confirm whether a revised setup letter for tool ECUs should be added to the SPEC.

## OUT-OF-SCOPE FLAGS

* **CONTINUITY**: Tether cable color shifts between bright orange in S17 and darker woven cord in S19.
* **BACKGROUND**: Earth/star field rotation speed varies slightly across S08 and S10 cuts.
* **ACTION / EFFORT**: Astronaut hand placement on ladder rungs resets instantly between S10 (top-down) and S11 (low angle).
