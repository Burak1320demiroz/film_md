# 🧩 THE STONE SKY — MANTIK QA HAM RAPORU

> **Rubrik:** `../../QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Alındı:** 05.08.2026 · dış model, repo erişimsiz · girdi: yalnız video (tek mod)
> **Model çıktısı aşağıda olduğu gibi korunmuştur — düzenlenmedi.**
> Tablolar operatör yapıştırmasında düzleşmiş olabilir; içerik dokunulmamıştır.
> ⭐ FLAGS FOR DOCUMENT CHECK cevapları → `../01_FILM_RAPORLARI/THE_STONE_SKY.md`

---

INPUT MODE: V
BASELINE: SELF-CONSISTENCY
This review answers "does the film agree with itself?"
It does NOT answer "does the film match its design?"

FILM: (not supplied)
RUNTIME: 02:15 · SCENES OBSERVED: 12
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees
with itself, not whether it matches its design.

OVERALL SCORE: 4/10
VERDICT: STRUCTURAL PROBLEM

SCENE INVENTORY
| # | In-out | Location | Present | What happens | Dialogue |
|---|---|---|---|---|---|
| S1 | 0:00-0:04 | Open plain | Astronaut | Kneeling, operating a tripod drill | No |
| S2 | 0:05-0:09 | Plain | Astronaut | Stands, observes ejecta ring | Yes |
| S3 | 0:10-0:19 | Plain | Astronaut | Geysers of rocks erupt upward | No |
| S4 | 0:20-0:29 | Base camp | Astronaut, Rover | Runs to rover, gets in, drives | No |
| S5 | 0:30-0:39 | Sky | Rocks | Debris shooting up against planet | No |
| S6 | 0:40-0:55 | Plain | Astronaut, Rover | Driving evasively through dust | No |
| S7 | 0:56-1:09 | Rover cab | Astronaut | Assessing routes via voice log | Yes |
| S8 | 1:10-1:29 | Canyon | Astronaut, Rover | Dodging falling rocks | No |
| S9 | 1:30-1:35 | Crevasse | Astronaut, Rover | Rover jumps across a gap | No |
| S10 | 1:36-1:49 | Ditch | Astronaut(s), Rover | Rover crashes; astronauts run | No |
| S11 | 1:50-1:59 | Dark Lake | None | Massive rock geyser erupts | No |
| S12 | 2:00-2:15 | Dark ground | Astronaut | Stops running, sits in defeat | No |

THE CHARACTER — as first clearly seen
Face:        Short dark hair, minor scarring on left cheek.
Suit:        Light grey/beige base, orange arm striping, dark chest rig.
Wear/dirt:   Clean base, minor dust on knees.
Equipment:   Clear dome helmet, grey gloves, silver tripod drill.
First scene this is fully visible: S1

THE WORLD — as the film shows it
Gravity read:     Mixed (dust floats slowly, heavy rocks and rover fall fast).
Atmosphere read:  Dust hangs in air, but sky is black like a vacuum.
Light source:     Single hard light (sun), casting sharp shadows.
Locations:        Plain (flat, dusty), Base camp (small dome), Canyon (rock walls), Dark Lake (smooth black basin).

THE COUNTER — does the film track a changing quantity?
NONE

NUMBERS SPOKEN OR SHOWN
0:05 — "30 to 55 meters out"
1:04 — "Not one at any time"

OBJECTS THAT GET ATTENTION
The tripod drill (S1)
The dark ground/apron (S2, S7, S12)
The Rover (S4, S6, S7, S8, S9, S10)

SCORES SUMMARY
| Category | Score | Critical Issue |
|---|---|---|
| Physical Consistency | 5/10 | Gravity/mass reads conflict (dust vs. rover). |
| Counter Logic | N/A | No counter observed. |
| Spatial Geography | 4/10 | Flat plain suddenly gains deep canyons. |
| Time & Light Logic | 3/10 | Shadow directions flip completely. |
| State, Costume & Props | 2/10 | Rover changes chassis and tank layout. |
| Causality & Knowledge | 7/10 | Decisions track with prior observations. |
| Quantity Consistency | 1/10 | One character splits into two clones. |
| Setup & Abandonment | 6/10 | Drill is deployed and immediately abandoned. |

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 3   🟡 MINOR: 2

COUNTER CURVE
NONE

LOCATION MAP
| Location (your name for it) | Scenes | Consistent? | Mismatch |
|---|---|---|---|
| Open plain | S1, S2, S3, S6 | Yes | None. |
| Canyon | S8, S9 | No | Appears out of nowhere from a flat plain. |
| Dark Lake / Apron | S11, S12 | Yes | None. |

DRIFT MAP — where the film starts losing itself
| Element | First slip (timecode) | Undeniable by | Recovered? |
|---|---|---|---|
| Rover Design | 0:50 | 1:45 | No. Remains a different vehicle in the ditch. |
| Character Count | 1:40 | 1:40 | Yes. Reverts to one person in S12. |
| Shadow Direction | 0:40 | 0:50 | No. Bounces back and forth. |

CONTRADICTION LOG
| Timecode A | Timecode B | Category | What contradicts what | Severity |
|---|---|---|---|---|
| 1:35 | 1:40 | Quantity | S9 shows one astronaut jumping gap; S10 shows TWO identical astronauts running side-by-side from crash. | 🔴 BLOCKER |
| 0:50 | 1:45 | State/Props | S6 rover has huge orange rear tanks; S10 crashed rover has empty rear bed and entirely different roll cage. | 🔴 BLOCKER |
| 0:00 | 0:50 | Time & Light | S1 shadows cast forward-right; S6 shadows cast left. | 🟠 MAJOR |
| 0:00 | 0:09 | State/Costume | S1 suit has flat chest rig; S2 suit has bulky black chest box. | 🟠 MAJOR |
| 0:10 | 1:18 | Physical | S3 rocks erupt upward (anti-gravity); S8 massive rocks fall downward (heavy gravity). | 🟠 MAJOR |
| 0:00 | 0:24 | Setup/Props | S1 drill is primary focus; S4 astronaut runs away completely empty-handed, leaving it. | 🟡 MINOR |
| 2:00 | 2:06 | State/Costume | S12 astronaut stands clean; S12 astronaut sits with heavy dirt accumulation on boots/knees. | 🟡 MINOR |

OPEN THREADS
| Object / setup | Introduced | Returned to? | Note |
|---|---|---|---|
| The tripod drill | S1 | No | Left behind in the chaos. |
| The small dome | S4 | No | Seen in background once, never entered. |

THE THREE THAT MATTER
The Clone (1:35 vs 1:40)
Why a viewer would feel it: The film is entirely focused on a solo survivor, and suddenly a twin is running next to her. It breaks reality instantly.
Fix: Recut to remove the wide shot of two runners, or regenerate S10.

The Shape-shifting Rover (0:50 vs 1:45)
Why a viewer would feel it: The vehicle goes from having giant bright orange cargo tanks to a bare buggy chassis.
Fix: Regenerate the crashed rover shot to match the earlier asset, or cut S6.

Flipping Shadows (0:00 vs 0:50)
Why a viewer would feel it: Reverses the spatial orientation of the planet and the sun, confusing the direction of travel.
Fix: Flip S6 horizontally in the edit if no text/asymmetry prevents it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
| Finding | Fix | Cost |
|---|---|---|
| Clone in S10 | Cut the 2-second wide shot of the runners | Cheap |
| Flipped shadows in S6 | Horizontal mirror the clip | Cheap |
| Rover chassis mismatch | Regenerate S10 ditch crash | High |
| Chest box changes S1-S2 | Accept it (hard to spot in motion) | Zero |

FLAGS FOR DOCUMENT CHECK
| Observation | Question the document must answer |
|---|---|
| The canyon appears abruptly after flat plains. | Did the plan specify a change in geology, or did the model invent the canyon? |
| Rocks shoot up in S3, but fall down in S8. | Is this a localized anti-gravity event, or just ejecta falling back to the surface? |
| The rover gains orange tanks in S6. | Which rover design is the intended spec? |

OUT-OF-SCOPE FLAGS
Technical: Hard cut injected mid-action at 0:05 (VIDEO_QA).
Technical: Lip-sync completely fails during S7 cab monologue (VIDEO_QA).
Technical: Huge burned-in title text at 2:10 (VIDEO_QA).
Dramatic: Driving sequence S6-S8 feels repetitive and stalls the narrative (SENARYO_QA).
