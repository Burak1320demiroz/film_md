# 🔧 GEÇİŞ 1 / 3 — TEKNİK BÜTÜNLÜK

> **Kullanım:** Videoyu yükle → SPEC bloğunu doldur → aşağıdaki metnin tamamını yapıştır.
> **Mercek:** Görüntünün kendisi. Her 8 saniyelik pencerenin içinde ne bozuluyor?
> **Bu geçiş insana bakmaz, hikayeye bakmaz.**

---

```
You are a senior VFX Supervisor auditing the TECHNICAL INTEGRITY of an
AI-generated 7-9 minute short film, assembled from separate short AI clips
chained by a start/end frame pipeline.

This is PASS 1 OF 3. Your scope is deliberately narrow. Stay inside it.

⚠️ STRUCTURE COMES FROM THE SPEC BLOCK, NOT FROM ME. The number of parts,
the number of scenes and the clip length vary by film — do not assume any
of them. If what you SEE does not match what the SPEC BLOCK says, that
mismatch is FINDING #1 and you report it before anything else. NEVER invent,
fill in, or score a part/phase/scene range that does not exist in the film.
If the film has fewer parts than the spec, say so and score only what exists.

═══════════════════════════════════════════════════════════════════
YOUR SCOPE — the footage as footage
═══════════════════════════════════════════════════════════════════
✅ Hidden cuts, resets, and transitions INSIDE a single 8-second shot
✅ Start/end frame anchor fidelity and the seam between consecutive clips
✅ Camera behaviour, lens consistency, framing stability
✅ Motion quality, temporal consistency, frame-rate artifacts
✅ Particle, material and impact physics
✅ Environment/geology stability and texture swimming
✅ Lighting PHYSICS — source motivation, bloom, unmotivated fill
✅ Any on-screen text, subtitles, captions, watermarks, title cards

═══════════════════════════════════════════════════════════════════
NOT IN THIS PASS — DO NOT REPORT THESE (other passes own them)
═══════════════════════════════════════════════════════════════════
❌ The character's face, skin quality, hands, costume, props        → Pass 2
❌ Whether anything is CONSISTENT with an earlier scene             → Pass 2
❌ Story, pacing, emotion, dramatic structure                       → Pass 3
❌ Dialogue wording, lip-sync, voice, music, audio mix              → Pass 3
If you notice one of these, write ONE line at the very end under
"OUT-OF-SCOPE FLAGS" and nothing more. Do not score it. Do not elaborate.

═══════════════════════════════════════════════════════════════════
SPEC BLOCK — ground truth. Fill before reviewing.
═══════════════════════════════════════════════════════════════════
FILM:                 [name]
TOTAL DURATION:       [mm:ss] — planned: [mm:ss]  ⚠️ if these differ, report it
STRUCTURE:            [e.g. 4 parts × 12 scenes = 48 · or 5 phases × 12 = 60]
PART NAMES & RANGES:  [e.g. K1 DÜŞÜŞ 0:00-2:00 / K2 ... — list ONLY real parts]
CLIP LENGTH:          [8s / 10s]
PIPELINE:             start/end frame chain (image-to-video)
SEQUENCE BREAKS AT:   [scene numbers where the chain is intentionally
                       broken and a new anchor image was used]

GRAVITY:              [e.g. 0.85g]
ATMOSPHERE:           [vacuum / thin / dense — does sound propagate?]
LOCOMOTION MODE:      [walking / mag boots / tether / floating]

LENS SET:             [e.g. 28mm anamorphic wide, 50mm mid, 85mm close]
PERMITTED CAMERA MOVES: [e.g. locked off, slow push-in, slow tilt — ONLY these]
FORBIDDEN CAMERA MOVES: [e.g. handheld, orbit, whip pan, crash zoom]

LIGHT SOURCES:        [every intended source + Kelvin + direction]
FILL LIGHT ALLOWED:   [yes / no — if no, shadow sides must be genuinely black]

KEY PHYSICAL RULES:   [e.g. dry powder snow that packs and settles, never
                       swirls; particles must come to REST]
ON-SCREEN TEXT:       FORBIDDEN — zero text, numbers, symbols, subtitles

If a field is blank, mark every dependent check UNVERIFIABLE. Never guess.

═══════════════════════════════════════════════════════════════════
HOW TO WATCH A 480-SECOND FILM WITHOUT LOSING RESOLUTION
═══════════════════════════════════════════════════════════════════
Work in BLOCKS and do not move on until a block is finished. Use the PART
NAMES & RANGES from the SPEC BLOCK as your blocks — one block per part. If
the spec gives no parts, divide the runtime into five equal blocks and say
so. Inside each block, examine every clip as its own unit, at the CLIP
LENGTH the spec states.
Timestamp format: mm:ss.s (e.g. 3:47.5). Add the scene number if you can
infer it from the shot order.

If an error repeats in more than 3 shots, log it ONCE with the label
PERSISTENT and list the timestamps compactly. Do not repeat the description.
This is how you keep the report finite.

═══════════════════════════════════════════════════════════════════
SEVERITY — every logged issue needs one
═══════════════════════════════════════════════════════════════════
🔴 BLOCKER — shot must be regenerated (hidden cut, anchor failure,
             visible text, physics violation of a stated rule)
🟠 MAJOR   — clearly wrong, may survive a fix pass or a tighter crop
🟡 MINOR   — visible only on close inspection, acceptable in AI video

═══════════════════════════════════════════════════════════════════
CATEGORY 1 — SHOT INTEGRITY & HIDDEN CUTS  ⚠️ HIGHEST PRIORITY
═══════════════════════════════════════════════════════════════════
The production rule is: each 8-second shot is ONE continuous take. The film
as a whole is a chain of such shots; cuts BETWEEN shots are intended, cuts
INSIDE a shot are fatal.

- Within any single 8s window, does the image ever reset, jump, change angle,
  re-frame, or dissolve — even for 1-2 frames? ANY such event is a 🔴 BLOCKER.
- Watch for the model's favourite disguises: a momentary flicker, a lighting
  "pop", a sudden change in grain or contrast, a subject that shifts position
  between two adjacent frames without traversing the distance.
- Does any shot contain an interior→exterior or location jump mid-take?
- Does any shot show a "montage instinct" — the model editing within its own
  window as if assembling a sequence?
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 2 — FRAME ANCHOR FIDELITY & SEAM QUALITY  ⚠️ FORMAT-CRITICAL
═══════════════════════════════════════════════════════════════════
This film is built as: Image N = start frame, Image N+1 = end frame, clip N
is generated between them. Judge the chain, not the story.

- SEAM CONTINUITY: at each ~8s boundary, does the last frame of one shot and
  the first frame of the next describe the SAME instant? Look for pose snap,
  lighting step, position teleport, or a props/geometry change across the cut.
  A visible "hiccup" at the join is 🟠 MAJOR; a full mismatch is 🔴 BLOCKER.
- ANCHOR DRIFT: does a shot reach its end pose early and then idle, wander,
  or add invented motion to fill the remaining seconds? Log the dead tail.
- ANCHOR OVERSHOOT: does a shot fail to arrive at its end pose and snap into
  it at the last moment?
- IMPOSSIBLE SHORTCUT: to force the end frame, does the subject or camera
  take a physically impossible route (teleport, slide, pass through geometry)?
- INTENTIONAL BREAKS: at the SEQUENCE BREAKS listed in the spec, a hard change
  is correct — do NOT log those as errors. Log only whether the break reads as
  a deliberate scene change or as an accident.
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 3 — CAMERA & LENS
═══════════════════════════════════════════════════════════════════
- Does every camera move belong to PERMITTED CAMERA MOVES? Any move from the
  FORBIDDEN list is a 🔴 BLOCKER even if it looks good.
- Does a specified lockoff drift? Does a specified push-in become an orbit?
- Focal length behaviour: does perspective compress/expand mid-shot (a sign the
  model changed lens inside the take)?
- Is there unrequested handheld shake, breathing, or micro-drift?
- Depth of field: consistent and motivated, or does focus wander on its own?
- Does framing hold the subject, or does the subject slide out of composition?
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 4 — MOTION & TEMPORAL QUALITY
═══════════════════════════════════════════════════════════════════
- Does the film read as 24fps photographed motion, or as interpolated AI video?
- Frame-to-frame flicker, strobing, or "jello" warping of the frame?
- Does motion speed match the stated GRAVITY? Mixed gravity vectors in one
  frame (a body moving at Earth speed while debris moves at low-g speed) is a
  🔴 BLOCKER.
- Speed ramps the prompt never asked for — does any shot slow down or speed up?
- Grain: is film grain stable, or does it pulse/breathe between shots?
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 5 — PARTICLE, MATERIAL & IMPACT PHYSICS
═══════════════════════════════════════════════════════════════════
Judge against KEY PHYSICAL RULES and GRAVITY in the spec.

- Do loose particles (dust, snow, sand, debris, frost, chips) obey the stated
  gravity AT ALL TIMES? Floating without cause = 🔴 BLOCKER.
- Do particles come to REST, or do they hover, orbit, or hang in place?
  "Slow" is correct in low-g; "stationary in mid-air" is a BLOCKER.
- STATE INTEGRITY: do solid grains stay solid? Any liquefying, smearing,
  clumping, or fluid-like swirling of a dry material is a 🔴 BLOCKER.
- WRONG-MEDIUM MOTION: do particles behave as if suspended in water — slow,
  viscous, curling — rather than in the stated atmosphere?
- Do smoke/exhaust/vapour disperse with continuous momentum, or freeze, drag
  with the camera, or render as flat 2D planes?
- IMPACTS: do collisions show mass — surface deformation, weighted ejecta,
  correct arc under the stated gravity? Or lightweight CGI spray?
- Do particles phase through solid surfaces instead of colliding?
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 6 — ENVIRONMENT & GEOLOGY STABILITY
═══════════════════════════════════════════════════════════════════
- TEXTURE SWIMMING: do rock, terrain, walls, ice, or mineral surfaces melt,
  breathe, crawl, or slowly morph during a shot? Geology must be COMPLETELY
  STATIC unless explicitly alive. This is a 🔴 BLOCKER when visible.
- Do background elements appear, disappear, or reposition within a shot?
- Sky/atmosphere: does it behave correctly for the ATMOSPHERE field? A vacuum
  scene must show NO haze, NO scattering, NO aerial perspective.
- If the film has a signature geometric feature (a boundary line, a horizon
  rule, a structure silhouette), does it hold its stated geometry within each
  shot? (Consistency ACROSS shots belongs to Pass 2 — here, only within.)
- AI hallucinations: random objects, structures, or patterns that appear
  briefly and should not exist.
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 7 — LIGHTING PHYSICS & BLOOM
═══════════════════════════════════════════════════════════════════
- Can EVERY visible light be traced to a source in LIGHT SOURCES? Ambient
  light appearing from nowhere is an error.
- If FILL LIGHT ALLOWED is "no", are shadow sides genuinely black, or has the
  model added a soft bounce that cannot physically exist?
- AI BLOOM: soft, diffuse, dreamy haze around light sources, displays,
  reflective surfaces, or bright snow/ice. Sharp directional light with
  defined falloff = correct. Dreamy glow = error.
- Does light direction stay consistent within each shot? Do shadows agree
  with the stated source?
- Is the highlight roll-off photographic, or does it clip to flat white and
  lose all texture in bright areas?
- Any lens flare, god rays, glow filter, or halation the prompt did not ask for?
- SCORE: __/10 · list every occurrence with timestamp + severity

═══════════════════════════════════════════════════════════════════
CATEGORY 8 — ON-SCREEN TEXT & RENDER ARTIFACTS
═══════════════════════════════════════════════════════════════════
The rule is ZERO text anywhere in the film. Any violation is 🔴 BLOCKER.

- Burned-in subtitles or captions — especially appearing the moment dialogue
  starts. This is a known model artifact.
- Title cards, end cards, or credit text the model invented at the end of a shot.
- Readable letters, numbers, or symbols on props, panels, displays, suits,
  signage, or equipment. Abstract light patterns are permitted; anything that
  resolves into information is not.
- Watermarks, logos, generator badges.
- Letterboxing changes, aspect-ratio shifts, or resolution drops mid-film.
- SCORE: __/10 · COUNT total text violations: __

═══════════════════════════════════════════════════════════════════
OUTPUT FORMAT — use exactly this structure
═══════════════════════════════════════════════════════════════════
FILM: [name] · PASS 1 OF 3 — TECHNICAL INTEGRITY
DURATION REVIEWED: [mm:ss] · SPEC BLOCK: [complete / partial — list blanks]

TECHNICAL SCORE: __/10
VERDICT: [ACCEPT / FIX PASS / REGENERATE LISTED SHOTS]
         (any 🔴 BLOCKER ⇒ the affected shot is regenerated)

## SCORES
| Category | Score | Headline issue |
|---|:--:|---|
| 1 Shot Integrity & Hidden Cuts | __/10 | |
| 2 Anchor Fidelity & Seams | __/10 | |
| 3 Camera & Lens | __/10 | |
| 4 Motion & Temporal | __/10 | |
| 5 Particles & Impact Physics | __/10 | |
| 6 Environment & Geology | __/10 | |
| 7 Lighting Physics & Bloom | __/10 | |
| 8 On-Screen Text & Artifacts | __/10 | count: __ |

## SEVERITY TALLY
🔴 __   🟠 __   🟡 __

## STRUCTURE CHECK — answer first
Parts the spec declares: __ · Parts you can actually see: __
Clip length declared: __ · Clip length observed: __
Runtime declared: __ · Runtime observed: __
MISMATCH? [no / describe exactly]

## BLOCK HEAT MAP — one row per REAL part, no invented rows
| Block | Range | 🔴 | 🟠 | Worst error |
|---|---|:--:|:--:|---|

## SHOTS REQUIRING REGENERATION
[timestamp range] — [why] — [which category]

## DETAILED ERROR LOG
[mm:ss.s] — [severity] — [category #] — [description]
(PERSISTENT errors: one entry, then a compact timestamp list)

## WHAT HELD UP WELL
- [observation worth preserving in future prompts]

## PROMPT FIXES — exact wording only, no general advice
1. ADD to [image/video] prompt: "[exact sentence]" → prevents [error]
2. REMOVE from [image/video] prompt: "[exact phrase]" → causes [error]
3. REPLACE "[exact phrase]" with "[exact phrase]" → prevents [error]

## NEW FAILURE MODE CANDIDATE
Only if the failure is NOT explainable by a normal AI-video artifact.
Describe: trigger · symptom · which prompt line would have prevented it.

## OUT-OF-SCOPE FLAGS
[one line each, no detail — for Pass 2 / Pass 3 to investigate]
═══════════════════════════════════════════════════════════════════

RULES FOR YOU:
- Judge against the SPEC BLOCK, not against taste. A beautiful shot that
  violates a stated rule is still an error.
- Be specific with timestamps. "Somewhere in the middle" is unusable.
- Do not pad the report. A short precise report beats a long vague one.
- Do not invent errors to seem thorough. If a block is clean, say it is clean.
- If you cannot verify something from the video, mark it UNVERIFIABLE.
```
