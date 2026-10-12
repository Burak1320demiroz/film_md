# THE_LAST_GATE
KAYNAK: ham rapor 60 (geçerli 7 [GO 4 · ŞARTLI 3 · biri mod D] · mod V/GEÇERSİZ/TEKRAR 47 · KESİK/DURDURULDU 6) · bulgu 159 tekil satır (🔴 80 · 🟠 79) — araç `--film` 105 ham → 100 tekil gösteriyordu; 64 satırı `(listede yok)` olarak elle ekledim (⑨–⑫ mod V · 'Major' yazımı · skor-satırı alt kalemleri); satırlara birleşen ham kayıt ≈191

Rapor durumu kaynağı: `RAPOR_KONTROL/RAPORLAR/THE_LAST_GATE_B1..B4_20261005_RAPOR_KONTROL.md` (GO: B1 ①③⑤ + B3 ⑤ · ŞARTLI: B1 ② + B3 ②③ · KESİK: ⑬ ×4 + B1 ⑦ ⑫ · TEKRAR 12 · GEÇERSİZ 35). Tek mod D rapor: PART1 ① KARE. Dört ⑬ UYUM ve PART1 ⑦ AKSİYON içeriksizdir (🔴/🟠 yok).

## KİMLİK İZİ VE ÇAPA YÖNTEMİ  (görevdeki 'kimlik izi' uyarısının cevabı)

**Hüküm: 14/60 bayrak YANLIŞ POZİTİF — raporlar bu filmi (THE_LAST_GATE, 96 klip) anlatıyor; fragmanı ya da başka kurguyu değil.**

- *Bayrağın kaynağı:* araç `SCENES OBSERVED`'ı klip sayısının (96) bölenleriyle (96/48/32/24 ±1) karşılaştırıyor. Bu film çok klipli sahne rejiminde (25 sahne / 96 klip): PART 1 = sahne 1–6 (24 klip, 240 s) → rapordaki "6 sahne · 240 s" planın birebir kendisi. PART4 ② DEVAMLILIK'taki "22" ise o merceğin kendi kesim sayısı (③ 15 · ④ 23 diyor; mod V sayımı tutarsız).
- *Replik çapaları (promptlardaki `AUDIO … The line spoken is "…"` satırlarıyla bire bir):* PART1 → K05 "Service berth…", K14 "Seal the service deck.", K19 "You got my signal.", K21 "One seat…", K22 "Then we need a bigger ship.", K23 "Open every cell.", K24 "We have a systems engineer."; PART2 → K25, K27, K30, K36, K45, K47, K48; PART3 → K49, 50, 51, 55, 58, 61, 67, 68, 69, 71, 72; PART4 → K73, 76, 78, 79, 82, 83, 88 (QA'nın duyduğu fazladan satırlar promptsuz — bkz. kusur #17). Karakterler de tutuyor (PART1 ② pasaportları: Mara · Lina · tek koyu kırmızı kol bantlı Saldırı Komutanı; PART3/4: uzaylı mühendis). Fragman 1:00'dır ve bu raporların hiçbiri 1 dk değil.
- *Ama zaman ızgarası kayık:* (a) PART1 master'ının açılışı ≈30 s (plan 40 s); içinde K47'nin replikli klibi kesin ("Disable the drives" 0:18'de), K48/K49/K52/K53 görüntüleri muhtemel (③ süre 230 s) → K05+ klipleri ızgaradan **10 s önce** (klip n ≈ ⌊t/10⌋+2; K05 'Service berth' 0:33, K24 'We have a systems engineer' 3:46). (b) PART2 master'ı 250 s: 4:00–4:10 aralığı 25. bir segment (ikinci "Close the gate."). (c) PART3 ve PART4 ızgaraya oturuyor (klip = 49+⌊t/10⌋ · 73+⌊t/10⌋; PART3 "Gate closure confirmed" 0:04 = K49 · PART4 "Use the local release." 2:31 = K88).
- *Araç hatası:* `prompt_hata_analizi.py` → `bolum_ofseti`, dosya adındaki **mercek numarasını PART aralığı** sanıyor (`_PART2_5_` → "PART2–5", `_PART4_8_` → "PART4–8"); mercek 1–9 olan PART2/3/4 dosyalarında ofset yanlış (örn. PART2_5 → +64 s, PART4_5 → +360 s, PART3_8 → +80 s). Ayrıca aralıklı zaman kodunda (`02:10–02:20`) BİTİŞ damgasını alıyor (bir klip ileri). Bu yüzden `--film` listesindeki **S numaraları güvenilmez**; bu dosyadaki **S sütununu replik çapalarıyla elle yeniden eşledim** (S = klip no; `H` = master'ın ilk 30 s'lik açılışı, `P2 kuyruk` = PART2'nin 4:00–4:10 fazla segmenti).
- *Sınır:* raporlar mod V (kör) — içerik tarifleri bazen sahnede olmayan olay anlatıyor (⑮ "ateş/kaçış", ⑭ "koşu", PART4 son 5 klipte insan yok). Çapası tutmayanlara 🅓 yazdım; zaman ±1 klip oynayabilir.

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |
|---|:--:|---|---|:--:|---|---|---|
| H(K47)/S05 | 🟠 | ① | kask/giysi/ekipman kayması | 🅒 | K47: textless angular rank patch · K05: textless three-winged pilot badge | QA | iki ayrı karakterin rozetini 'drift' saydı |
| H→S06 | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | the banded copper limb of a gas giant fills the lower background | prompt | bant yönü/fırtına lekesi 47 gezegen sahnesinde 1'inde (K44) |
| H(K52)/S10 | 🟠 | ⑥ | arka plan/dünya çapası | 🅒 | K10: soft-capture interface makes contact with the collar | QA | geçit halkası ile yanaşma halkasını karşılaştırdı |
| S05/S14 | 🟠 | ⑤ | arka plan/dünya çapası | 🅒 | K05: a short grey access key already seated in a socket on the console · K14: a security alert on the console rail | QA | iki ayrı mekânın konsolunu aynı sandı |
| S06-S11 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (kapsamlı plan §11: yanaşma K06–K12, K11 geri dönülemez eylem) | hikâye/plan | yanaşma uzunluğu bilinçli; SPEC gerekçeli sapma |
| S06-S11 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | QA | Plateau bütün-film hücresi; part koşusunda maskeli |
| S13 | 🟠 | ① | yerçekimi/süzülme | 🅐 | Nobody walks under weight and nothing falls to the deck — the lanyard never hangs downward. | kadraj kararı | yasak yazılı; 'before the next step' adımı çağrıştırıyor |
| S14 | 🟠 | ⑧ | efor/beden | 🅒 | the flat hand turns over on the rail and stops | QA | hafif düz el; 'ağır eldivenle HUD' olayı promptta yok |
| S15/S17 | 🔴 | ⑥ | yerçekimi/süzülme | 🅑+ | the guard holds his ground at the far end (K15) · each on their own boot locks (K17) | prompt | gardiyana ayak kilidi yok, 'holds his ground' 1g deyimi |
| S15 | 🟠 | ⑧ | efor/beden | 🅐 | the pilot pulls hard on the rail into the door reveal ... the second pull slower than the first | kadraj kararı | oran cümlesi yazılı; QA 'koşu+buton' diye okudu |
| S15-S16 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | the outer plate of her left forearm drags along the door edge and comes away with one single diagonal scuff | QA | çizik = kasıtlı bedel izi; QA 'az' saydı |
| S17 | 🔴 | ⑧ | efor/beden | 🅑 | the pilot comes onto the spine and stops; the six stay at their own bays | prompt | K16 efor borcu K17 başında ödenmiyor; nefes/dinlenme yok |
| S18 | 🔴 | ⑧ | efor/beden | 🅒 | The engineer is working on the inner panel of a cell bay with a short tool | QA | tremoru Lina'ya yükledi; koşan/zorlayan Mara'ydı |
| S18 | 🟠 | ⑪ (listede yok) | ışık | 🅑 | Rows of cool white bay lamps down the cell spine with one warmer service light low near the deck | prompt | K17 ve K18 LIGHT aynı, yön yok; saat yönü 0/92 |
| S19 | 🟠 | ⑧ | efor/beden | 🅐 | the door edge lifts clear of its frame, the second pull slower than the first | kadraj kararı | oran cümlesi yazılı; kasılma görünmemiş |
| S20 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | she holds her ground and the hold stays | QA | karar duruşla veriliyor; mod V ⑩ SPEC'siz |
| S24 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (PART 1 = BAŞ maskesi: Exit & Return —) | QA | BAŞ part'ta Exit hücresi maskeli |
| S25 | 🟠 | ① | yüz/kimlik | 🅐 | real skin pores and sweat, no airbrushing, no waxy texture, no face morphing | referans/panel | yazılı; Veyr yüz plakaları plastik çıktı |
| S25/S33 | 🟠 | ② (listede yok) | yüz/kimlik | 🅒 | K25: an adult face with two symmetrical bony plates behind a clear helmet | QA | 'Pilot' adıyla Veyr ve Mara karıştı |
| S25 | 🟠 | ③ (listede yok) | ses-görüntü uyumu | 🅒 | the four-fingered hand closes on the tool and takes its weight | QA | 'oturan/anahtar kaldıraç' sahnede yok |
| S25 | 🔴 | ⑧ | efor/beden | 🅑 | the four-fingered hand closes on the tool and takes its weight | prompt | oran yok; QA 'kaldıraç' dedi, sahnede el aleti |
| S25-S48 | 🔴 | ⑧ (listede yok) | efor/beden | 🅑 | YOK (klipler arası maliyet köprüsü yok; 'nothing needs correcting') | prompt | 9 kategori satırı: Fatigue/Recovery dahil tek kök |
| S25/P2 kuyruk | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK | QA | Rhyme Pair bütün-film dörtlüsü; part'ta — |
| S25/S36 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | the hand holds the tool still and the head stays where it turned to | QA | mod V ⑩; sakin yüz tasarım |
| S25-S30 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅑+ | 0.0-3.0 s ... 3.0-7.0 s ... 7.0-10.0 s | prompt | 87/92 klipte aynı 3-4-3 iskeleti; tempo düz |
| S25 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA part maskesi: Hook Question —) | QA | part ortasında açılış sorusu ölçülmez |
| S26 | 🔴 | ⑤ (listede yok) | diğer | 🅐 | structures static, no melting or warping | kadraj kararı | yazılı; konsol düğmeleri eridi |
| S26/S37 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | two of the seated adults check their own latches; nobody stands up | QA | 'manken' duruşu mod V uydurması |
| S27 | 🔴 | ⑤ (listede yok) | klon/fazla kişi | 🅐 | Six separate adults at six separate latches, spaced apart with clear deck between them | kadraj kararı | yazılı; Fig 4/5 gövde birleşti |
| S27 | 🔴 | ⑧ | efor/beden | 🅑 | the crew lead starts the nearest latch alone and turns it a short way | prompt | efor/direnç cümlesi yok |
| S27 | 🟠 | ⑮ | yön/180° | 🅑 | the crew lead starts the nearest latch alone | prompt | el/hedef ekran tarafı yazılı değil |
| S28 | 🟠 | ① | el-nesne kaynaşması | 🅑 | YOK — K28 NEGATIVE'de 'Hand-to-surface contact' düşmüş (0-insan şablonu) | prompt | dört parmaklı el makrosu; temas cümlesi yok |
| S28 | 🔴 | ⑧ | efor/beden | 🅑 | the connector goes into the socket and seats with one short push | prompt | 'ağır kablo' yok; efor yazılmamış |
| S28/S30 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | the connector goes into the socket and seats with one short push | QA | mod V ⑩; tereddüt beklentisi SPEC'te yok |
| S29 | 🟠 | ① | parçacık/duman/toz | 🅒 | two separate reports mark the panelling well above the shield edge | QA | mikrogravitede kıvılcım yayı beklenmez; QA 1g aradı |
| S29 | 🟠 | ① | ışık | 🅐 | shadow edges stay razor-sharp and nothing blooms | araç ayarı | bloom kilidi yazılı (0% bloom + nothing blooms) |
| S29 | 🔴 | ⑧ | efor/beden | 🅒 | the pilot rolls the shield a short way along its rail into the sightline | QA | patlama yok; atış kalkana değmiyor |
| S29 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA maske: Stakes —) | QA | maskeli hücre |
| S30 | 🔴 | ① ⑤ | istenmeyen yazı | 🅑 | A gloved hand confirms on a control detail ... releases the berth | prompt | 'release' 6×, kontrol etiketi yasağı yok; K21/K48 var |
| S30 | 🟠 | ③ | ses-görüntü uyumu | 🅑 | a short filtered line. The line spoken is "Send my shuttle empty. Draw them off." | kurgu-ses | tonlama/aciliyet yok; üretim sesi geçici (post-dub) |
| S30/S31 | 🟠 | ⑪ (listede yok) | ışık | 🅐 | Cool white corridor light on the near side, and outside hard sunlight from screen left | araç ayarı | iki klipte birebir aynı LIGHT |
| S30 | 🟠 | ⑭ | diğer | 🅑 | A gloved hand confirms on a control detail | prompt | tutulacak nesne belirsiz ('a control detail') |
| S31 | 🔴 | ① | ortama aykırı ses | 🅐 | no engine sound from outside | kurgu-ses | vakum yasası + açık 'dışarıdan ses yok' yazılı |
| S31/S32 | 🟠 | ② (listede yok) | arka plan/dünya çapası | 🅑 | The empty white service craft runs out along a side inspection corridor | referans/panel | araç silueti/motor sayısı yok; yalnız 'white craft' |
| S31 | 🟠 | ⑤ | kamera/kesme/kadraj | 🅒 | a locked-off camera 40 m from the hull | QA | kilitli kamerada paralaks beklenmez |
| S31/S47 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA maske: Peak —) | QA | maskeli hücre |
| S32 | 🔴 | ① | ortama aykırı ses | 🅐 | A radio link inside the helmet cutting out mid-carrier, nothing from outside. | kurgu-ses | yasa yazılı; patlama sesi yine geldi |
| S32 | 🟠 | ① | arka plan/dünya çapası | 🅑 | the banded planet filling the background | prompt | K32 insansız şablonda 'structures static' yok; K44'te var |
| S32 | 🔴 | ⑤ (listede yok) | parçacık/duman/toz | 🅒 | separate loose parts drifting beside it | QA | kopan parçalar kasıtlı |
| S32 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅐 | a locked-off camera 8.0 m from the subject | araç ayarı | kilit yazılı; yeniden-ortalama oldu |
| S32 | 🟠 | ⑪ (listede yok) | ışık | 🅑+ | Cool white corridor light on the near side, and outside hard sunlight from screen left | prompt | dış vakum planına koridor ışığı kopyalanmış |
| S32/S43 | 🟠 | ⑪ (listede yok) | ışık | 🅐 | 0% bloom, no glow, no soft focus | araç ayarı | bloom kilidi yazılı; vakumda parıltı çıktı |
| S32 | 🔴 | ⑮ | yön/180° | 🅓 | Exactly 0 human characters in frame | QA | insansız klipte 'bakış' olayı yok |
| S33 | 🔴 | ⑤ (listede yok) | kask/giysi/ekipman kayması | 🅐 | a single neck ring ... two neck rings | referans/panel | boyun halkası yazılı; yaka çöktü |
| S33 | 🔴 | ⑧ ⑭ | yerçekimi/süzülme | 🅑 | the pilot goes through first on the rail, the tall engineer after her | prompt | 'yürümez' yasağı K13'te var, K33'te yok |
| S34 | 🔴 | ⑤ (listede yok) | klon/fazla kişi | 🅑+ | In one two-sided frame the tall systems engineer closes an intermediate bulkhead panel | prompt | 'two-sided frame' bölünmüş kompozisyon çağırıyor |
| S35 | 🟠 | ① | el-nesne kaynaşması | 🅑 | the harness latch closes across her and takes up | prompt | kemer tokası↔göğüs plakası nesne-nesne; temas cümlesi yalnız el |
| S35 | 🟠 | ⑤ (listede yok) | efor/beden | 🅒 | each anchoring on a handhold rather than sitting under weight | QA | tutamakta süzülme tasarım; 'döngü nefes' belirsiz |
| S35 | 🔴 | ⑤ (listede yok) | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | yazılı; 'üçüncü eldiven' izi çıktı |
| S35/S36 | 🟠 | ⑤ | klon/fazla kişi | 🅑+ | Exactly 3 human characters in suits, and exactly one tall figure | prompt | K36 gövdesinde uzun figür yok; üç kişilik sahne, NEGATIVE dört |
| S35 | 🔴 | ⑧ | efor/beden | 🅑 | the harness latch closes across her and takes up | prompt | kayış direnci/omuz eğimi yok |
| S35 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | the harness latch closes across her and takes up | QA | mod V ⑩; tereddüt SPEC'te yok |
| S35/S36 | 🔴 | ⑮ | yön/180° | 🅑 | K36: 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot · K35: 2.6 m from the pilot's seat | prompt | bakış yönü/ekran tarafı kilidi yok |
| S36 | 🟠 | ① | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | cümle yazılı; parmaklar konsola karıştı |
| S37 | 🟠 | ① | klon/fazla kişi | 🅑+ | The other adults wear the same white main suit with measured blue and grey duty panels and closed helmets. | prompt | yedi oturan için tek aynı-giysi cümlesi klon çağırıyor |
| S37 | 🔴 | ⑤ (listede yok) | klon/fazla kişi | 🅐 | Seven adults are each seated in one separate seat with clear space between the seats | kadraj kararı | yazılı; oturanların gövdeleri birleşti |
| S37 | 🔴 | ⑧ | efor/beden | 🅑 | the crew lead brings the next harness down over a seated adult and it takes | prompt | yük/ağırlık karşıtı hareket yok |
| S38 | 🟠 | ① | diğer | 🅑 | YOK — K38 NEGATIVE'de 'structures static, no melting or warping' düşmüş | prompt | insansız şablon parçacık/yapı kilidini atıyor |
| S38 | 🟠 | ⑤ | arka plan/dünya çapası | 🅓 | two pressure panels of the port transfer tunnel close in turn | QA | K38'de pencere/ufuk yok |
| S38 | 🔴 | ⑤ (listede yok) | istenmeyen yazı | 🅑 | every badge and patch is textless | prompt | panel/plaket yasağı yok; K21/K26/K48'de özgül cümle var |
| S38-S41 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (bütün-film hücresi) | QA | Plateau part'ta —; K38–K41 insansız tasarım |
| S39 | 🟠 | ⑮ | yön/180° | 🅓 | Exactly 0 human characters in frame | QA | K39 insansız göbek bağı; 'ateş' yok |
| S40 | 🔴 | ① | ortama aykırı ses | 🅑+ | Six heavy strikes spaced along the cradle, then one flight clearance tone. | kurgu-ses | dış planda 'gövdeden taşınır' kaydı yok; ses isteniyor |
| S41 | 🟠 | ⑤ (listede yok) | kamera/kesme/kadraj | 🅐 | a locked-off camera 40 m from the hull | araç ayarı | kilitli kamera yazılı; ufuk titredi |
| S41/S42 | 🔴 | ⑪ (listede yok) | ışık | 🅐 | Hard sunlight from screen left | araç ayarı | iki klipte aynı LIGHT yönü yazılı |
| S42 | 🔴 | ⑮ | yön/180° | 🅓 | Over the pilot's shoulder both her gloves make small separate corrections | QA | K42'de kaçış yok |
| S43 | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | a broad copper wash from the banded planet filling the whole background | prompt | gezegen-sabit cümlesi K44'te var, K43'te yok |
| S44? | 🔴 | ⑤ | arka plan/dünya çapası | 🅓 | YOK (K44: dış gezegen planı) | QA | 03:12 'hücre kapısı' bu klipte yok |
| S45 | 🟠 | ⑤ (listede yok) | yerçekimi/süzülme | 🅓 | YOK (K45: üç figür istasyonda, yürüyüş yok) | QA | 03:22 yürüme döngüsü bu klipte yok |
| S46 | 🔴 | ① | ortama aykırı ses | 🅐 | A command channel carrier and the rhythm building under it. | kurgu-ses | yasa yazılı; motor uğultusu eklenmiş |
| S46? | 🟠 | ⑭ | yerçekimi/süzülme | 🅓 | YOK (K46: üç araç, dış plan; koridor/bacak yok) | QA | 03:30 koşu K46'da yok |
| S47 | 🟠 | ⑭ | oyunculuk | 🅐 | the officer reads the rail and the hand comes onto it ... the hand stays down | kadraj kararı | uzanış yazılı; yarıda kesildi |
| S48 | 🔴 | ③ | ses-görüntü uyumu | 🅑 | then a flat filtered command voice. The line spoken is "Close the gate." | kurgu-ses | K47/K48 aynı tarif; yaş/tını kilidi yok |
| S48 | 🔴 | ⑧ | efor/beden | 🅑+ | her grip tightening on the rail as the mass comes with her | prompt | komutan eldiveni için yanlış özne; 'rail' yok |
| S48/P2 kuyruk | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | IN FRAME: hands | QA | part sonu el makrosu tasarım; Final Beat bütün-film |
| S48 | 🟠 | ⑮ | yön/180° | 🅑 | A gloved hand in white armour closes one guarded control on the command rail | prompt | elin giriş yönü/ekran tarafı yok |
| P2 kuyruk | 🔴 | ③ | ses-görüntü uyumu | 🅓 | YOK ('Close the gate.' yalnız K48'de, 1 kez) | QA | 4:00–4:10 fazla segment; ikinci replik promptsuz |
| P2 kuyruk | 🔴 | ⑤ (listede yok) | diğer | 🅓 | YOK | QA | 04:05 mandal pimi; 4:00–4:10 segmenti promptsuz |
| P2 kuyruk | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA maske: Exit & Return —) | QA | maskeli hücre |
| S49/S72 | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK | QA | Rhyme Pair bütün-film dörtlüsü; part'ta — |
| S49 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA maske: Hook Question —) | QA | maskeli hücre |
| S50/S57/S63 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | the course holds on the centre and nobody changes it | QA | mod V ⑩; karar ağırlığı SPEC'siz |
| S51 | 🟠 | ① | el-nesne kaynaşması | 🅑 | A four-fingered hand tries a service connector in a second socket | prompt | 0-insan şablonu: temas cümlesi düşmüş; QA 'düğme' dedi |
| S51 | 🔴 | ⑧ | efor/beden | 🅑 | the connector goes into the second socket and seats | prompt | 'söküm' yok; efor/direnç cümlesi yok |
| S51/S62/S68 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | the hand squares the two circles against one another | QA | mod V ⑩; tereddüt SPEC'te yok |
| S52/S56 | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | a copper wash from the banded planet below | prompt | bant yönü iki klipte de yazılı değil |
| S52/S53 | 🔴 | ⑪ (listede yok) | ışık | 🅐 | Hard sunlight from screen left on the hull | araç ayarı | iki klipte aynı yön yazılı; kesmede 2→12 kaydı |
| S53 | 🔴 | ① | ortama aykırı ses | 🅐 | A strike carried through the hull from inside, nothing at all from outside. | kurgu-ses | yasa + 'no fireball, vacuum preserved' yazılı |
| S53 | 🔴 | ⑪ (listede yok) | ışık | 🅐 | 0% bloom, no glow ... nothing blooms | araç ayarı | yazılı; vakumda ışık huzmesi/parıltı çıktı |
| S53 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA maske: Stakes —) | QA | maskeli hücre |
| S54 | 🔴 | ⑧ | efor/beden | 🅑 | the harnesses and handholds take up and stop the movement | prompt | boyun/nefes gerilimi yazılı değil |
| S54/S61/S72 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | nobody speaks again; the three hold and the edge keeps moving | QA | mod V ⑩; sabit yüz SPEC'te kusur değil |
| S57 | 🟠 | ① | yerçekimi/süzülme | 🅐 | both move hand over hand on the rail with their boots locking as they go | kadraj kararı | AUDIO 'magnetic steps' yürüyüş çağırıyor |
| S57 | 🟠 | ⑧ | efor/beden | 🅒 | both move hand over hand on the rail with their boots locking as they go | QA | 'ağır adım' beklentisi 1g; mikrogravite |
| S57/S66 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅑+ | 0.0-3.0 s ... 3.0-7.0 s ... 7.0-10.0 s | prompt | 87/92 klipte aynı 3-4-3 iskeleti; tempo düz |
| S57-S60/S65-S68 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (bütün-film hücresi) | QA | Plateau part'ta — |
| S58 | 🔴 | ① | klon/fazla kişi | 🅑+ | The other adults wear the same white main suit ... six adults move in one single-file line | prompt | altı özdeş giysi + tek sıra = kopya yürüyüş çağrısı |
| S59 | 🟠 | ① | parçacık/duman/toz | 🅑 | one single shot from the nearer guard lands on the shield face | prompt | çarpma kıvılcımı↔el sınırı yok; QA 'plazma torç' dedi |
| S59 | 🔴 | ⑧ | efor/beden | 🅑 | her hand takes the shield and rolls it along the rail | prompt | tutma gerilimi yok; raylı kalkan |
| S60 | 🔴 | ⑧ | efor/beden | 🅒 | the four-fingered hand takes the panel control and the panel starts across | QA | motorlu panel; elle çok-tonluk kapı yok |
| S62 | 🟠 | ① | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | cümle yazılı; eldiven ekrana karıştı |
| S62 | 🟠 | ⑧ | efor/beden | 🅑 | the hand squares the two circles against one another | prompt | parmak/eldiven direnci yazılı değil |
| S62 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | A gloved hand holds two plain circles side by side on a console surface | QA | 'daire birleştirme' karar sahnesi değil; mod V |
| S63 | 🟠 | ⑧ | efor/beden | 🅑 | she pushes both controls forward and holds them | prompt | oran düşüşü yok |
| S65 | 🔴 | ① ⑪ | kamera/kesme/kadraj | 🅑+ | The two figures keep separate halves of the frame and never overlap. | prompt | 'separate halves' 11 klipte; bölünmüş ekran çağrısı |
| S65 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | Even cool white ceiling light in the pressurised service compartment ... the shadows stay shallow | QA | basınçlı iç hacim; vakum gölgesi beklenmez |
| S66 | 🔴 | ① | zemine geçme | 🅑 | She never rises or falls — she keeps the motion she was given | prompt | gövde↔güverte sınırı yok; K16'da 'never passes through' var |
| S66/S67 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅐 | her shoulders dropping as the load takes up | kadraj kararı | maliyet işareti yazılı (K67) |
| S67 | 🟠 | ⑦ | hikâye/anlatım/kurgu | 🅐 | the engineer's glove closes on it once and the line takes up | kadraj kararı | kavrama yazılı; QA kesim öncesi emin değil |
| S68 | 🟠 | ⑪ (listede yok) | ışık | 🅐 | each one shows the same independent state | araç ayarı | göstergeler sabit kalmalıydı; parlaklık düştü |
| S71 | 🔴 | ⑧ | efor/beden | 🅒 | A gloved hand rests beside the same plain mechanical release lever | QA | dönen kapı çarkı sahnede yok |
| S72 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (ORTA maske: Exit & Return —) | QA | maskeli hücre |
| S73 | 🔴 | ① | yerçekimi/süzülme | 🅑 | one more stands alone beside the row | prompt | ayakta duran figürde bot kilidi/tutamak yok |
| S73/S74/S76 | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | a copper wash from the banded planet | prompt | bant yönü hiçbir klipte yok; 25°→0°→60° kaydı |
| S73/S96 | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK | QA | Rhyme Pair bütün-film; plan: K96↔K85 eş kadraj |
| S73/S85 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | nobody moves out of a seat and no door opens | QA | mod V ⑩; kask arkası sakin yüz tasarım |
| S73-S76 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (SON maske: Stakes —) | QA | maskeli hücre |
| S74 | 🔴 | ① | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | yazılı; başparmak/dokunmatikte bozuldu |
| S74 | 🟠 | ① | ışık | 🅐 | nothing blooms | araç ayarı | bloom kilidi yazılı |
| S74 | 🔴 | ⑧ | efor/beden | 🅑 | the curve draws out toward the ring centre and locks into place | prompt | parmak/eldiven direnci yazılı değil |
| S74/S78/S86 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | the hand comes off and the loaded curve holds unchanged | QA | mod V ⑩; görev eli SPEC'te kusur değil |
| S75 | 🟠 | ⑤ | kamera/kesme/kadraj | 🅒 | a locked-off camera 40 m from the hull | QA | kilitli kamera; paralaks beklenmez |
| S76 | 🔴 | ① | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | yazılı; el kumandadan geçti |
| S78 | 🔴 | ① | el-nesne kaynaşması | 🅑 | YOK — K78 NEGATIVE'de 'Hand-to-surface contact' düşmüş (0-insan şablonu) | prompt | konnektör makrosu; K28 ile aynı kök |
| S78 | 🔴 | ⑧ | efor/beden | 🅑 | it goes into the handheld unit and seats with one push | prompt | efor/direnç cümlesi yok |
| S78/S79 | 🟠 | ⑪ (listede yok) | ışık | 🅑+ | Hard sunlight from screen left along the hull, cold white lamps at each rail cradle, and low warm seat lighting | prompt | pod içi K79'a dış güneş cümlesi kopyalı |
| S79 | 🔴 | ① | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | yazılı; el kayışa geçti |
| S79/S85 | 🟠 | ⑤ | sayı/nesne sayısı | 🅒 | Exactly 5 human characters in suits (K79) · pilot comes into the last transfer pod (K85) | QA | farklı iki araç kabinini aynı sandı |
| S79 | 🟠 | ⑧ | efor/beden | 🅒 | checks the harnesses of four seated adults one at a time | QA | 'koridor yürüyüşü' yok; 1g beklentisi |
| S80 | 🟠 | ① | parçacık/duman/toz | 🅑 | the pod translates clear of the rail on its own small thrusters | prompt | plume tarifi + parçacık cümlesi yok; K07'de var |
| S80/S81 | 🟠 | ② | arka plan/dünya çapası | 🅐 | Two more transfer pods leave the rail in turn ... running out along the same open lane | kadraj kararı | tek şerit yazılı; çok rampalı bay çıktı |
| S82-S84/S93-S96 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (bütün-film hücresi) | QA | Plateau part'ta — |
| S83 | 🔴 | ① | yerçekimi/süzülme | 🅐 | works her way along a short connecting corridor hand over hand on the handholds | kadraj kararı | yazılı; yine de zemin kayması çıktı |
| S83/S85 | 🟠 | ② | kask/giysi/ekipman kayması | 🅑 | YOK — K85'te 'The pilot wears ...' cümlesi yok (K83'te var) | prompt | QA Mara/Lina'yı karıştırmış olabilir |
| S83 | 🟠 | ⑧ | efor/beden | 🅐 | her grip tightening on the rail as the mass comes with her | kadraj kararı | efor cümlesi yazılı; görünmemiş |
| S83 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅐 | a locked-off camera 2.4 m along the corridor axis | araç ayarı | kilit yazılı; takip hareketi çıktı |
| S84/S87 | 🟠 | ② | arka plan/dünya çapası | 🅒 | the craft breaks off and turns away (K87) | QA | takipçi araç sığmaz = hikâye kuralı |
| S85 | 🟠 | ① | zemine geçme | 🅑 | the pilot pulls herself in through the hatch and takes a handhold | prompt | gövde↔kapı çerçevesi sınırı yok |
| S86 | 🔴 | ① | el-nesne kaynaşması | 🅑+ | the three pairs keep separate stations and no two overlap | kadraj kararı | tek makroda altı eldiven; fazla parmak riski |
| S86 | 🔴 | ⑧ | efor/beden | 🅑 | the first and second harness latches close on their own seats | prompt | hizalama çabası/parmak sertliği yok |
| S86 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | nothing reopens | QA | mod V ⑩; rahatlama beklentisi SPEC'siz |
| S87 | 🔴 | ① | ortama aykırı ses | 🅐 | A withdrawal advisory on the enemy channel, then a command voice with no reply. | kurgu-ses | yasa yazılı; motor/gümbürtü eklendi |
| S88 | 🔴 | ① | el-nesne kaynaşması | 🅐 | a four-fingered hand works the handheld unit ... no extra fingers | referans/panel | dört parmak yazılı; el uzadı |
| S89 | 🔴 | ① | el-nesne kaynaşması | 🅐 | Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. | kadraj kararı | yazılı; kol avuçtan geçti |
| S89 | 🔴 | ⑧ | efor/beden | 🅐 | the lever comes down through its full travel and stops hard at the end | kadraj kararı | yük ve duruş yazılı; deltoid/kol zorlanması yok |
| S91 | 🟠 | ⑤ | parçacık/duman/toz | 🅒 | breaks away in separate rigid pieces on straight paths | QA | kopan parçalar kasıtlı |
| S91-S96 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅐 | K95: the adult crew lead raises one open hand · K96: the pilot raises one open hand in answer | kadraj kararı | ② de son 5 klipte insan yok diyor; prompt insan ister |
| S92? | 🔴 | ① | parçacık/duman/toz | 🅓 | YOK (K92 dış plan; iç koridor/toz yok) | QA | 03:12 'iç koridor' bu klipte yok |
| S95-S96 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK (plan DÖNGÜ KANITI: K96 ↔ K85) | QA | döngü planda var; QA açılışa bakmış |

## ÖZET
```
HÜKÜM        🅐 41 · 🅑 42 · 🅑+ 13 · 🅒 53 · 🅓 10   = 159 satır
             🅑/(🅐+🅑) = %57  (🅑+ dahil: 55/96) · 🅒'nin 37'i (listede yok) ⑨–⑫ mod V satırı
TÜR (en sık 5) efor/beden 28 · oyunculuk 19 · hikâye/anlatım/kurgu 16 · el-nesne kaynaşması 13 · arka plan/dünya çapası 12
KAPANMA      QA 62 · prompt 50 · kadraj kararı 23 · araç ayarı 11 · kurgu-ses 8 · referans/panel 4 · hikâye/plan 1
PART BAZINDA P1: 🅐 3 · 🅑 3 · 🅑+ 1 · 🅒 10 · P2: 🅐 17 · 🅑 21 · 🅑+ 7 · 🅒 18 · 🅓 9 · P3: 🅐 8 · 🅑 9 · 🅑+ 3 · 🅒 13 · P4: 🅐 13 · 🅑 9 · 🅑+ 2 · 🅒 12 · 🅓 1
```

Okuma:
1. **Prompt kaynaklı bulgu (🅑 + 🅑+) 55 · model sapması (🅐) 41.** 55'in 30'u üç kökte: 16 efor (92 klibin 79'unda efor/oran cümlesi hiç yok) · 12 insansız ya da dört-parmaklı-el şablonlu klipte (36 klipte NEGATIVE kısalıyor: temas/giysi/parçacık cümleleri düşüyor) · 2 sahne bazında düşen metin yasağı (K30, K38).
2. **🅒 en büyük tek grup (53):** 33'i ⑨–⑫ mod V satırı (SPEC'siz plan-sadakati mercekleri; Rhyme Pair / Plateau / Hook / Exit hücreleri part koşusunda maskeli) — kalan 🅒'ler mikrogravite 1g beklentisi, iki ayrı karakteri/mekânı karıştırma.
3. **🅐'nın kapanma yeri prompt DEĞİL:** vakumda ses (kurgu-ses), temas füzyonu (kadraj kararı), bloom (araç ayarı) — 19.09 sınıf dosyasındaki 🅐1/🅐2/🅐4 bu filmde de aynen tekrar etti.
4. En kalabalık tür **efor/beden (28)**: ⑧ olay tablosunun neredeyse tamamı 🔴 'High'; çünkü 13/92 klip dışında hiçbir promptta efor işareti yok ve hiçbirinde sayısal oran yok.

## PROMPT METNİNİN KENDİ KUSURLARI
Okunan: K05–K96, 92 klibin IMAGE + VIDEO promptu (184 metin) ve K01–K04 kesim kartları. Bulgudan bağımsız.
| # | sahne | alıntı | neden kusur |
|---|---|---|---|
| 1 | K01–K96 (184/184 prompt) | `Clip 16 of 96.` (her IMAGE ve VIDEO'nun 2. satırı) | Meta sayaç etiketi ("Scene n of N" eşdeğeri): motor sıra numarasını görür; üstelik aynı promptta "No readable text, letters, digits or numerals" yasağı var — rakam yasağı ile rakam içeren etiket yan yana. |
| 2 | K08, 12, 15, 22, 23, 24, 29, 43, 44, 46, 54, 56, 59, 60, 67, 71, 72, 80, 88, 89, 94 (21 klip · 42 prompt) | `the same position, height and lens as Clip 5` (K08 CAMERA) | Başka klibe çapraz atıf: prompt "tek başına çalışır" kuralını (BOLUM başlığı) bozuyor; üretim motoru "Clip 5"i bilmez, cümle boşa gider ya da tahmin ettirir. |
| 3 | 38 klip IMAGE (`[EKSEN]` cümlesi) · K71 · K45 | `the ship's nose points to screen right for the whole film` · `the identical pod design seen berthing at the start of the film` · `the first small easing of the film` | Model "bütün film"i görmez: kendi 10 s'sini üretir. Film boyu süreklilik cümlesi motorun işleyemeyeceği meta bilgi. |
| 4 | K18 (VIDEO AUDIO) | `one word spoken close inside the helmet — the pilot names her sister and nothing more is said. No dialogue in this shot.` | Kendi içinde çelişki: "bir kelime söylenir" + "No dialogue". Üstelik ad isteniyor ama ad yasağı var (D34): PART1'in 13 içerikli raporundan 9'u (③④⑥⑨⑩⑪⑫⑭⑮) duyduğu sözü "Elena." diye yazdı — filmde böyle bir ad yok (Lina); ② 'Lina.' duydu. |
| 5 | K24 · K35/K36/K45/K50/K54/K61/K85/K88/K89/K96 (NEGATIVE) | `Exactly 4 human characters in suits, and exactly one tall figure …` (K24: sahnede 1 mühendis + 2 teknisyen + 1 uzun figür) · `Exactly 3 human characters in suits, and exactly one tall figure …` (üçlü kadrajlar: pilot + mühendis + uzun figür) | Sayı çelişkisi: sahnede 3 kişi varken NEGATIVE 4 kişi diyor (uzun figür hem "insan"a hem ayrıca sayılıyor) → "fazla kişi / cinsiyet-giysi değişimi" riskini bizzat yaratıyor (⑤ K35→K36 🟠). |
| 6 | K36, 45, 50, 54, 61, 72, 86, 88, 89 | NEGATIVE'de `exactly one tall figure with two arms, two legs and one head`; IMAGE gövdesinde uzun figürün tarifi YOK | Figür yalnız yasak cümlesinde tanımlı; pozitif tarif yok → motor kimliğini uydurur (K36 'sol/sağ figür' kayması). |
| 7 | K11 · K32 · K89 · K93 (IMAGE ↔ VIDEO) | K11 IMAGE `after the fourth the two hulls no longer move relative to one another` ↔ VIDEO START `all four clamps open above the seated ring` · K89 IMAGE `the four pod cradle latch indicators change to their open state` ↔ START `all four latch indicators still closed` · K93 IMAGE `the whole area is dark` ↔ START `still bright` · K32 IMAGE `a small bright scar opens on the drive housing` ↔ START `the empty craft filling the frame` | Görsel ile video arasında çelişki: IMAGE promptu (başlangıç karesi) eylemin SONUÇ halini anlatıyor, VIDEO `START FRAME` ön halini istiyor; I2V başlangıç karesi olayı çoktan yaşamış çıkıyor. |
| 8 | K18 · K45 · K64 · K42 | `when she registers something off-frame and stops` · `the moment is allowed to sit` · `nothing needs correcting` · `the edge is closing faster than the ship is closing the distance` · NEGATIVE `the difficulty is timing only` | Motorun gösteremeyeceği zihinsel/soyut ifadeler: "fark etmek", "an'ın oturmasına izin vermek", "zorluk yalnız zamanlama". Görünür karşılığı yok. |
| 9 | K34 · K65 (ve K15, 19, 20, 57, 59, 66, 67, 71, 72, 95) | `In one two-sided frame …` (K34) · `The two figures keep separate halves of the frame and never overlap.` (11 klip) | "Çerçevenin ayrı yarıları" bölünmüş ekran çağrısı: K65 🔴 'split-screen' çıktı, K34'te 🟡 'central split-screen partition'. Tek kameralı kilitli kadrajda iki yarı istemek yapılamaz/yanlış anlaşılır istek. |
| 10 | K30 (IMAGE+VIDEO) | `A gloved hand confirms on a control detail … releases the berth … commands the release … Four soft releases` | Tutulacak nesne belirsiz ("a control detail"), `release` kökü 6 kez; filmin tamamında 132 kez (92/92 klip). Büyük harfli jeton yok ama "rose/EVA" mekanizması küçük harfle de işledi: ekrana `SUIT RELEASE`, `EXTRA RELEASE`, `500` basıldı (🔴). |
| 11 | K48 · K71 · K79 · K83 · K85 · K89 (VIDEO TIMELINE) | `her grip tightening on the rail as the mass comes with her` | Aynı efor kalıbı yanlış yerlere yapıştırılmış: K48'de özne "the commanding officer's gauntlet" (komutan, tek eldivenli el makrosu) ama cümle `her` + `rail` diyor → özne/nesne uyumsuz; K71'de kadrajda yalnız 'hand beside the lever' var, tutulan ray yok; K79'da koltuk kontrolü yapan kişinin kolu. |
| 12 | K40 (VIDEO AUDIO) | `Six heavy strikes spaced along the cradle, then one flight clearance tone.` | Ortama aykırı istek: dış vakum planında (20 m uzaktan, insansız) mekanik vuruşlar "gövdeden taşınır" nitelemesi olmadan isteniyor → QA 🔴 'dış vakumda kenet sesi'. |
| 13 | K31 · K32 (LIGHT) · K79 (LIGHT) | `Cool white corridor light on the near side, and outside hard sunlight from screen left …` (dış vakum planlarında) · K79 pod içi: `Hard sunlight from screen left along the hull …` | Ortama aykırı ışık kaynağı kopyası: dış planda koridor ışığı → QA ⑪ 'vakumda yumuşak dolgu'; iç mekâna dış güneş cümlesi → 'ana ışık yönü atladı'. |
| 14 | K15 · K20 · K73 · K13 | `the guard holds his ground` · `she holds her ground` · `one more stands alone beside the row` · `before the next step` | 1g deyimleri mikrogravite filminde: duran/yürüyen beden çağrıştırıyor, bot kilidi/tutamak yazılı değil → ⑥ 'zemine basan gardiyan', K73 'zeminde kayan ayakta figür'. |
| 15 | 87/92 klip (VIDEO TIMELINE) | `0.0-3.0 s — … 3.0-7.0 s — … 7.0-10.0 s — … holds/stays` | Aynı 3-4-3 saniye iskeleti ve "hold" bitişi: tempo düzlüğünün (⑩ 'Tempo Flatline' 🔴) kaynağı şablonun kendisi. |
| 16 | 31 insansız klip + K25, K28, K51, K68, K78 (36 klip) · NEGATIVE | `Exactly 0 human characters …` şablonu: yalnız 4-5 cümle; `Equipment and clothing identical…`, `Particles obey the stated microgravity…`, `Hand-to-surface contact keeps a clear boundary…` YOK | Şişkin değil **eksik** NEGATIVE: kısaltma dört parmaklı el makrolarına da uygulanmış; kaynaşma bulguları tam bu klipte çıktı (K28 🟠, K51 🟠, K78 🔴; K38 yapı kayması, K80 duman). |
| 17 | K17, K18, K26, K31, K52, K56, K57, K65, K87 (VIDEO AUDIO) | `A targeting advisory on the radio, thin and filtered. No dialogue in this shot.` (K56) · `Approaching magnetic steps and one short security order. No dialogue in this shot.` (K57) · `A withdrawal advisory on the enemy channel, then a command voice with no reply. No dialogue in this shot.` (K87) | Kendi içinde çelişki + motorun betimlemeyi seslendirmesi: konuşma çağrıştıran AUDIO betimi ('advisory', 'order', 'radio talk', 'names her sister') ile "No dialogue" yan yana. QA'nın duyduğu promptsuz repliklar tam bu klipler: K56 "Vector hold, Interceptor 2." / "New firing line confirmed.", K57 "Maintain corridor line.", K87 prompt cümlesinin kendisi "Withdrawal advisory on enemy channel." (+ "Abort the approach immediately."), K17 "Zero seven alpha…", K26 "Detached.", K65 "Sending to visitors…". |
| 18 | 92 klip · NEGATIVE uzunluğu | IMAGE: min 402 · ortanca 782 · ort. 726 · maks 1063 (K54) karakter; VIDEO: min 482 · ortanca 862 · ort. 806 · maks 1143 (K54) | İnsanlı klipte NEGATIVE promptun karakterlerinin %41'i (IMAGE) / %37'si (VIDEO); 7–10 cümle (㉗ tavanı 11'i geçmiyor ama her sahneye kopyalanıyor, sahneye özel olan 1–3 cümle). |

## 19.09 KURALLARI BU FİLMDE
| kural | yazılı mı (kaç sahnede) | yine de bulgu çıktı mı (sayı) | okuma |
|---|---|---|---|
| 🅑1 ses yasası | EVET — vakum cümlesi `Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit` **92/92 video promptunda**; ek `nothing from outside` 10 klipte (K06, 07, 10, 31, 32, 41, 52, 53, 77, 81) | **6 🔴** (🅐 5 · 🅑+ 1): K31, K32, K40, K46, K53, K87 | Kural uygulandı ve ÇALIŞMADI: 6/6'sı vakum yasası yazılıyken çıktı; 3'ü açık 'nothing from outside' cümleli klipte (K31, K32, K53). Tek davet K40 (AUDIO dış vuruş istiyor). → 🅐1 tavanı doğrulandı, kapanma kurgu-ses. |
| 🅑2/2a temas (nesne-nesne dahil) | KISMEN — el-yüzey cümlesi **56/92** (insanlı klipler); **36 klipte yok** (31 insansız + dört parmaklı el makroları K25, K28, K51, K68, K78); nesne-nesne genel cümle **0/92**; sahneye özel temas-yasağı 8 klipte (K15, 16, 32, 34, 60, 69, 70, 92) | **15 temas/kaynaşma satırı** (9 🔴 · 6 🟠; 🅐 8 · 🅑 6 · 🅑+ 1) + K59 kıvılcım↔el (🅑) | Cümle düştüğü yerde çıkan: K28, K51, K78 (el makroları), K35/K66/K85/K59 (nesne-nesne, gövde↔yapı). Cümle varken çıkan 8 satır 🅐2 (kapanma kadraj kararı). 19.09'un 2a bulgusu bu filmde de geçerli: genel cümle el-yüzeyi kapsıyor, gövde↔kapı çerçevesi/kemer tokası kapsamsız. |
| 🅑3 giysi birebir | KISMEN — `Equipment and clothing identical throughout` 56/92; pilot giysi cümlesi 37 klipte, tam hâli (3 kaburga + boyun halkası + eldiven) 22/37, kırpık 15/37 (`IN FRAME` kuralı) | **3** (🅐 1 · 🅑 1 · 🅒 1) | Giysi kayması az: K33 boyun halkası (🅐), K85'te pilot giysi cümlesi hiç yok (🅑), rozet 'drift' 🅒. Kırpma kararı bulguya dönüşmedi. |
| 🅑4 ortam sayısı + adı | AD: EVET 92/92 (`continuous microgravity inside the pressurised hull and hard vacuum outside`); SAYI: **0/92** (g/m·s⁻² yok, 'orbital free fall') | **8 yerçekimi/süzülme satırı** (4 🔴 · 4 🟠; 🅐 3 · 🅑 2 · 🅑+ 1 · 🅓 2) | Hepsi 'yürüme/zemin kayması': ad yazılı olduğu için 1g sapması 🅐 (K13, K57, K83), ama yürüme/yer çağrıştıran deyimler (K13 'next step', K15/K20 'holds … ground', K73 'stands') 🅑/🅑+. Sayı yokluğu bu filmde ölçülebilir fark yaratmadı (rejim tek: mikrogravite). |
| 🅑5 efor oranı | KISMEN — efor/oran işareti **13/92** klipte (K13, 15, 16, 19, 76 `the second pull slower than the first` · K48, 71, 79, 83, 85, 89 `her grip tightening … the mass comes with her` · K67, K88 `shoulders dropping`); sayısal oran **0/92** | **28 satır** (19 🔴 · 9 🟠; 🅐 4 · 🅑 15 · 🅑+ 1 · 🅒 8) | En kalabalık tür. Cümle yokken çıkan 🅑 (K17, K25, K27, K28, K35, K37, K51, K54, K59, K62, K63, K74, K78, K86 + '25-48' maliyet köprüsü), cümle varken çıkan 🅐 (K15, K19, K83, K89): 19.09'daki 'kapı cümlenin varlığını sayıyor, şiddetini ölçmüyor' bu filmde de aynen. K48'de kalıp yanlış özneye kopyalanmış (🅑+). |
| 🅑6 büyük harfli jeton yok | EVET — gövdede büyük harfli jeton 0; NEGATIVE'de yalnız `CGI` (184/184); meta `Clip n of 96` 184/184 | **2 🔴 yazı** (🅑 2): K30 `SUIT RELEASE`/`EXTRA RELEASE`/`500` · K38 plaket | Büyük harf kuralı tuttu (basılan yazı 'CGI' ya da 'Clip' değil) ama aynı mekanizma küçük harfli tekrarlı sözcükle çalıştı: `release` 132× (K30'da 6×) → `RELEASE` yazısı. Kural 'çok tekrarlanan kısa ayırt edici sözcük'e genişletilmeli. |
| 🅑7 ekran/metin çelişkisi yok | KISMEN — ekran/şema/gösterge içeren **27 klip**; özgül `nothing written … plain geometry` cümlesi **7'sinde** (K21, 26, 48, 51, 62, 72, 74); **20'sinde yok** (K05, 07, 08, 12, 14, 22, 23, 30, 42, 43, 47, 55, 63, 68, 71, 75, 79, 88, 89, 96) | **2** (K30, K38; ikisi de özgül cümlesi olmayan klip) | Özgül cümle taşıyan 7 klipte yazı bulgusu 0 → kural işe yarıyor, ama 20 klipte düşmüş. K22/K23 aynı şemayı K21'den cümlesiz taşıyor. |
| 🅑8 dünya çapası | KISMEN — gezegen cümlesi **47 klipte** (`banded planet … copper wash`); fırtına lekesi yalnız K44 (1/47); bant yönü/açı **0/47** | **12 dünya/ölçek/araç satırı** (🅐 1 · 🅑 6 · 🅒 3 · 🅓 2): bant yönü kayması K06, K32, K43, K52/56, K73–76; araç silueti K31/32 | Gezegen bandı üç PART'ta (⑤ 🟠 ×5) aynı çıkış: 'copper wash' tarifi yönü kilitlemiyor. Kapanma referans paneli (R14) + her dış sahnede aynı dünya cümlesi. |
| 🅑13 ışık saat yönü | HAYIR — `o'clock` **0/92**; dış sahnelerde `from screen left` 47 klip; iç sahnelerde yönsüz tavan ışığı 58 klip | **12 ışık satırı** (3 🔴 · 9 🟠; 🅐 8 · 🅑 1 · 🅑+ 2 · 🅒 1) | Yön 'ekran solu' (kameraya göreli) — kamera değişince dünya yönü değişiyor; kesmelerde 'ana ışık yönü atladı' (⑪) çıktı. Saat yönü yazılmadığı için 🅑13 bu filmde de açık; ama 8/12 satır iki klipte aynı LIGHT yazılıyken çıktı (🅐). |

Ek ölçüm: 🅑+ 13 satır — kök nedenler: `separate halves of the frame` (bölünmüş ekran), 'aynı giysi' cümlesinin kopya çağırması (K37, K58), sayı çelişkisi (K35/K36), dış plana kopyalanan LIGHT/AUDIO (K32, K40, K79), tek makroda altı eldiven (K86), 3-4-3 tempo iskeleti (⑩ ×2), yanlış özneli efor kalıbı (K48), '1g deyimi' (K15/K17).
