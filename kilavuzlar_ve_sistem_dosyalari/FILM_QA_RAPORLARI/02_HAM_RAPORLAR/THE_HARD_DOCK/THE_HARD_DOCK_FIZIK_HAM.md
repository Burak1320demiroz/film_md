BASELINE: SELF-CONSISTENCY + PHYSICS
PREMISE REGISTER: none

---
INPUT MODE: D
FILM: THE_HARD_DOCK
FORMAT: YATAY
RUNTIME: 04:05 measured
SCENE COUNT: 24
CUTS COUNTED: 23

## SCORES SUMMARY

| Category | Score | Issues / Deductions |
| --- | --- | --- |
| 1. Gravity & Free Fall | N/A | Declared Absence: No gravity falls present (zero-g orbital vacuum) |
| 2. Ballistics & Trajectories | 8.5/10 | -1.5 · L12 (02:00): solar panel detachment trajectory without kickback |
| 3. Impact & Momentum | 8.0/10 | -2.0 · L12 (02:00): panel separation without station reaction force |
| 4. Material Behaviour | 9.0/10 | -1.0 · L10 (01:30): glove surface rigidity under force |
| 5. Particles & Atmosphere | N/A | Declared Absence: Space vacuum environment |
| 6. Scale & Measurement | 8.0/10 | -2.0 · L1 (00:00) vs L8 (01:10): portal to module ratio scale variance |
| 7. Rates & Timing | 8.0/10 | -2.0 · L1 (00:00) vs L5 (00:40): axial rotation rate slowdown from 0.10 to 0.08 rad/s |
| 8. Light & Shadow Physics | 9.0/10 | -1.0 · L5 (00:40): planetary key light falloff variance |
| 9. Human Biomechanics | N/A | Declared Absence: Seated controls only; no locomotion or free body dynamics |

---

## PHYSICS LEDGER

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:00–00:10 | Station axial rotation over planet | 10.0 s | ≈15 m dia (module) | ω ≈ 0.10 rad/s | Real physics |
| L2 | 00:10–00:20 | Astronaut seated at viewport | 10.0 s | ≈1.0 m cockpit width | Static inertia | Real physics |
| L3 | 00:20–00:30 | Astronaut head rotation | 10.0 s | ≈0.2 m head arc | Biomechanical speed | Real physics |
| L4 | 00:30–00:40 | Station drift seen through portal | 10.0 s | ≈20 m distance | v ≈ 0.5 m/s | Real physics |
| L5 | 00:40–00:50 | Wide station rotation over lava planet | 10.0 s | ≈30 m station span | ω ≈ 0.08 rad/s | Real physics |
| L6 | 00:50–01:00 | Capsule module orbital drift | 10.0 s | ≈10 m gap | v ≈ 0.2 m/s | Real physics |
| L7 | 01:00–01:10 | Frontal solar array orientation | 10.0 s | ≈12 m array span | Static alignment | Real physics |
| L8 | 01:10–01:20 | Module relative framing | 10.0 s | ≈15 m distance | Apparent size drift | Scale variance |
| L9 | 01:20–01:30 | Helmet posture adjustment | 10.0 s | ≈0.8 m seat width | Static mass | Real physics |
| L10 | 01:30–01:40 | Glove operating mechanical control lever | 10.0 s | ≈0.15 m pull distance | Lever resistance | Material rigid |
| L11 | 01:40–01:50 | Seated astronaut view | 10.0 s | ≈1.7 m adult height | Normal posture | Real physics |
| L12 | 02:00–02:10 | Solar panel debris separation | 10.0 s | ≈5 m panel length | v ≈ 0.4 m/s (no recoil) | Momentum slip |
| L13 | 02:10–02:20 | Top-down orbital view over planetary crust | 10.0 s | ≈100 km orbit height | Orbital translation | Real physics |
| L14 | 02:20–02:30 | Wide horizontal module translation | 10.0 s | ≈50 m span | v ≈ 0.3 m/s | Real physics |
| L15 | 02:30–02:40 | Capsule floating near hatch ring | 10.0 s | ≈8 m gap | Linear trajectory | Real physics |
| L16 | 02:40–02:50 | Rear view astronaut looking out hatch | 10.0 s | ≈1.5 m cockpit width | Static posture | Real physics |
| L17 | 02:50–03:00 | Frontal astronaut breathing in suit | 10.0 s | ≈0.6 m helmet dia | Normal chest excursion | Real physics |
| L18 | 03:00–03:10 | Control desk lever engagement | 10.0 s | ≈0.1 m travel | Spring tension | Real physics |
| L19 | 03:30–03:40 | Throttle lever pull | 10.0 s | ≈0.12 m travel | Manual leverage | Real physics |
| L20 | 03:50–04:05 | Station capture / final docking position | 15.0 s | ≈20 m distance | Zero-g trajectory | Real physics |

---

## PRESENCE STRING

`-111---11111----11-1-111`

---

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 2

---

## GRAVITY TABLE

No gravitational free-fall events observed (zero-gravity orbital vacuum).

---

## RATE TABLE

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| Station axial rotation | 00:00 (ω ≈ 0.10 rad/s) | 00:40 (ω ≈ 0.08 rad/s) | 🟡 MINOR DRIFT |

---

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| L1, L5 | 00:00, 00:40 | Cat 7 | Axial rotation slows down without thruster braking | 🟡 MINOR |
| L12 | 02:00 | Cat 3 | Panel detaches and drifts without opposing reaction force | 🟡 MINOR |

---

## THE THREE THAT MATTER

1. **Debris panel separation without recoil (02:00)**: Debris drifts away without visible mechanical impulse or body kickback.
2. **Rotation rate slowdown (00:00 vs 00:40)**: Unforced decay of station spin rate across shots in vacuum space.
3. **Apparent viewport scale drift (00:00 vs 01:10)**: Foreground portal rim changes proportion relative to background module width.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Rotation slowdown (00:40) | Speed-ramp shot 00:40 by ~1.25x to match 00:00 spin rate | Edit fix |
| Panel separation impulse (02:00) | Trim initial 0.5 s frame burst or regenerate separation impact | Trim / Regen |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Rotation rate changes between 00:00 and 00:40 | Is the station thruster system actively damping spin? |

---

## OUT-OF-SCOPE FLAGS

none
