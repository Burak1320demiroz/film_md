# 🔬 09 — KAPAK VE BAŞLIK: GENEL KILAVUZ İÇİN BEŞ DERİN ARAŞTIRMA PROMPTU (12.10.2026)

> **Durum:** ✅ KOŞULDU — 12.10.2026. Ham: `ham/21_KAPAK_YUZEY_HAM.md` · `22_KAPAK_OKUNURLUK_HAM.md` · `23_KAPAK_BASLIK_YAZI_HAM.md` · `24_KAPAK_URETIM_HAM.md` · `25_KAPAK_TEST_ESKI_VIDEO_HAM.md` · süzme: `10_SUZME_20261012.md` · kılavuz: `uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md`.
>
> **Neden:** sahip 12.10.2026'da kanalın tıklama oranı dökümünü ve bir model cevabını yapıştırdı. Ardından "bir de bunun için 5 adet araştırma promptu yazalım" dedi. Amaç `07` ile aynı: her yeni filme uygulanan genel bir kılavuz.
>
> **Hedef ürün:** genel bir kapak ve başlık kılavuzu, taslak adıyla `uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md`. Film adı taşımaz, her format için geçerlidir. kapak-tasarimcisi, yayin, izleyici (küçük boy testi), yonetmen ve senarist ajanları onu okur. Mekanik kısmı `kareler.py kucult` ve bir kapak denetimine iner.
>
> **Bu araştırmalar kılavuzu yazmaz.** Kılavuz, süzülmüş dış kaynak ve kanalın kendi tıklama verisiyle yazılır. Her promptun cevabı kılavuzun bir bölümünü besler:
>
> | # | konu | kılavuzda doldurduğu bölüm | okuyan ajanlar |
> |:--:|---|---|---|
> | 1 | **YÜZEYE GÖRE KAPAK** — önerilen videolar, ana sayfa, arama, televizyon; kapak hangi boyda, kimin yanında görünür | §1 Yüzeyler ve boyutlar · §2 Önerilen videolar kutusu | kapak-tasarimcisi · yayin |
> | 2 | **KÜÇÜK BOYDA OKUNURLUK** — tek odak, kontrast, renk, yazı; kuralı ölçülebilir kontrole çevirmek | §3 Okunurluk kuralları · §4 Mekanik kapak denetimi | kapak-tasarimcisi · izleyici · `kareler.py` |
> | 3 | **BAŞLIK İLE KAPAK BİRLİKTE** — merak cümlesi, kapak yazısı, film adı, anadili İngilizce olmayan okur | §5 Başlık kalıbı · §6 Kapak yazısı | yayin · senarist · kapak-tasarimcisi |
> | 4 | **KAPAĞIN ÜRETİMİ** — filmden kare mi, ayrı üretim mi; görsel modelle kapak; yanıltıcılık sınırı | §7 Üretim yolu ve vaat sınırı | kapak-tasarimcisi · goruntu-yonetmeni · cekim-yaz §F7 |
> | 5 | **TEST, OKUMA VE ESKİ VİDEOLAR** — kapak testi kararları, tıklama oranını gösterim hacmiyle okumak, zayıf eski videoları kurtarmak | §8 Test ve karar kuralları · §9 Eski video bakımı | yayin · paketleme §F9-§F10 |
>
> **Depoda bugün olan (kılavuzun çıkış noktası):**
> - `05/3` kapak öğelerinin genel etkisini sordu: yüz, ifade, metin, kontrast, tek odak, renk, ölçek, başlık türü, çok dilli erişim. `06_SUZME` bunların çoğunu "uygulama düzeyi" ya da "NOT" buldu. Bu dosya o soruları tekrarlamaz.
> - `07/2` kapaktaki vaadin ilk 30 saniyede teslimini soruyor. Bu dosya vaat-açılış bağını tekrarlamaz.
> - `apexaic/DIS_SAYILAR.md` §1: kapak boyutu, kapak testi (en çok 3 seçenek, izlenme süresi payıyla seçer), tıklama oranında evrensel eşik olmadığı.
> - `uretim_hatti/IZLEYICI_VERISI.md`: tıklama oranının nereden alınacağı ve kayıt tablosu.
> - kapak-tasarimcisi ajanının sekiz kuralı. Bunlardan biri doğrudan sınanacak: ajan "final kapak filmin gerçek karesinden" diyor, yapıştırılan öneri "kapağı filmden kare alarak değil ayrı üretin" diyor.
> - Eski hattın `FILM_KAPAGI_KILAVUZU`, `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU` ve `PAKETLEME_VE_VAAT_KILAVUZU` dosyaları. Donmuş hattın parçasıdır; okunur, düzenlenmez.
> - **Yeni olan:** kanalın trafik kaynağına göre tıklama oranı ve video video gösterim dökümü (sahibin yapıştırdığı metin, 12.10.2026). Bu veri araca verilmez, süzmede kullanılır.
>
> **Nasıl koşulur:** 01, 03, 05 ve 07'deki kuralla aynı.
> - Her prompt tek başına çalışır. Kod bloğunu derin araştırma aracına yapıştır, başka bir şey verme.
> - Depo, film adı ve kanal adı verilmez. Emsal kanal adları dış bilgi olduğu için promptta kalabilir.
> - **SINAMA SETİ araca verilmez.** Cevap gelince süzmede kullanılır.
>
> **Sıra:** beşi bağımsız. ⭐ 1 numara önce koşulsun: kanalın gösterimlerinin çoğu önerilen videolardan geliyor ve en düşük tıklama oranı orada. Sonra 5 gelsin: en çok gösterim alan zayıf eski videolar bugün kurtarılabilecek tek hazır kaynak.
>
> **Sahibin yapıştırdığı öneri metni** araştırılacak iddialar listesidir, kanıt değildir. İddialar her promptun SINAMA SETİ'nde ayrı satırda durur.

---

# 1️⃣ YÜZEYE GÖRE KAPAK — önerilen videolar kutusu, ana sayfa, arama ve televizyon

```
YouTube'da bir uzun videonun kapağının (küçük resim) her gösterim yüzeyinde nasıl göründüğünü ve tıklama oranının yüzeye göre neden değiştiğini Ekim 2026 itibarıyla araştır. Yüzeyler: ana sayfa akışı, izleme sayfasındaki önerilen videolar (masaüstünde sağ sütun, mobilde videonun altı), sıradaki otomatik oynatma, arama sonuçları, abonelik akışı, bitiş ekranı, kanal sayfası, televizyon uygulaması ve gömülü oynatıcı. Her yüzey için şunları bul: kapağın gerçek görüntülenme boyutu piksel olarak (mobil, masaüstü, tablet, televizyon), kapağın yanında başka hangi öğelerin durduğu (başlık satır sayısı, kanal adı, süre rozeti, izleme ilerleme çubuğu, "yeni" ve benzeri etiketler), koyu ve açık arayüz farkı, üzerine gelince ya da akışta sessiz oynatmanın kapağı ne kadar süre sonra videoya çevirdiği ve bu önizlemenin gösterim ile tıklama sayımına etkisi. YouTube'un resmî açıklamalarını (Yardım sayfaları, Creator Insider, YouTube blogu, tasarım duyuruları) ve 2024-2026 arayüz değişikliklerini tarihle ver.
Önerilen videolar yüzeyini ayrıca derinlemesine sor: bu yüzeyde izleyicinin karar anı nasıl işler (zaten bir video izliyor, yan sütunda birçok benzer kapak var), göz izleme ya da tıklama çalışmalarında yan sütundaki kapaklara ayrılan bakış süresi, kapağın izlenen videoya benzemesinin mi yoksa yanındakilerden ayrışmasının mı işe yaradığına dair kanıt, aynı türden (bilimkurgu kısa film) çok sayıda kapakla yan yana durmanın etkisi. Trafik kaynağına göre tıklama oranının neden farklı olduğunu YouTube'un kendi açıklamasıyla ver: hangi yüzeyde oran doğal olarak düşük çıkar, gösterim genişledikçe oran neden düşer, küçük gösterimde yüksek oranın neden yanıltıcı olduğu. Yüzeye göre tipik tıklama oranı aralığı yayımlayan kaynakları topla, örneklemini ve yöntemini yaz, YouTube'un "evrensel eşik yoktur" ifadesiyle çelişkilerini işaretle.
Kritik kısıt: kullanım yeri, bir kanalın her yeni filmine uygulanan GENEL bir kapak kılavuzudur. Kanal küçüktür (birkaç bin abone), fotogerçekçi yapay zekâ bilimkurgu kısa filmleri yayımlar (2-16 dakika, yatay); izleyicinin çoğu Hindistan, Türkiye, Endonezya ve Özbekistan'dandır ve gösterimlerin çoğu önerilen videolar yüzeyinden gelir. Kapak tek bir görsel olarak yüklenir; yüzeye göre farklı kapak yüklemek mümkün değilse bunu açıkça söyle ve tek görselin bütün yüzeylerde çalışması için ne gerektiğini yaz. Mobil cihaz oranını o ülkeler için ayrı veriyle ver; veri yoksa küresel veriyi o ülkelerinmiş gibi sunma.
Çıktıyı iki tablo ve üç liste olarak ver: (a) YÜZEY tablosu — yüzey, cihaz, kapağın piksel boyutu, yanındaki öğeler, koyu ve açık arayüz, önizleme davranışı, tarih, kaynak, etiket; (b) TIKLAMA ORANI tablosu — yüzey ya da trafik kaynağı, tipik aralık (varsa), örneklem ve yöntem, oranı düşüren ya da yükselten bilinen etken, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (yaratıcı, ajans ya da danışman raporu) · ÖNERİ (senin çıkarımın) olsun. ÖLÇÜLMÜŞ dediğin her satıra birebir alıntı ve bağlantı ver; veremiyorsan o satırı ÖLÇÜLMÜŞ yazma. Ekran görüntüsünden ölçtüğün piksel boyutlarını tarih ve cihazla "UYGULAMA" diye işaretle. Aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) önerilen videolar kutusunda çalışan kapak için en çok 6 kural, her biri tek cümle ve etiketli; (2) kapağın denetlenmesi gereken en küçük boy ya da boylar ve gerekçesi; (3) bağlantılı tam kaynak listesi. Belgede olmayan piksel değeri, oran ya da tarih uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bunları açıklamalı

```
KANALIN VERİSİ (sahibin yapıştırdığı döküm, 12.10.2026; tarih aralığı BİLİNMİYOR):
  toplam gösterim ≈1,11 M · önerilen videolar 671 B gösterim (≈%60) · tıklama oranı %2,39
  ana sayfa %4,42 · arama %3,76
DIŞ SAYI (DIS_SAYILAR §1): tıklama oranında evrensel eşik YOK, karşılaştırma kendi benzer videolarınla ·
  gösterim = kapak 1 saniyeden uzun ve en az %50 görünür (answer/7577430) · kapak 3840×2160 önerilir
HATTAKİ KONTROL: kapak-tasarimcisi faz 9'da 320×180 ve 160×90 (`kareler.py kucult`), gri tonlama, açık ve koyu arayüz
  → 160×90 gerçek bir yüzey boyutu mu, yoksa tahmin mi?
06_SUZME: "göz atma %2-5, arama %5-15" aralığı RED (resmî kaynakla çelişiyor)
SAHİBİN YAPIŞTIRDIĞI ÖNERİDEKİ İDDİALAR (doğrulanacak):
  "önerilen videolar = küçücük kutu, başka bilimkurgu kapaklarıyla yan yana" · "koyu mavi kapak karanlık modda kaybolur"
  · "sağ alt köşe süre rozetiyle kapanır" · "az gösterimde oran doğal olarak yüksek çıkar"
CEVAPTAN BEKLENEN: önerilen videolar kutusunun gerçek boyu · bu yüzeyde %2,39 düşük mü, beklenen mi ·
  ayrışma mı benzerlik mi · kapağın hangi boylarda denetleneceği.
```

---

# 2️⃣ KÜÇÜK BOYDA OKUNURLUK — tek odak, kontrast, renk ve yazıyı ölçülebilir kontrole çevirmek

```
Küçük boyda gösterilen bir görselin (video kapağı) bir bakışta anlaşılmasını sağlayan görsel algı ilkelerini ve bunları otomatik olarak ölçmenin yollarını Ekim 2026 itibarıyla araştır. Algı tarafında şunları topla: bir akışta tek bir kapağa ayrılan bakış süresi (göz izleme çalışmaları, milisaniye ya da saniye olarak), bu sürede kaç nesnenin ve kaç kelimenin işlenebildiği, figür-zemin ayrımı, görsel dikkat çekicilik (saliency), parlaklık kontrastı ile renk kontrastının ayrı etkileri, karmaşıklık ve ayrıntı yoğunluğunun küçültülünce "lekeye" dönüşmesi, renk körlüğü ve gri tonlamada okunurluk, koyu ve açık arka plan üzerinde algı. Kanıtı görsel algı ve reklam araştırmalarından, arayüz ve tipografi çalışmalarından, akış platformlarının kapak çalışmalarından (Netflix sanat eseri araştırmaları dahil) al ve her birinin video kapağına taşınabilirliğini yaz.
Ölçüm tarafında şunu sor: bu ilkeler bir komut satırı aracıyla (ffmpeg, Python görüntü kütüphaneleri) hangi sayılarla ölçülebilir? Örnekler: küçültülmüş görselde öznenin alanı ve konumu, özne ile arka plan arasındaki parlaklık farkı ya da kontrast oranı, kenar yoğunluğu ya da görsel karmaşıklık ölçütü, baskın renk sayısı, açık kaynak dikkat çekicilik haritası modelleri ve bunların insan bakışıyla uyumu, kapak yazısının küçük boyda kaç piksel yüksekliğe düştüğü ve okunur kalan en küçük harf boyu. Her ölçüt için yayımlanmış eşik ya da referans değer varsa kaynağıyla ver, yoksa "eşik yok, kanalın kendi kapaklarında kalibre edilir" de. Kapak yazısını ayrıca sor: kaç kelime, hangi yazı ağırlığı, kontur ya da gölge, büyük harf, görselin hangi bölgesinde; yazının tıklamaya etkisine dair ölçüm var mı.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kapak kılavuzudur ve mekanik bir kapak denetimidir. Kapaklar yapay zekâ görsel modeliyle üretilen fotogerçekçi bilimkurgu görselleridir; bu modeller çok ayrıntılı, geniş manzaralar ve koyu mavi-camgöbeği tonlar üretmeye eğilimlidir. Karakterler çoğunlukla basınç giysili ve kasklıdır; yüz bazen şeffaf vizör ardında görünür, bazen tamamen gizlidir. Kapak yazısı görsel modelle değil, sonradan ayrı bir katman olarak eklenir. Ücretli göz izleme ya da kapak puanlama hizmeti yoktur; bunları gerektiren yolları "hat dışı" diye işaretle ama silme, ücretsiz ve yerel çalışan ölçümleri öne al.
Çıktıyı iki tablo ve üç liste olarak ver: (a) ALGI tablosu — ilke, bulgu, sayı (bakış süresi, nesne ya da kelime sayısı), bağlam (durağan reklam, akış, arayüz), video kapağına taşınabilirlik, kaynak, etiket; (b) ÖLÇÜT tablosu — ölçüt, neyi yakalar, nasıl hesaplanır (araç ve tek satır yöntem), yayımlanmış eşik varsa değeri, insan algısıyla uyum kanıtı, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) kapak için en çok 8 okunurluk kuralı, her biri ölçülebilir ya da evet/hayır ile kontrol edilebilir biçimde; (2) yerel çalışan bir kapak denetimi için önerilen ölçüm sırası ve her adımın çıktısı; (3) bağlantılı tam kaynak listesi. Belgede olmayan eşik, kütüphane özelliği ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN VERİSİ: en zayıf dört video — THE_LAST_ARCHIVE 99 B gösterim %1,07 · HEIR_OF_ASHES 44 B %1,04 ·
  "Why Solar Panels…" 41 B %1,63 · THE_HERD 29 B %1,74 (kapak görselleri depoda YOK; sahipten ekran görüntüsü gerekir)
HATTAKİ KURALLAR (kapak-tasarimcisi): küçük boyda okunan tek ilişki ("iki leke ve aradaki boşluk") · 2-3 ana renk ·
  karenin %30-40'ı boş alan · gri tonlamada da okunur · sağ alt köşe ve alt şerit boş · promptta yazı yok
  → bunların hiçbiri bugün sayıyla ölçülmüyor; elde yalnız `kareler.py kucult` var
SAHİBİN YAPIŞTIRDIĞI ÖNERİDEKİ İDDİALAR (doğrulanacak):
  "tek odak noktası: tek insan ya da tek dev nesne" · "geniş, detaylı yapay zekâ manzaraları küçük boyda leke olur"
  · "koyu arka plan + parlak özne + tek vurgu rengi (lacivert/siyah üstünde turuncu ya da kırmızı)"
  · "en fazla 2-4 kelime" · "telefonda en küçük boyda 1 saniyede anlaşılıyor mu" · "gri tonlamada özne ayrılıyor mu"
CEVAPTAN BEKLENEN: kural başına ölçüt ve (varsa) eşik · yazı için en küçük okunur piksel boyu · ücretsiz
  dikkat çekicilik modeli insan bakışını ne kadar öngörüyor · kareler.py'ye eklenecek denetimin adımları.
```

---

# 3️⃣ BAŞLIK İLE KAPAK BİRLİKTE — merak cümlesi, kapak yazısı ve film adı

```
YouTube'da kurgusal kısa filmler için başlık ile kapağın birlikte nasıl çalıştığını Ekim 2026 itibarıyla araştır. Şunları sor: başlık ile kapak yazısının aynı şeyi tekrar etmesi ile birbirini tamamlaması arasındaki farka dair ölçüm ya da yöntemi yazılı deney; "merak cümlesi | FİLM ADI" kalıbı (örneğin bir olayın ilginç tarafını söyleyen cümle, sonra filmin adı) ile "FİLM ADI | Sci-Fi Short Film" kalıbının karşılaştırması; bilgi boşluğu (merak açığı) kuramı ve tıklama tuzağı tespit çalışmalarının, merakı tuzağa çevirmeden kurmak için ne söylediği; başlığın mobilde, masaüstünde, önerilen videolar sütununda ve televizyonda kaç karakterde kesildiği ve ilk kaç kelimenin görünür kaldığı; YouTube'un yanıltıcı meta veri ve tıklama tuzağı politikası ile bu politikanın 2024-2026'daki uygulaması. Kapak yazısını ayrı sor: kapakta yazı olmalı mı, kaç kelime, soru mu iddia mı uyarı mı, filmin adını içermeli mi, başlığa ne eklemeli.
Anadili İngilizce olmayan izleyici açısından ayrıca sor: Hindistan, Türkiye, Endonezya ve Özbekistan'daki izleyici için İngilizce başlık ve kapak yazısında kelime seçimi (sık kullanılan, kısa kelimeler; deyim ve kelime oyunu riski), YouTube'un otomatik başlık çevirisinin ne zaman ve hangi izleyiciye gösterildiği, çevirinin merak cümlesini nasıl bozduğu, çok dilli başlık eklemenin ölçülmüş etkisi, kapak yazısının çevrilememesinin sonucu. Film adlarını da sor: kısa film adının kendi başına anlam taşıması gerekir mi, seri adı ya da numaralandırma etkisi, aynı kanalda tutarlı başlık biçiminin keşfe etkisi.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir başlık ve kapak yazısı kılavuzudur. Kanal küçüktür, fotogerçekçi yapay zekâ bilimkurgu kısa filmleri yayımlar; başlık, açıklama ve kapak yazısı İngilizcedir; her filmin kısa, İngilizce bir adı vardır. Kanal kuralı olarak başlıkta "AI" ve üretim aracı adı kullanılmaz ve "Stunning, Epic, Mind-Blowing" türü abartı sözcükleri yasaktır; bu kuralları değiştirmeyi önerme, yalnız kanıt varsa ayrı satırda belirt. Yanıltıcı başlık önerilerini kanal sağlığı riskiyle birlikte yaz. Arama niyetli başlıklar (bilim sorusu) konusu daha önce araştırıldı; onu yalnız merak cümlesiyle karşılaştırmak için kullan.
Çıktıyı üç tablo ve üç liste olarak ver: (a) BAŞLIK KALIBI tablosu — kalıp, örnek, çalıştığı trafik kaynağı, ölçülen etki, risk, kaynak, etiket; (b) KAPAK YAZISI tablosu — tür (yok, film adı, soru, iddia, uyarı, sayı), kelime sayısı, ölçülen ya da bildirilen etki, başlıkla ilişkisi, kaynak, etiket; (c) KESİLME tablosu — yüzey, cihaz, görünen karakter ya da kelime sayısı, tarih, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; ekran görüntüsünden saydığın kesilme değerlerini tarih ve cihazla "UYGULAMA" diye işaretle; aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) başlık ve kapak yazısı için en çok 8 kural, evet/hayır ile kontrol edilebilir biçimde; (2) tıklama tuzağı ile meşru merak cümlesini ayıran ölçütler; (3) bağlantılı tam kaynak listesi. Belgede olmayan karakter sınırı, oran ya da politika maddesi uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN VERİSİ: OUTBREAK 163.703 gösterim %5,1 (en geniş kitlede en iyi oran) · THE_SECOND_SHIP %14,3 ama 1.843 gösterim
  · zayıflar THE_LAST_ARCHIVE %1,07 · HEIR_OF_ASHES %1,04 · THE_HERD %1,74 (başlık biçimleri dökümde yok; sahipten gerekir)
  · "Why Solar Panels Fail on Mars" arama niyetli tek başlık: 1,4 B görüntülenme (00_KANAL_DENETIMI), bu dökümde %1,63
KANAL KURALI (KANAL_KIMLIGI §1, §3): "AI" başlıkta ve ilk 3 hashtag'de yasak · Stunning, Epic, Mind-Blowing yasak
  · en iyi iki sonucun başlığı "sessiz" ("Official Cinematic Film (4K)")
YENİ HAT: YAYIN_PAKETI en az 3 başlık seçeneği, biri QUIET · kapak başlığı tekrar etmez, ona ekler (kapak-tasarimcisi kural 3)
SAHİBİN YAPIŞTIRDIĞI ÖNERİDEKİ İDDİALAR (doğrulanacak):
  "'THE HERD | Sci-Fi Short Film' adı söyler, vaadi söylemez" · "'Her Own SOS Arrived 8 Minutes Before She Sent It | CHRONOS'
  doğru örnek: önce fikir, sonra ad" · "'THE LAST ARCHIVE' adı yeni izleyiciye bir şey söylemiyor"
  · kapak yazısı örnekleri "IT'S STILL ALIVE" · "DON'T LOOK UP" · "sorunun cevabını değil soruyu göster"
CEVAPTAN BEKLENEN: "merak cümlesi | AD" kalıbının ölçülmüş bir üstünlüğü var mı · sessiz başlığın iki iyi sonucu nasıl açıklanır ·
  mobil önerilen sütununda kaç karakter görünür · otomatik çeviri merak cümlesini bozuyor mu.
```

---

# 4️⃣ KAPAĞIN ÜRETİMİ — filmden kare mi, ayrı üretim mi; görsel modelle kapak ve yanıltıcılık sınırı

```
Video kapağının nasıl üretildiğine dair pratikleri ve kanıtı Ekim 2026 itibarıyla araştır. Ana soru: kapak filmin kendi karesinden mi alınmalı, yoksa kapak için ayrı tasarlanmış bir görsel mi olmalı? Şunları topla: akış platformlarının ve stüdyoların kapak ve tanıtım görseli üretim yöntemleri (Netflix'in kişiselleştirilmiş sanat eserleri ve kareden seçme araştırmaları, film afişi pratiği, büyük YouTube kanallarının yayımlanmış kapak üretim süreçleri), filmden alınan kare ile ayrı kompozisyonun tıklamaya ve memnuniyete etkisini karşılaştıran ölçüm ya da yöntemi yazılı deney, ayrı kompozisyonda filmde olmayan bir anın ya da nesnenin gösterilmesinin YouTube'un yanıltıcı meta veri politikası açısından sınırı ve izleyici tepkisi.
Yapay zekâ görsel modelleriyle kapak üretimini ayrıca sor: Google'ın görsel modelleri (Gemini görsel modelleri, Imagen; Flow içindeki görsel üretim) ve karşılaştırma için diğerleri ile kapak üretiminde karakter ve mekân tutarlılığını referans görsellerle korumanın yolları; 16:9 ve 3840×2160 çıktı ile büyütme; görsel modelin kapakta sık ürettiği kusurlar (fazla ayrıntı, yapay parlaklık, yüz ve el bozulması, istenmeyen yazı, filigran) ve bunların küçük boyda görünürlüğü; "yapay zekâ ile yapılmış görünüm"ün kapakta tıklamaya ve güvene etkisine dair anket ya da ölçüm; YouTube'un sentetik içerik bildiriminin kapağa uygulanıp uygulanmadığı. Kapak için kaç aday üretilmesi, adayların teste girmeden önce nasıl elendiği ve kapağın üretim takviminde ne zaman yapılması gerektiği (çekimden önce mi, kurgudan sonra mı) konusundaki uygulayıcı pratiklerini topla.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kapak üretim kılavuzudur. Filmler Google Flow'da referans görselleri ve başlangıç kareleriyle üretilen fotogerçekçi bilimkurgu filmleridir; aynı referans görselleri kapak üretiminde de kullanılabilir. Film çıktısı 16:9'dur; video karesinin çözünürlüğü kapak için önerilen 3840×2160'ın altında kalabilir. Kapak yazısı sonradan ayrı katman olarak eklenir. Ücretli tasarımcı ve fotoğraf düzenleme ekibi yoktur; tek kişi üretir. Kapak filmin içinde görünmeyen bir şeyi gösterirse bunu "vaat riski" diye ayrı işaretle.
Çıktıyı iki tablo ve üç liste olarak ver: (a) ÜRETİM YOLU tablosu — yol (filmden kare, kareden düzenleme, aynı referanslarla ayrı kompozisyon, filmde olmayan sahne), tıklamaya etkisi, memnuniyete ve tutmaya etkisi, politika riski, gereken emek, kaynak, etiket; (b) GÖRSEL MODEL tablosu — konu (tutarlılık, çözünürlük, kusur türü, yapay görünüm algısı, bildirim), bulgu, model ve sürüm, tarih, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; firma tanıtım yazısını ÖLÇÜLMÜŞ sayma; aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) kapak üretimi için adım sırası önerisi (ne zaman, kaç aday, hangi eleme ölçütü, hangi kontrol); (2) "kapak filmde gördüğün şey olmalı" kuralının nereye kadar esneyebileceğine dair kanıtlı sınır; (3) bağlantılı tam kaynak listesi. Belgede olmayan model adı, sürüm, çözünürlük ya da politika maddesi uydurma.
```

### 🧪 SINAMA SETİ

```
HATTAKİ ÇELİŞKİ:
  kapak-tasarimcisi kural 1: "an plandan seçilir; bitmiş kliplerde 'en güzel kare' aranmaz"
  kapak-tasarimcisi faz 9: "final kapak hangi gerçek kareden (dosya + saniye)"
  faz 6: aynı referanslarla iki İngilizce kapak promptu (16:9, 3840×2160)
  SAHİBİN YAPIŞTIRDIĞI ÖNERİ: "kapağı filmden kare alarak değil ayrı üretin: yakın çekim, abartılı ışık, sade arka plan"
  → kapak-tasarimcisi kural 5 "ışık filmin kendi ışığıdır, yeni ışık icat edilmez" ile de çelişiyor
STILL_POINT ilk 30 saniye kusuru: 0. saniyeden itibaren sağ alt köşede filigran (Gemini mercekleri) → kapak görselinde de aranmalı
KAPAK_VE_YAYIN (THE_MAYDAY_SEA): sahibin planı üç kapak adayını ayrı görsel promptu olarak veriyor (A/B/C)
CEVAPTAN BEKLENEN: kare ile ayrı kompozisyon arasında ölçülmüş bir fark var mı · ayrı kompozisyonun vaat sınırı nerede ·
  aynı referanslarla kapak üretmenin tutarlılık riski · kapak hangi fazda üretilmeli · faz 9 kuralı kalmalı mı.
```

---

# 5️⃣ TEST, OKUMA VE ESKİ VİDEOLAR — kapak testi kararları ve zayıf videoları kurtarmak

```
YouTube'da kapak ve başlık değişikliklerinin nasıl sınanacağını, sonuçların nasıl okunacağını ve eski, zayıf videoların paketinin değiştirilmesinin etkisini Ekim 2026 itibarıyla araştır. Kapak testi aracını ("Test & Compare", "Test and compare") resmî belgelerle ayrıntılı sor: hangi hesaplara açık, kaç seçenek, kazananı hangi ölçütle seçtiği (izlenme süresi payı ve bunun tıklama oranıyla ilişkisi), testin süresi, "kesin kazanan yok" sonucunun anlamı, küçük gösterimde test sonucunun güvenilirliği, test sırasında değişiklik yapmanın etkisi, sonuçların dışa aktarılıp aktarılamadığı. Testin yayından hemen sonra mı yoksa eski videolarda mı daha çok işe yaradığına dair yayımlanmış yaratıcı deneyleri topla.
Eski videoların kurtarılmasını ayrıca sor: yayımlanmış bir videonun kapağını ya da başlığını haftalar veya aylar sonra değiştirmenin gösterimleri yeniden canlandırıp canlandırmadığına dair YouTube çalışanlarının açıklamaları ve belgelenmiş vaka çalışmaları; hangi videolara öncelik verilmeli (çok gösterim alıp düşük tıklama oranı olanlar mı, iyi tutma oranı olup az gösterim alanlar mı); değişikliğin etkisini ölçmek için ne kadar beklenmeli ve hangi pencere karşılaştırılmalı; sık değiştirmenin zararı var mı. Tıklama oranını doğru okumayı da sor: gösterim hacmi büyüdükçe oranın düşmesi, küçük gösterimde yüksek oranın istatistiksel olarak ne kadar belirsiz olduğu (güven aralığı nasıl hesaplanır), trafik kaynağı karışımı değişince oranın değişmesi, tıklama oranı ile ortalama izlenme süresinin birlikte nasıl yorumlanacağı ve "iyi kapak" kararının hangi iki ölçüte dayanması gerektiği.
Kritik kısıt: kullanım yeri, her yeni filme ve kanalın eski videolarına uygulanan GENEL bir test ve bakım kılavuzudur. Kanal küçüktür (birkaç bin abone, yüzlerce video), yeni videolar haftada birkaç kez yayımlanır; gösterimlerin çoğu önerilen videolar yüzeyinden gelir; bazı eski videolar yüz binin üzerinde gösterim almış ama tıklama oranı %1 civarında kalmıştır. Ücretli test aracı yoktur; YouTube'un kendi aracı ve Studio verisi kullanılır. İstatistik önerilerini bir kişinin elle ya da basit bir betikle uygulayabileceği biçimde ver.
Çıktıyı üç tablo ve üç liste olarak ver: (a) TEST ARACI tablosu — özellik, değer ya da davranış, koşul, tarih, kaynak, etiket; (b) ESKİ VİDEO tablosu — değişiklik türü (kapak, başlık, ikisi), belgelenmiş etki, örneklem, bekleme süresi, risk, kaynak, etiket; (c) OKUMA tablosu — durum (küçük gösterim, hacim artışı, trafik karışımı değişimi, yüksek tıklama ve düşük izlenme), ne anlama gelir, nasıl doğrulanır, ne yapılır, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; tek bir yaratıcının anekdotunu ÖLÇÜLMÜŞ sayma; aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) eski videolar için öncelik sırası kuralı ve bir kapak değişikliği kayıt şablonu (alanlar ve örnek cümle); (2) tıklama oranı için güven aralığı hesabının adımları ve "bu fark gerçek mi" kararının en küçük gösterim sayısı; (3) bağlantılı tam kaynak listesi. Belgede olmayan özellik, süre, eşik ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN VERİSİ (sahibin dökümü, 12.10.2026; tarih aralığı BİLİNMİYOR):
  en çok kaybeden: THE_LAST_ARCHIVE 99 B gösterim %1,07 · HEIR_OF_ASHES 44 B %1,04 · "Why Solar Panels…" 41 B %1,63 · THE_HERD 29 B %1,74
  en iyi geniş kitle: OUTBREAK 163.703 gösterim %5,1 · küçük örneklem: THE_SECOND_SHIP 1.843 gösterim %14,3
  → kaba hesap: 1.843 gösterimde %14,3 için %95 güven aralığı yaklaşık ±1,6 puan; 99 B'de %1,07 için ±0,06 puan
DIŞ SAYI (DIS_SAYILAR §1): Test & Compare en çok 3 seçenek · izlenme süresine göre seçer · birkaç gün-2 hafta · masaüstü
  + gelişmiş özellik · Shorts'ta yok · görsellerden biri 1280×720 altındaysa hepsi 480p · test sürerken değişiklik testi durdurur
HATTAKİ KURAL: kapak A/B "tek değişkenle ayrışır" (kapak-tasarimcisi kural 2) ↔ araç 3 seçenek alır
  · IZLEYICI_VERISI kayıt tablosunda "A/B sonucu" ve "CTR 48s / 7g / 28g" sütunu var · paketleme §F10 "not yazılır, kural yazılmaz"
SAHİBİN YAPIŞTIRDIĞI ÖNERİDEKİ İDDİALAR (doğrulanacak):
  "ilk testi THE_LAST_ARCHIVE ve HEIR_OF_ASHES'ta yap: gösterimi en çok olan ve en çok kaybedenler"
  · "kazananı tıklamaya değil izlenme süresine göre seçer, doğru ölçü bu" · "az gösterimde oran doğal olarak yüksek çıkar"
CEVAPTAN BEKLENEN: eski videoda kapak değişikliğinin gösterimi canlandırdığına dair kanıt · öncelik sırası kuralı ·
  güven aralığı yöntemi · tek değişken ile üç seçenek arasında hangi test tasarımı.
```
