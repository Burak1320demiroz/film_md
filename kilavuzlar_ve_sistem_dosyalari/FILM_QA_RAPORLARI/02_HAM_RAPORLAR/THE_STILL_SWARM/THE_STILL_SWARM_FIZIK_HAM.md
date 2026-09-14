# HAM RAPOR — THE STILL SWARM · ⑥ FİZİK (T6)

```
KÜNYE (operatör tarafından doldurulmadı — D160 ihlali)
girdi: <tam yol YOK> · <süre YOK> · <çözünürlük YOK>
işlendiği tarih: 02.09.2026 · işleyen kart: qa-isle
⛔ ⑪ ölçüm kapısı KOŞULAMADI (master verilmedi).
⛔ ① SPEC kapısı: THE_STILL_SWARM_QA_SPEC.md'nin C BLOĞU ⑥ için sayısal
   kilit listesi olarak yazılmıştı; rapor mod V koşuldu → NUMERIC LOCK
   VERIFICATION tablosu HİÇ üretilmedi, T6'ya satır YAZILMAZ [D129].
⛔ PREMISE REGISTER'a filmin NOVUM'u girmedi (yalnız "zero-g" yazıldı) →
   ⑩ ÖNERME KAPISI'nda üç kategorinin kesintisi düşer; film kaydına bakınız.
```

---

INPUT MODE: V
FILM: THE STILL SWARM
RUNTIME: 02:14 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 13 · CUTS COUNTED: 13
NON-SCENE MATERIAL: 2:10–2:14 Title card "THE STILL SWARM"
LINES HEARD: none — nothing audible to me
GRAVITY: Microgravity (0 g) — floating space environment across all scenes
PREMISE REGISTER: Zero-gravity / microgravity orbital space environment — objects, debris, and human figures float indefinitely unless acted upon by an external force.

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  8
SUM OF SCORES:      50.0
DIVISION:           50.0 ÷ 8 = 6.3

OVERALL SCORE: 6.3/10
VERDICT: MINOR SLIPS

PHYSICS LEDGER
#    Timecode    Event    Duration (measured)    Distance (est. + RULER)    Implied value    Consistent with?
L1    0:00–0:09    Shuttle drifting left in background    9.0 s    ≈15 m (shuttle length ≈10 m)    v ≈ 1.6 m/s constant    Microgravity premise
L2    0:20–0:25    Astronaut touches & pushes floating metal plate    5.0 s    ≈0.8 m displacement    Plate moves, astronaut zero recoil    Newton's 3rd Law violation
L3    0:50–0:58    Thruster gas sprayed from hand tool into vacuum    8.0 s    ≈1.5 m plume radius    Swirling atmospheric plume in space vacuum    Fluid physics break
L4    1:00–1:08    Astronaut floating past floating metal clamp    8.0 s    ≈2.5 m (astronaut height ≈1.7 m)    v ≈ 0.3 m/s constant drift    Microgravity premise
L5    1:20–1:28    Astronaut pulls tether hard; tether snaps/slips    8.0 s    ≈0.6 m recoil displacement    Body recoil v ≈ 0.5 m/s, rotational torque    Real momentum physics
L6    1:30–1:38    Astronaut holds metallic cargo box    8.0 s    Fixed position    Zero inertia felt in arms/torso during pivot    Mass/Inertia mismatch
L7    1:50–1:56    Astronaut pushes cargo box away in open space    6.0 s    Box: ≈1.2 m, Astronaut: ≈0.25 m    Box v ≈ 0.2 m/s, Astronaut v ≈ 0.04 m/s (Mass ratio ~5:1)    Momentum conservation

GRAVITY ESTIMATE: 0.0 m/s² (Microgravity / Zero-G environment verified across all 13 scenes).

NUMERIC LOCK VERIFICATION — MODE D ONLY
Mode V run — Lock list empty. Section omitted per rubric.

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Gravity & Free Fall    N/A    Declared absence: Microgravity environment throughout; no free fall drops occur
2    Ballistics & Trajectories    6/10    -4 · L3 (0:52), gas plume exhibits fluid drag curves in a vacuum
3    Impact & Momentum    5/10    -5 · L2 (0:22), metal plate accelerated with zero equal-and-opposite recoil on astronaut
4    Material Behaviour    6/10    -4 · L3 (0:54), pressurized gas plume forms billowing atmospheric cloud in vacuum
5    Particles & Atmosphere    5/10    -5 · L3 (0:56), thruster vapor swirls and lingers instead of expanding isotropically
6    Scale & Measurement    7/10    -3 · L1 vs L4 (0:02 vs 0:35), sphere structure relative scale varies against astronaut ruler
7    Rates & Timing    8/10    -2 · L1 vs L4 (0:05 vs 1:05), drift velocity of surrounding debris field slightly changes
8    Light & Shadow Physics    7/10    -3 · L2 vs L6 (0:24 vs 0:54), key directional sunlight angle on visor shifts by ~30°
9    Human Biomechanics    6/10    -4 · L6 (1:32), astronaut maneuvers ~20 kg metallic box without body counter-balance

PRESENCE STRING
1111111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 3

GRAVITY TABLE — every measured fall
Ledger row    Timecode    Height (est. + ruler)    Time    Implied g    vs film's g
—    —    No falls present (0 g environment)    —    0.0 m/s²    0.0 m/s²

RATE TABLE — every rate measured twice
Rate    First measure (timecode)    Second measure (timecode)    Verdict
Shuttle drift speed    0:02 (v ≈ 1.6 m/s)    0:08 (v ≈ 1.6 m/s)    Holds
Box drift after push    1:52 (v ≈ 0.20 m/s)    1:56 (v ≈ 0.19 m/s)    Holds

CONTRADICTION LOG
Ledger rows    Timecodes    Cat.    What contradicts what    Severity
L2 vs L7    0:22 vs 1:52    3    L2 push yields zero astronaut recoil; L7 push yields proper reactive recoil    🟠
L3 vs Vacuum    0:52    5    Gas spray exhibits atmospheric aerodynamic swirling in zero-atmosphere vacuum    🟠

THE THREE THAT MATTER
Gas Plume Swirling in Space Vacuum (0:50–0:58): Pressurized thruster gas forms billowing, atmospheric-style smoke rather than instantly expanding straight into the vacuum of space.

Missing Reaction Force on Plate Push (0:20–0:25): Pushing a heavy metal plate causes the plate to drift away without pushing the floating astronaut backward, breaking Newton's Third Law.

Massless Handling of Cargo Box (1:30–1:38): Rotating a heavy metallic crate shows no inertial resistance in the astronaut's wrists, arms, or torso posture.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Gas plume swirling (0:50–0:58)    Trim shot early before gas cloud billows    Cheap
Plate push recoil (0:20–0:25)    Recut shot to trim contact frame or replace plate motion    Moderate
Cargo box mass handling (1:30–1:38)    Accept or regenerate S10 with realistic inertial drag    High

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Thruster spray behavior (0:52)    Is there a localized magnetic or atmospheric field surrounding the structure, or should gas expand as a vacuum plume?

OUT-OF-SCOPE FLAGS
none
