# 🔧 THE ROSE COAT — ① KARE HAM RAPORU

> **Koşu:** 26.08.2026 · mod V (SPEC dosyası VARDI, verilmedi → ÖN KOŞU [D94/D117])
> **Rubrik:** `../../QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md`
> **Atıf:** rapor `FILM: (not supplied)` yazdı; kimlik kapısı ③ operatör
> tarafından koşuldu — iki metin-dışı çapa tuttu (gömülü mekik S2 · 13×10 s
> ızgara + insansız hook yuvası). Ayrıntı film kaydında.
> ⛔ Aşağısı MODELİN ÇIKTISIDIR, düzeltilmemiştir.

---

```
INPUT MODE: V
FORMAT: YATAY
BASELINE: SELF-CONSISTENCY + PHYSICS

FILM: (not supplied)
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 135s measured
MATERIAL TYPE: FILM
CUTS COUNTED: 13 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10)
NON-SCENE MATERIAL: 2:10-2:15 title card
LINES HEARD: none
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  7
SUM OF SCORES:      35.0
DIVISION:           35.0 ÷ 7 = 5.0

OVERALL SCORE: 5.0/10 (6 categories excluded as UNVERIFIABLE or N/A)
VERDICT: REGENERATE
```

## SCORES SUMMARY

| Category | Score | Critical Issues |
|---|:--:|---|
| Character | 2/10 | −8 · 1:05 (F1) · 1:18 (F2) · 2:02 (F3) |
| Scale & Physics | 3/10 | −7 · 0:03 (F1) · 0:45 (F2) · 1:13 (F3) |
| Camera | 10/10 | no in-scope source |
| Lighting | 7/10 | −3 · 0:22 (F1) |
| Environment | 5/10 | −5 · 1:33 (F1) |
| Creatures | N/A | no creatures |
| Particles & Materials | 4/10 | −6 · 0:55 (F1) · 1:25 (F2) |
| Dialogue & Audio | UNVERIFIABLE | (no sound) |
| Frame Anchor Fidelity | UNVERIFIABLE | (mode V) |
| Negative Violations | 5 count | — |
| Motion Quality | 4/10 | −6 · 0:12 (F1) · 0:32 (F2) |
| Vertical Format (9:16) | N/A | no in-scope source |
| Safe Zone | N/A | no in-scope source |
| Hook Timing | N/A | no in-scope source |

## SCENE INVENTORY

```
MATERIAL
What you were given: compilation edit · duration 135s
Cuts you can see:    13 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20,
                     1:30, 1:40, 1:50, 2:00, 2:10)
Aspect ratio:        16:9

THE CHARACTER — as first clearly seen
Face / hair / marks: mostly obscured by visors.  First frame fully visible: 0:10
Suit / wardrobe:     red/pink base coveralls, rectangular chest/back utility
                     panels, black utility straps.
Wear / dirt:         heavy pink sand accumulation on lower legs and back panels.
Equipment:           clear or opaque spherical visors, white/grey boots, black
                     gloves, handheld brushes.

THE WORLD — as the footage shows it
Gravity read:     ~1g (sand falls quickly, walking steps read as standard weight)
Atmosphere read:  dense enough for dust to hang, producing a hazy pink sky;
                  no vacuum visible.
Light sources:    singular strong directional sun (high angle), casting hard,
                  sharp shadows.
Location:         desert outpost with modular white habitat structures and
                  spacecraft.

MOTION
Camera:  static lockoffs or very slow, steady push-ins.
Subject: walking, falling, brushing sand, climbing ladders.
```

## PRESENCE STRING

```
-111111111111
```

## SEVERITY TALLY

```
🔴 BLOCKER: 7    🟠 MAJOR: 4    🟡 MINOR: 0
```

## TOP 3 CRITICAL ERRORS

1. `0:03` — 🔴 BLOCKER — Impossible physics: Sand pours out of a flat geometric
   slit in the wall with no physical volume or logical source, acting like a 2D
   fluid generator.
2. `2:02` — 🔴 BLOCKER — Contact morphing: While climbing the ladder, the
   astronaut's hands and fingers completely phase through the solid metal rungs
   instead of wrapping around them.
3. `1:18` — 🔴 BLOCKER — Text visible on screen: The word "rose" clearly appears
   written across the astronaut's backpack, violating the strict negative rule
   against in-world text.

## DETAILED ERROR LOG

```
0:03 — 🔴 BLOCKER — Scale & Physics — Sand pours continuously from a narrow
       horizontal wall groove that possesses no internal volume, defying
       physical logic.
0:12 — 🔴 BLOCKER — Motion Quality — The character slides/moonwalks across the
       sand; feet do not lock to the ground geometry during the stride.
0:22 — 🟠 MAJOR — Lighting — Shadow mismatch: The deep shadow cast by the buried
       shuttle runs horizontally left, while the characters cast shadows
       directly downward/forward.
0:32 — 🟠 MAJOR — Motion Quality — Pronounced jello/glide effect during the walk
       cycle toward the lander; weight distribution is lost.
0:45 — 🔴 BLOCKER — Scale & Physics — The physical brush phases entirely through
       the solid geometry of the astronaut's backpack during the brushing motion.
0:55 — 🟠 MAJOR — Particles & Materials — Sand falling off the hull behaves as a
       unified 2D fluid waterfall rather than individual physical grains
       separating in gravity.
1:05 — 🔴 BLOCKER — Character — Anatomical breakdown: As the character ascends
       the dune, the right leg collapses, the knee warps backward, and the limb
       sinks entirely into the ground.
1:13 — 🟠 MAJOR — Scale & Physics — Impact lacks weight: The astronaut's fall
       into the crater produces a weightless, low-density CGI-style particle
       spray with no mass or terrain deformation.
1:18 — 🔴 BLOCKER — Character — The word "rose" spontaneously generates on the
       astronaut's backpack, acting as burned-in text.
1:25 — 🔴 BLOCKER — Particles & Materials — Solid passing through solid: The
       bristles of the brush merge directly into the suit fabric instead of
       colliding with the surface.
1:33 — 🔴 BLOCKER — Environment — Texture swimming: As the astronaut brushes the
       hull, the surface texture and color spontaneously morph, turning from
       pink to white without physical peeling.
2:02 — 🔴 BLOCKER — Character — Contact morphing: Hands phase directly through
       the solid ladder rungs during the climb.
```

## NEGATİF KUTU DENETİMİ (raporun kendi çıktısı)

```
NEGATIVE BOX COUNT: 5 · LINKED FINDINGS: 5 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 6 · TICKED: 5 · MISSED: 0
NO BOX EXISTS FOR: shadow direction mismatch
```

## WHAT WORKED WELL

- The overall color palette and production design are highly cohesive; the
  monochromatic pink/red aesthetic translates beautifully.
- Camera moves are highly controlled, avoiding the frantic AI panning that
  usually breaks single-shot scenes.

## PROMPT IMPROVEMENT SUGGESTIONS

1. ADD to image prompt: "solid feet planted firmly on ground, anatomical
   accuracy, realistic weight distribution" → prevents foot sliding and knee
   collapsing.
2. REMOVE from image prompt: "text, numbers, logos, decals" → causes the word
   "rose" to spontaneously generate on the backpack.
3. REPLACE "brushing sand" with "carefully wiping away granular dust, strict
   collision physics, solid surface contact" → prevents the brush phasing
   through backpacks and hulls.

## NEW LESSON CANDIDATE

No new lesson — all errors map to the failure patterns listed above [4, 5, 6, 10, 11].

## OUT-OF-SCOPE FLAGS

- 0:10 boot colors change from black to white between clips → CONTINUITY lens
- 0:40 visor transparency and reflectivity shift between scenes → CONTINUITY lens

## FLAGS FOR DOCUMENT CHECK

- 0:03 sand pours from flat geometric wall — QUESTION: was this surreal,
  impossible architecture specified, or is it an AI hallucination?
- 1:18 "rose" written on backpack — QUESTION: is this text explicitly scripted
  in the plan despite the negative core rule?

## QUALITY TABLE ROW

```
| (not supplied) Ⓥ | YATAY | Compilation | 2/10 | 3/10 | 10/10 | 7/10 | 5/10 |  | 4/10 |  |  | 4/10 |  |  |  | 5 | 5.0/10 |
```
