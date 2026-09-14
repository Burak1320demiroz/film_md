# THE PAYLOAD — ③ SES QA · HAM RAPOR

> Model çıktısı, OLDUĞU GİBİ (kural ④). Düzeltilmez, kısaltılmaz.
> Koşu: 01.09.2026 · Gemini · rubrik `3_SES_QA_CRITIQUE_PROMPT.md` · MOD V (bu rubrik zaten yalnız video)
> ⛔ SPEC VAR → ÖN KOŞU [D129]. Değerlendirme: `01_FILM_RAPORLARI/THE_PAYLOAD.md`

---

FILM: THE LAST CUSTODIAN
RUNTIME: 04:06 measured
AUDIO STATE: A · SPOKEN LINES: 4 · CUTS COUNTED: 23
NON-SCENE MATERIAL: 4:00-4:06 Title card
LINES HEARD: 4
1:11 "I'm stepping down to the pad now."
1:15 "Setting the first case down on the regolith."
1:18 "Turning back for the next one."
2:51 "Control, this is..."
DISTINCT VOICES: 1 · REGISTERS: 1 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      67.0
DIVISION:           67.0 ÷ 8 = 8.4

OVERALL SCORE: 8.4/10
VERDICT: SOUNDTRACK HOLDS

AUDIO LEDGER
1a. DIALOGUE LEDGER
1 1:11-1:13 "I'm stepping down to the pad now." Custodian · mouth visible yes · moving yes · COMMS · HUMAN
2 1:15-1:17 "Setting the first case down on the regolith." Custodian · yes · yes · COMMS · HUMAN
3 1:18-1:19 "Turning back for the next one." Custodian · yes · yes · COMMS · HUMAN
4 2:51-2:53 "Control, this is..." Custodian · no (back of head) · no · COMMS · HUMAN

1b. VOICE PASSPORT
Label: Custodian · First heard: 1:11 · Register: HUMAN
Pitch & range: Mid-low, narrow range (calm, professional)
Age & gender coding: Adult male, 40s-50s
Accent / diction: American, clear, deliberate
Processing: Helmet/comms filter (radio EQ, slightly band-limited)
Breath: Very little audible breath (masked by comms filter/music)
Attributed to: The lone astronaut on screen

1c. AMBIENCE MAP
Mars Surface 0:00-1:00, 1:10-1:50 · Wind, sand impact, low rumble · Mid-High · Hard cut at 1:00 and 1:50
Ship Interior 1:00-1:10, 1:50-2:00, 2:10+ · Low drone, air circulation · Low · Masked heavily by music
Space Exterior 2:00, 2:40, 3:00+ · Low rumble, engine wash · Low · Relies on music

1d. LAYER COUNT
0:05 Music, Wind, Foley (wiping) · 3 · N/A
1:15 Music, Wind, Foley (case/footsteps), Dialogue · 4 · Yes, intelligible
2:05 Music, SFX (Rocket Roar) · 2 · N/A
2:51 Music, Interior Drone, Dialogue · 3 · Barely intelligible

1e. MUSIC LEDGER
Cinematic Score · 0:00-4:06 · enters S0 (start) · exits End card · under dialogue yes · ducked barely

SCORES SUMMARY
Speaker Attribution 10/10 -
Synthetic Voice Tells 8/10 −2 · 1:15 (S7)
Voice Identity Continuity 10/10 -
Delivery vs Performance 8/10 −2 · 1:15 (S7)
Turn-Taking & Acoustics N/A only one voice speaks
Ambience Continuity 7/10 −3 · 1:00 (S6) · 1:50 (S11)
SFX Causality & Sync 7/10 −2 · 0:04 (S0) · −1 · 1:11 (S7)
Mix Hierarchy & Levels 9/10 −1 · 2:51 (S17)
Music & Silence 8/10 −2 · 0:00 (S0)

SEVERITY TALLY
🔴 BLOCKER: 0 🟠 MAJOR: 1 🟡 MINOR: 6

ATTRIBUTION MAP
1 1:11 Custodian RESOLVED None · 2 1:15 RESOLVED None · 3 1:18 RESOLVED None · 4 2:51 INFERRED None

VOICE DRIFT COMPARISON
Custodian · first 1:11 · last 2:51 · same voice yes · Processing/EQ slightly muddier on last line, identity holds.

SYNTHETIC TELL LOG
1:15 Custodian HUMAN Timing: completely metrical phrasing, lacking human hesitation or micro-pauses. 🟡 MINOR

AMBIENCE HOLE LOG
1:00 → 1:10 Mars Surface → Interior · No, floor uncertain · 🟡 MINOR
1:50 → 2:00 Mars Surface → Interior · No, floor uncertain · 🟡 MINOR

CONTRADICTION LOG
1:10 / 1:15 Voice/Foley 4 Character lifts/hauls heavy cases visually, but voice sounds entirely rested and seated. 🟠 MAJOR
0:59 / 1:00 Ambience 6 Wind storm howling exterior; interior POV shot immediately loses all wind transmission through the hull. 🟡 MINOR
1:49 / 1:50 Ambience 6 Hard cut on the wind bed jumping from exterior to interior. 🟡 MINOR
0:00 / 0:04 SFX 7 Visual shows wiping a glass/solar panel; audio is generic white-noise hiss/sand that does not match glass friction. 🟡 MINOR
1:11 / 1:15 SFX 7 Footsteps on metal ramp and setting case on ground lack corresponding physical weight/thud. 🟡 MINOR

THE THREE THAT MATTER
1. Performance/Effort Mismatch (1:15): the actor sounds like he is sitting in a sound booth while hauling heavy cargo. Fix: replace the line with a take that includes physical strain/breath.
2. Ambience Hard Cuts (1:00, 1:50): the wind vanishes the millisecond the shot cuts to interior. Fix: carry a muffled low-pass version of the storm into the interior shots.
3. Wall-to-Wall Music (0:00-4:06): the music never stops, breathes, or ducks; it robs the climax/space shots of dynamic range. Fix: cut or dip the music during the airlock/interior quiet scenes.

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Ambience hard cuts (1:00, 1:50) · Smooth crossfades / add LPF wind · Low
SFX lack weight/sync (0:04, 1:11) · Replace foley samples in mix · Low
Line buried under music (2:51) · Automate volume / duck music · Low
Wall-to-wall music masking · Re-spot music cues / create stems · Medium
Lack of vocal exertion (1:15) · Re-record/regenerate dialogue lines · Medium

FLAGS FOR DOCUMENT CHECK
Music plays continuously from start to finish without any silences → Was the intention for this film to be driven entirely by score, or should there be moments of diegetic isolation?

OUT-OF-SCOPE FLAGS
Footstep SFX timing drifts away from the visual contact of the boots on the ramp at 1:11 → the FRAME lens
Sound of the rocket engine propagates loudly in the vacuum of space at 2:00, 3:20 → the FRAME lens
