INPUT MODE: V
FILM: LOW_POWER
RUNTIME: 04:15 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 6 · CUTS COUNTED: 28 · CUTS OFF GRID: 0 (mode V)
NON-SCENE MATERIAL: 00:00–00:04 (Title/Studio card display)
PRESENCE STRING: 111111
LINES HEARD: 14 lines total

* 00:12 "System diagnostics complete. Hull integrity at 84%."
* 00:22 "Can you hear me out there? Is anyone receiving this channel?"
* 00:38 "Proximity warning. Unidentified object approaching vector 4."
* 00:48 "I see it. Standard scan isn't picking up a registry."
* 01:05 "Rerouting secondary power to forward shields."
* 01:18 "Shield strength stabilizing at 62%."
* 01:31 "If anyone is monitoring this frequency, we have sustained heavy atmospheric drag."
* 01:52 "Pressure drop detected in airlock chamber B."
* 02:08 "Manual override engaged. Sealing bulkhead."
* 02:26 "Warning: Thermal threshold exceeded in thruster array."
* 02:44 "Hold on... I'm trying to equalize the pressure manually!"
* 03:02 "Thruster output failing. Preparing emergency landing sequence."
* 03:22 "Brace for impact!"
* 03:45 "Life support active. Main power offline."
SETUPS REGISTERED: 5 distinct camera positions
LOCKOFF HELD: 4 / 6 clips

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  6 (Category 1 Setup Fidelity takes N/A in Mode V)
SUM OF SCORES:      32.0
DIVISION:           32.0 ÷ 6 = 5.3

OVERALL SCORE: 5.3/10
VERDICT: RHYME BROKEN

---

## SETUP REGISTER

* **Setup A** (First seen S1, 00:04): MCU · Low Angle · Normal Lens (50mm feel) · Positioned directly in front of pilot console · **Anchor:** Top lip of HUD control panel (centered)
* **Setup B** (First seen S2, 00:35): WS · Eye Level · Wide Lens (24mm feel) · Positioned back near cockpit entrance facing main viewscreen · **Anchor:** Upper frame edge of viewscreen
* **Setup C** (First seen S3, 01:12): CU · Eye Level · Long/Tight Lens (85mm feel) · Positioned tight on pilot helmet · **Anchor:** Left visor clip hinge
* **Setup D** (First seen S4, 01:45): MS · High Angle · Normal-Wide Lens (35mm feel) · Positioned elevated in airlock corridor · **Anchor:** Archway door frame lintel
* **Setup E** (First seen S5, 02:20): MCU · Dutch Angle (~15° tilt) · Dynamic/Wide Lens (28mm feel) · Positioned tight side-on in vibrating cockpit · **Anchor:** Seat shoulder harness rail

---

## SETUP LEDGER

| Scene | In | Plan Letter | Observed Size / Angle / Lens / Position | Observed Letter | Match | Anchor Position | In-Clip Movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 00:04 | N/A | MCU / Low / Normal / Front console | Setup A | MATCH | Centered on lower frame | 0 (Held) |
| S2 | 00:35 | N/A | WS / Eye / Wide / Cockpit interior | Setup B | MATCH | Aligned top 10% frame | 0 (Held) |
| S3 | 01:12 | N/A | CU / Eye / Tight / Helmet close-up | Setup C | MATCH | Left third vertical line | 0 (Held) |
| S4 | 01:45 | N/A | MS / High / Normal-Wide / Airlock | Setup D | MATCH | Top horizontal threshold | 0 (Held) |
| S5 | 02:20 | N/A | MCU / Dutch / Dynamic / Side cabin | Setup E | MATCH | Right diagonal rail | Creep / push-in starts at 02:50 |
| S6 | 03:30 | N/A | MCU / Low-Dutch / Normal / Front console | Setup A' | NEAR | Shifted 12% lower-right | Drift / breathing starts at 03:55 |

---

## SETUP STRING

```
OBSERVED:   A B C D E A'
PLAN:       (not supplied — mode V)
DIFFERS AT: N/A (mode V)

```

---

## PRESENCE STRING

`111111`

---

## RHYME PAIR

| Axis | First Frame (00:05) | Last Frame (04:12) | Same? |
| --- | --- | --- | --- |
| Setup Letter | Setup A | Setup A' | No (Modified angle/anchor) |
| Shot Size | MCU | MCU | Yes |
| Camera Angle | Low Angle (Level horizon) | Low Angle with ~10° Dutch Tilt | No |
| Anchor Position | HUD Panel top lip centered at Y=0.72 | HUD Panel top lip shifted to Y=0.84, X=0.62 | No |
| Observed Variable | Clean interior, active console lights | Damaged cabin, shattered glass | Yes (Planned state change) |

Verdict line: `PAIR FAILS` — Closing frame fails to return to the exact camera position of Setup A, introducing an unplanned dutch tilt and shifting the anchor position by 12% across the frame.

---

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement Starts At | Verdict |
| --- | --- | --- | --- | --- |
| S1 | Lockoff | Held stationary | None | PASS |
| S2 | Lockoff | Held stationary | None | PASS |
| S3 | Lockoff | Held stationary | None | PASS |
| S4 | Lockoff | Held stationary | None | PASS |
| S5 | Lockoff | Unplanned creeping push-in | 02:50 | FAIL (Creeping Dolly) |
| S6 | Lockoff | Unplanned horizon drift & breathing | 03:55 | FAIL (Camera Breathing) |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V — no written setup plan supplied |
| 2 | Lockoff Integrity | 5/10 | Unplanned creep in S5 at 02:50; breathing/drift in S6 at 03:55 |
| 3 | Rhyme Pair | 3/10 | 🔴 BLOCKER: First (00:05) and last (04:12) frames fail setup match (A vs A') |
| 4 | Return Consistency | 6/10 | 🟠 MAJOR: Setup A return in S6 drops camera elevation and misaligns anchor |
| 5 | Cluster Seams | 6/10 | 🟡 MINOR: Seam transition across cut 02:10 shifts horizon plane |
| 6 | Angle Arc & Deliberate Shocks | 6/10 | 🟠 MAJOR: Unplanned dutch angle shift in S5 without established camera movement |
| 7 | Screen Geometry | 6/10 | 🟡 MINOR: Wide lens distortion in S2 bends straight bulkhead arch into curve |

---

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 2

---

## THE THREE THAT MATTER

1. **Rhyme Pair Mismatch (00:05 vs 04:12):** The opening and closing shots use different setups (Setup A vs Setup A'), causing the anchor object to jump down-right by 12% and introducing an unplanned dutch tilt.
* *Fix:* Re-render or crop/re-frame shot S6 (04:12) to match the level horizon and anchor position of S1 (00:05).


2. **Creeping Dolly in Locked-Off Clip (02:50):** Shot S5 begins as a lockoff but develops an unprompted 5% focal push-in over its final 10 seconds.
* *Fix:* Stabilize and scale-lock the frame in post, or trim the last 10 seconds of S5 before the cut.


3. **Anchor Drift on Setup Return (03:30):** The camera returning to Setup A in S6 sits lower than its original height in S1, making the cockpit environment appear physically altered.
* *Fix:* Position-match S6 to S1 using spatial transformation in post-production.



---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| S5 Creeping Push-In (02:50) | Post-stabilize frame and apply fixed crop ratio | Low (Post stabilization) |
| S6 Camera Breathing (03:55) | Lock frame transforms to eliminate breathing drift | Low (NLE lockoff keyframing) |
| S6 Setup A Anchor Misalignment | Digital re-framing and rotation correction to match S1 | Medium (Crop/scale resolution loss ~8%) |
| S6 Rhyme Pair Alignment | Re-render final frame with identical camera parameters to S1 | High (Re-generation required for clean match) |

---

## FLAGS FOR DOCUMENT CHECK

* **Setup E Dutch Angle (02:20):** Was the 15° dutch tilt in Scene 5 intentional to signal atmospheric descent, or a model-generated angle artifact?
* **Scene 6 Camera Elevation (03:30):** Did the production intend for the camera to sit lower in the post-crash scene to reflect a collapsed pilot seat, or was Setup A intended to hold fixed coordinates?

---

## OUT-OF-SCOPE FLAGS

* **Continuity Lens (03:30):** Console button layout pattern shifts position between S1 and S6.
* **Light Lens (01:45):** Key light direction flips 180 degrees between S3 and S4.
