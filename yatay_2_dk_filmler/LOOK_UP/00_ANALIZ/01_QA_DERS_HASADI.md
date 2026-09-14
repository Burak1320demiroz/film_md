# 🧾 LOOK_UP — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D1 | Tek çekim AI kesmesi yasak | Shot A ve Shot B timeline ofsetleriyle ve farklı vizör yönleriyle ayrılır | S01, S06, S09, S12 |
| D16 | Bot mekanizması kopması | Bot kilidi kopunca tutamağa tutunma mekaniği sayısal anlatılır | S02 |
| D34 | Karakter özel adı kullanımı | Promptlarda commander / rookie genel görsel ünvanları kullanılır | S01–S12 |
| D42 | Kıvılcım / sprey sapması | Atışlarda sönümlü namlu parlaması tarif edilir | S02, S04 |
| D45 | Prompt iskeleti ekrana sızması | Prompt gövdesine etiket / metin yazılmaz | S01–S12 |
| D62 | Doruk kurgu eksikliği | Kordon kesme ve kalkan devri Shot A/B olarak ayrılır | S09 |
| D67 | Politika nesne adı tuzağı | Pençe ve bıçak nötr form ile tarif edilir | S01, S06, S09 |
| D70 | Kapı mühür sürtünmesi | Kalkan ile kapı aralığı fiziksel teması sayısal yazılır | S10 |
| D78 | Görsel şok ve azimut sıçraması | S1-S2 ve S6-S7 geçişlerinde 28mm-50mm ölçek kademesi korunur | S02, S03, S07 |
| D79 | Vizör şeffaflığı & sırt paneli | Clear closed visor reveals face; back of suit is smooth single panel | S01–S12 |
| D122 | Replik zamanlaması | 12 replik zamanı ızgara formülüyle yazılır | S01–S12 |
| D138 | Metin yasağı kapsayıcılığı | Panellerde ve giysilerde hiçbir yazı / harf yer almaz | S01–S12 |
| D139 | Düz sırt paneli kilidi | Continuous smooth back collar to hip panel | S01–S12 |
| D141 | Twist & döngü kilitleri | C10 sol omuz gri çiziği S03 ve S12'de korunur | S03, S12 |
| D169 | Efor bedeni fiziksel anlatımı | Düşük yerçekiminde atalet ve kütle çekiş kadansı yazılır | S04, S05, S06, S08 |
| D172 | Taşıyıcı braket sıkışması | Kordon boşluktaki düğüme değil braket boynuna wedging yapar | S06 |
| D175 | Çıplak deri negatifi | Ten alanları giysi dışı verilmez | S01–S12 |
| D179 | Çapa optik eni ve pikseli | Kalkan ve carabiner kilitleri kadrajda ≥100px tutulur | S04, S07, S08 |
| D206 | Karar anı dikey yönelimi | Mara'nın kapıyı bırakıp dönmesi kinesik seçimle anlatılır | S07 |
| D210 | Kafiye çifti ve lockoff | S01A kapı bakışı ↔ S12A tavan bakışı kafiyesi kurulur | S01, S12 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D213 | Aksiyon elipsi kilidi S09'da uygulandığı için tavan aşılmadı |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| HERD | ① KARE | Gemi park yeri keyfî değişti | İstasyon şaftı ve asansör kapısı sabit uzamsal haritada kilitlendi |
| HOLDING FIELD | ② DEVAMLILIK | Giden gemi park hâlinde döndü | 5 astronotun kask şeritleri ve donanım tarafları sabit tutuldu |
| BRIGHT TETHER | ⑨ KADRAJ | Üç kurulum da aynı açıdan bakıyordu | 5 farklı açı tipi (Eye level, Low angle, High angle, 3/4 Elevated, Close-up) kullanıldı |
| SKYLIGHT | ① KARE | Kask vizörü kare kare değişti | R1 referans paketiyle berrak vizör camı kilitlendi |
| STANDING WIRE | ⑤ ARKA PLAN | İki astronotun dikey şeritleri karıştı | Mara tek dikey şerit, Noah çift çapraz sarı şerit ile ayrıldı |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika) | Bıçak / silah adlandırma | Nötr form tarifi (guarded utility blade) | S09 (Kordon kesme) |
| PB (Politika Biyolojik) | Yaratık ağız/kan detayı | Organik kompozit yüzey ve tırnak yapısı | S01, S05, S10 |
| KT (Kesme/Geçiş) | Tek çekimde AI kesmesi | Shot A/B ayrımı ve timeline offset | S01, S06, S09, S12 |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   D79 (Vizör/Sırt) · D169 (0g Efor) · D146 (Biçim Kilidi)
```
