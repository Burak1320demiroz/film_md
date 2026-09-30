FILM: THE_LAST_TOW
BOLUM: PART 1 (BÖLÜM 1 · K01–K24 · S01–S06)
NOT: Bu koşuda yanlışlıkla THE_STATIC_VEIL_QA_SPEC.md yapıştırılmıştır. Bu nedenle dik duran anahtar (soğuk kaynak novum'u) imkânsız nesne sanılmış ve 240 saniyelik süre 120 saniyelik plana göre kurgu hatası sayılmıştır. Doğru SPEC (THE_LAST_TOW_QA_SPEC.md) ile yeniden koşulmalıdır.

FORMAT: YATAY

INPUT MODE: D — SPEC block pasted.
BASELINE: AGAINST DOCUMENT (mode D)
FILM: THE_STATIC_VEIL
FORMAT: YATAY         ASPECT MEASURED: 16:9
LENGTH CLASS: 2 dk
SCENE: Compilation
VIDEO DURATION: 240.0 s measured
MATERIAL TYPE: FILM
CUTS COUNTED: 23 (0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50)
NON-SCENE MATERIAL: none
LINES HEARD: none — nothing audible to me
SPEC BLOCK PROVIDED: yes

## SCORES SUMMARY

| Category | Score | Critical Issues |
| --- | --- | --- |
| Character | 4/10 | −3 · 0:30 (🔴), −3 · 0:40 (🟠) |
| Scale & Physics | 4/10 | −3 · 0:00 (🔴), −3 · 3:50 (🟠) |
| Camera | 3/10 | −4 · 0:40 (🔴), −3 · 1:20 (🟠) |
| Lighting | 3/10 | −3 · 1:20 (🟠), −2 · 1:30 (🔴), −2 · 3:00 (🔴) |
| Environment | 4/10 | −3 · 0:10 (🔴), −3 · 1:00 (🔴) |
| Creatures | N/A | none |
| Particles & Materials | 4/10 | −3 · 0:30 (🔴), −3 · 2:00 (🔴) |
| Dialogue & Audio | N/A | none |
| Frame Anchor Fidelity | N/A | none |
| Negative Violations | 4 count | 1:00, 1:30, 2:00, 3:00 |
| Motion Quality | UNVERIFIABLE | (video provided as stills, motion unclear) |
| Vertical Format (9:16) | N/A |  |
| Safe Zone | N/A |  |
| Hook Timing | N/A |  |

VERDICT: REGENERATE

## PRESENCE STRING

`--1111111111---111111111`

## TOP 3 CRITICAL ERRORS

1. 0:30 — 🔴 — Suit mismatch: Visor is entirely transparent revealing a human face, and an interior helmet light is on, violating SPEC "altın aynalı küresel yansıtıcı vizör" and "kask içi ışık yok".
2. 0:40 — 🔴 — Screen direction violation: Astronaut is walking right-to-left, directly violating the 12/12 SPEC lock "astronot soldan sağa ilerler".
3. 2:00 — 🔴 — Particle physics: Sparks and glowing particles hang and slowly drift in mid-air (zero-g behavior), violating the requested 0.16 g gravity specification where they should fall downward.

## DETAILED ERROR LOG

0:00 — 🔴 — Scale & Physics — Object physics: Wrench stands perfectly vertical on its head on a flat plate without support, which is physically impossible.
0:10 — 🔴 — Environment & World — Environment morph: Massive vertical metal plates and structures appear instantly in the background, completely absent in the 0:00 shot of the exact same location.
0:30 — 🔴 — Character Consistency — Suit mismatch: Visor is transparent revealing a human face, and interior helmet light is present (violates SPEC).
0:30 — 🔴 — Particles & Materials — Material physics: Cutting torch emits smoke and an atmospheric flame that dissipates as if in air, violating the 0 Pa vacuum.
0:40 — 🔴 — Camera & Cinematography — Screen direction violation: Astronaut is walking right-to-left, violating SPEC "astronot soldan sağa ilerler" (Repeated at 2:30, 2:40).
0:40 — 🟠 — Character Consistency — Suit missing detail: Left arm pressure gauge is absent (violates SPEC "sol kolda basınç saati").
1:00 — 🔴 — Environment & World — Text/Symbols: AI-generated letters and runes are visibly embossed on the rim of the circular hatch.
1:20 — 🟠 — Lighting & Color — Lighting consistency: The astronaut's shadow falls to the left, directly contradicting the right-falling shadow established in the opening shots.
1:20 — 🟠 — Camera & Cinematography — Compilation cut error: Video continues past the 120.0 s RUNTIME plan defined in the grid, resulting in 12 un-planned scene boundaries.
1:30 — 🔴 — Lighting & Color — Unmotivated fill: Strong atmospheric light beam and haze visible in the background space, violating SPEC "0 Pa (sert vakum, hava sürtünmesi ve saçılma yok)".
2:00 — 🔴 — Particles & Materials — Particle physics: Sparks and glowing particles hang and float slowly in mid-air (zero-g behavior), violating the 0.16 g gravity.
3:00 — 🔴 — Lighting & Color — AI Bloom: Soft glowing atmospheric haze surrounds the ground line and pulled object, scattering light into the environment despite being in a hard vacuum.
3:50 — 🟠 — Scale & Physics — Tether physics: The sled tether is completely rigid and hovers horizontally in the air instead of sagging naturally under gravity.

## WHAT WORKED WELL

* The spacesuit's rigid chest piece and dark grey bellows joints correctly adhere to the SPEC instructions ("sırtsız düz gövde, koyu gri körük eklemler").
* The background sky is rendered as pitch black in multiple scenes, successfully anchoring the lunar aesthetic.

## PROMPT IMPROVEMENT SUGGESTIONS

ADD to video prompt: "gold mirrored opaque visor, reflection only, absolutely no face visible" → prevents transparent visor and internal light issues.
ADD to video prompt: "astronaut moving exclusively from left to right, facing right" → prevents screen direction violation.
REMOVE "cinematic lighting" → prevents atmospheric scattering, unmotivated fill, and bloom in a vacuum environment.

## NEW LESSON CANDIDATE

No new lesson — all errors map to patterns 3 (bloom), 5 (particles), 9 (structure shift), and 11 (text).

## OUT-OF-SCOPE FLAGS

none

### 10. 🚫 NEGATIVE BIBLE VIOLATIONS (Yasak İhlalleri) — a COUNT, not a score

[ ] cut/transition inside a single clip     [ ] handheld shake / drift
[ ] miniature/toy look · CGI/game aesthetic [ ] airbrushed, waxy, plastic skin
[ ] oversaturated/neon colour               [ ] horror tone (unless specified)
[ ] text, subtitles, captions, watermark — a static corner mark in every scene counts; never set dressing
[x] characters on the scene's own materials: letters, digits, units, scale marks, survey markers on rock, ground, hull, panel
[x] AI bloom / dreamy haze                  [x] unmotivated fill where forbidden
[ ] face morphing                           [ ] solid passing through solid
[ ] creature sliding                        [ ] warped/autonomous reflections
[ ] melting terrain / swimming rock texture [ ] duplicate character
[x] frozen/static/causeless-floating particles · zero-g objects without momentum · rigid floating character
[ ] hand breakdown near glowing surfaces · extra fingers · hand-surface fusion
[ ] rope clipping through surfaces          [ ] structure proportion shift · tilt drift
[ ] low-density impact spray · frame-rate variance
[ ] walking/standing where tethered movement is specified
[ ] airborne sound in vacuum · overlapping dialogue · invented on-screen speaker
COUNT total violations: 4
NEGATIVE BOX COUNT: 4 · LINKED FINDINGS: 4 · UNLINKED: 0
FINDINGS WITH A MATCHING BOX: 4 · TICKED: 4 · MISSED: 0
