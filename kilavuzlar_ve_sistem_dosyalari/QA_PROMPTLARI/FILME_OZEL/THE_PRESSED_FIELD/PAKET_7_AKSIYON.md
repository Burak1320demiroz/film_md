```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_PRESSED_FIELD
mercek    : ⑦ AKSİYON
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_PRESSED_FIELD_QA_SPEC.md  (aile: yatay)
üretildi  : 03.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_2_4_dk_filmler_uzay/THE_PRESSED_FIELD
belge: A (sahne haritası) + C (kilitler). ⛔ Rubriğin kuralı: ANLATIM CÜMLESİ önce EKRANDAN yazılır, sonra plana bakılır — ters sıra sahte PASS üretir
```

# ⑦ AKSİYON QA — ACTION LEGIBILITY CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑦. Kardeş mercekler: ① KARE · ② DEVAMLILIK ·
> ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑧ EFOR.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **ACTION LEGIBILITY** — whether a
first-time viewer can narrate what physically happened, in order, without
guessing.

This is not a physics review and not a story review. The physics lens asks
whether the numbers survive checking. The story lens asks whether the film
means anything. **You ask one question, of every moment where something
physical happens to someone: could a viewer describe it?**

An action beat that is physically perfect and dramatically motivated can
still fail here — because the contact happened behind an elbow, because the
threat arrived from a direction the frame never established, because the cut
landed on the wind-up and resumed on the aftermath and the beat itself was
never rendered.

⛔ **Legibility is not the same as beauty, speed, or intensity.** A calm,
slow, well-framed grapple can be perfectly legible. A fast, loud, shaking
sequence can be illegible. Rate your findings on what a viewer can RECOVER
from the screen, never on how exciting it felt.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

Before anything else, answer in one line:

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, cuts, scene counts,
durations, or motion of any kind. Write `MEDIA: nothing played`, put every
question in FLAGS, and stop. **A run that invents a timeline is worse than
a run never made.**

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied with the video
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated. If you were given a document, you are in mode D — read it.

**MODE D** — you verify the film against its own declared plan. Every beat
the plan declares must be found on screen or reported missing by name.

**MODE V** — you have no plan. You may never report that something is
MISSING; you have no way to know what was intended. An absence becomes a
question in FLAGS, never a deduction.

---

## 📋 BEAT LOCK LIST — MODE D ONLY

### ⬇️ OPERATÖR DOLDURDU — THE_PRESSED_FIELD_QA_SPEC.md'den A + C · MODE D

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE PRESSED FIELD
FORMAT:            yatay 16:9 · 2-4 dk hattı (sahne kısıtıyla 1:40)
RUNTIME:           100 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       10
THEME:             FIRST CONTACT
THEME SCENES:      S4 · S5 · S7 · S9
INTENDED EMOTION:  dread turning into awe — the fear of an unseen agent
                   becoming the scale of an unstoppable process
ENDING TYPE:       reversal (twist) with an ambiguous tail — the surveyor
                   has been inside the field for some time without knowing
PROTAGONIST:       a surveyor, unnamed (no proper name appears in any prompt)
CENTRAL CHOICE:    S7 — she pulls up her own planted line and re-plants it
                   as a warning arc, giving up the job she came to finish
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     10 of 10 (ambient and effect audio only, no speech)
VIRAL INTERSTITIALS: S1 (10.0-20.0 s) · S7 (70.0-80.0 s)
                   ⛔ THESE MAY NOT BE CUT
TITLE:             "THE PRESSED FIELD" promises the GROUND. The confirmation
                   is in the first second of S0.
LIBRARY CONTEXT:   same shelf as the thin-atmosphere survey films
                   (LOW_POWER · THE_SKYLIGHT). First film in this repository
                   whose antagonistic force is a non-human presence, and it
                   is never shown: 0 frames, 10 scenes of 10.
```


## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 10 sahnenin 10'unda · mürettebat 0 · araç 0 · klon 0
              yansımada insan 0 · başka insana ait ayak izi 0
VARLIK        0 KARE · 10 sahnenin 10'unda. Uzaylı varlığın gövdesi, uzvu,
              gölgesi ve yansıması hiçbir karede YOKTUR. Varlık yalnız
              ETKİSİYLE vardır (sertleşmiş zemin). ⛔ Kadrajda bir gövde
              görünüyorsa bu bir ÜRETİM HATASIDIR, tasarım değil.
KASK          vizör optik berrak, sıfır ton, sıfır ayna kaplama · sırt
              ünitesi YOK — düz siluet, tek sürekli panel [D79]
              HELMET STATE: kapalı S0-S9 (10 sahne) · açık 0 sahne
NOVUM         Bir şeyin geçtiği yerde gevşek toz kalıcı olarak taşa
              sıkışır ve sıkışma yayılmaya devam eder.
              İHLAL: aynı gevşek tozda özdeş iki çubuktan biri dize kadar
              girer, öteki hiç girmez ve bükülür (S6 · 60-70 s).
              TAŞIYICI: ölçüm çubuğu × tokmakla sürme jesti
              KURULUM S0-S1 · DOĞRULAMA S6 · SONUÇ S9 (≥3 sahne, 3 nesne:
              bot · çubuk · kendi izi)
YERÇEKİMİ     0.38 g — serbest düşen nesne ilk saniyede 1,9 m yol alır,
              düz yay çizer, havada asılı kalmaz.
              MASS ≠ WEIGHT [D169]: 0,38 g ağırlığı azaltır, kütle ve
              ataleti azaltmaz — tokmak vuruşu aynı eforu ister.
ATMOSFER      ince atmosfer · %0,6 basınç · ses boğuk, yüksek frekans yok ·
              toz YAVAŞ ama KESİN çöker, girdap/kıvrım/bağlı kütle YOK [D39] ·
              gölge yumuşak kenarlı MEŞRUDUR, bloom teşhisi DOKU KAYBINA
              bakılarak konur [D41]
EKRAN YÖNÜ    sertleşmiş alan/sınır kadrajın SAĞ yarısını veya sağ üçte
              birini tutar — S3 · S4 · S8 · S5 (dört sahnede yazılı) ·
              yön dönüşü 0 · alçak güneş HER sahnede kamera-SOLDA ·
              kimse ışığa doğru yürümez [KART 9 dört kanal]
SAYAÇ         KOVANDAKİ ÇUBUK — monotonik, hiç artmaz:
                S2 dört · S3 üç · S5 üç · S8 sıfır
                (S6 ve S7 eylem sahnesidir; sayım o ikisinde kilitlenmez)
              YAYDAKİ ÇUBUK: S8'de tam ÜÇ dik duran + elde bir = dört
              ⛔ Sayaç METİNSİZDİR: rakam, ibre, ekran içeriği YOKTUR
EŞ KADRAJ     S0 ↔ S9 (kurulum C · ECU tepe 90° · 0,9 m) — tek değişken:
              zeminin cevabı. Bot izi sayısı 2 → 0
YIPRANMA      monotonik merdiven, toz yalnız EKLENİR [D147]:
                PHASE 1 S0-S2 · PHASE 2 S3-S6 · PHASE 3 S7-S9
              ⛔ Sonraki sahnede önceki fazdan AZ toz varsa devamlılık hatası
IŞIK TAKVİMİ  monotonik ve SABİT: tek alçak güneş, ufkun ~12° üstünde,
              10 sahnenin 10'unda kamera-SOLDAN girer. Faz değişimi YOK.
SES REGISTER  HUMAN 0 · MACHINE 0 · yalnız kask içi nefes + temas sesleri
PLANTED DETAIL ⭐ BİLİNÇLİ TOHUM [UZAYLI_VARLIK §5 · 04_ARASTIRMA T7.4③]
              sahne S1 · saniye 13.5-15.0 · konum kadrajın SOL ÜST arka
              planı, odak DIŞI · ne: geldiği hattın iki çubuğu arasındaki
              tozun pürüzsüz olması (alanın ikinci kolu, henüz adı yok)
              ⛔ Bu bir üretim hatası DEĞİLDİR. ⑤ ARKA PLAN merceği onu
                bulgu ya da bayrak olarak yazarsa sonuç HATA değil ÖLÇÜMDÜR
                (tohum fark edilebilir demektir) ve kilit çelişkisi
                defterine "BİLİNÇLİ TOHUM — film sapmadı" olarak kapatılır.
                Skor düzeltilmez; tabloya dipnotla girer.
```



Read these out of the supplied SPEC before you watch:

```
A BLOĞU  → sahne haritası: her sahnenin ne yaptığı, doruk sahnesi
C BLOĞU  → kilitler: sayaçlar, ekran yönü, mesafeler, nesne konumları
```

From those, build a lock table BEFORE watching. One row per action beat the
plan declares: which scene, what the actor is trying to do, what resists,
what the outcome is. You will verify each row on screen.

> 📌 **Eksik blok kaydı (dürüst not):** bu depoda SPEC'ler ⑦ için ayrılmış bir
> blok TAŞIMAZ; A + C bloklarından çıkarım yaparsın. Bir film ileride
> **D BLOĞU — AKSİYON** yazarsa (beat listesi: sahne · niyet · direnç · temas ·
> sonuç · tehdit yönü), bu mercek belgeli koşar ve çıkarım gerekmez.
> Bugün çıkarım MEŞRUDUR ama çıkarım olduğu YAZILIR.

---

## ⛔ STEP 0 — THE PREMISE GATE (both modes — run it before judging anything)

The film may have declared rules that make an "error" correct. Before you
score anything, write the register:

```
PREMISE REGISTER
· gravity / medium         [e.g. vacuum, 0.12g contact steps]
· what the actor can do    [suit limits, tools, established capability]
· what resists them        [the antagonist force: matter, time, machine, person]
· established screen rules [is the camera ever handheld? does it ever cut mid-beat?]
```

A beat that violates ordinary expectation but obeys the film's declared
rules is **NOT a finding**. Write it in the register and move on.

⛔ NAMING THE MEDIUM IS NOT NAMING A RULE. "Zero-g", "vacuum", "motion is
continuous until arrested" describe the SETTING and restate ordinary
physics. If the film is built on an impossibility — matter that stops,
weight that transfers, a force that only works one way — the register must
state THAT, with the threshold the screen shows, and the beat that carries
it is then the film's MOST important beat, not a scene with no beat in it.
Before you write `-` in the beat string for any scene, ask whether that
scene is where the film's rule is demonstrated.

⛔ Absence of an antagonist figure is not absence of action. In this repo
most films have no second person: the resisting force is vacuum, cold,
a countdown, a mass, a mechanism. **Those are action beats and they are
yours.** A film where a lone figure fights a stuck coupling for 40 seconds
is an action film for this lens.

---

## STEP 1 — BUILD THE ACTION BEAT LEDGER (before judging anything)

Watch once for beats. A **beat** is one attempt at one physical problem. It
has a boundary you can name. Write one row per beat:

```
B<n> | in–out | ACTOR does WHAT | resisted by WHAT | contact? | outcome |
       threat/force direction on screen | readable? Y / PARTIAL / N
```

Rules for the ledger:

- A beat may span scenes. A scene may hold several beats. **Beats are not
  scenes** — do not force them to align.
- `contact?` is what you SAW: contact / near-miss / occluded / none.
- `outcome` is the state change: what is different after the beat that was
  not different before. If nothing is different, write `no state change` —
  that is itself a major finding.
- `readable?` is your verdict on that single beat, decided by the narration
  test below. Decide it BEFORE you look at your category scores.

### ⛔ THE NARRATION TEST — the only test this lens has

For each beat, write the sentence a first-time viewer would say:

> *"He braces his boot on the strut, pulls the lever twice, it doesn't move,
> then the third pull tears his glove."*

If you cannot write that sentence without using the SPEC, without guessing,
and without the words *"probably"*, *"seems to"*, or *"I think"* — the beat
is `N` (unreadable). If you can write it but one clause is uncertain, it is
`PARTIAL`. **Write the sentence in the ledger.** The sentence is the
evidence; a `readable? N` with no attempted sentence is not a finding.

⛔ In mode D you must write the narration sentence FROM THE SCREEN FIRST,
then compare it with the plan. Reading the plan first contaminates the test
— you will "see" what you were told is there. This is the single most common
way this lens produces a false PASS.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

These are the ways generated video breaks action. Each is a real, repeated
failure in this repo's material.

```
① CONTACT WITHOUT OCCLUSION — the hand reaches the surface but never
   deforms it, never occludes it, never stops on it. Contact is asserted by
   proximity alone.
② REACTION BEFORE CAUSE — the struck body, the dust, the cloth begins to
   move one or more frames BEFORE the thing that moved it arrives.
③ THE RESET POSE — after a violent motion the body returns to neutral
   standing. Nobody stays where the force left them.
④ THE ACTION ELLIPSIS — the cut lands on the wind-up and resumes on the
   aftermath. The beat itself was never rendered; the edit hides what the
   generator could not produce. Look for this specifically at every cut
   adjacent to a beat.
⑤ MOMENTUM EVAPORATION — a run, a fall, a swing ends without deceleration.
   Motion stops rather than slows.
⑥ THE FLOATING HIT — force lands and the world does not answer: no debris,
   no dust displacement, no cloth ripple, no camera answer, no settle.
⑦ GEOGRAPHY TELEPORT UNDER MOTION — the threat that was at screen-left is
   at screen-right mid-beat, with no move that put it there.
⑧ UNMOTIVATED CAMERA VIOLENCE — shake, whip, or blur with no in-world cause,
   arriving exactly where the action should be legible. Cover, not coverage.
⑨ LIMB MULTIPLICATION UNDER SPEED — an extra arm, a doubled hand, a leg
   that leaves and re-enters during fast motion.
⑩ THE ONE-SPEED FILM — every action at the same rate. No burst, no sustain,
   no hesitation. Effort has no tempo.
⑪ INTENT INVISIBLE — the body moves but you cannot tell what it is TRYING
   to do. Motion without a goal reads as animation, not action.
⑫ STAKES OBJECT OFF-SCREEN AT THE DECISIVE MOMENT — the thing the beat is
   about leaves the frame exactly when it resolves.
⑬ THREAT WITH NO APPROACH — the danger appears already at contact distance.
   It never travelled; therefore it was never coming.
⑭ SLOW-MOTION WITHOUT A SLOWED WORLD — the subject slows, the dust and the
   background do not.
```

---

## YOUR TASK

Watch the film. Build the beat ledger. Run the narration test on every beat.
Then score the categories below, deducting only from what your ledger holds.

## ═══ YOUR SCOPE ═══

```
✅ Whether physical events READ: beat boundaries, intent, spatial geography
   under motion, threat direction and approach, contact and its occlusion,
   consequence visibility, the camera's contract with the action, the tempo
   of effort, and whether the edit renders the beat or hides it.
```

⛔ **You own READABILITY, not correctness, not sameness, not meaning.**
Whether the momentum is numerically right, whether the glove is the same
glove, whether the scene earns its place in the story — none of these are
yours. You ask one question of every observation: **can a viewer recover
what happened?**

## ═══ NOT IN THIS PASS ═══

```
❌ Quantities: momentum, mass, speeds, stride rates, gravity, distances
   measured and computed                                  → the PHYSICS lens
   (the moment your finding needs a NUMBER to stand, it is theirs; the
   moment theirs needs a VIEWER to stand, it is yours)
❌ Artifacts read off one frame or one shot: morphing, melting, anatomy at
   rest, texture swimming, bloom, on-screen text        → the FRAME lens
   (limb multiplication DURING motion is yours when it destroys the beat's
   readability, and theirs as an artifact — both may write, each its kind)
❌ Whether a thing is the SAME across a cut: costume, prop, counter,
   established screen direction as a continuity value   → the CONTINUITY lens
   (their question is "did it change?"; yours is "could you follow it?"
   A perfectly consistent geography can still be unreadable, and that is
   yours alone)
❌ Whether the body shows strain, fatigue, injury cost, breath, load
                                                          → the EFFORT lens
❌ Dramatic escalation, pacing, whether the beat deserved its screen time,
   stakes as a story value                                → the STORY lens
❌ Anything in the non-subject field with no bearing on the beat
                                                      → the BACKGROUND lens
❌ Sound of impacts, mix, whether a hit is audible          → the SOUND lens
❌ In mode V, anything you think is MISSING — you have no plan. FLAGS only.
```

The boundary with the CONTINUITY lens, precisely: **they own "the threat was
at screen-left in S4 and screen-right in S5" — a comparison. You own "in S5
I could not tell where the threat was" — a reading.** The same cut can
produce both findings; each lens writes its own kind and neither writes the
other's.

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material in the film takes `N/A` and
leaves the mean (see DECLARED ABSENCE).

### 1. 🎯 BEAT ANATOMY
```
□ Each beat has a readable setup → commitment → contact → consequence
□ The beat's boundary is visible: you can say when it starts and ends
□ No beat is elided by a cut (pattern ④) — the attempt itself is on screen
□ A failed attempt reads as a FAILED ATTEMPT, not as an absent one
```

### 2. 🗺️ SPATIAL GEOGRAPHY UNDER MOTION
```
□ Actor, obstacle and goal have positions you could sketch during the beat
□ Movement between positions is shown or clearly implied, never teleported
□ Screen direction survives the beat's own cuts (pattern ⑦)
□ Frame scale lets you see the relationship the beat is about
```

### 3. ⚠️ THREAT VECTOR & APPROACH
```
□ The resisting force — figure, mass, mechanism, time — has a direction
□ It arrives from somewhere the frame established (pattern ⑬)
□ Its proximity is legible: you know how close it is to mattering
□ Where the threat is a countdown or a state, its progress is on screen
```

### 4. 👊 CONTACT LEGIBILITY
```
□ Contact occludes, deforms, or arrests — it is not asserted by proximity
□ Contact and reaction are in the right order (pattern ②)
□ The contact point is visible or its concealment is deliberate and covered
□ Near-misses read as near-misses, not as ambiguous contacts
```

### 5. 💢 CONSEQUENCE VISIBILITY
```
□ Every beat produces a visible state change (or is legibly a null attempt)
□ Force lands on a world that answers: debris, dust, ripple, settle
□ The body ends where the force left it (pattern ③)
□ Consequence persists at least into the following shot
```

### 6. 🎥 THE CAMERA'S CONTRACT WITH THE ACTION
```
□ Camera movement serves legibility — it does not hide the beat (pattern ⑧)
□ Shake, blur and whip have in-world causes
□ Cut rate does not outrun comprehension at the decisive moment
□ The lens distance at contact lets contact be seen
```

### 7. 🧭 AGENCY & INTENT
```
□ You can state what the actor is TRYING to do, at every beat (pattern ⑪)
□ The attempt has a method you can name, not generic exertion
□ Changes of plan mid-beat are visible as decisions
□ Where intent is deliberately hidden, the hiding is legible as hiding
```

### 8. 🎯 THE STAKES OBJECT
```
□ The object the beat is about is in frame when the beat resolves (⑫)
□ Its state is readable at the moment it changes
□ If it leaves frame, it returns in a state consistent with what happened
□ The viewer never has to be told what mattered
```

### 9. 📈 PHYSICAL TEMPO & ESCALATION
```
□ Beats differ in rate: burst, sustain, hesitation (pattern ⑩)
□ Successive attempts at the same problem escalate in method or cost
□ Slow motion, where used, slows the world with the subject (pattern ⑭)
□ The film's hardest physical moment is its most legible, not its blurriest
```

---

## OUTPUT FORMAT — use this exact structure

```
INPUT MODE: [D / V]
FILM: [name as stated by the operator, or "(not supplied)"]
RUNTIME: [mm:ss — "measured" or "~mm:ss ESTIMATED"]
FRAME RATE ASSUMED: [n fps — every duration in this report uses it]
SCENES OBSERVED: [n] · CUTS COUNTED: [n]
NON-SCENE MATERIAL: [in-out + what it is, or "none"]
PRESENCE STRING: [see the section below — one character per scene]
LINES HEARD: [n · every spoken line VERBATIM with its timecode, or "none"]
             When you write "none", say which none it is: "none — room tone
             present" or "none — nothing audible to me".
             ⛔ THIS LINE REPORTS WHAT YOU HEARD. It is never a statement
             about the file. You may not write that the file has no audio
             track: that is a property of the container, read with one
             ffprobe command, and no model can observe it. Write
             "none — nothing audible to me" and put the question in FLAGS.
BEATS COUNTED: [n · from the ledger]
BEATS READABLE: [n readable · n partial · n unreadable]
PREMISE REGISTER: [each declared rule, one line — or "none"]

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Material that carries
burned-in text, or is static, or bears no scene fingerprint, is a card.
Report its in and out timecode on that line, then EXCLUDE it from CUTS
COUNTED, from the ledger, from the beat string and from every duration you
report. Its text is never the film's name.

⛔ CUTS COUNTED is not optional and not a rounded impression: it is the
count you made in STEP 1, with its timecodes.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. When something this lens measures is
absent in EVERY scene without exception — no beat ever has a stakes object,
no threat is ever a figure — that category takes `N/A`, stays out of the
mean, and the absence is named in one line. Score low only for an absence
that is scattered. A throughout-absence you suspect is deliberate goes to
FLAGS as a question, never to a score.

⛔ A FILM WITH NO ACTION BEATS IS NOT A ZERO. If the ledger is empty, every
category is N/A, the OVERALL SCORE line reads `N/A — no action beats`, and
you write one line saying so. This lens does not punish a contemplative
film for being contemplative.

ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded,
                                 never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
VERDICT: [ACTION READS / MINOR BLUR / FIXABLE IN EDIT / BEATS ILLEGIBLE /
          ACTION NEVER RENDERED]
         One finding outranks every other score: if any beat's core attempt
         is elided by a cut (pattern ④) and never shown, the verdict is
         ACTION NEVER RENDERED, first line, regardless of the mean.
```

## ACTION BEAT LEDGER
[the full STEP 1 ledger with the narration sentence for every beat — this is
evidence, include it]

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` if a human figure is
visible anywhere in that scene, `-` if the scene has none. Cover only the
scenes you listed, excluding non-scene material. Never reorder it to match
what you expect a film to do — it is a fingerprint of the EDIT'S ORDER.

⛔ You write this even though it is not your subject. It is the ONE axis on
which every lens can be checked against every other lens: when six reports
of the same film print six strings, a disagreement locates the report that
misread the edit. A lens that skips it removes itself from that check.

⚠️ In a single-figure film this string is nearly constant (`1111…`) and
therefore proves very little on its own — a whole block of scenes can be
swapped without changing it [D163]. Write it anyway, and do not treat a
matching string as proof that the order is right.

## BEAT STRING
```
One character per scene, in order, length = SCENES OBSERVED:
  A = a beat runs in this scene and reads
  p = a beat runs and is PARTIALLY readable
  x = a beat runs and does NOT read
  - = no beat in this scene
Example (15 scenes): --A-ApxA--x-AA-
```
⛔ The string's length must equal SCENES OBSERVED, which must equal
CUTS COUNTED + 1 when there is no card. If those three numbers disagree,
say so on this line — do not silently adjust one to fit another.

## BEAT LOCK VERIFICATION — MODE D ONLY
| Beat the plan declares | Found at | Narration from screen | Verdict |
One row per declared beat. Verdicts: PASS / FAIL / UNREADABLE / NOT PRESENT.
A FAIL needs the ledger row it came from. This table is the reason mode D
exists — never omit a declared beat from it.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Issue cell, as ledger rows with
   timecodes: | Contact Legibility | 4/10 | -3 · B3 (1:20), B7 (2:41) |
   A deduction with no listed source is not applied; the category starts
   full.
② ONE OBSERVATION, ONE PLACE. An observation is EITHER a severity-tagged
   finding (it lowers ONE category's score) OR a question for the document
   (it lowers nothing). Never both, and never two categories at once — a
   contact that also broke the geography picks its owning category by the
   root cause, and the other category is not touched.
③ A category with material but no in-scope source keeps 10/10 and the Issue
   cell reads "no in-scope source". It never takes a silent deduction.
```

| # | Category | Score | Issue (with ledger rows and timecodes) |
|---|----------|-------|-----------------------------------------|
| 1 | Beat Anatomy | /10 | |
| 2 | Spatial Geography Under Motion | /10 | |
| 3 | Threat Vector & Approach | /10 | |
| 4 | Contact Legibility | /10 | |
| 5 | Consequence Visibility | /10 | |
| 6 | Camera's Contract with the Action | /10 | |
| 7 | Agency & Intent | /10 | |
| 8 | The Stakes Object | /10 | |
| 9 | Physical Tempo & Escalation | /10 | |

## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report. If they disagree, the report is not internally consistent and the
gate will say so.

## UNREADABLE MOMENTS TABLE
| Timecode | What I could not recover | Which pattern (①–⑭) | Severity |
Every `N` and `PARTIAL` from the ledger appears here. This is the table the
production line acts on.

## CONTRADICTION LOG
Every place where two things you observed cannot both be true, with both
timecodes. Do not resolve them silently — write both and name the one you
scored.

## THE THREE THAT MATTER
The three findings that most damage this film's legibility, in order, each
with its timecode and its one-line fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Two lists. A beat elided by a cut is almost never fixable in the edit — say
so plainly. A geography break at a single cut often is.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions. In mode V, every suspicion of a
missing beat lands here.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, with the lens
named. You do not score these and you do not argue them.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The narration sentence is the whole method.** Every finding in this
  report traces to a sentence you tried to write and could not finish.
- **Do not reward intensity.** Loud, fast and shaking is not legible.
- **Do not punish stillness.** A film with two beats in 150 seconds can
  score 10/10 here if both beats read.
- **Most films in this repo have no antagonist figure.** The resisting force
  is matter, cold, vacuum, a countdown, a stuck mechanism. Score those beats
  exactly as you would a fight.
- **In mode D, screen first, plan second.** Always.
