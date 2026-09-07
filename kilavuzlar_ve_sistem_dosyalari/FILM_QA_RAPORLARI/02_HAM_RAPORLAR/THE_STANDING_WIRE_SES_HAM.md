# THE STANDING WIRE — ③ SES QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi (raporun yazdığı): `the standıng wıre.mp4` · rapor süresi ~245 s
> ⛔ ⑪.0 KİMLİK [D160]: aynı ada uyan İKİ dosya var, ikisi de ölçüldü —
>   `~/Downloads/the standıng wıre.mp4` 1280x720 · 245,141 s
>   `~/Downloads/the standıng wıre (1).mp4` 3840x2160 · 245,141 s  ← MASTER, ölçüm bunda koşuldu
>   AYNI KURGU (süre birebir), farklı çözünürlük. Rapor 720p kopyayı ölçmüş.
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 05.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_3_5_dk_filmler/THE_STANDING_WIRE/THE_STANDING_WIRE_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/PAKET_1..8` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
> ⛔ AYRICA TESLİM KUSURU [D150]: master ÜRETİCİ FİLİGRANI taşıyor (Flow ▷ ikonu, 6/6 örnek).
>   Filigranlı master master değildir → sekiz mercek onu ÖLÇMEMİŞ sayılır, mod Vden bağımsız olarak.
> ⛔ ⑤/⑦ notu: sekiz mercek AYNI OTURUMDA koşuldu → bağımsız ölçüm değildir [D110].

---

FILM: THE STANDING WIRE
RUNTIME: ~04:04 ESTIMATED
AUDIO STATE: A · SPOKEN LINES: 4 · CUTS COUNTED: 23
NON-SCENE MATERIAL: 4:00-4:04 Title Card
LINES HEARD: 4
"Just a little further." at 0:50
"The wire is still holding." at 0:52
"Made it this far." at 0:55
"Almost at the top." at 0:58
DISTINCT VOICES: 1 · REGISTERS: 1 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY — this review measures whether the soundtrack
agrees with itself and with the picture, not whether it matches a script.

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  8
SUM OF SCORES:      60.0
DIVISION:           60.0 ÷ 8 = 7.5

OVERALL SCORE: 7.5/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX

AUDIO LEDGER
1a. DIALOGUE LEDGER
#    In-out    Transcribed line (verbatim)    Whose voice    Mouth visible?    Mouth moving?    Source    Intended register
1    0:50-0:51    "Just a little further."    The Astronaut    No    No    COMMS    HUMAN
2    0:52-0:53    "The wire is still holding."    The Astronaut    No    No    COMMS    HUMAN
3    0:55-0:56    "Made it this far."    The Astronaut    No    No    COMMS    HUMAN
4    0:58-0:59    "Almost at the top."    The Astronaut    No    No    COMMS    HUMAN

1b. VOICE PASSPORT
Label:          The Astronaut
First heard:    0:50
Register:       HUMAN
Pitch & range:  Mid-pitch, narrow conversational range
Age & gender coding: Adult female, 30s
Accent / diction: Standard American, clear diction
Processing:     Slight radio/helmet EQ filtering
Breath:         None audible between phrases
Attributed to:  The Astronaut (on-screen, back to camera)

1c. AMBIENCE MAP
Scene / location    In-out    Ambient bed (what you hear)    Level    Notes
Canyon Base    0:00-0:40    Heavy wind, low gravel crunches    Mid    Drops noticeably at cuts
Rock Stairs/Wall    0:40-1:20    Wind whistling, fabric rustle    Mid-Low    Hard cuts on scene boundaries
High Plateau    1:20-2:30    High altitude wind drone    Mid    -
Orbit Bridge    2:30-3:20    Metallic resonance, thinning wind    Low    -
Orbit Dock/Space    3:20-3:50    Low sub-frequency rumble, airlock    Mid-Low    -

1d. LAYER COUNT
Timecode    Layers audible (name each)    Count    Dialogue intelligible?
0:20    Wind bed, footsteps, wire clank    3    N/A
0:52    Wind bed, musical drone, voice, suit rustle    4    Yes
2:40    Orchestral music swell, sub drone    2    N/A

1e. MUSIC LEDGER
Cue    In-out    Enters on    Exits on    Under dialogue?    Ducked?
Epic Ascent    0:20-4:04    Astronaut walking    End of film    Yes    Yes

SCORES SUMMARY
Category    Score    Critical Issue
Speaker Attribution    10/10    no in-scope source
Synthetic Voice Tells    7/10    -3 · 0:50 (F1) · 0:58 (F2)
Voice Identity Continuity    10/10    no in-scope source
Delivery vs Performance    4/10    -6 · 0:50 (F3) · 0:58 (F4)
Turn-Taking & Acoustics    —    no in-scope source
Ambience Continuity    6/10    -4 · 0:20 (F5) · 0:40 (F6)
SFX Causality & Sync    7/10    -3 · 2:20 (F7)
Mix Hierarchy & Levels    8/10    -2 · 2:40 (F8)
Music & Silence    8/10    -2 · 3:50 (F9)

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 4

ATTRIBUTION MAP
#    Timecode    Voice    Attributed to    Confidence    Problem
1-4    0:50-0:59    The Astronaut    The Astronaut    INFERRED    None, only one character present.

VOICE DRIFT COMPARISON
Character    First line (tc)    Last line (tc)    Same voice?    What moved
The Astronaut    0:50    0:58    Yes    No drift.

SYNTHETIC TELL LOG
Timecode    Voice    Register    Tell observed    Severity
0:50    The Astronaut    HUMAN    Perfectly even pacing with zero audible inhalation before speaking.    🟡 MINOR
0:58    The Astronaut    HUMAN    Sentence pitch lands on the exact same falling note as the previous three lines.    🟡 MINOR

AMBIENCE HOLE LOG
Drops at    Returns at    Location    Absolute silence?    Severity
0:20    0:20.5    Canyon floor    No, floor uncertain    🟡 MINOR
0:40    0:40.5    Rock stairs    No, bed thins    🟡 MINOR

CONTRADICTION LOG
Timecode A    Timecode B    Element    Category    What contradicts what    Severity
0:50    0:58    Delivery    4    Vocal effort (calm, resting) contradicts physical effort (free-climbing a massive vertical rock face in a heavy suit).    🟠 MAJOR
2:18    2:22    SFX Sync    7    Footfall sound effects do not align with the visible pace of the boots hitting the rock.    🟠 MAJOR

THE THREE THAT MATTER
Delivery vs Physical Effort (0:50): The voice acting sounds like it was recorded by someone sitting in a chair, while the character is vertically free-climbing a cliff. It breaks the illusion of exertion. Fixable in the mix: replace the VO lines with takes that include heavy breathing and strain.
Footstep SFX Sync Drift (2:20): The heavy boot sounds fall out of rhythm with the character's visible walk cycle on the wide plateau. Fixable in the mix: nudge the SFX regions to lock to the heel strikes.
Ambience Drops at Cuts (0:20, 0:40): The wind and room tone slightly cut out at the clip boundaries before fading back in. Fixable in the mix: extend handles and crossfade the ambient beds across the cuts.

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Finding    Fix    Cost
Synthetic prosody / lack of breath    Replace VO lines    Low (Mix)
Delivery effort mismatch    Replace VO lines to match climb    Low (Mix)
Footstep sync drift    Slip SFX audio regions    Low (Mix)
Ambience dropping at cuts    Crossfade ambient beds    Low (Mix)

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The voice at 0:50 has a slight comms filter but is not speaking to anyone on screen.    Is this intended to be an internal monologue, a log recording, or live comms with an off-screen base?
The music builds to a massive climax in space.    Was a music-free zone or absolute silence intended when the character enters the vacuum of space?

OUT-OF-SCOPE FLAGS
3:36 — Airborne airlock whoosh sound propagating in the vacuum of space. → FRAME lens
