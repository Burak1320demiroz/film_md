# 🔬 14 — GPT IMAGE: ÜÇ DERİN ARAŞTIRMA PROMPTU (16.10.2026)

> **Durum:** ✅ KOŞULDU — 16.10.2026. Ham: `ham/31_GPT_IMAGE_MODEL_ARAYUZ_HAM.md` · `32_GPT_IMAGE_SERI_TUTARLILIK_HAM.md` ·
> `33_GPT_IMAGE_BASLANGIC_KARESI_HAM.md` · süzme: `15_SUZME_20261016.md`. ⚠️ Aşağıdaki SINAMA SETİ'ndeki "2.5-sunburst/flare YOK" satırı yanlıştı (15 §DÜZELTME).
>
> **Neden:** sahip 16.10.2026'da "GPT Image için de 3 araştırma promptu hazırla" dedi. Hattın görsel tarafı (başlangıç karesi, referans
> sayfası, düzeltme) GPT Image'a geçti (THE_SKY_CATCH: GPT Image → Gemini). Elde yalnız iki resmî OpenAI sayfasından doğrulanmış birkaç cümle var
> (`11` V7-V9, `13` V16-V18); rapor 28 uydurma model adları ("gpt-image-2.5-sunburst/flare") verdi.
>
> **Hedef ürünler:**
>
> | # | konu | beslediği yer | dört filmdeki kanıt |
> |:--:|---|---|---|
> | 1 | **MODEL VE ARAYÜZ GERÇEKLERİ** — hangi model, ChatGPT ile API farkı, boyut/oran, girdi sayısı, düzenleme, kota | `FLOW_GERCEKLERI.md` yeni Ek 3 (GPT Image olgu tablosu) · `GPT_IMAGE_OMNI_KILAVUZU` §1, §13 | 1536×1024 = 3:2 kare 16:9 videoya giremez; hangi referansın yüklendiği kayıtsız |
> | 2 | **SERİ TUTARLILIĞI** — 24-96 karede aynı yüz, giysi, mekân, nesne durumu; referans sayfası; çok turlu düzenleme | `KIMLIK_VE_REFERANS_KILAVUZU` §2-§7 · SMOKE P15/P17 | 4/4 filmde yüz, bant, bayrak/arma kayması |
> | 3 | **VİDEOYA HAZIR BAŞLANGIÇ KARESİ** — I2V'ye uygun kompozisyon, ışık, doku, yazısız kare; GPT Image karesinin video modelindeki davranışı | `GPT_IMAGE_OMNI_KILAVUZU` §6-§7 · `UZAY_FIZIGI_GORUNTU` §1 | kare hataları videoda çoğaldı; duman/damla karede başladı |
>
> **Depoda bugün olan (tekrar sorulmaz):** `GPT_IMAGE_OMNI_KILAVUZU.md` · `KIMLIK_VE_REFERANS_KILAVUZU.md` · `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` ·
> `.claude/skills/image/` (üçüncü taraf skill, NB2/NBP/GPT Image 2 prompt kalıpları; donmuş değil ama hat kuralı değil) · `ARASTIRMA/11` ve `13` süzmeleri.
>
> **Nasıl koşulur:** 01-12 ile aynı. Her prompt tek başına; kod bloğunu derin araştırma aracına yapıştır, başka bir şey verme.
> Depo, film ve kanal adı verilmez. **SINAMA SETİ araca verilmez.**
>
> **Sıra:** ⭐ 1 önce (model adı ve arayüz gerçeği yanlışsa 2 ve 3'ün cevapları da yanlış modele bağlanır), sonra 2, sonra 3.

---

# 1️⃣ MODEL VE ARAYÜZ GERÇEKLERİ — GPT Image Ekim 2026'da tam olarak ne yapar

```
OpenAI'ın görsel üretim modellerinin (GPT Image ailesi) Ekim 2026 itibarıyla güncel durumunu yalnız resmî kaynaklardan araştır: OpenAI API belgeleri (image generation guide, image prompting guide, model sayfaları, API reference, changelog, deprecations), OpenAI Cookbook, OpenAI Help Center ve ChatGPT sürüm notları, OpenAI blog duyuruları. Şunları bul ve her biri için birebir alıntı ve bağlantı ver:
(1) Model listesi: bugün hangi GPT Image modelleri var (tam model kimlikleriyle), hangisi en yetenekli, hangisi eski/kullanımdan kalkıyor, çıkış tarihleri; ChatGPT içinde hangi modelin kullanıldığı ve bunun kullanıcıya nasıl gösterildiği. Belgede bulamadığın model adını yazma; benzer adlı üçüncü taraf iddialarını ayrıca "doğrulanamadı" diye listele.
(2) Boyut ve oran: desteklenen çıktı boyutları ve en-boy oranları (API'de ve ChatGPT'de ayrı ayrı), 16:9 ya da 9:16 doğrudan üretilebiliyor mu, en yüksek çözünürlük, özel boyut kuralları (piksel katları, en büyük kenar, toplam piksel), kalite seviyeleri (low/medium/high vb.) ve bunların süre ve maliyete etkisi, çıktı biçimleri (PNG, JPEG, WebP), arka plan şeffaflığı.
(3) Girdi görselleri: bir üretim isteğine kaç görsel eklenebilir (API ve ChatGPT ayrı), girdi görselinin boyut ve biçim sınırları, girdiye sadakati ayarlayan bir parametre var mı (örneğin input fidelity) ve neyi etkiler, yüz ve kimlik koruma hakkında resmî ifade, referansa numara ve rol vermenin resmî önerisi.
(4) Düzenleme: maskeli düzenleme ve maskesiz düzenleme farkı, ChatGPT'de bir bölgeyi seçip düzenleme, çok turlu düzenleme (önceki çıktıyı girdi yapma, "previous response" türü zincirleme), tekrarlanan düzenlemede ayrıntı kaybına dair resmî uyarı, "yalnız X'i değiştir, gerisini koru" kalıbının resmî biçimi.
(5) Prompt ve yazı: resmî prompt rehberinin yapı önerisi (sahne, özne, ayrıntı, kısıt sırası), istenmeyen yazı/logo/filigranı dışlama ifadesi, görselde yazı üretimi ve bastırılması, olumsuz ifade kullanımı hakkındaki resmî tutum.
(6) İşletme: ChatGPT planlarına göre görsel üretim sınırları ve hız, API fiyatı (görsel başına ya da token başına; kalite ve boyuta göre), içerik politikası reddi ve gerçek kişi benzerliği kuralı, çıktıda C2PA köken metadatası ve görünür filigran olup olmadığı, ticari kullanım hakkı (Terms of Use ve Usage Policies'deki cümle).
Kritik kısıt: kullanım yeri, bir kanalın her filmine uygulanan GENEL bir araç olgu sayfasıdır. Görseller fotogerçekçi bilimkurgu film kareleridir (16:9 yatay), sonra Google'ın görselden videoya modeline başlangıç karesi olarak verilir; üretimi tek kişi çoğunlukla ChatGPT arayüzünden, bazen API'den yapar. Her satırda "API'de mi, ChatGPT'de mi, ikisinde de mi" belirt; birinde bulunanı ötekine genelleme. Tarihsiz ya da kaynaksız sayı verme; sayfanın tarihini yaz. Fiyat ve kota değişkense "sayfa tarihi şu, değişebilir" de.
Çıktıyı üç tablo ve iki liste olarak ver: (a) MODEL tablosu — model kimliği, durum (güncel/eski/kalkıyor), çıkış tarihi, nerede kullanılır (API/ChatGPT), öne çıkan yetenek, kaynak ve birebir alıntı; (b) PARAMETRE tablosu — konu (boyut, oran, kalite, girdi sayısı, sadakat, maske, biçim, şeffaflık), değer, API/ChatGPT, kaynak ve birebir alıntı; (c) İŞLETME tablosu — konu (kota, fiyat, red, benzerlik, köken metadatası, filigran, ticari hak), değer, API/ChatGPT, kaynak ve birebir alıntı. Etiketler RESMİ (birebir alıntı + bağlantı) · ÖLÇÜLECEK (belgede yok, kullanıcı denemesiyle görülür) · BİLİNMİYOR. Listeler: (1) resmî belgede olmayan ama sık tekrarlanan iddialar ve neden doğrulanamadıkları; (2) bağlantılı tam kaynak listesi, her biri sayfa tarihiyle. Belgede olmayan model adı, boyut, parametre, kota ya da fiyat uydurma.
```

### 🧪 SINAMA SETİ

```
DOĞRULANMIŞ (16.10.2026, Fable):
  OpenAI Cookbook (image-gen-models-prompting-guide): "gpt-image-2" "our most capable image model" · gpt-image-1.5 "for existing validated
    workflows during migration" · gpt-image-1 "Legacy compatibility only" · gpt-image-1-mini "cost and throughput"
  "gpt-image-2.5-sunburst / flare" YOK (rapor 28'in uydurması)
  image-prompting guide: "Identify each input by number and purpose" · "State exclusions such as unwanted text, logos, or watermarks." ·
    "Repeated edits can still change details you intended to preserve." · "Pass the previous output as the next edit input, request one change"
  Cookbook: "change only X" + "keep everything else the same" · "- No watermarks" · "- No logos" · "reusable “character anchor”"
HATTAKİ VARSAYIM: 1536×1024 (3:2) ve 1024×1536 (2:3) GPT Image boyutları; 16:9 için merkezden 1536×864 kırpma (GPT_IMAGE_OMNI §13)
  → gpt-image-2'de 16:9 doğrudan var mı?
HATTAKİ KURAL: görsel promptta olumsuz blok yok (Veo gerekçesiyle) — 11/13 §D K2 sahipte; OpenAI'ın kendi tutumu ne?
AÇIK: girdi görseli sınırı (ChatGPT kaç görsel alıyor) · input fidelity · ChatGPT'de hangi model · kota · C2PA · ticari hak cümlesi
CEVAPTAN BEKLENEN: tam model listesi · 16:9 doğrudan üretim · girdi sayısı (ChatGPT/API) · sadakat parametresi · düzenleme biçimleri ·
  olumsuz ifadeye resmî tutum · ticari kullanım cümlesi.
```

---

# 2️⃣ SERİ TUTARLILIĞI — 24-96 film karesinde aynı karakter, mekân ve nesne

```
OpenAI'ın GPT Image modelleriyle (ChatGPT ve API) bir film için onlarca başlangıç karesi üretirken karakterin, kostümün, mekânın ve nesnelerin tutarlı kalmasını sağlayan yöntemleri Ekim 2026 itibarıyla araştır. Önce resmî kaynakları (OpenAI image prompting guide, Cookbook örnekleri — özellikle karakter çapası ve hikâye devamı örnekleri —, API belgeleri, Help Center), sonra yöntemi yazılı uygulayıcı çalışmalarını (çizgi roman, storyboard, çocuk kitabı ve yapay zekâ film üreticilerinin yayımlanmış iş akışları, karşılaştırmalı testler) topla. Şunları sor:
(1) Referans biçimi: tek görselde önden/yandan/arkadan/yüz yakın panelleri olan karakter sayfası ile her görünüşün ayrı dosya olması — GPT Image hangisinde kimliği daha iyi taşır; panel sayfasından kareye kopya figür ya da panel düzeni sızıyor mu; "arka görünüş panelini kullan" gibi panel atfı işe yarıyor mu; sayfanın ızgara düzeni, panel sayısı, boşluk ve arka planın etkisi. Yöntemi yazılı karşılaştırma yoksa bunu açıkça söyle ve tek değişkenli küçük bir deney öner.
(2) Referans sayısı ve rol: bir isteğe eklenen referans sayısı arttıkça (karakter + mekân + nesne durumu) sadakatin nasıl değiştiği; iki karakterin aynı karede yüzlerinin karışması ve önlemi; referans sırasının etkisi; metinde numara ve rol vermenin etkisi.
(3) Kostüm mikro ayrıntısı: renkli kol bandının renginin kayması, şerit sayısının artması, rozetin biçim ya da konum değiştirmesi, giysiye kendiliğinden bayrak, ajans logosu, yazı eklenmesi — beyaz basınç giysili astronotlarda bu kaymaların bilinen örnekleri ve önlemleri (olumlu ve sayılı tarif, "the only marking on the suit" gibi kilit cümleler, dışlama satırı, renk kodu vermenin etkisi).
(4) Sohbet ve oturum: ChatGPT'de aynı sohbette kareleri sırayla üretmek ile her kare için yeni sohbet açıp referansları yeniden eklemek; sohbet uzadıkça kayma olup olmadığı; ChatGPT'nin "bellek" ya da proje özelliklerinin görsel tutarlılığa etkisi; API'de önceki yanıtı zincirlemek ile her seferinde referans göndermek.
(5) Çok turlu düzenleme ve kayma: aynı kareye arka arkaya düzenleme uygulandıkça yüzün, dokunun ve ışığın aşınması; kaç düzenlemeden sonra baştan üretmenin daha iyi olduğuna dair kanıt; maskeli düzenlemenin bu aşınmayı azaltıp azaltmadığı; düzenlemede korunacakları listeleme kalıbı.
(6) Mekân ve nesne durumu: aynı mekânın farklı kamera açılarında mimarinin (kapı hangi duvarda, konsol nerede) korunması; nesnenin açık/kapalı, katlı/açılmış durumlarının ayrı referanslarla yönetilmesi; ters açı üretiminde mekânın aynalanması hatası ve önlemi.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kimlik ve referans kılavuzudur. Filmler 2-16 dakikalık, fotogerçekçi, yatay bilimkurgu filmleridir; film başına 2-4 karakter (çoğunlukla beyaz basınç giysili, kasklı, birbirinden kol bandı rengi, rozet ve yüzle ayrılan astronotlar; yüz bazen şeffaf vizör ardında, bazen hiç görünmez), 5-10 mekân/araç/nesne referansı ve 12-96 başlangıç karesi vardır. Üretimi tek kişi web arayüzünden yapar; model eğitimi (LoRA, ince ayar) yoktur, gerektiren yolları "hat dışı" diye işaretle. Model kimliğini ve tarihini her satırda yaz; eski modelle (gpt-image-1 vb.) bulunan sonucu yeni modele genelleme ve belgede olmayan model adı kullanma.
Çıktıyı üç tablo ve üç liste olarak ver: (a) YÖNTEM tablosu — yöntem (panel sayfası, ayrı görünüşler, metin kimlik bloğu, karakter çapası, aynı sohbet, yeni sohbet, zincirleme, maskeli düzenleme), ne korur, bilinen yan etki, model ve tarih, kaynak, etiket; (b) KAYMA tablosu — kayma (yüz, bant rengi, şerit sayısı, rozet, bayrak/logo/yazı, kask/vizör, mekân aynalanması, nesne durumu), tipik neden, önlem ve kanıtı, kaynak, etiket; (c) DÜZENLEME tablosu — düzenleme türü, kaç turda aşınma görülür, aşınmanın belirtisi, önlem, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız test; birebir alıntı + bağlantı) · UYGULAMA (uygulayıcı pratiği) · ÖNERİ (senin çıkarımın); aynı kaynağa dayanan iki iddia tek kanıt; firma tanıtımı ÖLÇÜLMÜŞ değildir. Listeler: (1) 24 karelik bir film için adım adım tutarlılık iş akışı (referansları üret → onayla → kareleri hangi sırayla ve hangi oturum düzeniyle üret → her karede ne kontrol et); (2) panel sayfası ile ayrı görünüşü karşılaştıran, az krediyle yapılabilen tek değişkenli deney; (3) bağlantılı tam kaynak listesi. Belgede olmayan yüzde, eşik ya da model davranışı uydurma.
```

### 🧪 SINAMA SETİ

```
DÖRT FİLMİN KANITI (15.10.2026 QA):
  GPT Image → Gemini ile üretilen 4 dk film: aynı kadın 3 farklı yüz · turkuaz bant → mavi · göğüste yazılı arma · omuzda ABD bayrağı ·
    pilotta ikinci turuncu şerit · kapak menteşesi üstten → yandan (dolap kapağı) · kabin dikey → yatay halkalı istasyon
  diğer 3 film (görsel aracı kayıtlı değil): sakalsız başka yüz · hilal-yıldız arması · omuzluk rengi gidip geliyor · yeni yaralar ·
    aynı alet 3 biçim · kask içinde bere var/yok · çift vizör çizgisi
  Hiçbir filmde hangi referansın gerçekten yüklendiği kayıtlı değil
HATTAKİ KURAL (sahip, 10.10.2026): özne başına TEK panel sayfası · "Reference <No> (<rol>): take … from it, using the back-view panel" ·
  SMOKE P15/P17 koşulmadı · KIMLIK §7: P17 = panel sayfasını kırparak tek görünüş (tek değişken)
RAPOR 28 (uydurma model adıyla): "panel → klonlama ve sızma" · "3-4 referanstan sonra doygunluk" · düzeltme turu doku %85/%70/%40 — hepsi kaynaksız
HAT VARSAYILANI: çekim başına ≤3 referans (Veo 3.1 resmî sınırından muhafazakâr) · iki kontrollü düzeltmeden sonra yeniden üret
SAHİBİN EVA BLOKLARI: "smooth, unmarked chest and sleeves" kilidi (GPT_IMAGE_OMNI Ek A)
CEVAPTAN BEKLENEN: panel ↔ ayrı görünüş için gerçek bir karşılaştırma var mı · aynı sohbet mi yeni sohbet mi · bayrak/arma kilidinin en iyi biçimi ·
  çok turlu düzenlemede aşınmanın gerçek gözlemi · ters açıda mekânın aynalanması.
```

---

# 3️⃣ VİDEOYA HAZIR BAŞLANGIÇ KARESİ — GPT Image karesi görselden videoya modele nasıl girmeli

```
OpenAI'ın GPT Image modelleriyle üretilen bir görselin, görselden videoya (image-to-video) modellerine — özellikle Google'ın Gemini Omni 1.1 Flash ve Veo 3.1 modellerine — başlangıç karesi olarak verildiğinde iyi sonuç vermesi için nasıl tasarlanması gerektiğini Ekim 2026 itibarıyla araştır. Resmî kaynakları (Google'ın Veo/Omni prompt rehberleri ve image-to-video belgeleri, OpenAI görsel prompt rehberi) ve yöntemi yazılı uygulayıcı çalışmalarını topla. Şunları sor:
(1) Kompozisyon ve durum: başlangıç karesinin hareketten önceki anı göstermesi; hareket payı (kolun döneceği boşluk, yürünecek alan, yaklaşılacak aralık) bırakmanın etkisi; el-nesne temasının karede zaten kurulu olmasının videoda el erimesi ve fazla parmağı azaltıp azaltmadığı; kadraj dışı kalan uzvun videoda uydurulması; derinlik, ön plan nesnesi ve ölçeğin videodaki kamera hareketine etkisi.
(2) Işık, doku ve "yapay zekâ görünümü": GPT Image çıktılarında sık görülen görsel imzalar (aşırı keskinlik, düzgün cilt, sarı/sıcak renk eğilimi, yoğun ayrıntı, plastik malzeme, aşırı simetri) ve bunların video modelinde nasıl davrandığı (titreme, doku kaynaması, renk kayması); film greni, lens karakteri ve "35 mm film still" tarifinin hem görselde hem videoda etkisi; karanlık sahnede yüz ve nesnenin okunur kalması; video modelinin başlangıç karesinin rengini ve ışığını ne kadar koruduğu.
(3) Teknik uygunluk: başlangıç karesinin en-boy oranının videonun oranını belirlemesi (Gemini uygulaması yüklenen görselin oranını izler); GPT Image'ın verdiği boyutlardan 16:9'a kırpma ya da genişletme (outpaint) — hangisi daha iyi sonuç verir; çözünürlük, büyütme (upscale) ve sıkıştırmanın video kalitesine etkisi; PNG/JPEG farkı; video modelinin başlangıç karesini küçültüp küçültmediği.
(4) Kareye gömülü sorunlar: karede istemeden oluşan yazı, logo, bayrak, filigran ya da C2PA/görünür işaretin video modeline etkisi; karede yanlış bir fiziğin (duman, damla, basan ayak, ters yönlü alev) videoda büyümesi; video modelinin karedeki bir nesneyi "canlandırmaya" çalışması (örneğin hareketsiz kalması gereken kablo ya da sıvı).
(5) Görsel prompt ile video promptunun iş bölümü: görsel prompt karede ne olduğunu, video prompt yalnız neyin değiştiğini söylemeli mi; Google'ın "image-to-video'da karakteri, arka planı, ışığı yeniden tarif etme" uyarısı ve kanıtı; aynı kimlik cümlesinin iki promptta da birebir tekrarının etkisi.
(6) Kare kabulü: başlangıç karesini videoya göndermeden önce bakılacak ölçütler ve yerelde ölçülebilenler (oran ve piksel, histogram ve pozlama, keskinlik, yazı tespiti/OCR, renk ölçümü); çok sayıda kare için hızlı gözden geçirme yöntemi (kontak sayfası).
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir başlangıç karesi kılavuzudur. Filmler fotogerçekçi, yatay 16:9 bilimkurgu filmleridir; çekimler 10 saniyedir; sahneler çoğunlukla yörünge, istasyon dışı, kenetlenme, uzay yürüyüşü ve kokpit içidir; karakterler kasklı astronotlardır. Görseller GPT Image ile (çoğunlukla ChatGPT arayüzünden) üretilir, video Gemini Omni 1.1 Flash ile (Gemini uygulaması ya da Google Flow) üretilir. Video modeli tek başlangıç karesi alır; ayrı bitiş karesi her arayüzde yoktur, varmış gibi yazma. Model ve arayüz sürümlerini tarihle yaz; başka bir video modelinde (Runway, Kling, Sora) bulunanı ayrıca etiketle ve Google modellerine genelleme.
Çıktıyı üç tablo ve üç liste olarak ver: (a) KARE TASARIMI tablosu — ilke (hareketten önceki an, hareket payı, temas, derinlik, ışık okunurluğu, doku), videoda etkisi, kanıt, model, kaynak, etiket; (b) GPT IMAGE İMZASI tablosu — imza (keskinlik, renk eğilimi, plastik doku, yazı/logo, simetri), videoda ne olur, önlem (görsel promptta ya da sonradan düzeltmede), kaynak, etiket; (c) TEKNİK tablosu — konu (oran, kırpma/genişletme, çözünürlük, büyütme, biçim, sıkıştırma), öneri, kanıt, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız test; birebir alıntı + bağlantı) · UYGULAMA · ÖNERİ; aynı kaynağa dayanan iki iddia tek kanıt; firma tanıtımı ÖLÇÜLMÜŞ değildir. Listeler: (1) videoya göndermeden önce en çok 10 maddelik kare kabul listesi, her biri evet/hayır ya da yerel ölçümle; (2) başlangıç karesi için İngilizce görsel prompt iskeleti ve aynı çekimin video prompt iskeleti (yer tutucularla, kısa); (3) bağlantılı tam kaynak listesi. Belgede olmayan model özelliği, parametre ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
DÖRT FİLMİN KANITI (15.10.2026 QA):
  karede başlayıp videoda büyüyen: göğüste arma, bayrak, ikinci şerit · kapak menteşesi yönü · modülün biçimi · kokpitte su damlası
  videoda doğan: yüzün başka kadına dönmesi (C08) · 1 g yürüyüş · dumanlı alev · kıskacın koldan geçmesi · kolun 9 s donması
  ön plan eldiveni ile uzaktaki figür aynı düzlemde "temas" (perspektif) · aynı alet üç biçim
HATTAKİ: GPT_IMAGE_OMNI §6 "kare hareketten ÖNCEKİ an, temas ve hareket payı görünür" · §13 oran pikselden (1536×1024 = 3:2) ·
  Vertex resmî: I2V'de "Re-describe the character, the background, or the lighting depicted in the image." Not recommended (13 V15) ·
  Gemini uygulaması: "the aspect ratio will match your uploaded content" (11 V5) · Omni API'de ilk+son kare var, Gemini uygulamasında ∅ (13 V12)
  goruntu-yonetmeni: "Görüntüden videoya üretimde karede zaten olanı yeniden tarif etmek modeli kareden uzaklaştırır"
  hat çelişkisi: §3 ORTAK GÖRÜNÜM cümlesi her promptta birebir (görsel + video) ↔ "videoda karedekini yeniden anlatma"
CEVAPTAN BEKLENEN: kırpma mı genişletme mi · GPT Image imzalarının videodaki karşılığı · kimlik cümlesini video promptunda tekrarlamak yararlı mı zararlı mı ·
  kare kabulünde yerelde ölçülebilenler · karedeki yazı/işaretin videoya etkisi.
```
