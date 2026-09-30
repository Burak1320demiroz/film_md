# ⚠️ THE_BRITTLE_EDGE — UYARI NOTLARI

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
| 1 | S00 | D192 · OPEN CIRCUIT A5 | Metal kopmasının cam tozu veya kıvılcıma dönüşmesi | Sayısal kilit: 2 parçaya ayrılan çelik halka, 1 çatlak çizgisi, 0 kıvılcım, 0 cam tozu | ✅ |
| 2 | S08-S09 | D179 · D206 | S08 sonu ile S09 başı devamlılık kopması (araç havada kaybolması/konum sıçraması) | S09 video promptu S08'in son karesinden I2V zinciri olarak başlar; kamera konumu ve araç askı açısı kilitlenir | ✅ |
| 3 | S00-S11 | D16 · D146 | Kask içinde yüz morphing / kaskın cam fanusa dönmesi | Kask tasarımı: altıgen vizör çerçeveli, opak siyah yansıtıcı vizör, kask içi ışıksız | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S01 | D198 · THE_LAST_SHIFT | Düşük yerçekiminde regolit parçacıklarının Dünya gibi hızla çökmesi | 0,16g Ay yerçekimi; toz sürtünmesiz balistik yay çizer, süzülme ve sis yok | ⚠️ QA_SPEC |
| 2 | S05 | D169 · OYUNCULUK §8 | Karakter zorlanmasının sadece tek sahnede kalması | Eldivenlerin sapanı çekerken kasılması ve dizlerin regolitte bıraktığı derin iz bedende gösterilir | ⚠️ QA_SPEC |
| 3 | S11 | D62 · KURGU_RITMI §2 | Kurguda final sahnesinin aceleye gelmesi/düşmesi | S11 tek yavaş geri-yukarı kamera hareketiyle bağımsız vuruş olarak kurgulanır | ⚠️ QA_SPEC |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D1 | AI modelinin klip içinde kesme veya jump-cut yapması | Her video promptu tek kesintisiz sekans olarak yazılır; montaj/jump cut kelimeleri yasaklanır |
| D138 | Araç ve kostüm üzerine yapay zekanın rastgele harf ve logo basması | Giysi ve sarı araç gövdesi pürüzsüz endüstriyel boya ve metinsiz yüzey olarak pozitif tanımlanır |
| D180 | Modelden mutlak sessizlik istenip rastgele dip gürültü üretilmesi | Modelden sessizlik istenmez; AUDIO satırında mekanik sürtünme ve kask içi solunum titreşimleri yazılır |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | Tek astronot kasklı, araç sarı keşif aracı | Altıgen vizör çerçeveli opak siyah kask; sarı rover için 3 sabit çapa kelimesi kullanıldı. |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | Kurtarma sapanı kumaş değil kompozit kayış | Ağır dokuma sentetik kompozit kayış olarak tanımlandı; "fluttering" ve "cloth" kelimeleri yasaklandı. |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | 12 sahnede odak uzaklıkları ve mesafeler | S00 (50mm CU - 1m), S01 (24mm WS - 15m), S02 (50mm ECU - 0.5m), S08/S09 (28mm MS - 5m) tam hesaplandı. |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | S00 ve S02 novum anları | Kırık çelik kulak ve çatlak yüzeyi ECU/CU planlarda kadrajın en az üçte birini kaplar. |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | Krater gölgesi içinde araç ve astronot | Koyu bazalt zemin ile parlak endüstriyel sarı şasi ve beyaz giysi arasında güçlü kontrast kuruldu. |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | Ay vakum ortamı | §3.1 VAKUM negatif bloğu (makro-lens, tilt-shift, atmosferik sis, duman) 12 prompta eksiksiz taşındı. |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | UYUM VE ÖĞRENME teması | Sahne indeksleri S03, S05, S08, S11 olarak haritalandı ve davranışa bağlandı. |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | Karakterin ve aracın kaybı | Bedel açıkça S08 olarak tanımlandı: son kaya çıkıntısı desteğinin ve emniyetli temasın kaybı. |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | Kopma ve askıda kalma aksiyonları | Yasak dili kullanılmadı; fiziksel form ve mekanik durumlar pozitif tanımlarla yazıldı. |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | Çekme donanımı | Silindirik çelik halka, örgülü çelik halat ve turuncu sentetik kayış formlarıyla tarif edildi. |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | Filmde replik durumu | Bu film tamamen diyalogsuzdur; replik zamanlama riski yoktur. |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | Kopma ve kurtarma aşamaları | Klip içi radikal dönüşüm yok; aşamalar sahne sınırlarına (S00 kırılma, S01 kayma, S05 sapan, S08 kopuş) bölündü. |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | Tüm promptlar | Her prompt bağımsızdır; Character/World Bible'a atıf yapmaz, görsel unsurları doğrudan içerir. |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | QA_SPEC makine kapıları | ffprobe ile temel çözünürlük, kare hızı ve süre doğrulaması kullanıldı. |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | Astronot giysisi | Astronot basınç giysisi tam mühürlüdür; "bare skin, exposed flesh" negatif çekirdeğe eklendi. |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | S00 metal kopması | Sayısal kilit verildi: 2 ayrık çelik parça, 1 düz çatlak hattı, 0 kıvılcım, 0 cam tozu, 2 sn 1,5m kayma. |

---

## ✅ KAPI

```
[x] 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
[x] 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
[x] tekrar eden arıza tablosunun HER satırı cevaplandı (16 satır tamam)
→ üçü de ✅, 05_SAHNE_CALISMALARI/ açılabilir.
```
