# 🔍 THE SLOW STONE — BİRLEŞİK QA RAPORU

> **QA Tarihi:** 30 Temmuz 2026
> **Girdi:** 4 rapor — eski tekil-klip promptu (Rapor 0) + 3 Geçişli QA Sistemi (Geçiş 1/2/3)
> **Planlanan:** 48 sahne × 10s = 480s · **Gerçek:** 455s (07:35) — **25 saniye eksik**

---

## ⚠️ ÖNCE BU: RAPORLARIN GEÇERLİLİK SINIRI

Dört rapor da **SPEC bloğu boş** çalıştırıldı. Bu, sonuçların ne anlama geldiğini
kökten değiştiriyor ve rapor okunmadan önce bilinmeli.

### 1. Format uyuşmazlığı — QA promptu yanlış filme uygulandı

QA promptları **5 faz × 12 sahne × 8s = 60 sahne** varsayımıyla yazılmıştı.
The Slow Stone ise **4 kısım × 12 sahne × 10s = 48 sahne**.

Sonuç: Geçiş 2 ve Geçiş 3, **var olmayan bir "Faz 5 (sahne 49-60)" için puan verdi.**

```
Geçiş 2 → "5 Çözülme | 49-60 | Face 85% | Final close-ups maintain core identity"
Geçiş 3 → "F5 ÇÖZÜLME 6:24-end | intensity 9 | ends higher than F1"
```

Bu sahneler **yok**. İki model de eksik yapıyı bildirmek yerine doldurdu.
Hata bende: prompt şablonu yapıyı parametre değil sabit olarak yazmıştı.
→ Üç prompt da düzeltildi (aşağıda).

### 2. Geçiş 2'nin karakter yargısı Bible'a karşı DOĞRULANMADI

Geçiş 2, referans temelini **videodan** kurdu ("baseline inferred from video").
Bu, tanım gereği sadece **kendi içinde tutarlılığı** ölçebilir — Bible'a
uygunluğu ölçemez. "Identity holds, 7/10" hükmü bu yüzden bir uygunluk belgesi değil.

Somut kanıt — Bible'daki yüz işaretleri hiç kontrol edilmedi:

| Bible (kelimesi kelimesine sabit) | Geçiş 2 ne dedi |
|---|---|
| Sol burun kanadında küçük eski delik izi | Hiç bahsetmedi — yerine "freckles across the nose bridge" gördü |
| Alt dudakta dikey çatlak | Hiç bahsetmedi |
| Şakaklarda birkaç gri tel | Hiç bahsetmedi |
| Dış göz köşelerinde belirgin gülme çizgileri | Hiç bahsetmedi |

→ **Yüz uygunluğu hâlâ bilinmiyor.** Geçiş 2 dolu SPEC ile tekrar çalıştırılmalı.

### 3. Mineral birikim geri sayımı ölçülemedi

Bu filmin imzası, Bible'ın "filmin GERİ SAYIMI" dediği kısım-kısım artan
mineral kabuk (K1 temiz → K4 eldiven ve kask üstünde kalın kabuk).
Geçiş 2 bunu SPEC'siz gördüğü için **kasıtlı ilerlemeyi "istenmeyen sürüklenme"
sandı** ("slight suit weathering variations", Kostüm 7/10).

→ Filmin ana anlatı aracının ekranda okunup okunmadığı **hâlâ cevapsız.**
Bu, tüm QA'nın en önemli açık sorusu.

### 4. Rapor 0 kullanılamaz — yanlış prompt

Eski tekil-klip promptu (`VIDEO_QA_CRITIQUE_PROMPT.md`) yüklenen her şeyi
**tek kesintisiz çekim** sayar. Kurgulanmış 48 sahnelik filme uygulanınca
en kritik hatasını uydurdu:

```
Rapor 0 → "Camera 3/10 — Severe violation of single-cut rule (hundreds of cuts)"
          "0:10 — Camera cuts immediately, completely violating Single-Cut rule"
```

Bu **yanlış pozitif**. Bu formatta sahneler arası kesme kasıtlıdır.
Aynı videoyu formatı bilen Geçiş 1, Sahne Bütünlüğü'ne 6/10 verdi ve tek
gerçek bulgu 0:12'deki gösterge titremesiydi. Aynı şekilde Rapor 0'ın
"handheld tools in character's hands" ihlali de yanlış — kazıyıcı bu filmin
Çehov nesnesi.

> **Ders:** kurgulanmış filme tekil-klip QA promptu uygulanmaz. 3 geçişli
> sistemin var olma sebebi tam olarak budur ve ilk testte kendini kanıtladı.

---

## 📊 GEÇİŞ SKORLARI

| Geçiş | Kapsam | Skor | 🔴 | 🟠 | 🟡 | Güven |
|---|---|:--:|:--:|:--:|:--:|---|
| 1 — Teknik Bütünlük | Görüntünün kendisi | 4/10 | 4 | 3 | 2 | **Yüksek** — SPEC'e az bağımlı |
| 2 — Devamlılık & Karakter | İnsan + süreklilik | 7/10 | 0 | 4 | 3 | **Düşük** — Bible'sız çalıştı |
| 3 — Anlatı, Ritim & Ses | Seyirci deneyimi | 7/10 | 0 | 3 | 2 | **Orta** — novum kaçtı |
| **FİLM GENEL** | | **5/10** | **4** | **10** | **7** | |

**KARAR: DÜZELTME GEÇİŞİ + 4 SAHNE YENİDEN ÜRETİM**

---

## 🔗 İKİ KRİTİK KESİŞİM — hiçbir geçişin tek başına göremediği

Bu iki bulgu üç raporu Bible'la çakıştırınca ortaya çıktı. Raporlardaki en
değerli bilgi bunlar ve hiçbiri tek bir geçişte görünmüyor.

### 🔴 KESİŞİM 1 — Novum'un gösterildiği sahne, doku morphu ile bozulmuş

```
Bible:     "NOVUM ✅ Tek cümle, görsel, S9'da"        → S9 = 1:20-1:30
Geçiş 1:   "1:22.0 — 🔴 — Rock texture visibly morphs and swims
            as the scraper tool interacts with it"
Geçiş 3:   Novum'u yanlış okudu — "statues that mimic human forms
            and react to energy/ignition"
```

Filmin tek novum'u S9'da **bir kez** gösteriliyor ve o sahnede kazıyıcının
değdiği yüzey eriyor. Geçiş 3 filmi izledikten sonra novum'u yanlış anlattı:
"hareket birikimi engeller, bu yüzden karakter duramaz" kuralını —
**filmin tema cümlesini** — hiç fark etmedi.

> Geçiş 3'ün Kavrama puanı 8/10 idi; SPEC olsaydı bu **4/10** olurdu.
> Novum ekranda kaldı ama okunmadı. S9 yeniden üretilmeli — bu tek sahne
> filmin anlaşılıp anlaşılmadığını belirliyor.

### 🔴 KESİŞİM 2 — Kaskın çıktığı sahne hem ölü nokta hem de cilt çöküşü

```
Plan:      S21 = KASK ÇIKIYOR — "İlk çıplak nefes"      → S21 = 3:20-3:30
Geçiş 3:   "03:10-03:50 — 40s dead spot — folding fabric and sleeping"
           "İlk sıkıldığım an: 03:30"
Geçiş 2:   "03:25.0 — Helmet removal reveals skin noticeably MORE
            AIRBRUSHED than the cockpit close-up at 0:13"
```

Filmin en mahrem beat'i — 9 yıllık yalnız uçuşun ardından ilk çıplak nefes —
seyircide **can sıkıntısı** üretti ve tam yüzün ilk kez açıldığı anda cilt
plastikleşti. Bible o yüz için "görünür gözenek dokusu, doğal yüzey altı
saçılma" diyor; ihlal edilen şey doğrudan Character Bible.

> İki farklı geçiş, aynı 10 saniyeyi iki ayrı sebeple işaretledi.
> S21 filmin duygusal ödemesi ve şu an ödemiyor.

---

## 🗺️ KISIM BAZLI ISI HARİTASI

> ⚠️ Film 25 saniye kısa olduğu için gerçek sahne sınırları plandan
> giderek geriye kayıyor; sondaki zaman damgaları ±20s toleranslı.

| Kısım | Sahne | Zaman | 🔴 | 🟠 | En ağır hata |
|---|---|---|:--:|:--:|---|
| 1 DÜŞÜŞ | S1-S12 | 0:00-2:00 | 1 | 2 | **S9 novum sahnesinde doku morphu** |
| 2 YAŞAM ALANI | S13-S24 | 2:00-4:00 | 0 | 3 | S21 ölü nokta + cilt plastikleşmesi |
| 3 KEŞİF | S25-S36 | 4:00-6:00 | 1 | 3 | Yüzen kırıntı + oluşum içinde bloom |
| 4 TAMİR/GİDİŞ | S37-S48 | 6:00-7:35 | 2 | 2 | Zemin kırılmıyor, morph ediyor |

---

## 📋 BİRLEŞTİRİLMİŞ HATA KAYDI (tekilleştirilmiş)

| Zaman | Şid. | Bulgu | Kaynak | Ders eşleşmesi |
|---|:--:|---|---|---|
| 0:12 | 🟡 | Gösterge ışıkları titriyor/warp | G1 | Ders 33 |
| 0:35 | 🟠 | Egzoz dağılmıyor, katı koni geometrisi | G1 | **yeni — tek seferlik** |
| 0:44 | 🟠 | Toz sıvı gibi kıvrılıyor + kanattan geçiyor | G1 | **Ders 39** + Ders 11 |
| **1:22** | 🔴 | **Kazıyıcı değdiği kayayı eritiyor (S9 = novum)** | G1 | **DERS 43 (yeni)** |
| 2:20 | 🟠 | Göğüs göstergesi 3-nokta → kare ızgara | G1·G2·R0 | Ders 8 · Ders 33 |
| 2:22 | 🟠 | Kazıyıcı duvara giriyor (phasing) | G1 | Ders 11 |
| 2:51 | 🟠 | Çekirdek tutarken el/parmak deformasyonu | G2·R0 | **Ders 11/28** PERSISTENT |
| 3:25 | 🟡 | Kask çıkınca cilt airbrush — Bible ihlali | G2 | Ders 33 |
| 3:10-3:50 | 🟠 | 40s ölü nokta (S21 çevresi) | G3 | **yeni — anlatı** |
| 4:15 | 🟠 | Tekrarlayan kazıma, tempo düşüşü | G3 | anlatı |
| **4:42** | 🔴 | **Kırılan kristal yukarı süzülüyor + alet jello** | G1·R0 | **Ders 30** + DERS 43 |
| 4:46 | 🟠 | Göğüs amblemi kazıma sırasında warp | G2 | **DERS 43 (yeni)** |
| 5:21 | 🟠 | Oluşum içinde parlama halesi | G1·R0 | **Ders 29 · Ders 41** |
| 6:10 | 🟡 | ECU'da yüz genişliyor | G2 | Ders 7 |
| 6:25 | 🟡 | Ayak izleri derinliksiz, boyanmış gibi | G1 | **DERS 43 (yeni)** |
| **7:05** | 🔴 | **Zemin parçalanmıyor, geometrik morph ediyor** | G1 | **DERS 43 (yeni)** |
| **7:30** | 🔴 | **"THE SLOW STONE" başlık metni ekranda** | G1 | **Ders 34** ⚠️ doğrula |
| Film boyu | 🟠 | Yaygın ağır çekim hissi | G1·R0 | **DERS 44 (yeni)** |
| Film boyu | 🟠 | Süre 455s — plandan 25s eksik | hesap | yapısal |

⚠️ **7:30 başlık metni:** Bu jenerik senin kurguda eklediğin bir başlık mı,
yoksa model mi uydurdu? Modelse Ders 34 tekrar etti demektir; senin
eklediğinse hata değil. **Bunu bana söylemen gerekiyor** — Ders 34'ün
"PERSISTENT" etiketi buna bağlı.

---

## 🎓 DERSE DÖNÜŞENLER

Eşik: 1 sahne → not · 2-3 sahne → faz dosyası · **4+ sahne veya 2+ kısım → yeni ders**

| Bulgu | Görülme | Karar |
|---|---|---|
| Etkileşim tetikli morph (1:22, 4:42, 4:46, 6:25, 7:05) | **5 sahne, 3 kısım** | ✅ **DERS 43** |
| Yaygın ağır çekim (0.7g) | **film boyu, 2 rapor** | ✅ **DERS 44** |
| Toz sıvı gibi (0:44) | 1 sahne | Ders 39 zaten var → PERSISTENT |
| El morphu (2:51) | 1 sahne | Ders 11/28 zaten var → PERSISTENT |
| Bloom (5:21) | 1 sahne | Ders 29 var — ama sözlüğe ekleme gerek (aşağıda) |
| Egzoz katı koni (0:35) | 1 sahne | Ders değil → Kısım 1 dosyasına negatif satır |
| Ölü nokta (3:10-3:50) | 1 bölge | Ders değil → kurgu düzeltmesi |
| Faz 5 halüsinasyonu | QA sistemi | Ders değil → **prompt düzeltildi** |

---

## 🛠 AKSİYON LİSTESİ

### A. Yeniden üretilecek sahneler (4)

| Sahne | Zaman | Sebep | Öncelik |
|---|---|---|:--:|
| **S9** | 1:20-1:30 | Novum sahnesi doku morphu ile bozuk — film buna bağlı | **1** |
| S43-44 | 7:00-7:10 | Kalkışta zemin morph ediyor, kırılmıyor | 2 |
| S28 | 4:40-4:50 | Kristal yukarı süzülüyor + alet jello | 3 |
| S21 | 3:20-3:30 | Cilt plastikleşmesi — yüzün ilk açıldığı an | 4 |

### B. Kurgu düzeltmesi
- **3:10-3:50 arası 20-25s kısalt.** S21'in kaskı çıkarma anı korunur, çevresindeki
  dinlenme/kumaş katlama tekrarları atılır. Bu aynı zamanda süreyi 480s'ye
  yaklaştırmaz — film zaten kısa, o yüzden kesilen süre S9 ve S21'in yeniden
  üretiminde geri kazanılmalı.

### C. Prompt güncellemeleri → `01_KISIM_1_DUSUS.md` … `04_KISIM_4_TAMIR_VE_GIDIS.md`
Ders 43 ve 44'ün negatif satırları (aşağıdaki ders metinlerinde birebir yazılı).

### D. Yeniden çalıştırılacak QA
- **Geçiş 2, dolu SPEC ile** — yüz uygunluğu ve mineral geri sayımı hâlâ ölçülmedi.
- **Geçiş 3, dolu SPEC ile** — novum kavrama puanı SPEC'siz 8/10 çıktı, gerçek değil.

---

## ✅ NE İYİ ÇALIŞTI — sonraki filmde korunacak

- **Işık/grade devamlılığı 9/10** (Geçiş 2). Üç ışık fazı (dış gündüz 4200K /
  istasyon içi 3500K / oluşum içi saçılma) sahneler arası tutarlı kaldı.
  4 kısımlık ışık planı işe yarıyor.
- **Ekipman durum mantığı 9/10** — kask S21'de bir kez ve doğru yerde çıkıyor,
  keyfi geçiş yok. **Ders 37 bu filmde tetiklenmedi.**
- **Kamera 7/10, sarsıntı yok** — sabit lockoff stratejisi ikinci kez kendini
  kanıtladı (Low Power'da 8/10 idi).
- **Ölçek kilidi 8/10** — TALLOW'un 24m ve 6 derece yatıklığı korunmuş görünüyor.
  Ders 32 bu filmde tetiklenmedi.
- **Sessiz oyunculuk** — üç rapor da fiziksel performansı ayrı ayrı övdü.
