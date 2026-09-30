# 🧾 THE_INWARD_FALL — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Etiketi filme uymayan ders çizelgede "—" alır.

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D1 | AI klip içi montaj kesmesi üretiyor | Her klip tam 10.0 saniye tek kesintisiz çekimdir, klip içi kesme 0 | K01–K24 (tüm klipler) |
| D16 | Kask arkasında yüz morfolojisi değişiyor | Vizör altın reflektif kaplamadır, kask içi yüz morfolojisi sabittir | S1, S2, S4, S5 |
| D34 | Karakter özel adı jenerik kartı üretiyor | Karakter isimsiz teknisyendir; promptlarda özel ad veya başlık geçmez | K01–K24 |
| D42 | Giysi aşınması her klipte sıfırlanıyor | Eldiven silikonundaki çizikler ve aşınma klip geçişinde korunur | S2, S3, S4, S5, S6 |
| D62 | Kurguda en çok final sahnesi düşüyor | S6 tahliye kovanı kilitleniş sahnesi kurguda asla atlanamaz | S6 (K21–K24) |
| D70 | Jenerik kartı kurguya geri dönüyor | Ekran metni 0.0s; hiçbir klipte açılış/kapanış kartı bulunmaz | K01–K24 |
| D78 | Novum ve sayaç tek karede kanıtlanmadı | Devir sayacı ve düşen pimin yana sapması tek karede görsel kanıtla | S1 (K01, K04) |
| D138 | Metin yasağı yalnız giysiyi koruyor | No readable text, letters, digits, numbers or symbols on any surface | K01–K24 |
| D139 | Düz sırt kilidi arkadan çekimde deliniyor | Arka açıda sırt birleşik düz kompozit paneldir, sırt ünitesi yoktur | S2, S3, S5 |
| D146 | Dikişsiz vizör kubbe halüsinasyonu tetikler | Vizör kompozit kask çerçevesine entegre küresel altın aynadır | S1, S3, S4, S5 |
| D157 | Novum taşıyıcısı TEK KARE'de geçmiyor | Düşen çelik pim × merdiven tırabzanı yana sapma hareketi | S1 (K01, K04) |
| D169 | Efor fiili var ama gövde tepkisi yok | Tırmanışta parmak kavrama sertliği ve koldaki gerilim sayısal verilir | S3, S4, S5 |
| D174 | "Screen-right" modelde yön tutmuyor | Yön kadrajdaki dikey tırmanış merdiveni ve merkez aks referansıyla verilir | S2, S3, S4, S5 |
| D175 | "Through the glove" deriyi çizdiriyor | Eldiven kalın silikon kompozittir; deri veya tendon kelimeleri kullanılmaz | S2, S3, S5 |
| D192 | 1 numaralı risk tarif kilidiyle korunmadı | Coriolis yana savrulması sıfatla değil süre (0.9s) ve mesafe (0.6m) ile yazılır | S1, S3, S4 |
| D206 | Bedel bedende ödenmiyor | Emniyet mandalını kesme eylemi kolda sarsıntı ve gövdede savrulmayla ödenir | S5 (K20) |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D203 | Filmde diyalog veya sesli telsiz repliği yoktur (0 replik). |
| D217 | Replik bulunmadığı için ekranda olanı söyleme riski yoktur. |
| D172 | Taşıyıcı nesne bağımsız düşen bir çelik pimdir, kordon taşımaz. |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_SIGNAL_KEEPERS` | ⑨ KADRAJ | Ardışık kurulumlarda açı ve ölçek sıçraması | Kurulumlar arası açı yayında ardışık çiftler tam 1 kademe tutulur |
| `THE_HEAVY_SIDE` | ⑥ FİZİK | Dönme yerçekiminde yana sapmanın soyut kalması | Serbest pimin yana düşüşü net süre (0.9s) ve sapma mesafesiyle (0.6m) tanımlanır |
| `GUNES_MEZARI` | ④ HİKAYE | Bedelin fiziksel görünürlüğünün gecikmesi | Emniyet kordonunun kesilişi ve manyetik botun serbest kalışı kadrajda net gösterilir |
| `THE_DEEP_PRESSURE` | ① KARE | Plan dosyası ile kurgu sahne sayısı uyuşmazlığı | 24 klibin tamamı plan, sahne tablosu ve bölüm dosyalarıyla birebir hizalanır |
| `THE_COUNTED_RIVET` | ⑤ ARKA PLAN | Devasa yapıda ölçek kaybı ve arka plan erimesi | Dairesel halkanın 60 metrelik içbükey eğriliği her geniş açıda sabit tutulur |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika Kelimesi) | Bıçak/kesici alet sözcükleri | Endüstriyel kablo serbest bırakma mandalı / mekanik kovan kilidi | S5 emniyet kordonunu kesme anı |
| YR (Yüz/İsim Reddi) | Belirli insan kimliği veya isim | İsimsiz EVA bakım teknisyeni (unnamed space technician) | S1, S2, S4 kask yakın çekimleri |
| MÇ (Model Çarpışması) | "through the suit/glove" saydamlık | "conducted across the thick silicone grip" formülasyonu | S3 tırabzanı kavrama anı |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        16 adet (tavan ≤ 20)
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
```
