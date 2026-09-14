# 🗄️ ARŞİV — ORTAK ÇIKTI KURALLARI (rubrik diyeti · 14.09.2026)

> Altı rubrikte (①-⑥) tekrar eden ⛔ kalıp paragrafların UZUN hâli. 14.09.2026 rubrik diyetinde
> (`TODO_AKIS_VE_DERS_REFORMU.md` FAZ 5; `TODO_DERS_KILAVUZ_QA_KAPILARI.md` FAZ 5'in adı korundu)
> her rubrikte bu bloklar 1-3 satıra indirildi; kural DEĞİŞMEDİ, yeri değişti. Denetim yeri
> `RAPOR_KONTROL/rapor_kontrol.py` (CUTS COUNTED · NON-SCENE · LINES HEARD · ARITHMETIC GATE ·
> SEVERITY TALLY · PRESENCE STRING). Diyet-öncesi rubriklerin TAM kopyaları:
> `ARSIV_RUBRIK_DIYETI/<n>_..._DIYET_ONCESI_2026-09-14.md`. Bu dosya rubriğe yapıştırılmaz.

| rubrik | diyet öncesi | diyet sonrası |
|---|---|---|
| ① KARE | 61.054 B | 25.681 B (+ `1_KARE_DIKEY_EK.md` 3,8 KB, yalnız dikey) |
| ② DEVAMLILIK | 38.240 B | 20.078 B |
| ③ SES | 40.118 B | 20.316 B |
| ④ HİKAYE | 49.519 B | 24.646 B |
| ⑤ ARKA PLAN | 29.985 B | ~16 KB |
| ⑥ FİZİK | 33.484 B | 19.704 B |

Dondurulan (değişmeyen): kategori adları ve sırası · SCORES SUMMARY tablosu · başlık alanları
(INPUT MODE · FORMAT · RUNTIME · CUTS COUNTED · NON-SCENE · LINES HEARD · AUDIO STATE · PRESENCE
STRING · SEVERITY TALLY · ARITHMETIC GATE · PREMISE REGISTER) · tracking row sütunları ·
`MERCEK_IMZA` ifadeleri · `BOLUM_SONU` başlıkları. Kesilen: anekdotlar (07.09.2026 [D189] vb.),
tekrarlayan gerekçe paragrafları, kategori listelerindeki yinelenen SPECIFIC CHECK açıklamaları.

---

## MEDIA GATE (STEP −2) — altı rubrikte birebir aynıydı

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

## INPUT MODE — "INPUT MISSING" / SPEC MISMATCH / stop bloğu (①④⑥ mod D rubrikleri)

> 📌 **TO THE OPERATOR, BEFORE YOU PASTE THIS FILE: if the film's plan carries
> a QA SPEC block, this run is MODE D — copy it in.** A mode-V run of a film
> that has written locks reads its violations as matters of taste: a scene
> locked to zero frames of fire earns a 🟠 for sparks instead of a stop, and a
> film in which nobody ever speaks gets scored for lip-sync drift.

```
⛔ "INPUT MISSING" IS NOT A LEGAL OUTPUT OF THIS PROMPT.

Video with no document is MODE V — a defined, scored run, not a broken one.
Do not ask for the plan file. Do not stop. Do not print a stop block. Do not
reply with a request for more input. The document is not coming; you review
what you were given.

⛔ DO NOT SEARCH A REPOSITORY YOU CANNOT SEE, and never state or imply that
a file exists in one. If the operator did not paste it, it is not available
to you.

⛔ ONE STOP CONDITION SURVIVES, AND ONLY IN MODE D:
SPEC MISMATCH — the SPEC BLOCK was supplied and the footage contradicts it
(wrong scene number, dialogue where the script says silent). Then you are
looking at a different clip than the one you were handed, and scoring it
would poison the tracking table.

SPEC MISMATCH — RUN STOPPED
Field    : <name>   Stated : <x>   Footage shows : <y>
No scores. No tables. No verdicts. No tracking row.
This block is the ENTIRE output.
```

> ⚠️ **A stop condition may never appear as a FIELD inside your report.**
> A field is a box to fill; a model fills boxes and continues. Either you
> print the stop block and nothing else, or there is no stop.

> ⚠️ **An UNSAFE / UNVERIFIABLE label may not carry a number.** If a check
> is marked unverifiable, that category gets no score, does not enter any
> average, and goes to the table empty. A label that does not change
> behaviour is decoration.

---

## OUT-OF-SCOPE — sayı taşımaz · yalnız gördüğün (altı rubrik)

The boundary with the SOUND lens, precisely: **you ask whether the mouth
matches the words and whether the sound could exist in that medium at all.
They ask whether the voice matches the person.** A line whose lip-sync drifts is
yours. A line coming out of the wrong character is theirs.

The boundary with the CONTINUITY lens, precisely: **a face that warps WITHIN
one shot is yours. A face that is a different face in the NEXT scene is
theirs.**

If you notice an out-of-scope defect, write ONE line at the very end under
`OUT-OF-SCOPE FLAGS` and nothing more. Do not score it. Holding this boundary
is what lets reports from different rubrics be merged without counting the
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

## OUTPUT FORMAT başlık kuralları — LINES HEARD · NON-SCENE MATERIAL · CUTS COUNTED · DECLARED ABSENCE

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
you made in STEP 1, with its timecodes. "several cuts" is not a count. A
report that names scenes without printing this number has not measured the
material's shape, and every score built on that scene map is a score of a
film that may not exist.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. When something this lens measures is
absent in EVERY scene without a single exception, that is a constraint of the
material, not a defect. Such a category takes `N/A`, stays out of the mean,
and the absence is named in one line. Score low only for an absence that is
scattered: present in some scenes and gone in others. A throughout-absence
you suspect is deliberate goes to FLAGS as a question, never to a score.

---

## SCORES SUMMARY ①-⑤ — kaynak, tek yer, aritmetik, tally

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Critical Issues cell, as timecodes:
   | Environment | 5/10 | −3 · 2:20 (F2) · 2:30 (F3) |
   A deduction with no listed source is not applied; the category starts full.
② ONE OBSERVATION, ONE PLACE. An observation is EITHER a severity-tagged
   finding (it lowers a score) OR a FLAGS question (it lowers nothing).
   Never both.
③ An event you called UNVERIFIABLE in one category may NOT be scored in a
   neighbouring one. The label belongs to the OBSERVATION, not to the
   category cell you happened to write it in.
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

---

## IMPORTANT NOTES FOR THE REVIEWER — ① KARE'nin tam metni (SPEC-DEPENDENT / INDEPENDENT)

## IMPORTANT NOTES FOR THE REVIEWER:

- Be SPECIFIC with timestamps (e.g., "at 0:02.5")
- **Every logged issue needs a severity tag.** A report without severities is
  unusable — the whole point is deciding regenerate vs. accept.
- Focus on errors that BREAK immersion or violate the production rules
- Distinguish between minor artifacts (acceptable in AI video) and critical errors
  (breaks the film's believability)
- If the same error repeats throughout, note it once and mark "PERSISTENT"
- Compare what you see to what a real camera would capture — that's the standard
- **MODE D — judge against the SPECIFICATION BLOCK, not against your taste.**
  A clip can be beautiful and still be wrong. If the spec says 8-degree tilt
  and the clip shows 15, that is an error even if it looks better.
- **MODE V — judge against the clip itself and against physics.** You are not
  weaker in mode V, you are narrower: you still catch every fused hand, every
  swimming texture, every hidden cut, every hovering particle. What you lose
  is the right to call a choice wrong. Say what you see, not what was meant.
- If a spec field was left blank, mark the related checks UNVERIFIABLE rather
  than guessing. Say so in the report so the gap gets filled next time.
- **SPEC-DEPENDENT vs SPEC-INDEPENDENT** — a blank SPEC does not
  silence every check. Sort each finding before assigning severity:

```
SPEC-DEPENDENT — blank field → UNVERIFIABLE, NO severity, NO score
  suit colour · gravity value · camera move · light sources · tilt angle
  · locomotion mode · scene boundaries in compilation mode
  → you cannot call it a violation without seeing the rule

SPEC-INDEPENDENT — severity IS written even with an empty SPEC
  extra fingers · hand-surface fusion · on-screen text or subtitles
  · face morphing · solids passing through solids · frozen particles
  · duplicate human in frame
  → these are SERIES rules, not per-film spec. No film ever permits them.
```

  A blank SPEC silences the first list only. "Unverified field → no severity"
  applied to everything would discard findings that never needed a document:
  a fused hand and an extra digit are valid findings with no SPEC at all; a
  cut in a compilation is not.
- When suggesting prompt improvements, reference SPECIFIC vocabulary changes
  (e.g., replace "glowing" with "emitting sharp directional light") — word choice
  directly affects AI output quality
- The phrase "cinematic lighting" in a prompt is a known cause of waxy skin and
  bloom. If you see those symptoms, check whether that phrase is
  present and flag it for removal.
- Pay attention to the KNOWN AI FAILURE PATTERNS listed above — these are
  documented, recurring issues. If you see any of them, note which pattern
  number it matches

---

---

# 🗄️ 14.09.2026 · ÇIKTI SÖZLEŞMESİ — rubriklerden ÇIKARILAN tally / aritmetik / OVERALL metni

> QA çıktı reformu FAZ 1 (`TODO_QA_CIKTI_REFORMU.md`). Model artık saymaz; `rapor_kontrol.py`
> etiketleri sayar, ortalamayı hücrelerden hesaplar, VERDICT'i kapalı listeyle kıyaslar.
> Aşağıdaki bloklar 13 rubrikten olduğu gibi alındı (rubrik · kesilen parça). Eski raporlar
> bu satırları taşımaya devam eder; betik varsa yine kıyaslar, yoksa hesaplar.

### 1_KARE_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE and N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE
OVERALL SCORE: __/10   (state how many categories were excluded; NEGATIVE VIOLATIONS
                        is a count and never enters the mean)
```

### 1_KARE_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __    🟠 MAJOR: __    🟡 MINOR: __

```

### 2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE
OVERALL SCORE: __/10
```

### 2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __

```

### 3_SES_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE and N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE
OVERALL SCORE: __/10
```

### 3_SES_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __

```

### 4_HIKAYE_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE and N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL STORY SCORE
N/A LEDGER: __ of 10 · categories: ______ · OVERALL was computed over __ categories.
OVERALL STORY SCORE: __/10
```

### 5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE
OVERALL SCORE: __/10
```

### 5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __

```

### 6_FIZIK_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE
OVERALL SCORE: __/10
```

### 6_FIZIK_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __

```

### 7_AKSIYON_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded,
                                 never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
```

### 7_AKSIYON_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report. If they disagree, the report is not internally consistent and the
gate will say so.

```

### 8_EFOR_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded,
                                 never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
```

### 8_EFOR_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

```

### 9_KADRAJ_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
```

### 9_KADRAJ_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

```

### 10_OYUNCULUK_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
```

### 10_OYUNCULUK_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

```

### 11_ISIK_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
```

### 11_ISIK_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

```

### 12_HOOK_QA_CRITIQUE_PROMPT.md — ARITHMETIC GATE + OVERALL (başlık bloğu)
```
ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
```

### 12_HOOK_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

```

### 13_UYUM_QA_CRITIQUE_PROMPT.md — SCORED/SUM/DIVISION/OVERALL (⑬)
```
SCORED CATEGORIES: __
SUM OF SCORES: __
DIVISION: __ / __ = _._
OVERALL SCORE: _._
```

### 13_UYUM_QA_CRITIQUE_PROMPT.md — kontrat notu (⑬)
```
⛔ This block is the library's contract — the report-check script reads exactly
  these words. A category you could not verify is written `N/A`, is NOT counted
  in SCORED CATEGORIES, and enters no sum. The film-level category score is the
  worst scene's score for that category, not an average of averages.
```

### 13_UYUM_QA_CRITIQUE_PROMPT.md — SEVERITY TALLY bölümü
```
# SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report — the script recounts them and a mismatch voids the verdict [D161].

```
