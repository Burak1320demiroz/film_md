# HAM RAPOR — YERÇEKİMİ · FAZ 9 / DÜŞÜŞ · ON İKİ MERCEK

```
KÜNYE
koşu      : 06.09.2026 · Gemini · girdi "faz 9.mp4" · 120 s · 12 segment · 11 kesme
mercek    : ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK ·
            ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK
            ⭐ ⑨-⑫ depoda İLK KEZ koşuldu (06.09.2026 · D184)
mod       : on ikisi de V

⛔ ① SPEC KAPISI [D129]: YERCEKIMI_QA_SPEC.md YOK (README'de açık borç, D117),
   FILME_OZEL/ paketi YOK → on iki koşu da mod V. T tablolarına SATIR GİRMEZ.
   ⚠️ AMA BU FİLMDE SPEC'İN ADRESİ BAŞKADIR: 10-20 dk hattında QA birimi FAZDIR
   ve her fazın kendi rubriği vardır (`FAZ_0n_QA_PROMPT.md`, 761-1.674 satır).
   ⛔ FAZ 9'un rubriği YOK — üretilmiş dokuz fazın TEK rubriksizi. Operatörün
   elinde yapıştıracak faz rubriği olmadığı için genel mercekler koşuldu.
   Aynı karar FAZ 8'de 06.09'da alındı ve orada "YANLIŞ ALET" diye kaydedildi
   → İKİNCİ VAKA, ardışık iki fazda → [D185]

⛔ ⑪ ÖLÇÜM KAPISI: KOŞULMADI — proje sahibi kararı (06.09.2026): depo dışına
   çıkılmaz, master'a dokunulmaz. Aşağıdaki her süre/kesme sayısı RAPORUNKİDİR.
   ⚠️ Ama bu koşuda ölçüme İHTİYAÇ da yoktu: on iki raporun on ikisi de
   12 sahne · 11 kesme · 120 s · şerit `1111111111-1` yazdı. Depoda ilk kez
   ⑤ ÇAPRAZ SAYIM KAPISI hiçbir sapma bulmadan kapandı [D107].

⛔ ⑩ ÖNERME KAPISI — ÜÇ KİLİT KUSUR YAZILDI, ÜÇÜ DE PLANDA YAZILI:
   · KİLİT 43 (yerçekimi yağmuru / ivme rampası) → ⑥ "TWO GRAVITIES" 🔴
   · KİLİT 44 (renk takvimi: beyaz→turuncu→kızıl→beyaz→mavi) → ⑪ 3/10 · ② 🔴
   · 00_PLAN SAYISAL KİLİTLER: "F9: ivme rampası" — fazın KONUSU budur.
   → bu bulguların puanı geri verilir, hükümleri DÜŞER [D130 · D166]

⛔ ARİTMETİK: ⑤ ve ⑨'da "kusur yok" hücreleri 7/10 yazıldı (kural ④ ihlali:
   kaynaksız hücre `—` ya da 10/10'dur). ⑤ 6,5 → düzeltilmiş 9,0 · ⑨ 5,8 →
   düzeltilmiş 7,4 → [D186]

⛔ ④/⑫ KAPSAM: ikisi de bir ORTA FAZI (16:00-18:00, 20 dakikalık filmin
   %80-90 bandı) bağımsız kısa film sanarak Hook · Yapı · Final · Tutundurma
   puanladı ve kesme listesi yazdı → [D185]
```

---

## ① KARE

```
FORMAT: YATAY
INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
FILM: (not supplied) · FORMAT: YATAY · ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied) · SCENE: Compilation
VIDEO DURATION: 120s measured · MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 11 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50)
NON-SCENE MATERIAL: none
LINES HEARD: none — room tone present
SPEC BLOCK PROVIDED: no — mode V

SCORED CATEGORIES: 7 · SUM 55.0 · 55.0 ÷ 7 = 7.8
OVERALL SCORE: 7.8/10 (7 scored, 4 excluded)
VERDICT: REGENERATE
```

| Category | Score | Critical Issues |
|---|:--:|---|
| Character | 6/10 | −4 · 1:01 (fused fingers) · 1:51 (strap clipping) |
| Scale & Physics | 6/10 | −4 · 0:35 (pen bending) · 1:45 (strings phasing) |
| Camera | 10/10 | none |
| Lighting | 9/10 | −1 · 1:25 (AI bloom) |
| Environment | 10/10 | none |
| Creatures | — | no in-scope source |
| Particles & Materials | 7/10 | −3 · 0:34 (cloth phasing) |
| Dialogue & Audio | — | no in-scope source |
| Frame Anchor Fidelity | — | UNVERIFIABLE |
| Negative Violations | 3 count | 1:01 · 1:45 · 1:51 |
| Motion Quality | 7/10 | −3 · 0:25 (jello effect on watch) |
| Vertical Format / Safe Zone / Hook Timing | N/A | format is YATAY |

SCENE INVENTORY — gravity read: "Shifts entirely mid-edit. 0:00-0:40 zero-g
(hair and props float). 0:50-2:00 reads 1g (steam dissipates downward, paper
drops, character slumps)." Light sources: harsh white/blue exterior sunlight,
dark red interior emergency lighting, soft cabin lighting.

NEGATIVE BIBLE: [x] Object phasing/clipping · [x] Extra fingers / hand-surface
fusion · [x] AI bloom. BOX COUNT: 3 · LINKED FINDINGS: 5 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 5 · TICKED: 3 · MISSED: 0
NO BOX EXISTS FOR: jello effect / warping (Category 11)

PRESENCE STRING: `1111111111-1`
SEVERITY TALLY: 🔴 4 · 🟠 2 · 🟡 1

TOP 3:
1:51 — 🔴 — grey shoulder harness strap phases completely through the white suit during the downward jolt.
1:01 — 🔴 — right hand (resting on lap) lacks distinct fingers, fused into a single fleshy mass.
1:45 — 🔴 — multiple parachute suspension lines phase out of existence and disconnect mid-air.

DETAILED ERROR LOG
0:25 — 🟠 — Motion Quality — watch face and hands suffer severe jello effect, warping as the hand shifts.
0:34 — 🟠 — Particles & Materials — floating fabric strap phases through itself while spinning in zero-g.
0:35 — 🔴 — Scale & Physics — the floating metal pen bends entirely in half like rubber as it rotates.
1:01 — 🔴 — Character — extra fingers / hand-surface fusion on the right hand.
1:25 — 🟡 — Lighting — slight AI bloom/haze around the plasma/fire outside the window.
1:45 — 🔴 — Scale & Physics — parachute lines phase through the sky and disconnect from the capsule.
1:51 — 🔴 — Character — harness strap clips cleanly through the shoulder.

WHAT WORKED WELL: interior lighting transitions (stark daylight → red emergency)
render with realistic bounce and shadow falloff. Skin texture and subsurface
scattering in tight facial close-ups (0:10, 0:40) stay photoreal, not plastic.

PROMPT SUGGESTIONS: ADD "rigid solid objects, zero-g continuous physical
momentum, maintaining structural integrity"; ADD "anatomically correct hands,
distinctly separated fingers resting naturally"; REMOVE "cinematic glowing
window".

NEW LESSON CANDIDATE: No new lesson — all errors map to patterns 3, 4, 8.
OUT-OF-SCOPE FLAGS: none
FLAGS FOR DOCUMENT CHECK: 0:50 — gravity shifts entirely from zero-g to 1g —
QUESTION: Does the script specify a gravity transition/atmospheric entry at
this exact scene boundary?

QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 6/10 | 6/10 | 10/10 | 9/10 | 10/10 | | 7/10 | | | 7/10 | | | | 3 | 7.8/10 |

---

## ② DEVAMLILIK

```
FILM: (not supplied) · RUNTIME: 120s measured
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CHARACTERS TRACKED: 1
SETUP INVENTORY: distinct setups: 12 · repeat map: none · angle types: 4
   (eye level, low, high, profile)
NON-SCENE MATERIAL: none · LINES HEARD: none — room tone present
MATERIAL TYPE: FILM (undeclared) · BASELINE: SELF-CONSISTENCY

SCORED CATEGORIES: 10 · SUM 72.0 · 72.0 ÷ 10 = 7.2
OVERALL SCORE: 7.2/10
VERDICT: IDENTITY BREAK
```

SCENE INVENTORY: S1 window/Earth zero-g · S2 face in warm light · S3 hand on
worn armrest · S4 pen and straps floating · S5 ECU face red light · S6 slumped,
steam/smoke falling, 1G · S7 looking at watch, red · S8 head leaning back, red ·
S9 window, light turns white · S10 unconscious, white light · S11 EXTERIOR
capsule under parachute · S12 wakes with a jolt on the ground.

CHARACTER PASSPORT — Caucasian female, short dark brown chin-length bob,
cut/scar on LEFT forehead, cream/white suit with orange sleeve stripes, thick
grey chest harness, black watch with silver bezel on left wrist, no helmet.
FACE-VISIBLE: 60 s of 120 s · 6 of 12 scenes. COSTUME-VISIBLE: 9 of 12.

APPEARANCE TABLE — S3: "Hand only. Veiny, hairy, reads as male." · S6: "Grey
quilted chest panel, no orange stripes visible." · S7/S8: "Face clean, scar
missing." · S10: "Suit completely white/grey straps, no orange stripes."
· S12: "Orange stripes return."

| # | Category | Score | Critical Issue |
|:--:|---|:---:|---|
| 1 | Identity — Face, Hair & Build | 5/10 | −5 · 0:10 (S2) · 0:20 (S3) |
| 2 | Costume Identity | 5/10 | −5 · 0:00 (S1) · 1:30 (S10) |
| 3 | Wear, Damage & Injury | 5/10 | −5 · 0:10 (S2) · 1:00 (S7) |
| 4 | Equipment & Carried Objects | 10/10 | none |
| 5 | Cross-Cut Action | — | no in-scope source |
| 6 | Physical Consistency | 10/10 | none |
| 7 | Counter Logic | N/A | NONE |
| 8 | Spatial Geography | 6/10 | −4 · 0:50 (S6) · 1:50 (S12) |
| 9 | Time & Light Logic | 10/10 | none |
| 10 | World State & Props | 6/10 | −4 · 0:50 (S6) · 1:30 (S10) |
| 11 | Causality & Knowledge | 10/10 | none |
| 12 | Quantity & Character Count | 5/10 | −5 · 0:50 (S6) · 1:30 (S10) |
| 13 | Setup & Abandonment | N/A | NONE |

PRESENCE STRING: `1111111111-1`
SEVERITY TALLY: 🔴 2 · 🟠 3 · 🟡 0

CONTRADICTION LOG
| 0:10-0:20 | 0:20-0:30 | BODY | 1 | slender female face/build vs hairy, veiny male hand | 🔴 |
| 0:50-1:00 | 1:30-1:40 | WORLD | 12 | 2 red seats vs 3 white seats | 🔴 |
| 0:00-0:10 | 1:30-1:40 | BODY | 2 | thick orange arm stripes vs pure white suit with grey straps | 🟠 |
| 0:10-0:20 | 1:00-1:10 | BODY | 3 | cut on left forehead vs perfectly clean skin | 🟠 |
| 0:50-1:00 | 1:30-1:40 | WORLD | 10 | red flat-backed seats vs heavily padded white contoured seats | 🟠 |

WEAR TIMELINE: cut on left forehead — present 0:10, 0:40 · ABSENT 1:00, 1:10 ⚠️ · one-way? No
LOCATION MAP: Capsule Interior (S1-S10, S12) CONTRADICTED — "Seat counts, wall
shapes, and hatch locations change completely across shots." Capsule Exterior
(S11) CONSISTENT.

THE THREE THAT MATTER
The Male Hand (0:20) — identity break; cut scene 3.
The Shrinking/Growing Seats (0:50 / 1:30) — 2-seat → 3-seat → 1-seat; regenerate 6 and 10.
The Healing Face (1:00) — forehead cut disappears; add in post for scenes 7 and 8.

FLAGS FOR DOCUMENT CHECK
Gravity shifts abruptly at 0:50 — Was atmospheric entry / a gravity return
scripted to happen exactly at scene 6?
Visor state unreadable throughout — Is the astronaut intended to be helmetless?

OUT-OF-SCOPE FLAGS
0:20-0:30 watch face morphs and jellos → FRAME lens
1:01 right hand fingers fused into one mass → FRAME lens
1:51 strap clips cleanly through the suit shoulder → FRAME lens

---

## ③ SES

```
AUDIO STATE: B — no dialogue present, sound only
BASELINE: SELF-CONSISTENCY
FILM: (not supplied) · RUNTIME: 120s measured
SPOKEN LINES: 0 · CUTS COUNTED: 11 · NON-SCENE MATERIAL: none
LINES HEARD: none — room tone present
DISTINCT VOICES: 0 · REGISTERS: 0 human / 0 machine / 0 unclear

SCORED CATEGORIES: 3 · SUM 18.0 · 18.0 ÷ 3 = 6.0
OVERALL SCORE: 6.0/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX
```

AMBIENCE MAP — S1-S10 Capsule Interior 0:00-1:40 low cabin hum, room tone, LOW,
"bed drops out momentarily at every single cut" · S11 Exterior 1:40-1:50 wind,
atmosphere, MID, hard cut in / hard cut out · S12 Interior 1:50-2:00 low cabin
hum, returns abruptly.
LAYER COUNT: 0:15 room tone (1) · 0:55 room tone (1) · 1:45 exterior wind (1).
MUSIC LEDGER: (none — no music present)

| Category | Score | Critical Issue |
|---|:--:|---|
| Speaker Attribution / Synthetic Tells / Voice Identity / Delivery / Turn-Taking | N/A | no dialogue present |
| Ambience Continuity | 4/10 | −6 · every cut 0:10 … 1:50 |
| SFX Causality & Sync | 5/10 | −5 · 0:50 (S6) · 1:50 (S12) |
| Mix Hierarchy & Levels | 9/10 | −1 · 1:40 (S11) |
| Music & Silence | N/A | no music present |

SEVERITY TALLY: 🔴 1 · 🟠 1 · 🟡 1
AMBIENCE HOLE LOG: drops at 0:10 (and all cuts), returns +1 frame, Capsule
Interior, absolute silence? **No (floor still present, bed thins)** — 🔴 BLOCKER
CONTRADICTION LOG: 1:30-1:40 vs 1:40-1:50 — interior cabin hum hard-cuts
immediately to loud exterior wind with no transition — 🟡 MINOR

THE THREE THAT MATTER
Ambience Drops at Every Cut (0:10-1:50) — lay a continuous room tone under the interior edit.
Missing Impact SFX (1:50) — the wake-up jolt has zero physical sound.
Missing Environmental SFX (0:50) — heavy steam/smoke drops with no hiss or vent.

FIXABLE IN THE MIX: all three — Low cost.
FLAGS: "The entire 120s runtime contains only raw, disconnected room tone. Was a
full sound design and foley pass intended, or is this a scratch track?"
OUT-OF-SCOPE FLAGS: none

---

## ④ HİKAYE

```
FORMAT: YATAY · INPUT MODE: V · BASELINE: THE FILM AS SCREENED
MATERIAL TYPE: FILM (undeclared) · FILM: (not supplied)
LENGTH CLASS: (not supplied) · RUNTIME: 120s measured
SCENE COUNT: 12 counted, not from a document
CUTS COUNTED: 11 (0:10 … 1:50) · NON-SCENE MATERIAL: none
LINES HEARD: none — room tone present · SPEC BLOCK PROVIDED: no — mode V

ENDS OR STOPS: "The film ends with a visceral jolt as the astronaut wakes upon
   landing, providing a physical conclusion but lacking emotional payoff."
PEAK LOCATED AT: 1:40 (S11) capsule under parachute, but the film's shape builds
   toward an external physics event rather than a character-driven climax.

N/A LEDGER: 1 of 10 categories scored N/A — Dialogue
OVERALL was computed over 9 categories.
SCORED CATEGORIES: 9 · SUM 36.0 · 36.0 ÷ 9 = 4.0
OVERALL STORY SCORE: 4.0/10
VERDICT: REVISE STRUCTURE
```

THE FILM IN ONE SENTENCE: *"An astronaut sits in a capsule during a turbulent
re-entry, passes out, and wakes up safely on the ground."*

| Category | Score | Core Issue |
|---|:--:|---|
| Hook | 4/10 | −6 · 0:00 (S1) establishes a place, not a situation; no stakes until 0:40 |
| Premise & Clarity | 6/10 | −4 · 0:20 (S3) abrupt insertion of a seemingly different character's hand |
| Structure & Pacing | 4/10 | −6 · 0:10-0:40 (S2-S4) redundant waiting beats stall escalation entirely |
| Character | 3/10 | −7 · protagonist makes zero choices; fails camera-carrier test |
| Theme | 3/10 | −7 · 1:50 (S12) survival depicted, but no cost paid or theme dramatized |
| Dialogue | — | no in-scope source (silent film) |
| Emotional Arc | 4/10 | −6 · 1:30 (S10) tension purely external, no internal low point |
| Ending | 5/10 | −5 · 1:50 (S12) stops at waking up; does not recontextualize |
| Originality | 3/10 | −7 · repeats standard re-entry tropes without a unique novum |
| Retention Risk | 4/10 | −6 · 0:20 (S3) 20 seconds with no new information or question |

THE THREE THINGS THAT MOST HURT THIS FILM
0:00-0:40 (S1-S4) — Delayed Start — 40 seconds before the red light indicates trouble; a third of the film with zero narrative stakes.
0:00-2:00 — Lack of Interiority — the astronaut is entirely passive; never makes a decision, touches a control, or displays agency.
1:00-1:20 (S7-S8) — Redundant Escalation — two back-to-back red-light shots reacting to nothing new.

THE THREE THINGS WORTH PROTECTING
0:40 (S5) — The Turn — switch to ECU and red light is an effective wordless tone shift.
1:40 (S11) — The Reveal — exterior parachute shot gives scale and geographic context.
1:50 (S12) — The Final Jolt — the physical reaction sells the harsh landing.

THE ONE THING NOTHING ELSE DOES: "No unique element found. The film is a highly
standard, beautifully rendered but completely conventional depiction of orbital
re-entry."

SCENE-BY-SCENE VERDICT: S1 KEEP · S2 MERGE · S3 CUT · S4 CUT · S5 KEEP ·
S6 KEEP · S7 CUT · S8 REWRITE · S9 KEEP · S10 TIGHTEN · S11 KEEP · S12 KEEP

RANKED CUT LIST (to lose 30 seconds)
resulting runtime: 90s — BELOW FORMAT FLOOR, replace don't remove.
1. S3 (0:20-0:30) — 10s — cut the disembodied hand shot.
2. S4 (0:30-0:40) — 10s — cut the floating pen; redundant zero-g establishment.
3. S7 (1:00-1:10) — 10s — cut the red-light watch check; redundant waiting beat.

RETENTION DROP-OFF FORECAST
0:25 — S2/S3 provide no narrative question; "it just looks like a screensaver" — introduce the red light / danger at 0:15.
1:10 — S7/S8 repeat the same red-light tension without escalating — show her attempting a physical fix or bracing for impact.

SHAREABLE MOMENT: 1:40 (S11) — the capsule piercing the clouds under the
massive orange-and-white parachute.

REWRITE PRESCRIPTIONS
SCENE 4: replace [floating pen shot] with [astronaut spotting an urgent warning on a console].
SCENE 8: replace [head leaning back passively] with [astronaut desperately throwing a manual override switch].
SCENE 10: move to position 11 (after parachute reveal).

OUT-OF-SCOPE FLAGS: 0:20-0:30 the hairy male hand completely breaks character identity → CONTINUITY lens
FLAGS FOR DOCUMENT CHECK: does the plan declare an emotional peak, and is it the
exterior parachute shot at 1:40? · is the film's last planned scene the one at 1:50?

STORY TRACKING ROW
| (not supplied) Ⓥ | YATAY | (not supplied) | 4/10 | 6/10 | 4/10 | 3/10 | 3/10 | — | 4/10 | 5/10 | 3/10 | 4/10 | 4.0/10 | ⚠️ ŞARTLI |

---

## ⑤ ARKA PLAN

```
FILM: (not supplied) · RUNTIME: 02:00 measured
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · NON-SCENE MATERIAL: none
BASELINE: SELF-CONSISTENCY

SCORED CATEGORIES: 6 · SUM 39.0 · 39.0 ÷ 6 = 6.5
OVERALL SCORE: 6.5/10
VERDICT: FIELD DRIFTS BUT RECOVERABLE
```

SUBJECTS EXCLUDED: S1 woman looking out window · S2 woman's face · S3 hand, arm,
watch · S4 floating pen, cloth, strap · S5 woman's eyes · S6 woman in spacesuit
venting steam · S7 woman checking watch · S8 woman's face sleeping · S9 woman
looking out window · S10 woman sleeping in spacesuit · S11 falling capsule and
parachute · S12 woman waking and unbuckling.

BACKGROUND INVENTORY (abridged to its load-bearing lines)
S1  MID: 2 empty seats to the right, red emergency lever · FAR: none — enclosed
    interior · CEILING: padded off-white panels · EDGES: Clean
S6  MID: 2 red empty seats (flanking subject), control panel left, round window
    left, large round hatch right · CEILING: padded grey with circular overhead
    vent · FOCUS: all elements relatively sharp · EDGES: Clean
S10 MID: 2 empty white seats right, round window left, large round hatch right
    · CEILING: white padded panels · EDGES: Clean
S11 MID: none · FAR: flat desert plain, bottom third · SKY: blue, light
    scattered clouds · EDGES: Clean
S12 MID: 1 empty white seat right, round window left, large round hatch right,
    floor debris · EDGES: Clean

| # | Category | Score | Critical Issue |
|:--:|---|:---:|---|
| 1 | Background Figure Integrity | N/A | no background figures |
| 2 | Background Figure Behaviour | N/A | no background figures |
| 3 | Crowd Count & Density | N/A | no crowds |
| 4 | Horizon & Topology | 7/10 | none |
| 5 | Depth, Parallax & Scale | 7/10 | none |
| 6 | Background Set & Props | 4/10 | −3 · 0:00 vs 0:50 (capsule topology alters) |
| 7 | Focus Honesty | 7/10 | none |
| 8 | Sky & Atmospherics | 7/10 | none |
| 9 | Frame Edges & Emergent Artifacts | 7/10 | none |

PRESENCE STRING: `1111111111-1`
SEVERITY TALLY: 🔴 0 · 🟠 1 · 🟡 0
FIELD DRIFT MAP: S6 · mid · first slip 0:50 · undeniable by 0:55 · recovered? No
COUNT LOG: Capsule Seats · S1, S6, S10 · first clean count 3 (1 occupied, 2 empty
   right) · last clean count 3 (occupied left, 2 empty right) · Shifts positions
CONTRADICTION LOG: 0:00 vs 0:50 · mid · cat 6 · "S1 shows 2 seats right of window
   and no hatch; S6 introduces a massive right hatch and shifts seat layouts" · 🟠

THE THREE THAT MATTER: Interior Architecture Shift — the capsule rear wall
topology changes radically S1 → S6 → S10. Fix: accept it (tight cropping fails
due to wide angles).

FLAGS: Seat counts shift around the subject — is the capsule meant to have three
modular seats? · Red ambient light dominates middle scenes — does the interior
lighting change intentionally due to an emergency?
OUT-OF-SCOPE FLAGS: woman's spacesuit design and patches change continuously
between S1, S6 and S12 (Continuity Lens).

---

## ⑥ FİZİK

```
INPUT MODE: V · FILM: (not supplied) · RUNTIME: 02:00 measured
FRAME RATE ASSUMED: 24 fps · SCENES OBSERVED: 12 · CUTS COUNTED: 11
NON-SCENE MATERIAL: none · LINES HEARD: none — nothing audible to me
GRAVITY: GRAVITY ESTIMATE: Fractured (≈0.1 m/s² to ≈3.2 m/s²), using L4 (pen
   drop) and L7 (human slump)
PREMISE REGISTER: none

SCORED CATEGORIES: 6 · SUM 46.0 · 46.0 ÷ 6 = 7.6
OVERALL SCORE: 7.6/10
VERDICT: TWO GRAVITIES
```

PHYSICS LEDGER
| # | TC | Event | Duration | Distance + RULER | Implied | Consistent? |
| L1 | 0:00-0:10 | woman's hair floats in cabin | 10.0 s | ≈0.2 m (hair length) | microgravity (0g) | setting |
| L2 | 0:30-0:40 | pen and cloth float mid-air | 10.0 s | 0 m | microgravity (0g) | L1 |
| L3 | 0:50-0:58 | steam vents vertically downward | 8.0 s | ≈0.5 m (head to chest) | fast downward accel | new gravity state |
| L4 | 0:52-0:56 | pen and cloth fall past woman | 4.0 s | ≈0.8 m (seated torso) | g ≈ 0.1 m/s² | contradicts L3, L7 |
| L5 | 1:30-1:40 | objects rest on the floor | 10.0 s | 0 m | gravity active | L4 direction |
| L6 | 1:40-1:50 | capsule hangs under parachute | 10.0 s | 0 m (rel. frame) | terminal velocity | expected |
| L7 | 1:51-1:52 | woman slumps forward against belts | 0.5 s | ≈0.4 m (head drop) | g ≈ 3.2+ m/s² | Earth gravity |

| # | Category | Score | Critical Issue |
|:--:|---|:---:|---|
| 1 | Gravity & Free Fall | 3/10 | 🔴 −7 · L4 (0:52) vs L7 (1:51) |
| 2 | Ballistics & Trajectories | N/A | no throws or launches |
| 3 | Impact & Momentum | N/A | no impacts or collisions |
| 4 | Material Behaviour | 7/10 | 🟡 −3 · L4 (0:52) |
| 5 | Particles & Atmosphere | 6/10 | 🟠 −4 · L3 (0:50) vs L4 (0:52) |
| 6 | Scale & Measurement | 10/10 | none |
| 7 | Rates & Timing | N/A | no established rates or timers |
| 8 | Light & Shadow Physics | 10/10 | none |
| 9 | Human Biomechanics | 10/10 | none |

PRESENCE STRING: `1111111111-1`
SEVERITY TALLY: 🔴 1 · 🟠 1 · 🟡 1

GRAVITY TABLE
| L4 | 0:52-0:56 | ≈0.8 m (seated torso) | 4.0 s | ≈0.1 m/s² | contradicts L7 (much slower) |
| L7 | 1:51-1:52 | ≈0.4 m (head slump) | 0.5 s | ≈3.2 m/s² | contradicts L4 (much faster) |

CONTRADICTION LOG
| L4 vs L7 | 0:52 vs 1:51 | 1 | falling pen implies g≈0.1; slumping human implies g≈3.2 | 🔴 |
| L3 vs L4 | 0:50 vs 0:52 | 5 | venting steam falls rapidly downward while a solid pen falls in extreme slow-motion in the exact same shot | 🟠 |

THE THREE THAT MATTER
Two Gravities (Floating vs Dropping) — "zero-G in Scene 4, lunar/slow-motion in
Scene 6, Earth-normal in Scene 12. A viewer feels the physics engine restarting
on every cut." Fix: **Regenerate Scene 6 falls to match Scene 12's gravity, or
crop the objects out.**
Mismatched Fall Rates in Scene 6 — steam drops quickly while pen and cloth drop
in slow motion beside it. Fix: crop out the left side of the frame in Scene 6.
Rigid Cloth — the falling cloth acts like a solid board, falling exactly
parallel with a metal pen. Fix: crop out the left side of the frame in Scene 6.

FLAGS FOR DOCUMENT CHECK
"The film transitions from microgravity (0:30) to low gravity (0:52) to normal
gravity (1:51). Does the narrative plan call for a gradual restoration of
gravity via thrust/re-entry, or is this an engine hallucination?"
"Parachute descent (1:40) shows absolute static background with zero atmospheric
buffeting — locked-off perspective, or should there be ambient descent motion?"

OUT-OF-SCOPE FLAGS: spacesuit design, collar structure and arm patches change
completely between Scene 6 and Scene 12 (Continuity lens).

---

## ⑦ AKSİYON

```
MEDIA: video played · INPUT MODE: V · FILM: (not supplied)
RUNTIME: 02:00 measured · FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · NON-SCENE MATERIAL: none
PRESENCE STRING: 1111111111-1 · LINES HEARD: none — nothing audible to me
BEATS COUNTED: 1
BEATS READABLE: 0 readable · 1 partial · 0 unreadable
PREMISE REGISTER: none

SCORED CATEGORIES: 6 · SUM 33.0 · 33.0 ÷ 6 = 5.5
OVERALL SCORE: 5.5/10
VERDICT: BEATS ILLEGIBLE
```

ACTION BEAT LEDGER
| B1 | 1:51–1:58 | actor reaches down to unbuckle lap restraints | resisted by the
buckle mechanism | contact: occluded | outcome: unbuckles (implied) | force
direction: down (gravity) | readable? PARTIAL |
Narration: *"She wakes up after the landing impact, slumps forward against her
straps, and reaches down to unfasten her seatbelt, but her hands are hidden in
her lap."*

BEAT STRING: `-----------p`

| # | Category | Score | Issue |
|:--:|---|:---:|---|
| 1 | Beat Anatomy | 6/10 | −4 · B1 (1:51) contact occluded |
| 2 | Spatial Geography Under Motion | N/A | no motion between positions |
| 3 | Threat Vector & Approach | N/A | no approaching threat |
| 4 | Contact Legibility | 4/10 | −6 · B1 (1:51) contact point hidden behind lap |
| 5 | Consequence Visibility | 5/10 | −5 · B1 (1:51) no visible state change in the belt |
| 6 | Camera's Contract with the Action | 6/10 | −4 · B1 (1:51) lens angle truncates the decisive contact area |
| 7 | Agency & Intent | 10/10 | none |
| 8 | The Stakes Object | 2/10 | −8 · B1 (1:51) the buckle/belt is off-screen at resolution |
| 9 | Physical Tempo & Escalation | N/A | only one beat present |

SEVERITY TALLY: 🔴 0 · 🟠 1 · 🟡 0
UNREADABLE MOMENTS: 1:51 — "whether the belt actually unbuckled or if she just
rested her hands, because the buckle is out of frame" — pattern ⑫ — 🟠
CONTRADICTION LOG: none observed

THE THREE THAT MATTER: Stakes Object Off-Screen (1:51) — "The film's single
physical action beat centers on releasing a seatbelt, but the camera frames out
the buckle." Fix: regenerate S12 with slightly lower/wider framing, or accept as
implied action.

FLAGS: "The film contains only one minor physical attempt at the very end. Is
this intended to be a purely observational/atmospheric film without standard
physical action beats?"
OUT-OF-SCOPE FLAGS: spacesuit design and patches change completely between the
interior scenes (S6 vs S12) (Continuity Lens).

---

## ⑧ EFOR

```
MEDIA: video played · INPUT MODE: V · FILM: (not supplied)
RUNTIME: 02:00 measured · FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · NON-SCENE MATERIAL: none
PRESENCE STRING: 1111111111-1 · LINES HEARD: none — nothing audible to me
EXERTION EVENTS: 2 · EVENTS WITH NO STRAIN SHOWN: 1
BODY: suited human · PREMISE REGISTER: none

SCORED CATEGORIES: 6 · SUM 37.0 · 37.0 ÷ 6 = 6.2
OVERALL SCORE: 6.2/10
VERDICT: MINOR DEBT
```

EFFORT LEDGER
| E1 | 0:50–1:00 | survive cabin steam/gas venting | environmental | 10.0 s |
STRAIN: torso, head | RECOVERY: none | debt 2 |
Bill test: *"Nothing is different; she sits passively and then is back to
normal, relaxed watch-checking in the next scene."*
| E2 | 1:50–2:00 | recover posture after hard landing | high-G impact | 10.0 s |
STRAIN: torso, arms, head | RECOVERY: posture slump | debt 7 |
Bill test: *"Her torso collapses forward heavily into the lap restraints,
showing the severe toll of the physical impact."*

COST CURVE: `000002244447`
RESET LOG: none — "the curve only rises or holds; no falls observed"

| # | Category | Score | Issue |
|:--:|---|:---:|---|
| 1 | Strain During the Work | 8/10 | 🟡 −2 · E1 (0:50) passive response to venting |
| 2 | Breath & Recovery | 3/10 | 🟠 −7 · E2 (1:50) no chest heave / visible breath post-impact |
| 3 | Fatigue Accumulation | 10/10 | none |
| 4 | Load in the Body | N/A | no carried mass |
| 5 | Injury Persistence & Cost | 2/10 | 🟠 −8 · 0:10, 0:40, 1:10 (pattern ④ injury as makeup) |
| 6 | Grip & the Price of Holding On | N/A | no sustained grip tasks |
| 7 | Equipment Burden | 4/10 | 🟠 −6 · 1:00, 1:50 (pattern ⑥ the suit that isn't there) |
| 8 | Pain, Restraint and Proportion | N/A | no acute pain events |
| 9 | Recovery Curve Honesty | 10/10 | none |

SEVERITY TALLY: 🔴 0 · 🟠 3 · 🟡 1
UNPAID WORK: 0:50 — surviving extreme environmental venting/smoke — should have
shown coughing, squinting, visceral rejection of the gas, bracing — pattern ⑫ — 🟡
CONTRADICTION LOG: 0:50 vs 1:00 — "A cabin fills with dense steam/gas, but
seconds later the actor calmly and cleanly checks her watch with no residual
coughing, fogged visor, or distress." — 🟠

THE THREE THAT MATTER
Breath doesn't track work (1:50) — "her chest never heaves, zero visible
breathing. She looks like a powered-down mannequin rather than an exhausted
survivor." Fix: regenerate S12 with "heavy breathing, chest heaving".
The suit that isn't there (1:00, 1:50) — "the actor raises her arm to check her
watch and reaches down to unbuckle with the exact frictionless dexterity of
someone wearing a light autumn jacket." Fix: accept it in edit.
Injury as makeup (0:10, 0:40, 1:10) — "a cut/abrasion on her forehead and cheek
that persists throughout. It never causes a wince, she never favors it, and she
never touches it." Fix: accept it.

FLAGS: "The actor goes from awake to unconscious multiple times before the
landing. Does the narrative plan call for G-force blackouts or oxygen
deprivation?"
OUT-OF-SCOPE FLAGS: the design, color and patches of the spacesuit change
continuously across the scenes (Continuity Lens).

---

## ⑨ KADRAJ  ⭐ depoda ilk koşu

```
INPUT MODE: V · FILM: (not supplied) · RUNTIME: 02:00 measured
FRAME RATE ASSUMED: 24 fps · GRID GIVEN: none (mode V)
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none
NON-SCENE MATERIAL: none · PRESENCE STRING: 1111111111-1
LINES HEARD: none — nothing audible to me
SETUPS REGISTERED: 12 · LOCKOFF HELD: 12 / 12 clips

SCORED CATEGORIES: 5 · SUM 29.0 · 29.0 ÷ 5 = 5.8
OVERALL SCORE: 5.8/10
VERDICT: RHYME BROKEN
```

SETUP LEDGER (observed letter / size / angle / position / anchor / in-clip movement)
S1 A MS eye behind-right · window · 0 — S2 B CU eye front · headrest · 0
S3 C CU high, hand on armrest · armrest · 0 — S4 D MS eye side-front · seat back · 0
S5 E ECU eye front · eyes · 0 — S6 F WS eye front · seats · 0
S7 G MS eye side · wall panel · 0 — S8 H CU eye front · headrest · 0
S9 I MS eye directly behind · window · 0 — S10 J WS eye front · three seats · 0
S11 K EWS eye wide exterior · horizon · 0 — S12 L WS eye side · door frame · 0

SETUP STRING
```
OBSERVED:   ABCDEFGHIJKL
PLAN:       none (mode V)
DIFFERS AT: none
```

RHYME PAIR
| setup letter / size / angle / anchor / the one variable | A / MS / eye / window / N/A | L / WS / eye / door frame / N/A | No |
**PAIR FAILS** — "The closing frame abandons the opening setup entirely for a
new scale and angle."

LOCKOFF VERIFICATION: all held.

| # | Category | Score | Issue |
|:--:|---|:---:|---|
| 1 | Setup Fidelity | N/A | no in-scope source (Mode V) |
| 2 | Lockoff Integrity | 7/10 | flawless lockoffs mapped to 7 |
| 3 | Rhyme Pair | 3/10 | S1 (00:00) and S12 (01:50) mismatch |
| 4 | Return Consistency | 7/10 | no distinct returns attempted/failed |
| 5 | Cluster Seams | N/A | no in-scope source |
| 6 | Angle Arc & Deliberate Shocks | 5/10 | blind jumps due to absent plan |
| 7 | Screen Geometry | 7/10 | geometry stable mapped to 7 |

SEVERITY TALLY: 🔴 1 · 🟠 0 · 🟡 0
THE THREE THAT MATTER: 01:50 — RHYME PAIR — closing frame setup does not match
opening setup; regenerate to match S1. 🔴
FIXABLE vs REGENERATION: "A wrong setup on the final scene cannot be moved in
post. The rhyme pair failure requires fully regenerating S12 to match the S1
camera position."
FLAGS: "Did the plan intentionally request 12 distinct camera setups with zero
returns?"
OUT-OF-SCOPE FLAGS: lighting environment shifts heavily between cuts (e.g.
normal to red light) — LIGHT lens. Suit detailing and colour consistency
fluctuates — CONTINUITY lens.

---

## ⑩ OYUNCULUK  ⭐ depoda ilk koşu

```
INPUT MODE: V · FILM: faz 9.mp4 · RUNTIME: 02:00 measured
FRAME RATE ASSUMED: 24 fps · GRID GIVEN: none (mode V)
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none
NON-SCENE MATERIAL: none · PRESENCE STRING: 1111111111-1
LINES HEARD: none — nothing audible to me
CHANNEL REGISTER: face [visible], eyes [readable], hands [bare], posture
   [available], head [available], tempo [available], breath [none visible],
   proximity [available]
ANCHOR BEATS: CHOICE N/A · COST N/A · FINAL N/A (mode V)
SCENES TASK ONLY: 2

SCORED CATEGORIES: 9 · SUM 74.0 · 74.0 ÷ 9 = 8.2
OVERALL SCORE: 8.2/10
VERDICT: MOSTLY LEGIBLE
```

PERFORMANCE LEDGER — the sentence per scene
S1 0:05 "She contemplates the view, feeling awestruck or quietly reflective." — posture, head — LEGIBLE
S2 0:15 "She feels a quiet, resolute anxiety." — face, eyes — LEGIBLE
S3 0:25 "She waits with tense stillness." — hands, tempo — PARTIAL
S4 0:35 "She sits disengaged from her immediate surroundings." — posture — TASK ONLY
S5 0:45 "She feels sudden alarm or intense hyper-focus." — face, eyes — LEGIBLE
S6 0:55 "She endures a catastrophic event with catatonic shock." — posture — LEGIBLE
S7 1:05 "She calmly assesses her remaining time." — posture, gaze, hands — LEGIBLE
S8 1:15 "She yields to exhaustion and accepts the end." — face, eyes, posture — LEGIBLE
S9 1:25 "She watches the end approach with frozen stillness." — posture, head — PARTIAL
S10 1:35 "She is unconscious." — posture, head — LEGIBLE
S11 1:45 "The capsule falls." — none — TASK ONLY
S12 1:55 "She wakes up disoriented and completely drained." — posture, head, tempo — LEGIBLE

THE CHOICE ON THE BODY (anchor beats inferred — mode V)
CHOICE (S7 · 01:05) Before: frozen and catatonic amid smoke. After: calmly checking her watch to assess the situation.
COST   (S10 · 01:35) Before: leaning back in quiet acceptance. After: completely slumped and unconscious.
FINAL  (S12 · 01:55) Before: unconscious in the chair. After: slowly raising her head, drained but alive.

GAZE STRING
```
OBSERVED:   OO-OODDUOD-D
PLAN UP / DOWN: none (mode V)
```

| # | Category | Score | Issue |
|:--:|---|:---:|---|
| 1 | Face & Eyes | 9/10 | highly expressive, minimal frozen micro-expressions (S2, S5, S8) |
| 2 | Hands as Intent | 7/10 | hands mostly passive; S3 (00:25) borders on frozen rather than intentionally still |
| 3 | Posture & Weight of Decision | 8/10 | weight shifts well communicated during the slumps (S8, S10, S12) |
| 4 | Gaze Direction | 9/10 | gaze tracks with the inferred object of attention (watch, window) |
| 5 | Tempo & Stillness | 6/10 | pattern ① MANNEQUIN. S6 (00:55) and S9 (01:25) too static, feel like paused clips |
| 6 | The Central Choice on the Body | 8/10 | S7 (01:05) looking at the watch reads clearly as a decision |
| 7 | Cost & Aftermath | 10/10 | S8 (01:15) and S10 (01:35) physicalize the toll of the red-light event |
| 8 | Final Beat Legibility | 9/10 | S12 (01:55) awakening reads as survival and extreme fatigue |
| 9 | Proportion | 8/10 | subtle acting fits the claustrophobic setting, slightly under-animated in wides |

SEVERITY TALLY: 🔴 0 · 🟠 1 · 🟡 1
THE THREE THAT MATTER
00:55 (S6) — MANNEQUIN — "the body is entirely static while smoke billows; needs
   slight chest breathing or micro-adjustments to read as alive." 🟠
01:25 (S9) — MANNEQUIN — "the figure from behind is completely frozen; requires
   slight head drift or shoulder movement." 🟡
00:25 (S3) — STIFF INTENT — "hand on the armrest lacks muscle tension or
   micro-twitches; reads as a prop rather than a waiting hand." 🟡

FIXABLE vs REGENERATION: "the mannequin stillness in S6 and S9 requires
regeneration to introduce subtle human breathing and weight shifting; currently
they read as still images with moving VFX overlays."
FLAGS: "Did the plan call for the character to pass out in S10 and wake up in
S12, or is this an AI interpretation of a 'landing' sequence?"
OUT-OF-SCOPE FLAGS: the red lighting in S6-S9 appears suddenly without a clear
on-screen trigger — LIGHT lens. Floating objects in S4 lack interaction with the
cabin environment boundaries — PHYSICS lens.

---

## ⑪ IŞIK  ⭐ depoda ilk koşu

```
INPUT MODE: V · FILM: faz 9.mp4 · RUNTIME: 02:00 measured
FRAME RATE ASSUMED: 24 fps · GRID GIVEN: none (mode V)
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: none
NON-SCENE MATERIAL: none · PRESENCE STRING: 1111111111-1
LINES HEARD: none — nothing audible to me
ZONES REGISTERED: 5 · MEDIUM: air (cabin allows smoke/haze)
LIGHT JUMPS: 5 · CLEAN CUTS: 6

SCORED CATEGORIES: 7 · SUM 49.0 · 49.0 ÷ 7 = 7.0
OVERALL SCORE: 7.0/10
VERDICT: ZONE BROKEN
```

LIGHT LEDGER
| S | zone | key (clock·elev) | quality | shadow | temp | practicals | exposure | bg black | in-clip |
| S1 | Z1 | E · eye | soft | lifted | neutral | 1/1 | mid | dark | 0 |
| S2 | Z2 | 9 · eye | hard | deep | warm | 1/1 | mid | dark | 0 |
| S3 | Z2 | 9 · eye | soft | lifted | warm | 0/0 | mid | dark | 0 |
| S4 | Z2 | 9 · eye | hard | deep | warm | 1/1 | mid | dark | 0 |
| S5 | Z3 | T · top | soft | deep | neutral | 0/0 | bright | dark | 0 |
| S6 | Z4 | 9 · eye | soft | deep | red | 1/1 | mid | dark | 0 |
| S7 | Z4 | 9 · eye | soft | deep | red | 1/1 | mid | dark | 0 |
| S8 | Z4 | 9 · eye | soft | deep | red | 0/0 | mid | dark | 0 |
| S9 | Z4 | W · eye | soft | deep | red | 1/1 | mid | dark | 0 |
| S10 | Z5 | 9 · eye | soft | lifted | cool | 1/1 | mid | mid | 0 |
| S11 | Z6 | T · high | hard | deep | neutral | N/A | mid | N/A | 0 |
| S12 | Z5 | 9 · eye | soft | lifted | cool | 1/1 | mid | mid | 0 |

KEY DIRECTION STRING
```
OBSERVED:  E999T999W9T9
ZONES:     none (mode V)
```

LIGHT JUMP LOG
| S1 → S2 | Z1→Z2 | neutral daylight shifted instantly to intense amber golden-hour | N/A | 🔴 |
| S2 → S3 | Z2→Z2 | hard shadow quality became soft and lifted | N/A | 🟠 |
| S4 → S5 | Z2→Z3 | amber window key (9) vanished, replaced by neutral top key (T) | N/A | 🔴 |
| S5 → S6 | Z3→Z4 | neutral light instantly replaced by intense emergency red | N/A | 🟡 |
| S9 → S10 | Z4→Z5 | red emergency ambient instantly reverted to pale cyan daylight | N/A | 🔴 |

| # | Category | Score | Issue |
|:--:|---|:---:|---|
| 1 | Key Direction Continuity | 7/10 | S5 (00:45) abandons the established window key for a top/front key |
| 2 | Shadow Quality & Fill | 6/10 | density bounces between deep/hard and lifted/soft (S1, S2, S3) |
| 3 | Colour Temperature | 3/10 | severe and constant drift (Neutral → Amber → Neutral → Red → Cool) at S2, S5, S6, S10 |
| 4 | Practical Sources | 6/10 | the window acts as a practical but radically changes colour and intensity across clips |
| 5 | Exposure at Cuts | 7/10 | subject exposure relatively stable, background black levels lift in S10 and S12 |
| 6 | In-Clip Stability | 10/10 | flawless lockoffs; no dimmers, flicker or drift inside any clip |
| 7 | Zone Boundaries | N/A | no in-scope source (Mode V) |
| 8 | Atmosphere Honesty | 10/10 | smoke in S6 interacts naturally with the red light; no vacuums violated |

SEVERITY TALLY: 🔴 3 · 🟠 1 · 🟡 1
THE THREE THAT MATTER
00:10 (S1→S2) — TEMPERATURE DRIFT — "light shifts instantly from neutral white to intense amber. Grade S2-S4 to match S1, or regenerate if shadows are baked too hard." 🔴
01:30 (S9→S10) — TEMPERATURE DRIFT — "the red emergency light vanishes instantly across the cut without a narrative trigger. Regenerate S10 to carry the red light." 🔴
00:40 (S4→S5) — THE KEY THAT WALKS — "the key moves from the 9 o'clock window to a top/front studio light, abandoning the environment's motivated source. Regenerate S5." 🔴

FLAGS: "Did the plan call for a narrative time-jump between S1 and S2 (hence the
golden hour)? Did the plan explicitly request the red emergency lighting to
cease before S10?"
OUT-OF-SCOPE FLAGS: the character's physical state completely resets at S10
(awake and red to unconscious and pale) — PERFORMANCE / CONTINUITY lens.

---

## ⑫ HOOK  ⭐ depoda ilk koşu

```
INPUT MODE: V · FILM: faz 9.mp4 · RUNTIME: 02:00 measured
FRAME RATE ASSUMED: 24 fps · SCENES OBSERVED: 12 · CUTS COUNTED: 11
CUTS OFF GRID: none · NON-SCENE MATERIAL: none
PRESENCE STRING: 1111111111-1 · LINES HEARD: none — nothing audible to me
FORMAT MEASURED: 16:9
OPENING WINDOW: 0 → 10 s · HOOK QUESTION: NO QUESTION
SHARE MOMENTS: 3 candidates · 2 standing alone

SCORED CATEGORIES: 8 · SUM 47.0 · 47.0 ÷ 8 = 5.8
OVERALL SCORE: 5.8/10
VERDICT: HOOK MISSING
```

HOOK LEDGER
| OPENING | 00:00–00:10 | astronaut looks out window at Earth | **NO QUESTION** | N |
| COVER | 00:52 | astronaut sits catatonic as smoke pours down under red emergency lights | "Something went terribly wrong in space." | Y |
| SHARE 1 | 00:30–00:40 | a pen, strap and cloth float in mid-air inside the cabin | "I'd send this because the zero gravity looks so real." | Y |
| SHARE 2 | 00:50–01:00 | smoke fills the red-lit cabin around the seated astronaut | "I'd send this because the claustrophobia is intense." | Y |
| SHARE 3 | 01:40–01:50 | orange and white parachute lowers a capsule over a barren desert | "I'd send this because it looks like a real landing." | Y |
| EXIT | 01:50–02:00 | astronaut slumped, slowly raising head | "She survived, but what now?" (points forward to nothing, does not loop) | N |

DROP-OFF PREDICTION
```
1. 00:10 · reason: slow open
2. 00:25 · reason: plateau
3. 00:35 · reason: no stakes yet
```

| # | Category | Score | Issue |
|:--:|---|:---:|---|
| 1 | Hook Question | 2/10 | OPENING (00:00): "a 10-second establishing shot asks nothing of the viewer; it is a screensaver, not a hook" |
| 2 | Cover Second | 9/10 | COVER (00:52): reads instantly as an emergency without context or text |
| 3 | Stakes by the First Share Moment | 2/10 | SHARE 1 (00:30): "40 seconds in… nothing is at risk" |
| 4 | Share Moments Stand Alone | 8/10 | zero-G clip and parachute landing travel perfectly as standalone clips |
| 5 | Plateau | 4/10 | 00:00–00:40 severe pacing plateau; consecutive slow shots of sitting and staring |
| 6 | Peak Placement | 7/10 | peak (smoke event at 00:50) sits mid-film, leaving a long quiet denouement |
| 7 | Exit & Return | 5/10 | EXIT (01:50): "a definitive narrative end that stops dead. It does not send the stranger back to the beginning" |
| 8 | Format Fit | 10/10 | native 16:9, clean of UI conflicts |

SEVERITY TALLY: 🔴 2 · 🟠 1 · 🟡 0
THE THREE THAT MATTER
00:00 — THE SLOW OPEN — "The first 40 seconds are pure establishing atmosphere.
A stranger on a feed will not wait 50 seconds for the inciting incident.
**Reorder or cut to put the red-light emergency closer to the front.**" 🔴
00:35 — NO STAKES YET — "By the time the floating zero-g shot happens, the
viewer still doesn't know what this film is about." 🔴
01:50 — EXIT WITHOUT RETURN — "the waking up shot resolves the story but kills
the loop." 🟠

FIXABLE vs REGENERATION: "The slow open and the plateau are entirely fixable in
the edit. The first 40 seconds must be radically condensed. **Try opening on S5
(ECU eyes) slamming straight into S6 (red smoke), then use S1 (looking at Earth)
as a flashback or context shot.** The exit is baked in; creating a looping
structure would require a different final scene."
FLAGS: "Did the plan intend for the first 50 seconds to have zero narrative
tension? Is this meant to be a slow-cinema meditation or a viral short?"
OUT-OF-SCOPE FLAGS: the sudden light shift at 00:50 creates a massive visual
jump that is effective for attention, but breaks environmental continuity —
LIGHT lens.
