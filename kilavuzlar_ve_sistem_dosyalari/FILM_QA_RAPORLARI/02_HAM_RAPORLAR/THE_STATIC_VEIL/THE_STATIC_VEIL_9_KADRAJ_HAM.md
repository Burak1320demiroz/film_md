INPUT MODE: D
FILM: THE_STATIC_VEIL
RUNTIME: 02:05 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0 s + (n−1) × 10.0 s
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none
NON-SCENE MATERIAL: 02:00–02:05 (outro title card "THE STATIC VEIL")
PRESENCE STRING: -11111111111
LINES HEARD: none — room tone and ambient music present
SETUPS REGISTERED: 5 distinct camera positions
LOCKOFF HELD: 12 / 12 clips

SETUP REGISTER
· Setup A: EWS | low-to-eye angle | wide lens | front landscape facing crater, platform on right rail | anchor: steel rail base and beacon platform structure
· Setup B: [Planned wide/medium angle, replaced by Setup A in execution]
· Setup C: ECU | eye level | normal-long lens | front-facing direct close-up on visor | anchor: gold mirror circular visor rim
· Setup D: MCU | low angle | normal lens | front 3/4 low angle looking up at astronaut torso | anchor: horizontal steel rail at chest level
· Setup E: ECU | top-down / high angle | wide-normal lens | directly above circular housing socket | anchor: circular socket flange and locking notch
· Setup F: MCU/CU | side 3/4 angle | normal lens | side-on to platform mechanism and clamps | anchor: vertical tower strut / rail clamp joint

## SETUP LEDGER

| Scene | in | plan letter | observed size / angle / lens / position | observed letter | MATCH · NEAR · MISS | anchor position | in-clip movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S00 | 00:00 | A | EWS / low-eye / wide / front landscape | A | MATCH | platform structure at right rail | 0 |
| S01 | 00:10 | B | EWS / low-eye / wide / front landscape | A | MISS | platform structure at right rail | 0 |
| S02 | 00:20 | C | ECU / eye / long / front visor close-up | C | MATCH | gold visor circular frame | 0 |
| S03 | 00:30 | C | MCU / low / normal / front 3/4 low torso | D | MISS | horizontal rail at chest level | 0 |
| S04 | 00:40 | D | MCU / eye-3/4 / normal / side platform | F | MISS | platform side edge and tower | 0 |
| S05 | 00:50 | E | ECU / top-down / normal / directly above | E | MATCH | circular socket flange | 0 |
| S06 | 01:00 | D | MCU / low / normal / front 3/4 low torso | D | MATCH | steel rail post on right | 0 |
| S07 | 01:10 | C | CU / eye-3/4 / normal / side clamp joint | F | MISS | clamp joint on rail | 0 |
| S08 | 01:20 | C | MCU / low / normal / side-low kneeling | D | MISS | battery unlatch housing | 0 |
| S09 | 01:30 | D | MCU / low / normal / front 3/4 tower mount | D | MATCH | tower vertical strut | 0 |
| S10 | 01:40 | E | ECU / top-down / normal / directly above | E | MATCH | circular socket flange | 0 |
| S11 | 01:50 | A | EWS / low-eye / wide / front landscape | A | MATCH | platform structure at left rail (mirrored) | 0 |

## SETUP STRING

```
OBSERVED:   A A C D F E D F D D E A
PLAN:       A B C C D E D C C D E A
DIFFERS AT: S01, S03, S04, S07, S08
```

## PRESENCE STRING

`-11111111111`

## RHYME PAIR

|  | First frame (S00, 00:05) | Last frame (S11, 01:55) | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / EWS / low-eye / platform on frame-right / beacon unlit | A / EWS / low-eye / platform on frame-left / beacon lit amber | NO — anchor position horizontally mirrored |

VERDICT: PAIR FAILS — S11 horizontally mirrors the geometry of S00, placing the anchor platform on frame-left instead of frame-right.

## LOCKOFF VERIFICATION

All 12 clips held their camera position perfectly; no creep, drift, re-centering, or breathing observed.

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 3/10 | 🟠 S01 (00:10) silent reuse of Setup A instead of B; 🟠 S03 (00:30) replaced ECU visor C with MCU low angle D; 🟡 S04 (00:40) replaced low angle D with side MCU F; 🟠 S07 (01:10) replaced ECU visor C with side clamp MCU F; 🟠 S08 (01:20) replaced ECU visor C with low angle MCU D |
| 2 | Lockoff Integrity | 10/10 | none — all 12 clips locked off cleanly |
| 3 | Rhyme Pair | 4/10 | 🔴 S00 (00:05) vs S11 (01:55) anchor mirrored across frame axis (Pattern ⑦ / ⑨) |
| 4 | Return Consistency | 5/10 | 🟠 S11 (01:50) return to Setup A fails screen side geometry vs S00; 🟠 S07 (01:10) and S08 (01:20) returns to Setup C fail to restore visor ECU camera position |
| 5 | Cluster Seams | 6/10 | 🟠 Cluster S02–S03 (00:20–00:40) camera position jumps across seam (C → D); 🟠 Cluster S07–S08 (01:10–01:30) camera position jumps across seam (F → D) |
| 6 | Angle Arc & Deliberate Shocks | 8/10 | 🟡 Unplanned camera scale/angle jumps at S01→S02 and S03→S04 resulting from setup substitutions |
| 7 | Screen Geometry | 7/10 | 🟠 S11 (01:50) platform anchor inverted to frame-left relative to S00 frame-right orientation |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **S11 (01:50) Mirrored Setup / Rhyme Failure:** The final scene flips the orientation of the landscape, placing the beacon platform on the left side instead of the right as established in S00. *Fix: Regenerate S11 with explicit prompt constraint to keep platform anchor on frame-right.*
2. **S03, S07, S08 (00:30, 01:10, 01:20) Visor Setup Collapses:** Planned Setup C (ECU on visor) is repeatedly replaced by medium low-angle (D) or side angle (F) setups. *Fix: Regenerate S03, S07, S08 using strict framing prompts for ECU helmet visor.*
3. **Cluster Seam Jumps in S02–S03 & S07–S08:** Both declared two-clip clusters fail to hold camera position across their split seams. *Fix: Regenerate S03 and S08 with image-to-image anchor continuity from S02 and S07.*

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Wrong Setups (S01, S03, S04, S07, S08):** Cannot be corrected in post-production. Re-rendering/regeneration required.
* **S11 Mirrored Anchor:** A simple horizontal flip in NLE would fix the platform position, but will flip suit details/handedness. Full clip regeneration is recommended.
* **Lockoffs:** 100% held; no stabilization or cropping required.

## FLAGS FOR DOCUMENT CHECK

* **SPEC Setup B Definition:** Is Setup B intentionally identical to Setup A in lens/angle, or did the generator drop a distinct setup specification?
* **Cluster Intended Camera:** Confirm if Cluster S07–S08 was intended as ECU visor or MCU work area.

## OUT-OF-SCOPE FLAGS

* **CONTINUITY:** Astronaut's suit regolith staining level fluctuates non-monotonically between S03 and S04.
* **ACTION:** Battery unlatching gesture in S08 lacks physical resistance feedback.
* **LIGHTING:** Key light angle on the crater rim shifts slightly between S05 and S06.
