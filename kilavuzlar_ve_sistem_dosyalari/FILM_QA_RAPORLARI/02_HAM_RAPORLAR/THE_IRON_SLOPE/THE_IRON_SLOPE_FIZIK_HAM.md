# ⚖️ THE IRON SLOPE — ⑥ FİZİK_QA HAM RAPORU (derin tarama)

> Çalıştırma: 24-25.08.2026 · **mod V** — ⛔ bu merceğin VARLIK SEBEBİ mod D'dir
> (planın sayısal kilitleri NUMERIC LOCK LIST'e kopyalanacaktı, kopyalanmadı)
> Rubrik: `../QA_PROMPTLARI/6_FIZIK_QA_CRITIQUE_PROMPT.md`
> Malzeme: tam kurgu · `~/Downloads/the ıron slope.mp4`
> ⭐ Bu raporun ANA BULGUSU master ölçümüyle DOĞRULANDI: serbest parça
> hızlanmıyor. Ama gerekçesi yanlış — film 0 g dünyası değil, 0,220 g
> İTKİ dünyasıdır ve novum ekrana gelmemiştir. Ölçüm:
> `../01_FILM_RAPORLARI/THE_IRON_SLOPE.md` §KİLİT ÇELİŞKİSİ DEFTERİ.
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

INPUT MODE: V
FILM: the ıron slope.mp4
RUNTIME: 1:05 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 6 · CUTS COUNTED: 6 (0:09, 0:18, 0:29, 0:39, 0:49, 1:00)
NON-SCENE MATERIAL: 1:00-1:05 title card
LINES HEARD: none
GRAVITY: GRAVITY ESTIMATE 0 m/s² vs ~9.8 m/s² ± 9.8 m/s², events used: L2 (floating panel) vs L1 (astronaut climb effort)
PREMISE REGISTER: none

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      45.0
DIVISION:           45.0 ÷ 6 = 7.5      ← this is OVERALL SCORE

OVERALL SCORE: 7.5/10
VERDICT: TWO GRAVITIES

PHYSICS LEDGER
#    Timecode    Event    Duration (measured)    Distance (est. + RULER)    Implied value    Consistent with?
L1    0:00-0:09    Astronaut climbs ladder    9.0 s    ~2.0 m (ruler: human height)    Implied ~1g effort and speed    1g Earth gravity
L2    0:02-0:09    Rectangular panel floats away    7.0 s    ~3.0 m (ruler: astronaut scale)    Implied 0g (constant v, no drop)    0g microgravity
L3    0:10-0:18    Astronaut climbs    8.0 s    ~1.5 m (ruler: rungs)    Implied ~1g effort    L1 (1g climb)
L4    0:30-0:39    Astronaut climbs truss    9.0 s    ~2.0 m (ruler: rungs)    Implied ~1g effort    L1 (1g climb)
L5    0:40-0:45    Second panel floats    5.0 s    ~1.0 m (ruler: astronaut)    Implied 0g (constant v, flat 2D)    L2 (0g float)
L6    0:50-1:00    Astronaut climbs    10.0 s    ~2.5 m (ruler: human)    Implied ~1g effort    L1 (1g climb)

NUMERIC LOCK VERIFICATION — MODE D ONLY
N/A — Mode V only.

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Gravity & Free Fall    3/10    🔴 -7 · L2 (0:02), L5 (0:40) vs L1, L3 (Two gravities in one shot)
2    Ballistics & Trajectories    N/A    no throws or launched arcs
3    Impact & Momentum    N/A    no impacts or collisions
4    Material Behaviour    10/10    no in-scope source
5    Particles & Atmosphere    N/A    no dust, debris, or fluid releases
6    Scale & Measurement    8/10    🟡 -2 · L4 (0:30) truss scale contradicts hull scale
7    Rates & Timing    10/10    no in-scope source
8    Light & Shadow Physics    10/10    no in-scope source
9    Human Biomechanics    4/10    🟠 -6 · L1, L3, L4, L6 (1g heavy exertion biomechanics in a 0g setting)

PRESENCE STRING
111111

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 1   🟡 MINOR: 1

GRAVITY TABLE
Ledger row    Timecode    Height (est. + ruler)    Time    Implied g    vs film's g
L2    0:02-0:09    N/A (linear drift, no drop)    7.0 s    0 m/s²    Contradicts 1g climb
L5    0:40-0:45    N/A (linear drift, no drop)    5.0 s    0 m/s²    Contradicts 1g climb

RATE TABLE
Rate    First measure (timecode)    Second measure (timecode)    Verdict
Climb speed    ~0.22 m/s (L1: 0:00-0:09)    ~0.25 m/s (L6: 0:50-1:00)    Consistent

CONTRADICTION LOG
Ledger rows    Timecodes    Cat.    What contradicts what    Severity
L1, L2    0:00, 0:02    1    Astronaut's heavy 1g biomechanical effort contradicts the 0g environment proven by the floating panel.    🔴 BLOCKER
L3, L5    0:10, 0:40    1    Astronaut climbs with full weight in S2 and S5, while background objects float weightlessly in S5.    🔴 BLOCKER
L1, L4    0:00, 0:30    6    The ladder rungs are scaled to a flat hull surface in S1, but appear oversized on a freestanding truss in S4.    🟡 MINOR

THE THREE THAT MATTER
Two Gravities (Cat 1): The astronaut's body behaves as if under 1g (heavy footfalls, pulling full weight), while loose panels float in 0g. The viewer feels this mismatch immediately; they exist in two different physics engines. Fix: Regenerate the clip specifying zero-gravity locomotion for the astronaut.

Heavy Biomechanics in Space (Cat 9): Climbing in microgravity requires light guiding motions, mostly pulling with the hands while the lower body trails. The astronaut exerts massive, heavy-lifting effort against the ladder. Fix: Prompt for "zero-g weightless climbing, drifting body".

Truss Scale Disconnect (Cat 6): The ladder and its rungs change scale and topology drastically between the hull shots and the truss shots, making the distance climbed unmeasurable. Fix: Re-cut to remove the truss shots (S4) to maintain spatial scale.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Two Gravities (1g actor vs 0g panel)    Regenerate to enforce uniform gravity    High
Incorrect Biomechanics (1g climbing)    Regenerate using zero-g motion prompts    High
Ladder scale shifts    Trim or remove S4 from the sequence    Low

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The film exhibits both 1g human effort and 0g environmental debris simultaneously.    Does the plan call for a microgravity environment or a planet with Earth-normal gravity?

OUT-OF-SCOPE FLAGS
0:00-1:00 — Background structure morphs repeatedly from a solid hull to an open truss → CONTINUITY lens
0:00-1:00 — Airborne audio (clanking, breathing) exists in a visual vacuum → SOUND / FRAME lens
0:42-0:45 — Floating panel behaves as a 2D cutout lacking parallax depth → BACKGROUND / FRAME lens
