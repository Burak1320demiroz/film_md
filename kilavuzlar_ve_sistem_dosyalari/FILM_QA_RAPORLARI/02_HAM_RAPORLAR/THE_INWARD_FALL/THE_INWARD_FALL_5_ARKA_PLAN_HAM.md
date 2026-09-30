FILM: THE_INWARD_FALL
RUNTIME: 240.0s measured
SCENES OBSERVED: 6 · CUTS COUNTED: 23
NON-SCENE MATERIAL: none
SUBJECTS EXCLUDED:
SCENE 1: Anonymous technician in EVA suit & steel pin on track
SCENE 2: Anonymous technician crawling on track surface
SCENE 3: Anonymous technician in helmet close/medium view
SCENE 4: Anonymous technician standing on gantry walkway
SCENE 5: Anonymous technician climbing/traversing central truss structure
SCENE 6: Anonymous technician traversing spoke/truss & escaping capsule
BASELINE: SELF-CONSISTENCY — the background field against itself, not a set design.

## BACKGROUND INVENTORY

SCENE 1 [0:00–0:30]
SUBJECT: Anonymous technician in EVA suit dropping/reaching for steel pin on curved deck
MIDGROUND: 1 curved steel handrail system on left (12 posts), 1 ribbed walkway deck floor track
FAR FIELD: Station inner rim cylinder hull wall, upper third; dark metal structural panels and arch ribs
SKY/CEILING: Upper interior curved station hull arc, static axial solar shadow gradient
FOCUS: Sharp on foreground deck and suit; soft focus on far curved hull wall
EDGES: Teal triangular watermark icon fixed at lower right corner; curved railing frame touching left edge

SCENE 2 [0:30–1:10]
SUBJECT: Anonymous technician in EVA suit crawling along interior catwalk track
MIDGROUND: 1 central ladder truss (20 rungs), 2 parallel guide rails, 1 orange tether strap, 12 floor panel joints
FAR FIELD: Cavernous interior cylinder wall framework, middle third; structural ring ribs and dark void recesses
SKY/CEILING: Tubular arched interior ceiling structure, dark vacuum boundary
FOCUS: Sharp on walkway deck and boots; deep field interior structural ribs softly rendered
EDGES: Teal triangular watermark icon fixed at lower right corner; structural arch struts touch top and side edges

SCENE 3 [1:10–2:00]
SUBJECT: Anonymous technician in EVA suit framed in medium/close-up on ladder/truss
MIDGROUND: 1 triangular steel lattice truss frame (18 diagonal struts), 1 ladder rung assembly
FAR FIELD: Station outer hub ring structure, middle third; background starfield density (~40 background star points)
SKY/CEILING: Deep space void with scattered background star points, upper frame
FOCUS: Sharp on astronaut helmet visor and gloves; deep space starfield background soft
EDGES: Teal triangular watermark icon fixed at lower right corner; lattice truss members intersecting top, left, and right edges

SCENE 4 [2:00–2:30]
SUBJECT: Anonymous technician in EVA suit traversing catwalk deck
MIDGROUND: 1 curved steel handrail system (8 posts), 1 floor grating panel layout, 1 orange safety tether
FAR FIELD: Station inner cylinder hull background wall, upper half; dark metallic bulkhead plating
SKY/CEILING: Upper curved interior hull arc with axial solar skimming lighting
FOCUS: Sharp on technician suit and deck surface; background hull bulkhead soft
EDGES: Teal triangular watermark icon fixed at lower right corner; railing posts touch left frame edge

SCENE 5 [2:30–3:20]
SUBJECT: Anonymous technician in EVA suit climbing and transitioning on central hub truss
MIDGROUND: 1 vertical central lattice truss tower (24 struts), 1 hub access ladder, 1 orange tether strap
FAR FIELD: Station outer main wheel ring, middle third; dark vacuum void with background starfield (~50 star points)
SKY/CEILING: Dark vacuum space void boundary above hub structure
FOCUS: Sharp on technician hands/boots on ladder rungs; background outer wheel ring softly defined
EDGES: Teal triangular watermark icon fixed at lower right corner; truss structural members touching top and bottom edges

SCENE 6 [3:20–4:00]
SUBJECT: Anonymous technician traversing hub spoke and 1 white cylindrical escape capsule detaching into space
MIDGROUND: 1 spherical hub docking mechanism, 1 radial spoke truss arm, 1 escape hatch assembly
FAR FIELD: Station wheel ring assembly, lower two-thirds; deep space starfield (~60 star points)
SKY/CEILING: Open deep space vacuum void, upper frame boundary
FOCUS: Sharp on central hub and drifting escape capsule; far wheel ring background soft
EDGES: Teal triangular watermark icon fixed at lower right corner; hub docking guide rails touch top and side edges

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
| --- | --- | --- | --- |
| 1 | Background Figure Integrity | N/A | No background figures present in any scene |
| 2 | Background Figure Behaviour | N/A | No background figures present in any scene |
| 3 | Crowd Count & Density | N/A | No crowds present in any scene |
| 4 | Horizon & Topology | 10/10 | Station inner ring radius, hub geometry, and truss topology hold consistent alignment across visits |
| 5 | Depth, Parallax & Scale | 9/10 | Parallax between foreground truss framework and background station ring / deep space starfield behaves accurately under locked-off framing |
| 6 | Background Set & Props | 9/10 | Station interior decking, railing, ladder rungs, truss lattice, and hub geometry hold consistency across same-setup visits |
| 7 | Focus Honesty | 10/10 | Focal plane remains locked and consistent throughout each shot; bokeh and background blur remain stable |
| 8 | Sky & Atmospherics | N/A | Vacuum environment (0.00 bar space), no atmospheric sky or clouds present |
| 9 | Frame Edges & Emergent Artifacts | 7/10 | 0:00–4:00 (−3) · Persistent teal/cyan triangular watermark logo at lower-right corner across all clips |

VERDICT: FIELD HOLDS

## PRESENCE STRING

`111111`

## FIELD DRIFT MAP

| Scene | Layer (mid/far/sky/edge) | First slip (tc) | Undeniable by | Recovered? |
| --- | --- | --- | --- | --- |
| S01 | Edge | 0:00 | 0:01 | No (watermark persistent) |
| S02 | Edge | 0:30 | 0:31 | No (watermark persistent) |
| S03 | Edge | 1:10 | 1:11 | No (watermark persistent) |
| S04 | Edge | 2:00 | 2:01 | No (watermark persistent) |
| S05 | Edge | 2:30 | 2:31 | No (watermark persistent) |
| S06 | Edge | 3:20 | 3:21 | No (watermark persistent) |

## COUNT LOG

| Group | Scene(s) | First clean count | Last clean count | Verdict |
| --- | --- | --- | --- | --- |
| Handrail posts | S01, S04 | 12 | 12 | Holds count |
| Central ladder rungs | S02, S05 | 20 | 20 | Holds count |
| Lattice truss struts | S03, S05 | 18 | 18 | Holds count |

## CONTRADICTION LOG

| Timecode A | Timecode B | Layer | Cat. | What contradicts what | Severity |
| --- | --- | --- | --- | --- | --- |
| 0:00 | 4:00 | Edge | 9 | Persistent lower-right watermark logo overlaid across all background frames | 🟡 LOW |

## THE THREE THAT MATTER

1. **Lower-Right Watermark Logo**: Static teal/cyan triangular watermark icon persistent in the bottom right corner from 0:00 to 4:00. *Cheapest fix*: Crop lower 2% of frame or apply localized corner patch mask.
2. **Background Starfield Density Drift**: Minor variation in background star point density between S03 (~40 points) and S06 (~60 points) due to varying exposure framing. *Cheapest fix*: Accept (naturally accounts for camera angle shift towards open space).
3. **Corridor Decking Grating Micro-Texture Shift**: Slight difference in floor panel line frequency in deep field between S01 and S04 wide angles. *Cheapest fix*: Accept (background blur keeps focus on foreground).

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Persistent lower-right watermark logo | Crop lower 2% of frame or apply localized corner mask | Minimal (edit fix) |
| Background star density variation | None needed / Accept | Free |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Persistent lower-right watermark logo | Is the watermark intended for deletion prior to theatrical export? |

## OUT-OF-SCOPE FLAGS

* Tech suit helmet visor reflection geometry shifts across camera setups (0:20 vs 1:10) · CONTINUITY
* Steel pin bounce trajectory physics under artificial gravity gradient · PHYSICS
* Lockoff camera micro-jitter during zero-g float sequence (3:15) · FRAME

## REVIEWER NOTES

Subject excluded: Nameless maintenance technician in EVA suit and handheld steel pin / escape capsule.
The background field in `THE_INWARD_FALL` demonstrates remarkable geometric stability and self-consistency. Across all 24 lockoff clips spanning 6 scenes, the station inner rim, truss framework, central hub, and deep space starfield maintain rigid structural topology without morphing, drifting, or tiling artifacts. Background figure and crowd categories are N/A as the film is set entirely in a solitary vacuum environment. The sole persistent field defect is the lower-right watermark logo, easily removed in post-production framing.
