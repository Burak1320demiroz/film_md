# ⚠️ THE_STATIC_VEIL — UYARI NOTLARI

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
| 1 | S9 | PB S9 / Red Defteri | Batarya patlaması ve alev üretimi redde girer | Yangın, duman ve alev kesinlikle yok; ≤0.3 saniyelik beyaz-mavi elektriksel ark olarak nötr tarif edilecek | ✅ |
| 2 | S2 | KT S2 / Red Defteri | Kask camı kırılması / insan boğulması | Kask camı asla çatlamaz veya kırılmaz; çizilme ve matlaşma polikarbonatın dış yüzey aşınması olarak verilir | ✅ |
| 3 | S0 | D200 / FİZİK | Vakumda tozların yere yağması veya süzülmesi | Elektrostatik tozlar dikine 1-2 m yükselir, havada asılı kalır, yere inmez | ✅ |
| 4 | S1, S6, S11 | D139 / EKİPMAN | Modelin arkadan çekimde boş sırta sırt çantası uydurması | Pozitif yüzey kuralı: "the back of the suit is one continuous smooth panel from collar to hip, carrying nothing" | ✅ |
| 5 | S0–S11 | D214 / METİN | Kadraj dışı uzuvların prompta yazılması | IN FRAME satırında olmayan hiçbir beden parçası prompt gövdesinde anılmayacak | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S0 | D211 / T12 HOOK | İlk 2 saniyede görsel merak oluşmaması | Sessiz kraterde zemin üzerinden dik yükselen toz iplikleri ilk karede belirgin kılınacak | ✅ |
| 2 | S1–S10 | D42, D57 / T2 DEVAMLILIK | Vizör matlaşmasının sahneler arasında rastgele dalgalanması | S1 %10 → S2 %40 → S3-S8 %80 → S10'da tek temiz delik oranı SPEC'e bağlandı | ✅ |
| 3 | S8, S9 | D202, D206 / T4 HİKAYE | Bedelin bedende hissedilmemesi | S8'de tereddütlü el duraksaması; S9'da temas sonrası sönen kask ekranları ve omuz düşüşü | ✅ |
| 4 | S9, S10 | D213 / T7 AKSİYON | Aksiyon elipsiyle temasın kadraj dışına kaçması | Bataryanın şaseye vurulması ve kilit tırnağının yerine oturması kadraj merkezinde gösterilecek | ✅ |
| 5 | S11 | D210 / T11 IŞIK | Kapanış kafiyesinde fener ışığının yönünün şaşması | S0 zemin açısıyla tam aynı kadraj; tek fark pilon tepesindeki yanan amber fener | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D200 / §3.1 VAKUM | Atmosferik yanılsama | 0.16g Ay kütleçekimi: adımlar yavaş; gökyüzü zifiri siyah; atmosferik saçılma/hava yok |
| D215 / METİN | Araç filigranı ve AI damgası | No watermark, no text overlay araçtan kapatılacak, negatif çekirdek eksiksiz girilecek |
| D208 / DONANIM | Giysi parça değişimi | Beyaz sert gövde, gri esnek körük eklem, altın yansıtıcı küresel vizör, sol kolda basınç saati |
| D180 / SES | Modelden planlı sessizlik isteme hatası | Prompt gövdesinde No dialogue yazılacak; post-prodüksiyonda gövde iletimli ses miksi yapılacak |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | Uygulanıyor | THE_STATIC_VEIL_REFERANS_PAKETI hazırlanarak giysi, fener ve zemin kilitlendi |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | Muaf | Giysi sert kompozit ve körüklü karbon eklem olarak tanımlandı; kumaş kelimesi kullanılmadı |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | Uygulanıyor | 24mm (EWS), 50mm (MS/MCU), 85mm (CU/ECU) optik sınırlarına göre ölçeklendi |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | Uygulanıyor | Yakın çekimlerde fener tırnağı ve kask vizörü kadrajın en az %40'ını kaplar (≥100px) |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | Muaf | Tek karakter; beyaz giysi ile koyu zemin ve siyah gölge arasında yüksek kontrast var |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | Uygulanıyor | §3.1 Vakum negatif çekirdeği (no atmosphere, no ambient fill, zero feathering) tam eklendi |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | Uygulanıyor | Fedakârlık teması motif sahnelerine (S0, S2, S9, S11) bağlandı ve plana işlendi |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | Uygulanıyor | Bedel kesin olarak S9 sahnesine bağlandı (kask göstergelerinin feda edilmesi) |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | Uygulanıyor | Promptlarda asla "never" veya yasak fiil kullanılmadı; negatif çekirdeğe taşındı |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | Uygulanıyor | S9'da patlama/bomba denmedi; "small rectangular battery module", "electrical spark" dendi |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | Muaf | Filmde diyalog/replik yoktur |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | Uygulanıyor | Durum değişimleri (matlaşma, sönme) sahne sınırlarına yerleştirildi, klip içi tek eyleme odaklandı |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | Uygulanıyor | Hiçbir prompt Bible'a atıf yapmaz; kadrajda ne varsa IN FRAME altında tarif edilir |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | Uygulanıyor | SPEC kapısı kurulu standart ffmpeg filtreleriyle (crop, blackdetect, silencedetect) yazıldı |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | Uygulanıyor | no bare skin above the collar, no bare skin at the wrist, no bare skin at the ankle tam girildi |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | Uygulanıyor | Toz yükselme yüksekliği 1-2 m, tane boyutu 10-100 mikron, ark süresi ≤0.3 s sayıyla yazıldı |

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
✅ tekrar eden arıza tablosunun HER satırı cevaplandı (16 satır tam)
→ üçü de ✅ olduğu için 05_SAHNE_CALISMALARI/ açılabilir
```
