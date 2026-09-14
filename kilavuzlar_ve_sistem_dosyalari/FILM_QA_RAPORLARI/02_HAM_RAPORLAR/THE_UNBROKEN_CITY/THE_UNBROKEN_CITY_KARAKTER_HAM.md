# THE UNBROKEN CITY — KARAKTER HAM RAPOR (KARAKTER_QA · yalnız video)
> Kayıt: 06.08.2026 · model çıktısı olduğu gibi, düzenlenmedi.

FILM: (not supplied)
RUNTIME: 02:45 · SCENES OBSERVED: 8 · CHARACTERS TRACKED: 1
BASELINE: SELF-CONSISTENCY — this review measures whether each character
agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 8/10
VERDICT: DRIFTS BUT RECOVERABLE

CHARACTER PASSPORT(S)
Label:            "the astronaut"
First clear view: Scene 1, 00:10
Face:             Female adult, dark brown/black hair pulled back into a tight low ponytail, clean-shaven, neutral expression, visible through a clear curved glass visor.
Hair:             Dark brown/black, tied back in a low ponytail/bun structure.
Eyes:             Dark-toned, visible through glass bubble helmet.
Build:            Medium female adult build, standard proportions for a suited operator.
Costume:          Dark grey/charcoal full-body spacesuit with ribbed elastic articulation zones on limbs, ribbed boots, dark gloves, dark hard-shell chest pack/harness with dual straps, teal/cyan accent piping along the side torso and sleeves.
Equipment:        Clear bubble helmet with rear backpack life support unit, optional headlamp attachment in later scenes, dark gloves.
Wear map:         Clean throughout most scenes, light dust accumulation on boots during walking shots.
Voice:            Silent (no dialogue).

APPEARANCE TABLE
S1 00:00-00:10 Yes (profile/back) Standing on plain, looking at wall.
S2 00:10-00:40 Yes Walking on sand, suit clean, kicking up dust.
S3 00:40-00:50 Yes Examining pots in dark stone cell.
S4 00:50-01:20 Yes Walking mega corridor, looking out deep window.
S5 01:20-01:40 Yes Inspecting wall chain with headlamp active.
S6 01:40-02:00 Yes Kneeling at pottery table in shaft light.
S7 02:00-02:20 Yes Walking back across exterior plain.
S8 02:20-02:45 Yes Climbing ship ladder and departing.

SCORES SUMMARY
Facial Identity    9/10    Face structure and facial features remain remarkably stable across scenes.
Hair, Build & Proportions    9/10    Ponytail, height, and overall bodily proportions stay consistent.
Costume Identity    8/10    Teal piping and harness layout remain consistent; minor AI rendering shifts in panel stitching.
Wear, Damage & Injury    8/10    Suit remains clean; dust accumulates on boots during walks but lacks progressive permanent scuff accumulation.
Equipment State    9/10    Helmet, chest pack, and headlamp configuration match across continuous sequences.
Cross-Cut Action    8/10    Directional momentum on walking tracks matches reasonably well across cuts.
Count & Separation    N/A    Single character film; no multi-character separation or duplicates tracked.
Voice & Performance    N/A    Fully silent film.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 2

IDENTITY DRIFT MAP — per character
| The astronaut | Suit panel details & chest box straps | 00:40 | 01:40 | Partial (AI generation variance between indoor and outdoor shots) |

WEAR TIMELINE — per tracked mark
| Dust on boots | 00:15 (walking) | 00:15, 02:10 | Present during outdoor walks, absent indoors (wiped clean by floor transition - plausible) | Yes |

CONTRADICTION LOG
| 00:35 | 01:10 | The astronaut | Costume Identity | The small chest control panel/box straps shift slightly in height and width relative to the collar line between the exterior walk and the interior mega-corridor shot. | 🟡 MINOR |
| 01:30 | 02:00 | The astronaut | Equipment State | The headlamp accessory mounted on the top rim of the helmet is present and lit during corridor sequences, but the precise positioning of its mounting bracket fluctuates slightly between cuts. | 🟡 MINOR |

THE THREE THAT MATTER
Chest Harness Minor Drift (00:35 vs 01:10): The hard chest-pack harness geometry shifts slightly between generative shots, though the color palette and material remain identical. Fix: Accept as normal AI generation variance.
Helmet Headlamp Fluctuation (01:30 vs 02:00): The lighting and exact bracket position of the helmet-mounted light change subtly across interior cuts. Fix: Accept as minor continuity drift.
Purity of Suit Wear (00:15 vs 02:00): Despite walking across dusty exterior plains multiple times, the suit fabric itself never accumulates permanent dust stains or wear patterns. Fix: Add weathering consistency prompts in future generations.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Chest harness proportion micro-shifts | Accept as inherent to AI model consistency | Zero |

FLAGS FOR DOCUMENT CHECK
The character is never named or spoken to on screen — does the plan document designate a specific name or background for the astronaut?    What is the official name and narrative designation of the protagonist in the character bible?

OUT-OF-SCOPE FLAGS
Video QA: In-shot facial morphing and hand-surface contact distortions occur during close-ups (see VIDEO_QA report).
Mantik QA: Exterior lighting shifts rapidly relative to the short elapsed walking time (see MANTIK_QA report).
