# 📖 THE ROSE COAT — ④ HİKAYE HAM RAPORU

> **Koşu:** 26.08.2026 · mod V (SPEC dosyası VARDI, verilmedi → ÖN KOŞU [D94/D117])
> **Rubrik:** `../../QA_PROMPTLARI/4_HIKAYE_QA_CRITIQUE_PROMPT.md`
> ⛔ Aşağısı MODELİN ÇIKTISIDIR, düzeltilmemiştir.
> ⛔ **KESME LİSTESİ UYGULANMAZ** — ön koşu. Gerekçe film kaydında.

---

```
INPUT MODE: V
BASELINE: THE FILM AS SCREENED
MATERIAL TYPE: FILM (undeclared)
FILM: (not supplied)
FORMAT: YATAY
LENGTH CLASS: (not supplied)
RUNTIME: 135 s measured
SCENE COUNT: 13 counted, not from a document
CUTS COUNTED: 13 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10)
NON-SCENE MATERIAL: 2:10-2:15 title card
LINES HEARD: none
SPEC BLOCK PROVIDED: no — mode V

ENDS OR STOPS: stops — The film cuts to a title card while a character is
               midway up a ladder, resolving no narrative thread.
PEAK LOCATED AT: no peak located

ARITHMETIC GATE
SCORED CATEGORIES:  9
SUM OF SCORES:      21.0
DIVISION:           21.0 ÷ 9 = 2.3

OVERALL STORY SCORE: 2.3/10
VERDICT: REWRITE PREMISE
```

## THE FILM IN ONE SENTENCE

> "Two astronauts methodically wander a pink desert, repeatedly brushing sand
> off their suits and equipment with no clear objective or consequence."

## SCORES SUMMARY

| Category | Score | Core Issue |
|---|:--:|---|
| Hook | 5/10 | −5 · 0:10 (S2) |
| Premise & Clarity | 3/10 | −7 · 0:10 (S2) |
| Structure & Pacing | 2/10 | −8 · 0:50 (S6) |
| Character | 1/10 | −9 · 0:20 (S3) |
| Theme | 2/10 | −8 · 0:50 (S6) |
| Dialogue | N/A | silent film |
| Emotional Arc | 1/10 | −9 · 1:10 (S8) |
| Ending | 1/10 | −9 · 2:00 (S13) |
| Originality | 4/10 | −6 · 0:40 (S5) |
| Retention Risk | 2/10 | −8 · 0:30 (S4) |

## THE THREE THINGS THAT MOST HURT THIS FILM

1. `0:30 (S4)` — Lack of escalation — The film repeats the exact same action
   (walking, brushing sand) for over two minutes without introducing stakes, a
   goal, or a timeline.
2. `1:10 (S8)` — Consequence-free hazard — The only variation in the narrative
   (the fall into the crater) results in no injury, no change in routine, and no
   emotional reaction. It carries zero weight.
3. `2:00 (S13)` — Unresolved ending — Cutting to the title card while a
   character climbs a ladder provides no payoff, no thematic closure.

## THE THREE THINGS WORTH PROTECTING

1. `0:00 (S1)` — The surreal opening — Sand pouring from a geometric wall is a
   striking image that poses an immediate, intriguing visual question.
2. `0:40 (S5)` — The meticulous routine — The methodical brushing of the suits
   establishes a highly specific, deliberate tone that grounds the world (even
   if it is ultimately overused).
3. `1:40 (S11)` — The cohesive aesthetic — The visual world-building (the
   pink/red monochrome palette) is highly atmospheric and sustains a mood of
   isolation.

## THE ONE THING NOTHING ELSE DOES

> No other film treats astronaut surface operations entirely as an obsessive,
> meditative cleaning routine in a pastel desert — though it currently exists
> as an aesthetic mood board rather than a story.

## SCENE MAP — mode V (numbering is the reviewer's)

| # | In-out | Where | Who | What happens | Dialogue? | Function |
|---|---|---|---|---|:--:|---|
| 1 | 0:00-0:09 | Geometric Wall | None | Sand pours from a slit | No | Hook |
| 2 | 0:10-0:19 | Habitats | A, B | Walking right past modules | No | Establish characters |
| 3 | 0:20-0:29 | Buried shuttle | A, B | Walking right past a shuttle | No | Worldbuilding |
| 4 | 0:30-0:39 | Rocket distance | A, B | Walking right toward a distant rocket | No | Travel |
| 5 | 0:40-0:49 | Desert flat | A, B | One brushes sand off the other | No | Routine establishment |
| 6 | 0:50-0:59 | Rocket base | A, B | Brushing a low square panel | No | Routine |
| 7 | 1:00-1:09 | Dune by leg | A, B | Walking up a dune | No | Travel |
| 8 | 1:10-1:19 | Crater | A, B | One astronaut falls backward into dust | No | Hazard |
| 9 | 1:20-1:29 | Desert flat | A, B | Brushing sand off the fallen astronaut | No | Recovery |
| 10 | 1:30-1:39 | Rocket base | A, B | Brushing a large upper panel | No | Routine |
| 11 | 1:40-1:49 | Rocket base | A, B | Standing near landing leg | No | Arrival |
| 12 | 1:50-1:59 | Rocket ladder | A, B | Brushing the suit near a ladder | No | Routine |
| 13 | 2:00-2:09 | Rocket ladder | A, B | Climbing the ladder | No | Exit |

```
RUNTIME (measured):   135 s
SCENE COUNT (counted): 13
SPEAKING SCENES:       0 — (silent film)
THE FILM'S QUESTION:   What is the purpose of this facility, and why are they
                       constantly cleaning it?
THE READ:              Two silent figures perform endless, consequence-free
                       maintenance in a dusty environment before casually
                       boarding their ship.
```

## PRESENCE STRING

```
-111111111111
```

## SCENE-BY-SCENE VERDICT

| # | Scene | Function in story | Verdict | Note |
|---|---|---|:--:|---|
| S1 | 0:00-0:09 | Hook | KEEP | Strong, surreal visual opening. |
| S2 | 0:10-0:19 | Establish characters | KEEP | Introduces the protagonists. |
| S3 | 0:20-0:29 | Worldbuilding | MERGE | Combine with S4 to speed up travel. |
| S4 | 0:30-0:39 | Travel | CUT | Redundant walking sequence. |
| S5 | 0:40-0:49 | Routine establishment | KEEP | Establishes the obsessive brushing routine. |
| S6 | 0:50-0:59 | Routine | CUT | Redundant brushing; halts momentum. |
| S7 | 1:00-1:09 | Travel | KEEP | Necessary approach to the hazard. |
| S8 | 1:10-1:19 | Hazard | REWRITE | Needs stakes — currently a weightless, consequence-free fall. |
| S9 | 1:20-1:29 | Recovery | MERGE | Combine with S5 to make the brushing a reaction to the fall. |
| S10 | 1:30-1:39 | Routine | CUT | Redundant action stalling the finale. |
| S11 | 1:40-1:49 | Arrival | KEEP | Arrival at the final objective. |
| S12 | 1:50-1:59 | Routine | CUT | One last redundant brush before climbing. Unnecessary. |
| S13 | 2:00-2:09 | Exit | REWRITE | Must resolve the story, not just show a ladder climb. |

## RANKED CUT LIST (to lose 30 seconds)

```
resulting runtime: ~85s — BELOW FORMAT FLOOR, replace don't remove
```

1. S4 — 10 s — Redundant walking; travel is already established.
2. S6 — 10 s — Redundant brushing; action adds no new information.
3. S10 — 10 s — Redundant brushing; repetition is actively stalling the narrative.
4. S12 — 10 s — Redundant brushing; halts the momentum of the final ascent.
5. S3 — 10 s — Redundant walking; can easily be merged with other establishing wide shots.

## RETENTION DROP-OFF FORECAST

- `0:30` — The film has shown walking for 20 seconds with no escalation.
  Fix: Introduce the hazard or a new objective by 0:15.
- `0:50` — A second brushing scene confirms to the viewer that nothing else is
  going to happen in this film. Fix: Reveal a discovery under the sand.
- `1:30` — Yet another panel is brushed. The loop is exhausted.
  Fix: Have the panel brushing trigger a mechanism or unlock the ship.

## SHAREABLE MOMENT

`0:00-0:05` — The surreal image of sand pouring out of a floating/geometric
pink wall.

## REWRITE PRESCRIPTIONS

1. SCENE 8: replace the consequence-free fall with a moment where critical
   equipment is lost, damaged, or buried in the sand → fixes the lack of stakes
   and creates an emotional low point.
2. SCENE 6: replace the general panel brushing with the uncovering of a
   specific, mysterious artifact or mechanism → fixes the lack of narrative
   escalation and gives the characters a goal.
3. SCENE 13: move to a position where they enter the ship and discover the
   interior is completely filled with sand → fixes the lack of a thematic
   payoff and provides a strong ending image.

## OUT-OF-SCOPE FLAGS

- Boot colors flip between black and white throughout the edit → CONTINUITY lens
- Backpacks vanish and reappear completely between scenes → CONTINUITY lens
- Hands phase directly through solid ladder rungs in S13 → FRAME lens

## FLAGS FOR DOCUMENT CHECK

- QUESTION: Is the intense repetition of brushing sand intended as a specific
  thematic choice (e.g. a Sisyphean task), or is it an artifact of limited
  prompting? — because it occupies 5 of the 13 scenes with no variation.
- QUESTION: Does the plan declare an emotional peak, and is it intended to be
  the scene at 1:10 (the fall)?
- QUESTION: Is the film's last planned scene the one on screen at 2:00, or is
  there a missing interior/payoff sequence?

## STORY TRACKING ROW

```
| (not supplied) Ⓥ ⚠️ ŞARTLI | YATAY | (not supplied) | 5/10 | 3/10 | 2/10 | 1/10 | 2/10 | N/A | 1/10 | 1/10 | 4/10 | 2/10 | 2.3/10 |
```
