INPUT MODE: V
FILM: (not supplied)
RUNTIME: 02:59 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 18 · CUTS COUNTED: 17 · CUTS OFF GRID: none
NON-SCENE MATERIAL: none
PRESENCE STRING: -11-111111111111
LINES HEARD: 9 · "Orientation aligned. Horizon locked." (0:02), "Sling secured." (0:10), "Manual override ready." (0:13), "Disruptor... Horizon Station, maintain approach vector." (0:21), "Thrusters down." (0:41), "Guidance data is unreliable." (0:48), "Switching to manual attitude control." (0:50), "Horizon distance 142..." (1:07), "0.15 meters per second. Line is true." (1:36), "Hard lock engaged." (2:07)
SETUPS REGISTERED: 12 distinct camera positions
LOCKOFF HELD: 18 / 18 clips

## SETUP LEDGER

| Scene | In | Plan Letter | Observed Size / Angle / Lens / Position | Observed Letter | MATCH / NEAR / MISS | Anchor Position | In-Clip Movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 0:00 | — | EWS / Low Angle / Wide / Front-side profile, craft approaching station | A | — | Space station solar array top-right | 0 |
| S2 | 0:09 | — | MCU / Eye Level / Normal / Interior cockpit, pilot sitting left-center | B | — | Control console monitor screen bottom-right | 0 |
| S3 | 0:19 | — | WS / High Angle / Wide / Exterior orbit, craft approaching station docking hub | C | — | Station docking ring center-right | 0 |
| S4 | 0:29 | — | MS / Top-down axial / Normal / Tracking probe aligned with station hatch | D | — | Outer circular ring housing center | 0 |
| S5 | 0:39 | — | MCU / Eye Level / Normal / Two astronauts in cockpit with display UI foreground | E | — | UI telemetry panel right foreground | 0 |
| S6 | 0:49 | — | MS / Eye Level / Normal / Co-pilot left, pilot right operating console | F | — | Red toggle switch cluster center | 0 |
| S7 | 0:59 | — | ECU / Eye Level / Long / Extreme close-up of pilot eye through scope lens | G | — | Scope eyepiece housing right | 0 |
| S8 | 1:03 | — | MS / Eye Level / Long / Optical crosshair view of station | H | — | Station center core on crosshairs | 0 |
| S9 | 1:06 | — | ECU / Eye Level / Long / Pilot looking into scope (return to S7 position) | G | — | Scope eyepiece housing right | 0 |
| S10 | 1:09 | — | WS / Side-on / Normal / Exterior docking profile showing gap between craft & station | I | — | Station docking collar right edge | 0 |
| S11 | 1:19 | — | MCU / Eye Level / Normal / Co-pilot controlling joystick, station in window behind | J | — | Docking target window frame left | 0 |
| S12 | 1:29 | — | WS / Side-on / Normal / External profile of craft & station docking (return to S10) | I | — | Station docking collar right edge | 0 |
| S13 | 1:39 | — | CU / Low Angle / Wide / Close view of docking probe inserting into guide tube | K | — | Guide tube cylinder right center | 0 |
| S14 | 1:49 | — | WS / Side-on / Normal / External profile docking latch engagement (return to S10) | I | — | Station docking collar right edge | 0 |
| S15 | 1:59 | — | MCU / Eye Level / Normal / Co-pilot pulling locking lever (return to S11) | J | — | Docking target window frame left | 0 |
| S16 | 2:09 | — | MS / Eye Level / Normal / Cockpit crew view green status (return to S6 position) | F | — | Red toggle switch cluster center | 0 |
| S17 | 2:19 | — | WS / Eye Level / Wide / Airlock corridor, crew walking in through hatch | L | — | Circular airlock hatch frame left | 0 |
| S18 | 2:29 | — | MS / Eye Level / Wide / Crew standing inside airlock chamber | M | — | Center airlock hatch seams | 0 |
| S19 | 2:39 | — | CU / Eye Level / Normal / Radiation monitor mounted on wall, pilot resting | N | — | Radiation monitor box right foreground | 0 |
| S20 | 2:49 | — | WS / Eye Level / Wide / Symmetrical wide of crew resting in habitat pod | O | — | Porthole window top center | 0 |

## SETUP STRING

```
OBSERVED:   A B C D E F G H G I J I K I J F L M N O
PLAN:       (mode V — no spec provided)
DIFFERS AT: none

```

## PRESENCE STRING

`-11-1111111111111111`

## RHYME PAIR

|  | First frame (S1, 0:00) | Last frame (S20, 2:49) | Same? |
| --- | --- | --- | --- |
| Setup letter / size / angle / anchor position / the one variable | A / EWS / Low Angle / Station top-right / Spacecraft exterior | O / WS / Eye Level / Porthole top-center / Habitat interior crew | NO |

Verdict line: `PAIR FAILS` — S1 is an external orbital EWS while S20 is a interior wide shot of the crew resting in a habitat pod; no camera or subject rhyme exists.

## LOCKOFF VERIFICATION

All held.

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | — | N/A in Mode V |
| 2 | Lockoff Integrity | 10/10 | No camera drift, push, or reframing observed across all 20 clips |
| 3 | Rhyme Pair | 1/10 | 🔴 First frame (S1, 0:00) and last frame (S20, 2:49) share no camera setup, anchor, or framing scale |
| 4 | Return Consistency | 9/10 | 🟡 S10, S12, S14 (1:09, 1:29, 1:49) return to Setup I with identical scale and anchor placement; S6 and S16 (0:49, 2:09) return cleanly to Setup F |
| 5 | Cluster Seams | 10/10 | Seams across repeated setups (Setup I at 1:09/1:29 and Setup G at 0:59/1:06) maintain horizon and lockoff alignment |
| 6 | Angle Arc & Deliberate Shocks | 10/10 | Scale shifts between EWS, MCU, and ECU flow logically following the docking procedure |
| 7 | Screen Geometry | 9/10 | 🟡 S17 (2:19) airlock corridor geometry is stable; background object position shifts are physical movements rather than camera distortion |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **Rhyme Pair Failure (0:00 vs 2:49)**: Opening shot is an external space EWS, while the final frame is an internal wide shot of the hab module, breaking closing image structural symmetry.
* *Fix*: Match opening and closing frames by ending on an exterior EWS lockoff of the docked station.


2. **Setup Return Continuity across S10/S12/S14 (1:09, 1:29, 1:49)**: Minor lighting/shadow shift on the docking collar anchor between returns to Setup I.
* *Fix*: Match key light angle on exterior pass renders across Setup I cuts.


3. **Internal Perspective Jump S19 to S20 (2:39 to 2:49)**: Cut from CU wall monitor (Setup N) to wide habitat view (Setup O) introduces a minor camera axis shift.
* *Fix*: Re-align camera position in S19 to sit directly on the lateral axis of Setup O.



## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Rhyme Pair structural failure (2:49) | Append an exterior wide lockoff matching S1 to close the film | Low (Edit trim/add) |
| Minor key light inconsistency on Setup I returns (1:29) | Color grade / keylight match across external docking cuts | Low (Post grade) |

## FLAGS FOR DOCUMENT CHECK

* Is the opening/closing shot intended to rhyme externally, or is the habitat interior shot (S20) the designated ending?

## OUT-OF-SCOPE FLAGS

* **Biomechanics Lens**: Human walking gait inside airlock at 2:19 appears under 1g gravity despite prior microgravity orbital context.
* **Particles Lens**: Thruster gas plumes in vacuum exhibit slight atmospheric dispersion profiles at 0:04 and 1:12.

## REVIEWER NOTES

Assumed frame rate is 24 fps. The video demonstrates outstanding camera lockoff stability throughout all 20 individual scenes. Anchors remain completely fixed in-clip without breathing or drifting. The primary camera-specific failure is the lack of a functional Rhyme Pair between the first and last frames.
