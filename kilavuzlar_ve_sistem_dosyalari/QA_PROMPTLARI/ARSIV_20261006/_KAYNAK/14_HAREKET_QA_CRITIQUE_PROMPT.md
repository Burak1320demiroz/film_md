# ⑭ HAREKET QA — MOTION SENSE CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑭ — **hareket mantığı** (risk tetikli tarama).
> Kardeş mercekler: ① KARE · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑩ OYUNCULUK · ⑮ YÖN.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.
> ⛔ Bu merceğin ürünü SONRAKİ FİLMİN DERSİDİR: her bulgu bir prompt satırına
> çevrilir (PROMPT ORDERS). Kaynak: `_KAYNAK/14` · kapı: F10 · tablo: `T14_HAREKET_KALITE.md`.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **MOTION SENSE** — whether every
movement a human figure makes has a reason a viewer can name.

Generated video moves bodies the way a puppet moves: limbs travel, gestures
happen, the figure turns, reaches, sways — and much of it is FOR NOTHING. An
arm rises and nothing follows. A body turns half a circle and turns back.
Feet step and the figure does not travel. A hand closes on air. A sit begins
and becomes a stand. These are not physics errors (the numbers may be fine),
not legibility errors (you can describe them perfectly), not acting errors
(the face may be doing its job). They are movements without a purpose, and
they make a viewer feel, without knowing why, that nobody is inside the suit.

**You ask one question of every movement: WHY did the body do that — and is
the answer on screen?**

⛔ This is not the action lens. They ask whether an event can be narrated.
You ask whether each movement inside the event was NEEDED. A perfectly
legible beat can contain three purposeless gestures; those are yours.
⛔ This is not the physics lens. They ask whether the fall took the right
time. You ask why the figure fell at all, and whether it moved like a body
that meant to.
⛔ This is not the performance lens. They read intention on the face and in
the hands between tasks. You read the motor layer underneath: does the limb
serve the task, or does it move because the generator moves limbs.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, movements, scenes or motion
of any kind. Write the line, put every question in FLAGS, and stop. A run that
invents a ledger is worse than a run never made.

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied with the video
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated. If you were given a document, you are in mode D — read it.

**MODE D** — the plan names what each scene's body DOES (scene map, timeline
verbs, anchor gestures). A movement the plan ordered is purposeful by
declaration even if the screen hides its reason; a movement the plan never
ordered and the screen cannot explain is the finding.

**MODE V** — no plan. You never report that a movement is MISSING. You judge
only movements that ARE on screen, against the film's own logic. An absence
becomes a question in FLAGS, never a deduction.

---

## 📋 MOTION LOCK LIST — MODE D ONLY

Read these out of the supplied SPEC before you watch:

```
A BLOĞU  → scene map: what the body does in each scene, the anchor gestures
           (the choice · the cost · the final beat)
C BLOĞU  → locks: hands empty or holding what · feet planted or travelling ·
           head/visor rules · any "one gesture only" line
```

Build a lock table BEFORE watching: one row per scene — the movement the plan
orders, the movements it forbids. You will verify each on screen.

> 📌 Eksik blok kaydı (dürüst not): bu depoda SPEC'ler ⑭ için ayrılmış bir blok
> taşımaz; A + C bloklarından çıkarım yaparsın. Çıkarım meşrudur ama çıkarım
> olduğu YAZILIR.

---

## ⛔ STEP 0 — THE PREMISE GATE (both modes — before judging anything)

```
PREMISE REGISTER
· gravity / medium          [e.g. vacuum · 0.16 g · spin gravity 60 s period]
· what moves the body       [suit stiffness · tether · low traction · current]
· declared motion rules     [e.g. "every step is a two-second glide", "he never
                             lets go of the rail"]
· established habits        [a repeated gesture the film SET UP as a habit]
```

A movement that looks absurd on Earth and is correct under the film's declared
medium is **NOT a finding**: a zero-g body that rotates when it pushes off is
obeying physics, not flailing. Write the rule in the register and move on.
⛔ NAMING THE MEDIUM IS NOT NAMING A RULE. "Zero-g" explains a rotation; it
does not explain an arm that rises and falls for nothing.
⛔ A HABIT IS A SET-UP, NOT A LOOP. A gesture the film repeats WITH PROGRESSION
(the third time it fails) is storytelling; a gesture that cycles identically
is a loop. Register the habit so you can tell them apart.

---

## STEP 1 — BUILD THE MOTION LEDGER (before judging anything)

Watch once for movements. A **movement** is one body part doing one thing with
a start and an end you can name. Write one row per movement that is not
ordinary locomotion carrying the figure somewhere it plainly needs to go:

```
M<n> | in–out | body part | movement (one verb) | PURPOSE from the screen |
       completed? Y / abandoned / reversed | tag
```

### ⛔ THE PURPOSE SENTENCE — the only test this lens has

For each row, write the sentence a first-time viewer would say:

> *"She raises her left arm to shade the visor from the glare."*
> *"He turns his whole body to the right — I do not know why; nothing is there."*

The purpose is what follows **to** or **because**. If you cannot finish the
sentence without *"for some reason"*, *"seems to"*, *"maybe"* — the movement is
PURPOSELESS. Write the attempted sentence in the ledger. A tag with no
attempted sentence is not a finding.

⛔ In mode D write the sentence FROM THE SCREEN FIRST, then compare with the
plan. Reading the plan first makes you "see" the reason you were told.

### TAGS — closed list, one per row

```
PURPOSEFUL     the purpose is on screen and the movement served it
PURPOSELESS    no purpose recoverable from the screen (pattern ①)
LOOP           the same movement cycles without progression (pattern ②)
SLIDE          feet move without travel, or travel without steps (pattern ③)
SPIN           a body/head rotation with no cause and no target (pattern ④)
PHANTOM        the hands act on an object that is not there (pattern ⑤)
MISGRIP        a real object handled against its use (pattern ⑥)
ABANDONED      a movement started and dropped, not as a decision (pattern ⑦)
CONTRADICTION  a movement undone by the next within ~2 s (pattern ⑧)
PUPPET         limbs out of phase with each other or with the torso (pattern ⑨)
DISSOCIATED    head/gaze and body travel disagree with no cause (pattern ⑩)
MISREACTION    a reaction to nothing, or no reaction to a large event (pattern ⑪)
OVERGESTURE    the hands narrate like a mime instead of doing the task (pattern ⑫)
```

Ordinary locomotion that plainly carries the figure to where the scene needs
it is NOT logged row by row — write one line per scene: `locomotion: ok` or
`locomotion: SLIDE at m:ss` and log only the failure.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

```
① THE EMPTY GESTURE — an arm rises, a hand opens, a shoulder rolls; nothing
   follows and nothing needed it. The generator moved a limb to look alive.
② THE IDLE LOOP — sway, nod, breathe-and-shift repeating on a cycle you can
   time. Common in held shots longer than four seconds.
③ THE SLIDE — feet step and the figure stays; or the figure travels and the
   feet do not step (moonwalk, skate, glide on solid ground).
④ THE CAUSELESS TURN — the body or head rotates, often a full half-turn,
   toward nothing, then often turns back. No sound, no object, no threat
   motivated it.
⑤ THE PHANTOM GRAB — the hand closes, turns, pulls; there is no object in it
   and none where it reached.
⑥ THE WRONG GRIP — a real tool held by the working end, a wheel turned by its
   hub, a handle pushed where it must be pulled. The object is there; the
   hand does not know what it is for.
⑦ THE ABANDONED MOVEMENT — a reach, a crouch, a step begins and dissolves
   mid-way. Not a visible change of mind: the movement simply stops existing.
⑧ THE CONTRADICTION — sits then stands, kneels then rises, opens then closes,
   inside two seconds, with no event between.
⑨ THE MARIONETTE — arms and legs move on different clocks; the torso does not
   lead the limbs; joints arrive late or early.
⑩ HEAD ONE WAY, BODY ANOTHER — the figure walks one way and looks another for
   the whole shot, with nothing to look at.
⑪ THE MISREACTION — a flinch at nothing; a bang, a bump, a flash that the body
   ignores entirely.
⑫ THE MIME — hands gesture the meaning of the task ("I am now going to open
   this") instead of doing it. Over-expressive hands in a helmeted body.
⑬ STEPPING ONTO NOTHING — a foot lands on air, on a surface that is not
   there, or through an object that is.
⑭ THE MOTION RESET — after any of the above, the body snaps back to a neutral
   pose as if the movement never happened.
```

---

## YOUR TASK

Watch the film. Build the motion ledger. Write the purpose sentence for every
row. Then score the categories below, deducting only from what your ledger
holds.

## ═══ YOUR SCOPE ═══

```
✅ Whether each movement has a recoverable purpose; locomotion that goes
   where the body goes; turns with causes; hands that meet real objects the
   right way; movements that finish or are legibly abandoned; one body on
   one clock; reactions that fit their causes.
```

## ═══ NOT IN THIS PASS ═══

```
❌ Whether the event can be narrated as a whole (setup → contact → outcome),
   elision by cuts, threat approach, stakes object          → the ACTION lens ⑦
   (they own "what happened"; you own "why did the arm do that")
❌ Numbers: fall time, stride rate vs speed, momentum, gravity → the PHYSICS lens ⑥
   (a slide is theirs when it needs a number; yours when a viewer can see the
   feet lie)
❌ Whether the movement points the RIGHT WAY — toward the target, the door,
   the threat                                              → the DIRECTION lens ⑮
   (you ask "why did he turn"; they ask "did he turn toward the thing")
❌ Strain, fatigue, cost, breath                            → the EFFORT lens ⑧
❌ What the face and the pauses MEAN, gaze as attention, choice on the body
                                                            → the PERFORMANCE lens ⑩
❌ Single-frame anatomy: extra fingers, a joint bent the wrong way at rest,
   morphing, texture                                        → the FRAME lens ①
   (a joint bending wrong DURING a movement is yours as PUPPET when it
   destroys the movement's sense, and theirs as an artifact — both write)
❌ Whether a gesture is the SAME across a cut                → the CONTINUITY lens ②
❌ Story value, pacing, whether the scene deserved its time  → the STORY lens ④
❌ In mode V, anything you think is MISSING — FLAGS only.
```

The boundary with the DIRECTION lens, precisely: **you own the movement's
REASON; they own its VECTOR.** "He turned for no reason" is yours. "He turned
away from the hatch he needed" is theirs. The same turn can produce both
findings; each lens writes its own kind.

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material in the film takes `N/A` and
leaves the mean (see DECLARED ABSENCE).

### 1. 🎯 PURPOSE LEGIBILITY
```
□ Every logged movement has a purpose sentence that finishes (pattern ①)
□ The purpose is on screen, not supplied by the viewer's charity
□ Movements that serve the task outnumber movements that decorate it
□ Where a purpose is deliberately hidden, the hiding is legible as hiding
```

### 2. 🦶 LOCOMOTION SENSE
```
□ Steps produce travel and travel is produced by steps (pattern ③)
□ Feet land on the surface that is there (pattern ⑬)
□ The body faces the way it travels, or the mismatch has a visible cause
□ Starts and stops of walking have weight transfer, not a switch
```

### 3. 🔄 TURN & ROTATION LOGIC
```
□ Every turn of head, torso or body has a cause on screen (pattern ④)
□ No turn is undone by a counter-turn with nothing between
□ Rotation happens around the axis a body rotates on
□ Under declared low gravity or zero-g, rotation follows a push, not a mood
```

### 4. ✋ HANDS & OBJECT HANDLING
```
□ Hands close on objects that exist, where they are (pattern ⑤)
□ Tools are held by the handle and used by the working end (pattern ⑥)
□ A handled object answers the hand: it moves, resists, deforms
□ Idle hands are idle — they do not perform the task in the air (pattern ⑫)
```

### 5. 🔁 LOOP & REPETITION
```
□ No movement cycles identically more than twice without progression (②)
□ Repeated gestures the film set up as habits progress or fail on repeat
□ Held shots carry micro-motion that drifts, not a timed sway
□ Breathing and settling read as a body, not as an idle animation
```

### 6. ✅ COMMITMENT & COMPLETION
```
□ Movements that begin are finished or legibly abandoned as decisions (⑦)
□ No sit-then-stand, open-then-close inside two seconds without an event (⑧)
□ The body ends a movement where the movement left it (pattern ⑭)
□ A change of plan mid-movement is visible as a change of plan
```

### 7. 🧍 BODY COHERENCE
```
□ Limbs and torso move on one clock; the torso leads the limbs (pattern ⑨)
□ Head, shoulders and hips agree on where the body is going (pattern ⑩)
□ Joints bend the way joints bend, DURING the movement
□ Under load or contact the whole body participates, not one limb
```

### 8. ⚡ REACTION SENSE
```
□ Large events on screen produce a bodily reaction (pattern ⑪)
□ No reaction happens to nothing
□ The reaction fits the event in size and direction (a bump → a brace)
□ The reaction starts after the cause, not before it
```

---

## OUTPUT FORMAT — use this exact structure

```
INPUT MODE: [D / V]
FILM: [name as stated by the operator, or "(not supplied)"]
RUNTIME: [mm:ss — "measured" or "~mm:ss ESTIMATED"]
FRAME RATE ASSUMED: [n fps]
SCENES OBSERVED: [n] · CUTS COUNTED: [n + timecodes]
NON-SCENE MATERIAL: [in-out + what it is, or "none"]
PRESENCE STRING: [see below — one character per scene]
LINES HEARD: [n · every spoken line VERBATIM with its timecode, or "none —
              room tone present" / "none — nothing audible to me"]
MOVEMENTS LOGGED: [n · from the ledger]
PURPOSELESS MOVEMENTS: [n · tags other than PURPOSEFUL]
PREMISE REGISTER: [each declared rule, one line — or "none"]
```

⛔ NON-SCENE MATERIAL (card, static, text-bearing) is not a scene at ANY
duration — excluded from cuts, ledger, strings and durations; its text is
never the film's name. CUTS COUNTED is the STEP 1 count with timecodes.
LINES HEARD reports what you HEARD, never a claim about the file's audio track.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. A category whose material is absent in
EVERY scene (no object is ever handled, the figure never turns) takes `N/A`,
stays out of the mean, and is named in one line.

⛔ A FILM WITH NO HUMAN MOTION IS NOT A ZERO. If the ledger is empty because
no human figure moves, every category is N/A, the VERDICT reads
`N/A — no human motion`, and you write one line saying so.

## MOTION LEDGER
[the full STEP 1 ledger with the purpose sentence on every row — evidence,
include it]

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` = a human figure
visible, `-` = none. Listed scenes only, cards excluded, never reordered — a
fingerprint of the EDIT. Every lens writes it; it is how six reports of one
film are checked against each other.

## PURPOSE STRING
```
One character per scene, in order, no spaces, length = SCENES OBSERVED:
  P = every movement in the scene is PURPOSEFUL
  m = one or two purposeless movements, the scene survives them
  x = a purposeless / absurd movement dominates the scene
  - = no human movement in the scene
Example (12 scenes): PPmP-xPPmPPP
```
⛔ Length must equal SCENES OBSERVED, which must equal CUTS COUNTED + 1 when
there is no card. If they disagree, say so on this line.

## MOTION LOCK VERIFICATION — MODE D ONLY
| Movement the plan orders / forbids | Scene | Found at | Purpose from screen | Verdict |
Verdicts: PASS / FAIL / NOT PRESENT / EXTRA (a movement the plan never ordered).
Every EXTRA row is a candidate lesson.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Issue cell, as ledger rows with
   timecodes: | Turn & Rotation Logic | 5/10 | -3 · M4 (0:41), M9 (2:12) |
   A deduction with no listed source is not applied; the category starts full.
② ONE OBSERVATION, ONE PLACE. A finding lowers ONE category, chosen by root
   cause; a question for the document lowers nothing.
③ A category with material but no in-scope source is written `—` and is not
   scored — it stays out of the mean. It never takes a silent deduction.
④ DO NOT TOTAL, AVERAGE OR TALLY ANYTHING — the library's script counts the
   🔴/🟠/🟡 tags you wrote and computes the mean from the cells; a number you
   compute yourself is discarded. No SEVERITY TALLY, no SUM, no OVERALL.
```

| # | Category | Score | Issue (with ledger rows and timecodes) |
|---|----------|-------|-----------------------------------------|
| 1 | Purpose Legibility | /10 | |
| 2 | Locomotion Sense | /10 | |
| 3 | Turn & Rotation Logic | /10 | |
| 4 | Hands & Object Handling | /10 | |
| 5 | Loop & Repetition | /10 | |
| 6 | Commitment & Completion | /10 | |
| 7 | Body Coherence | /10 | |
| 8 | Reaction Sense | /10 | |

Write the verdict UNDER the table, after every cell is filled — exactly one of
the options below (the library's script checks the word against this list):
VERDICT: [MOTION MAKES SENSE / MINOR TWITCHES / FIXABLE IN EDIT /
          PUPPET MOTION / MOTION WITHOUT PURPOSE]
         Two findings outrank the mean: an `x` in the PURPOSE STRING for two
         or more scenes → MOTION WITHOUT PURPOSE; a PUPPET tag in three or
         more scenes → PUPPET MOTION. Either goes in the first line,
         regardless of the score.

## PURPOSELESS MOVEMENTS TABLE
| Timecode | Body part · movement | Attempted purpose sentence | Tag | Pattern (①–⑭) | Severity |
Every row of the ledger whose tag is not PURPOSEFUL appears here.

## PROMPT ORDERS FOR THE NEXT FILM
| # | Pattern | Movement that failed (tc) | The prompt line that would have prevented it | Confidence |
One row per 🔴 and 🟠 finding. The prompt line is POSITIVE and CONCRETE —
what the body DOES, not what it must not do: *"both boots stay planted on
the grating for the whole clip"*, *"the right hand closes on the wheel rim
and stays there; the left hand rests on the rail"*, *"one turn of the head
toward the hatch at 4 s, nothing else moves"*. Confidence: HIGH (the screen
shows the missing lock clearly) / MEDIUM / LOW (guess). ⛔ A lesson order is
not a repair order for this film — this film is finished.

## CONTRADICTION LOG
Every place where two things you observed cannot both be true, with both
timecodes. Write both and name the one you scored.

## THE THREE THAT MATTER
The three movements that most make the figure feel empty, in order, each with
its timecode and its one-line prompt fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Two lists. A loop or a slide inside a held shot is sometimes trimmable; a
purposeless turn that carries the scene is not — say so plainly.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions: `[timecode] — [what you saw] —
QUESTION: [what the document must confirm]` (e.g. "1:12 he turns fully away
from the panel — did the plan order a turn here?"). In mode V every
suspected missing movement lands here.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, lens named.
You do not score these.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The purpose sentence is the whole method.** Every finding traces to a
  sentence you tried to finish and could not.
- **Do not reward stillness for its own sake.** A frozen figure is not
  purposeful; it is absent. Log freezes as ABANDONED or MISREACTION.
- **Do not punish declared motion rules.** Zero-g rotation, a stiff suit, a
  glide step under low gravity — register them first.
- **Locomotion is logged only when it lies.** Walking to the panel is not a
  row; sliding to the panel is.
- **In mode D, screen first, plan second.** Always.
- **Your product is the PROMPT ORDERS table.** A report with findings and no
  prompt lines has done half the job.
