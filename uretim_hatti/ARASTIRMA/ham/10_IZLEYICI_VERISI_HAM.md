# HAM — 10 İZLEYİCİ VERİSİ (03 prompt 5)

> Kaynak: dış derin araştırma aracı · sahip sohbete yapıştırdı, 07.10.2026.
> Metin olduğu gibidir (oturum kaydından birebir çıkarıldı). Tablolar yapıştırmada satır sonlarını kaybetmiştir. Süzme: `../04_SUZME_20261007.md`.

---

Uzun Biçimli Bilimkurgu Kısa Filmleri ve Dikey Formatlar İçin Kapsamlı YouTube İzleyici Verisi Analizi ve API Entegrasyon Raporu
Stratejik Çerçeve ve Ekim 2026 YouTube Ekosistemi
Ekim 2026 itibarıyla YouTube ekosistemi, içeriklerin performansını salt tıklama oranları üzerinden değerlendirmek yerine, izleyici memnuniyetini merkeze alan derinlemesine etkileşim sinyallerine odaklanmaktadır. Özellikle tek kişilik operasyonlar tarafından üretilen, yüksek prodüksiyon değerine sahip 16:9 bilimkurgu kısa filmleri ve bu evrenden türetilen dikey kesimler (Shorts), algoritmanın kalite değerlendirme mekanizmalarında spesifik zorluklarla karşılaşmaktadır. Yüzlerce videodan oluşan geniş bir kütüphanenin, herhangi bir ücretli analiz aracı, üçüncü taraf tarayıcı eklentisi veya reklam bütçesi bulunmaksızın, tamamen YouTube Studio ve YouTube Analytics API verileriyle analiz edilmesi, organik ve sürdürülebilir büyümenin temel şartıdır.

Bu rapor, söz konusu kısıtlar altında bilimkurgu kısa filmlerinin yayın öncesi test aşamalarından, yayın sonrası API tabanlı mikro-metrik analizlerine kadar uzanan veri yaşam döngüsünü incelemektedir. Analiz, uzun biçimli (1-16 dakika) yatay içerikler ile hızlı tüketim dinamiklerine sahip Shorts formatı arasındaki metrik farklılıklarını tanımlamakta; gösterim, tıklama, mutlak ve göreli tutma oranları ile sentetik (yapay zekâ) içerik etiketlemelerinin algoritmik dağıtıma etkilerini resmî belgelere ve nicel bağımsız çalışmalara dayandırarak yapılandırmaktadır.

Temel İzleyici Ölçütlerinin Tanımı ve Teknik Altyapısı
YouTube ekosisteminde bir filmin performans döngüsü, izleyicinin videoyu keşfetmesi (Gösterim ve Tıklama Oranı) ve videoda ne kadar süre kaldığı (İzleyici Tutma) olmak üzere iki ana fazdan oluşur.

Gösterim (Impressions) ve Gösterim Tıklama Oranı (CTR)
Gösterim, bir videonun küçük resminin platform üzerinde (bilgisayar, TV, oyun konsolu veya mobil cihazlar) bir izleyiciye organik olarak sunulmasıdır. Bir sunumun gösterim olarak sayılabilmesi için, küçük resmin en az yüzde ellisinin ekranda görünür olması ve izleyicinin ekranında en az bir saniye boyunca kalması gerekmektedir. Dış sitelere (harici web sayfaları veya uygulamalar) yerleştirilmiş videolar, e-posta bildirimleri veya arka planda oynatılan içerikler gösterim havuzuna dâhil edilmez. Gösterim Tıklama Oranı (CTR), bu tescilli gösterimlerin ne sıklıkla bir video izlenmesine dönüştüğünü hesaplar. Yüksek bir tıklama oranı, görsel paketin (başlık ve küçük resim) izleyici beklentisini başarıyla tetiklediğini gösterse de, Ortalama İzleme Süresi (AVD - Average View Duration) ile birlikte analiz edilmediğinde algoritma nezdinde yanıltıcı olabilir. Yüksek tıklama oranına karşın düşük ortalama izleme süresine sahip videolar, sistem tarafından "tıklama tuzağı" (clickbait) olarak etiketlenir ve öneri algoritmasındaki gösterim hacimleri sınırlandırılır.   

Kısa film kanallarının yatay formattaki içeriklerinden kesilerek oluşturulan dikey Shorts formatlarında ise gösterim mekanizması tamamen farklıdır. Shorts akışında küçük resim tıklaması söz konusu olmadığından, gösterim metriğinin yerini "Akışta Gösterilme" (Shown in Feed) metriği almaktadır. Tıklama oranının dikey formattaki yapısal karşılığı ise "Görüntülenen ile Kaydırılarak Geçilen" (Viewed vs. swiped away) oranıdır. İçerik akışında karşılaşılan bir kısa videonun izleyici tarafından izlenmeyi seçilme yüzdesini belirten bu metrik, dikey algoritmada erişimin en kritik belirleyicisidir. İstatistiksel eğilimler, izleyicilerin yüzde kırk veya ellisinden fazlasının videoyu kaydırarak geçtiği durumlarda Shorts akışındaki trafiğin hızla kesildiğini göstermektedir.   

İzleyici Tutma (Audience Retention) Eğrileri ve Kilit Anlar
İzleyici tutma eğrisi, bir filmin hangi saniyesinde izleyicilerin anlatıdan koptuğunu veya hangi sahnede dikkatin zirveye ulaştığını saniye saniye yansıtan mikroskobik bir haritadır. YouTube, bu veriyi "Mutlak Tutma" (Absolute Retention) ve "Göreli Tutma" (Relative Retention) olmak üzere iki farklı boyutta sunar. Mutlak tutma, videonun belirli bir anında izleyicilerin yüzde kaçının içeriği izlemeye devam ettiğini saptar. Göreli tutma ise, analiz edilen içeriğin oynatma sırasındaki elde tutma performansını, YouTube'daki benzer uzunluğa sahip diğer ortalama videolarla karşılaştırır.   

YouTube Analytics'in bir video için "Kilit Anlar" (Key Moments) raporunu üretebilmesi için içeriğin en az altmış saniye uzunluğunda olması ve en az yüz izlenmeye (100 views) ulaşmış olması teknik bir zorunluluktur. Bu eşiği geçen videolarda sistem dört farklı kilit an tespit edebilir:   

Giriş (Intro): İçeriğin ilk otuz saniyesi tamamlandığında izleyicilerin yüzde kaçının hâlâ videoyu izlediğini ölçer. Yüksek bir giriş yüzdesi, ilk otuz saniyenin küçük resim ve başlık beklentisini tam olarak karşıladığını kanıtlar. Bilimkurgu gibi atmosfer inşasının zaman aldığı türlerde bu eşiğin yüksek tutulması zordur.   

En İyi Anlar (Top Moments): İzleyicilerin videoyu izlerken neredeyse hiçbir kayıp yaşanmadan, kitle boyutunun stabil kaldığı kesintisiz izleme bloklarıdır.   

Sıçramalar (Spikes): Eğrideki ani yükseliş eğilimleridir. Bu noktalar, izleyicilerin videonun o bölümünü geri sararak tekrar izlediğini veya bu spesifik bölümün harici platformlarda zaman damgasıyla (timestamp) paylaşıldığını işaret eder. İçeriğin karmaşık olması durumunda, izleyicinin sahneyi anlamak için geri sarması da sıçrama yaratabilir.   

Düşüşler (Dips): İzleyicilerin videoyu tamamen terk ettiği veya o sahneyi atlayarak ileri sardığı spesifik noktalardır. Bu kısımlar, kitle ilgisinin kaybedildiği anlatısal boşlukları temsil eder.   

YouTube Analytics API Mimarisi ve Otomasyon Dinamikleri
Yüzlerce videoluk bir kısa film arşivine sahip ancak verilerini düzenli kaydetmemiş tek kişilik bir kanal için, stüdyo arayüzünden manuel CSV dışa aktarımı yapmak ölçeklenebilir bir yöntem değildir. Bu ihtiyacı karşılamak için YouTube Analytics API'nin programatik altyapısı kullanılır. API'ye erişim, OAuth 2.0 protokolü aracılığıyla sağlanmak zorundadır ve raporları okuyabilmek için https://www.googleapis.com/auth/yt-analytics.readonly yetkilendirme kapsamına (scope) ihtiyaç vardır. API kullanımı belirli kota sınırlarına tabidir; kaynak listesi çeken sıradan bir okuma işlemi tipik olarak 1 kota birimi tüketirken, kanal raporu sorgulamaları daha yüksek maliyetler oluşturabilir.   

İzleyici tutma verisinin API tarafındaki çözünürlüğü ve veri modeli, üç temel parametre üzerinden yapılandırılır:

elapsedVideoTimeRatio (Boyut/Dimension): Raporlanan veri satırının, videonun toplam uzunluğunun yüzde kaçına denk geldiğini (örneğin 0.05, 0.50) ifade eden zaman oranıdır. Tutma eğrisinin zaman (X) eksenini oluşturur.   

audienceWatchRatio (Ölçüt/Metric): Belirlenen zaman oranında (elapsedVideoTimeRatio), videoyu izleyen izleyicilerin toplam görüntüleme sayısına kıyasla mutlak oranını tanımlar. Mutlak tutma grafiğinin dikey (Y) eksenidir.   

relativeRetentionPerformance (Ölçüt/Metric): Yine belirlenen zaman oranında, benzer uzunluktaki YouTube videolarına kıyasla elde tutma performansını belirtir. Eğri noktasında bu değer 0.5'ten yüksekse video ortalamanın üzerinde bir kitle tutma sergiliyor, düşükse ortalamanın altında kalıyor demektir.   

Bu verileri çekmek için tasarlanacak basit bir API betiğinde (script), boyut olarak elapsedVideoTimeRatio, ölçüt olarak audienceWatchRatio,relativeRetentionPerformance belirtilmeli ve sorgu video==VIDEO_ID formatında bir filtreyle tek bir video hedeflenerek yapılmalıdır.   

Kapak ve Başlık A/B Testleri ("Test ve Karşılaştır") Mekanizması
İçerik paketlemesinin (kapak ve başlık) organik erişime etkisini ölçmek için kullanılan "Test ve Karşılaştır" (Test & Compare) özelliği, izleyici verisi toplamada en güçlü organik yöntemlerden biridir. Sistem, içerik üreticisine en fazla üç farklı küçük resim (veya başlık) kombinasyonunu gerçek kitle üzerinde eşzamanlı olarak test etme imkânı tanır.   

Testin kazananı belirleme mekanizması, yaygın inancın aksine Tıklama Oranı (CTR) üzerinden değil, İzleme Süresi Payı (Watch Time Share) üzerinden çalışır. YouTube algoritması, izleyicileri yanıltan ve anlık tıklama getirse de hemen çıkma oranı yüksek olan görselleri engellemek için, testin sonunda en yüksek toplam izleme süresini sağlayan kombinasyonu galip ilan eder. Sistemin işleyişinde, test edilen seçenekler dışında kalan küçük bir izleyici dilimi kontrol grubu olarak ayrılabilir ve kazanan görsel bulunduktan sonra bu görsel otomatik olarak tüm platformda varsayılan hâle gelir.   

Testin olgunlaşması ve bir kazanan belirlemesi, videonun aldığı gösterim hacmine, yüklenme tarihinin ne kadar yeni olduğuna ve seçenekler arasındaki istatistiksel farka bağlı olarak birkaç gün ile iki hafta arasında sürebilir. Teste sokulacak küçük resimlerin çözünürlüğü kritik bir kısıttır; eğer yüklenen herhangi bir test görselinin çözünürlüğü 720p (1280 x 720) değerinin altındaysa, deneydeki tüm görseller sistem tarafından otomatik olarak 480p çözünürlüğe düşürülerek test edilir ki bu da tıklama eğilimini negatif etkileyebilir. Ayrıca, aktif bir test devam ederken Studio üzerinden başlık veya kapağın manuel olarak değiştirilmesi testi anında iptal eder. Uzun süredir yayında olan ve performansı duraklamış eski bilimkurgu kısa filmlerinin kapaklarının bu yöntemle test edilmesi, kanalın genel izlenmesine zarar verme riskini minimize ettiği için önerilen güvenli bir stratejidir.   

Yapay Zekâ (Sentetik İçerik) Etiketlemesi ve Algoritmik Dağıtım
Bilimkurgu ve uzay temalı kısa filmler, üretim süreçlerinde yoğun görsel efektler (VFX), fotogerçekçi üç boyutlu modellemeler ve güncel yapay zekâ araçları barındırabilir. YouTube'un saydamlık ve güvenilirlik politikaları gereği, bir videonun yapay zekâ tarafından oluşturulmuş veya anlamlı bir şekilde değiştirilmiş (meaningfully altered) "gerçekçi görünen" (photorealistic) sahneler içermesi durumunda, içerik yükleme aşamasında "Değiştirilmiş veya Sentetik İçerik" (Altered or synthetic content) olarak etiketlenmesi zorunludur. Örneğin, bir uzay filmi dünyadaki gerçek bir şehri yapay zekâ ile yıkılmış gibi gösteriyorsa bu zorunludur; ancak yeşil perde önünde uçan veya tamamen animasyon olduğu belli olan kurgusal fantastik bir sahne bu etiketlemeden muaftır.   

Resmî belgelere ve YouTube blog açıklamalarına göre, bir videonun yapay zekâ veya sentetik içerik olarak işaretlenmesi, videonun izleyici kitlesine ulaşmasını, öneri algoritmasındaki gösterim hacmini veya para kazanma uygunluğunu kesinlikle kısıtlamaz. Aksine, içeriğin gerçekçi bir sentetik yapıya sahip olmasına rağmen içerik üreticisi tarafından kasıtlı olarak etiketlenmemesi ve bunun platform sistemleri tarafından C2PA (Coalition for Content Provenance and Authenticity) içerik kaynağı meta verileriyle veya manuel incelemeyle tespit edilmesi durumunda kanal ceza alır. Bu cezalar arasında videonun kaldırılması veya YouTube İş Ortaklığı Programından men edilme riski bulunur.   

Öte yandan, videonun görsel ve işitsel hiçbir yapay müdahaleye uğramadığını kriptografik olarak kanıtlayan donanımlarla (örneğin C2PA V2.1 uyumlu kameralar) çekilmiş içerikler, platformda "Kamera ile Çekildi" (Captured with a camera) etiketi alabilir. Ancak videonun kurgu programından geçirilirken bu meta veri zincirinin koparılması ("air-gapping"), etiketin düşmesine neden olur. Bilimkurgu filmlerinde post-prodüksiyon yoğun olduğundan, bu içeriklerin sentetik etiket kurallarına göre değerlendirilmesi esastır.   

Eğri Düşüşlerinin Kaynağını Ayırma: İçerik mi, Dış Etken mi?
Elde tutma eğrisinde gözlemlenen bir düşüşün (dip) her zaman başarısız bir kurgudan, kötü oyunculuktan veya hikâyenin kopmasından kaynaklandığını varsaymak, veri biliminde yaygın bir teşhis hatasıdır. Düşüşün içsel (içerik kaynaklı) mi yoksa dışsal (trafik ve çevre kaynaklı) mı olduğunu ayırt etmek için çok katmanlı bir segmentasyon analizi yapılmalıdır.

Dış Etkenlerin Ayrıştırılması:
Elde tutma metriklerini en çok kirleten dışsal faktör trafik kaynağıdır. Örneğin, harici sitelere (bilimkurgu forumları, kişisel bloglar) yerleştirilmiş (embed) oynatıcılar üzerinden veya arama sonuçlarından gelen izleyiciler, genellikle belirli bir spesifik bilgiyi arayan ve bulamadığında hızla terk eden soğuk kitlelerdir. Öte yandan "Göz Atma Özellikleri" (Browse Features) veya "Önerilen Videolar" üzerinden gelen izleyicilerin tutma profilleri daha organiktir. Tutma eğrisindeki sert bir düşüşü test etmek için, Studio üzerinden trafik kaynakları filtrelenmeli ve sadece "Göz Atma" veya "Aboneler" kitlesinin eğrisine bakılmalıdır. Düşüş, sadık kitle filtrelemesinde kayboluyorsa sorun içerikte değil, videonun yerleştirildiği yanlış bir harici kaynakta veya algoritmanın videoyu yanlış bir "soğuk kitleye" önermesindedir.
Ayrıca, ilk 48 saatlik veri çoğunlukla bildirim zili açık abonelerden gelir ve bu kitlenin elde tutma oranı yapay olarak çok yüksektir. Video zamanla daha geniş kitlelere yayıldıkça ortalama izleme süresinin ve tutma oranının doğal olarak düşmesi, içerik kalitesizliğinin değil, algoritmik genişlemenin olağan bir sonucudur.   

İç Etkenlerin (İçerik) Ayrıştırılması:
Dış trafik etkileri filtrelendikten sonra düşüş hâlâ belirginse, sorun doğrudan içeriğin kendisindedir. Bu noktada düşüşün başladığı tam saniye (elapsedVideoTimeRatio) video oynatıcısıyla eşleştirilir. Eğer bu saniyede yavaş bir ortam çekimi (establishing shot), sessiz ve diyaloğun koptuğu bir karanlık ekran geçişi, yersiz bir müzik kesintisi veya videonun vaadiyle uyuşmayan bir kurgu hatası varsa, düşüşün sebebi kesin olarak içsel bir ritim sorunudur.   

Tek Videonun Yetersizliği:
Algoritmik performansı değerlendirirken tek bir kısa filmin verisi asla mutlak kural sayılamaz. Algoritma her videoyu farklı bir "tohum kitle" (seed audience) ile test edebilir. Gerçekçi bir kıyaslama yapabilmek için, aynı görsel atmosfere ve benzer uzunluğa sahip en az 5 ila 10 farklı videonun karşılaştırılması gerekir. Bu videoların birbiriyle kıyaslanabilmesi için de hepsinin benzer algoritmik olgunlaşma pencerelerini (örneğin hepsinin yayından sonraki 7. veya 28. günü) tamamlamış ve istatistiksel anlamlılığa ulaşacak kadar (en az binlerce) gösterim almış olması elzemdir.   

Yayın Öncesi Tahminler ve Yayın Sonrası Gerçeklik (Ölçümlerin Doğrulanması)
İçerik üreticileri, bir kısa filmi çekmeden veya yayına almadan önce izleyici kayıplarını tahmin edebilmek için çeşitli analitik ve yapay zekâ tabanlı (hat dışı) yöntemler kullanırlar. Televizyon ve sinema endüstrisinde senaryolar üzerinde uygulanan Doğal Dil İşleme (NLP) yöntemleri, YouTube içerik stratejilerine de uyarlanmaktadır.

Akademik araştırmalar, 200'den fazla televizyon dizisinin 25.000'i aşkın bölümünün senaryolarındaki "duygusal ton" (Öfke, Neşe, Negatif Duygu) ve "bilişsel karmaşıklık" gibi metin özelliklerinin makine öğrenimi modelleriyle (XGBoost, SARIMAX) analiz edilmesinin, bölümden bölüme izleyici tutma oranlarını tahmin etmede anlamlı bir istatistiksel katkı sağladığını kanıtlamıştır. YouTube özelinde, Prepublish.ai gibi (hat dışı) senaryo analiz araçları, özellikle ilk 30 saniyelik giriş bölümünün bilişsel kurgusunu test etmektedir. Bu yöntemlere göre, ilk 5 saniyede algoritmadaki "kaydırma" eğilimini kıracak bir görsel/işitsel örüntü kesicinin (pattern interrupt) olması, 5-15. saniyelerde izleyiciye videonun kapağındaki vaadin açıkça verilmesi ve 15-30. saniyelerde hikâyeye dair bilişsel bir boşluk (information gap) yaratılması, yayın sonrası tutma oranlarını doğrudan etkileyen kurgusal kurallardır.   

Ancak, yapay zekâ dil modellerine videoyu izletip "Nerede sıkıldın?" diye sormak veya hikâyeyi bilmeyen birkaç test izleyicisine ön gösterim yapmak (test screening), gerçek YouTube algoritmasını tam olarak simüle edemez. Test izleyicisinin dikkati yüksek, algısı açıktır ve videoyu sonlandırma (swipe away veya sekme kapatma) eşiği YouTube'un "göz atma" alışkanlığına kapılmış sıradan bir izleyicisinden çok daha yüksektir. Odak gruplarında izleyicilerin "kafam karıştı" dediği saniye, yayın sonrasındaki "Düşüşler" (Dips) grafiğiyle büyük oranda eşleşse de; algoritmanın soğuk kitlelere gösterimiyle oluşan rastgele erken terkler, ön gösterim verisinden bağımsız olarak gerçekleşir. Bu nedenle ön gösterim verileri, kurgusal boşlukları tespit etmek için mükemmeldir ancak gerçek kitle tutma yüzdesini sayısal olarak tahmin etmekte yetersiz kalır.   

Yapılandırılmış Veri Tabloları
(Kritik Kısıt Notu: Yaratıcının bütçe ve üçüncü taraf araç kısıtlaması göz önüne alınarak, dış donanım veya bütçe gerektiren maddeler "Hat Dışı" notu ile ancak tabloda varlığını koruyacak şekilde eklenmiştir.)

(a) ÖLÇÜT Tablosu
Aşağıdaki tablo, analitik ölçütlerin resmî tanımlarını ve API karşılıklarını düzenler.

Ölçüt    Resmî Tanım (Birebir Alıntı)    Studio'da Nerede    API'de Rapor / Boyut / Ölçüt Adı    En Düşük Veri Eşiği    Uzun Video / Shorts Farkı    Kaynak    Etiket
Görüntüleme (Views)    "The number of legitimate views for your channels or content. Views are counted the moment a video starts to play across all formats, including Shorts, long form videos (VOD), and live streams."    Analytics > Genel Bakış / İçerik    video raporu / views (ölçüt)    Eşik yok.    Fark yok, iki formatta da başlatıldığı an sayılır.        ÖLÇÜLMÜŞ
Gösterim (Impressions)    "How many times your video thumbnails were shown to viewers on YouTube through registered thumbnail impressions."    Analytics > İçerik > Videolar > Erişim    video raporu / impressions    Eşik yok. (>1 sn, %50 görünürlük)    Shorts formatında "Shown in feed" (Akışta Gösterilme) olarak adlandırılır.        ÖLÇÜLMÜŞ
Tıklama Oranı (CTR)    "How often viewers watched a video after seeing a thumbnail."    Analytics > İçerik > Videolar > Erişim    video raporu / annotationClickThroughRate (Manuel hesaplama gerekebilir)    Eşik yok. (Anlamlı bir gösterim hacmi önerilir)    Shorts formatında CTR yerine "Viewed vs. swiped away" (Görüntülenen/Kaydırılarak geçilen) oranı kullanılır.        ÖLÇÜLMÜŞ
Giriş (Intro)    "Intro tells you what percentage of your audience still watched your video after the first 30 seconds."    Analytics > Etkileşim > Kitleyi Elde Tutma    audienceWatchRatio at elapsedVideoTimeRatio <= 30s    En az 60 sn uzunluk, en az 100 izlenme.    Shorts'ta süre çok kısa olduğundan giriş kaybı genellikle ilk saniyelerde yaşanır.        ÖLÇÜLMÜŞ
Göreli Tutma (Relative Retention)    "relativeRetentionPerformance metriği, bir videonun izleyicileri oynatma sırasında elde tutma performansını benzer uzunluktaki YouTube videolarına kıyasla gösterir."    Analytics > Etkileşim > Elde Tutma (Kıyasla)    relativeRetentionPerformance (Ölçüt)    En az 60 sn uzunluk, en az 100 izlenme.    Dikey algoritmada göreli tutma analizinden ziyade döngü (loop) oranlarına bakılır.        ÖLÇÜLMÜŞ
  
(b) DIŞA AKTARMA Tablosu
Manuel Excel/CSV aktarımları ile temel betik tabanlı API çağrı yolları.

Veri    Studio Adımları    API Çağrısı    Dosya Biçimi    Kaynak    Etiket
Kanal Düzeyinde Metrikler    Analytics > Gelişmiş Mod > Videoya göre karşılaştır > Dışa Aktar (Sağ Üst)    reports.query metrics=views,estimatedMinutesWatched,averageViewDuration    CSV / Google E-Tablolar        UYGULAMA
Videonun Elde Tutma Eğrisi    Video Analytics > Etkileşim > Kitleyi Elde Tutma > Daha Fazla Göster > Dışa Aktar    dimensions=elapsedVideoTimeRatio metrics=audienceWatchRatio,relativeRetentionPerformance filters=video==[VIDEO_ID]    CSV (Manuel) / JSON (API betiği)        UYGULAMA
Trafik Kaynağı Karışımı    Video Analytics > Erişim > Trafik Kaynakları > Gelişmiş Mod > Dışa Aktar    dimensions=insightTrafficSourceType metrics=views,estimatedMinutesWatched filters=video==[VIDEO_ID]    CSV (Manuel) / JSON (API betiği)        UYGULAMA
  
(c) OKUMA Tablosu
Eğrideki anomalilerin (düşüş ve sıçrama) teşhisi.

Düşüş ya da Sıçrama Türü    Olası İç Neden (İçerik)    Olası Dış Neden (Çevre)    Ayırt Etme Yöntemi    Kaynak    Etiket
İlk 15-30 Saniyede Keskin Düşüş    Başlık/Kapak vaadinin gerçekleşmemesi (Clickbait hissi), çok yavaş bir ortam çekimiyle başlamak, jenerik kullanımı.    Dış bağlantılardan (embed) gelen otomatik oynamalar, algoritmanın videoyu çok ilgisiz bir geniş kitleye önermesi.    Gelişmiş Mod'da trafik kaynağı yalnızca "Göz Atma" (Browse) yapılarak eğriye tekrar bakılır. Düşüş sürüyorsa neden içerik kurgusudur.        ÖNERİ
Videonun Bir Noktasında Keskin Sıçrama (Spike)    Bilimkurgu dünyasına ait karmaşık bir VFX sahnesi veya "easter egg" nedeniyle geri sarma yapılması.    O spesifik anın bir Shorts kesiti olarak veya harici bir forumda (Reddit vb.) bağlantı olarak (timestamp) paylaşılması.    Trafik kaynağında o gün içinde "Harici" (External) veya doğrudan bağlantı artışı olup olmadığı kontrol edilir.        ÖLÇÜLMÜŞ
Videonun Ortasında Kademeli (Gradual) Düşüş    Anlatının (narrative) kopması, diyalogların uzaması ve kurgu ritminin aşırı yavaşlaması.    Kitlenin videodan aradığı hızlı tatmini (örn. sadece VFX izlemek) alıp çıkması.    Düşüş saniyesindeki sahne değişimleri analiz edilir. Görsel hızın yavaşladığı anlara denk geliyorsa içsel bir ritim sorunudur.        UYGULAMA
  
(d) KIYAS Tablosu
Bilimkurgu, kısa film ve uzun içerikler için hedeflenen aralıklar ve yöntemler.

İçerik Türü    Ölçüt    Aralık / Beklenti    Örneklem ve Yöntem    Kaynak    Etiket
Dikey Kesimler (Shorts)    Görüntülenen / Kaydırılan (Viewed vs Swiped Away)    > %50 - %60 Görüntülenen    Shorts algoritmasında trafik kesilmesini engellemek için %40-50'den fazla swipe-away oranı tehlikelidir (Ajans/Yaratıcı Vaka Analizleri).        UYGULAMA
Müzik / Kurgusal Kısa Filmler (3-4 dk)    İlk 30 Saniye Mutlak Tutma Oranı    %60 - %70+    Müzik ve kurgu odaklı içerik yönetimi ajans analizleri.        UYGULAMA
Kısa Filmler (10-20 dk)    Ortalama İzlenme Yüzdesi (APV)    %35 - %45    Genel YouTube kanalları üzerinde yapılan analiz (sayı ve örneklem büyüklüğü belirsizdir).        UYGULAMA
TV/Dizi Senaryoları (Yayın Öncesi NLP Tahmini)    Duygusal Ton ve Bilişsel Karmaşıklık Etkisi (Makine Öğrenimi)    R² = 0.742'ye varan doğruluk    219 diziden toplanan 25.257 bölüm senaryosu, OpenSubtitles API ile çekilip XGBoost/SARIMAX modelleriyle analiz edilmiştir. [HAT DIŞI YÖNTEM]        ÖLÇÜLMÜŞ
  
İzleme Listeleri ve Kayıt Mekanizmaları
Tek kişilik bir organizasyonda API betiğinin düzenli çalışmaması veya erişimin kesilmesi ihtimaline karşı, kanalın gelişimini belgelemek için asgari sütunlarla oluşturulmuş manuel bir takip tablosu tutulmalıdır.

(1) Film Başına Tek Satırlık Kayıt Şablonu Önerisi
Her yeni bilimkurgu kısa filmi yayımlandığında bir satır açılır ve 48. saat, 7. gün ve 28. gün sonlarında Stüdyo verileriyle doldurulur.

Video_ID: (Örn. dQw4w9WgXcQ)

Format_Türü: (16:9 Yatay / 9:16 Shorts)

Konsept_Özeti: (Örn. Uzay Gemisi İzolasyonu)

Uzunluk_Saniye: (Örn. 425 sn)

48s_Gösterim: (Veya Shorts için Akışta Gösterilme)

48s_CTR: (%) (Veya Shorts için Görüntülenme Oranı)

48s_APV: (Ortalama İzlenme Yüzdesi)

48s_İlk30sTutma: (Giriş performansı %)

7g_Gösterim:

7g_CTR:

7g_APV:

28g_Gösterim:

28g_CTR:

28g_APV:

Kritik_Düşüş_Saniyesi: (Eğrinin kırıldığı süre damgası)

Test_Karşılaştır_Sonucu: (Kazanan atandı / Sonuçsuz)

(2) Araştırma Bulgularının Doğrulanabilirliği ve Kaynaksız İddialar (Hipotezler)
Araştırma kapsamında platform politikaları ve ölçüm yöntemleri hakkında öne sürülen bulgular ve doğrulanamayan hipotezler aşağıda ayrıştırılmış ve ilgili kanıt URL'leriyle (https://...) sunulmuştur. Bütçe gerektiren yöntemler sistem sınırları gereği hat dışı bırakılarak değerlendirilmiştir.

DOĞRULANDI: Yapay zekâ (Sentetik) etiketinin organik dağıtımı kesmediği gerçeği.

YouTube resmî belgelerine göre, fotogerçekçi sentetik içerik etiketinin kullanılması, videonun kitlesini, öneri mekanizmasındaki yerini veya para kazanma uygunluğunu kısıtlamaz. Aksine, beyan edilmemesi videonun kaldırılmasına yol açar. (Kanıt: https://support.google.com/youtube/answer/14328491)   

DOĞRULANDI: A/B kapak testi kazananının Tıklama Oranı (CTR) ile değil İzleme Süresi (Watch Time) ile seçilmesi.

"Test ve karşılaştır" özelliği, salt tıklama tuzaklarını önlemek için kazananı her zaman en yüksek izleme süresi payını (watch time share) getiren görsele göre tayin eder. (Kanıt: https://support.google.com/youtube/answer/16391400)   

DOĞRULANDI: Elde tutma grafiğinde "Kilit Anlar" eşiğinin matematiksel sınırı.

Stüdyo arayüzünde giriş, sıçrama ve düşüşlerin işlenebilmesi için söz konusu videonun asgari 60 saniye uzunluğunda olması ve en az 100 izlenmeye ulaşması algoritmik bir zorunluluktur. (Kanıt: https://support.google.com/youtube/answer/9314415)   

DOĞRULANDI: Dikey formatta CTR yerine Görüntüleme/Kaydırma metriğinin kullanılması.

Shorts ekosisteminde küçük resim gösterimi olmadığı için başarı, izleyicinin videoyu gördüğünde yukarı kaydırmak yerine izlemeyi ("Viewed vs swiped away") seçme oranına göre hesaplanır. (Kanıt: https://support.google.com/youtube/answer/12942217)   

HİPOTEZ: Yayın öncesi senaryoyu yapay zekâya okutarak (Örn. Prepublish.ai) YouTube elde tutma oranlarının tam olarak tahmin edilebileceği iddiası.

Neden doğrulanamadı: Senaryolardaki NLP modelleri (XGBoost vb.) dizilerin bölüm bazlı izlenmesini akademik olarak öngörebilse de (https://arxiv.org/abs/2506.00076), YouTube'daki rastgele kaydırma yapan kitlelerin erken terkleri sadece senaryoyla açıklanamayacak dış trafik anomalilerine (mobil cihaz davranışı, rastgele öneriler) tabidir; dolayısıyla makine tahmini ile yayın sonrası mutlak tutma oranı matematiksel olarak tam örtüşmez (https://prepublish.ai/guides/first-30-seconds).   

HİPOTEZ: Kısa filmlerde %70 ve üzeri tutma oranının algoritma için kesin bir "viral sıçrama" garantisi olduğu iddiası.

Neden doğrulanamadı: Yüksek elde tutma algoritma için çok olumlu bir sinyal olsa da, YouTube öneri algoritması (Neural Networks altyapısı) çok boyutludur; CTR, izleyicinin oturum süresi (session time) ve kullanıcı bazlı kişiselleştirme gibi gizli etkenler nedeniyle tek başına %70 APV oranı hiçbir resmi belge tarafından "garanti" bir ölçüt sayılarak desteklenmemektedir.   

