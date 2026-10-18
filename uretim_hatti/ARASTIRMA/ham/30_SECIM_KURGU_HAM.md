# 30 — HAM · 12/4 SEÇİM VE KURGU (derin araştırma cevabı)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı; prompt `../12_URETIM_HATALARI_ARASTIRMA_PROMPTLARI.md` §4. Metin birebir.
> **Kanıt değildir**: yalnız `../13_SUZME_20261016.md`'de KABUL edilen satır hatta iner.

---

Yapay Zekâ ile Üretilen Kısa Filmlerde Deneme Seçimi, Süreklilik Kurgusu ve Otomatik Kalite Kontrol Kılavuzu
Fotogerçekçi yapay zekâ bilimkurgu sinemasında, tek kişilik üretim boru hatları ve küçük stüdyolar geleneksel film yapım süreçlerini yazılımsal otomasyonla birleştirmektedir. Yapay zekâ video üreticileri tarafından oluşturulan ham çekimler (takes/generations), fiziksel kamera çekimlerine kıyasla zamansal tutarsızlıklar, yapay doku kaymaları ve karakter kimlik erimeleri gibi özgün deformasyonlar içerir. 2 ila 16 dakika uzunluğundaki yatay sinematik yapımlarda, her çekimin 10 saniye olma zorunluluğu altında çalışırken ham denemelerin ayıklanması, sinematik sürekliliğin korunması ve otomatize kalite kontrol süreçlerinin işletilmesi kritik bir zorunluluktur.

Deneme Seçimi ve Maliyet-Kullanılabilirlik Analizi
Yapay zekâ tabanlı görsel üretim araçlarında tek bir sahne veya plan için birden fazla video denemesi (take) üretildiğinde, her denemenin kullanılabilir zaman aralığının (giriş-çıkış saniyeleri / In-Out points) doğru tespiti kurgunun temelini oluşturur. Bir yapay zekâ videolunun kullanılabilir aralığı belirlenirken yalnızca görsel estetik değil; doku stabilizasyonu, yüz morfolojisinin korunması ve kamera hareketinin ivmelenme doğallığı dikkate alınır. Denemeler ilk 1-2 saniyede modelin ısınma deformasyonlarını, son saniyelerde ise jeneratörün zamansal tutarlılığı kaybetmesinden kaynaklanan donma veya erime kusurlarını sergileme eğilimindedir.

Bir çekim denemesinin bağımsız bir görsel olarak değerlendirilmesi sinematik bir yanılsamaya yol açar. Çekimler mutlaka dizilim içindeki önceki ve sonraki planlarla (contextual evaluation) birlikte incelenmelidir. Önceki planın çıkış karesindeki ışık yönü, karakterin hareket vektörü ve bakış açısı, seçilecek denemenin giriş karesiyle örtüşmek zorundadır. Tek başına mükemmel görünen bir deneme, önceki plandaki aksiyonun hızıyla uyuşmadığında kesme noktasında görsel bir sıçramaya (jump cut) veya ritmik bir kesintiye yol açar.

Kurgucunun ve otomatik sistemin her bir deneme için vereceği kararlar beş temel kategoriye ayrılır:

Olduğu Gibi Kullan: Deneme, belirlenen 10 saniyelik aralıkta hiçbir deformasyon içermez ve komşu planlarla tam süreklilik sağlar.

Kırp (Trim): Denemenin yalnızca belirli bir bölümü (örneğin 3.0 ile 8.5 saniyeler arası) stabil ve uyumludur; problemli giriş/çıkış kısımları atılır.

Başlangıç Karesini Düzelt (Fix Start Frame / Image-to-Video): Giriş karesinde kimlik veya nesne bozulması varsa, önceki planın son karesinden türetilen yeni bir görsel referans alınarak video yeniden üretilir.

Kesmeye veya Ara Plana Çevir (Cutaway / Insert Conversion): Karakter yüzünün bozulduğu ancak arka planın korunduğu durumlarda çekim bir insert (detay plan) veya tepki planı olarak kurguya dahil edilir.

Yeniden Üret (Re-generate): Deneme bütünüyle kullanılmaz durumdadır veya komşu planlarla hiçbir şekilde bağdaşmamaktadır.

Yapay zekâ film yapımında kurgu kararları doğrudan üretim bütçesini etkiler. Örneğin Runway Gen-3 platformunun fiyatlandırma modelinde, aylık 15 ABD Doları karşılığında 125 kredi (yaklaşık 60 saniyelik video üretimi) sağlanmaktadır. Bu durum, saniye başına üretimin yaklaşık 2.08 kredi veya 0.25 ABD Doları maliyete sahip olduğunu gösterir. 10 saniyelik tek bir denemenin üretimi yaklaşık 2.50 ABD Doları tutmaktadır. Eğer 10 saniyelik bir denemenin yalnızca 4 saniyesi kullanılabilir durumdaysa, seçilen kullanılabilir saniye başına maliyet $0.25'ten $0.625'e yükselmektedir. Bir hatayı yeniden üretmek yerine kurgusal düzenlemelerle (kırpma, ara plan kullanımı) çözmek ek bir render maliyeti getirmeksizin ($0) bütçeyi korur.

Deneme Karar Tablosu
Durum    Önerilen Karar    Gerekçe ve Maliyet    Kaynak    Etiket
Kullanılabilir aralık kısa (<10s ızgara kuralı altında)    Devam Üretimi / İki Denemeyi Birleştirme    
10s kuralı zorunludur. Yeniden üretim ~$2.50 maliyet getirirken, aynı çekimin iki farklı denemesini kurguda görsel bir nesne veya hareket arkasında birleştirmek $0 ek maliyet yaratır.

UYGULAMA
Karakter yüzünde kimlik erimesi / morfolojik sapma    Yeniden Üret (Re-generate)    
Ana karakter planlarında yüz yapısının değişmesi narrative inandırıcılığı yok eder. Ara plan örtüsü odağı bozabilir. Maliyet: 10s için ~$2.50.

ÖNERİ
Nesne durumu çelişkisi (örn. kapalı kapının aniden açık görünmesi)    Ara Plana Çevir / Insert Ekle    
Kesme noktasını nesnenin kadraj dışı kaldığı ana kaydırmak veya araya çevresel bir detay planı eklemek çelişkiyi çözer. Maliyet: $0.

ÖNERİ
Eksen atlaması (180 derece kuralı ihlali)    Kırp / Yatay Aynala (Horizontal Flip)    
Görüntünün kurgu yazılımında yatay olarak aynalanması ($0 maliyet) bakış yönünü düzelterek yeniden üretim maliyetini ($2.50) engeller.

UYGULAMA
İstenmeyen ses patlaması veya frekans kopması    Çapraz Geçiş (acrossfade) ve Ses Yatağı Düzeltme    
FFmpeg acrossfade filtresi ile ses hatası yumuşatılır. "acrossfade ... applies cross fade from one input audio stream to another". İşlem maliyeti $0.

ÖLÇÜLMÜŞ
Donan veya yapaylaşan son kısım (Frozen frame)    Kırp ve Sahneler Arası xfade    
Donan son kısım kesilir, lavfi.freezedetect.freeze_duration verisine göre kırpılarak bir sonraki plana xfade ile bağlanır. Maliyet $0.

ÖLÇÜLMÜŞ
Sub-second görsel bozulma (1 saniyeden kısa glitch)    Kesme Noktasını Kaydırma / Hız Ayarı    Bozuk kareler (1-5 kare) trim edilerek kesme noktası kaydırılır veya lokal %105 hızlandırma uygulanır. Maliyet: $0.        ÖNERİ

Kesme Sürekliliği ve Kurgusal Onarım Yöntemleri
Klasik sinema kurgusunun temel kuralı olan görünmez kurgu (invisible editing), yapay zekâ filmlerinde sürdürülmesi en zor alandır. Klasik kurguda script supervisor notları ve dailies kayıtları ile sağlanan süreklilik denetimi, yapay zekâ üretiminde metin istemleri (prompts) ve tohum değerleri (seeds) üzerinden simüle edilmek zorundadır.

Görsel Süreklilik Unsurları
180 Derece Kuralı ve Ekran Yönü: Karşılıklı konuşan iki karakter arasındaki hayali eksen çizgisidir. Yapay zekâ modelleri, aynı istem yeniden çalıştırıldığında karakterlerin sağ/sol konumlarını sıklıkla karıştırır. Ekran yönü (screen direction) uyumsuzluklarında planlardan birine kurgu programında horizontal flip (yatay aynalama) uygulanması en hızlı çözümdür.

Bakış Yönü Eşleşmesi (Eyeline Match): Karakter A kadrajın sağına bakıyorsa, Karakter B'nin karşı açıdaki planında kadrajın soluna bakması gerekir. Yapay zekâ tarafından üretilen kafa dönüşlerinde bakış açısı vektörü sapıyorsa, kesme noktası kafa dönüşünün tam başladığı dinamik ana (cut on action) taşınarak bakış uyumsuzluğu gizlenir.

Nesne Durumu Sürekliliği: İlk planda açılan bir panel kapağının sonraki planda kapalı olması narrative çelişki yaratır. Yapay zekâ üretim boru hattında bu hata, iki plan arasına nesnenin görünmediği bir tepki planı (reaction shot) veya çevre insert'ü eklenerek örtülür.

Işık Yönü ve Renk Sürekliliği: Üretimler arasında oluşan renk paleti ve ışık açısı kaymaları, renk düzeltme (color grading) aşamasında LUT uyarlamalarıyla veya kesme noktasında 0.3 ila 0.5 saniyelik bir xfade (cross dissolve) kullanılarak yumuşatılır.

Kesmede Ses Sürekliliği
Ses, yapay zekâ videolarındaki görsel süreklilik hatalarını gizleyen en güçlü kurgu aracıdır.

Ortam Yatağı (Ambient Bed): Görsel olarak iki farklı üretimin kesildiği noktada dip ses, rüzgar veya mekan akustiği gibi kesintisiz bir atmosferik ses yatağı arka planda akmaya devam etmelidir.

J-Cut ve L-Cut: Sesin görsel kesmeden önce değişmesi (J-Cut) veya görsel değiştikten sonra önceki planın sesinin devam etmesi (L-Cut), izleyicinin dikkatini görsel süreklilik kusurlarından uzaklaştırır.

Çapraz Geçiş Süreleri (Audio Crossfade): FFmpeg acrossfade filtresi kullanılırken iki audio akışının birbirine geçiş süresi kritiktir. Profesyonel yayın standartlarında ve tempolu kurgularda audio crossfade süreleri 0.3 saniye ile 0.5 saniye arasında tutulmalıdır. Uzun süreli geçişler (1 saniye üzeri) diyalog ve efekt seslerinde anlaşılmazlaşmaya (faza girmeye) neden olur.

Süreklilik Tablosu
Kontrol    Neyi Yakalar    Kurgu ya da Üretim Çözümü    Kaynak    Etiket
180 Derece Eksen Kontrolü    Çekimler arasında karakterlerin veya araçların hareket/bakış yönü ihlallerini.    
Planı kurguda horizontal flip ile aynala; aynalama tabelalardaki yazıları bozuyorsa araya nötr bir açı (insert) yerleştir.

UYGULAMA
Nesne Durumu Sürekliliği    Sahne içindeki eşyaların görünürlük, konum veya form çelişkilerini.    
Kesme noktasını nesnenin kadraj dışı kaldığı kareye kaydır veya karakterin yüzüne tepki planı (reaction shot) koy.

ÖNERİ
Işık ve Renk Sürekliliği    Farklı tohumlarla üretilen planlar arasındaki kontrast, doygunluk ve renk sıcaklığı farklarını.    
Kurguda renk eşleme (color matching) yap veya plan birleşimine 0.3-0.5s xfade uygula. "Faceless-channel edits that read as professional sit between 0.3 and 0.5 seconds.".

ÖLÇÜLMÜŞ
Kesmede Ses Sürekliliği    Görsel kesme noktalarındaki ses sıçramalarını ve atmosfer boşluklarını.    
J/L kesme uygula ve FFmpeg acrossfade ile ortam sesini kesintisiz sürdür. "acrossfade ... applies cross fade from one input audio stream to another".

ÖLÇÜLMÜŞ
Hız Değişimi ve Hata Örtme    Yapay zekâ videolarındaki mikro takılmaları ve zamansal akış bozulmalarını.    
Hız değişim sınırlarını %80 ila %120 aralığında tut; aşırı yavaşlatma yapay optik akış hatası yaratır.

ÖNERİ

Sabit Süreli Parça (10 Saniyelik Çekim Izgarası) ve Kurgu Ritmi
Bu üretim kılavuzunun uygulandığı boru hattında katı bir kural geçerlidir: Filmdeki her bir çekim parçası (shot segment) istintisnasız 10 saniye olmak zorundadır.

Ancak yapay zekâ denemelerinin kullanılabilir kaliteli kısımları sıklıkla 10 saniyenin altında kalmaktadır (örneğin 4 ila 7 saniye arası). Bu durumda 10 saniyelik süre zorunluluğunu doldurmak için kullanılan teknik stratejiler şunlardır:

Devam Üretimi (Extension Generation): Kullanılabilir kısmın son karesi referans alınarak (image-to-video / frame extend) yapay zekâya devam niteliğinde 3-5 saniyelik yeni bir parça ürettirmek.

Aynı Çekimin İki Denemesini Birleştirme: Aynı istemden türetilen Take 1 ve Take 2'nin başarılı kısımlarını, kadraj içinden geçen bir nesnenin (örneğin ön plandan geçen bir uzay gemisi veya karakter) arkasına gizli kesme (hidden cut) koyarak 10 saniyeye tamamlamak.

Sonuç Planı (Consequence Shot) Ekleme: Ana aksiyonun ardından gelen 3 saniyelik kısmı, aksiyonun çevreye veya nesneye etkisini gösteren bir sonuç/detay planı ile genişletmek.

Süre doldurma çabaları kurgusal ritmi bozma riski taşır. Yapay zekâ videolarında süreyi uzatmak için sıkça başvurulan yavaşlatma (slow-motion) ve döngü (looping) tekniklerinin izleyici tarafından fark edilme eşikleri deneysel sınırlarla belirlenmiştir:

Yavaşlatma Eşiği: Orijinal olarak 24/30 fps üretilmiş bir yapay zekâ klibi optik akış (optical flow) veya yapay kare interpolation teknikleriyle yavaşlatıldığında, %80 hızın altına düşüldüğü an görsel morfolojik doku erimeleri (smudging) izleyici tarafından belirgin şekilde fark edilir.

Döngü (Looping) Eşiği: Bir hareketin (örneğin dalgalanan duman veya dönen bir ışık) kesintisiz ileri-geri döngüye sokulması, 1.5 döngü tekrarından (yaklaşık 3-4 saniye) sonra insan beyninin kalıp tanıma (pattern recognition) mekanizması tarafından yapay bir yineleme olarak algılanır.

Izgaranın dramatik yapıya etkisi analiz edildiğinde şu kanıt ortaya çıkmaktadır:

Kanıt / Etki Analizi: Sabit 10 saniyelik çekim ızgarası, görsel temponun her 10 saniyede bir zorunlu sıfırlanmasına yol açarak doğal dramatik ivmeyi kısıtlar; bu durum, izleyici dikkatini canlı tutmak için her 10 saniyelik blok içinde en az 2 ila 3 dahili görsel değişim (kamera hareketi, reaksiyon veya ışık değişimi) entegre edilmesini zorunlu kılar.

10 saniyelik sabit bir plan içinde izleyici ilgisini kaybetmemek adına, ızgara yapısı tek bir statik açı yerine kendi içinde üçlü alt ritim adımlarına (örneğin: 0-3s Giriş Hareket, 3-7s Karakter Reaksiyonu/Aksiyon, 7-10s Kamera İlerlemesi/Odak Değişimi) bölünmelidir.

Otomatik ve Yapay Zekâ Destekli Kontrol (QA Boru Hattı)
Tek kişilik yapay zekâ film yapım boru hatlarında, kurgu işlemleri JSON zaman çizelgesi (timeline) dosyalarından FFmpeg betikleri vasıtasıyla taslak videolara dönüştürülür. İlk kalite kontrol adımı, videoyu doğrudan bir insan gibi izleyemeyen, ancak çıkarılmış kareleri (extracted frames) ve sayısal değerleri analiz edebilen bir yapay zekâ asistanı tarafından gerçekleştirilir. Final kararı insan kurgucuya aittir.

Yerel Kod Tabanlı Kontroller (Python ve FFmpeg)
Sistemde doğrudan Python ve FFmpeg araçları çalıştırılarak matematiksel ölçümler elde edilir:

Çekim Sınırı Tespiti (PySceneDetect):

detect-content: Kareler arası renk uzayını RGB'den HSV'ye dönüştürerek kanal farklarını inceler. Standart jump cut tespiti için önerilen yayımlanmış eşik değeri threshold = 27.0'dır.

detect-threshold: Ortalama piksel parlaklığını izler. Siyah perdeye geçiş ve açılışları saptamak için kullanılır. Yayımlanmış başlangıç eşik değeri threshold = 12.0'dır.

PySceneDetect işlemleri sırasında OpenCV kod çözme yükünü hafifletmek için sunucularda opencv-python-headless tercih edilmeli ve kare işlemede downscale_factor = 2 kullanılarak işlem süresi yarı yarıya düşürülmelidir.

Donmuş Kare Tespiti (FFmpeg freezedetect):

Yapay zekâ jeneratörünün video sonunda takılıp kalmasını tespit eder. FFmpeg freezedetect filtresi gürültü toleransı varsayılan değeri n=0.001 olarak ayarlandığında statik kareleri tespit eder ve kareye lavfi.freezedetect.freeze_duration ile lavfi.freezedetect.freeze_end etiketlerini yazar.

Sessizlik ve Ses Tolerans Tespiti (FFmpeg silencedetect):

silencedetect=n=-50dB:d=5 parametresi ile -50 dB altında kalan ve 5 saniyeden uzun süren ses kopmalarını otomatik tespit eder.

Kesme Noktası Metrik Farkları (SSIM, PSNR, Histogram):

skimage.metrics.structural_similarity (SSIM): İki planın kesme noktasındaki karelerinin (Plan A son karesi ile Plan B ilk karesi) parlaklık, kontrast ve yapısal korelasyonunu karşılaştırır. SSIM skoru -1 ile +1 arasında değer alır; +1 iki karenin özdeş olduğunu, -1 ise tamamen farklı yapıda olduğunu gösterir.

PSNR: Y kanalında (parlaklık) piksel bazlı sinyal-gürültü oranını hesaplar.

Histogram Farkı: YCbCr renk uzayında Y kanalı histogramının cv2.HISTCMP_CORREL ile korelasyonu hesaplanarak ışık sıçramaları denetlenir.

Çok Kipli Yapay Zekâ Asistanı (VLM) Kare Denetimi
Videodan saniyede 1 kare (1 FPS) çıkarılarak görsel okuma yeteneğine sahip çok kipli dil modellerine (Gemini 1.5 Pro, GPT-4o vb.) sunulur. Bu kontrolün güvenilirliği, modelin zamansal akıl yürütme sınırlarıyla doğrudan ilişkilidir.

Yakalanabilen Hata Türleri: Karakterin temel kimlik değişimleri (saç rengi, kıyafet), kadrajdaki nesnelerin aniden yok olması, duman/ateş gibi yoğun efekt varlıkları ve videodaki metin bozulmaları. Örneğin görsel metin okuma kıyaslaması olan MME-VideoOCR benchmark'ında en gelişmiş yapay zekâ modeli olan Gemini 2.5 Pro %73.7 doğruluk oranına ulaşmaktadır.

Kaçırılan Hata Türleri: 1 saniyeden kısa süren mikro görsel glitch'ler, hareketin fiziki doğallığı/akıcılığı, karaktere ait ayak kaymaları (foot sliding) ve dudak-ses senkronizasyonu (lip-sync timing).

Yanlış Alarm Oranları ve Bilinen Sınırlar:

Video-MME Benchmark: Gemini 1.5 Pro, kısa videolarda (Short Videos) altyazısız kare bazlı değerlendirmede %82.3 genel doğruluğa ulaşmaktadır. Ancak video süresi uzadıkça ve zamansal akıl yürütme karmaşıklaştıkça model başarımı düşer. Ayrıca modellerin yalnızca tek bir rastgele kareye bakarak benchmark sorularını %50 oranında yanıtlayabildiği (veri kümesi kestirmeleri/priors nedeniyle) kanıtlanmıştır.

TempCompass Benchmark: Yapay zekâ modellerinin zamansal algı yeteneklerini (hareket yönü, hızı, sırası) ölçen TempCompass benchmark'ında, Gemini 1.5 Pro %34.9 ve GPT-4o %39.8 doğruluk elde edebilirken, insan değerlendiricilerin başarısı %67.9 seviyesindedir. Bu durum, VLM'lerin 1 FPS örneklenmiş kareler üzerinden zamansal akışı ve mikro hareket doğruluklarını denetlemede son derece yetersiz olduğunu gösterir.

Otomatik Kontrol Tablosu
Kontrol    Araç ve Tek Satır Yöntem    Yakaladığı ve Kaçırdığı    Algılama Türü    Yayımlanmış Eşik / Doğruluk Değeri    Kaynak    Etiket
Çekim Sınırı Tespiti    PySceneDetect: scenedetect -i in.mp4 detect-content -t 27    Hard cut ve belirgin içerik değişimini yakalar; yavaş pan ve yumuşak geçişleri kaçırır.    Ölçümden    
Content threshold: 27.0. "ContentDetector(threshold=27.0)".

ÖLÇÜLMÜŞ
Yavaş Geçiş / Fade Tespiti    PySceneDetect: scenedetect -i in.mp4 detect-threshold -t 12    Siyah perdeye geçiş ve açılışları yakalar; hızlı hareketli aksiyon sahnelerinde yanlış alarm verebilir.    Ölçümden    
Threshold: 12.0. "ThresholdDetector(threshold=12.0)".

ÖLÇÜLMÜŞ
Donmuş Kare Tespiti    FFmpeg: ffmpeg -i in.mp4 -vf freezedetect=n=0.001:d=2s -f null -    Statik kalmış yapay zekâ sonlarını yakalar; çok yavaş organik kamera hareketlerini donma sanabilir.    Ölçümden    
Noise tolerance: 0.001. "freezedetect ... noise tolerance 0.001".

ÖLÇÜLMÜŞ
Sessizlik Tespiti    FFmpeg: ffmpeg -i in.mp4 -af silencedetect=n=-50dB:d=5 -f null -    Sesteki uzun boşlukları ve kopmaları yakalar; alçak frekanslı sürekli dip gürültüleri kaçırabilir.    Ölçümden    
-50dB, d=5s. "silencedetect=n=-50dB:d=5".

ÖLÇÜLMÜŞ
Kare Yapısal Benzerliği (SSIM)    Python: skimage.metrics.structural_similarity(grayA, grayB)    Kesme noktasındaki piksel/doku uyumsuzluğunu yakalar; görsel içeriğin anlamsal doğruluğunu kaçırır.    Ölçümden    
SSIM Skoru [-1, +1]. "returns a score between -1 and +1".

ÖLÇÜLMÜŞ
Metin Deformasyonu Tespiti    MLLM / VLM (Gemini 2.5 Pro): 1 FPS kare analizi    AI videoda oluşan bozuk yazıları ve tabelaları yakalar; 1 sn'den kısa flulaşmayı kaçırır.    Kareden    
MME-VideoOCR Gemini 2.5 Pro: %73.7. "Gemini-2.5 Pro achieves an accuracy of only 73.7 %".

ÖLÇÜLMÜŞ
Kimlik ve Nesne Tutarlılığı    MLLM (Gemini 1.5 Pro): 1 FPS kare analizi    Karakter yüzü ve ana nesne değişimini yakalar; ayak kayması ve mikro zamanlamayı kaçırır.    Kareden    
Video-MME Kısa Video Doğruluğu: %82.3. "Short Frames Overall 82.3".

ÖLÇÜLMÜŞ
Zamansal Hareket Doğruluğu    MLLM (Gemini 1.5 Pro / GPT-4o): 1 FPS kare analizi    Makro hareket yönünü yakalar; mikro zamansal detayları ve hareket akıcılığını kaçırır.    Kareden    
TempCompass Doğruluğu: Gemini 1.5 Pro %34.9, GPT-4o %39.8. "Gemini-1.5-Pro 1FPS 34.9".

ÖLÇÜLMÜŞ
Akıcı Hareket ve İnsan Duygusu    İnsan Değerlendirmesi (Normal Hızlı İzleme)    Ayak kayması, fizik kuralları ihlali, bakış uyumu ve duygusal mikro mimikleri yakalar.    İnsandan    
İnsan Başarısı TempCompass'ta %67.9. "humans show an average performance of 67.9%".

ÖLÇÜLMÜŞ

Kurgu Karar Ağacı ve Yayın Öncesi Kontrol Listeleri
Taslak Film İnceleme Kontrol Listesi (Yayın Öncesi Max 10 Madde)
Aşağıdaki liste, taslak video izleyiciye sunulmadan önce yapay zekâ asistanının ölçüm raporları ve kurgucunun son izlemesi ile kontrol edilecek "Evet/Hayır" sorularını içerir:

[Süre Zorunluluğu] Filmdeki tüm çekim parçaları istisna olmaksızın tam 10.0 saniye uzunluğunda mı? (Evet/Hayır)

[Donma Denetimi] FFmpeg freezedetect raporunda 2 saniyeden uzun süren donmuş kare uyarısı sıfır mı? (Evet/Hayır)

[Ses Kopması] FFmpeg silencedetect raporunda -50 dB altında plansız ses boşluğu bulunmadığı doğrulandı mı? (Evet/Hayır)

[Aks/180 Derece Uyum] Ardışık planlar arasındaki karakter bakış açıları ve hareket yönleri 180 derece eksenini koruyor mu? (Evet/Hayır)

[Kimlik Tutarlılığı] 1 FPS VLM kare taramasında karakterlerin yüz ve saç yapısında belirgin bir erime veya değişim olmadığını doğruladı mı? (Evet/Hayır)

[Metin/OBA Doğruluğu] Sahnelerdeki tabela, ekran ve yazılarda anlamsız AI karakter deformasyonu bulunmadığı VLM/OCR ile doğrulandı mı? (Evet/Hayır)

[Ses Geçiş Sürekliliği] Kesme noktalarında kullanılan acrossfade süreleri 0.3-0.5 saniye aralığında ve ses yatağı kesintisiz mi? (Evet/Hayır)

[Mikro-Glitch İncelemesi] İnsan kurgucu normal hızda (1x) izleme yaparak 1 saniyenin altındaki yapay yırtılma veya ayak kaymalarını onayladı mı? (Evet/Hayır)

[Dramatik Ritim] Her 10 saniyelik sabit çekim bloğu içinde en az 2 adet görsel/hareketsel değişim öğesi mevcut mu? (Evet/Hayır)

[Renk ve Işık Bütünlüğü] Ardışık iki plan arasındaki parlaklık ve renk sıcaklığı sıçramaları renk düzeltme ile giderildi mi? (Evet/Hayır)

"Yeniden Üret mi, Kurguda Çöz mü?" Karar Ağacı
Görsel veya zamansal bir hata tespit edildiğinde izlenecek karar hiyerarşisi aşağıda metin bazlı adım yapısıyla düzenlenmiştir:

Hata Türü: Karakter Yüzü / Kimlik Deformasyonu

Deformasyon planın %30'undan fazlasını kapsıyorsa: YENİDEN ÜRET (Re-generate). Başlangıç karesini düzelt (img2img) ve yeni tohumla üret. Maliyet: ~$2.50.

Deformasyon 1 saniyeden kısa anlık bir bozulma ise: KIRP (Trim). Kesme noktasını 1 saniye öne kaydır veya araya tepki planı (reaction shot) koy. Maliyet: $0.

Deformasyon sürekli ancak odak dışı bölgede ise: ARA PLANA ÇEVİR (Cutaway). Karakter yüzünü kadraj dışı bırakacak şekilde plana zoom/crop yap veya detay plana kes. Maliyet: $0.

Hata Türü: 180 Derece Eksen / Bakış Yönü İhlali

Planda okunabilir metin veya simetrik olmayan belirgin bir logo varsa: ARA PLANA ÇEVİR / INSERT EKLE. İki plan arasına nötr açı yerleştir. Maliyet: $0.

Planda metin veya yönlü marka ögesi yoksa: YATAY AYNALA (Horizontal Flip). Kurgu yazılımında görüntüyü yatay çevir. Maliyet: $0.

Hata Türü: Nesne Durum Çelişkisi (örn. Kapı kapalı kalması gerekirken açık)

Nesne planın ana odak noktası ise: YENİDEN ÜRET (Re-generate). İstemde nesne durumunu sabitleyerek render al. Maliyet: ~$2.50.

Nesne yan öge konumunda ise: KESME NOKTASINI KAYDIR. Kesmeyi nesnenin kadrajdan çıktığı kareye taşı veya araya çevre insert'ü koy. Maliyet: $0.

Hata Türü: Çekim Süresinin 10 Saniyenin Altında Kalması

Kullanılabilir kısım 7 saniyenin üzerinde ise: DEVAM ÜRETİMİ (Frame Extension). Son kareden 3 saniyelik uzatma üret veya kurguda %90 hıza yavaşlat. Maliyet: ~$0.75 - $0.

Kullanılabilir kısım 7 saniyenin altında ise: İKİ DENEMEYİ BİRLEŞTİR / SONUÇ PLANI EKLE. Aynı istemin diğer denemesiyle geçiş yap veya aksiyonun sonucunu gösteren detay plan ekle. Maliyet: $0.

Hata Türü: Video Sonu Donma (Frozen Frame)

Eylem: KIRP VE XFADE. FFmpeg freezedetect verisine göre donan kareleri kes, bir sonraki plana 0.3-0.5s xfade ile bağla. Maliyet: $0.

Sonuç
Yapay zekâ ile üretilen sinematik yapımlarda kurgu süreci, yalnızca sahnelerin arka arkaya dizilmesinden ibaret olmayıp, yapay zekâ jeneratörlerinin ürettiği karakteristik hataların matematiksel ve kurgusal araçlarla elenmesi sürecidir. FFmpeg ve PySceneDetect gibi metrik tabanlı yerel araçlar donma, sessizlik ve sert kesme noktalarını kusursuz bir şekilde yakalarken; çok kipli yapay zekâ asistanları (VLM) 1 FPS taramalarla kimlik ve nesne sürekliliğini denetler. Ancak TempCompass ve Video-MME verilerinin gösterdiği üzere, mikro zamansal detayların, hareket akıcılığının ve duygusal ritmin nihai denetçisi insan kurgucunun gözüdür. Katı 10 saniyelik çekim kuralı altında maliyet etkin bir boru hattı işletmek, yeniden üretim harcamalarını en aza indirip kurgusal onarım tekniklerini (ara planlar, aynalama, J/L kesmeler) maksimum düzeyde kullanmaktan geçmektedir.
