# THE THIRD DUNE — MANTIK_QA HAM RAPOR

> **Tarih:** 11.08.2026 · **Rubrik:** `QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Mod:** V (rubrik zaten yalnız video) · **Malzeme:** 4:05 kurgu
> ⛔ Model çıktısı olduğu gibi. Belge cevapları film kaydında —
> ⚠️ bu raporun üç MAJOR'ından ikisi belge kontrolünde DÜŞTÜ.

---

```
INPUT MODE: V
BASELINE: SELF-CONSISTENCY
FILM: (not supplied)
RUNTIME: 04:05 · SCENES OBSERVED: 13 (counted, not from a document)
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 7/10
VERDICT: FIXABLE IN EDIT
```

## SCENE INVENTORY

| # | In-out | Location | Present | What happens | Dialogue |
|---|---|---|---|---|---|
| 1 | 0:00-0:19 | Open Dunes | Male, Female | Walking, female plants measuring stick in sand | Yes |
| 2 | 0:20-0:40 | Open Dunes | Male, Female | Walking, storm approaches in background | No |
| 3 | 0:40-1:00 | Open Dunes | Male, Female | Male scoops sand, it pours from hand | Yes |
| 4 | 1:00-1:20 | Flat Rippled Sand | Male, Female | Walking toward hexagonal ship in distance | Yes |
| 5 | 1:20-1:40 | Dune Crest | Male, Female | They find a white panel buried in sand | Yes |
| 6 | 1:40-2:00 | Steep Dune | Male, Female | Sliding down a steep dune toward ship | No |
| 7 | 2:00-2:20 | Ship Exterior | Male, Female | Inspecting ship embedded in dune side | Yes |
| 8 | 2:20-2:40 | Ship Exterior | Male, Female | Digging a white panel out of the sand | Yes |
| 9 | 2:40-2:50 | Ship Cargo Bay | Male, Female | Unloading cargo boxes from ship | Yes |
| 10 | 2:50-3:00 | Ship Exterior | Male | Tightening landing strut with wrench | Yes |
| 11 | 3:00-3:10 | Sand Flat | None | 10 cargo boxes lined up in the sand | No |
| 12 | 3:10-3:20 | Cockpit | Male, Female | Preparing for takeoff, discussing mass | Yes |
| 13 | 3:20-4:05 | Exterior | Ship | Ship takes off vertically, leaving crater | No |

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|---|---|
| Physical Consistency | 6/10 | Wrench fuses with strut; sand flows like liquid |
| Counter Logic | 10/10 | Storm proximity increases monotonically |
| Spatial Geography | 4/10 | Ship's surrounding terrain changes completely |
| Time & Light Logic | 9/10 | Consistent lighting and shadow angles |
| State, Costume & Props | 5/10 | Suit dirt regenerates/cleans itself between shots |
| Causality & Knowledge | 8/10 | Logical progression of unweighting the ship |
| Quantity Consistency | 10/10 | Cargo box count is strictly maintained |
| Setup & Abandonment | 6/10 | Measuring stick and first panel abandoned |

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 3

## COUNTER CURVE

Storm Proximity: S1 very far → S4 far → S7 approaching → S12 immediate →
S13 engulfing. (Moves in one direction. No reversals.)

## LOCATION MAP

| Location | Scenes | Consistent? | Mismatch |
|---|---|---|---|
| Open Dunes | 1, 2, 3, 5, 6 | Yes | None |
| Ship Exterior | 4, 7, 8, 9, 10, 13 | No | Terrain changes from flat ripples (S4) to steep dune (S7/S13); resting footprint changes to deep circular crater (S13). |
| Ship Cockpit | 12 | Yes | None |

## DRIFT MAP

| Element | First slip | Undeniable by | Recovered? |
|---|---|---|---|
| Terrain around ship | 1:00 (flat) | 2:00 (steep dune) | No |
| Suit dirt state | 2:25 (dirty) | 2:41 (clean) | No, stays clean |

## CONTRADICTION LOG

| Timecode A | Timecode B | Category | What contradicts what | Severity |
|---|---|---|---|---|
| 1:00 | 2:00 | Spatial Geography | Ship sits on flat, rippled sand vs Ship is embedded halfway up a smooth, steep dune. | 🟠 MAJOR |
| 2:25 | 2:41 | State, Costume | Female's suit is covered in dark sand from digging vs Female's suit is clean while carrying cargo out of the ship. | 🟠 MAJOR |
| 2:00 | 3:30 | Spatial Geography | Ship rests flatly on a sand slant vs Ship's departure reveals a perfectly circular, deep impact crater that does not match the hull's shape. | 🟠 MAJOR |
| 1:50 | 2:51 | Physical Consist. | (Out of scope for this rubric, but noted: Glove phasing through sand and wrench fusing into strut violate internal physics). | 🟡 MINOR |

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
|---|---|---|---|
| Black measuring stick | 0:13 | No | Planted in the sand and left behind when they walk away at 0:20. |
| Half-buried white panel | 1:30 | No | Found on the dune crest, but abandoned as they slide down the dune at 1:40. (A similar panel is dug up at 2:20, unclear if intended to be the same object). |

## THE THREE THAT MATTER

1. **Ship Terrain Shift (1:00 vs 2:00)** — the geography around the ship
   transforms from a flat plain to a steep hill. Fix: cut the wide shot at 1:00
   or replace it with a shot of the ship on a dune.
2. **Suit Dirt Reset (2:25 vs 2:41)** — heavily soiled digging, spotless 15
   seconds later. Fix: re-order shots, or regenerate the cargo-carrying shot.
3. **The Takeoff Crater (2:00 vs 3:30)** — a deep, perfectly spherical crater
   reads as a different landing site. Fix: regenerate the final wide shot.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Terrain shift at approach | Cut the 1:00 wide shot | Cheap (Edit) |
| Suit dirt resetting | Regenerate 2:40 cargo shot | Medium (Regen) |
| Spherical crater after takeoff | Regenerate 3:30 wide shot | Medium (Regen) |
| Measuring stick abandoned | Accept it (they were in a hurry) | Free (Accept) |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| The white panel at 1:30 and the white panel at 2:20. | Are these intended to be two separate pieces of debris, or did the continuity of one object break across the dune slide? |
| The circular crater at 3:30. | Did the plan specify the ship leaving a deep crater, or was it supposed to just lift off the dune surface as established in scene 7? |

## OUT-OF-SCOPE FLAGS

- 1:50 glove phasing through sand (technical → VIDEO_QA)
- 2:51 wrench fusing with metal strut (technical → VIDEO_QA)
- 4:00 Burned-in title text on screen (technical → VIDEO_QA)
