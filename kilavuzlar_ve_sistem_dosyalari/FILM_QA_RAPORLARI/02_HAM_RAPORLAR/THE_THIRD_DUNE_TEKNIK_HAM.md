# THE THIRD DUNE — VIDEO_QA (TEKNİK) HAM RAPOR

> **Tarih:** 11.08.2026 · **Rubrik:** `QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> **Mod:** V (SPEC yapıştırılmadı) · **Malzeme:** 245 s kurgu
> ⛔ Model çıktısı olduğu gibi. Düzenleme yok. Değerlendirme film kaydında:
> `../01_FILM_RAPORLARI/THE_THIRD_DUNE.md`

---

```
INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: (not supplied)
SCENE: Compilation
VIDEO DURATION: 245s
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 4/10 (2 categories excluded)
VERDICT: REGENERATE
```

## SCORES SUMMARY

| Category | Score | Critical Issues |
|---|---|---|
| Character | 4/10 | Hand fusion, visor shifts |
| Scale & Physics | 4/10 | Sand mass behaves like fluid |
| Camera | 5/10 | Standard tracking, mostly stable |
| Lighting | 5/10 | Uniform, minor bloom on panels |
| Environment | 4/10 | Dune textures swim/morph |
| Creatures | N/A | None present |
| Particles & Materials | 3/10 | Fluid sand, poor collision |
| Dialogue & Audio | 4/10 | Causal binding drift |
| Frame Anchor Fidelity | UNVERIFIABLE | Needs plan file |
| Negative Violations | 4 count | Text, fusion, texture swim, zero-mass spray |
| Motion Quality | 4/10 | Moonwalking, jello footsteps |

## SCENE INVENTORY

```
MATERIAL
What you were given: Compilation edit · duration 245s
Cuts you can see: Multiple scene boundaries
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Male with beard, female with dark hair. Fully visible: 0:10.
Suit / wardrobe: White/tan base, ribbed padding, blue/purple accents.
Wear / dirt: Slight dirt on knees/shins.
Equipment: Clear visors, backpacks, cargo boxes, shovel.

THE WORLD
Gravity read: ~1g expected, but particles read lower/floaty.
Atmosphere read: Dense enough for dust storms and sound.
Light sources: Single bright sun, harsh shadows.
Location: Desert dune landscape.

MOTION
Camera: Mostly static lockoffs, slow pushes, and lateral tracking.
Subject: Walking, digging, kneeling, lifting.
```

## SEVERITY TALLY

🔴 BLOCKER: 3    🟠 MAJOR: 3    🟡 MINOR: 2

## TOP 3 CRITICAL ERRORS (most impactful)

1. 4:00 — 🔴 BLOCKER — Burned-in title card text ("THE THIRD DUNE").
2. 2:51 — 🔴 BLOCKER — Hand and wrench completely fuse with the landing gear strut.
3. 1:50 — 🔴 BLOCKER — Glove fingers phase through the sand surface without physical collision.

## DETAILED ERROR LOG

```
0:33 — 🟠 MAJOR — Motion — Character walks but glides/moonwalks; no weight planted in sand.
1:12 — 🟡 MINOR — Particles — Sand kicked up by boot looks like low-density CGI spray.
1:44 — 🟠 MAJOR — Motion — Astronauts slide down the dune with jello-like leg warping.
1:50 — 🔴 BLOCKER — Character — Fingers phase into sand texture without displacement.
2:05 — 🟠 MAJOR — Physics — Sand pours out of the ship's side like a continuous liquid sheet.
2:51 — 🔴 BLOCKER — Character — Wrench and glove morph into the metal cylinder.
3:33 — 🟡 MINOR — Environment — The sand collapsing into the crater shows texture swimming.
4:00 — 🔴 BLOCKER — Negatives — Title card text on screen.
```

## WHAT WORKED WELL

- The ship's hard-surface geometry remains relatively stable across different shots.
- The overarching color grade (warm amber/orange) is consistent.

## PROMPT IMPROVEMENT SUGGESTIONS

1. ADD to image prompt: "dry granular sand, individual coarse grains" → prevents liquid-like sand pouring.
2. REMOVE from video prompt: "title card, cinematic poster" → causes burned-in text.
3. REPLACE "walking in desert" with "heavy footsteps sinking into deep sand" → prevents gliding/moonwalking.

## NEW LESSON CANDIDATE

No new lesson — all errors map to existing lessons [11, 24, 28, 31, 33].

## FLAGS FOR DOCUMENT CHECK

- 0:10 — Female astronaut speaks — QUESTION: Was dialogue expected for this scene?
- 2:00 — Hexagonal ship appears — QUESTION: Does the scale match the planned vehicle dimensions?
- 3:20 — Ship takes off — QUESTION: Was this vertical thrust takeoff specified in the motion plan?

## QUALITY TABLE ROW

| (not supplied) Ⓥ | Compilation | 4 | 4 | 5 | 5 | 4 | N/A | 4 | 4/10 |
