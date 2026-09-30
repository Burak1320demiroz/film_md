# TUR 24 · 2B — HAM RAPOR · Fiziksel Sadakat, D200 Yerçekimi Dalgalanmaları ve Kütlesiz Çarpışma

> Prompt: `../27_…` 2B · 22.09.2026 · sohbetten aktarıldı, metin değiştirilmedi
> (yapıştırmada hücrelere dağılmış tablolar satırlara açıldı).
> ⛔ Kural buradan okunmaz — süzgeç: `../04_ARASTIRMA_BULGULARI.md` §TUR 24.

---

Video Üretim Yapay Zekalarında Fiziksel Sadakat, D200 Yerçekimi Dalgalanmaları ve Kütlesiz Çarpışma Arızalarının Dinamik Analizi

Generatif video difüzyon modellerinin (Google Veo 3.1, Gemini Omni 1.1 Flash, Kling 3.0, OpenAI Sora 2, Runway Gen-3/Gen-4) sinematik fotogerçekçilik düzeyindeki hızlı artışı, bu sistemlerin fiziksel dünya simülasyonu yeteneklerine ilişkin ciddi tartışmaları beraberinde getirmiştir. Sinema endüstrisinde 10 saniyelik fotogerçekçi bilimkurgu sahnelerinin tekil promptlar vasıtasıyla üretimi hedeflendiğinde, fizik motoru veya post-prodüksiyon simülasyon desteği olmaksızın doğrudan model çıktısına bağımlı kalınmaktadır. Bu süreçte karşılaşılan en kritik teknik engel; sahneler arasında veya tek bir klip akışı içerisinde yerçekimi ivmesinin (g) 5 ila 10 kat arasında aniden dalgalanması olarak tanımlanan D200 "Two Gravities" problemi, kütlesiz çarpışma arızaları (solid passing through solid / ghosting), çarpışma anında kinetik momentum aktarımı yerine gerçekleşen faz geçişli morflama (morphing) ve sıvı/parçacıkların ortam yerçekimine aykırı biçimde sebepsiz havada asılı kalmasıdır (causeless floating).

## 1. D200 "Two Gravities" ve Kütlesiz Çarpışma Arızalarının Yapısal Nedenleri

Video difüzyon modelleri (Video Diffusion Models - VDMs) ve Diffusion Transformer (DiT) mimarileri, içsel olarak Newton mekaniğine dayalı diferansiyel denklem çözücüler içermez. Bu modeller, milyonlarca saatlik video verisinden öğrendikleri uzamsal-zamansal latent uzay (spatiotemporal latent space) üzerindeki olasılıksal piksel geçişlerini tahmin eden gelişmiş örüntü tanıma motorlarıdır. PhysBench, Physics-IQ / Physics-IQ Verified ve RigidBench gibi deneysel fizik doğrulamaları, güncel video üretken yapay zeka modellerinin algısal kaliteleri (visual realism) ile fiziksel gerçeklik anlayışları (physical correctness) arasında belirgin bir uyumsuzluk olduğunu kanıtlamaktadır.

Physics-IQ benchmark sonuçlarına göre, en gelişmiş yapay zeka video modelleri bile gerçek dünya fiziği varyansına kıyasla ortalama %10 ila %30 arasında başarı gösterebilmektedir. Benzer şekilde RigidBench değerlendirmeleri, üretilen videoların yapısal benzerlik skorları (SSIM) ve perceptual kaliteleri ile 3B kinetik yörünge doğruluğu arasında korelasyon bulunmadığını (r=0.002), hatta estetik açıdan en yüksek skoru alan kliplerin fiziksel yörünge sapmalarında en yüksek hatayı verebildiğini göstermektedir.

D200 "Two Gravities" arızası, modelin tek bir 10 saniyelik klip içinde iki farklı eğitim veri kümesi arasında ani mod geçişi (mode switching) yapmasıyla tetiklenir. Süreç, bağlamsal ortam belirteçlerinin ve hareket fiillerinin latent uzaydaki baskınlık mücadelesinden doğar. Sahne başlarken promptta yer alan "astronaut in space suit" ve "alien surface" gibi semantik token'lar, modelin dikkat (attention) katmanlarında düşük yerçekimli verilerle (0.16g veya 0.38g) eşleşen uzamsal-zamansal katmanları aktifleştirir. Bu evrede nesne yavaş ve geniş parabolik kavislerle hareket eder. Ancak astronot dengesini kaybedip zeminle temas edeceğinde veya bir kaza düşüşü başladığında, modelin dikkat mekanizması "falling", "crashing" ve "impact" eylemlerini eğitim setinde ezici çoğunlukla Dünya ortamında (1.0g) çekilmiş yüksek kinetik enerjili videolarla eşleştirir. Bu semantik eşleşme nedeniyle model, kaskat düzeyinde bir mod geçişi yaşayarak Ay yerçekimindeki (0.16g) bir kütleyi düşüşün son saniyelerinde 6 kat ivmelendirir ve Dünya yerçekiminde (1.0g) gibi sertçe yere çakar.

Kütlesiz çarpışma ve faz geçişi arızaları ise katı cisimlerin temas anında bir sınır koşulu (boundary condition) olarak birbirlerini tanıyamamasından kaynaklanır. Model, rijit cisimlerin birbirine nüfuz edemeyeceğini (non-interpenetration) matematiksel olarak hesaplayamadığından, nesnelerin temas noktalarında pikseller eriyerek birbirinin içinden geçer veya kinetik enerji aktarımı yapılmaksızın cisimlerin kütlesi hayalet gibi yok olur. Temas yüzeyinde deformasyon, sekme ve ikincil parçacık fırlaması üretilmediği için zemin tamamen stabil kalır ve darbenin büyüklüğü görsel olarak kanıtlanamaz.

## 2. Model İç Düzeyi: İvme Mantığı, Sayısal Değerler ve Kinematik Dil

Video difüzyon modellerinin yerçekimi ivmesini tespit etme hiyerarşisi belirli bir semantik öncelik sırasını takip eder. Model, ivme hızını ve düşüş karakteristiğini sırasıyla metindeki hareket fiillerinden, nesneye yüklenen eylemsizlik niteleyicilerinden, ortam adından ("lunar surface") ve görsel arka plan detaylarından türetir. Bu unsurlar arasında çelişki doğduğunda mod geçişleri ve fiziksel bozulmalar kaçınılmaz hale gelir.

Prompt içerisine yazılan nicel fiziksel parametreler (gravity is 0.38g, objects fall at 3.7 m/s², acceleration is 9.81 m/s²) modeller tarafından büyük oranda işlevsiz bırakılır. Video difüzyon modellerinin ön bileşeni olan dil kodlayıcıları (T5-XXL veya CLIP Text Encoder), bu sayısal değerleri latent uzayda karşılığı olan görsel-hareket vektörlerine doğrudan dönüştüremez. Metin kodlayıcı, 3.7 m/s² ifadesini soyut metin token'ları olarak işler; fakat bu token'lar temporal transformer katmanlarındaki kareler arası hız matrislerine yön veremez.

Modeller sayısal ivme tanımları yerine kinematik niteleyiciler ve kuvvet dili ile yönlendirildiğinde fiziksel sadakat dramatik biçimde artar. Modellerin hız ve ivme algısını yönlendiren temel yapılar; terminal velocity, retarded gravitational descent, slow-motion parabolic arc gibi hız ve sürüklenme tanımları ile high structural mass, extreme kinetic momentum, heavy inertia ve high impact resistance gibi kütle ve momentum tanımlarıdır.

Serbest düşüş (a=g, ivmeli hareket) ile süzülüş (v=sabit, ivmesiz veya düşük ivmeli hareket) arasındaki farkı prompt düzeyinde ayrıştırmak için modelin "falling" kelimesini gördüğü an yüksek ivmeli Dünya yerçekimi veri manifolduna sıçrama yaptığı gerçeği dikkate alınmalıdır. Düşüşün düşük yerçekimli bir ortamda ivmelenmeden sabit bir hızla gerçekleşmesi isteniyorsa, prompt "free fall" teriminden tamamen arındırılmalı ve "drag-limited slow vertical drift" veya "constant descent rate along a low-gravity parabolic trajectory" ifadeleriyle kilitlenmelidir.

## 3. Kütle, Çarpışma ve Zemin Etkileşimi Kontrolü

İki katı cisim temas ettiğinde modelin katı cisim penetrasyonu (clipping) yapmasını veya faz geçişli erimeye girmesini engellemek için darbe anının aşamalı bir enerji aktarım dizilimi olarak tanımlanması gerekir. Çarpışmanın bir görsel erime yerine rijit cisim etkileşimi olarak üretilmesi, kronolojik olay dizilimi tekniğiyle sağlanır. Prompt, darbe anını tek bir cümleyle özetlemek yerine sırasıyla yüksek kütleli nesnenin belirli bir vektörde yaklaşmasını (high-mass object approach), nesnenin zemini delmeden sertçe durmasını (impenetrable solid impact without clipping), ardından enerjinin geriye doğru sıçrama veya malzeme bükülmesi şeklinde dışa vurumunu (kinetic recoil, structural crumple with high resistance) dikte etmelidir.

Modeller birincil nesnenin kinetik momentumunu tek başına korumakta zorlanırken, çarpışmanın büyüklüğünü kanıtlayan ikincil fiziksel unsurlar sahnede tanımlandığında fiziksel doğruluk oranı belirgin şekilde yükselir. Temas noktasından fırlayan donmuş regolit tozları, mikro buz kristalleri, şok dalgası halkaları, kırılan yüzey plakaları ve sekme açısı (recoil angle) sahnede tanımlandığında, difüzyon modeli bu ikincil pikselleri oluşturabilmek için birincil nesneyi katı bir yüzeye çarpmaya zorlar. Bu ikincil unsurlar, latent uzayda uzamsal bir sınır koşulu (spatial boundary constraint) işlevi görerek katı cisim geçişini tamamen engeller.

## 4. Havada Asılı Kalma (Hovering) ve Serbest Parçacık Arızaları

Yerçekimli bir ortamda (0.38g veya 1.0g) sıvı damlalarının, toz partiküllerinin veya kopan ekipman parçalarının itkisiz şekilde havada düz çizgiler halinde asılı kalması (causeless floating) ya da tersine yukarı doğru yükselmesi, latent uzayda yönlü yerçekimi alanının türevsel kaybından doğar. Bu serbest parçacık arızalarını önlemek adına sahnede vektörel çökelme kilitleri ve atmosferik sürüklenme tanımları birleştirilmelidir. Sahnede serbest kalan tüm toz, gaz ve sıvı unsurlarının zemin yönlü bir kütleçekim kuvvetine tabi olduğu downward particulate settling ve gravity-bound dust layer terimleriyle belirtilmelidir. Düşük yerçekimli ortamlarda dahi parçacıkların dağılımını kontrol eden atmosferik direnç, parçacıkların yönü "floating in air" yerine "settling toward the terrain under thin atmospheric pressure" şeklinde kilitlenerek tanımlanmalı; böylece modelin sebepsiz havada asılı kalma arızası üretmesi engellenmelidir.

## 5. Model Fizik Sadakati Kıyaslama Değerlendirmesi

Önde gelen video difüzyon modellerinin bilimkurgu sahnelerindeki fiziksel sadakat performansları, yürütülen akademik benchmark ve stres testlerine dayalı olarak önemli farklar sergilemektedir.

Google Veo 3.1, sıvı mekaniği, yerçekimi ivmesi ve katı cisim etkileşimlerinde test edilen modeller arasında en yüksek fiziksel sadakat skorlarından birine sahiptir ve MovieBench fizik testlerinde %75 doğruluk oranına ulaşmaktadır. Kinematik dil komutlarına ve karmaşık kuvvet tanımlarına son derece hassas yanıt veren model, temporal tutarlılığını koruma yeteneğiyle öne çıkar.

Gemini Omni 1.1 Flash, ultra hızlı üretim ve 4K çözünürlük ölçekleme sunmasına karşın, karmaşık eklemli nesne çarpışmalarında ve anlık kütle aktarımlarında zaman zaman uzuv/nesne deformasyonları ve morflama arızaları sergileyebilmektedir.

Kling 3.0 / Kling O3, yüksek hızlı rijit cisim hareketlerinde ve sekme mekaniklerinde güçlü bir performans sergilemektedir. Buna karşın ikincil toz veya parçacık fırlaması tanımlanmadığı senaryolarda kütlesiz temas ve katı cisim geçiş (clipping) hataları yapabilmektedir.

OpenAI Sora 2, görsel kompozisyon ve hikaye anlatımında üstün bir estetik sunmasına rağmen, karmaşık fizik simülasyonlarında ve nesne etkileşimlerinde fiziksel kuralları sıklıkla ihlal etmekte ve MovieBench fizik testlerinde %23 seviyesinde kalmaktadır. D200 "Two Gravities" kırılmasının ve kütlesiz morflama arızalarının en sık gözlemlendiği mimarilerden biridir.

Runway Gen-3 / Gen-4, gelişmiş Motion Brush ve kamera yönlendirme araçlarıyla görsel kontrol sağlasa da, çoklu nesne çarpışmalarında kütlesizlik, erime ve hayaletleşme arızalarına yatkındır.

| Model Mimarisi | Fiziksel Sadakat Skoru (Physics-IQ / MovieBench) | D200 "Two Gravities" Hassasiyeti | Kütlesiz Morflama ve Clipping Eğilimi | Kinematik Prompt İtaati |
|---|---|---|---|---|
| Google Veo 3.1 | Yüksek (%75 Physics Accuracy) | Düşük (Dirençli) | Çok Düşük | Mükemmel |
| Kling 3.0 | Orta-Yüksek | Orta | Düşük (İkincil Etkenlerle) | Yüksek |
| Gemini Omni 1.1 Flash | Orta | Orta | Orta (Eklemli Yapılarda) | Yüksek |
| Runway Gen-3 / Gen-4 | Düşük-Orta (%22.8 Physics-IQ) | Yüksek | Yüksek | Orta-Yüksek |
| OpenAI Sora 2 | Düşük (%23 Physics Accuracy) | Çok Yüksek | Yüksek | Orta |

## 6. Uygulama Standartları ve Sistemik Çözüm Tabloları

Aşağıdaki tablolar, 10 saniyelik fotogerçekçi bilimkurgu filmlerinde fiziksel kırılmaları engellemek amacıyla tekil prompt yapılarında kullanılabilecek formülleri, kinetik tarifleri ve negatif prompt kilitlerini sunmaktadır.

### Tablo 1: YERÇEKİMİ SEVİYESİ PROMPT FORMÜLLERİ

| Rejim | Düşüş Hızı Tanımı (Kinematik) | Adım ve Zıplama Dinamiği | Modelin İtaat Ettiği İngilizce Tam Kalıplar |
|---|---|---|---|
| Mikro-g (0g Vakum / Yörünge) | Sıfır ivmeli, sabit hızlı lineer sürüklenme. Düşme fiili yok. | Zeminden tam kopukluk, kütle eylemsizliğiyle yönlü süzülme, sıfır zemin tepkisi. | Zero-gravity vacuum environment, frictionless inertia, body floating along a linear trajectory at constant velocity, weightless suspension without vertical acceleration, slow momentum rotation. [cite: 5, 19] |
| Mars / Cryo-Yüzey (0.38g) | Düşük ivmeli, retarde düşüş hızı. Geniş ve yavaş parabolik iniş kavisleri. | Yaylanan uzun adımlar, yavaş yükseliş ve gecikmeli zemin çöküşü, düşük darbe şoku. | Low-gravity environment at 0.38g, retarded gravitational acceleration, slow-motion parabolic descent arc, prolonged airborne duration, soft rebound step dynamics, weight-reduced impact velocity. [cite: 5, 17, 19] |
| Dünya / İstasyon İçi (1.0g) | Yüksek ivmeli, dik ve hızlı düşüş. Hızlı ivmelenme ve ani terminal hıza ulaşma. | Rijit ve sıkı zemin teması, anlık ağırlık aktarımı, sıfır uzatılmış hava süresi, sert adım darbesi. | Standard 1.0g earth-equivalent gravity, rapid downward kinetic acceleration, high-velocity vertical descent, firm heavy ground impact, sharp structural mass displacement, immediate gravitational anchorage. [cite: 5, 19] |

### Tablo 2: ÇARPIŞMA VE KÜTLE KİNETİĞİ TABLOSU

| Çarpışma Tipi | Fiziksel Arıza Türü (Morflama / Clipping) | Engelleme Metodolojisi & İkincil Fizik İmzası | Modelin İtaat Ettiği İngilizce Tam Kalıplar |
|---|---|---|---|
| Sert Zemin Çakılması (Astronot / Düşüş) | Astronotun zeminin içine girmesi (clipping) veya kaza anında 1.0g ivmeye sıçraması (Two Gravities). | Temas yüzeyinde penetrasyonu engelleyen rijit bariyer tanımı + zeminden fırlayan donmuş regolit tozu ve şok dalgası. | High-mass suit impact against impenetrable icy regolith terrain, zero surface clipping, kinetic energy dissipating into a high-velocity plume of frozen dust particulates, sharp physical recoil bounce, structural deformation without phase transition. [cite: 5, 19] |
| Nesne Çarpışması (İki Araç / Kızak-Kaya) | Cisimlerin birbirinin içinden hayalet gibi geçmesi (ghosting) veya çarpışma anında eriyerek birleşmesi (morphing). | Kronolojik kinetik aktarım tanımı (Temas -> Bükülme -> Sekme) + fırlayan sert enkaz ve kırılan kaya parçacıkları. | Solid-on-solid high-velocity collision, zero interpenetration, rigid body impact, heavy kinetic momentum transfer forcing an immediate angular rebound, shattering surface debris and flying frost fragments, high structural resistance. [cite: 5, 19] |

### Tablo 3: ÇEVRESEL FİZİK KİLİTLERİ VE NEGATİF PROMPT BLOKLARI

| Fiziksel İhlal Kategorisi | Negatif Prompt Blok Tanımlayıcıları | Kilit Mekanizması & Etiket (ÖLÇÜLMÜŞ / UYGULAMA / ÖNERİ) |
|---|---|---|
| D200 "Two Gravities" & Ani İvme Değişimi | gravity shift, sudden acceleration, rate spike, inconsistent fall speed, earth gravity fall in low-g, rapid drop, trajectory velocity break | Latent uzayda iki farklı yerçekimi veri manifoldunun aynı klip içinde çapraz tetiklenmesini engeller. [ÖLÇÜLMÜŞ] [cite: 3, 5, 28, 29] |
| Kütlesizlik, Clipping & Morflama | clipping, solid passing through solid, phantom object, visual morphing, interpenetration, mass fusion, zero-impact soft crash, liquid metal melting | Katı cisimlerin birbirinin uzamsal koordinatlarını ihlal etmesini ve erime biçiminde faz değiştirmesini engeller. [UYGULAMA] [cite: 4, 5, 30, 31] |
| Sebepsiz Havada Asılı Kalma (Causeless Floating) | causeless floating, hovering particles, anti-gravity drift, ascending dust, suspended liquid droplets, physics defiance, unnatural levitation | Yerçekimli sahnelerde serbest sıvı ve parçacıkların zemin yönlü çökmesini zorunlu kılar, vektör sapmasını önler. [ÖLÇÜLMÜŞ] [cite: 5, 28, 30, 31] |
| Zemin Tepkisizliği & Şok Eksikliği | static ground, zero dust displacement, unbroken ice, motionless dust layer, missing impact recoil, soft landing, frictionless slide | Darbe anında ikincil parçacık ve yüzey deformasyonu üretimini zorunlu kılarak katı zemin temasını doğrular. [ÖNERİ] [cite: 5, 19] |

## 7. Sonuç ve Metodolojik Sentez

Video difüzyon modellerinde fiziksel sadakatin sağlanması, yapay zekaya nicel sayısal denklemler dikte etmekle değil; modelin eğitildiği latent uzaydaki vektörel kuvvet alanlarını doğru kinematik dil, kronolojik eylem dizilimi ve ikincil fiziksel göstergeler ile koşullandırmakla mümkündür.

D200 "Two Gravities" arızası, prompt içerisindeki hareket fiillerinin sahnede tanımlanan ortam yerçekimiyle çelişmesinden kaynaklanmaktadır. Serbest düşüş eylemleri "slow-motion parabolic descent arc" gibi kelimelerle sabitlendiğinde ve negatif prompt bloklarıyla ivme kırılmaları kilitlendiğinde, 10 saniyelik bilimkurgu sahnelerinde fiziksel tutarlılık eksiksiz biçimde korunabilmektedir. Ayrıca çarpışma sahnelerinde ikincil fiziksel detayların (donmuş toz fırlaması, şok halkaları, sekme açıları) kullanılması, modelin temas yüzeylerini geçirgen olmayan katı rijit bariyerler olarak işlemesini garanti altına almaktadır.
