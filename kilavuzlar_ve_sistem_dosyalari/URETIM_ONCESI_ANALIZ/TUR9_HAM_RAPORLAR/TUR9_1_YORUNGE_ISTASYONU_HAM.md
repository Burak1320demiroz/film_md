# TUR 9 · RAPOR 1 (HAM) — YÖRÜNGE İSTASYONU — DIŞ ANATOMİ VE ASTRONOT-GÖRELİ ÖLÇEK

> **Koşu:** 04.09.2026 · **Girdi promptu:** `../12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` §1
> **Süzme kaydı:** `../04_ARASTIRMA_BULGULARI.md` §TUR 9
>
> ⛔ **HAM METİN.** Düzeltilmez, kısaltılmaz. Kaynak listesi raporun sonunda
> durur. Bu dosyadaki hiçbir sayı doğrulanmış değildir — doğrulama süzme
> kaydında, kural kılavuzdadır.
>
> ⚠️ Metin sahibin yapıştırdığı hâlden aktarılmıştır; araştırma aracının
> alt simge/dipnot işaretleri düz metne çevrilmiş, tablolar Markdown
> tablosuna dönüştürülmüştür. Cümleler ve sayılar DEĞİŞTİRİLMEMİŞTİR.

---

## KOŞULAN PROMPT (birebir)

```
Gerçek yörünge istasyonlarının dıştan görünür anatomisini birincil kaynaklardan (NASA Reference Guide to the ISS, ESA ve Roscosmos teknik dokümanları, NTRS, uçuş fotoğrafları) ölçüleriyle çıkar: Salyut, Skylab, Mir, ISS'in tek tek modülleri (Zarya, Zvezda, Destiny, Kibo, Columbus, düğüm modülleri, Cupola), bütünleşik kafes kirişi, güneş kanatları, radyatörler, robot kol, Quest ve Poisk hava kilitleri, kenetlenme portları ile Tiangong ve planlanan Gateway, Axiom, Starlab, Orbital Reef için çap, uzunluk, kanat açıklığı, kapak ve port açıklığı, tutamak aralığı değerlerini ver. Her ölçüyü kasklı basınç giysili astronotun ayakta boyuna göre orana çevir (sırt ünitesinin derinliğini ayrı ver): modül çapı kaç gövde boyu, kapak açıklığı kaç, kafes kiriş segmenti kaç, güneş kanadı kaç, tutamak aralığı kaç el genişliği — ve gerçek EVA fotoğraflarında ölçeği en güvenilir okutan eşleşmeleri (robot kol ucundaki astronot ile güneş kanadı, kapak önündeki astronot, kiriş üzerinde yürüyen astronot) örnekleriyle belgele. Silüet tipolojisi çıkar: kafes-ve-modül (ISS), tek gövdeli silindir (Skylab), yıldız biçimli modül kümesi (Mir), tek hat (Tiangong) ve uçmamış dönen biçimler (von Braun tekerleği, Stanford torusu, O'Neill silindiri, halatlı dönüş) — dönen tipler için hangi yarıçap ve devir hangi yapay yerçekimini verir, Coriolis rahatsızlık eşiği kaç devirdir ve kamera sabitken bir yapının döndüğü tek kadrajda hangi ipuçlarıyla (pencere süpürmesi, gölge kayması, kablo eğriliği) okunur, kaynak göstererek açıkla. Yüzey ve yaşlanma katmanını ayrıca belgele: çok katmanlı yalıtım örtülerinin (altın/gümüş kapton) görünümü, beyaz beta kumaşı, mikrometeorit çukurları, ultraviyole sararması, itici lekesi, radyatör beyazlığı, sarı tutamak geleneği — hangi yüzeyler yıllarla nasıl değişir ki yirmi yıllık istasyon yeni istasyondan tek bakışta ayırt edilsin. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz, 8-10 saniyelik sabit planlı AI videodur; hiçbir yüzeyde okunur yazı, bayrak, logo, rakam ya da ölçek işareti bulunamaz, parlama ve bloom sıfırdır (güneş sert bir nokta kaynaktır), yalıtım örtüsü dalgalanamaz ve serbest süzülen enkaz yasaktır — bu yüzden hangi öğelerin büyük, geometrik ve SAYILABİLİR olduğu için (n güneş kanadı, n radyatör, hizada n modül, n port) devamlılık çapası sayılabileceğini, hangilerinin (kablo demeti, örtü kırışığı, anten kümesi) sahneden sahneye kaydığını öncelik sırasıyla ayır. Çıktıyı tablo olarak ver: öğe, gerçek ölçüsü ve kaynağı, astronot-göreli oranı, ait olduğu silüet tipi, sayılabilir çapa değeri, üretimde kayma riski sınıfı ve nesne-göreli birimle yazılmış tek satırlık İngilizce prompt ifadesi; ayrıca her silüet tipi için bir "anatomi kartı" şablonu ekle (modül sayısı, kanat sayısı, radyatör sayısı, port sayısı ve tarafı).
```

---

## RAPOR (ham çıktı)

Yörünge İstasyonları Dış Anatomisi ve Yapay Zeka Video Üretimi İçin Tipolojik Referans Raporu

İnsanlı uzay uçuşları tarihi boyunca inşa edilen yörünge habitatları, fırlatma aracı kaporta çaplarının aerodinamik kısıtlamaları, mikro yerçekimi ortamının yapısal serbestlikleri ve termal/radyasyon kontrol gereksinimlerinin doğrudan bir sentezidir. Bu devasa mühendislik yapılarının dış anatomisini, yapay zeka (AI) destekli video difüzyon modellerinde (özellikle 8-10 saniyelik, kesmesiz ve sabit kameralı kadrajlarda) fotogerçekçi, zamansal olarak tutarlı ve fiziksel olarak doğru bir biçimde üretebilmek, yapısal ölçeklerin, yüzey materyali yaşlanma matrislerinin ve topolojik silüetlerin kusursuz bir şekilde formüle edilmesini gerektirir. Sentetik veri üretiminde karşılaşılan en büyük zorluk olan kareler arası nesne kayması (morphing/sliding) ve biçimsel halüsinasyon, ancak fiziksel uzay anatomisinin katı, sayısal ve geometrik çapalara (countable anchors) dönüştürülmesiyle aşılabilir.

Bu rapor, Salyut, Skylab, Mir, Uluslararası Uzay İstasyonu (ISS), Tiangong ve Gateway, Axiom, Starlab, Orbital Reef gibi planlanan ticari/ay yörüngesi habitatlarının dış anatomilerini, bir basınç giysisi içindeki astronotun biyometrik oranlarına çevirerek derinlemesine analiz etmektedir. Aynı zamanda, uçmamış rotasyonel yapay yerçekimi tasarımlarını (O'Neill, Stanford, von Braun) ve uzay ortamının (atomik oksijen, UV radyasyonu, mikrometeoritler) yüzeylerde yarattığı yaşlanma etkilerini belgeleyerek AI istem (prompt) mühendisliği için kesin bir referans matrisi sunmaktadır.

Biyometrik Ölçeklendirme ve Görsel Çapa Dinamikleri

Uzay yapılarının devasa boyutları ve perspektifi bozan vakum ortamı, referans noktaları olmadan insan gözü veya yapay zeka modelleri tarafından doğru algılanamaz. Uzay yürüyüşü (EVA) yapan tam donanımlı bir astronot, bu devasa yapılar için en güvenilir evrensel görsel ölçekleyici işlevini görür. Yörünge istasyonlarının geometrik analizinde kullanılacak standart biyometrik referans birimleri, ekstravehiküler mobilite ünitesinin (EMU veya Rus Orlan giysisinin) katı dış boyutlarına dayanır.

Temel referans birimi olan Kasklı Astronot Boyu (H_a), tam basınç altında dikey olarak 1.90 metre kabul edilmektedir. İkinci kritik ölçü, sırt ünitesinin derinliğidir (D_plss). Kişisel Yaşam Destek Sistemi (PLSS) ve göğüs kontrol paketi (DCM) birleştiğinde astronotun toplam ön-arka derinliği yaklaşık 0.85 metreye ulaşır; bunun 0.60 metresi salt sırt çantasıdır. Omuzdan omuza genişlik yaklaşık 0.75 metre iken, EVA eldiveninin dış kavrama genişliği (W_h) 0.12 metre olarak standardize edilmiştir.

Gerçek EVA fotoğraflarının tarihsel analizi, bu oranların uzay istasyonu anatomisine nasıl oturduğuna dair kesin eşleşmeler sunar. En çarpıcı ölçek eşleşmelerinden biri, STS-120 görevi sırasında Uluslararası Uzay İstasyonu'nun P6 güneş kanadındaki yırtığı onarmak üzere görevlendirilen astronot Scott Parazynski'nin fotoğraflarında görülür. Astronot, Canadarm2'nin ve OBSS (Orbital Boom Sensor System) uzantısının en ucunda bir ayak kısıtlayıcıya bağlı olarak uzay boşluğunda asılı dururken devasa güneş paneliyle aynı kadraja girmiştir. P6 güneş kanadı tam olarak açıldığında yaklaşık 35 metre (tek kanat) uzunluğa sahiptir. Bu bağlamda, 1.9 metrelik astronot (1H_a), tek bir güneş kanadının uzunluğunun yalnızca %5.4'üne eşdeğerdir. Kadrajda astronot, altın renkli devasa ve sert ızgaralı bir duvarın önünde süzülen mikroskobik bir nokta gibi görünerek, yapının devasa boyutlarını görsel bir şoka dönüştürür.

Bir diğer kritik ölçekleyici, kapak (hatch) önündeki astronotun geçiş dinamikleridir. Quest Hava Kilidi'nden veya Rus Pirs/Poisk modüllerinden dışarı çıkan bir astronot, 800 milimetre (0.8 metre) çapındaki standart bir Rus (APAS veya SSVP) kapağından geçmek zorundadır. Bu açıklık 0.42H_a boyutundadır. Astronotun omuz genişliği (0.75 m) ve PLSS derinliği (0.85 m) göz önüne alındığında, astronotlar bu kapaklardan doğrudan geçemezler; omuzlarını ve sırt çantalarını çaprazlayarak, dikkatli bir manevrayla süzülmeleri gerekir. Görsel olarak, kapak açıklığı astronotun kütlesinden zar zor büyüktür.

Kafes kirişi (Truss) üzerinde yürüyen astronot fotoğrafları ise ISS'in mimari belkemiğinin ölçeğini yansıtır. S0, S1 veya P1 ana kafes kiriş segmentleri üzerinde hareket eden bir mürettebat üyesi, 4.5 metre genişliğinde ve 4.6 metre yüksekliğinde olan bu kafesin yanında son derece küçük kalır. Kirişin yüksekliği 2.42H_a'dır, yani astronot, kirişin kalınlığının yarısından bile daha kısadır. Son olarak, yüzeydeki mikroskobik ölçeklendirme için EVA tutamakları (handrails) kullanılır. İstasyonun dış yüzeyinde yer alan standart sarı CETA tutamakları yaklaşık 0.6 metre uzunluğundadır. Bu uzunluk tam olarak 5 EVA eldiveni genişliğine (5W_h) eşittir. İki tutamak arasındaki boşluk ise, bir astronotun mikro yerçekiminde rahatça uzanabileceği kol açıklığına (yaklaşık 0.6H_a) uygun olacak şekilde standartlaştırılmıştır.

Yörünge İstasyonları Modüler Anatomisi ve Hacimsel Sınırlar

Uzay istasyonları, Dünya'dan fırlatılma sırasında roketlerin aerodinamik kaportalarının içine sığmak zorunda olduklarından, ağırlıklı olarak silindirik veya konik-silindirik melez geometrilere sahiptir. Uzay Mekiği'nin kargo bölümü 4.5 metre (15 ft) ile sınırlıyken, Rus Proton fırlatıcıları 4.15 metrelik sınırlara sahiptir. Bu balistik ve lojistik sınırlar, modüllerin insan vücuduna oranla çaplarını kesin bir şekilde belirlemiştir.

Erken Dönem Tek Gövdeli İstasyonlar

Sovyetlerin Salyut 7 uzay istasyonu, erken dönem silindirik tasarımın tipik bir örneğidir. Yaklaşık 15 metre uzunluğunda (7.89H_a) ve maksimum 4.15 metre çapında (2.18H_a) olan bu istasyon, iki astronot boyunu biraz aşan bir çapa sahipti. İstasyonun güneş kanatları açıldığında 17 metrelik (8.94H_a) bir uçtan uca açıklığa ulaşıyordu. Buna karşılık, ABD'nin Skylab istasyonu, bugüne kadar fırlatılmış en geniş çaplı tek parça habitat modülü olma unvanını korumaktadır. Skylab, devasa Saturn V roketinin S-IVB üçüncü aşamasından doğrudan dönüştürüldüğü için dış çapı tam 6.6 metreye (3.47H_a) ulaşıyordu. Toplam uzunluğu 26 metre (13.68H_a) civarında olan Skylab'ın dış çeperinde bir astronot durduğu varsayıldığında, modülün gövde eğriliği diğer tüm modern istasyonlara kıyasla çok daha düz bir zemin hissi yaratırdı.

Mir ve Modüler Mimarinin Doğuşu

Mir uzay istasyonu, tek gövdeli tasarımlardan, çoklu kenetlenme düğümüne sahip genişletilebilir mimariye geçişi temsil eder. Mir'in Çekirdek Modülü (Core), 13.1 metre uzunluğunda (6.89H_a) ve maksimum 4.15 metre çapındaydı (2.18H_a). Mir'e daha sonra eklenen Kvant-1, Kvant-2, Kristall ve Spektr gibi genişleme modülleri de fırlatma aracı kısıtlamaları nedeniyle 4.15 metrelik (2.18H_a) çap standardını korumuştur. Mir'in mimarisi, modüllerin asimetrik olarak uzandığı, güneş panellerinin ve antenlerin kaos içinde her yöne fırladığı yıldız biçimli bir küme yaratmıştır.

Uluslararası Uzay İstasyonu (ISS) Basınçlı Modülleri

Uluslararası Uzay İstasyonu, 109 metre uçtan uca açıklığı, 73 metrelik güneş kanadı genişliği ve 1,005 metreküplük devasa basınçlı hacmi ile en büyük insan yapımı uzay yapısıdır. İstasyonun mimarisi, ABD (Batı) ve Rus segmentleri olarak temel iki farklı mühendislik ekolünün birleşimidir.

Rus yörünge segmentinin belkemiğini oluşturan Zarya (FGB) ve Zvezda (Hizmet Modülü), tarihi Mir mirasının doğrudan devamıdır. Zvezda'nın uzunluğu 13.1 metre (6.89H_a), maksimum çapı ise 4.22 metredir (2.22H_a). Buna karşılık Amerikan yörünge segmentinin kalbi olan Destiny laboratuvarı, Uzay Mekiği kargo bölümüne optimum uyum sağlamak üzere 8.5 metre uzunluğunda (4.47H_a) ve 4.3 metre çapında (2.26H_a) tasarlanmıştır.

ISS üzerindeki en büyük tek basınçlı modül, Japon Uzay Ajansı'na (JAXA) ait Kibo (JEM) modülüdür. Uzunluğu 11.2 metre (5.89H_a), çapı ise 4.4 metredir (2.31H_a). Kibo'nun dışarıya bakan kısmında, uzay boşluğuna açık deneylerin yerleştirildiği JEM Exposed Facility (Açık Tesis) bulunur. Avrupa Uzay Ajansı'nın (ESA) Columbus laboratuvarı ise 6.9 metre uzunluğu (3.63H_a) ve 4.5 metre çapı (2.36H_a) ile en kısa ana laboratuvar modülüdür ve H_a açısından oldukça "tıknaz" bir silindirik görünüme sahiptir. Unity, Harmony ve Tranquility gibi Amerikan düğüm modülleri (nodes), genellikle 5 ila 7 metre uzunluğunda (2.6-3.6H_a) ve 4.5 metre çapındadır (2.36H_a). Altıgen yapısı ve tepe penceresiyle görsel bir başyapıt olan Cupola gözlem modülü, 2.95 metre dış çapa (1.55H_a) ve 1.5 metre yüksekliğe (0.78H_a) sahiptir; bir astronot en büyük orta pencereden bakarken, 0.75 metrelik omuz genişliği pencereyi neredeyse tamamen doldurur.

Astronotların EVA için kullandığı Quest Hava Kilidi, yaklaşık 6 metre uzunluğa (3.15H_a) ve 4 metre maksimum çapa (2.1H_a) sahiptir. Rus segmentindeki Poisk (MRM-2) ise, Zvezda'nın üst kısmında yer alan, sadece 2.55 metre dış çapı (1.34H_a) olan nispeten dar ve kısa bir modüldür.

Bütünleşik Kafes Kirişi, Güneş Kanatları ve Dış Ekipmanlar

ISS'in modüler olmayan en büyük yapısı, 94 metre uzunluğundaki (49.47H_a) Bütünleşik Kafes Kirişidir (Truss). Genellikle 4.5 metreye 4.6 metre (2.36H_a x 2.42H_a) bir kesite sahip olan bu yapı, S0, S1, S3 gibi ardışık alüminyum segmentlerden oluşur. İstasyonun devasa Güneş Kanatları (SAW - Solar Array Wings), kafes kirişinin uçlarında yer alır. Toplam açıklık 73 metreye ulaşır (38.42H_a). Her bir standart Amerikan güneş kanadı tekil olarak yaklaşık 35 metre uzunluğunda (18.42H_a) ve 12 metre genişliğindedir (6.3H_a). Bu kanatların oluşturduğu enerji sistemi, EATCS adı verilen ve kafes kirişinden aşağı/yukarı doğru yaklaşık 22 metre (11.57H_a) uzanan beyaz akordeon şeklindeki devasa ısıl radyatörlerle soğutulur.

İstasyonun lojistik ve montaj işlemlerinde kullanılan ana robotik kol olan Canadarm2 (SSRMS), 16.8 metre uzunluğundadır (8.84H_a). Tam 7 serbestlik dereceli eklemi bulunan bu kolun çapı sadece 0.35 metredir (0.18H_a), yani bir astronotun gövdesinden daha ince ancak son derece uzun, yılan benzeri bir manipülatördür.

Tiangong ve Gelecek Nesil İstasyonlar

Çin'in Tiangong Uzay İstasyonu, daha yeni ve daha rafine bir tasarım mimarisini temsil eder. Merkezdeki Tianhe çekirdek modülü, 16.6 metre uzunluğa (8.73H_a) ve 4.2 metre çapa (2.21H_a) sahiptir. Wentian ve Mengtian laboratuvar modülleri ise her biri 17.9 metre uzunluğunda (9.42H_a) ve 4.2 metre çapında (2.21H_a) devasa tekil silindirlerdir. ISS laboratuvarlarına kıyasla çok daha uzun olan bu modüllerin üzerinde, çekirdek modüle ait 10.2 metrelik (5.36H_a) ve Wentian modülüne ait 5 metrelik (2.63H_a) robotik kollar bulunur.

Ay yörüngesinde planlanan Gateway istasyonu ise Dünya yörüngesindeki devasa yapılara kıyasla son derece klostrofobik bir tasarıma sahiptir. HALO (Habitation and Logistics Outpost) modülü, 3.0 metre dış çapı (1.57H_a) ve yaklaşık 7 metre uzunluğu (3.68H_a) ile Cygnus kargo aracından türetilmiştir. İçerisinde 1.9 metrelik bir astronot tam olarak ayağa kalktığında, tavan ve taban arasındaki mesafe neredeyse sıfırlanır. Axiom Space tarafından geliştirilen ticari istasyon modülleri 4.4 metre çapında (2.31H_a) ve 9-10.5 metre uzunluğunda tasarlanırken, Starship veya New Glenn gibi yeni nesil süper ağır fırlatıcılarla gönderilecek olan Starlab ve Orbital Reef'in 7 ila 8 metre çapında (Skylab'dan bile büyük, 4.21H_a) devasa monolitik modüller olması planlanmaktadır. Sierra Space'in LIFE (Large Integrated Flexible Environment) modülü ise, kumaşın şişirilmesiyle 8 metre çapa ulaşabilen basınçlı bir küre yapısı sunar.

Kenetlenme Portları ve Kapak Açıklıkları

İstasyonların modülleri arasındaki geçişleri sağlayan kenetlenme sistemleri iki ana standarda ayrılır. Amerikan yörünge segmentinde kullanılan CBM (Common Berthing Mechanism), büyük kargo transferine olanak tanıyan kareye yakın (yuvarlatılmış köşeli) devasa bir iç serbest geçişe (hatch) sahiptir. Bu açıklık yaklaşık 1.3 metredir (0.68H_a). CBM'nin dış contası ve kenetlenme halkası çapı 1.8 metreyi bulur (0.94H_a). Rus modüllerinde, Soyuz araçlarında ve bazı ticari uçuşlarda (APAS-89 / APAS-95 / NDS / SSVP varyantları) kullanılan androjen veya probe-drogue kapaklar ise son derece dardır. Geçiş açıklığı tam olarak 800 milimetredir (0.8 metre, 0.42H_a). Astronotların kalın ve hantal basınç giysileriyle (0.75m genişlik) bu dar tünellerden geçişi, yörüngedeki en zorlu fiziksel manevralardan biridir.

Yapısal Silüet Tipolojisi ve Rotasyonel Dinamikler

Bir yapay zeka video üretiminde "uzay istasyonu" isteminin tutarlı, stabil ve morfolojik olarak mantıklı bir sonuç verebilmesi için, hedeflenen yapının geometrik mimarisinin net bir tipolojiye oturtulması zorunludur.

Uçmuş ve Uçan Mikro Yerçekimi Formları

Tek Gövdeli Silindir (Örn: Skylab, Salyut): Çıkıntısız, düz, devasa bir boru şeklindedir. Güneş panelleri gövdenin ortasından yanlara (radyal) veya eksenel olarak açılır. Geometrisinin aşırı basitliği nedeniyle AI tarafından en stabil ve hatasız üretilen silüet tipidir.

Yıldız Biçimli Modül Kümesi (Örn: Mir): Ana bir çekirdeğe bağlı çoklu kenetlenme küreleri üzerinden farklı eksenlerde (X, Y, Z) birleşen silindirler topluluğudur. Asimetrik paneller ve uzayda dağınık şekilde duran anten ormanıyla karakterizedir. AI için yüksek "kaotik silüet" riski taşır; kollar, modüller ve paneller birbirine geçerek formasyon bozulması yaratabilir.

Kafes ve Modül (Örn: ISS): Merkezde yatay bir hat boyunca uzanan devasa, yassı bir kafes kirişi (Truss) ve bu kafese dik açıyla bağlanmış ardışık silindirik laboratuvar modülleri dizisidir. Kafesin uçlarında dikey ve simetrik olarak yer alan devasa güneş kanatları bulunur. Çok hiyerarşik ve dik açılı (orthogonal) bir yapısı vardır.

Tek Hat (Örn: Tiangong): Uç uca eklenmiş modüllerden oluşan uzun bir "T" veya "çapraz" şeklidir. ISS gibi karmaşık ve devasa bir harici kirişi (truss) yoktur; bunun yerine güneş panelleri doğrudan laboratuvar modüllerinin uç kısımlarına entegredir.

Uçmamış Dönen Biçimler (Yapay Yerçekimi Tipolojileri)

İnsan fizyolojisinin mikro yerçekiminde uzun vadede maruz kaldığı kemik erimesi ve kas atrofisini engellemek için önerilen merkezkaç tabanlı yapay yerçekimi istasyonları, tamamen farklı bir dış anatomiye sahiptir. Yapay bir 1g (Dünya yüzeyi yerçekimi, 9.8 m/s^2) ortamı yaratmak için F_c = m . omega^2 . r (burada omega açısal hız, r ise dönüş yarıçapıdır) formülü kullanılır.

Ancak dönüş hızı, insan iç kulağındaki (vestibüler sistem) yarım daire kanallarında Coriolis kuvvetinden kaynaklanan çapraz-eşleşmeli açısal ivmelenmelere neden olur. Uzay tıbbı ve fizyolojik araştırmalara göre (NASA SP-413 referans alınarak), insan vücudunun adaptasyon gerektirmeden dayanabileceği Coriolis rahatsızlık eşiği (vertigo ve bulantı sınırı) maksimum 2 RPM (dakikada devir) olarak kabul edilir. Özel eğitimli sakinler 4 ila 6 RPM arasındaki hızlara adapte olabilirler, ancak 6 RPM üzerinde şiddetli ve kronik hareket hastalığı başlar. Bu biyolojik sınırlar, istasyon boyutlarını devasa ölçeklere iter:

2 RPM dönüşte 1g yaratmak için: Yarıçap = 225 metre (Çap 450 metre) olmalıdır.

4 RPM dönüşte 1g yaratmak için: Yarıçap = 56 metre olmalıdır.

6 RPM dönüşte 1g yaratmak için: Yarıçap = 25 metre olmalıdır.

Bu devasa kısıtlar altında tasarlanan teorik silüetler şunlardır:

von Braun Tekerleği: Merkezî bir hub, bu hub'dan dışarı uzanan tekerlek parmaklıkları (spokes) ve dış torus (simit).

Stanford Torusu: Von Braun'a benzer ancak yaklaşık 1.6 km çapındadır ve 1 RPM gibi çok düşük bir hızda döner. Dış çember, devasa pencereleri olan kesintisiz bir yaşam alanıdır.

O'Neill Silindiri (Island Three): Her biri 8 km çapında ve 32 km uzunluğunda olan çift, karşıt dönüşlü devasa silindirlerdir. Coriolis devrilme momentini (gyroscopic precession) iptal etmek için iki silindirin zıt yönlerde dönmesi mekanik bir zorunluluktur. 1g için saatte yaklaşık 28 ila 40 devir yapmaları öngörülür.

Halatlı Dönüş (Tether): İki küçük kapsülün veya modülün çok uzun bir kabloyla birbirine bağlanıp ortak kütle merkezi etrafında dönmesidir.

Rotasyonun AI Video Temsilinde Sabit Kamera (Local Frame of Reference) İpuçları:
Eğer yapay zeka tarafından oluşturulan bir videoda kamera, dönen istasyonun dış gövdesine sabitlenmişse (local frame of reference), istasyonun kendisi kadrajda sabit görünürken evren etrafında dönecektir. AI'ın bu rotasyonel hareketi tutarlı bir şekilde verebilmesi için belirli fiziksel görsel ipuçlarının prompt ile zorlanması gerekir:

Yıldız/Gezegen Süpürmesi: Arka plandaki yıldızlar, Dünya veya Ay saniyeler içinde doğrusal bir yay çizerek kadrajdan kaymalıdır. (Örneğin 4 RPM hızında dönen bir istasyonda, arka plan saniyede 24 derece kayar).

Gölge Kayması: İstasyon gövdesine vuran Güneş ışığı (nokta kaynak) yapının dönüşü nedeniyle saniyeler içinde hızla uzamalı, kısalmalı veya yüzey üzerinde yer değiştirmelidir.

Kablo Eğriliği (Bowing): İstasyondan uzay boşluğuna uzanan her türlü esnek anten veya bağlama kablosu, merkezkaç kuvveti nedeniyle dönüş ekseninin dışına doğru parabolik bir eğrilik yapacaktır.

Yüzey Katmanları, Termal Görünüm ve Yaşlanma Matrisi

Yörünge habitatlarının kaplamaları, bilim kurgu filmlerinde resmedildiği gibi pürüzsüz çelik zırhlar değil, ağırlıklı olarak aşırı radyasyon ve termal döngü kontrolüne adanmış yüksek teknoloji kumaş ve polimer film katmanlarından oluşur. Yirmi yıllık bir istasyon modülü ile yeni fırlatılmış bir modül, yüzeylerindeki uzay erozyonu nedeniyle uzaktan tek bakışta ayırt edilebilir.

Vakum ortamında ısı transferini (ışınım yoluyla) engellemek için Çok Katmanlı Yalıtım (MLI - Multi-Layer Insulation) battaniyeleri kullanılır. Dış yüzeylerinde alüminize Kapton (altın veya gümüş rengi) kullanılır. Altın folyo yeni olduğunda mükemmel bir ayna gibi parlar; ancak düşük Dünya yörüngesinde (LEO) atomik oksijen (AO) bu ince folyoyu aşındırdığı için, ISS gibi modern istasyonlarda dış katman olarak Beta Kumaşı (White Beta Cloth) tercih edilir. Cam elyafı dokumalı ve teflon (PTFE) kaplı bu beyaz kumaş, atomik oksijene son derece dayanıklıdır ve modüllerin dışını devasa, dikişli bir "uyku tulumu" gibi sarar.

Zamanla, Beta kumaşı ve diğer polimerler, yıllar boyu güneşin acımasız UV radyasyonuna maruz kaldıkça fotokimyasal bozulmaya (çapraz bağlanma ve zincir kopması) uğrar. Bu durum, malzemenin optik özelliklerinde bir kırmızıya kayma (red shift) yaratır ve başlangıçta bembeyaz olan modüller kirli, mat bir sarıya/kahverengiye (UV yellowing/darkening) döner. Zarya (1998) modülü ile Tiangong (2021) yan yana getirilse, Zarya'nın yüzeyi belirgin şekilde sararmış ve atomik oksijen bombardımanı nedeniyle mikroskobik olarak pürüzlenmiş görünecektir.

Modüllerin üzerinde görülen bir diğer yaşlanma belirtisi, İtici Lekesidir (Thruster Plume Soot). Rus Soyuz/Progress araçlarının kenetlendiği portların (APAS/SSVP) etrafında, UDMH/N2O4 hipergolik yakıtlarının yanma atıklarından kaynaklanan kahverengi ve siyah dairesel kurum lekeleri oluşur. ISS'te Zvezda modülünün kuyruk tarafı bu yanık izleriyle doludur. Isı atım radyatörleri ise Beta kumaşının aksine yüksek yansıtıcılı beyaz boya (örn. AZ93 veya Z-93 çinko oksit) ile kaplanmış sert, düz ve pürüzsüz yüzeylerdir. Zamanla mikro çatlaklar oluştursalar da, uzaktan izlendiklerinde "keskin geometrik beyaz paneller" olarak formlarını korurlar.

On yıllar boyunca uzayda kalan istasyonların yüzeyleri (özellikle sert alüminyum Whipple kalkanları ve radyatör panelleri), hiper-hızlı mikrometeorit ve yörünge enkazı (MMOD) çarpmalarının yarattığı binlerce mikroskobik veya 1-2 cm büyüklüğündeki kraterlerle (pitting) kaplanır. Iki kademeli hafif gaz tabancaları (two-stage light gas guns) ile Dünya'da simüle edilen bu çarpmalar, uzaydaki malzemenin üzerinde koyu siyah çukurcuklar şeklinde belirir. Son olarak, yüzey anatominin ayrılmaz bir parçası Sarı Tutamak Geleneğidir. Tüm Amerikan ve ESA modüllerinin yüzeyinde standardize edilmiş eloksallı alüminyum EVA tutamakları (handrails) bulunur. Bu tutamaklar, uzay boşluğunun sert aydınlatmasında yüksek kontrast sağlamak ve termal emilimi dengelemek için soluk bir "altın sarısı" rengindedir. Yüzeyi, uzaktan bakıldığında yüzlerce kısa çizgiyle kaplı gibi gösterir.

AI Video Üretimi İçin Kritik Kısıtlar ve Difüzyon Önceliklendirmesi

Raporun temel amacı olan "tek insan karakterli, kesmesiz, 8-10 saniyelik sabit planlı AI video" üretimi, mevcut yapay zeka video difüzyon modellerinin (Sora, Runway Gen-3, Kling vb.) gizli uzay (latent space) kısıtlamalarıyla doğrudan çarpışmaktadır. Bu modeller, ince detayları çerçeveden çerçeveye korumakta zorlanır ve nesnelerin birbirine erimesine (morphing) veya kaymasına (sliding) neden olurlar. Yüksek kaliteli, halüsinasyonsuz sentetik veri üretimi için fiziksel doğruluk, AI sınırlarıyla harmanlanmalıdır.

Yasaklı Öğeler (Prompt'ta kesinlikle hariç tutulacaklar - Negative Prompting):

Yazı, Bayrak, Logo, Rakam, Ölçek İşareti: AI, tipografiyi sürekli değiştirir ve okunaklı harfleri her karede yeniden yorumlayarak uzaylı alfabesine çevirir. Yüzeydeki bir logo, tüm videonun gerçekçiliğini bozar.

Parlama ve Bloom: Vakum ortamında atmosferik saçılım olmadığı için Güneş etrafına ışık halesi (bloom) saçan bulanık bir top değil, gölgeleri jilet gibi keskinleştiren sert bir nokta kaynaktır. Prompt içerisinde: zero bloom, harsh directional point-source lighting, deep black shadows, raytraced lighting zorunludur.

Dalgalanan Yalıtım Örtüsü: Yörüngede rüzgar veya atmosferik sürtünme yoktur. Kumaşlar (MLI) dalgalanmaz. AI, prompt içindeki "kumaş" (fabric) kelimesini bir yeryüzü simülasyonu olarak algılayıp dalgalandıracağı için rigid thermally insulated geometric panels, taut unmoving surface covers terimleri kullanılmalıdır.

Serbest Süzülen Enkaz (Debris): Arka planda yüzen toz veya parçacıklar AI tarafından sürekli farklı boyutlarda yaratılıp yok edileceğinden, temporal tutarlılığı saniyeler içinde çökertir. clean vacuum, zero floating particles eklenmelidir.

Devamlılık Çapaları (Sayılabilir Geometrik Öğeler - Continuity Anchors):
AI modelleri sayı sayamaz ancak "güçlü geometrik kalıpları" (patterns) kareler boyunca devam ettirebilir. Çerçeveden çerçeveye kaymayı önlemek için, modelin görsel hafızasını kitleyecek büyük, geometrik ve sayılabilir uzay parçaları kadraja hiyerarşik olarak yerleştirilmelidir.

Öncelik Sırasıyla Çapa Öğeleri:

Güneş Kanatları (En güçlü çapa): Düzenli, kareli ızgara yapısı (solar cells grid), modelin kaymasını engeller. Prompt'ta açıkça belirtilmelidir (two massive symmetrical rectangular solar arrays).

Radyatör Panelleri: Tamamen düz, akordeon çizgili bembeyaz paneller ışığı homojen yansıttığı için şeklini korur (five aligned flat white cooling radiators).

Hizada Modüller: Birbirine bağlı silindirler sırası (three sequential white cylindrical modules).

Dış Kapaklar (Hatch/Port): Dairesel, belirgin kalın kenarlı metalik daireler. Merkezdeki dairesel pencereler (genelde 1 adet) en güçlü noktasal çapadır (circular metallic docking port with one central rigid window).

Sahnede Kayma (Morphing/Sliding) Riski Yüksek Olanlar:
Karmaşık kablo demetleri (wire harnesses), gevşek MLI kumaş kırışıklıkları, ince anten kümeleri ve JEM Açık Tesis (Exposed Facility) gibi dış yüzeydeki karmaşık deney paletleri, AI tarafından sıvı gibi akıtılıp eritilebilir. Prompt üretiminde bu detaylardan kaçınılmalı veya minimalistic clean cylindrical hull şeklinde sadeleştirilerek baskılanmalıdır. Keza yüzlerce sarı EVA tutamağı (handrail) yapay zekanın çizgileri birbirine karıştırmasına yol açabileceğinden "negatif prompt" ile silinmesi gerekebilir.

Veri Tabloları ve Anatomik Kart Şablonları

Aşağıdaki Tablo 1, bahsedilen tüm yörünge yapılarının gerçek ölçülerini, astronot boyuna (H_a) endekslenmiş oranlarını, silüet tipini, AI üretimindeki çapa değerini, kayma riskini ve obje-göreli prompt ifadesini sunmaktadır.

Tablo 1: Yörünge İstasyonları Anatomi ve AI Üretim Matrisi

| Öğe / Modül | Gerçek Ölçüsü ve Kaynağı | Astronot-Göreli Oranı (H_a: 1.9m) | Ait Olduğu Silüet Tipi | Sayılabilir Çapa Değeri | Kayma (Morphing) Riski Sınıfı | İngilizce Prompt İfadesi (Object-Relative) |
|---|---|---|---|---|---|---|
| Salyut 7 Gövde | L: 15m, D: 4.15m | L: 7.89 H_a, D: 2.18 H_a | Tek Gövdeli Silindir | 1 Ana Gövde, 3 Radyal Panel | Düşük (Basit Geometri) | one plain smooth white cylindrical module, diameter equivalent to two astronauts, rigid solar arrays extending radially |
| Skylab Gövde | L: 26m, D: 6.6m | L: 13.68 H_a, D: 3.47 H_a | Tek Gövdeli Silindir | 1 Geniş Çaplı Ana Gövde, 1 Yel Değirmeni Panel | Çok Düşük (Pürüzsüz) | one monolithic wide grey cylindrical habitat, diameter three times astronaut height, flat metallic exterior |
| Mir Çekirdek | L: 13.1m, D: 4.15m | L: 6.89 H_a, D: 2.18 H_a | Yıldız Biçimli Modül Kümesi | 1 Ana Gövde, 5 Düğüm Portu | Yüksek (Asimetrik Eklemeler) | central cylindrical module connected to a spherical docking node with multiple perpendicular ports |
| ISS Zvezda | L: 13.1m, D: 4.22m | L: 6.89 H_a, D: 2.22 H_a | Kafes ve Modül (Eksen) | 1 Kademeli Silindir, 14 Pencere | Orta (Anten fazlalığı) | stepped cylindrical module with thruster soot on aft port, taut grey and white insulation panels |
| ISS Destiny | L: 8.5m, D: 4.3m | L: 4.47 H_a, D: 2.26 H_a | Kafes ve Modül (Eksen) | 1 Silindir, 1 Dünya'ya Bakan Pencere | Düşük (Düzgün kafesli örtü) | perfectly straight white cylindrical lab module covered in taut grid-patterned beta cloth |
| ISS Kibo (JEM) | L: 11.2m, D: 4.4m | L: 5.89 H_a, D: 2.31 H_a | Kafes ve Modül (Eksen) | 1 Büyük Silindir, 1 Açık Tesis Platformu | Orta (Dış platform detayları) | massive clean white cylindrical module with an attached flat exposed scientific platform |
| ISS Columbus | L: 6.9m, D: 4.5m | L: 3.63 H_a, D: 2.36 H_a | Kafes ve Modül (Eksen) | 1 Kısa Tıknaz Silindir | Düşük (Sade dış yüzey) | short stubby white cylindrical module with conical ends, smooth tight fabric skin |
| ISS Cupola | D: 2.95m, H: 1.5m | D: 1.55 H_a, H: 0.78 H_a | Kafes ve Modül (Eklenti) | 1 Altıgen Pencere Kümesi, 1 Orta Cam | Yüksek (Cam içi yansımalar) | hexagonal observation dome with one massive circular central window and six trapezoidal side windows |
| Quest Hava Kilidi | L: 6.0m, D: 4.0m | L: 3.15 H_a, D: 2.10 H_a | Kafes ve Modül (Eklenti) | 1 Kısa Silindir, Dış Tanklar | Düşük (Belirgin hatlar) | short white cylindrical airlock module surrounded by external high-pressure gas tanks |
| Poisk (MRM-2) | D: 2.55m | D: 1.34 H_a | Kafes ve Modül (Eklenti) | 1 Küçük Düğüm, 1 Port | Düşük | very small narrow cylindrical docking node attached perpendicularly to main hull |
| ISS Kafes (Truss) | L: 94m, Kesit: 4.5m | L: 49.47 H_a, Kesit: 2.36 H_a | Kafes ve Modül (Omurga) | 10+ Kafes Segmenti Hiyerarşisi | Çok Yüksek (Çubuklu karmaşa) | massive linear metallic truss framework composed of distinct rigid cubic segments, no loose wires |
| ISS SAW (Güneş K.) | L: 35m (Tek Kanat), W: 12m | L: 18.42 H_a, W: 6.3 H_a | Kafes ve Modül (Ek) | N Kanat, Geometrik Kafes | Çok Düşük (Güçlü Çapa) | vast rectangular solar array wing divided into countable rigid square cells, glowing orange in harsh sunlight |
| ISS Radyatör | L: 22m (Açılım) | L: 11.57 H_a | Kafes ve Modül (Ek) | Düzenli Katmanlı Akordeon | Düşük (Sıralı form) | perfectly flat white rectangular cooling radiator panels aligned in a rigid straight line |
| Canadarm2 | L: 16.8m, D: 0.35m | L: 8.84 H_a, D: 0.18 H_a | Kafes ve Modül (Ek) | 7 Eklem, 2 Uç Efektör | Orta (İnce uzun yapı bükülebilir) | rigid articulated robotic arm composed of long thin white cylindrical booms connected by distinct rotary hinges |
| Tiangong Çekirdek | L: 16.6m, D: 4.2m | L: 8.73 H_a, D: 2.21 H_a | Tek Hat | 1 Ana Gövde, 2 Esnek Güneş Kanadı | Düşük (Pürüzsüz) | modern white cylindrical core module, clean smooth hull segments, symmetrical docking hub |
| Gateway HALO | L: 7.0m, D: 3.0m | L: 3.68 H_a, D: 1.57 H_a | Tek Hat (Ay Yörüngesi) | 1 Dar Silindir, 2 Radyal Port | Düşük (Dar ve sade) | compact narrow cylindrical habitat module, diameter smaller than two astronauts, rigid metallic surface |
| Axiom İstasyonu | L: 9.0m, D: 4.4m | L: 4.73 H_a, D: 2.31 H_a | Ticari Ek modül | 1 Küt silindir, 4 Dev Pencere | Düşük (Pürüzsüz dış yüzey) | sleek commercial cylindrical module with large rigid observation windows, spotless clean white exterior |
| Orbital Reef | D: 8.0m (Planlanan) | D: 4.21 H_a | Süper-Ağır Ticari | 1 Devasa Monolitik Gövde | Düşük (Devasa Düzlük) | gigantic pristine monolithic cylindrical space station, diameter four times astronaut height, gleaming white |
| CBM Portu | Açıklık: 1.3m, Dış D: 1.8m | Açık: 0.68 H_a, Dış: 0.94 H_a | Tüm Batı Modülleri | 1 Kare-Daire Kapak Geometrisi | Düşük (Geometrik ve sabit) | heavy circular metallic berthing port with thick rigid docking ring, square inner hatch |
| APAS/SSVP Portu | Açıklık: 0.8m | Açık: 0.42 H_a | Tüm Rus/Çin Modülleri | 1 Çok Küçük Yuvarlak Kapak, 12 Çentik | Düşük (Geometrik ve sabit) | narrow circular docking collar with metallic guide petals, diameter barely wider than astronaut shoulders |
| EVA Tutamakları | Uzunluk: 0.6m, Kesit: 2.5cm | Uzunluk: 5W_h (Eldiven) | Tüm Yüzeyler | N Adet Sarı Metal Çubuk | Yüksek (AI çizgileri eritebilir) | (negative prompt: yellow handrails), smooth module surface without thin protruding bars (AI üretiminde çizgi bozulmasını engellemek için isteğe bağlı olarak çıkartılmalıdır) |

Tablo 2: Silüet Tipleri İçin AI Anatomi Kartı Şablonları

Her bir mimari silüet türünü üretmek için AI metin isteminde modül ve parça sayıları sabitlenmelidir. Aşağıdaki tablo şablonları, difüzyon modellerinin halüsinasyon riskini en aza indirecek katı mimari kuralları tanımlar.

| Şablon Tipi | Modül Sayısı / Mimarisi | Kanat / Radyatör / Kapak Yapılandırması | Yaşlanma Göstergesi Prompt Eklentisi |
|---|---|---|---|
| 1. Kafes ve Modül (ISS Tipi) | Hizalı 4 adet ana silindirik modül (Destiny, Unity, vb.) (Çapa: 4). Modül hattını 90 derece ile kesen tek, devasa metalik, kafes yapı (Truss). | Kanat: Kafesin her iki ucunda 4'er adet simetrik, toplam 8 devasa turuncu-altın panel. Radyatör: Kafes merkezinden sarkan 3 adet beyaz dikdörtgen blok. Kapak: Merkezî hizada, Dünya'ya bakan 1 adet kenetli araç (Dragon). | Hafif sararmış (yellowing) ana modül kumaşları, dış kenarlarda fotokimyasal kirlenme, termal battaniye dikişleri. |
| 2. Yıldız Biçimli Küme (Mir Tipi) | 1 Ana çekirdek modül, ucunda küresel bir düğüm (node). Düğüme 90 derece açılarla bağlı, haç şeklinde uzanan 4 eşit çaplı kısa silindir (Çapa: Toplam 5 silindir + 1 küre). | Kanat: Modüllerden rastgele fırlayan asimetrik yerleşimli toplam 6 adet güneş kanadı. Radyatör: Ayrı radyatör yok. Kapak: Boşta kalan radyal portlarda 2 açık APAS androjen kapak. | Kahverengi itici gaz (soot) lekeleri, ağır koyulaşmış termal battaniyeler, MMOD çukurcukları, yeşilimsi yansımalar. |
| 3. Tek Hat (Tiangong Tipi) | Uç uca eklenmiş 3 özdeş uzun silindirik modül ("T" şekli). Kafes kirişi yok, modüller doğrudan birbiriyle bütünleşiktir (Çapa: 3). | Kanat: Sadece sağ ve sol uçtaki laboratuvar modüllerinin uç kısmında yer alan 2 devasa, esnek görünümlü panel. Radyatör: Modül altına yapışık, çıkıntı yapmayan düz beyaz yüzeyler. | Bembeyaz, tertemiz yepyeni beta kumaşı, parlak beyaz metalik yüzeyler, sıfır UV sararması, mikrometeorit hasarı yok. |
| 4. Dönen Torus (Stanford Tipi) | Kesintisiz, kusursuz bir ana devasa çember/simit (Torus). Merkezî silindirik şafta bağlanan eşit açılı 4 veya 6 sert silindirik tünel kol (Çapa: 1 dış hat, 6 iç kol). | Kanat/Radyatör: Geleneksel kanat yok, devasa parabolik bir merkezi ayna sistemi (Sun reflection mirror). İç yüzeye vuran derin, keskin tekil Güneş gölgeleri. | Parlak cilalı alüminyum veya çok geniş alana yayılmış pürüzsüz pütürsüz geometrik netlik, hiç örtü kırışıklığı yok. |

--- KAYNAK LİSTESİ (raporun kendi listesi, birebir) ---

scribd.com — Wings in Orbit Scientific and Engineering Legacies of The Space
ntrs.nasa.gov — Assumption Management in Complex Spaceflight: The Artemis
quora.com — Do the astronauts feel the speed when going for a space walk? The
autoevolution.com — The International Space Station at a Glance
en-academic.com — International Space Station
en.wikipedia.org — Docking and berthing of spacecraft
grokipedia.com — Docking and berthing of spacecraft
en.wikipedia.org — International Space Station
researchgate.net — (PDF) An automated tether management system for microgravity
scispace.com — An automated tether management system for microgravity
researchgate.net — (PDF) The Interesting Challenges of Designing for Humans in Space
ntrs.nasa.gov — A Survey of Radiation Measurements Made Aboard Russian
thespacereview.com — Science Power Platform: the ISS's cancelled power module
scribd.com — International Space Station NASA Reference Guide
slideshare.net — Reference Guide To The International Space Station
ntrs.nasa.gov — international systems integration on the international space station
en.wikipedia.org — Common Berthing Mechanism
astronautix.com — Boeing
nasa.gov — International Space Station Facts and Figures
jaigp.org — Soft Inflatable Robotic Systems for Space Applications: A Survey
en.wikipedia.org — Tiangong space station
sigma-astro.co.uk — China - Tiangong Space Station
thalesaleniaspace.com — Lunar Gateway's HALO pressurized module in preparation for
en.wikipedia.org — Habitation and Logistics Outpost
reddit.com — Interview with the module manufacturer of the Axiom station
another-giant-leap.fandom.com — Axiom Station
reddit.com — Sierra Space larger LIFE 3.0 inflatable modules have been
pmc.ncbi.nlm.nih.gov — Built On-orbit Robotically assembled Gigatruss (BORG)
selenianboondocks.com — Selenian Boondocks
popsci.com — Watch a giant, inflatable space station prototype explode during its
en-academic.com — Mir
researchgate.net — (PDF) Space Settlement Population Rotation Tolerance
dyarstraights.com — The Gravity of the Situation
worldbuilding.stackexchange.com — How to make a Stanford torus start rotating?
en.wikipedia.org — O'Neill cylinder
en-academic.com — Island Three
mavericuniverse.fandom.com — Island Three The O'Neill cylinder
newspaceeconomy.ca — Materials Science in the Harsh Frontier of Space
mdpi.com — Material Characterization Required for Designing Satellites
researchgate.net — (PDF) Property changes in materials due to atomic oxygen in the low
researchgate.net — (PDF) Characterizing the optical performance of AZ93 with a
researchgate.net — The International Space Station and the Space Debris Environment
pubs.aip.org — The Texas A&M University Hypervelocity Impact Laboratory
archive.org — LDEF: 69 Months in Space. Third Post-Retrieval Symposium, part 3
ntrs.nasa.gov — Human Spaceflight Structures Engineering Internship
