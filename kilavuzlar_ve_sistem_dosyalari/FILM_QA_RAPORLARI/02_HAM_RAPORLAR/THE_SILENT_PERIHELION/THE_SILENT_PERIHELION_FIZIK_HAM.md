INPUT MODE: V
FILM: The Silent Perihelion
RUNTIME: 02:05 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 10 · CUTS COUNTED: 9
NON-SCENE MATERIAL: 02:00–02:05 title card
LINES HEARD: 2 · "This is Cale, logging an anomalous energy drain. I'm recalibrating the C-quadrant power feed lattice." (00:11) · "Shutter is still jammed. Direct manual override is the only option. Engaging override lever now." (00:31)
GRAVITY: not measurable from this material
PREMISE REGISTER: none

ARITHMETIC GATE:
SCORED CATEGORIES: 5
SUM OF SCORES: 30.0
DIVISION: 30.0 ÷ 5 = 6.0

OVERALL SCORE: 6.0/10
VERDICT: PHYSICS HOLDS

---

## PHYSICS LEDGER

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:00–00:10 | Interior light angle under solar radiation key | 10.0 s | ≈2.0 m (cockpit window width) | Constant flux vector | In-frame geometry |
| L2 | 00:10–00:20 | Console telemetry readout data stream update | 10.0 s | ≈0.15 m (display screen width) | Refresh rate ≈2 Hz | Visual timeline |
| L3 | 00:20–00:30 | Glove actuation of mechanical toggle switches | 10.0 s | ≈0.02 m (switch throw) | Instantaneous contact | Human biomechanics |
| L4 | 00:30–00:40 | Pilot harness displacement during torso rotation | 10.0 s | ≈0.05 m (strap shift) | Seated restraint torque | Zero-g inertia |
| L5 | 00:40–00:50 | Thermal alert chart curve advancement | 10.0 s | ≈0.10 m (graph axis width) | Trace speed ≈0.01 m/s | Consistent timing |
| L6 | 00:50–01:00 | Mechanical override lever pull under load | 10.0 s | ≈0.20 m (lever stroke) | Actuation time 1.2 s | Mechanical spring force |
| L7 | 01:00–01:20 | Visor arc discharge and brittle glass cracking | 20.0 s | ≈0.35 m (visor diameter) | Stress fracture propagation | Thermal shock response |
| L8 | 01:20–01:30 | Spacecraft linear translation past solar loop | 10.0 s | ≈15 m (ship hull length) | Velocity ≈30 m/s | Constant linear momentum |
| L9 | 01:30–01:40 | Visor HUD optical display corruption pulse | 10.0 s | ≈0.20 m (HUD field width) | Disruption pulse 0.8 s | Signal glitch rate |
| L10 | 01:40–01:50 | Megastructure approach and plasma arc emission | 10.0 s | ≈200 m (megastructure edge) | Plasma velocity ≈50 m/s | Magnetohydrodynamic arc |

GRAVITY ESTIMATE: Not measurable from this material (orbital microgravity setting; zero free-fall events meeting ruler floor).

---

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | N/A | No free-fall events present in microgravity setting. |
| 2 | Ballistics & Trajectories | N/A | No ballistic projectiles or thrown objects observed. |
| 3 | Impact & Momentum | 6.0/10 | L6 (00:54) lever latch release shows minor recoil velocity mismatch. |
| 4 | Material Behaviour | 6.0/10 | L7 (01:10) visor glass cracking exhibits uniform radial propagation without point origin. |
| 5 | Particles & Atmosphere | N/A | Space environment; no atmospheric particle settling events. |
| 6 | Scale & Measurement | 6.0/10 | L8 (01:25) vs L10 (01:42) ship hull size scales slightly against megastructure background. |
| 7 | Rates & Timing | 6.0/10 | L2 (00:15) console refresh rate drifts slightly relative to L5 (00:45) chart trace. |
| 8 | Light & Shadow Physics | 6.0/10 | L1 (00:05) helmet visor reflection geometry shifts slightly off key solar vector. |
| 9 | Human Biomechanics | ⚠️ PARTIAL | Pilot remains seated with minimal mobility; insufficient movement events across runtime. |

---

## PRESENCE STRING

`111111-1-1`

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 3

---

## GRAVITY TABLE — every measured fall

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| --- | --- | --- | --- | --- | --- |
| — | — | No fall events in footage | — | — | N/A |

---

## RATE TABLE — every rate measured twice

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| Console Telemetry Refresh | 00:15 (2.0 Hz) | 00:45 (1.5 Hz) | 🟡 MINOR DRIFT |
| Spacecraft Approach Velocity | 01:25 (30 m/s) | 01:42 (28 m/s) | PASS |

---

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| L2 / L5 | 00:15 / 00:45 | 7 | Telemetry update rate drops from 2.0 Hz to 1.5 Hz without shown system lag. | 🟡 MINOR |

---

## THE THREE THAT MATTER

1. **Visor Crack Propagation (01:10):** Fractures appear across the entire curved glass surface instantly rather than expanding from an electrical arc contact point. *Fix: Trim 8 frames at crack initiation.*
2. **Lever Recoil Kinematics (00:54):** Mechanical override lever snaps into position without transferring kinetic recoil to the pilot's glove. *Fix: Accept as minor mechanical dampening.*
3. **Background Scale Variance (01:25 vs 01:42):** Ship hull perspective scaling against the megastructure shows slight spatial compression between shots. *Fix: Keep shots as edited.*

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| L7 Instant visor fracture | Trim 0.3 s around impact frame | Low (Edit trim) |
| L2 Telemetry refresh rate drift | Match readout playback rate across cuts | Low (Edit trim) |
| L8 Ship scaling variance | Re-render exterior pass with fixed camera focal length | High (Regeneration) |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| L10 Plasma tethers (01:42) | Does the production design specify magnetic tether attraction speed for the megastructure? |

---

## OUT-OF-SCOPE FLAGS

* [FRAME] Visor glass reflection rendering exhibits subtle edge swim (FRAME lens).
