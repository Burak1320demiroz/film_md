# YERÇEKİMİ FRAGMAN — ⑤ ARKA PLAN QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi: `/Users/dai/Downloads/gravıty ıt holds one fragman (1).mp4` · 145,00 s · 3840x2160 · 30 fps · AAC stereo
> model: Gemini (tek sohbet) · tarih: 04.09.2026 · MALZEME: **FRAGMAN** (film değil)
> ⛔ ③ KİMLİK KAPISI [D105]: bu rapor GERÇEKTEN bu fragmana koşulmuş — künyesindeki süre
>   (2:25) ve sahne sayısı (14) ölçümle birebir tutuyor.
> ⛔ ⑧ FRAGMAN MERCEK KAPISI [D111]: fragmanın merceği ① KARE’dir; bu rapor derin tarama
>   merceğidir, FİLM tablolarına (T1-T4) satır YAZILMAZ.

---

FILM: gravity.mp4
RUNTIME: 02:25 measured
SCENES OBSERVED: 14 · CUTS COUNTED: 13
NON-SCENE MATERIAL: 2:20-2:25 Title Card
SUBJECTS EXCLUDED:
S1 circular hatch on truss · S2 astronaut opening hatch · S3 two astronauts floating outside a module ·
S4 close-up of astronaut face in helmet · S5 astronaut holding orange railing · S6 astronaut climbing along truss ·
S7 close-up of distressed astronaut face · S8 astronaut floating backwards · S9 three tethered astronauts ·
S10 astronaut pressing button on wall panel · S11 close-up of astronaut face in interior · S12 hand pressing buttons ·
S13 hand turning a large dial · S14 astronaut sitting in capsule seat
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      55.0
DIVISION:           55.0 ÷ 6 = 9.1

OVERALL SCORE: 9.1/10
VERDICT: FIELD HOLDS

BACKGROUND INVENTORY
S1  MID: white truss · FAR: dense debris field streaming R→L; largest: Earth limb, lower left · SKY: black + stars · FOCUS: sharp hatch, soft debris · EDGES: Clean
S2  MID: white truss · FAR: Earth filling frame, dense cloud; largest: Earth, full frame · SKY: black at top · FOCUS: sharp · EDGES: Clean
S3  MID: white module exterior + handrails · FAR: Earth full frame · SKY: black top right · FOCUS: sharp · EDGES: Clean
S4  MID: orange cylindrical railing · FAR: Earth limb left, black right; largest: Earth limb, left half · FOCUS: sharp face, soft bg · EDGES: Clean
S5  MID: truss, Space Shuttle mid-distance · FAR: Earth limb bottom; largest: Earth, lower third · SKY: black + stars · EDGES: Clean
S6  MID: white truss + flying debris · FAR: Earth full frame · SKY: black top right · FOCUS: debris motion blurred · EDGES: Clean
S7  MID: orange railing · FAR: black space, stars, faint streaks; largest: space/stars full frame · EDGES: Clean
S8  MID: metal structure right edge · FAR: Earth limb bottom half · SKY: black + stars · EDGES: Clean
S9  MID: tethers connecting figures · FAR: Earth bottom half, sun on horizon left · SKY: black, sun flare · EDGES: Clean
S10 MID: padded interior walls, control panel · FAR: padded corridor right half · CEILING: panels with lights · EDGES: Clean
S11 MID: padded interior walls · FAR: padded walls full frame · CEILING: panels with lights · EDGES: Clean
S12 MID: console surface, illuminated buttons · FAR: more buttons, blurred · EDGES: Clean
S13 MID: dial + padded wall · FAR: padded wall full frame · EDGES: Clean
S14 MID: capsule interior, empty seats, hatch, window · FAR: Earth through window · CEILING: recessed lights · EDGES: Clean

SCORES SUMMARY
| 1 | Background Figure Integrity | N/A | no background figures |
| 2 | Background Figure Behaviour | N/A | no background figures |
| 3 | Crowd Count & Density | N/A | no crowds |
| 4 | Horizon & Topology | 10/10 | no deductions |
| 5 | Depth, Parallax & Scale | 7/10 | -3 · 0:51 (S6) |
| 6 | Background Set & Props | 8/10 | -2 · 0:00-0:10 (S1) |
| 7 | Focus Honesty | 10/10 | no deductions |
| 8 | Sky & Atmospherics | 10/10 | no deductions |
| 9 | Frame Edges & Emergent Artifacts | 10/10 | no deductions |

PRESENCE STRING
-1111111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 1

FIELD DRIFT MAP
| S1 | Midground | 0:02 | 0:05 | No |
| S6 | Midground | 0:51 | 0:51 | Yes (debris exits frame) |

COUNT LOG — (none)

CONTRADICTION LOG
| 0:51 | (in-shot) | Midground | 5 | A piece of flying debris passes through the solid geometry of the subject's arm rather than occluding or being occluded by it. | 🟠 MAJOR |
| 0:00 | 0:10 | Midground | 6 | The metallic texture on the flat top surface of the large circular hatch boils and swims as the camera pans. | 🟡 MINOR |

THE THREE THAT MATTER
1. Layering failure (0:51) — debris passes through the astronaut's arm. Fix: mask the particle in VFX.
2. Texture swimming (0:00-0:10) — the circular hatch texture boils as the camera moves. Fix: stabilise or regenerate.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Layering failure (0:51) | Mask out offending particle in VFX | Medium |
| Texture swimming (0:00) | Lock texture in post or regenerate | Medium |

FLAGS FOR DOCUMENT CHECK
| None | |

OUT-OF-SCOPE FLAGS
none
