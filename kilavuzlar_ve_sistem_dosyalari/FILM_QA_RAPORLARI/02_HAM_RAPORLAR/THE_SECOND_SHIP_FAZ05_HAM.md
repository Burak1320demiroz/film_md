# THE SECOND SHIP — FAZ 5 / TEMAS · HAM QA ÇIKTISI (1. KOŞU)

> Tarih: 10.08.2026 · Rubrik: `FAZ_05_TEMAS/FAZ_05_QA_PROMPT.md`
> Girdi: 8 ayrı klip · **MODE T — beş fazda İLK KEZ** (dosya adlarında
> sahne numarası YOKTU → eşleme yükleme sırasına düştü)
> ⚠️ FAZ ölçümüdür — film tablolarına ve 00_INDEX sayacına GİRMEZ.
> ⚠️ EŞLEME KAYMASI: operatör S47'yi (ve büyük olasılıkla bir sahneyi
> daha) yüklemedi; numarasız adlar yüzünden 6-7-8. klipler bir(er) yuva
> kaydı. Raporun S46/S47/S48 satırlarındaki bulgular ile "S49 & S50
> missing" satırı bu kaymanın eseridir — düzeltilmiş eşleme ve gerçek
> bulgu listesi: `FAZ_05_TEMAS/FAZ_05_QA_DERSLER.md`
> ⚠️ ÇIKTI EKSİK: model rubriğin çıktı formatının yalnız ilk yarısını
> üretti — WATCHER LEDGER, GROUND RESPONSE TABLE, DRAWING LEDGER,
> SCORES, TOP 5, PHASE CHAIN, FLAGS ve WHAT WORKED bölümleri YOK.
> Skor satırı bulunmadığından hiçbir tabloya sayı işlenmez.
> Bu dosya modelin ham çıktısıdır, düzenlenmez.

---

MATERIAL & DELIVERY HYGIENE
Mode Selection: MODE T (TEN CLIPS)

Delivered Files: 8 separate video clips (expected 10).

Missing Slots: S49 and S50 have no video files delivered.

Duration Hygiene Deviations:

S45: Clip duration is ~8.0 s (undersized against 10.0 s spec).

S47 (Clip 7): Clip duration is ~8.0 s (undersized against 10.0 s spec).

CLIP MAP TABLE
Clip File    Target Slot    Content Match    Mapped Content Description
Clip 1    S41    MATCH    Standoff in clearing; 3 figures (Woman, Man, Watcher).
Clip 2    S42    MATCH    Medium shot; woman halts man's hand reach toward sheath.
Clip 3    S43    MATCH    Close-up retimed shot; Watcher helmet slow head bow.
Clip 4    S44    MATCH    Crouched woman finger-drawing in fine ground dust.
Clip 5    S45    MATCH    Close-up of dust drawing with Watcher glove resting at frame right.
Clip 6    S46    MISMATCH    Content represents S48: 3 figures walking toward 400 m white tower.
Clip 7    S47    MISMATCH    Content represents S49: Humans crossing knife-sharp line onto polished stone.
Clip 8    S48    MISMATCH    Content represents S50: Watcher standing alone touching smooth tower wall.
—    S49    MISSING    No file delivered for slot S49.
—    S50    MISSING    No file delivered for slot S50.

PASSPORT (OBSERVED MATERIAL)
The Woman:

Face & Hair: Light olive skin, high cheekbones, dark brown hair in a tight low bun. Faded white scar splitting her left eyebrow.

Suit & Accents: Dark grey-blue pressure suit with orange reinforcement panels on shoulders and knees. Transparent, un-tinted glass visor revealing face clearly.

The Man:

Face & Hair: Light brown skin, short black hair, three-day dark stubble, burn scar on right cheekbone.

Suit & Accents: Dark grey-blue suit with teal green shoulder/knee accents. Large oversized back tool module. Sheathed cutting tool on left hip. Fully transparent visor.

The Tall White Figure (Watcher):

Height & Build: ~2.10 m tall (stands a head over the man in three-figure compositions).

Back: Smooth, completely flat, featureless pearl-white back with zero hoses, straps, or packs.

Suit & Gloves:

Surface is seamless, dustless pearl white.

Gloves (S45, Clip 8): Rendered with 5 digits (4 fingers + 1 thumb) rather than the required 4 digits (3 fingers + 1 thumb).

Visor Plate: Dark grey-green/black flush plate, non-transparent, with ambient surface sheen.

The Ground:

S41–S45: Loose basaltic dust, small debris, and shattered ship wreckage in blurred background.

S45: Billowing, airborne dust clouds floating across the drawing zone.

Clip 7 (mapped S47): Knife-sharp boundary line separating rough cracked ground/dust from smooth light-grey polished bare stone.

The Dust Drawings (S44, S45):

S44: Crouched woman drawing in dust; pre-existing extra text/symbol glyphs visible on the ground surface.

S45: Drawing area shows a double-ended arrow and boxy ship outline under moving dust.

The Tower & Horizon:

Clip 6 (mapped S46) / Clip 7 (mapped S47): Massive matte white column rising into sky.

Clip 7 (mapped S47): Base of the white tower contains a visible recessed arched doorway/entrance opening.

Lighting:

Constant soft orange daylight (4400K key from frame left), pale daytime sky with pale daytime moon disk visible.

DETAILED FINDINGS BY MAPPED SCENE
S41 — THE STANDOFF (Clip 1)
S41 at 0s–3s: Man's right hand remains static at his hip rather than executing a distinct drift toward the sheath. (Minor motion deviation)

S41 at 0s–10s: Overall framing, three-figure composition, height differentials, scar placement, and Watcher head-tip conform to locked spec.

S42 — THE GRIP (Clip 2)
S42 at 2s–7s: Woman successfully reaches across and grips his wrist before he touches the sheath, guiding his arm down. Inverse lock maintained (Watcher absent). Fully compliant take.

S43 — "DO NOT." (Clip 3)
S43 at 3s–8s: Retimed fluid micro-bow of helmet performed cleanly. Visor plate remains opaque dark flush surface without internal eye/face rendering. Fully compliant take.

S44 — THE DRAWING (Clip 4)
S44 at 0s–10s [TEXT / PICTOGRAM VIOLATION]: Pre-existing letter-like text glyphs and extra symbol marks appear imprinted in the dust surface adjacent to the drawn ship outline.

S44 at 6s [DRAWING LAW]: The drawn directional mark contains extra line strokes rather than a single crisp V-profile wedge tip pointing UP.

S45 — THE GROUND ANSWERS (Clip 5)
S45 at 0s–8s [DELIVERY HYGIENE]: Clip duration is short (~8.0 s vs required 10.0 s).

S45 at 0s–8s [TEXT / GRAPHIC OVERLAY VIOLATION]: A vertical film strip border with readable numeric text ("40", "49") is burned into frame left.

S45 at 1s–8s [WATCHER ANCHOR #4]: The Watcher's glove resting at frame right is rendered with 5 digits (4 fingers + 1 thumb) instead of the mandated 3 fingers and a thumb.

S45 at 1s–5s [GROUND RESPONSE LAW]: Airborne dust clouds billow and stream across the frame above the ground surface. The spec strictly limits motion to dry sand-grain scale sliding under 3 cm without airborne dust suspension.

S45 at 4s–7s [DRAWING LAW]: The directional stroke forms a double-headed arrow rather than executing the required single downward-pointing wedge.

S46 — HORIZON LINE (Clip 6)
S46 at 0s–10s [MISFILED CLIP / CONTENT MISMATCH]: Clip 6 contains the content of S48 (3 figures walking toward the 400 m tower) instead of S46. Audited against the mapped row S46:

S46 at 0s–10s [FIGURE COUNT]: Clip displays 3 full figures instead of the required 2 (Watcher + partial woman shoulder/helmet).

S46 at 0s–10s [TOWER NEGATION]: The distant white line is rendered as a fully realized 400 m wide tower structure taking up mid-frame, violating the required single thin vertical line.

S47 — LATERAL FOLLOW (Clip 7)
S47 at 0s–8s [DELIVERY HYGIENE]: Clip duration is short (~8.0 s vs required 10.0 s).

S47 at 0s–8s [MISFILED CLIP / CONTENT MISMATCH]: Clip 7 contains the content of S49 (humans stepping across the dead ring line) instead of S47. Audited against the mapped row S47:

S47 at 0s–8s [SHOT CLASS & CAMERA]: Fixed medium shot of two humans crossing ground boundary instead of the mandated lateral follow camera on Watcher legs/boots.

S47 at 0s–8s [FIGURE COUNT]: Displays 2 human figures; Watcher legs/boots are entirely absent.

S47 at 0s–8s [GROUND RESPONSE LAW]: Surface swells around boot soles are absent.

S47 at 0s–8s [TOWER NEGATION LAW]: The base of the white tower in the background features a distinct arched doorway/entrance opening. The spec strictly forbids any doors, hatches, ports, or openings (lit or unlit) on the tower structure.

S48 — TOWER AT SCALE (Clip 8)
S48 at 0s–10s [MISFILED CLIP / CONTENT MISMATCH]: Clip 8 contains the content of S50 (Watcher hand pressed flat on tower wall) instead of S48. Audited against the mapped row S48:

S48 at 0s–10s [FIGURE COUNT]: Displays 1 figure (Watcher alone) instead of the required 3 figures (Watcher + woman + man walking).

S48 at 1s–10s [WATCHER ANCHOR #4]: The Watcher's glove pressed against the wall is rendered with 5 digits (4 fingers + 1 thumb) instead of 3 fingers and a thumb.

S49 — THE DEAD RING & S50 — SILENCE
S49 & S50: NO CLIPS DELIVERED. Slots S49 and S50 are empty.
