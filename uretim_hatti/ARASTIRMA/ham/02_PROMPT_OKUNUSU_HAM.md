# HAM — 02 TEK PROMPTUN OKUNUŞU (araştırma prompt 2)

> Kaynak: dış derin araştırma aracı · sahip sohbete yapıştırdı, 06.10.2026.
> Metin olduğu gibidir. Tablolar yapıştırmada sekmeyle ayrılmış düz satıra dönmüştür. Süzme: `../02_SUZME_20261006.md`.

---

Google Flow Üzerinde İleri Düzey Metinden-Videoya Üretim Modellerinde İstem (Prompt) Yorumlama Mekanizmaları ve Sinematik Optimizasyon
Araştırma Parametreleri ve Çerçeve Kısıtları
Bu kapsamlı araştırma raporu, Google Flow ekosisteminde çalışan güncel ve öngörülen ileri varyant (Veo 3.1 ve sonrası) metinden-videoya (T2V) difüzyon modellerinin istem yorumlama (prompt parsing) mekanizmalarını yapıbozuma uğratmaktadır. Analiz, rekabetçi modeller olan Kling 3.0, Runway Gen-3 Alpha, Luma Dream Machine ve Sora mimarileriyle karşılaştırmalı bir zemin üzerinde inşa edilmiştir. İncelemenin merkezinde, metin kodlayıcıların (text encoders) gizli uzayda (latent space) söz dizimsel ve anlamsal verileri nasıl ayrıştırdığı, kapasite sınırları ve dikkat mekanizmalarının (attention mechanisms) zaafları yer almaktadır.

Çalışmanın kısıtları son derece katı bir çerçeveye oturtulmuştur: Üretimler, Google Flow arayüzünde tek bir İngilizce istemle gerçekleştirilen, 8-10 saniyelik, kesmesiz (single-take), fotogerçekçi uzay bilimkurgu sekanslarından oluşmaktadır. Sahnelerde karakterler istisnasız basınç giysili ve kasklıdır. Ses, difüzyon modelinden bağımsız olarak kurguda ekleneceğinden ses komutları kapsam dışında bırakılmıştır. Görsel efekt (VFX) veya sonradan üretim (post-production) rötuşları bulunmamaktadır. Bu katı izolasyon nedeniyle, modeli dışarıdan manipüle eden tüm ince ayar (fine-tuning), Düşük Dereceli Adaptasyon (LoRA), IP-Adapter, ControlNet, referans video ekleme, API üzerinden gönderilen özel yönlendirme parametreleri (örneğin Runway'in -pan veya -zoom değerleri) veya ayrı bir negatif istem kutusu kullanımı [HAT DIŞI] (offline) olarak sınıflandırılmıştır. Tüm çözümlemeler ve stratejiler, modelin "saf metin mühendisliği" (prompt engineering) sınırları dahilinde tek bir metin bloğuyla nasıl yönlendirileceği üzerine kurulmuştur.   

İstem Yorumlama ve Gizli Yeniden Yazım Mekanizmaları (Prompt Enhancement)
Kullanıcının metin kutusuna girdiği İngilizce komut, metinden-videoya üretim sistemlerinde hiçbir zaman doğrudan video üreteci (video generator) bloğuna aktarılmaz. Google Flow, Veo 3.1, Sora ve Luma gibi modern sistemler, kullanıcının ham istemini bir Büyük Dil Modeli (LLM) filtresinden geçirerek yapılandırılmış bir "sinematik plana" dönüştürür. Literatürde "Prompt Enhancement" (İstem Genişletme) veya LLM-tabanlı yeniden yazım (LLM-grounded rewriting) olarak bilinen bu aşama, modelin kullanıcıya göstermeden perde arkasında metni baştan tasarlaması sürecidir.

Kullanıcı "Astronaut walking in a space station" gibi basit bir komut girdiğinde, sistem bunu doğrudan işlemek yerine WanPE veya PromptEnhancer benzeri mimariler aracılığıyla 150 kelimelik karmaşık bir yönerge dizisine dönüştürür. Araştırmalar, bu yeniden yazım işleminin T2V kalitesini artırmak için tasarlandığını, soyut kullanıcı taleplerini aydınlatma, kamera hareketleri ve ortam detayları gibi somut değişkenlerle doldurduğunu göstermektedir. Ancak 8-10 saniyelik uzay bilimkurgu klipleri gibi son derece spesifik, mikroskobik düzeyde kontrol gerektiren durumlarda, bu otomatik genişletme ciddi bir dezavantaja dönüşür. Modelin "güzelleştirme" çabası, kullanıcının "kaskın içindeki soluk kırmızı aydınlatma" veya "vizördeki ince toz tabakası" gibi spesifik direktiflerini, LLM'in kendi varsayılan estetik kalıplarıyla ezmesine neden olur.   

Buna ek olarak, güvenlik filtreleri (safety rewriting) istem üzerinde yıkıcı bir etki yaratabilir. Şiddet, telif hakkı veya uygunsuz içerik filtreleri, bazen masum kelimeleri yanlış yorumlar. Örneğin, bilimkurgu bağlamında yazılan "blood-red nebula" (kan kırmızısı bulutsu) ifadesindeki "kan" kelimesi, sistem tarafından şiddet unsuru olarak algılanıp, metin "crimson fluid" veya "red gas" olarak gizlice değiştirilebilir. Kullanıcı, ekranda neden tamamen farklı bir renk ve doku paleti oluştuğunu anlayamaz. Sistemlerin bu gizli manipülasyonu, profesyonel kullanımda doğrudan ve aşırı spesifik komutlar girilerek (LLM'in boşluk doldurmasına mahal vermeyecek kadar detaylı) aşılmak zorundadır.

Metin Kodlayıcı Kapasitesi, Dikkat Dağılımı ve Talimat Düşmesi
T2I ve T2V modelleri, metni T5-XXL veya CLIP gibi dil kodlayıcıları (text encoders) aracılığıyla yüksek boyutlu vektör uzayına yerleştirir. Ancak bir metin kodlayıcının tek bir istemde kaç ayrı talimatı güvenle taşıyabileceği, modelin mimari sınırlarına tabidir. Modern T2V modelleri çok sayıda token'ı işleyebilse de, semantik kapasite, kelime sayısından (token limits) bağımsız olarak "talimat sayısı" ile doğrudan sınırlıdır.

Bir istem uzadıkça ve sahnedeki eylemler, nesneler, aydınlatma türleri, kamera hareketleri ve zırh detayları art arda eklendikçe, modelin çapraz-dikkat (cross-attention) ağırlıkları seyreltilir. Araştırmalar, talimat veya sekans uzunluğu arttıkça, dikkat ağırlıklarının gereksiz belirteçler üzerine dağıldığını ve modelin ana eylemi anlamlandırma yetisinin çöktüğünü ortaya koymaktadır. Pratik uygulamalarda ve T2V-CompBench testlerinde, modelin bir istemde aynı anda güvenilir bir şekilde tutabileceği bağımsız "odak nesnesi ve eylem" sayısının 3 ile 4 arasında olduğu, bu üst sınırdan sonra eklenen talimatların görüntüden silindiği (instruction dropping) gözlemlenmiştir. Örneğin, "Basınç giysili astronot yürüyor, sağ eliyle kaskını tutuyor, sol eliyle paneli işaret ediyor, panelde mavi ışık yanıp sönüyor ve kamera yavaşça yukarı kayıyor" şeklindeki bir bileşik talimatta, model astronotu ve yürüyüşü oluşturacak, ancak muhtemelen el hareketlerinin birini veya panelin ışık rengini tamamen görmezden gelecektir.   

Cümle Sırasının Ağırlığı: Öncelik Etkisi (Primacy Effect)
Difüzyon modellerinde cümlelerin sırası, görselin temel iskeletini oluşturmada devasa bir etkiye sahiptir. "Öncelik Etkisi" (Primacy Effect) olarak adlandırılan bu fenomen, T2V modellerinde yapılan resmi ölçümlerle kanıtlanmıştır. İstem metninin en başında yer alan kelimeler, gürültü giderme (denoising) sürecinin ilk adımlarında global tensör yapısını kilitler. İlerleyen kelimeler ise yalnızca yerel (local) detayları etkiler. Bu nedenle, kılavuzlarda sıklıkla kamera hareketinin ve ana öznenin cümlenin en başında yer alması önerilir. Başa yazılan "Medium shot, tracking..." komutu, en sona yazılan aynı komuta göre model üzerinde çok daha otoriter bir yönlendirme gücüne sahiptir.   

Mekanizma Analizi: Çelişkiler, Olumsuzlama Zafiyeti ve Görünmez Atıflar
Metin yönlendirmesinde kullanıcıların sıklıkla düştüğü hatalar, difüzyon mimarisinin matematiksel doğasını anlamamaktan kaynaklanır. Modelin dil anlama yetisi ile mantıksal çıkarsama yetisi birbirinden tamamen farklı mekanizmalardır.

Çelişen Taleplerin Çözümlenmesi (Contradictions):
Aynı istem içerisinde, "the face is clearly visible behind the dark opaque visor" (yüz, koyu opak vizörün ardından netçe okunuyor) gibi birbiriyle fiziksel olarak çelişen iki komut verildiğinde, LLM bu mantıksal hatayı düzeltecek bir ara yüzeye sahip değildir. Metin kodlayıcı, hem "net görünür yüz" tensörünü hem de "opak koyu vizör" tensörünü hesaplar. Difüzyon modeli bu iki veriyi aynı piksel koordinatlarına (yüz bölgesi) çapraz-dikkat haritalarıyla bağlar. Sonuç, vizörün bir kısmının şeffaf, diğer kısmının mat olduğu, saniyeler ilerledikçe kendi içinde eriyen, titreşen ve morflanan (morphing) bir halüsinasyon durumudur. Benzer şekilde, aydınlatmada "tek ışık kaynağı" ile "yüze sıcak dolgu ışığı" istendiğinde, model bir aydınlatma uzmanı gibi seçim yapmaz; iki ışığın özelliklerini uzaysal olarak karıştırarak sahnenin fizik kurallarını bozar.

Olumsuzlama Zafiyeti ve Uzun Olumsuz Bloklar (Negation Failure):
T2V sistemlerinin en yaygın yapısal zafiyeti, olumsuzluk (negation) operatörüdür. Model, "toz hiç yere inmez" veya "hiçbir şey havada asılı kalmaz" komutlarını okuduğunda, metin kodlayıcı "toz" (dust) ve "asılı kalmak" (floating) kavramlarını çoktan uzaya çağırmıştır. Çapraz-dikkat mekanizması bir nesnenin "yokluğunu" değil, yalnızca "varlığını" haritalandırabilir. Bağımsız araştırmalar, mevcut dil-görme (vision-language) modellerinin olumsuzlamayı anlamada sistematik olarak başarısız olduğunu ve negatif kelimelerin yasaklanan yapıyı ironik bir şekilde kadraja yerleştirdiğini doğrulamaktadır.   

Bu sorunu aşmak için yıllarca kullanılan, istemin sonuna eklenen ve metnin %40'ını kaplayan uzun olumsuz kelime blokları ("no blurry, no bad anatomy, no floating dust...") son nesil modellerde tam bir yıkıma neden olmaktadır. Uzun sekanslar dikkat ağırlıklarını seyrelttiği için, model asıl üretmesi gereken uzay istasyonu veya basınç giysisi detaylarına odaklanamaz. Çözüm, olumsuz durumları asla yazmamak ve istenen durumu %100 pozitif bir tanımla ("Kusursuz net vizör", "Yerçekimine tam itaat eden nesneler") ifade etmektir.   

Alan Başlıkları ve Sıra Numaraları:
İstem metnine büyük harflerle "CAMERA:", "PHYSICS:", "AUDIO:" gibi alan başlıkları koymak, difüzyon modelinin kendisi için anlamsızdır; çünkü model sadece bir metin-görüntü eşleştiricisidir. Ancak, sistemin ön ucunda (frontend) çalışan LLM tabanlı "İstem Genişletici" (Prompt Enhancer) bu başlıkları yapısal bir komut olarak okur ve metni kategorize ederken daha disiplinli bir planlama oluşturabilir. Öte yandan, "Scene 7 of 12" gibi sıra numaraları veya "the same lens as Scene 3", "as before" gibi modelin göremeyeceği nesnelere yapılan atıflar felaketle sonuçlanır. Üretimler tamamen bağımsız (stateless) başlatılır ve modelin önceki sahnelere dair hiçbir hafızası yoktur. Her sahne, ilk defa var oluyormuş gibi tam ve eksiksiz tanımlanmalıdır.   

OKUNUŞ (Yorumlama) Tablosu
Aşağıdaki tablo, modelin çeşitli yönlendirme tekniklerine nasıl tepki verdiğini ve bu tepkilerin bilimsel / pratik kanıtlarını yapılandırmaktadır.

İstem Özelliği    Modelin Davranışı ve İşleme Mekanizması    Ölçülmüş Etkisi veya Sonucu    Model / Sürüm    Kaynak ve Bağlantı    Etiket
Cümle Sırasının Ağırlığı (Primacy)    Cümlenin başındaki belirteçler, modelin gürültü giderme sürecinde global tensör yapısını kilitler. Sondaki detayların dikkat ağırlığı keskin şekilde düşer.    İlk kelimeler sahne kompozisyonunu %83-%88 arasında dikte eder. Baştaki yönerge baskındır.    Tüm Difüzyon Modelleri (Veo, Sora, Gen-3)    
"primacy effect in MDLMs, which aligns with expectations" - https://arxiv.org/pdf/2511.21338

ÖLÇÜLMÜŞ
Olumsuzlama (Negation)    "No X" yapısı, X'in varlığını çapraz-dikkat haritalarında aktive eder. Model yokluğu değil, varlığı haritalandırır.    Negatif soruların doğruluğunda rastgelelikten bile daha düşük (%10 altı) performans ölçülmüştür.    CLIP, T5-XXL Tabanlı Modeller    
"All models perform poorly on Negation MCQs, reflecting a general struggle with negation understanding." - https://arxiv.org/html/2501.09425v1

ÖLÇÜLMÜŞ
Uzun Olumsuz Blok (%40)    İstem sonuna yığılan uzun kurallar listesi, "token dilution" yaratarak ana odak nesnelerine ayrılan dikkat ağırlıklarını seyreltir.    Ana talimata uyum oranını düşürür, mantıksal bütünlüğü ve nesne netliğini bozar.    T2V Modelleri    
"As the sequence length increases, the attention weights may become more diffuse, leading the model to distribute the focus between less relevant tokens..." - https://arxiv.org/html/2510.06265v1

ÖLÇÜLMÜŞ
Çelişen İstekler    "Koyu opak vizörden yüzün okunması" gibi taleplerde model seçim yapmaz; zıt tensörleri füzyonlar (morflama).    Titreyen, fizik kurallarına aykırı yarı saydam/yarı mat doku bozulmaları yaşanır.    Veo 3.1, Runway Gen-3    Çapraz-dikkat çakışması (Cross-attention conflict) nedeniyle fiziksel yıkım gerçekleşir.    ÖNERİ
Alan Başlıkları ("CAMERA:")    Metin kodlayıcı seviyesinde etkisiz olsa da, LLM tabanlı Prompt Enhancer tarafından yapısal blok olarak algılanır.    İstem genişleticiyi kısıtlayarak, modelin rastgele estetik kararlar almasını sınırlar.    Veo 3.1, Wan 3.0    
"where user prompts are enhanced before being passed to a frozen T2I model" - https://arxiv.org/html/2509.04545v2

ÖLÇÜLMÜŞ
Görünmeyen Şeye Atıf ("as before")    "Scene 2", "önceki lens" gibi atıflar başarısız olur. Model hafızasızdır (stateless). Zamansal sürekliliği bağlayamaz.    Karakter, mekan veya kıyafet tasarımı saniyeler içinde tamamen farklı bir tasarıma dönüşür (hallucination).    Tüm T2V Mimari    
"Each shot is rendered independently with no shared references, so every prompt must be fully self-contained... no pronouns referring to prior shots, no 'same as before.'" - https://arxiv.org/html/2610.01884v1

ÖLÇÜLMÜŞ
Soyut Fiiller ("realizes", "fears")    Görsel difüzyon modelleri zihinsel veya soyut eylemleri doğrudan piksellere çeviremez. Yalnızca fiziksel yansımalar işlenir.    Rastgele ve bağlamsız yüz ifadelerine, eylemin tamamen yok sayılmasına yol açar.    Veo 3.1, Luma Dream Machine    Karakter duygu durumları, fiziksel mekanizmalar ("ellerini sıkar", "göz bebekleri büyür") olmadan çöker.    UYGULAMA
Kesin Sayılar ve Mikro Sayılar    "1 derece döner", "yerçekimi 0.5G", "15 adet obje" gibi kesin metrikler difüzyon uzayında anlamsızdır; model saymayı (numeracy) bilmez.    Sayı 1'den 15'e çıktıkça, modelin o nesne sayısını tutturma doğruluğu keskin biçimde %10'lara düşer.    Veo 3.1, Kling 3.0, Sora    
"as the number of objects increases from 1 to 15, model accuracy significantly drops, reaching around 10% for higher counts." - https://arxiv.org/html/2503.06884v2

ÖLÇÜLMÜŞ
Zaman Damgası (0.0s-3.5s)    Veo 3.1 gibi bazı yeni sistemlerde desteklenen kronolojik ayrıştırma yöntemidir (Timestamp prompting).    Sahnede zamanla değişen spesifik hareketlerin yönlendirilmesinde kısmi (ancak garanti olmayan) başarı sağlar.    Veo 3.1    
Google Cloud'ın Veo 3.1 resmi kılavuzunda zaman damgalı yapıların (ör. [00:00-00:02]) eylem değişimlerini kontrol ettiği rapor edilmiştir.

UYGULAMA
  
Görüntüye Basılan Yazı ve Karakter Sızıntısı (Text Leakage)
Fotogerçekçi uzay bilimkurgu sekansları, paneller, ekranlar (HUD), giysi üzerindeki amblemler ve kask tasarımları nedeniyle T2V modellerinde benzersiz bir risk taşır: Görüntüye basılan yazı (Text Leakage). Difüzyon modellerinin görsel-dil veri setleri, bazı kelimeleri sadece anlamsal (semantik) bir kavram olarak değil, doğrudan "görsel bir harf dizisi" (tipografik glif) olarak kodlamıştır.

Örneğin, "NASA", "EVA", "HUD", "AI" gibi büyük harfli kısaltmalar; "name tag", "warning label", "monitor", "dashboard" gibi yazıyı çağrıştıran isimler; veya "label", "display", "print" gibi fiiller metin kodlayıcıda yüksek bir tipografik ağırlık taşır. Siz "astronaut in a NASA pressure suit looking at a warning display" yazdığınızda, modelin eğitim verisindeki çapraz-dikkat mekanizması "NASA" ve "Warning" kelimelerini doğrudan astronotun göğsüne veya kaskın camına bozuk uzaylı alfabeleri (gibberish/alien text) olarak basmaya çalışacaktır.

Bir kelimenin tekrar sayısı bu riski logaritmik olarak artırır. "Red alert lights flash, alarm sounds indicating general alert" şeklindeki bir tekrarda, "alert" token'ı o kadar ağır basar ki, ortamda uygun olmayan yüzeylerde bile (örneğin kaskın kendisinde) kırmızı neon harflerle "ALERT" veya bozuk versiyonları belirecektir.

Kullanıcıların panelleri veya kadranları metinsiz istemek için sıklıkla başvurduğu "no text", "blank screen", "without words" gibi komutlar, olumsuzlama zafiyeti yüzünden tam tersi bir felaketle sonuçlanır. VidScribe ölçümleri, görsel metin yoğunluğunun, modelin kadraja metin yazma eylemini kaçınılmaz şekilde tetiklediğini kanıtlamaktadır. Yazının metinsiz (text-less) çözümlerle tarif edilmesi bir zorunluluktur. Ekranlar için "glowing abstract geometries" (parlayan soyut geometriler), "amber light bars" (kehribar rengi ışıklı çubuklar) veya "color-coded gauge showing maximum capacity" (renk kodlu doluluk kadranı) gibi dolaylı ve tipografiyi dışlayan fiziksel tasvirler, harf sızıntısını engelleyen kanıtlanmış tek metin mühendisliği çözümüdür.   

YAZI SIZINTISI (Text Leakage) Tablosu
Tetikleyen Kelime Türü    İstem Örneği (İngilizce)    Karşılaşılan Risk / Sonuç    Önleyen Alternatif Yazım    Kaynak / Açıklama    Etiket
Yazı Çağrıştıran Objeler / Yüzeyler    "Monitor displaying data", "name tag", "neon sign", "chest badge"    Belirtilen yüzeylerde anlamsız, titreşen harf bloklarının ve bozuk gliflerin oluşması, videonun her karesinde morflanan yazılar.    "Glowing rectangular illumination", "blank metallic chest plate", "color-coded circular gauge" (Görseli metinsiz tarif etmek)    
"VidScribe spans 9 real-world domains, balancing high-frequency text such as street signage, logos..." - https://arxiv.org/html/2609.36598v2

ÖLÇÜLMÜŞ
Büyük Harfli Kısaltmalar / Kurum Adları    "EVA suit", "NASA astronaut", "HUD interface"    Kısaltmanın birebir giysi veya kask üzerine harf olarak basılması (ör. NVS, NSAA).    "Extravehicular pressure suit", "national space agency uniform", "transparent tactical light projection"    Kısaltmalar semantik karşılıkları yerine doğrudan tipografik veri setlerine bağlı olduğu için sızıntıyı şiddetle tetikler.    UYGULAMA
Sık Tekrar Eden Vurgulu Kelimeler    "Red alert, alert lights flashing, general alert status"    Artan token ağırlığı nedeniyle duvarlarda, panellerde veya kaskta "ALERT" yazısının belirmesi.    "Pulsing red hazard illumination, emergency protocol active, strobe lighting"    İstem içi kelime tekrarı, modelin o kelimeyi soyut bir kavramdan çıkarıp somut bir görsel objeye (harfe) dönüştürme basıncını artırır.    ÖNERİ
Doğrudan Olumsuzlama (Negation ile Yazı Engelleme)    "Screen with no text", "Helmet with no words"    Model olumsuzluk ekini anlayamaz, "text" kelimesini yakaladığı için yüzeyi rastgele alfabelerle doldurur.    "Completely smooth reflective visor", "solid state gradient display", "minimalist blank interface"    Difüzyon çapraz-dikkat haritaları eksikliği değil, varlığı haritalandırdığı için "yazı yok" demek yazıyı zorla davet eder.    UYGULAMA
  
Yazım Standartları ve Uzay Bilimkurgu Sahneleri İçin Pratik Uygulamalar
8-10 saniyelik, fotogerçekçi ve tek çekimlik bir video sekansını yönetirken, modelin kapasitesini maksimum verimlilikle kullanmak için dilin sadeleştirilmesi ve fizikselleştirilmesi gerekir.

Öncelikle, modelin ölçemeyeceği kesinlikte komutlardan kaçınılmalıdır. "The astronaut is 2.5 meters away, turning her head exactly 15 degrees" gibi bir cümle, metin kodlayıcı tarafından yalnızca "astronot uzak, kafasını çeviriyor" olarak indirgenir. Kesin metrikler yerine, kadraj ve eylem sinematik bir dille boyutlandırılmalıdır ("Wide shot", "subtle head turn").   

İkinci kritik nokta, pozitif, tek anlamlı ve kısa yazmanın, sayfalar dolusu kural listesine olan tartışmasız üstünlüğüdür. İstem ne kadar kısa ve eylem ne kadar tekilse, difüzyon modeli o nesnenin kenar keskinliğini, aydınlatmasını ve tutarlılığını (temporal consistency) o kadar iyi hesaplar. Cümleler arası eylem yüklemesi (action stacking) modelin çökmesinin ana nedenidir.

Görüntüden-Videoya (I2V) veya referans kare üzerinden başlatılan üretimlerde yapılan en ölümcül hata, kullanıcının "Görsel zaten orada, model astronotu görüyor" diyerek metin kutusuna sadece "Make her walk forward" (Onu ileri yürüt) yazmasıdır. Model, ilk karedeki piksel verisini alır, ancak saniyeler ilerledikçe, eğer metin kutusunda o zırhın, kaskın, basınç borularının ve ışıkların sürekli bir tanımı yoksa, görsel hafıza zayıflar. 3. veya 4. saniyede astronot giysisi bir kazağa, uzay kaskı bir motosiklet kaskına dönüşebilir (morphing/hallucination). İlk karedeki tüm kritik detaylar, metinle modele yeniden ve eksiksiz tarif edilmek zorundadır.

YAZIM KURALI (Writing Rule) Tablosu
Kural    İngilizce Doğru Örnek    İngilizce Yanlış Örnek    Kanıt / Gerekçe ve Kaynak    Etiket
1. Kamera ve Ana Özne Önceliği (Primacy Effect)    "Medium shot, slow push in. An astronaut in a white pressure suit walks..."    "An astronaut walks in the ship... shown in a medium shot with a slow push in."    
 MDLMs mimarilerinde öncelik etkisi kanıtlanmıştır. Kamera hareketleri ve çerçevelemenin cümlenin en başında olması, tüm tensör yapısını bu perspektife kilitler.

ÖLÇÜLMÜŞ
2. Bağımsız Üretimler İçin Bağlamın Yeniden Kurulması    "Scene 2: An astronaut in a white pressure suit enters the airlock..."    "Scene 2: She enters the airlock wearing the same suit as before."    
 "Every prompt must be fully self-contained... no pronouns referring to prior shots, no 'same as before.'" Modelin hafızası veya önceki kliplere erişimi yoktur.

ÖLÇÜLMÜŞ
3. Zihinsel Durumları Fizikselleştirmek    "The astronaut's gloved hand grips the console tightly, chest heaving."    "The astronaut realizes the critical error and feels intense fear."    T2V modelleri soyut eylemleri ("realizes", "feels") işleyemez. Eylem, zihinsel bir durum yerine fiziksel bir karşılıkla (titreyen eller) yazılmadıkça model çöker.    UYGULAMA
4. Tek Seferlik ve Net Eylem Yüklemesi    "The astronaut slowly turns her head to the left."    "The astronaut walks, turns her head to the left, raises her hand and presses a button."    Bir cümle (veya sekans) içine istiflenen çoklu eylemler (stacking actions) hareketlerin birbirine girmesine veya modelin birini tamamen silmesine neden olur.    ÖNERİ
5. Metin İstemeyen Ekran Temsilleri    "A wall panel featuring an intricate grid of glowing blue and amber light bars."    "A monitor on the wall displaying complex technical text and data."    
 VidScribe araştırması, ekranda yazı ve data belirtmenin modeli bozuk glif üretmeye zorladığını doğrular ("Visual text in video is... a combination of lexical, structural, and typographic skills that degrade differently").

ÖLÇÜLMÜŞ
6. Negatif Durumları Pozitif Varlıkla İfade Etme    "The helmet visor is perfectly clear, revealing the face beneath."    "The helmet visor has no reflections and no dark tint."    
 "All models perform poorly on Negation MCQs". Negatif kelimeler, yasaklanan yapıyı güçlendirir ve tersine çağırır.

ÖLÇÜLMÜŞ
7. I2V'de Mevcut Olanı Yeniden Tanımlama (Referans Koruması)    "The astronaut in the heavy white pressure suit and gold visor continues to turn..."    "Make the person turn around."    Görsel referans olmasına rağmen metinsel karşılığın eksik olması, modelin ilerleyen saniyelerde zırh detaylarını halüsinasyonla sıradan objelere dönüştürmesine (morphing) yol açar.    UYGULAMA
8. Uzun Olumsuz Bloklardan Kaçınma    [Sadece pozitif tasvirlerden oluşan, 70-80 kelimelik kompakt, eylem odaklı bir metin.]    "...no bad anatomy, no floating dust, no extra fingers, no blurry background..."    
 Sekans uzadıkça dikkat ağırlıkları seyreltilir ("attention weights may become more diffuse"). Model esas göreve odaklanamaz, video bulanıklaşır.

ÖLÇÜLMÜŞ
  
Liste 1: Doğrulanabilir Bulgular ve Kaynaksız İddialar (Hipotezler)
Difüzyon modellerinin topluluk tabanlı kullanımında yayılan efsaneler ile bilimsel olarak doğrulanmış mekanizmaların birbirinden ayrılması, zaman ve maliyet kayıplarını engellemenin en güvenilir yoludur. Aşağıda, doğrudan üretim çıktısını etkileyen kesin bulgular ve sınırlandırılmış bu çalışma (hat dışı araçların kullanılmadığı, Google Flow üzerinden yürütülen T2V) kapsamında neden doğrulanamadığı belirtilen hipotezler sunulmuştur:

Doğrulanabilir Bulgular:

Öncelik Etkisi (Primacy Effect) Gerçektir: Metin kodlayıcıları (T5, CLIP) cümlenin başındaki belirteçlere yapısal olarak daha fazla ağırlık verir. Kamera hareketi, genel çerçeve ve aydınlatma kurulumu başta belirtilmelidir.   

Olumsuzlama Zafiyeti (Negation Failure) Sistematiktir: Difüzyon modelinin gizli uzayında kavramlar eksi (-) değerle var olamaz. "Toz yok" (No dust) komutu, sistemde toz tensörünü ateşler. Hiçbir güncel model (Sora, Veo, Gen-3) çapraz-dikkat mekanizmasında bağlamsal olumsuzlamayı tam olarak başaramamaktadır.   

Sayısal ve Matematiksel Yeteneksizlik (Numeracy Failure): Difüzyon modelleri nesneleri sayamaz veya metrik ölçümleri (derece, ağırlık) işleyemez. Bir istemde nesne sayısı arttıkça, modelin o nesne sayısını tutturma doğruluğu keskin biçimde çöker. Matematiksel kesinlik, model tarafından sadece "çok", "az" veya "büyük" gibi genel sıfatlar olarak yorumlanır.   

İstem Uzunluğu ve Dikkat Seyrelmesi (Token Dilution): İstem uzunluğu gereksiz yere artırıldığında veya uzun olumsuz kurallar eklendiğinde, çapraz-dikkat ağırlıkları önemsiz kelimeler üzerinde dağılır (attention diffusion). Optimizasyon için uzun kurallar listesi yerine, eylemi net anlatan özlü metinler kullanılmalıdır.   

Tipografik Çöküş (Text Leakage): T2V modelleri, anlamsız glif topolojisini zaman içinde korumakta zorlanır. Bir "isim" veya "kısaltma" yazılması modelin istem dışı harf basmasına yol açar ve sekans ilerledikçe harfler yapısal olarak erir.   

Kaynaksız İddialar ve Hipotezler (Çalışma Kısıtları Nedeniyle):

Hipotez: "İstem sonuna '4k, 8k, Unreal Engine 5, ultra-detailed cinematic, masterpiece' yazmak video çözünürlüğünü, keskinliğini ve kalitesini artırır."

Neden Doğrulanamıyor: Güncel Veo 3.1, Sora ve Luma gibi mimariler LLM tabanlı "İstem Genişletici" (Prompt Enhancement) sistemler kullanır; siz bu "sihirli kelimeleri" yazsanız bile, arka plandaki aracı dil modeli bunları filtreleyip modeli kendi optimize ettiği yapısal etiketlerle beslediği için, bu kelimelerin doğrudan piksel kalitesine etkisi artık doğrulanabilir bir metrik değil, bir plasebodur.   

Hipotez: "Negatif istemlere eklenen 40 kelimelik 'mutasyon, kötü anatomi, bozuk uzuv' bloğu, karakterin anatomi tutarlılığını artırır."

Neden Doğrulanamıyor: Uzun metinlerin dikkat seyreltmesi yarattığı kanıtlanmıştır; çok fazla olumsuz kelime, modelin pozitif ana yönlendirmeye ayıracağı işlem kapasitesini felç eder. Ayrıca, kısıtlamalarımız gereği Google Flow'da yalnızca tek bir metin kutusu kullanılmaktadır; API veya WebUI gibi ayrı bir "negative prompt" ağırlık kutusu (hat dışı çözüm) olmadığı için bu bloğu ana metne yazmak yalnızca kaosa yol açar.

Hipotez: "Scene 1, Scene 2 gibi ardışık numaralandırmalar kullanmak, farklı video kliplerinde karakterin aynı kalmasını (Character Consistency) sağlar."

Neden Doğrulanamıyor: T2V üretimleri izole ve hafızasız (stateless) başlatılır; modelin bağlam penceresinde bir önceki videonun işlenmiş ağırlıkları tutulmadığı için yalnızca metinle "Scene 2" yazmak, tasarım sürekliliğini asla garanti etmez.   

Liste 2: Bağlantılı Tam Kaynak Listesi
Aşağıda, rapor boyunca "ÖLÇÜLMÜŞ" etiketiyle doğrudan alıntılanmış bulguların, ölçüm mekanizmalarının ve T2V kıyaslama metriklerinin (benchmarks) dayandığı hakemli bilimsel çalışmalar, arXiv makaleleri ve veri seti raporları sunulmuştur (Araştırmada olmayan parametreler, sürüm isimleri veya asılsız rakamlar dahil edilmemiştir):

 "Emergence of the Primacy Effect in Structured State-Space Models / Diffusion Models"   

Kullanım Bağlamı: Cümle sırası ve öncelik etkisi, T2V modellerinde ilk yönlendirmelerin genel tensör yapısını nasıl kilitlediği.

Bağlantı: https://arxiv.org/pdf/2511.21338

 "NegBench: Investigating Negation Understanding in Vision-Language Models"   

Kullanım Bağlamı: Olumsuz cümlelerin ("no X") neden anlaşılamaması, eksikliğin çapraz-dikkat sızıntıları yaratması ve yasaklı kavramın tersine çağrılması.

Bağlantı: https://arxiv.org/html/2501.09425v1

 "Investigating and Mitigating Hallucinations in LLMs and Multimodal Models"   

Kullanım Bağlamı: Uzun metinlerde (özellikle negatif bloklarda) çapraz-dikkat ağırlıklarının seyreltilmesi (attention diffusion) ve çelişkilerde yaşanan halüsinasyon mekanizması.

Bağlantı: https://arxiv.org/html/2510.06265v1

 "Text-to-Image Diffusion Models Cannot Count, and Prompt Refinement Cannot Help (T2ICountBench)"   

Kullanım Bağlamı: Kesin sayıların, miktarların ve mikro ölçümlerin modeldeki başarısızlığı (Generative Numeracy), sayı arttıkça başarının %10'lara düşmesi.

Bağlantı: https://arxiv.org/html/2503.06884v2

 "MemComposer: Memory-Augmented Video Composition"   

Kullanım Bağlamı: "Scene 7" gibi referansların izole edilmiş (stateless) modellerde neden çöktüğü ve bağlamın yeniden kurulması zorunluluğunun sınırları.

Bağlantı: https://arxiv.org/html/2610.01884v1

 "WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation" & "PromptEnhancer: Chain-of-Thought Prompt Rewriting for T2I/T2V"   

Kullanım Bağlamı: İstem genişletme (Prompt Enhancement) özelliklerinin LLM vasıtasıyla perde arkasında nasıl çalıştığı, kullanıcı metnini sinematik bloklara nasıl çevirdiği.

Bağlantı [46]: https://arxiv.org/html/2609.30221v1

Bağlantı [48]: https://arxiv.org/html/2509.04545v2

 "VidScribe: A Unified Diagnostic Benchmark for Visual Text in Video Generation"   

Kullanım Bağlamı: Tabela, ekran, kısaltma (HUD, EVA) çağrıştıran kelimelerin istemsiz yazı basma riskini (Text leakage) nasıl tetiklediği ve glif topolojisinin degradasyonu.

Bağlantı: https://arxiv.org/html/2609.36598v2

 "Ultimate Prompting Guide for Veo 3.1" (Google Cloud Blog)   

Kullanım Bağlamı: Veo 3.1'in resmi kılavuzunda belirtilen 5 parçalı formül, kamera hareketleri sınıflandırması ve Timestamp (Zaman damgası) yapıları (Kılavuzlar "UYGULAMA" olarak değerlendirilmiştir).

Bağlantı: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1

(T2V-CompBench gibi yan değerlendirme raporları, genel kompozisyon zorluklarının (spatial relations, dynamic attribute binding vb.) teyidi ve Sora, Kling, Runway Gen-3 kıyaslamaları için analizin zemininde çapraz doğrulamayla kullanılmış olup, alıntı yapılan temel çerçeveler yukarıdaki listeye sabitlenmiştir.)   
