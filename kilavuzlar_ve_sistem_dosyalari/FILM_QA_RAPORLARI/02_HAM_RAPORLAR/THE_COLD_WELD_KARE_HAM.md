# HAM RAPOR — THE COLD WELD · ① KARE (T1)

```
KÜNYE (operatör tarafından doldurulmadı — D160 ihlali)
girdi: <tam yol YOK> · <süre YOK> · <çözünürlük YOK>
işlendiği tarih: 01.09.2026 · işleyen kart: qa-isle
⛔ ⑪ ölçüm kapısı KOŞULAMADI (master verilmedi) → bu raporun süre ve
   sahne sayıları HİÇBİR KAPIYA girmedi.
⛔ ① SPEC kapısı: film klasöründe THE_COLD_WELD_QA_SPEC.md VAR, rapor
   mod V koşuldu → koşu TEKRARLANIR, T tablosuna satır YAZILMAZ [D129].
```

---

FORMAT: YATAY
INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS

FILM: (not supplied)
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 155s MEASURED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 14 (0:10, 0:20, 0:29, 0:40, 0:50, 0:59, 1:10, 1:19, 1:29, 1:39, 1:49, 1:59, 2:10, 2:19)
NON-SCENE MATERIAL: 2:30-2:35 title card
LINES HEARD: none — nothing audible to me
SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES: 8
SUM OF SCORES: 41.0
DIVISION: 41.0 ÷ 8 = 5.1

OVERALL SCORE: 5.1/10 (3 categories excluded: Creatures, Frame Anchor Fidelity, Vertical Format checks)
VERDICT: REGENERATE

## SCORES SUMMARY
| Category | Score | Critical Issues |
|---|:--:|---|
| Character | 5/10 | −2 · 1:31 (F3) |
| Scale & Physics | 4/10 | −3 · 1:50 (F2) |
| Camera | 7/10 | — |
| Lighting | 6/10 | −1 · 0:50 (F4) |
| Environment | 5/10 | −2 · 1:50 (F2) |
| Creatures | N/A | no in-scope source |
| Particles & Materials | 5/10 | −2 · 2:20 (F5) |
| Dialogue & Audio | 3/10 | −4 · 0:10 (F1) |
| Frame Anchor Fidelity | N/A | no in-scope source |
| Negative Violations | 3 count | 0:10 (F1) · 1:31 (F3) · 2:30 (F7) |
| Motion Quality | 6/10 | −1 · 0:30 (F6) |
| Vertical Format (9:16) | N/A | — |
| Safe Zone | N/A | — |
| Hook Timing | N/A | — |

## SCENE INVENTORY
MATERIAL — compilation edit · duration 155s
Cuts: 14 (0:10, 0:20, 0:29, 0:40, 0:50, 0:59, 1:10, 1:19, 1:29, 1:39, 1:49, 1:59, 2:10, 2:19)
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Female, short dark hair. First frame fully visible: 0:10
Suit / wardrobe: White spacesuit, grey accents, clear helmet visor.
Wear / dirt: Clean condition, minor scuffing on knees.
Equipment: Basic suit, no visible backpack/tethers.

THE WORLD
Gravity read: Sub-1g/low gravity (slow steps), but anomalous floating objects.
Atmosphere read: Vacuum (black sky, hard shadows).
Light sources: Single intense hard light (sun-like) from left/back-left.
Location: Lunar surface plated with metal panels.

MOTION
Camera: Mostly static lockoffs, minor pans/tilts following subject.
Subject: Slow walking, kneeling, interacting with metal panels.

## PRESENCE STRING
111111111111111

## SEVERITY TALLY
🔴 BLOCKER: 3    🟠 MAJOR: 2    🟡 MINOR: 1

## TOP 3 CRITICAL ERRORS
1. 0:10 — 🔴 BLOCKER — Airborne sound propagating in a vacuum (audible footsteps/clanking).
2. 1:31 — 🔴 BLOCKER — Object phasing (wrench head clips entirely through the metal bolt).
3. 2:30 — 🔴 BLOCKER — Text visible on screen (title card baked into the generated output).

## DETAILED ERROR LOG
0:10 — 🔴 BLOCKER — Audio — Airborne footsteps/clanking audible in clear vacuum setting.
1:31 — 🔴 BLOCKER — Character — Glove and wrench head phase through the metal surface.
1:50 — 🟠 MAJOR — Physics — Heavy metal plates float upwards against established gravity.
0:50 — 🟡 MINOR — Lighting — Slight bloom/haze appears on the spacesuit highlights.
2:20 — 🟠 MAJOR — Particles & Materials — Dropped disc lacks appropriate low-g momentum/impact.
0:30 — 🟡 MINOR — Motion Quality — Character footsteps exhibit slight gliding/moonwalking.
2:30 — 🔴 BLOCKER — Negative Violations — Large baked-in text ("THE COLD WELD").

## WHAT WORKED WELL
- Consistent lighting direction maintained across most scenes.
- Suit design remains relatively stable without major mid-clip drift.

## PROMPT IMPROVEMENT SUGGESTIONS
1. ADD to image prompt: "pure black sky, zero atmospheric haze" → prevents light bloom.
2. REMOVE from video prompt: "cinematic sound effects" → causes airborne sound in vacuum.
3. REPLACE "floating panels" with "structurally supported panels" → prevents gravity anomalies.

## NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above.

## OUT-OF-SCOPE FLAGS
none

## FLAGS FOR DOCUMENT CHECK
- 0:10 — audio contains footsteps/clanking — QUESTION: is exterior sound permitted in this scene's vacuum?
- 1:50 — metal plates float upwards — QUESTION: is zero-g or levitation intended for these structures?
- 2:30 — title card at end — QUESTION: is this burned-in text intentional for the edit?

## QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 5/10 | 4/10 | 7/10 | 6/10 | 5/10 | | 5/10 | 3/10 | | 6/10 | | | | 3 | 5.1/10 |
