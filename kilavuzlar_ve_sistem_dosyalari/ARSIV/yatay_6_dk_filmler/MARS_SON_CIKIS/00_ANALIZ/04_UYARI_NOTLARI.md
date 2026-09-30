# ⚠️ MARS_SON_CIKIS — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md` (bu filmde ne var).

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S26-S32 | D192 · THE_HOLLOW_COUNT | Manuel kenetlenme yaklaşma hızı sıfatla yazılırsa model kontrolsüz süzülme üretir | S26-S32 arasında mesafe ve hız sayıyla yazılacak (7.5m -> 1.5m -> 0.15 m/s -> temas) | ✅ |
| 2 | S14-S36 | D206 · THE_HOLLOW_COUNT | Aras'ın kol sakatlığı kesmelerde unutulup kol hareketli üretilebilir | Aras'ın sol kolu S14 sonrasında askı kayışına sabitlenmiş olarak kilitlenecek (Kapatılamaz Bedel) | ✅ |
| 3 | S01-S36 | D139 · THE_LAST_SHIFT | Giysi sırtındaki aksesuarlar model tarafından rastgele sırt ünitesine dönüştürülebilir | Sırt "one continuous smooth panel from collar to hip" olarak pozitif kilitlenecek | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S10, S11 | PK (Politika Kapısı) | Elektrik yangını patlama gibi algılanıp içerik filtresine takılabilir | "Elektrik ark parlamaları ve havalandırma Izgarasından yoğun siyah duman yükselişi" nötr tanımı yapılacak | ✅ |
| 2 | S23, S24 | D78 · D157 | Otomatik navigasyon sapması ekranda anlaşılmayabilir | Ekranlarda kırmızı ikaz ve sayısal veri sapması I2V başlangıcında gösterilecek | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D146 | Vizör biçimi kare kare değişebilir | Kirli beyaz kask, koyu dikey şerit ve şeffaf vizör geometrik oranla kilitlenecek |
| D167 | Karakterlerin ünlü benzerliği çıkabilir | Lena 4, Aras 4 temel ayırt edici görsel especially tarif edilecek |
| D174 | Camera screen-right/left sapması | Yönler Kestrel burnu, Horizon omurgası ve Mars yüzey çapasından tanımlanacak |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 | Evet (Kask, Vizör, Donanım) | MARS_SON_CIKIS_REFERANS_PAKETI.md yazılacak |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR | D59 | Evet (Astronot Giysileri) | Dokuma zırh katmanları esnek grafit eklemlerle pozitif tarif edilecek |
| 3 | Optik aritmetiği yapılmamış | OPEN CIRCUIT | Evet (Habitat & Kokpit) | İç mekânda 28mm/35mm, dış mekânda 24mm/50mm lens sınırı kondu |
| 4 | Uzak nesne ~60 piksel ekranda okunmuyor | D179 | Evet (Horizon Gemisi) | S21'de Horizon geniş silüet, S26'da 7,5m yakın kitle olarak boyutlandırıldı |
| 5 | Ayrım RENKLE kuruldu, koyu gövde ayrılmıyor | BLIND BERTH | Evet (Lena & Aras) | Lena petrol mavisi yan panel + dar omuz; Aras oksit turuncu omuz + geniş gövde |
| 6 | Ortam kartının NEGATİF bloğu prompta girmedi | UZAY_USSU | Evet (Mars & Uzay) | Uzay sahnelerinde starfield bloom yasağı ve filigran negatifi eklenecek |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | Evet (Tamamlayıcı Eylem) | Tema S01, S14, S24, S31, S36 sahnelerine bağlandı |
| 8 | Bedel var ama sahne numarası yok | B5 | Evet (Kol sakatlığı) | Bedel S14, S16 sahnelerine net bağlandı |
| 9 | Yasak cümlesi yazıldı | D123 | Evet (Yangın & Red) | Yasak cümlesi yerine nötr görsel nesne ve eylem tarifi yazılacak |
| 10 | Politika: nesne ADLANDIRILDI | D67 | Evet (Yangın) | Servis kabininde elektrik arkı ve duman yükselişi biçimsel tarif edilecek |
| 11 | Replik zamanı ELLE yazıldı | D122 | Evet (7 Replik) | Replik zamanları formülle (00:03, 00:15, 02:05 vb.) türetildi |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI | Evet (36 Sahne) | Durum değişimleri 0-3s, 3-7s, 7-10s zaman hücrelerinde bölümlendi |
| 13 | Prompt BIBLE'a bak diyor | kural ③ | Evet (Promptlar) | Her prompt self-contained tam görsel tarif taşıyacak |
| 14 | Makine kapısı ffmpeg filtresine yazıldı | D142 | Uygulanmıyor | FFmpeg filtresine bağımlı makine kapısı yok |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Evet (Astronot Giysileri) | Basınç giysisi tam kapalı, eldiven ve kask kilitli tarif edilecek |
| 16 | 1 NUMARALI risk yalnız SIFATLA korunmuş | D192 | Evet (Kenetlenme Hızı) | S26-S32 hızı 7.5m -> 1.5m -> 0.15 m/s sayıyla kilitlendi |

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak işaretlendi
✅ Tekrar eden arıza tablosunun 16 satırı da cevaplandı
→ 05_SAHNE_CALISMALARI/ açılabilir.
```
