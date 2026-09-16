INPUT MODE: V
FILM: (not supplied)
RUNTIME: 02:59
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 18 · CUTS COUNTED: 17 (00:10, 00:20, 00:30, 00:40, 00:50, 01:00, 01:10, 01:20, 01:30, 01:40, 01:50, 02:00, 02:10, 02:20, 02:30, 02:40, 02:50)
NON-SCENE MATERIAL: none
PRESENCE STRING: -11--111--11111111
LINES HEARD: 7 · "Orientation aligned. Horizon locked." (00:02), "Sling secured. Manual override ready." (00:10), "Disruptor, Horizon Station. Maintain approach vector." (00:21), "Guidance data is unreliable." (00:48), "Switching to manual attitude control." (00:51), "Horizon distance to lock 42." (01:08), "0.15 meters per second. Line is true." (01:36)
ACTS LOGGED: 15
ACTS MISSED: 11 HIT · 2 MISS · 1 UNKNOWN · 0 NO TARGET · 1 FLIP
PREMISE REGISTER: Zero-g space environment; docking target established screen-right in space view; internal orientation established relative to cockpit flight instruments.

## TARGET LEDGER

V1 | 00:00–00:10 | GO | screen-R toward space station | Station at screen-R (00:00) | HIT | The spacecraft maneuvers screen-right toward the station established screen-right at 00:00.

V2 | 00:10–00:20 | REACH / TOGGLE | right hand to console screen-R | Switch panel at screen-R (00:13) | HIT | He reaches screen-right toward the control panel established screen-right at 00:13.

V3 | 00:20–00:30 | GO | screen-R toward docking ring | Docking ring at screen-R (00:20) | HIT | The spacecraft travels screen-right directly toward the station docking hub.

V4 | 00:30–00:40 | GO | into depth toward tunnel center | Circular docking hatch centered in frame (00:30) | HIT | The craft advances into depth straight toward the circular docking mechanism.

V5 | 00:40–00:50 | LOOK | screen-R at telemetry HUD | Monitor at screen-R (00:40) | HIT | He looks screen-right at the flight telemetry display established screen-right at 00:40.

V6 | 00:50–01:00 | REACH / TOGGLE | left hand to safety cover / switch screen-L | Switch panel screen-L (00:50) | HIT | She flips safety switch cover screen-left where panel controls sit at 00:50.

V7 | 00:58–01:00 | LOOK | screen-L at co-pilot screen | Co-pilot console screen-L (00:50) | UNKNOWN | He looks screen-left across cockpit; her HUD display was not previously established on his screen side.

V8 | 01:00–01:10 | AIM / LOOK | into alignment scope depth | Station hatch through optical sight (01:03) | HIT | He looks through the optical scope aimed directly at the station crosshairs at 01:03.

V9 | 01:10–01:20 | FIRE / THRUST | thrusters fire downward / craft adjusts screen-R | Station port at screen-R (01:10) | HIT | Thrusters vent downward to align vector with docking collar screen-right at 01:10.

V10 | 01:20–01:30 | REACH / DRIVE | right hand pulling control stick back / screen-L | Flight stick screen-L (01:20) | HIT | She operates joystick control situated screen-left at 01:20.

V11 | 01:30–01:40 | GO | screen-R toward docking target | Docking port screen-R (01:30) | HIT | The docking probe moves screen-right toward female receiver screen-right at 01:30.

V12 | 01:40–01:50 | GO | into depth / screen-R | Docking collar mechanism (01:40) | HIT | Probe penetrates locking ring along established horizontal axis at 01:40.

V13 | 01:50–02:00 | REACH / GO | outer clamps swing screen-R to wrap collar | Ship hull screen-L, station collar screen-R (01:50) | HIT | Heavy mechanical clamps extend screen-right to secure the craft collar at 01:50.

V14 | 02:20–02:30 | WALK / ENTER | screen-L to screen-R through airlock hatch | Outer chamber hatch screen-R (02:20) | FLIP | She walks screen-right into airlock, but cut lands with her entering from screen-left across identical threshold at 02:20.

V15 | 02:50–02:59 | REACH / TOUCH | left arm reaches screen-R toward co-pilot shoulder | Co-pilot sitting screen-R (02:50) | MISS | She reaches screen-right toward co-pilot shoulder, but her hand lands on air rather than making physical contact at 02:54.

## PRESENCE STRING

`-11--111--11111111`

## VECTOR STRING

`HHHHH?HHHHHHHHmHHm`

## SCORES SUMMARY

| # | Category | Score | Issue (with ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Target Establishment | 9/10 | 🟡 V7 (00:58) — Target display cross-view not explicitly established prior to look. |
| 2 | Look Direction | 9/10 | 🟡 V7 (00:58) — Eyeline across co-pilot console relies on unestablished off-screen target. |
| 3 | Turn & Travel Direction | 10/10 | All spatial travel vectors hit established screen positions cleanly. |
| 4 | Reach & Aim | 7/10 | 🟠 -3 · V15 (02:54) — Reach toward co-pilot shoulder misses physical contact target. |
| 5 | Fire · Trigger · Throw · Release | 10/10 | Thruster bursts and docking probe extensions align precisely with target vectors. |
| 6 | Screen Direction Across Cuts | 6/10 | 🔴 -4 · V14 (02:20) — Airlock entry flips movement axis from screen-right to screen-left across cut. |
| 7 | Camera-Relative Sense | 10/10 | In-depth and lateral camera axes remain consistent relative to spacecraft geometry. |
| 8 | Consequence on Target | 9/10 | 🟡 V15 (02:54) — Intended contact gesture fails to connect with recipient's suit. |

VERDICT: FIXABLE IN EDIT

## MISSED VECTORS TABLE

| Timecode | Act | Vector on screen | Target and where it was (tc) | Match | Pattern (①–⑭) | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| 00:58 | LOOK | screen-L at co-pilot screen | Co-pilot HUD display unestablished | UNKNOWN | ⑪ | 🟡 LOW |
| 02:20 | WALK | screen-L to screen-R | Airlock interior hatch at 02:20 | FLIP | ① | 🔴 HIGH |
| 02:54 | REACH | arm extends screen-R | Co-pilot shoulder at 02:50 | MISS | ⑤ | 🟠 MED |

## PROMPT ORDERS FOR THE NEXT FILM

| # | Pattern | Act that missed (tc) | The prompt line that would have prevented it | Confidence |
| --- | --- | --- | --- | --- |
| 1 | ① | Walk (02:20) | The character enters the airlock walking screen-left to screen-right, maintaining left-to-right travel across the cut. | HIGH |
| 2 | ⑤ | Reach (02:54) | She extends her left hand screen-right and rests her glove firmly on the co-pilot's upper shoulder arm pad. | HIGH |

## CONTRADICTION LOG

* 02:20 (Scene 15 airlock entry): Character walks screen-right through open hatch door, but inner frame reveals her stepping in from screen-left boundary without camera crossing cue. (Scored under Screen Direction Across Cuts / Pattern ①).

## THE THREE THAT MATTER

1. **02:20 (Airlock Screen Direction Flip)**: Mirror shot 02:20 horizontal orientation so entry travel flows continuously from screen-left to screen-right.
2. **02:54 (Unconnected Shoulder Reach)**: Trim 2 seconds off the end of shot 02:50 before hand reaches empty space, ending on static seated rest.
3. **00:58 (Ambiguous Eyeline Look)**: Cut 1 second earlier at 00:57 to avoid unestablished gaze shift off-screen left.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Fixable in Edit**:
* Horizontal flip of scene at 02:20 to restore left-to-right airlock travel continuity across the cut.
* Tail trim on shot 02:50 (02:54–02:59) to cut prior to missed shoulder reach.


* **Requires Regeneration**:
* Re-rendering shot 02:50 if physical contact between astronaut glove and co-pilot suit shoulder is required narrative action.

## FLAGS FOR DOCUMENT CHECK

* 00:58 — Pilot looks screen-left across console — QUESTION: Does the document specify co-pilot telemetry screen mirror on left panel?

## OUT-OF-SCOPE FLAGS

* **CONTINUITY (Lens ②)**: Astronaut suit chest patch design shifts slightly between cockpit shot (00:40) and airlock scene (02:20).
* **ACTION (Lens ⑦)**: Docking probe speed in shot 01:40 lacks deceleration weight before mechanical catch.
