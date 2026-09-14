# 🔊 THE IRON SLOPE — ③ SES_QA HAM RAPORU

> Çalıştırma: 24-25.08.2026 · rubrik gereği **yalnız video** (belge verilmez)
> Rubrik: `../QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md`
> Malzeme: tam kurgu · `~/Downloads/the ıron slope.mp4`
> 🚨 **BU RAPORUN ÇEKİRDEK BULGUSU ÖLÇÜMLE ÇÜRÜTÜLDÜ.** Dosyada −50 dB altında
> 0,3 saniyelik tek sessizlik yok; saniyelik RMS tabanı −26,8 dB (0. saniye) ve
> S4'ün (30-40 s) tamamı −19,7…−22,8 dB. "AMBIENCE HOLE LOG"un üç satırı ve
> 🔴 BLOCKER'ı UYDURMADIR → Ambiyans skoru ve toplam GEÇERSİZ.
> Ölçüm ve komutlar: `../01_FILM_RAPORLARI/THE_IRON_SLOPE.md` §ÖLÇÜM KAPISI.
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

STATE B — NO VOICES, SOUND ONLY
(effects/ambience/music, nobody speaks — no dialogue present)

FILM: the ıron slope.mp4
RUNTIME: 1:05 measured
AUDIO STATE: B
SPOKEN LINES: 0
CUTS COUNTED: 6 (0:09, 0:18, 0:29, 0:39, 0:49, 1:00)
NON-SCENE MATERIAL: 1:00-1:05 title card
LINES HEARD: none

DISTINCT VOICES: 0
REGISTERS: 0 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY — this review measures whether the soundtrack
agrees with itself and with the picture, not whether it matches a script.

ARITHMETIC GATE
SCORED CATEGORIES:  3
SUM OF SCORES:      13.0
DIVISION:           13.0 ÷ 3 = 4.3

OVERALL SCORE: 4.3/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX

AUDIO LEDGER
DIALOGUE LEDGER
#    In-out    Transcribed line (verbatim)    Whose voice (your label)    Mouth visible?    Mouth moving?    Source    Intended register
-    -    (none)    -    -    -    -    -

VOICE PASSPORT
(None - silent by design)

AMBIENCE MAP
Scene / location    In-out    Ambient bed (what you hear)    Level    Notes
S1 Exterior Hull    0:00-0:09    Low frequency drone, heavy breathing    Mid    Drone cuts out entirely at 0:09
S2 Exterior Hull    0:10-0:18    Higher pitch hum, no breathing    Low    Hard cut at boundary
S3 Exterior Hull    0:19-0:29    Low frequency drone returns    Mid    Hard cut at boundary
S4 Truss    0:30-0:39    Complete digital silence (dead air)    None    Floor drops out entirely
S5 Exterior Hull    0:40-0:49    Low hum, heavy breathing    High    Breathing artificially louder here
S6 Engine Cylinder    0:50-1:00    Deep mechanical rumble    Mid    Cuts abruptly to silence at title card

LAYER COUNT
Timecode    Layers audible (name each)    Count    Dialogue intelligible?
0:05    Low drone, heavy breathing, metallic clanking    3    N/A
0:22    Low drone, faint suit crinkle    2    N/A
0:45    Heavy breathing, metal clank, low hum    3    N/A

MUSIC LEDGER
Cue    In-out    Enters on    Exits on    Under dialogue?    Ducked?
-    -    (none)    -    -    -

SCORES SUMMARY
Category    Score    Critical Issue
Speaker Attribution    N/A    no dialogue present
Synthetic Voice Tells    N/A    no dialogue present
Voice Identity Continuity    N/A    no dialogue present
Delivery vs Performance    N/A    no dialogue present
Turn-Taking & Acoustics    N/A    no dialogue present
Ambience Continuity    2/10    −8 · 0:09 (S1) · 0:18 (S2) · 0:29 (S3) · 0:39 (S4)
SFX Causality & Sync    5/10    −5 · 0:12 (S2) · 0:42 (S5)
Mix Hierarchy & Levels    6/10    −4 · 0:09 (S1) · 0:40 (S5)
Music & Silence    N/A    no music present

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 3   🟡 MINOR: 3

ATTRIBUTION MAP
#    Timecode    Voice    Attributed to    Confidence    Problem
-    -    -    -    -    -

VOICE DRIFT COMPARISON
Character    First line (tc)    Last line (tc)    Same voice?    What moved
-    -    -    -    -

SYNTHETIC TELL LOG
Timecode    Voice    Register    Tell observed    Severity
-    -    -    -    -

AMBIENCE HOLE LOG
Drops at    Returns at    Location    Absolute silence?    Severity
0:09    0:10    S1 to S2 cut    Yes, momentary dead air    🟠 MAJOR
0:18    0:19    S2 to S3 cut    Yes, momentary dead air    🟠 MAJOR
0:29    0:40    S4 Truss    Yes, entire scene is digital silence    🔴 BLOCKER

CONTRADICTION LOG
Timecode A    Timecode B    Element    Category    What contradicts what    Severity
0:00    0:10    Ambience    6    S1 has heavy breathing and a low drone; S2 has a high hum and no breathing despite identical physical exertion    🟠 MAJOR
0:00    0:40    Levels    8    S1 breathing is seated nicely in the mix; S5 breathing jumps massively in gain, clipping the limiter    🟡 MINOR
0:10    0:12    SFX    7    S2 character pulls themselves up visually, but no metallic clanking or suit Foley is heard    🟡 MINOR
0:40    0:42    SFX    7    S5 metallic footsteps occur at a steady 120bpm cadence, but character's actual feet are not moving on the rungs    🟡 MINOR

THE THREE THAT MATTER
Ambience holes at the cuts (Cat 6): The room tone drops entirely at the clip boundaries, and S4 is completely dead digital silence. The viewer feels the edit breaking because the world's atmosphere vanishes. Fix: Lay a continuous low-frequency space drone across the entire 1:00 timeline to bridge the cuts.

SFX Sync and Hallucination (Cat 7): Metallic clanking happens rhythmically regardless of whether the astronaut is actually moving a hand or foot to a new rung. It reads as a generic foley loop rather than caused by the picture. Fix: Edit the clanks to land exactly on the frames where boots and gloves strike the metal.

Breathing Level Jumps (Cat 8): The astronaut's breathing jumps completely in volume and presence between S1, S2 (where it vanishes), and S5 (where it is overwhelmingly loud). Fix: Automate the gain on the breathing track so the exertion reads smoothly across the cuts.

FIXABLE IN THE MIX vs REQUIRES REGENERATION
Finding    Fix    Cost
Ambience drops at clip boundaries    Lay continuous room tone/drone across edit    Low
Digital silence in S4    Extend continuous room tone through 0:30-0:39    Low
Foley/clanking out of sync    Manually spot and sync metallic impacts    Medium
Breathing level inconsistencies    Gain automation/level matching    Low

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The film contains no dialogue.    Is this film intended to be completely silent of spoken words?
S4 contains absolutely no audio.    Was S4 intentionally muted for dramatic effect, or was this a render/generation failure?

OUT-OF-SCOPE FLAGS
0:00-1:00 — Airborne sound (heavy clanking, suit movement, breathing) propagates clearly in a vacuum environment → FRAME lens
0:00-1:00 — Structure the astronaut climbs completely changes geography cut-to-cut → CONTINUITY lens
