# THE STANDING WIRE — ⑥ FİZİK QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi (raporun yazdığı): `the standıng wıre.mp4` · rapor süresi ~245 s
> ⛔ ⑪.0 KİMLİK [D160]: aynı ada uyan İKİ dosya var, ikisi de ölçüldü —
>   `~/Downloads/the standıng wıre.mp4` 1280x720 · 245,141 s
>   `~/Downloads/the standıng wıre (1).mp4` 3840x2160 · 245,141 s  ← MASTER, ölçüm bunda koşuldu
>   AYNI KURGU (süre birebir), farklı çözünürlük. Rapor 720p kopyayı ölçmüş.
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 05.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_4_dk_filmler/THE_STANDING_WIRE/THE_STANDING_WIRE_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/PAKET_1..8` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
> ⛔ AYRICA TESLİM KUSURU [D150]: master ÜRETİCİ FİLİGRANI taşıyor (Flow ▷ ikonu, 6/6 örnek).
>   Filigranlı master master değildir → sekiz mercek onu ÖLÇMEMİŞ sayılır, mod Vden bağımsız olarak.
> ⛔ ⑤/⑦ notu: sekiz mercek AYNI OTURUMDA koşuldu → bağımsız ölçüm değildir [D110].

---

INPUT MODE: V
FILM: the standıng wıre.mp4
RUNTIME: 04:05 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 24 · CUTS COUNTED: 24
NON-SCENE MATERIAL: 4:00–4:05 Title Card
LINES HEARD: none — nothing audible to me
GRAVITY: unmeasurable (no unobstructed free falls to compute g)
PREMISE REGISTER: none

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      37.0
DIVISION:           37.0 ÷ 6 = 6.1

OVERALL SCORE: 6.1/10
VERDICT: FIXABLE IN EDIT
The physical world is remarkably consistent in its timings and rates, specifically the slow human gait and mechanical ascensions. The film's physics fail primarily on material geometry (solid clipping) and a massive scale re-roll of the titular wire.

PHYSICS LEDGER
#    Timecode    Event    Duration    Distance (est. + RULER)    Implied value    Consistent with?
1    0:02–0:05    Small rocks float and rise around baseplate    3.0 s    ≈0.5m (suit knee to chest)    Rocks defy gravity, reversing mid-air    N/A
2    0:20–0:29    Astronaut walks with coiled wire    9.0 s    ≈6m (3-4 body lengths)    Walk speed ≈ 0.6 m/s    L5, L6, L7
3    0:34–0:38    Astronaut places circular cover over wire    4.0 s    ≈0.3m (arm reach)    Solid cover phases through solid wire    Real physics
4    0:39–0:50    Astronaut walks up stone stairs    11.0 s    ≈5m vertically (stair steps)    Climb speed ≈ 0.45 m/s    L2
5    1:20–1:29    Astronaut walks on high rock ledge    9.0 s    ≈4m (2 body lengths)    Walk speed ≈ 0.44 m/s    L2, L6
6    2:09–2:18    Astronaut walks along cliff edge    9.0 s    ≈5m (3 body lengths)    Walk speed ≈ 0.55 m/s    L2, L7
7    2:30–2:40    Astronaut walks on flat platform    10.0 s    ≈6m (3-4 body lengths)    Walk speed ≈ 0.6 m/s    L2, L6
8    3:00–3:10    Cage ascends with hanging astronaut    10.0 s    ≈4m (2 body lengths)    Ascension speed ≈ 0.4 m/s    L10
9    3:30–3:39    Wire enters space station airlock    9.0 s    ≈0.2m diameter (vs 1m hatch)    Wire thickness scales up 10x    L3, L11
10    3:39–3:50    Cage ascends toward airlock    11.0 s    ≈5m (hatch width reference)    Ascension speed ≈ 0.45 m/s    L8
11    3:52–3:58    Snapped wire recoils outside window    6.0 s    ≈2m (window height)    Snapped tension cable undulates slowly    Cinematic float
12    1:20–1:29    Astronaut shadow casting on ledge    9.0 s    N/A (direction: right)    Sun positioned left    L13
13    2:30–2:40    Astronaut shadow casting on platform    10.0 s    N/A (direction: forward-left)    Sun positioned back-right    L12

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Gravity & Free Fall    —    no in-scope source
2    Ballistics & Trajectories    —    no in-scope source
3    Impact & Momentum    —    no in-scope source
4    Material Behaviour    5/10    -5 · L3 (0:34) (baseplate cover clips through solid wire) 🟠
5    Particles & Atmosphere    7/10    -3 · L1 (0:02) (rocks reverse direction mid-air without cause) 🟡
6    Scale & Measurement    5/10    -5 · L9 (3:30) (wire diameter scales up 10x at the station) 🟠
7    Rates & Timing    8/10    -2 · L11 (3:52) (wire snap recoil shows cinematic slow-motion) 🟡
8    Light & Shadow Physics    5/10    -5 · L12 (1:20), L13 (2:30) (sun splits/relocates between scenes) 🟠
9    Human Biomechanics    7/10    -3 · L4 (0:39) (climbing massive stairs with insufficient knee flexion) 🟡

PRESENCE STRING
111111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 3

GRAVITY TABLE
| Ledger row | Timecode | Height | Time | Implied g | vs film's g |
| N/A | N/A | N/A | N/A | N/A | N/A |

RATE TABLE
Rate    First measure (timecode)    Second measure (timecode)    Verdict
Walk speed    L2 (0:20)    L7 (2:30)    PASS (~0.6 m/s)
Cage ascension    L8 (3:00)    L10 (3:39)    PASS (~0.4 - 0.45 m/s)

CONTRADICTION LOG
Ledger rows    Timecodes    Cat.    What contradicts what    Severity
L12 vs L13    1:20 vs 2:30    8    Sun positioned left vs sun positioned back-right    🟠
L3 vs L9    0:34 vs 3:30    6    Wire diameter ~2cm at base vs ~20cm at space station    🟠

THE THREE THAT MATTER
Material Phasing (0:34): The metal cover clips directly through the solid vertical wire during placement. Fix: Trim the shot just before the cover intersects the wire.
Scale Re-roll (3:30): The titular wire's thickness balloons ten-fold when it reaches the space station hatch. Fix: Regenerate scene 22 with correct wire diameter.
Sun Split (1:20 vs 2:30): Shadow directions reverse completely between wide exterior shots. Fix: Accept it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Solid cover phases through wire (0:34)    Trim shot by 1-2 seconds    Cheap
Wire scale re-roll (3:30)    Regenerate S22    Expensive
Sun split (1:20 vs 2:30)    Regenerate to match lighting    Expensive

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Walk speeds average 0.5 m/s throughout the film    Does the plan specify heavy suit encumbrance or a low-gravity world?
Floating rocks at 0:02 reverse direction mid-air    Does the script call for anti-gravity anomalies near the baseplate?

OUT-OF-SCOPE FLAGS
The astronaut's spacesuit geometry, helmet shape, and stripe patterns drift constantly between shots → CONTINUITY lens
