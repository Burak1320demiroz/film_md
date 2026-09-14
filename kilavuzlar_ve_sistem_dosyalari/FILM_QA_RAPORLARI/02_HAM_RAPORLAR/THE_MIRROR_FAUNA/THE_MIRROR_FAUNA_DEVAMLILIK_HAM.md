# 🔗 THE_MIRROR_FAUNA — T2 DEVAMLILIK QA HAM RAPORU

> **Kaynak:** ② Devamlılık mercek · MOD D · 09.09.2026  
> **Ham rapor — dokunulmaz.** Analiz: `01_FILM_RAPORLARI/THE_MIRROR_FAUNA.md`

---

INPUT MODE: D
FILM: THE_MIRROR_FAUNA
RUNTIME: 02:44 measured
SCENES OBSERVED: 16 · CUTS COUNTED: 16 · CHARACTERS TRACKED: 3
NON-SCENE MATERIAL: 02:39-02:44 title card
LINES HEARD: none
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
  SCORED CATEGORIES:  11
  SUM OF SCORES:      85.0
  DIVISION:           85.0 ÷ 11 = 7.7

OVERALL SCORE: 7.7/10
VERDICT: STRUCTURAL PROBLEM

| # | Category | Score | Critical Issue |
|:--:|---|:---:|---|
| 1 | Identity | — | no in-scope source |
| 2 | Costume Identity | 4/10 | -3 · 02:20 visor reverts · -3 · 01:30 tentacles revert |
| 3 | Wear, Damage & Injury | 7/10 | -3 · 02:20 smoke vanishes |
| 4 | Equipment & Carried Objects | 6/10 | -4 · 00:50/01:00/01:10 tool morphs |
| 5 | Cross-Cut Action | 10/10 | clean |
| 6 | Physical Consistency | 10/10 | clean |
| 7 | Counter Logic | N/A | no in-scope source |
| 8 | Spatial Geography | 8/10 | -2 · 01:40 ground veins |
| 9 | Time & Light Logic | 10/10 | clean |
| 10 | World State & Props | 10/10 | clean |
| 11 | Causality & Knowledge | 5/10 | -5 · 02:00 duplicate scene |
| 12 | Quantity & Character Count | 10/10 | clean |
| 13 | Setup & Abandonment | 10/10 | clean |

PRESENCE STRING: 1111111111111111
SEVERITY TALLY: 🔴 BLOCKER: 0  🟠 MAJOR: 3  🟡 MINOR: 1

THE THREE THAT MATTER:
1. The Repeated Scene (02:00): S13 accidental duplication. Fix: Cut S13.
2. Orange Astro Visor/State Revert (02:20): red visor → clean suit. Fix: Regenerate S15.
3. Equipment Morphing (00:50 - 01:10): tool changes shape. Fix: Accept or regenerate S7/S8.
