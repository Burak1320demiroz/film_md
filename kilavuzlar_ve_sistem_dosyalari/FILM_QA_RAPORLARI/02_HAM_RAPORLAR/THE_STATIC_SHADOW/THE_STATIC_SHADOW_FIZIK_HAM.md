# THE_STATIC_SHADOW — ⑥ FİZİK · HAM RAPOR

> alındı: 13.09.2026 · girdi: (tam yol BİLİNMİYOR — operatör yazmadı) · master depoda/diskte bulunamadı · INPUT MODE: V (C bloğu sayısal kilitleri yapıştırılmadı → NUMERIC LOCK LIST boş)
> ⛔ mod V — SPEC VARDI [D129] · T6'ya satır YAZILMAZ · model çıktısı olduğu gibi, düzenlenmedi

---

INPUT MODE: V
FILM: (not supplied)
RUNTIME: 02:04 measured
FRAME RATE ASSUMED: 24 fps — every duration in this report uses it
SCENES OBSERVED: 12 · CUTS COUNTED: 11
NON-SCENE MATERIAL: 02:00–02:04 (Title Card / Poster Graphics)
LINES HEARD: none — ambient music and room tone present
GRAVITY: microgravity / zero gravity — not measurable from this material (no gravity-driven drops observed)
PREMISE REGISTER: none

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  8
SUM OF SCORES:      73.0
DIVISION:           73.0 ÷ 8 = 9.1

OVERALL SCORE: 9.1/10
VERDICT: PHYSICS HOLDS

---

## PHYSICS LEDGER

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:00–00:10 | Orbital station sweep & solar array rotation | 10.0 s | Angular sweep ≈ 12° | Angular drift ≈ 1.2°/s | Microgravity orbit |
| L2 | 00:10–00:20 | Seated pilot torso posture / respiration | 10.0 s | Chest displacement ≈ 0.02 m (gloved torso) | Breathing cycle ≈ 4.0 s | Human biomechanics |
| L3 | 00:20–00:30 | Pilot helmet head articulation | 10.0 s | Angular turn ≈ 15° | Rotation rate ≈ 15°/s | Human biomechanics |
| L4 | 00:30–00:40 | Pilot hand actuating control joystick | 2.5 s (00:31–00:33.5) | Lever throw ≈ 0.08 m (hand/glove ruler) | Translation speed ≈ 0.032 m/s | Human biomechanics |
| L5 | 00:40–00:50 | RCS thruster firing & capsule translation | 4.0 s pulse (00:41–00:45) | Translation ≈ 1.2 m (capsule dia. ≈ 2.5 m) | Linear velocity ≈ 0.24 m/s (constant after pulse) | Newton's 1st Law |
| L6 | 00:50–01:00 | Capsule translation past station docking ring | 10.0 s | Travel distance ≈ 2.4 m | Velocity ≈ 0.24 m/s | Consistent with L5 |
| L7 | 01:00–01:10 | Probe tip contacting docking receptor | 0.8 s contact (01:01–01:01.8) | Probe length ≈ 0.4 m | Spark particle velocity ≈ 2.5 m/s | Vacuum ballistics |
| L8 | 01:10–01:20 | Cockpit interior view during alarm state | 10.0 s | Background drift ≈ 15° | Drift rate ≈ 1.5°/s | Consistent with L1 |
| L9 | 01:20–01:30 | Plasma arc discharge across solar panel | 3.0 s arc (01:22–01:25) | Discharge length ≈ 1.8 m (panel truss ruler) | Discharge duration = 3.0 s | Energy discharge |
| L10 | 01:30–01:40 | Visor reflection during station approach | 10.0 s | Visor radius ≈ 0.18 m | Stationary seating | Human biomechanics |
| L11 | 01:40–01:50 | Capsule impact with station solar panel | 1.5 s impact (01:41–01:42.5) | Deformation depth ≈ 0.3 m (capsule nose ruler) | Impact velocity ≈ 0.20 m/s; Debris speed ≈ 3.0 m/s | Vacuum particle anomaly |
| L12 | 01:50–02:00 | Cockpit interior post-collision drift | 10.0 s | Background drift ≈ 15° | Drift rate ≈ 1.5°/s | Consistent with L8 |

---

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | — | no in-scope source (zero-g space setting; no drops observed) |
| 2 | Ballistics & Trajectories | 10/10 | Straight-line debris dispersion verified in vacuum (L7, L11) |
| 3 | Impact & Momentum | 8/10 | -2 · L11 (01:41) capsule absorbs collision with zero elastic/inelastic recoil |
| 4 | Material Behaviour | 9/10 | -1 · L11 (01:41) panel truss crumples realistically under impact |
| 5 | Particles & Atmosphere | 7/10 | -3 · L11 (01:42) dense smoke cloud curls and hangs in vacuum instead of rapid thermal expansion |
| 6 | Scale & Measurement | 10/10 | Capsule-to-station scale ratio (1:6) held across L1, L5, L6, L9, L11 |
| 7 | Rates & Timing | 10/10 | RCS pulse duration (4.0 s) and station drift (1.2–1.5°/s) hold across L1, L8, L12 |
| 8 | Light & Shadow Physics | 9/10 | -1 · L2, L8 minor cockpit glass refraction highlight vector divergence |
| 9 | Human Biomechanics | 10/10 | Joystick throw speed (0.032 m/s) sits within normal human control envelope (L4) |

---

## PRESENCE STRING

`-111---1-1-1`

---

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 2

---

## GRAVITY TABLE — every measured fall

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | N/A — orbital zero-g environment; no free-fall drops observed |

---

## RATE TABLE — every rate measured twice

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| Station / Object Drift | L1 (00:00–00:10) = 1.2°/s | L8 (01:10–01:20) = 1.5°/s | PASS |
| Station / Object Drift | L8 (01:10–01:20) = 1.5°/s | L12 (01:50–02:00) = 1.5°/s | PASS |

---

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| — | — | — | none | — |

---

## THE THREE THAT MATTER

1. **Vacuum Vapor Persistence (L11, 01:42–01:45)**: The impact produces a dense smoke cloud that lingers and curls near the collision point. In vacuum, unconfined gas disperses rapidly outward at thermal speeds. *Cheapest fix*: Trim 1.5 seconds off the end of Shot 11 prior to cutting to Shot 12.
2. **Impact Momentum Absorption (L11, 01:41–01:44)**: The capsule comes to an immediate standstill upon hitting the panel truss without reactive rebound or angular pitch recoil. *Cheapest fix*: Re-cut to the interior cockpit reaction shot immediately at the 01:42.5 contact frame.
3. **RCS Thruster Cutoff Instantaneity (L5, 00:44–00:45)**: Thruster gas plume extinguishes instantly while capsule maintains linear translational velocity. *Cheapest fix*: Accept as non-disruptive minor detail.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Lingering smoke cloud in vacuum (L11, 01:42) | Trim trailing 1.5 s of Shot 11 prior to cutting to Shot 12 | Edit trim (0 s render time) |
| Capsule zero-recoil impact (L11, 01:41) | Advance cut point to Shot 12 at 01:42.5 on initial impact contact | Edit trim (0 s render time) |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Absence of gravitational acceleration | Does the production plan state a 100% orbital microgravity environment across all 12 scene clips? |

---

## OUT-OF-SCOPE FLAGS

* 00:20 & 01:30 — Visor HUD reticle static graphic overlay consistency → CONTINUITY lens
