# 🧩 SUSMAYAN_NOBETCI — prompt hata analizi

```
FORMAT      yatay 8 dk · 48 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   29/30 geçerli   ③ kimlik: 2/30 güçlü bayrak · raporlar B1 (24 sahne · 240 s)
BULGU       45 → tekil 44
HÜKÜM       🅐 34 · 🅑 5 · 🅒 4 · 🅓 1
OKUMA       🅑/(🅐+🅑) = %13 → deponun EN DÜŞÜK prompt hatası oranı
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 48/48: SES · parçacık · bloom · metin · g-ad · filigran · kamera
  KISMİ: dış-ses 23/48 · sayı 34/48 · temas 35/48 · giysi 35/48 · efor 32/48
  ⛔ HİÇ YOK: g-sayı
  bulgulu sahnelerde eksik: dış-ses 10/20 · sayı 16/20 · temas 16/20 · giysi 16/20 · efor 14/20 · g-sayı 0/20
```

> ⚠️ **BÖLÜM OFSETİ DÜZELTMESİ · 19.09.2026** — bu filmin QA'sı BÖLÜM
> birimiyle koşuldu ve ikinci yarımın masterı 0:00'dan başlıyor. İlk eşlemede
> o bulgular birinci yarının sahnelerine yazılmıştı; betiğe ofset eklendi ve
> **17 bulgunun sahne numarası değişti**. Sınıflar, sayılar ve hükümler AYNI;
> aşağıdaki prose ikinci-yarım bulgularında **düzeltme öncesi** numaraları
> taşıyabilir. ⛔ Kesin sahne numarası için [`../01_BULGU_DEFTERI.md`](../01_BULGU_DEFTERI.md)
> (makine yazar, ofsetli) hakemdir.

> ⭐ **Bu dosya üst sınırdır.** Depodaki en yeni yazım standardıyla yazılmış film:
> 96/96 promptta `0% bloom` · 96/96'da momentum cümlesi · 74'ünde temas sınırı ·
> 68'inde `Exactly one human character, no duplicates, no second person` ·
> **96/96'da `AUDIO:` satırı ve çoğunda açıkça `no exterior sound`.**
> Buna rağmen 44 bulgu çıktı. **Bu dosyanın söylediği şey şu: prompt yazımının
> tavanı buraya kadar; kalanı motorun sınırıdır.**

---

## 🅐 MODEL SAPMASI · 34

### 🅐-1 · VAKUMDA SES — kilit ne kadar açık yazılırsa yazılsın tutmuyor · 4 🔴

| S | bulgu | promptun AUDIO satırı |
|:--:|---|---|
| S00 🔴 | Airborne thruster audio present in hard vacuum exterior space shot | `no exterior sound at all, the hull parts in silence` |
| S07 🔴 | Thruster combustion roar audible in vacuum | `faint radio carrier hiss, one short burst of radio static …, no exterior sound` |
| S15 🔴 | Engine blast explosion produces full acoustic shockwave audio in space | `no exterior sound at all, the pod separates in silence` |
| S21 🔴 | Loud atmospheric explosion audio playing in vacuum shot | `a low cabin hum, a hard knock through the hull, then only the hum and her breathing` |

Bundan daha net yazılamaz. Kilit **pozitif** (ne duyulacağı yazılı), **negatif**
(dışarıdan ses yok) ve **fiziksel** (gövdeden iletilen ses adlandırılmış).
Motor dördünde de Hollywood sesini bastı.

**Hüküm 🅐 ×4.** ⭐ KRONOS'ta aynı sınıf 4 🔴 yazdı ve orada AUDIO satırı **hiç
yoktu**. İki film yan yana konunca sonuç şu:

```
AUDIO satırı YOK  → 4 🔴 (KRONOS)
AUDIO satırı TAM  → 4 🔴 (SUSMAYAN)
```

**Vakumda ses PROMPTLA ÇÖZÜLMÜYOR.** Bu bir yazım kuralı değil, bir **kurgu
kapısı**: master ihraç edildikten sonra dış ses kanalı ölçülür ve gerekiyorsa
susturulur. Ders siparişi bu — prompt cilası değil.

### 🅐-2 · PARÇACIK VE AÇISAL MOMENTUM · 6

S00 (2D düzlem enkaz) · S07 (kâğıt bant momentumu aniden duruyor) · S11 (gövde
plakası açısal momentumsuz) · S15 (kıvılcım kütlesiz · donan sıvı boncuk dizisi) ·
S18 (buz kristalleri düz 2D düzlem) · S21 (enkaz vakumda yavaşlıyor, a ≈ −1,2 m/s²)

**Promptta ne yazıyordu** — 96 promptun 96'sında:

> `Particles obey the stated gravity with continuous momentum, never hovering,
> never swirling like liquid, no melting or warping.`

**Hüküm 🅐 ×6** — ama bir boşlukla: cümle **doğrusal** momentumu söylüyor,
**açısal** momentumu (dönme) söylemiyor. S11 ve S15 tam oraya düştü.
→ Bu 🅐'nın içinde küçük bir 🅑 var: `and each fragment keeps its own slow spin`.

### 🅐-3 · BLOOM · 3 · 🅐-4 · DOKU YÜZMESİ VE ÖLÇEK · 5 · 🅐-5 · KİMLİK/GİYSİ · 3

`0% bloom, no glow, no soft focus, every surface keeps visible texture`
96/96'da yazılı; S01 · S03 · S19 bloom bulguları yine çıktı.
S09 · S16 · S20 doku yüzmesi, S10 🔴 (beyaz basınç giysisi koyu taktik giysiye
dönüyor) — giysi cümlesi ve `no drift` yazılı olduğu hâlde.

### 🅐-6 · EFOR · 9 · ⭐ en kalabalık grup

⑧ EFOR dokuz bulgu yazdı: S01 🔴 · S05 · S06 🔴 · S12 🔴 · S14 🔴 · S17 🔴 …
hepsi aynı kalıpta — *"ağır kolu çekiyor ama önkol gerginliği / omuz yuvarlanması /
oran düşüşü yok"*.

**Promptta ne yazıyordu:** bu filmde efor cümleleri VAR (`prompt_kontrol.py` ⑳
kapısı yeni rejimde koşuyor ve bu klasör 0 BLOCK verdi). Yani kilit yazıldı ve
kapıdan geçti; ekranda tutmadı.

**Hüküm 🅐 ×9.** ⭐ Bu, ⑳ kapısının **ölçülmüş sınırıdır**: kapı cümlenin VARLIĞINI
sayıyor, ŞİDDETİNİ değil. `his forearm tightens` yazmak yetiyor; ekranda bir şey
değişmiyor. Kapı önerisi `04_`'e: efor cümlesi **sayı** taşımalı
(`the lever moves 4 cm in the first second and 1 cm in the last`).

---

## 🅑 PROMPT BOŞLUĞU · 5

| # | S | bulgu | eksik cümle |
|:--:|:--:|---|---|
| 🅑-1 | S11 · S15 | Enkaz/plaka **açısal** momentum taşımıyor | momentum cümlesi dönmeyi kapsamıyor |
| 🅑-2 | S19 | Lomboz içindeki asılı lambalar 1G sarkaç gibi salınıyor | kadrajın **arka planındaki** nesneler için yerçekimi cümlesi yok — kural özneye yazılmış, dünyaya değil |
| 🅑-3 | S16 · S11 | Yırtık kenarları geniş ve yakın planlar arasında değişiyor | hasarın **biçimi** sayıyla kilitli değil (kaç cm, kaç parça) |
| 🅑-4 | S10 | Kokpit konsol yerleşimi gri metalden koyu döşemeye dönüyor | mekân devamlılığı taşıyıcısı yok — konsol her sahnede yeniden tarif ediliyor |
| 🅑-5 | S17 | Eldiven parmakları levye sapına giriyor | **S17'nin negatifinde temas sınırı cümlesi yok** (filmin 74 promptunda var, bu sahnede yok) |

⭐ 🅑-5 üçüncü filmde de aynı yerden çıktı: **çekirdek seçmeli uygulanıyor.**
KRONOS'ta 2, FROST_LINE'da 6, burada 1 bulgu — üç filmde tekrar.

---

## 🅒 BULGU DÜŞER · 4

| S | bulgu | neden düşer |
|:--:|---|---|
| S06 🔴 | *Airborne metallic collision SFX in vacuum during module separation* | Promptun AUDIO'su **gövdeden iletilen** sesi bilerek yazıyor: `two soft taps through the glove, a short muffled hiss through the hull`. Basınçlı kabuk üzerinden iletilen ses vakumda DOĞRUDUR. |
| S20 🔴 | *Heavy metallic latch impact sound propagating through vacuum* | Aynı: `through the hull, one hard knock as the line takes the load`. |
| S19 | *Unmotivated atmospheric haze halo around exterior portholes* | Lomboz camının iç yüzeyindeki buğu tasarım kararıdır. |
| S22 🔴 | *Female voice speaks line; identical phrase repeated by unassigned male voice* | Bu filmde promptlar **0 replik** üretiyor (post-dub); ekrandaki ses kurgu masasının işidir, promptun değil. |

⛔ İkisi de **⑩ ÖNERME KAPISI**'ndan geçirildi: düşen bulgunun puanı geri verilir.
S06/S20 tartışmaya açıktır — mercek "airborne" diyor ve videodan hava yolu ile
gövde yolu sesini ayırmak zordur. Karşı kanıt: promptun cümlesi net.

---

## 🎯 BU FİLMİN ÜÇ SATIRI

```
1. PROMPT YAZIMININ TAVANI. 🅑 oranı %13 — deponun en düşüğü. Bu filmde
   düzeltilecek prompt neredeyse kalmadı; kalan 5 boşluğun 3'ü tek cümlelik.
2. VAKUMDA SES PROMPTLA ÇÖZÜLMÜYOR. AUDIO satırı yokken 4 🔴, varken yine 4 🔴.
   Bu bir KURGU kapısıdır: master ihracından sonra dış ses kanalı ölçülür.
3. ⑳ EFOR KAPISI CÜMLEYİ SAYIYOR, ŞİDDETİ ÖLÇMÜYOR. Kapı 0 BLOCK verdi,
   ⑧ EFOR dokuz bulgu yazdı. Efor cümlesi SAYI istemeli.
```
