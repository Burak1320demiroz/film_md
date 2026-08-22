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

*(Henüz satır yok — ilk koşuyu işleyen ajan bu satırı siler.)*
