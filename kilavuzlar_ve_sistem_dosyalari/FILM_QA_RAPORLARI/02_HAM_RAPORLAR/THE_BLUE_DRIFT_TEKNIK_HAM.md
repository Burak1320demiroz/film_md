# 🔧 THE BLUE DRIFT — VIDEO_QA (TEKNİK) HAM RAPORU

> Çalıştırma: 20.08.2026 · MOD V (dış model — Gemini) · yatay TAM KURGU
> Rubrik: `../QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> ⚠️ Bu rapor BEŞ MERCEKLİK bir partinin parçasıdır ve parti kapılardan
> geçmedi — sahne sayıları 10/15/15 bildirildi, film 25 segmenttir.
> Parti durumu, kilit çelişkisi defteri ve belge cevapları:
> `../01_FILM_RAPORLARI/THE_BLUE_DRIFT.md` · KOŞU 2
> ⛔ Skor satırı hiçbir tabloya işlenmedi (ortak adım ⑤).
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: (not supplied)
SCENE: Compilation
VIDEO DURATION: ~255s ESTIMATED
MATERIAL TYPE: FILM (undeclared)
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 4/10 (2 categories excluded as UNVERIFIABLE)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    3/10    −2 · 0:12 (fingers) · 0:43 (duplicate) · 1:41 (fusion) · 3:04 (extra digits) · 3:50 (face morph)
Scale & Physics    4/10    −2 · 2:10 (ship proportions)
Camera    5/10    −1 · 1:15 (morph cut)
Lighting    4/10    −1 · 0:12 (AI bloom)
Environment    3/10    −2 · 1:20 (aurora in space)
Creatures    UNVERIFIABLE    none
Particles & Materials    3/10    −2 · 2:31 (gravity in space)
Dialogue & Audio    3/10    −2 · 0:52 (no lip-sync) · 1:20 (sound in vacuum)
Frame Anchor Fidelity    UNVERIFIABLE    none
Negative Violations    11 count    −3 · 4:10 (burned-in text)
Motion Quality    4/10    −1 · 0:43 (ghosting)

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration ~255s
Cuts you can see: multiple scene cuts
Aspect ratio: 16:9

THE CHARACTER
Face / hair: Female (fair, auburn bun), Male (rugged, dark hair). First frame: 0:10.
Suit / wardrobe: Blue suits. Female: gold/orange accents. Male: teal accents.
Wear / dirt: Clean.
Equipment: Clear visors, chest indicators.

THE WORLD
Gravity read: ~1g on surface, zero-g in space.
Atmosphere read: Surface atmosphere unknown (aurora present). Space is vacuum.
Light sources: Sun (directional), glowing gas giant, internal console lights.
Location: Ice moon, outer space, station interior.

MOTION
Camera: Static locks, slow pushes, tracks.
Subject: Walking, running, ship flight.

SEVERITY TALLY
🔴 BLOCKER: 9    🟠 MAJOR: 2    🟡 MINOR: 1

TOP 3 CRITICAL ERRORS
3:50 — 🔴 BLOCKER — Total face and ethnicity morph for both characters.

4:10 — 🔴 BLOCKER — Burned-in title text on screen.

2:31 — 🔴 BLOCKER — Vented gas falls downward in space, obeying 1g gravity in zero-g.

DETAILED ERROR LOG
0:12 — 🔴 BLOCKER — Character — Fingers merge into glowing core sample.
0:12 — 🟠 MAJOR — Lighting — AI bloom softens the core sample light.
0:43 — 🔴 BLOCKER — Character — Transparent duplicate astronaut silhouette overlays frame.
0:52 — 🔴 BLOCKER — Dialogue & Audio — Spoken audio plays but lips do not move.
1:15 — 🟠 MAJOR — Camera — Hidden morph cut as vertical jets vanish.
1:20 — 🔴 BLOCKER — Environment — Aurora borealis drags alongside ship in space vacuum.
1:20 — 🔴 BLOCKER — Dialogue & Audio — Engine sound effects propagate in vacuum.
1:41 — 🔴 BLOCKER — Character — Hands fuse into an anatomical blob.
1:50 — 🟡 MINOR — Character — Skin texture appears waxy/airbrushed.
2:10 — 🟠 MAJOR — Scale & Physics — Ship exterior sprouts new orange domes.
2:31 — 🔴 BLOCKER — Particles & Materials — Vented particles arc downward in zero-g.
3:04 — 🔴 BLOCKER — Character — Left hand has 6 fingers clipping into console.
3:50 — 🔴 BLOCKER — Character — Absolute character identity/face morph.
4:10 — 🔴 BLOCKER — Negative Violations — "THE BLUE DRIFT" burned-in text.

🚫 NEGATIVE BIBLE VIOLATIONS
NEGATIVE BOX COUNT: 11 · LINKED FINDINGS: 11 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 11 · TICKED: 11 · MISSED: 0

[x] Any visible CUTS or TRANSITIONS

[x] Airbrushed, waxy, or plastic skin texture

[x] Text, subtitles, captions, or watermarks visible on screen

[x] AI bloom / soft glow filter

[x] Face morphing

[x] Object phasing/clipping

[x] Duplicate characters

[x] Hand geometry breakdown near glowing surfaces

[x] Ship/structure proportion shifts between shots

[x] Extra fingers, phantom digits, or hand-surface fusion

[x] Airborne sound propagating in vacuum

WHAT WORKED WELL
Pacing of exterior ship shots.

Console UI design consistency.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "sharp directional light, hard shadows" → prevents AI bloom.

REMOVE from video prompt: "cinematic lighting" → causes waxy skin and bloom.

REPLACE "venting gas" with "gas expanding linearly in zero-g vacuum" → prevents gravity waterfalls.

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above (1, 2, 3, 4, 5, 9, 11).

FLAGS FOR DOCUMENT CHECK
0:12 — visors are open in exterior — QUESTION: was surface atmosphere breathable?

0:52 — audio line plays with no lip movement — QUESTION: is this meant to be comms/off-screen?

QUALITY TABLE ROW
| Ⓥ | Compilation | 3/10 | 4/10 | 5/10 | 4/10 | 3/10 | N/A | 4/10 | 4/10 |
