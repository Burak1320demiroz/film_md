# ⚠️ BLIND_ORBIT — UYARI NOTLARI

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
| 1 | S4 · K15 | D192 · COLD BURN S17 "dönüşü eşle" hiç ekrana gelmedi · HARD DOCK ① 1:10 dönme açısı 45° sıçradı | imza planı ya üretilmez ya ters döner (istasyon döner, kara delik durur) | Tek kilit üçüncü satırda SAYIYLA (çeyrek tur / 10 s · 3 kanat · tek yön); START karesinde kanatlar Y biçiminde, halka merkezde; İPTAL KAPISI 03 §7'de; üretimde İLK halka | ✅ |
| 2 | S5 · K20 · K21 | HARD DOCK ⑦ B4 kenetlenme darbesi kesmeyle gizlendi · D213 | doruk kadraj dışına ya da kesmeye düşer | K20: temas 3,0 s'de, merkez üçte birde, sonuç ≥1 s (halka bir parmak esner, tutar) · K21: dört kanca ARDIŞIK oturur (2,0 · 3,5 · 5,0 · 6,5 s), son kancadan sonra ≥2 s kadrajda; kilitler insansız makroda, kokpit tepkisine KESİLMEZ | ✅ |
| 3 | 22 insanlı klip | D146 · OPEN CIRCUIT 23/23 kubbe (paket VARKEN) · YERÇEKİMİ F2 geometri 0/6 | vizör kubbeye döner, iki kask birbirine benzer | vizör cümlesi biçim + sayı: "a single flat front pane set inside a thick dark rim"; RK1/RK2 sayfaları KAPI 0; ilk iki yüz klibinde (K18 · K23) gözle sınav | ✅ |
| 4 | K04 · K08 (iki insan) | D20 klon · D208 · COUNTED_TURN yüz cinsiyet değişti | iki figür aynı kimliğe akar ya da üçüncü belirir | iki kimlik dört eksende ZIT (altın SAĞ ↔ kobalt SOL · kanat ↔ altıgen rozet · inci kompozit ↔ teknik kumaş + kobalt eklem · SOL koltuk ↔ SAĞ koltuk); "Exactly 2 human characters" yalnız bu iki klipte; konum kilidi + faz farkı + "never touch" | ✅ |
| 5 | 13 replikli klip | KART 7 · SES §1a · D35 · D82 · Cold Burn sayılar ekrandaki ağızlara geçti | lip-sync çöküşü + AI damgası; sayı insan ağzında | konuşan ağız 0 klip (arkadan / sırttan / kadraj dışı); dinleyen yüzde "lips closed"; sayı yalnız MAKİNE sesinde (R4 · R16); her AUDIO satırı "heard only — never shown as text" | ✅ |
| 6 | 9 insansız dış klip (ölçüm 05.10: K01 K03 K05 K07 K13 K15 K20 K21 K24) | red defteri #2 (YR) · KART 10 | yapısal red | insansız klipte NEGATIVE dört cümle (metin · grain · bloom · halo), "0 human" kalıbı YOK | ✅ |
| 7 | K03 · K07 | red defteri #4 · #9 · POLİTİKA §2.2 | tehlike çerçevesi kelime reddi | damaged · emergency · danger · collision · crash · impact · dead · explosion · fire · burning · glow 0; nötr tarif 02 §6 | ✅ |
| 8 | K11 · K16 · K22 (ekranlı) | D138 · MARS_SON_CIKIS "HARD LOCK" yazısı · SIGNAL KEEPERS vizörde HUD | ekrana yazı/rakam basılır ya da vizöre yansır | ekranlar SOYUT ("a dark rectangular display" · "a single amber line"); tırnaklı gösterge yazısı 0; yüz kadrajında (H) ekran kadrajın kenarında ve vizöre yansımaz ("no reflection in the pane") | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | K01 · K03 · K07 · K13 · K24 (A) | D179 piksel · UZAY_USSU §5.2 | 250 m'den kenet halkası ~19 px — temas okunmaz | A'da temas HALKA değil GÖVDE düzeyinde okunur ("the small ship's nose meets the centre of the station's front face"); gemi ~194 px ✓; halka ayrıntısı I/J'ye bırakıldı | ⬜ üretimde ölç |
| 2 | K05 (D) | D179 | 600 m'den kenet ağzındaki lamba ~8 px | "cevap yok" SESLE taşınır (istek tonu, cevap 0); lamba promptta yalnız yön işareti | ⬜ |
| 3 | K11 | HOOK §3.1 ironi · SIGNAL KEEPERS HUD | ironi ekranı Lena'nın vizörüne yansırsa okunmaz/HUD olur | C kurulumu ARKADAN: ekran konsolda, kask ondan uzağa (pencereye) bakar; titreme ORAN (bir kez kararır, geri gelir) — klip sonu ekran yanık | ⬜ |
| 4 | K14 · K15 · K18 | KART 9 ışık mıknatısı · D104 | gemi/beden baskın ışığa (kara delik halkası) döner | ışık ve hedef AYNI yönde (kara delik istasyonun arkasında) → mıknatıs doğru cevabı üretir; pencere görüntüsü istasyonun ön yüzü | ⬜ |
| 5 | 24/24 | D124 klip süresi | 10,0 s ızgara araçta 8 s + extend olabilir (§2.3 kart satırı) | ilk üretilen klipte ffprobe; sapma varsa SPEC E ve replik saniyeleri yeniden hesaplanır | ⬜ K1 |
| 6 | K18 · K23 (⭐VİRAL) | SENARYO §2.4 · ölçüm: 0/2/3/3 | yüz + hareket aynı klipte birleşmeyebilir | iki kanal yazılı (yüz okunur ≥135 px + pencerede dönen halka / motor ışığı); üretimde ölçülür | ⬜ |
| 7 | K10 | D206 · D169 · ⑧ T8 tablosu (STATIC VEIL 1,4) | efor ağırlıksız | DESTEK (iki bot çerçeveye kilitli) + GÖVDE (omuz çarka yüklenir) + İŞARET (kollar gerilir, omuz düşer) + DURAKSAMA (çark takılır 3,0 s, ikinci yüklenme) | ⬜ |
| 8 | K09 · K17 | D200 · MARS_SON_CIKIS yörüngede yürüyüş | 0 g'de yürüme / ayakta durma | "pulls himself along the passage hand over hand on the rails, his legs trailing" — yürüme fiili 0; bot zemine basmaz | ⬜ |
| 9 | K03 · K10 | KART 6 · D36 | vakumda jet kıvrılır, duman gibi asılı kalır | "a short straight cone of gas that thins and is gone within a hull-length"; K10'da jet GÖRÜNMEZ (iç klip), K11'de ZATEN yok | ⬜ |
| 10 | dış klipler | HARD DOCK ⑤ gezegen topoğrafyası kaydı · D209 | kara delik her klipte başka biçim/yön | DÜNYA ÇAPASI üç cümle birebir; RD referans sayfası; kara delik yönü "upper left behind the station" A·D'de · "filling the background around the station's face" G'de | ⬜ |
| 11 | dış istasyon klipleri | HARD DOCK ① faz sıçraması | kesmede kanat açısı sıçrar | SPEC'te TASARIM olarak ilan: dönüş 9°/s, kesmeler arası faz serbest; iki dış istasyon klibi ardışık değil (iskelet) | ⬜ |
| 12 | K22-K23 | D193 · HARD DOCK ⑪ S8→S9 yüz ısısı | kabin ışığı klipler arası zıplar | iç LIGHT satırı sahne içinde birebir; K22 tek OLAY (zayıf ışık sabitlenir); K23 motor ışığı pencereden — yeni sahne, yeni satır | ⬜ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D34 · D45 · PROMPT_HATA §6 | ad / jeton ekrana basılır | Lena · Noah · LARK · VESPER promptta 0; BÜYÜK HARF jeton 0; "Clip n of 24." dışında künye 0 |
| D175 · ㉑ | çıplak deri | negatif cümlesi üç bölge tek satır: "No bare skin anywhere — none above the collar, none at the wrists between glove and sleeve, none at the ankles between boot and leg." |
| §3.1 lens · YANAŞMA §1.2 | anamorfik parlama | "spherical lens" yalnız dış kliplerde; "anamorphic" 0 |
| D200 · PROMPT_HATA §3.10b | iki yerçekimi | PHYSICS satırı 48/48 birebir (iç + dış tek cümle) |
| D216 · SES §5 | ses yatağı kesilir | MUZIK katman tablosu ≤4 · köprü ≥0,2 s · replik altında −6 dB · telsiz band-pass |
| D215 | filigran / altyazı / ağız | ÜRETİM DEFTERİ üç kutu KAPI 0'da |
| D168 · KAPI 0 | sayfası onaysız varlık | 8 referans sayfası onaylanmadan klip üretilmez |
| MIKRO_AKSIYON §4.2 · ADAY-98 | plansız tripod | CAMERA satırında "tripod" 0 |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | **VAR ve ÜÇ KATLI** — iki vizör + istasyonun üç kanatlı silueti + iki aşamalı kenet | referans paketi 8 sayfa KAPI 0 (RK1 · RK2 · RA · RB · RI1 · RI2 · RO · RD); sayılabilir öğe metinde (3 kanat · 4 kanca · 1 halka) |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | **KISMEN** — giysi teknik kumaşı ve kayışlar var; dışta örtü yok | giysi "technical textile" + "matte scuffed composite plate"; yalnız "fabric" yazılmaz; bağ kayışı "a short webbing strap pulled taut" (gergin, dalgasız) |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | **YAPILDI · üç kurulum düzeltildi** | kadraj eni = mesafe × 36 / odak: A 35mm·250 m → 257 m (gemi 194 px) · G 35mm·120 m → 123 m (gövde yüzü %58 yükseklik) · J 85mm→50mm·8 m → 5,8 m (dört kanca kadrajda, kanca ~100 px) · H 50mm→35mm·1,3 m → 1,34 m (kask + kabzadaki eldiven) · B 35mm·1,0 m → 1,03 m · C 35mm·1,8 m → 1,85 m (eldiven ~125 px) — 05 tablosunda OPTİK sütunu |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | **VAR · iki yerde** | A'da halka 19 px → temas gövde düzeyinde yazılır · D'de lamba 8 px → sesle taşınır (§2 #1-2) |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | **YOK — ayrım renk + KONUM + BİÇİM** | iki figür yalnız K04/K08'de aynı kadrajda ve orada kabin ışıklı; kalan kliplerde KONUM ayırır (Lena hep kokpitte · Noah K09'dan sonra servis/optik bölmede); rozet BİÇİMİ (kanat ↔ altıgen) |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | **VAR** — 900 m istasyon | dış kliplerde sahneye özel negatif: "no tilt-shift look, no miniature read, the far end of the structure as sharp as the near end" + "no logo, no emblem, no marking on the hull" (≤3 cümle sınırı içinde) |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | **YOK — klip numaralı** | GÜVEN · tanım "Göremediğin son metrede başkasının gözü senin gözün olur." · motif K04 · K08 · K12 · K18 · K19 · K24 (02 §4) |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | **YOK — numaralı** | S2·K07 (pay) · S3·K10 (itici grubu) · S4·K18 (kontrol); onay dosyasıyla aynı |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | **VAR · iki yerde** — "çarpışma" ve "kask açma" | ikisi de ADLANDIRILMAZ: K07 "stops a hull-length short" (pozitif mesafe) · kask durumu "the helmet sealed to the collar ring" (pozitif) |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | **VAR** — itici, vana, kenet | hepsi FORMLA: "a cluster of small nozzles on the left side of the hull" · "a heavy steel hand-wheel the width of a helmet" · "a soft outer ring and four hook-shaped latches" |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | **YOK — formülle** | `replik(K_n) = (n−1) × 10 + ofset` · örn. R10 = (16−1)×10 + 4,0 = 154,0 s = 2:34 · R17 = (24−1)×10 + 3,0 = 233,0 s = 3:53 (03 §5 tablosu) |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | **VAR · 5 yerde, hepsi SINIRA taşındı** | ekran kararması K15/K16 sınırı · jetin sönmesi K10/K11 sınırı (K10'da yalnız tıslama sesi çekilir) · rezerv çizgisi K07/K08 sınırı · motor ateşlemesi K22/K23 sınırı (K22'de yalnız titreşim başlar) · kabin ışığı K22 içinde ORAN (zayıf → sabit; ⚠️ tek klip içi, OLAY olarak kabul) |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | **YOK** | 48 prompt kendi kendine yeter; yalnız IN FRAME'deki tarif edilir [D214] |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | **AÇIK** — QA_SPEC adım 9 | her makine kapısı kuru koşuyla doğrulanır (`ffmpeg -filters` grep) · DOĞRULANDI satırı |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | **VAR** — 15 insanlı klip | üç bölge TEK satırda (§3) |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | **KAPATILDI** | K15: çeyrek tur / 10 s · 3 kanat · tek yön · göz kapısı (kanat Δ ≤10° · halka 70-110°) |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

### 4b. 🆕 BU FİLMİN AÇTIĞI ADAY SATIR (şablona önerilir, adım 11)

```
ADAY-C · "GÖVDEYE BAĞLI KAMERADA DÖNEN ŞEY ARKA PLAN — LOCKOFF TANIMI"
  Durum: K15 kamerası küçük gemiye bağlı; gemi dönüyor, kamera gövdeye göre SIFIR
  hareket. Klip içi lockoff kuralı (KART 8) "kamera hiç hareket etmez" diyor;
  dünya referansında kamera dönüyor. UZAY_USSU §7 bunu "dönen yapıda tek ucuz kanıt
  arka plandır" diye zaten kabul ediyor ama KART 8'in CAMERA kalıbıyla ("absolutely
  zero camera movement") çelişki gibi okunabilir.
  Karar: CAMERA satırı "locked to the hull — zero movement relative to the ship"
  yazar; arka planın dönüşü kilit satırındadır. Model "camera rotates" okursa
  ⑨ KADRAJ LOCKOFF bulgusu TASARIMDIR — SPEC yanlış-pozitif duvarına satır.
  Ölçüm: ilk üretilen K15. Tek vaka — ADAY bile değil, gözlem; ikinci dönen-kamera
  filminde tekrar ederse GOZLEM_DEFTERI'ne.
```

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (8/8 ✅)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (12 satır · ⬜ üretimde)
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16 · biri AÇIK: #14 makine kapısı,
  adım 9'da kapanacak)
→ 05_SAHNE_CALISMALARI/ açılabilir
```
