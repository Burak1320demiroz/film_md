# 🔍 THE DEAD APPROACH — QA KAYDI

> **Kaynak dosya:** `yatay_2_dk_filmler/THE_DEAD_APPROACH/THE_DEAD_APPROACH_EMERGENCY_LANDING_FILM.md`
> **Veri kaynağı:** `LESSONS_LEARNED.md` — kalite tablosu + Ders 34-38
> ⚠️ **Orijinal QA raporu dosya olarak mevcut değil** — ancak timestamp'li ham
> bulgular derslerde korunmuş.

---

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Compilation (montaj)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    3/10  🚨 SERİNİN EN DÜŞÜK SKORU (Tidal Hunt ile berabere)
ÖZELLİK:       serinin İLK DİYALOGLU compilation üretimi
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | **3/10** | 🚨 ilk kez 3'e düştü — kask/suit durum geçişi |
| Fizik | 3/10 | |
| Kamera | 3/10 | |
| Işık | 4/10 | |
| Çevre | 5/10 | |
| Canlı | N/A | |
| Hareket | 4/10 | |
| **Parçacık ve Malzeme** | **4/10** | ⚠️ derslerde var, **tabloda yok** |
| **Diyalog ve Ses** | **3/10** | ⚠️ derslerde var, **tabloda yok** |
| **Negatif İhlal** | **4 ihlal** | ⚠️ derslerde var, **tabloda yok** |
| Kare Çapası Sadakati | ⛔ kayıt yok | |

> 🚨 **Kritik kayıt hatası:** Bu filmin en düşük üç skoru (Karakter 3, Diyalog 3,
> Parçacık 4) arasından **ikisi kalite tablosuna hiç girmedi.** Tablo, filmin
> gerçekten nerede battığını göstermiyor.

---

## 🔬 HAM BULGULAR (korunmuş)

```
0:00 — Debris excessive, structural disintegration instead of localized damage
0:11 — Lip-sync fails entirely on dialogue
0:19 — Suit design drifts, helmet appears instantly
1:15 — Exhaust smoke billows as if in an atmosphere
2:10 — Text overlay ("THE DEAD APPROACH")
```

---

## 🧪 ÜRETTİĞİ DERSLER — 5 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 34 | Jenerik metni halüsinasyonu — model başlık kartı ekliyor | 4 negatif ihlal |
| 35 | Dudak senkronizasyonu çöküşü | 3/10 diyalog ve ses |
| 36 | Vakumda atmosferik duman | 4/10 parçacık |
| 37 | Ekipman durum geçişi — kask aniden beliriyor | 3/10 karakter |
| 38 | Hasar abartma — model "hasarlı"yı "parçalanmış" okuyor | 4/10 parçacık |

---

## 📌 KAYITLI TEŞHİS

> *"Dead Approach serinin en düşük puanı (3/10). Sebep: ilk diyaloglu
> compilation üretimi. Diyalog + birleştirilmiş kurgu, kesme ve senkron
> hatalarını aynı anda tetikledi."*

⚠️ Bu teşhis **test edilmedi.** Aynı film diyalogsuz üretilmedi, aynı diyalog
compilation'sız üretilmedi. İki değişken aynı anda değişti.

---

## 🏆 SONRADAN DOĞRULANAN BAŞARI

Ders 37 (ekipman durumu), Bible'da **sayısal olarak** kilitlendiğinde
("kask S21'de bir kez") The Slow Stone'da **hiç tetiklenmedi.**
"Sayısal kilit çalışır" bulgusunun ikinci kanıtı.

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok
🚨 Diyalog (3/10), Parçacık (4/10), Negatif (4 ihlal) skorları kalite
  tablosuna aktarılmamış — tabloya 3 sütun eklenmeli
□ Kare Çapası Sadakati ölçülmemiş
□ "Diyalog + compilation" teşhisi ayrıştırılmamış — iki değişken birlikte
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** Yüksek öncelik. Serinin en düşük skoru ve diyalog
tarafındaki tek veri noktası. Diyalog artık RISING SNOW dahil birçok filmde var.
