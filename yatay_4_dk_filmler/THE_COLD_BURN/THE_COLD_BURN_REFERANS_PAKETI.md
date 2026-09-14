# 🎯 THE COLD BURN — REFERANS PAKETİ

## Karakter · Araç · Mekan — **her varlık için TEK referans sayfası**
### 6 birleşik referans sayfası (28 panel) · kapak ayrı dosyada

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR.**
> 30 sahnelik, İKİ İNSANLI ve İKİ ARAÇLI bir filmde çapa önceden
> kilitlenmezse araç her sahnede yeniden tasarlanır. Üretim sırası:
> **bu dosya → onay → seed kilidi → PART_A/PART_B sahneleri.**
>
> Tüm promptlar Ders 34 uyumlu: **karakter adı hiçbir promptta geçmez.**
> Tüm promptlar Ders 79 uyumlu: **sırt ünitesi yok, vizör yansımasız.**

---

# 0. ⚠️ NEDEN BU DOSYA VAR

```
SORUN (07.08.2026'da doğrulandı): Dört varlığın tanımı 60 promptta
KELİMESİ KELİMESİNE aynı hâle getirildi (SAHNE_DEVAMLILIK §2.1 çapalama
kuralı) — ve bu YETMEZ. Metin çapası modelin aynı CÜMLEYİ okumasını
sağlar, aynı NESNEYİ çizmesini sağlamaz. Text-to-video her çağrıda gövde
oranlarını, panel yerleşimini, burun biçimini yeniden uyduruyor. 30
sahnede 30 farklı araç demek.

MEKANİZMA (kılavuzun kendi ölçümü — SAHNE_DEVAMLILIK §1): Kling 3.0
referanssız yüz devamlılığı %89 / 10 ardışık üretim Runway 4.5    "Gen-4
References" ile görsel referans → hata %38 azalıyor Veo 3.1
"Ingredients" — sahne bileşenlerini ayrı referanslardan kurar Luma Ray
keyframe/I2V — başlangıç karesi neyse video onu korur → Dördünün de
girdisi GÖRSEL. Elimizde görsel yoksa hiçbiri çalışmıyor.

KANIT — depodaki üç vaka:
· Starless Circle · Unbroken City: Character Bible doğruydu, metin
kilidi 36 promptta yazılıydı; sırt ünitesi ve aynalı vizör YİNE geldi
[Ders 79]. Bible metindi, referans değildi.
· Slow Stone: 7-9 dk formatı referans paketini ZORUNLU tutuyor ve
Kamera/tutarlılık skorları serinin en yükseği (7/10) — tek fark,
sahneleri ayrı üretmesi ve önceden çapa kilitlemesi.
· Waking Ground: format kartı "referans paketi EN BAŞTA hazırlanır — 75
imajlık zincirde çapa kilitlenmezse 3. fazda yüz kayar" diyor.

SONUÇ: 3-5 dk formatının dosya listesinde referans paketi YOKTU. Bu film
onu 7-9 dk formatından ödünç alıyor. Gerekçe: bu, depodaki ilk iki
insanlı + iki araçlı film; çapa yükü 7-9 dk formatınınkine yakın.
```

---

# 1. 📋 ÜRETİM SIRASI VE SEED TAKİP TABLOSU

| # | Referans sayfası | Panel | Öncelik | Seed | Durum |
|---|---|:---:|:---:|---|:---:|
| **RK1** | PİLOT SAYFASI | 5 | 🔴 ZORUNLU | | ☐ |
| **RK2** | MÜHENDİS SAYFASI | 5 | 🔴 ZORUNLU | | ☐ |
| **RA** | LANDER SAYFASI | 6 | 🔴 ZORUNLU | | ☐ |
| **RB** | ANA GEMİ SAYFASI | 4 | 🔴 ZORUNLU | | ☐ |
| **RI1** | LANDER KABİNİ | 4 | 🟠 GEREKLİ | | ☐ |
| **RI2** | ANA GEMİ İÇİ | 4 | 🟠 GEREKLİ | | ☐ |
| KP | Film kapağı | 2 | — | | ☐ |

```
ÜRETİM SIRASI — kapı kapı, atlama yok:

RA  →  ARAÇ ÖNCE. Filmin en çok kayan varlığı bu; 19 sahnede var.
Onaylanmadan hiçbir sahne üretilmez.
RK1 →  pilot yüzü + suit kilitlenir
RK2 →  mühendis yüzü + suit kilitlenir
⚠️ RK1 ve RK2 YAN YANA bakılır: iki kişi birbirine benziyorsa ikisi de
reddedilir (klon riski burada başlar, S4/S25'te patlar)
RB  →  ana gemi + drog konisi
RI1 →  kabin (duruş küresi ve yakıt göstergesi burada standartlaşır)
RI2 →  ana gemi iç hacimleri KP  →  kapak (THE_COLD_BURN_KAPAK.md) — RK1
onaylandıktan SONRA

Sonra: PART_A / PART_B sahne üretimi (kapı sahneleri S12·S21·S22·S25).
```

---

# 2. 🗺️ SAHNE → REFERANS EŞLEME

> Sahne üretirken **ilgili sayfanın TAMAMINI** yükle. Model sayfadaki
> bütün panelleri görür; tek panel yüklemekten daha güçlü çapadır.

| Sahne | Yüklenecek referans | Not |
|---|---|---|
| S0 | **RA** (p1-p2) | araç uzakta, siluet doğru olmalı |
| S1 · S2 · S3 · S4 | **RK1 + RK2 + RA** | iki insan aynı karede — klon riski |
| S5 · S6 | **RK1 + RK2 + RI1** | kabin içi, kasklı |
| **S7** | **RA (p1-p4)** | kalkış: karın lüleleri + bacak yuvaları |
| S8 | **RI1** (p1) | camdan dışarı, kabin çerçevesi |
| S9 | RK1 + RK2 + RI1 | arkadan iki kask |
| S10 | **RA (p5) + RB** | iki araç aynı karede, ölçek farkı |
| S11 | RK2 + RI1 (p3) | eldiven + konsol detayı |
| **S12** | **RA (p5 → p6)** | patlama: hasar burada DOĞAR |
| S13 · S17 | RI1 (p1) | cam kadrajı sabit kalmalı |
| S14 · S16 · S20 · S23 | RK1 + RK2 + RI1 | kokpit, kasklı |
| **S15 · S18 · S19 · S21 · S24 · S27 · S29** | **RA (p6)** | hasarlı gövde — aynı yırtık, aynı yer |
| S18 · S19 · S21 | + **RB (p2-p3)** | drog konisi ve mandal geometrisi |
| **S22** | **RB (p4)** | 3 kapalı + 1 takılı mandal |
| S25 | RK1 + RK2 + **RI2 (p1)** | tünel — klon sıcak noktası [D69] |
| S26 | RK1 (p5) + RK2 (p5) + RI2 (p2) | KASKSIZ paneller |
| S27 | RK1 (p5) + RK2 (p5) + RI2 (p3) + RA (p6) | kupola + yara |
| S28 | RK1 (p5) + RK2 (p5) + RI2 (p4) | koridor |

---

# 👤 BÖLÜM 1 — PİLOT SAYFASI `RK1` 🔴

> Filmin yüz çapası bu tek görselde. En yüksek çözünürlükte üret.
> Paneller arasında yüz sapıyorsa sayfayı at, yeniden üret.

```
Photorealistic CHARACTER REFERENCE SHEET, 16:9, maximum resolution. One
frame divided into FIVE CLEAN PANELS separated by thin neutral mid-grey
gutters: a TOP ROW of three equal portrait panels and a BOTTOM ROW of
two equal full-figure panels. Every panel shows THE SAME ONE WOMAN — no
other individual appears anywhere on the sheet. Neutral studio lighting
for reference use.

THE PERSON — IDENTICAL IN ALL FIVE PANELS: a woman in her late thirties,
1.70 metres, lean and wiry. Light olive skin with clearly visible pore
texture and natural subsurface scattering — no airbrushing, no
smoothing, no beauty retouching. Sharp defined jawline. Dark brown eyes,
steady and appraising. A thin pale scar splitting her LEFT EYEBROW into
two halves. Fine dry lines at the outer corners of both eyes. No makeup,
no jewellery.
HAIR: jet-black, cut in a short tactical crop, close at the sides, matte
and slightly uneven where it has been cut without care.

THE SUIT — THIS EXACT CONFIGURATION REPEATS IN EVERY SCENE OF THE FILM:
a sleek matte pearl-white HARD-SHELL pressure suit — segmented chest,
shoulder and thigh plates with crisp recessed seams; dark graphite
flex-weave fabric visible at every joint (shoulders, elbows, waist,
knees); machined aluminium articulation rings at both shoulders, both
elbows and both wrists; inlaid TEAL accent bands running across the top
of each shoulder plate and around each forearm plate, set flush into the
shell, not painted on. The whole suit is finely scuffed and hairline
scratched from use, dulled at the elbows and knees. The BACK IS FLAT: no
backpack, no tank, no hose, no cable, no rear housing of any kind. The
HELMET is low-profile, matte pearl-white, with a single seamless
optically clear panoramic visor — zero tint, zero mirror coating, zero
reflection of the environment; the face behind it is fully readable.

PANEL 1 — TOP LEFT, FACE FRONT, NO HELMET: head and shoulders, facing
camera straight on, neutral expression, mouth closed, eyes level with
the lens. Only the suit's white collar ring with its teal band shows at
the base. 85mm look, sharp across the whole face.

PANEL 2 — TOP CENTRE, LEFT PROFILE, NO HELMET: exact 90-degree left
profile, head and shoulders, looking straight ahead out of the panel.
The jawline and the scarred left eyebrow read clearly at this angle.
Same collar ring at the base.

PANEL 3 — TOP RIGHT, FACE THROUGH THE VISOR: close-up seen through the
CLOSED helmet's fully clear panoramic visor — the glass carries no tint,
no coating and no reflection, so her entire face is completely readable
and her skin texture is visible through it. Neutral alert expression,
mouth closed, slight three-quarter angle. A faint film of breath
condensation sits at the very bottom edge of the glass only.

PANEL 4 — BOTTOM LEFT, FULL FIGURE, HELMET CLOSED: standing upright,
full body with headroom, arms relaxed at her sides, three-quarters to
camera, face readable through the clear visor. The complete suit as
described, boots flat-soled and scuffed. Seen with enough clearance
around her that the flat back silhouette is unmistakable.

PANEL 5 — BOTTOM RIGHT, FULL FIGURE, BARE-HEADED AND SPENT: the same
woman in the same suit, helmet REMOVED and held in both gloved hands at
waist height, her short black hair matted flat with sweat, face bare and
exhausted, eyes closed, shoulders dropped. Skin damp, colour high on the
cheeks. This is her state in the last three scenes of the film. Panels 4
and 5 must be directly comparable — SAME face, SAME suit, only the
helmet and the fatigue differ.

Camera and light across the sheet: soft even neutral key at 5000K with
gentle fill, mid-grey seamless background in every panel, shadows soft
but present. Every pore, weave, scuff and machined edge stays visible.

Negative: the five panels show ONE person only — no second individual,
no crowd, no reflected figure. Face, hair, build and suit IDENTICAL
across every panel — no drifting, no morphing, no age or feature change.
The visor never carries tint, mirror coating, reflection, HUD graphics
or display overlay. The back is flat in every panel — no backpack, tank,
hose or rear unit ever appears. NO text, letters, numbers, labels,
captions, arrows, callouts, panel titles or watermarks anywhere on the
sheet or in the gutters. No airbrushing, no waxy or plastic skin, no
beauty filter, no makeup, no jewellery. No weapon. No stylisation, no
illustration, no CGI look, no video game render. Photorealistic with
35mm film grain.
```

---

# 👤 BÖLÜM 2 — MÜHENDİS SAYFASI `RK2` 🔴

> ⚠️ Üretildiğinde RK1 ile YAN YANA koy. İki yüz birbirine benziyorsa
> ikisi de reddedilir — depodaki klon vakalarının üçü de (Stone Sky,
> Unbroken City, Starless Circle) iki figürün ayrışamamasıydı.

```
Photorealistic CHARACTER REFERENCE SHEET, 16:9, maximum resolution. One
frame divided into FIVE CLEAN PANELS separated by thin neutral mid-grey
gutters: a TOP ROW of three equal portrait panels and a BOTTOM ROW of
two equal full-figure panels. Every panel shows THE SAME ONE MAN — no
other individual appears anywhere on the sheet. Neutral studio lighting.

THE PERSON — IDENTICAL IN ALL FIVE PANELS: a man in his mid-forties,
1.82 metres, broad-shouldered and heavy through the chest. Deep brown
skin with clearly visible pore texture and natural subsurface scattering
— no airbrushing, no smoothing. A broad nose with a wide bridge. A
short, close grey-flecked beard following the jaw, denser grey at the
chin. Close-cropped hair, receding slightly at the temples. Deep fatigue
lines beneath both eyes and across the forehead. Calm, heavy-lidded dark
eyes. No jewellery.

THE SUIT — IDENTICAL TO THE OTHER CREW MEMBER'S EXCEPT FOR THE ACCENT
COLOUR: a sleek matte pearl-white HARD-SHELL pressure suit — segmented
chest, shoulder and thigh plates with crisp recessed seams; dark
graphite flex-weave fabric at every joint; machined aluminium
articulation rings at shoulders, elbows and wrists; inlaid AMBER accent
bands across the top of each shoulder plate and around each forearm
plate, set flush into the shell. Finely scuffed and hairline scratched
from use. The BACK IS FLAT: no backpack, no tank, no hose, no cable, no
rear housing of any kind. The HELMET is low-profile, matte pearl-white,
with a single seamless optically clear panoramic visor — zero tint, zero
mirror coating, zero reflection.

PANEL 1 — TOP LEFT, FACE FRONT, NO HELMET: head and shoulders, facing
camera straight on, neutral expression, mouth closed. The beard's grey
distribution and the broad nose read clearly. Suit collar ring with its
amber band at the base. 85mm look.

PANEL 2 — TOP CENTRE, RIGHT PROFILE, NO HELMET: exact 90-degree right
profile, head and shoulders, looking straight ahead. Beard line, brow
weight and receding temple read clearly.

PANEL 3 — TOP RIGHT, FACE THROUGH THE VISOR: close-up through the CLOSED
helmet's fully clear panoramic visor — no tint, no coating, no
reflection; his entire face readable, beard texture visible through the
glass. Neutral alert expression, slight three-quarter angle.

PANEL 4 — BOTTOM LEFT, FULL FIGURE, HELMET CLOSED: standing upright,
full body with headroom, arms relaxed, three-quarters to camera, face
readable through the clear visor. Visibly taller and broader than a 1.70
m frame — the height difference is a continuity lock. Flat back
silhouette clear.

PANEL 5 — BOTTOM RIGHT, FULL FIGURE, BARE-HEADED AND SPENT: the same man
in the same suit, helmet REMOVED and clipped to a rack at his side, bare
head bowed slightly, face exhausted, eyes open and unfocused, sweat at
the hairline. This is his state in the last three scenes. Panels 4 and 5
must be directly comparable — SAME face, SAME suit, only the helmet and
the fatigue differ.

Camera and light across the sheet: soft even neutral key at 5000K,
mid-grey seamless background, shadows soft but present. Every pore,
beard hair, weave and machined edge visible.

Negative: ONE person only on the sheet — no second individual, no
reflected figure. Face, beard, build and suit IDENTICAL across every
panel — no drifting, no morphing. The visor never carries tint, mirror
coating, reflection or HUD graphics. Flat back in every panel — no
backpack, tank, hose or rear unit. NO text, letters, numbers, labels,
captions, arrows, callouts or watermarks anywhere on the sheet or in the
gutters. No airbrushing, no waxy skin, no beauty filter. No weapon. No
stylisation, no illustration, no CGI look, no video game render.
Photorealistic with 35mm film grain.
```

---

# 🚀 BÖLÜM 3 — LANDER SAYFASI `RA` 🔴

> **Filmin en çok kayan varlığı — 19 sahnede var ve şimdiye kadar her
> sahnede yeniden tasarlanıyordu.** Bu sayfa onaylanmadan hiçbir sahne
> üretilmez. Altı panel, aracın bütün okunuşlarını kapatır.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one single
spacecraft, 16:9, maximum resolution. One frame divided into SIX CLEAN
PANELS separated by thin neutral mid-grey gutters, in two rows of three.
Every panel shows THE SAME ONE VEHICLE from a different angle or in a
different state. No humans anywhere on the sheet. Neutral studio
lighting for reference use, plain mid-grey seamless background in every
panel.

THE VEHICLE — IDENTICAL IN ALL SIX PANELS: a 9-metre angular
LIFTING-BODY lander. It is NOT a cylinder and NOT a rocket: the hull is
a flattened, faceted wedge that sits HORIZONTAL, its long axis parallel
to the ground. A broad flat belly. Sharp chine lines running unbroken
from the nose back to the tail, dividing the upper and lower surfaces. A
low blended forward canopy faired into the nose, its single wide
windshield pane wrapping slightly around the front. Two short swept
strakes low on the flanks. The tail is notched, and set into that notch
are TWO main engine nozzles side by side. Under the belly, four
downward-facing LIFT NOZZLES in two pairs, one pair forward of the
centre of mass and one pair aft. Four articulated landing legs with oval
footpads, which fold up into flush wells in the belly behind hinged gear
doors. A rectangular SIDE HATCH on the port flank, forward, with a
recessed grab rail. A 30-centimetre docking probe on the nose with three
small alignment vanes around it.

FINISH — IDENTICAL EVERYWHERE: matte ceramic-white composite panels with
crisp recessed seams and visible flush fastener rows, laid over an
exposed graphite-grey structural spine that shows along the upper
centreline and around the tail notch. One sweeping TEAL chevron stripe
runs down each flank, following the chine line, its paint edge chipped
from use. Scuffs, grey-brown dust staining on the belly and legs, heat
discolouration around the tail. No markings, no numbers, no insignia of
any kind.

PANEL 1 — TOP LEFT, THREE-QUARTER FRONT, LEGS DOWN: the vehicle standing
level on all four extended landing legs, seen from a low three-quarter
front angle. The canopy, the nose probe, the side hatch and the chine
lines all read.

PANEL 2 — TOP CENTRE, PURE SIDE PROFILE, LEGS DOWN: exact 90-degree side
elevation, port side to camera, standing level. The full silhouette
reads: flat belly, chine line, canopy, strake, notched tail with its two
nozzles, side hatch, four legs.

PANEL 3 — TOP RIGHT, BELLY FROM BELOW, LEGS DOWN: the vehicle seen from
underneath, showing the flat belly plating, the FOUR downward lift
nozzles in their two pairs, the four open leg wells with their hinged
gear doors, and the leg geometry where it meets the hull.

PANEL 4 — BOTTOM LEFT, THREE-QUARTER REAR: seen from behind at a
three-quarter angle, showing the notched tail, the two recessed main
engine nozzles with their scorched throats, the graphite spine running
into the notch, and the aft ends of both teal chevrons.

PANEL 5 — BOTTOM CENTRE, FLIGHT CONFIGURATION, CLEAN: the same vehicle
in space configuration — all four legs folded up and locked away behind
CLOSED gear doors, the belly line completely smooth and unbroken with NO
landing leg visible anywhere, hull clean and undamaged. This is the
configuration for every scene after the launch. Three-quarter front
angle, floating free against plain grey. This is the vehicle as it
appears from the launch until the explosion.

PANEL 6 — BOTTOM RIGHT, DAMAGED CONFIGURATION: the same vehicle, same
flight configuration with legs stowed, now carrying its permanent battle
damage — on the PORT FLANK, aft of the side hatch, a one-metre hull
panel torn outward and peeled back, its edges scorched black, one bent
pipe end protruding from the breach, and scorch streaks raking aft from
it along the chevron. At the nose, ONE of the three probe alignment
vanes is bent five degrees off true. Everything else identical to panel
5. This exact damage appears in every scene after the explosion and
never changes shape or position.

Camera and light across the sheet: even neutral studio key at 5000K with
soft fill, plain mid-grey seamless background, shadows soft but present
so every facet, seam, fastener and scuff reads.

Negative: ONE vehicle only per panel — no second craft, no variants, no
alternative designs on the sheet. The design is IDENTICAL in all six
panels — same proportions, same hull facets, same nozzle count, same
chevron path, no morphing between panels. It is never a cylinder, never
a capsule, never a vertical rocket, never a winged aeroplane. Exactly
TWO tail engine nozzles, exactly FOUR belly lift nozzles, exactly FOUR
landing legs, exactly THREE probe alignment vanes — these counts never
change. No humans, no crew, no figure at the canopy. No engine plume, no
fire, no smoke, no glow — the vehicle is unpowered on this sheet. NO
text, letters, numbers, insignia, flags, labels, captions, arrows,
callouts, dimension lines or watermarks anywhere on the sheet or in the
gutters. No stylisation, no illustration, no blueprint look, no CGI
render aesthetic, no video game look. Photorealistic with 35mm film
grain.
```

---

# 🛰️ BÖLÜM 4 — ANA GEMİ SAYFASI `RB` 🔴

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one single
spacecraft, 16:9, maximum resolution. One frame divided into FOUR CLEAN
PANELS separated by thin neutral mid-grey gutters, in two rows of two.
Every panel shows THE SAME ONE SHIP or a detail of it. No humans
anywhere on the sheet. Neutral studio lighting, plain mid-grey seamless
background.

THE SHIP — IDENTICAL IN ALL PANELS: a 140-metre INTERSTELLAR transfer
vessel — a long, heavy, purposeful machine built for a crossing between
stars, not a shuttle. From bow to stern: a machined docking hub carrying
a 1.2-metre concave DROGUE CONE ringed by FOUR hinged LATCH PETALS; then
a forward cluster of SIX cylindrical habitat modules mounted in THREE
tandem pairs, each wrapped in dirty-white multi-layer insulation
quilting with visible quilting seams, taped edges and scuffing; then a
long OPEN HEXAGONAL TRUSS SPINE of machined graphite-grey members with
visible bolted nodes; amidships TWO immense BLACK KNIFE-EDGE RADIATOR
WINGS standing out from the spine on either side, each wing as long as
several modules; then a broad conical SHADOW SHIELD facing aft; and
finally the FUSION DRIVE BLOCK at the stern, a dense armoured mass
carrying FOUR deeply recessed nozzles. A slender communications mast
sits amidships. The ship does not rotate and has no spinning ring, no
centrifuge.
SCALE: this vessel is more than fifteen times the length of the small
9-metre lander that docks with it. Surfaces are worn: micrometeorite
pitting, sun-yellowed insulation on the sunward side, grey staining
around thruster ports. No markings, no numbers, no insignia.

PANEL 1 — TOP LEFT, FULL SIDE PROFILE: exact 90-degree side elevation of
the entire 140-metre ship, filling the panel end to end. The whole
architecture reads in order: bow docking hub, six modules in three
tandem pairs, long truss spine, two radiator wings, shadow shield,
fusion drive block. To make the scale unmistakable, the small 9-metre
lander is shown in the SAME panel, in silhouette only, holding station
off the bow — it must read as roughly one fifteenth of the ship's
length.

PANEL 2 — TOP RIGHT, THREE-QUARTER FRONT: the ship seen from a
three-quarter front angle, the bow docking hub facing camera-left, the
depth of the truss and the tandem module arrangement clear.

PANEL 3 — BOTTOM LEFT, DOCKING HUB CLOSE-UP, PETALS OPEN: tight on the
bow hub — the 1.2-metre concave drogue cone, its brushed metal throat
polished smooth by use, guide grooves worn pale, and the FOUR latch
petals standing fully OPEN around the rim like an opened flower, their
hinge pins and actuator arms visible. Machine detail sharp: bolt heads,
wear marks, shadow inside the throat.

PANEL 4 — BOTTOM RIGHT, LATCH FAILURE STATE: the same hub, now with a
docking probe seated to full depth in the cone's throat, and the four
petals in their end state — THREE petals folded fully closed over the
probe's collar and seated home, and the FOURTH petal STOPPED at half
travel, its hinge line visibly bent and distorted, refusing to close.
Fine paint flakes drift loose near the joint. This is the exact state
the film ends the docking on.

Camera and light across the sheet: even neutral studio key at 5000K,
soft fill, plain mid-grey background, shadows soft but present so every
truss member, quilting seam, hinge pin and wear mark reads.

Negative: ONE ship only — no second vessel, no variants, no fleet (the
lander silhouette in panel 1 is a scale reference, not a second design,
and appears in that panel only). The architecture is IDENTICAL across
panels — same spine, same six modules in the same three tandem pairs,
same two radiator wings, same drive block, no morphing. Exactly SIX
habitat modules, exactly TWO radiator wings, exactly FOUR fusion nozzles
and exactly FOUR latch petals — these counts never change. The ship is
never shuttle-sized: it always reads as a vessel more than fifteen times
the lander's length. The ship never rotates and never has a spinning
ring or centrifuge. No humans, no figure at any window. No engine plume,
no fire, no glow. NO text, letters, numbers, insignia, flags, labels,
captions, arrows, callouts, dimension lines or watermarks anywhere on
the sheet or in the gutters. No stylisation, no illustration, no
blueprint look, no CGI render aesthetic, no video game look.
Photorealistic with 35mm film grain.
```

---

# 🎛️ BÖLÜM 5 — LANDER KABİNİ `RI1` 🟠

> Kabin 13 sahnede görünüyor. Duruş küresi ve yakıt göstergesi filmin
> METİNSİZ SAYAÇ kanalı — biçimleri burada standartlaşmazsa her sahnede
> başka bir gösterge çıkar ve sayaç anlatısı ölür [Ders 50 · Ders 78].

```
Photorealistic INTERIOR REFERENCE SHEET of one single spacecraft cabin,
16:9, maximum resolution. One frame divided into FOUR CLEAN PANELS
separated by thin neutral mid-grey gutters, in two rows of two. Every
panel shows THE SAME ONE CABIN. No humans anywhere on the sheet.

THE CABIN — IDENTICAL IN ALL PANELS: the cramped 2.2-metre-wide cockpit
of a small lander. TWO seats side by side, deep-bucketed, with
five-point harnesses hanging slack; the LEFT seat is the pilot's, the
RIGHT the engineer's. Ahead of them ONE wide windshield pane, 1.4 metres
across and 0.5 metres tall, set in a worn machined metal frame. The
console is analogue-heavy: matte dark panels, rows of ABSTRACT amber and
teal LIGHT SEGMENTS that show fill level only — no digits, no letters,
no icons, no screens. At the centre of the console sits a 12-centimetre
MECHANICAL ATTITUDE BALL in a machined bezel, a matt sphere with a
painted horizon band, lit dimly from behind. Beside it, the RESERVE FUEL
GAUGE: a single horizontal row of TEN identical segment sockets, each
socket clearly visible whether lit or dark. Ribbed wall conduits,
handholds, a sealed inner hatch behind the seats, a stowage bracket on
the floor. Everything worn: scuffed panel paint, finger-polished switch
guards, dust in the seams. Dim practical lighting.

PANEL 1 — TOP LEFT, FROM BEHIND THE SEATS: the view forward over both
empty seat headrests, exactly as the film's cockpit scenes are framed —
the two headrests low in frame, the console beyond, the wide windshield
filling the upper centre with plain neutral grey outside. 35mm look.

PANEL 2 — TOP RIGHT, FROM THE FRONT LOOKING AFT: the two empty seats
seen from the front of the cabin, harnesses hanging, the sealed inner
hatch behind them, the side wall conduits visible.

PANEL 3 — BOTTOM LEFT, CONSOLE DETAIL: tight on the centre console — the
mechanical attitude ball in its bezel, level, and beside it the reserve
fuel gauge showing EIGHT dark empty sockets and only TWO lit amber
segments, so that the full scale and the remaining margin are readable
in one frame. 85mm look, shallow depth, machine detail sharp.

PANEL 4 — BOTTOM RIGHT, SIDE WALL AND HATCH: the cabin's port wall — the
ribbed conduit run that a gloved hand rests on in the film, the grab
handholds, the floor stowage bracket, and the inner hatch with its
wheel.

Camera and light across the sheet: dim practical cabin light plus a soft
neutral fill so every surface still reads; plain neutral grey beyond the
windshield in every panel.

Negative: ONE cabin only — the layout is IDENTICAL across panels: two
seats, pilot LEFT and engineer RIGHT, never swapped, never three seats,
never one. Exactly TEN fuel gauge sockets and exactly ONE attitude ball
— these counts never change. NO readable text, letters, digits, numbers,
icons, glyphs or screen graphics anywhere on any panel, display or
surface — abstract light segments and one mechanical ball only. No
humans, no hands, no reflected face in the glass. No holograms, no
floating interfaces, no glowing blue UI. 0% bloom, no glow filter — lit
segments are small lit shapes, not halos. No labels, captions, arrows,
callouts or watermarks on the sheet or in the gutters. No stylisation,
no CGI render aesthetic, no video game look. Photorealistic with 35mm
film grain.
```

---

# 🚪 BÖLÜM 6 — ANA GEMİ İÇİ `RI2` 🟠

> S25-S28 dört ayrı iç hacimde geçiyor ve dördü de filmde bir kez
> görünüyor. Tek sayfada kilitlenmezse dört ayrı gemi gibi çıkarlar.

```
Photorealistic INTERIOR REFERENCE SHEET of four connected compartments
of ONE spacecraft, 16:9, maximum resolution. One frame divided into FOUR
CLEAN PANELS separated by thin neutral mid-grey gutters, in two rows of
two. All four compartments belong to the same ship and share one
material language. No humans anywhere on the sheet.

SHARED MATERIAL LANGUAGE — IDENTICAL IN ALL FOUR PANELS: ribbed
structural walls in worn off-white composite over graphite-grey frames;
machined aluminium handholds and grab rails at regular intervals;
recessed amber-white light panels behind frosted covers; exposed conduit
runs with banded couplings; scuffed deck rails with boot-clip sockets;
soft dust and long-use wear in every corner. Everything is built for
zero gravity: no up or down cues, stowage on all surfaces. No markings,
no numbers, no labels.

PANEL 1 — TOP LEFT, DOCKING TUNNEL: a narrow tunnel 80 centimetres wide,
seen straight down its axis, ribbed walls closing in, handholds running
along both sides, a heavy hatch with a machined wheel at the near end
and a second hatch standing OPEN at the far end with warm amber-white
light flooding through it up the tunnel. Cold steel tones near, warm
light far.

PANEL 2 — TOP RIGHT, EQUIPMENT BAY: a small compartment with SUIT RACKS
along the ribbed walls — empty moulded cradles, helmet clips, tethers
hanging slack — a deck rail with boot-clip sockets underfoot, warm
amber-white overhead panels. The air reads cold: the space is powered
but not yet warm.

PANEL 3 — BOTTOM LEFT, OBSERVATION CUPOLA: a small bowl-shaped
observation station of FIVE fused windows set in a machined frame, seen
from inside looking out; a deck ring with boot-clip sockets at its base,
handholds around the rim. Beyond the glass, plain neutral grey for
reference. The glass is clean and optically clear with no tint.

PANEL 4 — BOTTOM RIGHT, MAIN CORRIDOR: a long corridor running away from
camera down its axis, ribbed walls, a handrail along one side, recessed
amber-white light panels spaced down its length, stowage netting and the
soft clutter of a long-inhabited but presently empty vessel, the far end
warmer and out of focus.

Camera and light across the sheet: warm amber-white practical lighting
at 3200K in panels 1, 2 and 4; cooler neutral light in the cupola; soft
fill throughout so surfaces, seams and wear all read.

Negative: all four compartments belong to ONE ship and share the same
materials, colour and construction — no style change between panels. No
humans, no figure, no silhouette, no reflected face in any glass.
Exactly FIVE fused windows in the cupola. NO readable text, letters,
digits, numbers, icons, signage or screen graphics anywhere — no labels
on hatches, racks or panels. No holograms, no floating interfaces, no
glowing blue UI. 0% bloom, no glow filter — light panels are lit shapes,
not halos. No captions, arrows, callouts or watermarks on the sheet or
in the gutters. No stylisation, no CGI render aesthetic, no video game
look. Photorealistic with 35mm film grain.
```

---

# 🔧 BÖLÜM 7 — KULLANIM

```
A) REFERANS DESTEKLİ ÜRETİM (tercih edilen) Runway Gen-4 References /
Veo Ingredients / Kling referans girişi: sahne promptunu yapıştır +
ilgili SAYFANIN TAMAMINI referans olarak yükle (eşleme tablosu §2).
Metin çapası promptta kalır — silme. Referans ile metin çeliştiğinde
metni düzelt, referansı değil.

B) I2V ZİNCİRİ (referans girişi yoksa) Sahnenin 📸 IMAGE promptunu
referans sayfasıyla birlikte üret → çıkan kareyi onayla → o kareyi
başlangıç karesi olarak 🎥 VIDEO promptuna ver. Luma/Runway I2V başlangıç
karesini korur.
⚠️ Onaylanmamış imajdan video üretme (KILAVUZ_REHBERI §6 adım 5).

C) SEED KİLİDİ Her sayfanın seed'ini §1 tablosuna YAZ. Aynı seed + aynı
metin, varyasyon ürettiğinde ilk bakılacak yer burasıdır.

D) PANEL KIRPMA Sayfayı üret, panelleri ayrı dosya olarak kırp:
RA_p6_HASARLI.png · RK1_p3_VIZOR.png · RB_p3_KONI.png Tek panel
gerektiğinde kırpılmışı yükle; kural yine aynı — hangi panelin hangi
sahneye gittiği §2 tablosunda.
```

---

# ✅ BÖLÜM 8 — DEVAMLILIK KAPISI

> Referans sayfaları üretildikten sonra, sahne üretimine geçmeden önce.
> Bir madde bile ☒ ise o sayfa yeniden üretilir.

```
RA — LANDER
□ Altı panelin altısında aynı araç mı? (oranlar, faset hatları, şevron
yolu)
□ Kuyrukta TAM 2 lüle, karında TAM 4 lüle, TAM 4 bacak, probda TAM 3
kanat
□ Panel 5 ile panel 6 farkı YALNIZCA hasar mı?
□ Panel 5 ve 6'da bacaklar GERÇEKTEN kapalı, karın hattı düz mü? →
S7'nin 4,5. saniyesinden sonraki 9 sahnenin çapası bu iki panel
□ Silindir/roket/kapsül/kanatlı uçak siluetine kaymış mı?  → kaydıysa at
□ Hiçbir panelde insan, alev, duman, yazı var mı?          → varsa at

RK1 / RK2 — KARAKTERLER
□ Beş panelde aynı yüz mü? (kemik yapısı, kaş yarası / sakal dağılımı)
□ İki sayfa YAN YANA konduğunda iki AYRI insan okunuyor mu?  ⭐ en kritik
□ Boy farkı (1.70 ↔ 1.82) panel 4'lerde okunuyor mu?
□ Sırt DÜZ mü — hiçbir panelde sırt ünitesi var mı?        → varsa at
□ Vizörde renk/aynalama/yansıma/HUD var mı?                → varsa at
□ Panel 5'te kask gerçekten ÇIKMIŞ ve elde/rafta görünür mü?

RB — ANA GEMİ
□ TAM 6 modül, TAM 2 radyatör kanadı, TAM 4 füzyon lülesi, TAM 4 mandal
□ Panel 1'de lander siluetiyle ölçek farkı (≈1/15) okunuyor mu?
□ Gemi mekik boyutuna küçülmüş mü?  → küçüldüyse at
□ Dönen halka / santrifüj var mı?                          → varsa at
□ Panel 4'te 3 kapalı + 1 yarı yolda takılı mı?

RI1 / RI2 — MEKANLAR
□ RI1'de iki koltuk, solda pilot / sağda mühendis
□ Yakıt göstergesinde TAM 10 yuva, 8 sönük + 2 yanık okunuyor mu?
□ Hiçbir panelde rakam, harf, ekran grafiği, hologram var mı? → varsa at
□ RI2'nin dört bölmesi aynı gemiye mi ait görünüyor?

HEPSİ
□ Sayfada ve ara boşluklarda yazı/etiket/ok/filigran YOK
□ Seed §1 tablosuna yazıldı
```

---

# 📌 SONRAKİ ADIM

```
Bu paket üretilip §8 kapısından geçtikten sonra sahne üretimi başlar:
S12 (patlama) → S21 (temas) → S22 (mandallar) → S25 (tünel) Kapı
sahneleri THE_COLD_BURN_PLAN.md → ÜRETİM PLANI bölümünde.

⚠️ Bu dosya 07.08.2026'da açıldı. Sebebi tek cümleyle: 60 promptta
kelimesi kelimesine aynı metin, aracın her sahnede yeniden
tasarlanmasını engellemedi. Metin çapası gerekli ama yeterli değil —
görsel çapa şart. Bu bulgu 3-5 dk formatının dosya listesini de
değiştiriyor: PLAN + PART_A + PART_B + KAPAK + **REFERANS_PAKETI**.
```
