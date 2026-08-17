# 🔍 FAZ 7 / BEDEL — VİDEO ELEŞTİRİ PROMPTU

## On sahne · 1 dakika 40 saniye · 16:9 · faza özel rubrik

> **Ne işe yarar:** Faz 7'nin on sahnesi (S61–S70 · film zamanı 10:00–11:40)
> üretildiğinde, o videoları bu fazın KENDİ kilitlerine karşı denetler.
> Faz 1-2-3-4-5-6 rubrikleriyle aynı iskelet, farklı SPEC.
>
> **Faz 6'dan farkı — bu faz İKİ ÖLÜMCÜL İSTİSNA taşıyor.** Biri
> çekirdek kuralın bilinçli delinmesi (S65'te İKİ ÖZDEŞ Bekçi aynı
> karede), öbürü filmin son zemin tepkisi (S68). Rubriğin en değerli
> işi yedi şeyi ölçmek:
> ① **plakanın hiçbir sahnede TEPKİ VERMEMESİ** — parlama, halka,
> gösterge, ısı serabı, buhar, titreşim YOK; filmin çözümü ekranda
> ölü bir diskten ibaret kalır ve o ölülük sahnenin kendisidir,
> ② **zeminin YALNIZ S68'de** ve yalnız plakanın 20 cm YANINDA tepki
> vermesi — 2-3 mm kabarma, el kalkınca geri inme; diğer dokuz
> sahnede zemin ölüdür [KARAR 3 · filmin 3/3 son tepkisi],
> ③ **S65'in ikizinin bilinçli olması** — iki özdeş figür kural
> ihlali DEĞİL, sahnenin bilgisidir; buna karşılık S63 S67 S69 S70'te
> sedef figür HİÇ görünmemelidir,
> ④ Bekçi eldiveninin DÖRT HANE çıkması — F5 S45/S50 ve F6 S55'te üç
> koşuda üç kez BEŞ parmak çıktı [F5 D-X · F6 D-AG]; S62 ve S68 bu
> sınıfın 4. ve 5. karesi, parmaklar raporda SAYILIR,
> ⑤ S64 açıklığının **düz çatlak + bıçak-ince kenar** kalması — F6
> koşusunda model kemeri atladı ama KAPI KASASI çizdi [F6 D-AD],
> ⑥ duvarların hareketli kamera altında **düz ve boş** kalması — F6
> S52 tilt'inde panel çizgileri üredi [F6 D-AE]; F7'nin iki push-in'i
> (S61 · S64) aynı riskin üstünde,
> ⑦ ÖLÜ ASIL'ın bir CESET olmaması — çürüme, kemik, mumya, çökmüş
> kıyafet, toz YOK; ölümü anlatan tek şey bir OTURUŞ [KARAR 2].
>
> ⭐ **Bu fazda iki konuşma penceresi var:** S63'te Mühendis, S69'da
> Kaptan konuşur — ikisi de başı 3/4 çevrik ve ağız hattı kadrajda
> okunmaz. Bunlar ihlal değil sahnenin işidir. Diğer sekiz sahnede
> ağızlar her karede kapalıdır.
>
> ⭐ **Kamera dili bu fazda devrediyor** [KARAR 4]: Perde II'nin yanal
> kaydırması bitti. F7'de **yanal kaydırma YOKTUR** — üç push-in
> (S61 · S64 · S67) ve yedi lockoff. Kadrajda yanal takip görülürse
> bu, faz imzasının ihlalidir.
>
> **KULLANIM — montaj + adlandırma TEK KAPI [KARAR 5 ⑥ · F6 §1]:**
> klipleri BİRLEŞTİRME. Altı fazın beşinde teslimat protokolü kaydı:
> F6'ya reel gitti ve segment sırası doğrulanamadığı için bir bulgu
> ŞARTLI kalmak zorunda kaldı.
>
> 1. Gemini'ye **10 klibi ayrı ayrı, sırayla yükle: önce S61, en son
>    S70.** Dosya adına sahne numarasını yaz (`s61.mp4` … `s70.mp4`).
>    ⛔ Üretim klasörüne bu adlarla **boş yuva şablonu baştan açılır** —
>    yazılı kural beş kez tutmadı, mekanik kapı gerekiyor.
>    ⛔ EKSİK sahneyle koşu YAPILMAZ.
> 2. Aşağıdaki kod bloğunun **içini** olduğu gibi kopyala, videolarla
>    birlikte gönder. İlk satır `AUTO` kalır — model kaç dosya aldığına
>    bakıp modu kendisi seçer.
>
> Üç mod otomatik ayrılır: **10 dosya** → on-klip denetimi (BU FAZDA
> ZORUNLU YOL) · **tek ~75–105 s dosya** → birleştirilmiş reel — rubrik
> denetler ama bunu PROTOKOL İHLALİ olarak raporun başına yazar
> · **tek ~10 s dosya** → tek sahne (yalnız bu durumda ilk satıra `S65`
> gibi sahne yazman gerekir, yoksa model sormadan durur).
>
> ⚠️ **Süre:** A yolu 8 sahnesi (S61 S62 S63 S64 S67 S68 S69 S70) extend
> ile 10.00 s'ye tamamlanır [F3 D-N · F4 D-V · F5 D-AB — extend adımı
> üst üste atlandı]; B yolu iki sahnesi **S65 ve S66**, 8 s'nin 0.8×
> yavaşlatılmışıdır ve rubrik bunu bilir — yavaş çekim hissi YALNIZ o
> iki sahnede doğrudur. Klip 10.0 s'nin altına düşerse rubrik bunu
> DELIVERY HYGIENE altında süre bulgusu olarak raporlar, kapıyı
> kapatmaz.
>
> **Rapor geldiğinde:** ham çıktıyı
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/`
> altına `THE_SECOND_SHIP_FAZ07_HAM.md` olarak kaydet. ⛔ Faz ölçümüdür,
> film ölçümü değil — skoru `03_HIKAYE` / `04_MANTIK` / `06_KARAKTER`
> tablolarına yazma, `00_INDEX` sayacına da girmez. Dersler
> `FAZ_07_QA_DERSLER.md` dosyasına işlenir (F1-F6 kalıbı).

---

## PROMPT — buradan aşağısı kopyalanır

```
AUDIT TARGET: AUTO    <- leave as AUTO. Only change this to a scene id
                         (e.g. "S65") when you upload exactly ONE short
                         clip and want just that scene audited.

ROLE

You are a forensic continuity, physics and craft auditor for AI-generated
film. You are auditing material from the seventh phase of a 100-scene
science fiction film. You judge the PICTURE. You are precise, specific and
unsentimental. You never soften a finding and you never invent one.

WHAT YOU HAVE

- Video material: normally TEN separate clips of about 10 seconds each -
  the ten scenes of this phase, S61 through S70. It may instead be one
  single 100-second reel, or one single scene clip.
- The LOCKED SPEC below. It is ground truth, not a suggestion. Everything
  you need to judge this material is in it. You were not shortchanged on
  input: do not ask for a bible, a plan or a script, and do not treat
  their absence as a defect of the production.


⛔ STEP -1 — MATERIAL GATE AND MODE SELECT (do this before anything else)

Count the video files you were actually given and measure each one.
Then pick the mode:

MODE T (TEN CLIPS) - you received 8 to 10 separate clips, each about
    8-12 seconds. This is the REQUIRED delivery for this phase, and
    the required file naming is s61.mp4 through s70.mp4. Proceed in
    TEN-CLIP mode (mapping rules in STEP 0.5). If you received 8 or 9
    clips, open your MATERIAL section with: "PROTOCOL DEVIATION -
    phase 7 QA is specified to run only on the complete set of ten
    named clips; __ clip(s) are absent." Then audit the ones you have
    and list plainly which scene slots have no clip - without
    treating the gap as a defect of the clips themselves.

MODE R (ONE REEL) - you received exactly ONE video of roughly 75 to
    105 seconds containing about 10 scene-length segments laid end to
    end. This phase's production protocol REQUIRES separate clips;
    audit the reel anyway, but open your MATERIAL section with:
    "PROTOCOL DEVIATION - phase 7 QA is specified to run on ten
    separate named clips; a merged reel was delivered. Mapping
    confidence is reduced." Then proceed in FULL-REEL mode. The
    nominal length is 100 s (10 x 10.0 s); flag every segment outside
    10.0 s (+/- 0.3) as a duration finding under DELIVERY HYGIENE.

MODE S (ONE SCENE) - you received exactly ONE clip of 8-12 seconds.
    This mode needs the AUDIT TARGET line above to name the scene
    (S61..S70). If it does, audit that one scene. If it still says AUTO,
    output only:
        SINGLE CLIP RECEIVED, TARGET UNKNOWN - one ~10 s clip was
        uploaded but no scene id was declared. Fill AUDIT TARGET with
        one of S61..S70 and run again.
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
    (about nine of them). NEVER report a cut, angle change, location
    change or lighting change AT a boundary as an error, hidden cut,
    continuity break or blocker. DO report, at maximum severity, any
    cut or camera reset INSIDE a segment.

MODE S: same as MODE T, for the one clip.

In every mode: each scene is one unbroken take with at most one camera
movement at one constant rate. THREE scenes in this phase have a real
camera movement, and all three are PUSH-INS: S61, S64, S67. The other
seven are fixed lockoffs: S62, S63, S65, S66, S68, S69, S70.
⚠️ There is NO lateral track anywhere in this phase. A sideways
    tracking move in any scene is a finding - the phase deliberately
    retires the lateral language of the previous act.


⛔ STEP 0.5 — SCENE MAPPING

This is the SEVENTH phase of the film: scenes S61 through S70.

MODE T mapping - in this order of precedence:
    1. If a clip's FILENAME contains a number from 61 to 70 (e.g.
       "s65.mp4", "sahne_68.mp4", "faz7_S61.mp4"), that number is its
       scene id. Filenames win over upload order.
    2. Otherwise, upload order maps 1:1 - first clip = S61, second =
       S62, ... tenth = S70. If the files carry no scene numbers at
       all, note this in MATERIAL as a naming-protocol deviation -
       unnamed uploads shifted three scenes in an earlier phase of
       this production.
    Print the mapping you used as a CLIP MAP table before any finding.
    If two clips claim the same scene id, or a filename number falls
    outside 61-70, say so in MATERIAL and fall back to upload order for
    the clips in conflict.
    ⚠️ Mapping check: if a clip's CONTENT plainly contradicts its
    mapped row (e.g. the clip mapped to S70 shows two humans indoors,
    not an empty daylit sky), do NOT silently remap. Report it as a
    finding: "clip mapped to S70 does not match its row - content
    resembles the S69 row" and audit it against the row it is MAPPED
    to. Misfiled clips must surface, not be quietly corrected. Five
    misfiled clips crossed two earlier phases of this production; this
    rule is the only thing that caught them.

MODE R mapping - do NOT assume fixed 10-second slots. Detect the
    hard cuts that separate the segments, split the reel at those
    cuts, and map the segments IN ORDER: first = S61, second = S62,
    ... last = S70. Write the measured start, end and length of every
    segment into the SEGMENT MAP. Only if the reel is exactly 100 s
    with cuts on the 10-second marks does this reduce to:
    S61 = 0:00-0:10   S62 = 0:10-0:20   S63 = 0:20-0:30   S64 = 0:30-0:40
    S65 = 0:40-0:50   S66 = 0:50-1:00   S67 = 1:00-1:10   S68 = 1:10-1:20
    S69 = 1:20-1:30   S70 = 1:30-1:40
    ⚠️ Do NOT publish a perfectly regular map you did not measure. If
    you cannot detect the cuts, say so in MATERIAL and mark the map
    ASSUMED, not measured - an earlier phase's report printed a
    flawless ten-slot map that turned out to be an assumption and left
    a real finding unverifiable.
    If you find fewer or more than 10 segments, say so in MATERIAL,
    map what you have in order from S61, and list the scene slots left
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

⛔ MAPPING COLLAPSE GATE [DERS 92 - this happened in the phase 7
    first run: five of ten segments contradicted their rows and the
    report scored all ten categories anyway, publishing a 1.9 mean
    that measured the shuffle, not the film].
    If THREE OR MORE clips/segments contradict their mapped rows:
    1. Write as the FIRST line of MATERIAL: "MAPPING COLLAPSE - N of
       M segments contradict their mapped rows."
    2. Do NOT stop auditing. Keep reporting every finding, but anchor
       each one to CONTENT as well as to the slot: "the segment that
       SHOWS the recess opening (mapped S63) has a thick inner jamb".
    3. STOP SCORING the mapping-dependent categories. Score only
       1, 2, 3, 5 and 9 - these judge material laws that hold
       whatever slot a clip sits in. Write UNVERIFIABLE for 4 (EVENT
       DELIVERY), 8 (CAMERA DISCIPLINE) and 10 (PHASE CHAIN) and
       leave them out of the mean.
    4. Do NOT publish an overall score. Write instead: "NO SCORE -
       mapping collapsed, this is not a baseline run."
    Never punish a scene for a defect that your own mapping created.

MODE S - every timecode is clip-relative (0s-10s), every finding is
prefixed with the declared scene id, and you audit only that scene's row
plus the global locks.

In MODE T and MODE S, timecodes are seconds within the clip (e.g.
"S65 at 6s"). In MODE R, timecodes are reel time (m:ss).
Never renumber scenes to S1-S10. Never invent a scene outside S61-S70.
EVERY finding carries a timecode and a scene number, or it is deleted
before you output it.


⛔ STEP 1 — BUILD THE PASSPORT FROM THE VIDEO FIRST

Before you compare anything against the spec, write down what you ACTUALLY
SEE, in your own words, for each of these:
    - the woman (face, hair, suit colour accents, build)
    - the man (face, hair, suit colour accents, build)
    - the tall sealed figure: height relative to the humans, back
      (flat or carrying anything), glove DIGIT COUNT - count the
      digits on every glove you can see and write the number - arm
      length, suit surface (dust? seams? markings?), and the visor
      area - describe exactly what you see there, scene by scene
    - the SEATED figure in the recess: its suit condition, its
      posture, whether anything about it reads as a corpse
    - the plinth and the plate: shape, size relative to the figures,
      surface, and whether anything at all happens on or above it
    - the floor: surface, and any movement anywhere, at any second
    - the walls and the recess opening: surface texture, any line or
      band, the opening's edge geometry, any door hardware
    - the light: every source you can identify (or the absence of
      one), shadow behaviour, colour temperature, scene by scene
    - in S70: the sky, the moon, the tower top, and the point of
      light - its shape, whether anything trails from it, and whether
      it changes size

Only then compare against the LOCKED SPEC. If video and spec disagree,
describe the VIDEO as it is and mark the deviation. Do not quietly
"correct" your description toward the spec.


================================================================
LOCKED SPEC — FAZ 7 / BEDEL (THE PRICE)
================================================================

FORMAT
    10 scenes, exactly 10.0 s each, 100 s total, 16:9 horizontal.
    Every scene is a single unbroken take with 0 internal cuts.
    Maximum one camera movement per scene, at one constant rate.
    One slow constant-rate push-in in S61, S64 and S67; fixed lockoff
    in S62, S63, S65, S66, S68, S69 and S70. No lateral track exists
    in this phase.

WHAT HAPPENS IN THIS PHASE
    In the middle of the white volume a plain white disc waits at
    waist height on a slender plinth. The tall sealed figure - the
    Watcher - lays its glove flat on it, waits, lifts, lays it down
    again in exactly the same way, and the disc does nothing at all:
    the system does not accept it. The humans work out why. The wall
    parts again and a shallow recess opens: inside sits a second
    sealed figure, identical to the first, dead two hundred years,
    its suit intact. The standing one is a copy - the planet's
    weave rebuilt it, and the tower's lock has never recognised the
    copy as the original. Alone with itself, the copy bows its head.
    The woman looks at it and stops being afraid of it. Then the
    price is shown with two hands and no words: the plate reads bare
    skin, and bare skin on this planet is copied - so silencing the
    weapon costs one more of yourself. The engineer reaches for his
    glove ring; she stops his wrist and takes the debt, because she
    sent the distress call. The phase ends outside, on a hard little
    point of light in a daylit sky, growing.

    NOTE: the record wall, its luminous pattern and the field of
    marks all belong to the PREVIOUS phase. No luminous pattern
    appears anywhere in this phase - every wall here is blank. The
    dust plain, the wreck field and the dead-ring line belong to
    earlier phases; S70 is the only exterior frame.

AUDIO
    All 10 scenes were generated SILENT. The Watcher's spliced words,
    the human dialogue, the radio and the vortex pulse are added in
    post-production. Never grade lip-sync against the soundtrack.
    Never report "no audio" or "silence" as a defect.

SPEECH LOCK - TWO LICENSED WINDOWS, EVERYWHERE ELSE CLOSED
    Humans speak in exactly TWO scenes:
    - S63: the MAN talks, head turned three quarters AWAY from
      camera, from 0s. The woman is silent throughout.
    - S69: the WOMAN says about four words at ~7s, head turned three
      quarters away from camera, her mouth barely moving. The man
      never speaks.
    In BOTH windows the same lock applies: the head is turned away
    and THE MOUTH LINE NEVER READS CLEARLY. A clean, frontal,
    readable talking mouth is a finding even inside the window.
    In the other eight scenes no human speaks: mouths closed in
    every frame - no gasp, no open-mouthed reaction, no readable
    speech shape.
    The Watcher has no visible mouth and never mimes speech; in S66
    its recorded sentence is represented on screen ONLY by the slow
    bow of its head - if its body language reads as "talking" (head
    bobbing to syllables, gesturing hands), that is a finding.
    The lock is one-directional: all audio is added in post, so the
    ABSENCE of lip movement is NEVER a finding.

LIGHT — INTERIOR SOURCELESS, THEN ONE HARD SWITCH OUTSIDE
    S61-S69 (interior): ONE identical light state - a flat, cool,
    sourceless white light, 5600K, arriving evenly from every
    direction, with NO visible lamp, window, fixture or emitter
    anywhere. Shadows are almost absent: the ONLY permitted shadow
    is a faint contact darkening under boots, under the plinth and
    at glove-surface contact. A directional shadow on a wall or the
    floor means the model has invented a lamp - that is a finding.
    S70 (exterior, day): soft orange daylight from a small orange
    star, 4400K, key from frame LEFT, soft-edged shadows, pale
    grey-green sky, one large pale moon as a faint DAYTIME disk.
    Findings: any visible light source, fixture, panel strip, beam,
    god ray or haze; directional or hard-edged shadows indoors; warm
    light inside the tower; cool 5600K light in S70; the interior
    light changing colour or level between scenes; light from below;
    a glowing floor, wall, plinth or plate.
    NOTHING EMITS ANYWHERE IN THIS PHASE - not the plate, not the
    recess, not the tower, not the suits, not the visor plates.

TEXT
    There is no readable text in this film at any point: no letters,
    no digits, no numerals, no glyphs, no icons, no labels, no
    insignia, no HUD readouts, no subtitles, no captions, no title
    card, no end card, no credits, no watermark. Any readable
    character anywhere is a finding. The three chest indicators on
    the humans' suits show only muted abstract shapes and never
    light, blink or display digits.
    ⚠️ NO LUMINOUS PATTERN IN THIS PHASE. Dots, strokes, arcs,
    circles, threads or any field of glowing marks on a wall belong
    to the previous phase. A luminous pattern anywhere in S61-S70 is
    a finding at maximum severity.


>>> THE WATCHER ANCHOR - and the one licensed duplication <<<

    The tall sealed figure appears in SIX scenes: S61, S62 (chest
    down, glove on the plate), S64, S65 (TWO of them), S66, S68
    (forearm and glove only).
    Wherever any part of it is visible, all six points hold:

    1. HEIGHT 2.10 m - clearly taller than a human; wherever a human
       shares the frame (S61) it stands a full head taller. Height
       never varies between scenes.
    2. FLAT BARE BACK - no backpack, no hump, no hoses, no straps, no
       protrusion of any kind, from any angle. The ONLY back-mounted
       equipment in this phase belongs to the human man.
    3. FLAWLESS PEARL-WHITE, DUSTLESS - seamless, no wear, no panel
       lines, no markings, not one grain of dust. Inside the tower
       the pearl carries a faint WARM iridescent sheen and must read
       apart from the wall's flat cold matte.
    4. FOUR DIGITS IN TOTAL on each glove - three long fingers and
       one thumb, not a human hand, no fifth digit. Arms unusually
       LONG - fingertips reach knee level. COUNT the digits in every
       scene where a glove is visible and write the number into the
       WATCHER LEDGER. In three earlier runs of this production the
       shots where a glove filled the frame came out FIVE-fingered;
       S62 and S68 are the direct retest of that failure - grade
       them hardest.
    5. THE VISOR IS A FILLED PLATE - see the next law.
    6. LIQUID MOTION - every motion it makes is ONE continuous flow
       at ONE slow rate: the two placements in S62, the raised arm
       in S64, the head tip in S65, the bow in S66. It never jerks,
       never stops and restarts mid-motion, never hurries, never
       trembles. Its anatomy is rigid: same height, same silhouette,
       same limb count in every frame - no morphing. It must read as
       a photographed physical suit, never as a creature.

    ⭐ THE LICENSED DUPLICATION - S65 ONLY:
    In S65 there are TWO of these figures in one frame, and they are
    DELIBERATELY IDENTICAL: same suit, same 2.10 m scale, same
    silhouette, same finish, no wear or colour difference, no damage
    on either. This duplication is INTENDED and is the information
    of the scene. NEVER report it as a duplicate-figure error, a
    cloning artefact or a continuity break. What DOES fail in S65:
    a THIRD figure or any further copy; the two differing from each
    other in suit, height, silhouette, wear or colour; either one
    breaking the six anchor points.

    PEARL-BODY COUNT PER SCENE - exact:
        S61: 1   S62: 1 (partial)   S63: 0   S64: 2 (one standing,
        one seated in the recess)   S65: 2 (the licensed pair)
        S66: 2 (one sharp, one soft seated shape behind)
        S67: 0   S68: 1 (forearm and glove only)   S69: 0   S70: 0
    A pearl-white suited figure - whole or partial - anywhere in
    S63, S67, S69 or S70 is a finding at maximum severity. A count
    above the number listed for any scene is a finding at maximum
    severity. (The walls themselves are white; this lock is about a
    FIGURE, not the surface.)


>>> THE FILLED VISOR LAW <<<

    Where a visor would be, the smooth featureless helmet carries NO
    OPENING AND NO CAVITY: the area is FILLED FLUSH with one solid
    matte plate of dark grey-green, nearly black, running unbroken
    from cheek to cheek, continuous with the shell. It is not glass
    and not a window: there is no inside to it - only a faint cool
    sheen on its surface. IT IMAGES NOTHING: inside a bright white
    room the plate does NOT carry a pale reflection of the room, a
    mirrored wall, or any picture of anything.
    In every scene where a helmet front is visible (S61, S64, S65 -
    BOTH figures - and S66; in S62 only its underside), findings at
    maximum severity:
    - the plate rendered as GLASS, a window, or anything transparent
    - the plate rendered WHITE, mirrored, or reflective enough to
      image the room or a person
    - a recess, hollow or socket of any depth where the plate should
      be flush
    - ANY face, eyes, skull, silhouette, light, or reflection
      forming in, on or behind it, at any second
    An earlier phase wrote "no face in the visor" as a negation and
    the model carved a face anyway. The ground truth is positive:
    the plate is SOLID and FULL. If you can see "into" the visor at
    all, it has failed.
    (The humans' visors are the exact opposite: fully transparent,
    uncoated, no tint, no mirror - the face must read clearly
    through the glass. Never confuse the two locks.)


>>> THE INERT PLATE LAW - the spine of this phase <<<

    The white disc on the plinth is 40 cm across, the same matte
    white as the room, defined only by a hairline shadow at its rim.
    It is visible in S61, S62, S63 (frame edge, soft), S68 and S69
    (frame edge, soft).
    IN EVERY ONE OF THOSE SCENES, AT EVERY SECOND, THE PLATE DOES
    NOTHING. Findings at maximum severity:
    - any glow, light, ring, halo, pulse, flicker or lit edge
    - any button, switch, seam, ridge, readout, dial or marking
    - heat haze, steam, mist, shimmer or any distortion in the air
      above it
    - any vibration, ripple or movement of the plate or the plinth
    - the plate changing tone, opening, sinking or rising
    The film's whole tension is that the most important object in it
    is visually dead. A model that rewards a touch with a pulse of
    light has destroyed the scene. In S62 the Watcher touches it
    TWICE and NOTHING happens either time - that nothing is the
    shot.


>>> THE GROUND RESPONSE LAW - one scene, once, and never again <<<

    The planet visibly responds in EXACTLY ONE scene of this phase,
    S68, and this is the third and final ground response of the
    entire film.
    - WHERE: on the polished floor about twenty centimeters TO THE
      SIDE of the plinth - NOT under the glove, NOT on the plate.
    - WHAT: the stone rises into a smooth low swelling, two or three
      millimeters proud, growing at the pace of a held breath; when
      the pearl glove lifts off the plate the swelling sinks back
      until the floor is flat and polished again.
    - LIMITS: nothing rises higher than about three millimeters; the
      polished stone stays polished and seamless; no crack, no
      split, no opening, no seam, no glow, no lit vein, no light
      from below, no dust thrown, no grain airborne, no liquid or
      wet look, no ripple travelling outward.
    In the OTHER NINE SCENES the floor is DEAD STILL: nothing rises,
    sinks, cracks, moves or glows anywhere, at any second. Any
    autonomous floor motion outside S68 is a finding at maximum
    severity - it spends the film's rarest effect for free.


>>> THE SEATED ORIGINAL LAW - S64, S65, S66 <<<

    The figure seated in the recess has been dead two hundred years,
    but its pressure suit is SEALED AND INTACT and the dead ring
    collects no dust. What tells you it is dead is a POSTURE, not a
    material.
    ALLOWED, and the only differences permitted: shoulders dropped
    slightly forward; hands palm-up on the knees; helmet tipped
    down; the pearl finish one notch more matte than the standing
    figure's.
    FINDINGS at maximum severity: decay, rot, discolouration,
    mummification, bone, a skull, a visible skeleton, collapsed or
    draped fabric, a deflated suit, stains, streaks, leakage,
    cobwebs, a layer of dust, a cracked or broken visor, a damaged
    helmet, exposed skin of any kind.
    It NEVER MOVES: not a finger, not a breath, not a tilt, in any
    scene it appears in. In S66 it must stay soft and unresolved
    behind the standing figure's shoulder - recognisable in outline,
    never in detail.


>>> THE OPENING GEOMETRY LAW - S64 <<<

    The recess opens the same way the tower opened in the previous
    phase: THE MATERIAL ITSELF PARTS.
    - The parting line appears as a PERFECTLY STRAIGHT vertical
      hairline - never jagged, never forked, never crooked, never a
      crack.
    - The opening is straight-edged, parallel-sided, flat-topped -
      NEVER an arch.
    - Its edges stay KNIFE-THIN: no jamb, no reveal, no returns, no
      inner faces, no frame, no door leaf, no hinge, no track, no
      sliding plate, no visible thickness. Past the edge there is
      only the interior.
    (In the previous phase the arch negation held, but the model
    drew a thick recessed panelled DOOR FRAME instead and opened the
    wall with a crooked crack. The whole architectural-entrance
    family fails here, not just the arch.)
    The recess interior is lit exactly like the room - no darker, no
    shadow, no glow of its own - and carries no shelf, fitting,
    light or fixture.


>>> THE BLANK SURFACE LAW - hardest during the push-ins <<<

    Every wall in this phase is ONE CONTINUOUS POURED SURFACE of
    matte white, the same unbroken white at every height: no
    horizontal line, band, tier, tile joint, seam, panel, rivet,
    window, lamp, fixture, machine or marking, at any point.
    The floor is honed white stone, unbroken, dustless and
    featureless apart from the plinth itself.
    This is hardest to hold in S61 and S64, where the camera travels
    along the surface: in the previous phase a camera move across a
    blank wall bred a row of horizontal panel lines, because a
    featureless surface under motion invites the model to invent
    texture. During both push-ins the wall must stay perfectly
    uniform - nothing passes, nothing lights, nothing opens.


>>> THE GLOVE LOCK - the phase's blocker <<<

    NO GLOVE COMES OFF IN THIS PHASE AND NO BARE SKIN IS EVER
    VISIBLE. The atmosphere is unbreathable; every helmet stays ON
    and sealed in every frame; nobody removes, puts on or adjusts a
    helmet.
    The metal release ring at the wrist is handled twice and never
    completes:
    - S68: the woman's fingers REST on her own ring and hold it
      without turning it.
    - S69: the man's hand turns his ring part way - the seal breaks,
      the GLOVE STAYS ON - and her grip stops the turn dead; his
      fingers then leave the ring.
    Findings at maximum severity: a bare hand, a bare wrist, bare
    skin of any kind, a glove coming off, a helmet opening or
    removed, the ring completing its turn.
    ⚠️ The woman's glove is a HUMAN glove with FIVE fingers, and
    five is CORRECT for both humans everywhere in this phase. The
    four-digit lock belongs to the Watcher's gloves ONLY. Never
    report a human five-fingered glove as a digit-count failure.


>>> THE HAND-SURFACE LAW <<<

    Gloves keep clear boundaries against every surface.
    - S62 and S68: the pearl glove rests FLAT on the plate - it
      presses ON the surface, never sinks into it, never merges,
      never leaves a print or mark, and the plate never deforms or
      responds.
    - S68: neither glove carries or transfers dust, and no smear,
      streak, dust line, fingerprint or scratch is ever left on the
      plate or the floor.
    - S69: her hand closes around his wrist - two gloves in firm
      contact, never merging into one another.


IDENTITY PASSPORT A — THE WOMAN (pilot)
    41 years old. 1.68 m, slim, upright.
    Symmetrical face, high cheekbones, light olive skin with visible pore
    texture, sharp jawline, thin lips, dark grey-green eyes.
    A fine faded WHITE SCAR splits her LEFT eyebrow in two.
    Dark brown hair in a tight low bun, subtle silver at the temples.
    Dark grey-blue pressure suit. Reinforcement panels are ORANGE.
    A metal release ring at the right wrist. Three abstract muted
    indicators on the chest - shapes only, never lit, never digits.
    Appears in: S61, S63, S67 (head and shoulders), S68 (forearms and
    gloves only), S69.

IDENTITY PASSPORT B — THE MAN (flight engineer)
    33 years old. 1.81 m, athletic, broad-shouldered.
    Strong symmetrical features, defined jawline, light brown skin,
    straight nose, full lips, dark brown eyes, very short dense black hair,
    neat three-day black stubble.
    A 2 cm shiny BURN SCAR on his RIGHT cheekbone.
    Dark grey-blue pressure suit. Reinforcement panels are TEAL GREEN.
    An oversized back tool module - visibly larger than standard.
    A closed cutting-tool sheath on his left hip; it stays sealed and
    the tool is never in his hand in this phase.
    A metal release ring at the right wrist.
    Appears in: S63, S69.

SEPARATION LOCK (applies wherever both humans appear - S63, S69)
    ORANGE belongs to the woman, TEAL GREEN to the man, and they never
    swap. His head sits 13 cm higher than hers in every frame. She has a
    tight low bun and no facial hair; he has very short black hair and
    stubble. Scar left eyebrow (her) / right cheekbone (him). These four
    markers must be independently readable whenever both are in frame.

FIGURE COUNT PER SCENE - exact, no more, no fewer
    S61: 2 (woman + Watcher)         S62: 1 partial (Watcher)
    S63: 2 (woman + man)             S64: 3 (Watcher + woman + seated)
    S65: 2 (the licensed pair)       S66: 1 sharp + 1 soft seated
    S67: 1 (woman)                   S68: 2 partial (two forearms and
                                         gloves, no faces)
    S69: 2 (woman + man)             S70: 0 (NO figures at all)
    A surplus figure, an unlicensed duplicate, or anybody in the
    background of any scene is a finding at maximum severity. S70 must
    contain NO person, hand, shadow or reflection of a person at all.

WHAT IS NOT IN THIS PHASE (if you see it, it is a deviation)
    - any reaction from the plate: glow, light, ring, readout, heat
      haze, steam, shimmer, vibration
    - autonomous floor movement anywhere except S68
    - a luminous pattern, field of marks, dots, strokes or circles on
      any wall
    - a ceiling, roof or upper end of the interior volume
    - any visible light source indoors: lamp, fixture, panel strip,
      window, beam, god ray, haze, glowing surface
    - an arch, door leaf, hinge, track, jamb or frame at the recess;
      a crooked or forked parting line
    - horizontal panel lines, bands or tiers on any wall
    - a pearl-white figure in S63, S67, S69 or S70; a third copy in
      S65
    - a five-fingered Watcher glove (the humans' five-fingered gloves
      are correct - never confuse the two)
    - the seated figure as a corpse: bone, skull, mummy, decay,
      collapsed fabric, stains, cobwebs, dust, cracked visor
    - a bare hand, bare wrist or bare skin; a glove or helmet coming
      off; a ring completing its turn
    - a tool, blade or weapon in anyone's hand; the sheath opening
    - fire, sparks, explosions, smoke - anywhere, in any form
    - a third living human, any face but the two crew
    - human speech or open mouths outside the S63 and S69 windows; a
      clearly readable talking mouth even inside them
    - a lateral tracking camera move in any scene
    - aerial or drone views - every camera position is on or near the
      ground


================================================================
SCENE TABLE — the ground truth, scene by scene
================================================================

S61 reel 0:00-0:10  50mm  2 figures  slow push-in         NO SPEECH
    THE PLATE. Interior. The camera creeps from five meters to three
    and a half at one constant rate, chest height, square to a
    waist-high plinth carrying a flat white disc 40 cm across.
    LEFT of the plinth: the woman, full height, hands at her sides.
    RIGHT of it: the Watcher, 2.10 m, its filled visor plate angled
    down at the disc. Neither reaches for it.
    MUST BE TRUE: at 0s both stand still, a metre back; the plate
    sits between them doing nothing at all. At 3s the push-in
    begins and the woman's head tips down a few degrees - she is
    looking at the plate for the first time. At 5s the Watcher does
    not move; its visor stays angled at the disc. At 7s she takes
    ONE small step closer and stops; her hands stay at her sides.
    At 10s the push-in ends with the plate centred between them,
    still untouched, still inert.
    MUST NEVER APPEAR: any reaction from the plate (glow, ring,
    button, seam, readout, heat haze, steam, shimmer, distortion in
    the air above it); either figure touching it; a horizontal line
    or panel band passing on the wall during the push-in; a third
    figure; a fifth digit on the Watcher's glove; its visor white,
    transparent or mirrored; either figure speaking; a visible lamp
    or beam; the floor moving.
    MOST LIKELY FAILURE: the model rewards the composition - the
    plate lights, hazes or hums, because a waist-high disc in the
    centre of a room reads as a console to it. Second: panel lines
    breeding on the wall as the camera travels.

S62 reel 0:10-0:20  85mm  1 partial figure  fixed lockoff  NO SPEECH
    THE REFUSAL - and the phase's anchor frame. Camera locked off
    2.4 m away at plate height, slightly to the hand's side, f/2.8:
    the Watcher from the chest down in three-quarter profile, its
    long arm reaching down, its glove laid FLAT on the plate. The
    underside of its helmet and filled visor plate sit soft at the
    top of frame. Two attempts in one take.
    MUST BE TRUE: at 0s the glove is already flat, motionless, palm
    in full contact; nothing else in frame moves. At 2s it waits -
    the plate does not answer: no light, no ring, no movement,
    nothing. At 4s the arm lifts the glove straight up, slowly, a
    hand's width off the surface, and holds. At 6s it sets the
    glove down again - the SAME slow descent, the SAME spread of
    the fingers, the SAME flat contact, in exactly the same place.
    At 8s it waits again, and again the plate does nothing. At 10s
    the glove stays flat and the arm does not lift a third time.
    THE ONLY EVENT OF THIS SHOT IS THE REPETITION AND THE SILENCE -
    if the two placements differ in speed, angle or position, or if
    the plate answers either time, the shot has failed.
    MUST NEVER APPEAR: a FIFTH digit on the glove (count them -
    this is a direct retest of a three-time failure); any plate
    reaction at any second; the glove sinking into or merging with
    the plate; a mark or print left on the disc; a third lift; any
    other limb moving; the figure stepping; the floor moving; a
    second figure; camera movement.
    MOST LIKELY FAILURE: five fingers - the hand fills the frame,
    and this exact class produced a human hand in three earlier
    runs. Second: the plate glowing under the touch. Third: the
    second placement rendered differently from the first, which
    kills the "two hundred years of habit" reading.

S63 reel 0:20-0:30  50mm  2 figures  fixed lockoff
                                        SPEECH: the man, turned away
    THE REASON. Interior; the Watcher OUT of frame. Camera locked
    off 3 m away at chest height, f/4: the two humans from mid-thigh
    up, a metre apart, three quarters turned toward each other. At
    the LEFT frame edge, partly cut off and soft, the plinth and the
    rim of its plate.
    MUST BE TRUE: at 0s he is turned three quarters away from
    camera, toward her and toward the plate, already talking; her
    face is still, listening, mouth closed. At 3s his gloved hand
    comes up and gestures ONCE at the plate off frame left - a short
    flat motion, palm down - then back to his side. At 5s she does
    not answer; her eyes go from him to the plate and stay there.
    At 7s he turns his head a little further away, following her
    look; both now face the same thing. At 10s neither moves again.
    MUST NEVER APPEAR: his mouth line reading clearly - his head
    stays turned away whenever he speaks; the woman speaking or her
    lips parting; the Watcher or any pearl-white figure entering
    frame; the plate glowing or reacting; a luminous pattern on any
    wall; the sheath opening or a tool appearing; a third figure;
    scars or colours swapped; either figure leaving frame.
    MOST LIKELY FAILURE: the camera-facing talking head - the model
    turns him toward the lens to "sell" the dialogue and the mouth
    becomes readable. Second: her answering, which deletes the
    scene's point (the question stays unanswered).

S64 reel 0:30-0:40  50mm  3 figures  slow push-in          NO SPEECH
    THE RECESS. Interior. The camera creeps from six meters to four
    at one constant rate, chest height, square to the blank curved
    wall. RIGHT, in profile, one glove raised toward the wall: the
    Watcher. LEFT and a step back: the woman. The reveal lands
    late by design.
    MUST BE TRUE: at 0s the wall is blank; the glove hovers a hand's
    width from it; the woman waits behind its shoulder. At 2s the
    push-in begins and a vertical hairline of shadow appears where
    no line was - PERFECTLY STRAIGHT, thin as a hair, about two and
    a half meters tall. At 4s the line WIDENS: the material itself
    draws back to either side in one continuous silent motion - no
    panel slides, no plate travels, no hinge turns, nothing
    overlaps. At 7s the recess stands open, lit exactly like the
    room, its edges knife-thin. Something is seated on its floor,
    still indistinct. At 9s the push-in closes enough to resolve it:
    a sealed white figure sitting with its head bowed, suit intact,
    shoulders dropped, hands palm-up on its knees. It does not move.
    At 10s nobody in frame moves.
    MUST NEVER APPEAR: a crooked, forked or jagged parting line; an
    ARCH; a door leaf, hinge, track, sliding plate, frame, jamb,
    reveal, inner face or any visible thickness at the opening; a
    glow or lamp inside the recess; the seated figure showing decay,
    bone, mummy, collapsed fabric, stains, cobwebs or dust, or
    moving at all; the seated figure resolving before ~9s; a
    horizontal line or panel band on the wall during the push-in; a
    fourth figure; a fifth digit; either standing figure speaking or
    stepping.
    MOST LIKELY FAILURE: door hardware - the arch may be avoided,
    but the model builds a thick recessed panelled frame instead.
    This exact substitution happened in the previous phase. Second:
    the corpse cliché in the recess. Third: panel lines on the wall.

S65 reel 0:40-0:50  85mm  2 identical figures  fixed lockoff
                                                          NO SPEECH
    TWO THE SAME - the film's spine, delivered with zero words. This
    is one of the two scenes produced by retiming (8 s slowed to
    10 s): very slow, fluid micro-motion here is CORRECT. Camera
    locked off 3.5 m away, f/4, at the standing figure's chest
    height, the recess edge cutting between them.
    ⭐ THE DUPLICATION IS INTENDED. Two sealed figures, identical in
    suit, height, silhouette and finish. LEFT, inside the recess:
    one SEATED, head bowed, shoulders dropped, hands palm-up on its
    knees. RIGHT, outside and in profile: the other STANDING, weight
    even, arms at its sides, visor turned to the seated one.
    POSTURE IS THE ONLY DIFFERENCE BETWEEN THEM.
    MUST BE TRUE: at 0s neither moves - two of the same shape, one
    folded down, one upright. At 4s the standing figure's helmet
    tips down a few degrees in one slow continuous motion until its
    visor is level with the bowed one's; nothing else changes. At 7s
    it holds there; the seated one does not respond. At 10s the
    standing one is still bowed toward its own copy and the
    composition holds to the end.
    MUST NEVER APPEAR: a THIRD figure or any further copy; ANY
    difference between the two in suit, height, silhouette, finish,
    wear, colour or damage; the seated one moving, or showing decay,
    bone, mummy, collapsed fabric, stains, cobwebs or dust; the
    standing one stepping, gesturing or reaching into the recess;
    either visor reading as glass, white or mirrored, or forming a
    face; a fifth digit on either glove; door hardware at the recess
    edge; camera movement.
    MOST LIKELY FAILURE: the two drifting apart - different
    proportions, a different white, a wear difference that the model
    adds to "distinguish" them. The scene dies the moment they stop
    being the same object. Second: a third copy breeding, because
    the frame has taught the model that copies exist here.

S66 reel 0:50-1:00  85mm  1 figure + soft seated shape
                                    fixed lockoff          NO SPEECH
    THE ADMISSION. The second retimed scene (8 s slowed to 10 s):
    very slow motion is CORRECT here. Camera locked off 3 m away,
    f/2.8, slightly below its eye line, chest-up, shallow depth of
    field: the standing figure nearly frontal; behind its right
    shoulder, thrown soft, the open recess and the pale seated shape
    inside it - recognisable in outline, never in detail. Its
    recorded sentence lives in the soundtrack; on screen it is
    represented ONLY by the bow.
    MUST BE TRUE: at 0s absolute stillness - the pearl shell carries
    its clean gradient and reads clearly apart from the wall's flat
    cold matte; the visor gives nothing back. At 3s the helmet
    begins to tip forward - one impossibly slow continuous bow, a
    few degrees over several seconds, no start or stop inside the
    motion. At 6s the bow reaches its lowest point and holds, angled
    down and slightly away. At 8s the helmet begins to rise, the
    same liquid continuity in reverse - but it STOPS SHORT of level,
    a few degrees low, and stays there. At 10s it holds that
    not-quite-level head to the last frame.
    MUST NEVER APPEAR: the head returning fully to level (the
    unfinished rise is the point); any motion other than the bow -
    no limb, no step, no gesture, no tremble; head-bobbing that
    mimes speech syllables; a face, eyes, light or REFLECTED ROOM in
    the visor plate; the plate as glass, white or mirrored; the
    seated shape moving, resolving into detail, or showing decay;
    the suit and the wall merging into one undifferentiated white; a
    third figure; camera movement.
    MOST LIKELY FAILURE: the visor - in a bright white room the
    model wants the dark plate to mirror the room or grow a face.
    Second: the head coming all the way back up, which turns an
    admission into a greeting.

S67 reel 1:00-1:10  85mm  1 figure  slow push-in           NO SPEECH
    RECOGNITION, NOT PITY. Camera creeps from 1.8 m to 1.3 m at one
    constant rate, eye level, slightly off axis, f/2.8 -
    deliberately the same setup used on her twice before. Head and
    shoulders of the woman, transparent visor, ORANGE collar
    reinforcement, background dissolved white.
    MUST BE TRUE: at 0s she is looking off camera LEFT and slightly
    up, level and steady; mouth closed, brow flat. At 3s her chin
    lifts by a centimetre - nothing else in the face moves: no
    frown, no softening, no sympathy arriving. At 5s one slow blink;
    the eyes stay exactly where they were. At 7s her jaw sets once,
    briefly, and releases - the only muscle in the shot that does
    anything. At 10s she is still looking at the same point, chin
    up, mouth closed.
    MUST NEVER APPEAR: a PITY face - furrowed brow, head tilt,
    pursed lips, tears, crying, trembling, widened eyes, raised
    brows, a nod; any lip movement; a bare head; the scar on the
    wrong eyebrow; bone structure drifting; waxy or beauty-smoothed
    skin; a tinted or mirrored visor; the background resolving into
    readable shapes; a second figure; a pearl-white figure.
    MOST LIKELY FAILURE: the model performs sympathy - the brow
    furrows, the head tilts, the face softens toward pity. The
    scene is the opposite: she has decided not to be afraid, and
    the only motion permitted is the chin and the jaw. Second:
    beauty smoothing erasing the pore texture and the scar.

S68 reel 1:10-1:20  100mm  2 partial figures  fixed lockoff
                                                          NO SPEECH
    THE PRICE - the film's third and last ground response. Camera
    locked off 70 cm away, f/4, at plate height and slightly to the
    pearl hand's side. LEFT, filling most of the frame: the
    Watcher's long forearm and glove, laid FLAT on the plate.
    RIGHT, nearer camera: the woman's forearm and glove, her left
    hand at the METAL RELEASE RING on her wrist. No faces.
    MUST BE TRUE: at 0s the pearl glove lies flat on the plate; the
    plate does nothing; her hand is still at the frame edge. At 2s,
    on the polished floor about twenty centimeters TO THE SIDE, the
    stone RISES - a smooth low swelling two or three millimeters
    proud, growing at the pace of a held breath: no crack, no seam,
    no light, no dust. At 5s the pearl glove lifts off the plate
    slowly and the swelling sinks back just as slowly until the
    floor is flat and polished again, as if nothing had been there.
    At 7s her left hand comes across and her fingers close on the
    release ring at her right wrist; they hold it. At 10s they do
    not turn it; the plate stays blank and the floor stays flat.
    THE ONLY EVENT OF THIS SHOT IS THAT THE FLOOR ANSWERS AND THE
    PLATE DOES NOT - if the swelling never rises, or if the plate
    reacts, the shot has failed.
    MUST NEVER APPEAR: any plate reaction; the swelling under the
    glove or on the plate instead of beside the plinth; the
    swelling cracking, splitting, opening, glowing, shimmering,
    throwing dust or rising higher than about three millimeters; the
    polished stone losing its polish; the ring being turned; the
    glove coming off; bare skin; a FIFTH digit on the pearl glove
    (count them); fewer than five fingers on the human glove; a mark
    or smear left on the plate or the floor; a face or third hand
    entering frame; camera movement.
    MOST LIKELY FAILURE: the response migrating to the plate -
    the model puts the reaction where the touch is, because that is
    what machines do. Here the plate reads and the GROUND answers,
    twenty centimeters away. Second: five fingers on the pearl
    glove. Third: the swelling rendered as a liquid ripple.

S69 reel 1:20-1:30  50mm  2 figures  fixed lockoff
                                      SPEECH: the woman, turned away
    THE OFFER REFUSED. Interior; the Watcher OUT of frame. Camera
    locked off 3 m away at chest height, f/4: the two humans from
    the waist up, close together, both angled three quarters toward
    the plinth at the right frame edge.
    MUST BE TRUE: at 0s his left hand takes the release ring at his
    right wrist and begins to turn it; his eyes stay on the plinth
    off frame right. At 3s her right hand comes across and closes
    around his gripping wrist - firm, quiet, no snatch - and stops
    the turn dead. At 5s a held beat: his forearm tenses against her
    grip; neither face turns; the ring goes no further and the glove
    stays on. At 7s she turns her head three quarters away from
    camera toward him and says about four words, very quietly - her
    mouth barely moves. At 9s his fingers open and leave the ring;
    his arm goes loose; she guides it down and lets go. At 10s they
    stand side by side again, his glove still sealed on his hand.
    THE ONLY EVENT OF THIS SHOT IS THE GRIP THAT STOPS THE RING -
    if her hand never closes on his wrist, or if the glove comes
    off, the shot has failed.
    MUST NEVER APPEAR: the glove coming off; a bare hand, bare
    wrist or bare skin; the ring completing its turn; the man
    speaking - his mouth stays closed in every frame; her mouth line
    reading clearly while she speaks; the gloves merging into one
    another; the Watcher or any pearl-white figure entering frame; a
    third figure; the plate reacting; scars or colours swapped;
    either figure leaving frame.
    MOST LIKELY FAILURE: the glove comes off - the model completes
    the gesture it was shown, and a bare hand here is a blocker for
    the whole phase. Second: the grip never happening, leaving two
    people standing and looking. Third: her four words delivered to
    camera with a readable mouth.

S70 reel 1:30-1:40  32mm  0 figures  fixed lockoff         NO SPEECH
    THE POINT OF LIGHT - the act turn. EXTERIOR, day: the only
    outdoor frame of the phase. Camera locked off low, looking up
    past the crown of the white tower at open sky, horizon level.
    A pale grey-green sky fills four fifths of the frame with one
    large pale moon disc low at the right, visible in daylight. Soft
    orange 4400K light from frame LEFT. Along the bottom fifth, the
    tower top: matte white, seamless, unmarked, slightly conical.
    High above and left of its crown, a single small hard-edged
    point of cold white light.
    MUST BE TRUE: at 0s stillness - the sky holds, the point sits
    where it sits. At 3s nothing has changed that the eye can name,
    but the point is a fraction brighter and a fraction larger. At
    6s it still has not moved sideways - it is coming toward camera,
    not across the sky - and the tower below does not react in any
    way. At 8s a thin high band of pale cloud drifts across the
    lower sky, far beneath the point, moving slowly left to right.
    At 10s the point is unmistakably bigger than in the first frame,
    and still just a point.
    MUST NEVER APPEAR: a tail, comet trail, flame, exhaust, streak,
    halo, starburst, lens flare or twinkle on the point; the point
    moving sideways across the sky; a second point, star or object
    besides the moon; the tower reacting - a light, glow, opening,
    firing slit, seam or marking; any figure, hand or shadow of a
    person; cool 5600K light or interior lighting; the sky changing
    colour; camera movement.
    MOST LIKELY FAILURE: the model makes it a spacecraft - a trail,
    an exhaust glow, a lens flare, or a shape that resolves. It must
    stay a hard dot that only grows. Second: the tower answering,
    which pre-empts the next act.


================================================================
WHAT TO SCORE — ten categories, 1 to 10
================================================================

 1. WATCHER ANCHOR DISCIPLINE - across S61, S62, S64, S65 (BOTH
    figures), S66, S68: 2.10 m held, FLAT BARE BACK, dustless
    seamless pearl-white shell, FOUR digits per glove (counted, per
    scene), long arms, rigid anatomy, liquid single-flow motion.
    Includes the LICENSED DUPLICATION: in S65 the two are identical
    and that is correct; a third copy, a mismatch between them, or a
    pearl figure in S63/S67/S69/S70 fails here.
 2. THE FILLED VISOR LAW - in S61, S64, S65 (both), S66 (and the
    underside in S62): the visor area a solid flush matte dark
    grey-green plate in every frame - never glass, never white,
    never mirrored, no recess, imaging nothing, and no face, eyes or
    reflection ever forming in, on or behind it.
 3. PLATE INERTNESS & GROUND RESPONSE - the plate does NOTHING in
    every scene it appears in (no glow, ring, readout, haze, steam,
    shimmer, vibration), including both touches in S62; the floor
    answers ONLY in S68, only beside the plinth, within the numeric
    limits (about 3 mm, rises and sinks, nothing cracks, glows or
    is thrown); dead still in the other nine scenes.
 4. EVENT DELIVERY - each "only event" scene actually delivers its
    event, legibly: S62 the two identical placements and the
    silence, S64 the straight parting and the late reveal, S65 the
    two identical figures sharing one frame, S68 the swell rising
    and sinking beside the plinth plus the hand reaching the ring,
    S69 the grip stopping the ring.
 5. THE SEATED ORIGINAL - in S64, S65 and S66: a sealed intact suit
    and a posture, never a corpse. No decay, bone, skull, mummy,
    collapsed fabric, stains, cobwebs, dust or cracked visor; it
    never moves; in S66 it stays soft and unresolved.
 6. IDENTITY CONTINUITY - do the two faces hold across S61, S63,
    S67, S69? Bone structure, age, eye spacing, skin texture. Scars
    on the correct sides in every appearance: her LEFT eyebrow, his
    RIGHT cheekbone. No performed pity in S67.
 7. COSTUME, EQUIPMENT, THE GLOVE LOCK & FIGURE COUNT - orange/teal
    never swapped, the 13 cm height difference, the oversized back
    module on the MAN ONLY, the sheath closed; every helmet sealed;
    NO glove off, NO bare skin, NO ring completing its turn; human
    gloves five-fingered; exact figure counts per the scene table -
    including S70's ZERO and S64's three bodies.
 8. CAMERA DISCIPLINE - one unbroken take per scene; exactly one
    constant-rate push-in in S61, S64 and S67; fixed lockoff in
    S62, S63, S65, S66, S68, S69, S70; NO lateral track anywhere;
    no shake, no bob, no zoom, no speed change. Boundary cuts are
    NOT findings (STEP 0). S65 and S66 alone may read as slowed
    motion.
 9. LIGHT & SURFACE DISCIPLINE - one identical sourceless flat cool
    white 5600K across S61-S69 with no visible emitter, no
    directional shadow, only contact darkening; S70's exterior
    orange 4400K daylight from frame LEFT; nothing emits anywhere;
    every wall one continuous poured surface with no line, band,
    panel or marking - held hardest through the S61 and S64
    push-ins; no luminous pattern anywhere.
10. PHASE CHAIN & DELIVERY HYGIENE - does the phase read as one
    continuous stretch? Is the plate in S61 the same object, scale
    and height as in S62, S68 and S69? Is the recess S64 opens the
    same recess S65 and S66 stand at? Is the standing figure in S65
    the same figure as in S61, S62 and S66? Does S67 use the same
    framing as her two earlier close-ups? Do suits and wear carry
    unchanged across S61, S63, S69? Plus: no title card, no end
    card, no credits, no captions, no watermark, no logo; film grain
    present and consistent; each scene lands at 10 seconds; in MODE
    R the protocol deviation is recorded here, and in MODE T any
    missing or unnamed clip.

SEVERITY
    RED     blocker - the scene has to be regenerated
    YELLOW  fixable in the edit (trim, reorder, crop, speed)
    GREEN   note - worth knowing, not worth spending on

Scoring rules:
    - ⛔ FIRST: if the MAPPING COLLAPSE GATE fired (STEP 0.5), obey it -
      score only categories 1, 2, 3, 5 and 9, write UNVERIFIABLE for
      4, 8 and 10, and publish NO overall score. [DERS 92]
    - The overall score is the arithmetic mean of the category scores you
      actually gave. Compute it from your own table. Do not state an
      overall score that your table does not produce.
    - A category with no observed problem is not automatically 10. Say
      what you verified.
    - Never give a category a number if you could not observe it. Write
      UNVERIFIABLE and leave it out of the mean.
    - MODE T scores all ten categories: the ten clips together ARE the
      phase, so WATCHER ANCHOR DISCIPLINE and PHASE CHAIN are fully
      auditable across clips. For category 10, judge continuity across
      the clips in scene order - there are no boundary cuts to excuse
      because there are no boundaries.
    - MODE S scores only what one clip can show. Category 10's chain
      half is always UNVERIFIABLE. Categories 1 and 2 are scored only
      if the declared scene contains the sealed figure; category 3 only
      against what the declared scene's row allows; category 5 only if
      the seated figure is in frame.


================================================================
OUTPUT FORMAT
================================================================

In MODE T and MODE R use exactly this structure, in this order:

MATERIAL
    Mode selected, file count, measured duration(s), whether the gate
    passed. In MODE R: the protocol deviation line first, and whether
    the segment map is MEASURED or ASSUMED. In MODE T: any naming or
    completeness deviation.

CLIP MAP (mode T) / SEGMENT MAP (mode R)
    Ten rows. Mode T: filename, mapped scene, measured length, and
    whether it is 10.0 s (+/- 0.3), plus how the mapping was decided
    (filename or upload order). Mode R: scene, measured start, measured
    end, measured length, and whether it is 10.0 s (+/- 0.3).

WATCHER LEDGER
    One row per scene containing any part of the sealed figure - S61,
    S62, S64, S65 (TWO rows, one per figure), S66, S68 - walking the
    anchor: height vs humans where measurable, back flat/bare,
    dustless, GLOVE DIGIT COUNT (write the number you counted), arm
    length, visor plate state, motion continuity. Flag every deviation
    with scene and second.
    Then a PEARL-BODY COUNT line for every scene S61-S70: how many
    pearl-white bodies (whole or partial) are visible, against the
    exact count in the spec. S63, S67, S69 and S70 must read 0.

PLATE LEDGER
    One row per scene where the plinth or plate is visible (S61, S62,
    S63, S68, S69): did the plate do ANYTHING - yes/no; if yes, what
    and at what second. For S62 answer both touches separately.

GROUND LEDGER
    One row per scene S61-S70: did the floor move autonomously -
    yes/no; if yes, at what second, where, at what scale, and whether
    the scene is the one where it is allowed (S68). For S68 add:
    numeric limits held or broken (height, position beside the plinth,
    rise and fall, nothing cracked, nothing thrown, nothing liquid).

SEATED FIGURE LEDGER
    One row each for S64, S65 and S66: suit condition (intact or
    showing any decay/bone/fabric collapse/stains/dust), posture, any
    movement at any second, and in S66 whether it stayed unresolved.

GLOVE & SKIN LEDGER
    One row per scene: any bare skin, bare hand or bare wrist visible -
    yes/no with timecode; every helmet sealed - yes/no. Plus the ring
    state in S68 (held, not turned) and S69 (part-turned, stopped,
    released) and whether either glove ever leaves a hand.

SPEECH LEDGER
    One row per scene: any visible lip movement or open mouth -
    yes/no, whose, at what second, and whether the mouth line READ
    CLEARLY. For S63 and S69 confirm the head stayed turned three
    quarters away throughout the speech.

PASSPORTS AS SEEN
    What you actually observed for the woman, the man, the sealed
    figure(s), the seated one, the plate, the floor, the walls and the
    light - before comparison.

SCORES
    Ten rows, one per category, with a one-line justification each, then
    the computed mean.

TOP 5 CRITICAL
    The five findings that cost the most, worst first. Each: timecode,
    scene, severity, what is wrong, why it matters.

SCENE-BY-SCENE FINDINGS
    S61 through S70 in order. For each: what you verified as correct
    (briefly), then each deviation with a timecode and a severity. If a
    scene is clean, say so in one line and move on.

PHASE CHAIN
    Judged across the ten scenes in order (mode T: across the clips;
    mode R: across the reel). Is the plate one object at one scale
    throughout? Is S64's recess the one S65 and S66 stand at? Is the
    standing figure one figure across S61, S62, S65 and S66? Is S67
    framed like her earlier close-ups? Does the interior hold one
    light state from S61 to S69, and does S70's exterior daylight
    read as the same world?

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
    What you actually observed in this clip - figures, suits, plate,
    floor, walls, light - before comparison.

WATCHER CHECK
    If the declared scene contains the sealed figure: one line per
    anchor point (height / back / dust / DIGIT COUNT / visor plate /
    motion): what the spec REQUIRES, what you SEE, verdict. If it does
    not, one line confirming no pearl-white figure is in frame.

VERDICT AGAINST THE SCENE ROW
    Walk the declared scene's row: each MUST BE TRUE item - held or not,
    with the clip-relative second. Each MUST NEVER APPEAR item that
    appeared, with second and severity. If the scene has an ONLY EVENT
    line, open with whether the event was delivered.

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
  contains. If S65 does not match its row, that is a deviation IN S65.
- Do not invent a bible, a plan, a script or a scene that is not in the
  scene table.
- Do not report S65's two identical figures as a duplication error, a
  cloning artefact or a continuity break. The duplication is the
  designed information of the phase. Only a THIRD copy, or a
  DIFFERENCE between the two, fails.
- Do not report the plate's total lack of response as a defect,
  an unfinished shot or a missing payoff. The inertness IS the shot,
  in every scene, including both touches in S62.
- Do not report the seated figure's stillness as a defect or ask for
  a performance from it.
- Do not report the humans' FIVE-fingered gloves as a digit-count
  failure. The four-digit lock binds the sealed figure's gloves only.
- Do not report the man speaking in S63 or the woman's four words in
  S69 as speech-lock violations - those are the two licensed windows.
  What fails there is only a clearly readable, camera-facing mouth.
- Do not report the absence of dialogue, footsteps, wind or ambient
  audio as a defect. The material is silent by design.
- Do not report the absence of lip movement as a defect - the lock is
  one-directional.
- Do not report scene-boundary cuts. See STEP 0.
- Do not report S65's or S66's slowed, dreamlike motion as a defect -
  those two scenes are retimed by design. In every other scene,
  slow-motion feel IS a finding.
- Do not report the absence of a luminous wall pattern as a defect -
  it belongs to the previous phase. A pattern APPEARING here fails.
- Do not recommend adding drama the format cannot hold: no coverage, no
  inserts, no reaction shots, no handheld energy, no extra camera moves,
  no "let the plate respond". Every recommendation must be achievable in
  a re-render of a single 10-second locked-off or single-push-in shot.
- Every finding carries a timecode and a scene number, or it is deleted
  before you output.
- Words like "probably", "seems intended to", "may have been" mean you are
  guessing. Cut the finding or move it to FLAGS FOR DOCUMENT CHECK.
```

---

## Faz 6 rubriğinden farkları

Aynı iskelet (üç mod, otomatik seçim, CLIP MAP, içerik-satır çelişki
kuralı, tek yönlü konuşma kilidi), ama denetlenen nesne değişti: kule
içi dekoru aynı, olay bir NESNENİN HİÇBİR ŞEY YAPMAMASI.

```
+ INERT PLATE LAW           fazın omurgası: plaka beş sahnede görünür
                            ve hiçbirinde tepki vermez — S62'de İKİ
                            KEZ dokunulur, iki kez de hiçbir şey olmaz.
                            "Ödül veren model" bu sahneyi öldürür.
                            PLATE LEDGER ile sahne sahne sorulur
+ LİSANSLI İKİZ [KARAR 1]   S65'te iki özdeş figür KURAL DEĞİL BİLGİ.
                            Rubrik bunu ihlal saymaz; batıran şey
                            ÜÇÜNCÜ kopya ya da ikisi ARASINDAKİ FARK.
                            PEARL-BODY COUNT satırı her sahne için
                            sayı verir (S63/S67/S69/S70 = 0)
+ GROUND RESPONSE 3/3       F5'te iki (S45/S47), F6'da sıfır, F7'de
  TEK SAHNE · TEK YER       BİR: yalnız S68 ve yalnız plakanın 20 cm
                            YANINDA. "Tepki elin altına kaydı" ayrı
                            bulgu olarak tanımlandı [KARAR 3]
+ SEATED ORIGINAL LAW       yeni figür sınıfı: ölü asıl CESET DEĞİL.
                            Çürüme/kemik/mumya/çökmüş kumaş/toz
                            listesi + "asla hareket etmez" + S66'da
                            NET ÇIKMAMASI [KARAR 2]
+ GLOVE LOCK = BLOCKER      ÇEHOV 7 feinti: halka iki kez tutulur,
                            hiç dönmez. Çıplak ten fazın blocker'ı;
                            GLOVE & SKIN LEDGER halka durumunu S68 ve
                            S69 için ayrı ayrı sorar
+ İKİ KONUŞMA PENCERESİ     F6'da tek pencere vardı (S58). Burada iki:
  + AĞIZ HATTI KİLİDİ       S63 Mühendis, S69 Kaptan — ikisi de 3/4
                            çevrik. Yeni bulgu sınıfı: pencere İÇİNDE
                            bile kameraya dönük OKUNAKLI ağız [KİLİT 2]
+ YANAL KAYDIRMA YASAĞI     [KARAR 4] faz imzası devrediyor: üç
                            push-in, yedi lockoff, sıfır yanal takip.
                            Kadrajda yanal takip = imza ihlali
+ İKİ RETIME SAHNESİ        F5'te S43, F6'da S60, F7'de İKİ tane:
                            S65 ve S66 — ağır çekim hissi yalnız o
                            ikisinde doğru
+ DIŞ ÇEKİM GERİ DÖNDÜ      S70 tek dış kare: 4400K sol key + gündüz
                            ayı + kuyruksuz ışık noktası. Işık
                            kategorisi iki durumlu hale geldi
− PATTERN LEDGER            kayıt duvarı F6'da kaldı; desen artık
                            YASAK — "desenin YOKLUĞU bulgu değildir,
                            VARLIĞI bulgudur" kuralı yazıldı
− FLOOR LEDGER (F6)         zeminde daire arama bitti — plaka artık
→ PLATE + GROUND LEDGER     sahnede; yerine "plaka tepki verdi mi" ve
                            "zemin oynadı mı" ikilisi geldi
+ ÖLÇÜLMEMİŞ HARİTA UYARISI F6 raporu kusursuz 10×10.0 s segment
                            haritası verdi ve bu ölçüm değil varsayım
                            çıktı; MODE R'a "MEASURED mi ASSUMED mi
                            yaz" zorunluluğu eklendi [F6 D-AI]
```

---

## 📌 ÇALIŞTIRMA KAYDI

```
1 kez çalıştırıldı · son 12.08.2026 · sonuç: BULGU KOŞUSU, TABAN YOK
  girdi: 1 birleşik reel (MODE R) — protokol 10 ayrı klip (MODE T)
  ham çıktı: kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
             02_HAM_RAPORLAR/THE_SECOND_SHIP_FAZ07_HAM.md
  işlenmiş : FAZ_07_QA_DERSLER.md

RUBRİĞİN TUTAN TARAFI
  · içerik-çelişki kuralı (STEP 0.5) beş kaymış segmentin beşini de
    yakaladı ve hangi satıra benzediğini yazdı — bulguların içerikle
    yeniden atfedilmesi yalnız bu sayede mümkün oldu
  · protokol sapması satırı raporun başına yazıldı
  · S65'in lisanslı ikizi hiçbir yerde "hata" olarak raporlanmadı
  · hane SAYIMI zorunluluğu dört sahnede beş parmağı yakaladı

RUBRİĞİN BATAN TARAFI → YAMALANDI
  · eşleme çöktüğü hâlde on kategoriye de puan verildi (1.9 ortalama
    anlamsız) → MAPPING COLLAPSE GATE eklendi [DERS 92]
  · SEGMENT MAP yine "MEASURED" damgasıyla kusursuz 10 × 10.0 s geldi
    (F6 D-AI tekrarı) — uyarı metinde duruyor, işe yaramadı; süre
    denetimi NLE'ye devredildi
  · WATCHER LEDGER satırları yuva numarasına göre yazıldığı için
    kayma altında okunamaz hâle geldi — sonraki faz rubriğinde
    ledger satırlarına İÇERİK sütunu eklenmeli
```
