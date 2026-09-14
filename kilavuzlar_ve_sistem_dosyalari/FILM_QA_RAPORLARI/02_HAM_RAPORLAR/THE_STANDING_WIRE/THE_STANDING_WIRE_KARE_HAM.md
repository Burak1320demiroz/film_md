# THE STANDING WIRE — ① KARE QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi (raporun yazdığı): `the standıng wıre.mp4` · rapor süresi ~245 s
> ⛔ ⑪.0 KİMLİK [D160]: aynı ada uyan İKİ dosya var, ikisi de ölçüldü —
>   `~/Downloads/the standıng wıre.mp4` 1280x720 · 245,141 s
>   `~/Downloads/the standıng wıre (1).mp4` 3840x2160 · 245,141 s  ← MASTER, ölçüm bunda koşuldu
>   AYNI KURGU (süre birebir), farklı çözünürlük. Rapor 720p kopyayı ölçmüş.
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 05.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_4_dk_filmler/THE_STANDING_WIRE/THE_STANDING_WIRE_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/PAKET_1..8` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
> ⛔ AYRICA TESLİM KUSURU [D150]: master ÜRETİCİ FİLİGRANI taşıyor (Flow ▷ ikonu, 6/6 örnek).
>   Filigranlı master master değildir → sekiz mercek onu ÖLÇMEMİŞ sayılır, mod Vden bağımsız olarak.
> ⛔ ⑤/⑦ notu: sekiz mercek AYNI OTURUMDA koşuldu → bağımsız ölçüm değildir [D110].

---

FORMAT: YATAY
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?" It does NOT answer "does this clip match its design document."

MATERIAL
What you were given: compilation edit · duration 245s
Cuts you can see: 24 cuts (0:10, 0:20, 0:29, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00)
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Female, fair skin, dark hair inside helmet. First frame fully visible: 0:01
Suit / wardrobe: Blue/grey space suit, white helmet, chest panels, thick gloves.
Wear / dirt: Dusty knees and forearms (0:40).
Equipment: Coiled wire/rope carried on shoulder.

THE WORLD
Gravity read: 1g on planet (dust falls, heavy steps). Zero-g in space.
Atmosphere read: Breathable/dense on surface (dust hangs slightly, wind audible). Vacuum in space.
Light sources: Sun (hard, directional) in canyon.
Location: Rocky canyon, ascending to orbit.

MOTION
Camera: Mix of static, slow pushes, and tilts.
Subject: Climbing, walking, ascending vertical wire.

FILM: THE STANDING WIRE
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: ~245s ESTIMATED
MATERIAL TYPE: FILM
CUTS COUNTED: 24 (0:10, 0:20, 0:29, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50, 4:00)
NON-SCENE MATERIAL: 4:00-4:04 Title Card
LINES HEARD: 1 · "Just a little further. The wire is still holding. Made it this far. Almost at the top." at 0:51.
SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES: 8
SUM OF SCORES: 46.0
DIVISION: 46.0 ÷ 8 = 5.7
OVERALL SCORE: 5.7/10
(Categories 6, 9 excluded as unmeasured/unverifiable. Categories 12-14 excluded as N/A.)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    6/10    −2 · 0:30 (F1) · 1:20 (F2)
Scale & Physics    5/10    −3 · 3:00 (F3) · 3:50 (F4)
Camera    6/10    −2 · 2:20 (F5)
Lighting    6/10    −2 · 1:50 (F6)
Environment    6/10    −2 · 2:10 (F7)
Creatures    —    no in-scope source
Particles & Materials    5/10    −3 · 0:03 (F8)
Dialogue & Audio    6/10    −2 · 3:36 (F9)
Frame Anchor Fidelity    —    no in-scope source
Negative Violations    2 count    Text on screen, Floating particles
Motion Quality    6/10    −2 · 3:00 (F10)
Vertical Format (9:16)    N/A    Format is YATAY
Safe Zone    N/A    Format is YATAY
Hook Timing    N/A    Format is YATAY

SCENE INVENTORY — mode V only
[See BASELINE above]

PRESENCE STRING
111111111111111111111111-

SEVERITY TALLY
🔴 BLOCKER: 2    🟠 MAJOR: 4    🟡 MINOR: 4

TOP 3 CRITICAL ERRORS
0:03 — 🔴 BLOCKER — Floating particles without gravitational cause near the base plate.
4:00 — 🔴 BLOCKER — Title text burned onto the screen.
3:00 — 🟠 MAJOR — Character is completely rigid while floating in zero-g; no micro-motion or limb drift.

DETAILED ERROR LOG
0:03 — 🔴 BLOCKER — Particles & Materials — Pebbles float and disappear without cause.
4:00 — 🔴 BLOCKER — Negative Violations — "THE STANDING WIRE" text baked onto screen.
0:30 — 🟠 MAJOR — Character — Glove details and thickness shift dramatically between shots.
1:20 — 🟡 MINOR — Character — Visor transparency fluctuates across consecutive cuts.
3:00 — 🟠 MAJOR — Scale & Physics — Rigid character model dragging in zero-g lift.
3:50 — 🟠 MAJOR — Scale & Physics — Wire behaves like a 2D ribbon inside the cabin, defying tension logic.
2:20 — 🟡 MINOR — Camera — Slight unnatural jitter in the tracking push.
1:50 — 🟡 MINOR — Lighting — Sun angle shifts abruptly across the canyon cut.
2:10 — 🟡 MINOR — Environment — Slight texture swimming on the distant canyon walls.
3:36 — 🟠 MAJOR — Dialogue & Audio — Airborne whoosh sound layered with hatch opening in vacuum.

NEGATIVE BIBLE VIOLATIONS
[x] Text, subtitles, captions, or watermarks visible on screen
[x] Floating particles without gravitational cause
NEGATIVE BOX COUNT: 2 · LINKED FINDINGS: 2 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 2 · TICKED: 2 · MISSED: 0

WHAT WORKED WELL
The canyon environment feels vast and texturally detailed.
Character's walking weight in 1g is mostly convincing.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to prompt: "continuous limb drift, zero-g micro-motion" → prevents rigid character in space.
REMOVE from prompt: "dust floating" → causes particle physics violations on the surface.
REPLACE "title card" with "clean wide shot" → prevents burned-in text.

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above [5, 8, 10].

OUT-OF-SCOPE FLAGS
none

FLAGS FOR DOCUMENT CHECK — mode V only
0:30 — Glove design shifts — QUESTION: Were specific glove models specified?
3:36 — Whoosh in space — QUESTION: Is this meant to be internal cabin pressurization or external audio error?

QUALITY TABLE ROW
| THE STANDING WIRE Ⓥ | YATAY | Compilation | 6/10 | 5/10 | 6/10 | 6/10 | 6/10 | | 5/10 | 6/10 | | 6/10 | | | | 2 | 5.7/10 |
