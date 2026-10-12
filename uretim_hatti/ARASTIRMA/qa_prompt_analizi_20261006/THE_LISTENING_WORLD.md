# THE_LISTENING_WORLD
KAYNAK: ham rapor 18 dosya (geçerli 11 · mod V 3 [② DEVAMLILIK · ③ SES · ⑤ ARKA_PLAN — SPEC gereği mod V] · GEÇERSİZ 1 [⑬ UYUM — girdi eksik] · KESİK 3 [HIKAYE/ISIK/UYUM_KESIK — ana dosyayla birebir aynı]) · bulgu 27 satır (🔴 15 · 🟠 12)

## OKUMA NOTLARI (bulgu tablosundan önce)
1. **Betiğin eşlemesi bu filmde bir sahne kayık.** `--film` listesi QA_SPEC `GRID: … hook 10,0 s + (n−1) × 10,0 s` satırından ofset 0 / 1-tabanlı çıkarıyor; oysa filmin sahneleri 0-tabanlı (BOLUM `SÜRE:` satırları: S0 = 0-10 s … S15 = 150-160 s). Betik `--sahne THE_LISTENING_WORLD 0` için "-10-0 s", `15` için "140-150 s" basıyor (gerçek 150-160 s). Ayrıca EFOR tablosunda aralığın SON damgasını alıyor (00:10–00:20 → ":20"). Bu dosyadaki S, BOLUM dosyalarının `SÜRE:` satırlarından elle eşlendi; betiğin S sütununa güvenilmedi.
2. **S2 ve S3 (20-40 s) görüntüsü bu repodaki promptlardan çıkmamış görünüyor.** S3 promptu CU (50mm, 0,8 m) el + telemetri tetiği; promptta rampa, gemi, yürüyüş YOK (plan negatifinde bile "no spaceships"). Buna karşılık 11 mercek (KARE 0:32 · DEVAMLILIK · ARKA_PLAN · FIZIK L4 · AKSIYON · EFOR E4 · KADRAJ "rampa tırmanış WS 28mm" · HOOK · OYUNCULUK · HAREKET M4 · YON V4) aynı şeyi görüyor: astronot iniş aracının rampasından gemiye tırmanıyor. S2 promptu A (EWS 24mm, ayakta, hareketsiz); KADRAJ + 6 mercek (DEVAMLILIK · ARKA_PLAN · FIZIK L3 · AKSIYON B2 · EFOR E3 · YON V3) diz çökmüş/cihazı yere koyan astronot, KADRAJ'a göre MS alt açı 40mm (= E kurulumu) görüyor. Bu tarifler `00_HIKAYE_ONAYI` S2 ("gemisine biner") ve `03_SAHNE_SIRALAMASI` gemi sürümüne benziyor; PLAN/BOLUM ise gemisiz. Promptlar 19.09 18:57-18:59, ham raporlar 20.09 22:35+; üretim defteri hâlâ ⬜33 ✅1. S4-S15 promptla örtüşüyor (S10 duruşu dışında). Bu yüzden S2/S3'te ve S3|S4 kesiminde, bulgunun özü promptta olmayan içeriğe bağlıysa hüküm 🅓 yazıldı; hüküm sahibin "bu klipler hangi prompttan üretildi" doğrulamasına bağlı.
3. ⑬ UYUM (prompt ↔ ekran karşılaştıran tek mercek) iki dosyada da "GİRDİ MODU: EKSİK — sahne promptları sağlanmadı" yazıyor: koşmadı. S2/S3 sapması bu yüzden promptla karşılaştırılmadan kaldı.
4. Başlık/afiş kartı ("THE LISTENING WORLD", 2:40-2:45, DEVAMLILIK'ta "SILENCE IS A MESSAGE") promptlarda ve SPEC'te yok; kurguda eklenmiş.

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| S0-S15 | 🔴 | ① KARE (listede yok) | filigran | 🅐 | "no subtitles, no captions, no watermark" (32/32 prompt) | araç ayarı | alt-sağ turkuaz köşe simgesi; yasak her promptta yazılı |
| S0 | 🟠 | ① KARE | parçacık/duman/toz | 🅐 | "no atmosphere, no fog, no haze, no floating particles" | araç ayarı | pus yasağı açıktı; kanyonda yine pus çıktı |
| S0 | 🟠 | ① KARE (kutu satırı; günlükte 🟡) (listede yok) | ışık | 🅒 | "Vacuum environment with perfectly sharp shadows and no atmospheric scatter." | QA | rapor 🟡/🟠 çelişiyor; Ereon/buz yansıması planın dolgusu |
| S1 | 🟠 | ① KARE | ışık | 🅐 | "The surrounding ice faintly captures the internal reflection without bloom." | araç ayarı | bloom iki kez yasak; ışın 2. sn'de, prompt flaşı 7. sn |
| S2 | 🟠 | ① KARE | parçacık/duman/toz | 🅓 | "Pristine vacuum clarity with sharp, ink-black shadows" (diz çökme yok) | QA | S2 görüntüsü prompttan farklı; hüküm verilemez |
| S3 | 🟠 | ① KARE | yerçekimi/süzülme | 🅓 | YOK (promptta rampa/yürüyüş yok; CU el + tetik) | QA | rampa yürüyüşü promptta yok |
| S5 | 🟠 | ① KARE | el-nesne kaynaşması | 🅑+ | görsel: "grips the knurled metal control knob … setting a new cadence"; video: "taps the optical pulse trigger four distinct times" | prompt | görsel kavrar/video dokunur; model çevirdi, eldiven karıştı |
| S6 | 🟠 | ① KARE | diğer | 🅐 | "terrain static, no melting or warping" | araç ayarı | buz duvar dokusu 'nefes aldı'; yasak yazılıydı |
| S8 | 🟠 | ① KARE | el-nesne kaynaşması | 🅐 | "Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers." | kadraj kararı | cümle var; avuç buza basılı, 'two-inch' kabuk |
| S3/S4 | 🔴 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅑 | S0 "off-white and matte grey … burnt-orange research bands"; S2 "white and matte grey"; S3 renk YOK; S4 "crisp white … dark orange stripe" | prompt | giysi cümlesi sahneden sahneye değişiyor; S0-S3 turuncu çıktı |
| S3/S4 | 🟠 | ② DEVAMLILIK | hikâye/anlatım/kurgu | 🅓 | YOK (promptlarda gemiye biniş/rampa yok) | QA | S3 rampa sahnesi promptta yok |
| S3/S4 | 🟠 | ② DEVAMLILIK (listede yok) | arka plan/dünya çapası | 🅓 | S4: lander cümlesi YOK; "research lander … 11 o'clock" yalnız S0/S2/S7 | QA | gemi S3 rampa görüntüsünden geliyor; S3 promptunda gemi yok |
| S0-S15 | 🔴 | ⑤ ARKA PLAN (listede yok) | filigran | 🅐 | "no subtitles, no captions, no watermark" (32/32 prompt) | araç ayarı | TEKRAR: ① KARE ile aynı turkuaz köşe simgesi |
| S1 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | "place a heavy rectangular optical telemetry box"; efor/direnç cümlesi YOK | prompt | 'heavy' var ama eldiven/kol yükü yazılı değil |
| S2 | 🔴 | ⑧ EFOR | efor/beden | 🅓 | YOK (S2 promptunda diz çökme/kadran yok; ayakta durma) | QA | S2 görüntüsü prompttan farklı |
| S3 | 🔴 | ⑧ EFOR | efor/beden | 🅓 | YOK (promptta rampa yok) | QA | rampa tırmanışı promptta yok |
| S5 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | "gloved index finger taps the optical pulse trigger four distinct times"; direnç YOK | prompt | eldiven sertliği/parmak yükü yazılı değil |
| S8 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | "Her thick gloved right hand is pressed flat against the bare crystalline surface" | prompt | oran düşüşü yok; 0,12 g'de QA beklentisi şişkin olabilir |
| S9 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | "does not stand or retreat; her gloved hand remains pressed flat … in deliberate patience" | prompt | BEDEL bedende yazılı değil; prompt çöküş değil sabır istiyor |
| S11 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | "slowly lifts her right hand six inches off the ice surface, fingers slightly curled in wonder" | prompt | 'wonder' duygu; omuz/kol direnci yazılı değil |
| S2 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅓 | "Static locked-off tripod at 1.7 meters height and 12.0 meters distance. Lens 24mm prime." | QA | prompt A'yı doğru yazıyor; görüntü MS/40mm diz çökme |
| S3 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅓 | "Close-up (CU), high-angle looking downward at the equipment on the ice surface" | QA | prompt B/CU; görüntü WS rampa — prompttan üretilmemiş |
| S0/S15 | 🔴 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | S15: "Lens 21mm prime. Extreme wide shot (EWS), high-angle looking down from high orbit" | hikâye/plan | uyak çifti kuralı SPEC'teki H ile çelişiyor; mercek de bunu yazdı |
| S2-S3 | 🟠 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅓 | YOK (aynı S2/S3 sapmasının açı-yayı yansıması) | QA | J1/J2'nin tekrarı |
| S3 | 🟠 | ⑫ HOOK (listede yok) | hikâye/anlatım/kurgu | 🅓 | YOK (promptta iniş aracına yöneliş yok) | QA | rampa hareketi promptta yok |
| S3-S5 | 🔴 | ⑫ HOOK (listede yok) | hikâye/anlatım/kurgu | 🅒 | S4: "For the entire 10 seconds, the ice floor remains inert and dark, offering zero response" | hikâye/plan | S4 TEPKİSİZLİK bilinçli bekleyiş; DÖNÜŞ %50 plan kararı |
| 2:40-2:45 | 🔴 | ⑫ HOOK (listede yok) | istenmeyen yazı | 🅒 | YOK (kart promptlarda yok); SPEC: "SCREEN TEXT: 0,0 saniye" | kurgu-ses | afiş kartı kurguda eklenmiş; üretim hatası değil |

## ÖZET
```
BULGU SATIRI    27  (🔴 15 · 🟠 12)
HÜKÜM           🅐 6 · 🅑 6 · 🅑+ 1 · 🅒 4 · 🅓 10
🅑(+🅑+)/(🅐+🅑+🅑+) = 7/13 = 54%   (🅒 ve 🅓 paydadan çıkarıldı)
TÜR (en sık 5)  efor/beden 7 · kamera/kesme/kadraj 4 · hikâye/anlatım/kurgu 3 · filigran 2 · parçacık/duman/toz 2
TÜR (hepsi)     efor/beden 7 · kamera/kesme/kadraj 4 · hikâye/anlatım/kurgu 3 · filigran 2 · parçacık/duman/toz 2 · ışık 2 · el-nesne kaynaşması 2 · yerçekimi/süzülme 1 · diğer 1 · kask/giysi/ekipman kayması 1 · arka plan/dünya çapası 1 · istenmeyen yazı 1
KAPANMA YERİ    QA 11 · prompt 7 · araç ayarı 5 · hikâye/plan 2 · kadraj kararı 1 · kurgu-ses 1
```

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız)
Okunan sahne: 16/16 (S0-S15, görsel + video). Her madde: sahne · alıntı · neden kusur.

1. **Meta etiket + iki ayrı numaralama.** 32/32 promptta `Scene N of 16.` var (S3 → "Scene 4 of 16.", S15 → "Scene 16 of 16."): etiket 1-tabanlı, ama çapraz atıflar 0-tabanlı. S3 görsel/video: `"Static locked-off tripod at 0.8 meters height and 1.2 meters distance. Lens 50mm prime … the same position, height and lens as Scene 1."` — etiket sayımıyla "Scene 1" S0'dır (24mm · 12 m · EWS); aynı cümlede 50mm/0,8 m yazıyor → promptun kendi içinde çelişki. S12: `"… the same position, height and lens as Scene 10."` ama etiket sayımıyla "Scene 10 of 16" = S9 (E · 40mm MS), S12 ise F (35mm WS). S9 video: `"Scene 10 of 16 … the same position, height and lens as Scene 8."` — etiketle "Scene 8" = S7 (D · 28mm WS). Motor sahne numarasını yazı/atıf olarak okur.
2. **İki başlangıç karesi komutu (S9 ve S14 video).** `"START FRAME: the approved still from this scene's IMAGE prompt — animate it …"` ile aynı promptun gövdesinde `"This video continues the previous clip from its exact last frame — the same position, height and lens as Scene 8."` (S14'te "Scene 13"). Hangi kareden başlanacağı iki kez, farklı söyleniyor.
3. **Şişkin NEGATIVE bloğu.** Görselde 887, videoda 967 karakter (S14: 1025, S15: 465/545), 15/16 sahnede birebir aynı metin; görsel promptların 1773-2055 karakterlik gövdesinin ≈ %45'i. İçinde el olmayan sahnelerde (S0 · S2 · S4 · S6 · S7 · S10 · S12 · S13 · S14: `IN FRAME: full body / face · torso`) `"Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers."` ölü yük.
4. **Kendi kendine çelişen istek: "ten" iste, ten yasakla.** S13 görsel: `"zero face, zero eyes, and zero human skin visible"` ile aynı promptun NEGATIVE'i `"real skin pores and sweat, no airbrushing, no waxy texture, no face morphing"` + `"No bare skin above the collar, at the wrist, or at the ankle."` — vizör %100 opak, ten yasak; aynı negatif blok ten gerektiren her filmden kopyalanmış.
5. **Parlama iste, parlamayı yasakla.** S10 görsel: `"vibrant, intense turquoise bioluminescence … illuminating the bottom fifty meters of the towering icy canyon walls with cool cyan brilliance"`; S11: `"strong turquoise light radiates upward, bathing the white EVA chestplate … in rich cyan light"` — NEGATIVE: `"0% bloom, no glow, no soft focus"`. Işık kaynağı olan filmde "no glow" motora çelişen iki komut verir (KARE 0:12 bloom bulgusu bu kalıbın ailesi).
6. **Yapılamaz/ortama aykırı istek.** S2 video: `"From 2.0 to 8.0 seconds, the golden rings of Ereon cast a subtle, razor-sharp shadow progression across the distant mountain peaks"` — halka gölgesi 6 saniyede dağlarda ilerlemez. S15 (yörünge): `"Static locked-off tripod at 50.0 meters height and 120.0 meters distance"` ve NEGATIVE `"Particles obey the stated gravity of 0.12g"` — yörüngede tripod ve yüzey yerçekimi. S8/S11: `"illuminating the frost patterns on her white suit fabric"` / `"microscopic frost crystals adhering to the seams … in hard vacuum"` — sert vakumda kırağı oluşmaz; aynı prompt vakumu 4 kez vurguluyor.
7. **Motorun gösteremeyeceği soyut/zihinsel ifade.** S13 video: `"a very subtle, microscopic nod of comprehension at 5.0 seconds, the motion controlled and solemn"`; S11 video: `"Her helmet tilts slightly upward, acknowledging the vast scale of the living moon"`; S9 görsel: `"holding the astronaut in cold suspended silence"`; S5 görsel: `"setting a new cadence"`; S11 görsel: `"fingers slightly curled in wonder"`.
8. **Görsel ↔ video çelişkisi (S5).** Görsel: `"grips the knurled metal control knob of the optical transmitter"`; video: `"gloved index finger taps the optical pulse trigger four distinct times"`. Başlangıç karesi (görsel) kavrama/çevirme, video dokunma istiyor → KARE 0:54 eldiven-düğme kaynaşması bulgusunun yanındaki komut.
9. **Yazı daveti (S5).** Görsel: `"Her thick insulated spacesuit sleeve displays the mission insignia patch on the forearm"` — NEGATIVE `"No readable text, letters, digits or symbols on any … patch"`; amblem yaması harf/simge istemekle aynı şey.
10. **Buz kalınlığı tutarsız.** S0 `"two meters of transparent methane ice"`, S1 `"channels resting three centimeters below the surface"`, S3/S7 `"two meters deep"`, S8 `"Beneath the two-inch surface crust"` — 2 m / 3 cm / 5 cm. Işık kanalının eldivene 5 cm kaldığı bir sahnede el-buz kaynaşması davet edilmiş olur (KARE 1:24).
11. **Gezegen evresi ve cinsiyet tutarsız.** Ereon: S0 `"dominating the black sky"`, S2 `"towering golden crescent"`, S4 `"immense curved arch of Ereon's rings"`, S7 `"massive curved disk sits low on the horizon"`. Özne: PLAN "kadın veya erkek ayırt edilmez", ama 34 kez `her`/`she` ("her gloved hand"); SES raporu "Hello." için erkek ses duydu.

## 19.09 KURALLARI BU FİLMDE
```
kural                         yazılı mı (16 sahne)                                         yine de bulgu
🅑1 ses yasası                AUDIO: satırı 0/16 · "no exterior sound" tipi yasa 0/16;     0 bulgu (⚠ SES mercek mod V:
                              "silence" geçen video promptu 3 (S4 · S9 · S15)               S1-S4 ambiyansında "wind hum / icy wind" duyulmuş,
                                                                                            vakumda rüzgâr — 🔴/🟠 yazılmadı)
🅑2 el-yüzey teması           15/16 (S15 insansız hariç), görsel + video                    2 (S5 🅑+ · S8 🅐)
🅑2a nesne-nesne teması        0/16                                                          0 (kutu-buz / eldiven-düğme "hand-to-surface" ile örtülü)
🅑3 giysi birebir             genel "identical throughout" 15/16; Bible giysi cümlesi      1 🔴 (S3|S4 turuncu → beyaz)
                              birebir 0/15 (S0 · S2 · S3 · S4 · S6 · S7 hepsi farklı)
🅑4 ortam adı + sayısı        "vacuum" video 16/16 · "0.12g" NEGATIVE 16/16                 3 (S0 pus 🅐 · S2 asılı parçacık 🅓 · S3 süzülen adım 🅓)
🅑5 efor oranı                0/16 (oran düşüşü cümlesi yok)                                7 🔴 EFOR (S1 · S5 · S8 · S9 · S11 🅑; S2 · S3 🅓)
🅑6 büyük harfli jeton yok    HAYIR: "EVA" 10 görsel promptta + 2 videoda · "LED" S9 ·     0 içerik yazısı bulgusu; 2 filigran simgesi 🅐, 1 kart 🅒
                              "KONUM:" 32/32 · "Scene N of 16." 32/32 · CAMERA/IN FRAME
🅑7 ekran/metin çelişkisi     okunacak ekran yok; S5 "mission insignia patch" + yazı yasağı 0
🅑8 dünya çapası              lander 11 o'clock yalnız S0 · S2 · S7 (3/16); S15 2 o'clock   1 🟠 (S3|S4 gemi kayboldu, 🅓) + ARKA_PLAN 🟡 gezegen konumu
🅑13 ışık saat yönü           0/16 (o'clock yalnız araç konumu için)                       0 (⑪ IŞIK'ta 🔴/🟠 yok; "GRADEABLE DRIFT" 🟡)
```
Not: film promptları 19.09 18:57'de yazıldı (sınıf belgesinin anlık görüntüsü 19.09 14:24); ham raporlar 20.09 22:35+. Ölçüm: 🅑1 (AUDIO/ses yasası), 🅑5 (efor oranı), 🅑13 (ışık saat yönü) ve nesne-nesne teması bu filmin hiçbir sahnesinde yazılı değil (0/16); 🅑2 ve 🅑4 yazılı olduğu hâlde 2 + 3 bulgu çıktı.
