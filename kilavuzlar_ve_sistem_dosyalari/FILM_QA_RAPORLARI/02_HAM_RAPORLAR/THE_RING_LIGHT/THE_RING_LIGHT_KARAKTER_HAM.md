# THE RING LIGHT — KARAKTER_QA HAM RAPOR

> **Tarih:** 12.08.2026 · **Rubrik:** `QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Mod:** V (rubrik zaten yalnız video) · **Malzeme:** 144 s kurgu · 2 karakter
> ⛔ Model çıktısı olduğu gibi. Belge cevapları ve kilit çelişkileri film kaydında.
> ⚠️ Pasaport **14 sahnenin 2'sinden** kuruldu (yüz yalnız 2:00-2:20 arasında
> görünüyor = 20 s / 144 s) ve Ses sütunu, planın YASAKLADIĞI bir ekran
> repliğine puan verdi → DERS 97.

---

```
FILM: (not supplied)
RUNTIME: 02:24 · SCENES OBSERVED: 12 · CHARACTERS TRACKED: 2
BASELINE: SELF-CONSISTENCY — this review measures whether each character
agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 8.5/10
VERDICT: DRIFTS BUT RECOVERABLE
```

## CHARACTER PASSPORT(S)

```
CHARACTER PASSPORT — 1
Label: The Pilot (Woman, Left Seat)
First clear view: S13, 2:00
Face: Smooth skin texture, rounded jaw structure, no visible marks or scars.
Hair: Dark, pulled back tightly inside the helmet collar.
Eyes: Dark brown, no distinctive marks.
Build: Average frame, seated posture.
Costume: EVA suit, white base. Dark grey and RED paneling on shoulders and
  arms. Red accents are strictly on the left and right outer arms.
Equipment: Helmet (visor retracted/open), heavy white and grey gloves (sealed).
Wear map: Clean; no dirt, dust, or tears on chest or arms.
Voice: Does not speak on screen.

CHARACTER PASSPORT — 2
Label: The Co-Pilot (Man, Right Seat)
First clear view: S13, 2:00
Face: Black male, shaved head, neatly trimmed short beard/stubble around jaw
  and chin.
Hair: Bald/shaved.
Eyes: Dark brown.
Build: Broad shoulders, solid frame.
Costume: EVA suit, white base. Dark grey and BLUE paneling on shoulders and
  arms. Blue accents are strictly on the left and right outer arms.
Equipment: Helmet (visor retracted/open), heavy white and grey gloves (sealed).
Wear map: Clean; no dirt, dust, or tears on chest or arms.
Voice: Deep, calm, authoritative texture.

CHARACTER COUNT
How many distinct recurring characters does the film track? 2
Any scene where the count on screen disagrees with who could be present? No.

CARRIED-OBJECT LEDGER
No objects are picked up, handed off, or put down by the characters in the
visible footage. Hands remain on flight controls or holding each other (2:08).
```

## APPEARANCE TABLE

| Character | Scene | In-out | Face visible? | State notes |
|---|---|---|:--:|---|
| The Pilot | S2 | 0:10-0:20 | No | Seated left. Opaque visor, back/side view. |
| The Co-Pilot | S2 | 0:10-0:20 | No | Seated right. Opaque visor, back/side view. |
| The Pilot | S5 | 0:40-0:50 | No | Seated left. Visor opaque. |
| The Co-Pilot | S5 | 0:40-0:50 | No | Seated right. Visor opaque. |
| The Pilot | S8 | 1:10-1:20 | No | Seated left. Visor opaque. |
| The Co-Pilot | S8 | 1:10-1:20 | No | Seated right. Visor opaque. |
| The Pilot | S11 | 1:40-1:50 | No | Seated left. Visor opaque. |
| The Co-Pilot | S11 | 1:40-1:50 | No | Seated right. Visor opaque. |
| The Pilot | S13 | 2:00-2:10 | Yes | First clear view. Visor open. |
| The Co-Pilot | S13 | 2:00-2:10 | Yes | First clear view. Visor open. |
| The Pilot | S14 | 2:10-2:20 | Yes | Floating in tunnel. Suit design drifts. |
| The Co-Pilot | S14 | 2:10-2:20 | Yes | Floating in tunnel. Suit design drifts. |

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|:--:|---|
| Facial Identity | 9/10 | Faces remain consistent across the two scenes they are fully visible. |
| Hair, Build & Proportions | 9/10 | Heights and physical builds hold perfectly. |
| Costume Identity | 4/10 | Massive suit design drift between the cockpit and the tunnel. |
| Wear, Damage & Injury | 10/10 | Pristine throughout; no continuity errors. |
| Equipment State | 8/10 | Visors go from opaque to retracted, but stay consistent thereafter. |
| Cross-Cut Action | 9/10 | Screen direction and relative positioning hold perfectly. |
| Count & Separation | 10/10 | Always exactly two characters. No duplicates. |
| Voice & Performance | 9/10 | Single on-screen spoken line matches the physical body perfectly. |

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 0

## IDENTITY DRIFT MAP

| Character | Element | First slip | Undeniable by | Recovered? |
|---|---|---|---|---|
| The Pilot | Costume | 2:10 | 2:10 | No (ends in drifted state) |
| The Co-Pilot | Costume | 2:10 | 2:10 | No (ends in drifted state) |

## WEAR TIMELINE

| Mark | Acquired | Present at | Absent at ⚠️ | One-way? |
|---|---|---|---|---|
| (No marks tracked) | N/A | N/A | N/A | N/A |

## CONTRADICTION LOG

| Timecode A | Timecode B | Character | Category | What contradicts what | Severity |
|---|---|---|---|---|:--:|
| 2:00 | 2:10 | The Pilot | Costume Identity | Suit changes from smooth red/grey/white paneling to ribbed/segmented shoulder pads. | 🟠 MAJOR |
| 2:00 | 2:10 | The Co-Pilot | Costume Identity | Suit changes from smooth blue/grey/white paneling to ribbed/segmented shoulder pads. | 🟠 MAJOR |

## THE THREE THAT MATTER

1. **Costume Drift at 2:10:** The space suits completely change design (shoulder
   pads, chest plating, fabric textures) between the cockpit and the transfer
   tunnel. A viewer will immediately feel the disconnect because the characters
   are identically framed but wearing different gear seconds apart.
   Cheapest fix: Regenerate S14 (2:10) using the 2:00 suits as strict image
   anchors.
2. (No other major continuity breaks found)
3. (No other major continuity breaks found)

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Suit design shift at 2:10 | Regenerate S14 (tunnel scene) using S13 anchors | High (requires new generation) |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Visors are opaque from 0:10 to 1:50, then open/invisible at 2:00. | Does the script specify the crew retracting their visors after docking, or is the model hallucinating the removal? |
| Early dialogue (0:10-1:50) occurs while visors are opaque and mouths are unseen. | Who is speaking these early lines? Are they meant to be The Pilot and Co-Pilot, or mission control? |

## OUT-OF-SCOPE FLAGS

- Contact morphing on the gloves during the hand-hold at 2:08 → VIDEO_QA
- Airborne sound effects in a vacuum environment → MANTIK_QA
- Abrupt cliffhanger ending → SENARYO_QA
