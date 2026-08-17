# 🔍 THE SLOW STONE — QA KAYDI

> **Kaynak dosya:** `yatay_7_9_dk_filmler/THE_SLOW_STONE/`
> ✅ **ORİJİNAL QA RAPORU MEVCUT:** `yatay_7_9_dk_filmler/THE_SLOW_STONE/QA_RAPORU.md`
> **(235 satır, 4 rapor birleştirilmiş) — projedeki TEK tam QA belgesi.**
> Bu dosya sadece özet ve indekstir; ayrıntı için kaynak rapora bakılır.

---

## 📋 KÜNYE

```
FORMAT:        7-9 dk · yatay · bilimkurgu
QA KAPSAMI:    Full — 3 geçişli QA sistemi + eski tekil-klip promptu (Rapor 0)
QA TARİHİ:     30 Temmuz 2026
SPEC BLOĞU:    🚨 DÖRT RAPORDA DA BOŞ ÇALIŞTIRILDI
GENEL SKOR:    5/10
YAPI:          4 kısım × 12 sahne × 10s = 48 sahne (planlanan 480s)
GERÇEK SÜRE:   455s (07:35) — 25 saniye eksik
YERÇEKİMİ:     0.7g
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | **7\*/10** | ⚠️ **DOĞRULANMAMIŞ** — aşağıya bak |
| Fizik | 4/10 | |
| Kamera | **7/10** | 📈 bir "full" filmde ilk kez 7 |
| Işık | 5/10 | |
| Çevre | 3/10 | temas tetikli geometri morphu |
| Canlı | N/A | |
| Hareket | 5/10 | yaygın ağır çekim hissi + jello |
| Parçacık ve Malzeme | ⛔ kayıt yok | |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

---

## 🔬 HAM BULGULAR (korunmuş)

```
1:22 — Rock texture visibly morphs and swims as the scraper tool interacts
4:42 — Chipped debris floats; scraper tool suffers jello warping
4:46 — Suit chest emblem warps during rock scraping
6:25 — Footprints lack depth, appear painted onto the terrain
7:05 — Cracking ground morphs geometrically rather than fragmenting
     — Pervasive slow-motion interpolation feel; jello effects on edges
```

---

## 🧪 ÜRETTİĞİ DERSLER — 2 ders

| Ders | Başlık | Kaynak |
|:---:|---|---|
| 43 | Etkileşim tetikli geometri morphu — alet değdiği yeri eritiyor | Geçiş 1 (Çevre 3/10) + Geçiş 2 (Kostüm 7/10), **iki bağımsız rapor aynı kök nedeni buldu** |
| 44 | Düşük-ama-yüksek yerçekimi ağır çekim okunuyor | Geçiş 1 (Hareket 5/10) + Rapor 0 (Hareket 5/10), **iki bağımsız rapor aynı bulgu** |

> Bu, **çapraz doğrulanmış ders üreten tek film.** İki bağımsız rapor aynı kök
> nedeni bulduğu için Ders 43 ve 44 kendinden önceki derslerden daha yüksek
> güvenilirlikte.

---

## 🚨 GEÇERLİLİK SINIRI — ciddi

Kaynak raporun kendi uyarıları:

```
1. FORMAT UYUŞMAZLIĞI
   QA promptu 5 faz × 12 sahne × 8s = 60 sahne varsaydı.
   Film ise 4 kısım × 12 sahne × 10s = 48 sahne.
   → Geçiş 2 ve Geçiş 3, VAR OLMAYAN bir "Faz 5" için puan UYDURDU.
   → İki model de eksik yapıyı bildirmek yerine doldurdu.
   (QA promptları düzeltildi — yapı artık parametre, sabit değil)

2. KARAKTER SKORU BIBLE'A KARŞI DOĞRULANMADI
   Geçiş 2 referansını Bible'dan değil VİDEODAN kurdu.
   → Sadece kendi içinde tutarlılığı ölçtü, uygunluğu ölçmedi.
   → Bible'daki 4 yüz işaretinin (burun izi, dudak çatlağı, gri teller,
     gülme çizgileri) HİÇBİRİ kontrol edilmedi.
   → 7/10 karakter skoru bir uygunluk belgesi DEĞİL.

3. MİNERAL BİRİKİM GERİ SAYIMI ÖLÇÜLEMEDİ
   Filmin imza öğesi (K1 temiz → K4 kalın kabuk) hiç değerlendirilmedi.
```

---

## 🏆 İKİ BÜYÜK BULGU

**1. Uzun format, serinin en dirençli hatasını yapısal olarak çözdü**
> *"Kamera ilk kez bir 'full' filmde 7/10 — ve DERS 1 (kesme) ilk kez
> tetiklenmedi. Sebep: 7-9dk formatı sahneleri ayrı üretiyor, model kesme
> uydurmak zorunda kalmıyor."*

**2. Sayısal kilit çalışıyor, tarif kilidi çalışmıyor**
> *"Ders 32 (gemi ölçek) ve Ders 37 (ekipman durumu) bu filmde HİÇ tetiklenmedi —
> ikisi de Bible'da sayısal olarak kilitlenmişti (24m / 6 derece / kask S21'de
> bir kez)."*

Bu iki bulgu, o tarihe kadarki derslerin tamamından daha fazla puan getirmiş
görünüyor.

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Dört raporun dördü de SPEC bloğu boş çalıştırıldı
□ Karakter skoru doğrulanmamış — dolu SPEC ile Geçiş 2 tekrarlanmalı
□ Mineral birikim geri sayımı hiç ölçülmedi
□ 25 saniye eksik süre nedeni raporlanmamış
□ 4 rubrik kategorisi (parçacık, diyalog, kare çapası, negatif) kayıt dışı
□ ⚠️ Bu, projedeki TEK tam QA belgesi — diğer 11 filmde eşdeğeri yok
```

**Tekrar QA gerekli mi?** Kısmen — **sadece Geçiş 2, dolu SPEC ile.**
Karakter uygunluğu hâlâ bilinmiyor.
