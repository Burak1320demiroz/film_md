# TUR 5 · HAM RAPOR 3/4 — SAAT VE BİLEK DÜZENİ

> Koşulan prompt: `../09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` §3
> Koşu: 03.09.2026 · dış derin araştırma modeli · HAM ÇIKTI — düzeltilmez
> Süzme: `../04_ARASTIRMA_BULGULARI.md` §TUR 5

---

Uzay Saatçiliği ve Ekstravehiküler Donanım Envanteri: Derinlemesine Bir Analiz
Uzay uçuşlarının doğası, insan fizyolojisinin ve mekanik mühendisliğin sınırlarının en uç noktalarda test edildiği, hata toleransının sıfıra yakın olduğu bir ekosistem yaratır. Bu bağlamda, astronotların bileklerinde taşıdıkları donanımlar, yalnızca zamanı gösteren basit araçlar olmaktan çıkıp, yaşam destek sistemlerinin ayrılmaz birer parçası, görev senkronizasyonunun anahtarı ve öngörülemeyen felaket durumlarında birer hayatta kalma mekanizması haline gelmişlerdir. Ekstravehiküler Aktivite (EVA - Uzay Yürüyüşü) sırasında bir astronotun bileği, hem insan bilişsel kapasitesinin doğrudan bir uzantısı hem de uzay giysisinin (Amerikan EMU veya Rus Orlan) teknolojik sınırlamalarını aşmak için tasarlanmış ergonomik bir "kontrol paneli" işlevi görür. Bu rapor, uzay saatçiliğinin tarihsel gelişimini, mekanik ve elektronik sistemlerin uzay boşluğundaki arıza modlarını, görsel ayırt ediciliklerini ve bilek topografyasında yer alan diğer hayati donanımları kapsamlı bir şekilde incelemektedir.

Apollo Dönemi ve NASA Kronograf Sertifikasyon Testlerinin Anatomisi
Uzay yarışının ivme kazandığı 1960'ların ortalarında NASA, dijital ve telemetrik sistemlerin çökmesi durumunda astronotların güvenebilecekleri, uzay boşluğuna dayanıklı yedek bir mekanik zamanlayıcıya ihtiyaç duyduğunu belirledi. Astronotların uzay aracının dışında, otonom bir şekilde görev sürelerini ve yaşam destek ünitelerinin kapasitelerini ölçebilmeleri gerekiyordu. Bu doğrultusunda 1964 yılında çeşitli saat üreticilerine resmi bir talep gönderildi. Bu talebe yanıt veren kronograflar, uzay aracının dışındaki aşırı koşulları simüle eden, havacılık ve uzay tarihinin en zorlu 11 aşamalı test sürecine tabi tutuldu. Testlerin amacı, saatlerin günlük kullanım dayanıklılığını ölçmek değil, bir felaket anında saatin işlevselliğini koruyup koruyamayacağını belirlemekti.

NASA'nın belirlediği test parametreleri, bir saatin maruz kalabileceği en yıkıcı fiziksel kuvvetleri sistematik olarak uyguluyordu. Aşağıdaki tablo, bu testlerin bilimsel parametrelerini özetlemektedir:

Test Adı    Parametreler ve Koşullar
Yüksek Sıcaklık    48 saat boyunca 71°C, ardından kısmi vakumda (0.35 atm) 30 dakika boyunca 93°C.
Düşük Sıcaklık    4 saat boyunca -18°C.
Termal Vakum Döngüleri    10^-6 atm basınç altında 71°C ile -18°C arasında 45 dakikalık periyotlarla 15 kez tekrarlanan ani geçişler.
Bağıl Nem    25°C ile 70°C arasında değişen sıcaklıklarda %95'in üzerinde nemde 240 saat.
Saf Oksijen Atmosferi    71°C'de 48 saat boyunca %100 saf oksijen atmosferi (yangın, toksik gaz ve oksidasyon riski).
Şok Direnci    Altı farklı yönden, her biri 11 milisaniye süren 40g kuvvetinde sarsıntılar.
Doğrusal İvmelenme    Üç eksende 333 saniye içinde 1g'den 7.25g'ye, ardından 30 saniye boyunca 16g'ye doğrusal ivmelenme.
Dekompresyon (Vakum)    71°C'de 90 dakika, ardından 93°C'de 30 dakika boyunca 10^-6 atm mutlak vakum.
Yüksek Basınç    60 dakika boyunca 1.6 atm basınç.
Rastgele Titreşim    5 ila 2000 Hz arasında değişen frekanslarda, ortalama 8.8g ivmeli üç eksenli titreşimler.
Akustik Gürültü    40 ila 10,000 Hz frekans aralığında 30 dakika boyunca 130 desibel ses dalgaları.

Teste üç büyük İsviçre markası dahil oldu: Rolex (Ref. 6238 "Pre-Daytona"), Longines-Wittnauer (Ref. 235T) ve Omega (Speedmaster Ref. 105.003). Bu testler sırasında mekanik saatlerin uzayda neden durduğuna dair çok kritik fiziksel veriler elde edildi. Rolex 6238, nem odasında iki kez tamamen durdu; yüksek sıcaklık ve termal vakum testleri sırasında ise saniye ibresi termal genleşme nedeniyle bükülerek diğer ibrelere takıldı ve mekanizmayı kilitledi. Longines 235T'nin camı, dekompresyon (vakum) ve yüksek sıcaklık testi sırasında genleşme ve kasanın içindeki hapsolmuş havanın yarattığı iç basınç farkı nedeniyle kasadan fırlayarak ayrıldı. Yalnızca efsanevi kalibre 321 mekanizmasına sahip olan Omega Speedmaster, kadranındaki fosforlu malzemenin (lume) aşırı ısı ve radyasyon simülasyonunda bozulmasına ve dekompresyon ile ivmelenme testlerinde oran sapmaları (ileri gitme ve geri kalma) göstermesine rağmen çalışmayı sürdürdü. Sonuç olarak, 1 Mart 1965'te "tüm insanlı uzay uçuşları ve ekstravehiküler aktiviteler için uçuşa uygun" onayı alan tek saat oldu.

Mekanik Saatlerin Uzayda Durma Nedenleri: Triboloji ve Termal Stres
Saatlerin uzayda arızalanmasının temel mekanik nedenleri termodinamik ve uzay tribolojisi (sürtünme bilimi) ile açıklanır. Uzay boşluğunda (10^-6 atm ve altı), standart hidrokarbon veya sentetik saat yağları "outgassing" (gaz çıkışı) adı verilen fiziksel bir fenomenle karşılaşır. Düşük basınç ortamında sıvı yağların buharlaşma noktası dramatik şekilde düşer; yağlar kaynayarak buharlaşır ve çarkların, eşapman mekanizmasının arasına katı tortular bırakır. Yağ tabakasının tamamen yok olması, metal-metale doğrudan sürtünmeye, ardından soğuk kaynağa (mikroskobik kaynaklanma) ve en nihayetinde mekanizmanın kilitlenmesine neden olur.

Ayrıca Alçak Dünya Yörüngesi'nde (LEO) veya Ay yüzeyinde, saatler Güneş'in doğrudan yakıcı ısısına (+120°C) ve gölgenin dondurucu soğuğuna (-150°C) maruz kalır. Bu ani sıcaklık dalgalanmaları, saat kasasındaki paslanmaz çelik, mekanizmadaki pirinç dişliler ve camdaki polimer gibi farklı termal genleşme katsayılarına sahip malzemelerin birbirleriyle savaşmasına yol açar. Dişliler genleşerek toleransları aşar ve sıkışır, ya da büzülerek diş atlamalarına neden olur. Mekanik bir saatin bu cehennemden sağ çıkabilmesi, bileşenlerinin termal genleşme paylarının olağanüstü bir mühendislikle hesaplanmış olmasına bağlıdır.

Hesalite İkilemi ve Ay Yüzeyindeki İstisna: Bulova Anomalisi
Apollo görevleri sırasında saat camlarında sentetik safir veya mineral cam yerine "Hesalite" (akrilik/pleksiglas) kullanılmasının ardında yatan neden, genellikle bir "kırılmazlık" efsanesiyle anılır. NASA'nın akrilik camı bilerek talep ettiği düşünülse de, aslında o dönemde kronografların standart üretim malzemesi akrilikti. Ancak akrilik, uzay uçuşları için inanılmaz derecede faydalı bir arıza moduna sahiptir. Safir veya mineral cam, ekstrem bir darbe aldığında mikroskobik, keskin cam şarapnellerine dönüşerek patlar. Sıfır yerçekimi ortamında bu cam tozları astronotların gözlerine, solunum yollarına veya uzay aracının hassas elektronik devrelerine sızarak ölümcül sonuçlar doğurabilir. Hesalite ise darbe aldığında esner veya parçalanmadan çatlar; bu da onu uzay görevleri için mükemmel bir pasif güvenlik donanımı haline getirir.

Bununla birlikte, NASA'nın tüm donanımı standartlaştırma çabasına rağmen, Apollo 15 görevinde beklenmedik bir anomali yaşanmıştır. Görev Komutanı Dave Scott'ın EVA-2 sonrasında standart üretim Omega saatinin akrilik camı, görev sırasındaki aşırı termal stres veya kabin içi basınç farkı nedeniyle yerinden fırlamıştır. Scott, EVA-3 (Ay yüzeyindeki son yürüyüş) için, yedeğinde bulundurduğu kişisel prototip Bulova kronografı (referans 885104/01) sol bileğine takarak Ay yüzeyine çıkmıştır. Bu saat, NASA spesifikasyonlarına uygun olarak üretilmiş ve üzerinde toz bırakmayan, SEB12100030-202 kodlu, "foliage gray" (gri-yeşil) 21.5 inç uzunluğunda bir Velcro cırt cırtlı kayışla giysinin kolunun üzerine sıkıca takılmıştır.

Bulova'nın bu kullanımı, mekanik bir saatin resmi NASA sertifikasyon testlerinden geçmemiş olsa bile, Ay'ın zorlu koşullarında, doğrudan vakum ve radyasyon altında bir EVA sırasında hayatta kalabileceğinin kanıtı olmuştur. Bu saat daha sonra özel bir müzayedede 1.6 milyon dolara satılarak, Ay yüzeyinde kullanılmış ve özel mülkiyette olan tek saat olarak tarihe geçmiştir.

Sovyet ve Rus Uzay Uçuşlarında Strela ve Poljot Geleneği
Sovyet uzay programı, kronometriye Amerikan yaklaşımından tamamen farklı, kendi özgün mühendislik felsefesiyle yaklaşmıştır. Yuri Gagarin 12 Nisan 1961'de Vostok 1 ile uzaya çıktığında, bileğinde 1. Moskova Saat Fabrikası (1MWF) tarafından üretilen Sturmanskie marka bir saat bulunuyordu. Bu saat, sivil piyasada bulunmayan, yalnızca uçuş akademisi mezunlarına verilen askeri bir donanımdı. Kırmızı saniye ibreli, hack (ikinci ibreyi durdurma ve senkronize etme) özelliğine sahip 17 taşlı manuel kurmalı bu model, tamamen IVA (araç içi) koşulları için tasarlanmıştı ve doğrudan basınçlı giysinin içine veya çıplak bileğe takılıyordu.

Ancak uzay yürüyüşü tarihi söz konusu olduğunda, ikonik saat Poljot Strela 3017 kronograftır. Alexei Leonov, 18 Mart 1965'te Voskhod 2 görevinde insanlık tarihinin ilk uzay yürüyüşünü gerçekleştirirken, şişkin Berkut uzay giysisinin üzerinde bir Strela taşıyordu. İsviçre Venus 150/175 mimarisini temel alan ve Sovyetler tarafından modifiye edilen Venus 3017 kalibresine sahip bu kolon çarklı kronograf, zarif gümüş/bej kadranı, altın rengi ince baton ibreleri ve 36-38 mm'lik nispeten küçük krom kaplama çelik kasasıyla dikkat çekiyordu.

Amerikan Apollo giysilerinde olduğu gibi, Sovyet EVA giysilerinde de saatin dışarıdan, kalın kolların üzerinden okunabilmesi gerekiyordu. Strela, 45 dakikalık alt kadranıyla uzay yürüyüşü süresinin zamanlanmasında kritik bir rol oynadı. İlerleyen yıllarda, uzay programı ilerledikçe Poljot 3133 mekanizmalı daha büyük, şoka daha dayanıklı ve gelişmiş modeller, Salyut ve Mir uzay istasyonlarında kozmonotların standart EVA ekipmanı haline geldi. Sovyet yaklaşımı, lüks veya özel üretim yerine, askeri standartlarda seri üretilmiş, kanıtlanmış ve güvenilir mekanizmaların modifiye edilerek uzaya çıkarılmasına dayanıyordu.

ISS Döneminde Dijitalleşme: Elektronik Saatlerin Meydan Okuması
Uluslararası Uzay İstasyonu (ISS) dönemi, astronotların zaman ölçüm ihtiyaçlarında bir paradigma değişimine sahne oldu. Araç içi (IVA) ve uzay yürüyüşü (EVA) senaryolarında, birden fazla programlanabilir alarm, saniyenin yüzde biri hassasiyetinde geri sayım sayacı, farklı zaman dilimleri (UTC, Houston, Moskova) ve Görev Geçen Süresi (MET - Mission Elapsed Time) takibi mekanik saatlerin fonksiyonel sınırlarını aşıyordu.

Bu spesifik ihtiyacı karşılamak için NASA, Microsoft işbirliğiyle üretilen Timex Datalink 150 modelini uzay uçuşları için onayladı. Bu saat, o dönemin şartlarında devrim niteliğinde bir optik sensöre sahipti. CRT monitörün ekranındaki yanıp sönen barkod benzeri ışık verilerini okuyarak bilgisayardan saatin hafızasına veri, randevu ve alarm aktarabiliyordu. ISS'te görev alarmlarını ve bakım takvimlerini senkronize etmek için yoğun olarak kullanıldı. Benzer şekilde, Casio G-Shock DW5600 serisi (özellikle DW-5600C ve DW-5600E), muazzam şok direnci, hafifliği ve güçlü kronometre özellikleri nedeniyle resmi onay alarak uçuşlarda standart IVA araçlarından biri haline geldi.

Dijital ve Elektronik Saatlerin EVA'da Durma Nedenleri
Dijital ve kuvars saatlerin araç içinde (IVA) mükemmel performans göstermesine rağmen, dış uzay boşluğunda (EVA sırasında) kullanımları ciddi fiziksel ve mühendislik engellerine takılır. Bir elektronik saatin vakumda ve aşırı radyasyon altında durmasının veya bozulmasının temel nedenleri şunlardır:

Likit Kristal Donması: LCD (Liquid Crystal Display) ekranlar, güneşin gölgesinde kalınan yörünge gece döngülerinde sıcaklığın -120°C ile -150°C arasına düşmesiyle saniyeler içinde donar. Kristallerin sıvı yapısı katılaşır, ekran kararır, tepki vermeyi bırakır ve likit yapı kalıcı mikroskobik hasar görebilir.

Kozmik Radyasyon ve SEU: Mikroişlemciler, entegre devreler ve bellek yongaları, güneş patlamalarından veya Van Allen kuşaklarından gelen yüksek enerjili protonların (ağır iyonların) çarpmasına maruz kalır. Bu parçacıklar, silikon devre üzerinde geçici bir elektrik yükü yaratarak "Tekil Olay Etkisi" (SEU - Single Event Upset) adı verilen duruma neden olur. Bellek bitleri aniden 0'dan 1'e dönebilir, saatin yazılımı çökebilir veya devrenin "latch-up" (SEL) olarak bilinen şekilde kısa devre yaparak tamamen yanmasıyla sonuçlanabilir.

Kuvars Osilatörü Frekans Kayması: Elektronik saatlerin kalbi olan kuvars kristali (SiO2), radyasyona maruz kaldığında kafes yapısındaki empüriteler (örneğin lityum veya alüminyum katkı maddeleri) yüksek enerji nedeniyle yer değiştirir. Bu, kristalin piezoelektrik rezonans frekansında geri döndürülemez bir kaymaya (frekans driftine) neden olarak saatin zaman tutma hassasiyetini kalıcı olarak bozar. Bu sorunu çözmek için uzay endüstrisi, kristali yüksek sıcaklık ve elektrik alanı altında arındıran "swept quartz" teknolojisini kullanmak zorundadır.

Avrupa Uzay Ajansı (ESA), bu dijital sorunları aşmak ve astronotların özel EVA/IVA ihtiyaçlarını karşılamak üzere, astronot Jean-François Clervoy'un bizzat geliştirdiği ve patentlediği fikirlere dayanarak Omega Skywalker X-33'ü tasarlattı. Fırçalanmış titanyum kasaya ve termo-kompanse (sıcaklık değişimlerine karşı kendini düzelten) bir kuvars mekanizmaya sahip olan X-33, analog ibreler ile arka plandaki dijital LCD ekranı hibrit bir şekilde birleştirir. Saatin en karakteristik özelliği, kaskın içinde veya gürültülü modüllerde bile duyulabilen olağanüstü yüksek sesli bir akustik alarm odasına sahip olması ve astronotların kendi tanımladıkları görev fazlarını (PET - Phase Elapsed Time) takip edebilmesidir.

Ekstravehiküler Aktivite (EVA): Bilek Topografyası ve Katmanlı Donanım Mimarisi
Bir EVA sırasında astronotun bileği ve ön kolu, hayatta kalma ve operasyonel verimlilik için bir gösterge panosuna dönüşür. NASA'nın Extravehicular Mobility Unit (EMU) ve Rusların Orlan giysileri, aşırı iç basınç nedeniyle (EMU'da 4.3 psi, Orlan'da 5.8 psi) şişirilmiş dev birer insan biçimli balon gibi katılaşır. Bu basınç, giysiyi inanılmaz derecede sertleştirir; kolları bükmek, parmakları hareket ettirmek muazzam bir "eklem torku" (joint torque) ve kalori harcaması gerektirir. Aynı zamanda geniş kask yapısı ve göğüs modülleri, astronotun görüş alanını ve baş hareketlerini kısıtlar. Bu nedenle, anlık olarak görülmesi gereken tüm donanımlar bileğe ve kolların alt kısmına özel bir mimariyle, katmanlar halinde yerleştirilir.

Saat Giysi Kolunun ÜZERİNE Nasıl Takılır? (SEB12100030 Pratiği)
Saatler, astronotun çıplak bileğine değil, termal ve mikrometeoroid koruma sağlayan kalın (TMG - Thermal Micrometeoroid Garment) basınç giysisinin üzerine takılır. Bu hacimli ve şişkin kolun etrafını sarabilmek için NASA mühendisleri, "SEB12100030" spesifikasyon numaralı özel bir Velcro (cırt cırtlı) kayış tasarlamıştır.

Çoğunlukla "olive drab" (askeri yeşil) veya "foliage gray" (gri-yeşil) renkte olan ana Apollo/Şekil kayışı (-202 spesifikasyonu), 21.5 inç (yaklaşık 54.6 cm) uzunluğundadır. Bu kayış, Mil-T-5038 naylon dokumadan, V-T-295 spesifikasyonlu sürtünmeye dayanıklı dikiş ipliğinden üretilir. Ucunda, kayışın saatin pimlerinden geçtikten sonra geriye doğru katlanıp kilitlenmesini sağlayan, paslanmaz 302 alaşım çelikten yapılmış oval/dikdörtgen bir halka bulunur. Bu uzun uzantı ve halka mekanizması, astronotun kalın, basınçlı EVA eldivenleriyle dahi kayışı kolayca kavrayabilmesini, çekebilmesini ve gerginliği milimetrik olarak ayarlayabilmesini sağlar. Kayış, EVA sırasında sürtünme veya takılma yoluyla saatin uçup gitmesini önleyen en kritik güvenlik bağıdır.

Cuff Checklist (Bilek Kontrol Listesi)
Kolların distal (ele yakın) veya proksimal (dirseğe yakın) bölgesine yerleştirilen bir diğer hayati donanım "Cuff Checklist"tir (Bilek Kontrol Listesi). Yaklaşık 3.5 x 2.5 inç (9x6 cm) boyutlarındaki spiral ciltli bu deftercik, astronotun giysisinin kolunun dışbükey kavisli yapısına tam uyum sağlayacak şekilde işlenmiş alüminyum bir taban plakasına (brace) monte edilmiştir. Bu alüminyum taban da yine cırt cırtlı kayışlarla kolun üzerine sabitlenir.

Apollo 15 ve Apollo 17 gibi görevlerde Dave Scott ve Gene Cernan tarafından yoğun olarak kullanılan bu liste, yüzeydeki jeolojik örnek toplama sıralamalarını, kamera ayarlarını veya acil durum protokollerini içerir. Sayfaların kalın, metal spiral telli olması ve tabanın alüminyum kavisi, uzay boşluğunda açık bırakılan bir sayfanın yerçekimsiz ortamda kendiliğinden kapanmasını önleyecek mekanik bir direnç oluşturur.

Bilek Aynası ve Gögüs Modülü (DCM) İletişimi
Hem NASA'nın EMU'sunda hem de Rus Orlan giysilerinde yaşam destek sisteminin ana kontrolleri, göğüs bölgesinde yer alan Display and Control Module (DCM) üzerinde bulunur. Ancak astronot, kaskın çeneyi ve boynu tamamen kısıtlayan sabit metal boyun halkası (neck ring / HUT - Hard Upper Torso) nedeniyle aşağıya, kendi göğsüne doğru bakamaz.

Bu aşılmaz optik kör noktayı telafi etmek için DCM üzerindeki tüm etiketler, yazılar, valf konumları ve dijital ekranlar fiziksel olarak ters basılmıştır (ayna yazısı). Astronot, genellikle sağ bileğinin iç veya dış kısmına elastik veya velcro bir bantla taktığı dışbükey (geniş açılı) veya düz bir "bilek aynasını" (wrist mirror) göğsüne doğru kaldırarak bu paneli aynadan düz ve okunaklı bir şekilde okur. Oksijen akış valflerinin ayarlanması, soğutma suyu regülasyonu, iletişim modları ve acil durum uyarı ışıkları bu ayna sayesinde anlık olarak yönetilebilir. Ayna, EVA topografyasının optik bir köprüsüdür.

Basınç Göstergeleri, Dozimetreler ve EMU/Orlan Mühendislik Farkı
Rus Sokol IVA giysilerinde ve Orlan EVA donanımlarında bilek topografyasının ayrılmaz bir diğer parçası analog giysi basınç göstergeleridir (suit pressure gauge). NASA'nın EMU'su 4.3 psi basınçla çalışırken, Rus Orlan giysileri 5.8 psi gibi çok daha yüksek bir basınçla çalışır. Yüksek basınç (Orlan), astronotun dekompresyon hastalığına yakalanmaması için gereken "ön-soluma" (pre-breathe) süresini saatlerden dakikalara indirir, ancak giysiyi çok daha sertleştirerek hareket kabiliyetini azaltır. Düşük basınç (EMU) ise hareket kabiliyetini artırır ancak uzun ön-soluma prosedürleri gerektirir.

Giysi içi basıncın hayati bir parametre olması nedeniyle, Orlan giysilerinde ve bazı erken dönem Amerikan giysilerinde eldiven bağlantı halkasının (wrist disconnect ring) yakınına entegre edilmiş mekanik basınç göstergeleri bulunur. Bu göstergeler genellikle kPa (kilopaskal) ve PSI cinsinden dual-scale (çift ölçekli) okuma yapan, dijital sistemler çökse bile uzay giysisinin iç basıncının tehlikeli bir seviyeye düşüp düşmediğini gösteren güvenilir ibreli mekanik ekranlardır. Ayrıca ISS ve Skylab döneminde astronotların maruz kaldığı kümülatif radyasyonu ölçmek için saat kayışının üzerine ikinci bir alet olarak iliştirilmiş pasif dozimetreler de bilek donanımının bir diğer katmanını oluşturur.

İşlev: EVA Sırasında Saat Gerçekte Neyi Zamanlar?
Bir uzay yürüyüşü son derece tehlikelidir, genellikle 6 ila 8 saat sürer ve çok kesin, saniye saniye planlanmış parametrelere göre kurgulanır. Bilekteki saat, yalnızca zamanı gösteren bir aksesuar değil, şu kritik olayları zamanlayan otonom bir hayatta kalma aracıdır:

Yörünge Gündoğumu ve Günbatımı Döngüleri (Termal ve Görsel Yönetim): Alçak Dünya Yörüngesi'nde (LEO) hızla dönen ISS'teki bir astronot için Güneş her 45 dakikada bir doğar ve batar; yani bir gün 90 dakika sürer. Karanlık (eclipse) fazına girildiğinde sıcaklık aniden -150°C'ye düşer; aydınlık faza geçildiğinde +120°C'ye çıkar. Saat, 45 dakikalık kadran okumasıyla astronota gece/gündüz geçişinin ne zaman olacağını bildirir. Böylece astronot, güneş doğmadan hemen önce vizördeki altın kaplama yansıtıcıyı indirebilir, karanlık çökmeden hemen önce kask lambalarını açabilir ve giysinin sıvı soğutma giysisi (LCVG) üzerinden akan suyun ısıtılmasını veya soğutulmasını manuel olarak ayarlayabilir.

PLSS Sarf Malzemeleri ve Oksijen Takibi: Saatin en kritik görevi, Birincil Yaşam Destek Sisteminin (PLSS) sınırlarının mekanik bir yedeği olmasıdır. Houston Görev Kontrol merkezi sürekli telemetri alıp kalan oksijeni hesaplasa da, güneş fırtınaları, anten arızaları veya LOS (Loss of Signal - Sinyal Kaybı) durumlarında iletişim kesilebilir. Bu felaket senaryosunda astronot, PLSS bataryasının, karbondioksit (LiOH) temizleyicilerinin ve en önemlisi 8 saatlik oksijeninin ne kadarının kaldığını bileğindeki kronografın üzerinden hesaplamak zorundadır.

Görev Aşamaları (PET - Phase Elapsed Time) Limitleri: EVA, belli alt görevlere veya "fazlara" bölünür. Örneğin, bir batarya modülünün sökülmesi işlemine tam 45 dakika ayrılmıştır. Bu sürenin aşılması, hem programın gerisinde kalınmasına hem de astronotun fiziksel tükenmişliğe girmesine veya kalan oksijeni tüketmesine yol açar.

Okuma Aralığı ve Yöntemi: Mürettebat, kalan süreyi düzenli olarak Görev Kontrol ile yapılan sesli iletişim sırasında teyit eder. Houston'ın sessiz kaldığı anlarda veya bir görevin başında/sonunda (her faz geçişinde), kronograf başlatılır veya durdurulur. Analog saat üzerindeki kalın fosforlu (lume) ibreler ve yüksek kontrastlı siyah kadran, okumanın bir saniyenin kesri kadar kısa bir sürede (glanceability - tek bakışta okuma) gerçekleşmesini sağlar. Astronot elindeki aletleri bırakmadan, sadece göz ucuyla bileğine bakarak ne kadar zamanı kaldığını anlar.

Görsel Düzey: Saatlerin Kamera Ölçeğindeki Okunabilirliği ve Ayırt Ediciliği
Uzay saatlerinin görsel tasarımı, onların yalnızca astronotlar tarafından değil, aynı zamanda televizyon yayınları, Hasselblad yüksek çözünürlüklü fotoğrafları ve ISS dış kameraları aracılığıyla nasıl algılandığını doğrudan etkiler. Orta (belden yukarı) ve uzak kamera ölçeğine göre saatlerin ayrıştırılması ve okunabilirlikleri şu şekildedir:

Aşağıdaki tablo, tarihsel uzay saatlerinin görsel tasarımlarını ve kamera karşısındaki algısal ayak izlerini detaylandırmaktadır:

Saat Tipi / Jenerik Tanım    Kadran ve Kasa Özellikleri    Kamera Ölçeğinde Ayırt Edici Özellikler (Medium/Macro shot)
Swiss manual-wind asymmetrical chronograph (Omega Speedmaster)    42mm mat çelik asimetrik kasa, derin siyah kadran, parlak beyaz baton ibreler, ince siyah takimetre bezel. Zeytin yeşili kayış (Sol bilek).    Orta ölçek: Yüksek siyah/beyaz kontrastı sayesinde "siyah bir daire içindeki beyaz vuruşlar" olarak net bir okunabilirlik sunar. Asimetrik kurma kolu koruyucuları (crown guards) silüeti asimetrik yapar.
Swiss manual-wind vintage chronograph (Rolex 6238 Pre-Daytona)    36mm çelik kasa, monokromatik gümüş/metalik kadran, düz (smooth) çelik bezel. Deri/Çelik kayış.    Orta/Uzak ölçek: Metalik kadran üzerindeki ince gümüş ibreler güneş ışığında parlar ve kontrast oluşturamaz. Uzaktan yansıtıcı gümüş bir metal parçası gibi görünür, okunabilirlik kaybolur.
American prototype manual-wind chronograph (Bulova 885104/01)    43mm'lik düz/köşeli çelik kasa, siyah kadran, beyaz göstergeler, ince, uzun, düz kronograf butonları (pushers). Gri-yeşil uzun kayış (Sol bilek).    Orta ölçek: Siyah/beyaz kontrastı uzaktan okunmasına izin verir, ancak silüet olarak kasadan dışarı fırlayan uzun, yassı basma düğmeleri onu ayırt edici kılan en net özelliğidir.
Soviet column-wheel manual-wind chronograph (Poljot Strela 3017)    36-38mm ince krom kaplama çelik kasa, gümüş/bej kadran, altın rengi kılıç ibreler. (Sol bilek).    Orta ölçek: Siyah kadranlı Amerikan saatlerinin aksine oldukça düşük bir kontrasta sahiptir. Orta uzaklıktan kadrandaki kiril yazıları bulanıklaşır, saat parlak gümüş bir düğme gibi görünür.
Japanese square black resin digital watch (Casio G-Shock DW5600)    43mm genişliğinde, koyu gri/siyah poliüretan reçine köşeli (kare) dış kasa, koruyucu tamponlar (bumpers), LCD ekran (Sağ/Sol bilek).    Orta ölçek: Karakteristik kare, kauçuk benzeri silüet uzaktan anında tanınır. Ancak LCD ekrandaki dijital rakamlar yalnızca çok yakın (macro) ölçekte okunabilir; uzaktan ekran ölü, gri bir boşluk gibi görünür.
Swiss advanced quartz hybrid analog-digital chronograph (Omega X-33)    45mm fırçalanmış titanyum kasa, koyu yeşil-gri LCD ekranın etrafında dönen iskelet beyaz-siyah ibreler, kırmızı saniye ibresi.    Orta ölçek: Titanyumun mat, gri yansıması ve büyük kasa çapı öne çıkar. Analog iskelet ibreler uzaktan yüksek kontrast sağlarken, arka plandaki dijital LCD panel uzaktan karanlık görünür.

Bölüm 1: Model → Jenerik İngilizce Tanım Eşleme Tablosu
Telif hakları kısıtlamaları nedeniyle marka isimlerinin doğrudan yapay zeka görsel üretim (prompt) süreçlerinde kullanılamaması durumunda, saatlerin tasarımsal ruhunu yansıtan karakteristik İngilizce çevirileri aşağıdaki gibidir:

Orijinal Model Adı    Generic English Description for Prompt Generation
Omega Speedmaster Pro    Swiss manual-wind asymmetrical chronograph with matte black dial and white baton hands
Rolex 6238 "Pre-Daytona"    Swiss manual-wind vintage chronograph with monochromatic silver dial and smooth steel bezel
Longines-Wittnauer 235T    Swiss manual-wind vintage chronograph with black dial and prominent contrasting white subdials
Bulova Prototype 885104/01    American prototype manual-wind chronograph with black dial, white luminous markers, and flat elongated pushers
Poljot Strela 3017    Soviet column-wheel manual-wind chronograph with silver-beige dial and slim gold indices
Sturmanskie Gagarin    Soviet manual-wind pilot watch with white dial, luminous Arabic numerals, and red sweep seconds hand
Casio G-Shock DW5600    Japanese square black resin digital watch with LCD screen and shock-absorbing bumper case
Timex Datalink 150    American early digital smartwatch with round resin case, LCD screen, and optical sensor lens
Omega Skywalker X-33    Swiss advanced quartz hybrid analog-digital chronograph with brushed titanium case and skeletonized hands

Bölüm 2: Sol-Sağ Bilek Yerleşim Şeması (Konfigürasyon Dizilimi)
Aşağıdaki şema, tipik bir Extravehicular Mobility Unit (EMU) veya Orlan giysisi üzerinde astronotun kollarındaki donanım yığınını (stacking) proksimalden (dirseğe yakın / yukarı) distale (ele yakın / aşağı) doğru anatomik dizilimini göstermektedir:

LEFT ARM (Primary Operational & Timing Arm - Sol Kol):

Spacesuit Sleeve (Zemin): Basınçlandırılmış, hacimli, çok katmanlı beyaz kumaş (Ortho-fabric/Kevlar/Nomex).

Cuff Checklist (Proksimal - Ön Kolun Üst Kısmı): Kavisli alüminyum plaka, ön kolun orta-üst kısmına sıkıca sarılmıştır. 3.5x2.5 inç boyutlarındaki spiral ciltli kontrol listesi sayfalarını tutar.

Primary Chronograph (Distal - Bilek Eklemi): Ana zamanlayıcı saat (örneğin Swiss manual-wind asymmetrical chronograph). 21.5 inçlik zeytin yeşili (olive drab) cırt cırtlı kayışla giysinin kolunun üzerine, eldiven bağlantı halkasının hemen arkasına takılır.

RIGHT ARM (Auxiliary & Life-Support Reading Arm - Sağ Kol):

Spacesuit Sleeve (Zemin): Basınçlandırılmış çok katmanlı beyaz kumaş.

Dosimeter / Radiation Gauge (Proksimal - Ön Kolun Üst Kısmı): EVA sırasında maruz kalınan kümülatif radyasyonu ölçmek için giysinin üzerine sabitlenmiş sensör.

Wrist Mirror (Orta - Bilek): Göğüsteki Display and Control Module (DCM) üzerindeki ters (ayna) yazılı etiketleri okumak için sağ bileğin iç veya dış kısmına elastik bantla takılan dışbükey ayna.

Suit Pressure Gauge (Distal - Eldiven Bağlantı Halkası): (Özellikle Rus Orlan ve Sokol konfigürasyonlarında) Mavi/Kırmızı anodize edilmiş eldiven bağlantı halkasının (wrist disconnect ring) hemen üzerine veya yanına monte edilmiş, giysi bütünlüğünü takip eden çift ölçekli (kPa/PSI) mekanik analog basınç göstergesi.

Bölüm 3: Öğe Başına Tek Satırlık İngilizce Prompt İfadeleri
Bu ifadeler, görsel üretim araçlarında (Midjourney, DALL-E vb.) telif hakkı filtrelerine takılmadan gerçeğe en yakın uzay saati ve donanımı konfigürasyonlarını üretmek için optimize edilmiştir:

Apollo Main Chronograph: A close-up shot of a Swiss manual-wind asymmetrical chronograph with matte black dial and white baton hands, strapped heavily over a white pressurized spacesuit sleeve using a long olive drab hook-and-loop velcro strap, harsh high-contrast orbital sunlight.

Bulova Backup Anomaly: A medium shot of an American prototype manual-wind chronograph with black dial, white markers and flat elongated pushers, worn on a spacesuit wrist with a foliage gray velcro strap, dusty lunar surface background.

Soviet EVA Watch: A macro photography shot of a Soviet column-wheel manual-wind chronograph with silver-beige dial and slim gold indices, attached over a rigid white Russian spacesuit sleeve, Earth's blue atmosphere visible in the background.

ISS Digital LCD Watch: A futuristic cinematic shot of a Japanese square black resin digital watch with LCD screen and shock-absorbing bumper case, floating weightlessly near a space station window, soft blue Earth glow illuminating the display.

Hybrid Titanium Chronograph: A highly detailed shot of a Swiss advanced quartz hybrid analog-digital chronograph with brushed titanium case and skeletonized hands over a dark LCD, worn on a modern spacesuit cuff during a spacewalk.

EVA Cuff Checklist: A curved aluminum wrist brace holding a spiral-bound checklist with 3.5x2.5 inch pages, strapped tightly to the forearm of an astronaut's white spacesuit, detailed technical text visible on the open page.

Astronaut Wrist Mirror: A convex wrist mirror attached to a bulky white spacesuit glove ring via an elastic band, perfectly reflecting a reverse-printed chest control module panel under harsh orbital lighting.

Analog Suit Pressure Gauge: A heavy-duty analog mechanical pressure gauge with dual kPa and PSI scales, mounted directly onto the blue and red anodized wrist disconnect ring of a pressurized astronaut suit, reading optimal pressure.

---

## KAYNAK LİSTESİ (rapor sonunda verildiği hâliyle)

luxurytribune.com — OMEGA Celebrates 60 Years Since The Speedmaster Was Certified
twentytwoten.com — NASA Testing Regime for the Omega Speedmaster Moonwatch
watchfid.com — THE MOONWATCH CERTIFICATION BY NASA - Watchfid
my-watchsite.com — Omega Speedmaster Moonwatch: 60 years of NASA certification
swatch.com — MoonSwatch pays tribute to the OMEGA Speedmaster's space flight
youtube.com — Rolex's Biggest Miss: Why the Speedmaster Won the Space Race
galli.ch — Omega Speedmaster Moonwatch Geschichte - die nächste Generation
gioielleriabonanno.it — omega speedmaster beats rolex 6238 in race to conquer nasa
lubesngreases.com — Greases Keep Components Moving in Space
incurelab.com — Does Vacuum Grease Outgas? Understanding Volatility for High
researchgate.net — Development of a Space Grease Lubricant with Long-Term-Storage
ntrs.nasa.gov — 3o3_o 7 - NASA Technical Reports Server
ntrs.nasa.gov — Lubrication of space systems: Challenges and potential solutions
youtube.com — Why a Quartz Watch Is Doomed in Space - YouTube
www1.ru — Tank in Space: What is Known About the New Orlan-MKS No. 6
mwrf.com — How Radiation Affects Crystals and Oscillators in Space Applications
omegaforums.net — Shattering the Speedy Hesalite Apollo / NASA selection myth (maybe)
omegaforums.net — Why the Moonwatch Used Hesalite vs Sapphire Crystal | Page 2
wornandwound.com — How Bulova Used a Universal Genève to Get to the Moon
zuludiver.com — Bulova's only walk on the Moon - Celebrating the Apollo 15 51st
rrauction.com — Apollo 15 Lunar Surface Worn Bulova Watch from the ... - RR Auction
reddit.com — [Bulova] Today is the 50th Anniversary of Apollo 15 EVA-3 - Reddit
seb12100030.com — Kizzi Precision Flightgear - NASA watch straps and lunar EVA replicas
lunareplicas.com — EXTRA Short NASA watchband - MIL-SPEC - GRAY Tape - 209
cbsnews.com — Watch Worn By Astronaut Dave Scott On Moon Sells For $1.6M
sturmanskie.com — Yuri Gagarin's watch in Space - Sturmanskie
longislandwatch.com — Sturmanskie Gagarin Commemorative, Manual Winding Mechanical
waecce.com — Vintage Sekonda Strela 3017 Chronograph – Waecce
sturmanskie.com — The Strela chronograph is a genuine legend of Soviet watchmaking
poljot24.de — Strela Chronograph Tribute 3017 Leonov - Poljot 24
ranfft.org — Poljot Poljot 3017 Strela Caliber Information - Ranfft DB
poljot24.de — STRELA Chronograph Cosmos Gold - Poljot 24
ranfft.org — Poljot 3133 - Calibers - Ranfft DB
en.wikipedia.org — Timex Datalink - Wikipedia
reddit.com — [Timex] Timex Datalink 150 (NASA / Microsoft) : r/Watches - Reddit
youtube.com — The Most Influential Timex Watch of the '90s: A Nostalgic Gem
hodinkee.com — Just Because: The Forgotten Glory Of The Timex Datalink - Hodinkee
casio.casioca.com — DW5600NASA21 G-SHOCK - | Casio CANADA
fratellowatches.com — The $40 Space Watch From Casio Right Under Your Nose (2021)
thearsenale.com — DW5600 NASA Watch by G-Shock - TheArsenale
g-central.com — NASA x G-Shock DW5600NASA20-7CR "All Systems Go" Collab
hodinkee.com — Introducing: The Casio G-Shock DW5600 NASA Limited Edition
researchgate.net — Examination of a crystal oscillator's frequency fluctuations during the
chinachipsun.com — Analysis of Crystal Oscillator Frequency Drift Causes - ChipSun
mdpi.com — Frequency Stability Degradation in Quartz and MEMS Oscillators
esa.int — ESA - Speedmaster Skywalker X-33 - European Space Agency
en.wikipedia.org — Jean-François Clervoy - Wikipedia
omegawatches.com — Speedmaster Skywalker X-33 Watches | OMEGA UK®
cnet.com — Omega Skywalker: A watch for astronauts - CNET
orbitalradar.com — NASA EMU Spacesuit — ISS Spacewalk Suit Guide - Orbital Radar
newspaceeconomy.ca — The Orlan-MKS EVA Suit - New Space Economy
orbitalradar.com — Orlan EVA Suit — Russian Spacewalk Suit History & Specs
en.wikipedia.org — Extravehicular Mobility Unit - Wikipedia
ntrs.nasa.gov — Results and Analysis from Space Suit Joint Torque Testing
ntrs.nasa.gov — Modeling Spacesuit-Human Interaction for Injury Risk Identification
bhp.engr.tamu.edu — Musculoskeletal Human-Spacesuit Interaction Model
newspaceeconomy.ca — Analysis of the Spacesuit Market - New Space Economy
lunareplicas.com — Short NASA watchband - MIL-SPEC Velcro Brand Fastener, OD
seb12100030.com — The small print for NASA designed watchbands
fratellowatches.com — Speedy Tuesday - Wear Your Speedmaster On VELCRO® Brand
seb12100030.com — Short NASA watchband (Apollo issue) - Kizzi Precision Flightgear
popsci.com — NSFW Lunar EVA Checklists - Popular Science
rrauction.com — Gene Cernan's Apollo 17 Flown Lunar Surface-Used EVA-3 Cuff
apollojournals.org — Cuff Checklists - Apollo 12 Lunar Surface Journal - apollojournals.org
apollojournals.org — Apollo 15 Cuff Checklists - apollojournals.org
seb12100030.com — Apollo 15 EVA-1 cuff checklist - Kizzi Precision Flightgear
space.stackexchange.com — eva - How smart is an EMU (...spacesuit)?
scribd.com — EMU: Space Suit for Extravehicular Activity | PDF - Scribd
wonderfulcollection.wordpress.com — What's an EMU? | A Strange and Wonderful Collection
researchgate.net — (PDF) Design and Development of Extravehicular Mobility Units
astronautix.com — Orlan
spacecenter.org — The Orlan Suit - Space Center Houston
ambu.pt — Ambu® Cuff Pressure Gauge
discoverspace.org — Soviet and U.S. Space Suits - Space Foundation Discovery Center
floydaustralia.com.au — The Top Destination for Capsule Pressure Gauges, Compound
europe.dixonvalve.com — PG00160 - Dual Scale Pressure Gauge PSI/kPa - Dixon Europe
barrelhand.com — T-02: EVA/IVA Strap - Barrelhand
nasa.gov — 11.0 Spacesuits - NASA
space.com — Casio's new digital watch marks 40 years since first space shuttle
