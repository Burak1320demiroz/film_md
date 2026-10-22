# 🔍 FAZ 1 / TRANSİT — VİDEO ELEŞTİRİ PROMPTU

## On sahne · 1 dakika 40 saniye · 16:9 · faza özel rubrik

> **Ne işe yarar:** Faz 1'in on sahnesi birleştirilip 1:40'lık tek video
> olduğunda, o videoyu bu fazın KENDİ kilitlerine karşı denetler.
> Genel rubrikler (`QA_PROMPTLARI/`) filmi tanımaz — bu prompt Faz 1'in
> sahne haritasını, kimlik pasaportlarını ve sayısal kilitlerini
> içinde taşır. Sapmayı bu yüzden görebilir.
>
> **Nasıl kullanılır:**
> 1. On sahneyi sırayla birleştir (S1→S10, arada geçiş efekti KOYMA).
> 2. Videoyu Gemini'ye yükle.
> 3. Aşağıdaki kod bloğunun **içini** kopyala, başka hiçbir şey ekleme.
> 4. Türkçe açıklama, dosya adı, bu satırlar — hiçbiri prompta girmez.
>
> **Rapor geldiğinde:** ham çıktıyı
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/`
> altına `THE_SECOND_SHIP_FAZ01_HAM.md` olarak kaydet.
> ⛔ Bu bir **faz** ölçümüdür, film ölçümü değil. Skoru
> `03_HIKAYE` / `04_MANTIK` / `06_KARAKTER` tablolarına **yazma** —
> o tablolar tamamlanmış filmler içindir. `00_INDEX` sayacına da girmez.

---

## PROMPT — buradan aşağısı kopyalanır

```
ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing ONE reel: the first phase of a 100-scene science
fiction film. You judge the PICTURE. You are precise, specific and
unsentimental. You never soften a finding and you never invent one.

WHAT YOU HAVE

- One video: 10 scenes, 10 seconds each, 100 seconds total, 16:9.
- The LOCKED SPEC below. It is ground truth, not a suggestion. Everything
  you need to judge this reel is in it. You were not shortchanged on input:
  do not ask for a bible, a plan or a script, and do not treat their
  absence as a defect of the production.


⛔ STEP -1 — MATERIAL GATE (do this before anything else)

Measure two numbers and write them down:
    measured total duration = ___ seconds
    number of distinct scene-length segments you can count = ___

Expected: 100 seconds (+/- 3) and 10 segments of about 10 seconds each.

If the measured duration is under 60 seconds, OR you count fewer than 8
segments, then what you have is not the phase reel. In that case your
ENTIRE output is this one line and nothing else:

    MATERIAL GATE FAILED - measured __ s, __ segments. Not the phase reel.

Then stop. Do not print the passports. Do not print the score table. Do not
print findings. There is no score field to fill in this case and no section
of this rubric applies below this line.


⛔ STEP 0 — THE COMPILATION RULE (read it twice, it is the most common
              way an auditor wastes this whole report)

This reel is a COMPILATION. Each of the 10 scenes was generated as a
separate clip and they were laid end to end. A cut at every scene boundary
is REQUIRED BY THE ARCHITECTURE.

There are exactly 9 legitimate boundaries:
    0:10  0:20  0:30  0:40  0:50  1:00  1:10  1:20  1:30

NEVER report a cut, an angle change, a location change or a lighting change
AT one of those boundaries as an error, a hidden cut, a continuity break or
a blocker. It is the design.

DO report, at maximum severity, any cut, camera reset, angle jump, sudden
reframe or teleport that happens INSIDE a 10-second scene. Each scene must
be one unbroken take with at most one camera movement.


⛔ STEP 0.5 — NUMBERING BASE

Scenes are numbered S1 through S10 and map to time 1:1:
    S1 = 0:00-0:10   S2 = 0:10-0:20   S3 = 0:20-0:30   S4 = 0:30-0:40
    S5 = 0:40-0:50   S6 = 0:50-1:00   S7 = 1:00-1:10   S8 = 1:10-1:20
    S9 = 1:20-1:30   S10 = 1:30-1:40

Never renumber. Never start from zero. Never invent a scene outside S1-S10.
EVERY finding you write carries both a timecode (m:ss) and a scene number.
A finding without a timecode is deleted before you output it.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before you compare anything against the spec, write down what you ACTUALLY
SEE, in your own words, for each of these:
    - the woman (face, hair, suit colour accents, build)
    - the man (face, hair, suit colour accents, build)
    - the cockpit interior
    - the exterior / orbital shots

Only then compare against the LOCKED SPEC. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec. The whole value of this pass is
catching the difference.


================================================================
LOCKED SPEC — FAZ 1 / TRANSIT
================================================================

FORMAT
    10 scenes, exactly 10.0 s each, 100 s total, 16:9 horizontal.
    Every scene is a single unbroken take with 0 internal cuts.
    Maximum one camera movement per scene, at one constant rate.

AUDIO
    All 10 scenes were generated SILENT. Dialogue, the recorded
    announcement and all atmosphere are added in post-production.
    Therefore: never grade lip-sync against the soundtrack, and never
    report "no audio" or "mouth moves but no sound" as a defect. You judge
    lips ONLY against the WHO SPEAKS column of the scene table below.

ERA
    This phase happens in transit, before anything goes wrong. The ship is
    intact. There is no hole, no collapsed landing leg, no tilt, no dust
    on anyone, no injury, no damage of any kind anywhere in this phase.

LIGHT
    Night and space only. There is no daylight anywhere in this phase.
    Grey-blue moonlight reads about 7000K. Cockpit console light is a warm
    amber about 2800K. No other light source exists in these 10 scenes.

TEXT
    There is no readable text in this film at any point: no letters, no
    digits, no numerals, no glyphs, no icons, no labels, no insignia, no
    HUD readouts, no subtitles, no captions, no title card, no end card,
    no credits, no watermark. Console displays carry abstract light only.
    Any readable character anywhere is a finding.

WHAT IS NOT IN THIS PHASE (if you see it, it is a deviation)
    - the ship seen from outside, at any distance
    - any third figure, human or otherwise
    - the tall sealed white figure
    - any planet surface walking, any spacewalk, any airlock
    - daylight, a star, a sunrise
    - fire, explosion, sparks, smoke, alarm strobes


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

SEPARATION LOCK (applies wherever both appear)
    ORANGE belongs to the woman, TEAL GREEN to the man, and they never
    swap. His head sits 13 cm higher than hers in every frame. She has a
    tight low bun and no facial hair; he has very short black hair and
    stubble. Scar left eyebrow (her) / right cheekbone (him). These four
    markers must be independently readable whenever both are in frame.

HELMET LOCK
    In every interior scene both humans wear an integrated helmet with a
    fully transparent, seamless visor, and the face reads clearly through
    the glass. Nobody ever removes, puts on or adjusts a helmet in this
    phase. A bare head in any interior scene is a blocker.
    The visor is clear uncoated glass: no tint, no mirror coating, no
    reflection so strong that it hides the face. A faint amber console
    reflection is correct and intended - a mirrored or blacked-out visor
    is a finding.

SPEECH LOCK
    On an 85mm lens both faces are readable, so nobody speaks on 85mm.
    Speech happens only where the mouth line cannot be read.
    See the WHO SPEAKS column. Lip movement in a NO SPEECH scene is a
    finding, and the severity is high - it breaks the film's whole
    dialogue strategy.


================================================================
SCENE TABLE — the ground truth, scene by scene
================================================================

S1  0:00-0:10  32mm  0 figures  fixed camera        NO SPEECH
    Night, a planet surface. A dark basalt plain of even, fine, repeating
    grain. A single thin WHITE VERTICAL LINE stands perfectly plumb.
    ONE pale grey-blue moon hangs HIGH in frame - it is the scene's only
    light source and it is CORRECT and intended. It must read as a small,
    cold, distant disk: judge its size, not its presence. If the moon
    dominates the frame (its disk wider than roughly one tenth of the
    frame width) or sits low enough to give the line a measurable height,
    that is a finding.
    MUST BE TRUE: the frame is completely still for 10 seconds; the line
    is exactly the same width, brightness and position at 0s and at 10s; a
    thin weak veil of low dust drifts across the base of frame and SETTLES
    back down by 8s.
    MUST NEVER APPEAR: any GROUND object that gives away scale - no ship,
    no figure, no lamp, no crater, no boulder, no structure, no horizon
    detail. The scene's entire job is that the viewer cannot tell how big
    the line is.
    MOST LIKELY FAILURE: the moon rendered giant or low, anchoring scale;
    a scale-giving object drifts in; the line bends, tapers, tilts off
    plumb or changes brightness; the dust swirls, hovers, or flows like
    liquid instead of settling; bloom around the line.
    [Rubric revision 07.08.2026: the first run flagged the moon's
    PRESENCE as RED. The moon belongs to the design; only its SIZE and
    position are auditable.]

S2  0:10-0:20  32mm  0 figures  very slow lateral track   NO SPEECH
    Straight down onto the planet's night surface from orbit. Dark basalt
    plains, wide shallow valleys, dry fracture lines. Scattered across the
    ground: pale grey WRECK PATCHES, and they occur in PAIRS.
    MUST BE TRUE: the pairs are identical to each other in outline and
    length but differ in age/completeness - one member more complete than
    the other. The lateral slide runs at ONE constant rate from 0s to 10s.
    MUST NEVER APPEAR: any wreck patch emitting light, glowing, pulsing
    or having its own colour. They only reflect moonlight, they are pale
    grey. No figure, no ship, no text.
    MOST LIKELY FAILURE: the patches glow; the pairs are not actually
    paired or not actually alike; the track accelerates, stops or
    reverses; the ground morphs, melts or swims under the camera.

S3  0:20-0:30  85mm  1 figure (the woman)  very slow push-in   NO SPEECH
    Tight three-quarter close-up of the seated woman pilot in the cockpit,
    lit by amber console light. Push-in from 1.6 m to 1.2 m.
    MUST BE TRUE: helmet on, visor transparent, face readable through it.
    She is still, eyes off to frame right on a display, unimpressed. She
    blinks once, slowly, around 5s and her eyes track a short distance.
    Her mouth stays closed for all 10 seconds.
    MUST NEVER APPEAR: any lip movement, any speech, any second person or
    reflection of a second person, a mirrored visor, the scar on the wrong
    eyebrow, the push-in becoming a zoom or a jump.
    MOST LIKELY FAILURE: her face drifts from the passport - jaw, nose,
    eye spacing, age; the eyebrow scar migrates or disappears; the visor
    goes mirrored; skin turns waxy or airbrushed.

S4  0:30-0:40  50mm  1 figure (the man)  fixed camera   NO SPEECH
    A narrow service corridor, lockoff down its length, 2.5 m. He works a
    ring collar at chest height with both gloved hands.
    MUST BE TRUE: helmet on. At 3s he tilts his head and presses the SIDE
    of his helmet flat against a pipe - listening through the helmet. At
    8s he lays the flat of one gloved palm across the pipe. He is
    satisfied at 10s. The oversized back tool module is present.
    MUST NEVER APPEAR: any handheld tool - the cutting-tool sheath stays
    CLOSED and empty-handed for the whole scene. No bare head, no bare
    ear against the pipe. His hand must not merge, sink into or phase
    through the pipe - contact keeps a clear structural boundary.
    MOST LIKELY FAILURE: a tool materialises in his hand mid-shot;
    equipment appears or disappears between 0s and 10s; the glove fuses
    with the pipe; the burn scar moves to the wrong cheek.

S5  0:40-0:50  50mm  2 figures  fixed camera        SHE SPEAKS, HE ANSWERS
    Locked off behind and between the two cockpit seats, 3.5 m. Both are
    seated, both face their own consoles.
    MUST BE TRUE: exactly two people. She speaks a short line at 3s
    WITHOUT turning her head; he answers at 5s, also without turning; she
    gives a single small nod at 7s. Neither of them looks at the other at
    any point. Lip movement is short and low-amplitude - the mouths are
    small in frame and the lines are added in post.
    MUST NEVER APPEAR: a third person, a duplicate of either of them, a
    reflection that reads as an extra crew member, colour swap (orange on
    him, teal on her), the height difference collapsing, either of them
    turning to face the other.
    MOST LIKELY FAILURE: this is one of only two scenes in the phase with
    two humans in frame - it is the highest clone risk in the reel. Check
    the seat behind and beside them for a duplicate. Check that the two
    faces do not converge toward each other over the 10 seconds.

S6  0:50-1:00  100mm macro  0 figures  fixed camera     NO SPEECH
    Macro on a scuffed dark grey-brown cockpit console face between two
    worn crew seats, 80 cm. A single horizontal AMBER STRIP is the only
    light source in frame, 2800K, lit from the left, with one clean sharp
    boundary where the lit part ends.
    MUST BE TRUE: total stillness. Between 0s and 10s the boundary creeps
    to the right by a hair's width - so little it is almost deniable. A
    faint cold blue spill from an off-frame indicator brightens slightly
    around 7s. The frame at 10s reads as the same frame as at 0s.
    MUST NEVER APPEAR: any digit, numeral, tick mark, scale, gauge
    marking or label on or near the strip. No shoulder, arm, hand, knee or
    helmet entering frame - this is a 0-figure shot. The strip must not
    read as a countdown, must not step, blink or jump.
    MOST LIKELY FAILURE: numbers appear on the bar; the bar shortens
    visibly enough to read as a timer; a body part drifts into frame; the
    amber strip blooms and washes the console.

S7  1:00-1:10  50mm  1 figure (the man)  slow push-in     NO SPEECH
    He leans toward a side display in the cockpit. Push-in 3.0 m to 2.2 m.
    On the display: an abstract signal trace that REPEATS ITSELF EXACTLY.
    MUST BE TRUE: helmet on. The pattern completes and repeats a second
    time, beat for beat identical, so the viewer registers "that is the
    same thing again". At 3s his right gloved hand slides a short control
    a small distance. At 7s he lifts his eyes off the display toward the
    black outside. His mouth stays closed.
    MUST NEVER APPEAR: any letter, digit or readable symbol in the trace;
    the pattern being decorative noise instead of an exact repeat; a
    second repeat that differs from the first; speech.
    MOST LIKELY FAILURE: the display carries alphanumeric characters; the
    "signal" is random animated noise so the repetition never reads.

S8  1:10-1:20  85mm  2 figures  fixed camera        NOBODY SPEAKS
    Cramped cockpit, lockoff at head height, 3 m. The woman in profile in
    the LEFT foreground, the man behind and to the right. A console strip
    pulses slowly in amber - it is the only thing representing the
    announcement they are hearing.
    MUST BE TRUE: both sit completely still, facing forward. The strip
    pulses on a slow steady beat at 0s, 3s and 10s. At 5s he turns his
    head a FEW DEGREES toward the strip - no more. At 7s she blinks once
    and does NOT turn, does not look at him. Nobody reacts. The
    non-reaction is the point of the scene.
    MUST NEVER APPEAR: ANY lip movement from either of them. This is the
    strictest lock in the phase: at 85mm both mouths are readable and the
    announcement is a recording being heard, not spoken. Also never: a
    subtitle or caption of the announcement, any text on the console, one
    of them turning to face the other, an alarm light, a strobe.
    MOST LIKELY FAILURE: one of them mouths words; the model animates a
    "reaction" - a startle, a head turn, a widening of the eyes; a
    caption of the spoken warning burns into the frame.

S9  1:20-1:30  50mm  1 figure (the woman)  fixed camera   SHE SPEAKS ONCE
    Lockoff at shoulder height on her right, 2.8 m. She is seated
    three-quarter, head turned down and away toward the console.
    MUST BE TRUE: at 0s her right hand rests flat on the console beside
    the pulsing strip. At 2s she presses two fingers down and THE PULSING
    STRIP GOES OUT - this is the visual link back to S8. At 4s, still
    looking down and away, she says one short line with her mouth line
    away from camera. At 8s she places her LEFT HAND FLAT OVER THE THREE
    ABSTRACT CHEST INDICATORS. At 10s she takes the hand away and faces
    forward.
    MUST NEVER APPEAR: the RIGHT hand on the chest indicators instead of
    the left; the gesture being skipped, rushed or turned into something
    else; the amber pulse still running after 2s; her mouth line readable
    while she speaks.
    MOST LIKELY FAILURE: the hand-on-chest gesture is the single most
    important beat of this phase - it is repeated twice later in the film
    and pays off at the climax. Verify it happens, that it is the LEFT
    hand, that the palm is FLAT, and that it lands on the chest
    indicators and not on the collar, the belly or the shoulder.

S10 1:30-1:40  32mm  0 figures  fixed camera        NO SPEECH
    Locked off in high orbit, level with the planet's limb. The night
    hemisphere fills the lower two thirds. A single POINT OF LIGHT on the
    dark surface.
    MUST BE TRUE: the point is small, sharp-cored and perfectly still at
    0s. From 3s it WIDENS - slowly, evenly, without flicker - into a
    circle, at one calm constant rate, holding at its widest at 10s. It is
    a real light source: it emits, with a sharp centre and a fast falloff.
    MUST NEVER APPEAR: the light RISING, travelling, drifting or moving
    across the surface - it only grows in place. No bloom, no glow filter,
    no lens flare, no starburst, no shockwave, no debris, no fireball. It
    is an opening, not an explosion.
    MOST LIKELY FAILURE: it reads as an explosion; it blooms and washes
    the frame; it lifts off the surface like a launch; it flickers or
    pulses instead of growing evenly.


================================================================
WHAT TO SCORE — ten categories, 1 to 10
================================================================

 1. IDENTITY CONTINUITY - do the two faces hold across S3, S4, S5, S7,
    S8, S9? Bone structure, age, eye spacing, skin. Scars on the correct
    sides in every appearance.
 2. COSTUME & EQUIPMENT - suit colour assignment, the back module, the
    wrist ring, the closed sheath, chest indicators. Nothing appears or
    disappears mid-shot.
 3. FIGURE COUNT & CLONE CONTROL - exact counts per the table. Special
    attention to S5 and S8, the only two-figure scenes.
 4. CAMERA DISCIPLINE - one unbroken take per scene, at most one movement,
    at one constant rate, no shake, no reset, no zoom substituted for a
    push-in. Boundary cuts are NOT findings (STEP 0).
 5. LIGHT & COLOUR - amber console 2800K, moonlight 7000K, no other
    source; no daylight; consistent direction; no bloom.
 6. PHYSICS & MATERIALS - dust settles and stays settled, never hovers or
    swirls; hands contact surfaces without merging; nothing floats.
 7. TEXT & SYMBOL DISCIPLINE - zero readable characters anywhere.
 8. PHASE CHAIN - does the reel read as one continuous 100 seconds? The
    cockpit must be the SAME cockpit in S3, S5, S6, S7, S8, S9. The amber
    strip that pulses in S8 must be the strip she switches off in S9.
 9. NOVUM DISCIPLINE - S1's line must stay unexplained and unscaled; S2's
    pairs must be noticeable but unremarked; S10 must not be an explosion.
    The phase's job is to plant three questions without answering any.
10. DELIVERY HYGIENE - no title card, no end card, no credits, no
    captions, no watermark, no logo. Film grain present and consistent.
    Each scene lands at 10 seconds.

SEVERITY
    RED     blocker - the scene has to be regenerated
    YELLOW  fixable in the edit (trim, reorder, crop, speed)
    GREEN   note - worth knowing, not worth spending on

Scoring rules:
    - The overall score is the arithmetic mean of the ten category scores.
      Compute it from your own table. Do not state an overall score that
      your table does not produce.
    - A category with no observed problem is not automatically 10. Say
      what you verified.
    - Never give a category a number if you could not observe it. Write
      UNVERIFIABLE and leave it out of the mean.


================================================================
OUTPUT FORMAT — use exactly this structure, in this order
================================================================

MATERIAL
    measured duration, segment count, and whether the gate passed.

SEGMENT MAP
    Ten rows: scene, measured start, measured end, measured length,
    and whether it is 10.0 s (+/- 0.3).

PASSPORTS AS SEEN
    What you actually observed for the woman, the man, the cockpit and the
    exterior - before comparison.

SCORES
    Ten rows, one per category, with a one-line justification each, then
    the computed mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: timecode,
    scene, severity, what is wrong, why it matters.

SCENE-BY-SCENE FINDINGS
    S1 through S10 in order. For each: what you verified as correct
    (briefly), then each deviation with a timecode and a severity. If a
    scene is clean, say so in one line and move on.

PHASE CHAIN
    Does the cockpit hold across its six scenes? Does the S8 to S9 amber
    strip link land? Do the three planted questions survive unanswered?

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
    Two lists. For the edit list, say what the trim or crop would be.

FLAGS FOR DOCUMENT CHECK
    Things you cannot settle from the picture alone and that a human must
    answer from the production files. Write them as direct questions.
    This section is where the most valuable findings usually live - do not
    leave it empty out of politeness.

WHAT WORKED
    Maximum five lines. Specific, with timecodes. No general praise.


================================================================
RULES AGAINST INVENTION - violating these makes the report worthless
================================================================

- Never state a credit, runtime, scene count, lens or intent that you did
  not measure or that is not in the LOCKED SPEC. If you did not measure
  it, you do not know it.
- If something is not visible, write "not visible". That is different from
  "missing" and different from a guess.
- Do not report a scene as "missing". The reel contains what it contains.
  If S7 does not match its row, that is a deviation IN S7.
- Do not invent a bible, a plan, a script or a scene that is not in the
  scene table.
- Do not report the absence of dialogue audio as a defect. The reel is
  silent by design.
- Do not report scene-boundary cuts. See STEP 0.
- Every finding carries a timecode and a scene number, or it is deleted
  before you output.
- Words like "probably", "seems intended to", "may have been" mean you are
  guessing. Cut the finding or move it to FLAGS FOR DOCUMENT CHECK.
- Your recommendations must be physically achievable in a re-render of a
  10-second locked-off shot. Do not recommend coverage, inserts, reaction
  shots or camera moves that the format does not have.
```

---

## Sonraki fazlar

Bu dosya Faz 1'e özeldir — sahne tablosu, kilitler ve "en olası hata"
satırları yalnızca S1–S10 için geçerlidir. Diğer fazlar için aynı iskelet
kendi sahne tablosuyla yeniden yazılır:

```
FAZ_02_VURULMA/FAZ_02_QA_PROMPT.md    S11–S20 · 1:40 – 3:20
FAZ_03_IMDAT/FAZ_03_QA_PROMPT.md      S21–S30 · 3:20 – 5:00
FAZ_04_TARLA/FAZ_04_QA_PROMPT.md      S31–S40 · 5:00 – 6:40
FAZ_05_TEMAS/FAZ_05_QA_PROMPT.md      S41–S50 · 6:40 – 8:20
FAZ_06_KULE/FAZ_06_QA_PROMPT.md       S51–S60 · 8:20 – 10:00
FAZ_07_BEDEL/FAZ_07_QA_PROMPT.md      S61–S70 · 10:00 – 11:40
FAZ_08_TIRMANIS/FAZ_08_QA_PROMPT.md   S71–S80 · 11:40 – 13:20
```

⚠️ Faz 2'den itibaren SPEC'e eklenecek olanlar: gemi hasarı (S13'ten sonra
kalıcı — 1.2 m delik, çökük sağ ayak, 4 derece yatıklık), yıpranma tek
yönlüdür (temizlenmez), Bekçi'nin opak vizörü ve sabit anatomisi (F4'ten
itibaren), kopya malzemesinin mat kemik grisi kalması, zeminin klip içinde
statik olması.
