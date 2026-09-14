# 🎬 Yatay 3-5 Dakika Filmler

## Format Kuralları

| Özellik | Değer |
|---|---|
| **Süre** | 3-5 dakika (180-300 saniye) |
| **Oryantasyon** | 16:9 yatay (widescreen) |
| **Toplam sahne** | 24 sahne |
| **Yapı** | 2 bölüm × 12 sahne |
| **Klip süresi** | 10 saniye / sahne (Hook = 9s) |
| **Tek çekim kuralı** | Her sahne ayrı tek çekim video |

---

## 📐 24 Sahne Yapısı

### BÖLÜM A — Sahneler 0-11 (İlk 12 sahne)

```
SAHNE 0   — HOOK (9s): Ölçek şoku / merak tetikleyici
SAHNE 1   — Varış / kuruluş
SAHNE 2   — İlk yüzey keşfi
SAHNE 2.5 — VİRAL ARA SAHNE #1
SAHNE 3   — Derinleşen gözlem
SAHNE 4   — İlk anomali / keşif
SAHNE 5   — Araştırma / kanıt toplama
SAHNE 5.5 — VİRAL ARA SAHNE #2
SAHNE 6   — Duygusal dönüm noktası
SAHNE 7   — Çevresel değişim (tutulma, fırtına, vb.)
SAHNE 8   — Değişimin doruk noktası
SAHNE 9   — Geçiş / yeni aşamaya hazırlık
```

**→ BÖLÜM A burada tamamlanır. Ayrı dosya olarak hazırlanır.**

### BÖLÜM B — Sahneler 10-21 (Son 12 sahne)

```
SAHNE 10  — Yeni bölge / derinleşme
SAHNE 11  — İkinci keşif katmanı
SAHNE 11.5 — VİRAL ARA SAHNE #3
SAHNE 12  — Bilimsel doğrulama / hipotez kanıtı
SAHNE 13  — Karakter iç yolculuğu
SAHNE 14  — İkinci çevresel olay
SAHNE 14.5 — VİRAL ARA SAHNE #4
SAHNE 15  — Doruk anı — filmin duygusal zirvesi
SAHNE 16  — Çözülme başlangıcı
SAHNE 17  — Son bakış / veda
SAHNE 18  — Ayrılış
SAHNE 19  — FINAL: Geniş çekim, evrensel perspektif
```

**→ BÖLÜM B burada tamamlanır. Ayrı dosya olarak hazırlanır.**

---

## ⚠️ DURUM NOTU — bu dosya BAYAT (04.09.2026)

> Bu not bir sayı taşımaz, bir ÇELİŞKİYİ kaydeder. Kural ①: sayı tek yerde
> durur; burada duran sayılar aşağıdaki iki kaynakla çakışıyor ve düzeltme
> kararı sahibindir.

```
① İSKELET DEĞİŞTİ (01.09.2026): bu dosya hâlâ PART_A / PART_B diyor.
   Geçerli iskelet KILAVUZ_REHBERI §2.0'dır: SEKİZ dosya —
   PLAN · BOLUM_1 · BOLUM_2 · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC ·
   REFERANS_PAKETI.
   ⛔ 06.09.2026 DÜZELTMESİ: bu satır "REFERANS_PAKETI, iki insandan veya
     iki araçtan fazlası varsa" diyordu ve o SAYIM KURALI ÖLDÜ. Tetikleyici
     artık REFERANS_PAKETI_KILAVUZU §1'in ALTI koşuludur ve T1 (kask/vizör/
     basınç giysisi) bu deponun neredeyse her filminde doğrudur → paket
     İSTİSNA DEĞİL VARSAYILANDIR.
   THE_SINKING_STAKE · THE_UPWARD_FALL · THE_WHITE_FLOOD · THE_STANDING_WIRE ·
   THE_KEPT_LIGHT bu iskeletle yazıldı; THE_OPEN_CIRCUIT (07.09.2026) sekiz
   dosyanın sekizini birden taşıyan İLK filmdir.

② SAHNE SAYISI ÇELİŞKİSİ, HÂLÂ AÇIK:
   bu dosya            → 24 sahne / 2 × 12
   KILAVUZ_REHBERI §2.3 → 25 sahne / 4:09 (13 + 12)
   Hangi filmin hangisini izlediği kendi PLAN'ında yazılıdır:
     THE PAYLOAD        → bu README
     THE SINKING STAKE  → §2.3
     THE UPWARD FALL    → §2.3
     THE WHITE FLOOD    → §2.3, ve sahne sayısını sahibin açık izniyle
                          30'a çıkardı (299 s = 4:59; 40 sahne 6:39 eder
                          ve 3-5 dk BANDININ DIŞINA çıkardı)
     THE STANDING WIRE  → §2.3
     THE KEPT LIGHT     → §2.3  (06.09.2026)
     THE OPEN CIRCUIT   → §2.3  (07.09.2026 · 25 sahne / 4:09)
   ⛔ İki kaynaktan biri düzeltilene kadar her yeni film hangisini
     izlediğini PLAN'ına YAZAR.

③ SÜRE HESABI BLOĞU (aşağıda) da bu çelişkiyi taşıyor: 23 sahne ve
   19 + 4 sahne diye iki ayrı aritmetik veriyor, ikisi de 239 s çıkıyor.
   Bandın kendisi (180-300 s) doğrudur; içindeki sahne sayısı değil.
```

---

## 📁 Dosya Yapısı

Her film için 2 dosya oluşturulur:

```
yatay_3_5_dk_filmler/
├── FILM_ADI_PART_A.md    ← Bölüm A (S0-S9, Bible'lar dahil)
├── FILM_ADI_PART_B.md    ← Bölüm B (S10-S19, Bible referansları)
└── README.md             ← Bu dosya
```

### Part A içeriği:
- Film kapağı promptu
- Tüm Bible'lar (World, Character, Ship, Camera, Lighting, Motion, Physics, Negative)
- Sahneler 0-9 (IMAGE + VIDEO promptları)
- Müzik promptu Bölüm A (ilk yarı)

### Part B içeriği:
- Bible referansı (Part A'ya yönlendirme — tekrar yazmaya gerek yok)
- Sahneler 10-19 (IMAGE + VIDEO promptları)
- Müzik promptu Bölüm B (ikinci yarı)
- Final özet tablosu

---

## 🔢 Süre Hesabı

```
Hook (9s) + 23 sahne × 10s = 239 saniye ≈ 3 dakika 59 saniye

Viral ara sahneler dahil:
Hook (9s) + 19 ana sahne × 10s + 4 viral × 10s = 239s ≈ 4 dakika
```

---

## 📏 2-4dk Filmlerle Karşılaştırma

| Özellik | 2-4dk Film | 3-5dk Film |
|---|---|---|
| Sahne sayısı | 13 (10+Hook+2 viral) | 24 (20+Hook+4 viral) |
| Dosya sayısı | 1 | 2 (Part A + Part B) |
| Bible tekrarı | Her dosyada tam | Part A'da tam, Part B'de referans |
| Anlatı derinliği | Tek katman keşif | Çift katman (keşif → derinleşme) |
| Müzik yapısı | Tek parça 130s | İki bölüm veya tek parça 240s |
| Viral ara sahne | 2 | 4 |
