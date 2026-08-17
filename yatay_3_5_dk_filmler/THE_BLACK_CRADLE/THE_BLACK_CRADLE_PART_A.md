# 🌑 THE BLACK CRADLE — Karanlıkta Yanaşma | PART A

## AI Production Bible — Self-Contained Prompts
### PART A: Sahne 0-12 (13 sahne) | 16:9 Yatay | Görsel + Video + Diyalog
### _"Işık onları kovaladı. Karanlık onları eve aldı."_

> **PART A süresi:** Hook (9s) + 12 sahne × 10s = 129 saniye
> **Toplam film:** 26 sahne = 259 saniye = 4 dakika 19 saniye
> (⚠️ 17.08: +S19b ara sahnesi PART_B'ye eklendi; S0-S14 değişmedi)
> **PART B:** `THE_BLACK_CRADLE_PART_B.md` (S13-S24)
> **Plan:** `THE_BLACK_CRADLE_PLAN.md` — QA SPEC, risk kartları, A4 kararları orada

---

## ⚠️ PART A ÜRETİM NOTLARI (promptlardan önce oku)

```
① İNSANSIZ SAHNELER (S7 · S8 · S9 · S12) — YAPISAL RED PROTOKOLÜ
   Cold Burn S8'de doğrulanan tetikleyici: insansız sahne + uzun
   NEGATIVE + "Exactly 0 human figures" kalıbı → "having a hard time"
   reddi. Bu dosyada azaltım BAŞTAN uygulandı: insansız sahnelerin
   NEGATIVE bloğu KISA tutuldu, boş kadraj POZİTİF anlatıldı ve insan
   sayısı imzası riskli "Exactly 0 human figures" kalıbı YERİNE
   "Human count in this frame: zero — both crew are inside the craft"
   biçiminde yazıldı (betik imzayı tanır). Buna rağmen yapısal
   red gelirse: KILAVUZ_REHBERI §7 merdiveni (NEGATIVE'i tek Style
   satırına indir → etiketleri kaldır → "human" kelimesini çıkar →
   3 satırlık prob → I2V).

② UZUNLUK BANDI — BİLİNÇLİ SAPMA GEREKÇESİ [Tall Shore / Slow Light
   §0.14b emsali] · prompt_kontrol 16.08.2026: 26 prompt · 0 BLOCK ·
   FIX yalnız uzunluk — 12 image bandın (1.700-2.100) üstünde (maks
   3.150), 12 video bandın (2.000-2.600) üstünde (maks 3.571); tavan
   (~4.300, Low Power doğrulaması) aşımı SIFIR. Sebep: iki karakterli
   sahnelerde iki kanonik çapa bloğu + kask cümleleri + D79 negatifi
   zorunlu (çapa kuralı kelime kelime kopya ister, kısaltılamaz).
   KAPATMA YOLU: bir sahne red alırsa O promptun NEGATIVE bloğu tek
   satır pozitif Style cümlesine indirilir (−600-800 karakter, bant
   içine iner) — KILAVUZ §7 merdiveni adım 1. İLK RED PROTOKOLÜ: önce
   HATA MESAJI sınıfına bak (§7 tablosu); aynı filmde 3 red / 0
   başarı görülürse kısaltma değil, 3 satırlık prob koşulur.

③ SİYAH-ÜSTÜ-SİYAH KAPISI
   Üretim S15'ten başlar (PART_B) ama PART A'nın kendi kapısı S7 ve
   S0'dır: kara ova DEAD MATTE çıkmazsa / lamba havuzları okunmazsa
   HAZIR DÜŞÜŞ (lander omurgasına iki ince beyaz konum şeridi ışığı)
   plandaki 🎨 bölümüne göre devreye girer.

④ KAPI KAYDI [D74]: S15 · S21 · S7 · S0 kapılarının her koşusu bu
   dosyanın sonuna TEK SATIR olarak yazılır. Kayıtsız kapı,
   koşulmamış kapıdır.

⑤ YÖN MIKNATISI [DERS 104 · 16.08.2026 · bu filmde bulundu]
   S4 üretim denemesinde koşucular landera değil ŞAFAĞA koştu —
   hedef-dilim + yön cümlesi yazılıyken. Sebep: kadrajın tek baskın
   ışığı yön mıknatısıdır ve GÖVDE YÖNELİMİ (omuz hattı) boş
   bırakılmıştı [İLKE 4: konum ≠ yönelim ≠ hareket]. Panzehir DÖRT
   KANAL birden ve bu dosyada yönlü her sahneye işlendi:
   ① hedef-dilim + yön aynı cümlede ② omuz hattı ekran yönüne dönük
   ③ IŞIĞA GÖRE POZ ("their backs are to the dawn — it rims their
   back silhouettes") ④ yön negatifi ("no one runs toward the light,
   no direction reversal"). Araç karşılığı: kıç önde sahnelerde
   "notched tail LEADS / canopy nose trails" + "never nose-first"
   (PART_B S15-S21 + fragman V3-V4'e işlendi). ⚠️ prompt_kontrol bu
   sınıfı GÖREMEZ (yönelim eksenini aramaz) — üretim öncesi insan
   gözüyle denetlenir.
   ⭐ İKİNCİ RED SONRASI KAÇIŞ BASAMAĞI (aynı gün): dört kanal da
   yanal koşuda yetmedi — model frontal refleksle gemiyi arkaya atıp
   koşucuları kameraya döndürdü. Çözüm refleksle hizalanmaktır:
   S4 V3'te kamera LANDERİN YANINDA durur, kameraya koşu = gemiye
   koşu (nötr çekim, dizide tek). Yanal koşu bu filmde artık hiçbir
   sahnede istenmez.
```

---

# 📖 BÖLÜM 1 — THE BIBLES

---

## 🌑 WORLD BIBLE — KARA GEZEGEN "KÖMÜR"

```
YÜZEY: Ufka kadar asfalt karası bazalt ovası, üstünde grafit tozu
kabuğu. Alçak basınç sırtları (1-3 m). Albedo ~%1 — yüzey DEAD
MATTE'tır: parlamaz, yansıtmaz, ışığı yutar. Doku YALNIZ yapay ışık
havuzlarının içinde okunur.

ATMOSFER: İnce azot-CO₂, Dünya basıncının %3'ü. Anlamı: - RÜZGAR
HİÇBİR ŞEYİ DEVİRMEZ; kumaş çırpmaz. - Kalkan toz 2-3 saniyede yüzeye
GERİ OTURUR. - SES BOĞUK VE ALÇAKTIR; yüksek frekans taşınmaz. -
GÖKYÜZÜ gece neredeyse siyah, keskin yıldızlar; ufuktaki şafak
kuşağında soluk menekşe.

ŞAFAK HATTI: Gezegen yavaş döner; gündüz-gece sınırı (terminatör)
yüzeyde 7 m/s ile YÜRÜR. Ufukta ince altın-beyaz YANAN DİKİŞ + üstünde
büyüyen ışık seti: S0'da 2° → S2'de 4° → S3'te 5° → S4'te 8° → S6-S7'de
10°. Tehdit kuvvet değil: gündüz yüzü +240°C — ışık geldiği yeri
kavurur, kalkış penceresini kapatır. Set yüksekliği filmin metinsiz
geri sayım kanalıdır.

YERÇEKİMİ (YÜZEY): 0.8g. Adımlar temaslı ve ağırlıklı, koşu gerçek
koşu. GERÇEK ZAMAN [Ders 44]: insan temposu Dünya'yla aynı; ağır çekim
YOK — her yüzey promptunda "real time, ordinary Earth pace" yazılır.

SICAKLIK: Gece yüzü -90°C. Kask kapalı; nefes buharı dışarıda yok.

IŞIK BÜTÇESİ (yüzey): TAM 5 yapay kaynak — 2 kask lambası + 2 göğüs
lambası + 1 karın projektörü (lander). Başka ışık YOK; ay yok, şehir
parıltısı yok. Havuzların dışı GERÇEKTEN siyahtır.

YÖRÜNGE: Saf siyah uzay, keskin sabit yıldızlar. Aşağıda gezegen:
kömür karası, ancak SEÇİLEBİLEN bir kavis + terminatör boyunca ince
parlak dikiş (ince atmosferin saçtığı şafak ışığı). ⭐ ALBEDO DOLGUSU
YOK: kara gezegen ışık geri vermez — gölge tarafları MUTLAK siyah,
ayrımı yalnız sert güneşin kenar ışığı (rim) yapar. VAKUM: dışarıda
ses SIFIR, pus yok, lens parlaması yok (küresel lens).

YERÇEKİMİ (YÖRÜNGE): 0g. Kayışlı bedenler koltuğa kilitli; serbest
nesne düz hatta süzülür, momentumunu korur; "yüzme" yok.
```

---

## ⚓ ÇAPA BLOKLARI — KANONİK İNGİLİZCE TANIMLAR

```
⚓ KANONİK ÇAPA BLOKLARI [SAHNE_DEVAMLILIK §2.1] Aşağıdaki bloklar
KANONİKTİR: varlık hangi promptta görünüyorsa oraya KELİMESİ KELİMESİNE
kopyalanmıştır — eşanlamlı bile yasak. Sahneye özgü durum (koşu, hasar,
uçuş konfigürasyonu) bloktan SONRA ayrı cümleyle eklenir; blok değişmez.

PILOT: the pilot — woman, mid-thirties, 1.70 m, wiry, pale cool-toned
skin with visible pores, grey eyes, sharp thin nose, an old thin burn
scar at her right temple, platinum-blond hair in a near-shaved crop;
matte charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use

ENGINEER: the engineer — man, around fifty, 1.84 m, lean and rangy,
warm tan skin with visible pores, hooded dark eyes, silver-streaked
close-cropped hair, clean-shaven, two deep creases across his brow;
same matte charcoal-black hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use

KASK CÜMLESİ (kasklı sahnelerde bloğun hemen ardına): low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
[her/his] face fully visible through it
(Kasksız tek sahne S23 PART_B'dedir: BARE-HEADED.)

LANDER — TAM BLOK (araç ÖZNE olduğu sahnelerde: S7 · S9 · S12 ·
PART_B'de S15-S22 dışları): the lander — an 8-meter angular
LIFTING-BODY craft, no plain cylinder: broad flat belly, sharp chine
lines running nose to tail, a low blended forward canopy, two short
swept strakes, twin main engines recessed in a notched tail, four
downward LIFT NOZZLES under the belly, four landing legs that fold up
into flush belly wells, two recessed thruster quads at the bow and two
at the stern, a 40-cm round aft observation port above the engine
notch, and two docking rails along the aft flanks; satin machined-black
composite panels with crisp recessed seams over a graphite-grey
structural spine, one thin SIGNAL-WHITE chevron line down each flank,
and a side hatch

LANDER — ZEMİN SÜRÜMÜ (S0-S4; araç 30-300 m uzakta, kadrajın öznesi
değil — tam bloğun ALT KÜMESİDİR, çelişen kelime içermez): the lander —
the same 8-meter angular lifting-body craft, satin machined black with
one thin SIGNAL-WHITE chevron line down each flank, standing level on
four landing legs, its single belly floodlight cutting a hard-edged
pool of white light onto the black ground

LANDER — UÇUŞ SÜRÜMÜ (S8; araç uzak ve uçuşta): the lander — the same
8-meter angular lifting-body craft in FLIGHT CONFIGURATION, all four
landing legs folded away into flush belly wells, its belly line clean,
satin machined black with one thin SIGNAL-WHITE chevron line down each
flank

MAIN SHIP — UZAK SÜRÜM (S10 · S11; gemi kilometrelerce uzakta):
the main ship — a 120-metre interstellar transfer vessel still
kilometres away, reading as a long black silhouette that blots out the
stars behind it, one full edge traced in hard sunlight, a few thin
white position lines spaced along its length; it does not rotate and
shows no lit windows
(TAM BLOK — rıhtım geometrisiyle birlikte — PART_B'de tanımlanır ve
S13'ten itibaren kullanılır.)

KARA ZEMİN KİLİDİ (her yüzey promptuna): The plain is light-swallowing
coal-black basalt under a skin of graphite dust, DEAD MATTE — no gloss,
no glint, no mirror reflection, never glowing; its texture reads only
inside the pools of artificial light.

IŞIK BÜTÇESİ CÜMLESİ (her yüzey promptuna): Exactly five artificial
light sources exist in this world: two helmet lamps, two chest lamps,
and the lander's single belly floodlight.

BACAK DURUMU [Cold Burn dördüncü tur dersi]: İniş bacakları YALNIZ
S0-S7 (kalkışın ilk 4,5 saniyesi dahil) açıktır. S7'nin 4,5.
saniyesinden film sonuna kadar: bacaklar KATLI, kapaklar kapalı, karın
hattı düz — kalkış sonrası araç görünen HER promptta "in FLIGHT
CONFIGURATION … no landing leg, no leg well and no open gear door is
visible" gövdede yazılır.

DOĞRULAMA (PART A blok sayımı): PILOT tam blok 16 · ENGINEER tam blok
16 · KASK cümlesi 16 (+S0'da kısa "helmets closed") · LANDER zemin 10 ·
LANDER tam 6 · LANDER uçuş 2 · MAIN SHIP uzak 4 · D79 negatif çifti 18
(insan görünen 9 sahnenin 18 promptu — film toplamı 28'in Part A payı).
```

---

## 🚀 SHIP BIBLE — GECE KUŞU (lander) & LİMAN (ana gemi)

```
LANDER ("the lander"): 8 m AÇILI KALDIRMA GÖVDESİ — düz silindir
DEĞİL, gövde YATAY durur. Geniş düz karın, burun-kuyruk keskin CHINE
hatları, alçak kaynaşık kanopi, iki kısa strake, kuyruk çentiğinde İKİ
ana motor, karın altında DÖRT kaldırma lülesi, karın yuvalarına
katlanan DÖRT iniş bacağı. SATEN İŞLENMİŞ SİYAH kompozit paneller —
gezegen gibi ölü mat DEĞİL: ince gömme derz dokusu ve kenar ışığı
tutan hafif saten (üç siyahın ayrışması: Lighting Bible). Her yanda
tek İNCE SİNYAL BEYAZI şevron çizgisi. Yan kapak.

İTİCİLER: Burunda İKİ gömme itici kümesi (S8'deki ısıl şoktan sonra
ÖLÜ — S9'dan itibaren hiçbir promptta burun jeti ateşlemez), kıçta İKİ
küme (çalışır): kısa DÜZ cold-gas jetleri, 1 saniyede seyrelir.

KIÇ: Motor çentiğinin üstünde, eksende, 40 cm'lik yuvarlak KUYRUK
GÖZLEM LOMBOZU (mühendisin gözü — PART_B). Kıç yanlarında rıhtım
kelepçelerine oturan İKİ gövde rayı.

KALKIŞ SIRASI (Cold Burn'de kanıtlanan dört adım — hiçbir promptta
değişmez):
① dört karın lülesi ateşler (araç hâlâ ayakta)
② araç düz seviyede yükselir
③ 20 m'de (S7'de 4,5 s) dört bacak yuvalara katlanır, kapaklar kapanır
④ kuyruktaki iki ana motor yanar, kaldırma kesilir, burnu ileride
  hızlanır
⛔ Kuyruk motoru asla yere doğru ateşlemez; dikleşme yok.

KABİN: 2.2 m genişlik, iki koltuk YAN YANA (solda pilot, sağda
mühendis). Panel: analog ağırlıklı — soyut amber/turkuaz IŞIK
SEGMENTLERİ (doluluk gösterir, metin/rakam ASLA), ortada 12 cm'lik
MEKANİK DURUŞ KÜRESİ. Tek geniş ön cam (1.4 × 0.5 m). Arka perdede
kuyruk lombozuna giden dar geçit + tutunma rayı (PART_B'de kullanılır).
YAKIT REZERV GÖSTERGESİ: 8 soyut amber segment (her biri %2); sönmüş
segmentin YUVASI görünür kalır [Ders 78 ①]. PART A'da gösterge
KADRAJA ALINMAZ (ilk okunuşu S16 — planlı sayılar: S16 2 yanık = %4,
S18 1 yanık = %2; plansız ara değer üretmemek için).

ANA GEMİ ("the main ship"): 120 m YILDIZLARARASI transfer gemisi —
lander'ın TAM 15 KATI. Saten siyah gövde, seyrek ince beyaz konum
çizgileri. Burun sensör kubbesi · koyu antrasit kapitoneli ALTI yaşam
modülü (üç tandem çift) · açık altıgen kafes omurga · omurga ortasında
AÇIK KIZAK RIHTIMI (10 × 4 × 3 m yuva · 2 kızak kolu · 4 açık kelepçe ·
ağzında 1 m tabanlı ÜÇ AMBER kılavuz ışığı) · iki koyu gri bıçak sırtı
radyatör kanadı · kıçta füzyon bloğu, dört gömük lüle. DÖNMEZ; modül
pencereleri S23'e kadar KARANLIK. PART A'da yalnız UZAK SÜRÜM görünür;
rıhtım geometrisi PART_B'de kadraja girer.

ÖLÇEK KİLİDİ: lander 8 m · ana gemi 120 m (15×) · rıhtım yuvası
10 × 4 × 3 m · yuva payı 50 cm · kelepçe 4 · kılavuz ışığı 3 · kuyruk
lombozu 40 cm · kabin 2.2 m · ön cam 1.4 × 0.5 m · karot 40 cm ·
pilot 1.70 m · mühendis 1.84 m. Tüm sahnelerde birebir korunur.
ORAN CÜMLESİ: ikisi aynı karedeyse yazılır — "the lander is
one-fifteenth of its length — a moth backing toward a cathedral."
```

---

## 👤 CHARACTER BIBLE — PİLOT & MÜHENDİS & MİRA

```
⚠️ PROMPT KURALI: Özel ad promptlara YAZILMAZ (Ders 34) — "the pilot"
/ "the engineer". Milliyet ifadesi YASAK.

PİLOT ("the pilot"): Kadın, 35, 1.70 m, sırım. Soluk soğuk ten,
görünür gözenek. Gri gözler, keskin ince burun, SAĞ ŞAKAKTA eski ince
yanık izi. PLATİN SARISI, neredeyse kazınmış çok kısa saç. Makyaj yok.
SUIT: mat kömür siyahı sert kabuk — segmentli göğüs/omuz plakaları,
grafit esnek-örgü eklemler, işlenmiş eklem halkaları, omuz ve ön
kollarda İNCE KAKMA TURKUAZ ÇİZGİ, ince çizikli. Düşük profilli SİYAH
kask, tek parça optik berrak panoramik vizör, sırt DÜZ.

MÜHENDİS ("the engineer"): Erkek, 50, 1.84 m, kuru-uzun. Sıcak buğday
ten, görünür gözenek. Çekik koyu gözler, gümüş çalıklı çok kısa saç,
SAKALSIZ, alında iki derin çizgi. SUIT: aynı sert kabuk, İNCE KAKMA
AMBER ÇİZGİ aksanları, ince çizikli. Aynı siyah kask, berrak vizör,
sırt DÜZ.

AYIRT EDİCİLİK KİLİDİ: TURKUAZ çizgi = pilot · AMBER çizgi = mühendis
· 1.70 ↔ 1.84 boy farkı · koşuda pilot önde eli boş, mühendis KAROT
KUTUSU taşır. İki karakterli her prompta bu satırlar yazılır.

HUMAN COUNT LOCK: Filmde TAM 2 insan. Her promptta karede görünen sayı
(0 / 1 / 2) açıkça yazılır. Üçüncü figür, kopya, yansımada fazladan
yüz, arka planda siluet YOK.

HELMET STATE SCHEDULE: İnsan görünen 14 sahnenin 13'ünde kask KAPALI;
kasksız tek sahne S23 (PART_B, basınçlı güverte). PART A'da kasksız
sahne YOKTUR; ara durum YOKTUR.

SIRT VE VİZÖR KİLİDİ [DERS 79 · zorunlu]: Sırt ünitesi YOK — sırt
silueti DÜZ. Vizör optik berrak: renklendirme, aynalama, ÇEVRE
YANSIMASI sıfır; yüz her karede okunur. ⚠️ Bu iki cümle bible'da
BIRAKILMAZ — insan görünen 28 promptun 28'inde negatif bloğun İÇİNDE
yazılıdır (bu dosyada 18'i).

MİRA (AI — "a calm neutral synthetic voice"): GÖVDESİZ. Ekranı,
avatarı, yüzü, robotu YOK. Kabin hoparlöründen/telsizden sakin nötr
sentetik ses. Asla görselleşmez. ⭐ D82 SİGORTASI: SAYI söyleyen her
replik MİRA'nındır; üretimde bir insana devredilemez.
```

---

## 🎥 CAMERA BIBLE

```
KURAL: 25/25 sahne SABİT LOCKOFF. Pan yok, tilt yok, zoom yok, track
yok, kesme yok. Her sahne = tek kesintisiz çekim = ayrı video.

LENS KİLİDİ (küresel/spherical — anamorfik yatay parlama YASAK):
- HOOK havadan                     → 24mm
- DIŞ GENİŞ (yüzey, yörünge)       → 32mm
- KABİN (arkadan/yandan, koltuklar)→ 35mm
- DETAY (burun kümeleri, panel)    → 85mm

MESAFE: her prompt kamera mesafesini metre cinsinden yazar.

KOKPİT DİYALOG KURALI: konuşmalı kokpit sahneleri (S6 · S10 · S11)
İKİ KOLTUĞUN ARKASINDAN çekilir — ağızlar kadrajda değildir, replikler
telsiz sesidir. S2 dış diyalog sahnesinde konuşan MİRA'dır (gövdesiz);
S9'da kadrajda hiç insan yoktur — replik saf telsiz sesi (depodaki en
güvenli diyalog biçimi).

EKRAN YÖNÜ KİLİDİ [UZAMSAL kılavuz]: Yüzeyde şafak dikişi DAİMA kadraj
SOLUNDA (arka plan), lander SAĞDA; kaçış hareketi SOLDAN SAĞA; gölgeler
SAĞA uzar. Yön hiçbir yüzey sahnesinde terslenmez.

SÜRE: Sahne başına 10 saniye (Hook = 9). ⚠️ Veo 3.1 native 8s üretir:
8s üret + 2s extend uygula.
```

---

## 💡 LIGHTING BIBLE — ÜÇ SİYAHIN AYRIŞMASI

```
⭐ FİLMİN ASIL İŞİ BU TABLODUR. Üç siyah, DOKUYLA ayrışır ve ilgili
cümleler promptların gövdesinde yazılıdır:
  GEZEGEN  → DEAD MATTE: ışık yutan; doku yalnız ışık havuzu içinde
  GÖVDELER → SATEN SİYAH: ince derzler; kenar ışığını (rim) tutar
  SUITLER  → MAT PLAKA + ÖRGÜ: iki malzeme dokusu + renkli çizgiler

AİLE 1 — GECE YÜZEYİ (S0-S6): TAM 5 yapay kaynak (2 kask + 2 göğüs
lambası + karın projektörü) — sert kenarlı beyaz havuzlar. Ufukta
şafak seti: 2°→10° büyüyen altın-beyaz kuşak; S3'ten itibaren sıyırıcı
sıcak kenar ışığı verir, gölgeler SAĞA uzar. Havuzların ve setin
dışında kalan her şey GERÇEKTEN siyah.

AİLE 2 — KALKIŞ (S7): Tek ışık olayı: dört lüle + kuyruk motorlarının
mavi-beyaz jet ışığı kara ovanın dokusunu İLK KEZ 30 m yarıçapında
ortaya çıkarır; jetler kesilince ova yeniden siyaha düşer.

AİLE 3 — YÖRÜNGE DIŞ (S8-S12): VAKUM IŞIĞI. Tek kaynak sert güneş —
kadraj SOLUNDAN. Jilet gölge. ⭐ ALBEDO DOLGUSU YOK: gölge tarafı
MUTLAK siyah; gövdeyi yalnız rim + beyaz şevron + yıldız örtme silueti
okutur. Pus yok, halo yok, parlama yok.

AİLE 4 — KABİN (S5-S6 · S10-S11): loş; soyut amber/turkuaz segmentler,
duruş küresinin arkadan soluk amber ışığı, camdan giren şafak/yıldız
alanı. VİZÖRDE ÇEVRE YANSIMASI YOK [D79].

ANTİ-BLOOM: "glowing/ethereal/radiant/shimmering" YASAK. Işık kaynağı
her zaman net ve fiziksel ("the seam of dawn light on the horizon",
"hard sunlight from frame left").
```

---

## ⚙️ PHYSICS BIBLE

```
YÜZEY (0.8g · %3 atmosfer): - Koşu gerçek koşu: temaslı, ağırlıklı.
Süzülme yok. - Kalkan grafit tozu düşer, 2-3 saniyede OTURUR; asılı
perde yok. - Rüzgar kumaş çırpmaz, kimseyi itmez. - Ses alçak, tok,
boğuk. - GERÇEK ZAMAN [Ders 44]: her yüzey promptunda "real time,
ordinary Earth pace". - KALKIŞ (VTOL, S7): dört karın lülesi düz
AŞAĞI; dört ayrı jet = dört ayrı toz halkası, balistik yay çizip
oturur. Sıra: motorlar → yükselme → bacak katlanması (4,5 s / 20 m) →
kuyruk motorları. Dikleşme YOK.

ŞAFAK HATTI: 7 m/s ile yürür; ışık seti sahne başına planlı yükseklikte
(2°→10°). Işık kuvvet uygulamaz — tehdit ısı ve pencere.

YÖRÜNGE (0g · vakum): - DIŞARIDA SES SIFIR. - İticiler: kısa DÜZ
cold-gas jetleri, 1 saniyede seyrelir; burun kümeleri S9'dan itibaren
ÖLÜ (hiç ateşlemez). - Serbest parça momentumunu korur: düz hat, sabit
hız. - Dönüş (S12): kıç kümelerinin darbeleriyle sabit hızda yaw;
karşı darbeyle durur. Yıldızlar her zaman KESKİN NOKTA — gerçek
zamanlı çekimde iz/yay oluşmaz. - Temas/eldiven: net yapısal sınır,
erime yok, iç içe geçme yok.
```

---

## 🚫 NEGATIVE BIBLE (çekirdek — sahneye göre uyarlanır)

```
İNSANLI SAHNE ÇEKİRDEĞİ: Single unbroken take, fixed locked-off camera
— no cuts, no transitions, no pans, no zoom, no camera movement of any
kind. Exactly [N] human figures in this frame (this film has exactly
two humans total) — no extra crew, no duplicates, no clones, no
background figures, no extra faces in reflections. Thin teal lines =
the pilot, thin amber lines = the engineer — the two are never
identical. 0% bloom, no glow filter, no soft focus — every surface
keeps visible texture. Photorealistic skin with pores — no airbrushing,
no waxy texture, no face morphing, identical bone structure throughout.
The suits have NO back-mounted unit: no backpack, no tank, no hose, no
cable, no rear housing of any kind — both back silhouettes are flat.
Each visor is optically clear glass with zero tint, zero mirror coating
and zero reflection of the environment; the face behind it is fully
readable in every frame, at every head angle. Suits and gear identical
to the description — no drift, nothing appears or disappears mid-shot.
The ground is DEAD MATTE light-swallowing black — no gloss, no glint,
no mirror reflection, never glowing. No readable text, letters, digits
or symbols on any panel, display, patch or hull — abstract light
segments only. No subtitles, no captions, no title card, no watermark.
All hand-surface contacts keep a clear structural boundary — no
merging, no phasing, no extra fingers. All particles obey the stated
gravity with continuous physical momentum — never hovering, never
frozen, never swirling or flowing like liquid. Terrain and hulls static
and stable — no melting, no warping, no swimming texture. No Unreal
Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic
with 35mm film grain.

İNSANSIZ SAHNE ÇEKİRDEĞİ (kısa — yapısal red azaltımı, üretim notu ①):
Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Human count in this frame: zero — both crew are inside the
craft. 0% bloom, no glow filter, no soft focus — every surface keeps
texture. Black surfaces stay DEAD MATTE (ground) or satin machined
(hulls) — never glossy, never mirror-like, never glowing. No readable
text anywhere. No subtitles, no title card, no watermark. All particles
obey the stated gravity with continuous momentum — never hovering,
never swirling. Terrain and hulls static — no melting, no warping. No
Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film
grain.

DİYALOGLU SAHNEDE EK: The spoken lines are heard only — never shown as
text. No subtitles, no captions, no transcript. One speaker at a time.
All human voices come over the suit radio channel; no mouth is readable
in frame. The synthetic voice is off-screen only — it has no body, no
face, no avatar, and no third figure ever appears.
```

---

# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART A: S0-S12)

> ⚡ **Her prompt tamamen bağımsızdır.** Bible'lara bakmanıza gerek yok.
> Sadece istediğiniz sahnenin 📸 veya 🎥 bloğunu kopyalayıp yapıştırın.

---

## 🎬 SAHNE 0 (S0) — HOOK: KÖMÜR (9 saniye)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. High aerial
night view of a pitch-black planet's surface. Exactly 2 human figures
in frame, tiny with distance, helmets closed.

SCENE: An endless coal-black basalt plain seen from 300 meters up,
angled 30 degrees down. The plain is light-swallowing coal-black basalt
under a skin of graphite dust, DEAD MATTE — no gloss, no glint, no
mirror reflection, never glowing; its texture reads only inside the
pools of artificial light. Near frame center stand two tiny suited
figures, each inside the small hard-edged white pool of its own helmet
and chest lamps, working over a core drill. Forty meters from them at screen-right: the lander — the same 8-meter angular lifting-body craft, satin
machined black with one thin SIGNAL-WHITE chevron line down each
flank, standing level on four landing legs, its single belly floodlight
cutting a hard-edged pool of white light onto the black ground. Along
the LEFT horizon runs a razor-thin burning seam of gold-white light,
with a band of scattered dawn light two degrees tall above it — the only feature of
this entire world.

ENVIRONMENT: Night side of a slow-rotating carbon planet. Thin
nitrogen-CO2 atmosphere, 3% of Earth pressure. Near-black sky with
sharp stars, faint violet only above the burning seam. -90°C. Gravity
0.8g. Exactly five artificial light sources exist in this world: two
helmet lamps, two chest lamps, and the lander's single belly
floodlight.

CAMERA & LIGHT: 24mm spherical lens, fixed high aerial position 300
meters above the plain. No moonlight, no ambient fill — the darkness
between the light pools is genuinely black.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human
figures — no others anywhere. Both suits have NO back-mounted unit —
back silhouettes flat; visors optically clear, zero mirror coating.
0% bloom, no glow filter, no soft focus. The ground is DEAD MATTE —
no gloss, no glint, never glowing. No readable text anywhere. No
subtitles, no title card, no watermark. Terrain static — no melting,
no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic
with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
9-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off aerial camera, no camera movement. Exactly 2 human figures
in frame, tiny with distance, helmets closed.

SCENE: An endless coal-black basalt plain from 300 meters up, angled
30 degrees down. The plain is light-swallowing coal-black basalt under
a skin of graphite dust, DEAD MATTE — no gloss, no glint, never
glowing; its texture reads only inside the pools of artificial light.
Near frame center, two tiny suited figures work over a core drill,
each inside the hard white pool of its own helmet and chest lamps.
Forty meters from them at screen-right: the lander — the same 8-meter angular
lifting-body craft, satin machined black with one thin SIGNAL-WHITE
chevron line down each flank, standing level on four landing legs, its
single belly floodlight cutting a hard-edged pool of white light onto
the black ground. Along the LEFT horizon: a razor-thin burning seam of
gold-white light, a band of scattered dawn light two degrees tall above it. Exactly
five artificial light sources exist in this world: two helmet lamps,
two chest lamps, and the lander's single belly floodlight.

TIMELINE:
0.0s — Stillness. Three pools of light in an ocean of black; sharp
stars above.
3.0s — One tiny figure kneels; its lamp pool shortens. The other
stands motionless.
6.0s — The seam on the left horizon brightens almost imperceptibly,
its glow pressing one ridge crest into faint silhouette.
9.0s — Nothing else has moved. Hold on the last frame.

AUDIO: A deep, muffled planetary ground-tone, low and sparse; thin
airy hiss. No high frequencies — the atmosphere is too thin to carry
them. No voice, no music.

PHYSICS: Gravity 0.8g, thin 3% atmosphere: nothing flutters, nothing
drifts. Real time, ordinary Earth pace.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no others. Both back
silhouettes flat — no back-mounted unit; visors optically clear, zero
mirror coating. 0% bloom, no glow filter, no soft focus. The ground is
DEAD MATTE — no gloss, no glint, never glowing. No readable text
anywhere. No subtitles, no title card, no watermark. Particles obey
0.8g with continuous momentum — never hovering, never swirling.
Terrain static — no melting, no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 1 (S1) — KAROT

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a pitch-black planet, lamplight only. Exactly 2 human
figures in frame — this film has exactly two humans total.

SCENE: Two astronauts work over a core drill inside overlapping pools
of hard white lamplight. Kneeling: the engineer — man, around fifty,
1.84 m, lean and rangy, warm tan skin with visible pores, hooded dark
eyes, silver-streaked close-cropped hair, clean-shaven, two deep
creases across his brow; same matte charcoal-black hard-shell suit,
dark graphite flex-weave joints, machined articulation rings, thin
inlaid AMBER accent lines on the shoulder plates and forearms, finely
scuffed with use; low-profile black helmet CLOSED with one seamless
optically clear panoramic visor, his face fully visible through it. He
draws a 40-cm core of coal-black rock from the drill sleeve — dead
matte black crossed by hairline bright mineral seams. Standing beside
him: the pilot — woman, mid-thirties, 1.70 m, wiry, pale cool-toned
skin with visible pores, grey eyes, sharp thin nose, an old thin burn
scar at her right temple, platinum-blond hair in a near-shaved crop;
matte charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
her face fully visible through it. She holds an open slim matte-black
sample case. Thirty meters behind them: the lander — the same 8-meter
angular lifting-body craft, satin machined black with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool of
white light onto the black ground. Far frame left on the horizon: a
thin gold-white seam of light. The plain is light-swallowing
coal-black basalt under a skin of graphite dust, DEAD MATTE — its
texture reads only inside the pools of artificial light.

CAMERA & LIGHT: 35mm spherical lens, fixed 8 meters from the pair at
chest height. Exactly five artificial light sources exist in this
world: two helmet lamps, two chest lamps, and the lander's belly
floodlight. Faces lit by lamp spill through clear visors. -90°C,
gravity 0.8g, thin 3% atmosphere.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures, no extra faces in
reflections. Teal lines = pilot, amber lines = engineer — never
identical. The suits have NO back-mounted unit — both back silhouettes are flat. Each visor is
optically clear glass with zero tint, zero mirror coating and zero
reflection of the environment; the face behind it is fully readable.
0% bloom, no soft focus. Photorealistic skin with pores — no
airbrushing, no face morphing. The ground is DEAD MATTE — no gloss, no
glint, never glowing. No readable text anywhere. No subtitles, no
watermark. Hand-object contacts keep clear structural boundaries — no
merging, no extra fingers. Particles obey 0.8g — never hovering.
Terrain static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame — this film has exactly two humans total.

CHARACTERS: The engineer — man, around fifty, 1.84 m, lean and rangy,
warm tan skin with visible pores, hooded dark eyes, silver-streaked
close-cropped hair, clean-shaven, two deep creases across his brow;
same matte charcoal-black hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
his face fully visible through it. The pilot — woman, mid-thirties,
1.70 m, wiry, pale cool-toned skin with visible pores, grey eyes,
sharp thin nose, an old thin burn scar at her right temple,
platinum-blond hair in a near-shaved crop; matte charcoal-black
hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid TEAL accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile black helmet
CLOSED with one seamless optically clear panoramic visor, her face
fully visible through it. Teal = pilot, amber = engineer — never
identical, never duplicated.

SCENE: Night surface, lamplight only. Overlapping hard white pools
from their helmet and chest lamps; 30 meters behind them the lander —
the same 8-meter angular lifting-body craft, satin machined black with
one thin SIGNAL-WHITE chevron line down each flank, standing level on
four landing legs, its single belly floodlight cutting a hard-edged
pool of white light onto the black ground. Thin gold-white seam far
frame left. The plain is DEAD MATTE coal-black basalt under graphite
dust — texture only inside the light pools. Camera fixed 8 meters
away, 35mm spherical lens, chest height.

TIMELINE:
0.0s — The engineer, kneeling, draws the 40-cm coal-black core from
the drill sleeve with both gloved hands — careful, weighted, ordinary
Earth pace.
3.5s — He tilts it once through his lamp beam; hairline bright mineral
seams flash across the dead-matte black.
6.0s — The pilot crouches, opens the slim matte-black sample case; he
seats the core into its cradle with a firm contact — clear structural
boundary.
8.5s — She closes the lid. A puff of graphite dust from her boot falls
and settles within 2 seconds.

AUDIO: Muffled low sounds only: drill sleeve scrape carried dull
through the ground, twin suit-fan hums on the radio channel, thin airy
hiss. No voices, no music.

PHYSICS: Gravity 0.8g — grounded, weighted movement, real time,
ordinary Earth pace, no slow motion. Thin air: nothing flutters. All
lifted dust falls and settles within 2-3 seconds.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures, no extra faces in reflections. The suits have NO back-mounted unit — both back silhouettes are flat. Each visor is optically clear glass with
zero tint, zero mirror coating and zero reflection of the environment.
0% bloom, no soft focus — every surface keeps texture. Photorealistic
skin with pores — no airbrushing, no face morphing. The ground is DEAD
MATTE — no gloss, no glint, never glowing. No readable text anywhere.
No subtitles, no watermark. Hand contacts keep clear structural
boundaries — no merging, no extra fingers. Particles obey 0.8g — never
hovering, never swirling. Terrain static. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 2 (S2) — UYARI

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a pitch-black planet. Exactly 2 human figures in frame —
this film has exactly two humans total.

SCENE: Two astronauts have frozen mid-task, both faces turned toward
the LEFT horizon. There, the burning gold-white seam has grown: a band of
scattered dawn light now four degrees tall stands above it, and its light
skims the plain for the first time, edging the crests of low pressure
ridges while every trough stays pure black. Standing, nearer camera:
the pilot — woman, mid-thirties, 1.70 m, wiry, pale cool-toned skin
with visible pores, grey eyes, sharp thin nose, an old thin burn scar
at her right temple, platinum-blond hair in a near-shaved crop; matte
charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
her face fully visible through it. A step behind her, half-risen from
a kneel: the engineer — man, around fifty, 1.84 m, lean and rangy,
warm tan skin with visible pores, hooded dark eyes, silver-streaked
close-cropped hair, clean-shaven, two deep creases across his brow;
same matte charcoal-black hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
his face fully visible through it. Thirty meters behind them, frame
right: the lander — the same 8-meter angular lifting-body craft, satin
machined black with one thin SIGNAL-WHITE chevron line down each
flank, standing level on four landing legs, its single belly
floodlight cutting a hard-edged pool of white light onto the black
ground. The plain is DEAD MATTE coal-black basalt under graphite dust.

CAMERA & LIGHT: 32mm spherical lens, fixed 10 meters from the pair at
chest height, horizon seam visible frame left. Exactly five artificial
light sources: two helmet lamps, two chest lamps, the belly
floodlight — plus the distant seam's faint warm skim. Gravity 0.8g.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures, no extra faces in
reflections. Teal lines = pilot, amber lines = engineer — never
identical. The suits have NO back-mounted unit — both back silhouettes
are flat. Each visor is optically clear glass with zero tint, zero
mirror coating and zero reflection of the environment. 0% bloom, no
soft focus. Photorealistic skin with pores — no airbrushing. The
ground is DEAD MATTE — no gloss, no glint, never glowing. No readable
text anywhere. No subtitles, no watermark. Particles obey 0.8g.
Terrain static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame — this film has exactly two humans total. One synthetic voice
speaks; no human speaks.

CHARACTERS: The pilot — woman, mid-thirties, 1.70 m, wiry, pale
cool-toned skin with visible pores, grey eyes, sharp thin nose, an old
thin burn scar at her right temple, platinum-blond hair in a
near-shaved crop; matte charcoal-black hard-shell suit, dark graphite
flex-weave joints, machined articulation rings, thin inlaid TEAL
accent lines on the shoulder plates and forearms, finely scuffed with
use; low-profile black helmet CLOSED with one seamless optically clear
panoramic visor, her face fully visible through it. The engineer —
man, around fifty, 1.84 m, lean and rangy, warm tan skin with visible
pores, hooded dark eyes, silver-streaked close-cropped hair,
clean-shaven, two deep creases across his brow; same matte
charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid AMBER accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
his face fully visible through it. Teal = pilot, amber = engineer —
never identical, never duplicated.

SCENE: Night surface, lamp pools; 30 meters behind them frame right
the lander — the same 8-meter angular lifting-body craft, satin
machined black with one thin SIGNAL-WHITE chevron line down each
flank, standing level on four landing legs, its single belly
floodlight cutting a hard-edged pool of white light onto the black
ground. On the LEFT horizon the gold-white seam with a band of
scattered dawn light four degrees tall; its warm light skims the ridge crests. The plain is
DEAD MATTE coal-black basalt. Camera fixed 10 meters away, 32mm
spherical lens, chest height.

TIMELINE:
0.0s — Both work over the drill site, unhurried, ordinary Earth pace.
2.5s — A calm neutral synthetic voice over the radio, level and
unhurried, in Turkish: "Şafak hattı bin iki yüz metrede. Pencere üç
dakika."
5.0s — Both freeze. The pilot's helmet turns LEFT toward the horizon;
one second later the engineer's follows.
8.0s — Neither moves. The seam's glow presses one more ridge crest
into silhouette. Hold.

AUDIO: Muffled low world-tone; twin suit-fan hums and slow breathing
on the radio channel. The synthetic voice at 2.5s is the only speech —
heard only, never shown as text.

PHYSICS: Gravity 0.8g, real time, ordinary Earth pace. Thin air:
nothing flutters. The distant light advances but exerts no force.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures. The suits have NO back-mounted unit — both back
silhouettes are flat. Each visor is optically clear glass with zero
tint, zero mirror coating and zero reflection of the environment. 0%
bloom, no soft focus. The ground is DEAD MATTE — no gloss, no glint,
never glowing. No readable text anywhere. The spoken line is heard
only — no subtitles, no captions, no transcript. One speaker; the
synthetic voice is off-screen only — no body, no avatar, no third
figure. No mouth is readable in frame. Particles obey 0.8g. Terrain
static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 3 (S3) — TOPLAMA

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a pitch-black planet, dawn glow rising. Exactly 2 human
figures in frame — this film has exactly two humans total.

SCENE: Hurried, disciplined packing. In the foreground, kneeling over
the slim matte-black sample case and snapping its latches shut: the
engineer — man, around fifty, 1.84 m, lean and rangy, warm tan skin
with visible pores, hooded dark eyes, silver-streaked close-cropped
hair, clean-shaven, two deep creases across his brow; same matte
charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid AMBER accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
his face fully visible through it. Behind him, collapsing the core
drill into a short black tube: the pilot — woman, mid-thirties, 1.70
m, wiry, pale cool-toned skin with visible pores, grey eyes, sharp
thin nose, an old thin burn scar at her right temple, platinum-blond
hair in a near-shaved crop; matte charcoal-black hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
TEAL accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile black helmet CLOSED with one seamless optically
clear panoramic visor, her face fully visible through it. Her boot has
kicked a low puff of graphite dust, caught mid-fall. The band of scattered dawn
light on the LEFT horizon is now five degrees tall; its warm grazing light
throws the figures' first long thin shadows to the RIGHT across the
black plain. Thirty meters frame right: the lander — the same 8-meter
angular lifting-body craft, satin machined black with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool of
white light onto the black ground. The plain is DEAD MATTE coal-black
basalt under graphite dust.

CAMERA & LIGHT: 35mm spherical lens, fixed 6 meters away at chest
height. Five artificial light sources plus the horizon's warm skim.
Gravity 0.8g, real time.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures. Teal lines = pilot, amber
lines = engineer — never identical. The suits have NO back-mounted
unit — both back silhouettes are flat. Each visor is optically clear
glass with zero tint, zero mirror coating and zero reflection of the
environment. 0% bloom, no soft focus. Photorealistic skin with pores.
The ground is DEAD MATTE — no gloss, no glint, never glowing. No
readable text anywhere. No subtitles, no watermark. Hand contacts keep
clear structural boundaries. Falling dust obeys 0.8g — never hovering,
never swirling. Terrain static. No CGI aesthetic. Photorealistic with
35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame — this film has exactly two humans total. No voice in this
scene.

CHARACTERS: The engineer — man, around fifty, 1.84 m, lean and rangy,
warm tan skin with visible pores, hooded dark eyes, silver-streaked
close-cropped hair, clean-shaven, two deep creases across his brow;
same matte charcoal-black hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
his face fully visible through it. The pilot — woman, mid-thirties,
1.70 m, wiry, pale cool-toned skin with visible pores, grey eyes,
sharp thin nose, an old thin burn scar at her right temple,
platinum-blond hair in a near-shaved crop; matte charcoal-black
hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid TEAL accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile black helmet
CLOSED with one seamless optically clear panoramic visor, her face
fully visible through it. Teal = pilot, amber = engineer — never
identical, never duplicated.

SCENE: Night surface; the band of scattered dawn light on the LEFT horizon
is five degrees tall, its warm grazing light throwing long thin shadows to the
RIGHT. Thirty meters frame right: the lander — the same 8-meter
angular lifting-body craft, satin machined black with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool of
white light onto the black ground. The plain is DEAD MATTE coal-black
basalt. Camera fixed 6 meters away, 35mm spherical lens.

TIMELINE:
0.0s — The engineer snaps the sample case latches shut, one-two, firm
gloved contacts.
2.5s — The pilot collapses the core drill into a short black tube and
slings it flat against her hip; a puff of graphite dust from her boot
falls and settles within 2 seconds.
5.5s — The engineer stands with the case; both turn to screen-right,
toward the lander at the right edge of frame — their backs coming
square to the dawn band — weighted, ordinary Earth pace, no slow
motion.
8.5s — They take their first strides toward the craft at screen-right. Their long
shadows swing ahead of them. Hold.

AUDIO: Muffled latch clicks carried low, boots crunching graphite
dust, twin suit-fans and controlled breathing on the radio channel.
No voice, no music.

PHYSICS: Gravity 0.8g — real time, ordinary Earth pace. All lifted
dust falls and settles within 2-3 seconds. Thin air: nothing flutters,
the light exerts no force.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures. The suits have NO back-mounted unit — both back
silhouettes are flat. Each visor is optically clear glass with zero
tint, zero mirror coating and zero reflection of the environment. 0%
bloom, no soft focus. The ground is DEAD MATTE — no gloss, no glint,
never glowing. No readable text anywhere. No subtitles, no watermark.
Hand contacts keep clear structural boundaries. Particles obey 0.8g —
never hovering, never swirling. Terrain static. No one moves toward
the dawn at screen-left — no direction reversal. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 4 (S4) — VİRAL #1: ŞAFAK DUVARI (V3 — kameraya koşu)

> ⭐ V3 KOMPOZİSYONU [DERS 104 · iki red sonrası]: V1'de koşucular şafağa
> koştu; V2'de (dört kanallı yön kilidi) model gemiyi arkaya atıp
> koşucuları kameraya döndürdü. V3 modelin frontal refleksiyle SAVAŞMAZ,
> onu doğru cevaba çevirir: kamera LANDERİN YANINDADIR — kameraya koşmak
> = gemiye koşmak. Uzamsal kılavuz §6.3 NÖTR ÇEKİM (kadran 6, yönsüz);
> dizideki tek nötr çekim budur ve geçiş noktasındadır (koşu → biniş).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a pitch-black planet, dawn line burning across the whole
horizon. Exactly 2 human figures in frame — this film has exactly two
humans total.

SCENE: The camera stands AT the lander, looking back along the escape
path. The craft's satin machined-black hull edge and one landing leg
cut into the extreme RIGHT foreground — the lander is the same 8-meter
angular lifting-body craft, satin machined black with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool of
white light onto the black ground — and that floodlight pool spills
across the near foreground. Twenty meters out, at frame center, two
suited figures run STRAIGHT TOWARD THE CAMERA — and toward the craft
beside it. Leading by a full stride, offset half a metre to
screen-left so both read fully: the pilot — woman, mid-thirties, 1.70
m, wiry, pale cool-toned skin with visible pores, grey eyes, sharp
thin nose, an old thin burn scar at her right temple, platinum-blond
hair in a near-shaved crop; matte charcoal-black hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
TEAL accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile black helmet CLOSED with one seamless optically
clear panoramic visor, her face visible through it, jaw set, mouth
closed. A stride behind her: the engineer — man, around fifty, 1.84 m,
lean and rangy, warm tan skin with visible pores, hooded dark eyes,
silver-streaked close-cropped hair, clean-shaven, two deep creases
across his brow; same matte charcoal-black hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
AMBER accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile black helmet CLOSED with one seamless optically
clear panoramic visor, carrying the slim matte-black sample case in
one hand. BEHIND the runners the entire background horizon burns: a
razor-thin gold-white dawn seam spans the full frame width, a band of
scattered dawn light eight degrees tall above it — back-lighting both
figures with warm rim light on shoulders and helmet crowns while their
fronts are lit only by their own chest and helmet lamps blazing toward
camera. Their long shadows reach toward the camera. The plain is
light-swallowing coal-black basalt under a skin of graphite dust, DEAD
MATTE — its texture reads only inside the pools of artificial light.

CAMERA & LIGHT: 32mm spherical lens, fixed 1.2 meters above the ground
beside the lander's bow, level gaze. Exactly five artificial light
sources exist in this world: two helmet lamps, two chest lamps, and
the lander's single belly floodlight. Gravity 0.8g — real sprint, real
time.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures. Teal = pilot (leading,
empty-handed, 1.70 m), amber = engineer (trailing, carrying the case,
1.84 m) — never identical. The lander is NEVER behind the runners —
its hull stays in the near RIGHT foreground beside the camera; the
background belongs to the dawn wall alone, no craft appears in the
background. The runners never turn away from the camera — no direction
reversal, no mirrored composition. The suits have NO back-mounted
unit — both back silhouettes are flat. Each visor is optically clear
glass with zero tint, zero mirror coating and zero reflection of the
environment. 0% bloom, no soft focus. The ground is DEAD MATTE — no
gloss, no glint, never glowing. No readable text anywhere. No
subtitles, no watermark. Particles obey 0.8g. Terrain static. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame — this film has exactly two humans total. No voice in this
scene.

SCENE: The camera stands AT the lander, 1.2 meters above the ground
beside its bow, 32mm spherical lens, looking back along the escape
path. The craft's satin machined-black hull edge and one landing leg
cut into the extreme RIGHT foreground — the lander is the same 8-meter
angular lifting-body craft, satin machined black with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool of
white light onto the black ground — its floodlight pool spilling
across the near foreground. The entire background horizon burns: a
razor-thin gold-white dawn seam spans the full frame width with a band
of scattered dawn light eight degrees tall above it. The plain between
is DEAD MATTE coal-black basalt. Two suited figures run STRAIGHT
TOWARD THE CAMERA — and toward the craft beside it: the pilot — woman,
1.70 m, matte charcoal-black hard-shell suit with thin inlaid TEAL
accent lines on the shoulder plates and forearms, low-profile black
helmet CLOSED — leading by a full stride, empty-handed, offset half a
metre to screen-left; the engineer — man, 1.84 m, same suit with thin
inlaid AMBER accent lines, low-profile black helmet CLOSED — a stride
behind, carrying the slim matte-black sample case. Both back-lit by
the dawn: warm rim on shoulders and helmets, fronts lit only by their
own four lamps blazing toward camera.

TIMELINE:
0.0s — Sixty meters out: two rim-lit silhouettes under the burning
horizon, four lamps swinging toward camera, closing at a real sprint —
grounded, weighted, ordinary Earth pace at 0.8g, no slow motion.
3.0s — Features resolve: teal lines leading, amber lines trailing with
the case. Graphite dust kicks from their heels and settles behind them
within 2 seconds.
6.0s — The dawn band brightens one step; their shadows stretch longer
toward the camera.
9.0s — The pilot reaches the edge of the floodlight pool, twelve
meters from camera, the engineer one stride behind. Hold — no
boarding, no hatch in this shot; the dawn wall stays behind them and
the craft stays beside the camera throughout.

AUDIO: Muffled rapid footfalls growing closer, two runners' hard
controlled breathing on the radio channel, thin airy hiss. No voice,
no music.

PHYSICS: Gravity 0.8g — real time, ordinary Earth pace. Dust settles
in 2-3 seconds. Thin air: nothing flutters; the distant light exerts
no force.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom, no slow motion. Exactly 2 human figures — never
identical, no third figure. The lander is NEVER behind the runners —
its hull stays in the near RIGHT foreground beside the camera; no
craft appears in the background, which belongs to the dawn wall alone.
The runners never turn away from the camera — no direction reversal,
no mirrored composition. The suits have NO back-mounted unit — both
back silhouettes are flat. Each visor is optically clear glass with
zero tint, zero mirror coating and zero reflection of the environment.
0% bloom, no soft focus. The ground is DEAD MATTE — no gloss, never
glowing. No readable text anywhere. No subtitles, no watermark.
Particles obey 0.8g — never hovering, never swirling. Terrain static.
No CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 5 (S5) — BİNİŞ

> A4 kararı [D69 ①]: kapak/merdiven hareketi kadraj DIŞI — S4 rayın
> kavranmasıyla bitti, S5 kabinde kayış takılırken açılır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Cramped
spacecraft cabin interior, night. Exactly 2 human figures in frame —
this film has exactly two humans total.

SCENE: A 2.2-meter-wide cockpit, two seats side by side, both crew
already seated and strapping in — the side hatch behind them is sealed
and no boarding movement occurs in this shot. In the LEFT seat: the
pilot — woman, mid-thirties, 1.70 m, wiry, pale cool-toned skin with
visible pores, grey eyes, sharp thin nose, an old thin burn scar at
her right temple, platinum-blond hair in a near-shaved crop; matte
charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
her face fully visible through it. She pulls her chest harness strap
down to its buckle. In the RIGHT seat: the engineer — man, around
fifty, 1.84 m, lean and rangy, warm tan skin with visible pores,
hooded dark eyes, silver-streaked close-cropped hair, clean-shaven,
two deep creases across his brow; same matte charcoal-black hard-shell
suit, dark graphite flex-weave joints, machined articulation rings,
thin inlaid AMBER accent lines on the shoulder plates and forearms,
finely scuffed with use; low-profile black helmet CLOSED with one
seamless optically clear panoramic visor, his face fully visible
through it. The slim matte-black sample case sits locked in a floor
rack beside his boot. Helmet lamps are OFF. The panel ahead is analog
and low-lit: rows of abstract amber and teal light segments — no text,
no digits — and a 12-cm mechanical attitude ball at its center.
Through the single wide windshield: black plain, and far LEFT the
gold-white dawn seam.

CAMERA & LIGHT: 35mm spherical lens, fixed at the front-left bulkhead
corner, 1.2 meters from the seats, three-quarter view of both. Light:
dim panel segments and the faint warm seam through the glass — low,
sculpted, no bloom.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no reflections with faces. Teal lines = pilot
(left seat), amber lines = engineer (right seat) — never identical.
The suits have NO back-mounted unit — both back silhouettes are flat.
Each visor is optically clear glass with zero tint, zero mirror
coating and zero reflection of the environment. 0% bloom, no soft
focus. Photorealistic skin with pores. No readable text, letters or
digits on any panel or display — abstract light segments only. No
subtitles, no watermark. Hand-buckle contacts keep clear structural
boundaries. Cabin static. No CGI aesthetic. Photorealistic with 35mm
film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame — this film has exactly two humans total. No voice in this
scene.

CHARACTERS: In the LEFT seat the pilot — woman, mid-thirties, 1.70 m,
wiry, pale cool-toned skin with visible pores, grey eyes, sharp thin
nose, an old thin burn scar at her right temple, platinum-blond hair
in a near-shaved crop; matte charcoal-black hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
TEAL accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile black helmet CLOSED with one seamless optically
clear panoramic visor, her face fully visible through it. In the RIGHT
seat the engineer — man, around fifty, 1.84 m, lean and rangy, warm
tan skin with visible pores, hooded dark eyes, silver-streaked
close-cropped hair, clean-shaven, two deep creases across his brow;
same matte charcoal-black hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED with one seamless optically clear panoramic visor,
his face fully visible through it. Teal = pilot, amber = engineer —
never identical, never duplicated.

SCENE: 2.2-meter cockpit, two seats side by side; sealed hatch behind
— no boarding movement in this shot. Analog panel of abstract amber
and teal light segments, no text; 12-cm mechanical attitude ball at
center. Through the windshield: black plain, dawn seam far LEFT. The
slim matte-black sample case locked in a floor rack. Camera fixed at
the front-left bulkhead corner, 1.2 meters away, 35mm spherical lens,
three-quarter view.

TIMELINE:
0.0s — The pilot pulls her chest strap down and seats the buckle with
a firm click; her gloved hands move with practiced economy, ordinary
pace.
3.0s — The engineer locks his own harness, then presses the sample
case rack latch once — checking it holds.
6.0s — The pilot's hand sweeps the panel edge; a row of amber segments
steps awake one by one, abstract, textless.
8.5s — Both settle back into their seats; two visored faces lit by the
panel glow. Hold.

AUDIO: Buckle clicks, soft cabin hum rising as systems wake, twin
suit-fans and calm breathing on the radio channel. No voice, no music.

PHYSICS: Gravity 0.8g inside the cabin — weighted arms, real time,
ordinary pace. Straps fall and hang naturally.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no faces in reflections. The suits have NO back-mounted unit — both
back silhouettes are flat. Each visor is optically clear glass with
zero tint, zero mirror coating and zero reflection of the environment.
0% bloom, no soft focus. No readable text, letters or digits on any
panel — abstract light segments only. No subtitles, no watermark. Hand
contacts keep clear structural boundaries — no merging, no extra
fingers. Cabin static — no warping. No CGI aesthetic. Photorealistic
with 35mm film grain.
```

---

## 🎬 SAHNE 6 (S6) — ATEŞLEME

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Spacecraft
cockpit seen from directly behind the two seats. Exactly 2 human
figures in frame, both seen from behind — this film has exactly two
humans total.

SCENE: The camera looks over the backs of two seats toward the wide
windshield; both crew are strapped in, seen from behind — their faces
are NOT visible, only the backs of two low-profile black helmets and
their shoulder plates. LEFT seat: the pilot — woman, mid-thirties,
1.70 m, wiry; matte charcoal-black hard-shell suit, dark graphite
flex-weave joints, machined articulation rings, thin inlaid TEAL
accent lines on the shoulder plates and forearms, finely scuffed with
use; low-profile black helmet CLOSED. Her right glove is wrapped
around a mechanical throttle lever at the center console, knuckles
set. RIGHT seat: the engineer — man, around fifty, 1.84 m, lean and
rangy; same matte charcoal-black hard-shell suit with thin inlaid
AMBER accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile black helmet CLOSED. His flat palm rests on the
console rail. Between them: the 12-cm mechanical attitude ball,
steady; rows of abstract amber and teal light segments, no text.
Through the windshield: the black plain and, frame LEFT, the dawn
seam — its band of scattered dawn light now ten degrees tall, gold-white, hard.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the seat
backs, centered. Light: panel segments from below, the seam's warm
light through the glass edging both helmets. Both back silhouettes are
FLAT — no back-mounted unit of any kind.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces visible, no faces in
reflections. Teal lines = pilot, amber lines = engineer. The suits have NO back-mounted unit — both back silhouettes are flat. Each visor is optically clear glass
with zero tint, zero mirror coating and zero reflection. 0% bloom, no
soft focus. No readable text, letters or digits on any panel —
abstract light segments only. No subtitles, no watermark. Hand-lever
contact keeps a clear structural boundary. Cabin static. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame, both seen from behind — this film has exactly two humans total.
Two spoken lines, one at a time; no mouth is visible.

CHARACTERS (from behind): LEFT seat — the pilot, woman, 1.70 m, matte
charcoal-black hard-shell suit with thin inlaid TEAL accent lines on
the shoulder plates and forearms, low-profile black helmet CLOSED; her
right glove wrapped around the mechanical throttle lever. RIGHT seat —
the engineer, man, 1.84 m, same suit with thin inlaid AMBER accent
lines, low-profile black helmet CLOSED; his palm flat on the console
rail. Teal = pilot, amber = engineer — never identical. Faces never
visible in this shot.

SCENE: Camera fixed 1.5 meters behind the two seat backs, 35mm
spherical lens, centered on the windshield. Analog panel: abstract
amber and teal segments, no text; 12-cm mechanical attitude ball
steady between the seats. Through the glass: black plain, and frame
LEFT the dawn seam with its band of scattered dawn light ten degrees tall.

TIMELINE:
0.5s — The pilot's voice over the radio, in Turkish, tight and even:
"Kalkıyoruz. Sıkı tutun."
3.0s — A calm neutral synthetic voice over the cabin speaker, in
Turkish: "Motorlar hazır. Pencere on saniye."
5.5s — Her glove tightens on the lever; the engineer's palm closes on
the rail.
7.0s — A low double thud rolls through the airframe; the amber segment
row climbs step by step; a faint vibration blurs nothing — the frame
stays locked.
9.5s — The attitude ball holds dead level. Hold on the last frame.

AUDIO: Cabin hum; two spoken lines exactly as scripted, one at a time,
heard only; deep muffled ignition thud at 7.0s building to a held low
rumble. No music.

PHYSICS: Gravity 0.8g; the craft has not yet lifted — vibration only,
no motion of the frame. Real time, ordinary pace.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces visible, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. Each
visor is optically clear glass with zero tint, zero mirror coating and
zero reflection. 0% bloom, no soft focus. No readable text on any
panel — abstract light segments only. The spoken lines are heard only
— no subtitles, no captions, no transcript. One speaker at a time; the
human voice comes over the radio with no mouth in frame; the synthetic
voice is off-screen only — no body, no avatar, no third figure. Cabin
static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 7 (S7) — VİRAL #2: KALKIŞ

> Kalkış reçetesi Cold Burn'de kanıtlanan dört adımdır; 4,5 s'den sonra
> hiçbir karede bacak görünmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
exterior on a pitch-black planet at the instant of engine ignition.
No human figure is in frame — both crew are inside the craft.

SCENE: Side view of the lander — an 8-meter angular LIFTING-BODY
craft, no plain cylinder: broad flat belly, sharp chine lines running
nose to tail, a low blended forward canopy, two short swept strakes,
twin main engines recessed in a notched tail, four downward LIFT
NOZZLES under the belly, four landing legs that fold up into flush
belly wells, two recessed thruster quads at the bow and two at the
stern, a 40-cm round aft observation port above the engine notch, and
two docking rails along the aft flanks; satin machined-black composite
panels with crisp recessed seams over a graphite-grey structural
spine, one thin SIGNAL-WHITE chevron line down each flank, and a side
hatch — still standing on its four legs, nose pointed frame RIGHT. Its
four belly lift nozzles have just ignited: four hard, short, blue-white
jets stab straight down, and their light carves the plain's true
texture out of the darkness for the first time — ridged coal-black
basalt and graphite dust across a 30-meter radius, four rings of black
dust bursting low and outward. Beyond that radius the world is black
again. At the far LEFT frame edge, the dawn seam's band of scattered light
stands ten degrees tall. The belly floodlight is OFF. The plain is DEAD MATTE
coal-black basalt — its texture reads only inside the engine light.

CAMERA & LIGHT: 32mm spherical lens, fixed 80 meters abeam at ground
level. The only lights: four engine jets and the distant dawn band.
Hard-edged shadows radiate from the craft.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame: zero — both crew are inside the craft. 0%
bloom, no glow filter, no soft focus — every surface keeps texture.
Black surfaces stay DEAD MATTE (ground) or satin machined (hull) —
never glossy, never mirror-like. No readable text anywhere. No
subtitles, no title card, no watermark. Dust obeys 0.8g with
continuous momentum — never hovering, never swirling. Terrain and hull
static — no melting, no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. No human figure is in frame —
both crew are inside the craft.

SCENE: Side view, camera fixed 80 meters abeam at ground level, 32mm
spherical lens. The lander — an 8-meter angular LIFTING-BODY craft, no
plain cylinder: broad flat belly, sharp chine lines running nose to
tail, a low blended forward canopy, two short swept strakes, twin main
engines recessed in a notched tail, four downward LIFT NOZZLES under
the belly, four landing legs that fold up into flush belly wells, two
recessed thruster quads at the bow and two at the stern, a 40-cm round
aft observation port above the engine notch, and two docking rails
along the aft flanks; satin machined-black composite panels with crisp
recessed seams over a graphite-grey structural spine, one thin
SIGNAL-WHITE chevron line down each flank, and a side hatch — nose
pointed frame RIGHT, standing on its four legs on a DEAD MATTE
coal-black basalt plain. Far LEFT frame edge: the dawn seam, its
scattered-light band ten degrees tall.

TIMELINE:
0.0s — The belly floodlight cuts out. One breath of darkness — only
the dawn seam burns.
0.8s — All four belly lift nozzles ignite at once: four hard blue-white
jets straight down. Their light carves the plain's texture out of the
dark across a 30-meter radius; four rings of black dust burst low and
outward in ballistic arcs.
2.5s — The craft rises dead level, body horizontal, no tilting; the
dust rings collapse and settle within 3 seconds.
4.5s — At 20 meters altitude the four landing legs fold up into their
flush belly wells and the well doors close; after 4.5s no landing leg,
no leg well and no open gear door is visible in any frame.
6.5s — The twin tail engines light; the belly jets cut out.
8.0s — The craft accelerates nose-first toward frame RIGHT, climbing
shallowly, engine light raking the ground beneath it.
9.5s — It exits frame right. The plain falls back to black; only the
dawn seam remains. Hold. The nose stays toward frame right throughout —
the craft never turns toward the dawn seam at frame left.

AUDIO: Two-stage muffled roar, all low frequencies — a deep flat
thunder that swells at ignition and Dopplers away; the patter of
falling dust; thin airy hiss after. No voice, no music.

PHYSICS: Gravity 0.8g, thin 3% atmosphere. Launch order is fixed:
belly nozzles → level rise → legs fold at 20 m → tail engines. The
body NEVER pitches vertical. Every dust particle follows a ballistic
arc and settles within 3 seconds — no hovering, no swirling.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside the craft. 0% bloom, no glow filter, no soft
focus. Black surfaces stay DEAD MATTE (ground) or satin machined
(hull) — never glossy. After 4.5s no landing leg, no leg well, no open
gear door in any frame. No readable text anywhere. No subtitles, no
title card, no watermark. Dust obeys 0.8g with continuous momentum —
never hovering, never swirling. Terrain and hull static. No Unreal
Engine look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 8 (S8) — IŞIK SINIRI

> ⚠️ Cold Burn S8 bu konumdaki sahnede YAPISAL RED almıştı — bu prompt
> kısa negatifle ve pozitif boş-kadraj anlatımıyla yazıldı (üretim notu ①).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. High
altitude over a pitch-black planet at the edge of dawn. No human
figure is in frame — both crew are inside the climbing craft.

SCENE: A vast, calm frame split by light. The lower half is the
planet's night side: featureless light-swallowing black. Running
diagonally across it, from lower left to mid right, the terminator — a
thin seam of scattered sunrise light burning along the boundary like a
heated wire. Beyond the seam, the day side: fully sunlit yet still
near-black charcoal, its ridges faintly modeled — this world reflects
almost nothing. The upper half of the frame is space: pure black,
sharp unblinking stars. At center-right, small and climbing toward
upper frame RIGHT: the lander — the same 8-meter angular lifting-body
craft in FLIGHT CONFIGURATION, all four landing legs folded away into
flush belly wells, its belly line clean, satin machined black with one
thin SIGNAL-WHITE chevron line down each flank — caught at the moment
it crosses out of shadow into direct sunlight: hard white rim light
ignites along its chine lines and canopy edge while its shadow side
stays absolutely black. A short, thin main-engine exhaust trail fades
behind it.

CAMERA & LIGHT: 32mm spherical lens, fixed high-altitude position. Two
lights only: the terminator seam below and hard sunlight from frame
LEFT on the craft. No atmospheric haze at this altitude, no lens
flare, no glow.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame: zero — both crew are inside the craft. 0%
bloom, no glow filter, no soft focus. Black surfaces stay DEAD MATTE
(ground) or satin machined (hull) — never glossy. No landing leg, no
leg well, no open gear door visible. No readable text anywhere. No
subtitles, no title card, no watermark. Terrain and hull static. No
Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. No human figure is in frame —
both crew are inside the climbing craft.

SCENE: High altitude, 32mm spherical lens, fixed frame split by light.
Lower half: the planet's night side, featureless light-swallowing
black, crossed diagonally by the terminator — a thin seam of scattered
sunrise light burning like a heated wire. Beyond it the day side:
sunlit yet still near-black charcoal, ridges faintly modeled. Upper
half: space, pure black, sharp stars. The lander — the same 8-meter
angular lifting-body craft in FLIGHT CONFIGURATION, all four landing
legs folded away into flush belly wells, its belly line clean, satin
machined black with one thin SIGNAL-WHITE chevron line down each
flank — enters at lower center, climbing steadily toward upper frame
RIGHT, nose forward, a short thin exhaust trail behind it.

TIMELINE:
0.0s — The craft climbs through shadow: visible only as a moving
absence of stars and a faint white chevron line.
4.0s — It crosses the light boundary: hard white rim light ignites
along its chine lines, canopy edge and tail in a single clean sweep;
its shadow side stays absolutely black.
7.0s — The exhaust trail thins and disappears as the air runs out; the
craft keeps climbing, steady, unhurried.
10.0s — It nears upper frame right, a rim-lit black arrowhead over a
burning line. Hold.

AUDIO: A faint, fading low engine tone in the first seconds — then
near-silence as the atmosphere thins to nothing. No voice, no music.

PHYSICS: Upper thin atmosphere into vacuum: the exhaust trail is short
and straight and fades within seconds; no billowing, no curling. The
craft's motion is smooth and continuous — real time. Stars stay sharp
points.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside the craft. 0% bloom, no glow filter, no soft
focus, no lens flare. Black surfaces stay DEAD MATTE (ground) or satin
machined (hull) — never glossy. No landing leg, no leg well, no open
gear door in any frame. No readable text anywhere. No subtitles, no
title card, no watermark. Exhaust obeys physics with continuous
momentum — never swirling. No direction reversal — the craft never
banks back toward the light boundary. Terrain and hull static. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 9 (S9) — HASAR

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Low orbit
above a pitch-black planet, hard vacuum. No human figure is in frame —
both crew are inside the craft.

SCENE: Close detail of the bow of the lander — an 8-meter angular
LIFTING-BODY craft, no plain cylinder: broad flat belly, sharp chine
lines running nose to tail, a low blended forward canopy, two short
swept strakes, twin main engines recessed in a notched tail, four
downward LIFT NOZZLES under the belly, four landing legs that fold up
into flush belly wells, two recessed thruster quads at the bow and two
at the stern, a 40-cm round aft observation port above the engine
notch, and two docking rails along the aft flanks; satin machined-black
composite panels with crisp recessed seams over a graphite-grey
structural spine, one thin SIGNAL-WHITE chevron line down each flank,
and a side hatch — in FLIGHT CONFIGURATION, no landing leg visible.
The bow fills frame right, nose toward camera at a shallow angle. Both
recessed BOW thruster quads are visible: their nozzle rims scorched
dull grey, hairline crazing webbed across the housings — heat damage
from the dawn crossing. From one quad, a last thin asymmetric cold-gas
jet sputters — short, straight, already dying. A few tiny flakes of
charred coating drift away from the housings in perfectly straight
lines. Background: black space, sharp stars; along the bottom frame
edge, the planet's limb — a barely-visible charcoal curve with a
razor-thin bright terminator seam far below.

CAMERA & LIGHT: 85mm spherical lens, fixed 6 meters off the bow. Hard
sunlight from frame LEFT: razor shadows, one lit flank, the shadow
side absolutely black — this black planet returns no fill light. No
haze, no flare, no glow.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame: zero — both crew are inside the craft. 0%
bloom, no glow filter, no soft focus, no lens flare. Hull stays satin
machined black — never glossy, never mirror-like; the planet stays
DEAD MATTE. No landing leg, no leg well, no open gear door visible. No
readable text anywhere. No subtitles, no title card, no watermark.
Drifting flakes obey zero gravity with continuous straight-line
momentum — never hovering in place, never swirling. Hull static — no
melting, no warping. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. No human figure is in frame —
both crew are inside the craft. One synthetic voice speaks over the
radio channel; there is no other sound.

SCENE: Low orbit, hard vacuum. Close detail, 85mm spherical lens,
camera fixed 6 meters off the bow of the lander — an 8-meter angular
LIFTING-BODY craft, no plain cylinder: broad flat belly, sharp chine
lines running nose to tail, a low blended forward canopy, two short
swept strakes, twin main engines recessed in a notched tail, four
downward LIFT NOZZLES under the belly, four landing legs that fold up
into flush belly wells, two recessed thruster quads at the bow and two
at the stern, a 40-cm round aft observation port above the engine
notch, and two docking rails along the aft flanks; satin machined-black
composite panels with crisp recessed seams over a graphite-grey
structural spine, one thin SIGNAL-WHITE chevron line down each flank,
and a side hatch — in FLIGHT CONFIGURATION, no landing leg visible.
Both bow thruster quads scorched dull grey, hairline crazing across
the housings. Hard sunlight from frame LEFT; shadow side absolutely
black — the black planet below returns no fill. Stars sharp; the
planet's charcoal limb and its thin bright terminator seam along the
bottom edge.

TIMELINE:
0.0s — One bow quad fires a short, thin, asymmetric cold-gas jet — it
stutters twice, straight and quickly fading.
3.5s — The jet dies completely. The quad stays dark.
5.0s — A few tiny flakes of charred coating continue drifting away in
perfectly straight lines at constant speed, unhurried.
6.5s — A calm neutral synthetic voice over the radio channel, level,
in Turkish: "Burun iticileri soğuk. İki küme, sıfır basınç."
10.0s — Stillness: the scorched quads, the stars, the thin burning
seam below. Hold.

AUDIO: No exterior sound — hard vacuum. The only audio is the radio
channel: faint carrier hiss, then the synthetic line at 6.5s, heard
only — never shown as text.

PHYSICS: Zero gravity, hard vacuum. Jets are short, straight cones
that thin out within one second — no billowing, no curling. Free
flakes keep straight-line momentum at constant speed — never hovering,
never swirling. The craft itself stays steady in frame.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside the craft. 0% bloom, no glow filter, no lens
flare. Hull satin machined black — never glossy; planet DEAD MATTE. No
landing leg, no leg well, no open gear door in any frame. No readable
text anywhere. The spoken line is heard only — no subtitles, no
captions, no transcript; the synthetic voice is off-screen only — no
body, no avatar, no third figure. Particles obey zero gravity with
continuous momentum. Hull static. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 10 (S10) — KARŞILAŞMA

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Spacecraft
cockpit seen from directly behind the two seats, orbit at night side.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total.

SCENE: Camera looks over the backs of two seats; the wide windshield
fills the frame with a field of sharp stars. Right of center in that
star field hangs the main ship — a 120-metre interstellar transfer
vessel still kilometres away, reading as a long black silhouette that
blots out the stars behind it, one full edge traced in hard sunlight,
a few thin white position lines spaced along its length; it does not
rotate and shows no lit windows. LEFT seat, from behind: the pilot —
woman, mid-thirties, 1.70 m, wiry; matte charcoal-black hard-shell
suit, dark graphite flex-weave joints, machined articulation rings,
thin inlaid TEAL accent lines on the shoulder plates and forearms,
finely scuffed with use; low-profile black helmet CLOSED. RIGHT seat,
from behind: the engineer — man, around fifty, 1.84 m, lean and rangy;
same matte charcoal-black hard-shell suit with thin inlaid AMBER
accent lines on the shoulder plates and forearms, finely scuffed with
use; low-profile black helmet CLOSED. His right arm is raised, gloved
finger pointing at the silhouette — arm seen from behind, no face
visible. Between the seats: the 12-cm mechanical attitude ball,
steady; abstract amber and teal panel segments, low, textless.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the seat
backs, centered on the windshield. Light: dim panel glow only; the
star field and the sunlit edge of the distant ship do the rest. Both
back silhouettes FLAT.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces visible, no faces in
reflections on the glass. Teal lines = pilot, amber lines = engineer.
The suits have NO back-mounted unit — both back silhouettes are flat.
Each visor is optically clear glass with zero tint, zero mirror
coating and zero reflection. 0% bloom, no soft focus, no lens flare.
No readable text on any panel — abstract light segments only. No
subtitles, no watermark. The distant ship is a positive solid object
edged by sunlight — not a hole, not a void effect. Cabin static. No
CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame, both seen from behind — this film has exactly two humans total.
One spoken line; no mouth is visible.

CHARACTERS (from behind): LEFT seat — the pilot, woman, 1.70 m, matte
charcoal-black hard-shell suit with thin inlaid TEAL accent lines on
the shoulder plates and forearms, low-profile black helmet CLOSED.
RIGHT seat — the engineer, man, 1.84 m, same suit with thin inlaid
AMBER accent lines, low-profile black helmet CLOSED. Teal = pilot,
amber = engineer — never identical. Faces never visible in this shot.

SCENE: Camera fixed 1.5 meters behind the seat backs, 35mm spherical
lens; the windshield fills the frame with sharp stars. Right of
center: the main ship — a 120-metre interstellar transfer vessel still
kilometres away, reading as a long black silhouette that blots out the
stars behind it, one full edge traced in hard sunlight, a few thin
white position lines spaced along its length; it does not rotate and
shows no lit windows. Panel: abstract amber and teal segments, 12-cm
mechanical attitude ball steady.

TIMELINE:
0.0s — Stillness. Star field steady; the black silhouette hangs right
of center, its sunlit edge a fine hard line.
3.5s — The engineer's right arm rises, gloved finger extending toward
it.
5.0s — His voice over the radio, quiet, in Turkish: "İşte orada.
Yıldızların olmadığı yer."
7.5s — The pilot's helmet turns a few degrees toward it, then back.
Her glove settles onto the translation controller.
10.0s — Hold: two flat black shoulder silhouettes, and the ship that
eats the stars.

AUDIO: Low cabin hum; twin suit-fans and slow breathing on the radio
channel; the single spoken line at 5.0s, heard only. No music.

PHYSICS: Zero gravity; both bodies strapped, motions economical. The
star field is steady — the craft holds attitude. Real time.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces visible, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. Each
visor is optically clear glass with zero tint, zero mirror coating and
zero reflection. 0% bloom, no soft focus, no lens flare. No readable
text on any panel — abstract light segments only. The spoken line is
heard only — no subtitles, no captions, no transcript; the voice comes
over the radio with no mouth in frame. The distant ship is a positive
solid object — not a hole. Cabin static. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 11 (S11) — KARAR

> Kadraj S10'un birebir tekrarıdır (bilinçli çift — güvenin kurulduğu
> yer aynı yerden gösterilir); değişen tek şey eller ve sözlerdir.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Spacecraft
cockpit seen from directly behind the two seats, orbit. Exactly 2
human figures in frame, both seen from behind — this film has exactly
two humans total.

SCENE: The same fixed framing as the previous cockpit shot: camera
over the backs of two seats, windshield full of sharp stars, and right
of center the main ship — a 120-metre interstellar transfer vessel
still kilometres away, reading as a long black silhouette that blots
out the stars behind it, one full edge traced in hard sunlight, a few
thin white position lines spaced along its length; it does not rotate
and shows no lit windows — now slightly larger than before. LEFT seat,
from behind: the pilot — woman, mid-thirties, 1.70 m, wiry; matte
charcoal-black hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED. Both her gloves now rest on the twin translation
and rotation controllers, deliberate and set. RIGHT seat, from behind:
the engineer — man, around fifty, 1.84 m, lean and rangy; same matte
charcoal-black hard-shell suit with thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
black helmet CLOSED. His torso is half-turned toward the dark narrow
passage in the rear bulkhead between the seats — toward the aft
observation port he will soon man. Between the seats: the 12-cm
mechanical attitude ball, steady; abstract amber and teal segments,
textless.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the seat
backs, centered. Dim panel glow; star field; the ship's single sunlit
edge. Both back silhouettes FLAT.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces visible, no faces in
reflections. Teal lines = pilot, amber lines = engineer. The suits
have NO back-mounted unit — both back silhouettes are flat. Each visor
is optically clear glass with zero tint, zero mirror coating and zero
reflection. 0% bloom, no soft focus, no lens flare. No readable text
on any panel — abstract light segments only. No subtitles, no
watermark. The distant ship is a positive solid object — not a hole.
Cabin static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. Exactly 2 human figures in
frame, both seen from behind — this film has exactly two humans total.
Two spoken lines, one at a time; no mouth is visible.

CHARACTERS (from behind): LEFT seat — the pilot, woman, 1.70 m, matte
charcoal-black hard-shell suit with thin inlaid TEAL accent lines on
the shoulder plates and forearms, low-profile black helmet CLOSED,
both gloves on the twin controllers. RIGHT seat — the engineer, man,
1.84 m, same suit with thin inlaid AMBER accent lines, low-profile
black helmet CLOSED. Teal = pilot, amber = engineer — never identical.
Faces never visible in this shot.

SCENE: Camera fixed 1.5 meters behind the seat backs, 35mm spherical
lens — the same framing as the previous cockpit shot. Windshield full
of sharp stars; right of center the main ship — a 120-metre
interstellar transfer vessel still kilometres away, reading as a long
black silhouette that blots out the stars behind it, one full edge
traced in hard sunlight, a few thin white position lines spaced along
its length; it does not rotate and shows no lit windows. Panel:
abstract segments, mechanical attitude ball steady.

TIMELINE:
1.0s — A calm neutral synthetic voice over the cabin speaker, level,
in Turkish: "Önden frenleme yok. Kızağa kıç önde gireceğiz."
4.0s — Silence. The pilot's gloves settle deeper onto the controllers.
5.5s — Her voice over the radio, quieter than command tone, in
Turkish: "Göremeyeceğim. Gözlerim sensin."
7.5s — The engineer's near glove closes briefly on the frame of her
seat — one firm press, an answer without words — then he turns toward
the dark aft passage.
10.0s — Hold: her hands on the controls, his shoulder entering the
passage, the black ship waiting in the glass.

AUDIO: Low cabin hum; the two lines exactly as scripted, one at a
time, heard only; the soft creak of his harness as he turns. No music.

PHYSICS: Zero gravity; strapped bodies, economical motion; the star
field steady. Real time.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces visible, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. Each
visor is optically clear glass with zero tint, zero mirror coating and
zero reflection. 0% bloom, no soft focus, no lens flare. No readable
text on any panel — abstract light segments only. The spoken lines are
heard only — no subtitles, no captions, no transcript. One speaker at
a time; the human voice comes over the radio with no mouth in frame;
the synthetic voice is off-screen only — no body, no avatar, no third
figure. Cabin static. No CGI aesthetic. Photorealistic with 35mm film
grain.
```

---

## 🎬 SAHNE 12 (S12) — PART A KAPANIŞ: DÖNÜŞ

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Low orbit
above a pitch-black planet, hard vacuum. No human figure is in frame —
both crew are inside the craft.

SCENE: The lander — an 8-meter angular LIFTING-BODY craft, no plain
cylinder: broad flat belly, sharp chine lines running nose to tail, a
low blended forward canopy, two short swept strakes, twin main engines
recessed in a notched tail, four downward LIFT NOZZLES under the
belly, four landing legs that fold up into flush belly wells, two
recessed thruster quads at the bow and two at the stern, a 40-cm round
aft observation port above the engine notch, and two docking rails
along the aft flanks; satin machined-black composite panels with crisp
recessed seams over a graphite-grey structural spine, one thin
SIGNAL-WHITE chevron line down each flank, and a side hatch — in
FLIGHT CONFIGURATION, no landing leg visible — caught mid-yaw at
exactly 90 degrees, seen full side-on from 30 meters abeam, pivoting
so its TAIL will lead. From one stern thruster quad: a short, straight
cold-gas jet, thin and already fading. Hard sunlight from frame LEFT
rims the hull's chines and the white chevron; the shadow side is
absolutely black — the black planet below returns no fill light. Along
the bottom frame edge: the planet as a charcoal crescent, barely
brighter than space, with a razor-thin burning terminator seam. Sharp
stars everywhere else.

CAMERA & LIGHT: 32mm spherical lens, fixed 30 meters abeam. Single
hard key from frame LEFT; no fill, no haze, no flare.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame: zero — both crew are inside the craft. 0%
bloom, no glow filter, no soft focus, no lens flare. Hull satin
machined black — never glossy; planet DEAD MATTE. No landing leg, no
leg well, no open gear door visible. No bow thruster fires — the bow
quads are dead and dark. No readable text anywhere. No subtitles, no
title card, no watermark. Jets obey vacuum physics — short straight
cones, never billowing. Hull static — no melting, no warping. No
Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera, no camera movement. No human figure is in frame —
both crew are inside the craft.

SCENE: Low orbit, hard vacuum, 32mm spherical lens, camera fixed 30
meters abeam. The lander — an 8-meter angular LIFTING-BODY craft, no
plain cylinder: broad flat belly, sharp chine lines running nose to
tail, a low blended forward canopy, two short swept strakes, twin main
engines recessed in a notched tail, four downward LIFT NOZZLES under
the belly, four landing legs that fold up into flush belly wells, two
recessed thruster quads at the bow and two at the stern, a 40-cm round
aft observation port above the engine notch, and two docking rails
along the aft flanks; satin machined-black composite panels with crisp
recessed seams over a graphite-grey structural spine, one thin
SIGNAL-WHITE chevron line down each flank, and a side hatch — in
FLIGHT CONFIGURATION, no landing leg visible — drifts nose toward
frame RIGHT. Hard sunlight from frame LEFT rims the hull; shadow side
absolutely black. Bottom frame edge: the planet as a charcoal crescent
with a razor-thin burning terminator seam. Sharp stars.

TIMELINE:
0.0s — The craft coasts steadily, nose leading toward frame right.
1.0s — Two short straight cold-gas jets puff from the STERN quads
only — each thins to nothing within one second — and the craft begins
a slow, constant yaw.
5.0s — Full side-on: the white chevron line broadside to camera, the
yaw continuing at the same unhurried rate.
8.5s — Two opposite stern jets puff once; the rotation stops cleanly.
The craft now points its TAIL toward frame right — it will fly the
rest of this journey backwards.
10.0s — Hold: a black arrowhead flying tail-first over a burning
thread of dawn.

AUDIO: None — hard vacuum silence. No radio, no voice, no music.

PHYSICS: Zero gravity, hard vacuum. Yaw begins and ends only with
visible stern thruster pulses; the rate between pulses is perfectly
constant. Jets are short straight cones fading within one second. The
BOW quads never fire — they are dead. Stars stay sharp points; no
motion blur, no star trails. At the end of the turn the TAIL — never
the nose — points toward frame right.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside the craft. 0% bloom, no glow filter, no lens
flare. Hull satin machined black — never glossy; planet DEAD MATTE. No
landing leg, no leg well, no open gear door in any frame. No bow
thruster fires. No readable text anywhere. No subtitles, no title
card, no watermark. Jets obey vacuum physics with continuous
momentum — never billowing, never swirling. Hull static. No Unreal
Engine look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

---

# 📋 PART A ÖZET TABLOSU

| # | Sahne | İnsan | Işık ailesi | Şafak seti | Replik | Lens / mesafe |
|---|---|:---:|---|:---:|:---:|---|
| S0 | HOOK — KÖMÜR (9s) | 2 (uzak) | Gece yüzeyi | 2° | — | 24mm / 300 m hava |
| S1 | KAROT | 2 | Gece yüzeyi | (sol uzak) | — | 35mm / 8 m |
| S2 | UYARI | 2 | Gece yüzeyi | 4° | MİRA | 32mm / 10 m |
| S3 | TOPLAMA | 2 | Gece yüzeyi | 5° | — | 35mm / 6 m |
| S4 | VİRAL #1 — ŞAFAK DUVARI (V3) | 2 | Gece yüzeyi | 8° | — | 32mm / araç yanı · NÖTR çekim (kameraya koşu) |
| S5 | BİNİŞ | 2 | Kabin | (camda) | — | 35mm / 1.2 m |
| S6 | ATEŞLEME | 2 (arkadan) | Kabin | 10° | PİLOT+MİRA | 35mm / 1.5 m |
| S7 | VİRAL #2 — KALKIŞ | 0 | Kalkış | 10° | — | 32mm / 80 m |
| S8 | IŞIK SINIRI | 0 | Yörünge geçiş | terminatör | — | 32mm / yüksek |
| S9 | HASAR | 0 | Yörünge | (altta dikiş) | MİRA | 85mm / 6 m |
| S10 | KARŞILAŞMA | 2 (arkadan) | Kabin | — | MÜHENDİS | 35mm / 1.5 m |
| S11 | KARAR | 2 (arkadan) | Kabin | — | MİRA+PİLOT | 35mm / 1.5 m |
| S12 | DÖNÜŞ | 0 | Yörünge | (altta dikiş) | — | 32mm / 30 m |

**Doğrulama:** 13 sahne · 26 prompt · insanlı 9 sahne / 18 prompt (D79
negatif çifti 18/18) · replikli 5 sahne / 7 replik (MİRA 4 · PİLOT 2 ·
MÜHENDİS 1) · sessiz 8 sahne · şafak seti monotonik 2°→10° →
terminatör · bacaklar S7 4,5 s'den sonra 0 kare.

---

## 🚪 KAPI KAYITLARI [D74] — her koşu TEK SATIR

```
Format: TARİH · KAPI (S15/S21/S7/S0) · SONUÇ (GEÇTİ / V2 / DÜŞÜŞ) · not
16.08.2026 · S4 (kapı dışı deneme, operatör raporu) · V2 — koşucular
  landera değil ŞAFAĞA (ters yöne) koştu → DERS 104 yazıldı; dört
  kanallı yön kilidi S3·S4·S7·S8·S12 + PART_B S15-S21 + fragman
  V0-V4'e işlendi.
16.08.2026 · S4 ikinci deneme (operatör raporu) · V2 de düştü —
  model gemiyi ARKAYA atıp koşucuları kameraya döndürdü (frontal
  refleks dört kanala rağmen kazandı) → KAÇIŞ BASAMAĞI uygulandı:
  V3 kompozisyonu — kamera landerin yanına taşındı, kameraya koşu =
  gemiye koşu (nötr çekim §6.3); fragman V0 da aynı karara çekildi.
  Yeni deneme V3 promptlarla yapılır.
17.08.2026 · S4 üçüncü deneme (operatör raporu) · V3 GEÇTİ — kamera
  landerin yanında, kameraya koşu = gemiye koşu; yön doğru. Karar
  UZAMSAL kılavuza Sürüm 3 olarak işlendi (§0.1 · §6.7 · §6.8).
17.08.2026 · ÜRETİM DURUMU: S0-S14 üretildi (operatör onayı).
17.08.2026 · S15 (kapı 1) · ÜRETİM ÖNCESİ V2 — yanal oran karesi
  üretilmeden RİSKLİ sınıftan çıkarıldı [YANAŞMA KILAVUZU §1.2]:
  kamera rıhtım ağzına, araç TAIL-ON; "geri geri" ancak kuyruk
  kameraya dönükken okunur. S17/S20 kararı S15 sonucunu bekler
  (PART_B üretim notu ⑤). Deneme V2 promptuyla yapılır.
17.08.2026 · S17-S21 (operatör kararı) · yanal kadrajda kuyruk-önde
  uçuş "önü dönük yanaşma" okunuyor → S17·S20 rıhtım ağzı kadrajına
  (S15 ile üçlü merdiven), S21 rıhtım İÇİ kameraya alındı; dördü de
  DEAD TAIL-ON. S13·S22·S24 statik, dokunulmadı. S0-S14 promptları
  değişmedi.
17.08.2026 · S19b EKLENDİ (operatör isteği) · kanat kamerası ara
  sahnesi: aracın kıç flankındaki yanaşma kamerasından rıhtım görüntüsü,
  kıç itici puflarıyla hafif sağ-sol düzeltmeler. Film 26 sahne = 4:19
  (bilinçli sapma, planda belgeli). Numaralar kaymadı; replik yok,
  diyalog takvimi değişmedi.
17.08.2026 · S16 video · 3 RED ("I encountered an error" ×3, 0 başarı;
  teknik/geçici mesaj ama aynı promptta 3/0 → yapısal muamele,
  KILAVUZ §7) · V2: NEGATIVE tek pozitif Style satırına indirildi,
  yokluk listeleri pozitife çevrildi, 3.1k → ~2.4k. ⚠️ D79 tam bloğu
  bu promptta Style içi kısa hâle indirildi — üretim çıktısında sırt
  ünitesi/yansıma görülürse ilk şüpheli budur. Deneme V2 ile yapılır.
17.08.2026 · QA · 232 s'lik bir kurguya BEŞ mercek koşuldu (mod V) —
  raporlar: kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
  01_FILM_RAPORLARI/THE_BLACK_CRADLE.md
  ⛔ Dördü GEÇERSİZ: ölçme aleti kendi içinde çelişti (🔧 21 kesme ↔ diğer
  dördü 4 sahne) → DERS 107-110. Ayrıca kurgu kapısı koşulmadı: kapı
  26 klip / 259 s ±2 s ister, ölçülen 232 s / ~22 kesme.
  ⬜ AÇIK — bu defter "S0-S14 üretildi" derken 232 s'lik kurgu ölçüldü:
  S15 sonrası üretim yapıldıysa SATIRLARI BURAYA YAZ [D74]. Kapı defteri
  güncellenmeden ve master'ın klip sayımı yapılmadan yeni QA koşulmaz.
```
