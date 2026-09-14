# 🔧 THE COLD BURN — VIDEO_QA (TEKNİK) HAM RAPORU

> Çalıştırma: 09.08.2026 · MOD V (dış model — Gemini; SPEC bloğu verilmedi,
> oysa PLAN §QA SPEC BLOĞU hazırdı — operatör kuralı ② yine atlandı)
> Rubrik: `../QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> Ölçülen malzeme: 225 s kurgu (12 sahne) — beş merceğin beşi AYNI dosyayı
> ölçtü (D75 ✅). Plan: 30 sahne / 299 s → belge cevapları:
> `../01_FILM_RAPORLARI/THE_COLD_BURN.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).
> ⚠️ Rubrik uyum notları: DERS 65 TUTTU (`FILM: (not supplied)`). Canlı
> kategorisi "UNVERIFIABLE" yazılmış — canlı yokken doğru etiket N/A'dır
> (tabloya N/A işlendi).

---

INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: (not supplied)
SCENE: (not supplied)
VIDEO DURATION: 225s
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 5/10 (3 categories excluded)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    5/10    Waxy skin; minor finger morphing
Scale & Physics    4/10    Rigid zero-g models; sliding walk
Camera    UNVERIFIABLE    Requires plan file
Lighting    6/10    Minor bloom on fire
Environment    6/10    Generally stable; minor cloud uniformity
Creatures    UNVERIFIABLE    No creatures present
Particles & Materials    4/10    Static fire/smoke; low-mass explosion
Dialogue & Audio    5/10    Lip sync acceptable; stiff facial animation
Frame Anchor Fidelity    UNVERIFIABLE    No spec provided
Negative Violations    5 count    Text, rigid zero-g, static particles, sliding, waxy skin
Motion Quality    4/10    Jello on run; zero-g drag

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 225s
Cuts you can see: multiple scene transitions
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Older gray-bearded man, dark-haired woman · First frame: 0:10
Suit / wardrobe: White base, teal/orange accents, chest panels, clear visors
Wear / dirt: Clean initially, minimal wear
Equipment: Helmets, gloves, blue sample container, metal case

THE WORLD
Gravity read: 1g on ice, 0g in space/station
Atmosphere read: Dense storm on surface, vacuum in space
Light sources: Harsh directional sun, interior module LEDs, fire
Location: Icy planet, orbital space station

MOTION
Camera: Mixed (static, tracking, push-ins)
Subject: Walking, running, ship flight, zero-g floating

SEVERITY TALLY
🔴 BLOCKER: 3    🟠 MAJOR: 3    🟡 MINOR: 4

TOP 3 CRITICAL ERRORS
3:00 — 🔴 BLOCKER — Rigid floating characters (no limb drift, dragged through space).
3:14 — 🔴 BLOCKER — Frozen/static particles (fire and smoke do not disperse).
3:40 — 🔴 BLOCKER — Text visible on screen (title card violation).

DETAILED ERROR LOG
0:16 — 🟡 MINOR — Character — Minor finger morphing on blue container.
0:20 — 🟠 MAJOR — Scale & Physics — Ship scale shifts compared to initial wide shot.
0:26 — 🟠 MAJOR — Motion — Walking animation slides/moonwalks; lacks planted weight.
0:45 — 🟡 MINOR — Motion — Jello effect on characters running.
0:50 — 🟡 MINOR — Character — Airbrushed/waxy skin texture on woman.
2:00 — 🟠 MAJOR — Particles — Station explosion yields lightweight CGI spray.
3:00 — 🔴 BLOCKER — Scale & Physics — Characters float as rigid 2D models.
3:14 — 🔴 BLOCKER — Particles — Fire and smoke hang completely frozen in module.
3:40 — 🔴 BLOCKER — Negative Violations — Burned-in text on screen.

WHAT WORKED WELL
Visor transparency and interior helmet lighting.
Ship design consistency across establishing shots.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to video prompt: "continuous micro-motion, independent limb drift" → prevents rigid zero-g.
REMOVE from image prompt: "cinematic lighting" → causes waxy skin.
REPLACE "explosion" with "mass-consistent debris, heavy ejecta arcs" → prevents lightweight particle spray.

NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [4, 23, 31, 33].

FLAGS FOR DOCUMENT CHECK
0:50 — interior helmets on — QUESTION: was helmet removal specified for interior?
2:00 — station explosion — QUESTION: was a hard vacuum atmosphere specified, forbidding sound?
3:40 — title card — QUESTION: was text generation explicitly requested despite series rules?

QUALITY TABLE ROW
| (not supplied) Ⓥ | (not supplied) | 5 | 4 | UNV | 6 | 6 | UNV | 4 | 5/10 |
