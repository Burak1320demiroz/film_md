# 🔍 YERÇEKİMİ — FAZ 2 / DALGA · VİDEO ELEŞTİRİ PROMPTU

## ⭐ İKİ MÜHÜRLÜ GEÇİŞ — önce KÖR hikâye, sonra KATALOG denetimi
### Kaynak kilitler: `FAZ_02_DALGA.md` KİLİT 5-8 · `../README.md` §Negatif Çekirdek · `../REFERANS_PAKETI.md`
### Emsal iskelet: `../FAZ_01_GOREV/FAZ_01_QA_PROMPT.md` (sıradan bağımsız sürüm)

---

# 🚨 NEDEN BU SEFER İKİ GEÇİŞ

Faz 1'de rubrik denetçiye her şeyi anlattı: yüz, vizör, renk, sayaç, hatta
komutanın sırt ünitesinin İKİ ayrı tasarımı da kelimesi kelimesine yazılıydı.
Denetçi geri döndüğünde raporda o tarifler vardı — ve ben bunları **çapa**
saydım. Değildi.

```
⛔ FAZ 1'İN DERSİ
   Denetçiye SÖYLENMİŞ bir tarifin raporda geri gelmesi GÖZLEM DEĞİLDİR.
   Bu bir eşleşme değil, bir YANKIDIR.
   Kimlik kapısı ③ bu yüzden UNATTRIBUTED düştü — rapordaki hiçbir bulgu
   "gördüm" statüsüne yükselemedi.
```

Çözüm rubriği zayıflatmak değil. Çözüm **sırayı ikiye bölmek**:

| | GEÇİŞ A — KÖR | GEÇİŞ B — KATALOG |
|---|---|---|
| Denetçi neyi bilir | Hiçbir şey. Sadece makara. | Her şey: kilitler, pasaportlar, katalog. |
| Ne üretir | **Hikâye + tarif** | **Uygunluk denetimi + skor** |
| Değeri | Yankısız → gerçek ÇAPA | Ölçülebilir → gerçek SKOR |
| Kaçırdığı | Neyin yanlış olduğunu bilemez | Ne gördüğünü bilemez, hatırlar |

**A'nın çıktısı çapadır çünkü denetçiye kimse söylemedi.** Vizörün düz cam
mı kubbe mi olduğunu, kadının sırtının düz mü çantalı mı olduğunu, adamın
sırtındaki şeyin dikdörtgen mi kafes mi olduğunu A geçişinde kendi
gözüyle söylemek zorunda. Faz 1'in kapanamayan kapısı burada kapanır.

---

# ⭐ VE SENİN ASIL SORDUĞUN ŞEY BU GEÇİŞTE CEVAPLANIYOR

> *"ne oldu nasıl ilerledi hikaye bunu anlamak ve diğer fazlara gerekirse
> müdahale etmek için"*

Faz 1'de sıranın karışık olması bir **engeldi** — etrafından dolaştık.
Faz 2'de sıranın karışık olması bir **TESTE dönüşüyor**:

```
⭐ KARIŞIK SIRA = HİKÂYENİN OKUNABİLİRLİK TESTİ

Denetçiye diyoruz ki: "Bu klipler karışık. Sırala. Ama belge yok —
yalnız görüntüye bakarak sırala ve her yerleştirmenin KANITINI yaz."

  Doğru sırayı bulursa  → hikâye replik olmadan, müzik olmadan, sırasız
                           bile OKUNUYOR. Görsel zincir sağlam.
  Bulamazsa             → hangi iki klip arasında takıldığı, görsel
                           zincirin KOPTUĞU yerdir. Adresi verilmiş bir
                           kusur — sonraki fazlarda tam oraya müdahale
                           edilir.
```

Bu, filmin görsel anlatımını ölçen tek gerçek deneydir ve maliyeti sıfırdır.
Faz 3'ten itibaren aynı testi her fazda koşabilirsin — ve fazlar arası
karşılaştırılabilir bir sayı elde edersin: **denetçi kaç klibi doğru
yerleştirdi.**

Filmin kendi içinde altı tane **tek yönlü saat** var (hasar · gök · halat ·
halka · dönüş · kaç kişi). Denetçiye bunların NE olduğunu söylemiyoruz —
"tek yönlü değişen şeyleri bul" diyoruz. Bulursa hikâye kendini anlatıyor
demektir.

---

# 📋 NASIL KOŞULUR — üç adım, sırası değişmez

```
1) YENİ bir sohbet aç. Makarayı yükle. Yalnız PROMPT A'yı yapıştır.
   → Gelen raporu OLDUĞU GİBİ sakla. ⛔ Buna dokunma, düzeltme.

2) İKİNCİ bir YENİ sohbet aç (aynı sohbette DEVAM ETME — A'nın çıktısı
   B'yi kirletir). Makarayı tekrar yükle. Yalnız PROMPT B'yi yapıştır.
   → Gelen raporu OLDUĞU GİBİ sakla.

3) İKİ raporu birlikte bana ver. Karşılaştırmayı ben yaparım (GEÇİŞ C).
```

⛔ **A ve B aynı sohbette koşulursa bu belgenin tüm değeri sıfırlanır.**
Tek amacı A'nın B'yi görmemesi.

⚠️ Makara sessiz üretildi. İki geçişte de "ses yok" bir kusur değildir.

---

# ⚠️ DENETÇİYE BİLEREK SÖYLENMEYENLER — koru

Aşağıdakiler PROMPT A'da **kasten yoktur**. Rapor A'da bunlardan biri
doğru çıkarsa o bir ÇAPADIR; yanlış çıkarsa gerçek bir kusurdur. İkisi de
bilgi. Söylersek ikisi de kaybolur.

```
1. Vizörün geometrisi    (düz dikdörtgen cam + metal çerçeve mi, kubbe mi)
2. Kadının sırtı         (düz mü, sırtında ünite var mı)
3. Adamın sırtındaki şey (dikdörtgen levha mı, açık kafes mi)
4. Şerit renkleri        (kadın TURUNCU, adam LACİVERT)
5. Halka segment sayısı  (kaç yanık, kaç sönük)
6. Mekiğin burun yönü    (EKRAN-SOL)
7. Güneşin yönü          (üst EKRAN-SAĞ, on iki klipte de aynı)
8. Ekranda yazı olup olmadığı
```

---

# ⚠️ İKİ AÇIK MADDE — B geçişinde denetçiye bilerek söyleniyor

```
① KOMUTANIN SIRT ÜNİTESİ — TARİF ET, PUANLAMA
   Belgeler kendi aralarında çelişiyor: REFERANS_PAKETI RC dikdörtgen
   levha diyor, FAZ_02'nin S23/S24 promptları hâlâ "thruster frame"
   (açık kafes) diyor. Hangisinin çıktığını RAPORDAN öğreneceğiz.
   ⛔ Faz 1'de bu maddeye İKİ tasarımı da yazmıştım — denetçi birini
      seçip aynı kelimelerle geri verdi. BU SEFER HİÇBİRİ YAZILMIYOR.

② ENKAZIN GEOMETRİSİ — RD p2 referans paneli HİÇ ÜRETİLMEDİ
   Yani platformun hasarlı halinin bağlayıcı bir aslı yok. Bu fazda
   ne çıkarsa Faz 3-10'un fiilî masteri O OLACAK. Denetçiden enkazı
   ölçülebilir ayrıntıyla tarif etmesini istiyoruz ki kilitleyebilelim.
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

 1. THE WOMAN. Face shape, apparent age, skin, eyes, hair length and
    colour, any mark on her face. Her suit: base colour and the colour of
    any stripes, and where the stripes are. Anything worn on her wrists
    or cuffs, described exactly — including how many of anything you can
    count. HER BACK: describe it — its shape, its surface, and everything
    you can see on it. If there is nothing on it, say that explicitly.
 2. HER HELMET AND THE GLASS IN FRONT OF HER FACE. Describe the shape of
    the transparent part the way a geometer would: trace its outline.
    Does it have countable straight edges and corners, and how many of
    each — or is it one continuous curved surface with no edge at all?
    Does it lie in a single plane, or does it wrap around her head? Is
    there a border of a different material around it; if so, how wide is
    it and what is it made of? How does light behave on it — can you see
    her face through it, or does it return the sky? Give sizes relative
    to her face.
 3. ANY SECOND PERSON. Build, suit colours, and — in detail — WHAT IS ON
    THEIR BACK. Describe its overall form, its proportions relative to
    their shoulders, how far it stands out from their body, what its
    surface and its edges look like, and everything that projects from
    it, counted. Say whether it looks the same in every appearance.
 4. THE STRUCTURE IN SPACE. Its shape, its approximate length, the
    colours on it, what is attached to it and where.
 5. THE VEHICLE, if you see one. Its shape, and WHICH WAY ITS NOSE POINTS
    on screen in each segment it appears in. Whether anything is open on
    it. Whether it is undamaged.
 6. THE SKY AND THE GROUND. What is above, what is below, where the light
    comes from on screen in each segment.
 7. ANY READABLE CHARACTER ANYWHERE. Letters, digits, numbers, symbols,
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
    a beginning" is not evidence. "The structure is intact here and bent
    in Segment 4" is evidence.

 c) THE CLOCKS. List the physical states you used as one-way markers, and
    for each, name the segments on each side of it. Say how confident you
    are in each one.

Then answer, in one line each:
    - Which single placement are you LEAST sure of, and why?
    - Are there any segments you could not place at all? Say which, and
      say what is missing from them that would have let you place them.


⛔ STEP 5 — TELL THE STORY

In your own order from STEP 4, write what happens, in at most 200 words,
as plain events. No interpretation of meaning, no theme, no praise. What
happens, to whom, in what order.

Then answer these directly:

 1. What is the SINGLE EVENT that changes everything? Which segment is it
    in, at what timecode, and is it legible in one viewing?
 2. Is it clear WHERE the people are and what they are doing there? If
    not, what is missing?
 3. Is it clear that the two people know each other and are working
    together? On what evidence?
 4. Does the sequence have a beginning, a turn and an end as material, or
    is it a set of shots that do not resolve? Answer plainly.
 5. ⭐ WHAT WOULD A FIRST-TIME VIEWER NOT UNDERSTAND? List every point of
    confusion, with segment and timecode. Be exhaustive and be blunt.
    This is the most useful list in the report — do not shorten it out
    of politeness, and do not fill it with things you personally
    understood on a second look.
 6. Which segment carries the MOST information about the story? Which one
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
PASSPORTS AS SEEN         (the seven items from STEP 3)
REBUILT ORDER             (order, evidence, clocks, least-sure, unplaced)
THE STORY                 (200 words, then the six questions)
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
film. You are auditing ONE reel: the second phase of a 120-scene science
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

⭐ AND ONE MORE THING, SPECIFIC TO THIS PHASE

THIS PHASE CONTAINS AN EVENT. Things get destroyed in it. The world in
this reel exists in two states, before and after, and BOTH ARE CORRECT.
Damage is not a defect here — damage in the WRONG ENTRY is.

Because the order is scrambled, you cannot use position to know which
state a shot should be in. You do not need to. EVERY CATALOGUE ENTRY
DECLARES ITS OWN STATE. Read it there and judge it against that.


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

⭐ THE MEASURED SHOT LENGTH IS ONE OF THE MOST VALUABLE NUMBERS IN THIS
REPORT. State it explicitly. Also state whether the individual segments
are all the same length within 0.3 s, or whether they differ.


⛔ STEP 0 — THE COMPILATION RULE, AND THE ONE MOVING SHOT

This reel is a COMPILATION. A cut at every segment boundary is REQUIRED
BY THE ARCHITECTURE. NEVER report a cut, an angle change, a lens change,
a lighting change or a location change AT a segment boundary as an
error, a hidden cut or a continuity break. Adjacent segments are
supposed to look nothing alike.

DO report, at maximum severity, any cut, camera reset, angle jump,
sudden reframe or teleport that happens INSIDE a segment. Every segment
must be one unbroken take.

⭐ CAMERA MOVEMENT — read this twice:
    EXACTLY ONE catalogue entry has camera movement: entry D. It is a
    very slow push-in of about half a metre over the whole shot, under
    10% of frame. That movement is CORRECT and is not a finding.
    EVERY OTHER ENTRY IS LOCKED OFF WITH ZERO MOVEMENT. Any pan, tilt,
    track, zoom, drift, handheld float or shake in any entry other than
    D is a finding at high severity.
    If entry D has NO movement at all, that is also a finding, a smaller
    one — report it.


⛔ STEP 0.5 — HOW TO REFER TO THINGS

Number the segments by their POSITION IN THE FILE you were given:
Segment 1 is the first one you see, Segment 2 the second, and so on.
Give each one its measured start and end timecode.

Separately, each segment gets a CATALOGUE LETTER (A-L) once you have
identified it in STEP 2.

EVERY finding you write carries BOTH: the segment number with its
timecode, AND the catalogue letter. A finding without both is deleted
before you output it. Never use a scene number like "S17" — this reel
has no scene numbers you can trust.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before comparing anything, write down what you ACTUALLY SEE, in your own
words:
    - the woman (face, hair, helmet glass shape, suit stripe colour, back)
    - the man (build, suit stripe colour, WHAT IS ON HIS BACK - describe
      its shape in detail, see OPEN ITEM 1 below)
    - the platform and the instrument body, in BOTH states
    - the shuttle, in BOTH states
    - the debris: how it moves, how much of it, what shape
    - Earth and the sky

Only then compare against the catalogue. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


⛔ STEP 2 — IDENTIFY EVERY SEGMENT (this is the core of this audit)

Go through the segments one at a time. For each one, decide which
catalogue entry it is, using its CONTENT SIGNATURE - the combination of
scale, how many people are in it, what is being done, what objects are
present and WHICH STATE THE WORLD IS IN. The catalogue entries are
deliberately distinct enough that each one has a signature no other
entry has.

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
    Every shot: 16:9 horizontal, one unbroken take, ZERO internal cuts.
    Zero camera movement everywhere except entry D (see STEP 0).

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
    carried on a white support arm.
    THE SHUTTLE: a white winged vehicle about 40 metres beyond the
    platform. Its NOSE POINTS SCREEN-LEFT in every shot it appears in. A
    shuttle with its nose pointing screen-right is a finding.
    EARTH: blue-white, cloud-streaked, in the lower and/or left part of
    frame in every wide shot. Black space with hard pinpoint stars
    above. Vacuum has no air: no haze, no glow around objects, no light
    shafts, no visible beams.

⭐ THE WORLD HAS TWO STATES - AND THIS IS THE HEART OF THIS AUDIT

    STATE 1 - INTACT
        Truss straight and unbroken. Grey cylinder mounted square on its
        white support arm. Handrails continuous. Shuttle hull unbroken,
        cargo bay doors OPEN and attached.
    STATE 2 - WRECKED
        The support arm is TORN where it met the truss; the cylinder
        hangs askew on one remaining bent strut with its cover bent open
        at the hinge. One section of truss is crumpled inward. Lengths
        of ORANGE rail are torn free and drifting. The shuttle hull has
        THREE clean dark punctures and a peeled strip of insulation
        blanket, and ONE cargo bay door is GONE.

    Each catalogue entry names its own state: INTACT, WRECKED, or
    TRANSITION (starts intact, ends wrecked, within the shot).

    Damage in an entry marked INTACT is a finding at maximum severity.
    An entry marked WRECKED that shows an undamaged platform or an
    unpunctured shuttle is a finding at maximum severity.
    ⛔ The damage in a WRECKED or TRANSITION entry is NOT a finding. Do
      not report the crumpled truss, the hanging cylinder, the torn rail
      lengths, the punctures or the missing door as errors. They are the
      story.

    DAMAGE IS ONE-WAY. Nothing is ever repaired, cleaned, straightened,
    reattached or made whole. Nothing in this phase gets better.

LIGHT
    ONE source: hard white sun, plus a soft cool blue-white bounce
    coming UP from Earth. Nothing else emits light. Shadows are ABSOLUTE
    BLACK with razor edges - vacuum has no fill.
    ⭐ THE SUN IS IN THE SAME PLACE IN ALL TWELVE SHOTS: UPPER
      SCREEN-RIGHT. There is no exception anywhere in this phase. A shot
      keyed from the left, from below, or from behind camera is a
      finding.
    Bounce always comes from below.
    NOTHING BURNS. No flame, no fire, no glow, no ember, no spark, no
    smoke, no dust cloud, no vapour cloud, no shockwave, no flash, no
    explosion anywhere in this reel, including at the moment things
    break. Metal parts cold and silently. Any of the above is a finding
    at maximum severity.

⭐ DEBRIS BEHAVIOUR - the physical law of this phase
    Where debris appears, it obeys all of the following:
      - Every piece travels in a DEAD STRAIGHT LINE. No curve, no arc,
        no drift off-line, no swirl, no spiral, no orbiting motion.
      - Every piece travels from SCREEN-RIGHT to SCREEN-LEFT. A piece
        crossing left-to-right is a finding.
      - CONSTANT SPEED. Nothing accelerates, decelerates, slows down
        near the camera, hovers, hangs, settles or stops.
      - Pieces that tumble KEEP TUMBLING at the same rate. A tumble that
        slows or stops is a finding - nothing damps rotation out here.
      - In the near field, the discrete pieces are COUNTABLE and there
        are TWELVE OR FEWER of them on screen at once. A dense cloud, a
        swarm, a storm or an uncountable blizzard in the near field is a
        finding. Distant debris may read as fine parallel texture.
      - Debris never contacts a human body. If a fragment strikes,
        grazes or passes through a person, that is a finding at maximum
        severity.

⭐ ROTATION LOCK
    Once the woman is adrift and turning, she turns at ONE CONSTANT RATE
    of roughly twenty degrees per second - a full turn every eighteen
    seconds. She never speeds up and she never slows down. There is
    nothing out there to slow her.
    THE ONLY THING THAT MAY STOP HER ROTATION IS A HAND ON HER BODY. In
    the one entry where a second figure grips her, her turn slows and
    stops AND HIS BODY IS PUSHED THE OTHER WAY at the same instant - the
    momentum has to go somewhere. Her stopping without a counter-motion
    on him is a finding.
    Rotation that decays on its own in any entry is a finding.

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
    A short vertical pale scar on her LEFT temple near the hairline.
    Dark chestnut jaw-length hair, tucked behind both ears.

    SUIT: warm off-white with ORANGE reinforcement stripes on shoulders,
    knees and glove cuffs. A soft chest panel with three small coloured
    lights and NO numerals.

    ⭐ HER BACK IS FLAT. Smooth off-white shell fabric, one vertical
      spine seam, a low webbing waist belt. NO pack, NO tank, NO
      backpack, NO hose, NO cable, NO frame, NO thruster unit of any
      kind. Anything mounted on her back is a finding at maximum
      severity. She is tethered to the structure; she carries nothing.
      Entry I turns her back fully to camera - that entry is the
      decisive test of this lock, and you must state its result
      explicitly.

    ⭐ HELMET: a rigid white shell with a FLAT RECTANGULAR front glass,
      24 by 16 centimetres, held in a VISIBLE bright metal frame the
      width of a finger. Four straight edges and four corners you can
      count. The glass is optically clear: zero tint, no mirror coating,
      her face fully readable through it. It may carry a faint
      TRANSPARENT reflection - you see the reflection and her face at
      the same time, never a mirror.
      A domed, bubble, spherical, wraparound, frameless, seamless,
      tinted, gold or mirrored visor is a finding at maximum severity.

    WRISTS: a ring of six small amber light segments set into her LEFT
    glove cuff. A steel mechanical watch on a black strap over her RIGHT
    glove cuff, its hands STOPPED. Left and right never swap. Each entry
    below states how many ring segments should be lit in it.

    TETHER: an orange-and-white line from her hip ring to the structure.
    Each entry states whether it is attached, parting or gone.


================================================================
IDENTITY PASSPORT B - THE MAN (commander)
================================================================
    45 years old. 1.85 m, broad and heavy-shouldered. Square jaw, deep
    nasolabial lines, close-cropped grey-flecked dark hair, grey-blue
    eyes.
    SUIT: the same warm off-white, but the stripes are NAVY BLUE, never
    orange. The same flat rectangular framed visor as hers.
    He appears in TWO entries only: fully in K, and as one gloved hand
    with a NAVY cuff in L.
    ⚠️ WHAT IS ON HIS BACK: see OPEN ITEM 1. Describe it. Do not score it.


================================================================
⭐ INTENDED - DO NOT REPORT THESE AS ERRORS
================================================================
 1. Cuts at segment boundaries. Required by the architecture.
 2. Adjacent segments looking nothing alike. Required.
 3. The slow push-in in entry D. The only intended camera move.
 4. The damage in entries D (second half), E (second half), J and L.
    That is the event this phase exists to show.
 5. The grey cylinder hanging crooked on one strut in a WRECKED entry.
    It is not a modelling error; it is the wreck.
 6. Torn lengths of orange handrail drifting away from the platform in a
    WRECKED entry.
 7. The shuttle missing one cargo bay door in a WRECKED entry.
 8. The river of tiny specks flowing across the sky in entry C. It is
    debris seen at distance, not a filter, not an artifact, not grain,
    not a star trail.
 9. Her being alone, with no crew visible, in nine of the twelve entries.
10. The frayed useless stub of her old tether floating beside a new line
    in entry L. Both lines present at once is correct there.
11. A silent reel with no dialogue and no music.
12. Her face showing no expression change in a close-up. Held stillness
    is the performance.


================================================================
⚠️ OPEN ITEM 1 - THE COMMANDER'S BACK: DESCRIBE IT, DO NOT SCORE IT
================================================================
The production documents disagree with each other about what the man
wears on his back, and the point of this audit is to find out which one
the render produced. So you are given NO description of it.

In the entry where he appears, look at his back and write a paragraph:
    - Is it one solid closed object, or an open structure you can see
      through?
    - Its overall shape, and its proportions - is it taller than wide,
      wider than tall, or square?
    - Roughly how far does it stand out past his shoulders on each side,
      and how far off his back?
    - Are its edges straight or curved? Are its corners sharp or round?
    - Is its surface divided into panels, and by what?
    - Does anything stick out of it - arms, pods, nozzles, tubes, struts?
      Are they flush with the surface or standing off it? Count them.
    - Where does the thrust come from when he manoeuvres, and what shape
      is the plume?

Write this as OBSERVATION. Give it NO score and NO verdict, and do not
say whether it is right or wrong. Someone else decides that.


================================================================
⚠️ OPEN ITEM 2 - THE WRECK HAS NO REFERENCE: DESCRIBE IT PRECISELY
================================================================
The wrecked state of the platform was never drawn as a reference sheet.
Whatever this reel produced will become the master for everything that
follows, so it has to be written down exactly.

From the entries that show the wreck, write a precise paragraph:
    - Which section of the truss is crumpled, and where along its length?
    - How is the cylinder hanging - what angle, on how many struts,
      which side?
    - Is its cover open or shut, and how far?
    - How many separate torn pieces are drifting near the wreck, and
      roughly how big are they?
    - Do the wrecked entries agree with each other? If two of them show
      the wreck differently, say exactly how. That disagreement is a
      finding at high severity, because they are the same object.

Describe it. Do not score it.


================================================================
THE SHOT CATALOGUE - twelve entries, no order implied
================================================================
Letters are labels only. A is not first and L is not last. Identify by
signature, not by letter.

Every entry: 16:9, one unbroken take, sun from upper screen-right, no
readable text, no readable mouth.


A - OVER HER SHOULDER TO THE SHUTTLE      1 figure · INTACT
    Medium shot, 35mm, from 1.5 m directly BEHIND her at shoulder
    height. Her left shoulder and the back of her helmet fill the
    screen-left foreground, SOFT; past her the truss with orange rails
    runs away to the screen-right; the white shuttle hangs far off,
    sharp, nose screen-left, cargo doors open and attached. Earth's limb
    along the bottom.
    Ring: 6 lit if legible. Tether: attached, taut. Sky: no debris
    visible anywhere in frame.
    HAPPENS: her right glove tightens on a rail post until the fabric
    creases; her helmet turns to the screen-right and holds; she then
    pulls herself along the rail hand over hand, past the camera-side
    post, legs trailing a beat behind, and does not stop.
    SIGNATURE: the only over-the-shoulder shot in the reel. The only one
    where the camera is behind her with the shuttle sharp beyond.
    ⛔ No mouth in frame at any point. She never turns to camera.

B - FULL BODY ON THE RAIL, TRUE SCALE     1 figure · INTACT
    Wide shot, 24mm, from 9 m away level with the truss, eye-level,
    Earth's horizon perfectly horizontal, deep focus. She is small in a
    big frame: the whole figure, the whole truss, and the shuttle far
    off in the screen-right third, nose screen-left, doors open.
    Ring: 6 lit if legible. Tether: attached.
    Sky: in the UPPER SCREEN-LEFT of the black, a thin bright line of
    sunlit specks - a distant line, not a flow across frame.
    HAPPENS: both gloves work a metal karabiner off a rail post and clip
    it onto a line running along the rail; she gives it ONE SHARP TUG as
    a test and her whole body swings a few centimetres against it and
    settles; then she moves hand over hand to the screen-right, passing
    a post without pausing. The specks in the upper left grow slightly
    longer and brighter. SHE NEVER LOOKS UP AT THEM.
    SIGNATURE: the only full-body wide of a single figure on an intact
    platform, and the only shot where a karabiner is transferred and
    tested.

C - THE SKY IS FLOWING                    0 figures · INTACT
    Extreme wide shot, 24mm, from 6 m, camera pitched UP 20 degrees at
    the sky, deep focus.
    The upper two thirds: black space filled with hundreds of tiny
    sunlit specks running in PERFECTLY PARALLEL STRAIGHT LINES from
    screen-right to screen-left, like a river of light seen edge-on.
    The lower third: still and calm, the top of the grey instrument
    cylinder and the edge of the truss with an orange handrail, both
    undamaged, shadows unchanged throughout.
    ⭐ Far beyond the band, ONE SMALL FIXED BRIGHT POINT that does NOT
      move with the flow and does not move at all. It must still be in
      exactly the same place in the last frame as in the first. A bright
      point that drifts with the debris is a finding.
    HAPPENS: the band thickens from the screen-right edge as more specks
    enter; a few larger pieces cross within it, tumbling end over end at
    constant rates, each on a dead straight path; the band reaches its
    densest and the flow continues unbroken to the last frame. The
    platform edge below is NEVER touched and never moves.
    SIGNATURE: the only shot with no one in it that looks UP at the sky.
    The only shot where the sky is a flowing river.
    ⛔ ZERO humans. Any figure, limb, glove or helmet is a finding at
      maximum severity.

D - THE WAVE ARRIVES                      1 figure · TRANSITION
    Wide shot, 24mm, from 7 m ABOVE the truss, camera pitched DOWN 20
    degrees, deep focus, true scale.
    ⭐ THE ONLY SHOT WITH CAMERA MOVEMENT: a very slow push-in of about
      half a metre across the shot, under 10% of frame. No other move.
    She clings to the ORANGE handrail with BOTH gloves, knees drawn up,
    helmet down and turned away. Earth's sunlit curve fills the lower
    left. Ring: 6 lit if legible. Tether: attached, taut throughout.
    STARTS INTACT, ENDS WRECKED:
      - six small fragments cross the near field from the screen-right
        in dead straight lines at constant speed
      - a larger piece crosses; the white support arm TEARS where it
        meets the truss; the grey cylinder swings slowly outward on its
        one remaining strut and KEEPS SWINGING at a constant rate
      - a section of truss beyond her crumples inward; two orange rail
        lengths bend, one comes free and drifts off screen-left in a
        straight line, turning end over end at a constant rate
      - her body is pulled a few centimetres along the rail by the
        shudder; HER GLOVES HOLD - she is never torn off in this shot
      - fragments thin out; the cylinder hangs askew, cover bent open
      - the last near fragment leaves screen-left; she is still on the
        rail, tether taut, the platform wrecked around her
    ⛔ No flash, no flame, no smoke, no spark, no shockwave at the
      tearing. Cold metal parting.
    ⛔ Near-field discrete fragments: TWELVE OR FEWER on screen at once.
    SIGNATURE: the only shot where the platform is whole at the start
    and wrecked at the end. The only shot with camera movement.

E - THE SHUTTLE IS PUNCTURED              0 figures · TRANSITION
    Medium shot, 50mm, from 15 m, eye-level with the hull, deep focus.
    The mid-flank of the white winged shuttle fills the frame, its nose
    pointing screen-left and OUT of frame; one open cargo bay door
    stands up from the hull with its white inner face in sun. Earth's
    blue curve low in frame.
    STARTS INTACT, ENDS DAMAGED:
      - three small fragments cross the near field from the screen-right
        in straight lines at constant speed; the hull is intact
      - one clean round dark puncture opens in the white hull below the
        door, its edge bent INWARD; a puff of white insulation fibre
        drifts out in a straight line and thins. NO FLASH.
      - two more punctures appear along the flank, a hand's width apart,
        each a clean dark hole; a strip of quilted blanket peels back,
        lifts slowly, and HOLDS - it does not tear away
      - the open cargo door SHEARS AT ITS HINGE, lifts free as one
        piece, and drifts screen-left in a straight line, turning end
        over end at a constant rate, its white face flashing sun once
        per turn; it leaves at the left edge
      - the punctured flank hangs still: three dark holes, one peeled
        strip, one missing door
    ⛔ No flame, no smoke, no explosion, no burning edge, no spark.
    SIGNATURE: the only shot of the shuttle's hull alone. The only shot
    where a door comes off.
    ⛔ ZERO humans.

F - THE LINE PARTS                        1 figure · no structure
    Close-up, 85mm, from 0.9 m, THREE-QUARTER FRONT, at eye level with
    her face. Shallow focus: face, visor and the tether line sharp,
    background soft.
    At the LOWER RIGHT edge of frame, the orange-and-white tether line
    is pulled straight as a bar under load. In her clear visor a faint
    TRANSPARENT reflection of Earth's blue curve lies across the lower
    third. Eyes wide, mouth closed.
    HAPPENS: the line PARTS - it goes slack in an instant and its free
    end whips out of the lower right of frame in a straight line. Her
    eyes snap to where it was. Then the reflection in her visor BEGINS
    TO SLIDE: Earth creeps up across the glass, black comes in from
    below, a slow constant rotation at twenty degrees a second, never
    speeding up, never slowing. Breathing shallow and quick; jaw sets;
    her shoulders make a small rhythmic movement (fingers tapping out of
    frame). A bead of sweat lifts off her temple and drifts STRAIGHT UP
    inside the helmet. Her eyes close for one breath and open.
    Ring: out of frame. Tether: PARTS during this shot.
    SIGNATURE: the only close-up in which a tether line is visible and
    separates.
    ⛔ Mouth closed throughout. No lip movement.
    ⛔ The visor reflection is TRANSPARENT - her face stays readable
      through it. A mirror visor is a finding at maximum severity.

G - THE EMPTY HAND                        1 hand only · no structure
    Extreme close-up, 100mm macro, from 0.35 m, SIDE-ON to the glove,
    profile. Shallow focus: the glove and the ring sharp, everything
    beyond soft.
    Her LEFT glove reaches into empty black space, fingers spread wide.
    On the cuff: a ring of six small amber light segments — ⭐ FOUR LIT,
    TWO DARK. This is the only entry in the reel where the ring is meant
    to be fully legible, and it must read four-of-six. Six lit here is a
    finding at high severity.
    Behind the glove, out of focus, Earth's blue curve slides across the
    frame at a CONSTANT rate.
    HAPPENS: the fingers close on nothing, slowly, and open again; the
    hand turns at the wrist, palm to camera, and closes into a loose
    fist that stays closed; Earth slides out of the top of frame leaving
    black and hard stars; the fist relaxes one finger at a time; the
    blue edge of Earth slides back in from the lower right; the open
    hand hangs in the black, still reaching.
    SIGNATURE: the only extreme close-up of a hand. The only shot where
    nothing but a glove and a ring is in focus.
    ⛔ No face, no second person, no structure, nothing to grab.
    ⛔ The four lit segments are small, steady, sharp-edged amber lights
      with NO halo and NO number beside them.

H - THE TUMBLE, HEAD ON                   1 figure · wreck in background
    Close-up, 85mm, from 0.8 m, HEAD-ON at eye level with her face.
    Shallow focus: face and visor sharp, background soft.
    Her face is fixed in frame while everything behind her rotates:
    Earth's tilted sunlit curve sweeps out of the lower half and black
    sweeps in, at twenty degrees a second, ONE CONSTANT RATE that never
    changes across the whole shot.
    HAPPENS: background goes all black and stars; her breathing fast and
    shallow, jaw locked, lips closed; Earth sweeps back in from the
    UPPER edge, upside down relative to the start, same rate; ⭐ THE
    WRECKED PLATFORM, tiny and white, passes ONCE through the soft
    background and is gone; the sun's key crosses her face from right to
    left as she turns; her eyes close for one breath and open; a single
    hair strand lifts across her forehead; Earth enters once more from
    the upper edge, rate unchanged.
    Ring: out of frame (4 lit if glimpsed). Tether: GONE.
    SIGNATURE: the only head-on close-up with the background in full
    rotation.
    ⛔ Mouth closed throughout.
    ⛔ The rotation rate must be identical in the first second and the
      last. Any acceleration or decay is a finding.

I - ADRIFT, TURNING, BACK TO CAMERA       1 figure · wreck in background
    Medium shot, 35mm, from 1.5 m, side-on, profile, at her chest
    height, deep focus.
    She is adrift in empty space, turning slowly and steadily to the
    screen-left at one constant rate, drifting a few centimetres to the
    screen-right as she turns. Earth's sunlit curve fills the lower
    third, black above. ⭐ Far off SCREEN-LEFT, tiny, the WRECKED
    platform.
    Ring: 4 lit if legible. Tether: GONE.
    HAPPENS: she turns until her BACK IS FULLY TO THE CAMERA and her
    helmet faces away — ⭐ THIS IS THE DECISIVE TEST OF THE FLAT-BACK
    LOCK. Her back must read as flat off-white shell fabric with one
    spine seam, a low waist belt, orange shoulder stripes catching sun,
    and NOTHING MOUNTED ON IT. State explicitly what you see there.
    Then her left glove comes in and folds across her chest with the
    right, both arms held tight; she turns back through profile and her
    face comes into view, calm, eyes open, mouth closed; three-quarter
    front, still turning, arms folded, drifting.
    ⛔ She speaks in this shot in the finished film, with her back
      turned. There must be NO readable mouth at any point.
    SIGNATURE: the only medium shot of her adrift alone in which her
    back fully faces the camera.

J - THE WRECK FROM ABOVE                  0 figures · WRECKED
    Wide shot, 24mm, from 12 m ABOVE the platform, camera pitched DOWN
    25 degrees, deep focus.
    The wrecked service platform, seen whole from overhead: the truss
    crumpled along one section; the grey cylinder hanging askew on a
    single bent strut with its cover bent open; torn ORANGE rail lengths
    drifting nearby; Earth's sunlit curve filling the lower left.
    HAPPENS: the last fragments cross the left edge and are gone; the
    drifting rail lengths and loose pieces move away from the wreck at
    constant speed on straight lines, turning slowly at constant rates;
    ⭐ THE SKY CLEARS to black and hard stars and STAYS clear; the
    cylinder hangs still on its strut; one orange rail length leaves the
    frame at the bottom edge; Earth's cloud bands creep beneath the
    wreck; nothing else moves but the slow straight drift of the loose
    pieces.
    SIGNATURE: the only overhead shot of the wreck with no one in it.
    The only shot where the sky goes from debris to clear.
    ⛔ ZERO humans. Any figure is a finding at maximum severity.
    ⛔ Nothing burns, nothing sparks, nothing strobes, no alarm light.

K - THE CATCH                             2 figures · no structure
    Medium shot, 35mm, from 1.5 m from the woman, eye level with her
    chest, deep focus.
    Foreground: the woman adrift, three-quarter front, turning slowly at
    one constant rate, arms folded. Background to the SCREEN-RIGHT,
    small at first: the man, flying IN TOWARD THE CAMERA, growing across
    the shot, one arm already reaching. Earth's sunlit curve fills the
    lower third.
    Ring: 4 lit if legible. Tether: hers is GONE.
    HAPPENS: from a corner of his back unit, ONE SHORT THIN WHITE PLUME
    — a straight sharp cone that stops instantly, no cloud, no trail, no
    lingering vapour; he moves in from background to foreground on a
    DEAD STRAIGHT LINE, his own body steady and NOT turning; a second
    shorter plume from the OPPOSITE corner and he slows and arrives
    beside her, large in frame; his right glove closes on her left
    forearm with a clear grip.
    ⭐ THE PHYSICS TEST OF THIS PHASE: at the instant he grips her, her
      rotation slows and stops AND HIS BODY IS JOLTED THE OTHER WAY in a
      small counter-swing, his legs drifting a beat behind. Two separate
      motions become one. Her stopping with no reaction on him is a
      finding at maximum severity.
    Then his left glove lets go of a control arm and takes her shoulder;
    her arms unfold; her right glove closes on the control arm; they
    hold together, still, two helmets a hand apart, faces turned to each
    other.
    SIGNATURE: the only two-figure shot, and the only shot in which a
    figure travels from background to foreground.
    ⛔ Exactly two figures. A third is a finding at maximum severity.
    ⛔ Orange stripes on her, NAVY on him. Never both orange.
    ⛔ Both faces are visible at the end and NEITHER mouth may move.

L - THE CLIP                              2 gloves · WRECKED shuttle
    Close-up, 85mm, from 0.5 m ABOVE her hip, looking DOWN at the ring,
    high angle. Shallow focus: gloves, ring and karabiner sharp, the
    shuttle soft.
    In frame: her hip, a small steel ring sewn into her off-white suit,
    her own ORANGE-cuffed glove steadying it, and a big off-white glove
    with a NAVY cuff stripe bringing a steel karabiner on an
    orange-and-white line to it.
    ⭐ Beyond, out of focus: the PUNCTURED white shuttle with a DARK GAP
      where one cargo door is missing, drifting slowly to the
      screen-left on a straight line and turning slowly.
    HAPPENS: the karabiner hooks the ring and the spring gate snaps shut
    under his thumb; his glove gives the line a short tug and the ring
    pulls a centimetre and HOLDS; his glove withdraws to the
    screen-right; her glove stays on the ring, then her fingers slide
    along the new line to check the gate and rest. Beside the new line,
    the FRAYED STUB of her old tether floats straight — both lines
    present at once is correct.
    SIGNATURE: the only close-up of two gloves at a hip. The only shot
    in which a new line is attached.
    ⛔ Two gloves, no faces, no helmets, no third hand.
    ⛔ One cuff ORANGE and one cuff NAVY. Two orange cuffs is a finding.


================================================================
⭐ CROSS-SHOT CHECKS - the part that does NOT depend on order
================================================================
These are the only "continuity" judgements in this audit. They compare
shots against each other WITHOUT any assumption about sequence. Answer
every one, by name, and name the segments in each answer.

 1. IS SHE THE SAME PERSON in every shot she appears in? Bone structure,
    age, eye spacing, skin, hair length. The temple scar on the LEFT
    wherever it is visible.
 2. IS THE VISOR THE SAME GEOMETRY in every shot? Flat pane, visible
    metal frame, four countable edges, clear glass. Name any shot where
    it changes, and say which shots show a dome.
 3. IS HER BACK FLAT in every shot where it is visible? Name each shot
    where her back can be seen and say what is on it. Entry I is the
    decisive one.
 4. IS HIS BACK UNIT THE SAME OBJECT in every shot he appears in?
    Describe it once (see OPEN ITEM 1), then say whether it holds.
 5. IS THE SHUTTLE'S NOSE ALWAYS SCREEN-LEFT wherever it appears?
 6. ⭐ IS THE WRECK THE SAME WRECK? The intact platform and the wrecked
    platform are the SAME OBJECT in two states. Does the wrecked version
    have the same truss length, the same rail colour, the same cylinder
    in the same place on the same end? Is the SAME section crumpled in
    every wrecked entry? Is the cylinder hanging at the same angle on
    the same side? Two wrecks that differ from each other is a finding
    at high severity - name exactly how they differ.
 7. ⭐ IS THE DAMAGE ONE-WAY? Does anything appear repaired, straightened
    or reattached in any entry? Does any entry marked WRECKED show an
    intact platform, or any entry marked INTACT show damage? List every
    such contradiction.
 8. ⭐ DOES THE DEBRIS ALWAYS FLOW SCREEN-RIGHT TO SCREEN-LEFT? Name
    every entry with debris and give its direction. Any entry flowing
    the other way is a finding. Do any pieces curve, swirl, slow, hover
    or stop?
 9. ⭐ IS THE ROTATION RATE THE SAME in every entry where she is adrift
    and turning? Estimate the rate in each - roughly how many seconds
    for one full turn. Does it ever slow with no hand on her?
10. THE RING: entry G must read FOUR lit of six. Report the count in
    every entry where the ring is legible at all, and name any entry
    where it contradicts its own entry.
11. IS THE SUN ALWAYS FROM THE UPPER SCREEN-RIGHT, in all twelve? Name
    every exception.
12. IS EARTH ALWAYS BELOW or to the lower left wherever it appears?
13. THE SKY AS A CLOCK: for each entry, say what the sky holds - nothing,
    a thin distant line, a dense flow, thinning fragments, or clear
    stars. Just report the split. Do NOT call any of them wrong; the
    correct order is decided elsewhere.


================================================================
WHAT TO SCORE - thirteen categories, 1 to 10
================================================================

 1. COVERAGE - how much of the catalogue is actually present, and how
    confidently could each segment be identified? Score the reel as a
    body of material, not the order.
 2. IDENTITY CONTINUITY - does she hold across every shot she is in?
 3. HELMET AND VISOR GEOMETRY - flat rectangular pane, visible metal
    frame, four countable edges, clear glass, face readable. Score this
    separately and score it hard.
 4. COSTUME AND BACK - orange on her, navy on him, HER BACK FLAT with
    nothing mounted on it, ring on the left cuff, watch on the right.
    (The SHAPE of his back unit is not scored - see OPEN ITEM 1.)
 5. FIGURE COUNT AND CLONE CONTROL - correct counts per catalogue entry.
    Special attention to the three ZERO-figure entries C, E and J, and
    to the two-figure entries K and L.
 6. CAMERA DISCIPLINE - locked off everywhere except the push-in in D,
    one unbroken take each. Boundary cuts are NOT findings.
 7. LIGHT AND SHADOW - one sun from upper screen-right in all twelve,
    Earth bounce from below, absolute black razor-edged shadows, no
    bloom, no flare, no haze, no light shafts, nothing burning.
 8. VACUUM PHYSICS - bodies, tethers and plumes: straight lines,
    constant speed, continuous momentum; nothing hovers, settles,
    swirls or falls; taut tethers; thruster gas a narrow straight cone
    that stops instantly; bodies never rigid.
 9. ⭐ DEBRIS BEHAVIOUR - straight lines, constant speed, right to left,
    twelve or fewer countable in the near field, tumbles that never
    decay, no contact with any body, no fire, no smoke, no shockwave.
10. ⭐ DAMAGE STATE AND CONTINUITY - is each entry in the state its own
    catalogue line declares, is the wreck the same wreck everywhere,
    and is the damage strictly one-way?
11. TEXT AND SYMBOL DISCIPLINE - zero readable characters anywhere.
12. WORLD CONSISTENCY - the cross-shot checks above: same platform, same
    shuttle orientation, same counters, same sun, Earth always below.
13. DELIVERY HYGIENE - no title card, no end card, no credits, no
    captions, no watermark, no logo, no letterboxing. Film grain present
    and consistent. Segments the same length.

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
    What you actually observed for the woman, the man, the platform in
    both states, the shuttle in both states, the debris and the sky -
    before comparison.

THE COMMANDER'S BACK UNIT - OBSERVATION ONLY
    The paragraph from OPEN ITEM 1. No score, no verdict.

THE WRECK - OBSERVATION ONLY
    The paragraph from OPEN ITEM 2, including whether the wrecked
    entries agree with each other.

SCORES
    Thirteen rows with a one-line justification each, then the mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: segment
    number, timecode, catalogue letter, severity, what is wrong, why it
    matters.

FINDINGS BY SEGMENT
    Every segment in file order. For each: catalogue letter, what you
    verified as correct (briefly), then each deviation with a timecode
    and a severity. If a segment is clean, say so in one line.

CROSS-SHOT CHECKS
    The thirteen checks above, answered one by one, by number.

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
- ⛔ Never report the damage in a WRECKED or TRANSITION entry as an
  error. Read each entry's declared state before you judge it.
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
  shot of a few seconds. Do not recommend coverage, inserts, reaction
  shots, cutaways or camera moves - this format has none.
```

---
---

# 📌 İKİ RAPOR GELDİKTEN SONRA — GEÇİŞ C (bende)

```
1) İkisi de 02_HAM_RAPORLAR/ altına BİREBİR düşer [AGENTS kural ④].
   YERCEKIMI_FAZ02_KOR_HAM.md  ·  YERCEKIMI_FAZ02_KATALOG_HAM.md

2) ③ KİMLİK KAPISI — bu sefer gerçek çapayla koşar.
   A raporundaki tarifler denetçiye SÖYLENMEDİ. Belgeye eşlenen her
   metin-dışı tarif GERÇEK ÇAPADIR. Eşik: en az 2.
   ⭐ Faz 1'de kapanamayan kapı burada kapanır.

3) ⭐ SIRA SKORU — filmin okunabilirlik ölçüsü
   A'nın kurduğu sıra ile gerçek sıra karşılaştırılır:
     doğru yerleştirilen klip / toplam klip = ___/12
   Yanlış yerleştirilen her klip = görsel zincirin koptuğu adres.
   Bu sayı fazlar arası karşılaştırılabilir; F3'ten itibaren eğri çizilir.

4) ⑩ ÖNERME KAPISI — A'nın "anlaşılmayanlar" listesi plana karşı okunur.
   Bilerek gizlenen bilgi (S22'ye kadar B'nin varlığı, enkaz saati) ile
   kazara anlaşılmayan ayrılır. İlki tasarımdır, ikincisi kusurdur.

5) B'nin çelişkileri A'nın gözlemiyle sağlanır. İkisi aynı şeyi
   söylüyorsa bulgu SAĞLAM. Yalnız B söylüyorsa bulgu ŞÜPHELİ (yankı
   olabilir). Yalnız A söylüyorsa bulgu GERÇEK ama ölçüsüz.

6) Skor satırı ⚠️ ŞARTLI kalır: film klasöründe *_QA_SPEC.md YOK [D129]
   ve master elde yok [⑪]. Faz koşusu T tablolarına GİRMEZ.
```

---

## 🔑 KATALOG HARFİ → SAHNE NUMARASI

⛔ Bu tablo İKİ PROMPTUN DA DIŞINDADIR. Rapor geldikten SONRA kullanılır.

| Harf | Sahne | Başlık | Kadro | Durum |
|:--:|:--:|---|:--:|---|
| A | S13 | İPTAL | 1 | SAĞLAM |
| B | S14 | PROSEDÜR | 1 | SAĞLAM |
| C | S15 | GÖK AKIYOR | 0 | SAĞLAM · 🔥 viral #1 |
| D | S16 | DALGA BİR | 1 | **GEÇİŞ** · tek hareketli plan |
| E | S17 | MEKİK | 0 | **GEÇİŞ** |
| F | S18 | KOPUŞ | 1 | halat kopar |
| G | S19 | BOŞ EL | 1 el | halka 6/6 → **4/6** |
| H | S20 | SAVRULUŞ | 1 | enkaz arkada bir kez geçer |
| I | S21 | ÇAĞRI | 1 | ⭐ düz sırt testi |
| J | S22 | DOKSAN DAKİKA | 0 | HASARLI · gök temizlenir |
| K | S23 | YAKALAYIŞ | 2 | ⭐ momentum testi |
| L | S24 | KANCA | 2 eldiven | HASARLI mekik |

**Gerçek sıra: A→B→C→D→E→F→G→H→I→J→K→L** (S13'ten S24'e, alfabetik).
Sıra skoru bu diziye karşı hesaplanır.

---

## ⚠️ BU FAZDA ÜRETİM ÖNCESİ AÇIK KALAN İKİ DOSYA SORUNU

```
① RD p2 (HASARLI) REFERANS PANELİ ÜRETİLMEDİ — 0/15 panel
   D · E · J · L hasarlı durumu her klipte YENİDEN icat edilecek.
   Enkazın dört klipte tutması için tek yol: D veya J önce üretilir,
   çıkan kare RD p2 yerine geçer, kalan üçü ona bakarak üretilir.
   ⭐ 00_PLAN üretim sırası zaten S16'yı (D) başa koymuş — sebep bu.

② S23 ve S24 PROMPTLARI HÂLÂ "thruster frame" DİYOR
   FAZ_02_DALGA.md:1479 ve :1568. REFERANS_PAKETI'ndeki RC ise artık
   dikdörtgen levha. Aynı fazda iki tasarım.
   ⛔ Karar senin: promptu levhaya çevireyim mi, yoksa kafes tarifi
      kalsın mı. Ben tek başıma değiştirmiyorum — depoda 63 geçiş var
      ve tümü aynı anda dönmeli, tek tek değil.
```
