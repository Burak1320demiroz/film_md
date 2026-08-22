# 🔊 T3 — SES KALİTE TABLOSU (film boyu · ses)

> **Kaynak rubrik:** `../QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 22.08.2026 — dört mercekli sisteme geçişle birlikte
> **Selefi:** `07_SES_KALITE_TABLOSU.md` — aynı gün KAPANDI.
>
> **Ne ölçer:** "Doğru ses doğru bedenden mi çıkıyor." Dokuz kategori;
> eski karakter merceğinin ses/performans yarısı da buraya geldi — ses
> merceğin, beden T2'nin.
>
> ⛔ **Yalnız TAM KURGUYA koşulur**, tek klibe koşulmaz. Ayrıca `STEP 0`
> ses varlık kapısı vardır: sessiz film ≠ sesi ihraç edilmemiş dosya.
>
> ⚠️ **REGISTER şerhi:** "Sentetik" sütunu yalnız İNSAN register'lı
> repliklerin insan geçip geçmediğini ölçer. MACHINE register'lı bir sesin
> düz okuması TASARIMDIR, buraya ceza olarak yazılmaz. Bu seri diegetik
> yapay ses kullanıyor; register'sız "AI gibi konuşuyor" bulgusu çalışan
> tasarımı bozar.

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

| Film | Ses Durumu | Atıf | Sentetik | Ses Kimliği | Aktarım | Sıra Alma | Ambiyans | SFX Senk | Miks | Müzik | Toplam |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

*(Henüz satır yok — ilk koşuyu işleyen ajan bu satırı siler.)*

⛔ **Bir bulgu diğer bütün skorları ezer:** yanlış karakterden çıkan replik,
ya da hiçbir kaynağa bağlanmayan ses → **WRONG VOICE, REGENERATE.**
