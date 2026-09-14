FORMAT: YATAY
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

MATERIAL
What you were given: compilation edit · duration 105s
Cuts you can see:    9 (0:09, 0:19, 0:29, 0:39, 0:49, 0:59, 1:09, 1:19, 1:29)
Aspect ratio:        16:9

THE CHARACTER — as first clearly seen
Face / hair / marks: Not visible, helmeted        First frame fully visible: 0:00
Suit / wardrobe:     White suit, gray/yellow accents, chest harness
Wear / dirt:         Clean, minor dust on boots
Equipment:           Gold visor, handheld diagnostic scanner

THE WORLD — as the footage shows it
Gravity read:     ~1g (planted footsteps, heavy suit movement)
Atmosphere read:  Dense (dust particles hang, sound carries)
Light sources:    Sunlight (hard, top-left), tower fissures (soft amber, untraceable bounce)
Location:         Barren rocky valley, monolithic black tower

MOTION
Camera:  Static lockoffs, slow pushes
Subject: Slow, deliberate walking, scanning

SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES:  8
SUM OF SCORES:      40.0
DIVISION:           40.0 ÷ 8 = 5.0

OVERALL SCORE: 5.0/10 (Excluded: Creatures, Frame Anchor Fidelity, Vertical Format, Safe Zone, Hook Timing)
VERDICT: REGENERATE

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 4/10 | −3 · 0:20 (F1) · 1:20 (F2) |
| Scale & Physics | 5/10 | −2 · 1:10 (F1) |
| Camera | 5/10 | −2 · 0:50 (F1) |
| Lighting | 5/10 | −2 · 1:25 (F1) |
| Environment | 6/10 | −1 · 0:30 (F1) |
| Creatures | — | no in-scope source |
| Particles & Materials | 4/10 | −3 · 1:10 (F1) |
| Dialogue & Audio | 6/10 | −1 · 0:24 (F1) |
| Frame Anchor Fidelity | — | no in-scope source |
| Negative Violations | 3 count | 0:20, 0:24, 1:25 |
| Motion Quality | 5/10 | −2 · 0:20 (F1) |
| Vertical Format (9:16) | N/A | format is yatay |
| Safe Zone | N/A | format is yatay |
| Hook Timing | N/A | format is yatay |

NEGATIVE BOX COUNT: 3 · LINKED FINDINGS: 3 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 3 · TICKED: 3 · MISSED: 0
NO BOX EXISTS FOR: missing sound effect sync

## SCENE INVENTORY — mode V only

[Completed in BASELINE block above]

## PRESENCE STRING

111111111

## SEVERITY TALLY

🔴 BLOCKER: 2    🟠 MAJOR: 3    🟡 MINOR: 1

## TOP 3 CRITICAL ERRORS

1. 0:24 — 🔴 BLOCKER — Character: Burned-in text visible on the scanner display.
2. 0:20 — 🔴 BLOCKER — Character: Hand geometry fuses directly into the scanner casing.
3. 1:10 — 🟠 MAJOR — Particles: Floating rocks lack physical momentum, hanging statically.

## DETAILED ERROR LOG

0:20 — 🔴 BLOCKER — Character — Hand geometry morphs into the scanner body.
0:24 — 🔴 BLOCKER — Character — AI-generated text/symbols appear on the screen.
0:30 — 🟡 MINOR — Environment — Slight texture swimming on the distant mountain ridges.
0:50 — 🟠 MAJOR — Camera — Internal reflection on the visor moves independently of head track.
1:10 — 🟠 MAJOR — Particles & Materials — Suspended debris exhibits frozen, flat 2D behavior.
1:20 — 🟠 MAJOR — Character — Right hand holding the emitter shows phantom digits.
1:25 — 🟠 MAJOR — Lighting — Excessive AI bloom wash surrounds the energy sphere.

## WHAT WORKED WELL

* The cinematic space-exploration score integrates seamlessly with the visual pacing.
* The overarching monochrome aesthetic with high-contrast amber accents remains exceptionally stable across cuts.

## PROMPT IMPROVEMENT SUGGESTIONS

For robust multi-scene workflows, especially when executing local generations, control these specific artifacts:

1. ADD to image prompt: "sharp directional light, defined shadows, blank display screens" → prevents AI bloom and text generation.
2. REMOVE from prompt: "cinematic lighting, glowing data" → causes waxy bloom and Veo text artifacts.
3. REPLACE "energy field" with "sharp electrical arcing, clear atmospheric distortion" → prevents the diffuse spherical bloom filter.

## 🔴 DERS 101: GÖRÜNMEZ YAZI VE EKRAN ARTEFAKTLARI

**Kaynak:** THE_AMBER_LATTICE Ⓥ QA — Character: 4/10 — `0:24 — text visible on the scanner display`
**Sorun:** Model, ekran veya cihaz gördüğünde otomatik olarak anlamsız metinler üretir.
**ÇÖZÜM — PROMPT GÜNCELLEMESİ:**

```
blank screen, perfectly dark glass display, entirely devoid of text, no UI elements
```

## OUT-OF-SCOPE FLAGS

none

## FLAGS FOR DOCUMENT CHECK — mode V only

1:19 — sudden appearance of spherical energy shield — QUESTION: was an energy shield specified in the prop list?
1:40 — title card attached — QUESTION: is the card intentional for this edit?

## QUALITY TABLE ROW

| THE_AMBER_LATTICE Ⓥ | YATAY | Compilation | 4 | 5 | 5 | 5 | 6 | | 4 | 6 | | 5 | | | | 3 | **5.0/10** |
