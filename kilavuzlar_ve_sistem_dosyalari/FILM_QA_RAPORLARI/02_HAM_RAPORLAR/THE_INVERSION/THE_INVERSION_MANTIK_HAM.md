# THE INVERSION — MANTIK VE DEVAMLILIK QA · HAM RAPOR

```
QA TARİHİ:     31 Temmuz 2026
QA MODELİ:     Gemini (video analiz)
QA PROMPTU:    QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md
GİRDİ:         tam kurgu · 02:46 · yalnızca video (rubrik gereği doküman yok)
SPEC BLOĞU:    YOK — bu rubrik SPEC istemez, taban çizgisini videodan kurar
BASELINE:      SELF-CONSISTENCY
```

> ⚠️ Değiştirilmedi, düzeltilmedi, kısaltılmadı. Doğrulama ve plan
> karşılaştırması `../01_FILM_RAPORLARI/THE_INVERSION.md` içindedir.

---

FILM: The Inversion
RUNTIME: 02:46 · SCENES OBSERVED: 18
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees with itself, not whether it matches its design.

OVERALL SCORE: 3/10
VERDICT: STRUCTURAL PROBLEM
(The edit contains a duplicated 40-second block of footage, multiple teleporting helmet state changes without transitions, and an erratic gravity state that flips back and forth multiple times despite a stated 9-hour cycle.)

---

## SCENE INVENTORY

| # | In-out | Location | Present | What happens | Dialogue |
| --- | --- | --- | --- | --- | --- |
| S1 | 0:00–0:05 | Lander Ramp | Explorer | Exits spaceship, walks down ramp onto surface | None |
| S2 | 0:06–0:15 | Red Plain | Explorer | Kneels to touch lifting pebble; gravity wave approaches | None |
| S3 | 0:16–0:25 | Beetle Field | Explorer | Runs alongside alien beetles; attaches anchor cable to rock | None |
| S4 | 0:26–0:35 | Anchor Rock | Explorer | Anchors suit to black rock as gravity inversion hits | None |
| S5 | 0:36–0:45 | Mudbed | None | Water droplets pool and lift upward into zero-G spheres | None |
| S6 | 0:46–0:55 | Sky / Mid-Air | Explorer | Suspended upside-down on tether amidst floating debris | None |
| S7 | 0:56–1:05 | Debris Field | Explorer, Manta Rays | Floats on cable as giant sky-rays glide past | None |
| S8 | 1:06–1:15 | Debris Field | Explorer, Manta Rays | Hair floats loose in zero-G; pulls cable tether | None |
| S9 | 1:16–1:25 | Mudbed | None | **DUPLICATE OF S5:** Water droplets lift into zero-G | None |
| S10 | 1:26–1:35 | Sky / Mid-Air | Explorer | **DUPLICATE OF S6:** Suspended upside-down on tether | None |
| S11 | 1:36–1:45 | Debris Field | Explorer, Manta Rays | **DUPLICATE OF S7:** Sky-rays glide past floating explorer | None |
| S12 | 1:46–1:55 | Debris Field | Explorer, Manta Rays | **DUPLICATE OF S8:** Pulls cable tether near sky-rays | None |
| S13 | 1:56–2:01 | High Orbit / Debris | Explorer | Floats inside a perfectly symmetrical ring of asteroids | None |
| S14 | 2:02–2:11 | Rock Ridge | Explorer | Checks wrist interface; gravity restores, rocks crash down | None |
| S15 | 2:12–2:21 | Rock Ridge | Explorer, Bird Swarm | UI text appears; zero-G vortex of birds and rocks encircles her | None |
| S16 | 2:22–2:31 | Rock Ridge | Explorer, Manta Ray | Gravity restores again; debris smashes into terrain | None |
| S17 | 2:32–2:41 | Red Plain | Explorer | Unlatches and removes helmet ring; checks wrist HUD | None |
| S18 | 2:42–2:46 | Title Screen | None | Text overlay: "EVERY 9 HOURS, GRAVITY TURNS AGAINST US." | None |

---

## SCORES SUMMARY

| Category | Score | Critical Issue |
| --- | --- | --- |
| Physical Consistency | 3/10 | Gravity state fluctuates rapidly back and forth across scenes |
| Counter Logic | 2/10 | Inversion cycle flips 3 times in 2.5 minutes (contradicts 9-hour title) |
| Spatial Geography | 4/10 | Terrain jumps between flat desert, muddy puddle, and high cliffs |
| Time & Light Logic | 2/10 | Identical 40-second shot sequence is repeated back-to-back (1:16–1:55) |
| State, Costume & Props | 2/10 | Helmet toggles between ON, OFF, and MISSING VISOR without transitions |
| Causality & Knowledge | 4/10 | Anchor winch vanishes and re-attaches across scene changes |
| Quantity Consistency | 5/10 | Stated 9-hour cycle time vs observed 30-second inversion intervals |
| Setup & Abandonment | 5/10 | Beetle swarm (0:16) and HUD text callouts (2:12) appear once and vanish |

---

## SEVERITY TALLY

🔴 **BLOCKER:** 3     🟠 **MAJOR:** 4     🟡 **MINOR:** 2

---

## COUNTER CURVE

**Observed Gravity State:**
`S1 (1G Normal) → S2 (0G Inversion onset) → S3 (1G Normal running) ⚠️ → S4–S13 (0G Zero-Gravity) → S14 (1G Gravity restored) → S15 (0G Zero-Gravity vortex) ⚠️ → S16 (1G Gravity restored) ⚠️ → S17 (1G Normal)`

---

## LOCATION MAP

| Location | Scenes | Consistent? | Mismatch |
| --- | --- | --- | --- |
| Lander Drop Site | S1, S17 | No | Lander spacecraft present in S1, missing from horizon in S17 |
| Red Plain / Energy Wall | S2, S3, S4 | No | S3 shows flat desert with beetles; S4 instantly shows giant cliff rock |
| Mudbed Puddle | S5, S9 | Yes | Identical footage reused |
| Sky Debris Field | S6–S8, S10–S12, S13 | No | Background sky ring angle shifts 90 degrees between S12 and S13 |
| Rock Ridge Cliff | S14, S15, S16 | No | Terrain changes from bare black rock to dusty plateau |

---

## DRIFT MAP

| Element | First slip (timecode) | Undeniable by | Recovered? |
| --- | --- | --- | --- |
| Costume (Helmet) | 0:06 (ON head) | 0:16 (OFF head while running) | No (toggles continuously) |
| Sequence Timeline | 1:16 (Loop start) | 1:26 (Verbatim repeat of S6) | No (runs through 1:55) |
| Gravity Cycle | 2:02 (Gravity restores) | 2:12 (Gravity reverses again) | No |

---

## CONTRADICTION LOG

| Timecode A | Timecode B | Category | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| 0:06 | 0:16 | Costume | Helmet is fully sealed on head at 0:06; at 0:16 head is bare with hair in a bun, with no helmet held or carried | 🔴 BLOCKER |
| 0:16 | 0:26 | Costume | Bare head running at 0:16; helmet is instantly back on head at 0:26 bracing against rock | 🔴 BLOCKER |
| 0:36–1:15 | 1:16–1:55 | Timeline | Shots S5–S8 are replayed verbatim in S9–S12 (water drops, floating tether, ray flyby), resetting the timeline | 🔴 BLOCKER |
| 1:06 | 1:11 | Costume | At 1:06 visor/glass is missing and hair floats in zero-G; at 1:11 glass visor with blue rim light is intact | 🟠 MAJOR |
| 2:02 | 2:12 | Physical | Gravity restores at 2:02 (rocks fall, boots hit ground); at 2:12 zero-G returns instantly with floating rocks/birds | 🟠 MAJOR |
| 2:12 | 2:22 | Physical | Zero-G bird vortex at 2:12; at 2:22 gravity restores a second time with rocks crashing to earth | 🟠 MAJOR |
| 2:42 | 0:00–2:41 | Quantity | Title card states "Every 9 hours gravity turns against us", but gravity flips state 3 times within 160 seconds | 🟠 MAJOR |
| 0:23 | 2:32 | Props | Winch mechanism is mounted to left hip/rock at 0:23; vanishes entirely from suit harness at 2:32 | 🟡 MINOR |
| 0:00 | 2:32 | Atmosphere | Character walks outside without helmet at 0:00, wears helmet in space/zero-G, then removes helmet on surface at 2:32 | 🟡 MINOR |

---

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
| --- | --- | --- | --- |
| Beetle Swarm | 0:16 | No | Crawl on ground in 1G; never seen floating during zero-G inversions |
| Technical UI Text Overlay | 2:12 | No | "Dr. Kaya Uçan", "Anchor Stone" text overlay appears in S15 only |

---

## THE THREE THAT MATTER

1. **Duplicated 40-Second Video Loop (1:16–1:55):**
* *What it is:* Scenes 5–8 are copy-pasted directly into Scenes 9–12.
* *Why a viewer feels it:* It causes immediate confusion and breaks narrative progression, making the film feel like an unedited reel loop.
* *Fix:* Cut 1:16–1:55 entirely in the edit timeline.

2. **The Teleporting Helmet (0:06 vs 0:16 vs 0:26 vs 1:06):**
* *What it is:* The suit helmet vanishes and reappears between adjacent shots without the character putting it on or taking it off.
* *Why a viewer feels it:* It exposes the AI-generated nature of the footage and breaks physical continuity on an alien world.
* *Fix:* Re-order or trim shots so helmet removal/donning occurs only at explicit transition points.

3. **Erratic Gravity Flaps vs Stated Premise (2:02–2:31 vs 2:42):**
* *What it is:* Gravity restores at 2:02, reverses at 2:12, and restores again at 2:22.
* *Why a viewer feels it:* Contradicts the core tagline ("Every 9 Hours") established at the end of the film.
* *Fix:* Trim 2:12–2:21 (the bird vortex shot) so gravity restores once cleanly from 2:02 into 2:22.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Duplicated loop (1:16–1:55) | Ripple delete S9–S12 from edit timeline | 0 USD (1 minute edit) |
| Double gravity drop (2:12–2:21) | Cut S15 (bird vortex); bridge S14 directly to S16 | 0 USD (1 minute edit) |
| Visor disappearance (1:06) | Trim head-shot in S8, keep shot starting from 1:11 | 0 USD (30 sec edit) |
| Helmet toggle (0:16) | Regenerate S3 (running shot) with helmet prompt ON | Requires 1 clip regeneration |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Atmospheric breathable air | Is the planet's atmosphere breathable without a helmet? (Determines if S1/S3/S17 without helmet are valid) |
| Anchor tether mechanism | Is the tether cable designed to detach automatically when gravity restores? |

---

## OUT-OF-SCOPE FLAGS

* **VIDEO_QA:** Severe "jello" warping on running legs at 0:18; micro-droplets show heavy AI bloom at 0:38.
* **SENARYO_QA:** The character lacks an internal obstacle/choice; narrative mid-section plateaus due to static floating beats.
