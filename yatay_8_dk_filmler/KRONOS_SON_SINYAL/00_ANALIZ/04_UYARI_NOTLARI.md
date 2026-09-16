# ⚠️ KRONOS_SON_SINYAL — UYARI NOTLARI

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S41 | D202 · MERKEZÎ SEÇİM | Bedel bedende okunmuyor | Kestrel'in EJECT düğmenin kapağını açarken tereddütü ve titreyen eli gösterilecek | ✅ |
| 2 | S02, S18, S22 | D146 · VİZÖR BİÇİMİ | Vizör biçimi sayıyla yazılmadı | Vizör 180 derece şeffaf polikarbon dome olarak sayıyla tarif edilecek | ✅ |
| 3 | S03, S08 | D157 · NOVUM TAŞIYICISI | Tek kare testi geçilemiyor | RECEIVED 12:00:00 / SENT 12:08:00 saatleri tek makro kadrajda verilecek | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S01, S48 | D210 · KAFİYE ÇİFTİ | Açılış ve kapanış kadrajı uyuşmuyor | Kamera pozisyonu, lensi ve yüksekliği S01 ile S48'de birebir aynı yazılacak | ✅ |
| 2 | S21, S27, S34 | D198 · SIFIR-G | Nesnelerde sahte yerçekimi düşüşü | Serbest süzülen halat ve beden doğrusal eylemsizlikle hareket ettirilecek | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D216 | Dış mekanda vakum sesi üretilmesi | Tüm dış mekan sahnelerinde vakum sessizliği korunacak |
| D203 | Repliklerin imaj/video promptuna metin olarak yazılması | Replikler promptlara eklenmeyecek, ses miksinde eklenecek |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 | Var (Kestrel & Aras kaskları) | Kask ve vizör ölçüleri 180 derece polikarbon şeffaf dome olarak sayıyla yazıldı |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR | D59 | Yok | Kumaş kelimeleri yerine krem-gri poliamit katman terimleri kullanıldı |
| 3 | Optik aritmetiği hiç yapılmamış | OPEN CIRCUIT | Var | Macro shots 85mm, Medium shots 50mm, Wide shots 35mm olarak eşlendi |
| 4 | Uzak nesne ~60 piksel | D179 | Yok | Tüm kritik göstergeler (RX, EJECT) yakın veya makro kadrajda |
| 5 | Ayrım RENKLE kuruldu | BLIND BERTH | Var (Kestrel & Aras) | Kestrel petrol mavisi omuz bantsız, Aras turuncu omuz bantlı ve sakallı |
| 6 | Ortam kartının NEGATİF bloğu prompta girmemiş | UZAY_USSU | Var | Negatif prompt bloklarına "no atmospheric haze, no volumetric clouds" eklenecek |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | Var | ZAMAN teması S03, S08, S18, S46 sahnelerine bağlandı |
| 8 | Bedel var ama sahne numarası yok | B5 | Var | Bedel S41–S43 olarak kilitlendi |
| 9 | Yasak cümlesi yazıldı ("never drawn") | D123 | Yok | Yasak ifadeler yazılmadı, doğrudan pozitif tarifler verildi |
| 10 | Politika: nesne ADLANDIRILDI | D67 | Yok | Cihazlar formlarıyla tarif edildi |
| 11 | Replik zamanı ELLE yazıldı | D122 | Var | Replik zamanları formülle sahne zamanına bağlandı |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI | Var (S35/S36) | Kapak sıkışması sahne sınırlarına bölündü |
| 13 | Prompt "BIBLE'a bak" diyor | Kural ③ | Yok | Tüm promptlar self-contained olarak yazılacak |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg | D142 | Yok | Standart araçlar kullanılıyor |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Var | Deri ve dikiş bölgeleri kask içiyle sınırlandırıldı |
| 16 | 1 NUMARALI risk yalnız SIFATLA korunmuş | D192 | Var | MİKRO_YERÇEKİMİ_MOMENTUM en az 2 saniye kesintisiz doğrusal süzülme sayısı verildi |

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşındı
☑ tekrar eden arıza tablosunun 16 satırının HER BİRİ cevaplandı
→ 05_SAHNE_CALISMALARI/ açılabilir.
```
