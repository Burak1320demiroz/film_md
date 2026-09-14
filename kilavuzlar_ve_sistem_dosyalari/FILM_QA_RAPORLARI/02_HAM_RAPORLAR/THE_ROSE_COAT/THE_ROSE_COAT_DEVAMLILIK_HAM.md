# 🔗 THE ROSE COAT — ② DEVAMLILIK HAM RAPORU

> **Koşu:** 26.08.2026 · video-only (bu merceğin tek modu)
> **Rubrik:** `../../QA_PROMPTLARI/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Atıf:** rapor `FILM: (not supplied)` yazdı; kimlik kapısı ③ operatörde koşuldu.
> ⛔ Aşağısı MODELİN ÇIKTISIDIR, düzeltilmemiştir.

---

```
FILM: (not supplied)
RUNTIME: 135s measured
SCENES OBSERVED: 13 · CUTS COUNTED: 13 · CHARACTERS TRACKED: 2
NON-SCENE MATERIAL: 2:10-2:15 title card
LINES HEARD: none

MATERIAL TYPE: FILM
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  12
SUM OF SCORES:      86.0
DIVISION:           86.0 ÷ 12 = 7.2

OVERALL SCORE: 7.2/10
VERDICT: STRUCTURAL PROBLEM
(Severe costume and equipment drift breaks character identity across nearly
 every cut.)
```

## SCENE INVENTORY

| # | In-out | Location | Present | What happens | Dialogue |
|---|---|---|---|---|---|
| 1 | 0:00-0:09 | Sand wall | None | Sand pours from wall slit | None |
| 2 | 0:10-0:19 | Habitats | A, B | Walking right past modules | None |
| 3 | 0:20-0:29 | Buried shuttle | A, B | Walking right past shuttle | None |
| 4 | 0:30-0:39 | Rocket distance | A, B | Walking right toward rocket | None |
| 5 | 0:40-0:49 | Desert flat | A, B | B brushes sand off A | None |
| 6 | 0:50-0:59 | Rocket base | A, B | Brushing a low square panel | None |
| 7 | 1:00-1:09 | Dune by leg | A, B | Walking up a dune | None |
| 8 | 1:10-1:19 | Crater | A, B | A falls backward into dust | None |
| 9 | 1:20-1:29 | Desert flat | A, B | B brushes A's pack | None |
| 10 | 1:30-1:39 | Rocket base | A, B | Both brush large upper panel | None |
| 11 | 1:40-1:49 | Rocket base | A, B | Standing near landing leg | None |
| 12 | 1:50-1:59 | Rocket ladder | A, B | B brushes A near ladder | None |
| 13 | 2:00-2:09 | Rocket ladder | A, B | A climbs the ladder | None |

## CHARACTER PASSPORT(S)

```
Label:            Character A (Shorter / Left)
First clear view: S2, 0:10
Face:             UNVERIFIABLE (obscured by opaque/reflective spherical visor)
Hair:             UNVERIFIABLE
Build:            Shorter frame, standard proportions
Costume:          Pink/red coveralls. Boots fluctuate between black and white.
                  Gloves fluctuate between black and white.
Equipment:        Backpack appears, vanishes, and changes shape/color throughout.
Wear map:         Dust on backpack accumulates, resets to clean, and re-accumulates.
Voice:            N/A

⭐ EVIDENCE BASE
FACE-VISIBLE:     0 s of 135 s total · 0 of 13 scenes
COSTUME-VISIBLE:  12 of 13 scenes
MOUTH ON SCREEN:  no

Label:            Character B (Taller / Right)
First clear view: S2, 0:10
Face:             UNVERIFIABLE (obscured by opaque/reflective spherical visor)
Hair:             UNVERIFIABLE
Build:            Taller frame, standard proportions
Costume:          Pink/red coveralls. Black boots, black gloves.
Equipment:        Backpack vanishes and reappears. Black case held in hand,
                  vanishes, reappears.
Wear map:         Clean throughout.
Voice:            N/A

⭐ EVIDENCE BASE
FACE-VISIBLE:     0 s of 135 s total · 0 of 13 scenes
COSTUME-VISIBLE:  12 of 13 scenes
MOUTH ON SCREEN:  no
```

## APPEARANCE TABLE

| Character | Scene | In-out | Face visible? | State notes |
|---|---|---|:--:|---|
| Char A | S2 | 0:10-0:19 | No | Black boots, black gloves. Red pack. |
| Char B | S2 | 0:10-0:19 | No | Black boots. Carrying black case. |
| Char A | S3 | 0:20-0:29 | No | Black case appears in left hand. |
| Char B | S3 | 0:20-0:29 | No | Black case in right hand. |
| Char A | S4 | 0:30-0:39 | No | Black case in left hand. |
| Char B | S4 | 0:30-0:39 | No | Black case in right hand. |
| Char A | S5 | 0:40-0:49 | No | Boots flip to WHITE. Gloves WHITE. |
| Char B | S5 | 0:40-0:49 | No | Holding brush. Case vanished. |
| Char A | S6 | 0:50-0:59 | No | Boots/gloves BLACK again. Pack vanished. |
| Char B | S6 | 0:50-0:59 | No | Pack vanished. |
| Char A | S7 | 1:00-1:09 | No | Black boots. Carrying black case again. |
| Char B | S7 | 1:00-1:09 | No | No pack, no case. |
| Char A | S8 | 1:10-1:19 | No | Boots WHITE. Large white pack with "rose". |
| Char B | S8 | 1:10-1:19 | No | No pack. |
| Char A | S9 | 1:20-1:29 | No | Boots/gloves WHITE. Pack dirty, no text. |
| Char B | S9 | 1:20-1:29 | No | No pack. Holding brush. |
| Char A | S10 | 1:30-1:39 | No | Boots/gloves BLACK. No pack. |
| Char B | S10 | 1:30-1:39 | No | Boots BLACK. No pack. |
| Char A | S11 | 1:40-1:49 | No | Boots WHITE. Small red pack. |
| Char B | S11 | 1:40-1:49 | No | Case in hand. No pack. |
| Char A | S12 | 1:50-1:59 | No | Boots/gloves WHITE. Large white pack. |
| Char B | S12 | 1:50-1:59 | No | Large white pack appears. |
| Char A | S13 | 2:00-2:09 | No | Boots/gloves BLACK. Pack vanishes. |
| Char B | S13 | 2:00-2:09 | No | Pack vanishes. |

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
|:--:|---|:--:|---|
| 1 | Identity — Face, Hair & Build | 10/10 | no in-scope source (build holds; face UNVERIFIABLE) |
| 2 | Costume Identity | 1/10 | −9 · 0:10 (S2) vs 0:40 (S5) boots color · 0:40 (S5) vs 0:50 (S6) packs vanish |
| 3 | Wear, Damage & Injury | 3/10 | −7 · 1:20 (S9) vs 1:40 (S11) heavy pack dirt resets to clean |
| 4 | Equipment & Carried Objects | 2/10 | −8 · 0:10 (S2) vs 0:20 (S3) case appears · 0:40 (S5) vs 0:50 (S6) case vanishes |
| 5 | Cross-Cut Action | 7/10 | −3 · 1:10 (S8) vs 1:20 (S9) falls, then standing casually |
| 6 | Physical Consistency | 10/10 | no in-scope source |
| 7 | Counter Logic | N/A | no counter present |
| 8 | Spatial Geography | 7/10 | −3 · 0:50 (S6) vs 1:30 (S10) rocket base layout changes |
| 9 | Time & Light Logic | 10/10 | no in-scope source |
| 10 | World State & Props | 6/10 | −4 · 1:30 (S10) vs 1:50 (S12) rocket hatch vanishes, ladder appears |
| 11 | Causality & Knowledge | 10/10 | no in-scope source |
| 12 | Quantity & Character Count | 10/10 | no in-scope source |
| 13 | Setup & Abandonment | 10/10 | no in-scope source |

## PRESENCE STRING

```
-111111111111
```

## SEVERITY TALLY

```
🔴 BLOCKER: 2   🟠 MAJOR: 3   🟡 MINOR: 0
```

## DRIFT MAP

| Half | Element | Character | First slip | Undeniable by | Recovered? |
|---|---|---|---|---|:--:|
| BODY | Costume | Char A | 0:40 (S5) | 0:50 (S6) | No |
| BODY | Equipment | Char A | 0:20 (S3) | 0:40 (S5) | No |
| WORLD | Geography | Rocket | 1:30 (S10) | 1:50 (S12) | No |

## WEAR TIMELINE

| Mark | Character | Acquired | Present at | Absent at ⚠️ | One-way? |
|---|---|---|---|---|:--:|
| Sand on pack | Char A | 0:40 (S5) | 1:20 (S9) | 1:40 (S11) ⚠️ | No |

## COUNTER CURVE

```
NONE
```

## LOCATION MAP

| Location | Scenes | Consistent? | Mismatch |
|---|---|:--:|---|
| Rocket base | S6, S10, S11, S12, S13 | No | Panels shift heights; ladders appear/vanish. |
| Desert flat | S5, S9 | Yes | — |

## CONTRADICTION LOG

| Timecode A | Timecode B | Half | Character | Cat. | What contradicts what | Severity |
|---|---|---|---|:--:|---|:--:|
| 0:10 | 0:40 | BODY | Char A | 2 | Boots are black at 0:10, white at 0:40. | 🔴 BLOCKER |
| 0:40 | 0:50 | BODY | Both | 2 | Backpacks present at 0:40, completely vanish by 0:50. | 🔴 BLOCKER |
| 1:10 | 1:20 | BODY | Char A | 5 | A falls backward into crater at 1:10, is standing casually on flat ground at 1:20. | 🟠 MAJOR |
| 1:20 | 1:40 | BODY | Char A | 3 | Backpack is heavily covered in sand at 1:20, pristine clean at 1:40. | 🟠 MAJOR |
| 0:50 | 1:30 | WORLD | — | 8 | Rocket panel is low to the ground at 0:50, huge and higher up at 1:30. | 🟠 MAJOR |

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
|---|---|:--:|---|
| Black carrying case | 0:10 | Yes | Set on ground in S12, left behind. |

## THE THREE THAT MATTER

1. **Boot and glove color flipping** (0:10 vs 0:40 vs 0:50). Viewers will
   instantly notice the stark contrast of white vs black extremities switching
   back and forth across cuts, breaking the illusion that this is the same suit.
   Fix: Regenerate scenes enforcing fixed boot/glove colors.
2. **Backpacks vanishing and reappearing** (0:40 vs 0:50). The large, bulky
   life-support packs evaporate into thin air across multiple cuts,
   fundamentally breaking object permanence. Fix: Regenerate S6, S7, S10, S13.
3. **Action continuity break on the fall** (1:10 vs 1:20). Character A takes a
   dramatic backward fall into a crater, but the next shot cuts to them standing
   calmly being brushed. Fix: Insert a shot of Character B helping A up.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|:--:|
| Boot/glove color flip | Regenerate offending shots with strict color prompts | High |
| Backpacks vanishing | Regenerate offending shots forcing backpack presence | High |
| Missing fall recovery | Generate an intermediate bridging shot | Medium |
| Clean backpack (S11) | Crop tighter or regenerate to maintain dirt state | Low |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Boot colors flip constantly between black and white. | Which color boots does the character bible specify for Character A? |
| Black case teleports between characters' hands in early scenes. | Who is supposed to be carrying the black equipment case? |

## OUT-OF-SCOPE FLAGS

- 0:03 sand pours from flat geometric wall with no physical volume → FRAME lens
- 1:18 "rose" text spontaneously generates on backpack → FRAME lens
- 2:00 hands phase through solid metal ladder rungs → FRAME lens
