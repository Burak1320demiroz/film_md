INPUT MODE: V
FILM: the rıng walker.mp4
RUNTIME: 01:15 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 14 · CUTS COUNTED: 13 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 01:10–01:15 title card / end graphic ("THE RING WALKER")
PRESENCE STRING: 11111111111-1-
LINES HEARD: none — room tone and ambient musical score present
SETUPS REGISTERED: 14 distinct camera positions
LOCKOFF HELD: 6 / 14 clips

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  3
SUM OF SCORES:      14.5
DIVISION:           14.5 ÷ 3 = 4.8

OVERALL SCORE: 4.8/10
VERDICT: RHYME BROKEN

---

## SETUP LEDGER

| Scene | Time | Plan Letter | Observed Size / Angle / Lens / Position | Observed Letter | Match | Anchor Position | In-Clip Movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 00:00 | - | WS / eye-low / wide / front-quarter lander & astronaut | A | MATCH | Lander module right | 0 |
| S2 | 00:05 | - | ECU / steep high / macro / ground level footprints | B | MATCH | Boot print in crystal sand | Tracking drift along footsteps at 00:05s |
| S3 | 00:10 | - | MCU / low angle / normal / facing astronaut looking up | C | MATCH | Ringed planet horizon | Push-in / tilt-up at 00:10s |
| S4 | 00:15 | - | MS / eye-level / wide / side-front walking astronaut | D | MATCH | Distant lander | 0 |
| S5 | 00:20 | - | MCU / eye-high / normal / crouching astronaut side-front | E | MATCH | Wrist interface module | Breathing re-centre at 00:20s |
| S6 | 00:25 | - | ECU / top-down / macro / close-up glove touching sand | F | MATCH | Tread pattern in sand | Push-in / zoom at 00:26s |
| S7 | 00:30 | - | MS / low angle / wide / crater rim with rock walls | G | MATCH | Cleft rock wall left | Upward tilt & push at 00:31s |
| S8 | 00:35 | - | MCU / eye-high / normal / kneeling astronaut with object | H | MATCH | Crater rim edge behind | 0 |
| S9 | 00:40 | - | MS / eye level / wide / kneeling astronaut pouring sand | I | MATCH | Crater rim ridge | Slow push-out at 00:41s |
| S10 | 00:45 | - | MS / low angle / wide / walking astronaut near meteorite | J | MATCH | Distant lander | 0 |
| S11 | 00:50 | - | MS / low angle / normal / astronaut under meteor shower | K | MATCH | Planet ring arc behind helmet | Upward creep at 00:51s |
| S12 | 00:55 | - | EWS / low angle / ultra-wide / ringed planet sky | L | MATCH | Lander silhouette lower-left | 0 |
| S13 | 01:00 | - | MCU / low angle / normal / feet climbing ladder | M | MATCH | Ladder steps & hatch text | Tilt-up tracking at 01:01s |
| S14 | 01:05 | - | EWS / eye level / ultra-wide / lander ship in desert | N | MATCH | Silver spaceship body | 0 |

---

## SETUP STRING

```
OBSERVED:   ABCDEFGHIJKLMN
PLAN:       none (mode V)
DIFFERS AT: none

```

---

## PRESENCE STRING

```
11111111111-1-

```

---

## RHYME PAIR

|  | First frame (00:00 - S1) | Last frame (01:05 - S14) | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / variable | Setup A / WS / eye-low / lander on right / astronaut walking | Setup N / EWS / eye-level / silver ship center-left / desert landscape | NO |

Verdict line: `PAIR FAILS` — Opening frame (S1: wide shot of astronaut next to orange/black lander module) and closing scene frame (S14: extreme wide shot of a silver spaceship in desert) do not share camera setup, scale, anchor, or environment.

---

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S2 | Locked off | Tracking drift along footsteps | 00:05s | DRIFT |
| S3 | Locked off | Push-in and tilt-up motion | 00:10s | PUSH / TILT |
| S5 | Locked off | Camera breathing and frame re-centre | 00:20s | BREATHING |
| S6 | Locked off | Push-in / zoom toward glove | 00:26s | PUSH |
| S7 | Locked off | Upward tilt and push motion | 00:31s | TILT |
| S9 | Locked off | Slow camera push-out / zoom | 00:41s | PUSH |
| S11 | Locked off | Upward camera creep | 00:51s | CREEP |
| S13 | Locked off | Tilt-up tracking along ladder | 01:01s | TRACKING |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V pass — no written SPEC supplied |
| 2 | Lockoff Integrity | 5.0/10 | Unplanned camera movement/drift in S2 (00:05), S3 (00:10), S5 (00:20), S6 (00:26), S7 (00:31), S9 (00:41), S11 (00:51), S13 (01:01) |
| 3 | Rhyme Pair | 2.0/10 | S1 (00:00) vs S14 (01:05) pair fails; different setup, camera distance, anchor, and lander asset |
| 4 | Return Consistency | N/A | No setup letter repeats across the film (14 unique setups used) |
| 5 | Cluster Seams | N/A | No split shots or seams declared |
| 6 | Angle Arc & Deliberate Shocks | 7.5/10 | Abrupt scale jump between S11 (00:50 MS) and S12 (00:55 EWS) without intermediate transition |
| 7 | Screen Geometry | N/A | No setup letter repeats to evaluate geometry consistency across returns |

---

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 1

---

## THE THREE THAT MATTER

1. **00:00 (S1) vs 01:05 (S14)** — 🔴 BLOCKER: Rhyme pair completely fails. The closing scene uses a new extreme wide camera setup (N) showing a silver ship in a flat desert, failing to match the opening setup (A) with the orange/black lander module and foreground astronaut scale.
*Fix:* Regenerate S14 from the camera position, lens angle, and lander asset of Setup A to lock the bookend rhyme frame.
2. **00:05–01:05 (S2, S3, S5, S6, S7, S9, S11, S13)** — 🟠 MAJOR: Unprompted camera movement and drift break lockoff across 8 out of 14 scenes.
*Fix:* Lock camera parameters during generation or apply post-stabilization/cropping to remove creep.
3. **00:50 (S11) to 00:55 (S12)** — 🟡 MINOR: Unplanned two-step scale jump from MS (S11) to EWS (S12) creates a jarring camera visual shock.
*Fix:* Adjust S12 framing to a Wide Shot (WS) or insert a transitional WS setup between S11 and S12.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration:** S14 rhyme pair failure cannot be corrected in post. The lander asset and camera setup in S14 differ entirely from S1; regenerating S14 with Setup A reference parameters is mandatory.
* **Fixable in Post / Edit:** Minor camera breathing and lockoff drifts in S2, S5, S6, S9, and S11 can be stabilized in editing software at a slight resolution crop cost.

---

## FLAGS FOR DOCUMENT CHECK

* Is S14 intended to be a bookend rhyme return to Setup A, or is the change in spaceship design and desert landscape a planned narrative shift?

---

## OUT-OF-SCOPE FLAGS

* **CONTINUITY:** The lander module morphs from an orange/black multi-leg module ("SAVCI" text) in S1/S4 to a sleek silver spaceship in S14.
* **BACKGROUND:** The terrain shifts from a dark, rock-strewn lunar surface with craters and waterfalls in S1–S10 to flat desert sand dunes in S14.
* **FRAME:** The glow intensity and crystal physics in the ground footprint vary drastically between S2, S6, and S9.
