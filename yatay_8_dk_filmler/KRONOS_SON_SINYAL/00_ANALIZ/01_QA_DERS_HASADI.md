# 🧾 KRONOS_SON_SINYAL — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (tavan 20)

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D16 | Vizör arkasında yüz morph riski | Kask içi aydınlatma ve çene pozisyonu sabit tutulacak | S02, S05, S06, S18, S22, S25, S40, S41, S46 |
| D146 | Vizör biçimi sayıyla yazılmadı | 180 derece şeffaf kask vizörü ve polikarbon kenar şeridi | S02, S18, S22 |
| D157 | Novum taşıyıcısı tek kare testini geçmiyordu | Alıcı ekranında RECEIVED 12:00:00 / SENT 12:08:00 gösterilecek | S03, S08 |
| D174 | Yön "screen-right" verildi | Yönler kadrajdaki nesneye göre "toward A" / "toward B" tarif edilecek | S21, S26, S29, S34 |
| D198 | Sıfır-G nesne momentum | Halat ve serbest nesneler mikro yerçekimi eylemsizliğiyle hareket edecek | S21, S27, S34, S42 |
| D202 | Seçim ve bedel bedende okunmuyor | Kestrel'in EJECT düğmesine basarken tereddütü ve titreyen eli gösterilecek | S41 |
| D209 | Dünya çapası eksik | Dünya yörüngesi kadraj açısı sabitlenecek | S01, S09, S43, S48 |
| D210 | Kafiye çifti niyette kaldı | S01 ve S48 dış kadraj açısı kilitlenecek | S01, S48 |
| D211 | İlk 10s soru yok | S01'de doğrudan acil durum SOS mesajı başlayacak | S01, S03 |
| D216 | Ses miksi yazılmadı | Dış mekanda vakum sessizliği, iç mekanda kabin uğultusu | S01, S02, S43, S48 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar

| ders | neden bu filmde uygulanmadı |
|---|---|
| — | Tavan aşılmadı (10 kilit kullanıldı). |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| MARS_SON_CIKIS | T2 DEVAMLILIK | Kask vizörlerinin klip içinde kaybolması | Visor lock etiketi tüm kask sahnelerine eklenecek |
| THE_COLD_WELD | T6 FİZİK | Vakumda hava akıntısının abartılması | Kapak açılışında uzay rüzgarı yapılmayacak |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PB | Basınç patlaması görsel abartı | Nötr uzay acil durumu ve mekanik ayrılma | S42 |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        10 adet
QA ARIZASI:         2 adet
RED SINIFI:         1 adet
⛔ EN PAHALI ÜÇÜ:   D16 (YÜZ MORPH) · D198 (SIFIR-G) · D202 (BEDEL BEDENDE)
```
