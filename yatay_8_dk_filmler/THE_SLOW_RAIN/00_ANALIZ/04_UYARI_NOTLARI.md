# ⚠️ THE_SLOW_RAIN — UYARI NOTLARI

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
| 1 | S0 · S7 · S17 · S24 · S32 (novum sahneleri) | D192 (OPEN CIRCUIT şimşek) · D157 (PAYLOAD bandı) · KART 6 | damla Dünya yağmuru gibi ÇİZGİ olur ya da asılı PERDE olur (çekirdek "never hovering" ile çelişir) → novum ölür | pozitif sayı her novum promptunda birebir: "no more than a few dozen separate drops in frame, each the size of a marble, each falling at a slow jogging pace, far slower than rain on Earth, crossing a wide frame top to bottom in about two seconds, none streaking, none hanging"; SPEC göz kapısı iki ardışık karede aynı damla yarım kadraj yol almış mı; S24 iptal kapısı | ✅ (03 §7 · SPEC E) |
| 2 | S38 · S14 · S22 · S26 (damla + düşen/kayan nesne aynı kadrajda) | D200 (5 film TWO GRAVITIES) · IRON SLOPE ⑥ | ⑥ merceği yavaş damla ile hızlı düşen çekirdeği "iki yerçekimi" okur; model ikisini eşitler (damla hızlanır ya da çekirdek süzülür) | PHYSICS satırı iki hızı adlandırır ("rain falls slowly at a slow jogging pace, far slower than rain on Earth; anything let go falls fast"); SPEC C düşüş tablosu iki satır (damla: sabit hız / nesne: eldiven boyu 0,3 s); S38 TIMELINE çekirdek kayışı saniyeli; mekanik sebep yazılır (§2b): "the drops are slowed by the dense air; the solid core is not" | ✅ |
| 3 | S15 · S29 (seçim · bedel) | D179 (HEALING GROUND imaj sonrayı yazdı, 40 m EWS) · D202 · COUNTED_TURN ⑩ 3,4 | seçim/bedel bedende okunmaz; imaj bitmiş hâli dondurur; EWS'de üç piksel | S15 O (MS · 2,2 m) · S29 Y (CU · 1,5 m); IMAGE = 0,0 s (kanatlar sırtta / kayış bağlı); ÇAPA ÜÇLÜSÜ BEFORE/AFTER omuz+el saniyeli; S29'da el tokaya gider, iki parmak durur 2 s, sonra keser; reddedilen nesne (kanat) kadrajda ve S30'da hâlâ orada | ✅ |
| 4 | S1 · S6-S8 · S12-S13 (kanat sırtta) · S15-S28 (kızak) · S29-S30 (batıyor) | D146 (kubbe 4 vaka) · D208 · KART 3 · referans paketi YOK | kanat takımı biçimi sahneden sahneye değişir; kızak hâli "yeni nesne" okunur; sırt ünitesi doğar | tek geometri cümlesi 48 promptta birebir (Bible KANAT bloğu); KİMLİK DİZİSİ SPEC C: sırtta S0-S14 / kızak S15-S28 / yok S29-S47; S1 ve S15 üretim sırasında ilk iki — ilk onaylı kare sonraki kanat/kızak sahnelerine imaj referansı; kanatsız sahnelerde `IN FRAME: back` promptunda pozitif düz sırt cümlesi (D139) | ✅ |
| 5 | S22 · S28 · S38 (kısıtlanmış uzuv · bele kadar sıvı · gövdeye gelen nesne) | POLİTİKA §3 imza ①⑤ · YERCEKIMI S8 (iptal) · LAST SPAN S9 · red defteri PB | üretim reddi (kompozisyon ekseni — sözlük çözmez) | S22 N yan WS, yüz görünür, uzak kıyı çapası; S28 T 3/4 arka ama vizör açık, çevre çapası ("the far edge of the lakebed visible behind her"); S38 kuvvet nesnede ("the core stops against the sole of her braced boot; she stands beside its path"); iki yenilgide kamera değişir, üçüncü yeniden yazım yok | ✅ |
| 6 | S16-S23 · S27-S31 · S37-S39 (efor dizileri) | COUNTED_TURN ⑧ 0,0 NOBODY PAYS · STOLEN_SKY ⑧ 1,7 · D169 · D206 | iş yapılıyor, beden ödemiyor; kesmede sıfırlanıyor | her efor sahnesinde ≥2 kanal + ödeme satırı saniyeli (GÖVDE omuz kalçanın altına · KADANS dördüncü çekiş yavaş · ELDİVEN segmentler gerilir · NEFES omuz); sonraki sahnenin IMAGE'ı kalıntı gövdeyle (yorgunluk 0-6 SPEC'te, düşüş ≤1) | ✅ |
| 7 | S9 · S41 (kapı) · S43→S44 (gösterge) · S35 (kabuk) · S3 (gösterge sönük) | SAHNE_ZINCIRI §1 · T2V-CompBench 0,0687 · KART 5 | klip içinde durum değişimi (kapı açılır · lamba yanar · kabuk çözülür) motorda ya donar ya bozulur | kapı: klip "bir el genişliği aralanmış" ile biter (süreç); gösterge: S43 sönükken biter, S44 yanık açılır (SINIR); kabuk: S35'te pul pul DÖKÜLME süreci (oranla), tamamen çözülmüş hâl S36 IMAGE'ında; gösterge tek ışık noktası, rakam/çentik yok | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S0 (eldiven insert) | HEALING GROUND ② "magic glove" (kare 45) | kolu yazılmayan eldiven sahipsiz doğar, ikinci mürettebat okunur | "her right glove raised palm-up at chest height, the sleeve running down into the lower edge of frame, her helmet and shoulders behind it" — uzuv gövdeye bağlı yazılır | SPEC ② |
| 2 | S1 · S7 · S13 (uçuş) | D44 (süzülen koşu) · KART 8 · ⑭ HAREKET | süzülüş "düşüş" ya da "süper kahraman uçuşu" okunur; çırpma üretilir | "glides, wings level, at one steady rate, losing height slowly; no flapping" + hız gövde-göreli ("a body-length every two seconds"); S13'te "cannot hold the air: drops at twice that rate and meets the frost"; kanat açıklığı "twice her arm-span" | SPEC ⑥ |
| 3 | S16-S23 · S31-S36 (yürüyüş dizileri) | KRONOS ⑫ LEAVES AT 00:48 (konsol platosu) · D212 · T14 döngü riski | orta bölüm platosu; model yürüyüşü döngüye bindirir | her sahnede yeni engel (kabuk · kazıma · kesme · yere değen yağmur · çukur · bacak) ve görünür ilerleme (üs kubbesi her sahnede biraz büyük — ÖLÇEK MERDİVENİ SPEC D); vuruş adı ardışık tekrar 0 | SPEC ⑫ |
| 4 | S2 · S3 · S42 · S44 (kırağı çizgisi sayacı) | D78 (STARLESS CIRCLE sayaç tek karede kanıtlanmadı) · D138 | çizgi "ölçek çentiği" gibi yazılıp yazıya dönüşür; iki uç karşılaştırılamaz | çizgi = duvarda kırağının beyaz sınırı, tek düz hat, işaretli çentik yalnız S2'de (bir kazıma, rakam yok); a/b kare çifti S3 ↔ S42 aynı iç kurulum (J/L) — SPEC C SAYAÇ satırı | SPEC C |
| 5 | S9 · S11 (dramatik ironi taşıyıcısı) | HOOK §3.1 · ①-⑤ taşıyıcı | perde arka planda okunmazsa ironi yok; model perdeyi ön plana alır | I kurulumu kapı 3/4: damla perdesi kapı boşluğunun üst yarısında, "lower than in S7" oran cümlesi; karakter sakin (panik 0) | SPEC ⑫ |
| 6 | S25 · S35 · S47 (vizör/yüz CU) | D167 ⑲ (7 öznitelik red) · D79 · POLİTİKA §3.2 (CU'da bağlam kaybı) | kimlik yığını red; CU'da doku tek başına | yüz ≤3 öznitelik; CU'ya çevresel çapa ("behind her the flooded lakebed" / "the door frame"); vizör "single flat pane inside a thick dark rim, zero tint" | ⑯ |
| 7 | S20 · S32 · S40 · S46 (yağmurun yere değişi · dolu göl) | D209 (dünya çapası) · KART 1 · D39 ("swirl") | göl yatağı sahneden sahneye başka dünya; sıvı akar/döner | DÜNYA ÇAPASI 3 cümle birebir; sıvı "dark, still, matte" — akış/dalga 0; dolan göl OLAY olarak sahne haritasında (S20 uzak uç · S33 şerit · S40 dolu) | SPEC ⑤ |
| 8 | S34-S36 (sıcak çekirdek buharı) | §3.9 kartı kanıt nesnesi (a) · D127 · D143 | buhar yakası "duman perdesi" olur, kıvrılır | "a thin white puff rises to knee height straight up and falls back as dry snow within two seconds; the air above stays clear" — süre ve yükseklik yazılı, "swirl" yok | SPEC ⑥ |
| 9 | S44 (iç damlalar hızlı) | D200 · §3.10 | iç mekânda erimiş kırağı damlaları dış yağmur gibi yavaş çizilir | PHYSICS satırı iç sahnede farklı: "inside the pressurised base water drips fall fast, unlike the slow rain outside" — tek promptta iki hız değil, iç/dış ayrı prompt | SPEC ⑥ |
| 10 | bölüm sınırları S11→S12 · S23→S24 · S35→S36 | 8 dk README "sınır da ardışık çifttir" · ② sınır çifti elle kare | QA yarımı S23↔S24 küme (aynı kurulum) — sınırda sıçrama yok | S23↔S24 küme bilinçli: yarım masterı S23'ün son karesiyle biter, S24 onun devamı; ② raporuna "sınır küme" notu SPEC'te | SPEC A |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| PROMPT_HATA_ONLEME §1 · KRONOS 🅑 %93 | çekirdek 8 cümle + PHYSICS/AUDIO gövde satırı ulaşmazsa önlenebilir hata oranı üç kat | 48/48 promptta §5.1 sekiz cümle (image 7) birebir + PHYSICS (0.38 g · dense cryogenic nitrogen-methane · 0.9 bar · 95 K · slow rain · fast drop) + AUDIO (low, heavy, close; highs die; no dialogue, no music) — film başına bir kez yazılır, kopyalanır |
| D175 · §3.9 çıplak deri = fizik hatası | bilek/boyun/ayak bileğinde deri | üç bölgeli negatif her insanlı promptta; zorlanma eldiven/kumaş üstünde |
| D34 · D45 · D155 | film adı / rol etiketi / defter etiketi ekrana basılır | "THE SLOW RAIN", "kanatçı", "S12", "BÖLÜM" hiçbir prompt gövdesinde yok; Scene n of 48 yalnız ikinci satırda |
| D210 · KRONOS ⑨ RHYME BROKEN | kafiye niyette kalır, lockoff kendi kendine yaklaşır | S47 CAMERA = S0 birebir + işaret satırı; her CAMERA satırı "fixed lockoff — absolutely zero camera movement"; TIMELINE son satırı sürdürme |
| D70 · D215 · HEALING GROUND ⑪ | kuyruk kartı · filigran · true peak | üretim defteri KAPI 0 üç kutu; kurgu kapısı 48 klip · 480 s · kart 0 s · −1,0 dBTP |
| UZAY_USSU §1 · D138 | üs/istasyon ölçüsü prompta metre olarak iner | üs "three body-lengths tall dome", istasyon "a low module barely taller than she is"; metre SPEC D'de |
| KURGU_RITMI §3 · D216 | ambiyans klip sınırında ölür; katman 5 | MUZIK: tek ambiyans yatağı (ağır alçak), J-cut ≥%60, katman ≤4, damla tıkırtısı tek periyodik saat |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | KANAT TAKIMI + kask — referans paketi yok | kanat tek geometri cümlesi birebir; S1/S15 ilk onaylı kareler imaj referansı; kask düz pane + çerçeve; iptal kapısı S1 |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | `fabric` kanat membranı için geçiyor (membran kumaş) — dalgalanma riski | membran 'taut dark membrane stretched on a rigid spar frame' — 'fabric/cloth' 0; rüzgâr yok (1-2 m/s), 'never ripples' yazılmaz, gerginlik pozitif |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | 48 kurulumun optik aritmetiği: 22 kurulum 03 §4b'de lens·mesafe·yükseklikle yazılı | EWS'lerde (G · W · F) figür ≥1/10 kadraj (16-20 m 24mm'de figür ~1/8 kare yüksekliği ✅); insert'ler 1,2-1,6 m |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | damla EWS'de okunmaz | novum sahneleri MS/CU/WS (S0 CU · S7 EWS ⚠️ → S7'de damla YAKIN kadraj kenarında iri, uzaktaki perde 'a band of pale beads'; S24 MS) |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | giysi soluk gri ↔ zemin koyu, pus amber: ayrım var; kanat koyu füme ↔ giysi soluk (S30 batan kanat ikinci figür okunmasın) | tek aksan bandı teal göğüs; zemin tek cümle WORLD'de |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | §3.9 + UZAY_USSU §6 negatif: 'seamless/bubble/dome', 'glow', 'swirl', 'hundreds of' 0; büyük yapı planında ölçek şahidi figür + derin netlik | PLAN Negative Bible'a kart negatifleri; prompta yalnız §5.1 + ≤3 |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | KİMLİK teması sahne indeksleri S1 · S10 · S15 · S19 · S25 · S29 · S45 · S47 (≥3 ✅), bedel sahnesi listede | 02_KONSEPT §4 |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | BEDEL S29 (+ S15 · S30 · S45 zinciri) — numaralı | 02_KONSEPT §7 |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | yasak cümlesi yok; 'no flapping' tek istisna → pozitif 'wings level, gliding' ile birlikte | NEGATIVE'e şiddet/tehlike kelimesi 0 |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | kesici 'sleeve cutter' işlevle; çekirdek 'the core' (yakıt/reaktör adı yok); 'dead' yok → 'unlit' | POLİTİKA §2 sözlüğü uygulandı |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | replik yok | — |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | kapı · gösterge · kabuk · batış · gösterge — hepsi SINIRA taşındı (04 §1 #7) | süreç fiilleri, sınır satırı End/Start |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | V3 iskelet: START FRAME tek satır, Bible tekrar yok | prompt yazımında kural ③ 14.09 tanımı |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | SPEC E her kapı DOĞRULANDI satırıyla; ffmpeg -filters koşusu adım 9b'de | damla hızı için kare farkı ölçümü (tblend) — ⬜ hareket profili adayı |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | üç bölge tek cümlede, satır sonunda bölünmez | NEGATIVE cümlesi tek satır |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | 1 NO. RİSK = damla hızı — sayıyla (04 §1 #1 · 02 §5 A5) | ✅ |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (7 satır, durum ✅ — kapanış 03 §7 · SPEC · Bible kararlarıyla)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (10 satır, SPEC sütunu)
✅ tekrar eden arıza tablosunun HER satırı cevaplandı
→ 05_SAHNE_CALISMALARI/ açılabilir
```
