# 🧪 THE HERD — ÜÇ MERCEK HAM ÇIKTI (03.08.2026)

> ⚠️ **DOKUNULMAZ.** Üç model çıktısı da olduğu gibi, düzenlenmeden
> kaydedildi (AGENTS kural ④). Teşhis ve belge kontrolü cevapları:
> `../01_FILM_RAPORLARI/THE_HERD.md`
>
> **Plan dosyası:** `yatay_2_dk_filmler/THE_HERD/THE_HERD_PLANET_FILM.md`
> — 3.401 satır, 15 sahne, 150 s. **Depoda duruyordu.**
>
> ```
> MERCEK        GİRDİ İDDİASI              GEÇERLİ Mİ
> VIDEO_QA      "prompt file missing"      ❌ GEÇERSİZ — künye boş, yine puanladı
> SENARYO_QA    "plan document not         ❌ GEÇERSİZ — kendi DUR kodunu yazdı,
>                supplied"                    sonra 10 kategori puanladı
> MANTIK_QA     yalnız video (kurala uygun) ✅ GEÇERLİ
> ```
>
> **İkisi de dosyanın yokluğunu VARSAYDI, aramadı.** Ders 54(b)'nin üçüncü
> tekrarı. Bu iki geçersiz çıktı **kanıt olarak** korunuyor — Ders 60 ve 61
> onlardan çıktı.

---

# 1️⃣ VIDEO_QA — ❌ GEÇERSİZ (künye boş, severity üretti)

```
FILM:                The Herd
FORMAT:              Compilation
SCENE:               Compilation
CLIP LENGTH:         153s
PIPELINE:            text-to-video

CHARACTER:           UNVERIFIABLE (Prompt file missing)
SUIT:                UNVERIFIABLE (Blue base, yellow accent visible)
CHARACTER HEIGHT:    UNVERIFIABLE
GRAVITY:             UNVERIFIABLE
ATMOSPHERE:          UNVERIFIABLE (Sound propagates, implying dense atmosphere)
LOCOMOTION MODE:     UNVERIFIABLE (Walking visible)
LENS:                UNVERIFIABLE
CAMERA DISTANCE:     UNVERIFIABLE
CAMERA MOVE:         UNVERIFIABLE
LIGHT SOURCES:       UNVERIFIABLE
FILL LIGHT ALLOWED:  UNVERIFIABLE
VEHICLE/STRUCTURE:   UNVERIFIABLE
DIALOGUE EXPECTED:   none
AUDIO LAYERS:        Atmospheric rumble, engine thrusters, breathing

OVERALL SCORE: 4/10
VERDICT: REGENERATE
SPEC BLOCK PROVIDED: partial — prompt file not provided, fields marked UNVERIFIABLE.

SCORES SUMMARY
Character                4/10   Severe contact morphing on hands.
Scale & Physics          4/10   Inconsistent mass on large creatures.
Camera                   3/10   Multiple cuts violate single-cut rule.
Lighting                 5/10   Heavy AI bloom on emissive elements.
Environment              6/10   Minor texture swimming on ship hull.
Creatures                5/10   Tentacles clip through geometry.
Particles & Materials    3/10   Smoke transitions into solid geometry.
Dialogue & Audio         6/10   Atmospheric layers lack structured progression.
Frame Anchor Fidelity    N/A    Text-to-video pipeline.
Negative Violations      6      Cuts, bloom, morphing, clipping, physics.
Motion Quality           5/10   Jello effect during fast pans.

SEVERITY TALLY
🔴 BLOCKER: 3    🟠 MAJOR: 4    🟡 MINOR: 5

TOP 3 CRITICAL ERRORS
0:07 — 🔴 BLOCKER — Camera cuts from exterior landing directly to interior cockpit.
0:38 — 🔴 BLOCKER — Character's hands severely morph and fuse with the alien
       tentacles upon contact.
1:48 — 🔴 BLOCKER — Particle physics violation: explosion smoke instantly
       solidifies into floating disc creatures.

DETAILED ERROR LOG
0:07 — 🔴 BLOCKER — Camera — Hard cut to interior.
0:38 — 🔴 BLOCKER — Character — Fingers merge into the biological asset.
0:48 — 🟠 MAJOR — Lighting — Heavy AI bloom on the jellyfish creature.
1:10 — 🟡 MINOR — Physics — Dust kick-up feels slightly low-density for a
       massive footfall.
1:19 — 🟠 MAJOR — Particles — Falling discs lack continuous physical momentum;
       they hover uniformly.
1:39 — 🔴 BLOCKER — Character — Extra digits and structural hand collapse while
       holding the glowing cylinder.
1:48 — 🟠 MAJOR — Particles — Smoke exhaust fails to disperse naturally.
2:03 — 🟡 MINOR — Environment — The giant creature's shell textures exhibit
       slight swimming during the flyover.

WHAT WORKED WELL
The ambient sound design anchors the scale effectively without overwhelming the mix.
The color grading remains stable across exterior and interior transitions.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to video prompt: "Continuous single-take tracking shot, zero cuts,
  uninterrupted camera motion." → prevents hidden cuts.
REMOVE from image prompt: "Cinematic lighting, glowing, magical."
  → causes AI bloom and waxy skin.
REPLACE "holding glowing creature" with "hands firmly gripping asset, sharp
  directional lighting, distinct finger geometry." → prevents contact morphing.

NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [1, 3, 5, 24, 31, 33].

QUALITY TABLE ROW
| The Herd | Compilation | 4 | 4 | 3 | 5 | 6 | 5 | 5 | 4/10 |
```

---

# 2️⃣ SENARYO_QA — ❌ GEÇERSİZ (kendi DUR kodunu yazdı ve durmadı)

```
FILM: The Herd
FORMAT: 2-4dk
RUNTIME: 152s
REVIEW INPUT: video only
SPEC BLOCK PROVIDED: no — all fields blank (plan document not supplied)
SPEC VERIFIED AGAINST PLAN DOC: no — abort
  scene count [N/A] · runtime [N/A] · dialogue [N/A] · interstitials [N/A]
  · protagonist [mismatch]

DECLARED EMOTIONAL PEAK: ABSENT — plan document missing
  planned runtime N/A vs actual 152s
  (if ABSENT: Emotional Arc and Structure scores are UNSAFE)

OVERALL STORY SCORE: 4.8/10
VERDICT: REVISE STRUCTURE

THE FILM IN ONE SENTENCE
"An astronaut flies around a desert landscape filled with massive biological
structures that start moving and shedding jellyfish-like creatures."

SCORES SUMMARY
Hook                 6/10   Visually arresting ship landing, but unclear what is at stake.
Premise & Clarity    5/10   The nature of the "herd" and the protagonist's mission remain opaque.
Structure & Pacing   4/10   Repetitive loops of landing, gathering, and watching structures move.
Character            4/10   Acts mostly as a camera-carrier; interiority is minimal.
Theme                5/10   Explores ecological coexistence, but lacks a sharp dramatic cost.
Dialogue             N/A    Completely silent film.
Emotional Arc        4/10   Flat emotional progression without a clear valley before a climax.
Ending               4/10   Stops rather than lands; leaves the viewer hanging.
Originality          6/10   Striking architectural sci-fi imagery, though reminiscent of classic tropes.
Retention Risk       4/10   Mid-section drags significantly during repetitive harvesting beats.

THE THREE THINGS THAT MOST HURT THIS FILM
1. 0:28-0:46 — Repetitive Harvesting Beat — pulling organisms from a compartment
   multiple times without escalating tension.
2. 1:08-1:17 — Redundant Scale Shot — massive foot stepping down mirrors previous
   scale-establishing shots.
3. 2:18-2:27 — Unresolved Exit — the final cockpit check lacks a concluding
   thematic punch, making the film feel unfinished.

THE THREE THINGS WORTH PROTECTING
1. 0:00-0:07 — Opening Landing — strong visual establishment of valley walls and ship.
2. 0:48-0:56 — Jellyfish Interaction — intimate close-up, strong sense of wonder.
3. 1:48-1:57 — Wall Eruption — explosive breach creates a high-impact dynamic shift.

THE ONE THING NOTHING ELSE DOES
The fusion of monumental, architectural biological entities acting as a literal
moving terrain that the protagonist navigates.

SCENE-BY-SCENE VERDICT
S1  0:00-0:07  Establish setting and vehicle landing   KEEP      Strong visual hook.
S2  0:08-0:17  Interior pilot perspective              TIGHTEN   Trim duration.
S3  0:18-0:27  Exterior check on top of ship           KEEP      Good grounding of scale.
S4  0:28-0:47  Organism retrieval from hatch           CUT       Redundant action loop.
S5  0:48-0:57  Floating organism interaction           KEEP      Core sense of wonder.
S6  0:58-1:07  Wide view of moving valley walls        KEEP      Establishes premise.
S7  1:08-1:17  Structural footstep close-up            TIGHTEN   Shorten.
S8  1:18-1:27  Floating discs cascade                  KEEP      Visually striking.
S9  1:28-1:37  Interior corridor reflection            TIGHTEN   Shorten for pacing.
S10 1:38-1:47  Fire tool interaction with creature     KEEP      Introduces proactive choice.
S11 1:48-2:07  Wall rupture and flight escape          KEEP      Primary set-piece climax.
S12 2:08-2:17  Wide convoy movement                    CUT       Adds length, no weight.
S13 2:18-2:27  Final cockpit check and fade out        REWRITE   Needs stronger closing image.

RANKED CUT LIST (to lose 30 seconds)
resulting runtime: 122s — still within format (2-4dk)
1. S4 (0:28-0:47) — 19s — Organism retrieval repetition.
2. S12 (2:08-2:17) — 9s — Wide convoy movement; redundant tracking shot.
3. S2 (0:08-0:17) — 2s — Interior pilot trim.

RETENTION DROP-OFF FORECAST
0:28 — Repetitive harvesting loop with no immediate conflict.
1:08 — Pacing slows as scale shots repeat structural imagery.

SHAREABLE MOMENT
1:48-1:57 — The dramatic vertical rupture and release of disk organisms.

REWRITE PRESCRIPTIONS
1. SCENE S4: replace the prolonged hatch-emptying loop with a single decisive
   extraction that triggers a structural reaction.
2. SCENE S13: replace the standard cockpit check with an exterior matching shot
   of the protagonist looking out at the moving horizon.

STORY TRACKING ROW
| The Herd | 2-4dk | 6/10 | 5/10 | 4/10 | 4/10 | 5/10 | N/A | 4/10 | 4/10 | 6/10 | 4/10 | **4.8/10** |
```

---

# 3️⃣ MANTIK_QA — ✅ GEÇERLİ (doküman istemiyor, kurala uygun çalıştı)

```
FILM: the herd - the valley started walkıng.mp4
RUNTIME: 02:32 · SCENES OBSERVED: 14
BASELINE: SELF-CONSISTENCY
This review answers "does the film agree with itself?"
It does NOT answer "does the film match its design?"

OVERALL SCORE: 4/10
VERDICT: FIXABLE IN EDIT / REGENERATION REQUIRED
A structural reversal is not present, but major state and causality
contradictions require attention.

SCENE INVENTORY
#   In-out        Location            Present      What happens                              Dialogue
1   00:00-00:07   Valley / Giant Feet None         Ship lands/reverses kicking up dust       No
2   00:08-00:17   Ship Interior       Character    Looking out window, sealed helmet         No
3   00:18-00:20   Valley              Character    Walks away from ship; discs in sky        No
4   00:21-00:27   Ship Exterior       Character    Climbs atop ship, kneels at hatch         No
5   00:28-00:47   Ship Hatch          Character    Opens hatch, throws out jellyfish         No
6   00:48-00:57   Ship Exterior       Character    Holds a glowing jellyfish                 No
7   00:58-01:07   Valley Wide         Character    Stands between giant feet                 No
8   01:08-01:17   Ground level        Character    Giant scaly foot steps down nearby        No
9   01:18-01:27   Scaly Wall          Character    Jellyfish float up the wall               No
10  01:28-01:37   Corridor            Character    Holds unlit orange flare                  No
11  01:38-01:47   Scaly Wall          Character    Holds burning flare                       No
12  01:48-01:57   Scaly Wall Wide     None (Ship)  Flare on ground, jellyfish erupt          No
13  01:58-02:17   Aerial / Herd       None (Ship)  Ship flies over giant creatures           No
14  02:18-02:27   Ship Interior       Character    Looks out window                          No

SCORES SUMMARY
Physical Consistency     5/10   Scale of giant feet shifts relative to character.
Counter Logic            N/A    NONE
Spatial Geography        4/10   Ship parking location changes arbitrarily.
Time & Light Logic       5/10   Shadow directions swing between scenes.
State, Costume & Props   3/10   Helmet bubble constantly vanishes and reappears.
Causality & Knowledge    4/10   Jellyfish float in sky before being released.
Quantity Consistency     5/10   Number of jellyfish pulled vs flying.
Setup & Abandonment      6/10   Flare introduced without prior visual setup.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 3

COUNTER CURVE
NONE

LOCATION MAP
Valley / Giant Feet   1, 3, 7, 8   Mostly   Giant toe scale at 01:08 vastly larger than 00:00.
Scaly Wall            9, 11, 12    No       Ship parked centrally at 00:58, flush against wall at 01:48.
Ship Interior         2, 14        Yes      None.

DRIFT MAP
Helmet bubble    00:28   00:28   Yes, at 01:18
Jellyfish release 00:18  00:28   No
Ship location    01:48   01:48   No

CONTRADICTION LOG
00:21 | 00:28 | State     | Helmet bubble present vs missing (no removal shown). | 🟠 MAJOR
00:18 | 00:28 | Causality | Jellyfish floating in sky vs still packed in sealed hatch. | 🟠 MAJOR
01:18 | 01:28 | State     | Helmet bubble present vs helmet bubble missing. | 🟠 MAJOR
00:58 | 01:48 | Spatial   | Ship parked between two toes vs flush against flat wall. | 🟡 MINOR
01:18 | 01:28 | Props     | Empty hands vs orange flare suddenly in right hand. | 🟡 MINOR

OPEN THREADS
Knee wear/tear | 00:08 | No | Distinct rip on left knee not clearly visible later.

THE THREE THAT MATTER
1. Helmet bubble popping in and out (State). Fix: Regenerate scenes 5, 6, 10, 11
   to include the helmet bubble, or cut them.
2. Backward Jellyfish Causality. The sky is already full of discs before she
   climbs up to release them. Fix: Regenerate scene 3 to remove sky discs, or
   move scene 3 after scene 5.
3. Teleporting Ship (Spatial Geography). Fix: Regenerate scene 12 to match the
   original landing geography.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Jellyfish causality      | Reorder 00:18 to follow 00:47    | Cheap (Edit)
Helmet bubble missing    | Regenerate 00:28-00:47, 01:28    | Expensive (Regen)
Ship parking location    | Regenerate 01:48                 | Expensive (Regen)

FLAGS FOR DOCUMENT CHECK
Helmet bubble disappears and reappears. | Is the helmet designed to physically
  retract its glass automatically, or is this a generation error?
Discs in sky vs jellyfish in hatch.     | Are the discs at 00:18 a different
  species/object, or the same ones she releases at 00:28?

OUT-OF-SCOPE FLAGS
Extreme texture swimming and morphing on the alien jellyfish during the hatch
  sequence (00:38). → VIDEO_QA
Lip sync / facial animation static during interior shots. → VIDEO_QA
```
