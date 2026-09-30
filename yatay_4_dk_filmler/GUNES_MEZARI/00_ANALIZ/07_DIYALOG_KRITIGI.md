# 🎙️ GUNES_MEZARI — DIALOGUE CRITIQUE (pre-production)

**Rubric:** `PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md` · run 26.09.2026 · text only
**Why it ran:** the film has spoken words, so the replik gate chain is open
(`SES_VE_DIYALOG` §1a-§2a). ⛔ Not a score — labels and one verdict.

```
INPUT MODE: FULL
  A. STORY SPINE   ✅ B5 in GUNES_MEZARI_PLAN.md (WANT · OBSTACLE · PRICE K17/K20 · WITNESS)
  B. DIALOGUE TABLE ✅ GUNES_MEZARI_QA_SPEC.md 🅐 + GUNES_MEZARI_MUZIK.md §replik
  C. SCENE PROMPTS  ✅ BOLUM_1 K03 · BOLUM_2 — quoted lines present
LINES FOUND: 2 in prompts · 2 in table   (no mismatch)
  ⚠️ NOTE: both occurrences are the SAME recorded line, not two written lines.
    One line, two hearings. The rubric judges it as two slots.
```

## DIALOGUE LEDGER

| # | scene | second | speaker | register | quoted line | words | function claimed | function observed |
|---|---|---|---|---|---|:--:|---|---|
| 1 | S01 · K03 | 24.0 | recording (not present) | HUMAN · recording via cabin speaker | "There are children here. Please give the light back." | 9 | WANT pressure / inciting | **OBSTACLE + WITNESS** — it names what the job is for, and it is the only voice the film has. `FUNCTIONAL · SUBTEXT · DISTINCT · FIT · SPEAKABLE · FIRST-LINE (on beat)` |
| 2 | S03 · K10 | 90.0 | same recording, looping | HUMAN · recording off stone | "There are children here. Please give the light back." | 9 | second hearing, loudest | **WITNESS** — the room that made the request is empty and the loop was never switched off. `FUNCTIONAL · SUBTEXT · SPEAKABLE` |

## FINDINGS BY TEST

**T1 · FUNCTION.** Delete slot 1: the film loses its only statement of what the
work is for, and K23's empty street loses the thing it answers — the request.
Delete slot 2: the tower scene becomes a room with a lamp in it; the loop is what
proves nobody is alive to stop it. Both `FUNCTIONAL`.
⚠️ Slot 2 was one step from `REDUNDANT`: an identical line, heard again, is only
information if something around it changed. What changed is written and audible —
the source is now in the room, the room is empty, and (added this pass) the last
word clips off before the loop restarts. Without that clip the milder label would
not have been earned.

**T2 · ON-THE-NOSE.** "There are children here" is a fact. "Please give the light
back" is a request. No emotion is named anywhere: not afraid, not alone, not sorry.
`SUBTEXT` both slots. No `THINKING-OUT-LOUD` — the line is addressed to someone.
No `CLIMAX-DIRECT` is spent, and the climax (K21) has no speech at all.

**T3 · EXPOSITION.** One new fact per sentence; nothing is explained. And the
information arrives inside resistance in the strongest available way: it accuses
the person hearing it. She is the one who took the light, and the line asks her
for it without knowing she is listening. No `LECTURE`, no `AS-YOU-KNOW` (there is
no second speaker), no `OVERLOADED`.

**T4 · VOICE.** Swap test against the film's only other possible register
(MACHINE): a machine in this repo speaks agentless, terse, numeric — it does not
say "please", and it does not say "here". The line cannot move. `DISTINCT`.

**T5 · REGISTER FIT.** HUMAN: verb-heavy, no numbers, no units, a request rather
than a readout. `FIT`. No `MISPLACED-NUMBER` — every number in this film lives in
the prompt body, never in a mouth.

**T6 · NATURALNESS.** Nine words, two short sentences, one of them a fragment of
politeness. "give the light back" is the spoken order (a written English would
have said "give back the light"). No calque, no hyper-formality, no relative
clause. `PASS`.
⚠️ Translation note, recorded honestly: the owner's treatment wrote this line in
Turkish. The English is what the prompt carries, because the prompt is what
generates the audio and the channel is English. The Turkish original is kept in
`GUNES_MEZARI_MUZIK.md` as a deviation record [D74 pattern].

**T7 · ECONOMY & SPEAKABILITY.** Read aloud with its pause: ~3.5 s. Slot 1 sits
inside the 4.0-8.0 s window of a 10 s clip, slot 2 starts at 0.0 s and the clip
runs 10 s. No line fills a clip; one speaker; no overlap. `SPEAKABLE` both.

**T8 · PLACEMENT & IRONY.**
`FIRST-LINE` — the first words of the film arrive at 24.0 s, on the reaction clip
that closes S01, and land on a structural beat: the call starts and she does not
flinch. Not wasted.
`IRONY-BREAK` — the package declares a window: the audience learns at K11 what she
has known all along. The line sits inside that window and does NOT name the hidden
fact. It says the light was taken; it never says by whom. The window survives, and
the second hearing at 90.0 s is the last beat before the window closes. This is
the rubric's PASS shape, not a violation.
`EARLY-EMBODIMENT` — no speaking mouth anywhere in the film. Her mouth is visible
behind a clear visor in 4 clips and is closed in all of them; the only voice is a
recording of someone who is not in the frame. The authority of the voice is never
spent. ⭐ This is the film's strongest dialogue decision.

## REWRITE LIST
```
(empty — no line failed a test)
```

## CUT LIST
```
(empty — deleting either slot removes a spine element; proofs under T1)
```

## SILENCE CANDIDATES
```
(none. The film is already 22 of 24 clips silent, the climax is silent, and the
last 30 s are silent. There is nothing here that an action would do better —
the one thing a picture cannot do is ASK.)
```

## THE THREE THAT MATTER

```
① THE SECOND HEARING HAD TO EARN ITSELF — and the fact that earned it was written
   in the MUSIC file, not in the prompt that makes the sound. A detail that lives
   only in a planning document does not reach the tool. FIXED this pass: K10's
   AUDIO line now carries "its last word clips off before it starts again".
   ⭐ This is the finding that cost the most: without it, the film's only repeated
   line was repetition instead of information.
② THE WINDOW IS CARRIED BY WHAT THE LINE DOES NOT SAY. "Please give the light
   back" must never become "please give our light back" or name a taker; one word
   would close the irony window 7 clips early and make K11 a recap. Locked as a
   rule here, because a later pass shortening prompts would not know it.
③ THE MOUTH STAYS SHUT — including in the four face clips. If any future revision
   lets her speak once, the recording loses its authority and the film's whole
   sound design (one voice, twice, from nobody) collapses. The tool setting box in
   GUNES_MEZARI_URETIM_DEFTERI.md §0⑵ is what enforces it, not a prompt sentence.
```

## VERDICT

```
GO
RESIDUAL NOTES:
  · Two slots, one written line: if the measured clip duration is not 10.0 s
    [D124], both seconds (24.0 · 90.0) recompute from the grid formula, not by hand.
  · Delivery is band-limited in both prompts (cabin speaker · off stone). The
    300-3400 Hz setting and the two loop skips are ⬜ production measurements in
    GUNES_MEZARI_MUZIK.md — not claimed as done.
  · The word "children" is the film's only sensitivity axis. No child is shown in
    any clip; the axis is SOUND only, and KART 12 was opened on that axis
    (02_KONSEPT_VE_RISK §6).
```
