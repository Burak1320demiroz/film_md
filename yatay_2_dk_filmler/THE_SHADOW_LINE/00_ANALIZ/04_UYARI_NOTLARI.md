# ⚠️ THE_SHADOW_LINE — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S00 | D200 / D211 | Vakumda duman süzülmesi ve zayıf hook | Plazma ışığı temas anında turuncu buhar anında dağılacak şekilde tarif edilecek | ✅ |
| 2 | S08 | D192 / D146 | Mandal mekanizmasının aşırı küçük kalması ve okunmaması | Toggle latch mandalı 85mm yakın lens ve sayıyla kadraj oryantasyonu ile belirginleştirilecek | ✅ |
| 3 | S10 | D202 / D213 | Bedelin eliptik kalması / kadraj dışına çıkması | Eldiven parmaklarının plazma ışığına girişi ve temas anı kadraj tam ortasında gösterilecek | ✅ |
| 4 | S12 | D206 / D141 | Bedelin beden dilinde kalıcı görünmemesi | Mühendisin bükülmüş parmaklarını açamaması ve gölge hattının gerilemesi net kapatılacak | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S01 | D208 | Kask vizörü renginin değişmesi | Gold reflective visor kask visual seed ile sabitlenecek | ✅ |
| 2 | S02 | D209 | Yönün soldan sağa kayması | Kamera ve astronot depar yönü Ekran Solundan Ekran Sağına kilitlenecek | ✅ |
| 3 | S06 | D192 | Gölge çizgisinin bulanıklaşması | Knife-edge sharp shadow line prompt metninde sayıyla korunacak | ✅ |
| 4 | S11 | D216 | Soğutma sıvısı sesinin eksik kalması | Yeşil sıvı püskürmesi ve vana açılma mekanik sesi 5 katmanlı mixe yazılacak | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D200 | Vakum ortamında yanlış fizik (toz, hover parçacık) | Tüm prompt negative bloğuna `floating dust, smoke hovering, space debris particle trails` eklenecek |
| D214 | Kadrajda olmayan organ/giysi tarifi | Kadraj dışı beden elemanları prompta kesinlikle yazılmayacak |
| D215 | Prompt içi HUD / yazı talimatı | HUD ve filigran ifadeleri prompt cümlesi yerine araç parametresine bırakılacak |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 | Uygulanıyor | Astronot giysisi ve mandal referans paketi visual seed ile kilitlendi |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR | D59 | Uygulanıyor | Uzay giysisinde kumaş kelimesi kullanılmadı, sert kabuk ve karbon fiber esnek eklem yazıldı |
| 3 | Optik aritmetiği hiç yapılmamış | OPEN CIRCUIT | Uygulanıyor | Odak uzaklığı ve kadraj ölçeği her sahne için optik kurallara göre seçildi (24mm-85mm) |
| 4 | Uzak nesne ~60 piksel | D179 | Uygulanıyor | Mandal ve valf gibi kilit nesneler 50mm ve 85mm yakın çekimlerde kadraja alındı |
| 5 | Ayrım RENKLE kuruldu | ASTRONOT_DONANIM | Uygulanıyor | Beyaz sert kabuk giysi zifiri gölgede yüksek siluet ve altın vizör kontrastı ile ayrıldı |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş | UZAY_USSU §6 | Uygulanıyor | Uzay vakum negatif bloğu (~1,970 karakter) tüm promptlara eksiksiz eklendi |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | Uygulanıyor | FEDAKÂRLIK teması S09-S10-S12 sahneleriyle doğrudan indekslendi |
| 8 | Bedel var ama sahne numarası yok | 03_PLAN_ONCESI | Uygulanıyor | Bedel açıkça S10 ve S12 sahnelerine bağlandı |
| 9 | Yasak cümlesi yazıldı ("never drawn") | D123 | Uygulanıyor | Yasak cümleleri pozitif aksiyon ve görsel tanımlara dönüştürüldü |
| 10 | Politika: nesne ADLANDIRILDI | D67 | Uygulanıyor | Formlar ve materyaller fiziksel nitelikleriyle tarif edildi |
| 11 | Replik zamanı ELLE yazıldı | D122 | Uygulanıyor | Replik bulunmuyor (sessiz film) |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI | Uygulanıyor | Durum değişimleri sahneler arası sınır satırlarına işlendi |
| 13 | Prompt "BIBLE'a bak" diyor | kural ③ | Uygulanıyor | Her prompt self-contained şekilde tüm tanımları taşır |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı | D142 | Uygulanıyor | Standart ffmpeg komutları belirlendi |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Uygulanıyor | Negatif bloğuna bare skin, exposed human face eklendi (S12 haricinde) |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş | D192 | Uygulanıyor | Gölge hattı 45 derece açı ve 0.5s kayma hızı gibi sayılarla tanımlandı |

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (16 satır)
→ üçü de ✅ ise 05_SAHNE_CALISMALARI/ açılabilir
```
