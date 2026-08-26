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

| ~~**The Iron Slope** Ⓥ ⛔ 🚨~~ | B (sessiz, tasarımlı) | — | — | — | — | — | ~~2~~ | ~~5~~ | ~~6~~ | — | ~~4,3~~ |

| **The Rose Coat** ⬜ | C (ses bilgisi yok) | — | — | — | — | — | — | — | — | — | **—** |

> **The Rose Coat · 26.08.2026 · `AUDIO ABSENT — RUN NOT STARTED`**
> ⛔ Bu bir SKOR SATIRI DEĞİL, bir İZ satırıdır [D136]: stop bloğu doğru
> çalıştı ama hiçbir tabloya satır bırakmıyordu ve "koşuldu, dosya bozuk"
> ile "hiç koşulmadı" kayıtta aynı görünüyordu.
> · Plan 13 sahnenin **11'inde müzik** yazıyor (`MUSIC-FREE SCENES: 2`)
> ve S11 · 7,0 s'de iki eldiven tıklaması (ses tasarımı). Dosyada ses yok.
> · ⬜ KAPATMA: `ffprobe -v error -select_streams a -show_entries
> stream=codec_type -of csv=p=0 "$M"` — çıktı boşsa 🔴 TESLİM KUSURU,
> master yeniden ihraç edilir ve DÖRT mercek yeniden koşulur.
> · Öteki dört mercek şüpheyi görmedi: üçü `LINES HEARD: none`, biri
> `Dialogue & Audio | UNVERIFIABLE | (no sound)` yazıp geçti.

> **The Iron Slope · 25.08.2026 · 🚨 GEÇERSİZ — satır üstü çizili, ortalamaya girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_IRON_SLOPE.md`](01_FILM_RAPORLARI/THE_IRON_SLOPE.md)
> · Sebep: merceğin tek 🔴 BLOCKER'ı ve Ambiyans 2/10'u **hiç var olmayan bir
> sessizliğe** dayanıyor. Master ölçümü: `silencedetect -50 dB / 0,3 s` → sıfır
> sonuç; saniyelik RMS 0-60 s boyunca en düşük −26,8 dB, S4 (30-40 s) −19,7…−22,8 dB.
> · "no music present" satırı da şüpheli: 0-60 s kesintisiz, düzenli vuruşlu
> geniş bant katman var. · Altı kategori N/A — film **repliksizdir**, bu bir
> kısıttır, eksik değil [D113]. → **DERS 125**

⛔ **Bir bulgu diğer bütün skorları ezer:** yanlış karakterden çıkan replik,
ya da hiçbir kaynağa bağlanmayan ses → **WRONG VOICE, REGENERATE.**
