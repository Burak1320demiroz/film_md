INPUT MODE: V
FILM: The Cracked Helmet
RUNTIME: 02:05 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none (mode V)
NON-SCENE MATERIAL: 01:59.6–02:05 Title poster graphic ("THE CRACKED HELMET")
PRESENCE STRING: 111111111111
LINES HEARD: 1 · 00:54 "Critical ticker."
ZONES REGISTERED: 4 · MEDIUM: vacuum
LIGHT JUMPS: 2 · CLEAN CUTS: 9

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  7
SUM OF SCORES:      61.0
DIVISION:           61.0 ÷ 7 = 8.7

OVERALL SCORE: 8.7/10
VERDICT: KEY WALKS

## LIGHT LEDGER

S1 | 00:00 | Zone 1 (Crash Site) | 10 o'clock · high | hard | deep dark shadows | cool / neutral | 0/0 | mid | deep space black | 0 (steam venting)
S2 | 00:10 | Zone 1 (Helmet CU) | 10 o'clock · high rim | hard sun / soft HUD | lifted interior shadow | neutral + warm orange HUD | 1/1 (HUD lit) | bright | deep space black | 0 (gas venting)
S3 | 00:20 | Zone 1 (Sitting Up) | 10 o'clock · high | hard | deep shadows | cool purple ground / neutral suit | 1/1 (HUD lit) | mid | deep space black | 0
S4 | 00:30 | Zone 1 (Chest Pack) | 10 o'clock · high rim | hard key / soft LED | dark suit shadows | cool grey suit + warm yellow LED | 1/1 (Chest UI lit) | mid | dark background | 0 (bar countdown)
S5 | 00:40 | Zone 1 (Pickup Macro) | 10 o'clock · high | hard | crisp shadow | cool ground + warm amber glow | 0/0 | bright | dark background | 0
S6 | 00:50 | Zone 2 (Arch Canopy) | 2 o'clock · back-rim | hard rim | soft ambient shadow under arch | cool ambient + warm amber glow | 0/0 | mid | deep space black | 0
S7 | 01:00 | Zone 1 (Wrist Scan) | 10 o'clock · high | hard sun / soft UI | deep shadow right cheek | cool background + warm orange UI | 1/1 (Wrist scanner lit) | bright | deep space black | 0
S8 | 01:08 | Zone 3 (Liquid Macro) | 10 o'clock · top-left | hard backlit | deep background shadow | neutral background + golden amber liquid | 0/0 | bright | deep space black | 0 (drop forms sphere)
S9 | 01:20 | Zone 1 (Repair Visor 1) | 10 o'clock · high | hard key + reaction glow | deep shadow right face | cool exterior + fiery orange emission | 0/0 | bright face | dark space background | 0 (resin setting)
S10 | 01:30 | Zone 1 (Repair Visor 2) | 2 o'clock · high right | hard key | deep shadow left face (FLIPPED) | neutral daylight | 0/0 | mid face | dark space background | 0 (steam fades)
S11 | 01:40 | Zone 1 (Chest Pack Green) | 10 o'clock · high | hard key / soft LED glow | dark suit shadows | cool suit + green LED readout | 1/1 (Chest UI lit green) | mid | dark background | 0 (display stable)
S12 | 01:50 | Zone 4 (Twin Sun Ridge) | 9 o'clock · low horizon | soft/hard dusk | long horizontal shadows | warm golden sunset + cool upper sky | 2/2 (Twin suns lit) | mid-bright | warm horizon / space top | 0

## KEY DIRECTION STRING

OBSERVED:  000002000209
ZONES:     AAAAABACAAAA

## PRESENCE STRING

111111111111

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| Cut 9 (S9 → S10 @ 01:29.6) | Zone 1 | Key light flipped from 10 o'clock to 2 o'clock; facial shadow side inverted | No (mode V) | 🟠 MAJOR |
| Cut 10 (S10 → S11 @ 01:39.6) | Zone 1 | Key direction flipped back from 2 o'clock to 10 o'clock | No (mode V) | 🟡 MINOR |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 7/10 | S9 to S10 (01:29–01:30) key light flips from 10 o'clock to 2 o'clock; S10 to S11 (01:39–01:40) flips back to 10 o'clock |
| 2 | Shadow Quality & Fill | 9/10 | S9 to S10 (01:29–01:30) facial shadow density flips cheeks |
| 3 | Colour Temperature | 9/10 | S9 to S10 (01:29–01:30) color temp shifts from warm amber emission tint to cool daylight key |
| 4 | Practical Sources | 10/10 | no in-scope source |
| 5 | Exposure at Cuts | 8/10 | S9 to S10 (01:29–01:30) facial key illumination level jumps due to directional flip |
| 6 | In-Clip Stability | 10/10 | no in-scope source |
| 7 | Zone Boundaries | N/A | mode V |
| 8 | Atmosphere Honesty | 8/10 | S1 (00:00), S2 (00:10), S9 (01:20) venting gas exhibits soft volumetric light scatter in vacuum medium |

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 2

## THE THREE THAT MATTER

1. **01:30 (S10):** Key direction flips 120° from 10 o'clock (upper left) to 2 o'clock (upper right) across cut S9→S10 inside Zone 1. *Fix: Regenerate S10 with primary key light locked at 10 o'clock to match S9 and S11.*
2. **01:40 (S11):** Key light direction abruptly flips back from 2 o'clock to 10 o'clock across cut S10→S11. *Fix: Standardize key direction parameters to 10 o'clock across all Zone 1 AI prompts.*
3. **00:10 & 01:20 (S2 & S9):** Venting gas displays soft volumetric light scattering and bloom despite the vacuum medium declaration. *Fix: Reduce volumetric glow scattering on gas assets during post-compositing.*

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Fixable in the Grade**: The slight color temperature shift on the suit faceplate between S9 (warm amber glow) and S10 (cool daylight key) at 01:29–01:30.
* **Requires Regeneration**: Key light direction flip in S10 (01:30–01:39) where primary sun highlights and facial cast shadows flip completely from right to left across baked pixels.

## FLAGS FOR DOCUMENT CHECK

* Verify whether the environment spec declares a strict vacuum or allows thin atmospheric haze around venting gases.
* Confirm standard key light sun coordinates for Zone 1 (Crash Site) to enforce consistent clock angle across all close-up generation prompts.

## OUT-OF-SCOPE FLAGS

* `SETUP lens`: Camera focal length and perspective distortion change noticeably between close-up shots S9 and S10.
* `PHYSICS lens`: Fluid surface tension dynamics of the liquid resin droplet in microgravity (01:08–01:19).
* `BACKGROUND lens`: Ground crystal geometry layout varies between wide shot S3 and close-up S5.
