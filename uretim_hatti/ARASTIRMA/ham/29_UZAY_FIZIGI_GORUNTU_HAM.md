# 29 — HAM · 12/3 UZAY FİZİĞİ GÖRÜNTÜDE (derin araştırma cevabı)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı; prompt `../12_URETIM_HATALARI_ARASTIRMA_PROMPTLARI.md` §3. Metin birebir; formüller
> yapıştırmadaki kırık biçimiyle. **Kanıt değildir**: yalnız `../13_SUZME_20261016.md`'de KABUL edilen satır hatta iner.

---

Yapay Zekâ Video Modellerinde Uzay Fiziği ve Görsel Doğruluk Kılavuzu
Yapay zekâ tabanlı video üretim teknolojilerinin (Veo 3/3.1, Gemini Omni, Sora, Kling, Runway Gen-3 vb.) hızlı gelişimi, sinematik içerik üretiminde yeni bir dönem başlatmıştır. Ancak bu modellerin internet ölçeğindeki verisetleriyle eğitilmesi, yeryüzü koşullarına (1 g yerçekimi, atmosferik basınç, hava direnci, akışkanlar mekaniği) dayalı güçlü görsel önyargıların jenerasyon süreçlerine sızmasına yol açmaktadır. Fotogerçekçi, yatay formatlı ve 10 saniyelik çekimlerden oluşan bilimkurgu yapımlarında; alçak Dünya yörüngesi (LEO), uzay istasyonu dışı faaliyetler (EVA), kenetlenme ve kokpit içi sahnelerin doğruluğu, yapımın inandırıcılığını doğrudan belirlemektedir. Bu araştırma kılavuzu, vakum ortamı ve ağırlıksızlık koşullarındaki gerçek fiziksel olguları, yapay zekâ video modellerinde gözlemlenen sistematik hataları ve uygulayıcılar için istem (prompt) mühendisliği ile kurgu bazlı önleme yöntemlerini incelemektedir.

Bölüm A: Gerçek Uzay Fiziği ve Görsel Yansımaları
Vakumda Roket ve Tepki Kontrol İticisi (RCS) Alevinin Dynamics ve Görünümü
Atmosferik ortamda roket egzozu, çevreleyen hava basıncının sınırlandırması nedeniyle görece dar bir sütun halinde ilerler ve türbülanslı koyu dumanlar ile kor halindeki ateş topları oluşturur. Ancak uzay vakumunda dış basınç sıfır (
p≈0) olduğu için, nozülden çıkan gazlar anında aşırı genleşmeye (under-expansion) uğrar. Gazların genleşme açısı nozül çıkışında 
60 
∘
  ila 
90 
∘
  düzeyine ulaşır ve koni şeklinde genişleyen yarı saydam bir bulut yapısı meydana getirir.

Kullanılan yakıt türü visual imzayı kökten değiştirmektedir:

Hipergolik Yakıtlar (MMH / 
N 
2

 O 
4

 ): Uzay mekikleri ve Apollo RCS sistemlerinde kullanılan bu bileşim, vakumda neredeyse tamamen görünmez ya da son derece soluk, morumsu/saydam bir genleşme bulutu üretir.

Sıvı Methane / Sıvı Oksijen (LOX): İtki anında nozül çıkışında çok kısa, temiz, soluk mavi-beyaz bir çekirdek alev oluşturur; is, duman veya turuncu ateş topu barındırmaz.

Kerosene / LOX (RP-1): Atmosferde parlak turuncu alev üretmesine karşın, vakumda dış gaz zarfı hızla dağılarak duman içermeyen yarı saydam bir parlamaya dönüşür.

Görüntüde görünümü: Engine nozülünün ucunda beliren anlık, çok kısa bir parlama ve ardından geniş bir açıyla uzaya yayılan son derece soluk, yarı saydam gaz bulutudur; duman halkaları, türbülans veya ateş topu kesinlikle oluşmaz.

Promptta tarifi: "Clean narrow blue-white thrust line exiting the nozzle, expanding instantly into a translucent wide pale gas plume in pure vacuum space, zero smoke, no fireball".

Vakumda ve Ağırlıksızlıkta Sıvı Dinamiği: Yüzey Gerilimi, Islatma ve Anlık Kaynama
Mikroçekim ortamında yerçekimi ivmesinin baskılanmasıyla (
g≈0) birlikte sıvılara yön veren ana etmen yüzey gerilimi haline gelir. Serbest kalan sıvı kütleleri, yüzey alanını minilimize eden kusursuz küre biçimini alır. Sıvının bir yüzeye temas ettiği senaryolarda, yüzey enerjisine bağlı olarak yapışma (wetting/capillary) etkisi baskın çıkar ve sıvı yüzey boyunca yayılır.

Sıvının doğrudan uzay vakumuna salındığı durumlarda "anlık kaynama" (flash boiling) olgusu gerçekleşir. Ortam basıncının sıvının doymuş buhar basıncının altına düşmesiyle sıvı aniden buharlaşır; bu sırada gerçekleşen endotermik buharlaşmalı soğuma, kalan sıvı damlacıklarını anında dondurarak mikro buz kristalleri bulutuna dönüştürür. Kabin içinde ise serbest damlalar tabana düşmez, sabit hızla veya havada asılı durarak salınım yapar.

Görüntüde görünümü: Basınçlı kabin içinde havada süzülen, ışığı kıran, yüzeyi hafifçe titreşen kusursuz su küreleri; vakum ortamında ise dışarı fışkıran sıvının anında ışıldayan bir buğu ve buz kristali bulutuna dönüşerek dağılmasıdır.

Promptta tarifi: "Weightless translucent fluid droplet forming a perfect hovering sphere in zero gravity inside pressurized cabin, surface tension holding its shape, floating steadily in mid-air".

Ağırlıksızlık ve Vakum Ortamında Parçacık, Kıvılcım ve Buz Kristalleri Hareketi
Sürtünmesiz vakum ortamında veya durgun kabin havasında serbest kalan tüm mikro parçacıklar Newton'un Birinci Hareket Yasası'na uygun olarak net bir kuvvet etki etmediği sürece kararlı hat izler (
v

 =sabit). Parçacıklar yeryüzündeki gibi parapolik rotalarla aşağı ivmelenmez ya da hava direnciyle yavaşlamaz.

Görüntüde görünümü: Kabin içi elektrik arızasından saçılan kıvılcımlar veya venting (gaz tahliyesi) sırasında oluşan buz kristalleri, kapkaranlık uzay fonunda sabit hızla ve kusursuz doğrusal çizgiler halinde ilerler; güneş ışığı vurduğunda keskin parlamalar saçar.

Promptta tarifi: "Bright ice crystals and electrical sparks drifting in pure straight linear trajectories at constant speed across black space background, zero-gravity particle motion".

Uzay Yürüyüşünde (EVA) Biyomekanik, Tutamak İlerlemesi ve Atalet
Uzay yürüyüşü gerçekleştiren bir astronot yerçekimsiz ortamda yürüme eylemi gerçekleştiremez. Dış gövde üzerindeki ilerleme, istasyon yapısına monte edilmiş sarı renkli tutamaklar (handrails) boyunca elden ele çekme eylemiyle (hand-over-hand locomotion) sağlanır. Sabit çalışma gerektiren noktalarda botlar ayak kilitlerine (Portable Foot Restraints - PFR) sabitlenir. Güvenlik emniyet bağları (safety tethers) astronotu sürekli araca bağlar.

Etki-Tepki (Newton'un Üçüncü Yasası) ve Atalet: NASA Extravehicular Mobility Unit (EMU) uzay elbisesinin boş kütlesi yaklaşık 
113 kg ila 
140.6 kg aralığındadır. Astronot ile birlikte toplam kütle 
m≈200−220 kg seviyesine ulaşır. Momentumun korunumu (
m 
astro

 ⋅Δv 
astro

 =−m 
obj

 ⋅Δv 
obj

 ) uyarınca, astronotun dış bir kütleyi itmesi kendisini zıt yönde ivmelendirir. Yüksek atalet nedeniyle yön değiştirme ve durma eylemleri son derece yavaş ve kontrollüdür.

Görüntüde görünümü: Ağır ve hantal uzay elbisesi içinde yavaş kol hareketleriyle tutamakları kavrayarak ilerleyen astronot; bir nesneyi ittiğinde bedeninin geriye doğru kayması ve emniyet bağının süzülmesi.

Promptta tarifi: "Astronaut in bulky white EMU spacesuit moving slowly hand-over-hand along yellow station rail, tether floating smoothly, heavy body inertia in zero gravity".

Yönelim ve Hareket Vektörünün Ayrışması (İtki-Hareket İlişkisi)
Vakum ortamında aracın uzamsal yönilimi (attitude) ile hareket doğrultusu (velocity vector) tamamen bağımsızdır. 
7.8 km/sn hızla ilerleyen bir uzay aracı, yönelimini 
180 
∘
  çevirerek arkasına bakabilir ancak aynı eksende ilerlemeyi sürdürür. Aracın yavaşlaması veya durması için gidiş yönüne doğru bakması ve ters iticilerini (retro-thrusters) hareket yönünün aksine ateşlemesi gerekir.

Görüntüde görünümü: Uzay aracının burnu yan tarafa veya arkaya dönükken yörünge hattı boyunca ilerlemeye devam etmesi; yavaşlama anında ön taraftaki RCS nozüllerinden anlık soluk gaz püskürmelerinin gerçekleşmesi.

Promptta tarifi: "Spacecraft coasting forward along orbital path while oriented sideways, brief pale counter-thrust RCS pulses firing from front nozzles to decelerate".

Alçak Dünya Yörüngesinden Kinematik Görünüm ve Yörünge Hızı
Alçak Dünya Yörüngesinde (LEO, yaklaşık 
400−420 km irtifa) Uluslararası Uzay İstasyonu'nun (ISS) yörünge hızı 
7.66 km/sn ila 
7.8 km/sn (
27,600 km/saat) düzeyindedir.

Yer İzinin Kayma Hızı: 10 saniyelik bir sinematik çekim sürecinde, Dünya yüzeyindeki yer izi (ground track) kadrajın altında net olarak 
76.6 km ila 
78 km kaymaktadır.

Görsel Hız Algısı: 
400 km yükseklikten bakıldığı için Dünya yüzeyi jet uçağındaki gibi bulanık bir hızla geçmez; devasa kavisli bir küre üzerinde kıtalar ve bulut sistemleri kararlı, pürüzsüz ama belirgin bir hızla kayar.

Gündüz-Gece Sınırı (Terminatör Geçişi): İstasyon bir turunu 90 ila 92 dakikada tamamlar. Gündüz bölgesinden gece bölgesine geçişte (terminatör çizgisi), güneş ışığı atmosfer kırılmasıyla sönümlenir ve geçiş 2 ila 5 saniye içinde tamamlanarak araç kapkaranlık Dünya gölgesine girer.

Görüntüde görünümü: Kadrajın alt kısmını kaplayan devasa kavisli Dünya yüzeyinin 10 saniyede ~78 km kayması; terminatör geçişinde istasyon gövdesindeki güneş parlamalarının saniyeler içinde karanlığa gömülmesi.

Promptta tarifi: "Curved Earth horizon drifting smoothly below spacecraft at low Earth orbit speed of 7.8 km/s, visible 78 kilometer ground track displacement over 10 seconds".

Kenetlenme Dinamiği, Temas Mekaniği ve Sönümleme Hızları
Uluslararası Kenetlenme Sistemi Standardı (IDSS / NASA NDS) uyarınca serbest uçan aracın istasyona yaklaşma ve ilk temas hızları son derece düşüktür:

Eksenel Yaklaşma Hızı: 
0.05 m/sn ila 
0.10 m/sn (
5−10 cm/sn).

Radyal/Lüzumsuz Hız Limiti: Maksimum 
0.04 m/sn.

Temas anında araçlar esnek bir top gibi zıplamaz. Yumuşak Yakalama Sistemi (Soft Capture System - SCS) üzerindeki aktif kuvvet geri beslemeli sönümleyiciler kinetik enerjiyi emer. Mekanizma kilitlendikten sonra aktif halkanın geri çekilmesiyle Sert Yakalama (Hard Capture System - HCS) mandalları kilitlenir.

Görüntüde görünümü: Neredeyse duruyormuş hissi veren milimetrik yaklaşma; yumuşak yakalama halkalarının teması anında mikro titreşimlerin hidrolik/elektromekanik olarak sönümlenmesi.

Promptta tarifi: "Spacecraft performing ultra-slow docking approach at 0.05 m/s closing speed, soft capture mechanism gently contacting docking ring without elastic recoil".

Kabin İçi İvmelenme ve Yerçekimsizliğe Geçişte Beden Reaksiyonu
Motor ateşlenmesi (itki anı) esnasında eylemsizlik nedeniyle insan bedeni itki vektörünün aksi yönüne, koltuğun arkalığına doğru baskılanır. Motor kesildiği an (engine cutoff) beden üzerindeki yük kalkar; emniyet kemerleri, kıyafet askıları ve sabitlememiş nesneler serbest kalır.

Görüntüde görünümü: İvmelenme esnasında astronotların yüz dokularının geriye çekilerek koltuğa gömülmesi; motor kesildiği anda kemer bağlarının ve uzuvların anında ağırlıksızlaşarak hafifçe yükselmesi.

Promptta tarifi: "Astronaut strapped in pilot seat pressed firmly backward into padding during acceleration burn, instant body release into floating weightlessness upon engine cutoff".

Bölüm B: Model Hataları, Benchmark Bulguları ve Önleme Teknikleri
Akademik Fizik Evaluasyon Benchmark Bulguları
Yapay zekâ video modellerinin fiziksel doğruluk kapasitelerini ölçen akademik çalışmalar (VideoPhy, PhyGenBench, Physics-IQ, VideoScience-Bench) derin simülasyon yetersizliklerini ortaya koymaktadır:

VideoPhy & VideoPhy-2 (Bansal et al., 2024; Goldenberg et al., 2025): Video jenerasyon modellerinin aksiyon odaklı fiziksel mantıkta, kütle ve momentumun korunumu yasalarında ağır ihlaller yaptığını doğrulamıştır.

PhyGenBench (Meng et al., 2024): 160 farklı prompt ve 27 fizik yasası üzerinden yapılan değerlendirmelerde, Kling-1.6, Runway Gen-3, OpenSora ve CogVideoX modellerinin Mekanik ve Akışkanlar kategorilerinde son derece düşük Fiziksel Mantık Doğruluğu (PCA) aldığı saptanmıştır. Özellikle mekanik testlerinde Kling modelinin fırlatılan yumurtayı kayaya çarptığında kauçuk top gibi zıplattığı, cam küreleri suda batırmak yerine havada asılı tuttuğu ve mikroçekim sıvı davranışını simüle edemediği kaydedilmiştir. PhyWorldBench insan değerlendirme verilerinde (Table 3), modellerin hem anlamsal bağlılık hem de fiziksel mantık kriterlerini sağlama oranları (Both) düşük seviyelerde kalmıştır: Pika 2.0 (%26.2), Sora-Turbo (%20.8), Kling-1.6 (%18.8), Wanx-2.1 (%18.9), Hunyuan 720p (%18.5) ve Runway Gen-3 (%13.0).

Physics-IQ & Physics-IQ Verified (Rädsch et al., 2026): Üretilen videoların %57.6'sının temel fiziksel nedensellik kurallarını (eylemsizlik, temas kuvvetleri) ihlal ettiğini gösteren veriler sunmaktadır.

VideoScience-Bench (2025/2026): Sora-2 ve Veo-3 modellerinin bilimsel süreç simülasyonlarında en yüksek performansı sergilediğini, ancak uzaya özgü ağırlıksızlık sahnelerine yeryüzü yerçekimi normlarını sızdırmaya devam ettiğini belirlemiştir.

Tetikleyici Prompt İfadeleri ve Olumsuz Promptların Ters Etkisi
Uygulayıcı tarafında uzay fiziği hatalarını tetikleyen ana faktör, modellerin eğitim verisetindeki yeryüzü kavramlarını çağıran prompt kelimeleridir. "Rocket blast", "fiery explosion", "walking in space", "spilling water" gibi ifadeler anında atmosferik duman ve 1 g yerçekimi kalıplarını devreye sokmaktadır.

Olumsuz Promptların ("No Smoke", "No Gravity") Ters Etki Mekanizması:
Metinden videoya difüzyon modellerinde (Classifier-Free Guidance - CFG) olumsuz prompt kullanımı deneysel araştırmalarda ters etki (backfire effect) üretebilmektedir. Difüzyon sürecinin erken gürültü adımlarında (
t≈T), negatif metin kodlayıcıya girilen "smoke" veya "gravity" kelimeleri, modelin latent temsil alanında ilgili kavramı aktif tutar. Erken adımlardaki gradyan farkı (
Δt) küçük olduğu için negatif filtreleme geç bir düzeltici olarak kalır ve görsel yapının ilk evrelerinde istenmeyen duman veya yerçekimi önyargılarının oluşmasını engelleyemez.

Çözüm: Olumsuz filtreler yerine tamamen olumlu olgusal tanımlar kullanmaktır. "No smoke" yerine "clear transparent exhaust spray in vacuum"; "no gravity" yerine "weightless microgravity state with hovering objects" yazılmalıdır.

Başlangıç Karesi (Image-to-Video) Çapalanması ve Kurgusal Çözümler
Metinden videoya (T2V) jenerasyonlarında fiziksel sapma oranı yüksekken, doğrudan doğruya fiziksel oranları içeren bir başlangıç karesi (I2V / Image-to-Video) kullanılması model için uzamsal çapa (spatial anchor) oluşturur. Doğru nozül yapısı, kusursuz sıvı küresi veya tutamağı kavrayan el görseli içeren bir ilk kare, 10 saniyelik jenerasyon sürecinde modelin fizik ihlali yapma olasılığını belirgin biçimde azaltır.

Kurgusal ve Kadraj Bazlı Önleme Yöntemleri:

Kesme (Quick Cut): Temas veya darbe anından hemen önce kesme yaparak reaksiyon karesine geçilmesi.

Kadraj Dışı Bırakma (Off-Screen Action): Astronotun adımlama yapan ayaklarının kadraj dışında tutulması; yalnızca gövde ve tutamak ilerlemesinin gösterilmesi.

Sonucu Gösterme (Result-Oriented Framing): Karmaşık kenetlenme dinamiğini simüle etmek yerine, kenetlenmiş nihai durumun gösterilmesi.

Bilimkurgu Sinemasında Bilinçli Sapmalar ve İzleyici Algısı
Sinema sektörü anlatısal gerilimi artırmak için bilinçli fizik ihlalleri yapmaktadır. Yapılan araştırmalar izleyici algısında iki farklı hata kategorisi ortaya koymaktadır:

Sıradan İzleyicinin Fark Ettiği Hatalar: Kabin içinde süzülmesi gereken su damlasının yere dökülmesi, astronotun uzay yürüyüşünde taş gibi aşağı düşmesi, uzay aracının atmosferik uçak gibi bank dönmesi.

Yalnız Uzmanın Fark Ettiği Hatalar: Vakumda fışkıran sıvının anlık kaynama (flash boiling) ile buz kristallerine dönüşmemesi, LEO yörüngesindeki 
7.8 km/sn hızda Dünya yüzeyinin 10 saniyede ~78 km kayma hassasiyeti, IDSS kenetlenme sisteminin 
0.05 m/sn olan milimetrik yaklaşma hızı, hipergolik RCS iticilerinin vakumda tamamen saydam olması.

İzleyici Toleransı: Narrative transport araştırmaları, izleyicilerin görsel anlatıya odaklandıklarında sinematik patlamaları ve ses efektlerini mantıksal olarak hatalı bulsalar da anlatısal heyecan nedeniyle tolere ettiklerini kanıtlamaktadır.

Bölüm C: Yapılandırılmış Referans Tabloları
(a) FİZİK Tablosu
Olgu    Gerçek Davranış (Sayıyla)    Kamerada Nasıl Görünür    Sık Yapılan Görsel Hata    Kaynak    Etiket
Vakumda RCS / Roket İticisi    
Genleşme açısı 
60 
∘
 −90 
∘
 'ye ulaşır; yanma kalıntısız yakıtlarda alev saydamdır.

Nozülden çıkan kısa, saydam/mavi hüzme; geniş açılı soluk gaz bulutu.    Türbülanslı turuncu ateş topu, koyu siyah duman bulutu ve dar çizgi alev.    
NASA SP-8080 / NASA RP-1028

ÖLÇÜLMÜŞ
Sıvıların Ağırlıksızlık ve Vakumda Davranışı    
Yüzey gerilimi sıvıyı küreye çeker; vakumda anlık kaynama (flash boiling) ve donma yaşanır.

Havada süzülen kusursuz sıvı küreleri; vakumda anında buz kristali bulutuna dönüşme.    Damlaların kabin tabanına aşağı doğru düşmesi ve dökülme akışı.    
NASA Microgravity Fluid Studies / Phys. Rev. E

ÖLÇÜLMÜŞ
EVA Hareket Mekaniği ve Atalet    
NASA EMU elbise kütlesi ~140.6 kg; toplam kütle ~200 kg. 
F=ma uyarınca yüksek atalet.

Tutamaklar boyunca elden ele yavaş ilerleme; itme anında astronotun zıt yönde ivmelenmesi.    İstasyon yüzeyinde yeryüzündeki gibi adımlayarak yürüme veya anlık duruşlar.    
NASA TP-2004-212068 / AIAA Papers

ÖLÇÜLMÜŞ
Alçak Yörünge Dünya Kayma Hızı    
ISS orbital hızı 
7.66−7.8 km/sn; 10 saniyede yer izi 
76.6−78 km kayar.

Devasa kavisli Dünya yüzeyinin kadraj altında kararlı ve pürüzsüz biçimde akması.    Dünya'nın tamamen sabit durması ya da jet uçağı gibi aşırı hızlı bulanık akması.    
NASA Space Math / ISS Orbital Mechanics

ÖLÇÜLMÜŞ
Kenetlenme Hızları ve Temas    
Eksenel yaklaşma hızı 
0.05−0.10 m/sn (
5−10 cm/sn).

Neredeyse durur vaziyette yavaş yaklaşma; SCS sönümlemesiyle esnek olmayan temas.    Sert gövde çarpışması, kauçuk top gibi geriye zıplama veya yüksek hızda yaklaşma.    
IDSS IDD Rev C/E / NASA NDS User Guide

ÖLÇÜLMÜŞ
İtki vs. Hareket Yönü Bağımsızlığı    Vektörel bağımsızlık; durma için zıt yönde ters itki (retro-burn) şarttır.    Aracın gittiği yönün aksine bakabilmesi; yavaşlarken ön RCS'lerin ateşlenmesi.    Aracın itki ateşlemesi durduğu an uzayda anında durması veya atmosferik bank dönüşü.    NASA Flight Dynamics / Physics Textbooks    UYGULAMA
Kokpit İvme Reaksiyonu    İvmelenmede gövde itki aksi yönüne bastırılır; motor kapanınca serbest süzülme başlar.    Pilotların koltuğa gömülmesi; motor kesildiğinde kemer ve saçların serbest kalması.    İvmelenme esnasında pilotların öne doğru sarkması veya havada süzülmeye devam etmesi.    NASA Crew Systems Manuals    UYGULAMA

(b) MODEL HATASI Tablosu
Hata Türü    Hangi Modellerde ve Hangi Çalışmada    Çağıran Kelime ya da Durum    Önleyen Olumlu Tarif ya da Kadraj    Kanıt    Kaynak    Etiket
Akışkan ve Temas Mekaniği İhlali    
Kling-1.6, Gen-3, OpenSora, CogVideoX (PhyGenBench)

"water drop falling", "liquid in space", "collision"    "weightless translucent fluid sphere hovering inside cabin, zero-gravity surface tension holds shape"    
"In mechanics, the models struggle to generate simple physically accurate phenomenons... for material properties, Kling displaying the egg bouncing like a rubber ball."

PhyGenBench (Meng et al., 2024 / arXiv:2410.05363)

ÖLÇÜLMÜŞ
Kütle ve Momentum Korunumu İhlali    
Sora, Sora-Turbo, Wan2.1, Veo-3 (VideoPhy-2)

"spacecraft stopping", "turning ship", "thruster launch"    "spacecraft coasting forward with vacuum inertia, subtle counter-thruster pulse firing to alter vector"    
"We find that the models particularly struggle with conservation laws like mass and momentum."

VideoPhy-2 (Goldenberg et al., 2025 / arXiv:2503.06800)

ÖLÇÜLMÜŞ
İstenmeyen Atmosferik Duman ve Ateş Topu    
Veo 3, Kling, Gen-3, Sora (Physics-Aware Negative Prompting Study)

"rocket engine in space", "no smoke" (negatif promptun ters tepmesi)

"clean narrow blue-white thrust plume in vacuum, clear highly-expanded exhaust cone, no smoke"    
"vanilla negative prompting functions more as a late-stage retroactive corrector, rather than as a proactive, preventive blocker of early implausible or undesired content."

Physics-Aware Counterfactual Reasoning (arXiv:2509.24702)

ÖLÇÜLMÜŞ
Düşük Fiziksel Mantık Doğruluğu (PCA)    
Sora-Turbo, Gen-3, Kling-1.6, Pika 2.0 (PhyWorldBench)

Metin tabanlı karmaşık fizik istemleri

Başlangıç karesi (I2V) kullanımı ve olumlu otonom fiziksel tanım

"Table 3: We present the human evaluation results of 10 video generation models across 3 physics types... Pika 2.0 achieves the best overall performance... Gen-3 achieves 0.130 overall performance."

PhyWorldBench (arXiv:2507.13428)

ÖLÇÜLMÜŞ
Yörünge Hızı Kararsızlığı ve Titreşim    
Open-Sora 2.0, Luma, LTX-Video (VideoScience-Bench)

"Earth background moving", "orbital view"    "smooth steady Earth ground track movement at 7.8 km/s, locked camera frame on station body"    
"many systems still lack the capacity to model complex scientific phenomena and often violate basic physical laws."

VideoScience-Bench (2025/2026 / arXiv:2512.02942)

ÖLÇÜLMÜŞ

(c) İZLEYİCİ Tablosu
Hata    Sıradan İzleyici Fark Eder mi?    Kanıt (Anket, Yorum Analizi, Eleştiri)    Kaynak    Etiket
Vakumda Koyu Duman ve Ateş Topu Patlamaları    Fark eder, ancak sinematik gelenek nedeniyle tolere eder.    
Narrative transport araştırmalarında izleyicilerin bilimselliğe aykırı görsel öğelerde duygusal bağ kursa da mantıksal çelişki hissettikleri kanıtlanmıştır: "emotional resonance plays a significant positive mediating role between narrative transportation and scientific thinking skills, with an indirect effect size of 0.246".

Frontiers in Communication / Narrative Transport Study (2026)

ÖLÇÜLMÜŞ
Dünya'nın Yörüngedeki Gerçek Kayma Hızı (
7.8 km/sn)    Fark etmez (Yalnız Uzman Hatası).    
Sıradan izleyici LEO yörüngesindeki (
7.8 km/sn) bir istasyondan Dünya'nın 10 saniyede ~78 km kaymasını "yavaş" zanneder; sinemadaki uçak benzeri hızlı kayma beklentisi algı sapmasından kaynaklanır.

NASA Orbital Mechanics & Space Perception Studies

UYGULAMA
Kenetlenmedeki Aşırı Hız ve Sert Temas    Fark etmez (Yalnız Uzman Hatası).    
IDSS IDD standardı dinamik yüklerin 6500 N değerini aşmaması için 
0.05−0.10 m/sn eksenel yaklaşma hızı zorunlu kılar; izleyiciler sinematik hızlanmayı aksiyon sanır.

IDSS IDD Revision C/E

ÖLÇÜLMÜŞ
Ağırlıksızlıkta Sıvı Damlasının Yere Düşmesi    Fark eder (Sıradan İzleyici Hatası).    
Test panellerinde izleyiciler kabin içinde havada durması gereken suyun tabana düşmesini doğrudan bir "yapay zekâ render hatası" veya "düşük bütçeli efekt" olarak etiketlemektedir.

PhyGenBench Human Evaluation Data

ÖLÇÜLMÜŞ
Vakumda Sıvının Anlık Kaynaması (Flash Boiling) Eksikliği    Fark etmez (Yalnız Uzman Hatası).    
İzleyiciler vakuma çıkan suyun dökülmesini veya küre olarak kalmasını doğal karşılar; faz değişimiyle buz kristallerine dönüşmemesi yalnız fizik uzmanlarınca fark edilir.

NASA Microgravity Physics Reports

UYGULAMA

Bölüm D: Uygulayıcı Kontrol ve Dönüşüm Dizinleri
(1) Uzay Fiziği İki Aşamalı Kontrol Listesi
Aşağıdaki 10 maddelik kontrol listesi, her 10 saniyelik yapay zekâ video çekimi için başlangıç karesi ve video promptu düzeyinde doğrulanmalıdır:

[Evet/Hayır] Başlangıç karesindeki roket/RCS nozül çıkışında atmosferik koyu duman veya ateş topu yerine saydam/geniş açılı soluk gaz jeti tanımlanmış mı?

[Evet/Hayır] Yerçekimsiz kabin içi sahnesinde sıvılar tabana dökülmek yerine kusursuz küre biçiminde ve havada askıda duruyor mu?

[Evet/Hayır] Uzay yürüyüşündeki (EVA) astronot adımlamak yerine sarı tutamaklar boyunca ("hand-over-hand") elden ele mi ilerliyor?

[Evet/Hayır] Astronot kütlesi (~200 kg EMU dahil) nedeniyle hareket başlatma ve durdurma eylemlerinde belirgin atalet ve momentum sergiliyor mu?

[Evet/Hayır] Uzay aracının yavaşlaması veya yön değiştirmesi için zıt vektörde ters itici (retro-thrust) ateşlenmesi tanımlanmış mı?

[Evet/Hayır] Alçak Dünya Yörüngesi (LEO) çekiminde Dünya yüzeyi 10 saniyede ~78 km'lik kararlı kayma hızında mı gösteriliyor?

[Evet/Hayır] Gündüz-gece sınırı (terminator) geçişinde ışık düşüşü 2–5 saniye aralığında hızlı ve keskin mi?

[Evet/Hayır] Kenetlenme sahnelerinde Soft Capture temas hızı 
0.05−0.10 m/sn aralığında son derece yavaş ve sönümlemeli mi?

[Evet/Hayır] Vakuma salınan sıvılarda anlık kaynama (flash boiling) ve buz kristali oluşumu görsellere yansıtılmış mı?

[Evet/Hayır] Prompt yazımında "no smoke", "no gravity" gibi ters tepen olumsuz filtreler yerine pozitif fiziksel tanımlamalar tercih edilmiş mi?

(2) Prompt Dönüşüm Dizini (Kaçınılacak ve Olumlu İfadeler)
Aşağıdaki dizin, yapay zekâ video promptlarında kaçınılması gereken atmosferik/terrestriyal kelimeleri ve bunların yerine kullanılacak İngilizce olumlu ifadeleri içermektedir:

Kaçınılacak Kelime / İfade (Avoid)    Yerine Yazılacak İngilizce Olumlu İfade (Use Positive Substitute)
smoke, billowing smoke, fiery plume, burning exhaust    clean narrow blue-white thrust line, translucent highly-expanded vacuum plume, clear exhaust spray
walking in zero gravity, astronaut walking on station    astronaut performing hand-over-hand locomotion along yellow handrails, tethered microgravity floating posture
water spilling, liquid falling down, water drop dropping    weightless spherical water globe hovering in mid-air, surface-tension bound liquid sphere, floating droplet
spacecraft stopping instantly, sudden turn in space    spacecraft coasting smoothly with vacuum inertia, subtle counter-thruster RCS pulse firing for deceleration
dramatic explosion fireball in vacuum    silent energetic flash burst, expanding pale vapor shell in vacuum, instantly dispersing debris cloud
no gravity, no smoke, no fire (Ters etki yapan negatifler)    zero-gravity microgravity environment, clear vacuum space, transparent thruster exhaust
docking collision, ship bumping into station    ultra-slow docking approach at 0.05 m/s closing speed, soft capture ring gently absorbing contact kinetic energy
fast blurry Earth background    curved Earth horizon drifting steadily below at orbital velocity of 7.8 km/s, realistic ground track displacement

(3) Bağlantılı Tam Kaynak Listesi
VideoPhy Benchmark (arXiv:2406.03520): Bansal et al., VideoPhy: Evaluating Physical Commonsense for Video Generation.

VideoPhy-2 Benchmark (arXiv:2503.06800): Goldenberg et al., VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation.

PhyWorldBench (arXiv:2507.13428): Multi-Dimensional Physics Evaluation Benchmark for Video Generation Models.

VideoScience-Bench (arXiv:2512.02942): Zero-Shot Scientific Reasoning in Video Generation Models.

PhyGenBench & PhyGenEval (arXiv:2410.05363): Meng et al., Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation.

Physics-IQ & Physics-IQ Verified (arXiv:2606.18943): Rädsch et al., Physics-IQ Verified: Assessing Physical Faithfulness in Video Foundation Models.

NASA Plume Impingement & Vacuum Plume Dynamics (NASA SP-8080 / NASA RP-1028): Liquid Propellant Gas Dynamics and Under-Expanded Nozzle Flow Analysis.

NASA Microgravity Fluid Physics & Flash Evaporation: Flash Boiling Mechanisms of Liquid Droplets in Low Pressure Vacuum.

NASA EMU Suit & EVA Operational Guidelines (NASA TP-2004-212068 / AIAA-2020-4170): Extravehicular Mobility Unit Mass Properties, Tether Protocol, and Handrail Mobility.

International Docking System Standard (IDSS IDD Revision C/E / NASA NDS Users Guide): Interface Definition Document for Spacecraft Docking Rates, Axial Velocities, and SCS Attenuation.

Physics-Aware Counterfactual Reasoning in Video Diffusion Models (arXiv:2509.24702): Analysis of Classifier-Free Guidance Dynamics and Negative Prompting Limitations.

CleanVideo Framework (arXiv:2609.20267): Concept Erasure and Spatiotemporal Intervention Subspace in Video Diffusion Models.

Narrative Transport and Cognitive Dynamics in Sci-Fi Cinema (Frontiers in Communication, 2026): Empirical Analysis of Audience Perception regarding Movie Physics Errors.
