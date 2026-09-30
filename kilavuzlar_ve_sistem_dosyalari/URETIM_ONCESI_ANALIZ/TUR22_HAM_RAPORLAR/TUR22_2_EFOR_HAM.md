# TUR 22 · RAPOR 2 — BEDENİN YÜKÜ (ham, birebir)
> Prompt: `25_PROMPT_HATA_ONLEME_ARASTIRMA_PROMPTLARI.md` §2️⃣
> ⚠️ Oturuma yapıştırıldı, buraya birebir aktarıldı (bkz. 00_KUNYE.md).

---

Güncel Video Üretim Modellerinde İnsan Biyomekaniği ve Efor Sadakatsizliği: Fiziksel Tutarlılık, Yorgunluk Birikimi ve Temassız Hareket Analizi

Üretken yapay zeka ve difüzyon tabanlı video üretim modelleri, piksel düzeyinde görsel sadakat (perceptual realism) ve sinematik estetik açısından dikkate değer bir olgunluğa erişmiş olsalar da, bu sistemlerin temel bir fizik motoru veya dünya simülatörü olarak işlev görme kapasiteleri ciddi yapısal zafiyetler barındırmaktadır. Google Veo 3.1, Gemini Omni 1.1 Flash, Sora 2, Wan 2.1, Kling, Luma Ray, Hailuo ve Runway Gen-4/4.5 gibi öncü modellerin incelenmesi, modellerin istatistiksel örüntü eşleştirme yetenekleri ile Newton mekaniğini (özellikle kinematik ve dinamik arasındaki ilişkiyi) anlama kapasiteleri arasında derin bir uçurum olduğunu göstermektedir.

Özellikle fotogerçekçi bir uzay bilimkurgu filmi bağlamında — on saniyelik, kesmesiz, sabit kameralı, basınç giysili ve yüzün tamamen görünmediği opak vizörlü karakterlerin yer aldığı senaryolarda — insan figürünün ağır bir yükü taşıdığına dair efor işaretlerinin (sırtın bükülmemesi, omzun düşmemesi, bacaklardan destek alınmaması, kavrayışın gevşememesi, nefes ritminin değişmemesi, hareket hızının iş boyunca sabit kalması ve kalın eldivenin çıplak el gibi hareket etmesi) üretilememesi, doğrudan mimari kısıtlamalardan kaynaklanmaktadır. Bu rapor, VideoPhy-2, Physion-Eval, Morpheus, Principia ve PhyGenBench gibi fizik sadakati kıyaslamalarından elde edilen veriler ışığında, efor yanılsamasının mekanizmalarını sökmekte, yorgunluk birikimi krizini incelemekte, temassız uzuv arızalarının kök nedenlerini saptamakta ve belirtilen katı prodüksiyon kısıtları altında uygulanabilecek metin tabanlı (prompt) müdahaleleri detaylandırmaktadır.

## Mekanizmayı Sök: Modeller Yükü ve Eforu Nasıl Algılar?

Görsel-dil modelleri (VLM) ve Difüzyon Transformer (DiT) mimarilerine dayalı video üreticileri, ağırlığı, kütleyi veya yerçekimini bir simülasyon ortamındaki gibi sayısal vektörler olarak hesaplamazlar. Bunun yerine, metin kodlayıcılarından (örneğin T5-XXL veya CLIP) gelen gömüleri (embeddings), eğitim verilerindeki görsel eşzamanlılıklarla (co-occurrence) eşleştirirler. Bu durum, modelin "yükü" çevresel ve anlamsal bağlamlardan çıkarmasına neden olur.

### Yükün Çıkarım Kaynağı: Sayısal Ağırlık vs. Sıfatsal Betimleme

Model, nesnenin ağırlığını gerçek bir fiziksel değerden ziyade nesnenin adından (örneğin "kargo kasası" veya "çelik kiriş"), hacimsel boyutundan, yüzey malzemesinden (metal dokusu), fiilin kendisinden ("drag", "heave") ve en önemlisi videonun ilk karesindeki karakterin duruşundan çıkarır. Prompt tasarımında ağırlığı sayıyla yazmak ("a 40 kg case") ile sıfatla yazmak ("a heavy massive case") arasında, modelin bilişsel süreci açısından dramatik ve ölçülebilir bir fark bulunmaktadır.

T2V-CompBench ve benzeri kompozisyonel değerlendirme çalışmaları, video difüzyon modellerinin "sayısallık" (generative numeracy) ve "özellik bağlama" (attribute binding) konularında zayıf olduğunu ortaya koymuştur. Bir dil modeli "40 kg" ifadesini bağlamsal olarak anlasa da, bu matematiksel değerin video modelinin görsel gizli uzayında (latent space) doğrudan bir piksel deformasyonu karşılığı yoktur. Öte yandan, "heavy" veya "crushing" gibi abartılı sıfatlar, modelin eğitim verilerindeki devasa endüstriyel nesnelerle ve bu nesneleri kaldırırken yüzü buruşmuş, vücudu gerilmiş insan görselleriyle yüksek korelasyona sahiptir. Sayısal ağırlık belirtmek genellikle modelin "yük" kavramını tamamen göz ardı etmesiyle sonuçlanırken, abartılı sıfatlar görsel eşleşme olasılığını artırır. Buna rağmen, Physion-Eval verileri, fiziksel tutarlılığın kritik olduğu senaryolarda dış merkezli (exocentric) videoların %83.3'ünün ve iç merkezli (egocentric) videoların %93.5'inin insan tarafından fark edilebilir fiziksel (contact, force, timing) arızalar içerdiğini kanıtlamaktadır.

### Eforun Metinsel Temsili: Sonuç Odaklı vs. Beden Tarifi Odaklı Promptlar

Bir eforu tanımlarken hareketi sonuca bağlayarak yazmak ("the heavy lever moves four centimetres in the first second and one in the last") ile bedensel reaksiyonlara odaklanarak yazmak ("his forearm muscles tighten visibly through the suit, his shoulders drop under the extreme tension, his wide stance anchors him to the deck") arasındaki fark, biyomekanik sadakatsizliğin temel nedenlerinden biridir.

Sonuç odaklı promptlar, modeli pürüzsüz bir kinematik yörünge çizmeye iter. Model, kolun hareketini kusursuz bir şekilde anime ederken, arka plandaki dinamik kuvvetleri (eklem torku, yer tepki kuvveti, kas gerilimi) hesaba katacak bir iç mimariye sahip olmadığı için figürü tamamen çabasız, hafif ve ağırlıksız bir şekilde renderlar. PhyMotion araştırması, 2 boyutlu pürüzsüzlük metriklerinin yüksek puan verdiği videoların 3 boyutlu bir fizik simülatörüne aktarıldığında uzuvların birbirine girmesi, ayakların kayması ve bedenin havada asılı kalması gibi arızalar gösterdiğini belgelemiştir. VideoPhy-2 testlerinde momentumun korunumu (%39) ve sürtünme (%31) yasalarının en sık ihlal edilen kurallar olmasının nedeni, modelin hareketi bir kuvvetin (force) sonucu olarak değil, yalnızca bir yer değiştirme (displacement) olarak görmesidir.

Buna karşın, beden tarifiyle yazılan promptlar, modelin doğrudan piksel düzeyindeki dikkat (attention) haritalarını hedef alır. Model ağırlığı hissetmez, ancak "düşen omuz" veya "bükülen sırt" komutunu eğitim verilerindeki karşılıklarıyla eşleştirerek görsel bir efor illüzyonu yaratır. Karakterin vizörünün tamamen opak olduğu uzay bilimkurgu kısıtlamasında, yüz ifadelerinin (diş sıkma, göz kısma) kullanılamayacak olması, tüm efor yükünü gövde tarifine bindirir.

### Hareket Hızı Kontrolü ve Ağır Çekim (Slow-Motion) Riski

Ağır bir yükü hareket ettiren insanın doğal yavaşlamasını prompt üzerinden kontrol etmeye çalışmak, güncel T2V modellerinde genellikle istenmeyen bir yapay ağır çekim (slow-motion) arızasına dönüşmektedir. Model, nesnenin veya karakterin yavaş hareket etmesi gerektiğini algıladığında, bu yavaşlığı lokal (sadece karaktere ait) bir durum olarak değil, global bir zaman bükülmesi olarak işler.

Google Veo 3.1 ve Luma Ray üzerinde yapılan bağımsız analizler, modellerin "hareket zorluğu" ile "kare hızı (frame rate) manipülasyonunu" birbirine karıştırdığını göstermektedir. Ağırlığı hissettirmek için "moves slowly" yazıldığında, uçuşan tozlar, sarkan kumaşlar ve arka plan öğeleri de yavaşlar. Ağır çekim, eforun bir göstergesi değil, sinematik bir efekt arızasıdır. 10 saniyelik kesmesiz bir klipte eforun gerçekçi okunabilmesi için yavaşlama yerine duraksamalar (micro-pauses) kullanılmalıdır: "He pulls the lever, halts abruptly holding the tension, then pulls again." Bu yapı, modelin zamanı bükmesini engellerken mekanik direnci görselleştirir.

### Kamera Ölçeğinin Efor Okunurluğuna Etkisi

Yakın Plan (Önkol ve Eller): Difüzyon modellerinin ince motor kontrolündeki yetersizlikleri en çok burada göze çarpar. Kalın uzay eldiveninin çıplak el gibi bükülmesi, parmakların nesneye nüfuz etmesi (self-penetration) veya kavrayışın hiç gevşemeden objeye kaynaşması (object fusion) çok yaygındır.

Orta Plan (Gövde): Eforu iletmek için en güvenli ve etkili ölçektir. Yüz görünmese dahi; asimetrik omuz düşüşleri, gövdenin yük yönünde bükülmesi ve basınç giysisinde nefes nefese kalmaya bağlı genişlemeler (chest heaving) orta planda tutarlı bir şekilde okunabilir.

Geniş Plan (Tüm Figür): Bacakların zeminden destek alması beklenirken, yerçekimi ve sürtünme arızaları ortaya çıkar. Ayakların yeri kavramadan kayması (foot sliding) geniş planın en büyük riskidir.

### 10 Saniyelik Klipte Beden İşareti Üretim Sınırları

Video üretim modelleri 10 saniyelik bir süre zarfında aynı anda en fazla 2 veya 3 bağımsız beden işaretini güvenilir ve tutarlı bir şekilde üretebilir. "Temporal State Transport" teorisine göre, video modelleri uzamsal özellikleri zaman boyunca aktarırken "parçalanmış taşıma" (fragmented transport) veya "aşırı karışma" (over-mixing) sorunları yaşarlar. Eğer promptta çok fazla işaret sıralanırsa ("shoulders drop AND knees bend AND hands grip tightly AND chest heaves"), özellik kanaması (attribute bleeding) meydana gelir.

Tutan Kalıplar: İki yönlü, birbiriyle uyumlu hareketler ("leans back heavily while pulling") model tarafından tek bir bütünleşik eylem olarak algılandığı için başarı oranı yüksektir.

Tutmayan Kalıplar: Vücudun iki yarısının farklı işler yaptığı durumlar ("right arm pulls hard while left arm hangs loose") difüzyon modellerinin simetri önbilgisi nedeniyle sıklıkla bozulur.

## Yorgunluğun Birikmesi: Bağımsız Klipler Arası Durum Aktarımı

Bir filmde 12 ile 48 arasında değişen kliplerin her birinin bağımsız tohumlardan üretilmesi, yorgunluk gibi zamanla biriken durumların aktarımını "durum amnezisi" krizine dönüştürür.

### Metin Merdivenleri ve Anlamsal Durum Taşıma

Durumu korumak için metin promptuna numaralı bir merdiven eklemek ("wear state three of four" veya "fatigue level: extreme") Büyük Dil Modelleri tarafından mantıksal olarak işlenebilse de, difüzyon mimarisinin görsel üretim tarafında başarısız olur. T2V-CompBench analizleri, modellerin bu tarz soyut, sayısal ardışıklıkları piksel düzeyinde tutarlı bir kirlenme veya terleme miktarına dönüştüremediğini göstermiştir. Titreme, terleme, adım kısalması veya duruş gevşemesi gibi durumlar numaralarla değil, her klipte o duruma özgü ağır fiziksel betimlemelerle yazılmalıdır.

### İlk Kare (Image-to-Video) Referansının Sınırları

Kesmesiz klipler arası yorgunluk aktarımının belgelenmiş ve ölçülmüş tek güvenilir yolu, bir önceki klibin son karesini yeni klibin başlangıç karesi (I2V) olarak kullanmaktır. Ancak bu yalnızca statik yorgunluğu (kir, toz, hasar, çökmüş duruş) korur. Nefes nefese kalma, titreme, adımın kısalması gibi dinamik yorgunluk belirtileri statik bir görüntü piksellerine kodlanamaz.

## Serbest Uzuv ve Temassız Hareket Arızaları

Bu arızaların ana tetikleyicisi, promptta yer alan "zero-gravity", "floating in space" veya "microgravity" gibi kelimelerdir. Model bu anahtar kelimeleri gördüğünde eğitim verilerindeki astronot kliplerinin ortalama hareketlerini taklit eder, ancak momentum transferini hesaba katmaz; yalnızca görsel yer değiştirmeyi çizer.

Bu temassız hareket arızaları ile efor arızaları tam olarak aynı kökten beslenir: modellerin görünmez kuvvetleri (tork, sürtünme, tepki) hesaplayacak bir iç mekanizmaya sahip olmaması.

### Temas Noktası (Anchor Point) ve Etki-Tepki Kalıpları

Bu arızaları en aza indirmenin yolu, hareketi zorla bir temas noktasına bağlayarak yazmaktır: "He pulls himself along the rail with his right hand, his boots never touch the deck". Bu yaklaşım modele uzaysal bir referans verir ve dikkat mekanizmasını boşluktaki serbest hareketlerden ziyade el ile ray arasındaki tutunmaya odaklar.

## (a) EFOR İŞARETİ Tablosu

| Beden İşareti | İngilizce Tam Kalıp | Uyma Oranı | Okunabildiği Ölçek | Model | Etiket / Kaynak |
|---|---|---|---|---|---|
| Bacak Desteği (Kaymama) | "His boots are firmly planted, wide stance digging into the floor, absolute zero foot sliding." | Düşük (%69 ihlal; sürtünme kaybı %31) | Geniş Plan | Sora 2, Gen-3, Kling, Veo 3.1 | ÖLÇÜLMÜŞ · "Friction (31% violation rate): Interactions between surfaces often lacked appropriate resistance, resulting in objects sliding unnaturally..." — https://arxiv.org/abs/2503.06800 |
| Duruş Bozulması (Denge) | "He struggles to maintain balance, center of gravity shifts drastically under the crushing load." | Çok Düşük | Orta / Geniş Plan | Tüm modeller | ÖLÇÜLMÜŞ · "floating, sliding, penetrating the ground, losing balance... VideoAlign assigns a high normalized z-score of 1.21" — https://arxiv.org/html/2605.14269v1 |
| Kavrayış Gevşemesi | "Thick pressurized gloves slowly slip from the heavy handles, fingers losing their grip." | Çok Düşük | Yakın Plan | Veo 3.1, Wan 2.1 | ÖLÇÜLMÜŞ · "Fine motor control: Hand movements, finger articulation, and small object manipulation remain challenging." — https://www.mindstudio.ai/blog/what-is-google-veo-3-1-flagship-video |
| Hız Düşüşü | "Movement halts abruptly mid-way due to extreme resistance, holds tension, then pulls again." | Orta (düz yavaşlama yazılırsa ağır çekim hatası) | Tümü | Veo 3.1, Luma Ray, Sora 2 | ÖLÇÜLMÜŞ · "the model prioritizes visual smoothness over physical accuracy... momentum doesn't always carry through" — https://www.mindstudio.ai/blog/... |
| Sırt Eğrisi | "His spine curves forward intensely, upper back heavily hunched under the extreme weight." | Yüksek | Orta Plan | Gemini Omni 1.1, Veo 3.1 | UYGULAMA |
| Omuz Düşüşü | "One shoulder drops significantly lower than the other due to the heavy mass." | Orta (simetri önyargısı düzeltmeye çalışır) | Orta Plan | Kling, Luma Ray | UYGULAMA |
| Nefes (Göğüs Hareketi) | "Heavy, rapid chest heaving visible through the thick pressure suit." | Orta | Orta Plan | Gemini Omni 1.1 | ÖNERİ |
| Titreme | "High-frequency subtle shaking in his arms and legs from severe muscle exhaustion." | Çok Düşük (denoise bunu blur olarak yok eder) | Yakın / Orta Plan | Wan 2.1, Luma Ray | ÖNERİ |

## (b) BİRİKEN BEDEL Tablosu

| Durum | Klipler Arası Taşıma Yöntemi | Tutuş | Kopma Noktası | Model | Etiket / Kaynak |
|---|---|---|---|---|---|
| Yorgunluk Seviyesi (soyut) | Metin merdiveni ("wear state three of four") | Çok Düşük | Özellik bağlama ve sayısal algı eksikliği | CogVideoX-5B, Wan 2.1 | ÖLÇÜLMÜŞ · "degradation across attribute binding, spatial relationships, and generative numeracy" — https://arxiv.org/html/2608.12426 |
| Duruşun Gevşemesi (dinamik) | İlk Kare (I2V) + metin promptu | Düşük / Orta | Karakter ilk saniyede dikleşip taze animasyona geçebilir | Wan 2.1, Kling | ÖLÇÜLMÜŞ · "The original model retains over-mixing hotspots... fragmented transport" — https://arxiv.org/abs/2609.08505 |
| Statik Kir / Hasar | İlk Kare (I2V referansı) | Yüksek | Kameranın fazla dönmesi doku kaybına yol açar | Veo 3.1, Sora 2 | ÖLÇÜLMÜŞ · "maintain character consistency across different scenes. Preserve background and environmental elements." — https://aitoolsreview.co.uk/tool/veo-3 |
| Nefes Nefese Kalma | Klip başı sürekli metin promptu | Düşük | İlk kareden aktarılamaz; model anlık sıfırlanma yaşar | Gemini Omni 1.1, Veo 3.1 | UYGULAMA |

## (c) TEMASSIZ HAREKET Tablosu

| Arıza Türü | Tetikleyici İfade | Önleyen İngilizce Kalıp | Model | Etiket / Kaynak |
|---|---|---|---|---|
| İtmesiz Dönme | "Turns around in mid-air", "zero-gravity" | "He pushes hard against the airlock wall with his left hand to spin his body around." | Veo 3.1, Sora 2 | ÖLÇÜLMÜŞ · "Conservation of Momentum (39% violation rate): Objects often moved in ways that defied momentum principles..." — https://arxiv.org/abs/2503.06800 |
| Kayan Ayak | Efor gerektiren itme/çekme, "floating" | "Boots remain completely static on the floor grating, providing a solid anchor point." | Tüm Modeller | ÖLÇÜLMÜŞ · "Friction (31% violation rate)... resulting in objects sliding unnaturally..." — https://arxiv.org/abs/2503.06800 |
| Havada Yürüme | "Microgravity", "floating in space" | "His legs stay locked together, torso stiff, only pulling with his arms." | Sora 2, Runway Gen-4.5 | UYGULAMA |
| Boşluğu Kavrama | "Reaches out to grab the floating tool" | "He anchors his boots into the deck before extending his arm to grab the tool." | Kling, Luma | ÖNERİ |

## Doğrulanabilir Bulgular

1. Physion-Eval: fizik kritik senaryolarda dış merkezli videoların %83.3'ü, iç merkezli videoların %93.5'i insan tarafından fark edilebilir fizik hatası içerir — https://arxiv.org/abs/2603.19607
2. VideoPhy-2: momentum korunumu %39, esneklik %37, sürtünme %31, yerçekimi %29 ihlal; en iyi model zorlu alt kümede %22 — https://arxiv.org/abs/2503.06800
3. T2V-CompBench: "wear state three of four" gibi sayısal durum ifadeleri anlamlandırılamıyor — https://arxiv.org/html/2608.12426
4. PhyMotion / ImDy: 2B pürüzsüzlük metrikleri kinematik tutarsızlıkları yakalayamaz — https://arxiv.org/html/2605.14269v1
5. Yapay Ağır Çekim Arızası: "yavaş hareket" istemi sahnedeki tüm zamanı büker — https://www.mindstudio.ai/blog/what-is-google-veo-3-1-flagship-video
6. Temporal State Transport kırılımı: 10 saniyede dikkat dengesizleşir, yorgunluk silinir, model "dinlenmiş insan" önyargısına döner — https://arxiv.org/abs/2609.08505

## Kaynaksız İddialar (Hipotezler)

- Modeller "ağır" kelimesini kas gerilimiyle değil nesnenin piksel boyutuyla eşleştirir. (Kapalı kaynak mimariler ölçülemiyor.)
- "Heaving chest" opak vizörlü giyside eforu göstermenin tek güvenilir yoludur. (İzole akademik veri seti yok.)
- Temassız hareket ile efor arızaları aynı düğümlerdeki tork/momentum eksikliğinden gelir. (Mekanistik yorumlanabilirlik henüz yok.)
- 11 negatif cümle dikkat kapasitesini tüketip pozitif efor işaretlerini silikleştirir. (İzole test yok.)
- Titreme difüzyonda imkânsızdır çünkü denoise onu blur olarak düzleştirir. (Ayırt eden ölçüt yayımlanmamış.)
