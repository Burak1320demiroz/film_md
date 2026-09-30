INPUT MODE: D
FILM: THE_FALLING_WORLD (PART 1 & 2 / S00-S22)
RUNTIME: 03:49 measured (~04:00 planned for S00-S23)
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: hook 0.0 s + (n−1) × 10.0 s · 10.0 s fixed grid
SCENES OBSERVED: 23 · CUTS COUNTED: 22 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: 11111111111111111111111
LINES HEARD: 3 · "Sector 7 clear" (02:31), "Pressurizing" (03:32), "Auto lock system" (03:35)
SETUPS REGISTERED: 8 distinct camera positions (A, B, C, E, G, H, I, K, L, M)
LOCKOFF HELD: 19 / 23 clips

## SETUP LEDGER

| Scene | in | plan letter | observed size / angle / lens / position | observed letter | MATCH · NEAR · MISS | anchor position | in-clip movement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S00 | 00:00 | A | ECU / high angle / normal / above rail | A | MATCH | rail post & knot | 0 |
| S01 | 00:10 | B | EWS / eye level / wide / chasm view | B | MATCH | chasm edge & rail | 0 |
| S02 | 00:20 | B | MCU / eye level / normal / rock wall | C | MISS | cliff rock face | creep (00:25) |
| S03 | 00:30 | A | EWS / eye level / wide / chasm view | B | MISS | chasm edge & rail | 0 |
| S04 | 00:40 | C | MCU / eye level / normal / rock wall | C | MATCH | cliff rock face | 0 |
| S05 | 00:50 | E | ECU / high angle / normal / glove grip | E | MATCH | wrist & glove joint | 0 |
| S06 | 01:00 | E | WS / low angle / wide / lander exterior | I | MISS | lander legs & ramp | drift (01:04) |
| S07 | 01:10 | C | CU / top-down / normal / ring hatch | G | MISS | yellow ring plate | 0 |
| S08 | 01:20 | F | WS / low angle / wide / lander exterior | I | MISS | lander ramp & pad | 0 |
| S09 | 01:30 | G | CU / top-down / normal / hatch cover | G | MATCH | metal hatch plate | 0 |
| S10 | 01:40 | F | CU / high angle / normal / valve lever | H | MISS | lever shaft | 0 |
| S11 | 01:50 | F | EWS / eye level / wide / chasm shake | B | MISS | chasm wall | shake (01:52) |
| S12 | 02:00 | I | MCU / eye level / normal / corridor | K | MISS | interior bulkhead | 0 |
| S13 | 02:10 | I | MCU / eye level / normal / corridor | K | MATCH | interior bulkhead | 0 |
| S14 | 02:20 | K | MCU / eye level / normal / interior | K | MATCH | interior frame | 0 |
| S15 | 02:30 | K | MCU / eye level / normal / interior | K | MATCH | visor & panel | 0 |
| S16 | 02:40 | L | MCU / low angle / normal / airlock duct | L | MATCH | duct wall | 0 |
| S17 | 02:50 | L | MCU / low angle / normal / airlock duct | L | MATCH | duct wall | 0 |
| S18 | 03:00 | K | CU / high angle / normal / console hand | M | MISS | console lever | 0 |
| S19 | 03:10 | M | CU / high angle / normal / console hand | M | MATCH | console lever | 0 |
| S20 | 03:20 | N | EWS / eye level / wide / chasm collapse | B | MISS | chasm edge | shake (03:22) |
| S21 | 03:30 | O | MCU / eye level / normal / corridor | K | MISS | visor & interior | 0 |
| S22 | 03:40 | N | MCU / eye level / normal / airlock | K | MISS | airlock door frame | 0 |

## SETUP STRING

```
OBSERVED:   A B C B C E I G I G H B K K K K L L M M B K K
PLAN:       A B B A C E E C F G F F I I K K L L K M N O N
DIFFERS AT: S02, S03, S06, S07, S08, S10, S11, S12, S13, S18, S20, S21, S22
```

## PRESENCE STRING

`11111111111111111111111`

## RHYME PAIR

|  | First frame (S00) | Last frame (S22) | Same? |
| --- | --- | --- | --- |
| setup / size / angle / anchor / variable | A / ECU / high / rail post / knot tying | K / MCU / eye / door frame / corridor walking | No |

VERDICT: RHYME BROKEN — Opening ECU knot framing (A) does not match closing MCU interior corridor framing (K).

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S02 | Locked off | MCU cliff wall | 00:25 | Camera creep |
| S06 | Locked off | WS lander | 01:04 | Handheld drift |
| S11 | Locked off | EWS chasm | 01:52 | Camera shake |
| S20 | Locked off | EWS collapse | 03:22 | Camera shake |

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | 4/10 | 13 scenes MISS plan setup string (S02, S03, S06-S08, S10-S13, S18, S20-S22) |
| 2 | Lockoff Integrity | 7/10 | In-clip camera drift/shake in S02 (00:25), S06 (01:04), S11 (01:52), S20 (03:22) |
| 3 | Rhyme Pair | 2/10 | Opening ECU rope (A) vs closing MCU corridor (K) fails framing rhyme |
| 4 | Return Consistency | 5/10 | Returning setup B (S03, S11, S20) exhibits shifting anchor positions |
| 5 | Cluster Seams | 4/10 | Declared clusters S01-S02, S05-S06, S10-S11 show setup jump cuts |
| 6 | Angle Arc & Deliberate Shocks | 5/10 | Unplanned 2-step scale jumps across S01->S02, S02->S03, S05->S06 |
| 7 | Screen Geometry | 6/10 | Anchor positions drift across wide setup repeats (S03, S11, S20) |

VERDICT: SETUP BROKEN

## THE THREE THAT MATTER

1. **00:20 (S02)** — Delivered MCU cliff face instead of planned EWS chasm (B). Fix: Regenerate S02 with locked-off EWS chasm prompt.
2. **01:00 (S06)** — Delivered WS lander (I) instead of planned CU wrist grip (E). Fix: Regenerate S06 specifying close-up glove lockoff.
3. **03:40 (S22)** — Final frame failed to return to opening setup A. Fix: Regenerate S22 using setup A parameters to hold the rhyme pair.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Requires Regeneration:** All setup mismatches (S02, S03, S06-S08, S10-S13, S18, S20-S22) cannot be repositioned in post and require prompt re-renders.
* **Fixable in Edit:** Minor camera creep/shake in S02 and S06 can be post-stabilized at a minor resolution crop cost.

## FLAGS FOR DOCUMENT CHECK

* Document names 48 scenes total; video payload provides 23 scenes (PART 1 & 2 subset).

## OUT-OF-SCOPE FLAGS

* **CONTINUITY:** Forearm repair tape missing on white suit in S02.
* **LIGHTING:** Key light direction shifts between S01 and S03 chasm shots.
