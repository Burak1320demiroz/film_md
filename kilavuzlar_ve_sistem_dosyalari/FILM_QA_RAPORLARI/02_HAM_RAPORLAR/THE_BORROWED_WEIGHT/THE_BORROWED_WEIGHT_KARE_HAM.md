# 🔧 THE BORROWED WEIGHT — ① KARE_QA HAM RAPORU

> Çalıştırma: 24.08.2026 · **mod V** (SPEC dosyası hazırdı, VERİLMEDİ → ⛔ ön koşu [D94/D117])
> Rubrik: `../QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md`
> Malzeme: tam kurgu (operatörün beyanı yok; rapor 266 s "measured" diyor)
> ⚠️ Dört mercekli partinin parçası. **Parti ⑤ ÇAPRAZ SAYIM kapısından geçmedi**
> (kesme sayıları 26 · 24 · 24 · 25 → fark 2) → 🚨 GEÇERSİZ; skor satırı
> T1 tablosuna İŞLENMEDİ.
> Kapı defterleri, ızgara geri alma ve çapraz gözlem tablosu:
> `../01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④). Tablolar sohbetten
> yapıştırıldığı için boru işaretlerini kaybetmiştir; sayılar değiştirilmemiştir.

---

FORMAT: YATAY
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 266s MEASURED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 26 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00, 4:10, 4:20)

SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES:  8
SUM OF SCORES:      56.0
DIVISION:           56.0 ÷ 8 = 7.0

OVERALL SCORE: 7.0/10 (Excluded 6 categories: Creatures, Frame Anchor Fidelity, Vertical Format, Safe Zone, Hook Timing as N/A or UNVERIFIABLE; Negative Violations as count)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    2/10    −2 · 0:58 (F1) · −2 · 1:16 (F2) · −2 · 1:43 (F3) · −2 · 2:32 (F4)
Scale & Physics    4/10    −3 · 1:13 (F1) · −3 · 3:17 (F2)
Camera    10/10    no in-scope source
Lighting    8/10    −1 · 3:04 (F1) · −1 · 3:51 (F2)
Environment    10/10    no in-scope source
Creatures    N/A    no in-scope source
Particles & Materials    8/10    −2 · 1:45 (F1)
Dialogue & Audio    5/10    −5 · 4:20 (F1)
Frame Anchor Fidelity    UNVERIFIABLE    no in-scope source
Negative Violations    5 count    [x] Text [x] AI bloom [x] Object phasing [x] Hand-surface fusion [x] Frozen particles
Motion Quality    9/10    −1 · 1:15 (F1)
Vertical Format (9:16)    N/A    no in-scope source
Safe Zone    N/A    no in-scope source
Hook Timing    N/A    no in-scope source

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 266s
Cuts you can see: 26 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00, 4:10, 4:20)
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Older male, graying beard, dark skin. First frame fully visible: 1:10
Suit / wardrobe: Off-white bulky space suit, square chest plate, dark grey gloves, patch on left shoulder.
Wear / dirt: Dirty on lower legs and knees, smudges on chest.
Equipment: Helmet with clear spherical visor, brass-colored gauge/scale.

THE WORLD
Gravity read: Feels close to 1g, dust settles quickly, heavy objects fall fast.
Atmosphere read: Dense enough for wind and dust storms to carry, sound carries.
Light sources: Diffuse overcast daylight from above, some glowing cyan elements on ships/doors.
Location: Desolate grey sandy plain with scattered ship wreckage.

MOTION
Camera: Mostly slow pushes and static lockoffs.
Subject: Walking slowly, lifting heavy objects.

PRESENCE STRING
1111111111111111-11111-111

SEVERITY TALLY
🔴 BLOCKER: 5    🟠 MAJOR: 4    🟡 MINOR: 1

TOP 3 CRITICAL ERRORS
1:43 — 🔴 BLOCKER — Object phasing: Character's hands push completely through the solid metal geometry of the solar panel.

1:13 — 🔴 BLOCKER — Object morphing: The brass scale completely loses structural integrity and dynamically morphs into a different design in the character's hands.

4:20 — 🔴 BLOCKER — On-screen text: Burned-in title text ("THE BORROWED WEIGHT") appears on screen, violating the clean frame rule.

DETAILED ERROR LOG
0:58 — 🔴 BLOCKER — Character — Contact morphing: Fingers fuse and melt into the metal wrenches as they are picked up.
1:13 — 🔴 BLOCKER — Scale & Physics — The entire brass scale dynamically morphs, altering its geometry and dial shape mid-shot.
1:15 — 🟡 MINOR — Motion Quality — Slight jello effect on the brass scale as it transforms.
1:16 — 🔴 BLOCKER — Character — Contact morphing: Hand holding the upper ring of the scale merges physically with the brass ring.
1:43 — 🔴 BLOCKER — Character — Object phasing: Both hands sink completely through the solid texture of the solar panel while pushing.
1:45 — 🟠 MAJOR — Particles & Materials — Dust kicked up by the falling panel hovers and freezes statically instead of dispersing.
2:32 — 🔴 BLOCKER — Character — Contact morphing: Fingers phase through the flat surface of the metal wall being pushed.
3:04 — 🟠 MAJOR — Lighting & Color — Severe AI bloom on the small glowing orb, creating a dreamy haze that washes out the suit.
3:17 — 🟠 MAJOR — Scale & Physics — The dropped scale falls with balloon-like, low-mass physics that contradicts the established gravity.
3:51 — 🟠 MAJOR — Lighting & Color — AI bloom effect present on the glowing cyan hatch in the ground.
4:20 — 🔴 BLOCKER — Dialogue & Audio — Burned-in title text ("THE BORROWED WEIGHT") appears on screen.

NEGATIVE BIBLE VIOLATIONS
NEGATIVE BOX COUNT: 5 · LINKED FINDINGS: 5 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 5 · TICKED: 5 · MISSED: 0

[x] Text, subtitles, captions, or watermarks visible on screen

[x] AI bloom / soft glow filter / dreamy haze on light sources

[x] Object phasing/clipping (any solid passing through another solid)

[x] Extra fingers, phantom digits, or hand-surface fusion

[x] Frozen or static particles (dust, exhaust, smoke that doesn't disperse)

WHAT WORKED WELL
The character's face model remains highly consistent across different framing distances.

The environment's desolate mood and overarching color grading stay robust throughout the compilation.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "sharp, distinct fingers with firm contact boundaries, no intersecting geometry" → prevents hand-surface fusion

REMOVE from image prompt: "cinematic lighting" → causes AI bloom and soft dreamy glow on light sources

REPLACE "heavy impact" with "physical mass collision with rapid dust dispersion" → prevents frozen hovering dust particles

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above [2, 3, 4, 5, 8, 10, 11].

OUT-OF-SCOPE FLAGS
0:33 — identical repeated voiceover line from 0:23 without apparent narrative cause → SOUND lens

FLAGS FOR DOCUMENT CHECK
0:55 — wrenches fall with surprisingly low mass — was a specific gravity value requested?
3:17 — scale bounces lightly — is this a micro-gravity environment?

QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 2/10 | 4/10 | 10/10 | 8/10 | 10/10 |  | 8/10 | 5/10 |  | 9/10 |  |  |  | 5 | 7.0/10 |
