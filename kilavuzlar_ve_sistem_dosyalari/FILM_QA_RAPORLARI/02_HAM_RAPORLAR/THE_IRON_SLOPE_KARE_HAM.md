# 🔧 THE IRON SLOPE — ① KARE_QA HAM RAPORU

> Çalıştırma: 24-25.08.2026 · **mod V** (SPEC dosyası depoda YOK, verilmedi → ⛔ ön koşu [D94/D117])
> Rubrik: `../QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md`
> Malzeme: tam kurgu · `~/Downloads/the ıron slope.mp4`
> ⚠️ Altı mercekli partinin parçası (🔧🔗🔊📖🖼️⚖️).
> ⛔ Bu raporun KESME LİSTESİ ve SESSİZLİK bulguları master ölçümüyle
> çürütülmüştür — gerekçe ve sayılar: `../01_FILM_RAPORLARI/THE_IRON_SLOPE.md`
> §ÖLÇÜM KAPISI.
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④). Tablolar sohbetten
> yapıştırıldığı için boru işaretlerini kaybetmiştir; sayılar değiştirilmemiştir.

---

FORMAT: DİKEY

INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: DİKEY
ASPECT MEASURED: 9:16 (measured from file dimensions)
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 1:05 measured
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 6 (0:09, 0:18, 0:29, 0:39, 0:49, 1:00)
NON-SCENE MATERIAL: 1:00-1:05 title card
LINES HEARD: none

SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  11
SUM OF SCORES:      61.0
DIVISION:           61.0 ÷ 11 = 5.5

OVERALL SCORE: 5.5/10 (3 categories excluded: Creatures is N/A; Frame Anchor is UNVERIFIABLE; Negative Violations is a count).
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    4/10    −6 · 0:58 (hand clipping) · 0:45 (strap clipping)
Scale & Physics    2/10    −8 · 0:00-0:09, 0:40-0:45 (mixed gravity)
Camera    10/10    no in-scope source
Lighting    10/10    no in-scope source
Environment    6/10    −4 · 0:30-0:39 (impossible truss geometry)
Creatures    N/A    no in-scope source
Particles & Materials    4/10    −6 · 0:42-0:45 (2D panel rotation)
Dialogue & Audio    1/10    −9 · 0:00-1:00 (sound in vacuum)
Frame Anchor Fidelity    UNVERIFIABLE    mode V
Negative Violations    3 count    0:58 (clipping), 0:42 (2D asset), 0:00 (audio)
Motion Quality    2/10    −8 · 0:00-0:09, 0:40-0:45 (mixed gravity vectors)
Vertical Format (9:16)    6/10    −4 · 0:00-1:00 (centered composition)
Safe Zone    6/10    −4 · 0:11-0:18 (character in right/top band)
Hook Timing    10/10    no in-scope source

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 1:05 measured
Cuts you can see: 6 (0:09, 0:18, 0:29, 0:39, 0:49, 1:00)
Aspect ratio: 9:16

THE CHARACTER — as first clearly seen
Face / hair / marks: clean-shaven male, dark hair. First frame fully visible: 0:00
Suit / wardrobe: bulky white spacesuit, grey accents, rectangular chest pack with orange stripes
Wear / dirt: clean, no visible wear
Equipment: helmet with clear visor, heavy gloves, tether straps

THE WORLD — as the footage shows it
Gravity read: Mixed. Character climbs with 1g weight/effort, loose panels float in zero-g.
Atmosphere read: Vacuum (space, stars visible)
Light sources: Single strong harsh source (sun) from the left, hard shadows
Location: Exterior hull of a large spacecraft/station

MOTION
Camera: Mostly static lockoffs with slight slow pans/tilts
Subject: Climbing a ladder vertically

PRESENCE STRING
111111

SEVERITY TALLY
🔴 BLOCKER: 5    🟠 MAJOR: 4    🟡 MINOR: 0

TOP 3 CRITICAL ERRORS
0:00 — 🔴 BLOCKER — Airborne sound (heavy clanking, suit movement, breathing) propagates clearly in a vacuum environment.

0:00 — 🔴 BLOCKER — Mixed gravity vectors: Character climbs the ladder with heavy 1g weight and effort, while background panels float weightlessly in zero-g.

0:58 — 🔴 BLOCKER — Contact morphing: Character's right hand phases completely into the solid metal vertical rail of the ladder.

DETAILED ERROR LOG
0:00-1:00 — 🔴 BLOCKER — Dialogue & Audio — Airborne sound (clanking, suit movement, breathing) propagates clearly in a vacuum environment.
0:00-0:09 — 🔴 BLOCKER — Scale & Physics — Mixed gravity: Loose panel floats in zero-g while astronaut climbs with 1g weight/effort.
0:11-0:18 — 🟠 MAJOR — Safe Zone — Story-critical element (astronaut's head/upper body) climbs into the top UI band (top 200px) and the right UI band (last 242px).
0:00-1:00 — 🟠 MAJOR — Vertical Format — Standard composition lock violated: Character is framed heavily in the center and upper half rather than the lower third.
0:30-0:39 — 🟠 MAJOR — Environment — AI hallucination on geometry: The ladder/truss structure does not connect physically and forms a visually impossible M.C. Escher-like shape.
0:40-0:45 — 🔴 BLOCKER — Motion Quality — Mixed gravity: Panels float while character steps heavily onto rungs.
0:42-0:45 — 🔴 BLOCKER — Particles & Materials — Zero-g object (floating panel) rotates like a flat 2D cutout with no physical mass or realistic inertia.
0:45 — 🟠 MAJOR — Character — Strap hanging from the character's right hip clips completely through the solid metal ladder rail.
0:58 — 🔴 BLOCKER — Character — Contact morphing: Character's right hand phases through and merges with the solid vertical rail of the ladder.

NEGATIVE BOX COUNT
[x] Object phasing/clipping

[x] Zero-g objects hanging without momentum (flat 2D asset behavior)

[x] Airborne sound propagating in vacuum

NEGATIVE BOX COUNT: 3 · LINKED FINDINGS: 3 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 3 · TICKED: 3 · MISSED: 0
NO BOX EXISTS FOR: mixed gravity vectors, impossible geometry hallucination, vertical composition deviation, safe zone occlusion.

WHAT WORKED WELL
The lighting is appropriately harsh and directional for space, with no AI bloom or dreamy diffusion.

The hook scene immediately establishes motion and context within the first 2 seconds, successfully grabbing attention.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to video prompt: "uniform zero-gravity physics for all elements, weightless locomotion, no gravitational weight on subject" → prevents mixed gravity climbing.

REMOVE from audio prompt: "heavy footsteps, clanking metal" → causes airborne sound in vacuum.

REPLACE "intricate ladder structure" with "simple solid metal ladder rungs" → prevents impossible AI geometry hallucination.

🔴 DERS 12: EŞ ZAMANLI YERÇEKİMİ ÇELİŞKİSİ
Kaynak: (not supplied) QA — Motion Quality: 2/10 — 0:00 — Mixed gravity vectors
Sorun: Karakterin hareketleri (ağır adımlar, vücut ağırlığı) Dünya yerçekiminde gibi görünürken, aynı karedeki objeler (kopan paneller) sıfır yerçekiminde süzülüyor. Fizik kuralları aynı kare içinde tutarsız çalışıyor.
ÇÖZÜM — PROMPT GÜNCELLEMESİ:

uniform zero-gravity physics for all elements, weightless locomotion, no gravitational weight on subject

OUT-OF-SCOPE FLAGS
0:13, 0:25, 0:54 — Character's face and suit details (patches, tubing) change drastically across the scene cuts → CONTINUITY lens

FLAGS FOR DOCUMENT CHECK
0:00 — Atmosphere reads as vacuum but loud audio exists — QUESTION: Is the film intended to have stylized, non-literal audio?

0:00 — Character climbs ladder with full weight — QUESTION: Was the locomotion mode specified as walking/climbing or tether-pulling/floating?

QUALITY TABLE ROW
| (not supplied) Ⓥ | DİKEY | Compilation | 4/10 | 2/10 | 10/10 | 10/10 | 6/10 | | 4/10 | 1/10 | | 2/10 | 6/10 | 6/10 | 10/10 | 3 | 5.5/10 |
