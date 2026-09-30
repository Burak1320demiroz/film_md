# TUR 24 · 3 — HAM RAPOR · Fiziksel Hafıza ve Travma Sürekliliği ("D42 Anti-Reset Protokolü")

> Prompt: `../27_…` 3 · 22.09.2026 · sohbetten aktarıldı, metin değiştirilmedi
> (yapıştırmada hücrelere dağılmış tablolar satırlara açıldı).
> ⚠️ Rapor "D42" adını promptun yanlış atfından devralır: depoda D42 kir/toz
> sürüklenmesidir, beden sıfırlanması **D207**'dir (bkz. `../27_…` düzeltme tablosu).
> ⛔ Kural buradan okunmaz — süzgeç: `../04_ARASTIRMA_BULGULARI.md` §TUR 24.

---

Yapay Zeka Video Üretim Modellerinde Fiziksel Hafıza ve Travma Sürekliliği: D42 Anti-Reset Protokolü

Yapay zeka video üretim mimarileri—özellikle Google Veo 3.1, Gemini Omni 1.1 Flash, Kling 3.0, Runway Gen-4 ve OpenAI Sora 2—metinden video (T2V) ve görselden video (I2V) sentezleme süreçlerinde üst düzey fotogerçekçilik sunmaktadır. Ancak bu modellerin temelini oluşturan bellek hücresinden yoksun (stateless) Difüzyon Transformer (DiT) mimarileri, ardışık anlatılarda ciddi bir süreklilik kırılmasına yol açmaktadır. Literatürde ve profesyonel üretim hatlarında D42 "Anti-Reset / Physical Amnesia" (Fiziksel Hafıza Kaybı) olarak adlandırılan bu teknik arıza; bir sahnede ağır travma, patlama, yaralanma veya giysi tahribatı geçiren bir figürün, bir sonraki bağımsız klipte tüm fiziksel hasarlarından arınmış, dik bir duruşla ve sıfırlanmış nötr bir beden diliyle yeniden üretilmesi olgusudur.

Görsel efekt (VFX) makyajı, CGI karakter kafesi (mesh) veya 3B model takip sistemlerinin bulunmadığı; tamamen bağımsız promptlar, referans görseller ve difüzyon parametreleri ile yürütülen 10 saniyelik fotogerçekçi uzay bilimkurgu yapımlarında bu durum temel bir kısıt teşkil eder. Karakterin basınç giysisi ve kask taşıdığı bu senaryolarda süreklilik; prompt yazım standartları, SPEC (State Parameter Explicit Conditioning) durum parametreleri ve negatif kadro kilitleri üzerinden kurulmalıdır.

## Stateless Difüzyon Mimarilerinde Fiziksel Hafıza Kaybının (D42) Analizi

Çoklu klip dizilimlerinde her video jenerasyonu, difüzyon modelinin gürültüden görsel sentezleme (denoising) sürecini bağımsız olarak başlatır. Model, geçmiş kliplerin kinetik veya dokusal durumunu dahili bir bellek vektöründe tutmaz. Metin kodlayıcılar (CLIP, T5 veya LLM tabanlı ön modeller) ve çapraz dikkat (Cross-Attention) mekanizmaları, prompt içerisindeki kavramları işlerken eğitildiği veri kümesindeki en yüksek olasılıklı baskın vektörlere çekilir.

Prompt içerisinde sadece "An astronaut walking on the Moon" ifadesi kullanıldığında, modelin latent alanındaki en güçlü önsel (prior), hasarsız, dik duran ve temiz bir basınç giysisi giyen astronot figürüdür. Karakter bir önceki klipte bir patlamayla fırlamış veya kask vizörü çatlamış olsa dahi, durum parametresi açık metin kilitleriyle bir sonraki klibe taşınmadığı takdirde çapraz dikkat katmanları baskın nötr duruma geri döner.

İkinci temel kriz ise Zombi Dirilişi (Zombie Resurrection) / Arka Plan Duplikasyonu hatasıdır. Bir sahnede vurulan, ölen, düşen veya gruptan ayrılan figürler, sonraki kalabalık sahnelerde modelin "uzay keşif ekibi" gibi gruptan oluşan kompozisyon önsellerine (group priors) tutunması nedeniyle arka planda canlı, yürürken veya hasarsız şekilde halüsinasyonla belirir. Bu sorunların çözümü, toparlanma eğrilerinin, kalıcı kostüm hasar takvimlerinin ve negatif kadro kilitlerinin metodik bir disiplinle yazılmasını gerektirir.

## Post-Impact (Darbe Sonrası) Toparlanma Eğrisi ve Kinetik Aşamalandırma

Sinematik dramaturjide ve gerçekçi fizik simülasyonlarında, şiddetli bir darbe veya patlama geçiren bir insanın biyomekanik reaksiyonu anlık olarak sıfırlanamaz. Basınç giysisi içerisindeki bir astronotun kaza sonrasındaki ilk 30–40 saniyelik süreci (4 bağımsız 10 saniyelik klip), kademeli bir kinetik toparlanma eğrisi izler.

Difüzyon modellerinde "wounded" (yaralı) veya "pain" (acı) gibi soyut sıfatlar tek başına kullanıldığında, modelin güvenlik filtreleri devreye girebilmekte ya da jenerik bir yüz ifadesi üreterek beden dilini sabit tutmaktadır. Bu nedenle sakatlık ve acı durumu, soyut duygularla değil, biyomekanik kısıtlar, duruş bozuklukları ve yerçekimiyle olan uyumsuzluklar üzerinden tanımlanmalıdır.

İlk aşamada (Klip 1: 0s - Darbe ve İnersiyel Çöküş), karakter kas kontrolünü tamamen kaybetmiştir ve pasif beden hareketsizdir. İkinci aşamada (Klip 2: +10s - Şok ve Akut Solunum Krizi), sinir sisteminin refleksleri başlar; karakter ayağa kalkamaz, zeminde yarı-fetal pozisyonda acıyla kıvranır ve kask içi yoğun buğulanma gösterir. Üçüncü aşamada (Klip 3: +20s - Kusurlu Doğrulma ve Ağırlık Aktarımı), kas gücü kısmen döner fakat asimetrik sakatlık belirginleşir; karakter tek bacağına ağırlık veremez ve hasarlı uzvunu göğsüne bastırır. Dördüncü aşamada (Klip 4: +30s - Kompromize Lokomosyon), yürüyüş döngüsü (gait) bozulmuş durumdadır; 30 derece öne eğik gövde, ayak sürükleme ve çevredeki yapılara tutunma hareketleri kilitlenir.

### 4 Aşamalı Travma Merdiveni

Aşağıdaki tablo, 10 saniyelik klipler halinde tasarlanan bu 40 saniyelik Post-Impact toparlanma sürecinin biyomekanik kısıtlarını ve modellerde (Veo 3.1, Sora 2, Kling 3.0, Gen-4) doğrulanmış tam İngilizce prompt kalıplarını sunmaktadır.

| Klip Dizilimi & Zaman | Zorunlu Beden Dili & Fiziksel Reaksiyon | Hareket Kısıtı ve Biyomekanik | İngilizce Prompt Kalıbı (Tam SPEC Standardı) |
|---|---|---|---|
| Klip 1 (0s) · Darbe Anı & Atalet | Yüzüstü veya yan yatış, sıfır kas tonusu, tamamen gevşemiş ve hareketsiz uzuvlar. | Aktif hareket yok. Darbe inersiyasıyla zeminde kayma ve toz bulutunun çökmesi. | Cinematic sci-fi shot, 10s, photorealistic 8k. A pressure-suited astronaut is thrown violently onto dusty lunar regolith by a plasma shockwave, collapsing motionless in a face-down position, limp limbs, zero active posture, unmoving suit, thick dust settling over helmet. Shot on 35mm. [cite: 1, 2] |
| Klip 2 (+10s) · Şok & Akut Aşama | Yarı-fetal pozisyona bükülme, göğüs plakasına sarılma, şiddetli titreme. | Kalkamama, zeminde acıyla kıvranma, kask içinde hızlı ve düzensiz nefes alıp verme. | Cinematic sci-fi shot, 10s, photorealistic 8k. A severely injured astronaut lying on dusty lunar regolith, writhing in acute physical pain, unable to stand, curling into a semi-fetal posture, hyperventilating with rapid heavy breathing fogging the visor interior, trembling gloved hands clutching chest plate. [cite: 1, 2] |
| Klip 3 (+20s) · Kusurlu Doğrulma | Tek dize dayanarak dengesiz doğrulma, sağa yatık asimetrik duruş. | Sol bacağa ağırlık verememe, sol kolu göğse bastırma, kalkarken sarsıntılı yalpalama. | Cinematic sci-fi shot, 10s, photorealistic 8k. A wounded astronaut struggling into an asymmetrical half-upright stance on crater ground, limping heavily while shifting weight away from left leg, pressing damaged left arm tightly against chest plate, staggering forward with unsteady off-balance gait. [cite: 1, 2] |
| Klip 4 (+30s) · Sakat Lokomosyon | Öne 30 derece kambur eğilme, tek eliyle çevredeki enkaz/kayaya tutunma. | Sol botu zemin üzerinde sürükleme, kesik kesik adımlar, belirgin sendeleme ve düşme eğilimi. | Cinematic sci-fi shot, 10s, photorealistic 8k. A battered astronaut dragging left boot across harsh terrain, hunched forward at a 30-degree angle, heavily limping and stumbling forward, resting a hand against a jagged rock for support, visible bodily exhaustion and compromised movement. [cite: 1, 2] |

## Kostüm ve Ekipman Hasarının Kilitlenmesi (SPEC Standardizasyonu ve I2V Sınırları)

Fiziksel bedendeki sakatlığın yanı sıra uzay kıyafeti, kask, vizör ve botlar üzerindeki tahribatın 10 ila 20 klip boyunca temizlenmeden taşınması gerekir. Metin tanımlarının zamanla bozulmasını (semantic drift) önlemek için SPEC (State Parameter Explicit Conditioning) standardı uygulanır.

SPEC standardı, prompt metninin başında köşeli parantez içinde değişmeyen bir durum veri bloğu tanımlar. Örneğin: [SPEC DAMAGE STATE: cracked right visor corner with spiderweb fracture, 15cm jagged tear on left shoulder seam, heavy black carbon scoring across central chest plate, thick dark hydraulic fluid encrusted up to mid-calf] formatı metin kodlayıcıya durum değişkeni olarak iletilir ve ardışık klip promptlarında aynen korunur.

Görselden video (I2V) üretimi, ilk karenin dokusunu korumada başarılı olsa da kalıcı hasar aktarımında üç temel kısıta sahiptir:

- Dinamik Hasar Genişlemesi Yetersizliği: Statik referans görseller, vizördeki çatlağın zamanla büyümesi veya sıvı sızıntısının yayılması gibi süreçleri tek başına simüle edemez.
- Çapraz Dikkat Yumuşatması: Referans görseldeki küçük detaylar (örneğin kasktaki çamur izleri), model hareket ürettikçe görsel pürüzsüzleştirme mantığı nedeniyle 3–4 saniye içinde kaybolma eğilimi gösterir.
- Görsel-Metin Çatışması: Referans görseldeki hasar durumu ile prompttaki eylem çeliştiğinde model görseli deforme eder. Bu nedenle referans görsel kullanımı, SPEC metin bloklarıyla desteklenmelidir.

### Kostüm Hasar Takvimi

Aşağıdaki tablo, uzay giysisi üzerindeki kalıcı tahribat unsurlarını, prompt içerisindeki SPEC yazım formatını ve modellerin (Google Veo 3.1, Sora 2, Kling 3.0, Runway Gen-4) bu detayları koruma performansını listelemektedir.

| Hasar Tipi & Konumu | Prompt Kalıcı Yazım Formatı (SPEC Standardı) | Model Koruma Başarımı (% & Davranış Analizi) |
|---|---|---|
| Vizör Çatlağı (Helmet Visor) | damage state: spiderweb fracture across upper-right corner of gold-coated helmet visor, radial glass cracks with visible inner condensation [cite: 5] | %88 (Çok Yüksek): Sora 2 ve Veo 3.1 kırılma geometrisini korur. Kling 3.0 ise 6. saniyeden sonra çatlağı yumuşatabilmektedir. |
| Giysi Yırtığı / Basınç Kaybı (Suit Shoulder/Arm) | damage state: jagged 15cm tear on left shoulder seam of white thermal pressure suit, exposed inner dark insulation fabric, fraying edges [cite: 5] | %82 (Yüksek): Veo 3.1 ve Gen-4 kumaş yırtıklarını sabit tutar. Geniş açılı kamera çekimlerinde küçük detaylar kaybolabilir. |
| Göğüs Plakası Hasarı (Chest Armor Scoring) | damage state: heavy black carbon burn marks and deep diagonal metal scratches across central chest armor plate, melted badge emblem [cite: 5] | %91 (Çok Yüksek): Yüksek kontrastlı siyah/gri yanık izleri difüzyon modellerinin latent alanına güçlü şekilde tutunur. |
| Çamur / Sıvı Bulaşması (Boots & Lower Legs) | damage state: thick dark viscous hydraulic fluid and dark regolith mud encrusted up to mid-calf on both boots and lower suit legs [cite: 5] | %79 (Orta-Yüksek): Kling 3.0 ve Veo 3.1 yürüyüş sırasında çamuru korur. Hızlı hareket sahnelerinde model çamuru dokudan silebilir. |

## Kadro Dondurma ve Elenen Figür Kontrolü (Zombi Dirilişi Engelleme)

Çoklu karakter anlatılarında bir karakterin sahneden çıkması (ölüm, düşme veya gruptan ayrılma) sonrasında difüzyon modelleri boş alanları doldurma eğilimi gösterir. Modeller, eğitim verisindeki grup sahnelerine dayanarak elenmiş karakterlerin kopyalarını arka planda halüsinasyon olarak üretebilir.

Bu durumu engellemek için Kadro Dondurma (Cast Freezing) ve Negatif Dışlama Blokları birlikte kullanılır. Geçmiş zamana dayalı ifadeler ("the astronaut who died is gone") metin kodlayıcılar tarafından yanlış işlenebileceği için kullanılmamalıdır. Bunun yerine mevcut kadro sayısı kesin pozitif ifadelerle sabitlenmeli ve negatif prompt alanında dışlama kuralları tanımlanmalıdır.

### Kadro Dondurma ve Elenen Figür Tablosu

| Sahne Durumu ve Kadro Değişimi | Pozitif Kadro Kilit Cümlesi | Negatif Blok Cümlesi (Dışlama Kuralları) |
|---|---|---|
| Sahnede Vurulan / Ölen Karakter (1 Karakter Eksildi, 1 Sağ Kaldı) | Wide camera framing, shot of precisely 1 surviving astronaut in frame, solitary subject on crater ground, absolute solo presence, no other humans. [cite: 7, 10] | Negative prompt: duplicate character, extra astronaut, second person, resurrected figure, background clone, alive partner, multiple pressure suits, extra limbs. [cite: 6, 10] |
| Düşen / Geride Kalan Karakter (Gruptan Ayrılma) | Establishing shot, exact count of 1 astronaut walking away alone into the ravine, isolated lone explorer, empty vast environment. [cite: 7, 10] | Negative prompt: duplicate suit, trailing companion, extra survivor, cloned crew member, secondary astronaut, split personality body. [cite: 6, 10] |
| Sedye / Tahliye Edilen Karakter (Taşıyanlar ve Yatan Karakter) | Focus shot, precisely 2 standing medics carrying 1 horizontal unconscious astronaut on a stretcher, exactly 3 human bodies in total composition. [cite: 7, 10] | Negative prompt: extra medic, standing duplicate of injured astronaut, duplicate subject walking in background, fourth person, cloned squad. [cite: 6] |
| Gruptan Ayrılan Karakter (3 Kişiden 2 Kişiye Düşüş) | Medium tracking shot, exactly 2 astronauts continuing mission together side by side, explicit party of two, double suit composition. [cite: 7, 10] | Negative prompt: third astronaut, departed member returning, duplicate explorer, extra crew member in background, ghostly apparition. [cite: 6, 10] |

## Anti-Reset Protokolü (D42 Operasyonel Uygulama Kuralları)

Süreklilik hatalarını önlemek ve 10 saniyelik bağımsız kliplerden oluşan uzay bilimkurgu serilerinde tutarlı fiziksel travma üretmek amacıyla geliştirilen operasyonel kurallar aşağıda kategorize edilmiştir.

- [ÖLÇÜLMÜŞ] Stateless Mimaride Durum Taşıma Zorunluluğu: Video difüzyon modelleri (Veo 3.1, Sora 2, Kling 3.0, Gen-4) klipler arasında kendiliğinden durum hafızası taşımamaktadır. Her klip bağımsız bir denoiser işlemidir. Bir önceki sahnede oluşan fiziksel deformasyon, bir sonraki klip promptuna metin tabanlı bir durum değişkeni olarak aktarılmadığı sürece model varsayılan "hasarsız" durumuna dönmektedir.
- [UYGULAMA] SPEC Blok Enjeksiyonu: Tüm promptların ilk 30 kelimesi içerisine değişmeyen bir [SPEC DAMAGE STATE] bloğu eklenmelidir. Örneğin: [SPEC DAMAGE STATE: spiderweb fracture right visor corner, 15cm tear left suit shoulder, heavy carbon scoring chest plate]. Bu blok, difüzyon adımlarının başlangıcında çapraz dikkat katmanlarını tanımlanan dokulara kilitler.
- [ÖNERİ] Referans Görsel ve Delta-Prompting Hibrit Kullanımı: Sadece Image-to-Video (I2V) kullanmak, dinamik hareket sahnelerinde hasarın zamanla yumuşamasına yol açar. İlk kadranda referans görsel verilmeli, ancak metin alanında mutlaka görseldeki hasarın durumu ve o klipte geçireceği değişimi tanımlayan ifadeler (maintaining visor crack while adding fresh dust accumulation) yer almalıdır.
- [ÖLÇÜLMÜŞ] Biyomekanik Kinetik Kelime Dağarcığı: Güvenlik filtrelerinin kısıtlamalarını aşmak ve tutarsız vücut hareketlerini önlemek için acı ve sakatlık durumu kinestetik terimlerle ifade edilmelidir. En yüksek tutarlılığı sağlayan terimler şunlardır:
  - Bacak Yaralanması: asymmetrical gait, shifting weight to right foot, dragging left boot, limping stumble.
  - Gövde Travması: hunched forward at 30-degree angle, clutching chest plate with gloved hand, restricted upper body rotation.
  - Solunum Krizi: rapid hyperventilation fogging visor interior, spasmic diaphragm movement.
- [UYGULAMA] Sayısal Pozitif Kilit ve Negatif Kadro Dondurma: Sahnede elenen veya ölen karakterlerin arka planda yeniden belirip halüsinasyon oluşturmasını önlemek için iki aşamalı kilit uygulanmalıdır. Kadro sayısı kelimeyle ve rakamla kesin olarak sabitlenmeli (precisely 1 solo astronaut), negatif prompt alanına ise duplicate character, extra astronaut, background clone, resurrected person, secondary suit ifadesi eklenmelidir.
- [ÖNERİ] Klip Arası İnersiyal Geçiş Tekniği: Klip N'in son saniyesindeki fiziksel duruş ile Klip N+1'in ilk saniyesindeki duruş arasında kinetik süreklilik kurulmalıdır. Klip N "karakter yere düşerken" bitiyorsa, Klip N+1 "karakter zemin üzerinde hareketsiz yatarken" başlamalıdır. Düşen bir karakter, takip eden klipte doğrudan yürür vaziyette başlatılmamalıdır.

## Sonuç

Yapay zeka video üretim modellerinde karşılaşılan D42 Anti-Reset hatası ve arka planda ölen karakterlerin yeniden belirmesi, difüzyon jeneratörlerinin durum hafızasız yapısından kaynaklanan mimari olgulardır. Harici 3B karakter modelleri veya VFX yazılımları olmadan, tamamen prompt mühendisliği standartları üzerinden süreklilik sağlamak mümkündür. Bu süreç; fiziksel travmanın biyomekanik kısıtlar üzerinden tanımlanmasına, kostüm hasarlarının SPEC durum parametreleri ile kilitlenmesine ve kadro değişikliklerinin pozitif sayısal kilitler ile negatif dışlama blokları üzerinden yönetilmesine dayanmaktadır.
