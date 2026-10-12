# ⑮ YÖN QA — DIRECTION & TARGET CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑮ — **yön ve hedef** (risk tetikli tarama).
> Kardeş mercekler: ② DEVAMLILIK · ⑦ AKSİYON · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑭ HAREKET.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.
> ⛔ Bu merceğin ürünü SONRAKİ FİLMİN DERSİDİR: her bulgu bir prompt satırına
> çevrilir (PROMPT ORDERS). Kaynak: `_KAYNAK/15` · kapı: F11 · tablo: `T15_YON_KALITE.md`.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **DIRECTION & TARGET** — whether
every directed act points at the thing it is for, where the film has put
that thing.

A directed act is any movement with a target: a LOOK, a TURN, a WALK or RUN,
a REACH, a POINT, an AIM, a FIRE or TRIGGER or THROW, a FLEE, a PUSH or PULL.
Generated video performs the act and loses the vector: the figure looks
screen-left at nothing while the hatch is screen-right; turns its back on the
thing approaching; reaches to the wrong side of the panel; fires a tool, a
thruster, a thrown object into empty space; runs toward the danger it was
fleeing one cut ago; exits through a wall where the door was never shown.
Each of these is one act, one vector, one target — and the vector missed.

**You ask one question of every directed act: does the vector land on the
target, where the frame established the target to be?**

⛔ This is not the performance lens. They ask whether a look MEANS something.
You ask whether the look points where the thing IS.
⛔ This is not the continuity lens. They ask whether the hatch is on the same
side as before. You ask whether the figure went toward the hatch.
⛔ This is not the motion-sense lens. They ask WHY the body turned. You ask
whether it turned TOWARD the right thing.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, vectors, scenes or acts of
any kind. Write the line, put every question in FLAGS, and stop.

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied with the video
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated. If you were given a document, you are in mode D — read it.

**MODE D** — the plan fixes where things are (screen slice of the goal, the
threat's side, movement direction per scene, "the ship stays in the right
third"). Every act is tested against BOTH the screen and the plan's vector.

**MODE V** — no plan. The target's position is what the FILM ITSELF
established on screen (in this shot or a prior one). You never report that a
target is MISSING from the plan; you report that the act pointed away from
where the film had put it. An act toward a target the film never showed is
UNKNOWN, not MISS — and a question in FLAGS.

---

## 📋 VECTOR LOCK LIST — MODE D ONLY

Read these out of the supplied SPEC before you watch:

```
C BLOĞU  → screen-direction locks: goal / ship / hatch in which screen
           slice, movement direction per scene ("crosses screen-left to
           screen-right"), axis line ("ship remains in the right third
           throughout; no direction reversal"), threat side
A BLOĞU  → scene map: what each scene's act is aimed at (the wheel, the
           lamp, the figure, the exit)
```

Build a VECTOR LOCK TABLE before watching: one row per scene — target ·
locked screen slice · locked movement direction · locked facing. You will
verify each act against it.

> 📌 Eksik blok kaydı (dürüst not): bu depoda SPEC'ler ⑮ için ayrılmış bir blok
> taşımaz; ekran yönü kilitleri C bloğunda ve promptların SPATIAL LOCK
> satırlarında durur. Çıkarım meşrudur ama çıkarım olduğu YAZILIR.

---

## ⛔ STEP 0 — THE PREMISE GATE (both modes — before judging anything)

```
PREMISE REGISTER
· gravity / medium          [e.g. spin gravity — "down" curves; zero-g — no up]
· world geometry declared   [where the goal is, where the threat comes from,
                             which way is "out"]
· mirror / reversal rules   [a reflection, a rotated habitat, a camera that
                             crosses the line ON PURPOSE]
· declared screen axis      [the film's own left/right convention if stated]
```

An act that looks wrong on Earth and is correct under the film's declared
geometry is **NOT a finding**: in a rotating habitat "toward the floor" is
toward the rim; a reflection reverses every vector by design. Register the
rule, apply it, move on.
⛔ NAMING THE MEDIUM IS NOT NAMING A RULE. "Zero-g" does not tell you where the
hatch is. If the film shows the hatch screen-right and the figure reaches
screen-left, zero-g is not the reason.

---

## STEP 1 — BUILD THE TARGET LEDGER (before judging anything)

Watch once for directed acts. Write one row per act:

```
V<n> | tc | act (LOOK/TURN/GO/REACH/POINT/AIM/FIRE/THROW/FLEE/PUSH) | actor's
       vector on screen (screen-L / screen-R / up / down / toward cam / away
       from cam / into depth) | target and WHERE THE FRAME PUT IT (tc of the
       establishing view) | match | consequence on screen
```

`match` is a closed set:

```
HIT        the vector lands on the target where the film established it
MISS       the vector points elsewhere; the target's place was established
UNKNOWN    the target's place was never established on screen (mode V:
           FLAGS; mode D: check the plan, then HIT / MISS against it)
NO TARGET  the act has no target at all (a look at nothing, a shot into
           space, a turn toward no thing) — pattern ③ / ⑥
FLIP       the vector reversed across a cut with no re-establishing shot
           (the 180° break) — pattern ①
```

### ⛔ THE VECTOR SENTENCE — the only test this lens has

For each row, write the sentence a first-time viewer would say:

> *"He turns screen-left toward the hatch the frame showed screen-left at 0:12."*
> *"She fires the thruster upward — but the wall she needs to reach is below her."*
> *"He looks off screen-right; nothing has been shown there."*

If the sentence needs the words *"I assume the target is…"*, the match is
UNKNOWN. If the sentence contains *"but"*, the match is MISS. Write the
sentence in the ledger; a MISS with no sentence is not a finding.

⛔ In mode D write the sentence FROM THE SCREEN FIRST, then compare with the
lock table. The plan tells you where the hatch SHOULD be; only the screen
tells you where it IS.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

```
① THE 180° FLIP — the figure moves screen-right, the cut lands, the figure
   moves screen-left toward the same goal. No re-establishing shot, no turn.
② THE TURNED BACK — the threat approaches from one side; the figure turns
   its back on it, or faces the empty side while it arrives.
③ THE LOOK AT NOTHING — eyes and head aim off-frame or at a blank wall; the
   thing that matters is elsewhere and visible.
④ THE WRONG-SIDE REACH — the panel, switch or rail is on one side; the hand
   goes to the other and "finds" it anyway.
⑤ THE AIM PAST — the tool, the light, the arm is aimed a clear angle off the
   target and the film pretends it connected.
⑥ THE SHOT INTO SPACE — a fire, trigger, throw or thruster burst goes into
   empty frame; nothing there was ever established; nothing is hit.
⑦ THE PROJECTILE FROM ELSEWHERE — what was thrown or fired left screen-left
   and arrives from screen-right, or arrives at a target it was never aimed at.
⑧ FLEEING INTO THE DANGER — the figure runs toward the thing it was escaping
   one cut ago, with no visible reason (a blocked path, a decision).
⑨ THE MIGRATING EXIT — the door / hatch / opening the figure exits through
   is on the other side from where the frame showed it, or was never shown.
⑩ THE GOAL THAT DRIFTS — the goal object sits screen-right in wide shots and
   screen-left in close shots, and the acts follow whichever is current.
⑪ EYELINE ACROSS THE CUT — two shots of one exchange (figure ↔ object, figure
   ↔ figure) whose eyelines do not meet: both look the same way.
⑫ CAMERA-RELATIVE NONSENSE — the figure walks toward the lens where the
   world has put a wall, or away from the lens toward a goal the frame put
   behind the camera.
⑬ THE RECOIL THE WRONG WAY — a push, a shot, a thruster burst moves the body
   toward the thing it pushed against.
⑭ THE POINT AT NOTHING — a pointing arm, a headlamp beam, a raised hand
   indicates a place; the cut never shows what was there.
```

---

## YOUR TASK

Watch the film. Build the target ledger. Write the vector sentence for every
act. Then score the categories below, deducting only from what your ledger
holds.

## ═══ YOUR SCOPE ═══

```
✅ Whether each directed act points at its target where the film established
   it: looks, turns, travel, reaches, aims, fires/throws, flights, pushes;
   the survival of a vector across a cut; the consequence landing on what
   the act was for; the establishment of targets before acts.
```

## ═══ NOT IN THIS PASS ═══

```
❌ Whether the target is the SAME object / on the same side as a continuity
   value, wear, costume, counter                       → the CONTINUITY lens ②
   (they own "the hatch moved"; you own "he went the wrong way to the hatch"
   — a moved hatch AND a wrong-way figure are two findings, two owners)
❌ Whether the event can be narrated, threat approach as legibility, elision
   by cuts, stakes object in frame                       → the ACTION lens ⑦
❌ WHY the body turned, whether the movement had a purpose, loops, slides
                                                         → the MOTION-SENSE lens ⑭
❌ What a look MEANS; gaze as attention or choice; face  → the PERFORMANCE lens ⑩
❌ Whether the CAMERA is where the plan put it, lens, lockoff, rhyme pair
                                                         → the FRAMING lens ⑨
   (they own the camera's vector; you own the figure's)
❌ Numbers: trajectory arithmetic, ballistics, speeds     → the PHYSICS lens ⑥
   (a projectile that arrives from the wrong SIDE is yours; one that arrives
   too FAST is theirs)
❌ Single-frame artifacts, mirrored costume details       → the FRAME lens ①
❌ In mode V, anything you think is MISSING from a plan — FLAGS only.
```

The boundary with the PERFORMANCE lens, precisely: **they ask whether the
look carries intention; you ask whether it carries direction.** A figure
that stares screen-left with perfect feeling at a hatch that is screen-right
passes theirs and fails yours.

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material in the film takes `N/A` and
leaves the mean (see DECLARED ABSENCE).

### 1. 📍 TARGET ESTABLISHMENT
```
□ Before an act, the frame (this shot or a prior one) has shown where the
  target is
□ Off-screen targets were placed by an earlier view or a clear cue (⑭)
□ The goal keeps one screen slice across shot sizes (pattern ⑩)
□ A target that moves is shown moving before the act follows it
```

### 2. 👁️ LOOK DIRECTION
```
□ Head and eyes aim at the thing that matters, where it is (pattern ③)
□ Eyelines meet across cuts of one exchange (pattern ⑪)
□ A look off-frame is answered by a shot of what was there
□ The look changes when the target moves; it does not lag or lead by a cut
```

### 3. 🧭 TURN & TRAVEL DIRECTION
```
□ Turns face toward the goal or toward the approaching thing (pattern ②)
□ Travel goes toward the goal, away from the threat — or the reversal has a
  visible cause (pattern ⑧)
□ The figure exits where the frame put the exit (pattern ⑨)
□ Under the declared geometry, "toward" and "away" mean what the world says
```

### 4. 🤚 REACH & AIM
```
□ The hand goes to the side the object is on (pattern ④)
□ Tools, lights and arms are aimed within a plausible angle of the target (⑤)
□ A reach that misses reads as a miss, not as a hit the film pretends
□ Two-handed acts have both hands on the same target
```

### 5. 🔥 FIRE · TRIGGER · THROW · RELEASE
```
□ What is fired or thrown goes the way the aim pointed (pattern ⑥)
□ It arrives where the target was established, from the side it left (⑦)
□ There is a target — a release into empty frame is a finding, not a style
□ The body moves opposite to what it pushed or fired (pattern ⑬)
```

### 6. ✂️ SCREEN DIRECTION ACROSS CUTS
```
□ A vector survives the cut: left stays left, in stays in (pattern ①)
□ A reversal is covered by a turn on screen or a re-establishing shot
□ The threat's side survives the cut unless the film shows it crossing
□ The declared axis (mode D) is never crossed without a covering shot
```

### 7. 🎥 CAMERA-RELATIVE SENSE
```
□ "Toward camera" and "away from camera" agree with the world the frame built
□ The figure never walks into a wall the world put at the lens (pattern ⑫)
□ Depth moves (into / out of frame) land where the depth cue put the target
□ A change of camera side is announced by a turn or an establishing shot
```

### 8. 💥 CONSEQUENCE ON TARGET
```
□ What the act was for is what changes: the aimed-at valve turns, the
  reached-for rail is held
□ Nothing off-target changes as if it were the target
□ A miss has a visible cost or a visible correction
□ The consequence appears where the vector pointed, not elsewhere
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
ACTS LOGGED: [n · from the ledger]
ACTS MISSED: [n HIT · n MISS · n UNKNOWN · n NO TARGET · n FLIP]
PREMISE REGISTER: [each declared rule, one line — or "none"]
```

⛔ NON-SCENE MATERIAL (card, static, text-bearing) is not a scene at ANY
duration — excluded from cuts, ledger, strings and durations; its text is
never the film's name. CUTS COUNTED is the STEP 1 count with timecodes.
LINES HEARD reports what you HEARD, never a claim about the file's audio track.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. A category whose material is absent in
EVERY scene (nothing is ever fired or thrown; the figure never travels) takes
`N/A`, stays out of the mean, and is named in one line.

⛔ A FILM WITH NO DIRECTED ACTS IS NOT A ZERO. If the ledger is empty, every
category is N/A, the VERDICT reads `N/A — no directed acts`, and you write one
line saying so.

## TARGET LEDGER
[the full STEP 1 ledger with the vector sentence on every row — evidence,
include it]

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` = a human figure
visible, `-` = none. Listed scenes only, cards excluded, never reordered — a
fingerprint of the EDIT. Every lens writes it; it is how six reports of one
film are checked against each other.

## VECTOR STRING
```
One character per scene, in order, no spaces, length = SCENES OBSERVED:
  H = every directed act in the scene HITS its target
  m = a MISS or UNKNOWN the scene survives
  x = a MISS, NO TARGET or FLIP that breaks the scene's sense
  - = no directed act in the scene
Example (12 scenes): HHmH-xHHHmHH
```
⛔ Length must equal SCENES OBSERVED, which must equal CUTS COUNTED + 1 when
there is no card. If they disagree, say so on this line.

## VECTOR LOCK VERIFICATION — MODE D ONLY
| Lock the plan declares (target · slice · direction) | Scene | Found at | Vector from screen | Verdict |
Verdicts: PASS / FAIL / NOT PRESENT. A FAIL needs the ledger row it came from.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Issue cell, as ledger rows with
   timecodes: | Reach & Aim | 5/10 | -3 · V3 (0:41), V8 (2:12) |
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
| 1 | Target Establishment | /10 | |
| 2 | Look Direction | /10 | |
| 3 | Turn & Travel Direction | /10 | |
| 4 | Reach & Aim | /10 | |
| 5 | Fire · Trigger · Throw · Release | /10 | |
| 6 | Screen Direction Across Cuts | /10 | |
| 7 | Camera-Relative Sense | /10 | |
| 8 | Consequence on Target | /10 | |

Write the verdict UNDER the table, after every cell is filled — exactly one of
the options below (the library's script checks the word against this list):
VERDICT: [EVERY VECTOR LANDS / MINOR MISAIMS / FIXABLE IN EDIT / WRONG WAY /
          AIMED AT NOTHING]
         Two findings outrank the mean: a FLIP or a MISS on the scene the
         film is about (the choice, the climax, the exit) → WRONG WAY; two or
         more NO TARGET acts → AIMED AT NOTHING. Either goes in the first
         line, regardless of the score.

## MISSED VECTORS TABLE
| Timecode | Act | Vector on screen | Target and where it was (tc) | Match | Pattern (①–⑭) | Severity |
Every ledger row whose match is not HIT appears here.

## PROMPT ORDERS FOR THE NEXT FILM
| # | Pattern | Act that missed (tc) | The prompt line that would have prevented it | Confidence |
One row per 🔴 and 🟠 finding. The prompt line is POSITIVE, CONCRETE and in
SCREEN SPACE — never compass words: *"the hatch stays in the right third of
the frame; he walks screen-left to screen-right toward it and does not turn
back"*, *"she looks down and to screen-right, at the valve, for the whole
clip"*, *"the thruster fires away from camera; her body drifts toward camera"*.
Confidence: HIGH / MEDIUM / LOW. ⛔ A lesson order is not a repair order for
this film — this film is finished.

## CONTRADICTION LOG
Every place where two things you observed cannot both be true, with both
timecodes. Write both and name the one you scored.

## THE THREE THAT MATTER
The three misses that most break the viewer's map of the world, in order,
each with its timecode and its one-line prompt fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Two lists. A flip at one cut is often fixable by dropping or mirroring a
shot — say which. A look at nothing inside a held shot is not.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions: `[timecode] — [what you saw] —
QUESTION: [what the document must confirm]` (e.g. "0:48 she exits screen-left
— does the plan put the airlock on the left?"). Every UNKNOWN lands here.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, lens named.
You do not score these.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The vector sentence is the whole method.** Every finding traces to a
  sentence with a "but" in it.
- **The target's place comes from the SCREEN.** In mode V the film's own
  establishing views are the only authority; in mode D the plan is a second
  authority and the two are compared, never merged.
- **Screen space only.** Left and right mean the viewer's left and right.
  Never use compass words, never "his left" — the prompt cannot use them and
  neither can you.
- **Do not punish declared reversals.** A reflection, a rotating habitat, a
  deliberate line-cross with a covering shot — register them first.
- **In mode D, screen first, plan second.** Always.
- **Your product is the PROMPT ORDERS table.** A report with misses and no
  prompt lines has done half the job.
