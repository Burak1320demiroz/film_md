# 🔍 THE SLOW TIDE — QA KAYDI

> **Kaynak dosya:** `yatay_2_dk_filmler/THE_SLOW_TIDE/THE_SLOW_TIDE_PLANET_FILM.md`
> **İlgili:** `dikey_shorts_filmler/THE_SLOW_TIDE/THE_SLOW_TIDE_DIKEY_SHORTS.md` — **dikey
> versiyonun ayrı QA'sı YOK**
> **Veri kaynağı:** `LESSONS_LEARNED.md` — kalite tablosu + Ders 1, 13-16
> ⚠️ **Orijinal QA raporu dosya olarak mevcut değil.**

---

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Montaj (compilation)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    5/10
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 4/10 | |
| Fizik | 3/10 | |
| Kamera | 3/10 | kesme sorunu tekrarladı |
| Işık | 6/10 | |
| Çevre | 5/10 | büyük su kütleleri statik |
| Canlı | N/A | |
| Hareket | 4/10 | |
| Parçacık ve Malzeme | ⛔ kayıt yok | |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ✅ tetiklendi (sayı bilinmiyor) | Ders 13'ün kaynağı |

---

## 🧪 ÜRETTİĞİ DERSLER — 4 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 13 | AI metin — hologramda anlamsız yazı | negatif ihlal |
| 14 | Donmuş su — büyük su kütleleri statik | 5/10 çevre, 4/10 hareket |
| 15 | İmkansız fizik — yerçekimine aykırı pozisyon | 3/10 fizik |
| 16 | Yüz morph — kask arkasında yüz değişimi | 4/10 karakter |

**Ayrıca doğruladığı ders:** Ders 1 (kesme, 3/10)

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok
□ 4 rubrik kategorisi kayıt dışı
□ ⛔ DİKEY SHORTS VERSİYONU HİÇ QA EDİLMEDİ — aynı içerik, farklı format,
  farklı hata profili beklenir (48s, 6 sahne, text-to-video)
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** Evet — ve **dikey versiyon ayrıca QA edilmeli.**
Aynı filmin iki formatı, aynı rubrikle ölçülürse format ↔ hata ilişkisi için
projedeki tek doğal kontrol grubu elde edilir.
