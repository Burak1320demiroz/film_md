# 🔍 YERÇEKİMİ — FAZ 1 / GÖREV · VİDEO ELEŞTİRİ PROMPTU

## ⭐ SIRADAN BAĞIMSIZ SÜRÜM — kadraj kataloğu, sahne tablosu değil
### Kaynak kilitler: `FAZ_01_GOREV.md` KİLİT 1-4 · `../README.md` §Negatif Çekirdek · `../REFERANS_PAKETI.md`
### Emsal iskelet: `THE_SECOND_SHIP/FAZ_01_TRANSIT/FAZ_01_QA_PROMPT.md`

> **NEDEN BU SÜRÜM VAR (01.09.2026):** Faz 1 üretildi ama **kliplerin
> sırası karıştı.** Önceki rubrik zaman koduna kilitliydi (S1 = 0:00-0:08
> …); karışık sırada koşulursa her satırı yanlış sahneye bakar ve rapor
> baştan sona çöp olur.
>
> Bu sürüm **sıradan tamamen bağımsızdır.** Denetçiye sahne numarası
> vermez; **on bir KADRAJIN İÇERİK İMZASINI** verir ve şunu söyler:
> _"makaradaki her parçayı bul, hangisi olduğunu KENDİN teşhis et,
> nerede olduğunu yaz, sonra kendi şartnamesine göre yargıla."_
>
> ⭐ Yan kazanç: bu rubrik **eksik ve fazla kadrajı da bulur.** Sıralı
> rubrik "S7 tutmuyor" der; bu rubrik "katalogda D var, makarada yok"
> ve "makarada katalogda olmayan bir parça var" der.

> **Nasıl kullanılır:**
> 1. Klipleri **elindeki sırayla** birleştir — düzeltmeye çalışma,
>    karışık hâli denetlenecek olan şeydir. Araya geçiş/fade/kart/müzik
>    KOYMA.
> 2. Videoyu yükle.
> 3. Aşağıdaki kod bloğunun **içini** kopyala, başka hiçbir şey ekleme.
>
> **Rapor geldiğinde:** ham çıktıyı olduğu gibi
> `FILM_QA_RAPORLARI/02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ01_HAM.md`'ye kaydet
> [AGENTS kural ④ — özetleme, düzeltme yok], sonra bana ver.
>
> ⛔ Bu bir **faz** ölçümüdür. Skoru `00_INDEX`in T1-T4 tablolarına
> **yazma** — o tablolar tamamlanmış filmler içindir.

---

## ⭐ BU KOŞU D124 KAPISINI DA KAPATIR

`00_PLAN.md`'de `KLİP SÜRESİ = ____` hâlâ boş. Rubrik ızgarayı
**varsaymıyor, ÖLÇTÜRÜYOR**: toplam süre ÷ parça sayısı.

```
⛔ Kendi makinende de koş, iki bağımsız ölçüm olsun:
ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>.mp4
```

## ⚠️ İKİ AÇIK MADDE — denetçiye bilerek söyleniyor

```
① S8 (SAAT) İPTAL EDİLDİ, ÜRETİLMEYECEK [31.08.2026]
   Katalog 11 kadraj bekliyor, 12 değil. S8 varsa da bulgu DEĞİL —
   yalnız kayda geçer.

② KOMUTANIN SIRT ÜNİTESİ İKİ TARİF ARASINDA
   REFERANS_PAKETI 31.08'de güncellendi (düz dikdörtgen levha), sahne
   promptları eski tarifi taşıyor (açık boru kafes). Propagasyon
   yapılmadı — bilinçli, karar bekliyor.
   ⛔ Bu yüzden denetçiden sırt ünitesini PUANLAMASI değil TARİF
      ETMESİ isteniyor. Hangisi çıktıysa o yazılır, hata sayılmaz.
```

---

## PROMPT — buradan aşağısı kopyalanır

```
ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing ONE reel: the first phase of a 120-scene science
fiction film set in low Earth orbit. You judge the PICTURE. You are
precise, specific and unsentimental. You never soften a finding and you
never invent one.

⭐ THE ONE THING THAT MAKES THIS AUDIT DIFFERENT

THE SHOTS IN THIS REEL ARE IN THE WRONG ORDER, AND THAT IS EXPECTED.

They were generated separately and assembled in an arbitrary sequence.
You are NOT auditing the order. You are auditing WHAT IS PRESENT.

Therefore:
  - NEVER report "the order is wrong", "this shot comes too early",
    "the sequence is confusing" or anything about narrative flow.
    Order is not a finding here. Not once.
  - NEVER assume shot number N is at position N.
  - Instead: identify every segment by WHAT IS IN IT, match it to the
    catalogue below, and judge each one against ITS OWN entry.

WHAT YOU HAVE

- One video: a number of separately generated shots laid end to end,
  16:9 horizontal, each roughly 8 seconds long, in scrambled order.
- The SHOT CATALOGUE below. It is ground truth, not a suggestion.
  Everything you need is in it. Do not ask for a bible, a plan or a
  script, and do not treat their absence as a defect.


⛔ STEP -1 — MATERIAL GATE AND GRID MEASUREMENT

Measure and write down:
    measured total duration           = ___ seconds
    number of distinct shot segments  = ___
    measured shot length = total / segment count = ___ seconds

The catalogue expects ELEVEN shots. Ten, eleven or twelve segments are
all plausible material — report the number you actually count, do not
force it to eleven.

If the measured duration is under 45 seconds, OR you count fewer than 6
segments, your ENTIRE output is this one line and nothing else:

    MATERIAL GATE FAILED - measured __ s, __ segments. Not the phase reel.

Then stop.

⭐ THE MEASURED SHOT LENGTH IS ONE OF THE MOST VALUABLE NUMBERS IN THIS
REPORT. State it explicitly. Also state whether the individual segments
are all the same length within 0.3 s, or whether they differ.


⛔ STEP 0 — THE COMPILATION RULE

This reel is a COMPILATION. A cut at every segment boundary is REQUIRED
BY THE ARCHITECTURE. NEVER report a cut, an angle change, a lens change,
a lighting change or a location change AT a segment boundary as an
error, a hidden cut or a continuity break. Adjacent segments are
supposed to look nothing alike.

DO report, at maximum severity, any cut, camera reset, angle jump,
sudden reframe or teleport that happens INSIDE a segment. Every segment
must be one unbroken take with ZERO camera movement — this phase is
locked off throughout. There is not one push-in, pan, tilt, track or
zoom anywhere. Any camera movement inside any segment is a finding.


⛔ STEP 0.5 — HOW TO REFER TO THINGS

Number the segments by their POSITION IN THE FILE you were given:
Segment 1 is the first one you see, Segment 2 the second, and so on.
Give each one its measured start and end timecode.

Separately, each segment gets a CATALOGUE LETTER (A-K) once you have
identified it in STEP 2.

EVERY finding you write carries BOTH: the segment number with its
timecode, AND the catalogue letter. A finding without both is deleted
before you output it. Never use a scene number like "S7" — this reel
has no scene numbers you can trust.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before comparing anything, write down what you ACTUALLY SEE, in your own
words:
    - the woman (face, hair, helmet glass shape, suit stripe colour, back)
    - the man (build, suit stripe colour, WHAT IS ON HIS BACK - describe
      its shape in detail, see the OPEN ITEM below)
    - the platform and the instrument body
    - the shuttle in the distance
    - Earth and the sky

Only then compare against the catalogue. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


⛔ STEP 2 — IDENTIFY EVERY SEGMENT (this is the core of this audit)

Go through the segments one at a time. For each one, decide which
catalogue entry it is, using its CONTENT SIGNATURE - the combination of
scale, how many people are in it, what is being done, and what objects
are present. The catalogue entries are deliberately distinct enough that
each one has a signature no other entry has.

For each segment produce one row:
    Segment N | start-end | catalogue letter | confidence high/low |
    the one detail that settled it

Then produce three lists, and none of them may be skipped:
    MATCHED     - catalogue entries found in the reel
    MISSING     - catalogue entries NOT found anywhere in the reel
    UNMATCHED   - segments that fit no catalogue entry, described in full

If two segments both claim the same catalogue letter, say so explicitly
and describe how they differ - a duplicate generation is a real finding.

If you cannot confidently identify a segment, do NOT guess. Mark it
UNMATCHED and describe what is in it. An honest UNMATCHED is worth more
than a wrong match, because a wrong match makes every later judgement
about that segment wrong too.


================================================================
LOCKED SPEC - CONDITIONS THAT HOLD IN EVERY SHOT
================================================================

FORMAT
    Every shot: 16:9 horizontal, one unbroken take, ZERO internal cuts,
    ZERO camera movement. Locked off, all of them.

AUDIO
    Every shot was generated SILENT. Breathing, the radio band, the suit
    AI and all atmosphere are added in post. Never grade lip-sync
    against the soundtrack, and never report "no audio", "silent" or
    "mouth moves but no sound" as a defect.

ENVIRONMENT - HARD VACUUM, LOW ORBIT, DAYLIGHT
    Every shot is outside, in vacuum, in sunlight. There is NO interior,
    NO airlock, NO station, NO planet surface, NO capsule and NO night
    anywhere in this phase.
    THE PLATFORM: a thirteen-metre white lattice truss with ORANGE
    handrails. At one end, a four-metre grey cylindrical instrument body
    with a hinged access panel on the camera-facing side.
    THE SHUTTLE: about 40 metres beyond the platform. Its NOSE POINTS
    SCREEN-LEFT and its cargo doors are OPEN, in every shot it appears
    in. A shuttle with its nose pointing screen-right, or with closed
    doors, is a finding.
    EARTH: blue-white, cloud-streaked, in the lower and/or left part of
    frame in every wide shot. Black space with hard pinpoint stars
    above. Vacuum has no air: no haze, no glow around objects, no light
    shafts, no visible beams.

NOTHING IS DAMAGED YET
    The platform, the instrument body and the shuttle are all INTACT.
    Nobody is injured, dirty, torn, bent, punctured or scorched. No
    debris impact, no wreck, no floating fragment field near the
    platform, no alarm, no strobe. Damage of any kind anywhere is a
    finding at maximum severity - the story has not reached it yet.

LIGHT
    ONE source: hard white sun, plus a soft cool blue-white bounce
    coming UP from Earth. Nothing else emits light. Shadows are ABSOLUTE
    BLACK with razor edges - vacuum has no fill.
    ⭐ SUN SIDE IS SPLIT BY CAMERA POSITION, and this is deliberate:
        Shots where the camera is on the main side (catalogue A, B, D,
        E, H, I, J, K): sun from UPPER SCREEN-RIGHT.
        Shots where the camera is behind the commander, looking back at
        the platform (catalogue C, F, G): sun from UPPER SCREEN-LEFT.
    A shot lit from the wrong side for its catalogue entry is a finding.
    Bounce always comes from below, on both sides.

TEXT - ZERO CHARACTERS, NO EXCEPTIONS
    No letters, no digits, no numerals, no glyphs, no icons, no labels,
    no insignia, no mission patch, no flag, no HUD readout, no gauge
    marking, no subtitle, no caption, no title card, no end card, no
    credits, no watermark. Every indicator in this film is an abstract
    segmented light with NO number beside it. Any readable character
    anywhere is a finding at maximum severity.

SPEECH LOCK - ZERO READABLE MOUTHS
    Every human voice comes over a helmet radio, and every speaker is
    turned away, too far away, or out of frame. There is NO shot in this
    phase in which a mouth may be read forming words. Any visible lip
    movement anywhere in the reel is a finding, and its severity is high.


================================================================
IDENTITY PASSPORT A - THE WOMAN (flight engineer)
================================================================
    38 years old. 1.70 m, slim, upright.
    Oval face, soft defined jawline, light wheat-toned skin with visible
    pores, thin straight nose, dark hazel eyes.
    A short vertical PALE SCAR on her LEFT TEMPLE, near the hairline.
    Dark chestnut JAW-LENGTH hair, tucked behind both ears.
    Warm off-white pressure suit. Reinforcement stripes are ORANGE.
    Chest: a soft panel, three small coloured lights, NO numerals.
    LEFT cuff: a six-segment amber ring. In this entire phase all SIX
    segments are lit. No numbers on it.
    RIGHT glove cuff: a steel mechanical watch on a black band, and ITS
    HANDS ARE STOPPED throughout. This is intended - see INTENDED.
    HER BACK IS FLAT: smooth off-white shell fabric, one vertical spine
    seam, a low webbing waist belt, and NO pack, tank, hose, cable or
    frame of any kind.

    ⭐ HER HELMET - THE MOST FRAGILE LOCK IN THE FILM
    A rigid white shell with a FLAT RECTANGULAR FRONT GLASS, 24 by 16
    centimetres, held in a VISIBLE BRIGHT METAL FRAME about a finger
    wide - four straight edges, countable. The glass is optically clear:
    zero tint, no mirror coating, face fully readable through it.
    It is a FLAT PANE IN A METAL SURROUND. It is NOT a dome, NOT a
    curved bubble, NOT a seamless wraparound, NOT a gold or mirrored
    faceplate. A dome or a continuous curved bubble with no frame is a
    finding at maximum severity.

================================================================
IDENTITY PASSPORT B - THE MAN (mission commander)
================================================================
    52 years old. 1.85 m, broad and heavy - visibly larger than her.
    Warm off-white pressure suit. Reinforcement stripes are NAVY.
    Helmet with an optically clear visor; his face is never a subject in
    this phase - he is seen from behind, at distance, or in fragments.

    ⚠️ OPEN ITEM - HIS BACK UNIT: DESCRIBE IT, DO NOT SCORE IT
    Two descriptions of his back-mounted unit exist in the production
    files and they were deliberately not reconciled before this shoot.
    One is an open tubular frame with two forward control arms and eight
    corner nozzles; the other is a flat rectangular slab, taller than
    wide, with recessed seams and flush corner nozzle recesses.
    YOUR JOB: describe in detail what is actually on his back - overall
    shape, whether it is an open frame or a closed slab, whether it is
    curved or square, how far it stands past his shoulders, whether
    anything protrudes on an arm or strut, and how many nozzle groups
    you can count. Report it as an OBSERVATION in a section of its own.
    Do NOT score it and do NOT call it a deviation. Whichever it is, it
    must be THE SAME in every shot he appears in - and inconsistency
    between shots IS a finding.

================================================================
SEPARATION LOCK - wherever both people appear
================================================================
    ORANGE belongs to the woman. NAVY belongs to the man. They NEVER
    swap. ONLY the man carries a back unit; her back is flat, always.
    He is 15 cm taller and clearly heavier.
    These three markers must be independently readable whenever both are
    in frame. A colour swap, a unit on her back, or a flat back on him
    is a finding at maximum severity - it is the film's clone gate.

================================================================
VACUUM PHYSICS - the film's hardest rule
================================================================
    Every free object drifts in a STRAIGHT LINE at CONSTANT SPEED with
    continuous momentum. It never hovers, never slows on its own, never
    stops, never curves without a force, never swirls, never flows like
    liquid, never falls.
    Nothing hangs. Nothing settles. No dust billows. No cloth drapes
    downward. Tethers under tension are STRAIGHT.
    Thruster gas is a narrow straight cone that stops the instant the
    valve stops - it never billows, curls, mushrooms or lingers.
    Bodies are never rigid: a figure at rest still drifts and
    counter-drifts slightly. A statue-still human in zero gravity is a
    finding.
    Hands contacting surfaces keep a clear structural boundary - no
    merging, no phasing, no sinking into metal, no extra fingers.


================================================================
⭐ INTENDED - DO NOT REPORT THESE AS ERRORS
================================================================
Read this before writing anything. A previous phase audit on another
film in this series burned its top finding on a design element.

 1. THE SCRAMBLED ORDER. Not a finding. Not once. See the top of this
    prompt.
 2. THE STOPPED WATCH on her right cuff. The hands do not move. It is a
    planted story object. Report it ONLY if the hands DO move.
 3. THE THIN BRIGHT LINE IN THE SKY, small, far, weak, made of tiny
    parallel sunlit points, in the upper screen-left of the two widest
    two-figure shots. It belongs to the design and it is supposed to
    grow slightly. Judge its SIZE and POSITION, not its presence. It is
    a finding only if it is large, close, central, obviously a
    spacecraft, or if a character looks at it.
 4. NEITHER CHARACTER EVER LOOKS UP AT THAT LINE. Their not-noticing is
    the entire point of those shots. Not a missed reaction.
 5. THE FREE BOLT drifting out of frame on one straight line in the
    opening wide shot. It is the zero-gravity proof. A finding only if
    it curves, slows, stops or arcs.
 6. THE SUN CHANGING SIDES between shots. Camera position, not a
    lighting error. See LIGHT.
 7. LARGE SCALE JUMPS BETWEEN ADJACENT SEGMENTS. The film's grammar
    requires it, and the scrambled order exaggerates it.
 8. NO MUSIC, NO DIALOGUE, NO SOUND. Added in post.
 9. THE COMMANDER'S BACK UNIT SHAPE. See the OPEN ITEM. Describe, do
    not score.


================================================================
SHOT CATALOGUE - eleven entries, identified by CONTENT
================================================================
Each entry begins with its SIGNATURE: the smallest set of facts that
tells this shot apart from every other one in the reel. Use the
signature to identify; use MUST BE TRUE and MUST NEVER APPEAR to judge.

⚠️ A twelfth shot - an extreme close-up of a stopped watch and a
six-segment ring on a handrail - was CANCELLED and should NOT be in the
reel. If you find it, record it under UNMATCHED and move on. It is not
an error, and it is not scored.


--- A -- OPENING WIDE, ONE TINY FIGURE, NO SHUTTLE ---------------
SIGNATURE: extreme wide from high above; exactly ONE person, about a
tenth of frame height; NO shuttle anywhere in frame. 24mm.
MUST BE TRUE: she is already halfway through closing a hinged panel
cover when the shot begins - right hand on the cover, left gripping the
rail. Feet free of any surface. An orange-and-white tether runs STRAIGHT
and TAUT from her hip to the rail. About a third of the way in, a single
free bolt crosses frame on one straight line at constant speed and
leaves. Earth's lit curve fills the screen-left two thirds and the
bottom. Camera absolutely still throughout.
MUST NEVER APPEAR: a second person; the shuttle; any damage; the figure
large enough to read her face; a slack, curved or coiled tether; bloom
on sunlit edges; her feet planted on a surface.
MOST LIKELY FAILURE: the model enlarges her to "make her matter" and the
1:10 scale contrast dies; the bolt arcs or slows; the tether droops as
if under gravity; the panel is already shut at the start so no action is
in progress.

--- B -- LATERAL WIDE, ONE FIGURE, SHUTTLE VISIBLE ----------------
SIGNATURE: wide from the side at eye level; exactly ONE person, full
length, in profile; the SHUTTLE is visible far behind. 24mm.
MUST BE TRUE: the panel is now CLOSED and she is reaching for the upper
latch. The shuttle sits about 40 m beyond, NOSE POINTING SCREEN-LEFT,
cargo doors OPEN. Earth in the lower third. Nothing damaged.
MUST NEVER APPEAR: the man; the shuttle nose pointing screen-right;
closed cargo doors; the shuttle moving, manoeuvring or firing anything;
a second vehicle.
MOST LIKELY FAILURE: shuttle orientation flips relative to the other
shots it appears in; the shuttle drifts or rotates during the take; the
truss changes length or handrail colour.

--- C -- OVER THE COMMANDER'S SHOULDER, TWO FIGURES ---------------
SIGNATURE: medium shot from BEHIND the man; his shoulder, the back of
his helmet and a corner of his back unit fill the blurred foreground;
she is sharp in the mid-background at the latch. TWO people. 35mm.
Sun from UPPER SCREEN-LEFT.
MUST BE TRUE: exactly two figures. NAVY stripes and a back unit on HIM;
ORANGE stripes and a FLAT back on HER. A short thin straight cone of
thruster gas may vent from his unit.
MUST NEVER APPEAR: any lip movement from either of them; a third figure;
a reflection that reads as an extra person; a colour swap; a unit on her
back; a plume that billows, curls, mushrooms or lingers.
MOST LIKELY FAILURE: this is one of the reel's highest clone risks -
check for a duplicate of either figure, and check that the foreground
shoulder is genuinely a different body: bigger, navy, with a unit.

--- D -- HER FACE, CLOSE, THROUGH THE VISOR -----------------------
SIGNATURE: the ONLY close shot of her face in the reel. 85mm,
three-quarter front. ONE person.
MUST BE TRUE: the visor reads as a FLAT PANE IN A VISIBLE METAL FRAME.
In the LOWER THIRD of the glass, a faint partial reflection of Earth -
present but weak; it is the only sign that the visor is glass at all.
Face fully readable through it. Calm breathing. Her eyes move; her mouth
stays closed the whole time.
MUST NEVER APPEAR: any lip movement; a mirrored, tinted, gold or
blacked-out visor; a reflection strong enough to hide her face; a dome
or seamless bubble; a reflection containing a PERSON; the temple scar on
the wrong side or missing; airbrushed or waxy skin.
MOST LIKELY FAILURE: the visor renders as a dome and the metal frame
disappears; the Earth reflection becomes a mirror and swallows the face;
her face drifts off the passport - age, jaw, nose, eye spacing.

--- E -- MACRO ON THE LATCH, ONE GLOVE, TOP-DOWN ------------------
SIGNATURE: the tightest shot in the reel; straight down onto a latch;
only ONE gloved hand in frame, nothing else. 100mm.
MUST BE TRUE: the glove turns the latch lever a QUARTER TURN and the
bolt head seats flush. Bare glove - NO TOOL of any kind. The ORANGE cuff
stripe is visible. Camera absolutely still.
MUST NEVER APPEAR: any handheld tool, wrench, driver or gripper; a
second hand; any numeral, tick mark or scale on or near the latch; the
glove merging into the metal; more than five fingers.
MOST LIKELY FAILURE: a tool materialises in her hand; the latch turns
the wrong way or keeps turning past a quarter; markings appear around
the latch; glove and panel fuse at the contact point.

--- F -- HIS GLOVE ON THE CONTROL ARM, FUEL SEGMENTS --------------
SIGNATURE: close on a gloved hand with a NAVY cuff stripe resting on a
control arm; a strip of FOUR segments with exactly TWO lit. No face.
85mm. Sun from UPPER SCREEN-LEFT.
MUST BE TRUE: exactly two of the four segments lit, and the count does
not change during the shot. NAVY cuff. No face, no mouth.
MUST NEVER APPEAR: any digit or number beside the strip; three or four
lit segments; the woman; an ORANGE cuff in this shot; the strip
animating, pulsing or counting.
MOST LIKELY FAILURE: numerals appear next to the segments; the lit count
drifts during the take; the strip reads as a progress bar filling up.

--- G -- THE COMMANDER FROM BEHIND, HE ROTATES --------------------
SIGNATURE: medium shot from behind the man, three-quarter; he is the
only person; he VENTS, ROTATES about ten degrees, then vents again and
STOPS. 50mm. Sun from UPPER SCREEN-LEFT.
MUST BE TRUE: the rotation STOPS after the counter-vent - it does not
continue, because that is what a counter-vent does. His mouth is not in
frame at any point. The platform edge enters from screen-LEFT.
MUST NEVER APPEAR: his face turning far enough to read a mouth; the
woman in frame; the rotation continuing or oscillating after the
counter-vent; a plume that hangs, curls or billows; the unit vanishing
off his back.
MOST LIKELY FAILURE: he keeps spinning after the counter-vent - momentum
handled wrong in the opposite direction; the vent renders as smoke or
fire instead of a thin straight cone of gas.

--- H -- HER FLAT BACK, SHE SEATS THE LAST LATCH ------------------
SIGNATURE: medium shot from behind HER, three-quarter; her BACK is the
main shape in frame; ONE person; she is working a latch. 50mm.
MUST BE TRUE: her back is smooth shell fabric with one vertical spine
seam and a low webbing belt, and NOTHING ELSE on it. The six-segment
ring is visible at the frame edge, out of focus, all six lit,
unemphasised. Her mouth is not in frame.
MUST NEVER APPEAR: any pack, tank, hose, cable or frame on her back; a
mouth; a numeral; the ring pushed into focus or lit up for emphasis.
MOST LIKELY FAILURE: ⭐ THE BACK. The model's default astronaut has a
life-support pack and this film's astronaut does not. This is the shot
where that default is most likely to reassert itself. Check it hard.

--- I -- LATERAL WIDE, TWO FIGURES, SHE CLIPS A HOOK --------------
SIGNATURE: wide from the side at eye level; TWO people, both small; she
clips a hook to the rail and moves hand over hand; he is far away and
small; the SHUTTLE is visible. 24mm.
MUST BE TRUE: exactly two figures, each with its OWN separate movement -
they are not doing the same thing at the same time. Both faces too small
to lip-read. Hand-over-hand movement is continuous, with no push-off
drift and no walking gait. A short straight vent from him. Shuttle nose
SCREEN-LEFT.
MUST NEVER APPEAR: a third figure; a duplicate; a colour swap; either of
them WALKING, stepping or standing on the truss; readable lip movement;
the shuttle nose flipped relative to shot B.
MOST LIKELY FAILURE: the two bodies move in sync as if driven by one
animation vector - the film's declared risk for two-body zero gravity;
one of them acquires a walking gait; the hook attaches to nothing.

--- J -- WIDE FROM ABOVE, TWO TINY FIGURES, LINE IN THE SKY -------
SIGNATURE: extreme wide from high above; TWO people, each about a tenth
of frame height, at OPPOSITE ends of the platform; a thin bright line of
tiny parallel points in the upper screen-left. 24mm.
MUST BE TRUE: each figure at most about a tenth of frame height, each
doing something different. The line in the sky GROWS slightly - a little
longer at the end than at the start - and stays small, far, weak and in
the upper screen-left. NEITHER FIGURE LOOKS UP. The instrument body's
access cover is SEALED.
MUST NEVER APPEAR: the line becoming large, central, close or resolving
into a recognisable spacecraft; either figure noticing it, pointing or
turning toward it; a flash, flare, explosion or shockwave; the figures
enlarged.
MOST LIKELY FAILURE: the model dramatises the line - makes it bright,
big, or gives someone a reaction - and destroys the whole point of the
shot. Second most likely: the panel cover renders OPEN again,
contradicting shots E and H.

--- K -- LATERAL WIDE, ONE FIGURE, SHE RAISES HER HEAD ------------
SIGNATURE: wide from the side at eye level; ONE person at a rail
stanchion; she RAISES HER HEAD and looks SCREEN-RIGHT; the thin line is
in the sky BEHIND her at the upper screen-left. 24mm.
MUST BE TRUE: she looks SCREEN-RIGHT, toward the shuttle - NOT up, NOT
toward the line. One glove comes up beside her helmet. The line stays in
the upper screen-LEFT, behind her, unlooked-at. Shuttle nose still
SCREEN-LEFT. Everything intact.
MUST NEVER APPEAR: her looking up at the line; her looking at camera;
any damage; the line moving to the right side of frame; a second figure;
any lip movement.
MOST LIKELY FAILURE: the model resolves the tension by making her look
at the line. Check her eye and head direction carefully: screen-right is
correct, upper-left is a blocker.


================================================================
⭐ CROSS-SHOT CHECKS - the part that does NOT depend on order
================================================================
These are the only "continuity" judgements in this audit. They compare
shots against each other WITHOUT any assumption about sequence.

 1. IS SHE THE SAME PERSON in every shot she appears in? Bone structure,
    age, eye spacing, skin, hair length. The temple scar on the LEFT in
    every appearance where it is visible.
 2. IS THE VISOR THE SAME GEOMETRY in every shot? Flat pane, metal
    frame, four edges. Name any shot where it changes.
 3. IS HIS BACK UNIT THE SAME OBJECT in every shot he appears in?
    (Describe it once, then say whether it holds. See the OPEN ITEM.)
 4. IS THE SHUTTLE'S NOSE ALWAYS SCREEN-LEFT, with open cargo doors, in
    every shot it appears in?
 5. IS THE PLATFORM THE SAME PLATFORM? Truss length, handrail colour,
    the instrument body's size and position.
 6. THE PANEL COVER: in some shots it is open, in others sealed. List
    which shots show which. Do NOT call either state wrong - just report
    the split, because the correct order is decided elsewhere.
 7. COUNTERS: her ring should read six-of-six lit wherever it is
    visible. His fuel strip should read two-of-four. Report any shot
    where a count differs.
 8. IS EARTH ALWAYS BELOW, and is the sky line always upper screen-left
    wherever it appears?


================================================================
WHAT TO SCORE - eleven categories, 1 to 10
================================================================

 1. COVERAGE - how much of the catalogue is actually present, and how
    confidently could each segment be identified? Score the reel as a
    body of material, not the order.
 2. IDENTITY CONTINUITY - does she hold across every shot she is in?
 3. HELMET AND VISOR GEOMETRY - flat rectangular pane, visible metal
    frame, four countable edges, clear glass, face readable. Score this
    separately and score it hard.
 4. COSTUME AND BACK - orange on her, navy on him, her back flat with no
    pack, ring on the left cuff, watch on the right. (The SHAPE of his
    back unit is not scored - see OPEN ITEM.)
 5. FIGURE COUNT AND CLONE CONTROL - correct counts per catalogue entry.
    Special attention to C, I and J, the only two-figure shots.
 6. CAMERA DISCIPLINE - locked off everywhere, zero movement, one
    unbroken take each. Boundary cuts are NOT findings.
 7. LIGHT AND SHADOW - one sun plus Earth bounce, correct side per
    entry, absolute black razor-edged shadows, no bloom, no flare, no
    haze, no light shafts.
 8. VACUUM PHYSICS - straight lines, constant speed, continuous
    momentum; nothing hovers, settles, swirls or falls; taut tethers;
    thruster gas as a narrow straight cone that stops instantly; bodies
    never rigid.
 9. TEXT AND SYMBOL DISCIPLINE - zero readable characters anywhere.
10. WORLD CONSISTENCY - the cross-shot checks above: same platform, same
    shuttle orientation, same counters, Earth always below.
11. DELIVERY HYGIENE - no title card, no end card, no credits, no
    captions, no watermark, no logo, no letterboxing. Film grain present
    and consistent. Segments the same length.

SEVERITY
    RED     blocker - the shot has to be regenerated
    YELLOW  fixable in the edit (trim, crop, speed, reframe)
    GREEN   note - worth knowing, not worth spending on

Scoring rules:
    - The overall score is the arithmetic mean of the eleven category
      scores. Compute it from your own table. Do not state an overall
      score your table does not produce.
    - A category with no observed problem is not automatically 10. Say
      what you verified.
    - Never give a category a number if you could not observe it. Write
      UNVERIFIABLE and leave it out of the mean.
    - ⛔ There is NO category for order, pacing, flow or structure. Do
      not invent one.


================================================================
OUTPUT FORMAT - use exactly this structure, in this order
================================================================

MATERIAL
    Measured total duration. Segment count. MEASURED SHOT LENGTH (total
    divided by segment count), stated explicitly. Whether all segments
    are the same length within 0.3 s. Whether the gate passed.

SEGMENT MAP
    One row per segment: number, measured start, measured end, measured
    length.

IDENTIFICATION TABLE
    One row per segment: number, timecode, catalogue letter, confidence,
    and the one detail that settled it.

MATCHED / MISSING / UNMATCHED
    Three explicit lists. Never leave MISSING empty without saying you
    checked. Describe every UNMATCHED segment in full.

PASSPORTS AS SEEN
    What you actually observed for the woman, the man, the platform, the
    shuttle and the sky - before comparison.

THE COMMANDER'S BACK UNIT - OBSERVATION ONLY
    A paragraph describing its actual shape, in detail, and whether it
    is identical in every shot he appears in. No score, no verdict.

SCORES
    Eleven rows with a one-line justification each, then the mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: segment
    number, timecode, catalogue letter, severity, what is wrong, why it
    matters.

FINDINGS BY SEGMENT
    Every segment in file order. For each: catalogue letter, what you
    verified as correct (briefly), then each deviation with a timecode
    and a severity. If a segment is clean, say so in one line.

CROSS-SHOT CHECKS
    The eight checks above, answered one by one.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
    Two lists. For the edit list, say exactly what the trim or crop
    would be.

FLAGS FOR DOCUMENT CHECK
    Things you cannot settle from the picture alone and that a human
    must answer from the production files. Write them as direct
    questions. This section usually holds the most valuable findings -
    do not leave it empty out of politeness.

WHAT WORKED
    Maximum five lines. Specific, with timecodes. No general praise.


================================================================
RULES AGAINST INVENTION - violating these makes the report worthless
================================================================

- ⛔ Never comment on the order, sequence, pacing or narrative flow. The
  order is scrambled on purpose and is not being audited.
- Never state a runtime, shot length, segment count, lens, distance or
  intent you did not measure or that is not in the spec above. If you
  did not measure it, you do not know it.
- If something is not visible, write "not visible". That is different
  from "missing" and different from a guess.
- Do not report a catalogue entry as "missing" until you have checked
  every segment for it. Then report it in the MISSING list, not as a
  defect inside another segment.
- Do not invent a bible, a plan, a script or a shot outside the
  catalogue.
- Do not report the absence of audio, dialogue or music as a defect.
- Do not report segment-boundary cuts.
- Do not report anything on the INTENDED list as an error unless the
  specific condition named there is met.
- Every finding carries a segment number, a timecode and a catalogue
  letter, or it is deleted before you output it.
- "Probably", "seems intended to", "may have been", "appears to suggest"
  mean you are guessing. Cut the finding or move it to FLAGS FOR
  DOCUMENT CHECK.
- Your recommendations must be achievable in a re-render of a single
  locked-off shot of a few seconds. Do not recommend coverage, inserts,
  reaction shots, cutaways or camera moves - this format has none.
```

---

# 📌 RAPOR GELDİKTEN SONRA

```
1. Ham çıktıyı OLDUĞU GİBİ kaydet [AGENTS kural ④]:
   FILM_QA_RAPORLARI/02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ01_HAM.md

2. Bana ver. Koşacağım kapılar:
   ⑪ ÖLÇÜM   → raporun süre/parça sayısı ölçümle çelişiyor mu
   ③ KİMLİK  → rapordan belgeye metin-olmayan ≥2 çapa; <2 ise
                UNATTRIBUTED, skor yazılmaz
   ④ KURGU   → ⚠️ BU KOŞUDA DEĞİŞİK: klip sayısı ve süre ölçülür,
                ama SIRA ölçütü UYGULANMAZ (sıra kasten karışık)
   ⑩ ÖNERME  → her iddia kareyle doğrulanabilir mi

3. Üçe ayırırım: gerçek bulgu / raporun uydurması / rubriğin hatası.

4. ⭐ Bu rubriğin ASIL çıktısı üç liste: MATCHED · MISSING · UNMATCHED.
   Kliplerin doğru sırası bu listeden yeniden kurulur — katalog harfi
   ile sahne numarası eşlemesi aşağıda.
```

## 🔑 KATALOG HARFİ → SAHNE NUMARASI (rapor geldikten SONRA kullanılır)

⛔ Bu tablo **denetçiye verilmez** — prompta girmez. Rapor elde olunca
kliplerin doğru sırasını kurmak için burada durur.

| Harf | Sahne | Konum | Kadraj |
|:--:|:--:|---|---|
| A | **S1** | 0:00-0:08 | EWS üst açı · 1 figür · mekik YOK · cıvata |
| B | **S2** | 0:08-0:16 | WS yanal · 1 figür · mekik görünür |
| C | **S3** | 0:16-0:24 | MS OTS · 2 figür · komutanın omzu |
| D | **S4** | 0:24-0:32 | CU · yüz · vizörde Dünya yansıması |
| E | **S5** | 0:32-0:40 | ECU tepeden · tek eldiven · mandal |
| — | ~~S8~~ | — | ⛔ **İPTAL** (31.08) — makarada olmamalı |
| F | **S6** | 0:40-0:48 | CU · komutanın eldiveni · şerit 2/4 |
| G | **S7** | 0:48-0:56 | MS sırttan · komutan döner ve durur |
| H | **S9** | 1:04-1:12 | MS sırttan · A'nın DÜZ sırtı · son mandal |
| I | **S10** | 1:12-1:20 | WS yanal · 2 figür · kanca |
| J | **S11** | 1:20-1:28 | EWS üst açı · 2 figür · gökte çizgi |
| K | **S12** | 1:28-1:36 | WS yanal · 1 figür · başını kaldırır |

⚠️ **S8 iptal olduğu için 1:04'lük yuva boş.** Kurguda ne yapılacağı
karara bağlı — `FAZ_01_GOREV.md` S8 notundaki üç seçenek.

## Sonraki fazlar

Bu iskelet artık **iki sürümlüdür**: sıralı (emsal Second Ship) ve
**sıradan bağımsız** (bu dosya). Klipler karışık geliyorsa ikincisi
kullanılır. Diğer dokuz faz için katalog aynı yöntemle yazılır: her
kadrajın İÇERİK İMZASI çıkarılır, sahne numarası prompta GİRMEZ.
