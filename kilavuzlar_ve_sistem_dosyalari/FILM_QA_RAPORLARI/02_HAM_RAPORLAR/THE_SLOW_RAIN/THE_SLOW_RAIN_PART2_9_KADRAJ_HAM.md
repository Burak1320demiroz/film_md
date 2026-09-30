INPUT MODE: D
FILM: THE_SLOW_RAIN (Part 1 of 2 — S00–S23)
RUNTIME: 04:00
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0 s + (n−1) × 10 s (S00–S23, 24 clips × 10 s)
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: 111111111111111111111111
LINES HEARD: none — room tone and environment ambience present
SETUPS REGISTERED: 10 distinct camera positions
LOCKOFF HELD: 24 / 24 clips

## SETUP LEDGER

S00 | 00:05 | A | CU / eye / normal / frontal | A | MATCH | dome on ridge right third | 0
S01 | 00:15 | C | ECU / eye / long / frontal face | C | MATCH | visor frame centered | 0
S02 | 00:25 | R | WS / low-eye / wide / rear-side pool | R | MATCH | pool edge right | 0
S03 | 00:35 | J | MS / eye / normal / side pool | J | MATCH | pool rim left-center | 0
S04 | 00:45 | R | WS / low-eye / wide / rear-side pool | R | MATCH | pool edge right | 0
S05 | 00:55 | B | MCU / eye / normal / 3/4 front chest | B | MATCH | chest buckle | 0
S06 | 01:05 | B | MS / low / normal / 3/4 kneeling ground | K | MISS | ground keg center | 0
S07 | 01:15 | G | WS / eye / wide / side profile walking | G | MATCH | horizon dome right | 0
S08 | 01:25 | G | WS / eye / wide / side profile walking | G | MATCH | horizon dome right | 0
S09 | 01:35 | I | WS / eye / wide / side-on stream | I | MATCH | winding liquid shore | 0
S10 | 01:45 | K | MCU / low / normal / front kneeling | K | MATCH | keg on ground center | 0
S11 | 01:55 | I | MCU / eye / normal / side profile holding keg | P | MISS | helmet collar | 0
S12 | 02:05 | G | WS / low-eye / wide / rear view walking away | N | MISS | distant dome center | 0
S13 | 02:15 | G | WS / low-eye / wide / rear view walking away | N | MISS | distant dome center | 0
S14 | 02:25 | N | WS / low-eye / wide / rear view walking away | N | MATCH | distant dome center | 0
S15 | 02:35 | O | MS / low / normal / 3/4 front kneeling | O | MATCH | rig/strap on ground | 0
S16 | 02:45 | P | CU / eye / normal / side profile | P | MATCH | helmet neck ring | 0
S17 | 02:55 | O | MS / low / normal / 3/4 front kneeling | O | MATCH | rig/strap on ground | 0
S18 | 03:05 | P | CU / eye / normal / side profile | P | MATCH | helmet neck ring | 0
S19 | 03:15 | O | MS / low / normal / 3/4 front kneeling | O | MATCH | rig/strap on ground | 0
S20 | 03:25 | Q | CU / low / normal / tight hands buckle | Q | MATCH | chest buckle | 0
S21 | 03:35 | O | MS / low / normal / 3/4 front kneeling | O | MATCH | rig/strap on ground | 0
S22 | 03:45 | N | WS / low-eye / wide / rear view walking away | N | MATCH | distant dome center | 0
S23 | 03:55 | R | WS / low-eye / wide / rear-side pool | R | MATCH | pool edge right | 0

## SETUP STRING

```
OBSERVED:   ACRJRBKGGIKPNNNOPOPQONR
PLAN:       ACRJRBBGIKIGGNOPOPOQONR
DIFFERS AT: S06, S11, S12, S13
```

## PRESENCE STRING

```
111111111111111111111111
```

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / CU / eye-level frontal / dome right / glove raised | R / WS / low-angle rear-side / pool edge right / leaning at pool | No (setup A vs R) |

PAIR FAILS — Part 1 of 2 file ends on mid-film boundary setup R (S23) rather than closing rhyme setup A (planned for S47 at end of Part 2).

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| all held |  |  |  |  |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 6/10 | 🔴 S06 (01:05) MISS [K instead of B], 🔴 S11 (01:55) MISS [P instead of I], 🔴 S12 (02:05) MISS [N instead of G], 🔴 S13 (02:15) MISS [N instead of G] |
| 2 | Lockoff Integrity | 10/10 | None (all 24 clips held lockoff without drift or creep) |
| 3 | Rhyme Pair | 5/10 | 🟠 S00 (00:05) vs S23 (03:55) setup mismatch (A vs R) due to Part 1 split boundary |
| 4 | Return Consistency | 8/10 | 🟡 S06 (01:05) misrenders setup B as K, causing anchor conflict with true setup K at S10 (01:45) |
| 5 | Cluster Seams | 6/10 | 🔴 S05 ↔ S06 (01:00) seam jump (MCU chest B breaks to kneeling MS K across cluster) |
| 6 | Angle Arc & Deliberate Shocks | 8/10 | 🟡 S11 (01:55) unplanned scale collapse from WS profile to MCU profile |
| 7 | Screen Geometry | 9/10 | None (screen direction and world anchor positions stable) |

VERDICT: SETUP BROKEN

## THE THREE THAT MATTER

1. **01:00 (S06)** — Cluster seam break S05↔S06: Setup B jumps from MCU chest shot to kneeling MS (K). *Fix: Regenerate S06 retaining exact MCU chest camera setup from S05.*
2. **02:00–02:20 (S12–S13)** — Angle flip G→N: Profile walking setups rendered as rear-view walking away. *Fix: Regenerate S12 and S13 with camera locked to side-profile setup G.*
3. **01:50 (S11)** — Scale collapse I→P: Planned wide shot along liquid stream rendered as MCU side profile. *Fix: Regenerate S11 with wide lens framed on winding stream.*

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration:** S06, S11, S12, and S13 camera setup mismatches represent fundamental perspective changes that cannot be adjusted in post-production.
* **Fixable in Edit:** Lockoff integrity across all clips is 100% stable; no optical stabilization or cropping required.

## FLAGS FOR DOCUMENT CHECK

* SPEC indicates S23↔S24 is a boundary cluster sharing Setup R. Confirm whether Part 2 master seamlessly connects to S23's end frame without frame step.

## OUT-OF-SCOPE FLAGS

* **CONTINUITY:** Liquid level in dark pool varies slightly between S02 and S04.
* **ACTION / EFFORT:** S02 rope tension does not show physical recoil on release.
