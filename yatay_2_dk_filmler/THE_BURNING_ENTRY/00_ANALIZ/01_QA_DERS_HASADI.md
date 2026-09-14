# 🧾 THE_BURNING_ENTRY — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D36 | Vakumda dumanın yuvarlanıp kıvrılması | Vakumda roket itkisi ve plazma sızıntısı konik yayılır, kıvrılmaz, yuvarlanmaz | S00, S01, S02 |
| D38 | Hasarlı aracın uzayda toz gibi dağılması | Mekik hasarı sayılı ve sınırlıdır; gövde siluetini korur, sürekli parça saçmaz | S01, S03, S05, S07 |
| D39 | Parçacıkların su gibi akması/yuvarlanması | Vakum parçacıkları balistik ve düz hatlı ilerler; atmosferde yavaşça çökelir | S01, S03, S08, S09 |
| D42 | Kir ve çiziklerin sahneler arası yer değiştirmesi | Vizör ve kokpit paneli üzerindeki çizik/kir desenleri sabittir, hareket etmez | S00-S11 |
| D57 | Kask/giysi detaylarının kare 1 ile kare 300 arası değişmesi | Pilot kaskı ve uzay giysisi kare 1'den 300'e birebir aynı kalır; kask açılmaz | S00-S11 |
| D65 | Sahne içi sıçramalı kesme (jump-cut) | Her 10s klip tek bir kesintisiz kurgusal kamera hareketidir (single unbroken take) | S00-S11 |
| D159 | Kokpit ekranlarında yapay zeka harf çorbası | Kokpit göstergeleri ışıklı grafiksel telemetry çizelgeleridir; harf overlay yazılmaz | S00, S01, S07 |
| D45 | Köşeli parantez ders kodlarının prompta sızması | Prompt gövdesine [DERS n] veya [BIBLE] etiketi girmez, saf İngilizce yazılır | S00-S11 |
| D123 | Yasaklanan şeylerin prompta negatif olarak yazılması | Şiddet/zarar kelimeleri negatife bile yazılmaz; eylem pozitif fiziki kuvvetle ifade edilir | S00-S11 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_LAST_SHIFT.md` | Ritim / ASL | 2. dakikada aksiyon düşüşü ve ritim gevşemesi | S06-S11 arasında her 10s'de yeni somut fiziki engel (kanyon kulesi, tek itici, 3 kademeli darbe) |
| `THE_CRACKED_HELMET.md` | Görsel Devamlılık | Kask vizöründeki mikro çatlağın sahneden sahneye yer değiştirmesi | Çatlak S04'te pilotun göz hizasında başlar; koordinatı ve boyutu S04-S11 boyu kilitlenir |
| `THE_COLD_BURN.md` | Politika / Sözlük | Kask çıkarma ve zarar sözcükleri yüzünden Veo reddi | Kask asla çıkarılmaz, bedensel efor yalnızca parmak kasılması, nefes buğulanması ve G-kuvveti le ifade edilir |
| `THE_OPEN_CIRCUIT.md` | Spec Sadakati | Çizelge okumasının atlanması sonucu plan sadakati düşüşü | Kart A 00_ANALIZ pipeline adımları eksiksiz sırayla işletildi ve kilitler plan dosyasına taşındı |
| `LOSS_OF_LIFT.md` | Fizik & Görsel | Mekik irtifa düşüşünde arka plan kanyonunun jöle gibi dalgalanması | Kanyon duvarları ve zemin masif statik kaya olarak kilitlenir, arka plan dalgalanması engellenir |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK | `wounded ship`, `gore`, `blood`, `wounds` vb. kelimeler | Kelimeler tamamen silindi; pozitif fiziksel kuvvet tarifi yazıldı | S00, S01, S03 (Mekik hasar sahneleri) |
| PB | Kask çıkarma eylemi (`helmet off`) | Kask başa mühürlü kilitlendi; efor poşet/kol kumandasına aktarıldı | S04, S09, S11 (Çatlak ve çakılma sahneleri) |
| PK+PB | Replik içinde tehlike çığırtkanlığı | Sözel diyalog kaldırıldı; gerilim ses efektleri ve ışık renk değişimiyle sağlandı | S00, S01, S07 |
| PK | Karakter tanımında yedi kimlik niteliği üst üste (Kişi Tanımlama Yüzeyi) | Kesin boy/yaş yerine göreli astronot giysisi zırh geometrisi ve vizör içi ışık yazıldı | S00-S11 (Pilot kadrajları) |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        9 adet
QA ARIZASI:         5 adet
RED SINIFI:         4 adet
⛔ EN PAHALI ÜÇÜ:   Kask Çıkarma Yasağı (PB) · Vizör Çatlağı Koordinat Kilidi (Devamlılık) · Şiddet/Zarar Sözlüğü Yasağı (PK)
```
