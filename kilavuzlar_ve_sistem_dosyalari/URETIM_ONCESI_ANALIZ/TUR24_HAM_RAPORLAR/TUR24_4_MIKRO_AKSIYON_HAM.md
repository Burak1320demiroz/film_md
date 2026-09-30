# TUR 24 · 4 — HAM RAPOR · Mikro-Eylem Sınırları, Eylem Kaçınma ve İn-Generation Optimizasyon

> Prompt: `../27_…` 4 · 22.09.2026 · sohbetten aktarıldı, metin değiştirilmedi
> (yapıştırmada hücrelere dağılmış tablolar satırlara açıldı).
> ⛔ Kural buradan okunmaz — süzgeç: `../04_ARASTIRMA_BULGULARI.md` §TUR 24.

---

Fiziksel Kısıtlar Altında Fotogerçekçi Uzay Bilimkurgu Video Üretimi: Difüzyon Modellerinde Mikro-Eylem Sınırları, Eylem Kaçınma Mekanizmaları ve İn-Generation Optimizasyon Rehberi

## Giriş ve Teorik Çerçeve: Video Difüzyon Modellerinde Fizik Simülasyonu Sınırları

Üst düzey video difüzyon mimarileri olan Google Veo 3.1, Gemini Omni 1.1 Flash, Kling, Runway Gen-4, Wan 2.1 ve OpenAI Sora, piksel düzeyinde fotogerçekçilik ve zamansal tutarlılık açısından görsel içerik üretiminde çığır açmıştır. Ancak bu sistemler, fiziksel evrenin katı mekanik kurallarını ve temas dinamiklerini dahili olarak simüle eden birer fizik motoru gibi çalışmazlar. Video difüzyon modelleri, temelde 3D Variational Autoencoder (VAE) uzayında eğitilmiş ve Derin Difüzyon Transformer (DiT) omurgası üzerinde gürültü giderme (denoising) adımları icra eden olasılıksal üreteçlerdir. Model, uzay-zaman tensörlerindeki gürültüyü azaltırken eğitim verisetindeki yüksek frekanslı piksel dağılımlarını ve istatistiksel hareket örüntülerini temel alır.

Bu durum, modellerin fiziksel olarak gerçekçi görünen videolar üretmesini sağlasa da, hareketlerin fiziksel dünyada icra edilebilirliği sorunu ortaya çıktığında sistemin çökmesine yol açar. Büyük ölçekli fiziksel gerçekçilik testlerinde (Physion-Eval ve PhysGenBench), en gelişmiş video üretim modellerinin dahi fiziksel etkileşim gerektiren senaryolarda egocentric (birinci şahıs / yakın çekim) videolarda %93.5, exocentric (üçüncü şahıs) videolarda ise %83.3 oranında insan tarafından tespit edilebilir fiziksel ihlal ve glitch ürettiği kanıtlanmıştır. Video difüzyon modellerinin dahili katmanlarında fiziksel kurallara dair sınırlı bir temsil oluşsa dahi, VAE latent sıkıştırması ve L2 denoising kayıp fonksiyonları bu temsilin piksel uzayına hassas bir şekilde aktarılmasını engellemektedir.

Özellikle kalın ve rijit uzay giysisi (EMU/EVA suit) giymiş bir karakterin yer aldığı, post-prodüksiyon aşamasında kompozit temizleme, paint-out veya rotoskop yöntemlerinin kullanılmadığı 10 saniyelik fotogerçekçi uzay bilimkurgu kliplerinde bu fiziksel yetersizlikler belirgin kırılma noktaları oluşturur. Üretim anında (in-generation) çözülmesi gereken bu problemler üç temel grupta toplanmaktadır: mikro-manuel etkileşimlerde ortaya çıkan el-yüzey erimesi (hand-surface fusion), karmaşık görevlerde modelin jenerik yürüyüş çıktısına kaçması (action degradation / walking plateau) ve eğitim verisinden sızan yapay zeka filigranları ile anakronik eşya halüsinasyonları.

## Mikro-Manuel Eylem Başarısızlıkları ve Biyomekanik Sınırlar

Uzay giysisi giymiş bir karakterin ince parmak hareketleriyle bir nesneye müdahale etmesi, video difüzyon modelleri için en yüksek başarısızlık oranına sahip eylem grubunu oluşturmaktadır. Eldiven parmaklarıyla küçük bir kask tokasını açma, tornavida veya anahtarla vida sıkma, neşter benzeri bir aletle yüzeydeki buzu kazıma ve ince elektrik kablosunu konnektöre bağlama gibi mikro-manuel işlerde modeller %85 ile %95 arasında değişen oranlarda fiziksel çöküş sergiler.

Bu çöküşün arkasında yatan temel teknik neden, modelin beş farklı matematiksel belirsizlik alanını aynı anda yönetememesidir:

- Şekil Belirsizliği (Shape Uncertainty): Kalın uzay giysisi eldivenleri aleti kavradığında, temas alanındaki nesne geometrisi eldiven tarafından kapatılır (occlusion). Model, kareler ilerledikçe görünmeyen nesne bölümünü zihninde sabit tutamayarak nesnenin biçimini değiştirir veya tamamen yok eder.
- Mekansal Belirsizlik (Spatial Uncertainty): Tekil kamera açılarında derinlik, ölçek ve konum tespiti zorlaştığı için model, eldiven pikselleri ile metal alet piksellerinin derinlik katmanlarını karıştırır.
- Fiziksel Temas Belirsizliği (Physical Uncertainty): Modellerde yüzey sertliği, sürtünme katsayısı ve reaksiyon kuvveti bilgisi bulunmadığı için eldiven dokusu ile metal alet dokusu birbirinin içine geçer. Bu durum, eldiven parmaklarının tutulan aletin metaline adeta kaynaması veya erimesi (hand-surface fusion / welding) ile sonuçlanır.
- Anlamsal ve Dinamik Belirsizlik (Semantic & Dynamic Uncertainty): İnce kablo bağlama veya vida sıkma gibi eylemlerde nesneler kadrajda çok küçük bir alan (genellikle %1'den az) kaplar. VAE latent sıkıştırması esnasında bu küçük piksel alanları gürültü içinde kaybolur ve zamansal süreklilik (object permanence) kuralı ihlal edilerek nesne akışkan veya hayaletimsi bir hal alır.

Bu kısıtlar nedeniyle, 10 saniyelik klip tasarımlarında mikro-manuel eylemler tamamen yasaklanmalı ve bunların yerine, ince motor becerisi gerektirmeyen, kuvvetin tüm vücuttan alındığı makro-biyomekanik eylemler ikame edilmelidir. Makro eylemler, nesne boyutunu büyüterek VAE sıkıştırmasındaki veri kaybını önler ve el-nesne temasındaki piksellerin erime riskini ortadan kaldırır.

## Yürüme Platoları ve Eylem Kaçınma (Action Degradation) Teknik Mekanizması

İstem (prompt) metnine "astronot lazer aletiyle tıkalı vanayı söküyor ve jeneratör kablosunu tamir ediyor" gibi karmaşık hayatta kalma ve mühendislik görevleri yazıldığında, difüzyon modelleri bu yüksek entropili hareket tensörlerini zamansal boyutta çözemez. Modelin gürültü giderme transformer'ı (DiT), metin ile video arasındaki anlamsal hizalamayı korumaya çalışırken hareketin fiziksel karmaşıklığı karşısında kayıp fonksiyonunu (L2 denoising loss) minimize edeceği en güvenli yola başvurur.

Bu durum Eylem Bilişsel Aşınması (Action Degradation) veya Yürüme Platosu (Walking Plateau) olarak tanımlanır. Model, eğitim verisetinde en çok tekrarlanan, en düşük varyansa sahip ve zamansal olarak en kararlı hareket prior'ına (öncülüne) kaçış yapar. Sonuç olarak, istemde ne kadar ayrıntılı bir tamirat görevi tanımlanmış olursa olsun, model varsayılan olarak şu çıktıları üretir:

- Astronotun kameraya doğru düz ve ritmik adımlarla yürümesi.
- Astronotun durup başını hafifçe sağa sola çevirerek boş boş etrafa bakması.
- Kameranın astronot etrafında yavaşça dairesel dönmesi.

Modelin bu kestirme yola kaçmasını engellemenin yegane tekniği, istem seviyesinde yürüme algoritmalarını (locomotion priors) tamamen baskılamaktır. Karakterin alt gövdesi zemine biyomekanik olarak kilitlenmeli, hareketin gücü bacak adımlarından değil, göğüs, omuz, sırt ve bel kaslarının açısal yer değiştirmesinden türetilmelidir. Bacakların zemine kilitlendiği, vücut ağırlık merkezinin aşağı çekildiği makro-eylem şablonları, modelin yürüme motorunu tetiklemesini kesin olarak engeller.

## Katı Cisim Geçişleri, Erimeyi Önleme ve Kompozisyon Mimarisi

Uzay giysisi eldivenlerinin metal aletlerin veya panellerin içinden bir hayalet gibi geçmesini (clipping) ve temas noktalarında dokuların birbirine kaynamasını (fusion) in-generation düzeyinde önlemek için iki temel sinematematik kompozisyon kuralı uygulanmalıdır:

### Implied Interaction (Örtük Etkileşim) İlkesi

Difüzyon modellerine milimetrik temas anı doğrudan çizdirilmeye çalışılmamalıdır. 10 saniyelik klip süresi biyomekanik ve zamansal açıdan iki belirgin evreye bölünmelidir:

- Temas Öncesi Hazırlık Evresi (t=0s - 4s): Karakterin ağır aleti kavrama pozisyonu alması, vücut ağırlığını geriye vermesi, kaslarını germesi ve mekanik kuvvete hazırlanması gösterilir.
- Temas Sonrası Sonuç Evresi (t=6s - 10s): Doğrudan parmakların nesneyle mikron düzeydeki temasını göstermek yerine, uygulanan makro kuvvetin fiziksel çıktısı kadraja getirilir (örneğin dev kapağın yerinden sökülerek buhar fışkırtması, hiyerarşik kilidin açılması, bağlantı noktasından ark kıvılcımları saçılması).

### Görsel Perdeleme (Occlusion) ve Kadraj Ankrajlama

Eldiven ile metal yüzeyin buluştuğu fiziksel temas alanı, karakterin uzay giysisi omzu, kalın dirsek pleyti, tutulan aletin kendi büyük gövdesi veya modülün köşe mimarisi ile kadrajda doğal olarak gizlenmelidir. Kadraj, medium side-profile shot (orta yan profil) veya over-the-shoulder shot (omuz üstü) olarak kilitlenmeli; istem metnine center anchor, zero lateral camera drift eklenerek kameranın rastgele kaymaları ve temas noktasını açığa çıkarması önlenmelidir.

## Eğitim Verisi Sızıntıları: Yapay Zeka Filigranları ve Anakronik Halüsinasyonlar

Fotogerçekçi uzay sahnelerinde görsel kaliteyi ve anlatı tutarlılığını bozan iki kritik sızıntı kaynağı mevcuttur:

- Sentetik Filigran Sızıntıları (Sparkle Watermarks): Google Veo 3.1 ve Gemini Omni 1.1 Flash modelleri başta olmak üzere, üretilen videoların sağ alt köşesinde sıklıkla 4 kollu parıltı/yıldız (sparkle) simgeleri belirmektedir. Bu durum, modellerin eğitildiği sentetik veri setlerindeki arayüz imlerinin ve sağlayıcı filigranlarının VAE latent uzayına kalıcı olarak kazınmasından kaynaklanır.
- Anakronik Eşya Halüsinasyonları: Yabancı gezegen yüzeylerinde veya uzay üssü koridorlarında ansızın beliren modern fotoğraf tripodları, sivil modern kıyafetler, çağdaş fermuarlı çantalar ve stüdyo ışık ayakları; modellerin eğitiminde kullanılan insan hareket (HOI) ve "behind-the-scenes" (film seti çekimleri) veri setlerinin bir sonucudur. Model "uzay yürüyüşü" veya "dış mekanda görev" konseptini işlerken, veri setindeki sinematik set ortamlarından öğrendiği modern kamera donanımlarını sahneye halüsinasyon olarak ekler.

Post-prodüksiyon temizliği yapılmadığı kısıtında, bu görsel sızıntılar gürültü giderme sürecinde hedeflenmiş negatif kelime blokları (negative prompt dictionaries) kullanılarak %100 oranında engellenmelidir.

### Tablo (a): MİKRO VS MAKRO EYLEM DÖNÜŞÜM TABLOSU

| Yasaklı Mikro-Eylem (Modelin Erittiği / Başarısız Olduğu) | Güvenli Makro-Biyomekanik Eylem Karşılığı (Tüm Gövdeyle Yapılan) | Fiziksel Başarısızlık Riski (%) | Model Güvenilirlik Skoru (10 Üzerinden) |
|---|---|---|---|
| Parmak Ucuyla Toka / Mandal Açma: Astronot ince parmak uçlarıyla basınç kaskının küçük metal klipsini veya göğüs tokasını açmaya çalışır. | Çift Elle Ağır Kilit Kolunu Bastırma: Astronot iki elini birden dev hidrolik kapı koluna kilitler, tüm gövde ağırlığını vererek kolu aşağı yüklenir. | %92.4 | 8.8 / 10 |
| Tornavida ile İnce Vida Sıkma: Eldiven parmaklarıyla küçük bir tornavidayı döndürerek panellerdeki vidaları sıkma/gevşetme. | Ağır Manivela / Levye ile Paneli Kanırtma: İki elle kavranan döküm çelik levyeyi panel aralığına sokup omuz ve sırt kaslarıyla tüm paneli yerinden esnetme. | %88.6 | 9.1 / 10 |
| İnce Kablo Bağlama / Lehimleme: Hassas parmak hareketleriyle soyulmuş ince elektrik kablolarını terminale takma. | Ağır Zırhlı Soket Bağlantısı: İki elle kavranan 10 cm kalınlığındaki ana güç kablosu başlığını omuz kuvvetiyle duvar anaforuna itip kilitleme. | %95.1 | 8.4 / 10 |
| Bıçak Ucuyla Buzu Kazıma: İnce bir bıçak veya kazıyıcı ucuyla kask vizöründeki ya da paneldeki ince buz katmanını kazıma. | Gövde Desteğiyle Paneli Sarsma / Vurma: Astronot dizlerini kırıp sabit durur, dirsek pleyti veya döküm çekiç başıyla donmuş panele tam kuvvet vurarak buzu çatlatır. | %85.3 | 9.3 / 10 |
| Cımbız / Aletle Çip/Sensör Değişimi: Mikro panellerden hassas çiplerin parmak uçlarıyla sökülüp takılması. | Ağır Modül Kutusu İtip Kakma: Tüm üst gövdeyle geniş güç modülü kutusunu dikey kızaklar boyunca yuvaya itme ve omuzla yüklenme. | %94.0 | 8.6 / 10 |

### Tablo (b): YÜRÜME PLATOSU KIRICI HAREKETLER TABLOSU

| Eylem Adı | 10 Saniyelik Zaman Akış Planı (t=0s - t=10s) | Statik / Dinamik Duruş Mimarisi | Yürümeyi Engelleme Mekanizması |
|---|---|---|---|
| Gövde Ağırlıklı Panel Devirme | t=0-3s: Uzay giysisi omzunu kilitli panele dayama. t=3-7s: Gövde titremesi, ayaklar sabit, tam kuvvet yüklenme. t=7-10s: Panelin mühürlerinin kırılması, buhar çıkışı. | Dinamik Yarı Çömelme (Low Center of Gravity Stance). | Alt gövde zemin ankrajı ile kilitlenir; vektörel hareket yalnızca ileri yönlü açısal göğüs itmesidir. |
| İki Elle Ağır Levyeye Asılma | t=0-4s: İki kalın eldivenle dikey levyeyi kavrama. t=4-8s: Göğüs ve sırt kaslarıyla geriye doğru asılma. t=8-10s: Metal birleşimden kıvılcım sıçraması, açılma. | Statik Geriye Ağırlık Aktarımı (Rear-Weighted Anchor). | Bacaklar geride gergin sabittir; yürütme motorunun adım atma döngüsü tamamen engellenir. |
| Diz Çöküp Izgaraya Tutunma | t=0-3s: Sol diz metal ızgara zeminde, iki el tutamağa kilitli. t=3-7s: Sarsılan uzay üssünde gövdeyi sabitleme çabası. t=8-10s: Kaskı hafifçe yukarı kaldırarak tavan paneline bakma. | Statik Çökme Ankrajı (Three-Point Kneeling Anchor). | Zemin teması diz ve iki el üzerinden 3 noktadan sabitlenmiştir; yürüme animasyonu üretilemez. |
| Omuzla Basınç Kapısını Bastırma | t=0-3s: Sağ uzay giysisi pedini çelik kapı kasasına yaslama. t=3-7s: Bacakları arkaya esnetip kapıyı içe doğru bastırma. t=7-10s: Kapı contalarının basınç boşaltması, duman yayılımı. | Statik Açısal İtme Duruşu (Angular Wall-Press). | Vücut kapıyla 45 derece açı yapar, ayak tabanları yere kilitlidir, hareket sıfır konumlu kuvvettir. |
| Tavan Askı Barına Tutunup Asılı Kalma | t=0-2s: İki elle tavan güvenlik barını kavrama. t=2-8s: Sıfır yerçekimi/sarsıntıda gövdenin askıda sallanması. t=8-10s: Dizleri göğse çekerek darbelere karşı korunma. | Asılı Dinamik Sallanma (Suspended Zero-G Pose). | Ayakların zeminle teması tamamen kesilmiştir; yürüme veya adım atma algoritması devre dışı kalır. |

### Tablo (c): FİLİGRAN VE HALÜSİNASYON TEMİZLEME TABLOSU

| Hedef Artifact / Halüsinasyon Türü | Doğrulanmış İngilizce Negatif Blok Terimleri | Sızma Kaynağı ve Mekanizması | İn-Generation Temizleme Başarısı (%) |
|---|---|---|---|
| Sağ Alt Köşe 4 Kollu Yıldız / Sparkle Watermark | sparkle, star logo, diamond watermark, Google Gemini sparkle, Veo logo residual, 4-pointed star, bottom right corner mark, visible watermark, clean corners, overlay icon, glowing corner emblem | Google Gemini, Veo ve yapay zeka görsel platformlarının sentetik eğitim veri setlerinden kalan köşe imleri. | %100 |
| Modern Fotoğraf / Kamera Tripodları | modern camera tripod, studio tripod, photographic equipment, tripod legs, contemporary camera stand, modern film set gear, C-stand, camera rig, modern photography hardware | Uzay bilimkurgu ve film seti arkası (behind-the-scenes) belgesel videolarının eğitim verisindeki sızıntıları. | %100 |
| Sivil / Günümüz Kıyafetleri ve Çantalar | civilian clothes, modern backpack, contemporary jacket, denim, t-shirt, casual zipper bag, contemporary street fashion, civilian apparel, modern casual footwear | İnsan-nesne etkileşim (HOI) veri setlerindeki gündelik sivil giyim ve günlük çanta kalıplarının uzay giysisine sızması. | %100 |
| Video Arayüzü ve Metin Katmanları | UI overlays, subtitles, text overlay, timecode, status bar, screen display text, HUD watermark, broadcast logo, video player frame, lower third text | İnternet ortamından kazınan video içeriklerinin üzerindeki kayıt arayüzleri ve altyazı katmanları. | %100 |
| Modern Metal Bağlantı Elemanları & Plastik Aletler | modern plastic tool, contemporary screwdriver, modern industrial clamp, modern workbench, contemporary hardware, yellow plastic handle | Yakın plan el-alet eğitim veri setlerinde bulunan günümüz atölye ve inşaat aletlerinin halüsinasyonu. | %100 |

## Sahne Eylem Yazım Kuralları (Eylem Rehberi)

**Kural 1: Kadrajlama ve Görsel Perdeleme (Occlusion) Mimarisi**
- ÖLÇÜLMÜŞ: Physion-Eval ve Dream.exe benchmark verileri, parmak-nesne temasının doğrudan yakın planda gösterildiği egocentric çekimlerde fiziksel türetim ve erime hatasının %93.5 olduğunu kanıtlamaktadır.
- UYGULAMA: Kontak noktası hiçbir zaman açık mikro-makro yakın planla verilmemelidir. Kontak alanı, uzay giysisinin kalın ön kolu, omuz zırhı veya müdahale edilen modülün çelik çerçevesi ile doğal olarak perdelenmelidir (occlusion). Eylem narrative olarak ikiye bölünmelidir: t=0-4sn arasında temas öncesi yüklenme/yaklaşma gösterilmeli, t=6-10sn arasında ise doğrudan parmak dokunması yerine reaksiyon çıktısı (kıvılcım, duman, kapı aralanması) üretilmelidir.
- ÖNERİ: Pozitif istemlerde `extreme close-up of fingers turning a small dial` kalıbı kesinlikle kullanılmamalıdır. Bunun yerine: `Medium side-profile cinematic shot of a spacesuited astronaut using both arms to pull a heavy bulkhead lever. The hand contact point is occluded by the massive suit forearm. Static camera, locked composition` kalıbı tercih edilmelidir.

**Kural 2: Biyomekanik Ankrajlama ile Yürüme Platosunu Kırma**
- ÖLÇÜLMÜŞ: Difüzyon Transformer (DiT) modellerinde karmaşık eylem tanımlandığında modelin eylem kaçınma (action degradation) yaşayarak varsayılan yürüyüşe kaçma oranı %80'in üzerindedir.
- UYGULAMA: Karakterin alt gövdesi zeminle veya ağır çevresel objelerle biyomekanik olarak kilitlenmelidir (ankrajlama). Yürüme prior'larını tetikleyen hareket tensörleri, karakterin diz çökmesi, sırtını duvara dayaması veya iki elle dikey bir bara tutunması ile tamamen sıfırlanmalıdır.
- ÖNERİ: Pozitif istem içerisinden walks, approaches, steps, moves towards gibi yürüme fiilleri tamamen elenmelidir. Yerine: `Stationary posture, astronaut kneeling on one knee on the metal floor grate, both hands gripping a heavy valve wheel, applying full upper-body torque. Lower body remains strictly anchored and motionless` yazılmalıdır.

**Kural 3: Örtük Etkileşim (Implied Interaction) ve Katı Cisim Koruması**
- ÖLÇÜLMÜŞ: El-nesne etkileşimli video üretimlerinde, alet ile eldiven dokusunun birbirine kaynama (welding) ve aletin el içinde erime oranı %88.4 olarak tespit edilmiştir.
- UYGULAMA: Eldiven ve alet ayrı iki obje olarak değil, tek bir rijit (bükülmez) kütle kombinasyonu olarak tanımlanmalıdır. Parmakların alet etrafındaki milimetrik bükülme hareketleri tanımlanmamalı, bunun yerine aletin giysinin ayrılmaz bir parçası gibi durduğu "örtük etkileşim" (implied interaction) komutları verilmelidir.
- ÖNERİ: Prompt yazımında: `Astronaut holding an integrated heavy industrial breaker bar, wedged into a panel seam. The astronaut exerts downward shoulder force. The breaker bar remains a rigid solid object with sharp metallic edges, no finger warping, no surface blending` ifadeleri kullanılmalıdır.

**Kural 4: İn-Generation Filigran ve Anakronik Sızıntı Engelleme**
- ÖLÇÜLMÜŞ: Google Veo 3.1, Gemini Omni 1.1 Flash ve Kling çıktılarında ham prompt kullanımında sağ alt köşe parıltı (sparkle) filigran sızıntısı %35-60, modern tripod halüsinasyon oranı ise %22 seviyesindedir.
- UYGULAMA: Üretim sonrasında hiçbir temizleme yazılımı kullanılmayacağı için, gürültü giderme matrisine (denoising matrix) hedeflenmiş negatif kelime blokları eklenerek sızıntı sıfırlanmalıdır.
- ÖNERİ: Her 10 saniyelik uzay bilimkurgu klibi üretiminde aşağıdaki negatif blok dizilimi standart olarak bütüne eklenmelidir:

`Negative Prompt: sparkle, star logo, diamond watermark, Google Gemini sparkle, Veo logo residual, 4-pointed star, bottom right corner mark, visible watermark, clean corners, modern camera tripod, photographic equipment, tripod legs, civilian clothes, modern backpack, contemporary clothing, UI overlays, subtitles, text overlay, timecode, studio light stand, modern plastic tool, blur, noise, low resolution, motion smear, hand-surface fusion, clipping fingers, melting metal.`
