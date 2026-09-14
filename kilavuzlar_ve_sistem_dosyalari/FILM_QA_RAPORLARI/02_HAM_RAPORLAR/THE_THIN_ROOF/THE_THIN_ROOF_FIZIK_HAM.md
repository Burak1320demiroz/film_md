# THE THIN ROOF — ⑥ FİZİK QA · HAM RAPOR (derin tarama)

> Model çıktısı, OLDUĞU GİBİ (kural ④). Düzeltilmez, kısaltılmaz.
> Koşu: 28.08.2026 · rubrik `6_FIZIK_QA_CRITIQUE_PROMPT.md` · MOD V
> ⛔ SPEC'in D BLOĞU (24 satırlık KİLİT LİSTESİ) mevcuttu ve VERİLMEDİ → mod V.
> ⛔ Rapor 24 fps varsaydı; master 30 fps'tir → türetilen her süre %25 hatalıdır.
>    Ayrıntı: `01_FILM_RAPORLARI/THE_THIN_ROOF.md` §ÖLÇÜM KAPISI

---

INPUT MODE: V
FILM: the thın roof.mp4
RUNTIME: 1:04 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 6 · CUTS COUNTED: 5
NON-SCENE MATERIAL: 1:00-1:04 title card
LINES HEARD: none — no audio information at all
GRAVITY: ~1.5 - 2.5 m/s² (low gravity) ± spread, based on L1 (walking cadence) and L4 (push-up momentum)
PREMISE REGISTER:
- Low gravity environment (established by movement speed and dust settling).
- Anomalous localized zero-gravity or anti-gravity (established by spherical stones floating at 0:40).

ARITHMETIC GATE
SCORED CATEGORIES:  3
SUM OF SCORES:      19.0
DIVISION:           19.0 ÷ 3 = 6.3

OVERALL SCORE: 6.3/10
VERDICT: INCONSISTENT WORLD

## PHYSICS LEDGER

| # | Timecode | Event | Duration | Distance (est. + RULER) | Implied value | Consistent with? |
|---|---|---|---|---|---|---|
| L1 | 0:02-0:06 | Character walks 3 steps | 4.0s | ~2.5m (stride length) | ~0.6 m/s walk speed | Low gravity (slow, floating steps) |
| L2 | 0:10-0:15 | Character kneels | 5.0s | ~1.0m (waist to ground) | ~0.2 m/s descent | Low gravity |
| L3 | 0:40-0:50 | Stones levitate | 10.0s | ~1.5m (chest height) | ~0.15 m/s rise | Premise (Anti-gravity anomaly) |
| L4 | 0:50-0:55 | Character pushes up | 5.0s | ~1.0m (ground to stand) | ~0.2 m/s ascent | Low gravity |
| L5 | 0:52 | Minor dust kicks up | 3.0s | ~0.3m (boot height) | ~0.1 m/s settle | Low gravity |

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
|---|---|---|---|
| 1 | Gravity & Free Fall | N/A | no free fall events observed |
| 2 | Ballistics & Trajectories | N/A | no ballistic events observed |
| 3 | Impact & Momentum | N/A | no impacts observed |
| 4 | Material Behaviour | — | no in-scope source |
| 5 | Particles & Atmosphere | 5/10 | −5 · L3 (0:40) - stones hang without momentum |
| 6 | Scale & Measurement | — | no in-scope source |
| 7 | Rates & Timing | 8/10 | −2 · L1 vs L4 - minor cadence mismatch |
| 8 | Light & Shadow Physics | 6/10 | −4 · 0:30 - multiple conflicting shadow directions on suit |
| 9 | Human Biomechanics | N/A | walking is stylized low-g, biomechanics unmeasurable |

## PRESENCE STRING
111111

## SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 2

## GRAVITY TABLE
| Ledger row | Timecode | Height | Time | Implied g | vs film's g |
|---|---|---|---|---|---|
| none | N/A | N/A | N/A | N/A | N/A |

## RATE TABLE
| Rate | First measure | Second measure | Verdict |
|---|---|---|---|
| Walking/moving cadence | 0:02 (L1) - ~0.6 m/s | 0:50 (L4) - ~0.2 m/s | Passable (different actions, but consistent low-g feel) |

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
|---|---|---|---|---|
| L3 | 0:40-0:50 | 5 | Stones levitate (premise) but then freeze completely without continuous momentum, acting as static 2D objects rather than objects in zero-g. | 🟠 MAJOR |
| N/A | 0:30 | 8 | The key light is from the upper right, but the character's suit shows soft shadows on the right side and harsh shadows on the left, implying conflicting light sources. | 🟡 MINOR |
| L1, L4 | 0:02, 0:50 | 7 | The character's upward push in L4 is slightly too fast for the extreme slow-motion walking established in L1. | 🟡 MINOR |

## THE THREE THAT MATTER
1. Frozen zero-g (0:40) — The stones levitate (which is fine as a premise) but then hang perfectly static. Real zero-g requires continuous momentum; static floating looks like a video game glitch. Fix: Regenerate to show continuous slow drift.
2. Conflicting shadows (0:30) — The close-up shot ignores the established sun direction, lighting the character from multiple unmotivated angles. Fix: Accept it (minor issue).
3. Push-up speed (0:50) — The push-up is slightly too snappy compared to the lunar-style walking at the beginning. Fix: Trim the shot or slow down the clip by 15%.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Static floating stones | Regenerate scene | High |
| Shadow conflict in close-up | Accept it | None |
| Push-up speed mismatch | Speed ramp / slow down the clip | Low |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Stones hovering at 0:40 | Does the plan call for the stones to freeze in mid-air, or should they be drifting continuously? |
| Extremely slow walking at 0:02 | Is the gravity on this planet explicitly stated as lunar (approx 1.6 m/s²), or is this just cinematic slow motion? |

## OUT-OF-SCOPE FLAGS
0:30 — Twin faces clipping through each other → the FRAME / CONTINUITY lens.
0:50 — Morphing terrain artifacts → the FRAME / BACKGROUND lens.
