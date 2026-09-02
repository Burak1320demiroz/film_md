# HAM RAPOR — THE STILL SWARM · ⑤ ARKA PLAN (T5)

```
KÜNYE (operatör tarafından doldurulmadı — D160 ihlali)
girdi: <tam yol YOK> · <süre YOK> · <çözünürlük YOK>
işlendiği tarih: 02.09.2026 · işleyen kart: qa-isle
⛔ ⑪ ölçüm kapısı KOŞULAMADI (master verilmedi).
⚠️ Rapor "FILM: THE STILL SWARM" yazıyor — ad BAŞLIK KARTINDAN okunmuş
   olabilir; ekrandaki yazı kimlik kanıtı DEĞİLDİR [D105]. Kimlik ③ kapısında
   METİN OLMAYAN çapalarla ayrıca kuruldu (film kaydına bakınız).
⚠️ SCENES OBSERVED 13 · CUTS COUNTED 13 — rubriğin kendi kuralına göre
   kartsız kurguda sahne = kesme + 1 olmalıydı.
```

---

FILM: THE STILL SWARM
RUNTIME: 02:14 measured
SCENES OBSERVED: 13 · CUTS COUNTED: 13
NON-SCENE MATERIAL: 2:10-2:14 Title card
SUBJECTS EXCLUDED:
S1: Astronaut pulling tether
S2: Astronaut pulling tether, closer
S3: Astronaut touching panel
S4: Astronaut seen from behind
S5: Astronaut belt and hands
S6: Astronaut spraying tool
S7: Astronaut floating left
S8: Astronaut floating center
S9: Astronaut pulling tether, interior
S10: Astronaut holding box
S11: Astronaut with box, back view
S12: Astronaut with box, side view
S13: Astronaut clinging to wall

BASELINE: SELF-CONSISTENCY — this review measures whether the background field agrees with itself, not whether it matches a set design.

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      26.0
DIVISION:           26.0 ÷ 6 = 4.3

OVERALL SCORE: 4.3/10
VERDICT: SUBJECT DUPLICATE IN FIELD
The background in Scene 13 generates an exact duplicate of the primary subject, compromising the far field entirely.

BACKGROUND INVENTORY
SCENE 1
SUBJECT: Astronaut pulling tether.
MIDGROUND: 1 small spacecraft left, tether line.
FAR FIELD: Large fragmented spherical structure, right side, fills ~60% frame.
SKY/CEILING: None — empty black.
FOCUS: Deep focus, sphere sharp.
EDGES: Clean.

SCENE 2
SUBJECT: Astronaut pulling tether, closer.
MIDGROUND: 1 small spacecraft left.
FAR FIELD: Fragmented spherical structure, fills ~70% frame.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 3
SUBJECT: Astronaut touching panel.
MIDGROUND: ~15 floating metal panel fragments.
FAR FIELD: Dark void.
SKY/CEILING: None — empty black.
FOCUS: Shallow, midground debris soft.
EDGES: Clean.

SCENE 4
SUBJECT: Astronaut seen from behind.
MIDGROUND: None.
FAR FIELD: Fragmented sphere, fills 90% frame.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 5
SUBJECT: Astronaut's belt and hands.
MIDGROUND: Soft focus small debris (~10 pieces).
FAR FIELD: Dark void.
SKY/CEILING: None — empty black.
FOCUS: Very shallow, background blurred.
EDGES: Soft debris entering/leaving slowly.

SCENE 6
SUBJECT: Astronaut spraying tool.
MIDGROUND: ~8 metal fragments, spray cloud.
FAR FIELD: Dark void.
SKY/CEILING: None — empty black.
FOCUS: Subject sharp, midground soft.
EDGES: Clean.

SCENE 7
SUBJECT: Astronaut floating left.
MIDGROUND: ~20 small debris pieces.
FAR FIELD: Dark void.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Debris clipping left edge.

SCENE 8
SUBJECT: Astronaut floating center.
MIDGROUND: 5 floating hand tools in a row.
FAR FIELD: Interior cylindrical wall structure.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 9
SUBJECT: Astronaut pulling tether.
MIDGROUND: 5 floating hand tools in a row.
FAR FIELD: Interior cylindrical wall.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 10
SUBJECT: Astronaut holding box.
MIDGROUND: ~15 debris pieces.
FAR FIELD: Dark void.
SKY/CEILING: None — empty black.
FOCUS: Subject sharp, debris soft.
EDGES: Clean.

SCENE 11
SUBJECT: Astronaut with box, back view.
MIDGROUND: 1 floating clamp, small debris.
FAR FIELD: Interior cylindrical wall.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 12
SUBJECT: Astronaut with box, side view.
MIDGROUND: Small debris.
FAR FIELD: Interior cylindrical wall.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 13
SUBJECT: Astronaut clinging to wall.
MIDGROUND: 1 astronaut figure, ~7 floating clamps.
FAR FIELD: Fragmented sphere, fills 50% frame.
SKY/CEILING: None — empty black.
FOCUS: Deep focus.
EDGES: Clean.

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Background Figure Integrity    3/10    🔴 2:00-2:09 (subject duplicate right field)
2    Background Figure Behaviour    4/10    🟠 2:00-2:09 (background figure arm morphs)
3    Crowd Count & Density    —    no in-scope source
4    Horizon & Topology    4/10    🟠 0:00 vs 0:30 (sphere geometry shifts)
5    Depth, Parallax & Scale    5/10    🟡 0:00-0:09 (sphere moves as single plate)
6    Background Set & Props    5/10    🟡 0:20-0:29 (panel debris melts/morphs)
7    Focus Honesty    —    no in-scope source
8    Sky & Atmospherics    —    no in-scope source
9    Frame Edges & Emergent Artifacts    5/10    🟡 1:01-1:09 (debris pop-in left edge)

PRESENCE STRING
1111111111111

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 3

FIELD DRIFT MAP
Scene    Layer    First slip (timecode)    Undeniable by    Recovered?
S13    Midground    2:00    2:02    No
S4    Far Field    0:30    0:32    No
S3    Midground    0:21    0:24    No

COUNT LOG
Group    Scene(s)    First clean count    Last clean count    Verdict
Floating panels    S3    15    15    Holds
Floating tools    S8, S9    5    5    Holds
Tool row    S13    7    7    Holds

CONTRADICTION LOG
Timecode A    Timecode B    Layer    Cat.    What contradicts what    Severity
0:00    0:30    Far    4    Sphere panel structure completely regenerates    🟠
1:10    1:40    Far    6    Cylinder wall pattern changes width    🟡

THE THREE THAT MATTER
Subject Duplicate (S13): Viewing identical gear on a background extra destroys scene immersion instantly. Fix: Crop the right field.

Sphere Topology Shift (S1 vs S4): The primary visual landmark loses architectural consistency between cuts. Fix: Regenerate S4 background.

Debris Morphing (S3): Floating metal stretches unconvincingly mid-shot. Fix: Accept.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
S13 Duplicate    Crop right side heavily    Cheap
S7 Edge Pop-in    Slight punch-in    Cheap
S4 Sphere shift    Regenerate far field layer    High

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
S8 vs S11 cylinder walls    Does the interior geometry change width here, or is it just lens FOV?

OUT-OF-SCOPE FLAGS
Astronaut tether clips through gauntlet physically at 0:08 (PHYSICS lens)
