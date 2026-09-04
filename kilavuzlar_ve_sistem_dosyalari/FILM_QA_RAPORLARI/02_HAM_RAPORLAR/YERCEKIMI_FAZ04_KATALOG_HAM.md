# YERÇEKİMİ — FAZ 4 · GEÇİŞ B (KATALOG) · HAM QA RAPORU

```
KÜNYE
  Film        YERÇEKİMİ (yatay_10_20_dk_filmler/YERCEKIMI)
  Malzeme     FAZ 4 makarası · 12 parça · ⛔ 120 s (rapor beyanı)
  ⛔⛔ IZGARA: 10,0 s/klip. F1-F3 = 8,0 s. → D124, 4. vaka (ilk kez FİLM İÇİNDE)
  Rubrik      FAZ_04_FEDA/FAZ_04_QA_PROMPT.md — 🅱️ PROMPT B (KATALOG)
  Motor       Gemini · ⭐ GEÇİŞ A'DAN AYRI SOHBET (mühür korundu)
  Tarih       02.09.2026
  Mod         ⚠️ V — *_QA_SPEC.md YOK [D129] · master YOK [⑪]
  ⛔ Faz koşusudur: T1-T4 skor tablolarına GİRMEZ

⚠️ SINIRI [D164]: bu geçişte her tarif önden verildi. Buradaki bir
   tarifin geri gelmesi ÇAPA DEĞİLDİR. Bulgu ancak GEÇİŞ A da bağımsız
   gördüyse SAĞLAM sayılır.
```

⛔ Aşağısı raporun BİREBİR kendisidir — özetlenmedi, düzeltilmedi [AGENTS kural ④].

---

MATERIAL
measured total duration           = 120 seconds
number of distinct shot segments  = 12
measured shot length = total / segment count = 10 seconds

The measured shot length is explicitly 10 seconds. All segments are the same length within 0.3 s.

SEGMENT MAP
Segment 1 | 0:00-0:10 | A | Low | Two people at the hull, smaller person tangled in grey cords.
Segment 2 | 0:10-0:20 | B | Low | Close-up of female face outside, closing eyes.
Segment 3 | 0:20-0:30 | C | High | Macro of boot with thin grey cord wrapped around it.
Segment 4 | 0:30-0:40 | D | High | Close-up of the man's face outside.
Segment 5 | 0:40-0:50 | E | High | Macro of boot (identical framing to C) but with thick white rope.
Segment 6 | 0:50-1:00 | F | High | Square-on face close-up, glove enters from bottom edge.
Segment 7 | 1:00-1:10 | UNMATCHED | High | Two figures, man pushes a rigid orange pole into cords.
Segment 8 | 1:10-1:20 | H | Low | Wide shot of two figures, man drifting away with trailing rope.
Segment 9 | 1:20-1:30 | I | High | Extreme wide shot of the whole station with two tiny figures.
Segment 10 | 1:30-1:40 | UNMATCHED | High | Woman crawling along exterior hull pulling thick white rope.
Segment 11 | 1:40-1:50 | K | High | Woman at circular white airlock hatch.
Segment 12 | 1:50-2:00 | L | High | Woman inside brightly lit padded airlock, no helmet.

IDENTIFICATION TABLE
MATCHED: A, B, C, D, E, F, H, I, K, L
MISSING: G, J
UNMATCHED:

Segment 7 (1:00-1:10): Medium-wide shot of two figures outside. The smaller person is clustered in tangled grey cords. The larger person stands above, holding a rigid, straight orange pole and pushing it down toward the smaller person.

Segment 10 (1:30-1:40): Medium shot of the woman crawling along an intact, pristine section of the white quilted hull, pulling heavily on a thick white rope with an orange stripe.

PASSPORTS AS SEEN

The woman: Face matches a woman in her 30s with fair skin, scattered freckles, and brown eyes. Hair is short and brown (visible in Seg 12). Suit has a white base with orange stripes. Back: Flat in Segs 1 and 11, but carries a large rigid white backpack in Seg 8. Head covering: Rigid clear helmet outside with a metallic grey border. No helmet inside (Seg 12).

The man: Broader, taller build. Suit is white with grey/black stripes (NOT navy blue). His back carries a large, rigid white rectangular backpack.

The station: Made of white, square-quilted cylindrical modules with dark rectangular solar panels at the far ends. It is completely intact in Segs 1, 9, 10, and 11, but features a massive, jagged hole torn into the side in Seg 8.

The cord and tether: Thin grey cord is tangled in Seg 1 and wrapped tightly 4 times in Seg 3. A completely different thick white rope with an orange stripe appears wrapped tightly 4 times in Seg 5, and trailing in Segs 8, 10, and 11. No wraps are loose.

The counters: No segment shows loops dropping. Loops remain statically at 4 in both Seg 3 and Seg 5. The six-segment amber wrist ring is entirely absent/dark in all segments.

The light and Earth: Hard white light from the upper screen-right outside, casting deep black shadows. Earth's curved limb is visible low in frame in Segs 7, 8, 9, and 10. Indoors (Seg 12) is evenly lit with bright white light, missing the targeted amber patch.

THE COMMANDER'S BACK UNIT - OBSERVATION ONLY
The back unit is one solid, closed rectangular object. It is taller than it is wide, spanning roughly the width of his shoulders, and stands out about 12 to 18 inches off his back. Its edges are straight with rounded corners. The surface is divided into flat white panels. Two small, conical thruster nozzles project downward from the bottom corners, standing flush with the base. There is no visible four-segment indicator strip anywhere on it. It appears to be the exact same object in Segs 1, 4 (implied edge), and 8.

THE STATION - OBSERVATION ONLY
The station consists of multiple cylindrical modules joined in a straight line, covered entirely in white square quilting. The spine joining them is heavily structured. Dark rectangular solar panels are attached symmetrically at both extreme ends. In Segment 8, there is a massive, jagged hole torn directly into the side of the main body module, exposing the dark interior framework. The airlock hatch is a raised circular white rim on the side of a module. The close entries completely disagree with Segment 8; Segments 1, 9, 10, and 11 show a perfectly pristine, undamaged quilted hull where the massive puncture should be.

C VERSUS E
Segments 3 and 5 are deliberately framed identically, showing the same white and orange boot resting on the same white quilted hull with an orange bracket in the background.
Differences:

Segment 3 features a thin grey cord wrapped around the ankle. Segment 5 features a thick white rope with an orange stripe.

In Segment 5, the boot pulls back slightly against the tension; in Segment 3, it is static.
Verdict on drops: Both segments completely fail their catalogue descriptions. Neither starts at 3 loops (both show exactly 4 loops). Segment 5 (E) does NOT drop from 3 to 2 on screen; the 4 loops remain static. Segment 3 (C) holds at 4, not 3.

SCORES

COVERAGE: 7

IDENTITY CONTINUITY: 8

HELMET PRESENCE AND CLARITY: 10

COSTUME AND BACK: 2

FIGURE COUNT AND CLONE CONTROL: 8

CAMERA DISCIPLINE: 8

LIGHT AND SHADOW: 7

THE RELEASE: 1

VACUUM MOTION: 3

COUNTERS: 1

STATION ROTATION: 1

WORLD CONSISTENCY: 2

TEXT AND DELIVERY HYGIENE: 3
Overall Score: 4.7

TOP 5 CRITICAL

Missing Narrative Actions: The hook release (G) and the boot freeing (J) are entirely absent, replaced by unmatched segments of an orange pole and crawling.

Station Continuity Failure: The station features a massive catastrophic puncture in Seg 8, but is flawlessly intact in all other close and wide exterior shots (Segs 1, 9, 10, 11).

The Woman's Back: She wears a large, rigid white backpack in Seg 8, which is a maximum severity finding against the locked "flat back" requirement.

Counter Failure: Segments 3 (C) and 5 (E) fail as counters. They display 4 loops of mismatched ropes (grey cord vs thick white rope) and no loops ever drop on screen.

Station Rotation Failure: The sky explicitly does NOT slide in D (Seg 4), H (Seg 8), or I (Seg 9), breaking the physical premise of the entire phase.

FINDINGS BY SEGMENT

Segment 1 (0:00-0:10, A): Camera does not skim. No physical strike or bounce occurs; the figures are static.

Segment 2 (0:10-0:20, B): No hard jolt or helmet knocking against the hull. The eyes simply close.

Segment 3 (0:20-0:30, C): Shows 4 loops of cord, not 3.

Segment 4 (0:30-0:40, D): The sky does not slide. He does not hang from a tether. His suit stripes are grey/black, not navy blue.

Segment 5 (0:40-0:50, E): Shows 4 loops of a completely different thick white rope. No loop slides off or snaps away.

Segment 6 (0:50-1:00, F): Visibly moving mouth (speech lock violation). She does not shake her head. Glove has a grey ribbed cuff, missing the wrist ring.

Segment 7 (1:00-1:10, UNMATCHED): Introduces an unscripted rigid orange pole.

Segment 8 (1:10-1:20, H): Woman is wearing a large backpack (maximum severity). Station has a massive hole. Rope is curved and slack, not straight. No slow pull-back.

Segment 9 (1:20-1:30, I): The sky does not slide.

Segment 10 (1:30-1:40, UNMATCHED): Shows unscripted crawling. Station is suddenly pristine again.

Segment 11 (1:40-1:50, K): No lever turning occurs. Gloves are plain white, missing both the grey cuff from earlier and the wrist ring.

Segment 12 (1:50-2:00, L): Lighting is entirely bright white, lacking the specific cold panel and amber patch. The stopped watch is missing from her right wrist.

CROSS-SHOT CHECKS

YES, she is the same person in all her entries (Segments 1, 2, 6, 8, 10, 11, 12).

YES, he is the same person in all four of his entries (Segments 1, 4, 7, 8).

YES, she is wearing a helmet in every exterior shot (Segments 1, 2, 6, 8, 10, 11). There are no exterior shots where her head is bare.

YES, you can tell she is wearing a helmet, and the glass is optically clear making her face fully readable in Segments 2, 4, and 6.

NO, her back is not flat wherever visible. It is flat in Seg 1 and Seg 11 (K). However, in Seg 8, she is wearing a large, rigid white backpack. K (Seg 11) confirms the flat back, but Seg 8 violates it.

YES, his back unit is the same object in Segments 1, 4, 7, and 8.

The loops are exactly 4 at the first and last frame of Seg 3. The loops are exactly 4 at the first and last frame of Seg 5. The count does NOT drop 3 to 2 in E. The count does NOT drop 2 to 0 in J (missing). It does not go up, but it starts incorrectly at 4.

Segment 3 uses thin grey cord; Segment 5 uses a thick white rope with an orange stripe. Neither entry shows 3 loops, and E does not show the drop.

The ring is 0 in all entries. It is not legible or present on her cuffs, completely failing the 3 -> 2 drop in J and the reading of TWO in K (Seg 11).

YES, his arm strip is completely dark/absent in all entries he appears in.

YES, there is NO thruster plume anywhere in this reel.

The sky does NOT slide in any entry. It fails to slide in Segments 4 (D), 8 (H), and 9 (I).

The release in G is MISSING from the reel. No hand visibly opens a hook.

NO, the trailing pinkish-white line in Seg 8 curves and arcs; it is not dead straight.

YES, the hull is on the screen-left or bottom in every exterior entry.

YES, the sun is low and golden from the upper screen-right, throwing long hard black shadows outside in Segments 1, 3, 5, 7, 9, 10, and 11.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION

Segments 1, 2, 4, 6, 8, and 9 require REGENERATION due to missing physics (no slide), missing actions (no bounce/helmet knock), and speech lock violations.

Segments 3 (C) and 5 (E) require REGENERATION to correct the rope materials, loop counts, and to animate the physical drop of the loop.

Segments 7 and 10 require REGENERATION to become the missing entries G and J.

Segments 11 and 12 could be FIXABLE in edit (crop/trim) if the absent lever turn and absent watch are ignored, but technically require regeneration to meet the exact script.

FLAGS FOR DOCUMENT CHECK

The man's suit stripes consistently generated as grey/black, not navy. Check if the prompt for his suit is sufficiently weighted for the color navy blue.

The massive hole in the station in Seg 8 completely contradicts the pristine station in all other shots. The physical state of the hull needs a master lock.

WHAT WORKED

The helmet glass is optically clear and face readability is excellent in all close-ups (Segments 2, 4, 6), maintaining zero tint or mirror reflection.

The lighting properly throws deep, razor-edged black shadows across the white quilting outside.

Her interior performance in L (Segment 12) captures the slow rotation perfectly without gravity affecting her speed as she curls.
