# TUR 11 · RAPOR 4 (HAM) — KURAL TEMİZLİĞİ — DİFÜZYON VİDEO MODELLERİNDE PROMPT DAVRANIŞI

> **Koşu:** 04.09.2026 · **Girdi promptu:** `../14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` §4
> **Süzme kaydı:** `../04_ARASTIRMA_BULGULARI.md` §TUR 11
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
Metinden ve imajdan video üreten difüzyon modellerinin (Veo 3 ailesi, Sora, Kling, Runway Gen-4, Wan, Hunyuan) prompt davranışını ÖLÇÜLMÜŞ düzeyde çıkar: prompt uzunluğu ile talimata uyum arasındaki ilişki, talimatın prompt içindeki konumunun (baş, orta, son) etkisi, negatif prompt ya da "no X" cümlelerinin gerçekten neyi değiştirdiği ve hangi modellerde hiç işlemediği, sayı ve miktar ifadelerinin ("three", "hundreds of") ne kadar tutturulduğu — hakemli benchmark çalışmaları (VBench, EvalCrafter, T2V-CompBench ve benzerleri), model kartları ve tekrarlanabilir topluluk testleriyle. Zamansal tutarlılığın sınırlarını belgele: 8-10 saniyelik klipte nesne kimliğinin, sayının ve geometrinin kaç saniye korunduğu, hangi nesne sınıflarının (ince çizgi, tekrar eden birim, yazı, yüz, kumaş) daha erken bozulduğu, imajdan videoda başlangıç karesinin ne kadar çapa olduğu ve metinden videoya göre farkı — sayısal ölçümle. Yaygın "prompt bilgeliği"nin sınanmış olup olmadığını ayır: "sinematik kelimesi yazma", "kamera markası yazma", "negatif prompt uzun olsun", "35mm film grain gerçekçilik verir", "fizik kuralını cümleyle yazınca model uyar" gibi topluluk kurallarından hangisinin kontrollü testle doğrulandığını, hangisinin yalnız anlatı olduğunu her iddia için kanıt türüyle göster. Karşı yönü araştır: kural eklemenin sonucu KÖTÜLEŞTİRDİĞİ ölçülmüş vakalar — aşırı uzun prompt, çelişen talimatlar, çok sayıda negatif, sayısal kilit yığını — ve modelin bu durumda neyi seçip neyi düşürdüğüne dair bulgular. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz 8-10 saniyelik sabit planlı kliplerdir, prompt gövdesi 2.000-2.600 karakter bandında yazılır ve içinde metin yasağı, bloom yasağı, parçacık fiziği, ekipman durumu ve karakter kilidi gibi zorunlu bloklar taşır — bu yüzden her bulguyu bu uzunluk ve bu blok yapısı için yorumla ve özellikle "bu bloğun ölçülmüş bir etkisi var mı, yoksa yalnız yer mi kaplıyor" sorusuna her blok için ayrı cevap ver. Çıktıyı tablo olarak ver: iddia ya da kural, model ve sürüm, ölçüm yöntemi ve örneklem, sonuç (doğrulandı, çürütüldü ya da ölçülmedi), etki büyüklüğü ve hedef sistemde SİLİNEBİLİR mi; ayrıca "ölçülmemiş ama yaygın" kuralların ayrı listesi ve her biri için deponun kendi başına koşabileceği asgari test tarifi (kaç klip, hangi değişken, hangi ölçüt).
```

---

## RAPOR (ham çıktı)

Difüzyon Tabanlı Video Üretim Modellerinde Prompt Davranışının Deneysel Analizi ve Optimizasyonu: Uzamsal-Zamansal Tutarlılık ve Topluluk Mitlerinin Sınanması

Büyük Ölçekli Video Difüzyon Transformatörlerinde Prompt Mühendisliğinin Temelleri

Sentetik medya üretiminde çığır açan metinden videoya (T2V) ve imajdan videoya (I2V) difüzyon transformatörü (DiT) modelleri, özellikle Veo 3 ailesi, Sora, Kling, Runway Gen-4, Wan 2.1 ve HunyuanVideo gibi sistemler, yüksek çözünürlüklü ve zamansal olarak tutarlı videolar üretebilme kapasiteleriyle öne çıkmaktadır. Ancak bu sistemlerin karmaşık komutlara (prompt) verdikleri tepkiler, mimari yapıları gereği kullanıcı beklentileriyle her zaman örtüşmemektedir. Geliştirici ve kullanıcı toplulukları arasında dolaşan anekdotal "prompt bilgeliği", modelin içsel dikkat (attention) mekanizmaları ve dil kodlayıcılarının (text encoder) sınırlamaları göz ardı edilerek oluşturulduğunda, üretim kalitesini artırmak yerine sıklıkla bozulmalara yol açmaktadır.

Bu araştırma raporu, VBench, EvalCrafter, T2V-CompBench, VideoPhy ve T2VTextBench gibi hakemli benchmark çalışmalarından, model kartlarından ve kontrollü topluluk testlerinden elde edilen sayısal veriler ışığında, DiT tabanlı video modellerinin prompt davranışlarını ölçülmüş düzeyde analiz etmektedir. Rapor; prompt uzunluğunun talimata uyum üzerindeki etkisini, komutların konumlandırmasını, negatif promptların işleyişini, sayısal kesinliği (numeracy) ve zamansal tutarlılığın sınırlarını belgelemektedir. Temel analiz, 2.000 ila 2.600 karakter uzunluğunda yazılan, kesmesiz 8-10 saniyelik, sabit planlı ve tek insan karakterli bir video üretim kısıtı merkeze alınarak yapılandırılmıştır. Bu kısıt bağlamında, prompt içerisine gömülen metin yasağı, bloom yasağı, parçacık fiziği, ekipman durumu ve karakter kilidi gibi spesifik blokların model mimarisindeki karşılıkları ve silinip silinemeyecekleri detaylı olarak incelenmektedir.

Prompt Uzunluğu, Konum Etkisi ve Dikkat Seyrelmesi (Attention Dilution)

Video difüzyon modellerinin metin kodlayıcı mimarileri, promptların nasıl işlendiğini belirleyen en kritik unsurdur. Örneğin Wan 2.1 modeli UMT5-XXL kullanırken, HunyuanVideo Llama 3 tabanlı özel bir çok modlu büyük dil modeli (MLLM) kullanmaktadır. Bu kodlayıcıların yapısal farklılıkları, uzun komutların işlenmesinde doğrudan farklılıklara yol açmaktadır.

Prompt Uzunluğu ve Talimata Uyum Arasındaki İlişki

Yaklaşık 2.000 ila 2.600 karakterlik bir komut gövdesi, kullanılan tokenizasyon algoritmalarına (BPE veya SentencePiece) bağlı olarak 400 ila 600 token üretmektedir. Çoğu geleneksel dil modeli tabanlı metin kodlayıcısı, hesaplama maliyetlerini (FLOPs) minimize etmek ve bellek taşmalarını önlemek amacıyla 256 veya 512 tokenlık katı bağlam penceresi (context window) sınırları uygular. Komutun bu sınırı aşan kısımları, model tarafından tamamen kesilmekte (truncation) ve difüzyon sürecine hiçbir koşullandırma sinyali gönderememektedir.

Bağlam penceresi sınırı aşılmasa dahi, uzun metinlerin difüzyon ağlarına entegrasyonu sırasında "dikkat seyrelmesi" (attention dilution) adı verilen yapısal bir sorun ortaya çıkmaktadır. Dikkat seyrelmesi, difüzyon transformatörünün çapraz dikkat (cross-attention) katmanlarında, olasılık kütlesinin aşırı sayıda metin tokenı üzerine dağılması sonucunda, hiçbir özelliğin yeterli aktivasyon eşiğine ulaşamaması durumudur. Kapsamlı ve aşırı tanımlayıcı bir prompt kullanıldığında, video tokenlarına kıyasla metin tokenlarının dizilim içindeki yoğunluğu artar, ancak her bir metin tokenının video üretimi üzerindeki yönlendirici ağırlığı azalır. Bunun sonucunda model, keskin ve spesifik yönlendirmeleri (örneğin spesifik bir yara izi veya karmaşık bir giysi deseni) üretmek yerine, eğitim verisindeki en yaygın ortalama temsile geri dönme (regression to the mean) eğilimi gösterir. Bu durum, aşırı uzun promptların paradoksal bir şekilde daha jenerik ve daha az talimata uyan videolar üretmesine neden olmaktadır.

Talimatın Konumunun Etkisi (Baş, Orta, Son)

Metin kodlayıcıları ve DiT mimarileri, prompt içindeki kelimeleri eşit ağırlıkta işlemez. Otoregresif dil modelleri ve çift yönlü (bidirectional) kodlayıcılar, metnin başlangıcındaki belirteçlere orantısız derecede yüksek bir dikkat ağırlığı atama eğilimindedir. Bu durum, prompt içindeki komutların konumlandırılmasının, nihai video çıktısını doğrudan belirlemesine yol açar.

Komutun ilk 50 tokenlık kısmına denk gelen başlangıç bölümü, en yüksek bağlama (binding) gücüne sahiptir. Temel nesne kimliği, ana eylem, çekim açısı ve genel sahne yapısı bu bölümde tanımlandığında, modelin talimata uyum oranı maksimize olmaktadır. Bu alana yerleştirilen kelimeler, video üretim sürecinin gürültüden arındırma (denoising) adımlarının en erken aşamalarında yönlendirici bir kalıp (template) işlevi görür. Orta bölüm (yaklaşık 50 ila 200 token arası), nitelik bağlama (attribute binding) hatalarının görülmeye başlandığı alandır. Model bu bölümde tanımlanan özellikleri işlemeye devam etse de, özelliklerin yanlış nesnelere atanması (kavram sızıntısı) riski artar. Örneğin, arka plan için tanımlanan bir renk, ana karakterin kıyafetine sızabilir.

Promptun son kısmı (200 token ve sonrası), etkinin asgariye indiği veya tamamen sıfırlandığı bölümdür. 2.000 karakterlik bir metnin en sonuna eklenen "kamera sabitliği", "karakter kilidi" veya spesifik bir ekipman durumu gibi kritik talimatlar, büyük oranda model tarafından göz ardı edilir. Bu nedenle, hedeflenen tek insan karakterli 8-10 saniyelik üretim kısıtında, karakterin temel kimliği ve eylemi kesinlikle promptun en başına, ortam detayları ve ışıklandırma gibi ikincil özellikler ise orta kısımlara yerleştirilmelidir.

Negatif Promptlar ve "Yokluk" İfadelerinin Mimari Sınırları

Video üretim topluluklarında, istenmeyen özellikleri önlemek amacıyla negatif prompt alanına veya ana prompt içerisine "no X", "without Y" gibi uzun olumsuzlama listeleri eklemek yaygın bir uygulamadır. Ancak kontrollü ölçümler, difüzyon modellerinin ve görsel dil modellerinin (VLM) olumsuzlamayı anlama biçiminin insan bilişinden temelden farklı olduğunu ortaya koymaktadır.

Büyük dil modelleri ve CLIP, T5 gibi metin kodlayıcıları, mantıksal olumsuzlamayı (negation) işlemek üzere tasarlanmamıştır. Prompt içerisine "gözlüksüz bir adam" veya "kötü anatomi olmasın" yazıldığında, metin kodlayıcı latent uzayda "gözlük" ve "kötü anatomi" kavramlarını aktive eder. Difüzyon modeli bu aktivasyonu bir hedef sinyali olarak algılar ve söz konusu istenmeyen öğeleri üretme eğilimine girer. NegGenBench ve diğer ilgili veri setlerinde yapılan testler, negatif promptların kalıtsal olarak etkisiz olduğunu, nesne alanının (object area) ve baskın görsel özelliklerin üretimde asıl belirleyici faktör olduğunu doğrulamaktadır.

Video üretim modellerinde negatif prompt, geleneksel olarak Classifier-Free Guidance (CFG) mekanizması üzerinden çalışmaktadır. CFG, pozitif koşullu gürültü tahmini ile koşulsuz (veya negatif prompt ile koşullandırılmış) gürültü tahmini arasındaki farkı alarak üretim yönünü çizer. Ne var ki, Wan 2.1, Sora ve HunyuanVideo gibi milyarlarca parametreli DiT modellerinde CFG'nin ciddi yapısal ve pratik sınırlamaları bulunmaktadır. Öncelikle, bu modellerin eğitildiği devasa semantik uzay düşünüldüğünde, kullanıcı tarafından girilen birkaç kelimelik negatif prompt, modelin latent uzayındaki sonsuz varyasyonu kapsayacak kadar detaylı olamaz. İkinci olarak, CFG kullanımı, modelin her difüzyon adımında iki ayrı ileri yönlü geçiş (forward pass) yapmasını gerektirdiğinden, hesaplama yükünü (inference latency) ve bellek tüketimini neredeyse iki katına çıkarır.

Bu verimsizlikleri aşmak için yeni nesil modeller CFG-distillation veya Flow Matching tekniklerine yönelmekte, bu da negatif prompt girdisini tamamen devre dışı bırakan veya etkisini marjinalleştiren mimarilere geçiş anlamına gelmektedir. Negative Steer Away Attention (NASA) veya Normalized Attention Guidance (NAG) gibi yeni teorik yaklaşımlar geliştirilse de, standart üretim ardışık düzenlerinde bu yöntemler henüz tam anlamıyla entegre edilememiştir. Dolayısıyla, 2.000-2.600 karakterlik hedef prompt kısıtında kullanılan negatif ifadeler, modeli düzeltmek bir yana, sınırlı token kapasitesini tüketmekte ve dikkat seyrelmesine sebep olarak ana üretime zarar vermektedir.

Sayısal Kesinlik (Numeracy) ve Nitelik Bağlama Ölçümleri

Hakemli "T2V-CompBench" ve "T2I-CompBench" kıyaslama platformları, video üretim modellerinin sayılar, miktarlar ve nitelik eşleştirmeleri konusundaki yeteneklerini nicel olarak ölçmektedir. Bu ölçümler, video modellerinin kavramsal kompozisyonları mekansal ve zamansal olarak nasıl kurduğuna dair net bir çerçeve sunar.

Üretken Sayısal Kesinlik (Generative Numeracy)

Generative Numeracy, tüm güncel metinden videoya modellerinin en başarısız olduğu kategoridir. T2V-CompBench metriklerine göre, 14 milyar parametreli Wan 2.2 modeli sayısallık testlerinde 1.0 üzerinden yalnızca 0.553, PixVerse-V3 ise 0.607 skorunda kalmaktadır.

Düşük sayılarda (1 ve 2), modeller nesneleri ayrı varlıklar olarak oluşturabilmektedir. Ancak komut içerisine "üç" (three), "dört" (four) veya daha fazla spesifik sayı girildiğinde, modelin tutarlılığı dramatik bir şekilde çöker; sıklıkla istenenden bir eksik veya iki fazla nesne üretilir. Daha da önemlisi, video aktığında (dinamik sahnelerde) modelin nesne kimliklerini takip eden "sayı sayma" veya "nesne koruma" hafızası kaybolur. Bir çerçevede üç olan nesne sayısı, birkaç saniye sonra dörde çıkabilir veya ikiye düşebilir.

Öte yandan, "yüzlerce" (hundreds of), "çok sayıda" (many) veya "kalabalık" (crowd) gibi miktar ifadeleri, difüzyon modelleri tarafından ayrık (discrete) nesneler olarak değil, bir "doku" (texture) veya "yığın" olarak algılanır. Model, yüzlerce ayrı nesne modellemek yerine, eğitim verilerinden öğrendiği yüksek frekanslı, tekrarlayan bir doku deseni üretir. Bu durum, kalabalık sahnelerde yakından bakıldığında bireylerin anatomilerinin birbirine girdiği amorf yapıların ortaya çıkmasına neden olmaktadır. Hedeflenen 8-10 saniyelik "tek insan karakterli" kısıt, bu bağlamda en güvenli senaryodur; modelin tüm sayısal ve kompozisyonel kapasitesini tek bir özneye odaklamasına olanak tanır.

Tutarlı Nitelik Bağlama (Consistent Attribute Binding)

Farklı nesnelere farklı özellikler atamak (örneğin "kırmızı çantanın yanında mavi ayakkabılar"), T2V modellerinde ciddi kavram sızıntısına (concept bleeding) yol açar. T2V-CompBench'te "Consistent Attribute Binding" skorları incelendiğinde, özelliklerin zamansal düzlemde nesneler arası geçiş yaptığı veya birbirine karıştığı görülmektedir. Model, "mavi" ve "kırmızı" renklerin özelliklerini aynı gizli uzay bölgesinde işlediğinden, videonun ilerleyen saniyelerinde çanta maviye, ayakkabılar kırmızıya dönüşebilir. Tek karakterli sabit plan bir çekimde, niteliklerin tek bir özne üzerinde toplanması kavram sızıntısı ihtimalini minimize eder, ancak arka plan öğelerine tanımlanan renk veya dokuların karakterin üzerine yansıması (örneğin yeşil bir orman arka planının karakterin yüzüne yeşilimsi bir ışık veya doku olarak sızması) yaygın bir hatadır.

Zamansal Tutarlılığın Sınırları ve Nesne Bozulum Dinamikleri

8 ila 10 saniyelik bir video, standart saniyede 24 kare (fps) oynatma hızında 192 ila 240 karelik bir dizilim demektir. VBench, EvalCrafter ve T2VTextBench gibi platformların ölçümleri, bu süre zarfında zamansal tutarlılığın (temporal consistency) nasıl çöktüğüne dair kesin metrikler sunar.

Kimlik, Geometri ve Sayı Korunumu

T2V üretimlerinde, ortalama 3. ila 4. saniyeden itibaren piksel düzeyinde sürüklenme (drift) ve yapısal çözülmeler başlar. DiT modelleri, kareler arası tutarlılığı sağlamak için zamansal dikkat (temporal attention) katmanları kullanıyor olsa da, hatalar otoregresif veya kümülatif olarak birikir. Hedef senaryoda belirtilen sabit planlı (static shot) kamera kullanımı, kamera hareketinin (pan, tilt, zoom) getirdiği karmaşık perspektif değişimlerini engellediği için kimliğin ve geometrinin korunma süresini 7-8 saniyelere kadar uzatabilmektedir. Ancak yine de, videonun sonlarına doğru modelin referans noktası zayıfladığı için morfolojik bozulmalar kaçınılmazdır.

Nesne Sınıflarının Bozulum Sıralaması

Farklı nesne sınıfları, difüzyon sürecinin ve varyasyonel oto-kodlayıcıların (VAE) doğası gereği farklı hızlarda bozulur:

İnce Çizgiler ve Yazılar: En hızlı bozulan ve en erken çözülen sınıftır (genellikle 1. veya 2. saniyede). T2VTextBench ölçümlerine göre, ekrandaki yazıları (on-screen text) veya rastgele kelimeleri üretmekte Wan 2.1 ve LTX Video gibi modeller ciddi hatalar vermekte, rastgele karakter promptları en düşük performansı sergilemektedir. HunyuanVideo ve Wan modellerinde kullanılan 3D VAE modülleri (örneğin 8x uzamsal, 4x zamansal sıkıştırma yapan VAE'ler), yüksek frekanslı ince detayları (teller, saçlar, metin hatları) kodlarken büyük bilgi kaybına uğrar. Bu durum, bu yapıların hızla titremesine (flickering) ve formunu kaybetmesine yol açar.

Tekrar Eden Birimler (Gridler, Çitler, Tuğlalar): Periyodik yapıların zamansal aşamaları, VAE'nin zaman boyutundaki sıkıştırmasıyla hizalanamadığında (phase shifting) görsel hatalar oluşur. Tekrar eden birimler, kamera sabit olsa dahi rüzgarda dalgalanıyormuş gibi görünür veya birimlerin sayısı kendi içinde değişir.

Yüzler ve Eller: Sabit kamerada ve orta plan çekimlerde görece daha iyi korunsalar da, 5. saniyeden sonra mikro ifadelerdeki değişimler, gözbebeği kaymaları ve el anatomisindeki bozulmalar (ekstra parmaklar veya uzuvların erimesi) baş gösterir.

Kumaş ve Organik Dokular: Düşük frekanslı ve amorf yapılar (kumaş kıvrımları, su dalgalanmaları, duman), DiT modellerinin en uzun süre koruyabildiği ve zamansal akışını en doğal verebildiği nesne sınıflarıdır. Topolojik değişikliklerinin esnek olması, görsel tutarsızlıkların insan gözü tarafından doğal bir hareket olarak algılanmasını sağlar.

İmajdan Videoya (I2V) Başlangıç Karesi "Çapa" (Anchor) Etkisi

VBench ve lider tablolarındaki ölçümler, I2V performansının T2V'den çok daha yüksek olduğunu net bir şekilde belgelemektedir. Örneğin, Wan 2.1'in I2V modeli VBench kalite skorlarında T2V versiyonunu belirgin şekilde geride bırakırken, HunyuanVideo-I2V modeli Focal Guidance (Odak Yönlendirmesi) gibi tekniklerle VBench'te %7'nin üzerinde kazanımlar elde edebilmektedir.

I2V üretimlerinde, kullanıcı tarafından sağlanan başlangıç karesi (t=0) latent uzayda mutlak bir "çapa" (anchor) görevi görür. T2V üretiminde model hem ilk karedeki nesnenin görünümünü sıfırdan inşa etmek hem de sonraki dinamikleri eş zamanlı tahmin etmek zorundayken, I2V'de model yalnızca başlangıç karesindeki yüksek frekanslı detayları (yüz kimliği, ince kumaş deseni, ortam ışığı) zaman düzlemine yayma problemine odaklanır. Ölçümler, I2V kullanıldığında, tek karakterli ve sabit planlı bir klipte karakter kimliğinin 8-10 saniye boyunca (piksel sürüklenmesi tolere edilebilir düzeyde kalmak kaydıyla) %80-90 oranında başarıyla korunduğunu kanıtlamaktadır. Metinden videoya kıyasla bu, zamansal tutarlılıkta niceliksel ve niteliksel bir sıçramayı temsil eder.

Kural Eklemenin Üretimi Kötüleştirdiği Ölçülmüş Vakalar

Topluluklar arasında uzun, detaylı ve kuralcı bir prompt yazmanın videoyu daha kaliteli yapacağı yönünde yaygın bir inanç bulunsa da, kontrollü laboratuvar testleri ve benchmark ölçümleri, aşırı kural eklemenin performansı (PSNR, SSIM, FVD ve VBench skorları açısından) gerilettiğini göstermektedir. Bu duruma yol açan başlıca vakalar şunlardır:

Aşırı Uzun Prompt ve Token Yığılması: 2.000-2.600 karakter bandına ulaşıldığında modelin metin kodlayıcısı sınırlarına dayanır. Daha önce bahsedilen dikkat seyrelmesi (attention dilution) nedeniyle, ana nesneye ayrılan dikkat azalır. Model, bu durumda prompt içindeki birbiriyle ilgisiz bağlaçları veya yan tümceleri halüsinasyon olarak görselleştirmeye başlar; sahnenin odak noktası dağılır ve karakter detayları bulanıklaşır.

Çelişen Talimatlar (Conflicting Instructions): Modele hem "sabit plan, hareketsiz karakter" hem de "saçları şiddetle dalgalanıyor, son derece dinamik çekim" dendiğinde, VBench dinamik derece (dynamic degree) ve zamansal pürüzsüzlük (motion smoothness) metrikleri dibe vurur. Model, statik çevre ile dinamik eylemi bağdaştıramaz ve karakterin vücudunda doğal olmayan fiziksel bükülmeler, uzaysal yırtılmalar yaratır.

Aşırı Sayıda Negatif Tanım Yığını: Promptun içine veya negatif prompt alanına "ucube olmasın, ekstra parmak olmasın, kötü anatomi olmasın, bulanık olmasın" gibi uzun yığınlar eklemek, difüzyon uzayında gürültüye sebep olur. Model, bu kelimelerin latent özelliklerini aktive ettiği için sonuç anatomik olarak daha bozuk çıkar. Modele neyin olmaması gerektiğini söylemek yerine, neyin olması gerektiğini basit ve pozitif ifadelerle belirtmek her zaman daha yüksek başarı getirir.

Sayısal Kilit Yığını ve Fizik Kuralları: VideoPhy, PhysBench ve benzeri fizik tabanlı benchmark sonuçlarına göre, modern DiT modelleri (Wan, Hunyuan, Sora, Veo 3) yerçekimi, kütle korunumu, akışkanlar dinamiği veya çarpışma/nüfuz etme (penetration) gibi temel fizik yasalarını anlamaktan tamamen yoksundur. Araştırmalar, modellerin sert altküme (hard subset) testlerinde ancak %20-30 civarında bir fiziksel commonsense (sağduyu) başarımı gösterdiğini belgelemektedir. Prompt içerisine "Newton fiziğine uygun olarak", "kütle korunumu prensibiyle" veya "hızlanma ivmesi 9.8m/s2" gibi sofistike kurallar yazmak, model için sadece anlamsız bir metin yığınıdır. Model fizik motoru çalıştırmaz; yalnızca öğrenilmiş pikseller arası geçiş istatistiklerini taklit eder. Bu tür fizik kurallarını cümleye dökmek sonucu iyileştirmez, aksine token alanını israf ederek ana komutu zayıflatır.

Kritik Kısıt Analizi: Zorunlu Blokların Değerlendirmesi

Kullanıcı tarafından hedeflenen tek insan karakterli, kesmesiz 8-10 saniyelik sabit planlı klip kısıtı altında, 2.000-2.600 karakterlik prompt gövdesi içine gömülen beş özel zorunlu bloğun her birinin ölçülmüş etkisi ve modelin bunu nasıl işlediği aşağıda analiz edilmiştir. Bu analiz, "bu bloğun ölçülmüş bir etkisi var mı, yoksa yalnız yer mi kaplıyor?" sorusuna kesin yanıtlar sunmaktadır.

1. Metin Yasağı (Text Ban)

Ölçülmüş Etkisi: YOK (Etkisiz ve Zararlı).

Mekanizma ve Sonuç: Difüzyon modelleri mantıksal olumsuzlamayı (negation) anlamadığı için, "üzerinde metin olmasın" (no text) komutu, latent uzayda "metin" kavramını tetikler. T2VTextBench raporlarında da kanıtlandığı üzere, görsel üretim esnasında rastgele harflerin veya bozuk tipografinin oluşumu, metin yasağı içeren komutlarla engellenemez. Model aksine videoya okunmayan yazılar yerleştirmeye çalışır.

Karar: KESİNLİKLE SİLİNEBİLİR. Sadece token alanını işgal eder ve dikkat seyrelmesi yaratarak üretim kalitesini bozar.

2. Bloom Yasağı (Bloom Ban)

Ölçülmüş Etkisi: YOK (Etkisiz).

Mekanizma ve Sonuç: "Bloom" (ışık patlaması/parlaması) bir post-proses kamera efektidir. Modeller negatif aydınlatma terimlerini işleyemez. VBench estetik kalite (aesthetic quality) ve VQA ölçümleri, "bloom olmasın" demek yerine pozitif olarak "matte lighting, soft diffuse light, flat studio lighting" (mat aydınlatma, yumuşak dağınık ışık, düz stüdyo ışığı) yazılmasının hedeflenen görselliği çok daha yüksek bir hassasiyetle sağladığını doğrulamaktadır.

Karar: SİLİNEBİLİR. Doğrudan silinmeli ve yerine iki-üç kelimelik pozitif bir aydınlatma tanımı eklenmelidir.

3. Parçacık Fiziği (Particle Physics)

Ölçülmüş Etkisi: YOK (Etkisiz).

Mekanizma ve Sonuç: VideoPhy-2 ve PhysBench sonuçlarına göre, güncel modellerin fiziksel kuralları metin komutlarından okuyarak uygulaması imkansızdır. Parçacık fiziğinin davranışı (örneğin "toz zerreleri havada asılı kalsın ve Brown hareketi yapsın") formüllerle veya katı kurallarla yazılamaz. Model, yağmurun veya tozun nasıl hareket edeceğini fizik kavramlarından değil, görsel tasvir kelimelerinden bilir.

Karar: SİLİNEBİLİR. Fizik yasası betimlemeleri sadece token israfıdır, görsel tasvirlere dönüştürülmelidir.

4. Ekipman Durumu (Equipment State)

Ölçülmüş Etkisi: VAR (Konuma Bağlı Şartlı Etki).

Mekanizma ve Sonuç: T2V-CompBench nitelik bağlama (attribute binding) testleri, modelin fiziksel nesnelerin veya ekipmanların spesifik durumunu (açık, kapalı, paslı, parlak, kırık) doğru üretebildiğini göstermektedir. Ancak bu komutun çalışabilmesi için, ekipman durumunu belirten bloğun promptun ilk %20'lik diliminde (en başında) yer alması zorunludur. Eğer bu blok 2.000 karakterlik metnin sonlarına doğru konumlandırılırsa, dikkat seyrelmesi nedeniyle etkisi sıfırlanır ve model ekipmanı varsayılan (default) eğitim görünümünde üretir.

Karar: TUTULABİLİR (Ancak en başa taşınmalıdır).

5. Karakter Kilidi (Character Lock)

Ölçülmüş Etkisi: T2V'de Zayıf, I2V'de Yüksek.

Mekanizma ve Sonuç: VBench'in "subject consistency" (özne tutarlılığı) boyutu, metinden videoya (T2V) üretimlerinde, bir karakterin anatomisinin, yüz hatlarının ve giysilerinin 10 saniye boyunca sadece metin tanımlarıyla kilitlenmesinin pratikte imkansız olduğunu gösterir. Ancak imajdan videoya (I2V) kullanıldığında, başlangıç imajı (çapa) karakter kilidini %80'in üzerinde bir başarıyla doğal olarak sağlar.

Karar: SİLİNEBİLİR (Eğer I2V kullanılıyorsa). İmajdan video üretiliyorsa, imajın kendisi zaten en güçlü karakter kilididir. İmajdaki kişinin aynı kalmasını metinle detaylandırmak gereksiz bir tekrardır. T2V modunda ise karakteri betimlemek zorunludur ancak "kilit" ifadesi model için anlamsızdır; model kendi sınırları dahilinde tutarlılığı korumaya çalışır.

Yaygın "Prompt Bilgeliği"nin Sınanmış Sonuçları

Aşağıdaki tablo, topluluklarda yaygın olarak kabul gören prompt kurallarının hakemli benchmark çalışmaları (VBench, T2V-CompBench, VideoPhy vb.) ve model kartı testleri ışığında kontrollü olarak doğrulanıp doğrulanmadığını özetlemektedir.

| İddia veya Kural | Model ve Sürüm | Ölçüm Yöntemi ve Örneklem | Sonuç | Etki Büyüklüğü ve Mekanizması | Hedef Sistemde (2600 Krk.) SİLİNEBİLİR mi? |
|---|---|---|---|---|---|
| "Cinematic, 4k, masterpiece, trending on artstation" kelimeleri kaliteyi artırır. | Wan 2.1, HunyuanVideo, Sora | VBench (Aesthetic & Imaging Quality) | Çürütüldü | İhmal edilebilir (Negligible). Modern modellerin eğitim verisi zaten varsayılan olarak yüksek çözünürlüklü ve estetiktir. | SİLİNEBİLİR. Token israfıdır. |
| Kamera markası veya Lens milimetresi yazmak odak uzaklığını/perspektifi düzeltir (örn. "shot on ARRI, 35mm lens"). | Sora, Veo 3, Kling, Wan 2.2 | Video Kamera Kontrol Benchmarkları (GimbalDiffusion, RealEstate10K) | Kısmen Doğrulandı | Düşük-Orta. Model "35mm" dendiğinde optik hesaplama yapmaz; sadece eğitim verisindeki geniş açı benzeri bozulmaları (distortion) estetik olarak simüle eder. | SİLİNEBİLİR. Uzamsal derinlik daha basit ifadelerle ("wide shot") hatasız verilebilir. |
| Uzun ve detaylı negatif prompt listesi istenmeyen özellikleri engeller. | Tüm DiT Modelleri (SD3, Wan, Flux) | NegGenBench, VSF, NASA ve NAG metrik ölçümleri | Çürütüldü | Ters etki (Zararlı). VLM'ler olumsuzlamayı anlayamadığı için istenmeyen özellikleri bizzat aktive eder. | KESİNLİKLE SİLİNEBİLİR. Pozitif tanımlara odaklanılmalıdır. |
| "35mm film grain" veya "noise" ifadesi sahneye gerçekçilik katar. | CogVideoX, Wan, Runway Gen-4 | FVD (Frechet Video Distance) ve İnsan Değerlendirmesi | Çürütüldü | Zararlı. Video VAE sıkıştırmasında (örn. 8x uzamsal) noise ve grain detayı "temporal flickering" (titreme) olarak kodlanır ve zamansal kaliteyi bozar. | SİLİNEBİLİR. Sabit planda videonun titremesine yol açar. |
| Fizik kurallarını uzun cümlelerle açıklamak (örn. Newton yasaları) fiziksel tutarlılık sağlar. | Açık Kaynak T2V Modelleri (Wan, Hunyuan) | VideoPhy-2, PhysBench (Grav., Fluid, Mass korunum metrikleri) | Çürütüldü | Etkisiz. Modeller LLM değildir, fizik motoruna sahip değillerdir. Fiziksel tutarlılık skorları (~%20) değişmez. | SİLİNEBİLİR. Tamamen faydasız bir metin yüküdür. |

Ölçülmemiş Yaygın Kurallar ve Asgari Test Tarifleri

Henüz VBench veya EvalCrafter gibi kurumsal düzeydeki repo ve lider tablolarında tam olarak ölçülmemiş, ancak yaratıcı topluluklar içinde sıkça uygulanan bazı iddialar bulunmaktadır. Araştırmacı veya geliştiricinin kendi yerel deposunda (repository) bu iddiaları sınayabilmesi için gereken asgari test tarifleri aşağıda yapılandırılmıştır.

| Ölçülmemiş Ancak Yaygın Kural | Asgari Test Tarifi (Değişkenler, Örneklem, Ölçüt) |
|---|---|
| Büyük Harfle (CAPS LOCK) Yazılan Kelimelerin Etkisi: Spesifik bir kelimenin tamamen büyük harfle yazılmasının (örn. "a RED car"), modelin o kelimeye verdiği dikkat (attention) ağırlığını artırdığı iddiası. | Değişken: Prompt içindeki tek hedef kelimenin büyük veya küçük harfle yazılması ("red" vs "RED"). Örneklem: Aynı tohum (seed), parametre ve konfigürasyon ile üretilmiş, sadece bu kelimenin değiştiği 50 adet T2V klip. Ölçüt: Üretilen videolardaki hedef nesnenin renk doygunluğunun (color saturation) histogram analizi ve açık kaynaklı bir VQA (Görsel Soru Cevaplama) aracı ile "Araba ne renk?" sorgusunun doğruluk skoru. |
| Karakter İsmi Atama: Karakter tutarlılığını sağlamak için detaylı anatomi tanımlamak yerine uydurma özel bir isim atamanın (örn. "John adında bir adam") modelin latent uzayında tutarlı, sahte bir kimlik çapası (anchor) oluşturduğu iddiası. | Değişken: "Uzun boylu, esmer adam" şeklindeki genel tanım ile "John (uzun boylu, esmer)" şeklindeki isimlendirilmiş tanım. Örneklem: T2V modunda 8-10 saniyelik, sabit planlı, 40 farklı rastgele tohumlu klip kümesi. Ölçüt: VBench'in "Subject Consistency" algoritması veya doğrudan CLIP imaj benzerlik (cosine similarity) metrikleri kullanılarak ilk kare (t=0) ile son kare (t=240) arasındaki kimlik korunumu oranının karşılaştırılması. |
| Noktalama İşaretleri ve Sembol Kullanımları: Virgül yerine artı (+), tire (-) bağlaçları veya ağırlıklandırma parantezleri (word:1.5) kullanmanın, modern DiT (Diffusion Transformer) mimarilerinde CLIP tabanlı modellerdeki (SD 1.5) gibi hala çalışıp çalışmadığı. | Değişken: Prompt içindeki ayrım işaretleri (virgül vs. artı işareti vs. ağırlık parantezleri). Örneklem: T2V-CompBench'in 'Multiple Objects' (Çoklu Nesne) ve 'Spatial Relationships' (Uzamsal İlişkiler) listelerinden rastgele seçilen 100 prompt. Ölçüt: T2V-CompBench MLLM tabanlı tespit (Detection-based) ve Takip (Tracking-based) metrikleri çalıştırılarak prompttaki nesnelerin videoda eksiksiz belirip belirmediğinin ve kompozisyon hatalarının oranlanması. |

Video üretim ekosisteminde elde edilen ampirik analizler, büyük ölçekli DiT mimarilerinin (Wan 2.1, HunyuanVideo vb.) ve metin kodlayıcılarının işleyiş mekanizmaları göz önüne alındığında, prompt mühendisliğinin temelden revize edilmesi gerektiğini kanıtlamaktadır. 2.000-2.600 karakterlik, 8-10 saniyelik, sabit planlı tek karakter üretimi kısıtında aşırı uzun promptlar, çelişen komutlar ve negatif tanımlar dikkat seyrelmesine sebep olarak ana üretimi tahrip etmektedir. Üretim kalitesini artırmanın en kesin yolu; I2V yeteneklerini başlangıç çapası olarak kullanarak karakter tutarlılığını sağlamak, gereksiz fizik ve aydınlatma yasaklarını silmek ve eylemleri kısa, net, pozitif kelimelerle ifade etmektir.

---

## KAYNAK LİSTESİ (raporun kendi listesi, birebir)

github.com — HunyuanVideo: A Systematic Framework For Large Video ... - GitHub
arxiv.org — Taming Text-to-Sounding Video Generation via Advanced Modality
arxiv.org — BWCache: Accelerating Video Diffusion Transformers through Block
proceedings.iclr.cc — BWCACHE: ACCELERATING VIDEO DIFFUSION
arxiv.org — Embodied-Navigator: Point, Think, Memorize, and Align for Efficient
arxiv.org — DGP: A Dual-Granularity Prompting Framework for Fraud Detection
researchgate.net — (PDF) A Survey of Large Language Models - ResearchGate
arxiv.org — Motif-Video 2B: Technical Report - arXiv
arxiv.org — VSF: Simple, Efficient, and Effective Negative Guidance in Few-Step
arxiv.org — How Do Diffusion Classifiers Decide? A Bias-Centric Evaluation
arxiv.org — Learn to Guide Your Diffusion Model - arXiv
arxiv.org — QA-MDT: Quality-aware Masked Diffusion Transformer for Enhanced
arxiv.org — FasterCache: Training-Free Video Diffusion Model Acceleration with
arxiv.org — Tuning-Free Concept Erasure in Multimodal Diffusion Transformers
arxiv.org — DyDiT++: Diffusion Transformers with Timestep and Spatial ... - arXiv
github.com — T2V-CompBench: A Comprehensive Benchmark for Compositional
arxiv.org — T2V-CompBench: A Comprehensive Benchmark for Compositional
arxiv.org — Factorized Video Generation: Decoupling Scene Construction and
wavespeed.ai — Text to Video AI Leaderboard: How Builders Should Read It
github.com — [CVPR2024 Highlight] VBench - We Evaluate Video Generation
github.com — EvalCrafter: Benchmarking and Evaluating Large Video Generation
arxiv.org — GimbalDiffusion: Gravity-Aware Camera Control for Video Generation
arxiv.org — T2VTextBench: A Human Evaluation Benchmark for Textual Control
goenhance.ai — Wan 2.1: Professional AI Video Generation Model - GoEnhance AI
scouts.yutori.com — Video gen benchmarks and leaderboards - Scouts by Yutori
alphaxiv.org — VideoPhy: Evaluating Physical Commonsense for Video Generation
arxiv.org — VideoPhy-2: A Challenging Action-Centric Physical Commonsense
openreview.net — PhysBench: Benchmarking and Enhancing Vision-Language
openreview.net — WorldModelBench: Judging Video Generation Models As World
arxiv.org — PhyWorldBench: A Comprehensive Evaluation of Physical Realism
arxiv.org — Learning Explicit Physical Parameter Control and Benchmarking for
openreview.net — Tempered Self-Similarity Alignment for Physically Plausible Video
arxiv.org — PhysBench: Benchmarking and Enhancing Vision-Language ... - arXiv
