# THE_STATIC_SHADOW — ⑪ IŞIK · HAM RAPOR

> alındı: 13.09.2026 · girdi: (tam yol BİLİNMİYOR — operatör yazmadı) · master depoda/diskte bulunamadı · INPUT MODE: V
> ⛔ ⑪ MOD V'DE GEÇERSİZ, tekrar değil [D190] — KARANTİNA: T11'e satır yok, ders/sipariş üretmez · model çıktısı olduğu gibi, düzenlenmedi

---

INPUT MODE: V
FILM: The Static Shadow
RUNTIME: 02:04 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none (mode V)
NON-SCENE MATERIAL: 01:59–02:04 title card ("THE STATIC SHADOW")
PRESENCE STRING: -111---1-1-1
LINES HEARD: none — nothing audible to me
ZONES REGISTERED: 2 · MEDIUM: vacuum (exterior) / air (interior)
LIGHT JUMPS: 4 · CLEAN CUTS: 7

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  7
SUM OF SCORES:      47.0
DIVISION:           47.0 ÷ 7 = 6.7

OVERALL SCORE: 6.7/10
VERDICT: GRADEABLE DRIFT

---

## ⛔ STEP 0 — THE ZONE REGISTER

```
ZONE REGISTER
· zone            Zone A: Exterior Space [S1, S5, S6, S7, S9, S11]
· sources         1 main distant star (Sun)
· key direction   10 o'clock to 11 o'clock (top-left elevation)
· key quality     hard specular
· shadow          absolute black (vacuum)
· temperature     neutral / cool sunlight (5500K–6000K)
· fill            none / minimal metal surface bounce
· medium          vacuum (no haze, no bloom, no dust scattering)
· change allowed  N/A (mode V)

· zone            Zone B: Cockpit Interior [S2, S3, S4, S8, S10, S12]
· sources         Canopy window sunlight, console displays, overhead cabin practicals
· key direction   11 o'clock (front window key) + 9 o'clock / top ambient
· key quality     hard direct sun + soft interior console fill
· shadow          dark / slightly lifted interior ambient
· temperature     mixed (warm white 2700K console, red emergency overlay S8, green LED S12)
· fill            console screen glow & canopy frame bounce
· medium          air (pressurized cabin)
· change allowed  N/A (mode V)

```

---

## LIGHT LEDGER

S1 | 00:00–00:09 | Zone A | 0 (10 o'clock) | hard | absolute black | neutral | 1/1 (Sun) | mid | black | 0

S2 | 00:10–00:19 | Zone B | E (11 o'clock) | hard/soft | lifted | neutral warm | 2/2 (Sun, panels) | mid | dark grey | 0

S3 | 00:20–00:29 | Zone B | T (top diffuse) | soft | lifted | warm white | 2/2 (Console, HUD) | bright | dark grey | 0

S4 | 00:30–00:39 | Zone B | 0 (10 o'clock) | hard/soft | lifted | warm white | 2/2 (Window, console) | bright | dark grey | 0

S5 | 00:40–00:49 | Zone A | E (11 o'clock) | hard | absolute black | neutral | 1/1 (Sun) | mid | black | 0

S6 | 00:50–00:59 | Zone A | 0 (10 o'clock) | hard | absolute black | neutral | 1/1 (Sun) | mid | black | 0

S7 | 01:00–01:09 | Zone A | 0 (10 o'clock) | hard | absolute black | neutral | 1/1 (Sun) | dark | black | 0

S8 | 01:10–01:19 | Zone B | 9 (9 o'clock) | soft/hard | red fill | deep red | 3/3 (Sun, red alert, panels) | dark | dark red | 0

S9 | 01:20–01:29 | Zone A | 0 (10 o'clock) | hard | absolute black | neutral | 1/1 (Sun) | mid | black | 0

S10 | 01:30–01:39 | Zone B | T (top diffuse) | soft | lifted | amber warm | 1/1 (Console backlights) | mid | dark grey | 0

S11 | 01:40–01:49 | Zone A | 0 (10 o'clock) | hard | absolute black | neutral | 1/1 (Sun) | mid | black | 0

S12 | 01:50–01:59 | Zone B | W (12 o'clock) | soft | lifted | neutral green-tint | 3/3 (Sun, green LED, console) | dark | dark grey | dimmer (01:56)

## KEY DIRECTION STRING

```
OBSERVED:  0ET0E0090T0W
ZONES:     ABBBABABABAB

```

## PRESENCE STRING

`-111---1-1-1`

---

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| S7 → S8 (01:09 → 01:10) | Zone A → Zone B | Interior ambient lighting instantly shifts to intense red emergency alert cast | No | 🟠 MAJOR |
| S8 → S10 (01:19 → 01:30) | Zone B | Red emergency lights vanish; interior reverts to amber warm white; visor transforms from transparent HUD glass to opaque mirror black | No | 🔴 BLOCKER |
| S10 → S12 (01:39 → 01:50) | Zone B | Interior lighting shifts to cool green-tinted white with an unestablished green canopy LED | No | 🟠 MAJOR |
| S12 (01:56 → 01:59) | Zone B | In-clip overall exposure dims down unexpectedly before title card cut | No | 🟡 MINOR |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 8.0/10 | S8 (01:10) interior key shifts to 9 o'clock red overhead source |
| 2 | Shadow Quality & Fill | 7.0/10 | S1 (00:00), S6 (00:50) shadow regions show soft ambient bounce fill in space vacuum |
| 3 | Colour Temperature | 6.0/10 | S8 (01:10) red alert, S10 (01:30) amber white, S12 (01:50) green-tinted white temperature jumps |
| 4 | Practical Sources | 5.0/10 | S8 (01:10) red alert practicals vanish in S10 (01:30); S12 (01:50) introduces unestablished green canopy LED |
| 5 | Exposure at Cuts | 7.0/10 | S8 (01:10) to S10 (01:30) exposure drop on pilot suit across interior cut |
| 6 | In-Clip Stability | 8.0/10 | S12 (01:56–01:59) in-clip exposure dimming before title card cut |
| 7 | Zone Boundaries | N/A | mode V (no spec supplied) |
| 8 | Atmosphere Honesty | 6.0/10 | S1 (00:00) volumetric sun rays in vacuum; S7 (01:00)/S9 (01:20) lingering smoke haze in space; S10 (01:30) opaque black visor vs S3 clear visor |

---

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 1

---

## THE THREE THAT MATTER

1. **01:19 → 01:30 (S8 → S10)** — Red emergency alert lighting completely disappears between wide cockpit shot and helmet close-up. *Fix:* Grade S10 background and helmet reflections with matching red emergency ambient tint.
2. **00:00 & 01:00 (S1 & S7)** — Volumetric sunbeams and lingering smoke clouds rendered in outer space vacuum. *Fix:* Remove atmospheric volumetric scattering and particle smoke diffusion from space exterior shots.
3. **01:30 (S10)** — Visor property shift from transparent HUD glass (S3) to opaque mirror black. *Fix:* Regenerate S10 visor render with internal face/HUD transparency matching S3.

---

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Fixable in the Grade:** S8/S10/S12 cockpit color temperature wobble (tinting S10 interior red to match S8 emergency state; balancing S12 green LED cast) and S12 in-clip exposure dimming correction.
* **Requires Regeneration:** S1 volumetric vacuum sunbeams, S7/S9 vacuum smoke haze, and S10 opaque black helmet visor surface.

---

## FLAGS FOR DOCUMENT CHECK

* MODE V: Is the red emergency lighting state in S8 intended to be triggered only during kinetic impact and reset automatically afterwards?

---

## OUT-OF-SCOPE FLAGS

* **BACKGROUND lens:** S3 cockpit button panel layout differs slightly from S8/S12 background console structures.
* **PHYSICS lens:** S7 thruster plume expanding and remaining visible in vacuum frame without rapid dispersal.
* **SETUP lens:** S3 and S10 helmet close-up framing shows slight focal length and camera distance discrepancy.
