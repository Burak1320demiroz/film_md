INPUT MODE: V
FILM: (not supplied)
RUNTIME: 04:00 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 25 · CUTS COUNTED: 24 · CUTS OFF GRID: none (mode V)
NON-SCENE MATERIAL: none
PRESENCE STRING: 1111111111111111111111-11
LINES HEARD: 02:14 - 02:20: "69... 48... transfer for quiet..."
SETUPS REGISTERED: 24 distinct camera positions
LOCKOFF HELD: 20 / 25 clips

## SETUP LEDGER

S01 | 00:00 | N/A | WS / eye / wide / front platform view | A | N/A | "BAY 14" railing left | 0
S02 | 00:10 | N/A | MCU / eye / normal / 3/4 right profile | B | N/A | Blue suit visor right | 0
S03 | 00:20 | N/A | WS / eye / wide / front platform view | A | N/A | "BAY 14" railing left | 0
S04 | 00:30 | N/A | MS / eye / normal / OTS behind blue suit | C | N/A | Blue helmet foreground right | 0
S05 | 00:40 | N/A | WS / eye / wide / side-on cage view | D | N/A | Elevator cage mesh left | 0
S06 | 00:50 | N/A | MS / low-eye / normal / OTS behind blue suit | E | N/A | Floor hatch rim center | 0
S07 | 01:00 | N/A | ECU / top-down / wide / above hatch panel | F | N/A | Square hatch panel frame | creep (starts 01:05)
S08 | 01:10 | N/A | EWS / high / wide / elevated top-down | G | N/A | Hangar floor grid center | 0
S09 | 01:20 | N/A | MS / eye / normal / OTS behind blue suit | H | N/A | Hatch opening left foreground | 0
S10 | 01:23 | N/A | MS / eye / normal / OTS behind blue suit | I | N/A | EN-664 wall door right | 0
S11 | 01:30 | N/A | MS / eye / normal / corridor side view | J | N/A | Wall conduit / railing left | 0
S12 | 01:40 | N/A | MCU / low / normal / OTS blue suit | K | N/A | Crate behind guard | 0
S13 | 01:50 | N/A | WS / eye / normal / side-on circular door | L | N/A | Circular portal frame left | 0
S14 | 02:00 | N/A | MCU / eye / normal / POV behind wire mesh | M | N/A | Wire mesh bar center | handheld float / breathing (starts 02:01)
S15 | 02:10 | N/A | WS / eye / wide / corridor center perspective | N | N/A | Bronze canister center background | 0
S16 | 02:20 | N/A | MCU / eye / normal / behind orange suit | O | N/A | Boat hull latch center | 0
S17 | 02:30 | N/A | ECU / top-down / normal / above lever console | P | N/A | Bronze lever slot center | push / creep (starts 02:32)
S18 | 02:40 | N/A | MS / eye / normal / OTS blue suit | Q | N/A | Console screen center | 0
S19 | 02:50 | N/A | ECU / top-down / wide / above canister lid | R | N/A | Circular dial knob center | drift / wobble (starts 02:53)
S20 | 03:00 | N/A | MCU / eye / normal / behind orange suit | S | N/A | Round hatch rim right | 0
S21 | 03:10 | N/A | MS / eye / normal / side profile | T | N/A | Large orange tank center | 0
S22 | 03:20 | N/A | MCU / eye / normal / side view astronaut | U | N/A | Light arm fixture right | 0
S23 | 03:30 | N/A | WS / low / wide / hangar floor looking up | V | N/A | Hovercraft stern & engines | tilt / pan up (starts 03:33)
S24 | 03:40 | N/A | MCU / eye / normal / side-profile alien | W | N/A | Porthole window frame right | 0
S25 | 03:50 | N/A | MS / eye / wide / corridor door view | X | N/A | Vault door right | 0

## SETUP STRING

```
OBSERVED:   ABACDEFGHIJKLMNOPQRSTUVWX
PLAN:       none (mode V)
DIFFERS AT: none (mode V)

```

## PRESENCE STRING

`1111111111111111111111-11`

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / WS / eye-level / "BAY 14" rail left / platform overview | X / MS / eye-level / corridor door right / two astronauts in gunfire | No |

PAIR FAILS — First and last frames use completely different camera setups, framing scales, locations, and anchor positions.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S07 | Locked off | Downward creep | 01:05 | DRIFT |
| S14 | Locked off | Handheld float / breathing | 02:01 | UNSTABLE |
| S17 | Locked off | Push-in creep | 02:32 | DRIFT |
| S19 | Locked off | Camera drift / wobble | 02:53 | DRIFT |
| S23 | Locked off | Slow pan/tilt up | 03:33 | UNPLANNED MOVE |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | N/A (Mode V — no written SPEC supplied) |
| 2 | Lockoff Integrity | 5/10 | 🔴 S07 @ 01:05 (downward creep), 🟠 S14 @ 02:01 (handheld float), 🟡 S17 @ 02:32 (push-in creep), 🟡 S19 @ 02:53 (frame wobble), 🟠 S23 @ 03:33 (unplanned pan/tilt tracking) |
| 3 | Rhyme Pair | 1/10 | 🔴 S01 @ 00:00 vs S25 @ 03:59 (opening WS platform does not rhyme with closing MS corridor door) |
| 4 | Return Consistency | 10/10 | Setup A (S01 @ 00:00 ↔ S03 @ 00:20) holds identical anchor position, lens perspective, and framing scale |
| 5 | Cluster Seams | 8/10 | 🟡 S09 ↔ S10 @ 01:23 (abrupt position shift across adjacent OTS shots) |
| 6 | Angle Arc & Deliberate Shocks | 6/10 | 🔴 S07 ↔ S08 @ 01:10 (unplanned 4-step scale shock ECU → EWS), 🟠 S16 ↔ S17 @ 02:30 (abrupt 2-step jump MCU → ECU top-down) |
| 7 | Screen Geometry | 8/10 | 🟡 S09 ↔ S10 @ 01:23 (subject screen direction flips without camera bridging) |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **S01 @ 00:00 vs S25 @ 03:59**: Closing frame fails to return to the opening setup (Setup A), breaking the bookend structure.
*Fix*: Regenerate S25 matching Setup A framing or add a final returning shot in post.
2. **S07 ↔ S08 @ 01:10**: Extreme 4-step scale jump from top-down ECU directly to EWS high angle.
*Fix*: Insert an intermediate MS/WS setup to bridge the scale shock.
3. **S23 @ 03:33**: Unplanned camera tracking (pan/tilt up) during a locked-off hovercraft shot.
*Fix*: Regenerate S23 with strict lockoff prompt constraints or stabilize in post.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration**: Camera setup mismatches (S01 vs S25 rhyme failure, S09/S10 orientation flip, S07/S08 scale shock) cannot be repositioned in post-production.
* **Fixable in Post**: Slight lockoff creeps (S07 @ 01:05, S17 @ 02:32, S19 @ 02:53) can be post-stabilized at the expense of slight border cropping and resolution loss.

## FLAGS FOR DOCUMENT CHECK

* Does the intended plan specify a bookend structure (Setup A return) for the final scene?
* Was S23 intended to be a dynamic tracking shot or a strict lockoff?

## OUT-OF-SCOPE FLAGS

* **CONTINUITY**: Alien shield geometry and suit helmet textures shift between S01 and S03.
* **LIGHTING**: Key light intensity on Bay 14 platform shifts between S01 and S03.
* **ACTION / EFFORT**: Shotgun recoil force does not propagate naturally to the guard's torso in S11.
