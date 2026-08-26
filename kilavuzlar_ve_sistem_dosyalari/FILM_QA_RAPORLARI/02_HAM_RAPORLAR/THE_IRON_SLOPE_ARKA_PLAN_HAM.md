# 🖼️ THE IRON SLOPE — ⑤ ARKA PLAN_QA HAM RAPORU (derin tarama)

> Çalıştırma: 24-25.08.2026 · rubrik gereği **yalnız video** (belge verilmez)
> Rubrik: `../QA_PROMPTLARI/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md`
> Malzeme: tam kurgu · `~/Downloads/the ıron slope.mp4`
> 🚨 **BU RAPOR ALANIN EN BÜYÜK NESNESİNİ GÖRMEDİ:** S2'de (20-30 s) kadrajın
> alt üçte birini bir GEZEGEN kaplıyor; rapor altı sahnenin altısında da
> "FAR FIELD: Black space, star field" yazdı. Gezegen planın negatif
> bloğunda AÇIKÇA YASAK ("no planet, no moon"). → **DERS 126**.
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

FILM: the ıron slope.mp4
RUNTIME: 1:05 measured
SCENES OBSERVED: 6 · CUTS COUNTED: 6 (0:09, 0:18, 0:29, 0:39, 0:49, 1:00)
NON-SCENE MATERIAL: 1:00-1:05 title card
SUBJECTS EXCLUDED:
S1: Astronaut climbing ladder.
S2: Astronaut climbing.
S3: Astronaut climbing.
S4: Astronaut climbing.
S5: Astronaut climbing.
S6: Astronaut climbing.

BASELINE: SELF-CONSISTENCY — this review measures whether the background
field agrees with itself, not whether it matches a set design.

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      23.0
DIVISION:           23.0 ÷ 6 = 3.8

OVERALL SCORE: 3.8/10
VERDICT: FIELD COLLAPSES

BACKGROUND INVENTORY
SCENE 1 [0:00–0:09]
SUBJECT: Astronaut climbing ladder.
MIDGROUND: Flat grey hull, glowing seam, floating rectangular panel.
FAR FIELD: Black space, static star field.
SKY/CEILING: Deep space void.
FOCUS: Midground hull sharpens and blurs inconsistently; far field sharp.
EDGES: Clean.

SCENE 2 [0:10–0:18]
SUBJECT: Astronaut climbing.
MIDGROUND: Hull section featuring a small circular window/port.
FAR FIELD: Black space, star field.
SKY/CEILING: Deep space void.
FOCUS: Hull textures hold soft focus.
EDGES: Smear artifact hugging the right frame boundary.

SCENE 3 [0:19–0:29]
SUBJECT: Astronaut climbing.
MIDGROUND: Flat hull viewed from a severe low angle.
FAR FIELD: Space void.
SKY/CEILING: Deep space void.
FOCUS: Sharp across midground.
EDGES: Clean.

SCENE 4 [0:30–0:39]
SUBJECT: Astronaut climbing.
MIDGROUND: Freestanding triangular metal truss, no solid hull behind it.
FAR FIELD: Space void.
SKY/CEILING: Deep space void.
FOCUS: Truss edges exhibit slight texture swimming mid-shot.
EDGES: Clean.

SCENE 5 [0:40–0:49]
SUBJECT: Astronaut climbing.
MIDGROUND: Flat hull with horizontal paneling, second rectangular panel floating.
FAR FIELD: Space void.
SKY/CEILING: Deep space void.
FOCUS: Floating panel lacks depth and stays soft.
EDGES: Floating panel pops into frame unnaturally at the edge.

SCENE 6 [0:50–1:00]
SUBJECT: Astronaut climbing.
MIDGROUND: Large cylindrical engine nozzle and a heavy round hatch.
FAR FIELD: Space void.
SKY/CEILING: Deep space void.
FOCUS: Sharp across all visible background elements.
EDGES: Clean.

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Background Figure Integrity    N/A    no background figures
2    Background Figure Behaviour    N/A    no background figures
3    Crowd Count & Density    N/A    no crowd
4    Horizon & Topology    3/10    🟠 0:00 vs 0:30 (topology changes from solid hull to open truss)
5    Depth, Parallax & Scale    3/10    🔴 0:42-0:45 (midground panel moves as flat 2D layer)
6    Background Set & Props    3/10    🟠 0:00 vs 0:10 (set dressing changes entirely)
7    Focus Honesty    4/10    🟡 0:02-0:06 (hull texture swimming)
8    Sky & Atmospherics    6/10    🟡 0:00 vs 0:10 (star density shifts slightly)
9    Frame Edges & Artifacts    4/10    🟠 0:10-0:14 (smear) · 0:40 (pop-in)

PRESENCE STRING
111111

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 3   🟡 MINOR: 2

FIELD DRIFT MAP
Scene    Layer (mid/far/sky/edge)    First slip (timecode)    Undeniable by    Recovered?
S2    Midground    0:10    0:12    No
S4    Midground    0:30    0:32    No
S5    Midground    0:40    0:42    No
S6    Midground    0:50    0:52    No

COUNT LOG
Group    Scene(s)    First clean count    Last clean count    Verdict
Floating Panels    S1, S5    1    1    Consistent count, inconsistent presence

CONTRADICTION LOG
Timecode A    Timecode B    Layer    Cat.    What contradicts what    Severity
0:00    0:10    Midground    6    S1 features a smooth hull and glowing seam; S2 features a window port.    🟠 MAJOR
0:00    0:30    Midground    4    S1 features solid surface topology; S4 features open void behind a truss.    🟠 MAJOR
0:42    0:45    Midground    5    The floating panel exhibits 2D flat movement lacking parallax depth relative to the hull.    🔴 BLOCKER
0:02    0:06    Midground    7    Sharp hull paneling softens and swims locally as the camera pans.    🟡 MINOR
0:10    0:14    Edge    9    Smear artifact persists along the right frame edge.    🟠 MAJOR
0:00    0:10    Far Field    8    Star field density is visibly different between cuts.    🟡 MINOR

THE THREE THAT MATTER
Topology shifts (Cat 4): The background structure changes completely between scenes, destroying environmental coherence. Crop cannot fix; requires regeneration with locked set seeds.

2D Parallax failure (Cat 5): The S5 floating panel moves like a flat cutout against the background plate. Crop cannot fix; requires regenerating the midground asset.

Prop and Set drift (Cat 6): The appearance of windows, hatches, and seams changes randomly. Crop cannot fix; requires regeneration.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Topology and Set drift across S1-S6    Regenerate backgrounds with locked spatial map    High
2D panel movement in S5    Regenerate S5 midground pass    Medium
Edge smear in S2    Crop right edge by 5%    Low
Focus swimming in S1    Accept it or regenerate    Low

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Background structure morphs from solid hull to open truss across scenes.    Does the plan dictate a continuous climb on one surface, or a montage across vastly different station sections?
Star field density shifts slightly.    Is the ambient sky lighting intended to be perfectly static, or dynamic based on ship rotation?

OUT-OF-SCOPE FLAGS
0:00-1:00 — Subject's gravity reading contradicts floating panel physics → PHYSICS lens
0:00-1:00 — Climbing action audio plays in a vacuum environment → SOUND lens
