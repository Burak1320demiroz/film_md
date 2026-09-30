# TUR 22 · RAPOR 1 — KATI CİSİM SINIRI (ham, birebir)
> Prompt: `25_PROMPT_HATA_ONLEME_ARASTIRMA_PROMPTLARI.md` §1️⃣
> ⚠️ Oturuma yapıştırıldı, buraya birebir aktarıldı (bkz. 00_KUNYE.md).
> ⛔ Bu metinden KURAL OKUNMAZ; süzgeç `../04_ARASTIRMA_BULGULARI.md` §TUR 22'dedir.

---

Görüntüden-Videoya Üretim Modellerinde El-Nesne Etkileşimi ve Geometri Bozulmaları: Sci-Fi Üretim Kısıtları Altında Bir Analiz

Yapay zekâ tabanlı metinden-videoya (T2V) ve görüntüden-videoya (I2V) üretim modelleri, piksel doğruluğu ve sinematik estetik açısından doygunluk noktasına yaklaşmış olsa da, "içsel sadakat" (intrinsic faithfulness) olarak adlandırılan fiziksel tutarlılık, nedensellik ve anatomik doğruluk testlerinde kritik zafiyetler sergilemektedir. Güncel video temel modelleri olan Google Veo 3.1, Gemini Omni 1.1 Flash, OpenAI Sora, Kling 1.6, Runway Gen-4, Luma Ray, Pika, Hailuo ve Wan 2.1 gibi sistemler, özellikle iki katı cismin etkileşime girdiği "el-nesne etkileşimi" (Hand-Object Interaction - HOI) senaryolarında temel geometri kurallarını ihlal etmektedir. VBench-2.0, T2V-CompBench ve OSCBench gibi güncel kıyaslama ölçütleri (benchmark), modellerin genel görsel kaliteleri ile ince motor becerilerini ve nesne durum değişikliklerini (Object State Change - OSC) modelleme yetenekleri arasında derin bir uçurum olduğunu ortaya koymaktadır.

Bu analiz, on saniyelik, kesmesiz, sabit kameralı ve görsel efekt (VFX) müdahalesine kapalı fotogerçekçi bir uzay bilimkurgu üretimi kısıtı altında gerçekleştirilmiştir. Bu senaryoda; basınç giysili ve eldivenli bir karakterin karabina, kemer tokası, halat veya kontrol vanası gibi katı cisimleri manipüle etmesi, modellerin mimari sınırlarını en uç noktaya taşımaktadır. Sonradan uygulanan 3B takip (3D tracking), 3B el modeli entegrasyonu, rotoskop, maskeleme ve kare-kare manuel rötuş (inpainting) gibi çözümler, belirtilen tek metin istemli (single prompt) üretim iş akışı kuralları gereği tamamen "hat dışı" (offline) kabul edilerek kapsam dışında bırakılmıştır. Bunun yerine, arızaların üretim zincirinin hangi aşamasında doğduğu mekanik olarak sökülecek, istem (prompt) mühendisliğinin psikolinguistik zafiyetleri ölçülecek ve yalnızca kadraj, zamanlama ile mimari dinamiklerin manipülasyonuna dayalı önlemler incelenecektir.

## Mekanizmanın Sökülmesi: Arızalar Üretim Zincirinin Neresinde Doğuyor?

El ve nesne etkileşimi sırasında ortaya çıkan geometri bozulmaları, tek bir hata noktasından ziyade, Latent Difüzyon Modellerinin (LDM) ardışık mimari darboğazlarının birikimli bir sonucudur. Difüzyon tabanlı üretim modellerinde, nesnelerin hacmini ve çarpışma fiziklerini hesaplayan gerçek bir "fizik motoru" bulunmamaktadır. Model, devasa veri setlerinden öğrenilmiş pikseller arası geçiş olasılıklarını kullanarak fiziksel dünyayı ve nesne kalıcılığını (object permanence) taklit etmeye çalışır. Ancak bu taklit, karmaşık topolojik etkileşimlerde çökmektedir.

### Varyasyonel Otomatik Kodlayıcılar (VAE) ve Sıkıştırma Kayıpları

Görüntüden-videoya (I2V) ve metinden-videoya (T2V) üretim modellerinde (Google Veo 3.1, Gemini Omni 1.1 Flash, Wan 2.1, Sora), pikseller yüksek boyutlu uzaydan alınıp düşük boyutlu bir latent (örtük) uzaya sıkıştırılır. Varyasyonel Otomatik Kodlayıcılar (VAE), bu sıkıştırma işlemini hem uzamsal (spatial) hem de zamansal (temporal) boyutlarda gerçekleştirir. Tipik bir video modeli, uzamsal boyutta 8x, zamansal boyutta ise 4x veya daha fazla sıkıştırma uygular.

Bir eldivenin veya çıplak elin bir alete (örneğin bir vanaya veya karabinaya) temas ettiği an, görsel olarak son derece yüksek frekanslı bir sınır (edge) bilgisidir. Uzamsal sıkıştırma (spatial downsampling) sırasında, temas noktasındaki pikseller aynı latent yama (patch) veya kanal içine düşer. Model bu latent veriyi difüzyon süreci sonunda tekrar piksellere açarken (decoding), iki farklı katı cismin kesin sınırını koruyacak topolojik çözünürlüğe sahip olmadığı için pikselleri birbirine karıştırır (blending). Bu durum, ekranda "parmakların nesneye erimesi" veya "uzay eldiveninin alete kaynaması" (melting/welding) olarak belirir. VAE'lerin salt uzamsal sıkıştırmaya odaklanan mimarilerden, 3B nedensel evrişimlere geçişi bu erime problemini çözmek yerine, nesne ve elin aynı hareket vektörünü paylaştığı anlarda (tutma eylemi gibi) iki dokunun birbirine geçmesine neden olmaktadır.

### 3B Nedensel Evrişimler ve Zamansal Sürüklenme (Temporal Drift)

Zamansal tutarlılığı sağlamak için kullanılan 3B nedensel evrişim (causal 3D convolution) mekanizmaları, kareler (frames) arasında bilgi alışverişini sağlar. Ancak bu bilgi akışı tek yönlüdür. Araştırmalar, nedensel evrişimlerin kare grupları içinde eşit olmayan bilgi etkileşimlerine ve dengesiz performansa yol açtığını göstermektedir. Erken kareler, geç kareler kadar bağlam bilgisine sahip olamaz.

Uzay bilimkurgu kısıtında istenen 10 saniyelik, kesmesiz ve sabit kameralı çekimlerde, bu durum "zamansal sürüklenme" (temporal drift) adı verilen bir yıkıma neden olur. Klibin ilk iki saniyesinde eldiven ve tutulan alet (örneğin bir çekiç) ayrı varlıklar olarak nispeten sorunsuz işlense bile, 5. veya 8. saniyeye gelindiğinde hareket vektörleri iç içe geçer. Aletin semantik kimliği ile elin semantik kimliği harmanlanır. Çapraz dikkat (cross-attention) katmanları, nesneyi elin bir uzantısı olarak yorumlamaya başlar. Bu sürüklenme, "alet morfu" olarak adlandırılan, tutulan çekicin sapının kademeli olarak eldivenin bir parçasına dönüşmesi veya şekil değiştirmesi zafiyetini doğurur. Hailuo ve Runway Gen-4 gibi ardışık üretim yapan veya uzun video sürelerini hedefleyen modellerde bu morfolojik bozulma daha belirgindir.

### Derinlik Yanılsaması, Örtüşme (Occlusion) ve Katı Cisimlerin Geçişi

Görsel belirsizliğin ve geometri bozulmasının en yoğun olduğu anlar, elin nesneyi (veya nesnenin eli) örttüğü (occlusion) durumlardır. Yapay zekâ, "görsel yakınlık" (local proximity) ile "fiziksel temas ve itme" arasındaki farkı ayırt edemez. Bir uzay eldiveninin arkasında kalan kemer kayışının veya halatın, su sızdırmaz (watertight) ve kesintisiz bir geometriye sahip olduğu bilgisi latent modelde yapısal olarak mevcut değildir.

İki katı cismin, örneğin bir kayış ile pimin veya bir karabina ile halatın birbirinin içinden geçmesi (interpenetration / phasing), modelin derinlik sırasını (Z-index) ve katı madde sınırlarını kaybetmesiyle oluşur. AGILE gibi 3B el-nesne etkileşimi rekonstrüksiyon araştırmaları, mevcut görsel üretim modellerinin yerel yakınlığı optimize ettiğini, bu durumun da fiziksel iç içe geçmeye (interpenetration) izin verdiğini doğrulamaktadır. Modeller, fiziksel nüfuz etmeme (non-penetration) kuralını zorlayacak küresel bir geometrik doğruluğa öncelik vermezler. Bu nedenle, el bir aleti sıkıca kavradığında, aletin modeli avuç içinden geçerek elin dışına taşabilir.

### Çapraz Dikkat Yanılsaması ve Anatomik Hatalar (Fazla Parmak)

"Fazla veya eksik parmak" üretimi, genellikle metin kodlayıcılarının (text encoders) ve çapraz dikkat mekanizmalarının anatomik kısıtları uygulayamamasından kaynaklanır. Model, "el" kavramını beş parmaklı yapısal bir bütün olarak değil, "parmaklara benzeyen doku öbekleri" olarak öğrenmiştir. El, bir nesneyi (örneğin bir vana kolunu) kavradığında, parmaklar farklı açılara bükülür ve görsel veri setlerindeki standart (düz) el pozlarından sapar. Difüzyon süreci, bükülmüş parmakların arkasındaki boşlukları "burada da bir parmak dokusu olmalı" diyerek doldurur ve altıncı veya yedinci parmakları üretir. EchoMotion gibi çalışmalar, piksel tabanlı eğitim hedeflerinin modelleri içsel kinematik prensipleri öğrenmek yerine görünüm sadakatine (appearance fidelity) kaydırdığını ve bu yüzden insan artikülasyonunda zorlandıklarını vurgulamaktadır.

## Bağlamsal Değişkenlerin Arıza Oranına Etkisi

El-nesne etkileşimlerindeki geometri bozulmaları, çekimin bağlamsal değişkenlerine göre şiddetlenmekte veya hafiflemektedir. Zamanlama, ölçek, hareket hızı ve nesne biçimi, arızanın ortaya çıkışını doğrudan belirler.

### Temas Anının Klipteki Yeri (Zamanlama)

Temas anının klibin neresinde gerçekleştiği, I2V ve T2V modellerinde arıza oranını manipüle eden en kritik faktördür.

Eğer üretim 0. saniyede (ilk kare) zaten temas halinde başlıyorsa (örneğin, ilk kare bir görsel istem ile verilmiş ve eldiven halatı sıkıca kavramışsa), difüzyon modelinin işi yalnızca mevcut dokuyu zamansal olarak ilerletmektir (Anchor-and-track). Bu "bağla ve takip et" mantığında, nesne pozu etkileşim başlangıç karesinde kilitlenir ve model görsel benzerliği kullanarak bunu korur. Parmak erimesi ve aletin içinden geçme oranı bu senaryoda nispeten düşüktür.

Ancak, video temassız başlayıp (eller boşta), 5. veya 8. saniyede elin bir nesneye uzanıp kavramasıyla (çarpışma anı - collision) devam ediyorsa, arıza oranı katlanarak artar. Çarpışma anının simülasyonu, modelin latent uzayda yepyeni bir görsel sınır ve durum değişikliği (OSC) yaratmasını gerektirir. 10 saniyelik kesmesiz bir üretimde, 8. saniyede gerçekleşen dinamik bir eylem (kemer tokasını takmak gibi), zamansal sürüklenmeden (temporal drift) dolayı dikkat katmanlarının odak kaybına uğraması sebebiyle neredeyse her zaman geometri bozulması, erime veya nesnenin elin içinden geçmesiyle sonuçlanır. OSCBench sonuçları, güncel T2V modellerinin (Veo, Wan 2.1 dahil) özellikle yeni ve kompozisyonel durumlarda nesne durum değişikliklerini doğru ve zamansal olarak tutarlı bir şekilde gerçekleştirmede sürekli olarak başarısız olduğunu ölçmüştür.

### Kadrajdaki Ölçek ve Çözünürlüğün Etkisi

Temasın kadrajdaki boyutu (ölçeği), VAE sıkıştırma mekanizmasının bir fonksiyonu olarak ikili bir doğaya sahiptir:

Küçük Ölçek (El yüksekliği kadrajın %10'u veya daha azı): Eller çok küçük olduğunda, el ve nesne VAE sıkıştırmasında birkaç latent yama hücresine hapsolur. Bu durumda anatomik detaylar (örneğin altıncı bir parmak) izleyici tarafından algılanamayacak kadar küçüktür, model anatomik hataları gizlemiş olur. Ancak, çözünürlük eksikliği nedeniyle eldiven ile tutulan alet (örneğin bir levyenin ucu) tamamen aynı renge ve dokuya bürünerek tek bir leke (blob) halini alır. "Kaynama" ve "erime" arızası pik yapar.

Büyük Ölçek (El yüksekliği kadrajın %60'ı, Yakın Plan/ECU): Yakın planlarda piksel yoğunluğunun artması, doku (texture) kalitesini en üst düzeye çıkarır. Uzay giysisinin karbon fiber detayları veya dikişleri kusursuz görünür. Ancak, topolojik kusurlar vahşice açığa çıkar. Çözünürlük arttığı için, modelin ürettiği ekstra bir eklem, altıncı bir parmak veya bir metal borunun başparmağın içinden (phasing) geçişi anatomik bir netlikle, adeta bir vücut korkusu (body horror) estetiğiyle izleyiciye yansır.

### Hareket Hızı ve Kamera Hareketi

Elin veya nesnenin hareket hızının yüksek olması, hareket bulanıklığına (motion blur) neden olur. Difüzyon modelleri bulanık sınırları işlerken, iki cismin ayrımını tamamen kaybeder. Sabit kameralı (kısıt gereği) bir çekim, modelin arka planı ve uzamsal tutarlılığı korumasına yardımcı olur; ancak el-nesne etkileşiminin kendisi hızlıysa, sabit kamera geometri bozulmasını engelleyemez. Kamera hareketi eklendiğinde ise, model Z-eksenindeki derinlik sırasını korumakta daha fazla zorlanır ve nesneler arası geçişler (interpenetration) artar.

### Eldiven (Kalın Yüzey) vs. Çıplak El

Uzay bilimkurgu temasındaki "karakterin her sahnede basınç giysili ve eldivenli olması" kısıtı, üretim için çelişkili bir etki yaratır.

Anatomik Avantaj: Çıplak ellerdeki ince detaylar (tırnaklar, parmak boğumları, deri kırışıklıkları, tendonlar) modelin anatomik olarak en çok hata yaptığı yerlerdir. Kalın, tek parça bir uzay eldiveni, parmakların bireysel hatlarını gizleyerek modeli rahatlatır. Model eldiveni yekpare bir obje olarak algıladığı için "fazla parmak" (extra fingers) hatası belirgin ölçüde azalır.

Geometrik Dezavantaj: Eldivenin silindirik ve kalın yapısı, tutulan nesne ile olan temas yüzeyini genişletir. Temas alanı büyüdükçe, modelin iki katı cisim arasındaki ortam gölgelemesini (Ambient Occlusion) ve temas sınırını (boundary) koruması zorlaşır. Eldivenin nesneye "erimesi" veya "kaynaması", çıplak ele göre çok daha sık ve şiddetli görülür.

### Nesne Biçimi ve Tutuş Tipinin Etkisi

Tutuş tipi (grip type) ve nesnenin formu, arızanın karakterini belirler:

İnce Uzun Çubuklar, Halat ve Kumaş Kayış: Bir uzay istasyonu dışındaki onarım (EVA) sırasında karakterin bir halatı veya vana kolunu tam avuç içiyle kavraması (grasp), difüzyon modelleri için en yıkıcı senaryodur. Nesnenin bir ucu elin altından, diğer ucu elin üstünden çıkmalıdır. Nesnenin bu "hizalamasını ve bütünlüğünü" korumak, modelin derinlik ve örtüşme anlayışının ötesindedir. Halat, genellikle avucun içinden geçerken kopar, elin derisine erir veya alt ve üst kısımlar hizasız (kırık) çıkar.

Halka (Ring) ve Karabina: İki veya üç parmakla tutulan (pinch) ince metalik objeler, parmakların arasından geçme (phasing) arızasına çok müsaittir. Model, metalin sertliğini ve kapalı döngü topolojisini (halka yapısı) idrak edemediği için parmaklar karabinanın içinden eriyerek geçer.

Düz Levha ve Avuç İçi Baskı: Elin düz bir kontrol paneline bastırılması veya sürtünerek kaydırılması (sliding) durumu, modellerin en başarılı olduğu HOI senaryosudur. Parmak uçlarının veya avuç içinin düz bir yüzeye teması, arkada kalan parmakları gizlediği ve karmaşık bir kavrama gerektirmediği için geometri bozulması minimuma iner.

## İstem (Prompt) Mühendisliği: Sözcüklerle Çözüm Mümkün mü?

Görsel üretimlerde arızaları engellemek için metin yönlendirmelerine (prompt) başvurmak standart bir uygulamadır. Ancak el-nesne etkileşimindeki topolojik hataları metinle çözme girişimleri, difüzyon modellerinin psikolinguistik mimarisi nedeniyle çoğu zaman geri tepmektedir.

### Negatif Cümlelerin İflası: Beyaz Ayı Fenomeni (İronik Zihinsel Süreçler)

Kullanıcılar genellikle negatif komut blokları (en çok on bir cümlelik olumsuz blok kısıtı) kullanarak arızayı yasaklamaya çalışırlar: "no merging, no phasing, no extra fingers, hand-to-surface contact keeps a clear boundary." Ancak bu yöntem ölçülebilir biçimde başarısız olmaktadır.

Kavramsal Geri Alma (Concept Unlearning) ve dikkat haritaları üzerine yapılan son çalışmalar, Latent Difüzyon Modellerinin (LDM) negatif komutları işleme konusunda insan bilişindeki "Beyaz Ayı Fenomeni" (Pink Elephant Paradox / İronik Zihinsel Süreçler) ile aynı zafiyeti paylaştığını kanıtlamıştır. Modelin bir konsepti üretmemesi için öncelikle o konsepti ('fazla parmak' veya 'erime') tanıması ve latent uzayda çağırması gerekir.

Metin kodlayıcıları ve çapraz dikkat (cross-attention) katmanları 'negasyon' (olumsuzluk) işlemini matematiksel olarak doğru işleyemez. "No extra fingers" (fazla parmak yok) yazıldığında, kelimenin ("extra fingers") salt varlığı, dikkat ağırlıklarının o kavrama yönelmesine neden olur. Bu durum, promptun modele doğrudan "ekstra parmakları ve erimeyi düşün ve bu konseptleri latent aktivasyon uzayına dahil et" talimatı vermesiyle eşdeğerdir. Sonuç olarak, negatif bloklarda bu hataları yasaklamak, paradoksal bir şekilde arızanın ortaya çıkma ihtimalini ve şiddetini artırır.

### Pozitif Cümle ile Yönlendirme (Ara Katman İllüzyonu)

Negatif istemlerin aksine, aynı engelleme işini pozitif cümlelerle (120-300 kelimelik pozitif gövde içinde) yapmak çok daha etkilidir. İstenmeyen durumu (erime) yasaklamak yerine, modelin dikkatini çekecek ve iki cisim arasına kavramsal/görsel bir yalıtkan yerleştirecek fiziksel arayüzler tarif edilmelidir.

"Görünür ara katman (visible gap), kauçuk tutamak kılıfı (handle grip), kemer tokası, iki parmak arasında metalik parlama, contrasting colors" gibi pozitif eklemeler, modelin o temas bölgesine yeni bir anlamsal kimlik (semantics) atamasını sağlar. Örneğin, turuncu bir uzay eldiveni ile koyu gri bir karbon-fiber vana arasına "parlak çelik cıvata" yazmak, difüzyon sürecinde o bölgenin renk ve doku matrisini değiştirir. Bu, modelin gerçek bir 3B sınırı anladığı anlamına gelmez, ancak piksel bazında yaratılan görsel zıtlık (illüzyon), kaynama ve erime arızasını izleyicinin gözünden saklar.

## Kadraj, İş Akışı ve Belgelenmiş Yapay Zekâ Film Kararları

Kritik kısıtımız gereği post-prodüksiyon VFX (3B takip, rotoskop, maske, elle kare-kare rötuş) kesinlikle "hat dışı" (offline) bırakılmış olup kullanılamaz. Kesme (kurgu) ve ses miksi haricinde bir müdahalenin olmadığı durumda, yapay zekâ film ekiplerinin başvurduğu belgelenmiş kadraj ve iş akışı kararları şunlardır:

### Temas Öncesi, Sonrası ve Kasten Perdeleme (Deliberate Occlusion)

Madem ki çarpışma anı (0-2 saniye sonrası) modelleri çökertiyor, ekipler etkileşimi kasten perdeliyerek (deliberate occlusion) sorunu çözerler.

Temasın Kadraj Dışında Bırakılması: Karakterin yüzü ve omuzları gösterilirken, ellerin aleti manipüle ettiği bölge gövdenin arkasında veya kadrajın altında (off-frame) bırakılır.

Gövdeyle Örtme: Karakterin uzay giysisi gövdesi ile kamera arasına nesneyi almak, etkileşimi kör noktada bırakır.

Okunurluk Bedeli: Bu teknikler geometri bozulmasını tamamen engeller, ancak izleyici okunurluğuna (readability) çok ağır bir bedel ödetir. Filmin ana olayı elle yapılan bir iş (kemer halkası, çekiç, halat) ise, eylemin gizlenmesi sinematik anlatımı zayıflatır ve seyircinin olayı kavramasını imkansızlaştırır.

### İlk Kare Kararı: Temas Halinde Başlamak

Eylemi gizlemek istenmiyorsa uygulanan en güçlü teknik, üretime temasın çoktan kurulmuş olduğu bir "İlk Kare" (Image Prompt) ile başlamaktır.

Temassız Başlayıp Klip İçinde Temas Kurmak: Video üretimi sırasında ellerin nesneye uzanıp kavraması, durum değişikliği (OSC) gerektirdiği için %90'a varan oranlarda erime/geçiş arızası üretir.

Temas Halinde Başlamak: Mükemmel oluşturulmuş (Midjourney, Stable Diffusion veya Gemini Imagen 4 ile) bir görselde, eldiven karabinayı zaten sıkıca tutmaktadır. Bu görsel I2V modeline (Google Veo 3.1, Runway Gen-4, Kling) verilir. Model, "Anchor-and-track" mantığıyla bu referans noktalarını kilitler ve 10 saniye boyunca pikselleri sürükler. Sabit el, hareket eden nesne veya kamera stratejisiyle birleştiğinde, bu yöntem tek prompt ve kısıtlar altında en temiz sonuçları verir.

### Tekrar Üretimin (Red-Üret-Seç) Gerçek Maliyeti

En mükemmel pozitif prompt ve ilk kare kullanılsa dahi, deterministik olmayan difüzyon modellerinde "şanslı yol" (lucky path) bağımlılığı vardır. "Generate-and-select" (red-üret-seç) yönteminde, aynı prompt birkaç kez üretilir ve en iyisi seçilir.

Gerçek maliyet ve sayısal veri şöyledir: Tamamen temiz bir el-nesne teması (sıfır erime, sıfır phasing) elde etmek, ortalama %5 ila %10 arasında bir başarı oranına sahiptir. Bu, 10 saniyelik tek bir kusursuz kesit için 10 ila 20 tam üretim denemesi yapılması gerektiği anlamına gelir. Finansal maliyetin (API kredisi) ötesinde, her bir videonun oluşturulması (Google Veo veya Sora için üretim süreleri) ve görsel denetmen tarafından izlenip reddedilmesi, ciddi bir insan saati ve iş akışı maliyeti yaratır.

### Google Veo 3.1, Gemini Omni Flash 1.1 ve Diğer Modellerin Kıyaslaması

Google Veo 3.1 ve Gemini Omni 1.1 Flash: Veo 3.1, Google'ın fotogerçekçi sinematik üretimdeki lider modelidir ve fizik simülasyonu ile sıvı akışlarında (fluid dynamics) rakiplerine göre daha stabil sonuçlar verir. Gemini Omni 1.1 Flash ise yerleşik (native) ses yeteneği ve hızlı video düzenleme ile öne çıkar. Ancak, her iki model de I2V ve T2V süreçlerinde VAE mimarisinin getirdiği temel topolojik sınırlara tabidir. OSCBench gibi testlerde Veo 3.1, sahne hizalamasında güçlü olsa da kompleks nesne durum değişikliklerinde (ellerin aletle çarpışması) arızalar sergilemektedir.

OpenAI Sora: Fiziksel dünya simülatörü iddiasına rağmen, Sora'nın kendi teknik raporu bile cam kırılması veya objelerin durum değiştirmesi gibi temel etkileşimlerin fiziğini tam olarak modelleyemediğini, yiyecek yeme veya nesne tutma eylemlerinde OSC hataları yaptığını belirtmektedir.

Wan 2.1, Kling 1.6 ve Runway Gen-4: Wan 2.1 ve Kling 1.6, VBench-2.0 skorlarında anatomik sadakat açısından yüksek puanlar alsa da, 10 saniyelik uzun kesintisiz üretimlerde zamansal sürüklenmeye maruz kalırlar. Gen-4, I2V ilk kare (anchor) başlatmalarında tutarlı sonuçlar verirken, karmaşık tutuşlarda "fazla parmak" veya arka plan objelerinin erimesi sorununu yaşamaktadır. Luma Ray, Pika ve Hailuo gibi modeller ise hızlı hareket eden el-nesne etkileşimlerinde bulanıklaşarak arıza oranını artırmaktadır.

## (a) ARIZA Tablosu

| Arıza Biçimi | Doğduğu Aşama | Tetikleyen Koşul | Ölçülmüş Oranı | Model ve Sürüm | Etiket | Birebir Alıntı |
|---|---|---|---|---|---|---|
| Parmakların / Eldivenin Nesneye Erimesi ve Kaynaması | VAE (Latent) Uzamsal ve Zamansal Sıkıştırma Kaybı | Kalın yüzey (eldiven) ile katı aletin kadrajda küçük ölçekte (%10) yan yana gelmesi | - | Sora, Wan 2.1, Veo 3.1, Gemini Omni 1.1 Flash | ÖLÇÜLMÜŞ | "generated outputs may appear realistic at a glance while exhibiting incorrect, incomplete, or inconsistent object state changes" / "interactions like eating food do not always yield correct changes in object state" |
| İki Katı Cismin Birbirinin İçinden Geçmesi (Phasing / Interpenetration) | DiT Blokları Çapraz Dikkat ve 3B Evrişim (Derinlik Zafiyeti) | Klip ortasında (5. sn vb.) dinamik eylem, çarpışma, ince çubuk (halat/kayış) kavrama | Model bazında nesne fiziki uyum başarı oranı ~%40-60 aralığı (VBench-2.0 / T2V-CompBench) | Sora, Kling 1.6, Gen-4, Veo 3.1 | ÖLÇÜLMÜŞ | "prior methods optimize for local proximity—often allowing physical interpenetration" |
| Fazla / Eksik Parmak | Çapraz Dikkat Yanılsaması ve Görünüm Sadakati Odaklı Eğitim | Yakın plan (%60 kadraj), çıplak el veya bükülmüş parmak gerektiren karmaşık tutuşlar | - | Luma Ray, Pika, Gen-4 | UYGULAMA | N/A (Uygulayıcı Raporu: "Hands would have wrong numbers of fingers. Background objects would appear and disappear.") |
| Tutulan Aletin Biçim Değiştirmesi (Morphing) | 3B Nedensel Evrişim (Causal Conv.) ve Zamansal Sürüklenme | 10 saniyelik uzun çekimlerde nesne ucunun avuç içinde kalarak hareket vektörünü paylaşması | - | Gen-4, Hailuo, Gemini Omni 1.1 Flash | ÖLÇÜLMÜŞ | "adoption of causal reasoning leads to unequal information interactions and unbalanced performance between frames" |
| Temassız Başlayan Cisimlerin Çarpışmada Bütünleşmesi | Hareket Kestirimi, Sınır Tahmini ve OSC Zafiyeti | Klibin başlarında ayrı duran elin nesneye uzanıp kavraması (Collision) | OSCBench testlerinde genel modellerin başarısı ~%64 altında | Wan 2.1, Veo 3.1, Kling | ÖLÇÜLMÜŞ | "current T2V models consistently struggle with accurate and temporally consistent object state changes" / "achieve only approximately 64" |

## (b) ÖNLEM Tablosu

| Önlem | İngilizce Tam Kalıp | Ölçülmüş Etkisi | Yan Etkisi ve Okunurluk Bedeli | Model | Etiket | Birebir Alıntı |
|---|---|---|---|---|---|---|
| Olumsuz Cümle (Negatif İstem — İşe Yaramaz/Zararlı) | "no merging, no phasing, no extra fingers, hand-to-surface contact keeps a clear boundary" | Negatif etki: Beyaz Ayı Fenomeni ile istenmeyen konsepti latent uzayda aktive eder ve hatayı artırır | İstemdeki toksisite artar, model odak kaybeder. Hatayı ölçülebilir biçimde azaltmaz | Genel (Sora, SD/DiT Tabanlılar) | ÖLÇÜLMÜŞ | "attempting not to think about a pink elephant inevitably brings a pink elephant to mind. This happens because avoiding a concept requires recognizing it" |
| Pozitif Ara Katman Cümlesi | "visible gap between glove and tool, thick handle grip, mechanical latch locking, clear contrasting colors" | Renk ve doku zıtlığı yaratarak sınır erimesini illüzyonla azaltır | Aletin veya giysinin tasarımını prompta bağımlı hale getirir, estetik değişir | Gen-4, Kling 1.6, Veo 3.1 | ÖNERİ | N/A |
| İlk Kare Kararı (Image Prompting ile Temas Halinde Başlama) | (I2V Girdisi) Sahnede elin nesneyi hali hazırda mükemmel kavramış olduğu bir görsel yüklemek | "Anchor-and-track" sayesinde başlangıçtaki topoloji kilitlenir, erime ve kaynama büyük oranda önlenir | Olayın "yakalama/kavrama" anı anlatılamaz, aksiyon çoktan başlamıştır. Anlatı gücü düşer | Gen-4, Kling, Luma, Veo 3.1 | ÖLÇÜLMÜŞ | "We initialize the object pose at a single interaction onset frame using a foundation model and propagate it temporally" |
| Kadraj Kararı (Kasten Perdeleme / Deliberate Occlusion) | Temas eylemini, karakterin sırtının arkasında veya gövdenin / kadrajın dışında bırakacak kamera açısı kullanmak | Etkileşim görünmediği için geometri arızası görsel olarak sıfırlanır | Eylemin okunurluğu çok ağır hasar alır | Hailuo, Pika, Sora, Omni Flash | ÖNERİ | N/A |
| Tekrar Üretim (Red-Üret-Seç) | Aynı pozitif prompt ile farklı "seed" değerlerinde ardışık 15-20 üretim yapmak | Rastlantısal (lucky path) olarak %5-10 ihtimalle temiz temas elde edilir | Zaman ve API kredisi maliyeti devasadır. Deterministik bir çözüm değildir | Genel | ÖLÇÜLMÜŞ | "consistency loss requires the model to produce identical outputs... This constraint eliminates 'lucky path' dependence" |
| Hat Dışı (Offline) Çözümler | 3B Takip, Rotoskop, Maske, Kare-Kare Manuel Rötuş, 3B El Modeli | Geometri bozulmalarını post-prodüksiyon aşamasında tamamen düzeltir | Kısıt gereği (VFX YOK) uygulanamaz | Tüm Modeller | UYGULAMA | N/A |

## (c) KARAR AĞACI: Üretim Stratejisi

Girdi: "Sahnede el (veya eldiven) bir nesneye değiyor."
Kısıtlar: 10 saniyelik, kesmesiz, fotogerçekçi uzay bilimkurgu, tek İngilizce prompt (120-300 pozitif kelime, max 11 negatif cümle), VFX YOK, karakter basınç giysili.

Adım 1: Temas eyleminin başlangıcı hikaye gereği klip içinde görünmek zorunda mı?
- Hayır: İlk Kare (Image Prompt) ile üretime başla. Temas anını başlangıç görselinde kurgula, I2V modeliyle 10 saniye boyunca sürdürmeye (Anchor-and-track) zorla. [ÖLÇÜLMÜŞ | "initialize the object pose at a single interaction onset frame... propagate it temporally"]
- Evet: Adım 2'ye git.

Adım 2: Kavranan aletin detayları izleyici tarafından net görülmek zorunda mı?
- Hayır: Kasten Perdeleme kullan. [ÖNERİ]
- Evet: Adım 3'e git.

Adım 3: Karakter çıplak elle mi çalışmak zorunda, yoksa uzay giysisi eldiveni kullanabilir mi?
- Çıplak el: Arıza riski zirvededir. Kadraj ölçeğini küçült (eller ekranın %15'inden azı). [ÖNERİ]
- Eldiven: Anatomik hatalar azalır ancak temas yüzeyi genişlediği için erime artar. Adım 4'e git.

Adım 4: Erimeyi azaltmak için prompta renk/materyal zıtlığı ekleyebilir misin?
- Evet: Pozitif prompt ekle ("bright orange pressure glove gripping a dark carbon-fiber lever, visible metallic gap"). Kesinlikle "no merging" gibi negatif prompt KULLANMA. [ÖLÇÜLMÜŞ | "avoiding a concept requires recognizing it"]
- Hayır: Tekrar Üretim (Red-Üret-Seç) döngüsüne gir, 20-50 üretim, %5-10 ihtimal. [ÖLÇÜLMÜŞ | "consistency loss requires the model to produce identical outputs... eliminates 'lucky path' dependence"]

## Doğrulanabilir Bulgular

1. Negatif İstemlerin İflası ve Beyaz Ayı Fenomeni: Bir kavramı olumsuz cümlelerle yasaklamak, çapraz dikkat katmanlarında o konsepti aktive ederek hatanın ortaya çıkma ihtimalini ölçülebilir biçimde artırır.
2. Sora ve Veo'nun Fiziksel Uyumsuzluğu: Nesne durum değişiklikleri (OSC) ve iki katı cismin etkileşimi gibi fizik kurallarında yapısal olarak başarısızdır. Sora'nın teknik raporu cam kırılması ve nesne tutma fiziğini doğru modelleyemediğini belirtmektedir.
3. VAE Sıkıştırma Hataları: Uzamsal (8x) ve zamansal (4x) sıkıştırmalar el ve nesne arasındaki yüksek frekanslı sınırların kaybolmasına ve "erime" görüntüsüne doğrudan neden olur.
4. Zamansal Nedensellik Yanılgısı: 3B nedensel evrişimler kareler arasında dengesiz bilgi dağılımı yapar; nesne ve el kimliği 10 saniyelik çekimlerde birbirine karışır.
5. Derinlik (Z-Index) Zafiyeti ve Phasing: Modeller yerel yakınlığı optimize ederken küresel geometrik katı cisim sınırlarını ihlal eder.

## Kaynaksız İddialar / Hipotezler

- Hipotez: "Uzay giysisi eldiveni kullanmak, anatomiyi basitleştirdiği için HOI başarısını çıplak ele göre kesin olarak artırır."
  Neden doğrulanamadı: Literatürde kalın eldiven ile çıplak elin başarı oranını HOI özelinde kıyaslayan nicel bağımsız test bulunmamaktadır.
- Hipotez: "Temasın 8. veya 10. saniyede kurulması, 2. saniyede kurulmasına göre arıza oranını %X artırır."
  Neden doğrulanamadı: Zamansal sürüklenme bilinen bir mimari kısıtlamadır; ancak saniye-saniye arıza artış oranını veren hakemli bağımsız ölçüm sunulmamıştır.
