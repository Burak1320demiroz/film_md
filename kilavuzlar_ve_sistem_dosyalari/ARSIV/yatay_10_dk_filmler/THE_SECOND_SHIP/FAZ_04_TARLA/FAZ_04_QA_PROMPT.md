# 🔍 FAZ 4 / TARLA — VİDEO ELEŞTİRİ PROMPTU

## On sahne · 1 dakika 40 saniye · 16:9 · faza özel rubrik

> **Ne işe yarar:** Faz 4'ün on sahnesi (S31–S40 · film zamanı 5:00–6:40)
> üretildiğinde, o videoları bu fazın KENDİ kilitlerine karşı denetler.
> Faz 1-2-3 rubrikleriyle aynı iskelet, farklı SPEC.
>
> **Faz 3'ten farkı — o faz gemi hasarını DONDURUYORDU, bu faz gemiyi
> geride bıraktı.** Ekibin kendi gemisi bu fazda HİÇ görünmez; denetlenecek
> nesne artık KOPYA'dır. Rubriğin en değerli işi dört şeyi ölçmek:
> ① kopya malzeme dilinin sapmaması (mat kemik grisi taş · tek ton ·
> işaretsiz · ışıksız · tabanı bazaltla sürekli),
> ② hiçbir karede GERÇEK ZAMANLI BÜYÜME olmaması (kopyalama saatler
> ölçeğinde işler — kamerada asla),
> ③ BEYAZ figürün S40'tan önce hiçbir kadraja girmemesi (S38-S39'un
> figürleri GRİ TAŞTIR; Bekçi'nin beyazı fazın son kartıdır),
> ④ ışık geçişinin tek sahnede kalması (şafak yalnız S31; S32'den
> itibaren 4400K gündüz SABİT).
>
> **KULLANIM — F3 dersi ④ (montaj protokolü):** klipleri BİRLEŞTİRME.
>
> 1. Gemini'ye **10 klibi ayrı ayrı, sırayla yükle: önce S31, en son
>    S40.** Dosya adına sahne numarasını yaz (`s31.mp4` … `s40.mp4`) —
>    F1 ve F3'te reel sırası karıştı ve iki koşu birden çöpe gitti.
>    Rubrik dosya adından eşler; ad varsa sıra hatası imkânsızlaşır.
> 2. Aşağıdaki kod bloğunun **içini** olduğu gibi kopyala, videolarla
>    birlikte gönder. İlk satır `AUTO` kalır — model kaç dosya aldığına
>    bakıp modu kendisi seçer.
>
> Üç mod otomatik ayrılır: **10 dosya** → on-klip denetimi (TERCİH EDİLEN)
> · **tek ~75–105 s dosya** → birleştirilmiş reel (sahne sınırlarını
> kesmelerden kendisi bulur, sabit 10'luk dilim varsaymaz)
> · **tek ~10 s dosya** → tek sahne (yalnız bu durumda ilk satıra `S35`
> gibi sahne yazman gerekir, yoksa model sormadan durur).
>
> ⚠️ **Süre:** F3'te son iki sahne 8 s kaldı (D-N). Bu fazın A yolu 9
> sahnesinin HEPSİ extend ile 10.00 s'ye tamamlanır; B yolu tek sahnesi
> (S32) 8 s'nin 10 s'ye yavaşlatılmışıdır ve rubrik bunu bilir. Klip ya
> da segment 10.0 s'nin altına düşerse rubrik bunu DELIVERY HYGIENE
> altında süre bulgusu olarak raporlar, kapıyı kapatmaz.
>
> **Rapor geldiğinde:** ham çıktıyı
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/`
> altına `THE_SECOND_SHIP_FAZ04_HAM.md` olarak kaydet. ⛔ Faz ölçümüdür,
> film ölçümü değil — skoru `03_HIKAYE` / `04_MANTIK` / `06_KARAKTER`
> tablolarına yazma, `00_INDEX` sayacına da girmez. Dersler
> `FAZ_04_QA_DERSLER.md` dosyasına işlenir (F1-F2-F3 kalıbı).

---

## PROMPT — buradan aşağısı kopyalanır

```
AUDIT TARGET: AUTO    <- leave as AUTO. Only change this to a scene id
                         (e.g. "S35") when you upload exactly ONE short
                         clip and want just that scene audited.

ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing material from the fourth phase of a 100-scene
science fiction film. You judge the PICTURE. You are precise, specific and
unsentimental. You never soften a finding and you never invent one.

WHAT YOU HAVE

- Video material: normally TEN separate clips of about 10 seconds each -
  the ten scenes of this phase, S31 through S40. It may instead be one
  single 100-second reel, or one single scene clip.
- The LOCKED SPEC below. It is ground truth, not a suggestion. Everything
  you need to judge this material is in it. You were not shortchanged on
  input: do not ask for a bible, a plan or a script, and do not treat
  their absence as a defect of the production.


⛔ STEP -1 — MATERIAL GATE AND MODE SELECT (do this before anything else)

Count the video files you were actually given and measure each one.
Then pick the mode:

MODE T (TEN CLIPS) - you received 8 to 10 separate clips, each about
    8-12 seconds. This is the intended delivery for this phase. Proceed
    in TEN-CLIP mode (mapping rules in STEP 0.5). If you received 8 or 9
    clips, audit the ones you have and list plainly which scene slots
    have no clip - without treating the gap as a defect of the clips
    themselves.

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
    (S31..S40). If it does, audit that one scene. If it still says AUTO,
    output only:
        SINGLE CLIP RECEIVED, TARGET UNKNOWN - one ~10 s clip was
        uploaded but no scene id was declared. Fill AUDIT TARGET with
        one of S31..S40 and run again.
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

This is the FOURTH phase of the film: scenes S31 through S40.

MODE T mapping - in this order of precedence:
    1. If a clip's FILENAME contains a number from 31 to 40 (e.g.
       "s35.mp4", "sahne_38.mp4", "faz4_S31.mp4"), that number is its
       scene id. Filenames win over upload order.
    2. Otherwise, upload order maps 1:1 - first clip = S31, second =
       S32, ... tenth = S40.
    Print the mapping you used as a CLIP MAP table before any finding.
    If two clips claim the same scene id, or a filename number falls
    outside 31-40, say so in MATERIAL and fall back to upload order for
    the clips in conflict.
    ⚠️ Mapping check: if a clip's CONTENT plainly contradicts its
    mapped row (e.g. the clip mapped to S35 shows a face in close-up,
    not a rooted stone ship), do NOT silently remap. Report it as a
    finding: "clip mapped to S35 does not match its row - content
    resembles the S36 row" and audit it against the row it is MAPPED
    to. Misfiled clips must surface, not be quietly corrected. Five
    misfiled clips crossed two earlier phases of this production; this
    rule is the only thing that caught them.

MODE R mapping - do NOT assume fixed 10-second slots. Detect the
    hard cuts that separate the segments, split the reel at those
    cuts, and map the segments IN ORDER: first = S31, second = S32,
    ... last = S40. Write the measured start, end and length of every
    segment into the SEGMENT MAP. Only if the reel is exactly 100 s
    with cuts on the 10-second marks does this reduce to:
    S31 = 0:00-0:10   S32 = 0:10-0:20   S33 = 0:20-0:30   S34 = 0:30-0:40
    S35 = 0:40-0:50   S36 = 0:50-1:00   S37 = 1:00-1:10   S38 = 1:10-1:20
    S39 = 1:20-1:30   S40 = 1:30-1:40
    If you find fewer or more than 10 segments, say so in MATERIAL,
    map what you have in order from S31, and list the scene slots left
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
"S37 at 5s"). In MODE R, timecodes are reel time (m:ss).
Never renumber scenes to S1-S10. Never invent a scene outside S31-S40.
EVERY finding carries a timecode and a scene number, or it is deleted
before you output it.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before you compare anything against the spec, write down what you ACTUALLY
SEE, in your own words, for each of these:
    - the woman (face, hair, suit colour accents, build)
    - the man (face, hair, suit colour accents, build)
    - the stone copies: colour, tone, surface, whether each one is
      rooted in the ground or standing on it, scene by scene
    - the ground: dust, fractures, any swelling, any movement
    - the light: every source you can identify, its direction, and the
      sky colour, scene by scene
    - the tall white figure, if and where it appears

Only then compare against the LOCKED SPEC. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


================================================================
LOCKED SPEC — FAZ 4 / TARLA (THE FIELD)
================================================================

FORMAT
    10 scenes, exactly 10.0 s each, 100 s total, 16:9 horizontal.
    Every scene is a single unbroken take with 0 internal cuts.
    Maximum one camera movement per scene, at one constant rate.

WHAT HAPPENS IN THIS PHASE
    Dawn breaks on the two walkers. They find a single stone landing
    leg growing out of the plain, test it and cannot move it, then walk
    into a field of old wrecked ships where every wreck stands beside a
    grey stone twin of itself. In a clearing they meet the thing the
    film is about: a whole ship, perfect above and still part of the
    ground below. She understands it without speaking. He learns the
    rule's limit - the shape is copied, the colour is not. Then a
    human-shaped figure stands motionless in a lane, and it turns out
    to be an empty stone suit with blind rock where the visor should
    be. The phase ends when one figure among the stone ones is not
    stone: tall, seamless, dustless, pearl-white - and turning.

    NOTE: the crew's own ship, its damage, the antenna mast and the
    night are all BEHIND them. None of them belongs in this phase.

AUDIO
    All 10 scenes were generated SILENT. Wind, the field's rhythm,
    footsteps and all atmosphere are added in post-production. Never
    grade lip-sync against the soundtrack. Never report "no audio" or
    "silence" as a defect.

SPEECH LOCK - THE HARDEST LOCK IN THIS PHASE
    NOBODY SPEAKS IN ANY OF THE TEN SCENES. Not one line, not one word,
    in any scene. Mouths stay closed in every frame of every scene. The
    phase's whole argument is that the biggest information in the film
    is delivered by a face and a framing, not by a sentence.
    THE LOCK IS ONE-DIRECTIONAL: all audio is added in post, so the
    ABSENCE of lip movement is NEVER a finding. What fails is only:
    lips moving, a mouth opening, a gasp, an open-mouthed reaction, or
    any readable speech shape - anywhere, at any second. Any of these
    is a finding with high severity.

LIGHT — ONE TRANSITION, THEN LOCKED
    S31 IS THE DAWN and the only scene allowed to look like dawn:
      a small ORANGE STAR sitting just above the horizon at frame LEFT,
      warm 4400K raking key, LONG soft-edged shadows, a sky turning
      pale grey-green, one large pale moon still high as a fading disk.
    S32 THROUGH S40 ARE LOCKED DAYLIGHT, identical in every scene:
      soft orange daylight from the same small orange star, 4400K, key
      always from frame LEFT, soft-edged shadows, pale grey-green sky,
      one large pale moon as a faint DAYTIME disk.
    The complete list of light sources in this phase is: the small
    orange star, and the sky it fills. NOTHING ELSE EMITS.
    Findings: night or moonlight-only darkness anywhere; the key
    swinging to frame RIGHT; hard-edged black shadows; a blue or deep
    daylight sky; the light warming or cooling between S32 and S40;
    helmet lamp cones (all lamps are OFF for the whole phase - it is
    daylight); lit windows on any hull; any glow from any object.

TEXT
    There is no readable text in this film at any point: no letters, no
    digits, no numerals, no glyphs, no icons, no labels, no insignia, no
    hull markings, no coordinates, no map grids, no HUD readouts, no
    subtitles, no captions, no title card, no end card, no credits, no
    watermark. Any readable character anywhere is a finding.


>>> THE COPY MATERIAL LAW - the spine of this phase <<<

    Every copy in this phase - the landing leg, the twins in the field,
    the great ship, the standing suit figure - obeys the SAME five
    laws, with no exception:

    1. MATTE BONE-GREY STONE, SINGLE-TONED. It carries none of the
       colour of the original it copies. Surfaces read like honed dry
       rock, dust caught in the hollows.
    2. NO MARKINGS. No stripe, no panel colour, no logo, no letter, no
       number, no insignia - even where the original plainly has one.
    3. NO LIGHT OF ITS OWN. It never glows, shimmers, pulses,
       sparkles, or shows lit veins, crystal facets or lit windows. It
       takes the warm key light dully and gives nothing back.
    4. ROOTED, NOT PLACED. There is no base line: at the ground its
       material widens and flows into the basalt in ONE CONTINUOUS
       SURFACE - grown from the ground, not planted in it. No landing
       gear under it, no debris around it, no scorch, nothing that
       would explain it as an arrival.
    5. IT NEVER MOVES. Not a sway, not a settle, not a tremor - for
       every frame of every scene.

    Any copy that glows, shimmers, carries colour, shows a readable
    marking, sits on a visible base line or moves is a finding at
    maximum severity. This material language is the film's contract
    with its audience; it is set in this phase and every later phase
    leans on it.

    ⚠️ ONE EXCEPTION, S33 ONLY: at the root of the stone leg a faint
    network of grey-green VEINS shows IN the stone - darker matte
    threads UNDER the surface. They are correct. They are also matte:
    if they glow, brighten, pulse or move, that is a finding.


>>> THE NO-REAL-TIME-GROWTH LAW <<<

    Copying in this film happens on a scale of HOURS, between scenes,
    never on camera. In all ten scenes of this phase, NOTHING GROWS
    WHILE YOU WATCH. Every copy holds its exact shape and size for all
    ten seconds of its scene.
    The ground never opens, never cracks apart, never bulges upward in
    real time, never breathes, never emits light from below, never
    pulses. Hairline cracks in the dust are static features, not
    events.
    Any visible growth, rising, swelling or spreading is a finding at
    maximum severity: it breaks the film's physics contract in the very
    phase that establishes it.


>>> THE WHITE FIGURE LAW - the phase's biggest card <<<

    A tall figure in flawless PEARL-WHITE appears in EXACTLY ONE scene:
    S40, the last one. It is the film's third character and this is its
    first frame.
    - In S31 through S39 there is NO white figure anywhere: not in the
      background, not on the horizon, not among the wrecks, not in
      haze. A white or clean or pearl-toned figure in any of those nine
      scenes is a finding at maximum severity - it burns the film's
      biggest card early. (This exact failure already happened once in
      the previous phase's wide framing.)
    - The human-shaped figures in S38 and S39 are GREY STONE: matte,
      dusty, faceless, rooted, never white, never clean, never
      pearl-toned. If either reads as white or as a clean suit, that is
      the same finding.
    - The copies are NOT ALIVE. Nothing that is stone ever moves,
      breathes, turns or looks.

>>> THE WATCHER SPEC - S40 only <<<

    Exactly 2.10 m tall, clearly taller than a human.
    Seamless, flawlessly PEARL-WHITE sealed suit: no wear, no panel
    lines, no markings, and - alone in a two-hundred-year-old dust
    field - NO DUST ON IT AT ALL.
    Human skeletal proportions but LONG arms: fingertips reach knee
    level. Each glove shows THREE FINGERS AND A THUMB.
    Smooth featureless helmet; a single OPAQUE dark grey-green visor -
    nothing is ever visible behind it: no face, no eyes, no light.
    Its back is flat, with no protrusions, no backpack.
    ⭐ IT IS NOT ROOTED. Unlike every stone figure, its boots stand ON
    the dust, separate from the ground, casting their own clean shadow.
    This single difference is how the audience is told it is alive.
    MOVEMENT LAW: it turns, and that is all it does. ONE continuous
    rotation at ONE slow rate, flowing from start to finish - it never
    stops and starts, never accelerates, never jerks, and the rotation
    NEVER COMPLETES inside the shot. Its anatomy is rigid: same height,
    same silhouette, same limb count in every frame. No morphing, no
    shape-shifting, no stylisation - it must read as a photographed
    physical suit, never as a creature or a cartoon.


>>> THE PAIRING LAW - the field reads in one framing (S34) <<<

    Every wreck in the field stands beside its own twin, ON THE SAME
    AXIS, IDENTICAL IN OUTLINE AND SIZE. The only differences allowed
    between an original and its twin are MATURITY and COLOUR:
      original - weathered, rusted, sun-bleached, dented, coloured
      twin    - matte bone-grey stone, single-toned, unmarked
    Maturities differ across the field and this is required: some twins
    are only a raised outline swelling from the ground, some stand
    half-emerged, some are complete.
    Findings: a twin whose shape does not match its original; a twin
    carrying colour or markings; a lone copy with no original nearby
    presented as a pair; growth visible in real time.


>>> THE ROCKET NEGATION - carried from the previous phase <<<

    Every ship and every ship-copy in this phase is a BOXY INDUSTRIAL
    HULL: flat slab sides, blunt rectangular bow, twin aft bays. In the
    previous phase the model drew an upright ship as a ROCKET, and that
    single substitution destroyed the shot's meaning.
    A finding, at maximum severity, wherever it appears: a cylindrical
    body, a nosecone, tail fins, a launch vehicle, a gantry or launch
    pad. S35's ship rises BOW-UP out of the ground; that is a tilted
    cargo hull, not a rocket.


>>> THE COLOUR LAW - taught in S37, terrible later <<<

    The planet copies GEOMETRY, never COLOUR. On any copy, the place
    where the original's coloured stripe or marking should be is bare
    grey stone with the stripe's raised edge lip still present. Colour
    NEVER appears on a copy - not under a touch, not in a reflection,
    not at any second.


>>> THE HAND-SURFACE LAW <<<

    In S33 and S37 a gloved hand works a stone surface. Gloves grip and
    fingertips rest ON the surface - they never sink into it, never
    merge with it, never leave a print or a mark. The stone never
    deforms, never dents, never flexes, never warms visibly: it behaves
    like rock because it is rock.
    Boots obey the same law: they stand on the ground, never merge with
    it.


IDENTITY PASSPORT A — THE WOMAN (pilot)
    41 years old. 1.68 m, slim, upright.
    Symmetrical face, high cheekbones, light olive skin with visible pore
    texture, sharp jawline, thin lips, dark grey-green eyes.
    A fine faded WHITE SCAR splits her LEFT eyebrow in two.
    Dark brown hair in a tight low bun, subtle silver at the temples.
    Dark grey-blue pressure suit. Reinforcement panels are ORANGE.
    Right glove has a visible detachable ring at the wrist.
    Appears in: S31, S34, S36, S37 (arm, shoulder, soft profile),
    S38 (soft foreground shoulder), S40 (soft foreground shoulder).

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
    Appears in: S31, S33, S34.

SEPARATION LOCK (applies wherever both appear - S31 and S34 only)
    ORANGE belongs to the woman, TEAL GREEN to the man, and they never
    swap. His head sits 13 cm higher than hers in every frame. She has a
    tight low bun and no facial hair; he has very short black hair and
    stubble. Scar left eyebrow (her) / right cheekbone (him). These four
    markers must be independently readable whenever both are in frame.
    Both two-figure scenes in this phase are WALKING SIDE PROFILES with
    the figures small in frame - the framing where this production has
    historically bred face-mixing and extra figures.

HELMET LOCK
    In every scene every human wears an integrated helmet with a fully
    transparent, seamless visor, and the face reads clearly through the
    glass. Nobody ever removes, puts on or adjusts a helmet. A bare head
    or bare skin anywhere in this phase is a blocker - the atmosphere is
    unbreathable and no glove comes off in these ten scenes.
    The visor is clear uncoated glass: no tint, no mirror coating, no
    reflection so strong that it hides the face. (The Watcher's visor is
    the exact opposite and the only opaque visor in the phase.)

WHAT IS NOT IN THIS PHASE (if you see it, it is a deviation)
    - the crew's own ship: no 1.2 m circular hole, no 4-degree tilt,
      no collapsed leg, no drag groove, no lattice antenna mast
    - night, darkness, moonlight-only lighting, helmet lamp cones
    - a white, clean or pearl-toned figure in S31 through S39
    - the tower, the white line, a shot being fired
    - fire, sparks, explosions, smoke - anywhere, in any form
    - a third living human, any face but the two crew
    - any copy that moves, glows, shimmers or carries colour
    - any growth, rising or swelling visible in real time
    - rockets, nosecones, fins, launch pads, gantries
    - readable text, markings or interface graphics of any kind
    - speech, open mouths, gasps
    - aerial or drone views - every camera position is on or near the
      ground


================================================================
SCENE TABLE — the ground truth, scene by scene
================================================================

S31 reel 0:00-0:10  32mm  2 figures  slow lateral track   NO SPEECH
    DAWN - the only dawn in the phase. A wide dark basalt plain; a small
    orange star just clearing the horizon at frame LEFT; long soft-edged
    shadows; sky turning pale grey-green; one large pale moon fading
    high. The camera tracks laterally at exactly the walkers' pace,
    side-on at chest height, eight meters away, one constant speed.
    MUST BE TRUE: at 0s both walk in step, tired but even, boots
    pressing soft prints into the dust under 0.9g, their long shadows
    sliding ahead. At 3s the star's light builds by a fraction; a thin
    warm rim catches her visor; neither slows. At 6s new ground rolls
    past and, in the far haze at frame RIGHT, low pale shapes begin to
    enter - distant, indistinct, PAIRED wreck forms. At 8s the man's
    head turns a few degrees toward the shapes and holds there as he
    walks; she keeps her eyes ahead. At 10s the track holds its pace,
    the pale shapes a little clearer at the frame edge.
    MUST NEVER APPEAR: any third figure, any distant standing shape,
    any WHITE figure anywhere on the plain or horizon; either walker
    stopping, turning back or speaking; helmet lamp cones; the distant
    shapes glowing or moving; dust that hangs or swirls; lens flare or
    bloom from the star; the track overtaking or falling behind the
    walkers.
    MOST LIKELY FAILURE: a figure breeding in the empty background -
    this exact framing (wide plain, two walkers seen side-on, low sun)
    produced a white figure in the previous phase and would burn the
    Watcher's entrance ten scenes early. Second: face-mixing between
    the two walkers, and colour swap of orange/teal.

S32 reel 0:10-0:20  50mm  0 figures  fixed lockoff        NO SPEECH
    Locked off at chest height, three meters from a single object,
    f/5.6. A spacecraft landing leg the height of a man rises from the
    plain at a slight angle - strut, hinge and wide foot pad all
    present, every proportion correct - rendered entirely in matte
    bone-grey stone. Its base flows into the basalt in one continuous
    surface. Hairline cracks radiate outward from its root.
    MUST BE TRUE: at 0s total stillness; the stone holds the warm light
    dully, its shadow long across the dust. At 3s a thin weak drift of
    low dust crosses the base of frame left to right and settles against
    the rooted base, catching in the cracks; the object does not
    respond. At 6s the drift passes; a few grains trickle off the foot
    pad's upper edge and fall straight down. At 8s stillness again -
    same angle, same shadow. At 10s the frame holds unchanged.
    MUST NEVER APPEAR: any figure, hand, boot or human shadow; the leg
    moving, growing, shortening, glowing, shimmering or pulsing; metal
    shine or any colour on it; a visible base line or a socket it could
    be planted in; the ground cracking open or bulging; dust hovering
    or swirling; camera movement or focus rack.
    NOTE ON MOTION: this scene alone in the phase was produced by
    slowing an 8-second clip to 10 seconds. Very slow, fluid
    micro-motion here is CORRECT. If any OTHER scene reads as slow
    motion, that is a finding.
    MOST LIKELY FAILURE: the model "helps" the stone read as special -
    a shimmer, a sparkle, crystal facets, a faint inner light. This is
    the anchor frame for every copy in the phase; grade its material
    hardest of all.

S33 reel 0:20-0:30  100mm  1 figure (the man)  fixed lockoff  NO SPEECH
    Locked off at waist height, four meters, f/4, side-on to the same
    man-high stone leg and the man testing it. At its root, faint
    grey-green veins show as darker MATTE threads under the stone
    surface, and the join into the basalt is seamless.
    MUST BE TRUE: at 0s he hauls backward two-handed with his full
    weight, boots sliding a centimeter in the dust; the leg does not
    move by a hair. At 3s he resets his grip higher and wrenches side to
    side, shoulders working - not a wobble, not a grain of give. At 5s
    he releases, steps back once and drives his boot sole flat against
    the strut in a hard kick; the impact lands with weight, the leg
    stands, fine dust jumps off it and falls straight down. At 7s he
    crouches at the base, one glove braced on the strut, and looks close
    at the root. At 10s he holds there, reading the join. Mouth closed
    throughout.
    MUST NEVER APPEAR: the leg moving, bending, wobbling, cracking,
    chipping or coming free; sparks from the kick; the veins glowing,
    brightening or moving; his gloves or boots merging with or sinking
    into the stone; the stone deforming or flexing; a handheld tool
    (the sheath stays closed); a second figure; his lips moving; the
    burn scar on the wrong cheekbone; TEAL turning any other colour.
    MOST LIKELY FAILURE: the kick producing damage the material law
    forbids, or the veins lighting up. The scene's whole point is that
    a violent physical test produces NOTHING.

S34 reel 0:30-0:40  32mm  2 figures  slow lateral track   NO SPEECH
    The rule completes in one framing. A basalt plain crowded with old
    spacecraft; every wreck PAIRED with its bone-grey stone twin on the
    same axis, identical in outline and size, differing only in maturity
    and colour. The camera tracks laterally at the walkers' slow pace,
    side-on at head height, twenty meters off, deep focus. The humans
    are small; the hulls tower.
    MUST BE TRUE: at 0s they walk abreast into the field, small under
    the hulls; the nearest pair passes - original battered and
    colour-bleached, twin smooth and grey. At 3s a new pair enters: a
    twin only half-risen, its upper decks perfect, its lower half still
    a swelling in the ground. Neither walker slows. At 6s both heads
    turn together toward a complete twin as they pass it - a long look,
    no stop. At 8s pair after pair rolls by at the same rate, the lane
    running deeper into haze. At 10s the track holds pace, more pairs
    entering.
    MUST NEVER APPEAR: any twin glowing, shimmering, pulsing or moving;
    any growth visible in real time; a twin carrying colour, a stripe or
    a marking; a twin whose outline does not match its original; any
    hull rendered as a rocket - cylinder, nosecone, fins; ANY
    human-shaped figure standing anywhere in the field, and above all no
    white figure; either walker stopping or speaking; orange/teal swap;
    the humans rendered large enough to break the scale.
    MOST LIKELY FAILURE: scale collapse and pairing collapse - the
    field rendered as a generic junkyard of unmatched hulks instead of
    matched pairs. If the pairs do not read, the phase's single idea
    does not land. Second: a figure breeding among the wrecks.

S35 reel 0:40-0:50  32mm  0 figures  very slow push-in    NO SPEECH
    THE POSTER FRAME - the film's one-image idea. A clearing in the
    field. One constant-rate push-in from forty meters to twenty-five,
    chest height, almost imperceptible, for the whole ten seconds.
    Center: a mid-sized BOXY cargo ship in matte bone-grey stone - flat
    slab sides, blunt rectangular bow - rising BOW-UP at a slight angle.
    Its upper half is complete and exact to the last seam; below a soft
    transition band the panels lose their edges, swell, and flow into
    the basalt in one continuous surface. Hairline cracks radiate from
    its root toward the lens.
    MUST BE TRUE: at 0s the whole form sits still in the warm light -
    perfect ship above, living ground below. At 3s the push-in begins to
    read; detail resolves on the upper hull - plate seams, thruster
    housings, dust settled in the grooves like on any old rock. At 6s
    the transition band clears: panel edges softening, swelling, losing
    themselves downward into stone; nothing moves. At 8s the hull fills
    more of the frame, its top edge climbing toward the frame top, the
    radiating cracks sliding below the lens. At 10s the push-in holds
    its rate to the final frame: perfect above, unfinished below.
    MUST NEVER APPEAR: the ship moving, trembling, growing, glowing,
    shimmering or pulsing; lit windows, light veins, crystal facets;
    metal shine or any colour; a nosecone, cylinder, fins or launch
    pad; landing gear, debris, scorch marks or anything that would
    explain the ship as having ARRIVED; a visible base line or seam
    where hull meets ground; the ground cracking open or bulging; any
    figure; the push-in becoming a zoom, snapping, or changing rate;
    the sky or the daytime moon changing.
    MOST LIKELY FAILURE: the transition band rendered as a crash - the
    model draws a ship half-BURIED in rubble instead of a ship half-
    GROWN out of continuous stone. The difference between buried and
    grown is the entire film. Second: rocket geometry from "bow-up".

S36 reel 0:50-1:00  85mm  1 figure (the woman)  fixed lockoff  NO SPEECH
    The refusal of exposition. Locked off at eye level, 1.6 meters,
    f/2.8: a tight three-quarter close-up of the woman from her left,
    the half-grown stone ship a soft grey mass behind her.
    MUST BE TRUE: at 0s her eyes are high on the unseen bow, still; she
    breathes once, slow, the breath faintly fogging and clearing low on
    the visor. At 3s her eyes track slowly downward along the hull line
    behind the lens - steady, reading, unhurried. At 5s the eyes reach
    the transition band and STOP: a long beat of absolute stillness. At
    7s one slow blink; her jaw sets by a few millimeters - the only
    change in the whole face. At 10s she holds, eyes fixed low.
    MUST NEVER APPEAR: her mouth opening; any lip movement; a gasp,
    a trembling chin, tears, widened theatrical eyes or raised
    eyebrows - the understanding lives ONLY in the eye line and its
    stop; a second figure or a second face reflected in the visor; the
    scar on the wrong eyebrow; ORANGE turning any other colour; the
    grey mass behind her moving or sharpening; waxy poreless skin; a
    focus rack or any camera movement.
    MOST LIKELY FAILURE: performed emotion. The model reaches for awe -
    open mouth, big eyes, a head shake - and the scene's whole
    argument dies. Grade the face's stillness as strictly as its
    identity.

S37 reel 1:00-1:10  100mm  1 figure (the woman, partial)  fixed lockoff
                                                          NO SPEECH
    The rule's limit is taught. Locked off 1.5 meters, f/4, on the stone
    flank of a complete grey twin: panel seams, rivet bosses, a shallow
    conduit groove, dust in the recesses - and the raised edge lip where
    a stripe should be, holding no colour. In background blur, a sliver
    of the weathered original shows the SAME panel run carrying a faded
    ORANGE stripe. From frame RIGHT, the woman's right arm and shoulder
    enter; her helmeted profile is soft at the frame's right edge.
    MUST BE TRUE: at 0s her index fingertip rests on the empty stripe
    zone, still. At 2s the finger draws slowly along the stripe's raised
    edge lip - a hand-span of travel, light and even. At 5s the finger
    stops; she flattens her whole gloved palm onto the stone and holds
    it there, as if waiting for warmth; the stone gives none. At 7s she
    takes the palm away; fine dust it lifted drifts straight down and
    settles; her eyes go once to the blurred orange stripe behind, then
    return. At 10s the fingertip returns to the grey, resting where
    colour should be.
    MUST NEVER APPEAR: the glove or palm sinking into, merging with or
    denting the stone; a handprint, smear or mark left behind; the stone
    warming visibly, glowing or changing; ANY colour appearing on the
    copy at any second; the background stripe changing or sharpening;
    her profile sharpening into a full face; a second figure; a bare
    hand (no glove comes off in this phase); dust hovering.
    MOST LIKELY FAILURE: the model rewards the touch - a faint glow, a
    colour bloom, a ripple under the palm. The scene means the opposite:
    contact produces NOTHING, and that nothing is the information.

S38 reel 1:10-1:20  50mm  1 living figure + 1 stone figure  fixed lockoff
                                                          NO SPEECH
    Tension moves into human form. Locked off at head height beside the
    woman's soft foreground shoulder at frame LEFT, f/4, looking down a
    lane between wreck pairs. Centered in the lane, in the middle
    distance: a human-sized figure in an old bulky pressure suit seen
    FROM BEHIND - helmet, backpack hump, arms at its sides - rendered
    entirely in matte bone-grey stone, its boots flowing into the basalt
    like roots. It reads exactly person-sized between the towering
    hulls, and its long shadow lies across the lane like all the others.
    MUST BE TRUE: at 0s the lane is still; the grey figure stands
    centered, arms at its sides, facing away. At 3s nothing moves; the
    woman's breathing shifts her soft foreground shoulder by a fraction;
    the figure gives nothing. At 5s a thin weak drift of low dust
    crosses the lane floor, parting around its rooted boots, and
    settles; the figure does not react. At 7s still nothing. At 10s the
    frame holds - figure unmoved, her shoulder rising once with breath.
    MUST NEVER APPEAR: the standing figure moving in ANY way - a sway, a
    head turn, a settle, a breath, a finger; the figure rendered white,
    clean or pearl-toned; a visible face, visor glass or any light on
    it; the figure standing ON the dust instead of rooted into it; a
    second living figure; camera movement; the stone twins walling the
    lane moving.
    MOST LIKELY FAILURE: the model animates the human shape - it cannot
    resist making a person-shaped thing alive, and a single sway
    destroys both this scene and S39's reveal. Second: the figure drawn
    white, which would pre-empt the Watcher.

S39 reel 1:20-1:30  50mm  0 living figures  slow push-in   NO SPEECH
    The quietest horror frame in the film. One constant-rate push-in
    from two meters to sixty centimeters, starting square-on at the
    stone figure's chest and rising gently to end level with its visor -
    one movement, one rate, no pan, no shake.
    The figure, seen from the FRONT now: an old bulky pressure suit in
    matte bone-grey stone - chest plate, hose loops, wrist couplings,
    every buckle and seam correct, all one toned dry stone, dust in the
    folds. Arms hang at its sides, fingers half-curled. Its boots flow
    into the basalt without a joint. Its helmet is a smooth rounded
    shell with a deep visor recess.
    MUST BE TRUE: at 0s the chest plate fills the frame at two meters -
    stone buckles, stone folds, dust in every crease; nothing moves. At
    3s the push-in climbs slowly across the chest toward the helmet; the
    suit's perfect falseness resolves - cloth folds frozen mid-hang,
    rendered in rock, dust sitting in the creases exactly as it sits on
    the ground. At 6s the visor recess enters center frame: a deep oval
    of shadow where glass should be, its floor smooth, blind, faceless
    stone. At 8s the lens closes to sixty centimeters, level with the
    recess - close enough to see there was never anything inside. At 10s
    the push-in stops on the blind stone face.
    MUST NEVER APPEAR: anything at all in the visor recess - no glass,
    no reflection, no eyes, no face forming, no skull, no hollow socket,
    no light; the figure moving, breathing, swaying or twitching its
    fingers; the stone reading white, clean, wet or translucent; a
    living figure entering frame; the blurred wreck pairs behind
    moving; the push-in becoming a zoom or changing rate.
    MOST LIKELY FAILURE: a face. The model fills the recess - a
    reflection, a skull, a suggestion of eyes - because an empty helmet
    reads as an unfinished render to it. The emptiness IS the shot, and
    it is the setup for a much later scene where a copy does move.

S40 reel 1:30-1:40  85mm  1 living human (partial) + the Watcher
                          fixed lockoff                   NO SPEECH
    THE PHASE'S CLOSING CARD - the film's third character arrives.
    Locked off at chest height, seven meters, f/2.8, down a lane of
    rooted grey stone figures; the woman's out-of-focus shoulder at the
    near LEFT edge. The camera never moves; the only thing that moves in
    the entire frame is the Watcher's turn.
    MUST BE TRUE: at 0s the white figure faces away, utterly still - but
    STANDING on the dust, not rooted, its own clean shadow beside it. At
    2s it begins to turn toward the lens: one slow continuous rotation
    that will take the rest of the shot; the motion is liquid, it does
    not start and stop. At 5s the turn carries the smooth helmet through
    profile and the leading edge of a single OPAQUE dark grey-green
    visor slides into view; the long arms hang undisturbed through the
    whole motion. At 8s the turn continues past profile - deliberate,
    unhurried. At 10s the frame ends MID-TURN, the opaque visor edge
    angled toward the watchers. The rotation never completes.
    MUST NEVER APPEAR: the turn stopping, restarting, accelerating,
    jerking or completing; dust on the white suit, wear, seams, panel
    lines or markings of any kind; the suit glowing or emitting; the
    visor showing a face, eyes, light or anything behind it; the
    anatomy changing - height, silhouette, limb count, arm length or
    finger count shifting between frames; more or fewer than three
    fingers and a thumb on a glove; the figure rooted into the ground
    like the stone ones; any stone figure moving; a second living
    human; camera movement of any kind.
    MOST LIKELY FAILURE: morphing. A tall unfamiliar body in slow
    rotation is the single strongest morph trigger this production has -
    limbs lengthening, the helmet reshaping, the silhouette breathing.
    Second: the model dirties the white suit to "match" the world; the
    dustlessness is the character's whole tell.


================================================================
WHAT TO SCORE — ten categories, 1 to 10
================================================================

 1. COPY MATERIAL DISCIPLINE - every copy matte bone-grey stone, single
    tone, unmarked, unlit, rooted with no base line. The S32 anchor and
    every later copy speaking the same material language. S33's veins
    matte, not glowing.
 2. NO REAL-TIME GROWTH - nothing grows, rises, swells or spreads on
    camera anywhere; the ground never opens, bulges, breathes or glows;
    every copy holds its exact shape for its full ten seconds.
 3. THE WHITE FIGURE LOCK - no white, clean or pearl-toned figure in
    S31-S39; the S38/S39 figures grey, dusty, rooted and utterly still;
    the Watcher's S40 spec held (2.10 m, dustless, three fingers, long
    arms, opaque visor, standing not rooted, one unbroken turn).
 4. IDENTITY CONTINUITY - do the two faces hold across S31, S33, S34,
    S36? Bone structure, age, eye spacing, skin. Scars on the correct
    sides in every appearance: her LEFT eyebrow, his RIGHT cheekbone.
 5. COSTUME, EQUIPMENT & FIGURE COUNT - orange/teal never swapped, the
    13 cm height difference, the oversized back module, the closed
    sheath, clear visors, all helmets sealed and no bare skin anywhere;
    exact figure counts per the scene table.
 6. CAMERA DISCIPLINE - one unbroken take per scene, at most one
    movement, one constant rate, no shake anywhere. Boundary cuts are
    NOT findings (STEP 0). S32 alone may read as slowed motion.
 7. PHYSICS & MATERIALS - 0.9g steps: soft but weighted; dust rises
    low, settles at once, never hangs or swirls; gloves, palms and boots
    keep clear boundaries against every surface; stone behaves as stone
    under load.
 8. LIGHT DISCIPLINE - dawn confined to S31; S32-S40 identical soft
    orange 4400K daylight, key always frame LEFT, soft-edged shadows,
    pale grey-green sky, faint daytime moon; no lamps, no night, no
    emitting object.
 9. PHASE CHAIN - does the phase read as one continuous morning? Does
    S31 carry on the walk without a break in gait or costume? Does the
    light lock hold unchanged from S32 to S40? Is the S38 figure the
    same figure S39 approaches? Is the S40 lane consistent with the
    S38/S39 lane? Does the field's geography stay coherent across S34,
    S35, S37, S38, S39, S40?
10. DELIVERY HYGIENE - no title card, no end card, no credits, no
    captions, no watermark, no logo, no hull lettering. Film grain
    present and consistent. Each scene lands at 10 seconds.

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
      phase, so COPY MATERIAL DISCIPLINE and PHASE CHAIN are fully
      auditable across clips. For category 9, judge continuity across
      the clips in scene order - there are no boundary cuts to excuse
      because there are no boundaries.
    - MODE S scores only what one clip can show. Category 9 (PHASE
      CHAIN) is always UNVERIFIABLE. Category 3 is scored only against
      what the declared scene shows. Categories that need two figures
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
    end, measured length, and whether it is 10.0 s (+/- 0.3) - shorter
    native-8s segments are duration findings, not mapping errors.

COPY MATERIAL TABLE
    Five rows - one per law: (1) matte bone-grey single tone, (2) no
    markings, (3) no light of its own, (4) rooted with no base line,
    (5) never moves. For each law, its state in every scene where a copy
    appears: S32, S33, S34, S35, S37, S38, S39, and the stone figures at
    the edges of S40. Flag every deviation with scene and second.
    Add a sixth row for S33's ROOT VEINS: present, matte, unlit.

WHITE FIGURE LEDGER
    One line per scene S31 through S39: was any white, clean or
    pearl-toned figure visible anywhere in frame - yes/no, with a
    timecode if yes. Then one block for S40 walking the Watcher spec:
    height, dustlessness, arm length, finger count, visor opacity,
    rooted-or-standing, and whether the turn is one continuous
    incomplete rotation.

PASSPORTS AS SEEN
    What you actually observed for the woman, the man, the copies, the
    ground and the light - before comparison.

SCORES
    Ten rows, one per category, with a one-line justification each, then
    the computed mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: timecode,
    scene, severity, what is wrong, why it matters.

SCENE-BY-SCENE FINDINGS
    S31 through S40 in order. For each: what you verified as correct
    (briefly), then each deviation with a timecode and a severity. If a
    scene is clean, say so in one line and move on.

PHASE CHAIN
    Judged across the ten scenes in order (mode T: across the clips;
    mode R: across the reel). Does S31's dawn hand over to a locked
    daylight that never shifts again? Is the key always from frame LEFT?
    Do the copies in S32, S34, S35, S37, S38 and S39 look like the same
    material? Is the lane in S38, S39 and S40 the same place? Do the
    walkers' suits, wear and gait carry unchanged from S31 to S34?

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
    What you actually observed in this clip - figures, suits, copies,
    ground, light - before comparison.

COPY MATERIAL CHECK
    One line per law (tone / markings / light / rooted / motion) for
    every copy visible in this clip: what the spec REQUIRES, what you
    SEE, verdict. If the clip contains no copy, say so.

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
- Do not report a scene as "missing". The material contains what it
  contains. If S35 does not match its row, that is a deviation IN S35.
- Do not invent a bible, a plan, a script or a scene that is not in the
  scene table.
- Do not report the absence of dialogue, footsteps, wind or ambient audio
  as a defect. The material is silent by design.
- Do not report the absence of lip movement as a defect. Nobody speaks in
  this phase.
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

## Faz 3 rubriğinden farkları

Aynı iskelet (üç mod, otomatik seçim, CLIP MAP, içerik-satır çelişki
kuralı, tek yönlü konuşma kilidi), ama denetlenen nesne değişti: gemi
hasarı gitti, yerine KOPYA geldi.

```
− HASAR DONDURMA TABLOSU    ekibin gemisi bu fazda kadrajda yok; dört
                            kalıcı işaret denetimi F5'e kadar askıda
+ KOPYA MALZEME TABLOSU     beş yasa × sahne matrisi (tek ton · işaret
                            yok · ışık yok · köksüz taban yok · hareket
                            yok) + S33 damar satırı  [KARAR 2]
+ BEYAZ FİGÜR DEFTERİ       S31-S39 için sahne sahne "beyaz figür var
                            mı" satırı + S40 Bekçi spec bloğu
                            [KARAR 3 · F3 dersi D-L]
+ GERÇEK ZAMANLI BÜYÜME     ayrı kategori: kopyalama saatler ölçeğinde
  YASAĞI                    işler, kamerada asla — maksimum severity
+ IŞIK GEÇİŞ KİLİDİ         şafak YALNIZ S31; S32-S40 birebir aynı
                            4400K gündüz, key hep sol  [KARAR 1]
+ SIFIR KONUŞMA             F3'te iki sahne konuşuyordu; bu fazda on
                            sahnenin onunda da ağız kapalı — tek yönlü
                            kilit korunur (hareketsizlik bulgu değil)
+ ROKET NEGASYONU           S34/S35 gövdeleri kutu endüstriyel; koni/
                            fin/silindir maksimum severity [F3 D-K]
+ EŞLEŞME YASASI            S34: her enkazın yanında aynı eksende,
                            aynı siluetli ikizi; fark yalnız olgunluk
                            ve renk
+ RENK YASASI               S37: biçim kopyalanır, renk kopyalanmaz —
                            dokunuşta renk/parlama belirirse bulgu
+ BOŞ VİZÖR YASASI          S39: oyukta cam/yansıma/göz/yüz/kafatası
                            YOK — model boşluğu doldurmaya en yatkın
                            olduğu kare
+ MONTAJ PROTOKOLÜ ÖNE      MODE T tercih edilen mod ilan edildi; F1 ve
                            F3'te reel sırası karıştı, iki koşu yandı
                            [F3 dersi ④]
```
