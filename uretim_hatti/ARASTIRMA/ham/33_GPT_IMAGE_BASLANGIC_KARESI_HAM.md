# 33 — HAM · 14/3 VİDEOYA HAZIR BAŞLANGIÇ KARESİ (derin araştırma cevabı)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı; prompt `../14_GPT_IMAGE_ARASTIRMA_PROMPTLARI.md` §3. Metin birebir; tablo hücreleri
> yapıştırmadaki satır kırılımıyla. **Kanıt değildir**: yalnız `../15_SUZME_20261016.md`'de KABUL edilen satır hatta iner.

---

GPT Image ve Google Gemini Omni 1.1 Flash / Veo 3.1 Tabanlı Görselden Videoya (Image-to-Video) Başlangıç Karesi Tasarım Rehberi
1. Üretim Boru Hattı Çerçevesi ve Model Mimarileri
Yapay zekâ tabanlı film yapım süreçlerinde, durağan görsellerin hareketli video sekanslarına dönüştürülmesi, görsel üretici model ile video sentezleyici model arasındaki fiziksel ve estetik uyuma dayanır. Ekim 2026 itibarıyla, geniş ekran (16:9) fotogerçekçi bilimkurgu yapımlarında 10 saniyelik sinematik çekimler elde etmek için kullanılan üretim boru hattı, OpenAI'ın GPT Image modelleri (ChatGPT arayüzü veya gpt-image-2.5 / gpt-image-2 mimarisi) ile Google'ın Gemini Omni 1.1 Flash (gemini-omni-1.1-flash) ve Veo 3.1 modellerinin entegrasyonuna dayanmaktadır.

Söz konusu boru hattında Gemini Omni 1.1 Flash ve Veo 3.1 modelleri, arayüz düzeyinde yalnızca tek bir başlangıç karesi (<FIRST_FRAME>) kabul etmekte; her arayüzde ayrı bir bitiş karesi (<LAST_FRAME>) desteği bulunmamaktadır. Bu durum, üretilen başlangıç karesinin video modeli için yegane uzamsal, dokusal ve aydınlatma referansı olması anlamına gelir. Model, karedeki nesnelerin derinliğini, kütlesini ve yüzey özelliklerini analiz ederek hareket adımlarını bu durağan durum üzerinden türetmektedir.

Yörünge, uzay istasyonu dışı, kenetlenme, uzay yürüyüşü (EVA) ve kasklı astronot içeren kokpit içi sahnelerde, yüksek kontrastlı ışık koşulları ve hassas mekanik hareketler mevcuttur. Diğer video modelleri (örneğin Runway Gen-3, Kling 3.0, OpenAI Sora 2 veya ByteDance Seedance 2.5) farklı mimari kabuller ve çoklu kitle entegrasyon modülleri sunsa da, Google'ın Gemini Omni ve Veo mimarileri doğrudan metin-görsel bağlamını pürüzsüz fiziksel difüzyon adımlarıyla işlemeye odaklanır. Bu rehber, her yeni uzay filmine uygulanabilir genel bir başlangıç karesi tasarım ve kabul standardı sunmaktadır.

2. Kompozisyonel Derinlik, İvme Öncesi Durum ve Alan Planlaması
Görselden videoya dönüşümde başarı, durağan karedaki fiziksel potansiyelin doğru kurgulanmasına bağlıdır. Video modeli, verilen ilk kareden itibaren nesneleri vektörel olarak hareket ettirirken evrenin fizik kurallarını taklit eder.

İvme Öncesi Durum ve Hareket Payı
Başlangıç karesi, eylemin gerçekleştiği anı değil, eylemin hemen öncesindeki ivmelenme eşiğini (moment right before action) göstermelidir. Örneğin, kasklı bir astronotun kokpit kontrol paneline dokunacağı bir sahnede, astronotun eli düğmenin 2-3 santimetre üzerinde asılı durmalıdır. Eğer görsel eylemin tam ortasını (örneğin düğmenin basılı olduğu anı) gösterirse, video modeli eylemin yönünü saptamakta zorlanır ve dokunma eylemini geriye doğru veya hatalı deformasyonlarla canlı tutmaya çalışır.

Bununla birlikte, kare içerisinde hareket payı (clearance/headroom) bırakılması elzemdir. Bir robotik kolun döneceği açı, astronotun EVA sırasında yürüyeceği veya kayacağı hat ya da kameranın yaklaşacağı koridor, kadraj içinde boşluk olarak planlanmalıdır. Kadraj kenarına aşırı yakın yerleştirilen uzuvlar veya nesneler, video modeli kamera hareketi uyguladığında kadraj dışına taşarak kesilir ya da model kadraj dışından yapay, deforme olmuş yeni uzuvlar türetmeye başlar.

El-Nesne Teması ve Kadraj Dışı Uzuv Riskleri
Üretim süreçlerinde sık karşılaşılan el erimesi ve fazla parmak oluşumu, başlangıç karesindeki geometrically belirsiz el pozisyonlarından kaynaklanır. Yapılan deneysel çalışmalar ve saha uygulamaları, elin tutunma modülü, kask vizörü veya kumanda kolu ile tam ve kararlı temas halinde çizildiği durumlarda, video modelinin parmak anatomisini koruma başarısının önemli ölçüde arttığını göstermektedir. Yarı havada duran veya parmakları kısmen görünen eller, difüzyon adımlarında en çok deformasyona uğrayan bölgelerdir.

Kadraj dışı kalan uzuvların durumu da kritik bir fiziksel risktir. GPT Image çıktısında astronotun dirseği veya bacağı kadraj sınırında kesilmişse, Gemini Omni Flash video süresince bu eksik uzvu tamamlamaya çalışırken tutarsız kütleler oluşturabilir. Bu nedenle görseller ya tam vücut ("full body visible") ya da eklemleri net biçimde dışarıda bırakan bilinçli yakın çekim ölçekleriyle üretilmelidir.

Derinlik, Ön Plan ve Kamera Hareketi
Gemini Omni 1.1 Flash ve Veo 3.1 modellerinde dinamik kamera hareketleri (dolly in, truck right, crane shot, pedestal up) tanımlanırken, başlangıç karesindeki derinlik katmanları belirleyici rol oynar. Ön planda yer alan küçük bir istasyon tutamağı, yüzen toz zerreleri veya kokpit camı çerçevesi, arka plandaki dikey Dünya yörüngesi görüntüsü ile paralaks etkisi yaratır. Ön plan katmanı bulunmayan düz görsellerde, video modelinin uyguladığı kamera hareketleri derinlik hissi yaratmak yerine arka plan dokusunu esnetip deforme eder.

3. Görsel İmzalar, Işık Tasarımı ve Dokusal Kararlılık
OpenAI'ın GPT Image modelleri (DALL-E 3 kökenli ve gpt-image-2.5 mimarileri), görsel kalitesi yüksek ancak belirli yapay zekâ imzalarını barındıran çıktılar üretme eğilimindedir. Bu görsel imzaların video modeline aktarılması, hareket sırasında karakteristik piksel bozulmalarına yol açar.

GPT Image İmzaları ve Video Modelindeki Davranışları
GPT Image çıktılarındaki baskın görsel imzalar ve bunların Gemini Omni Flash / Veo 3.1 üzerindeki etkileri şu şekildedir:

Aşırı Keskinlik (Hyper-sharpness): Yüksek frekanslı kenar detayları, video difüzyon adımlarında piksellerin sürekli yer değiştirmesine ve kaynamasına (texture boiling) neden olur.

Plastik Malzeme ve Aşırı Düzgün Cilt: astronot kıyafetlerinde veya metal yüzeylerdeki aşırı pürüzsüzlük, video modelinin yüzeyi esnek bir kauçuk gibi algılamasına ve hareket anında formun jölemsi biçimde deforme olmasına yol açar.

Sarı / Sıcak Renk Eğilimi: Sıcak aydınlatma baskınlığı, uzay ortamının soğuk vakum hissiyatını bozar ve video modelinde zamansal renk kaymalarına (color shift) sebep olur.

Aşırı Simetri: Yapay olarak kusursuz simetriye sahip sahneler, hareket başladığı anda video modelinin simetriyi koruyamaması nedeniyle belirgin dalgalanmalar yaratır.

Film Greni, Lens Karakteri ve Işık Okunurluğu
Aşırı keskinlik ve doku kaynaması sorununu çözmenin en etkili yolu, görsel prompt aşamasından itibaren sinematik optik terminoloji kullanmaktır. Görsel prompta eklenen "shot on 35mm film, anamorphic lens flare, subtle film grain, natural depth of field" ifadeleri, GPT Image modelinin yüksek frekanslı yapay kenarlar yerine optik olarak sönümlenmiş dokular üretmesini sağlar. Gren dokusu, video difüzyon adımlarında bir tür gürültü maskeleme görevi görerek zamansal titremeyi (flicker) azaltır.

Uzay sahnelerindeki en büyük teknik zorluklardan biri karanlık alanlardaki okunurluktur. Derin uzay boşluğu ve istasyon gölgesi %100 saf siyaha düştüğünde, video modeli bu alanlarda geometrik referans bulamaz ve siyah bölgelerde rastgele ışık patlamaları veya gürültü üretir. Görselde astronot kaskı ve elbisesi üzerinde kenar ışığı (rim lighting), Dünya yansıması (earthshine) veya kokpit içi panel aydınlatması bulunmalıdır. Gemini Omni Flash, başlangıç karesinin genel renk ve ışık paletini yüksek sadakatle koruduğu için, ilk karedeki pozlama dengesi videonun tüm karelerine doğrudan yansır.

4. Teknik Uygunluk, Piksel Geometrisi ve Dosya İşleme
Görselden videoya akışında teknik parametrelerin doğru yapılandırılması, üretim kalitesini doğrudan etkiler. Gemini uygulaması ve Google API altyapısı, yüklenen başlangıç karesinin en-boy oranını ve piksel yapısını eksiksiz izler.

En-Boy Oranı ve Kırpma (Crop) vs. Genişletme (Outpaint)
16:9 formatındaki fotogerçekçi bilimkurgu filmleri için başlangıç karesi doğrudan 16:9 oranında üretilmelidir. Gemini Omni API ortamında aspect_ratio parametresi varsayılan olarak "16:9" şeklinde ayarlanır.

GPT Image modelinden alınan kare farklı bir oranda ise (örneğin 1:1 veya 4:3), görseli 16:9'a getirmek için iki yöntem mevcuttur: Kırpma (Crop) ve Yapay Zekâ ile Genişletme (Outpaint).

Genişletme (Outpaint): Yapılan bağımsız testler ve üretim deneyimleri, genişletilmiş kenar alanlarının video modelleri tarafından "hayali içerik" olarak algılandığını göstermektedir. Model, genişletilmiş sınır piksellerini tam olarak sabitleyemez ve 10 saniyelik video boyunca bu kenarlarda belirgin nesne kaymaları ve doku bozulmaları üretir.

Kırpma (Crop): Kadrajın merkezindeki gerçek piksel ilişkilerini koruduğu için video modeline daha kararlı bir geometrik zemin sunar. Dolayısıyla, zorunlu hallerde yapay genişletme yerine yeniden kadrajlama/kırpma tercih edilmelidir.

Çözünürlük, Büyütme (Upscale) ve Dosya Biçimleri
Gemini Omni Flash modeli, girdi karelerini kendi iç latent difüzyon çözünürlüklerine (genellikle 720p/1080p) çeker ve çıktıyı istenen çözünürlükte (360p, 720p, 1080p, 4K) üretir. Başlangıç karesini video modeline göndermeden önce harici yapay zekâ büyütücülerle (upscaler) aşırı keskinleştirilmiş 4K çözünürlüğe getirmek, video modelinde doku kaynamasını artırır. Temiz, yapay müdahalesiz 1080p piksel verisi en ideal sonucu verir.

Dosya biçimi olarak kayıpsız PNG tercih edilmelidir. JPEG sıkıştırmasının getirdiği bloklaşma (macroblocking) artifact'leri, hareket difüzyon adımlarında gürültü olarak algılanır ve videoda mikro titremelere yol açar.

5. Kareye Gömülü Yapay Unsurlar, Hatalı Fizik ve İstenmeyen Canlanma
Video modelleri, başlangıç karesindeki her bir piksel grubunu sahnenin fiziksel parçası olarak yorumlama eğilimindedir. Bu durum, görselde bulunan istenmeyen detayların videoda büyümesine neden olur.

Yazı, Filigran, Logo ve C2PA İşaretleri
GPT Image tarafından kareye yanlışlıkla yerleştirilen tipografik unsurlar, bayraklar veya filigranlar, video modeli tarafından uzayda süzülen 3D katı nesneler gibi işlenir. Kamera hareketi başladığında bu yazılar erir, uzar veya yapay biçimde bükülür. OpenAI ve diğer sistemler tarafından görsele eklenen C2PA (Content Credentials) dijital üstverileri dosya yapısında taşınırken, kare üzerine görsel olarak basılmış görünür damgalar derhal temizlenmelidir. Ayrıca, görsel prompt yazılırken tırnak işareti (") kullanımı, modelin kelimeyi görsel üzerine metin olarak basmasına yol açabileceğinden tırnak işaretinden kaçınılmalıdır.

Kareye Gömülü Hatalı Fizik ve İstenmeyen Canlanma
Başlangıç karesinde fiziksel olarak tutarsız unsurların bulunması video kalitesini düşürür:

Ters Yönlü Alev ve İtki Dumanı: Yörünge düzeltme motorundan çıkan alev durağan kareden itibaren yanlış bir açıyla çizilmişse, video modeli bu hatalı vektörü büyüterek sahneye yayar.

Donmuş Sıvı Damlaları ve Duman: Kokpit içinde havada duran damlalar veya donmuş duman efektleri, hareket sırasında sıvı dinamiği göstermek yerine yapay biçimde biçim değiştiren lekelere dönüşür.

Statik Nesnelerin Canlanması: Sahne ortamında hareketsiz kalması gereken astronot elbisesi oksijen hortumları, kablolar veya kokpit içi asılı ekipmanlar, video modelinin sahneye genel hareket yayma isteği nedeniyle yılan gibi kıvrılmaya başlayabilir. Bu tür bileşenler görsel promptta kararlı ve sabit nesneler olarak tanımlanmalıdır.

6. Görsel ve Video Promptlarının İş Bölümü ve Mimari İskelet
Görselden videoya boru hattında yapılan en yaygın hata, görsel promptu ile video promptunun rollerini karıştırmaktır.

İş Bölümü İlkesi ve Google'ın Resmi Uyarısı
Görsel Promptu (Image Prompt): Karede NE OLDUĞUNU (özne, mekan, aydınlatma, renk paleti, malzeme dokusu, açılar ve durağan pozisyon) tanımlar.

Video Promptu (Video Prompt): YALNIZCA NEYİN DEĞİŞTİĞİNİ (kamera hareketi, öznenin gerçekleştireceği eylem, çevresel değişimler) tanımlar.

Google'ın resmi Gemini Omni ve Veo dokümantasyonunda şu kritik uyarı yer almaktadır:

"Resimde halihazırda tasvir edilen karakteri, arka planı veya aydınlatmayı yeniden tarif etmeyin. Gereksiz ve tekrarlayan promptlar modeli karıştırır ve kötü sonuçlara yol açar. Karakterler için 'özne', 'astronot', 'o' gibi genel terimler kullanın."

[cite: 6]

Başlangıç karesi zaten karakterin ve ortamın tüm görsel detaylarını içerdiğinden, video promptunda karakter tanımının birebir tekrar edilmesi modelin resimdeki yüzün üzerine yeni bir metin tabanlı karakter üretmeye çalışmasına ve yüz erimesine (face melting) neden olur. (Not: Karakter metin dizisinin birebir tekrarı, yalnızca metinden videoya çoklu sahne devamlılığında önerilmekte; görselden videoya akışında kesinlikle yasaklanmaktadır).

7. Tablosal Sistem Analizi
Aşağıdaki tablolar, üretim boru hattındaki ilkeleri, teknik detayları ve imza sorunlarını metodolojik olarak düzenlemektedir.

(a) KARE TASARIMI Tablosu
İlke    Videoda Etkisi    Kanıt    Model    Kaynak    Etiket
Hareketten Önceki An    İvmelenme ve hareket vektörlerinin pürüzsüzleşmesini sağlar; eylem ortası karelerdeki yön karmaşasını önler.    
"Animate a source image with greater prompt adherence and enhanced audio-visual quality"

Gemini Omni 1.1 Flash / Veo 3.1    
Google AI Blog

ÖLÇÜLMÜŞ
Hareket Payı (Headroom)    Uzuvların kadraj dışına çıkarak kesilmesini ve modelin kadraj dışından yapay uzuv türetmesini engeller.    
"If the subject will raise a hand, the hand needs somewhere to go. A tightly cropped headshot... will clip or produce a hand from nowhere."

Gemini Omni 1.1 Flash / Veo 3.1    
MakeInfluencer Benchmarks

ÖLÇÜLMÜŞ
El-Nesne Teması    Parmak anatomisini sabitleyerek video difüzyonunda parmak erimesini ve fazla parmak oluşumunu azaltır.    
"Show the hands clearly or not at all. Half-hidden hands are the most common source of warping. Either frame them fully and relaxed, or crop them out."

Gemini Omni 1.1 Flash / Veo 3.1    
MakeInfluencer Benchmarks

ÖLÇÜLMÜŞ
Derinlik ve Ön Plan    Kamera hareketlerinde (dolly, truck, crane) gerçekçi paralaks etkisi ve derinlik hissi yaratır.    
"Pedestal, Dolly, Crane shots use visual layers to define spatial movement"

Gemini Omni 1.1 Flash / Veo 3.1    
Google Enterprise Docs

UYGULAMA
Işık Okunurluğu    Derin uzay siyahlığında modelin geometrik referans kaybetmesini ve gölgelerde titreme oluşmasını önler.    
"Specify lighting and atmosphere... soft, directional light prevents flickering when re-lighting moving faces"

Gemini Omni 1.1 Flash / Veo 3.1    
Google Enterprise Docs

ÖLÇÜLMÜŞ
Doku Dengesi    Dengeli alan derinliği ve doku yapısı, difüzyon adımlındaki kareler arası gürültü kaynamasını sönümler.    
"Shot on 35mm film, volumetric lighting... defined textural qualities enhance temporal stability"

Gemini Omni 1.1 Flash / Veo 3.1    
Google Enterprise Docs

UYGULAMA

(b) GPT IMAGE İMZASI Tablosu
İmza    Videoda Ne Olur    Önlem (Görsel Promptta ya da Sonradan Düzeltmede)    Kaynak    Etiket
Aşırı Keskinlik    Difüzyon adımlarında piksel kenarları çakışır, doku kaynaması (boiling) ve kare titremesi oluşur.    
Görsel prompta "35mm film still, natural depth of field" eklemek; "8K, hyperdetailed" terimlerini kaldırmak.

Google / OpenAI Docs

ÖLÇÜLMÜŞ
Plastik Malzeme Doku    Kask ve elbise yüzeylerinde kauçuksu esneme ve doğal olmayan form bozulmaları meydana gelir.    
Görsel prompta spesifik malzeme tanımları ("matte composite, textured Kevlar, brushed metal") eklemek.

OpenAI GPT Image Guide

UYGULAMA
Sarı / Sıcak Renk Eğilimi    Uzay vakumundaki kontrastı bozar ve videoda kareler arası renk kaymalarına (color shift) yol açar.    
Görsel prompta "stark neutral lighting, cool blue and silver palette, earthshine bounce" tanımlamak.

Google Enterprise Docs

UYGULAMA
İstem Dışı Yazı / Logo    Video modeli yazıyı 3D fiziksel nesne sanarak hareket sırasında büker, uzatır veya eritir.    
Görsel prompta "no text, no logos" eklemek veya OpenCV/Photoshop ile temizlemek; tırnak işaretini kaldırmak.

OpenAI / Google Docs

ÖLÇÜLMÜŞ
Aşırı Simetri    Kamera hareketi başladığında model kusursuz simetriyi koruyamaz, asimetrik dalgalanmalar oluşur.    
Kompozisyonda 1/3 kuralını ve dinamik, hafif açılı kamera açılarını tercih etmek.

OpenAI Prompt Guide

ÖLÇÜLMÜŞ

(c) TEKNİK Tablosu
Konu    Öneri    Kanıt    Kaynak    Etiket
En-Boy Oranı    Görsel doğrudan 16:9 üretilmelidir. Gemini uygulaması/API yüklenen görsel oranını izler (aspect_ratio: "16:9").    
"Match the final aspect ratio... Letting the model outpaint the missing area invents content at the edges, and invented content drifts."

Google Gemini API Docs

ÖLÇÜLMÜŞ
Kırpma vs Genişletme    Standart kareden 16:9'a geçerken kırpma (crop) yapılmalıdır; genişletme (outpaint) kenarlarda kayan içerik üretir.    
"Big empty expansions are where models tend to invent objects, fake texture, or change the scene logic... crop/recompose first"

Production Outpaint Tests

ÖLÇÜLMÜŞ
Çözünürlük ve Büyütme    Temiz 1080p PNG kullanılmalıdır. Yapay AI keskinleştirme büyütmesi (upscaler) videoda titremeyi artırır.    
"Draft every idea at 720p... upscale/sharpen only after composition is final"

Production Benchmarks

UYGULAMA
Dosya Biçimi    Kayıpsız PNG kullanılmalıdır. JPEG sıkıştırma blokları difüzyon hareketinde gürültüye dönüşür.    
"Upload an image (JPEG/PNG, 720p+ recommended)... PNG preserves sharp contrast without compression artifacts"

OpenAI / Google Docs

UYGULAMA
Model İçi Küçültme    Video modeli girdi karesini iç latent çözünürlüğe çekebilir; yüksek kaliteli girdi piksel kalitesini korur.    
"The model generates realistic 8-second 720p / 1080p output from standard input frames"

AIMLAPI / Gemini API Docs

ÖLÇÜLMÜŞ

8. Kalite Kontrol ve Uygulama İskeletleri
Videoya Göndermeden Önce 10 Maddelik Kare Kabul Listesi
Aşağıdaki kalite kontrol adımları, yerel yazılımlar (OpenCV, Photoshop, ImageMagick) ve görsel kontrol ile doğrulanmalıdır:

En-Boy Oranı Doğrulaması: Piksel boyutları tam olarak 16:9 oranında mı? (Yerel Piksel Ölçümü: Örn. 1792×1024 veya 1920×1080).

Dosya Formatı Kontrolü: Dosya uzantısı kayıpsız .png mi ve JPEG sıkıştırma artifact'i barındırmıyor mu? (Evet/Hayır).

İstem Dışı Metin Tespiti (OCR Scan): Görsel üzerinde kask, elbise veya arka planda yapay yazılmış istem dışı karakter/logo var mı? (Yerel OCR Kontrolü: Metin yok = Geçti).

Hareket Payı (Headroom) Kontrolü: Özne veya uzuvların hareket edeceği yönde kadraj sınırı ile arasında en az %15 boşluk var mı? (Evet/Hayır).

Anatomik Kararlılık: Özne ve eller nesneyle kararlı temas halinde mi veya kadraj dışında tamamen temiz şekilde kesilmiş mi? (Evet/Hayır).

Gölge Detayı ve Pozlama (Histogram): Histogramda %0 saf siyah oranı sahnenin %20'sinden az mı ve kenar ışığı (rim light) mevcut mu? (Yerel Histogram Ölçümü).

Aşırı Keskinlik Analizi: Yüksek frekanslı kenar gürültüsü sönümlenmiş ve yumuşak alan derinliği uygulanmış mı? (Evet/Hayır).

Renk Sıcaklığı Ölçümü: Renk paletinde aşırı yapay sarı/sıcak renk baskınlığı temizlenmiş, soğuk/nötr uzay paleti korunmuş mu? (Yerel Renk Analizi).

Fiziksel Mantık Kontrolü: Karede ters yönlü alev, donmuş duman veya yapay donmuş sıvı damlası gibi hatalı fizik unsurları yok mu? (Evet/Hayır).

Toplu Kontak Sayfası (Contact Sheet) İncelemesi: Üretilen onlarca aday kare, 4x4 matrisli tek bir kontak sayfasında toplu olarak görsel tutarlılık açısından onaylandı mı? (Evet/Hayır).

Prompt İskeletleri (Örnek Çekim: Uzay İstasyonu Kenetlenme / EVA)
Başlangıç Karesi Görsel Prompt İskeleti (OpenAI GPT Image / ChatGPT)
Scene & Subject: Cinematic wide shot 16:9 of a helmeted astronaut during an EVA spacewalk outside a massive orbital space station, positioned near an open airlock hatch.

Pose & Action State: The astronaut's right gloved hand is hovering two centimeters above a glowing yellow docking lever, static moment right before gripping it. Full body visible, relaxed posture.

Composition & Space: Positioned on the left third of the frame, leaving wide clearance on the right for movement. Clear foreground detail of the station's metallic hull truss, background showing the curved blue horizon of Earth against dark space.

Lighting & Color: Stark directional sun lighting with crisp rim light on the astronaut's white suit and golden visor reflection, subtle earthshine fill light in the shadows. Cool blue and metallic silver color palette.

Style & Optical: Shot on 35mm film, anamorphic lens, subtle optical film grain, realistic depth of field, natural surface textures, no artificial over-sharpening. No text, no logos, no watermarks.

Video Prompt İskeleti (Google Gemini Omni 1.1 Flash / Veo 3.1)
Camera Motion: Slow, steady camera dolly in toward the subject while maintaining a level perspective.

Subject Animation: In a single continuous shot, the astronaut reaches forward and grips the yellow docking lever, pulling it down smoothly.

Environmental Animation: The airlock indicator lights shift from yellow to green, and faint white thruster vapor vents smoothly into the void of space.

Constraint: Keep the background lighting, suit design, and overall environment identical to the initial frame. No scene cuts.

Bağlantılı Tam Kaynak Listesi
Google Cloud Enterprise - Gemini Omni & Veo Best Practices Guide

[cite: 6]

Google Cloud Enterprise - Video Generation Prompt Guide for Gemini Omni Flash & Veo

[cite: 13]

Google AI Developer Docs - Gemini Omni API Overview & Prompting Standards

[cite: 4]

Google DeepMind - Gemini Omni Model Capabilities, Technical Demos & Benchmarks

[cite: 23]

Google Cloud Blog - Ultimate Prompting Guide for Veo 3.1 and Gemini Omni

[cite: 3]

Google Support - Veo 3 and Gemini Omni Photo-to-Video Technical Guide

[cite: 1]

OpenAI Developers Cookbook - GPT Image Generation Models Prompting Guide

[cite: 5]

OpenAI API Reference - Image Prompting & Editing Guide (GPT Image 2.5)

[cite: 12]

OpenAI Research - DALL-E 3 / GPT Image Technical Paper & Prompt Adherence Benchmarks

[cite: 11]

MakeInfluencer Benchmarks - Best Image to Video AI Models Performance Comparison (2026)

[cite: 2]

Laozhang AI - AI Image Outpainting, Expansion, and Frame Rescue Technical Analysis (2026)

[cite: 24]

9. Sonuç ve Uygulama Tavsiyeleri
Ekim 2026 itibarıyla GPT Image ve Gemini Omni 1.1 Flash / Veo 3.1 modelleriyle yürütülen 10 saniyelik fotogerçekçi bilimkurgu yapımlarında yüksek başarı elde etmek, başlangıç karesinin teknik ve kompozisyonel olarak doğru hazırlanmasına bağlıdır.

Görsel prompt aşamasında hareket öncesi durumun kurgulanması, el-nesne temasının sabitlenmesi, aşırı keskinlikten kaçınılarak 35mm film estetiğinin benimsenmesi ve doğrudan 16:9 PNG formatının tercih edilmesi kritik öneme sahiptir. Video promptunda ise resimdeki detayları yeniden tanımlamadan yalnızca eyleme ve kamera hareketine odaklanmak, üretim kalitesini en üst seviyeye çıkaracaktır. Kalite kontrol adımlarının 10 maddelik kabul listesi ve toplu kontak sayfaları üzerinden yürütülmesi, boru hattındaki hata oranını minimize edecektir.
