# 🛰️ UZAY ÜSSÜ VE İSTASYON MİMARİSİ KILAVUZU

> **Ne yapar:** kadrajda bir istasyon, üs ya da büyük yapı varsa **ne kadar
> büyük olduğunu** ve **büyüklüğün nasıl kanıtlandığını** söyler. Üç iş:
> ① yapıyı astronota göre ölçeklendirmek, ② ölçeği sahneden sahneye
> kilitlemek, ③ ölçeği tek sabit planda izleyiciye kanıtlamak.
>
> **Kaynak:** TUR 9 (04.09.2026) · dört derin araştırma raporu →
> `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 9.
> **Girdi promptları:** `URETIM_ONCESI_ANALIZ/12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md`
> **Ham raporlar:** `URETIM_ONCESI_ANALIZ/TUR9_HAM_RAPORLAR/`
>
> **Ne yapmaz:** iç mekân FİZİĞİNİ tanımlamaz (→ `KILAVUZ_REHBERI` §3.10),
> dönme yerçekimi mekaniğini tanımlamaz (→ §3.7), yanaşma/kenetlenme
> vuruşlarını tanımlamaz (→ `YANASMA_VE_KENETLENME_KILAVUZU.md`),
> ekran yönü ve kuşbakışı haritayı tanımlamaz
> (→ `UZAMSAL_HARITA` §3 kuşbakışı harita · §4 ekran yönü kilidi).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① BU KILAVUZUN KAYNAĞI ZAYIF BİR TURDU VE BU GİZLENMİYOR.
   TUR 9'un dört raporunun sayısal iddialarının BÜYÜK KISMI denetimde
   düştü: ISS kafes kirişi 94 m yazılmıştı (109 m), Canadarm2 16,8 m
   yazılmıştı (17,6 m), Stanford torusu 1,6 km yazılmıştı (~1,79 km),
   House Rock 30 m yazılmıştı (~12 m), KRUSTY 4 m yazılmıştı (~1,9 m),
   basınçlı gezici 5×3 m yazılmıştı (6,0×5,2×3,8 m). Aşağıdaki ölçülerin
   HEPSİ denetimden geçmiş olanlardır; düşenler süzme kaydında adıyla
   duruyor ve bir daha "araştırmada vardı" diye geri eklenmez.

② ASTRONOT CETVELİ TEK. Dört rapor dört farklı boy kullandı
   (1,90 · 1,90-1,95 · 2,00 · ima yoluyla 2,20 m) ve aynı 4,2 m'lik
   modül raporlar arasında 2,10 ile 2,50 gövde boyu arasında gezindi.
   ⭐ DEPO KARARI: 1 GÖVDE BOYU (1H) = kasklı, basınç giysili, ayakta
   karakterin boyu = 1,90 m. Bu bir ÖLÇÜM DEĞİL SÖZLEŞMEDİR ve yalnız
   DIŞ (EVA) sahneler içindir. İç mekânda karakter kasksızdır ve aynı
   sayı kullanılamaz.

③ "ÇAPA" VE "KAYMA RİSKİ" SÜTUNLARI DIŞ KANIT DEĞİLDİR.
   Dört promptun dördü de bu sütunları raporun önüne koydu, dört rapor
   da onları doldurdu — tek bir koşu, sürüm, seed ya da başarısızlık
   oranı olmadan. Bu kılavuzda o satırlar ⚙️ ÜRETİM TERCİHİ damgası
   taşır ve ölçülmüş satırlarla AYNI tabloda durmaz.

④ HİÇBİR FİLM ÜRETİLMEDİ. Bu kılavuzun ilk sınavı, istasyon/üs içeren
   ilk filmin ① KARE (ölçek satırı) ve ② DEVAMLILIK (yapı kilidi)
   skorlarıdır. Skorlar bugünkü bandında kalırsa kılavuz revize edilir.
```

---

# 1. 📏 ÖLÇEK BİRİMİ — metre SPEC'te, oran promptta

**Mekanizma:** depo iki dersi aynı anda tutamıyordu. **Ders 32** yapı
oranlarını korumak için image prompta metre yazdırıyordu
(`door height = 2.1m … COPIED IDENTICALLY into every scene prompt`);
**Ders 138** ise ölçünün prompt gövdesine inince modelin onu nesnenin
ÜSTÜNE bastığını ölçtü (THE THIN ROOF S2 · 22,41 s · halkanın iç yayına
`11 metres` + gradasyon çentikleri). İki ders çarpıştığı için ikisi de
uygulanamıyordu.

```
⭐ ÇÖZÜM — AYNI ORAN, İKİ AYRI YERDE, İKİ AYRI DİLDE

  SPEC (D bloğu) + PLAN fizik defteri     →  METRE
     hull 11,0 m · hatch 0,80 m · handrail 0,53 m · figure 1,90 m
     Burada ölçülür, burada denetlenir, buradan değişmez.

  IMAGE / VIDEO PROMPT gövdesi            →  GÖVDE BOYU (nesne göreli)
     "the hull's long axis reads about six body-lengths of the figure
      standing beside it"
     "the opening is barely wider than her shoulders"
     Rakam yok, birim yok, çentik yok.

⛔ Prompt gövdesine ASLA: metre · santimetre · derece · f-sayısı ·
   "2.1m" · "25 degrees" · "f/128". [D45 dizge riski · D138 kapsam]
✅ Kamera MESAFESİ muaftır ("from ten meters away") — kadrajdaki bir
   nesneye bitişik değildir. [D138 muafiyet satırı]
```

**Dönüşüm tablosu — 1H = 1,90 m (yalnız denetimden geçmiş ölçüler):**

| Yapı öğesi | Ölçü | Gövde boyu | Prompt gövdesindeki hâli |
|---|--:|--:|---|
| Modül gövde çapı (ISS/Tiangong bandı) | 4,2-4,5 m | 2,2-2,4 H | *a little over two body-lengths across* |
| Skylab gövde çapı (en geniş uçmuş) | 6,6 m | 3,5 H | *three and a half body-lengths across* |
| Dar modül (Gateway sınıfı) | 3,0 m | 1,6 H | *barely wider than a figure is tall* |
| Yanaşma kapağı açıklığı (CBM) | 1,27 m | 0,67 H | *an opening two thirds of a body-length across; she passes through without turning* |
| Kenetlenme kapağı açıklığı (SSVP/IDSS) | 0,80 m | 0,42 H | ⛔ giysili gövde GEÇEMEZ — yalnız kadrajda ölçek çapası: *a round opening no wider than the pack on her back* |
| Kafes kirişi kesiti | 4,5 × 4,6 m | 2,4 H | *a bay nearly two and a half body-lengths tall; the figure beside it reaches less than half its height* |
| Kafes kirişi tam boy | 109 m | 57 H | *a spine that runs out of frame in both directions* |
| Güneş kanadı (tek) | 34,2 × 11,6 m | 18 H × 6 H | *a wing eighteen body-lengths long* |
| Güneş kanadı açıklığı (uçtan uca) | 72,8 m | 38 H | — (tek kadraja girmez) |
| Robot kol | 17,6 m · Ø 0,35 m | 9,3 H · 0,18 H | *a jointed arm about nine body-lengths long, no thicker than a thigh* |
| EVA tutamağı | ~0,53 m ⚠️ tek kaynaklı | 0,28 H | *a handrail a little longer than her forearm* |
| İniş aracı tam boy | 7,04 m | 3,7 H | *a lander a little under four body-lengths tall* |
| İniş aracı ayak açıklığı | 9,4 m | 4,9 H | *legs spread five body-lengths apart* |
| İniş aracı kapağı | 0,81 × 0,81 m | 0,43 H | *a square opening she has to crouch through* |
| Merdiven basamak aralığı | 0,23 m | 0,12 H | *rungs a hand-span apart* |
| En alt basamak — pabuç arası | 0,76 m | 0,40 H | *the last rung sits chest-high above the pad* |
| Yüzey habitatı tam boy | ~10 m | 5,3 H | *five body-lengths tall* |
| Yüzey habitatı yaşam katı çapı | 6,5 m | 3,4 H | *three and a half body-lengths across* |
| Basınçlı gezici | 6,0 × 5,2 × 3,8 m | 3,2 × 2,7 × 2,0 H | *a rover taller than she is, twice as long as it is tall* |
| Mikro reaktör (KRUSTY sınıfı) | ~1,9 m | 1,0 H | *a drum exactly her own height* |
| Dikey güneş kulesi | 10 m | 5,3 H | *a mast five body-lengths tall* |
| Lav tüpü çukuru (Marius Hills) | 65 × 90 m · ~34 m derin | 34-47 H · 18 H | *a pit so wide the far rim is a thin line* |

> ⚠️ **BU TABLODA OLMAYAN ÖLÇÜ PROMPTA YAZILMAZ.** Tabloya girmeyen her
> sayı ya denetimde düştü ya hiç ölçülmedi; ikisi de aynı kapıdan geçer.
> Yeni bir öğe gerekiyorsa önce ölçüsü bulunur, sonra 1,90'a bölünür,
> sonra tabloya satır olarak yazılır — prompta doğrudan girmez.

---

# 2. 🛰️ YÖRÜNGE İSTASYONU — dış anatomi

## 2.1 Dört silüet — ve hangisinin AI'da ne kadar tuttuğu

| Silüet | Mimari | Örnek | ⚙️ Üretim notu |
|---|---|---|---|
| **Tek gövdeli silindir** | Tek boru, panel gövdeden açılır | Skylab · Salyut | En sade geometri; kadrajda tek kütle. |
| **Kafes ve modül** | Yatay kiriş omurgası + ona dik modül dizisi + uçlarda kanatlar | ISS | Dik açılı ve hiyerarşik; kiriş çubukları kalabalıklaşırsa karışır. |
| **Tek hat** | Uç uca eklenmiş modüller ("T" ya da haç), harici kiriş YOK | Tiangong | Kafesin karmaşası olmadan büyük kütle. |
| **Yıldız kümesi** | Çekirdek + küresel düğüm + farklı eksenlerde kollar | Mir | Asimetrik; kadrajda okunması en zor siluet. |
| **Dönen halka** | Torus + parmaklık + göbek | uçmamış | Fiziği ayrı karttadır → `KILAVUZ_REHBERI` §3.7. |

```
⛔ SİLÜET SEÇİMİ PLANA YAZILIR ve film boyunca DEĞİŞMEZ.
   Aynı istasyonun bir sahnede kafesli, bir sahnede tek hat görünmesi
   Ders 32'nin ölçtüğü oran kaymasının en büyük hâlidir.
```

## 2.2 Sayılabilir çapa — büyük, geometrik, TEK sayı

⚙️ **ÜRETİM TERCİHİ** — ölçülmedi, denenecek.

```
PLANA YAZILAN ANATOMİ KARTI (istasyon başına bir kez, film boyu sabit)

  MODÜL         hizada n silindir            n = 3 önerilir
  KANAT         simetrik n kanat             n = 2 veya 4 (tek sayı YAZMA)
  RADYATÖR      düz beyaz n panel            n = 3 (ISS'te EATCS 3 kanattır)
  PORT          n kapak, hangi tarafta       n = 1-2, tarafı yazılır
  PENCERE       n pencere                    en fazla 1 büyük + n küçük

⛔ "hundreds of handrails", "thousands of struts" gibi SAYISIZ ÇOĞUL
   hiçbir bantta yazılmaz — model saymaz, doldurur ve doldurduğu şey
   her karede değişir.
⛔ Anten kümesi, kablo demeti, gevşek örtü kırışığı, dış deney paleti
   çapa DEĞİLDİR; kadrajda tutulacaksa tek ve büyük yazılır.
```

## 2.3 Kapak iki sınıftır — ve ikisi iki ayrı sahne kurar

```
GENİŞ / YANAŞMA KAPAĞI      1,27 m · 0,67 H · yuvarlatılmış KARE
  Kargo ve raf geçsin diye büyüktür. Giysili gövde rahat geçer.
  "an opening two thirds of a body-length across; she passes through
   without turning"

DAR / KENETLENME KAPAĞI     0,80 m · 0,42 H · DAİRE
  Giysisiz mürettebat için tasarlandı. Sırt üniteli gövde SIĞMAZ.
  "a round opening no wider than the pack on her back; she stops in
   front of it"

⭐ KADRAJ OKUMA KURALI: büyük kare kapak = Batı segmenti · küçük yuvarlak
   kapak = Rus/Çin segmenti. Kapak biçimi tek başına istasyonun kimliğini
   söyler ve metin gerektirmez.
⛔ Basınç giysili bir karakteri dar kapaktan GEÇİRME. Sırt ünitesiyle
   toplam derinlik açıklıktan büyüktür; sahne fizik hatası olur.
```

## 2.4 Yaşlanma merdiveni — metinsiz sayaç

Yörünge yüzeyi dört yönlü işaret taşır ve dördü de **yalnız artar**.
Bu, `Kart 5`'in üçüncü kanalıdır: sayaç metinle değil fizikle anlatılır.

```
MONOTONİK — hiçbir sahnede geri dönmez [D147 kir merdiveni mantığı]

  ① UV SARARMASI     beyaz beta örtüsü matlaşır ve sarıya döner
  ② İTİCİ KURUMU     kenetlenme portu çevresinde kahverengi-siyah halka
  ③ MMOD ÇUKURU      yüzeyde mm ölçekli koyu çukurcuk dokusu (cm DEĞİL)
  ④ TUTAMAK AŞINMASI kavrama noktasında boya kalkar, metal parlar

YENİ İSTASYON   bembeyaz gergin örtü · kurum yok · çukur yok
YİRMİ YILLIK    sarı-mat örtü · portta kurum halkası · çukurlu yüzey

⛔ Faz SATIRI her prompta yazılır, faz ADI yazılmaz. [D155: "PHASE 1"
   göğse basıldı.]
```

---

# 3. 🌑 YÜZEY ÜSSÜ — Ay ve Mars

## 3.1 Gölge kuralı — kutupta ölçek ışıkla yazılır

Ay'ın eksen eğikliği 1,54°; kutupta Güneş bu açının üstüne çıkmaz.
Shackleton enleminde tavan ~1,9°'dir. Gölge uzunluğu tek formülden çıkar:

```
GÖLGE = YÜKSEKLİK ÷ tan(güneş yüksekliği)

  2,0°  →  ×28,6      (fiziksel TAVAN, en kısa gölge)
  1,5°  →  ×38,2      ⭐ VARSAYILAN
  1,0°  →  ×57,3      (en dramatik)

  Örnek: 10 m'lik habitat 1,5°'de 382 m gölge atar = 201 gövde boyu.
         10 m'lik güneş kulesi aynı açıda 382 m.

⛔ "Kilometrelerce gölge" YANLIŞTIR. 1 km gölge için yapının 2°'de
   35 m, 1,5°'de 26 m yüksek olması gerekir. Depodaki hiçbir yapı
   o boyda değil. Kilometrelik gölge yalnız krater kenarına aittir.
⛔ Gölge uzunluğu prompta METREYLE yazılmaz: "her shadow runs so far
   it leaves the frame" ya da "the mast's shadow crosses the whole
   plain and does not end inside the frame".
```

**Ekvator kartı ayrıdır:** 14,75 günlük gündüz (+127 °C) ve 14,75 günlük
gece (−173 °C). Kutupta bu döngü yoktur; ışık yönü neredeyse sabittir ve
bu, çok sahneli bir üs filminde ışık sürekliliğini FİZİKLE garanti eder.

## 3.2 Yerleşim grameri — mesafe değil, DİZİLİM iner

⚙️ **ÜRETİM TERCİHİ.** TUR 9'un verdiği bütün mesafe sayıları
(pist 1 km · reaktör 500 m-2,8 km · avlu 10-50 m) denetimde kaynaksız
çıktı ve İNMEDİ. İnen şey mantıktır:

```
İNİŞ PİSTİ    en uzakta ve bir setin/tepenin ARDINDA.
              Gerekçe fiziktir: iniş püskürtüsü birkaç yüz m/s ile
              ~3 km/s arasında saçılır ve Ay kaçış hızı 2,38 km/s'dir —
              en ince fraksiyon yüzeyi TERK EDER. Mesafe tek başına
              koruma değildir; engel gerekir.
GÜÇ ALANI     görüş hattı dışında, tercihen krater ardında. Habitata
              tek bir kalın, gergin, koyu kablo hattıyla bağlanır.
ANTEN         kesintisiz Dünya gören en yüksek sırtta.
AVLU          habitatın dibinde: tank, batarya, hortum. Ölçüt tek ve
              dramatik: karakter buradan hava kilidine KOŞARAK yetişir.
```

**İnsansız kadrajda üs nasıl okunur** (Kart 10'un bu ortamdaki hâli):

```
AYDA   patika hiç silinmez. Tekrar kullanılan hat ezilir, sıkışır,
       altındaki koyu regolit çıkar ve asfalt gibi kararır.
MARSTA patika dolar ve yumuşar; her yüzey aynı kızıl oksite boyanır.
       Yaş, izin keskinliğiyle değil KAYBOLMASIYLA okunur.

⭐ İkisi TERS yönde çalışır: Ayda yaşlanma iz BİRİKTİRİR, Marsta iz SİLER.
```

## 3.3 Biçimin gerekçesi

```
Basınç kabı KÖŞELİ olamaz — iç basınç köşede yırtar. Küre ideal, ama
fırlatma kaportası silindiri dayatır. Bu yüzden her şey silindir,
kapsül ya da torustur.

Basınç bandı:  kabin 101 kPa · keşif atmosferi ~57 kPa · giysi ~30 kPa

Radyasyon örtüsü 1,5-2,5 m regolit = 0,8-1,3 gövde boyu.
⛔ Bu "Dünya atmosferi eşdeğeri" DEĞİLDİR — eşdeğerlik için ~6,5 m
   gerekir. Bu bir GÜNEŞ PATLAMASI SIĞINAĞI mertebesidir.
Sonuç görsel: üs narin bir laboratuvar değil, gömülü bir tümsektir.

Toz kontrolü kapıyı belirler: suitport (giysinin sırttan girilen kapağı)
tozlu giysiyi hiç içeri almaz. Dış cephede yan yana duran suitportlar
üssün en okunaklı anatomik uzvudur ve tam bir gövde geçişi kadardır.
```

---

# 4. 🚪 BASINÇLI İÇ HACİM

> Bu bölümün FİZİĞİ ayrı karttadır: `KILAVUZ_REHBERI` §3.10 (04.09.2026'da
> bu turla açıldı). Burada yalnız MİMARİ gramer durur.

```
KORİDOR       ISS modülünde yaşanabilir kesit ~2 × 2 m'lik bir KARE
              tüneldir; dört yüzey de raf sırasıdır, köşeler tesisat
              kamasıdır. Yani "zemin" yoktur, dört duvar vardır.
RAF           standart raf 2,01 × 1,05 × 0,86 m — bir gövde boyundan
              biraz uzun, iki omuz genişliğinde.
              ⚙️ Kadrajda duvar başına 4 BÜYÜK BLOK yazılır (gerçekte
              sıra başına 6'dır) — bu bir tasarım tercihidir, ISS
              gerçeği diye sunulmaz.
KABİN         ABD mürettebat kabini 2,1 m³ · Rus kayutası 1,17 m³
              (0,73 × 0,85 × 1,89 m). İkisi de bir telefon kulübesi.
YEREL DİKEY   mikro yerçekiminde "yukarı" biyolojik değil GÖRSELDİR ve
              renkle kurulur: tavan beyaz · duvar krem · zemin koyu
              (zeytin/kahve). Işık yalnız tavandan gelir. Bu üç satır
              olmadan izleyici yönünü kaybeder.
IŞIK          gerçek referans ~4500 K, parlamasız, yüzeyde sert gölge.
PENCERE       gözlem kubbesi: 1 büyük dairesel (0,80 m) + 6 yamuk yan.
              Bir gövde omzu büyük pencereyi neredeyse doldurur.
```

```
⛔ İÇ MEKÂNDA GÖVDE BOYU 1,90 m DEĞİLDİR — karakter kasksızdır.
   İç ölçüler için ayrı bir cetvel gerekir ve TUR 9 onu ölçmedi.
   İç mekân oranları bugün yalnız NİTELİKSEL yazılır.

⛔ SİNEMA KALİBRASYONU BOŞ ÇIKTI — dürüst kayıt.
   Deponun sorusu "sinema iç mekânı büyütüyor mu, ölçüldü mü" idi.
   TUR 9 tek bir ölçülü karşılaştırma getirmedi: "Gravity'de hacimler
   %20-30 geniş" ve "Hermes koridorları 4 m" iddialarının ikisi de
   kaynaksız çıktı. Bu kılavuz o soruyu AÇIK BIRAKIR ve hiçbir
   "sinema büyütür" kuralı yazmaz.
```

---

# 5. 🔭 ÖLÇEK KANITI — tek sabit planda büyüklük

## 5.1 Neden kırılır

Vakumda ışık saçılmaz: bir metre ötedeki kaya ile ufuktaki dağ aynı
keskinlikte, aynı kontrastta, aynı mutlak siyah gökyüzüne karşı durur.
Beynin mesafe hesabı çöker, boyut hesabı da onunla birlikte çöker.

```
BELGELENMİŞ İKİ VAKA — sayısız, olay olarak

  Apollo 14 · Cone Krateri: Shepard ve Mitchell kraterin kenarına
  ulaşamadan döndüler; sonradan kenara çok yaklaşmış oldukları anlaşıldı.
  Güneş alçaktı ve kabartmayı gösterecek gölge yoktu.

  Apollo 16 · House Rock: mürettebat bir ev büyüklüğündeki kayayı
  yakın ve küçük sandı; aynı bölgede yamaç eğimini de olduğundan
  çok daha dik okudular.

⛔ Bu vakalara iliştirilen bütün sayılar ("30 m yükseklik", "400 metreyi
   50 metre sandılar", "80 metrelik yükseklik") denetimde düştü. Vaka
   iner, sayı inmez.
```

## 5.2 Mesafe → kadraj kesri tablosu

**Kesir = (nesne yüksekliği × odak) ÷ (mesafe × sensör dikey yüksekliği)**

```
⭐ SENSÖR DİKEYİ KADRAJ ORANINA GÖRE DEĞİŞİR — ve bu tek satır
   TUR 9'un tablolarını geçersiz kılmıştı:

     16:9 yatay   dikey = 20,25 mm   (tam kare 36×24'ten kırpılır)
     9:16 dikey   dikey = 36,00 mm   (kamera döndürülür)

   Rapor 3:2 fotoğraf karesini (24 mm) varsaymıştı. Aynı sahne
   16:9'da raporun dediğinden %18,5 BÜYÜK, 9:16'da %33 KÜÇÜK kaplar.
   Aynı nesne yatayda dikeydekinin 1,78 KATI kadar kadraj doldurur.
```

**Her hücre: `%16:9 / %9:16`. Depo lensleri: 24 · 32 · 35 · 50 mm.**

| Nesne | mesafe | 24 mm | 32 mm | 35 mm | 50 mm |
|---|--:|--:|--:|--:|--:|
| **Modül gövdesi** 4,2-4,5 m | 1000 m | %0,50 / %0,28 | %0,66 / %0,37 | %0,73 / %0,41 | %1,0 / %0,58 |
|  | 200 m | %2,5 / %1,4 | %3,3 / %1,9 | %3,6 / %2,0 | %5,2 / %2,9 |
|  | 50 m | %10,0 / %5,6 | %13 / %7,5 | %15 / %8,2 | %21 / %12 |
|  | 10 m | %50 / %28 | %66 / %37 | %73 / %41 | %104 / %58 |
|  | 2 m | %249 / %140 | %332 / %187 | %363 / %204 | %519 / %292 |
| **Kafes kirişi kesiti** 4,6 m | 1000 m | %0,55 / %0,31 | %0,73 / %0,41 | %0,80 / %0,45 | %1,1 / %0,64 |
|  | 200 m | %2,7 / %1,5 | %3,6 / %2,0 | %4,0 / %2,2 | %5,7 / %3,2 |
|  | 50 m | %11 / %6,1 | %15 / %8,2 | %16 / %8,9 | %23 / %13 |
|  | 10 m | %55 / %31 | %73 / %41 | %80 / %45 | %114 / %64 |
|  | 2 m | %273 / %153 | %363 / %204 | %398 / %224 | %568 / %319 |
| **Yanaşma kapağı (CBM)** 1,27 m | 1000 m | %0,15 / %0,08 | %0,20 / %0,11 | %0,22 / %0,12 | %0,31 / %0,18 |
|  | 200 m | %0,75 / %0,42 | %1,0 / %0,56 | %1,1 / %0,62 | %1,6 / %0,88 |
|  | 50 m | %3,0 / %1,7 | %4,0 / %2,3 | %4,4 / %2,5 | %6,3 / %3,5 |
|  | 10 m | %15 / %8,5 | %20 / %11 | %22 / %12 | %31 / %18 |
|  | 2 m | %75 / %42 | %100 / %56 | %110 / %62 | %157 / %88 |
| **Kenetlenme kapağı (SSVP/IDSS)** 0,80 m | 1000 m | %0,09 / %0,05 | %0,13 / %0,07 | %0,14 / %0,08 | %0,20 / %0,11 |
|  | 200 m | %0,47 / %0,27 | %0,63 / %0,36 | %0,69 / %0,39 | %0,99 / %0,56 |
|  | 50 m | %1,9 / %1,1 | %2,5 / %1,4 | %2,8 / %1,6 | %4,0 / %2,2 |
|  | 10 m | %9,5 / %5,3 | %13 / %7,1 | %14 / %7,8 | %20 / %11 |
|  | 2 m | %47 / %27 | %63 / %36 | %69 / %39 | %99 / %56 |
| **Yüzey habitatı tam boy** 10 m | 1000 m | %1,2 / %0,67 | %1,6 / %0,89 | %1,7 / %0,97 | %2,5 / %1,4 |
|  | 200 m | %5,9 / %3,3 | %7,9 / %4,4 | %8,6 / %4,9 | %12 / %6,9 |
|  | 50 m | %24 / %13 | %32 / %18 | %35 / %19 | %49 / %28 |
|  | 10 m | %119 / %67 | %158 / %89 | %173 / %97 | %247 / %139 |
|  | 2 m | %593 / %333 | %790 / %444 | %864 / %486 | %1235 / %694 |
| **İniş aracı tam boy** 7,0 m | 1000 m | %0,83 / %0,47 | %1,1 / %0,63 | %1,2 / %0,68 | %1,7 / %0,98 |
|  | 200 m | %4,2 / %2,3 | %5,6 / %3,1 | %6,1 / %3,4 | %8,7 / %4,9 |
|  | 50 m | %17 / %9,4 | %22 / %13 | %24 / %14 | %35 / %20 |
|  | 10 m | %83 / %47 | %111 / %63 | %122 / %68 | %174 / %98 |
|  | 2 m | %417 / %235 | %556 / %313 | %608 / %342 | %869 / %489 |

```
OKUMA
  ① 1000 m'de hedef 1080 satırlık karede ~10 pikseldir. Bu bir SAHNE
     DEĞİLDİR, bir açılış noktasıdır — malzeme, biçim, doku okunmaz.
  ② 10 m bandı formata göre üç ayrı sahne kurar: 50 mm'de yapı 16:9'da
     kadrajı TAŞAR (%104), 9:16'da yarısını biraz geçer (%58).
  ③ 2 m bandında taşma ZORUNLUDUR — kapak dışında hiçbir yapı sığmaz.
  ⚠️ 2 m satırları iğne deliği yaklaşımıdır; gerçek değer %1-2,6 daha
     düşüktür. 10 m ve üstünde sapma ihmal edilir.
```

## 5.3 Ölçek şahidi merdiveni — hangi bantta ne kanıtlar

| Bant | Kanıtlayan | Kadrajda ne var | ⚠️ |
|---|---|---|---|
| **1000 m** | yok | parlak nokta | Ölçek KURULAMAZ. Yalnız "orada bir şey var" der. |
| **200 m** | ritim | tekrar eden kanat/radyatör/modül dizisi | Beyin ritmi sayar, kütleyi tahmin eder. |
| **50 m** | mimari | kapak, pencere, port | İlk tanıdık-boyut ipucu: "oradan bir insan geçer". |
| **10 m** | ergonomi | tutamak, perçin, kalkan katmanı | Kadraja giren figür ölçeği ANINDA kilitler. |
| **2 m** | doku | örtü dikişi, çukur, giysi dokuması | Taşma + doku = "bu devasa bir şeyin yüzeyi". |

```
SABİT KAMERADA ÇALIŞAN ÜÇ ARAÇ (kesme ve kamera hareketi yok)
  ① ÖN PLANDA FİGÜR — kadrajın köşesinde küçük bir gövde, arkada yapı.
     En hızlı ve en güvenilir kilit.
  ② TEKRAR EDEN BİRİM — aynı öğenin perspektifte küçülerek dizilmesi.
  ③ KADRAJI TAŞAN KENAR — yapının sınırı iki yandan dışarı çıkar.

⛔ Paralaks ve yavaş dönüş bu depoda KULLANILAMAZ (kamera kilitli).
⛔ Yumuşak gölge yapıyı stüdyo maketine indirger. Tek sert kaynak şart.
```

⭐ **ON İŞLENMİŞ VAKA: `DIS_REFERANS_OLCUMU.md §3`** (🆕 05.09.2026) — dış
referanslardan çıkarılmış şahit sözlüğü: her satırda *şahit → ölçülen →
yukarıdaki araç*, ve **kilitli kamerada çalışıp çalışmadığı**. Bu son sütun
zorunludur: referansların hepsi ölçeği kamera hareketiyle kuruyor, o bu
depoda yasak — taşınabilir olan hareket değil, ŞAHİDİN KENDİSİDİR. On
vakanın dokuzunda şahit kamera dursa da iş görür; onuncusunda hiç şahit
yoktur ve o klip bu depoya hiçbir şey vermez.

⚠️ `§3.1`'de bu listeden çıkan **dördüncü statik araç adayı** duruyor:
çerçeve içinde çerçeve (kadrajın kenarını bilinen bir insan yapısı tutar).
ADAYDIR — üretimde ölçülmedi; yukarıdaki üçlüye girmesi kart G'den geçer.

## 5.4 Maket etkisi — yasak bulanıklık DEĞİL, bulanıklık GRADYANI

```
Ölçülmüş mekanizma (Held, Cooper, O'Brien & Banks 2010, ACM TOG):
küçültme etkisini yapan şey bulanıklığın varlığı değil, kadraj boyunca
uzanan DİKEY BULANIKLIK GRADYANI'dır. Uzun odakta tekdüze bulanık bir
arka plan maket okutmaz; üstten alta kayan bir netlik bandı okutur.

✅ prompt:  "no tilt-shift look, no miniature or toy-model read, no
             vertical band of blur across the frame; the far end of the
             hull is as sharp as the near end"
⛔ prompt:  "f/128 aperture equivalent"   → D45 dizge riski, HUD basar
⛔ prompt:  çıplak "no shallow depth of field" → depo şablonu karakter
            çekimlerinde sığ DOF'u REÇETE olarak yazıyor. Yasak yalnız
            YAPIYA bağlanır: "no shallow depth of field on the structure".
```

---

# 6. 🚫 NEGATİF EKLENTİSİ — iki ayrı blok

> Negatif çekirdek (`KILAVUZ_REHBERI` §5) DEĞİŞMEZ; bunlar onun ÜSTÜNE
> eklenir. İki blok birbirinin yerine geçmez: yörüngedeki "süzülen
> parçacık yok" cümlesi Ay yüzeyinde FİZİK HATASI yazdırır (§3.1: toz
> yükselir ve gitmez).

**[YÖRÜNGE / EVA]**
```
No free-floating debris, no drifting flecks, nothing untethered in the
vacuum around the structure. Insulation panels are rigid, taut,
drum-tight, foil-skinned, seamed in flat rectangles — nothing billows, nothing flaps,
nothing hangs loose. One unfiltered sun, no fill light, shadow edges as
sharp as the frame allows; hard specular glints with immediate falloff,
zero halo, zero glow spill onto neighbouring pixels. No atmospheric
haze, no aerial perspective, no light scattering of any kind. No
tilt-shift look, no miniature or toy-model read, no vertical band of
blur across the frame, no shallow depth of field on the structure — the
far end of the hull is as sharp as the near end. No national flag, no
agency logo, no mission patch, no manufacturer marking, no painted
roundel or emblem of any kind on the hull.
```

**[YÜZEY ÜSSÜ · AY — vakum]**
```
Insulation and covers are rigid and taut — nothing billows, nothing
flaps. One unfiltered sun low on the horizon, no fill light, shadows
absolutely black with razor edges, running out of frame. No atmospheric
haze, no aerial perspective. No tilt-shift look, no miniature or
toy-model read, no shallow depth of field on the structure. No national
flag, no agency logo, no mission patch, no painted emblem on any
surface. Tracks and worn paths are permanent and unchanging.
```

**[YÜZEY ÜSSÜ · MARS — ince atmosfer]**
```
Insulation and covers are rigid and taut — nothing billows, nothing
flaps. One low sun; shadows soft-edged and weak but the frame stays
high-contrast — this softness is correct, not a rendering fault. No
tilt-shift look, no miniature or toy-model read, no shallow depth of
field on the structure. No national flag, no agency logo, no mission
patch, no painted emblem on any surface. Tracks are dulled and
partly filled with settled dust, unchanging within the shot.
```

```
⛔ AY BLOĞUNU MARS'A YAPIŞTIRMA — bu kılavuzun kendi uyardığı hata.
   Mars'ta atmosferik saçılma VARDIR ve meşrudur: "no atmospheric
   haze" ile "shadows absolutely black" cümleleri orada FİZİK HATASI
   yazdırır ve §3.2 ortam kartıyla çarpışır (KILAVUZ_REHBERI §3.2:
   "Gölge zayıf ve yumuşak kenarlı — MEŞRU, hata değil · Dolgu ışığı
   VAR ve motivasyonlu"). Ayrıca mutlak siyah gölge dayatması, ince
   atmosfer filmlerinde kurgunun parlaklık kapısını düşürür.
```

```
⛔ "raytraced lighting" YAZILMAZ — render motoru terimidir ve negatif
   çekirdeğin "no Unreal Engine look, no CGI aesthetic" satırına çarpar.
⛔ "fabric", "cloth", "blanket" kelimeleri prompt gövdesine girmez;
   model onları yeryüzü kumaşı sanıp dalgalandırır. Pozitif ve KATI
   adla yazılır [D59 · D153]: "taut foil-skinned insulation panels".
⛔ Gerçek araç/ajans adı (Dragon, Soyuz, NASA) prompta yazılmaz —
   D45/D155 dizge riski ve Kart 12 politika yüzeyi.
✅ Pozitif hâl [D59]: "the only things carrying information on this hull
   are seams, rivets, handhold grooves and micrometeoroid pitting".
```

**Tutamak — mesafeye bölünmüş tek kural** (⚙️ deneme, ölçülmedi):
```
UZAK BANT (≥50 m)   tutamak YAZILMAZ. Yüzlerce ince çubuk kayma üretir.
YAKIN BANT (≤10 m)  SAYILI ve TEK yazılır:
                    "a single gold handrail, thin enough to close a gloved
                     hand around, within reach of the figure"
HİÇBİR BANTTA       "hundreds of handrails" gibi sayısız çoğul yazılmaz.
```

---

# 7. 🔁 DÖNEN YAPI — bu kılavuzun ölçtüğü tek yeni sınır

Dönme yerçekiminin fiziği ve **bütün sayıları** `KILAVUZ_REHBERI` §3.7'dedir
(1 g için yarıçap · tasarım ölçütü · süpürme hızı). Bu bölüm o sayıları
TEKRARLAMAZ; yalnız kadrajda ne işe yaradıklarını söyler.

```
⭐ SABİT KAMERADA DÖNMENİN TEK UCUZ KANITI ARKA PLANDIR.
   Kamera gövdeye kilitliyse yapı kadrajda durur, evren döner. Yıldız
   alanı ya da gezegen kadrajı doğrusal bir yayla süpürür ve süpürme
   miktarı doğrudan devir sayısından gelir (tablo §3.7'de).

   Prompt SÜREYLE yazılır, dereceyle değil [D138]:
   "the starfield sweeps most of the way around the frame during the
    shot, in one steady direction, never reversing"

   İkinci ve üçüncü kanıt §3.7'de zaten yazılı: gölgenin gövde üzerinde
   hızla yer değiştirmesi, ve serbest bırakılan cismin YANA inmesi.
```

```
⛔ TASARIM ÖLÇÜTÜ PLANA YAZILIR — ve deponun kendi filmi onu aşıyor.
   THE HEAVY SIDE'ın halkası SABİT DÖNMÜYOR, HIZLANIYOR: periyot
   60 saniyede 13,00 s'den 8,00 s'ye iniyor. Karşılığı:
       başlangıç  T = 13,00 s → 4,6 RPM → 2,10 m/s² = 0,21 g
       son        T =  8,00 s → 7,5 RPM → 5,55 m/s² = 0,57 g
   Yani film boyunca devir sayısı 4,6'dan 7,5'e çıkıyor ve BANDIN
   TAMAMI §3.7'nin 1-2 RPM tasarım ölçütünün ÜSTÜNDE.
   ⚠️ Bu bir kusur DEĞİL — hızlanma filmin KONUSUDUR ve ağırlığın
      artışı (202 N → 533 N) senaryonun kendisidir. Ama plana yazılır:
      bu ortamda oturan bir insan adapte olmuş sayılmaz.
   ⛔ Ve "ağırlıksızlığa yakın" DEĞİLDİR: film 0,21 g ile açılıp
      0,57 g ile kapanıyor. Sayılar filmin QA_SPEC'inde durur, bu
      kılavuzda değil.
```

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 8 maddesi

```
□ SİLÜET TİPİ planda mı (§2.1) — film boyu tek mi?
□ ANATOMİ KARTI dolu mu (§2.2): modül n · kanat n · radyatör n · port n?
□ ÖLÇÜLER SPEC'te metre, PROMPTTA gövde boyu mu (§1)?
  ⛔ Prompt gövdesinde tek bir metre/derece/f-sayısı bile varsa GEÇMEZ.
□ KAPAK SINIFI seçildi mi (§2.3) ve giysili gövde dar kapaktan
  geçirilmiyor mu?
□ YAKLAŞMA DİZİSİ varsa kesirler §5.2'den TÜRETİLDİ mi — aynı nesne,
  aynı eksen (kare yüksekliği), monotonik büyüme, sabit yönelim?
□ ÖLÇEK ŞAHİDİ her yapı planında var mı (§5.3): figür / tekrar eden
  birim / taşan kenar — en az biri?
□ YAŞLANMA FAZI yazıldı mı (§2.4 · §3.2) ve MONOTONİK mi?
□ NEGATİF BLOK doğru olan mı seçildi (§6) — yörünge mi yüzey mi?
```

---

# 9. ⬜ BU KILAVUZUN SINIRI — açık kalanlar

```
① İÇ MEKÂN CETVELİ YOK. Kasksız gövde boyu ölçülmedi; iç oranlar
   niteliksel. Bir sonraki tur bunu kapatmalı.
② TUTAMAK ÖLÇÜSÜ ZAYIF. "0,53 m" tek kaynaklı; aralık hiç ölçülmedi.
   §1 tablosundaki tek gevşek satır budur.
③ "SİNEMA BÜYÜTÜR" SORUSU KAPANMADI (§4). Ölçülü tek karşılaştırma yok.
④ ÇAPA/KAYMA SÜTUNLARI SINANMADI. ⚙️ damgalı her satır bir hipotezdir;
   ilk üretimde koşu kaydıyla ölçülür.
⑤ YERLEŞİM MESAFELERİ ÖLÇÜLMEDİ (§3.2). Yalnız dizilim mantığı indi.
```

> ⚠️ **VE EN ÖNEMLİSİ:** bu kılavuzdaki hiçbir oran üretimde sınanmadı.
> İlk istasyon/üs filmi yazıldığında ① KARE ve ② DEVAMLILIK skorları
> bu dosyanın sınavıdır — Ders 32'nin ölçtüğü oran kayması tekrar
> ederse çözüm §1 değildir ve kılavuz yeniden yazılır.
