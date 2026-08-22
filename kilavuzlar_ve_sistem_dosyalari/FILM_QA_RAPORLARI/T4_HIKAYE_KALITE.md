# 📖 T4 — HİKAYE KALİTE TABLOSU (film boyu · anlatı)

> **Kaynak rubrik:** `../QA_PROMPTLARI/4_HIKAYE_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 22.08.2026 — dört mercekli sisteme geçişle birlikte
> **Selefi:** `03_HIKAYE_KALITE_TABLOSU.md` — aynı gün KAPANDI.
>
> **Ne ölçer:** "Kimse umursar mı." On kategori. Eski dikey rubriğin hikaye
> ve tutundurma kategorileri de buraya geldi; `Format` sütunu yatay ile
> dikeyi ayırır — dikeyde kanca bir ZAMANLAMA YASASI olarak, tutundurma da
> saniye ölçeğinde puanlanır.
>
> ⚠️ Bu tablo teknikten bağımsızdır. Aynı film T1'de 4, burada 7 alabilir;
> iki skor birbirini yordamaz.

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

| Film | Format | Süre Sınıfı | Kanca | Önerme | Yapı | Karakter | Tema | Diyalog | Duygu Yayı | Final | Özgünlük | Tutundurma | Toplam |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

*(Henüz satır yok — ilk koşuyu işleyen ajan bu satırı siler.)*

⛔ **Sessiz filmde Diyalog `N/A`'dır, düşük puan değil.** Sessizlik bu
serinin ilan edilmiş kısıtıdır; sözsüz bir filme "sözsüz olduğu için" 5
vermek tasarımı cezalandırır ve ortalamayı sebepsiz aşağı çeker. N/A
ortalamanın DIŞINDA kalır.
