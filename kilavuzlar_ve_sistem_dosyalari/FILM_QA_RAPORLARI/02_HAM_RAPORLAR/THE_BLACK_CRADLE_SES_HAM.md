# THE BLACK CRADLE — SES_QA HAM RAPOR

> **Tarih:** 17.08.2026 · **Rubrik:** `QA_PROMPTLARI/SES_VE_DIYALOG_QA_CRITIQUE_PROMPT.md`
> **Mod:** rubrik zaten yalnız kurgu · **Malzeme:** 3:52 (232 s) kurgu
> ⛔ Model çıktısı olduğu gibi. Register doğrulaması (kart E3 adım 2) ve belge
> cevapları film kaydında: `../01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`
> ⚠️ Rapor 2 replik / 4 sahne saydı; planın DIALOGUE SCHEDULE'ı 14 replik / 12
> sahne diyor ve raporun MACHINE işaretlediği iki repliğin biri planda HUMAN'dır.

---

```
FILM: (not supplied)
RUNTIME: 03:52 · AUDIO STATE: STATE A — FULL SOUNDTRACK · SPOKEN LINES: 2
DISTINCT VOICES: 2 · REGISTERS: 0 human / 2 machine / 0 unclear
BASELINE: SELF-CONSISTENCY — this review measures whether the soundtrack agrees with itself and with the picture, not whether it matches a script.

OVERALL SCORE: 5.6/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX
The overall soundtrack presents clean machine-register comms dialogue and atmospheric sound design. However, significant physics/realism contradictions occur in hard vacuum space sequences (audible atmospheric engine roars) and noticeable lip-sync delay is present on spoken dialogue.

AUDIO LEDGER
1a. DIALOGUE LEDGER
#    In-out    Transcribed line (verbatim)    Whose voice (your label)    Mouth visible?    Mouth moving?    Source    Intended register
1    0:30–0:33    "Şafak hattı 1200 metrede..."    Female Astronaut (VOICE A)    Yes    Yes    ON-SCREEN    MACHINE
2    1:09–1:12    "Kalkıyoruz. Sıkı tutunun..."    Male Astronaut (VOICE B)    Yes    Yes    ON-SCREEN    MACHINE

1b. VOICE PASSPORT
VOICE PASSPORT — Female Astronaut (VOICE A)
  Label:          Female Astronaut
  First heard:    0:30
  Register:       MACHINE (Filtered radio/helmet comms)
  Pitch & range:  Mid-high, band-limited range
  Age & gender coding: Young adult female
  Accent / diction: Turkish, clear pronunciation
  Processing:     Band-limited comms filter, dry internal helmet resonance
  Breath:         None audible
  Attributed to:  Female astronaut on surface

VOICE PASSPORT — Male Astronaut (VOICE B)
  Label:          Male Astronaut
  First heard:    1:09
  Register:       MACHINE (Filtered radio/helmet comms)
  Pitch & range:  Low-mid, steady cadence
  Age & gender coding: Adult male
  Accent / diction: Turkish, authoritative
  Processing:     Band-limited comms filter
  Breath:         None audible
  Attributed to:  Male pilot in cockpit

1c. AMBIENCE MAP
Scene / location    In-out    Ambient bed (what you hear)    Level    Notes
Planetary Surface    0:00–1:05    Low wind drone, mechanical drill hum    Moderate    Clean bed, consistent across cuts
Cockpit Interior    1:05–1:25    Electronic hum, low thruster rumble    Moderate    Transitions cleanly from exterior
Space / Orbit    1:25–2:50    Heavy engine roar, vacuum rumble    Loud    Unrealistic atmospheric sound in space
Hangar Bay    2:50–3:52    Industrial echo, mechanical movement    Moderate    Smooth room tone transitions

1d. LAYER COUNT
Timecode    Layers audible (name each)    Count    Dialogue intelligible?
0:30    Helmet comms dialogue, surface wind drone, drilling effect    3    Yes
1:09    Pilot comms dialogue, cockpit electronic hum, thruster ignite    3    Yes
1:45    Heavy engine roar, exterior thruster hum, synth music drone    3    N/A (no dialogue)

1e. MUSIC LEDGER
Cue    In-out    Enters on    Exits on    Under dialogue?    Ducked?
Cue 1    0:00–3:52    Opening scene    Fade out    Yes    Yes

SCORES SUMMARY
Category    Score    Critical Issue
Speaker Attribution    8/10    -2 · 0:30 (F1) · Minor visor sync offset
Synthetic Voice Tells    8/10    -2 · 1:09 (F2) · Processing remains static across environments
Voice Identity Continuity    9/10    -1 · 0:30 vs 1:09 · Consistent timbre across characters
Delivery vs Performance    5/10    -5 · 1:09 (F3) · Lip-sync exhibits ~0.4s delay on male pilot line
Turn-Taking & Acoustics    7/10    -3 · 0:30 (F1) · Helmet internal acoustic space lacks variation
Ambience Continuity    8/10    -2 · 1:25 (F4) · Ambient room tone shifts abruptly at space entry
SFX Causality & Sync    4/10    -6 · 1:45 (F5) · Loud atmospheric engine roar in hard vacuum
Mix Hierarchy & Levels    7/10    -3 · 1:45 (F5) · Engine rumble overpowers ambient balance
Music & Silence    8/10    -2 · 3:40 (F6) · Synth bed ends on abrupt fade

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 3

ATTRIBUTION MAP
#    Timecode    Voice    Attributed to    Confidence    Problem
1    0:30    Female Astronaut    Female Astronaut    RESOLVED    Minor visor sync drift
2    1:09    Male Astronaut    Male Pilot    RESOLVED    0.4s lip-sync delay

VOICE DRIFT COMPARISON
Character    First line (tc)    Last line (tc)    Same voice?    What moved
Female Astronaut    0:30    0:30    Yes    Single line spoken; no drift
Male Astronaut    1:09    1:09    Yes    Single line spoken; no drift

SYNTHETIC TELL LOG
Timecode    Voice    Register    Tell observed    Severity
1:09    Male Pilot    MACHINE    Processing lacks dynamic acoustic reflection for cockpit volume    🟡 MINOR

AMBIENCE HOLE LOG
Drops at    Returns at    Location    Absolute silence?    Severity
N/A    N/A    N/A    No absolute silence detected    N/A

CONTRADICTION LOG
Timecode A    Timecode B    Element    Category    What contradicts what    Severity
1:09    1:12    Dialogue Lip-Sync    Delivery vs Performance    Spoken line sound starts ~0.4s after mouth opening visually    🟠 MAJOR
1:45    2:10    Vacuum SFX Physics    SFX Causality    Deep atmospheric thruster roar playing over open vacuum space sequence    🔴 BLOCKER

THE THREE THAT MATTER
Vacuum Sound Physics (1:45): Deep atmospheric thruster roars playing in open space break hard sci-fi immersion.
Fix: Re-level / low-pass filter engine FX to represent internal hull vibrations rather than external airborne roars.

Lip-Sync Lag on Pilot Line (1:09): The spoken sentence "Kalkıyoruz. Sıkı tutunun..." lags behind visible mouth movements by roughly 0.4 seconds.
Fix: Re-cut / nudge audio track back by ~0.4s in timeline edit.

Visor Reflection/Acoustic Staticness (0:30): Dialogue acoustics sound flat inside the helmet without subtle internal wall reflections.
Fix: Re-level / apply short impulse response helmet reverb in mix.

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Finding    Fix    Cost
Lip-sync offset at 1:09    Nudge dialogue clip 0.4s earlier on timeline    Fixable in Mix
Unrealistic vacuum engine roar at 1:45    Mute/filter external roar, boost low hull-rumble frequency    Fixable in Mix
Flat helmet reverb at 0:30    Apply subtle enclosure reverb plug-in    Fixable in Mix
Abrupt music exit at 3:40    Smooth out master music fade-out tail    Fixable in Mix

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Engine audio in vacuum (1:45)    Is the production intended to follow strict hard sci-fi vacuum physics, or stylized cinematic sound design?

OUT-OF-SCOPE FLAGS
[VIDEO_QA] Phoneme-level lip-sync accuracy drift at 1:09 and 0:30.
[VIDEO_QA] Unrealistic particle/dust behavior during surface drill at 0:23.
[KARAKTER_QA] Facial structure variation on male pilot character between 0:17 and 1:08.
```
