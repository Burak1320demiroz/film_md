# THE BLACK CRADLE — VIDEO_QA (TEKNİK) HAM RAPOR

> **Tarih:** 17.08.2026 · **Rubrik:** `QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> **Mod:** V — ⛔ SPEC planda hazırdı (`THE_BLACK_CRADLE_PLAN.md` §QA SPEC BLOĞU),
> rubriğe verilmedi → **ÖN KOŞU** [D94, 6. vaka]
> **Malzeme:** 3:52 (232 s) kurgu · rapor 21 kesme saydı
> ⛔ Model çıktısı olduğu gibi. Belge cevapları ve kilit çelişkisi defteri film kaydında:
> `../01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`
> ⚠️ Rapor **OVERALL SCORE, VERDICT ve tracking row üretmedi** — kategori 10 sonrası
> yalnız kutu listesi + FLAGS geldi; kategori 11 (Motion Quality) hiç yazılmadı.

---

```
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically believable?" It does NOT answer "does this clip match its design document."

STEP 1 — MODE V BASELINE
MATERIAL
  What you were given: compilation edit · duration 3:52 (232 s)
  Cuts you can see:    21 visible hard cuts across multiple scenes (e.g., 0:07, 0:17, 0:27, 0:37, 0:47, 0:57, 1:08, 1:17, 1:27, 1:37, 1:47, 2:07, 2:17, 2:27, 2:37, 2:48, 2:53, 2:57, 3:07, 3:15, 3:32)
  Aspect ratio:        16:9

THE CHARACTER — as first clearly seen
  Face / hair / marks: Male astronaut (bearded/stubble, short dark hair) & Female astronaut (short blonde hair) · First frame fully visible: 0:17
  Suit / wardrobe:     Dark matte tactical suits; male suit features orange accent lines/piping, female suit features teal/cyan accent lines
  Wear / dirt:         Clean, smooth suit surfaces; minor dust/weathering near boots on planetary surface
  Equipment:           Clear bubble helmets with integrated neck-ring seals, illuminated internal visors, portable sampling drill, hard-shell flight cases

THE WORLD — as the footage shows it
  Gravity read:     Low-gravity surface environment (slow dust settling, floaty movement) transitioning to zero-g space/orbit operations
  Atmosphere read:  Airless/thin atmospheric surface (dark sky with stars, visible dawn light horizon); hard vacuum in space sequences
  Light sources:    Ship exterior landing lights, horizon dawn light, cockpit panel ambient glow, external thruster plumes, distant stars/sun
  Location:         Extraterrestrial planet/moon surface, ship cockpit interior, space orbit, hangar bay

MOTION
  Camera:  Compilation features static framing, slow forward pushes, exterior tracking shots, and orbital flybys
  Subject: Characters drilling, carrying cases, running, pilot controls, ship takeoff, docking/approach maneuvers

CRITIQUE REPORT

1. 🧑 CHARACTER CONSISTENCY

0:17 — 🟡 MINOR — Female character's hair length and facial structure soften slightly between close-up and medium shots.

0:48 — 🟠 MAJOR — Character running gait shows floating/gliding mechanics; feet slide on the ground surface rather than planting firmly.

1:08 — 🟠 MAJOR — Male character's facial features and age read alter slightly inside the cockpit framing compared to surface shots.

1:55 — 🟡 MINOR — Reflection on female visor drifts out of sync with head turn.

SCORE: 6/10

2. 📐 SCALE & PHYSICS

0:23 — 🟠 MAJOR — Dust kicked up by the drilling mechanism hovers in a uniform cloud rather than falling in parabolic arcs for low-gravity environment.

0:48 — 🟠 MAJOR — Running motion lacks proper inertia/weight transfer, producing lightweight sliding across terrain.

1:20 — 🟡 MINOR — Thruster exhaust smoke in vacuum/space sequence lingers as dense volume clouds instead of rapidly dispersing.

2:40 — 🟡 MINOR — Ship approach trajectory in zero-g displays unnatural damping without micro-thruster corrections.

SCORE: 6/10

3. 🎥 CAMERA & CINEMATOGRAPHY

Compilation edit containing 21 scene transitions. As per Mode V compilation rules without a plan file, cut boundaries are marked UNVERIFIABLE for plan matching.

1:37 — 🟡 MINOR — Subtle camera axis wobble during the orbital tracking shot.

2:37 — 🟡 MINOR — Lens focal perspective jumps slightly between exterior hangar opening frame and ship flyby.

SCORE: 7/10

4. 💡 LIGHTING & COLOR

0:08 — 🟡 MINOR — Harsh directional lighting on surface shows slight ambient fill bleed on pure shadow sides.

1:08 — 🟠 MAJOR — Cockpit interior displays inconsistent light source origins relative to exterior sun/horizon position.

1:48 — 🟡 MINOR — Slight AI bloom on ship accent lights and control panel displays.

SCORE: 6/10

5. 🌍 ENVIRONMENT & WORLD

0:01 — 🟡 MINOR — Metal surface texture on initial object displays subtle breathing/swimming before scene transition.

1:28 — 🟡 MINOR — Planetary horizon edge line flickers slightly during high-altitude flyby shot.

2:08 — 🟡 MINOR — Hangar bay interior truss structure details show minor geometry warping across frames.

SCORE: 7/10

6. 🦎 CREATURE DESIGN & MOTION

N/A — No creatures present in footage.

SCORE: N/A

7. 🔬 PARTICLE & MATERIAL PHYSICS

0:27 — 🟠 MAJOR — Dust generated during soil sampling floats in place like a 2D haze layer rather than reacting to directional force/gravity.

1:20 — 🟠 MAJOR — Rocket exhaust ejecta in vacuum creates lingering particle clouds that freeze momentarily before fading.

1:40 — 🟡 MINOR — Space debris/particles around thrusters lack continuous linear momentum vectors.

SCORE: 5/10

8. 🗣️ DIALOGUE & AUDIO

0:30 — 🟡 MINOR — Turkish spoken dialogue ("Şafak hattı 1200 metrede...") shows minor lip-sync drift behind clear helmet visor.

1:09 — 🟠 MAJOR — Dialogue line ("Kalkıyoruz. Sıkı tutunun...") spoken on-screen exhibits noticeable lip-sync lag (~0.4s).

1:45 — 🔴 BLOCKER — Audible atmospheric thruster roar and engine rumble during hard vacuum space flight sequences.

SCORE: 5/10

9. 🔗 FRAME ANCHOR FIDELITY

UNVERIFIABLE — Requires pipeline start/end anchor images.

SCORE: N/A

10. 🚫 NEGATIVE BIBLE VIOLATIONS
[ ] Any visible CUTS or TRANSITIONS (N/A in Compilation Mode)

[ ] Shaky/handheld camera feel

[ ] Miniature/toy-like appearance

[ ] CGI/video game/Unreal Engine aesthetic

[ ] Airbrushed, waxy, or plastic skin texture

[ ] Oversaturated or neon colors

[ ] Horror/threatening tone

[ ] Text, subtitles, captions, or watermarks visible on screen

[x] AI bloom / soft glow filter / dreamy haze on light sources (Observed at 1:48)

[x] Unmotivated ambient fill in a scene where fill light is forbidden (Observed at 0:08)

[ ] Face morphing

[ ] Object phasing/clipping

[ ] Creature sliding

[x] Warped or autonomous reflections (Observed at 1:55)

[x] Melting or morphing terrain/geology (Observed at 0:01, 2:08)

[ ] Duplicate characters

[x] Frozen or static particles (Observed at 0:27, 1:20)

[x] Floating particles without gravitational cause (Observed at 0:23)

[ ] Zero-g objects hanging without momentum

[ ] Rigid floating character

[ ] Hand geometry breakdown near glowing surfaces

[ ] Rope/tether clipping through walls or surfaces

[ ] Ship/structure proportion shifts between shots

[ ] Tilt angle drift

FLAGS FOR DOCUMENT CHECK
Is the sound design intended to be stylized/audible in vacuum for cinematic effect, or strict hard sci-fi physics?

Are character running/walking physics on surface intended to represent ultra-low gravity locomotion?
```
