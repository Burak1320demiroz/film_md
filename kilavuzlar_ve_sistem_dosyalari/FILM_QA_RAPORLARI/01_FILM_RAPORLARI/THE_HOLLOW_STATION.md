# 🔍 THE HOLLOW STATION — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_HOLLOW_STATION/THE_HOLLOW_STATION_FILM.md`
> **Veri kaynağı:** `LESSONS_LEARNED.md` — kalite tablosu + Ders 23-25
> ⚠️ **Orijinal QA raporu dosya olarak mevcut değil.**

---

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Full (tam film)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    4/10
ORTAM:         kapalı mekan + sıfır-g + sıvı etkileşim
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 4/10 | sıvı temasında morph |
| Fizik | 4/10 | sıfır-g'de karakter rijit |
| Kamera | 3/10 | kesme sorunu tekrarladı |
| Işık | 5/10 | vizör yansıması bağımsız hareket ediyor |
| Çevre | 5/10 | |
| Canlı | 4/10 | |
| Hareket | 4/10 | |
| Parçacık ve Malzeme | ⛔ kayıt yok | |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

---

## 🧪 ÜRETTİĞİ DERSLER — 3 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 23 | Sıfır-G katılığı — süzülen karakter rijit | 4/10 fizik, 4/10 hareket |
| 24 | Sıvı etkileşim morph — su küresi dokunma hatası | 4/10 fizik, 4/10 karakter |
| 25 | Vizör yansıma otonomisi — yansıma bağımsız hareket ediyor | 5/10 ışık |

---

## 📌 KAYITLI HİPOTEZ

> LESSONS_LEARNED notu: *"Hollow Station serinin en düşük puanı (4/10) — kapalı
> mekan + sıfır-g + sıvı etkileşim AI için en zor kombinasyon."*

⚠️ Bu hipotez **test edilmedi.** Üç zorluk aynı anda değiştiği için hangisinin
puanı düşürdüğü ayrıştırılamaz. Kontrollü karşılaştırma yapılmadı.

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok
□ 4 rubrik kategorisi kayıt dışı
□ "En zor kombinasyon" hipotezi ölçülmemiş — üç değişken birlikte değişti
□ SPEC bloğu durumu bilinmiyor
□ Ders 24 (sıvı temas) ile Ders 43 (temas morphu) aynı kök nedene mi bakıyor
  belirsiz — ikisi ayrı ders olarak duruyor
```

**Tekrar QA gerekli mi?** Evet — ayrıca Ders 24 ↔ 43 ↔ 11 (dokunma morphi)
üçlüsü birleştirilmeli mi diye bakılmalı. Üçü de "temas anında geometri bozulur"
diyor, üç ayrı ders olarak prompt şişiriyor olabilir.
