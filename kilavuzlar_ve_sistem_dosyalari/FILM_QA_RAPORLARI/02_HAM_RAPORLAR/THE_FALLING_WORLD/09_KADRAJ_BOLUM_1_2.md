INPUT MODE: D
FILM: THE_FALLING_WORLD
RUNTIME: 04:00 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: hook 10s + (n−1) × 10s · 10.0s fixed grid
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: none
NON-SCENE MATERIAL: none
PRESENCE STRING: 111111111111111111111111
LINES HEARD: 1 · "Hold on!" at 02:46
SETUPS REGISTERED: 13 distinct camera positions (A, B, C, E, F, G, I, K, L, M, N, O, P)
LOCKOFF HELD: 24 / 24 clips

---

## ⛔ STEP 0 — SETUP REGISTER

* **A**: EWS/WS · Low angle · Wide lens · Front across fissure · Anchor: Fissure center-left
* **B**: MCU/CU · Eye level · Normal lens · Side-on harness · Anchor: Belt buckle
* **C**: MCU · Eye/low angle · Wide-normal · Rear buggy interior · Anchor: Roll bar frame
* **E**: EWS · High angle · Wide lens · Overhead slab road · Anchor: Paved road centerline
* **F**: WS · Low-eye angle · Wide lens · Rear cliff road · Anchor: Cliff face wall
* **G**: ECU · Low ground angle · Wide-macro · Wheel-rock contact · Anchor: Buggy tire rim
* **I**: WS · High angle · Wide lens · Platform three-quarter · Anchor: Platform grating corner
* **K**: MS · Eye level · Normal lens · Tunnel interior · Anchor: Arch frame
* **L**: MCU/CU · Eye level · Macro-normal · Suit wrist cuff · Anchor: Cuff joint seam
* **M**: WS · Low-eye angle · Wide lens · Ridge path · Anchor: Ridge edge line
* **N**: MS · Eye level · Normal lens · Figures walking · Anchor: Foreground rock
* **O**: WS · High angle · Wide lens · Ledge path top-down · Anchor: Ledge border
* **P**: WS · Low-eye angle · Wide lens · Cliff structure approach · Anchor: Structure base

---

## SETUP LEDGER

| Scene | in | plan letter | observed size / angle / lens / position | observed letter | MATCH / NEAR / MISS | anchor position | in-clip movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S00 | 00:00 | A | EWS / low angle / wide / front-side | A | MATCH | Fissure center-left | 0 |
| S01 | 00:10 | B | MCU / eye level / normal / side harness | B | MATCH | Belt buckle | 0 |
| S02 | 00:20 | B | MCU / eye level / normal / side latch | B | MATCH | Belt latch strap | 0 |
| S03 | 00:30 | A | EWS / low angle / wide / rear-side | A | MATCH | Foreground fissure | 0 |
| S04 | 00:40 | C | MCU / eye level / wide-normal / buggy interior | C | MATCH | Roll bar frame | 0 |
| S05 | 00:50 | E | EWS / high angle / wide / road top-down | E | MATCH | Road centerline | 0 |
| S06 | 01:00 | E | EWS / high angle / wide / road & tower | E | MATCH | Slab edge | 0 |
| S07 | 01:10 | C | MCU / eye level / normal / buggy side-rear | C | MATCH | Roll cage bar | 0 |
| S08 | 01:20 | F | WS / low-eye angle / wide / cliff road rear | F | MATCH | Cliff face wall | 0 |
| S09 | 01:30 | G | ECU / low ground angle / wide-macro / wheel | G | MATCH | Tire rim | 0 |
| S10 | 01:40 | F | WS / low-eye angle / wide / rockfall road | F | MATCH | Cliff face wall | 0 |
| S11 | 01:50 | F | WS / low-eye angle / wide / door ramp | F | MATCH | Steel doorway | 0 |
| S12 | 02:00 | I | WS / high-eye angle / wide / platform | I | MATCH | Platform grating | 0 |
| S13 | 02:10 | I | WS / high angle / wide / platform collapse | I | NEAR (elevation shift) | Doorway arch | 0 |
| S14 | 02:20 | K | MS / eye level / normal / tunnel walk | K | MATCH | Archway frame | 0 |
| S15 | 02:30 | K | MS / eye level / normal / tunnel walk | K | MATCH | Wall joint | 0 |
| S16 | 02:40 | L | MCU / eye level / macro-normal / wrist cuff | L | MATCH | Sleeve cuff | 0 |
| S17 | 02:50 | L | MCU / eye level / normal / hands repair | L | MATCH | Wrist console | 0 |
| S18 | 03:00 | K | MS / eye level / normal / door exit | K | MATCH | Door arch | 0 |
| S19 | 03:10 | M | WS / low-eye angle / wide / ridge path | M | MATCH | Ridge edge line | 0 |
| S20 | 03:20 | N | MS / eye level / normal / figures walk | N | MATCH | Foreground rock | 0 |
| S21 | 03:30 | O | WS / high angle / wide / top-down ledge | O | MATCH | Ledge border | 0 |
| S22 | 03:40 | N | MS / eye level / normal / figures walk | N | MATCH | Rock cluster | 0 |
| S23 | 03:50 | P | WS / low-eye angle / wide / cliff structure | P | MATCH | Structure base | 0 |

---

## SETUP STRING

```
OBSERVED:   ABBACEECFGFFIIKKLLKMNONP
PLAN:       ABBACEECFGFFIIKKLLKMNONP
DIFFERS AT: none
```

---

## PRESENCE STRING

`111111111111111111111111`

---

## RHYME PAIR

|  | First frame (S00, 00:00) | Last frame (S23, 03:59) | Same? |
| --- | --- | --- | --- |
| setup / size / angle / anchor / variable | A / EWS / low angle / fissure center / holding cable | P / WS / low-eye angle / structure base / walking | No |

VERDICT: `PAIR FAILS` — S00 uses Setup A while S23 uses Setup P (file contains Part 1 & 2; planned closing rhyme sits at S47/Setup H).

---

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| All held. |  |  |  |  |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 9/10 🟡 | S13 (02:10) angle elevation shift relative to S12 |
| 2 | Lockoff Integrity | 10/10 🟢 | None; all 24 clips hold static camera lockoff |
| 3 | Rhyme Pair | 5/10 🔴 | Opening frame S00 (Setup A) vs closing frame S23 (Setup P) |
| 4 | Return Consistency | 9/10 🟡 | S13 (02:10) minor camera pitch drift on return of Setup I |
| 5 | Cluster Seams | 10/10 🟢 | Seams at S11↔S12 (02:00) and S23 (03:50) hold geometry |
| 6 | Angle Arc & Deliberate Shocks | 10/10 🟢 | Planned scale jumps land cleanly on grid cuts |
| 7 | Screen Geometry | 10/10 🟢 | Screen direction and anchor lines hold across setups |

VERDICT: `RHYME BROKEN`

---

## THE THREE THAT MATTER

1. **S23 (03:59)**: Rhyme pair fails for this 2-part file; opening frame S00 (Setup A) does not match closing frame S23 (Setup P).
* *Fix*: Append remaining Part 3 & 4 files to complete sequence through S47.

2. **S13 (02:10)**: Setup I returns with a slightly steeper high-angle pitch compared to S12.
* *Fix*: Re-render S13 using identical camera height and pitch parameters as S12.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration**: S13 camera angle elevation shift (cannot be corrected in post without distortion).
* **Fixable in Edit**: None; all clip durations and cuts adhere strictly to the 10.0s grid.

---

## FLAGS FOR DOCUMENT CHECK

* S23 serves as the file boundary for Part 2; confirm master assembly binds Part 1–4 continuously to preserve S00↔S47 rhyme.

---

## OUT-OF-SCOPE FLAGS

* **CONTINUITY**: Suit dust level jumps slightly between S13 (02:10) and S14 (02:20).
* **AUDIO**: Single radio line heard at 02:46 ("Hold on!").
