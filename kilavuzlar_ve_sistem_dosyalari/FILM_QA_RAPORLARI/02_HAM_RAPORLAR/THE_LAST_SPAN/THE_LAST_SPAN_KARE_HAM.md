# ① 🔧 KARE — HAM RAPOR · THE LAST SPAN · 25.08.2026

> ⛔ Model çıktısı OLDUĞU GİBİ. Düzenlenmedi, kısaltılmadı [AGENTS kural ④].
> İşleme, kapı sonuçları ve geçerlilik kararı:
> `../01_FILM_RAPORLARI/THE_LAST_SPAN.md`
>
> ⚠️ Bu koşu bir ÖN KOŞU'dur — kurgu kapısı 3/3 ihlal + D110 oturum
> bulaşması. Skorları hiçbir tabloya işlenmedi.

---

```
INPUT MODE: V
FORMAT: YATAY
BASELINE: SELF-CONSISTENCY + PHYSICS
FILM: (not supplied)
ASPECT MEASURED: 16:9 · LENGTH CLASS: (not supplied) · SCENE: Compilation
VIDEO DURATION: 114s measured · MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 10 (0:10, 0:19, 0:29, 0:39, 0:50, 0:59, 1:10, 1:18, 1:33, 1:40)
NON-SCENE MATERIAL: 1:50-1:54 title card
LINES HEARD: none
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES: 7 · SUM: 35.0 · DIVISION: 35.0 / 7 = 5.0
OVERALL SCORE: 5.0/10 (6 excluded: Creatures, Audio, Frame Anchor, 9:16, Safe Zone, Hook)
VERDICT: REGENERATE

SCORES SUMMARY
| Category | Score | Critical Issues |
|---|---|---|
| Character | 4/10 | -6 · 1:02 (F1) · 1:24 (F2) |
| Scale & Physics | 3/10 | -7 · 0:15 (F1) · 0:33 (F2) |
| Camera | 5/10 | -5 · 1:28 (F1) |
| Lighting | 7/10 | -3 · 0:10 (F1) |
| Environment | 6/10 | -4 · 0:52 (F1) |
| Creatures | UNVERIFIABLE | no in-scope source |
| Particles & Materials | 6/10 | -4 · 0:03 (F1) |
| Dialogue & Audio | N/A | no in-scope source |
| Frame Anchor Fidelity | UNVERIFIABLE | no in-scope source |
| Negative Violations | 6 count | 6 linked |
| Motion Quality | 4/10 | -6 · 0:30 (F1) |
| Vertical Format (9:16) | N/A | no in-scope source |
| Safe Zone | N/A | no in-scope source |
| Hook Timing | N/A | no in-scope source |

SCENE INVENTORY
MATERIAL: compilation edit · 114s · cuts 10 · aspect 16:9
THE CHARACTER: Brunette woman, short hair tied back, smudged dirt on cheeks.
  First frame fully visible 0:10. Orange mechanic/flight jumpsuit, black
  gloves, black boots. Moderate dust and soot on thighs, chest, shoulders.
  Holding a silver metal jerrycan.
THE WORLD: Gravity mixed - 1g for walking, sub-1g for jumping/falling.
  Dense dusty air, haze visible. Sun/directional light from the right,
  hard light casting deep shadows. Long highway bridge packed with
  abandoned cars and petrified dust-covered people. Largest background
  object: bridge structure and distant rolling hills.
MOTION: Camera ranges from static lockoffs to slow pushes and tracking
  shots following the subject. Woman walking, climbing, jumping across
  vehicles.

PRESENCE STRING
11111111111

SEVERITY TALLY
BLOCKER: 5 · MAJOR: 4 · MINOR: 0

TOP 3 CRITICAL ERRORS
0:15 - BLOCKER - Object phasing: right foot phases completely through the
  solid metal hood/windshield of the car.
0:30 - BLOCKER - Mixed gravity: the jumping motion exhibits floaty sub-1g
  physics which contradicts the 1g planted steps.
1:02 - BLOCKER - Hand-surface fusion: the handle of the jerrycan morphs and
  fuses seamlessly into her black glove.

DETAILED ERROR LOG
0:03 - MAJOR - Particles & Materials - Dust and debris from the collapsing
  figures clip straight through the car geometries rather than colliding,
  piling, or bouncing.
0:10 - MAJOR - Lighting - A soft AI bloom/glow filter affects the bright
  orange suit, clashing with the harsh directional lighting.
0:15 - BLOCKER - Scale & Physics - The character's right foot phases
  entirely through the solid metal hood and windshield of the car.
0:30 - BLOCKER - Motion Quality - The jumping motion exhibits extremely
  floaty sub-1g physics, contradicting the 1g planted steps seen during
  walking (mixed gravity).
0:33 - BLOCKER - Scale & Physics - As she lands, the jerrycan phases
  directly through her right leg/knee.
0:52 - MAJOR - Environment - The surface textures on the road and the
  petrified bodies in the foreground breathe and morph continuously
  (texture swimming).
1:02 - BLOCKER - Character - The handle of the jerrycan morphs and fuses
  seamlessly into her black glove as she steps up onto the trunk.
1:24 - MAJOR - Character - The character's jawline visibly widens and her
  cheekbone structure shifts during the walk cycle (face morphing).
1:28 - BLOCKER - Camera - There is a micro-stutter/jump in the character's
  walk cycle and camera tracking, acting as a hidden cut within a
  continuous motion.

NEGATIVE BIBLE VIOLATIONS (ticked)
[x] Any visible CUTS or TRANSITIONS
[x] AI bloom / soft glow filter / dreamy haze on light sources
[x] Face morphing
[x] Object phasing/clipping
[x] Swimming/animated rock textures on geological surfaces
[x] Extra fingers, phantom digits, or hand-surface fusion
NEGATIVE BOX COUNT: 6 · LINKED FINDINGS: 6 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 6 · TICKED: 6 · MISSED: 0
NO BOX EXISTS FOR: mixed gravity vectors (Cat 11)

WHAT WORKED WELL
- Excellent colour contrast and compositional separation between the bright
  orange suit and the desaturated dusty environment.
- The conceptual aesthetic of the petrified/dust people is visually striking
  and held its structural integrity well in the extreme wide shots.

PROMPT IMPROVEMENT SUGGESTIONS
1. ADD to video prompt: "perfect solid collision, firm ground contact,
   weight-bearing steps" -> prevents object phasing/clipping.
2. REMOVE from image prompt: "cinematic lighting" -> causes AI bloom.
3. REPLACE "dynamic jump" with "heavy 1G jump, fast parabolic fall"
   -> prevents mixed gravity vectors.

NEW LESSON CANDIDATE
No new lesson - all errors map to the failure patterns listed above
(1, 3, 4, 6).

OUT-OF-SCOPE FLAGS
0:59 - The environment layout drastically shifts from a packed bridge to an
  empty road with neatly lined bodies. -> CONTINUITY lens.

FLAGS FOR DOCUMENT CHECK
1:18 - Woman walks away without the jerrycan - QUESTION: was dropping the
  prop scripted here?

QUALITY TABLE ROW
| (not supplied) V | YATAY | Compilation | 4 | 3 | 5 | 7 | 6 | | 6 | | | 4 | | | | 6 | 5.0/10 |
```
