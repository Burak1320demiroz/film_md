# ⑬ UYUM QA — SCENE ↔ PROMPT CONFORMANCE CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑬ — **üretim sadakati** sınıfının ilk merceği.
> Kardeşleri plan sadakati ⑨-⑫'dir; onlar PLANI ekrana karşı okur, bu mercek
> **PROMPTU** ekrana karşı okur. Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri
> `qa-isle` skill'inden okunur.
> ⛔ Bu merceğin ürünü SONRAKİ FİLMİN DERSİDİR. Ölçülen filmin promptu asla
> güncellenmez; kaynak: `_KAYNAK/13` · kapı: F9 · tablo: `T13_UYUM_KALITE.md`.
>
> **16.09.2026 · REVİZYON — beş koşu, beş boş rapor.** ⑬ beş filmde koşuldu
> (THE_STATIC_SHADOW · THE_RESONANT_STRAND · LOOK_UP · MARS_SON_CIKIS ×2 ·
> KRONOS_SON_SINYAL); beşi de STEP −1'de durup yedi satır yazdı. Sebep bilgi
> eksikliği değil: rubrik DÖRT girdi istiyordu, sistem ise medya + TEK dosya
> yapıştırıyor. Bu sürümde:
> 1. Girdi ikiye indi — **kurgu + sahne promptları**. SPEC ve makine tablosu
>    VARSA okunur, yoksa koşu sürer ve eksiklik başlıkta yazılır. Promptsuz koşu
>    hâlâ KOŞU DEĞİLDİR (mod V yok) — ①.11 kapısı yerinde.
> 2. Promptlar **bölüm dosyası** olarak da yapıştırılabilir (`<FILM>_BOLUM_n.md`);
>    model 🎥 VİDEO PROMPT bloklarını kendisi ayıklar, Türkçe plan satırlarını
>    prompt saymaz.
> 3. Izgara kapısı bölümü tanır: yarım makara artık "TESLİM UYUŞMAZLIĞI" değildir.
> 4. Çıktı hacmi indi — sahne başına 10 satırlık defter ve 8 sütunlu SCENE SCORES
>    tablosu kaldırıldı (24 sahnede model hücre uyduruyordu); yerine sahne başına
>    TEK satır + **KİLİT DEFTERİ** geldi: sayılan her kilit bir satırdır.
> 5. Model artık BÖLMÜYOR: `LOCKS HELD ÷ LOCKS CHECKED` türetmesini T13 satırını
>    yazan ajan hesaplar (FAZ 1 ilkesi: model saymaz/bölmez, betik hesaplar).

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

## ⛔ STEP −3 — HOW THE PASTE ARRIVES (read before anything else)

You were given a video, this file, and — pasted above or below this text — one
or more of the film's own documents. Those documents are your only inputs: you
cannot open files, run scripts, or look anything up.

```
WHERE THE PROMPTS ARE — two legitimate shapes:

A) BARE PROMPTS between the markers in STEP −1, one block per scene, in order.

B) THE FILM'S CHAPTER / PRODUCTION FILE(S) pasted whole — one file, or two when
   the cut spans two chapters. Read them in the order pasted, like this:
   · a scene begins at a heading that carries its number (SAHNE 07 · S07 · SCENE 7)
   · the text under that scene's VIDEO PROMPT heading, up to the next horizontal
     rule, IS the prompt that produced the clip. This is the prompt you compare.
   · the text under its IMAGE PROMPT heading ordered the FIRST FRAME only.
   · the NEGATIVE line and the Output line belong to the prompt — they were sent
     with it. C4 is checked against the NEGATIVE line.
   · EVERY OTHER LINE IS PLAN, NOT PROMPT: planning notes, scene titles, timing
     tables, dialogue rows, VFX/edit notes, and any line written in another
     language. None of it reached the generator. ⛔ Never quote a plan line as a
     prompt line — a finding built on one is worse than no finding.
```

⛔ If a scene's heading exists but its VIDEO PROMPT block is absent, that scene
has NO prompt: it is not scored, its character in the string is `-`, and it is
named in OPEN QUESTIONS.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, scenes, strings or conformance
of any kind. Write the line, put every question in OPEN QUESTIONS, and stop.

---

## ⛔ STEP −1 — INPUT GATE: TWO REQUIRED, TWO OPTIONAL

```
① THE CUT          REQUIRED. The master video (a chapter or the whole film).
                   It lives outside the library; the operator uploads it.
② SCENE PROMPTS    REQUIRED. The prompt of every scene in this cut, VERBATIM —
                   bare (shape A) or inside the chapter file (shape B).
③ QA SPEC          OPTIONAL. The film's QA SPEC: declared design decisions.
④ MACHINE TABLE    OPTIONAL. sahne_kapisi.sh output + production-notebook rows
                   (as-built deviations · seeds · SHA-256 · scene count).

INPUT MODE: D        ① and ② are present → the run proceeds.
INPUT MODE: MISSING  ② is absent → THE RUN STOPS HERE.
```

⛔ **THIS LENS HAS NO MODE V.** Every other lens can look at a video and say
something. This one cannot: with no prompt text there is nothing to conform to,
and a lens that invents the prompt from the screen will agree with the screen
every time. If ② is absent, write exactly this and nothing else:

```
INPUT MODE: MISSING — no scene prompts were supplied.
This lens compares the screen with the text that was sent to the generator.
Paste the scene prompts (or the chapter file that contains them) and run again.
```

**What changes when an OPTIONAL input is absent — write it, then continue:**

```
no QA SPEC       → `SPEC: not supplied` in the header. You may not call a
                   repeated choice a fault on the suspicion that it was
                   undeclared; the firewall list below is your only declaration
                   list, and questions of intent go to OPEN QUESTIONS.
no MACHINE TABLE → `SCENE COUNT SOURCE: counted from cuts` in the header. Count
                   the scenes yourself from the cuts. You may not report a
                   seed, a SHA-256 or an as-built deviation: write
                   `AS-BUILT DEVIATIONS DECLARED: unknown (no machine table)`.
                   ⛔ Never invent a machine number. A number with no source is
                   the one thing this lens exists to stop.
```

```
<<<SCENE_PROMPTS

>>>

<<<MACHINE_TABLE

>>>
```

**Your report header must state: mode, which inputs arrived, runtime, scene
count and its source, cuts counted, prompts supplied, and the scene range.**
A run whose header is missing is not a run.

---

## ⛔ STEP 0 — GRID GATE (before you look at a single frame)

```
SCENES OBSERVED : __        PROMPTS SUPPLIED : __        SCENE RANGE : S__–S__
```

```
EQUAL                 → run every scene.
FEWER PROMPTS, and they align with a contiguous stretch of the cut
                      → this is a CHAPTER RUN and it is normal: the QA unit of a
                        long film is a chapter or a half. Review the covered
                        scenes, write `-` for the rest of the string, and state
                        the covered range in the header.
MORE PROMPTS than scenes, aligning from the first scene
                      → the cut is shorter than the chapter. Same treatment:
                        review what is on screen, name the uncovered prompts in
                        OPEN QUESTIONS.
NO ALIGNMENT          → write exactly one finding, `DELIVERY MISMATCH`, state
                        both numbers and what the first mismatching scene shows,
                        and stop the run.
```

⛔ Alignment is decided on CONTENT, never on the numbers alone: check the FIRST,
the MIDDLE and the LAST scene of the cut against the prompt you believe belongs
to it. If those three land, the stretch is aligned. Two films have already been
reviewed frame by frame against a plan that was not the film on screen; every
finding from such a run is unusable.

---

## 🚫 FALSE-POSITIVE FIREWALL — read BEFORE watching

A design decision that the SPEC **declares** is not a fault. If a SPEC was
supplied, read it first and list what it declares. These constraints hold in
this library whether or not a SPEC arrived:

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

## STEP 1 — THE OBSERVED LEDGER: ONE ROW PER SCENE

Watch the cut once and write what is on screen — one row per scene, fields in
the fixed order of the table in OUTPUT FORMAT.

⛔ **WRITE THE ROW BEFORE YOU LOOK UP THAT SCENE'S PROMPT.** The prompts are in
front of you and you cannot unsee them, so the discipline is procedural: never
copy a noun out of the prompt into an observation cell unless you can point at
it on screen. A ledger written from the prompt is a description of the prompt,
and it will agree with the prompt in every row.

```
what happens        ≤ 12 words, plain, no adjectives of quality
humans in frame     a number, plus what distinguishes them
countable objects   only what a prompt would count: legs, pads, lamps,
                    brackets, tools, lines, hatches, figures
camera              scale (EWS/WS/MS/CU) · low / eye / high · does it move?
text on screen      yes (what) / no
audio               every sound you hear, dialogue as "quote" (mm:ss)
```

---

## STEP 2 — PULL THE LOCKS OUT OF THE PROMPT (this is the measurement)

A **lock** is a fragment of the prompt that the screen can answer yes or no to:

```
a count        "exactly four legs" · "two brackets" · "one hatch"
a time window  "from 7 to 10 seconds the hatch swings open"
a forbidden    anything in the NEGATIVE line: "no text", "no camera shake"
a state        "the sling is on the left arm" · "the case is on the sled"
a camera word  "locked macro, no camera movement" · "35mm wide"
a readable     "the number reads" · "fully readable through the visor"
an audio item  a sound the prompt orders, or silence it orders
```

```
· AT MOST SIX LOCKS PER SCENE — the six the scene is about.
· NOT a lock, and skipping them is correct: mood and quality words
  ("cinematic", "photorealistic", "crisp textures"), lighting adjectives,
  anything you cannot resolve at normal viewing size.
⛔ EVERY LOCK YOU COUNT IS A ROW IN THE LOCK LEDGER. LOCKS CHECKED is the number
  of rows in that table — not a number you estimate. If you did not write the
  row, you did not check the lock.
```

⭐ **TWO PROMPTS, ONE SCENE.** Where a first-frame (IMAGE) prompt exists beside
the clip (VIDEO) prompt, compare them: a lock that lives ONLY in the first-frame
prompt is a 🅑 PROMPT GAP the moment the screen loses it after the first second.
A state the clip prompt never repeats — an injury, a stain, a sling, a helmet in
the hand — is the most common gap in this library, and the model is not at fault
for dropping what it was never told to keep.

---

## STEP 3 — ATTRIBUTION GATE (run for every lock that did not hold)

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

🅒 NOT A FINDING   screen matches the prompt, or the item is on the firewall,
                   or it came from the edit and not from the generator — a
                   spoken line that matches a dialogue row of the plan was laid
                   in afterwards: log it in LINES HEARD, do not score it.

🅓 UNATTRIBUTED    an as-built deviation was declared for this scene and the
                   sent text is not available, or no machine table arrived and
                   the scene's prompt may have been edited before sending.
                   State it; do not guess.
```

```
⛔ QUOTE RULE. A finding with no quoted prompt line (🅐) and no "instead" line
   (🅑) is DROPPED at the report gate — the script checks this. Quotation is
   what separates this lens from an opinion.
⛔ SECOND RULE. Every finding carries a SECOND (or a range). "Late in the scene"
   is not a time. Adjectives are not measurements.
```

---

## 🔧 CATEGORIES — every lock belongs to exactly one

```
C1  COUNTABLE OBJECTS
    The prompt says "exactly four legs", "two brackets", "one hatch". Count
    them on screen. A count that cannot be resolved is `?`, not a guess.

C2  CAMERA SETUP AS WRITTEN
    Lens / distance / height / angle words versus what the frame shows. Use
    proxies you can see: where the horizon sits, what fraction of frame height
    the subject occupies, whether the camera is below, at, or above eye level,
    and whether a prompt that says "locked" holds still.

C3  TIMELINE BEATS
    Does each beat named in the prompt happen, in order, at roughly its stated
    second? Missing beat · beat at the wrong time · a beat the prompt never
    asked for.
    ⭐ These prompts usually carry three windows (0-3 s · 3-7 s · 7-10 s). Check
    the LAST one specifically: if the closing window names an action and the
    screen holds still, that is a finding here — the beat was ordered and not
    delivered. Say whether the prompt named an action for it at all; if it did
    not, the stillness is a 🅑 PROMPT GAP.

C4  FORBIDDEN ITEMS ON SCREEN  ⭐ hardest category
    ⛔ Do not name this row "negative violations": in this library that exact
       phrase is a COUNTING row belonging to lens ①, and the report-check
       script drops it out of every average. Use the name given here.
    Anything the NEGATIVE line forbids and the screen shows. Count each
    violation separately and quote the forbidding phrase. If the negative block
    is SHORT or missing, that is a 🅑 PROMPT GAP, not a low model score.
    ⭐ A prompt that forbids text while its own body orders readable words or
    digits on a display is contradicting itself: report it here as 🅑, quoting
    both halves.

C5  CONTINUITY CARRIERS AND COUNTERS
    The state the prompt assigned to this scene: a bracket empty or full, a dust
    line higher than before, a case on the sled or on the ground, an injury, a
    stain, which arm carries the sling. Is that state on screen, at that value?

C6  LEGIBILITY OF WHAT THE PROMPT CALLS READABLE
    Where the prompt says "reads", "visible", "fully readable through", check
    that it reads at normal viewing size. An object the scene was built around
    that occupies a handful of pixels is a finding.

C7  UNREQUESTED ADDITIONS
    On screen but in no prompt: a second figure, an extra object, weather,
    equipment, on-screen text, and ⭐ SPOKEN LINES that match nothing in the
    plan. Dialogue that appears in no prompt AND in no plan row is a 🔴 finding
    and it is reported here, not under audio.

C8  SOUND AND TEXT DISCIPLINE
    The audio inventory the prompt asks for versus what is heard; zero readable
    text, captions, title cards or watermarks anywhere in frame.
```

---

## 🧮 SEVERITY AND THE CONFORMANCE COUNT

```
· Severity: 🔴 BLOCKER (breaks a lock or the point of the shot) ·
  🟠 MAJOR (visible, cheapens the shot) · 🟡 MINOR (only on close look).
· A 🔴 tagged 🅑 PROMPT GAP does NOT lower the model's score — it lowers the
  PROMPT's. Report it in the same table and say so in one clause.

CONFORMANCE COUNT — the primary number of this lens:
  LOCKS CHECKED   rows in the LOCK LEDGER
  LOCKS HELD      rows whose `held?` cell is Y
⛔ Do not divide and do not write a derived score: the library's script and its
  operator compute that from your two counts. A `?` row counts in neither.
```

### VERDICT — one per scene, choose exactly one

```
ACCEPT              no 🔴; at most two 🟠 the edit can hide.
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

⛔ There is no scene score table in this report. The per-scene result is the
CONFORMANCE STRING and nothing else — eight invented cells per scene is what
this lens used to produce instead of evidence.

---

## OUTPUT FORMAT — use this exact structure, and write nothing outside it

No introduction, no closing summary, no restatement of the prompts, no advice
about the film's story. Every heading below appears once, in this order.

```
# HEADER
INPUT MODE: D
FILM: ____
INPUTS: prompts ✓ · SPEC ✓/✗ · machine table ✓/✗
RUNTIME: __._ s
SCENES OBSERVED: __
CUTS COUNTED: __
PROMPTS SUPPLIED: __
SCENE RANGE: S__–S__   (or: whole film)
SCENE COUNT SOURCE: machine table / counted from cuts
AS-BUILT DEVIATIONS DECLARED: none / S__ , S__ / unknown (no machine table)
LINES HEARD: none  /  __ · "quote" (mm:ss) · (matches plan row: yes/no)

# CONFORMANCE STRING
OBSERVED: `__________`
⛔ Write it on an `OBSERVED:` line exactly as above — the report-check script
  reads this line and nothing else. One character per scene, in edit order,
  no spaces:
      K = accept · T = fix in edit · P = lock for next film ·
      Y = regenerate · - = no prompt / could not measure
⛔ Length must equal SCENES OBSERVED.

# OBSERVED LEDGER
| scene | start | what happens | humans | countable objects | camera | text | audio |
(one row per scene, written before that scene's prompt was read)

# LOCK LEDGER
| scene | lock (quoted from the prompt, ≤10 words) | cat. | held? | second |
(≤6 rows per scene · held? = Y / N / ? · every counted lock is a row)

# CONFORMANCE LEDGER
| scene | second | what is on screen | prompt line (quoted) | tag | severity | category |
(only the rows whose `held?` was N, expanded with attribution)

# ATTRIBUTION SUMMARY
🅐 MODEL DRIFT: __ · 🅑 PROMPT GAP: __ · 🅒 NOT A FINDING: __ · 🅓 UNATTRIBUTED: __

# LESSON ORDERS (for the NEXT film — 🅑 findings only · at most 8 rows)
| # | what the screen did | what the prompt never said | the lock to write next time |
⛔ NO SCENE NUMBER ANYWHERE IN THE ROW — not in the lock, not in the evidence —
  and no film name: the library's script drops a row that contains `S07`. Use a
  timecode if you need a trace. Each row must be usable by someone who has never
  seen this film, and the lock is written POSITIVELY: what the next prompt SAYS,
  not what it must avoid.

# CONFORMANCE COUNT
LOCKS CHECKED: __ · LOCKS HELD: __
(LOCKS CHECKED = rows in the LOCK LEDGER · LOCKS HELD = its Y rows · do not divide)

# SCORES SUMMARY
⛔ EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.
  ① The film-level cell is the WORST scene's value for that category, never an
     average of averages. Its Issue cell names the scene and the second.
  ② ONE OBSERVATION, ONE PLACE: a finding lowers ONE category, chosen by root
     cause; a question for the document lowers nothing.
  ③ A category with no in-scope source is written `—` and is not scored — it
     stays out of the mean. It never takes a silent deduction.
  ④ DO NOT TOTAL, AVERAGE OR TALLY ANYTHING — the library's script counts the
     🔴/🟠/🟡 tags you wrote and computes the mean from the cells. No SEVERITY
     TALLY, no SUM, no OVERALL.

| # | Category | Score | Issue (with scene, second and tag) |
|---|----------|-------|-------------------------------------|
| 1 | Countable objects | /10 | |
| 2 | Camera setup as written | /10 | |
| 3 | Timeline beats | /10 | |
| 4 | Forbidden items on screen | /10 | |
| 5 | Continuity carriers | /10 | |
| 6 | Legibility | /10 | |
| 7 | Unrequested additions | /10 | |
| 8 | Sound and text | /10 | |

⛔ **"NO FAULT" IS EITHER 10/10 OR `—`, NEVER 7** [D186]. Every score below 10
  carries its reason in the Issue column with a source trace: a second, a scene
  number, or a ledger row. A score whose Issue column is empty, "none" or "—" is
  stripped by the script and leaves the average.
⛔ **WRITE THE SOURCE TRACE AS `mm:ss` OR `S__`.** The script recognises those two
  shapes and nothing else; "14.0 s dust above the hull" reads to it as a
  deduction with no source and the row is flagged. Write `0:14 dust above the
  hull (S01)` instead.
⛔ This lens writes NO film-level VERDICT line: its verdicts are per scene and
  they live in the CONFORMANCE STRING.

# OPEN QUESTIONS
(anything you could not verify, and what would settle it: a missing prompt
block, an intent only the SPEC could declare, a number only the machine table
carries)
```

---

## ⛔ WHAT THIS LENS NEVER DOES

```
⛔ It never proposes an edit to the prompts of the film under review. Those
   prompts are the evidence that produced these frames; changing them destroys
   the only record of what was actually asked for.
⛔ It never quotes a plan line — a title, a dialogue row, a note — as a prompt
   line. Only the text inside the prompt block was sent.
⛔ It never writes a cut list and never orders a REMOVE. Trimming is ④'s and
   ⑫'s business; you only say whether a fault is trimmable.
⛔ It never invents a lock, a seed, a SHA or a scene count. If a number is not in
   the prompt, the SPEC or the machine table, you have no number for it — the
   observation goes to OPEN QUESTIONS.
⛔ It never scores a scene whose prompt was not supplied.
⛔ It never counts a lock it did not write down.
⛔ It never searches a repository. Everything is in this file and in what the
   operator pasted.
```
