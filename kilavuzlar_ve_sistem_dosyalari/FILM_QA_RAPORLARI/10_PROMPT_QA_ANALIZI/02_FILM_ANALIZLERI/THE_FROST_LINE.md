# 🧩 THE_FROST_LINE — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara sahne(n) = 9 s + (n−1) × 10 s
HAM RAPOR   13/13 geçerli   ③ kimlik: 9/13 bayrak (sahne 23 ≠ 25 — ölçüm/plan farkı)
BULGU       55 → tekil 51
HÜKÜM       🅐 27 · 🅑 20 · 🅒 2 · 🅓 2
OKUMA       🅑/(🅐+🅑) = %43 → KRONOS'un TERSİ: burada kusur ağırlıklı MOTORDA
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 23/25 · sayı 24/25 · temas 3/25 · giysi 24/25 · parçacık 13/25 · bloom 23/25 · metin 20/25 · efor 24/25 · g-ad 1/25 · g-sayı 24/25 · filigran 23/25 · kamera 23/25
  ⛔ HİÇ YOK: dış-ses
  bulgulu sahnelerde eksik: SES 18/20 · dış-ses 0/20 · sayı 19/20 · temas 2/20 · giysi 19/20 · parçacık 11/20 · bloom 18/20 · metin 17/20 · efor 19/20 · g-ad 0/20 · g-sayı 19/20 · filigran 18/20 · kamera 18/20
```

> ⭐ **Bu dosya kontrol grubudur.** KRONOS'ta %93 🅑 çıktı; burada %43. Fark
> yazım standardıdır ve ölçülebilir: FROST_LINE'ın 50 promptunun **25'inde
> `AUDIO:` satırı**, **28'inde `Exactly one human`**, hepsinde `0% bloom`,
> hepsinde `Suit identical; wear marks and rime never move` var.
> Aynı depo, aynı motor, iki farklı yazım — iki farklı hata dağılımı.

---

## 🅐 MODEL SAPMASI — kilit yazıyordu, tutmadı · 27

### 🅐-1 · Kirlilik/kırağı durum merdiveni yazıldı, motor tutmadı · 6

| S | bulgu |
|:--:|---|
| S02 🔴 | Forearms and knees heavily frosted vs clean grey suit |
| S05 | Thick black back harness appears in S6, absent in S2 |
| S11 | Glove and suit heavily dusted with red soil in S5, pristine clean in S12 |
| S13 | Flat back with no pack vs large grey backpack present |
| S21 | Glove coated in white frost in S21, clean in S22 |
| S21 | Frost accumulates on leaves in S17, fresh unfrosted sprouts in S22 |

**Promptta ne yazıyordu** — her sahnede, harfi harfine:

> `Wear state: PHASE 3 — red dust on both knees and glove palms; a thin matte
> white rime on the suit`
> `NEGATIVE: … Suit identical; wear marks and rime never move.`

Dört fazlı bir **durum merdiveni** yazılmış (PHASE 1→4), her sahne kendi fazını
taşıyor ve negatif "yer değiştirmez" diyor. Kilit bundan daha net yazılamaz.
Motor yine de sahne başına sıfırladı.

**Hüküm 🅐 ×6.** Ders siparişi: durum merdiveni METİNLE tutmuyor →
**referans paketi** gerekir (varlığın iki durumu PANEL olarak kilitlenir, D168).
FROST_LINE'ın referans paketi yok.

### 🅐-2 · Filigran · 2 🔴

| S | bulgu |
|:--:|---|
| S00 🔴 | Static blue triangle logo burned into bottom right corner throughout the entire video |
| S22 🔴 | Static blue triangle watermark in bottom right corner of every scene |

**Promptta ne yazıyordu:** `no watermark` — dosyada **53 kez**. Kilit eksiksiz.

**Hüküm 🅐 ×2 — ve bu bir PROMPT işi değil.** Filigran araç/ihraç kusurudur
[D150]: master yeniden ihraç edilir, promptta yapılacak hiçbir şey yoktur.
⭐ KRONOS'ta da aynı bulgu aynı biçimde çıktı (S25, köşe sparkle) → **iki filmde
tekrar**, ders eşiğini geçti.

### 🅐-3 · Düşük yerçekimi yürüyüşü · 3

| S | bulgu |
|:--:|---|
| S03 | Running feels like slow-motion gliding ("moonwalking"); footsteps lack planted weight |
| S08 | Floaty, weightless running motion despite heavy suit |
| S02 🔴 | Vent gas falls >1g while jog hang time <0.4g |

**Promptta ne yazıyordu** — S02 video gövdesi:

> `Earth with slightly longer strides; only the dust behaves lightly.`
> `Red dust lifts behind each trailing boot and settles within three to …`

Kilit hem yazılı hem sayılı (toz için sönüm süresi verilmiş). Motor gövdeye
uygulamadı, yalnız toza uyguladı — **ikisini ayıran cümle zaten promptta var
ve doğru tarafta duruyordu.**

**Hüküm 🅐 ×3.** ⭐ Ama S02'deki bulgu iki ölçüyü KARŞILAŞTIRIYOR (gaz >1g,
koşu <0,4g). Sonraki filmlerde bu yüzden tek ortam sayısı yazılıyor
(THE_FALLING_WORLD: "0,30 g", her promptta aynı sayı).

### 🅐-4 · Işık ve bloom · 9 · 🅐-5 · Doku yüzmesi · 7

`0% bloom, no glow filter, no soft focus — every surface keeps visible texture`
her negatifte var; S04 · S08 · S01 bloom bulguları buna rağmen çıktı.
Doku yüzmesi (S07 · S09 🔴 · S10) için de `Plants and skin static — no swaying`
yazılı. İkisi de **sayısal olarak yazılmış** kilitlerin tutmadığı yerler.

---

## 🅑 PROMPT BOŞLUĞU · 20

### 🅑-1 · TEMAS SINIRI CÜMLESİ YOK · 5 🔴 · 1 🟠  ⭐ EN AĞIR

| S | bulgu |
|:--:|---|
| S05 🔴 | Hand-surface fusion; fingers merge and phase completely into the greenhouse hull |
| S09 | Object phasing. The roll of tape clips straight through the gloves |
| S10 🔴 | Hands morph and glitch into each other during the clap |
| S14 🔴 | Severe hand geometry breakdown, extra fingers sprout when the glove touches the leaf |
| S14 🔴 | Contact morphing. Extra fingers appear, glove geometry breaks down |
| S20 🔴 | Gloved fingers phase directly through the solid helmet rim |

**Promptta ne yazıyordu:** S05 · S09 · S10 · S14 · S20 — **beşinin de negatifinde
temas cümlesi YOK.** Negatifleri kelimesi kelimesine okundu; taşıdıkları:

> `Exactly one human — no second person. 0% bloom, no glow filter, no soft focus …
> Photorealistic skin — no airbrushing, no face morphing. Suit identical; wear
> marks and rime never move. No readable text anywhere; no subtitles, no watermark.`

`no face morphing` var, **el-yüzey teması yok.** Filmin bütününde `no merging`
10 kez geçiyor ama **temas BLOCKER'ının düştüğü beş sahnenin hiçbirinde değil.**

**Hüküm 🅑 ×6.** Yazım kuralı: negatif çekirdek
`Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.`
satırını **eldivenin bir şeye dokunduğu HER sahnede** taşır — çekirdek seçmeli değildir.

⭐ KRONOS'ta aynı sınıf 2 bulgu yazdı (S02 · S13). **İki filmde tekrar → ders eşiği geçildi.**

### 🅑-2 · MALZEME SERTLİĞİ SAYIYA ÇEVRİLMEMİŞ · 2 🔴 · 4 🟠

| S | bulgu |
|:--:|---|
| S05 🔴 | Pressurized greenhouse acts like soft dough or snow when the patch is pressed |
| S06 | Deflated greenhouse collapses like a soft bedsheet |
| S07 | Greenhouse instantly deflated and crushed, behaving like a thin bedsheet |
| S08 🔴 | Greenhouse collapses flat in S7, interior perfectly arched and rigid in S9 |
| S12 | Hull yields like soft dough externally, rigid internally |
| S19 | Metal bar bends flexibly like rubber |

**Promptta ne yazıyordu:** sera zarfı her sahnede **sıfatla** tarif edilmiş
(`pressurized`, `taut`, `stiff sheet`). Hiçbir promptta malzemenin ne kadar
çöktüğü **sayıyla** yok. Aynı yüzey bir sahnede hamur, diğerinde çelik oldu —
motor sıfatı her sahnede yeniden yorumladı.

**Hüküm 🅑 ×6.** Yazım kuralı: yük alan her yüzey sayısal çöküş taşır
(`the panel dents 2 cm and springs back; it never folds`).

### 🅑-3 · SES GÖRÜNTÜYLE EŞLENMEMİŞ · 1

S06 ③: *"massive pressurized structure collapsing; the sound effect is a light
fabric rustle lacking low-end weight"*. AUDIO satırı **var** ama ne çöktüğünü
değil ne duyulduğunu yazıyor; kütle ile ses arasında bağ kurulmamış.

**Hüküm 🅑 ×1.** Yazım kuralı: AUDIO satırı sesin **kaynağını ve kütlesini** adlandırır.

### 🅑-4 · EL/NESNE DEVAMLILIĞI · 3 · 🅑-5 · ÖLÇÜ · 1

S02 (fırça S2'de var, S3'te el boş) · S04 (sol elle uzanıyor, yakın planda sağ el) ·
S09 (bant rulosu var/yok): nesnenin **hangi elde** olduğu promptta yazılı değil.
S10 ⑥: dış yükseklik ~3 m, iç koridor ~4,5 m — ölçü gövde boyu cinsinden verilmemiş [D138].

---

## 🅒 BULGU DÜŞER · 2

S08 🔴 *"Visor persistence failure — helmet glass appears absent (perfectly clear
face), then abruptly catches heavy reflections"*: bu filmde vizör **berrak**
tasarlanmış ve yansımanın ışığa göre değişmesi fizikî olarak doğrudur. Mercek
tasarım kararını kusur saymış → ⑩ ÖNERME KAPISI. (Yansımanın **aynı sahne içinde**
aniden değişmesi ayrı bir konudur; rapor onu ayırmıyor.)

---

## 🎯 BU FİLMİN ÜÇ SATIRI

```
1. YAZIM İYİ, KUSUR BAŞKA YERDE. 🅑 oranı %43 — deponun en iyi yazılmış
   filmlerinden biri. AUDIO 25/25, "Exactly one human" 28, "0% bloom" hepsinde.
2. TEMAS SINIRI TEK GERÇEK BOŞLUK. Beş 🔴'nın beşi el-yüzey temasında ve
   beş sahnenin hiçbirinde temas cümlesi yok. Tek satır, beş BLOCKER.
3. DURUM MERDİVENİ METİNLE TUTMUYOR. PHASE 1-4 kusursuz yazılmış, altı bulgu
   yine de çıktı → bu kilit METİN DEĞİL REFERANS PANELİ ister [D168].
```
