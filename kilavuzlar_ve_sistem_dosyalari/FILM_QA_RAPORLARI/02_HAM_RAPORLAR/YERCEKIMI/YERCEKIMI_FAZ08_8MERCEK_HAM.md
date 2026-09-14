# YERÇEKİMİ — FAZ 8 / AYRILIS · SEKİZ MERCEK HAM RAPORU

```
Koşu     06.09.2026 · Gemini · makara "faz 8 .mp4" · ~99-100 s · 10 segment
Rubrik   ⛔ FAZ_08_QA_PROMPT.md KOŞULMADI. Onun yerine _KAYNAK/ altındaki
         genel 8 mercek (⑤ arka plan · ⑥ fizik · ① kare · ② devamlılık ·
         ③ ses · ④ hikaye · ⑦ aksiyon · ⑧ efor) ÇIPLAK koşuldu.
Mod      ⚠️ V — SPEC yok · çıplak rubrik [D129] → T tablolarına GİREMEZ

🔴 KONTAMİNASYON UYARISI [DERS 110] — bu dosyanın en önemli satırı:
   Sekiz mercek AYNI SOHBETTE arka arkaya koşuldu. Kanıt dosyanın
   içinde duruyor:
     · ⑥ FİZİK (erken) : "LINES HEARD: none — nothing audible to me"
     · ① KARE (sonra)  : "LINES HEARD: 3" + üç cümle + zaman kodları
     · ②③④⑦⑧ (sonra) : AYNI üç cümleyi AYNI zaman kodlarıyla tekrar
     · ②③④⑦⑧        : AYNI sahne haritası, AYNI presence string
   ⛔ Bu SEKİZ ÖLÇÜM DEĞİL, bir ölçüm ve yedi kopyadır. Özellikle
     "üç replik duyuldu" iddiası ŞÜPHELİDİR ve ffprobe + kulakla
     doğrulanmadan ders yazılamaz.
```

Aşağısı raporların BİREBİR kendisidir, koşulma sırasıyla.

---
---

# ⑤ ARKA PLAN MERCEĞİ — HAM

BASELINE: SELF-CONSISTENCY — this review measures whether the background field agrees with itself, not whether it matches a set design.

FILM: (not supplied)
RUNTIME: 01:39 measured
SCENES OBSERVED: 10 · CUTS COUNTED: 9
NON-SCENE MATERIAL: none
SUBJECTS EXCLUDED:
S1: Speaker grill and sweeping light.
S2: Hands buckling seatbelt.
S3: Hand pressing square buttons.
S4: Hand touching round window frame.
S5: White space capsule.
S6: Astronaut's face and helmet ring.
S7: Light sweeping across a white interior wall and window.
S8: Hand holding a red recessed handle.
S9: Astronaut shaking in seat, holding handle.
S10: Capsule firing thrusters.

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      42.0
DIVISION:           42.0 ÷ 6 = 7.0

OVERALL SCORE: 7.0/10
VERDICT: FIELD DRIFTS BUT RECOVERABLE

BACKGROUND INVENTORY
SCENE 1 [0:00–0:09] SUBJECT: Speaker grill and sweeping light. MIDGROUND: Wall panel holding the speaker. FAR FIELD: none — empty black. SKY/CEILING: none. FOCUS: Sharp on speaker grill, soft on shadow edges. EDGES: Dark shadow on right edge, stable.
SCENE 2 [0:10–0:19] SUBJECT: Hands buckling seatbelt. MIDGROUND: Astronaut suit and seat buckle. FAR FIELD: Dark cabin interior. Largest object: none — empty black. SKY/CEILING: none. FOCUS: Sharp on hands and buckle, soft background. EDGES: Clean, fading to black.
SCENE 3 [0:20–0:29] SUBJECT: Hand pressing square buttons. MIDGROUND: Control panel surface. FAR FIELD: Soft-focus spacesuit/body. Largest object: torso, right half. SKY/CEILING: none. FOCUS: Sharp on buttons, soft background. EDGES: Clean.
SCENE 4 [0:30–0:39] SUBJECT: Hand touching round window frame. MIDGROUND: White interior wall. FAR FIELD: Starfield. Largest object: Sun glare, upper right quadrant. SKY/CEILING: none. FOCUS: Sharp on hand and window edge. EDGES: Clean.
SCENE 5 [0:40–0:49] SUBJECT: White space capsule. MIDGROUND: Docking module and solar panels. FAR FIELD: Earth horizon and space. Largest object: Earth limb, lower third. SKY/CEILING: Space/stars. FOCUS: Sharp on capsule, Earth is distant but resolved. EDGES: Clean.
SCENE 6 [0:50–0:59] SUBJECT: Astronaut's face and helmet ring. MIDGROUND: Seat headrest. FAR FIELD: Dark cabin interior. Largest object: none — empty black. SKY/CEILING: none. FOCUS: Sharp on face, soft background. EDGES: Clean.
SCENE 7 [1:00–1:09] SUBJECT: Light sweeping across a white interior wall and window. MIDGROUND: Empty passenger seat. FAR FIELD: Starfield visible through window. Largest object: none — empty black with lines. SKY/CEILING: none. FOCUS: Sharp on wall and seat, stars in window are sharp lines. EDGES: Clean.
SCENE 8 [1:10–1:19] SUBJECT: Hand holding a red recessed handle. MIDGROUND: White wall panel, mechanical wheel on left. FAR FIELD: none — empty black. SKY/CEILING: none. FOCUS: Sharp on hand and handle, soft on wheel. EDGES: Mechanical wheel touches left edge.
SCENE 9 [1:20–1:29] SUBJECT: Astronaut shaking in seat, holding handle. MIDGROUND: Empty seat on right, interior walls. FAR FIELD: Back wall of cabin. Largest object: Back wall panel, full width. SKY/CEILING: none. FOCUS: Sharp on astronaut, midground shows motion blur. EDGES: Clean.
SCENE 10 [1:30–1:39] SUBJECT: Capsule firing thrusters. MIDGROUND: Exploding space station debris. FAR FIELD: Earth and sun. Largest object: Earth limb, lower half. SKY/CEILING: Sun and stars. FOCUS: Sharp on capsule and debris. EDGES: Debris exits frame cleanly.

SCORES SUMMARY
1 Background Figure Integrity N/A no in-scope source
2 Background Figure Behaviour N/A no in-scope source
3 Crowd Count & Density N/A no in-scope source
4 Horizon & Topology 7.0/10 -3 · 0:40 vs 1:30 (Earth texture scale shifts) 🟡
5 Depth, Parallax & Scale 7.0/10 -3 · 1:00-1:09 (Window starfield is flat 2D lines) 🟡
6 Background Set & Props 7.0/10 -3 · 1:20-1:29 (Empty seat headrest morphs during shake) 🟡
7 Focus Honesty 7.0/10 -3 · 0:20-0:29 (Soft focus background torso pulses) 🟡
8 Sky & Atmospherics 7.0/10 -3 · 0:30 vs 1:30 (Sun placement shifts vs orbit) 🟡
9 Frame Edges & Emergent Artifacts 7.0/10 -3 · 1:10-1:19 (Wheel on left edge smears) 🟡

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 6

FIELD DRIFT MAP
S3 mid 0:22 0:25 Yes · S7 far 1:02 1:05 No · S8 edge 1:12 1:15 Yes · S9 mid 1:22 1:25 Yes

COUNT LOG
Debris chunks S10 ~15 ~15 Holds

CONTRADICTION LOG
0:40 / 1:30 far 4 Earth surface texture scale shifts 🟡
0:30 / 1:30 sky 8 Sun placement relative to orbit 🟡

THE THREE THAT MATTER
2D Lines in Window (S7): Feels like a flat UI graphic rather than deep space. Fix: Regenerate plate inside window.
Morphing Seat (S9): Right-side seat gelatinizes during the camera shake. Fix: Crop right edge.
Earth Texture Shift (S5 vs S10): Planet surface scale jumps between exterior angles. Fix: Accept it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
S7 2D Window Lines — Regenerate plate — High
S9 Morphing Seat — Crop right edge — Low
S8 Edge smear — Reframe slightly — Low

FLAGS FOR DOCUMENT CHECK
S7 window displays flat geometric lines. — Does S7's window design intend to show graphical data rings instead of a physical starfield?

OUT-OF-SCOPE FLAGS
Audio implies an alarm, but interior lights do not flash -> SOUND/CONTINUITY lens.

---
---

# ⑥ FİZİK MERCEĞİ — HAM

INPUT MODE: V
FILM: faz 8 .mp4
RUNTIME: 01:39 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 10 · CUTS COUNTED: 9
NON-SCENE MATERIAL: none
LINES HEARD: none — nothing audible to me
GRAVITY: 0 m/s² (microgravity) ± 0, based on constant-velocity drift of orbital debris in S5 and S10
PREMISE REGISTER: none

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      77.0
DIVISION:           77.0 ÷ 8 = 9.6

OVERALL SCORE: 9.6/10
VERDICT: MINOR SLIPS

PHYSICS LEDGER
L1 0:00-0:09 Shadow sweeps across speaker grill 9.0s ~10 cm ~1.1 cm/s Light source rotation
L2 0:10-0:19 Astronaut pulls and buckles seatbelt 9.0s ~10 cm Normal human force
L3 0:20-0:29 Finger actuates square button 9.0s ~2 mm Normal compression
L4 0:30-0:39 Hand touches window frame 9.0s 0 cm Static
L5 0:40-0:49 Capsule orbits Earth 9.0s N/A 0 m/s²
L6 0:50-0:59 Astronaut face inside 9.0s 0 cm Static
L7 1:00-1:09 Shadow/light sweeps interior wall 9.0s ~1 m ~11 cm/s
L8 1:10-1:19 Hand pulls and holds red handle 9.0s 0 cm Static tension
L9 1:20-1:29 Severe shaking of astronaut 9.0s ~5 cm ~3-4 Hz
L10 1:30-1:39 Capsule fires continuous thrusters; inert debris drifts 9.0s ~4 m a=0 m/s², v≈0.4m/s Violates Newton's 2nd Law
GRAVITY ESTIMATE: 0 m/s² (microgravity), based on S5 capsule drift and S10 constant-velocity debris. No standard free falls observed.

SCORES SUMMARY
1 Gravity & Free Fall N/A no in-scope source (setting is microgravity)
2 Ballistics & Trajectories 10/10 none
3 Impact & Momentum 7/10 -3 · L10 (1:30) 🟡
4 Material Behaviour 10/10 none
5 Particles & Atmosphere 10/10 none
6 Scale & Measurement 10/10 none
7 Rates & Timing 10/10 none
8 Light & Shadow Physics 10/10 none
9 Human Biomechanics 10/10 none

PRESENCE STRING
-111-1-11-

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 0   🟡 MINOR: 1

THE THREE THAT MATTER
Inertial failure on thrust (S10): The capsule fires its main engines continuously for 9 seconds, but does not accelerate relative to the drifting inert station debris (the distance increases linearly, not quadratically). Fix: Add a slight exponential scale to the debris layer in compositing.

FLAGS FOR DOCUMENT CHECK
No audio track is present. — Does the final delivery require sound, or is this a silent pass?

OUT-OF-SCOPE FLAGS
Starfield in S7 window renders as flat 2D lines instead of points of light -> BACKGROUND lens.

---
---

# ① KARE MERCEĞİ — HAM

FORMAT: YATAY
INPUT MODE: V
BASELINE: SELF-CONSISTENCY + PHYSICS
FILM: (not supplied)
ASPECT MEASURED: 16:9
SCENE: Compilation
VIDEO DURATION: ~100s ESTIMATED
MATERIAL TYPE: FILM (undeclared)
CUTS COUNTED: 9 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30)
NON-SCENE MATERIAL: none
LINES HEARD: 3
0:52 "Trajectory confirmed."
1:24 "Sequence initiated."
1:35 "Trajectory nominal, separation complete."
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      60.0
DIVISION:           60.0 ÷ 8 = 7.5

OVERALL SCORE: 7.5/10
VERDICT: REGENERATE

SCORES SUMMARY
Character 6/10 -3 · 1:15 (hand-surface fusion) · -1 · 0:52 (waxy skin)
Scale & Physics 8/10 -2 · 1:30 (rigid thruster plumes)
Camera 9/10 -1 · 1:26 (synthetic jello shake)
Lighting 8/10 -2 · 0:50 (AI bloom on face)
Environment 8/10 -2 · 1:00 (depth sorting error on star field)
Creatures N/A no in-scope source
Particles & Materials 7/10 -3 · 1:35 (debris lacks momentum)
Dialogue & Audio 7/10 -3 · 1:24 (lip-sync drift)
Frame Anchor Fidelity UNVERIFIABLE no in-scope source
Negative Violations 4 count [x] fusion, skin, bloom, 2D momentum
Motion Quality 7/10 -3 · 1:26 (warping during shake)
Vertical Format (9:16) N/A · Safe Zone N/A · Hook Timing N/A

SCENE INVENTORY
THE CHARACTER: Female subject, brunette short hair, no visible scars. First frame fully visible: 0:50. Suit: White space suit, orange accents, grey harness straps. Wear: Clean, pristine. Equipment: Internal comms assumed; no helmet worn in cabin.
THE WORLD: Gravity read: 1g interior (seated posture holds weight), zero-g exterior. Atmosphere: Breathable interior, vacuum exterior. Light sources: Hard sunlight exterior, soft LED panel lighting interior. Location: Spacecraft cabin and low Earth orbit.
MOTION: Camera: Static lockoffs with slow mechanical push-ins. Subject: Minor hand interactions, steady head turns, intense physical shake during thruster firing.

PRESENCE STRING
-111-1-11-

SEVERITY TALLY
🔴 BLOCKER: 1    🟠 MAJOR: 6    🟡 MINOR: 0

TOP 3 CRITICAL ERRORS
1:15 — 🔴 BLOCKER — thumb fuses entirely with the red lever handle, breaking structural integrity.
1:35 — 🟠 MAJOR — station debris behaves as flat 2D assets, hanging without proper physical momentum or 3D tumble.
1:24 — 🟠 MAJOR — lip sync fails completely on "Sequence initiated", lacking proper phoneme articulation.

DETAILED ERROR LOG
0:50 — 🟠 MAJOR — Lighting — AI bloom/soft glow filter softens the character's face.
0:52 — 🟠 MAJOR — Character — Airbrushed, plastic skin texture appears on the close-up shot.
1:00 — 🟠 MAJOR — Environment — Star field sits in front of the dark side of the planetary rings, breaking depth logic.
1:15 — 🔴 BLOCKER — Character — Thumb geometry breaks down and melts into the surface of the lever.
1:24 — 🟠 MAJOR — Dialogue & Audio — Mouth movement feels disconnected from the jaw and misses phoneme sync.
1:26 — 🟠 MAJOR — Motion Quality — Physical shake induces a synthetic "jello" warping effect across the frame.
1:30 — 🟠 MAJOR — Scale & Physics — Capsule thruster plumes render as rigid solid cones instead of expanding gas.
1:35 — 🟠 MAJOR — Particles & Materials — Debris from the separation sequence hangs motionless without zero-g momentum.

NEGATIVE BOX COUNT: 4 · LINKED FINDINGS: 4 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 4 · TICKED: 4 · MISSED: 0
NO BOX EXISTS FOR: depth sorting error on background, lip-sync failure, motion shake jello effect.

WHAT WORKED WELL
The interior control panel macro shots hold exceptional detail and remain highly stable without swimming textures.
The hard sunlight phase on the exterior capsule shots reads effectively.

PROMPT IMPROVEMENT SUGGESTIONS
ADD to image prompt: "32mm anamorphic lens, sharp optical characteristics, hard sunlight phase" → prevents AI bloom.
REMOVE from image prompt: "cinematic lighting" → causes waxy, airbrushed skin.
REPLACE "zero-g debris" with "high-velocity physical ejecta, strict negative parameters for floating objects" → prevents flat 2D momentum loss.

NEW LESSON CANDIDATE
No new lesson — all errors map to the failure patterns listed above 2, 3, 4, 8.

OUT-OF-SCOPE FLAGS: none
FLAGS FOR DOCUMENT CHECK: none

---
---

# ② DEVAMLILIK MERCEĞİ — HAM

FILM: faz 8 .mp4
RUNTIME: ~1:39 ESTIMATED
SCENES OBSERVED: 10 · CUTS COUNTED: 9 · CHARACTERS TRACKED: 1
SETUP INVENTORY: 10 distinct setups · repeat map: none · distinct angle types used: 3 — CU, MS, Wide
NON-SCENE MATERIAL: none
LINES HEARD: 3
"Trajectory confirmed." at 0:52
"Sequence initiated." at 1:24
"Trajectory nominal, separation complete." at 1:35
MATERIAL TYPE: FILM (undeclared)

ARITHMETIC GATE
SCORED CATEGORIES:  12
SUM OF SCORES:      108.0
DIVISION:           108.0 ÷ 12 = 9.0

OVERALL SCORE: 9.0/10
VERDICT: DRIFTS BUT RECOVERABLE

SCENE INVENTORY
1 0:00-0:10 Interior, wall — speaker shown
2 0:10-0:20 Interior, seat — Pilot (torso) buckles harness
3 0:20-0:30 Interior, panel — Pilot (hand) presses button
4 0:30-0:40 Interior, window — Pilot (hand) touches window
5 0:40-0:50 Space — capsule near station
6 0:50-1:00 Interior, seat — Pilot speaks "Trajectory confirmed."
7 1:00-1:10 Interior, window — window shows rings
8 1:10-1:20 Interior, wall — Pilot (hand) pulls red lever
9 1:20-1:30 Interior, seat — Pilot pulls lever "Sequence initiated."
10 1:30-1:39 Space — capsule departs "Trajectory nominal..."

CHARACTER PASSPORT
Label: The Pilot · First clear view: Scene 2, 0:10
Face: Female, clear skin, no visible marks.
Hair: Brunette, short bob, parted on the right.
Eyes: Dark/brown. Build: Slender.
Costume: White spacesuit with orange trim. Grey harness.
Equipment: No helmet worn. Wear map: Clean and pristine throughout.
Voice: Female, calm, commanding.
FACE-VISIBLE: ~20 s of ~99 s total · 2 of 10 scenes
COSTUME-VISIBLE: 4 of 10 scenes · MOUTH ON SCREEN: yes

SCORES SUMMARY
1 Identity — Face, Hair & Build 10/10 -
2 Costume Identity 6/10 -2 · 0:10 vs 1:20 (harness buckle) · -2 · 0:30 vs 1:10 (wrist cuff)
3 Wear, Damage & Injury 10/10 -
4 Equipment & Carried Objects 10/10 -
5 Cross-Cut Action 8/10 -2 · 1:10 vs 1:20 (lever pull repeats)
6 Physical Consistency 10/10 -
7 Counter Logic — no in-scope source
8 Spatial Geography 6/10 -2 · 0:30 vs 1:00 (window background) · -2 · 1:10 vs 1:20 (lever mounting)
9 Time & Light Logic 10/10 -
10 World State & Props 8/10 -2 · 0:40 vs 1:30 (station module geometry shifts)
11 Causality & Knowledge 10/10 -
12 Quantity & Character Count 10/10 -
13 Setup & Abandonment 10/10 -

PRESENCE STRING
-111-1-11-

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 4   🟡 MINOR: 2

CONTRADICTION LOG
0:30 / 1:10 BODY Pilot 2 Black wrist cuff with indicator is present; later arm is plain white sleeve 🟠
0:10 / 1:20 BODY Pilot 2 Harness has massive central metal buckle; later straps are flat with no central buckle 🟠
1:10 / 1:20 BODY Pilot 5 Hand pulls lever fully down; cut to wide shot where she begins the pull again 🟠
0:30 / 1:00 WORLD 8 Window looks out onto plain stars; later same window reveals massive planetary rings 🟠
1:10 / 1:20 WORLD 8 Lever housed in a recessed wall box; later mounted flat on the interior wall 🟡
0:40 / 1:30 WORLD 10 Station solar arrays and module geometry shift between approach and separation 🟡

OPEN THREADS
Speaker (S1) 0:00 No — Macro shot establishes a speaker that is never used for the dialogue
Button (S3) 0:20 No — Button is pressed but the resulting specific action is unspecified

THE THREE THAT MATTER
Window view changing (0:30 vs 1:00) — Ruins spatial continuity. Fix: Regenerate Scene 4 or 7.
Lever action repeating (1:10 vs 1:20) — Temporal stutter across the cut. Fix: Trim the head of Scene 9.
Wrist cuff vanishing (0:30 vs 1:10) — Visual pop on the arm during key macro interactions. Fix: Regenerate Scene 4 arm.

FLAGS FOR DOCUMENT CHECK
0:40 vs 1:30 station condition — Was the station intended to break apart during separation, or is this structural drift?
0:50 comms voice — Does the pilot speak into a built-in suit comms system, since she wears no headset?

OUT-OF-SCOPE FLAGS
1:15 — thumb geometry breaks down and fuses into the lever handle → FRAME lens
1:24 — lip-sync fails to match phonemes on "Sequence initiated" → SOUND / FRAME lens
1:26 — physical shake creates synthetic "jello" warping across the frame → FRAME lens
1:35 — zero-g debris lacks proper physical momentum and hangs → FRAME lens

---
---

# ③ SES MERCEĞİ — HAM

FILM: faz 8 .mp4
RUNTIME: ~1:39 ESTIMATED
AUDIO STATE: A · SPOKEN LINES: 3 · CUTS COUNTED: 9
LINES HEARD: 3
"Trajectory confirmed." at 0:52
"Sequence initiated." at 1:24
"Trajectory nominal, separation complete." at 1:35
DISTINCT VOICES: 1 · REGISTERS: 1 human / 0 machine / 0 unclear

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      56.0
DIVISION:           56.0 ÷ 8 = 7.0

OVERALL SCORE: 7.0/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX

DIALOGUE LEDGER
1 0:52-0:54 "Trajectory confirmed." The Pilot mouth visible yes moving yes ON-SCREEN HUMAN
2 1:24-1:25 "Sequence initiated." The Pilot mouth visible yes moving yes ON-SCREEN HUMAN
3 1:35-1:38 "Trajectory nominal, separation complete." The Pilot mouth not visible OFF-SCREEN HUMAN

VOICE PASSPORT
Label: The Pilot · First heard: 0:52 · Register: HUMAN
Pitch & range: Mid-low pitch, very narrow movement
Age & gender coding: Adult female
Accent / diction: Standard American, extremely crisp and metered
Processing: Dry, slight small-room reflection
Breath: None audible at any point
Attributed to: The on-screen female pilot

AMBIENCE MAP
Capsule Interior 0:00-0:40 Low hum, air filtration Mid-Low — Drops to digital silence at every cut
Exterior Space 0:40-0:50 Low frequency drone Low — Hard cut at boundaries
Capsule Interior 0:50-1:30 Low hum, air filtration Mid-Low — Drops to digital silence at cuts
Exterior Space 1:30-1:39 Low frequency drone Low

MUSIC LEDGER: NONE

SCORES SUMMARY
Speaker Attribution 10/10 -
Synthetic Voice Tells 6/10 -4 · 0:52 (no breath/flat) · 1:24 (robotic timing)
Voice Identity Continuity 10/10 -
Delivery vs Performance 5/10 -5 · 1:24 (calm vocal effort during extreme physical shake)
Turn-Taking & Acoustics 8/10 -2 · 1:35 (exterior shot has interior room reverb)
Ambience Continuity 4/10 -6 · 0:10, 0:20, 0:30, 0:50, 1:00, 1:10 (bed drops to dead air)
SFX Causality & Sync 6/10 -2 · 0:24 (late button click) · -2 · 1:14 (early lever clunk)
Mix Hierarchy & Levels 7/10 -3 · 1:10 (SFX level jump on cut)
Music & Silence N/A no in-scope source

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 5   🟡 MINOR: 3

AMBIENCE HOLE LOG
0:10 / 0:20 / 0:30 Interior Yes 🟠 · 0:50 / 1:00 / 1:10 Interior Yes 🟡

THE THREE THAT MATTER
Ambience dropping at every cut — the room tone cuts to absolute digital silence at scene boundaries. Fix: Drag the ambient bed across the cuts in the mix.
Delivery mismatch during the action beat (1:24) — the capsule is shaking violently and the pilot sounds seated in a quiet room. Fix: Regenerate/re-record with exertion.
Missing comms filter on the exterior line (1:35). Fix: Apply band-pass EQ.

FLAGS FOR DOCUMENT CHECK
1:35 line (exterior) — Was this intended to be the Pilot over the radio (comms), or a ship computer (MACHINE register)?

OUT-OF-SCOPE FLAGS
1:24 — Lip-sync fails to match the spoken phonemes on "Sequence initiated." → the FRAME lens

---
---

# ④ HİKAYE MERCEĞİ — HAM

FORMAT: YATAY · INPUT MODE: V
BASELINE: THE FILM AS SCREENED
MEASURED RUNTIME: ~99 s (ESTIMATED) · CUTS COUNTED: 9
MATERIAL TYPE: FILM (undeclared)
SCENE COUNT: 10 (counted, not from a document)
LINES HEARD: 3 (as above)
ENDS OR STOPS: ends
PEAK LOCATED AT: 1:20 (Scene 9)

ARITHMETIC GATE
SCORED CATEGORIES:  10
SUM OF SCORES:      35.0
DIVISION:           35.0 ÷ 10 = 3.5

OVERALL STORY SCORE: 3.5/10
VERDICT: REWRITE PREMISE

THE FILM IN ONE SENTENCE
"An astronaut executes a routine, obstacle-free procedural checklist to separate her capsule from a space station."

SCORES SUMMARY
Hook 2/10 · Premise & Clarity 5/10 · Structure & Pacing 4/10 · Character 3/10 ·
Theme 2/10 · Dialogue 4/10 · Emotional Arc 3/10 · Ending 6/10 ·
Originality 3/10 · Retention Risk 3/10

THE THREE THINGS THAT MOST HURT THIS FILM
0:00 — Hook — Opening with 10 seconds of a static speaker grill provides zero curiosity gap.
0:20-0:40 — Procedural Bloat — 20 seconds on buckling a harness and pressing an unexplained button.
1:20 — Empty Characterization — Violent physical shake, no emotional reaction. She acts exactly like a drone.

THE THREE THINGS WORTH PROTECTING
0:30 — Hand on the window — the sole attempt at wonder or interiority.
0:40 — The capsule establishing shot — grounds the geography.
1:20 — The lever pull — the only true punctuation mark.

THE ONE THING NOTHING ELSE DOES
None found.

RANKED CUT LIST (to lose 30 seconds)
resulting runtime: 69s — BELOW FORMAT FLOOR, replace don't remove.
S1 (0:00-0:10) 10s · S7 (1:00-1:10) 10s · S3 (0:20-0:30) 10s

RETENTION DROP-OFF FORECAST
0:08 — static shot of a speaker grill poses no curiosity gap.
0:35 — procedural bloat without context.

SHAREABLE MOMENT: none found

REWRITE PRESCRIPTIONS
SCENE 1: replace [static speaker] with [a blinking warning light or hazard indicator].
SCENE 4: replace [hand resting on the glass] with [pilot looking at a damaged oxygen gauge or personal keepsake].
SCENE 9: move earlier; cut the procedural fat (S1, S3, S7).

---
---

# ⑦ AKSİYON MERCEĞİ — HAM

MEDIA: video played · INPUT MODE: V
FILM: faz 8 .mp4 · RUNTIME: ~1:39 ESTIMATED · FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 10 · CUTS COUNTED: 9
PRESENCE STRING: -111-1-11-
LINES HEARD: 3 (as above)
BEATS COUNTED: 3 · BEATS READABLE: 2 readable · 1 partial · 0 unreadable

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      65.0
DIVISION:           65.0 ÷ 8 = 8.1

OVERALL SCORE: 8.1/10
VERDICT: FIXABLE IN EDIT

ACTION BEAT LEDGER
B1 0:10-0:20 Pilot buckles harness · readable Y
B2 0:20-0:30 Pilot presses button · outcome unreadable · PARTIAL
B3 1:10-1:30 Pilot pulls separation lever · readable Y

SCORES SUMMARY
1 Beat Anatomy 7/10 -3 · B3 (1:10 vs 1:20)
2 Spatial Geography Under Motion 10/10 -
3 Threat Vector & Approach N/A no in-scope source
4 Contact Legibility 10/10 -
5 Consequence Visibility 6/10 -4 · B2 (0:20)
6 Camera's Contract with the Action 8/10 -2 · B3 (1:26)
7 Agency & Intent 9/10 -1 · B2 (0:20)
8 The Stakes Object 10/10 -
9 Physical Tempo & Escalation 5/10 -5 · film-wide

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 3

UNREADABLE MOMENTS TABLE
0:20 — What state changed when the black square button was pressed — ⑪ INTENT INVISIBLE — 🟠
1:20 — Why the lever pull starts over in the wide shot after completing in the CU — ④ ACTION ELLIPSIS — 🟠

THE THREE THAT MATTER
1:10 vs 1:20 — The lever pull repeats across the cut. Fix: Trim the head of the wide shot.
0:20 — The button press has no consequence. Fix: Insert a shot of an indicator reacting.
1:26 — The violent camera shake feels unmotivated compared to the calm vocal delivery.

---
---

# ⑧ EFOR MERCEĞİ — HAM

MEDIA: video played · INPUT MODE: V
FILM: faz 8 _3.mp4 · RUNTIME: ~1:39 ESTIMATED · FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 10 · CUTS COUNTED: 9
PRESENCE STRING: -111-1-11-
EXERTION EVENTS: 2 · EVENTS WITH NO STRAIN SHOWN: 2
BODY: suited human

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      12.0
DIVISION:           12.0 ÷ 6 = 2.0

OVERALL SCORE: 2.0/10
VERDICT: NOBODY PAYS

EFFORT LEDGER
E1 0:10-0:20 buckling heavy harness · strain none · recovery none · debt 0
   "Nothing is different about the body after wrestling the thick straps into the buckle."
E2 1:10-1:30 pulling separation lever under violent shake · strain none · recovery none · debt 0
   "Despite the violent mechanical shake and pulling a heavy lever, the pilot's body remains completely unmarked, unwinded, and unbothered."

COST CURVE: 0000000000

SCORES SUMMARY
1 Strain During the Work 2/10 -8 · E2 (1:20)
2 Breath & Recovery 2/10 -8 · E2 (1:30)
3 Fatigue Accumulation 1/10 -9 · E2 (1:30)
4 Load in the Body N/A
5 Injury Persistence & Cost N/A
6 Grip & the Price of Holding On 3/10 -7 · E2 (1:15)
7 Equipment Burden 3/10 -7 · E1 (0:15), E2 (1:15)
8 Pain, Restraint and Proportion N/A
9 Recovery Curve Honesty 1/10 -9 · E2 (1:30)

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 1   🟡 MINOR: 0

UNPAID WORK TABLE
1:20 Pulling separation lever during violent shake — should show core bracing, shoulder engagement, facial tension — ① EFFORTLESS HEAVY — 🔴
0:15 Manipulating heavy suit buckles — should show forearm engagement, glove resistance — ⑥ THE SUIT THAT ISN'T THERE — 🟠

THE THREE THAT MATTER
1:20 — Lever pull lacks bracing.
1:30 — No breath elevation after the separation sequence.
0:15 — The suit isn't there: bare-hand dexterity in thick pressurized gloves.

OUT-OF-SCOPE FLAGS
1:24 — Voice remains completely calm during the shake → the SOUND lens
1:15 — Thumb geometry melts into the lever → the FRAME lens
1:10 vs 1:20 — Lever pull action repeats across the cut → the ACTION lens
