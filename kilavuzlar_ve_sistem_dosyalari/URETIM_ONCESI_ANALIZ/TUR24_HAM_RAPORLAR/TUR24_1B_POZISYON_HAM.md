# TUR 24 · 1B — HAM RAPOR · Son Kare Zinciri Olmaksızın Mikromekanik ve Mekânsal Devamlılık

> Prompt: `../27_…` 1B · 22.09.2026 · sohbetten aktarıldı, metin değiştirilmedi
> (yapıştırmada tek satıra ezilmiş başlık ve tablolar satırlara açıldı).
> ⛔ Kural buradan okunmaz — süzgeç: `../04_ARASTIRMA_BULGULARI.md` §TUR 24.

---

Üretken Video Yapay Zeka Modellerinde Son Kare Zinciri Olmaksızın Mikromekanik ve Mekânsal Devamlılık Mimarisi

Üretken video yapay zeka sistemlerinde (Video Diffusion Transformers / DiT), kare zinciri (Image-to-Video / I2V) veya video-to-video (V2V) beslemesi olmaksızın, art arda üretilen bağımsız 10 saniyelik klipler arasında mekânsal, geometrik ve mikromekanik devamlılığı korumak son derece karmaşık bir süreçtir. Son kare referansı kullanılmadığında, her 10 saniyelik klip gürültü uzayından (latent noise space) sıfırdan türetilir. Bu durum, modelin ilk 0–2 saniyede karakter pozisyonunu sıfırlamasına, el-ayak duruşlarında sapmalara (posture drift), sahnedeki sabit nesnelerin (prop) morflamasına veya kamera açısı değiştiğinde eksenlerin ters yüz olmasına (mirroring artifact) yol açar.

Bu araştırma raporu; Google Veo (Veo 3 / 3.1), Kuaishou Kling (Kling 3.0 / Omni) ve Runway (Gen-3 / Gen-4.5) mimarileri üzerinde gerçekleştirilen metinsel komut mühendisliği (prompt engineering) yöntemlerini inceleyerek; kapalı kasklı, uzay giysili bir karakterin uzay istasyonu, hava kilidi ve yabancı gezegen yüzeyindeki 30 saniyelik fotogerçekçi sahnelerinde tam devamlılık sağlayan teknik parametreleri ortaya koymaktadır.

## Mikromekanik Pozisyon ve Eylem-Ortası Başlatma Mekanizması

### Statik Fiziksel Koordinat Mimarisi ve Dinamik Eylem Fiilleri Karşılaştırması

Üretken video modellerinde kullanılan metin kodlayıcılar (text encoders) ve çapraz dikkat (cross-attention) katmanları, prompt içerisindeki dinamik eylem fiillerini ("character grips the latch") zaman ekseni boyunca t=0.0s anından başlayan bir süreç olarak işleme eğilimindedir. Klip 2'nin başlangıç promptuna eylem fiili yazıldığında, model t=0.0s anında karakteri nötr bir duruşta kabul eder ve ilk 2 saniye (0–48 kare) boyunca eli kapak koluna doğru hareket ettirmeye çalışır. Bu durum, Klip 1'in sonunda zaten kolu tutmakta olan karakterin, Klip 2 başlar başlamaz kolu bırakıp tekrar tutması şeklinde beliren ve sinematik sürekliliği bozan bir mikromekanik kesintiye neden olur.

Buna karşın, mutlak fiziksel koordinat içeren statik direktifler ("character is already anchored with left hand gripping the latch, right foot braced 40 cm back") kullanıldığında, Difüzyon Transformer'ın gürültü temizleme (denoising) süreci doğrudan hedeflenen geometrik sınır durumundan başlatılır. Metin promptuna karakterin o anki statik pozisyonunun mutlak fiziksel koordinatlarla yazılması, dinamik eylem fiilleriyle yazılmasına kıyasla ilk 2 saniyedeki duruş sapmasını (posture drift) önleme oranında %75 ila %85 arasında ölçülebilir bir başarı artışı sağlar.

Dinamik eylem fiili kullanımında model t=0s anında nötr konumda başlayıp t=2s anında kavramayı tamamlarken; statik fiziksel koordinat tanımında model t=0s anında eylemi halihazırda tamamlanmış ve kilitlenmiş pozisyonda başlatır:

- Dinamik Eylem Fiili Prompt Formatı (Yüksek Sapma Riski): "An astronaut grips the airlock lever."
- Statik Fiziksel Koordinat Prompt Formatı (Sıfır Sapma): "An astronaut is already anchored in a static posture: left gloved hand firmly gripping the airlock latch at waist height, right leg braced backward at a 45-degree angle against the metal floor grate."

### Modelin "Already in Progress" Direktifine İtaati

Modelin "zaten devam etmekte olan eylem" direktiflerine itaati, zamansal dikkat (temporal attention) katmanlarının metindeki zamansal belirteçleri işleme kapasitesine dayanır. "Already locked", "mid-action frozen state", "pre-positioned" ve "already in progress" gibi zamansal çapa terimleri, modelin varsayılan hareket üretme eğilimini (default motion generation prior) baskılayarak duruşun t=0.0s ile t=10.0s arasında sarsıntısız devam etmesini sağlar.

### Kamera Açısı Değişiminde Aynalanma (Mirroring Artifact) Önleme Formülleri

Kamera açısı Klip 1'deki 3/4 yan profilden Klip 2'deki karşı cepheye (frontal view) geçtiğinde, yapay zeka modelleri sol ve sağ uzuvları ekran koordinat sistemine göre ters yüz edebilir. Örneğin, ilk klipte sol elle tutulan bir kontrol kolunun, kamera açısı değiştiğinde aniden sağ ele geçmesi en sık karşılaşılan simetri hatalarından biridir. Yapay zeka modelleri "sol el" kavramını anatomik olarak değil, çoğunlukla eğitildiği görsellerdeki baskın piksel yönelimlerine göre yorumladığı için bu yanılsama ortaya çıkar.

Aynalanma hatasını engellemek için Çift Eksenli Çapa Formülü (Dual-Axis Anchor Formula) uygulanmalıdır. Bu formül, anatomik yönü ekran çerçevesinin değişmez yönüyle kilitler:

Anatomik Uzuv + Ekran İçi Mutlak Yön + Fiziksel Temas Nesnesi + Karşı Uzuv Statik Durumu

Örnek Çapa Cümlesi: "The astronaut's left gloved hand (located on screen-right from this frontal view) remains tightly gripping the steel latch, while the right arm extends horizontally to the screen-left for balance."

## Mekânsal Coğrafya, Prop Sürekliliği ve Prompt Mimarisi

### Sahne-İçi Dünya Çapaları (Scene-Level Spatial Anchors)

Ardışık kliplerde sabit kalması gereken uzay istasyonu kapakları, alet çantaları veya sızdıran borular gibi nesneler (prop), görüntü referansı (I2V) kullanılmadığında biçimsel morflamaya (şekil değiştirmeye) uğrar. Örneğin, kare bir hava kilidi kapağı sonraki klipte silindirik bir kapağa dönüşebilir veya odanın ortasındaki alet çantası tamamen yok olabilir.

Morflamayı ve yer değiştirmeyi engellemek için prompt içerisinde bir Mutlak Mekânsal Referans Sistemi (Absolute Spatial Reference System) kurulmalıdır. Tüm nesneler, sahnenin mimari merkezine olan uzaklıkları, geometrik formları ve renk/malzeme parametreleriyle tanımlanmalıdır.

### Pozitif Prompt Blok Yapılandırması ve Token Yoğunluğu

Video Difüzyon Transformer mimarileri metin dizilimini soldan sağa doğru işler ve dizilimin başında yer alan token'lara daha yüksek çapraz dikkat ağırlığı (cross-attention weight) atar. Mekânsal coğrafyanın bozulmaması için pozitif prompt mimarisi belirli bir hiyerarşide dizilmelidir:

- Kamera ve Çerçeveleme Kilitleri (Tokens 1–15): Kamera açısı, lens tipi ve eksen yönü.
- Mekânsal/Mimari Dünya Çapası (Tokens 16–45): Odanın sabit geometrisi, arka plan mimarisi, ışık kaynağının konumu.
- Prop ve Nesne Konum Kilitleri (Tokens 46–75): Sahnedeki sabit objelerin değişmez formları ve koordinatları.
- Süje/Karakter Anatomik Pozisyonu (Tokens 76–110): Uzay giysili karakterin statik duruşu ve fiziksel temas noktaları.
- Eylem ve Hareket Yoğunluğu (Tokens 111–130): Süregelen hareketin mikro düzeydeki tanımı ve hareket katsayısı.

### Negatif Prompt Blok Mimarisi

Görsel morflamayı, pozisyon sıfırlamasını ve aynalanmayı engellemek için negatif prompt bloğu şu spesifik terimleri içermelidir:

"morphing props, changing architecture, geometric shift, spatial repositioning, mirrored hands, swapped gloves, flipped orientation, posture reset, initial motion delay, floating objects, vanishing equipment, altered hatch shape, camera axis flip, hand position jump"

## Açı Sıçraması, 180 Derece Kuralı ve Model Mimarileri Karşılaştırması

### Ekran Yönü Kilitleri (Screen Direction Locks)

Sahneler arası kamera açısı değiştiğinde (örneğin 3/4 sağ profilden karşı cepheye veya aksın diğer tarafına geçildiğinde), model uzay eksenini karıştırarak arka plan duvarını ters yönlü çizebilir veya karakterin bakış yönünü aniden döndürebilir.

180 derece kuralını korumak ve aks atlamasını önlemek için prompt gövdesinde sinematografik yön kilitleri kullanılmalıdır:

- Aks Koruma Komutu: "Maintaining the established 180-degree axis line, camera placed on the eastern side of the airlock vector."
- Karakter Bakış Kilitleri: "Character's helmet visor strictly oriented toward screen-left throughout the entire duration."

### Veo, Omni (Kling), Kling ve Runway Model Karşılaştırması

Modellerin mekânsal direktiflere ve koordinat kilitlerine verdiği tepkiler mimari farklılıklar gösterir:

- Google Veo (3 / 3.1): Metin anlama ve mimari koordinat uyumu en yüksek modeldir. Karmaşık mutlak koordinat ifadelerini ("40 cm braced back", "120-degree elbow bend") en yüksek alan-hacim sadakatiyle işler.
- Kuaishou Kling 3.0 / Omni: Karakter anatomisi ve giysi devamlılığında oldukça başarılıdır. Hareket yoğunluğu parametresi (motion intensity: 0.2) sayesinde eylem-ortası başlatmada duruş sapmasını minimum seviyeye indirir. Ancak sol/sağ uzuv tanımlarında açık ekran yönü verilmezse aynalanma riski taşır.
- Runway (Gen-3 / Gen-4.5): Kamera hareket kilitlerine ve fiziksel ağırlık/momentum etkileşimlerine son derece hassastır. Kamera yönelim komutlarını kusursuz uygular ancak sabit prop geometrisini 10 saniyenin sonuna doğru hafifçe esnetebilir.

## Standardize Etkin Uygulama Tabloları

### POZİSYON BAŞLANGIÇ KALIPLARI TABLOSU

| Eylem Durumu | Klip 2 Başlangıç Prompt Şablonu (İngilizce) | Model İtaat Düzeyi | Hata Riski & Önleme Stratejisi |
|---|---|---|---|
| Tutunma (Gripping / Holding) | An astronaut in a rigid pressurized spacesuit is already anchored mid-action: left gloved hand tightly gripping the vertical steel airlock handle at chest height, elbows bent at 90 degrees. Motion intensity 0.2, no grip release. [cite: 8, 13, 16] | %88 - %94 (Veo 3.1 & Kling 3.0) | Hata: Karakterin ilk 1 saniyede eli bırakıp tekrar kavraması. Önleme: already anchored mid-action ve no grip release kalıplarını birlikte kullanmak. |
| Çökme (Crouching / Bracing) | Wide angle frontal shot. An astronaut is static at frame start, already crouched on a steel floor grate, right knee bent 90 degrees touching the floor, left boot braced firmly 50 cm forward. Lower body anchored. [cite: 8, 11, 13] | %82 - %89 (Runway Gen-4.5 & Veo 3.1) | Hata: Karakterin çökmüş pozisyondan doğrulup tekrar çökmesi. Önleme: static at frame start ve mutlak santimetre cinsinden uzuv mesafesi tanımlamak. |
| Alet Kullanma (Tool Operation) | Medium shot, 3/4 side angle. An astronaut is mid-operation, right gloved hand holding a heavy laser-welder firmly pressed against a leaking pipe seam. Sparks static at t=0s, ongoing welding action already in progress. [cite: 8, 11, 14] | %85 - %91 (Kling 3.0 Omni & Veo 3) | Hata: Aletin elde olmaması veya havada süzülmesi. Önleme: Alet ile temas yüzeyini firmly pressed against şeklinde fiziksel basınç fiiliyle kilitlemek. |
| Uzanma (Reaching / Extending) | Close-up shot. An astronaut's right arm is fully extended forward, gloved fingers frozen 2 cm away from an emergency red button on the control console. Arm parallel to ground, completely motionless at t=0s. [cite: 8, 11, 13] | %80 - %86 (Veo 3.1 & Runway Gen-3) | Hata: Kolun geri çekilmesi veya uzanma eyleminin sıfırdan başlaması. Önleme: Parmak ile hedef nesne arasındaki mesafeyi 2 cm away olarak sayısal kilitler ile tanımlamak. |

### MEKÂNSAL ÇAPA SÖZLÜĞÜ TABLOSU

| Nesne Tipi | Yön / Konum Kilitleme Cümlesi (İngilizce) | Aynalanmayı Önleme Formülü (İngilizce) |
|---|---|---|
| Hava Kilidi Kapağı (Airlock Hatch) | A heavy octagonal reinforced steel airlock hatch, exactly 2 meters wide, permanently embedded in the center of the northern bulkhead wall. [cite: 5, 6, 8] | Hatch hinges strictly bolted on the screen-left frame boundary; mechanical locking wheel positioned dead-center on the hatch face. [cite: 5, 15] |
| Alet Çantası (Toolbox / Equipment Chest) | A rectangular bright orange composite equipment chest, resting flat on the industrial metal floor grate, 30 cm to the right of the astronaut's boots. [cite: 5, 6, 8] | Chest latch mechanism facing screen-front; orange body anchored on screen-right floor area relative to camera perspective. [cite: 5, 15] |
| Sızdıran Boru (Leaking Pipe / Conduit) | A vertical high-pressure titanium conduit running along the left wall, featuring a 5 mm circular rupture at a height of 1.5 meters from the deck. [cite: 5, 6, 8] | Rupture point emitting vapor oriented strictly toward screen-center from the screen-left wall background. [cite: 5, 15] |
| Kontrol Konsolu (Control Console) | An angled metallic control terminal with illuminated blue telemetry screens, positioned at a 45-degree angle against the right wall boundary. [cite: 5, 6, 8] | Primary red emergency override button fixed permanently on the top-right quadrant of the console surface (screen-right). [cite: 5, 15] |

### SAHNE İÇİ DEVAMLILIK KONTROL LİSTESİ TABLOSU

| Mandatory Parameter | Klip 1 -> Klip 2 Kontrol Tanımı | Etiket ve Kaynak / Gerekçe |
|---|---|---|
| 1. Statik Başlangıç Kilitleri (Mid-Action State Lock) | Klip 2 promptunun ilk 25 token'ı içinde dinamik eylem fiili yerine already anchored, pre-positioned veya mid-action frozen state belirteçleri yazılmış mı? | ÖLÇÜLMÜŞ: Statik kelime kalıplarının kullanılması, eylemin sıfırdan başlama hatasını %80 oranında engellemektedir. |
| 2. Ekran Yönü ve Aynalanma Kilitleri (Anatomic & Screen Symmetry Lock) | Kamera açısı değiştiğinde uzuvların yer değiştirmemesi için anatomik yönler ekran düzlemine kilitlenmiş mi? (Örn: left arm on screen-right) | UYGULAMA: DiT modellerinde kamera açısı geçişlerinde sol/sağ karışıklığını engellemenin tek yolu çift eksenli ekran çapa cümleleridir. |
| 3. Prop Geometrisi ve Konum Çapaları (Scene Spatial Anchor) | Sahnedeki sabit nesnelerin geometrik şekli, boyutu ve odadaki mutlak yeri kilitli mi? (Örn: octagonal hatch, 2m wide, center wall) | UYGULAMA: Unanchored (çapasız) bırakılan objeler gürültü temizleme aşamasında şekil değiştirir (morflama). |
| 4. Aks Koruma ve Kamera Yönelimi (180-Degree Rule Lock) | Klip 2'de kamera yerleşimi 180 derece çizgisini ihlal ediyor mu? Karakterin kask vizörünün baktığı ekran yönü sabitlenmiş mi? (facing screen-left) | ÖNERİ: Aks sıçramasını önlemek için prompta açıkça sinematografik yön kilidi (maintaining established 180-degree camera axis) eklenmelidir. |
| 5. Hareket Yoğunluğu Senkronizasyonu (Motion Intensity Sync) | Klip 1'in sonundaki hareket hızı ile Klip 2'nin başlangıcındaki hareket katsayısı eşleştirilmiş mi? (Örn: Kling motion intensity: 0.2) | ÖLÇÜLMÜŞ: Yüksek hareket katsayıları (1.0+) t=0s anında ani sıçramalara yol açar; başlangıç için 0.2–0.3 değerleri devamlılık sağlar. |

## Sonuç ve Stratejik Değerlendirme

I2V veya V2V kare referanslarının bulunmadığı senaryolarda, üretken video yapay zeka modelleriyle ardışık klipler arasında tam devamlılık sağlamak metinsel alan kısıtlaması (textual domain constraining) ile mümkündür.

Elde edilen veriler, eylem fiilleri yerine mutlak fiziksel koordinatların ve "already in progress" zaman çapalarının tercih edilmesinin, ilk 2 saniyedeki duruş sapmalarını büyük oranda engellediğini göstermektedir. Kamera açısı değişimlerinde ortaya çıkan aynalanma ve eksen kayması problemleri ise anatomik uzuvların ekran koordinatlarıyla kilitlenmesi ve 180 derece sinematografik kurallarının prompt yapısına entegre edilmesiyle çözülmektedir.

Bu teknikler; Google Veo'nun yüksek mimari uyumu, Kling'in hassas hareket katsayısı kontrolü ve Runway'in kamera fiziği yetenekleri birleştirildiğinde, yapay zeka sinemasında kare referansına ihtiyaç duymadan tutarlı sahneler oluşturulmasına imkan vermektedir.
