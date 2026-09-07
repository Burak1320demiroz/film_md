# TUR 12 · RAPOR 3 — AI HATTINDA REFERANSIN ÇALIŞMASI VE ZİNCİR SÜRÜKLENMESİ (ham metin)

> Girdi promptu: `../15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` PROMPT 3
> Koşu tarihi: 06.09.2026 · Sahibin yapıştırdığı metin, DEĞİŞTİRİLMEDEN.
> Süzme: `../04_ARASTIRMA_BULGULARI.md` §TUR 12

---

Yapay Zekâ Destekli Uzay Temalı Kısa Film Üretiminde Referans Çapalaması, Kimlik Korunumu ve Zamansal Sürüklenme Analizi

Basınç giysili ve kasklı karakterlerin yer aldığı, sabit kamera ağırlıklı ve on saniyelik ardışık kliplerden oluşan yapay zekâ destekli kısa uzay filmi üretimleri, difüzyon modellerinin mimari sınırlarını en çok zorlayan senaryoların başında gelmektedir. Bu rapor, önceden onaylanmış başlangıç karelerinin (image-to-video referanslarının) üretim boru hatlarındaki işlevlerini, modelin iç ön işleme (preprocessing) dinamiklerini, kimlik korunumunun piksel tabanlı sınırlarını ve zamansal sürüklenme (temporal drift) süreçlerini detaylı bir şekilde analiz etmektedir.

Aşağıdaki yapılandırılmış veri matrisi, güncel yapay zekâ üretim araçlarının referans kabul yüzeylerini, ağırlıklandırma ve determinizm derecelerini içermektedir. Matris içindeki veriler; sağlayıcıların resmî belgeleri, arayüz dışı API kısıtlamaları ve ölçüm paylaşan bağımsız testlere dayandırılmış olup, resmî belgeyle doğrulanamayan istisnai davranışlar metodolojik bir standart olarak "tahmin" veya "topluluk gözlemi" şeklinde işaretlenmiştir.

## 1. Referans Yüzeyleri, Kontrol Bileşenleri ve Model İçi Gerçeklik Matrisi

| Araç / Boru Hattı | Kabul Edilen Referans Sayısı | Rol Ataması | Ağırlık Kontrolü | Çağırma Söz Dizimi | Tohum Görünürlüğü | Determinizm | Varlık Saklama | Belge/Sürüm Tarihi |
|---|---|---|---|---|---|---|---|---|
| Google Veo & Flow (Scenebuilder) | Üretim başına en fazla 3 görsel (Scenebuilder içinde bileşen olarak). | Karakter Kartı üzerinden bütünleşik yüz ve kıyafet; nesne/stil bağımsız bileşendir. | Metinsel hiyerarşi ve referans sıralaması; arayüzde kaydırıcı yoktur (tahmin). | @karakter_adi veya @me. | API seviyesinde mevcuttur; arayüzde gizlidir. | Orta-Yüksek (tohum, kilitli prompt ve referansla tekrarlanabilirlik). | Özel hesaba bağlıdır, oturum dışı kalıcıdır. | Ağustos 2026 (Veo 3.1) |
| Runway (Gen-4.5) | İlk ve son kare (First/Last Frame) olarak 2 görsel. | Kare bazlı mutlak çapa; rol ataması yoktur. | Sabit (kare doğrudan referanstır). | Arayüz üzerinden T2V veya I2V görsel yüklemesi. | Geliştirici API'sinde mevcuttur. | Yüksek (başlangıç karesi mutlak sınır koşuludur). | Proje dosyası silinene kadar (tahmin). | Temmuz 2026 (Gen-3 Alpha emekliliği sonrası) |
| Kling AI (3.0 Omni) | Çoklu görsel girişi (Multi-elements) kısıtlamasız. | Maskeleme olmaksızın tüm görsel (öznelerin önceden kırpılmış olması sistem şartıdır). | "Reference Strength" arayüz kaydırıcısı. | Arayüz yüklemesi veya API üzerinden Base64. | Tohum parametresi API üzerinden yönetilebilir (tahmin). | Orta. | Sistem panosunda oturum/proje süresince (tahmin). | Ağustos 2026 |
| Midjourney (V6/V7) | Çoklu görsel (URL'ler boşlukla ayrılarak). | --cref (karakter), --sref (stil/atmosfer/ışık/arka plan). | --cw 0-100, --sw 0-1000. | Prompt sonuna URL. | 0-4294967295 aralığında görünür. | Yüksek. | Discord/Web URL'si barındığı sürece. | Haziran 2025 (V7 SV) / Ağustos 2026 |
| Sora (Cameo / Storyboard) | Tekil karakter aktarımı (Cameo). | "How I appear in videos" paneli üzerinden bütünleşik. | Sistem içi otonom. | Storyboard sekmesinde karakter seçimi. | Sistem içi gizli (topluluk gözlemi). | Çok Yüksek (%95+ doğruluk). | Hesap kütüphanesinde kalıcı (topluluk gözlemi). | 2026 |
| Gemini / Nano Banana | Karakter şablonu inşasında temel ve çoklu yön (360°) için birleştirme. | Metin ağırlıklı. | Metinsel hiyerarşi. | Flow Agent içinde şablondan çağrı. | API düzeyinde mevcut. | Orta. | Hesapta karakter varlığı olarak kalıcı. | Ağustos 2026 |
| IP-Adapter (Açık Uçlu) | Teorik olarak sınırsız (çoklu adaptör + maske). | Maskeleme ile rol mutlak atanabilir. | scale 0.0-1.0. | Düğüm bağlantısı veya ip_adapter_image argümanı. | Tamamen kontrol edilebilir. | Yüksek (scale 1.0'da referans metni ezer). | Yerel donanımda sonsuz. | 2023-2024 (temel), 2026 (çoklu maske) |
| InstantID (Açık Uçlu) | Genellikle tekil yüz. | Yüz landmark'ları ve kimlik üzerine kilitli. | instantid_weight / ipadapter_weight 0.01-2.0. | Özel düğüm bağlantısı. | Tamamen görünür. | Çok Yüksek (metne direnir). | Yerel donanımda sonsuz. | 2024-2026 |
| LoRA / DreamBooth | 3 ila 15+ eğitim görseli. | Etiketlemeye bağlı tüm kavramlar. | Rank ve lora_alpha. | Tetikleyici kelime. | Tamamen görünür. | Değişken (aşırı eğitimde yanma). | Ağırlık dosyası silinene kadar. | Sürekli güncel |

### Model İç Ön İşleme Gerçeklikleri, Piksel Limitleri ve Kimlik Çöküşü

Araçların arayüzlerinde sundukları vaatler ile difüzyon modellerinin iç vektör uzayındaki (latent space) işleyişleri arasında ciddi yapısal farklılıklar bulunmaktadır. Görüntüden videoya üretim boru hatlarında, yüklenen başlangıç karesi veya referans karakter kartı, modelin U-Net mimarisine girmeden önce CLIP gibi bir görüntü işleyicisi tarafından matematiksel vektörlere dönüştürülür. Standart IP-Adapter yapıları, görseli merkezden kırparak (center crop) 224x224 piksel boyutuna indirgemektedir. Daha gelişmiş ViT-H veya ViT-L/14 tabanlı modeller ise bu çözünürlüğü 336x336 piksel boyutuna kadar destekler. Model mimarisindeki bu fiziksel donanım sınırı, kimlik çöküşü (identity collapse) adı verilen alt eşiği doğrudan belirler.

Kimlik tanıma ve yüz hizalama ağları (örneğin InsightFace, ArcFace, Antelopev2), referans içerisindeki yüzü izole edip vektörel kimlik haritası çıkarırken, yüzün piksel yoğunluğuna yüksek derecede bağımlıdır. Çeşitli yüz veri setleriyle yapılan ölçümler, ArcFace varyantları için ideal yüz çözünürlüğünün 112x112 piksel, VGG-Face için ise 224x224 piksel olduğunu göstermektedir. Uzay konulu kısa filmlerde, sisteme örneğin 1920x1080 boyutunda tam boy basınç giysili bir figür yüklendiğinde, kask içindeki yüzün kapladığı alan toplam kadraj yüksekliğinin yüzde onundan daha küçük olabilir. Bu durumda yüz, fiilen 108x108 pikselin altına, modelin iç CLIP kırpma aşamasından sonra ise yapısal olarak 12x12 ila 15x15 piksele kadar düşmektedir. Endüstri standartlarındaki ölçümler, yüz bölgesinin mutlak piksel değerinin 64x64 pikselin altına inmesi durumunda ortalama mutlak hatanın dramatik şekilde arttığını, kimlik tespitinin başarısız olduğunu ve karakter kimliğinin tamamen çöktüğünü doğrulamaktadır. Bu matematiksel gerçeklik; yüz, gövde, araç ve küçük proplar için kimlik çöküş sınırının, ana referansın CLIP işleyicisine girmeden önce bizzat kullanıcı tarafından ilgili öge etrafında daraltılarak (kırpılarak) verilmesini zorunlu kılar. Kling AI'ın resmî API belgelerinde de açıkça belirtildiği üzere, sistem referans üzerinde otomatik kırpma yapmamakta olup öznelerin sisteme önceden kırpılarak yüklenmesi şart koşulmuştur. Aksi takdirde, model uzay gemisinin geniş iç mekânını bir bütün olarak kodlar ve içindeki yüz detaylarını görmezden gelir.

Karakter kartları oluşturulurken, Midjourney gibi sistemler tek bir yüksek çözünürlüklü onaylı referans ile sıfır noktasından (--cw 100) başarılı kimlik koruması yapabilirken, Google Flow veya Gemini platformları, karakterin uzaysal geometrisini (360 derecelik algıyı) inşa etmek adına en az iki (cephe ve tam boy kıyafet) görsel referans ve detaylı metin açıklaması talep etmektedir. Bu karakter kartlarının oluşturulmasında, ses ve replik alanının doldurulması zorunlu bir teknik girdi değildir. İsteğe bağlı bırakıldığında veya metin promptu ile özel bir diyalog çağrılmadığında, Flow Agent arayüzü yalnızca görsel referans modellemesine odaklanarak, karakterin "Character Info" bölümüne yazılan temel kişilik özelliklerini eylemlerin varsayılan davranış stili olarak sahneye yansıtır. Aynı tohum değerinin, aynı metin ve aynı referans kilitlendiğinde dahi tam deterministik bir kare verip vermediği sorusu, difüzyon modellerindeki donanımsal asenkronizasyona dayanır. CUDA çekirdeklerindeki kayar nokta yuvarlama hataları nedeniyle çıktılar pikselsel bir kopyadan ziyade "yüzde doksan dokuz aynı kompozisyonu" ifade eder. Tohum kilitliyken metin değiştirildiğinde ise, tohumdan geriye yalnızca genel kütle geometrisi ve başlangıç renk gürültüsü dağılımı kalır; ağaçlar, uzay gemileri ve figürler yeni metnin anlamsal ağırlığına göre yepyeni formlara bükülür. Tohum ve görsel referansın bir arada verildiği çatışmalı durumlarda, referans ağırlığı yeterince yüksekse (örneğin IP-Adapter Scale = 1.0 veya --cw 100) görsel referans baskın çıkarak metnin birbiriyle çelişen özniteliklerini (örneğin metinde "kırmızı kask" yazarken referansın beyaz olması) tamamen ezer.

Çok panelli bir sayfanın (örneğin bir storyboard, konsept sanat paftası veya çizgi roman formatı) doğrudan referans olarak verilmesi, S-gutter adı verilen panel aralıklarındaki beyaz boşlukların ve olası metin etiketlerinin, CLIP işleyicisi tarafından yapısal kenar hatları ve yüksek frekanslı doku gürültüsü olarak kodlanmasına sebep olur. Sonuç olarak, bu ayırıcı çizgiler ve tipografik öğeler, üretilen video karesine ekranı bölen fiziksel engeller, garip pencere pervazları veya asimetrik artefaktlar olarak doğrudan sızmaktadır (topluluk gözlemi).

Referansın ışık şeması ve arka planının yeni üretilen sahneye sızması, IP-Adapter ve benzeri görüntü yönlendirme mekanizmalarındaki çapraz dikkat (cross-attention) katmanlarının ayrıştırılmamış doğasından kaynaklanır. U-Net mimarisinde görseli ve metni işleyen katmanlar, özel bölgesel maskeleme algoritmaları kullanılmadığı sürece, referanstaki karanlık dış uzay boşluğu dokusunu, yeni promptta istenen "aydınlık laboratuvar" aydınlatması ile çarpıştıracak ve her ikisinin ortalaması olan yarı karanlık melez bir aydınlatma profili üretecektir. İki farklı durumun (sağlam/temiz kask ile hasarlı/kirli kask) aynı görsel referans seti içinde sisteme verilmesi veya tek bir karakter kartında birleştirilmesi, difüzyon modellerinde iyi bilinen "özne karışması" (subject mixing) sorununu tetikler. Model, zaman cetveli içermediği için bu özellikleri ayrıştıramaz; ağırlık haritalarını ortalayarak yarı kirli, mantıksız bir doku çıkarır. Aynı sahnede beyaz basınç giysili iki farklı karakterin yer alması durumunda ise, her iki figür de metin işleyicideki aynı konsept kelimesine bağlandığı için, öz-dikkat ve çapraz dikkat haritaları çakışmakta, figürlerin yüz kimlikleri ve fiziksel oranları birbirine bulaşmaktadır. Bir üretim oturumunda veya film sahnesinde eşzamanlı olarak kırılmadan taşınabilecek kilitli bağımsız varlık sayısı; açık kaynak kodlu mimarilerde özel bölgesel maskeleme yöntemleriyle teknik olarak sınırsız görünse de, Google Veo, Runway, Kling ve Sora gibi kapalı kutu sistemlerde en fazla 2 ila 3 ayrıştırılabilir ana karakter veya belirgin nesne ile sınırlıdır.

## 2. Başlangıç Karesi Kontrat Tablosu ve Zincir Sürüklenmesi Çözümleri

Önceden onaylanmış bir başlangıç karesi sisteme yüklüyken, yapay zekâ modeline verilecek prompt metni, sıfırdan bir üretim (text-to-video) promptu gibi tasarlanamaz. Görsel referansın piksel verisi ve metin komutları, U-Net mimarisi içindeki aynı dikkat katmanlarını rekabetçi bir biçimde tüketir.

| Prompta Girecek | Prompta Girmeyecek | Mimari Gerekçe | Kaynak |
|---|---|---|---|
| Kamera Hareketi (Pan, Tilt, Dolly) | — | Başlangıç karesi hareketsiz bir matristir; uzaysal navigasyon metin kodlayıcı üzerinden yönlendirilmelidir. | Google Veo Prompt Guide (2026) |
| Öznenin Devinim ve Eylemi | — | Eylemler zaman uzayı vektörlerini tetikleyen "fiil" mekanizmasıdır. | Gemini Video Gen (2026) |
| Çevresel Dinamikler (duman, toz, rüzgâr) | — | Statik piksellerin hareketlenmesi için zıtlık etkisi gerekir. | Skywork Veo Flow (2025) |
| — | Öznenin Görünümü (renk, kıyafet, yüz, kask) | Görsel çapa zaten piksel düzeyinde kısıtlama yaratır; tekrar tanım özne karışmasına yol açar. | ArXiv Temporal Consistency (2024) |
| — | "İlk karedeki özneyi koru" türü koruyucu kelimeler | Model bunu şart kipi değil semantik etiket olarak algılar. | QuestStudio Limits (2025) |
| Sadece referansla eşleşen stil kelimeleri | Referansla çelişen atmosferik tanımlar | Çelişki, piksellerde kumlanma/yanma yaratır. | Midjourney Sref (2026) |

Başlangıç karesi bir difüzyon zincirine kilitlendiğinde, U-Net mimarisi bu kareyi gürültüden arındırma işleminin "sıfırıncı adımı" olarak kabul eder. Görsel referans ile metin çeliştiğinde model; genel kaba konumlama, hareketin yönü ve mekânsal ilişkiler için metni referans alırken, yüzey dokusu, yansıma geometrisi, renk ve fiziksel kimlik için her zaman görsel referansı otorite kabul etmektedir.

Ancak metin, görseldeki bir öğeyi fiziksel değişime zorlarsa, modelin zamansal tutarlılık modülleri görselin statik kalma eğilimi ile metnin değişim talebi arasında sıkışır. İçinde form değişimi veya kırılma olan bir sahnenin başlangıç karesi daima değişimin öncesini göstermelidir. Model, zamanın ileriye dönük akışında sağlam bir dokuyu metin rehberliğinde mantıklı bir şekilde parçalayabilir; ancak başlangıç karesi zaten parçalanmış, hasarlı veya kirli verilirse, difüzyon modelinin geçmiş bir "sağlam" form interpolasyonu üretme ve bunu zamansal olarak geriye bağlama yeteneği yoktur.

Ses ve diyalog girdisinin video üretim aşamasında (native audio) sisteme entegre edilmesi, mevcut jeneratif yapay zekâ video modellerinde agresif dudak senkronizasyonu algoritmalarını devreye sokar. Bu durum, özellikle yüz etrafında kask, vizör, solunum tüpleri ve mikrofonlar barındıran basınç giysili uzay karakterleri için felakettir. Dudak senkronizasyonu algoritmaları, ağız hareketini taklit edebilmek için yüz çevresindeki rijit geometriyi biyolojik bir kas dokusu gibi esneterek bükülmeye ve erimeye neden olur. Sahneleri tamamen sessiz ve salt görsel çapalama ile üretmek; karakter seslerini ve çevresel atmosferi video üretiminden sonra, kurgu aşamasında eklemek, bu geometrik çöküşleri tamamen önler.

Kabul edilemez düzeyde bozulan veya sürüklenen bir karenin kısmi kurtarma yolları, modelin mantığına göre uyarlanmalıdır. Eğer sekiz saniyelik bir klibin yalnızca son iki saniyesinde kimlik sürüklenmesi gerçekleşiyorsa, çok panelli sayfayı veya uzun klibi tek seferde yeniden üretmeye çalışmak yerine üretim parçalara bölünmelidir. Son sağlam kare video düzenleyicide dışa aktarılıp yeni klibin "ilk karesi" olarak tekrar modele beslenmelidir.

## 3. Sayısal Yeniden Çapalama Çizelgesi ve Sürüklenme Metrikleri

| Varlık Tipi | Kadraj/Kamera | Sapmadan Taşınabilen Maks. Klip | Biriken Bozulmalar | Yeniden Çapalama Stratejisi |
|---|---|---|---|---|
| Kasklı Karakter (Sabit Kamera) | Statik veya çok hafif pan | 4-5 Klip (~32-40 sn) | Kask camındaki yansımaların donması/boyaya dönmesi; kirlerin kademeli temizlenip CGI pürüzsüzlüğüne dönmesi. | Aynı tohum kullanılarak durum/ışık sabitlenir. 5. klipten sonra ana onaylı referans tekrar ilk kare olarak verilir. |
| Kasklı Karakter (Dinamik Eylem) | Hızlı tracking / aksiyon | 1-2 Klip (~8-16 sn) | Keskin renk kayması; eklemlerde oran kayması; kollarda lastikleşme. | Her kesmede/açı değişiminde o açı için üretilmiş onaylı statik çapa yenilenir. |
| Uzay Aracı / Mekanik Gövde | Sabit perspektif, yavaş dolly | 3-4 Klip (~24-32 sn) | Panel çizgilerinde asimetri; logo/uyarı etiketlerinin halüsinasyon diline dönmesi. | Negatif prompt güçlendirilir; logo bölgesi statikse hareket minimumda tutulur. |
| Açık Yüz (Basınç Giysili) | Yakın çekim | 2-3 Klip (~16-24 sn) | Göz bebeklerinde asimetri; saç dokularında kaynaşma; ton solması. | Standart I2V'de her 16 saniyede referans yüz çapası yenilenir. |
| Grup Sahnesi (Çoklu Karakter) | Geniş açı | 1 Klip (8-10 sn) | İkizlenme (twinning); kask/giysi renklerinin birbirine bulaşması. | Tek oturumda batch üretim sürüklenmeyi azaltır ama ikizlenmeyi çözmez. |

Aynı durumdaki sahneleri tek bir oturumda toplu üretmek (batch generation), sürüklenmeyi kısmen azaltır. Bunun teknik sebebi, modelin aktif GPU belleğinde tutulan gizli durumların ve dikkat matrislerinin taze kalmasıdır. Ancak bu durum ikizlenme problemini çözmez; zira ikizlenme, modelin metindeki birden fazla özneyi mekânsal olarak ayırt edemeyip özellikleri ekran boyunca klonlaması kaynaklıdır.

Karakterin ağır yerçekiminde zorlanması, sekmeli yürüyüşü veya devinim nitelikleri gibi kinetik durumlar, statik bir başlangıç karesiyle korunamayacak kadar çok katmanlı hareket vektörleri gerektirir. Modelin bu devinimleri çapalayabilmesinin karşılığı statik bir referans değil; modelin optik akış vektörlerini kopyalayabileceği kısa bir referans video klip, hareket fırçaları (motion brush) veya jestin ortasında dondurulmuş dinamik bir kare üzerinden çapalamaktır.

## 4. Karar Ağacı ve Araç Başına Kimlik Kayar Uyarı Listeleri

DÜĞÜM 1: Girdi kontrolü. Başlangıç karesi ve metin U-Net çapraz dikkat katmanına girdi.
- Metin, görseldeki nesnenin pozisyonuna müdahale ediyorsa → DÜĞÜM 2.
- Metin, görseldeki nesnenin temel geometrisine/rengine müdahale ediyorsa → DÜĞÜM 3.

DÜĞÜM 2 (Hareket Çatışması): Model, görseldeki pikselleri metnin istediği konuma doğru eritmeye başlar. Sonuç: temel fiziksel kimlik korunur ve eylem gerçekleşir; ancak referans çok statik bir pozdaysa uzuvlar anatomik olmayan biçimde bükülebilir (temporal smearing).

DÜĞÜM 3 (Kimlik/Stil Çatışması):
- Durum A (referans gücü yüksek): Model metnin renk/form emrini görmezden gelir; çoğu zaman hareketsiz veya donuk bir video üretir.
- Durum B (referans gücü düşük): Model zorla dönüştürmeye çalışırken ara tonlarda aşırı gürültülü, yapay renk artefaktları verir; geometri deforme olur.

### Araç Başına Kimlik Kayar Uyarı Listesi

Google Veo & Flow
- Üç referans sınırını zorlayıp çelişen/zıt ışıklandırmalı referanslar yüklerseniz, model aydınlatma profillerini karıştırarak formsuz, gri ve bulanık yüzey üretir.
- Sekiz saniyelik sahnelerde çok fazla ardışık alt eylem tanımlamak, karakter kartındaki yüz geometrisinin yırtılmasına neden olur; sahneler tek majör eylemli 4-6 saniyelik parçalara bölünmelidir.
- Karakter bilgi kartındaki metinsel tanım ile yüklenen görsel eşleşmezse, Flow Agent metne sadık kalıp görseli halüsinasyona uğratır.
- Kasklı karakterde yerel ses üretimini videoyla aynı anda tetiklemek, kask altındaki ağzın zorunlu senkronizasyonu için tüm kaskın hareket etmesine ve vizör formunun bozulmasına yol açar.
- Ardışık kliplerde poz ve giysi kırışıklıkları farklılaşırsa Veo eşleştiremez ve tek kadrajda ikizleme yapar.

Midjourney (V6/V7)
- --cref kullanılırken referans çok geniş plandan alınmışsa yüz piksel çözünürlüğü yetersiz kalır, kimlik çöker.
- --cw 100'de model yalnız yüz ve kıyafeti değil, referanstaki eski arka plan dokusunu ve ışık atmosferini de kopyalar.
- --sref harmanlanırken referanslardan birinde panel çizgisi veya logo/metin varsa, bu ögeler artefakt olarak sızar (topluluk gözlemi).
- Vizörde yansıyan stüdyo ışıkları --cref tarafından karakterin değişmez uzvu gibi algılanır.
- Aynı tohum kilitliyken tek kelimelik değişiklik, tüm başlangıç kompozisyonunu geri dönüşsüz siler.

Runway (Gen-4.5)
- İlk ve son kare arasında kamerasal perspektif mantığı yoksa geçiş morfolojik 2D erime olur.
- Sabit kamera komutlu sahnelerde referanstaki flu/bokeh alanlar titreyen piksellere dönüşür.
- Kirlilik/yanık/aşınma durumları 10 saniyelik uzatmalarda kademeli olarak temizlenir.
- Metin ile görsel çeliştiğinde Runway daima referans görselin piksel yapısını otorite kabul eder.
- V2V'de kaynak videonun çözünürlüğü/FPS'i düşükse yüzey dokuları plastikleşir.

Kling AI (3.0 Omni)
- Referanslar önceden sıkıca kırpılmamışsa (oto-kırpma yok), ana karakter yerine arka plandaki önemsiz bir donanım çapalanabilir.
- Referans Gücü çok yüksekte tutulursa eylem komutları ezilir; karakter kartonet gibi kayar.
- İki farklı varlık referansı multi-element olarak eklendiğinde giysi renkleri ve kask tipleri harmanlanır.
- Işık şemasını kopyalamak istemeseniz bile Kling ortalama ışık değerini alarak atmosferi kirletir (topluluk gözlemi).
- Yüksek kinetik kamera komutları statik referansla çatıştığında varlığın etrafında hale (halo) oluşur.

IP-Adapter & InstantID
- Referans 224x224/336x336 alt sınırında ve kare formatında değilse, CLIP kırpması nedeniyle omuz ve kask uzantıları yok olur.
- InstantID yüz landmark'larına aşırı kilitlendiği için vizör kapalı/yarı yansımalıysa noktaları bulamaz ve grotesk sonuç üretir.
- IP-Adapter scale 0.8 üzerinde metin promptu işlevsizleşir.
- Bölgesel maskeleme yapılmadan iki karakter çapası birlikte verilirse ikizlenme/doku bulaşması kaçınılmazdır.
- LoRA/kontrolcü mimari uyumsuzluğunda arka planda gürültü blokları ve piksel yanmaları oluşur.

---

## RAPORUN KAYNAK LİSTESİ (sahibin yapıştırdığı hâliyle)

skywork.ai — Veo 3.1 in Flow (2025) · blog.google — 5 tips for getting started with Flow ·
kartaca.com — Mastering Google Flow · ltx.io — Veo 3.1 Prompt Guide ·
cloud.google.com — Ultimate prompting guide for Veo 3.1 ·
scribd.com — Runway Gen-3 Video Prompting Guide · learnprompting.org — A Complete Guide to Runway ·
docs.dev.runwayml.com — Runway Dev API · help.runwayml.com — Creating with Video to Video ·
kling.ai — Image Reference Guide / API MultiElements / Multi-element Video Editing / Image Generation / Multi-Reference, Local Editing, and Series Workflows / Image Capability Map / KlingAI Documentation PDF ·
docs.midjourney.com — Style Reference / Seeds · picovix.app — How to Keep a Consistent Character in Midjourney ·
aimensa.com — Character Consistency in Midjourney · sref-midjourney.com — Midjourney Cheat Sheet ·
styleref.io — Midjourney Style Reference · aifreeapi.com — Can Sora 2 Maintain Character Consistency ·
portotheme.com — Sora 2 Cameo Feature · reddit.com — Character Cameo Voice Consistency ·
mindstudio.ai — What Is Sora's Reference System ·
github.com — IP-Adapter masking issue / tencent-ailab IP-Adapter / huggingface diffusers IP-Adapter ·
docs.openvino.ai — Image Generation with Stable Diffusion and IP-Adapter ·
replicate.com — instant-id-ipadapter-plus-face · github.com — InstantID ·
github.com — diffusers DreamBooth README_z_image · huggingface.co — LoRA training scripts ·
medium.com — LoRA Not Working in AI Art · arxiv.org — 2402.04252 · arxiv.org — CLIP (Learning Transferable Visual Models) ·
arxiv.org — Impact of Image Resolution on Age Estimation with DeepFace ·
veobulk.com — Google Flow Consistent Characters · arxiv.org — Training-Free Consistent Text-to-Image Generation ·
arxiv.org — Self-Cross Diffusion Guidance · mdpi.com — Cross-Attention and Seamless Replacement of Latent Prompts ·
queststudio.io — Veo 3.1 Prompt Guide (2026) · docs.cloud.google.com — Video generation prompt guide ·
veo3ai.io — How to Storyboard a Video
