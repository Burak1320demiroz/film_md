# 🧍 THE STONE SKY — KARAKTER QA HAM RAPORU

> **Rubrik:** `../../QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Alındı:** 05.08.2026 · dış model, repo erişimsiz · girdi: yalnız video (tek mod)
> ⭐ **RUBRİĞİN İLK ÇALIŞTIRMASI.**
> **Model çıktısı aşağıda olduğu gibi korunmuştur — düzenlenmedi.**
> ⚠️ Kural ihlali not edildi: rapor `FILM: The Stone Sky` yazdı — rubrik
> başlık kartından isim okumayı yasaklıyor (DERS 65). Doğru çıktı
> `FILM: (not supplied)` olurdu. Bulguları etkilemiyor; kayda geçirildi.
> FLAGS FOR DOCUMENT CHECK cevapları → `../01_FILM_RAPORLARI/THE_STONE_SKY.md`

---

INPUT MODE: V
BASELINE: SELF-CONSISTENCY — this review measures whether each character agrees with themselves, not whether they match a design sheet.
FILM: The Stone Sky
RUNTIME: 02:15 · SCENES OBSERVED: 13 · CHARACTERS TRACKED: 1

OVERALL SCORE: 6/10
VERDICT: IDENTITY BREAK
A literal on-screen duplicate in scene 10 triggers an automatic identity break, regardless of the strong facial and voice consistency elsewhere.

CHARACTER PASSPORT(S)
CHARACTER PASSPORT — one per character
Label:            The Astronaut
First clear view: S1, 0:00
Face:             Short dark hair, olive skin, minor dirt/scarring on left cheek and forehead, prominent cheekbones.
Hair:             Short, dark brown/black, swept slightly right.
Eyes:             Dark, visible through the visor.
Build:            Average height, athletic/slender frame, competent posture.
Costume:          Grey/beige space suit. Orange striping down the arms and legs. Dark grey gloves. Dark flat chest harness with horizontal straps. White patch/detail on left shoulder.
Equipment:        Clear dome helmet with a silver/dark lower rim (sealed). Silver tripod drill (held in S1). Small backpack unit.
Wear map:         Clean base suit, slight grey dust on knees from kneeling.
Voice:            Mid-pitch female, calm and analytical texture.

APPEARANCE TABLE
| Character | Scene | In-out | Face visible? | State notes |
|---|---|---|---|---|
| The Astronaut | S1 | 0:00-0:04 | Yes | Kneeling with drill. Flat chest rig. |
| The Astronaut | S2 | 0:05-0:09 | Yes | Standing. Chest rig is now a bulky black box. |
| The Astronaut | S3 | 0:10-0:19 | No | Wide shot, back visible. |
| The Astronaut | S4 | 0:20-0:29 | No | Runs to rover, gets in. Drill left behind. |
| The Astronaut | S6 | 0:40-0:55 | Yes (Profile) | Driving. Orange arm stripes visible. |
| The Astronaut | S7 | 0:56-1:09 | Yes | Close up in cab. Chest rig is flat/grey again. |
| The Astronaut | S8 | 1:10-1:29 | No | Wide shots driving in canyon. |
| The Astronaut | S9 | 1:30-1:35 | No | Inside rover jumping gap. |
| The Astronaut | S10 | 1:36-1:49 | No | Crash. TWO identical astronauts exit and run. |
| The Astronaut | S12 | 2:00-2:09 | Yes (Profile) | Stops running (clean knees). Sits down (dirty knees). |

Note: S5 and S11 are environmental/vehicle shots with no character clearly visible. S13 is the title card.

SCORES SUMMARY
| Category | Score | Critical Issue |
|---|---|---|
| Facial Identity | 8/10 | Facial structure and hair remain highly consistent across close-ups. |
| Hair, Build & Proportions | 9/10 | Frame and height read consistently throughout the action. |
| Costume Identity | 4/10 | Chest rig shifts drastically in shape and volume. |
| Wear, Damage & Injury | 5/10 | Dust accumulation on legs spikes instantly between cuts. |
| Equipment State | 8/10 | Drops drill logically to run; helmet stays consistently sealed. |
| Cross-Cut Action | 7/10 | Screen direction and momentum generally hold across the escape sequence. |
| Count & Separation | 1/10 | A clone appears mid-escape. |
| Voice & Performance | 8/10 | Voice tone and accent match in both speaking scenes. |

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 1   🟡 MINOR: 1

IDENTITY DRIFT MAP — per character
| Character | Element | First slip (timecode) | Undeniable by | Recovered? |
|---|---|---|---|---|
| The Astronaut | Chest Rig | 0:05 | 0:05 | Yes (Reverts to flat at 0:56) |
| The Astronaut | Count | 1:40 | 1:40 | Yes (Back to solo at 2:00) |
| The Astronaut | Suit Wear | 2:06 | 2:06 | No (Film ends) |

WEAR TIMELINE — per tracked mark
| Mark | Acquired | Present at | Absent at ⚠️ | One-way? |
|---|---|---|---|---|
| Knee/Boot Dirt | Kneeling (0:00) | 0:00, 2:06 | 2:00 | No (Appears clean at 2:00, heavily soiled immediately after at 2:06) |

CONTRADICTION LOG
| Timecode A | Timecode B | Character | Category | What contradicts what | Severity |
|---|---|---|---|---|---|
| 1:35 | 1:40 | The Astronaut | Count & Separation | 1:35 shows one driver in the rover; 1:40 shows two identical astronauts running side-by-side from the crash. | 🔴 BLOCKER |
| 0:00 | 0:05 | The Astronaut | Costume Identity | 0:00 shows a flat, dark strap harness on the chest; 0:05 shows a protruding, boxy black chest unit. | 🟠 MAJOR |
| 2:00 | 2:06 | The Astronaut | Wear, Damage & Injury | 2:00 shows the astronaut stopping with relatively clean grey boots/knees; 2:06 shows her sitting with heavily caked dark dirt on the boots/knees. | 🟡 MINOR |

THE THREE THAT MATTER
The Clone (1:35 vs 1:40)
What: A second, identical astronaut appears running away from the crashed rover.
Why: The film establishes a solo survivor narrative. A sudden twin completely shatters the reality of the scene.
Fix: Re-cut to trim the wide shot of the two runners, or regenerate scene 10.

The Shifting Chest Rig (0:00 vs 0:05)
What: The central chest equipment changes from a flat harness to a bulky black box on a simple stand-up cut.
Why: It sits dead-center in the frame during a close-up dialogue shot, making the model's instability obvious.
Fix: Accept it; it happens fast and is mostly obscured by action later, but it is a noticeable continuity slip.

Spontaneous Dirt (2:00 vs 2:06)
What: Massive dark dirt accumulation appears on the legs in the exact moment the character sits down.
Why: It breaks the one-way rule of wear and makes the final emotional beat feel stitched together from different generation batches.
Fix: Accept it. The emotional posture of sitting down is strong enough to carry the scene despite the texture pop.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Finding | Fix | Cost |
|---|---|---|
| Clone running | Trim the wide shot to only show the crash dust, skip the running wide shot | Low |
| Sudden dirt when sitting | Accept it | Zero |
| Chest rig change | Regenerate S2 close-up | High |

FLAGS FOR DOCUMENT CHECK
| Observation | Question the document must answer |
|---|---|
| The chest rig changes from flat to a bulky box. | Did the design bible specify a flat harness or a hard chest box? |
| A wrist symbol (yellow/orange cross) is highly visible at 0:56 but not earlier. | Is this wrist indicator part of the intended suit patch layout? |

OUT-OF-SCOPE FLAGS
Vehicle identity: The rover's chassis and bright orange rear tanks completely change shape between 0:50 and 1:45 → MANTIK_QA
Physics: Rocks shoot upward against gravity at 0:10, but fall downward heavily at 1:18 → MANTIK_QA
Editing: There is a jarring hidden cut injected mid-action at 0:05 → VIDEO_QA
Visuals: Large title text is burned directly into the final frames at 2:10 → VIDEO_QA
