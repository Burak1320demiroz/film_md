INPUT MODE: V — video-only
BASELINE: SELF-CONSISTENCY + PHYSICS — answers "internally consistent and physically believable?", NOT "matches its design document?"
FILM: (not supplied)
FORMAT: YATAY        ASPECT MEASURED: 16:9 (container ratio W > H)
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 230 s measured
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 22 — 00:10, 00:20, 00:30, 00:40, 00:50, 01:00, 01:10, 01:20, 01:30, 01:40, 01:50, 02:00, 02:10, 02:20, 02:30, 02:40, 02:50, 03:00, 03:10, 03:20, 03:30, 03:40
NON-SCENE MATERIAL: none
LINES HEARD: 3 · "Line secure, bracing." (00:23), "Sector 7 clear." (02:31), "...rest of the... life support system..." (03:31)
SPEC BLOCK PROVIDED: no — mode V

SCORES SUMMARY
Category	Score	Critical Issues
Character	7/10	−3 · 00:07 (F1), 02:40 (F1), 03:01 (F1)
Scale & Physics	6/10	−4 · 00:12 (F2), 01:56 (F2), 03:21 (F2)
Camera	8/10	−2 · 00:15 (F3)
Lighting	8/10	−2 · 01:00 (F4), 02:30 (F4)
Environment	7/10	−3 · 01:30 (F5), 02:10 (F5)
Creatures	—	no in-scope source
Particles & Materials	6/10	−4 · 00:16 (F7), 00:26 (F7), 01:04 (F7), 03:22 (F7)
Dialogue & Audio	9/10	−1 · 03:31 (F8)
Frame Anchor Fidelity	UNVERIFIABLE	mode V — no target frames provided
Negative Violations	6 count	waxy skin, hand morph, AI bloom, texture swimming, low-density dust spray, motion jitter
Motion Quality	7/10	−3 · 01:56 (F11), 02:45 (F11)
Vertical Format (9:16)	N/A	format is YATAY
Safe Zone	N/A	format is YATAY
Hook Timing	N/A	format is YATAY
VERDICT: REGENERATE

SCENE INVENTORY — mode V only
MATERIAL: compilation · duration 230 s · cuts: 22 (00:10, 00:20, 00:30, 00:40, 00:50, 01:00, 01:10, 01:20, 01:30, 01:40, 01:50, 02:00, 02:10, 02:20, 02:30, 02:40, 02:50, 03:00, 03:10, 03:20, 03:30, 03:40) · aspect: 16:9
CHARACTER: two astronauts (white EVA pressure suit with blue trim; orange EVA suit with dark grey harness) · first frame fully visible: 00:00 (gloved hands), 00:10 (full figures) · suit/wardrobe: multi-layer planetary pressure suits, utility pouches, safety carabiners, reflective/clear visors · wear/dirt: moderate scuff marks and fine red regolith dust along knees, elbows, chest plates.
WORLD: gravity read: low-to-medium planetary gravity (slow dust settling, floaty debris acceleration) · atmosphere read: thin/airless exterior under dark sky with celestial bodies (eclipse ring, gas giant); radio comms and mechanical suit audio present · light sources: harsh direct solar/key light with deep shadows, secondary warm interior fills · location: canyon ridge, cliff faces, catwalk structure, lander craft exterior and airlock/cockpit interior.
MOTION: camera: mix of static detail holds, slow tracking pushes, overhead POVs, and low-angle exterior shots · subject: tether handling, cliff climbing, grating collapse, airlock ingress/egress, pilot seating.

PRESENCE STRING
11111111111111111111-1-

TOP 3 CRITICAL ERRORS (most impactful)
01:56 — 🔴 BLOCKER — Catwalk grating collapses beneath astronaut, causing the figure to float/glide unnaturally without realistic gravity acceleration or drop momentum.

02:40 — 🟠 MAJOR — Hand contact morphing and finger fusion when the orange-suited astronaut grabs the white suit wrist during the rescue pull.

01:30 — 🟠 MAJOR — Metal panel surface texture breathes and swims while the gloved hand operates the hatch latch mechanism.

DETAILED ERROR LOG
00:07 — 🟡 MINOR — Character — Glove fingers slip and deform structure slightly while tightening yellow rope knot around metal railing.

00:12 — 🟠 MAJOR — Scale & Physics — Collapsing metal bridge structure drops into canyon like lightweight material without structural mass inertia.

00:15 — 🟡 MINOR — Camera — Unmotivated micro-jitter and frame edge distortion during wide pan across canyon rim.

00:16 — 🟠 MAJOR — Particles & Materials — Dust clouds from canyon edge collapse expand as low-density volumetric haze rather than ballistically falling dust/rock particles.

00:26 — 🟠 MAJOR — Particles & Materials — Loose rock and dust trickling down cliff face phase directly through astronaut suit shoulder material without physical collision.

01:00 — 🟠 MAJOR — Lighting — Key light direction flips between wide lander shot and cliff shots relative to the eclipse position in background sky.

01:04 — 🟠 MAJOR — Particles & Materials — Dust kicked up by walking astronauts floats without gravity weight, remaining suspended in thin atmosphere.

01:30 — 🟠 MAJOR — Environment — Surface metal plating on machine panel swims/morphs under hand pressure during lever operation.

01:56 — 🔴 BLOCKER — Scale & Physics — Astronaut falls through collapsed catwalk section with zero-G glide physics instead of gravity acceleration.

02:10 — 🟠 MAJOR — Environment — Background gas giant ring geometry changes scale and tilt angle compared to earlier wide exterior shots.

02:30 — 🟡 MINOR — Lighting — Unmotivated soft AI bloom and glow around dark cockpit control panel indicators.

02:40 — 🟠 MAJOR — Character — Glove fingers phase and fuse into sleeve fabric during two-person wrist grab.

02:45 — 🟠 MAJOR — Motion Quality — Temporal warping/jello effect on arm pulling motion during airlock entrance rescue.

03:01 — 🟠 MAJOR — Character — Astronaut face inside helmet appears noticeably airbrushed/waxy with lost skin pore texture compared to real photoreal footage.

03:21 — 🟠 MAJOR — Scale & Physics — Lander engine thruster blast creates flat 2D-like floor tile tearing without mass-consistent debris arcs or structural resistance.

03:22 — 🟠 MAJOR — Particles & Materials — Thruster exhaust dust spray lacks momentum density and dissipates like CG particle fog.

03:31 — 🟡 MINOR — Dialogue & Audio — Radio transmission speech cuts off abruptly with static distortion mid-phrase ("...rest of the... life support system...").

WHAT WORKED WELL (keep these in future prompts)
Tactile detail on suit fabric scuffs, metal carabiners, and mechanical hatch latches in close-up insert shots.

Strong high-contrast directional lighting on cliff faces and lander exterior hull panels.

Convincing radio audio filtering and breathing sound design on suit comms channels.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to video prompt: "hard physical collision between falling rock particles and astronaut suit material, sharp trajectory decay" → prevents particle phasing and floaty dust haze.

ADD to video prompt: "solid tactile grip with distinct glove digits on suit wrist, zero mesh penetration" → prevents hand contact morphing and finger fusion.

REMOVE "cinematic glow, dreamy atmosphere, soft lighting".

REPLACE "collapsing structure" with "heavy steel girder collapse with high structural mass and rapid acceleration drop".

NEW LESSON CANDIDATE
No new lesson — all errors map to patterns 2 (Plastic Skin), 3 (AI Bloom), 4 (Hand Morph at Contact), 5 (Particle Physics), 6 (Texture Swimming), and 8 (Zero-G Momentum Loss).

OUT-OF-SCOPE FLAGS
01:00 vs 03:20 lander footprint position relative to metal platform edge — CONTINUITY lens.

FLAGS FOR DOCUMENT CHECK — mode V only
00:10 — Bridge structure collapsed in canyon — QUESTION: Was the bridge collapse meant to occur on-screen in this scene or pre-exist?

00:23 — Radio line "Line secure, bracing." — QUESTION: Was this line scripted for astronaut 1 or astronaut 2?

02:30 — Cockpit interior layout — QUESTION: Was an orange pilot suit suit-change specified for scene 16?

NEGATIVE BIBLE CHECKLIST & LINKED FINDINGS
[ ] cut/transition inside a single clip
[x] airbrushed, waxy, plastic skin → 03:01 · cat. 1 · 🟠
[x] hand breakdown near glowing surfaces / hand-surface fusion / extra fingers → 02:40 · cat. 1 · 🟠
[x] AI bloom / dreamy haze → 02:30 · cat. 4 · 🟡
[x] melting terrain / swimming rock texture → 01:30 · cat. 5 · 🟠
[x] low-density impact spray · frame-rate variance → 00:16 · cat. 7 · 🟠
[x] motion quality temporal jello/warp → 02:45 · cat. 11 · 🟠

NEGATIVE BOX COUNT: 6 · LINKED FINDINGS: 6 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 6 · TICKED: 6 · MISSED: 0
NO BOX EXISTS FOR: light source directional flip across montage cuts

QUALITY TABLE ROW (operator's technical quality table)
| (not supplied) Ⓥ | YATAY | Compilation | 7/10 | 6/10 | 8/10 | 8/10 | 7/10 | — | 6/10 | 9/10 | | 7/10 | | | | [Negatif: 6] | — |
