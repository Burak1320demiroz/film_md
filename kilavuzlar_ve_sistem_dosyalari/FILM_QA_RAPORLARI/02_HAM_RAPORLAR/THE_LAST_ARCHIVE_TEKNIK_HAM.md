# THE LAST ARCHIVE — VIDEO QA (TEKNİK) · HAM RAPOR

```
QA TARİHİ:     31 Temmuz 2026
QA PROMPTU:    QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md
GİRDİ:         Compilation · 148 s
SPEC BLOĞU:    🚨 BOŞ — 12 alan doldurulmadı (rapor bunu dürüstçe bildirdi)
GEÇERLİLİK:    ⚠️ ŞARTLI
```

> ⚠️ Değiştirilmedi, kısaltılmadı. Doğrulama: `../01_FILM_RAPORLARI/THE_LAST_ARCHIVE.md`

---

FILM: The Last Archive
FORMAT: 2-4dk
SCENE: Compilation
VIDEO DURATION: 148s
SPEC BLOCK PROVIDED: no — CHARACTER, SUIT, CHARACTER HEIGHT, GRAVITY, ATMOSPHERE, LOCOMOTION MODE, LENS, CAMERA DISTANCE, CAMERA MOVE, LIGHT SOURCES, FILL LIGHT ALLOWED, VEHICLE/STRUCTURE are blank. Marked UNVERIFIABLE.

OVERALL SCORE: 4/10
VERDICT: REGENERATE
         (Contains multiple 🔴 BLOCKER issues regarding locomotion and anatomy.)

## SCORES SUMMARY

| Category | Score | Critical Issues |
|----------|:-----:| --------------- |
| Character | 5/10 | Waxy skin, hand morphing on contact. |
| Scale & Physics | 4/10 | Gliding steps, floaty impacts. |
| Camera | 6/10 | Stable, mostly motivated moves. |
| Lighting | 5/10 | AI bloom on luminous surfaces. |
| Environment | 4/10 | Severe texture swimming on rocks. |
| Creatures | N/A | None present. |
| Particles & Materials | 4/10 | Landing dust lacks physical mass. |
| Dialogue & Audio | 5/10 | No dialogue; SFX sync is passable. |
| Frame Anchor Fidelity | N/A | Compilation edit. |
| Negative Violations | 6 count | Morphing, bloom, gliding, texture swim, particle mass, waxy skin. |
| Motion Quality | 4/10 | General jello effect and moonwalking. |

## SEVERITY TALLY
🔴 BLOCKER: 2    🟠 MAJOR: 4    🟡 MINOR: 3

## TOP 3 CRITICAL ERRORS (most impactful)
1. 1:00 — 🔴 BLOCKER — Fingers morph and merge into the carved rock surface on contact.
2. 0:21 — 🔴 BLOCKER — Character glides/moonwalks; feet lack surface friction and weight.
3. 0:08 — 🟠 MAJOR — Deep texture swimming and morphing on the stationary rock carvings.

## DETAILED ERROR LOG
0:08 — 🟠 MAJOR — Environment — Rock carvings "breathe" and shift shapes.
0:14 — 🟠 MAJOR — Particles — Ship landing kicks up CGI-style, low-mass dust.
0:21 — 🔴 BLOCKER — Motion — Character locomotion lacks weight; feet slide.
0:36 — 🟡 MINOR — Lighting — AI bloom evident on helmet reflections and smoke.
1:00 — 🔴 BLOCKER — Character — Hand geometry fails when touching the inscription.
1:19 — 🟡 MINOR — Character — Suit details and display panel flicker slightly.
1:36 — 🟠 MAJOR — Character — Face exhibits airbrushed, plastic skin lacking pores.
2:00 — 🟠 MAJOR — Character — Tear physics look slightly viscous and unnatural.
2:05 — 🟡 MINOR — Physics — Ship thruster exhaust freezes/drags with camera.

## WHAT WORKED WELL (keep these in future prompts)
- Overall composition and framing are highly cinematic.
- Color grading maintains a consistent, desolate aesthetic.

## PROMPT IMPROVEMENT SUGGESTIONS
1. REMOVE from image/video prompt: "cinematic lighting" → causes waxy skin and bloom.
2. ADD to video prompt: "planted footsteps with physical weight" → prevents gliding/moonwalking.
3. ADD to video prompt: "static, unchanging geological textures" → prevents texture swimming.

## NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [4, 6, 10, 11, 27, 28, 33].

## QUALITY TABLE ROW (paste into LESSONS_LEARNED.md)
| The Last Archive | Comp | 5 | 4 | 6 | 5 | 4 | N/A | 4 | **4/10** |
