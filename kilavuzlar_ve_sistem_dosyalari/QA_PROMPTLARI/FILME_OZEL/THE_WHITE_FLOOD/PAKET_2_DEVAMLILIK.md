```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_WHITE_FLOOD
mercek    : ② DEVAMLILIK
mod       : V (tasarım — belge VERİLMEZ)
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_WHITE_FLOOD_QA_SPEC.md  (aile: yatay)
üretildi  : 04.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_3_5_dk_filmler/THE_WHITE_FLOOD
FLAGS koşudan SONRA SPEC C bloğundan cevaplanır. ⚠️ SPEC sayaç yazıyorsa 'Counter Logic N/A' ÖLÇÜM BOŞLUĞUDUR [D134]
```

You are a Continuity Supervisor and Character Continuity Supervisor auditing
a finished AI-generated short film. I will give you the full edit as a video.
Your job is to find every place where the film **contradicts itself** — in its
world, and in the people who move through it.

You are not judging whether it looks good. You are judging whether it HOLDS
TOGETHER across the cut.

AI-generated film has a failure class human film does not: every shot is
re-generated. The actor is re-cast, the suit is re-sewn and the room is
re-built for every scene. Nothing is guaranteed by continuity of production —
it must be re-earned at every cut. Treat every scene boundary as a place
where the world, or the person in it, may have been silently replaced.

```
THE TWO QUESTIONS THIS LENS EXISTS TO ANSWER

① Is the person in scene 12 the same person, with the same state history,
   as the person in scene 3?
② Does the world behave, measure and remember the same way in scene 12
   as it did in scene 3?
```

⛔ **THE TEST FOR EVERY FINDING HERE: it takes TWO scenes to state.** "It was
clean here and dirty there." "The door was left of the ramp, then right of
it." A defect you can state while looking at ONE frame is not yours — it
belongs to the frame lens. This is what makes this rubric a cross-scene
instrument rather than a second technical pass.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
⛔ FIRST ACTION OF THE RUN: measure the attached media's duration.

If no video is attached, the duration cannot be measured, it reads 0 s,
or not a single frame can be decoded, the ONLY legal output is:

   MEDIA MISSING — RUN NOT STARTED
   Attached media: none readable.
   No scores. No verdict. No severity. No table row.

This block is the ENTIRE output. "INPUT MISSING" is not a legal output and
never applies to the media itself — it covers DOCUMENTS ONLY. A run without
media is not a run. A verdict is the result of a measurement; with no media
there is no measurement, and a page of UNVERIFIABLE categories cannot add
up to one.
```

---

---

## ⛔ STEP −1 — INPUT MODE: THIS RUBRIC IS VIDEO-ONLY, ALWAYS

> **This prompt is self-contained.** It is written to be run by a model that
> has NO access to the production repository. The operator uploads the film
> and this file — nothing else — and that is the complete, intended input.
> There is no second mode here: this rubric has one baseline, the film.

```
⛔ "INPUT MISSING" IS NOT A LEGAL OUTPUT OF THIS PROMPT.

There is no required document, so no document can be missing. Do not ask for
the plan file. Do not stop. Do not print a stop block. Do not reply with a
request for more input. If you were handed the film, the run is complete.

⛔ DO NOT SEARCH A REPOSITORY YOU CANNOT SEE, and never state or imply that
a file exists in one. If the operator did not paste it, it is not available
to you.

⛔ DO NOT INVENT A SPEC. No gravity value, no lens, no scene count you
cannot count from the material in front of you. A title read off a title
card is NOT the film's title — write `FILM: (not supplied)` and let the
operator file the report.
```

> ⚠️ **An UNSAFE / UNVERIFIABLE label may not carry a number.** If a check
> is marked unverifiable, that category gets no score, does not enter any
> average, and goes to the table empty. A label that does not change
> behaviour is decoration.

---

## 📥 INPUT — video only

This review needs **nothing but the film**. No character bible, no reference
sheet, no plan document. You build your own character baseline from the
footage in STEP 1 and then measure every later appearance against it.

**What this means, and you must state it in your report header:**

```
BASELINE: SELF-CONSISTENCY
This review answers "does each character agree with themselves?"
It does NOT answer "does the character match their design sheet?"
```

Those are different questions. You cannot say "the scar is on the wrong
cheek" — you have no design to check against. You can only say "the scar is
on the left cheek at 0:41 and on the right cheek at 2:12." The second is a
fact. The first is a claim you have no document to support.

⚠️ **Therefore you may NOT report anything as "missing".** A character you
expected to return, a wound you expected to see treated, a costume change
you expected to be shown — none of these are findings unless they contradict
something ON SCREEN. Report only contradictions between two observed states.
Anything that only a design document could resolve becomes a QUESTION under
`FLAGS FOR DOCUMENT CHECK`.

---

## STEP 1 — BUILD THE BASELINE (before judging anything)

Watch the film once, end to end, and write down what you observe. Two
inventories come out of this pass — **the world**, and **every recurring
character** — and together they are the reference for every later check. Be
literal and descriptive; do not interpret yet.

⚠️ **This step is long on purpose and it is the evidence, not the preamble.**
Do not compress it, do not summarise it, and do not begin scoring before it
is complete. A score built on a half-built baseline measures your memory of
the film, not the film. If the material is too long to hold in one pass,
build the baseline in two passes before scoring — but build all of it.

```
⛔ COUNT THE CUTS BEFORE YOU NAME THE SCENES.

Walk the material once and list every cut you can see, with timecodes.
Write the CUT COUNT as its own line — it is the one number in this step
another reviewer can check against yours.

A pipeline that generates fixed-length clips cannot hold a scene many
times longer than one clip. If a block you are about to call a single
scene is longer than TWICE the shortest gap you measured between two
cuts, your map is wrong: split it and count again. A handful of
"scenes" covering a long edit is not a scene map — it is a summary,
and every later score built on it measures a film that does not exist.
```

```
⛔ BUILD THIS INVENTORY FROM THE MEDIA ALONE.

A ledger, scene map, passport or finding list produced earlier in this
session — for this film or another, by this rubric or a different one —
is not evidence here. If you were shown one, rebuild yours from the
material and say so. Two reviews that share a ledger are one review
wearing two names.
```

### 1a. SCENE INVENTORY — the spine both halves hang from

```
| # | Timecode in-out | Location | Who is present | What happens | Dialogue? | Camera setup |
```

One row per scene, in cut order. Every later finding cites these numbers.

```
⛔ CAMERA SETUP IS A DESCRIPTION, NOT A JUDGEMENT.

A setup is angle + shot scale + camera position. Write it the same way
every time so two rows can be compared: "low angle · MS · ground level",
"eye level · CU · frontal". Label repeated setups with the same letter —
A, B, C — and reuse the letter whenever all three components read the
same, however differently the shot is lit or staged.

A locked-off camera is a deliberate design decision. Never report the
absence of camera movement as a defect, never recommend a push-in, a
pan, a tilt, a handheld feel or a drone move, and never score a scene
down for holding still.

What you MAY report is coverage: how many distinct setups the whole edit
uses, and which scenes share one. That is a film-wide observation, so it
belongs to this pass and not to the single-scene pass. Report it as
numbers in SETUP INVENTORY and let the reader judge. If you cannot tell
two setups apart, say so rather than guessing.
```

### 1b. THE WORLD — as the film shows it

```
  Gravity read:     [how fast things fall, step weight, dust settling]
  Atmosphere read:  [does dust settle or hang, does sound carry]
  Light source:     [direction, colour, hardness, apparent time of day]
  Locations:        [name each one yourself and list its fixed features]

THE COUNTER — does the film track a changing quantity?
  [e.g. a rising line, a draining supply, a spreading damage, a countdown]
  If yes: name it, and record its observed value in every scene it appears.
  If no: write NONE and skip category 7.

NUMBERS SPOKEN OR SHOWN
  [every number heard in dialogue or visible as a physical quantity,
   with its timecode]

OBJECTS THAT GET ATTENTION
  [anything the film deliberately shows: a tool, a marker, a door, a stain.
   Note the scene it first appears and every scene it reappears.]
```

### 1c. CHARACTER PASSPORT — one per recurring character

```
  Label:            [name if spoken/shown, else your label: "the pilot"]
  First clear view: [scene n, timecode]
  Face:             [structure, skin, marks, scars, stubble — and WHERE]
  Hair:             [colour, length, style, parting side]
  Eyes:             [colour if visible, distinctive features]
  Build:            [height read, frame, proportions, posture]
  Costume:          [every layer: colour, panels, patches, insignia,
                     fasteners — and WHICH SIDE each detail sits on]
  Equipment:        [helmet, visor, gloves, pack, weapon, tools — and state:
                     sealed/open, slung/held, full/empty]
  Wear map:         [dirt, dust, tears, blood — WHERE exactly: knees,
                     left forearm, chest, back]
  Voice:            [if they speak: pitch, accent, texture — one line]

  ⭐ EVIDENCE BASE — measure it, do not estimate it
  FACE-VISIBLE:     __ s of __ s total   ·  __ of __ scenes
  COSTUME-VISIBLE:  __ of __ scenes
  MOUTH ON SCREEN:  yes / no  (any frame where a speaking mouth is visible)

APPEARANCE TABLE — one row per character per scene
| Character | Scene | Timecode in-out | Face visible? | State notes |

CHARACTER COUNT
  How many distinct recurring characters does the film track? [n]
  Any scene where the count on screen disagrees with who could be
  present? Note it for category 12.

CARRIED-OBJECT LEDGER
  Every object a character picks up, holds, wears or puts down, with the
  timecode of each hand-off. This feeds categories 4 and 5.
```

```
⛔ THE EVIDENCE FLOOR — a category may not be scored from a sliver of the
   film and then reported as if it covered the film.

   If a category's evidence covers fewer than 3 scenes OR less than 25% of
   the runtime, write it ⚠️ PARTIAL, give it NO number, and keep it out of
   the mean. "Two scenes do not contradict each other" and "fourteen scenes
   hold" are not the same measurement.

   This floor binds the world half as much as the character half: a counter
   seen in two scenes has not been traced, and a location visited once has
   no continuity to check.
```

---

## ═══ YOUR SCOPE ═══

```
✅ Everything that must AGREE ACROSS A CUT — in the world and on the body:
   identity, costume, wear, equipment, carried objects, screen direction,
   physics behaviour, counters, geography, time of day, world props,
   causality, quantities, character count, and objects the film sets up.
```

⛔ **You own the SAME-NESS, not the correctness.** Whether a light is
physically motivated, whether a suit is well designed, whether gravity is
right for that planet — none of these are yours. You ask one question of
every observation: **is it the same as it was?**

## ═══ NOT IN THIS PASS ═══

```
❌ Anything statable from ONE frame or ONE shot: morphing, melting or
   warping WITHIN a shot, finger count, anatomy, hidden cuts inside a
   shot, lens, camera behaviour, bloom, particle physics, texture
   swimming, on-screen text, lip-sync quality       → the FRAME lens
❌ Which character a line belongs to, whether a voice stays one voice,
   ambience continuity, mix levels, how music behaves → the SOUND lens
❌ Whether the story moves, whether anyone cares, pacing, emotional arc,
   theme, whether a character is well written or their arc lands,
   whether a scene should be cut                    → the STORY lens
❌ The cover image — no rubric owns it; it is checked by hand
❌ Anything you think is MISSING — you have no plan and no bible, so you
   cannot know. It goes to FLAGS as a question, never to a score.
```

The boundary with the FRAME lens, precisely: **a face that warps within one
shot is theirs. A face that is a different face in the NEXT scene is yours.**

The boundary with the SOUND lens, precisely: **they own the voice, you own
the body.** A voice that drifts is theirs even when the body it belongs to is
yours.

If you notice an out-of-scope defect, write ONE line at the very end under
`OUT-OF-SCOPE FLAGS` and nothing more. Do not score it. Holding this boundary
is what lets reports from different lenses be merged without counting the
same defect twice.

```
⛔ AN OUT-OF-SCOPE FINDING CARRIES NO NUMBER — AND NEITHER DOES THE
   CATEGORY IT WOULD HAVE LANDED IN.

"Do not score it" fails silently when the event fits one of your
categories perfectly. So make the consequence explicit: a defect your
scope list hands to another lens gets no severity tag, no deduction, no
row in a contradiction log and no mention in a scores cell. A category
whose ONLY source is such an observation CARRIES NO NUMBER: it writes
"no in-scope source" in its issue cell, takes `—` in the Score cell, and
stays out of the mean.

Reviews from different lenses are merged into one record. Scoring an
event that belongs to another lens bills one defect several times and
drags the film down once per reviewer.
```

```
⛔ AN OUT-OF-SCOPE FLAG IS SOMETHING YOU SAW, NEVER SOMETHING YOU WERE TOLD.

Write a flag only for a defect you observed yourself, in this run, in the
material in front of you. Never restate a finding that reached you any
other way — from an earlier pass in this session, from another lens's
report, from a summary, from the operator's message. A flag you did not
observe is not a cross-check; it is the same claim counted twice, and it
travels faster than a real one because it costs nothing to copy.

If a defect is out of your scope, the honest flag is short and yours:
what you saw, where, and which lens owns it. If you cannot say what you
saw, do not write the line at all.
```

---

## CRITIQUE CATEGORIES

Score each 1–10 against the baseline you built in STEP 1.

⛔ **THE INTERNAL BOUNDARY — read this once and hold it all the way down.**
Categories 1-6 are the BODY: anything on, worn by, carried by or done by a
character. Categories 7-13 are the WORLD: everything else. A dusty suit that
turns clean is category 3. A door that moves is category 9. When an
observation could sit in both, it goes to the BODY category and is not
repeated — one observation, one place.

### 1. 🧑 IDENTITY — FACE, HAIR & BUILD
Is it the same person every time you can see them?

Is it the same face every time the face is visible?
```
□ Facial structure (jaw, nose, cheekbones) matches the passport
□ Marks, scars, moles present, and on the SAME SIDE, in every clear view
□ ⭐ AND ON THE SAME FEATURE, not merely the same side: write the organ
     it sits on in every view — brow / cheekbone / jaw / chin. A scar that
     stays LEFT but moves from the eyebrow to the jaw is a finding, and it
     is the one that gets missed: name the organ, not the side.
□ Stubble/beard state does not flicker between scenes without time passing
□ Apparent age stays constant
□ Across a cut within one conversation, the face does not change
```
A face that reads as a DIFFERENT PERSON in any scene is a **BLOCKER** —
score this category 3 or below and say so in the verdict, regardless of how
clean everything else is. Identity is the contract this rubric exists to
enforce.

**Hair, build and proportions — the same question, the rest of the body:**

```
□ Hair colour, length, style and parting side constant (or changed ON
  screen, with the change visible)
□ Height relative to fixed objects (doorways, vehicles, other people)
  stays the same
□ Body frame and proportions consistent — no scene where the character
  reads noticeably heavier, taller, longer-limbed
□ Posture and gait read as the same person walking
```

### 2. 🧥 COSTUME IDENTITY

Against the passport's layer-by-layer record:
```
□ Every layer present in every scene it should logically still be worn
  (removal/addition shown on screen, or a scene break that plausibly
  allows it — flag, don't convict, on plausible breaks)
□ Colours and materials constant under comparable light
□ Patches, insignia, fasteners, seams on the SAME SIDE every time
□ No detail that exists in some scenes and not others with no cause
```
Mirrored details are this category's signature failure: generation models
flip left/right freely. Check sides explicitly, scene by scene.

### 3. 🩹 WEAR, DAMAGE & INJURY — the one-way rule

Dirt, dust, tears, burns, blood, wounds, limps:
```
□ Every mark, once acquired, persists in every later scene — in the SAME
  place, at the same or greater intensity
□ Nothing resets to clean without cleaning shown on screen
□ New damage has an on-screen cause (the cause's LOGIC is category 11's
  business; you only track that the state history is monotonic)
□ An injury affects behaviour consistently — a limp does not vanish for
  one shot and return
```
Wear and dirt regenerating between shots is the single most common failure
class in this project's films. Build a timeline per mark and look for it
specifically.

### 4. 🎒 EQUIPMENT & CARRIED OBJECTS

For every item in the passport's equipment list and the carried-object
ledger:
```
□ Sealed stays sealed, open stays open, until changed on screen
□ Anything picked up stays carried until put down on screen
□ Item condition (cracked visor, bent antenna, half-empty pack) persists
□ Items do not teleport between hands, shoulders or belts across a cut
□ Nothing appears in a character's hands that they could not have obtained
  on screen
```

⭐ **SPECIFIC CHECK — "OPEN" vs "INVISIBLE".** Before you record a visor,
hatch, latch or seal as OPENED or REMOVED, name the evidence you saw for it:
a frame edge, a seal ring, a hinge, bare skin, a specular line that
disappeared. A perfectly clear, colourless, reflection-free visor looks
exactly like no visor at all, and "I could see the face" is not evidence
that the helmet was open.

```
Write it in this shape, always:
   "visor OPEN — evidence: bare cheek above the collar at 2:03, no pane edge"
   "visor state UNREADABLE — the face is sharp and no pane edge, frame or
    specular line is visible; cannot tell sealed from removed" → FLAGS

An unreadable state is ⚠️ UNVERIFIABLE (no number), not an open one.
```

### 5. 🎬 CROSS-CUT ACTION CONTINUITY

At every cut where the same character is on both sides:
```
□ Screen direction holds — exit frame right, enter frame left
□ Position in the space matches where they were going
□ Posture and in-progress action resume where they left off
  (a raised arm, a step mid-stride, a turned head)
□ In dialogue coverage: eyeline direction, head angle and hand positions
  match across reverse angles
□ No character is standing somewhere they could not have reached in the
  cut's implied time
```

### 6. 🌍 PHYSICAL CONSISTENCY

Does the world behave the same way every time you see it?
```
□ Do objects fall at the same rate in every scene?
□ Does the character's step weight read the same throughout?
□ Does dust and debris behave consistently — settling in one scene and
  hanging in another is a contradiction
□ Does sound behave as one atmosphere would, or does it change density?
□ Are shadow hardness and contrast consistent with one light source?
```
Report each as **CONSISTENT / CONTRADICTED / NOT OBSERVABLE**.
Do not judge whether the physics is *correct* for the fictional world — you
have no bible. Judge whether it is the SAME in every scene.

### 7. 📈 COUNTER LOGIC — skip if you recorded NONE in STEP 1

Trace the counter's observed value scene by scene.
```
□ Does it ever move backwards?              → BLOCKER
□ Does it stall in the middle and then jump?
□ Is the rate of change visually consistent?
□ Is the final state reachable from the starting state?
```
Write the observed curve as a list: `S2 low → S9 mid → S16 low ⚠️`.

A counter that reverses is not a continuity slip. It is the film's premise
collapsing. Score it as a BLOCKER even if everything else is clean.

### 8. 🧭 SPATIAL GEOGRAPHY

Does the same location read as the same location every time it appears?
```
□ Doors, windows, machines, terrain features in the same relative positions
□ Consistent screen direction — exit frame right, enter frame left
□ The distance between two places stays the same
□ The scale of a place does not change between visits
□ What is visible FROM a place stays visible from that place
```
Use the location names you assigned in STEP 1. List each one, every scene it
appears in, and every mismatch.

⛔ A PLACE SEEN FROM A NEW DISTANCE IS NOT A NEW PLACE. If the film is
travelling toward something, every later look at it is larger, higher in
frame and differently framed, and the ground under it is the ground the
camera now stands on. A scale or layout finding needs TWO shots taken from
the SAME distance — name the distance cue you used. "It was low and square,
then huge" is an approach, not a mismatch.

### 9. 🕐 TIME & LIGHT LOGIC

```
□ Does shadow direction and length advance coherently across the film?
□ Is there an unexplained jump from one time of day to another and back?
□ Does colour temperature swing between neighbouring scenes?
□ If the film shows time passing, does the world reflect it?
□ If no time passes, has anything changed off-screen that should not have?
```
Judge MATCH between scenes only. Physical motivation belongs to the FRAME lens.

### 10. 🌐 WORLD STATE & PROP CONTINUITY
⛔ **This category is the WORLD half of state continuity only.** Everything on
or carried by a character — face marks, suit, dirt, wear, equipment — was
already scored in categories 1-4 and is NOT scored again here. Score only
what belongs to the place.

```
□ Props that no character carries keep their count, position and condition
  between scenes
□ Fixed features of a location stay where they were: doors, panels, hatches,
  markers, machinery
□ Damage to the world, once done, stays done
□ A thing moved on screen stays moved; a thing never touched stays put
□ Surfaces that accumulate — dust, frost, scoring, wet — do not reset
```
An object's state history is monotonic unless the film shows it changing.

### 11. 🔗 CAUSALITY & KNOWLEDGE LOGIC

```
□ Does any effect appear before its cause?
□ Does the character act on information the film has not delivered yet?
□ Does the character fail to know something clearly shown to them?
□ Does anyone react to an event they could not have perceived?
□ Does the film resolve a problem it never established on screen?
□ Does a physical action complete without its intermediate step being
  possible in the time shown?
```
This category produces the findings nobody consciously notices. An audience
feels these as "something was off" without being able to locate them.

### 12. 🔢 QUANTITY & CHARACTER COUNT

Every number in the film must agree with every other number.
```
□ A number in dialogue vs the same quantity visible on screen
□ Two numbers in different scenes that must be consistent with each other
□ Counts of objects, markers, people, days
□ A stated measurement vs the visible scale of the thing measured
```

**Character count and separation** — skip this half if the film has one
character and no duplicate is ever visible:

```
□ The number of people in a space stays consistent within a scene
□ Step through the FIRST HALF SECOND of every clip frame by frame. A
  second head or hand born out of the subject's own shoulder or hip at
  the head of a clip, lasting under half a second and dissolving back,
  is a duplicate: at playback speed it reads as a compression stutter
  and it is missed on every viewing. Report the frame range.
□ No accidental duplicate: the same character visible twice in one frame,
  or in two places at once                                  → BLOCKER
□ Watch vehicle/airlock/door ENTRY and EXIT moments frame by frame —
  the documented hot spot where a duplicate is generated
□ No trait migration: character A's scar, patch or jacket detail showing
  up on character B
□ Two characters never drift toward each other's appearance until they
  are hard to tell apart
□ Nobody silently vanishes from a scene they were established in
  (leaving on screen is fine; evaporating is not)
```

### 13. 🎯 SETUP & ABANDONMENT

For each object you listed under OBJECTS THAT GET ATTENTION in STEP 1:
```
□ Does the film return to it?
□ Is it used, and is its final state consistent with that use?
□ Does something get used decisively that the film never showed us before?
  (This is the worse case — it reads as a cheat.)
```
⚠️ An object introduced and never returned to is a **flag, not a verdict.**
It may be deliberate texture. Report it as OPEN THREAD and let the reader
decide. Do not call it a mistake.

---

## OUTPUT FORMAT — use this exact structure

```
FILM: [name as shown, or "(not supplied)"]
RUNTIME: [mm:ss — "measured" if read from the container's own duration,
          "~mm:ss ESTIMATED" if counted from playback; an estimated runtime
          may never be used to declare a scene missing or a plan violated]
SCENES OBSERVED: [n] · CUTS COUNTED: [n] · CHARACTERS TRACKED: [n]
SETUP INVENTORY: [distinct setups: n · repeat map: which scenes share a
          setup, e.g. "A: S0, S2, S5 · B: S1, S3 · C: S4" · distinct angle
          types used: n, named — low, high, overhead, dutch, eye level,
          over-the-shoulder, profile, POV]
          This line is a measurement, not a score. It changes no category
          and lowers nothing on its own. Write "not determinable" for any
          part you cannot read off the image.
NON-SCENE MATERIAL: [in-out + what it is, or "none"]
LINES HEARD: [n · every spoken line VERBATIM with its timecode, or "none"]
             When you write "none", say which none it is: "none — room tone
             present" or "none — nothing audible to me". A film with no
             dialogue and a film with no audio track are different objects and
             only one of them is a delivery defect.
             ⛔ THIS LINE REPORTS WHAT YOU HEARD. It is never a statement
             about the file. You may not write that the file has no audio
             track, no audio stream, no audio information, or that the audio
             was stripped in export: that is a property of the container, it
             is read with one ffprobe command, and no model can observe it.
             Write "none — nothing audible to me" and put the question in
             FLAGS. A run that stops on that claim is a run never made.

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Material that carries
burned-in text, or is static, or bears no scene fingerprint, is a card — a
14-second card is no more a scene than a 4-second one. Report its in and out
timecode on that line, then EXCLUDE it from CUTS COUNTED, from the scene map,
from the presence string and from every duration you report. Its text is never
the film's name.

⛔ LINES HEARD is a transcript, not a summary. Write each line inside quotes
exactly as spoken, with the second it starts. If a line repeats, list BOTH
occurrences with both timecodes — the same line twice, one clip length apart,
is evidence about the edit and is lost the moment you collapse it into one
entry. Write "none" for a silent film; never leave this line off.

⛔ CUTS COUNTED is not optional and not a rounded impression: it is the count
you made in STEP 1, with its timecodes. A report that names scenes without
printing this number has not measured the material's shape, and every score
built on that scene map is a score of a film that may not exist. If your
scene map contains a block longer than twice the shortest gap you measured
between two cuts, split it and count again BEFORE you write this line.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. When something this lens measures is
absent in EVERY scene without a single exception — no face ever framed, no
second figure ever present, no counter anywhere in the film — that is a
constraint of the material, not a defect. Such a category takes `N/A`, stays
out of the mean, and the absence is named in one line. Score low only for an
absence that is scattered: present in some scenes and gone in others. A
throughout-absence you suspect is deliberate goes to FLAGS as a question,
never to a score.

MATERIAL TYPE: [FILM / TEASER / FILM (undeclared)]
          A teaser is a trailer for a longer piece. It advances by JUMPING,
          so a skipped transition is never a causality finding in it; report
          only STATE contradictions — what was opened is closed again, what
          was taken is back, what was damaged is whole.
BASELINE: SELF-CONSISTENCY — this review measures whether the film and its
          people agree with themselves, not whether they match a design.

ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded,
                                 never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
VERDICT: [HOLDS TOGETHER / DRIFTS BUT RECOVERABLE / FIXABLE IN EDIT /
          STRUCTURAL PROBLEM / IDENTITY BREAK]
         Two findings outrank every other score:
         · a different-person face or an on-screen duplicate = IDENTITY BREAK
         · a reversing counter                               = STRUCTURAL

## SCENE INVENTORY
| # | In-out | Location | Present | What happens | Dialogue |

## CHARACTER PASSPORT(S)
[the full STEP 1 passport for each character — this is evidence, include it]

## APPEARANCE TABLE
| Character | Scene | In-out | Face visible? | State notes |

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Issue cell, as timecodes:
   | Geography | 4/10 | -3 · 2:20 (C1) · 2:30 (C2) |
   A deduction with no listed source is not applied; the category starts full.
② ONE OBSERVATION, ONE PLACE. An observation is EITHER a severity-tagged
   finding (it lowers a score) OR a question for the document (it lowers
   nothing). Never both. This applies with double force here: the BODY
   categories (1-6) and the WORLD categories (7-13) meet at costume, props
   and state, and the same dusty sleeve must not be billed to both.
③ An event you called UNVERIFIABLE / NOT OBSERVABLE / ⚠️ PARTIAL in one
   category may NOT be scored in a neighbouring one. The label belongs to
   the OBSERVATION, not to the category cell you happened to write it in.
④ THE OVERALL SCORE IS ARITHMETIC, NOT AN IMPRESSION. Every category begins
   at 10/10 and loses only the deductions its own Issue cell lists with
   timecodes. A category whose issue cell reads "no in-scope source", "no
   source" or the equivalent CARRIES NO NUMBER: write `—` in the Score cell
   and keep it OUT of the mean, exactly like N/A. Absence of evidence is not
   evidence of perfection, and a full score is a claim you did not measure.
   Writing that phrase and any number in the same row is a contradiction, and
   the phrase wins. Then
   compute the OVERALL SCORE as the mean of the category scores you actually
   printed, and use that same number everywhere the report asks for a total.
   Before you finish, add the printed cells and check the mean against your
   overall: if they disagree, the table is right and the overall is wrong.
   Two different totals for one film is a defect, and a total that no set of
   printed cells can produce is a fabricated measurement.
⑤ COUNT THE SEVERITY TALLY FROM THE FINDINGS, NOT FROM MEMORY. Before
   printing it, count the 🔴, 🟠 and 🟡 tags actually written in this
   report; the tally must equal those counts. A verdict driven by a tally
   that does not match the findings is a fabricated verdict.
```

| # | Category | Score | Critical Issue |
|:--:|---|:---:|---|
| 1 | Identity — Face, Hair & Build | __/10 | [brief] |
| 2 | Costume Identity | __/10 | [brief] |
| 3 | Wear, Damage & Injury | __/10 | [brief] |
| 4 | Equipment & Carried Objects | __/10 | [brief] |
| 5 | Cross-Cut Action | __/10 | [brief] |
| 6 | Physical Consistency | __/10 | [brief] |
| 7 | Counter Logic | __/10 or N/A | [brief] |
| 8 | Spatial Geography | __/10 | [brief] |
| 9 | Time & Light Logic | __/10 | [brief] |
| 10 | World State & Props | __/10 | [brief] |
| 11 | Causality & Knowledge | __/10 | [brief] |
| 12 | Quantity & Character Count | __/10 or N/A | [brief] |
| 13 | Setup & Abandonment | __/10 | [brief] |

Categories 1-6 are the BODY, 7-13 are the WORLD. A reader scanning this table
should be able to tell at a glance whether the film loses its people or loses
its place — they are different production failures with different fixes.

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` if a human figure is
visible anywhere in that scene, `-` if the scene has none. Cover only the
scenes you listed above, and leave out any title card or other non-scene
material you set aside. Write this line even when the order looks fine to
you, and never reorder it to match what you expect a film to do — it is a
fingerprint of the EDIT'S ORDER, and it is the one line another reader can
check against the shooting plan without watching anything.

## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __

## DRIFT MAP — where the film starts losing itself
| Half | Element | Character (if body) | First slip (timecode) | Undeniable by | Recovered? |
One table, both halves — write BODY or WORLD in the first column. This is the
single most useful output of this lens: it tells the editor where to cut and
the next film where to anchor.

## WEAR TIMELINE — per tracked mark
| Mark | Character | Acquired | Present at | Absent at ⚠️ | One-way? |

## COUNTER CURVE
[observed values in scene order, ⚠️ on any reversal or stall. Or: NONE]

## LOCATION MAP
| Location (your name for it) | Scenes | Consistent? | Mismatch |

## CONTRADICTION LOG
| Timecode A | Timecode B | Half | Character | Cat. | What contradicts what | Severity |
⚠️ Every row must have TWO timecodes. A single observation is not a
contradiction. If you cannot name both sides, it does not belong here.

## OPEN THREADS
| Object / setup | Introduced | Returned to? | Note |
Flags only, no verdicts.

## THE THREE THAT MATTER
The three breaks a viewer is most likely to FEEL, ranked. For each: what it
is, why a viewer would feel it (even without being able to locate it), and
the cheapest fix (re-cut / regenerate one scene / insert a shot / accept it).

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Finding | Fix | Cost |

## FLAGS FOR DOCUMENT CHECK
Things you cannot resolve from the video alone, listed as questions for
whoever holds the plan and the character bible:
| Observation | Question the document must answer |
Examples: "The patch reads left-shoulder in S3 and right-shoulder in S7 —
which side does the bible specify?" · "The line appears lower in S16 than in
S9 — was it designed to rise monotonically?"
Do NOT guess the answer. Ask the question.

## OUT-OF-SCOPE FLAGS
One line each, no score, no severity — the lens that owns it is named at the
end of the line. Write "none" if there are none.
```

---

## IMPORTANT NOTES FOR THE REVIEWER

- **Two timecodes or it is not a finding.** "The suit is dirty" and "the face
  looks different" are impressions. "The suit is dusted at 1:12 and clean at
  2:40 with no cleaning shown" and "the jawline at 0:22 and at 1:47, in
  comparable light, do not belong to the same person" are findings.
- **Light changes faces.** Before calling an identity break, ask whether the
  difference is explainable by light, angle or distance. If it plausibly is,
  report MINOR with the caveat, not a break. An identity break verdict needs
  at least two clear, comparably lit views.
- **You have no plan and no bible, so nothing can be "missing".** If you
  catch yourself writing "the film should have…" or "the character should
  have…", stop and move it to FLAGS FOR DOCUMENT CHECK as a question.
- **Deliberate change is not drift.** A character may cut their hair, shed a
  jacket, get dirty — ON SCREEN. A film may hold on emptiness or leave an
  object unused. Change with a visible cause is storytelling; change without
  one is the defect. An unused object is an OPEN THREAD, not a mistake.
- **One defect, one category — and one HALF.** A dirty-then-clean suit is
  category 3, not also 2 and not also 10. Pick the category that owns the
  root cause, and remember that anything on a body belongs to 1-6.
- **Two findings outrank everything.** An identity break: a film can score 9
  everywhere else and still be unreleasable if the lead becomes a different
  person. A reversing counter: that is not a continuity slip, it is the
  premise collapsing. Either one goes in the first line of the verdict.
- If the film holds, say so plainly and keep the report short. A review that
  always finds nine problems teaches everyone to skip the review.
