# 🔧 T1 — KARE KALİTE TABLOSU (sahne içi)

> **Kaynak rubrik:** `../QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 22.08.2026 — dört mercekli sisteme geçişle birlikte
> **Selefleri:** `../LESSONS_LEARNED.md` · KALİTE TAKİP (yatay teknik) ve
> `05_SHORTS_KALITE_TABLOSU.md` (dikey) — ikisi de aynı gün KAPANDI.
> Bu tablo ikisini birden karşılar; `Format` sütunu ayrımı taşır.
>
> **Ne ölçer:** "Bu karede ne bozuk." Tek bir kareye ya da tek bir çekime
> bakarak söylenebilen her kusur. İki sahne gerektiren hiçbir bulgu buraya
> yazılmaz — o T2'nindir.

---

## 📏 BU TABLOYU OKUMA KURALLARI

```
Ⓥ   MOD V — SPEC verilmeden koşuldu; film kendisiyle + fizikle ölçüldü.
    Gerçek satırdır, eksik satır değildir; ama mod D satırıyla aynı
    ölçüm DEĞİLDİR. İkisi aynı sütunda toplanmaz.
⛔   ÖN KOŞU — planda SPEC hazırdı ama mod V koşuldu. Skor tabloya girer,
    tamlık matrisine GİRMEZ.
🚨   GEÇERSİZ — koşu bir kapıdan geçmedi (sahne sayısı tutmadı, yanlış
    materyal, yanlış mercek). Satır üstü çizili durur, ortalamaya girmez.
—    Kategori N/A veya UNVERIFIABLE: boş bırakılır. ASLA 0 yazılmaz;
    sıfır, ortalamayı temiz bir filmmiş gibi gösterir.
```

⚠️ **ÖLÇÜM SAPMASI ±1.3 PUAN.** Aynı rubrik aynı filmi iki kez ölçtü,
kategoriler 2 puana kadar oynadı. **1.5 puandan küçük fark, fark değildir.**
Bir filmin diğerinden iyi olduğunu söylemek için aradaki farkın 1.5'i
geçmesi gerekir.

⛔ **Bir filme koşulan bütün merceklere AYNI dosya verilir** ve **her mercek
temiz oturumda koşulur.** Aynı oturumda ikinci bir mercek çalıştırılırsa
mercekler birbirinin sahne haritasını devralır; "dört mercek aynı şeyi
gördü" o zaman bir doğrulama değil, tek raporun dört kopyasıdır.

---

## 📊 TABLO

Rubriğin `QUALITY TABLE ROW` çıktısı doğrudan buraya yapıştırılır. Dikey
satırlarda 9:16 / Güvenli Alan / Kanca dolar; yatay satırlarda boş kalır.

| Film | Format | Sahne | Karakter | Fizik | Kamera | Işık | Çevre | Canlı | Parçacık | Diyalog-Ses | Kare Çapası | Hareket | 9:16 | Güvenli Alan | Kanca | Negatif | Toplam |
|---|:--:|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

| **The Iron Slope** Ⓥ ⛔ ⚠️ | DİKEY | Derleme (6) | 4 | (2) | (10) | 10 | (6) | — | 4 | ⬜ | — | 2 | 6 | 6 | 10 | 3 | **5,5** |

| **The Rose Coat** Ⓥ ⛔ ⚠️ | YATAY | Derleme (13) | ⬜ | ⬜ | ⬜ | ⬜ | — | — | ⬜ | — | — | ⬜ | | | | (5) | **—** |

> **The Rose Coat · 26.08.2026 · Ⓥ mod V · ⛔ ÖN KOŞU · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_ROSE_COAT.md`](01_FILM_RAPORLARI/THE_ROSE_COAT.md)
> · **SPEC dosyası filmin klasöründe hazırdı ve verilmedi [D129].**
> · Raporun toplamı 5,0. **Toplam `—`**: ⑩ önerme kapısı iki 🔴'ü düşürdü
> (0:03 hook = filmin novum'u · 1:33 "texture swimming" = filmin ana
> mekaniği, bir fırça darbesi paneli DURUM 3'ten DURUM 0'a indirir), kalan
> her hücre ⬜ AÇIK — ayakta, kapalı, sayı taşıyan hücre **0** [D130].
> · Kaynaksız hücreler `—` yazıldı [D131]; Kamera'nın 10/10'u ⬜'ye döndü:
> raporun KENDİ taban envanteri "very slow, steady push-ins" diyor, plan
> `0 pan · 0 tilt · 0 zoom · 0 track`.
> · **SEVERITY TALLY HATALI:** rapor 🔴 7 yazdı, kendi kayıt defterinde 8
> var [D132]. Negatif sayım da kendi içinde çelişkili
> (`FINDINGS WITH A MATCHING BOX: 6 · TICKED: 5 · MISSED: 0`).
> · 🔴 KAPALI TEK MADDE: 2:10-2:15 başlık kartı — `SCREEN TEXT 0.0 s`
> kilidinin ihlali, dört mercek aynı in-out'u verdi [D70/72/120].

> **The Iron Slope · 25.08.2026 · Ⓥ mod V · ⛔ ÖN KOŞU · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_IRON_SLOPE.md`](01_FILM_RAPORLARI/THE_IRON_SLOPE.md)
> · Parantezli hücreler ortak adım ⑩'dan (önerme kapısı) geçemedi:
> **Fizik (2)** ve **Çevre (6)** düşüşlerinin kaynağı planda YAZILI tasarımdı
> (0,220 g itki yerçekimi · S3'ün planlı anten latisi); **Kamera (10)** ise
> kaynaksız değil, mercek kaymayı GÖRMEDİ — master ölçümü S2'de kamera
> kaymasını gösteriyor. · **Diyalog-Ses 1/10** ⬜ AÇIK (vakumda ses hükmü
> 10 sn dinleme bekliyor). · Toplam, rubriğin kendi aritmetiğidir;
> kapı ④ düştüğü için satır ortalamalara girmez.
