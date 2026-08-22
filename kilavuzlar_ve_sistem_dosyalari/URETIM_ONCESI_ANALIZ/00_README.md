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
