# 📋 HIZLI REFERANS — HER PROMPT'A EKLENECEK BLOK

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya ders
> içermez — tüm derslerden damıtılan **evrensel kopyala-yapıştır bloğunu** taşır.
> Ders metinleri kardeş dosyalarda, tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

Aşağıdaki blok, tüm derslerden çıkarılan direktifleri tek bir kopyala-yapıştır
bloğu olarak içerir. Her video prompt'unun sonuna eklenmelidir:

```
=== UNIVERSAL QUALITY DIRECTIVES (from Lessons Learned v8) ===

MEDIUM LOCK [LESSON 56]: State the physical medium and forbid the wrong one by
name. In a gas atmosphere: no water, no ocean, no bubbles, no scuba tank, no
regulator, no dive mask, no fins, no wetsuit, no coral, no fish, no submarine,
no buoyancy. Never write "dive suit", "diver", "swims", "underwater" or
"deep sea" — the model draws the dictionary meaning, not the metaphor.

EQUIPMENT FRAME LOCK [LESSON 57]: The suit and life-support configuration in
frame 1 is IDENTICAL in frame 300. Restate the full suit line at 0s, 3s, 6s
and 10s of the timeline — not only in the opening description. No tank, mask,
regulator or backpack appears mid-take; no visor opens, closes, tints or clears.

RECURRING ENTITY LOCK [LESSON 58]: Any location, structure, creature or tool
that appears in more than one scene carries a numeric identity card (colour,
size, texture) that is copied verbatim into every scene it appears in. No prop
is introduced for a single scene.

PARTICLE MEDIUM LOCK [LESSON 39]: Particles have individual mass and follow
discrete paths under the scene's stated gravity. They never swirl, curl, eddy,
billow or flow as a connected mass. No underwater motion, no fluid current, no
viscous drift. Vacuum = ballistic and never settling; thin atmosphere = slow
but certain settling; the World Bible's pressure decides which applies.

DIALOGUE TEXT LOCK [LESSON 40]: Spoken lines are heard only, never shown. No
subtitles, captions, closed captions, burned-in dialogue text or transcript at
any point during or after a line. Attach this to every scene that has dialogue.

DIFFUSION WITHOUT TEXTURE LOSS [LESSON 41]: In atmospheres, soft shadows and
ambient fill are CORRECT and must be preserved — bloom is diagnosed by loss of
TEXTURE, not by softness. Every surface keeps visible grain, weave and pores.
In vacuum this inverts: shadows are absolute black and there is no fill.

WEAR PATTERN LOCK [LESSON 42]: Dirt, dust staining and wear are placed by
location and fixed — they never shift, redistribute, regenerate or animate
between frames. State where the staining is AND where it is not.

CONTINUITY LOCK: SINGLE UNBROKEN CAMERA TAKE. No teleport, no jump-cut, no
reset, no angle change, no transitions. Every frame flows from the previous.

NO COMPOSITED TEXT [LESSON 34]: No text overlay, no title card, no end card,
no credits, no caption, no lower third, no logo, no watermark, no subtitles,
no burned-in text, no letters or numbers composited over the frame at any
point. The take ends on the held frame — no title appears, no text fades in.

LIP-SYNC DISCIPLINE [LESSON 35]: Dialogue only in medium or closer framing.
Every spoken line under 5 seconds. Single speaker, strict turn-taking, never
simultaneous. If a voice is off-screen (AI, radio, recorder), state it
explicitly: no character speaks on camera, no mouth in frame, no lip
movement required. If a character does speak on camera, lip movements match
the spoken words for the full line and the mouth is still before and after.

VACUUM PLUME [LESSON 36]: In vacuum, exhaust expands rapidly outward in a
straight, sharply defined cone and thins away. It does NOT billow, curl,
mushroom, roll or rise. No turbulence, no smoke plume, no backpressure, no
ground-effect cloud. (In thin atmospheres this rule inverts — dust spreads
slowly and SETTLES. The World Bible's pressure value decides which applies.)

EQUIPMENT STATE LOCK [LESSON 37]: Declare the STATE of every piece of gear
per scene, not just its design. Helmet worn/removed, harness on/off, gloves
on/off, dust-staining level — each stated as already true at 0s and
unchanged for the whole take. No equipment appearing or disappearing, no
helmet materializing, no gear state change mid-shot.

DAMAGE CONTAINMENT [LESSON 38]: State damage as a counted, bounded list and
explicitly state what remains INTACT. No excessive debris, no structural
disintegration, no fragmenting hull, no expanding debris field, no
continuous shedding — a damaged vehicle stays whole and holds its silhouette.

SINGLE CHARACTER: EXACTLY ONE human character in the scene. No duplicates,
no clones, no second person appearing. Only the described character exists.

CREATURE ANATOMY LOCK: Fixed rigid anatomy throughout. Locked silhouette.
Background creatures in shallow DOF.

CREATURE LOCOMOTION: Articulated limb motion for all creatures. Each leg
lifts, plants, pushes. Wings flap with joint articulation. NEVER slide.

FACE LOCK: Face maintains IDENTICAL bone structure, eye spacing, nose shape
throughout. No morphing, no feature drift.

ANTI-BLOOM: Sharp directional light with clear falloff. HIGH CONTRAST. Skin
retains pore texture. Visor reflections match environment.

REFLECTION ACCURACY: All reflections match source object in shape, scale,
color, and angle. No warped or invented reflections.

WEIGHT & CONTACT: Visible weight on every surface. No floating. Rigid
skeletal proportions. No jello, no rubber-banding.

GRAVITY VECTOR: Body responds to gravity correctly. On vertical surfaces,
body leans in with effort. Hair/equipment hangs downward.

COLLISION INTEGRITY: ALL objects obey rigid body collision. Nothing phases
through, clips through, or merges with any other solid object. Ship gear
rests ON surfaces. Creature limbs contact surfaces, not penetrate.

CONTACT INTEGRITY: Fingers/hands NEVER merge with surfaces. Clear boundary.
Head connected to neck/torso at all times.

VISOR PERSISTENCE: Visor ALWAYS VISIBLE regardless of head angle.

ENVIRONMENT STABILITY: Background elements STATIC unless explicitly moving.
No breathing, warping, morphing, topology changes, terrain melting.

DYNAMIC WATER: All water shows continuous micro-motion. NEVER frozen, static,
gel-like. Accurate wakes. Tsunami/waves show spray and turbulence.

DYNAMIC FIRE: All fire, flames, explosions show CONTINUOUS chaotic motion.
NEVER static, painted, or frozen. Debris falls with correct gravity.

VOLUMETRIC PARTICLES: Dust, smoke, exhaust = volumetric with real dispersion.
Never frozen, flat, static, or solid.

MOTION SPEED: Real-time natural speed unless slow-motion specified.

ACTION CONTINUITY: During physical actions (jumping, climbing, running),
background must remain spatially consistent. No environment teleportation,
no sudden background swaps mid-action.

ZERO-G MICRO-MOTION: Floating characters show continuous subtle body
rotation, limb drift, hair float, equipment drift. Never a rigid static
model dragged through space.

FLUID CONTACT: Fingers touching liquid maintain structural integrity.
Water deforms around contact, rebounds on withdrawal. Never merge,
never extra digits, never phase through.

REFLECTION SYNC: Reflections in visor/glass match character's actual
pose, expression, and movement in real time. Never autonomous.

NO AI TEXT: Displays show abstract patterns or blank glow only. NEVER text.

NO PROMPT BLEED [LESSON 45]: The frame never shows HUD overlays, lens data,
focal-length or f-stop text, camera metadata, name labels, character-name
captions, lower thirds or annotations. Write camera specs as a sentence, not
as a "CAMERA: 75mm, f/5.6" line, and keep bracketed [BIBLE] tags out of the
prompt body — the model draws them.

SUIT CONTINUITY: Equipment matches CHARACTER BIBLE EXACTLY across all scenes.
The full suit description is written out in THIS prompt — the words "her suit"
or "his gear" never appear without the complete description [LESSON 55].

ANTI-CUT NEGATIVE: No cuts, transitions, dissolves, fades, jump cuts,
montage, editing, multiple angles, scene changes, camera teleportation,
chase-cam, text overlay, title card, watermark, HUD overlay, lens data,
focal length text, camera metadata, name label, character name caption,
subtitle, lower third, annotation, bloom, glow filter,
airbrushed skin, plastic texture, Unreal Engine, video game aesthetic,
frozen particles, static exhaust, hand-surface merging, frozen water,
gel-like water, AI-generated text, face morphing, object phasing,
object clipping, creature sliding, warped reflections, melting terrain,
duplicate characters, static fire, painted explosions, frozen flames,
environment teleportation, rigid zero-g floating, finger-fluid merging,
autonomous reflections, water, ocean, bubbles, scuba gear, wetsuit, dive mask,
regulator, swim fins, coral reef, fish, submarine, equipment appearing
mid-shot, suit design change, helmet type change.
===
```

---
