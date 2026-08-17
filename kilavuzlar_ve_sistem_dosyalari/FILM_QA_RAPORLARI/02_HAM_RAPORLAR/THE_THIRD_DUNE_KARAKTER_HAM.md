# THE THIRD DUNE — KARAKTER_QA HAM RAPOR

> **Tarih:** 11.08.2026 · **Rubrik:** `QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Mod:** V (rubrik zaten yalnız video) · **Malzeme:** 4:05 kurgu · 2 karakter
> ⛔ Model çıktısı olduğu gibi. Belge cevapları film kaydında.
> ⚠️ SES_QA koşusu geçersiz olduğu için 8. kategori `→🔊`'ye İNMEDİ, puanlandı.

---

```
INPUT MODE: V
BASELINE: SELF-CONSISTENCY
FILM: (not supplied)
RUNTIME: 04:05 · SCENES OBSERVED: 13 · CHARACTERS TRACKED: 2

OVERALL SCORE: 7/10
VERDICT: DRIFTS BUT RECOVERABLE
```

## CHARACTER PASSPORT(S)

```
CHARACTER PASSPORT — Female Astronaut
Label:            Female Astronaut
First clear view: S1, 0:10
Face:             Dark skin, dark hair, clean features, no visible scars.
Hair:             Dark, contained inside helmet.
Eyes:             Dark, not fully visible due to visor.
Build:            Average height, athletic frame.
Costume:          Tan spacesuit base. Light blue horizontal bands on upper arms
                  and chest harness. Grey ribbed joints.
Equipment:        Clear helmet (sealed). Light grey backpack.
Wear map:         Clean.
Voice:            Low, calm, female Turkish.

CHARACTER PASSPORT — Male Astronaut
Label:            Male Astronaut
First clear view: S1, 0:10
Face:             Light skin, prominent brown beard and mustache.
Hair:             Brown, contained inside helmet.
Eyes:             Unclear, obscured by reflections.
Build:            Slightly taller and broader than female.
Costume:          Tan spacesuit base. Purple horizontal bands on upper arms and
                  chest harness. Grey ribbed joints.
Equipment:        Clear helmet (sealed). Light grey backpack.
Wear map:         Clean.
Voice:            Mid-range, male Turkish.
```

## APPEARANCE TABLE

| Character | Scene | In-out | Face visible? | State notes |
|---|---|---|---|---|
| Female Astronaut | S1-S9, S12 | 0:00-3:20 | Yes (S1, S3, S5, S7) | Costume consistent. Heavy dirt acquired S8, completely lost S9. |
| Male Astronaut | S1-S8, S10, S12 | 0:00-3:20 | Yes (S1, S3, S5, S7, S8, S10) | Purple stripes vanish in S7, return S8. Dirt acquired S8, completely lost S10. |

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|---|---|
| Facial Identity | 9/10 | Holds identity well across varied lighting. |
| Hair, Build & Proportions | 9/10 | Consistent relative height and frame. |
| Costume Identity | 5/10 | Male's identifying purple stripes vanish entirely for one scene. |
| Wear, Damage & Injury | 3/10 | Massive dirt reset; both suits go from heavily caked to spotless. |
| Equipment State | 8/10 | Helmets stay sealed; handled items are consistent. |
| Cross-Cut Action | 6/10 | Frequent left/right screen swapping during walking sequences. |
| Count & Separation | 9/10 | Two distinct characters, no clones generated at airlock exit. |
| Voice & Performance | 9/10 | Voices are stable and match the physical bodies. |

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 2

## IDENTITY DRIFT MAP

| Character | Element | First slip | Undeniable by | Recovered? |
|---|---|---|---|---|
| Male Astronaut | Purple suit stripes | 2:10 | 2:14 | Yes, at 2:20 |
| Female Astronaut | Suit dirt accumulation | 2:40 | 2:45 | No, stays clean |
| Male Astronaut | Suit dirt accumulation | 2:50 | 2:55 | No, stays clean |

## WEAR TIMELINE

| Mark | Acquired | Present at | Absent at ⚠️ | One-way? |
|---|---|---|---|---|
| Heavy brown sand on suit (Both) | 2:20 | 2:29 | 2:40 | No (resets to clean) |

## CONTRADICTION LOG

| Timecode A | Timecode B | Character | Category | What contradicts what | Severity |
|---|---|---|---|---|---|
| 1:30 | 2:10 | Male Astronaut | Costume Identity | Purple stripes on upper arms vs No purple stripes on suit. | 🟠 MAJOR |
| 2:29 | 2:40 | Female Astronaut | Wear, Damage | Suit is heavily caked with brown sand vs Suit is completely clean. | 🟠 MAJOR |
| 2:29 | 2:50 | Male Astronaut | Wear, Damage | Suit is heavily caked with brown sand vs Suit is completely clean. | 🟠 MAJOR |
| 0:10 | 0:20 | Both | Cross-Cut Action | Male walks on frame left, Female on right vs Female walks on frame left, Male on right. | 🟡 MINOR |
| 0:10 | 1:50 | Female Astronaut | Costume Identity | Forearm is solid tan/grey vs Forearm has a bright orange/gold vent detail. | 🟡 MINOR |

## THE THREE THAT MATTER

1. **The Dirt Reset (2:29 vs 2:40)** — heavily soiled digging the ship out,
   spotless in the next shots. Fix: regenerate the 2:40 and 2:50 shots with dirt.
2. **Disappearing Stripes (1:30 vs 2:10)** — the male's identifying purple
   stripes vanish for one scene; the visual separation of the two characters is
   lost. Fix: regenerate the 2:10 shot.
3. **Random Screen Swapping (0:10 vs 0:20)** — the characters constantly swap
   left/right positions between cuts while walking. Fix: flip horizontal on
   select wide shots if lighting allows, or accept it.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Suit dirt resetting | Regenerate 2:40 and 2:50 shots | Medium (Regen) |
| Missing purple stripes | Regenerate 2:10 shot | Medium (Regen) |
| Screen direction swaps | Flip horizontal or accept | Free (Edit/Accept) |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Female's suit has blue stripes, Male's has purple. | Does the character bible specify this exact color coding for the suits? |
| Suits reset to clean at 2:40. | Were they intended to decontaminate/clean their suits off-screen before unloading the cargo? |

## OUT-OF-SCOPE FLAGS

- 1:50 close-up glove phasing through sand → VIDEO_QA
- 2:51 wrench fusing with metal strut → VIDEO_QA
- 1:00 to 2:00 ship terrain changing from flat ripples to steep dune → MANTIK_QA
