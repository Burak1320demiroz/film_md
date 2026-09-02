# 🎵 YERÇEKİMİ — MÜZİK: BEŞ ALTERNATİF

## 960 saniye · 120 sahne × 8 s · yatay 10-20 dk
### Kaynak kılavuz: `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 (üretim akışı yalnız bu bölümü kullanır)
### Filmin ses beyanları: on faz dosyasının `□ Ses:` satırları + KİLİT 30 · 38 · 45

> ⛔ **BU DOSYA BİR KARAR DOSYASIDIR, TESLİM DOSYASI DEĞİL.**
> Beşinden biri seçilince `MUZIK_VE_SES.md` yazılır: seçilen yay +
> 960 saniyelik spotting cetveli + aşağıdaki 5 teknik maddenin kapanışı.
> Sayı iki yerde durmaz [kural ①] — bu dosya alternatifleri, o dosya
> KİLİTLENMİŞ olanı taşır.

---

# 0. 🔍 TARAMA — müzik yazılmadan önce ne bulundu

## ⭐ BULGU 1 — FİLMİN MÜZİĞİ TAM ORTASINDA ÖLÜYOR

On faz dosyasının ses defterlerini üst üste koyduğumda ortaya
kimsenin tek bir yerde yazmadığı bir yapı çıktı:

```
SAHNE      SÜRE           MÜZİK      KAYNAK
S1         0:00-0:08      ⛔ YOK     F1 sahne kartı ("müzik YOK")
S2-S60     0:08-8:00      ⚠️ TANIMSIZ  ← hiçbir faz dosyası söylemiyor
S61-S72    8:00-9:36      ⛔ 0/12    F6 ses defteri
S73-S84    9:36-11:12     ⛔ 0/12    F7 ("MÜZİK 0/12", §5.3 yuvası)
S85-S96    11:12-12:48    ⛔ 0/12    F8 ses defteri
S97-S108   12:48-14:24    ✅ GERİ    F9 ("nabız, perküsyonsuz", tepe S104-106)
S109-S119  14:24-15:52    ✅ sürer   F10 (S118 = filmin TEK kreşendosu)
S120       15:52-16:00    ⛔ 0       F10 ("yalnız rüzgâr")

⭐ MÜZİKSİZ KUŞAK: S61 → S96 = 36 ARDIŞIK SAHNE = 4 DAKİKA 48 SANİYE
   ve başlangıcı S61 = 8:00 = filmin TAM ORTA NOKTASI.
```

Kılavuz `§10` her filmde **en az bir** müziksiz sahne istiyor. Bu filmde
36 tane var ve tam yarısında başlıyor. Bu bir eksiklik değil, **filmin
en büyük müzikal kararı** — ve beş alternatifin beşi de bunu miras alır.

```
⚠️ İKİ DÜZELTME, AYNI TARAMADAN
① F9 şunu diyor: "F7'nin sessizliğinden sonra ilk müzik."
   Yanlış — sessizlik F6'da (S61) başlıyor, F7'de değil. Doğrusu:
   "S60'tan sonra ilk müzik." Kayıt bu dosyada düzeltildi; faz
   dosyasındaki cümle MUZIK_VE_SES yazılırken düzeltilecek.
② S2-S60 arası (58 sahne · 7 dakika 52 saniye) müzik durumu hiçbir
   faz dosyasında yazılı DEĞİL. Filmin müziğinin dörtte üçü burada
   ve bugüne kadar tanımsızdı. Beş alternatifin ayrıştığı yer de burası.
```

## ⭐ BULGU 2 — KILAVUZUN KENDİ TEMPO TABLOSU BU FİLM İÇİN HAZIR

```
BPM = 240 × (sahne başına ölçü) ÷ (sahne saniyesi)          [§14.2]

8 SANİYELİK SAHNELER:
   60 BPM  → 2 ölçü/sahne     ⭐ bu filmin doğal tempo tabanı
   90 BPM  → 3 ölçü/sahne
  120 BPM  → 4 ölçü/sahne
  150 BPM  → 5 ölçü/sahne

⛔ Bu dördünün DIŞINDA hiçbir tempo kullanılmaz. Emsal ceza kayıtlı:
   THE DEAD APPROACH 130 BPM → 5,42 ölçü (hizasız) ·
   THE REMEMBERING DUST 58 BPM → 2,42 ölçü (hizasız).
   Hizalı tempoda her sahne geçişi bir ölçü başına düşer ve müzik
   kurguyu "biliyormuş" gibi durur.

ÖLÇÜ SAYIMI (60 BPM · 4/4 · ölçü = 4 s):
  BLOK 1  S2 başı (0:08) → S60 içinde bırakılır (~7:56) = 468 s = 117 ölçü
  BLOK 2  S97 başı (12:48) → S119 sonu (15:52)         = 184 s = 46 ölçü
  TOPLAM MÜZİK ≈ 10:52 / 16:00 = %68   (alternatif ⑤ hariç)
```

## ⭐ BULGU 3 — REVERB KARARI FİLMİN YAPISINI TAŞIYABİLİR

`§16`: _"vakum filmlerinde reverb'in YOKLUĞU bir karardır — müzik 'kuru'
kalmalı."_ Bu filmin ilk 108 sahnesi vakumda/kapsülde, **son 12 sahnesi
Dünya'da** (kuru göl yatağı, F10).

```
⭐ ORTAK KARAR (beş alternatifte de aynı):
   Müzik S2-S119 boyunca TAMAMEN KURU üretilir — sıfır reverb, sıfır
   oda. S109'dan (14:24) itibaren, yalnız F10'da, müziğe ilk kez
   GERÇEK BİR MEKÂN girer: geniş, düz, açık ova yankısı.
   → Filmin tek reverb'i, karakterin ayak bastığı ilk gerçek zemindir.
   → İzleyici bunu "müzik değişti" diye duymaz; "hava geldi" diye duyar.
```

## ⭐ BULGU 4 — SUB-BASS ÇELİŞKİSİ HÂLÂ AÇIK VE BURADA KAPANIYOR

```
04_ARASTIRMA §TUR 2 ② — açık bırakılmış madde:
  "Gravity ses mimarisi sub-bass sismik ikameye yaslanır; tur 1 bulgusu
   150 Hz altının telefonda HİÇ duyulmadığını söylüyor. … Planın müzik
   dosyası yazılırken karara bağlanır."

KAYNAK ÇELİŞKİSİ (kılavuz §15.1 kendi kaydını tutuyor):
  eski metin  ~300-400 Hz altı telefonda yok
  27.08 arşt.  150 Hz altı telefonda yok
  → İki kattan fazla fark, ikisi de ölçülmemiş dış kaynak.

✅ KARAR — SIKI TARAF SEÇİLDİ, BEŞ ALTERNATİFTE DE ZORUNLU:
   Müzik, 150 Hz altındaki HER ŞEYİN tamamen kaybolduğu varsayımıyla
   yazılır. Sub-bass VARDIR (kulaklıkta derinlik verir) ama duyguyu
   TEK BAŞINA hiçbir yerde taşımaz. Ağırlık, missing-fundamental
   yığınıyla (100 · 150 · 200 Hz) beynin içinde İNŞA EDİLİR [§15.1a].
   ⛔ Eşlikçi bir yedek DEĞİLDİR — kısık değil, TAŞIYICI seviyede.
   ⛔ İnfrasound (17-19 Hz) kullanılmaz [§15.2 — teslim edilemez].
```

---

# 1. 🔒 ORTAK KAP — beşi de bunun içine yazılır

Aşağıdakiler alternatif değildir; filmin kendi dosyalarında zaten kilitli
oldukları için **beş öneriye de aynen uygulanır.**

```
① MÜZİK TEK PARÇADIR, SAHNE SAHNE ÜRETİLMEZ [§14.1]
   İki blok, iki üretim: BLOK 1 (S2-S60) ve BLOK 2 (S97-S119).
   Aynı malzemeden, aynı seed ailesinden.

② TEMPO 60 / 90 / 120 / 150 BPM'den biri [§14.2] — başka sayı yok.

③ MÜZİKSİZ KUŞAK S61-S96 (4:48) DOKUNULMAZ.
   Müzik S60'ın İÇİNDE bırakılır: son nota S60 biterken değil,
   bitmeden EN AZ 2 saniye önce sönmüş olur [§10 — sessizliğin
   farkına varılması 1-2 saniye alır]. Kesme ile bitmez, bırakılır.

④ GERİ DÖNÜŞ S97'DE TEK NOTAYLA OLUR [§10] — patlamayla değil.
   F9 zaten şart koşuyor: "nabız, PERKÜSYONSUZ".

⑤ TEK KREŞENDO S118 (15:36) — filmin ayağa kalkışı.
   ⛔ Filmde başka kreşendo yoktur. Doruk (S94-96) müziksizdir;
      bu bilinçlidir ve S84'te verilen kararın faturasıdır.

⑥ S120 MÜZİKSİZ (15:52-16:00) — yalnız rüzgâr. Müzik S119'un
   sonunda biter. ⛔ Fade-out yok: müzik biter, film sürer.

⑦ FREKANS TABANI — her prompta birebir eklenir [§15.1 + §15.1a]:
   "The sub-bass is doubled by a companion tone one or two octaves
   higher, around 90-160 Hz, so the weight survives on small speakers.
   Reinforce the low end with a dense harmonic stack at roughly 100 Hz,
   150 Hz and 200 Hz so the missing fundamental is implied rather than
   played; the perceived weight must survive full loss of everything
   below 150 Hz."

⑧ REVERB: S2-S108 tamamen KURU · S109-S119 geniş açık ova [Bulgu 3].

⑨ MİKS HEDEFLERİ [§16]
   nihai -14 LUFS integrated · true peak ≤ -1 dBTP
   müzik yatağı (repliksiz) -16 … -18 LUFS
   MACHINE anonsu altında müzik ek -6 … -9 dB
   ⛔ mono fold-down kontrolü zorunlu — hacim kaybı varsa miks yanlış.

⑩ MICKEY-MOUSING YASAK [§13] — uzun filmde istisnası yok.
   Kalem düşerken nota düşmez; halat kopmadan trampet vurmaz.
```

## 🔊 MÜZİK DEĞİL AMA BU DOSYANIN İŞİ — dört ses maddesi

```
A) B'NİN HALÜSİNASYON SESİ (S76 · S78 · S81) — dosyanın EN TEKNİK maddesi
   [F7 KİLİT 30 ①] ses hoparlörden GELMEZ: her yönden gelir, bant
   filtresi YOKTUR, oda akustiği YOKTUR. Canlı telsiz (S66 çoban)
   bandın içindeydi ve uzaktı; bu ses YAKIN ve FİLTRESİZDİR.
   ⛔ MİKS KURALI: telsiz EQ'su (300 Hz-3 kHz bant) uygulanmaz,
      pan merkezde ama korelasyonsuz (her iki kanalda aynı anda,
      yönsüz), oda kuyruğu 0. Kabin tonundan DAHA YAKIN durur.
   ⛔ Duraklama bırakmaz — bırakırsa izleyici konuşma sanar.

B) S94 DİEGETİK SESSİZLİK BIÇAĞI [F8 KİLİT 38]
   Olayın KENDİ sesi 0 (vakum + insansız). ⛔ Ama dijital sıfır YOK
   [D83]: S93'ten S95'e uzanan çok düşük kabin tonu KESİLMEDEN altta
   sürer. Ses köprüsü ölçülür: S93 → S94 → S95 tek dalga, kesme 0.
   ÖLÇÜM NOKTASI FİLMİN EN DÜŞÜK SEVİYESİ DEĞİLDİR — o S68'dir.

C) S68 = FİLMİN EN DÜŞÜK SES SEVİYESİ [F6]. Bütün seviye ölçeği bu
   sahneden kalibre edilir; S94 buradan yukarıda durur.

D) S117 SAAT TIKI [F10 · Çehov 2]
   Saniye ibresi 8 saniyede EN AZ BEŞ sayılabilir adım atar — filmin
   TEK mekanik ritmi. ⛔ Tık müziğin temposuna KİLİTLENMEZ (bu
   Mickey-Mousing olurdu) — alternatif ④ hariç, ve orada gerekçesi
   yazılı bir yapı kararıdır.
```

---

# 2. 🎼 BEŞ ALTERNATİF — bir bakışta

| | Ad | Temel fikir | BPM | Çözülme | Risk |
|:--:|---|---|:--:|:--:|---|
| ① | **KAYITSIZ NABIZ** | Müzik olaya hiç tepki vermez | 60 | 0 | monotonluk |
| ② | **DÜŞEN HAT** | Müzik filmin fiziğidir: hiçbir şey düşmez → her şey düşer | 60→90 | 1 (S118) | fazla açık |
| ③ | **İKİ SES** | İki enstrüman = iki insan; biri S43'te susar | 60 | 1 (S117) | duygusal risk |
| ④ | **DOKSAN DAKİKA** | Müzik sayılamayan bir geri sayımdır | 90 | 1 (S117) | Mickey-Mousing sınırı |
| ⑤ | **ÖNCE SESSİZLİK** | Neredeyse hiç müzik yok — 16 dakikada ~4 | 60 | 1 (S118) | seyirci kaybı |

> ⚠️ Beşi de kılavuzun `§18 karar tablosunu` geçer. Aralarındaki fark
> "hangisi doğru" değil, **filmin hangi cümlesini müziğe verdiğin**.

---

# 🅰️ ALTERNATİF ① — "KAYITSIZ NABIZ" (The Indifferent Pulse)

> ⭐ **Kılavuzun açıkça istediği ve bu depoda HİÇ KULLANILMAMIŞ araç.**
> `§9`: _"Anempatik müzik … evrenin insan acısına duyarsızlığını
> vurgulayarak etkiyi büyütür. … Bizim anempatik hâlimiz: DEĞİŞMEYEN
> müzik. Olay büyürken müziğin tepki vermemesi."_

### 📋 KÜNYE [§17]

```
FİLM:                 YERÇEKİMİ · 16:00 · 120 × 8 s
NOVUM OKUMASI:        "İzleyici bu görüntüyü BİR KAZA olarak değil,
                       EVRENİN NORMAL İŞLEYİŞİ olarak okumalı."
MÜZİK-GÖRÜNTÜ:        ANEMPATİK (kayıtsız)
TEMPO:                60 BPM → 2 ölçü/sahne
TONALİTE:             Re minör, modal — çözülmez, hiç
SESSİZLİK KUŞAĞI:     S61-S96 (müzik S60 bitmeden ≥2 s önce bırakılır)
ÇÖZÜLMEYEN CÜMLE:     TÜMÜ. Bu alternatifte hiçbir cümle çözülmez.
KAPANIŞ:              S119'da figür ORTASINDA bırakılır → S120 rüzgâr
FREKANS TABANI:       sub 45 Hz + eşlikçi 90/135 Hz + yığın 100/150/200
KATMANLAR:            4 — nabız (viyolonsel pizz.) · alt drone ·
                      sürtme yaylı · tek ahşap nefesli (yalnız F9-F10)
LUFS:                 -14 nihai / -17 yatak
REVERB:               S2-S108 kuru · S109-S119 açık ova
```

### 🎯 FİKİR

Altı notalı tek bir figür. **S2'de başlar ve S60'a kadar hiç değişmez.**
S16'da enkaz dalgası gelir — figür değişmez. S30'da yara — değişmez.
**S43'te B kendini feda eder — figür değişmez.** Aynı hız, aynı ses,
aynı altı nota.

S97'de müzik geri geldiğinde **aynı figürdür** — 4 dakika 48 saniye
boyunca bir yerlerde çalmaya devam etmiş gibi. Hiçbir şey olmamış gibi.

```
⭐ FİLMİN CÜMLESİ MÜZİĞE ŞÖYLE GİRER:
   S120'de gökteki çizgiler hâlâ akıyor ve o onlara bakmıyor —
   "kurtulan kişi kurtulmuş bir dünyaya dönmedi."
   Kayıtsız nabız bu cümleyi 16 dakika boyunca ÖNCEDEN söyler.
   S43'te ağlamayan müzik, S120'de haklı çıkar.
```

### 🎹 ÜRETİM PROMPTU — BLOK 1 (S2-S60 · 468 s · 117 ölçü)

```
A single continuous instrumental cue for a science-fiction film,
7 minutes 48 seconds long, 60 BPM, 4/4, D minor, modal and unresolved.

CORE FIGURE: one six-note cello pizzicato figure, two bars long, low
register, repeating without variation for the entire duration. The
figure NEVER changes: same notes, same dynamic, same tempo from the
first bar to the last. No swell, no build, no drop, no fill, no
percussion of any kind. It does not react to anything.

LAYERS UNDER IT: one sustained low drone; one bowed string texture
holding a single open fifth that never moves; nothing else. Do not add
instruments over time. Do not develop the material.

TONALITY: the figure implies a cadence and never delivers one. No
resolution anywhere in the piece — the phrase does not resolve, the
suspended fifth never closes.

FREQUENCY: the sub-bass is doubled by a companion tone one or two
octaves higher, around 90-160 Hz, so the weight survives on small
speakers. Reinforce the low end with a dense harmonic stack at roughly
100 Hz, 150 Hz and 200 Hz so the missing fundamental is implied rather
than played; the perceived weight must survive full loss of everything
below 150 Hz.

SPACE: completely dry. No reverb, no room, no echo, no delay, no wide
stereo effects — the piece must lose nothing when folded to mono.

ENDING: the figure stops in the middle of its own phrase and is released
rather than cut. No fade-out, no final chord, no ritardando.

[Instrumental] [No Vocals] [No Percussion] [Sustained]
```

### 🎹 ÜRETİM PROMPTU — BLOK 2 (S97-S119 · 184 s · 46 ölçü)

```
A continuous instrumental cue, 3 minutes 4 seconds, 60 BPM, 4/4, D
minor. THE SAME six-note cello pizzicato figure as before, identical
tempo and identical dynamic — it returns as if it had been playing all
along and no time had passed.

ENTRY: begin with ONE single note alone, then the figure from the second
bar. No swell, no crescendo on entry, no percussion.

FOR THE FIRST 2 MINUTES the figure again does not change. One low
woodwind enters quietly, holding long tones, but the figure ignores it.

AT 2 MINUTES 48 SECONDS INTO THIS CUE, and only there, the piece finally
lifts: a single controlled crescendo over 8 seconds, strings rising a
minor third above the figure, reaching its peak and stopping. This is
the ONLY crescendo in the entire film. The figure itself still does not
change underneath it.

AFTER THE CRESCENDO: 8 seconds, the figure alone again, then it stops in
the middle of its phrase. No final chord, no fade-out.

SPACE: the first 96 seconds completely dry. From 1 minute 36 seconds
onward a wide, flat, open outdoor reverb enters gradually — as if the
music had walked out of a sealed room into a desert. This is the only
reverb in the film.

FREQUENCY: the sub-bass is doubled by a companion tone one or two
octaves higher, around 90-160 Hz. Reinforce the low end with a dense
harmonic stack at roughly 100 Hz, 150 Hz and 200 Hz; the perceived
weight must survive full loss of everything below 150 Hz.

[Instrumental] [No Vocals] [No Percussion]
```

### 🚪 KABUL / RET — ①

```
KABUL ① S43'e (feda) müzik HİÇBİR tepki vermiyor — kör dinlemede
        o saniyede bir şey olduğu ANLAŞILMIYOR.
      ② Figür 7:48 boyunca ölçülebilir biçimde aynı: tempo sapması
        yok, dinamik sapması yok, enstrüman eklenmiyor.
      ③ S97 girişi tek nota, kreşendosuz.
      ④ Mono fold-down'da hacim kaybı yok.
RET   ① Herhangi bir yerde bir yükseliş/dolgu/trampet varsa.
      ② Figür çözüldüyse (kadans geldiyse) — fikir ölür.
      ③ S118 dışında bir kreşendo varsa.
YABANCI GÖZ  Filmi görmemiş birine yalnız müziği 3 dakika dinlet,
      sor: "Bu parçada bir şey oluyor mu?" → "Hayır" demeli.
      "Evet, bir yerde gerginleşiyor" derse anempati düşmüştür.
SONUÇ ☐ SEÇİLDİ   ☐ ELENDİ      seed: __________
```

---

# 🅱️ ALTERNATİF ② — "DÜŞEN HAT" (The Falling Line)

> Filmin adı YERÇEKİMİ. Bu alternatifte müzik **yerçekiminin kendisidir**:
> yörüngede hiçbir nota düşmez, Dünya'da her nota düşer.

### 📋 KÜNYE [§17]

```
FİLM:                 YERÇEKİMİ · 16:00 · 120 × 8 s
NOVUM OKUMASI:        "İzleyici bu görüntüyü AĞIRLIĞIN YOKLUĞU olarak
                       okumalı — ve ağırlık geri geldiğinde bunu
                       görmeden önce DUYMALI."
MÜZİK-GÖRÜNTÜ:        EMPATİK ama fizikle — duyguyla değil
TEMPO:                BLOK 1 = 60 BPM (2 ölçü) · BLOK 2 = 90 BPM (3 ölçü)
TONALİTE:             La minör; tek çözülme S118'de, YÜKSELEREK
SESSİZLİK KUŞAĞI:     S61-S96
ÇÖZÜLMEYEN CÜMLE:     Bütün blok 1 askıda — 118 sahne boyunca inen
                      hiçbir hat dibe varmaz
KAPANIŞ:              S118'de tek yükselen kadans → S119 iniş → S120 rüzgâr
FREKANS TABANI:       sub 42 Hz + eşlikçi 84/126 Hz + yığın 100/150/200
KATMANLAR:            5 — süzülen pad · yüksek yaylı · alt drone ·
                      düşen figür (yalnız F9-F10) · nabız (yalnız BLOK 2)
LUFS:                 -14 nihai / -17 yatak
REVERB:               S2-S108 kuru · S109-S119 açık ova
```

### 🎯 FİKİR — üç evre

```
EVRE 1 · S2-S60  ⟶  HİÇBİR ŞEY DÜŞMEZ
  Sürekli tutulan notalar. Melodi yok, çünkü melodi inip çıkar.
  Her hat ya sabit kalır ya YUKARI gider. Bir nota bile aşağı inmez.
  ⛔ 468 saniye boyunca inen tek bir aralık YOKTUR — bu ölçülebilir
     ve kabul kapısıdır.

EVRE 2 · S61-S96  ⟶  SESSİZLİK (ortak kap)
  Ağırlık yok, müzik de yok. En dürüst 4:48.

EVRE 3 · S97-S119  ⟶  HER ŞEY DÜŞER
  S97'de tek nota geri gelir ve o nota AŞAĞI iner — filmin
  ilk düşen sesi, ve görüntüde henüz hiçbir şey düşmemiştir.
  S102'de (yerçekimi yağmuru · imza çekim) bütün doku birden iner:
  beş katman aynı anda, farklı hızlarda.
  ⭐ Kalem 0,5 saniyede düşer, kumaş 1 saniyede, toz perde gibi —
     müzik AYNI ORANLARLA iner ama notaya değil, dokuya bağlanır.
     ⛔ Bu Mickey-Mousing DEĞİLDİR: tek bir olaya tek bir vuruş
        konmuyor; bütün doku bir FİZİK KURALINI paylaşıyor.
  S118'de ilk ve tek kez bir hat YUKARI çıkar ve ÇÖZÜLÜR.
```

### 🎹 ÜRETİM PROMPTU — BLOK 1 (S2-S60 · 468 s)

```
A single continuous instrumental cue for a science-fiction film,
7 minutes 48 seconds long, 60 BPM, 4/4, A minor, weightless and
suspended.

THE ONE RULE: nothing in this piece ever descends in pitch. Every line
either holds absolutely still or rises. There is not a single falling
interval, no downward glissando, no descending bass movement anywhere in
seven minutes and forty-eight seconds. Lines drift upward and simply
stop; they never come back down.

TEXTURE: very slow synth pads with no attack, entering and leaving
without articulation; one high sustained string layer sitting far above
the bass with a wide empty gap in the middle of the spectrum; one low
drone that holds one pitch for the entire piece. No melody, no theme, no
percussion, no rhythmic articulation of any kind — nothing that could be
counted.

TONALITY: suspended chords, no cadence, the phrase does not resolve.
Tension accumulates and is never released.

FREQUENCY: the sub-bass is doubled by a companion tone one or two
octaves higher, around 90-160 Hz, so the weight survives on small
speakers. Reinforce the low end with a dense harmonic stack at roughly
100 Hz, 150 Hz and 200 Hz so the missing fundamental is implied rather
than played; the perceived weight must survive full loss of everything
below 150 Hz.

SPACE: completely dry. No reverb, no room, no echo — a vacuum has no
reverberation. Must lose nothing folded to mono.

ENDING: the highest line drifts up, thins out and is released mid-phrase.
No fade-out, no final chord.

[Instrumental] [No Vocals] [No Percussion] [Sustained]
```

### 🎹 ÜRETİM PROMPTU — BLOK 2 (S97-S119 · 184 s)

```
A continuous instrumental cue, 3 minutes 4 seconds, 90 BPM, 4/4, A
minor. This cue is the mirror of the previous one: here everything falls.

ENTRY: begin with ONE single sustained note alone, and let that note
slowly bend downward a whole tone over 8 seconds — the first descending
sound in the film. No crescendo, no percussion.

BUILD: a low pulse enters, felt rather than struck, with no drum kit and
no percussion instruments. Descending lines begin to appear, sparse at
first.

AT 40 SECONDS INTO THIS CUE the whole texture descends at once: five
layers falling together at different speeds, the fastest crossing an
octave in half a second, the slowest taking four seconds, a fine high
shimmer of particles settling slowest of all. They do not land on a beat
and they do not hit anything — the descent is a property of the whole
sound, not an effect on one event.

AT 56 SECONDS the texture reaches its densest point and the low pulse is
at its fullest, and it holds that density for 24 seconds. It does not
resolve.

AT 2 MINUTES 48 SECONDS, and only there: one single controlled crescendo
over 8 seconds in which a line rises for the first and only time in the
whole film, and RESOLVES — a full cadence, the only one. This is the only
crescendo in the film.

AFTER IT: 8 seconds, one held note descending gently, then stop. No
fade-out.

SPACE: the first 96 seconds completely dry. From 1 minute 36 seconds a
wide, flat, open outdoor reverb enters gradually — the only reverb in the
film.

FREQUENCY: the sub-bass is doubled by a companion tone one or two octaves
higher, around 90-160 Hz. Reinforce the low end with a dense harmonic
stack at roughly 100 Hz, 150 Hz and 200 Hz; the perceived weight must
survive full loss of everything below 150 Hz.

[Instrumental] [No Vocals] [No Drum Kit]
```

### 🚪 KABUL / RET — ②

```
KABUL ① BLOK 1'de inen tek bir aralık YOK — dinleyerek doğrulanır,
        şüphede kalınırsa piyano rulosuna dökülür ve sayılır.
      ② S97'nin ilk notası AŞAĞI iniyor ve görüntüde henüz hiçbir
        şey düşmemiş.
      ③ S102'de düşüş TEK bir olaya değil, bütün dokuya ait.
      ④ Filmin tek yükselen kadansı S118'de.
RET   ① BLOK 1'de bir melodi belirdiyse (melodi iner-çıkar → fikir ölür).
      ② S102'de tek bir "düşme" vuruşu varsa → Mickey-Mousing [§13].
      ③ Kadans S118'den önce geldiyse.
YABANCI GÖZ  Yalnız BLOK 1'i dinlet, sor: "Bu müzik nerede geçiyor?"
      → "Havada / boşlukta / yerçekimsiz" demeli.
SONUÇ ☐ SEÇİLDİ   ☐ ELENDİ      seed: __________
```

---

# 🅲 ALTERNATİF ③ — "İKİ SES" (Two Voices)

> `§11.2`'nin birebir uygulaması: _"Yükselen bir figürün doruğa varmadan
> kesilmesi = en ucuz gerilim. … THE REMEMBERING DUST S9/S12 bunu
> yapıyor — viyola yarım kalıyor, 10 saniye sonra tamamlanıyor.
> **Yapı = tema.**"_ Burada yarım kalan cümle 74 sahne bekler.

### 📋 KÜNYE [§17]

```
FİLM:                 YERÇEKİMİ · 16:00 · 120 × 8 s
NOVUM OKUMASI:        "İzleyici bu görüntüyü BİR KAYIP olarak okumalı —
                       ve kaybın yerini, o yer boş kaldığı için bilmeli."
MÜZİK-GÖRÜNTÜ:        EMPATİK, ama kişiye değil İLİŞKİYE
TEMPO:                60 BPM → 2 ölçü/sahne
TONALİTE:             Sol minör; tek çözülme S117'de
SESSİZLİK KUŞAĞI:     S61-S96
ÇÖZÜLMEYEN CÜMLE:     S43'te ikinci ses cümlenin ORTASINDA susar →
                      S117'de BİRİNCİ ses onun cümlesini tamamlar
KAPANIŞ:              S117 çözülme · S118 kreşendo · S119 tek ses · S120 rüzgâr
FREKANS TABANI:       sub 48 Hz + eşlikçi 96/144 Hz + yığın 100/150/200
KATMANLAR:            4 — viyolonsel (A) · bas klarnet (B) · alt drone ·
                      oda tonu köprüsü
LUFS:                 -14 nihai / -17 yatak
REVERB:               S2-S108 kuru · S109-S119 açık ova
```

### 🎯 FİKİR — bir düet, bir eksilme

```
S2-S42   İKİ SES. Viyolonsel (A) ve bas klarnet (B) sırayla konuşur:
         biri iki ölçülük bir cümle söyler, öteki cevap verir.
         39 replikli filmde müzik de bir DİYALOGDUR.

S43      ⭐ FEDA. Bas klarnet bir cümleye başlar ve ÜÇÜNCÜ NOTADA
         susar. Cümle bitmez. Kesme yok, azalma yok — yalnızca yok.

S44-S60  VİYOLONSEL YALNIZ. Ama her cümlesinden sonra hâlâ
         İKİ ÖLÇÜLÜK BOŞLUK bırakıyor — cevap gelecekmiş gibi.
         ⛔ Boşluk doldurulmaz. 17 sahne boyunca aynı boşluk.

S61-S96  SESSİZLİK. İki ses de yok.

S97-S116 VİYOLONSEL GERİ DÖNER — ve artık boşluk BIRAKMIYOR.
         Cümleler birbirine bağlanıyor. Beklemeyi bıraktı.

S117     ⭐⭐ SAAT KURULUR — VE VİYOLONSEL, BAS KLARNETİN
         S43'TE YARIM BIRAKTIĞI CÜMLEYİ TAMAMLAR.
         Filmin tek çözülmesi. Kendi cümlesi değil, ONUN cümlesi.
         ⛔ Enstrüman değişmez, taklit yok — aynı notalar, öteki ses.

S118     Kreşendo (ayağa kalkış).
S119     Tek ses, alçalarak.
S120     Rüzgâr.
```

```
⭐ NEDEN BU FİLME OTURUYOR:
   S117'nin sahne kartı diyor ki: "⛔ Jest açıklanmaz: kim için
   kurulduğu söylenmez." Müzik de açıklamaz — sadece onun cümlesini
   söyler. İzleyici kimin için olduğunu 74 sahne önce duyduğu için bilir.
```

### 🎹 ÜRETİM PROMPTU — BLOK 1 (S2-S60 · 468 s)

```
A single continuous instrumental cue for a science-fiction film,
7 minutes 48 seconds long, 60 BPM, 4/4, G minor, sparse and conversational.

TWO VOICES ONLY: a solo cello in its low register, and a bass clarinet.
They never play at the same time. One states a two-bar phrase, then rests
two bars while the other answers. This alternation continues, unhurried,
for the first five minutes and twenty-eight seconds. Under them, one very
quiet sustained drone; nothing else. No percussion, no pads, no strings
section.

AT 5 MINUTES 28 SECONDS INTO THIS CUE: the bass clarinet begins a phrase
and stops on its third note. The phrase is not finished. It is not faded
out and not cut off musically — it simply stops, and the bass clarinet
NEVER PLAYS AGAIN for the rest of this cue.

FROM THAT POINT ON: the cello plays alone. It keeps its old habit — after
every two-bar phrase it leaves exactly two bars of silence, as if waiting
for an answer that does not come. That empty space is never filled by any
other instrument. This continues for the last two minutes and twenty
seconds.

TONALITY: no cadence anywhere. The phrase does not resolve.

FREQUENCY: the sub-bass is doubled by a companion tone one or two octaves
higher, around 90-160 Hz, so the weight survives on small speakers.
Reinforce the low end with a dense harmonic stack at roughly 100 Hz,
150 Hz and 200 Hz so the missing fundamental is implied rather than
played; the perceived weight must survive full loss of everything below
150 Hz.

SPACE: completely dry. No reverb, no room, no echo. Mono-safe.

ENDING: the cello leaves one more two-bar gap and does not play into it.

[Instrumental] [No Vocals] [No Percussion]
```

### 🎹 ÜRETİM PROMPTU — BLOK 2 (S97-S119 · 184 s)

```
A continuous instrumental cue, 3 minutes 4 seconds, 60 BPM, 4/4, G minor.
Solo cello, low register, with one quiet sustained drone underneath. The
bass clarinet does not appear anywhere in this cue.

ENTRY: one single cello note alone, held. Then phrases — but this time
the cello no longer leaves gaps. Its phrases run into one another
continuously. It has stopped waiting.

AT 2 MINUTES 40 SECONDS INTO THIS CUE, the cello plays a phrase in a
register and shape clearly different from its own: a short, plain,
descending line that resolves fully onto the tonic. This is the only
resolution in the entire film, and it arrives once.

AT 2 MINUTES 48 SECONDS: a single controlled crescendo over 8 seconds,
the cello joined by a low string section rising underneath it, reaching
its peak and stopping. This is the only crescendo in the film.

AFTER IT: 8 seconds, cello alone, descending, then stop. No fade-out.

SPACE: the first 96 seconds completely dry. From 1 minute 36 seconds a
wide, flat, open outdoor reverb enters gradually — the only reverb in
the film.

FREQUENCY: the sub-bass is doubled by a companion tone one or two octaves
higher, around 90-160 Hz. Reinforce the low end with a dense harmonic
stack at roughly 100 Hz, 150 Hz and 200 Hz; the perceived weight must
survive full loss of everything below 150 Hz.

[Instrumental] [No Vocals] [No Percussion]
```

### 🚪 KABUL / RET — ③

```
KABUL ① İki ses BLOK 1'de hiç üst üste binmiyor (dinleyerek sayılır).
      ② Bas klarnetin son cümlesi S43'te ve YARIM.
      ③ S44-S60'ta viyolonselin bıraktığı boşluklar ÖLÇÜLEBİLİR
        biçimde iki ölçü ve HİÇBİRİ doldurulmamış.
      ④ S117'nin cümlesi S43'te yarım kalanla AYNI notalar.
RET   ① Bas klarnet S43'ten sonra bir kez bile duyuluyorsa.
      ② Boşluklar pad/reverb kuyruğu ile doldurulmuşsa — fikir ölür.
      ③ S117 çözülmesi bir kreşendoya bağlandıysa (S118'in işini çalar).
YABANCI GÖZ  BLOK 1'in son 2 dakikasını dinlet, sor: "Bu müzikte bir
      şey eksik mi?" → "Evet, sanki cevap gelmiyor" demeli.
SONUÇ ☐ SEÇİLDİ   ☐ ELENDİ      seed: __________
```

---

# 🅳 ALTERNATİF ④ — "DOKSAN DAKİKA" (Ninety Minutes)

> Çehov 5'in işitsel karşılığı. S22'de B "doksan dakika" der (enkaz
> yörüngeyi tamamlayıp geri gelecek); S94'te geri gelir. Bu alternatifte
> **müzik o doksan dakikadır** — izleyicinin sayamadığı bir geri sayım.

### 📋 KÜNYE [§17]

```
FİLM:                 YERÇEKİMİ · 16:00 · 120 × 8 s
NOVUM OKUMASI:        "İzleyici bu görüntüyü BİR SÜRE olarak okumalı:
                       kötü olan şey geri geliyor ve saati işliyor."
MÜZİK-GÖRÜNTÜ:        GERİLİM — beklenti mimarisi (ITPRA §11)
TEMPO:                90 BPM → 3 ölçü/sahne
TONALİTE:             Do minör, pedal üstünde; tek çözülme S117
SESSİZLİK KUŞAĞI:     S61-S96
ÇÖZÜLMEYEN CÜMLE:     Çevrim her turda bir nota EKSİK kapanır
KAPANIŞ:              S117'de çevrim ilk kez tam kapanır → S118 kreşendo
FREKANS TABANI:       sub 40 Hz + eşlikçi 80/120 Hz + yığın 100/150/200
KATMANLAR:            4 — pedal · çevrim figürü · yüksek gerilim yaylısı ·
                      metalik tıkırtı (perküsyon DEĞİL, doku)
LUFS:                 -14 nihai / -17 yatak
REVERB:               S2-S108 kuru · S109-S119 açık ova
```

### 🎯 FİKİR — sayılamayan çevrim

```
Müzik 17 ölçülük bir çevrim taşır. 17 asal sayıdır ve sahne 3 ölçüdür:
çevrim hiçbir zaman sahne başına denk gelmez.
  → İzleyici bir tekrar olduğunu HİSSEDER ama nereye oturduğunu
    ÇIKARAMAZ. Gerilimin kaynağı budur: sayamadığın bir saat.

⭐ Her turda çevrimin SON NOTASI eksiktir. 468 saniyede yaklaşık
   yedi tur döner ve yedisinde de kapanmaz [ITPRA §11.1].

S117'de — saat kurulurken — çevrim ilk kez TAM döner ve kapanır.
   ⭐ Filmin tek çözülmesi bir MELODİ değil, bir SAYININ tamamlanması.

⛔ MICKEY-MOUSING SINIRI — bu alternatifin tek riski ve tek istisnası:
   §13 uzun filmde Mickey-Mousing'i YASAKLAR. Burada tek bir yerde
   müzik ve görüntü aynı tempoya girer: S117, saniye ibresi
   8 saniyede beş adım atarken. Bu bir "vuruşa vuruş" değil, filmin
   TEK mekanik ritminin müziğin çevrimini KAPATMASIDIR — yapı kararı.
   ⚠️ Yine de bu, beş alternatif içinde kılavuza en yakın duran
      sınırdır. Seçilirse ödünç alınan istisna kayda geçer [D74].
```

### 🎹 ÜRETİM PROMPTU — BLOK 1 (S2-S60 · 468 s)

```
A single continuous instrumental cue for a science-fiction thriller,
7 minutes 48 seconds long, 90 BPM, 4/4, C minor, tense and patient.

STRUCTURE: the piece is built on a cycle exactly 17 bars long that
repeats for the whole duration. Because the cycle is 17 bars, it never
lines up the same way twice against anything — the listener can feel a
repetition without being able to locate it.

THE CYCLE: a low pedal note held throughout; over it a spare figure of
rising fourths on muted strings; a thin high sustained violin line far
above, holding tension. EVERY TIME THE CYCLE COMES ROUND, ITS FINAL NOTE
IS MISSING — the cycle restarts one note before it closes. It never
completes, not once in seven minutes and forty-eight seconds.

TEXTURE: no drum kit, no percussion instruments. A dry metallic ticking
texture sits quietly in the background but is deliberately NOT locked to
the tempo — it drifts against the beat and never coincides with it.

TONALITY: suspended over the pedal, no cadence, the phrase does not
resolve.

FREQUENCY: the sub-bass is doubled by a companion tone one or two octaves
higher, around 90-160 Hz, so the weight survives on small speakers.
Reinforce the low end with a dense harmonic stack at roughly 100 Hz,
150 Hz and 200 Hz so the missing fundamental is implied rather than
played; the perceived weight must survive full loss of everything below
150 Hz.

SPACE: completely dry. No reverb, no room, no echo. Mono-safe.

ENDING: the cycle stops partway through, one note before it would close.
No fade-out.

[Instrumental] [No Vocals] [No Drum Kit]
```

### 🎹 ÜRETİM PROMPTU — BLOK 2 (S97-S119 · 184 s)

```
A continuous instrumental cue, 3 minutes 4 seconds, 90 BPM, 4/4, C minor.
The same 17-bar cycle as before, the same missing final note.

ENTRY: one single low note alone, then the pedal, then the cycle from
the second bar. No crescendo on entry, no percussion.

BUILD: the high violin line thickens; the dry metallic ticking texture
grows slightly louder but still drifts against the beat and never
coincides with it. The cycle still does not close.

AT 2 MINUTES 40 SECONDS INTO THIS CUE, for the first and only time, the
cycle completes: the missing final note arrives and the 17 bars close.
At that same moment the ticking texture locks onto the tempo and, for
exactly eight seconds, ticks in time — five clear audible ticks. This is
the only place in the film where the ticking and the music agree.

AT 2 MINUTES 48 SECONDS: a single controlled crescendo over 8 seconds,
strings rising over the closed cycle, reaching its peak and stopping.
This is the only crescendo in the film.

AFTER IT: 8 seconds, the pedal alone, then stop. The ticking does not
return. No fade-out.

SPACE: the first 96 seconds completely dry. From 1 minute 36 seconds a
wide, flat, open outdoor reverb enters gradually — the only reverb in
the film.

FREQUENCY: the sub-bass is doubled by a companion tone one or two octaves
higher, around 90-160 Hz. Reinforce the low end with a dense harmonic
stack at roughly 100 Hz, 150 Hz and 200 Hz; the perceived weight must
survive full loss of everything below 150 Hz.

[Instrumental] [No Vocals] [No Drum Kit]
```

### 🚪 KABUL / RET — ④

```
KABUL ① Çevrim 17 ölçü ve BLOK 1'de bir kez bile kapanmıyor.
      ② Tıkırtı BLOK 1'in tamamında tempoya OTURMUYOR.
      ③ S117'de çevrim kapanıyor VE tıkırtı sekiz saniye boyunca
        tempoya kilitleniyor — beş sayılabilir tık.
      ④ S94 doruğunda müzik YOK (ortak kap ⑤) — gerilim müzikle
        değil, sessizlikle ödeniyor.
RET   ① Tıkırtı BLOK 1'de tempoya oturduysa — geri sayım sayılabilir
        hâle gelir, gerilim ölür.
      ② Çevrim kapandıysa (S117 dışında).
      ③ Trampet/davul girdiyse — bu bir aksiyon filmi değil.
YABANCI GÖZ  BLOK 1'i dinlet, sor: "Bu müzikte bir tekrar var mı,
      kaç saniyede bir?" → "Var ama sayamıyorum" demeli.
      Doğru sayıyı verirse çevrim çok basit demektir.
SONUÇ ☐ SEÇİLDİ   ☐ ELENDİ      seed: __________
```

---

# 🅴 ALTERNATİF ⑤ — "ÖNCE SESSİZLİK" (Silence First)

> `§10`'un birebir kaynağı: _"No Country for Old Men — Carter Burwell tüm
> film için sadece 12 dakikalık, neredeyse duyulmayan drone yazdı.
> Müziğin yokluğu … asıl araç oldu."_ Bu alternatif diğer dördünün
> yaptığını **yapmamayı** öneriyor.

### 📋 KÜNYE [§17]

```
FİLM:                 YERÇEKİMİ · 16:00 · 120 × 8 s
NOVUM OKUMASI:        "İzleyici bu görüntüyü BELGESEL olarak okumalı —
                       kimse ona ne hissedeceğini söylemiyor."
MÜZİK-GÖRÜNTÜ:        neredeyse YOK; olduğunda ANEMPATİK
TEMPO:                60 BPM (yalnız ölçü hizası için; nabız duyulmaz)
TONALİTE:             tonalite yok — tek aralık, açık beşli
SESSİZLİK KUŞAĞI:     S61-S96 + filmin geri kalanının çoğu
ÇÖZÜLMEYEN CÜMLE:     yok — cümle yok
KAPANIŞ:              S118 kreşendo → S119 iniş → S120 rüzgâr
FREKANS TABANI:       sub 45 Hz + eşlikçi 90/135 Hz + yığın 100/150/200
KATMANLAR:            2 — tek drone · tek yaylı (yalnız 5 girişte)
LUFS:                 -14 nihai / -18 yatak (diğerlerinden 1 dB kısık)
REVERB:               S2-S108 kuru · S109-S119 açık ova
⭐ TOPLAM MÜZİK:       40+32+8+56+24 = 160 s = 2:40 / 16:00 = %17
                       (diğer dördünde %68 — dört kat fark)
```

### 🎯 FİKİR — beş giriş, hepsi tek olay

```
Müzik sürekli çalmaz. Filmde YALNIZ BEŞ KEZ girer, her seferinde tek
bir sürekli ses olarak, ve her girişte bir şey söyler:

  ① S15  1:52  ⟶ 40 s   gökte parıltı belirir (izleyici görür, o görmez)
                        ⭐ dramatik ironi anı — müziğin TEK işlevi bu
  ② S43  5:36  ⟶ 32 s   feda. ⛔ Ama müzik ÜZÜLMEZ: aynı açık beşli,
                        aynı seviye. Anempatik [§9].
  ③ S60  7:52  ⟶ 8 s    orta nokta; müzik girer ve HEMEN bırakılır —
                        4:48'lik sessizliğin kapısını o açar
  ④ S102 13:28 ⟶ 56 s   yerçekimi yağmuru · imza çekim
  ⑤ S117 15:28 ⟶ 24 s   saat + ayağa kalkış + ilk adımlar,
                        S118'de tek kreşendo, S119 sonunda biter

Aralarda müzik YOKTUR. Filmin duygusal zemini oda tonu, nefes ve
kumaştır. 16 dakikanın 13 dakika 20 saniyesi müziksizdir.
```

```
⚠️ DÜRÜST RİSK — bu alternatifin bedeli yazılı olmalı:
   Bu hat YouTube'da, telefonda, kaydırarak izlenen bir mecrada
   yayınlanıyor. 13 dakika 20 saniye müziksiz görüntü, "prestij"
   kazandırır ve İZLEYİCİ KAYBETTİRİR. Depoda bu ölçekte müziksiz bir film
   YAYINLANMADI — yani bu bahsin karşılığı ölçülmüş değil.
   Seçilirse, kararın ölçülmemiş olduğu 00_INDEX'e yazılır.
   ⭐ Karşı argüman da gerçek: filmin S61-S96 arası zaten 4:48
      müziksiz. ⑤ bunu bir istisna olmaktan çıkarıp KURAL yapar —
      ve o zaman sessizlik bir eksiklik değil, filmin dili olur.
```

### 🎹 ÜRETİM PROMPTU — BEŞ GİRİŞ TEK PARÇADA

```
Five short instrumental cues for a science-fiction film, generated as one
piece with silence between them, 60 BPM, 4/4, no key centre — the music
uses one open fifth and almost nothing else.

CUE 1 — 40 seconds: one low drone fades in over 12 seconds and holds a
single open fifth. Nothing moves. It fades out over 10 seconds.
CUE 2 — 32 seconds: the same open fifth, at exactly the same volume and
in the same register as cue 1. Nothing about it is sadder, larger or more
urgent than cue 1. It is indifferent.
CUE 3 — 8 seconds: the fifth enters and is released almost immediately,
leaving the piece open.
CUE 4 — 56 seconds: the fifth returns with one low pulse beneath it,
felt rather than struck, no drum kit and no percussion instruments. A
high thin string layer descends slowly across the whole cue.
CUE 5 — 24 seconds: the fifth, then at 8 seconds a single controlled
crescendo over 8 seconds with a low string section rising underneath,
reaching its peak and stopping. This is the only crescendo in the piece.
The last 8 seconds are one descending held note, then stop.

THROUGHOUT: no melody, no theme, no development, no percussion kit, no
build between cues. Each cue is the same material at the same weight.

FREQUENCY: the sub-bass is doubled by a companion tone one or two octaves
higher, around 90-160 Hz, so the weight survives on small speakers.
Reinforce the low end with a dense harmonic stack at roughly 100 Hz,
150 Hz and 200 Hz so the missing fundamental is implied rather than
played; the perceived weight must survive full loss of everything below
150 Hz.

SPACE: cues 1-4 completely dry, no reverb, no room. Cue 5 has a wide,
flat, open outdoor reverb — the only reverb in the film.

[Instrumental] [No Vocals] [No Percussion] [Sustained]
```

### 🚪 KABUL / RET — ⑤

```
KABUL ① Beş giriş de AYNI malzeme, aynı seviye — 2. giriş (feda)
        1. girişten daha "duygulu" değil.
      ② Girişler arasında hiçbir müzik yok (oda tonu müzik değildir).
      ③ Tek kreşendo 5. girişin içinde, S118'de.
RET   ① Herhangi bir giriş bir melodi taşıyorsa.
      ② Feda girişi büyütülmüşse — anempati düşer, fikir ölür.
      ③ Girişler arasına "çok kısık müzik" konmuşsa [§16: sessizlik
        sahnesi gerçekten sessizdir, kısık müzik değildir].
YABANCI GÖZ  Filmi baştan sona izlet, sor: "Bu filmde müzik var mıydı?"
      → "Sanırım vardı ama hatırlamıyorum" demeli. İdeal cevap budur.
SONUÇ ☐ SEÇİLDİ   ☐ ELENDİ      seed: __________
```

---

# 3. ⚖️ KARŞILAŞTIRMA — hangisi neyi kazandırır

| Ölçüt | ① Kayıtsız | ② Düşen Hat | ③ İki Ses | ④ Doksan Dk | ⑤ Sessizlik |
|---|:--:|:--:|:--:|:--:|:--:|
| Kılavuzun boş bıraktığı aracı kullanıyor (§9 anempati) | ⭐⭐ | — | — | — | ⭐ |
| Filmin adını (yerçekimi) müziğe çeviriyor | — | ⭐⭐ | — | — | — |
| Temayı (FEDAKÂRLIK) yapıya çeviriyor | — | — | ⭐⭐ | — | — |
| Çehov zincirini taşıyor | — | — | ⭐ (S117) | ⭐⭐ (S22→S94) | — |
| 16 dakika boyunca ilgi tutar | ⚠️ | ⭐⭐ | ⭐ | ⭐⭐ | ⚠️⚠️ |
| Üretimi kolay (tek parça, az iterasyon) | ⭐⭐ | ⭐ | ⚠️ | ⚠️ | ⭐⭐ |
| Depoda emsali var | yok | yok | ⭐ (Rem. Dust) | yok | yok |
| Kılavuz kuralını zorluyor | — | — | — | ⚠️ §13 | ⚠️ §16 |

```
⭐ ÖNERİM: ③ İKİ SES

Üç sebep, hiçbiri estetik değil:
  ① Bu filmin TEMASI beyan edilmiş ve indekslenmiş: FEDAKÂRLIK,
     motif sahneleri S30 · S43 · S84 · S117. ③, müziğin yapısını
     bu dört sahnenin ÜÇÜNE bağlar — TEMA_MUHENDISLIGI'nin
     "indekssiz tema dekoratiftir" kuralının müzik tarafı.
  ② Filmin en büyük anlatı riski beyan edilmiş: A'nın son repliği
     S45, sonrası 75 sahne sessiz (00_PLAN §kart-dışı risk ②).
     ③ o boşluğu bir SES BOŞLUĞUNA çevirir — risk, biçime dönüşür.
  ③ Depoda emsali var ve o emsal işe yaramış: THE REMEMBERING DUST'ın
     yarım kalan viyolası kılavuzda örnek olarak anılıyor ("Yapı =
     tema"). ③ aynı mekanizmayı 10 saniye yerine 74 sahneye yayıyor.

⚠️ EĞER FİLMİN İZLENME PERFORMANSI ÖNCELİKSE: ② DÜŞEN HAT.
   En "duyulur" olan, imza çekimi (S102) en iyi taşıyan ve
   fragmanda en iyi kesilen alternatif odur.
```

---

# 4. ⛔ SEÇİMDEN SONRA — MUZIK_VE_SES.md'de kapanacaklar

```
Bu dosya seçim yapmaz, seçenekleri kapatır. Seçim geldiğinde
MUZIK_VE_SES.md şunları taşır ve BAŞKA HİÇBİR ŞEYİ:

□ 1. Seçilen alternatifin künyesi (§17 şablonu, tek yerde)
□ 2. 960 saniyelik spotting cetveli: hangi sahnede hangi katman
     aktif — 120 satır, sahne numarasıyla
□ 3. Ortak kap'ın on maddesi + dört ses maddesi (bu dosyadan taşınır)
□ 4. S94 sessizlik köprüsünün ÖLÇÜMÜ (S68 kalibrasyonuna göre dB)
□ 5. B'nin halüsinasyon sesinin miks reçetesi (KİLİT 30 ① uygulaması)
□ 6. Üretilen parçanın gerçek süresi — ⛔ ffprobe ile ÖLÇÜLÜR, plandan
     alınmaz [D124'ün ses tarafı]. Süre 468/184 s değilse kurgu
     ızgarası değil MÜZİK yeniden üretilir.
□ 7. Mono fold-down kontrolü: geçti/kaldı, tarihli

⚠️ VE HÂLÂ AÇIK OLAN: 00_PLAN'daki `KLİP SÜRESİ = ____`.
   Klip 8,0 saniye değilse bu dosyadaki BÜTÜN saniyeler ve ölçü
   sayıları o ölçümden yeniden türetilir. Yüzdeler korunur,
   mutlak saniyeler korunmaz. ⛔ Müzik üretmeden önce o kapı.
```
