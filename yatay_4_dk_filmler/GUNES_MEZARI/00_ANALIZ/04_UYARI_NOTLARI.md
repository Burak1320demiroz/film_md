# ⚠️ GUNES_MEZARI — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır:
> **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.** Üçünden biri
> yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | klip | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | K01 · K02 · K04 · K11 · K21 · K24 | red defteri #2 (COLD BURN S8 V2) — insansız sahne + uzun `NEGATIVE:` + `Exactly 0 human figures` = **YAPISAL RED**; V3'te NEGATIVE tek pozitif satıra indi ve GEÇTİ | üretim hiç başlamadan reddedilir; gün yakar | altı insansız klipte NEGATIVE bloğu KISALTILIR (metin yasağı + fotogerçekçilik/grain + tek sahneye özel), insan sayısı cümlesi YAZILMAZ; boşluk POZİTİF envanterle tarif edilir ("the flight deck above it is dark and unmanned" · "the hall around the plate is empty, the benches tipped over") | ✅ yazıldı · QA_SPEC yanlış-pozitif duvarına da geçti |
| 2 | K17 · K18 · K19 · K20 | D89 (THE SECOND SHIP S69) — çıkarma sahnesinde model yasaklanan parçayı bırakıp KASKI çıkardı + red defteri #3: bedenden bir şey çıkarma = PB reddi | mühürlü giysi delinir; hem devamlılık hem politika kaybı | ⭐ dört klipte TEK MÜHÜR SAYIMI cümlesi: çıkarılan şey ADIYLA sayılır ve geri kalan bütün mühürler tek tek kapalı ilan edilir. Ayrıca anahtar GEMİDE, gövdede değil | ✅ kapandı |
| 3 | K01 · K02 · K03 · K21 · K22 | D59 (HOLDING FIELD) — 28/28 promptta yazılan yasak, aynı promptun POZİTİF isminde yenildi (`hang` → anti-gravite) | filmin öncülü tersine döner: küre "anti-gravite bir top" okunur | yedi kök (`hang/suspend/float/hover/still/frozen/stopped`) YALNIZ negatif blokta; küre pozitif gövdede **tutulur ve sıkıştırılır** ("three machined rings close around it and it turns with the ship as one body"); üretimden önce grep koşulur | ✅ kapandı · grep adım 10'da |
| 4 | K21 | D192 (OPEN CIRCUIT) — 1 numaralı risk yalnız sıfatla korundu, doruğun boşalması ŞİMŞEK geldi | filmin en pahalı karesi ateş topu olur | küre pozitif biçimi SAYIYLA (kenar keskin · çap halkaların iç açıklığının 4/5'i · hücre 4 s'de bir genişlik · korona 0 kare); SPEC göz kapısı aynı sayıları tekrarlar; İPTAL KAPISI yazılı | ✅ kapandı |
| 5 | K24 ↔ K01 | D210 + KEPT_LIGHT ④d — kapanış açılışın kamera cümlesini taşımadı (S0 tepeden CU ↔ S24 alttan alt açı); T9 KADRAJ'da HARD_DOCK bu kategoriye 2/10 aldı | kafiye ölür, döngü kanıtı düşer | K24'ün CAMERA satırı K01'in CAMERA satırının BİREBİR kopyası + dönüş işareti; iskelet ilk/son harf C | ✅ kapandı |
| 6 | K11 | D138 + THE_SOLAR_MIRROR (`S04` gövdeye basıldı) + KART 5 iki yönlü risk | arşiv levhasına model YAZI basar; ya da metin yasağı yüzünden levha hiç gösterilmez [D50] | levha METİN taşımaz, GÖRÜNTÜ taşır (eldiven + kol + kol kolu); promptta hiçbir büyük harfli kısa dizge yok; metin yasağı KAPSAMLI yazılır (giysi + ekipman + zemin + doğal yüzey + levha) | ✅ kapandı |
| 7 | K17 · K18 | red defteri #4 (COLD BURN S26) — `wounded ship` + `dull orange glow` = PK+PB reddi | geminin sönmesi "tehlike çerçevesi" okunur ve reddedilir | `wounded` · `dying` · `dead` · `glow` 0 kez; gemi "goes dark in the stated order"; küre ışığı "a deep red-gold light on the underside ribs" | ✅ kapandı |
| 8 | K08 | D91 (THE SECOND SHIP) — iz doğru tarafta ama YANLIŞ ORGANDA çıktı (sol kaş → sol çene) | filmin KANITI (hilal yanık) yanlış yere gider ve K11'in bağı kopar | ÖZELLİK + ÖLÇÜ + KAPATMA üçlüsü: "a crescent scorch the width of two fingers across the KNUCKLES of the back of her left glove — on the leather itself, not on the cuff, not on the palm, not on the fingers; the rest of the suit carries no burn and no mark" | ✅ kapandı |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | klip | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | insanlı 20 klip | D146 · ⛔ ÇALIŞMIYOR damgalı ders; 4 vaka, biri REFERANS PAKETİ olan filmde | vizör kubbeye kayar | paket yazıldı + `seamless/bubble/dome/sphere` 0 kez + kalın çerçeve/yaka halkası/tek spekülar çizgi üçlüsü [D95]. ⬜ **ÖLÇÜM RANDEVUSU:** ikinci üretilen klipte kubbe görülürse üretim DURUR | ⬜ üretimde |
| 2 | 6 efor klibi (K13·K16·K17·K19·K20 + K18) | D206 · T8 tablosu: COUNTED_TURN **0,0** · RESONANT_STRAND 1,0 · SOLAR_MIRROR 2,9 — deponun en düşük ekseni | "NOBODY PAYS" | her birinde saniyeli ödeme satırı + DESTEK/GÖVDE/2 işaret/DURAKSAMA; ⑳ sözlüğü tanıyor | ✅ yazıldı · ⑧ ölçer |
| 3 | K22 · K23 · K24 | LOW_POWER Parçacık **2/10** (projenin en düşük skoru) + mavi gün batımında bloom | ilk sabah bloom'a döner, kırağı deseni her karede yeniden üretilir | `0% bloom` + "the air carries no haze and no halo" + kırağı GLOBAL bitiş (konumlu leke değil) + dolgu KAYNAKLI (yalnız güneş ve kar) | ✅ yazıldı · ⑪ ölçer |
| 4 | film boyu | T11 IŞIK: COUNTED_TURN `KEY WALKS` (ana ışık 3→9 saat sıçradı) | ⚠️ **YANLIŞ-POZİTİF RİSKİ:** bu filmde ana ışık ELDE TAŞINAN FENERDİR ve kadının hareketiyle birlikte döner; mercek bunu "key walks" yazacak | ışık yönü SAATLE değil KAYNAKLA kilitlenir ("her own lamp, at her own chest height"); QA_SPEC YANLIŞ-POZİTİF DUVARI'na tasarım kararı olarak yazılır | ✅ duvara yazıldı |
| 5 | S2 (6 klip) | T12 HOOK: HARD_DOCK `LEAVES AT 00:25` (kokpit-dış platosu) · COUNTED_TURN ızgara platosu | 60 saniyelik şehir sahnesi plato olur, izleyici 0:40-1:20 bandında gider | MIKRO §2: altı klipte YALNIZ BİR yol klibi (K05); K06 omuzla kapı · K07 diz çöküp oyuk · K08 avuç · K09 diz çökmüş duvar — dördünde alt gövde zemine kilitli | ✅ yazıldı · ⑫ ölçer |
| 6 | K19 · K20 | PROMPT_HATA §3b: temas cümlesi VARKEN bulgu oranı YÜKSEK (RR 2,10); COUNTED_TURN 22/25'te yazılı → 7 🔴 | eldiven metalle erir | temas ilk 2 saniyede KURULU (%5,9 bandı) + görünür ARA KATMAN (çelik halka / çubuğun kılıfı) + iki yönlü temas cümlesi; temasa bakan ECU yok | ✅ yazıldı |
| 7 | K15 → K16 → K17 | D57 (DEEP PRESSURE) — tek çekimin İÇİNDE ekipman morfu (7. saniyede tüp belirdi) | gemi içi sahnede kask/eldiven durumu oynar | EKİPMAN DURUM TABLOSU: kask 24/24 KAPALI; gemi içi de mühürlü ve soğuk (kırağı çözülmez) — bu, S5'in PHYSICS satırında yazılı | ✅ yazıldı |
| 8 | K12 · K17 | §2.4 ⭐VİRAL kapısı — ölçülmedi, dış korpus | iki aday kapıyı geçti ama gerçek paylaşılma verisi YOK (yayınlanmış film 0) | ⭐VİRAL etiketi ölçütle yazıldı (yüz px + hareket kanalı); "viral olacak" İDDİASI yazılmadı | ✅ ölçüm olarak yazıldı |
| 9 | K24 | KART 2 (CANLI) — filiz insan dışı canlı | model filizi büyütür, hareket ettirir, çoğaltır | filiz SAYILI ve BOYUTLU (bir parmak boyu · üç yaprak · 1 adet); hareket etmez, yalnız ışık gelir; anatomi kilidi tek cümle | ✅ yazıldı |
| 10 | film boyu | D147 · THE_FROST_LINE: faz metni 50/50 promptta yazılıydı ve kırağı hem erken geldi hem dalgalandı | kırağı pası sıfırlanır | merdiven 3 kademe, monotonik, GLOBAL bitiş; SPEC C'de; ⬜ **ÖLÇÜM RANDEVUSU:** ② DEVAMLILIK'in WEAR TIMELINE satırı | ⬜ üretimde |
| 11 | K21 | D127 — 12/12 promptta yazılan ivme ekrana gelmedi | kürenin yükselişi sabit hızda süzülme olur | ivme YAZILMAZ, KADRAJI TERK SÜRESİ yazılır ("by the sixth second its lower edge has crossed the top frame line, by the eighth it is gone") + kendi genişliğini ~2 s'de geçer | ✅ yazıldı |
| 12 | film boyu | ADAY-98 · THE_SLOW_RAIN S14 + THE_STOLEN_SKY: CAMERA satırındaki `tripod` kelimesi kadraja TRIPOD soktu | plansız tripod | 48/48 CAMERA satırında `locked-off camera`, `tripod` kelimesi 0 kez | ✅ yazıldı |

## 3. 🧯 FİLM GENELİ — tek klibe bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D209 · 3 film | gök/ufuk/yer imi her klipte başka dünya üretir | DÜNYA ÇAPASI üç cümle, dış-mekân klibinin hepsinde BİREBİR |
| D193 + KART 6b | katmanlı dünyada ışık yanlış katmanın ışığıyla çıkar | IŞIK TAKVİMİ 7 satır, SPEC C'de; artış S7'de ve OLAY olarak ilan edilmiş |
| D167 + red #15 | kimlik yığını "belirli bir gerçek kişi" kalıbı olarak okunur ve üretim durur | promptta kimlik özniteliği ≤3; kesin boy YOK; ten/saç/yaş YOK; yüz yalnız 4 klipte |
| D155 + §6 jeton sızıntısı | prompt gövdesindeki büyük harfli kısa dizge giysiye BASILIR | `S04` · `K14` · `PHASE 2` · kısaltma 0 kez; klip numarası yalnız `Clip 14 of 24.` cümlesinde |
| D34 · D70 · D72 (12 tekrar) | kuyruk kartı / kapak çıktısı kurguya girer ve döngüyü öldürür | KAPAK ayrı dosya, kurgu klasörüne girmez; K24'e "the take ends on the held frame" cümlesi; SPEC E'de freezedetect kapısı |
| D83 · D216 | ortam yatağı klip sınırında ölür, kesmede dijital sıfır | MUZIK dosyası: tek oda tonu 240 s kesintisiz · katman ≤4 · köprü ≥0,2 s |
| D180 | planlı sessizlik video modelinden istenirse gelmez | K12 sonunun sessizliği KURGUDA HARD MUTE (119,0–120,0 s); üç eşikte ölçülür |
| §4 PROMPT_HATA (promptun kapatamadığı üç sınıf) | ① ince atmosferde ses ② temas füzyonu ③ filigran — üçü de yazımla kapanmıyor | ① kurguda low-pass < 300-400 Hz + noise gate ② kadraj kararı (ilk 2 s + ara katman) ③ KAPI 0'da araç ayarı, üretim defterinin üç kutusu |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | **VAR** — insanlı 18 klipte kask, 5 klipte küre iki hâlde | REFERANS PAKETİ (KAPI 0) + `seamless/bubble/dome` 0 kez + D95 üçlüsü; ⬜ ikinci klipte biçim kontrolü, sapmada üretim DURUR |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT | **VAR** — uzun pelerin insanlı 18 klipte | pelerin yalnız KENDİ hareketiyle savrulur; rüzgâr kumaşı kıpırdatmaz (§3.9 kartı); "loose folds" kalıbı YAZILMAZ (D153'te ayrı bir branda nesnesi doğurdu) — "a long worn cloak, one continuous surface" |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | **YAPILDI** — 7 kurulumun 7'si `03_SAHNE_SIRALAMASI` §3b'de hesaplı | her kurulumda kadraj eni/boyu + kritik nesnenin piksel karşılığı yazılı; gemi (40 m) I kadrajını (37,5 m) bilinçli aşıyor |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | **KONTROL EDİLDİ** — en küçük kritik nesne filiz 136 px · hilal iz 163 px | 100 px altı kritik nesne YOK; K18'in uzak penceresi 267 px (derin odak) |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | **VAR VE TERSİ** — mat grafit zırh, siyah bazalt şehir: figür zeminde erir | ⭐ ayrım RENKLE değil KIRAĞIYLA: omuz kapaklarında ve pelerin kenarında soluk kırağı pası figürü ayıran tek şeydir (fiziksel, monotonik, D147 uyumlu). Kontrast cümlesi ÖZNEYE yazılır, zemine renk atanmaz [D176] |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | **KAPANDI** — §3.9'un PHYSICS/AUDIO çifti bu filmde YAZILDI ve 24/24 prompta girer | çift `PROMPT_HATA_ONLEME` §2'ye de inecek (kart için hazır cümle bugün YOK) |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | **KAPANDI** — FEDAKÂRLIK 3 motif kanalıyla ve klip numaralarıyla | nesne kanalı K02·K19·K21 · kinesik kanal K08·K12·K19(+K20 kırılma) · ışık kanalı K03·K22·K23 |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | **KAPANDI** — BEDEL iki numara taşıyor: S5·K17 ve S6·K20 | ikinci kayıp S7·K23'te ve SÜRPRİZ olarak değil kesinleşme olarak yazılı |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | **RİSK VAR** — K21 patlama okuması davet ediyor | `explosion/fireball/flash/blast` NEGATİF BLOKTA BİLE yazılmaz; yerine pozitif biçim + sayı |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | **ÖNLENDİ** | küre "sun" olarak değil BİÇİM olarak yazılır: "a smooth sphere of dark red-gold light, its edge sharp"; gemi "cathedral" değil "a long ribbed hull" |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | **KAPANDI** — iki replik saati formülle: 26,0 s ve 92,0 s | SPEC A'ya aynı formülle yazılır; ③ SES register haritasıyla karşılaştırılır |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | **VAR VE BİLİNÇLİ** — K17 (ışıklar söner) · K19 (kilitlenir) · K20 (kilit yutar) · K21 (halkalar açılır) | dördü de üç satırlı (TEMAS·DEĞİŞİM·SONUÇ), sonuç ≥1 s kadrajda; geri kalan 20 klipte klip içi durum değişimi YOK, değişim SINIRA yazıldı |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | **YOK** | 48/48 promptta atıf cümlesi 0; self-contained = KADRAJDAKİ her şey, kadraj dışı hiçbir şey [D214] |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | **ÖNLENECEK** | SPEC E'nin her makine kapısı KURU KOŞUYLA doğrulanır (`ffmpeg -filters \| grep`) ve DOĞRULANDI satırı sürümle yazılır |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | **ÖNLENDİ** | üç bölge TEK satırda: "no bare skin anywhere — none above the collar, none at the wrists between glove and sleeve, none at the ankles between boot and leg" |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | **KAPANDI** — küre pozitif biçimi dört sayıyla | çap oranı 4/5 · hücre 4 s · korona 0 kare · aradaki hava pussuz; SPEC göz kapısı aynı dört sayıyı sorar |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
□ 🔴 ⛔ satırlarının hepsi kapatıldı (8/8 ✅)
□ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
  (12 satır · 2'si ⬜ üretimde ölçülür: vizör biçimi · kırağı merdiveni)
□ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16)
→ üçü de ✅ → 05_SAHNE_CALISMALARI/ açılabilir
```
