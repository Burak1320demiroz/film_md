# 🧾 THE_STILL_POINT — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D1 | AI klip içi kesme uyduruyor | Her sahne bağımsız tek plandır, klip içi kesme yapılmaz, kesme kurguda yapılır | S00-S23 |
| D34 | Model jenerik ve başlık kartı ekliyor | Jenerik kartı ve metin yasağı hem gövdede hem negatifte vurgulanır | S00, S23 |
| D42 | Yıpranma her karede yeniden üretiliyor | Mat beyaz göğüs paneli ve turuncu aletteki aşınma dokusu sabittir | S00-S23 |
| D62 | Montajda en çok düşen sahne final | S23 final karesi (kapsül içi ve sakinleşen anahtar) ilk üretim sırasındadır | S23 |
| D70 | Üretim kilitleri kurguyu bağlamıyor | Kurguda ek kart konmaz, net süre 24 sahne × 10s = 240s olarak korunur | S00-S23 |
| D78 | Sahneler arası anlatım okunmuyor | Arabanın ters sürüşü ve hızın sıfırlanması merkez modül referansıyla kanıtlanır | S09-S11 |
| D139 | Düz sırt kilidi arkadan çekimde deliniyor | Arkadan açılarda sırt ünitesi tek parça kompakt panel olarak pozitif tarif edilir | S02, S08, S12, S15, S20 |
| D141 | Klip var vuruş yok | S17 Durgun Nokta anı net görsel vuruş olarak kilitlenir | S17 |
| D146 | "Seamless visor" kubbe davetiyesi | Opak parlak siyah dışbükey vizör; küresel kubbe vizör yasaktır | S00-S23 |
| D157 | Novumun taşıyıcısı tek karede geçmiyor | Bakım arabasının ters hızlanışı ve hız göstergesi tek karede okunur | S09-S11 |
| D167 | Fazla kimlik özgeliği ünlüye benzetiyor | Karakter kimliği 3 unsura kilitlenir: koyu gri giysi, beyaz göğüs, turuncu kol bandı | S01-S23 |
| D169 | Zorlanma sözlüğü bedende eksik | Zorlanma omuz gerginliği, eldiven sıkması ve ayak sabitleme ile verilir | S08, S12, S15, S20 |
| D174 | "Screen-right" referansı ters dönüyor | Yönler screen-right yerine merkez aks, halka yayı ve ray ekseniyle verilir | S00-S23 |
| D198 | Sıfır-g momentumu havada asılı kalma sanılıyor | Serbest süzülmede (S15-S19) balistik sabit hızlı ötelenme korunur | S15-S19 |
| D200 | Tek kadrajda iki yerçekimi çöküyor | Dönen halka (0.065g) ve sabit merkez (0g) aynı kadrajda bağımsız fizik sistemleridir | S03, S17, S19 |
| D210 | Kafiye çifti ve lockoff niyette kalıyor | S00 fırlayan anahtar ile S23 sakin süzülen anahtar kafiye çifti oluşturur | S00, S23 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D16 | Vizör tamamen opak siyahtır, kask arkasında yüz görünmez |
| D172 | Asılı kordon taşıyıcı olarak kullanılmamıştır |
| D203 | Film diyalogsuzdur |
| D217 | Film diyalogsuzdur |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_COUNTED_TURN | Scale & Physics | 0.065g yapay yerçekimi ile 0g serbest süzülme bölgeleri karıştı | Kadraj bölgelerine göre fizik kuralları kesin ayrılır |
| THE_LAST_SHIFT | Character | Sırt açılarında sırt ünitesi her karede büyüdü | D139 pozitif panel tanımı ile kilitlenir |
| THE_LEANING_ROOM | Camera | Dönme ekseni referansı kadrajda kayboldu | Arka plandaki merkez modül sabit çapa olarak korunur |
| THE_HOLLOW_COUNT | Lighting | Vakum gölgeleri yumuşadı ve dolgu ışığı eklendi | Tek sert Güneş ışığı ve mutlak siyah gölgeler korunur |
| THE_FIRST_DRIFT | Physics | Boşlukta süzülen figürün ivmesi duraksadı | Sürekli sabit hızlı doğrusal ötelenme kuralı yazılır |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK | Opak vizörün anonim maske sanılması | Teknik endüstriyel astronot kaskı pozitif tanımı | S02, S08, S17 |
| PB | Boşluğa savrulmanın kontrolsüz düşüş sanılması | Bilinçli balistik itiş ve hesaplanmış manevra dili | S12, S15 |
| TK | Kopan geçidin patlama hasarı sanılması | Mekanik yorulma ve gerilim kırılması olarak form tarif edilir | S01, S03 |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        16 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   D139 (düz sırt) · D200 (çift yerçekimi) · D146 (opak vizör)
```
