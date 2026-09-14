# THE_STATIC_SHADOW — ⑨ KADRAJ · HAM RAPOR

> alındı: 13.09.2026 · girdi: (tam yol BİLİNMİYOR — operatör yazmadı) · master depoda/diskte bulunamadı · INPUT MODE: V
> ⛔ ⑨ MOD V'DE GEÇERSİZ, tekrar değil [D190] — KARANTİNA: T9'a satır yok, ders/sipariş üretmez · model çıktısı olduğu gibi, düzenlenmedi

---

INPUT MODE: V
FILM: THE STATIC SHADOW
RUNTIME: 02:05 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 12 · CUTS COUNTED: 12 · CUTS OFF GRID: none (mode V)
NON-SCENE MATERIAL: 02:00–02:05 title card ("THE STATIC SHADOW")
PRESENCE STRING: -111---1-1-1
LINES HEARD: none — synth ambient audio track present
SETUPS REGISTERED: 11 distinct camera positions
LOCKOFF HELD: 12 / 12 clips

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  6        (N/A excluded, never 0)
SUM OF SCORES:      54.0
DIVISION:           54.0 ÷ 6 = 9.0      ← this is OVERALL SCORE

OVERALL SCORE: 9.0/10
VERDICT: RHYME BROKEN

## SETUP LEDGER

S1 | 00:05 | N/A | EWS / eye level / wide lens feel / exterior space station & solar panel | A | N/A (mode V) | solar array edge & cylinder sub-assembly | 0

S2 | 00:15 | N/A | MCU / eye level / normal lens feel / interior cockpit OTS behind pilot facing window | B | N/A (mode V) | windshield frame struts | 0

S3 | 00:25 | N/A | MCU / eye level / normal lens feel / frontal centered view of pilot helmet | C | N/A (mode V) | helmet collar ring | 0

S4 | 00:35 | N/A | ECU / high 45° angle / normal lens feel / pilot gloved hand on joystick | D | N/A (mode V) | joystick base & console panel | 0

S5 | 00:45 | N/A | WS / axial eye level / wide lens feel / capsule firing thrusters through octagonal ring | E | N/A (mode V) | octagonal docking frame | 0

S6 | 00:55 | N/A | WS / low side angle / wide lens feel / capsule docked to solar panel array | F | N/A (mode V) | solar panel edge seam | 0

S7 | 01:05 | N/A | ECU / low side angle / macro lens feel / docking probe tip contact point | G | N/A (mode V) | docking latch rail | 0

S8 | 01:15 | N/A | MCU / low rear-left OTS / normal lens feel / interior cockpit (red lighting) | H | N/A (mode V) | left window frame pillar | 0

S9 | 01:25 | N/A | WS / high angle / wide lens feel / capsule on dark solar panel (electrical flash) | I | N/A (mode V) | panel top edge | 0

S10 | 01:35 | N/A | MCU / eye level / normal lens feel / frontal centered view of pilot helmet | C | N/A (mode V) | helmet collar ring | 0

S11 | 01:45 | N/A | WS / dutch low angle / wide lens feel / capsule scraping solar array with sparks | K | N/A (mode V) | panel diagonal rail | 0

S12 | 01:55 | N/A | MCU / rear-right OTS / normal lens feel / interior cockpit (green lighting) | L | N/A (mode V) | right console frame pillar | 0

## SETUP STRING

```
OBSERVED:   ABCDEFGHCKSL
PLAN:       none (mode V)
DIFFERS AT: none (mode V)

```

## PRESENCE STRING

`-111---1-1-1`

## RHYME PAIR

|  | First frame (00:05) | Last frame (01:55) | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | Setup A / EWS / Eye-level exterior / Solar array edge & cylinder / N/A | Setup L / MCU / Interior rear-right OTS / Right console frame pillar / N/A | No |

Verdict line: `PAIR FAILS` — The opening frame is an exterior wide shot of the space station, whereas the closing frame is an interior cockpit over-the-shoulder shot, failing setup type, subject scale, and anchor parity.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| all held |  |  |  |  |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V — no written spec supplied |
| 2 | Lockoff Integrity | 10/10 | no in-scope source |
| 3 | Rhyme Pair | 4/10 | S1 (00:00–00:10) vs S12 (01:50–02:00): setup mismatch (exterior EWS vs interior MCU OTS) |
| 4 | Return Consistency | 10/10 | no in-scope source |
| 5 | Cluster Seams | 10/10 | no in-scope source |
| 6 | Angle Arc & Deliberate Shocks | 10/10 | no in-scope source |
| 7 | Screen Geometry | 10/10 | no in-scope source |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 0   🟡 MINOR: 0

## THE THREE THAT MATTER

1. [00:00 vs 01:50] 🔴 RHYME PAIR FAILURE: The film starts on exterior wide Setup A and ends on interior cockpit Setup L, breaking bookend framing symmetry. Fix: Cut back to Setup A after S12 or append an exterior bookend shot.
2. [01:10 vs 01:50] 🟡 COCKPIT OTS ANGLE VARIATION: Cockpit interior shots shift across three distinct camera positions (S2 center, S8 left low, S12 right) rather than maintaining a unified master OTS position. Fix: Standardize cockpit OTS camera coordinates across interior scenes.
3. 🟡 HUD VISOR RETICLE DISAPPEARANCE: Returning Setup C in S10 lacks the target reticle graphic overlay present in S3. Fix: Composite matching reticle element onto visor in post.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Rhyme Pair Failure**: Fixable in edit by trimming/moving S1 to the end or inserting a generated exterior Setup A clip after S12.
* **HUD Reticle Discontinuity**: Fixable in edit via 2D graphic tracking overlay on S10.
* **Lockoff Stabilization**: All 12 shots held locked off; no post-stabilization or frame re-centering required.

## FLAGS FOR DOCUMENT CHECK

* Mode V run: Confirm whether S2, S8, and S12 were planned as distinct setups or intended as returns to a single cockpit OTS setup.
* Confirm whether HUD reticle in S3/S10 was intended to toggle off dynamically during flight operations.

## OUT-OF-SCOPE FLAGS

* LIGHTING: Solar panel arc flash introduces an abrupt step-change in local key illumination.
* ACTION: Gloved hand joystick displacement lacks dynamic mechanical resistance recoil.
* PHYSICS: Collision debris particles drift smoothly without micro-impact angular velocity scattering.
