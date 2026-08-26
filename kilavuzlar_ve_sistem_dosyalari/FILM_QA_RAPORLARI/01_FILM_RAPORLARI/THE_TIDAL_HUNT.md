# 🔍 THE TIDAL HUNT — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_TIDAL_HUNT/THE_TIDAL_HUNT_PLANET_FILM.md`
> **Bu filmde İKİ ayrı QA var:**
> · **TEKNİK QA** (aşağıda) — `LESSONS_LEARNED.md` kalite tablosu + Ders 17-19
> · **MANTIK QA** (31.07.2026) — **4.0/10** · [aşağıdaki bölüm](#-mantik-ve-devamlilik-qa--31-temmuz-2026) · ham çıktı: [`../02_HAM_RAPORLAR/THE_TIDAL_HUNT_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_TIDAL_HUNT_MANTIK_HAM.md)
> · Senaryo QA: ❌ henüz yapılmadı
>
> ⚠️ **Teknik QA'nın orijinal raporu dosya olarak mevcut değil.**

---

# 🔧 TEKNİK QA

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Montaj (compilation)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    3/10  ⚠️ serinin en düşük üç skorundan biri
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 3/10 | |
| Fizik | **2/10** | **serinin en düşük fizik skoru** |
| Kamera | 4/10 | |
| Işık | 4/10 | |
| Çevre | 3/10 | |
| Canlı | **2/10** | **serinin en düşük canlı skoru** |
| Hareket | 3/10 | |
| Parçacık ve Malzeme | ⛔ kayıt yok | |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

> **Not:** Bu filmin 7 kategorisinin 7'si de 4'ün altında. Tek kategori bile
> ortalamanın üstünde değil. Serideki tek "her yerde başarısız" QA'sı.

---

## 🧪 ÜRETTİĞİ DERSLER — 3 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 17 | Çarpışma fiziği — nesneler birbirinden geçiyor | 2/10 fizik |
| 18 | Canlı yürüyüşü — hayvanlar kayarak hareket ediyor | 2/10 canlı, 3/10 hareket |
| 19 | Yansıma tutarlılığı — su yansımaları eşleşmiyor | 4/10 ışık |

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok
□ 4 rubrik kategorisi kayıt dışı
□ 3/10 alan bir filmden neden sadece 3 ders çıktığı açıklanmamış —
  Canopy World 4/10 aldı ve 8 ders verdi. Ders çıkarma sistematik değil.
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** Evet — **öncelikli.** Seride avcı canlı + su + hareket
üçlüsünü barındıran tek film ve üçünde de dipte. Canlı puanı 2/10'dan beri hiçbir
filmde tekrar ölçülmedi (sonraki filmlerin çoğunda canlı yok).

## 🆕 MANTIK QA'DAN GELEN TEKNİK BULGULAR (31.07.2026)

Mantık raporu kapsam dışı bulgularını doğru şekilde ayrı listeledi. Üçü de
bu filmin **mevcut derslerine ilk kez zaman damgası veriyor** — bu kaydın
en büyük eksiği "ham veri yok" idi, kısmen kapandı:

| Zaman | Bulgu | Ait olduğu ders |
|---|---|---|
| 0:14 / 0:54 | Yengeç kayaya çarpıyor ↔ yaratık bacaklardan geçiyor | **Ders 17** — çarpışma fiziği |
| 1:13 | Kırmızı kuşlar bulanık kütleye dönüşüyor | **Ders 18** — canlı morphu |
| 1:30 | Leviathan dalgayla akışkan etkileşmiyor | Ders 24 / 31 |
| 1:03 | Yüzde "jello" morphu | Karakter 3/10 — timestamp'i yoktu |

> 0:14 ve 0:54 aynı filmde **çarpışmanın hem çalıştığı hem çalışmadığı**
> iki kare. Ders 17 buradan çıkmıştı; artık nerede olduğu da kayıtlı.

---
---

# 🧩 MANTIK VE DEVAMLILIK QA — 31 Temmuz 2026

> **Prompt:** `../../QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Ham çıktı + doküman kontrolü cevapları:** [`../02_HAM_RAPORLAR/THE_TIDAL_HUNT_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_TIDAL_HUNT_MANTIK_HAM.md)

```
SKOR:      4.0/10  ·  VERDİKT: FIXABLE IN EDIT
GİRDİ:     yalnız video (rubrik böyle istiyor) — ✅ KURALA UYGUN
DURUM:     ✅ GEÇERLİ — projedeki ilk kapı ihlali olmayan QA raporu
BLOCKER:   0  ·  MAJOR: 4  ·  MINOR: 3
```

## 📊 SKORLAR

| Kategori | Skor | Not |
|---|:---:|---|
| Fiziksel Tutarlılık | 3/10 | 0:54 yaratık bacaklardan geçiyor |
| **Sayaç Mantığı** | **N/A** | 🚨 sayaç ekranda hiç yok — aşağıya bak |
| Uzamsal Coğrafya | 4/10 | konum geçişleri ani |
| Zaman ve Işık | 3/10 | 1:12 turuncu/berrak → 1:21 karanlık/fırtınalı |
| Kostüm ve Prop | 3/10 | dalgıç tüpü açılıp kapanıyor |
| Nedensellik | 4/10 | dalga ekran dışında çözülüyor |
| Nicelik | 6/10 | tek karakter odağı çoğunlukla stabil |
| Kurulum ve Terk | 4/10 | bilek cihazı sürekli kullanılıyor, hiç açıklanmıyor |

## 🚨 EN ÖNEMLİ BULGU — FİLMİN OMURGASI EKRANA ÇIKMAMIŞ

Rapor sayacı arayıp bulamadı ve `N/A` yazdı. Plan dosyasına bakınca ne
kaybolduğu ortaya çıkıyor:

| Plan diyor ki | Ekranda |
|---|---|
| Character Bible: *"a constant countdown to the cycle's final hour"* | — |
| S0: *"the countdown reads **6:00:00** and begins ticking"* | ekran gösterilmiyor |
| S4: *"the countdown reading **past the halfway**"* | ekran gösterilmiyor |
| S9: *"the countdown resting at **0:00:00**"* | ekran gösterilmiyor |

Film "6 saatte gel-git düzlüğünü geç" filmi. Sayaç, gerilimin tek kaynağı.
Görünmeyince geriye **"bir kadın koşuyor"** kalıyor.

**Kök sebep — plan dosyası kendi içinde çelişiyor:**

```
satır 285   NO AI TEXT [LESSON 13]: Wrist display = abstract patterns only.
                                    NEVER text.
satır 338   2s — She raises her wrist display; the countdown reads 6:00:00
```

Model yasağa uydu, anlatım öldü. → **DERS 50** (`../../LESSONS_LEARNED.md`)

## 🔎 DOKÜMAN KONTROLÜ — raporun sorduğu 2 soru cevaplandı

```
❓ "Başta ve sonda 2 kâşif var — yalnız mı olmalıydı?"
✅ YALNIZ. Character Bible: "the first researcher to attempt a full SOLO
   crossing". İkinci figür DERS 20 (karakter klonlama) ihlali.
   Yerleri: 0:00-0:09 ve 1:49-2:00.
   → Ders 20 Kaleida Crash'ten çıkmıştı; bu filmde TEKRARLADI.

❓ "Dalgıç ekipmanı dinamik mi, hata mı?"
✅ HATA — üstelik Bible'ın önceden yasakladığı bir hata:
   "a low-profile chest-mounted rebreather unit, integrated into the suit,
    NEVER a separate handheld device"
   Sırt tüpü ne Bible'da ne 13 sahne prompt'unun hiçbirinde geçiyor.
   Model "su + dalgıç" bağlamından kendi ekledi. Ders 8 / 37 kapsamında.
```

## 🌊 DALGA ATLAMASI — kurgu değil, SENARYO boşluğu

Rapor 1:38 → 1:40 arasını "climax is skipped" diye işaretledi ve düzeltmeyi
"yüksek maliyet" diye fiyatladı. Doğru fiyatlamış — çünkü boşluk **planda da
var:**

```
S8 son kare:  "Dalga reaches the base of the outcrop and BEGINS TO CLIMB
               as the wave closes the final distance."
S9 ilk kare:  "The wave HAS PASSED."

Dalganın çarptığı an hiçbir sahnede yazılmamış.
```

Filmin doruğu iki sahnenin arasına düşmüş. Kurguyla kapatılamaz —
**yazılması gereken bir sahne var.**

## 📌 SONRAKİ ADIM

```
□ S8.5 yazılsın: dalganın çarpması / geçmesi (filmin doruğu şu an yok)
□ Sayaç metinsiz kanala taşınsın (Ders 50 çözümü: su çizgisi + ışık açısı
  + bilek ekranında kapanan halka)
□ S1 ve S10 yeniden üretilsin — tek insan (Ders 20)
□ Dalgıç tüpü içeren kareler yeniden üretilsin (Bible'da göğüs ünitesi var)
□ Senaryo QA'sı yapılsın — dalga boşluğunu bağımsız bulması beklenir
```
