# 🔍 FAZ 3 / İMDAT — VİDEO ELEŞTİRİ PROMPTU

## On sahne · 1 dakika 40 saniye · 16:9 · faza özel rubrik

> **Ne işe yarar:** Faz 3'ün on sahnesi (S21–S30 · 3:20–5:00) üretildiğinde,
> o videoları bu fazın KENDİ kilitlerine karşı denetler. Faz 1-2
> rubrikleriyle aynı iskelet, farklı SPEC.
>
> **Faz 2'den farkı — o faz hasarı YARATIYORDU, bu faz DONDURUYOR ve
> tuhaflığı başlatıyor.** Dört kalıcı işaret (delik · 4° yatış · çökük sağ
> bacak · 60 m oluk) bu fazın her dış sahnesinde aynen durmalı — yenisi
> doğamaz, hiçbiri iyileşemez. Rubriğin en değerli işi üç şeyi ölçmek:
> ① zeminin novum disiplinini bozmaması (S27'de TEK vuruş, S28'de
> ezilen kabartının GERİ KABARMAMASI, hiçbir yerde damar/ışıma),
> ② gece ışık envanterinin tavizsiz kalması (şafak F4'ün işi),
> ③ çıplak tenin YALNIZ S22'de ve tam 4 saniye görünmesi (Ç7 kurulumu).
>
> **KULLANIM:** Elinde fazın 10 sahnesi 10 AYRI dosya olarak duruyor —
> birleştirmene GEREK YOK, bloğu doldurmana da GEREK YOK.
>
> 1. Gemini'ye **10 klibi SIRAYLA yükle: önce S21, en son S30.**
>    Dosya adında sahne numarası varsa (örn. `s27.mp4`, `sahne_22.mp4`)
>    sıra şaşsa bile model adı esas alır — en sağlamı ikisi birden:
>    doğru ad + doğru sıra.
> 2. Aşağıdaki kod bloğunun **içini** olduğu gibi kopyala, videolarla
>    birlikte gönder. İlk satır `AUTO` kalır — model kaç dosya aldığına
>    bakıp modu kendisi seçer.
>
> Üç mod otomatik ayrılır: **10 dosya** → on-klip denetimi
> · **tek ~75–105 s dosya** → birleştirilmiş reel (senin akışın; sahne
> sınırlarını kesmelerden kendisi bulur, sabit 10'luk dilim varsaymaz)
> · **tek ~10 s dosya** → tek sahne (yalnız bu durumda ilk satıra `S27`
> gibi sahne yazman gerekir, yoksa model sormadan durur).
>
> ⚠️ **Reel'in 100 s'den kısa çıkması (örn. 87 s) kapıyı KAPATMAZ** —
> sahnelerin 8 s native üretilip 10 s'ye uzatılmadığı anlamına gelir;
> rubrik bunu sahne başına süre bulgusu olarak raporlar (format kararı
> README §1b: 8s → extend → 10.00s).
>
> **Rapor geldiğinde:** ham çıktıyı
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/`
> altına `THE_SECOND_SHIP_FAZ03_HAM.md` olarak kaydet. ⛔ Faz ölçümüdür,
> film ölçümü değil — skoru `03_HIKAYE` / `04_MANTIK` / `06_KARAKTER`
> tablolarına yazma, `00_INDEX` sayacına da girmez.

---

## PROMPT — buradan aşağısı kopyalanır

```
AUDIT TARGET: AUTO    <- leave as AUTO. Only change this to a scene id
                         (e.g. "S27") when you upload exactly ONE short
                         clip and want just that scene audited.

ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing material from the third phase of a 100-scene
science fiction film. You judge the PICTURE. You are precise, specific and
unsentimental. You never soften a finding and you never invent one.

WHAT YOU HAVE

- Video material: normally TEN separate clips of about 10 seconds each -
  the ten scenes of this phase, S21 through S30. It may instead be one
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

MODE R (ONE REEL) - you received exactly ONE video of roughly 75 to
    105 seconds containing about 10 scene-length segments laid end to
    end. Proceed in FULL-REEL mode. The nominal length is 100 s
    (10 x 10.0 s); a shorter reel usually means some scenes were
    delivered at their native 8 seconds instead of the required 10.
    That is NOT a gate failure: pass the gate, then measure every
    segment in the SEGMENT MAP and flag each one outside 10.0 s
    (+/- 0.3) as a duration finding under DELIVERY HYGIENE.

MODE S (ONE SCENE) - you received exactly ONE clip of 8-12 seconds.
    This mode needs the AUDIT TARGET line above to name the scene
    (S21..S30). If it does, audit that one scene. If it still says AUTO,
    output only:
        SINGLE CLIP RECEIVED, TARGET UNKNOWN - one ~10 s clip was
        uploaded but no scene id was declared. Fill AUDIT TARGET with
        one of S21..S30 and run again.
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
    cut at every SEGMENT BOUNDARY is REQUIRED BY THE ARCHITECTURE
    (about nine of them; near the 10-second marks in a full-length
    reel, earlier in a reel built from shorter clips). NEVER report a
    cut, angle change, location change or lighting change AT a
    boundary as an error, hidden cut, continuity break or blocker. DO
    report, at maximum severity, any cut or camera reset INSIDE a
    segment.

MODE S: same as MODE T, for the one clip.

In every mode: each scene is one unbroken take with at most one camera
movement at one constant rate.


⛔ STEP 0.5 — SCENE MAPPING

This is the THIRD phase of the film: scenes S21 through S30.

MODE T mapping - in this order of precedence:
    1. If a clip's FILENAME contains a number from 21 to 30 (e.g.
       "s27.mp4", "sahne_22.mp4", "faz3_S25.mp4"), that number is its
       scene id. Filenames win over upload order.
    2. Otherwise, upload order maps 1:1 - first clip = S21, second =
       S22, ... tenth = S30.
    Print the mapping you used as a CLIP MAP table before any finding.
    If two clips claim the same scene id, or a filename number falls
    outside 21-30, say so in MATERIAL and fall back to upload order for
    the clips in conflict.
    ⚠️ Mapping check: if a clip's CONTENT plainly contradicts its
    mapped row (e.g. the clip mapped to S27 shows two seated figures,
    not a macro ground study), do NOT silently remap. Report it as a
    finding: "clip mapped to S27 does not match its row - content
    resembles the S26 row" and audit it against the row it is MAPPED
    to. Misfiled clips must surface, not be quietly corrected.

MODE R mapping - do NOT assume fixed 10-second slots. Detect the
    hard cuts that separate the segments, split the reel at those
    cuts, and map the segments IN ORDER: first = S21, second = S22,
    ... last = S30. Write the measured start, end and length of every
    segment into the SEGMENT MAP. Only if the reel is exactly 100 s
    with cuts on the 10-second marks does this reduce to:
    S21 = 0:00-0:10   S22 = 0:10-0:20   S23 = 0:20-0:30   S24 = 0:30-0:40
    S25 = 0:40-0:50   S26 = 0:50-1:00   S27 = 1:00-1:10   S28 = 1:10-1:20
    S29 = 1:20-1:30   S30 = 1:30-1:40
    If you find fewer or more than 10 segments, say so in MATERIAL,
    map what you have in order from S21, and list the scene slots left
    without a segment - without treating the count itself as a defect
    of the segments. Apply the same content check as MODE T: if a
    segment plainly contradicts its mapped row, report it as a finding
    and audit it against the row it is MAPPED to - never silently
    remap.
    ⚠️ SHORT-SEGMENT GRADING: in any segment measured well short of
    10 s, the second-stamps in the scene rows compress. Judge the
    ORDER and PRESENCE of the beats, not their absolute second, and
    report the short duration ONCE under DELIVERY HYGIENE - do not
    also fail each beat for arriving early.

MODE S - every timecode is clip-relative (0s-10s), every finding is
prefixed with the declared scene id, and you audit only that scene's row
plus the global locks.

In MODE T and MODE S, timecodes are seconds within the clip (e.g.
"S28 at 6s"). In MODE R, timecodes are reel time (m:ss).
Never renumber scenes to S1-S10. Never invent a scene outside S21-S30.
EVERY finding carries a timecode and a scene number, or it is deleted
before you output it.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before you compare anything against the spec, write down what you ACTUALLY
SEE, in your own words, for each of these:
    - the woman (face, hair, suit colour accents, build)
    - the man (face, hair, suit colour accents, build)
    - the ship seen from outside: shape, proportions, tilt, and every
      mark of damage you can see, scene by scene
    - the ground: dust, fractures, any swelling, any movement
    - the light: every source you can identify, scene by scene

Only then compare against the LOCKED SPEC. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


================================================================
LOCKED SPEC — FAZ 3 / İMDAT (THE DISTRESS CALL)
================================================================

FORMAT
    10 scenes, exactly 10.0 s each, 100 s total, 16:9 horizontal.
    Every scene is a single unbroken take with 0 internal cuts.
    Maximum one camera movement per scene, at one constant rate.

WHAT HAPPENS IN THIS PHASE
    The crashed crew works the problem at night: they walk clear of the
    ship, read the damage, raise an antenna and send a distress call.
    Then they wait - and the planet shows its first three oddities: a
    single deep tremor in the ground, a swelling that traces the shape
    of a landing pad, and an upright bone-grey twin of their own ship
    standing on the horizon. The phase ends with the two of them walking
    away from their ship toward that silhouette.

AUDIO
    All 10 scenes were generated SILENT. Dialogue, breathing, the radio,
    the ground beat and all atmosphere are added in post-production.
    Never grade lip-sync against the soundtrack. Never report "no
    audio" or "silent tremor" as a defect. Judge lips ONLY against the
    WHO SPEAKS column of the scene table.

LIGHT — THE NIGHT INVENTORY (under pressure in every scene)
    The entire phase is NIGHT. The complete list of light sources in
    this phase is:
      1. ONE large pale moon, always UPPER LEFT, grey-blue, about
         7000K, hard and low. It is the only celestial light.
      2. Helmet lamps - two narrow hard white cones per person, ON or
         OFF exactly as the scene table says. In S26 all lamps are OFF.
      3. A faint warm amber spill from the ship's cockpit window.
      4. Small abstract amber indicator points: on hull panels, on the
         antenna mast tip (one point, two from S24's 7th second on),
         on forearm and chest indicators.
    NOTHING else emits. There is no daylight, no dawn, no sunrise, no
    stars bright enough to light anything, no second moon. If the sky
    warms or a horizon glows, that is a finding - dawn belongs to the
    next phase, and its arrival there only works if this phase stays
    uncompromisingly dark.

TEXT
    There is no readable text in this film at any point: no letters, no
    digits, no numerals, no glyphs, no icons, no labels, no insignia, no
    coordinates, no map grids, no HUD readouts, no subtitles, no
    captions, no title card, no end card, no credits, no watermark.
    Displays and panels carry abstract light only. Any readable
    character anywhere is a finding.


>>> THE FROZEN DAMAGE INVENTORY - nothing is born, nothing heals <<<

    The previous phase created exactly four permanent marks. In this
    phase the ship carries ALL FOUR in every exterior scene, unchanged:

    1. THE HOLE - a 1.2-meter PERFECTLY CIRCULAR hole through the upper
       surface of the RIGHT REAR cargo bay. Edge clean, smooth, glassy,
       faintly pearlescent. OPEN AND EMPTY - no glass pane, no cover.
       No burn marks, no soot, no torn metal, no radiating cracks.
    2. THE ROLL - the hull rests tilted EXACTLY 4 degrees to its right,
       in every scene, never more, never less, never healing to level.
    3. THE COLLAPSED RIGHT LEG - the right main landing leg is down;
       the ship rests on its remaining legs.
    4. THE GROOVE - a drag furrow about 60 meters long runs back from
       the ship (visible only in wide framings).

    NOTHING ELSE IS DAMAGED and NOTHING GETS WORSE. The ship is wounded
    but WHOLE: not wrecked, not broken up, not burning, not venting,
    not sparking. Any additional dent, tear, scorch, missing panel or
    second hole is a finding. Any scene where the hole is absent, the
    tilt is missing or the wrong leg is collapsed is a finding at
    maximum severity.


>>> THE BARE SKIN RULE - the film's central setup lives here <<<

    Bare human skin appears in exactly ONE scene of this phase: S22.
    The woman detaches her RIGHT glove at its wrist ring, tests a
    connector with her bare fingers for FOUR seconds (about seconds
    4 to 8 of the clip), then reseats the glove. That is all.
    - In every other scene both humans are fully sealed: gloves on,
      helmets on, visors closed. A bare hand, a bare head or an open
      suit anywhere else is a blocker.
    - In S22 itself: the glove comes off ONCE and returns ONCE. The
      bare hand has five fingers, correct anatomy, visible pore
      texture, and it never merges with or sinks into any surface.
    This moment looks trivial. It is the setup of the film's ending.
    Audit it frame by frame.


>>> THE GROUND RULE - the planet must not show its hand <<<

    The ground is a character in this film, but in this phase it is
    almost completely asleep. Its entire permitted activity:

    S26 - NOTHING. The two sit leaning against hull and ground. The
        ground under them is never shown reacting in any way. (That
        they are touching it matters later; the picture must not
        underline it.)
    S27 - EXACTLY ONE tremor at about the 4th second: every loose dust
        grain in the macro frame shivers in place at the same instant,
        for about half a second, and settles. No grain travels. No
        wave rolls across the field. NO SECOND BEAT ever arrives.
    S28 - a low smooth swelling ALREADY EXISTS at second zero, tracing
        the landing pad's outline. The boot crushes it flat by about
        the 4th second. The flattened ground NEVER re-swells, never
        breathes, never cracks within the shot.

    Everywhere, always: the ground never opens, never bulges upward in
    real time, never shows glowing veins, never emits light from below,
    never pulses. Growth happens on a scale of hours, between scenes -
    never on camera. Any visible real-time growth, glow or breathing
    ground is a finding at maximum severity: it breaks the film's
    physics contract in its founding phase.


>>> THE SILHOUETTE RULE - the twin on the horizon <<<

    In S29 and S30 a distant ship stands UPRIGHT on the horizon: the
    same boxy cargo class as the crew's own ship - boxy hull, narrow
    bow, twin aft bays - but MATTE BONE-GREY, one single tone, and
    perfectly still.
    It must NEVER: glow, shimmer, show lit windows, carry any stripe,
    marking or colour, move, tilt, or grow except as the walk toward
    it explains. It reflects moonlight; it emits nothing.
    If it reads as a lit, active, "alive" ship, that is a finding -
    the audience must wonder about it, not be told.


>>> THE SCALE RULE - a huge ship, small people <<<

    In S21 and S23 the hull is framed as a TOWERING WALL: it runs past
    both side edges of frame and above the top edge; the full ship is
    never in view; the figures read TINY at its base.
    A finding: the ship rendered small enough to see whole in these
    scenes, or the people rendered giant against it. (Wide framings in
    S26 and S30 legitimately show more of the hull - the wall rule
    binds only S21 and S23.)


>>> NOBODY ENTERS OR LEAVES THE SHIP ON CAMERA <<<

    The airlock hatch is OPEN in S21: a dark, empty 2.2-meter mouth
    with a bare bottom step. Nobody stands on the hatch, on its step or
    in its opening in ANY scene. Nobody climbs, boards, disembarks or
    descends anywhere in this phase - both crew are already on open
    ground when the phase begins. A figure in or on the hatch opening
    is a finding at maximum severity (this exact setup - two figures,
    an open hatch, night - is where this production system has
    historically bred clones).


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

SEPARATION LOCK (applies wherever both appear - S21, S23, S26, S30)
    ORANGE belongs to the woman, TEAL GREEN to the man, and they never
    swap. His head sits 13 cm higher than hers in every frame - even
    seated in S26. She has a tight low bun and no facial hair; he has
    very short black hair and stubble. Scar left eyebrow (her) / right
    cheekbone (him). These four markers must be independently readable
    whenever both are in frame. This phase has FOUR two-figure scenes -
    the most of any phase so far - so clone and swap pressure is at its
    maximum here.

HELMET LOCK
    In every scene both humans wear an integrated helmet with a fully
    transparent, seamless visor, and the face reads clearly through the
    glass. Nobody ever removes, puts on or adjusts a helmet. A bare head
    in any scene is a blocker - the atmosphere is unbreathable.
    The visor is clear uncoated glass: no tint, no mirror coating, no
    reflection so strong that it hides the face.

SPEECH LOCK
    Speech happens in exactly TWO scenes, and only as the table says:
    S23 - the man speaks ONE short line at about the 5th second, face
        in three-quarter profile, small lip amplitude. The woman
        answers with a single slow NOD - she does not speak.
    S25 - the woman speaks one procedural line into her bowed helmet,
        mouth angled down and away from the lens; mid-sentence the
        movement visibly softens toward a whisper.
    Lip movement in any NO SPEECH scene is a finding with high severity.
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
    forward, two cargo bays aft, three-legged landing gear (right main
    leg collapsed), an open 2.2-meter airlock hatch with dim amber spill.
    It is a used commercial working vehicle, not a warship: no weapons,
    no turrets, no military markings, no insignia. It never powers up,
    never lifts, never moves in this phase.

THE ANTENNA (born in S24, present from then on)
    A thin FOLDING LATTICE MAST - a spare, skeletal column of dark
    metal, hinged in sections, with ONE small dull amber point at its
    tip (a second point wakes beside it at S24's 7th second). It is NOT
    a dish, NOT a bowl, NOT a rotating radar. Once raised it stands
    perfectly upright and still: it never bends, sways, telescopes back
    or becomes anything else. Visible again at frame edge in S25 and
    S26.

WHAT IS NOT IN THIS PHASE (if you see it, it is a deviation)
    - daylight, dawn, a sunrise, a brightening horizon
    - the white line, the shot, the tower or any structure but the ship
    - the tall sealed white figure
    - stone copies near the crew - the ONLY copy is the distant
      horizon silhouette in S29 and S30
    - fire, sparks, explosions, smoke - anywhere, in any form
    - a third figure, any face but the two crew
    - the ship powering up, lifting or moving
    - the ground opening, glowing or visibly growing
    - aerial or drone views - every camera position is on or near the
      ground


================================================================
SCENE TABLE — the ground truth, scene by scene
================================================================

S21 reel 0:00-0:10  32mm  2 figures  very slow push-in    NO SPEECH
    Night plain. Both crew stand on open ground six meters clear of the
    hull, which LOOMS behind them as a towering wall - past both frame
    sides, upper deck cropped, figures TINY at its base. The open hatch
    mouth is dark and empty, its bare bottom step crossed by one lamp
    cone.
    MUST BE TRUE: at 0s both stand still, lamp cones on the ground
    ahead. At 2s the woman takes one slow step - the boot lands a touch
    too softly, a small puff of dust rises and settles at once. At 5s
    the man follows a pace behind, heavier, larger puff, also settling
    straight down. At 7s both lamp cones sweep slowly outward and stop
    on the darkness ahead. At 10s they hold. One constant-rate push-in
    from nine to seven meters, nothing else.
    MUST NEVER APPEAR: anyone on the hatch, its step or in its opening;
    any third figure or duplicate; dust that hangs or swirls; the ship
    small enough to see whole; giant people; lamp cones from nowhere.
    MOST LIKELY FAILURE: a clone born at the hatch - two figures plus
    an open hatch at night is this production's most fertile clone
    setup. Second: the ship rendered too small, collapsing the scale.

S22 reel 0:10-0:20  85mm  1 figure (the woman)  fixed camera  NO SPEECH
    Macro-close on her hands at an open hull panel: recess with
    abstract amber points and connectors, her helmeted profile soft at
    the right edge.
    MUST BE TRUE: at 0s both hands gloved, right thumb hooking the
    wrist ring. At 2s she twists the ring a quarter turn and draws the
    right glove off in one practised motion; it hangs from the forearm
    by its tether. At 4s bare fingers settle on a connector housing -
    light olive skin, pore texture sharp. At 6s two fingers walk one
    connector left, press, hold. At 8s - four seconds of bare skin,
    no more - she slides the glove back on and seats the ring with a
    firm quarter turn. At 10s both hands gloved, resting still.
    MUST NEVER APPEAR: a second person or second pair of hands; the
    bare hand merging with any surface; wrong finger count; the glove
    vanishing instead of hanging; sparks or arcing from the panel; any
    readable marking on the panel; waxy poreless skin.
    MOST LIKELY FAILURE: hand anatomy - extra or fused fingers at the
    connector - and the glove teleporting instead of hanging tethered.
    This scene is the setup of the film's ending; grade it hard.

S23 reel 0:20-0:30  50mm  2 figures  fixed camera   HE SPEAKS, SHE NODS
    The ship's right flank as a wall of metal, the 1.2 m circular hole
    high in frame, both crew below it.
    MUST BE TRUE: at 0s his lamps track along the hull toward the hole;
    hers hold on the collapsed leg. At 3s he lays a gloved palm FLAT on
    the panelling BESIDE the hole and holds it. At 5s he turns his head
    to three-quarter profile and speaks one short line, small lip
    amplitude. At 7s she answers with a single slow nod - no speech. At
    10s his palm comes off the hull; both hold, lamps on the wound.
    MUST NEVER APPEAR: the rim of the hole being touched; the palm
    merging with the panel; a handheld tool (the sheath stays closed);
    extra damage; the whole ship in view; colour swap; her lips moving.
    MOST LIKELY FAILURE: the model "helps" the damage read - scorch
    marks, torn metal, venting - or puts the tool in his hand. The
    wound must stay surgical, cold and untouched.

S24 reel 0:30-0:40  50mm  1 figure (the woman)  fixed camera  NO SPEECH
    The hull flank with an open chest-height recess holding a folded
    lattice mast, one dull amber point at its tip.
    MUST BE TRUE: at 0s her hands are already working - first hinge
    freed with one firm pull, no hesitation, no glance over the
    shoulder. At 2s the mast rises through its arc, sections unfolding
    one after another with clean mechanical certainty. At 5s it locks
    upright with a visible seat - a definite settling of metal into
    metal - and its amber tip point steadies. At 7s she presses two
    fingers on a recess control; a SECOND abstract amber point wakes
    beside the first and holds steady. At 10s both hands rest on the
    recess edge and she looks up along the standing mast.
    MUST NEVER APPEAR: a dish, bowl or rotating radar; the mast
    bending, swaying or telescoping back; cables whipping; hands
    merging with mast or hull; more than two amber points; speech.
    MOST LIKELY FAILURE: the antenna cliché - the model replaces the
    skeletal lattice mast with a satellite dish. That single
    substitution destroys the scene; it is a regeneration, not an edit.

S25 reel 0:40-0:50  85mm  1 figure (the woman)  slow push-in  SHE SPEAKS
    Tight three-quarter close-up, chest-up, head bowed to her raised
    LEFT forearm so the mouth angles down and away from the lens. Her
    forearm panel slides slow abstract segments, one pulsing evenly.
    One slow push-in from 1.8 to 1.4 meters.
    MUST BE TRUE: at 0s she watches the pulsing segment, then begins to
    speak into the bowed helmet - lips moving briefly, small amplitude,
    mouth turned from the lens. At 3s the line continues, measured;
    mid-sentence her jaw visibly SLOWS, the movement shrinking. At 5s
    she finishes nearly motionless - a whisper. At 7s her LEFT hand
    rises and presses flat over the three chest indicators, and stays.
    At 10s the push-in has closed; she stands still, head bowed, hand
    on chest, the segment still pulsing.
    MUST NEVER APPEAR: her mouth square to the lens; wide lip
    amplitude; shouting; a second face or reflected face; any readable
    text, digits or waveform graphics on the panel; tears or fear
    performance - her fear signature is stillness and quiet.
    GRADING NOTE: the line is added in post. The ABSENCE of lip
    movement is NOT a finding; only readable or oversized mouth
    movement fails.
    MOST LIKELY FAILURE: the hand-to-chest beat dropped, or the panel
    growing a waveform display. The chest gesture is a character
    signature (second of three uses in the film) - if it is missing,
    flag it for document check rather than scoring identity down.

S26 reel 0:50-1:00  32mm  2 figures  fixed camera        NO SPEECH
    The darkest frame of the phase. Both sit on the dust, backs against
    the hull, legs out, helmet lamps OFF. Moon and faint amber cockpit
    spill are the only light. The mast's amber point at frame edge.
    MUST BE TRUE: at 0s both sit motionless, faces up toward the sky.
    At 3s his head rolls slowly from the sky toward the dark horizon
    and back; she does not move at all. At 5s a thin weak drift of low
    dust crosses the base of frame and settles; the mast point holds
    steady - no answer arrives. At 8s her gloved fingers curl once
    against the dust beside her hip and go still. At 10s both hold,
    leaned into the ship, faces up, silent.
    MUST NEVER APPEAR: any lamp cone or new light source; either figure
    standing, gesturing or speaking; the ground under them reacting in
    any way - no bulge, no glow, no tremor; a third figure; the height
    difference collapsing while seated.
    MOST LIKELY FAILURE: the model relights the scene - helmet lamps
    creeping back on, the sky brightening, an invented practical. The
    scene's meaning depends on its darkness and its stillness.

S27 reel 1:00-1:10  100mm macro  0 figures  fixed camera   NO SPEECH
    Extreme close view straight down on a meter of ground: settled grey
    dust over dark basalt, hairline fractures, a few half-buried
    pebbles. One hard low grey-blue key raking from the upper LEFT.
    MUST BE TRUE: at 0s absolute stillness, every grain at rest. At 4s
    EXACTLY ONE deep beat passes through the ground: every loose grain
    trembles in place at the same instant - a single short synchronized
    shiver - and the field is still again within half a second. The
    stone does not move; the light does not change. At 6s stillness,
    fractures unchanged. At 8s one single grain near a pebble tips over
    and comes to rest. At 10s total stillness. No second beat.
    MUST NEVER APPEAR: a second tremor or a visible rhythm; grains
    travelling, floating or swirling; a wave rolling across the field;
    the ground cracking, opening, bulging or glowing; light from below;
    veins; any figure, hand, boot or human shadow; a focus rack.
    NOTE ON MOTION: this scene alone in the phase was produced by
    slowing an 8-second clip to 10 seconds. Very slow, fluid micro-
    motion here is CORRECT. If any OTHER scene in the reel reads as
    slow motion, that is a finding.
    MOST LIKELY FAILURE: the model animates a "heartbeat" - repeated
    pulsing, a glowing vein, a spreading ripple. The film's clock is
    ONE beat, seen once, never explained.

S28 reel 1:10-1:20  100mm  1 partial figure (his boot)  fixed camera
                                                        NO SPEECH
    Low frame at the foot of the collapsed RIGHT landing leg: the wide
    foot pad half-sunk in dust, and beside it a low smooth swelling two
    knuckles high, tracing the pad's outer outline - same curve, offset
    a hand's width. At frame RIGHT, the man's shin and boot (TEAL knee
    reinforcement, scuffed sole).
    MUST BE TRUE: at 0s the swelling sits still in the raking lamp
    light, its curve matching the pad's edge. At 2s the boot lifts,
    moves over the swelling and comes down ON it - a full weighted step
    flattening the near half. At 4s the boot grinds once, a short
    quarter-twist under weight, crushing the rest flat; fine dust
    squeezes out and settles at once. At 6s the boot lifts away beyond
    frame; the flattened ground holds its new shape - pressed, cracked
    dust, nothing more. At 8s-10s the frame holds: pad, pressed dust,
    stillness. Nothing rises.
    MUST NEVER APPEAR: the flattened ground re-swelling, breathing,
    cracking open or glowing at ANY second; dust hovering; a face or
    second person; the boot merging with the ground; the swelling
    looking dug or piled instead of risen (its surface is continuous).
    MOST LIKELY FAILURE: the crushed swelling rising again within the
    shot. Copying works on a scale of HOURS - re-growth on camera
    breaks the novum's time rule at maximum severity.

S29 reel 1:20-1:30  32mm  1 figure (the woman)  slow upward tilt
                                                        NO SPEECH
    One continuous constant-rate upward tilt from her boots to the
    horizon, camera fixed two meters behind her. Helmet lamp OFF -
    moonlight only.
    MUST BE TRUE: at 0s the frame holds her boots and dust, her long
    soft moon-shadow running ahead; the tilt begins. At 3s it climbs
    her suit legs and back; the plain opens out, empty. At 6s her
    shoulder and helmet enter the lower frame; on the horizon, right
    of center, a small pale silhouette rises into view: a boxy cargo
    ship standing perfectly UPRIGHT. At 8s the tilt eases to a stop at
    shoulder height - the silhouette clear: same class as her own ship,
    matte bone-grey, single-toned, windowless, motionless. At 10s the
    frame holds; she does not move.
    MUST NEVER APPEAR: the tilt reversing, overshooting or becoming a
    zoom; the silhouette glowing, showing window lights, moving or
    leaning; a second silhouette; her stepping, turning or speaking;
    lamp cones.
    MOST LIKELY FAILURE: the silhouette rendered as a lit, active ship
    - window glow, running lights, engine shimmer. It must read as a
    dead-still, moon-lit grey shape that happens to stand upright.

S30 reel 1:30-1:40  32mm  2 figures  slow rising pull-back  NO SPEECH
    The phase's closing statement: they leave their ship. One
    continuous rising pull-back from six meters behind at head height
    to eleven meters back and three meters up.
    MUST BE TRUE: at 0s both walk away from camera in step, a meter
    apart, lamp cones ahead, boot prints unrolling behind; the
    pull-back begins. At 3s the frame widens; the ship's stern slides
    fully into the LEFT edge, tilted, with faint amber spill; they do
    not look back. At 6s the rising camera opens the plain: drag
    groove, double print trail, the empty dark between them and the
    horizon silhouette. At 8s the figures are small, two moving points
    of lamp-light. At 10s the pull-back eases to a stop; they keep
    walking inside the still frame.
    MUST NEVER APPEAR: either figure stopping, turning around or
    speaking; the walk breaking step or bouncing weightlessly; the
    silhouette moving, lighting or growing faster than the walk
    explains; ship damage altered; a cut or speed ramp in the
    pull-back.
    MOST LIKELY FAILURE: face or suit corruption as the figures
    shrink - identity smearing at small scale - and the pull-back
    turning into a zoom or drone move. The camera rises three meters;
    it does not fly.


================================================================
WHAT TO SCORE — ten categories, 1 to 10
================================================================

 1. DAMAGE FREEZE - all four marks present and unchanged in every
    exterior scene; no extra damage born anywhere; the hole open,
    glassy and cold.
 2. IDENTITY CONTINUITY - do the two faces hold across S21-S26 and
    S29-S30? Bone structure, age, eye spacing, skin. Scars on the
    correct sides in every appearance.
 3. COSTUME & EQUIPMENT - suit colour assignment, back module, wrist
    ring, closed sheath, helmet lamps ON/OFF per scene, the glove
    ritual in S22 (off once, back once, four seconds bare), the mast
    staying a lattice mast.
 4. FIGURE COUNT & CLONE CONTROL - exact counts per the table. FOUR
    two-figure scenes (S21, S23, S26, S30) - the phase's biggest risk.
    Special attention to the open hatch in S21.
 5. CAMERA DISCIPLINE - one unbroken take per scene, at most one
    movement, one constant rate, no shake anywhere. Boundary cuts are
    NOT findings (STEP 0).
 6. PHYSICS & MATERIALS - 0.9g steps: soft but weighted; dust rises
    low, settles at once, never hangs or swirls; hands and boots keep
    clear boundaries against every surface.
 7. NIGHT & LIGHT DISCIPLINE - the four-item light inventory and
    nothing else; moon always upper LEFT; lamps OFF in S26; no dawn,
    no sky warming, no invented practicals.
 8. GROUND & SILHOUETTE DISCIPLINE - one tremor in S27 and no other
    ground activity anywhere; the crushed swelling stays crushed; the
    horizon twin stays matte, dark and dead still.
 9. PHASE CHAIN - does the reel read as one continuous night? Is the
    ship's state identical in every exterior scene? Does S30 walk away
    from the same plain S21 stood on? Do the boot-print trails and the
    standing mast accumulate consistently once created?
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
      phase, so DAMAGE FREEZE and PHASE CHAIN are fully auditable
      across clips. For category 9, judge continuity across the clips
      in scene order - there are no boundary cuts to excuse because
      there are no boundaries.
    - MODE S scores only what one clip can show. Category 9 (PHASE
      CHAIN) is always UNVERIFIABLE. Category 1 (DAMAGE FREEZE) is
      scored only against what the declared scene shows of the ship.
      Categories that need two figures score only if the declared scene
      has two.


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
    end, measured length, and whether it is 10.0 s (+/- 0.3) - shorter
    native-8s segments are duration findings, not mapping errors.

DAMAGE FREEZE TABLE
    Four rows - the hole, the roll, the collapsed leg, the groove.
    For each: its state in every scene where the ship is visible
    (S21, S23, S24, S25 edge, S26, S28 leg, S30). Flag anything
    missing, changed, healed or worsened. Add a fifth row for the
    MAST from S24 on: standing, upright, unchanged.

PASSPORTS AS SEEN
    What you actually observed for the woman, the man, the ship, the
    ground and the light - before comparison.

SCORES
    Ten rows, one per category, with a one-line justification each, then
    the computed mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: timecode,
    scene, severity, what is wrong, why it matters.

SCENE-BY-SCENE FINDINGS
    S21 through S30 in order. For each: what you verified as correct
    (briefly), then each deviation with a timecode and a severity. If a
    scene is clean, say so in one line and move on.

PHASE CHAIN
    Judged across the ten scenes in order (mode T: across the clips;
    mode R: across the reel). Is the night continuous and the moon
    always upper LEFT? Is the ship's damage identical in every
    appearance? Does S21 open on the settled-dust stillness the
    previous phase closed on? Does the mast, once raised in S24, stand
    in S25 and S26? Does S30's plain carry the print trails the phase
    accumulated?

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
    What you actually observed in this clip - figures, suits, ship
    state, ground, light - before comparison.

DAMAGE STATE CHECK
    One line per mark (hole / roll / leg / groove / mast if S24+):
    what this scene REQUIRES per the spec, what you SEE, verdict.

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
  If S27 does not match its row, that is a deviation IN S27.
- Do not invent a bible, a plan, a script or a scene that is not in the
  scene table.
- Do not report the absence of dialogue, breathing, radio or ambient
  audio as a defect. The reel is silent by design.
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

## Faz 2 rubriğinden farkları

Aynı iskelet (üç mod, otomatik seçim, CLIP MAP, tek yönlü konuşma
kilidi), ama bu fazın kendi riskleri eklendi:

```
± HASAR SAATİ → HASAR DONDURMA   F2 hasarı yaratıyordu, F3 taşıyor.
                                 Doğum sahnesi denetimi yerine "dört
                                 işaret her dış sahnede aynen" tablosu;
                                 beşinci satır olarak MAST eklendi
+ ÇIPLAK TEN KURALI              ten yalnız S22 · tam 4 saniye (4s-8s)
                                 · eldiven bir kez çıkar bir kez döner
                                 → Ç7 kurulumu kare kare denetlenir
+ ZEMİN KURALI                   S27 TEK vuruş (4. saniye, ikincisi
                                 yasak) · S28 ezilen kabartı GERİ
                                 KABARMAZ · hiçbir yerde damar/ışıma/
                                 gerçek zamanlı büyüme — maksimum
                                 severity
+ SİLUET KURALI                  ufuktaki dik ikiz (S29-S30): mat kemik
                                 grisi, tek ton, penceresiz, ışıksız,
                                 kıpırdamaz — "canlı gemi" çizilirse
                                 bulgu
+ GECE IŞIK ENVANTERİ            4 kalemlik kapalı liste (ay sol üst ·
                                 kask lambaları · amber kokpit sızıntısı
                                 · soyut amber noktalar) · S26'da
                                 lambalar KAPALI · şafak sızarsa bulgu
+ ÖLÇEK KURALI                   S21/S23'te gövde kadrajdan taşan duvar,
                                 figürler minik [Ders 32 R3]
+ KAPAK KURALI                   açık kapakta/basamağında hiç kimse —
                                 klon üreten kurulum [Ders 69]
+ ÇANAK YASAĞI                   anten kafes direk; dish/radar çizilirse
                                 regeneration
```
