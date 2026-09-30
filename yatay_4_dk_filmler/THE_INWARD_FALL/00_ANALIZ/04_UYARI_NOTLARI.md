# ⚠️ THE_INWARD_FALL — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır:
> **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.** Üçünden biri
> yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S1 (K01) | D157 · THE OPEN CIRCUIT §Novum | Model serbest düşen pimi dikey düşürür veya rastgele savurur | Pozitif sayısal sapma yazılacak: 1.4 m düşüşte tam 0.6 m geriye kavisli sapma | ✅ KAPATILDI |
| 2 | S2 (K05) | D200 · YERÇEKİMİ §İki yerçekimi | Model bot adımında sıradan Dünya yürüyüşü üretir | Yapay merkezkaç yükü (1.0g) ve manyetik taban ayrılma direnci adım adım tarif edilecek | ✅ KAPATILDI |
| 3 | S3 (K09-K11) | D206 · D207 · THE LAST SHIFT | Coriolis yan kuvveti hissedilmezse tırmanış yapay kalır | Gövdenin 15 derece ters yatışı, omuz çarpması ve gerilen kas eforu pozitif yazılacak | ✅ KAPATILDI |
| 4 | S4 (K13) | D209 · D174 · THE QUIET FIELD | Merkeze yaklaştıkça dönen arka plan titrer, yön kaybolur | Eksenel kamera açısı ve sabit axial güneş ışığı açısı korunacak | ✅ KAPATILDI |
| 5 | S5 (K19-K20) | D213 · D175 · RED DEFTERİ | Kordon kesimi ve botların ayrılışı uzuv hasarı gibi algılanabilir | Mekanik kesici aparat ve botların rayda kilitli kalışı kan/yara olmadan teknik yazılacak | ✅ KAPATILDI |
| 6 | S6 (K21) | D208 · D146 · SKYLIGHT | Sıfır-g merkez kovanında kask vizörü ve tulum rengi değişebilir | Referans Paketi R1 panelleri birebir eşlenecek, vizör yarı-ayna altın kalacak | ✅ KAPATILDI |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S1 (K03) | D211 · QA_CRITIQUE Hook | İlk 10 saniyede retention düşüşü | K01'de ilk 2 saniyede pimin yana fırlaması ve K03'te alarm yansıması kilitlendi | ⚠️ QA İZLENECEK |
| 2 | S3 (K10) | D213 · QA_CRITIQUE Aksiyon | Çanta kopuşunda temas ve sonuç aynı karede kaybolabilir | Çantanın tırabzandan kopup boşluğa savrulması net kavisli yörüngeyle yazılacak | ⚠️ QA İZLENECEK |
| 3 | S5 (K17) | D215 · QA_CRITIQUE Halat | Emniyet kordonu boşlukta elastik yılan gibi bükülebilir | Örgülü çelik halat sert gergin hat olarak tanımlanacak | ⚠️ QA İZLENECEK |
| 4 | S6 (K22) | D210 · QA_CRITIQUE Kafiye | Dönen jantın geniş açıda perspektifi bozulabilir | 60 m çapındaki halkanın kavisli silueti ve 8 RPM dönme ritmi korunacak | ⚠️ QA İZLENECEK |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D208 · Referans Paketi | Karakterin kask/giysi tutarsızlığı | Tüm promptlarda "nameless technician in heavy EVA pressure suit, gold-reflective visor, charcoal grey composite fabric" birebir taşınacak |
| D209 · Dünya Çapası | Dönen istasyonda ışık yönü sapması | Güneş ışığı dönme eksenine tam paralel (axial skimming light) kilitlendi; istasyon dönse de ana ışık yönü değişmez |
| D214 · Self-Contained | Promptların Bible'a atıfla eksik kalması | Hiçbir prompt "bkz. Bible" demeyecek; tüm kıyafet ve çevre parametreleri her promptta kendi içinde tam yer alacak |
| D215 · Araç / Ekran Metni | Modelin vizöre veya ekrana uydurma yazılar basması | Her promptun negatif bloğunda "no text, no hud, no numbers, no subtitles, no digital overlay, no watermark" bulunacak |
| D217 · Diyalog / Replik | Boş replik veya yapay dudak hareketi | Film %100 diyalogsuzdur; ağız hareketi tamamen kapalıdır ("no dialogue, mouth closed behind visor") |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | Teknisyen EVA giysisi ve döner jant mimarisi var | R1 (EVA giysisi) ve R2 (jant & kafes merdiven) REFERANS PAKETİ hazırlandı; promptlar sayfaya işaret eder. |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | Vakumda kumaş dalgalanması riski | "fabric" ve "cloth" kelimeleri yasaklandı; yerine "rigid multi-layer composite insulation, stiff articulated plates" yazıldı. |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | 60 m jant ile dar tırabzan ölçeği | Geniş sahnelerde 20–35mm lenslerle jant kavisi kadraja alındı; detaylarda 65–100mm lenslerle mesafe korundu. |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | Çelik pim ve merkez kovanı mesafesi | K01'de pim ön planda 200+ pikseldir; merkez kovanı K08 ve K21'de kadrajın %25'ini kaplar. |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | Koyu uzay ve metalik gövde | Grafit gri tulum üzerinde parlak turuncu/sarı ikaz reflektörleri ve mat siyah kafes tırabzanı ile lüminans kontrastı kuruldu. |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | İstasyon jantının oyuncak maket görünmesi riski | UZAY_USSU §6 ve §3.7 negatif blokları ("no tilt-shift, no miniature toy look, no atmospheric haze, no CGI plastic shine") eklendi. |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ENTROPİ teması sahnelere dağıtılmalı | Tema nesne ve kinesik motifleriyle S1 (K01 pim sapması), S3 (K10 çanta kopuşu), S5 (K19-K20 kordon kesimi ve bot terki) sahnelerine doğrudan endekslendi. |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | Karakterin fedakarlığı belirsiz kalabilir | Bedel açıkça S5 (K20) sahnesine endekslendi: Manyetik botlar ve emniyet kordonu feda edilir. |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | Ters psikoloji modeli istenmeyeni üretmeye iter | Yasak emirleri yerine ellerin tırabzana kenetlenişi ve botların raya kilitlenişi pozitif eylem cümleleriyle yazıldı. |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | Kesici alet silah sanılabilir | "Bıçak/silah" yerine "ergonomic mechanical cord-cutter tool with enclosed safety blade" teknik geometrisiyle tarif edildi. |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | Replik zamanlama kayması | Film %100 repliksiz ve diyalogsuzdur; replik tablosu boştur, çelişki riski sıfırdır. |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | Model klip içinde durum değiştirmekte başarısızdır | Kordonun kesilişi ve pimin sapması klip içi karmaşık süreç yerine tek bir net kesme anı veya sınır satırına yazıldı. |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | Model harici dosyaları göremez | Her prompt teknisyenin giysisini, istasyon jantını ve aydınlatma parametrelerini kendi metninde eksiksiz taşır. |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | Eksik araç nedeniyle testlerin atlanması | Yalnız depoda doğrulanmış prompt_kontrol.py ve rapor_kontrol.py standart betikleri kullanıldı. |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | Model boyun veya bilekten et üretebilir | "no bare skin, no exposed neck, no exposed wrists, completely sealed helmet rubber gasket" negatif bloğa eklendi. |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | Coriolis yana savrulmasının modelce unutulması | Pozitif sayı kilitlendi: 15 cm uzunluğunda çelik pim, 1.4 m düşüşte tam 0.6 m geriye sapar; tırmanışta gövde 15 derece ters yatar. |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅ KAPATILDI)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16 satır tam)
→ üçü de ✅ ise 05_SAHNE_CALISMALARI/ açılabilir
```
