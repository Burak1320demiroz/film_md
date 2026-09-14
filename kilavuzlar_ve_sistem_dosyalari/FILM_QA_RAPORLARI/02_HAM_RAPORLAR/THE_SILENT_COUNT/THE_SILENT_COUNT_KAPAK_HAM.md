# THE SILENT COUNT — KAPAK_QA HAM ÇIKTI

> Rubrik: `QA_PROMPTLARI/KAPAK_QA_CRITIQUE_PROMPT.md`
> Tarih: 09.08.2026 · Depodaki **ilk KAPAK_QA çalıştırması**
> ⚠️ Model çıktısı olduğu gibi, düzenlenmeden. Biçim bozuklukları
> (tablo satırlarının düz metne çökmesi) kaynağındaki hâliyle korundu.
> Kural ④: ham çıktı önce buraya yazılır, sonra özetlenir.

---

```
INPUT MODE: V
FILM: (not supplied)
COVER ASPECT: 16:9
PLATFORM: YouTube
COVER STATE: final
SPEC BLOCK PROVIDED: no

🔍 POSTAGE STAMP TEST — 120 px
Face visible:      yes
Emotion readable:  yes
Action readable:   yes
Text readable:     yes
Anything pops:     yes
VERDICT: PASSES

OVERALL SCORE: 6/10
VERDICT: YAYINLA

SCORES SUMMARY
Category / Score / Critical Issue
Face & Emotion              7/10   Intense gaze drives attention.
Curiosity Gap               6/10   Off-screen threat creates tension.
Contrast & Color            7/10   Orange/white pops against dark space.
Composition & Negative Space 6/10  Text balanced well with subject.
Typography                  6/10   Bold, readable at small scales.
Safe Zone                   7/10   Bottom-right clear of key elements.
AI Artifacts                7/10   Clean at thumbnail scale.
Character Conformity        N/A    Unverifiable in Mode V.
Promise vs Payload          UNVERIFIABLE   Film not provided.

MEASURED VALUES
Face coverage:        ~45% of frame   (target ≥60%)
Negative space:       ~35%            (target 30-40%)
Dominant colors:      3               (target 2-3)
Contrast estimate:    6:1             (target ≥4.5:1)
Word count:           3               (target 0-3)
Eyes in upper third:  yes

THE SCROLLER'S QUESTION
"What catastrophic event is he watching unfold off-screen?"

CHARACTER BIBLE CHECK
Bible detail / Present?
N/A (Mode V) / N/A

SAFE ZONE VIOLATIONS
Element / Position / Band it falls in
Right shoulder/suit / Bottom-right / Duration badge (safe to cover)

AI ARTIFACT LOG
Artifact / Severity / Visible at 120px?
Slight waxy skin texture / Low / No
Helmet rim reflection anomalies / Low / No

TOP 3 FIXES (ranked by CTR impact)
1. Increase face scale — Push zoom closer to hit the 60% face coverage target.
2. Dim background stars — Push the space background deeper into shadows to
   increase subject pop.
3. Thicken text outline — Add a slightly heavier drop shadow behind
   "THE SILENT COUNT" for maximum contrast.

REGENERATION PROMPT CHANGES
N/A (Verdict is YAYINLA)

PLAN B RECOMMENDATION
Alternative cover: Red-hued emergency lighting inside the cockpit, extreme
close-up (70% frame) of the astronaut's eye reflecting a countdown timer.
Prompt: SUBJECT — extreme close up astronaut face inside dark cockpit,
illuminated by harsh red emergency flashing lights, pure terror expression,
reflecting bright digital numbers in visor, cinematic lighting, 8k --ar 16:9

FLAGS FOR DOCUMENT CHECK — mode V only
QUESTION: Does the cover face match the Character Bible — specifically the
stubble and dark hair?
QUESTION: Does the film deliver an intense, high-stakes countdown or
impending threat as promised by the expression and text?
```
