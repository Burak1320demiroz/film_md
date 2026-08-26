# ⚫ THE STARLESS CIRCLE — Film QA Kaydı

> Oluşturma: 06.08.2026 · dört mercek aynı gün, dördü de MOD V (belgesiz)
> koşuldu — oysa filmin kendi dosyasında hazır SPEC bloğu var (§0.15).
> Kaynak dosya: `yatay_2_4_dk_filmler_uzay/THE_STARLESS_CIRCLE/THE_STARLESS_CIRCLE_PLANET_FILM.md`

---

## 🎯 MERCEK DURUMU

| Mercek | Durum | Skor | Ham rapor |
|---|---|---|---|
| 🔧 VIDEO_QA | ⚠️ Ⓥ mod V — **12 s tek klip**, kimliği doğrulanmadı | **5.7/10** · REGENERATE (1 BLOCKER) | `02_HAM_RAPORLAR/THE_STARLESS_CIRCLE_TEKNIK_HAM.md` |
| 📖 SENARYO_QA | 🚨 **GEÇERSİZ** — 12 s klip film gibi puanlandı | ~~4.1/10~~ | `..._SENARYO_HAM.md` |
| 🧩 MANTIK_QA | ✅ (rubrik zaten belgesiz) · tam kurgu | **5.5/10** · STRUCTURAL PROBLEM | `..._MANTIK_HAM.md` |
| 🧍 KARAKTER_QA | ✅ (opsiyonel 5. mercek) · tam kurgu | **6.0/10** · IDENTITY BREAK | `..._KARAKTER_HAM.md` |
| 🎨 KAPAK_QA | ❌ | — | — |

```
KÜNYE (plan)    18 sahne × 10 s = 180 s · 0 kesme · sessiz · ince atm. GECE
                doruk S9 (ışık takası) · bedel S12'de görülür ·
                S15-S17 insansız koda · yıldızsız daire = YOKLUK
KURGU (ölçülen) 174 s · 19 klip = 18 sahne + 2:50'de YANIK BAŞLIK KARTI
                ("THE CIRCLE WITH NO STARS") · doruk kurguda VAR ama
                hiçbir mercek okuyamadı · daire NESNE olarak çıktı
                ("black sphere") · vizör aynalı, sırtta yaşam destek ünitesi
İKİ FARKLI      🔧 ve 📖 mercekleri 12 s'lik TEK KLİBE koşuldu;
MALZEME         🧩 ve 🧍 2:54'lük kurguya. Dört skor aynı şeyi ölçmüyor.
DERS 65 NOTU    dört raporun dördü de FILM: (not supplied) yazdı — kural TUTTU
```

---

## 🔎 FLAGS FOR DOCUMENT CHECK — CEVAPLAR (plan dosyasından)

> Mod V raporları soru sordu; cevaplar plan/bible'dan verildi. Bu bölüm
> kart C/D/E/E2 adım 2'dir ve koşunun en değerli çıktısıdır.

### 🔧 VIDEO_QA soruları

**1. "0:00 gök tamamen yıldızsız — tasarım mı, halüsinasyon mu?"**
🚨 **HALÜSİNASYON — ve filmin öncülünü siliyor.** Plan (WORLD BIBLE ·
LIGHTING BIBLE · §0.13) her gece karesinde **yoğun, titreşimsiz yıldız
alanı + soluk galaksi bandı** şart koşar. Yıldızsız daire bir **yokluktur**:
yıldız alanı yoksa daire de yoktur. Raporun tarif ettiği "dark sky devoid
of stars" filmin novum'unun ekrandan silinmesi demektir. → **DERS 76.**

**2. "0:00 baştan sona sessizlik — tasarım mı, ses mi eksik?"**
TASARIM. `DIALOGUE LINES: 0 · SILENT SCENES: 18` (§0.15). Bulgu düşürüldü.
(Kurgu talimatı §0.18: bot/kumaş/nefes + S10'dan sonra sinyal — müzik ve
ses tasarımı ayrı geçiştir, klipte olmaması beklenir.)

**3. "0:08 gizli kesme — derleme sınırı olabilir mi?"**
HAYIR. `PLANNED CUTS: 0` · "single unbroken take" 36 promptun 36'sında.
Klip 10.0 s planlanmışken 12 s ölçüldü ve içinde ~15°'lik kamera sıçraması
var → **gerçek ihlal**, Ders 1/68 sınıfı.

**4. Cevap istemeyen ama daha ağır olan üç sapma** (rapor mod V olduğu için
"eksik" diyemezdi; belge karşılaştırması gösteriyor):

| Rapor ne gördü | Plan ne diyor | Sonuç |
|---|---|---|
| "Barren rocky landscape", boulder'a dokunma | Düz, sert, açık gri ova + ufka kadar **çanak dizisi**; kadın filmde **tam beş şeye** dokunur, kaya bunlardan biri değil | 🚨 klip kimliği şüpheli |
| "Opaque gold-tinted visor" | "one fully transparent seamless visor, **no tint, no coating**" | 🔴 ihlal → DERS 79 |
| "White base, charcoal accent panels" | kemik beyazı + **pas kızılı mühürlü dikişler** (ön kol + göğüs) | 🟠 ihlal |

⚠️ **Bu klibin bu filme ait olduğu doğrulanmadı.** 12 s (plan: 10 s), çanak
yok, yıldız yok, kayaya temas var. Operatör hangi dosyayı yüklediğini
doğrulayana kadar teknik satır ŞARTLI kalır.

### 📖 SENARYO_QA soruları

**Rapor GEÇERSİZ — sorular cevaplanmadan önce malzeme kapısı düştü.**
Mercek 12 saniyelik tek çekimi "film" sayıp on kategoriye puan verdi
(Yapı 3 · Final 3 · Tutundurma 4 · "no peak located" · "ends mid-stride").
Bunlar 174 saniyelik kurgunun değil, tek klibin özellikleri. → **DERS 75.**

Yine de iki soruya belge cevabı yazılır (tekrar koşuda kullanılmak üzere):
- **"Bağımsız kısa mı, viral ara mı?"** → Malzeme filmin S1/S3 sınıfı bir
  sahnesi; film 18 sahnelik bir bütün, viral aralar S3 · S6 · S16 · S17 ve
  **kesilemez** (§0.15).
- **"Plan bir doruk ilan ediyor mu?"** → EVET: **S9, ışık takası**
  (§0.6 · §0.15 CENTRAL CHOICE), bedeli S12'de görünür.

### 🧩 MANTIK_QA soruları

**1. "1:50 gece → 2:00 gündüz sıçraması: planlı zaman atlaması mı?"**
YARISI PLANLI, YARISI ÜRETİM KAYBI. Plan tek yönlü bir ışık ekseni yazar
(§0.11): S12 **PRE-DAWN** (sağ ufukta gri-mavi bant, kadın ışıksız yürür) →
S13 **DAWN** (güneş doğar, parıltılar sırayla yanar) → S14 MORNING. Yani
gece ile gündüz arasında **iki kademeli geçiş sahnesi planlanmıştı.**
Kurguda 1:50 hâlâ tam gece, 2:00 tam gündüz — **PRE-DAWN kademesi ekranda
yok.** Rapor doğru gördü: 🟠 MAJOR **ayakta kalır**, ama sebebi devamlılık
tasarımı değil, S12'nin ışık fazının üretilmemesi. Aynı sahne bedelin
görüldüğü sahnedir (aşağıya bak) — iki kayıp tek sahnede.

**2. "S15'te iki özdeş astronot: klon filmi mi, halüsinasyon mu?"**
🔴 **GERÇEK KLON İHLALİ.** `HUMAN COUNT LOCK: tam 1 insan` (§0.12); negatif
çekirdek ayrıca "no second person, no clone, no figure in any reflection,
no statue or silhouette shaped like a person" der. Dahası klon **planın
S14 BİNİŞ sahnesinde** çıktı — **DERS 69'un yasakladığı sahne tipinin ta
kendisi** ("biniş/iniş hareketi hiçbir segmentte kadraja alınmaz").
DERS 69'un üçüncü vakası (Stone Sky araçtan iniş · Unbroken City loş iç
mekân · burada gemi binişi) ve ilk kez **ders yazıldıktan bir gün sonra
plana eklenen sahnede.** → **DERS 77.**

**3. "Silindir, alet duvarı, mercek kutusu: nedensel zincir mi, doku mu?"**
ÜÇÜ DE PLANLI ÇEHOV HALKASI — ama ikisi yanlış okunmuş:

| Raporun gördüğü | Planda ne | Ödeme nerede |
|---|---|---|
| S4 "ribbed cylinder" | dış kuşak pilonu / kaide halkası — **ÇEHOV 1: yedi oluklu bant** (S2) | S11: parmak havada aynı deseni izler |
| S6 "tool wall" | **ÇEHOV 2: bakım körfezi** — kapanışın kasıtlı olduğunun kanıtı | ödeme S8'de boş beşik (kararla bitmiş bekleyiş) |
| S11 "case with a mirror/lens" | 🎯 **DORUK: güç hücresinin beşiğe oturtulması** (S9) | S9 8.5 s: iş lambası uyanır · S10 taneler zıplar |
| S12 "glowing particles on a pan" | **membran taneleri** — sinyalin görsel kanalı, 7 vuruş / 6 s | S13: gün ışığında hâlâ yanan lamba |

Yani **"terk edilmiş prop" diye raporlanan dört şeyin dördü de filmin
anlatı omurgası.** Mercek zinciri göremedi çünkü zincirin iki ucu (oluk
deseni ↔ vuruş ritmi, hücre ↔ boş yuva) **hiçbir karede yan yana gelmiyor.**
🟠 "Abandoned discovery" bulgusu bu haliyle **ayakta kalır** — kurgunun
değil, anlatım kanalının kusuru. → **DERS 78.**

**4. "Kara kürenin yükselmesi (0:30 → 1:00) tutarsızlık mı?"**
HAYIR — **SAYAÇ C planlı**: dairenin yüksekliği mesafeyi gösterir
(S0'da 58°, S6'da 82°, merkezde zenit). 🟡 MINOR bulgu **DÜŞER.**
⚠️ Ama raporun kullandığı kelime asıl bulgudur: **"black sphere"**. Daire
bir **küre/cisim** olarak render edilmiş; plan "a black disc of absence…
never glowing, never outlined, not an eclipse, not a planet" diyor. Yokluk
nesneye dönüşmüş → **DERS 76.**

### 🧍 KARAKTER_QA soruları

**1. "Vizör açık/aynalı geçişleri: akıllı cam tasarımı mı?"**
HAYIR. Character Bible: "one fully transparent seamless visor, **no tint,
no coating**, no mask or regulator beneath it, her whole face clearly
readable through it" + `HELMET STATE SCHEDULE: kapalı 15/15, ara durum yok`.
🟠 MAJOR **ayakta kalır ve büyür**: raporun tablosunda yüz 14 sahnenin
yalnız 3'ünde okunuyor; plan 15'inde okunmasını şart koşuyor. Aynalı vizör
modelin astronot ön-yargısıdır ve bible'daki olumsuz cümle onu durdurmadı.
→ **DERS 79.**

**2. Pasaportun belgeyle karşılaştırmasından çıkan üç ek bulgu**
(mod V bilemezdi — Unbroken City'deki üç bulgunun ikisi birebir tekrar):
- **"life-support backpack"** → Bible AÇIKÇA yasaklıyor: "No back-mounted
  tank, no hose, no cable." **İki filmde üst üste aynı ihlal.** → DERS 79.
- **"no specific asymmetric damage"** → Bible'ın SABİT yıpranma izleri (sağ
  kalça plakasında gri sürtme, iki incikte soluk toz, sol eldiven
  boğumlarında mat çizik) üretilmemiş. İkinci tekrar.
- **Pasaportta güç hücresi de, BOŞ KALÇA YUVASI da yok.** Filmin bedeli
  tam olarak budur: S0-S8 hücre takılı, S10-S14 "cradle EMPTY, clamp
  standing open". Karakter merceği 14 sahne boyunca kalçaya hiç bakmadı —
  çünkü orada bakılacak bir şey üretilmemiş. Doruk ekranda VAR, bedeli YOK.
  → **DERS 78.**

---

## 📊 KATEGORİ SKORLARI

**🔧 Teknik (Ⓥ ŞARTLI · 12 s klip):** Karakter 7 · Fizik 5 · Kamera 2 ·
Işık 8 · Çevre 6 · Canlı N/A · Parçacık 4 · Hareket 8 → **5.7/10** —
1 BLOCKER: 0:08 gizli kesme. Ayrıca 0:04 asılı toz (PARTICLE GRAVITY LOCK
sayısal kilidi tutmadı), 0:11 eldiven-kaya kaynaşması (Ders 11/43).

**📖 Senaryo:** 🚨 GEÇERSİZ — malzeme kapısı (12 s ≠ film). Tabloya üstü
çizili girer, ortalamaya katılmaz. Tekrar koşusu: **tam kurgu + BÖLÜM 0.**

**🧩 Mantık:** Fizik 8 · Sayaç **N/A** · Coğrafya 6 · Zaman-Işık **3** ·
Kostüm-Prop 7 · Nedensellik 4 · Nicelik **1** · Kurulum 3 → **5.5/10**

**🧍 Karakter:** Yüz 9 · Saç-Beden 9 · Kostüm 8 · Yıpranma 9 · Ekipman **4**
· Kesme 8 · Sayı **1** · Ses N/A → **6.0/10** · IDENTITY BREAK

> ⚠️ Klon bulgusu iki tabloda da 1/10 olarak duruyor (Nicelik ve Sayı) —
> bu, iki rubriğin aynı olayı kendi dilinde ölçmesidir, çift sayım değil.
> Birleştirmede **tek bulgu** sayılır (kart E2 adım 5).

---

## 🚪 KURGU KAPISI — teslimden önce koşulmalıydı (DERS 70/72)

| Ölçüt | Plan | Kurgu | Sonuç |
|---|---|---|---|
| Klip sayısı = SCENE COUNT | 18 | 18 (+1 kart) | ⚠️ raporun ilk iki satırı (0:00-0:05 / 0:06-0:09) tek sahnenin iki okuması olabilir — klip envanteriyle doğrulanmalı |
| Süre = RUNTIME ±2 s | 180 s | 174 s | ❌ −6 s |
| Ekran metni 0.0 sn | 0 | **4 s** (2:50-2:54) | ❌ |
| CENTRAL CHOICE kurguda | S9 | var (1:30-1:49) | ⚠️ var ama okunmuyor |

🚨 **Yanık başlık kartı "THE CIRCLE WITH NO STARS" filmin adı bile değil —
bu dosyanın KAPAK PROMPTU A sürümünün kendi bölüm başlığıdır** (satır 3384:
`SUBJECT — THE CIRCLE WITH NO STARS:`, iki satır üstünde "NO TEXT ANYWHERE
IN THE IMAGE" yazarken). **Unbroken City ile birebir aynı mekanizma, iki
film üst üste:** kapak promptunun başlığı görsele basıldı ve kapak çıktısı
kurguya kapanış kartı olarak girdi. → DERS 72'ye ikinci vaka işlendi.

## 🚪 ÜRETİM KAPILARI — kaydı yok (DERS 74)

Film dosyası üç kapı tanımlıyordu ve üçünün de sonucu hiçbir yere
yazılmamış:

| Kapı | Ölçüt | Kurguda görünen |
|---|---|---|
| KAPI 1 — GECE TESTİ (S1) | zemin karanlık ama okunur · tek ışık lamba havuzu · yıldız alanı sabit · gemi ışıksız | kısmen tuttu (gece sahneleri okunur), ama 🔧 klibinde gök yıldızsız |
| KAPI 2 — DAİRE TESTİ (S0) | daire keskin kenarlı ve BOŞ · parlamıyor · konumu sabit | **BATTI** — daire "black sphere" olarak çıktı; Plan B (daireyi yalnız S0/S6'da tut) devreye alınmamış |
| KAPI 3 — TOZ TESTİ (S10) | taneler ayrık · ≤2 mm zıplayıp düşüyor | okunamadı — mercek "glowing particles on a pan" gördü, ritim yok |

**Kaydı olmayan kapı koşulmamış sayılır** (DERS 74). Bu filmde kapı kaydı
yoktu ve kapı-sonrası bütün adımlar (15 sahne + kurgu + 4 QA merceği) yine
de koşuldu. DERS 74'ün **ikinci vakası ve yatay hattaki ilki.**

---

## 🧭 SONUÇ VE SONRAKİ ADIM

```
1. ⛔ ÖNCE ŞUNU DOĞRULA: 🔧 ve 📖 merceklerine hangi dosya yüklendi?
   12 s · çanaksız · yıldızsız · kayaya temas — bu klibin bu filme ait
   olduğu belgeyle uyuşmuyor. Yanlış dosyaysa iki satır da silinir.
2. 📖 SENARYO_QA tam kurgu (174 s) + BÖLÜM 0 ile TEKRAR koşulur.
   Geçersiz satır ancak o zaman değişir.
3. 🔴 2:50 başlık kartı kurgudan çıkarılır (kapak çıktısı ayrı dosyadır) —
   4 saniye, sıfır maliyet, DERS 72'nin ikinci vakasını kapatır.
4. 🔴 S14 (biniş) yeniden üretilir — DERS 69 ①'e göre biniş HAREKETİ
   kadraj dışına alınır: kadın ya yerde ya kapak eşiğinde; merdiven
   tırmanışı gösterilmez. Kurgu kurtarması: iki figürlü kadraj kesilir.
5. 🔴 S12 (PRE-DAWN) yeniden üretilir — hem gece→gündüz sıçramasını
   kapatır hem bedeli (boş kalça yuvası, açık kelepçe) ekrana getirir.
   Bu tek sahne iki merceğin üç bulgusunu birden düşürür.
6. 🟠 Vizör: aynalı/renkli vizör içeren bütün klipler yeniden üretim
   adayı; DERS 79 cümlesi negatif çekirdeğe girmeden tekrar denenmez.
7. 🟠 Yıldızsız daire: KAPI 2 sonucu kayda geçirilir. Daire nesneleşmeye
   devam ederse plan dosyasındaki Plan B uygulanır (daire yalnız S0/S6).
8. Yeni dersler: DERS 75-79. Tekrar kayıtları: DERS 69 (3. vaka) ·
   DERS 72 (2. vaka) · DERS 74 (2. vaka).
```
