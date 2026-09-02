# THE SKYLIGHT — ⑥ FİZİK QA · HAM RAPOR

> Model çıktısı, OLDUĞU GİBİ (kural ④). Düzeltilmez, kısaltılmaz.
> Koşu: 29.08.2026'da sahip tarafından yapıştırıldı · Gemini · rubrik `6_FIZIK_QA_CRITIQUE_PROMPT.md` · MOD V
> Dosya (raporun künyesi): `the skylight_2.mp4`
> ⚠️ Rapor 24 fps varsaydı; master 30 fps (ffprobe) — süre ölçümleri o oranda kayar.
> ⛔ Film klasöründe `THE_SKYLIGHT_QA_SPEC.md` VARDIR (C bloğu sayısal kilitler) → NUMERIC LOCK LIST verilmedi, koşu ÖN KOŞU'dur [D129].
> Değerlendirme: `01_FILM_RAPORLARI/THE_SKYLIGHT.md`

---

INPUT MODE: V
FILM: the skylight_2.mp4
RUNTIME: ~314 s ESTIMATED
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 31 · CUTS COUNTED: 30
NON-SCENE MATERIAL: 5:10-5:14 Title Card
LINES HEARD: none — nothing audible to me
GRAVITY: GRAVITY ESTIMATE ≈ 3.8 m/s² ± 1.0 m/s², events used: dust falling from hand (0:40, 2:10) and rock placement (3:20).
PREMISE REGISTER: Zero-gravity environment in orbit (established at 4:50 by floating bolts).

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      64.0
DIVISION:           64.0 ÷ 8 = 8.0

OVERALL SCORE: 8.0/10
VERDICT: MINOR SLIPS

PHYSICS LEDGER
#    Timecode    Event    Duration (measured)    Distance (est. + RULER)    Implied value    Consistent with?
L1    0:30-0:40    Dust falling in cave shaft    10.0 s    ≈15.0 m (cave wall height)    Low terminal velocity    Cave environment
L2    0:40-0:50    Dust dropped from hand    0.8 s    ≈0.5 m (arm to floor)    g ≈ 3.8 m/s²    Sub-1g world
L3    1:00-1:10    Dust waterfall    10.0 s    ≈20.0 m (visible height)    Steady flow    Sub-1g world
L4    2:10-2:20    Dust dropped from hand    0.8 s    ≈0.5 m (arm to floor)    g ≈ 3.8 m/s²    Sub-1g world
L5    3:20-3:30    Placing rock on cairn    0.4 s    ≈0.1 m (hand to stack)    Human speed    1g to Sub-1g
L6    3:50-4:00    Walking to rocket    10.0 s    ≈10.0 m (stride count)    Walk ≈ 1.0 m/s    1g biomechanics
L7    4:20-4:30    Rocket exhaust/liftoff    10.0 s    ≈50.0 m (rocket height x3)    a ≈ 1.0 m/s²    Heavy lift mass
L8    4:50-5:00    Bolts floating in cockpit    10.0 s    ≈0.1 m (window frame)    Drift ≈ 0.01 m/s    0g in orbit
NUMERIC LOCK VERIFICATION — MODE D ONLY
Lock    Stated    Measured on screen    Δ    Verdict
N/A    N/A    N/A    N/A    N/A
SCORES SUMMARY
#    Category    Score    Critical Issue
1    Gravity & Free Fall    8/10    -2 · L2 (0:40), L7 (4:20)
2    Ballistics & Trajectories    N/A    [no objects thrown or launched]
3    Impact & Momentum    9/10    -1 · L7 (4:20)
4    Material Behaviour    9/10    -1 · L2 (0:40)
5    Particles & Atmosphere    7/10    -3 · L1 (0:30), L2 (0:40)
6    Scale & Measurement    9/10    -1 · L6 (3:50)
7    Rates & Timing    8/10    -2 · L6 (3:50)
8    Light & Shadow Physics    8/10    -2 · L6 (3:50)
9    Human Biomechanics    6/10    -4 · L8 (4:50)
PRESENCE STRING
1111111111111111111111111-1111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 3

GRAVITY TABLE
Ledger row    Timecode    Height (est. + ruler)    Time    Implied g    vs film's g
L2    0:40    ≈0.5 m (arm to floor)    0.8 s    ≈3.8 m/s²    Matches estimate
L4    2:10    ≈0.5 m (arm to floor)    0.8 s    ≈3.8 m/s²    Matches estimate
RATE TABLE
Rate    First measure (timecode)    Second measure (timecode)    Verdict
Walking pace    2:20 (1.0 m/s)    3:50 (1.0 m/s)    Holds
CONTRADICTION LOG
Ledger rows    Timecodes    Cat.    What contradicts what    Severity
L8    4:50 vs 4:50    9    Floating bolts indicate a 0g environment, but the astronaut's body, harness, and suit are entirely rigid, reacting to 1g physics without micro-motion.    🟠 MAJOR
L1, L2    0:30 vs 0:40    5    Dust hangs indefinitely in the background light shafts with almost zero terminal velocity, but dust dropped from the hand falls rapidly.    🟡 MINOR
L6    3:50 vs 4:20    8    Rocket shadow stretches very far to the left (implying a sun near the horizon), but the sky is uniformly bright and takeoff exhaust shadows imply a higher sun.    🟡 MINOR
L6    3:50 vs 3:50    7    Astronaut walks at an Earth-normal 1g gait, contradicting the slower sub-1g dust falls observed inside the caves.    🟡 MINOR
THE THREE THAT MATTER
Zero-G Biomechanics Disconnect (4:50): The bolts float past the character's head, signaling orbit, but the astronaut is frozen like a rigid statue. A viewer feels the mismatch between the live environment and the dead model. Fix: Regenerate the clip with continuous micro-motion or limb drift prompted.

Particle Terminal Velocity Split (0:30 vs 0:40): Dust behaves like two different materials. It acts like heavy sand when handled, but hangs like smoke in the environment. Fix: Accept it (common cinematic shorthand for "cave atmosphere").

Shadow Arithmetic (3:50): The extremely long shadow of the rocket suggests a sunset/sunrise, but the flat, bright lighting on the desert floor doesn't match the shadow angle. Fix: Accept it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Zero-G rigidity (4:50)    Regenerate scene to add human micro-motion    High
Dust falling vs hanging (0:30)    Accept as atmospheric styling    None
Rocket shadow angle (3:50)    Accept    None
FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Falls at 0:40 and 2:10 imply g ≈ 3.8 m/s², but walking gait looks like 1g.    Does the plan explicitly declare a low-gravity world, or should the astronaut be walking with more effort/bounce?
OUT-OF-SCOPE FLAGS
4:20 — Rocket exhaust flames clip entirely through the solid metal landing legs during liftoff → FRAME lens.
