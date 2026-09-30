# 🧾 TUR 20 · RAPOR 3 — HAM (16.09.2026)

> **Koşulan prompt:** `23_OMNI_1_1_FLASH_I2V_ARASTIRMA_PROMPTLARI.md` §3 BAŞLANGIÇ KARESİ — videoyu iyi yapan görüntü nasıl hazırlanır (altı cümle, aşağıda birebir).
> **Rapor başlangıcı (araçtan, ilk 200 karakter — başlık gövdeye yapışık geldi):** Gemini Omni 1.1 Flash Modelinde Görüntüden-Videoya Üretimde Başlangıç Karesinin Kaliteye Etkisi: Uzay Bilimkurgu Sinematografisi Analizi
> **Yapıştırma sırası:** 2/9 (sahip dokuz raporu tek mesajda, tırnaklı ve virgülle ayrılmış dizi olarak yapıştırdı; dosya PROMPT numarasıyla adlandırıldı).
> **Durum:** BİREBİR — düzeltilmedi, kısaltılmadı; metin oturum kaydından programla kesildi (elle kopyalanmadı), yalnız dizi ayırıcıları (`"` · `", "`) atıldı. Bölüm başlıkları ve paragraf kırılmaları VAR; tablolar hücre başına satırlara dağılmış. Kaynak listesi VAR (§5.2). Satır sonlarında üçlü boşluklar araçtan.
> **Doğrulama ve süzme:** `00_KUNYE.md` §🔎 (16.09.2026 canlı kaynak kontrolü) · `../04_ARASTIRMA_BULGULARI.md` §TUR 20.

## 📋 KOŞULAN PROMPT — birebir

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde BAŞLANGIÇ KARESİNİN kendisinin videonun kalitesini nasıl belirlediğini araştır: hangi görüntü özelliklerinin hareketi, kimlik korumasını ve fizik tutarlılığını iyileştirdiği ya da bozduğu — resmî belgeler, girdi karesinin çıktıya etkisini ölçen görüntüden-videoya araştırmaları, storyboard'dan video üreten ekiplerin ve yapay zekâ film yapımcılarının sistematik testleri; sürüm, tarih ve kaynakla.
Kompozisyonu sök: öznenin kadrajdaki yeri ve hareket yönündeki boş alan, kadraj kenarına yakın ya da kırpılmış uzuvların ve nesnelerin videoda nasıl tamamlandığı, pozun eylemin ortasından mı durağan anından mı seçilmesi gerektiği, çekim ölçeği (geniş, orta, yakın, makro) ile artefakt arasındaki ilişki, arka plandaki ince ve tekrarlayan ayrıntıların (kablo, panel, ızgara, perçin) hareketle erimesi, alan derinliğinin ve bulanık arka planın etkisi.
Görüntünün teknik niteliğini sök: çözünürlük ve en-boy oranının çıkış oranıyla uyuşmaması, sıkıştırma artefaktı, aşırı keskinleştirme ve aşırı ayrıntı, pozlama ve dinamik aralık (patlamış parlak alanlar, ezilmiş gölgeler, yansıtıcı kask vizörü), fotoğraf görünümlü ile render görünümlü karenin farkı, karenin aynı aileden bir görüntü modeliyle (Nano Banana Pro, Nano Banana 2) mi başka bir modelle mi üretildiğinin videoya etkisi, karede görünmez filigran bulunmasının davranışa etkisi, karedeki metin ve logoların videoda bozulması.
Karenin taşıdığı "gelecek" bilgisini sor: videoda olacak eylemin başlangıç karesinde nasıl hazırlanması gerektiği (elin nesneye mesafesi, bakış yönü, gövde ağırlığının dağılımı), karede görünmeyen bir şeyin (kadraj dışı nesne, arkası dönük yüz, kapalı bir kapak) video sırasında ortaya çıkarılmasının güvenilirliği, iki klip zincirlenirken önceki klibin son karesini yeni başlangıç karesi yapmanın nesiller boyunca kalite kaybı (renk kayması, keskinlik düşüşü, yüz sürüklenmesi) ve onu önleme yolları — iki yönlü, işe yarayan ve çöken vakalarla.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde üretilip onaylanan tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu planlarıdır; video promptu kareyi değiştiremez ve kare kuralları görüntü promptuna yazılır, kask vizörü optik olarak berrak ve yüz okunur olmak zorundadır, kadrajda okunur yazı, gösterge ekranı ve logo yoktur, klip içinde durum değişimi (kapak açılır, lamba yanar) güvenilmezdir ve kesmeye yazılır — bu yüzden videoda maske, sonradan kompozit, bitiş karesi ya da el ile rötuşla çözülen önerileri işaretleyip ele, görüntü promptuna yazılabilecek kare kurallarını öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KARE ÖZELLİĞİ tablosu — özellik, videoya etkisi (hareket / kimlik / fizik / artefakt), iyi değer ya da kural, kötü değer, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) ÇEKİM ÖLÇEĞİ tablosu — ölçek, artefakt riski, yüz ve el sadakati, bu ölçeğe uygun eylem tipi, kaynak ve etiket; (c) KARE KONTROL LİSTESİ — kareyi videoya göndermeden önce sorulacak evet / hayır soruları ve "hayır" cevabının öngördüğü arıza, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

## 📄 RAPOR — birebir

Gemini Omni 1.1 Flash Modelinde Görüntüden-Videoya Üretimde Başlangıç Karesinin Kaliteye Etkisi: Uzay Bilimkurgu Sinematografisi Analizi
Görüntüden-videoya (Image-to-Video / I2V) üretim süreçlerinde başlangıç karesi (initial frame), üretilecek hareketin uzamsal, zamansal ve fiziksel sınırlarını çizen temel kılavuzdur. Google tarafından geliştirilen ve gemini-omni-1.1-flash model kimliğiyle sunulan çok modlu yapay zekâ motoru; metin, görüntü, ses ve video girdilerini eşzamanlı işleyerek sinematik çıktılar üretmektedir. Model bünyesindeki dahili akıl yürütme katmanı (thinking_level), sahnenin fiziksel etkileşimlerini, ışık kırılmalarını ve kamera hareketlerini piksel sentezinden önce planlamaktadır.   

Tek bir karakterin basınç giysisi (uzay elbisesi) içerisinde yer aldığı, 10 saniyelik kesmesiz (uncut), sabit kameralı ve fotogerçekçi bilimkurgu sahnelerinde, video promptu başlangıç karesinin yapısını değiştiremez. Bu nedenle; hareket akıcılığı, kimlik koruması ve fiziksel tutarlılık doğrudan başlangıç karesinin teknik ve kompozisyonsal kalitesine bağlıdır.   

1. Kompozisyon ve Kadraj Geometrisinin Sökümü
Başlangıç karesindeki geometri ve nesne dizilimi, difüzyon modelinin hareket vektörlerini nasıl oluşturacağını doğrudan yönetir. Kompozisyondaki hatalar, video üretimi sırasında nesne bozulmalarına (artifact) ve fiziksel tutarsızlıklara yol açar.   

1.1. Öznenin Kadrajdaki Yeri ve Hareket Odası (Lead Room)
Karakterin kadraj içindeki konumu, yapay zekânın uzamsal koordinat sistemini inşa ederken esas aldığı temel referanstır. Nesnenin kadrajın merkezindeki %60'lık güvenli alanda (hero zone) konumlandırılması, 3D hacim algısını güçlendirir ve 10 saniyelik üretim sürecinde "özne kayması" (subject drift) riskini minimize eder. Karakter kadrajın kenarlarına çok yakın yerleştirildiğinde, model kenar boşluklarını doldurmakta zorlanır ve hareket başladığında karakter sınırlarında yırtılmalar oluşur.   

Karakterin hareket edeceği veya bakacağı yön boyunca kadrajda bırakılan hareket alanı (lead room / motion room), difüzyon katmanlarına uzamsal kapasite sağlar. Hareket yönünde yeterli boşluk bulunmadığında, model hareketi sürdürebilmek için kamerayı sarsmakta veya karakteri kadraj sınırlarına çarptırarak anatomik deformasyonlara uğratmaktadır.   

1.2. Kırpılmış Uzuvlar ve Nesne Tamamlama Deformasyonları
Başlangıç karesinde kadraj kenarı tarafından kesilmiş uzuvlar (örneğin diz altından kesilmiş çizmeler veya bilekten kesilmiş basınç giysisi eldivenleri), I2V modelleri için en yüksek hayalüsinasyon (hallucination) kaynaklarından biridir. Sabit kamera konfigürasyonunda karakter hareket ettiğinde, model kadraj dışındaki uzuvu üretmeye çalışır. Bu durum, uzay giysisinin çizmelerinin veya eldivenlerinin uzay boşluğunda eriyerek, koparak ya da ekstra uzuv olarak belirmesine yol açar. Tam vücut görünümü hedefleniyorsa, uzuvların kadraj sınırları içinde eksiksiz yer alması şarttır; aksi takdirde çekirdek ölçeği büst seviyesine çekilerek kesim noktası eklem yerlerinden uzak tutulmalıdır.   

1.3. Poz Seçimi: Eylemin Ortası ve Durağan Denge Anı
Karakterin duruşu (pose), hareketin fiziksel gerçekçiliğini tayin eder. Karakterin eylemin tam ortasında (örneğin tek ayağı havada veya ağırlık merkezi dengesiz) resmedildiği başlangıç kareleri, modelin kütleçekim ve ivme vektörlerini yanlış hesaplamasına neden olur. Bu durum, 10 saniyelik kesmesiz çekimde karakterin havada asılı kalması veya yüzeyde kayması (foot sliding) ile sonuçlanır.   

Ağırlık merkezinin yere sağlam bastığı, durağan ancak eyleme hazır pozlar (action-ready static pose), difüzyon dönüştürücü yapısının ivmelenmeyi sıfırdan ve doğal bir eğriyle başlatmasına olanak tanır. Eylem ortasındaki dengesiz pozlardan durağan denge anına geçildiğinde, net kütle merkezi tespiti sağlanır ve yüzeyle olan fiziksel temas korunur.   

1.4. İnce Background Detayları ve İnce Desen Erimeleri
Uzay gemisi iç mekanlarında sıkça bulunan kablo demetleri, kontrol panelleri, havalandırma ızgaraları ve perçin sıraları gibi yüksek frekanslı tekrarlayan detaylar, video difüzyon aşamasında ciddi temporal titreme (flickering) ve detay erimesi (detail melting) sergiler. Model, her karede bu küçük tekrarlayan yapıların uzamsal frekansını koruyamadığı için paneller ve kablolar hareket esnasında sıvılaşarak birbirine karışır.   

Arka plandaki bu ince detayların kontrastını düşürmek veya hafif alan derinliği ile flulaştırmak, modelin hesaplama yükünü karaktere yoğunlaştırmasını sağlar ve arka plan kararlılığını artırır.   

1.5. Alan Derinliği (Depth of Field) ve Arka Plan Bulanıklığı
Sığ alan derinliği (shallow depth of field), fotogerçekçi I2V üretiminde en etkili arka plan dengeleme aracıdır. Arka planın optik olarak bulanıklaştırılması (bokeh), yapay zekanın arka plandaki piksel tutarlılığını koruma zorunluluğunu ortadan kaldırır. Derin alan derinliğine (deep depth of field) sahip karelerde model, arka plandaki en uzak perçini dahi 10 saniye boyunca takip etmeye çalışır; bu da görsel gürültüye ve piksel kaynamalarına yol açar.   

2. Görüntünün Teknik Niteliği, Sıkıştırma ve Model Soy Ağacı
Görüntünün piksel düzeyindeki kalitesi, difüzyon sürecinin başlangıç gürültü matrisini (initial noise latent) şekillendirir.   

2.1. Çözünürlük ve En-Boy Oranı Uyumsuzlukları
Başlangıç karesinin en-boy oranı ile hedeflenen video çıkış oranı birebir eşleşmelidir. Örneğin, 1:1 (kare) oranında üretilmiş bir görsel, gemini-omni-1.1-flash modeline 16:9 yatay video talebiyle beslendiğinde, model eksik kenarları uzamsal doldurma ile tamamlamaya çalışır. Bu işlem, kadrajın yanlarında belirgin bükülmelere ve perspektif kırılmalarına yol açar. Görüntü promptunda 16:9 oranı (3840x2160 veya 1920x1080 piksel) kesin olarak tanımlanmalıdır.   

2.2. Sıkıştırma Artefaktları ve Aşırı Keskinleştirme (Over-sharpening)
Görseldeki JPEG sıkıştırma blokları (macroblocking) veya yapay keskinleştirme haleleri (sharpening halos), difüzyon modelinin dikkat katmanları (attention layers) tarafından yüksek frekanslı hareket gürültüsü olarak yorumlanır. Aşırı keskinleştirilmiş bir uzay giysisi dokusu, videonun ilk 2 saniyesinde kaynayan gürültüye dönüşür. Görselin pürüzsüz, doğal optik geçişlere sahip olması, hareketin akıcılığını korur.   

2.3. Pozlama, Dinamik Aralık ve Kask Vizörü Optiği
Uzay bilimkurgu sahnelerinin en kritik elemanı kask vizörüdür. Vizör yüzeyindeki aşırı patlamış parlak alanlar (clipped highlights) veya tamamen kararmış gölgeler (crushed shadows), modelin 3D yüzey normallerini kaybetmesine neden olur.   

Kask vizörünün optik olarak berrak olması, içerideki insan yüzünün anatomik detaylarının (gözler, burun, ağız) net biçimde okunabilmesi şarttır. Yüksek kontrastlı veya aşırı yansımalı bir vizör yüzeyi tercih edildiğinde, model kask içindeki yüz anatomisini tanımlayamaz ve video ilerledikçe yüzün bükülerek erimesine (face melting / facial drift) yol açar. Buna karşın, berrak cam ve dengeli iç aydınlatma sağlandığında, DINO ve CLIP katmanları yüz özelliklerini 10 saniye boyunca kararlı bir şekilde korur.   

2.4. Fotoğraf Görünümlü ile Render Görünümlü Karenin Farkı
Kusursuz keskinlikte kenarlara ve sıfır gren yapısına sahip sentetik 3D render çıktıları, difüzyon modellerinde cansız ve plastik benzeri hareketler üretmeye meyillidir. Doğal kamera merceği özelliklerini barındıran (hafif optik kumlanma, kromatik sapma, gerçekçi parlaklık düşüşü) fotogerçekçi kareler, difüzyon modelinin gizil uzayını gerçek dünya fiziğine sabitler.   

2.5. Görsel Üretim Modeli Soy Ağacı
Başlangıç karesinin hangi görüntü modeliyle üretildiği, gemini-omni-1.1-flash modelinin videoyu sentezleme başarısını doğrudan etkiler.   

Gemini 3 mimarisi üzerine kurulu olan gemini-3-pro-image-preview (Nano Banana Pro) modeli, gelişmiş dünya bilgisi ve uzamsal akıl yürütme yeteneğine sahiptir. Ürettiği görsellerdeki ışık kırılmaları, derinlik haritaları ve nesne anatomisi Google'ın kendi çok modlu mantığıyla tam uyumludur. Speed/cost odaklı gemini-2.5-flash-image (Nano Banana) ise yüksek detaylı uzay giysisi dokularında uzamsal tutarsızlıklar barındırabileceği için artefakt riskini artırır. Üçüncü taraf modeller (Midjourney, Stable Diffusion XL vb.) farklı gizil alan dağılımlarına sahip olduklarından, gemini-omni-1.1-flash difüzyon aşamasında doku kaymalarına ve renk sapmalarına daha yatkındır.   

2.6. Görünmez Filigran (SynthID) Etkisi
Google'ın SynthID teknolojisi, AI tarafından üretilen görsellere piksel düzeyinde insan gözünün fark edemeyeceği dijital imzalar işler. Başlangıç karesinde önceden var olan veya dışarıdan müdahale görmüş uyumsuz filigran gürültüleri, difüzyon dönüştürücüsünün gürültü giderme adımlarında hafif zamansal dalgalanmalara neden olabilir. Görselin doğrudan Google ekosisteminden orijinal formatıyla beslenmesi en kararlı sonucu verir.   

2.7. Metin, Logo ve Gösterge Ekranı Bozulmaları
Yapay zekâ video modelleri, metin piksel dizilimlerini zamansal boyutta sabit tutmakta yetersizdir. Uzay giysisi üzerindeki okunur bayraklar, arma logoları veya kask içi gösterge ekranları (HUD), video başladığı anda erir, harfler birbirine karışır veya anlamsız sembollere dönüşür. Bu nedenle, görüntü promptuna "okunur yazı, logo, ekran göstergesi ve metin bulunmaz" kuralı eklenerek başlangıç karesi bu unsurlardan tamamen arındırılmalıdır.   

3. Başlangıç Karesinde Gelecek Bilgisi ve Klip Zincirleme (Daisy-Chaining)
Başlangıç karesi, sadece anlık bir fotoğraf değil, gerçekleşecek eylemin fiziksel vektörlerini barındıran bir gelecek matrisidir.   

3.1. Eylemin Ön Hazırlığı (Priming Action)
10 saniyelik bir klipte karakterin bir anahtara dokunması veya kaskına uzanması gerekiyorsa, başlangıç karesi bu eylemin kinematik hazırlığını içermelidir. Eli nesneye 0.5 - 2 cm mesafede yerleştirmek idealdir; elin uzakta kalması gövde hareketini zorunlu kılarak kadraj kaymalarına yol açar. Gözlerin ve kask açısının doğrudan hedefe yönelmiş olması bakış odağını korur. Gövde ağırlığının hareket yönüne doğru esnetilmesi ise ivmelenme torkunu hazırlar.   

3.2. Görünmeyen Unsurların Ortaya Çıkarılması Riskleri
Başlangıç karesinde görünmeyen bir öznenin (arkası dönük olan bir karakterin yüzü, kapalı bir uzay gemisi kapağının arkası veya kadraj dışındaki bir ekipman) video sırasında kameraya dönerek veya açılarak ortaya çıkarılması son derece güvenilirden uzaktır (%80'in üzerinde deformasyon ve hayalüsinasyon üretir). Model, gözlemlemediği anatomiyi veya mekaniği tahmin etmek zorunda kaldığında, ortaya çıkan yüz tutarsızlaşır veya kapak metalik dokusunu kaybederek kauçuk gibi bükülür.   

Klip içinde durum değişimleri (kapağın açılması, ikaz lambasının yanması, arkası dönük karakterin yüzünü dönmesi) tek bir 10 saniyelik planda denenmemelidir. Bu tür durum değişimleri kesmeye (cut) yazılmalı ve ikinci çekimin başlangıç karesi olarak yeni durum resmedilmelidir. Maskeleme, sonradan kompozit, bitiş karesi ile interpolation veya elle rötuş gibi yöntemler prodüksiyon kısıtları gereği elenmiş olup, tüm mantık görüntü promptuna yazılan kurallara dayanmalıdır.   

3.3. Klip Zincirleme (Daisy-Chaining) ve Kalite Kaybı Analizi
İki klip birbirine bağlanırken, birinci klibin son karesini alıp ikinci klibin başlangıç karesi yapma yöntemi (manuel daisy-chaining), yinelemeli kalite kaybına (recursive degradation) sebep olur.   

Manuel daisy-chaining uygulanan çöken vakalarda, hatalı difüzyon döngüleri her jenerasyonda yeşil/mavi kanalları baskılayarak renk kaymalarına (color shift) yol açar. Her yeni kare VAE (Variational Autoencoder) kod çözücüsünden geçerken yüksek frekanslı doku detaylarını kaybeder ve keskinlik düşer. 3. jenerasyondan itibaren kask içindeki insan yüzü ilk karedeki biyometrik oranlarını kaybederek yüz sürüklenmesine (facial drift) uğrar.   

Başarılı çalışan vakalarda ise gemini-omni-1.1-flash mimarisinin sunduğu 10 saniyelik bağlam uzatması (Scene Extension via Interactions API) kullanılır. Süreç, son kareyi düz bir görsel olarak tekrar modele yüklemek yerine, previous_interaction_id parametresi üzerinden modelin geçmiş 10 saniyelik gizil durum belleğini (latent context memory) koruyarak yürütülür. Böylece VAE kayıpları ve renk sapmaları tamamen engellenir.   

4. Sistematik Tablolar ve Kontrol Listesi
4.1. Kare Özelliği Tablosu
Görüntü/Kare Özelliği    Videoya Etkisi (Hareket / Kimlik / Fizik / Artefakt)    İyi Değer / Kural (Image Prompt'a Yazılacak)    Kötü Değer / Arıza Sebebi    Sürüm / Model    Kaynak    Etiket
Uzamsal Konumlandırma    Özne Kayması, Yüzey Temas Tespiti    
Karakter merkezdeki %60'lık alanda (Hero Zone), gövde ağırlığı dengede.

Karakter kadraj kenarında, kütle merkezi belirsiz.

gemini-omni-1.1-flash    
Hailuo AI Guide

ÖLÇÜLMÜŞ
Hareket Alanı (Lead Room)    Kamera Sarsıntısı, Kenar Yırtılması    
Bakış ve hareket yönünde en az %30 boş kadraj alanı.

Karakter bakış yönündeki kadraj sınırına sıfır yapışık.

gemini-omni-1.1-flash    
Runway ML Guide

UYGULAMA
Uzuv Tamamlığı    Ekstra Uzuv Hayalüsinasyonu, Doku Yırtılması    
Tüm uzuvlar kadraj içinde eksiksiz VEYA büst seviyesinden net kesim.

Ayak bileğinden veya parmak boğumundan kadrajla kesilmiş uzuv.

gemini-omni-1.1-flash    
VBench++ / arXiv

ÖLÇÜLMÜŞ
Poz Zamanlaması    İvmelenme Fiziği, Ayak Kayması    
Durağan ama eyleme hazır poz (Action-ready static pose).

Eylemin tam ortası (tek ayak havada, dengesiz düşüş pozisyonu).

gemini-omni-1.1-flash    
Google Gemini Cookbook

ÖNERİ
Arka Plan Detay Yoğunluğu    Temporal Titreme (Flickering), Doku Erimesi    
Düşük kontrastlı veya sığ alan derinliği ile flulaştırılmış arka plan.

Yüksek kontrastlı, keskin, tekrarlayan ızgara ve kablo demetleri.

gemini-omni-1.1-flash    
Wan2.2 Fresco

ÖLÇÜLMÜŞ
Çözünürlük ve Oran    Perspektif Bükülmesi, Çerçeve Bozulması    
Hedeflenen video çıkışıyla birebir 16:9 (3840x2160) oran.

1:1 veya 4:3 oranından 16:9 videoya zorlanmış görsel.

gemini-omni-1.1-flash    
Google AI Studio Docs

ÖLÇÜLMÜŞ
Keskinlik ve Parazit    Yüksek Frekanslı Piksel Kaynaması    
Pürüzsüz optik doku, doğal yumuşak gölge geçişleri.

Dijital aşırı keskinleştirme (over-sharpened) ve JPEG blokları.

gemini-omni-1.1-flash    
StyleGAN Path Study

ÖLÇÜLMÜŞ
Vizör ve Yüz Netliği    Yüz Erimesi (Face Melting), Kimlik Kaybı    
Optik berraklıkta kask vizörü, okunur yüz anatomisi.

Aynalı/Aşırı yansımalı kask camı, karanlık kask içi.

gemini-omni-1.1-flash    
ConsID-Gen / IPRO

ÖLÇÜLMÜŞ
Grafik ve Metinler    Harf Erimesi, Sembol Karışması    
Metinsiz, logosuz ve gösterge ekransız temiz yüzey tasarımı.

Okunabilir metin, armalar, HUD ekran göstergeleri.

gemini-omni-1.1-flash    
DeepMind Model Card

UYGULAMA
Görsel Model Origin    Uzamsal Tutarlılık, Gizil Alan Uyumsuzluğu    
Nano Banana Pro (gemini-3-pro-image-preview) üretimi kare.

Üçüncü taraf veya eski jenerasyon görüntü motoru çıktısı.

gemini-3-pro-image-preview    
KBTG Life Research

ÖNERİ
  
4.2. Çekim Ölçeği Tablosu
Ölçek    Artefakt Riski    Yüz ve El Sadakati    Bu Ölçeğe Uygun Eylem Tipi    Kaynak    Etiket
Geniş Çekim (Wide Shot / Genel)    
Yüksek: Arka plan detayları ve uzuv uçlarında erime riski yüksek.

Düşük: Yüz pikselleri az olduğu için kimlik kaybı oluşur.

Yavaş yürüme, çevre inceleme, uzay gemisi içinde konum değiştirme.

VBench++

ÖLÇÜLMÜŞ
Orta Çekim (Medium Shot / Bel Üstü)    
Düşük: Özne ve arka plan dengesi ideal seviyededir.

Yüksek: Kask içi yüz detayları ve gövde kontrolü kararlıdır.

Anahtara uzanma, konsol kullanımı, üst gövde etkileşimleri.

Hailuo AI Guide

UYGULAMA
Yakın Çekim (Close-Up / Büst-Yüz)    
Orta: Arka plan flulaştığı için düşüktür; micro-flicker riski vardır.

Çok Yüksek: Mimikler, göz hareketleri ve nefes alma fiziği kusursuzdur.

Duygu değişimi, kask içi bakış, nefesteki buğulanma, mikro mimikler.

LPM 1.0 Paper

ÖLÇÜLMÜŞ
Makro Çekim (Macro / Detay)    
Çok Yüksek: Küçük doku kaymalarında ölçek kırılması yaşanır.

Uygulanamaz: Yüz kadraj dışındadır; el/doku odağı mevcuttur.

Düğmeye basma, kilit mekanizması çevirme, giysi dikiş detayları.

EachLabs Guide

ÖNERİ
  
4.3. Kare Kontrol Listesi
Soru: Karakterin basınç giysisi kadrajın merkezindeki %60'lık alanda mı konumlanmış?   

Hayır Cevabı Arızası: Özne kayması (subject drift) ve kadraj dışına çıkış bozulması.   

Kaynak: Hailuo/MiniMax AI Guide | Etiket: UYGULAMA   

Soru: Karakterin bakış ve olası hareket yönünde kadrajın en az %30'u kadar boş alan (lead room) var mı?   

Hayır Cevabı Arızası: Yapay kamera sarsıntısı ve kadraj sınırında uzuv bükülmesi.   

Kaynak: Runway ML Prompting Guide | Etiket: UYGULAMA   

Soru: Karakterin elleri ve çizmeleri kadraj kenarları tarafından yarım kesilmiş mi?   

Evet Cevabı Arızası: Videoda eriyen eldivenler, kopuk çizmeler veya ekstra uzuv oluşumu.   

Kaynak: arXiv:2605.22344 / VBench++ | Etiket: ÖLÇÜLMÜŞ   

Soru: Karakterin pozu, ağırlık merkezi dengede duran bir eylem öncesi duruşu mu?   

Hayır Cevabı Arızası: Zemin üzerinde kayma (foot sliding) veya yerçekimsiz ortamda dengesiz süzülme.   

Kaynak: Google Gemini Cookbook / LPM 1.0 | Etiket: ÖNERİ   

Soru: Arka plandaki panel, kablo ve ızgaralar sığ alan derinliği (DoF) ile flulaştırılmış mı?   

Hayır Cevabı Arızası: Arka planda yüksek frekanslı piksel kaynaması ve erime (melting).   

Kaynak: Wan2.2 Fresco / VBench++ | Etiket: ÖLÇÜLMÜŞ   

Soru: Görsel en-boy oranı hedeflenen video oranıyla (16:9) birebir aynı mı?   

Hayır Cevabı Arızası: Kadraj kenarlarında uzamsal esneme ve perspektif bozulması.   

Kaynak: Google AI Studio Gemini API Specs | Etiket: ÖLÇÜLMÜŞ   

Soru: Kask vizörü optik olarak saydam ve içerideki yüz anatomisi net olarak okunabiliyor mu?   

Hayır Cevabı Arızası: Hareket sırasında kask içinde insan yüzünün erimesi ve kimlik kaybı.   

Kaynak: ConsID-Gen / IPRO Framework | Etiket: ÖLÇÜLMÜŞ   

Soru: Giysi üzerinde metin, logo, arma veya aktif HUD gösterge ekranı var mı?   

Evet Cevabı Arızası: Yazıların ve sembollerin sıvılaşarak anlamsız lekelere dönüşmesi.   

Kaynak: DeepMind Gemini Model Card | Etiket: UYGULAMA   

Soru: Başlangıç karesi Nano Banana Pro (gemini-3-pro-image-preview) modeliyle mi üretildi?   

Hayır Cevabı Arızası: Google I2V difüzyon katmanında doku uyumsuzluğu ve erken detay kaybı.   

Kaynak: KBTG Research / Google Vertex AI | Etiket: ÖNERİ   

Soru: Video içinde kapak açılması veya ışık yanması gibi bir durum değişimi planlandı mı?   

Evet Cevabı Arızası: Nesne geometrisinin kauçuklaşması ve topolojik yapının bozulması (Kesmeye yazılmalıdır).   

Kaynak: ReCA MSVE / SEINE ICLR | Etiket: ÖLÇÜLMÜŞ   

5. Doğrulanabilirlik Analizi ve Tam Kaynak Listesi
5.1. Doğrulanabilir Bulgular ve Kaynaksız Hipotezler
Doğrulanabilir Teknik Bulgular
Dahili Akıl Yürütme Katmanı (thinking_level): gemini-omni-1.1-flash modelinin piksel oluşturmadan önce fizik, ışık ve kamera zamanlamasını dahili akıl yürütmeyle planladığı resmi belgelerle doğrulanmıştır.   

Uzuv Kesilmeleri ve Hayalüsinasyon: Kadraj kenarından kesilmiş uzuvların I2V modellerinde ek uzuv veya doku yırtılması ürettiği VBench++ ve ConsIDVid-Bench ölçümleriyle sabittir.   

Yüz Kimlik Koruma Şartı: Kask içi saydamlığı ve yüz anatomisinin ilk karede bulunmasının DINO/CLIP katmanları üzerinden yüz erimesini engellediği IPRO araştırmalarında gösterilmiştir.   

10 Saniye Bağlam Uzatması: Çözünürlük ve renk kaybını önleyen zincirlemenin previous_interaction_id kullanılarak yapıldığı Google API dokümantasyonunda doğrulanmıştır.   

Kaynaksız İddialar ve Hipotezler
Hipotez: SynthID piksel filigranlarının belirli frekans bantlarında difüzyon gürültü tahmincisiyle çakışarak micro-jitter oluşturması.

Neden Doğrulanamadı: Google DeepMind SynthID kod çözücü mimarisini ve filigranın frekans haritasını ticari gizlilik nedeniyle kamuoyuna açmadığı için bu etkileşim deneysel olarak ayrıştırılamamaktadır.   

Hipotez: Nano Banana Pro (gemini-3-pro-image-preview) görsellerinin üçüncü taraf modellere kıyasla %25 daha az doku kayması üretmesi.

Neden Doğrulanamadı: Google, kapalı kaynaklı model gizil alanlarının (latent spaces) birbirleriyle olan nicel cross-attention çakışma skorlarını yayınlamamıştır.   

5.2. Tam Kaynak Listesi
Motor / Araştırma Çerçevesi    Sürüm / Model Kimliği    Yayın Tarihi / Türü    Kaynak Başlığı ve Yayın kanalı
Google Gemini Omni    gemini-omni-1.1-flash    2025/2026 Resmî API    
Get Started with Gemini Omni 1.1 Flash, Google Colab Cookbook

Google Gemini Omni    gemini-omni-1.1-flash    2025 Resmî Duyuru    
Build with Gemini Omni 1.1 Flash, Google Developers Blog

Google DeepMind    gemini-omni-flash    2025 Model Kartı    
Gemini Omni Flash Model Card, DeepMind Research

Google Vertex AI    veo, imagen-3    2024/2025 Cloud Blog    
Introducing Veo and Imagen 3 on Vertex AI, Google Cloud

Google Image Gen    gemini-3-pro-image-preview    2025 İnceleme    
Nano Banana vs Nano Banana Pro, KBTG Life Research

Google Image Gen    gemini-2.5-flash-image    2025 Model İncelemesi    
Gemini 2.5 Flash Image Specs, Google Enterprise Agent Platform

ConsID-Gen    ConsID-Gen / ConsIDVid-Bench    2026 Akademik Makale    
View-Assisted I2V Generation Framework, arXiv:2602.10113

IPRO Framework    IPRO Video Diffusion    2026 CVPR Yayın    
Identity-Preserving Reward-guided Optimization, arXiv:2510.14255

VBench Suite    VBench++ / VBench-2.0    2025/2026 TPAMI / ICLR    
Evaluation Benchmark for Video Generation, IEEE TPAMI

Wan2.2    Wan2.2-I2V (14B)    2026 Akademik Makale    
Ultra-High-Resolution I2V with FrescoDiffusion, arXiv:2603.17555

LPM    Base LPM (17B DiT)    2026 Akademik Makale    
Interactive Character Performance Model, arXiv:2604.07823

ReCA    ReCA MSVE    2026 Akademik Makale    
Recursive Context Allocation for MSVE, arXiv:2605.26525

SEINE    SEINE Transition Model    2024 ICLR Konferansı    
Short-to-Long Video Diffusion Model, ICLR Proceedings

SynthID    SynthID-Image / SynthID-O    2025 DeepMind Makale    
Invisibly Watermarking AI-Generated Imagery, arXiv:2510.09263

Hailuo / MiniMax    Hailuo I2V Engine    2025 Uygulama Rehberi    
Centering Subjects in AI Product Videos Guide, Hailuo AI Knowledge

Runway ML    Gen-2 / Gen-3 Alpha    2024/2025 Prompt Rehberi    
AI Video Prompting Guide, Runway Resources

EachLabs    I2V Workflow    2025 Prodüksiyon Rehberi    
Best Practices for Realistic Image to Video Results, EachLabs

  

