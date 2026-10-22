<!-- teknik-danisman (sonnet) · F5 tur 1 · eser PROMPTLAR/G05-G08 (ilk sürüm) · risk sütunu dolu 34 çekim · 18.10.2026 · ajan cevabı aynen -->

TEKNİK DANIŞMAN · BLACK_ACCORD · Faz 5 tur 1 · G05-G08 (risk sütunu dolu 34 çekim)

Bu fazın dosyasında numaralı soru listesi yok. Ajan kontrol listesindeki iki soruyu (riskli an hâlâ isteniyor mu; meta etiket, büyük harfli jeton, çekim kodu var mı) her çekim için cevapladım.
- Meta etiket ve çekim kodu: yok. G05-G08'in 96 Görsel/Video bloğunu tarattım; blok gövdelerinde C/K/R/A kodu, büyük harfli jeton ve başlık satırı bulunmadı. Notlar promptun dışında duruyor.
- Riskli an: 34 çekimin çoğunda hâlâ isteniyor ve YEDEK ancak notta duruyor. Ayrıntı B1-B14'te, çekim bazında özet en altta.

KORU:
- Alıcısı çıkmış çekimlerde Reference cümlesi alıcıyı almıyor: `take his face and armour from it` (G08 C86, C95), `take her face and coat from it` (G07 C74/C79/C81). Referans sayfasında alıcı takılı göründüğü için bu doğru önlem.
- Kadraj dışı yanıt promptta üretilmiyor ve kadrajdaki ağız olumlu cümleyle kapatılıyor (G08 C85 `Every mouth except Nem's stays closed`; C92-C94 `No other voice speaks`).
- Her videoda aynı oda sesi cümlesi birebir (`quiet chamber ventilation and distant table resonance`), dolayısıyla oda tonu kayması riski düşük.

### B1 · CİDDİ · C59 tek klipte dört el durumu
YER       G05.md:219 (Video), G05.md:214 (Görsel); C59 0-10 s
KANIT     `his open right hand slides from the table edge down to the holstered blaster at his right hip. 3-7 s: His right hand draws the compact dark blaster from the holster and brings it up, turning the barrel across the table … his index finger resting along the side of the barrel`
ETKİ      Kılıfa temas, silahı kılıftan çekme, kaldırıp çevirme ve parmak konumu 7 s içinde aynı elde ardışık istenmiş. Bu, kayıtlı en sık arıza olan el-nesne kaynaşmasının en ağır hâli.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:47 (§B sıra 1: temas anı gösterilmez, kesmeyle atlanır) [HİPOTEZ, ölçülmüş vaka, kapı değil]; FILM.md:384 risk sütunu T01 [ARAÇ]
ARIZA     T01
DÜZELTME  `, his index finger resting along the side of the barrel,` → sil (ek parmak durumu). İkinci denemede notun kendi YEDEK'i: kare silahı kılıfta bırakır, video çekmeden önceki bakış ve uzanışla biter. Bu seçenek B9'daki Flow iş emri satırına yazılmalı.

### B2 · CİDDİ · C60 adım ve parmakları açık ellerin kameraya kalkması
YER       G05.md:238 (Video), G05.md:233 (Görsel); C60 0-3 s
KANIT     `Nem takes one step to the middle of the frame and both of her hands rise to chest height, palms open and fingers spread toward the camera` · kare: `her arms relaxed at her sides`
ETKİ      Kameraya doğru açık parmaklar kısa mesafeden en çok parmak sayısı bozan duruş. Aynı anda adım ve konuşma var. Bel üstü kadrajda adım "kayan ayak" arızasına gider, kare ile video arasındaki fark da iki hareket.
DOĞDUĞU   kare + hareket
KURAL     BILINEN_TUZAKLAR.md:47 [HİPOTEZ]; ARIZA_LISTESI.md:53 (T10) [ARAÇ]
ARIZA     T01 · T10
DÜZELTME  Kare: `her arms relaxed at her sides` → `both open hands raised to chest height, palms outward, fingers together`. Video: `takes one step to the middle of the frame and both of her hands rise to chest height, palms open and fingers spread toward the camera` → `holds both raised open hands steady at chest height`. "Hedef çizgisine girer" kesmeyle (C59→C60) atlanır.

### B3 · CİDDİ · C61 pilot: alıcı çıkarma, avuç çevirme ve "kendi dilinde"
YER       G06.md:27 (Video); C61 0-8 s
KANIT     `lifts the thin silver receiver tab away from it, and lowers it to rest on the table beside her hands … she speaks to him calmly in his own language … Her two open palms turn upward on the table edge as she speaks.`
ETKİ      Üç ayrı durum var: şerit şakaktan çıkıyor, masaya iniyor, avuçlar dönüyor. Üstüne `in his own language` modele Türkçe ya da uydurma dil üretme izni veriyor. Tutan sonuç da yabancı bir sesle gelirse R110'un İngilizce dublaj katmanı bozulur.
DOĞDUĞU   metin + hareket
KURAL     BILINEN_TUZAKLAR.md:21 (bedenden çıkarma, "eylem değişti" çözümü) [HİPOTEZ, ölçülmüş vaka]; FILM.md:638 (replik videoda birebir İngilizce) [SÖZLEŞME]
ARIZA     T01 · T09
DÜZELTME  `speaks to him calmly in his own language, in a precise steady adult female voice` → `speaks to him calmly in a precise steady adult female voice`. `Her two open palms turn upward on the table edge as she speaks.` → sil. "Kendi dilinde" izleyiciye R110'un "VEKH'S LANGUAGE" etiketi ve kurgu ile verilir.

### B4 · CİDDİ · C67 alıcı çıkarma kubbe yuvasından, pilot kapsamıyor
YER       G06.md:141 (Video); C67 5-10 s
KANIT     `her right hand rises from below the frame to the external socket at the right side of the dome and lifts the small silver receiver out of it`
ETKİ      C61 pilotu tek şakaktaki bir şeridi sınıyor. Burada el, su dolu saydam bir başlığın yanına uzanıyor; bu "kask durum değiştiriyor" kalıbı (T05). Model başlığı ya da suyu oynatırsa tek öznede iki yaşam desteği durumu çıkar.
DOĞDUĞU   hareket + referans
KURAL     BILINEN_TUZAKLAR.md:21 (kask çıkarma reddi, çözüm "kimse bir şey çıkarmıyor") · :51 (§B sıra 5, kask/ekipman kayması) [HİPOTEZ, ölçülmüş vaka]
ARIZA     T05 · T01
DÜZELTME  Kare: `Her hands are below the crop.` → `Her right hand, beside the dome, holds the small silver receiver between thumb and finger; the external socket at the right side of the dome is empty.` Video 5-10 s: `her right hand rises from below the frame … lifts the small silver receiver out of it` → `her right hand lowers the small silver receiver out of frame toward the table`. Çıkarma anı kesmeyle atlanır; kubbe ve su dokunulmadan kalır.

### B5 · CİDDİ · C68 iki el eylemi aynı klipte, üç figür
YER       G06.md:160 (Video), G06.md:155 (Görsel); C68 0-10 s
KANIT     `Vekh's right hand lowers the compact dark blaster toward the table … 7-10 s: Silex's right hand rises to its right temple, lifts the thin silver receiver away, and lowers it onto the table beside the flat frosted-purple pentagonal recording slab` · kare: Nith "soft out-of-focus ivory silhouette"
ETKİ      İki kişi, iki el-nesne teması ve ikisi de masa üzerinde küçük nesne yanında (blaster, şerit, K2 levha). Üçüncü figür flu da olsa klon ya da kimlik karışması riski taşıyor. Konuşan Vekh, hareketli Silex'in ağzı kapalı kalmalı.
DOĞDUĞU   hareket + kadraj
KURAL     FILM.md:393 risk sütunu `T01 iki el eylemi` (plan: kesmeyle sadeleşir) [SÖZLEŞME, plan]; BILINEN_TUZAKLAR.md:47 [HİPOTEZ]
ARIZA     T01 · T15
DÜZELTME  Notun YEDEK'i birincil olsun. Video 7-10 s: `Silex's right hand rises to its right temple, lifts the thin silver receiver away, and lowers it onto the table beside the flat frosted-purple pentagonal recording slab, Silex's mouth seam staying closed and its facets fixed.` → `Silex's mouth seam stays closed and its facets stay fixed as the gold light slides across them.` Kare: Silex `A thin separate silver translation receiver rests at the right temple.` → `The right temple is bare; a thin separate silver strip lies on the table beside the recording slab.` Alıcının masaya konması C68/C69 arasındaki kesmeye düşer.

### B6 · CİDDİ · C65 oturmuş yüz yakın planında ayağa kalkma
YER       G06.md:103 (Video), G06.md:98 (Görsel); C65 0-4 s
KANIT     `The camera begins a slow tilt up as Nith presses both palms on the table edge and rises from the head chair` · kare: `Close frontal portrait … seated upright`
ETKİ      Yakın portrede başın 30-40 cm yükselmesi kamera tilti ile birleşince iki hareket oluyor (kamera + beden). Koltuk geri itme, avuç masadan kalkma ve konuşma aynı anda. Pencere ve kara delik arkada kayarsa C73-C84'te ayakta Nith'in referansı bozulur.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:56 (§B sıra 10, geniş temas/kalkış kısa tutulur) [HİPOTEZ]; ARIZA_LISTESI.md:45 (T02) [ARAÇ]
ARIZA     T02 · T10
DÜZELTME  Kare: `Both of his palms lie flat on the table edge at the bottom of the frame.` → `Both of his palms press the table edge, his torso already leaning forward and half risen from the chair.` Video: `as Nith presses both palms on the table edge and rises from the head chair` → `as Nith finishes rising from the head chair, his palms leaving the table edge`.

### B7 · CİDDİ · C83 iki beden, üç hareket vuruşu, kollar kesişiyor
YER       G07.md:218 (Video), G07.md:213 (Görsel); C83 0-10 s
KANIT     `Nith's right arm extends across the table toward the black octagonal body … his right forearm rises from the table edge and sweeps across, stopping level between Nith's open hand and the black octagonal body without touching either … Nith's open hand draws slowly back`
ETKİ      Uzanma, süpürme, durma, geri çekilme ardışık. İki kol masanın ortasındaki küçük nesnede kesişiyor; "dokunmadan" cümlesi tutmaz, kol-kol erimesi en olası arıza. Orun konuşurken kolu hareket ediyor.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:47 [HİPOTEZ]; FILM.md:408 (T01 tek engelleme hareketi) [SÖZLEŞME, plan]
ARIZA     T01
DÜZELTME  Kare: `his right arm just beginning to rise from his side toward the table centre` → `his right arm extended toward the table centre, the open hand halted above the table; Orun's right forearm lies level and horizontal between that hand and the black octagonal body, touching neither`. Video 0-4 s: `as Nith's right arm extends … As he speaks, his right forearm rises from the table edge and sweeps across, stopping level between …` → `as the two arms hold their positions`. Tek hareket kalır: Nith'in eli geri çekilir (7-10 s).

### B8 · CİDDİ · C85 altı figür, dört eşzamanlı baş-omuz dönüşü, nesne sayımı
YER       G08.md:29 (Video), G08.md:24 (Görsel); C85 0-10 s
KANIT     `Vekh, Ishra, Silex and Orun turn their heads and shoulders away from her toward the personal translation speaker in front of their own seat, while Nith stays seated and still` · kare: `all four looking toward Nem` · `five separate thin silver strips`
ETKİ      Küçük, arkadan ve profilden görünen dört figürün aynı anda dönmesi klon ya da kimlik kayması üretir. Kare ile video arasındaki fark dört beden dönüşü, Nem'in konuşması ve 7-10 s'deki Silex/Nith bakış değişimiyle çok. Geniş planda masadaki yedi küçük nesne (blaster, K1, K2, beş şerit) sayıyla okunmaz.
DOĞDUĞU   kare + hareket
KURAL     ARIZA_LISTESI.md:58 (T15 kadrajda en az kişi) [ARAÇ]; FILM.md:410 [SÖZLEŞME, plan: arkalar veya flu siluetler]
ARIZA     T15 · T09
DÜZELTME  Kare: `all four looking toward Nem` → `all four turned toward the personal translation speaker in front of their own seat`; `five separate thin silver strips` → `small separate thin silver strips`. Video: `Vekh, Ishra, Silex and Orun turn their heads and shoulders away from her toward the personal translation speaker in front of their own seat` → `Vekh, Ishra, Silex and Orun stay turned toward the personal translation speaker in front of their own seat`. 7-10 s: `Silex's head lifts a little toward the centre of the table with its mouth closed, and Nith's gaze lowers to the table while` → sil. "Kendi kaydına döner" kesmeyle kare durumuna alınır.

### B9 · CİDDİ · YEDEK notta, Flow iş emrinde yok
YER       G05.md:263-274 (iş emri, Deneme 2), G06.md:250-273, G07.md:252-275; C59 C61 C64 C67 C68 C69 C75 C78 C82 C83
KANIT     İş emri her satırda `| 2 |` yazıyor. C59, C68, C75, C78, C82, C83 notlarında "YEDEK" var; C61, C64, C67, C69 notlarında yok. Hiçbir iş emri satırı YEDEK'i Deneme 2'ye bağlamıyor.
ETKİ      Aynı sebeple bozulan çekim için aynı prompt tekrar gönderilmez (ajan kuralı). Deneme 2 elde yalnız aynı prompt kalıyorsa kredi boşa gider.
DOĞDUĞU   araç/iş emri
KURAL     ARIZA_LISTESI.md:44 (T01: temas anı gösterilmez) [ARAÇ]; ajan kuralı "aynı sebeple iki kez bozulan çekim için aynı prompt yeniden önerilmez"
ARIZA     T01
DÜZELTME  Bu 10 çekimin iş emri satırında `Deneme 2` → `Deneme 2 = YEDEK (temas anı kesmeyle atlanır, ayrı kare)`. C61, C64, C67, C69 için YEDEK cümlesini nota ekle: kare alıcı eli nesne yanında ya da elde, video yalnız konuşma ve kamera (B4'teki kare biçimi).

### B10 · CİDDİ · C84 kılıf kopyası ve derinlik sırası
YER       G07.md:232 (Görsel), G07.md:237 (Video); C84 0-10 s
KANIT     `Medium view of Vekh standing … seen from across the table … On the black table surface in front of the bronze-red chair, at frame-right in the foreground, lies a single compact dark blaster … At the centre of the table, behind it, rests a single palm-sized black octagonal body` · `Reference 2 … take his face and armour from it` (G07 not satırı: referans sayfası kılıfı sağ kalçada gösteriyor)
ETKİ      Vekh ayakta ve orta plan olduğu için kalça görünür; sayfadaki kılıf çıkmış blasterin yanında ikinci bir blaster üretir (T09 kopya). Kamera masanın karşısında ise K1 (orta) kameraya blasterden yakındır; promptta "behind it" ters. Model birini seçer, K1 ve silah yer değiştirir.
DOĞDUĞU   metin + kare
KURAL     ARIZA_LISTESI.md:52 (T09) [ARAÇ]; FILM.md:409 (T09 silahı eline almaz) [SÖZLEŞME, plan]
ARIZA     T09
DÜZELTME  `At the centre of the table, behind it, rests a single palm-sized black octagonal body with one cyan triangular light.` → `At the centre of the table in the lower foreground rests a single palm-sized black octagonal body with one cyan triangular light, and farther back the compact dark blaster lies in front of the bronze-red chair.` (önceki blaster cümlesi sil). Ek: `The holster at his right hip is empty.` C64'te silah elde ve kadrajın alt kenarı kalçaya yakın, orada da aynı cümle önerilir.

### B11 · CİDDİ · C49 K1 "parlayarak açılıyor", plan C10-C74 bekleme diyor
YER       G05.md:28 (Video); C49 0-3 s ve 7-10 s
KANIT     `the pale amber triangular light on the black octagonal body brightens steadily to a full glow` · `the amber glow stays at full strength beside his hands` · FILM.md:242 (plan A10): `C10–C74 bekleme; C75 özel bağlantı açılır`
ETKİ      Plan "rakam tablosu yerine yüzü ve sesi kanıtı taşır" diyor; ışık durumu değişimi gereksiz bir T09 durumu ekliyor. C69 ve C74'te `pale amber` bekliyor, C49'da tam parlaklık görülürse K1'in C75'te "açılması" önceden harcanmış olur.
DOĞDUĞU   metin
KURAL     FILM.md:242 (plan A10) [SÖZLEŞME, plan]; FILM.md:384 (T06, T09 K1 açılır)
ARIZA     T09
DÜZELTME  `while the pale amber triangular light on the black octagonal body brightens steadily to a full glow;` → `while the pale amber triangular light on the black octagonal body stays lit;` · `the amber glow stays at full strength beside his hands` → `the pale amber light stays steady beside his hands`.

### B12 · CİDDİ · C57 ve C76 Orun arkadan, ense ve baş tarifi yok
YER       G05.md:176 (Görsel C57), G07.md:80 (Görsel C76); C57/C76
KANIT     `Orun sits at the ochre-brown chair position, seen from behind … Orun is an adult nonhuman trade consul. He wears an expensive ochre-brown formal coat` (yüz cümleleri bilerek yazılmadı); C92'de aynı durum için Nem'e `without human ears or hair` konmuş
ETKİ      Referans 5 yalnız yüzü ve alıcıyı taşıyor; C76'da sadece "take his coat". Önplandaki ense/başın arkası hiçbir metin ya da görselde yok; model saç ya da insan ense üretir. Orun'un yüzü bu iki çekimde hiç görünmediği için kimlik sadece ceket ve ense üzerinden okunuyor.
DOĞDUĞU   metin
KURAL     ARIZA_LISTESI.md:59 (T16 yüz/kimlik) [ARAÇ]; FILM.md:381-382 [SÖZLEŞME]
ARIZA     T16
DÜZELTME  `Orun is an adult nonhuman trade consul.` → `Orun is an adult nonhuman trade consul; layered moss-green bark-like plates cover the back of his head, with no hair and no human ears.` Not: bu, plan A05'in yüz plakası kelimelerini başın arkasına uzatır; "plandan dışarı çıkma" talimatı gereği Fable onayı gerekir.

### B13 · CİDDİ · C79 konuşan yüz odak dışı
YER       G07.md:137 (Görsel); C79 0-10 s
KANIT     `Behind it Nem stands at her near position, her upper body and face softly focused but readable` · video: `she speaks … Original voices. Original faces. No substituted lines.`
ETKİ      Ağzı kadrajda replik için kontrol listesi "yüz net, tek konuşan" diyor. Yüz yumuşak odakta olursa dudak hareketi okunmaz ve model odağı Nem'e çekerken K1'in sınanan ışık değişimi flulaşır. Bu çekim planın pilotu: sonuç yanlış sebeple "tutmadı" çıkabilir.
DOĞDUĞU   kare
KURAL     FILM.md:639 (model sesi replik; yüz net) [SÖZLEŞME]
ARIZA     yeni (lip-sync için odak)
DÜZELTME  `In the foreground at the centre of the table, sharply focused, rests` → `In the foreground at the centre of the table rests`; `her upper body and face softly focused but readable` → `her face and upper body in the same deep focus`.

### B14 · CİDDİ · C90→C91 aynı ölçek, aynı açı, farklı durum (jump cut)
YER       G08.md:122 (C90 Görsel), G08.md:141 (C91 Görsel); C90/C91
KANIT     C90: `Extreme wide exterior of the four separated outer fleet groups … across the open corridor` · C91: `Extreme wide exterior of the separated outer fleet groups around a visible but narrow open corridor` · C90 videosu rust-red formasyonu açarak biter; C91 koridoru dar başlatıyor.
ETKİ      Aynı referans çifti, aynı ölçek ve yanal drift; durum geri alınmış gibi görünür ve kesme jump cut okunur. Koridor C90 sonunda açılmışken C91'de yeniden dar.
DOĞDUĞU   kare + kurgu
KURAL     kesme sürekliliği kuralı (12.10.2026, GECIS_VE_SES_SUREKLILIGI.md; bu eleştiri okumadı) [TERCİH]
ARIZA     yeni
DÜZELTME  C91 Görsel açılış: `Extreme wide exterior of the separated outer fleet groups around a visible but narrow open corridor.` → `Wide view from low at the edge of the open corridor, looking along it between the pearl-white and teal fleet and the rust-red fleet, a few tiny medical and civilian craft waiting in the near foreground and the station silhouette far down the corridor.` C91 video 7-10 s `the drift carries on past the station silhouette` → `the drift carries on along the corridor toward the station silhouette`.

### B15 · KÜÇÜK · C90 silah şeritleri "extreme wide" ölçekte okunur mu
YER       G08.md:122 (Görsel), G08.md:127 (Video); C90 3-7 s
KANIT     `The rust-red wedge ships are at one side with their weapon-light strips still lit` · `The strips on the rust-red wedge ships go dark group by group`
ETKİ      Sahnenin tek anlatı vuruşu, ölçekten dolayı seçilmeyebilir. Kareyi görmeden okunur ya da okunmaz diyemem (görülmedi).
DOĞDUĞU   kare
KURAL     —
ARIZA     yeni
DÜZELTME  Kare kapısına ekle: "strip ışıkları 1080p'de seçiliyor mu". Seçilmiyorsa `their weapon-light strips still lit` → `bright red weapon-light strips along every hull, still lit`.

### B16 · KÜÇÜK · C94 cam konumu oturma düzeniyle çelişiyor
YER       G08.md:201 (Görsel); C94
KANIT     `The broad panoramic curved window glows behind Silex and Nem` · `Nith … Vekh … Ishra and Orun … sit small and soft-focus at their fixed positions in the background`
ETKİ      Cam Nith'in arkasında (saat 12), Silex (8) ve Nem (6) yakın taraf. Cam onların arkasındaysa öteki dört "arka planda" olamaz; model biri kazanır.
DOĞDUĞU   metin
KURAL     FILM.md:204-206 (sahne düzeni, plan) [SÖZLEŞME]
ARIZA     yeni
DÜZELTME  `The broad panoramic curved window glows behind Silex and Nem.` → `The panoramic window curves along the far wall.`; `their golden light edging the two figures' shoulders` → `its golden light edging the two figures' shoulders from the side`.

### B17 · KÜÇÜK · C73 temas var, risk sütununda T01 yok
YER       G07.md:28 (Video), FILM.md:398 risk sütunu; C73 0-7 s
KANIT     `his right hand lowers onto the simple physical control … the small pale lamp beside the control goes dark under his hand`
ETKİ      El masaya gömülü kumandaya iniyor ve lamba el altında sönüyor. Kare "just above" gösterdiği için temas anı yine kadrajda; risk sütunu yalnız T06 diyor.
DOĞDUĞU   hareket
KURAL     ARIZA_LISTESI.md:44 [ARAÇ]
ARIZA     T01
DÜZELTME  Risk sütununa `T01 basma` ekle; Video: `the small pale lamp beside the control goes dark under his hand` → `the small pale lamp beside the control goes dark as his hand lifts away`.

### B18 · KÜÇÜK · C57 "wounded" şiddet kelimesi listede yok
YER       G05.md:181 (Video); FILM.md:646 (şiddet kelimeli replikler listesi)
KANIT     `You armed the ships that trapped our wounded.` · FILM.md:646: `R001 C01 · C27 · C29 · C53 · C58 · C68 · C80 · C89 · C95`
ETKİ      BILINEN_TUZAKLAR §A `wounds` kelimesini listeler; `wounded` aynı kök, model sesi repliğinde. Red gelirse kayıt planı hazır olmaz.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:19 [HİPOTEZ, `wounded` sınanmadı]
ARIZA     yeni
DÜZELTME  FILM.md:646 listesine C57 ekle. Replik planın olduğu için metin değişmez; red gelirse yalnız R102 kayda geçer.

### B19 · KÜÇÜK · C50 C51 C53 replik vuruş sınırında bitiyor
YER       G05.md:47, :66, :104
KANIT     C50 `Silex finishes by about 4.5 s. 4-7 s: The mouth seam closes` (R089 1,0+3,4 = 4,4) · C51 `She finishes by about 4.5 s. 4-7 s: Her mouth closes` · C53 `He finishes by about 4 s` (R095 1,0+3,2 = 4,2)
ETKİ      Replik, "ağız kapanır" vuruşuna taşıyor; model sessizliği 4. saniyede keserse son kelime kesilir.
DOĞDUĞU   metin
KURAL     FILM.md:639 (≤5 s, replik penceresi)
ARIZA     yeni
DÜZELTME  C50 ve C51'de ilk vuruşu `0-5 s`, ikinci vuruşu `5-7 s` yap; C53'te `finishes by about 4 s` → `finishes by about 4.2 s` ve `4-7 s` → `4.5-7 s`.

### B20 · KÜÇÜK · R116 (C64) R110'un (C61) ikinci cümlesi
YER       FILM.md:573 (R110) ve :579 (R116)
KANIT     R110 `My hands are empty. I am not your enemy.` · R116 `I am not your enemy.` (C64, kadraj dışı, kurguda)
ETKİ      Aynı cümlenin iki ayrı kaynaktan (model sesi, sahibin kaydı) gelmesi Nem'in sesinde sıçrama yaratır. C61 tutarsa model sesi C64'te yeniden kullanılabilir.
DOĞDUĞU   ses
KURAL     GECIS_VE_SES_SUREKLILIGI (12.10.2026, okunmadı) [TERCİH]
ARIZA     yeni
DÜZELTME  C61 tutarsa R116 için `ses/R116.wav` yerine R110'un 7,0-8,3 s kesitini kullan (F8 kayıt listesi notu).

KAPSAM DIŞI: C85 `Nith sits upright` (G08.md:24) ve C86 `Vekh seated` (G08.md:44) için, C84'te ikisi de ayakta bitiyor (Nith C65'ten beri, Vekh C84) ve oturma geçişi hiçbir yerde gösterilmiyor; devamlılık ajanına.
KAPSAM DIŞI: FILM §2 S78 "cyan" ile plan A10 "C78 sonrası" arasındaki karar zaten G07 notunda Fable'a bırakılmış.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 14 · KÜÇÜK 6
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok). CİDDİ B1-B14 için KABUL ya da RED cevabı beklenir.

Çekim bazında özet (34 çekim; "karedeki hareket görülmedi", hiçbir deneme karesi bu turda yok):
- C49: B11
- C53, C58, C62, C80, C89, C95: şiddet kelimesi model sesinde; kayıt planı var, prompt temiz. Bulgu yok.
- C57: B12, B18 (kubbe içinde dudak: B4'ün açıklaması geçerli; C02 sonucu kapı olarak yazılsın)
- C59: B1, B9
- C60: B2
- C61: B3, B9, B20
- C64: B9, B10 (kılıf cümlesi)
- C65: B6
- C67: B4, B9
- C68: B5, B9
- C69: B9
- C73: B17
- C75, C78, C82: B9 (temas notta; YEDEK'e bağlanmalı)
- C76: B12
- C79: B13
- C83: B7, B9
- C84: B10
- C85: B8
- C86: bulgu yok (silah kadraj altında, hareketsiz)
- C90: B15 · C91: B14
- C92, C93: bulgu yok (Nem arkadan ya da ağzı kapalı; Ishra'nın kubbe içindeki dudağı kare kapısında)
- C94: B16
- C96: bulgu yok (dış ortam cümlesi birebir, T13 yatak Y2 ile kurguda)

GİRDİ    ELESTIRI_PROTOKOLU.md; BILINEN_TUZAKLAR.md (A-D); ARIZA_LISTESI.md T satırları (grep); FILM.md §1, §3 (satır 1-249), §4 risk sütunu (grep), §5 R001-R171, §6, §7; PROMPTLAR/G05.md, G06.md, G07.md, G08.md (tam); NOTLAR.md ve timeline.json (grep, ilgili eşleşme yok). Kare görseli yok.
YAPILMADI  ILK_30_SANIYE_KILAVUZU §6 (C01-C03 bu turda kapsam dışı); FLOW_GERCEKLERI.md ve GECIS_VE_SES_SUREKLILIGI.md (okunmadı; mod↔model için gerek yoktu, tüm çekimler Frames to Video); ODA/F5_* ajan çıktıları (bağımsızlık için okunmadı); kare/video incelemesi (hareket için "görülmedi"); prompt uzunlukları sayılmadı (tahminen en uzun blok C85 Görsel, 4.300 karakterin altında; sınır kontrolü film_dogrula'ya bırakıldı).
