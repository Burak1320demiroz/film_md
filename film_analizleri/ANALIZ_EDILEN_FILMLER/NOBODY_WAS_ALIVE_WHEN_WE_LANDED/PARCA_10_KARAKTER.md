# 🧍 KARAKTER — PART 10 (segment koşusu — KARAKTER_DEVAMLILIK_QA rubriği)
> ⚠️ Operatör notu: rubrik TAM FİLM için yazılmıştır; burada tek 3:27'lik
> segmente koşuldu. Skorlar segment-içi tutarlılığı ölçer, depo skor
> tablolarına GİRMEZ (dış film analizi).

FILM: Adsız tasarım (20).mp4
RUNTIME: 03:27 · SCENES OBSERVED: 4 · CHARACTERS TRACKED: 2
BASELINE: SELF-CONSISTENCY — this review measures whether each character agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 7/10
VERDICT: SAME PERSON THROUGHOUT

## CHARACTER PASSPORT(S)

CHARACTER PASSPORT — 1
- Label: The Doctor
- First clear view: Scene 1, 00:00
- Face: Fair skin, prominent freckles across bridge of nose and cheeks, blue eyes, sharp cheekbones.
- Hair: Auburn/reddish-brown, styled in a low bun/updo.
- Eyes: Light blue.
- Build: Slender, average height, upright posture.
- Costume: Beige knit cardigan over dark charcoal top (00:00–02:04); dark grey shirt/jumpsuit (02:34). Messenger bag strap over left shoulder.
- Equipment: Hologram interface console, metal transport case, paper note.
- Wear map: Clean; no visible injuries.
- Voice: Calm, articulate, soft mid-register accent.
- EVIDENCE BASE: FACE-VISIBLE: 45 s of 207 s total · 3 of 4 scenes · COSTUME-VISIBLE: 4 of 4 · MOUTH ON SCREEN: yes

CHARACTER PASSPORT — 2
- Label: Scarred Man
- First clear view: Scene 1, 00:09
- Face: Square jaw, dark stubble, linear scar across right cheekbone under right eye.
- Hair: Dark brown/black, short cropped cut.
- Eyes: Dark brown/hazel.
- Build: Broad shoulders, athletic frame.
- Costume: Dark jacket over black crew-neck t-shirt.
- Equipment: None carried.
- Wear map: Scar on right cheekbone (00:15, 01:40, 03:24).
- Voice: Deep, low pitch, gravelly texture.
- EVIDENCE BASE: FACE-VISIBLE: 35 s of 207 s total · 3 of 4 scenes · COSTUME-VISIBLE: 3 of 4 · MOUTH ON SCREEN: yes

## APPEARANCE TABLE

| Character | Scene | Timecode in-out | Face visible? | State notes |
|---|---|---|---|---|
| The Doctor | 1 | 00:00–01:14 | Yes | Cardigan, bun, freckles clear around console |
| Scarred Man | 1 | 00:09–01:14 | Yes | Dark jacket, scar on right cheekbone visible |
| The Doctor | 2 | 01:14–02:04 | Yes | Cardigan, packing briefcase, note retrieved |
| Scarred Man | 2 | 01:14–02:04 | Yes | Dark jacket, dialogue with Doctor |
| The Doctor | 3 | 02:04–02:24 | No | Silhouette crossing bridge in dome |
| Scarred Man | 3 | 02:04–02:24 | No | Silhouette crossing bridge in dome |
| The Doctor | 4 | 02:24–02:42 | Yes | Off-screen cardigan removal; grey top, boots off |
| Scarred Man | 4 | 03:24–03:27 | Yes | Closed eyes in cryo pod; right cheek scar holds |

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|---|---|
| Facial Identity | 7/10 | High facial stability across scene boundaries. |
| Hair, Build & Proportions | 7/10 | Hairstyles and body frames remain consistent. |
| Costume Identity | 6/10 | Off-screen cardigan removal between Scene 2 and 4. |
| Wear, Damage & Injury | 7/10 | Scar location on right cheekbone remains fixed. |
| Equipment State | 7/10 | Briefcase latches and paper note handoffs held cleanly. |
| Cross-Cut Action | 6/10 | Eyelines and positions match across coverage cuts. |
| Count & Separation | 7/10 | 5 group members maintained across scenes. |
| Voice & Performance | 7/10 | Audio timbre and performance pitch remain stable. |

## SEVERITY TALLY
🔴 BLOCKER: 0 · 🟠 MAJOR: 0 · 🟡 MINOR: 1

## IDENTITY DRIFT MAP — per character
| Character | Element | First slip (timecode) | Undeniable by | Recovered? |
|---|---|---|---|---|
| The Doctor | Costume (cardigan) | 02:34 | 02:34 | Plausible transition for cryo stasis |

## WEAR TIMELINE — per tracked mark
| Mark | Acquired | Present at | Absent at ⚠️ | One-way? |
|---|---|---|---|---|
| Right cheek scar (Scarred Man) | Pre-existing (00:15) | 01:40, 03:24 | None | Yes |

## CONTRADICTION LOG
| Timecode A | Timecode B | Character | Category | What contradicts what | Severity |
|---|---|---|---|---|---|
| 01:54 | 02:34 | The Doctor | Costume Identity | Beige cardigan worn over grey top at 01:54; cardigan absent at 02:34 | MINOR |

## THE THREE THAT MATTER
1. Off-screen costume change (Doctor, 01:54 vs 02:34): Doctor sheds her cardigan between workshop and cryo chamber. Minor transition jump, though contextually justified by entering stasis. Fix: Insert 2-second shot of her shedding outer layer.
2. Cryo pod lighting shift (Scarred Man, 01:40 vs 03:24): Blue frost filter obscures facial structure inside pod, but right cheek scar remains identifiable. Fix: Accept as environmental lighting.
3. Bridge silhouette scale (Group, 02:04): Figures on bridge are distant silhouettes, limiting character-level tracking. Fix: Accept as wide shot.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Finding | Fix | Cost |
|---|---|---|
| Missing cardigan removal transition (01:54 → 02:34) | Insert quick coat-removal shot or trim cut | Minimal / Edit only |

## FLAGS FOR DOCUMENT CHECK
| Observation | Question the document must answer |
|---|---|
| Doctor wears grey shirt/jumpsuit in cryo pod (02:34) | Does the character bible specify standard-issue undergarments for cryo sleep? |

## OUT-OF-SCOPE FLAGS
- In-shot particle swimming in background hologram projection (00:24) → VIDEO_QA
- Colony reporting logic and 11-month timeline gap (00:42) → MANTIK_QA
