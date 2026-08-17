# 🌗 THE WRONG SHADOW — SHORTS_QA HAM ÇIKTI (06.08.2026)

> ⚠️ **DOKUNULMAZ.** Model çıktısı olduğu gibi, düzenlenmeden kaydedildi
> (AGENTS kural ④). Rubrik: `../../QA_PROMPTLARI/SHORTS_QA_CRITIQUE_PROMPT.md`
> · Koşu: **INPUT MODE V** (SPEC verilmedi) · MATERIAL MODE B iddiası.
>
> **Plan dosyası:** `dikey_shorts_filmler/THE_WRONG_SHADOW_DIKEY_SHORTS.md`
> — 835 satır, 6 sahne × 8 s = 48 s planı. Depoda duruyordu (MOD V koşusu
> geçerli; künye uydurulmadı, `FILM: (not supplied)` yazıldı ✅ Ders 60/65).
> Aritmetik kapı tuttu: 73.0 ÷ 13 = 5.6 ✅ [Ders 62].
>
> ⚠️ **Operatör teşhisi (rapora dokunmadan):** Rapor 64 s / 7 segment /
> ~10 s'lik sahneler ve sonda jenerik kartı ölçtü — plan 6 × 8 = 48 s,
> metin 0,0 sn der. DERS 70 ihlalinin İKİNCİ vakası (ilki The First
> Morning, aynı gün). Daha ağırı: raporun hiçbir satırında **çift gölge**
> geçmiyor — filmin novum'u (kaynaksız ikinci gölge seti) ekrana hiç
> girmemiş; dönme hareketi S5'te JALONLARIN kendisine transfer olmuş
> ("poles hovering horizontally and spinning"). Bkz. DERS 73. Belge
> cevapları: `../01_FILM_RAPORLARI/THE_WRONG_SHADOW.md`.

---

MATERIAL MODE: B full 48s cut
INPUT MODE: V — video-only
BASELINE: SELF-CONSISTENCY + PHYSICS + SERIES RULES (V)
FILM: (not supplied)
FORMAT: dikey shorts (9:16)
SCENE: S0-S5 (own numbering, 6 scenes + end title card)
GENERATION MODE: (not supplied)
SOURCE DOCUMENT: (not supplied) — mode V
SPEC BLOCK PROVIDED: no — mode V

ARITHMETIC GATE
SCORED CATEGORIES:  13
SUM OF SCORES:      73.0
DIVISION:           73.0 ÷ 13 = 5.6

OVERALL SCORE: 5.6/10
VERDICT: REGENERATE

THE FILM IN ONE SENTENCE
A man observes mysterious red-and-white poles in a barren desert over the course of a day, leading to inexplicable floating crosses and an abrupt title card.
The film transmits a vague sense of mystery regarding the poles, but the lack of a clear novum or escalation leaves the central idea unread.

SCORES SUMMARY

| Category | Score | Critical Issues |
|---|:--:|---|
| Character | 6/10 | Hand morphs into leg shadow; minor facial drifts |
| Scale & Physics | 4/10 | Floating poles break 1g gravity |
| Camera | 5/10 | Hidden cut inside S0 |
| Lighting | 6/10 | Shadow directions drift relative to sun |
| Environment | 5/10 | Static geometry violated by floating objects |
| Creatures | N/A | None present |
| Particles & Materials | 8/10 | Ground textures mostly stable |
| Dialogue & Audio | N/A | No dialogue |
| Vertical Format (9:16) | 9/10 | Strong vertical composition throughout |
| Safe Zone | 7/10 | S1 crouching action borders UI bottom band |
| Hook Timing | 5/10 | No curiosity gap; poles revealed at 0:00 |
| Negative Violations | 4 count | Title card, hidden cut, phasing, morphs |
| Cross-Scene Logic | 6/10 | Abrupt jump to dusk at S5 |
| Story & Transmission | 3/10 | Lacks escalation; novum illegible |
| Retention | 3/10 | High 0:03 drop-off; ends on title card |
| Music & Sound | 6/10 | Drone functional but lacks dynamic hits |

SCENE INVENTORY — INPUT MODE V only
MATERIAL
Clips given: 7 (6 scenes + 1 title card) · duration each ~10s · joined
Aspect ratio: 9:16 · Cuts inside any single clip: S0
THE CHARACTER
Face / hair / marks: Short brown hair, stubble. Wardrobe: Olive green field jacket over a dark t-shirt, olive pants, tan work boots, olive cap.
Wear & dirt: Light dust on boots. Equipment: None. Hands: Empty. First clear frame: S0 @ 0:00.0
THE WORLD
Location(s): Barren white-gravel desert under a clear blue sky. Red and white striped surveying poles planted in the ground.
Gravity read: 1g. Atmosphere read: Clear. Sky: Blue, transitioning abruptly to dusk.
The central impossible thing, if any: Poles hovering horizontally and spinning in the sky at dusk.
PROGRESSION
Time of day advances from bright noon to dusk (S5 @ 0:49).

SEVERITY TALLY
🔴 BLOCKER: 3    🟠 MAJOR: 2    🟡 MINOR: 2

PER-SCENE SPREAD

| Scene | Score | Worst category | One-line verdict |
|:--:|:--:|---|---|
| S0 | 5.0 | Camera | Hidden cut breaks single-take rule |
| S1 | 7.0 | Safe Zone | Crouching action risks UI overlap |
| S2 | 6.0 | Character | Minor facial bone structure drift |
| S3 | 5.0 | Character | Left hand melts into shadow/thigh |
| S4 | 6.0 | Lighting | Shadow placement contradicts previous scenes |
| S5 | 4.0 | Physics | Floating objects violate static geometry |
| S6 | 0.0 | Negative | Title card violates 0.0s screen-text rule |

Weakest scene: S6 (Title Card)
Strongest scene: S1

CHARACTER DRIFT TABLE

| Detail | As first seen (clip + tc) | Later state (clip + tc) | Drift? |
|---|---|---|---|
| Hand anatomy | S0 @ 0:00.0 | S3 @ 0:34.0 | Left hand morphs into shadow/leg. |
| Facial features | S1 @ 0:09.0 | S4 @ 0:41.0 | Bone structure widens, beard changes. |

PROGRESSION LADDER CHECK

| Scene | Observed state | Verdict |
|:--:|---|---|
| S0 | Midday | Pass |
| S1 | Midday | Pass |
| S2 | Midday | Pass |
| S3 | Midday | Pass |
| S4 | Midday | Pass |
| S5 | Dusk (Abrupt jump) | Fail (Jump instead of transition) |

TOP 3 CRITICAL ERRORS
1. S6 @ 0:59.0 — 🔴 BLOCKER — Negative Bible — A title card appears at the end of the cut, violating the 0.0s screen-text rule [Lesson 9, 34].
2. ALL @ 0:00.0 — 🔴 BLOCKER — 48-Second Assembly Rules — The total cut runs 64 seconds with 7 segments (10s scenes + title card), violating the strict 6-scene 48.0s (±0.5s) limit [Lesson 70].
3. S0 @ 0:04.0 — 🔴 BLOCKER — Single-Clip Integrity — A hard cut to the sky occurs inside what should be a continuous single-take scene [Lesson 1].

DETAILED ERROR LOG
S6 @ 0:59.0 — Negative Bible — Burned-in text — Title card "THE DEVIL'S DOUBLE" appears.
ALL @ 0:00.0 — Vertical Rules (E) — Assembly length is 64s instead of 48s. PERSISTENT
S0 @ 0:04.0 — Camera — Hidden cut/camera reset inside single clip.
S3 @ 0:34.0 — Character — Hand morphs into thigh/shadow.
S5 @ 0:50.0 — Environment — Static geometry fails as poles float in the sky.
S5 @ 0:49.0 — Cross-Scene Logic — Time of day jumps instantly to dusk.

CROSS-SCENE CONTRADICTION LOG

| Timecode A | Timecode B | What contradicts | Anchor | Drift | Lesson # |
|---|---|---|---|---|---|
| 0:39.0 | 0:49.0 | Time of day (Day → Dusk) | Anchor S4 | Drift S5 | 47 |
| 0:09.0 | 0:29.0 | Shadow direction relative to body | Anchor S1 | Drift S3 | 47 |

LESSON MATCH

| Timestamp | Lesson # | Lesson name |
|---|:---:|---|
| 0:04.0 | 1 | Hidden cuts / camera reset |
| 0:34.0 | 43 | Contact morph — hand or tool melts the surface |
| 0:49.0 | 47 | Light jump between scenes — day → night → sunset |
| 0:59.0 | 9, 34 | Text, gibberish display text, title card |
| 0:00.0 | 70 | Assembly length / Extra segments (NEW LESSON CANDIDATE) |

SHAREABLE MOMENT
S0 @ 0:00.0 — The initial framing of the man staring at the poles utilizes the vertical space well.

WHAT WORKED WELL
- The 9:16 framing is natively vertical, utilizing the top two-thirds for the sky and poles consistently.
- Wardrobe consistency is relatively stable across the assembly.

PROMPT UPDATE RECOMMENDATIONS

| Issue | Prompt section that caused it | Concrete change to make |
|---|---|---|
| Title card generation | NEGATIVE BIBLE | Add "0% text, no typography, no title cards, no credits" |
| Hidden cut in S0 | CAMERA | Add "single unbroken take, zero cuts" |
| Hand morphing | CHARACTER BIBLE | Add "hands remain distinct from body, rigid anatomy" |

QUALITY TABLE ROW
| Ⓥ [FILM: to be filed by operator] | ALL | 6.0 | 4.0 | 5.0 | 6.0 | 5.0 | 8.0 | 9.0 | 7.0 | 5.0 | 5.6/10 |

FLAGS FOR DOCUMENT CHECK
- ALL 0:00 — The cut runs 64 seconds with ~10s scenes plus a title card — does the document script 10s scenes or is this an edit failure?
- S5 0:50 — The poles float horizontally in the sky — is this the declared NOVUM or a physics failure?
- S6 0:59 — Title card appears — is this a DELIBERATE DEVIATION for distribution?
