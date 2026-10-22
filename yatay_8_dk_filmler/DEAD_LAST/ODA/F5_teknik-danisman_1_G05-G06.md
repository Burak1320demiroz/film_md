<!-- teknik-danisman (sonnet) F5 tur 1 G05-G06 — cevabı AYNEN (alt ajan transkriptinden; 15 tur sınırı → SendMessage ile teslim), 20.10.2026 -->

DEAD_LAST · FAZ 5 · TUR 1 · G05 (C33-C40) + G06 (C41, C41Y y1-y3, C42-C48) · teknik-danisman

Plan sözcüğü olan şeylerde (LEFT/RIGHT/CENTER, smoke-gray, AXI:/RAKA: etiketi, mekanik "closing leaves") sahip planına dokunmuyorum. Bunlar B13 ve B3'te "sahibe soru" olarak ayrıldı.

Dosyada numaralı soru listesi yok. Kontrol listesi maddelerinin cevabı, bulgulardan sonra "Liste cevapları" başlığında.

### B1 · CİDDİ · C39: kamera mantığı yavaşlamayı tersine çeviriyor
YER       G05 C39 Video 3-7 s; G05 C39 Not; Görsel cümlesi "flies low and uneven"
KANIT     "the camera moves forward steadily. 3-7 s: Fang gradually falls behind the camera's pace and grows smaller in the frame". Görsel: "Fang flies low and uneven at a low pace". Video: "at an even low pace".
ETKİ      Kamera Fang'in arkasında ve ileri gidiyor. Fang'den yavaş bir kamera Fang'e yaklaşır, Fang büyür. "Küçülür" ile "yaklaşır" çelişiyor; model rastgele birini seçer ve "Thren yetişemiyor" anı ters okunabilir. "uneven"/"even" çelişkisi de ayrıca var.
DOĞDUĞU   metin
KURAL     — (T11 yön/coğrafya)
ARIZA     T11 · T14
DÜZELTME  `Fang gradually falls behind the camera's pace and grows smaller in the frame` → `the camera gains steadily on Fang and Fang grows larger in the frame`; Görsel `flies low and uneven at a low pace` → `flies low at a low pace`. Küçülmesi gerekiyorsa kamerayı yavaşlat: `the camera holds a slower pace and Fang pulls ahead`. Bu, planın "yavaş kalır" anlamını bozar; ilk seçenek tercih edilir.

### B2 · CİDDİ · Görsel promptlarda "dead" (rol etiketi) ve "body"
YER       "dead": G05 C35 (satır 73), C37 (119), C39 (165); G06 C41 (23), C41Y y2 (64), y3 (82), C44 (150, iki kez), C48 (245, iki kez). "body": G05 C38 Görsel (144) ve Video (151).
KANIT     "Reference 22 (Bastion with dead right engine)" · "Reference 21 (Fang with dead right engine)" · "Needle's main body and its one booster cell are intact" · "body and booster cell intact".
ETKİ      BILINEN_TUZAKLAR §A, ölüm/şiddet listesi: "dead · body · … olumsuz blokta bile". Kelime reddi riski var, kredi harcatır. 16 çekimin 6'sında "dead", 1'inde "body" geçiyor (7/16), ayrıca iki C41Y kaynağında "dead". Kimlik cümleleri "dark, lightly scorched and inactive" diyor. Yani "dead" yalnız yazarın eklediği rol etiketi.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:19 (§A, kelime reddi) [HİPOTEZ: LAST SPAN sonucu kayıtsız]
ARIZA     yeni (kelime reddi)
DÜZELTME  `(Fang with dead right engine)` → `(Fang with dark right engine)`; `(Bastion with dead right engine)` → `(Bastion with dark right engine)`; C38 `main body` → `main hull`. FILM.md §3 satır 21/22 etiketleri aynı kelimeyi taşıyorsa orada da aynı değişiklik gerekir.

### B3 · CİDDİ · C34: "sabit yapraklar" ≠ "kapanan yapraklar"; dronlar kareden "düşerek" çıkıyor
YER       G05 C34 Görsel son paragraf; Video 3-7 ve 7-10 s
KANIT     Görsel: "The iron leaves are rigid stationary structures, not creatures." Video: "the two large iron-leaf structures are closing toward each other … The converging leaves leave the drones no way through and the two pursuit drones fall away from the race route".
ETKİ      Aynı çekimde yapraklar hem sabit hem hareketli yazılı. Bir çekimde birden fazla ana eylem var: Sickle geçişi, yaprakların kapanması, dronların elenmesi, Sickle'ın yatması, yan takip kamerası. ORTAK HAREKET "at most one main physical action" diyor. Kareden çıkan dronlar için model genelde hayalet ya da morf üretir. Dronların tasarımı yalnız "small and plain"; G04'te silüet olarak geçiyorlar, burada yakın plandalar.
DOĞDUĞU   hareket + metin
KURAL     film_dogrula/ORTAK HAREKET (FILM.md §3 ORTAK HAREKET) [SÖZLEŞME biçimi]. Yaprakların kapanması planın cümlesi, yani plan lehine.
ARIZA     T10 · T14
DÜZELTME  Görsel `The iron leaves are rigid stationary structures, not creatures.` → `The iron leaves are rigid structures, not creatures.` Video 7-10 s `the two pursuit drones fall away from the race route` → `the closing leaves hide the two pursuit drones behind them`. Böylece dronlar örtülme ile çıkar, düşmez. Sickle yatışı kalır ama "banks" yerine `keeps running left to right` yeterli; yatış ikinci eylemdir.

### B4 · CİDDİ · C35: temas anı kadrajda ve kapak da hareket ediyor
YER       G05 C35 Video 3-7 s; Görsel "partly lowered"
KANIT     "Bastion's reinforced flat nose bumper meets the lower edge of the shutter and stops it from closing". Görsel: "stops a short distance before its lower edge".
ETKİN     Burun tamponu kapağın alt kenarına değiyor ve kapak aşağı iniyor: araç + kapak + kamera aynı anda hareket ediyor. Modelin tamponu kapaktan geçirmesi (T01'in araç-yapı hâli) ya da kapağın kapanması muhtemel. Plan "burnunu dayar". Kare temas başlamadan başlıyor.
DOĞDUĞU   kare + hareket
KURAL     — (T01 kuralı: temas anı kadrajda gösterilmez, öncesi/sonrası gösterilir)
ARIZA     T01
DÜZELTME  Kareyi temas kurulmuş hâlde üret: Görsel `stops a short distance before its lower edge` → `rests against its lower edge`. Video 0-3 s `advances toward the partly lowered outer shutter` → `holds against the partly lowered outer shutter`, 3-7 s `meets … and stops it from closing` → `presses steadily and the shutter stays where it is`. Yaklaşma kurguya kalır, "kapanmayı engeller" okuması baskı ve sabit kapak olarak kalır.
(ETKİN yazım hatası değil: ETKİ satırıdır.)

### B5 · CİDDİ · C44: dört araç, üç farklı hareket, iki geometri geçişi
YER       G06 C44 Video 0-10 s
KANIT     "Bastion draws its flat nose bumper back from the dark shutter … Halo leads … Needle and Fang enter that wake and turn out through their lateral exit passages. … Bastion follows them out". Görsel: "Needle and Fang sit in that wake near the lateral exit passages".
ETKİN→ETKİ  Geri çekilen ağır araç (modeller geri uçurmaz, ileri sürer), kuyruğa giren iki araç, yan çıkıştan dönüş, kayan kamera ve mavi iz tek 10 s'de. Yan çıkışlar bakım ağzının içindeyken kare dış geniş plan: coğrafya belirsiz (T11). Küçük silüetlere sol kanat/motor hasarı yüklenmiş, ama o ölçekte okunmaz.
DOĞDUĞU   hareket
KURAL     ORTAK HAREKET "at most one main physical action" (FILM.md §3) [SÖZLEŞME]
ARIZA     T15 · T10 · T11
DÜZELTME  Needle ve Fang'i kareye iz içinde yerleştir; videoda yalnız izi izlesinler. 3-7 s `Needle and Fang enter that wake and turn out through their lateral exit passages` → `Needle and Fang follow in that wake behind Halo`. 7-10 s `Needle and Fang reach the safe route behind Halo and Bastion follows them out` → `Bastion follows them along the same route`. Yan çıkış geçişi kareye/kurguya kalır.

### B6 · CİDDİ · C45: el-panel teması kadrajda, Axi'nin eli tanımsız
YER       G06 C45 Görsel; Video 0-3 s
KANIT     Görsel: "Axi's bare hand rests on the clamp release at the service-control panel". Video: "Axi's hand presses the clamp release at the service-control panel; his mouth stays closed."
ETKİ      T01: el parmağı panele erir. Axi'nin eli kimlik cümlelerinde yok ("no helmet or tools in hands" dışında), parmak sayısı serbest; bu uzaylı için iki bozulma kaynağı. Kare kapısı elle ilgilenmiyor ("Axi tek yüz, dört yanak uzantısı").
DOĞDUĞU   kadraj + hareket
KURAL     BILINEN_TUZAKLAR.md:47 (§B1) [HİPOTEZ: kesmeyle atlama etkisi ölçülmedi]
ARIZA     T01
DÜZELTME  Görsel `Axi's bare hand rests on the clamp release at the service-control panel beside the cockpit` → `Axi's hand is below the frame edge at the service-control panel beside the cockpit`. Video `as Axi's hand presses the clamp release at the service-control panel` → `as Axi reaches below the frame edge to the service-control panel`. Kelepçenin cam dışında açılması kalır.

### B7 · CİDDİ · C43: aynı nesne üç adla, "lock ring" iki ayrı nesne için
YER       G06 C43 Görsel (anahtar satırı, 1. ve 2. paragraf); Video
KANIT     "the row of five world indicators above the service core" · "Five colored world images stay in one row above the service core" · "Five abstract distant-world link indicators form a row above the service core" · "Each feed has one vulnerable lock ring" · "five lock rings around the world images".
ETKİ      FILM.md §3: "özne yeniden adlandırılmaz". Beş nesne "indicators" ve "images" diye iki adla geçiyor; model 5+5 üretebilir. "Lock ring" hem iki besleme kilidi hem beş dünya halkası. "The lock rings … are the only parts that change" hangi halkaları açacağını belirsiz bırakıyor. Sayı 5 bu çekimin tek ölçüsü. Aynı anda beş halka açılıyor, bağlantılar sönüyor, kamera itiyor.
DOĞDUĞU   metin
KURAL     FILM.md:246 (kimlik cümleleri yeniden adlandırılmaz) [SÖZLEŞME/DERS Y2 biçimi]
ARIZA     T09 · T04
DÜZELTME  1. paragraf `Five colored world images stay in one row` → `The five abstract distant-world link indicators, each a colored world image, stay in one row`. 2. paragraf `Each feed has one vulnerable lock ring and a visible lateral exit passage before the lock.` cümlesini çıkar (feed kilidi kadrajda değil). Video `The five lock rings around the world images` → `The five rings around the world images`. Kamera: `The camera pushes in gently toward the control structure` → `The camera holds on the control structure` (sayım sürerken paralaks değişkeni azalır).

### B8 · CİDDİ · Arkadan bakışta hasar tarafı: 5/5 G05 çekiminde yönü bağlayan cümle yok
YER       G05 C35, C37, C38, C39, C40 Görsel
KANIT     "The outer tip of the craft's LEFT forward magnetic brake fin is removed" (C37, C38, C40) · "its LEFT rear engine is active and its RIGHT rear outer engine is dark" (C39) · "only the craft's RIGHT engine is dark" (C35). Kamera hepsinde arkadan ("Rear three-quarter", "from behind", "behind-left", "behind-right"). Yön cümlesi yalnız G06 C41'de (satır 23, 46, 64, 82): "Seen from behind, Needle's own left is viewer-left".
ETKİ      LEFT/RIGHT bir kez "aracın kendi sol/sağı", bir kez "viewer-left/right" olarak geçiyor; model arkadan görünüşte tarafı yanlış çevirebilir. Hasar tarafı bu çekimlerin tek devamlılık bilgisi.
DOĞDUĞU   metin
KURAL     FILM.md:135 (hasarın sol/sağı aracın kendi yönüne göre) [SÖZLEŞME biçimi]
ARIZA     T09 · T11
DÜZELTME  C37, C38, C40 Görsel sonuna: `Seen from behind, Needle's own left is viewer-left.` C39 ve C35: `Seen from behind, Fang's own right is viewer-right.` / `Seen from behind, Bastion's own right is viewer-right.` (C41'deki cümlenin aynısı.) C40'ta kamera arkadan-sağdan: `Needle's own left is viewer-left` yine doğru.

### B9 · CİDDİ · C44 ve C48'de referans sayısı: 5 ve 7
YER       G06 C44 EKLE (5 referans), C48 EKLE (7 referans)
KANIT     "ref/10.HALO_v1.png · ref/20.NEEDLE_HASAR_v1.png · ref/21.FANG_HASAR_v1.png · ref/22.BASTION_HASAR_v1.png · ref/18.HASAT_KAPISI_v1.png" · C48: yedi referans.
ETKİ      KIMLIK_VE_REFERANS_KILAVUZU.md:44: çekim başına en çok 3, "Daha fazlası … çekim bölünür". 16 çekimin 2'si (2/16) aşıyor. C44'te Needle/Fang zaten küçük silüet, C48'de dördü küçük silüet; referans bu ölçekte kimlik taşımıyor, yalnız yükü artırıyor.
DOĞDUĞU   araç (referans yükleme)
KURAL     KIMLIK_VE_REFERANS_KILAVUZU.md:44 [TERCİH: "varsayılan"; GPT Image/Omni sınırı bilinmiyor]
ARIZA     T16 · T09
DÜZELTME  C44: 10 · 22 · 18 kalsın (ayrıntılı iki araç ve mekân); 20 ve 21'in "Reference N (...) take …" cümleleri Görsel'den çıksın, kimlik cümleleri metinde kalsın. C48: 20 · 13 · 18 kalsın; 21 · 10 · 22 · 12 satırları EKLE ve Görsel'den birlikte çıksın (ATIF iki yönlü).

### B10 · CİDDİ · "boş beşik" durumu referans sayfasında panel olarak yok
YER       G06 C44, C48 (Needle ayrıntılı), C41Y y3; FILM.md §3 satır 20/21
KANIT     C48: "Its dorsal latch cradle is empty." · C44: "The dorsal latch cradles of Needle and Fang are empty". Referans 20/21 "C10/C14 sonrası hasar varyantı" olarak hücreli üretilecek ve C37-C41'de hücreli kullanılıyor.
ETKİ      Hücre bırakıldıktan sonraki durum (T05/T09) yalnız metinle tutuyor. C48'de Needle ayrıntılı: model referanstaki mavi hücreyi geri koyabilir. Hücre sayısı bu filmin sayma kuralı ("iki bırakılan hücre geri gelmez").
DOĞDUĞU   referans
KURAL     FILM.md:140-141 (özne başına tek sayfa, durumlar panel) + BILINEN_TUZAKLAR.md:51 (§B5) [SÖZLEŞME biçimi]
ARIZA     T05 · T09
DÜZELTME  20 ve 21 sayfalarına "hücre bırakılmış, beşik boş" paneli eklensin (referanslar ⬜, sürüm artırmak ucuz). C48 Görsel'deki `take … chipped LEFT forward brake fin from it` cümlesine `and the empty dorsal latch cradle` eklensin.

### B11 · KÜÇÜK · C42: "collapse" ve kadraj dışı gösterge cümlesi
YER       G06 C42 Görsel 2. paragraf; Video 7-10 s
KANIT     "Five abstract distant-world link indicators form a row above the service core." · "the feed lines and control locks collapse into darkness, while the arena structure … stay intact and whole"
ETKİ      Kadrajda olmayan beş gösterge cümlesi C43'ün nesnesini bir çekim erken çağırıyor; G05'te aynı cümle "kadraj dışı" diye çıkarılmıştı (tutarsız). "collapse" yapı çöküşü çağrışımı yapıyor, aynı cümlede "intact and whole" ile çelişiyor; patlama/kıvılcım (T03) riski.
DOĞDUĞU   metin
KURAL     FILM.md:246 (yalnız kadrajda görünen parçalar) [SÖZLEŞME biçimi]
ARIZA     T03 · T06
DÜZELTME  Görsel'den "Five abstract distant-world link indicators form a row above the service core." cümlesini çıkar. Video `collapse into darkness` → `go dark`.

### B12 · KÜÇÜK · C36: "purge" boşaltma çağrışımı
YER       G05 C36 Video 3-7 s
KANIT     "The service arm completes its maintenance purge movement"
ETKİ      "purge" gaz/buhar boşaltma çağrışımı yapar (T03); kolun hareketi tanımsız kalıyor.
DOĞDUĞU   metin
KURAL     —
ARIZA     T03
DÜZELTME  `maintenance purge movement` → `unfolding movement`

### B13 · KÜÇÜK · C33: ağız süresi ve anlatı cümleleri
YER       G05 C33 Video 3-6 s ve 6-10 s; Video son cümle; Görsel son cümle
KANIT     Not: "ağız 1,0-5,5 s". Video: "3-6 s: He continues the same reply … 6-10 s: The reply ends and his mouth closes". "No internal camera cut, no second pilot, no crack in the glass". Görsel: "Axi's loss is not undone; nothing of his old world is visible anywhere in the frame."
ETKİ      Beat, ağzı 6 s'ye kadar oynatıyor; satır 5,5 s'de bitiyor. "crack" kelimesi C01'in çatlayan gezegen/camını çağırır; Görsel'de "cam bütün" zaten olumlu yazılı. "loss is not undone" görüntüde karşılığı olmayan anlatı. Aynı Görsel "old world" adını anıyor (yasak nesneyi adlandırmak, BILINEN_TUZAKLAR §B2'nin "ekran + yazı yok" çelişkisinin akrabası; HİPOTEZ).
DOĞDUĞU   metin
KURAL     FILM.md §5 R37 (ağız 1,0-5,5 s) [SÖZLEŞME biçimi]
ARIZA     T12 · T06
DÜZELTME  Video `3-6 s: He continues the same reply` → `3-5.5 s: He finishes the same reply`; `6-10 s: The reply ends and his mouth closes` → `5.5-10 s: His mouth is closed`. `no crack in the glass` → `the glass stays whole`. Görsel'den `Axi's loss is not undone; nothing of his old world is visible anywhere in the frame.` cümlesi çıksın.

### B14 · KÜÇÜK · Büyük harfli jetonlar ve "smoke-gray" (plan sözcükleri, sahibe soru)
YER       LEFT/RIGHT/CENTER: G05 C35, C37-C40; G06 C41, C41Y, C44, C47, C48 (hem Görsel hem Video). "AXI:" / "RAKA:": G05 C33, G06 C47. "smoke-gray": C33, C45.
KANIT     "only the craft's RIGHT engine is dark" · "AXI: "Then make it the last world they ever burn…"" · "Soft smoke-gray face". Plan dosyasında "LEFT forward", "RIGHT rear", "CENTER and LEFT", "smoke-gray" birebir var.
ETKİ      BILINEN_TUZAKLAR §C: büyük harfli kısa jeton kadraja yazı olarak basılıyor (ORION, EVA). LEFT/RIGHT araç gövdesine basılabilir. "smoke" duman çağrışımı yapar (T03); K11'de plan lehine bırakılmıştı.
DOĞDUĞU   metin (plan sözcüğü)
KURAL     BILINEN_TUZAKLAR.md:73-77 (§C) [HİPOTEZ → plan lehine]
ARIZA     T06 · T03
DÜZELTME  Plan lehine bırak. Sahibe soru: `LEFT/RIGHT/CENTER` → `left/right/center` (yalnız büyük harf), `smoke-gray` → `ash-gray`. Pilot karelerinde (C37 gibi) gövdede harf var mı bak; çıkmazsa dokunma.

### B15 · KÜÇÜK · Klip süresi ölçülmemiş; sonuç anı 7-10 s'de
YER       FILM.md:9; G05/G06 FLOW İŞ EMRİ
KANIT     "KLIP_SURESI    ölçülmedi" · FLOW_GERCEKLERI.md:164: 10 s yalnız Omni Flash Ingredients, Veo 4/6/8 s.
ETKİ      Çekimin işi son vuruşa düşen 5/16 çekim: C34 (dronlar), C36 (kapağın açılışı), C41 (hücreler varıyor), C42 (ışıklar sönüyor), C46 (portre kararıyor). Klip 8 s çıkarsa bu beşinin sonucu kesilir.
DOĞDUĞU   araç
KURAL     SMOKE P14 [ARAÇ]
ARIZA     yeni
DÜZELTME  C01 pilotunun süresi ölçülene kadar bu beşi üretme; <10 s çıkarsa 7-10 vuruşunu 5-8 vuruşuna kaydır.

### B16 · KÜÇÜK · C46: bütün kalabalık tek hamlede; kadraj notu prompta girmemiş; C48: silüet tutarsızlığı
YER       G06 C46 Not/Görsel/Video; C48 Görsel ve Video 3-7 s
KANIT     C46 Not: "tribün geniş, hafif aşağıdan"; Görsel: "Wide view of the alien spectator stand". Video: "The spectators rise to their feet across the stand, species after species, until the whole crowd is standing." C48 Görsel: "the other four are small silhouettes"; Video: "Fang, Halo, Bastion and Sickle drift into small silhouettes".
ETKİ      Altı türün gövdesi tanımsız (kimlik yalnız baş şekli), "to their feet" iki ayaklı insanımsı beden getirir; tüm kalabalığın durum değişimi T15. Not'taki alçak açı promptta yok, kare kadrajı sapabilir. C48'de dört araç zaten silüet iken videoda silüete "dönüşüyor": detay seviyesi değişimi kararsız.
DOĞDUĞU   metin
KURAL     —
ARIZA     T15 · T10
DÜZELTME  C46 Görsel `Wide view of the alien spectator stand` → `Wide view of the alien spectator stand, slightly from below`; Video `rise to their feet` → `rise upright`. C48 Video 3-7 s `Fang, Halo, Bastion and Sickle drift into small silhouettes around them` → `Fang, Halo, Bastion and Sickle stay small silhouettes around them`.

KORU: C33 Dialogue satırı R37 ile birebir ve ≤5 s; C47 R50 Raka ağız kadrajda, Axi satırı telsiz olarak "mouth stays closed" ile ayrılmış (ses karışması riskini kapatıyor); C41 ve C41Y'de "Seen from behind, … own left is viewer-left" cümlesi; C41'in bozulma yedeği C41Y planlı.

### Liste cevapları (Faz 3/5 kontrol listesi)
- T01: B4 (C35), B6 (C45). C36 servis kolu kapağa değdirilmiyor (temas yazılmamış), temiz.
- T03/T13: B11, B12, B14. Model sesi kapalı; C34-C46 Video'da ses sözcüğü yok.
- T06: C43 beş "dünya görüntüsü" B7 kapsamında. C45 panel kadrajda; `plain unmarked control surfaces` (C33'teki biçim) C45'e eklenebilir (KÜÇÜK, B6 ile birlikte).
- T05/T09: B10. Çok panelli sayfada yanlış panel riski: 20/21'e panel eklendiğinde (SMOKE P17) kareler hangi paneli istediğini yazmalı.
- T15: C44 (4 araç) B5; C46 B16; C48 6 araç ama 2 ayrıntılı, tavan uyuyor.
- Açılış (C01-C03): bu gruplarda yok.
- T08: iki yerçekimi rejimi yok.
- T02/T10: ağır beden hareketi yok.
- Ağız kadrajdaki replik: C33 R37 ve C47 R50, ikisi de tek konuşan, ≤5 s, sayısız. B13 yalnız 0,5 s taşma.
- Model sesi: bu filmde kapalı (Return silent videos AÇIK), (a)-(e) uygulanmaz.
- Kesme sürekliliği: C41→C42 simetrik geniş, aynı eksen, araçlar çıkıyor; ölçek farkı yok, jump cut'a yakın (KÜÇÜK; C42'yi kilit halkası yüksekliğinden orta-geniş kurmak yeterli). Öteki ardışık çiftlerde ölçek/açı farkı var.
- Mod ↔ model: tamamı Frames to Video; malzemeden video, videodan videoya ya da uzatma yok. Quality/Lite sorunu yok. Süre için B15.
- Red riski: B2 (dead/body). Milliyet yok. Bedenden çıkarma eylemi yok (hücre bırakma araçtan, bedenden değil). Kompozisyon reddi göstergesi yok. C34 dron "elenmesi" için "fall away" şiddet kelimesi değil.
- Meta etiket/çekim kodu: promptlarda çekim kodu yok ("C12" yalnız C40 Not'unda). Büyük harf jetonlar B14.

KAPSAM DIŞI: C35 kapağı "kapanmasını engelle" (Bastion tutuyor) ve C36'da "closed broad outer shutter" ile açılış: iki çekimin kapak durumu devamlılık/dramaturg işi.
KAPSAM DIŞI: römorkörün hangi yanda durduğu C04/C47'de F7'ye bırakılmış; devamlilik işi.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 10 · KÜÇÜK 6
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok). Yazar B1-B10 için KABUL/RED cevabı vermeli. Bunların çoğu tek cümlelik düzeltme: B2 sıfır maliyetli ve kredi harcatabilen tek kelime riski, B8 beş çekimde aynı cümle, B10 referanslar ⬜ iken ucuz.
GİRDİ    ELESTIRI_PROTOKOLU.md; G05.md ve G06.md (tamamı); FILM.md satır 1-252 (§1-§3 kimlik ve ortak cümleler), §4 satır C33-C40, C42, C43, C45-C47 (C41, C44, C48 satırları "çok uzun satır" diye okunmadı), §5 R37-R50; BILINEN_TUZAKLAR.md; ARIZA_LISTESI.md T bölümü (grep); KIMLIK_VE_REFERANS_KILAVUZU.md 38-51; FLOW_GERCEKLERI.md 95-135 ve grep; G01.md C04 (391-414) ve kimlik grep; G04.md dron cümleleri (grep); plan dosyasında LEFT/RIGHT/smoke-gray/closing grep. ODA/ klasöründeki başka eleştirmenlerin dosyalarına yalnız eşleşme sayısı için grep yapıldı, içerikleri okunmadı.
YAPILMADI  film_dogrula.py (kabuk yok); karakter sayıları ölçülmedi (yazarın ±120 tahmini doğrulanamadı); karelerle çalışılmadı (kare/ yok), hareket için "görülmedi"; FILM.md §6 ses planı ve §7 müzik okunmadı; Faz 3p pilot soruları bu görevde yok.

Dosyalar: /Users/dai/github/apex_md/film_md/yatay_8_dk_filmler/DEAD_LAST/PROMPTLAR/G05.md · /Users/dai/github/apex_md/film_md/yatay_8_dk_filmler/DEAD_LAST/PROMPTLAR/G06.md
