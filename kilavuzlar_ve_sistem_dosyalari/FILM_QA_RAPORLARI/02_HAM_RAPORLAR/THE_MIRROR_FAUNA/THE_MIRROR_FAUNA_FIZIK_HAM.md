# ⚖️ THE_MIRROR_FAUNA — T6 FİZİK QA HAM RAPORU

> **Kaynak:** ⑥ Fizik mercek · MOD D · 09.09.2026  
> **Ham rapor — dokunulmaz.** Analiz: `01_FILM_RAPORLARI/THE_MIRROR_FAUNA.md`

---

INPUT MODE: D
FILM: THE_MIRROR_FAUNA
RUNTIME: 02:44 measured
GRAVITY: 0.7g
PREMISE REGISTER: TRAPPIST-1e Biyo-ışıldayan Taklitçi Fauna

ARITHMETIC GATE
SCORED CATEGORIES:  5
SUM OF SCORES:      27.0
DIVISION:           27.0 ÷ 5 = 5.4

OVERALL SCORE: 5.4/10
VERDICT: TWO GRAVITIES

PHYSICS LEDGER:
| # | Timecode | Event | Duration | Distance | Implied g | Consistent? |
| L1 | 0:00 | Walking | 10.0s | ~5m | ~0.7-1.0g | ✅ 0.7g |
| L2 | 1:12 | Sparks from laser | 8.0s | ~1.5m | ~0g | ⛔ Cinematic float |
| L3 | 1:50 | Astronaut falls back | 1.2s | ~1m | ~0.14g | ⛔ FAIL |
| L4 | 2:00 | Duplicate fall | 1.2s | ~1m | ~0.14g | ⛔ FAIL |
| L5 | 2:10 | Smoke vents helmet | 10.0s | ~1m | Normal drift | ✅ atm. |
| L6 | 2:30 | Walking | 10.0s | ~5m | ~0.7-1.0g | ✅ 0.7g |

NUMERIC LOCK VERIFICATION:
| GRAVITY | 0.7g | ~0.14g @ 1:50 | 0.56g | FAIL (L3) |

SCORES SUMMARY:
| 1 | Gravity & Free Fall | 3/10 | -7 · L3 (1:50) |
| 3 | Impact & Momentum | 6/10 | -4 · L3 (1:50) |
| 5 | Particles & Atmosphere | 5/10 | -5 · L2 (1:12) |
| 8 | Light & Shadow Physics | 7/10 | -3 · L1 (0:00) |
| 9 | Human Biomechanics | 6/10 | -4 · L3 (1:50) |

SEVERITY TALLY: 🔴 BLOCKER: 1  🟠 MAJOR: 3  🟡 MINOR: 1

THE THREE THAT MATTER:
1. 1:50 Fall (Cinematic Float): ~1m drop in 1.2s → 0.14g vs 0.7g lock. Fix: Speed-ramp 200%.
2. Eternal Particles (1:12): sparks freeze in air. Fix: Regenerate with gravity on particulates.
3. Rigid Body Landing (1:50): no reflex arm flail, no joint shock. Fix: Regenerate.

FLAGS FOR DOCUMENT CHECK:
- 1:50 fall: deliberate cinematic slow-motion or model failure?
