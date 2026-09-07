```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_OPEN_CIRCUIT
mercek    : ⑪ IŞIK
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_OPEN_CIRCUIT_QA_SPEC.md  (aile: yatay)
üretildi  : 07.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_3_5_dk_filmler/THE_OPEN_CIRCUIT
belge: C (ışık takvimi · atmosfer · yapı anatomisi · kask) + B (ızgara). ⛔ ORTAM YASAYI KOYAR: vakumda pus/bloom/kaldırılmış gölge bulgudur; ilan edilmiş sınırdaki değişim PASS
```

# ⑪ IŞIK QA — LIGHT & GRADE CONTINUITY CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑪. Kardeş mercekler: ① KARE · ② DEVAMLILIK ·
> ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ ·
> ⑩ OYUNCULUK · ⑫ HOOK.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **LIGHT AND GRADE CONTINUITY** —
whether the light agrees with itself from clip to clip, and changes only
where the plan says it changes.

A film built from many separately generated clips has no gaffer. Each clip
invents its own key: from the left in one scene, from above in the next, warm
then cool, black shadows then lifted ones, a lamp that is lit in one frame
and dark in the next. The viewer cannot name it and feels it as "something
keeps resetting". **Every other lens looks at what the light falls on; you
look at the light.**

⛔ This is not the background lens. They ask whether the OBJECTS behind the
subject hold. You ask whether the LIGHT on everything holds. A lamp that
exists in every scene is their PASS; a lamp that is lit in one and dark in
the next is your finding.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, directions, temperatures
or jumps of any kind. Write the line, put every question in FLAGS, and stop.

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied (light calendar · atmosphere · sources)
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated.

**MODE D** — the plan declares zones, sources and the exact boundaries where
light may change. A change AT a declared boundary is a PASS; a change inside
a zone is a finding.

**MODE V** — you have no plan. You score self-consistency only: the same
place must be lit the same way twice. You may never call a change "unplanned"
against a plan you do not have — that goes to FLAGS.

---

## 📋 LIGHT LOCK LIST — MODE D ONLY

### ⬇️ OPERATÖR DOLDURDU — THE_OPEN_CIRCUIT_QA_SPEC.md'den C(IŞIK · ATMOSFER · YAPI · KASK) + GRID · MODE D

```

```


Read out of the supplied SPEC before you watch:

```
IŞIK TAKVİMİ    → zones: which scenes · which sources · where change is allowed
ATMOSFER        → medium: vacuum / thin / thick · shadow density · fill · haze
YAPI ANATOMİSİ  → how many light sources exist, and where
KASK            → visor: clear / tinted / mirrored — what may reflect in it
GRID            → scene start times. ⛔ THE GRID IS GIVEN: one frame per scene
                  at start + 5 s and one at the last second; a cut off the
                  grid is reported, never re-numbered.
```

Build the ZONE REGISTER (STEP 0) from these lines before the first frame.

---

## ⛔ STEP 0 — THE ZONE REGISTER (both modes — before scoring anything)

For every zone (mode D) or every distinct lit space you meet (mode V):

```
ZONE REGISTER
· zone            [name · scenes it covers]
· sources         [count · kind · position — "two ceiling heads, top"]
· key direction   [clock position as seen from camera · elevation]
· key quality     [hard / soft]
· shadow          [absolute black / lifted · edge hard / soft]
· temperature     [warm / neutral / cool]
· fill            [none / ambient / from a named source]
· medium          [vacuum — no haze, no bloom, no dust · air — what it allows]
· change allowed  [at which scene boundary, to what]
```

⛔ **THE MEDIUM SETS THE LAW.** In a vacuum there is no haze, no volumetric
beam, no bloom around a source, no lifted shadow. Register the medium; then
every glow that has no air to glow in is a finding.

---

## STEP 1 — BUILD THE LIGHT LEDGER (before judging anything)

One frame per scene at `start + 5 s`, one at the last second. One row per
scene:

```
S<n> | in | zone | key direction (clock · elevation) | quality | shadow
       density | temperature | practicals lit / present | subject exposure
       (bright · mid · dark) | background black level | in-clip change
```

- **Practicals lit / present**: count the sources you can see, and how many
  are lit. `2/2` and `1/2` are different rows.
- **In-clip change**: `0` if the light holds for the whole clip; otherwise
  name it — dimmer, flicker, drift in temperature, a source that fades — and
  the second it starts.

Then write the **KEY DIRECTION STRING**: one character per scene — the clock
hour of the key as seen from camera (`1`–`9`, `T` for top, `0` for 10, `E`
for 11, `W` for 12), `?` if no key is readable, `-` if no subject. It is a
fingerprint of where the light comes from.

### ⛔ THE ADJACENT-PAIR TEST — the only test this lens has

For every cut, put the last frame of the outgoing clip beside the first frame
of the incoming clip and answer in one line: *"What changed in the light?"*

- Same zone, something changed → **LIGHT JUMP**, one row in the jump log.
- Declared boundary, the declared thing changed → PASS, write it anyway.
- Declared boundary, something ELSE changed too → finding.

If the honest answer is "nothing", the cut is clean. **Write the line.** A
deduction with no adjacent-pair line is not a finding.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

```
① THE KEY THAT WALKS — the key light changes direction between clips of the
   same place.
② FILL FROM NOWHERE — shadows lifted in a medium that has no air to bounce
   light; a vacuum with soft shadows.
③ TEMPERATURE WOBBLE — warm, cool, warm across consecutive clips of one zone.
④ THE PRACTICAL THAT BLINKS — a lamp lit in one scene, dark in the next,
   lit again; or a source that exists only in some clips.
⑤ EXPOSURE SEESAW — the subject's brightness jumps at the cut, though nothing
   in the scene changed.
⑥ SATURATION CREEP — colour intensity drifts across the film with no cause.
⑦ THE IN-CLIP DIMMER — light changes inside a clip declared static.
⑧ HAZE IN A VACUUM — beams, bloom, glow, dust in a medium that forbids them.
⑨ THE LIT VISOR — reflections, tint or a glow in a visor declared clear.
⑩ BLACK THAT ISN'T — the background black lifts to grey in some clips.
⑪ THE SECOND SUN — two shadow directions on one subject in one frame.
⑫ THE FLAT FRAME — no key at all; even light from everywhere, no modelling.
```

---

## ═══ YOUR SCOPE ═══

```
✅ Where the light comes from, what it does to shadow and colour, whether
   sources are lit, whether any of it changes — and whether every change
   sits at a boundary the plan declared.
```

## ═══ NOT IN THIS PASS ═══

```
❌ Whether the lamp EXISTS and is the same lamp                → CONTINUITY / BACKGROUND
   (existence is theirs; lit / unlit and the light it casts are yours)
❌ Single-frame artefacts — banding, flicker noise, blown pixels → the FRAME lens
❌ Where the camera stands                                      → the SETUP lens
   (a return that changes POSITION is theirs; a return that changes LIGHT
    is yours; both can fail)
❌ Whether the palette CHOICE is good                           → the STORY lens
❌ Dust, particles, atmosphere as PHYSICS                        → the PHYSICS lens
   (a dust cloud's motion is theirs; the glow it makes in a vacuum is yours)
❌ In mode V, anything you think the PLAN intended — FLAGS only.
```

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material takes `N/A` and leaves the mean.

### 1. 🧭 KEY DIRECTION CONTINUITY
```
□ KEY DIRECTION STRING is constant inside every zone (pattern ①)
□ One shadow direction per subject per frame (pattern ⑪)
□ A key exists — the frame is modelled, not flat (pattern ⑫)
```

### 2. 🌑 SHADOW QUALITY & FILL
```
□ Shadow density matches the registered medium (pattern ②)
□ Shadow edge hardness is constant inside a zone
□ Fill, where it exists, has a named source
```

### 3. 🌡️ COLOUR TEMPERATURE
```
□ Constant inside a zone (pattern ③)
□ Each source keeps its own temperature every time it appears
□ No saturation drift across the film (pattern ⑥)
```

### 4. 💡 PRACTICAL SOURCES
```
□ Source count per zone matches the register, every scene
□ Every source is lit or dark consistently (pattern ④)
□ A source that is meant to change — brighten, die, be replaced — changes
  once, at the declared scene, and stays changed
```

### 5. ✂️ EXPOSURE AT CUTS
```
□ Subject exposure holds across every cut inside a zone (pattern ⑤)
□ Background black level holds (pattern ⑩)
□ Every jump has a row in the jump log with both timecodes
```

### 6. ⏸️ IN-CLIP STABILITY
```
□ No clip declared static changes its light inside the clip (pattern ⑦)
□ No flicker, breathing or drift in any source across a clip
```

### 7. 🚧 ZONE BOUNDARIES (mode D · N/A in mode V)
```
□ Light changes ONLY at the boundaries the plan declares
□ At each declared boundary, the declared thing changed and nothing else
□ The plan's single changing variable is readable across the boundary
```

### 8. 🌫️ ATMOSPHERE HONESTY
```
□ No haze, beam, bloom or glow in a medium that has no air (pattern ⑧)
□ The visor obeys its register — clear stays clear (pattern ⑨)
□ Any glow has a source and a medium that permit it
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
ZONES REGISTERED: [n] · MEDIUM: [vacuum / thin / thick — from the register]
LIGHT JUMPS: [n · from the jump log] · CLEAN CUTS: [n]

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Exclude it from every
count and every string.

ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (N/A excluded, never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
VERDICT: [LIGHT HOLDS / GRADEABLE DRIFT / KEY WALKS / ZONE BROKEN /
          LIT FROM NOWHERE]
         One finding outranks the mean: if the KEY DIRECTION STRING changes
         inside a zone at three or more cuts, the verdict is KEY WALKS
         regardless of the score.
```

## LIGHT LEDGER
[the full STEP 1 ledger — this is evidence, include it]

## KEY DIRECTION STRING
```
OBSERVED:  [one character per scene · 1-9 T 0 E W ? -]
ZONES:     [one letter per scene naming its zone — mode D]
```
⛔ Length = SCENES OBSERVED. If they disagree, say so on this line.

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` if a human figure is
visible anywhere in that scene, `-` if none. You write this even though it is
not your subject — it is the one axis on which every lens of the same film is
checked against every other. In a single-figure film it is nearly constant
and proves little on its own; write it anyway.

## LIGHT JUMP LOG
| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
|---|---|---|---|---|
One row per LIGHT JUMP from the adjacent-pair test. Write "no jumps" if none.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**
Write the deduction's source as ledger rows with timecodes. A deduction with
no listed source is not applied. A category with material but no in-scope
source keeps 10/10 and its Issue cell reads "no in-scope source".

| # | Category | Score | Issue (ledger rows and timecodes) |
|---|----------|-------|-----------------------------------|
| 1 | Key Direction Continuity | /10 | |
| 2 | Shadow Quality & Fill | /10 | |
| 3 | Colour Temperature | /10 | |
| 4 | Practical Sources | /10 | |
| 5 | Exposure at Cuts | /10 | |
| 6 | In-Clip Stability | /10 | |
| 7 | Zone Boundaries | /10 | |
| 8 | Atmosphere Honesty | /10 | |

## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

## THE THREE THAT MATTER
The three findings that most damage this film's light, in order, each with
its timecode and its one-line fix.

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION
Temperature, exposure and saturation drift are grade work — say so and name
the clip. Key direction, fill from nowhere, a source that blinks, haze in a
vacuum and in-clip dimming are baked into the pixels and require regeneration.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, lens named.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The adjacent-pair line is the whole method.** Every finding traces to
  "what changed in the light at this cut?"
- **The medium sets the law.** No air, no glow.
- **Existence is theirs; lit is yours.** Do not bill a missing lamp twice.
- **A change at a declared boundary is a PASS.** Write it anyway.
- **Grade drift and baked light are different bills.** Say which.
