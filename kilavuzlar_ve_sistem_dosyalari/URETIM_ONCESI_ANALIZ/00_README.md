# 🔮 ÜRETİM ÖNCESİ ANALİZ

> **Amaç:** Parayı harcamadan önce neyin bozulacağını bilmek.
> **Oluşturma:** 31 Temmuz 2026
> **Girdi:** Yeni üretim YOK. Yalnızca elimizdeki 11 QA raporu + 50 ders.

---

## 🎯 BU KLASÖR NEDEN VAR

Projede üç mercek var ve **üçü de para harcandıktan sonra bakıyor:**

```
PLAN → BIBLE → PROMPT → ÜRETİM ──┬── VIDEO_QA      ← para harcandı
                                 ├── MANTIK_QA     ← para harcandı
                                 └── SENARYO_QA    ← para harcandı
```

50 ders bu üç mercekten çıktı. Ama kalite tablosunda **11 filmin ortalaması
hiç 5'i geçmedi** ve seri düz: `4 · 5 · 5 · 3 · 4.5 · 4 · 5 · 5 · 3 · 4 · 5`.

**Kural eklemek kaliteyi artırmadı.** Bu klasör bunun üzerine kuruldu:
üretmeden önce, elimizdeki veriye bakarak **bu filmin nerede kırılacağını**
söylemek.

---

## 📁 DOSYALAR

| Dosya | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| `01_DERS_ETKINLIK_RAPORU.md` | 50 dersin hangisi işe yarıyor — kanıtla | ders eklerken / çıkarırken |
| `02_RISK_KARTLARI.md` | "Filmde su var" → ne bozulacak, ne yapılmalı | **plan yazmadan önce** |
| `03_PLAN_ONCESI_KONTROL_LISTESI.md` | Yazılmış planı üretime sokmadan tara | plan bitti, üretim başlamadan |

---

## 🔁 AKIŞTAKİ YERİ

```
   FİKİR
     │
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
   PROMPT → ÜRETİM → (üç QA merceği)
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

Şu an 50 dersin 36'sı ÖLÇÜLEMEDİ durumunda. Bu bir eksiklik değil,
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
| `../LESSONS_LEARNED.md` | sürekli | 50 dersin metni |
