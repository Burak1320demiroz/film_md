# ⑥ ⚖️ FİZİK — HAM RAPOR · THE LAST SPAN · 25.08.2026

> ⛔ Model çıktısı OLDUĞU GİBİ. Düzenlenmedi, kısaltılmadı [AGENTS kural ④].
> Köşeli parantezli `[!! ...]` notlar operatörün işaretleridir, modelin metni
> değildir; ham gövdeye dokunulmadı.
> İşleme ve geçerlilik kararı: `../01_FILM_RAPORLARI/THE_LAST_SPAN.md`

---

```
INPUT MODE: V
FILM: the last stand_2.mp4
RUNTIME: 1:54 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 11 · CUTS COUNTED: 10
NON-SCENE MATERIAL: 1:50-1:54 title card
LINES HEARD: none
GRAVITY: 2.3 to 4.6 m/s2 (sub-1g) +/- 2.3 spread, events used: L3 (hop down),
  L5 (figure collapse).
PREMISE REGISTER:
  - Human bodies have petrified into brittle, dry ash/dust structures that
    hold their shape until collapsing.
BASELINE: THE FILM AS SCREENED   [!! bu satır ④ HİKAYE'nin mod-V damgasıdır,
                                  ⑥'nin değil — D110 bulaşma izi]

ARITHMETIC GATE
SCORED CATEGORIES: 8 · SUM: 46.0 · DIVISION: 46.0 / 8 = 5.7
  [!! 46/8 = 5.75; rapor 5.7 yazdı — kesme, yuvarlama değil]
OVERALL SCORE: 5.7/10
VERDICT: TWO GRAVITIES

PHYSICS LEDGER
| # | Timecode | Event | Duration | Distance (est. + ruler) | Implied | Consistent with? |
| L1 | 0:10 (S2) | Step up onto car | ~1.0 s | ~0.5 m (car hood) | slowed kinetics | nothing (cinematic float) |
| L2 | 0:30 (S4) | Jump between cars | ~1.2 s | ~1.5 m (car gap) | sub-1g arc | L1, L3 |
| L3 | 0:50 (S6) | Hop down from roof | ~0.8 s | ~1.5 m (truck to ground) | g ~ 4.6 m/s2 | sub-1g environment |
| L4 | 0:59 (S7) | Climb onto trunk | ~1.5 s | ~0.8 m (trunk height) | slowed kinetics | L1, L2, L3 |
| L5 | 1:40 (S11) | Standing bodies collapse | ~1.2 s | ~1.7 m (human height) | g ~ 2.3 m/s2 | contradicts L3 |
| L6 | 1:45 (S11) | Dust cloud expands | ~5.0 s (holds frame) | ~3.0 m (road width) | constant rate | gas expansion physics |
| L7 | 0:10-1:18 | Carrying metal jerrycan | continuous | N/A | mass ~ 0 kg | visual prop volume |
| L8 | 1:33 (S10) | Woman jogging | ~2.0 s (stride) | ~3.5 m (lane dash) | ~1.7 m/s | 1g Earth biomechanics |

SCORES SUMMARY
| # | Category | Score | Critical Issue |
| 1 | Gravity & Free Fall | 2/10 | -8 · L3 (0:50), L5 (1:40) |
| 2 | Ballistics & Trajectories | N/A | no trajectories observed |
| 3 | Impact & Momentum | 4/10 | -6 · L7 (0:10-1:18) |
| 4 | Material Behaviour | 8/10 | -2 · L5 (1:40) |
| 5 | Particles & Atmosphere | 5/10 | -5 · L6 (1:45) |
| 6 | Scale & Measurement | 8/10 | -2 · L2 (0:30) |
| 7 | Rates & Timing | 7/10 | -3 · L1 (0:10), L8 (1:33) |
| 8 | Light & Shadow Physics | 9/10 | -1 · L8 (1:33) |
| 9 | Human Biomechanics | 3/10 | -7 · L7 (0:10-1:18), L8 (1:33) |

PRESENCE STRING
11111111111

SEVERITY TALLY
BLOCKER: 1 · MAJOR: 2 · MINOR: 1

GRAVITY TABLE
| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
| L3 | 0:50 | ~1.5 m (truck to ground) | 0.8 s | 4.6 m/s2 | upper bound (sub-1g) |
| L5 | 1:40 | ~1.7 m (standing adult) | 1.2 s | 2.3 m/s2 | contradicts L3 |

RATE TABLE
| Rate | First measure | Second measure | Verdict |
| Walk/jog stride | 1:18 (S9) | 1:33 (S10) | plausible acceleration |
| Dust expansion | 1:42 (S11) | 1:48 (S11) | consistent linear expansion |

CONTRADICTION LOG
| Ledger rows | Timecodes | Cat | What contradicts what | Sev |
| L3, L5 | 0:50, 1:40 | 1 | The hop down (0:50) implies g ~ 4.6 m/s2, while the collapsing bodies (1:40) fall much slower at g ~ 2.3 m/s2 (two gravities) | BLOCKER |
| L7, L8 | 0:10, 1:33 | 9 | The protagonist jogs and jumps with 1g body mechanics, completely ignoring the ~20 kg inertial mass of a metal jerrycan (massless handling) | MAJOR |
| L2, L8 | 0:30, 1:33 | 7 | The jumps (0:30) exhibit cinematic slow-motion float, while the jogging stride (1:33) runs in real time | MAJOR |
| L6 | 1:45 | 5 | The dust from the collapsing bodies expands but does not begin to settle downward, hovering indefinitely despite the visible gravity acting on the chunks | MINOR |

THE THREE THAT MATTER
1. Rolled Gravities (0:50 vs 1:40): the film's gravity fundamentally changes
   between scenes. The protagonist hops down relatively quickly, but the
   bodies collapse in dreamy slow motion. A viewer feels the physics engine
   breaking. Cheapest fix: speed-ramp S11 by ~140% to match the gravity of
   the earlier falls.
2. Massless Jerrycan (0:10-1:18): a full 20 L metal jerrycan weighs over
   20 kg, but the protagonist swings it effortlessly with one hand at arm's
   length while jumping gaps. It reads as a hollow plastic prop. Cheapest
   fix: accept it, as modifying the arm's counter-swing requires full
   regeneration.
3. Cinematic Float (0:30): the jumps between cars drift into slow motion,
   severing the film's gritty grounded aesthetic. Cheapest fix: trim the
   hang-time frames in the edit to restore a heavier 1g landing.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Finding | Fix | Cost |
| Two gravities (slow collapse) | Speed-ramp S11 in post | Low |
| Cinematic float on jumps | Trim mid-air frames in edit | Low |
| Massless jerrycan carrying | Regenerate S2-S8 with "heavy load" prompt | High |
| Dust refusing to settle | Add downward post-particle effect | Medium |

FLAGS FOR DOCUMENT CHECK
| Observation | Question the document must answer |
| The jumps and collapses imply sub-1g gravity (2.3-4.6 m/s2), but walking implies 1g | Does the plan state this takes place on a low-gravity planet, or is this an artifact of AI slow-motion generation? |
| The jerrycan is swung as if empty | Is the jerrycan supposed to be empty at the start of the film? |

OUT-OF-SCOPE FLAGS
1:18 - Jerrycan completely disappears from the character's hand across a cut.
  -> CONTINUITY lens.
1:02 - Jerrycan handle visibly fuses into the character's glove. -> FRAME lens.
```
