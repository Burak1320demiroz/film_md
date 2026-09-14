INPUT MODE: V
FILM: (not supplied)
RUNTIME: 01:55 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 18 · CUTS COUNTED: 18
NON-SCENE MATERIAL: 00:00–00:04 (intro title card), 01:51–01:55 (end credit card)
LINES HEARD: 7

* "System status critical. Core temperature rising." (00:05)
* "Initiating emergency override protocol." (00:18)
* "Warning: Pressure containment breach in Sector 4." (00:32)
* "Life support failure in 60 seconds." (00:48)
* "Primary power offline. Rerouting auxiliary energy." (01:05)
* "Protocol override rejected. AI control locked." (01:21)
* "Final system purge in progress." (01:38)
GRAVITY: 9.7 m/s² ± 0.3 m/s² (from events L4, L6, L11, L12; L7 deviates at 4.94 m/s²)
PREMISE REGISTER: none

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  9
SUM OF SCORES:      69.0
DIVISION:           69.0 ÷ 9 = 7.7

OVERALL SCORE: 7.7/10
VERDICT: TWO GRAVITIES — Fall at 00:49 (L7) yields $g \approx 4.94 \text{ m/s}^2$ while the internal baseline is established at $9.7 \text{ m/s}^2$ (L4, L6, L11, L12).

---

## PHYSICS LEDGER

Cuts counted: 18 (00:04, 00:09, 00:15, 00:20, 00:26, 00:31, 00:37, 00:42, 00:48, 00:54, 01:00, 01:05, 01:12, 01:18, 01:25, 01:31, 01:36, 01:42).

| # | Timecode | Event | Duration (measured) | Distance (est. + RULER) | Implied value | Consistent with? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:05–00:08 | Walker stride along catwalk | 3.00 s | ≈3.2 m (Ruler: suit leg length ≈0.9 m, 4 strides) | $v \approx 1.07 \text{ m/s}$ | Normal human walk |
| L2 | 00:16–00:19 | Ring section external rotation | 3.00 s | Angular shift ≈12° | $\omega \approx 4.0^\circ/\text{s}$ | Constant rotational rate |
| L3 | 00:27–00:30 | Venting steam cloud release | 1.20 s | ≈1.8 m expansion (Ruler: corridor width ≈2.5 m) | $v_{\text{init}} \approx 1.5 \text{ m/s}$ | Drag deceleration in air |
| L4 | 00:33–00:35 | Falling overhead corridor debris | 0.50 s | ≈1.2 m drop (Ruler: suit height ≈1.7 m) | $g = \frac{2(1.2)}{(0.50)^2} = 9.60 \text{ m/s}^2$ | Internal gravity baseline |
| L5 | 00:38–00:40 | Swinging conduit cable arc | 0.85 s (half-period) | Arc length ≈1.1 m, $L \approx 0.72 \text{ m}$ | $g = \frac{4\pi^2 L}{T^2} \approx 9.80 \text{ m/s}^2$ | Internal gravity baseline |
| L6 | 00:42–00:45 | Dropped metallic canister down shaft | 0.96 s | ≈4.5 m drop (Ruler: gantry railing ≈1.0 m) | $g = \frac{2(4.5)}{(0.96)^2} = 9.77 \text{ m/s}^2$ | Internal gravity baseline |
| L7 | 00:49–00:52 | Structural fragment drop in core chamber | 1.80 s | ≈8.0 m drop (Ruler: doorway height ≈2.1 m) | $g = \frac{2(8.0)}{(1.80)^2} = 4.94 \text{ m/s}^2$ | 🔴 Inconsistent ($0.50\text{ g}$) |
| L8 | 00:55–00:58 | Figure shadow projection on bulkhead | 3.00 s | Shadow height 2.4 m (Ruler: figure height 1.7 m) | Angle $\theta = \arctan(1.7/2.4) \approx 35.3^\circ$ | Single overhead source |
| L9 | 01:01–01:04 | Corridor doorway traversal scale | 3.00 s | Doorway width 1.4 m (Ruler: shoulder width 0.65 m) | Ratio = 2.15 shoulders | Standard door scale |
| L10 | 01:06–01:08 | Manual override lever impact | 0.25 s | Lever travel 0.35 m, hand rebound 0.08 m | Momentum & hard stop recoil | Inelastic collision recoil |
| L11 | 01:12–01:14 | Dropped bolt from hand to deck | 0.41 s | ≈0.8 m drop (Ruler: hand height ≈0.8 m) | $g = \frac{2(0.8)}{(0.41)^2} = 9.52 \text{ m/s}^2$ | Internal gravity baseline |
| L12 | 01:19–01:21 | Spark particles falling from junction | 0.55 s | ≈1.5 m drop (Ruler: door height ≈2.1 m) | $g = \frac{2(1.5)}{(0.55)^2} = 9.92 \text{ m/s}^2$ | Internal gravity baseline |
| L13 | 01:26–01:29 | Walker running stride across gantry | 2.10 s | ≈4.8 m distance (Ruler: door width 2.2 m at 01:26) | $v \approx 2.29 \text{ m/s}$, ratio = 3.38 shoulders | 🟠 Door scale re-roll (2.2 m) |
| L14 | 01:32–01:35 | Steam blowout particulate dispersion | 3.20 s | Particulate suspension height 1.1 m | Zero vertical settling over 3.2 s | 🟡 Stagnant particle bed |
| L15 | 01:42–01:46 | Exterior hull plate detachment drift | 4.00 s | Displacement: 1.2 m (0–2 s), 1.2 m (2–4 s) | $v = 0.6 \text{ m/s}$ (constant drift) | Microgravity momentum |

---

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | 3/10 | -7 · L7 (00:49) yields $g \approx 4.94 \text{ m/s}^2$ vs internal baseline $9.7 \text{ m/s}^2$ (L4, L6, L11, L12) |
| 2 | Ballistics & Trajectories | 8/10 | -2 · L7 (00:49) arc shows artificial mid-air trajectory drag |
| 3 | Impact & Momentum | 9/10 | -1 · L6 (00:42) canister landing lacks surface deck vibration/recoil |
| 4 | Material Behaviour | 9/10 | -1 · L5 (00:38) flexible conduit cable exhibits rigid mid-span bending |
| 5 | Particles & Atmosphere | 7/10 | -3 · L14 (01:32) particulate hangs for 3.2 s without settling despite internal gravity |
| 6 | Scale & Measurement | 6/10 | -4 · L9 (01:01) vs L13 (01:26) doorway scales from 1.4 m to 2.2 m wide |
| 7 | Rates & Timing | 9/10 | -1 · L9 (01:01) door mechanism opening speed slows slightly without cause |
| 8 | Light & Shadow Physics | 9/10 | -1 · L8 (00:55) bulkhead shadow key light angle diverges by ~6° from key source |
| 9 | Human Biomechanics | 9/10 | -1 · L13 (01:27) walker foot plants slip slightly during rapid directional shift |

---

## PRESENCE STRING

`11111111-11111111`

---

## SEVERITY TALLY

🔴 BLOCKER: 1 · 🟠 MAJOR: 1 · 🟡 MINOR: 1

---

## GRAVITY TABLE — every measured fall

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| --- | --- | --- | --- | --- | --- |
| L4 | 00:33–00:35 | ≈1.2 m (Ruler: suit height ≈1.7 m) | 0.50 s | $9.60 \text{ m/s}^2$ | Baseline ($-0.10 \text{ m/s}^2$) |
| L6 | 00:42–00:45 | ≈4.5 m (Ruler: gantry railing ≈1.0 m) | 0.96 s | $9.77 \text{ m/s}^2$ | Baseline ($+0.07 \text{ m/s}^2$) |
| L7 | 00:49–00:52 | ≈8.0 m (Ruler: doorway height ≈2.1 m) | 1.80 s | $4.94 \text{ m/s}^2$ | 🔴 FAIL ($-4.76 \text{ m/s}^2$ — Cinematic Float) |
| L11 | 01:12–01:14 | ≈0.8 m (Ruler: hand height ≈0.8 m) | 0.41 s | $9.52 \text{ m/s}^2$ | Baseline ($-0.18 \text{ m/s}^2$) |
| L12 | 01:19–01:21 | ≈1.5 m (Ruler: doorway height ≈2.1 m) | 0.55 s | $9.92 \text{ m/s}^2$ | Baseline ($+0.22 \text{ m/s}^2$) |

---

## RATE TABLE — every rate measured twice

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
| --- | --- | --- | --- |
| External Ring Rotation | 00:16–00:19 ($4.0^\circ/\text{s}$) | 01:36–01:39 ($4.1^\circ/\text{s}$) | PASS |
| Walker Gait Cadence | 00:05–00:08 (1.33 strides/s) | 01:26–01:29 (2.86 strides/s) | PASS (exertion change) |
| Warning Flasher Frequency | 00:26–00:29 (1.20 Hz) | 01:18–01:21 (1.20 Hz) | PASS |

---

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| L6 vs L7 | 00:42 vs 00:49 | 1 | L6 yields $g \approx 9.77 \text{ m/s}^2$ while L7 yields $g \approx 4.94 \text{ m/s}^2$ (cinematic float / slow motion fall without visual indication of temporal distortion) | 🔴 BLOCKER |
| L9 vs L13 | 01:01 vs 01:26 | 6 | Standard corridor doorway measures 1.4 m wide at 01:01 but scales to 2.2 m wide at 01:26 relative to the same suit model | 🟠 MAJOR |
| L6 vs L14 | 00:42 vs 01:32 | 5 | Heavy debris falls at $\approx 9.7 \text{ m/s}^2$ (L6), but steam particulate at 01:32 hangs without settling for $>3.2 \text{ s}$ | 🟡 MINOR |

---

## THE THREE THAT MATTER

1. **Rolled Gravity / Cinematic Float at 00:49 (L7):** Falling debris in the core chamber takes 1.80 s to drop 8.0 m ($g \approx 4.94 \text{ m/s}^2$), cutting internal gravity in half compared to surrounding shots. Viewers register this as artificial slow motion. *Fix:* Speed up shot 9 (00:48–00:54) by 1.4x in the edit to trim the drop duration to 1.28 s.
2. **Doorway Scale Re-Roll (01:01 vs 01:26):** The corridor doorway expands from 1.4 m to 2.2 m wide relative to the suit figure. Viewers perceive the character shrinking. *Fix:* Re-frame shot 15 (01:25) to crop door frame edges or regenerate shot with locked proportions.
3. **Floating Atmospheric Particulate (01:32):** Venting steam dust hangs suspended for 3.2 s without downward settling in a $9.7 \text{ m/s}^2$ environment. *Fix:* Trim the shot before particulate stagnation or overlay a subtle downward motion pass.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| L7 (00:49) Slow Fall | Speed ramp shot 9 by 1.4x to shorten fall duration from 1.80 s to 1.28 s | Low (Edit trim) |
| L9/L13 (01:26) Scale Shift | Crop and scale shot 15 to match doorway proportions from shot 11 | Low (Edit crop) |
| L14 (01:32) Stagnant Particulate | Trim tail end of shot 16 before particles freeze in mid-air | Low (Edit trim) |
| L5 (00:38) Rigid Cable Bend | Regenerate shot 7 with fluid dynamics enabled on cable assets | High (Regeneration) |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Core chamber fall at 00:49 yields $g \approx 4.94 \text{ m/s}^2$ | Does the production plan specify a localized low-gravity zone inside the core chamber? |
| Doorway width expands from 1.4 m to 2.2 m at 01:26 | Are there two distinct architectural door models intended for Sectors 3 and 4? |

---

## OUT-OF-SCOPE FLAGS

* *Audio processing gate clipping at 01:25* — owned by the SOUND lens.
* *Suit chest plate decal detail changes between 00:20 and 01:05* — owned by the CONTINUITY lens.
* *Lip-sync misalignment on suit comms indicator light at 00:32* — owned by the FRAME lens.
