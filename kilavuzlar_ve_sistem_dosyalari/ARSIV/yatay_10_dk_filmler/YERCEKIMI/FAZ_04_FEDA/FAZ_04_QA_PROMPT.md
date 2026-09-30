# 🔍 YERÇEKİMİ — FAZ 4 / FEDA · VİDEO ELEŞTİRİ PROMPTU

## ⭐ İKİ MÜHÜRLÜ GEÇİŞ — önce KÖR hikâye, sonra KATALOG denetimi
### Kaynak kilitler: `FAZ_04_FEDA.md` KİLİT 13-17 · `../README.md` §Negatif Çekirdek
### Yöntem: **D164** (rubrik ikiye bölünür; ③ yalnız kör geçişten koşulur)

---

# 📋 NASIL KOŞULUR — değişmedi

```
1) YENİ sohbet · makarayı yükle · yalnız PROMPT A. Raporu OLDUĞU GİBİ sakla.
2) İKİNCİ YENİ sohbet (aynı sohbette DEVAM ETME) · makarayı tekrar yükle ·
   yalnız PROMPT B. Raporu OLDUĞU GİBİ sakla.
3) İki raporu birlikte bana ver.

⛔ A ve B aynı sohbette koşulursa belgenin tüm değeri sıfırlanır.
⚠️ Makara sessiz üretildi; "ses yok" iki geçişte de kusur değildir.
```

---

# ⚠️ F3'TEN DÖRT ŞEY DEĞİŞTİ

## ① 🔴 KADRO SAYISI FAZIN ORTASINDA KALICI DÜŞÜYOR

```
F1-F3'te iki karakter vardı ve sayı sabitti. Bu fazda ADAM FİLMDEN ÇIKIYOR.
   İKİ figür : A · G · H · I
   TEK figür : B · C · D · E · F · J · K · L
Sıra karışık olduğu için konumdan bilinemez → her girdi kendi sayısını yazar.
⛔ Bu, denetçinin en kolay yanlış okuyacağı şey: "adam bazı planlarda yok"
   bir kusur DEĞİL, fazın olayıdır.
```

## ② ⭐ BİLEREK ÇEKİLMİŞ NEREDEYSE-AYNI BİR ÇİFT VAR (C ve E)

```
C ve E aynı botun aynı kadrajıdır: 100mm makro, 0,5 m yukarıdan, 35° aşağı.
Ayıran TEK şey sayaç:
   C → üç ilmek, sahne boyunca ÜÇ kalır
   E → üç ilmekle başlar, EKRANDA ikiye düşer
⛔ F2'de birebir kopya GERÇEK bir kusurdu. Burada benzerlik ZORUNLU.
   Rubrik ikisini de tarif ediyor ve ayırt ediciyi veriyor.
   Ama İKİSİ DE sabit üç ilmek gösteriyorsa → o zaman gerçekten kopyadır.
```

## ③ ⭐ BU FAZDA HİÇBİR İTKİ ATEŞLENMEZ

```
Adamın manevra paketinin yakıtı bir önceki fazda bitti (şerit 0/4).
12 klibin hiçbirinde puf YOK. Bir puf görülürse maksimum ciddiyette kusur.
⛔ Ve fedanın anlamı buna bağlı: adam kendini İTMİYOR — bıraktığı için
   dönen yapının savurması onu götürüyor.
```

## ④ ⭐ SON KLİP İÇ MEKÂN — FİLMİN İLK İÇ MEKÂNI

```
L girdisi bir airlock'un İÇİNDE geçer: güneş yok, vakum yok, Dünya yok.
Soğuk beyaz tavan paneli + tek amber acil lamba. Ve kadın KASKSIZDIR.
⛔ Kalan on bir girdi dışarıda, vakumda, alçak altın güneşte.
   Dışarıdaki HERHANGİ bir girdide kask çıkmışsa maksimum ciddiyette kusur.
```

---

# ⚠️ DENETÇİYE BİLEREK SÖYLENMEYENLER — koru

```
1. Vizörün biçimi ve kaskın kadrajdaki görünürlüğü
2. Kadının sırtı  ·  3. Adamın sırtındaki şey
4. Şerit renkleri (kadın TURUNCU · adam LACİVERT)
5. İlmek sayısı ve halka segment sayısı, düşüşleri
6. İstasyonun geometrisi ve gövdenin ekranda hangi tarafta olduğu
7. Güneşin yönü
8. Ekranda yazı olup olmadığı
9. ⭐ AYRILMANIN KAZA MI SEÇİM Mİ OLDUĞU — bu fazın tüm meselesi budur
```

---

# ⚠️ İKİ AÇIK MADDE — B geçişinde bildiriliyor

```
① KOMUTANIN SIRT ÜNİTESİ — TARİF ET, PUANLAMA (yine hiçbir tarif verilmiyor)
   F3'te YEDİ klipte görünüyordu ve ÜÇÜNDE kayboldu. Burada dört klipte.

② İSTASYONUN GEOMETRİSİ — RE paneli hâlâ üretilmedi. I girdisi (40 m'den
   tam boy) bu fazın referans görüntüsüdür; ölçülebilir tarif isteniyor.
```

---
---

# 🅰️ PROMPT A — KÖR GEÇİŞ · buradan aşağısı kopyalanır

```
ROLE

You are watching a reel of footage from an unreleased film and writing a
first-viewing report. You have no script, no plan, no shot list and no
production notes, and none are coming. Everything you say must come from
the picture in front of you.

You are precise, specific and unsentimental. You never soften an
observation and you never invent one. Where you are unsure, you say you
are unsure — that is a real answer and it is worth more than a confident
guess.


WHAT YOU HAVE

- One video: a number of separately generated shots laid end to end,
  16:9 horizontal, each roughly the same length.
- ⭐ THE SHOTS ARE IN THE WRONG ORDER. They were generated separately and
  assembled arbitrarily. Putting them back in the right order is one of
  your jobs, and it is the most important one.
- The shots were generated SILENT. Voices, breathing and atmosphere are
  added later. Never report missing audio, missing dialogue or missing
  music as a defect, and never grade lips against a soundtrack.
- A cut at every segment boundary is REQUIRED by how this was made.
  Never report a boundary cut, or the fact that adjacent shots look
  nothing alike, as an error.


⛔ STEP 1 — MEASURE THE MATERIAL

Write down:
    measured total duration           = ___ seconds
    number of distinct shot segments  = ___
    measured shot length = total / segment count = ___ seconds
    are all segments the same length within 0.3 s?  yes / no

If the measured duration is under 55 seconds, OR you count fewer than 7
segments, your ENTIRE output is this one line and nothing else:

    MATERIAL GATE FAILED - measured __ s, __ segments.

Then stop.

Number the segments by their POSITION IN THE FILE: Segment 1 is the first
one you see. Every observation you write carries a segment number and a
timecode.


⛔ STEP 2 — DESCRIBE, DO NOT INTERPRET

For each segment, in file order, write a short factual paragraph:
    - what the shot is (how close, how wide, from where, moving or still)
    - how many people are in it
    - what objects are in it
    - what physically happens between the first frame and the last

Describe only what is on the screen. No mood words, no adjectives about
tension or emotion, no guesses about what a character feels or intends.
If a thing is hard to see, write "not clearly visible" rather than
choosing a likely answer.


⛔ STEP 3 — WRITE THE PASSPORTS FROM THE PICTURE

This is the most valuable section in your report. Someone will compare it
against a document you have never seen, so describe things as an observer
would, in detail, with numbers where you can estimate them.

For each of the following, describe what you ACTUALLY SEE, and list the
segments you saw it in:

 1. THE SMALLER PERSON. Face shape, apparent age, skin, eyes, hair length
    and colour, any mark on the face. The suit: base colour and the
    colour of any stripes, and where the stripes are. Anything worn on
    the wrists or cuffs, described exactly — including how many of
    anything you can count, and whether that count is the same in every
    segment. THE BACK: describe it — its shape, its surface, and
    everything you can see on it. If there is nothing on it, say that
    explicitly.
 2. WHAT IS ON EACH PERSON'S HEAD, in every segment where a head is
    visible. Describe it as a geometer would: is there a rigid covering,
    and can you trace its outline? If part of it is transparent, does
    that part have countable straight edges and corners, or is it one
    continuous curved surface? Is there a border of a different material
    around it, and how wide? Can you see the face through it, or does it
    return the sky? ⭐ IS THE HEAD COVERED IN EVERY SEGMENT? Name any
    segment where it is not, and describe what you see there instead.
 3. THE LARGER PERSON. Build, suit colours, and — in detail — WHAT IS ON
    THEIR BACK. Describe its overall form, its proportions relative to
    their shoulders, how far it stands out from their body, what its
    surface and its edges look like, and everything that projects from
    it, counted. Say whether it is IDENTICAL in every segment it appears
    in; if not, name the segments and the difference.
 4. THE LARGE STRUCTURE, if you see one. Describe it as if someone had to
    rebuild it from your words: how many separate body sections, how they
    are joined, what is attached above and below, whether the two sides
    match each other, any hole or tear and WHERE along its length, and
    anything docked at either end. ⭐ You will see it at several
    different distances and from several sides. Say whether it is THE
    SAME OBJECT every time. If two segments show it differently, say
    exactly how.
 5. ANY CORD, LINE OR CABLE. In each segment: is it tight or loose,
    straight or curved, and what is it attached to at each end? ⭐ If any
    of it is wrapped around anything, COUNT THE WRAPS and say whether
    that number is the same in every segment where you can count it.
 6. ANY SMALL LIGHTS on a person or on equipment. How many are there in
    total, how many are lit, and is that number the same in every segment
    where you can see them? Note every segment where the number changes
    DURING the shot.
 7. THE SPACE AROUND THEM. What is above, what is below, where the light
    comes from ON SCREEN in each segment, and what colour it is. ⭐ IS
    ANY SEGMENT SET SOMEWHERE FUNDAMENTALLY DIFFERENT FROM THE OTHERS?
    Name it and describe how it differs.
 8. ANY READABLE CHARACTER ANYWHERE. Letters, digits, numbers, symbols,
    logos, patches, labels, gauges with markings, captions, watermarks.
    List every one with its segment and timecode. If there are none, say
    so explicitly — do not leave this blank.


⛔ STEP 4 — REBUILD THE ORDER  ⭐ THE CORE OF THIS REPORT

Put the segments into the sequence you believe they were meant to run in.

Use only the picture. Some things in this world change ONCE and never
change back. Find them yourself — do not assume what they are, and do not
be told. When a thing has changed in one shot and not in another, you
know which shot came first.

Produce three things:

 a) THE ORDER. A single list: your first shot to your last, by segment
    number. If two segments are interchangeable, say so and put them as a
    pair rather than inventing a reason.

 b) THE EVIDENCE. One line per placement: the single physical fact that
    put this segment where you put it, with its timecode. "It feels like
    a beginning" is not evidence. "There are more wraps here than in
    Segment 6" is evidence.

 c) THE CLOCKS. List the physical states you used as one-way markers, and
    for each, name the segments on each side of it. Say how confident you
    are in each one.

Then answer, in one line each:
    - Which single placement are you LEAST sure of, and why?
    - Are there any segments you could not place at all? Say which, and
      say what is missing from them that would have let you place them.
    - ⭐ ARE THERE TWO SEGMENTS THAT LOOK ALMOST IDENTICAL? If so,
      describe both and list every difference you can find between them,
      however small. Then say whether you think they are two different
      shots or the same shot used twice, and why.


⛔ STEP 5 — TELL THE STORY

In your own order from STEP 4, write what happens, in at most 200 words,
as plain events. No interpretation of meaning, no theme, no praise. What
happens, to whom, in what order.

Then answer these directly:

 1. ⭐ DOES THE CAST CHANGE DURING THE REEL? Count the people in every
    segment. If someone stops appearing, say at what point, and say
    whether the picture explains why. Answer plainly.
 2. ⭐ DOES ANYTHING SEPARATE, COME LOOSE, OR GET RELEASED anywhere in
    this reel? For each instance: segment, timecode, what separated from
    what, and — this is the important part — DID IT LOOK ACCIDENTAL OR
    DELIBERATE? Say what in the picture made you decide. If you cannot
    tell, say you cannot tell; that is a real answer.
 3. Does anything RUN OUT, EMPTY, DROP BY STEPS or STOP WORKING? Name
    every instance with segment and timecode and say how you could tell.
 4. Do any two people ever touch or exchange anything? Name every moment
    of contact or gesture between them, with segment and timecode.
 5. Does the sequence have a beginning, a turn and an end as material, or
    is it a set of shots that do not resolve? Answer plainly.
 6. ⭐ WHAT WOULD A FIRST-TIME VIEWER NOT UNDERSTAND? List every point of
    confusion, with segment and timecode. Be exhaustive and be blunt.
    This is the most useful list in the report — do not shorten it out
    of politeness, and do not fill it with things you personally
    understood on a second look.
 7. ⭐ WHICH MOMENT IN THIS REEL LOOKS IMPORTANT BUT IS HARD TO SEE?
    Something small, brief, at the edge of frame, or out of focus, that
    you suspect matters. Name it with a segment and a timecode and say
    what makes it hard to see. If nothing qualifies, say so.
 8. Which segment carries the MOST information about the story? Which one
    carries the LEAST — that is, which one could be removed with the
    story still standing?


⛔ STEP 6 — WHAT LOOKS WRONG TO THE EYE

Without any reference document, list anything that reads as a mistake:
things that contradict each other between segments, things that behave
oddly, things that look artificial. For each: segment, timecode, what you
see, and what it contradicts.

Pay particular attention to anything that appears DIFFERENT in two
segments while apparently being the same object or the same person.
List every such pair you find.

⛔ Do NOT list the order as a problem. The order is scrambled on purpose
and you have already rebuilt it.


OUTPUT FORMAT — exactly this, in this order

MATERIAL
SEGMENT DESCRIPTIONS      (one paragraph per segment, file order)
PASSPORTS AS SEEN         (the eight items from STEP 3)
REBUILT ORDER             (order, evidence, clocks, least-sure, unplaced,
                           near-identical pair)
THE STORY                 (200 words, then the eight questions)
WHAT LOOKS WRONG          (contradictions, with pairs)
WHAT WORKED               (maximum five lines, specific, with timecodes)


RULES

- Never state a duration, a count, a distance or a lens you did not
  measure or cannot see.
- "Probably", "seems to", "appears intended to" mean you are guessing.
  Either observe it or drop it.
- If something is not visible, write "not visible". That is different
  from "absent" and different from a guess.
- Do not invent a script, a plan or a shot you did not see.
- Do not report missing audio, missing dialogue, missing music, boundary
  cuts, or the scrambled order.
```

---
---

# 🅱️ PROMPT B — KATALOG GEÇİŞİ · YENİ SOHBET · buradan aşağısı kopyalanır

```
ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing ONE reel: the fourth phase of a 120-scene science
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

⭐ AND THREE THINGS SPECIFIC TO THIS PHASE — read all three before you
start, because each one will look like an error if you do not know it.

  ① THE CAST CHANGES. There are two people in this story and ONE OF THEM
    LEAVES DURING THIS PHASE. Four entries have two figures; eight have
    one. A shot with only one person in it is NOT a missing-character
    error. Each entry declares its own count; judge it against that.

  ② TWO ENTRIES ARE ALMOST THE SAME SHOT ON PURPOSE. Entries C and E are
    the same macro framing of the same boot, deliberately repeated so a
    counter can be read twice. They are supposed to look nearly
    identical. What separates them is the count and whether it changes.
    Read both entries carefully before you judge either.

  ③ ONE ENTRY IS INDOORS. Entry L is inside an airlock: no vacuum, no
    sun, no Earth, no stars, and the woman has no helmet on. Everything
    else is outside. Do not report L's different environment or its
    different light as an error, and do not report the other eleven for
    not matching it.


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

The catalogue expects TWELVE shots. Ten, eleven, twelve or thirteen
segments are all plausible material — report the number you actually
count, do not force it to twelve.

If the measured duration is under 55 seconds, OR you count fewer than 7
segments, your ENTIRE output is this one line and nothing else:

    MATERIAL GATE FAILED - measured __ s, __ segments. Not the phase reel.

Then stop.

⭐ STATE THE MEASURED SHOT LENGTH EXPLICITLY. Also state whether the
individual segments are all the same length within 0.3 s, or differ.


⛔ STEP 0 — THE COMPILATION RULE, AND THE ONE MOVING SHOT

This reel is a COMPILATION. A cut at every segment boundary is REQUIRED
BY THE ARCHITECTURE. NEVER report a cut, an angle change, a lens change,
a lighting change or a location change AT a segment boundary as an
error, a hidden cut or a continuity break. Adjacent segments are
supposed to look nothing alike.

DO report, at maximum severity, any cut, camera reset, angle jump,
sudden reframe or teleport that happens INSIDE a segment. Every segment
must be one unbroken take.

⭐ CAMERA MOVEMENT:
    EXACTLY ONE catalogue entry has camera movement: entry H, a very slow
    PULL-BACK of about half a metre across the shot, under 10% of frame.
    That movement is CORRECT.
    EVERY OTHER ENTRY IS LOCKED OFF WITH ZERO MOVEMENT. Any pan, tilt,
    track, zoom, drift, handheld float or shake in any entry other than H
    is a finding at high severity. If H has NO movement at all, that is
    also a finding, a smaller one — report it.

⛔ THE SAME TRAP AS BEFORE: in several entries THE BACKGROUND SLIDES while
   the foreground stays fixed. That is NOT camera movement — it is the
   station turning, and it is the physical cause of everything that
   happens in this phase. If the FOREGROUND drifts in frame, that IS a
   finding.


⛔ STEP 0.5 — HOW TO REFER TO THINGS

Number the segments by their POSITION IN THE FILE you were given:
Segment 1 is the first one you see, and so on. Give each one its
measured start and end timecode.

Separately, each segment gets a CATALOGUE LETTER (A-L) once you have
identified it in STEP 2.

EVERY finding carries BOTH: the segment number with its timecode, AND
the catalogue letter. A finding without both is deleted before you
output it. Never use a scene number like "S43" — this reel has no scene
numbers you can trust.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before comparing anything, write down what you ACTUALLY SEE, in your own
words:
    - the woman (face, hair, suit stripe colour, back, head covering)
    - the man (build, suit stripe colour, WHAT IS ON HIS BACK - describe
      its shape in detail, see OPEN ITEM 1)
    - the station hull and the station seen whole
    - the cord and the tether: how many wraps, tight or loose, in which
      entries
    - the counters: how many segments are lit, in which entries
    - the light, and where Earth is

Only then compare against the catalogue. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


⛔ STEP 2 — IDENTIFY EVERY SEGMENT (this is the core of this audit)

Go through the segments one at a time. For each one, decide which
catalogue entry it is, using its CONTENT SIGNATURE - the combination of
scale, how many people are in it, what is being done, what objects are
present and what the counters read.

For each segment produce one row:
    Segment N | start-end | catalogue letter | confidence high/low |
    the one detail that settled it

Then produce three lists, and none of them may be skipped:
    MATCHED     - catalogue entries found in the reel
    MISSING     - catalogue entries NOT found anywhere in the reel
    UNMATCHED   - segments that fit no catalogue entry, described in full

⭐ C AND E WILL BOTH LOOK LIKE THE SAME SHOT. Do not put them both under
one letter without checking the counter. If two segments claim the same
letter and you cannot separate them, say so explicitly and describe
exactly what you compared.

If you cannot confidently identify a segment, do NOT guess. Mark it
UNMATCHED and describe what is in it.


================================================================
LOCKED SPEC - CONDITIONS THAT HOLD IN EVERY SHOT
================================================================

FORMAT
    Every shot: 16:9 horizontal, one unbroken take, ZERO internal cuts.
    Zero camera movement everywhere except entry H (see STEP 0).

AUDIO
    Every shot was generated SILENT. Breathing, the radio band, the suit
    AI and all atmosphere are added in post. Never grade lip-sync
    against the soundtrack, and never report "no audio", "silent" or
    "mouth moves but no sound" as a defect.

ENVIRONMENT - ELEVEN OUTSIDE, ONE INSIDE
    Eleven entries are outside in hard vacuum, close to a damaged
    orbital station. Entry L is inside its airlock. There is NO planet
    surface, NO other interior and NO other spacecraft anywhere.
    THE STATION: white-grey quilted thermal blanket over cylindrical
    modules, with ORANGE handrail runs; a circular white airlock hatch
    with a long external lever and a recessed ORANGE grab bar; a
    ragged dark puncture in one module.
    ⭐ THE HULL IS THE GROUND IN THIS PHASE. In every outside entry the
    hull lies along the SCREEN-LEFT side or the BOTTOM of frame, and
    open space is to the SCREEN-RIGHT and above. A shot with the hull on
    the screen-right and open space on the screen-left is a finding.
    EARTH: this phase sits at the day/night line. Earth's limb reads as
    a DARK edge with a THIN WARM ORANGE RIM along it, low in frame.
    Black space with hard pinpoint stars. Vacuum has no air: no haze, no
    glow around objects, no light shafts, no visible beams.

⭐ LIGHT - LOW GOLDEN SUN, ONE SIDE, ELEVEN TIMES
    Outside: ONE source, a LOW GOLDEN sun from the UPPER SCREEN-RIGHT in
    all eleven exterior entries, with no exception, plus a DIM WARM
    bounce from Earth. The low sun RAKES the quilted hull and throws
    LONG HARD SHADOWS from every handrail. Shadows stay ABSOLUTE BLACK
    with razor edges - a low sun lengthens shadows, it does not fill
    them. A hard white overhead key anywhere outside is a finding.
    Inside (entry L only): NO sun. Cold white panel light from a ceiling
    ring as the key, flat and even, plus ONE warm amber patch from an
    emergency lamp on the screen-left wall. No daylight, no Earth, no
    stars.
    NOTHING BURNS anywhere: no flame, no fire, no ember, no spark, no
    smoke, no dust cloud, no vapour cloud, no explosion. Metal is cold.

⭐ NOTHING FIRES IN THIS PHASE - READ THIS TWICE
    The man's manoeuvring unit ran out of propellant in the previous
    phase. Its indicator strip is DARK in every entry. There is NO
    thruster plume anywhere in this reel - not one, not brief, not
    faint. Any plume, jet, puff, gas cone or exhaust from any entry is a
    finding at MAXIMUM severity.
    ⭐ THIS IS NOT A DETAIL. Everything in this phase moves because it
    was released or because the structure is turning. If something moves
    because it fired, the phase means the opposite of what it means.

⭐ THE STATION IS TURNING - AND IT IS THE CAUSE OF EVERYTHING
    In entries D, G, H and I the star field and Earth's rim SLIDE
    STEADILY TO THE SCREEN-LEFT behind the figures at ONE CONSTANT RATE,
    from the first frame to the last. The figures and the hull stay
    fixed in frame. In entry K the edge of the module swings across a
    wedge of black for the same reason.
      - If the sky does NOT slide in D, G, H or I, that is a finding at
        maximum severity.
      - If the slide speeds up, slows down or stops, that is a finding.
      - If the foreground drifts instead, that is a finding.
      - The rate must look the SAME in all four entries.

⭐ VACUUM MOTION
    Bodies travel in DEAD STRAIGHT LINES at CONSTANT SPEED and never
    slow down, hover, settle or drift off-line. A body that has been
    released keeps going at the same speed to the last frame. Nothing
    decelerates on its own.
    A pull travels through a body in order: shoulders lead, hips follow
    a beat later, legs swing last and settle. A body that moves all at
    once, or that jerks and stops dead, is a finding. Bodies are never
    rigid: a figure held stiff like a mannequin is a finding.
    A TAUT line is DEAD STRAIGHT. A taut line that sags, curves, arcs or
    droops is a finding at maximum severity. A SLACK line makes slow
    wide curves and holds them; it never whips, never hangs, never
    falls.

⭐ THE TWO COUNTERS - AND WHERE EACH ONE CHANGES
    Neither counter ever has a number printed beside it.

    THE CORD LOOPS on her right boot - the visible counter of this phase:
        THREE loops in entries A (after the snag), B, C, D, F, G, H
        ⭐ In entry E it starts at THREE and DROPS TO TWO on screen: the
          outermost loop slides off the toe and snaps away. That change
          must be VISIBLE inside the shot.
        TWO loops in entry I.
        ⭐ In entry J she takes BOTH remaining loops off HERSELF, one
          then the other, and the bundle falls slack. After that, none.
        A loop count that goes UP anywhere is a finding at maximum
        severity.

    HER WRIST RING, six small amber segments on her LEFT glove cuff:
        THREE lit wherever it is legible in A through I.
        ⭐ In entry J it drops to TWO lit on screen, during the shot.
        TWO lit in entry K, where it is meant to read clearly.
        A ring reading four or more lit anywhere is a finding.

    HIS ARM STRIP, four segments on his back unit's control arm:
        DARK in every entry. All four segments out. Any lit segment is a
        finding at high severity - it is the reason he cannot save
        himself.

TEXT - ZERO CHARACTERS, NO EXCEPTIONS
    No letters, no digits, no numerals, no glyphs, no icons, no labels,
    no insignia, no mission patch, no flag, no HUD readout, no gauge
    marking, no subtitle, no caption, no title card, no end card, no
    credits, no watermark. Every indicator in this film is an abstract
    segmented light with NO number beside it. Any readable character
    anywhere is a finding at maximum severity.
    ⭐ Entry L is indoors with wall panels and a lamp. Panels there carry
    NO text and NO numbers either.

SPEECH LOCK - ZERO READABLE MOUTHS
    Every human voice comes over a helmet radio, and every speaker is
    turned away, too far away, or out of frame. There is NO shot in this
    phase in which a mouth may be read forming words. Any visible lip
    movement anywhere in the reel is a finding, and its severity is high.
    ⭐ Note entry D: his face is close and fully readable there, and he
    does NOT speak in it. A mouth forming words in D is a finding at
    maximum severity.
    ⭐ Entry L: she has no helmet and does not speak either. Silent.


================================================================
IDENTITY PASSPORT A - THE WOMAN (flight engineer)
================================================================
    38 years old. 1.70 m, slim. Oval face, soft defined jawline, light
    wheat-toned skin with visible pores, thin straight nose, dark hazel
    eyes. A short vertical pale scar on her LEFT temple near the
    hairline. Dark chestnut jaw-length hair.

    SUIT: warm off-white with ORANGE reinforcement stripes on shoulders,
    knees and glove cuffs. A soft chest panel with three small coloured
    lights and NO numerals.

    ⭐ HER BACK IS FLAT. One continuous smooth panel from collar to hip,
      carrying nothing: off-white shell fabric, one vertical spine seam,
      a low webbing waist belt. NO pack, NO tank, NO backpack, NO hose,
      NO cable, NO frame, NO thruster unit of any kind. Anything mounted
      on her back is a finding at maximum severity. Entry K turns her
      back fully to camera - that entry is the decisive test of this
      lock and you must state its result explicitly.

    WRISTS: the six-segment amber ring in her LEFT glove cuff. A steel
    mechanical watch on a black strap over her RIGHT glove cuff, its
    hands STOPPED and its crystal scratched. Left and right never swap.

⭐ HER HELMET - AND THE ONE PLACE IT COMES OFF
    In ALL ELEVEN EXTERIOR ENTRIES she is wearing a rigid white helmet.
    ⛔ AN EXTERIOR ENTRY IN WHICH HER HEAD IS BARE, OR HER HAIR IS LOOSE
      AND MOVING, IS A FINDING AT MAXIMUM SEVERITY. Hair cannot move
      outside a helmet in vacuum and a bare head there is fatal to the
      film.
    ⭐ ONLY IN ENTRY L, INDOORS, is her head bare - and there the helmet
      is already off and turning slowly a metre away from her. The act
      of removing it is deliberately NOT in frame. A shot of her taking
      the helmet off is a finding.

    THE SHAPE of the transparent part is NOT scored in this audit,
    whatever it is. Do not report it.
    WHAT IS SCORED, AND SCORED HARD:
      - the helmet must READ AS A HELMET: you can see where the rigid
        shell ends and the clear part begins, in every close shot
      - the glass optically CLEAR - zero tint, zero colour, zero
        darkening, NO mirror coating, NO gold, NO chrome
      - her face FULLY READABLE through it in every close and medium shot
    A face you cannot read through the glass is a finding at maximum
    severity. A close shot in which you cannot tell whether she is
    wearing a helmet at all is a finding at maximum severity.


================================================================
IDENTITY PASSPORT B - THE MAN (commander)
================================================================
    52 years old. 1.85 m, broad and heavy. Wide bony face, thick dark
    brows, deep lines at the eye corners, olive-brown skin with visible
    pores, short greying stubble, short dense salt-and-pepper hair, dark
    brown eyes, a small old notch in his RIGHT earlobe.
    SUIT: the same warm off-white, but the stripes are NAVY BLUE, never
    orange. Orange on him, or navy on her, is a finding. The same helmet
    rules as hers apply to his, and his head is covered in every entry
    he appears in.
    ⭐ He appears in FOUR entries only: A, D, G, H — and as a distant
      pale mark in I.
    ⚠️ WHAT IS ON HIS BACK: see OPEN ITEM 1. Describe it. Do not score
      its design - but DO check that it is the same object every time.


================================================================
⭐ INTENDED - DO NOT REPORT THESE AS ERRORS
================================================================
 1. Cuts at segment boundaries. Required by the architecture.
 2. Adjacent segments looking nothing alike. Required.
 3. The pull-back in H. The only intended camera move.
 4. The background sliding behind fixed figures in D, G, H and I, and
    the module edge swinging in K. That is the station turning.
 5. C and E looking nearly identical. Deliberate repetition.
 6. Eight entries containing only one person. One of the two leaves
    during this phase; that is the story, not a missing character.
 7. Entry L being indoors, lit differently, with no vacuum and no stars.
 8. Her head being bare in entry L, and the helmet floating empty beside
    her there.
 9. The station's puncture and its torn parts. Damage from earlier
    phases, permanent.
10. His arm strip being completely dark. He has no propellant left.
11. Nothing ever firing. There is no fuel in this phase.
12. The stopped watch on her right cuff. It has never worked.
13. The SHAPE of either visor, whatever it is. Not scored here.
14. A silent reel with no dialogue and no music.
15. Held stillness in a close-up. That is the performance.
16. Entry G ending with him still travelling and no one catching him.
    That is the end of the shot, not an unfinished render.


================================================================
⚠️ OPEN ITEM 1 - THE COMMANDER'S BACK: DESCRIBE IT, DO NOT SCORE IT
================================================================
The production documents disagree about what the man wears on his back,
so you are given NO description of it.

Look at his back and write a paragraph:
    - Is it one solid closed object, or an open structure you can see
      through?
    - Its overall shape and proportions - taller than wide, wider than
      tall, or square?
    - How far does it stand out past his shoulders on each side, and how
      far off his back?
    - Are its edges straight or curved? Corners sharp or round?
    - Is its surface divided into panels, and by what?
    - Does anything stick out of it - arms, pods, nozzles, tubes,
      struts? Are they flush or standing off it? Count them.
    - Where on it is the four-segment indicator strip?

⭐ He appears in four entries. Is it the SAME OBJECT in all four? Compare
nozzle count, proportions and control arms and name every difference.

Write this as OBSERVATION. Give the DESIGN no score and no verdict.
Whether it is the same object every time IS scored, under continuity.


================================================================
⚠️ OPEN ITEM 2 - THE STATION HAS NO REFERENCE: DESCRIBE IT PRECISELY
================================================================
The station was never drawn as a reference sheet. Entry I shows it whole
from a distance and is the reference view; whatever it produced becomes
the master for everything that follows.

Write a precise paragraph:
    - How many separate cylindrical modules, and are they the same size?
    - How are they joined - what does the spine look like?
    - What is attached above and below, and do the two sides match?
    - Where is the puncture, counting modules from which end?
    - Where is the airlock hatch relative to the puncture?
    - ⭐ Do the close entries agree with entry I? Compare the quilting,
      the handrail spacing and the hatch. Two stations that differ is a
      finding at high severity, because they are the same object.

Describe it. Do not score the design.


================================================================
THE SHOT CATALOGUE - twelve entries, no order implied
================================================================
Letters are labels only. A is not first and L is not last. Identify by
signature, not by letter.

Every entry except L: 16:9, one unbroken take, low golden sun from the
upper screen-right, hull on the screen-left or bottom, no readable text,
no readable mouth, no thruster plume.


A - THE STRIKE                        2 figures · loops 0 then 3
    Medium shot, 35mm, from 4 m out from the hull and level with it, the
    lens SKIMMING ALONG the quilted surface, camera pitched down 25
    degrees, deep focus.
    Two astronauts have just struck the white quilted underside of a
    module and are folding at the knees. A tangled bundle of white-grey
    cord is snagged around a handrail post between them. An
    orange-and-white tether lies slack across the quilting.
    HAPPENS: her boots take the surface and her body folds at the knees,
    the shock running up through her and back out; she rebounds and
    travels sideways along the hull to the SCREEN-LEFT, arms out, BOTH
    GLOVES CLOSING ON NOTHING. Half a body length away his boots strike
    and THE RIGID UNIT ON HIS BACK DRIVES HIM STRAIGHT BACK OFF the
    surface to the SCREEN-RIGHT — ⛔ NOTHING FIRES; it is the rebound,
    not thrust. Then her RIGHT BOOT swings into the snagged bundle and
    DRIVES THROUGH TWO OF ITS LOOPS; the loops close around the boot and
    she STOPS HARD, swinging once around the snag point. He is a body
    length clear and still moving out, arms open, nothing under his
    gloves. The slack tether lifts off the quilting and begins to
    straighten. She hangs from the snagged boot; he keeps going.
    SIGNATURE: the only shot where two people hit a surface and bounce.
    The only shot where a boot goes INTO the cord.
    ⛔ Exactly two figures. Nobody grabs anything successfully.

B - HER FACE AT THE HULL              1 figure · loops out of frame
    Close-up, 85mm, from 0.7 m from her visor, THREE-QUARTER FRONT, at
    eye level. Shallow focus: her face sharp, the quilting soft.
    Her face inside a clear helmet, PRESSED CLOSE TO THE WHITE QUILTED
    HULL which fills the frame behind her, a narrow wedge of black space
    along the screen-right edge. Eyes wide open and fixed to the
    SCREEN-RIGHT.
    HAPPENS: a HARD JOLT runs through her as a load comes onto the line
    behind her — her whole head snaps a little to the screen-right and
    HER HELMET KNOCKS ONCE AGAINST THE QUILTING. Her expression does not
    change for a full second. Her eyes track down and to the
    screen-right, following a line she can see and the camera cannot;
    her lids narrow. Her jaw closes and sets; one long slow breath
    instead of the short ones. She does not speak.
    SIGNATURE: the only close-up of her face against the hull. The only
    shot where a helmet touches the station.
    ⛔ Mouth closed throughout.

C - THREE LOOPS, HOLDING              1 boot only · loops 3, STAYS 3
    Extreme close-up, 100mm macro, from 0.5 m ABOVE her boot,
    HIGH-ANGLE pitched down 35 degrees. Shallow focus: boot, loops and
    cord sharp; the quilting soft. NO FACE, NO PERSON above the knee.
    An astronaut's white boot and lower leg against the quilted hull,
    with THREE LOOPS of white-grey braided cord coiled tight around the
    boot. The cord leaves frame to the SCREEN-RIGHT, straight and
    stone-still under load.
    ⭐ THE COUNT IS THREE AT THE FIRST FRAME AND THREE AT THE LAST. It
      does not change in this entry. That is what separates C from E.
    HAPPENS: the load rises and each loop draws DEEPER into the ribbing
    of the boot, the braid FLATTENING where it bites. The outermost loop
    creeps a short way toward the toe, THEN STOPS AND HOLDS. The boot
    turns a few degrees as the leg above it shifts and ALL THREE LOOPS
    TRAVEL WITH IT. A short frayed fibre end lifts off the braid and
    drifts straight out, then keeps that line.
    SIGNATURE: one of two identical macro framings of the boot; THE ONE
    WHERE NOTHING COMES OFF.
    ⛔ No face, no second person, no station beyond the quilting.

D - HIS FACE ON THE LINE              1 figure · sky SLIDES
    Close-up, 85mm, from 0.8 m from his visor, THREE-QUARTER FRONT, at
    eye level. Shallow focus: his face sharp, the star field and hull
    soft.
    The big man's face inside a clear helmet, HANGING AT THE END OF A
    TAUT TETHER against black space, his eyes lowered along the tether
    line to the screen-left. Earth's dark rim low in the screen-right.
    Arm strip: DARK.
    ⭐ BEHIND HIM THE WHOLE STAR FIELD SLIDES STEADILY TO THE SCREEN-LEFT
      at ONE CONSTANT RATE, and Earth's rim slides with it at the SAME
      rate, first frame to last. His face stays fixed in frame.
    HAPPENS: his breathing is slow and long; his eyes travel UP the
    tether line and hold on something off-frame to the screen-left for a
    full second; then they DROP TO HIS OWN BELT at the bottom of frame
    and stay there, and the lines at his eye corners deepen once; then
    he raises his eyes again, level and steady. He does not react and he
    does not speak.
    SIGNATURE: the only close-up of the man's face. The only close-up
    with a sliding star field behind it.
    ⛔ HIS MOUTH STAYS CLOSED. His face is fully readable here and he
      does not speak. Lip movement is a finding at maximum severity.

E - THREE LOOPS BECOME TWO            1 boot only · loops 3 → 2 ON SCREEN
    Extreme close-up, 100mm macro, from 0.5 m ABOVE her boot,
    HIGH-ANGLE pitched down 35 degrees — DELIBERATELY THE IDENTICAL
    FRAMING TO ENTRY C, same boot, same hull, same light.
    ⭐ THIS IS THE ONE WHERE THE COUNT DROPS. Three loops at the first
      frame; about three seconds in THE OUTERMOST LOOP SLIDES OFF THE
      TOE, OPENS, AND SNAPS AWAY to the screen-right along the line of
      the cord in ONE STRAIGHT TRAVEL. TWO loops for the rest of the
      shot. The change must be visible INSIDE the shot — not a cut, not
      a state.
    HAPPENS: the load JERKS ONCE and every loop shifts a fraction along
    the boot, the braid squeaking flat where it bites; then the outer
    loop goes; the two remaining loops creep together toward the toe,
    STOP, AND HOLD, the braid still flattened where it bites.
    SIGNATURE: one of two identical macro framings of the boot; THE ONE
    WHERE A LOOP COMES OFF.
    ⛔ If this entry shows three loops at the last frame, or two at the
      first, it is a finding at high severity.
    ⛔ No face, no second person.

F - HER FACE, SQUARE ON               1 figure · glove enters frame
    Close-up, 85mm, from 0.7 m in front of her visor, STRAIGHT ON,
    SQUARE to her, at eye level. Shallow focus: her face sharp,
    everything behind soft.
    Her face inside a clear helmet, square to camera, eyes open wide and
    turned HARD TO THE SCREEN-RIGHT, mouth closed in a flat line. At the
    BOTTOM EDGE of frame the fingers of her ORANGE-cuffed glove rise
    into shot, spread open.
    HAPPENS: her eyes do not move for two seconds. Then SHE SHAKES HER
    HEAD TWICE, small and hard, once and once again — and the white
    shell and its bright rim MOVE WITH HER HEAD AS ONE RIGID PIECE. Her
    lids tighten and stay tight; she holds one breath instead of taking
    the next. Her open glove RISES FURTHER into the bottom of frame and
    REACHES OUT to the screen-right anyway, fingers spread, passing out
    of focus as it comes forward.
    SIGNATURE: the only close-up shot square-on to her face. The only
    shot where she shakes her head. The only shot where a glove enters
    from the bottom edge.
    ⛔ Mouth closed throughout, including during the head shake.
    ⛔ The two head shakes are SMALL and HARD, not a slow sad sway.

G - THE RELEASE ⭐                     2 figures · sky SLIDES
    Medium shot, 35mm, from 3 m from the man and SQUARE TO THE TETHER
    LINE, FULL PROFILE, camera level with his shoulders, deep focus,
    true scale between the two figures.
    In the near foreground at the SCREEN-RIGHT, in full profile facing
    the screen-left: the big man, hanging at the end of a TAUT tether
    that runs from his belt straight across frame. Far behind him at the
    SCREEN-LEFT, SMALL against the hull: the woman, folded, one boot in
    the cord, ONE ARM HELD OUT toward him. Arm strip: DARK.
    ⭐ Behind both figures the star field SLIDES STEADILY to the
      screen-left at ONE CONSTANT RATE.
    ⭐ HAPPENS - THIS IS THE MOST IMPORTANT SHOT IN THE REEL:
      his RIGHT GLOVE CLOSES ON THE STEEL SNAP HOOK AT HIS OWN BELT
      RING and his THUMB SETTLES ON ITS SPRUNG GATE; then HIS THUMB
      ROLLS THE GATE OPEN and THE HOOK LEAVES THE RING. The freed tether
      end WHIPS STRAIGHT and travels away to the screen-left in one
      line. He begins to move to the SCREEN-RIGHT, away from the hull,
      AT ONE STEADY SPEED, WITH NOTHING PUSHING HIM. At the screen-left
      SHE DOES NOT MOVE; her out-held arm stays exactly where it was. He
      ends clear of the tether and still travelling, ARMS DOWN AT HIS
      SIDES, NOT REACHING.
    ⛔ HE UNDOES IT HIMSELF, WITH HIS OWN HAND, AND THE HAND MUST BE
      VISIBLE DOING IT. If the line snaps, frays, tears, is cut, or
      comes loose on its own — that is a finding at MAXIMUM severity,
      because it makes a choice into an accident.
    ⛔ NO PLUME. Nothing fires. He is not pushed by anything.
    ⛔ He does not tumble and does not reach back.
    ⛔ His mouth is edge-on at 3 m and must not be readable.
    SIGNATURE: the only full-profile two-shot. The only shot in which a
    hand opens a hook.

H - TWO ENDS OF ONE CORD              2 figures · sky SLIDES · ⭐ MOVING
    Wide shot, 24mm, from 6 m out from the hull, at eye level with the
    hull plane, LOOKING ALONG THE MODULE'S LENGTH, deep focus, true
    scale. ⭐ SLOW PULL-BACK of about half a metre across the shot.
    The module runs away down the frame with its handrails converging.
    In the LOWER SCREEN-LEFT, small, the woman held at the hull, a loose
    cord curving away from her boot into black space. Beyond the hull's
    edge at the SCREEN-RIGHT, the man drifts clear.
    ⭐ Behind both, the star field slides steadily to the screen-left at
      one constant rate.
    HAPPENS: he travels steadily to the screen-right, away from the
    hull, AT ONE CONSTANT SPEED; SHE DOES NOT MOVE. The FREE END OF THE
    TETHER TURNS SLOWLY END OVER END as it travels, the open hook
    CATCHING THE SUN ONCE. ⛔ HE DOES NOT TUMBLE: he holds one attitude,
    facing back to the screen-left, arms down at his sides, and does not
    reach for anything. The gap between them grows by a body length. The
    long curve of the tether PULLS OUT STRAIGHT as it travels — one end
    still looped at her boot, the other end EMPTY. He is smaller in
    frame at the last frame and still going.
    SIGNATURE: the only shot looking down the length of the module. The
    only shot showing both ends of one cord. The only moving shot.
    ⛔ No plume. He never slows.

I - THE SCALE                         2 tiny figures · loops 2
    Extreme wide shot, 24mm, from 40 m out and above the station,
    HIGH-ANGLE pitched down 25 degrees, deep focus, true scale.
    The whole damaged station lies ACROSS THE WHOLE FRAME. ONE TINY PALE
    FIGURE on its flank; a SECOND, SMALLER PALE FIGURE far out in black
    space to the SCREEN-RIGHT. Both are marks, not bodies — no face, no
    limbs readable.
    ⭐ Behind the structure the star field and Earth's rim slide steadily
      to the screen-left at one constant rate.
    HAPPENS: the structure lies STILL across the frame. The figure on the
    hull DOES NOT MOVE. The pale point out to the screen-right travels
    steadily away IN A STRAIGHT LINE and NOTHING CHANGES SPEED; the gap
    opens at one steady rate and the point is SMALLER at the end than at
    the start.
    SIGNATURE: the only shot of the whole station from a distance. The
    only shot where both people are smaller than a tenth of frame
    height. This is the reference view of the station.
    ⛔ Exactly two figures and no more. No plume from the distant one.

J - SHE FREES HERSELF ⭐               1 figure · loops 2 → 0 · ring 3 → 2
    Wide shot, 24mm, from 5 m out from the hull, at eye level with the
    hull plane, SQUARE to it, deep focus, true scale.
    The woman folded against the quilted surface with ONE BOOT CAUGHT in
    the cord bundle at a handrail post, one glove reaching PAST HER OWN
    BOOT toward an ORANGE handrail.
    ⭐ TWO COUNTERS CHANGE IN THIS ONE SHOT, both on screen:
      the RING on her left cuff goes from THREE lit to TWO lit, and the
      CORD LOOPS on her boot go from TWO to NONE.
    HAPPENS: she hangs folded from the snagged boot, both gloves open
    and empty, drifting a few degrees around the snag point. She REACHES
    PAST HER OWN BOOT and closes her left glove HARD on an ORANGE
    handrail — HER DRIFT STOPS AT ONCE. One amber segment on her left
    wrist goes dark. Then, WITH THE RAIL HELD, her right glove works the
    OUTER LOOP OFF THE HEEL of the boot and it opens and drifts free in
    a straight line; then THE SECOND LOOP SLIDES OFF and the bundle
    falls slack against the hull, STILL COILED AROUND ITS POST. She does
    not drift — the rail holds her. She pulls herself FLAT along the
    hull and takes the NEXT rail with her right glove, boots trailing.
    SIGNATURE: the only shot where she frees her own boot. The only shot
    where two counters change at once.
    ⛔ She does it HERSELF, with her hands, one loop then the other. A
      loop that falls off on its own is a finding.
    ⛔ Nobody helps her. Exactly one figure.

K - THE HATCH ⭐ HER BACK              1 figure · ring 2 · last helmet
    Medium shot, 35mm, from 2.5 m BEHIND her and slightly above,
    HIGH-ANGLE pitched down 20 degrees, deep focus; the hatch and both
    gloves sharp.
    Seen from behind: her back FILLS THE MIDDLE OF FRAME, at a CIRCULAR
    WHITE AIRLOCK HATCH with a raised rim, a LONG EXTERNAL LEVER lying
    across it and a RECESSED ORANGE GRAB BAR beside it. To the
    screen-left, the handrail post with the slack cord bundle still
    coiled around it. A wedge of black space and Earth's dark rim along
    the upper screen-right.
    ⭐ THIS IS THE DECISIVE TEST OF THE FLAT-BACK LOCK. Her back must
      read as one continuous smooth panel from collar to hip carrying
      nothing — off-white shell fabric, one spine seam, a low waist
      belt, the collar ring at the top, and NOTHING mounted on it. State
      explicitly what you see there.
    HAPPENS: she pulls up to the hatch, boots trailing, and stops square
    to it. Her LEFT glove takes the recessed ORANGE grab bar and the
    wrist turns into frame — ⭐ THE RING READS CLEARLY HERE: TWO
    SEGMENTS LIT, FOUR DARK. Then AT THE UPPER SCREEN-RIGHT THE EDGE OF
    THE MODULE SWINGS ACROSS THAT WEDGE OF BLACK as the whole structure
    turns. Her right glove closes on the long lever and TURNS IT HALF A
    TURN; the lever comes to a stop against its rim and the hatch ring
    seats. She holds the grab bar with her HEAD DOWN, not moving.
    ⛔ THE HATCH STAYS CLOSED. It does not open in this shot.
    SIGNATURE: the only shot from behind her. The only shot with the
    airlock hatch and its lever. Her last shot wearing a helmet.

L - INSIDE ⭐ NO HELMET                1 figure · INTERIOR · no vacuum
    Wide shot, 24mm, from 3 m along the airlock, at eye level with her,
    SQUARE to the volume, deep focus; the whole small space and the
    curled figure in frame.
    ⭐ INSIDE a small cylindrical station airlock. NO sun, NO stars, NO
      Earth, NO vacuum. COLD WHITE PANEL LIGHT from a ceiling ring as
      the key, flat and even, plus ONE WARM AMBER PATCH from an
      emergency lamp on the SCREEN-LEFT wall falling across her shoulder
      and chest. Hoses curve past her in long slack arcs.
    ⭐ SHE HAS NO HELMET ON. Her head is bare, her hair loose and
      standing out from her head. Her EMPTY HELMET turns slowly a metre
      away from her, its clear visor passing across frame WITH NOTHING
      INSIDE IT.
    HAPPENS: she floats at the centre of the volume with arms loose and
    head back, TURNING VERY SLOWLY; her chest rises and falls, deep and
    uneven. She DRAWS HER KNEES UP to her chest, folds both arms over
    her shins and pulls in tight — and HER BODY KEEPS TURNING AT THE
    SAME RATE IT ALREADY HAD; curling up does not slow her and does not
    speed her up. Her chin comes down onto her knees and HER EYES CLOSE.
    On her RIGHT wrist the steel watch turns into view, ITS HANDS
    STOPPED. She holds the curl, turning slowly, eyes closed, the empty
    helmet still turning beside her.
    SIGNATURE: the only interior shot. The only shot without a helmet on
    her head. The only shot with no stars and no Earth.
    ⛔ THE ACT OF REMOVING THE HELMET IS NOT IN FRAME. The helmet is
      already off at the first frame.
    ⛔ SHE DOES NOT SPEAK. Exactly one figure; nobody else is in the
      airlock. No text on any panel.
    ⛔ Her curling up must NOT change her rate of turn — that is the
      physics test of this entry.


================================================================
⭐ CROSS-SHOT CHECKS - the part that does NOT depend on order
================================================================
Answer every one, by number, and name the segments in each answer.

 1. IS SHE THE SAME PERSON in every shot she appears in? Bone structure,
    age, eye spacing, skin, hair length, the LEFT temple scar.
 2. IS HE THE SAME PERSON in all four of his entries?
 3. ⭐ IS SHE WEARING A HELMET IN EVERY EXTERIOR SHOT? Name every
    exterior segment and say yes or no for each. Name any exterior shot
    where her head is bare or her hair is loose and moving. This is the
    single most important check in this audit.
 4. THE GLASS: in every close and medium shot, can you tell she is
    wearing a helmet, and can you read the face through it? Name any
    shot where the visor is tinted, mirrored, or where you cannot tell
    whether a helmet is there at all. (Do NOT comment on its shape.)
 5. IS HER BACK FLAT wherever it is visible? Name each shot where her
    back can be seen and say what is on it. Entry K is the decisive one.
 6. ⭐ IS HIS BACK UNIT THE SAME OBJECT in all four of his entries?
    Compare nozzle count, proportions and control arms. (See OPEN ITEM 1.)
 7. ⭐ COUNT THE LOOPS on her boot in every entry where they are
    visible, and give the count at the FIRST frame and at the LAST frame
    of each. Then confirm: does the count drop 3 → 2 on screen in E?
    Does it drop 2 → 0 on screen in J? Does it ever go UP anywhere?
 8. ⭐ C AND E: they are the same framing on purpose. List every
    difference you can find between them. Then say whether E really
    shows the drop, and whether C really holds at three. If you cannot
    tell them apart at all, say so — that is a finding.
 9. THE RING: report the lit count in every entry where it is legible.
    Confirm the 3 → 2 drop on screen in J and the clear reading of TWO
    in K. Does it ever read four or more?
10. HIS ARM STRIP: is it dark in every entry he appears in? Name any
    entry with a lit segment.
11. ⭐ IS THERE ANY THRUSTER PLUME ANYWHERE IN THIS REEL? There must not
    be one. Name every entry with a plume, jet, puff, gas cone or
    exhaust, however brief.
12. ⭐ THE SLIDING SKY: name every entry where the background slides.
    Does it slide in D, G, H and I? Does it look like the SAME rate in
    all four? Does the foreground stay fixed in each?
13. ⭐ THE RELEASE IN G: does a hand visibly open the hook? Or does the
    line break, fray, tear or come loose by itself? Answer plainly and
    quote the timecode.
14. TAUT LINES: is every taut line DEAD STRAIGHT with no sag, curve or
    droop? Name every exception.
15. THE HULL SIDE: is the hull on the screen-left or the bottom, with
    open space to the screen-right, in every exterior entry? Name every
    exception.
16. THE LIGHT: is the sun LOW and GOLDEN from the UPPER SCREEN-RIGHT in
    all eleven exterior entries? Does it RAKE the quilting and throw
    LONG HARD shadows from the handrails? Are the shadows still
    absolute black? Name every exception. (Entry L is indoors and is not
    part of this check.)


================================================================
WHAT TO SCORE - thirteen categories, 1 to 10
================================================================

 1. COVERAGE - how much of the catalogue is present, and how confidently
    could each segment be identified? Score the material, not the order.
 2. IDENTITY CONTINUITY - do both people hold across every shot?
 3. HELMET PRESENCE AND CLARITY - a helmet on her head in every exterior
    entry, readable as a helmet, glass clear, face readable. Score this
    hard. ⛔ Do NOT score visor shape.
 4. COSTUME AND BACK - orange on her, navy on him, HER BACK FLAT with
    nothing mounted on it, ring on the LEFT cuff, watch on the RIGHT.
 5. FIGURE COUNT AND CLONE CONTROL - correct counts per entry: two
    figures in A, G, H, I; one in the other eight. A third figure
    anywhere is maximum severity.
 6. CAMERA DISCIPLINE - locked off everywhere except the pull-back in H.
    Boundary cuts are NOT findings. The sliding background is NOT camera
    movement.
 7. LIGHT AND SHADOW - low golden sun from the upper screen-right
    outside, raking the hull, long hard black shadows; the interior's
    cold panel plus one amber patch; no bloom, no flare, no haze,
    nothing burning.
 8. ⭐ THE RELEASE - entry G: a visible hand opening a hook, no break, no
    plume, one steady speed after it, she does not move.
 9. VACUUM MOTION - straight lines, constant speed, nothing decelerating
    on its own, nobody tumbling, taut lines dead straight, slack lines
    slow and wide, bodies never rigid, and the curl in L not changing
    her rate of turn.
10. ⭐ COUNTERS - loop counts correct per entry, both on-screen drops
    visible (3→2 in E, 2→0 in J), ring correct, arm strip dark.
11. ⭐ STATION ROTATION - sliding sky in D, G, H, I at one shared
    constant rate with the foreground fixed.
12. WORLD CONSISTENCY - the cross-shot checks: same two people, same
    back unit, same station near and far, hull always on the same side,
    same light.
13. TEXT AND DELIVERY HYGIENE - zero readable characters anywhere,
    indoors included; no title card, no end card, no credits, no
    captions, no watermark, no logo, no letterboxing; film grain present
    and consistent; segments the same length.

SEVERITY
    RED     blocker - the shot has to be regenerated
    YELLOW  fixable in the edit (trim, crop, speed, reframe)
    GREEN   note - worth knowing, not worth spending on

Scoring rules:
    - The overall score is the arithmetic mean of the thirteen category
      scores. Compute it from your own table. Do not state an overall
      score your table does not produce.
    - A category with no observed problem is not automatically 10. Say
      what you verified.
    - Never give a category a number if you could not observe it. Write
      UNVERIFIABLE and leave it out of the mean.
    - ⛔ There is NO category for order, pacing, flow or structure.


================================================================
OUTPUT FORMAT - use exactly this structure, in this order
================================================================

MATERIAL
SEGMENT MAP
IDENTIFICATION TABLE
MATCHED / MISSING / UNMATCHED
PASSPORTS AS SEEN
THE COMMANDER'S BACK UNIT - OBSERVATION ONLY
THE STATION - OBSERVATION ONLY
C VERSUS E - a short section listing every difference between the two
    macro boot shots, and your verdict on whether both drops behaved as
    their entries describe
SCORES
TOP 5 CRITICAL
FINDINGS BY SEGMENT
CROSS-SHOT CHECKS      (the sixteen checks, answered by number)
FIXABLE IN THE EDIT vs REQUIRES REGENERATION
FLAGS FOR DOCUMENT CHECK
WHAT WORKED            (maximum five lines, specific, with timecodes)


================================================================
RULES AGAINST INVENTION - violating these makes the report worthless
================================================================

- ⛔ Never comment on the order, sequence, pacing or narrative flow.
- ⛔ Never report the SHAPE of a visor. It is not scored in this audit.
- ⛔ Never report a one-figure entry as a missing character. One of the
  two people leaves during this phase.
- ⛔ Never report C and E resembling each other as an error.
- ⛔ Never report entry L's interior, its light, or her bare head there.
- Never state a runtime, shot length, segment count, lens, distance or
  intent you did not measure or that is not in the spec above.
- If something is not visible, write "not visible". That is different
  from "missing" and different from a guess.
- Do not report a catalogue entry as "missing" until you have checked
  every segment for it. Then report it in the MISSING list.
- Do not invent a bible, a plan, a script or a shot outside the
  catalogue.
- Do not report the absence of audio, dialogue or music as a defect.
- Do not report segment-boundary cuts.
- Do not report anything on the INTENDED list as an error unless the
  specific condition named there is met.
- Every finding carries a segment number, a timecode and a catalogue
  letter, or it is deleted before you output it.
- "Probably", "seems intended to", "may have been", "appears to suggest"
  mean you are guessing. Cut the finding or move it to FLAGS.
- Your recommendations must be achievable in a re-render of a single
  shot of a few seconds. Do not recommend coverage, inserts, reaction
  shots, cutaways or camera moves - this format has none.
```

---
---

# 📌 İKİ RAPOR GELDİKTEN SONRA — GEÇİŞ C (bende)

```
1) İkisi de 02_HAM_RAPORLAR/ altına BİREBİR düşer [kural ④]:
   YERCEKIMI_FAZ04_KOR_HAM.md · YERCEKIMI_FAZ04_KATALOG_HAM.md
2) ③ KİMLİK KAPISI — yalnız KÖR geçişin pasaportundan [D164].
3) ⭐ SIRA SKORU = doğru yerleşen klip / 12.   F2 8/12 · F3 5/12
   ⚠️ BEKLENTİ: F4 filmin en yüksek skorunu vermeli. Sebebi ALTI tek
   yönlü saat: kadro sayısı (2→1) · ilmek (3→2→0) · halka (3→2) ·
   aradaki mesafe · kask (var→yok) · dışarısı→içerisi.
   Çıkmazsa sebebi saat yokluğu DEĞİL, yine bir kusurdur — ara.
4) ⑩ ÖNERME — kör geçişin "anlaşılmayanlar" listesi plana karşı okunur.
5) SAĞLAM / ŞÜPHELİ / ÖLÇÜSÜZ: A+B → SAĞLAM · yalnız B → ŞÜPHELİ
   (yankı) · yalnız A → GERÇEK ama ölçüsüz.
6) Skor ⚠️ ŞARTLI: mod V (SPEC yok [D129]) + master yok [⑪]; T'ye girmez.
```

## 🔬 BU KOŞUNUN ÖZEL OLARAK ÖLÇTÜĞÜ DÖRT ŞEY

```
① ⭐ FEDA KAZA MI, SEÇİM Mİ OKUNUYOR — fazın TEMA'sı budur.
   Kör geçişe doğrudan soruluyor: "bir şey ayrılıyor, kopuyor ya da
   bırakılıyor mu? KAZA gibi mi göründü, KASITLI mı?"
   ⛔ "Halat koptu" cevabı gelirse TEMA ekrana hiç gelmemiştir —
   G yeniden üretilir. F3'te omuz vuruşu görülmemişti; bu onun
   ağırlaştırılmış hâli, çünkü burada görülmeyen şey filmin adı.

② ⭐ C ↔ E ÇİFTİ — depoda ilk kez benzerlik ZORUNLU.
   Kör geçişe "neredeyse aynı iki klip var mı, farkları ne?" diye
   soruluyor; katalog geçişine ayrı bir "C VERSUS E" bölümü yazdırılıyor.
   Sayaç iki karede de sabitse üretim gerçekten kopya vermiştir.

③ ⭐ DIŞARIDA KASK — F3'ün S28'i tam bunu düşürmüştü.
   Çapraz kontrol 3, denetimin en önemli maddesi olarak işaretli:
   on bir dış girdinin her biri için tek tek "kask var mı" cevabı.

④ ⭐ İSTASYON DÖNÜŞÜ — F3'te I'de hiç kurulmadı. Burada DÖRT girdide
   (D · G · H · I) ve fedanın SEBEBİ o. Dördünde de aynı hızda kaymalı.
```

---

## 🔑 KATALOG HARFİ → SAHNE NUMARASI

⛔ Bu tablo İKİ PROMPTUN DA DIŞINDADIR. Rapor geldikten SONRA kullanılır.

| Harf | Sahne | Başlık | Kadro | İlmek | Halka | Not |
|:--:|:--:|---|:--:|:--:|:--:|---|
| A | S37 | TEMAS | 2 | 0→3 | 3 | çarpma + sekme |
| B | S38 | DARBE | 1 | — | — | yüz CU, gövdede |
| C | S39 | ÜÇ KAT | 1 bot | **3 sabit** | — | ⭐ çiftin biri |
| D | S40 | HESAP | 1 (B) | — | — | ⭐ gök kayar · B konuşmaz |
| E | S41 | İKİ KAT | 1 bot | **3→2** | — | ⭐ çiftin öteki |
| F | S42 | HAYIR | 1 | — | — | kare cephe · baş sallama |
| G | S43 | **FEDA ⭐TEMA** | 2 | 3 | 3 | ⭐ kanca ELLE açılır · gök kayar |
| H | S44 | İKİ UÇ 🔥viral#2 | 2 | 3 | — | ⭐ tek hareketli plan · gök kayar |
| I | S45 | ÖLÇEK ⭐1:10 | 2 uzak | 2 | — | ⭐ istasyon referans görüntüsü |
| J | S46 | TUTAMAKLAR | 1 | **2→0** | **3→2** | ⭐ iki sayaç birden |
| K | S47 | KOL | 1 | 0 | 2 | ⭐ düz sırt testi · son kasklı |
| L | S48 | **CENİN** | 1 | — | — | ⭐ iç mekân · KASKSIZ |

**Gerçek sıra: A→B→C→D→E→F→G→H→I→J→K→L** (S37'den S48'e, alfabetik).

---

## ⚠️ BU FAZDA AÇIK KALAN İKİ DOSYA SORUNU

```
① RF (KASKSIZ A) ve RG (İSTASYON İÇ) ÜRETİLMEDİ — ikisi de "F4'ten önce"
   diyordu. L girdisi filmin ilk iç mekânı ve ilk kasksız karesi;
   geri düşecek hiçbir kare yoktu. ⛔ L'nin çıktısı F5-F7'nin iç mekân
   masteri olacak → OPEN ITEM 2'ye ek olarak L'nin tarifi de kilitlenmeli.

② SIRT ÜNİTESİ — F3'te yedi klipte görünüp ÜÇÜNDE kaybolmuştu.
   Burada dört klip. Tarif yine verilmiyor, yine "aynı nesne mi"
   sorusuyla ölçülüyor. RC paneli hâlâ üretilmedi.
```
