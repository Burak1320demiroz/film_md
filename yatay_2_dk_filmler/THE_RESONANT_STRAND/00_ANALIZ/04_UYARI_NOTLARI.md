# ⚠️ THE_RESONANT_STRAND — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S00-S13 | DERS 197 | Vizör opaklığının kare kare değişmesi ve dış yüz görünmesi | Vizör prompt metninde "sealed gold-reflective EVA helmet visor, zero face visible" olarak kilitlenir. | ✅ |
| 2 | S00, S03, S07, S12 | DERS 198 / DERS 200 | Rezonansa giren nesnelerin rastgele sarsılması veya düşmesi | Prompt metninde "laminar acoustic resonance lift along parallel vector, no rotation, no gravity drop" kelimeleri verilir. | ✅ |
| 3 | S06, S08, S09 | RED YR (Yapısal Red) | Varlığa insansı organlar (göz, ağız, kol) eklenmesi | Varlık V2 promptunda "featureless translucent silicate bell mantle, 3 ribbon fins, zero eyes, zero face, zero mouth" kilitlenir. | ✅ |
| 4 | S12 | DERS 202 | Astronotun bedel seçiminin ekranda eylemsiz kalması | Chen'in güvenlik tether'ını sökme hareketi "hands unlatch metal carabiner clip from waist harness" olarak mikro-kinesik tanımlanır. | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S00 - S13 | DERS 201 | Ochre atmosferde ışık açısının flip etmesi | Güneş ışığı açısı "key light from top-left at 30 degree elevation" olarak ortak stilde sabit tutulur. | ✅ |
| 2 | S02, S05, S07 | THE_TETHERED_MASS | Yoğun toz bulutunun maket etkisi yapması | Volumetrik ışık ve hygroscopic toz "ochre volumetric haze, true scale atmospheric depth" diliyle verilir. | ✅ |
| 3 | S06, S09, S11 | THE_CANOPY_WORLD | Devasa varlık kadrajlandığında ölçeğin kaybolması | Kadraj daima 15° alt açı (low-angle) ve ön planda pod/astronot ölçek şahidi (1H = 1.8m) ile kurulur. | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| POLITIKA / PK | Motor kelime reddi | Şiddet/silah içeren fiiller yerine fiziksel nötr dalga ve rezonans tanımları kullanılacak. |
| V2 PROMPT | BİBLE referansı verme | Her sahne V2 promptu tamamen self-contained (kendi kendine yeten) yazılacak. |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT | VAR | `THE_RESONANT_STRAND_REFERANS_PAKETI.md` hazırlanacak ve seed/prompta kilitlenecek. |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 | VAR | "Ribbon fins" tanımında kumaş kelimesi kullanılmayacak; "silicate membrane fins" yazılacak. |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi | VAR | Devasa varlık sahnelerinde 24mm geniş lens, yakın sahnelerde 35mm lens kullanılacak. |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | VAR | Sensör kulesi ve wrist telemetri ekranı yakın plan kadrajlarda (medium close-up) gösterilecek. |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH | VAR | Koyu giysi üstüne parlak yeşil/altın telemetri şeridi ve ochre fon kontrastı verilecek. |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 | VAR | Uzay negatif bloğu ("no miniature, no tilt-shift, no studio lighting, no CGI artifact") eklenecek. |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | VAR | "Algının Ötesindeki Düzen" teması S03, S10 ve S12 sahnelerinin kinesik kararlarına bağlandı. |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | VAR | Bedel açıkça S12 olarak kilitlendi (tether mandalı sökümü). |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | VAR | Negatif cümleler nesne/fiil negatifi olarak yazıldı ("no weapons, no eyes, no face"). |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | VAR | Nesneler biçim ve malzemeyle tanımlandı ("shuddering titanium panel", "translucent silicate mantle"). |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | YOK | Replik yok (0/14). |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0.0687 | VAR | Klip içi aksiyon tek bir fiziksel eyleme sınırlandı (örn: S07 yalnız flare ateşleme ve duruş). |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | VAR | Tüm V2 promptları dış dosyaya atıf yapmadan 100% bağımsız yazıldı. |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı | D142 | YOK | ffmpeg komutlarında standart filtreler kullanılacak. |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | VAR | Karakter tamamen EVA giysisi içinde tutulacak, skin negatifi eklenecek. |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · A5 | VAR | A5 riski sayıyla yazıldı: "1000m genişlik, 300m boyunda 3 yüzgeç, 0 göz, 0 ağız". |

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
✅ tekrar eden arıza tablosunun HER satırı cevaplandı (16 satır)
→ 05_SAHNE_CALISMALARI/ açılabilir.
```
