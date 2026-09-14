# 🧾 THE_TETHERED_MASS — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D197 | Vizör opaklık kayması | Astronot kask vizörü film boyunca %100 şeffaf kalacak, iç yüzey yansıması hafif tutulacak | S01, S04, S07, S09, S11 |
| D198 | Sıfır-G momentum kilidi | Vakumda halat bağlıyken gerilim liflerde titreşim olarak ilerleyecek, kopan lif beyazlaşıp kıvrılacak | S00, S06, S10, S11, S15 |
| D200 | Yerçekimi çelişkisi | Çekici gemisi ile istasyon arasında Dünya atmosfer çizgisi sabit alt eksen çapa olarak kalacak | S00-S15 |
| D201 | Güneş ışığı flip arızası | Vakum ortamında güneş ışığı açısı (sol üst 45 derece) tüm uzay sahnelerinde sabit tutulacak | S00, S01, S05, S10, S12, S14 |
| D202 | Görünmez seçim yasağı | B5 seçimi ve bedeli astronotun fiziksel eylemiyle (manuel pimi çekme, kapağı kırma) gövdede okunacak | S04, S07, S09, S11 |
| D146 | Biçim kilidi kaybı | Astronot basınç giysisi (göğüs paketi, rol şeridi) ve halat tamburu referans pakediyle kilitlenecek | S01, S03, S06, S11 |
| D179 | Okunurluk / Optik arızası | Dar kokpit sahnelerinde 85mm, uzay ölçek sahnelerinde 24mm kullanılacak; ana nesne ≥100px olacak | S00-S15 |
| D67/D123 | Politika kelime tuzağı | Promptlarda "no fire/no magic" gibi negatif yasaklar yerine pozitif form tanımları yazılacak | Tüm promptlar |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_SINKING_STAKE | ② Devamlılık | Göğüs paketi S13'te değişiyor (Referans pakedi üretilmediği için) | Referans pakedi KAPI 0 olarak yazılacak ve seed kilitlenecek |
| THE_OPEN_CIRCUIT | ⑨ Kadraj / Optik | 64m üs 5.9m kadraja sığdırılmaya çalışıldı | 24mm prime lens ile ölçek şahidi (1H = astronot) kullanılacak |
| THE_COLD_WELD | ⑩ Oyunculuk | Karar anında astronotun yüzü/bedeni nötr kaldı | Titreyen el kapağa gider, nefes vizörde buğu yapar, kilit çekilir |
| THE_GRAVITY_ANCHOR | ③ Ses | Vakum ortamında dış ses katmanı kullanıldı | Vakum sahneleri tamamen sessiz + 28Hz sub-bass, ses yalnız kask içinde |
| THE_HOLLOW_STATION | ⑤ Arka Plan | İstasyonun modüler detayları sahneler arası değişti | İstasyon tarım-habitat modülleri grid kılavuzuyla sabitlenecek |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| MÇ (Motor Çan) | Motor alevi / patlama efekti | Alev yerine "red heat glow on nozzle, micro-fractures, coolant gas vapor venting" | S02, S06, S08 |
| PK (Patlayıcı Kilit) | Patlayıcı fünye / yangın | Kıvılcım yerine "mechanical latch release, pneumatic decoupling, sudden separation shock" | S11 (Halat release) |
| YR (Yüzey Reddi) | Hava ve rüzgar efekti | Vakum ortamı için "zero wind, motionless floating debris, rigid metallic cable" | S00, S10, S15 |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        8 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   D197 (Vizör Opaklığı) · D202 (Bedende Okunan Seçim) · MÇ (Motor Patlaması Alev Yasağı)
```
