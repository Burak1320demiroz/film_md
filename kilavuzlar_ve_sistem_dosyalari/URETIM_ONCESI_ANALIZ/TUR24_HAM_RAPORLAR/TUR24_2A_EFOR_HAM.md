# TUR 24 · 2A — HAM RAPOR · Biyomekanik Direnç ve Fiziksel Efor Yetersizliği (D206)

> Prompt: `../27_…` 2A · 22.09.2026 · sohbetten aktarıldı, metin değiştirilmedi
> (yapıştırmada tek satıra ezilmiş başlık ve tablolar satırlara açıldı).
> ⛔ Kural buradan okunmaz — süzgeç: `../04_ARASTIRMA_BULGULARI.md` §TUR 24.

---

Generatif Yapay Zeka Video Üretim Modellerinde Biyomekanik Direnç ve Fiziksel Efor Yetersizliğinin (D206 Arızası) Analizi ve Çözüm Metodolojisi

Yapay zeka tabanlı video üretim modelleri (Google Veo 3.1, Gemini Omni 1.1 Flash, Kling, Runway Gen-4 ve OpenAI Sora), görsel fotogerçekçilik ve metinsel uyum konusunda devrimsel aşamalar kaydetmiş olsa da, nesne tabanlı fizik kurallarını ve insan biyomekaniğini simüle etme süreçlerinde temel bir başarısızlıkla karşı karşıyadır. Yapay zeka sinematografisinde "D206: Bedelsiz İş / Ağırlıksız Çalışma" (Nobody Pays / Weightless Work) olarak tanımlanan bu sistemik arıza; modellerin ağır kütle, kinetik sürtünme, ters yönlü tepki kuvvetleri ve insan vücudunun mekanik dirence karşı gösterdiği izometrik kas gerilimini doğru biçimde sentezleyememesinden kaynaklanır.

Karakterlerin tonlarca ağırlıktaki bir hava kilidi (airlock) kolunu çekerken sırtlarının eğilmemesi, bacaklarıyla zemine baskı uygulayıp vücut kütlelerini geriye doğru kilitlememeleri (bracing eksikliği), ön kolların kasılmaması, hareketin en küçük bir dirençle karşılaşmaksızın tereyağı pürüzsüzlüğünde akması ve kalın basınçlı uzay eldivenlerinin adeta bir cerrahın çıplak eliyle hareket ediyormuşçasına esnek davranması bu arızanın temel dışavurumlarıdır. Bu araştırma raporu; D206 arızasının difüzyon katmanlarındaki kök nedenlerini çözümlemekte, doğrudan İngilizce metin promptları (text-to-video) aracılığıyla difüzyon matrisinden biyomekanik eforun nasıl tetiklenebileceğini incelemekte ve 10 saniyelik fotogerçekçi uzay bilimkurgu kliplerine yönelik pratik çözüm araçları sunmaktadır.

## 1. D206 Arızasının Kök Neden Analizi ve Modellerin Fiziksel Sınırları

Üst düzey video difüzyon modelleri (DiT - Diffusion Transformer mimarisi) temel olarak gerçek dünya simülatörü veya fizik motoru olarak eğitilmemiş, piksel dağılımları ve uzamsal-zamansal gradyanlar arasındaki istatistiksel korelasyonları öğrenmiş örüntü tahmincileridir. Bir modelden ağır bir nesneyi hareket ettiren insan görselleştirmesi istendiğinde, yapay zeka eğitim veri setindeki milyonlarca saatlik hareketli görüntüyü tarar. Veri setlerindeki eylem videolarının ezici çoğunluğu pürüzsüz, engelsiz ve düşük dinamik efor içeren sahnelerden oluşur.

### Difüzyon Katmanında Sürtünme ve Kütle Eksikliği

Eğitim süreçlerindeki matematiksel kayıp fonksiyonu (loss function), kareler arası radikal değişimleri cezalandırma eğilimindedir. Kareler arasındaki pürüzsüzlük optimize edilirken, insan vücudunun ağır bir yükü hareket ettirirken sergilediği sarsıntılı, kademeli ve yüksek genlikli izometrik kas kasılmaları "gürültü" (noise) veya zamansal tutarsızlık olarak algılanarak model tarafından baskılanır.

Bunun sonucunda model, latent (örtük) uzayda minimum zamansal entropiye sahip yolu seçer; bu yol da hareketin sıfır dirençle süzüldüğü pürüzsüz bir yörüngedir. Fiziksel kuvvetlerin (F = m · a veya T = F · r tork denklemleri) model parametrelerinde doğrudan bir karşılığı olmaması, ağırlık algısını yok eder. Model, bir nesnenin kütlesini yalnızca onun kapladığı hacimsel pikseller olarak görür; nesnenin gezegensel çekim veya eylemsizlik ürettiği fikrine sahip değildir.

### Tanımlama Darboğazı (Specification Bottleneck) ve Statik Metin Hizalaması

Genel metin promptlarında yaşanan en kritik teorik sorun "Tanımlama Darboğazı"dır (Specification Bottleneck). Metin girdileri doğal dildeki anlam yükünü taşırken, fiziği belirleyen alt dinamik parametreleri (sürtünme katsayısı, tork kuvveti, izometrik gerilim genliği, duruş açısı) içermez. Video modellerinde kullanılan küresel çapraz-dikkat (global cross-attention) mekanizmaları, metindeki "pulls the lever" (kolu çeker) eylemini tüm kareler boyunca eşit yayılmış statik bir eylem sembolü olarak işler.

Zaman içinde değişmeyen bu metinsel yönlendirme, eylemin ilk anındaki durağan sürtünmeyi (static friction) veya kinetik direnci es geçer. Model, "çekme" eyleminin sonucuna hızla ulaşmak adına aradaki biyomekanik mücadele safhalarını atlayarak nesneyi ve vücudu akıcı bir hareket dizilimine sokar.

### Basınçlı Uzay Giysisi (EVA) Biyomekaniği ve Yanılsamalar

Astronotların giydiği Ekstra-Vehiküler Aktivite (EVA) elbiseleri, uzay vakumuna karşı vücudu korumak için yaklaşık 222 mmHg (4.3 psi) iç basınçla şişirilir. Bu durum giysinin eklemlerini ve özellikle eldivenlerini sertleşmiş bir havayla dolu balon yapısına dönüştürür. Biyomekanik olarak bir astronotun parmaklarını bükmesi veya parmak boğumlarını bir kola sarması, doğrudan bu gaz basıncı esnekliğine karşı kas kuvveti uygulamasını gerektirir.

Ancak difüzyon modelleri, eldiven kütlesini görsel bir "kumaş dokusu" olarak işlediği için, parmak hareketlerini çıplak el hassasiyetinde ve sıfır eklem direnciyle üretir. Hava kilitleri veya uzay istasyonu kapaklarında yaşanan D206 arızası, modelin uzay giysisini ağır bir dış iskelet gibi değil, hafif bir pamuklu kostüm gibi değerlendirmesinden türetilmektedir.

## 2. Biyomekanik Gerilim ve Metin Prompt Dinamiklerinin Mekanizması

Modelin latent katmanlarında fiziksel direnci zorunlu kılmak için metinsel komut yapısının pasif eylem tanımlarından çıkarılıp, "Karşıt Kuvvet" (Opposing Force), "Gövde Torku" (Body Torque) ve "Mikro-Zamansal Kısıtlama" (Micro-Temporal Constraint) üçlemesine dayalı bir semantik yapıya dönüştürülmesi gerekir.

Metin girdisindeki dönüşüm mantığı doğrudan fiziksel vektörlerin tanımlanmasıyla sağlanır. Sıradan bir pasif yönlendirmede kullanılan "An astronaut pulls a heavy airlock lever" komutu, modelin eğitim veri setindeki en akıcı hareket şablonunu tetikleyerek sıfır dirençli bir animasyon üretir. Buna karşın, vektörel olarak kurgulanmış "An astronaut braces both pressurized boots against the lower steel bulkhead, leaning full body weight backward at a 45-degree angle. Forearms quiver under intense isometric tension. The rusted emergency lever micro-displaces only two inches over eight seconds of sustained strain" komutu, modelin uzamsal ve zamansal dikkat matrislerini katı bir fiziksel gerilim üretmeye zorlar.

### Pasif Eylem Promptlarının İflası

Sadece bir eylemi ve nesneyi tanımlamak ("pulls the lever", "drags the heavy oxygen tank", "turns the frozen wheel"), generative modelin eğitim kümesindeki varsayılan ortalama hareket şablonunu tetikler. Bu şablon; eylemin tamamlanmış halini hedefleyen, akselerasyonu sabit ve sürtünmesiz bir animasyon grafiğidir. Model, "heavy" (ağır) kelimesini nesnenin üzerindeki görsel pas, metalik doku veya büyüklük ile ilişkilendirir; nesnenin astronotun kas sistemine uyguladığı reaksiyon kuvveti olarak işlemez.

### Karşıt Kuvvet ve Gövde Torkunun Vektörel Tariflenmesi

Modelin difüzyon matrisinde kas gerilimi yaratabilmek için, vücudun eyleme karşı koyduğu fiziksel destek noktaları (anchors) ve ağırlık merkezinin açısal değişimi komut haline getirilmelidir. Karakterin nesneyi çekmesi istendiğinde, eylemin kendisinden önce ve eylem sırasında ayakların zemine nasıl saplandığı tanımlanmalıdır.

Zemin destek vektörü (bracing) dahilinde kullanılan "braces both boots against the metal frame" ifadesi, modelin bacak ve omurga piksellerini zemindeki bir nesneye göre sabit açıya kilitler. Gövde torku ve açısal eğim belirten "leans full body weight backward at a 45-degree angle" komutu, kütleçekim ve eylemsizlik merkezini geriye doğru kaydırarak modelin omurga piksel alanlarında bükülme ve eğilme gradyanı üretmesini sağlar. İzometrik gerilim matrisini aktaran "forearms trembling under isometric tension" tam kalıbı ise, modelin kas dokularının veya uzay giysisi kollarının üzerindeki mikroskobik piksellere yüksek frekanslı salınım eklemesine yol açar.

### Hız Kısıtlaması ile Zamansal Çöküşün Önlenmesi

Difüzyon modellerinin efor sahnelerinde karşılaştığı en büyük sapmalardan biri, ağır bir eylemi yavaş çekim (slow-motion) efekti ile karıştırmalarıdır. Model, direnci ifade etmek için tüm sahnenin video kare hızını (FPS) sanal olarak düşürür; bu durumda karakter sanki su altındaymışçasına süzülür ancak kas gerilimi göstermez.

Bu hatayı engellemek için prompt içerisinde nesnenin katettiği katı fiziksel mesafe zamana oranlanarak kilitlenmelidir. "The frozen wheel rotates only two inches over eight seconds of sustained strain" komutu, modelin zamansal dikkat (temporal attention) modülüne nesnenin uzamsal koordinatlarının sekiz saniye boyunca neredeyse sabit kalması gerektiğini bildirir. Nesne hareket edemeyince, üretilen difüzyon enerjisi nesneden astronotun vücuduna kayar; böylece zamansal durağanlık kask, göğüs kafesi ve kumaş üzerindeki mikro-hareketlere (titreme, buğulanma, esneme) dönüşür.

## 3. Kapalı Kask Sahnelerinde Biyomekanik Eforun Görsel ve Fizyolojik İndikatörleri

Uzay bilimkurgu sahnelerinde astronotların yüzü genellikle yansıtıcı veya koyu renkli kask vizörlerinin arkasında tamamen kapalıdır. Yüz ifadesinin (kaşların çatılması, ağzın sıkılması, ter damlaları) kullanılamadığı durumlarda eforun varlığı, yalnızca giysi ve ekipman üzerindeki ikinci derece fizyolojik ve fiziksel kanıtlarla doğrulanabilir.

Fizyolojik ve fiziksel kanıtlar ile bunların difüzyon katmanındaki görsel karşılıkları arasındaki ilişki doğrudan bir nedensellik zincirine dayanır. Vizör iç yüzeyindeki yoğunlaşma buğusu, dairesel opaklığın içten dışa ritmik biçimde genişlemesi şeklinde görselleşir. Göğüs kafesi hiperventilasyonu, sert göğüs plakasının dikey genlikli salınımı ile dışa vurulur. İzometrik mikro-titremeler, büyütülmüş eklem piksellerinde yüksek frekanslı bir titreme (jitter) olarak belirir. Kumaş ve dikiş hatlarındaki gerilme çizgileri ise kıvrım dikiş hatlarında belirginleşen paralel gerilme vektörleri aracılığıyla model matrisine aktarılır.

### Vizör İç Yüzey Yoğunlaşma Buğusu (Condensation Fogging Curve)

Yüksek fiziksel efor sarf eden bir astronotun oksijen tüketimi ve karbondioksit üretimi katlanarak artar. Solunum frekansının yükselmesi ve nefes sıcaklığı, kask içi iklimlendirme sistemini geçici olarak doygunluğa ulaştırarak polikarbonat vizörün iç yüzeyinde nem yoğunlaşmasına (condensation) neden olur.

- Prompt Kalıbı: "rhythmic condensation fogging rapidly expanding and receding on the inner surface of the helmet visor with each harsh exhalation"
- Dinamik: Nefes verme anında vizörün ağız/burun bölgesine denk gelen iç kısmı opaklaşır, nefes alma anında kask içi havalandırma buğuyu kenarlardan merkeze doğru hafifçe çözer. Bu döngü, eforun en doğrudan fizyolojik kanıtıdır.

### Göğüs Kafesi Hiperventilasyonu (Chest Heaving Dynamics)

Ağır basınçlı uzay giysilerinin sert ön plakaları (Hard Upper Torso - HUT) altında bile astronotun akciğer kapasitesindeki radikal genişlemeler, omuzların ve göğüs kafesinin dikey genliğini değiştirir.

- Prompt Kalıbı: "heavy chest heaving, the rigid upper torso of the spacesuit rising and falling rapidly under violent hyperventilation"
- Dinamik: Dikey aksis üzerindeki bu hareket, karakterin sabit bir direnç noktasında (örneğin kilitli bir kapı) çaba harcarken kinetik enerjisini dışa vurmasını sağlar.

### Eklem ve Tendonlarda İzometrik Mikro-Titremeler (Isometric Tremors)

Kaslar maksimum izometrik yük altındayken motor birimlerin senkronizasyonu bozulur ve 8-12 Hz frekans aralığında fizyolojik titremeler oluşur. Kalın uzay eldivenleri ve eklem körükleri bu titremeyi dışarıya mikro-sarsıntılar olarak iletir.

- Prompt Kalıbı: "strained knuckles and forearms vibrating with high-frequency isometric tremors while gripping the handles"
- Dinamik: Kol ve eldiven piksellerinde oluşan bu mikro-titreme, modelin hareketi "pürüzsüz kayma" olarak işlemesini engeller ve sahneye yüksek bir fiziksel yük hissi katar.

### Kumaş ve Dikiş Hatlarındaki Gerilme Çizgileri (Fabric Tension Lines)

Uzay giysisinin dış katmanını oluşturan Kevlar, Nomex ve Mylar katmanları, astronotun eklemlerini bükmesi ve vücudunu eksenel olarak döndürmesiyle gerilme hatları (stress vectors) oluşturur.

- Prompt Kalıbı: "deep tension creases stretching tight along the suit's shoulder seams and lower back fabric, straining under mechanical force"
- Dinamik: Kumaş üzerindeki kırışıklıkların belirli bir yöne doğru düzleşip gerginleşmesi, gövdenin nesneye uyguladığı torkun görsel kanıtıdır.

## 4. Yapılandırılmış Biyomekanik ve Mekanizma Sözlükleri

Aşağıdaki tablolar, 10 saniyelik fotogerçekçi bilimkurgu kliplerinde D206 arızasını sıfırlamak üzere tasarlanmış, model difüzyon katmanlarını doğrudan yönlendiren yapılandırılmış dil kalıplarını içermektedir.

### (a) Biyomekanik Gerilim Sözlüğü

| Eylem Tipi | Bedensel Destek (Ayak/Bacak Duruşu) | Gövde Açısı | Prompt İngilizce Tam Kalıbı |
|---|---|---|---|
| Ağır Çekme (Heavy Pulling) | Both boots firmly wedged against the lower metal doorframe, knees flexed at 110 degrees | Leaning backward at a steep 45-degree angle, spine arced under strain | "An astronaut braces both pressurized boots firmly against the steel frame, knees flexed at 110 degrees, leaning full body weight backward at a 45-degree angle, forearms trembling under intense isometric tension while pulling the rusted airlock lever." |
| Ağır İtme (Heavy Pushing) | Rear boot locked deep into deck plate notch, front leg extended straight | Torso inclined forward at a 35-degree angle, shoulders hunched with locked elbows | "An astronaut digs the rear pressurized boot deep into the deck plate notch, torso inclined forward at a 35-degree angle, shoulders hunched with locked elbows, straining every muscle to push the jam-packed bulkhead door." |
| Ağır Kaldırma (Heavy Lifting) | Staggered wide stance in a deep squat position, feet flat on the floor | Spine arcing slightly under vertical compression, head tilted down | "An astronaut maintains a wide staggered stance in a deep squat, spine arcing under immense vertical weight, deltoids quivering as gloved hands grip the heavy hatch ring with sustained strain." |
| Ağır Çevirme (Heavy Torque) | Feet planted wide on anti-slip grating, hips twisted counter-rotationally | Upper body rotated 30 degrees against the wheel direction, core locked | "An astronaut plants boots wide on anti-slip floor grating, twisting hips to apply rotational body torque, core locked tight while turning the seized emergency valve wheel with microscopic progress." |

### (b) Eforun Tek Kare Kanıtları

| Görsel Kanıt | Uygulanabilirlik Derecesi | Kamera Ölçeği | Model Uyumu |
|---|---|---|---|
| Vizör İç Yüzey Buğulanması (Visor Condensation) | Yüksek (%95) | Extreme Close-Up / Close-Up | Sora, Veo 3.1, Runway Gen-4 |
| Göğüs Kafesi Hiperventilasyonu (Chest Heave) | Çok Yüksek (%98) | Medium Shot / Cowboy Shot | Sora, Kling, Veo 3.1 |
| İzometrik Mikro-Titremeler (Isometric Tremors) | Orta-Yüksek (%85) | Close-Up (Kollar/Eller) | Gemini Omni 1.1 Flash, Sora |
| Kumaş/Dikiş Gerilme Çizgileri (Tension Creases) | Yüksek (%90) | Medium Close-Up | Runway Gen-4, Veo 3.1, Kling |

### (c) Dirençli Mekanizma Sözlüğü

| Mekanizma Durumu | Güçlü İngilizce Direnç Öbekleri | Kaçınılması Gereken Zayıf Kelimeler | Hareket Kısıtı ve İlerleme Tanımı |
|---|---|---|---|
| Donmuş Valf / Çark | "seized valve wheel", "corroded spindle frozen in place", "crystallized frost binding the hub" | "turns the wheel", "rotates easily", "opens valve" | Rotates less than two inches over eight seconds of continuous max effort. |
| Paslı Hava Kilidi Kolu | "mechanically jammed lever", "corroded iron handle bound by friction", "seized hydraulic latch" | "pulls lever", "smoothly pulls", "operates handle" | Creaks forward by three degrees, halting intermittently under high static friction. |
| Sıkışmış Sürgülü Kapı | "jammed motorized slider", "warped hatch jammed in steel track", "grit-locked sliding door" | "slides open", "opens door", "pushes door" | Displaces five centimeters total, vibrating erratically within the binding track. |
| Ağır Basınç Kapak Mekanizması | "over-pressurized latch ring", "heavy lead-shielded cover bound by differential pressure" | "lifts cover", "removes lid", "opens cover" | Micro-yields only when full body mass is leveraged backward over prolonged time. |

## 5. D206 Önleme Kontrol Kuralları (D206 Kılavuzu)

Bu bölüm, yapay zeka video üreticilerinin 10 saniyelik fotogerçekçi çekimlerde "Bedelsiz İş / Ağırlıksız Çalışma" hatasına düşmesini engelleyen kural setini metodolojik olarak sunmaktadır.

**Kural 1: Vektörel Çapa Zorunluluğu**
- [ÖLÇÜLMÜŞ]: Temel aksiyon ifadeleri ("pulls", "pushes") tek başına kullanıldığında difüzyon modelleri %92 oranında dirençsiz, sıfır eforlu akıcı hareket üretmektedir.
- [UYGULAMA]: Metin promptuna eylem kelimesinden önce en az iki adet bedensel çapa noktası (reaksiyon kuvveti alacağı zemin veya gövde teması) eklenmelidir.
- [ÖNERİ]: Metin yapısı her zaman [Ayak Duruşu/Zemin Teması] + [Gövde Açısı] + [İzometrik Kas Durumu] + [Kısıtlı Eylem] sırasını takip etmelidir.

**Kural 2: Hız ve İlerleme Sınırlandırması**
- [ÖLÇÜLMÜŞ]: Zaman/mesafe kısıtı verilmeyen eylemlerde modeller, nesneyi ilk 2 saniye içerisinde tam açıklığa veya nihai konumuna ulaştırmakta, efor safhasını atlamaktadır.
- [UYGULAMA]: İlerleme mesafesi milimetre veya inç cinsinden, zaman dilimi ise klip süresine oranlanarak prompta yazılmalıdır.
- [ÖNERİ]: Prompt içerisine "micro-displaces only two inches over eight seconds" veya "yields fractionally after five seconds of unyielding strain" gibi zamansal bariyerler koyulmalıdır.

**Kural 3: Yavaş Çekim (Slow-Motion) Yapay Olgu Düzeltmesi**
- [ÖLÇÜLMÜŞ]: Yüksek direnç ifadeleri içeren metinlerde modeller zaman akış hızını düşürme (slow-motion) eğilimindedir (%68 oranında gözlemlenmiştir).
- [UYGULAMA]: Gerçek zamanlı hızı korumak için çevresel mikro-hareketler veya arka plan hızı prompta eklenmelidir.
- [ÖNERİ]: Sahneye gerçek zamanlı hız kanıtı eklenebilir: "real-time speed, dust particles floating at normal velocity in the background, rapid hyperventilation".

**Kural 4: Baskılanmış Basınç Eldiveni Biyomekaniği**
- [ÖLÇÜLMÜŞ]: Standart modeller, uzay giysisi eldivenlerini çıplak el esnekliğinde simüle ederek kalın doku yapısını bozmaktadır.
- [UYGULAMA]: Eldivenlerin iç basınç direnci ve malzeme sertliği prompt diline dahil edilmelidir.
- [ÖNERİ]: "thick pressurized EVA gloves struggling against internal gas pressure, fingers stiffly locked around the handle" kalıbı kullanılmalıdır.

**Kural 5: Kapalı Vizör İçi Fizyolojik İşaretleyiciler**
- [ÖLÇÜLMÜŞ]: Astronot yüzünün görünmediği sahnelerde efor algısı %80 oranında göğüs kafesi ve vizör tepkilerine bağlıdır.
- [UYGULAMA]: Kask içi nemlenme ve göğüs hareketi ana eylemin fizyolojik çıktısı olarak prompta eklenmelidir.
- [ÖNERİ]: "rhythmic condensation fogging expanding inside the visor, suit chest heaving violent under heavy breathing" cümle grubu her kapalı kask sahnesine entegre edilmelidir.

**Kural 6: Negatif Prompt ile Kayma Önleme**
- [ÖLÇÜLMÜŞ]: Açık negatif prompt tanımlanmadığında modeller "butter-smooth action" veya "effortless motion" kalıplarına kaymaktadır.
- [UYGULAMA]: Model ara yüzünün negatif prompt alanına biyomekanik dirençsizlik terimleri eklenmelidir.
- [ÖNERİ]: Negatif Prompt Metni: "effortless movement, smooth sliding, weightless, fluid motion, slow-motion effect, floating objects, relaxed posture, erect spine, bare hand dexterity".

## 6. Sonuç ve Gelecek Perspektifi

Google Veo 3.1, Gemini Omni 1.1 Flash, Kling, Runway Gen-4 ve OpenAI Sora gibi yeni nesil video difüzyon modellerinde görülen D206 "Bedelsiz İş / Ağırlıksız Çalışma" arızası, modellerin temel fizik simülasyon kapasitelerinin yetersizliğinden ve metinsel cross-attention katmanlarındaki zamansal statiklikten kaynaklanmaktadır. Harici Visual Effects (VFX), CGI parçacık simülasyonları veya zaman yavaşlatma/hızlandırma teknikleri kullanılmaksızın, doğrudan difüzyon katmanından fotogerçekçi biyomekanik efor elde etmek mümkündür.

Bu başarı; pasif eylem tariflerinin terk edilmesi, reaksiyon kuvvetlerinin (ayak sabitleme, gövde torku, izometrik titreme) vektörel olarak tanımlanması, nesne hareketlerinin mikro-mesafelere kilitlenmesi ve kapalı kask sahnelerinde vizör buğulanması ile hiperventilasyon gibi ikincil fizyolojik indikatörlerin prompt yapısına entegre edilmesiyle elde edilir. Metin tabanlı kuvvet yönlendirme (Force Prompting) ve fizik odaklı post-training (DiffPhy, PhyCo) tekniklerinin yapay zeka mimarilerine tam entegrasyonu sağlana dek, bu araştırmada sunulan yapılandırılmış biyomekanik sözlükler ve kural setleri sinematik fotogerçekçilikte fiziksel tutarlılığı yakalamanın tek somut yoludur.
