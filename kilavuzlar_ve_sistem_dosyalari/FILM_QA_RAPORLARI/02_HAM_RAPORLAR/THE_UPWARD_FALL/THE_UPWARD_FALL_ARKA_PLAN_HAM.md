# THE UPWARD FALL — ⑤ ARKA PLAN QA (HAM)


> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi: `/Users/dai/Downloads/the upward fall (1).mp4` · 225,11 s · 3840x2160 · 30 fps · AAC 48 kHz stereo
> model: Gemini (tek sohbet, sekiz mercek arka arkaya) · tarih: 04.09.2026
> ⛔ SPEC KAPISI [D129]: `yatay_4_dk_filmler/THE_UPWARD_FALL/THE_UPWARD_FALL_QA_SPEC.md` VAR ve
>   paket `QA_PROMPTLARI/FILME_OZEL/THE_UPWARD_FALL/PAKET_*` VAR — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
---

FILM: THE UPWARD FALL
RUNTIME: 03:45 measured
SCENES OBSERVED: 21 · CUTS COUNTED: 21
NON-SCENE MATERIAL: 3:40–3:45 title card "THE UPWARD FALL"
SUBJECTS EXCLUDED: S1 kneeling astronaut · S2 standing astronaut looking up · S3 kneeling astronaut ·
S4 astronaut close-up · S5 standing astronaut holding cylinder · S6 glove holding shell · S7 standing astronaut ·
S8 astronaut walking away · S9 astronaut lifting flat rock · S10 astronaut lifting cylinder overhead ·
S11 standing astronaut looking up · S12 astronaut looking up · S13 kneeling astronaut · S14 glove tying vine ·
S15 astronaut looking up · S16 astronaut on log · S17 astronaut lifting cylinder mid-air · S18 astronaut holding cylinder ·
S19 glove cutting vine · S20 astronaut walking in ash · S21 sitting astronaut holding shell
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      46.0
DIVISION:           46.0 ÷ 9 = 5.1

OVERALL SCORE: 5.1/10
VERDICT: FIELD DRIFTS BUT RECOVERABLE

BACKGROUND INVENTORY (özet — ham çıktıda 21 sahnenin 21'i tek tek yazılı)
S1 [0:00–0:09] MID: 3 floating leaves · FAR: smooth grey tree trunks · SKY: none · FOCUS: subject sharp · EDGES: Clean
S2 [0:10–0:29] MID: ~10 floating leaves · FAR: smooth grey banyan-like trunks · EDGES: Clean
S3 [0:30–0:39] MID: 1 floating insectoid creature · FAR: smooth grey trunks · SKY: diffuse top light rays · EDGES: Clean
S4 [0:40–0:49] MID: 2 white figures on trees · FAR: dark forest trunks · EDGES: Minor blur on left frame line
S5 [0:50–0:59] MID: ~15 floating leaves · FAR: smooth grey trunks · EDGES: Clean
S6 [1:00–1:09] MID: thin ground straw/grass · FAR: dark blurred vertical trunks · EDGES: Clean
S7 [1:10–1:19] MID: ~40 floating white cloth strips · FAR: redwood tree trunks · EDGES: Clean
S8 [1:20–1:29] MID: ~12 floating leaves · FAR: smooth grey trunks · EDGES: Clean
S9 [1:30–1:39] MID: ~5 floating leaves · FAR: smooth grey trunks · EDGES: Clean
S10 [1:40–1:49] MID: floating flat rocks · FAR: smooth grey trunks · EDGES: Clean
S11 [1:50–1:59] MID: axe stuck in trunk right · FAR: towering redwood canopy · SKY: bright diffuse overcast · EDGES: Clean
S12 [2:00–2:09] MID: floating cylinder, white dead trunk · FAR: redwood trunks · EDGES: Clean
S13 [2:10–2:19] MID: mantis-like leg on right tree · FAR: redwood trunks · EDGES: Clean
S14 [2:20–2:29] MID: ground straw · FAR: blurred dark wall/base · EDGES: Clean
S15 [2:30–2:39] MID: floating rocks around central trunk · FAR: dense pine canopy · EDGES: Clean
S16 [2:40–2:49] MID: thick vines on log · FAR: twisted dark spooky forest · EDGES: Clean
S17 [2:50–2:59] MID: floating dark tentacle top right · FAR: redwood trunks · EDGES: Clean
S18 [3:00–3:09] MID: massive quadruped leg stepping on log · FAR: dark twisted forest · EDGES: Clean
S19 [3:10–3:19] MID: log bark · FAR: highly blurred dark background · EDGES: Clean
S20 [3:20–3:29] MID: dead white log on left · FAR: ash/snow covered terrain · SKY: overcast grey · EDGES: Clean
S21 [3:30–3:39] MID: large quadruped walking on log · FAR: pine forest, parked rover · EDGES: Clean

SCORES SUMMARY
| 1 | Background Figure Integrity | 6/10 | -4 · 0:40 (white figures hold silhouette but lack fine anatomy) |
| 2 | Background Figure Behaviour | 5/10 | -5 · 3:30 (quadruped slides slightly across log surface) |
| 3 | Crowd Count & Density | 6/10 | -4 · 1:10 (floating cloth density fluctuates mildly) |
| 4 | Horizon & Topology | 3/10 | -7 · 1:00 vs 1:10 (smooth banyan forest becomes redwood forest) |
| 5 | Depth, Parallax & Scale | 5/10 | -5 · 2:30 (canopy lacks parallax during subtle camera drift) |
| 6 | Background Set & Props | 4/10 | -6 · 1:50 vs 2:00 (axe in redwood disappears in subsequent redwood shot) |
| 7 | Focus Honesty | 5/10 | -5 · 1:00 (slight bokeh flicker in extreme macro field) |
| 8 | Sky & Atmospherics | 6/10 | -4 · 2:50 (fog density shifts mid-shot) |
| 9 | Frame Edges & Emergent Artifacts | 6/10 | -4 · 0:40 (minor edge blur on background figure left) |

PRESENCE STRING
111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 6

FIELD DRIFT MAP
| S7 | Far | 1:10 | 1:12 | Yes (S8) |
| S11 | Mid | 1:50 | 1:50 | No |
| S20 | Far | 3:20 | 3:20 | No |
| S21 | Mid | 3:30 | 3:33 | No |

COUNT LOG
| Floating leaves | S1,S2,S5,S8,S9 | ~3 | ~15 | Fluctuates across scenes |
| White figures | S4 | 2 | 2 | Holds |
| Cloth strips | S7 | ~40 | ~40 | Holds |

CONTRADICTION LOG
| 1:00 | 1:10 | Far | 4 | Smooth banyan trunks become textured redwoods | 🟠 MAJOR |
| 1:50 | 2:00 | Mid | 6 | Axe lodged in trunk disappears in identical environment | 🟠 MAJOR |
| 3:20 | 3:30 | Far | 4 | Ash/snow flatland becomes deep pine forest valley | 🟠 MAJOR |
| 3:30 | 3:38 | Mid | 2 | Quadruped slides rather than stepping | 🟡 MINOR |

THE THREE THAT MATTER
1. Topology volatility (1:00 vs 1:10). Fix: regenerate S7 or S8 to match.
2. Missing props (1:50 vs 2:00). Fix: crop out the upper right quadrant of 1:50.
3. Sliding walk cycle (3:30). Fix: trim shot before the slide becomes obvious.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Topology changes | Regenerate out-of-place scenes | High |
| Disappearing axe (1:50) | Crop tighter or remove shot | Low |
| Sliding creature (3:30) | Re-cut/trim tail of shot | Low |

FLAGS FOR DOCUMENT CHECK
| The forest type cycles between smooth grey, redwood, and pine. | Does the narrative intend rapid teleportation across different biomes? |
| A rover appears parked in S21. | Is this rover established elsewhere in the pre-production plan? |

OUT-OF-SCOPE FLAGS
The astronaut's suit texture and geometry exhibit minor shifting across cuts (CONTINUITY lens).
