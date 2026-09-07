# THE STANDING WIRE — ⑤ ARKA PLAN QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi (raporun yazdığı): `the standıng wıre.mp4` · rapor süresi ~245 s
> ⛔ ⑪.0 KİMLİK [D160]: aynı ada uyan İKİ dosya var, ikisi de ölçüldü —
>   `~/Downloads/the standıng wıre.mp4` 1280x720 · 245,141 s
>   `~/Downloads/the standıng wıre (1).mp4` 3840x2160 · 245,141 s  ← MASTER, ölçüm bunda koşuldu
>   AYNI KURGU (süre birebir), farklı çözünürlük. Rapor 720p kopyayı ölçmüş.
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 05.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_3_5_dk_filmler/THE_STANDING_WIRE/THE_STANDING_WIRE_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/PAKET_1..8` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
> ⛔ AYRICA TESLİM KUSURU [D150]: master ÜRETİCİ FİLİGRANI taşıyor (Flow ▷ ikonu, 6/6 örnek).
>   Filigranlı master master değildir → sekiz mercek onu ÖLÇMEMİŞ sayılır, mod Vden bağımsız olarak.
> ⛔ ⑤/⑦ notu: sekiz mercek AYNI OTURUMDA koşuldu → bağımsız ölçüm değildir [D110].

---

FILM: THE STANDING WIRE
RUNTIME: 04:05 measured
SCENES OBSERVED: 24 · CUTS COUNTED: 24
NON-SCENE MATERIAL: 4:00–4:05 Title Card
SUBJECTS EXCLUDED:
S1: Astronaut kneeling and base plate
S2: Astronaut holding wire coil
S3: Astronaut walking forward
S4: Astronaut's hands and base plate
S5: Astronaut ascending stairs
S6: Astronaut climbing rock wall
S7: Distant astronaut figure on massive stairs
S8: Astronaut climbing close-up
S9: Astronaut walking on rock ledge
S10: Astronaut looking upward
S11: Astronaut in profile holding wire
S12: Astronaut scrambling over rocks
S13: Astronaut climbing over ledge
S14: Astronaut walking on wide plateau
S15: Astronaut walking on sheer cliff edge
S16: Astronaut walking on straight platform
S17: Astronaut grabbing descending cage
S18: Astronaut standing near wire and cage
S19: Astronaut hanging from ascending cage
S20: Astronaut grabbing wire at space hatch
S21: Astronaut facing space station
S22: Space station hatch and wire
S23: Astronaut in cage ascending to hull
S24: Hand in foreground, snapping wire in window

BASELINE: SELF-CONSISTENCY — this review measures whether the background field agrees with itself, not whether it matches a set design.

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      35.0
DIVISION:           35.0 ÷ 6 = 5.8

OVERALL SCORE: 5.8/10
VERDICT: FIELD DRIFTS BUT RECOVERABLE
The primary field failure is a persistent static artifact across multiple wide shots, but the lack of background crowds insulates the film from severe integrity collapse.

BACKGROUND INVENTORY
SCENE 1 [0:00–0:10]  SUBJECT: Astronaut kneeling and base plate · MIDGROUND: Basalt column gorge walls · FAR FIELD: Distant gorge walls. Largest: Sky slit, upper middle · SKY: Bright daylight slit · FOCUS: Midground sharp, far field soft · EDGES: Floating rock artifacts popping in at 0:03–0:05
SCENE 2 [0:10–0:20]  MIDGROUND: Stepped rocky quarry walls · FAR FIELD: Crater rim. Largest: Crater wall rim, top half · SKY: Clear sky · FOCUS: Background steps slightly soft · EDGES: Clean
SCENE 3 [0:20–0:30]  MIDGROUND: Rocky walls, metal container right · FAR FIELD: Canyon exit. Largest: Canyon opening, center vertical · SKY: Bright light · FOCUS: Background soft · EDGES: Container merges into rock wall on right edge (0:24–0:28)
SCENE 4 [0:30–0:40]  MIDGROUND: Rocky ground · FAR FIELD: None. Largest: None — empty black/rock · FOCUS: Ground sharp · EDGES: Clean
SCENE 5 [0:40–0:50]  MIDGROUND: Blocky rock stairs · FAR FIELD: Stairway peak, upper center · SKY: Bright light · FOCUS: Far field soft · EDGES: Clean
SCENE 6 [0:50–1:00]  MIDGROUND: Sheer rock wall · FAR FIELD: Opposite canyon wall, left half · SKY: Sky slit · FOCUS: Sharp · EDGES: Clean
SCENE 7 [1:00–1:10]  MIDGROUND: Carved canyon walls · FAR FIELD: Canyon wall face, right half · SKY: Deep blue sky · FOCUS: Sharp · EDGES: Texture crawl on far walls (1:02–1:08)
SCENE 8 [1:10–1:20]  MIDGROUND: Rock face · FAR FIELD: Background canyon wall, left side · SKY: Sky slit · FOCUS: Background heavily blurred · EDGES: Clean
SCENE 9 [1:20–1:30]  MIDGROUND: Rock ledge, guide wire · FAR FIELD: Canyon chasm, background full · SKY: Clear blue · FOCUS: Background slightly soft · EDGES: Clean
SCENE 10 [1:30–1:40] MIDGROUND: Blocky rock wall · FAR FIELD: Rock wall, filling frame · SKY: Clear blue · FOCUS: Rock wall slightly soft · EDGES: Clean
SCENE 11 [1:40–1:50] MIDGROUND: None · FAR FIELD: Canyon wall, right background · SKY: Sunset/sunrise glow · FOCUS: Shallow depth of field · EDGES: Clean
SCENE 12 [1:50–2:00] MIDGROUND: Rocky terrain · FAR FIELD: Gorge wall, back right · SKY: Hazy sky · FOCUS: Background soft · EDGES: Clean
SCENE 13 [2:00–2:10] MIDGROUND: Ledge edge · FAR FIELD: Desert plain, back middle · SKY: Clear blue · FOCUS: Sharp · EDGES: Clean
SCENE 14 [2:10–2:20] MIDGROUND: Plateau surface · FAR FIELD: Terraced cliff, right half · SKY: Dark blue sky with planet limb · FOCUS: Sharp · EDGES: Persistent vertical line artifact dividing frame on right
SCENE 15 [2:20–2:30] MIDGROUND: Cliff edge · FAR FIELD: Planet surface below, bottom half · SKY: Black sky, massive planet limb · FOCUS: Sharp · EDGES: Persistent vertical line artifact on right
SCENE 16 [2:30–2:40] MIDGROUND: Grey platform · FAR FIELD: Planet horizon, middle horizontal · SKY: Black space, atmospheric glow · FOCUS: Sharp · EDGES: Persistent vertical line artifact on right
SCENE 17 [2:40–2:50] MIDGROUND: Wire and cage · FAR FIELD: Canyon edge, right background · SKY: Blue fading to black · FOCUS: Background slightly soft · EDGES: Clean
SCENE 18 [2:50–3:00] MIDGROUND: Platform, cage · FAR FIELD: Planet curvature, bottom half · SKY: Dark space · FOCUS: Sharp · EDGES: Clean
SCENE 19 [3:00–3:10] MIDGROUND: Cage structure · FAR FIELD: Planet surface, bottom half · SKY: Black space · FOCUS: Sharp · EDGES: Clean
SCENE 20 [3:10–3:20] MIDGROUND: Hatch frame · FAR FIELD: Planet surface, bottom right · SKY: Black space · FOCUS: Sharp · EDGES: Clean
SCENE 21 [3:20–3:30] MIDGROUND: Railings · FAR FIELD: Space station, upper center · SKY: Black space · FOCUS: Sharp · EDGES: Clean
SCENE 22 [3:30–3:40] MIDGROUND: Station hull · FAR FIELD: None · FOCUS: Sharp · EDGES: Clean
SCENE 23 [3:40–3:50] MIDGROUND: Underside of station · FAR FIELD: Station hull, top half · FOCUS: Sharp · EDGES: Clean
SCENE 24 [3:50–4:00] MIDGROUND: Interior walls, hooks · FAR FIELD: Starfield, window frame center · SKY: Interior ceiling · FOCUS: Sharp · EDGES: Clean

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Background Figure Integrity    N/A    No background figures
2    Background Figure Behaviour    N/A    No background figures
3    Crowd Count & Density    N/A    No crowds
4    Horizon & Topology    6/10    -1 · 2:00 vs 2:10 (topology jump from mesa to terraced canyon) 🟡
5    Depth, Parallax & Scale    7/10    -1 · 2:10-2:20 (minor parallax flatness on far cliffs) 🟡
6    Background Set & Props    6/10    -1 · 0:03-0:05 (floating rocks pop-in) 🟡 · -1 · 0:24-0:28 (container merges into rock wall) 🟡
7    Focus Honesty    7/10    -1 · 1:02-1:08 (texture crawl on canyon walls) 🟡
8    Sky & Atmospherics    6/10    -1 · 2:12-2:18 (dust clouds boil instead of drift) 🟡
9    Frame Edges & Emergent Artifacts    3/10    -4 · 2:10-2:40 (persistent static vertical line artifact) 🟠

PRESENCE STRING
111111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 6

FIELD DRIFT MAP
Scene    Layer    First slip (timecode)    Undeniable by    Recovered?
S14    Edge    2:10    2:12    No (persists to 2:40)
S14    Sky    2:12    2:15    Yes (ends at cut)

COUNT LOG
Group    Scene(s)    First clean count    Last clean count    Verdict
None    N/A    N/A    N/A    N/A

CONTRADICTION LOG
Timecode A    Timecode B    Layer    Cat.    What contradicts what    Severity
2:00    2:10    Far field    4    Flat desert plain becomes massive terraced canyon    🟡

THE THREE THAT MATTER
Persistent Vertical Line (S14-S16): A dark static line divides the right quadrant of the screen. Viewers will perceive a broken render or display error. Fix: Crop right edge.
Topology Jump (S13 to S14): The environment suddenly changes from a flat desert mesa to an alien terraced canyon. Viewers will feel geographic discontinuity. Fix: Accept it as a story location jump.
Container Merging (S3): The metal box on the right merges physically into the stone wall. Viewers will feel the geometry is unnatural. Fix: Crop right edge.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Vertical line artifact (2:10-2:40)    Refine crop by ~15% on right side    Cheap
Container merging (0:24-0:28)    Refine crop by ~10% on right side    Cheap
Dust boiling (2:12-2:18)    Regenerate S14    Expensive

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Topology changes drastically at 2:10    Does the story script imply a massive location jump or time skip here?

OUT-OF-SCOPE FLAGS
The guide wire exhibits physically impossible tension and slack behaviors across cuts (Physics lens).
The astronaut's suit details and helmet visor reflections drift severely across scenes (Continuity lens).
