INPUT MODE: V
FILM: LOW_POWER
RUNTIME: 04:15 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 6 · CUTS COUNTED: 28
NON-SCENE MATERIAL: 00:00–00:04 (Title/Studio card display)
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
GRAVITY: GRAVITY ESTIMATE 6.50 ± 2.37 m/s² (derived from unobstructed cabin free falls at 01:55 [8.87 m/s²] and 02:41 [4.13 m/s²])
PREMISE REGISTER: none

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  8 (Cat 2 Ballistics & Trajectories takes N/A)
SUM OF SCORES:      37.0
DIVISION:           37.0 ÷ 8 = 4.6
OVERALL SCORE: 4.6/10
VERDICT: TWO GRAVITIES — falls within the cabin imply two incompatible acceleration rates (8.87 m/s² vs 4.13 m/s²), alongside unaccelerated cinematic floating during atmospheric descent.

---

## PHYSICS LEDGER

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:15 | Cockpit dust particle drift | 4.20 s | ≈0.15 m (Ruler: Pilot helmet width ≈0.25 m) | 0.036 m/s linear drift | Cockpit air currents |
| L2 | 00:42 | Approaching external object | 5.00 s | ≈120 m (Ruler: Ship hull length ≈30 m) | 24.0 m/s relative speed | Vacuum linear motion |
| L3 | 01:08 | Console electrical spark ejection | 0.80 s | ≈0.40 m (Ruler: Control panel width ≈0.80 m) | High initial velocity | Local arc discharge |
| L4 | 01:34 | Cabin vibration amplitude | 6.00 s | ≈0.05 m displacement (Ruler: Seat width ≈0.50 m) | ~1.5 g oscillation (12 Hz) | Atmospheric re-entry |
| L5 | 01:55 | Unsecured canister falls to deck | 0.52 s | ≈1.20 m (Ruler: Pilot height ≈1.75 m) | $g = 2(1.20)/(0.52)^2 \approx 8.87\text{ m/s}^2$ | Cabin acceleration (0.90 g) |
| L6 | 02:10 | Bulkhead door closure travel | 1.40 s | ≈2.10 m (Ruler: Doorway height ≈2.10 m) | 1.50 m/s linear rate | Pneumatic door drive |
| L7 | 02:22 | Loose airlock debris release | 2.50 s | ≈3.00 m (Ruler: Bulkhead width ≈2.00 m) | 1.20 m/s constant velocity ($a \approx 0\text{ m/s}^2$) | Inconsistent: Cinematic float |
| L8 | 02:41 | Loose wrench drops to floor | 0.88 s | ≈1.60 m (Ruler: Seat back height ≈1.00 m) | $g = 2(1.60)/(0.88)^2 \approx 4.13\text{ m/s}^2$ | Inconsistent: Rolled gravity (0.42 g) |
| L9 | 02:58 | Console panel deformation | 0.30 s | ≈0.10 m flex (Ruler: Console depth ≈0.60 m) | Elastic rebound flex | Structural metal bending |
| L10 | 03:10 | Helmet visor inertia shift | 0.15 s | ≈0.20 m drop (Ruler: Visor height ≈0.18 m) | Rapid deceleration load | Biomechanical neck strain |
| L11 | 03:25 | Impact deceleration stop | 1.10 s | ≈15.0 m (Ruler: Cockpit section ≈6.0 m) | $a \approx 24.8\text{ m/s}^2$ (~2.53 g) | Hull crush zone absorption |
| L12 | 03:48 | Smoke vapor expansion | 8.00 s | ≈1.50 m (Ruler: Cabin width ≈2.50 m) | 0.18 m/s thermal spread | Cooling ambient air |

---

## NUMERIC LOCK VERIFICATION — MODE D ONLY

N/A — Run conducted in INPUT MODE V (no numeric lock list supplied).

---

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | 3/10 | 🔴 BLOCKER: L5 vs L8 gravity discrepancy (8.87 m/s² vs 4.13 m/s²); L7 zero acceleration drift |
| 2 | Ballistics & Trajectories | N/A | No ballistic projectiles launched or thrown in arc trajectories |
| 3 | Impact & Momentum | 5/10 | 🟠 MAJOR: L11 crash impact lacks proportional inertia transfer on loose console items |
| 4 | Material Behaviour | 7/10 | 🟡 MINOR: L9 console flex exhibits slight plastic rubberiness under stress |
| 5 | Particles & Atmosphere | 4/10 | 🔴 BLOCKER: L7 debris floats horizontally for 2.5s with zero gravity acceleration |
| 6 | Scale & Measurement | 6/10 | 🟡 MINOR: L2 external object apparent scale shifts relative to distant stars |
| 7 | Rates & Timing | 5/10 | 🟠 MAJOR: L6 door closing rate varies between cuts (1.4s at 02:10 vs 2.8s at 02:18) |
| 8 | Light & Shadow Physics | 4/10 | 🟠 MAJOR: L3 console sparks project dual contradictory shadow angles across pilot chest |
| 9 | Human Biomechanics | 3/10 | 🔴 BLOCKER: L10 pilot body exhibits zero forward inertia lean during 2.53 g impact deceleration |

---

## PRESENCE STRING

`111111`

---

## SEVERITY TALLY

🔴 BLOCKER: 3   🟠 MAJOR: 3   🟡 MINOR: 2

---

## GRAVITY TABLE — every measured fall

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| --- | --- | --- | --- | --- | --- |
| L5 | 01:55 | ≈1.20 m (Pilot height ≈1.75 m) | 0.52 s | 8.87 m/s² (0.90 g) | Baseline reference |
| L7 | 02:22 | ≈3.00 m (Bulkhead width ≈2.00 m) | 2.50 s | 0.00 m/s² (0.00 g) | -8.87 m/s² (Cinematic float drift) |
| L8 | 02:41 | ≈1.60 m (Seat back height ≈1.00 m) | 0.88 s | 4.13 m/s² (0.42 g) | -4.74 m/s² (Rolled gravity defect) |

---

## RATE TABLE — every rate measured twice

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| Bulkhead Door Closure Rate | 02:10 (1.50 m/s over 1.40s) | 02:18 (0.75 m/s over 2.80s) | FAIL (2x rate reduction) |
| Alarm Beacon Flashing Rate | 00:38 (1.20 Hz / 20 frames) | 01:45 (1.20 Hz / 20 frames) | PASS |

---

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| L5 vs L8 | 01:55 / 02:41 | 1 | Free-fall acceleration in L5 implies g = 8.87 m/s², while L8 implies g = 4.13 m/s² | 🔴 BLOCKER |
| L5 vs L7 | 01:55 / 02:22 | 1, 5 | L5 establishes active vertical gravity, whereas L7 debris floats in a straight horizontal line for 2.5s with zero downward acceleration | 🔴 BLOCKER |
| L6 (Cut 1 vs Cut 2) | 02:10 / 02:18 | 7 | Pneumatic bulkhead door closes at 1.50 m/s in shot 1, then slows to 0.75 m/s in shot 2 | 🟠 MAJOR |

---

## THE THREE THAT MATTER

1. **Rolled Gravity on Falling Objects (01:55 vs 02:41):** The canister at 01:55 drops sharply ($g = 8.87\text{ m/s}^2$), while the wrench at 02:41 drifts downward in slow motion ($g = 4.13\text{ m/s}^2$). Viewers instantly feel the inconsistent weight of cabin props.
* *Cheapest Fix:* Speed up the 02:41 shot by 1.47x in the edit to match the initial fall acceleration.


2. **Cinematic Debris Float (02:22):** Debris released in the airlock travels horizontally for 2.5 seconds without dropping a single centimeter, violating the downward vector established in adjacent shots.
* *Cheapest Fix:* Trim the middle 1.8 seconds of the clip or re-cut around the floating phase.


3. **Inertial Disconnect During Impact (03:25):** The cockpit undergoes a violent ~2.5 g deceleration, but the pilot's torso remains rigid without leaning forward into the harness.
* *Cheapest Fix:* Regenerate the pilot shot with appropriate forward biomechanical momentum.



---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| L8 Wrench Fall Acceleration | Speed up clip by 1.47x to bring implied gravity from 4.13 m/s² to 8.87 m/s² | Low (Edit trim/speed adjustment) |
| L7 Floating Airlock Debris | Re-cut shot to eliminate the 2.5s unaccelerated horizontal drift phase | Low (Edit cut) |
| L6 Door Closure Rate Drift | Trim second shot of bulkhead door to match 1.50 m/s speed from 02:10 | Low (Edit trim) |
| L10 Pilot Biomechanics at Impact | Regenerate clip to introduce forward body inertia under 2.5 g crash deceleration | High (Re-generation required) |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Falls at 01:55 and 02:41 yield g = 8.87 m/s² and g = 4.13 m/s² | Does the ship's artificial gravity system experience a planned, document-specified power drain/fluctuating spec? |
| Bulkhead door speed changes from 1.50 m/s to 0.75 m/s between shots | Was the bulkhead door intended to stall halfway through its mechanical cycle? |

---

## OUT-OF-SCOPE FLAGS

* **Frame Lens (02:45):** Minor surface texture warping on the control panel during violent cockpit shaking.
* **Sound Lens (01:12):** Audio room tone drops out for 3 frames across cut 01:12.
