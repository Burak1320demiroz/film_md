# 🔍 THE RING WALKER — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_RING_WALKER/THE_RING_WALKER_MOON_FILM.md`
> **İki QA geçişi var:**
> - **TEKNİK (VIDEO_QA)** — 5/10 · ham rapor ❌ kayıp · veri `LESSONS_LEARNED.md` Ders 30-32'den geri çıkarıldı
> - **SENARYO (SENARYO_QA)** — 5/10 · ham rapor ✅ `../02_HAM_RAPORLAR/THE_RING_WALKER_SENARYO_HAM.md` (31.07.2026)
>
> Bu, projede **iki farklı rubrikle ölçülmüş ilk film.**

---

# 🎥 BÖLÜM A — TEKNİK QA (VIDEO_QA)

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Full (tam film)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    5/10
TASARIM KARARI: filmde canlı YOK — "canlı yok = düşük risk" hipoteziyle üretildi
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 5/10 | |
| Fizik | 4/10 | parçacık yerçekimi + çarpma fiziği |
| Kamera | 4/10 | |
| Işık | 5/10 | |
| Çevre | 5/10 | |
| Canlı | N/A | bilinçli olarak yok |
| Hareket | 4/10 | |
| Ölçek | 4/10 | ⚠️ Ders 32'nin kaynağı — **tabloda ayrı sütun yok** |
| Parçacık ve Malzeme | ⛔ kayıt yok | parçacık filmi — kritik kategoriydi |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

---

## 🧪 ÜRETTİĞİ DERSLER — 3 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 30 | Parçacık yerçekimi kilidi — küçük parçalar yüzüyor | 4/10 fizik |
| 31 | Çarpma fiziği — düşük yoğunluklu etkiler | 4/10 fizik, 5/10 çevre |
| 32 | Gemi/yapı ölçek tutarlılığı — oranlar değişiyor | 4/10 ölçek |

---

## 📌 ÇÜRÜTÜLMÜŞ HİPOTEZ ✅

> *"Ring Walker'ın 'canlı yok = düşük risk' hipotezi Fizik ve Hareket
> skorlarını yükseltmedi — parçacık fiziği yeni darboğaz."*

**Bu, projedeki tek açıkça test edilip çürütülmüş hipotez.** Bir zorluk kaynağı
(canlı) tamamen kaldırıldı, puan değişmedi. Sonuç: hata bütçesi kaynak
kaldırılınca yok olmuyor, başka kategoriye kayıyor.

---

## 🏆 SONRADAN DOĞRULANAN BAŞARI

Ders 32 (ölçek), Bible'da **sayısal olarak** kilitlendiğinde (24m / 6 derece)
The Slow Stone'da **hiç tetiklenmedi.** Bu, "sayısal kilit çalışır, tarif kilidi
çalışmaz" bulgusunun iki kanıtından biri.

---

## ⚠️ BU KAYDIN EKSİKLERİ (yalnızca teknik geçiş)

```
□ Ham QA raporu yok
□ ⛔ "Ölçek" kategorisi kalite tablosunda sütun olarak YOK — Ders 32'nin
  kaynak skoru hiçbir tabloda görünmüyor
□ ⛔ PARÇACIK kategorisi ölçülmemiş — oysa kayıtlı sonuç "parçacık fiziği
  yeni darboğaz" diyor. Darboğaz olarak ilan edilen kategori ölçülmemiş.
□ Diğer 3 rubrik kategorisi kayıt dışı
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** Orta öncelik — ama tablo yapısı **kesinlikle**
düzeltilmeli: darboğaz ilan edilen kategorinin sütunu yok.

---

# 📖 BÖLÜM B — SENARYO QA (SENARYO_QA)

## 📋 KÜNYE

```
RUBRİK:        SENARYO_QA_CRITIQUE_PROMPT.md — 10 kategori
QA TARİHİ:     31 Temmuz 2026
GİRDİ:         yalnızca video (doküman verilmedi)
SPEC BLOĞU:    KISMİ — logline, tema ve merkezi seçim videodan çıkarıldı
SÜRE:          115 saniye
GENEL SKOR:    5/10
KARAR:         SHOOT WITH TRIMS
GEÇERLİLİK:    ⚠️ ŞARTLI — izlenen kurgu plandan sapıyor (bkz. Bulgu 1)
               Rapor dürüst ve ekranda olanı ölçüyor; sorun girdide.
HAM RAPOR:     ✅ ../02_HAM_RAPORLAR/THE_RING_WALKER_SENARYO_HAM.md
```

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Kanca (Hook) | 5/10 | Güzel bir YER kuruyor ama SORU sormuyor |
| Önerme ve Anlaşılırlık | 6/10 | Tek cümlede anlatılabiliyor |
| Yapı ve Tempo | 5/10 | Orta bölüm tekrarlı zemin incelemesinde takılıyor |
| Karakter | 4/10 | ⚠️ **En düşük** — gözlemci, eyleyen değil |
| Tema | 6/10 | Sessiz hayret geçiyor ama tema estetik kalıyor |
| Diyalog | 7/10 | ⭐ **En yüksek** — sıfır replik, sıfır kendi kendine anlatım |
| Duygusal Yay | 5/10 | Yükseliş var, karakter tepkisi düz |
| Final | 6/10 | Lander'a dönüş döngüyü temiz kapatıyor |
| Özgünlük | 4/10 | ⚠️ Tanıdık bilimkurgu görüntüsü |
| Retention Risk | 4/10 | ⚠️ 0:25'te yüksek terk riski |

## 🩸 FİLME EN ÇOK ZARAR VEREN 3 ŞEY

```
0:00–0:15  AÇILIŞTA ACİLİYET YOK
           Muhteşem bir ortam var, anlatısal soru yok → erken kaydırma riski
0:20–1:05  TEKRARLI KEŞİF BEAT'İ
           Kuma/kristale diz çöküp dokunma ÜÇ ayrı kez, tırmanma olmadan
1:12       PASİF PROTAGONİST
           Meteor tam önüne düşüyor; şaşkınlık ya da bedensel gerilim yok
```

## 🛡️ KORUNACAK 3 ŞEY

```
1:00–1:08  PARLAYAN KUM DÖKÜMÜ — filmin görsel çapası
1:20–1:35  METEOR YAĞMURU DORUĞU — gereken görsel tırmanma
1:40–1:50  LANDER'A DÖNÜŞ — keşif döngüsünün somut kapanışı
```

**Paylaşılabilir an:** `1:02–1:06` — eldiven parmaklarından akan çok renkli
parçacıkların dev halka gökyüzü önündeki yakın çekimi.

**Başka hiçbir şeyin yapmadığı tek şey:** dokunulabilir, mücevher gömülü ay
jeolojisi + tehdit içermeyen, tamamen huzurlu bir meteor olayı.

## 🔪 SAHNE KARARLARI

> ⚠️ **Numaralandırma uyarısı:** Aşağıdaki S1-S10, **eleştirmenin video
> zaman kodundan kendi çıkardığı** bölümlemedir. Prodüksiyon dokümanının
> 13 sahnesiyle (S0, S1, S2, S2.5, S3…S9.5, S10) **birebir eşleşmez.**
> Doküman verilmediği için eşleme yapılamadı.

| # | Zaman | Karar | Not |
|---|---|---|---|
| S1 | 0:00–0:10 | KEEP | Ortam ve ölçek iyi kuruluyor |
| S2 | 0:10–0:20 | KEEP | Parlayan zemin mekaniği tanıtılıyor |
| S3 | 0:20–0:30 | TIGHTEN | Yürüyüş süresi kısaltılmalı |
| S4 | 0:30–0:40 | MERGE | S3 ile birleşsin — çift diz çökme kalksın |
| S5 | 0:40–0:50 | KEEP | Ölçek ve kadraj değişimi iyi |
| S6 | 0:50–0:57 | **CUT** | Ayak izi kristal beat'inden sonra tekrar |
| S7 | 0:58–1:09 | KEEP | Filmin en güçlü görsel beat'i |
| S8 | 1:10–1:19 | **REWRITE** | Astronot olayı takip etmeli/tepki vermeli |
| S9 | 1:20–1:39 | TIGHTEN | Uzun pozlama çizgi kareleri azaltılsın |
| S10 | 1:40–1:55 | KEEP | Döngüyü kapatıyor |

**30 saniyelik kesim listesi:** S6 (7s) → S3/S4 birleştirme (13s) → S9 kırpma (10s)

**Terk noktaları:** `0:15` hedefsiz keşif · `0:35` üçüncü zemin incelemesi ·
`1:32` duran ışık-çizgisi montajı

## ✍️ YENİDEN YAZIM REÇETELERİ

```
S3+S4   Tek 5 saniyelik beat'te birleştir — ilk adımda kristalleri keşfetsin,
        ikinci diz çökme olmasın
S8      Meteor çarpmasında geri adım / koruyucu kol → bedensel varlık ve içgüdü
S1      İlk 3 saniyede bilek konsolu sesi veya hedef işareti → yürüyüşe amaç
```

---

## 🚨 BU RAPORDAN ÇIKAN 4 SİSTEM BULGUSU

### 1. 🚨 FİLMİN İLAN EDİLMİŞ DUYGUSAL ZİRVESİ EKRANDA YOK

Bu, raporun kendisinden daha önemli bir bulgu.

| | Plan dosyası | İzlenen video |
|---|---|---|
| Süre | **129 s** (9s hook + 12×10s) | **115 s** |
| Sahne | **13** (S0, S1, S2, S2.5, S3-S9, S9.5, S10) | ~10 zaman bloğu |
| 1:09–1:29 | **TUTULMA (S7-S8)** | meteor çarpması + meteor yağmuru |
| S9 — meteorit parçasının sırrı | var | ❌ görünmüyor |

Plan dosyası tutulmayı iki ayrı yerde **filmin duygusal zirvesi** ilan ediyor:

> *"MÜZİK ANAHTARI: Tutulma sahnesi (S7-S8) — sıcak yıldız tınısının kesilmesi
> ve geri dönüşü = filmin duygusal zirvesi"* — `THE_RING_WALKER_MOON_FILM.md:1221`

**Yani film, kendi zirvesi olmadan monte edilmiş.** Rapor bunu bilemezdi —
yalnızca video verildi. Sonuç:

```
Duygusal Yay 5/10  →  hikayenin değil, EKSİK KURGUNUN puanı
Yapı 5/10          →  "orta bölüm tekrarlı" bulgusu, tutulma çıkarılınca
                      geriye sadece keşif beat'leri kaldığı için oluşmuş olabilir
```

⚠️ Bu yüzden hikaye tablosundaki satır **ŞARTLI** işaretlendi. Tutulmalı
kurgu ölçülmeden bu iki puan hikayeye atfedilemez.

**Asıl aksiyon rapordaki kesim listesi değil:** önce tutulma sahnelerinin
neden montaja girmediği bulunmalı (üretilmedi mi, üretildi de düştü mü?).

### 2. Süre, hem plandan hem format tabanından düşük

```
PLANLANAN       129 s
FORMAT TABANI   2-4 dk = en az 120 s
GERÇEK SÜRE     115 s          → plandan 14 s, format tabanından 5 s aşağıda
30 s KESİMDEN SONRA  ~85 s     → bu artık 2-4dk değil, shorts uzunluğu
```

Kayıp 14 saniye ile eksik tutulma sahneleri büyük olasılıkla **aynı olayın
iki yüzü.**

Kesim listesi **olduğu gibi uygulanamaz.** Ya kesilen süre yeni içerikle
(kanca + karakter seçimi) geri konur, ya film bilinçli olarak dikey/shorts
formatına taşınır. Üçüncü seçenek yok.

### 3. Raporda "title card" görünüyor — Ders 34 ile çakışıyor

S10 notu: *"Return to lander & title card."* `LESSONS_LEARNED` **Ders 9**
(videoda yazı olmamalı) ve **Ders 34** (jenerik metni halüsinasyonu) bunu
yasaklıyor. Kartın montajda bilinçli eklenip eklenmediği **doğrulanmalı** —
model uydurduysa bu bir Ders 34 tekrarıdır.

### 4. En yüksek puan, yazılmayan şeyden geldi

Diyalog 7/10 — filmde **sıfır replik** var. Bu, serinin en yüksek hikaye
kategori puanı. Aynı anda Dead Approach'un teknik çöküşü (3/10) **diyaloglu**
ilk üretimde gerçekleşti. İki rubrik aynı yöne işaret ediyor: **replik
eklemek bu seride hem teknik hem hikaye riskini birlikte artırıyor.**

---

## 📌 İKİ RUBRİĞİN ÇAPRAZ OKUMASI

| | Teknik QA | Senaryo QA |
|---|:---:|:---:|
| Genel skor | 5/10 | 5/10 |
| Karakter | 5/10 (görsel tutarlılık) | 4/10 (seçim / iç dünya) |
| İlan edilen darboğaz | parçacık fiziği | karakter etkinliği |

Aynı film, aynı puan, **farklı sebep.** Teknik kilitleri sıkılaştırmak bu
filmin hikaye puanına dokunmuyor. Ring Walker'ın çürütülmüş "canlı yok =
düşük risk" hipotezinin hikaye tarafındaki karşılığı: **zorluk kaynağını
kaldırmak (canlı/tehlike/diyalog) hata bütçesini yok etmiyor, karakter
etkinliğine kaydırıyor.**
