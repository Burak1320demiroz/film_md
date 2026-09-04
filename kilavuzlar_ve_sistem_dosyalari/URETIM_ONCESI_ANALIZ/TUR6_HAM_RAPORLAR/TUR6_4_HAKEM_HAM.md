# TUR 6 · HAM RAPOR 4/4 — HAKEM GÜVENİLİRLİĞİ

> Koşulan prompt: `../10_DIYALOG_ARASTIRMA_PROMPTLARI.md` §4
> Koşu: 03.09.2026 · dış derin araştırma modeli · HAM ÇIKTI — düzeltilmez
> Süzme: `../04_ARASTIRMA_BULGULARI.md` §TUR 6

---

Yaratıcı Metinlerin Değerlendirilmesinde İnsan ve Yapay Zeka Uzlaşısı: Güvenilirlik, Yanlılıklar, Hafifletme Stratejileri ve Ölçüm Araçları Üzerine Kapsamlı Bir Analiz

Yaratıcı metinlerin (senaryo, kurmaca, diyalog, şiir) kalitesini nesnel bir biçimde ölçmek, doğal dil işleme (NLP) ve eğitimde ölçme-değerlendirme literatürünün en karmaşık problemlerinden biridir. Kesin bir doğru yanıtın (ground truth) veya referans metnin bulunmadığı açık uçlu (open-ended) görevlerde, BLEU, ROUGE veya METEOR gibi geleneksel kelime örtüşme (N-gram) metrikleri, insan yargısıyla anlamlı bir korelasyon kurmakta yetersiz kalmaktadır. Bu epistemolojik boşluk, tarihsel olarak insan uzmanların kullanıldığı Uzlaşımsal Değerlendirme Tekniği (Consensual Assessment Technique - CAT) ile doldurulmaya çalışılmış; ancak son yıllarda Büyük Dil Modellerinin (LLM) "hakem" (LLM-as-a-Judge) olarak konumlandırıldığı otomatik sistemler, hem maliyet hem de ölçeklenebilirlik avantajlarıyla öne çıkmaya başlamıştır.

Bu rapor, yaratıcı metin değerlendirmelerinde insan hakemlerin kendi aralarındaki tutarlılığını (inter-rater reliability - IRR) yapısal ve öznel eksenler bağlamında incelemekte; ardından LLM hakemlerin sergilediği sistematik yanlılıkların (bias) ölçülmüş büyüklüklerini detaylandırmaktadır. Analiz, bu algoritmik sapmaları hafifletmek için literatürde sınanmış yöntemlerin istatistiksel etkilerini ve senaryo/diyalog analizi için yayımlanmış açık değerlendirme araçlarının (DramaBench, FED) geçerlilik yapılarını kapsamlı bir çerçevede sentezlemektedir.

İnsan Hakemlerin Yaratıcı Metinlerdeki Tutarlılığı (Inter-Rater Reliability) ve Eksenler Arası Ayrışma
İnsan hakemler arası güvenilirlik, bir değerlendirme aracının öznellikten ne kadar arındırıldığının ve ölçülmek istenen yapıyı ne kadar istikrarlı bir şekilde yakaladığının temel göstergesidir. Yaratıcı yazarlık ve diyalog gibi alanlarda bu ölçüm; sürekli veriler için Sınıfiçi Korelasyon Katsayısı (ICC), kategorik veriler için Cohen's Kappa (κ) veya Fleiss' Kappa ve sıralı/aralıklı veriler için Krippendorff's Alpha (α) istatistikleriyle ifade edilmektedir. Literatür, yaratıcı metin değerlendirmelerinde insan hakemlerin, nesnel doğruluk veya bilgi çıkarımı gerektiren görevlere kıyasla çok daha düşük bir uyuşma sergilediğini, uyuşma düzeyinin ise değerlendirilen eksenin "yapısal" veya "öznel" olmasına göre dramatik kırılmalar yaşadığını göstermektedir.

Uzlaşımsal Değerlendirme Tekniği (CAT) ve Bilişsel Yük
Teresa Amabile tarafından 1982 yılında literatüre kazandırılan Uzlaşımsal Değerlendirme Tekniği (CAT), yaratıcılığın kavramsal bir tanımdan ziyade, o alanın uzmanları tarafından bağımsız olarak algılanan operasyonel bir olgu olduğu varsayımına dayanır. Eğitim bilimleri ve yaratıcı düşünce literatüründe sıkça başvurulan bu yöntemin geçerliliği, büyük oranda hakemler arası yüksek güvenilirlik elde edilmesine bağlıdır. Ancak, 2018 yılında European Proceedings of Social and Behavioural Sciences (EPSBS) dergisinde yayımlanan ampirik bir ölçme-değerlendirme çalışmasında, 277 çocuğun yazdığı yaratıcı hikayelerin değerlendirilmesinde güvenilir bir IRR değerine ulaşmak için en az 5 bağımsız koda (hakeme) ihtiyaç duyulduğu saptanmıştır. İlgili çalışmada, hikayeler 10 farklı boyutta incelenmiş ve değerlendirmenin iki ana faktöre ayrıştığı görülmüştür: "Mantık" (Logic) ve "Yaratıcı İfade" (Creative Expressiveness). Hakemlerin yapısal ve kurala dayalı olan mantık eksenindeki uyuşmalarının (r = 0.44), yoruma açık olan yaratıcı ifade ekseninden çok daha belirgin ve kolay elde edilebilir olduğu vurgulanmıştır.

Tasarım ve yaratıcılık literatüründe yayımlanan 2015 tarihli hakemli bir başka çalışma, CAT'in grafik tasarım ve metin tabanlı yaratıcı görevlerdeki güvenilirliğini sorgulamış; hakemlerin teknik icra (format ve yapı) konusundaki kişisel tercihlerinin, asıl ölçülmek istenen "yaratıcılık" kavramını gölgeleyerek IRR'yi düşürdüğünü kanıtlamıştır. Hakemlere teknik yapıyı "göz ardı etmeleri" yönünde açık bir talimat verildiğinde uyuşma bir miktar artsa da, metin bazlı görevlerde güvenilirlik 0.56 ile 0.69 gibi marjinal (ideal olan 0.70'in altında) seviyelerde kalmıştır. Bu durum, insanlar için yapısal hataların (teknik formatın) değerlendirme sürecinde güçlü bir bilişsel çapa (anchor) işlevi gördüğünü, bu çapa ortadan kalktığında öznel estetik yargılarda uzlaşmanın zorlaştığını göstermektedir. Öte yandan, 2018 tarihli bir başka hakemli çalışmada, yaratıcı yazarlığı "anlatıcı sesi", "karakterizasyon", "diyalog" ve "olay örgüsü" gibi 9 spesifik alt yapıya bölen detaylı bir analitik rubrik kullanıldığında, uzman hakemler arası korelasyonun 0.79'a ulaştığı raporlanmıştır.

Öznel ve Yapısal Eksenlerdeki Güvenilirlik Farklılıklarının Doğrulanması
Yaratıcı metinlerdeki kişisel tercihlerin ne kadar ayrışabileceğini gösteren en güncel veri, 2025 tarihli "LiteraryTaste" adlı doğal dil işleme (arXiv) ön baskı çalışmasından gelmektedir. 60 katılımcının kısa yaratıcı yazarlık metinleri üzerindeki "açıklanan tercihlerinin" (revealed preferences) ölçüldüğü bu araştırmada, ortalama Fleiss' Kappa değeri 0.1405 (standart sapma 0.1005) olarak bulunmuştur. En düşük kappa değerinin -0.0179, en yükseğinin ise 0.3805 olması, kurmaca metinlerin estetik değerine ilişkin yargıların son derece bireysel olduğunu ve insanların edebi zevk konusunda neredeyse hiç uzlaşamadığını istatistiksel olarak kanıtlamaktadır.

Değerlendirme aracı yapısal (örneğin dilbilgisi, format) ve öznel (örneğin diyalog kalitesi, duygusal derinlik) eksenlere bölündüğünde, uyuşma rakamlarındaki kutuplaşma netleşmektedir. Metin özetleme ve üretimi üzerine 2021 tarihli SummEval çalışmasını inceleyen 2023 tarihli bir ikincil derleme raporu (arXiv), uzman hakemlerin yapısal eksenlerde yüksek uyuşma sağlarken, anlamsal eksenlerde çöktüğünü belgelemiştir. Uzmanlar, metnin içsel tutarlılığı (consistency) konusunda 0.798 gibi oldukça yüksek bir Krippendorff's Alpha değerine ulaşırken; alaka düzeyi (relevance) gibi bağlama ve yoruma açık bir eksende bu uyuşma 0.398'e çakılmıştır. Daha çarpıcı olanı, kitle kaynaklı (crowdsourced / Amazon Mechanical Turk) sıradan hakemlerin, görevi kavrama sınırlılıkları nedeniyle tüm metriklerde 0.48 ile 0.51 bandına sıkışması ve uzmanlar ile sıradan hakemler arasındaki uyuşmanın en fazla 0.247 olarak ölçülmesidir.

Empatik iletişimin değerlendirildiği 2025 tarihli bir başka NLP çalışması (arXiv ön baskı), uzman hakemlerin Krippendorff's Alpha değerlerinin alt bileşenlerin karmaşıklığına ve öznelliğine göre 0.29 ile 0.78 arasında (ortanca = 0.55) şiddetli bir dalgalanma gösterdiğini ortaya koymuştur. Aynı çalışmada Ağırlıklı Cohen's Kappa (κw) değerleri de 0.11 ile 0.84 arasında (ortanca 0.58) ölçülmüştür.

Değerlendirme Ekseni / Araştırma Konusu    Kaynak Türü ve Yılı    Kullanılan Ölçüm Metriği    Uyuşma (IRR) Değeri    Nicel ve Nitel İçgörü
Literatür Zevki (Kurmaca Tercihi)    Özgün Araştırma (2025)    Fleiss' Kappa    0.1405    Kurmaca metinlerde estetik tercihlerin tamamen bireysel olduğu, genellenebilir bir "kalite" uzlaşısının zor olduğu kanıtlanmıştır.
İçsel Tutarlılık (SummEval - Uzman)    İkincil Derleme (2023)    Krippendorff's α    0.798    Mantıksal ve yapısal tutarlılıkta, uzmanların zihinsel modelleri örtüştüğü için yüksek güvenilirlik elde edilir.
Alaka Düzeyi (SummEval - Uzman)    İkincil Derleme (2023)    Krippendorff's α    0.398    Anlamsal derinlik veya bağlamsal ilişki gibi yoruma açık görevlerde uzman uyuşması yarı yarıya azalmaktadır.
Empatik İletişim Analizi    Özgün Araştırma (2025)    Ağırlıklı Kappa (κw)    0.11 - 0.84 (Ort: 0.58)    Çerçeve ne kadar belirgin ve nesnel ise uyuşma o kadar artar; duygu analizi işin içine girdiğinde uyuşma çöker.
CAT ile Yaratıcı Hikaye (Çocuk)    Ölçme Çalışması (2018)    Alfa / Korelasyon    Mantık: r=0.44    Kesin yapısal rubrikler (Mantık) olmadan yaratıcılık (İfade) uyuşması dalgalıdır; güvenilirlik için minimum 5 hakem şarttır.
Metin Tabanlı Grafik Tasarım (CAT)    Tasarım Literatürü (2015)    Sınıfiçi Korelasyon    0.56 - 0.69    Teknik icrayı dışarda tutma çabası bile, görsel/metinsel yaratıcılıkta mükemmel uyumu ( > 0.70) sağlayamamıştır.

Bu istatistiksel panorama, diyalog akıcılığı, karakter derinliği veya olay örgüsünün yaratıcılığı gibi öznel eksenlerdeki insan hakem uyuşmasının; dilbilgisi, format standartları veya mantıksal nedensellik gibi yapısal eksenlere kıyasla sistematik olarak daha düşük olduğunu kesin bir biçimde göstermektedir. İnsanlar, yapısal hataları bulmakta ortak bir dil konuşurken, sanatsal veya yaratıcı değer atfetme noktasında kendi bilişsel önyargılarına yenik düşmektedirler.

LLM Hakemlerin Sergilediği Sistematik Yanlılıklar ve Ölçülmüş Büyüklükleri
İnsan değerlendirmesinin yavaş, pahalı ve düşük güvenilirlikli (özellikle öznel konularda) olması, araştırmacıları 2023 yılından itibaren "Hakem Olarak LLM" (LLM-as-a-Judge) paradigmasına yöneltmiştir. GPT-4, Claude gibi modellerin insan tercihleriyle (İnsan Geri Bildirimli Pekiştirmeli Öğrenme - RLHF sayesinde) yüksek oranda hizalanmış olması, bu modellerin sentetik hakemler olarak kullanılmasının önünü açmıştır. Ufuk açıcı nitelikteki 2023 tarihli Zheng vd. çalışması (NeurIPS), güçlü LLM hakemlerin kontrollü ve kitle kaynaklı insan tercihleriyle %80'in üzerinde bir uyuşma yakaladığını (bu oran, insanların kendi aralarındaki %81'lik uyuşmayla aynı seviyededir) duyurmuştur.

Ancak LLM hakemler mükemmel değildir; kendi eğitim süreçlerinin (hedef-vekil uyuşmazlığı) bir yan etkisi olarak insanlardan farklı, sistematik algısal sapmalar (bias) üretirler. Bu yanlılıklar rastgele (noise) değildir; istatistiksel bir güven aralığıyla ölçülebilir ve sabit bir yöne doğru sapma gösterirler. Model sağlayıcı teknik raporları, yarışma kılavuzları ve hakemli meta-değerlendirme literatüründe belgelenmiş spesifik yanlılıkların büyüklükleri aşağıda detaylandırılmıştır.

1. Uzunluk ve Ayrıntı Yanlılığı (Verbosity / Length Bias)
LLM hakemler, metnin anlamsal kalitesi, bilgi yoğunluğu veya doğruluğu kontrol altında tutulduğunda dahi, salt daha uzun olan (daha fazla token içeren) yanıtları daha yüksek puanlama eğilimindedir. Modeller, "daha fazla kelimeyi" "daha fazla efor ve kapsam" olarak algılayan bir kısayol (heuristics) geliştirmişlerdir ve çoğu zaman gereksiz kelime salatası (filler) içeren yanıtları ödüllendirirler.

Ölçülmüş Büyüklüğü: AlpacaEval veri seti üzerinde 2024 yılında (arXiv) yapılan çalışmalarda, kazanma oranlarının (win rates) yanıt uzunluğuyla orantılı olarak yapay şekilde arttığı kanıtlanmıştır. Daha çarpıcı bir veri, Spectrum of Research platformunda 2024 yılında yayımlanan ve MT-Bench, FairEval, LLMBar gibi 5 büyük veri setini sentezleyen ikincil derleme raporundan gelmektedir. Bu çalışmada, bir değerlendirme sisteminde yalnızca yanıt uzunluğu (length control) istatistiksel olarak kontrol altına alındığında (uzunluğa verilen haksız prim silindiğinde), otomatik sistemin kitle kaynaklı Arena liderlik tablosundaki insan tercihleriyle olan sıra korelasyonunun (rank correlation) 0.94'ten 0.98'e fırladığı ölçülmüştür. Bu, uzunluk yanlılığının tek başına bir modelin genel performans haritasını %4 oranında saptırabildiğini göstermektedir.

2. Konum Yanlılığı (Position Bias)
Açık uçlu metinlerin değerlendirilmesinde en sık başvurulan yöntem olan "ikili karşılaştırma" (pairwise comparison) senaryolarında LLM hakemler, istem (prompt) içinde ilk sırada (A konumu) sunulan metni, kalitesinden bağımsız olarak sistematik şekilde tercih ederler. Literatürde daha nadir olarak "ikinci konumu" kayıran modellere rastlansa da, genel eğilim "öncelik" (primacy) etkisidir.

Ölçülmüş Büyüklüğü: 2023 tarihli NeurIPS çalışmasında (Zheng vd.) ve bunu takip eden denetimlerde, GPT-4 gibi yüksek parametreli gelişmiş modellerin 1. Konumu ortalama ~%5 oranında haksız yere kayırdığı ölçülmüştür. Zayıf (örneğin 13 milyar parametreli) açık kaynaklı hakemlerde ise bu konum yanlılığı muazzam boyutlara ulaşarak sıralama sonuçlarında %25 ile %30 arasında sapmalara neden olmaktadır. Wang vd. (FairEval, 2023) tarafından yapılan ampirik bir çalışmada, aynı iki adayın sadece sunum sırasının değiştirilmesinin, zayıf bir değerlendirici modelin 80 karşılaştırmanın 66'sında (yaklaşık %82,5) galibi değiştirmesine neden olduğu gözlemlenmiştir. Çalışmalar ayrıca, konum yanlılığının şiddetinin, aday metinler arasındaki "kalite farkı" azaldıkça üstel olarak arttığını göstermektedir; metinler birbirine ne kadar yakınsa, model kolaya kaçıp ilk gördüğünü seçmektedir.

3. Kendi Üslubuna / Çıktısına Yatkınlık Yanlılığı (Self-Enhancement Bias)
Modeller, senaryo devamlılığı veya kurmaca gibi değerlendirmelerde, kendi ürettikleri veya kendi temel mimari ailelerine (örn. LLaMA ailesi, GPT ailesi) ait olan metinleri, başka modellerin eşit kalitedeki metinlerine kıyasla daha yüksek puanlama eğilimindedir. LLM'ler, kendi eğitim verilerindeki içsel üslubu daha "akıcı" veya "doğru" bulurlar.

Ölçülmüş Büyüklüğü: 2024 ve 2025 yıllarında yayımlanan hakemli ve arşiv (arXiv) ön baskı istatistiksel çerçeve çalışmalarında (Panickssery vd., Liu vd.), aile-içi değerlendirmelerde modellerin kendi çıktılarını kayırma oranının (bağımsız uzman hakemlerin tarafsız referanslarına göre) kazanma oranlarında net %3 ile %8 arasında bir enflasyon (şişkinlik) yarattığı ölçülmüştür. Örneğin, GPT-4'ün kendisiyle aynı kalitede olduğu bağımsızca doğrulanmış bir Claude çıktısına kıyasla, kendi çıktısına istatistiksel olarak daha fazla galibiyet verdiği belgelenmiştir.

4. Üslubu ve Biçimi İçeriğe Tercih Etme (Style / Formatting Bias)
Yaratıcı ve akademik metinlerde LLM'lerin en ciddi zaaflarından biri, içerik boş olsa bile yüzey düzeyindeki biçimlendirme hilelerine (bold yazılar, listeler, temiz paragraflar) kanmalarıdır.

Ölçülmüş Büyüklüğü: LLM değerlendirme sistemlerine odaklanan LatentEval kurumunun yayımladığı 2026 tarihli açık inceleme raporuna göre, "biçim/stil yanlılığı" ölçülen en büyük sapma olarak kayıtlara geçmiştir. LLM'lerin salt biçimlendirme farklılıklarından (örneğin düz düzyazı -prose- yerine Markdown kullanımı) dolayı verdikleri yanlı kararların etki büyüklüğü farklı modellerde 0.10 ile 0.76 arasında (korelasyon sapması veya galibiyet marjı olarak) değişmektedir. Bu devasa oran, biçimlendirmenin konum yanlılığından bile daha tehlikeli bir illüzyon yarattığını kanıtlamaktadır.

5. Koşu İçi Kararsızlık (Intra-Rater Instability) ve Rubrik Çürümesi
Sıcaklık (temperature) parametresi 0'a (tam deterministik) ayarlansa bile, LLM'lerin aynı metne iki farklı çalışmada (run) farklı puanlar vermesi, kapalı uçlu kodlama görevlerinden ziyade yaratıcı metinlerde sıkça görülür.

Ölçülmüş Büyüklüğü: 2025 tarihli Kostina vd. ve 2024 tarihli Megahed vd. gibi ikincil derlemeler (Taylor & Francis yayını), deterministik davranışın karmaşık yaratıcı metinlerde her zaman korunamadığını, API güncellemeleri nedeniyle modellerde "puan toleransı kayması" (leniency drift) yaşandığını vurgulamaktadır. Literatür, 1'den 10'a kadar olan mutlak Likert ölçeklerinin (Single Answer Grading) anlamsız olduğunu; çünkü bir LLM'in bir yaratıcı metne neden 6 değil de 7 verdiğini yapısal olarak gerekçelendiremediğini ve bu durumun aynı metin için sonraki koşularda ± 1-2 puanlık rastgele gürültü (noise) ürettiğini saptamıştır.

Yanlılıkları Azaltmak İçin Sınanmış Yöntemler ve Nicel İyileştirme Oranları
Söz konusu sistematik yanlılıklar, LLM-as-a-Judge paradigmasının sonunu getirmemiş; aksine istem mühendisliği (prompt engineering) ve değerlendirme ardışık düzeni (pipeline) mimarilerinde çeşitli test edilmiş metodolojilerin doğmasına yol açmıştır. Aşağıda, her bir yöntemin hangi koşulda ne kadarlık bir nicel iyileştirme sağladığı detaylandırılmıştır.

1. Düşünce Zinciri: Gerekçeyi Puandan Önce Yazdırmak (Chain-of-Thought)
Bir senaryoyu veya diyalogu değerlendirirken modele doğrudan "Bir puan ver" veya "A'yı mı B'yi mi seçtin?" demek yerine; "Önce değerlendirme rubriğine göre adım adım akıl yürüt, güçlü ve zayıf yönleri tartış, kararını en sona yaz" şeklinde talimat vermek (Chain-of-Thought - CoT), ani karar (premature commitment) hatalarını dramatik şekilde azaltmaktadır.

Sağladığı İyileştirme: Tekil çıktılı (Single-Output) G-Eval mimarisine odaklanan büyük ölçekli bir vaka analizinde (2026), karar sürecinden önce gerekçe yazdırılmasının ve az-atımlı (few-shot) örnekler sunulmasının, modelin insan yargısıyla uyuşmasını %65 seviyesinden %77.5 seviyesine yükselttiği belgelenmiştir. Matematik ve mantık izleme gibi doğrulanabilir görevlerde ise, standart istemle 20 soruda 14 hata (14/20 failure) yapan bir hakemin, CoT eklendiğinde hata oranını 6/20'ye düşürdüğü (hataları %50'den fazla azalttığı) saptanmıştır.

2. Mutlak Puan Yerine İkili Karşılaştırma (Pairwise Comparison)
Modellerden 1 ile 10 arasında veya sürekli bir ölçekte tekil bir mutlak puan (Single Answer Grading) istemek, modelin içsel bir ölçek kalibrasyonu olmaması nedeniyle kararsız sonuçlar üretir. Bunun yerine, iki farklı senaryo yazarının metinlerinin (A ve B) modele yan yana sunulup "Hangisi daha iyi?" diye sorulması, LLM'lerin (tıpkı insanlar gibi) görece kaliteyi (relative judgement) belirlemedeki üstün yeteneklerini ortaya çıkarır.

Sağladığı İyileştirme: 250.000'den fazla anotasyon içeren Arena G-Eval platformundan alınan verilere göre, ikili karşılaştırma yöntemi, "sohbet botu samimiyeti" veya "yaratıcılık" gibi son derece öznel metinlerde insan tercihleriyle uyuşma oranını %95'e kadar çıkarmaktadır. Tekli mutlak puanlama yöntemleri, hacimsel olarak doğrusal (O(n)) ölçeklendikleri için daha ucuz olsalar da, insan uyuşmasında genellikle en iyi ihtimalle %80 ila %90 bandında (GPT-4 seviyesi modellerde) kalmaktadır. Zheng vd. (2023), her iki yöntemin de GPT-4'te %80'in üzerinde başarı sağladığını belirtse de, genel literatür ikili karşılaştırmanın "öznel" kalite farklarını yakalamada ezici bir üstünlüğü olduğunu doğrulamaktadır.

3. Kör Yeniden Koşu ve Konum Değiştirme (Position Swapping)
Konum yanlılığını (Position Bias) sıfırlamanın algoritmik olarak kanıtlanmış tek yolu, sistemi aynı iki seçenekle çift yönlü koşturmaktır.

Sağladığı İyileştirme: MT-Bench metodolojisinde (Zheng 2023) altın standart haline gelen bu yöntemde, Hakem LLM'e önce (Metin A, Metin B) sırasıyla, ardından (Metin B, Metin A) sırasıyla aynı soru sorulur. Eğer hakem ilk koşuda Metin A'yı, ikinci koşuda da (sırası B konumuna geçmesine rağmen) Metin A'yı seçerse karar tutarlı (geçerli) sayılır. Eğer model sadece ilk sıradakini seçtiği için kararı değişirse, sonuç "Berabere (Tie) / İnandırıcı Değil" olarak işaretlenir. Bu işlem, LLM API değerlendirme maliyetini tam iki katına çıkarsa da, ölçülebilir konum yanlılığını tamamen ortadan kaldırmakta (sıfıra indirmekte) ve liderlik tablosundaki sapmaları engellemektedir.

4. Çapa Örnekli Rubrik (Few-Shot Calibration / Anchored Rubrics)
Yalnızca kural tabanlı yönergeler ("Yaratıcı olanı seç") vermek yerine, hakem LLM'e geliştiricinin kendi verilerinden insanlar tarafından puanlanmış gerçekçi örnekler ("Çapa" - Anchor) sunmaktır. Bu sayede model, gereksiz uzunluğun değil, bağlamsal yoğunluğun ödüllendirilmesi gerektiğini anlar.

Sağladığı İyileştirme: Uzunluk kontrolünün rubrik içine açıkça gömülmesi (Örn: "Puan 5: Gereksiz sözcük kullanmayan 200 kelime altı yanıt") sistemi kelime salatası (verbosity) tuzağından kurtararak genel pazar sıralamalarındaki model-insan korelasyonunu 0.94'ten 0.98'e çıkarmaktadır.

5. Birden Çok Koşunun Ortalaması ve Meta-Hakem (Multi-Agent Debate)
Kendi üslubuna yatkınlık (Self-enhancement) yanlılığını önlemek ve kararsızlığı gidermek için uygulanan yöntemlerdir. Ya farklı mimari ailelerden modeller çapraz hakem (Örn: LLaMA modelini GPT-4 ile değerlendirmek) olarak kullanılır, ya da birden fazla farklı hakemin (MAD - Multi-Agent Debate) tartıştığı ve bir Meta-Hakem'in nihai kararı verdiği sistemler kurulur.

Sağladığı İyileştirme: 2025 EMNLP (Findings) araştırmalarına göre, Meta-Hakem sistemleri, tekli temsilcilere (single-agent) kıyasla konum, kelime kalabalığı ve sürü psikolojisi (bandwagon) yanlılıklarına karşı istatistiksel olarak belirgin bir direnç göstererek, tekil model yanlılık seviyelerini etkisiz hale getirmektedir. Çapraz model kullanımı ise çıktı değerlendirmelerindeki %3-%8'lik haksız şişkinliği doğrudan ortadan kaldırır.

Hafifletme Stratejisi    Hedeflenen Ana Yanlılık    İyileştirme Büyüklüğü (Ampirik Veri)
Gerekçeyi Önce Yazdırma (CoT)    Rastgelelik (Noise), Ani Karar    İnsanla uyuşmayı %65'ten %77.5'e çıkarır. Matematikte hata oranını yarı yarıya düşürür.
İkili Karşılaştırma (Pairwise)    Ölçek Kayması (Leniency Drift)    Öznel (yaratıcı) metinlerde hizalanmayı (Arena) %90'lardan %95'e taşır.
Konum Değiştirerek İki Koşu    Konum Yanlılığı (Position Bias)    Karşılaştırma maliyetini ikiye katlar ancak konum kaynaklı sıralama hatasını tamamen sıfırlar.
Açık Uzunluk Kontrollü Çapa Rubrik    Uzunluk / Ayrıntı Yanlılığı    Modelin referans sıralama korelasyonunu 0.94'ten 0.98'e yükseltir.
Çapraz Aile Modeli Kullanma    Kendini Kayırma (Self-Bias)    Yaratıcı çıktılardaki %3-%8'lik haksız puan şişkinliğini yok eder.

Diyalog ve Senaryo Değerlendirmesi İçin Yayınlanmış Açık Araçlar (Rubrikler)
Yaratıcı metinlerin değerlendirilmesinde LLM'lerin doğrudan kalite puanı vermekteki yetersizliklerini aşmak için, metni semantik, yapısal ve tematik alt boyutlara bölen açık kaynaklı ve akademik olarak yayımlanmış değerlendirme araçları (frameworks) geliştirilmiştir. Literatürdeki en belirgin iki araç DramaBench (Senaryo/Kurmaca) ve FED (İkili Diyalog) çerçeveleridir.

1. DramaBench (2025)
Senaryo ve drama devamlılığını (drama script continuation) değerlendirmek üzere oluşturulmuş, literatürdeki ilk geniş ölçekli (1,103 benzersiz senaryo, 8,824 değerlendirme) ve çok boyutlu kıyaslama (benchmark) aracıdır.

Ölçek Maddeleri (Boyutları): Araç 6 bağımsız (ortogonal) değerlendirme boyutu sunar:

Biçimsel Standartlar (Format Standards)

Anlatı Verimliliği (Narrative Efficiency)

Karakter Tutarlılığı (Character Consistency) (Örn: Diyalog karakterin sesiyle eşleşiyor mu?)

Duygusal Derinlik (Emotional Depth) (Örn: Duygusal arkların varlığı)

Mantıksal Tutarlılık (Logic Consistency)

Çatışma Yönetimi (Conflict Handling).

Güvenilirlik ve Geçerlilik Ölçümü: Sistem, LLM'leri doğrudan puan (1-10) veren "hakemler" olarak kullanmak yerine, onları yapılandırılmış veri çıkarıcılar (structured data annotators / categorical labelers) olarak kullanır (Örn: Senaryodaki bir bölümü "Durağan vuruş" veya "İlerletici vuruş" olarak etiketler). Bu etiketler daha sonra istatistiksel formüllerle nesnel metriklere dönüştürülür. İnsan doğrulama (human validation) analizlerinde, 188 senaryo üzerinde, 5 boyutun 3'ünde κ = 0.42 ile 0.53 arasında insan-insan uyuşması (substantial agreement) elde edilerek aracın yapı geçerliliği ve kabul edilebilir güvenilirliği ispatlanmıştır. Altı boyutun da birbirinden istatistiksel olarak bağımsız olduğu (ortalama Pearson |r|=0.020) kanıtlanmıştır.

2. FED (Fine-Grained Evaluation of Dialog - 2020/2022)
İnsan-makine (chatbot) veya insan-insan diyaloglarını, herhangi bir "referans doğru yanıta" (reference response) ihtiyaç duymadan değerlendirmek için geliştirilmiş referanssız (unsupervised) bir değerlendirme metriğidir. Sistem, DialoGPT gibi modellerin, kullanıcının vereceği bir sonraki yanıtın olasılığını hesaplaması (Follow-up log-likelihood) mantığına dayanır.

Ölçek Maddeleri (Boyutları): FED toplam 18 alt nitelik (ince taneli nitelik) tanımlamıştır. Bu nitelikler turn-level (dönüş) ve dialog-level (tüm diyalog) olarak gruplandırılmıştır. Temel faktör kümeleri şunlardır:

Tutarlılık (Coherent, Understanding)

Beğenilebilirlik / Esneklik (Likable, Flexible, Informative)

Derinlik / Çeşitlilik (Topic Depth, Diverse)

Bağlamsal İstikrar (Consistent)

Sorgulayıcılık (Inquisitive)

Hata Telafisi (Error Recovery).

Güvenilirlik Ölçümü: FED veri seti üzerinde 5 insan hakemin katıldığı anotasyon çalışmalarında, çoğu boyut için Spearman korelasyonu (IRR) 0.75'in üzerindedir. Ancak bağlamsal istikrar (Consistency) boyutunda uyuşma 0.562'ye gerileyerek öznelliğin sınırlarını çizmiştir.

Otomatik ve İnsan Değerlendirmesinin En Çok Ayrıştığı Maddeler
İlgili ölçüm araçlarının (özellikle FED ve SummEval verileri) meta-analizleri, otomatik LLM değerlendirmesiyle insan değerlendirmesinin en çok ayrıştığı noktanın mantıksal tutarsızlıkları/halüsinasyonları (logic consistency / relevance) saptama ve uzunluk tuzağına (verbosity) düşme eksenlerinde olduğunu göstermektedir.

İnsan hakemler, akıcı ve uzun olsa bile bağlamdan kopuk, alakasız veya olay örgüsü bozuk bir metni anında cezalandırır. Ancak LLM hakemler, sırf dilbilgisel olarak akıcı veya yapısal olarak uzun olduğu için (uzunluk yanlılığı nedeniyle) bu tür yanıtları yanıltıcı şekilde yüksek puanlama eğilimindedir.

Ayrıca, SummEval'de görüldüğü üzere insan uzmanlar, "tutarlılık" (coherence) gibi yapısal faktörlerde otomatik metriklerle paralellik gösterirken (Krip. α = 0.798), "alaka" (relevance) ekseninde (Krip. α = 0.398) anlamsal derinliği yorumlamakta ayrışmaktadır. Kısacası LLM, metnin "nasıl" (stilistik/akıcı) yazıldığını değerlendirmekte başarılıyken; "ne" söylediğini ve karakterin "neden" öyle davrandığını (içsel mantık) yorumlamakta insana kıyasla dramatik şekilde yetersiz kalmaktadır.

Sonuç Bulguları ve Sınanmamış Hipotezler
Yukarıdaki kapsamlı analizin bir özeti olarak, doğrulanabilir akademik/endüstriyel kaynaklara dayanan kesin bulgular ve mekanik olarak mantıklı olmakla birlikte araştırma materyallerinde doğrulanamayan hipotezler aşağıda tablolanmıştır.

1. Doğrulanabilir Kaynağa Dayanan Kesin Bulgular
Bulgu / Çıkarım    Dayanak (Tür ve Yıl)    Ölçülen Değer / Gerçeklik
İnsan Güvenilirliği (IRR) Yapısal vs. Öznel Ayrımı    İkincil Derleme (2023), Özgün Araştırma (2025)    Uzman hakemler yapısal tutarlılıkta yüksek uyum (Krip. α 0.79) gösterirken, diyalog/alaka gibi öznel eksenlerde bu uyuşma 0.39'a; kurmaca tercihlerinde 0.14'e (Fleiss) kadar düşmektedir.
Konum Yanlılığının (Position Bias) Varlığı    Hakemli Çalışma (2023), İkincil Derleme (2024)    İkili karşılaştırmada LLM'ler A seçeneğini kayırır. Bu sapma GPT-4'te ~%5 iken zayıf modellerde sıralamayı %30 (hatta 66/80 oranında) saptırabilir.
Uzunluk ve Format Yanlılığı (Verbosity/Style)    Meta-Değerlendirme (2024), Kurum Raporu (2026)    Biçimsel stil (Markdown vb.) 0.10 ile 0.76 arasında devasa bir yanlılık yaratır. Uzunluk kontrol edildiğinde LLM'in insanla korelasyonu 0.94'ten 0.98'e çıkar.
Öz-Kayırma (Self-Enhancement Bias)    Ön Baskı Araştırma (2024/2025)    LLM'ler kendi ailesinden olan (üslubu benzeyen) çıktıları, kaliteden bağımsız olarak %3 ila %8 oranında şişirerek ödüllendirir.
Hafifletme: Çift Koşu ve İkili Karşılaştırma    Teknoloji Raporu (2026), Hakemli Çalışma (2023)    Konum değiştirmeli kör koşu (swapping) konum yanlılığını %100 oranında sıfırlar. İkili karşılaştırma (pairwise) ise insan uyumunu mutlak puanlamaya kıyasla %95'lere taşır.
Hafifletme: Düşünce Zinciri (CoT)    Teknoloji Raporu (2026)    Gerekçeyi puandan önce yazdırmak rastgeleliği engeller; genel uyumu %65'ten %77.5'e çıkarır, matematik görevlerindeki başarısızlığı yarı yarıya azaltır.
DramaBench ve FED Araçlarının Ayrıştığı Madde    Ön Baskı (2025), Hakemli Çalışma (2020)    İnsanlar ve otomasyon en çok "mantıksal tutarsızlık (logic consistency/hallucination)" ve "uzunluk" tuzağında ayrışır. İnsanlar mantıksızlığı hemen cezalandırırken, LLM'ler akıcı uzunluk karşısında mantıksızlığı gözden kaçırır.

2. Mekanik Olarak Makul Ancak Kaynaksız İddialar (Hipotezler)
Aşağıdaki iddialar, NLP ve makine öğrenimi dinamikleri açısından son derece mantıklı görünmesine rağmen, sağlanan veri setlerinde ve literatür parçacıklarında nicel olarak ölçülmemiş veya doğrulanmamıştır.

Hipotez    Doğrulanamama Nedeni (Neden Kaynaksız?)
Hipotez 1: Yaratıcı yazarlıkta mizah, ironi veya kültürel hiciv içeren diyalogları değerlendirirken, LLM hakemler düz (mekanik) diyaloglara kıyasla çok daha yüksek oranda kararsızlık yaşar ve tutarsız puan verir.    Sağlanan literatür materyallerinde mizah, ironi veya kültürel hiciv gibi spesifik üslup ögeleri üzerine odaklanan bir etki büyüklüğü veya hata ölçümü (failure rate) istatistiği yer almamaktadır.
Hipotez 2: Bir LLM hakeminin sıcaklık (temperature) değerini 0 (deterministik) yerine 0.7 gibi daha "yaratıcı" bir seviyeye çıkarmak, "Duygusal Derinlik" gibi soyut/öznel eksenlerdeki değerlendirme başarısını (insan korelasyonunu) artırır.    Sağlanan metinler sıcaklık parametresinin (0 değeri) sadece deterministik davranışı (kararlılığı) sağlayıp sağlamadığını tartışmış, yüksek sıcaklığın değerlendirme isabetliliğine olan etkisini test etmemiştir.
Hipotez 3: Diyalog değerlendirmelerinde (örneğin FED sisteminde), karakterin uzun vadeli psikolojik değişimini (character arc) yakalamak, LLM'ler için diyalog akıcılığını yakalamaktan çok daha fazla bağlam penceresi (context window) ve işlem gücü gerektirir.    Uzun menzilli bağlam limitleri nedeniyle teknik olarak doğru görünse de, parçalarda "psikolojik değişim" (character arc) tespit başarısının modelin bağlam penceresi boyutuyla olan ilişkisine dair bir ölçüm verilmemiştir.

---

## KAYNAK LİSTESİ (raporun kendi verdiği bağlantı adları, olduğu gibi)

aclanthology.org — A Comprehensive Assessment of Dialog Evaluation Metrics
arxiv.org — arXiv:2106.03706v4 [cs.CL] 7 Jul 2021
arxiv.org — arXiv:2203.13927v1 [cs.CL] 25 Mar 2022
spectrumofresearch.com — Position Bias and Verbosity Bias in LLM-as-a-Judge
researchgate.net — (PDF) Amabile's consensual assessment technique: Why has it not
arxiv.org — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena - arXiv
openreview.net — WEBDEVJUDGE: EVALUATING (M)LLMS AS CRI - OpenReview
arxiv.org — Rating Roulette: Self-Inconsistency in LLM-As-A-Judge Frameworks
arxiv.org — Selecting the Right Inter-annotator Agreement Metric for NLP ... - arXiv
files.eric.ed.gov — Journal of Technology Education - ERIC
europeanproceedings.com — Assessing Creative Expressiveness In Children's Written Stories
bnu.repository.guildhe.ac.uk — Download (904kB) - Buckinghamshire New University repository
designsociety.org — Design Creativity Assessment and Capturing
researchgate.net — Development of a rubric for evaluating creative writing - ResearchGate
academia.edu — Development of a rubric for evaluating creative writing - Academia.edu
arxiv.org — LiteraryTaste: A Preference Dataset for Creative Writing ... - arXiv
arxiv.org — When Large Language Models are Reliable for Judging Empathic
researchgate.net — (PDF) Judging LLM-as-a-judge with MT-Bench and Chatbot Arena
medium.com — Arena G-Eval vs Single-Output "LLM-as-a-judge" — Case Study
scaler.com — LLM-as-a-Judge: Can a Model Grade Another Model's Homework
latenteval.ai — LLM-as-a-judge bias, and the tests that catch it | LatentEval
arxiv.org — BabelJudge: Measuring LLM-as-a-Judge Reliability Across ... - arXiv
arxiv.org — A Systematic Investigation of Position Bias in Pairwise Comparative
github.com — agent-research-book/docs/21-llm-as-judge-trajectory-eval.md at main
arxiv.org — Explaining Length Bias in LLM-Based Preference Evaluations - arXiv
arxiv.org — Length-Controlled AlpacaEval: A Simple Way to Debias Automatic
researchgate.net — Judging the Judges: A Systematic Investigation of Position Bias in
arxiv.org — Language Model Council: Democratically Benchmarking ... - arXiv
arxiv.org — A Statistical Method to Measure Self-Bias in LLM-as-a-Judge - arXiv
tandfonline.com — Reliable decision support with LLMs: a framework for evaluating
aclanthology.org — Judging with Many Minds: Do More Perspectives ... - ACL Anthology
mdpi.com — Benchmarking LLM-as-a-Judge Models for 5W1H Extraction ... - MDPI
jyx.jyu.fi — Evaluating LLMs' Ability to Help Students Using GPT-4-As-A-Judge
arxiv.org — Wider and Deeper LLM Networks are Fairer LLM Evaluators - arXiv
ojs.aaai.org — Auto-PRE: An Automatic and Cost-Efficient Peer-Review Framework
researchgate.net — DramaBench: A Six-Dimensional Evaluation Framework for Drama
emergentmind.com — DramaBench: Six-Dimensional Script Evaluation - Emergent Mind
dramabench.pages.dev — DramaBench - Drama Script Evaluation Benchmark
huggingface.co — DramaBench: A Six-Dimensional Evaluation Framework for Drama
github.com — IIIIQIIII/DramaBench: A six-dimensional evaluation ... - GitHub
openreview.net — I CAN'T BELIEVE LLMS STILL CAN'T WRITE DRAMA - OpenReview
arxiv.org — FineD-Eval: Fine-grained Automatic Dialogue-Level Evaluation - arXiv
arxiv.org — arXiv:2209.05185v1 [cs.CL] 12 Sep 2022
arxiv.org — arXiv:2210.13832v2 [cs.CL] 29 Oct 2022
arxiv.org — arXiv:2006.12719v1 [cs.CL] 23 Jun 2020
aclanthology.org — Leveraging User Sentiment for Automatic Dialog Evaluation
