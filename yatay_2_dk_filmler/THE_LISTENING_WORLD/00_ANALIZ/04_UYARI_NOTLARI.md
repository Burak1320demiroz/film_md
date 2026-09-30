# ⚠️ THE_LISTENING_WORLD — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S0-S15 | D146 · SKYLIGHT | Seamless vizör kubbe davetiyesi | Opak vizör metalik dış çerçeve contası ve geometrik yuva ile kilitlendi | ✅ |
| 2 | S8, S10, S11, S12 | D78 · THE_LOCKED_PULSE | Sinyal ritminin sayılamaması | Beyaz verici flaşları ile turkuaz yanıt darbeleri saniye aralıklarıyla kompozit notuna bağlandı | ✅ |
| 3 | S0-S15 | D209 · THE_COLD_BURN | Buzda dünya ve yön çapası kaybı | EREON gezegeni ve ufuktaki dev kaya sütunları sabit yön çapası yapıldı | ✅ |
| 4 | S5 | D36 · VAKUM | Buz püskürmelerinin duman gibi kıvrılması | Gayzerler vakumda balistik düz koni olarak dağılmadan yükselir | ✅ |
| 5 | S0-S15 | D70 · THE_LAST_SHIFT | Kurguda sahnelerin düşmesi | 16 klip tam 10.0 saniye, 160 saniye toplam süre olarak kurgu kapısında kilitlendi | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S1, S14 | D214 | Yakın planda kadraj dışı beden uzuvlarının tarif edilmesi | Yalnızca kadrajdaki eldiven, cihaz veya ince buz penceresi tarif edilecek | ✅ |
| 2 | S9 | D202 / D206 | Karakter bedelinin bedende okunamaması | Astronotun omuzlarının çökmesi, nefes ritminin yavaşlaması beden diliyle verilecek | ✅ |
| 3 | S13 | D174 | Kuşbakışı açıda vadi bağlantısının kopması | Geçilen kanyon, sütunlar ve gayzer yarıkları tek bir coğrafi eksende birleştirilecek | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D180 / §3.1 | Vakumda dış uzay seslerinin ve motor gürültüsünün üretilmesi | Dış ses post-prodüksiyonda tamamen sıfırlanacak; kask içi soluk ve bas dron ile mikslenecek |
| D201 | EREON gezegeninin açısının sahneler arasında rastgele dönmesi | Gezegen gökyüzünde sabit bir kuzey-doğu kerterizi olarak korunacak |
| D45 | Promptlara estetik ve kalite sıfatlarının sızması | Yalın, fiziksel ve eylem odaklı İngilizce prompt dili kullanılacak |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 · SKYLIGHT | Kask ve giysi var | Koyu turuncu kumaş + kırık beyaz omuz + gömülü metalik çerçeveli %100 opak siyah vizör |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR | D59 · D153 | Giysi kumaşı | "fabric" veya "cloth" yerine "heavy rigid pressurized ballistic nylon shell" |
| 3 | Optik aritmetiği yapılmamış | OPEN CIRCUIT | Geniş manzaralar | Kadraj enleri 24mm-50mm lenslerle hesaplandı, ana nesneler >100 px |
| 4 | Uzak nesne ~60 piksel | D179 | Küçük astronot | Çok geniş planlarda dahi astronotun turuncu rengi ve parlak kaskı kontrastla ayrılır |
| 5 | Ayrım RENKLE kuruldu | BLIND BERTH | Tek insan var | İkinci insan yok; çevre beyaz buz ve siyah kaya ile giysiden ayrılır |
| 6 | Ortam kartının NEGATİF bloğu prompta girmedi | UZAY_USSU §6 | Vakum ortamı | Mutlak siyah gölgeler ve motivasyonsuz dolgu yasağı her prompta işlendi |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | Yalnızlık ve Bağlantı | Motif sahneleri açıkça indekslendi: S0, S7, S14 |
| 8 | Bedel var ama sahne numarası yok | 03_PLAN_ONCESI B5 | Sessiz bekleyiş | Bedel doğrudan S9 sahnesine indekslendi |
| 9 | Yasak cümlesi yazıldı ("never drawn") | D123 | Güvenlik | Yasak yerine pozitif eylem kilitleri yazıldı |
| 10 | Politika: nesne ADLANDIRILDI | D67 | Ölçüm cihazı | "sensor/scanner" yerine "compact matte grey rectangular telemetry box" |
| 11 | Replik zamanı ELLE yazıldı | D122 | Tek replik | S14 replik formülüyle 145.0 saniye olarak hesaplandı |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI §1 | Işık atımları | Durum değişimleri klip sınırlarına veya net saniyeli flaşlara bağlandı |
| 13 | Prompt "BIBLE'a bak" diyor | kural ③ | Prompt dili | Her prompt kendi IN FRAME ve nesne tarifini tam taşır |
| 14 | Makine kapısı KURULU OLMAYAN filtre | D142 | ffmpeg | Özel filtre bağımlılığı yok |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 · ㉑ | Astronot giysisi | Bilekler ve boyun metalik contalarla kapatıldı, ten tamamen yasaklandı |
| 16 | 1 NUMARALI risk yalnız SIFATLA korunmuş | D192 · OPEN CIRCUIT | Ritim süreleri | Sinyal süreleri sayıyla verildi: 0.5s kısa, 1.6s uzun |

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
✅ tekrar eden arıza tablosunun 16 satırının tamamı cevaplandı
→ üçü de ✅, 05_SAHNE_CALISMALARI/ açılabilir.
```
