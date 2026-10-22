<!-- teknik-danisman (sonnet) · F5 tur 1 · eser PROMPTLAR/G01.md (tur 1b) · risk sütunu dolu çekimler C01 C02 C03 C06 C07 C10 C12 · 18.10.2026 · ajan cevabı aynen -->

## BLACK_ACCORD G01 · Faz 5 tur 1 · teknik-danışman

KAPSAM: risk sütunu dolu 7 çekim (C01 C02 C03 C06 C07 C10 C12). Sütunu boş çekimlere (C04 C05 C08 C09 C11) bakmadım.

### B1 · ÖLÜMCÜL · C03: 7-10 s'de "medical craft" isteniyor ama başlangıç karesinde yok
YER       PROMPTLAR/G01.md C03 Video (satır 248) ↔ C03 Görsel (satır 243)
KANIT     Video: `7-10 s: The medical craft remain waiting near the corridor edge.` Görsel'de "medical" ya da "craft" geçen cümle yok. Görsel yalnız kırmızı kama gemileri, beyaz-teal yelpaze gemileri, gümüş ve okra gemileri, silah ışıkları ve uzak istasyonu sayıyor. Frames to Video'ya referans eklenmiyor (satır 432), yani model 9.FOUR_FLEETS'i görmez.
ETKİ      Karede olmayan nesne isteniyor. Model onu sonradan belirtir ya da hayaletle çözer ("kadraja giren" = ölümcül).
DOĞDUĞU   metin (Görsel ile Video uyumsuz)
KURAL     Faz 3 delta bütçesi: kadraja giren ya da çıkan şey ölümcüldür [SÖZLEŞME, teknik-danisman kontrol listesi] · FILM.md:432 "Frames to Video'ya referans eklenmez" [ARAÇ]
ARIZA     yeni (T15 klon/fazla nesne akrabası)
DÜZELTME  Görsel'e `Rust-red wedge ships are at one side;` cümlesinden sonra bir cümle: `A few tiny medical craft wait at the corridor edge.` Video'daki `The medical craft remain waiting` cümlesi kalır. İki şey de olmazsa video cümlesi silinir.

### B2 · CİDDİ · C03: açılışta kamera filonun içinden geçiyor, olumsuz cümleler tutmuyor
YER       C03 Video 0-3 s ve son iki cümle (satır 248)
KANIT     `Use a slow lateral drift through the wide formation.` · `Do not start a major battle or add new ship groups.` · `no atmospheric engine or explosion sound in vacuum.`
ETKİ      Açılış çekimi (C01-C03). Çok sayıda gemi ve kamera hareketi bir arada: gemiler kameraya göre kayarken kaynaşır ya da çoğalır. "Do not…" cümlesi ölçülmüş biçimde tutmuyor. "battle" ve "explosion" kelimeleri model sesini ve olayı o yöne çeker.
DOĞDUĞU   hareket + prompt kelimesi
KURAL     ILK_30_SANIYE_KILAVUZU §6 (kalabalık + hızlı kamera) [SÖZLEŞME] · BILINEN_TUZAKLAR §B3 (ses kurguda kurulur; Y2 yatağı zaten planlı) · görev yasağı "no X ölçüldü, tutmuyor"
ARIZA     T13 · T15
DÜZELTME  (a) `through the wide formation` → `past the wide formation at a fixed distance` (gemilerin önünden geçer, aralarına girmez). (b) `Do not start a major battle or add new ship groups.` sil. 3-7 s'deki `all four fleet groups hold their separated positions` zaten pozitif karşılığı. (c) `Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design;` bırak, `no atmospheric engine or explosion sound in vacuum` sil. C03'ün sesi kurguda Y2 ile değişiyor. Plan "birebir" kuralı sahibin; sahip bu cümleleri istiyorsa gerekçeyle RED.

### B3 · CİDDİ · C02: Ishra'nın ağzı hiçbir yerde tanımlı değil, repliği ağız kadrajda
YER       C02 Video 2-6 s (satır 229) · KİMLİK CÜMLELERİ Ishra · yüz (satır 66) · ref 3.ISHRA (satır 133)
KANIT     A03 yüzü: `Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face.` Ağız yok. Video: `then she answers in a clear restrained female voice…: Then you came here to boast about it?`
ETKİ      Dudak senkronu için hedef yok. Üstüne saydam kubbe, su ve yansıma geliyor. Model ağzı uydurur ya da konuşmayı kubbenin içindeki suya veya gözlere bağlar. Göz asimetrisi riski (yan gözler) açılış kare kapısında zaten izleniyor, ağız izlenmiyor.
DOĞDUĞU   referans (ağız yok) + metin
KURAL     Teknik-danışman kontrol listesi, "ağız kadrajdaki replik" maddesi [SÖZLEŞME]
ARIZA     T05 (su başlığı) · yeni (tanımsız ağız)
DÜZELTME  Ref 3 onayında ağız görünüyor mu bakılır; görünmüyorsa v2. Video: `then she answers in` → `then her small mouth, visible below the eyes, moves minimally as she answers in`. Kare kapısına bir madde: "Ishra'nın ağzı suyun içinden okunuyor mu".

### B4 · CİDDİ · C02: "subtle fluid movement" suyu hareket ettirir, oda sesi yatakla uyuşmuyor
YER       C02 Video son cümle (satır 229)
KANIT     `Sound: subtle fluid movement, quiet room tone, no additional speaker.` Aynı prompttaki `constant water level` ve `Maintain the water dome, water level` cümlesi yalnız 6-10 s'de, yani konuşma bittikten sonra duruyor. Yatak Y1: `quiet chamber ventilation and distant table resonance` (FILM.md:672).
ETKİ      Ses tarifi görüntüyü de etkiler: model suya salınım ve dalgalanma çizer, "sabit su düzeyi" bozulur. "quiet room tone" da C01/C04'ün havalandırma tonundan ayrı bir oda üretir (kesme sürekliliği, ses yatağı).
DOĞDUĞU   prompt kelimesi
KURAL     BILINEN_TUZAKLAR §B4 (sıvı ortama aykırı) [SÖZLEŞME] · GECIS_VE_SES_SUREKLILIGI: ortam cümlesi birebir (görev (e) maddesi; dosyayı açmadım)
ARIZA     T05
DÜZELTME  `Sound: subtle fluid movement, quiet room tone, no additional speaker.` → `Sound: quiet chamber ventilation and distant table resonance.` Ayrıca `Maintain the water dome, water level and fixed life-support geometry.` cümlesi 0-2 s vuruşuna alınır.

### B5 · CİDDİ · C06: Nith'in kadraj dışı repliğiyle çakışma, Nem'in 6-10 s ağız durumu yazılmamış
YER       C06 Video 2-6 s ve 6-10 s (satır 306) · FILM.md §5 R007 (satır 463) · R008 (satır 464)
KANIT     Prompt: `2-6 s: She addresses Nith … Your translator just declared a war.` (başlangıç 2,0 s). R007 süresi 2,4 s → 4,4 s'de biter. R008 `| C06 | 4,0 | NITH | kadraj dışı |`. 6-10 s: `Keep the existing chair behind her and the face anatomy intact. … Nith's reply is an off-screen post-production line after she finishes.` Nem'in ağzının kapalı olduğu yazılmamış.
ETKİ      (a) R008 Nem'in repliğinin 0,4 s içine biniyor (FILM tablosu 1,0 s'ye göre yazılmıştı, prompt 2,0 s'ye kaydı). (b) Nith'in yanıtı kurguda eklenirken kadrajdaki Nem ağzı oynuyor olabilir. Model "yanıtı" kendisi de seslendirebilir.
DOĞDUĞU   metin + kurgu planı
KURAL     Teknik-danışman kontrol listesi, model sesi repliği (a) ve (d) [SÖZLEŞME]
ARIZA     yeni
DÜZELTME  FILM.md R008 başlangıcı 4,0 → 4,8 (kurguda). Prompt: `6-10 s: Keep the existing chair behind her` → `6-10 s: She stands still with her mouth closed, listening; keep the existing chair behind her`. `Nith's reply is an off-screen post-production line after she finishes.` cümlesi sil: ikinci bir ses tarif ediyor. C01'deki röle cümlesi için B9.

### B6 · CİDDİ · C06: kalkarken eller masa kenarında, arkada sandalye
YER       C06 Görsel (satır 301) · Video 0-2 s (satır 306)
KANIT     Görsel: `Both hands lightly brace the broad table edge`. Video: `0-2 s: Use a quiet low-angle camera as Nem completes one controlled rise to her feet.` Aynı promptta `the existing chair behind her`.
ETKİ      Kalkma (T02/T10) ile el-masa teması (T01) aynı 2 saniyede. Orta plandaki avuçlar masa kenarına gömülür ya da kayar. Kalkan bedenin arkasında sandalye kaybolur ya da çoğalır.
DOĞDUĞU   kare + hareket
KURAL     BILINEN_TUZAKLAR §B1 (temas gösterilmez) [SÖZLEŞME] · §B10 (beden/nesne zemine geçme)
ARIZA     T01 · T10
DÜZELTME  Görsel: `Both hands lightly brace the broad table edge, the silver receiver still attached.` → `Her hands are below the crop, the silver receiver still attached.` (C01 ile aynı çözüm). Kalkma 0-2 s'de tek hareket kalır, bu zaten yazılı.

### B7 · CİDDİ · C07: dolu kubbe "tilts / turns" diyor, su düzeyi koruması videoda yok
YER       C07 Video 3-6 s ve 6-10 s (satır 326)
KANIT     `the back of her water dome tilts a few degrees and her shoulders draw back as she leans away` · `while her dome turns slightly away from him`. Su düzeyi cümlesi yalnız Görsel'de (`a constant visible water level`), Video'da yok.
ETKİ      Eğilen ya da dönen dolu kubbede model su yüzeyini sallar, su seviyesi değişir. Ön plandaki flu kubbe yatay kamera kaymasıyla Vekh'in yüzünün üstünden geçebilir. Hepsi aynı 10 saniyede: konuşma + kamera kayması + iki ayrı hareket.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR §B7 · FILM §3 Ishra tanımı: "sabit görünür su düzeyi" [SÖZLEŞME]
ARIZA     T05 · T15
DÜZELTME  `the back of her water dome tilts a few degrees and her shoulders draw back as she leans away` → `her shoulders draw back as she leans away, the dome and its water level staying fixed`. `while her dome turns slightly away from him` → `while her shoulders turn slightly away from him`. İkinci kişi hikâye için şart (T15): evet, tepkisi sahnenin yarısı.

### B8 · CİDDİ · C10 ve C12: asıl plan avuçtan masaya bırakmayı ve avucun kayıp gitmesini kadrajda gösteriyor
YER       C10 Video 3-6 s (satır 384) · C12 Video 3-6 s (satır 422) · "YEDEK" yalnız not satırında (satır 374, 413)
KANIT     C10: `The palm lowers until the octagonal body rests flat on the table surface … and the palm slides away from it`. C12: `The palm lowers until the slab rests flat on the table surface and the palm slides away from it`.
ETKİ      En çok bozulan tür (🔴 92). Cümle yazmak tutmuyor (COUNTED_TURN 7 🔴 / 22 promptta temas cümlesi). Avuç nesnenin altından çekilirken nesne ya ele yapışır ya içinden geçer ya da masaya gömülür. Yedek ancak ilk deneme bozulunca devreye giriyor, bir deneme ve kredi gider.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR §B1 satır 47 (temas anı gösterilmez, öncesi ve sonrası çekilir) [SÖZLEŞME]
ARIZA     T01 · T09
DÜZELTME  YEDEK birincil olsun. Kare K1'i/levhayı masada ve el masa kenarında gösterir. Video yalnız kamera + konuşma + `the pale amber light stays lit`. Bırakma kesmeyle atlanır. Gerek: C10 Görsel `on his open right palm, a hand's width above the table surface, rests` → `on the table surface in front of his right hand rests`. C12 Görsel'de aynı değişiklik. 3-6 s vuruşlarından avuç hareketi çıkar.

### B9 · CİDDİ · C10 ve C12: nesne ile onu tutan yüzey ayırt edilemiyor, ellerin tasarımı yok
YER       C10 Görsel (satır 379) · C12 Görsel (satır 417) · A05 ve A04 kimlik cümleleri (satır 79, 73)
KANIT     C10: `One rigid black hexagonal table` (satır 86) ↔ `a single palm-sized black octagonal body`; ayırıcı yalnız `one pale amber triangular light`. C12: yüz `A frosted amethyst face`, levha `a single flat frosted-purple pentagonal recording slab`, aynı karede ametist yüz ve soluk gümüş-mor koltuk. Orun için `Two arms, substantial but not exaggerated build.`, Silex için `Two arms and a calm upright body` : el, parmak sayısı ve malzeme tarifi yok.
ETKİ      Siyah üstüne siyah ve mor üstüne mor: kenar kaybolur, nesne ele ya da masaya kaynaşır. Elin yapısı hiçbir referansta olmadığı için her kare farklı el uydurur. Aynı eller C23, C28, C75-C83'te de çıkıyor.
DOĞDUĞU   referans (el yok) + kare
KURAL     Teknik-danışman kontrol listesi T01 [SÖZLEŞME]
ARIZA     T01 · T09
DÜZELTME  Kare kapısına iki madde: "el + nesne ayrılıyor mu", "levhanın kenarı ametist yüzden ayrışıyor mu". C10 Görsel'e: `with one pale amber triangular light` → `with one pale amber triangular light, its edges catching a thin gold rim light against the black table`. C12 Görsel'e: `recording slab` → `recording slab with a thin silver edge`. Referans v1 onayında Orun ve Silex'in elleri görünmüyorsa o iki ref için sahibe soru: kare üretiminde el serbest kalacak.

### B10 · CİDDİ · C01: röle cümlesi ikinci ses davet ediyor
YER       C01 Video 5-10 s (satır 209)
KANIT     `5-10 s: After he stops, hold his listening expression and the stable black-hole view. … The altered official relay line is a separate off-screen sound layer added after his original utterance, not a second line spoken by Vekh.`
ETKİ      Modele bir "röle repliği" kavramı veriliyor. Model onu üretip aynı klibe ikinci ses ekleyebilir (R002 4,6 s'de kurguda ekleniyor; çakışırsa klibin 5-10 s'si kullanılamaz). Plan pilotu P18 ölçümü bunu bozar. Bu cümle de "not a second …" biçiminde olumsuz.
DOĞDUĞU   prompt kelimesi
KURAL     ILK_30 §6 + SMOKE P18 pilot ölçümü [SÖZLEŞME]; olumsuz cümle görev yasağı
ARIZA     yeni
DÜZELTME  `The altered official relay line is a separate off-screen sound layer added after his original utterance, not a second line spoken by Vekh.` → `After he stops, the room stays silent except for quiet ventilation.` ("fire" red riski: C01 not satırında R001 kayda planlı, ek bulgu yok.)

### B11 · KÜÇÜK · C01/C07/C10: arkada "panoramic window", C12'de kaburga
YER       C01 Görsel (satır 204) · C07 Görsel (321) · C10 Görsel (379) · C12 Görsel (417)
KANIT     C01 `Through the panoramic window behind him` (Vekh saat 2) · C07 `The panoramic window stands behind him` (Vekh) · C10 `Behind him the curved panoramic window glows` (Orun saat 10) · C12 `Behind Silex are the dark stone-metal ribs` (Silex saat 8). FILM §3: cam baş koltuk Nith'in arkasında.
ETKİ      Aynı salon dört ayrı yön söylüyor. Kesmede pencere konumu sıçrar (kesme sürekliliği). Camın Vekh ve Orun arkasında olabildiği açı varsa kare kapısında doğrulanır.
DOĞDUĞU   kare + metin
KURAL     FILM.md §3 SAHNE DÜZENİ [SÖZLEŞME]
ARIZA     yeni
DÜZELTME  Kare kapısında C01/C07/C10 karesi için "kamera hangi koltuktan bakıyor, cam sağ/sol/arka" notu alınır. C07 ve C10 arkasını `the panoramic window curves behind and beside him`'e çevirmek yeterli.

---
**Kontrol listesi cevapları (risk sütunlu çekimler)**
- T01 el/nesne: C10, C12 temas kadrajda (B8, B9). C06 el-masa teması (B6). Diğerlerinde temas yok.
- T03/T13: C03 vakum, soyut skor; B2'deki cümle düzeltilirse temiz. C02 su sesi (B4).
- T06 okunan yazı: C01-C12'de ekran yok. C04 "source-monitor surface" kapsam dışı (benim listemde değil).
- T05/T09 durum değişimi: Ishra kubbe (B7), K1/K2 ve alıcı tarafı. Tek-panelli planlı referans, panel sayfası yok (plan kararı, NOTLAR'da).
- T15: C07'de iki kişi, ikincisi şart. Diğer riskli çekimlerde tek yüz.
- Açılış C01-C03: C03 kalabalık + hareket (B2), C02 yakın plan şeffaf kubbe + yüz (B3, B4); C01 yavaş itme, düşük risk.
- T08: yok. T02/T10: C06 kalkma (B6), kısa ve tek hareket.
- Model sesi (a)-(e): (a) C06 ve C01 için B5/B10; (b) C07 iki konuşan değil, Ishra kadraj dışı ve arkadan, doğru; (c) yedek plan FILM §5 (satır 632-637) mevcut, bulgu yok; (d) R008 çakışması B5, klibin son saniyesine düşen replik yok; (e) ortam cümlesi C02'de ayrışıyor (B4).
- Mod ↔ model: tüm çekimler Frames to Video (kare + sesli), malzemeden video/uzatma yok. Bulgu yok.
- Red riski: milliyet yok, bedenden çıkarma eylemi yok. C03 "weapon lights" ve "battle" kelimeleri listedeki şiddet/ölüm kelimeleri değil, B2'de izlenecek. Büyük harfli jeton ve çekim kodu yok.

KORU: C01-C07 sesli çekimlerde kimlik cümleleri video promptunda tekrarlanmıyor, kare onayı yeterli. C07 Ishra arkadan yüz tarifsiz yazılmış (doğru, dudak riski yok).

F5'e not (film içi): C04 de aynı kaymaya sahip. Nem'in repliği 2,0 s'de başlayıp 4,0 s'de bitiyor, R005 Silex 3,6 s'de, 0,4 s çakışma; R005 3,6 → 4,4 s. Ayrıca B8/B9 aynı riski taşıyan sonraki çekimler: C23 (K2 elde), C28 (K1 kendine çeker), C59 ve C68 (blaster), C75-C83 (K1/K2 el-nesne). Ishra kubbe riski: C14, C19, C34, C44, C57, C67, C71, C87, C93. Nem'in 11 çekimlik kalkma sonrası ayakta durumu C06 karesine bağlı.

KANIT eksiği: kare/ham yok, Flow'da henüz üretim yapılmamış (Durum ⬜); bu yüzden hareket için "görülmedi".

ÖZET     ÖLÜMCÜL 1 · CİDDİ 9 · KÜÇÜK 1
KARAR    TUR KAPANAMAZ (ÖLÜMCÜL: B1)
GİRDİ    uretim_hatti/ELESTIRI_PROTOKOLU.md, BILINEN_TUZAKLAR.md (§A-§D), yatay_16_dk_filmler/BLACK_ACCORD/PROMPTLAR/G01.md (tamamı), BLACK_ACCORD/FILM.md §1 başı, §3, §4 C01-C14 satırları, §5 R001-R020, §6 ses planı ve yataklar.
YAPILMADI ARIZA_LISTESI.md T bölümü, ILK_30_SANIYE_KILAVUZU §6 ve GECIS_VE_SES_SUREKLILIGI.md açılmadı: madde adları (T01 vb.) ve kuralları görev tanımından ve FILM.md'den alındı. Kare, ham video ve ses yok (üretim başlamadı).
