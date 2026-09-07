# TUR 9 · RAPOR 4 (HAM) — ÖLÇEK KANITI GRAMERİ — TEK SABİT PLANDA BÜYÜKLÜK

> **Koşu:** 04.09.2026 · **Girdi promptu:** `../12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` §4
> **Süzme kaydı:** `../04_ARASTIRMA_BULGULARI.md` §TUR 9
>
> ⛔ **HAM METİN.** Düzeltilmez, kısaltılmaz. Kaynak listesi raporun sonunda
> durur. Bu dosyadaki hiçbir sayı doğrulanmış değildir — doğrulama süzme
> kaydında, kural kılavuzdadır.
>
> ⚠️ Metin sahibin yapıştırdığı hâlden aktarılmıştır; araştırma aracının
> alt simge/dipnot işaretleri düz metne çevrilmiş, tablolar Markdown
> tablosuna dönüştürülmüştür. Cümleler ve sayılar DEĞİŞTİRİLMEMİŞTİR.

---

## KOŞULAN PROMPT (birebir)

```
Gerçek yaklaşma ve EVA görüntülerinden (Mekik, Soyuz, Dragon ve Cygnus yanaşma videoları, robot kol kameraları, Apollo yüzey filmi, Chang'e iniş kamerası) bir istasyon modülünün, kafes kirişin ya da yüzey habitatının görünür boyutunun mesafeyle nasıl büyüdüğünü ölç: bilinen odak uzaklığında bin metre, iki yüz metre, elli metre, on metre ve iki metreden hedef kare yüksekliğinin kaçta kaçını kaplar, mesafe-kesir tablosu kur ve her satırın kaynağını ver. İnsanı cetvel olarak kalibre et: kasklı basınç giysili astronotun ayakta boyu, kol erişimi, eldivenli elin tutamağa oranı, regolitteki ayak izinin boyu — ve algı literatüründen boyut sabitliği ile tanıdık-boyut ipuçları (insan figürü, kapak, tutamak, basamak) üzerine bulguları topla; atmosferik perspektif ve pusun bulunmadığı vakumda hangi ipuçlarının çalıştığını, Apollo mürettebatının mesafe yanılgılarının neyi öğrettiğini açıkla. Sinema gramerini sök: Gravity, Interstellar, 2001, Ad Astra, The Martian ve First Man tek karede istasyon ya da üssün büyüklüğünü hangi araçlarla kanıtladı — ön plandaki insan, tekrar eden birim (raf, panel, pencere, tutamak), kadrajı taşan kenar, gölge uzunluğu, ışığın gövde üzerinde katettiği yol, yavaş dönen yapının paralaksı, nokta kaynak güneş — ve bunlardan hangileri kamera hareketi ya da kesme gerektirir, hangileri tek kilitli planda çalışır. Bozulma vakalarını belgele: eleştiri ve VFX çözümlemelerinden ölçeğin kırıldığı örnekler (fazla büyük kapak, sahneler arasında küçülen araç, yanlış alan derinliğinin ürettiği "maket" ve tilt-shift etkisi, yumuşak gölgenin cüceleştirmesi) ve derin netlik, sert gölge ile yüzey doku sıklığının neden "büyük" okuttuğuna dair optik ve algısal açıklama. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz, hareketsiz kameralı 8-10 saniyelik AI videodur; hiçbir yüzeyde okunur ölçü, rakam, çentik ya da işaret olamaz ve ölçü sayısı prompt gövdesine yazılamaz (model onu yüzeye etiket olarak basıyor), bu yüzden her ölçek ifadesi nesne-göreli birimle ("yaklaşık dört gövde boyu") verilmeli ve yaklaşma dizilerinde hedef sahneden sahneye yönelimi sabit kalarak yalnız büyümelidir. Çıktıyı üç parça ver: yapı tipi başına (modül, kafes kiriş, habitat, kapak) 24, 35 ve 50 mm eşdeğer odaklarda mesafe-kesir tablosu; hangi ipucunun hangi mesafe bandında boyutu kanıtladığını gösteren bir "ölçek şahidi merdiveni"; ve nesne-göreli birimle yazılmış tek satırlık İngilizce prompt ifadeleriyle bir bozulma kontrol listesi.
```

---

## RAPOR (ham çıktı)

Uzay Görselleştirmesinde Ölçek Algısı: Gerçekçi Yapay Zeka Video Üretimi İçin Optik, Algısal ve Sinematografik Temeller

Giriş ve Optik Çerçeve

Atmosferin bulunmadığı, ışığın parçacıklara çarparak saçılmadığı ve tanıdık yeryüzü referanslarının tamamen ortadan kalktığı derin uzay ve yörünge ortamları, insan görsel sisteminin evrimsel olarak başa çıkmaya alışkın olmadığı benzersiz bir optik rejim sunar. Bir yörünge istasyon modülünün, devasa bir kafes kirişin (truss) veya ay yüzeyine inşa edilmiş bir habitatın ölçeğinin, tek bir kamera açısından ve kesintisiz, kilitli bir plan içinde doğru bir şekilde algılanması, bir dizi karmaşık görsel ipucunun kusursuz bir uyum içinde çalışmasını gerektirir.

Günümüzde üretken yapay zeka (AI) video modelleri, eğitim verilerindeki atmosferik perspektif (hava katmanı, pus, Rayleigh saçılması) önyargıları nedeniyle uzay sahnelerinde sıklıkla "maket" veya "minyatür" (tilt-shift) etkisi yaratma eğilimindedir. Hedeflenen sekiz ila on saniyelik, hareketsiz kameralı ve kesmesiz yapay zeka video üretimi için en kritik kısıt, hedefin üzerindeki rakam, metin veya okunaklı ölçü birimlerinin kullanılamamasıdır. Rakamlar veya ölçek çentikleri, yapay zeka modelleri tarafından birer görsel doku hatası olarak yüzeye yapıştırılmış anlamsız tipografik etiketlere dönüşmektedir. Bu nedenle, devasa yapıların boyutu tamamen "insan" ölçeğine indirgenmiş, nesne-göreli birimlerle ve sinematografik aydınlatma kurallarıyla ispatlanmalıdır. Gerçek yaklaşma ve uzay yürüyüşü (EVA) görüntülerinden (Uzay Mekiği, Soyuz, Dragon, Cygnus yanaşma videoları, robot kol kameraları, Apollo yüzey filmleri ve Chang'e iniş sistemleri) elde edilen verilerle, sinema gramerinin köşe taşları birleştirilerek sentetik bir görsel doğruluk standardı oluşturulabilir.

Vakum Ortamında Boyut Algısı ve Boyut Sabitliği

İnsan beyni, dünyevi ortamlarda mesafeyi ve boyutu hesaplarken atmosferik perspektife, nesnelerin ufuk çizgisine olan açısına ve araya giren diğer tanıdık nesnelere güvenir. Vakum ortamında ise ışık saçılmaz; ufuktaki bir dağ ile bir metre ötedeki bir kaya aynı keskinlikte, aynı netlikte ve aynı mutlak siyah gökyüzü kontrastıyla görünür. Bu durum, algı psikolojisinde "Boyut-Mesafe Değişmezliği Hipotezi" (Size-Distance Invariance Hypothesis - SDIH) çerçevesinde ciddi bilişsel çöküşlere neden olur.

SDIH kuramına göre, görsel sistem bir nesnenin algılanan boyutunu, nesnenin retinadaki görsel açısı ile algılanan mesafesinin bir fonksiyonu olarak (Emmert Yasası'nın bir uzantısı şeklinde) hesaplar. Vakumda atmosferik ipuçlarının (pus, renk solması) kaybı nedeniyle mesafe algısı bozulduğunda, beynin boyut algısı da zorunlu olarak çöker. Derinlik algısının sağlanması için beyin, aşina olduğu nesnelerin boyutlarını veri tabanından çağırarak (Tanıdık Boyut İpucu - Familiar-Size Cue) bir tersine mühendislik yapar. Ancak doğal bir yeryüzü yapısının (ağaç, ev, bulut) bulunmadığı uzay ortamında bu mekanizma kilitlenir.

Apollo Mürettebatının Mesafe Yanılgılarının Öğrettikleri

Vakum optiğinin insan algısı üzerindeki yıkıcı etkisi, Apollo programı sırasındaki yüzey görevlerinde dramatik şekillerde belgelenmiştir. Apollo astronotları, Ay yüzeyinde yürürken devasa kraterleri veya tepeleri, çok yakındaki küçük çukurlar veya tümsekler olarak algılama eğilimi göstermişlerdir.

Apollo 14 görevinde astronotlar Alan Shepard ve Edgar Mitchell, Fra Mauro bölgesinde yürürken Cone Krateri'nin kenarına ulaşmaya çalışmış, ancak hedeflerinin mesafesini ve boyutunu büyük ölçüde yanlış hesaplamışlardır. Beklediklerinden çok daha uzak ve devasa olan bu krater, yüksek güneş açısı ve pürüzsüz görünen regolit nedeniyle yakın bir tepe gibi algılanmış, bu da astronotların rotada kaybolmalarına ve dik yamaçlarda tehlikeli seviyede metabolik yorgunluk yaşamalarına yol açmıştır. Mesafe algısının olmaması, astronotların 80 metrelik bir yüksekliği ve yüzlerce metrelik bir yatay mesafeyi sıradan bir yürüyüş parkuru sanmalarına neden olmuştur.

Daha çarpıcı bir ölçek kırılması vakası ise Apollo 16 görevinde yaşanmıştır. Astronotlar John Young ve Charlie Duke, North Ray Krateri'nin kenarında yer alan ve sonradan "House Rock" (Ev Kayası) olarak adlandırılan bir jeolojik oluşuma doğru ilerlerken, bu kayanın boyutunu tamamen yanlış yorumlamışlardır. Uzaktan bakıldığında Ay yüzeyinde duran sıradan, orta boy bir kaya bloğu gibi görünen bu yapının yanına geldiklerinde, aslında 24 metre uzunluğunda ve 20 metre yüksekliğinde devasa bir kütle olduğu ortaya çıkmıştır. Astronotlar, tanıdık bir referans nesnesi olmadığı için, 24 metrelik bir kayayı 3-4 metrelik bir kaya olarak, 400 metre mesafeyi ise 50 metre olarak algılamışlardır. House Rock'ın fırlattığı devasa ve keskin gölge dahi, atmosferik derinlik hissinin yokluğunda beyni ikna etmeye yetmemiştir.

Bu yanılgılar, görsel ölçeğin sağlanabilmesi için tanıdık insan ürünü referansların (familiar-size cues) ne kadar hayati olduğunu kanıtlamaktadır. Güneş panelleri, uzay giysileri veya mekanik modüller olmadan, ham uzay ortamında boyut mutlak bir belirsizlik içindedir.

İnsanı Cetvel Olarak Kalibre Etmek: Nesne-Göreli Birimler

Yapay zeka üretiminde metrik ölçülerin (metre, santimetre) yazılı prompt gövdesine entegre edilmesi, modelin bu verileri semantik olarak işlemek yerine doğrudan yüzeye kazınmış harfler ve rakamlar olarak halüsinasyon görmesine neden olmaktadır. Bu yapay etiketlemeleri engellemek için tüm sentetik sahneler, algı psikolojisindeki "Tanıdık Boyut İpucu" ilkesine uygun olarak "insan cetveli" ile nesne-göreli birimlere çevrilerek kalibre edilmelidir. İnsan figürü veya insanın ergonomik sınırlarına göre tasarlanmış donanımlar sahnede yer aldığında, ölçek yanılgısı ortadan kalkar.

Birinci kalibrasyon aracı, kasklı ve basınçlı giysili astronotun ayakta duruş boyudur. Standart bir NASA Extravehicular Mobility Unit (EMU) giysisi veya Rus Sokol giysisi içindeki bir astronotun boyu yaklaşık 1.90 ila 1.95 metre civarındadır. Bir istasyon modülünün dış çapı standart olarak 4.2 metre olduğunda, bu dış yüzey görsel olarak "iki buçuk tam boy astronot" yüksekliği ile tanımlanabilir. Kollarını iki yana açmış bir astronotun kol erişimi ise modüller üzerindeki büyük panellerin genişliğini kanıtlamak için kusursuz bir biyometrik birimdir.

İkinci ve en kritik kalibrasyon aracı, uzay yürüyüşü (EVA) tutamakları ve eldivenli el oranlarıdır. Uluslararası Uzay İstasyonu (ISS) veya Hubble Teleskobu üzerindeki standart sarı/altın renkli EVA tutamakları, devasa modüllerin üzerindeki en küçük ve en hayati tekrar eden ergonomik birimlerdir. Basınçlı bir EVA eldiveni, içerideki basınç (yaklaşık 0.29 atm) nedeniyle şişkin ve hantaldır. Bu eldivenler, standart tutamakları ancak tam olarak kavrayabilecek kalınlıktadır. Uzaktan yaklaşılan bir sahnede, modülün devasa boşlukları üzerinde tekrarlayan bu minik tutamaklar, insan elinin ne kadar küçük olduğunu beyne fısıldayarak ana gövdenin devasa doğasını bilinçaltına işler. Tutamağı kavrayan bir el, istasyonun tüm metrik haritasını saniyeler içinde zihnimizde kurar.

Üçüncü kalibrasyon noktası kapaklar (hatches) ve geçiş portlarıdır. Ortak Kenetlenme Mekanizması (Common Berthing Mechanism - CBM) veya SpaceX Dragon, Orbital Cygnus ve Soyuz kapsüllerinin kenetlenme kapakları yaklaşık 1.3 metre karelik (veya çaplı) bir serbest geçiş alanına sahiptir. Bir astronot bu kapıdan geçerken omuzlarını daraltmak ve dikkatlice süzülmek zorundadır. Bu nedenle bir kapak, istasyonun dış yüzeyinde "kabaca bir insan gövdesi genişliği" olarak tanımlanmalıdır.

Dördüncü araç ise yüzey regolitindeki ayak izleridir. Yüzey habitatları (Ay veya Mars üsleri) söz konusu olduğunda, habitatın devasa iniş ayaklarının tabanında yer alan nervürlü astronot bot izleri, habitatın büyüklüğünü kanıtlayan mikro-doku unsurlarıdır. Apollo kayıtlarında ay modülünün ayaklarının çevresindeki küçük bot izleri, uzay aracının boyutunu net bir şekilde kanıtlayan kontrast araçları olarak işlemiştir.

Görünür Boyut ve Mesafe Geometrisi: Odak Uzaklığı ve Kesir Analizi

Bir yörünge istasyonuna yaklaşan Uzay Mekiği, Soyuz kapsülünün Kurs radar/kamera sistemi, SpaceX Dragon'un yanaşma sensörleri veya Canadarm robot kolunun (SRMS/SSRMS) üzerindeki kameralar ele alındığında, hedef yapının kameranın görüş alanında (Field of View - FOV) kapladığı alan, mesafeyle ters orantılı olarak, mutlak bir geometrik kuralla büyür. AI yaklaşma dizilerinde hedef yapının yöneliminin sabit kalarak sahnede büyümesini sağlamak için bu optik matematiğin bilinmesi şarttır.

Standart bir 35mm tam kare (full-frame) sensör referans alındığında (dikey sensör boyutu V_sensor = 24mm), belirli bir odak uzaklığında (f) ve mesafede (d), kameranın algıladığı dikey görüş alanı şu formülle hesaplanır: FOV_height = d x (V_sensor / f). Hedef nesnenin (örneğin 4.2 metre çapındaki bir modülün) kadrajın yüzde kaçını doldurduğu ise nesne yüksekliğinin (h_obj) FOV yüksekliğine bölünmesiyle elde edilir.

Aşağıdaki mesafe-kesir tabloları, bir istasyon modülü (4.2m), kafes kiriş kesiti (4.5m), yüzey habitatı (6.0m) ve bir kenetlenme kapağının (1.3m) 1000 metre, 200 metre, 50 metre, 10 metre ve 2 metre mesafelerden; geniş açı (24mm), standart (35mm) ve normal (50mm) odak uzaklıklarında hedef kare yüksekliğinin kaçta kaçını kapladığını detaylandırmaktadır.

Tablo 1: İstasyon Modülü (Station Module, 4.2m Çap)

| Mesafe (m) | Odak Uzaklığı (mm) | Dikey FOV (m) | Kadraj Kesri | Yüzdelik Kaplama (%) |
|---|---|---|---|---|
| 1000 | 24 | 1000.000 | 0.0042 | 0.42 |
| 200 | 24 | 200.000 | 0.0210 | 2.10 |
| 50 | 24 | 50.000 | 0.0840 | 8.40 |
| 10 | 24 | 10.000 | 0.4200 | 42.00 |
| 2 | 24 | 2.000 | 2.1000 | 210.00 |
| 1000 | 35 | 685.714 | 0.0061 | 0.61 |
| 200 | 35 | 137.143 | 0.0306 | 3.06 |
| 50 | 35 | 34.286 | 0.1225 | 12.25 |
| 10 | 35 | 6.857 | 0.6125 | 61.25 |
| 2 | 35 | 1.371 | 3.0625 | 306.25 |
| 1000 | 50 | 480.000 | 0.0088 | 0.88 |
| 200 | 50 | 96.000 | 0.0438 | 4.38 |
| 50 | 50 | 24.000 | 0.1750 | 17.50 |
| 10 | 50 | 4.800 | 0.8750 | 87.50 |
| 2 | 50 | 0.960 | 4.3750 | 437.50 |

Analizler, 1000 metre mesafede devasa bir istasyon modülünün insan gözüne en yakın doğal görüşü sağlayan 50mm lenste dahi çerçevenin yalnızca %0.88'ini kaplayan parlak bir nokta olduğunu ortaya koymaktadır. Yaklaşma dizilerinde hedef uzun süre boyunca oldukça küçük kalırken, 10 metre bariyeri geçildiğinde yapılar aniden çerçevenin yarısından fazlasını doldurur.

Tablo 2: Kafes Kiriş Kesiti (Truss Segment, 4.5m Yükseklik)

| Mesafe (m) | Odak Uzaklığı (mm) | Dikey FOV (m) | Kadraj Kesri | Yüzdelik Kaplama (%) |
|---|---|---|---|---|
| 1000 | 24 | 1000.000 | 0.0045 | 0.45 |
| 200 | 24 | 200.000 | 0.0225 | 2.25 |
| 50 | 24 | 50.000 | 0.0900 | 9.00 |
| 10 | 24 | 10.000 | 0.4500 | 45.00 |
| 2 | 24 | 2.000 | 2.2500 | 225.00 |
| 1000 | 35 | 685.714 | 0.0066 | 0.66 |
| 200 | 35 | 137.143 | 0.0328 | 3.28 |
| 50 | 35 | 34.286 | 0.1313 | 13.12 |
| 10 | 35 | 6.857 | 0.6562 | 65.62 |
| 2 | 35 | 1.371 | 3.2812 | 328.12 |
| 1000 | 50 | 480.000 | 0.0094 | 0.94 |
| 200 | 50 | 96.000 | 0.0469 | 4.69 |
| 50 | 50 | 24.000 | 0.1875 | 18.75 |
| 10 | 50 | 4.800 | 0.9375 | 93.75 |
| 2 | 50 | 0.960 | 4.6875 | 468.75 |

Tablo 3: Yüzey Habitatı (Surface Habitat, 6.0m Yükseklik)

| Mesafe (m) | Odak Uzaklığı (mm) | Dikey FOV (m) | Kadraj Kesri | Yüzdelik Kaplama (%) |
|---|---|---|---|---|
| 1000 | 24 | 1000.000 | 0.0060 | 0.60 |
| 200 | 24 | 200.000 | 0.0300 | 3.00 |
| 50 | 24 | 50.000 | 0.1200 | 12.00 |
| 10 | 24 | 10.000 | 0.6000 | 60.00 |
| 2 | 24 | 2.000 | 3.0000 | 300.00 |
| 1000 | 35 | 685.714 | 0.0088 | 0.88 |
| 200 | 35 | 137.143 | 0.0438 | 4.38 |
| 50 | 35 | 34.286 | 0.1750 | 17.50 |
| 10 | 35 | 6.857 | 0.8750 | 87.50 |
| 2 | 35 | 1.371 | 4.3750 | 437.50 |
| 1000 | 50 | 480.000 | 0.0125 | 1.25 |
| 200 | 50 | 96.000 | 0.0625 | 6.25 |
| 50 | 50 | 24.000 | 0.2500 | 25.00 |
| 10 | 50 | 4.800 | 1.2500 | 125.00 |
| 2 | 50 | 0.960 | 6.2500 | 625.00 |

Tablo 4: Kapak / Kenetlenme Portu (Hatch / Docking Port, 1.3m Çap)

| Mesafe (m) | Odak Uzaklığı (mm) | Dikey FOV (m) | Kadraj Kesri | Yüzdelik Kaplama (%) |
|---|---|---|---|---|
| 1000 | 24 | 1000.000 | 0.0013 | 0.13 |
| 200 | 24 | 200.000 | 0.0065 | 0.65 |
| 50 | 24 | 50.000 | 0.0260 | 2.60 |
| 10 | 24 | 10.000 | 0.1300 | 13.00 |
| 2 | 24 | 2.000 | 0.6500 | 65.00 |
| 1000 | 35 | 685.714 | 0.0019 | 0.19 |
| 200 | 35 | 137.143 | 0.0095 | 0.95 |
| 50 | 35 | 34.286 | 0.0379 | 3.79 |
| 10 | 35 | 6.857 | 0.1896 | 18.96 |
| 2 | 35 | 1.371 | 0.9479 | 94.79 |
| 1000 | 50 | 480.000 | 0.0027 | 0.27 |
| 200 | 50 | 96.000 | 0.0135 | 1.35 |
| 50 | 50 | 24.000 | 0.0542 | 5.42 |
| 10 | 50 | 4.800 | 0.2708 | 27.08 |
| 2 | 50 | 0.960 | 1.3542 | 135.42 |

Özellikle 2 metre mesafeye inildiğinde, 24mm geniş açı lenste dahi 4.2 metrelik istasyon modülü kadrajı %210 oranında doldurarak tamamen dışarı taşar (edge bleed). Bu taşkınlık (hedefin objektifi yutması), kapak (hatch) dışındaki tüm devasa yapıların yakından çekimlerinde AI modellerine dayatılması gereken bir optik zorunluluktur.

Sinema Gramerinde Ölçek Kanıtı ve Bozulma Vakaları

Stanley Kubrick'in 2001: A Space Odyssey eserinden bu yana sinematograflar, vakum ortamının getirdiği optik zorlukları aşmak için özel teknikler geliştirmişlerdir. Gerçek uzay görüntülerindeki soğuk, affetmez ve mutlak kontrastlı yapıyı film gramerine aktarmak, özellikle bilgisayar tabanlı yapay modellemelerde derin optik müdahaleler gerektirir.

Derin Netlik (Deep Focus) vs. "Tilt-Shift" Maket Etkisi

2001: A Space Odyssey'de görsel efekt dehası Douglas Trumbull, uzay gemisi maketlerini (Discovery ve Orion gibi) çekerken her detayın (ön plandan arka plana kadar) tamamen net olmasını sağlamak için f/128 gibi iğne deliği büyüklüğünde, ekstrem bir diyafram açıklığı kullanmıştır. Bu devasa kısma işlemi, net alan derinliğini (depth of field) sonsuza kadar uzatarak, kamera maketin sadece birkaç santim uzağında odaklanmış olsa bile, maketin yüzlerce metre uzunluğunda devasa bir gerçek gemi gibi algılanmasını sağlamıştır.

Bunun tam zıttı, "tilt-shift" veya "minyatür faking" olarak bilinen optik bozulmadır. İnsan beyni, yalnızca bir böcek veya oyuncak araba gibi çok yakından (makro) bakılan küçük nesnelerde arka ve ön planın aynı anda sığ bir şekilde bulanıklaştığını görmeye evrimsel olarak alışıktır. Bir uzay istasyonunun arka tarafı veya güneş panellerinin uçları odak dışında (bulanık) bırakılırsa, optik algı bunu derhal "bu küçük bir maket" olarak çevirir. AI video modelleri genellikle bu sığ net alan derinliğini estetik bir "sinematik" dokunuş sanarak sahnelere uygular ve devasa yapının ölçeğini saniyeler içinde çökertip oyuncaklaştırır. Bu nedenle AI promptlarına mutlak keskinlik ve sonsuz alan derinliği (infinite focus) dikte edilmelidir.

Sert Gölgeler ve Nokta Kaynaklı Güneş Işığı

Uzayda ışığı dağıtacak bir atmosfer olmadığı için gölgeleri yumuşatacak mavi bir gökyüzü dolgusu (ambient fill) yoktur. Güneş tek, amansız ve sert bir ışık (single-point source) kaynağıdır. Gravity filminde Görüntü Yönetmeni Emmanuel Lubezki, bu amansız güneşi ve mutlak siyahlık içindeki sert gölgeleri simüle etmek için "LED Kutu" (LED Box) icat etmiş ve ışığı tamamen doğala sadık kalarak tekil kaynaklardan yansıtmıştır.

Ad Astra filminde Hoyte van Hoytema, uzay yolculuğu sahnelerinde gökyüzünün tamamen siyah kalırken yüzeyin ışıkla yıkanmasını sağlamak için özel ışıklandırmalar yapmış, speküler yansımaları (specular highlights) NASA referanslarından birebir kopyalamıştır. Yüksek oranda parlayan (blooming) nokta yansımalar ve zifiri karanlık gölgeler, yapının ne kadar büyük olduğuna dair mikro-kontrastlar sağlar. Gölgelerin kenarları jilet gibi keskindir. Yumuşak (soft) gölgeler, devasa bir uzay gemisini masa lambasıyla aydınlatılmış bir stüdyo maketi boyutuna indirgeyerek optik cüceleşmeye (dwarfism) neden olur. Dahası, ışığın gövde üzerinde katettiği yol uzadıkça ve gölge uzadıkça, beynimiz bu devasa mesafeyi kavrar.

Tek Karede Ölçek: Statik vs. Dinamik Kanıtlar

Sinema gramerinde ölçeği kurmanın yolları kameranın hareketli olup olmamasına göre değişir. Interstellar ve First Man gibi yapımlarda IMAX 70mm kameraların devasa negatifleri kullanılarak, uçsuz bucaksız uzay altyapıları ile kırılgan insan unsuru yan yana getirilmiştir.

Kamera hareketinin olduğu sahnelerde (özellikle 2001 ve Gravity), yavaş dönen devasa yapıların yarattığı hareket paralaksı (motion parallax) beyni hedefin devasa olduğuna ikna eder. Devasa bir kütle, eylemsizlik (inertia) yasaları gereği hızlı dönemez; ağırbaşlı ve statik bir momentumla süzülür. Ancak AI video hedefimiz için kesmesiz, hareketsiz ve kilitli (locked-off) bir kamera şart koşulduğundan, paralaks ve kesme kurgusu kullanılamaz.

Kilitli planda ölçeği kanıtlamak için geriye şu statik araçlar kalır:

Ön Plandaki İnsan: Kadrajın bir köşesinde uzay yürüyüşü yapan küçük bir astronot ile arka planı tamamen dolduran devasa yapı. (Ölçeği anında kilitler).

Tekrar Eden Birimler: İstasyon modülü boyunca sonsuza doğru uzanan radyatör panelleri, yüzlerce minik ısı kalkanı kiremiti veya kenetlenme portları dizisi. Beyin bu ritmik tekrarı sayarak mimarinin devasa olduğunu algılar.

Kadrajı Taşan Kenar (Edge Bleed): Yapının sınırlarının kadrajın dışına, dört bir yana taşması. Nesne objektife sığamayacak kadar büyüktür.

Ölçek Şahidi Merdiveni (Scale Witness Ladder)

Farklı mesafe bantlarında beynin boyutu algılamasını sağlayan görsel kanıtlara "şahitler" diyebiliriz. Vakumda atmosferik pus olmadığı için, her mesafe bandında farklı bir optik yapı ön plana çıkarak devasalığı kademeli olarak ispatlar.

1000 Metre Bandı (Nokta Şahitler): Hedef vizörde bir parlak nokta veya küçük bir siluettir (Tablolarda %0.88 kaplama). Form veya ebat tam anlaşılamaz. Ancak güneş ışığının yapı üzerindeki aşırı parlak speküler patlamaları malzemenin donuk bir asteroit değil, metalik/cam doğasına sahip bir insan yapımı olduğunu sezinletir.

200 Metre Bandı (Ritim ve Kütle Şahitleri): Kafes kirişler (trusses), devasa güneş paneli yelkenleri ve ısı radyatörlerinin ritmik ardışıklığı seçilmeye başlar. Seyirci, devasa bir modül diziliminin tekrarını görerek yapının mühendislik büyüklüğünü idrak etmeye başlar.

50 Metre Bandı (Mimari Şahitler): Kenetlenme kapakları (CBM'ler, PMA'lar), pencere modülleri (Cupola gibi) ve iletişim antenleri netleşir. Beyin, pencerelerin içine bir insan sığabileceğini varsayarak ilk "Tanıdık Boyut İpucunu" devreye sokar ve yapının toplam hacmini hesaplar.

10 Metre Bandı (Ergonomik Şahitler): Astronotların EVA sırasında tutundukları minik sarı tutamaklar (handrails), yüzeydeki kablo kanalları, perçinler ve mikrometeorit kalkan katmanları görünür. Bir astronot kadraja girerse, gövdesi tüm yapının büyüklüğünü anında ve kusursuzca kalibre eder. Bu noktada yapı kadrajın yarısından fazlasını yutmuştur (%87.5 kaplama).

2 Metre Bandı (Doku ve Malzeme Şahitleri): Çoklu Katmanlı Yalıtım (MLI) battaniyelerinin kırışıklıkları, kapron bant izleri, dikiş yolları, astronot giysisinin dış kumaş örgüsü (beta bezi dokusu). Bu makro detayların mutlak keskinliği (infinite focus) ve kadrajı %400 aşan "edge bleed" etkisi, yapının devasa bir gerçeğin yüzeyi olduğunu ispatlar.

Bozulma Kontrol Listesi ve Nesne-Göreli AI Prompt Yazımı

Hedef üretimin 8-10 saniyelik, tek karakterli, kamerasız kesmeli ve hareketsiz kameralı bir AI videosu olduğu göz önüne alındığında, yüzeylerde asla okunur bir metin, rakam, çentik veya mezura işareti olmamalıdır. AI modellerine "4 meters" veya "30 feet" gibi ifadeler yazıldığında, model bu sayıları görselin kalitesi yerine doğrudan metal yüzeye etiket olarak basmaktadır.

Bu tipografik halüsinasyonları önlemek ve optik fizik yasalarını AI'a dayatmak için mesafe, ölçek ve netlik kısıtları nesne-göreli birimlerle (object-relative units) ve kesin sinematografik İngilizce direktiflerle ifade edilmelidir. Yaklaşma dizilerinde hedef sahneden sahneye yönelimi (orientation) sabit kalarak yalnız büyümelidir.

Aşağıdaki kontrol listesi, ölçeğin kırılmasını önleyen, tilt-shift etkisini ve yumuşak gölge cüceleştirmesini bloke eden prompt formüllerini içermektedir:

Derin netliği zorlamak ve minyatür (tilt-shift) bozulmasını engellemek için:
extreme deep focus, infinite depth of field, f/128 aperture equivalent, entire structure razor sharp from foreground to background, no blurred edges, no shallow depth of field, absolutely no tilt-shift miniature effect, no background blurring.

Vakum aydınlatmasını dikte etmek ve yumuşak gölge cüceleşmesini engellemek için:
single-point source illumination, extremely harsh unfiltered sunlight, pitch black deep space background, razor-sharp hard cast shadows perfectly mapping the surface topology, high contrast, blinding specular highlights on metallic textures, absolutely no atmospheric haze, zero aerial perspective, no light scattering.

İstasyon modülü ölçeğini insan-göreli birimle kalibre etmek (yakl. 4.2m / 50m mesafeden):
a massive cylindrical space station module, filling roughly one quarter of the vertical frame, the outer cylinder diameter is equivalent to two and a half full-length astronaut bodies, covered in hundreds of tiny rhythmic micrometeoroid impact panels, hull edges bleeding outside the frame boundaries.

Kafes kiriş (Truss) yapısını tekrar eden birimlerle kalibre etmek (yakl. 4.5m / 10m mesafeden):
a colossal modular truss backbone, completely dominating the frame, the span of a single structural bay equals roughly three full arm spans of a human, thousands of tiny repeating mechanical struts fading into sharp perspective, perfectly rigid architecture.

Yüzey Habitatını ve ayak izlerini kalibre etmek (yakl. 6.0m):
a towering lunar surface habitat, casting a tremendously long hard shadow across the regolith, the vertical height of the main habitat equals roughly three stacked human figures, tiny ribbed astronaut bootprints visible in the pristine dust near the massive landing pads, deep focus on both bootprints and the habitat roof simultaneously.

Kapak (Hatch) ve tutamakları yakın mesafede kalibre etmek (yakl. 1.3m / 2m mesafeden):
an orbital airlock hatch occupying the vast majority of the frame, the hatch diameter is exactly the width of one human torso, a tiny gold-anodized EVA handrail next to the hatch matching the exact grip width of a pressurized astronaut glove, heavy MLI foil stitch textures visible.

AI'ın gövde üzerine yazı/rakam basmasını kesinlikle yasaklamak için:
pristine exterior hull, pure functional geometry, completely devoid of any text, numbers, letters, decals, measuring ticks, or typography, no written markings whatsoever, pure mechanical textures only.

Yaklaşma dizilerinde kamera yönelimini sabitlemek için:
static locked-off camera, fixed perspective, target structure slowly expanding in size without changing spatial orientation, continuous unbroken scaling, zero cuts, unmoving horizon line.

Bu algoritmik kurgu, vakum ortamının SDIH (boyut-mesafe) krizlerini optik gerçekçilikle ekarte ederken, AI video modelini sonsuz alan derinliği, keskin güneş ışığı ve tekrarlayan insan-ölçekli nesneler aracılığıyla hatasız bir şekilde kalibre edilmiş devasa uzay yapıları üretmeye zorlayacaktır. Kusursuz bir AI uzay sinematografisi, donanımın metrik büyüklüğünü rakamlarla değil, insanın mekandaki görsel çaresizliğiyle ispatlamaktan geçer.

--- KAYNAK LİSTESİ (raporun kendi listesi, birebir) ---

researchgate.net — (PDF) The Moon Illusion
researchgate.net — The Moon Illusion, An Unsolved Mystery
semanticscholar.org — slope, distance, and height estimation of lunar and lunar-like terrain
researchgate.net — The Interplay of the Two Descriptors of Visual Space
ia601509.us.archive.org — To see the unseen : a history of planetary radar astronomy
dokumen.pub — Star Bound: A Beginner's Guide to the American Space Program
researchgate.net — Slopes along Apollo EVAs: Astronaut experience as input for future
honeysucklecreek.net — Apollo 16 Essay
reddit.com — David Scott working near Apollo 15's lunar rover. Mons Hadley Delta
lunarnetworks.blogspot.com — LROC: How Young is Young? (Apollo 16)
apollojournals.org — Apollo 16 Image Library
orbitalradar.com — NASA EMU Spacesuit — ISS Spacewalk Suit Guide
satnow.com — What is Extravehicular Activity (EVA)?
science.gov — space suit gloves: Topics by Science.gov
isslivenow.com — ISS Live Now - NASA ISS Live Stream & Real-Time Tracking
science.gov — laser docking system: Topics by Science.gov
weasdown.com — William Easdown MSc Thesis
shutterstock.com — 157 Docking Iss Royalty-Free Images, Stock Photos & Pictures
researchgate.net — The configuration and function of the DragonEye 3D flash LIDAR
space-robotics.org — Terrain Relative Navigation | Space Robotics
mdpi.com — A Pathfinder Lunar Construction Mission Concept Using Regolith
catacombs.space1999.net — SFX miniatures - Space: 1999 Catacombs
cinematyler.com — How Kubrick Made 2001: A Space Odyssey - Part 5: Jupiter Mission
visual-memory.co.uk — Creating Special Effects for "2001: A Space Odyssey"
neiloseman.com — VFX - Neil Oseman
nzpetesmatteshot.blogspot.com — Kubricks' 2001: One Mans Incredible Odyssey - Matte Shot
reddit.com — Colbert's tilt-shift intro is incredible
reddit.com — ELI5: in movies, what makes the difference whether a miniature
reddit.com — Tilt-Shift Dubai
supercarblondie.com — Surreal tilt shift video makes real derby cars look like toys
occupycinematography.com — Occupy Cinematography: Cinematography Blog & Film Culture
fxguide.com — Gravity: vfx that's anything but down to earth
hellardmedia.wordpress.com — Ad Astra - VFX SCIENCE
awn.com — MPC's Visual Effects are Out of This World on 'Ad Astra'
fxguide.com — MPC's mission: Ad Astra
reddit.com — Interstellar: Sure the visuals were nice, but what about the
motionpictures.org — Jean-Marc Vallée to Direct John Lennon/Yoko Ono Film for Universal
thecinemaholic.com — What is First Man About? | Ending, Explained
thewrap.com — How the Keighley Imax Camera Was Designed for Christopher Nolan
jov.arvojournals.org — Focus cues affect perceived depth | JOV
americaspace.com — CRS-29 Cargo Dragon Departs Space Station, Heads Home
