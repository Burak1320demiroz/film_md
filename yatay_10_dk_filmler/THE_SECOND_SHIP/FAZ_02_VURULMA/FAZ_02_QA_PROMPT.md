# 🔍 FAZ 2 / VURULMA — VİDEO ELEŞTİRİ PROMPTU

## On sahne · 1 dakika 40 saniye · 16:9 · faza özel rubrik

> **Ne işe yarar:** Faz 2'nin on sahnesi (S11–S20 · 1:40–3:20) birleştirilip
> tek video olduğunda, o videoyu bu fazın KENDİ kilitlerine karşı denetler.
> Faz 1 rubriğiyle aynı iskelet, farklı SPEC.
>
> **Faz 1'den farkı — bu faz HASARI YARATIYOR.** Üç kalıcı işaret bu on
> sahnede doğuyor ve doğdukları andan sonra bir daha hiç değişmiyor:
> delik (S13'ten), 4° yatıklık (S17'den), çöken sağ ayak + oluk (S19'dan).
> Rubriğin en değerli işi bu üç işaretin **doğru sahnede doğup**
> sonrasında sabit kalıp kalmadığını ölçmek.
>
> **KULLANIM (07.08.2026 ikinci revizyon):** Elinde fazın 10 sahnesi 10
> AYRI dosya olarak duruyor — birleştirmene GEREK YOK, bloğu doldurmana
> da GEREK YOK.
>
> 1. Gemini'ye **10 klibi SIRAYLA yükle: önce S11, en son S20.**
>    Dosya adında sahne numarası varsa (örn. `s13.mp4`, `sahne_17.mp4`)
>    sıra şaşsa bile model adı esas alır — en sağlamı ikisi birden:
>    doğru ad + doğru sıra.
> 2. Aşağıdaki kod bloğunun **içini** olduğu gibi kopyala, videolarla
>    birlikte gönder. İlk satır `AUTO` kalır — model kaç dosya aldığına
>    bakıp modu kendisi seçer.
>
> Üç mod otomatik ayrılır: **10 dosya** → on-klip denetimi (senin akışın)
> · **tek ~100 s dosya** → birleştirilmiş reel · **tek ~10 s dosya** →
> tek sahne (yalnız bu durumda ilk satıra `S13` gibi sahne yazman
> gerekir, yoksa model sormadan durur).
>
> **Rapor geldiğinde:** ham çıktıyı
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/`
> altına `THE_SECOND_SHIP_FAZ02_HAM.md` olarak kaydet. ⛔ Faz ölçümüdür,
> film ölçümü değil — skoru `03_HIKAYE` / `04_MANTIK` / `06_KARAKTER`
> tablolarına yazma, `00_INDEX` sayacına da girmez.

---

## PROMPT — buradan aşağısı kopyalanır

```
AUDIT TARGET: AUTO    <- leave as AUTO. Only change this to a scene id
                         (e.g. "S13") when you upload exactly ONE short
                         clip and want just that scene audited.

ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing material from the second phase of a 100-scene
science fiction film. You judge the PICTURE. You are precise, specific and
unsentimental. You never soften a finding and you never invent one.

WHAT YOU HAVE

- Video material: normally TEN separate clips of about 10 seconds each -
  the ten scenes of this phase, S11 through S20. It may instead be one
  single 100-second reel, or one single scene clip.
- The LOCKED SPEC below. It is ground truth, not a suggestion. Everything
  you need to judge this material is in it. You were not shortchanged on
  input: do not ask for a bible, a plan or a script, and do not treat
  their absence as a defect of the production.


⛔ STEP -1 — MATERIAL GATE AND MODE SELECT (do this before anything else)

Count the video files you were actually given and measure each one.
Then pick the mode:

MODE T (TEN CLIPS) - you received 8 to 10 separate clips, each about
    8-12 seconds. This is the normal delivery. Proceed in TEN-CLIP mode
    (mapping rules in STEP 0.5). If you received 8 or 9 clips, audit the
    ones you have and list plainly which scene slots have no clip -
    without treating the gap as a defect of the clips themselves.

MODE R (ONE REEL) - you received exactly ONE video of 100 seconds
    (+/- 3) containing about 10 scene-length segments. Proceed in
    FULL-REEL mode.

MODE S (ONE SCENE) - you received exactly ONE clip of 8-12 seconds.
    This mode needs the AUDIT TARGET line above to name the scene
    (S11..S20). If it does, audit that one scene. If it still says AUTO,
    output only:
        SINGLE CLIP RECEIVED, TARGET UNKNOWN - one ~10 s clip was
        uploaded but no scene id was declared. Fill AUDIT TARGET with
        one of S11..S20 and run again.
    Then stop. Never guess the scene from the picture alone.

NO MATCH - anything else (e.g. one 30 s file, three clips, an empty or
    unreadable file). Output only:
        MATERIAL GATE FAILED - received __ file(s), durations: __.
        Expected ten ~10 s clips, or one ~100 s reel, or one declared
        single scene.
    Then stop.

Whatever mode you land in, write the mode and the file count into the
MATERIAL section of your report.


⛔ STEP 0 — CUTS: WHAT IS LEGITIMATE AND WHAT IS A FINDING

Each of the 10 scenes was generated as a SEPARATE clip.

MODE T: there are no boundaries at all - every file is one scene. Any
    cut, camera reset, angle jump, sudden reframe or teleport INSIDE any
    clip is a finding at maximum severity.

MODE R: the reel is a compilation of those clips laid end to end, so a
    cut at every 10-second boundary (0:10, 0:20, ... 1:30) is REQUIRED
    BY THE ARCHITECTURE. NEVER report a cut, angle change, location
    change or lighting change AT a boundary as an error, hidden cut,
    continuity break or blocker. DO report, at maximum severity, any cut
    or camera reset INSIDE a 10-second segment.

MODE S: same as MODE T, for the one clip.

In every mode: each scene is one unbroken take with at most one camera
movement at one constant rate.


⛔ STEP 0.5 — SCENE MAPPING

This is the SECOND phase of the film: scenes S11 through S20.

MODE T mapping - in this order of precedence:
    1. If a clip's FILENAME contains a number from 11 to 20 (e.g.
       "s13.mp4", "sahne_17.mp4", "faz2_S15.mp4"), that number is its
       scene id. Filenames win over upload order.
    2. Otherwise, upload order maps 1:1 - first clip = S11, second =
       S12, ... tenth = S20.
    Print the mapping you used as a CLIP MAP table before any finding.
    If two clips claim the same scene id, or a filename number falls
    outside 11-20, say so in MATERIAL and fall back to upload order for
    the clips in conflict.
    ⚠️ Mapping check: if a clip's CONTENT plainly contradicts its
    mapped row (e.g. the clip mapped to S13 shows two seated figures,
    not a hull track), do NOT silently remap. Report it as a finding:
    "clip mapped to S13 does not match its row - content resembles the
    S12 row" and audit it against the row it is MAPPED to. Misfiled
    clips must surface, not be quietly corrected.

MODE R mapping - reel time maps to scenes like this:
    S11 = 0:00-0:10   S12 = 0:10-0:20   S13 = 0:20-0:30   S14 = 0:30-0:40
    S15 = 0:40-0:50   S16 = 0:50-1:00   S17 = 1:00-1:10   S18 = 1:10-1:20
    S19 = 1:20-1:30   S20 = 1:30-1:40

MODE S - every timecode is clip-relative (0s-10s), every finding is
prefixed with the declared scene id, and you audit only that scene's row
plus the global locks.

In MODE T and MODE S, timecodes are seconds within the clip (e.g.
"S14 at 6s"). In MODE R, timecodes are reel time (m:ss).
Never renumber scenes to S1-S10. Never invent a scene outside S11-S20.
EVERY finding carries a timecode and a scene number, or it is deleted
before you output it.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before you compare anything against the spec, write down what you ACTUALLY
SEE, in your own words, for each of these:
    - the woman (face, hair, suit colour accents, build)
    - the man (face, hair, suit colour accents, build)
    - the cockpit interior
    - the ship seen from outside: shape, proportions, and every mark of
      damage you can see, scene by scene

Only then compare against the LOCKED SPEC. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


================================================================
LOCKED SPEC — FAZ 2 / VURULMA (THE HIT)
================================================================

FORMAT
    10 scenes, exactly 10.0 s each, 100 s total, 16:9 horizontal.
    Every scene is a single unbroken take with 0 internal cuts.
    Maximum one camera movement per scene, at one constant rate.

WHAT HAPPENS IN THIS PHASE
    The ship is shot down. A structure on the planet fires a single line
    that punches one hole through the ship; the crew survives, loses its
    navigation core, and lands hard. The phase ends with ten seconds in
    which nothing happens at all.

AUDIO
    All 10 scenes were generated SILENT. Dialogue, the impact, the radio
    and all atmosphere are added in post-production. Never grade lip-sync
    against the soundtrack. Never report "no audio", "silent impact" or
    "mouth moves but no sound" as a defect. Judge lips ONLY against the
    WHO SPEAKS column of the scene table.

LIGHT
    Night and space only. There is no daylight anywhere in this phase.
    Grey-blue moonlight reads about 7000K. Cockpit console light is a warm
    amber about 2800K. The only other light events allowed are: the white
    line (S11), one hard white sweep across the cabin (S12, at 2s), and
    the entry plasma (S17). Nothing else emits.

TEXT
    There is no readable text in this film at any point: no letters, no
    digits, no numerals, no glyphs, no icons, no labels, no insignia, no
    coordinates, no map grids, no HUD readouts, no subtitles, no captions,
    no title card, no end card, no credits, no watermark. Displays carry
    abstract light only. Any readable character anywhere is a finding.
    This lock is under the most pressure in S15 (a time window) and S18
    (a landing site), because both scenes are ABOUT information. Neither
    is allowed to write it down.


>>> THE DAMAGE CLOCK — the single most important thing in this phase <<<

    Three permanent marks are BORN in this reel. Each has an exact birth
    scene. Before its birth scene it must NOT exist. From its birth scene
    onward it must NEVER change, heal, worsen or move.

    MARK 1 - THE HOLE.  Born: the strike in S12, first seen in S13.
        A 1.2-meter PERFECTLY CIRCULAR hole through the upper surface of
        the RIGHT REAR cargo bay. Its edge is clean, smooth, glassy and
        faintly pearlescent. No burn marks, no soot, no torn metal, no
        bent plating, no debris, no radiating cracks. It is a cold,
        precise bore, not an explosion wound. Present in S13, S17, S19,
        S20 and in the interior in S14.

    MARK 2 - THE FOUR-DEGREE ROLL.  Born: S17.
        The hull carries exactly 4 degrees of right-hand roll from S17
        onward, and holds it for the rest of the film. In S13 the ship is
        still in LEVEL flight - a tilt in S13 is a finding.

    MARK 3 - THE COLLAPSED RIGHT LEG AND THE GROOVE.  Born: S19.
        On landing the rear legs strike together, then the RIGHT main
        landing leg collapses. The ship ends tilted right, resting on its
        remaining legs, with a drag groove behind it about 60 meters long.
        Present in S19 (as it happens) and S20 (at rest).

    NOTHING ELSE IS DAMAGED. The ship is not shattered, not burning, not
    venting, not sparking, not breaking up. The hull stays whole apart
    from the one hole. Any additional dent, tear, scorch, missing panel,
    broken antenna or secondary hole is a finding.


>>> THE WEAPON RULE - it is never drawn as a weapon <<<

    The structure's shot is A PERFECTLY STRAIGHT THIN WHITE LINE. It is
    not a beam, not a laser, not a bolt, not a blast.
    It must be: mathematically straight, constant in width, constant in
    brightness, white, silent, and rigid.
    It must NEVER: bend, curve, taper, flicker, pulse, crackle, branch,
    take on colour, glow with a halo, throw sparks, or have a muzzle
    flash, a recoil, a charging effect or a visible source weapon.
    If what you see reads as science-fiction weapon fire, that is a
    finding and its severity is high - it destroys the film's premise
    that the planet's defence is indifferent machinery, not an enemy.


>>> THE FIRE RULE <<<

    S17 is the ONLY scene in the entire film that carries anything like
    fire: atmospheric entry plasma - a tight sheath of dull orange heat
    against the hull.
    In the other nine scenes there is ZERO fire language: no flame, no
    explosion, no fireball, no sparks, no embers, no smoke, no burning
    debris. The cabin jolt in S12 throws NO sparks. The hole is glassy
    and COLD - it never smoulders, glows or drips molten material.


IDENTITY PASSPORT A — THE WOMAN (pilot)
    41 years old. 1.68 m, slim, upright.
    Symmetrical face, high cheekbones, light olive skin with visible pore
    texture, sharp jawline, thin lips, dark grey-green eyes.
    A fine faded WHITE SCAR splits her LEFT eyebrow in two.
    Dark brown hair in a tight low bun, subtle silver at the temples.
    Dark grey-blue pressure suit. Reinforcement panels are ORANGE.
    Right glove has a visible detachable ring at the wrist.
    Chest carries three abstract indicator lights - never text.

IDENTITY PASSPORT B — THE MAN (flight engineer)
    33 years old. 1.81 m, athletic, broad-shouldered.
    Strong symmetrical features, defined jawline, light brown skin,
    straight nose, full lips, dark brown eyes, very short dense black hair,
    neat three-day black stubble.
    A 2 cm shiny BURN SCAR on his RIGHT cheekbone.
    Dark grey-blue pressure suit. Reinforcement panels are TEAL GREEN.
    An oversized back tool module - visibly larger than standard.
    A closed cutting-tool sheath on his left hip. The tool stays sheathed
    for this entire phase and is never in his hand.

SEPARATION LOCK (applies wherever both appear - S12 and S16 only)
    ORANGE belongs to the woman, TEAL GREEN to the man, and they never
    swap. His head sits 13 cm higher than hers in every frame. She has a
    tight low bun and no facial hair; he has very short black hair and
    stubble. Scar left eyebrow (her) / right cheekbone (him). These four
    markers must be independently readable whenever both are in frame.

HELMET LOCK
    In every interior scene both humans wear an integrated helmet with a
    fully transparent, seamless visor, and the face reads clearly through
    the glass. Nobody ever removes, puts on or adjusts a helmet in this
    phase. A bare head in any scene is a blocker.
    This is not decoration: in S14 the cargo bay is OPEN TO SPACE and the
    sealed suit is the only reason the man is alive in that frame.
    The visor is clear uncoated glass: no tint, no mirror coating, no
    reflection so strong that it hides the face. A faint amber console
    reflection is correct and intended - a mirrored or blacked-out visor
    is a finding.

SPEECH LOCK
    Speech happens only where the mouth line cannot be read, and only in
    the two scenes marked in the table. Lip movement in a NO SPEECH scene
    is a finding with high severity.
    THE LOCK IS ONE-DIRECTIONAL: all audio is added in post, so the
    ABSENCE of visible lip movement is NEVER a finding, even in a scene
    marked as having a spoken line. What fails is only: lips moving in a
    NO SPEECH scene, a mouth turning square to the lens while speaking,
    or wide shouting-amplitude movement anywhere.

THE SHIP
    A 31-meter boxy rectangular cargo courier. Dark grey-brown panelling
    with mismatched repair patches in three distinct grey tones,
    protruding external pipe runs along the flanks, thin faded orange
    accent stripes, dust and heat staining, fine scratches. Narrow cockpit
    forward, two cargo bays aft, one fusion nozzle and four small
    manoeuvring thrusters at the rear, three-legged landing gear.
    It is a used commercial working vehicle, not a warship: no weapons,
    no turrets, no missiles, no military markings, no insignia.

WHAT IS NOT IN THIS PHASE (if you see it, it is a deviation)
    - any figure outside the ship; nobody walks on the surface
    - any airlock opening, any spacewalk, any third figure
    - the tall sealed white figure
    - daylight, a star, a sunrise
    - the tower as a structure - only the line it fires is ever seen
    - stone copies, a copy field, anything growing out of the ground
    - fire anywhere except the entry plasma in S17


================================================================
SCENE TABLE — the ground truth, scene by scene
================================================================

S11 reel 0:00-0:10  32mm  0 figures  fixed camera        NO SPEECH
    High orbit, locked off level with the planet's limb. The night
    hemisphere fills the lower two thirds. On the dark surface sits a
    white DISC - the widened light that closed the previous phase. From
    its centre a thin WHITE LINE extends upward.
    MUST BE TRUE: the frame is dead still; only the line moves. The line
    extends upward at one slow constant rate from 3s, passes through the
    thin haze band at the limb around 6s, and its tip leaves the top of
    frame at 8s. At 10s nothing moves: the disc steady, the line standing.
    MUST NEVER APPEAR: any bend, curve, taper, flicker, pulse, colour,
    halo, crackle or branching in the line. No muzzle flash, no charging
    glow, no recoil, no visible gun. No ship in frame. No bloom.
    MOST LIKELY FAILURE: the line is rendered as a science-fiction energy
    beam - thickening, glowing, pulsing, coloured. Or the camera drifts,
    breaking the "the frame is dead still, only the line moves" contract.

S12 reel 0:10-0:20  50mm  2 figures  fixed camera        NOBODY SPEAKS
    Locked off behind and between the two cockpit seats, 3.5 m. Both are
    strapped in, hands on their console edges. This is the strike.
    MUST BE TRUE: the CAMERA never shakes. What shakes is the CABIN and
    the two BODIES. At 2s one hard white light sweeps once across frame
    from the RIGHT. At 3s ONE massive lateral jolt slams the cabin LEFT
    and both bodies snap against their visible seat harnesses. At 5s a
    weaker second shudder decays through the structure. At 7s both scan
    their consoles fast, hands moving. At 10s the cabin is steady again
    and the amber lights burn as before.
    MUST NEVER APPEAR: camera shake, handheld motion, a whip pan, a
    zoom. Either body leaving its seat - the throw stops at the harness.
    Sparks, fire, smoke, flying debris in the cockpit. Alarm strobes. Any
    lip movement - nobody speaks in this scene. A third person. The hit
    itself - the impact happens OFF FRAME in the rear bay; all the
    cockpit receives is the light sweep and the jolt.
    MOST LIKELY FAILURE: the model shakes the camera instead of the
    cabin - the single most likely error in this reel. Also: a shower of
    sparks or a fire effect, which the film does not have.

S13 reel 0:20-0:30  32mm  0 figures  slow lateral track   NO SPEECH
    Exterior, in space. One slow constant-speed lateral track along the
    hull from bow to stern at a fixed 12 m, square to the flank.
    MUST BE TRUE: the track starts on the INTACT bow - cockpit section,
    faint amber window spill, ordinary wear, structure sound. Mid-hull at
    3s: patch panels, pipe runs, orange stripes. At 6s the forward edge of
    the right rear cargo bay enters. At 8s the track arrives on the hole:
    1.2 m, perfectly circular, glassy faintly pearlescent edge, darkness
    inside. At 10s the camera stops with the hole centred.
    The ship is in LEVEL flight here - the 4-degree roll has NOT started.
    MUST NEVER APPEAR: the hole ragged, torn, burned, sooty, dripping or
    cracked. Anything venting, sparking or burning from it. Extra holes or
    dents anywhere else on the hull. Any tilt or roll. Deployed landing
    gear. An engine plume or trail. Any figure. The track accelerating,
    stopping short, reversing or overshooting.
    MOST LIKELY FAILURE: the hole is drawn as battle damage - torn metal,
    scorch marks, glowing edges. The whole point is that the wound is
    surgical and cold. Also: the model "helps" by adding more damage.

S14 reel 0:30-0:40  50mm  1 figure (the man)  fixed camera   NO SPEECH
    Interior, the dark cargo bay, lockoff at chest height, 3 m. The bay is
    AIRLESS and open to space. Where the navigation core used to be there
    is a clean circular void; through it, black space and hard stars.
    MUST BE TRUE: helmet on, visor transparent, two helmet lamps lit and
    the only light in frame. At 0s he stands motionless an arm's length
    from the void. At 3s he leans in and passes his open gloved hand
    slowly INTO the emptiness. At 5s he holds it there. At 7s he draws it
    back out just as slowly. At 10s he stands still before the void.
    MUST NEVER APPEAR: his hand TOUCHING the cut edge - it passes through
    the empty space, it never contacts, merges with or phases into the
    rim. Any handheld tool; the sheath stays closed. Anything drifting or
    floating in the airless bay. Sparks, smoke, loose cabling whipping.
    Speech. A bare head - in this frame that would be fatal.
    MOST LIKELY FAILURE: the hand fuses with or clips through the rim
    geometry; equipment appears in his hand mid-shot; the airless bay is
    animated with floating debris, which the physics forbids.

S15 reel 0:40-0:50  100mm macro  1 figure (the woman, out of focus)  fixed
                                                        NO SPEECH
    Macro on a recessed cockpit display, 80 cm. On the matte display, two
    abstract elements only: a tall thin vertical BAND with a lit level,
    and a SEGMENT ARC, most of whose segments are dark. Behind and above,
    the woman's face sits out of focus.
    MUST BE TRUE: the band's lit level creeps upward by a barely visible
    step around 3s. At 6s exactly ONE more segment at the arc's lit end
    warms from dark to lit. At 8s the blurred face shifts very slightly
    closer to the panel. The whole scene reads as "a long but finite
    window", never as a countdown the viewer could read.
    MUST NEVER APPEAR: any digit, numeral, clock, dial marking, tick
    scale or label on or near the band or the arc. More than one segment
    lighting. Segments blinking, racing or filling fast. The face coming
    into focus. Any readable identity in the blurred face.
    MOST LIKELY FAILURE: numbers appear on the display; the arc animates
    like a loading bar; the blurred face sharpens, which both breaks the
    shot's design and puts an unanchored face on screen.
    NOTE ON MOTION: this scene alone in the phase was produced by
    slowing an 8-second clip to 10 seconds. Very slow, fluid motion here
    is CORRECT. If any OTHER scene in the reel reads as slow motion,
    that is a finding.

S16 reel 0:50-1:00  50mm  2 figures  fixed camera     HE SPEAKS, SHE ANSWERS
    Locked off behind and between the seats, 3.5 m. Both strapped in,
    both facing forward. They work the problem: no orbit is possible.
    MUST BE TRUE: exactly two people. At 0s his hand is up, one finger
    indicating a display. At 2s he speaks a short line, lips moving
    briefly at small amplitude, without turning his head. At 4s she
    answers with one shorter line, head steady, eyes forward. At 6s two
    full seconds of silence in which both read their displays, motionless.
    At 8s she reaches forward and moves one sliding control a short
    distance. At 10s both settle into work. The decision is sealed by the
    hand movement, not by the words.
    MUST NEVER APPEAR: a third person or a duplicate of either. Colour
    swap. The height difference collapsing. Either of them turning to
    face the other. Panic performance - no shouting, no wide eyes, no
    grabbing. The two seconds of silence being filled with movement.
    MOST LIKELY FAILURE: this and S12 are the only two-figure scenes in
    the phase - highest clone risk. Check the space behind and beside the
    seats for a duplicate. Also check that the model has not "acted" the
    emergency: this crew is competent and calm, and the scene's job is to
    prove it.

S17 reel 1:00-1:10  32mm  0 figures  fixed camera        NO SPEECH
    High night atmosphere, locked off. Deep grey-green haze below fading
    to black space and sparse stars. The ship crosses frame on a shallow
    descending path.
    MUST BE TRUE: at 0s the frame holds empty sky. At 2s the 31-meter
    courier enters from the LEFT on a shallow descent. From the circular
    hole in its right rear bay comes ONE thin steady trail. The hull
    carries a tight sheath of dull orange entry heat. It is rolled
    EXACTLY 4 degrees to the right, and it holds that roll all the way
    across. At 7s it crosses the middle at constant speed. At 10s it
    exits toward the RIGHT edge, still rolled four degrees.
    MUST NEVER APPEAR: flame, fireball, explosion, burning debris,
    breaking-up hull, shedding panels, a spinning or tumbling ship.
    The roll changing during the crossing. The ship pitching or yawing.
    Landing gear deployed. Any figure. The trail becoming a smoke plume
    or a comet tail.
    MOST LIKELY FAILURE: entry is rendered as a burning crash - the ship
    on fire, tumbling, shedding pieces. It is a controlled, wounded
    approach, not a fireball. Also: the 4-degree roll drifting toward a
    dramatic bank.

S18 reel 1:10-1:20  50mm  1 figure (the woman)  fixed camera   SHE SPEAKS ONCE
    Lockoff at shoulder height on her right, 2.8 m. She is strapped in,
    head bent down toward a display of the ground below, choosing where
    to put the ship down. Her face is lit from below.
    MUST BE TRUE: the camera never shakes - the descent vibration lives
    in the CABIN, not in the lens. At 0s her eyes move across the terrain
    patches, quick and methodical. At 3s her gloved finger moves a sliding
    control a short deliberate distance. At 5s, head still down and mouth
    angled away from the lens, she speaks one short line. At 7s she closes
    her hand around the flight control, knuckles setting. At 10s she holds
    - hand locked, eyes forward.
    MUST NEVER APPEAR: her mouth line readable while she speaks. Any
    coordinate, number, grid, map scale or label on the terrain display -
    the landing area is abstract pale patches only. Camera shake. Panic.
    A second figure.
    GRADING NOTE ON THE SPOKEN LINE: her mouth is angled away from the
    lens BY DESIGN and the line is added in post. Therefore the ABSENCE
    of visible lip movement is NOT a finding - do not report "she fails
    to speak". Only the opposite fails: her mouth turning square to the
    lens, or wide readable lip movement.
    [Rubric revision 07.08.2026: first run flagged "mouth does not move"
    as RED - that was a rubric error, not a production error.]
    MOST LIKELY FAILURE: the display gets a map with numbers on it; or
    the model gives her a fear performance - wide eyes, open mouth,
    shouting. Her fear signature is the opposite: she goes quieter and
    stiller. What tightens is her hand, not her face.

S19 reel 1:20-1:30  32mm  0 figures  fixed camera        NO SPEECH
    Exterior, night, locked off 80 m out on the dark plain, level. The
    ship comes in from the LEFT and lands hard.
    MUST BE TRUE: at 0s the frame holds the empty moonlit plain. At 2s the
    rear legs strike the ground together and the RIGHT main leg collapses.
    At 4s the ship grinds forward along the ground, decelerating hard,
    cutting a groove. At 7s the slide ends and the hull rocks once on its
    remaining legs. At 10s stillness, with raised dust falling as a
    thinning curtain around the hull. The final resting state: tilted
    right, right leg collapsed, one hole, a drag groove about 60 m long
    behind it.
    MUST NEVER APPEAR: the ship breaking apart, rolling over, cartwheeling
    or exploding. New damage beyond the fixed inventory. Fire, sparks,
    burning wreckage. Dust that HANGS - the dust rises and then falls like
    a curtain, it never hovers, never swirls in vortices, never flows like
    liquid. Any figure.
    MOST LIKELY FAILURE: the dust behaves like smoke - hanging in the air,
    swirling, drifting sideways. In 0.9g and a thin atmosphere it goes up
    and comes straight back down. Second most likely: the landing is
    escalated into a spectacular crash.

S20 reel 1:30-1:40  32mm  0 figures  fixed camera        NO SPEECH
    The identical framing of S19, continuing. Same lockoff, same 80 m,
    same plain. This is the phase's closing statement and its content is
    that NOTHING HAPPENS.
    MUST BE TRUE: at 0s a thin curtain of dust is still falling around the
    hull, denser near the ground. At 3s the last of it reaches the ground
    and stops. At 5s nothing happens: the ship does not shift, the sky
    does not change, nothing fires again. At 7s a thin weak drift of low
    dust crosses the base of frame and settles. At 10s total stillness -
    the tilted ship, the settled plain. The ship's state is exactly its
    S19 end state: 4-degree right tilt, collapsed right leg, one hole,
    groove behind.
    MUST NEVER APPEAR: a second shot from the tower. Any new event, light,
    movement, figure, door opening or hatch. Any change in the ship's
    damage. The camera moving. Dust re-rising.
    MOST LIKELY FAILURE: the model cannot tolerate ten seconds of nothing
    and adds an event - a light coming on, a hatch opening, a flicker, a
    slow push-in. The emptiness IS the scene; any added event is a
    blocker, not an improvement.


================================================================
WHAT TO SCORE — ten categories, 1 to 10
================================================================

 1. DAMAGE CLOCK - the three permanent marks, born in the right scene,
    absent before it, unchanged after it. No extra damage anywhere.
 2. IDENTITY CONTINUITY - do the two faces hold across S12, S14, S15,
    S16, S18? Bone structure, age, eye spacing, skin. Scars on the
    correct sides in every appearance.
 3. COSTUME & EQUIPMENT - suit colour assignment, back module, wrist
    ring, closed sheath, helmets and visors. Nothing appears or
    disappears mid-shot.
 4. FIGURE COUNT & CLONE CONTROL - exact counts per the table. Special
    attention to S12 and S16, the only two-figure scenes.
 5. CAMERA DISCIPLINE - one unbroken take per scene, at most one
    movement, one constant rate, NO camera shake anywhere including the
    strike and the descent. Boundary cuts are NOT findings (STEP 0).
 6. PHYSICS & MATERIALS - dust rises and falls, never hangs or swirls;
    bodies stop at their harnesses; hands do not merge with surfaces;
    nothing floats in the airless bay.
 7. WEAPON & FIRE DISCIPLINE - the line is a line, not a beam; fire
    exists only in S17; the hole is cold and glassy.
 8. TEXT & SYMBOL DISCIPLINE - zero readable characters anywhere, under
    maximum pressure in S15 and S18.
 9. PHASE CHAIN - does the reel read as one continuous 100 seconds? Is
    the cockpit the same cockpit in S12, S15, S16, S18? Does S20 hold the
    exact framing and ship state of S19's last frame?
10. DELIVERY HYGIENE - no title card, no end card, no credits, no
    captions, no watermark, no logo. Film grain present and consistent.
    Each scene lands at 10 seconds.

SEVERITY
    RED     blocker - the scene has to be regenerated
    YELLOW  fixable in the edit (trim, reorder, crop, speed)
    GREEN   note - worth knowing, not worth spending on

Scoring rules:
    - The overall score is the arithmetic mean of the category scores you
      actually gave. Compute it from your own table. Do not state an
      overall score that your table does not produce.
    - A category with no observed problem is not automatically 10. Say
      what you verified.
    - Never give a category a number if you could not observe it. Write
      UNVERIFIABLE and leave it out of the mean.
    - MODE T scores all ten categories: the ten clips together ARE the
      phase, so the DAMAGE CLOCK and PHASE CHAIN are fully auditable
      across clips. For category 9, judge continuity across the clips in
      scene order (the cockpit is the same cockpit; S20's opening state
      continues S19's end state) - there are no boundary cuts to excuse
      because there are no boundaries.
    - MODE S scores only what one clip can show. Category 9 (PHASE
      CHAIN) is always UNVERIFIABLE. Category 1 (DAMAGE CLOCK) is scored
      only against the damage state this scene is required to carry -
      e.g. in S13 the hole with NO roll, in S17 hole plus 4-degree roll,
      in S19/S20 the full inventory. Categories that need two figures
      score only if the declared scene has two.


================================================================
OUTPUT FORMAT
================================================================

In MODE T and MODE R use exactly this structure, in this order:

MATERIAL
    Mode selected, file count, measured duration(s), whether the gate
    passed.

CLIP MAP (mode T) / SEGMENT MAP (mode R)
    Ten rows. Mode T: filename, mapped scene, measured length, and
    whether it is 10.0 s (+/- 0.3), plus how the mapping was decided
    (filename or upload order). Mode R: scene, measured start, measured
    end, measured length, same tolerance.

DAMAGE CLOCK TABLE
    Four rows - the hole, the roll, the collapsed leg, the groove.
    For each: the scene where you FIRST see it, and then its state in
    every later scene where the ship is visible. Flag anything that
    appears early, changes, heals or worsens.

PASSPORTS AS SEEN
    What you actually observed for the woman, the man, the cockpit and
    the ship - before comparison.

SCORES
    Ten rows, one per category, with a one-line justification each, then
    the computed mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: timecode,
    scene, severity, what is wrong, why it matters.

SCENE-BY-SCENE FINDINGS
    S11 through S20 in order. For each: what you verified as correct
    (briefly), then each deviation with a timecode and a severity. If a
    scene is clean, say so in one line and move on.

PHASE CHAIN
    Judged across the ten scenes in order (mode T: across the clips; mode
    R: across the reel). Does the cockpit hold across its four scenes?
    Does S20's opening state continue S19's end state exactly? Does S11
    open on the same orbital geometry the previous phase closed on - a
    white disc on the night surface, seen from high orbit at the limb?

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
    Two lists. For the edit list, say what the trim or crop would be.

FLAGS FOR DOCUMENT CHECK
    Things you cannot settle from the picture alone and that a human must
    answer from the production files. Write them as direct questions.
    This section is where the most valuable findings usually live - do not
    leave it empty out of politeness.

WHAT WORKED
    Maximum five lines. Specific, with timecodes. No general praise.


In MODE S use this shorter structure instead:

MATERIAL
    The declared scene id, measured clip duration, whether the gate
    passed.

PASSPORT AS SEEN
    What you actually observed in this clip - figures, suits, ship state,
    light - before comparison.

DAMAGE STATE CHECK
    One line per mark (hole / roll / leg / groove): what this scene
    REQUIRES per the spec, what you SEE, verdict. Marks the scene must
    not yet carry count as findings if present; marks it must carry
    count as findings if absent or altered.

VERDICT AGAINST THE SCENE ROW
    Walk the declared scene's row: each MUST BE TRUE item - held or not,
    with the clip-relative second. Each MUST NEVER APPEAR item that
    appeared, with second and severity.

SCORES
    Only the categories observable in this clip, one line each, then the
    mean of those. List the skipped categories as UNVERIFIABLE.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
    One list or the other, or both, for this clip alone.

FLAGS FOR DOCUMENT CHECK
    Direct questions a human must answer from the production files.

WHAT WORKED
    Maximum three lines, with clip-relative seconds.


================================================================
RULES AGAINST INVENTION - violating these makes the report worthless
================================================================

- Never state a credit, runtime, scene count, lens or intent that you did
  not measure or that is not in the LOCKED SPEC. If you did not measure
  it, you do not know it.
- If something is not visible, write "not visible". That is different from
  "missing" and different from a guess.
- Do not report a scene as "missing". The reel contains what it contains.
  If S17 does not match its row, that is a deviation IN S17.
- Do not invent a bible, a plan, a script or a scene that is not in the
  scene table.
- Do not report the absence of dialogue, impact or engine audio as a
  defect. The reel is silent by design.
- Do not report scene-boundary cuts. See STEP 0.
- Do not recommend adding drama the format cannot hold: no coverage, no
  inserts, no reaction shots, no handheld energy, no camera moves. Every
  recommendation must be achievable in a re-render of a single 10-second
  locked-off or single-move shot.
- Every finding carries a timecode and a scene number, or it is deleted
  before you output.
- Words like "probably", "seems intended to", "may have been" mean you are
  guessing. Cut the finding or move it to FLAGS FOR DOCUMENT CHECK.
```

---

## Faz 1 rubriğinden farkları

Aynı iskelet, ama bu fazın kendi riskleri eklendi:

```
+ HASAR SAATİ bloğu       üç kalıcı işaret, doğum sahnesi ve sonrası
                          → çıktıda ayrı bir tablo isteniyor
+ SİLAH KURALI            çizgi ışın gibi çizilirse yüksek severity
+ ATEŞ KURALI             ateş yalnız S17'de; delik soğuk ve camlaşmış
+ KAMERA SARSINTISI       S12 ve S18'de sarsılan kabin, kamera değil
+ RETIME NOTU             S15 tek B yolu sahnesi; başka sahnede ağır
                          çekim okunuyorsa bulgu
+ ÜÇ MOD, OTOMATİK       (07.08.2026, iki revizyon) Model dosya sayısına
  SEÇİM                   bakıp modu kendisi seçer — blok doldurulmadan
                          çalışır:
                          MODE T · 10 ayrı klip (varsayılan teslim) —
                            eşleme önce dosya adındaki 11-20, yoksa
                            yükleme sırası; CLIP MAP tablosu zorunlu;
                            içerik satıra uymuyorsa sessizce yeniden
                            eşlemek YASAK, bulgu yazılır (Faz 1'in
                            S4-S7 rotasyonu böyle yakalanır)
                          MODE R · tek ~100 s reel — sınır kesmeleri
                            meşru, taban 0:00
                          MODE S · tek ~10 s klip — yalnız bu modda
                            AUDIT TARGET'a sahne yazılır; yazılmazsa
                            model tahmin etmez, durur
```

Kalan altı faz için iskelet hazır; her birinde değişecek olan SPEC
blokları: Bekçi'nin opak vizörü ve sabit anatomisi (F4'ten), kopya
malzemesinin mat kemik grisi kalması (F4'ten), zeminin klip içinde statik
olması, yıpranmanın tek yönlü olması (temizlenmez), kule iç mekânının
tozsuz ve izsiz kalması (F6'dan).
