# THE HEALING GROUND — ⑧ EFOR QA (HAM)


> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi: `/Users/dai/Downloads/the healıng ground.mp4` · 145,09 s · 1920x1080 · 30 fps · AAC
> model: Gemini (tek sohbet, yedi mercek arka arkaya) · tarih: 04.09.2026
> ⛔ SPEC KAPISI [D129]: SPEC ve PAKET_1..8 VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
---

INPUT MODE: V
FILM: (not supplied)
RUNTIME: ~02:25 ESTIMATED
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 14 · CUTS COUNTED: 13
NON-SCENE MATERIAL: 2:19-2:25 title card
PRESENCE STRING: 1111-111111111
LINES HEARD: 3
"The last one's gone under. Same as the others." (0:43)
"Whoever walks this line next, start from this end." (1:13)
"It'll hold once it's cold." (1:55)
EXERTION EVENTS: 3
EVENTS WITH NO STRAIN SHOWN: 2
BODY: suited human
PREMISE REGISTER:
· gravity / medium: ~1g (standard desert environment based on dust fall and walk cycle)
· what the body wears: heavy spacesuit with chest box, gloves, helmet
· declared capability: none (mode V)
· declared limits: none (mode V)
· is the body human?: yes

ARITHMETIC GATE
SCORED CATEGORIES:  5
SUM OF SCORES:      19.0
DIVISION:           19.0 ÷ 5 = 3.8

OVERALL SCORE: 3.8/10
VERDICT: WEIGHTLESS WORK

EFFORT LEDGER
| E1 | 0:00–0:09 | Kneeling, pressing metal disk into hard earth | Rigid sand/soil surface | 9s | torso, hands | none | 2 |
Bill test: Nothing. The arms push, but the shoulders do not lock and the body does not lean into the work.
| E2 | 1:29–1:39 | Pushing black rod deep into sand | Deep sand friction | 10s | hands | none | 3 |
Bill test: Nothing. The hand slides the rod down smoothly with no vibration, no grip readjustment, and no torso engagement.
| E3 | 2:09–2:19 | Kneeling with small dome, preparing to plant | Small payload | 10s | none | none | 2 |
Bill test: Nothing. The body holds the dome as a weightless prop.

PRESENCE STRING
1111-111111111

COST CURVE
22220222333332

RESET LOG
| S4–S5 | 2 → 0 | No (VO only scene) | Unclear | UNEARNED |
| S13–S14 | 3 → 2 | No | Unclear | UNEARNED |

SCORES SUMMARY
| # | Category | Score | Issue |
| 1 | Strain During the Work | 3/10 | -4 · E1 (0:00), -3 · E2 (1:29) |
| 2 | Breath & Recovery | 2/10 | -8 · E1 (0:00), E2 (1:29) |
| 3 | Fatigue Accumulation | 4/10 | -6 · Reset log S4-S5, S13-S14 |
| 4 | Load in the Body | 2/10 | -4 · E1 (0:00), -4 · E2 (1:29) |
| 5 | Injury Persistence & Cost | N/A | No injuries present |
| 6 | Grip & the Price of Holding On | 8/10 | -2 · E2 (1:29) |
| 7 | Equipment Burden | N/A | (Suit errors caught in CONTINUITY, no functional burden shown) |
| 8 | Pain, Restraint and Proportion | N/A | No pain events shown |
| 9 | Recovery Curve Honesty | N/A | No curve to measure, workload is minimal |

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 1

UNPAID WORK TABLE
| 0:00 | Pressing disk into hard earth | Shoulder lock, body weight transfer, braced core | ① EFFORTLESS HEAVY | 🟠 MAJOR |
| 1:29 | Pushing rod into sand | Forearm tension, micro-pauses, wrist adjustment | ① EFFORTLESS HEAVY | 🟠 MAJOR |
| 2:09 | Holding dome | Slight arm dip, posture adjustment for mass | ① EFFORTLESS HEAVY | 🟡 MINOR |

CONTRADICTION LOG
| 0:00 | 0:08 | The action of pushing the disk requires force, but the character's posture (upright, arms casually extended) contradicts the physical requirement of the task. | 🟠 MAJOR |

THE THREE THAT MATTER
0:00 (E1) — The opening action establishes the film's physical language. Pushing an object into the ground with extended, relaxed arms makes the world feel weightless.
1:29 (E2) — The rod slides into the sand like a knife through soft butter, with zero friction or grip adjustment.
Reset S4-S5 — The character's physical state vanishes entirely during the VO scene.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
REQUIRES REGENERATION: E1 (0:00) and E2 (1:29).
FIXABLE IN EDIT: The curve resets might be mitigated by adding subtle audio cues.

FLAGS FOR DOCUMENT CHECK
1:29 — Was the sand intended to be extremely loose/fluid, allowing the rod to slide easily, or is this an AI failure to render friction?

OUT-OF-SCOPE FLAGS
0:59 — Massive costume changes across cuts → CONTINUITY lens.
1:55 — Dialogue lip sync is extremely stiff → FRAME lens.
