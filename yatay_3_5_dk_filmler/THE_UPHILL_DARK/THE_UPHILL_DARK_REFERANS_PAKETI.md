# 🎯 THE UPHILL DARK — REFERANS PAKETİ

## Gemi · Yanaşma Yeri · Kapsül · Kabin · Karakterler
### 5 birleşik referans sayfası · **her sayfada TAM 4 PANEL** (20 panel)

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR.** Üretim sırası:
> **bu dosya → onay → seed kilidi → PART_A / PART_B sahneleri.**
>
> ⭐ **Format kararı (17.08.2026):** paket ilk yazıldığında varlık başına
> TEK görseldi — 13 üretim. Şimdi **varlık başına TEK SAYFA, sayfa başına
> TAM 4 PANEL** — 5 üretim. Gerekçe ve bedeli §0'da; kaybedileni geri
> alan üç önlem de orada.
>
> Tüm promptlar **Ders 34** uyumlu: karakter adı hiçbir promptta geçmez.
> Tüm promptlar **Ders 79 + 95** uyumlu: sırt düz, vizör berrak ama
> **görünür** (çerçeve + yaka mührü + tek parlama çizgisi).
> Tüm promptlar **yazısızdır**: sayfada, panelde, oluklarda 0 harf.

---

# 0. ⚠️ NEDEN BU DOSYA VAR — VE NEDEN 5 SAYFA

```
ÖLÇÜLMÜŞ SEBEP (Cold Burn, 07.08.2026): dört varlığın tanımı 60 promptta
KELİMESİ KELİMESİNE aynı yazıldı — ve yetmedi. Metin çapası modelin aynı
CÜMLEYİ okumasını sağlar, aynı NESNEYİ çizmesini sağlamaz. Text-to-video
her çağrıda gövde oranlarını yeniden uydurur: 25 sahne = 25 farklı gemi.

BU FİLMDE RİSK DAHA YÜKSEK, ÇÜNKÜ GEMİNİN GÖVDESİ SAYAÇTIR.
Filmin mesafe anlatımı tek bir şeye dayanıyor: pencerede HANGİ bölümün
olduğu (motor bloğu → gölge kalkanı → radyatör → omurga → yakıt küreleri
→ yuva). Gemi sahneden sahneye yeniden tasarlanırsa merdivenin basamakları
karışır ve film "iki kişi bir şeyin yanında duruyor"a döner — Tidal Hunt'ın
sayacını kaybetme biçiminin gemi ölçeğindeki hâli [D50 · D78].

⭐ Bu yüzden RA (gemi) bu paketin en yüksek öncelikli sayfasıdır;
   karakterlerden bile önce onaylanır.
```

```
FORMAT KARARI — 13 TEK GÖRSEL → 5 SAYFA × 4 PANEL

BEDELİ (dürüst hâli): panel sayfasının iki bilinen açığı var.
  ① Sayfa modele "bu bir çizim tablosu" diye okunur; panel araları
     metin / ok / etiket / ölçü çizgisi üretmeye açıktır.
  ② Her panel karenin dörtte birine düşer — varlık başına çözünürlük
     dörtte bire iner.

KARŞILIĞI: 13 üretim yerine 5 üretim; ve panel sayfasının TEK GÖRSELDE
OLMAYAN bir kazancı var — AYNI SAYFADAKİ İKİ DURUM AYNI ÇAĞRIDA ÇİZİLİR.
Bu filmin iki kritik karşılaştırması tam olarak budur:
  · yanaşma yeri AÇIK ↔ KAPALI  (RB p1 ↔ p2)  — tek fark kolların durumu
  · kapsül YÜKLÜ ↔ BOŞ KIZAK    (RC p1 ↔ p3)  — tek fark yük ve kayış
13 ayrı üretimde bu iki çift AYRI çağrılardı ve gövdenin aynı kalacağının
garantisi yoktu. Şimdi aynı karede, aynı çağrıda, yan yana çıkıyorlar.
Filmin bedeli RC p1 ile p3 arasındaki farktır — o fark artık ölçülebilir.

AÇIKLARI KAPATAN ÜÇ ÖNLEM (her promptta uygulanmıştır):
  ① Oluk dili: "thin neutral mid-grey gutters" — oluk bir AYIRICI olarak
     tanımlanır, bir yerleşim alanı olarak değil.
  ② Negatifte oluk ADIYLA geçer: "no text, labels, captions, arrows,
     callouts, dimension lines, panel titles or watermarks anywhere on
     the sheet OR IN THE GUTTERS."
  ③ "maximum resolution" + 16:9 + panel başına tek varlık; §4 kapısına
     "panel içi detay okunuyor mu" maddesi eklendi. Okunmuyorsa sayfa
     atılır ve o varlık TEK GÖRSEL olarak yeniden üretilir (kaçış yolu
     §3-F'de).
```

---

# 1. 📋 ÜRETİM SIRASI VE SEED TAKİP TABLOSU

| # | Referans sayfası | Panel | Ne | Öncelik | Seed | Durum |
|---|---|:---:|---|:---:|---|:---:|
| **RA** | GEMİ SAYFASI | 4 | yan · üç çeyrek+ölçek · alev · orta gövde | 🔴 ZORUNLU | | ☐ |
| **RB** | YANAŞMA YERİ SAYFASI | 4 | açık · kenetli · yuva detay · bağlam | 🔴 ZORUNLU | | ☐ |
| **RC** | KAPSÜL DIŞI SAYFASI | 4 | yüklü · alttan · boş kızak · kayış detay | 🔴 ZORUNLU | | ☐ |
| **RD** | KAPSÜL İÇİ SAYFASI | 4 | kabin · konsol · seçici · kol+kordon | 🔴 ZORUNLU | | ☐ |
| **RE** | KARAKTER SAYFASI | 4 | pilot · mühendis · ⭐ikisi · iki yüz | 🔴 ZORUNLU | | ☐ |

```
ÜRETİM SIRASI — kapı kapı, atlama yok:

RA   GEMİ ÖNCE. Gövdesi filmin sayacıdır; 21 sahnede var.
     Onaylanmadan hiçbir sahne üretilmez.
RB   Yanaşma yeri: doruğun geometrisi burada donar. p1 ↔ p2 farkı
     YALNIZCA kolların durumu olmalı — aynı sayfada olduğu için
     ölçülebilir.
RC   Kapsül: p1 ↔ p3 farkı YALNIZCA yük ve kayış olmalı. Bu iki panelin
     farkı filmin bedelidir; başka bir fark varsa sayfa atılır.
RD   Kabin: 13 sahnenin kadrajı burada standartlaşır.
RE   ⭐ İKİ KARAKTER TEK SAYFADA — bu sayfa aynı zamanda KLON KAPISIDIR.
     p3 ve p4 iki figürü aynı karede yan yana koyar. Ayrışmıyorlarsa
     sayfa reddedilir ve yeniden üretilir (bkz. §4 kapı).
     Depodaki üç klon vakasının (Stone Sky · Unbroken City ·
     Starless Circle) üçü de bu iki panelle yakalanabilirdi.
```

---

# 2. 🗺️ SAHNE → REFERANS EŞLEME

> Sahne üretirken **ilgili sayfanın TAMAMINI** yükle — model sayfadaki
> bütün panelleri görür, tek panel kırpıp yüklemekten daha güçlü çapadır.
> Parantez içindeki panel numarası "hangi panel bu sahnenin kadrajıdır"
> demektir, "yalnız onu yükle" demek değildir.

| Sahne | Yüklenecek referans | Kadraj paneli |
|---|---|---|
| S0 · S24 | **RA** | p1 · p2 · p3 (gemi tam boy, ölçek, alev) |
| S1 · S2 | **RD + RE** | RD p1 + RE p1·p2 (kabin + iki karakter) |
| S3 · S8 · S14 · S17 | **RD** | p2 · p3 (kartuş atışı — konsol ve seçici) |
| **S4** | **RA + RC** | RA p3 + RC p1 (alevin yanında kapsül) |
| S5 · S13 | **RE** | p4 (yüz yakın planı, kasklı) |
| S6 · S15 · S16 · S20 | **RA + RC** | RA p1·p4 + RC p1 (gövde pencerede akıyor) |
| S7 · S9 · **S10** | **RA** | p1 · p4 (radyatör kanadı geometrisi) |
| S11 | RA + RC | RA p1 + RC p1 (yanal öteleme) |
| **S12** | **RB** | p4 → p1 (yuva ilk kez görünür) |
| S18 | RB + RC | RB p1 + RC p1 (16 m altında asılı) |
| **S19** | **RC + RD** | RC p1·p3·p4 + RD p4 (dolu → boş kızak + turuncu kol) |
| **S21** | **RB** | p1 → p2 (temas: kollar açıktan kapalıya) |
| S22 | RB + RD | RB p2 + RD p1 (kenetli + kabin) |
| **S23** | **RC** | p3 (boş kızak — bedelin görüntüsü) |

---

# 🛰️ RA — GEMİ SAYFASI 🔴

> **Bu sayfa filmin sayacıdır.** p1'de altı bölüm pruvadan kıça DOĞRU
> SIRAYLA ve DOĞRU ORANDA okunmazsa pencere merdiveni çalışmaz.
> Ölçek kilidi [D32] p2'de, vakum alevi [D36] p3'te donar.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one single
spacecraft, 16:9 widescreen, maximum resolution. One frame divided into
FOUR CLEAN PANELS separated by thin neutral mid-grey gutters, in two rows
of two. Every panel shows THE SAME ONE SHIP from a different angle or in
a different state. No humans anywhere on the sheet. Plain neutral
mid-grey seamless background in every panel, even neutral key light at
5000K with soft fill so every surface reads.

THE SHIP — IDENTICAL IN ALL FOUR PANELS: a 210-metre interstellar
crossing vessel, a long working machine built for a passage between stars
— not a shuttle, not a warship, not a saucer. From bow to stern, in this
exact order and these exact proportions:

1) BOW ICE SHIELD, 0 to 24 metres: a blunt disc 26 metres across, dirty
   grey ablative composite, its forward face pitted and scoured with
   thousands of tiny impact craters, its rim chipped. It is a shield, not
   a dish, not an antenna: solid, thick, featureless.
2) THREE HABITAT DRUMS, 24 to 60 metres: three cylinders in a line, each
   18 metres across and 12 metres long, wrapped in dirty-white quilted
   multi-layer insulation with visible quilting seams, taped edges, sun
   yellowing on the upper side and grey staining below.
3) FOUR PROPELLANT SPHERES, 60 to 92 metres: four bare machined metal
   spheres in a row, each 9 metres across, held in ring cradles, their
   lower surfaces streaked with frost and their weld seams visible.
4) THE BERTH BOOM at 100 metres: a machined lattice boom standing 12
   metres straight out from the near flank, square in section, carrying a
   flat pad at its outer end; a 2.0-metre machined capture ring is set
   into the UNDERSIDE of that pad, facing down, with three curved capture
   arms standing open around it.
5) OPEN TRUSS SPINE, 104 to 150 metres: a bare hexagonal lattice of
   machined graphite-grey members with bolted nodes, cable runs clipped
   along it.
6) TWO RADIATOR WINGS, 150 to 166 metres: two dead-black knife-edge
   panels standing straight out from the spine on opposite sides, each 40
   metres long and only 30 centimetres thick, their surfaces matte and
   light-swallowing.
7) SHADOW SHIELD, 166 to 182 metres: a dull grey cone 30 metres across,
   its wide face turned toward the stern.
8) DRIVE BLOCK, 182 to 210 metres: a dense armoured mass with THREE
   deeply recessed engine nozzles in a triangle, their throats scorched.

FINISH — IDENTICAL EVERYWHERE: worn and used — micrometeorite pitting,
sun-yellowed insulation, grey thruster staining, chipped paint, heat
discolouration to straw and blue-grey near the nozzle throats. No
markings, no numbers, no insignia, no flags, no logos anywhere on the
hull.

PANEL 1 — TOP LEFT, FULL SIDE ELEVATION, ENGINES COLD: exact 90-degree
side elevation, the whole vessel filling the panel end to end, its long
axis horizontal, bow at panel-left and stern at panel-right, so all eight
sections read in order at their correct proportions. The drive is cold
and unlit in this panel: no plume of any kind.

PANEL 2 — TOP RIGHT, THREE-QUARTER BOW WITH SCALE REFERENCE: the same
ship seen from ahead and slightly above, its bow toward panel-left and
its stern receding toward panel-right, so the depth of the truss and the
standoff of the berth boom both read. A single small ferry capsule holds
station 40 metres off the ship's near flank, level with the berth boom —
a 5.2-metre truncated cone standing nose-up, 3.6 metres across its flat
base, matte grey-white composite, with a 60-centimetre docking probe on
its nose. It must read as roughly ONE FORTIETH of the ship's length: the
capsule is shorter than one propellant sphere is wide, and one radiator
wing alone is nearly eight times the capsule's height. Both craft are
unpowered and unlit in this panel.

PANEL 3 — BOTTOM LEFT, DRIVE BLOCK UNDER POWER: the armoured stern mass
alone, seen from below and to one side at 60 metres, filling the upper
part of the panel with its exhaust running away toward the panel's lower
edge, against deep black space with sharp pinpoint stars — the only panel
on the sheet with a black background. The THREE recessed nozzles, each
throat 4 metres across with its inner bell scorched dark, produce three
pale blue-white exhaust cones that merge within 20 metres into a single
straight lance about 400 metres long, running dead straight away from the
ship and thinning steadily until it fades to nothing. In vacuum it is
sharply defined at its edges near the throats and diffuse only at its far
end. It does not billow, does not curl, does not mushroom, does not roll,
does not form smoke, and never bends. It is a hard directional light
source: it throws pale blue light onto the underside of the drive block
and the shadow shield, leaving every surface facing away from it in
absolute black with a razor-sharp shadow edge. No atmospheric haze
anywhere, no light scattering in the empty space around the lance.

PANEL 4 — BOTTOM RIGHT, MIDSHIP CLOSE — THE WINDOW LADDER: the middle of
the ship seen square-on from 60 metres, filling the panel from the fourth
propellant sphere at panel-left to the root of the first radiator wing at
panel-right, so four rungs of the ladder read together and in order:
sphere → berth boom standing 12 metres out with its socket facing DOWN →
open hexagonal truss spine with bolted nodes and clipped cable runs →
black knife-edge radiator wing rising out of frame. This is the exact
scale at which the hull passes the capsule's window in the film: close
enough that quilting seams, bolt heads, frost streaks and grab rails read
individually, far enough that four sections fit in one frame.

NEGATIVE: ONE ship only per panel — no second vessel, no fleet, no
variant designs on the sheet; panel 2's small ferry capsule is the only
other craft anywhere and it appears in that panel alone. The architecture
is IDENTICAL in all four panels — same order, same proportions, no extra
module, no missing section, no morphing between panels. Exactly THREE
habitat drums, exactly FOUR propellant spheres, exactly TWO radiator
wings, exactly THREE engine nozzles, exactly THREE capture arms — these
counts never change. The ship never rotates and has no spinning ring, no
centrifuge, no wings, no sails, no dish antenna. The size relation in
panel 2 never changes: the capsule is never shuttle-sized, never half the
ship, never larger than one habitat drum. No humans, no crew, no figure
at any window, in any panel. Panels 1, 2 and 4 carry NO engine plume, no
fire, no exhaust, no glow of any kind — the drive is cold there; panel 3
carries exactly ONE merged exhaust lance and nothing else: no smoke, no
billowing, no curling, no mushroom cloud, no turbulence, no shock
diamonds spreading sideways, no sparks, no debris, no explosion, no fire
of any other colour, and the exhaust never swirls or behaves like a
liquid. No readable text, letters, digits, numbers, insignia, labels,
captions, arrows, callouts, dimension lines, blueprint grid, panel titles
or watermark anywhere on the sheet OR IN THE GUTTERS. 0% bloom, no glow
filter, no lens flare, no soft focus — surfaces keep visible texture
inside the blue light. No stylisation, no illustration, no blueprint
look, no CGI render aesthetic, no video game look. Photorealistic with
35mm film grain.
```

---

# 🔩 RB — YANAŞMA YERİ SAYFASI 🔴

> **Doruğun geometrisi bu sayfadadır.** Yuva AŞAĞI bakar; kapsül altından
> yükselip oturur. Cold Burn'ün drog konisi + 4 mandalından bilinçli
> olarak ayrıdır.
> ⛔ p1 ile p2 arasındaki tek fark **kolların durumu ve oturmuş prob**
> olmalıdır — başka hiçbir şey değişmez. İkisi aynı sayfada olduğu için
> bu artık ölçülebilir bir kapıdır.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one docking berth on
the flank of a large spacecraft, 16:9 widescreen, maximum resolution. One
frame divided into FOUR CLEAN PANELS separated by thin neutral mid-grey
gutters, in two rows of two. Every panel shows THE SAME ONE BERTH from a
different angle or in a different state. No humans anywhere on the sheet.
Deep black space background with sharp pinpoint stars in every panel;
even neutral key at 5000K plus the berth's own light.

THE BERTH — IDENTICAL IN ALL FOUR PANELS: a machined lattice boom, square
in section and 1.6 metres on a side, standing 12 metres straight out from
the hull of a large vessel; the hull itself reads at the inboard end of
the boom as a wall of dirty-white quilted insulation and bare machined
propellant sphere. At the boom's outer end is a flat structural pad 4
metres square. Set into the UNDERSIDE of that pad, facing straight down,
is the socket:

  - a 2.0-metre machined capture ring, its brushed metal face worn pale
    and polished smooth by use, with shallow guide grooves cut radially
    into it;
  - at its centre a 40-centimetre conical throat, dark inside, its lip
    chamfered and scuffed;
  - THREE curved capture arms spaced evenly at 120 degrees around the
    ring, each arm 1.1 metres long, hinged at its base, their hinge pins,
    actuator rods and wear marks clearly visible;
  - a continuous recessed light channel running all the way around the
    socket's outer rim, a thin unbroken line of warm white light at 3400K
    set deep in its groove so no lamp is visible, throwing a clean pool of
    warm light down onto the arms and leaving the boom lattice above in
    cold neutral tones.

Machine detail everywhere and identical in every panel: bolt heads, hinge
pins, hand-worn grab rails along the boom, dust staining in the corners,
chipped paint on the arm edges. No markings, no numbers, no labels of any
kind.

PANEL 1 — TOP LEFT, WAITING STATE, ARMS OPEN: the camera sits 14 metres
below the berth and slightly to one side, looking up at its underside, so
the whole socket assembly reads from beneath. All THREE capture arms
stand FULLY OPEN, angled outward and downward like the legs of a tripod.
Nothing is docked: no probe in the throat, no capsule anywhere in the
panel. The warm light pool falls on the open arms and on empty black
space beneath them.

PANEL 2 — TOP RIGHT, SEATED STATE, ARMS CLOSED: exactly the same camera
position, distance and angle as panel 1 — 14 metres below and slightly to
one side, looking up. A 60-centimetre docking probe with three alignment
vanes has risen into the throat from below and is seated to full depth;
the vanes have rotated into their guide grooves and sit flush. The THREE
capture arms have swung inward and are now CLOSED over the probe's
collar, all three seated home and identical to one another, their
actuator rods drawn in, their hinge pins loaded. Below the ring, the top
1.5 metres of a ferry capsule's nose is visible: matte grey-white
composite with crisp recessed seams and flush rivet rows, pressed up
against the ring so the two machined faces meet with a clean structural
boundary and a visible 1-centimetre seam line between them — the metal
does not merge, blend or melt into the ring at any point. Fine paint
flakes and dust knocked loose by the contact hang for an instant beside
the joint, each falling straight down out of the panel under thrust.
NOTHING ELSE differs from panel 1: same boom, same pad, same ring, same
grooves, same light channel, same wear.

PANEL 3 — BOTTOM LEFT, SOCKET DETAIL, ARMS OPEN: an 85mm close view from
3 metres directly beneath the socket, the ring filling the panel. The
radial guide grooves, the chamfered and scuffed lip of the 40-centimetre
conical throat, the dark interior of the throat, and ONE capture arm's
full mechanism — hinge pin, knuckle, actuator rod and the bright wear
band where the arm rides — all read individually. The recessed light
channel is a thin lit line deep in its groove, not a halo. No probe, no
capsule, nothing docked.

PANEL 4 — BOTTOM RIGHT, THE BERTH IN CONTEXT: a wide view from 50 metres
below and forward, showing where the boom meets the ship: dirty-white
quilted habitat insulation and one bare machined propellant sphere at
panel-top, the lattice boom standing 12 metres clear of that flank, and
the socket at its outer end facing straight DOWN into empty black space,
arms open, its warm light channel a small bright ring at this distance.
This panel locks the standoff and the direction the socket faces; nothing
is docked in it.

NEGATIVE: ONE berth only, in every panel — no second berth, no variant
socket design, no alternative geometry on the sheet. Exactly THREE
capture arms, exactly ONE capture ring, exactly ONE conical throat,
everywhere. The arms are OPEN in panels 1, 3 and 4 — none closed, none
folded over the throat — and CLOSED in panel 2 — none open, none at half
travel, none bent, none missing. Exactly ONE probe with exactly THREE
alignment vanes, and it appears in panel 2 only. The socket always faces
DOWN in every panel; it is never on the side of the hull, never facing
forward, never rotated. The boom, pad, ring, grooves, light channel and
wear are IDENTICAL across all four panels — no morphing, no redesign, no
changed proportion between panels. In panel 2 the probe and the ring keep
a clear rigid structural boundary at the joint — no merging, no phasing,
no melting, no blending of surfaces. No humans, no figure, no hands, no
face at any window, in any panel. No engine plume, no fire, no exhaust,
no sparks, no explosion, no debris field. No holograms, no floating
interfaces, no blue user interface, no indicator digits. No readable
text, letters, digits, numbers, insignia, labels, captions, arrows,
callouts, dimension lines, panel titles or watermark anywhere on the
sheet OR IN THE GUTTERS. 0% bloom, no glow filter — the light channel is
a thin lit line, not a halo. No stylisation, no illustration, no CGI
render aesthetic, no video game look. Photorealistic with 35mm film
grain.
```

---

# 🚀 RC — KAPSÜL DIŞI SAYFASI 🔴

> Filmin ikinci en çok kayan varlığı.
> ⛔ **p1 ile p3 arasındaki fark YALNIZCA yüktür.** Gövde, pencere, prob,
> lüleler, dikişler birebir aynı olmalı. **Filmin bedeli bu iki panelin
> arasındaki farktır** — ve artık iki panel aynı karede yan yana.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one single small
spacecraft, 16:9 widescreen, maximum resolution. One frame divided into
FOUR CLEAN PANELS separated by thin neutral mid-grey gutters, in two rows
of two. Every panel shows THE SAME ONE CAPSULE from a different angle or
in a different load state. No humans anywhere on the sheet. Plain neutral
mid-grey seamless studio background in every panel, even neutral key at
5000K with soft fill so every seam and rivet reads.

THE CAPSULE — IDENTICAL IN ALL FOUR PANELS: a 5.2-metre truncated cone
ferry capsule, 3.6 metres across its flat circular base and 2.1 metres
across its flat top face. It is not a rocket, not a winged shuttle, not a
sphere: a short blunt cone standing on its base. Matte machined grey-white
composite panels with crisp recessed seams and visible flush rivet rows,
laid over an exposed graphite-grey structural frame that shows at every
panel joint.

  - NOSE: a 60-centimetre docking probe standing straight up from the
    centre of the flat top face, with THREE small alignment vanes spaced
    evenly around it near its tip.
  - WINDOW: one wide curved window set into the upper cone below the top
    face, 1.6 metres across and 0.6 metres tall, in a worn machined metal
    frame, its glass clean and optically clear with no tint.
  - BASE: a machined ring at the bottom carrying FOUR main engine nozzles
    spaced evenly at 90 degrees, each throat 0.4 metres across and
    scorched dark inside, with cooling lines and machined feed pipes
    running to each one across the base plate.
  - SMALL THRUSTER CLUSTERS: four small square manoeuvring thruster
    clusters set flush into the flank near the base and four more near
    the top face, each cluster showing four tiny recessed ports.
  - NEAR FLANK, LOW: a cartridge rack of SIX cylindrical sockets in a
    single horizontal row, each socket 0.3 metres across, machined into a
    single frame with a hinged retaining bar and plain unmarked collars.
  - FAR FLANK, MID: the cargo cradle — a machined rack sized for FORTY
    identical sealed white core tubes in five rows of eight, each tube 0.9
    metres long and 0.12 metres across, with ONE single wide BURNT-ORANGE
    strap running across the whole rack through a machined buckle.

FINISH — IDENTICAL EVERYWHERE: used and worn — scuffs on the base ring,
grey staining around the nozzles, hairline scratches across the flanks,
dust in the seams. The only saturated colour anywhere on the craft is the
single burnt-orange cargo strap. No markings, no numbers, no insignia, no
logos. The engines are cold and unlit on the whole sheet.

PANEL 1 — TOP LEFT, SIDE ELEVATION, LOADED: exact 90-degree side
elevation, the craft standing nose-UP with its long axis vertical,
filling the panel's height. THE LOADED STATE: the cargo cradle holds all
FORTY core tubes, packed tight in five rows of eight and held down by the
one burnt-orange strap drawn tight through its buckle. The cartridge rack
shows SIX sockets, EVERY ONE OF THEM LOADED with a white cylindrical
cartridge seated flush. This is the configuration for every scene from
the opening until the release.

PANEL 2 — TOP RIGHT, LOW THREE-QUARTER FROM BENEATH: the same capsule
seen from beneath and to one side, standing nose-up so its base ring
dominates the panel and its flank recedes upward. The FOUR main nozzles
read individually, their bells deeply scorched and heat-discoloured to
straw and blue-grey, with their cooling lines and feed pipes across the
scuffed grey-stained base plate. On the near flank the cartridge rack is
seen square: in THIS panel FOUR sockets hold white cartridges seated
flush and TWO sockets are EMPTY, showing their dark machined interior,
the ejector rod at the back and the scorching around the mouth left by
firing — the difference between a loaded socket and an empty one is
unmistakable at a glance. Above the rack, the lower edge of the wide
curved window and its worn machined frame read in the receding flank.

PANEL 3 — BOTTOM LEFT, SIDE ELEVATION, EMPTY CRADLE: the same view, the
same distance and the same lighting as panel 1 — 90-degree side
elevation, nose-up, filling the panel's height. Every seam, scuff, stain
and scratch is identical to panel 1. THE TWO CHANGES, AND ONLY THESE TWO:
  - THE CARGO CRADLE IS EMPTY: the rack now shows FORTY empty moulded
    sockets in five rows of eight, their pale interiors clean where the
    tubes sat and grey-dusted at the edges where they did not. Not one
    tube remains. The clamp bar is open and swung back on its hinge.
  - THE ORANGE STRAP HANGS LOOSE: the single wide burnt-orange strap is
    still attached at one end to its machined buckle and hangs straight
    DOWN along the flank, slack and unloaded, its free end swinging clear
    of the empty rack. It is still the only saturated colour on the craft.
Additionally the cartridge rack on the near flank shows SIX sockets, ALL
SIX EMPTY and scorched at the mouth. Nothing else differs from panel 1.

PANEL 4 — BOTTOM RIGHT, CARGO CRADLE DETAIL, LOADED: an 85mm close view
from 1.5 metres square onto the cradle in its loaded state. The FORTY
sealed white core tubes read individually in their five rows of eight,
their end caps machined and dust-filmed. The one wide BURNT-ORANGE strap
crosses them under visible tension, its weave texture, its stitched
edges, its chipped machined buckle and the way it presses a shallow line
into the tube row all clearly readable. The rack's clamp bar is closed
and latched. The strap's paint-worn buckle is the mechanical anchor of
the release: it must read as a thing a gloved hand can throw.

NEGATIVE: ONE capsule only, in every panel — no second craft, no variant,
no exploded view, no alternative design on the sheet. The hull, window,
probe, seams, nozzles and wear are IDENTICAL in all four panels — no
redesign, no new panel, no changed proportion, no morphing between
panels. Exactly FOUR base nozzles, exactly SIX cartridge sockets, exactly
FORTY core tube positions, exactly ONE orange strap, exactly ONE probe
with THREE vanes — these counts never change. The load states are exactly
as specified: panel 1 six loaded cartridges and forty tubes, panel 2 four
loaded and two empty cartridges, panel 3 six empty cartridges and forty
empty sockets, panel 4 the loaded cradle — no panel mixes these states.
No core tube remains anywhere in panel 3 — not one, not a fragment; the
cradle was released, not destroyed, so no damage, no tear, no scorch mark
on the flank, no debris cloud. The craft is never a cylinder, never a
rocket, never a winged aeroplane, never a sphere, and never has landing
legs, wheels, wings, a parachute or heat shield tiles. No humans, no
figure, no face at the window, in any panel. No engine plume, no fire, no
exhaust, no sparks, no glow anywhere on the sheet — the craft is
unpowered in every panel. No readable text, letters, digits, numbers,
insignia, labels, captions, arrows, callouts, dimension lines, panel
titles or watermark anywhere on the sheet OR IN THE GUTTERS. 0% bloom, no
glow filter, no soft focus. No stylisation, no illustration, no blueprint
look, no CGI render aesthetic, no video game look. Photorealistic with
35mm film grain.
```

---

# 🎛️ RD — KAPSÜL İÇİ SAYFASI 🔴

> Filmin ana iç kadrajı p1'dedir; 13 sahne bu kadrajdan çekilir ve koltuk
> düzeni (SOL pilot / SAĞ mühendis) burada kilitlenir [D86].
> Filmin iki mekanik olayı — seçicinin bir diş ilerlemesi ve turuncu kolun
> çekilmesi — p3 ve p4'te donar. Kordonun DÜMDÜZ AŞAĞI sarkması filmin
> novum'udur: süzülüyorsa sayfa atılır.

```
Photorealistic INTERIOR REFERENCE SHEET of one single spacecraft cabin,
16:9 widescreen, maximum resolution. One frame divided into FOUR CLEAN
PANELS separated by thin neutral mid-grey gutters, in two rows of two.
Every panel shows THE SAME ONE CABIN, wide or in detail. No humans
anywhere on the sheet. Dim practical cabin lighting plus a soft neutral
fill in every panel so every surface still reads.

THE CABIN — IDENTICAL IN ALL FOUR PANELS: the cramped 2.4-metre-wide
interior of a small cone-shaped ferry capsule. TWO deep-bucketed seats
sit side by side, reclined so that anyone strapped into them faces UP
toward the window: the LEFT seat is the pilot's, the RIGHT seat is the
engineer's. Both are empty; their five-point harnesses hang slack over
the seat edges, the buckles resting where they fell. The seat shells are
worn graphite composite with abraded padding at the shoulder wings.

Ahead of and above the seats: ONE wide curved window, 1.6 metres across
and 0.6 metres tall, set in a heavy machined metal frame worn bright at
the handholds beside it. The glass is clean and optically clear with no
tint; beyond it, plain neutral grey for reference use.

THE CONSOLE, filling the space between the seats and the window: matte
dark grey panels with crisp recessed seams and flush fastener rows,
scuffed to bare metal along every edge a glove has touched. Rows of
ABSTRACT amber and pale grey light segments indicate fill level only by
how many are lit — no digits, no letters, no icons, no screens, no
graphics anywhere. Machined toggle guards worn shiny by gloved fingers. A
12-centimetre mechanical attitude ball sits in a machined bezel at the
centre of the console: a matt sphere carrying a single painted horizon
band, level, lit dimly from behind.

THREE OBJECTS THAT MUST READ CLEARLY AND IDENTICALLY WHEREVER THEY APPEAR:
  - A 40-centimetre plain brass lanyard hangs from the lower edge of the
    window frame at the centre of the cabin, ending in a plain machined
    toggle. It hangs perfectly straight DOWNWARD toward the base of the
    capsule, dead still and under tension, like a plumb line.
  - On the right cheek of the console, within the right seat's reach: a
    BURNT-ORANGE two-handed lever, 30 centimetres long, with a machined
    knurled grip at each end and a hinged steel safety collar folded back
    and clipped off it. It is the only saturated colour in the cabin.
  - On the left cheek of the console, within the left seat's reach: a
    machined rotary selector 9 centimetres across with SIX detent
    positions cut evenly into its collar and a stubby knurled lever arm,
    its detents worn bright.

Everywhere else: ribbed wall conduits, machined grab handholds, boot
rails on the floor, a sealed inner hatch low behind the seats, fine grit
resting in the floor seams. Everything worn and long-used.

PANEL 1 — TOP LEFT, THE MASTER FRAME: the camera sits low behind and
between the two empty seats, looking forward and slightly UP through the
window, exactly as the film's cockpit scenes are framed. Both seats, the
window, the full width of the console, the brass lanyard hanging dead
straight at centre, the orange lever on the right cheek and the selector
on the left cheek are all in this one frame. This panel is the standard
interior framing of the film.

PANEL 2 — TOP RIGHT, CONSOLE, 85mm FROM 0.8 METRES: tight across the
centre and right of the console, shallow depth of field with the machined
detail sharp. The abstract amber and pale grey light segment rows, the
attitude ball in its bezel at panel-left, the orange lever standing up
from the console cheek at panel-right, and the lower length of the brass
lanyard crossing the upper part of the panel all read. Fine grit sits in
the console seams; a machined grab handhold worn bright runs along the
console's outer edge.

PANEL 3 — BOTTOM LEFT, THE SELECTOR, MACRO: a 100mm macro view from 0.4
metres straight onto the rotary selector alone, filling the panel. All
SIX detent positions read individually as clean machined cuts in the
collar; the stubby knurled lever arm stands at the FIRST position; the
collar is worn bright between the notches where the arm has travelled;
beside each detent sits a plain machined dimple — no marking, no number,
no letter, no dot of paint. The mechanism must read as a thing a gloved
thumb advances one notch at a time.

PANEL 4 — BOTTOM RIGHT, THE ORANGE LEVER AND THE LANYARD: a 100mm view
from 0.5 metres holding both objects in one frame — the BURNT-ORANGE
two-handed lever standing up from the console cheek, its paint chipped
along both knurled grips down to bare metal, its hinged steel safety
collar folded back and clipped off it; and beside it the 40-centimetre
plain brass lanyard hanging from the window frame above, straight DOWN
and under tension, dead still, its plain machined toggle hanging free 5
centimetres above the console lip. The lever must read as needing two
gloved hands. The lanyard must read as a plumb line, not as something
floating.

NEGATIVE: ONE cabin only, in every panel — no second cabin, no variant
layout, no alternative console design on the sheet. Exactly TWO seats,
pilot LEFT and engineer RIGHT, never swapped, never three seats, never
one. Exactly SIX detents on the selector, exactly ONE orange lever,
exactly ONE brass lanyard, exactly ONE attitude ball — identical in
shape, wear and position wherever they appear, with no morphing between
panels. The lanyard hangs straight down in every panel and is never
floating, never drifting sideways, never slack, never coiled, never
swinging. No humans, no figure, no hands, no gloves, no reflected face in
the glass, in any panel. No readable text, letters, digits, numbers,
icons, glyphs, screen graphics or labels anywhere on any panel or surface
— abstract light segments, machined dimples and one mechanical ball only.
No holograms, no floating interfaces, no blue user interface. No captions,
arrows, callouts, dimension lines, panel titles or watermark anywhere on
the sheet OR IN THE GUTTERS. 0% bloom, no glow filter — lit segments are
small lit shapes, not halos. No stylisation, no illustration, no CGI
render aesthetic, no video game look. Photorealistic with 35mm film grain.
```

---

# 👥 RE — KARAKTER SAYFASI 🔴

> ⛔ **Bu sayfa aynı zamanda bir DENETİMDİR.** p3 ve p4 iki figürü aynı
> karede yan yana koyar; amaçları iki insanın ayrışıp ayrışmadığını
> üretimden ÖNCE ölçmektir. Ayrışmıyorlarsa sayfa reddedilir ve yeniden
> üretilir. Depodaki üç klon vakasının (Stone Sky · Unbroken City ·
> Starless Circle) üçü de bu iki panelle yakalanabilirdi.
>
> Yüz çapası bu sayfadadır. Vizör **berrak ama görünür** olmalı: çerçeve +
> yaka mührü + tek parlama çizgisi [D95]. Sırt DÜZ [D79].

```
Photorealistic CHARACTER REFERENCE SHEET of TWO different people in
pressure suits, 16:9 widescreen, maximum resolution. One frame divided
into FOUR CLEAN PANELS separated by thin neutral mid-grey gutters, in two
rows of two. Exactly TWO people exist on the whole sheet and they are two
clearly different individuals. Neutral studio lighting in every panel:
soft even key at 5000K with gentle fill, plain mid-grey seamless
background, shadows soft but present.

PERSON A — THE TALLER ONE, IDENTICAL WHEREVER HE APPEARS: a man, 54 years
old, 1.75 metres tall, lean and wiry with narrow shoulders. Weathered
pale olive skin with clearly visible pore texture, deep sun lines across
the forehead and at the outer corners of both eyes, and natural
subsurface scattering — no airbrushing, no smoothing, no beauty
retouching. A THICK GREY MOUSTACHE completely covers his upper lip; he
has no beard and his cheeks and jaw are clean-shaven with visible grey
stubble shadow. His hair is close-cropped grey, receding at both temples.
His eyes are pale grey-brown, steady and tired. HIS ONE MARK: a
2-centimetre shiny burn scar ON THE BONE OF HIS RIGHT CHEEK, 2
centimetres below the outer corner of his right eye — it sits on the
cheekbone, not on his jaw, not on his temple, not on his brow. The rest
of his face is completely unmarked: no scar, line or blemish on his
forehead, nose, chin, jaw or left cheek. His shoulder bands are CHARCOAL
GREY. BOTH his forearm plates are plain and bare — nothing mounted on
either forearm. No jewellery.

PERSON B — THE SHORTER ONE, IDENTICAL WHEREVER SHE APPEARS: a woman, 33
years old, 1.58 metres tall — a full 17 centimetres shorter than the man,
noticeably short and compact, square-shouldered and solidly built. Very
dark brown skin with clearly visible pore texture and natural subsurface
scattering — no airbrushing, no smoothing, no beauty retouching. HER HEAD
IS COMPLETELY SHAVED: no hair at all, only a 2-millimetre dark shadow of
stubble over the scalp, so the shape of her skull reads clearly. A broad
flat nose with a wide bridge, a full mouth, high round cheekbones, dark
brown eyes, steady and direct. HER ONE MARK: a fine pale 4-centimetre
surgical line that runs ALONG THE BONE OF HER RIGHT JAW, from just below
her right ear to the point of her chin — it sits on the jawline itself,
not on her cheek, not on her neck, not on her brow. The rest of her face
is completely unmarked: no scar, line or blemish on either cheek, her
forehead, nose or left jaw. Her shoulder bands are BONE WHITE. ON HER
LEFT FOREARM ONLY: a 12-centimetre machined grey tool block, rectangular
and low-profile, bolted flush to the forearm plate with four visible
fasteners — her right forearm is bare. No jewellery.

BOTH SUITS — IDENTICAL IN EVERY PANEL: matte BURNT-ORANGE hard-shell
pressure suits — a deep saturated oxidised-iron orange with a faint red
bias, never fluorescent, never plastic-looking. Segmented chest,
shoulder, thigh and shin plates with crisp recessed seams; dark graphite
flex-weave fabric visible at every joint at the shoulders, elbows, waist,
hips and knees; machined aluminium articulation rings at both shoulders,
both elbows and both wrists; a band inlaid flush across the top of each
shoulder plate, charcoal grey on him and bone white on her. Both gloves
on, matte orange with graphite palms worn shiny. Finely scuffed and
hairline-scratched from use, dulled at the elbows and knees. BOTH BACKS
ARE FLAT: no backpack, no tank, no hose, no cable, no rear housing of any
kind — each back silhouette is a clean flat line.

BOTH HELMETS — WORN AND SEALED IN EVERY PANEL: low-profile helmets in the
same burnt orange, locked to the collar. Each visor is a single curved
optically clear pane held in a 2-centimetre brushed-metal frame; the
frame's lower seal ring is clearly visible where it meets the suit
collar, showing the helmet is closed and locked. ONE thin unbroken
specular line runs along each pane's upper edge — the only reflection a
visor carries. Through the pane each face is fully readable: skin
texture, his moustache hairs, her shaved scalp, and both marks visible
with no distortion. A faint film of breath condensation sits at the very
bottom edge of each glass only.

PANEL 1 — TOP LEFT, PERSON A, FULL FIGURE: the man alone, standing
upright and centred, three-quarters to camera with his head turned to
face the lens directly, arms relaxed at his sides, with clear space
around him so the silhouette reads on all sides — including the BACK line
of the suit, visible along his turned shoulder. He is the only person in
this panel.

PANEL 2 — TOP RIGHT, PERSON B, FULL FIGURE: the woman alone, standing
upright and centred, three-quarters to camera with her head turned to
face the lens directly, arms relaxed at her sides, with clear space
around her so the silhouette reads on all sides — including the BACK line
of the suit, visible along her turned shoulder. She is the only person in
this panel.

PANEL 3 — BOTTOM LEFT, THE TWO TOGETHER, HEIGHT COMPARISON: both people
standing upright and facing the camera directly, shoulder to shoulder
with a 40-centimetre gap between them, arms relaxed at their sides, feet
level on the same plane so their heights compare directly — the man on
the LEFT, the woman on the RIGHT. The 17-centimetre difference must be
plainly visible: the top of her helmet reaches only to his eyebrow line.
At a glance the two must be unmistakably different people — different
height, different build, different skin, different head, different
forearms, different shoulder bands.

PANEL 4 — BOTTOM RIGHT, THE TWO FACES, CLOSE: both heads side by side in
one frame, seen from 1 metre, each face square to camera through its
CLOSED and locked visor, the man on the LEFT and the woman on the RIGHT,
cropped at the shoulders. At this size every difference reads
individually: his thick grey moustache and receding cropped grey hair
against her completely shaved scalp; his weathered pale olive skin
against her very dark brown skin; his burn scar on the right cheekbone
against her surgical line along the right jaw; his sun-lined 54-year-old
face against her 33-year-old one. On each visor: the 2-centimetre
brushed-metal frame, the seal ring at the collar, and the single thin
specular line along the upper edge — and nothing else.

THE POINT OF THIS SHEET: nothing anywhere on it reads as the same person
twice.

NEGATIVE: exactly TWO people on the whole sheet — no third person, no
duplicate, no clone, no mirrored copy, no reflected figure, no crowd, no
silhouette in any background. Panels 1 and 2 contain exactly ONE figure
each; panels 3 and 4 contain exactly TWO. Each person is IDENTICAL
wherever they appear — same face, same bone structure, same skin, same
age, same build, same marks, no drifting, no morphing between panels. The
two faces are completely different in bone structure, skin, age and head:
they are never the same face, never twins, never one figure repeated,
never siblings. The height difference is always visible and never
equalised. No visor ever carries tint, mirror coating, environment
reflection, HUD graphics or display overlay, and no visor is ever open,
lifted, retracted or removed — there is no bare skin above either collar
anywhere on the sheet. Both backs are flat in every panel — no backpack,
tank, hose, cable or rear unit on either suit. Nothing is mounted on
either of his forearms; nothing is mounted on her right forearm. She has
hair nowhere: no stubble beyond 2 millimetres, no braids, no fringe, no
wig. No airbrushing, no waxy or plastic skin, no beauty filter, no
makeup, no jewellery, no beard on him beyond the moustache, no tattoo. No
weapon. No readable text, letters, digits, numbers, insignia, flags,
patches, labels, captions, arrows, callouts, panel titles or watermark
anywhere on either suit, on the sheet, OR IN THE GUTTERS. 0% bloom, no
glow filter, no soft focus. No stylisation, no illustration, no CGI
render aesthetic, no video game look. Photorealistic with 35mm film grain.
```

---

# 🔧 3. KULLANIM

```
A) REFERANS DESTEKLİ ÜRETİM (tercih edilen)
   Runway Gen-4 References / Veo Ingredients / Kling referans girişi:
   sahne promptunu yapıştır + §2 eşleme tablosundaki SAYFA(LAR)ın
   TAMAMINI yükle. Model sayfadaki bütün panelleri görür; tek panel
   kırpıp yüklemekten daha güçlü çapadır. Metin çapası promptta KALIR —
   silme. Referans ile metin çeliştiğinde METNİ düzelt, referansı değil.

B) I2V ZİNCİRİ (referans girişi yoksa)
   Sahnenin 📸 IMAGE promptunu referansla birlikte üret → kareyi onayla →
   o kareyi başlangıç karesi olarak 🎥 VIDEO promptuna ver.
   ⚠️ Onaylanmamış imajdan video üretme.

C) DURUM BLOKLARI [D84 ②]
   Aynı durumdaki sahneler AYNI OTURUMDA üretilir:
     blok 1: S0-S3 (6 kartuş dolu)     blok 2: S4-S7 (5 kartuş)
     blok 3: S8-S12 (3→2 kartuş)       blok 4: S13-S18 (1→0 kartuş)
     blok 5: S19-S24 (yüksüz, 0 kartuş)
   Kartuş yuvası sayısı ve kızak durumu blok içinde SABİTTİR; blok
   sınırında değişir. Metin bunu tek başına tutmuyor — oturum tutuyor.

D) SEED KİLİDİ
   Her sayfanın seed'ini §1 tablosuna YAZ. Sahne üretiminde varyasyon
   çıkarsa ilk bakılacak yer burasıdır.

E) PROMPT UZUNLUĞU
   Sayfa promptları 6.100-8.100 karakter (tek görsel promptları
   2.000-3.000'di). 4.300 karakter tavanı VEO'nun VİDEO tavanıdır
   [prompt_kontrol.py] ve buraya UYGULANMAZ — bunlar imaj promptlarıdır
   ve tek karede üretilir. Yine de kullandığın imaj aracı promptu
   kırpıyorsa KISALTMA SIRASI şudur, yukarıdan aşağı:
     1. FINISH paragrafındaki aşınma ayrıntıları
     2. panel metinlerindeki kamera mesafesi cümleleri
     3. negatifin biçim/estetik kuyruğu (stylisation · CGI · film grain)
   ⛔ ASLA kırpılmaz: sayı kilitleri (TAM 3 / TAM 4 / TAM 6 / TAM 40),
      "IDENTICAL IN ALL FOUR PANELS" cümlesi, oluk yazı negatifi,
      vizör üç işareti, sırt DÜZ maddesi.

F) ⚠️ PANEL ÇÖZÜNÜRLÜĞÜ KAÇIŞ YOLU
   Panel sayfasının bilinen bedeli: her varlık karenin dörtte birine
   düşer. Bir panel §4 kapısında "detay okunmuyor" diye kalırsa o TEK
   PANELİ, aynı metni kullanarak, tam kare tek görsel olarak yeniden
   üret — sayfanın tamamını değil. Sayfadaki diğer üç panel geçerli
   kalır; eşleme tablosunda o sahneye hem sayfayı hem tek görseli yükle.
   En olası adaylar: RB p3 (yuva makro) · RD p3 (seçici makro) ·
   RE p4 (iki yüz).
```

---

# ✅ 4. DEVAMLILIK KAPISI — sahne üretimine geçmeden önce

> Bir madde bile ☒ ise o sayfa yeniden üretilir.
> "Panel içi detay" maddeleri için §3-F kaçış yolu geçerlidir.

```
SAYFA BİÇİMİ (hepsi)
□ TAM 4 panel var mı — 3 değil, 5 değil, birleşmiş panel yok mu?
□ Oluklarda ve panel içinde yazı / etiket / ok / ölçü çizgisi / panel
  başlığı / filigran YOK mu? → varsa at
□ Panel içi detay okunuyor mu? (RB p3'te menteşe pimi, RD p3'te altı
  diş, RE p4'te gözenek dokusu ayrı ayrı görülmeli) → okunmuyorsa §3-F

GEMİ (RA)
□ Altı bölüm pruvadan kıça DOĞRU SIRADA mı?
  (buz kalkanı → 3 tambur → 4 küre → yanaşma kolu → omurga →
   2 radyatör → gölge kalkanı → motor bloğu)
□ TAM 3 tambur · TAM 4 küre · TAM 2 radyatör kanadı · TAM 3 lüle
□ Dört panelde de AYNI gemi mi — panel arası oran kayması var mı?
□ Yanaşma kolu gövdeden 12 m DIŞARI çıkıyor ve yuva ALT yüzünde mi?
□ p2'de kapsül geminin 1/40'ı olarak okunuyor mu? (kapsül, tek bir
  yakıt küresinin çapından kısa olmalı)
□ p3'te alev DÜZ ve keskin mi — kıvrılma, kabarma, mantar var mı? → varsa at
□ p1, p2, p4'te alev/parıltı SIZDI mı? → sızdıysa at
□ Dönen halka / santrifüj / kanat / çanak anten var mı? → varsa at

YANAŞMA YERİ (RB)
□ TAM 3 yakalama kolu, TAM 1 halka, TAM 1 konik boğaz — dört panelde de
□ p1'de üçü de AÇIK, p2'de üçü de KAPALI mı?
□ ⭐ p1 ile p2 arasındaki TEK fark kolların durumu ve oturmuş prob mu?
  (kadraj, mesafe, açı, aşınma, ışık oluğu birebir aynı olmalı)
□ Yuva dört panelde de AŞAĞI bakıyor mu? (yana bakıyorsa at)
□ p2'de prob ile halka arasında NET yapısal sınır var mı — kaynaşma
  (merging/phasing) var mı? → varsa at [D11 · D17]
□ Işık oluğu ince bir ÇİZGİ mi, hale mi? → haleyse at

KAPSÜL (RC)
□ Dört panelde de aynı araç mı? (koni açısı, pencere yeri, dikiş hattı)
□ TAM 4 lüle · TAM 6 kartuş yuvası · TAM 40 karot yuvası · TAM 1 prob
□ ⭐ p1 ile p3 farkı YALNIZCA yük ve kayış mı? Gövdede başka fark
  varsa sayfa yeniden üretilir — filmin bedeli bu iki panelin farkı
□ Kartuş durumları panel panel doğru mu? (p1: 6 dolu · p2: 4 dolu 2 boş ·
  p3: 6 boş) → karışmışsa at
□ p3'te turuncu kayış DÜMDÜZ AŞAĞI ve gevşek mi sarkıyor?
□ Silindir / roket / kanatlı uçak / kapsül-kapsülü siluetine kaymış mı?
□ Hiçbir panelde bacak, tekerlek, kanat, paraşüt var mı? → varsa at

KABİN (RD)
□ İki koltuk, SOLDA pilot / SAĞDA mühendis — takas var mı? → varsa at
□ TAM 6 diş seçicide · TAM 1 turuncu kol · TAM 1 pirinç kordon
□ Kordon her panelde DÜMDÜZ AŞAĞI sarkıyor mu? (süzülüyorsa filmin
  novum'u ölür, at)
□ p3'te seçici kolu BİRİNCİ konumda mı ve altı diş ayrı ayrı sayılıyor mu?
□ Hiçbir panelde rakam, harf, ekran grafiği, hologram var mı? → varsa at
□ Kabindeki tek doygun renk turuncu kol mu?

KARAKTERLER (RE)
□ ⭐ p3 ve p4'te İKİ AYRI İNSAN okunuyor mu?  ← en kritik madde
□ p3'te boy farkı (17 cm) gerçekten görünüyor mu? (kask tepesi kaş hizası)
□ Bıyık ↔ tıraşlı baş ayrımı ilk bakışta okunuyor mu?
□ p1'deki adam p3 ve p4'tekiyle AYNI adam mı? p2'deki kadın p3 ve
  p4'tekiyle AYNI kadın mı? → panel arası kayma varsa at
□ Pilotun ön kolları BOŞ, mühendisin SOL ön kolunda blok var mı?
□ İzler doğru ORGANDA mı? (sağ elmacık kemiği ↔ sağ çene hattı)
□ Omuz bantları doğru mu? (adam KÖMÜR GRİSİ · kadın KEMİK BEYAZI)
□ Sırt DÜZ mü — hiçbir panelde sırt ünitesi var mı? → varsa at [D79]
□ Vizörde üç işaret de var mı: 2 cm çerçeve · yaka mührü · tek parlama
  çizgisi? Ve yüz tam okunuyor mu? [D95]
□ Vizörde renk / aynalama / çevre yansıması / HUD var mı? → varsa at

HEPSİ
□ Turuncu YALNIZ üç yerde: iki skafandr · yük kayışı · atma kolu
□ Seed §1 tablosuna yazıldı
```

---

# 📌 5. SONRAKİ ADIM

```
Bu paket üretilip §4 kapısından geçtikten sonra sahne üretimi başlar:
  KAPI 1 → S19 (yük atma)      KAPI 2 → S21 (temas)
  KAPI 3 → S4  (alev)          KAPI 4 → S1  (kabin, iki insan)
Kapı sahneleri ve Plan B'leri: THE_UPHILL_DARK_PLAN.md → ÜRETİM PLANI.

⚠️ Bu paket 3-5 dk formatında ikinci kez yazılıyor (ilki THE COLD BURN,
07.08.2026). Cold Burn'ün panel sayfası biçimi burada da kullanılıyor —
fark, sayfa başına panel sayısının TAM 4'e sabitlenmiş olması ve iki
DURUM ÇİFTİNİN (RB p1↔p2, RC p1↔p3) bilerek aynı sayfaya konması.
Gerekçe ve bedeli §0'da.
```
