# 🔊 THE COLD BURN — SES_QA HAM RAPORU

> Çalıştırma: 09.08.2026 · tek mod, yalnız video (dış model — Gemini)
> Rubrik: `../QA_PROMPTLARI/SES_VE_DIYALOG_QA_CRITIQUE_PROMPT.md`
> ⭐ **RUBRİĞİN İLK KOŞUSU** — yazıldığı gün koşuldu. STEP 0 ses varlık
> kapısı çalıştı (AUDIO STATE: A), register haritası dolduruldu, ledger
> tam. DERS 65 TUTTU (`FILM: (not supplied)`).
> Ölçülen malzeme: 225 s TAM KURGU (D75 gereği tek klip değil ✅).
> ⚠️ EN KRİTİK BELGE BULGUSU: rapor 7 replik saydı, 7'sini de HUMAN /
> ON-SCREEN işaretledi. Plan 12+ replik diyor ve TÜMÜ kapalı kask telsizi
> (insan) + gövdesiz EKO (makine); ağız hiçbir karede kadrajda olmamalı.
> Register haritası (7 insan / 0 makine / ekranda ağızlar) planın ses
> mimarisinin üretimde TERSİNE döndüğünü kanıtladı → DERS 82'nin kaynağı.
> Ortam yatağı bulgusu (1:20-1:40 mutlak sessizlik) → DERS 83'ün kaynağı.
> Belge cevapları: `../01_FILM_RAPORLARI/THE_COLD_BURN.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

FILM: (not supplied)
RUNTIME: 03:45 · AUDIO STATE: A · SPOKEN LINES: 7
DISTINCT VOICES: 2 · REGISTERS: 2 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY — this review measures whether the soundtrack
agrees with itself and with the picture, not whether it matches
a script.

OVERALL SCORE: 5/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX

AUDIO LEDGER
1a. DIALOGUE LEDGER
#    In-out    Transcribed line    Voice    Mouth vis?    Mouth mov?    Source    Register
1    0:12-0:14    "We have the sample."    VOICE A (Woman)    Yes    Yes    ON-SCREEN    HUMAN
2    0:22-0:24    "Storm front approaching."    VOICE B (Man)    Yes    Yes    ON-SCREEN    HUMAN
3    0:28-0:30    "Distance?"    VOICE A (Woman)    No    N/A    OFF-SCREEN    HUMAN
4    0:31-0:34    "Ninety seconds. Closing fast."    VOICE B (Man)    Yes    Yes    ON-SCREEN    HUMAN
5    0:52-0:54    "Engines hot."    VOICE A (Woman)    Yes    Yes    ON-SCREEN    HUMAN
6    0:58-1:01    "Twelve seconds to window."    VOICE B (Man)    Yes    Yes    ON-SCREEN    HUMAN
7    1:52-1:55    "Fire detected in module three."    VOICE A (Woman)    Yes    Yes    ON-SCREEN    HUMAN

1b. VOICE PASSPORT
Label: VOICE A (Woman)
First heard: 0:12
Register: HUMAN
Pitch & range: Mid-high, calm, slightly compressed.
Age & gender coding: Female, 30s-40s.
Accent / diction: Standard American, precise.
Processing: Helmet comms filter (0:12-0:30), Dry (0:52-1:55).
Breath: None audible.
Attributed to: The woman character.

Label: VOICE B (Man)
First heard: 0:22
Register: HUMAN
Pitch & range: Deep, low, gravelly.
Age & gender coding: Male, 50s.
Accent / diction: Standard American.
Processing: Helmet comms filter (0:22-0:34), Dry (0:58-1:01).
Breath: Short inhale before line 4.
Attributed to: The older man character.

1c. AMBIENCE MAP
Scene / location    In-out    Ambient bed    Level    Notes
Ice Planet Ext    0:00-0:50    Howling wind, blowing snow    Loud    Dominates mix; hard cuts at 0:50.
Cockpit    0:50-1:20    Low engine hum, slight vibration    Mid    Bed drops completely at 1:20 cut.
Space    1:20-1:40    Dead silence    None    Total digital silence.
Space / Explosion    1:40-2:20    Bass rumble, debris impact    Loud    Surges instantly; no build-up.
Hub Interior    2:50-3:30    Fire crackle, alarm blare    Very Loud    Dialogue gets buried here.

1d. LAYER COUNT
Timecode    Layers audible    Count    Dialogue intelligible?
0:30    Wind, footstep crunch, dialogue    3    Yes, but wind is masking frequencies.
2:00    Explosion rumble, alarm, debris    3    N/A (no dialogue).
3:00    Fire, alarm, breathing, footsteps, dialogue    5    Barely; fire SFX masks the vocal range.

1e. MUSIC LEDGER
Cue    In-out    Enters on    Exits on    Under dialogue?    Ducked?
1    0:20-1:15    Storm spotted    Jump to space    Yes    No, competing.
2    1:45-3:40    Explosion    Final card    Yes    Poorly.

SCORES SUMMARY
Category    Score    Critical Issue
Speaker Attribution    9/10    All lines clearly attributed to the right bodies.
Synthetic Voice Tells    6/10    Total lack of breath/hesitation in high-stress human dialogue.
Voice Identity Continuity    8/10    Voices hold pitch/timbre; processing shifts without on-screen cause.
Delivery vs Performance    5/10    Line 7 delivered calmly while running from fire.
Turn-Taking & Acoustics    6/10    Comms filter vanishes when entering the ship, despite helmets staying on.
Ambience Continuity    3/10    Bed drops to absolute zero at 1:20; hard cuts everywhere.
SFX Causality & Sync    5/10    Footsteps missing on ice run; explosion sound in vacuum.
Mix Hierarchy & Levels    4/10    Dialogue buried under fire SFX at 3:00; music doesn't duck.
Music & Silence    4/10    Music cues hard-cut at scene transitions.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 4

ATTRIBUTION MAP
#    Timecode    Voice    Attributed to    Confidence    Problem
1    0:12    VOICE A    Woman    RESOLVED    None
2    0:22    VOICE B    Man    RESOLVED    None
3    0:28    VOICE A    Woman    INFERRED    Spoken off-screen, but established as her.
4    0:31    VOICE B    Man    RESOLVED    None
5    0:52    VOICE A    Woman    RESOLVED    None
6    0:58    VOICE B    Man    RESOLVED    None
7    1:52    VOICE A    Woman    RESOLVED    None

VOICE DRIFT COMPARISON
Character    First line (tc)    Last line (tc)    Same voice?    What moved
Woman    0:12    1:52    Yes    Acoustic space only (comms -> dry).
Man    0:22    0:58    Yes    Acoustic space only (comms -> dry).

SYNTHETIC TELL LOG
Timecode    Voice    Register    Tell observed    Severity
0:31    B    HUMAN    Perfectly metronomic timing between phrases despite running.    🟡 MINOR
0:52    A    HUMAN    Loss of comms filtering despite helmet still being sealed.    🟠 MAJOR
1:52    A    HUMAN    Delivery is flat and calm while navigating an active fire.    🟠 MAJOR

AMBIENCE HOLE LOG
Drops at    Returns at    Location    Absolute silence?    Severity
0:50    0:51    Ship transition    Yes (1 sec hole)    🟡 MINOR
1:20    1:40    Space Orbit    Yes    🟠 MAJOR

CONTRADICTION LOG
Timecode A    Timecode B    Element    Category    What contradicts what    Severity
0:12    0:52    Processing    Voice Identity Continuity    Voice A has a comms filter on the ice, but is completely dry in the cockpit, despite the helmet remaining sealed in both shots.    🟠 MAJOR
1:20    1:40    Ambience    Ambience Continuity    The ship interior has a hum at 1:19, but cuts to absolute digital silence for 20 seconds during the space approach.    🟠 MAJOR
2:50    3:00    Mix Level    Mix Hierarchy    Dialogue is clear before the fire, but entirely swallowed by 5 overlapping layers (fire, alarm, music, breathing) at 3:00.    🟠 MAJOR

THE THREE THAT MATTER
Absolute silence during space approach (1:20-1:40)
Why: It feels like the audio engine crashed. It pulls the viewer entirely out of the film.
Fix: Re-level / add a low-frequency hum or subtle music bed.
Dialogue buried by fire SFX (3:00)
Why: The audience cannot hear the characters during the climax.
Fix: Re-level (duck the SFX bed by -6dB during speech).
Comms filter vanishes (0:52)
Why: Contradicts the visual reality of two people wearing sealed helmets.
Fix: Re-level (apply EQ/filter to match the earlier lines).

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Finding    Fix    Cost
Ambience holes / dead space    Re-level / add bed    Mid
Dialogue buried at climax    Re-level / ducking    Low
Comms filter inconsistency    Apply EQ in mix    Low
Unmotivated calm delivery at 1:52    Regenerate clip    High
Missing footsteps on ice    Add foley    Mid

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The explosion at 1:40 is loud and bass-heavy in a vacuum.    Does the plan dictate hard realism (silent space) or cinematic physics (loud explosions)?
Total silence between 1:20 and 1:40.    Was this a designed moment of contrast, or a missed ambience track?

OUT-OF-SCOPE FLAGS
Lip-sync phoneme matching is imprecise on the final two lines -> VIDEO_QA
Explosion sound in vacuum -> VIDEO_QA
Helmet visibility contradicts itself at the end -> KARAKTER_QA
