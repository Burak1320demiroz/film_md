# ⑬ UYUM QA — SCENE ↔ PROMPT CONFORMANCE CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑬ — **üretim sadakati** sınıfının ilk merceği.
> Kardeşleri plan sadakati ⑨-⑫'dir; onlar PLANI ekrana karşı okur, bu mercek
> **PROMPTU** ekrana karşı okur. Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri
> `qa-isle` skill'inden okunur.
> ⛔ Bu merceğin ürünü SONRAKİ FİLMİN DERSİDİR. Ölçülen filmin promptu asla
> güncellenmez; kaynak: `_KAYNAK/13` · kapı: F9 · tablo: `T13_UYUM_KALITE.md`.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **SCENE ↔ PROMPT CONFORMANCE**: for
every scene of the cut, you compare what is ON SCREEN against the exact prompt
text that was sent to the generator for that scene.

You answer three questions and only three:

```
① CONFORMANCE   Does the scene on screen match the prompt written for it?
② ATTRIBUTION   For every mismatch: did the MODEL disobey a line that was in
                the prompt, or was the lock NEVER IN THE PROMPT at all?
③ DECISION      Accept · fix in edit · lock it for the NEXT film · regenerate?
```

Question ② is the reason this file exists. Every other lens can tell you a shot
is wrong. None of them can tell you **whose fault it is**, so every fault ends
up as the same word — "REGENERATE" — and the same money is burned twice:
regenerating from a prompt that never carried the lock reproduces the fault.

⛔ This lens is not the frame lens and not the camera lens. They ask what is
wrong in the picture. You ask whether the picture is the one that was ordered.

⭐ **THE PRODUCT OF THIS LENS IS A LESSON, NOT A REPAIR ORDER.** The film you
are reviewing is finished; its prompts are evidence and will not be edited. Your
🅑 findings become locks for the NEXT film's prompt-writing standard. Write them
so a person who has never seen this film can apply them.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, scenes, strings or conformance
of any kind. Write the line, put every question in OPEN QUESTIONS, and stop.

---

## ⛔ STEP −1 — INPUT GATE: FOUR INPUTS, ALL REQUIRED

```
INPUT MODE: D   → the four inputs below were supplied
INPUT MODE: MISSING → one or more is absent. THE RUN STOPS HERE.
```

⛔ **THIS LENS HAS NO MODE V.** Every other lens can look at a video and say
something. This one cannot: with no prompt text there is nothing to conform to,
and a lens that invents the prompt from the screen will agree with the screen
every time. If input ② or ④ is missing, write `INPUT MODE: MISSING`, name what
is absent, and write nothing else.

```
① THE CUT            the master video (a chapter or the whole film). Required.
                     ⛔ The file lives OUTSIDE the repository — this library
                     stores prompts and measurements, never media. The operator
                     uploads it to you; the repo only ever holds its SHA-256.
② SCENE PROMPTS      the prompt of every scene in this cut, VERBATIM, in order,
                     between the markers below. Required.
③ QA SPEC            the film's <FILM>_QA_SPEC.md. Required — it carries the
                     declared design decisions (the firewall reads it).
④ MACHINE TABLE      the output of sahne_kapisi.sh + the matching rows of
                     <FILM>_URETIM_DEFTERI.md (as-built deviations · seeds).
                     Required. You do not count scenes yourself; the machine
                     counted them and you inherit that count.

<<<SCENE_PROMPTS

>>>

<<<MACHINE_TABLE

>>>
```

**Your report header must state: mode, runtime, scene count, cuts counted, and
whether an as-built deviation was declared for any scene.** A run whose header
is missing is not a run.

---

## ⛔ STEP 0 — GRID GATE (before you look at a single frame)

```
SCENES OBSERVED (from the machine table) : __
PROMPTS SUPPLIED                          : __
```

If these two numbers differ, **stop**. Write exactly one finding —
`DELIVERY MISMATCH` — state both numbers, and stop the run. Do not score, do not
attribute, do not guess which prompt belongs to which scene. Two films have
already been reviewed frame by frame against a plan that was not the film on
screen; every finding from such a run is unusable.

---

## 🚫 FALSE-POSITIVE FIREWALL — read BEFORE watching

A design decision that the SPEC **declares** is not a fault. Read input ③ first
and list what it declares. Typical declared constraints in this library:

```
· fixed lock-off camera, zero movement, one setup repeated across scenes
· a fixed clip grid (every scene the same length) and no intra-scene cuts
· zero dialogue — silence is designed, not missing
· a designed silent stretch, or music that stops before the climax
· soft-edged shadows with real fill (thin-atmosphere cards) — not a lighting fault
· a textless counter (an object that changes state between cuts) instead of text
· deliberate stillness: a scene where nothing moves is a scene, not dead air
⛔ None of these may be written as a finding. If the SPEC declares it, it is
   the design. You may still note it under OPEN QUESTIONS if it looks harmful.
```

⛔ **AN UNVERIFIABLE CHECK CARRIES NO NUMBER.** If you cannot see it, the
category is N/A, carries no score, and enters no average. N/A is a correct
answer; a guessed number is not.

⛔ **ON-SCREEN TEXT IS NEVER EVIDENCE OF IDENTITY.** If a title card, caption or
watermark appears, that is itself a finding — never use it to confirm which
scene or which film you are watching.

---

## STEP 1 — BUILD THE OBSERVED LEDGER (before you read the prompts)

Watch the cut once and write what is on screen. **Do not open the prompts while
you do this.** Then compare. A ledger written with the prompt in view is a
description of the prompt, not of the film.

```
LEDGER — one block per scene, every line filled
  scene / start time            S__ · __._ s
  what happens                  one sentence, plain
  humans in frame               __  (and what distinguishes them)
  countable objects             list every object the prompt would count
                                (legs, pads, lamps, brackets, tools, lines)
  camera read                   scale (EWS/WS/MS/CU) · high / eye / low ·
                                does the frame move at any point?
  beats with times              0.0s … / __s …
  light                         how many sources · direction of shadows
  audio                         every sound you hear
  on-screen text                yes / no
  first frame vs last frame     what changed, and what did NOT
```

---

## STEP 2 — ATTRIBUTION GATE (run for every mismatch)

For each difference between the ledger and the prompt, assign exactly one tag.

```
🅐 MODEL DRIFT     the lock IS in the prompt for that scene and the screen
                   disobeys it.
                   → to claim this you must QUOTE the prompt line.
                   → meaning: regenerating with the same prompt MAY fix it.

🅑 PROMPT GAP      the lock is absent, weakened or paraphrased in the prompt.
                   → to claim this you must state what the prompt says INSTEAD,
                     or write "no corresponding line".
                   → meaning: regenerating with the same prompt REPRODUCES the
                     fault. This tag is the one that becomes a LESSON.

🅒 NOT A FINDING   screen matches the prompt, or the item is on the firewall.

🅓 UNATTRIBUTED    an as-built deviation was declared for this scene and the
                   sent text is not available. State it; do not guess.
```

```
⛔ QUOTE RULE. A finding with no quoted prompt line (🅐) and no "instead" line
   (🅑) is DROPPED at the report gate — the script checks this. Quotation is
   what separates this lens from an opinion.
⛔ SECOND RULE. Every finding carries a SECOND (or a range). "Late in the scene"
   is not a time. Adjectives are not measurements.
```

---

## 🔧 CATEGORIES — score each 0-10, or N/A, PER SCENE

```
C1  COUNTABLE OBJECTS
    The prompt says "exactly four legs", "two brackets", "one hatch". Count
    them on screen. A count that cannot be resolved is N/A, not a guess.

C2  CAMERA SETUP AS WRITTEN
    Lens / distance / height / angle words in the prompt versus what the frame
    shows. Use proxies you can actually see: where the horizon sits in frame,
    what fraction of frame height the subject occupies, whether the camera is
    below, at, or above the subject's eye.

C3  TIMELINE BEATS
    Does each beat named in the prompt happen, in order, at roughly its stated
    second? Missing beat · beat at the wrong time · a beat the prompt never
    asked for — all belong here.

C4  FORBIDDEN ITEMS ON SCREEN  ⭐ hardest category
    ⛔ Do not name this row "negative violations": in this library that exact
       phrase is a COUNTING row belonging to lens ①, and the report-check
       script drops it out of every average. Use the name given here.
    Anything the prompt's NEGATIVE block forbids and the screen shows. Count
    each violation separately and quote the forbidding phrase. If the negative
    block is SHORT or missing entirely, that is a 🅑 PROMPT GAP, not a low
    model score — say so in the same line.

C5  CONTINUITY CARRIERS AND COUNTERS
    The scene's own anchor: the state the prompt assigned to it (a bracket
    empty or full, a dust line higher than before, a case on the sled or on the
    ground). Is that state on screen, at that value?

C6  LEGIBILITY OF WHAT THE PROMPT CALLS READABLE
    Where the prompt says "reads", "visible", "fully readable through", check
    that it actually reads at normal viewing size. An object the prompt built
    the scene around that occupies a handful of pixels is a finding.

C7  UNREQUESTED ADDITIONS
    On screen but in no prompt: a second figure, an extra object, weather,
    equipment, on-screen text, and ⭐ SPOKEN LINES. Dialogue that appears in no
    prompt is a 🔴 finding and it is reported here, not under audio.

C8  SOUND AND TEXT DISCIPLINE
    The audio inventory the prompt asks for versus what is heard; zero readable
    text, captions, title cards or watermarks anywhere in frame.
```

---

## 🧮 SCORING AND THE CONFORMANCE COUNT

```
· Score only what you can see. Unverifiable → N/A, no number, no average.
· Severity: 🔴 BLOCKER (breaks a lock or the point of the shot) ·
  🟡 MAJOR (visible, cheapens the shot) · 🟢 MINOR (only on close look).
· A 🔴 tagged 🅑 PROMPT GAP does NOT lower the model's score — it lowers the
  PROMPT's. Report it in the same table and say so in one clause.

CONFORMANCE COUNT — the primary number of this lens:
  LOCKS CHECKED   every countable, timed or forbidden item you could verify
  LOCKS HELD      how many of them the screen honoured
  DERIVED SCORE   LOCKS HELD ÷ LOCKS CHECKED × 10, one decimal
⛔ The derived score is computed from the count. Do not write a score first and
   a count afterwards; the count is the measurement, the score is its shadow.
```

### VERDICT — one per scene, choose exactly one

```
ACCEPT              no 🔴; at most two 🟡 the edit can hide.
FIX IN EDIT         the fault is trimmable or maskable inside the clip
                    (state the trim in seconds).
LOCK FOR NEXT FILM  at least one 🔴 tagged 🅑 PROMPT GAP. This film is finished
                    and will NOT be re-prompted; the lock goes to the next
                    film's standard. Write the lock as one sentence a prompt
                    writer can paste.
REGENERATE          at least one 🔴 tagged 🅐 MODEL DRIFT with the lock provably
                    present in the prompt — the same prompt may produce a clean
                    take. (Only meaningful while the film is still in production.)
```

---

## OUTPUT FORMAT — use this exact structure

```
# HEADER
INPUT MODE: D
FILM: ____
RUNTIME: __._ s          (from the machine table)
SCENES OBSERVED: __
CUTS COUNTED: __
PROMPTS SUPPLIED: __
AS-BUILT DEVIATIONS DECLARED: none / S__ , S__
LINES HEARD: none  /  __ · "quote" (mm:ss)

# CONFORMANCE STRING
OBSERVED: `__________`
⛔ Write it on an `OBSERVED:` line exactly as above — the report-check script
  reads this line and nothing else. One character per scene, in edit order,
  no spaces:
      K = accept · T = fix in edit · P = lock for next film ·
      Y = regenerate · - = could not measure
⛔ Length must equal SCENES OBSERVED.

# OBSERVED LEDGER
(every scene block from STEP 1)

# CONFORMANCE LEDGER
| scene | second | what is on screen | prompt line (quoted) | tag | severity | category |

# ATTRIBUTION SUMMARY
🅐 MODEL DRIFT: __ · 🅑 PROMPT GAP: __ · 🅒 NOT A FINDING: __ · 🅓 UNATTRIBUTED: __

# LESSON ORDERS (for the NEXT film — 🅑 findings only)
| # | what the screen did | what the prompt never said | the lock to write next time |
⛔ Each row must be usable by someone who has not seen this film. No film name
  in the lock sentence, no scene number, no "as in S07".

# CONFORMANCE COUNT
LOCKS CHECKED: __ · LOCKS HELD: __ · DERIVED SCORE: _._ / 10

# SCORES SUMMARY
| # | category | score | issue (one line, or "—") |
| 1 | Countable objects | _/10 | |
| 2 | Camera setup as written | _/10 | |
| 3 | Timeline beats | _/10 | |
| 4 | Forbidden items on screen | _/10 | |
| 5 | Continuity carriers | _/10 | |
| 6 | Legibility | _/10 | |
| 7 | Unrequested additions | _/10 | |
| 8 | Sound and text | _/10 | |


⛔ This table is the library's contract — the report-check script reads the
  category names exactly as written. Do not total, average or tally anything:
  the script computes the mean from the cells and recounts the tags. A category
  you could not verify is written `N/A` and enters no mean. The film-level
  category score is the worst scene's score for that category, not an average
  of averages.

⛔ **"NO FAULT" IS EITHER 10/10 OR `—`, NEVER 7** [D186]. Every score below 10
  must carry its reason in the issue column, with a source trace: a second, a
  scene number, or a ledger row. A score whose issue column is empty, "none" or
  "—" is stripped by the script and leaves the average — a clean axis that was
  written lazily reads as an unmeasured one, and the category disappears.

⛔ **WRITE THE SOURCE TRACE AS `mm:ss` OR `S__`.** The script recognises those two
  shapes and nothing else; "14.0 s dust above the hull" reads to it as a
  deduction with no source and the row is flagged. Write `0:14 dust above the
  hull (S01)` instead. Same fact, one shape the gate can see.

# SCENE SCORES
| scene | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | verdict |

# OPEN QUESTIONS
(anything you could not verify, and what would settle it)
```

---

## ⛔ WHAT THIS LENS NEVER DOES

```
⛔ It never proposes an edit to the prompts of the film under review. Those
   prompts are the evidence that produced these frames; changing them destroys
   the only record of what was actually asked for.
⛔ It never writes a cut list and never orders a REMOVE. Trimming is ④'s and
   ⑫'s business; you only say whether a fault is trimmable.
⛔ It never invents a lock. If a number is not in the prompt or the SPEC, you
   have no number for it — the observation goes to OPEN QUESTIONS.
⛔ It never scores a scene whose prompt was not supplied.
⛔ It never searches a repository. Everything is in this file and in what the
   operator pasted.
```
