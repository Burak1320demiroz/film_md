# 🔗 T2 — DEVAMLILIK KALİTE TABLOSU (sahneler arası)

> **Kaynak rubrik:** `../QA_PROMPTLARI/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 22.08.2026 — dört mercekli sisteme geçişle birlikte
> **Selefleri:** `04_MANTIK_KALITE_TABLOSU.md` ve
> `06_KARAKTER_KALITE_TABLOSU.md` — ikisi de aynı gün KAPANDI. İki rubrik
> tek merceğe indi: 16 kategori yuvası 13'e, çift sayım kuralla değil
> YAPIYLA kesildi.
>
> **Ne ölçer:** "Film ve içindeki insan kendiyle çelişiyor mu." Her bulgu
> İKİ sahne gerektirir; tek kareden söylenebilen hiçbir şey buraya girmez.
>
> ```
> GÖVDE   1-6   kimlik · kostüm · yıpranma · ekipman · çapraz kesme · fizik
> DÜNYA   7-13  sayaç · coğrafya · zaman-ışık · dünya propu · nedensellik
>               · nicelik+sayı · kurulum
> ```
> Bir okur bu tabloya bakıp filmin **insanını mı yoksa yerini mi**
> kaybettiğini görebilmeli — ikisi farklı üretim hatasıdır ve farklı
> çözümleri vardır.

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

| Film | Kimlik | Kostüm | Yıpranma | Ekipman | Çapraz Kesme | Fizik | Sayaç | Coğrafya | Zaman-Işık | Dünya Propu | Nedensellik | Nicelik+Sayı | Kurulum | Toplam |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

*(Henüz satır yok — ilk koşuyu işleyen ajan bu satırı siler.)*

⛔ **İki bulgu diğer bütün skorları ezer:**
```
KİMLİK KIRILMASI  başka bir yüz, ya da ekranda kopya karakter
SAYAÇ TERSİNMESİ  geri giden sayaç — devamlılık kayması değil,
                  önermenin çöküşü
```
İkisi de verdict'in ilk satırına yazılır; ortalama ne olursa olsun.
