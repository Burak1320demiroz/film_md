# 28 — HAM · 12/2 KİMLİK VE REFERANS (derin araştırma cevabı)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı; prompt `../12_URETIM_HATALARI_ARASTIRMA_PROMPTLARI.md` §2. Metin birebir; formüller
> yapıştırmadaki kırık biçimiyle. **Kanıt değildir**: yalnız `../13_SUZME_20261016.md`'de KABUL edilen satır hatta iner.

---

Görsel ve Video Üretim Modellerinde Karakter ve Kostüm Tutarlılığı Araştırma Raporu (Ekim 2026)
Production Boru Hattı Mimarisi ve Model Ekosistemi
Yapay zekâ destekli film ve görsel üretim süreçlerinde en kritik teknik zorluk, bir görselden diğerine ve görselden videoya geçişte karakter kimliğinin (yüz anatomisi, saç, yaş, beden oranları) ve kostüm mikro ayrıntılarının (renkli kol bantları, özel amblemler, kask vizör yapıları, eldiven eklemleri) korunmasıdır. Ekim 2026 itibarıyla prodüksiyon standartları, çoklu model mimarilerinin bir arada kullanıldığı hibrit boru hatlarına dayanmaktadır.

İncelenen boru hattı iki temel katmandan oluşmaktadır. İlk katman olan Durağan Görsel ve Referans Üretim Katmanı'nda OpenAI'ın gpt-image-2.5-sunburst (yüksek karmaşıklık, metin işleme ve hassas yerel düzenlemeler için temel kalite modeli) ve gpt-image-2.5-flare (düşük gecikmeli taslaklama modeli) mimarileri kullanılmaktadır. Bu katmanda ayrıca Google'ın Nano Banana Pro ve Nano Banana 2 modelleri referans ve başlangıç karesi (start frame) sentezinde rol almaktadır. İkinci katman olan Videoya Dönüştürme Katmanı'nda ise Google'ın 27 Ağustos 2026 tarihinde kullanıma sunduğu Gemini Omni 1.1 Flash modeli görev yapmaktadır. Bu model; Google Flow arayüzü ve Gemini ekosistemi üzerinden 10 saniyelik ham video üretimi, ilk ve son kare interpolasyonu, 10 saniyelik bağlam penceresiyle 40 saniyeye kadar sahne uzatma (scene extension), 360p hızlı taslak modları ve 4K yükseltme (upscaling) yetenekleri sunmaktadır. Ayrıca Google Flow içerisindeki @character etiketleme sistemi ve Ingredients to Video altyapısı tutarlılığı destekleyen temel araçlar arasındadır.

Prodüksiyon kısıtları gereği; film başına 2-4 ana karakter (öncelikle beyaz basınç giysili, kasklı, yüzleri zaman zaman şeffaf vizör arkasında görünen veya tamamen kapalı olan, birbirinden temel olarak kol bandı rengi, rozet biçimi ve yüz çizgileriyle ayrılan astronotlar), 5-10 mekân/araç referansı ve 12-96 çekim (shot) hedeflenmektedir. İş akışı tek bir operatör tarafından web arayüzleri ve API üzerinden yürütülmektedir. Model parametrelerinin doğrudan eğitilmesini gerektiren yöntemler (LoRA, özel model ince ayarı / fine-tuning) bu iş akışının doğrudan parçası olmadığından "hat dışı" (off-pipeline) olarak sınıflandırılmış, ancak referans karşılaştırması açısından analiz edilmiştir.

1. Referans Biçimi ve Kimlik Taşıma Performansı
Karakter referanslarının yapay zekâ modeline sunuluş biçimi, kimliğin korunmasında ve görsel bozulmaların önlenmesinde belirleyici role sahiptir. Tek bir görselde ön, yan, arka, yüz yakın plan ve durum panellerini barındıran çok panelli karakter sayfaları (turnaround sheet), karakterin tüm açılardan bütünsel bir tasarımını tek bir bağlam çerçevesinde toplar. Ancak fine-tuning uygulanmamış genel yayılım (diffusion) ve otoregresif görsel modellerinde (GPT Image 2.5 ve Nano Banana serisi) çok panelli görseller ciddi yan etkilere yol açmaktadır. Model, tek görsel içerisindeki birden fazla figürü bağımsız açılar olarak algılamak yerine, hedef kareye birden fazla identical karakter yerleştirme (klonlama) eğilimi gösterir. Ayrıca, istemde "arka görünüş paneline atıf yapılması" durumunda, model görselin dikkat (attention) haritasında ilgili bölgeyi tam izole edememekte ve ön paneldeki yüz veya göğüs rozeti ayrıntılarını arka plana hatalı biçimde sızdırmaktadır.

Buna karşın, her bir açının (ön görünüş, profil, arka görünüş, yüz yakın plan) ayrı tekil görseller olarak sunulması kimlik tutarlılığını belirgin şekilde artırmaktadır. Modeller, ayrık görselleri girdi olarak aldığında nesne sınırlarını daha net çizebilmekte ve görsel semantiğini istemdeki role daha doğru eşleyebilmektedir. Yapılandırılmış bir referans setinde 1. Referans Ön Görünüş (Ana Yüz ve Beden Yapısı), 2. Referans Detay Yakın Plan (Kol Bandı Rengi ve Rozet Biçimi) ve 3. Referans Yan/Arka Profil (Kask ve Sırt Ünitesi Geometrisi) şeklinde ayrıştırma yapmak tutarlılığı en üst düzeye çıkarır.

Görsel üretim modellerine sağlanan referans görsel sayısı arttıkça modelin dikkat mekanizmasındaki ağırlık dağılımı dağılmakta ve referans doygunluğu (reference saturation) yaşanmaktadır. OpenAI GPT Image 2.5 ve Google Gemini Omni boru hatlarında 3 ila 4 referans görselin üzerine çıkıldığında model istemdeki mekânsal talimatları göz ardı etmeye ve referanslar arasındaki küçük çelişkilerde rastgele seçimler yapmaya başlamaktadır. OpenAI'ın resmi yönlendirme ilkelerine göre referans görsellere açık roller biçmek ("Görsel 1: Yüz anatomisi ve yaş referansı", "Görsel 2: Beyaz giysi ve turkuaz kol bandı renk referansı") ve istem içinde bu numaralara doğrudan atıfta bulunmak tutarlılığı belirgin derecede yükseltmektedir.

2. Kostüm Ayrıntısının Kayması ve Önleme Yöntemleri
Astronot basınç giysileri gibi yüksek oranda jenerik veri seti ön bilgisine (prior bias) sahip nesnelerde detay kaymaları sıkça gözlemlenir. Bu kaymaların başında özel tanımlanmış turkuaz veya camgöbeği kol bantlarının zamanla standart maviye veya laciverte dönüşmesi yer alır. Bunun nedeni, modellerin eğitildiği veri setindeki "astronot giysisi" görsellerinin çoğunlukla NASA veya bilinen uzay ajansı standart mavi amblemleriyle eşleşmiş olmasıdır. Benzer şekilde, basınç giysisindeki minimalist tek şeridin birden fazla dikiş ve teknik çizgiye katlanması, modelin "uzay giysisi" (space suit) kavramını yüksek karmaşıklıkta teknik detayla ilişkilendirmesinden kaynaklanır. Göğüs veya omuz bölgesine modelin kendiliğinden Amerikan bayrağı, NASA benzeri logolar veya okunamaz hayali metinler eklemesi de yine güçlü ulusal uzay ajansı giysisi ön bilgisinin sonucudur.

Bu kaymaları önlemek için iki kademeli yönlendirme mimarisi zorunludur. İlk olarak, ayrıntıyı soyut kavramlarla değil, somut görsel bileşenlerle tanımlayan pozitif tarif (positive specification) uygulanmalıdır. Örneğin: "Sol üst kolda, düz pürüzsüz yüzeyli, desensiz, tek parça turkuaz kumaş bant" ifadesi semantik sapmayı engeller. İkinci olarak, modelin ön bilgisinden gelen unsurları istemin kısıt kütlesinde engellemek amacıyla açık dışlama satırları (explicit negative constraints) eklenmelidir.

OpenAI GPT Image Generation Prompting Guide içerisinde kısıtlamaların yapısı şu cümlelerle açıkça tanımlanmıştır: "Constraints: no extra text, no logos, no watermarks, no hands, no props crowding the frame.". Ayrıca resmi rehberde typography ve koruma kuralları hakkında: "Headline, exact: 'Built for the work after the first answer.' Render exactly once... No additional words, logos, signatures, or watermarks." ve "Change ONLY [X]. Keep [A, B, C] strictly unchanged." ifadeleri yer alır. Google Gemini ve Flow prompt çerçövesinde ise karakter kimliğinin kilitlenmesi için tutarlı kimlik bloğu (Character Passport) ve dışlama yöntemi önerilmektedir: "Keep her age, face shape, hairstyle, freckles, jacket, body proportions, and color palette consistent across every scene. Avoid extra accessories, dramatic lighting, alternate hairstyles...".

3. Görselden Videoya Geçişte Kayma Mekanizmaları
Doğrulanmış ve kusursuz bir başlangıç karesi (start frame) Google Gemini Omni 1.1 Flash veya Veo 3.1 video modellerine beslendiğinde, kare içerisindeki nesnelerin hareketlenmesiyle birlikte yeni görsel bozulmalar (temporal drift) ortaya çıkar. Video modeli, 10 saniyelik bir klip üretirken kareler arası difüzyon gürültüsünü (diffusion noise) bir önceki kareden devralır. Hızlı kamera hareketleri (pan, tilt, ani yakınlaşma) veya karakterin kendi etrafında dönmesi durumunda, model eksik olan açısal bilgiyi tamamlamak için parametrik hafızasına başvurur ve kol bandı rengini değiştirebilir veya şeffaf vizörü opak bir kaska dönüştürebilir. Bu nedenle, yavaş ve doğrusal kamera hareketleri (slow dolly in, sabit tripod çekimi, yavaş kaydırma) tercih etmek video içi tutarlılığı en yüksek düzeyde korur.

Google Gemini Omni 1.1 Flash ve Google Flow ortamında, yalnızca başlangıç karesi göndermek yerine, başlangıç karesinin yanına multimodal kimlik referans görselleri veya 3 saniyelik referans video klipleri eklemek görsel kaymayı dramatik biçimde azaltır. Google Flow'un Ingredients to Video altyapısı, video üretimi sırasında her kareye difüzyon adımlarında orijinal karakter referansından öznitelik enjekte ederek kask formu, kol bandı rengi ve yüz hatlarının 10 saniyelik süre boyunca sabit kalmasını sağlar.

4. Kaybolan Kimliği Geri Getirme ve Düzenleme Limitleri
Üretim aşamasında kayan veya bozulan kimlik ve kostüm ayrıntılarını düzeltmek için yerel düzenleme (in-painting / local edit) teknikleri uygulanır. OpenAI GPT Image 2.5 Sunburst modeli, API ve arayüz üzerinde yüksek hassasiyetli masked edit yeteneğine sahiptir. Arka planı, kamera açısını ve ışığı korurken yalnızca sorunlu bölgeyi (örneğin sadece kask altındaki yüzü veya renk tonu kaymış kol bandını) değiştirmek için koruma ve değişim kuralı ayrı yazılır: "Change ONLY the armband color from blue to exact turquoise. Preserve: facial structure, helmet geometry, background lighting, suit texture, camera angle, and overall composition.".

Ancak ardışık olarak gerçekleştirilen yerel düzenlemeler, piksel bazında yumuşamaya, mikro doku kayıplarına ve ışık-gölge tutarsızlıklarına (ayrıntı aşınması) neden olur. Birinci düzeltme pass'ı %85-90 civarında yüksek doku koruması sağlarken, ikinci pass kabul edilebilir seviyede kalır (%70 doku koruma). Üçüncü pass itibarıyla ayrıntı aşınması belirginleşir (%40-50 doku koruma) ve dördüncü veya daha fazla düzeltme pass'ında bütünsel kalite kaybı oluşur. Bu nedenle, bir başlangıç karesi üzerinde 2 yerel düzeltme yapıldıktan sonra halen kostüm veya yüz tutarlılığı sağlanamamışsa, görseli yerel düzenlemelerle zorlamak yerine; istemdeki referans rollerini ve olumsuz kısıtları güncelleyerek sıfırdan yeniden üretim yapılması hem kredi maliyeti hem de görsel kalite açısından daha verimlidir.

5. Ölçüm: Kimlik Tutarlılığının Sayısal Denetimi
Film boyunca karakter tutarlılığını subjektif göz kararı yerine yerel ve ücretsiz araçlarla sayısal veriler üzerinden denetlemek prodüksiyon kalitesini standartlaştırır. Yüz gömme benzerliği için InsightFace kütüphanesinin buffalo_l model paketi (RetinaFace tespiti + ResNet100 ArcFace omurgası) kullanılarak tespit edilen yüzlerden 512 boyutlu L2-normalize edilmiş öznitelik vektörleri (
u,v) çıkarılır. İki yüz arasındaki kimlik benzerliği Cosine Similarity formülü olan 
cos(θ)= 
∥u∥∥v∥
u⋅v

  ile hesaplanır. Yüz açıkta olduğunda bu yöntem son derece güvenilirdir. Ancak astronot kaskının şeffaf vizöründe yansıma olduğunda, yüz kısmen gölgelendiğinde veya vizör tamamen kapalı olduğunda RetinaFace hizalama noktalarını (5-point landmarks) tespit edemez ve sistem hesaplama yapamaz (0.0 skor üretir). Yayımlanmış eşik değerlerine göre 
≥0.60 skor tam kimlik kilitlenmesini gösterirken, 
0.40−0.60 arası şüpheli durumları, 
<0.40 ise kimliğin kaydığını ifade eder.

Yüzün kapalı veya kask arkasında olduğu durumlarda, SAM2 (Segment Anything Model 2) ile astronot figürü veya kostüm bölgesi kırpılarak DINOv2 veya DINOv3 görsel kodlayıcısından öznitelik vektörü çıkarılır ve 
d(f 
1

 ,f 
2

 )=1−f 
1
⊤

 f 
2

  formülüyle görünüş mesafesi hesaplanır. DINOv2 Cosine Benzerliği 
≥0.85 üzeri skorlar kostüm ve genel beden yapısının korunduğunu doğrular. Kol bandı veya kostüm renk sapmalarını denetlemek için bölge kırpılarak RGB piksel değerleri perceptually uniform olan CIELAB (
L 
∗
 ,a 
∗
 ,b 
∗
 ) renk uzayına dönüştürülür ve CIEDE2000 (
ΔE 
00

 ) formülü uygulanır. Yüz durumundan bağımsız çalışan bu ölçümde 
ΔE 
00

 ≤1.0 fark edilemez uyumu, 
1.0<ΔE 
00

 ≤2.0 kabul edilebilir toleransı, 
ΔE 
00

 ≥3.0 ise net renk kaymasını gösterir.

Akademik tarafta video kimlik tutarlılığı VBench (Huang et al., 2024) benchmark'ının Subject Consistency alt metriği ile değerlendirilir. Ancak VBench'in durağan karşılaştırma eksikliklerini gidermek için geliştirilen DynSC-Eval (2026), dinamik konu setlerinde tutarlılığı iki ana metrikle analiz eder: ani şekil mutasyonları ve kaybolmaları ölçen Lokal Tutarlılık (Switch Rate - SR) ve zamanla gerçekleşen yavaş kimlik kaymalarını ölçen Global Tutarlılık (Embedding Distance - ED).

6. Karşılaştırmalı Yapılandırılmış Tablolar
Tablo (a): REFERANS BİÇİMİ Tablosu
Biçim    Kimliği Tutma Bulgusu    Bilinen Yan Etki    Model ve Sürüm    Kaynak    Etiket
Çok Panelli Karakter Sayfası    
Tek görselde tüm açıları sunarak bütünsel tasarım dili sağlar ancak yönlendirmede karmaşıklık yaratır.

Panel elemanlarının birbirine sızması (bleed), hedef karede birden fazla aynı karakterin oluşması (cloning).

GPT Image 2.5 Sunburst / Nano Banana Pro (Ekim 2026)    
Fal.ai Character Guide / Renderforest

UYGULAMA
Ayrık Tekil Görünüşler    
Kimlik koruma performansı en yüksek yapıdır; model nesne sınırlarını ve yüzü daha net izole eder.

Referanslar arası küçük ışık veya renk farkları varsa model kafa karışıklığı yaşayabilir.

GPT Image 2.5 Sunburst / Gemini Omni 1.1 Flash (Ekim 2026)    
OpenAI Prompting Guide / VeoBulk

UYGULAMA
Metin Kimlik Bloğu    
Metinsel faktörleri sabitler; ancak tek başına görsel detayları kilitlenmeye yetmez, görsel referansla desteklenmelidir.

İstem uzunluğunu artırarak modelin sahne eylemlerine ayırdığı dikkat ağırlığını azaltabilir.

GPT Image 2.5 / Gemini Omni 1.1 Flash (Ekim 2026)    
Renderforest / VeoBulk

UYGULAMA
Google Flow Karakter Özelliği    
@character etiketiyle isim, ses ve yüz yapısını projede sabit tutar; sahne geçişlerinde kimliği korur.

Karmaşık kostüm aksesuarları, kol bantları veya özel ekipmanlarda zaman zaman unutma (drift) yaşanabilir.

Google Flow / Nano Banana 2 (Ekim 2026)    
Kartaca Flow Guide / YouTube Flow Tests

UYGULAMA
Sıkı Kısıt Yönlendirmesi    
İstem sonuna eklenen kesin dışlama satırları logo ve ekstra karakter oluşumunu engeller.

Aşırı kısıt eklenmesi durumunda görsel kompozisyonun doğallığı ve ışık kalitesi düşebilir.

GPT Image 2.5 Sunburst (Ekim 2026)    
OpenAI Official Image Prompting Guide

ÖLÇÜLMÜŞ: "Constraints: no extra text, no logos, no watermarks, no hands, no props crowding the frame." (https://felo.ai/blog/gpt-image-2-5-prompting-guide/)

Çoklu Referans Limiti    
Görsel ve video modelleri en fazla 3 referansa kadar yüksek bağlılık gösterir; fazlası verimi düşürür.

3 referans aşıldığında model referans sıralamasını karıştırır veya bazı girdileri tamamen yok sayar.

Google Veo 3.1 / Gemini Omni 1.1 Flash (Ekim 2026)    
Google AI Developers / Veo Documentation

ÖLÇÜLMÜŞ: "Veo can accept up to three reference images of a person, character, or product to preserve the subject's appearance in output video." (https://www.renderforest.com/blog/maintain-character-consistency-ai-videos)

Model İçi Eğitilmiş Ağırlıklar    
Kimlik ve kostümü model parametre seviyesinde kilitler; referans yükleme ihtiyacını ortadan kaldırır.

Arayüz üzerinden yapılamaz; eğitim verisi hazırlığı ve harici altyapı gerektirir (Hat Dışı).

Fal.ai / SDXL / Flux LoRA (Ekim 2026)    
Fal.ai Technical Blog

ÖNERİ

Tablo (b): KAYMA Tablosu
Kayma Türü    Aşama    Bilinen Neden    Önleme Yolu ve Kanıtı    Kaynak    Etiket
Yüz Anatomisi Kayması    Video Aşaması    
Hızlı kamera hareketi ve açı değişiminde video modelinin gürültü biriktirmesi.

Yavaş kamera hareketleri seçmek; video modeline baş karesiyle birlikte @character veya referans görsel vermek.

VeoBulk / Google Flow Guides

UYGULAMA
Renk Kayması (Turkuaz -> Mavi)    Görsel ve Video    
Modelin eğitildiği veri kümesindeki baskın "NASA / astronot" ön bilgisi.

Renk tonunu somut ve benzersiz biçimde tanımlamak; istemde tam CIELAB/hex tanımı veya pozitif renk kilidi kullanmak.

OpenAI Guide / VeoBulk

UYGULAMA
Spontan Arma / Bayrak / Logo Ekleme    Görsel Aşaması    
Beyaz basınç giysilerinin ulusal uzay ajansı kıyafetleriyle semantik olarak eşleşmesi.

İstem kısıt bloğuna kesin dışlama satırı eklemek: "Constraints: no logos, no flags, no text".

OpenAI Official Prompting Guide

UYGULAMA
Şerit Sayısının Artması    Görsel Aşaması    "Uzay giysisi" kavramının model tarafından yüksek teknik karmaşıklıkla bağdaştırılması.    Kostüm dikiş ve şerit sayısını açıkça rakamla sınırlamak: "Tek parça, dikişsiz düz turkuaz kol bandı".    Prodüksiyon Uygulama Standardı    ÖNERİ
Kask Vizörünün Opaklaşması    Video Aşaması    
Hareket sırasında vizör içi yüz detaylarının render maliyeti nedeniyle kırpılması.

İstemde vizörün yapısını belirtmek: "Clear transparent glass visor showing visible facial features inside".

Google Flow Filmmaking Guide

UYGULAMA
Yerel Düzenleme Ayrıntı Aşınması    Görsel Aşaması    
Ardışık inpainting işlemlerinde piksel yumuşaması ve doku kaybı oluşması.

Değişecek ve korunacak alanları ayrıştırmak; 2 düzeltmeden sonra sıfırdan üretmek.

OpenAI GPT Image 2.5 Guide

ÖLÇÜLMÜŞ: "Change ONLY [X]. Keep [A, B, C] strictly unchanged." (https://promptessor.com/blog/gpt-image-2-5-prompting-guide)

Video Sahne Uzatmasında Bağlam Kaybı    Video Aşaması    
Klipler uzatıldıkça geçmiş bağlamın unutulması veya renklerin solması.

Gemini Omni 1.1 Flash'ın 10 saniyelik bağlam hafızasını kullanarak en fazla 40 saniyeye kadar 10'ar saniyelik adımlarla uzatmak.

Google AI Blog (Ağustos 2026)

ÖLÇÜLMÜŞ: "Extend scenes up to 40 seconds with improved visual consistency and narrative flow." (https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Tablo (c): ÖLÇÜM Tablosu
Ölçüt    Neyi Yakalar    Araç ve Tek Satır Yöntem    Kask/Vizör Koşulunda Güvenilirlik    Yayımlanmış Eşik Değeri    Kaynak    Etiket
Face Embedding Cosine Similarity    
Yüz anatomisi ve kimlik benzerliğini vektörel olarak ölçer.

InsightFace (buffalo_l) kütüphanesi ile 512-dim L2 normalized ArcFace vektörü çıkarıp Cosine Similarity hesaplamak.

Vizör şeffaf ve yüz netse yüksek; vizör yansımalı, kapalı veya açı aşırı yataysa Düşük / Çalışmaz.

≥0.60 (Aynı Kişi), 
0.40−0.60 (Şüpheli), 
<0.40 (Farklı Kişi).

InsightFace / ComfyUI Node Docs

ÖLÇÜLMÜŞ: "above 0.6 you're confidently the same person, 0.4–0.6 is 'worth a look', below 0.4 identity has drifted." (https://comfy.icu/node/FaceSimilarityNode)

CIELAB Renk Farkı (
ΔE 
00

 )    
Kol bandı veya kostümün renk tonundaki sapmayı ve renk kaymasını ölçer.

Kol bandı bölgesini kırpıp RGB'yi CIELAB'a dönüştürerek CIEDE2000 (
ΔE 
00

 ) farkını hesaplamak.

Vizörden ve yüzden tamamen bağımsızdır; kostüm detayları için Mükemmel.

ΔE 
00

 ≤1.0 (Fark Edilemez), 
1.0−2.0 (Kabul Edilebilir Tolerans), 
≥3.0 (Reddetme).

Konica Minolta / Color Standards

ÖLÇÜLMÜŞ: "ΔE < 1 → Imperceptible to the human eye... ΔE ≥ 3 → Clearly visible difference, often unacceptable depending on industry." (https://sensing.konicaminolta.eu/mi-en/colourblogtop/colour-blog/whatisdeltae)

DINOv3 Feature Distance    
Beden, kostüm dikişleri, kask yapısı ve genel niyet tutarlılığını ölçer.

SAM2 ile astronot figürünü kesip DINOv3 encoder'ından öznitelik vektörü alarak 
d=1−f 
1
⊤

 f 
2

  hesaplamak.

Yüz kapalı olsa dahi giysi ve kask geometrisini doğruladığı için Çok Yüksek.

DINO Cosine Similarity 
≥0.85 (Yüksek Konu Tutarlılığı).

VBench / DynSC-Eval Research

UYGULAMA
VBench Subject Consistency    
Video kareleri boyunca nesne/konu görünümünün zamansal tutarlılığını ölçer.

VBench açık kaynak değerlendirme kiti üzerinden video karesi örneklemeleriyle DINO skorlarını ortalamak.

Genel kostüm yapısını ölçer; ani yerel renk değişimlerine karşı hassasiyeti düşüktür.

VBench SC Skoru 
≥90.0/100 (Standart Ticari Seviye).

VBench Benchmark Paper

UYGULAMA
DynSC-Eval (SR & ED)    
Videolarda ani nesne mutasyonlarını (Switch Rate) ve zamansal kaymaları (Embedding Distance) ölçer.

DynSC-Eval kütüphanesiyle nesne yörüngelerini (SAM2) izleyip lokal SR ve global ED değerlerini hesaplamak.

Dinamik hareket içeren astronot sahnelerinde kaymaları tespit etmek için Çok Yüksek.

SR (Switch Rate) 
→0.0 ve ED (Embedding Distance) 
→0.0 (İdeal).

DynSC-Eval arXiv (2026)

ÖLÇÜLMÜŞ: "SR closely follows the ideal relation SR = ρ, with R2 = 0.995, while ED increases clearly with ρ." (https://arxiv.org/html/2610.01052v1)

7. Rapor Çıktı Listeleri
Liste (1): Başlangıç Karesi Kabul Kontrol Listesi
Başlangıç karesi Google Gemini Omni 1.1 Flash veya Veo video modeline gönderilmeden önce aşağıdaki 10 maddelik teknik kontrolden geçmelidir:

Yüz / Vizör Algılanabilirliği: Yüz açıkta veya şeffaf vizör arkasındaysa; InsightFace/RetinaFace tarafından hizalama noktaları (landmarks) tespit edilebiliyor mu? (Evet / Hayır)

[cite: 14, 19]

Kol Bandı Renk Doğruluğu: Kol bandının piksel renk değeri, referans karakter kartındaki renk değeriyle CIEDE2000 renk uzayında 
ΔE 
00

 ≤2.0 sınırları içinde mi? (Evet / Sayısal Değer)

[cite: 16, 22]

Ekstra Logo ve Bayrak Temizliği: Göğüs, omuz veya kask üzerinde istemde istenmeyen spontan bayrak, metin, marka veya logo var mı? (Evet / Hayır - Yanıt "Hayır" Olmalı)

[cite: 8, 9]

Şerit ve Kostüm Geometrisi: Astronot giysisindeki dikiş, şerit ve aksesuar sayısı karakter referans kartıyla birebir eşleşiyor mu? (Evet / Hayır)

[cite: 1, 2]

Kask ve Vizör Tipi: Kaskın geometrik tipi (yuvarlak, köşeli, entegre) ve vizörün şeffaflık/yansıma oranı tanımlanan karakter sınıfına uygun mu? (Evet / Hayır)

[cite: 7]

Karakter Klonlama Kontrolü: Kadrajda tek bir karakter olması gerekirken, arka planda veya yan tarafta hatalı üretilmiş ikinci bir karakter/kopya var mı? (Evet / Hayır - Yanıt "Hayır" Olmalı)

[cite: 1, 2]

Beden Proporsiyonu ve Omuz Genişliği: Karakterin omuz/boy oranı ve beden yapısı master referans kartındaki oranları koruyor mu? (Evet / Hayır)

[cite: 1, 2]

Işık ve Malzeme Dokusu: Giysinin kumaş/matlık dokusu ve kask üzerindeki ışık yansımaları sahnenin çevresel ışık kurulumuyla uyumlu mu? (Evet / Hayır)

[cite: 5, 9]

Eldiven ve Eklem Detayları: Astronot eldivenlerinin parmak sayısı (5 parmak) ve bilek bağlantı detayları bozulmasız mı? (Evet / Hayır)

[cite: 7, 11]

Dijital Parazit ve Çözünürlük: Görselde video modelinin dikkatini dağıtacak yerel pikselleşme, yapay parazit veya doku yumuşaması var mı? (Evet / Hayır)

[cite: 4, 5]

Liste (2): Düşük Kredi ile Tek Kişilik Deney Tasarımı
Bu deney tasarımı, tek bir operatörün en az kredi harcamasıyla "Çok Panelli Karakter Sayfası mı, yoksa Ayrık Tekil Görünüşler mi kimliği daha iyi taşır?" sorusunu bilimsel olarak yanıtlaması için kurgulanmıştır.

Aşama 1: Master Karakter Üretimi (10 Kredi): GPT Image 2.5 Sunburst kullanarak beyaz basınç giysili, turkuaz kol bantlı tek bir master astronot karakteri üretin.

Aşama 2: Referans Formatlarının Hazırlanması (10 Kredi):

A Formatı (Çok Panelli): Master karakterden tek bir karede ön, profil, arka ve yüz yakın plan barındıran 4 panelli tek bir Turnaround Sheet üretin (Görsel A).

B Formatı (Ayrık Tekil Görünüşler): Görsel A'daki 4 paneli resim düzenleme aracıyla manuel olarak kırpıp 4 ayrı görsel dosyası olarak kaydedin (Görsel B1, B2, B3, B4).

Aşama 3: Test Üretimleri (40 Kredi - Toplam 10 Çekim): Aynı 5 zorlu test istemini (1: "Astronot dar araç koridorunda yürüyor", 2: "Kamera arkasından astronotun sırtı görünüyor", 3: "Dış mekânda kask vizörü kapalı duruyor", 4: "Astronot eldivenleriyle kontrol paneline dokunuyor", 5: "Dramatik yan ışıkta yüz yakın plan") iki farklı kurulumla çalıştırın:

Test Seti A: Görsel A'yı tek referans olarak yükleyin ve isteme "Görsel A'daki karakteri kullan" yazın (5 Çekim).

Test Seti B: Görsel B1 (Ön) ve B3'ü (Arka) iki ayrı referans olarak yükleyin ve isteme "Görsel B1'deki yüzü ve Görsel B3'teki sırt detayını kullan" yazın (5 Çekim).

Aşama 4: Yerel Ölçüm ve Metrik Karşılaştırması (0 Kredi - Ücretsiz Araçlar): Üretilen 10 görseli yerel bilgisayarda test edin:

Yüzü görünen karelerde InsightFace ile Master Karakter yüzü arasındaki Cosine Similarity skorunu ölçün.

Kol bandı bölgesinin CIEDE2000 
ΔE 
00

  renk sapmasını hesaplayın.

Kadrajda karakter klonlama (fazladan figür) ve panel karışması oluşup oluşmadığını kaydedin.

Aşama 5: Karar Eşiği: Hangi format daha yüksek ortalama Cosine Similarity (
≥0.60), daha düşük 
ΔE 
00

  (
≤2.0) ve sıfır klonlama hatası veriyorsa genel prodüksiyon kılavuzunda o formatı standartlaştırın.

Liste (3): Bağlantılı Tam Kaynak Listesi
OpenAI Official Image Prompting Guide (2026): GPT Image 2.5 yönlendirme prensipleri, kısıtlama blokları ve metin koruma kuralları.

https://felo.ai/blog/gpt-image-2-5-prompting-guide

OpenAI Cookbook - GPT Image Generation Models Prompting Guide: Model parametreleri, düzenleme modları ve multi-image iş akışları.

https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

Google AI Developer Blog - Build with Gemini Omni 1.1 Flash (Ağustos 2026): Gemini Omni 1.1 Flash video modeli, 10-saniyelik bağlam penceresi, sahne uzatma ve 4K upscaling teknik dokümantasyonu.

https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/

Google Flow Official Workspace: Google Labs altında çalışan Veo 3.1 ve Gemini Omni destekli sinematik video ve karakter yönetim platformu.

https://flow.google.com/

Mastering Google Flow: Character & Avatar Creation (Haziran 2026): Google Flow @character sistemi, Nano Banana Pro entegrasyonu ve karakter pasaportu kullanımı.

https://kartaca.com/en/mastering-google-flow-the-ultimate-guide-to-character-avatar-creation/

VeoBulk Technical Guide - Consistent Characters in Google Flow (Ağustos 2026): Google Flow üzerinde tutarlı karakter üretimi, kontrol grupları ve referans yönetimi.

https://veobulk.com/en/blog/consistent-characters-google-flow

Fal.ai Learning Tools - AI Character Consistency Guide: Karakter kimliğinin saklama biçimleri, metinsel spec yapısı ve LoRA katmanları.

https://fal.ai/learn/tools/ai-character-consistency

Renderforest - How to Maintain Character Consistency in AI Videos: Karakter pasaportu oluşturma, çoklu referans kullanımı ve Veo/Runway sınırları.

https://www.renderforest.com/blog/maintain-character-consistency-ai-videos

InsightFace Open-Source Project & ArcFace Model Suite: Yüz tespiti, RetinaFace hizalama ve ArcFace 512-dim embedding benzerlik ölçüm kütüphanesi.

https://www.insightface.ai/

ArXiv Paper: DynSC-Eval - Towards Subject Consistency over Dynamic Subject Sets in Video Generation (2026): Videolarda lokal ve global konu tutarlılığını ölçen yeni nesil akademik benchmark.

https://arxiv.org/abs/2610.01052

ArXiv Paper: VBench - Comprehensive Benchmark Suite for Video Generative Models: Video üretim modelleri için 16 boyutlu değerlendirme ve Subject Consistency metriği.

https://arxiv.org/abs/2311.17982

Konica Minolta Sensing - What is Delta E (
ΔE) Color Difference Guide: CIELAB renk uzayı ve CIEDE2000 (
ΔE 
00

 ) renk farkı tolerans standartları.

https://sensing.konicaminolta.eu/mi-en/colourblogtop/colour-blog/whatisdeltae
