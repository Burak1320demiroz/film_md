# 🦕 THE FIRST MORNING — SHORTS_QA HAM ÇIKTI (06.08.2026)

> ⚠️ **DOKUNULMAZ.** Model çıktısı olduğu gibi, düzenlenmeden kaydedildi
> (AGENTS kural ④). Rubrik: `../../QA_PROMPTLARI/SHORTS_QA_CRITIQUE_PROMPT.md`
> · Koşu: **INPUT MODE V** (SPEC verilmedi) · MATERIAL MODE B iddiası.
>
> **Plan dosyası:** `dikey_shorts_filmler/THE_FIRST_MORNING/THE_FIRST_MORNING_DIKEY_SHORTS.md`
> — 821 satır, 6 sahne × 8 s = 48 s planı. **Depoda duruyordu** (MOD V
> koşusu geçerli; künye uydurulmadı, "not supplied" yazıldı ✅ Ders 60/65'e
> uygun).
>
> ⚠️ Dikkat: rapor MATERIAL MODE **B (full 48s cut)** ilan edip süreyi
> **64 s / 7 segment** ölçtü ve kendi numaralandırmasını (S0-S6) açıkça
> beyan etti — Ders 66'ya uygun davranış, ama kurgunun kendisi 48 s
> tavanını aşıyor (bkz. DERS 70). FLAGS cevapları ve teşhis:
> ders çıkarımı bu dosyanın altındaki koşu değerlendirmesinde DEĞİL,
> `../../LESSONS_LEARNED.md` DERS 70-71'dedir.

---

```
MATERIAL MODE: B full 48s cut
INPUT MODE: V — video-only
BASELINE: SELF-CONSISTENCY + PHYSICS + SERIES RULES (V)
FILM: (not supplied)
FORMAT: dikey shorts (9:16)
SCENE: ALL (S0-S6, using custom numbering as duration is 1:04)
CLIP DURATION: actual 64s
GENERATION MODE: (not supplied)
SOURCE DOCUMENT: (not supplied) — mode V
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  14
SUM OF SCORES:      84.0
DIVISION:           84.0 ÷ 14 = 6.0

OVERALL SCORE: 6/10
VERDICT: REGENERATE

THE FILM IN ONE SENTENCE
An astronaut finds herself stranded on a prehistoric planet alongside
giant sauropods. The visual premise is transmitted clearly, but
continuity errors and a title card break the format.

SCORES SUMMARY
Category    Score    Critical Issues
Character    6/10    S5 @ 0:50 dirt and wear pop onto face/suit abruptly.
Scale & Physics    6/10    S3/S4 capsule scale fluctuates compared to character.
Camera    7/10    Mostly stable with acceptable motion.
Lighting    6/10    General atmospheric haze holds, but shadow angles shift across cuts.
Environment    6/10    Flora types swap between shots (S1 vs S2).
Creatures    5/10    S0 @ 0:02 gait sliding; S3 @ 0:25 neck/tail morphing.
Particles & Materials    5/10    S4 @ 0:43 dust kicks up but behaves somewhat liquidly.
Dialogue & Audio    N/A    Silent by observation.
Vertical Format (9:16)    7/10    Framing utilizes vertical space adequately.
Safe Zone    7/10    Primary subjects remain mostly clear of UI areas.
Hook Timing    6/10    S0 @ 0:00 anomaly is revealed immediately; no curiosity gap.
Negative Violations    1 count    🔴 BLOCKER: Title card presented at 1:00.
Cross-Scene Logic    5/10    S2 capsule is absent, S3 capsule appears suddenly.
Story & Transmission    7/10    Basic survival/time-lost concept lands well.
Retention    6/10    Pacing is slow, visuals carry the weight.
Music & Sound    5/10    Ambient track present, lacking diegetic foley/sync points.

STEP 0.7 — INPUT MODE V BASELINE
MATERIAL
Clips given: 1 joined cut (7 segments) · duration 64s
Aspect ratio: 9:16 · Cuts inside any single clip: None

THE CHARACTER
Face / hair / marks: Female, dark hair under helmet.
Wardrobe: Orange suit, white boots, white helmet.
Wear & dirt: Clean initially. First clear frame: S1 @ 0:11.
Hands: Empty.

THE WORLD
Location(s): Misty prehistoric jungle.
Gravity read: ~1g.
Atmosphere read: Dense, hazy.
Sky/light direction and colour: Soft sunlight, hazy sky.
The central impossible thing: Modern astronaut amidst dinosaurs.

PROGRESSION
Dirt: S0-S3 (NONE) -> S4-S5 (HEAVY).
Damage: Capsule introduced midway.

🚩 FLAGS FOR DOCUMENT CHECK (Unverifiable in Mode V)
Novum intent: Was the capsule intended to be missing in earlier shots?

Timing: The sequence totals 64 seconds, exceeding the standard 48s limit.

Audio: Should there be foley for the dinosaur footsteps?
```
