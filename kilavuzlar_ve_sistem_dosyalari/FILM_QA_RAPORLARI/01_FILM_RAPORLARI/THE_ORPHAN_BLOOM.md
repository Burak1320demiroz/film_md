# 🔍 THE ORPHAN BLOOM — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_ORPHAN_BLOOM/THE_ORPHAN_BLOOM_ROGUE_PLANET_FILM.md`
> **Veri kaynağı:** `LESSONS_LEARNED.md` — kalite tablosu + Ders 26-29
> ⚠️ **Orijinal QA raporu dosya olarak mevcut değil** — ancak bu filmin
> derslerinde **timestamp'li ham bulgular korunmuş.** Seride ilk kez.

---

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Full (tam film)
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    5/10
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 5/10 | biyolüminesan yüzeye dokunmada morph |
| Fizik | 4/10 | halat çarpışma ve gerginlik fiziğini yoksayıyor |
| Kamera | **6/10** | 📈 seride ilk iyileşme — kararlı geniş çekimler |
| Işık | 5/10 | yaygın AI bloom ve doğal olmayan parlama |
| Çevre | 4/10 | mağara kaya dokusu yüzüyor |
| Canlı | 5/10 | |
| Hareket | 4/10 | |
| Parçacık ve Malzeme | ⛔ kayıt yok | |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

---

## 🔬 HAM BULGULAR (korunmuş — seride ilk)

```
0:45 — Rock textures in the cavern visibly swim and shift.
0:52 — Rappelling rope ignores collision and tension physics.
     — Pervasive AI bloom and unnatural glow.
```

---

## 🧪 ÜRETTİĞİ DERSLER — 4 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 26 | İp/tether fizik kilidi — halat duvara geçiyor | 4/10 fizik |
| 27 | Mağara dokusu yüzme — jeoloji stabil olmalı | 4/10 çevre |
| 28 | Biyolüminesan temas morph | 5/10 karakter |
| 29 | Anti-parlama kelime sözlüğü — tetikleyen sözcükler | 5/10 ışık |

> **Ders 29 farklı bir tip:** Diğer dersler "şunu ekle" der; bu ders
> "şu kelimeleri **kullanma**" der. Prompt'a ekleme değil, prompt'tan
> çıkarma öneren tek ders. Etkinliği ayrıca ölçülmeli.

---

## 📌 KAYITLI GÖZLEM

> *"Orphan Bloom kamera skorunu 6'ya çıkardı (kararlı geniş çekimler) —
> ancak kesme sorunu devam etti."*

Kamera puanı yükseldi ama Ders 1 hâlâ tetiklendi. Yani **kamera skoru ile
kesme hatası aynı şey değil.** Tabloda bu ikisi tek sütunda toplanıyor.

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok — sadece 3 bulgu satırı derslerde korunmuş
□ 4 rubrik kategorisi kayıt dışı
□ Kamera 6/10 aldı ama Ders 1 tetiklendi — tablo bu ayrımı gösteremiyor
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** Orta öncelik. Ders 29'un (kelime sözlüğü) sonraki
filmlerde ışık skorunu yükseltip yükseltmediği ölçülmeli — Low Power'da ışık
4/10'a düştü, yani sözlük işe yaramamış olabilir.
