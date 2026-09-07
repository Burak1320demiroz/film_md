# TUR 12 · RAPOR 2 — GÖRÜNÜŞ AÇILARI, SAYFA MİMARİSİ, ÖLÇEK VE REFERANS IŞIĞI (ham metin)

> Girdi promptu: `../15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` PROMPT 2
> Koşu tarihi: 06.09.2026 · Sahibin yapıştırdığı metin, DEĞİŞTİRİLMEDEN.
> Süzme: `../04_ARASTIRMA_BULGULARI.md` §TUR 12

---

Yapay Zekâ Destekli Sinematik Üretimde Varlık Kilitleme ve Referans Kareleri Optimizasyonu

Yapay zekâ tabanlı görsel üretim (image-to-video) sistemleri, özellikle iki ila yirmi dakikalık kısa metrajlı anlatılarda, sahneden sahneye tutarlılığı koruma konusunda kritik yapısal zorluklar sunar. Karakterlerin uzay ortamına uygun biçimde basınç giysili ve kasklı tasarlandığı; dolayısıyla insan kimliğini ele veren yüz, ten, saç ve mimik gibi biyometrik ayırt edicilerin örtüldüğü senaryolarda, izleyicinin ve makine öğrenimi modelinin nesneyi tanıması tamamen form, siluet, donanım topolojisi ve yüzey materyali üzerinden gerçekleşir. Bu koşullar altında üretim hattının tek bir video kanalı üzerinden seri ilerleyebilmesi, varlıkların (assets) üretime girmeden önce matematiksel ve görsel olarak kilitlenmesini zorunlu kılar.

Bu rapor, söz konusu referans karelerinin nasıl çizileceği, kadrajlanacağı, aydınlatılacağı ve test edileceğine dair endüstri standartlarını, bilişsel psikoloji teorilerini ve makine öğrenimi kısıtlarını sentezleyerek dört ana analitik yapıda sunmaktadır.

## 1. Zorunlu Görünüş Açıları ve Hacimsel Sınırların Sabitlenmesi

Bir karakterin veya mekanik donanımın üç boyutlu hacminin, iki boyutlu bir referans karesine dönüştürülmesi (turnaround / model sheet), geleneksel animasyondan modern görsel efekt (VFX) süreçlerine kadar uzanan köklü bir standartlar dizisidir. Özellikle basınç giysilerinin kütlesel ağırlığı ve asimetrik modülleri söz konusu olduğunda, eksik bırakılan her görünüş açısı, yapay zekâ modelinin gizil uzayında (latent space) bir veri boşluğu yaratır. Model, bu boşluğu doldurmak için bağlamsal halüsinasyonlara başvurur; bu da videonun saniyeleri akarken donanımın erimesi, şekil değiştirmesi veya hacmini yitirmesi ile sonuçlanır.

Endüstri standardı dönüşüm sayfaları temel olarak dört noktalı veya beş noktalı dönüşlerden oluşur. Ancak uzay giysileri gibi kompleks topolojilerde sırt ve tepe görünümlerinin eksikliği telafi edilemez hatalara yol açar. Tepe görünümünün (top view) eksikliği, omuz genişliğinin karakter kendi etrafında dönerken dalgalanmasına, uzamsal ayak izinin (footprint) yanlış hesaplanmasına ve tepe ışığının (rim light) materyal üzerindeki speküler kırılımının yanlış konumlanmasına mal olur.

Özellikle kapalı bir sırt görünümü, yapay zekâya yalnızca "ön yüzün yokluğu" olarak tanımlanamaz. Pozitif bir ifadeyle; yaşam destek ünitesinin (PLSS) topolojik akışı, termal yalıtım dikişlerinin yönelimi, oksijen hortumlarının giriş noktaları, asimetrik valf kilitleri ve kumaşın omuz bıçakları üzerindeki gerilim hatları (tension lines) olarak açıkça çizilmeli ve kilitlenmelidir. Bu veriler eksik olduğunda, model karakter arkasını döndüğünde göğüs plakasındaki detayları sırt bölgesine kopyalar (texture bleeding) veya sırt çantasını bedene gömük iki boyutlu bir katman gibi algılar.

İnsan dışı bir canlı ya da alışılmadık bir makine tasarlandığında, ön, yan ve arka görünümlerin tek bir kadrajda mı yoksa ayrı karelerde mi hazırlanacağı konusu, topolojik karmaşıklıkla doğrudan ilintilidir. Karmaşık uzuvlara sahip yaratık tasarımlarında görünümler kesinlikle ayrı ayrı hazırlanmalıdır; zira yapay zekâ, tek bir kompozit görseldeki farklı uzuv sınırlarını birbirine karıştırabilir. Kamera yayı, karakterin etrafında 360 derecelik dönüşü sağlamak için 60 derecelik kesin dilimlerle sınırlandırılmalıdır (0°, 60°, 120°, 180°, 240°, 300°).

| Görünüş Açısı / Ek Sayfa | Canlı Çekim | Animasyon | Görüntü Efekti | Oyun | Önlediği Somut Arıza | Sayfada Yazılacak Bilgi | Kaynak |
|---|---|---|---|---|---|---|---|
| Ön (Front) | Zorunlu | Zorunlu | Zorunlu | Zorunlu | Simetri kaybı, çapa noktası kayması, ölçek bozulması. | Orijin noktası, simetri ekseni, genel boy oranı. | Liberty Guide (2023), Quizanjacy (2020) |
| Dörtte Üç (3/4 Front) | Zorunlu | Zorunlu | Zorunlu | Zorunlu | Derinlik yanılsaması eksikliği, hacimsel düzleşme. | Perspektif daralma oranları, uzak omuz hizası. | Liberty Guide (2023) |
| Profil (Side) | Zorunlu | Zorunlu | Zorunlu | Zorunlu | Omurga eğrisinin düzleşmesi, kask ön çıkıntısının çökmesi. | Kütle merkezi, öne eğim açısı. | Liberty Guide (2023) |
| Dörtte Üç Arka (3/4 Back) | Opsiyonel | Zorunlu | Zorunlu | Zorunlu | Pelvis eğiminin yanlış hizalanması, sırt ekipmanlarının silueti bozması. | Kemer hattı, sırt çantası izdüşüm derinliği. | Liberty Guide (2023) |
| Arka (Back) | Zorunlu | Zorunlu | Zorunlu | Zorunlu | Yükseklik aktarım hataları, çanta bağlantı hataları. | Topolojik akış, yaşam destek girişleri, valf asimetrileri. | Liberty Guide (2023), VES Handbook (2024) |
| Tepe (Top) | Opsiyonel | Opsiyonel | Zorunlu | Zorunlu | Omuz genişliği dalgalanması, tepe ışığı kırılım hataları. | Omuz-kalça genişlik oranı, kask tepe radyusu. | Anekdot (Oyun/VFX Lookdev Pratiği, 2023) |
| Alt (Bottom) | Opsiyonel | Opsiyonel | Opsiyonel | Zorunlu | Ayakkabı taban izi uyuşmazlığı, körük kayıpları. | Zemin bası noktaları, taban oluk desenleri. | Anekdot (2023) |
| Kostüm Katmanı | Zorunlu | Zorunlu | Zorunlu | Zorunlu | Kumaş altı anatomi belirsizliği, eklem kırılması. | Alt katman dikiş yerleri, kumaş esneme payı. | Liberty Guide (2023) |
| Aksesuar (Prop) | Zorunlu | Opsiyonel | Zorunlu | Zorunlu | Araç/gereçlerin eldiven ölçeğiyle uyuşmazlığı. | Bedene kilitlenme noktaları ve tork. | Liberty Guide (2023), VES Handbook (2024) |
| El ve Ayak (Makro) | Opsiyonel | Zorunlu | Zorunlu | Zorunlu | Mafsal bükülmelerindeki hacim erimeleri. | Basınçlı eldiven şişkinliği, mafsal sayısı. | Anekdot (2021) |
| Makro Mekanizma | Zorunlu | Opsiyonel | Zorunlu | Zorunlu | Vizör kilit ve valflerinin hareket sırasında yok olması. | Dönme eksenleri, kilit tork yönleri, conta hatları. | NASA TP-2004-212068 (2004) |
| Hasar Durumu (Damage) | Zorunlu | Opsiyonel | Zorunlu | Zorunlu | Yıpranma/çizik dokularının rastgeleleşmesi. | Yıpranma gradyanı, karbon yanık izlerinin koordinatları. | Anekdot (2022) |

## 2. Sayfa Mimarisi, İzolasyon ve Ayırt Edilebilirlik Kanıtı

Birden çok görünümü tek bir ızgara (grid) veya kontakt sayfasında (contact sheet) toplamak, geleneksel 3D üretim süreçlerinde sanatçıların topolojiyi genel bir bakışla algılaması için standarttır. Ancak bu durumun yapay zekâ tabanlı üretim hattındaki sınırları oldukça katıdır. Difüzyon tabanlı görüntüden videoya dönüşüm sistemleri, yüksek çözünürlüklü 4K girdilerle çalışırken mekânsal dikkat haritalarını korumakta zorlanır. Bir sayfaya birden fazla figür yerleştirildiğinde, "çini denoise" (tiled denoising) süreçleri lokal yapıları korurken global dizilim tutarlılığını kırabilir, piksellerin bilgi yoğunluğunu (texel density) düşürür ve detay kaybına yol açar.

Endüstri standardı model sayfalarında figürlerin etrafında ölçü çizgileri, oklar, etiketler ve başlıkların bulunması bir normdur. Ancak görsel girdi olarak doğrudan bir yapay zekâ modeline beslenecek bir referans sayfasında bu tür vektörel ve tipografik işaretlemelerden kaçınılmalıdır. Model, bu etiketleri ve okları karakterin fiziksel materyaline veya uzay ortamına ait dokusal hatalar (artifacts) olarak yorumlama eğilimindedir. Sadece yatay uzamsal rehber çizgileri — burun, omuz, diz ve ayak hizalarını belirten ve çok ince çizilmiş kontrastlı çizgiler — kullanılabilir.

Boy ve karşılaştırma (line-up) sayfaları, evren içi ölçeğin kurulması için elzemdir. Bir uzay gemisinin, rover'ın veya devasa bir maden yapısının ölçeğini kanıtlamak için mutlaka "ölçek şahitleri" (scale witnesses) kullanılmalıdır. NASA standartlarına göre bu şahitler; 95. persentil bir insan figürü, modüler bir geçiş kapısı, merdiven basamağı, standart uzay yürüyüşü tırabzanı (handrail) veya bir eldivenin tutabileceği boyutlardaki modül kollarıdır.

İki figür birbirine benziyorsa (örneğin iki ayrı branştan astronot) aynı sayfada yan yana gösterilip gösterilmeyeceği, testin doğasına bağlıdır. Doğrudan kıyaslama yapılmayan her üretim karesinde, figürler kendi kadrajlarında izole edilmelidir.

### İzolasyon ve Birleştirme Karar Ağacı

1. Referans karesinin nihai tüketicisi kimdir?
   - İnsan 3D sanatçısı → Tüm görünümleri ölçü çizgileriyle tek ızgarada topla.
   - Ardışık video üretecek yapay zekâ modeli (I2V) → Adım 2.
2. Hedef varlığın dokusal karmaşıklığı ne seviyededir?
   - Yüksek frekanslı ince detay (kask mikro-valfleri, yıpranmış kumaş iplikleri) → Ayrı kareler üret (texel density düşer).
   - Düşük frekanslı, pürüzsüz, stilize form → Adım 3.
3. İki figür arasında boyut/tasarım karşılaştırması mı hedefleniyor?
   - Boy kıyaslaması (line-up) → Aynı sayfada, aralarında %20 genişliğinde negatif boşluk bırakarak yan yana koy.
   - Figürleri kendi sahneleri için kilitlemek → Adım 4.
4. Kullanılan difüzyon modeli "tiled-denoising" mimarisine sahip mi?
   - Standart bütünsel işlemci → Ayrı kareler üret (feature bleeding engellenir).
   - FrescoDiffusion gibi global tutarlılığı koruyan yapı → Tek sayfada ızgara kurulabilir.

### Okunabilirlik ve Ölçek Testleri Kontrol Listesi

Bilişsel psikolog Irving Biederman'ın Tanıma-Bileşenleri (Recognition-by-Components / RBC) teorisine göre insan ve makine görüşü, nesneleri renklerinden veya ince yüzey detaylarından ziyade; silindir, koni, küp gibi temel geometrik formların (Geon) birbirleriyle olan kesişim, paralellik ve simetri (non-accidental properties) ilişkileri üzerinden algılar. Bir kask, Biederman prensiplerine göre N≥36 temel geon setinden seçilen parçaların birleşimiyle beyinde kodlanır.

| Test Adı | Sorulan Soru | Sayısal Eşik / Küçültme Boyutu | Geçme Ölçütü | Kaynak |
|---|---|---|---|---|
| Tam Karartma (Siluet) Testi | Figür tek renk siluete çevrildiğinde ne olduğu anlaşılıyor mu? | 2D Düzlem (0 Işık) / Kontrast 1.0 | Temel geon çıkıntıları (kask kavisi, omuz podyumu, sırt ünitesi) dış hatlardan tanınabilmeli. | Biederman RBC (1987) |
| Başparmak Boyutunda Okuma | Uzak çekimde iki benzer karakter ayırt edilebiliyor mu? | Orijinal çözünürlüğün %10'u (ör. 64x64 px) | Majör kütleler ve asimetriler korunmalı; feature bleeding olmamalı. | V.S. Concept Art Guidelines (n.d.) |
| Kontur Okunabilirliği (Shadow Test) | Renk silindiğinde figür arka planla eriyor mu? | Gri tonlama / value testi | Yüzey değerleri arasında belirgin kontrast geçişleri olmalı. | V.S. Concept Art Guidelines (n.d.) |
| Ölçek Şahitliği | Araç/mimari yanındaki şahitle mantıklı orantı kuruyor mu? | 1:1 ölçek hizalaması | Kapı, merdiven, korkuluk veya insan bedeni gerçek ergonomi kısıtlarıyla eşleşmeli. | NASA MSFC-HDBK-3701 (2015), TP-2004-212068 |
| Amblem/Rol Şeridi Küçültme | Yazısız rol belirteci ne kadar uzaktan algılanıyor? | Ekran yüksekliğinin %25'i | Mipmap seviyesinde amblem ile fon arasında en az 3:1 luma kontrastı. | Doku Çözünürlüğü Limitleri (2024), Anekdot |

## 3. Görünüm Geliştirme (Lookdev), Işık ve Kadraj Çözümleri

Bir yapay zekâ modeline nesnenin ne olduğunu öğretmek ile nasıl aydınlatıldığını göstermek arasındaki fark, endüstride görünüm geliştirme (lookdev) ve ışık bağlama (light linking) prosedürleriyle yönetilir. Görünüm geliştirme sunumu ve turntable animasyonları, nesnenin her türlü fiziksel sapmadan arındırıldığı kanonik (canonical) aydınlatma koşullarında hazırlanmalıdır.

Bir referans karesi, kullanılacağı dramatik sahnenin ışığında değil, mutlaka nötr stüdyo ışığında hazırlanmalıdır. Nötr, kalibre edilmiş bir HDRI (genellikle 3:1 veya 4:1 key-to-fill oranında) kullanılmasının ardındaki temel mekanizma şudur: Eğer referans karesi sert bir yönlü ışık ve keskin düşen gölgeler barındırıyorsa, difüzyon modeli bu gölgeleri nesnenin fiziksel formuna veya kalıcı rengine (albedo) ait bir leke olarak öğrenir. Video üretimi sırasında karakter hareket ettiğinde veya ortam ışığı değiştiğinde, bu boyanmış gölgeler karakterin üzerinde onunla birlikte döner. Bu durum uzamsal gerçekliğin kırılmasına yol açar. Aynı mekânın faz faz değişen ışık koşulları için ayrı kareler hazırlamaya gerek yoktur. Varlığın temel fiziksel özellikleri (albedo, roughness, F0) tek bir nötr karede sabitlendikten sonra, sahnelerin özel aydınlatma gereksinimleri metinsel yönlendirmeler veya dışsal kontrol ağları ile ortam bağlamında sonradan oluşturulmalıdır.

Turntable ve lookdev standart kadrajında, arka planın tamamen nötr olması şarttır (genellikle %18 nötr gri). Ayrıca kadraja pozlamayı ve ışık şiddetini ölçmek için 18% gri küre, çevresel yansımaları görmek için krom küre ve renk doğruluğunu onaylamak için Macbeth ColorChecker girmek zorundadır. Weta Digital'in geliştirdiği PhysLight sistemi gibi gerçek dünya birimlerine dayalı kalibrasyonlarda, bu üç referans objesi sahnedeki ışığın matematiksel olarak doğrulanabilir olmasını sağlar.

Konunun kare içinde kaplaması gereken yer, yapay zekâ modelinin sinyal/gürültü oranını maksimize edecek şekilde ayarlanmalıdır. Konu, kadrajın merkezinde olmalı, kenar payı güvenli bölge sınırlarında %10 civarında tutulmalı ve en boy oranı, üretilecek nihai filmin oranına (örneğin 16:9) tam olarak uymalıdır.

### Kasklı Figürlerin Kadrajlanması ve Aydınlatılması

Uzay filmlerinde yüzü tamamen kapatan kaskların aydınlatılması teknik bir paradokstur. Gerçek tarihsel uzay giysilerinde (örneğin Apollo EMU kasklarında), güneşi ve zararlı radyasyonu engellemek için vizörler ince altın katmanlarıyla kaplanır ve yüksek oranda yansıtıcıdır. Bu durum, astronotun yüzünü dışarıdan görünmez kılar. Ancak sinematografik anlatımda izleyicinin karakterin yüzünü şeffaf bir vizörün ardından görebilmesi istenir.

Eğer dışarıdan güçlü bir set ışığı kullanılırsa, bu ışık dışbükey vizör yüzeyinde patlamalar yaratır ve kamera ekibinin/çevrenin yansımasını vizöre hapseder. Endüstrinin bu sorunu aşmak için geliştirdiği yerleşik yöntem, kask içi lokal aydınlatmadır (internal eye lights). Kaskın iç üst kısmına ve yan yanak hizalarına yerleştirilen düşük lümenli ışık kaynakları veya ışın ayırıcı yansıtıcılar, dış ortamdan bağımsız olarak sadece aktörün yüzünü aydınlatır. Yapay zekâ referans kareleri üretirken de dış mekan aydınlatması ne kadar karanlık olursa olsun, "kask içi lokal ışıklandırma" tanımı kareye işlenmelidir.

### Fikri Mülkiyetten (IP) Kaçınma Yöntemleri

Gerçek tarihsel donanım mirasından (örneğin NASA tasarımlarından) görsel form ödünç alırken tescilli marka (trade dress) ve model adlarından kaçınmanın yerleşik yolu; donanımı doğrudan kopyalamak yerine onu Biederman'ın yapıtaşlarına (geon) kadar "soymak" (genericizing) ve yeniden birleştirmektir. Gerçek logolar, görev peçleri veya tanınmış ekipman kilit sistemleri, yerini tamamen jenerik, endüstriyel tehlike uyarılarına (chevron şeritleri, seri numarası benzeri anlamsız veri blokları, nötr renk kodlamaları) bırakmalıdır. Orijinal dikiş hatları ve birleşim noktalarının topolojik yerleri değiştirilerek işlevsellik algısı korunur ancak patentlenebilir görünüm bozulur.

### Varlık Tipi Reçete Tablosu

| Varlık Tipi | Kaç Kare | Hangi Görünümler | Arka Plan | Işık | Kaynak |
|---|---|---|---|---|---|
| İnsan (Kasklı ve Basınç Giysili) | 6 Kare | Ön, Dörtte Üç, Profil, Arka, Makro Kask/Vizör, Kask İçi Yüz. | Nötr %18 Gri (sonsuz fon) | 3:1 key-to-fill stüdyo ışığı, kask içi lokal aydınlatma. | CG Lounge (2024), SciFi SE (2017) |
| Uzay Aracı / Mekanik Yapı | 5 Kare | Ön, Profil, Tepe, 3/4 Üst Perspektif, İtici/Egzoz Makro. | Nötr Gri / Düz Zemin | Yumuşatılmış tepe ışığı, alttan yansıma. | 3D Graphics Guide (2022) |
| İç Mekân (Kabin/Koridor) | 4 Kare | Merkezden 4 ana yöne bakış. | Arka Plan Yok (kapalı geometri) | Nötr ambiyans + dengeli pratik ışıklar. | Anekdot (2023) |
| Dış Mekân (Gezegen Yüzeyi) | 3 Kare | Geniş Açı Kurulum, Orta Açı Bağlam, Zemin Detayı. | Açık Gökyüzü (skybox) | Bulutlu/difüze gün ortası, gölge uzatmayan düz ışık. | Anekdot (2023) |
| Prop (Aksesuar / Alet) | 3 Kare | Ön, Dörtte Üç, Makro Arayüz / Tutamak. | %18 Gri veya Siyah | Ürün fotoğrafçılığı ışığı; güçlü kenar ışığı + net dolgu. | Liberty Guide (2023) |
| Tekrar Eden Doğa Olayı | 3 Kare | 1: Olayın biçimi (form). 2: Kadans sayısı (density). 3: Tek düşme davranışı (motion). | Saf Siyah (kompozitleme için) | Yönlü, sert laboratuvar ışığı. | Anekdot (VFX Element Library, 2021) |
| İnsan Dışı Canlı / Biyomekanik | 7 Kare | Ön, 3/4 Ön, Profil, Arka, Tepe, Alt, Uzuv Hareketi. | Nötr %18 Gri | Düşük açılı yüzey ışığı (grazing light). | Biederman RBC (1987) |

(Tekrar Eden Doğa Olayı Reçetesi Detayı: Metan yağmuru, plazma kıvılcımı veya sıfır yerçekimi kan damlası gibi olaylarda fiziksel simülasyonu kilitlemek için ardışık üç kare kullanılır. Birinci kare damlanın küresel veya asimetrik formunu sabitler. İkinci kare, 1 metrekarelik hacimdeki parçacık miktarını yani kadans sayısını kilitler. Üçüncü kare ise sistemin hareket izini, yani tek bir partikülün saniyelik düşme davranışında bırakacağı izi gösterir. Bu üç aşama olmadan yapay zekâ, partikülleri rastgele hızlarda veya formlarda üreterek tutarlılığı yıkar.)

---

## RAPORUN KAYNAK LİSTESİ (sahibin yapıştırdığı hâliyle)

lbrtgu.com — Process Blog, Elbert Gu · dokumen.pub — The VES Handbook of Virtual Production ·
threedium.io — How To Make Superhero 3D Characters From Image ·
arc.aiaa.org — David Clark Company and the Evolution of the Spacesuit ·
aipromptgeneer.com — Master Generative AI Prompting · quizanjacy.wordpress.com — qjacymay ·
spacearchitect.org — Advanced EVA Capabilities · huggingface.co — Kazzze/AI-ArtTools-Pack ·
arxiv.org — FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion ·
ftp.pluspetrol.net — EASY SKETCHING TEMPLATE · standards.nasa.gov — MSFC-HDBK-3701.pdf ·
hailuoai.video — Creating Tileable Textures with Generative AI ·
en.wikipedia.org / pigeon.psy.tufts.edu / researchgate.net / academia.edu — Recognition-by-components theory ·
vsquad.art — Step-by-Step Character Concept Art for 3D Game Design ·
cglounge.studio — Light Linking Is a Symptom, Not a Solution ·
epdf.pub — The Visual Effects Producer · dokumen.pub — Computer Graphics for Artists ·
escooptics.com — Choosing the right optical coating ·
spacevoyageventures.com — Astronaut Helmets: Protection and Visibility in Space ·
ttu-ir.tdl.org — Electrochromic Visors for Advanced Spacesuit Helmets ·
reddit.com — It's called a LENS flare for a reason · scifi.stackexchange.com — Why internal lights on space helmets? ·
reddit.com — What is the story of scifi movies' helmets being backlit from the inside? ·
mitmecsept.wordpress.com — Intellectual Property: The Law of Trademarks, Copyrights, Patents ·
researchgate.net — How Does the Modeling Strategy Influence Design Optimization
