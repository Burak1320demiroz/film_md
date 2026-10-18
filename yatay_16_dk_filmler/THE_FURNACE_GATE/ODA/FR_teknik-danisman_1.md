# FR · teknik-danisman · tur 1 — dikey fragman kartı v1 (17.10.2026)

> Girdi: `ODA/FR_kart_v1.md` (kart v1) · FILM.md §3 · G01 C08 C09 C11 C12 · G03 C25-C27 · G04 C48 · GPT_IMAGE_OMNI §13 · BILINEN_TUZAKLAR · UZAY_FIZIGI. Model: sonnet. Ham çıktı, düzenlenmez.

**FR teknik danışman, THE_FURNACE_GATE dikey fragman kartı v1 (17.10.2026).**
Salt okudum, dosya yazmadım. Okunanlar: kart (tamamı), FILM.md §3 (157-232), G01 C08-C09-C11-C12, G03 C25-C26-C27, G04 C48, GPT_IMAGE_OMNI §13, BILINEN_TUZAKLAR A-C, UZAY_FIZIGI egzoz satırları. ARIZA_LISTESI'ne bakmadım. Karşılığı olmayan risklere `T(yeni)` yazdım.

Genel durum:
- Hiçbir çekimin kare ya da video denemesi yok. Aşağıdakiler film içi emsal çekimlerden (C08-C12, C25-C27, C48) ve tuzak listesinden çıkarımdır, ölçüm değildir.
- Kartın en zayıf noktası: V2b, V3b ve V4 "vizörde yeşil yansıma" istiyor. Filmde bu zaten çözülmüştü (C08 K11: "vizörde ışık yok").
- İkinci zayıf nokta: 10.CEKIRDEK sayfasında `core overheating panel` ve `core spent panel` var. Fragmana sızarsa C69 spoiler'ı olur.

## Bulgular

**Ortak (7 çekim)**

T(yeni) · CİDDİ · hepsi · 16:9 çok panelli referans sayfaları 9:16 kareye ekleniyor. Model sayfanın yatay düzenini ya da panel çerçevesini taşıyabilir, yanlış paneli alabilir (SMOKE P17). · Çekim başına en çok 2 referans yeter: V1a 5+6, V1b 8, V2a 10, V2b 2+7, V3a 2+10, V3b 1+7, V4 2+7. Her anahtar paneli adlandırmalı: `Reference 2 (woman): take her face, the clear pearl helmet and the pearl pressure suit from it, using the left-profile close-up panel.` Kareye ekle: `A single full-bleed vertical photograph of one scene; the references supply only identity and design.`

T(yeni) · KÜÇÜK · hepsi · Piksel. ChatGPT 1024×1536 verirse 864×1536 kırpımında yanlardan 80'er px (%7,8) gider. Mümkünse API'den 1152×2048 al (kırpma yok). Kırpacaksan yüz ve çekirdeği x=%12–%70 içinde kur.

T(yeni) · CİDDİ · hepsi · Merkezin altındaki nesne (çekirdek, eller, ön plan kapsülleri) push-in'le aşağı ve dışa kayar, bitişte alt çeyreğe düşer. V3a, V4, V1b, V2a'da geçerli. · Başlangıç karesinde odak y=%25–%65 aralığında olsun, itiş hafif kalsın (en çok ~%12–15 ölçek): `The camera closes in only slightly, so the core stays in the middle band of the frame.`

T(yeni) · KÜÇÜK · hepsi · Omni ilk saniyede yavaş başlarsa dilim boş kalır (dilim klibin başından). · Ana hareketi 0,5 s'de başlat, bitiş saniyesini yaz: `From the first second the latch is already turning, completing its swing by about 3 s.` Başlangıç karesi hareketin hazır durumunu göstersin.

T(yeni) · KÜÇÜK · hepsi · Promptta "no X" yok (ölçüldü, tutmuyor). Tek istisna kartın onaylı cümlesi `No part of the figure falls into the bottom quarter of the frame.` Gerisi olumlu tarif.

**V1a**

T03/T13 · CİDDİ · V1a · Işık ateşe, dumana ya da plume'a döner (UZAY_FIZIGI egzoz satırı). Alttan çekimde "kameraya yükselir" okunabilir. C12 kalıbı: kaburgaların ARKASINDA yerinde kabaran ışık. · `The orange furnace glow swells in place behind the heavy blast ribs, brightening the rim of each rib and the underside of the ark's stern; the light stays behind the ribs.` Yazılmayacak kelimeler: exhaust, rises, flames, fire, burst, plume.

T(yeni) · CİDDİ · V1a · Dev yapı alttan bükülür (24 mm'de dikey kaçış çizgileri kaburgayı ve kıçı eğer). · `Low-angle view on a 35 mm lens, the camera nearly still, drifting upward very slowly; the black blast ribs stand rigid in two straight vertical rows, and the ark's stern with its two blue engine housings hangs rigid in the upper half.` Tek hareket ışığın kabarması. Gantri kolları, C biçimli beşik ve kepenkler kadraja girmesin.

T08 · KÜÇÜK · V1a · Eksen. FILM sabit tasarımı kıç SOLDA, ark yatay; kart dikeye çevirdi (sapma ④, kabul). Model kıçı yan çevirip "devrilmiş" gösterebilir. · `The ark's long ivory hull recedes upward from its stern in strong perspective, its bow out of frame.`

T(yeni) · KÜÇÜK · V1a · Tug sürekliliği. FILM: tug C80'e kadar ark'ın SANCAK kıç portunda (C12 bu yüzden cümle ekledi). Ya sancak portu kadrajda görünmesin, ya `1 small salvage tug is docked at the ark's starboard stern port, small against the hull` yaz (3. referans gerekir, önermem).

T(yeni) · KÜÇÜK · V1a · Güvenli alan. Alt çeyrekte yalnız koyu kaburga dipleri. Işığın çekirdeği y=%40–%62, kıç y=%10–%35. Kabarma 0,5 s'de başlar, 3,5 s dilim kabarma ortasında kesilir; dilime sığar.

**V1b**

T(yeni) · CİDDİ · V1b · Tekrar eden kapsül sıraları klibin ikinci yarısında erir ya da sayı/biçim değiştirir (dilim yalnız 0-6,5 s olduğu için kısmen korunur). Görünen sıra sayısını azalt. · `A slow steady low track forward at knee height down the central aisle; about seven identical sealed ivory pods stand on each side, each with one dim green status dot, receding to a vanishing point in the upper-left-centre of the frame.`

T(yeni) · CİDDİ · V1b · Yeşil nokta rengi teal, beyaz ya da bokeh'e kayar, noktalar birleşir. Her cümlede "dim green" yaz. Kapaklar opak ve kapalı kalsın.

T(yeni) · KÜÇÜK · V1b · Güvenli alan. Kaçış noktası üst-orta ve diz hizası kamera: yakın sağ sıranın yeşil noktaları sağ %22 şeride ve alt çeyreğe düşer. Kaçış noktasını x≈%40'a çek. Zemin buharı alt çeyrekte kalabilir, odak orada olmasın.

Not: C09 (tek referans 8.KRIYO) zaten çözülmüş; en güvenli çekim.

**V2a**

T(yeni) · CİDDİ · V2a · Süre. C25'te mandal 3 s'de dönmeye başlıyor, 5-8 s'de duruyor. Kart "ilk 5 s'de dönüş ve durma" istiyor; kaynak ritim sığmıyor. Dönüşü 0,5-3,5 s'ye çek. · `0-1 s: the camera begins a slow push-in; the single retaining latch already starts to rotate outward on its hinge. 1-3.5 s: it swings clear of the carry handle and stops at its hinge stop. 3.5-10 s: the push-in continues as the amber glass center settles into a steady glow.` Yavaş başlarsa ikinci denemede dönüşü 0-2,5 s'ye daralt.

T05/T09 · CİDDİ · V2a (aynı zamanda V3a, V4) · Spoiler sızması. 10.CEKIRDEK sayfasındaki yanık/aşırı parlak paneller seçilebilir. · V2a'da `cradle close panel`, V3a'da `core object panel` adı açık yazılsın: `The core is unused, its casing clean graphite with ivory corner guards.` V4'e 10 eklenmez.

T(yeni) · KÜÇÜK · V2a · Çekirdek yatay dikdörtgen; dikeyde "kadrajı doldurur" iddiası zayıf, genişliği doldurur, altta/üstte boşluk kalır. Mandalı ve cam merkezi y=%40–%60'a koy, alt çeyrek boş beşik dibi/zemin olsun. Kasa duvarı dikey bantlarla üst boşluğu doldurabilir.

T01 · KÜÇÜK · V2a · El yok, mandal kendi dönüyor (C25 emsali çözülmüş). C25'teki "from out of frame" ses cümlesi fragmanda çıkar. Prompta `retaining latch` yaz, tek başına "latch" yazma (§C: ayırt edici kelime nesneye bağlanır).

**V2b**

T(yeni) · ÖLÜMCÜL · V2b · Vizörde yeşil yansıma yüzü örter. Şeffaf vizörde yansıma yüzü maskeler; C08'de film bu yüzden "vizörde ışık yok" dedi (K11), kart bunu çevirdi. Yansıma vizör kenarında dar bantla sınırlansın. · `A few small soft green points reflect along the outer edge of her clear visor, while her eyes and face behind the glass stay fully visible and evenly lit; the green light also falls as a soft rim on her helmet's window side.` Yedek (ikinci deneme): vizörde yansıma yok, yeşil yalnız kask yan kenarında ve cam ardında (C08 çözümü).

T(yeni) · CİDDİ · V2b · Yön. Kriyo penceresi koridorun SOL duvarında (FILM). C08'de pencere sağ üçte birdeydi ve Rhea'nın yara tarafı (sağ çene) kameraya bakıyordu. Dikeyde pencere SOLDA olmalı (sağ şerit yeşil noktaları kesmesin); kadın sola bakar, sağ yanağı kameradan uzak kalır. C08'i aynalamak yarayı yanlış yana koyar. `left-profile close-up panel` kullan. · `She stands in left profile facing the cryo window at frame-left, her right cheek turned away from the camera.`

T10 · KÜÇÜK · V2b · Cama eğilmek: ayaklar sabit, yalnız bel. `her boots planted, she leans a little from the hips.` Eğilme 0,5 s'den başlasın (5 s dilim).

T(yeni) · KÜÇÜK · V2b · Güvenli alan. Kafa y=%25–%45, omuz y=%55–%70; pencere solda, kadın merkezde, sağ şeritte yüz yok.

**V3a**

T01 · ÖLÜMCÜL · V3a · İki eldiven + çekirdek kulpu ve kasa kenarı: BILINEN_TUZAKLAR B sıra 1 (92 🔴, el-nesne kaynaşması). C26 emsali: kavrayış ilk karede kurulu, tek kısa kaldırma. Kaldırmayı 4-7 s'den 0,5-3,5 s'ye çek. · `One white glove is already wrapped around the core's rigid carry handle and the other cups under the casing's edge; she lifts the single core a few centimeters straight up out of the cradle, both gloves keeping the same grips.` Yedek kadraj (C26 YEDEK): kare kaldırılmış hâli gösterir, video yalnız hafif itiş + nefes.

T(yeni) · CİDDİ · V3a · "Amber ışık yüzü alttan aydınlatır" vizörde amber yansıma ve yüzün kaybolması riskini taşır; C26 amber ışığı bilerek vizöre değil köşe korumalarına verdi (K11). · `Warm amber light from the core glass falls on the underside of her chin and cheeks inside the helmet; the visor glass stays clear and her eyes stay visible.`

T(yeni) · CİDDİ · V3a · Alt çeyrek. Eller ve çekirdek y=%52–%70, yüz y=%22–%40 olmalı. Beşik alt çeyrekte kalabilir (önemsiz yüzey). Push-in çekirdeği aşağı iter, itiş hafif.

T09 · KÜÇÜK · V3a · Askı boş kalmalı (V4'te dolu). `Her fixed graphite core-carry harness on her chest stays empty.` Panel: `front full-length panel`.

**V3b**

T(yeni) · CİDDİ · V3b · Yakın dikey plan, şeffaf vizörde yeşil: yeşil yansıma yüzü örter, ten yeşile döner. · `Cool green light from the cryo window falls from the side as a soft rim on his cheek and helmet ring; the clear visor shows only a thin green reflection along its edge, his eyes and beard fully visible.`

T(yeni) · CİDDİ · V3b · Baş dönüşü yüz kaydırır (sol şakak yarası ve sakal kaybolur ya da yer değiştirir). Dönüş küçük (en çok ~20-25°), tek hareket. · `Over about two seconds he turns his helmet a few degrees toward frame-right, his eyes following the same direction.`

T(yeni) · KÜÇÜK · V3b · Yön ve şerit. Leon FILM'de solda, Rhea sağda; bakış sağa. Yüz x≈%38'de kurulsun ki dönüşten sonra sağ %22 şerite girmesin. Çene ve omuz halkası y=%62–%74.

T(yeni) · KÜÇÜK · V3b · Pencere ışığı "yandaki camdan": pencere kadraja tamamen girmesin, yalnız ışığı gelsin (yeşil noktalar bokeh'e gitmez). 2 referans: 1.LEON `face close-up panel` + 7.KORIDOR `cryo window panel`.

**V4**

T(yeni) · ÖLÜMCÜL · V4 · İki renkli ışık tek renge kayar. Alttan amber + yandan yeşil: model karışımı tek bakır/teal renge indirir ya da yüzü gri-yeşil boyar. Renkleri YÖNLE ayır, her cümlede renk adını yaz. · `Warm amber light from the core on her chest lights the underside of her chin and helmet from below; cool green light from the cryo window at frame-left lights the left side of her helmet and cheek as a distinct rim; the two colours stay separate on her face, amber below and green at the side.` Pencerede ayrı yeşil noktalar: `a row of small distinct green status dots glows behind the window glass`.

T(yeni) · ÖLÜMCÜL · V4 · "Amber güçlenir" model tarafından aşırı parlama, bloom, ısı izi ya da yanık kasa olarak üretilebilir (C69 `core overheating panel`, spoiler §2). Sınırlama: (1) 10.CEKIRDEK eklenmez, çekirdek 2.RHEA `harness with core panel`'inden gelir; (2) "güçlenir" yerine C25/C26 kalıbı: derinleşme + köşe korumalarını ısıtma; (3) üst sınır cümlesi. · `The amber glass center stays a defined glowing rectangle with crisp edges; once, slowly, its warm light deepens along the ivory corner guards and the underside of her chin, while the graphite casing stays clean, matte and intact.` Yasak: brighter, intense, overheat, glare, burn, blinding. Yedek (ikinci deneme): amber sabit, "güçlenme" yalnız kameranın yaklaşmasından doğsun.

T(yeni) · CİDDİ · V4 · Kesmesiz 10 s, üç hareket (yaklaşma, baş çevirme, amber). Üçüncüsü son 3 saniyeye düşer ve Omni orada yüzü/ışığı kaydırır. Sırala ve süre ver: 0-3 s yaklaşma + bakış camda, 3-6 s bakış çekirdeğe iner, 6-10 s yaklaşma biter + tek amber derinleşmesi. · `She lowers her gaze and tilts her helmet slightly from the window toward the core on her chest over about two seconds.` "Baş çevirme" yerine "gaze lowers + slight tilt" kask kaymasını azaltır.

T(yeni) · CİDDİ · V4 · "İki ışık tek vizörde" imza kadrajı, V2b/V3b'deki maskeleme riskinin iki katı. Öneri: imzayı "tek vizör"den çok "tek yüz üzerinde iki ışık" olarak kur (amber çene altı, yeşil yan); vizörde en çok iki küçük nokta yansıma.

T(yeni) · CİDDİ · V4 · Alt çeyrek + yaklaşma. Çekirdek göğüs askısında y=%58–%72, yüz y=%24–%44. Yaklaşma sürdükçe çekirdek y=%75'in altına iner. Push-in hafif, bitiş kompozisyonunu karede hesapla. Pencere SOLDA (sağ şerit).

T(yeni) · KÜÇÜK · V4 · "Kapsül camı" belirsiz. Kapsül kapakları opak; kastedilen koridor gözlem penceresi. · `the cryo observation window in the corridor's left wall`. 7.KORIDOR'dan yalnız `cryo window panel` (aynı sayfadan ikinci panel eklenmez, C48 notu).

T(yeni) · KÜÇÜK · V4 · Loop. Kart §6 ① V4'ün son karesini "karanlık zeminde ortada parlayan amber dikdörtgen" sayıyor; V4 yüze yaklaşıyor, son kare yüz + çekirdek olur, grafik eşleşme zayıf kalır. Bitişi amber cam merkezin kadraja doldurduğu biçimde kur ya da eşleşmeyi renk/ışık eşleşmesine indir. (Teknik uyarı, hikâye eleştirisi değil.)

T15 · KÜÇÜK · V4 · Kadrajda tek kişi, doğru.

Kapak: V4 120 px'te okunmalı; yüz, amber dikdörtgen ve yeşil nokta kümesi ayrı öbekler olsun. Yedek V4b: amber sabit, tek hareket yaklaşma + bakış.

## Sorulara kısa cevap

- **Dilim.** Ana hareket 3,5 s (V1a), 5 s (V2a, V2b, V3a, V3b) ve 6,5 s (V1b) içine sığar. Koşul: hareket 0,5 s'de başlar ve süresi yazılır. V2a'daki mandal kaynak ritimle (3-8 s) sığmaz, yeniden zamanlanmalı. V4 dilimsiz 10 s.
- **Güvenli alan.** Kartın kadrajları kağıt üzerinde sığıyor. Odağın alt ya da sağ şeride kaydığı çekimler: V4 (push-in çekirdeği aşağı iter), V3a (eller), V1b (yakın sağ sıra yeşil noktaları), V3b (baş dönüşü sağa).
- **Referans.** 16:9 çok panelli sayfalar risktir. Çekim başına en çok 2 referans, panel adı zorunlu. 10.CEKIRDEK yalnız V2a ve V3a'da, tek panel adıyla.
- **En riskli / yedek kadraj ister.** V4 en riskli, ilk denenmesi kartın üretim sırasıyla uyumlu. Yedek kadraj ister: V4 (V4b), V3a (kaldırılmış kare), V2b (vizör yansımasız).

## Risk sırası (en riskliden en aza)

1. **V4** — iki renk karışımı, amber aşırı parlaması/spoiler, 10 s üç hareket, vizör iki yansıma, alt çeyrek.
2. **V3a** — el-nesne (sıra 1 hata), amber vizör yansıması, alt çeyrek.
3. **V2b** — vizörde yeşil yansıma yüzü örter, C08 aynalama/yara yönü.
4. **V1a** — dev yapı bükülmesi, ışığın ateşe/dumana dönmesi, tug sürekliliği.
5. **V3b** — vizörde yeşil, baş dönüşünde yüz kayması.
6. **V2a** — mandal süresi 5 s'ye sığmıyor, 10.CEKIRDEK sayfasındaki yanık paneller.
7. **V1b** — sıraların erimesi, yeşil nokta rengi (emsali C09 çözülmüş, en güvenlisi).

## Dikey prompt kuralları (yazara, 5 madde)

1. **Referans.** Çekim başına en çok 2 referans, her biri panel adıyla. Kareye `A single full-bleed vertical photograph of one scene; the references supply only identity and design` eklenir. 10.CEKIRDEK yalnız V2a (`cradle close panel`) ve V3a (`core object panel`). Yanık ve aşırı parlak paneller asla adlandırılmaz, V4'te 10 eklenmez.
2. **Konum ve itiş.** Odağı y=%25–%70, x=%12–%70 içine kur. Push-in hafif olsun (~%12-15 ölçek), alttaki nesne itişte alt çeyreğe kayar. Pencere ve yeşil nokta kümeleri SOLDA, baş dönüşü merkezden sağa en çok ~%15.
3. **Işık.** Vizör camı berrak kalsın. Amber çene altından, yeşil yan kenardan gelir, vizörde yalnız dar yansıma bandı. İki renk iki yönle ayrılır, her cümlede renk adı yazılır. Güçlenme yerine `deepens along the corner guards` (C25/C26 kalıbı). Vakumda kaburga arkasında `swells in place`; exhaust, rises, flames, plume yazılmaz.
4. **Hareket.** Tek ana hareket 0,5 s'de başlar, bitiş saniyesi yazılır, kare başlangıç durumunu gösterir (el kavrayışı kurulu, mandal hazır, ışık kabarmaya hazır). V4'te üç hareket 0-3 / 3-6 / 6-10 s sırayla. Baş dönüşü yerine bakış + küçük baş eğme.
5. **Lens ve yapı.** Dev yapıda 28-35 mm ve neredeyse sabit kamera. Kapsül sırası en çok ~7/yan. Prompt gövdesine çekim kodu (V1a, C26), büyük harfli kısa etiket ya da başlık satırı yazılmaz (§C); kadrajda yazı ve rakam yok. Kimlik: "the man" / "the woman" ve FILM KİMLİK TABANI birebir.

KAPSAM DIŞI: V4'ün afiş tasarımı ("tek vizör" mü "tek yüzde iki ışık" mı) dramaturg ve Fable kararıdır; burada yalnız model riskini belirttim.

Okunan dosyalar:
- /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/THE_FURNACE_GATE_FRAGMAN_DIKEY.md
- /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/FILM.md
- /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/PROMPTLAR/G01.md
- /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/PROMPTLAR/G03.md
- /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/PROMPTLAR/G04.md
- /Users/dai/github/apex_md/film_md/uretim_hatti/GPT_IMAGE_OMNI_KILAVUZU.md
- /Users/dai/github/apex_md/film_md/uretim_hatti/BILINEN_TUZAKLAR.md
- /Users/dai/github/apex_md/film_md/uretim_hatti/UZAY_FIZIGI_GORUNTU_KILAVUZU.md
