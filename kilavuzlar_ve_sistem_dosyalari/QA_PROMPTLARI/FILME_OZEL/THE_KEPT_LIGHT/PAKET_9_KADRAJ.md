```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_KEPT_LIGHT
mercek    : ⑨ KADRAJ
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_KEPT_LIGHT_QA_SPEC.md  (aile: yatay)
üretildi  : 06.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_3_5_dk_filmler/THE_KEPT_LIGHT
belge: B (kurgu geometrisi · KURULUM İSKELETİ = PLAN STRING) + C (eş kadraj · ekran yönü). ⛔ KARE ÖNCE, HARF SONRA — SETUP STRING plandan kopyalanmaz
```

# ⑨ KADRAJ QA — CAMERA SETUP FIDELITY CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑨. Kardeş mercekler: ① KARE · ② DEVAMLILIK ·
> ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑩ OYUNCULUK ·
> ⑪ IŞIK · ⑫ HOOK.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **CAMERA SETUP FIDELITY** — whether
the camera stands where the plan put it, at the lens and distance the plan
wrote, and stays there.

A generated clip is asked for a camera and gives you a camera; the two are
not always the same. The prompt says "50mm, fixed 0.6 m above the lip,
top-down" and the model delivers a low angle from beneath. The prompt says
"locked off" and the frame breathes, creeps or re-centres. Every other lens
looks THROUGH the camera at the subject; **you look at the camera itself.**
Nobody else does.

⛔ This is not the frame lens. They ask what is broken inside the picture.
You ask whether the picture was taken from the right place. A flawless image
from the wrong setup is a PASS for them and a finding for you.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, setups, strings or
movement of any kind. Write the line, put every question in FLAGS, and stop.

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied (setup sequence · skeleton · pairs)
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated.

**MODE D** — the plan names every setup. You match what you see to what was
named, scene by scene.

**MODE V** — you have no plan. You may still score lockoff integrity, return
consistency (the same place must look the same twice) and the opening /
closing pair as SELF-consistency. You may never call a setup "wrong" against
a plan you do not have — that goes to FLAGS.

---

## 📋 SETUP LOCK LIST — MODE D ONLY

### ⬇️ OPERATÖR DOLDURDU — THE_KEPT_LIGHT_QA_SPEC.md'den B + C(EŞ KADRAJ · EKRAN YÖNÜ) · MODE D

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      22 · sahne içi kesme 0
                 (3 çekim ikiye bölündü: S3-S4 · S16-S17 · S20-S21 — bunlar
                  KÜMEDİR, kesme değil bölünmüş tek çekim [ACI_YAYI §3 🕰️])
CUT COUNT:       21 (24 sınır − 3 görünmez küme dikişi)
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, BİLİNÇLİ SAPMA)
                 ⛔ GEREKÇE SATIRI [D74]: bu hattın klibi sabittir ve klip
                 süresi ARAÇTAN ölçülür [D124]. Değişken çekim süresi
                 yazmak KART 11'i açar ve talimatsız kurgu KIRPMAZ, KLİP
                 DÜŞÜRÜR. Ritim kırpmadan değil KADRAJ İÇİNDEN gelir
                 (ölçek merdiveni · palet · ses dokusu — plan §örüntü kırıcı).
ASL CURVE:       ①10.0 ②10.0 ③10.0 ④10.0 ⑤10.0  (sabit ızgara)
GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10 s klip
                 S0 0 · S1 9 · S2 19 · S3 29 · S4 39 · S5 49 · S6 59 ·
                 S7 69 · S8 79 · S9 89 · S10 99 · S11 109 · S12 119 ·
                 S13 129 · S14 139 · S15 149 · S16 159 · S17 169 · S18 179 ·
                 S19 189 · S20 199 · S21 209 · S22 219 · S23 229 · S24 239
RUNTIME:         249 s = 4:09
RAW FOOTAGE:     25 klip × 10.0 s = 250.0 s · TRIM BUDGET: 1.0 s
KIRPMA TABLOSU [KART 11 · D100]:
                 S0   10.0 s ham → 9.0 s kurguda · baştan 1.0 s (hook)
                 S1-S24  10.0 s ham → 10.0 s kurguda · kırpma 0
                 ⛔ Kırpma klip DÜŞÜRMEK değildir. Satırı olmayan klip
                   kırpılmamış sayılır.
SCREEN TEXT:     0.0 saniye (jenerik · başlık kartı · kapanış kartı ·
                 filigran: 0 kare) [D34 · D70 · D72]
CAMERA:          25/25 sabit lockoff · klip içi hareket 0
SETUP SEQUENCE (sahne sahne kurulum imzası):
  A 50mm/0.6 m üstü/CU/tepe    B 85mm/0.9 m üstü/CU/üst açı
  C 50mm/2.0 m/MS/profil+göz   D 24mm/5.0 m/WS/göz hizası
  E 24mm/0.4 m üstü/EWS/tepe   F 28mm/9.0 m/EWS/alt açı
KURULUM İSKELETİ: A E D C C D C B C D F D C D C B C C B C E E D C A
                 (PLAN'daki ile AYNI — 25 harf = 25 sahne)
KÜME:            3 · S3-S4 · S16-S17 · S20-S21   (12+ sahnede ≥2 ✅)
                 her biri 2 klip (tavan 3) · üçü de DEVAM işaretini taşıyor
DÖNÜŞ:           15/25 = %60  (12+ sahnede ≥%40 ✅ · betiğin kendi ölçümü)
                 S4 S5 S6 S8 S9 S11 S12 S13 S14 S16 S17 S18 S19 S21 S23
ANGLE ARC:       5 açı TİPİ (tepe · üst açı · profil · göz hizası · alt açı)
                 ⛔ ≥3 ister ✅ · dutch 0 sahne · abartı eşiği aşılmadı
                 (üst açı ~30° · alt açı ~20°, ikisi de 15-30 meşru bandında)
BİLİNÇLİ ŞOK:    2/2 · S0→S1 (CU→EWS, 3 kademe) · S19→S20 (MS→EWS, 2 kademe)
DORUK:           S19 → 189 s (sahne başlangıcı) · kesim 192 s · sonucu
                 S20 (199 s) ve S21 (209 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 9 s hook + (n−1) × 10 s klip + promptun TIMELINE ofseti
   ⛔ BU FİLMDE REPLİK 0 — formülün koşacağı kayıt yok. Formül yine de
     burada durur çünkü aynı formül aşağıdaki üç kaydı DOĞRULAR:
       tohum       S3  · 29 + 2.0  = 31.0 s  = 0:31 ✅
       katalizör   S3  · 29 + 5.0  = 34.0 s  = 0:34 ✅
       kapak anı   S0  · 0  + 4.0  =  4.0 s  = 0:04 ✅
       merkezî seçim S19 · 189 + 3.0 = 192.0 s = 3:12 ✅
       final kanıtı S24 · 239 + 8.0 = 247.0 s = 4:07 ✅
     Beşi de formülle doğrulandı; sapma 0.

FİNAL VURUŞ KANITI [D141]:
   nesne: ağzın altında asılı duran PARLAK NESNE
   saniye: 247.0 (4:07)
   kaç tane: ALTI — beş kelepçe + bekçinin lambası
   BULUNAN mı BULUNMAYAN mı: **BULUNAN** (sayılabilir ve adı konabilir)
   ⛔ Sap (kesilmiş altıncı kelepçenin gövdesi) kadrajın ÜST kenarındadır,
     çerçeveye cıvatalıdır ve bu sayıya GİRMEZ.
   ffmpeg -ss 247 -i "$M" -frames:v 1 kanit.jpg   → BAK VE SAY

DÖNGÜ KANITI: bu film DÖNGÜ değil KAFİYE bandındadır [ACILIS_KAPANIS §1].
   İlk kare (S0 · 0:00) ile son kare (S24 · 4:09) AYNI kurulum (A), aynı
   ölçek, aynı ışık, aynı jest (açık eldiven, aynı koordinat).
   DEĞİŞEN TEK DEĞİŞKEN: avuçtan çıkan şey — eskimiş bir kelepçe →
   bekçinin kendi YANAN lambası. Kalçadaki klips son karede BOŞTUR.
   ⛔ İki kare yan yana konduğunda değişim okunmuyorsa çift BAŞARISIZDIR.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111111111111111
       (25 sahnenin 25'inde insan var · insansız sahne 0 — KART 10
        yapısal olarak tetiklenmez)
       ⚠️ S1 · S7 · S15 · S18 · S20 · S21'de insanın YALNIZ bir parçası
       kadrajdadır (botlar/dizler ya da iki eldiven). Bu bir insansız
       sahne DEĞİLDİR ve şeritte 1 sayılır.
```


```
EKRAN YÖNÜ    "Yukarı" = KAYA TAVANI · "aşağı" = KARA DİSK — ikisi de
              adlandırılmış NESNEDİR, koordinat değil [D174].
              Ağız her yatak kadrajında kadrajın ALT yarısında · alan her
              zaman ağızdan AŞAĞI gider · kaya her dış kadrajda ÜST üçte
              birde. 25/25 sahnede SABİT · ters dönüş 0.
EŞ KADRAJ     S0 ↔ S24 (kurulum A · konum kilidi) ·
              S3 ↔ S4 ↔ S6 ↔ S8 ↔ S12 ↔ S14 ↔ S16 ↔ S17 ↔ S19 ↔ S23 (C) ·
              S2 ↔ S5 ↔ S9 ↔ S11 ↔ S13 ↔ S22 (D) ·
              S1 ↔ S20 ↔ S21 (E) · S7 ↔ S15 ↔ S18 (B) · S10 tek (F)
              ⛔ [D153] Aynı harfin ikinci ve sonraki imajları, o harfin
                ONAYLI ilk karesinden ≤3 maddelik fark listesiyle türetilir.
```


Read out of the supplied SPEC before you watch:

```
SETUP SEQUENCE    → the letters: lens / distance / shot size / angle per letter
KURULUM İSKELETİ  → one letter per scene, in order — this is the PLAN STRING
CAMERA            → lockoff count · in-clip movement allowed (usually 0)
EŞ KADRAJ         → scenes that must share a frame (S0 ↔ last · clusters)
KÜME / DÖNÜŞ      → split shots (seams) · returns to an earlier setup
ANGLE ARC · BİLİNÇLİ ŞOK → the planned scale jumps; any other jump is unplanned
GRID              → scene start times
```

⛔ **THE GRID IS GIVEN.** You do not build a scene count from scratch. You
pull ONE frame per scene at `start + 5 s` and confirm that each cut you see
sits on the grid. A cut off the grid is reported with its timecode on the
`CUTS OFF GRID` line — never silently re-numbered.

Write the PLAN STRING at the top of your ledger before the first frame.

---

## ⛔ STEP 0 — THE SETUP REGISTER (both modes)

For every letter (mode D) or every distinct camera position you meet (mode V):

```
SETUP REGISTER
· letter        [A / B / … in mode D · "first seen S<n>" in mode V]
· shot size     [EWS / WS / MS / MCU / CU / ECU]
· angle         [top-down / high / eye / low / dutch]
· lens feel     [wide — edges stretch, deep · normal · long — compressed]
· position      [above the subject / side-on / front / behind · distance]
· anchor        [ONE fixed object that must sit at the same place in frame
                 every time this setup returns — the lip, the rail, the far wall]
```

The anchor is your ruler. A returning setup that moves the anchor has moved
the camera, whatever the prompt said.

---

## STEP 1 — BUILD THE SETUP LEDGER (before judging anything)

One frame per scene at `start + 5 s`; a second frame at the end of the clip
if anything moved. One row per scene:

```
S<n> | in | plan letter | observed size / angle / lens / position |
       observed letter | MATCH · NEAR · MISS | anchor position | in-clip movement
```

- **MATCH**: size, angle and position all agree with the letter.
- **NEAR**: one of the three drifts (a CU that is an MCU; a top-down that is
  a steep high angle) — write which.
- **MISS**: a different setup. Name the letter it actually is, or `?`.
- **In-clip movement**: `0` for a held frame; otherwise name it — creep,
  drift, re-centre, push, breathing, handheld — and the second it starts.

Then write the **SETUP STRING**: your observed letters, one per scene, in
order, no spaces. Under it the PLAN STRING. Mark every position that differs.

⛔ **DESCRIBE THE FRAME FIRST, ASSIGN THE LETTER SECOND.** Never correct the
SETUP STRING toward the plan. It is a fingerprint of what was delivered; a
string that matches because you read the plan first is worthless.

### ⛔ THE RHYME PAIR — one test, run on every film

Put the first frame of the film and the last frame of the film side by side.
Answer three questions, one line each:

1. Same setup? (size · angle · position · anchor in the same place)
2. Same scale of the subject?
3. What is the ONE thing that changed?

In mode D the plan names the one variable. If more than one thing changed,
or the setup is not the same, the pair FAILS — and the film has lost its
closing image whatever the last scene contains. Write the three lines.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

```
① SILENT REFRAME — the model ignores lens and distance and picks its own,
   usually a "nicer" three-quarter angle.
② ANGLE FLIP — top-down becomes low angle or the reverse; the subject is
   framed from the side the prompt excluded.
③ CREEPING DOLLY — a locked-off frame drifts, breathes or pushes in over the
   clip. Often only in the last two seconds.
④ SCALE COLLAPSE — an EWS returns as an MS; the world shrinks to the figure.
⑤ SEAM JUMP — a shot split into two clips reframes across the seam: anchor
   moves, horizon shifts, lens changes.
⑥ RETURN THAT DOESN'T RETURN — the same letter appears twice and the second
   is a different camera; the same place reads as a new place.
⑦ MIRRORED SETUP — the plan's setup flipped left-right; screen direction
   inverts.
⑧ HORIZON TILT — an unplanned dutch; the anchor line is no longer level.
⑨ THE RHYME THAT ISN'T — the closing frame is CLOSE to the opening one but
   from a different setup; the pair reads as "similar", not "same".
⑩ THE FRAME THAT BREATHES AT THE CUT — a re-centre in the first ten frames
   as the model settles; reads as a jump cut.
```

---

## ═══ YOUR SCOPE ═══

```
✅ Where the camera is, what lens it wears, whether it holds, whether it
   returns to the same place when the plan says it does, and whether the
   first and last frames rhyme.
```

## ═══ NOT IN THIS PASS ═══

```
❌ What is INSIDE the frame — artefacts, anatomy, texture     → the FRAME lens
❌ Whether the PROPS are the same twice                       → CONTINUITY
❌ Whether the environment behind the subject holds            → BACKGROUND
❌ Whether the beat READS, whether the body PAYS               → ACTION / EFFORT
❌ Whether the LIGHT holds between clips                       → the LIGHT lens
   (a setup that returns with a different key light is theirs;
    a setup that returns from a different POSITION is yours)
❌ Whether the cut RHYTHM works                                 → the STORY lens
❌ In mode V, anything you think the PLAN intended — FLAGS only.
```

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material takes `N/A` and leaves the mean.

### 1. 🎯 SETUP FIDELITY (mode D only · N/A in mode V)
```
□ SETUP STRING matches PLAN STRING position by position
□ Every MISS is named with its observed letter and timecode
□ No setup silently replaced by a "nicer" angle (pattern ①)
□ No angle flipped in side or elevation (pattern ②)
```

### 2. 🔒 LOCKOFF INTEGRITY
```
□ Every clip declared locked off holds for its full length
□ No creep, breathing, push or re-centre (patterns ③ ⑩)
□ Movement, where it exists, starts at a named second
□ The anchor object does not move inside any clip
```

### 3. 🔁 RHYME PAIR
```
□ First and last frames share a setup (size · angle · position · anchor)
□ Exactly one declared variable changed
□ The change reads with the two frames side by side
□ Nothing sits between the last scene and the end of the file
```

### 4. ↩️ RETURN CONSISTENCY
```
□ Every repeat of a letter puts the anchor at the same place (pattern ⑥)
□ Lens feel is the same on every return
□ Scale of the subject is the same on every return (pattern ④)
□ Screen direction is preserved on every return (pattern ⑦)
```

### 5. 🪡 CLUSTER SEAMS
```
□ Across a declared split, the camera does not move (pattern ⑤)
□ Horizon, anchor and lens agree on both sides of the seam
□ Last frame / first frame side by side: the seam is invisible
```

### 6. 📐 ANGLE ARC & DELIBERATE SHOCKS
```
□ The planned scale jumps land where the plan put them
□ No unplanned jump of two or more scale steps at any other cut
□ Every angle type the plan promised appears at least once
□ No unplanned dutch (pattern ⑧)
```

### 7. 🧭 SCREEN GEOMETRY
```
□ The plan's "up" and "down" objects sit where it puts them, in every setup
□ The subject's side of frame is stable across returns
□ Wide setups do not bend a straight anchor into a curve
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
SETUPS REGISTERED: [n distinct camera positions]
LOCKOFF HELD: [n / n clips]

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Exclude it from every
count and every string.

ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
VERDICT: [CAMERA HELD / MINOR DRIFT / SETUP BROKEN / RHYME BROKEN /
          CAMERA WANDERED]
         One finding outranks the mean: if the RHYME PAIR fails, the verdict
         is RHYME BROKEN regardless of the score. If three or more scenes are
         MISS, the verdict is SETUP BROKEN.
```

## SETUP LEDGER
[the full STEP 1 ledger — this is evidence, include it]

## SETUP STRING
```
OBSERVED:   [one letter per scene · `?` for unmatched]
PLAN:       [from the SPEC — mode D only]
DIFFERS AT: [S-numbers, or "none"]
```
⛔ Length of OBSERVED = SCENES OBSERVED. If they disagree, say so on this line.

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` if a human figure is
visible anywhere in that scene, `-` if none. You write this even though it is
not your subject — it is the one axis on which every lens of the same film is
checked against every other. In a single-figure film it is nearly constant
and proves little on its own; write it anyway.

## RHYME PAIR
| | First frame | Last frame | Same? |
|---|---|---|---|
| setup letter / size / angle / anchor position / the one variable | | | |

Verdict line: `PAIR HOLDS` or `PAIR FAILS` — and why, in one sentence.

## LOCKOFF VERIFICATION
| Scene | Declared | Observed | Movement starts at | Verdict |
|---|---|---|---|---|
One row per clip that did not hold; write "all held" if none.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**
Write the deduction's source as ledger rows with timecodes. A deduction with
no listed source is not applied. A category with material but no in-scope
source keeps 10/10 and its Issue cell reads "no in-scope source".

| # | Category | Score | Issue (ledger rows and timecodes) |
|---|----------|-------|-----------------------------------|
| 1 | Setup Fidelity | /10 | |
| 2 | Lockoff Integrity | /10 | |
| 3 | Rhyme Pair | /10 | |
| 4 | Return Consistency | /10 | |
| 5 | Cluster Seams | /10 | |
| 6 | Angle Arc & Deliberate Shocks | /10 | |
| 7 | Screen Geometry | /10 | |

## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

## THE THREE THAT MATTER
The three findings that most damage this film's camera, in order, each with
its timecode and its one-line fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
A wrong setup cannot be moved in post — say so plainly. A small scale miss
on a high-resolution lockoff may be cropped; a creep may be stabilised at a
resolution cost. Name the cost.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, lens named.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **Describe the frame first, assign the letter second.** Never the reverse.
- **The anchor is the ruler.** A prompt is a request; the anchor is evidence.
- **The rhyme pair is run on every film,** including in mode V.
- **A beautiful frame from the wrong place is a finding.**
