# ⑩ OYUNCULUK QA — PERFORMANCE LEGIBILITY CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑩. Kardeş mercekler: ① KARE · ② DEVAMLILIK ·
> ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ ·
> ⑪ IŞIK · ⑫ HOOK.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **PERFORMANCE LEGIBILITY** —
whether what the character wants, decides and feels is readable ON THE BODY,
from the screen alone.

Most of these films have no dialogue and a closed helmet. The story lives in
where the head points, what the hands do between tasks, where the weight
sits, how fast or slow a gesture is, and what the body does in the second
AFTER something happens. Generated video is excellent at performing a TASK
and poor at performing an INTENTION: the hands cut the clamp, and nothing
about the figure tells you whether it wanted to. **The story lens reads the
plan; the action lens reads the event; you read the person.**

⛔ This is not the effort lens. They ask whether the work cost the body. You
ask whether the body shows what the work MEANT. A lift can be strained and
empty; a motionless figure can carry the whole film.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, gestures, gaze or tempo of
any kind. Write the line, put every question in FLAGS, and stop.

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied (scene map · choice · cost · final)
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated.

**MODE D** — the plan names the beat of every scene and the three anchor beats. You test whether each reached the body.

**MODE V** — no written SPEC supplied. Perform acting and performance analysis directly from the video footage. Evaluate character emotional expression, body posture, gesture legibility, physical strain, and performance consistency across cuts based strictly on direct visual evidence.

---

## 📋 BEAT & BODY LOCK LIST — MODE D ONLY

Read out of the supplied SPEC before you watch:

```
A BLOĞU → scene map: what happens in each scene · CENTRAL CHOICE (scene +
          second) · FAILED ATTEMPTS · CHOICES AFTER · INTENDED EMOTION ·
          THEME SCENES · ENDING TYPE
C BLOĞU → İNSAN (how many bodies) · KASK (is the face available? visor clear
          or opaque?) · EKRAN YÖNÜ (what "up" and "down" ARE — your gaze ruler)
GRID    → scene start times. ⛔ THE GRID IS GIVEN: one frame per scene at
          start + 5 s; a cut off the grid is reported, never re-numbered.
```

Write the three anchor beats before you watch:
`CHOICE at __ · COST at __ · FINAL at __`. You will freeze-frame each.

---

## ⛔ STEP 0 — THE CHANNEL REGISTER (both modes — before scoring anything)

```
CHANNEL REGISTER
· face              [visible / behind a clear visor — CU only / unavailable]
· eyes              [readable / not]
· hands             [bare / gloved — gloved hands still carry intent]
· posture · weight  [available whenever the torso is in frame]
· head · gaze       [available whenever the helmet is in frame]
· tempo             [always available]
· breath (visible)  [chest · visor fog · none]
· proximity         [distance to the object of the scene — always available]
```

⛔ **SCORE ONLY ON REGISTERED CHANNELS.** Face unavailable → category 1 is
`N/A`, not 1/10. A film that cannot show a face is not failing to show one.

⛔ **NAMING A CHANNEL IS NOT SCORING IT.** "Posture available" is not
"posture legible". Every deduction still needs a ledger row.

---

## STEP 1 — BUILD THE PERFORMANCE LEDGER (before judging anything)

One row per scene. **Write the sentence FIRST, from the screen, before you
read the plan's line for that scene.**

```
S<n> | in | THE SENTENCE — what a viewer would say the figure WANTS or FEELS
       here, from the body alone | channels carrying it | plan beat (D) |
       LEGIBLE · PARTIAL · ILLEGIBLE · TASK ONLY
```

- **TASK ONLY**: the only honest sentence is "he does X", with no wanting or
  feeling in it. **This is the most important cell in this report.**
- **PARTIAL**: the intention is there, but only if you already know the story.
- The sentence may not contain "seems", "probably", "I think". If it needs
  them, the row is PARTIAL at best.

### ⛔ THE CHOICE ON THE BODY — the only test this lens has

For each anchor beat — CHOICE · COST · FINAL — freeze one frame BEFORE and
one AFTER. Write in one line what is different about the body:

> *"Before: … After: …"*

If the honest answer is *"nothing"*, the beat is NOT ON THE BODY — whatever
the plan says happened, the screen did not perform it. **Write the sentence.**
A deduction with no attempted sentence is not a finding.

⛔ In mode D, freeze first, read second. The plan says "he decides" and you
will start seeing a decision that is not there.

### GAZE STRING

One character per scene, in edit order: `O` = head / gaze toward the object
of the scene's action · `A` = away from it · `D` = down · `U` = up ·
`-` = head not in frame. It is a fingerprint of attention. Read it against
the plan's up / down: a figure looking UP at the thing the plan puts BELOW
him is a finding, not a style.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

```
① MANNEQUIN — the body holds a pose with no micro-adjustment; alive the way
   a statue is alive.
② TASK WITHOUT INTENT — the hands complete the task; nothing before or
   after says the figure wanted it, feared it, or chose it.
③ THE UNCHANGED BODY AT THE CHOICE — before and after the decision are the
   same body.
④ EMOTION SPRAY — a generic emotive gesture (head shake, hand to helmet,
   slump) attached to no event in the scene.
⑤ TEMPO FLATLINE — every gesture at the same speed across the film; no
   hesitation, no rush.
⑥ GAZE NOWHERE — head orientation unrelated to the action: the camera, the
   wall, the middle distance.
⑦ PREMATURE RESOLUTION — the body relaxes before the outcome is known.
⑧ THE RESET — the next scene opens on a body that carries nothing from the
   last; the low point is followed by a neutral figure.
⑨ GESTURE LOOP — the same filler gesture (glove check, helmet touch) recurs
   as padding.
⑩ ACTING TO CAMERA — awareness of the lens in a film whose camera is meant
   to be unseen.
⑪ THE OVER-TOLD BEAT — the reverse error: a small moment performed with big
   theatre; the proportion is wrong.
```

⛔ Pattern ⑪ scores exactly like the others. This lens is not "more acting
is better". An oversized gesture is as false as an absent one.

---

## ═══ YOUR SCOPE ═══

```
✅ Whether wanting, deciding, feeling and their aftermath are legible on the
   body from the screen alone, at the tempo the moment needs, in proportion
   to the moment.
```

## ═══ NOT IN THIS PASS ═══

```
❌ Whether the work COST the body — strain, breath, fatigue   → the EFFORT lens
   (a strained lift with no intention is yours; an intended lift with no
    strain is theirs; a film can fail both)
❌ Whether the EVENT reads — what happened, contact, geography → the ACTION lens
❌ Whether the story on the PAGE works — structure, stakes     → the STORY lens
   (you never judge the plan; you judge whether it reached the screen)
❌ Whether it is the same figure, suit, wear                    → CONTINUITY
❌ Face artefacts, hand anatomy, morphing                        → the FRAME lens
❌ Where the camera stands                                        → the SETUP lens
❌ In mode V, anything you think the PLAN intended — FLAGS only.
```

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material takes `N/A` and leaves the mean.

### 1. 🙂 FACE & EYES (N/A whenever the register says unavailable)
```
□ Expression changes with the event, not on a schedule
□ Eyes go where the attention goes
□ No frozen expression held across a cut
```

### 2. ✋ HANDS AS INTENT
```
□ Hesitation is visible before a committed act — the hand stops, then goes
□ Release after the act is visible — the hand lets go, not just opens
□ Between tasks the hands do something that belongs to this person
□ No filler gesture recurs as padding (pattern ⑨)
```

### 3. 🧍 POSTURE & WEIGHT OF DECISION
```
□ Weight shifts before, at and after a choice
□ Stillness is held, not frozen (pattern ①)
□ The body after a failed attempt differs from the body before it
```

### 4. 👁️ GAZE DIRECTION
```
□ GAZE STRING agrees with the object of each scene
□ The head points toward the plan's "down" when the story is down there
□ No gaze to camera, wall or nowhere (patterns ⑥ ⑩)
```

### 5. ⏱️ TEMPO & STILLNESS
```
□ Speed varies with meaning across the film (pattern ⑤)
□ The slowest gesture is at the moment that matters most
□ A pause reads as a decision, not as a stalled clip
```

### 6. ⚖️ THE CENTRAL CHOICE ON THE BODY
```
□ Before and after the choice are two different bodies (pattern ③)
□ The difference is in a registered channel, not inferred from the plot
□ The choice reads without the title and without the plan
```

### 7. 💸 COST & AFTERMATH
```
□ The low point is on the body, not only in the situation
□ It is carried into the next scene (pattern ⑧)
□ The body does not relax before the outcome is known (pattern ⑦)
```

### 8. 🏁 FINAL BEAT LEGIBILITY
```
□ The last thing the figure does reads as a decision or a recognition
□ It differs from the first thing the figure did, in a nameable way
□ A viewer can say what the figure understood, from the body alone
```

### 9. 📏 PROPORTION
```
□ The size of the performance matches the size of the moment (patterns ④ ⑪)
□ No emotive gesture without an event to cause it
□ The biggest gesture of the film sits at its biggest moment
```

---

## OUTPUT FORMAT — use this exact structure

```
INPUT MODE: [D / V]
FILM: [name as stated by the operator, or "(not supplied)"]
RUNTIME: [mm:ss — "measured" or "~mm:ss ESTIMATED"]
FRAME RATE ASSUMED: [n fps]
GRID GIVEN: [hook s + (n−1) × clip s · from the SPEC — or "none (mode V)"]
SCENES OBSERVED: [n] · CUTS COUNTED: [n] · CUTS OFF GRID: [n · timecodes]
NON-SCENE MATERIAL: [in-out + what it is, or "none"]
PRESENCE STRING: [one character per scene — see below]
LINES HEARD: [n · verbatim with timecode, or "none — room tone present" /
             "none — nothing audible to me"]
             ⛔ This reports what you HEARD, never a property of the file.
CHANNEL REGISTER: [one line — the channels available, from STEP 0]
ANCHOR BEATS: CHOICE __ · COST __ · FINAL __   (mode D — from the SPEC)
SCENES TASK ONLY: [n · from the ledger]

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Exclude it from every
count and every string.
```

## PERFORMANCE LEDGER
[the full STEP 1 ledger with the sentence for every scene — this is evidence]

## THE CHOICE ON THE BODY
```
CHOICE  (S__ · __ s)  Before: …   After: …
COST    (S__ · __ s)  Before: …   After: …
FINAL   (S__ · __ s)  Before: …   After: …
```

## GAZE STRING
```
OBSERVED:  [one character per scene, in edit order, no spaces · O A D U -]
PLAN UP / DOWN: [what the SPEC names as up and down — mode D]
```
⛔ Length = SCENES OBSERVED. If they disagree, say so on this line.

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` if a human figure is
visible anywhere in that scene, `-` if none. You write this even though it is
not your subject — it is the one axis on which every lens of the same film is
checked against every other. In a single-figure film it is nearly constant
and proves little on its own; write it anyway.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**
Write the deduction's source as ledger rows with timecodes. A deduction with
no listed source is not applied. A category with material but no in-scope source is
written `—` and is not scored — it stays out of the mean. It never takes a silent
deduction. DO NOT TOTAL, AVERAGE OR TALLY ANYTHING — the library's script counts the
🔴/🟠/🟡 tags you wrote and computes the mean from the cells; a number you compute
yourself is discarded. No SEVERITY TALLY, no SUM, no OVERALL.

| # | Category | Score | Issue (ledger rows and timecodes) |
|---|----------|-------|-----------------------------------|
| 1 | Face & Eyes | /10 | |
| 2 | Hands as Intent | /10 | |
| 3 | Posture & Weight of Decision | /10 | |
| 4 | Gaze Direction | /10 | |
| 5 | Tempo & Stillness | /10 | |
| 6 | The Central Choice on the Body | /10 | |
| 7 | Cost & Aftermath | /10 | |
| 8 | Final Beat Legibility | /10 | |
| 9 | Proportion | /10 | |

Write the verdict UNDER the table, after every cell is filled — exactly one of the
options below (the library's script checks the word against this list):
VERDICT: [THE BODY TELLS IT / MOSTLY LEGIBLE / TASK WITHOUT FEELING /
          THE CHOICE IS INVISIBLE / MANNEQUIN]
         One finding outranks the mean: if THE CHOICE ON THE BODY returns
         "nothing" for the central choice, the verdict is THE CHOICE IS
         INVISIBLE regardless of the score.

## THE THREE THAT MATTER
The three findings that most damage this film's performance, in order, each
with its timecode and its one-line fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Intention is almost never fixable in the edit — say so plainly. A missing
aftermath sometimes is: hold a frame longer, or reorder so the body that
carries the cost arrives next.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, lens named.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The sentence is the whole method.** Every finding traces to "what does
  this body want, and can I say it without the plan?"
- **Freeze first, read second.** In mode D, always.
- **Face unavailable is not a fault.** Score the channels the film has.
- **More acting is not better.** Pattern ⑪ scores like the others.
- **Cost of the work is the EFFORT lens; meaning of the work is yours.**
