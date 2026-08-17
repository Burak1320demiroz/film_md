# THE UNBROKEN CITY — TEKNİK HAM RAPOR (VIDEO_QA · MOD V)
> Kayıt: 06.08.2026 · model çıktısı olduğu gibi, düzenlenmedi.

INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: (not supplied)
SCENE: Compilation
VIDEO DURATION: 165 seconds
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 5/10 (3 categories excluded as UNVERIFIABLE)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    4/10    Duplicate figure in frame, airbrushed skin, sliding fingers
Scale & Physics    4/10    Lack of weight transfer on ladder, moonwalking on sand
Camera    8/10    Mostly stable per shot, no mid-shot hidden cuts observed
Lighting    6/10    General consistency is okay, but slight AI bloom on light sources
Environment    5/10    Texture swimming on stone walls in interior shots
Creatures    UNVERIFIABLE    N/A
Particles & Materials    3/10    CGI exhaust spray, hovering dust particles
Dialogue & Audio    UNVERIFIABLE    N/A (No spoken dialogue to verify sync/turn-taking)
Frame Anchor Fidelity    UNVERIFIABLE    Mode V
Negative Violations    4 count    Text on screen, duplicate character, CGI particles, moonwalking
Motion Quality    4/10    Jello effect in walking, sliding feet

SCENE INVENTORY
MATERIAL
What you were given: compilation edit · duration 165s
Cuts you can see: 14 scene boundaries
Aspect ratio: 16:9

THE CHARACTER — as first clearly seen
Face / hair / marks: Female, dark hair pulled back. First frame fully visible: 0:10
Suit / wardrobe: Dark grey/greenish spacesuit with ribbed joints, hard chest box, boots.
Wear / dirt: Clean, minimal weathering.
Equipment: Clear bubble helmet with rear housing, headlamp in later shots, dark gloves.

THE WORLD — as the footage shows it
Gravity read: Seems intended as 1g (Earth-like), but reads lower due to floaty motion.
Atmosphere read: Breath visible (1:59, 1:35), dust settles slowly. Ambient sound carries.
Light sources: Distant sun, harsh directional light, headlamp.
Location: Various (vast concrete plain, sandy dunes, dark stone corridors, circular tunnels).

MOTION
Camera: Static lockoffs, slow pushes, and tracking shots matching subject speed.
Subject: Walking, examining objects, climbing a ladder. Moves at a consistent but slightly floaty pace.

SEVERITY TALLY
🔴 BLOCKER: 3    🟠 MAJOR: 6    🟡 MINOR: 2

TOP 3 CRITICAL ERRORS (most impactful)
2:40 — 🔴 BLOCKER — Burned-in text ("THE WINDOW THAT SHOWS NO SKY") appears on screen, violating the strict no-text rule.
0:40 — 🔴 BLOCKER — Duplicate character/clone visible on the right side of the frame. It acts as an autonomous reflection or a second entity.
2:32 — 🔴 BLOCKER — Rocket exhaust behaves as low-density CGI spray without physical mass, failing to deform the terrain or carry momentum.

DETAILED ERROR LOG
0:10 — 🟡 MINOR — Character — Skin texture on the face appears slightly waxy and airbrushed (lacks pore detail).
0:33 — 🟠 MAJOR — Scale & Physics — Character's boots do not sink into the sand; they float on the surface, lacking physical weight.
0:40 — 🔴 BLOCKER — Character — Duplicate character standing on the right side of the room.
1:25 — 🟠 MAJOR — Environment — Subtle texture swimming/breathing on the stone walls as the camera tracks alongside the character.
1:37 — 🟠 MAJOR — Character — Fingers slide over the metal lock without proper anatomical wrapping or friction.
1:49 — 🟠 MAJOR — Particles & Materials — Dust/particles disturbed by the bowl hover unnaturally in the air instead of falling with a gravitational arc.
2:03 — 🟡 MINOR — Character — Slight frame-rate jitter on the chest box details.
2:12 — 🟠 MAJOR — Motion Quality — Character's feet glide/moonwalk over the terrain rather than planting firmly with each step.
2:25 — 🟠 MAJOR — Scale & Physics — Hands and feet slide through the ladder rungs without believable weight transfer or contact tension.
2:32 — 🔴 BLOCKER — Particles & Materials — Exhaust smoke from the lander is flat, CGI-like spray. No physical ejecta or ground interaction.
2:40 — 🔴 BLOCKER — Negative Violations — Title card text is burned into the final frame.

WHAT WORKED WELL (keep these in future prompts)
Visor transparency is generally well-maintained without clipping into the face.
Camera moves are largely smooth and deliberate, avoiding the handheld "shake" trap.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "sharp skin texture with visible pores, unretouched photography" → prevents airbrushed/waxy face.
REMOVE from video prompt: "cinematic lighting" → causes soft AI bloom on the environment and sky.
REPLACE "exhaust smoke" with "heavy physical dust displacement and heavy terrain ejecta" → prevents low-density CGI particle spray during liftoff.
ADD to video prompt: "no text, no titles, no watermarks, textless" → prevents burned-in title cards.

NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [3, 4, 6, 20, 31, 33].

FLAGS FOR DOCUMENT CHECK — mode V only
0:40 — Character has a reflection or duplicate in the room — was a mirror wall specified, or did the model invent a clone?
1:20 — Flashlight beam is visible in a dark corridor — was FILL LIGHT ALLOWED set to "no"? (The shadows are not pure black).
2:40 — Title card appears at the end of the compilation — was text explicitly requested in the final shot prompt?

QUALITY TABLE ROW
| (not supplied) Ⓥ | Compilation | 4 | 4 | 8 | 6 | 5 | N/A | 4 | 5/10 |
