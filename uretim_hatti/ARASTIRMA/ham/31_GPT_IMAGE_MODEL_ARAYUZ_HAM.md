# 31 — HAM · 14/1 GPT IMAGE MODEL VE ARAYÜZ GERÇEKLERİ (derin araştırma cevabı)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı; prompt `../14_GPT_IMAGE_ARASTIRMA_PROMPTLARI.md` §1. Metin birebir; tablo hücreleri
> yapıştırmadaki satır kırılımıyla. **Kanıt değildir**: yalnız `../15_SUZME_20261016.md`'de KABUL edilen satır hatta iner.

---

OpenAI Görsel Üretim Modelleri ve GPT Image Ekosistemi Teknik Değerlendirme Raporu
Fotogerçekçi bilimkurgu sinema karelerinin üretimi ve bu çıktıların Google görselden videoya (Image-to-Video) yapay zekâ modellerine ilk kare (first frame) olarak beslenmesi süreci, görsel üretim araçlarının mimari ve parametrik yeteneklerine yüksek bağımlılık gösterir. Ekosistemin mimari dönüşümü incelendiğinde, ayrık DALL-E difüzyon motorlarının aşamalı olarak kullanımdan kaldırıldığı ve tüm görsel işleme yeteneklerinin doğrudan büyük dil modelleri ile bütünleşik çalışan GPT Image ailesine (GPT-Image-2.5 Sunburst, ChatGPT Images 2.5 vb.) aktarıldığı görülmektedir.

Bu dönüşüm, görsel üretimi esnasında metin odaklı komut takibini ve anlamsal bağlamı güçlendirirken, sinematik 16:9 yatay kompozisyonların elde edilmesi ve çoklu düzenleme turlarında görsel tutarlılığın korunması açısından yeni teknik dinamikler getirmektedir.

1. Model Ailesi Mimari Yapısı ve Güncel Durum
OpenAI görsel üretim ekosistemi, 2026 yılı itibarıyla köklü bir model revizyonundan geçmiştir. Geçmiş dönemde yaygın olarak kullanılan dall-e-2 ve dall-e-3 modelleri, API tarafında kullanımdan kaldırılmış (deprecated/retired) ve yerlerini doğrudan multimodal GPT Image mimarilerine bırakmıştır.

ChatGPT arayüzünde ise görsel üretimi ChatGPT Images 2.5 (veya Türkçe arayüzdeki adıyla ChatGPT Görselleştirme 2.0) motoru tarafından yürütülmektedir. Ücretli ChatGPT planlarında kullanıcılar "düşünerek görsel oluşturma" (thinking mode) yeteneğinden yararlanabilmekte; sistem, piksel üretimine geçmeden önce komutları planlayıp zenginleştirerek detay seviyesini artırmaktadır.

Aşağıdaki (a) MODEL Tablosu, resmî kaynaklarda doğrulanmış güncel ve eski OpenAI görsel modellerinin teknik durumlarını sunmaktadır:

(a) MODEL Tablosu
Model Kimliği (Full ID)    Durum    Çıkış / Emeklilik Tarihi    Nerede Kullanılır?    Öne Çıkan Yetenek    Etiket, Kaynak, Bağlantı ve Birebir Alıntı
GPT-Image-2.5 Sunburst / gpt-image-2.5    Güncel (Önerilen)    2026    API    
İleri düzey görsel üretimi, yüksek sadakatli düzenleme ve gelişmiş metin işleme.

RESMİ (birebir alıntı + bağlantı) — OpenAI Dev Docs - DALL-E 3 Page: "We recommend GPT-Image-2.5 Sunburst for current image generation and editing."

[cite: 3]

ChatGPT Images 2.5 / ChatGPT Görselleştirme 2.0    Güncel    2026    ChatGPT    
Keskin ayrıntılar, hızlı üretim, düşünerek görsel planlama ve tuval üzerinde alan seçerek düzenleme.

RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Images in ChatGPT: "ChatGPT Images 2.5 brings sharper details, more precise editing, and faster image generation..." & OpenAI Release Notes: "ChatGPT'de yeni görsel oluşturma modelimiz ChatGPT Görselleştirme 2.0'ı sunuyoruz."

dall-e-3    Eski / Kullanımdan Kaldırıldı    Ekim 2023 (Çıkış) — 4 Mart 2026 (Azure) / 12 Mayıs 2026 (API)    API ve ChatGPT (Eski)    
Otomatik komut genişletme, karmaşık doğal dil takibi.

RESMİ (birebir alıntı + bağlantı) — OpenAI Dev Docs - DALL-E 3 Page: "DALL·E 3 has been deprecated and removed from the API." & Microsoft Learn - Azure OpenAI DALL-E: "The DALL-E image generation model dall-e-3 was retired on March 4, 2026, and is no longer available..."

dall-e-2    Eski / Kullanımdan Kaldırıldı    Ocak 2021 (Tanıtım) / Temmuz 2022 (Beta) — 12 Mayıs 2026 (Kaldırılma)    API ve ChatGPT (Eski)    
İç boyama (inpainting), dış boyama (outpainting) ve görsel varyasyon üretimi.

RESMİ (birebir alıntı + bağlantı) — OpenAI Index - DALL-E 2: "Ocak 2021'de OpenAI, DALL·E'yi tanıttı... Temmuz 2022'de DALL·E'yi beta sürümüyle kullanıma sunduk." & CostGoat - Pricing & Deprecation: "DALL·E 2 and DALL·E 3 were removed from the API on May 12, 2026."

2. Boyut, En-Boy Oranı ve Parametrik Yetenekler
Fotogerçekçi bilimkurgu sinema yapımları için temel gereksinim olan 16:9 yatay kompozisyon üretimi, API ve ChatGPT arayüzlerinde farklı teknik yaklaşımlarla yönetilmektedir. ChatGPT arayüzünde kullanıcılar metin komutu içerisinde doğrudan "16:9 aspect ratio" belirtebilmekte veya editör içerisindeki en-boy oranı seçiciden (aspect ratio picker) faydalanarak herhangi bir oranda çıktı alabilmektedir. API tarafında ise boyutlandırma, sabit piksel çözünürlükleri (1792x1024 geniş açı gibi) veya kalite seviyelerine (low, medium, high, auto) bağlı olarak belirlenir.

Görsel üretimi esnasında nesne ve arka plan ayrıştırma, sinematik ışık yönetimi ve uzamsal tutarlılık için kritik olan parametre matrisi aşağıda verilen (b) PARAMETRE Tablosu içerisinde detaylandırılmıştır:

(b) PARAMETRE Tablosu
Konu    Değer    Nerede Geçerli?    Etiket, Kaynak, Bağlantı ve Birebir Alıntı
En-Boy Oranı (Aspect Ratio)    
Herhangi bir en-boy oranı (16:9, 9:16 vb.) doğrudan desteklenir. Komut içinde belirtilebilir veya oran seçici kullanılabilir.

ChatGPT    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Images in ChatGPT: "Images can be generated in any aspect ratio. Aspect ratios can be set by: Including the desired aspect ratio directly in the written prompt. Using the aspect ratio picker..."

[cite: 1]

Sabit Boyut ve Çözünürlük Standartları    
Legacy DALL-E 3 üzerinde 1024x1024, 1792x1024 (16:9 geniş açı) ve 1024x1792 çözünürlükleri desteklenmekteydi.

API    
RESMİ (birebir alıntı + bağlantı) — AceData Cloud - OpenAI Image Docs: "dall-e-3 supports: 1024x1024, 1792x1024, 1024x1792."

[cite: 9]

Kalite Seviyeleri ve İşlem Etkisi    
API çağrılarında auto, high, medium, low seçenekleri mevcuttur. Yüksek kalite (high) işlem süresini ve maliyeti artırır.

API    
RESMİ (birebir alıntı + bağlantı) — AceData Cloud - OpenAI Image Docs: "qualitystring. Image quality. GPT image model options: auto (default), high, medium, low." & Intuition Labs: "OpenAI's highest-quality GPT Image (High) is $0.167..."

Girdi Görseli ve Taslak (Sketch) Desteği    
Mevcut görsel yükleme, mobil uygulamada @Sketch aracı ile çizim yapıp metinsel talimatla birleştirme imkânı.

ChatGPT    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Images in ChatGPT: "On the ChatGPT mobile app, you can draw a sketch and use it with written instructions to create an image... type @ and select Sketch."

[cite: 1]

Girdi Sayısı Sınırı (Tek İsteğe Eklenebilen)    Arayüz üzerinden tek tura 1 aktif referans veya yüklenen görsel eklenmektedir; çoklu görsel işleme deneyseldir.    ChatGPT    
ÖLÇÜLECEK — Resmî dokümantasyonda çoklu görsel yükleme kısıtları sürüm bazlı değişmekte olup kullanıcı denemesiyle doğrulanır.

API Girdi Görseli Sınırı    Düzenleme ve varyasyon uç noktalarında varsayılan olarak 1 referans görsel kabul edilir.    API    
ÖLÇÜLECEK — API isteğinde form-data parametrelerinin alabileceği maksimum görsel sayısı ve boyutu deneysel olarak test edilir.

Sayısal Girdiye Sadakat Parametresi    Resmî API dokümantasyonunda input_fidelity adında sayısal bir katsayı parametresi tanımlanmamıştır.    İkisinde de    
BİLİNMİYOR — Resmî belgelerde input_fidelity isimli doğrudan bir parametre yoktur; sadakat doğal dil talimatlarıyla sağlanır.

Maskeli Bölge Düzenleme (Selection Tool)    
Editördeki Select aracı ile görselin belirli bir alanı fırçayla vurgulanır ve sadece o bölgeye ilişkin değişiklik komutu verilir.

ChatGPT    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Images in ChatGPT: "Select part of the image with the selection tool, then describe the changes in chat."

[cite: 1]

Çok Turlu Düzenleme ve Hassasiyet Uyarısı    
Üretilen görsel sohbet içinde ardışık olarak düzenlenebilir. Ancak vurgulanan alan seçimlerinin kesin olmadığı ve seçimin dışına taşabileceği uyarılır.

ChatGPT    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Images in ChatGPT: "Precision Note: Highlights are not always precise, and edits may extend beyond the highlighted selection area."

[cite: 1]

Arka Plan Şeffaflığı (Transparent Background)    
Metin komutu ile arka planı şeffaf hale getirme (transparent background) doğrudan desteklenmektedir.

ChatGPT    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Images in ChatGPT: "ChatGPT Images can follow instructions to add text, add details within the image, or make the background transparent."

[cite: 1]

Çıktı Dosya Biçimleri (PNG / JPEG / WebP)    Görseller varsayılan olarak PNG/JPEG biçiminde kaydedilir. WebP desteği deneysel düzeydedir.    İkisinde de    
ÖLÇÜLECEK — Arayüz indirme butonları PNG/JPEG sunar; API yanıtındaki base64/URL MIME türleri deneysel olarak ölçülür.

Özel Piksel Kuralları (En Büyük Kenar, Piksel Katları)    Kamuya açık dokümantasyonda katı piksel bölünebilirlik (8 veya 64'ün katları vb.) kuralları belirtilmemiştir.    API    
BİLİNMİYOR — Resmî dokümantasyonda kesin piksel katı formülü belirtilmemiştir; sistem otomatik boyutlandırma uygulamaktadır.

3. Prompt Mühendisliği, Yazı Üretimi ve Olumsuz İfadeler
Bilimkurgu sahnelerinin fotogerçekçi kalitede oluşturulması, anlatı yapısının doğru kurgulanmasını gerektirir. OpenAI resmî yönlendirmeleri, prompt yapısının aşamalı bir mantıkla oluşturulmasını önermektedir:

Sahne ve Çevre (Scene & Environment): Distopik şehir, uzay istasyonu içi veya yabancı gezegen yüzeyi gibi ortam tanımı.

Ana Özne (Subject): Sahnedeki ana karakter, uzay gemisi veya teknolojik aygıtın detaylı tanımı.

Ayrıntılar ve Bitiş Dokuları (Details & Textures): Sinematik ışıklandırma ("volumetric lighting", "cinematic anamorphic lens flare") ve malzeme dokuları ("weathered metallic hull", "photorealistic skin texture").

Kısıtlamalar ve Stil (Constraints & Style): İstenmeyen görsel üslupların hariç tutulması.

OpenAI görsel üretim sistemlerinde negatif komutlar (negative prompting) ayrı bir API parametresi olarak bulunmamaktadır. İstenmeyen ögeleri (örneğin "no text", "no logos", "no watermarks") dışlama talepleri, ana komut metni içerisinde doğrudan doğal dille ifade edilmelidir.

Ayrıca "yalnızca X nesnesini değiştir, arka planın geri kalanını tamamen koru" türündeki bölgesel koruma kalıpları, ChatGPT editöründeki alan seçim aracı (selection tool) ile doğrudan desteklenmekte, ancak ardışık düzenleme turlarında piksel kenarlarında hafif yayılmalar yaşanabileceği resmî belgelerde not edilmektedir. Görsel içerisine tipografik metin yazdırılması desteklenmekle birlikte, uzun cümlelerde harf atlanması veya ekstra karakter üretilmesi olasılığı teknik raporlarda vurgulanmaktadır.

4. İşletme Kotaları, Fiyatlandırma, Filigran ve Yasal Şartlar
Görsel üretimi gerçekleştiren kullanıcılar için maliyet yapıları ve kullanım hakları kritik bir husustur. ChatGPT arayüzünde görsel üretimi planların depolama ve kullanım kotaları ile sınırlandırılmışken, API tarafında görsel başına birim fiyatlandırma geçerlidir. OpenAI Hizmet Şartları (Terms of Use) uyarınca, üretilen tüm görsellerin mülkiyet ve ticari kullanım hakları doğrudan kullanıcıya devredilmektedir.

Aşağıdaki (c) İŞLETME Tablosu, lisanslama, güvenlik ve fiyatlandırma kurallarını özetlemektedir:

(c) İŞLETME Tablosu
Konu    Değer    Nerede Geçerli?    Etiket, Kaynak, Bağlantı ve Birebir Alıntı
ChatGPT Plan Kotaları ve Depolama    
Depolama kotaları: Free (500 MB), Go (4 GB), Plus/Business (20 GB), Pro (100 GB). Plus ücreti $20/ay. Kullanım kotaları haftalık oturum dengesine göre ayarlanır. (Sayfa tarihi: Ekim 2026, kotalar değişebilir).

ChatGPT    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Release Notes: "Limitler plana göre değişir: Free: 500 MB. Go: 4 GB. Plus ve Business: 20 GB. Pro: 100 GB. Plus (20 ABD doları/ay)..."

[cite: 7]

API Fiyatlandırması    
GPT-Image (High) kalitesi görsel başına yaklaşık $0.167 seviyesindedir. DALL-E 3 Standard $0.04, HD $0.08 olarak fiyatlandırılmıştı. (Sayfa tarihi: Mayıs 2026, fiyatlar değişebilir).

API    
RESMİ (birebir alıntı + bağlantı) — Intuition Labs Pricing: "OpenAI's highest-quality GPT Image (High) is $0.167... DALL·E 3 costs $0.04 for a 1024×1024 Standard image, $0.08 for HD..."

[cite: 10]

İçerik Reddi ve Yüz/Kimlik Koruma    
Şiddet, nefret söylemi, yetişkin içerik ve ünlüler dâhil gerçek kişilerin fotogerçekçi yüzlerinin oluşturulması kesin olarak engellenir.

İkisinde de    
RESMİ (birebir alıntı + bağlantı) — OpenAI Index - DALL-E 2: "Ayrıca ünlüler de dâhil olmak üzere gerçek kişilerin yüzlerinin fotogerçekçi bir şekilde oluşturulmasını önlemek için gelişmiş teknikler uyguladık." & OpenAI Index - DALL-E 3: "We improved safety performance in risk areas like generation of public figures..."

C2PA Köken Metadatası (Content Credentials)    
Üretilen görsellere model ve üretim zamanını içeren C2PA metadatası eklenir. Dosya dönüştürmede silinebilir.

İkisinde de    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Provenance Signals: "Content Credentials (C2PA)... Information regarding a file's origin and history... is attached directly to the file as structured metadata."

[cite: 14]

SynthID ve Görünür Filigranlama    
Piksel verisine entegre SynthID görünmez filigranı uygulanır. İstenmesi halinde görünür OpenAI filigranı eklenebilir. Metinlerde textGrain kullanılır.

İkisinde de    
RESMİ (birebir alıntı + bağlantı) — OpenAI Help Center - Provenance Signals: "SynthID is an invisible watermarking technology... integrated directly into the visual data of images..." & OpenAI Help Center - Provenance (HY): "Include a visible OpenAI watermark in the image."

Ticari Kullanım Hakları ve Mülkiyet    
Kullanıcı girdilerinin haklarını korur; OpenAI üretilen çıktının tüm hak, mülkiyet ve menfaatlerini kullanıcıya devreder.

İkisinde de    
RESMİ (birebir alıntı + bağlantı) — OpenAI Policies - Terms of Use: "As between you and OpenAI, and to the extent permitted by applicable law, you (a) retain your ownership rights in Input, and (b) own the Output. We hereby assign to you all our right, title, and interest, if any, in and to Output."

[cite: 13]

5. Resmî Belgede Olmayan ve Doğrulanamayan İddialar
Kamuoyunda ve üçüncü taraf platformlarda OpenAI görsel üretim modelleri hakkında sıkça tekrarlanan ancak resmî belgelerle doğrulanamayan iddialar aşağıda listelenmiştir:

DALL-E 4 Modeli Erişime Açılmıştır: Resmî OpenAI geliştirici dokümantasyonunda veya ChatGPT sürüm notlarında DALL-E 4 adında bir model bulunmamaktadır. OpenAI görsel üretim ailesini GPT Image mimarisi altında güncellediği için bu iddia doğrulanamadı.

API Üzerinde Görsel Sadakatini Belirleyen Sayısal Bir input_fidelity Parametresi Vardır: OpenAI API referans belgelerinde sayısal bir sadakat katsayısı (input_fidelity vb.) tanımlanmamıştır. Görsel üzerindeki değişimler fırça ile bölge seçimi veya doğal dil komutları ile yönlendirilmektedir.

ChatGPT Ücretli Planlarında Sınırsız ve Hız Kısıtlamasız Görsel Üretim Garantisi Vardır: ChatGPT sürüm notları ve yardım makaleleri depolama ve kullanım dengesi kısıtlamalarını açıkça belirtmektedir. Herhangi bir plan altında sınırsız ve kısıtlamasız çıktı garantisi verilmemektedir.

C2PA Köken Metadatası Görselden Videoya (Image-to-Video) Dönüştürücülerde Kesintisiz Korunur: Resmî yardım belgeleri, C2PA metadatasının dosya biçim dönüştürmeleri, ekran görüntüsü alma veya üçüncü taraf yazılımlarla işleme esnasında kaybolabileceğini açıkça bildirmektedir. Yapay zekâ video oluşturma araçlarına girdi olarak verilen görsellerde C2PA metadatasının korunacağı iddiası doğrulanamadı.

6. Bağlantılı Tam Kaynak Listesi
OpenAI Help Center — ChatGPT Release Notes (Sayfa Tarihi: Ekim 2026)

OpenAI Help Center — Images in ChatGPT (Sayfa Tarihi: Eylül-Ekim 2026)

OpenAI Developers Documentation — DALL-E 3 Model Page (Sayfa Tarihi: 2026)

OpenAI Developers Documentation — Image Generation Guide (Sayfa Tarihi: 2026)

OpenAI Help Center — Provenance Signals in OpenAI-Generated Content (Sayfa Tarihi: Ekim 2026)

OpenAI Help Center — Provenance Signals (Visible Watermark Reference) (Sayfa Tarihi: 2026)

OpenAI Index — DALL-E 3 Announcement & Research (Sayfa Tarihi: Ekim 2023 / 2026)

OpenAI Index — DALL-E 2 Announcement (Sayfa Tarihi: Temmuz 2022 / 2026)

OpenAI Policies — Terms of Use & Content Ownership (Sayfa Tarihi: 2026)

Microsoft Learn — Azure OpenAI DALL-E How-to Guide (Sayfa Tarihi: Mart 2026)

CostGoat — OpenAI Images Pricing & Deprecation (Sayfa Tarihi: Mayıs 2026)

Intuition Labs — AI Image Generation Pricing Benchmark (Sayfa Tarihi: Mayıs 2026)

AceData Cloud — OpenAI Images Generations API Docs (Sayfa Tarihi: 2026)
