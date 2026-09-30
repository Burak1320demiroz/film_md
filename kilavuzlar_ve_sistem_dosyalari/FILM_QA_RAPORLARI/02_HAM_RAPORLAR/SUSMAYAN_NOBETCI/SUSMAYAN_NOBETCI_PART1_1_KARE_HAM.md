FORMAT: YATAY
INPUT MODE: V — video-only
BASELINE: SELF-CONSISTENCY + PHYSICS — answers "internally consistent and physically believable?", NOT "matches its design document?"
FILM: (not supplied)
FORMAT: YATAY ASPECT MEASURED: 16:9 — measured from video frame dimensions
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 239 s measured
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 23 cuts at 0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50
NON-SCENE MATERIAL: none
LINES HEARD: 2 · "Stop" at 0:14, "F6" at 2:23
SPEC BLOCK PROVIDED: no — mode V

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 8/10 | −2 · 0:14, 1:40 glove seam shift and visor reflection jitter |
| Scale & Physics | 6/10 | −4 · 1:52 zero-g momentum loss; 3:12 hanging lamps sway in 1G orbital weightlessness |
| Camera | 8/10 | −2 · 0:50 space station perspective warping against planet limb |
| Lighting | 8/10 | −2 · 0:16 AI bloom around helmet spotlights; 3:10 porthole glow haze |
| Environment | 8/10 | −2 · 0:25 planet texture swimming; 2:42 breach hole geometry drift |
| Creatures | — | no in-scope source |
| Particles & Materials | 7/10 | −3 · 0:04, 2:34 planar particle spray and lack of mass dynamics |
| Dialogue & Audio | 4/10 | −6 · 0:04, 1:10, 2:33, 3:23 sound in vacuum (explosions, thrusters, latching) |
| Frame Anchor Fidelity | — | no in-scope source |
| Negative Violations | 4 count | airborne sound in vacuum, AI bloom, flat particles, breach drift |
| Motion Quality | 8/10 | −2 · 1:05, 2:03 micro-jitter during control panel lever activation |
| Vertical Format (9:16) | N/A | horizontal format |
| Safe Zone | N/A | horizontal format |
| Hook Timing | N/A | horizontal format |

VERDICT: REGENERATE

## SCENE INVENTORY

MATERIAL given: compilation · duration 239 s · cuts visible: 23 cuts · aspect: 16:9
CHARACTER face/hair visible in helmet close-ups (0:10, 3:40) · heavy padded white EVA suit with orange arm striping and dark leather gloves · wear/scuffs on helmet ring and glove knuckles
WORLD zero-g orbital space environment over red/orange planetary body · atmospheric vacuum · key directional sun lighting + interior warm incandescent panel lights
MOTION camera mostly locked off or slow push-ins per shot · subjects include small tug craft, cylindrical habitat module, debris particles, and astronaut arm movements

## PRESENCE STRING

11111111--111-1-111---111

## TOP 3 CRITICAL ERRORS

1. 0:04 — 🔴 BLOCKER — Explosive acoustic boom audible in space vacuum during craft separation.
2. 2:33 — 🔴 BLOCKER — Main engine explosion sound carrying airborne acoustic roar in vacuum.
3. 3:12 — 🟠 MAJOR — Hanging lamps inside porthole windows sway in 1G pendulum motion despite orbital zero-G.

## DETAILED ERROR LOG

00:04 — 🔴 BLOCKER — Dialogue & Audio — Acoustic explosion sound carrying through space vacuum.
00:04 — 🟠 MAJOR — Particles & Materials — Debris spray behaves like planar 2D particle layer without 3D rotation.
00:16 — 🟠 MAJOR — Lighting & Color — Soft dreamy AI bloom around helmet spotlight emitters.
00:25 — 🟡 MINOR — Environment & World — Planetary texture surface undergoes slight swimming drift.
00:50 — 🟠 MAJOR — Camera — Rotating ring station exhibits perspective scale warping relative to horizon.
01:05 — 🟡 MINOR — Motion Quality — Micro-jitter on glove fingers during lever actuation.
01:10 — 🔴 BLOCKER — Dialogue & Audio — Thruster combustion roar audible in vacuum.
01:40 — 🟡 MINOR — Character — Glove stitching pattern shifts between cockpit control shots.
01:52 — 🟠 MAJOR — Scale & Physics — Decoupled hull plate floats without angular momentum or rotational drift.
02:33 — 🔴 BLOCKER — Dialogue & Audio — Engine blast explosion produces full acoustic shockwave audio in space.
02:34 — 🟠 MAJOR — Particles & Materials — Low-density spark spray lacking physical mass/inertia.
02:42 — 🟠 MAJOR — Environment & World — Structure breach geometry shifts edges between wide and close cuts.
03:10 — 🟠 MAJOR — Lighting & Color — Unmotivated atmospheric haze halo around exterior module portholes.
03:12 — 🟠 MAJOR — Scale & Physics — Lantern lamps inside windows show gravitational hanging sway in zero-G.
03:23 — 🔴 BLOCKER — Dialogue & Audio — Heavy metallic latch impact sound propagating through vacuum.

## WHAT WORKED WELL

* High-fidelity surface texturing on cockpit panels, leather gloves, and metal hull plates.
* Believable facial skin pores and natural eye tracking inside helmet close-ups.
* Excellent hard-surface sci-fi design language across spacecraft models.

## PROMPT IMPROVEMENT SUGGESTIONS

* ADD to video prompt: "hard vacuum environment, zero acoustic audio propagation in space, silent exterior space shots" → prevents sound in vacuum errors.
* REMOVE "cinematic glow, dreamy lighting" → prevents AI bloom around spotlights and portholes.
* REPLACE "floating debris" with "rigid hardware fragments drifting with constant zero-gravity angular velocity" → prevents planar particle floating.

## NEW LESSON CANDIDATE

## 🔴 DERS 12: UZAYDA SES VE AĞIRLIKSIZLIK FİZİĞİ SİMÜLASYONU

**Kaynak:** (not supplied) QA — Dialogue & Audio: 4/10 — 00:04 — Uzay vakumunda patlama ve motor sesi ihlali
**Sorun:** AI video modelleri dış mekan uzay sahnelerine varsayılan olarak atmosferik ses efektleri ve dikey yerçekimi sallantıları (sarkan lamba vb.) eklemektedir.
**ÇÖZÜM:** Dış uzay istemlerine `silent vacuum, mute exterior space, weightless floating objects, zero-g inertia` negatif ve pozitif parametrelerini ekleyin.

## OUT-OF-SCOPE FLAGS

none

## FLAGS FOR DOCUMENT CHECK

— "Stop" spoken word heard — QUESTION: Is dialogue intended in this silent cockpit sequence?
— "F6" radio chatter heard — QUESTION: Was off-screen comms audio scripted for scene 15?

## QUALITY TABLE ROW

| (not supplied) Ⓥ | YATAY | Compilation | 8 | 6 | 8 | 8 | 8 | | 7 | 4 | | 8 | | | | [Negatif: 4] | — |
