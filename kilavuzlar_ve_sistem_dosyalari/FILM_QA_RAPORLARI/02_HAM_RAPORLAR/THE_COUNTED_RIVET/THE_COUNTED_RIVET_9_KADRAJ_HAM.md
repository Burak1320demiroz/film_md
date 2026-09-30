INPUT MODE: V
FILM: (not supplied)
RUNTIME: 04:05
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 04:00–04:05 (Title poster graphic)
PRESENCE STRING: 111111111111111111111111
LINES HEARD: none — room tone present
SETUPS REGISTERED: 20
LOCKOFF HELD: 23 / 24 clips

## SETUP LEDGER

S1 | 00:00 | N/A | CU / eye level / normal / side-on to clamp | A | MATCH | C-clamp top-left | 0
S2 | 00:10 | N/A | MCU / eye level / normal / side-on to console | B | MATCH | console housing left | 0
S3 | 00:20 | N/A | WS / eye level / normal / side profile | C | MATCH | roof edge horizon | 0
S4 | 00:30 | N/A | MCU / low angle / normal / side 3/4 | D | MATCH | rail clamp center | 0
S5 | 00:40 | N/A | WS / eye level / wide / front centered | E | MATCH | central rivet sphere | 0
S6 | 00:50 | N/A | MCU / eye level / normal / side-on to console | B | MATCH | console housing left | slow creep @ 00:56
S7 | 01:00 | N/A | WS / eye level / wide / front centered | E | MATCH | central rivet sphere | 0
S8 | 01:10 | N/A | MS / high angle / normal / rear 3/4 | F | MATCH | beacon post right | 0
S9 | 01:20 | N/A | MS / eye level / normal / side 3/4 | G | MATCH | railing bar mid-frame | 0
S10 | 01:30 | N/A | MCU / eye level / normal / front 3/4 | H | MATCH | corrugated rod bottom | 0
S11 | 01:40 | N/A | MS / high angle / normal / rear 3/4 | F | MATCH | beacon post right | 0
S12 | 01:50 | N/A | CU / eye level / normal / side profile | I | MATCH | canvas grommets left | 0
S13 | 02:00 | N/A | MS / eye level / normal / side profile | J | MATCH | canvas corner left | 0
S14 | 02:10 | N/A | CU / top-down / normal / centered | K | MATCH | circular dome edge | 0
S15 | 02:20 | N/A | CU / top-down / normal / centered | K | MATCH | circular dome edge | 0
S16 | 02:30 | N/A | MS / low angle / normal / side profile | L | MATCH | deck rail mid-frame | 0
S17 | 02:40 | N/A | MCU / low angle / normal / side profile | M | MATCH | handrail bar center | 0
S18 | 02:50 | N/A | CU / high angle / wide / top-down 3/4 | N | MATCH | C-clamp center | 0
S19 | 03:00 | N/A | ECU / eye level / normal / front centered | O | MATCH | helmet ring center | 0
S20 | 03:10 | N/A | CU / eye level / normal / front POV | P | MATCH | shears pivot point | 0
S21 | 03:20 | N/A | MS / high angle / wide / side 3/4 | Q | MATCH | deck rivet line | 0
S22 | 03:30 | N/A | CU / top-down / wide / front POV | R | MATCH | deck edge flange | 0
S23 | 03:40 | N/A | MS / high angle / wide / side 3/4 | S | MATCH | clamp line along edge | 0
S24 | 03:50 | N/A | CU / eye level / wide / front POV | T | MATCH | wall bracket center | 0

## SETUP STRING

```
OBSERVED:   A B C D E B E F G H F I J K K L M N O P Q R S T
PLAN:       none (mode V)
DIFFERS AT: none
```

## PRESENCE STRING

`111111111111111111111111`

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / variable | A / CU / eye level / C-clamp top-left / initial clamp state | T / CU / eye level / wall bracket center / resting gloved hands | No |

Verdict line: `PAIR FAILS` — S1 (Setup A) and S24 (Setup T) use completely different camera setups, positions, and anchors, failing to form a visual rhyme pair.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S6 | Locked off | Creep / drift | 00:56 | Unplanned movement |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V — no written spec supplied |
| 2 | Lockoff Integrity | 9/10 | 🟡 S6 (00:56): minor camera creep/drift in last 4 seconds |
| 3 | Rhyme Pair | 1/10 | 🔴 S1 (00:00) vs S24 (03:50): setup mismatch (Setup A vs Setup T); pair fails |
| 4 | Return Consistency | 10/10 | None — all setup returns (B, E, F) maintain exact anchor placement |
| 5 | Cluster Seams | 8/10 | 🟡 S14 (02:10) -> S15 (02:20): S15 is an exact duplicate take/loop of S14 |
| 6 | Angle Arc & Deliberate Shocks | 10/10 | None — well-structured variation in shot scale and angle |
| 7 | Screen Geometry | 10/10 | None — horizon and anchor alignment remain stable |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **S1 vs S24 (00:00 vs 03:50)**: The final scene uses Setup T instead of returning to Setup A, breaking the closing rhyme pair.
*Fix*: Regenerate S24 from Setup A's perspective (CU side-on C-clamp) showing the final post-action state.
2. **S14 to S15 seam (02:10–02:30)**: S15 duplicates S14 frame-for-frame, creating a stagnant shot loop across the cut seam.
*Fix*: Trim S15 from the timeline in post-production.
3. **S6 (00:56)**: Subtle camera drift during the final 4 seconds of the control console lockoff.
*Fix*: Apply digital image stabilization to freeze the frame position in post.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Fixable in Post**: The S6 camera drift can be stabilized digitally with minimal frame cropping. The S15 duplicate seam can be edited out by cutting directly from S14 to S16.
* **Requires Regeneration**: The S24 rhyme pair failure cannot be corrected in post because the camera setup and spatial perspective are fundamentally different; S24 must be re-rendered using Setup A.

## FLAGS FOR DOCUMENT CHECK

* Mode V evaluated without a written SPEC. Were S14 and S15 intended as two distinct actions or an accidental clip duplication?
* Was a closing camera rhyme explicitly requested to mirror S1 in S24?

## OUT-OF-SCOPE FLAGS

* **Continuity**: The metal bar position on the dome resets between S14 and S15.
* **Background**: Atmospheric density shifts abruptly between S13 (cloud layer) and S14 (clear orange sky).
* **Action / Effort**: S3 hammer impacts show minimal physical weight feedback on the metal roof.
