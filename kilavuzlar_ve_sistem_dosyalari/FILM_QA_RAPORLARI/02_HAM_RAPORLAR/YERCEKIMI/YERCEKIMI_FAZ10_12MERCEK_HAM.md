# 🌍 YERÇEKİMİ — FAZ 10 / ZEMİN · ON İKİ MERCEK HAM RAPORLARI

```
Koşu       07.09.2026 · Gemini · tek oturum · on iki mercek
Malzeme    "faz 10.mp4" · raporların ölçtüğü süre 109–111 s
Faz        S109–S120 · 18:00–20:00 · Perde III · FİLMİN SON FAZI
Mod        ⚠️ V — on ikisinin on ikisi. SPEC yok (D117 borcu), fazın kendi
           rubriği FAZ_10_QA_PROMPT.md YOK → genel _KAYNAK mercekleri koşuldu
           [D185 · F9'dan sonra ikinci kez]

⛔ ⑪ ÖLÇÜM KAPISI KOŞULMADI — sahip kararı (06.09.2026, F9):
   "sen videoya dokunma arkadaş repodan niye dışarı cıkıyon"
   Bütün sayılar RAPOR beyanıdır; ölçüm hakemliği yoktur.

🚨 PARTİ GEÇERSİZ — ①.9 TESLİM KAPISI [D188]
   plan 12 sahne (FAZ_10_ZEMIN.md) · sekiz mercek 11 sahne saydı
   → hiçbir satır T tablolarına girmez · kesme listesi UYGULANMAZ
   ⛔ Kapı HÜKÜM VERMİYOR: (a) eksik teslim mi (b) toplu sayım hatası mı —
      ölçüm gelmeden ayrılmaz. Aritmetik (a) lehine: 12 × 10 s = 120 s,
      oysa on iki raporun on ikisi de 109–111 s ölçtü.

BETİK   python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
        <12 rapor> --film yatay_10_20_dk_filmler/YERCEKIMI/FAZ_10_ZEMIN --rapor
        çıktı: RAPOR_KONTROL/RAPORLAR/FAZ_10_ZEMIN_20260907_RAPOR_KONTROL.md
DERSLER ../../../yatay_10_20_dk_filmler/YERCEKIMI/FAZ_10_ZEMIN/FAZ_10_QA_DERSLER.md
```

## KÜNYE ÇAPRAZ OKUMASI — raporların kendi beyanları

| Mercek | süre | kesme | sahne | şerit | replik | iddia ort | betik ort |
|---|---|---|---|---|---|---|---|
| ① KARE | 110 s | 10 | (11) | `--111111111` | 0 | 7,3 | **6,9** |
| ② DEVAMLILIK | 110 s | 10 | 11 | `--111111111` | 0 | 8,6 | **6,0** |
| ③ SES | 110 s | 10 | — | — | 0 | 9,0 | **8,5** |
| ④ HİKAYE | 111 s | 10 | 11 | `--111111111` | 0 | 6,0 | **6,0** (4 hücre düştü) |
| ⑤ ARKA PLAN | 111 s | 10 | 11 | `--111111111` | — | 6,0 | **6,0** (n=1) |
| ⑥ FİZİK | 111 s | 10 | 11 | `--111111111` | 0 | 10,0 | **—** (sayı taşıyan hücre yok) |
| ⑦ AKSİYON | 109 s | 11 | 12 | `--1111111111` | 0 | 6,3 | **4,0** |
| ⑧ EFOR | 109 s | 11 | 12 | `--1111111111` | 0 | 5,4 | **5,4** |
| ⑨ KADRAJ | 109 s | 10 | 11 | `--111111111` | 0 | 4,5 | **5,3** (kafiye düştü) |
| ⑩ OYUNCULUK | ~110 s | 10 | 11 | `--111111111` | 0 | 5,6 | **5,7** |
| ⑪ IŞIK | 110 s | 10 | 11 | `--111111111` | 0 | 9,2 | **9,2** |
| ⑫ HOOK | 110 s | 10 | 11 | `--111111111` | 0 | 7,5 | **—** 🚨 aritmetik fabrike |

```
⭐ PLANIN ŞERİDİ: `--1111111111` — 12 hane, S109 ve S110 İNSANSIZ.
   Dokuz mercek 11 haneli şerit yazdı. ⑦ ve ⑧ 12 haneli yazdı ama
   ZAMAN KODU BASMADI ve 12 sahneyi 109 saniyeye sığdırdı (12 × 10 = 120).
   Yani çoğunluk MAKARAYI doğru saydı, azınlık PLANI doğru saydı,
   ikisi birden doğru olamaz — ve fark tam bir kliptir.
```

---


# ═══ 01_KARE ═══

```
FORMAT: YATAY
INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS

FILM: (not supplied)
FORMAT: YATAY
ASPECT MEASURED: 16:9
LENGTH CLASS: (not supplied)
SCENE: Compilation
VIDEO DURATION: 110s MEASURED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 10 (0:09, 0:19, 0:29, 0:39, 0:49, 0:59, 1:09, 1:19, 1:29, 1:39)
NON-SCENE MATERIAL: none
LINES HEARD: none — room tone present
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      58.0
DIVISION:           58.0 ÷ 8 = 7.3

OVERALL SCORE: 7.3/10 (6 categories excluded)
VERDICT: REGENERATE

SCORES SUMMARY
Category    Score    Critical Issues
Character    4/10    −4 · 1:20 (F1) · −2 · 1:36 (F2)
Scale & Physics    6/10    −4 · 0:50 (F3)
Camera    10/10    none
Lighting    8/10    −2 · 0:20 (F4)
Environment    7/10    −3 · 1:40 (F5)
Creatures    —    no in-scope source
Particles & Materials    8/10    −2 · 1:12 (F6)
Dialogue & Audio    9/10    −1 · 1:22 (F7)
Frame Anchor Fidelity    —    UNVERIFIABLE
Negative Violations    3 count    BOX 3 · LINKED 3 · UNLINKED 0
Motion Quality    6/10    −4 · 1:42 (F8)
Vertical Format (9:16)    N/A    [YATAY]
Safe Zone    N/A    [YATAY]
Hook Timing    N/A    [YATAY]

SCENE INVENTORY
MATERIAL
What you were given: 11-clip compilation edit · duration 110s
Cuts you can see: 10 (0:09, 0:19, 0:29, 0:39, 0:49, 0:59, 1:09, 1:19, 1:29, 1:39)
Aspect ratio: 16:9

THE CHARACTER
Face / hair / marks: Brunette, facial dirt, forehead laceration. First frame fully visible: 0:20
Suit / wardrobe: Cream/white flight suit with orange arm striping, mechanical watch on left wrist.
Wear / dirt: Dust heavy on knees and forearms.
Equipment: Survival capsule, parachute, analog field watch.

THE WORLD
Gravity read: ~1g (dirt falls rapidly, heavy body weight).
Atmosphere read: Dense (dust hangs in background trails).
Light sources: Single harsh directional key (sunlight), high contrast.
Location: Cracked arid lakebed / desert expanse.

MOTION
Camera: Mostly locked off or slow, stable linear tracking.
Subject: Slow, deliberate post-crash survival movements.

PRESENCE STRING
--111111111

SEVERITY TALLY
🔴 BLOCKER: 1    🟠 MAJOR: 4    🟡 MINOR: 2

TOP 3 CRITICAL ERRORS
1:20 — 🔴 BLOCKER — Character: Extreme contact morphing; thumb phases entirely into the watch crown during winding.
0:50 — 🟠 MAJOR — Scale & Physics: Capsule exterior volume shrinks significantly compared to established interior geometry.
1:40 — 🟠 MAJOR — Environment: Severe spatial jump; capsule hatch and parachute orientation shift completely from the 0:50 master shot.

DETAILED ERROR LOG
1:20 — 🔴 BLOCKER — Character — Thumb phases entirely into the watch crown during winding.
0:50 — 🟠 MAJOR — Scale & Physics — Capsule exterior volume shrinks compared to established interior geometry.
1:36 — 🟠 MAJOR — Character — Suit patches and zipper geometry flicker and alter design upon standing.
1:40 — 🟠 MAJOR — Environment — Spatial jump; capsule hatch and parachute orientation shift completely from the 0:50 master shot.
1:42 — 🟠 MAJOR — Motion Quality — Subject glides/moonwalks, lacking 1g kinematic foot-planting.
0:20 — 🟡 MINOR — Lighting — Soft AI bloom artifacting around the interior hatch window.
1:12 — 🟡 MINOR — Particles & Materials — Falling dirt clumps unnaturally, lacking fine particulate separation.
1:22 — 🟡 MINOR — Dialogue & Audio — Slight sync drift between Foley (winding click) and thumb actuation.

WHAT WORKED WELL
High-frequency details on the cracked lakebed terrain maintain excellent temporal stability.
Skin texture and subsurface scattering during the extreme close-up (0:30) avoid the standard plastic/waxy AI degradation.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "rigid kinematic contact, solid state geometry, distinct mechanical boundaries" → prevents hand-surface fusion during the watch winding sequence.
REMOVE from image prompt: "cinematic soft lighting" → causes AI bloom on the interior capsule window.
REPLACE "walking in desert" with "heavy planted footsteps, weight-bearing stride, 1g gravity mechanics" → prevents the zero-friction glide/moonwalk effect.

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above [4, 7, 9].

OUT-OF-SCOPE FLAGS
none

FLAGS FOR DOCUMENT CHECK
0:50 — capsule exterior scale drops — QUESTION: what are the precise vehicle dimensions?
1:12 — sand physics fall rapidly — QUESTION: was 1g gravity specified?

QUALITY TABLE ROW
| (not supplied) Ⓥ | YATAY | Compilation | 4/10 | 6/10 | 10/10 | 8/10 | 7/10 |  | 8/10 | 9/10 |  | 6/10 |  |  |  | 3 | 7.3/10 |
```


# ═══ 02_DEVAMLILIK ═══

```
FILM: faz 10.mp4
RUNTIME: 110s MEASURED
SCENES OBSERVED: 11 · CUTS COUNTED: 10 · CHARACTERS TRACKED: 1
SETUP INVENTORY: 7 distinct setups · repeat map: A: S0, S1 · B: S2 · C: S3, S7 · D: S4, S6 · E: S5, S10 · F: S8 · G: S9 · distinct angle types used: 5, named — low, eye level, high/overhead, wide profile, extreme close-up
NON-SCENE MATERIAL: none
LINES HEARD: none — room tone present
MATERIAL TYPE: FILM
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  12
SUM OF SCORES:      104.0
DIVISION:           104.0 ÷ 12 = 8.6

OVERALL SCORE: 8.6/10
VERDICT: DRIFTS BUT RECOVERABLE

SCENE INVENTORY
S0    0:00-0:09    Lakebed    None    Capsule drags on parachute    None
S1    0:10-0:19    Lakebed    None    Capsule comes to rest    None
S2    0:20-0:29    Int. Capsule    The Pilot    Opens the interior hatch    None
S3    0:30-0:39    Lakebed    The Pilot    Lying face down, wakes up    None
S4    0:40-0:49    Lakebed    The Pilot    Crawls away from capsule    None
S5    0:50-0:59    Lakebed    The Pilot    Crawling (extreme wide shot)    None
S6    1:00-1:09    Lakebed    The Pilot    Crawls toward camera    None
S7    1:10-1:19    Lakebed    The Pilot    Examines dirt in hands    None
S8    1:20-1:29    Lakebed    The Pilot    Winds mechanical watch    None
S9    1:30-1:39    Lakebed    The Pilot    Stands up    None
S10   1:40-1:49    Lakebed    The Pilot    Walks toward the capsule    None

CHARACTER PASSPORT(S)
Label:            The Pilot
First clear view: S2, 0:20
Face:             Fair skin, defined jaw, light freckling.
Hair:             Brunette, shoulder-length, straight, parted slightly right.
Eyes:             Brown.
Build:            Athletic, average height.
Costume:          Cream flight suit with dual orange arm stripes above the elbow. Silver front zipper.
Equipment:        Mechanical field watch with black dial and heavily weathered leather strap on left wrist.
Wear map:         Heavy dust on knees and forearms. Prominent vertical red scratch/laceration on the left side of the forehead.
Voice:            N/A

EVIDENCE BASE
FACE-VISIBLE:     ~50 s of 110 s total   ·  5 of 11 scenes
COSTUME-VISIBLE:  9 of 11 scenes
MOUTH ON SCREEN:  yes

APPEARANCE TABLE
The Pilot    S2    0:20-0:29    Yes    Clean face, turning hatch wheel
The Pilot    S3    0:30-0:39    Yes    Prominent red scratch on left forehead
The Pilot    S4    0:40-0:49    No    Suit dusty, zipper pulled down slightly
The Pilot    S5    0:50-0:59    No    Extreme wide, unreadable detail
The Pilot    S6    1:00-1:09    Yes    Crawling, zipper down at chest, scratch missing
The Pilot    S7    1:10-1:19    No    Hands only, watch clearly visible
The Pilot    S8    1:20-1:29    No    Close-up of watch
The Pilot    S9    1:30-1:39    No    Standing, zipper now pulled fully up to collar
The Pilot    S10   1:40-1:49    No    Walking away, full body

SCORES SUMMARY
1    Identity — Face, Hair & Build    10/10    none
2    Costume Identity    7/10    -3 · 1:00 (S6) · 1:30 (S9)
3    Wear, Damage & Injury    5/10    -5 · 0:30 (S3) · 1:00 (S6)
4    Equipment & Carried Objects    10/10    none
5    Cross-Cut Action    10/10    none
6    Physical Consistency    10/10    none
7    Counter Logic    N/A    NONE recorded
8    Spatial Geography    7/10    -3 · 0:20 (S2) · 0:50 (S5)
9    Time & Light Logic    10/10    none
10   World State & Props    5/10    -3 · 0:10 (S1) · 0:50 (S5) · -2 · 0:50 (S5) · 1:40 (S10)
11   Causality & Knowledge    10/10    none
12   Quantity & Character Count    10/10    none
13   Setup & Abandonment    10/10    none

PRESENCE STRING
--111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 1

DRIFT MAP
BODY    Forehead scratch vanishes    The Pilot    1:00 (S6)    1:00 (S6)    No
WORLD   Parachute relocates    N/A    0:50 (S5)    1:40 (S10)    No
BODY    Zipper state changes    The Pilot    1:30 (S9)    1:30 (S9)    No

WEAR TIMELINE
Left forehead scratch    The Pilot    S3 (0:30)    S3    S6 (1:00) ⚠️    No
Dust on knees    The Pilot    S4 (0:40)    S4, S6, S9    None    Yes

COUNTER CURVE
NONE

LOCATION MAP
Lakebed / Crash site    All scenes    No    Capsule/parachute arrangement and scale shift

CONTRADICTION LOG
0:30    1:00    BODY    The Pilot    3    Prominent red scratch on left forehead at 0:30 is completely gone at 1:00.    🟠 MAJOR
1:00    1:30    BODY    The Pilot    2    Suit zipper is open at the chest at 1:00, but fully zipped to the collar at 1:30 without action shown.    🟡 MINOR
0:10    0:50    WORLD    N/A    10    Parachute is directly behind the capsule at 0:10, but far to the left in the wide shot at 0:50.    🟠 MAJOR
0:50    1:40    WORLD    N/A    10    Parachute moves again from far left at 0:50 to bundled directly beside the hatch at 1:40.    🟠 MAJOR

OPEN THREADS
Examining dirt    S7 (1:10)    No    Establishes location texture
Winding watch    S8 (1:20)    No    Thematically establishes survival/time

THE THREE THAT MATTER
The vanishing forehead injury: sharp red laceration at 0:30, entirely missing at 1:00. Fix: Regenerate S6 or cut S3.
The teleporting parachute: crash-site footprint rearranges across S1, S5, S10. Fix: Regenerate S10 to match S5.
The zipper state change: minor continuity error between S6 and S9. Fix: Accept it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Vanishing scratch (S6)    Cut S3 entirely or regenerate S6    Moderate
Parachute layout (S1, S5, S10)    Regenerate S10 to match S5    High
Zipper change (S6 to S9)    Accept    None

FLAGS FOR DOCUMENT CHECK
The capsule interior feels much larger than the exterior at 0:50.    What are the exact dimensions of the capsule?
The pilot winds an analog watch at 1:20.    Was this specific timepiece mandated by the character bible?

OUT-OF-SCOPE FLAGS
1:20 — Extreme morphing/fusion of thumb into watch crown → FRAME lens
1:40 — Character glides/moonwalks instead of planting feet → FRAME lens
```


# ═══ 03_SES ═══

```
FILM: faz 10.mp4
RUNTIME: 110s MEASURED
AUDIO STATE: B — no dialogue present
SPOKEN LINES: 0 · CUTS COUNTED: 10
NON-SCENE MATERIAL: none
LINES HEARD: none — room tone present
DISTINCT VOICES: 0 · REGISTERS: 0 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  3
SUM OF SCORES:      27.0
DIVISION:           27.0 ÷ 3 = 9.0

OVERALL SCORE: 9.0/10
VERDICT: SOUNDTRACK HOLDS

AUDIO LEDGER
DIALOGUE LEDGER
N/A — no dialogue present

VOICE PASSPORT
N/A — no voices present

AMBIENCE MAP
S0-S1 (Lakebed)    0:00-0:19    Desert wind, dry air, blowing dust    Mid    Consistent
S2 (Int. Capsule)  0:20-0:29    Muffled wind, metallic resonance    Low    Level drops appropriately for interior
S3-S10 (Lakebed)   0:30-1:49    Desert wind, crunching footsteps, fabric rustle    Mid    Consistent

LAYER COUNT
0:40    Wind, heavy fabric rustle, dirt crunch    3    N/A
1:22    Wind, mechanical watch winding clicks    2    N/A

MUSIC LEDGER
N/A — no music present

SCORES SUMMARY
Speaker Attribution    N/A    [STATE B]
Synthetic Voice Tells    N/A    [STATE B]
Voice Identity Continuity    N/A    [STATE B]
Delivery vs Performance    N/A    [STATE B]
Turn-Taking & Acoustics    N/A    [STATE B]
Ambience Continuity    9/10    -1 · 0:20 (F1)
SFX Causality & Sync    8/10    -2 · 1:22 (F2)
Mix Hierarchy & Levels    10/10    none
Music & Silence    N/A    [No music]

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 2

ATTRIBUTION MAP
N/A — no voices present

VOICE DRIFT COMPARISON
N/A — no voices present

SYNTHETIC TELL LOG
N/A — no voices present

AMBIENCE HOLE LOG
None — no absolute silence observed.

CONTRADICTION LOG
0:19    0:20    Ambience    6    Exterior wind transitions to interior volume, but lacks the expected enclosed acoustic signature of the capsule.    🟡 MINOR
1:22    1:23    SFX    7    Foley winding clicks drift out of sync with the visible thumb actuation on the watch crown.    🟡 MINOR

THE THREE THAT MATTER
Sync drift on watch winding at 1:22. Fix: Re-cut/nudge Foley clips.
Interior acoustic transition at 0:20. Fix: Add EQ/reverb filtering to the interior bed.
(None)

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Foley sync drift (1:22)    Nudge/re-align Foley clips    Low
Interior ambience profile (0:20)    Re-level / add EQ filter    Low

FLAGS FOR DOCUMENT CHECK
The interior ambience drops in volume at 0:20 but retains exterior characteristics.    Does the plan specify a completely sealed acoustic environment for the capsule interior?

OUT-OF-SCOPE FLAGS
none
```


# ═══ 04_HIKAYE ═══

```
INPUT MODE: V
BASELINE: THE FILM AS SCREENED
MATERIAL TYPE: FILM (undeclared)
FILM: (not supplied)
FORMAT: YATAY
LENGTH CLASS: (not supplied)
RUNTIME: 111 s (measured)
SCENE COUNT: 11 (counted, not from a document)
CUTS COUNTED: 10 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40)
NON-SCENE MATERIAL: none
LINES HEARD: none — nothing audible to me
SPEC BLOCK PROVIDED: no — mode V

— MODE V ONLY —
ENDS OR STOPS: ends — she walks away toward the horizon, completing the sequence of recovery and choosing to move forward.
PEAK LOCATED AT: 1:20 S9 — the quiet, deliberate winding of the watch grounds her survival before she stands.

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      54.0
DIVISION:           54.0 ÷ 9 = 6.0

N/A LEDGER: 1 of 10 categories scored N/A
categories: Dialogue
OVERALL was computed over 9 categories.

OVERALL STORY SCORE: 6.0/10
VERDICT: SHOOT WITH TRIMS

THE FILM IN ONE SENTENCE
"An astronaut survives a hard landing in a barren desert and slowly gathers the physical and mental strength to stand up and walk into the unknown."

SCORES SUMMARY
Hook    8/10    -2 · 0:10 (S2) static wide holds too long and kills the momentum of the crash
Premise & Clarity    8/10    -2 · 0:40 (S5) the rule of the world is just "empty desert," limiting stakes
Structure & Pacing    5/10    -5 · 0:40 (S5) · 0:50 (S6) redundant beats of lying on the ground stall the narrative
Character    6/10    -4 · 0:30 (S4) character is reduced to pure physical survival with little interiority shown
Theme    7/10    -3 · 1:30 (S10) straightforward resilience without a specific cost or sacrifice
Dialogue    —    no in-scope source (silent film)
Emotional Arc    5/10    -5 · 0:30-1:00 (S4-S6) flat intensity during the prolonged physical recovery phase
Ending    7/10    -3 · 1:40 (S11) standard walk-away trope without recontextualizing the beginning
Originality    4/10    -6 · 0:00 (S1) highly swappable desert crash premise seen in numerous sci-fi properties
Retention Risk    4/10    -6 · 0:40-1:00 (S5-S6) long stretch with no new visual information or escalation

THE THREE THINGS THAT MOST HURT THIS FILM
0:40-1:00 (S5-S6) — Redundant recovery shots — kills the pacing and risks heavy viewer drop-off.
0:10 (S2) — The static wide shot of the landed capsule — halts the built-in tension instead of escalating it.
Overall — Generic setting — the environment poses no specific, immediate threat other than being barren.

THE THREE THINGS WORTH PROTECTING
0:00 (S1) — The opening shot of the capsule dragging — dynamic hook, clear survival question.
1:20 (S9) — Winding the watch — tactile micro-action that shows character interiority.
1:40 (S11) — The final wide shot — excellent sense of scale and isolation.

THE ONE THING NOTHING ELSE DOES
The specific, intimate detail of a character choosing to wind a mechanical analog watch while wearing a high-tech space suit immediately after a traumatic crash.

SCENE MAP — mode V only
S1    0:00-0:10    Desert    None    Capsule drags across the ground    No    Hook / Setup
S2    0:10-0:20    Desert    None    Capsule rests silently    No    Establish aftermath
S3    0:20-0:30    Interior    Astronaut    Woman opens the hatch    No    Reveal survivor
S4    0:30-0:40    Desert    Astronaut    Close-up of face on ground    No    Establish toll
S5    0:40-0:50    Desert    Astronaut    Woman lies face down, coughing    No    Physical struggle
S6    0:50-1:00    Desert    Astronaut    Wide shot lying by capsule    No    Scale of isolation
S7    1:00-1:10    Desert    Astronaut    Pushes up to hands and knees    No    Escalation of effort
S8    1:10-1:20    Desert    Astronaut    Close-up on trembling hands    No    Micro-struggle
S9    1:20-1:30    Desert    Astronaut    Winds her mechanical watch    No    Thematically ground character
S10   1:30-1:40    Desert    Astronaut    Stands up fully    No    Climax / Turn
S11   1:40-1:51    Desert    Astronaut    Walks away toward horizon    No    Resolution

RUNTIME (measured): 111 s
SCENE COUNT (counted): 11
SPEAKING SCENES: 0
THE FILM'S QUESTION: Did the occupant survive the crash, and what will they do next?
THE READ: An astronaut survives a rough landing on a barren world, gathers her strength, and sets out into the unknown.

PRESENCE STRING
--111111111

SCENE-BY-SCENE VERDICT
S1    0:00-0:10    Hook / Setup    KEEP    Strong dynamic opening.
S2    0:10-0:20    Establish aftermath    CUT    Stalls momentum; we know it stopped.
S3    0:20-0:30    Reveal survivor    KEEP    Good claustrophobic contrast to desert.
S4    0:30-0:40    Establish toll    KEEP    Establishes her baseline state.
S5    0:40-0:50    Physical struggle    CUT    Redundant with S4 and S6.
S6    0:50-1:00    Scale of isolation    TIGHTEN    Trim to 5s.
S7    1:00-1:10    Escalation of effort    KEEP    Necessary physical transition.
S8    1:10-1:20    Micro-struggle    KEEP    Good textural detail.
S9    1:20-1:30    Thematically ground character    KEEP    Best character beat in the film.
S10   1:30-1:40    Climax / Turn    KEEP    The payoff of the physical effort.
S11   1:40-1:51    Resolution    KEEP    Earned ending.

RANKED CUT LIST (to lose 30 seconds)
resulting runtime: 91s — BELOW FORMAT FLOOR (assuming 120s floor), replace don't remove.
S5 (0:40-0:50) — 10s saved — lost: repetitive shot of her lying down.
S2 (0:10-0:20) — 10s saved — lost: static shot of the capsule.

RETENTION DROP-OFF FORECAST
0:40 — Viewers leave here because the action completely stops for 30 seconds of slow recovery shots (S4-S6). Fix: condense the recovery sequence.

SHAREABLE MOMENT
0:00-0:05 — The high-speed impact and dragging of the capsule across the desert floor.

REWRITE PRESCRIPTIONS
SCENE S5: replace the shot of her lying down with a POV shot of a distant anomaly on the horizon → fixes the lack of a specific destination.
SCENE S2: cut this scene entirely → fixes the immediate pacing stall right after the energetic hook.

OUT-OF-SCOPE FLAGS
none

FLAGS FOR DOCUMENT CHECK — mode V only
QUESTION: is the lack of audio track intentional? — because I heard absolutely nothing, not even room tone or wind.
QUESTION: what is the intended format length? — because the film measures 111s.

STORY TRACKING ROW
| (not supplied) Ⓥ | YATAY | (not supplied) | 8 | 8 | 5 | 6 | 7 | N/A | 5 | 7 | 4 | 4 | 6.0/10 |
```


# ═══ 05_ARKAPLAN ═══

```
FILM: (not supplied)
RUNTIME: 01:51 measured
SCENES OBSERVED: 11 · CUTS COUNTED: 10
NON-SCENE MATERIAL: none
SUBJECTS EXCLUDED:
S1: Capsule dragging parachute
S2: Resting capsule and parachute
S3: Astronaut opening hatch
S4: Astronaut's face on the ground
S5: Astronaut lying on ground
S6: Astronaut on the ground
S7: Astronaut pushing up
S8: Astronaut's hands
S9: Hands winding watch
S10: Astronaut standing up
S11: Astronaut walking away

BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  1
SUM OF SCORES:      6.0
DIVISION:           6.0 ÷ 1 = 6.0

OVERALL SCORE: 6.0/10
VERDICT: FIELD HOLDS

BACKGROUND INVENTORY
SCENE 1 [0:00–0:10]
MIDGROUND: Cracked desert earth (playa), large dust cloud.
FAR FIELD: Flat horizon line, lower third. Distant haze.
SKY/CEILING: Clear blue sky, thin cirrus clouds.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 2 [0:10–0:20]
MIDGROUND: Cracked desert earth.
FAR FIELD: Flat horizon, middle third. Empty.
SKY/CEILING: Clear blue sky.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 3 [0:20–0:30]
MIDGROUND: Capsule interior, padded walls, metal latch.
FAR FIELD: Blown-out white/blue glare outside the window.
SKY/CEILING: Padded capsule interior ceiling.
FOCUS: Subject sharp, midground walls slightly soft.
EDGES: Clean.

SCENE 4 [0:30–0:40]
MIDGROUND: Cracked earth immediately around her face.
FAR FIELD: None — ground fills frame.
FOCUS: Shallow focus, background blur.
EDGES: Clean.

SCENE 5 [0:40–0:50]
FAR FIELD: Capsule (left/center) and parachute (left). Flat horizon, upper third.
SKY/CEILING: Pale blue sky.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 6 [0:50–1:00]
FAR FIELD: Capsule (right) and parachute (left). Flat horizon line, top edge.
SKY/CEILING: Sliver of blue sky at the top.
FOCUS: Deep focus.
EDGES: Clean.

SCENE 7 [1:00–1:10]
FAR FIELD: Capsule (left) and parachute (far left). Flat horizon.
SKY/CEILING: Blue sky, thin wisps.
FOCUS: Subject sharp, far field soft.
EDGES: Clean.

SCENE 8 [1:10–1:20]
MIDGROUND: Cracked earth. FAR FIELD: None. FOCUS: Shallow focus. EDGES: Clean.

SCENE 9 [1:20–1:30]
MIDGROUND: Blurred cracked earth. FAR FIELD: None. FOCUS: Shallow focus. EDGES: Clean.

SCENE 10 [1:30–1:40]
FAR FIELD: Capsule (right). Flat horizon. SKY: Clear blue sky. FOCUS: Subject sharp, far field soft. EDGES: Clean.

SCENE 11 [1:40–1:51]
FAR FIELD: Parachute (left), capsule (right). Flat horizon, upper third.
SKY/CEILING: Blue sky with cirrus clouds. FOCUS: Deep focus. EDGES: Clean.

SCORES SUMMARY
1    Background Figure Integrity    N/A    declared absence - no background figures
2    Background Figure Behaviour    N/A    declared absence - no background figures
3    Crowd Count & Density    N/A    declared absence - no crowds
4    Horizon & Topology    —    no in-scope source
5    Depth, Parallax & Scale    —    no in-scope source
6    Background Set & Props    6/10    -4 · 0:10 vs 0:50 (capsule hatch orientation jumps, parachute cords vanish)
7    Focus Honesty    —    no in-scope source
8    Sky & Atmospherics    —    no in-scope source
9    Frame Edges & Emergent Artifacts    —    no in-scope source

PRESENCE STRING
--111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 2

FIELD DRIFT MAP
None    No within-shot drift observed    -    -    -

COUNT LOG
None    No countable groups in field    -    -    -

CONTRADICTION LOG
0:10    0:50    Far field    Set/Props    Capsule hatch faces right in S2, left in S6, and front in S7    🟡 MINOR
0:10    0:50    Far field    Set/Props    Parachute tether lines are visible in S2, entirely absent in S6 and S11    🟡 MINOR

THE THREE THAT MATTER
Capsule orientation jumping — the untouched capsule's scorched hatch rotates to face a different direction in nearly every wide shot. Fix: Accept it.
Missing parachute cords — the parachute loses its tether lines entirely after the crash scene. Fix: Accept it.
None — The field holds exceptionally well. Ground textures do not boil, and the horizon line remains perfectly flat and stable.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Capsule rotation    Accept it    Zero
Missing parachute lines    Accept it    Zero

FLAGS FOR DOCUMENT CHECK
The film contains no background figures or crowds in any scene.    Is this meant to be an absolutely unpopulated/desolate location by design?

OUT-OF-SCOPE FLAGS
The astronaut's suit dirt patterns reset and shift heavily between 1:00 (S7) and 1:30 (S10) — CONTINUITY LENS.
```


# ═══ 06_FIZIK ═══

```
INPUT MODE: V
FILM: (not supplied)
RUNTIME: 01:51 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 11 · CUTS COUNTED: 10
NON-SCENE MATERIAL: none
LINES HEARD: none — nothing audible to me
GRAVITY: GRAVITY ESTIMATE 1g (9.8 m/s²) ± 10%, L4, L6
PREMISE REGISTER: none

ARITHMETIC GATE
SCORED CATEGORIES:  7
SUM OF SCORES:      70.0
DIVISION:           70.0 ÷ 7 = 10.0

OVERALL SCORE: 10.0/10
VERDICT: PHYSICS HOLDS

PHYSICS LEDGER
L1    0:00-0:10    Capsule dragging    10.0 s    ~30 m (est. ≈10 capsule lengths)    ~3 m/s velocity    1g / Earth atmosphere drag
L2    0:32-0:36    Sand blown by breath    ~0.5 s    ~10 cm (est. face scale)    Rapid settle    1g gravity
L3    1:00-1:05    Push up from ground    5.0 s    ~0.4 m rise (torso length)    Slow exertion    1g biomechanics
L4    1:11-1:14    Sand falls from hand    ~0.2 s    ~5 cm (hand scale)    9.8 m/s²    1g gravity
L5    1:30-1:35    Astronaut stands up    5.0 s    ~1.6 m rise    Heavy load transfer    1g biomechanics
L6    1:32-1:34    Dirt falls from knees    ~0.3 s    ~0.5 m (knee to ground)    ~9.8 m/s²    1g gravity
L7    1:40-1:51    Walking away    11.0 s    ~15 strides    ~1.4 steps/s    1g walk cycle

NUMERIC LOCK VERIFICATION — MODE D ONLY
Not applicable in Mode V.

SCORES SUMMARY
1    Gravity & Free Fall    10/10    no deductions
2    Ballistics & Trajectories    N/A    declared absence - no thrown or launched objects
3    Impact & Momentum    N/A    declared absence - no direct collisions or impacts shown
4    Material Behaviour    10/10    no deductions
5    Particles & Atmosphere    10/10    no deductions
6    Scale & Measurement    10/10    no deductions
7    Rates & Timing    10/10    no deductions
8    Light & Shadow Physics    10/10    no deductions
9    Human Biomechanics    10/10    no deductions

PRESENCE STRING
--111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 0

GRAVITY TABLE
L4    1:11    ~0.05 m (hand to ground)    ~0.1 s    ~10 m/s²    Matches 1g
L6    1:32    ~0.5 m (knee to ground)    ~0.3 s    ~11 m/s²    Matches 1g (within tolerance)

RATE TABLE
Walk cadence    1:41 (stride 1)    1:45 (stride 6)    Holds constant (~1.4 steps/s)

CONTRADICTION LOG
None    -    -    No arithmetic contradictions found    -

THE THREE THAT MATTER
Flawless Gravity Match — the time for dirt to fall off the suit (L6) correlates to sand falling from the hand (L4). Fix: Accept.
Biomechanics of Exhaustion — centre of mass shifts correctly during the 5-second rise (L5). Fix: Accept.
Shadow Logic Consistency — the sun remains fixed low left across all wide shots. Fix: Accept.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
None    All measured physics hold to 1g standards    Zero

FLAGS FOR DOCUMENT CHECK
A completely soundless vacuum environment is implied by the audio, yet dust billows and a parachute inflates (L1).    Does the plan establish a thin atmosphere, or was the audio stripped in export?

OUT-OF-SCOPE FLAGS
The capsule hatch rotates its orientation across cuts, and the parachute cords vanish completely after the first shot — CONTINUITY LENS.
```


# ═══ 07_AKSIYON ═══

```
MEDIA: video played
INPUT MODE: V
FILM: (not supplied)
RUNTIME: 01:49 MEASURED
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 12 · CUTS COUNTED: 11
NON-SCENE MATERIAL: none
PRESENCE STRING: --1111111111
LINES HEARD: none — nothing audible to me
BEATS COUNTED: 4
BEATS READABLE: 3 readable · 0 partial · 1 unreadable

PREMISE REGISTER:
· gravity / medium [Earth-normal gravity, desert surface]
· what the actor can do [crawl, push up, manipulate small objects]
· what resists them [gravity, physical exhaustion, mechanical locks]
· established screen rules [none specific]

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      57.0
DIVISION:           57.0 ÷ 9 = 6.3

OVERALL SCORE: 6.3/10
VERDICT: ACTION NEVER RENDERED

ACTION BEAT LEDGER
B1 | 00:00–00:09 | Capsule | drag to a stop | ground friction | yes | capsule stops | Y | "The capsule is dragged across the desert by its parachute until it comes to a rest."
B2 | 00:20–00:29 | Woman | turn hatch wheel | mechanical resistance | yes | wheel turns | Y | "The woman turns the locking wheel on the capsule's hatch."
B3 | 01:00–01:09 | Woman | push up from crawl | gravity | yes | fails and drops back to crawl | Y | "The woman pushes up onto her knees but drops back down to a crawl."
B4 | 01:30–01:39 | Woman | stand up | gravity | yes | she is standing | N | "She gets into a crouch, and then a cut jumps to her already standing upright."

PRESENCE STRING
--1111111111

BEAT STRING
A-A---A--xx-

SCORES SUMMARY
1    Beat Anatomy    3/10    -4 · B4 (01:36)
2    Spatial Geography Under Motion    7/10    no in-scope source
3    Threat Vector & Approach    7/10    no in-scope source
4    Contact Legibility    7/10    no in-scope source
5    Consequence Visibility    7/10    no in-scope source
6    Camera's Contract with the Action    5/10    -2 · B4 (01:36)
7    Agency & Intent    7/10    no in-scope source
8    The Stakes Object    7/10    no in-scope source
9    Physical Tempo & Escalation    7/10    no in-scope source

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 0   🟡 MINOR: 0

UNREADABLE MOMENTS TABLE
01:36    The physical action of rising from a crouch to a standing position is skipped.    ④    🔴

CONTRADICTION LOG
none

THE THREE THAT MATTER
01:36 - The core action of standing up is elided by a cut. Fix: Render the continuous motion of rising.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Requires Regeneration: Beat B4 (01:36) — the cut elides the beat; the missing action must be generated.

FLAGS FOR DOCUMENT CHECK
Is the transition between 00:29 (inside capsule) and 00:30 (outside) an intended ellipsis, or is the action of exiting the capsule missing?

OUT-OF-SCOPE FLAGS
CONTINUITY: Parachute placement changes drastically between wide shots and close-ups.
```


# ═══ 08_EFOR ═══

```
INPUT MODE: V
FILM: (not supplied)
RUNTIME: 01:49 MEASURED
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 12 · CUTS COUNTED: 11
NON-SCENE MATERIAL: none
PRESENCE STRING: --1111111111
LINES HEARD: none — nothing audible to me
EXERTION EVENTS: 5
EVENTS WITH NO STRAIN SHOWN: 2
BODY: human
PREMISE REGISTER:
· gravity / medium [Earth-normal gravity on solid ground]
· what the body wears [heavy flight suit, no helmet or gloves]
· declared limits [severe physical exhaustion/crash survivor, visible head wound]

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      43.0
DIVISION:           43.0 ÷ 8 = 5.4

OVERALL SCORE: 5.4/10
VERDICT: WEIGHTLESS WORK

EFFORT LEDGER
E1 | 00:20–00:29 | Turn hatch wheel | mechanical resistance | ~9s | arms · torso | none (cuts away) | 4 | "Her arms engage to turn the wheel, but the cut arrives before any bodily aftermath is shown."
E2 | 00:40–00:49 | Crawling across ground | body weight | ~9s | arms · torso · legs | collapse / pause | 8 | "She collapses onto the ground, unable to keep moving upright, breathing heavily."
E3 | 01:00–01:09 | Pushing to hands and knees | body weight | ~9s | arms · torso · head | head hangs heavily | 7 | "Her head drops and shoulders slump, showing she lacks the energy to rise further."
E4 | 01:20–01:29 | Winding/touching watch (fine motor) | negligible | ~9s | hands | none | 7 | "Nothing; she performs delicate fine motor work immediately after severe gross exertion with no visible tremor."
E5 | 01:40–01:49 | Walking away | body weight | ~9s | none | none | 2 | "Nothing; she walks away with a steady, upright, symmetric gait, completely discarding the severe exhaustion."

PRESENCE STRING
--1111111111

COST CURVE
004888777622

RESET LOG
S10 and S11    6 to 2    No    No    UNEARNED

EFFORT LOCK VERIFICATION — MODE D ONLY
(Mode V - N/A)

SCORES SUMMARY
1    Strain During the Work    7/10    -3 · E5 (01:40)
2    Breath & Recovery    8/10    -2 · E5 (01:40)
3    Fatigue Accumulation    4/10    -6 · E5 (01:40)
4    Load in the Body    5/10    -5 · E5 (01:40)
5    Injury Persistence & Cost    5/10    -5 · E2 (00:40), E5 (01:40)
6    Grip & the Price of Holding On    5/10    -5 · E4 (01:20)
7    Equipment Burden    N/A    no in-scope source
8    Pain, Restraint and Proportion    6/10    -4 · E5 (01:40)
9    Recovery Curve Honesty    3/10    -7 · Reset S10-S11 (01:36)

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 1   🟡 MINOR: 0

UNPAID WORK TABLE
01:20    Winding watch    Tremor, fumble, or hesitation    ⑬    🟠
01:40    Walking away    Stumbling, asymmetric gait, or laboured posture    ⑪    🔴

CONTRADICTION LOG
00:40 (crawling in total exhaustion) vs 01:40 (walking with a steady, symmetric, completely unburdened gait). Scored the unearned reset at 01:40.

THE THREE THAT MATTER
01:40 - The character walks with an unearned symmetric, fresh gait after extreme exhaustion. Fix: stumbling, slumping, or favouring a side.
01:36 - The jump from struggling to stand to a perfectly rested upright posture. Fix: show the physical toll of rising.
01:20 - Fine motor control flawless right after exhausting gross motor work. Fix: add hand tremor.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Fixable in Edit: the unearned reset between 01:36 and 01:40 could be mitigated by a shot of her resting at length against the capsule.
Requires Regeneration: the flawless fine motor control at 01:20 and the perfectly steady walking gait at 01:40.

FLAGS FOR DOCUMENT CHECK
Was the character intended to fully recover her strength before walking away?

OUT-OF-SCOPE FLAGS
ACTION: The physical motion of standing up is completely elided by a cut at 01:36 (Pattern ④).
```


# ═══ 09_KADRAJ ═══

```
INPUT MODE: V
FILM: (not supplied)
RUNTIME: 01:49 MEASURED
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 11 · CUTS COUNTED: 10 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: --111111111
LINES HEARD: none — nothing audible to me
SETUPS REGISTERED: 11
LOCKOFF HELD: 0 / 11 clips

ARITHMETIC GATE
SCORED CATEGORIES:  4
SUM OF SCORES:      18.0
DIVISION:           18.0 ÷ 4 = 4.5

OVERALL SCORE: 4.5/10
VERDICT: RHYME BROKEN

SETUP LEDGER
S1 | 00:00 | - | WS / eye / wide / tracking capsule | A | - | ground/capsule | pan right starts 00:00
S2 | 00:10 | - | WS / eye / wide / stationary capsule | B | - | capsule | slow push starts 00:10
S3 | 00:20 | - | MS / eye / normal / inside capsule | C | - | hatch | handheld drift starts 00:20
S4 | 00:30 | - | CU / ground / normal / front | D | - | face | subtle drift starts 00:30
S5 | 00:40 | - | WS / ground / wide / front-left | E | - | capsule (screen left) | slow push starts 00:40
S6 | 00:50 | - | EWS / high / wide / top-down | F | - | capsule | very slow push starts 00:50
S7 | 01:00 | - | MS / ground / normal / side | G | - | capsule (screen right) | slow drift starts 01:00
S8 | 01:10 | - | CU / high / normal / top-down | H | - | hands | micro drift starts 01:10
S9 | 01:20 | - | ECU / high / macro / top-down | I | - | watch | slow push starts 01:20
S10 | 01:30 | - | MFS / ground / normal / front | J | - | capsule (screen right) | tilt/drift starts 01:30
S11 | 01:40 | - | WS / eye / normal / behind | K | - | capsule (screen right) | tracking forward starts 01:40

SETUP STRING
OBSERVED:   ABCDEFGHIJK
PLAN:       none (mode V)
DIFFERS AT: none (mode V)

PRESENCE STRING
--111111111

RHYME PAIR
setup letter / size / angle / anchor position / the one variable    A / WS / eye / dragging capsule / tracking movement    K / WS / eye / walking figure / forward tracking    No
PAIR FAILS — The film opens on an empty tracking shot of a dragging object and closes on a follow shot of a walking human; the setups do not match.

LOCKOFF VERIFICATION
S2    none (mode V)    Creeping dolly (Pattern ③)    00:10    FAIL
S5    none (mode V)    Creeping dolly (Pattern ③)    00:40    FAIL
S6    none (mode V)    Creeping dolly (Pattern ③)    00:50    FAIL
S9    none (mode V)    Creeping dolly (Pattern ③)    01:20    FAIL

SCORES SUMMARY
1    Setup Fidelity    N/A    no in-scope source
2    Lockoff Integrity    4/10    -6 · S2 (0:10), S5 (0:40), S6 (0:50), S9 (1:20)
3    Rhyme Pair    2/10    -8 · First and last frames fail to rhyme
4    Return Consistency    N/A    no in-scope source
5    Cluster Seams    N/A    no in-scope source
6    Angle Arc & Deliberate Shocks    8/10    -2 · S10 (1:30) jump cut in scale reads as accidental shock
7    Screen Geometry    4/10    -6 · S5 (0:40), S7 (1:00), S10 (1:30) anchor object (capsule) jumps from screen-left to screen-right

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 1   🟡 MINOR: 0

THE THREE THAT MATTER
00:00 vs 01:40 — The opening and closing frames do not rhyme. Fix: Regenerate either the opening or closing shot.
00:40 & 01:00 & 01:30 — The anchor object (the capsule) teleports across the frame's geography. Fix: Regenerate setups.
00:10 & 00:40 & 00:50 — Unmotivated AI creeping dolly (Pattern ③). Fix: Stabilize in post or regenerate.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
The creeping dolly motions in S2, S5, S6 can be stabilized at the cost of resolution loss. The spatial geometry jump requires regeneration.

FLAGS FOR DOCUMENT CHECK
Was the constant creeping push-in on the exterior wide shots intended as a stylistic choice, or is it an artifact of the model refusing a locked-off prompt?
Is the lack of a returning setup deliberate? Every cut introduces a completely new camera position.

OUT-OF-SCOPE FLAGS
ACTION: The cut at 01:36 skips the physical action of standing up entirely (Lens 7 - Action Ellipsis).
EFFORT: The flawless watch winding (01:20) immediately follows extreme physical exhaustion without any visible tremor (Lens 8).
```


# ═══ 10_OYUNCULUK ═══

```
INPUT MODE: V
FILM: (not supplied)
RUNTIME: ~01:50 ESTIMATED
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 11 · CUTS COUNTED: 10 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: --111111111
LINES HEARD: none — nothing audible to me
CHANNEL REGISTER: face visible, eyes readable, hands bare, posture available, head/gaze available, tempo available, breath visible, proximity available
ANCHOR BEATS: CHOICE N/A · COST N/A · FINAL N/A (mode V)
SCENES TASK ONLY: 2

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      51.0
DIVISION:           51.0 ÷ 9 = 5.6

OVERALL SCORE: 5.6/10
VERDICT: MOSTLY LEGIBLE

PERFORMANCE LEDGER
S1 | 00:00 | Capsule lands. | N/A | N/A | TASK ONLY
S2 | 00:10 | Capsule rests. | N/A | N/A | TASK ONLY
S3 | 00:20 | She wants to escape the capsule. | posture, hands | N/A | LEGIBLE
S4 | 00:30 | She is physically exhausted. | face, breath | N/A | LEGIBLE
S5 | 00:40 | She wants to assess her status. | hands, gaze | N/A | LEGIBLE
S6 | 00:50 | She lies immobilized by the crash. | posture | N/A | PARTIAL
S7 | 01:00 | She wants to rise despite weakness. | posture, tempo | N/A | LEGIBLE
S8 | 01:10 | She seeks to ground herself in reality. | hands, tempo | N/A | LEGIBLE
S9 | 01:20 | She decides to restart her routine. | hands, gaze | N/A | LEGIBLE
S10 | 01:30 | She commits to standing up. | posture, weight | N/A | LEGIBLE
S11 | 01:40 | She decides to walk forward and survive. | posture, tempo | N/A | LEGIBLE

THE CHOICE ON THE BODY
CHOICE  (S10 · 01:30)  Before: Kneeling in defeat.   After: Standing upright in resolve.
COST    (S7 · 01:00)  Before: Prone and still.   After: Straining on hands and knees.
FINAL   (S11 · 01:40)  Before: Static assessment.   After: Deliberate forward movement.

GAZE STRING
OBSERVED: --OODDOODOO
PLAN UP / DOWN: N/A

PRESENCE STRING
--111111111

SCORES SUMMARY
1    Face & Eyes    6/10    Subtle changes read well (S4 00:30).
2    Hands as Intent    6/10    Winding watch shows clear intent (S9 01:20).
3    Posture & Weight of Decision    6/10    Weight shift from kneeling to standing (S10 01:30).
4    Gaze Direction    5/10    Looks follow action mostly (S5 00:40).
5    Tempo & Stillness    5/10    Sluggish pacing reflects exhaustion (S7 01:00).
6    The Central Choice on the Body    6/10    Clear physical shift to standing (S10 01:30).
7    Cost & Aftermath    6/10    Exhaustion carried into ground scenes (S4 00:30, S7 01:00).
8    Final Beat Legibility    6/10    Walking away reads as survival choice (S11 01:40).
9    Proportion    5/10    Quiet gestures match the barren setting.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 0

THE THREE THAT MATTER
00:50 - Wide shot lacks human agency. Fix: Push in closer to show breath or micro-movement.
01:00 - Struggle to knees feels slightly uniform in speed. Fix: Add a pause before the final push.
00:20 - Hatch turning is highly mechanical. Fix: Show body weight behind the turning effort.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Mostly fixable by trimming the static wide shots to prioritize the close-up intentional gestures.

FLAGS FOR DOCUMENT CHECK
N/A (Mode V)

OUT-OF-SCOPE FLAGS
ACTION: Sand physical interaction feels floaty (S8).
EFFORT: Stand up sequence lacks visible strain (S10).
```


# ═══ 11_ISIK ═══

```
INPUT MODE: V
FILM: faz 10.mp4
RUNTIME: 01:50 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 11 · CUTS COUNTED: 10 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: --111111111
LINES HEARD: none — nothing audible to me
ZONES REGISTERED: 2 · MEDIUM: air
LIGHT JUMPS: 0 · CLEAN CUTS: 10

ARITHMETIC GATE
SCORED CATEGORIES:  7
SUM OF SCORES:      65.0
DIVISION:           65.0 ÷ 7 = 9.2

OVERALL SCORE: 9.2/10
VERDICT: LIGHT HOLDS

LIGHT LEDGER
S1 | 00:05 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S2 | 00:15 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S3 | 00:25 | Zone 2 (Interior) | 3 · mid | soft | lifted | neutral | 1/1 | mid | dark | 0
S4 | 00:35 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S5 | 00:45 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S6 | 00:55 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S7 | 01:05 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S8 | 01:15 | Zone 1 (Exterior) | 0 · low | hard | dark | warm | 1/1 | mid | dark | 0
S9 | 01:25 | Zone 1 (Exterior) | 0 · low | hard | dark | warm | 1/1 | mid | dark | 0
S10 | 01:35 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0
S11 | 01:45 | Zone 1 (Exterior) | 9 · low | hard | dark | warm | 1/1 | mid | dark | 0

KEY DIRECTION STRING
OBSERVED:  99399990099
ZONES:     N/A (mode V)

PRESENCE STRING
--111111111

LIGHT JUMP LOG
no jumps

SCORES SUMMARY
1    Key Direction Continuity    9/10    Excellent consistency; minor shift to 10 o'clock in CU shots (S8 01:15, S9 01:25) is natural.
2    Shadow Quality & Fill    10/10    Hard shadows perfectly match the unfiltered desert sun across all exterior clips.
3    Colour Temperature    9/10    Golden hour warmth holds exceptionally well across all exterior clips without saturation drift.
4    Practical Sources    10/10    The sun is the single source and remains established.
5    Exposure at Cuts    9/10    Subject exposure remains stable when returning from interior to exterior (S3 to S4).
6    In-Clip Stability    9/10    No unmotivated dimming, flickering, or pulsing; S1 (00:05) dust occlusion is physically accurate.
7    Zone Boundaries    N/A    (mode V)
8    Atmosphere Honesty    9/10    Air medium is respected; volumetric dust kicks up correctly with hard light scattering.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 0

THE THREE THAT MATTER
This film exhibits exceptionally rare light consistency for AI generation. No major fixes required.

FIXABLE IN THE GRADE vs REQUIRES REGENERATION
Nothing requires regeneration for light continuity.

FLAGS FOR DOCUMENT CHECK
None. (mode V)

OUT-OF-SCOPE FLAGS
BACKGROUND: Capsule orientation and position relative to the parachute seems to shift slightly between S2 and S11.
```


# ═══ 12_HOOK ═══

```
INPUT MODE: V
FILM: faz 10.mp4
RUNTIME: 01:50 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 11 · CUTS COUNTED: 10 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: none
PRESENCE STRING: --111111111
LINES HEARD: none — nothing audible to me
FORMAT MEASURED: 16:9
OPENING WINDOW: 0 → 10 s · HOOK QUESTION: "Did someone just crash-land on a dead planet?"
SHARE MOMENTS: 0 declared · 3 standing alone

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      60.0
DIVISION:           60.0 ÷ 8 = 7.5

OVERALL SCORE: 7.5/10
VERDICT: LEAVES AT 00:50

HOOK LEDGER
OPENING | 00:00–00:10 | Capsule dragging in the desert dust | "Did someone just crash-land on a dead planet?" | Y
COVER SECOND | 00:32–00:32 | Woman's bruised face resting in the cracked earth | "This looks like a high-budget sci-fi survival movie." | Y
SHARE MOMENT 1 | 00:30–00:39 | Exhausted face on the ground, breathing heavily | "I'd send this because the makeup and exhaustion feel incredibly real." | Y
SHARE MOMENT 2 | 01:10–01:19 | Hands sifting the dry desert sand | "I'd send this because it's a beautiful, tactile shot of realizing you survived." | Y
SHARE MOMENT 3 | 01:40–01:49 | Walking away from the wrecked capsule into the vast desert | "I'd send this because the framing of her leaving the wreck is cinematic." | Y
EXIT | 01:40–01:50 | Figure walking away into the distance | "She's choosing to walk out and survive." (Points forward to a journey) | Y

INTERSTITIAL CHECK
Candidate 1    00:30–00:39    "...the makeup and exhaustion feel incredibly real."    Y    N
Candidate 2    01:10–01:19    "...it's a beautiful, tactile shot of realizing you survived."    Y    N
Candidate 3    01:40–01:49    "...the framing of her leaving the wreck is cinematic."    Y    N

DROP-OFF PREDICTION
00:50  · reason: plateau
00:15  · reason: slow open
01:05  · reason: plateau

PRESENCE STRING
--111111111

SCORES SUMMARY
1    Hook Question    7/10    S1 (00:00) sets a mood, but takes 20 seconds to show the human at risk.
2    Cover Second    9/10    S4 (00:32) reads immediately as survival/crash without context.
3    Stakes by the First Share Moment    9/10    By S4 (00:30), the harsh environment and physical toll make the stakes obvious.
4    Share Moments Stand Alone    9/10    Visuals are striking enough to exist without prior scenes.
5    Plateau    3/10    S4, S5, S6, and S7 (00:30–01:09) trap the eye in a repetitive loop of lying on the ground.
6    Peak Placement    7/10    S10 (01:30) standing up feels like the peak, placed reasonably well near the end.
7    Exit & Return    8/10    S11 (01:40) points forward clearly, though it does not loop back to the first frame.
8    Format Fit    10/10    16:9, clean frame, no burned-in text.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 1

THE THREE THAT MATTER
00:50 - Severe plateau where the character remains prone across too many consecutive shots. Fix: Cut S5 or S6.
00:10 - The opening spends 20 seconds on establishing shots. Fix: Condense S1 and S2.
01:05 - The struggle sequence lingers too long. Fix: Trim S7.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
The plateau (00:50) and slow open (00:10) are fixable in the edit.

FLAGS FOR DOCUMENT CHECK
N/A (Mode V)

OUT-OF-SCOPE FLAGS
PERFORMANCE: The character's face remains remarkably stoic and unblinking during the close-up at 00:30.
```
