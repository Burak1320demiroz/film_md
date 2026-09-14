# ⚠️ LOOK_UP — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S01 | D1 · D34 · D79 | Karakter adı & vizör kapalılığı | Commander/rookie ünvanları yazıldı, berrak vizör kilitlendi | ✅ |
| 2 | S06 | D139 · D172 | Sırt ünitesi ve kordon düğümü | Düz sırt paneli yazıldı, kordon braket boynuna kilitlendi | ✅ |
| 3 | S09 | D62 · D213 · D67 | Doruk aksiyon elipsi & politika | Shot A/B ayrımı yapıldı, nötr bıçak tarifi kullanıldı | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S02 | D16 · D42 | Bot kilit kopması | Sönümlü kıvılcım ve tutunma eylemi yazıldı | ✅ |
| 2 | S04 | D169 · D179 | 0g Efor & Kalkan pikseli | Kalkan kadrajda ≥280px tutuldu, atalet kadansı yazıldı | ✅ |
| 3 | S07 | D78 · D206 | Karar yönelimi | Mara'nın kapıyı bırakıp dönmesi kinesik seçimle yazıldı | ✅ |
| 4 | S10 | D70 | Kapı mühür sürtünmesi | Kalkan ile kapı aralığı fiziksel teması yazıldı | ✅ |
| 5 | S12 | D141 · D210 | C10 kimliği & Kafiye | Sol omuz gri çiziği korundu, S01 bakış kafiyesi kuruldu | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D45 · D138 | Metin sızması | Prompt gövdesine ve sahne arka planına hiçbir metin/yazı koyma |
| D79 · D175 | Vizör & Ten | Closed clear visor reveals face; no skin exposure outside suit |
| R1-R5 | Referans tutarlılığı | 5 insan ve 10 yaratık referans paketi kilitleriyle üretilecek |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 | R1 & R3 paketleri oluşturuldu | Görsel kilitler referans sayfasına bağlandı |
| 2 | Yasak kelime dalgalandırılıyor | D59 · D153 | Kumaş/dalgalanma terimi kullanılmadı | Grafit dokuma tekstil ve sert paneller tarif edildi |
| 3 | Optik aritmetiği yapılmamış | OPEN CIRCUIT | Tüm sahnelerde yapıldı | Kadraj eni ve piksel değerleri sığma denetiminden geçti |
| 4 | Uzak nesne ~60 piksel | D179 | Çapalar ≥100px tutuldu | Kalkan 280px, kesici 400px, yüz 380px kilitlendi |
| 5 | Ayrım RENKLE kuruldu | BLIND BERTH | Donanım ve şeritlerle kuruldu | Mara dikey şerit, Noah sarı çapraz şerit ile ayrıldı |
| 6 | Ortam kartı NEGATİF bloğu girmemiş | UZAY_USSU §6 | Negatif bloklara eklendi | Maket/tilt-shift negatif kısıtlamaları yazıldı |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | İndeksler bağlandı | Motif sahneleri S01, S07, S09, S10, S11 bağlandı |
| 8 | Bedel var ama sahne numarası yok | 03_PLAN_ONCESI | Numaralar bağlandı | Bedeller S02, S06, S08, S10 bağlandı |
| 9 | Yasak cümlesi yazıldı | D123 | Yasak cümlesi kurulmadı | "never drawn" yerine pozitif kilit kullanıldı |
| 10 | Politika: nesne ADLANDIRILDI | D67 | FORMU tarif edildi | "guarded utility blade" ve "hooked claw" tarif edildi |
| 11 | Replik zamanı ELLE yazıldı | D122 | Formülle yazıldı | hook + (n-1)*10 + offset formülü uygulandı |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI | Shot A/B ayrıldı | S01, S06, S09, S12 iki çekime bölündü |
| 13 | Prompt "BIBLE'a bak" diyor | kural ③ | Self-contained | Bütün promptlar bağımsız biçimde yazıldı |
| 14 | Makine kapısı kurulmayan ffmpeg | D142 | İnceleme yapıldı | Kurulum dökümü doğrulandı |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Çıplak ten negatifte | Bare skin negatifi bölge olarak kilitlendi |
| 16 | 1 NUMARALI risk sıfatla korunmuş | D192 | Sayısal yazıldı | 5 insan, 10 yaratık, 1 gri çizik kilitlendi |

---

## ✅ KAPI

```
[x] 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
[x] 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
[x] tekrar eden arıza tablosunun HER satırı cevaplandı (16 satır)
→ üçü de ✅: 05_SAHNE_CALISMALARI/ açılabilir.
```
