# THE FROST LINE — ⑥ FİZİK HAM RAPORU (2. koşu · mod V)

> Operatör künyesi: sahip 31.08.2026 mesajıyla teslim etti · aynı rubriğin
> aynı malzemeye İKİNCİ koşusu (1. koşu: `THE_FROST_LINE_FIZIK_HAM.md`).
> ⚠️ Bağımsızlık şüpheli [D110] ve iki koşu arasında kategoriler kaynaksız
> oynadı: Ölçek 10→7 ve Işık 10→7, ikisinin de Issue gözü "none" — raporun
> kendi aritmetik kuralı ④'e aykırı (kaynaksız düşüş uygulanmaz). İşlemede
> 1. koşu esas alındı. Aşağısı model çıktısıdır, düzenlenmemiştir.

---

INPUT MODE: V
FILM: the frost lıne.mp4
RUNTIME: ~3:55 ESTIMATED
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 23 · CUTS COUNTED: 23
NON-SCENE MATERIAL: 3:50-3:55 title card
LINES HEARD: none — nothing audible to me
GRAVITY: GRAVITY ESTIMATE ≈11.1 m/s² ± 2.0 (gas fall) vs ≈3.8 m/s² (human jog)
PREMISE REGISTER: none

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      29.0
DIVISION:           29.0 ÷ 6 = 4.8

OVERALL SCORE: 4.8/10
VERDICT: TWO GRAVITIES

PHYSICS LEDGER
#    Timecode    Event    Duration (measured)    Distance (est. + RULER)    Implied value    Consistent with?
L1    0:03    Gas vent release    0.6s    ≈2.0m (astronaut height)    g ≈ 11.1 m/s²    Earth gravity
L2    0:21    Astronaut jogging    1.0s    ≈1.5m (stride length)    Low-g float    Martian gravity
L3    0:45    Hand presses patch    2.0s    ≈0.1m (glove width)    Low tension    Soft dough
L4    1:03    Greenhouse crushed    N/A    ≈3.0m radius (structure)    Zero pressure    Vacuum
L5    2:05    Pulls thermal screen    2.0s    ≈1.0m (arm reach)    v ≈ 0.5 m/s    Human effort
L6    3:45    Pulling massive tarp    3.0s    ≈2.0m (suit width)    Low mass/friction    Small cloth
NUMERIC LOCK VERIFICATION — MODE D ONLY
Lock    Stated    Measured on screen    Δ    Verdict
(none - Mode V)
SCORES SUMMARY
#    Category    Score    Critical Issue
1    Gravity & Free Fall    3/10    -4 · L1 (0:03), L2 (0:21)
2    Ballistics & Trajectories    N/A    [no ballistic objects]
3    Impact & Momentum    N/A    [no impacts]
4    Material Behaviour    3/10    -4 · L3 (0:45) · L6 (3:45)
5    Particles & Atmosphere    4/10    -3 · L1 (0:03)
6    Scale & Measurement    7/10    none
7    Rates & Timing    ⚠️ PARTIAL    [only L5 measured]
8    Light & Shadow Physics    7/10    none
9    Human Biomechanics    5/10    -2 · L2 (0:21)
PRESENCE STRING
11111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 2   🟡 MINOR: 0

GRAVITY TABLE — every measured fall
Ledger row    Timecode    Height (est. + ruler)    Time    Implied g    vs film's g
L1    0:03    ≈2.0m (astronaut height)    0.6s    ≈11.1 m/s²    Contradicts human stride
L2    0:21    ≈0.5m (apex)    0.5s    ≈4.0 m/s²    Contradicts gas fall
RATE TABLE — every rate measured twice
Rate    First measure (timecode)    Second measure (timecode)    Verdict
(none)
CONTRADICTION LOG
Ledger rows    Timecodes    Cat.    What contradicts what    Severity
L1, L2    0:03, 0:21    1    Vent gas falls >1g vs jog hang time <0.4g.    🔴 BLOCKER
L3, L5    0:45, 2:05    4    Hull yields like soft dough externally, rigid internally.    🟠 MAJOR
THE THREE THAT MATTER
Gravity Split: Vent gas falls fast, human floats. Blocker. Fix: Regenerate S1.

Soft Hull: Pressing patch deforms pressurized rigid hull. Fix: Regenerate S5.

Weightless Tarp: Massive tarp pulled without leverage/mass. Fix: Trim S23.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Two Gravities    Regenerate S1    Regenerate
Unpressurized hull    Regenerate S5    Regenerate
Massless tarp    Trim head of S23    Edit
FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Vent gas acts like solid granular material.    Does plan call for liquid/solid leak?
Greenhouse crushed at 1:03 but intact at 1:20.    Timeline gap or continuity error?
OUT-OF-SCOPE FLAGS
1:03 vs 1:20 — Greenhouse crushed externally but intact internally → CONTINUITY lens.
