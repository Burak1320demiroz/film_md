# 🔮 ÜRETİM ÖNCESİ ANALİZ

> ⚠️ **KESİT UYARISI (eklendi 21.08.2026):** Bu klasörün 00/01/02
> dosyaları **01.08.2026 kesitiyle** yazıldı — o gün depoda 11 QA raporu
> ve 50 ders vardı. Güncel sayılar: `bash ../sayac.sh`. 01 raporu
> D51-119'u HİÇ ölçmedi (bilinen borç: `../KILAVUZ_REHBERI.md` §9).
> 02'ye 10-12 kartları 21.08.2026'da eklendi; eski filmlerin `n/9` risk
> skorları 9 kartlık sürümle ölçüldü ve yeniden yazılmaz.
> Akış şeması 22.08.2026'da güncellendi: konsept+tema kapısı ve
> PROMPT_KONTROL adımı işaretçi olarak eklendi (içerik kesit malıdır).

> **Amaç:** Parayı harcamadan önce neyin bozulacağını bilmek.
> **Oluşturma:** 31 Temmuz 2026
> **Girdi:** Yeni üretim YOK. Yalnızca 01.08.2026 kesitindeki 11 QA raporu + 50 ders.

---

## 🎯 BU KLASÖR NEDEN VAR

Kesit gününde projede üç mercek vardı ve **üçü de para harcandıktan
sonra bakıyordu** (bugünkü rubrik listesi: `../QA_PROMPTLARI/00_README.md`):

```
PLAN → BIBLE → PROMPT → ÜRETİM ──┬── VIDEO_QA      ← para harcandı
                                 ├── MANTIK_QA     ← para harcandı
                                 └── SENARYO_QA    ← para harcandı
```

Kesitteki 50 ders (01.08.2026) bu üç mercekten çıktı. Ama kalite tablosunda **11 filmin ortalaması
hiç 5'i geçmedi** ve seri düz: `4 · 5 · 5 · 3 · 4.5 · 4 · 5 · 5 · 3 · 4 · 5`.

**Kural eklemek kaliteyi artırmadı.** Bu klasör bunun üzerine kuruldu:
üretmeden önce, elimizdeki veriye bakarak **bu filmin nerede kırılacağını**
söylemek.

---

## 📁 DOSYALAR

| Dosya | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| `01_DERS_ETKINLIK_RAPORU.md` | kesit dersleri (01.08.2026) hangisi işe yarıyor — kanıtla | ders eklerken / çıkarırken |
| `02_RISK_KARTLARI.md` | "Filmde su var" → ne bozulacak, ne yapılmalı | **plan yazmadan önce** |
| `03_PLAN_ONCESI_KONTROL_LISTESI.md` | Yazılmış planı üretime sokmadan tara | plan bitti, üretim başlamadan |
| `04_ARASTIRMA_BULGULARI.md` 🆕 | Dış araştırma turlarının süzme kaydı: hangi bulgu hangi kılavuza indi, hangisi **girmedi ve neden** | dış araştırma geldiğinde · bir kuralın gerekçesi sorulduğunda |
| `05_DIKEY_HAT_TESHISI.md` 🆕 | **Dikey hattın neden "anlamsız" hissettirdiği** — 18 filmin makine taraması, dört üretim önleminin hikâye formatına dönüşme mekanizması, maliyete göre sıralı altı çözüm ve iki prob | dikey film yazmadan önce · "neden hepsi aynı film?" sorulduğunda |
| `06_HIKAYE_HATTI_TESHISI.md` 🆕 | **Bütün deponun neden "saçma" hissettirdiği** — 79 filmin taraması, üç halkalı kapalı döngü (yasaklar türü kurdu · kapılar yalnız üretimi ölçtü · **tür kendini ölçen rubriğe "bu kusur değildir" diye yazıldı**), maliyete göre sıralı çözüm + sahibin iki editoryal kararı | **her film yazmadan önce** · "hikâye neden zayıf?" sorulduğunda · rubrik/novum kuralı tartışılırken |
| `08_SENARYO_ARASTIRMA_PROMPTLARI.md` 🆕 | Hikâye tarafı için dört derin araştırma promptu (çıkarılabilir an · sözsüz istek-hasım · az replikli senaryo · uzay kısa film rakip seti) — altışar cümle, salt prompt, kapanışları aynı | 06'nın açık sorularını dış bilgiyle kapatırken · araştırma turu koşulacağında |
| `PROB_KOSUSU.md` + `prob_olcum.sh` 🆕 | 05 §5④'ün koşu sayfası: yapıştırmaya hazır iki prob, adım adım koşu, boş sonuç tablosu ve **makineyle ölçüm betiği** (gerçek master üstünde doğrulandı) | dört yasak (ikinci insan · replik · isim · kesme) sınanacağında |

> ⚠️ **04, diğer üçünden farklıdır ve kesit uyarısına tabi değildir.**
> Diğer üçü 01.08.2026 kesitinden konuşur; 04 tarih tarih büyüyen bir
> kayıttır ve ilk turu 27.08.2026'dır. Kural 04'ten okunmaz — 04, kuralın
> NEREDEN geldiğini tutar.

> ⚠️ **05 de kesit uyarısına tabi değildir (30.08.2026).** Kendi taramasını
> kendi içindeki betikle yapar (§9.1) ve istendiği an yeniden koşulabilir.
> ⭐ **05, bu klasörün ilk TERS YÖNLÜ dosyasıdır:** 01/02/03 "bu film
> nerede kırılacak" diye sorar; 05 "yazdığımız her filmin AYNI yerde
> kırılmasının sebebi ne" diye sorar. Tek filme değil, HATTA bakar.

---

## 🔁 AKIŞTAKİ YERİ

```
   FİKİR
     │
     ▼
  KONSEPT + TEMA KAPISI  ← ../ONERME_VE_NOVUM_KILAVUZU.md (üç kabul testi —
     │                      geçmeyen konsept plana dönüşmez) + tema kararı:
     │                      ../TEMA_MUHENDISLIGI_KILAVUZU.md (22.08.2026)
     ▼
  06_HIKAYE_HATTI_TESHISI ← ⛔ HER FORMAT: İSTEK/ENGEL/BEDEL/HASIM'ın
     │                      GEREKÇESİ. Kapı 03_PLAN_ONCESI B5'tedir ve
     │                      prompt_kontrol ⑰ olarak KOŞAR (02.09.2026)
     ▼
  05_DIKEY_HAT_TESHISI   ← ⛔ DİKEY FİLM YAZILACAKSA: dört yasağın
     │                      birikme mekanizması + final vuruş kanıtı
     ▼
  02_RISK_KARTLARI       ← "bu filmde su + canlı + diyalog var"
     │                      → 3 risk kartı, 3 sayısal kilit, 1 uyarı
     ▼
   PLAN + BIBLE yazılır
     │
     ▼
  03_PLAN_ONCESI_KONTROL ← plan kendi içinde çelişiyor mu, sahne sayısı
     │                      tutuyor mu, doruk yazılmış mı
     ▼
   PROMPT
     │
     ▼
  ../PROMPT_KONTROL/     ← betik + rubrik · sıfır kare (12.08.2026)
     │
     ▼
   ÜRETİM → QA mercekleri (güncel liste: ../QA_PROMPTLARI/00_README.md)
     │
     ▼
  01_DERS_ETKINLIK       ← QA sonucu buraya döner: ders tuttu mu tutmadı mı
```

Döngü kapanıyor: QA yeni ders üretiyor, **01** o dersin işe yarayıp
yaramadığını ölçüyor, **02** işe yarayanları bir sonraki filmin planına
sokuyor. Şu ana kadar eksik olan halka **01**'di — ders yazılıyor ama
tuttu mu tutmadı mı hiç ölçülmüyordu.

---

## ⚠️ BU KLASÖRÜN DÜRÜSTLÜK KURALI

```
Her satır bir KANITA dayanır: film adı + kategori skoru veya timestamp.
Kanıt yoksa satır "ÖLÇÜLEMEDİ" yazar — tahmin yazmaz.

Kesit gününde (01.08.2026) 50 dersin 36'sı ÖLÇÜLEMEDİ durumundaydı. Bu bir eksiklik değil,
BULGUNUN KENDİSİ: proje kurallarının çoğunun işe yarayıp yaramadığını
bilmiyor. Bunu gizlemek, 44 dersi 50'ye çıkarıp aynı yerde saymak olurdu.
```

---

## 🔗 KOMŞU KLASÖRLER — karıştırma

| Klasör | Ne zaman | Neye bakar |
|---|---|---|
| **URETIM_ONCESI_ANALIZ** (bu) | üretimden **önce** | geçmiş veriye — "ne bozulacak" |
| `../QA_PROMPTLARI/` | üretimden **sonra** | üretilmiş işe — "ne bozuldu" |
| `../FILM_QA_RAPORLARI/` | sonra | rapor arşivi + üç skor tablosu |
| `../LESSONS_LEARNED.md` | sürekli | ders dizini (güncel sayı: sayac.sh) |
