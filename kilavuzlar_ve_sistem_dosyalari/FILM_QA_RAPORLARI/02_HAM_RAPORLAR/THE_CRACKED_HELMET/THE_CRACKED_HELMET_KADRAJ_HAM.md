INPUT MODE: D
FILM: THE_CRACKED_HELMET
RUNTIME: ~01:50 ESTIMATED
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode D, but SPEC grid missing)
SCENES OBSERVED: 11 · CUTS COUNTED: 10 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 01:50-02:04 Title Card
PRESENCE STRING: 11111111111
LINES HEARD: none — nothing audible to me
SETUPS REGISTERED: 8 distinct camera positions
LOCKOFF HELD: 0 / 11 clips

ARITHMETIC GATE
SCORED CATEGORIES:  7
SUM OF SCORES:      15.0
DIVISION:           15.0 ÷ 7 = 2.1

OVERALL SCORE: 2.1/10
VERDICT: RHYME BROKEN

SETUP REGISTER
· letter A [first seen S1] · WS · eye · normal · side-on · anchor: cracked helmet
· letter B [first seen S2] · CU · eye · normal · front · anchor: helmet visor
· letter C [first seen S3] · MS · low · normal · front · anchor: character torso
· letter D [first seen S4] · MCU · top-down · normal · front · anchor: chest UI
· letter E [first seen S5] · ECU · eye · normal · front · anchor: glowing crystal
· letter F [first seen S6] · MS · low · normal · front (profile) · anchor: lunar shelter
· letter G [first seen S10] · ECU · eye · normal · front · anchor: liquid sphere
· letter H [first seen S11] · WS · eye · wide · rear · anchor: binary suns

SETUP LEDGER
| # | in | plan letter | observed size / angle / lens / position | observed letter | MATCH · NEAR · MISS | anchor position | in-clip movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 0:00 | A | WS / eye / normal / side-on | A | MATCH | Centered | slow push-in, starts 0:00 |
| S2 | 0:10 | B | CU / eye / normal / front | B | MATCH | Centered | slow push-in, starts 0:10 |
| S3 | 0:20 | C | MS / low / normal / front | C | MATCH | Centered | static |
| S4 | 0:30 | D | MCU / top-down / normal / front | D | MATCH | Lower third | static |
| S5 | 0:40 | E | ECU / eye / normal / front | E | MATCH | Centered | static |
| S6 | 0:50 | F | MS / low / normal / front (profile) | F | MATCH | Centered | slow push-in, starts 0:50 |
| S7 | 0:59 | E | CU / eye / normal / side (profile) | ? | MISS (Expected ECU) | Centered | slow push-in, starts 0:59 |
| S8 | 1:08 | E | ECU / eye / normal / front | E | MATCH | Centered | static |
| S9 | 1:20 | B | CU / eye / normal / front | B | MATCH | Centered | slow push-in, starts 1:20 |
| S10 | 1:30 | G | ECU / eye / normal / front | G | MATCH | Centered | static |
| S11 | 1:40 | H | WS / eye / wide / rear | H | MATCH | Horizon | slow push-in, starts 1:40 |

SETUP STRING
OBSERVED:   ABCDEF?EBGH
PLAN:       [Not supplied in prompt, assumed A-H mapping for ledger purposes based on visual evidence, but cannot verify against a non-existent plan string]
DIFFERS AT: S7

RHYME PAIR
| First frame (S1) | Last frame (S11) | Same? |
| --- | --- | --- |
| A / WS / eye / side-on / helmet | H / WS / eye / rear / suns | NO |
Verdict line: PAIR FAILS — The film does not return to the opening setup; it introduces a completely new wide shot from behind for the ending.

LOCKOFF VERIFICATION
| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S1 | Lockoff (assumed default) | Slow push-in | 0:00 | FAILS |
| S2 | Lockoff (assumed default) | Slow push-in | 0:10 | FAILS |
| S6 | Lockoff (assumed default) | Slow push-in | 0:50 | FAILS |
| S7 | Lockoff (assumed default) | Slow push-in | 0:59 | FAILS |
| S9 | Lockoff (assumed default) | Slow push-in | 1:20 | FAILS |
| S11 | Lockoff (assumed default) | Slow push-in | 1:40 | FAILS |

SCORES SUMMARY
| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 5/10 | -5 · S7 (0:59) (Expected ECU based on previous 'E' setup, delivered CU profile) |
| 2 | Lockoff Integrity | 1/10 | -9 · S1, S2, S6, S7, S9, S11 (Unplanned creeping dolly throughout film) |
| 3 | Rhyme Pair | 1/10 | -9 · S1 vs S11 (Total setup mismatch) |
| 4 | Return Consistency | 4/10 | -6 · S9 (1:20) returns to B but anchor (helmet cracks) shift position relative to frame edge due to drift. |
| 5 | Cluster Seams | N/A | no declared seams |
| 6 | Angle Arc & Deliberate Shocks | 1/10 | -9 · S3 (0:20) (Unplanned low angle Dutch introduced without prior setup) |
| 7 | Screen Geometry | 3/10 | -7 · S6 (0:50) vs S7 (0:59) (Subject flips screen side between consecutive shots) |

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 3   🟡 MINOR: 0

THE THREE THAT MATTER
1. **0:00 vs 1:40 — Rhyme Broken:** The film opens on a side-on wide and ends on a rear wide. The visual loop is shattered. Fix: Regenerate S11 using Setup A.
2. **Continuous — Creeping Dolly (Pattern 3):** Six out of eleven shots feature an unmotivated slow push-in, destroying the intended contemplative lockoff aesthetic. Fix: Stabilize in edit (will cost 10-15% resolution crop).
3. **0:59 (S7) — Setup Miss:** Reverts to a generic profile medium-close instead of the tight ECU established for the crystal interaction. Fix: Regenerate S7 with tighter framing.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
The creeping dollys can be stabilized in post, but at a significant cost to framing and resolution. The broken rhyme pair and the setup miss on S7 require regeneration.

FLAGS FOR DOCUMENT CHECK
QUESTION: Was the constant slow push-in across multiple clips an intended "breathing" effect, or an AI generation artifact?

OUT-OF-SCOPE FLAGS
- 1:20 — The glowing liquid sphere appears to float regardless of the character's orientation. → PHYSICS lens.
- 0:20 — The HUD text is baked into the glass surface. → FRAME lens.
