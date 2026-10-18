# 🔬 12 — ÜRETİM HATALARI: DÖRT KILAVUZ İÇİN DÖRT DERİN ARAŞTIRMA PROMPTU (16.10.2026)

> **Durum:** ✅ KOŞULDU — 16.10.2026. Ham: `ham/27_REPLIK_KLIP_SESI_HAM.md` · `28_KIMLIK_REFERANS_HAM.md` ·
> `29_UZAY_FIZIGI_GORUNTU_HAM.md` · `30_SECIM_KURGU_HAM.md` · süzme: `13_SUZME_20261016.md` · kılavuzlar: `uretim_hatti/REPLIK_VE_KLIP_SESI_KILAVUZU.md` ·
> `KIMLIK_VE_REFERANS_KILAVUZU.md` · `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` · `SECIM_VE_KURGU_KILAVUZU.md`.
>
> **Neden:** `11_SUZME_20261016.md` §B. Yeni hattın dört filminde (15.10.2026 QA) aynı dört kusur ailesi görüldü ve hepsi
> metin aşamasında değil üretimde doğdu. Sahip 16.10.2026'da "önce şu 4 kılavuzu oluşturalım, bunun için 4 derin araştırma
> promptu hazırla" dedi.
>
> **Hedef ürünler** (her prompt bir kılavuzu besler):
>
> | # | konu | hedef kılavuz | dört filmdeki kanıt | okuyan |
> |:--:|---|---|---|---|
> | 1 | **REPLİK VE KLİP SESİ** — diyalog filme nasıl girer, istenmeyen klip sesi nasıl temizlenir | `uretim_hatti/REPLIK_VE_KLIP_SESI_KILAVUZU.md` | 3/3 kurgu kaydı filminde replik yok · 4/4 vakumda klip sesi | ses-tasarimcisi · diyalog-yazari · kurgucu · sahip |
> | 2 | **KİMLİK VE REFERANS** — yüz, giysi, şerit, rozet tutarlılığı; referans sayfası; ölçüm | `uretim_hatti/KIMLIK_VE_REFERANS_KILAVUZU.md` | 4/4 kimlik kayması, bayrak/arma eklenmesi | goruntu-yonetmeni · devamlilik · sahip |
> | 3 | **UZAY FİZİĞİ GÖRÜNTÜDE** — vakumda duman/damla/alev, 0 g hareket, itki yönü, Dünya hızı | `uretim_hatti/UZAY_FIZIGI_GORUNTU_KILAVUZU.md` | 3/4 duman-damla · 0 g'de yürüme · ters itki · hızlı Dünya | goruntu-yonetmeni · teknik-danisman · bilim-danismani |
> | 4 | **SEÇİM VE KURGU** — deneme seçimi, kesme sürekliliği, 10 s parçayı doldurma, yeniden üret mi kırp mı | `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` | C11↔C12 çelişkisi · eksen atlaması · 02:41 / 04:00 · her 10 s ses kopması | kurgucu · zincir-bekcisi · sahip · Fable (kare incelemesi) |
>
> **Depoda bugün olan (tekrar sorulmaz):** `GPT_IMAGE_OMNI_KILAVUZU.md` (16.10.2026) · `FLOW_GERCEKLERI.md` (Ek 2: Gemini uygulaması) ·
> `GECIS_VE_SES_SUREKLILIGI.md` · `GOSTERIM_COZUMLERI.md` · `BILINEN_TUZAKLAR.md` · eski hattın efor/yerçekimi kılavuzu (TUR 24; donmuş, okunur).
>
> **Nasıl koşulur:** 01-09 ile aynı kural. Her prompt tek başına çalışır; kod bloğunu derin araştırma aracına yapıştır, başka bir şey verme.
> Depo, film adı ve kanal adı verilmez. **SINAMA SETİ araca verilmez**; cevap gelince süzmede kullanılır.
>
> **Sıra:** dördü bağımsız. ⭐ 1 numara önce: en ucuz düzeltme ve hikâyenin anlaşılmasını en çok etkileyen. Sonra 4 (kurgu ve seçim kararlarının
> mekanik kısmı burada), sonra 2 ve 3.

---

# 1️⃣ REPLİK VE KLİP SESİ — diyaloğu filme sokmak, istenmeyen klip sesini temizlemek

```
Yapay zekâ ile üretilen kısa filmlerde diyaloğun ve klip sesinin nasıl yönetildiğini Ekim 2026 itibarıyla araştır. Üç bölüm var.
(A) VİDEO MODELİNİN KENDİ SESİ: Google'ın Gemini Omni 1.1 Flash modeli (Gemini uygulaması ve Google Flow) görselden video üretirken "yerel ses" üretiyor. Şunları bul: promptta birebir yazılan repliği doğru kelimelerle söyleme oranı, aynı karakterin sesinin ayrı kliplerde ne kadar benzer kaldığı, ses tarifinin (yaş, cinsiyet, telsiz filtresi) uyulma derecesi, konuşmacı kadrajda değilken ya da kasklıyken kadrajdaki kişinin ağzını oynatma eğilimi, istenmediği hâlde konuşma, mırıltı, müzik ya da ortam sesi ekleme sıklığı, "no speech / no music" gibi ifadelerin etkisi ve konuşmayı promptta yazma biçimi (tırnak, iki nokta). Google'ın resmî belgelerini (Gemini yardım, Flow yardım, Vertex/Gemini API video belgeleri, model kartı) ve yöntemi yazılı bağımsız testleri ayır. Veo 3/3.1 için bilinen bulguları Omni'ye taşınabilirliği belirterek ver.
(B) AYRI KAYIT: aynı karakter sesini film boyunca tutmanın yolları — metinden sese ve ses klonlama araçları (ElevenLabs, Google'ın kendi ses modelleri ve diğerleri), sentetik sesin ticari kullanım koşulları ve YouTube'un sentetik içerik bildirimi açısından durumu, oyuncu kaydı ile sentetik sesin izleyici algısı. Kask içi ses, telsiz, iç ses (voice-over) için kurgu tekniği: bant geçiren filtre değerleri, telsiz bipi ve hışırtı, kask içi yakınlık, kişileri sesle ayırt ettirme. Kelime/saniye konuşma hızı, 10 saniyelik bir parçaya sığan replik uzunluğu, repliğin kesmenin önünden ya da arkasından taşması (J/L kesme).
(C) İSTENMEYEN KLİP SESİNİ TEMİZLEMEK VE UZAY SES KURALI: kliple gelen sesi atıp yerine ortam yatağı koymak; açık kaynak kaynak ayırma araçlarının (Demucs, UVR ve benzerleri) yapay zekâ klip sesinden konuşmayı, müziği ve efekti ayırma başarısı; bir klipte konuşma olup olmadığını yerelde otomatik tespit etmek (ses etkinliği tespiti, Whisper gibi konuşmadan yazıya modellerle repliğin doğru söylenip söylenmediğini senaryoyla karşılaştırmak, kelime hata oranı); ffmpeg ile sessizlik ve yükseklik ölçümü. Vakumda ses: gerçekçi bilimkurgu filmlerinin (Gravity, The Expanse, Interstellar, 2001, First Man ve benzerleri) dış uzay sahnelerinde hangi sesleri neden duyurduğu — giysi ve gövde iletimi, kask içi nefes, telsiz, müzik — ve izleyicinin "uzayda ses" beklentisine dair kanıt.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir ses ve replik kılavuzudur. Filmler 2-16 dakikalık, yatay, fotogerçekçi yapay zekâ bilimkurgu filmleridir; çekim başına 10 saniyelik klipler; karakterler çoğunlukla kasklı astronotlardır; diyalog İngilizcedir ve çoğu telsizden ya da kask içinden gelir. Üretimi tek kişi yapar; ses stüdyosu ve oyuncu yoktur; kurgu ffmpeg tabanlı betiklerle ve bir kurgu programıyla yapılır. Asıl sorun şudur: "diyalog kurguda eklenecek" diye planlanan filmlerde kayıt hiç yapılmadan montaja geçiliyor. Bu yüzden yöntem kadar, tek kişilik üretimde diyaloğun montajdan önce hazır olmasını güvenceye alan iş sırası ve kontrol noktalarını da sor.
Çıktıyı üç tablo ve üç liste olarak ver: (a) MODEL SESİ tablosu — davranış (kelime doğruluğu, ses tutarlılığı, istenmeyen konuşma/müzik, ağız hareketi, prompt biçimi), bulgu, model ve sürüm, tarih, kaynak, etiket; (b) AYRI KAYIT tablosu — araç ya da teknik, ne çözer, kalite ve tutarlılık, ticari ve bildirim koşulu, maliyet, kaynak, etiket; (c) TEMİZLEME VE ÖLÇÜM tablosu — iş (sesi atma, ayırma, konuşma tespiti, replik doğrulama, yükseklik), araç ve tek satır yöntem, başarı ölçüsü, yerelde çalışır mı, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı, stüdyo ya da ajans pratiği) · ÖNERİ (senin çıkarımın). ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver, veremiyorsan ÖLÇÜLMÜŞ yazma; aynı kaynağa dayanan iki iddiayı iki kanıt sayma; firma tanıtım yazısını ÖLÇÜLMÜŞ sayma. Listeler: (1) film başında "model sesi mi, ayrı kayıt mı" seçimi için karar ölçütleri; (2) montajdan önce sesin hazır olduğunu gösteren en çok 8 kontrol, her biri evet/hayır; (3) bağlantılı tam kaynak listesi. Belgede olmayan model özelliği, oran, fiyat ya da filtre değeri uydurma.
```

### 🧪 SINAMA SETİ

```
DÖRT FİLMİN KANITI (15.10.2026 QA):
  3 film "replikler kurguda kaydedilecek" → 3'ünde de kayıt yapılmadı → hikâye anlaşılmadı
    (2 dk film: izleyici "Kopuk"; 4 dk filmler: "sabotaj mı tamir mi" belirsiz · "48 yolcu" bilgisi yalnız bitiş kartında)
  1 film model sesi (Omni, replikler promptta) → hikâye "baştan sona" anlaşıldı; AMA: iki erkek ses aynı tonda karıştı (00:11 ↔ 00:24),
    bir replikte kekeleme ("call— is calling"), alıcıdan gelen seste kadrajdaki kişinin dudağı aralık
  4/4 filmde vakumda klip sesi: metal çarpma, whoosh, rüzgâr, dalga, jet motoru; 2 dk filmde model hecesi ("anlamsız telsiz heceleri")
  1 filmde her 10 s'de ambiyans ve müzik sıfırlanıyor (yatak kurulmamış)
HATTAKİ KURAL: model sesi KAPALI (istisna: FILM §5 Kaynak = model sesi) · video promptunda konuşma/ses tarifi yasak
  (gerekçe: "No dialogue" yazılı promptta model yine konuşma üretti, filmde olmayan bir ad 9 raporda duyuldu)
  · kurgu.py klip_sesi + yataklar var ama montaj hat dışında yapıldı · SMOKE P18 (Omni ses tutarlılığı) koşulmadı
HAM 26 (sahibin kılavuzu): "Audio: ambience only; no speech or music" satırı öneriliyor · 2-2,5 kelime/s
CEVAPTAN BEKLENEN: Omni'nin replik doğruluğu ve ses tutarlılığına dair herhangi bir ölçüm · "no speech" ifadesinin etkisi ·
  tek kişilik üretimde ses klonlamanın ticari koşulu · Whisper ile replik doğrulamanın pratikliği · vakumda hangi seslerin
  kabul gördüğü · diyaloğu montajdan önce zorunlu kılan iş sırası.
```

---

# 2️⃣ KİMLİK VE REFERANS — yüz, giysi ve işaretlerin film boyunca tutması

```
Görsel ve video üretim modellerinde bir karakterin kimliğini (yüz, saç, yaş, beden) ve kostüm ayrıntılarını (renkli kol bantları, rozet, kask tipi, eldiven) bir film boyunca tutarlı tutmanın yollarını Ekim 2026 itibarıyla araştır. Üretim yolu: OpenAI'ın GPT Image görsel modelleri (ChatGPT ve API) ile referans görselleri ve her çekim için başlangıç karesi; Google'ın Gemini Omni 1.1 Flash modeli (Gemini uygulaması, Google Flow) ile bu kareden 10 saniyelik video. Karşılaştırma için Google'ın Nano Banana / Gemini görsel modellerini ve Flow'un "karakter" özelliğini de kapsa.
Şunları sor: (1) Referans biçimi: çok panelli karakter sayfası (önden, yandan, arkadan, yüz yakın, durum panelleri tek görselde) ile her görünüşün ayrı tek görsel olması — hangisi kimliği daha iyi taşır, model panelleri karıştırır ya da kareye birden fazla kopya koyar mı, belirli bir panele ("arka görünüş paneli") atıf işe yarar mı; kaç referansta verim düşer; referansa numara ve rol vermenin etkisi. (2) Kostüm ayrıntısının kayması: rengin kayması (turkuazın maviye dönmesi), şerit sayısının artması, göğse kendiliğinden arma, bayrak, yazı ya da logo eklenmesi — bunların bilinen nedenleri (modelin "astronot" ön bilgisi, ulusal ajans giysilerine benzeme), olumlu tarifle ve "yazı/logo/bayrak yok" dışlama satırıyla önleme kanıtı; OpenAI ve Google'ın resmî prompt rehberlerinin bu konudaki cümleleri. (3) Görselden videoya geçişte kayma: başlangıç karesi doğruyken video içinde yüzün, kaskın ya da giysinin değişmesi; hareket ve kamera karmaşıklığıyla ilişkisi; video modeline başlangıç karesinin yanında kimlik referansı da vermenin etkisi. (4) Kaybolan kimliği geri getirme: görsel düzenleme ile yerel düzeltme (yalnız yüzü ya da yalnız bandı değiştirme), tekrarlanan düzenlemelerde ayrıntı aşınması, kaç düzeltmeden sonra yeniden üretimin daha verimli olduğu. (5) Ölçüm: kimlik tutarlılığını yerelde, ücretsiz araçlarla sayıyla denetlemek — yüz gömme benzerliği (ArcFace / InsightFace), genel görsel benzerlik (CLIP, DINOv2), belirli bir bölgenin renk ölçümü (kol bandının renk tonu), kask içindeki ve kısmen görünen yüzde bu ölçümlerin güvenilirliği, yayımlanmış eşik değerler. Akademik tarafta kimlik koruyan üretim ve video kimlik tutarlılığı ölçütleri (benchmark) hakkında bulguları da topla.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kimlik ve referans kılavuzudur. Karakterler çoğunlukla beyaz basınç giysili, kasklı yetişkin astronotlardır; yüz bazen şeffaf vizör ardında görünür, bazen hiç görünmez; karakterler birbirinden çoğu zaman yalnız kol bandı rengi, rozet biçimi ve yüzle ayrılır. Film başına 2-4 karakter, 5-10 mekân/araç/nesne referansı, 12-96 çekim vardır. Üretimi tek kişi web arayüzlerinden yapar; ince ayar (LoRA, model eğitimi) yoktur, bunu gerektiren yolları "hat dışı" diye işaretle ama silme. Model sürümlerini ve tarihlerini açık yaz; eski bir sürüm için bulunan sonucu yeni sürüme genelleme.
Çıktıyı üç tablo ve üç liste olarak ver: (a) REFERANS BİÇİMİ tablosu — biçim (panel sayfası, tek görünüş, durum sürümü, metin kimlik bloğu, karakter özelliği), kimliği tutma bulgusu, bilinen yan etki, model ve sürüm, kaynak, etiket; (b) KAYMA tablosu — kayma türü (yüz, renk, şerit sayısı, arma/bayrak/yazı, kask, nesne biçimi), görsel aşamasında mı video aşamasında mı, bilinen neden, önleme yolu ve kanıtı, kaynak, etiket; (c) ÖLÇÜM tablosu — ölçüt, neyi yakalar, araç ve tek satır yöntem, kask/vizör koşulunda güvenilirlik, yayımlanmış eşik varsa değeri, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı; aynı kaynağa dayanan iki iddia tek kanıt; firma tanıtımı ÖLÇÜLMÜŞ değildir. Listeler: (1) başlangıç karesini videoya göndermeden önce en çok 10 maddelik kare kabul listesi, her biri evet/hayır ya da sayıyla; (2) "panel sayfası mı, tek görünüş mü" sorusunu tek kişinin az krediyle çözebileceği küçük bir deney tasarımı; (3) bağlantılı tam kaynak listesi. Belgede olmayan model özelliği, referans sayısı sınırı ya da eşik uydurma.
```

### 🧪 SINAMA SETİ

```
DÖRT FİLMİN KANITI (15.10.2026 QA): 4/4 filmde kimlik kayması
  2 dk film: C01'de kol şeridi yok → C02'de turuncu şerit · kask içinde bere var/yok · çift vizör çizgisi · kask lambası dev küreye dönüşüyor
  4 dk film A: aynı karakter C19'da sakalsız başka yüz · C20 göğüste hilal-yıldız arması · aynı alet üç farklı biçim (kutu, matkap, tüfek)
  4 dk film B: omuzluk lacivert → beyaz → lacivert · yanağa yeni yaralar · göğse yeni arma · kolda iki turuncu şerit
  4 dk film C (GPT Image → Gemini): kadın astronotun yüzü 3 farklı kadın · turkuaz şerit → mavi · göğüste yazılı arma · omuzda ABD bayrağı ·
    erkek pilotta ikinci turuncu şerit
  Hiçbir filmde hangi referansın gerçekten yüklendiği kayıtlı DEĞİL → "referans kullanılmadı" tahmindir
HATTAKİ KURAL (sahip, 10.10.2026): özne başına TEK çok panelli referans sayfası · promptta "Reference <No> (<rol>): take … from it,
  using the back-view panel" · SMOKE P15 (anahtar cümle) ve P17 (panel ↔ tek görünüş) KOŞULMADI
HATTAKİ KURAL: olumsuz blok yok (gerekçe Veo/Runway) · OpenAI resmî: "State exclusions such as unwanted text, logos, or watermarks."
HAM 26: "çok panelli kart tasarımı incelemek içindir; video girdisi olarak kullanma" · durum sürümleri ayrı dosya (HATCH_CLOSED/OPEN)
CEVAPTAN BEKLENEN: panel sayfasının tek görünüşe göre ölçülmüş bir farkı var mı · bayrak/arma kendiliğinden ekleniyorsa nedeni ve önlemi ·
  kask altında yüz benzerliği ölçülebilir mi · P17'nin daha ucuz bir tasarımı.
```

---

# 3️⃣ UZAY FİZİĞİ GÖRÜNTÜDE — vakum, ağırlıksızlık ve yörünge hareketi

```
Yapay zekâ video modellerinin uzay ve yörünge sahnelerinde yaptığı fizik hatalarını ve bunları önlemenin yollarını Ekim 2026 itibarıyla araştır. İki bölüm var.
(A) GERÇEK FİZİK — her biri için kısa, kaynaklı bir referans ver ve kameraya nasıl yansıdığını yaz: vakumda roket ve tepki kontrol iticisi (RCS) alevinin görünümü (saydam ya da görünmez çekirdek, kısa parlama, genişleyen soluk bulut, duman ve ateş topu olmaması; yakıta göre fark); vakumda ve ağırlıksızlıkta sıvının davranışı (yüzey gerilimiyle küre, yüzeye yapışma, kaynama/buharlaşma; damlanın "aşağı düşmemesi"); ağırlıksızlıkta toz, kıvılcım, buz ve parçacık hareketi; uzay yürüyüşünde (EVA) hareket — tutamaktan tutamağa ilerleme, ayak kilidi, emniyet bağı, tepki kuvveti (bir şeyi itince bedenin geri gitmesi), kütle ve atalet; itki yönü ile hareket yönünün ilişkisi; alçak yörüngeden Dünya'nın görünür kayma hızı (yer izinin saniyede kaç kilometre aktığı, 10 saniyede kadrajda ne kadar hareket görüneceği; gündüz-gece sınırının ne hızla geçtiği); kenetlenme hızları ve temas davranışı; kokpit ve basınçlı kabin içinde ivme anında bedenin tepkisi. Kaynak olarak NASA, ESA ve uzay ajanslarının eğitim ve görev belgelerini, gerçek EVA ve kenetlenme görüntülerinin açıklamalarını ve fizik ders kaynaklarını kullan.
(B) MODEL HATALARI VE ÖNLEME — yapay zekâ video modellerinin (Veo 3/3.1, Gemini Omni, Sora, Kling, Runway ve diğerleri) fizik değerlendirme çalışmalarındaki (VideoPhy, PhyGenBench, Physics-IQ ve benzerleri) bulguları: hangi fizik türlerinde en çok hata yapıyorlar (akışkanlar, yerçekimi, temas, momentum), uzaya özgü bulgu var mı. Uygulayıcı tarafında: vakumda istenmeyen duman, damla, alev bulutu, 1 g yürüme ve ters itkiyi çağıran prompt kelimeleri; bunları olumlu tarifle önlemenin yolları ("clean narrow blue-white thrust line", "hand-over-hand along the rail" gibi); başlangıç karesinin bu hataları ne kadar belirlediği; olumsuz ifadenin ("no smoke") bu modellerde ters etki yapıp yapmadığına dair kanıt; hatanın görünmemesi için kadraj ve kurgu çözümleri (kesme, kadraj dışı bırakma, sonucu gösterme). Ayrıca bilimkurgu sinemasının bu konularda nerede bilerek gerçeklikten saptığını ve izleyicinin neyi "yanlış" algıladığını ayır: izleyicinin fark ettiği hata ile yalnız uzmanın fark ettiği hata.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir "uzay fiziği görüntüde" kılavuzudur. Filmler fotogerçekçi, yatay, 10 saniyelik çekimlerden oluşan yapay zekâ bilimkurgu filmleridir; sahneler çoğunlukla alçak yörünge, istasyon dışı, kenetlenme, EVA ve kokpit içidir. Kılavuz bir bilim makalesi değildir: her fizik kuralı için "görüntüde nasıl görünür" ve "promptta nasıl tarif edilir" cümlesi gerekir. Kurgusal teknolojiyi (yapay yerçekimi, bilinmeyen sıvı) reddetme; yalnız filmin kendi kurduğu kurala tutarlılık iste. Sayısal değerleri birimleriyle ve kaynağıyla ver.
Çıktıyı üç tablo ve üç liste olarak ver: (a) FİZİK tablosu — olgu, gerçek davranış (sayıyla), kamerada nasıl görünür, sık yapılan görsel hata, kaynak, etiket; (b) MODEL HATASI tablosu — hata türü, hangi modellerde ve hangi çalışmada, çağıran kelime ya da durum, önleyen olumlu tarif ya da kadraj, kanıt, kaynak, etiket; (c) İZLEYİCİ tablosu — hata, sıradan izleyici fark eder mi, kanıt (anket, yorum analizi, eleştiri), kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı; aynı kaynağa dayanan iki iddia tek kanıt. Listeler: (1) bir başlangıç karesi ve video promptu için en çok 10 maddelik "uzay fiziği" kontrol listesi, evet/hayır; (2) promptta kaçınılacak kelimeler ve yerine yazılacak olumlu ifadeler (İngilizce); (3) bağlantılı tam kaynak listesi. Belgede olmayan sayı, model sürümü ya da çalışma sonucu uydurma.
```

### 🧪 SINAMA SETİ

```
DÖRT FİLMİN KANITI (15.10.2026 QA):
  vakumda istasyon ağzından siyah baca dumanı · kararan cephe volkanik kül gibi · roket alevi "dumanlı kamp ateşi" (2 film)
  kenetlenme halkasından 1 g'de aşağı damlayan sıvı · kapalı kokpitte tavandan su damlaması · duvardaki kablodan su damlası
  gemi kendi motor ateşinin yönüne kayıyor (ters itki) · mekik iticisiz asansör gibi yükseliyor
  astronot 0 g'de 1 g gibi yürüyor/basıyor (3 çekim) · kapağı açarken diz çöküyor, tepki kuvveti yok · ayrılma kolu çekişinde efor yok
  ateşlemede kokpitte ivme tepkisi yok · Dünya 6 saniyede gece-gündüz çizgisi geçecek hızda dönüyor · ön plan eldiveni ile uzaktaki
  küçük figür aynı düzlemde temas (perspektif)
HATTAKİ: BILINEN_TUZAKLAR · GOSTERIM_COZUMLERI · eski hattın efor/yerçekimi kılavuzu (TUR 24, donmuş) · bilim-danismani yalnız
  FIZIK_IDDIASI=var filmde çağrılıyor (4 filmin 3'ünde "yok" denmişti) · "olumsuz ifade ters etki yapar mı" SMOKE P13 koşulmadı
CEVAPTAN BEKLENEN: alçak yörüngeden 10 s'de Dünya'nın gerçek kayma miktarı · vakum alevinin olumlu İngilizce tarifi ·
  sıvı/damla için doğru tarif · fizik benchmark'larında uzaya en yakın bulgular · izleyicinin gerçekten fark ettiği hatalar.
```

---

# 4️⃣ SEÇİM VE KURGU — denemeden filme: seçmek, bağlamak, süreyi doldurmak

```
Yapay zekâ ile üretilen kısa filmlerde denemelerin seçilmesi ve filmin kurgulanması için yöntemleri Ekim 2026 itibarıyla araştır. Dört bölüm var.
(A) SEÇİM: her çekim için birden çok video denemesi üretildiğinde kullanılabilir aralığın (giriş-çıkış saniyesi) nasıl belirlendiği; denemenin tek başına değil sonraki ve önceki planla birlikte değerlendirilmesi; "yeniden üret / kırp / başlangıç karesini düzelt / kesmeye ya da ara plana çevir / olduğu gibi kullan" kararını veren ölçütler ve maliyet hesabı (deneme başına kredi, seçilen kullanılabilir saniye başına maliyet). Yapay zekâ film yapımcılarının ve küçük stüdyoların yayımlanmış iş akışlarından (blog, konuşma, vaka anlatımı) ve sinema kurgusunun klasik pratiğinden (script supervisor notları, dailies, kurgucunun seçim notları) topla.
(B) KESME SÜREKLİLİĞİ: 180 derece kuralı ve ekran yönü, bakış yönü eşleşmesi, nesne durumu sürekliliği (açılan kapağın sonraki planda kapalı olmaması, iki planın birbirini yalanlaması), ışık yönü ve renk sürekliliği; kesmede ses sürekliliği (ortam yatağının kesintisiz sürmesi, J/L kesme, çapraz geçiş süreleri); bir hatayı yeniden üretmeden örtmenin kurgu yolları (ara plan, tepki planı, insert, kesme noktasını kaydırma, hız değişimi sınırları).
(C) SABİT SÜRELİ PARÇA: film her biri 10 saniyelik parçalardan oluşmak zorundaysa ama denemelerin kullanılabilir kısmı 10 saniyenin altında kalıyorsa — devam üretimi, sahne uzatma, aynı çekimin iki denemesini birleştirme, sonuç planı ekleme gibi yollar; ritmi bozmadan süre doldurmanın sınırları; yavaşlatma ve döngünün izleyicide fark edilme eşiği; tersine, sabit 10 s ızgaranın kurgu ritmine etkisi ve 10 saniyede kaç görsel değişim gerektiğine dair kanıt.
(D) OTOMATİK VE YAPAY ZEKÂ DESTEKLİ KONTROL: ffmpeg ve Python ile yerelde yapılabilen kontroller — çekim sınırı tespiti (PySceneDetect), donmuş kare ve gizli kesme tespiti, iki planın kesme noktasındaki karelerinin SSIM/PSNR/histogram farkı, renk eşleşmesi, ses seviyesi ve sessizlik tespiti; videodan saniyede bir kare çıkarıp çok kipli bir dil modeline (görsel okuyabilen yapay zekâ) göstererek süreklilik ve kimlik hatası yakalamanın güvenilirliği — hangi hata türlerini yakalar (kimlik, nesne, yazı, duman), hangilerini kaçırır (bir saniyeden kısa bozulma, hareketin doğallığı, ayak kayması, zamanlama), yanlış alarm oranı, Gemini gibi modellerin video anlama değerlendirmelerinde (zamansal akıl yürütme, kısa olay tespiti) bilinen sınırları ve kare örnekleme hızının etkisi.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir seçim ve kurgu kılavuzudur. Filmler 2-16 dakikalık, yatay, fotogerçekçi yapay zekâ bilimkurgu filmleridir; çekim başına 10 saniye kuralı vardır (değiştirmeyi önerme; kanıt varsa ayrı satırda belirt). Üretimi ve kurguyu tek kişi yapar; kurgu bir JSON zaman çizelgesinden ffmpeg ile taslak üreten betiklerle ve bir kurgu programıyla yapılır; ilk kontrolü videoyu doğrudan izleyemeyen, yalnız çıkarılmış kareleri ve ölçümleri okuyabilen bir yapay zekâ asistanı yapar, son karar insanındır. Bu yüzden her kontrol için "kareden görülebilir mi, ölçümle mi yakalanır, yoksa insanın normal hızda izlemesi mi gerekir" ayrımını açık yaz.
Çıktıyı üç tablo ve üç liste olarak ver: (a) KARAR tablosu — durum (kullanılabilir aralık kısa, kimlik hatası, nesne durumu çelişkisi, eksen atlaması, istenmeyen ses, donan son kısım vb.), önerilen karar (kullan, kırp, kareyi düzelt, yeniden üret, kesmeye/ara plana çevir), gerekçe ve maliyet, kaynak, etiket; (b) SÜREKLİLİK tablosu — kontrol, neyi yakalar, kurgu ya da üretim çözümü, kaynak, etiket; (c) OTOMATİK KONTROL tablosu — kontrol, araç ve tek satır yöntem, yakaladığı ve kaçırdığı, kareden mi ölçümden mi insandan mı, yayımlanmış eşik ya da doğruluk varsa değeri, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı; aynı kaynağa dayanan iki iddia tek kanıt; firma tanıtımı ÖLÇÜLMÜŞ değildir. Listeler: (1) bir taslak filmi izleyiciye göstermeden önce en çok 10 maddelik kontrol listesi, evet/hayır; (2) "yeniden üret mi, kurguda çöz mü" için tek sayfalık karar ağacı; (3) bağlantılı tam kaynak listesi. Belgede olmayan araç özelliği, eşik ya da doğruluk oranı uydurma.
```

### 🧪 SINAMA SETİ

```
DÖRT FİLMİN KANITI (15.10.2026 QA):
  2 dk film: C11'de iki astronot çarpışıp istasyondan uzağa savruluyor → C12'de korkulukta → izleyici "son iki sahne birbirini yalanladı",
    tek kelime "Kopuk" (SEÇİM hatası: doğru deneme yerine savrulma denemesi kullanıldı) · C07 ortasına plansız 3 s'lik istasyon duvarı
  4 dk film C: montaj 02:41, hedef 04:00 (çekimler 2-5 s'ye kırpılmış) · C05→C06 ve C11→C12 180° atlaması (araçlar yer değiştiriyor) ·
    C17 sağ el → C18 yakın planda sol el · C12'de kol 9 s hareketsiz (donan kısım)
  4 dk film A: her 10 s'de ambiyans ve müzik sıfırlanıyor · kilit sesi görüntüden 2 s geç
  4 dk film B: müzik kesmede bıçak gibi kesiliyor
SÜREÇ: üretim ve montaj hattın klasörleri ve timeline.json dışında yapıldı · NOTLAR DENEMELER/İŞARETLEME boş ·
  "dış izleyici" satırları en az 2 filmde AI simülasyonu
HATTAKİ ARAÇLAR: kurgu.py (kontrol · liste · taslak · yukseklik; gecis, yataklar, klip_sesi) · kareler.py (cikar · dikis SSIM/PSNR · kuyruk
  donma/gizli kesme) · Gemini taraması 1 fps örnekler (1 s'den kısa kusur kaçabilir) · GECIS_VE_SES_SUREKLILIGI (karışım 0,3-0,8 · karartma 0,5-1,5)
HAM 26: "Seçim ekranında normal hızda izle, hemen ardından sonraki planla birlikte izle" · usable_in/usable_out kaydı · 4 dk için ~30 kaynak
CEVAPTAN BEKLENEN: kare tabanlı yapay zekâ incelemesinin gerçekten yakaladığı ve kaçırdığı hata türleri · 10 s parçayı doldurmanın
  kabul gören yolları · ara planla örtme pratiği · kesme noktası SSIM eşiği için yayımlanmış bir değer var mı · taslak öncesi kontrol listesi.
```
