# THE UPWARD FALL — ① KARE QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi: `/Users/dai/Downloads/the upward fall (1).mp4` · 225,11 s · 3840x2160 · 30 fps · AAC 48 kHz stereo
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 04.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_3_5_dk_filmler/THE_UPWARD_FALL/THE_UPWARD_FALL_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_UPWARD_FALL/PAKET_*` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
> ⛔ ⑤/⑦ notu: sekiz mercek AYNI OTURUMDA koşuldu → bağımsız ölçüm değildir [D110].

---

FORMAT: YATAY
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

MATERIAL
What you were given: compilation edit · duration 226s
Cuts you can see: 21 · 0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: white male, short dark hair, clean-shaven · First frame fully visible: 0:40
Suit / wardrobe: black tactical spacesuit, segmented armor panels, clear visor
Wear / dirt: mostly clean, slight scuffing on knees
Equipment: cylindrical grey canister, knife

THE WORLD
Gravity read: inverted for loose objects (leaves, rocks, cloth fall upward), standard 1g for character
Atmosphere read: dense, misty forest, breathable look
Light sources: soft canopy sunlight, character chest light
Location: redwood-style alien forest

MOTION
Camera: static lockoffs and slow tracking pushes
Subject: slow, deliberate kneeling and walking

FILM: (not supplied)
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: 3-5dk
SCENE: Compilation
VIDEO DURATION: 226s measured
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 21 · 0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30
NON-SCENE MATERIAL: 3:40-3:46 Title Card
LINES HEARD: none — nothing audible to me
SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES:  8
SUM OF SCORES:      47.0
DIVISION:           47.0 ÷ 8 = 5.8

OVERALL SCORE: 5.8/10
VERDICT: ACCEPT WITH FIX PASS

SCORES SUMMARY
Category    Score    Critical Issues
Character    4/10    −2 · 2:23 (F1) · −2 · 3:11 (F1)
Scale & Physics    7/10    no in-scope source
Camera    7/10    no in-scope source
Lighting    7/10    no in-scope source
Environment    5/10    −2 · 3:10 (F5)
Creatures    5/10    −2 · 2:51 (F6)
Particles & Materials    7/10    no in-scope source
Dialogue & Audio    —    no in-scope source
Frame Anchor Fidelity    —    no in-scope source
Negative Violations    2 count    3:11 (F1), 3:10 (F5)
Motion Quality    5/10    −2 · 2:51 (F11)
Vertical Format (9:16)    N/A    N/A
Safe Zone    N/A    N/A
Hook Timing    N/A    N/A

SCENE INVENTORY — mode V only
(STEP 1 baseline yukarıda tekrarlandı — ham çıktıda birebir aynı blok)

PRESENCE STRING
1111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 0    🟠 MAJOR: 3    🟡 MINOR: 0

TOP 3 CRITICAL ERRORS
3:11 — 🟠 MAJOR — Fingers morph and fuse with knife handle and vine during cut.
2:23 — 🟠 MAJOR — Hand geometry breaks down, phasing into grey cylinder and vine.
2:51 — 🟠 MAJOR — Creature jump animation is stiff and lacks natural biological weight.

DETAILED ERROR LOG
2:23 — 🟠 MAJOR — Character — Hand geometry phases through green vine and container.
2:51 — 🟠 MAJOR — Motion Quality — Background creature leaps with linear, rigid trajectory.
2:51 — 🟠 MAJOR — Creatures — Background alien lacks joint articulation during jump.
3:10 — 🟠 MAJOR — Environment — Wood and vine textures swim during close-up interaction.
3:11 — 🟠 MAJOR — Character — Left hand fuses with knife handle; blade clips through wood.

WHAT WORKED WELL
Inverted gravity physics for particles and loose objects remains highly consistent.
Environmental lighting and atmospheric canopy haze feel cohesive and cinematic.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "rigid solid tools, distinct surface contact" → prevents hand-surface fusion.
REMOVE from video prompt: "cinematic lighting" → causes slight textural softness/bloom on character.
REPLACE "cutting vine" with "pressing blade against static vine" → prevents complex object phasing.

## 🔴 DERS 01: EL-NESNE ETKİLEŞİMİNDE ERİME
Kaynak: THE UPWARD FALL QA — Character: 4/10 — 3:11 — Left hand fuses with knife handle
Sorun: Karakter bir aleti sıkıca kavradığında veya kestiğinde parmaklar ve nesne iç içe geçip eriyor.
ÇÖZÜM — PROMPT GÜNCELLEMESİ:
firm grip, distinct structural boundaries between fingers and solid tool, no clipping

OUT-OF-SCOPE FLAGS
none

FLAGS FOR DOCUMENT CHECK — mode V only
3:40 — burned-in title card present — QUESTION: is this final formatting intentional?

QUALITY TABLE ROW
| THE UPWARD FALL Ⓥ | YATAY | Compilation | 4/10 | 7/10 | 7/10 | 7/10 | 5/10 | 5/10 | 7/10 | — | — | 5/10 | | | | 2 | 5.8/10 |
