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
