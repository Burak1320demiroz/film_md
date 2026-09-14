# 🧾 THE_RESONANT_STRAND — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| DERS 197 | Vizör opaklık/saydamlık kayması | Kask vizörü altın sarısı yansıtıcı zarda sabit tutulur; astronotun gözleri kask içi yeşil/mavi telemetri LED ışığı ile okunur, dış cilt görünmez. | S00 - S13 (Tüm Sahneler) |
| DERS 198 | Sıfır-G / Rezonans nesne momentum sapması | Rezonans ceplerine giren nesneler rastgele dönmez; akustik basınç dalga düzleminde yatay ve lamine biçimde yükselir. | S00, S03, S07, S12 |
| DERS 200 | Tek kadrajda iki farklı yerçekimi çelişkisi | Rezonansa giren nesneler yükselirken zemin tozu ve mineral zerreleri aynı frekansta havalanır; zemin ile hava çelişmez. | S03, S07, S12 |
| DERS 201 | Komşu sahnelerde ışık açısı sapması | Ochre sky ve ana güneş ışığı açısı kadrajın sol üstünden (30° açı) sabit gelir; sahneler arası gölge flip etmez. | S00 - S13 |
| DERS 202 | Seçim ve bedel bedende okunmuyor | S12'de astronot telemetri verisini kaydetmek için güvenlik tether'ını kilit mandalından kendi eliyle çözer; beden eforu ve seçimi fizikselleşir. | S12, S13 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_COLD_WELD.md` | Kare / Fizik | Rezonans alanında kütle havalanırken mikro-titreme ve görsel kopma | Prompt metninde kütle yükselişi "laminar acoustic resonance rise, smooth non-turbulent motion" ifadesiyle sabitlenir. |
| `THE_GRAVITY_ANCHOR.md` | Devamlılık | Karakter giysisi göğüs harness şeridinin sahneler arası kaybolması | Harness şeridi "dark grey EVA suit with chest telemetry panel, twin shoulder clips" olarak V2 prompt başlığında çapalanır. |
| `THE_MIRROR_FAUNA.md` | Arka Plan / Varlık | Modelin uzaylı varlığa rastgele göz/ağız eklemesi | Varlık tanımında "featureless translucent silicate mantle, smooth bell structure, zero eyes, zero face, zero appendages" kelimeleri kilitlenir. |
| `THE_CANOPY_WORLD.md` | Kadraj | Devasa varlık kadrajlandığında ölçek hissinin yitirilmesi | Kamera açısı daima 15° alt açı (low angle) ve ön planda astronot/pod ölçek şahidi (1H = 1.8m) ile kurulur. |
| `THE_TETHERED_MASS.md` | Isık | Yoğun atmosferde ışık huzmelerinin tutarsız kırılması | "Thick hygroscopic dust atmosphere with ochre volumetric light rays" stili tüm sahnelerde ortak çevre bloğunda verilir. |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika) | Şiddet veya saldırı içeren fiiller ("shoot", "blast", "attack") | Fiziksel nötr terimler ("emits acoustic pulse", "expands atmospheric membrane", "resonates") kullanıldı. | S06 (Varlığın ilk tırmanışı) |
| YR (Yapısal Red) | Şekilsiz biçimsiz kütle / yaratık karmaşası | Varlığın anatomisi netleştirildi: 1000m genişliğinde çan gövde, 3 adet 300m boyunda şerit yüzgeç. | S09 (Varlığın tam belirişi) |
| MÇ (Motor Çelişkisi) | İnsansı uzaylı/kollu-bacaklı organizma varsayımı | Organik yapı tamamen silikat/kristal zar ve biyolüminesans ışık şeritleriyle sınırlandı. | S11 (Yakın hizalanma) |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        5 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   DERS 197 (Vizör Opaklığı) · DERS 198 (Rezonans Kütle Momentum) · RED YR (Varlık İnsansılaşma Yasağı)
```
