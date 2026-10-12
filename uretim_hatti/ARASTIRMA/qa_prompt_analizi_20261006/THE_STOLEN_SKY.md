# THE_STOLEN_SKY
KAYNAK: ham rapor 60 (geçerli 12 · mod V/TEKRAR/GEÇERSİZ 44 · KESİK 4) · bulgu 192 (🔴 98 · 🟠 94)

```
EŞLEME (elle yapıldı — `prompt_hata_analizi.py --film` bu filmde 0 bulgu veriyor: ham raporlar alt klasörde, glob inmiyor)
  QA_SPEC PART GRID: PART 1 = S00-S23 (0-240 s) · PART 2 = S24-S47 · PART 3 = S48-S71 · PART 4 = S72-S95; her PART 24 klip × 10,000 s (doğrulandı).
  klip = PART başı + ⌊t/10⌋. Raporlardaki "S n"/"Scene n" parça-içi 1-tabanlı (V numarası): S = PART başı + n − 1. `--sahne THE_STOLEN_SKY <n>` çalışıyor (0-tabanlı S).
  60 rapor = 4 PART × 15 mercek. Hepsi mod V ("FILM: (not supplied)", "SPEC BLOCK PROVIDED: no"), ⑬ 4/4 INPUT MODE: MISSING = KESİK.
  rapor_kontrol kararı: GO/ŞARTLI = ② ③ ⑤ ×4 = 12 · TEKRAR (SPEC var, mod V) = ① ④ ⑥ ⑦ ⑧ ⑭ ⑮ ×4 = 28 · GEÇERSİZ = ⑨ ⑩ ⑪ ⑫ ×4 = 16 · KESİK = ⑬ ×4.
  Süre-kesik not (00_INDEX): ⑤ P1 150 s · ⑩ P3 100 s · ⑦ P2 187 s — rapor_kontrol bunları ŞARTLI/TEKRAR saydı, burada da öyle.
  Ham satır: 144 🔴 + 147 🟠 (extract.py, dosyalardaki sayıyla birebir) → tekilleştirme (aynı klip + aynı kusur; TOP3/log/kutu/skor tekrarları, ③'ün 23 ambiyans satırı tek satır) → 98 🔴 + 94 🟠.
  Atlanan 🟠: 9 (toplu kategori satırı: ⑩ P2 ×3 · ⑩ P3 ×3 · ⑪ P1 renk sıcaklığı · ⑪ P3 poz · ⑦ P3 tempo). Bütün 🔴'ler işlendi.
  ⚠️ İÇERİK↔IZGARA KAYMASI: üç çiftte QA'nın anlattığı içerik zaman ızgarasının tersi: S19↔S20 (03:10 = S20 içeriği) · S49↔S50 (00:10 = S50 içeriği) · S59↔S60 (01:50 = S60 içeriği).
     Bu satırlar İÇERİK çapasıyla yazıldı, S sütununda "(ızgara Sxx)" var. Master'da sıra ters ya da QA zaman kodu kaymış; filmi bilmeden doğrulanamaz.
  Mercek simgeleri: ① KARE ② DEVAMLILIK ③ SES ⑤ ARKA PLAN ⑥ FİZİK ⑦ AKSİYON ⑧ EFOR ⑨ KADRAJ ⑩ OYUNCULUK ⑪ IŞIK ⑫ HOOK ⑭ HAREKET ⑮ YÖN; "×k" = k mercek aynı kusuru yazdı.
```

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| S00 | 🔴 | ① | zemine geçme | 🅑 | YOK — yalnız "The thrown ship stays one rigid piece, no bending hull" | prompt | Gemi–kule nesne-nesne teması yazılı değil (🅑2a) |
| S00 | 🔴 | ①+⑥ ×2 | parçacık/duman/toz | 🅐 | "sparks and plate fragments fall straight down at 0.9 g" | araç ayarı | Enkaz 1,56 m/s²; S22 ile iki yerçekimi |
| S00 | 🔴 | ⑪ (listede yok) | ışık | 🅒 | "Gravity is 0.9 g under one atmosphere of breathable-density air; … haze rises and thins" | QA | Mercek vakum sanmış; S00/S01/S03/S12 pusu "ihlal" yazmış |
| S00 | 🟠 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the gloves stay on the parapet" | prompt | On saniyelik çömelmede efor/oran cümlesi yok |
| S00–S22 (23 sınır) | 🟠 | ③ | ses-görüntü uyumu | 🅒 | "A closed-space echo, a steady low fan …" / "Sound carries normally — engine roar, metal impacts, wind" | kurgu-ses | AUDIO klip başına yazıldı; sert bed geçişi birleştirme gerçeği |
| S01 | 🔴 | ⑪ (listede yok) | ışık | 🅑 | "amber key from above and behind the tall figure" | prompt | Saat/taraf yok (🅑13, 0/96); S00→S01 anahtar ışık sıçraması |
| S01 | 🟠 | ① | parçacık/duman/toz | 🅐 | "plate fragments fall straight down, no glow lingering" | araç ayarı | Kıvılcım kalkanı geçip havada asılı kalmış |
| S01 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "shadow edges soft but deep" | QA | Vakumda siyah gölge bekliyor; SPEC yumuşak-derin diyor (S01/S07/S19) |
| S01 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | Mod V; parça kesitinde "amaç belirsiz" hükmü, film bilinmiyor |
| S02 | 🔴 | ⑧ | efor/beden | 🅒 | "the near helmet turns to look back at the figure, the shoulder rising a hand" | QA | Kalkanı Veyra taşıyor; mühendis yalnız dönüyor, yük yok |
| S02 | 🟠 | ① | zemine geçme | 🅑+ | "its border a sharp line" · "a tall figure steps through the gate onto the basalt" | prompt | Sert çizgili kapı ile içinden adım: çelişen istek |
| S03 | 🔴 | ① | el-nesne kaynaşması | 🅐 | "Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers." | kadraj kararı | On saniye süren kavrama; kıvılcım planlı sıyrıktan geliyor |
| S03 | 🔴 | ① | klon/fazla kişi | 🅐 | "Exactly 2 human characters in suits, no duplicates, no extra person." | araç ayarı | Sayı kilidi yazılıydı; üçüncü figür sol kenardan çıktı |
| S03 | 🟠 | ⑧ | efor/beden | 🅐 | "the cobalt figure staggers one step sideways, knees bending" | araç ayarı | Sendeleme yazılıydı; QA "tepki yok" diyor |
| S04 | 🔴 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the gloves settle onto the two grips" | prompt | Eldiven sertliği/yavaş parmak cümlesi yok (🅑5) |
| S04 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | Tablet/ekran dokunuşları SAYAÇ tasarımı (S04-S06, S14-S16) |
| S05 | 🔴 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the foot figure walks up the left ramp" | prompt | Rampa eğimi/adım oranı cümlesi yok |
| S05 | 🟠 | ⑤ | sayı/nesne sayısı | 🅒 | "The last two figures walk up their ramps and inside" | QA | Figürler tasarım gereği içeri girer; kayıp yok |
| S06 | 🔴 | ⑧ | efor/beden | 🅑 | "the forearm tightening as it takes the weight" | prompt | Şiddet sayısız (🅑5); kapak ağırlığı yazılı değil |
| S06 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "the right glove unclips the field reader from the belt" | kadraj kararı | Temas cümlesi vardı; parmak bozulması |
| S06 | 🟠 | ① | istenmeyen yazı | 🅑 | "the screen lights: three thin branching lines joined at identical angular joints" | prompt | Ekran çizgileri için kaymaz/yüzmez kilit yok |
| S06 | 🟠 | ⑭ | oyunculuk | 🅑 | "the reader held out at arm's length" | prompt | Okuyucunun hedefi yazılı değil |
| S07 | 🔴 | ⑤ | arka plan/dünya çapası | 🅑 | "the ring small above the ridge on the right" | prompt | B'ye dönüşte S01'in "rooftops under the amber lattice" cümlesi yok (🅑11) |
| S07 | 🔴 | ⑭ | oyunculuk | 🅐 | "the tool still levelled, and shifts his weight back one step to the channel mouth at his back" | araç ayarı | Asker düşmana sırt dönüp yürüdü |
| S08 | 🟠 | ① | ışık | 🅒 | "two bright impacts mark its outer face" · "the amber wedge on the floor narrows and goes out" | QA | Planlı ışık olayı; kıvılcım darbelerden |
| S08 | 🟠 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the graphite figure's helmet is turned to the door" | prompt | Uzun alet tutuşu için kol/omuz gerilimi yok |
| S08 | 🟠 | ⑭ | oyunculuk | 🅑 | "the three figures standing in it" | prompt | Darbe anında beden tepkisi yazılı değil |
| S09 | 🔴 | ① | el-nesne kaynaşması | 🅑 | YOK — insansız kısa NEGATIVE temas cümlesini düşürmüş | prompt | Veyra eli maket bloklara değiyor (🅑2) |
| S09 | 🟠 | ① | diğer | 🅒 | "a tall pale-ceramic figure … dark seams at every joint" | QA | Seramik tasarım; "plastik" bu yüzden |
| S10 | 🟠 | ② | kask/giysi/ekipman kayması | 🅒 | "the back of the dark cobalt suit is one continuous sculpted surface from collar to hip" | QA | S10 sırttan; göğüs sıyrığı kadrajda olamaz |
| S11 | 🔴 | ① | el-nesne kaynaşması | 🅑 | "the engineer holding the reader up to the commander" | prompt | Okuyucu↔komutan nesne-gövde sınırı yok (🅑2a) |
| S12 | 🔴 | ①+⑤ ×2 | kamera/kesme/kadraj | 🅒 | "The dark cell is a dimmed patch, not a hole and not a tear." | QA | Planlı karanlık hücre (SPEC ENGEL); yapay kesim sanılmış |
| S12 | 🟠 | ② | arka plan/dünya çapası | 🅑 | "one empty service tower taller than the rest" (S00) | prompt | S00'da kule hasarı belirsiz; S12'de sağlam |
| S12 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | Lazer doruğu "teknik" bulunmuş; mod V |
| S14 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "both catches press down with one click" | kadraj kararı | Temas cümlesi vardı; parmak kasanın içine girdi |
| S14 | 🟠 | ⑧ | efor/beden | 🅑 | YOK — yalnız "both catches press down with one click" | prompt | Eldiven direnci cümlesi yok |
| S15 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "The cobalt fingertip touches three places on the map" | kadraj kararı | Minyatür blok üstünde kayan parmak: yüksek risk |
| S17 | 🔴 | ⑧ | efor/beden | 🅒 | "The lid opens, the orange glove lifts out a squared steel clamp" | QA | QA "engebeli arazide yürüyüş" yazmış; sahne kabinde oturuyor |
| S17 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "the glove lifts a squared steel clamp out of the recess" | kadraj kararı | Temas cümlesi vardı |
| S18 | 🔴 | ⑧ | efor/beden | 🅒 | "boots on the ramp" | QA | "Hızlı hareket" yok; durağan donanım sahnesi |
| S18 | 🟠 | ① | el-nesne kaynaşması | 🅑 | "The strap is pulled by the gunner's glove only, no third hand." | prompt | Kayış↔tok nesne-nesne sınırı yok (🅑2a) |
| S20 (ızgara S19) | 🔴 | ① | parçacık/duman/toz | 🅐 | "glances off to the side into the deck plating two figure-lengths away, no glow lingering" | araç ayarı | Kalkan kıvılcımı havada asılı |
| S20 (ızgara S19) | 🔴 | ① | zemine geçme | 🅑 | "the figure swings its shield square to the gunner and walks at the ramp" | prompt | Ayak–zemin teması yok; geri bükülen bacak |
| S21 | 🔴 | ⑪ (listede yok) | ışık | 🅒 | "cold blue-white work lamps from above" | QA | Hangar içi; QA "dış çatışma 2↔10" saymış |
| S22 | 🔴 | ⑪ (listede yok) | ışık | 🅒 | "cold blue-white work lamps from above" | QA | Aynı: iç mekân; yön hepsinde "from above" |
| S22 | 🟠 | ① | ışık | 🅐 | "The impact light lives on the ceramic surface only, nothing spills, nothing sprays." | araç ayarı | 0% bloom yazılıydı; darbe çevresinde bloom |
| S23 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | PART 1 sonu film sonu değil; döngü S95↔S00 |
| S23 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "amber daylight in the mouth" | QA | Planlı IC→YUZEY geçişi |
| S24 | 🔴 | ① | ortama aykırı ses | 🅒 | "Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet." | QA | Mercek vakum sanmış; SPEC 1 atm, dış ses normal |
| S24 / S47 | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK | QA | PART içi S24↔S47 kafiyesi plan değil; eş çiftler S23↔S24 |
| S25 | 🟠 | ① | ışık | 🅐 | "0% bloom, no glow, no soft focus" (aynı promptta "the fighters' amber edges bright") | araç ayarı | Parlak kenar isteği gerilim yaratıyor ama kilit yazılıydı |
| S26 | 🔴 | ⑧ | efor/beden | 🅑 | "the orange gloves push both grips forward, the forearms tightening" | prompt | Şiddet sayısız; oran yok (🅑5) |
| S26 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "the orange gloves push both grips forward, the forearms tightening" | kadraj kararı | Temas cümlesi vardı; kumanda kolu eğrilmiş |
| S26 | 🟠 | ① | diğer | 🅐 | "The fighter is not hit and does not vanish, it stays whole above the trench." | referans/panel | Veyra avcı şekil/ölçek kayması; panel gerek |
| S26 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | "it moves only as the craft moves" | QA | Kamera araca bağlı; "kilitli" sanılmış |
| S27 | 🟠 | ① | parçacık/duman/toz | 🅐 | "sparks and torn plate fall straight down into the trench" | araç ayarı | Kıvılcım havada patlamış, enkaz kaybolmuş |
| S28 | 🔴 | ① | zemine geçme | 🅐 | "drives under the swinging pipe end with a hull-width to spare" | araç ayarı | Boşluk yazılıydı; boru motordan geçmiş |
| S28 | 🔴 | ⑤ | arka plan/dünya çapası | 🅒 | "the pipe end reaches the floor behind it" | QA | Boru kapalı hendekte düştü; S29 hendeğin dışında |
| S29 | 🟠 | ① | parçacık/duman/toz | 🅐 | "sparks and a piece of the ring's rim fall straight down" | araç ayarı | Kıvılcım yatay süzüldü; egzoz sıçraması kısmen planlı |
| S29 | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | "a stack of steel pipes" (S24) · "steel pipes behind" (S29) | prompt | Boru yığını/hattı iki ayrı tarif (🅑11) |
| S30 | 🔴 | ⑥ | yerçekimi/süzülme | 🅐 | "The whole cabin is tilted to the right with four seated torsos leaning the same way" | araç ayarı | QA "sıfır atalet eğimi"; eğim yazılıydı |
| S30 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "both gloves on a hold bar" | kadraj kararı | Temas cümlesi vardı; parmak bozulması |
| S31 | 🟠 | ① | parçacık/duman/toz | 🅐 | "the dust it raised settles within two seconds" | araç ayarı | Toz düz hacim levhası gibi |
| S31 | 🟠 | ② | kask/giysi/ekipman kayması | 🅑 | "its landing skid grinds along the metal floor throwing sparks" | prompt | Kızak hiçbir araç cümlesinde yok |
| S32 | 🔴 | ①+⑧ ×2 | zemine geçme | 🅑 | YOK — yalnız "boots on the ramp at four different beats" | prompt | Ayak/adım ağırlığı cümlesi yok |
| S33 | 🔴 | ① | el-nesne kaynaşması | 🅐 | "the glove pushes the collar; the forearm tightens, the collar does not move" | kadraj kararı | Temas cümlesi vardı; eldiven kilide kaynadı |
| S33 | 🔴 | ⑧ | efor/beden | 🅑 | "the glove pushes the collar; the forearm tightens, the collar does not move" | prompt | Şiddet sayısız; oran yok |
| S33 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅐 | "fixed, absolutely zero camera movement" | araç ayarı | Klip içi yeniden çerçeveleme |
| S33 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "a cold work lamp on the pilot's chest lighting the panel flat" | QA | Planlı D kurulumu göğüs lambası |
| S34 | 🟠 | ① | el-nesne kaynaşması | 🅑+ | "her left glove rises flat, palm back, at shoulder height" | prompt | "flat glove" levha gibi okunmuş; parmak yapısı yok |
| S34 | 🟠 | ② | kask/giysi/ekipman kayması | 🅒 | "a long pale scrape across the left chest plate" (S30) | QA | S34 sırttan; QA "delik" sanmış (prompt: no hole) |
| S35 | 🔴 | ⑦+⑧+⑩ (listede yok)+⑭ ×4 | oyunculuk | 🅒 | "the raised glove closes into a fist" | QA | Promptta baston/saldırı yok; kaldırılan eldiven "dur" işareti |
| S35 | 🟠 | ① | zemine geçme | 🅑 | "a long stride on the curved floor with a different rhythm from human boots" | prompt | Ayak teması yok; promptta "grating" yok |
| S37 | 🔴 | ⑤ | klon/fazla kişi | 🅑 | "Far back the off-white and orange figures" | prompt | Arka figür yalnız renkle; "characters in suits" iş takımı okutmuş |
| S37 | 🔴 | ⑧ | efor/beden | 🅑 | "Another short burst from the niche keeps the shield fixed on it" | prompt | Rekil/omuz cümlesi yok |
| S37 | 🟠 | ① | klon/fazla kişi | 🅐 | "walking the whole way in view" | araç ayarı | Gunner ışınlandı; arka figür 2B planlı "still" |
| S38 | 🔴 | ⑦ | diğer | 🅐 | "four bright points cross the gap and meet the shoulder plate; a hard impact light spreads on the ceramic" | araç ayarı | İsabet yazılıydı; QA "ölümcül atış yok" |
| S38 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅑 | YOK — yalnız "the tool levelled" | prompt | Atıcıda rekil/tepki yazılı değil |
| S38 | 🟠 | ① | zemine geçme | 🅑 | "the figure folds at the knees and goes down onto the plate as one piece" | prompt | Canlı uzvu↔zemin sınırı yok (🅑2a) |
| S39 | 🔴 | ① | el-nesne kaynaşması | 🅐 | "draws it out of the slot with one steady pull, the forearm tightening" | kadraj kararı | Temas cümlesi vardı; parmak kol derisine girdi |
| S39 | 🔴 | ⑧ | efor/beden | 🅑 | "draws it out of the slot with one steady pull, the forearm tightening" | prompt | Şiddet sayısız; oran yok |
| S39 | 🟠 | ① | ışık | 🅐 | "the module's screen lights amber, a plain lit surface with no marks" | araç ayarı | Parlak ekran istendi; 0% bloom yazılıydı |
| S39 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅐 | "fixed, absolutely zero camera movement" | araç ayarı | Aşağı eğilme sanılmış; eller kare dışına çıkıyor |
| S40 | 🔴 | ① | zemine geçme | 🅑+ | "the two shields swinging round until they meet at the edges in one closed curve" | prompt | Kalkanlar birleşecek; dikiş/ayrım yazılı değil |
| S41 | 🔴 | ① | zemine geçme | 🅑+ | "the two figures step clear on the far side as it comes down" | kadraj kararı | İnen kapak altından geçiş: temas anı davet |
| S42 | 🔴 | ⑧ | efor/beden | 🅑 | YOK — yalnız "his long bursts" | prompt | Rekil/omuz cümlesi yok |
| S42 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "no merging, no phasing, no extra fingers" | araç ayarı | Altıncı parmak; kilit yazılıydı |
| S42 | 🟠 | ⑦ | diğer | 🅑 | "Bright points from the balcony strike the plate near the gunner, his long bursts drive the tall figure down" | prompt | Tek klipte dört eşzamanlı eylem; ana eylem yok |
| S42 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | "her arm extended, pointing at a gap in the curved wall" | QA | Jest yazılı; QA beklentisi |
| S43 | 🟠 | ① | ışık | 🅑 | YOK — S02'deki "not a glow and not a beam" bu kapı klibinde yok | prompt | Kapı ışığı için glow kilidi düşmüş |
| S44 | 🟠 | ① | zemine geçme | 🅑 | "the figure crosses to the ring in three long strides, the lower legs bending backward" | prompt | Ayak kilidi yok; QA Veyra'yı giysili yürüyüş sanmış |
| S44 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "low amber from the curved surfaces" | QA | Planlı IC→C0 hacim geçişi |
| S45 | 🔴 | ⑧ | efor/beden | 🅒 | "She steps through the gate in two strides" | QA | "Uzun yürüyüş" yok; iki adım |
| S47 | 🟠 | ⑩ (listede yok) | oyunculuk | 🅒 | YOK | QA | PART sonu küme S47-S49; final vuruş PART kuralı değil |
| S48 | 🔴 | ① | zemine geçme | 🅑+ | "the two shields swing together and lock edge to edge into one wider curve" | prompt | S40'la aynı: kalkan birleşme sınırı yok |
| S48 | 🔴 | ⑭ | oyunculuk | 🅐 | "the pilot beside the winch post with his hand at his side" | araç ayarı | Eller havada sallandı; "hand at his side" yazılıydı |
| S48 | 🔴 | ⑧ | efor/beden | 🅒 | "the pilot's hand closes on the release lever, not pulling" | QA | S48'de çekme yok; çekme S49'da |
| S48–S64 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | YOK | QA | Tek tempo şikâyeti; sahneler tek jestle yazıldı |
| S48 / S71 | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK | QA | Kafiye S00↔S95; S71↔S72 PART sınırı |
| S48–S53 | 🔴 | ⑪ (listede yok) | ışık | 🅐 | "cold platform lamps from above" | araç ayarı | Prompt tek yön yazdı; ışık yönü kayıyor |
| S48 | 🟠 | ① | parçacık/duman/toz | 🅐 | "glance off into the far wall" | araç ayarı | Kıvılcım asılı; yerçekimi kilidi yazılıydı |
| S48 | 🟠 | ① | ışık | 🅐 | "0% bloom, no glow, no soft focus" | araç ayarı | Kalkan amber yüzeyi çevresinde bloom |
| S49 (ızgara S50) | 🔴 | ① | zemine geçme | 🅑 | "the two tall figures spring apart, one to each side" | prompt | Ayak/zemin kilidi yok; "spring apart" kayma çağırıyor |
| S49 (ızgara S50) | 🔴 | ① | diğer | 🅑 | "a heavy squared load" | prompt | Yükün ölçüsü yazılı değil; kasa küçülmüş |
| S49 (ızgara S50) | 🔴 | ⑥ | yerçekimi/süzülme | 🅐 | "the load drops straight down" · PHYSICS 0.9 g | araç ayarı | Kargo 2,48; vurulan Veyra 1,67 m/s² |
| S49–S52 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | YOK | QA | Mod V: "manken gibi duruş"; tek jest kuralı tasarım |
| S49 (ızgara S50) | 🟠 | ① | arka plan/dünya çapası | 🅑 | YOK — S48-S50'de arka duvar/boru cümlesi yok | prompt | Arka plan envanteri dönmüyor (🅑11) |
| S49 (ızgara S50) | 🟠 | ⑭ | oyunculuk | 🅐 | "the pilot pulls the lever down, his forearm tightening" | araç ayarı | Tek çekiş yazılıydı; döngüye girmiş |
| S49 (ızgara S50) | 🟠 | ⑧ | efor/beden | 🅑 | YOK — yalnız "dust rising and settling within two seconds" | prompt | Yakındaki figürlerin darbe tepkisi yazılı değil |
| S50 (ızgara S49) | 🟠 | ⑦ | diğer | 🅐 | "a short burst of four bright points meets the bare flank" | araç ayarı | Kaynak ve isabet yazılıydı |
| S50 (ızgara S49) | 🟠 | ⑭ | oyunculuk | 🅑 | "the torso turns to the left, the shoulder dropping" | prompt | Hangi "sol"? yön ve sebep yazılı değil |
| S51 | 🔴 | ⑭ | oyunculuk | 🅒 | "he goes down onto that knee, hauls himself up by the crate edge" | QA | Zincire uzanma yok; diz çökme planlı |
| S52 | 🔴 | ⑭ | diğer | 🅑 | "sends one short burst of four bright points back along the platform" | prompt | Hedef kadrajda yok (🅑12) |
| S53 | 🔴 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the hatch swings open" | prompt | Kapağı kaldıran efor yazılı değil |
| S53 | 🟠 | ⑭ | oyunculuk | 🅒 | "his glove points down the shaft and then up at the ceiling" | QA | Replik 4 (post-dub) jesti |
| S54 | 🔴 | ⑭ | diğer | 🅑+ | "the off-white fingertip presses the hand-crank icon on the plan; the icon lights amber" | prompt | Kâğıt plan üstünde yanan simge: çelişen istek |
| S54 | 🔴 | ⑧ | efor/beden | 🅑 | YOK — yalnız "presses the hand-crank icon" | prompt | Eldiven sertliği cümlesi yok |
| S54 | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅐 | "fixed, absolutely zero camera movement" | araç ayarı | Aşağı doğru sürünme |
| S54 | 🟠 | ② | kask/giysi/ekipman kayması | 🅑+ | "Slightly above eye height looking down at three pairs of gloves." | prompt | Eldivenler nesne gibi; kol–gövde bağı yazılı değil |
| S54 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "cold platform lamps from above" | QA | Planlı kurulum değişimi; mercek kendi "Evet" demiş |
| S55 | 🔴 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | "wide shot, 24mm spherical lens" | QA | Planlı MCU→WS; "4 kademe" değil |
| S55 | 🔴 | ⑭ | zemine geçme | 🅑 | "the two step into the lift cage one after the other" | prompt | Ayak kilidi yok; geriye kayma |
| S55 / S57 / S58 | 🔴 | ⑩ (listede yok) | oyunculuk | 🅒 | YOK | QA | Silah sonrası reaksiyon: "ölçülü seri" bilinçli |
| S55 | 🟠 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the gunner sends four bright points at the far end" | prompt | Rekil/duruş tepkisi yok |
| S55 | 🟠 | ⑤ | sayı/nesne sayısı | 🅒 | "the pilot's helmet sinks below the hatch rim and is gone" | QA | Pilot iner, iki kişi kafese girer |
| S56 | 🟠 | ⑭ | oyunculuk | 🅒 | "the engineer's helmet turns to it" (6.0 s) | QA | Baş dönüşü 6,0 s'de yazılı; QA 3 s'de ölçmüş |
| S57 | 🔴 | ⑧ | efor/beden | 🅒 | "three bright points leave the tool in one measured burst, the shoulders steady" | QA | "shoulders steady" bilinçli: ölçülü seri |
| S57 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "cold platform lamps" (S56→S57) | QA | Mekân değişimi mercekçe bildirilmiş |
| S57 | 🟠 | ⑭ | zemine geçme | 🅐 | "leaning his left hip on a crate" · "his weight on the left leg" | araç ayarı | Ağırlık cümlesi vardı; ayak kaymış |
| S58 | 🔴 | ⑭ | el-nesne kaynaşması | 🅐 | "The cobalt glove is already closed around the graphite forearm cuff and pulling" | kadraj kararı | Temas yazılıydı; QA "temas yok" diyor |
| S58 | 🔴 | ⑭ | diğer | 🅑 | "three bright points pass the cobalt shoulder into the platform" | prompt | Hedef yönü yok; "ona ateş" okunuyor (🅑12) |
| S58–S60 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | Aksiyon doruğu ortada: SEK15-16 planlı |
| S59 (ızgara S60) | 🔴 | ⑭ | oyunculuk | 🅒 | "a cobalt glove is pressed flat to the mesh at the lower edge" | QA | Eldiven kafese yaslı: tasarım |
| S59 (ızgara S60) | 🔴 | ⑦ | diğer | 🅒 | "A single brief flash at the end of the raised arm" | QA | Nötr tarif (POLİTİKA S59); yörünge bilinçli yok |
| S59 (ızgara S60) | 🔴 | ⑥ | yerçekimi/süzülme | 🅐 | "the long tool slips from his gloves to the deck in the same second" | araç ayarı | 0,68 m/s² (S57: 3,13); 0,9 g yazılıydı |
| S59 (ızgara S60) | 🔴 | ⑪ (listede yok) | ışık | 🅒 | "cold platform lamps through the mesh" | QA | Master sırası S60↔S59; planlı şok S59→S60 |
| S59 / S71 | 🔴 | ② | hikâye/anlatım/kurgu | 🅓 | YOK | QA | S71'de "sarı muhafız" yok; yalnız komutan+mühendis |
| S59 (ızgara S60) | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | "the camera rises with the cage" | QA | Kamera kafesle yükseliyor; "handheld" değil |
| S60 (ızgara S59) | 🔴 | ⑭ | zemine geçme | 🅑 | "the crested figure walks through the ring in three strides" | prompt | Ayak kilidi yok |
| S60 (ızgara S59) | 🔴 | ⑪ (listede yok) | ışık | 🅒 | "the light on it goes from cold to amber as it passes the ring's plane" | QA | Planlı portal ışık olayı |
| S61 | 🔴 | ⑭ | zemine geçme | 🅑 | "they step into the room, the commander two paces, the engineer one" | prompt | Ayak kilidi yok |
| S61 | 🟠 | ① | ses-görüntü uyumu | 🅑+ | "a radio channel opening on static and staying empty" | prompt | "Radio channel opening" ses çağırdı; S10/S83'te aynı |
| S61 | 🟠 | ⑭ | oyunculuk | 🅒 | "her helmet turns to the side and holds as if to a channel" | QA | Kanalı dinleme jesti yazılı |
| S62 | 🔴 | ⑭ | el-nesne kaynaşması | 🅐 | "it lifts the steel clamp out of its recess" | kadraj kararı | Temas cümlesi vardı; tutuş açısı döndü |
| S62–S65 | 🔴 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | Vana/panel sahneleri SEK16-17 planlı |
| S63 | 🟠 | ⑭ | diğer | 🅓 | YOK — "IN FRAME: hands" | QA | Başlar kadrajda yok; çapa belirsiz |
| S63 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅒 | "50mm spherical lens, high angle" | QA | MCU→MCU geçişi; 2 kademe değil |
| S64 | 🔴 | ⑭ | el-nesne kaynaşması | 🅐 | "the cobalt glove moves the lever another hand's width, the forearm tightening" | kadraj kararı | Temas cümlesi vardı; kol eklemi bağımsız |
| S64 | 🔴 | ⑪ (listede yok) | ışık | 🅒 | "the module's screen goes from amber to dark in one step" | QA | Planlı: modül söner |
| S64 | 🔴 | ⑧ | efor/beden | 🅑 | "the cobalt glove moves the lever another hand's width, the forearm tightening" | prompt | Şiddet sayısız; oran yok |
| S65 | 🔴 | ⑭ | el-nesne kaynaşması | 🅑 | "the off-white gloves draw the strap through its buckle in one pull" | prompt | Kayış↔tok sınırı yok (🅑2a) |
| S65 | 🟠 | ⑧ | efor/beden | 🅑 | YOK — eldiven beceriksizliği cümlesi | prompt | "second pull shorter" oranı var; eldiven direnci yok |
| S66 | 🔴 | ⑭ | diğer | 🅓 | YOK — gövde sarsılması yok ("four bolt turns") | QA | S66'da kapağa darbe/sarsılma yok |
| S66 | 🔴 | ⑧ | efor/beden | 🅐 | "the third and fourth turns, slower than the first" | araç ayarı | Oran cümlesi yazılıydı |
| S66–S71 | 🔴 | ⑦ | diğer | 🅓 | YOK | QA | 03:00–04:00 altı klip; çapa belirsiz |
| S67 | 🟠 | ⑭ | diğer | 🅓 | YOK — "Exactly 2 human characters in suits" | QA | S67'de silahlı muhafız yok |
| S67 | 🟠 | ⑧ | efor/beden | 🅒 | "The engineer's glove taps the short thick pipe once" | QA | Kablo çekme yok |
| S68 | 🔴 | ⑭ | diğer | 🅓 | YOK — "Human count zero in this frame" | QA | S68 insansız; yana kayan muhafız yok |
| S69 | 🔴 | ⑭ | diğer | 🅓 | YOK — "Exactly one human character in a suit" | QA | Turuncu çömelme yok; yalnız komutan |
| S69 | 🟠 | ⑧ | efor/beden | 🅒 | YOK | QA | İtki rüzgârı yok; iç mekân |
| S69 | 🟠 | ⑨ (listede yok) | kamera/kesme/kadraj | 🅐 | "fixed, absolutely zero camera movement" | araç ayarı | Plansız pan/tilt |
| S69 | 🟠 | ⑪ (listede yok) | ışık | 🅒 | "amber from the slit on the helmet and gloves" | QA | Hacim geçişi planlı |
| S70 | 🟠 | ⑧ | efor/beden | 🅒 | YOK — "human count zero" | QA | S70 insansız; çömelme yok |
| S71 | 🟠 | ⑫ (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK | hikâye/plan | PART sonu; döngü S95↔S00 |
| S72 | 🔴 | ① | klon/fazla kişi | 🅒 | "The side door slides open and one tall figure steps through" | QA | Planlı Veyra girişi; "kopya takım" değil |
| S72 | 🔴 | ⑧ | efor/beden | 🅒 | "the commander raises her tool at the hatch" | QA | "Kapı kaldırma" yok |
| S73–S74 | 🟠 | ② | kask/giysi/ekipman kayması | 🅑 | "her right glove draws the short tool from her hip" | prompt | Kalça tarafı yazılı değil (🅑3a) |
| S75 | 🔴 | ① | zemine geçme | 🅑 | "one tall figure is in the entrance beyond, two paces from the threshold" | prompt | Ayak kilidi yok; geri kayma |
| S75 | 🔴 | ⑧ | efor/beden | 🅑 | "she pulls the lever down, the forearm tightening, the shoulders dropping into it" | prompt | Şiddet sayısız; oran yok |
| S75 (S72 ile) | 🟠 | ② | kask/giysi/ekipman kayması | 🅐 | "a pale grey mark on the left shoulder plate" | referans/panel | İşaret solda yazılıydı; model aynalamış |
| S75 (S72 ile) | 🟠 | ② | arka plan/dünya çapası | 🅒 | "the outer hatch … bent inward a hand's depth" (S72) | QA | İki farklı kapı: dış kapak ↔ muhafaza kapağı |
| S76 | 🔴 | ⑧ | efor/beden | 🅑 | YOK — yalnız "the coil compressing a hair" | prompt | Eldiven sertliği cümlesi yok |
| S76 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "The T-handle does not move from the centre." | kadraj kararı | Temas cümlesi vardı; eldiven kola girdi |
| S77 | 🟠 | ①+⑥ ×2 | parçacık/duman/toz | 🅐 | "fragments falling straight down" | araç ayarı | Enkaz 2B düzlem gibi, asılı |
| S78 | 🔴 | ⑪ (listede yok) | ışık | 🅑 | "amber from the lattice band above" | prompt | Taraf/saat yok (🅑13); 9→3 sıçraması |
| S79 | 🔴 | ⑧ | efor/beden | 🅐 | "the second and third turns, each slower than the first" | araç ayarı | Oran cümlesi yazılıydı |
| S80 | 🔴 | ② | klon/fazla kişi | 🅒 | "At the foot of each ramp one figure in a plain grey hard-shell suit" | QA | Planlı: iki özdeş gri sivil |
| S81 | 🟠 | ⑮ | yön/180° | 🅑 | "the glove rises off the housing and comes over the T-handle" | prompt | Hareketin ekran yönü yazılı değil |
| S81 / S84 | 🟠 | ⑤ | istenmeyen yazı | 🅑+ | "A T-handle selector stands centred" | prompt | "selector" ×10, T-handle ×28 → panele basılmış (🅑6) |
| S82 | 🔴 | ①+⑦+⑭ ×3 | diğer | 🅑+ | "The cobalt glove hangs a finger above the centred T-handle" | prompt | Kol/gövde bağı yok; kask yalnız üst kenarda |
| S83 | 🔴 | ⑧ | efor/beden | 🅒 | "the commander's glove drops onto the T-handle and closes on it; the handle does not turn" | QA | "Kol çekme" yok |
| S83 | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | "The heavy containment door is seated on the threshold" | prompt | Kapı yüzeyi tarifsiz; "rigid slab" kilidi burada yok |
| S84 | 🟠 | ① | el-nesne kaynaşması | 🅐 | "The glove drives the T-handle from the centre to the long pipe's side" | kadraj kararı | Temas cümlesi vardı; parmaklar kola eriyor |
| S86 | 🟠 | ① | parçacık/duman/toz | 🅐 | "fragments dropping straight down" | araç ayarı | Enkaz yapay süzülme + sıçrama |
| S87 (S86 ile) | 🔴 | ⑤ | arka plan/dünya çapası | 🅑 | "Above, the amber lattice, whole" (S86) | prompt | Kafes biçimi S86'da tarifsiz; kubbe↔düz duvar (🅑8) |
| S88 | 🟠 | ① | arka plan/dünya çapası | 🅑 | "the lattice's hard amber edges run past on both sides" | prompt | Kafes/halka dünya cümlesi S88-S92'de düşmüş |
| S88 (S87 ile) | 🟠 | ⑤ | arka plan/dünya çapası | 🅑 | "beyond it the lensed bright ring, larger" | prompt | Halka eğimi/yönü yazılı değil (🅑8) |
| S89 | 🔴 | ⑤ | arka plan/dünya çapası | 🅑 | "the gap's hard amber edges on both sides of it" | prompt | Kafes cümlesi yok; "ikiz tüp" okunmuş |
| S89 (S77 ile) | 🔴 | ⑤ | arka plan/dünya çapası | 🅒 | "Black basalt rooftops far below" | QA | Farklı irtifa/kadraj; aynı yer sanılmış |
| S90 | 🔴 | ⑪ (listede yok) | ışık | 🅐 | "The last frame of the previous clip, unchanged" | araç ayarı | Küme dikişinde ışık yönü sıçradı |
| S90 | 🟠 | ⑮ | yön/180° | 🅒 | "leaning right" | QA | SPEC: K-1 sapması hep sağa |
| S91 | 🟠 | ① | arka plan/dünya çapası | 🅓 | YOK — "IN FRAME: none" | QA | S91'de kaya duvar yok; çapa belirsiz |

## ÖZET
```
HÜKÜM (tekil 192)   🅐 51 · 🅑 59 · 🅑+ 10 · 🅒 64 · 🅓 8      🅑/(🅐+🅑+🅑+) = %58   (19.09 genel ölçüsü %54)
  yalnız 🔴 (98)   🅐 21 · 🅑 34 · 🅑+ 5 · 🅒 33 · 🅓 5
  yalnız 🟠 (94)    🅐 30 · 🅑 25 · 🅑+ 5 · 🅒 31 · 🅓 3
  --film listesindeki mercekler (151)   🅐 45 · 🅑 56 · 🅑+ 10 · 🅒 32 · 🅓 8
  (listede yok) ⑨-⑫ (41 satır: 🔴 22 · 🟠 19)
  PART başına        P1: 🅐 12 · 🅑 17 · 🅑+ 1 · 🅒 18 · 🅓 0 | P2: 🅐 17 · 🅑 15 · 🅑+ 3 · 🅒 11 · 🅓 0 | P3: 🅐 15 · 🅑 16 · 🅑+ 4 · 🅒 28 · 🅓 7 | P4: 🅐 7 · 🅑 11 · 🅑+ 2 · 🅒 7 · 🅓 1
TÜR (hepsi)         efor/beden 33 · ışık 23 · el-nesne kaynaşması 20 · oyunculuk 18 · zemine geçme 17 · diğer 17 · arka plan/dünya çapası 13 · kamera/kesme/kadraj 11 · parçacık/duman/toz 9 · hikâye/anlatım/kurgu 8 · kask/giysi/ekipman kayması 6 · klon/fazla kişi 5 · yerçekimi/süzülme 3 · ses-görüntü uyumu 2 · sayı/nesne sayısı 2 · istenmeyen yazı 2 · yön/180° 2 · ortama aykırı ses 1
  en sık 5          efor/beden 33 · ışık 23 · el-nesne kaynaşması 20 · oyunculuk 18 · zemine geçme 17
KAPANMA YERİ        prompt 68 · QA 64 · araç ayarı 35 · kadraj kararı 15 · hikâye/plan 7 · referans/panel 2 · kurgu-ses 1
```
## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız · okunan klipler: S00–S11, S12–S15, S17–S23, S24–S45, S47–S59, S60–S71, S72–S90)

1. **Meta etiket, 192/192 prompt.** S59 görsel: `Scene 60 of 96.` · video: `Scene 60 of 96. Duration 10 seconds.` Dosya başlığında etiketin "S + 1" olduğu kayıtlı, ama etiket modele giden metindir; dosya numarası (SAHNE 59) ile prompt numarası (60) farklı, QA ve operatör aynı klibe iki numara veriyor. Sayı/etiket kadraja basılma riski 🅑6 sınıfının kendisi.
2. **Başka sahneye atıf, 76 klipte.** S58 CAMERA: `— the same position, height and lens as Scene 51.` Başlık "hiçbir prompt oraya ATIF YAPMAZ, her prompt tek başına çalışır" diyor; I2V motoru "Scene 51"i göremez, cümle ya boş kalır ya da yazı olarak okunur.
3. **Büyük harfli jeton.** Her video promptunda `START FRAME: the approved still from this scene's IMAGE prompt` (96/96); NEGATIVE'de `no CGI or video-game look` (192/192); S76–S85'te `T-handle selector` (28 kez). QA yalnız küçük harfli `selector` kelimesinin panele "SELECTOR" diye basıldığını yazdı (S81/S84, 🟠).
4. **Çelişen iki istek.** S54 görsel+video: `a flat plan sheet showing a hatch outline with a hand-crank icon` + `the icon lights amber` — kâğıt üstünde yanan simge (QA: "boş yüzeye işaret", 🔴). S25 LIGHT: `the fighters' amber edges bright` ↔ NEGATIVE `0% bloom, no glow` (QA: bloom, 🟠). S02: `its border a sharp line` + figür kapıdan adım atıyor (QA: bot çerçeveden geçiyor, 🟠). S40/S48: `lock edge to edge into one wider curve` — birleşme sınırı hiçbir yerde yok (QA: kalkanlar kaynaştı, 🔴 ×2).
5. **Kendi içinde çelişki.** S60 AUDIO: `…breathing inside the helmet. After the transition, low curved tones inside the hull, a slow deep hum, no human breathing.` (aynı satırda hem nefes var hem yok). S35 CAMERA: `the camera moves forward at their walking pace` ↔ TIMELINE `0.0s — four still backs … 9.5s — four backs still` (figürler 10 s durur, kamera yürüyen figürü izliyor sanılır). S26 NEGATIVE: `it stays whole above the trench` ↔ TIMELINE `9.0s — … the fighter gone above`.
6. **İnsansız klipte kask nefesi, 19 klip** (S12 S13 S19 S24 S25 S27 S28 S29 S31 S60 S68 S77 S78 S87–S92; hepsinde İNSAN: 0). S24 AUDIO: `Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet.` Kadrajda ne kask ne insan var; ortam-ses kalıbı ezbere yapıştırılmış. Aynı 20 klipte NEGATIVE: `the empty deck and sky are the subject` — S24 koridor uçuşunda ve S88 kafes tırmanışında "deck" yok.
7. **Telsiz kanalı sesi çağırıyor.** S61 AUDIO: `a radio channel opening on static and staying empty` + `No dialogue.` → QA bu klipte konuşma duydu (`69... 48... Transfer request accepted`). S10 `a thin radio hiss opening on the channel` → QA `Roger, system secure` (01:47); S83 `a radio channel opening on breath and static without words` → QA `Depth check complete.` (P4 01:54). Dört "radio channel" klibinden üçünde ses üretildi; S91'de (P4 03:17, `Unidentified vehicle, state your clearance code.`) telsiz cümlesi olmadan da konuşma çıktı → toplam 4 duyulan replik, planlı post-dub'ların hiçbiri değil. NEGATIVE'in `No voice is written into the picture, no mouth, no invented on-screen speaker` cümlesi de motor için anlamsız meta ifade.
8. **Motorun gösteremeyeceği soyut/zihinsel ifade.** S61: `her helmet turns to the side and holds as if to a channel`. S33: `two fingers measure a span across the mechanism where a clamp would seat`. S26/S61 gibi "dinleme", "ölçme" fiilleri kadrajda iz bırakmıyor; QA bu yüzden "nedensiz baş dönmesi" (⑭) yazdı.
9. **Şişkin NEGATIVE.** Görsel NEGATIVE ortalama 911 karakter (695–1064), video 994 (775–1144); S00: 1031 / 1111. Yedi-sekiz çekirdek cümle her klibe kopya (bloom/foto/giysi/parçacık 96/96). Kısa "insansız" NEGATIVE'ler (24 klip, <900) temas cümlesini düşürüyor — ama S09'da Veyra eli maket bloklara değiyor (QA: kaynaşma, 🔴).
10. **Hasar/yıpranma kilidi sahneye göre kopuk.** Mara'nın `a long pale scrape across the left chest plate` 14 klipte yazılı (S03 S08 S14 S22 S30 S45 S50 S67 S69 S71 S72 S75 S83 S94); ön/yan kadrajda görünüp yazılmadığı 8 klip: S32 S36 S37 S41 S42 S52 S61 S86 (🅑3).
11. **Yalnız-eller kadrajında kol–gövde bağı yok.** `IN FRAME: hands…` ile başlayan 17 klipte kolun gövdeye bağlandığı hiçbir yerde yazılı değil. S54: `looking down at three pairs of gloves` (QA: masada çıkarılmış eldivenler); S82: `The cobalt glove hangs a finger above the centred T-handle` + `The lower rim of the helmet at the top of frame` (QA: havada asılı eldiven+kask, 🔴 ×3 mercek).

## 19.09 KURALLARI BU FİLMDE

```
🅑1  SES YASASI        YAZILI 96/96  (AUDIO ilk cümle ortamı adlandırıyor: 61 "closed-space echo" · 22 "Sound carries normally" · 8 kabin uğultusu · 3 hull tonu · 2 "No exterior sound at all"; S88/S92 geçişte "After the transition, no exterior sound")
                       BULGU 3 satır (🔴 1 · 🟠 2): S24 "vakumda motor sesi" 🅒 (QA vakum sanmış) · S61 telsiz konuşması 🅑+ (AUDIO'nun "radio channel opening" cümlesi) · ③ ambiyans sert kesim 🅒 → ortam-yasası ihlali 0
🅑2  TEMAS (el-yüzey)  YAZILI 72/96   (düşen 24 = insansız kısa NEGATIVE; bunlardan S09'da Veyra eli maketle temas ediyor)
🅑2a TEMAS (nesne-nesne) YAZILI 0/96
                       BULGU 37 satır (el-nesne 20 + zemine geçme 17): 🅐 17 · 🅑 15 · 🅑+ 5 → yarısından fazlası (20/37) cümlenin kapsamı dışı: nesne-nesne, canlı uzvu↔zemin, kalkan×kalkan, kapak×figür
🅑3  GİYSİ BİREBİR     YAZILI 96/96 ("Equipment and clothing identical throughout"; kimlik cümleleri klipten klibe birebir) · hasar kilidi: Mara "scrape" 14 klipte, ön/yan kadrajda 8 klipte eksik
                       BULGU 6 satır (kask/giysi/ekipman): 🅐 1 · 🅑 2 · 🅑+ 1 · 🅒 2  (🅑 olanlar: kalça tarafı yazılı değil S73-S74, kızak S31; 🅑+ S54 "three pairs of gloves")
🅑4  ORTAM SAYI+AD     YAZILI 93/96 sayı+ad ("Gravity is 0.9 g under one atmosphere…"); 2 vakum · 1 mikrogravite açıkça adlı
                       BULGU 12 satır (yerçekimi/süzülme 3 + parçacık 9, hepsi 🅐): QA ölçümleri 0,68–3,13 m/s² (film 8,8) — sayı kilidi yazılı, model tutmadı (🅑4'ün "sayı %100 tuttu" öngörüsü bu filmde ÇÜRÜDÜ)
🅑5  EFOR ORANI        ORAN cümlesi 6/96 (S58 S65 S66 S78 S79 S89) · şiddetsiz "tightening / shoulders dropping" 24/96 · hiç yok 66/96
                       BULGU 33 satır (efor/beden): 🅑 19 · 🅒 11 · 🅐 3 — oran yazılı S66 ve S79 yine de 🔴 (🅐)
🅑6  BÜYÜK HARFLİ JETON  VAR: "IMAGE" 96/96 video · "CGI" 192/192 · "T-handle" 28 (6 klip) · "Scene n of 96" 192/192 · "selector" (küçük harf) 10 kez / 5 klip
                       BULGU 1 (🟠 S81/S84 "SELECTOR" panele basıldı, 🅑+); büyük harfli jetonların kendisi kadraja basılmadı
🅑7  EKRAN/METİN       Pozitif metinde ekran/okuyucu/harita/plan 19 klip; hepsi "no letters, no digits" taşıyor → doğrudan çelişki 0 (metinsiz sayaç çözümü tuttu)
                       BULGU 3 (ekran yüzmesi S06 🅑 · yanan kâğıt plan S54 🅑+ · SELECTOR S81/S84 🅑+)
🅑8  DÜNYA ÇAPASI      27 dış-hacim klipte bazalt+kafes+halka üçlüsü 4/27 (S00 S12 S13 S87) · kafes cümlesi tam 9/27
                       BULGU 13 satır (arka plan/dünya çapası): 🅑 9 · 🅒 3 · 🅓 1 — kafes biçimi/halka eğimi S86-S92'de düştüğü yerde 4 🔴/🟠
🅑13 IŞIK SAAT YÖNÜ    YAZILI 0/96 ("o'clock" yok; LIGHT satırı 96/96 ama "from above / behind the camera")
                       BULGU 23 satır (ışık): 🅒 14 · 🅐 6 · 🅑 3 → saat/taraf eksikliğinden 🅑 2 (S01, S78) + S43 kapı-glow kilidi
```
