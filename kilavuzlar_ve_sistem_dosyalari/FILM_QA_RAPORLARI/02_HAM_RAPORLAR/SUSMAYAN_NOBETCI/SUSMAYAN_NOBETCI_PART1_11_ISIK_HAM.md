INPUT MODE: V
FILM: (not supplied)
RUNTIME: 04:00 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: 11-1111---1-1-1---1---111
LINES HEARD: 2 · 01:11 "Target detected", 02:23 "F6"
ZONES REGISTERED: 3 · MEDIUM: vacuum — no haze, no bloom, no dust
LIGHT JUMPS: 3 · CLEAN CUTS: 20

## LIGHT LEDGER

S1 | 00:05 | Cockpit | Key 11 | soft | lifted | cool | 2/2 ceiling lights | bright | deep black | 0
S2 | 00:15 | Cockpit | Key 1 | soft | lifted | cool | 2/2 helmet lights | mid | deep black | helmet lights flicker off at 00:16
S3 | 00:25 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 0/0 practicals | bright | absolute black | 0
S4 | 00:35 | Console | Key T | soft | lifted | cool | 1/1 top panel | mid | dark grey | 0
S5 | 00:45 | Console | Key T | soft | lifted | cool | 1/1 top panel | mid | dark grey | 0
S6 | 00:55 | Cockpit | Key E | soft | lifted | cool | 2/2 ceiling lights | mid | deep black | 0
S7 | 01:05 | Console | Key T | soft | lifted | cool | 1/1 top panel | mid | dark grey | 0
S8 | 01:15 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 0/0 practicals | bright | absolute black | thruster flare at 01:17
S9 | 01:25 | Orbit | Key E | hard | absolute black | cool key / warm fill | 0/0 practicals | mid | absolute black | 0
S10 | 01:35 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 3/3 windows lit | mid | absolute black | 0
S11 | 01:45 | Console | Key T | soft | dark shadow | cool | 1/1 top panel | dark | deep grey | exposure drops vs S7
S12 | 01:55 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 0/0 practicals | bright | absolute black | 0
S13 | 02:05 | Console | Key T | soft | lifted | neutral | 1/1 top panel | mid | dark grey | 0
S14 | 02:15 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 3/3 windows lit | bright | absolute black | 0
S15 | 02:25 | Console | Key T | soft | dark shadow | cool | 1/1 top panel | mid | dark grey | 0
S16 | 02:35 | Orbit | Key 9 | hard | absolute black | cool key / neutral fill | 0/0 practicals | bright | absolute black | volumetric explosion haze at 02:33
S17 | 02:45 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 3/3 windows lit | mid | absolute black | 0
S18 | 02:55 | Console | Key T | soft | lifted | neutral | 1/1 top panel | mid | dark grey | screen bloom drift at 02:56
S19 | 03:05 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 3/3 windows lit | mid | absolute black | 0
S20 | 03:15 | Orbit | Key T | hard | dark shadow | warm inside | 3/3 windows lit | mid | absolute black | background dims to black at 03:18
S21 | 03:25 | Orbit | Key 0 | hard | absolute black | cool key / warm fill | 0/0 practicals | mid | absolute black | thruster flash at 03:23
S22 | 03:35 | Console | Key T | soft | lifted | neutral | 1/1 top panel | dark | dark grey | 0
S23 | 03:45 | Cockpit | Key T | hard/soft | lifted | cool | 2/2 helmet lights | mid | deep black | helmet lights turn off at 03:44 and 03:48
S24 | 03:55 | Console | Key T | soft | lifted | neutral | 1/1 top panel | mid | dark grey | 0

## KEY DIRECTION STRING

```
OBSERVED:  E10TTETE0T0T0T90T0T0TTT
ZONES:     (mode V)

```

## PRESENCE STRING

11-1111---1-1-1---1---111

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| S1 (00:09) → S2 (00:10) | Cockpit | Key direction flipped from 11 o'clock to 1 o'clock on helmet | N/A | 🟠 |
| S10 (01:39) → S11 (01:40) | Console | Exposure drop on console panel by ~1.5 EV | N/A | 🟡 |
| S20 (03:19) → S21 (03:20) | Orbit | Sudden exposure jump after S20 dims to pitch black at 03:18 | N/A | 🟠 |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 6/10 | S1 (00:05) key at 11 o'clock jumps to 1 o'clock in S2 (00:15); S23 (03:45) key dominated by visor practicals |
| 2 | Shadow Quality & Fill | 7/10 | Console fill levels bounce between deep shadow (S11 at 01:45) and lifted grey (S4 at 00:35, S13 at 02:05) |
| 3 | Colour Temperature | 8/10 | Console CRT screen drift between cool cyan (S4 at 00:35) and neutral/warm (S18 at 02:55) |
| 4 | Practical Sources | 5/10 | Helmet mounted lights blink and turn off/on unmotivated in S2 (00:16) and S23 (03:44, 03:48) |
| 5 | Exposure at Cuts | 7/10 | S10 → S11 (01:40) console exposure drop; S20 → S21 (03:20) jump from blackout to daylight |
| 6 | In-Clip Stability | 6/10 | In-clip dimming to black during camera movement in S20 (03:18); screen glare drift in S18 (02:56) |
| 7 | Zone Boundaries | — | N/A in mode V |
| 8 | Atmosphere Honesty | 6/10 | Volumetric light beams and explosion haze rendered in vacuum in S1 (00:03), S16 (02:33), S21 (03:23) |

VERDICT: KEY WALKS

## THE THREE THAT MATTER

1. **00:10 (S1 → S2)**: Key light flips from 11 o'clock to 1 o'clock on pilot helmet. Fix: Re-generate S2 with key light aligned to top-left (11 o'clock).
2. **00:16 & 03:44 (S2, S23)**: Visor headlights blink and shut off without pilot action. Fix: Re-generate S2 and S23 with locked, constant visor practical illumination.
3. **02:33 (S16)**: Volumetric atmospheric glow and ray scatter rendered during explosion in space vacuum. Fix: Re-generate S16 enforcing vacuum light behavior without particulate haze.

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Fixable in Grade**: Lift exposure on S11 (01:45) by +1.2 EV to match S7 console levels; trim colour temperature on S18 (02:55) CRT display to match cool baseline.
* **Requires Regeneration**: Key light direction flip on S2 (00:15); helmet practical light blinking on S2 (00:16) and S23 (03:44); volumetric haze in vacuum on S16 (02:33); in-clip blackout dimming on S20 (03:18).

## FLAGS FOR DOCUMENT CHECK

* Verify whether pilot helmet headlights are intended to be switchable practicals or static illuminators across cockpit scenes.

## OUT-OF-SCOPE FLAGS

* **CONTINUITY / BACKGROUND**: Display graphics on CRT console monitor switch layout between S4 (00:35) and S18 (02:55).
* **SETUP**: Camera height and angle on control panel shift between low close-up in S7 (01:05) and high quarter angle in S15 (02:25).
* **PHYSICS**: External module hatch panel velocity and floating trajectory vary noticeably between S14 (02:15) and S16 (02:35).
