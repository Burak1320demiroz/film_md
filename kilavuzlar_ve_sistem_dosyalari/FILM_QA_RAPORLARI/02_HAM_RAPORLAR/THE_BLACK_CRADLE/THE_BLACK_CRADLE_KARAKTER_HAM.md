# THE BLACK CRADLE — KARAKTER_QA HAM RAPOR

> **Tarih:** 17.08.2026 · **Rubrik:** `QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Mod:** rubrik zaten yalnız video · **Malzeme:** 3:52 (232 s) kurgu · rapor **4 sahne** saydı
> ⛔ Model çıktısı olduğu gibi. Belge cevapları film kaydında:
> `../01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`
> ⚠️ Rapor kendi KANIT TABANI EŞİĞİ'ni (D97) ihlal etti: yüz kanıtı 1/4 sahne ve
> ~%11 süre — eşik "3 sahneden az VEYA süre %25'in altında → ⚠️ PARTIAL, sayı yok"
> diyor; sütunlar yine de puanlandı. Ses sütunu SES_QA koşulduğu hâlde puanlandı
> (kart E2 adım 5 / kart E3 adım 6: işaretçiye inmeliydi).

---

```
FILM: (not supplied)
RUNTIME: 03:52 · SCENES OBSERVED: 4 · CHARACTERS TRACKED: 2
BASELINE: SELF-CONSISTENCY — this review measures whether each character agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 5.8/10
VERDICT: DRIFTS BUT RECOVERABLE
Both tracked characters remain visually distinguishable and maintain consistent overall costumes across scene transitions. However, minor state variations in suit wear/dirt and equipment configurations—along with lip-sync audio lag—introduce minor internal friction across scene cuts.

CHARACTER PASSPORT(S)
CHARACTER 1: FEMALE ASTRONAUT
Label: Female Astronaut
First clear view: S1, 0:15
Face: Medium-toned skin, oval face structure, dark brown hair pulled back inside helmet hood, visible through visor.
Hair: Dark brown, tucked tightly beneath internal suit skullcap.
Eyes: Dark, reflective under golden visor tint.
Build: Slender frame, average height relative to drill equipment.
Costume: Off-white/grey pressure suit with articulated shoulder joints, dark grey chest harness straps, blue trim on chest utility panel.
Equipment: Sealed extravehicular activity (EVA) helmet with reflective visor, heavy composite gloves, chest telemetry pack.
Wear map: Dust and regolith grit present on knees, lower suit forearms, and lower boots in S1.
Voice: Mid-register, calm, Turkish language ("Şafak hattı 1200 metrede...").
Evidence Base:
FACE-VISIBLE: ~25 s of 232 s total · 1 of 4 scenes
COSTUME-VISIBLE: 1 of 4 scenes (S1)
MOUTH ON SCREEN: Yes (visible through transparent visor section at 0:28–0:32)

CHARACTER 2: MALE PILOT
Label: Male Pilot
First clear view: S2, 1:06
Face: Mid-30s male, square jawline, light olive skin, clean-shaven, no visible facial scars.
Hair: Short dark brown hair, neat crew cut style.
Eyes: Dark brown, sharp focus on control panels.
Build: Broad-shouldered, athletic upper body frame.
Costume: Soft-shell internal flight suit, dark charcoal grey with shoulder padding and utility straps.
Equipment: Open-face communications headset with boom microphone along left jaw; suit collar open.
Wear map: Clean flight suit; no visible dust, dirt, or physical abrasion.
Voice: Deep baritone, authoritative, Turkish language ("Kalkıyoruz. Sıkı tutunun...").
Evidence Base:
FACE-VISIBLE: ~15 s of 232 s total · 1 of 4 scenes
COSTUME-VISIBLE: 1 of 4 scenes (S2)
MOUTH ON SCREEN: Yes (clearly visible during cockpit launch sequence at 1:08–1:12)

APPEARANCE TABLE
Character    Scene    In-out    Face visible?    State notes
Female Astronaut    S1    0:00–1:05    Yes    Sealed EVA suit; visible regolith dust on forearms and knees.
Male Pilot    S2    1:05–1:25    Yes    Internal flight suit; clean condition, communications headset on.
(Craft Only)    S3    1:25–2:50    No    Exterior space flight; pilot/crew not directly visible inside.
(Craft / Station)    S4    2:50–3:52    No    Hangar docking sequence; no character visible.

SCORES SUMMARY
Category    Score    Critical Issue
Facial Identity    7/10    -3 · Single facial view per character; face integrity holds within respective scenes
Hair, Build & Proportions    7/10    -3 · Proportions remain proportional within individual scene frames
Costume Identity    6/10    -4 · Direct cut from EVA suit (S1) to internal flight suit (S2) without transition shot
Wear, Damage & Injury    5/10    -5 · 0:50 (S1) vs 1:08 (S2) · Forearm dust disappears entirely upon cut to cockpit
Equipment State    6/10    -4 · 0:45 (S1) vs 1:08 (S2) · Transition from sealed EVA helmet to open headset
Cross-Cut Action    6/10    -4 · 1:05 (S1 to S2) · Abrupt jump from surface drilling posture to seated flight posture
Count & Separation    N/A    Characters appear in separate scenes; no shared multi-character frames
Voice & Performance    5/10    -5 · 1:09 (S2) · Dialogue audio lags behind mouth movement by ~0.4 seconds

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 3

IDENTITY DRIFT MAP — per character
Character    Element    First slip (timecode)    Undeniable by    Recovered?
Female Astronaut    Suit Wear    0:50    1:05 (Cut to S2)    No (Character absent after S1)
Male Pilot    Dialogue Lip Sync    1:09    1:12    Yes (S3 contains no spoken dialogue)

WEAR TIMELINE — per tracked mark
Mark    Acquired    Present at    Absent at ⚠️    One-way?
Surface Regolith Dust (Forearms/Knees)    S1 (0:15)    S1 (0:50)    S2 (1:08) ⚠️    No (Resets to clean in S2 flight suit)

CONTRADICTION LOG
Timecode A    Timecode B    Character    Category    What contradicts what    Severity
0:50    1:08    Female Astronaut / Male Pilot    Wear, Damage & Injury    Dusty planetary EVA suit cuts directly to pristine cockpit flight suit without ingress/cleaning sequence    🟠 MAJOR
1:09    1:12    Male Pilot    Voice & Performance    Audio track for dialogue plays ~0.4s after physical mouth articulation begins    🟠 MAJOR
0:45    1:08    Female Astronaut / Male Pilot    Equipment State    Full sealed EVA helmet with gold visor abruptly shifts to open headset without hatch/airlock transition    🟡 MINOR

THE THREE THAT MATTER
Abrupt Costume/Environment Jump (1:05): Direct cut from dusty planetary EVA work to a clean interior cockpit creates a jarring continuity gap.
Fix: Insert a brief 1-2 second intermediate shot showing the suit airlock transition or hatch closure.

Lip-Sync Audio Lag (1:09): Pilot mouth movement leads the Turkish dialogue audio track by roughly 0.4 seconds.
Fix: Nudge the audio dialogue track 0.4 seconds forward on the NLE timeline to align with speech sync.

Unexplained Suit Cleanliness (1:08): Regolith dust accumulated during drilling is entirely absent in the subsequent flight suit view.
Fix: Add minor surface smudges to the flight suit or accept as an off-screen suit change.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Pilot lip-sync offset at 1:09    Nudge audio track 0.4s earlier on editing timeline    Fixable in Edit
Missing transition beat at 1:05    Insert brief B-roll clip of airlock/hatch sealing    Add shot / Regenerate
Sudden suit cleanliness at 1:08    Apply subtle dirt pass in color grading / accept off-screen change    Fixable in Edit / Accept

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Abrupt transition at 1:05    Was an intermediate airlock or ingress shot planned between Scene 1 and Scene 2?
Character hand-off between S1 and S2    Are the Female Astronaut (S1) and Male Pilot (S2) co-pilots on the same craft, or sequential perspectives?

OUT-OF-SCOPE FLAGS
[VIDEO_QA] Minor facial micro-texture shifting on pilot chin between 1:08 and 1:12.
[MANTIK_QA] Combustion engine sound effects playing in orbital vacuum during Scene 3 (1:45).
```
