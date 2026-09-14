# 🔍 THE DEEP PRESSURE — QA KAYDI

> **Kaynak dosya:** `yatay_2_dk_filmler/THE_DEEP_PRESSURE/THE_DEEP_PRESSURE_GAS_GIANT_FILM.md`
> ⚠️ **Bu dosya 13 sahnelik filmin yalnız 2 sahnesini içeriyor (56 satır).**
> Character Bible, sahne haritası ve negatif blok depoda YOK.
>
> **Bu filmde bir QA var:**
> · **MANTIK QA** (1 Ağustos 2026) — **3.0/10** · ham çıktı:
>   [`../02_HAM_RAPORLAR/THE_DEEP_PRESSURE/THE_DEEP_PRESSURE_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_DEEP_PRESSURE/THE_DEEP_PRESSURE_MANTIK_HAM.md)
> · Teknik QA: ❌ henüz yapılmadı
> · Senaryo QA: ❌ henüz yapılmadı

---

# 🧩 MANTIK VE DEVAMLILIK QA — 1 AĞUSTOS 2026

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu (gaz devi keşif)
QA KAPSAMI:    Montaj — 2:15 · 14 sahne
BASELINE:      SELF-CONSISTENCY ✅ (header'da bildirildi)
GİRDİ:         yalnız video — doküman verilmedi ✅ kurala uygun
GENEL SKOR:    3.0/10 — STRUCTURAL PROBLEM
                🔴 4 BLOCKER · 🟠 2 MAJOR · 🟡 0 MINOR
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Fiziksel Tutarlılık | 4/10 | S12'ye kadar su altı okuması, S12'de aynada dik duruş |
| Sayaç Mantığı | N/A | izlenebilir sayaç yok |
| Mekânsal Coğrafya | 4/10 | tekrar eden portal iki sahnede iki farklı yer |
| Zaman ve Işık | 3/10 | ortam ışığı sahneden sahneye sıçrıyor |
| Durum, Kostüm, Prop | **1/10** | 🚨 **üç tablonun tamamındaki en düşük kategori skoru** |
| Nedensellik | N/A | montaj — sahneler arası neden-sonuç gözlenemiyor |
| Nicelik | N/A | sayılan bir şey yok |
| Kurulum ve Terk | 7/10 | denizaltı açılış/kapanış motifini tutturmuş |

---

## 🧪 ÜRETTİĞİ DERSLER — 4 ders

| Ders | Başlık | Kaynak bulgu |
|:---:|---|---|
| **55** | Bible'sız üretim — kıyafet her sahnede yeniden icat ediliyor | Kostüm-Prop 1/10, 4 BLOCKER |
| **56** | "Dalış" sözlüğü su üretiyor — atmosfer okyanusa dönüşüyor | ortam okuması: yoğun sıvı + kabarcık |
| **57** | Tek çekim içinde ekipman morphu — 7. saniyede tüp beliriyor | 00:00 vs 00:07 |
| **58** | Tekrar eden varlık kimlik kilidi — aynı yer iki farklı yer | portal S4↔S8, göz S11↔S14 |

**Tekrar tetiklenen dersler (yeni değil):** 5 (vizör kalıcılığı), 8 ve 37
(kıyafet/ekipman durumu), 47 (ışık sıçraması), 48 (biyom sıçraması).

---

## 🔎 DOKÜMAN KONTROLÜ — 2 soru, 2 cevap

Ayrıntı ham raporda. Özet:

```
❓ "Kanonik kıyafet hangisi?"
✅ Hiçbiri. Seri Bible'ındaki mor + bakır kıyafet 14 sahnenin HİÇBİRİNDE yok.
   Deep Pressure'ın kendi dosyası kıyafeti tarif etmeden referans veriyor.

❓ "Sürreal montaj mı, gerçek yolculuk mu?"
✅ Yolculuk olmalıydı. Plan "Scene 2.5 of 13", "Starts on the exact Scene 2.5
   image", "No cuts" diyor — bitişik bir iniş. Montaj bir plan sonucu.
```

Filmin gerçekten bu plana ait olduğu iki sahnenin birebir eşleşmesiyle
doğrulandı: S4 ↔ SAHNE 2.5 (yoğunluk sınırı + manta), S7 ↔ SAHNE 6.5
(donan yıldırımın kristalleşip dağılması).

---

## 📤 OUT-OF-SCOPE FLAGS — teknik kayıt

Mantık raporu bunları kendi kapsamı dışında bıraktı; teknik QA yapıldığında
başlangıç noktası bunlar:

| Gözlem | Timecode | İlgili ders |
|---|---|---|
| Vizör camının arkasında yüz morphu, yapı kaybı | 00:48 · 02:04 | **DERS 16** (yüz kilidi) — iki yeni timestamp |
| Film anlatı değil, mood board / fragman gibi okunuyor; lokasyonlar arası nedensellik yok | tüm film | SENARYO_QA konusu — dramatik yargı, ders üretmez |

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
❌ Teknik QA (VIDEO_QA) hiç yapılmadı — 11 kategorinin hiçbiri ölçülmedi
❌ Senaryo QA hiç yapılmadı
❌ Plan dosyası eksik: 13 sahnenin 11'inin metni yok
   → bu haliyle film YENİDEN ÜRETİLEMEZ; önce dosya yazılmalı (Ders 55)
```
