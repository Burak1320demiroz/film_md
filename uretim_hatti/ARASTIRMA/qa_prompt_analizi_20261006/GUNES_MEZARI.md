# GUNES_MEZARI
KAYNAK: ham rapor 15 (tool: geçerli 15 · bunların içinde SPEC'li mod D 0 · mod V/GEÇERSİZ 14 · KESİK/giriş-eksik 1 [⑬ UYUM, 0 bulgu]) · bulgu 43 (🔴 16 · 🟠 27)

> **Nasıl sayıldı.** `--film` listesi 25 satır verdi → aynı bulgunun TOP-3 ve ayrıntı günlüğünde tekrarı (S02 ses ×2, S07 buhar ×2, S13 kask ×4 ifade) birleştirilince 21 tekil.
> Listede OLMAYAN 22 bulgu elle eklendi (② DEVAMLILIK 2 · ③ SES 1 · ⑤ ARKA PLAN filigran 1 · ⑨ KADRAJ 4 · ⑩ OYUNCULUK 10 · ⑪ IŞIK 4); `--film` bunları ayrıştıramadı.
> Çok sahneli satırlar sahne başına ayrı sayıldı. Yalnız 🔴/🟠 ikonu taşıyan bulgular sayıldı; ikonsuz (yalnız skor) gözlemler en altta ayrı.
> **S = klip numarası** (K01-K24, 10 s ızgara; K01 0:00'da). Prompt metni = bölüm dosyalarındaki metin; ÜRETİM DEFTERİ BOŞ (as-built kaydı yok), gönderilen metnin dosyayla aynı olduğu varsayıldı.

> ⛔ **Üç yöntem uyarısı.**
> (1) 15 raporun hepsi `SPEC BLOCK PROVIDED: no` / `FILM: (not supplied)` — `GUNES_MEZARI_QA_SPEC.md` yazılı olduğu halde verilmedi. Sonuç: mercek 0,90 bar kriyojenik atmosferi **vakum** ve "Ay yüzeyi" sandı; 4 satır (S02 ses · S05 toz · S07 buhar · S21 yerçekimi) yalnız bu yüzden 🅒.
> (2) Mercek zaman damgaları 2:10'dan sonra güvenilmez: videoda K14'ün içinde 2:16'da bir kesme var ve ⑦ ⑧ ⑨ ⑩ raporlarının zamanları 2:10 sonrası içerikten ±10 s kayıyor. Her satırda içeriği klibin promptuyla karşılaştırıp S'yi içerik doğrulamalı yazdım; `--film`'in S'sinden farklı olanlar aşağıdaki tabloda.
> (3) 2:00-2:10 aralığındaki kask kaybı ve 2:16 klip içi kesme, mercekler arasında en tutarlı görülen iki gerçek kusur; 16 🔴'nin 7'si 🅒/🅓.

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| S01 | 🟠 | ① KARE | ışık | 🅐 | IMAGE `no corona, no rays and no halo around it` · NEG `0% bloom, no glow, no soft focus` | araç ayarı | bloom 24/24 promptta yazılı; yine çıktı |
| S02 | 🔴 | ① KARE | ortama aykırı ses | 🅒 | AUDIO `The cold dense air carries low frequencies close and strong and kills the highs.` | QA | mod V; mercek 0,90 bar atmosferi vakum sandı |
| S02 | 🟠 | ① KARE | arka plan/dünya çapası | 🅑 | YOK — insansız klibin kısaltılmış NEGATIVE'inde `terrain static, no melting or warping` yok | prompt | bilinçli kısaltma (ret defteri #2) şehir geometrisini kilitsiz bıraktı |
| S02 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | `fixed lockoff — absolutely zero camera movement. In a single continuous shot.` | araç ayarı | gövde kadrajı geçiyor; model takibe kaymış |
| S03 | 🟠 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `her shoulders rise once with a slow breath and ease`; yüz kası eylemi yok | QA | tepki kanalı omuz+kask; yüz kanalı tasarımda yok |
| S03 | 🟠 | ⑪ IŞIK | ışık | 🅐 | K02 LIGHT `the only source is the caged sphere below the deck, a deep red-gold coming up from underneath` | araç ayarı | K02 serin üst anahtar ışığı almış (K02→K03) |
| S04 | 🟠 | ⑤ ARKA PLAN | arka plan/dünya çapası | 🅑 | `one shattered moon low over the rooftops, its ring a thin arc` | prompt | ekran tarafı ve boyut yok; model halkalı dev gezegen çizdi |
| S05 | 🟠 | ① KARE | parçacık/duman/toz | 🅒 | VIDEO `the frost lifted by her boots settles within half a second` | QA | vakum balistiği beklendi; dünya 0,90 bar |
| S05 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | aynı CAMERA cümlesi · NEG `no camera resets, no angle change` | araç ayarı | yürüyen özne kamerayı çekmiş |
| S05 | 🔴 | ⑩ OYUNCULUK | oyunculuk | 🅑+ | `She keeps the same walking cadence for the whole clip, three steps every two seconds` | prompt | prompt sabit hızı bizzat istiyor; plan TEMPO K05=N |
| S06 | 🟠 | ⑧ EFOR | efor/beden | 🅑 | `she resets her boots without stepping back and leans in again` — hız düşüşü sayısı YOK | prompt | sırttan çekimde vizör buğusu zaten görünemez |
| S07 | 🔴 | ① KARE | parçacık/duman/toz | 🅒 | IMAGE `A thin upright vapour collar stands a hand's height off the lip of the hollow and does not lean.` | QA | vakum varsayımı; sıcak oyuk buharı SPEC'te tasarım |
| S08 | 🔴 | ⑩ OYUNCULUK | oyunculuk | 🅑 | `the fingers press once and ease`; eldiven t=0'da duvarda, ön duraksama YOK | prompt | 'already flat' kalıbı temas öncesi tereddüdü yazdırmıyor |
| S09 | 🟠 | ① KARE | ışık | 🅑+ | IMAGE `Her lamp lies on the ground at screen left` ↔ LIGHT `her own lamp at chest height` | prompt | aynı promptta lambanın iki çelişen konumu |
| S10 | 🟠 | ③ SES | ses-görüntü uyumu | 🅒 | K03 ve K10 aynı satır: `There are children here. Please give the light back.` | QA | SPEC: aynı kayıt iki kez duyulur, tasarım |
| S10 | 🔴 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `she is still standing a step inside the door` | QA | K10 durağan (Y); mercek yürüyüş temposu okudu |
| S12 | 🟠 | ① KARE | yüz/kimlik | 🅐 | NEG `real skin pores and sweat, no airbrushing, no waxy texture, no face morphing` | araç ayarı | prompt açıkça önlüyor |
| S12 | 🟠 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `her brows draw together and her jaw sets` | QA | CHOICE çapası K16; mercek tahminle S12'yi seçti |
| S13 | 🔴 | ① KARE | kask/giysi/ekipman kayması | 🅑 | YOK — `IN FRAME: hands · torso`; yalnız NEG `No bare skin anywhere — none above the collar` | prompt | video promptlarının 11/18'inde kask adı yok |
| S13 | 🟠 | ① KARE | efor/beden | 🅐 | `she halts holding the strain, then leans her weight in again` | araç ayarı | tasarlanan duraksama 'sert hareket' diye okunmuş olabilir |
| S13 | 🔴 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅑 | YOK — aynı kök: K12'de vizör cümlesi var, K13'te yok | prompt | kask kayboldu, saç ve baş şekli de değişti |
| S13 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | `the lever gives a hand's width and grips; she halts holding the strain` — oran sayısı, nefes YOK | prompt | duraksama var, hız düşüşü sayısı ve soluk yok |
| S14 | 🟠 | ② DEVAMLILIK | kamera/kesme/kadraj | 🅐 | VIDEO NEG `Single unbroken take, no cuts, no dissolves, no camera resets, no angle change.` | araç ayarı | 2:16'da klip içi kesme; KARE ve FİZİK de saydı |
| S14 | 🟠 | ⑩ OYUNCULUK | efor/beden | 🅑 | K14 `IN FRAME: hands`; K13'ten devreden efor cümlesi YOK | kadraj kararı | eller yakın planında omuz ve nefes görünmez |
| S15 | 🟠 | ① KARE | ses-görüntü uyumu | 🅓 | K15 AUDIO `No dialogue. No music.` | QA | 2:24'te replik yok; 0:24 ise K03 ve 🅒 |
| S15 | 🟠 | ⑪ IŞIK | ışık | 🅒 | SPEC: `K14|K15` ilan edilmiş sahne sınırı; K15 LIGHT iç lambalar + ızgaradan kızıl-altın | QA | mod V; ilan edilmiş sahne geçişi (K14→K15) |
| S16 | 🟠 | ① KARE | kamera/kesme/kadraj | 🅐 | `fixed lockoff — absolutely zero camera movement` · NEG `no camera resets, no angle change` | araç ayarı | prompt iki cümleyle önlüyor |
| S16 | 🟠 | ⑭ HAREKET | oyunculuk | 🅐 | `the open hand stays at the lever's height through the last second and does not close again` | araç ayarı | K16 merkezî seçim; dört mercek eli kolda gördü |
| S17 | 🟠 | ① KARE | efor/beden | 🅐 | `her grip locks and the first ring stops for half a second, then gives` | araç ayarı | kütle ve duraksama cümlesi promptta var |
| S17 | 🟠 | ① KARE | efor/beden | 🅐 | `both boots braced against the frame of its open bed` | araç ayarı | temas cümlesi yalnız el içindir; bot-zemin kapsamsız |
| S17 | 🔴 | ⑧ EFOR | efor/beden | 🅐 | `her weight low and back` · `her chest is rising and falling hard` | araç ayarı | mercek 2:50 yazdı; içerik K17 (araç S18 dedi) |
| S17 | 🟠 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `her chest is rising and falling hard` | QA | FINAL çapası K23; mercek S18'i seçti |
| S17 | 🟠 | ⑪ IŞIK | ışık | 🅐 | K17 LIGHT `the ship's own interior lamps and a dull red-gold coming up through the deck grating` | araç ayarı | K16→K17 aynı sahne; model soğuk tavan ışığı kurmuş |
| S18 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | `fixed lockoff — absolutely zero camera movement` | araç ayarı | mercek 3:02 yazdı; içerik K18 kayış |
| S18 | 🔴 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `a hand's width of strap comes through her glove at one steady rate` | QA | K18 görev (G) klibi; mekanik olması tasarım |
| S20 | 🟠 | ⑧ EFOR | efor/beden | 🅑 | `She drives the key bar home and turns it a quarter with her shoulder` | prompt | oran düşüşü, nefes ve toparlanma cümlesi yok |
| S20 | 🔴 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `stops a hand's width short; then it goes back onto the bar` | QA | tereddüt promptta yazılı; HAREKET aynı anı gördü |
| S20 | 🟠 | ⑩ OYUNCULUK | oyunculuk | 🅒 | `turns the bar a quarter with her shoulder, the lock closes over it` | QA | FINAL çapası K23; mercek S20'yi seçti |
| S20 | 🟠 | ⑭ HAREKET | oyunculuk | 🅒 | `her left glove lifts toward the lock face, straightens, and stops a hand's width short` | QA | alışkanlık kırılması (K20) 'phantom' okunmuş |
| S21 | 🔴 | ⑥ FİZİK | yerçekimi/süzülme | 🅒 | K21 `the sphere lifts clear at one steady rate` · K06 `reach the step in about a second` | QA | küre g ölçümü SPEC ④ duvarı; yükseliş düşüş okunmuş |
| S22 | 🟠 | ⑪ IŞIK | ışık | 🅒 | SPEC: `THE RISE IS A DECLARED EVENT`; K22 LIGHT `one hard low source high over the city` | QA | K21→K22 ilan edilmiş ışık artışı |
| S23 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅓 | K23 `Both her gloves are open and empty at her sides` — kızak yok | QA | içerik K23'e uymuyor; lockoff 24/24 yazılı |
| S* | 🟠 | ⑤ ARKA PLAN | filigran | 🅐 | `Output: 16:9, no text, no watermark.` (48/48 promptta) | araç ayarı | sağ alt turkuaz oynat ikonu; yalnız ARKA PLAN gördü |

### `--film` S numarası ↔ benim S (içerik doğrulamalı)
| bulgu | `--film` S | benim S | neden |
|---|---|---|---|
| ⑧ E4 "ribbed cylinder kaldırma" 2:50-2:59 | S18 | S17 | çekirdeğin yataktan çıkarılması = K17; mercek 8 +10 s |
| ⑨ lockoff "kızak kayışı" 03:02 | S19 | S18 | kayış tutan el = K18 (profil yakın plan) |
| ⑭ M22 PHANTOM 03:04 · ⑩ final 03:04 · ⑩ eller 03:02 · ⑧ E6 3:06-3:13 | S19/S20 | S20 | "metal bar/kilit çubuğu" = anahtar çubuğu K20 |
| ⑥ L6 ↔ L21 yerçekimi (0:54 ↔ 3:14) | S20 | S21 (+K06) | "küre düşüşü" = K21; öbür ucu K06 |
| ⑪ 2:30 "fener→kargo" | S16 | S15 | K14→K15 (ilan edilmiş sahne sınırı) |
| ⑪ 2:50 "kokpit→kargo" | S18 | S17 | K16→K17 |
| ⑪ 0:20 "dış→kokpit" | S03 | S03 (K02→K03) | |
| ⑩ final 02:46 | S17 | S17 | |

## ÖZET
```
BULGU          43  (🔴 16 · 🟠 27)
HÜKÜM          🅐 15 · 🅑 9 · 🅑+ 2 · 🅒 15 · 🅓 2
               prompt kaynaklı (🅑 + 🅑+) = 11/43 = %26  ·  önlenebilirlik (🅑+🅑+)/(🅐+🅑+🅑+) = 11/26 = %42
               QA/eşleme kaynaklı (🅒 + 🅓) = 17/43 = %40
TÜR (en sık 5) oyunculuk 11 · efor/beden 8 · ışık 6 · kamera/kesme/kadraj 6 · arka plan/dünya çapası 2
TÜR (hepsi)    oyunculuk 11 · efor/beden 8 · ışık 6 · kamera/kesme/kadraj 6 · arka plan/dünya çapası 2 · parçacık/duman/toz 2 · ses-görüntü uyumu 2 · kask/giysi/ekipman kayması 2 · ortama aykırı ses 1 · yüz/kimlik 1 · yerçekimi/süzülme 1 · filigran 1
KAPANMA        QA 17 · araç ayarı 15 · prompt 10 · kadraj kararı 1
```

Okuma: 43 bulgunun **%40'ı QA/eşleme kaynaklı** (🅒 15 + 🅓 2 — SPEC'siz mod V ve tahminle konmuş çapalar), **%26'sı promptta önlenebilirdi** (🅑 9 + 🅑+ 2), **%35'i** prompt doğru yazılmışken model tutmadı (🅐 15). 🔴'lerin dağılımı: 🅒 6 · 🅑 4 · 🅐 4 · 🅑+ 1 · 🅓 1.
**Gerçekten promptla kapanan** satırlar yalnızca 11: K13 kask (2 satır) · K09 lamba çelişkisi · K04 gök/ay tarafı · K02 kısaltılmış NEGATIVE · efor ×4 (K06 K13 K20 + K14 devir) · K08 temas öncesi · K05 sabit kadans.
**Prompt cilasıyla kapanmayacaklar** (🅐 15): kamera sürüklenmesi 4 + klip içi kesme 1 · efor ×4 (K17 ×3, K13) · K16 bırakma · bloom · cilt · filigran · ışık ×2 — kapanma yeri araç ayarı/yeniden üretim.

## HÜKÜM GEREKÇELERİ (yalnız tartışılabilir olanlar)
- **🅒 vakum varsayımı (S02 ses · S05 toz · S07 buhar):** SPEC §C ATMOSFER = `dense cryogenic atmosphere, 0.90 bar, 95 K … lifted frost settles within 0.5 s`; OYUK = `a thin upright vapour collar`. Üç prompt da bunu yazıyor (PHYSICS 24/24, AUDIO `cold dense air carries low frequencies` 24/24). Mercek `deep space vacuum` yazdı. S05'te "2B sis" görüldüyse (frost 0,5 s'de oturmadıysa) bu ayrıca 🅐 olur — videoyu görmeden ayıramadım.
- **🅒 S21 FİZİK 🔴 "iki yerçekimi":** 2,4× farkın bir ucu küre (SPEC ④: `Küre DIŞINDA hiçbir şey havada durmaz. "Two gravities" hükmü ancak küre DIŞINDAKİ bir nesne için yazılabilir`). Mercek 6 küreyi "düşüyor" okudu; ⑩ ve ⑨ aynı anı "yukarı yükseliyor" okudu. Öbür uç K06 enkaz: prompt `reach the step in about a second` (0,38 g'de 1 m = 0,73 s) — mercek 0,5 m/0,6 s ölçtü, ölçüm hatası içinde.
- **🅒 ⑩ OYUNCULUK çapaları:** mod V mercek çapaları tahminle koydu: CHOICE=S12, COST=S13, FINAL=S18. Plan: CHOICE=K16, COST=K17, FINAL=K23. S12/S17/S20 "final/seçim zayıf" satırları bu yüzden 🅒. K20'deki `stops a hand's width short` PLAN §ALIŞKANLIK "KIRILMA K20" — ⑩ "tereddüt yok" dedi, ⑭ aynı anı "PHANTOM GRAB" diye 🟠 yazdı: iki mercek aynı tasarım jestine zıt hüküm verdi.
- **🅒 S10 ses kopyası:** PLAN REPLİK TABLOSU `aynı kayıt` (K03 24,0 s · K10 90,0 s); SPEC `RECORDED HUMAN 2 (the same sentence twice)`.
- **🅒 ışık geçişleri K14→K15 ve K21→K22:** SPEC `SCENE BOUNDARIES: … K14|K15 … K21|K22` ve `IŞIK TAKVİMİ … THE RISE IS A DECLARED EVENT`.
- **🅓 S15 (2:24 dudak):** tek replik zamanı 0:24 ve 1:31; 2:24'te replik yok. 0:24 (K03) kastedildiyse 🅒: prompt `no one speaks on camera`, SPEC ⑥ "kadrajda konuşan ağız 0 klip".
- **🅓 S23 (3:41 kamera):** mercek "kızak çeken astronot" yazdı; K23'te kızak yok, eller açık ve boş. Aynı anı 4 mercek 4 farklı şey olarak anlatıyor (çekirdeği kapağa oturtma · fenerle yürüme · duvara el · kızak çekme) → o aralıktaki içerik bu merceklerde güvenilmez.
- **🅑 S13 kask:** K13 `IN FRAME: hands · torso` + 35 mm/2,2 m/yüksek açı orta plan; kask/vizör hiçbir cümlede yok. NEG'deki `none above the collar` olumsuzlama, kask adı değil. Ayrıca ⑨ mercek K13'ü "WS / alçak açı / geniş" gördü (prompt: MS / yüksek açı) — kadraj da prompttan sapmış; çıplak baş geniş kadrajın sonucu.
- **🅑+ K09 ışık:** çelişki promptun kendi içinde — bkz. "Kusurlar" madde 3.

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız; 24 klibin 48 promptu okundu)
1. **Meta etiket — K01-K24, 48/48 prompt:** her IMAGE ve VIDEO promptun ikinci satırı `Clip 7 of 24.` (video: `Clip 7 of 24. Duration 10 seconds.`). Model bunu sahne dışı etiket olarak okuyabilir; `Scene n of N` sınıfının aynısı (🅑6). Ölçümde yazıya basılma çıkmadı (0), ama kapı dışında.
2. **Başka klibe atıf — 11/24:** K03 `— the same position, height and lens as Clip 1.`, K04 → Clip 2, K07 → Clip 5, K11 → Clip 9, K12 → Clip 8, K13 → Clip 11, K14 → Clip 12, K17 → Clip 15, K18 → Clip 16, K19 → Clip 17, K24 → Clip 22. Neden kusur: her klip kendi görselinden üretiliyor (zincir kalktı), model "Clip 5"i hiç görmez; aynı satırda sayılar zaten yazılı (öbür atıf gereksiz gürültü). Numaralama tutarlı (BRITTLE_EDGE'deki gibi kaymış değil).
3. **K09 kendi içinde çelişki:** IMAGE gövdesi `Her lamp lies on the ground at screen left with its face up, throwing one hard cone across the wall.` — LIGHT satırı (S02'den kopya) `her own lamp at chest height and one shattered moon`. Aynı kaynak hem yerde hem göğüs hizasında. → ① KARE "duvardaki kaynaksız turuncu ışık" (🟠) 🅑+. K13/K14 LIGHT'ı `her own lamp set down on the stone` diye düzeltilmiş; K09'da düzeltilmemiş.
4. **Işık kaynağı nesnesiz — K05, K06, K08:** LIGHT `her own lamp at chest height …` ama gövdede fener yok (K05 `IN FRAME: full body · legs`, K06 sırt görünümü, K08 yalnız el). Model kaynağı uydurur; NEG `no glow` ile birlikte okununca fener ya görünmez ya parlak çizilir.
5. **Yetim PHYSICS cümlesi — K03, K18, K19, K20:** `The sphere is clamped at the focus of three rings and moves with the hull as one body.` küre kadrajda olmayan klipte (kokpit yüzü · kayış eli · çekirdek oturtma · anahtar çubuğu). Küre cümlesi 10/24 videoda (K01-K03 ve K18-K21 `clamped…`; K22-K24 `The sphere is held by the stone cradle high above the city.`); K19/K20 el-yakın planında olmayan bir nesneyi çağırıyor.
6. **Kask 24/24 değil:** SPEC §C `KASK worn and sealed in 24/24` diyor; insanlı 18 klibin video promptunda `helmet|visor|pane` yalnız 7'sinde (K03 K09 K10 K12 K15 K16 K23), `The visor is one flat clear pane…` cümlesi 6'sında. K05 K06 K07 K08 K13 K14 K17 K18 K19 K20 K22 kasksız yazılı (D214 `IN FRAME` kırpması başı da attı). Gerçek sonuç: K13 🔴.
7. **Viral yüz kuyruğu prompta inmemiş — K17:** başlık satırı `⭐VİRAL · YÜZ: brows draw together and stay, shoulders lift with each breath, 546 px` kod bloğunun DIŞINDA; K17 video gövdesinde `brow` yok (K12'de var). COST çapasının yüz kanalı gönderilen metinde yok.
8. **IMAGE promptlarında video kavramı:** `Nothing changes shape, melts or warps, and the only change is the stated one.` 9 IMAGE promptta (K06 K10 K11 K13 K17 K19 K20 K21 K24) — duran kareye "değişim" cümlesi. K03/K10 IMAGE'inde `The spoken line is heard only and is never shown as text` — ses cümlesi still'e girmiş.
9. **NEGATIVE şişkinliği:** insanlı 18 klipte VIDEO NEGATIVE 1195-1307 karakter (183-219 kelime; toplam prompt 450-505 kelime → NEG ≈ %42; K03 1297 · K12/K16 1307), IMAGE 1044-1227 karakter; insansız altı klipte 508-603 karakter. ⚠️ İnsansız kısaltma bilinçli (ret defteri #2) ama K02'de `terrain static` kilidini de götürdü (🅑, S02).
10. **K24 insansız klipte soluk:** AUDIO `One slow breath off frame` — `IN FRAME: none` ve NEG'de insan sayısı cümlesi yok; "kadraj dışı soluk" figür çağırabilir (ölçümde çıkmadı).

## 19.09 KURALLARI BU FİLMDE
| kural | yazılı mı (kaç klipte) | yine de bulgu çıktı mı |
|---|---|---|
| 🅑1 ses yasası | AUDIO `The cold dense air carries low frequencies close and strong and kills the highs.` 24/24 VIDEO (ortam adı + neyi taşıdığı). (`--kilit` "dış-ses 0/24" vakum denetimi — bu ortamda geçersiz.) | 1 🔴 (S02 gürleme) — 🅒, vakum varsayımı |
| 🅑2/2a temas (nesne-nesne dahil) | el-yüzey cümlesi 18/18 insanlı klip; nesne-nesne cümlesi 0/24 | 0 füzyon bulgusu (tek 🟡: 1:14 parmak kayması). Nesne-nesne temasları (K14 fener↔yuva · K19 çekirdek↔yuva · K20 çubuk↔kilit) 0 bulgu |
| 🅑3 giysi birebir | `Equipment and clothing identical throughout` 18/18; **kask/vizör cümlesi 7/18** | 2 satır (K13 kask: ① 🔴 + ② 🔴) — ikisi 🅑 |
| 🅑4 ortam sayısı + adı | VIDEO `Gravity is 0.38 g in a dense cryogenic atmosphere at 0.90 bar and 95 kelvin` 24/24; IMAGE 0/24 | yerçekimi/ortam 🅐🅑 bulgusu 0; yalnız 🅒 ×4 (vakum varsayımı + küre ölçümü) |
| 🅑5 efor oranı | nitel efor cümlesi 6/6 efor klibinde (K06 K13 K17 K18 K19 K20); **sayılı oran düşüşü 0/6** | 8 satır (⑧ 4 · ① K13 sert hareket · ① K17 ×2 · ⑩ K14 devir): 🅑 4 · 🅐 4 |
| 🅑6 büyük harfli jeton | `S07`/`PHASE`/`EVA` 0/48; ama `Clip n of 24` 48/48 ve alan etiketleri (IN FRAME · LIGHT · CAMERA · NEGATIVE · PHYSICS · AUDIO · TIMELINE · START FRAME · CONTINUOUS ACTION · `IMAGE` 24/24 videoda) | yazıya basılma 0. ("TOMB OF THE SUN" kartı kurgu eki, prompt dışı) |
| 🅑7 ekran/metin çelişkisi | K11 `archive plate … lit from within` + `No readable text … on any display` — içerik metinsiz (eldiven+kol resmi) → çelişki yok | 0 |
| 🅑8 dünya çapası | üç cümle (gök · ufuk · yer imi) birebir **2/24** (K04, K21); `shattered moon` 9/24; ufuk cümlesi 6/24 | 1 🟠 (K04 gezegen sağdan sola) — 🅑 |
| 🅑13 ışık saat yönü | `o'clock` 0/24 (tasarım: ışık KAYNAKLA kilitli, SPEC duvarı ②) | "key walks" 0; ışık satırları 6: 🅐 3 (K01 bloom + 2 geçiş) · 🅒 2 · 🅑+ 1 (K09 lamba) |

⭐ 19.09 kurallarının SEÇMELİ uygulanması bu filmde de görüldü: ses (24/24) ve ortam sayısı+adı (24/24) tam yazıldı ve **sıfır** 🅐/🅑 bulgu çıkardı; kask/vizör (7/18), dünya çapası (2/24), efor oranı (0/6) ve K09'un ışık satırı eksik/çelişik yazıldı — prompt kaynaklı 11 bulgunun 8'i bu dört eksikten (kask 2 · efor oranı 4 · dünya çapası 1 · K09 ışık 1).

## SAYIMA GİRMEYEN (ikonsuz, yalnız skor) — hüküm yine yazıldı
| mercek | gözlem | hüküm | not |
|---|---|---|---|
| ⑨ KADRAJ | Rhyme pair S1 ↔ S24 kırık (2/10): "CU alçak açı küre ↔ EWS şehir" | 🅒 | K01 ve K24'ün CAMERA cümlesi aynı (`35mm … 2.2 m … 1.60 m, high angle fifteen degrees, medium shot`); ⑥ ve ⑫ son klipte "filiz yakın plan" gördü, ⑨'un S24 okuması tek başına |
| ⑤ ARKA PLAN | 01:48-02:44 "56 s siyah ekran" | 🅓 | öbür 14 rapor aynı aralıkta içerik anlattı |
| ⑪ IŞIK | S7/S8 "vakumda gölge yumuşaması" (3. en önemli) | 🅒 | vakum varsayımı; SPEC: gölge sert, dolgu zayıf (0,90 bar, pus yok) |
| ⑫ HOOK | "bitiş kartta kesiliyor, döngü yok" | 🅒 | SPEC `title card: NONE`; kart sahibin kurgu eki (K01↔K24 döngüsü içerikte var) |
