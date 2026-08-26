# 🖼️ THE ROSE COAT — ⑤ ARKA PLAN HAM RAPORU (derin tarama)

> **Koşu:** 26.08.2026 · video-only (bu merceğin tek modu)
> **Rubrik:** `../../QA_PROMPTLARI/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md`
> ⛔ Aşağısı MODELİN ÇIKTISIDIR, düzeltilmemiştir.

---

```
FILM: (not supplied)
RUNTIME: 135s measured
SCENES OBSERVED: 13 · CUTS COUNTED: 13
NON-SCENE MATERIAL: 2:10-2:15 title card
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES:  6
SUM OF SCORES:      36.0
DIVISION:           36.0 ÷ 6 = 6.0

OVERALL SCORE: 6.0/10
VERDICT: FIELD DRIFTS BUT RECOVERABLE
```

## SUBJECTS EXCLUDED

```
S1  Sand pouring from wall slit          S8   Astronaut falling
S2  Two astronauts standing/walking      S9   Astronaut brushing pack
S3  Two astronauts walking               S10  Astronauts brushing large high panel
S4  Two astronauts walking               S11  Astronauts standing
S5  Astronaut brushing sand off other    S12  Astronaut brushing suit
S6  Astronauts brushing low panel        S13  Astronaut climbing ladder
S7  Astronauts climbing dune
```

## BACKGROUND INVENTORY

```
SCENE 1
MIDGROUND:   Pink geometric wall extending right.
FAR FIELD:   Flat concrete ground. Largest non-empty object: none — empty pink
             sky, upper half.
SKY/CEILING: Featureless pink haze.
FOCUS:       Wall sharp, sky infinite focus.
EDGES:       Right edge clips an adjacent structure.

SCENE 2
MIDGROUND:   Three-segment white cylindrical habitat with stairs.
FAR FIELD:   Rolling pink hills. Largest non-empty object: Hill line, bottom third.
SKY/CEILING: Hazy pink.       FOCUS: All sharp.        EDGES: Clean.

SCENE 3
MIDGROUND:   Half-buried white space shuttle, habitats on far left.
FAR FIELD:   Distant white spire/rocket. Largest non-empty object: Tiny rocket,
             center right.
SKY/CEILING: Hazy pink.       FOCUS: Midground sharp, far field slightly soft.
EDGES:       Left edge clips habitats.

SCENE 4
MIDGROUND:   Lander/rocket on legs.
FAR FIELD:   Flat desert. Largest non-empty object: Rocket hull, right half.
SKY/CEILING: Hazy pink.       FOCUS: All sharp.        EDGES: Clean.

SCENE 5
MIDGROUND:   Out-of-focus rocket lander far back left.
FAR FIELD:   Flat horizon. Largest non-empty object: None — empty desert/sky.
SKY/CEILING: Hazy pink.       FOCUS: Subject sharp, midground/far field soft.
EDGES:       Clean.

SCENE 6
MIDGROUND:   Rocket hull and leg struts.
FAR FIELD:   Flat desert. Largest non-empty object: Rocket hull, upper center.
SKY/CEILING: Hazy pink.       FOCUS: Sharp.            EDGES: Clean.

SCENE 7
MIDGROUND:   Massive rocket engine bells and mechanical struts.
FAR FIELD:   Flat desert. Largest non-empty object: Engine structure, upper right.
SKY/CEILING: Hazy pink.       FOCUS: Sharp.            EDGES: Clean.

SCENE 8
MIDGROUND:   Crater rim, rocket leg on the right.
FAR FIELD:   Horizon. Largest non-empty object: Rocket leg, right third.
SKY/CEILING: Hazy pink.       FOCUS: Sharp.            EDGES: Clean.

SCENE 9
MIDGROUND:   Rocket lander far right, ladder part.
FAR FIELD:   Horizon. Largest non-empty object: Rocket hull, right edge.
SKY/CEILING: Hazy pink.       FOCUS: Subject sharp, background soft.
EDGES:       Right edge clips rocket.

SCENE 10
MIDGROUND:   Rocket hull.
FAR FIELD:   Desert floor. Largest non-empty object: Rocket hull, full frame.
SKY/CEILING: None visible.    FOCUS: Sharp.            EDGES: Clean.

SCENE 11
MIDGROUND:   Rocket hull, blank screen/panel.
FAR FIELD:   Horizon, desert. Largest non-empty object: Rocket hull, center.
SKY/CEILING: Hazy pink.       FOCUS: Sharp.            EDGES: Clean.

SCENE 12
MIDGROUND:   Rocket hull, ladder.
FAR FIELD:   Desert. Largest non-empty object: Rocket hull, right half.
SKY/CEILING: Hazy pink.       FOCUS: Sharp.            EDGES: Clean.

SCENE 13
MIDGROUND:   Ladder, hatch.
FAR FIELD:   Rocket hull. Largest non-empty object: Rocket hull, full frame.
SKY/CEILING: None visible.    FOCUS: Sharp.            EDGES: Clean.
```

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
|:--:|---|:--:|---|
| 1 | Background Figure Integrity | N/A | no background figures |
| 2 | Background Figure Behaviour | N/A | no background figures |
| 3 | Crowd Count & Density | N/A | no crowds |
| 4 | Horizon & Topology | 5/10 | −5 · 0:30 (S4) vs 1:00 (S7) |
| 5 | Depth, Parallax & Scale | 7/10 | −3 · 0:50 (S6) vs 1:00 (S7) |
| 6 | Background Set & Props | 4/10 | −6 · 0:50 (S6) vs 1:30 (S10) vs 1:50 (S12) |
| 7 | Focus Honesty | 7/10 | −3 · 0:40 (S5) |
| 8 | Sky & Atmospherics | 6/10 | −4 · 0:20 (S3) |
| 9 | Frame Edges & Emergent Artifacts | 7/10 | no in-scope source |

## PRESENCE STRING

```
1111111111111
```

## SEVERITY TALLY

```
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 2
```

## FIELD DRIFT MAP

| Scene | Layer | First slip | Undeniable by | Recovered? |
|---|---|---|---|:--:|
| S7 | far | 1:00 | 1:10 (S8) | No |
| S10 | mid | 1:30 | 1:50 (S12) | No |

## COUNT LOG

| Group | Scene(s) | First clean count | Last clean count | Verdict |
|---|---|:--:|:--:|---|
| Habitat modules | S2 | 3 | 3 | Consistent |

## CONTRADICTION LOG

| Timecode A | Timecode B | Layer | Cat. | What contradicts what | Severity |
|---|---|---|:--:|---|:--:|
| 0:30 | 1:00 | Far | 4 | Terrain under rocket is flat hardpan at 0:30, large rolling dunes at 1:00. | 🟠 MAJOR |
| 0:50 | 1:30 | Mid | 6 | Rocket panel is low/square at 0:50, massive/high at 1:30. | 🟠 MAJOR |
| 1:30 | 1:50 | Mid | 6 | Hull is bare at 1:30, features a massive ladder at 1:50. | 🟠 MAJOR |
| 0:50 | 1:00 | Mid | 5 | Scale of rocket legs changes massively relative to ground between S6 and S7. | 🟡 MINOR |
| 0:20 | 0:20 (in-shot) | Far | 8 | Shuttle casts shadow left, sky gradient implies light from top/right. | 🟡 MINOR |

## THE THREE THAT MATTER

1. **Rocket Hull Geometry Shift** (0:50 vs 1:30 vs 1:50): The background rocket
   transforms entirely across scenes, gaining ladders and shifting panel sizes.
   Fix: Regenerate S10 and S12 to match the S6 hull layout.
2. **Terrain Topology Shift** (0:30 vs 1:00): The environment immediately
   surrounding the landing struts goes from a flat parking lot to deep sand
   dunes. Fix: Regenerate S7 and S8 on flat terrain.
3. **Scale Drift** (0:50 vs 1:00): The physical scale of the rocket base swells
   massively between cuts. Fix: Crop S7 slightly or regenerate to match scale.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|:--:|
| Rocket hull/ladder shifts | Regenerate S10/S12 to enforce matching background geometry | High |
| Terrain shifts to dunes | Regenerate S7/S8 to remove dunes | High |
| Light direction mismatch | Accept it (very subtle to casual viewers) | Low |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Habitats in S3 have a different window arrangement than S2. | Are these intended to be the same habitat modules, or a different cluster? |
| The rocket changes from having no ladder (S10) to having one (S12). | Does the plan document specify the rocket's layout? |

## OUT-OF-SCOPE FLAGS

- Boot colors flip between black and white throughout the edit → CONTINUITY lens
- Text spontaneously generates on subject backpack at 1:18 → FRAME lens
- Hands phase directly through solid ladder rungs at 2:02 → FRAME lens
- Subject slides/moonwalks across sand without lifting feet at 0:12 → FRAME lens
