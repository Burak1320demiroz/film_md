# 🔧 THE STONE SKY — TEKNİK QA HAM RAPORU

> **Rubrik:** `../../QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> **Alındı:** 05.08.2026 · dış model, repo erişimsiz · girdi: video + rubrik (MOD V)
> **Model çıktısı aşağıda olduğu gibi korunmuştur — düzenlenmedi.**
> Tablolar operatör yapıştırmasında düzleşmiş olabilir; içerik dokunulmamıştır.
> Belge kontrolü cevapları burada DEĞİL → `../01_FILM_RAPORLARI/THE_STONE_SKY.md`

---

INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: (not supplied)
SCENE: (not supplied)
VIDEO DURATION: 135s
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 4/10 (2 UNVERIFIABLE categories excluded)
VERDICT: REGENERATE

SCORES SUMMARY

| Category | Score | Critical Issues |
|---|---|---|
| Character | 3/10 | Clone appears; heavy suit drift. |
| Scale & Physics | 4/10 | Mixed gravity (rover falls fast, dust floats). |
| Camera | 3/10 | Frequent hard cuts mid-action. |
| Lighting | 5/10 | Shadows mismatch on falling debris. |
| Environment | 6/10 | Terrain and sky remain mostly stable. |
| Creatures | UNVERIFIABLE | No creatures present. |
| Particles & Materials | 3/10 | Debris hangs without momentum. |
| Dialogue & Audio | 4/10 | Poor lip sync; sound in apparent vacuum. |
| Frame Anchor Fidelity | UNVERIFIABLE | Requires pipeline data. |
| Negative Violations | 5 count | Text, cuts, clone, particles, lip sync. |
| Motion Quality | 4/10 | Sliding footsteps; rigid posing. |

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 135s
Cuts you can see: multiple (0:05, 0:09, 0:19, 0:23, 0:30, etc.)
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: short dark hair, minor facial scarring/dirt. First seen: 0:00.
Suit / wardrobe: light grey/beige suit, orange striping, dark chest rig, clear dome helmet.
Wear / dirt: clean base, minor dust on boots.
Equipment: portable drill, driving a 4-wheeled rover.

THE WORLD
Gravity read: mixed. Dust/debris falls slowly (low-g), but heavy rover and impacts suggest 1g.
Atmosphere read: vacuum visual (no sky scatter), but airborne sound and dust suspension occur.
Light sources: single primary hard source (sun) back-left.
Location: barren rocky moon, giant ringed planet in background.

MOTION
Camera: mix of static lockoffs, slow tracking, and push-ins.
Subject: kneeling/drilling, driving, running. Speeds vary wildly.

SEVERITY TALLY
🔴 BLOCKER: 4    🟠 MAJOR: 4    🟡 MINOR: 3

TOP 3 CRITICAL ERRORS
2:10 — 🔴 BLOCKER — Burned-in text "THE STONE SKY" covers frame.
1:40 — 🔴 BLOCKER — Duplicate character; two identical astronauts running side-by-side.
0:05 — 🔴 BLOCKER — Hard cut from wide drill shot to close-up speaking face.

DETAILED ERROR LOG
0:05 — 🔴 BLOCKER — Camera — Hard cut mid-scene (violates single-cut rule if judged as continuous).
0:06 — 🟠 MAJOR — Audio — Lip sync fails to match "Analyze that" audio line.
0:09 — 🟠 MAJOR — Character — Suit drift; chest rig changes geometry upon standing.
0:30 — 🔴 BLOCKER — Particles — Debris columns freeze and hang in mid-air without momentum.
0:56 — 🟠 MAJOR — Audio — Sync drift on "Impact line ahead".
1:16 — 🟡 MINOR — Lighting — Shadows on falling rocks front-right, contradicting back-left sun.
1:36 — 🟠 MAJOR — Motion — Character moonwalks/slides; feet do not plant with weight.
1:40 — 🔴 BLOCKER — Character — Clone generation (two identical astronauts).
2:06 — 🟡 MINOR — Character — Left hand fingers appear fused when resting on dark ground.
2:10 — 🔴 BLOCKER — Negative Violations — Large cinematic title text burned into frame.

WHAT WORKED WELL
Visor transparency and reflections are generally stable without breaking face geometry.
Gas giant and ring structures remain locked and static in the sky.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to negative prompt: "text, watermark, typography, title cards" → prevents burned-in titles.
ADD to negative prompt: "multiple characters, clones, duplicates" → prevents the twin anomaly.
REPLACE "dynamic editing" with "single continuous unbroken shot" → prevents injected cuts.

NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [1, 4, 15, 20, 33].

FLAGS FOR DOCUMENT CHECK
0:00 — airborne sound and hanging dust — QUESTION: is this a vacuum or thin atmosphere?
0:05 — multiple hard cuts in sequence — QUESTION: is this a compilation edit with defined boundaries?
1:36 — sliding gait — QUESTION: was locomotion specified as walking or low-g bounding?

QUALITY TABLE ROW
| (not supplied) Ⓥ | (not supplied) | 3 | 4 | 3 | 5 | 6 | UNV | 4 | 4/10 |
