# 🔍 THE LAST CROSSING — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_LAST_CROSSING_BLACK_HOLE_FILM.md`
> **Veri kaynağı:** `LESSONS_LEARNED.md` — Ders 33
> 🚨 **BU FİLM KALİTE TAKİP TABLOSUNDA YOK.** QA yapıldı (Genel 4/10), ders
> üretildi, ama tabloya hiç satır eklenmedi. Sistemin ilk kayıt kaybı.

---

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Compilation (montaj)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    4/10
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | ⛔ kayıt yok | ders metninde sorun bildiriliyor, puan yok |
| Fizik | ⛔ kayıt yok | sıfır-g momentum kaybı bildirildi, puan yok |
| Kamera | ⛔ kayıt yok | hard cut bildirildi, puan yok |
| Işık | ⛔ kayıt yok | bloom / waxy skin bildirildi, puan yok |
| Çevre | ⛔ kayıt yok | |
| Canlı | ⛔ kayıt yok | |
| Hareket | ⛔ kayıt yok | frame-rate dalgalanması bildirildi, puan yok |
| Parçacık ve Malzeme | ⛔ kayıt yok | |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

> ⚠️ **Hiçbir kategori skoru kaydedilmemiş.** Sadece "Overall 4/10" var.
> Bu film 11 kategorinin 11'inde de ölçüsüz.

---

## 🔬 BİLDİRİLEN SORUNLAR (ders metninden)

```
· Tek çekim ihlali — dışarıdan içeriye / çevreye hard cut
· Sıfır-g'de kargo dumanı, enkaz ve kokpit içi nesneler momentumdan yoksun,
  2D asset gibi statik asılı
· "Cinematic lighting" ifadesi bloom + waxy/smoothed skin üretiyor
· Karakter teması ve kıyafet konumları (rozet, yakalık) frame-rate
  dalgalanmalarına maruz
```

---

## 🧪 ÜRETTİĞİ DERSLER — 1 ders

| Ders | Başlık |
|:---:|---|
| 33 | Compilation cuts and zero-g physics |

> **Ders 33 biçim olarak aykırı:** Başlığı İngilizce (diğer derslerin tamamı Türkçe),
> kaynak satırı skorsuz, çözümü üç ayrı prompt parçasına bölünmüş. Sisteme
> farklı bir oturumda ve farklı şablonla eklenmiş görünüyor.

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
🚨 KALİTE TABLOSUNDA SATIRI YOK — eklenmeli
□ 11 kategorinin 11'i de puansız
□ Ham QA raporu yok, timestamp yok
□ Ders 33 başlığı Türkçeleştirilmeli (biçim tutarlılığı)
□ Ders 33'ün "sıfır-g momentum" kısmı Ders 23 (sıfır-g katılığı) ile
  büyük ölçüde örtüşüyor — birleştirilmeli mi bakılmalı
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** **EVET — en yüksek öncelik.** Bu film QA edildi ama
verisi sisteme hiç girmedi. Tekrar puanlanmadan kalite tablosu eksik kalır ve
11 film üzerinden yapılan her ortalama yanlış olur.
