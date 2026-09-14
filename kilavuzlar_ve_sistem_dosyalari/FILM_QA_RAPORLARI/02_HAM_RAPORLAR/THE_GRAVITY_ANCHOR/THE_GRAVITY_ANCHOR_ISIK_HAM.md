INPUT MODE: V
FILM: the gravıty anchor.mp4
RUNTIME: 01:44 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 10 · CUTS COUNTED: 9 · CUTS OFF GRID: none
NON-SCENE MATERIAL: 01:40–01:44 end title card
PRESENCE STRING: 1111111111
LINES HEARD: none — nothing audible to me
ZONES REGISTERED: 1 · MEDIUM: vacuum
LIGHT JUMPS: 2 · CLEAN CUTS: 7

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  7        (N/A excluded, never 0)
SUM OF SCORES:      36.0
DIVISION:           36.0 ÷ 7 = 5.1      ← this is OVERALL SCORE

OVERALL SCORE: 5.1/10
VERDICT: GRADEABLE DRIFT

---

## LIGHT LEDGER

| S | in | zone | key direction (clock · elevation) | quality | shadow density | temperature | practicals lit / present | subject exposure (bright · mid · dark) | background black level | in-clip change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 00:00 | Crater Zone | 10:00 · 45° | Hard | Absolute black | Warm key / cool ambient | 0/0 | Mid | Deep black | 0 |
| S2 | 00:10 | Crater Zone | 10:00 (face) / 01:00 (suns) · 30° | Soft fill / hard rim | Lifted shadow | Warm key / neutral fill | 1/1 | Mid | Mid black | 0 |
| S3 | 00:20 | Crater Zone | 10:00 · 45° | Hard | Absolute black | Warm key / cool ambient | 1/1 | Mid | Deep black | 0 |
| S4 | 00:30 | Crater Zone | 10:00 · 45° | Hard | Deep shadow | Warm key / cool ambient | 1/1 | Mid | Deep black | 0 |
| S5 | 00:40 | Crater Zone | 10:00 · 45° | Hard | Absolute black | Warm key / cool ambient | 0/0 | Mid | Deep black | 0 |
| S6 | 00:50 | Crater Zone | 10:00 · 45° | Hard | Deep shadow | Warm key / cool ambient | 0/0 | Mid | Deep black | 0 |
| S7 | 01:00 | Crater Zone | 10:00 · 45° | Hard | Deep shadow | Warm key / gold interface | 1/1 | Mid | Deep black | 0 |
| S8 | 01:10 | Crater Zone | 10:00 · 45° | Soft / direct glow | Lifted helmet interior | Warm key / gold reflection | 1/1 | Bright | Deep black | 0 |
| S9 | 01:20 | Crater Zone | 10:00 · 45° | Hard | Absolute black | Warm key / star floor glow | 1/1 | Mid | Deep black | 0 |
| S10 | 01:30 | Crater Zone | 10:00 · 45° | Hard | Absolute black | Warm key / star floor glow | 1/1 | Mid | Deep black | 0 |

### ADJACENT-PAIR TEST

* **S1 → S2 (00:10):** Twin suns jump from top-left background (10:00) to right background (01:00), while key on astronaut's face remains top-left.
* **S2 → S3 (00:20):** Sun position snaps back to 10:00 high left.
* **S3 → S4 (00:30):** Clean cut; practical glow on wrist interface remains stable.
* **S4 → S5 (00:40):** Clean cut; ground shadow density holds.
* **S5 → S6 (00:50):** Clean cut; key direction on boot/leg matches 10:00 key.
* **S6 → S7 (01:00):** Clean cut; golden interface ring practical lights up smoothly.
* **S7 → S8 (01:10):** Subject face exposure jumps brighter in close-up shot.
* **S8 → S9 (01:20):** Exposure returns to standard mid-tone wide balance.
* **S9 → S10 (01:30):** Clean cut; starry ground reflection path key intensity holds.

---

## KEY DIRECTION STRING

```
OBSERVED:  0000000000
ZONES:     CCCCCCCCCC

```

---

## PRESENCE STRING

`1111111111`

---

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| Cut 1 (S1 → S2) | Crater Zone | Sun placement jumps to right background while face key remains left | No | 🟠 MAJOR |
| Cut 7 (S7 → S8) | Crater Zone | Visor interior and face exposure jump ~0.5 EV brighter on close-up cut | No | 🟡 MINOR |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 4.0/10 | -3 · S2 (00:10) key direction on face conflicts with background sun placement |
| 2 | Shadow Quality & Fill | 5.0/10 | -2 · S2 (00:10), S8 (01:10) shadow density lifts inside helmet interior |
| 3 | Colour Temperature | 6.0/10 | -1 · S7–S8 (01:00–01:10) gold practical light causes slight warmth drift on cheek |
| 4 | Practical Sources | 6.0/10 | -1 · S4 (00:30) wrist interface output fluctuates slightly relative to sun key |
| 5 | Exposure at Cuts | 5.0/10 | -2 · S7→S8 (01:10 cut) close-up face exposure jumps brighter than wide shot |
| 6 | In-Clip Stability | 6.0/10 | -1 · S3 (00:20) rainbow beam glow intensity shows subtle in-clip drift |
| 7 | Zone Boundaries | N/A | Mode V — no written specification supplied |
| 8 | Atmosphere Honesty | 4.0/10 | -3 · S1 (00:00), S3 (00:20) volumetric light bloom around suns in airless vacuum |

---

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 1

---

## THE THREE THAT MATTER

1. **00:10 (S2) — Background Sun Position Mismatch:** Key light on astronaut's face stays front-left while twin suns jump behind her shoulder.
*Fix:* Re-render S2 background with twin suns placed in the upper-left frame quadrant.
2. **01:10 (S8) — Close-Up Exposure Jump:** Helmet interior exposure brightens noticeably upon cutting to close-up.
*Fix:* Trim exposure on S8 by ~0.5 EV during color grade to match S7.
3. **00:00 & 00:20 (S1 & S3) — Atmospheric Bloom in Vacuum:** Volumetric halos around suns contradict airless crater environment.
*Fix:* Reduce soft volumetric halos on twin suns during compositing pass.

---

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Fixable in the Grade:** S8 close-up face exposure trim and minor warmth balance adjustment across S7–S8.
* **Requires Regeneration:** S2 background key mismatch (sun placement relative to key lighting).

---

## FLAGS FOR DOCUMENT CHECK

* Does the narrative specification define localized gas venting near the monolith to validate volumetric bloom in a vacuum setting?

---

## OUT-OF-SCOPE FLAGS

* **CONTINUITY lens:** Monolith surface texture and terrain cracks display minor AI morphing between S1 and S3.
* **PHYSICS lens:** Levitating rocks in S5 lift smoothly without visible impulse forces.
