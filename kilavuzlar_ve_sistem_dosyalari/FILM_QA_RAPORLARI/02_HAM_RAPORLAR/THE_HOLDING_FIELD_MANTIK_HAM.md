# 🧩 THE HOLDING FIELD — MANTIK_QA HAM ÇIKTI

> ⚠️ **DOKUNULMAZ.** Model çıktısı olduğu gibi, düzenlenmeden kaydedildi
> (AGENTS kural ④). Özet ve belge kontrolü cevapları ayrı dosyada:
> `../01_FILM_RAPORLARI/THE_HOLDING_FIELD.md`
>
> **Çalıştırma tarihi:** 03.08.2026
> **Rubrik:** `../../QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Girdi:** yalnız video (rubrik doküman istemez)
> **Videodaki başlık:** "The Shift" — üretim sırasındaki geçici ad.
> Depodaki kanonik ad **THE HOLDING FIELD**'dır; sahne envanteri plan
> dosyasıyla birebir eşleşiyor (bkz. film kaydı §1).

---

```
FILM: The Shift
RUNTIME: 02:14 · SCENES OBSERVED: 13
BASELINE: SELF-CONSISTENCY
This review answers "does the film agree with itself?"
It does NOT answer "does the film match its design?"

OVERALL SCORE: 4/10
VERDICT: STRUCTURAL PROBLEM
The physical rules of gravity fundamentally contradict themselves from scene
to scene, collapsing the world's logic.

SCENE INVENTORY
#   In-out       Location       Present            What happens                                              Dialogue
1   0:00-0:10    Landing Site   Ship               Ship lands, a side panel breaks and falls to the ground.   None
2   0:10-0:20    Landing Site   Astronaut          Astronaut walks down ramp; a rock falls heavily to the
                                                   ground.                                                   None
3   0:20-0:30    Landing Site   Astronaut          Astronaut kicks a rock; other rocks float upwards in
                                                   background.                                               None
4   0:30-0:40    Landing Site   Ship, Astronaut    Ship hovers and leaves; ground is clear of previous
                                                   debris.                                                   None
5   0:40-0:50    Debris Field   Astronaut          Astronaut touches floating rocks suspended in mid-air.     None
6   0:50-1:00    Pillars        Astronaut, Figure  Astronaut walks; a second dark figure appears left, then
                                                   vanishes.                                                 None
7   1:00-1:10    White Pillar   Astronaut          Astronaut watches dust/debris fall downwards from pillar.  None
8   1:10-1:20    White Pillar   Astronaut          Astronaut examines a 3-pronged mechanical dial.            None
9   1:20-1:30    Pillars        Astronaut          Astronaut drops a handful of sand; it falls downwards.     None
10  1:30-1:40    Sky View       Astronaut          POV looking up; debris and rocks float upwards into the
                                                   sky.                                                      None
11  1:40-1:50    White Pillar   Astronaut          Astronaut touches a smooth, dial-less section of the
                                                   pillar.                                                   None
12  1:50-2:00    White Pillar   Astronaut          Astronaut turns a 1-handled dial with a lit rim.           None
13  2:00-2:10    Landing Site   Astronaut          Astronaut walks among floating rocks; ship is parked in
                                                   background.                                               None

SCORES SUMMARY
Category                Score    Critical Issue
Physical Consistency    3/10     Gravity randomly flips between normal (falling) and inverted (floating)
                                 across scenes.
Counter Logic           N/A      NONE
Spatial Geography       3/10     Ship leaves in S4 but reappears parked in S13.
Time & Light Logic      7/10     Sun angle, shadows, and atmosphere remain relatively steady.
State, Costume & Props  3/10     The pillar dial completely changes its physical geometry and design.
Causality & Knowledge   4/10     A phantom second astronaut appears and vanishes without cause.
Quantity Consistency    4/10     Dial prongs shift from 3 to 1; astronaut count shifts from 2 to 1.
Setup & Abandonment     4/10     Ship panel falls off in S1 and is instantly abandoned in subsequent
                                 wide shots.

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 2   🟡 MINOR: 1

COUNTER CURVE
NONE

LOCATION MAP
Location             Scenes         Consistent?  Mismatch
Landing Site         1,2,3,4,13     No           Ship leaves then returns; fallen ship panel vanishes from
                                                 the ground.
Pillars              6, 9           Yes          None
White Pillar         7, 8, 11, 12   No           The dial prop changes design; debris direction changes.
Debris Field / Sky   5, 10          Yes          None

DRIFT MAP — where the film starts losing itself
Element        First slip (timecode)  Undeniable by  Recovered?
Gravity        0:20                   0:42           No
Ship Location  0:30                   2:00           No
Dial Prop      1:12                   1:52           No

CONTRADICTION LOG
Timecode A  Timecode B  Category      What contradicts what                                        Severity
0:16        0:42        Physical      Rock falls heavily down vs rocks float suspended upwards.     🔴 BLOCKER
0:38        2:00        Spatial       Ship takes off and leaves frame vs ship is parked statically
                                      in background.                                               🔴 BLOCKER
1:12        1:52        State/Props   Dial has 3 inner prongs and solid rim vs dial has 1 handle
                                      and segmented lit rim.                                       🟠 MAJOR
0:51        0:54        Causality     Second astronaut figure walks on left vs figure vanishes
                                      entirely from the open plain.                                🟠 MAJOR
0:08        0:38        Spatial       Ship panel rests on ground near landing gear vs ground is
                                      empty during hover.                                          🟡 MINOR

OPEN THREADS
Object / setup     Introduced  Returned to?  Note
Fallen ship panel  S1          No            Breaks off upon landing, never addressed.

THE THREE THAT MATTER
Gravity flipping: S2 shows normal gravity; S5 shows anti-gravity. Viewer feels the
physical rules of the world are broken. Cheapest fix: Decide on one gravity state and
regenerate the conflicting shots.

Ship teleportation: Ship leaves in S4 but is parked in S13. Viewer is confused about the
timeline and location. Cheapest fix: Paint out or crop the ship from the background of S13.

Morphing dial: S8 shows a 3-prong dial; S12 shows a 1-handle dial. Reads as a blatant prop
continuity error. Cheapest fix: Regenerate S12 to match the S8 design.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding                     Fix                                  Cost
Ship parked in S13          Mask/paint out ship from background  Low
Fallen panel missing in S4  Accept it (dust obscures ground)     Zero
Dial prop mismatch          Regenerate S12                       High
Gravity contradictions      Regenerate physics-breaking scenes   High

FLAGS FOR DOCUMENT CHECK
Observation                                           Question the document must answer
Gravity shifts from normal to inverted across cuts.   Is the environment designed to have
                                                      fluctuating/fractured gravity?
A second dark figure appears in S6.                   Is this meant to be a
                                                      hallucination/clone, or an AI
                                                      generation glitch?

OUT-OF-SCOPE FLAGS
Poster and title text at the end of the video → KAPAK_QA
The dust simulation clipping through the ship thrusters during liftoff → VIDEO_QA
```
