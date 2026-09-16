INPUT MODE: V — video-only
BASELINE: SELF-CONSISTENCY + PHYSICS — answers "internally consistent and physically believable?", NOT "matches its design document?"
FILM: (not supplied)
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 179s
MATERIAL TYPE: FILM
CUTS COUNTED: 17 (0:09, 0:19, 0:29, 0:39, 0:49, 0:59, 1:09, 1:19, 1:29, 1:39, 1:49, 1:59, 2:09, 2:19, 2:29, 2:39, 2:49)
NON-SCENE MATERIAL: none
LINES HEARD: 9 · "Orientation aligned. Horizon locked." (0:02), "Sling secured." (0:11), "Nav override ready." (0:13), "Jesper, Horizon station, maintain approach vector." (0:21), "Guidance data is unreliable." (0:48), "Switching to manual attitude control." (0:51), "Horizon distance 142." (1:07), "0.15 meters per second. Line is true." (1:36), "Hard lock engaged." (2:06)
SPEC BLOCK PROVIDED: no — mode V

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 4/10 | 🔴 Suit design drifts significantly between cuts (2:20). |
| Scale & Physics | 5/10 | 🟠 Thruster exhaust exhibits atmospheric vapor dispersion in vacuum (1:12). |
| Camera | 6/10 | 🟠 Optical reticle HUD overlays behave as 2D graphics plane (1:04). |
| Lighting | 5/10 | 🟠 Unmotivated interior fill lighting and diffuse bloom on visor glass (0:07). |
| Environment | 6/10 | 🟠 Background starfield density shifts across module docking angles (0:30). |
| Creatures | — | no in-scope source |
| Particles & Materials | 5/10 | 🟠 Debris and vapor particles lack micro-g inertia (0:05). |
| Dialogue & Audio | 4/10 | 🔴 Airborne radio chatter lacks suit transmission acoustics in vacuum (0:02). |
| Frame Anchor Fidelity | UNVERIFIABLE | Mode V pass — start/end frame anchors not supplied. |
| Negative Violations | 4 count | 🔴 On-screen HUD text, suit drift, vacuum audio, AI bloom. |
| Motion Quality | 6/10 | 🟠 Minor motion warping during manual joystick control (1:22). |
| Vertical Format (9:16) | N/A | Format is YATAY (16:9). |
| Safe Zone | N/A | Format is YATAY (16:9). |
| Hook Timing | N/A | Format is YATAY (16:9). |

VERDICT: REGENERATE

## SCENE INVENTORY

* **MATERIAL:** Compilation clip · duration 179 s · 17 visible hard cuts separating 18 shots · aspect ratio 16:9.
* **CHARACTER:** Two astronauts (male pilot, female copilot) · white/grey pressure suits with chest harness, wrist units, clear visors · suit paneling shifts to blue accent in airlock shot (2:20).
* **WORLD:** Orbital space station exterior and capsule interior · vacuum atmosphere · hard directional key light from distant star with soft unmotivated cabin fill · metallic interiors and station hull.
* **MOTION:** Mix of slow orbital push-ins, interior static lockoffs, and hand adjustments on controls.

## PRESENCE STRING

`-1--111-1---111111`

## TOP 3 CRITICAL ERRORS

1. 0:02 — 🔴 BLOCKER — Dialogue & Audio — Unfiltered airborne voiceover played over vacuum exterior without suit radio acoustic processing.
2. 0:41 — 🔴 BLOCKER — Negative Bible — On-screen computer HUD text graphics burned directly over video frame.
3. 2:20 — 🔴 BLOCKER — Character — Suit wardrobe drifts from standard white suit to blue chest paneling mid-sequence.

## DETAILED ERROR LOG

* 0:02 — 🔴 — Dialogue & Audio — Clear airborne voice acoustics present during external vacuum shot.
* 0:05 — 🟠 — Particles & Materials — Dust/ice particles drift with artificial camera-dragged motion.
* 0:07 — 🟠 — Lighting & Color — Diffuse AI bloom haze present around station solar arrays and module highlights.
* 0:41 — 🔴 — Negative Bible — Burned-in text and numerical readouts overlaying cockpit monitor view.
* 0:58 — 🟠 — Character — Visor HUD target graphic floats off-plane from glass reflection.
* 1:04 — 🟠 — Camera & Cinematography — Scope reticle overlay lacks optical depth and lens glass distortion.
* 1:12 — 🟠 — Scale & Physics — RCS thruster plume expands like dense atmospheric vapor in hard vacuum.
* 2:20 — 🔴 — Character Consistency — Copilot suit shifts color scheme to blue torso accents before reverting.
* 2:41 — 🔴 — Negative Bible — Text labels ("RADIATION DOSIMETER") rendered on wall monitor prop asset.

## WHAT WORKED WELL

* High surface detail on exterior hull greebles and metallic docking ring mechanisms.
* Consistent character facial structure and realistic skin texture under interior lighting.

## PROMPT IMPROVEMENT SUGGESTIONS

* ADD to video prompt: `"hard vacuum RCS thruster plume, crisp directional lighting, no atmospheric haze"` → prevents thruster vapor spreading like steam.
* REMOVE `"cinematic glow, screen graphics display"`.
* REPLACE `"digital HUD overlay"` with `"physical mechanical gauge, clean glass visor"`.

## NEW LESSON CANDIDATE

No new lesson — all errors map to patterns 1, 2, 3, 7, and 11.

## OUT-OF-SCOPE FLAGS

* 1:29 — Docking probe latch mechanism geometry differs slightly from wide station view at 0:25 — CONTINUITY lens.

## FLAGS FOR DOCUMENT CHECK

* 0:10 — Male astronaut wears arm sling inside suit — QUESTION: Was an injured arm specified in character lore?
* 1:00 — Pilot uses optical telescope sight for docking — QUESTION: Was optical manual alignment in script plan?

## QUALITY TABLE ROW

| [Film] | [Format] | [Sahne] | [Karakter] | [Fizik] | [Kamera] | [Işık] | [Çevre] | [Canlı] | [Parçacık] | [Diyalog-Ses] | [Kare Çapası] | [Hareket] |  | [Güvenli Alan] | [Kanca] | [Negatif: n] | — |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (not supplied) Ⓥ | YATAY | Compilation | 4/10 | 5/10 | 6/10 | 5/10 | 6/10 |  | 5/10 | 4/10 |  | 6/10 |  |  |  | [Negatif: 4] | — |
