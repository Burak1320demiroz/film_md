MEDIA: video played
INPUT MODE: V

FILM: (not supplied)

RUNTIME: 02:59 measured

FRAME RATE ASSUMED: 24 fps

GRID GIVEN: none (mode V)

SCENES OBSERVED: 20 · CUTS COUNTED: 19 · CUTS OFF GRID: none

NON-SCENE MATERIAL: none

PRESENCE STRING: `-1--111-1-1---111111`

LINES HEARD: 11

· 00:02 "Orientation aligned, horizon locked."

· 00:10 "Sling secured."

· 00:14 "Nav override ready."

· 00:21 "Vessel approach Horizon station, maintain approach vector."

· 00:31 "Approaching system threshold, autopilot tracking."

· 00:42 "Thruster two is down."

· 00:48 "Guidance data is unreliable."

· 00:51 "Switching to manual attitude control."

· 01:08 "Horizon distance locked, 42 meters."

· 01:36 "0.15 meters per second, line is true."

· 02:07 "Hard lock engaged."

ZONES REGISTERED: 5 · MEDIUM: vacuum / air mixed

LIGHT JUMPS: 1 · CLEAN CUTS: 18

---

## ZONE REGISTER

```
ZONE 1: Exterior Space (S1, S3, S4, S10, S12, S13, S14)
· sources: 1 (Sun key)
· key direction: 10 o'clock · high elevation
· key quality: hard solar
· shadow: absolute black · razor sharp edge
· temperature: neutral-cool white (~5600K)
· fill: none
· medium: vacuum — no haze, no bloom, no fill bounce
· change allowed: none

ZONE 2: Cockpit Interior (S2, S5, S6, S7, S9, S11, S15, S16)
· sources: 3 (Console displays, overhead ambient panels, status indicator)
· key direction: 2 o'clock · eye level
· key quality: soft diffused tech glow
· shadow: lifted dark teal/cyan
· temperature: cool cyan/blue (~6500K)
· fill: ambient display bounce
· medium: air — soft display bloom permitted
· change allowed: ambient shift to green alert at S16

ZONE 3: Scope View (S8)
· sources: 1 (Solar backlight through reticle)
· key direction: 12 o'clock
· key quality: blown optical highlight
· shadow: high contrast silhouette
· temperature: neutral white
· fill: optical flare
· medium: filtered optics
· change allowed: none

ZONE 4: Station Airlock & Corridor (S17, S18)
· sources: Overhead recessed strip panels
· key direction: 12 o'clock · top down
· key quality: soft architectural
· shadow: soft ground drop shadow
· temperature: cool white (~5000K) in S17 · warm bronze (~3500K) in S18
· fill: metallic wall bounce
· medium: air
· change allowed: zone shift between airlock chamber and corridor

ZONE 5: Crew Cabin (S19, S20)
· sources: 4 wall sconces
· key direction: 9 o'clock & 3 o'clock
· key quality: warm practical soft bulb
· shadow: lifted warm brown
· temperature: warm tungsten (~2700K)
· fill: upholstered interior bounce
· medium: air
· change allowed: none

```

---

## LIGHT LEDGER

S1 | 00:00 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | 0

S2 | 00:09 | Zone 2 | 2 o'clock · level | soft | lifted cyan | 6500K | 3/3 lit | mid | dark teal | 0

S3 | 00:19 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | 0

S4 | 00:29 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | thruster vapor bloom (vacuum flaw)

S5 | 00:39 | Zone 2 | 2 o'clock · level | soft | lifted cyan | 6500K | 4/4 lit | mid | dark teal | 0

S6 | 00:49 | Zone 2 | 2 o'clock · level | soft | lifted cyan | 6500K | 4/4 lit | mid | dark teal | 0

S7 | 00:59 | Zone 2 | 1 o'clock · level | soft | lifted cyan | 6500K | 2/2 lit | mid | dark teal | 0

S8 | 01:02 | Zone 3 | 12 o'clock · backlight | hard | deep black | 5600K | 1/1 lit | bright halo | reticle black | 0

S9 | 01:06 | Zone 2 | 1 o'clock · level | soft | lifted cyan | 6500K | 2/2 lit | mid | dark teal | 0

S10 | 01:09 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | 0

S11 | 01:19 | Zone 2 | 2 o'clock · level | soft | lifted cyan | 6500K | 3/3 lit | mid | dark teal | 0

S12 | 01:29 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | 0

S13 | 01:39 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | 0

S14 | 01:49 | Zone 1 | 10 o'clock · high | hard | abs black | 5600K | 0 practicals | dark | pitch black | 0

S15 | 01:59 | Zone 2 | 10 o'clock · high | soft | lifted cyan | 6200K | 3/3 lit | mid | dark teal | slight key angle shift

S16 | 02:09 | Zone 2 | 2 o'clock · level | soft | lifted green | 5200K green | 3/3 lit | mid-dark | dark green | abrupt green cast shift

S17 | 02:19 | Zone 4 | 12 o'clock · top | soft | lifted grey | 5000K | 6/6 lit | bright | neutral grey | 0

S18 | 02:29 | Zone 4 | 12 o'clock · top | soft | lifted bronze | 3500K | 8/8 lit | bright | warm grey | 0

S19 | 02:39 | Zone 5 | 9 o'clock · level | soft | lifted brown | 2700K | 2/2 lit | mid-dark | warm shadow | 0

S20 | 02:49 | Zone 5 | 9 o'clock · level | soft | lifted brown | 2700K | 4/4 lit | mid-dark | warm shadow | 0

---

## KEY DIRECTION STRING

```
OBSERVED:  0200221W10200002WW99
ZONES:     VVVVVVVXVVVVVVVVAAAA

```

---

## PRESENCE STRING

```
PRESENCE:  -1--111-1-1---111111

```

---

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| S15 (02:08) → S16 (02:09) | Zone 2 | Sudden green alert color cast across entire cockpit cabin | Mode V (Undeclared) | 🟠 Medium |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 7/10 | S15 (01:59) key shifts temporarily to 10 o'clock relative to S11/S16. |
| 2 | Shadow Quality & Fill | 7/10 | Shadow density remains stable within individual zones. |
| 3 | Colour Temperature | 6/10 | 🟠 S16 (02:09) abrupt green color cast shift without visual trigger. |
| 4 | Practical Sources | 7/10 | Practical monitor and console source counts maintain structural consistency. |
| 5 | Exposure at Cuts | 7/10 | Exposure levels hold across interior and exterior cut pairs. |
| 6 | In-Clip Stability | 7/10 | Exposure and key angles remain steady inside individual clips. |
| 7 | Zone Boundaries | — | Mode V — no written spec supplied. |
| 8 | Atmosphere Honesty | 5/10 | 🟠 S4 (00:29) thruster plume displays volumetric lighting scatter in vacuum environment. |

VERDICT: GRADEABLE DRIFT

## THE THREE THAT MATTER

1. **Abrupt Cockpit Green Cast Jump (02:09 · S16)**
*Fix:* Match S16 color grade wheels to the cyan/blue baseline tone of S11 and S15.
2. **Volumetric Plume Glow in Vacuum (00:29 · S4)**
*Fix:* Re-render S4 thrust particles without atmospheric bloom or volumetric light scattering.
3. **Key Angle Drift on Pilot Close-up (01:59 · S15)**
*Fix:* Match key light positioning in S15 to 2 o'clock key established in S11.

---

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Grade Fixable:** S16 green color tint shift (02:09) can be corrected in post color balance.
* **Requires Regeneration:** S4 (00:29) thruster plume volumetric lighting effect in vacuum space.

---

## FLAGS FOR DOCUMENT CHECK

* Is S16 intended to feature an active green hazard alert state in the production spec?

---

## OUT-OF-SCOPE FLAGS

* **PHYSICS:** Thruster vapor dispersion rate in S4 assumes atmospheric backpressure in orbital vacuum.
* **CONTINUITY:** Astronaut chest harness webbing buckle orientation flips between S2 and S5.
