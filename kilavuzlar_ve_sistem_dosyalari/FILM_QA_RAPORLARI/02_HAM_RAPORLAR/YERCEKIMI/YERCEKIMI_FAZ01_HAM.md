# YERÇEKİMİ — FAZ 1 · HAM QA RAPORU

```
KÜNYE
  Film        YERÇEKİMİ (yatay_10_20_dk_filmler/YERCEKIMI)
  Malzeme     FAZ 1 makarası · 10 parça · 80 s (rapor beyanı)
  Rubrik      FAZ_01_GOREV/FAZ_01_QA_PROMPT.md — ⭐ SIRADAN BAĞIMSIZ sürüm
              (kadraj kataloğu A-K; denetçiye sahne numarası verilmedi)
  Tarih       01.09.2026
  Mod         ⚠️ V (ÖN KOŞU) — film klasöründe *_QA_SPEC.md YOK [D129]
  Master      ⛔ ELDE YOK — ⑪ ölçüm kapısı koşulamadı; raporun süre ve
              parça sayıları DOĞRULANMADI, yalnız beyandır
  ⛔ Faz koşusudur: T1-T4 skor tablolarına GİRMEZ [00_PLAN §faz klasörü]
```

⛔ Aşağısı raporun BİREBİR kendisidir — özetlenmedi, düzeltilmedi [AGENTS kural ④].

---

MATERIAL
Measured total duration = 80 seconds
Number of distinct shot segments = 10
Measured shot length = 8.0 seconds
All segments are the same length within 0.3 s.
Gate passed.

SEGMENT MAP
Segment 1 | 00:00 - 00:08 | 8.0s
Segment 2 | 00:08 - 00:16 | 8.0s
Segment 3 | 00:16 - 00:24 | 8.0s
Segment 4 | 00:24 - 00:32 | 8.0s
Segment 5 | 00:32 - 00:40 | 8.0s
Segment 6 | 00:40 - 00:48 | 8.0s
Segment 7 | 00:48 - 00:56 | 8.0s
Segment 8 | 00:56 - 01:04 | 8.0s
Segment 9 | 01:04 - 01:12 | 8.0s
Segment 10 | 01:12 - 01:20 | 8.0s

IDENTIFICATION TABLE
Segment 1 | 00:00-00:08 | A | High | One tiny figure, wide, closing panel
Segment 2 | 00:08-00:16 | B | High | Wide profile, shuttle visible
Segment 3 | 00:16-00:24 | C | High | Over shoulder, two figures
Segment 4 | 00:24-00:32 | D | High | Close on female face
Segment 5 | 00:32-00:40 | E | High | Macro top-down on latch
Segment 6 | 00:40-00:48 | F | High | Glove on arm, lit segments
Segment 7 | 00:48-00:56 | H | High | Back view, working latch
Segment 8 | 00:56-01:04 | I | High | Two figures, lateral wide, moving
Segment 9 | 01:04-01:12 | J | High | Wide from above, line in sky
Segment 10 | 01:12-01:20 | K | High | One figure raises head

MATCHED / MISSING / UNMATCHED
MATCHED: A, B, C, D, E, F, H, I, J, K
MISSING: G
UNMATCHED: None

PASSPORTS AS SEEN
Woman: Oval face, dark hair. Wears a white suit with orange stripes. Visor is a seamless curved glass dome without a metal frame.
Man: Broad build, white suit with navy stripes.
Platform: White lattice truss, orange rails, grey cylinder.
Shuttle: White, open cargo doors, nose oriented screen-right.
Sky: Earth below, black space above, thin dotted line upper left.

THE COMMANDER'S BACK UNIT - OBSERVATION ONLY
The unit is a flat rectangular slab, taller than it is wide, with recessed seams and flush corner nozzle recesses. It does not possess an open tubular frame or protruding arms. The geometry is consistent across his appearances.

SCORES

COVERAGE: 6 - Missing G, all others identified.

IDENTITY CONTINUITY: 6 - Facial features remain stable.

HELMET AND VISOR GEOMETRY: 3 - Visors render consistently as seamless domes, missing frames entirely.

COSTUME AND BACK: 3 - Woman wears a backpack in Seg 7; watch appears on left arm in Seg 5.

FIGURE COUNT AND CLONE CONTROL: 7 - Counts strictly accurate.

CAMERA DISCIPLINE: 7 - Locked off with zero movement.

LIGHT AND SHADOW: 6 - Light placement correct, minor bloom.

VACUUM PHYSICS: 3 - Tether curves; shuttle drifts.

TEXT AND SYMBOL DISCIPLINE: 3 - Readable text appears on suits.

WORLD CONSISTENCY: 3 - Shuttle orientation flips; counters wrong.

DELIVERY HYGIENE: 7 - No watermarks, correct segment timing.
Mean: 4.9

TOP 5 CRITICAL

Seg 3 | 00:16-00:24 | C | RED | Readable text on commander's chest | Violates absolute zero-text lock.

Seg 4 | 00:24-00:32 | D | RED | Visor is a curved seamless dome | Violates fragile flat-pane lock.

Seg 7 | 00:48-00:56 | H | RED | Woman wearing a life-support pack | Violates flat-back separation lock.

Seg 2 | 00:08-00:16 | B | RED | Shuttle nose points screen-right and drifts | Orientation flipped and physics violated.

Seg 6 | 00:40-00:48 | F | RED | Strip displays five lit segments | Violates strict two-of-four lock.

FINDINGS BY SEGMENT
Segment 1 (A): Verified 1 figure, bolt straight. Deviation: 00:03 Tether curved under gravity (RED). 00:05 Dome visor (RED).
Segment 2 (B): Verified 1 figure profile. Deviation: 00:09 Shuttle drifts (RED). 00:10 Shuttle nose right (RED).
Segment 3 (C): Verified 2 figures. Deviation: 00:18 Mouths moving (RED). 00:19 Text on suit (RED).
Segment 4 (D): Verified face readable. Deviation: 00:25 Mouth moving (RED). 00:26 Dome visor (RED).
Segment 5 (E): Verified latch action. Deviation: 00:34 Watch on left wrist (RED).
Segment 6 (F): Verified navy cuff. Deviation: 00:42 Five lit segments instead of two (RED).
Segment 7 (H): Verified working latch. Deviation: 00:50 Pack on her back (RED).
Segment 8 (I): Verified 2 figures. Deviation: 00:58 Shuttle pointing right (RED).
Segment 9 (J): Verified line grows. Deviation: 01:08 Figure looks up at line (RED).
Segment 10 (K): Verified 1 figure. Deviation: 01:14 Looks up/left instead of right (RED).

CROSS-SHOT CHECKS

Yes, her face holds.

No, visors are curved domes across all segments.

Yes, flat rectangular slab holds.

No, shuttle nose is screen-right in B and I.

Yes, platform geometry holds.

Panel is open in A, sealed in B and J.

His fuel strip displays five segments in F.

Yes, Earth below and sky line upper-left hold.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Fixable: None.
Requires Regeneration: Segments 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

FLAGS FOR DOCUMENT CHECK

Is the watch appearing on the left wrist in Segment 5 a mirrored render error, or was the passport handedness inverted?

Does the flat rectangular back unit match the preferred production design?

WHAT WORKED
Camera discipline was flawless across the reel with zero internal movement. Figure counts rigorously adhered to the catalogue specifications in every segment. Earth bounce lighting was accurately positioned below the subjects.
