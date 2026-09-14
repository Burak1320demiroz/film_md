# 🔧 THE BANDED DEEP — TEKNİK QA HAM RAPORU

> **Tarih:** 14.08.2026 · **Model:** Gemini · **Rubrik:** VIDEO_QA_CRITIQUE_PROMPT.md
> **Girdi:** 186 s kurgu (3:06) · **Mod:** V — ⛔ SPEC planda hazırdı (§0.15),
> mod V koşuldu → bu koşu bir ÖN KOŞUDUR [DERS 94].
> Model çıktısı aşağıda olduğu gibi, düzenlenmeden.

---

INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

STEP 1 — MODE V BASELINE
MATERIAL
What you were given: Compilation edit
Duration: 186s (3:06)
Cuts you can see: Multiple apparent scene boundaries.
Aspect ratio: 16:9

THE CHARACTER
Face/hair/marks: Female, dark hair visible through visor. First seen: 0:30.
Suit/wardrobe: White spacesuit with thin blue piping, grey joint details, white backpack, standard helmet with clear visor.
Wear/dirt: Clean, pristine condition.
Equipment: Tether/piton device used at 1:43.

THE WORLD
Gravity read: ~1g based on walking gait, though particle physics conflict with this.
Atmosphere read: Present. Dust kicks up and hangs; clear skies shifting to dusk.
Light sources: Single primary directional sun.
Location: Desert canyon with extreme, wavy, multi-colored rock striations and a distinct horizontal black mineral band.

MOTION
Camera: Mix of wide aerial tracking, static lockoffs, and slow pushes.
Subject: Ship flight, vertical landing, character walking, kneeling, rappelling.

CRITIQUE CATEGORIES

1. 🧑 CHARACTER CONSISTENCY
Suit design remains relatively stable across cuts. Base colors and blue piping persist.
Contact Morphing: Slight structural softening of the glove fingers when brushing the black band.
Detail Flicker: Minor shifting of the blue wrist ring and backpack strap connections across wide shots.
SCORE: 6/10
ISSUES:
0:55 — 🟡 MINOR — Glove fingers slightly glide/soften against the rock texture.
2:02 — 🟠 MAJOR — Hand merges slightly with the dust/surface during the brushing motion.

2. 📐 SCALE & PHYSICS
Character scale against the environment is mostly consistent.
Ship scale shows minor discrepancies between the aerial shots and the landed shots.
SCORE: 4/10
ISSUES:
1:43 — 🟡 MINOR — Tether physics lack tension; rope clips slightly near the anchor point.
2:20 — 🟡 MINOR — Ship appears slightly smaller in proportion to the astronaut compared to the opening flight sequence.

3. 🎥 CAMERA & CINEMATOGRAPHY
Camera moves are generally smooth and motivated. Depth of field is appropriate.
Hidden Cuts: Compilation mode without a plan file renders scene boundary checks unverifiable.
SCORE: 6/10
ISSUES:
UNVERIFIABLE — Scene boundaries cannot be validated against a spec document.

4. 💡 LIGHTING & COLOR
Lighting direction remains consistent relative to the terrain.
No severe AI bloom or impossible light sources detected. Shadow falloff is natural.
SCORE: 6/10
ISSUES: None notable.

5. 🌍 ENVIRONMENT & WORLD
The wavy rock formations and black band hold their structure well across different focal lengths.
Minimal texture swimming.
SCORE: 6/10
ISSUES:
1:10 — 🟡 MINOR — Slight swimming in the micro-textures of the red rock face in the background.

6. 🦎 CREATURE DESIGN & MOTION
SCORE: N/A (No creatures present).

7. 🔬 PARTICLE & MATERIAL PHYSICS
Severe failures in loose material interactions.
SCORE: 3/10
ISSUES:
0:24 — 🟠 MAJOR — Landing thrust kicks up debris in bizarre, solid, tentacle-like strings rather than a dispersed particle cloud.
2:02 — 🟠 MAJOR — Sand brushed from the wall falls artificially, lacking correct collision and gravity dynamics.

8. 🗣️ DIALOGUE & AUDIO
SCORE: N/A (No audio provided/analyzable in this run).

10. 🚫 NEGATIVE BIBLE
SCORE: 3/10
ISSUES:
3:00 — 🔴 BLOCKER — Burned-in text ("THE BANDED DEEP") appears on screen. Violates the strict no-text core rule.

11. 🏃 MOTION QUALITY
Character locomotion is functional but exhibits typical AI stiffness.
SCORE: 5/10
ISSUES:
0:35 — 🟡 MINOR — Walking gait feels slightly floaty; footfalls lack heavy physical impact with the ground.

🚩 FLAGS FOR DOCUMENT CHECK
Category 9 (Frame Anchor Fidelity): Unverifiable. Needs pipeline anchor images.
Cuts: 14+ visible cuts. Without a plan file, cannot verify if these match intended scene boundaries.
Text/Titles: Title card appended at the end. Assuming this is a compilation edit, check if a title card was explicitly requested (though it still violates general series rules).
