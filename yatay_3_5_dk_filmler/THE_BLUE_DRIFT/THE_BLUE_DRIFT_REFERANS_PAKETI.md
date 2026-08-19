# 🎯 THE BLUE DRIFT — REFERANS PAKETİ

## Lander · Ana Gemi · Yakalama Ağzı · Kabin · Karakterler
### 5 birleşik referans sayfası · **her sayfada TAM 4 PANEL** (20 panel)

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR.** Üretim sırası:
> **bu dosya → onay → seed kilidi → PART_A / PART_B sahneleri.**
>
> ⭐ **Format:** Uphill Dark emsali (17.08.2026) birebir — varlık başına
> TEK SAYFA, sayfa başına TAM 4 PANEL; kritik DURUM ÇİFTLERİ bilerek
> aynı sayfada (gerekçe §0'da).
>
> ⭐ **Kaplama (ev stili):** lander + ana gemi **saten çelik mavisi +
> ince sinyal beyazı çizgi**; suitler **mat kobalt + turkuaz/amber
> çizgi**; tamburlar koyu kapitone. AMBER yalnız üç yerde: verici
> kubbesi · hangar içi ışık · mühendis çizgisi. Turkuaz/amber her yerde
> BOYADIR, ışık değil (hangar içi ışık hariç — o filmin tek sıcak
> mekânıdır).
>
> Tüm promptlar **Ders 34** uyumlu: karakter adı hiçbir promptta geçmez.
> Tüm promptlar **Ders 79 + 95** uyumlu: sırt düz, vizör berrak ama
> **görünür** (çerçeve + yaka mührü + tek parlama çizgisi).
> Tüm promptlar **yazısızdır**: sayfada, panelde, oluklarda 0 harf.

---

# 0. ⚠️ NEDEN BU DOSYA VAR — VE NEDEN 5 SAYFA

```
ÖLÇÜLMÜŞ SEBEP (Cold Burn, 07.08.2026): dört varlığın tanımı 60
promptta KELİMESİ KELİMESİNE aynı yazıldı — ve yetmedi. Metin çapası
modelin aynı CÜMLEYİ okumasını sağlar, aynı NESNEYİ çizmesini sağlamaz.
Text-to-video her çağrıda gövde oranlarını yeniden uydurur.

BU FİLMDE RİSK DAHA YÜKSEK, ÇÜNKÜ PALET TEKTİR: MAVİ-ÜSTÜNE-MAVİ.
Beş mavinin ayrışması (safir gezegen · kırağı · aurora · çelik mavisi
gövdeler · kobalt suitler) ton ve doku farkına dayanıyor. Model tonu
sahne sahne yeniden seçerse skala çöker ve film "mavi sisin içinde mavi
lekeler"e döner [D76]. Referans sayfası tonu SABİTLER — metin çapasının
yapamadığı tek şey budur.

ÜÇ DURUM ÇİFTİ bu filmde kritik ve üçü de bilerek AYNI SAYFADA:
  · RA p1 ↔ p2  bacaklar AÇIK ↔ KATLI (Cold Burn dördüncü tur dersi:
    bacak durumu metinle tutmadı — kanıtlı delik)
  · RC p1 ↔ p2  yakalama kolları AÇIK ↔ KENETLİ (doruğun geometrisi)
  · RD p2 ↔ p4  panel ÖLÜ ↔ CANLI (arızanın tüm görsel dili)
Aynı sayfadaki iki durum aynı çağrıda çizilir; fark artık ölçülebilir.

PANEL SAYFASININ BİLİNEN İKİ AÇIĞI VE ÖNLEMLERİ (Uphill Dark emsali):
  ① Oluklar yazı/ok üretmeye açık → oluk dili "thin neutral mid-grey
    gutters" + negatifte oluk ADIYLA geçer.
  ② Panel başına çözünürlük dörtte bire iner → "maximum resolution" +
    §4 kapısına "panel içi detay okunuyor mu" maddesi + §3-F kaçış
    yolu (okunmayan TEK panel tam kare yeniden üretilir).
```

---

# 1. 📋 ÜRETİM SIRASI VE SEED TAKİP TABLOSU

| # | Referans sayfası | Panel | Ne | Öncelik | Seed | Durum |
|---|---|:---:|---|:---:|---|:---:|
| **RA** | LANDER SAYFASI | 4 | zemin · uçuş · ÖLÜ · kıç detay | 🔴 ZORUNLU | | ☐ |
| **RB** | ANA GEMİ SAYFASI | 4 | yan · üç çeyrek+ölçek · orta gövde · tahrik | 🔴 ZORUNLU | | ☐ |
| **RC** | YAKALAMA AĞZI SAYFASI | 4 | açık · kenetli · iç kadraj · kol+kelepçe detay | 🔴 ZORUNLU | | ☐ |
| **RD** | UÇUŞ GÜVERTESİ SAYFASI | 4 | ⭐arkadan geniş (S5 kadrajı) · ölü panel · omurga+valf makro · canlı panel | 🔴 ZORUNLU | | ☐ |
| **RE** | KARAKTER SAYFASI | 4 | pilot · mühendis · ⭐ikisi · iki yüz | 🔴 ZORUNLU | | ☐ |

```
ÜRETİM SIRASI — kapı kapı, atlama yok:

RA   LANDER ÖNCE. 20 sahnede kadrajda; üç durumu (zemin/uçuş/ölü) film
     boyunca sırayla yaşanıyor. p1↔p2 bacak çifti Cold Burn'ün kanıtlı
     deliğini kapatır. Onaylanmadan hiçbir sahne üretilmez.
RB   Ana gemi: 1/15 oranı p2'de donar ("katedral"); orta gövde/ağız
     bölgesi p3'te — RC bu geometriyi devralır.
RC   Yakalama ağzı: doruğun geometrisi burada donar. p1 ↔ p2 farkı
     YALNIZCA kolların durumu ve içerideki araç olmalı. p3, S21'in
     birebir kamera kadrajıdır (üretim kapısı 1).
RD   Uçuş güvertesi: 11 iç sahnenin kadrajı burada standartlaşır.
     p1 ARKADAN geniştir — kabin çekimlerinin çoğu arkadan olduğu için
     referansın da hero karesi odur (S5 birebir). p2↔p4 ölü/canlı panel
     çifti arızanın dilini sabitler.
RE   ⭐ İKİ KARAKTER TEK SAYFADA — bu sayfa aynı zamanda KLON
     KAPISIDIR. p3/p4 ayrışmıyorsa sayfa reddedilir (depodaki üç klon
     vakası bu iki panelle yakalanabilirdi).
```

---

# 2. 🗺️ SAHNE → REFERANS EŞLEME

> Sahne üretirken **ilgili sayfanın TAMAMINI** yükle — model sayfadaki
> bütün panelleri görür. Parantezdeki panel "bu sahnenin kadrajı hangi
> panele en yakın" demektir, "yalnız onu yükle" demek değildir.
>
> ⭐ **18.08.2026:** aynı eşleme artık sahne başlıklarının altında da
> yazılıdır (PART_A / PART_B / KAPAK · `> 🎯 REFERANS:` satırı —
> Uphill Dark emsali). İki kaynak çelişirse BU TABLO esastır ve
> başlık satırı düzeltilir.

| Sahne | İç/Dış | Yüklenecek referans | Kadraj paneli |
|---|:---:|---|---|
| **S0** | dış | **RA** | RA p1 (zemin, uzak) |
| S1 | dış | **RE + RA** | RE p1·p2 + RA p1 (30 m arkada) |
| S2 | dış | **RE + RA** | RE p3 (ikisi, yukarı bakış) + RA p1 |
| S3 | dış | **RE + RA** | RE p3 + RA p1 |
| **S4** | dış | **RE + RA** | RE p3 ⭐ (koşu, boy farkı) + RA p4 (bacak+chine yakın) |
| S5 | iç | **RD + RE** | RD **p1** ⭐ (arkadan geniş — birebir kadraj) + p4 + RE (arkadan) |
| S6 | iç | **RD + RE** | RD p1·p4 + RE (arkadan) |
| **S7** | dış | **RA** | RA p1 → p2 ⭐ (bacak katlanışı — durum çifti geçişin kendisi) |
| S8 | dış | **RA** | RA p2 (uçuş) |
| S9 | iç | **RD + RE** | RD p4 → p2 ⭐ (panel ölümü) + RE (arkadan) |
| S10 | iç | **RD + RE** | RD p2 (ölü panel + amber lamba) + RE |
| S11 | iç | **RD + RE** | RD p2 + RE (arkadan) |
| **S12** | dış | **RA** | RA p3 ⭐ (ÖLÜ + amber nabız) |
| S13 | dış | **RA** | RA p3 |
| S14 | iç | **RD + RE** | RD p3 ⭐ (pirinç valf) + RD p2 + RE |
| **S15** | dış | **RA** | RA p3 + p4 (vent port kıç detayda) |
| S16 | iç | **RD + RE** | RD p2 (duran küre · ibre %40) + RE |
| S17 | iç (cam) | **RB + RD + RE** | RB p1·p2 (gemi 200 m) + RD p1 + RE |
| S18 | iç detay | **RD + RE** | RD p2·p3 (konsol + eldivenler) + RE (kollar) |
| S19 | iç (cam) | **RB + RC + RD + RE** | RB p3 + RC p1 (açık ağız dead-on) + RD p1 + RE |
| S20 | iç (cam) | **RB + RC + RD + RE** | RB p3 (60 m dolduran gövde) + RC p1 + RD p1 + RE |
| **S21** | dış | **RC + RA** | RC p3 ⭐ (hangar içi kadraj — birebir) + RC p1 + RA p3 |
| S22 | iç | **RD + RE** | RD p2 (yükselen ibre) + RE (arkadan) |
| S23 | iç güverte | **RE** | RE p4 ⭐ (iki yüz) + p1·p2 (kasksız — kilit §4'te) |
| S24 | dış | **RB + RC + RA** | RB p1·p2 + RC p2 (kenetli) + RA p3 |

```
⚠️ TEK PANELDE OLMAYAN DURUMLAR (metin taşır, referans taşımaz):
  · S16 · S22 — ibre %40 / yükselen: RD p2 ibreyi YÜKSEK gösterir;
    ibrenin DİLİ p2'den, açısı prompt metninden gelir.
  · S23 — kasksız yüzler: RE tüm panellerde KASKLI. Yüz kemiği ve
    izler p4'ten; kasksızlık sahne promptunun kendi kilididir
    (BARE-HEADED + yarı takılı kask yasağı). Referans yüz İÇİN
    yüklenir, kask için değil.
  · S15 — puflar hiçbir panelde yok (hareket, durağan karede
    taşınmaz); vent port yeri RA p4'ten, puf fiziği prompt metninden.
```

---

# 🚀 RA — LANDER SAYFASI 🔴

> **Filmin ana gövdesi.** Üç durumu (zeminde canlı → uçuşta → ÖLÜ)
> film sırasıyla yaşar; p1↔p2 bacak çifti Cold Burn'ün kanıtlı
> deliğini, p3 ölü durum amber nabzıyla filmin ikinci yarısını taşır.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one single small
spacecraft, 16:9 widescreen, maximum resolution. One frame divided
into FOUR CLEAN PANELS separated by thin neutral mid-grey gutters, in
two rows of two. Every panel shows THE SAME ONE CRAFT from a different
angle or in a different state. No humans anywhere on the sheet. Plain
neutral mid-grey seamless background in every panel, even neutral key
light at 5000K with soft fill so every surface reads.

THE CRAFT — IDENTICAL IN ALL FOUR PANELS: a 9-meter angular
LIFTING-BODY lander, no plain cylinder: broad flat belly, sharp chine
lines running nose to tail, a low blended forward canopy of dark
glass, two short swept strakes, twin main engines recessed in a
notched tail, four downward LIFT NOZZLES under the belly, four
landing legs that fold up into flush belly wells, recessed thruster
quads at bow and stern, a small round vent port on the right flank
beside the side hatch, and a 40-cm domed emergency-beacon housing on
the left shoulder line. FINISH — IDENTICAL EVERYWHERE: satin
steel-blue composite panels with crisp recessed seams over a
graphite-grey structural spine, one thin SIGNAL-WHITE chevron line
down each flank, finely scuffed from use, light grey staining at the
thruster ports — a working machine, maintained, never dirty, never
derelict. No markings, no numbers, no insignia, no flags, no logos
anywhere on the hull.

PANEL 1 — TOP LEFT, GROUND CONFIGURATION, FULL SIDE ELEVATION: exact
90-degree side elevation, the whole craft filling the panel, its long
axis horizontal, canopy nose at panel-left and notched tail at
panel-right. It stands LEVEL on its FOUR landing legs, legs extended,
gear doors open at the belly wells. Engines cold, every light off.

PANEL 2 — TOP RIGHT, FLIGHT CONFIGURATION, SAME SIDE ELEVATION: the
IDENTICAL craft from the IDENTICAL angle and distance as panel 1 —
same size in frame, same lighting — with exactly ONE difference: all
four landing legs are folded away into their flush belly wells, gear
doors closed, the belly line perfectly clean. Engines cold. Nothing
else differs from panel 1 in any way.

PANEL 3 — BOTTOM LEFT, DEAD STATE, THREE-QUARTER VIEW: the same craft
seen from three-quarters ahead and slightly above, canopy nose toward
panel-left, in flight configuration with legs folded. It is DEAD:
every window dark, every thruster cold, every panel light off — and
on its left shoulder line the single 40-cm beacon dome is caught at
the peak of a warm AMBER pulse, a small hard warm point on a cold
blue hull. This is the only light anywhere on the sheet.

PANEL 4 — BOTTOM RIGHT, STERN AND FLANK CLOSE: the aft third of the
craft seen from behind and to the right at 4 meters, filling the
panel: the notched tail with its TWO recessed main engine bells,
throats clean and cold; the stern thruster quad recessed into the
hull; the right-flank side hatch with its flush handle recess; the
small round vent port beside the hatch, its cover a machined ring;
and across the top of frame the rear chine line and the thin
SIGNAL-WHITE chevron. Every seam, fastener and scuff reads at this
distance.

NEGATIVE: ONE craft only per panel — no second vessel, no variant
designs on the sheet. The architecture is IDENTICAL in all four
panels — same proportions, no extra module, no missing part, no
morphing between panels. Exactly FOUR landing legs, exactly FOUR lift
nozzles, exactly TWO main engines, exactly ONE beacon dome, exactly
ONE vent port — these counts never change. Panels 2, 3 and 4 show NO
landing leg, no leg well and no open gear door. No engine plume, no
fire, no exhaust, no glow of any kind in any panel — the only light
on the sheet is panel 3's single amber beacon point. The craft is
never a cylinder, never a rocket standing on its tail, never winged
like an aeroplane, never a capsule. No humans, no figure at any
window, in any panel. No readable text, letters, digits, numbers,
insignia, labels, captions, arrows, callouts, dimension lines,
blueprint grid, panel titles or watermark anywhere on the sheet OR IN
THE GUTTERS. 0% bloom, no glow filter, no lens flare, no soft focus.
No stylisation, no illustration, no blueprint look, no CGI render
aesthetic, no video game look. Photorealistic with 35mm film grain.
```

---

# 🛰️ RB — ANA GEMİ SAYFASI 🔴

> **Katedralin gövdesi.** 1/15 oranı p2'de donar; orta gövde/ağız
> bölgesi p3'te — RC sayfası bu geometriyi devralır. Yakalama ağzı
> her panelde AÇIK ve boştur (kenetli durum RC p2'dedir).

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one single large
spacecraft, 16:9 widescreen, maximum resolution. One frame divided
into FOUR CLEAN PANELS separated by thin neutral mid-grey gutters, in
two rows of two. Every panel shows THE SAME ONE SHIP from a different
angle or at a different distance. No humans anywhere on the sheet.
Plain neutral mid-grey seamless background in panels 1, 2 and 3, even
neutral key light at 5000K with soft fill.

THE SHIP — IDENTICAL IN ALL FOUR PANELS: a 135-metre INTERSTELLAR
transfer vessel, a long working machine — not a shuttle, not a
warship, not a saucer. From bow to stern, in this exact order and
these exact proportions: 1) a closed BOW SENSOR DOME, a smooth
rounded cap; 2) SIX cylindrical HABITAT MODULES in three tandem
pairs, each wrapped in dark quilted insulation with taut even seams;
3) a long OPEN HEXAGONAL TRUSS SPINE of machined graphite-grey
members with bolted nodes and clipped cable runs, carrying at
midships an OPEN CATCH BAY — a 12-metre hangar slot, 7 metres wide
and 5 metres deep, flanked by TWO machined yoke arms, FOUR open
clamps along its rails, and FOUR small WHITE frame lights marking the
corners of its mouth, its interior lit a warm amber-white; 4) TWO
dead-dark knife-edge RADIATOR WINGS standing straight out from the
spine on opposite sides, each only 30 centimetres thick; 5) an aft
FUSION DRIVE BLOCK, a dense armoured mass with FOUR deeply recessed
nozzles, throats scorched. FINISH — IDENTICAL EVERYWHERE: satin
steel-blue hull panels with crisp recessed seams, sparse thin WHITE
position lines spaced along its length, dark quilted module wrap —
clean and maintained, never dirty, never derelict. The ship does not
rotate and has no spinning ring, no centrifuge, no wings, no dish. No
markings, no numbers, no insignia, no flags, no logos anywhere.

PANEL 1 — TOP LEFT, FULL SIDE ELEVATION, DRIVE COLD: exact 90-degree
side elevation, the whole vessel filling the panel end to end, long
axis horizontal, bow at panel-left and stern at panel-right, so all
five sections read in order at their correct proportions. The catch
bay's warm mouth and four white corner lights read as a small lit
notch at midships. No plume of any kind.

PANEL 2 — TOP RIGHT, THREE-QUARTER BOW WITH SCALE REFERENCE: the same
ship seen from ahead and slightly above, bow toward panel-left, stern
receding toward panel-right, so the depth of the truss and the bay
recess both read. Holding station 60 metres off its near flank, level
with the bay: a small 9-meter angular lifting-body lander, satin
steel-blue with one thin signal-white chevron line down each flank,
in flight configuration, dark and unpowered. It must read as exactly
ONE FIFTEENTH of the ship's length — shorter than a single habitat
module, dwarfed by the truss: a moth beside a cathedral. Both craft
unpowered; only the bay's warm mouth and corner lights are lit.

PANEL 3 — BOTTOM LEFT, MIDSHIP CLOSE — THE APPROACH VIEW: the middle
of the ship seen square-on from 60 metres, filling the panel from the
last habitat module at panel-left to the root of the first radiator
wing at panel-right, the open catch bay centered: its warm
amber-white mouth, the four white corner lights in a perfect
rectangle, the two yoke arms and four open clamps readable inside,
truss members and cable runs sharp around it. This is the exact scale
at which the ship fills the lander's windshield at 60 metres in the
film.

PANEL 4 — BOTTOM RIGHT, DRIVE BLOCK UNDER POWER: the armoured stern
mass alone, seen from below and to one side at 80 metres, against
deep black space with sharp pinpoint stars — the only panel with a
black background. The FOUR recessed nozzles produce four pale
blue-white exhaust cones that merge within 25 metres into a single
straight lance about 300 metres long, running dead straight and
thinning steadily to nothing. Sharply defined near the throats,
diffuse only at its far end. It does not billow, does not curl, does
not mushroom, never bends. It throws pale blue-white light onto the
drive block's underside, leaving surfaces facing away in hard shadow
softened only by faint blue fill.

NEGATIVE: ONE ship only per panel — no second vessel, no fleet, no
variant designs; panel 2's small lander is the only other craft
anywhere and it appears in that panel alone. The architecture is
IDENTICAL in all four panels — same order, same proportions, no extra
module, no missing section, no morphing. Exactly SIX habitat modules,
exactly TWO yoke arms, exactly FOUR clamps, exactly FOUR white corner
lights, exactly TWO radiator wings, exactly FOUR nozzles — these
counts never change. The bay is OPEN and EMPTY in every panel — no
craft inside it anywhere on this sheet. The size relation in panel 2
never changes: the lander is never half the ship, never larger than
one module. The ship never rotates. No humans, no figure at any
window. Panels 1, 2 and 3 carry NO engine plume, no fire, no exhaust
— the drive is cold there; panel 4 carries exactly ONE merged exhaust
lance and nothing else: no smoke, no billowing, no sparks, no debris,
no explosion, and the exhaust never swirls or behaves like a liquid.
No readable text, letters, digits, numbers, insignia, labels,
captions, arrows, callouts, dimension lines, blueprint grid, panel
titles or watermark anywhere on the sheet OR IN THE GUTTERS. 0%
bloom, no glow filter, no lens flare, no soft focus. No stylisation,
no illustration, no blueprint look, no CGI render aesthetic, no video
game look. Photorealistic with 35mm film grain.
```

---

# 🧲 RC — YAKALAMA AĞZI SAYFASI 🔴

> **Doruğun geometrisi bu sayfadadır.** Kollar aracın ÇEVRESİNE
> kapanır (Black Cradle'da araç kollara oturuyordu — ters çevirme).
> ⛔ p1 ile p2 arasındaki tek fark **kolların durumu ve içerideki ölü
> araç** olmalıdır — başka hiçbir şey değişmez. p3, S21'in birebir
> kamera kadrajıdır.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one hangar
capture bay on the truss spine of a large spacecraft, 16:9
widescreen, maximum resolution. One frame divided into FOUR CLEAN
PANELS separated by thin neutral mid-grey gutters, in two rows of
two. Every panel shows THE SAME ONE BAY. No humans anywhere on the
sheet.

THE BAY — IDENTICAL IN ALL FOUR PANELS: an OPEN CATCH BAY recessed
into a satin steel-blue open hexagonal truss spine — a 12-metre
hangar slot, 7 metres wide and 5 metres deep, its inner walls
machined and clean, flanked by TWO machined yoke arms (heavy curved
capture arms hinged at the bay rails, their gripping faces padded),
FOUR clamps along its rails, and FOUR small WHITE frame lights
marking the corners of its rectangular mouth. Its interior is lit a
warm amber-white by recessed strips — the only warm light in a cold
blue structure. Around the bay: truss members with bolted nodes,
clipped cable runs, sparse thin white position lines on satin
steel-blue panels. No markings, no numbers, no insignia anywhere.

PANEL 1 — TOP LEFT, MOUTH FRONTAL, ARMS OPEN, BAY EMPTY: the bay seen
square-on from 25 metres outside, its rectangular mouth centered and
filling most of the panel: four white corner lights in a perfect
rectangle, warm interior beyond, the TWO yoke arms swung OPEN to
either side, the FOUR clamps open along the rails. The bay is EMPTY.
Deep black space with pinpoint stars around the truss.

PANEL 2 — TOP RIGHT, SAME FRONTAL, ARMS CLOSED ON THE CRAFT: the
IDENTICAL view from the IDENTICAL distance and lighting as panel 1 —
with exactly ONE difference: inside the bay, held at its center, sits
a dead 9-meter angular lifting-body lander, satin steel-blue with one
thin signal-white chevron line down each flank, canopy nose facing
out toward the viewer, every window dark; the TWO yoke arms are swung
IN and CLOSED around its hull, the FOUR clamps seated on its rails,
1.5 metres of clearance between hull and bay wall on each side.
Nothing else differs from panel 1 in any way.

PANEL 3 — BOTTOM LEFT, INTERIOR VIEW OUT — THE FILM'S CLIMAX FRAMING:
camera low on the bay's REAR WALL looking straight out through the
open mouth, arms OPEN, bay EMPTY: the warm-lit interior walls recede
toward the rectangular mouth, the four white corner lights frame it,
and beyond lies deep black space with sharp stars and, low in the
opening, the sunlit banded curve of a deep sapphire-blue gas giant.
The threshold between warm interior light and cold blue exterior
light reads as a clean line across the deck.

PANEL 4 — BOTTOM RIGHT, YOKE ARM AND CLAMP MACRO: one yoke arm and
one rail clamp seen from 2 metres, filling the panel: the arm's
machined hinge with its greased pivot pin, the padded gripping face,
the clamp's two jaws and seat, a white corner light housing at the
frame's edge — every fastener, machining mark and wear line
readable. Warm interior light from one side, cold fill from the
other.

NEGATIVE: The bay geometry is IDENTICAL in all four panels — same
proportions, no extra arm, no missing clamp, no morphing. Exactly TWO
yoke arms, exactly FOUR clamps, exactly FOUR white corner lights —
these counts never change. Panels 1 and 3 show the bay EMPTY with
arms OPEN; panel 2 is the ONLY panel containing the lander, and the
ONLY differences from panel 1 are the closed arms, the seated clamps
and the craft itself. The lander in panel 2 is dead — no window
light, no engine, no jet. No fire, no exhaust, no sparks anywhere on
the sheet. No humans, no figure anywhere. No readable text, letters,
digits, numbers, insignia, labels, captions, arrows, callouts,
dimension lines, blueprint grid, panel titles or watermark anywhere
on the sheet OR IN THE GUTTERS. 0% bloom, no glow filter, no lens
flare, no soft focus — the warm interior light is contained, not
hazy. No stylisation, no illustration, no blueprint look, no CGI
render aesthetic, no video game look. Photorealistic with 35mm film
grain.
```

---

# 🎛️ RD — UÇUŞ GÜVERTESİ SAYFASI 🔴

> **11 iç sahnenin kadrajı burada standartlaşır.** Filmin kabin
> çekimlerinin neredeyse tamamı ARKADAN olduğu için sayfanın p1'i de
> arkadan geniştir — S5'in birebir kadrajı odur.
> p2 ↔ p4 çifti arızanın tüm görsel dilidir: aynı panel, ölü ↔ canlı,
> tek fark ışık segmentleri. Üç mekanik kahraman (duruş küresi · basınç
> ibresi · pirinç valf) burada donar.

```
Photorealistic INDUSTRIAL DESIGN REFERENCE SHEET of one small two-seat
spacecraft flight deck, 16:9 widescreen, maximum resolution. One frame
divided into FOUR CLEAN PANELS separated by thin neutral mid-grey
gutters, in two rows of two. Every panel shows THE SAME ONE FLIGHT
DECK. No humans anywhere on the sheet — both seats are empty in every
panel.

THE FLIGHT DECK — IDENTICAL IN ALL FOUR PANELS: 2.2 metres wide, built
as a working machine, not a lounge. TWO HIGH-BACKED MACHINED SEAT
SHELLS side by side, each with an open headrest cage, cross-harness
webbing hanging over the shoulder line, and one thin PIPING LINE down
the seat back — TEAL down the LEFT seat, AMBER down the RIGHT seat.
Between them a machined CONSOLE SPINE, and at its foot a 30-cm BRASS
VENT-VALVE LEVER with a worn knurled grip, purely mechanical, on a
machined manifold. At each elbow a canted SIDE CONSOLE carrying
abstract light segment bars. Overhead, a ribbed structural ARCH
spanning both seats, carrying exactly SIX guarded toggles and exactly
TWO recessed TEAL strip lights that wash down onto the seat backs.
Ahead, a THREE-PANE WRAPAROUND CANOPY: one wide central pane 1.4 by
0.5 metres flanked by two angled quarter-panes, all three separated by
machined graphite frames. The main panel below the canopy is analog:
abstract AMBER and TEAL light segment strips (pure indicator bars — no
text ever), at its centre a 12-cm MECHANICAL ATTITUDE SPHERE in a
machined bezel, and on the right side a 12-cm MECHANICAL
CABIN-PRESSURE DIAL — an unnumbered arc scale with TEN tick marks and
a fine needle on a phosphor face — with a small round AMBER REPEATER
LAMP above it. Floor: open grating, a thin blue rim light along the
sill, cable looms clipped along the bilge. Surfaces: matte dark grey
structure, cobalt-blue seat shells, brushed metal bezels, fine wear on
every touch point. No markings, no numbers, no letters anywhere.

PANEL 1 — TOP LEFT, THE FILM'S SIGNATURE FRAMING, FROM BEHIND: the
whole deck seen from 1.2 metres behind the seat backs and 20 cm above
them, centred on the console spine, looking forward through the
canopy — both seats EMPTY. The two seat backs, their piping lines, the
overhead arch with its six toggles and two teal strips, the side
consoles, the panel and all three canopy panes read together in one
frame. Beyond the glass: plain neutral mid-grey.

PANEL 2 — TOP RIGHT, PANEL CLOSE, DEAD STATE: the instrument panel
seen square-on from 0.8 metres, filling the frame — and DEAD: every
amber and teal segment strip dark and unlit, the overhead strips and
the floor rim light OUT, the attitude sphere still and lit only by its
own pale backlight, the pressure dial's phosphor face soft-lit with
its needle HIGH on the arc, and the small round amber repeater lamp
caught at the peak of a pulse — the only three light sources in frame.

PANEL 3 — BOTTOM LEFT, CONSOLE SPINE AND BRASS LEVER MACRO: the foot
of the console spine seen from 0.4 metres, filling the panel: the
30-cm brass vent-valve lever with its worn knurled grip, the machined
manifold it mounts to, its travel slot and end stops, the low amber
strip running along the spine, and the hairline scratches of use on
the brass — every machining mark readable. Neutral even light.

PANEL 4 — BOTTOM RIGHT, PANEL CLOSE, ALIVE STATE: the IDENTICAL panel
view from the IDENTICAL distance and angle as panel 2 — with exactly
ONE difference: the amber and teal segment strips are LIT in a full
launch state, stepped bars of clean abstract light, the two overhead
strips and the floor rim light on; the attitude sphere level and
backlit; the dial needle HIGH; the repeater lamp dark. Nothing else
differs from panel 2 in any way.

NEGATIVE: The flight deck is IDENTICAL in all four panels — same
layout, same instruments, same seats, no extra screen, no added
display, no morphing between panels. Exactly TWO seats — teal piping
left, amber piping right, never swapped. Exactly SIX guarded toggles,
exactly TWO overhead strip lights, exactly THREE canopy panes, exactly
TEN tick marks on the dial, exactly ONE brass lever, ONE attitude
sphere, ONE repeater lamp — these counts never change. NO readable
text, letters, digits or numerals anywhere: the segment strips are
pure abstract bars, the dial is unnumbered, no screen shows
characters, no placard, no label, no HUD, no hologram. No humans, no
hands, no helmet, no figure reflected in the canopy. Panel 2 is DEAD
(three light sources only) and panel 4 is ALIVE — the only difference
between them is which lights are on. 0% bloom, no glow filter, no soft
focus — the amber lamp is a hard point, not a haze. No stylisation, no
illustration, no CGI render aesthetic, no video game look.
Photorealistic with 35mm film grain.
```

# 👥 RE — KARAKTER SAYFASI 🔴

> ⛔ **Bu sayfa aynı zamanda bir DENETİMDİR.** p3 ve p4 iki figürü aynı
> karede yan yana koyar; ayrışmıyorlarsa sayfa reddedilir ve yeniden
> üretilir (depodaki üç klon vakası bu iki panelle yakalanabilirdi).
>
> Yüz çapası bu sayfadadır. Vizör **berrak ama görünür**: çerçeve +
> yaka mührü + tek parlama çizgisi [D95]. Sırt DÜZ [D79].

```
Photorealistic CHARACTER REFERENCE SHEET of TWO different people in
pressure suits, 16:9 widescreen, maximum resolution. One frame
divided into FOUR CLEAN PANELS separated by thin neutral mid-grey
gutters, in two rows of two. Exactly TWO people exist on the whole
sheet and they are two clearly different individuals. Neutral studio
lighting in every panel: soft even key at 5000K with gentle fill,
plain mid-grey seamless background, shadows soft but present.

PERSON A — THE TALLER ONE, IDENTICAL WHEREVER HE APPEARS: a man, 44
years old, 1.83 metres tall, broad-shouldered and lean. Warm tan skin
with clearly visible pore texture and natural subsurface scattering —
no airbrushing, no smoothing. Short black hair greying at the
temples, cropped close. Dark brown eyes, calm and steady. A broad
nose ONCE BROKEN AT THE BRIDGE — the small flattened step in its line
reads clearly in profile and three-quarter. HIS ONE MARK: a thin old
scar on his LEFT CHEEKBONE, 3 centimetres long — on the cheekbone,
not the jaw, not the temple. The rest of his face is unmarked. His
suit's accent lines are TEAL.

PERSON B — THE SHORTER ONE, IDENTICAL WHEREVER SHE APPEARS: a woman,
36 years old, 1.69 metres tall — a full 14 centimetres shorter than
the man, wiry and light-framed. Pale cool-toned skin with clearly
visible pore texture, FAINT FRECKLES across the nose and cheekbones,
and natural subsurface scattering — no airbrushing, no smoothing.
Dark auburn hair in a near-shaved crop, 3 millimetres, so the skull
shape reads. Grey-green eyes, direct and precise. HER ONE MARK: a
small notch scar SPLITTING HER LEFT EYEBROW into two segments — on
the eyebrow itself, not the forehead, not the lid. The rest of her
face is unmarked. Her suit's accent lines are AMBER.

BOTH SUITS — IDENTICAL IN EVERY PANEL EXCEPT THE ACCENT COLOUR: matte
COBALT-BLUE hard-shell pressure suits — deep even cobalt, never
glossy, never plastic-looking. Segmented chest, shoulder, thigh and
shin plates with crisp recessed seams; dark graphite flex-weave
fabric at every joint; machined aluminium articulation rings at
shoulders, elbows and wrists; thin inlaid accent lines along the
shoulder plates and forearms — TEAL on him, AMBER on her — finely
scuffed from use, dulled at elbows and knees. Both gloves on, cobalt
with graphite palms worn shiny. BOTH BACKS ARE FLAT: no backpack, no
tank, no hose, no cable, no rear housing of any kind — each back
silhouette is a clean flat line.

BOTH HELMETS — WORN AND SEALED IN EVERY PANEL: low-profile
cobalt-blue helmets locked to the collar. Each visor is a single
curved optically clear pane held in a 2-centimetre brushed-metal
frame; the frame's lower seal ring is clearly visible at the collar,
showing the helmet closed and locked. ONE thin unbroken specular
line runs along each pane's upper edge — the only reflection a visor
carries. Through the pane each face is fully readable: pore texture,
his greying temples and broken nose bridge, her freckles and shaved
scalp, and both marks visible with no distortion.

PANEL 1 — TOP LEFT, PERSON A, FULL FIGURE: the man alone, standing
upright and centred, three-quarters to camera with his head turned
to face the lens directly, arms relaxed, clear space around him so
the silhouette reads on all sides — including the flat BACK line
along his turned shoulder. He is the only person in this panel.

PANEL 2 — TOP RIGHT, PERSON B, FULL FIGURE: the woman alone,
standing upright and centred, three-quarters to camera with her head
turned to face the lens directly, arms relaxed, clear space around
her so the silhouette reads on all sides — including the flat BACK
line along her turned shoulder. She is the only person in this
panel.

PANEL 3 — BOTTOM LEFT, THE TWO TOGETHER, HEIGHT COMPARISON: both
people standing upright and facing the camera directly, shoulder to
shoulder with a 40-centimetre gap, arms relaxed, feet level on the
same plane — the man on the LEFT, the woman on the RIGHT. The
14-centimetre difference must be plainly visible: the top of her
helmet reaches only to the line of his nose. At a glance the two
must be unmistakably different people — different height, different
build, different skin, different face, different accent colour.

PANEL 4 — BOTTOM RIGHT, THE TWO FACES, CLOSE: both heads side by
side in one frame, seen from 1 metre, each face square to camera
through its CLOSED and locked visor, the man on the LEFT and the
woman on the RIGHT, cropped at the shoulders. At this size every
difference reads individually: his greying temples and broken nose
bridge against her freckles and near-shaved auburn scalp; his warm
tan skin against her pale cool-toned skin; his left-cheekbone scar
against her split left eyebrow; his 44-year-old face against her
36-year-old one. On each visor: the 2-centimetre brushed-metal
frame, the seal ring at the collar, and the single thin specular
line along the upper edge — and nothing else.

THE POINT OF THIS SHEET: nothing anywhere on it reads as the same
person twice.

NEGATIVE: exactly TWO people on the whole sheet — no third person,
no duplicate, no clone, no mirrored copy, no reflected figure, no
crowd, no silhouette in any background. Panels 1 and 2 contain
exactly ONE figure each; panels 3 and 4 contain exactly TWO. Each
person is IDENTICAL wherever they appear — same face, same bone
structure, same skin, same age, same build, same marks, no drifting,
no morphing between panels. The two faces are completely different:
never the same face, never twins, never one figure repeated. The
height difference is always visible and never equalised. No visor
ever carries tint, mirror coating, environment reflection, HUD
graphics or display overlay, and no visor is ever open, lifted,
retracted or removed — there is no bare skin above either collar
anywhere on the sheet. Both backs are flat in every panel — no
backpack, tank, hose, cable or rear unit. No airbrushing, no waxy or
plastic skin, no beauty filter, no makeup, no jewellery, no beard,
no tattoo. No weapon. No readable text, letters, digits, numbers,
insignia, flags, patches, labels, captions, arrows, callouts, panel
titles or watermark anywhere on either suit, on the sheet, OR IN THE
GUTTERS. 0% bloom, no glow filter, no soft focus. No stylisation, no
illustration, no CGI render aesthetic, no video game look.
Photorealistic with 35mm film grain.
```

---

# 🔧 3. KULLANIM

```
A) REFERANS DESTEKLİ ÜRETİM (tercih edilen)
   Runway Gen-4 References / Veo Ingredients / Kling referans girişi:
   sahne promptunu yapıştır + §2 eşleme tablosundaki SAYFA(LAR)ın
   TAMAMINI yükle. Metin çapası promptta KALIR — silme. Referans ile
   metin çeliştiğinde METNİ düzelt, referansı değil.

B) I2V ZİNCİRİ (referans girişi yoksa)
   Sahnenin 📸 IMAGE promptunu referansla birlikte üret → kareyi
   onayla → o kareyi başlangıç karesi olarak 🎥 VIDEO promptuna ver.
   ⚠️ Onaylanmamış imajdan video üretme. ⚠️ Panelli sayfa START FRAME
   olarak KULLANILMAZ (panel çizgisi videoya taşınır) [D34/D45].

C) DURUM BLOKLARI [D84 ②]
   Aynı durumdaki sahneler AYNI OTURUMDA üretilir:
     blok 1: S0-S6  (zemin konfig. · bacaklar açık · panel canlı)
     blok 2: S7-S8  (kalkış/uçuş geçişi)
     blok 3: S9-S14 (ölü panel · dönüş var · verici nabzı S10'dan)
     blok 4: S15-S20 (despin sonrası · dönüş SIFIR · ibre %40)
     blok 5: S21-S24 (hangar · sıcak ışık · kenetli)
   Bacak durumu, panel durumu ve dönüş blok içinde SABİTTİR; blok
   sınırında değişir. Metin bunu tek başına tutmuyor — oturum tutuyor.

D) SEED KİLİDİ
   Her sayfanın seed'ini §1 tablosuna YAZ. Sahne üretiminde varyasyon
   çıkarsa ilk bakılacak yer burasıdır.

E) PROMPT UZUNLUĞU
   Sayfa promptları tek görsel bandının üstündedir; 4.300 tavanı
   VEO'nun VİDEO tavanıdır [prompt_kontrol.py] ve buraya UYGULANMAZ.
   İmaj aracı kırpıyorsa KISALTMA SIRASI: ① FINISH aşınma ayrıntıları
   ② kamera mesafesi cümleleri ③ negatifin estetik kuyruğu.
   ⛔ ASLA kırpılmaz: sayı kilitleri (TAM 2/4/6/10), "IDENTICAL IN ALL
   FOUR PANELS" cümlesi, oluk yazı negatifi, vizör üç işareti, sırt
   DÜZ maddesi, p1↔p2 / p2↔p4 "exactly ONE difference" cümleleri.

F) ⚠️ PANEL ÇÖZÜNÜRLÜĞÜ KAÇIŞ YOLU
   Bir panel §4 kapısında "detay okunmuyor" diye kalırsa o TEK
   PANELİ, aynı metni kullanarak, tam kare tek görsel olarak yeniden
   üret — sayfanın tamamını değil. En olası adaylar: RC p4 (kol
   makro) · RD p3 (valf makro) · RE p4 (iki yüz).
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
□ Panel içi detay okunuyor mu? (RC p4'te menteşe pimi, RD p3'te
  knurl dokusu, RE p4'te gözenek/çil) → okunmuyorsa §3-F

LANDER (RA)
□ TAM 4 bacak (yalnız p1) · TAM 4 lüle · TAM 2 motor · TAM 1 verici
  kubbesi · TAM 1 vent port — dört panelde sayılar doğru mu?
□ ⭐ p1 ↔ p2 tek fark BACAKLAR mı? (kadraj, boy, ışık birebir aynı)
□ p2·p3·p4'te bacak / yuva / kapak 0 mı? → varsa at
□ p3'te araç gerçekten ÖLÜ mü — tek ışık amber kubbe mi? Pencere
  ışığı, jet, segment sızdıysa at
□ Silindir / dik roket / kanatlı uçak siluetine kaymış mı? → at
□ Gövde saten ÇELİK MAVİSİ mi — gri/beyaz/siyaha kaymışsa at

ANA GEMİ (RB)
□ Bölümler pruvadan kıça DOĞRU SIRADA mı? (kubbe → 6 modül → omurga +
  ağız → 2 radyatör → tahrik)
□ TAM 6 modül · TAM 2 kol · TAM 4 kelepçe · TAM 4 beyaz ışık ·
  TAM 2 radyatör · TAM 4 lüle
□ Ağız her panelde AÇIK ve BOŞ mu? (kenetli durum yalnız RC p2'de)
□ p2'de lander 1/15 mi — tek modülden kısa mı? Değilse at
□ p4'te alev DÜZ ve keskin mi; p1-p3'e alev/parıltı sızdı mı? → at
□ Dönen halka / kanat / çanak var mı? → at

YAKALAMA AĞZI (RC)
□ TAM 2 kol · TAM 4 kelepçe · TAM 4 köşe ışığı — dört panelde de
□ ⭐ p1 ↔ p2 tek fark KOLLAR + İÇERİDEKİ ARAÇ mı? (kadraj birebir)
□ p2'de kollar aracın ÇEVRESİNE mi kapanmış (araç kollara oturmuş
  değil — ters çevirme doğru mu)? Pay her yanda 1.5 m okunuyor mu?
□ p3 iç kadrajda eşik çizgisi (sıcak iç ↔ soğuk dış) net mi?
□ p2'deki araç ÖLÜ mü — pencere ışığı/jet varsa at
□ Kol-gövde temasında kaynaşma (merging) var mı? → at [D11 · D17]

UÇUŞ GÜVERTESİ (RD)
□ İki koltuk: SOL turkuaz boru / SAĞ amber boru — takas var mı? → at
□ TAM 6 kapaklı toggle · TAM 2 tavan şeridi · TAM 3 kanopi paneli ·
  TAM 10 çentik ibrede · TAM 1 pirinç kol · TAM 1 küre · TAM 1
  tekrarlayıcı lamba
□ ⭐ p1 gerçekten ARKADAN mı (koltuk sırtları kadrajın öznesi)? Yandan
  ya da önden çıktıysa at — filmin kabin dili budur
□ ⭐ p2 ↔ p4 tek fark SEGMENTLERİN/ŞERİTLERİN YANIK-SÖNÜK olması mı?
□ p2'de yalnız ÜÇ ışık var mı (küre · fosfor kadran · amber nabız)?
  Tavan şeritleri ve zemin kenar ışığı p2'de SÖNÜK mü?
□ Koltuk sırtı boru çizgisi ince bir ÇİZGİ mi, neon şerit mi? → neonsa at
□ Hiçbir panelde rakam, harf, ekran grafiği, hologram var mı? → at
□ İnsan, el, kask, kanopide yansıyan figür var mı? → at

KARAKTERLER (RE)
□ ⭐ p3 ve p4'te İKİ AYRI İNSAN okunuyor mu?  ← en kritik madde
□ p3'te boy farkı (14 cm) görünüyor mu? (kask tepesi burun hizası)
□ Kırık burun köprüsü ↔ çilli tıraşlı baş ayrımı ilk bakışta var mı?
□ p1'deki adam p3/p4'tekiyle AYNI mı? p2'deki kadın p3/p4'tekiyle
  AYNI mı? → panel arası kayma varsa at
□ İzler doğru ORGANDA mı? (SOL elmacık ↔ SOL kaş)
□ Çizgiler doğru mu? (adam TURKUAZ · kadın AMBER)
□ Sırt DÜZ mü — hiçbir panelde sırt ünitesi var mı? → at [D79]
□ Vizörde üç işaret de var mı: 2 cm çerçeve · yaka mührü · tek
  parlama çizgisi? Yüz tam okunuyor mu? [D95]
□ Vizörde renk / aynalama / çevre yansıması / HUD var mı? → at

HEPSİ
□ AMBER yalnız üç yerde mi: mühendis çizgisi · verici kubbesi (RA p3)
  · hangar içi ışık (RB/RC)? Başka sıcak renk sızdıysa at
□ Beş mavi ayrışıyor mu — gövdeler saten ÇELİK MAVİSİ, suitler MAT
  KOBALT, ikisi aynı tona düşmüşse at (mavi-üstü-mavi kapısı)
□ Turkuaz yalnız BOYA mı? Turkuaz ışık/neon varsa at
□ Seed §1 tablosuna yazıldı
```

---

# 📌 5. SONRAKİ ADIM

```
Bu paket üretilip §4 kapısından geçtikten sonra sahne üretimi başlar:
  KAPI 1 → S21 (yakalayış — RC p3 kadrajı)
  KAPI 2 → S15 (nefes pufları)
  KAPI 3 → S4  (aurora perdesi)
  KAPI 4 → S0  (planetshine paleti)
Kapı sahneleri ve geri çekilme planları: THE_BLUE_DRIFT_PLAN.md →
ÜRETİM PLANI · kapı kayıtları PART_A sonuna TEK SATIR [D74].

⚠️ Bu paket 3-5 dk formatında üçüncü kez yazılıyor (Cold Burn
07.08 · Uphill Dark 17.08). Uphill Dark'ın 4-panel formatı ve üç
önlemi birebir devralındı; bu filmin eklediği tek şey, durum
çiftlerinin ÜÇE çıkması (bacaklar · kollar · ölü/canlı panel) ve
mavi-üstü-mavi ton kilidinin §4'e ayrı madde olarak girmesi.
```


