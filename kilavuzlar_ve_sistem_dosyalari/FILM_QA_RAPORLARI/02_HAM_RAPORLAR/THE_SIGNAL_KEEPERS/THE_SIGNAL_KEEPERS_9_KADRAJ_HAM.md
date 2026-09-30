INPUT MODE: D
FILM: THE_SIGNAL_KEEPERS
RUNTIME: 04:00 (240.0 s measured)
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: clip(n) start = (n−1) × 10.0 s (0.0 s to 230.0 s)
SCENES OBSERVED: 24 · CUTS COUNTED: 23 · CUTS OFF GRID: none
NON-SCENE MATERIAL: none
PRESENCE STRING: 111111-11-111111-1111111
LINES HEARD: 2 · "If anyone hears this... We are here." at 00:12 (broken) and 02:52 (clean)
SETUPS REGISTERED: 12 distinct camera positions (A through L)
LOCKOFF HELD: 24 / 24 clips

## SETUP REGISTER

· A | WS | eye level | normal | behind astronaut on cliff edge | anchor: cliff rim & ringed planet horizon
· B | MCU | eye level | normal | frontal view facing astronaut torso/helmet | anchor: visor rim & shoulder sphere seat
· C | MS-MCU | low angle | normal | tracking lower body through plant field | anchor: suit boots & glowing plant stems
· D | ECU | top-down | wide | overhead view of ground flora/stone floor | anchor: green leaf on dark rock floor
· E | MCU | eye level | normal | close-up on visor and astronaut face | anchor: visor frame & shoulder sphere
· F | ECU | eye level | normal | tight face frame inside visor | anchor: eyes & upper visor rim
· G | CU | ground level | low angle | mineral hands resting on dark stone | anchor: mineral hands & dark rock floor
· H | MS | eye level | normal | archway framing astronaut & tall figure | anchor: archway pillars & distant city skyline
· I | MCU | low angle | normal | looking up at fluted dark monolith | anchor: monolith base & planet sky
· J | MS | eye level | normal | behind suit facing monolith entrance | anchor: monolith entrance arch
· K | MCU | low angle | normal | control panel / cradle ring assembly | anchor: panel edge & cradle rings
· L | MCU | eye level | normal | suit shoulder socket / probe interface | anchor: shoulder socket rim

## SETUP LEDGER

S01 | 00:00 | A | WS / eye level / normal / behind suit on cliff | A | MATCH | cliff edge & planet ring | 0
S02 | 00:10 | B | MCU / eye level / normal / frontal torso & helmet | B | MATCH | visor rim & shoulder sphere | 0
S03 | 00:20 | A | WS / eye level / normal / behind suit on cliff | A | MATCH | cliff edge & planet ring | 0
S04 | 00:30 | C | MCU / low angle / normal / lower body walking in flora | C | MATCH | boots & plant stems | 0
S05 | 00:40 | D | ECU / top-down / wide / gloved hand touching leaf | D | MATCH | leaf & rock surface | 0
S06 | 00:50 | C | MS / low angle / wide / behind suit facing tall figure | C | NEAR (wider MS framing) | plant field & pillars | 0
S07 | 01:00 | D | ECU / top-down / wide / leaves on dark stone floor | D | MATCH | leaves & dark stone floor | 0
S08 | 01:10 | E | MCU / eye level / normal / suit walking forward | E | MATCH | visor rim & horizon line | 0
S09 | 01:20 | F | ECU / eye level / normal / tight face frame in visor | F | MATCH | visor rim & eyes | 0
S10 | 01:30 | G | CU / ground level / low angle / mineral hands on rock | G | MATCH | mineral hands & dark floor | 0
S11 | 01:40 | F | ECU / eye level / normal / visor close-up with sphere | F | MATCH | visor rim & blue sphere | 0
S12 | 01:50 | E | WS / eye level / normal / rear facing monolith wall | J | MISS (E WS rear view instead of MCU visor) | monolith wall & sky | 0
S13 | 02:00 | H | MS / eye level / normal / archway with dark figure | H | MATCH | archway pillars & city | 0
S14 | 02:10 | I | MCU / low angle / normal / looking up at monolith | I | MATCH | monolith base & sky | 0
S15 | 02:20 | H | MS / eye level / normal / archway with figure & suit | H | MATCH | archway pillars & city | 0
S16 | 02:30 | J | MS / eye level / normal / suit facing monolith entry | J | MATCH | monolith entrance | 0
S17 | 02:40 | K | MCU / eye level / normal / visor close-up in hall | E | NEAR (MCU visor setup E framing) | visor rim & hall background | 0
S18 | 02:50 | E | MCU / eye level / normal / visor frame listening | E | MATCH | visor rim & shoulder sphere | 0
S19 | 03:00 | K | MCU / low angle / normal / hand near panel | K | MATCH | panel edge & mineral hand | 0
S20 | 03:10 | E | MCU / eye level / normal / visor frame on reaction | E | MATCH | visor rim & shoulder sphere | 0
S21 | 03:20 | K | MCU / low angle / normal / cradle panel rings | K | MATCH | cradle rings & panel edge | 0
S22 | 03:30 | E | MCU / eye level / normal / visor frame watching rings | E | MATCH | visor rim & lighting shift | 0
S23 | 03:40 | L | MCU / eye level / normal / placing sphere in socket | L | MATCH | probe socket & gloved hand | 0
S24 | 03:50 | G | CU / ground level / low angle / mineral hands holding sphere | G | MATCH | mineral hands & blue sphere | 0

## SETUP STRING

```
OBSERVED:   A B A C D C D E F G F J H I H J E E K E K E L G
PLAN:       A B A C D C D E F G F E H I H J K E K E K E L G
DIFFERS AT: S12, S17

```

Length of OBSERVED = 24. SCENES OBSERVED = 24. Counts match.

## PRESENCE STRING

`111111-11-111111-1111111`

## RHYME PAIR

|  | First frame (S01, 00:00) | Last frame (S24, 03:50) | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / WS / eye level / cliff edge & planet ring / astronaut on cliff | G / CU / ground level / mineral hands holding blue sphere / whole sphere vs empty hands | No (A vs G) |

Verdict line: `PAIR FAILS` — While the film contains an internal camera loop between K10 and K24 (Setup G), the outer boundary frames S01 (Setup A) and S24 (Setup G) do not share the same camera setup.

## LOCKOFF VERIFICATION

all held

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 8/10 | S12 (01:50) MISS — plan specified E (MCU visor), observed J/WS rear view. S17 (02:40) NEAR — plan K (MCU panel), observed E (MCU visor).

 |
| 2 | Lockoff Integrity | 10/10 | None. All 24 clips held lockoff without drift, creep, or re-centering.

 |
| 3 | Rhyme Pair | 5/10 | Outer frame pair (S01 00:00 vs S24 03:50) uses different setups (A vs G).

 |
| 4 | Return Consistency | 9/10 | Setup returns (A, C, D, E, F, H, J, K, G) exhibit rock-solid anchor stability and lens consistency.

 |
| 5 | Cluster Seams | 10/10 | Intra-scene cuts maintain seamless horizon, scale, and spatial alignment across boundaries.

 |
| 6 | Angle Arc & Deliberate Shocks | 10/10 | Scale steps are smooth and planned without unintended scale jumps or Dutch angles.

 |
| 7 | Screen Geometry | 10/10 | Left/right third orientation, horizon level, and subject spatial axes are fully preserved.

 |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **01:50 (S12)** — Silent Reframe / Setup Miss: S12 delivered a wide shot facing the monolith instead of the planned E setup (MCU visor). *Fix: Regenerate S12 with prompt explicitly enforcing tight MCU eye-level visor framing.*


2. **00:00 vs 03:50 (S01 ↔ S24)** — Rhyme Pair Setup Discrepancy: The outer file boundary opens on Setup A (WS cliff view) and closes on Setup G (Ground-level CU). *Fix: Align closing frame setup or structure outer file boundary if an exact camera rhyme was intended across outer limits.*


3. **02:40 (S17)** — Near Setup Drift: S17 defaulted to an MCU visor shot (Setup E) instead of low-angle control panel setup (Setup K). *Fix: Adjust S17 framing prompt to focus tightly on control panel interface.*



## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **S12 (Setup Miss at 01:50)**: Requires regeneration. Post-production cropping from a wide shot to an MCU visor frame introduces severe resolution degradation and perspective distortion.
* **S17 (Near Setup at 02:40)**: Requires regeneration if the low-angle panel perspective (Setup K) is required for story clarity.
* **Lockoff & Geometry**: Zero post-stabilization required; all clips held fixed position.



## FLAGS FOR DOCUMENT CHECK

* **S12 Setup Specification**: Verify whether S12 was intended to bridge S11 (ECU visor) and S13 (MS archway) with an MCU visor shot or if the wide monolith establishing view was an intentional edit variation in production.



## OUT-OF-SCOPE FLAGS

* **CONTINUITY**: Bioluminescent plant density between S04 and S06 shows slight variance.


* **LIGHT**: Ringed planet fill light intensity increases slightly between S03 and S08.
