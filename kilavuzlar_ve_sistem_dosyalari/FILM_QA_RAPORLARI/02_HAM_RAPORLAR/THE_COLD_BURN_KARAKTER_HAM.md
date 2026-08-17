# 🧍 THE COLD BURN — KARAKTER_QA HAM RAPORU

> Çalıştırma: 09.08.2026 · MOD V (rubrik zaten belgesiz çalışır — Gemini)
> Rubrik: `../QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> Ölçülen malzeme: 225 s kurgu / 12 sahne. Belge cevapları:
> `../01_FILM_RAPORLARI/THE_COLD_BURN.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④). DERS 65 TUTTU.
> ✅ KLONSUZ koşu — D69/D77 sıcak noktası (biniş/iniş + tünel) bu kurguda
> tekrarlamadı (ama planın en riskli sahnesi S25 tünel zaten ekranda yok).
> ⚠️ D79 pasaport alanı yine iş gördü: her iki pasaportta da "backpack" —
> bible SIRT DÜZ diyor → D79'un 4. vakası (belge kontrolünde).
> ⚠️ SES_QA aynı kurguya koşulduğu için 8. kategori (Ses) birleştirmede
> işaretçiye iner (kart E3 adım 6) — ayrıntı 07_SES_KALITE_TABLOSU.md.

---

FILM: (not supplied)
RUNTIME: 03:45 · SCENES OBSERVED: 12 · CHARACTERS TRACKED: 2
BASELINE: SELF-CONSISTENCY — this review measures whether each character
agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 6/10
VERDICT: DRIFTS BUT RECOVERABLE

CHARACTER PASSPORT(S)
Label: The Man
First clear view: S2, 0:10
Face: Older Black male, gray beard, short gray hair.
Build: Broad, average height.
Costume: White base suit, orange accent lines, chest panels.
Equipment: Helmet with clear visor, backpack. Holds blue sample/metal case.
Wear map: Clean initially.
Voice: Deep, calm, authoritative.

Label: The Woman
First clear view: S2, 0:10
Face: Dark hair, fair skin, sharp jawline.
Build: Slim, slightly shorter than the man.
Costume: White base suit, teal/blue accent lines, chest panels.
Equipment: Helmet with clear visor, backpack.
Wear map: Clean initially.
Voice: Clear, composed.

APPEARANCE TABLE
Character    Scene    In-out    Face visible?    State notes
Man/Woman    S2    0:10-0:20    Yes (through visors)    Kneeling, collecting sample.
Man/Woman    S3    0:20-0:40    Yes    Standing, holding arms/hands.
Man/Woman    S4    0:40-0:50    Yes    Running; man holds case.
Man/Woman    S5    0:50-1:20    Yes    Cockpit seated, visors down.
Man/Woman    S9    2:50-3:10    Yes    Floating inside station, visors down.
Man/Woman    S10    3:10-3:30    Yes    Escaping fire, closing hatch.
Woman    S12    3:40-3:45    Yes    Title card, helmet suddenly absent.

SCORES SUMMARY
Category    Score    Critical Issue
Facial Identity    7/10    Highly consistent across scenes.
Hair, Build & Proportions    7/10    Proportions hold well.
Costume Identity    6/10    Suits maintain respective orange/teal accents.
Wear, Damage & Injury    5/10    Snow/wear resets when entering ship.
Equipment State    4/10    Carried sample case vanishes completely.
Cross-Cut Action    6/10    Eyelines and positions match in cockpit.
Count & Separation    7/10    Exactly two people throughout; no clones.
Voice & Performance    6/10    Voices match physical presence consistently.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 2

IDENTITY DRIFT MAP — per character
Character    Element    First slip (timecode)    Undeniable by    Recovered?
Man    Metal Case    0:50    0:55    No.
Woman    Helmet    3:40    3:42    No, film ends.

WEAR TIMELINE — per tracked mark
Mark    Acquired    Present at    Absent at ⚠️    One-way?
Snow/Frost on suits    0:40    0:45    0:50    No (resets).

CONTRADICTION LOG
Timecode A    Timecode B    Character    Category    What contradicts what    Severity
0:45    0:50    Man    Equipment State    Man carries metal case while running; case is entirely missing in cockpit.    🟠 MAJOR
0:45    0:50    Both    Wear, Damage & Injury    Suits show snow accumulation outside, but are perfectly clean upon cockpit entry.    🟡 MINOR
3:30    3:40    Woman    Costume Identity    Helmet is on and sealed during jump; helmet is completely gone in the final title card shot.    🟡 MINOR

THE THREE THAT MATTER
Vanishing metal case (0:45 vs 0:50)
Why: The object drives the entire opening scene but disappears immediately after.
Fix: Add a quick insert shot of the case secured in the cockpit.
Suit wear reset (0:45 vs 0:50)
Why: Breaks physical continuity of the storm's impact.
Fix: Accept it; pacing masks the error.
Helmet disappearance (3:30 vs 3:40)
Why: Inexplicable costume change in deep space.
Fix: Cut the title card scene entirely.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Vanishing case    Add insert shot of secured case.    Low
Suit snow reset    Accept.    Zero
Final helmet loss    Cut S12 (title card).    Zero

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The metal case is never seen after S4.    Does the script specify the case being stowed, or did the model drop it?
The final shot features the woman without a helmet.    Was this un-helmeted hero shot mandated by the design document despite the space setting?

OUT-OF-SCOPE FLAGS
Title card text violation -> VIDEO_QA
Dramatic purpose of the blue sample never resolves -> SENARYO_QA
