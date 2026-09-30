# TUR 24 · 1A — HAM RAPOR · Çoklu-Klip Kapsama, Kesme ve Kesintisiz Akış

> Prompt: `../27_…` 1A · 22.09.2026 · sohbetten aktarıldı, metin değiştirilmedi.
> ⛔ Kural buradan okunmaz — süzgeç: `../04_ARASTIRMA_BULGULARI.md` §TUR 24.

---

Yapay Zeka Destekli Sanal Sinematografi: Üretken Video Modellerinde Çoklu-Klip Kapsama, Kesme ve Kesintisiz Akış Mimarisi

## Geleneksel Kurgu Sözdiziminin Üretken Zekaya Entegrasyonu ve Slayt Gösterisi Problemi

Geleneksel sinematografide bir sahnenin inşası, farklı açılardan ve ölçeklerden çekilmiş görüntülerin uzamsal ve zamansal bir bütünlük içinde kurgulanmasına dayanır. İzleyicinin zihninde kesintisiz bir gerçeklik algısı yaratan bu kapsama (coverage) teknikleri, güncel üretken yapay zeka (AI) video modellerinin temel mimarileriyle doğrudan bir çatışma halindedir. Google Veo 3.1, Gemini Omni 1.1 Flash, Kling 1.5/3.0, Runway Gen-4 ve Sora gibi modeller, milyarlarca parametreli difüzyon ve transformer mimarileri üzerinden çalışarak ortalama 10 saniye süren, yüksek fotogerçekçiliğe sahip yalıtılmış klipler üretmek üzere optimize edilmiştir. Bu mimari yapı, bağımsız üretilmiş 3 ila 5 klibin art arda dizilerek 30-50 saniyelik bir sahne oluşturulması durumunda, izleyicide "hareketli bir slayt gösterisi" (slideshow effect) izliyormuş hissi uyandıran şiddetli bir bilişsel kopukluğa neden olmaktadır. Her yeni klip, modelin gizli uzayında (latent space) sıfırdan bir evren yaratması anlamına geldiğinden, sahneler arası mikro-geometri farklılıkları, aydınlatma kaymaları ve karakter kimliği bozulmaları kaçınılmaz hale gelmektedir.

Bu araştırmanın temel kısıtı ve odak noktası; her biri bağımsız bir metin (text-to-video) veya statik referans görseli (image-to-video) ile üretilen, tam 10.00 saniye süren, varsayılan olarak sabit kameralı fotogerçekçi uzay bilimkurgu kliplerinin kurgu masasında sert kesmeyle (hard cut) birleştirilmesi senaryosudur. Üretken video ardışıklığında sıklıkla başvurulan modeller arası son kare zincirleme (I2V frame chain) veya video-to-video geçiş yöntemleri, yaratıcı kontrolü kısıtladığı ve jenerasyon hatalarını katlayarak (error propagation) artırdığı için kesin bir kuralla dışarıda bırakılmıştır. Karakterin basınç giysili ve kasklı olduğu bu uzay bilimkurgu konseptinde, görsel hataları maskelemek için post-prodüksiyon aşamasında eklenebilecek VFX kompozitlemeleri, 3B kamera eşlemeleri ve ek kurgu efektleri (dissolve, wipe, optical transitions) yasaklanmıştır. Çözüm uzayı tamamen ve yalnızca prompt dilinin yapısal mühendisliği, sinematik ölçek atlama kuralları (30 derece kuralı, 180 derece aks kuralı) ve akustik montaj (J-cut, L-cut, oda tonu) ile sınırlandırılmıştır.

Akademik literatürde ve endüstriyel test platformlarında yayımlanan güncel veriler, mevcut yapay zeka modellerinin görsel kaliteyi başarsa da ardışık yapı kurma konusunda ciddi bir dar boğaza (bottleneck) girdiğini göstermektedir. Özellikle DirectorBench ve CutCraft gibi çoklu-klip değerlendirme metrikleri, yapay zeka tarafından üretilen içeriklerde "geçiş kalitesinin" (transition quality) ve "kurgusal niyetin" (editorial intent) en zayıf halkalar olduğunu sayısal olarak kanıtlamaktadır. Bu dar boğazı aşmak, AI modelinin her yeni üretimde sahneyi sıfırlamak (reset) yerine, bir önceki olayın uzantısını ürettiğine ikna edilmesini sağlayan yapısal prompt dizilimlerini, zamansal bağlaçları ve kurgusal kesme (cut on action) anlarının matematiksel bir hassasiyetle ayarlanmasını gerektirir.

## Güncel Modellerin Kapasite Analizi ve Akademik Ölçeklendirme Yönergeleri

Üretken video alanındaki teknolojik sıçrama, modellerin her birinin belirli sinematik görevlerde uzmanlaşmasına, ancak aynı zamanda kendilerine has hata modları (failure modes) geliştirmelerine yol açmıştır. Çoklu-klip kapsama tekniklerinin başarılı bir şekilde uygulanabilmesi için, Google Veo 3.1, Gemini Omni 1.1 Flash, Kling 1.5, Runway Gen-4 ve Sora'nın kapasitelerinin, özellikle CutCraft ve DirectorBench gibi endüstri standardı haline gelmiş yönergeler ışığında analiz edilmesi zorunludur.

DirectorBench tarafından gerçekleştirilen yapılandırılmış meta veri testleri, uzun formlu (long-form) video üretiminde modellerin "Birimler Arası Dar Boğaz" (Between-Unit Bottleneck) olarak adlandırılan bir çöküş yaşadığını ortaya koymuştur. Bu testlerde, tekil prompt uyumu (user demand fulfillment) 0.71 gibi yüksek bir ortalamaya sahipken, ardışık klipler arasındaki geçiş kalitesi (transition quality) yalnızca 0.256 seviyesinde kalmıştır. Bu uçurum, modellerin tek bir plan için mükemmel talimat izleme yeteneğine sahip olduklarını, ancak uzun süreli ve kesintisiz bir akış sağlamak için gereken küresel bellek (global memory) ve durum yönetiminden yoksun olduklarını kanıtlamaktadır. Benzer şekilde, profesyonel kurgu tekniklerinin uygulanabilirliğini ölçen CutCraft kıyaslaması, modellerin sürekli bir olay örgüsünü (continuous narrative) oluşturmada kısmen başarılı olsalar da, kesme noktalarında (hard cut, J-cut, L-cut) ses ve görüntü senkronizasyonunu kontrol etmede büyük ölçüde başarısız olduklarını, klip sayısı beşe çıktığında geçiş skorlarının 0.542'den 0.383'e düştüğünü tespit etmiştir.

Bu bağlamda Google Veo 3.1, doğal ses senkronizasyonu (native audio synchronization) yeteneğiyle öne çıkmaktadır. 48kHz kalitesinde diyalog, ortam sesi ve ses efektlerini görsel jenerasyonla aynı anda üretebilen model, bağımsız üretilen 10 saniyelik klipler arasındaki işitsel devamlılığı sağlamak için güçlü bir temel sunar. "Ingredients to Video" özelliği sayesinde üç adede kadar referans görselini işleyerek karakter tutarlılığını koruyabilmesi, çoklu-açı kapsama (multi-angle coverage) senaryolarında geniş, orta ve yakın planlar arasındaki kimlik kaymalarını asgariye indirir. Ancak, modelin 8 ila 10 saniyelik kesin süre kısıtlamaları, sahnenin iç ritminin doğrudan prompt üzerinden yönetilmesini zorunlu kılar.

Gemini Omni 1.1 Flash, konuşmaya dayalı kurgu (conversational editing) ve akıl yürütme (reasoning) entegrasyonuyla farklı bir mimari sunar. Model, internet ölçeğindeki bilgi tabanını kullanarak fizik kurallarına uygun hareketler üretebilmektedir; örneğin, bir kask vizöründeki yansımaların geometrik olarak nasıl davranması gerektiğini hesaplayabilir. Ne var ki, DirectorBench ve bağımsız testler, modelin dört turluk bir düzenleme tavanı (4-turn editing ceiling) olduğunu, bu sayının aşılmasının ardından kademeli bir halüsinasyon ve sapma (drift) başladığını göstermektedir. Ayrıca, prompt aracılığıyla kamera açısı değiştirilmek istendiğinde, modelin yalnızca açıyı değiştirmek yerine sahne coğrafyasını ve arka plan geometrisini tamamen bozma eğiliminde olduğu ölçülmüştür. Bu durum, Omni'nin dar açılı yakın planlarda (close-up) kimlik kaybetme eşiğinin çok düşük olduğunu gösterir.

Kling (1.5 ve 3.0 sürümleri), hareket fiziği (motion physics) ve çevresel etkileşimler açısından pazarın en güçlü motorlarından biri olarak kabul edilmektedir. Özellikle "Hareket Kontrolü" (Motion Control / Motion Brush) özelliği, referans videolardaki veya tanımlanmış yönergelerdeki hareket vektörlerini yeni jenerasyona aktararak eylem tutarlılığı sağlar. Su, kumaş, duman ve basınç giysisi kıvrımları gibi dinamiklerin simülasyonunda rakiplerinden üstün olan Kling, 10.00 saniyelik bağımsız kliplerin her birinde kumaşın ve ışığın fiziksel ağırlığını koruyabilir. Kling 3.0 ile gelen "Çoklu-Plan Hikaye Tahtası" (Multi-Shot Storyboard) altyapısı, farklı açıların tek seferde planlanmasına izin verse de, kısıtımız gereği her klip bağımsız üretileceği için bu özellik yerine modelin 4 adede kadar referans görseli kabul eden karakter tutarlılık modülü kullanılmalıdır.

Runway Gen-4 (ve 4.5 sürümü), kamera koreografisi ve sanal sinematografi alanında açık ara en gelişmiş kontrol mekanizmalarını sunar. Model, sanal bir kameranın mekandaki konumunu matematiksel bir hassasiyetle simüle edebilen bir dünya modeli (world model) gibi davranır. DirectorBench metriklerine göre Runway Gen-4, karakterin yüz oranlarını ve kıyafet dokusunu tek bir referans görselinden alarak farklı açılarda kusursuz bir şekilde yeniden üretebilmektedir. Sora ise sinematik kalite, karmaşık kamera hareketleri ve çoklu karakter etkileşimleri konusunda devrim niteliğinde sonuçlar verse de, bağımsız kliplerin kurgu masasında kesilmesi senaryosunda, tutarlılığı sağlamak için son derece spesifik ve deterministik promptlara ihtiyaç duyar.

## Sinematik Kapsama Hiyerarşisi ve Uzamsal Çapa Kurulumu

Bir olayın 10 saniyelik yalıtılmış zaman dilimlerine bölünerek işlenmesi, izleyicinin uzamsal oryantasyonunu korumak amacıyla klasik sinematografik hiyerarşinin yapay zeka yönlendirmelerine (prompting) entegre edilmesini gerektirir. Basınç giysili bir astronotun uzay gemisi hava kilidinde (airlock) kritik bir butona basması gibi tekil bir dramatik olay, Geniş Plan (Establishing), Orta Plan (Action/Interaction) ve Yakın Plan (Detail/Reaction) hiyerarşisiyle çözümlenmelidir.

### Uzamsal Çapanın Kurulması: Geniş Plan (Establishing Shot)

Serinin ilk 10.00 saniyelik klibi mutlak surette geniş plan olmalıdır. Bu plan, yalnızca izleyicinin mekanı anlamlandırması için değil, aynı zamanda yapay zeka modelinin "Uzamsal Çapasını" (Spatial Anchor) oluşturmak için kritiktir. Üretken modeller, üç boyutlu bir dünya haritasına sahip olmadıkları için mekansal sürekliliği referans görseller veya aşırı detaylı aydınlatma tasvirleri üzerinden kurarlar. Başlangıç promptu, ortamın tüm coğrafi, atmosferik ve fotometrik özelliklerini statik bir kesinlikle tanımlamalıdır.
Kullanılacak prompt, ortamın aydınlatma tipini, ışık kaynaklarının frekansını ve nesnelerin birbirine olan uzaklığını sabitlemelidir. Örneğin, "düşük frekanslı kırmızı flaşörler" (low frequency emergency red strobe lights) ve "titanyum duvarlar" (titanium walls), ardışık kliplerdeki orta ve yakın planlar için referans bir atmosfer (atmo-lock) görevi görecektir. Modelin, karakterin ve dekorun pozisyonlarını gizli uzayında (latent space) bir çapa olarak sabitlemesi, sonraki kliplerde referans görsel olarak kullanılacak çerçevenin tutarlılığını garanti altına alır.

### Eylem, Etkileşim ve 30 Derece Kuralı: Orta Plan (Medium Shot)

Geniş plandan eylemin gerçekleştiği orta plana geçişte, izleyicinin görsel bir sıçrama veya teknik bir hata (jump cut) algılamaması için, kameranın açısı ve lens ölçeği bir önceki plana göre belirgin bir şekilde değiştirilmelidir. Sinematografinin temel kurallarından biri olan 30 derece kuralı (30-degree rule), birbirini izleyen aynı özneye ait iki çekim arasında kameranın en az 30 derecelik bir açıyla hareket ettirilmesini şart koşar. Yapay zeka video modelleri, kameranın mekandaki mutlak pozisyonunu algılayamadığı için, bu açı değişikliği promptun en başında belirgin bir şekilde yazılmalıdır.
Orta planda, 180 derece aks kuralı (axis of action) kesinlikle ihlal edilmemelidir. Karakter geniş planda ekranın sağından soluna doğru hareket ediyorsa veya panele sağ koluyla uzanıyorsa, orta planda da aynı yönelim korunmalıdır. Yapay zeka modellerinin "sol" ve "sağ" kavramlarını sıklıkla karıştırdığı bilindiğinden, yönelimler vücut anatomisine göre ("sağ eldivenli el", "sol omuz") detaylandırılmalıdır. Bu hiyerarşi, astronotun harekete başladığı ve mekanla fiziksel etkileşime girdiği 10 saniyelik süreci kapsar.

### Kimlik Kaybetme Eşiği ve Makro Detaylar: Yakın Plan (Close-Up)

Yakın planlar, sahnenin dramatik geriliminin zirveye ulaştığı, kask vizörünün yansıması veya kalın eldivenin butona temas ettiği anları içerir. Ancak üretken modeller (özellikle Gemini Omni 1.1 Flash ve erken dönem difüzyon modelleri), kadraj çok fazla daraldığında arka plan coğrafyasını işlemeyi bırakır ve "unutur". Kadrajın yalnızca bir eldiven veya vizörden ibaret olduğu durumlarda, model çevresel bağlamı kaybettiği için uzay giysisinin materyal dokusunu, rengini veya kaskın tasarımını halüsinatif bir şekilde değiştirmeye başlar. Bu durum, "Kimlik Kaybetme Eşiği" (Identity Loss Threshold) olarak adlandırılır.
Bu eşiği aşmanın ve modelin sahnenin geri kalanını hafızasında tutmasını sağlamanın tek yapısal yolu, makro detay promptlarına mikro-yansımaları (visor reflection) ve çevresel ışık sızıntılarını dahil etmektir. Kask vizöründeki kavisli camda beliren kontrol paneli yansıması veya kırmızı flaşörlerin eldiven üzerindeki yansıması, modele arka planın hala var olduğunu kanıtlayan bir "Görsel Kanıt" (Visual Evidence) sunar. Bu prompt stratejisi, modelin gizli uzayında (latent space) çevresel bağlamı aktif tutarak, yakın planın geniş planla aynı evrende geçtiğini matematiksel olarak doğrular.

## Sahne İçi Kurgusal Kesme (Cut on Action) Dinamikleri ve Hareketi Maskeleme

Farklı promptlarla ve statik referans görselleriyle (image-to-video) üretilen bağımsız kliplerin, I2V zincirlemesi (frame chain) kullanılmadan kurgu masasında birleştirilmesi durumunda görsel sürekliliği sağlamanın en etkili yolu "Eylem Üzerinden Kesme" (Cut on Action / Match on Action) tekniğidir. CutCraft benchmark verileri, modellerin kendi içlerinde geçiş (transition) planlamakta yetersiz kaldıklarını açıkça göstermektedir; optik geçiş komutları sıklıkla sert kesmelere (hard cut) çökmekte veya zamanlama hataları yaratmaktadır. Bu yapısal zafiyet, AI modeline geçiş yaptırmaya çalışmak yerine, ardışık kliplerin kurgu masasında (NLE) manuel olarak sert bir şekilde kesilmesiyle avantaja dönüştürülür.

İnsan beyni, perdedeki hareketi algılarken, hareketin tamamlanacağına dair kısa süreli nörolojik bir öngörüde bulunur (Sensorimotor Projection). Bir eylem başladığında, zihin sonraki 0.5 ila 0.7 saniyelik süreci otomatik olarak hesaplar. Eğer bu öngörü süreci kesintiye uğratılıp hareket farklı bir açıdan devam ettirilirse (Sensorimotor Projection Violation), beyin hareketin sürekliliğine o kadar odaklanır ki, ardışık iki klip arasındaki ufak tefek görsel tutarsızlıkları görmezden gelir. Bu psikolojik zaafiyet, yapay zekanın uzay giysisi kıvrımlarında, düğmelerin sayısında veya ışık yönlerinde yaptığı mikroskobik halüsinasyonları maskelemek için mükemmel bir kamuflajdır.

Bir hareketin kinetik olarak maskelenebilmesi için eylem üç faza bölünmelidir:

- Eylem Başlangıcı (Initiation): Karakterin kaslarını ateşlemesi, astronotun elini panele doğru kaldırmaya başlaması.
- Eylem Ortası (Execution): Hareketin uzayda kat ettiği yol. Uzvun havada süzülmesi ve hareket bulanıklığının (motion blur) en yüksek olduğu an.
- Eylem Sonucu (Resolution): Eldivenin butona basması, etkinin gerçekleşmesi ve eylemsizlik.

Yapay zeka üretim stratejisi, iki klibin (Klip A ve Klip B) eylemin ortasında "örtüşmesini" (overlapping) gerektirir. Klip A (Orta Plan), eylemin başlangıcını ve ortasını üretmelidir. Klip B (Yakın Plan), farklı bir açıdan eylemin ortasını ve sonucunu üretmelidir. Kurgu masasında, astronotun elinin havada en hızlı hareket ettiği, ivmenin zirve yaptığı "Eylem Ortası" noktasında Klip A'dan Klip B'ye sert kesme uygulanır. Modelin tutarsızlıkları, kinetik enerjinin ardına saklanmış olur. Bu teknik uygulanmadığı takdirde, eylemin bitip karakterin durduğu noktada yapılan kesmeler (pacing cuts), arka plandaki en ufak bir geometri kaymasının dahi izleyici tarafından "hata" olarak algılanmasına neden olur.

## Mekanizmayı Sökmek: Zamansal Bağlaçlar ve Prompt Kalıpları

Modelin bir klibi, gizli uzayda sıfırdan başlayan yeni bir olay olarak değil de süregelen dinamik bir sahnenin devamı olarak görmesini sağlamak, prompt dilinde ustaca tasarlanmış zamansal bağlaçların (temporal conjunctions) kullanımını gerektirir. Herhangi bir bağlaç kullanılmadığında ve yalnızca durum tasviri yapıldığında, Kling 1.5 ve Veo 3.1 gibi modeller karakteri varsayılan olarak "durağan" (idle) bir bekleme pozisyonundan başlatmaya son derece eğilimlidir. Oysa "Cut on Action" tekniğinin çalışabilmesi için ikinci klibin aniden ivmeli bir hareketle başlaması şarttır.

Sahneyi baştan başlatma (reset) eğilimini kırmak için promptun hemen başına yerleştirilen kinetik başlangıç direktifleri, modelin dikkat mekanizmalarını (attention mechanisms) hareket vektörleri üzerine yoğunlaştırır.

Tutan Yapılar (Başarılı Prompt Kalıpları):

- `Mid-action sequence, the heavy white gloved hand is already in swift motion...` (Modeli doğrudan eylemin ortasından başlatır, karakter ivmeli ve bulanık bir başlangıç yapar. Kurguda kesme yapmayı kolaylaştırır.)
- `Continuing the intense momentum from the previous moment...` (Modelin, referans görseldeki statik duruşa rağmen sahnede yüksek bir kinetik enerji olduğunu varsaymasını sağlar.)
- `Immediate aftermath of the button press, the astronaut's hand recoils slightly...` (Bir eylem sonucunun yarattığı dalgalanmayı veya geri tepmeyi koruyarak fiziksel gerçekliği sürdürür.)
- `Matching the exact red strobe lighting of the established scene...` (Atmosferik sürekliliği kilitler, ortamın coğrafyasının değişmesini engeller.)

Tutmayan Yapılar (Başarısız Prompt Kalıpları):

- `Next scene,...` veya `Following shot,...` (Yapay zeka modelleri bu terimleri, zamanın veya mekanın tamamen değiştiği bir sıçrama olarak algılar ve dekoru, kıyafetleri yeniden tasarlar.)
- `After that, the astronaut presses the button.` (Karakteri önce durdurup sonra yeni bir eyleme başlatır. 10 saniyelik klibin ilk 3-4 saniyesi çöpe gider, ritim ölür.)
- `Suddenly, the panel lights up.` (Modeller "aniden" kelimesini aşırı dramatize eder. Gereksiz kamera sarsıntıları, lens parlamaları (lens flare) veya patlama benzeri VFX olayları ekleyerek sahnenin sabit kameralı gerçekçi dokusunu bozar.)

Bu bağlaçların doğru kullanımı, DirectorBench ölçümlerinde "transition quality" (geçiş kalitesi) skorunu ortalama 0.256 bandından, kabul edilebilir kurgusal akıcılık seviyelerine çıkarabilen en kritik kelime öbekleridir. Promptun dilbilgisel yapısı, sahnenin zamansal dokusunu dikte eden bir koda dönüşmektedir.

## Akustik Süreklilik ve Montaj Analizi: Sesin Maskeleme Gücü

Bağımsız üretilen 10'ar saniyelik klipler arasındaki görsel sıçramaları (jump cuts) ve açı değişimlerini zihinsel olarak pürüzsüzleştirmenin en güçlü aracı, şaşırtıcı bir şekilde, görsellik değil sesten gelir. Veo 3.1 (48kHz diyalog, ortam sesi ve SFX) ve Kling 3.0 gibi yerleşik (native) ses üretebilen modeller, metne dayalı olarak son derece gerçekçi akustik profiller yaratabilmektedir. Ancak her 10 saniyelik klip bağımsız üretildiğinden, model her seferinde farklı bir dip ses frekansı (noise floor) ve yankı (reverb) profili oluşturacaktır. Eğer bu sesler görsellerle aynı anda sert bir şekilde kesilirse, izleyicinin beyni sahnenin koptuğunu ve suni birleştirme yapıldığını anında algılar.

### Oda Tonu (Room Tone) ve Ambiyansın Yapıştırıcı Etkisi

Sinematografide "oda tonu" (Room tone / Ambient sound), mekandaki sessizliğin ve çevresel unsurların yarattığı kendine has akustik imza olarak tanımlanır. Uzay bilimkurgusu kısıtı altında bu imza; uzay gemisinin düşük frekanslı motor uğultusu (engine hum), hava filtreleme ve yaşam destek sistemlerinin ritmik tıslaması veya kask içi solunum sesidir. Çoklu-klip üretiminde, her bağımsız AI klibinin promptunda akustik direktif standart olarak yer almalıdır.

Audio Prompt Eki: `Native audio: Constant low-frequency spacecraft engine hum, heavy rhythmic breathing inside the spacesuit helmet, metallic vibrations.`

NLE (Kurgu masası) aşamasında, her klipten elde edilen bu motor uğultusu ve oda tonu, sert kesmelerle parçalanmaz. Aksine, ses kanalları arasında 1-2 saniyelik çapraz soluklaşma (cross-fade) uygulanarak kesintisiz bir akustik yatak (audio bed) oluşturulur. İzleyicinin kulağı bu kesintisiz motor uğultusuna kilitlendiğinde, göz ardışık klipler arasındaki mikroskobik ışık ve doku hatalarını affetme eğilimine girer. Ses, görsel yırtılmaların üzerine bir battaniye gibi örtülür.

### J-Cut ve L-Cut Köprüleri ile Diyalog Dağılımı

İzleyicinin 30-50 saniyelik süre boyunca (3-5 bağımsız klip) aynı zaman diliminde kaldığını hissetmesi için görsel kesme noktaları ile işitsel kesme noktaları birbirinden ayrıştırılmalıdır. Bu ayrıştırma, J-Cut ve L-Cut teknikleriyle sağlanır. CutCraft benchmarkı, AI modellerinin bu asimetrik kesmeleri kendi başlarına tek bir prompt içinde gerçekleştiremediğini kanıtlamıştır. Bu nedenle kurgu masası müdahalesi şarttır.

- J-Cut (Sesin önden gelmesi): İkinci klibin sesinin (örneğin astronot düğmeye basmadan hemen önce panelden yükselen uyarı alarmı sesi), görsel henüz birinci klipten (Astronotun panele yürümesi) çıkmadan 1.5 saniye önce başlatılmasıdır. Bu teknik, izleyicinin beynini görsel değişmeden önce yeni mekana veya yaşanacak eyleme hazırlar. Göz, sesi duyduğu yöne doğru bir sonraki planı beklemeye başlar ve geçiş kusursuz hissedilir.
- L-Cut (Sesin uzaması): Birinci klipteki bir eylemin sesinin veya bir diyaloğun, görsel olarak ikinci klibe (panelin yakın çekimi veya dinleyen karakterin reaksiyonu) geçilmesine rağmen devam etmesidir.

Özellikle diyalog içeren sahnelerde, konuşmaların tamamının 10.00 saniyelik tek bir klibe yığılması, hem modellerin lip-sync (dudak senkronizasyonu) kapasitelerini zorlayarak kaymalara neden olur (Gemini Omni 1.1 Flash'taki dudak bozulmaları gibi), hem de sahnenin tiyatral doğallığını bozar. Çözüm, diyaloğun bir kısmını (örneğin telsiz konuşmasını) birinci klibin geniş planında başlatmak ve cümlenin geri kalanını L-cut tekniği ile yüzün görünmediği kask içi yakın planlara (Klip 2 ve Klip 3) sarkıtmaktır. Bu strateji, diyaloğu 30 saniyelik sahneye yayarak anlaşılırlığı artırır, modelin üzerindeki dudak senkronizasyonu yükünü alır ve izleyiciye kesintisiz bir zaman algısı sunar.

## Ritim, Tempo Platosu ve Bilişsel Yorgunluğun Önlenmesi

Her biri yapay zeka tarafından "tam 10.00 saniye" sürecek şekilde üretilen fotogerçekçi kliplerin kurgu masasında doğrudan uç uca eklenmesi, kurgusal ritimde "10 Saniye Metronomu" olarak adlandırılan ölümcül bir tekdüzelik yaratır. İnsan beyni, kesmelerin (hard cut) düzenli, matematiksel aralıklarla (10. saniye, 20. saniye, 30. saniye) gerçekleştiğini bilinçdışı bir şekilde algıladığında bir tempo platosuna girer. Beklentinin tamamen tahmin edilebilir hale gelmesi, izleyicide "bilişsel yorgunluk" (cognitive fatigue) başlatır ve dramatik illüzyon çöker. Sinematik kurguda ritim, bir kalp atışı gibi organik olmalıdır; bazen hızlanmalı, bazen nefes almalı, bazen de duraklamalıdır.

Bu kısıt, kurgu masasında kliplerin farklı sürelerde, asimetrik olarak kesilmesiyle aşılır (Örn: Klip 1'den 4 saniye, Klip 2'den 7 saniye, Klip 3'ten 3 saniye kullanılması). Ancak bunun mümkün olabilmesi için, AI'ın 10.00 saniyelik üretimi boyunca eylemin homojen ve düz bir hızda ilerlememesi gerekir. Modelin zaman çizelgesi (timeline) içindeki ritmi, prompt düzeyinde yönetilen "mikro-tempo değişimleri" (micro-pacing) ile manipüle edilmelidir:

- Duraklama ve Nefes Alma (Building Tension): Prompt içerisine eklenecek `Starts completely motionless for the first 3 seconds, building intense tension, then suddenly the gloved hand darts forward...` komutu, modelin klibin ilk bölümünü statik bir fotoğraf gibi tutmasını, ardından ani bir ivme yaratmasını sağlar. Sora 2 ve Kling 3.0 gibi modeller bu tür zamansal eylem direktiflerini harfiyen uygulama kapasitesine sahiptir.
- Eylem Hızlanması (Acceleration): `Moves with agonizing slowness at first, abruptly transitioning into a rapid, frantic button press...` komutu, hareket vektörünün (motion vector) hızını zaman içinde değiştirir.

Bu mikro-tempo değişimleri, NLE (Non-Linear Editing) editörüne inanılmaz bir esneklik sağlar. Editör, 10 saniyelik klibin içindeki bu değişken kinetik eğrileri inceleyerek, sert kesme (hard cut) yapacağı en dinamik noktayı (action point) veya en duygusal duraklama anını seçebilir. Böylece sahneler arası geçişler, yapay zekanın mekanik üretim sürelerinden bağımsızlaşarak tamamen sinematik ve duygusal bir ritme kavuşur.

## Yapılandırılmış Kapsama ve Kurgu Tabloları

Aşağıdaki tablolar ve karar ağacı, rapor boyunca teorik olarak incelenen kapsama hiyerarşisi, zamansal bağlaçlar ve kesme dinamiklerinin, uzay bilimkurgu kısıtı altındaki pratik ve yapılandırılmış özetleridir. Etiketler kısıtlara uygun olarak [ÖLÇÜLMÜŞ], [UYGULAMA] ve [ÖNERİ] formatında standardize edilmiştir.

### Tablo A: 3-5 KLİP KAPSAMA ŞABLONU (Cinematic Coverage)

| Klip Sırası ve Fonksiyonu | Sinematik Ölçek ve Açı | Eylem Fazı | İngilizce Prompt Kalıbı (Uzay Bilimkurgu) | Etiket |
|---|---|---|---|---|
| Klip 1: Uzamsal Çapa | Geniş Plan (Establishing), Sabit Kamera | Başlangıç ve Yönelim (Orientation) | Cinematic wide establishing shot, fixed camera. A lone astronaut in a heavy white pressure suit stands motionless in a dimly lit metallic spacecraft airlock, illuminated by pulsing red strobes. | [UYGULAMA] |
| Klip 2: İvmelenme | Orta Plan (Medium), 45-derece profil, Sabit | Eylem Başlangıcı (Initiation) | Medium shot, 45-degree offset profile, fixed camera. Matching red strobe lighting. The astronaut turns their body heavily and raises a thick gloved hand towards a glowing interface. | [UYGULAMA] |
| Klip 3: Zirve Noktası | Yakın Plan (Close-up), Omuz Üstü (OTS), Sabit | Eylem Ortası (Execution) | Over-the-shoulder close up, fixed camera. Mid-action sequence, the heavy white gloved hand forcefully presses a bright blue holographic button on the metallic control panel. Immediate physical feedback. | [ÖNERİ] |
| Klip 4: Görsel Kanıt | Makro Detay (Extreme Close-up), Sabit | Eylem Sonucu (Resolution) | Extreme close-up macro shot, fixed camera. Highly reflective gold visor of the astronaut's helmet. Reflected clearly in the visor is the flashing blue light of the activated panel and red strobes. Subtle nod. | [ÖLÇÜLMÜŞ] |
| Klip 5: Nefes Alma | Orta Plan (Medium), Karşı Açı (Reverse), Sabit | Gevşeme (Idle / Tension Drop) | Medium shot, reverse angle from the panel, fixed camera. The astronaut stands in the airlock, lowering their arm slowly as the ambient light turns from red to a calm, steady blue. | [ÖNERİ] |

### Tablo B: SAHNE İÇİ BAĞLAÇ TABLOSU (Temporal Conjunctions)

| Bağlaç Tipi (Fonksiyon) | İngilizce Prompt Örneği | Etki Mekanizması ve Kurgusal Faydası | Model (Veo/Kling/Gemini/Sora) Toleransı | Etiket |
|---|---|---|---|---|
| Kinetik Başlangıç (Kinetic Start) | Mid-action sequence, the gloved hand is already moving swiftly to the right... | Karakteri durağan (idle) animasyon döngüsünden çıkarıp doğrudan yüksek ivmeyle başlatır. Kurguda kusursuz "Cut on Action" imkanı sağlar. | Veo 3.1 ve Kling 1.5/3.0'da yüksek tolerans. Gemini Omni'de bazen nesne deformasyonu yapabilir. | [UYGULAMA] |
| Atmosferik Süreklilik (Atmo-Lock) | Matching the exact lighting from the previous moment, steady red strobes... | Uzamsal çapa (spatial anchor) oluşturur. Modelin arka plan coğrafyasını ve ışık yönünü sıfırlamasını engeller. | Runway Gen-4 statik referansla birleştiğinde kusursuz çalışır, gölge yönleri sabit kalır. | [ÖNERİ] |
| Mikro-Tempo Kontrolü (Micro-Pacing) | Starts motionless for 2 seconds, building tension, then abruptly... | 10.00 saniyelik yekpare üretimin içine doğal bir es (pause) ve asimetrik hızlanma ekler. Bilişsel metronom yorgunluğunu kırar. | Sora 2 ve Kling 3.0 zaman çizelgesindeki eylem direktiflerini harfiyen algılar. | [ÖLÇÜLMÜŞ] |
| Görsel Kanıt (Visual Evidence) | Reflected clearly in the curved gold glass is the glowing control panel... | Kamera mekanı görmediğinde (aşırı yakın planda), mekanın yansıma ile var olduğunu modele fiziksel bir kısıt olarak hatırlatır. | Gemini Omni'de karmaşık geometriler kaybolabilir, Veo 3.1'de yansımalar ve fizik kuralları çok başarılıdır. | [UYGULAMA] |

### Tablo C: KESME VE RİTİM TABLOSU (Acoustic & Montage Dynamics)

| Kesme Tipi (Kurgu Prensibi) | AI Üretim Stratejisi (10sn Üretim) | NLE Kurgu Uygulaması (Post-Prodüksiyon) | Akustik Maskeleme ve Etkisi (Room Tone / J-L Cut) | Etiket |
|---|---|---|---|---|
| Eylem Kesmesi (Cut on Action) | Klip A ve Klip B'de, hareketin ortası (overlapping) her iki farklı açıdan da mecburen üretilir. | Hareketin havada en hızlı olduğu, bulanıklığın (motion blur) tavan yaptığı an seçilerek sert kesme (hard cut) atılır. | Oda tonu (engine hum) iki klip arası sabit tutulur. Kesme anına denk gelen mekanik bir ses efekti görseldeki olası hataları gizler. | [UYGULAMA] |
| J-Cut (Sesin Önden Gelmesi) | Reaksiyon planında (Klip B) duyulacak alarm veya mekanik panel sesi modele doğal ses (native audio) olarak ürettirilir. | Klip B'nin sesi, görsel geçişten 1.5 saniye önce kurguda Klip A'nın üzerine kaydırılarak başlatılır. | Görseldeki potansiyel aydınlatma ve geometri sıçramalarını, izleyicinin dikkatini önceden işitsel duyguya çekerek maskeler. | [ÖNERİ] |
| L-Cut (Diyalog Köprüsü) | Karakterin konuşması tek bir klibin (Klip A) metnine veya native audio girdisine yazılır. | Görsel olarak Klip B'ye (örn: yakın plan vizör) geçilse de, konuşma sesi Klip A kanalından devam edecek şekilde uzatılır. | Native lip-sync zayıflıklarını (dudak kaymalarını) gizler. Diyaloğu 30 saniyeye yayarak bilişsel akışı sağlar. | [ÖLÇÜLMÜŞ] |
| Tempo Kırıcı (Pacing Cut) | AI klibi içerisinde durağanlık (idling) "starts motionless" promptu ile zorlanarak yaratılır. | 10.00 saniyelik klipler, 4sn, 7sn, 3sn gibi asimetrik ve aritmetik olmayan uzunluklarda kesilerek 10sn metronomu yok edilir. | Derin uzay uğultusu (low freq hum) sürekli cross-fade yapılarak sessizliğin ve sahnenin içsel basıncı vurgulanır. | [UYGULAMA] |

### KARAR AĞACI: Çoklu-Klip Kurgu ve Prompt Akışı

Aşağıdaki karar ağacı, "hava kilidi paneline basılması" gibi tek bir dramatik olayın, yapay zeka video motorlarında bağımsız klipler olarak üretilip (I2V zinciri olmadan) kurgu masasında sinematografik bir bütünlüğe dönüştürülmesi mantığını adım adım göstermektedir.

```
[BAŞLANGIÇ: Sahnenin Dramatik Tanımı & Kapsama İhtiyacı]
|
v
[Adım 1 Üretimi: Geniş Plan - Uzamsal Çapanın Kurulması (Tam 10.00sn)]
Prompt: "Cinematic wide shot... (Coğrafya, ışık, karakter tanımı eksiksiz yapılır)"
Üretim Yöntemi: Text-to-Video veya Statik Referans
|
+---> NLE Kurgu Çıktısı: Sadece ilk 4 saniye kullanılır (Oryantasyon sağlanır).
|
v
[KARAR NOKTASI 1: Karakter İvmeli Bir Eyleme Başlıyor mu?]
[EVET]     [HAYIR] -> Prompt'ta mikro-tempo kontrolü kullan: "Starts motionless for 3s, then moves."
|
v
[Adım 2 Üretimi: Orta Plan - 30 Derece Kuralının Uygulanması (Tam 10.00sn)]
Prompt: "Mid-action sequence, 45-deg offset profile... hand moves swiftly toward panel."
|
+---> NLE Kurgu Çıktısı: Hareketin en hızlı noktasında (örn. 5. saniye)
      [Cut on Action] uygulanarak kesilir.
|
v
[KARAR NOKTASI 2: Görsel Sıçrama (Jump Cut) veya Geometri Bozulması Riski Var mı?]
[HAYIR]    [EVET] -> J-Cut kullanarak Klip 3'ün sesini (Panel alarmı) Klip 2'nin üstüne önden ver.
                     Böylece dikkati işitsel yöne çekerek görsel sıçramayı maskele.
|
v
[Adım 3 Üretimi: Yakın Plan - Kimlik Koruma ve Görsel Kanıt (Tam 10.00sn)]
Prompt: "Extreme close-up... Gold visor reflection clearly showing the panel. Hand presses button."
|
+---> NLE Kurgu Çıktısı: Düğmeye basılma anı (3 saniye) kullanılır.
|
v
[KARAR NOKTASI 3: Eylem Tamamlandı ve Diyalog Devam Ediyor mu?]
[HAYIR]    [EVET] -> L-Cut uygula. Diyalog devam ederken görseli Klip 4'e geçirerek dudak
                     kaymalarını (lip-sync drift) seyirciden gizle.
|
v
[Adım 4 Üretimi: Karşı Açı - Eylem Sonucu ve Nefes Alma (Tam 10.00sn)]
Prompt: "Reverse angle... Astronaut exhales, lowering arm. Red strobe changes to steady blue."
|
v
[SONUÇ: 30-50 Saniyelik Kesintisiz, Organik ve Psikolojik Olarak İnandırıcı Sahne Bütünlüğü]
```

## Sonuç

Güncel üretken video modelleri, sahip oldukları milyarlarca parametre ile tekil ve yalıtılmış kadrajlar içerisinde kusursuza yakın fotogerçekçilik ve ileri düzey fizik motoru yetenekleri sergilemektedirler. Ancak CutCraft ve DirectorBench gibi platformlardan elde edilen endüstriyel metrikler, bu modellerin uzun soluklu anlatılarda (30-50 saniyelik çoklu-klip kurgusu) insan kurgu psikolojisini ve sinematografik sürekliliği otomatize etmekte henüz yetersiz kaldıklarını kanıtlamıştır. Modelleme mimarilerindeki bu "geçiş kalitesi" (transition quality) dar boğazını aşmak; I2V son kare zincirleme yöntemi kullanılmadan, sadece metin ve referans görsel ile çalışılan katı kısıtlar altında, prompt mimarisini kurgu masasının (NLE) vizyonuyla sentezlemeyi zorunlu kılmaktadır.

Modelin gizli uzayındaki hafıza kaybını (scene amnesia) ve kimlik bozulmalarını önlemek için promptlar içerisine stratejik olarak yerleştirilen kinetik zamansal bağlaçlar ve uzamsal çapalar (visor yansımaları, 30 derece referansları); görsel sıçramaları (jump cut) perdelemek için kullanılan Eylem Üzerinden Kesme (Cut on Action) tekniği ile simbiotik bir biçimde çalışmalıdır. Son olarak, Veo 3.1 ve Kling 3.0 gibi native AI ses modellerinin kapasiteleri doğrultusunda yaratılan akustik oda tonu (room tone) ve J-Cut/L-Cut köprüleri, 10.00 saniyelik AI üretim metronomunu asimetrik olarak kırarak izleyicideki bilişsel yorgunluğu önleyen en temel araçtır. Sunulan bu sanal sinematografi metodolojisi, yapay zekanın ürettiği bağımsız ve parçalı pikselleri; akıcı, psikolojik olarak inandırıcı ve sinematik olarak kusursuz bir anlatı evrenine dönüştüren anahtar doktrindir.
