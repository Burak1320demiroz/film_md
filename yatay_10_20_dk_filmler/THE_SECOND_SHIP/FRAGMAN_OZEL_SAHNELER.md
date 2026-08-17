# 🎥 THE SECOND SHIP — FRAGMANA ÖZEL BEŞ SAHNE

## 16:9 · 5 sahne × 10.000 s · her sahne TEK KESİNTİSİZ ÇEKİM (0 kesme)

### **Toplam üretim: 5 video · 5 imaj · 50.000 saniye ham malzeme**

### _"Cevap veren herkes ölür."_

> **Bu dosya kimin için:** `FRAGMAN_PRO_YATAY.md` kesimi 27 kesmeden
> oluşur ve 27'si de masterda ZATEN üretilmiş kliplerden kırpılır.
> Bu dosya o kesimin **beş kesmesini gösterişli birer yeni çekimle
> değiştirir.** Fragmanın süresi, ritmi ve vuruş ızgarası DEĞİŞMEZ.
>
> **Çapa kaynağı:** `REFERANS_PAKETI.md` · Bible: `README.md`
> **Fragman kesimi:** `FRAGMAN_PRO_YATAY.md` §4 EDL
>
> ⛔ Beş promptun beşi de **self-contained**'dır (AGENTS.md kural ③).
> Hiçbiri "BIBLE'a bak" demez; her biri tek başına çalışır.
>
> ✅ **PROMPT KONTROL KAPISI (görev kartı P): GO** — 10 promptun 10'u
> betikten geçti (çıkış kodu 0 · 0 BLOCK · 0 FIX). Video promptları
> 2.220–2.595 karakter, yani bandın (2.000–2.600) içinde. Image
> promptları 1.930–2.645; betik image uzunluğunu "karar bekliyor"
> olarak işaretler ve bulgu saymaz (depodaki hiçbir film o bandı
> tutmuyor). **Üretime girmeden önce betiği tekrar koş:**
> `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <bu dosya>`

---

## ⭐ NEDEN BU BEŞİ — ve neden tam bu beş yer

Kırpma tabanlı bir fragmanın tek zayıf noktası şudur: **master, fragman
için çekilmedi.** Filmin sahneleri anlatıyı taşımak üzere kadrajlanmıştır,
afiş olmak üzere değil. Bu beş sahne o boşluğu kapatır — beşi de filmde
**var olan bir olgunun, filmde çekilmemiş kadrajıdır.**

```
⛔ BEŞİNİN DE UYDUĞU KURAL — pazarlıksız:
   yeni hikaye YOK · yeni varlık YOK · yeni novum YOK · yeni mekan YOK
   Beşi de kaynak filmde kurulmuş bir gerçeğin daha geniş, daha yüksek
   ya da daha alçak bir açısıdır. Fragman ikinci bir film değildir.
```

|   #    | Sahne     | Ne veriyor                                        | Kadro | Yol |
| :----: | --------- | ------------------------------------------------- | :---: | :-: |
| **F1** | **ÇİFT**  | Filmin BAŞLIĞI tek karede: gemi ve ikizi yan yana |   2   |  A  |
| **F2** | **TARLA** | 200 yılın ölçeği: onlarca çift, ufka kadar        |   0   |  B  |
| **F3** | **ÇİZGİ** | Silah — ve hiç silah gibi durmuyor                |   0   |  B  |
| **F4** | **YARIM** | 🔥 AFİŞ: metalin taşa döndüğü bant                |   2   |  A  |
| **F5** | **SAYIM** | Sayım bozuluyor: hepsi gri, biri beyaz            |  0+B  |  A  |

```
A YOLU = 8 s native üretim → extend → 10.000 s'ye kırp
B YOLU = 8 s üretim → 0.8× retime → 10.000 s
⚠️ B yolu YALNIZ figürsüz kadrolarda (F2, F3). Yürüyen/eğilen figür
   olan hiçbir sahnede kullanılmaz — 0.9g yalanı görünür hale gelir.
```

---

# 1. 🎞️ KESİME NASIL GİRİYORLAR — sıfır yeniden hesaplama

> ⭐ **Beş sahnenin beşi de DROP-IN'dir.** Her biri `FRAGMAN_PRO_YATAY.md`
> EDL'sindeki bir kesmenin **tam olarak aynı vuruş sayısını** kaplar.
> Fragmanın toplam süresi 100.000 s, vuruş sayısı 160 ve ölçü sayısı 40
> olarak **değişmeden kalır.** Müziği yeniden kesmek gerekmez.

| Sahne  | Hangi kesmenin yerine       | FRAGMAN TC |   IN → OUT    | SÜRE  |  ♩  |
| :----: | --------------------------- | :--------: | :-----------: | :---: | :-: |
| **F3** | C8 (S11 · yükselen çizgi)   |  0:44.375  | 4.000 → 7.750 | 3.750 |  6  |
| **F1** | C14 (S29 · ufuktaki siluet) |  1:05.000  | 5.000 → 8.750 | 3.750 |  6  |
| **F2** | C16 (S34 · tarlaya giriş)   |  1:11.875  | 3.000 → 6.750 | 3.750 |  6  |
| **F4** | C17 (S35 · ikinci gemi) 🔥  |  1:15.625  | 2.500 → 7.500 | 5.000 |  8  |
| **F5** | C18 (S38 · figür)           |  1:20.625  | 6.000 → 8.500 | 2.500 |  4  |

```
KONTROL: 6 + 6 + 6 + 8 + 4 = 30 vuruş
         değiştirilen kesmelerin toplamı da 30 vuruş → fark 0 ✓

⚠️ HEPSİNİ BİRDEN DEĞİŞTİRMEK ZORUNDA DEĞİLSİN. Beşi bağımsızdır;
   yalnız F4'ü üretip kalan 26 kesmeyi masterdan almak da geçerli
   bir teslimdir. Her sahne kendi başına drop-in'dir.

⭐ HER KLİP 10.000 s ÜRETİLİR AMA KESİME 2.5-5.0 s GİRER.
   Bu israf değil, sigortadır: kırpma noktası kurguda kayarsa
   klibin iki yanında 2-5 saniyelik pay durur. Bir klibi yeniden
   üretmek, on saniye üretmekten pahalıdır.
```

---

# 2. ⚓ ÇAPA BLOKLARI — beş promptta kelimesi kelimesine aynı

> `REFERANS_PAKETI.md`'den birebir kopyalandı, tek kelime değişmedi
> [`SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1]. Aşağıdaki sıkıştırılmış biçim
> prompt gövdesine girer; sekiz zorunlu alanın (yaş+rol · boy · gövde
> tipi · ten · saç · yara izi ve tarafı · takviye rengi · vizör durumu)
> biri düşerse kimlik kayması başlar [Ders 55].

```
KAPTAN:   a 41-year-old woman pilot, 1.68 m, slim — light olive skin,
          a fine faded white scar splitting her LEFT eyebrow, dark
          brown hair in a low bun, dark grey-blue suit with ORANGE
          worn reinforcement, helmet on, visor transparent

MÜHENDİS: a 33-year-old man flight engineer, 1.81 m, broad-shouldered —
          light brown skin, short three-day stubble, a 2 cm burn scar
          on his RIGHT cheekbone, very short black hair, the same dark
          grey-blue suit with TEAL GREEN reinforcement and an oversized
          back tool module, helmet on, visor transparent

BEKÇİ:    a tall sealed figure in an unfamiliar white pressure suit,
          exactly 2.10 m — seamless, flawlessly pearl-white, no wear,
          no dust, no panel lines; human skeletal proportions but LONG
          arms with fingertips at knee level; a smooth featureless
          helmet with one opaque dark grey-green visor

CANTOR:   a 31-meter two-crew cargo courier — boxy dark grey-brown
          panelling with mismatched patch panels in three grey tones,
          protruding pipe runs, a narrow forward cockpit, two large
          aft cargo bays, three-legged gear with a 9-meter footprint,
          thin faded orange stripes, dust and heat staining everywhere

HASAR:    a 1.2-meter perfectly circular hole with clean, glassy,
          faintly pearlescent edges in the upper surface of the RIGHT
          rear cargo bay; the RIGHT main leg collapsed and the hull
          tilted exactly 4 degrees to the right

KARIŞMA:  Orange stays on the woman, teal on the man, never swapped;
          his head sits 13 cm higher. Her scar stays on her LEFT
          eyebrow, his on his RIGHT cheekbone.

KOPYA:    matte, bone-grey, stone-textured. The original's SHAPE, none
          of its COLOUR. Never glows, never emits light, never shimmers.
```

## 🚫 Negatif çekirdek — beş promptun beşine gömülü

```
Single unbroken take, no cuts, no transitions, no camera shake, no
speed ramp, no slow motion. CHARACTER COUNT LOCK: exactly [N] human
figures — no duplicates, no extra people, no crowd. Copy material is
matte bone-grey stone — it never glows, never emits light, never
shimmers, and never carries the colour of the original. Growth is
never visible in real time; the ground is static inside the take. No
bloom, no glow filter, no lens flare, no waxy skin, no face morphing.
Visors carry zero tint and stay optically clear — distinct glass
surfaces in every frame, never a mirror coating. No back-mounted
thrusters, wings or tanks on any suit. No readable text, letters,
digits, insignia or symbols on any panel, hull or surface. No
subtitles, no captions, no title card, no watermark. All dust obeys
0.9g — it falls and comes to rest, never hovers, never swirls. Sound
exists but is muffled and low — thin atmosphere, not vacuum.
Photorealistic, 35mm anamorphic film grain.
```

---

# 3. 🔒 ÜRETİM SIRASI — kapı önce, ucuz sonra

```
1) F4  YARIM  🔥 ⛔ KAPI SAHNESİ
      Fragmanın afişi budur. Çıkmıyorsa kalan dördüne para harcanmaz —
      afişsiz bir trailer'ın gösterişli dört sahnesi hiçbir işe yaramaz.
      Bütçe payı: %35 · 6 varyasyon planla

2) F1  ÇİFT
      Filmin başlığını taşıyan kare. İki kadrajda da CANTOR + ikizi
      aynı geometride olmalı — F4'ün geçiş bandı dili buraya taşınır.
      Bütçe payı: %20 · 4 varyasyon

3) F5  SAYIM
      ⚠️ Bu dosyanın TEK pahalı riski (aşağıda). Bekçi kadraja giriyor.
      Bütçe payı: %20 · 5 varyasyon

4) F2  TARLA
      Figürsüz, uzak, defokuslu — kimlik riski sıfır.
      Bütçe payı: %15 · 3 varyasyon

5) F3  ÇİZGİ
      Kadroda iki şey var: bir çizgi ve karanlık. En ucuz sahne.
      Bütçe payı: %10 · 2 varyasyon
```

## 🚨 RİSK KAYDI — dürüst

```
RİSK SAYIMI: 3 / 9
  · Kart 3  kask + vizör        → F1, F4 (iki insan kasklı)
  · Kart 4  ikinci figür        → F1, F4 (iki insan aynı karede)
  · Kart 6  tanınmayan siluet   → F5 (Bekçi)

YOK OLAN RİSKLER: su yok · canlı doku yok · diyalog yok · patlama yok ·
  kamera hareketi yok (5/5 tam lockoff) · yüz yakın çekimi yok

⛔ TEK GERÇEK RİSK F5'TİR ve sebebi Ders 2'dir (anatomi morphu).
   Bekçi 10 saniye boyunca kadrajda ve uzuv sayısı, siluet, boy,
   omuz genişliği klip boyunca sabit kalmalı. Bu dosyada risk üç
   sayıyla bastırılmıştır:
     ① Bekçi kadrajın %6'sını kaplar (uzak) — morph yüzeyi küçük
     ② Bekçi 10 saniyenin 10'unda HAREKETSİZ ve SIRTI DÖNÜK
     ③ Kesime giren dilim 2.500 s — masterdaki en kısa Bekçi
        maruziyeti
   Üçü de "Bekçi'yi ucuza çekmenin" bilinen tek yoludur.
```

---

## 🎬 SAHNE F1 — ÇİFT

`kesime: 1:05.000` · 32mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** ÇAPA A + ÇAPA B + ÇAPA D + HASAR (start frame'e yükle)

_"Filmin adı bu karede duruyor."_

```
⚙️ SAHNE KARTI
  Tek çekim · 0 KESME · 10.000 s · kamera tam sabit.
  İŞLEV: fragmanın sayımı burada geminin KENDİSİNE iner. Seyirci
         onlarca enkazın ikizini gördü; şimdi KAHRAMAN GEMİNİN
         ikizini görüyor. Filmin başlığı açıklanmadan anlaşılıyor.
  ⭐ GEOMETRİ KİLİDİ: iki gövde de tam 4 derece sağa yatık, ikisinde
     de sağ ana bacak çökük, ikisinde de 1.2 m'lik daire delik.
     Kopya orijinali DEĞİL — orijinalin O ANKİ HÂLİNİ kopyalıyor.
     Bu, novum'un en zarif kanıtıdır ve tek karede okunur.
  ⛔ Kopyanın tabanı hâlâ zemine bağlı: ayrılmış bir gemi değil,
     büyümekte olan bir gemi.
  🎞️ Kesime IN 5.000 → OUT 8.750 girer (3.750 s · 6 vuruş).
```

### 📸 IMAGE PROMPT

```
SCENE:
A wide dawn view across a dark basalt plain. Two identical 31-meter
cargo ships stand twelve meters apart, side by side. The LEFT one is
real: dark grey-brown panelling, mismatched patch panels in three
grey tones, protruding pipe runs, dust and heat staining. The RIGHT
one is its exact twin rendered in matte bone-grey stone, the same
hull, the same panels, the same proportions — but colourless, dull
and stone-textured, its lower third still fused to the ground it grew
out of. Both hulls' noses point away from camera toward the far haze.
Both rest tilted exactly 4 degrees to the right on a collapsed right
main leg, and both carry a 1.2-meter perfectly circular hole in the
upper surface of the right rear cargo bay.

FIGURES — exactly 2 human figures, small at the bottom of frame:
LEFT: a 41-year-old woman pilot, 1.68 m, slim, dark grey-blue suit
with ORANGE worn reinforcement, helmet on, visor transparent.
RIGHT: a 33-year-old man flight engineer, 1.81 m, broad-shouldered,
the same suit with TEAL GREEN reinforcement and an oversized back
tool module, helmet on, visor transparent. His head sits 13 cm
higher. They stand between the two hulls, dwarfed by both.

ENVIRONMENT:
A rocky world, 0.9g, thin 0.6 atmosphere. Pale grey-green sky, one
large pale moon high in the upper LEFT, visible in daylight. Low
haze flattens the far plain into grey bands.

LIGHTING:
A small orange star newly risen at 4400K raking from the LEFT,
roughly seventy percent of Earth daylight. Long soft-edged shadows
run to screen-right from both hulls and both figures.

COMPOSITION:
32mm anamorphic, camera locked off nine meters above the ground,
level with the horizon. Horizon on the upper third line. Deep focus.

NEGATIVE:
Copy material is matte bone-grey stone — it never glows, never emits
light, never shimmers, and never carries the colour of the original.
Growth is never visible; the ground is static. CHARACTER COUNT LOCK:
exactly 2 human figures — no third person, no crowd, no duplicate
face. Orange stays on the woman, teal on the man. Visors carry zero
tint and stay optically clear, never a mirror coating. No
back-mounted thrusters, wings or tanks on either suit. No fire,
smoke, sparks or explosion. No bloom, no glow filter, no lens flare.
No readable text, letters, digits or insignia on any hull or panel.
No subtitles, captions, title card or watermark. All dust obeys
0.9g. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff nine meters
above the ground, level with the horizon, no cuts, no camera
movement:

FRAME: two identical 31-meter cargo ships twelve meters apart on a
dark basalt plain at dawn. LEFT: the real ship, dark grey-brown
panelling, mismatched patch panels, dust and heat staining. RIGHT:
its exact twin in matte bone-grey stone, colourless and dull, its
lower third still fused to the ground. Both hulls' noses point away
from camera toward the far haze. Both tilted exactly 4 degrees to
the right on a collapsed right main leg, both carrying a 1.2-meter
perfectly circular hole in the right rear cargo bay. Between them,
exactly 2 human figures, small: LEFT a 41-year-old woman pilot,
1.68 m, ORANGE worn reinforcement on a dark grey-blue suit; RIGHT a
33-year-old man flight engineer, 1.81 m, broad-shouldered, TEAL
GREEN reinforcement and an oversized back tool module. Both
helmeted, visors transparent. A small orange star at 4400K rakes
from the LEFT; long soft-edged shadows run to screen-right.

0s — Total stillness. Both hulls hold their identical tilt. Both
figures stand between them, looking at the stone twin.
3s — A thin, weak veil of low dust drifts across the base of the
stone hull from LEFT to RIGHT, grain-textured and dry. Neither hull
changes.
6s — The veil thins and settles. A few grains trickle off the stone
hull's lower edge and come to rest against its fused base.
8s — Stillness again. The woman's helmet turns a few degrees to the
RIGHT and stops.
10s — Both hold, small between the two hulls. No cuts.

Growth is never visible in real time; the ground is static inside
the take. Copy material is matte bone-grey stone — it never glows,
never emits light, never shimmers, and never carries the original's
colour. CHARACTER COUNT LOCK: exactly 2 human figures — no third
person, no crowd, no duplicate. Orange stays on the woman, teal on
the man; the 13 cm height gap holds. No tall sealed white figure, no
tower. No fire, smoke, sparks or explosion. Visors carry zero tint
and stay optically clear. No back-mounted thrusters or tanks on
either suit. All dust obeys 0.9g — it falls and comes to rest, never
hovers, never swirls. Sound exists but is muffled and low — thin
atmosphere, not vacuum. The camera never moves, drifts, zooms or
tilts. No cuts, transitions, camera shake or speed ramp. No bloom,
no glow filter, no lens flare. No readable text, letters, digits or
insignia. No subtitles, captions or watermark. Photorealistic, 35mm
anamorphic film grain.
```

---

## 🎬 SAHNE F2 — TARLA

`kesime: 1:11.875` · 32mm · kadro 0 · fixed lockoff · **B yolu (retime)**
📎 **REFERANS:** ÇAPA D + KOPYA (start frame'e yükle)

_"Bir gemi mezarlığı değil. Bir gemi fidanlığı."_

```
⚙️ SAHNE KARTI
  Tek çekim · 0 KESME · 10.000 s · kamera tam sabit.
  İŞLEV: 200 yılın ölçeği. Filmde tarla hep İÇİNDEN çekildi (şerit,
         tek gemi); toplam büyüklüğü veren tek kadraj yok. Bu o kadraj.
  ⭐ SAYIM DERSİ: kadrajdaki her gövdenin YANINDA tam ikizi var.
     Seyirci saymayı öğreniyor — F5'te sayım bozulacak.
  ⛔ KADRODA İNSAN YOK. Ölçeği figür değil, TEKRAR veriyor. Figür
     koyulursa göz figüre gider ve tarla arka plana düşer.
  🎞️ Kesime IN 3.000 → OUT 6.750 girer (3.750 s · 6 vuruş).
```

### 📸 IMAGE PROMPT

```
SCENE:
A very wide elevated view across a vast plain filled with grounded
ship hulls arranged in pairs, receding in rough parallel lanes until
they dissolve into haze. Each pair is the same hull twice: one
weathered dark grey-brown metal wreck, and beside it its exact twin
in matte bone-grey stone, half-risen and still fused to the ground
at its base. Every hull's nose points away from camera toward the
far haze, so the lanes read as long rows of sterns. The pairs are at
different stages: some stone twins are barely a raised outline in
the dust, some are recognisable rough forms, some are complete.

ENVIRONMENT:
A rocky world, 0.9g, thin 0.6 atmosphere. Dark basalt ground between
the lanes, dry and even-grained. A pale grey-green sky fills the top
quarter of frame with one large pale moon high in the upper RIGHT,
visible in daylight. Low haze flattens the far half of the field
into stacked grey bands.

LIGHTING:
A small orange star low on the horizon at 4400K raking from the
LEFT, roughly seventy percent of Earth daylight. Every hull throws a
long soft-edged shadow to screen-right, and the shadows form their
own repeating pattern across the ground.

COMPOSITION:
32mm anamorphic, camera locked off sixty meters above the ground,
angled fifteen degrees down across the field. Horizon on the upper
quarter line. Deep focus from the near lane to the haze.

NEGATIVE:
Copy material is matte bone-grey stone — it never glows, never emits
light, never shimmers, and never carries the colour of the original.
Growth is never visible; the ground is static. CHARACTER COUNT LOCK:
exactly 0 human figures — no people, no crew, no crowd, no standing
white figure, no tall sealed suit, no tower. No fire, smoke, sparks,
explosion or burning wreck. No bloom, no glow filter, no lens flare.
No readable text, letters, digits, insignia or hull markings on any
surface. No subtitles, captions, title card or watermark. All dust
obeys 0.9g — it lies flat and at rest, never hovers. Photorealistic,
35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff sixty meters
above the ground, angled fifteen degrees down, no cuts, no camera
movement:

FRAME: a vast plain filled with grounded ship hulls in pairs,
receding in rough parallel lanes into haze. Each pair is the same
hull twice: one weathered dark grey-brown metal wreck, beside it its
exact twin in matte bone-grey stone, half-risen and fused to the
ground at its base. Every hull's nose points away from camera toward
the far haze. The pairs sit at different stages — some stone twins a
raised outline, some rough forms, some complete. Pale grey-green sky
across the top quarter, one large pale moon upper RIGHT. A small
orange star at 4400K rakes from the LEFT; every hull throws a long
soft-edged shadow to screen-right.

0s — Total stillness across the whole field. Nothing moves anywhere
in frame. Every shadow holds its length.
3s — A thin, weak veil of low dust drifts along the nearest lane
from LEFT to RIGHT, grain-textured and dry, no higher than the
landing gear. The hulls do not change.
6s — The veil thins and settles back onto the ground. In the far
haze the shapes stay exactly as they were, flat and grey.
8s — Stillness again — the same lanes, the same pairs, the same
shadows, exactly as at 0s.
10s — The frame holds unchanged to the final frame. No cuts.

Growth is never visible in real time; the ground is static inside
the take. Nothing rises, grows or changes shape anywhere in frame.
Copy material is matte bone-grey stone — it never glows, never emits
light, never shimmers, and never carries the original's colour.
CHARACTER COUNT LOCK: exactly 0 human figures — no people, no crew,
no crowd, no standing white figure, no tall sealed suit, no tower.
No fire, smoke, sparks or explosion. All dust obeys 0.9g — it falls
and comes to rest, never hovers, never swirls. Sound exists but is
muffled and low — thin atmosphere, not vacuum. The camera never
moves, drifts, zooms or tilts. No cuts, transitions, camera shake,
speed ramp or slow motion. No bloom, no glow filter, no lens flare.
No readable text, letters, digits, insignia or hull markings. No
subtitles, captions, title card or watermark. Photorealistic, 35mm
anamorphic film grain.
```

---

## 🎬 SAHNE F3 — ÇİZGİ

`kesime: 0:44.375` · 32mm · kadro 0 · fixed lockoff · **B yolu (retime)**
📎 **REFERANS:** yok — kadro 0, ölçeksiz gece. Referans imaj EKLEME.

_"Işın değil. Çizgi."_

```
⚙️ SAHNE KARTI
  Tek çekim · 0 KESME · 10.000 s · kamera tam sabit.
  İŞLEV: silah fragmanda ilk ve tek kez görülüyor, ve hiç silah gibi
         durmuyor. Ne patlama var, ne ışın, ne renk — bir GEOMETRİ var.
  ⛔ SAHNENİN TEK KURALI: ÖLÇEK OKUNMAMALI. Kadrajda boyu bilinen
     hiçbir nesne olamaz — gemi, figür, krater, kaya yok. Çizginin ne
     kadar büyük olduğu bilgisi filmde verilir, fragmanda değil.
  ⛔ YASAK KELİMELER (Ders 67): laser, beam, weapon, cannon, blast.
     Kullanılan dil: "a perfectly straight thin white line".
     "Laser" yazarsan model bilim-kurgu ışını çizer — halo, titreme,
     renk. Çizgi matematiksel kalmalı.
  🎞️ Kesime IN 4.000 → OUT 7.750 girer (3.750 s · 6 vuruş).
```

### 📸 IMAGE PROMPT

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff at eye level
with the horizon, camera absolutely still for the entire ten
seconds, no cuts, no camera movement:

FRAME: a night view across a rocky plain. From a point beyond the
horizon a perfectly straight, thin white line rises vertically and
crosses the whole height of frame, leaving the top edge — seamless,
uniform in width from base to top, sharp-edged, mathematically
straight. It stands slightly right of the vertical centre axis. A
dark basalt plain fills the lower two thirds as near-silhouette,
with no craters, no boulders and no landmarks of known size.
Near-black sky above, one large pale grey-blue moon upper LEFT,
sparse hard stars, a thin haze band along the horizon. Moonlight
rakes from the LEFT at 7000K, very low level.

0s — The frame is completely still. The line reads as an even soft
sheen on the screen-left face, deep grey on the screen-right face.
3s — A thin, weak veil of low dust drifts slowly across the base of
frame from LEFT to RIGHT, no more than a hand's width of the image,
grain-textured and dry. The line does not change at all.
6s — The veil thins and begins to settle back toward the ground. The
horizon haze breathes very faintly. Nothing else moves.
8s — The last dust comes to rest. The line is exactly as it was at
0s — same width, same brightness, same position, perfectly plumb.
10s — Absolute stillness holds to the final frame. No cuts.

The white line never moves, grows, shortens, curves, tapers,
flickers, thickens, pulses or changes colour. It emits no light of
its own — no halo, no bloom, no glow, no lens flare, no light spill
on the ground, no volumetric shafts, no god rays. No explosion, no
fire, no sparks, no smoke, no impact, no debris. CHARACTER COUNT
LOCK: exactly 0 human figures — no people, no ship, no vehicle, no
structure, no landmarks of known size. The ground is static: nothing
rises from it and nothing grows. All dust obeys 0.9g — it falls and
comes to rest, never hovers, never swirls. Sound exists but is
muffled and low — thin atmosphere, not vacuum. The camera never
moves, drifts, zooms or tilts. No cuts, transitions, camera shake,
speed ramp or slow motion. No readable text, letters, digits or
symbols. No subtitles, captions, title card or watermark.
Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE F4 — YARIM 🔥 AFİŞ

`kesime: 1:15.625` · 32mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** ÇAPA A + ÇAPA B + ÇAPA D + KOPYA (start frame'e yükle)

_"Bu gezegen tehlikeli değil. Bu gezegen SABIRLI."_

```
⚙️ SAHNE KARTI
  Tek çekim · 0 KESME · 10.000 s · kamera tam sabit.
  ⛔ KAPI SAHNESİ — üretim buradan başlar. Çıkmazsa diğer dördü
     üretilmez.
  İŞLEV: filmin novum'u tek karede, sıfır açıklamayla. Fragmanın
         afişi, kapak fotoğrafı ve en paylaşılabilir karesi budur.
  ⭐ GEÇİŞ BANDI — bu sahnenin tek gerçek fikri: gövdenin ortasından
     çapraz geçen bir bant boyunca koyu gri-kahve METAL, kemik grisi
     TAŞA dönüyor. Panel kenarları yumuşuyor, boru hatları taş
     kabartmaya iniyor, cıvatalar körelmiş yumrulara dönüyor.
     Bant KESKİN DEĞİL — 2 metrelik bir geçiş bölgesi.
  ⛔ Gövdenin alt üçte biri hâlâ zemine BAĞLI. Bu bir enkaz değil,
     büyümekte olan bir şey.
  ⭐ ALÇAK AÇI ZORUNLU: kamera zeminden 1.2 m'de, yukarı bakıyor.
     Gövde izleyicinin üstüne geliyor. Yüksek açı bu kareyi öldürür.
  🎞️ Kesime IN 2.500 → OUT 7.500 girer (5.000 s · 8 vuruş) —
     fragmanın en uzun ikinci kesmesi.
```

### 📸 IMAGE PROMPT

```
SCENE:
A low wide dawn view looking up at a single enormous ship hull
rising out of the ground. The hull is a 31-meter boxy cargo ship,
and it is half-finished: across a diagonal transition band running
through its middle, dark grey-brown metal panelling gives way to
matte bone-grey stone. On the metal side, mismatched patch panels,
protruding pipe runs and heat staining read clearly. Across the two
meter transition zone, panel edges soften and swell, pipe runs sink
into stone relief, and bolt heads become blunted nubs. Below the
band the entire lower third of the hull is unbroken stone, still
fused to the ground it is growing out of, with no gap and no shadow
beneath it. The hull's nose points away from camera toward the haze.

FIGURES — exactly 2 human figures, tiny at the very bottom of frame:
LEFT: a 41-year-old woman pilot, 1.68 m, slim, dark grey-blue suit
with ORANGE worn reinforcement, helmet on, visor transparent.
RIGHT: a 33-year-old man flight engineer, 1.81 m, broad-shouldered,
the same suit with TEAL GREEN reinforcement and an oversized back
tool module, helmet on, visor transparent. His head sits 13 cm
higher. Both stand at the base, dwarfed by the hull above them.

ENVIRONMENT:
A rocky world, 0.9g, thin 0.6 atmosphere. Dark basalt ground. Pale
grey-green sky filling the upper half behind the hull, one large
pale moon high in the upper RIGHT.

LIGHTING:
A small orange star newly risen at 4400K raking from the LEFT,
roughly seventy percent of Earth daylight. The metal side catches a
measured, controlled specular; the stone side stays completely
matte. Long soft-edged shadows run to screen-right.

COMPOSITION:
32mm anamorphic, camera locked off 1.2 meters above the ground
angled upward, so the hull looms over the lens. The transition band
crosses frame diagonally through the centre. Deep focus.

NEGATIVE:
Copy material is matte bone-grey stone — it never glows, never emits
light, never shimmers, and never carries the colour of the original.
Growth is never visible in real time; the hull and ground are static.
The transition band never moves or spreads within the shot.
CHARACTER COUNT LOCK: exactly 2 human figures — no third person, no
crowd, no duplicate face. Orange stays on the woman, teal on the
man. Visors carry zero tint and stay optically clear, never a mirror
coating. No back-mounted thrusters, wings or tanks on either suit.
No fire, smoke, sparks or explosion. No bloom, no glow filter, no
lens flare. No readable text, letters, digits or insignia on any
hull or panel. No subtitles, captions, title card or watermark. All
dust obeys 0.9g. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff 1.2 meters above
the ground angled upward, no cuts, no camera movement:

FRAME: a single enormous 31-meter boxy cargo hull rising out of the
ground at dawn, looming over the lens. It is half-finished: a
diagonal transition band crosses frame through the centre, and along
it dark grey-brown metal gives way to matte bone-grey stone. On the
metal side, mismatched patch panels, pipe runs and heat staining. Across the two meter transition zone, panel edges
soften and swell, pipe runs sink into stone relief, bolt heads
become blunted nubs. Below the band the lower third is unbroken
stone fused to the ground. The hull's nose points away from camera
toward the haze. At the very bottom of frame, exactly 2 human
figures, tiny: LEFT a 41-year-old woman pilot, 1.68 m, ORANGE
reinforcement on a dark grey-blue suit; RIGHT a 33-year-old man
flight engineer, 1.81 m, broad-shouldered, TEAL GREEN reinforcement
and an oversized back tool module. Both helmeted, visors
transparent. A small orange star at 4400K rakes from the LEFT; the
metal catches a measured specular, the stone stays matte.

0s — Total stillness. The hull holds. Both figures stand at the
base, heads tipped back.
3s — A thin, weak veil of low dust drifts across the base of the
hull from LEFT to RIGHT, dry and grain-textured. The hull does not
change; the band does not move.
6s — The veil thins and settles. A few grains trickle down the stone
face and come to rest.
8s — Stillness again. The woman's helmet tips further back and stops.
10s — Both hold, tiny beneath the hull. No cuts.

Growth is never visible; the hull and ground are static inside the
take, and the transition band never moves or spreads.
Copy material is matte bone-grey stone — it never glows, never emits
light and never carries the original's colour. CHARACTER COUNT LOCK:
exactly 2 human figures — no third person, no crowd, no duplicate.
Orange stays on the woman, teal on the man; the 13 cm height gap
holds. No tall sealed white figure, no tower. No fire, smoke, sparks
or explosion. Visors carry zero tint and stay optically clear. No
back-mounted thrusters or tanks on either suit. All dust obeys
0.9g — it falls and comes to rest, never hovers, never swirls. Sound
exists but is muffled and low — thin atmosphere, not vacuum. The
camera never moves, drifts, zooms or tilts. No cuts, transitions,
camera shake or speed ramp. No bloom, no glow filter, no lens flare.
No readable text, letters, digits or insignia. No subtitles,
captions or watermark. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE F5 — SAYIM

`kesime: 1:20.625` · 32mm · kadro 0+B · fixed lockoff · **A yolu**
📎 **REFERANS:** ÇAPA C + KOPYA (start frame'e yükle)

_"Hepsi gri. Biri değil."_

```
⚙️ SAHNE KARTI
  Tek çekim · 0 KESME · 10.000 s · kamera tam sabit.
  İŞLEV: fragmanın mekaniği burada BOZULUYOR. Dört sahne boyunca
         "her şeyin ikizi var" diye sayan seyirci, sayıya UYMAYAN
         tek şeyi görüyor.
  ⭐ KOMPOZİSYON FİKRİ: şeridin iki yanında sıra sıra BOŞ TAŞ SUIT
     duruyor — kopyalanmış ama içi olmayan insanlar, mezar taşı gibi.
     Hepsi mat kemik grisi. Şeridin sonunda, uzakta, TEK bir figür
     kusursuz inci beyazı ve sırtı dönük.
  ⛔ BEKÇİ 10 SANİYENİN 10'UNDA HAREKETSİZ VE SIRTI DÖNÜK.
     Dönmüyor, adım atmıyor, kol kaldırmıyor. Ders 2 riski (anatomi
     morphu) yalnızca böyle bastırılır: hareket yoksa morph da yok.
     Dönüş fragmanın BAŞKA bir kesmesinde (C20) ve masterdan gelir.
  ⛔ Bekçi kadrajın en fazla %6'sını kaplar. Yaklaşırsa bu sahne
     F5 olmaktan çıkar, Bekçi portresi olur — ve pahalıya patlar.
  🎞️ Kesime IN 6.000 → OUT 8.500 girer (2.500 s · 4 vuruş) —
     fragmanın en kısa Bekçi maruziyeti.
```

### 📸 IMAGE PROMPT

```
SCENE:
A wide daylight view straight down a long lane between two rows of
grounded ship hulls. Standing along both edges of the lane, spaced
evenly like markers, are fourteen empty pressure suits rendered
entirely in matte bone-grey stone — upright, arms at their sides,
helmets on, and where each visor should be there is only a deep oval
recess of shadow with nothing behind it. They are hollow copies:
stone-textured, colourless, dull, each still fused to the ground at
the boots. At the far end of the lane, small in the distance, stands
one single figure that does not match: a tall sealed figure in a
flawlessly pearl-white pressure suit, exactly 2.10 m, seamless, with
no wear, no dust and no panel lines, its back turned to the camera,
completely still. Its arms are long, the fingertips at knee level.

ENVIRONMENT:
A rocky world, 0.9g, thin 0.6 atmosphere. Dark basalt lane floor.
The flanking hulls are weathered dark grey-brown metal, their noses
pointing away from camera, and they frame the lane on both sides. A
pale grey-green sky above, one large pale moon high in the upper
LEFT.

LIGHTING:
A small orange star at 4400K raking from the LEFT, roughly seventy
percent of Earth daylight. Long soft-edged shadows from every stone
suit run to screen-right across the lane floor in a repeating
pattern. The white figure stays matte and carries only a clean,
measured specular.

COMPOSITION:
32mm anamorphic, camera locked off 1.6 meters above the lane floor,
level, looking straight down the lane. The white figure sits on the
vertical centre axis at the far end, occupying a small part of the
frame. Deep focus.

NEGATIVE:
Copy material is matte bone-grey stone — it never glows, never emits
light, never shimmers, and never carries the colour of the original.
The white suit is matte and never glows. Growth is never visible;
the ground is static. CHARACTER COUNT LOCK: exactly 0 human figures,
exactly 1 tall sealed white figure and exactly 14 empty stone suits
— no crowd, no duplicate of the white figure, no faces anywhere. The
stone visor recesses stay empty — no eyes, no face, no light behind
them. No fire, smoke, sparks or explosion. No bloom, no glow filter,
no lens flare. No readable text, letters, digits or insignia. No
subtitles, captions, title card or watermark. All dust obeys 0.9g.
Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff 1.6 meters above
the lane floor, level, looking straight down the lane, no cuts, no
camera movement:

FRAME: a long lane between two rows of weathered dark grey-brown
ship hulls whose noses point away from camera. Along both edges of
the lane stand fourteen empty pressure suits rendered entirely in
matte bone-grey stone — upright, arms at their sides, helmets on,
each visor a deep oval recess of shadow with nothing behind it, each
fused to the ground at the boots. At the far end of the lane, small
on the vertical centre axis, stands one tall sealed figure in a
flawlessly pearl-white pressure suit, exactly 2.10 m, seamless, no
wear, no panel lines, arms long with fingertips at knee level, its
back turned to the camera. A small orange star at 4400K rakes from
the LEFT; long soft-edged shadows run to screen-right in a repeating
pattern.

0s — Total stillness down the whole lane. Every stone suit holds its
shadow. The white figure stands with its back turned, motionless.
3s — A thin, weak veil of low dust drifts along the lane floor from
LEFT to RIGHT, no higher than the boots. Nothing else changes.
6s — The veil thins and settles. The stone suits are exactly as they
were. The white figure has not moved a millimetre.
8s — Stillness holds. The tension is the stillness itself — fourteen
grey forms and one white one.
10s — The frame ends unchanged, the white figure still turned away.
No cuts.

The white figure never turns, never steps, never raises an arm and
never changes silhouette: its height, shoulder width, limb count and
proportions are identical in every frame — no morphing, no stretching,
no extra limbs, no fabric ripple. Its suit is a rigid shell. Copy
material is matte bone-grey stone — it never glows, never emits
light and never carries the original's colour. Growth is never
visible; the ground is static inside the take. CHARACTER COUNT LOCK:
exactly 0 human figures, exactly 1 tall sealed white figure and
exactly 14 empty stone suits — no crowd, no duplicate, no faces
anywhere. The stone visor recesses stay empty — no eyes, no face, no
light behind them. No fire, smoke, sparks or explosion. All dust
obeys 0.9g — it falls and comes to rest, never hovers, never swirls.
Sound exists but is muffled and low — thin atmosphere, not vacuum.
The camera never moves, drifts, zooms or tilts. No cuts, transitions,
camera shake or speed ramp. No bloom, no glow filter, no lens flare.
No readable text, letters, digits or insignia. No subtitles, captions
or watermark. Photorealistic, 35mm anamorphic film grain.
```

---

# 4. ✅ ÜRETİM KAPISI — her klip teslim edilmeden önce

```
□ 1. SÜRE        klip tam 10.000 s · A yolunda extend sonrası kırpıldı

□ 2. TEK ÇEKİM   klibin İÇİNDE kesme YOK · geçiş YOK · hız rampası YOK
                 ⭐ bu dosyanın adı budur: 5 sahne, 5 çekim, 0 kesme

□ 3. LOCKOFF     5/5 tam sabit. Pan, tilt, zoom, track, el kamerası,
                 kayma — hiçbiri yok. Fragmanın hareketi KURGUDAN gelir.

□ 4. EKRAN METNİ 0.000 s — tek karede bile harf/rakam/insignia yok
                 (bu beş klip Veo çıktısıdır; D70/D72 tam olarak
                  burada geçerlidir, logo bloklarında değil)

□ 5. ÖLÇEK       CANTOR 31 m · Bekçi 2.10 m · Kaptan 1.68 m ·
                 Mühendis 1.81 m · yatıklık 4° · delik 1.2 m
                 F3'te ölçek OKUNMUYOR (ters kontrol)

□ 6. KOPYA       taş mat · parlamıyor · ışık yaymıyor · orijinalin
                 rengini taşımıyor · tabanı zemine bağlı

□ 7. BÜYÜME      klibin içinde hiçbir şey büyümüyor. Büyüme sahneler
                 ARASINDA olur, sahne içinde asla.

□ 8. F5 SİLUET   Bekçi 10 saniyenin 10'unda hareketsiz · sırtı dönük ·
                 uzuv sayısı ve omuz genişliği ilk kareyle son kare
                 üst üste bindirilerek kontrol edildi [Ders 2]

□ 9. VİZÖR       insan vizörleri her karede ayrı bir cam yüzey ·
                 aynalı kaplama yok · renkli tint yok [Ders 79]

□ 10. TOZ        0.9g · toz çöküyor, asılı kalmıyor, girdap yapmıyor

SONUÇ:  □ GO      □ YENİDEN ÜRET (hangi madde: ____)
```

---

> **Bu dosya ne zaman güncellenir**
> □ Bir sahne üretilince → sahne kartına "üretildi · kaç deneme" satırı
> □ Bir sahne kesime girince → `FRAGMAN_PRO_YATAY.md` §4 EDL'de o
> satırın KAYNAK sütunu master sahnesinden F-numarasına çevrilir
> □ Yeni bir red sebebi çıkarsa → `KILAVUZ_REHBERI.md` §7 BİLİNEN TUZAKLAR
> □ Ders çıkarsa → görev kartı G (AGENTS.md §3)
