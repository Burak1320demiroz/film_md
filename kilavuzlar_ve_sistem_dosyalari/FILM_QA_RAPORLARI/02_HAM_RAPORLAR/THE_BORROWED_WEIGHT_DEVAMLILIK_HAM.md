# 🔗 THE BORROWED WEIGHT — ② DEVAMLILIK_QA HAM RAPORU

> Çalıştırma: 24.08.2026 · yalnız video (kural gereği: bu rubriğe belge verilmez)
> Rubrik: `../QA_PROMPTLARI/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> ⚠️ Dört mercekli partinin parçası. **Parti ⑤ ÇAPRAZ SAYIM kapısından geçmedi**
> → 🚨 GEÇERSİZ; skor satırı T2 tablosuna İŞLENMEDİ.
> ⛔ Bu raporun iki aritmetik ihlali film kaydında kalem kalem yazıldı:
> (a) dört hücre "no in-scope source" + 7/10 aynı satırda [D119 TEKRARI],
> (b) sahne haritası 3:59'da bitiyor ama künye 4:24 diyor — 25 s haritasız.
> Kapı defterleri: `../01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④). Tablolar sohbetten
> yapıştırıldığı için boru işaretlerini kaybetmiştir; sayılar değiştirilmemiştir.

---

FILM: the borrowed weıght (1).mp4
RUNTIME: 04:24 MEASURED
SCENES OBSERVED: 24 · CUTS COUNTED: 24 · CHARACTERS TRACKED: 1

MATERIAL TYPE: FILM
BASELINE: SELF-CONSISTENCY — this review measures whether the film and its people agree with themselves, not whether they match a design.

ARITHMETIC GATE
SCORED CATEGORIES:  11
SUM OF SCORES:      54.0
DIVISION:           54.0 ÷ 11 = 4.9

OVERALL SCORE: 4.9/10
VERDICT: IDENTITY BREAK

SCENE INVENTORY
#    In-out    Location    Present    What happens    Dialogue
1    0:00-0:09    Plain    1    Carrying strut    N
2    0:10-0:19    Plain    1    Looking at pod    N
3    0:20-0:29    Plain    1    Drops strut    N
4    0:30-0:39    Plain    1    Approaches pod    N
5    0:40-0:49    Plain    1    Looking at strut    N
6    0:50-0:59    Plain    1    Picks up wrenches    N
7    1:00-1:09    Plain    1    Weighing rock    N
8    1:10-1:19    Plain    1    Close-up weighing    N
9    1:20-1:29    Plain    1    Walking left    N
10    1:30-1:39    Plain    1    Near large ring    N
11    1:40-1:49    Plain    1    Pushing panel    N
12    1:50-1:59    Plain    1    Helmet close-up    N
13    2:00-2:09    Pod    1    Touching pod    N
14    2:10-2:19    Plain    1    Holding scale    N
15    2:20-2:29    Plain    1    Looking at prints    N
16    2:30-2:39    Wall    1    Pushing wall    N
17    2:40-2:49    Plain    1    Wide view    N
18    2:50-2:59    Plain    1    Kneeling w/ pipe    N
19    3:00-3:09    Plain    1    Box with orb    N
20    3:10-3:19    Plain    1    Holding scale    N
21    3:20-3:29    Plain    1    Levering strut    N
22    3:30-3:39    Plain    1    Walking at night    N
23    3:40-3:49    Plain    -    Ship crashes    N
24    3:50-3:59    Plain    1    Opens hatch    N

CHARACTER PASSPORT(S)
Label: Astronaut
First clear view: 1, 0:00
Face: Older dark-skinned male, graying beard.
Hair: Not visible.
Eyes: Brown.
Build: Stocky.
Costume: Off-white suit, large square chest plate, brass loop right waist.
Equipment: Clear visor helmet, dark grey gloves.
Wear map: Dusted lower legs/knees.
Voice: N/A.

⭐ EVIDENCE BASE
FACE-VISIBLE: 80 s of 264 s total · 8 of 24 scenes
COSTUME-VISIBLE: 23 of 24 scenes
MOUTH ON SCREEN: no

APPEARANCE TABLE
Character    Scene    In-out    Face visible?    State notes
Astronaut    1    0:00-0:09    Yes    Square chest plate
Astronaut    2    0:10-0:19    No    From behind
Astronaut    5    0:40-0:49    Yes    Loop on waist
Astronaut    7    1:00-1:09    Yes    Weighing
Astronaut    8    1:10-1:19    Yes    Rectangular chest plate
Astronaut    12    1:50-1:59    Yes    Face structure wider
Astronaut    13    2:00-2:09    Yes    Large pod scale
Astronaut    18    2:50-2:59    Yes    Dirty knees
Astronaut    21    3:20-3:29    No    Clean knees
Astronaut    24    3:50-3:59    Yes    Night lighting

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Identity — Face, Hair & Build    3/10    -4 · 1:10 (A) · 1:50 (B)
2    Costume Identity    3/10    -4 · 0:40 (A) · 1:10 (B)
3    Wear, Damage & Injury    4/10    -3 · 2:50 (A) · 3:20 (B)
4    Equipment & Carried Objects    3/10    -4 · 1:00 (A) · 2:10 (B)
5    Cross-Cut Action    7/10    no in-scope source
6    Physical Consistency    7/10    no in-scope source
7    Counter Logic    N/A    no in-scope source
8    Spatial Geography    4/10    -3 · 0:30 (A) · 2:00 (B)
9    Time & Light Logic    4/10    -3 · 3:20 (A) · 3:30 (B)
10    World State & Props    5/10    -2 · 0:40 (A) · 3:20 (B)
11    Causality & Knowledge    7/10    no in-scope source
12    Quantity & Character Count    N/A    no in-scope source
13    Setup & Abandonment    7/10    no in-scope source

PRESENCE STRING
1111111111111111111111-1

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 4   🟡 MINOR: 0

DRIFT MAP — where the film starts losing itself
Half    Element    Character    First slip (timecode)    Undeniable by    Recovered?
BODY    Costume    Astronaut    1:10    1:10    No
BODY    Identity    Astronaut    1:50    1:50    No
WORLD    Scale    -    2:00    2:00    No

WEAR TIMELINE — per tracked mark
Mark    Character    Acquired    Present at    Absent at ⚠️    One-way?
Knee dust    Astronaut    S1    S18    S21 ⚠️    No

COUNTER CURVE
NONE

LOCATION MAP
Location    Scenes    Consistent?    Mismatch
Plain    All    No    Geography shifts entirely
Pod    4, 13, 24    No    Scale jumps drastically

CONTRADICTION LOG
Timecode A    Timecode B    Half    Character    Cat.    What contradicts what    Severity
1:10    1:50    BODY    Astronaut    1    Facial bone structure changes    🔴 BLOCKER
0:40    1:10    BODY    Astronaut    2    Chest plate changes shape    🟠 MAJOR
2:50    3:20    BODY    Astronaut    3    Dirty knees reset to clean    🟠 MAJOR
1:00    2:10    BODY    Astronaut    4    Brass scale morphs design    🟠 MAJOR
0:30    2:00    WORLD    -    8    Pod scales from tiny to massive    🔴 BLOCKER
3:20    3:30    WORLD    -    9    Daylight instantly becomes night    🟠 MAJOR

OPEN THREADS
Object / setup    Introduced    Returned to?    Note
Wrenches    S6    No    Picked up and abandoned
Glow orb    S19    No    Box left behind

THE THREE THAT MATTER
Identity Shift: The astronaut's face changes structure entirely. It breaks the promise of a single protagonist. Fix: Regenerate close-ups to match S1.

Pod Scale: The pod is tiny, then massive. Ruins spatial logic. Fix: Regenerate wide shots to match S13 scale.

Prop Morphing: The brass scale changes design every time it appears. Fix: Fixable in edit if closely cropped, otherwise regenerate.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Face changes    Regenerate    High
Pod scale    Regenerate    High
Night jump    Re-cut/Remove    Low

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Chest plate shifts    Was a specific suit module requested?
Night falls instantly    Is there a time jump intended here?

OUT-OF-SCOPE FLAGS
none
