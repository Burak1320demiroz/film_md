# 🧍 KARAKTER — PART 13 (segment koşusu — KARAKTER_DEVAMLILIK_QA rubriği)
> ⚠️ Operatör notu: tam-film rubriği tek 3:07'lik segmente koşuldu; skorlar
> segment-içi tutarlılıktır, depo tablolarına girmez.

FILM: (not supplied)
RUNTIME: 03:07 · SCENES OBSERVED: 3 · CHARACTERS TRACKED: 3
BASELINE: SELF-CONSISTENCY

OVERALL SCORE: 6.5/10
VERDICT: SAME PERSON THROUGHOUT

## CHARACTER PASSPORTS

CHARACTER 1: Male Driver / Expedition Lead
- First clear view: Scene 1, 00:10
- Face: Caucasian male, mid-30s, brown short beard/stubble, strong jawline.
- Hair: Dark brown, cropped short inside helmet.
- Eyes: Dark, visible through clear visor.
- Build: Athletic frame, masculine posture.
- Costume: White sci-fi composite armor, chest plate, shoulder guards, clear helmet visor.
- Equipment: Drives Mule 01 vehicle; holds assault rifle at compound.
- Wear map: Clean torso at 00:10; mud smudges acquired at 00:57 on chest and back.
- Voice: American accent, baritone, calm/commanding tone.
- EVIDENCE BASE: FACE-VISIBLE: 85 s of 187 s · 3 of 3 scenes · COSTUME-VISIBLE: 3 of 3 · MOUTH ON SCREEN: yes

CHARACTER 2: Female Scientist / Co-pilot
- First clear view: Scene 1, 00:10
- Face: Caucasian female, early-30s, fair skin, oval face structure.
- Hair: Dark brown, pulled back neatly inside helmet.
- Eyes: Dark brown/hazel.
- Build: Slender frame, average height.
- Costume: White sci-fi composite suit matching lead armor style.
- Equipment: Handheld scanner/gear, sidearm holster.
- Wear map: Clean at start; mud splatters on suit front acquired at 00:57.
- Voice: American accent, articulate, soft/obsessive cadence.
- EVIDENCE BASE: FACE-VISIBLE: 70 s of 187 s · 3 of 3 scenes · COSTUME-VISIBLE: 3 of 3 · MOUTH ON SCREEN: yes

CHARACTER 3: Heavy / Squad Member
- First clear view: Scene 2, 00:26
- Face: Black male, short buzzcut, light stubble beard.
- Hair: Black, closely shaved.
- Build: Broad, heavy frame.
- Costume: White heavy sci-fi armor with padded shoulders.
- Equipment: Tactical rifle.
- Wear map: Light dirt smudges on lower boots and shins.
- Voice: American accent, deep baritone.
- EVIDENCE BASE: FACE-VISIBLE: 25 s of 187 s · 2 of 3 scenes · COSTUME-VISIBLE: 2 of 3 · MOUTH ON SCREEN: yes

## APPEARANCE TABLE

| Character | Scene | Timecode in-out | Face visible? | State notes |
|---|---|---|---|---|
| Male Driver | S1–S3 | 00:00–03:07 | Yes | Clean suit S1; torso mud splatters S2–S3 |
| Female Scientist | S1–S3 | 00:00–03:07 | Yes | Clean suit S1; chest/shoulder mud S2–S3 |
| Heavy | S2–S3 | 00:26–03:07 | Yes | Armor intact; standing guard S3 |

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|---|---|
| Facial Identity | 6.8/10 | High face structure retention across visor views. |
| Hair, Build & Proportions | 6.7/10 | Body proportions remain stable across all cuts. |
| Costume Identity | 6.5/10 | Armor panels and seam placements hold consistency. |
| Wear, Damage & Injury | 6.2/10 | Mud from fall persists monotonically into later scenes. |
| Equipment State | 6.3/10 | Vehicle and rifle states remain stable. |
| Cross-Cut Action | 6.2/10 | Eyelines match well; slight motion jump during plant rescue. |
| Count & Separation | 6.8/10 | Squad count holds steadily between 3 and 4 members. |
| Voice & Performance | 6.5/10 | Pitch and accent registers remain consistent. |

## SEVERITY TALLY
🔴 BLOCKER: 0 · 🟠 MAJOR: 0 · 🟡 MINOR: 2

## IDENTITY DRIFT MAP
| Character | Element | First slip (timecode) | Undeniable by | Recovered? |
|---|---|---|---|---|
| Female Scientist | Suit mud density | 01:25 | 02:40 | Yes |
| Male Driver | Visor reflections | 02:00 | 02:05 | Yes |

## WEAR TIMELINE
| Mark | Acquired | Present at | Absent at ⚠️ | One-way? |
|---|---|---|---|---|
| Torso mud (Male Driver) | 00:57 | 01:10, 02:41 | None | Yes |
| Chest mud (Female Scientist) | 00:57 | 01:12, 02:41 | None | Yes |

## CONTRADICTION LOG
| Timecode A | Timecode B | Character | Category | What contradicts what | Severity |
|---|---|---|---|---|---|
| 00:57 | 01:25 | Female Scientist | Wear, Damage & Injury | Heavy mud coverage from fall at 00:57 appears slightly thinned by 01:25 | Minor |
| 00:28 | 01:33 | Male Driver | Equipment State | Rifle slung on back at 00:28 is held in hands at 01:33 without explicit draw shot | Minor |

## THE THREE THAT MATTER
1. Mud Density Shift across Cuts (00:57 vs 01:25): The mud splatters gained during the plant attack lighten slightly in subsequent shots. Fix: Standardize dirt overlays via color grading.
2. Implicit Weapon Transition (00:28 vs 01:33): The lead character transitions from slung rifle to held rifle without an on-screen draw action. Fix: Insert a brief unholstering cut.
3. Visor Lighting Variations (02:00 vs 02:05): Internal helmet visibility alters between dense canopy shade and open sunlight. Fix: Match interior helmet exposure in post-production.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Finding | Fix | Cost |
|---|---|---|
| Mud density variation | Apply dirt overlay pass in edit | Low |
| Weapon handling shift | Insert 1-second weapon draw shot | Low |

## FLAGS FOR DOCUMENT CHECK
| Observation | Question the document must answer |
|---|---|
| Fourth soldier appears at 02:40 | Does the official squad roster specify 3 or 4 operators? |

## OUT-OF-SCOPE FLAGS
- Background foliage motion flickering during vehicle travel → VIDEO_QA
- Automated turret mechanical housing feasibility → MANTIK_QA
