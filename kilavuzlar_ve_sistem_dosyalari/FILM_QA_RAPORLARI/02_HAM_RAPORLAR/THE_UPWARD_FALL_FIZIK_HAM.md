# THE UPWARD FALL — ⑥ FİZİK QA (HAM)


> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi: `/Users/dai/Downloads/the upward fall (1).mp4` · 225,11 s · 3840x2160 · 30 fps · AAC 48 kHz stereo
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 04.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_3_5_dk_filmler/THE_UPWARD_FALL/THE_UPWARD_FALL_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_UPWARD_FALL/PAKET_*` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
---

INPUT MODE: V
FILM: THE UPWARD FALL
RUNTIME: 03:45 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 21 · CUTS COUNTED: 21
NON-SCENE MATERIAL: 3:40–3:45 title card "THE UPWARD FALL"
LINES HEARD: none — nothing audible to me
GRAVITY: UPWARD g ≈ 0.2 - 0.8 m/s² ± 0.6 spread, events used L1, L2, L4, L6
PREMISE REGISTER:
· Inanimate/unrooted objects experience inverted gravity (falling upwards).
· Living entities (humans, creatures) experience downward gravity.

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      54.0
DIVISION:           54.0 ÷ 9 = 6.0

OVERALL SCORE: 6.0/10
VERDICT: TWO GRAVITIES

PHYSICS LEDGER
| L1 | 0:02–0:05 | Leaf rises ground→mid-chest | 3.0 s | ≈1.2 m (suit torso) | UP a ≈ 0.26 m/s² | Premise |
| L2 | 0:52–0:55 | Leaves rise in background | 3.0 s | ≈1.5 m (suit height) | UP a ≈ 0.33 m/s² | L1 |
| L3 | 1:02–1:06 | Shell released, rises out of frame | 4.0 s | ≈0.8 m (arm span) | UP a ≈ 0.10 m/s² | Inconsistent (too slow) |
| L4 | 1:11–1:14 | Cloth strips float upward | 3.0 s | ≈2.0 m | UP a ≈ 0.44 m/s² | Premise |
| L5 | 1:42–1:46 | Cylinder released overhead | 4.0 s | ≈1.5 m | UP a ≈ 0.19 m/s² | L1 |
| L6 | 2:31–2:36 | Boulders float into canopy | 5.0 s | ≈10.0 m (tree scale) | UP a ≈ 0.80 m/s² | Inconsistent (too fast) |
| L7 | 2:52–2:54 | Tossed cylinder keeps rising | 2.0 s | ≈2.0 m | constant v ≈ 1.0 m/s | NO ACCELERATION |
| L8 | 3:22–3:26 | Astronaut walking in ash | 4.0 s | ≈2.5 m stride | stride cycle 2.0 s | Superhuman slow float |
| L9 | 3:32–3:35 | Large creature steps on log | 3.0 s | ≈4.0 m (log width) | massless landing | Mass amnesia |

SCORES SUMMARY
| 1 | Gravity & Free Fall | 3/10 | -7 · L3, L6, L7 |
| 2 | Ballistics & Trajectories | 5/10 | -5 · L7 |
| 3 | Impact & Momentum | 6/10 | -4 · L9 |
| 4 | Material Behaviour | 6/10 | -4 · L4 |
| 5 | Particles & Atmosphere | 7/10 | -3 · L8 |
| 6 | Scale & Measurement | 8/10 | -2 · L5 vs L7 |
| 7 | Rates & Timing | 6/10 | -4 · L8 |
| 8 | Light & Shadow Physics | 7/10 | -3 · L4 |
| 9 | Human Biomechanics | 6/10 | -4 · L8 |

PRESENCE STRING
111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 3   🟡 MINOR: 5

GRAVITY TABLE
| L1 | 0:02 | 1.2 m | 3.0 s | 0.26 m/s² UP | Core |
| L3 | 1:02 | 0.8 m | 4.0 s | 0.10 m/s² UP | Too slow |
| L4 | 1:11 | 2.0 m | 3.0 s | 0.44 m/s² UP | High end |
| L6 | 2:31 | 10.0 m | 5.0 s | 0.80 m/s² UP | Out of bounds |
| L7 | 2:52 | 2.0 m | 2.0 s | N/A (linear v) | Drift / Zero a |

RATE TABLE
| Upward fall rate | 0:02 (0.26) | 2:31 (0.80) | DRIFTS |
| Astronaut stride | 1:20 (2.0 s) | 3:22 (2.0 s) | HOLDS |

CONTRADICTION LOG
| L1 vs L6 | 0:02 vs 2:31 | 1 | Upward acceleration triples floor→canopy | 🔴 BLOCKER |
| L5 vs L7 | 1:42 vs 2:52 | 1 | Accelerates in S10, drifts at constant velocity in S17 | 🟠 MAJOR |
| L8 vs L4 | 3:22 vs 1:11 | 7 | Real-time environment vs slow-motion biomechanics | 🟠 MAJOR |
| L8 | 3:22 | 5 | Kicked ash hangs neutrally, ignoring both directions | 🟡 MINOR |

THE THREE THAT MATTER
1. Multiple upward gravities (0:02 vs 2:31). Fix: regenerate S15.
2. Constant velocity drift (2:52). Fix: regenerate.
3. Cinematic float vs real-time (3:22). Fix: speed up the walking shots 1.5x.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Cinematic float stride | Speed ramp to 1.0-1.2 s gait | Low |
| Constant velocity cylinder (2:52) | Requires regeneration | High |
| Inconsistent upward g | Trim shots earlier | Low |

FLAGS FOR DOCUMENT CHECK
| The film contains no spoken dialogue or ambient audio. | Is the final render intended to be completely silent, or is an audio track missing? |
| The astronaut is heavy while loose objects fall upwards. | Does the plan dictate a mass-based threshold for inverted gravity, or is it strictly organic vs inorganic? |

OUT-OF-SCOPE FLAGS
The large creature slides slightly across the log surface rather than stepping (FRAME/BACKGROUND lens).
