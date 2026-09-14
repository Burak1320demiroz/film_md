# 🔊 THE BORROWED WEIGHT — ③ SES_QA HAM RAPORU

> Çalıştırma: 24.08.2026 · yalnız video (kural gereği: bu rubriğe belge verilmez)
> Rubrik: `../QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md`
> ⚠️ Dört mercekli partinin parçası. **Parti ⑤ ÇAPRAZ SAYIM kapısından geçmedi**
> → 🚨 GEÇERSİZ; skor satırı T3 tablosuna İŞLENMEDİ.
> ⛔ REGISTER DOĞRULAMASI (kart E3 adım 2): plan HUMAN 0 · MACHINE 4 diyor.
> Rapor iki repliği de HUMAN yazdı ve "sentetik duruyor" bulgusuyla
> Sentetik hücresini 4/10'a indirdi → **bu bulgu DÜŞER**.
> ⭐ Bu raporun DIALOGUE LEDGER'ı partinin en değerli belgesi oldu: replik
> alıntısı, hangi raporun ölçtüğünü hangisinin uydurduğunu tek satırda
> ayırdı (**DERS 121**).
> Kapı defterleri: `../01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

FILM: the borrowed weıght (1).mp4
RUNTIME: 04:24 MEASURED
AUDIO STATE: A · SPOKEN LINES: 2 · CUTS COUNTED: 24
DISTINCT VOICES: 1 · REGISTERS: 1 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY — this review measures whether the soundtrack agrees with itself and with the picture, not whether it matches a script.

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      54.0
DIVISION:           54.0 ÷ 9 = 6.0

OVERALL SCORE: 6.0/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX

AUDIO LEDGER
1a. DIALOGUE LEDGER
#    In-out    Transcribed line (verbatim)    Whose voice    Mouth visible?    Mouth moving?    Source    Intended register
1    0:23-0:26    "The weight is all we have left."    Astronaut VO    No    No    OFF-SCREEN    HUMAN
2    0:33-0:36    "The weight is all we have left."    Astronaut VO    No    No    OFF-SCREEN    HUMAN

1b. VOICE PASSPORT
Label: Astronaut VO
First heard: 0:23
Register: HUMAN
Pitch & range: Low, narrow movement
Age & gender coding: Older male
Accent / diction: American, gravelly, slow delivery
Processing: Dry, close-mic, no environmental reverb
Breath: None audible
Attributed to: Astronaut (inferred)

1c. AMBIENCE MAP
Scene / location    In-out    Ambient bed    Level    Notes
Plain    0:00-0:09    Desolate wind, low rumble    Mid    Establishes space
Plain    0:10-0:19    Digital silence    None    Hard drop at cut
Plain    0:20-0:49    Wind, low rumble    Mid    Returns abruptly
Plain    0:50-0:59    Digital silence    None    Hard drop
Plain    1:00-4:24    Wind, low rumble    Mid    Persistent but drops repeatedly at cuts (e.g., 1:40, 2:10, 3:20)

1d. LAYER COUNT
Timecode    Layers audible    Count    Dialogue intelligible?
0:25    VO, Wind, Drone    3    Yes
1:05    Wind, Drone, Metal clink    3    N/A
3:25    Wind, Heavy Drone    2    N/A

1e. MUSIC LEDGER
Cue    In-out    Enters on    Exits on    Under dialogue?    Ducked?
Low Drone    0:00-4:24    0:00    4:24    Yes    No

SCORES SUMMARY
Category    Score    Critical Issue
Speaker Attribution    8/10    −2 · 0:23 (F1)
Synthetic Voice Tells    4/10    −6 · 0:33 (F1)
Voice Identity Continuity    10/10    no in-scope source
Delivery vs Performance    7/10    −3 · 0:23 (F1)
Turn-Taking & Acoustics    6/10    −4 · 0:23 (F1)
Ambience Continuity    2/10    −8 · 0:10 (F1) · 0:50 (F2) · 1:40 (F3) · 2:10 (F4)
SFX Causality & Sync    4/10    −3 · 0:27 (F1) · −3 · 3:52 (F2)
Mix Hierarchy & Levels    7/10    −3 · 3:20 (F1)
Music & Silence    6/10    −4 · 1:00 (F1)

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 5   🟡 MINOR: 4

ATTRIBUTION MAP
#    Timecode    Voice    Attributed to    Confidence    Problem
1    0:23    Astronaut VO    Astronaut    INFERRED    No framing or comms filter establishes this VO.
2    0:33    Astronaut VO    Astronaut    INFERRED    Repeated unestablished VO.

VOICE DRIFT COMPARISON
Character    First line (tc)    Last line (tc)    Same voice?    What moved
Astronaut VO    0:23    0:33    Yes    No drift. Exact duplicate.

SYNTHETIC TELL LOG
Timecode    Voice    Register    Tell observed    Severity
0:33    Astronaut VO    HUMAN    Exact identical acoustic duplicate of the line from 0:23. Prosody and timing are mathematically identical.    🟠 MAJOR
0:23    Astronaut VO    HUMAN    Zero breath before a grave, dramatic line.    🟡 MINOR

AMBIENCE HOLE LOG
Drops at    Returns at    Location    Absolute silence?    Severity
0:10    0:20    Plain    Yes    🟠 MAJOR
0:50    1:00    Plain    Yes    🟠 MAJOR
1:40    1:50    Plain    Yes    🟠 MAJOR
2:10    2:20    Plain    Yes    🟠 MAJOR

CONTRADICTION LOG
Timecode A    Timecode B    Element    Category    What contradicts what    Severity
0:23    0:33    Voice    2    Exact duplicate sample used for two separate narrative thoughts    🟠 MAJOR
0:09    0:10    Ambience    6    Wind bed drops to digital zero across the cut    🟠 MAJOR

THE THREE THAT MATTER
Ambience Dropouts at Cuts: The bed of wind and low rumble abruptly vanishes into digital silence at multiple clip boundaries (0:10, 0:50, 1:40). It breaks the world entirely. Fix: Re-cut/Add a continuous stereo ambient track across the whole edit.

Missing SFX on Heavy Impacts: The heavy metal strut is dropped, and the pod hatch is opened, with absolutely no corresponding sound effects. The visuals demand weight, the audio provides nothing. Fix: Re-mix/Add foley.

Repeated Voice Generation: The line at 0:33 is an exact, mathematically identical audio file to the line at 0:23. It immediately reads to the ear as an AI-generated anomaly. Fix: Replace or remove the second line.

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Finding    Fix    Cost
Ambience holes at cuts    Lay down continuous room tone/wind    Low
Missing SFX    Foley / Sound Design pass    Low
Dry VO outdoors    Add subtle slapback / verb to VO    Low
Repeated identical VO line    Mute or replace line    Low

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The VO line repeats verbatim at 0:23 and 0:33.    Was the script written with this repetition, or is this an AI generation looping error?
The VO has no comms filter but the character is in a sealed suit.    Was this intended as an internal monologue, or a radio transmission?

OUT-OF-SCOPE FLAGS
0:23 — lips do not move while voice speaks (assuming on-screen, but logged as OFF-SCREEN for safety) → the FRAME lens
0:40 — suit chest plate geometry changes drastically → the CONTINUITY lens
