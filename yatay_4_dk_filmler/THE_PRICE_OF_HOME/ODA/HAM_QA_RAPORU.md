# 🧪 THE_PRICE_OF_HOME — Ham QA Raporları (`taslak_01`)

> **Kayıt Tarihi:** 16.10.2026  
> **Kapsam:** 4 dakikalık film (24 × 10 s), `taslak_01`  
> **İçerik:** Sahibin ilettiği 4 ham rapor: Anlatım Testi · İzleme Formu (A + B) · Süreklilik · Tarama.  
> **Kural (AGENTS.md Madde ⑦):** Bu dosya ham çıktıdır, içeriği değiştirilmeden saklanır. (Yalnızca tablo hücrelerinin içindeki boş satırlar, tablo bozulmasın diye kaldırıldı; kelime değişmedi.)  
> **Kaynak notları (değerlendirme: `QA_DEGERLENDIRME.md`):**
> - **İzleme Formu A ve B'yi Gemini yazdı** ("simülasyon"); insan izleyici değildir. AGENTS.md ⑤: gerçek izleme = sahip + ≥2 dış izleyici.
> - **Tarama ve Süreklilik**: şablondaki `WHAT SHOULD BE IN THIS VIDEO` ve `CUT LIST` bölümleri doldurulmadan gönderildi (Gemini kendisi belirtti). Kaynak bayrağı: `ne olmalı` + `kesme` yok → ağırlık düşük.
> - `timeline.json` boş → zaman → çekim eşlemesi `çapa: içerik` (Cn ≈ ⌊t/10⌋+1) ile yapıldı.

---

# 1. ANLATIM TESTİ

Videoyu yalnızca ekranda görülen ve duyulanlara dayanarak, hikâyenin planını bilmeyen sıradan bir izleyici gözüyle değerlendirdiğim yanıtlar aşağıdadır:

### 1. NE OLDU (WHAT HAPPENED)

* **00:00** – Bir erkek ve bir kadın astronot, arkalarındaki camda Dünya benzeri mavi bir gezegen görünürken uzay aracının kokpitinde endişeyle birbirlerine bakarlar.
* **00:10** – Uzay aracı, Jüpiter benzeri dev bir gaz gezegeninin yakınındaki halka şeklinde büyük bir uzay istasyonuna yaklaşır.
* **00:40** – Uzay aracı, istasyonun kenetlenme kapısına mekanik kilitlerle bağlanır.
* **00:50** – İki astronot istasyonun içinde, ortasında parlayan piramit/kristal benzeri bir nesne bulunan konsolun başında uzaylı bir varlıkla karşı karşıya durur.
* **01:00** – Konsolun üzerindeki el izi tarayıcısı ve kristalin arkasındaki şeffaf ekran aktifleşir.
* **01:10** – Kadın astronot (Mara) konsola ve ardından karşısındaki erkek astronota üzüntüyle ve dolu gözlerle bakar.
* **01:20** – Astronot eldivenli ellerde, gün batımında sahilde oturan bir çiftin fotoğrafı ve zincire takılı altın bir yüzük tutulur.
* **01:30** – Erkek astronot zamanlarının daraldığını ve başka bir seçenek olması gerektiğini söyler; Mara ise bir yol bulmaya çalıştığını belirtir.
* **02:10** – Erkek astronot Mara'ya bunu yapmak zorunda olmadığını söyleyerek onun yerini almayı teklif eder.
* **02:20** – Mara elini konsolun üzerine uzatır ve **02:40**'ta elini tarayıcı panele bastırarak mekanizmayı çalıştırır.
* **02:50** – İstasyonun dev halkasının içinde Dünya'yı gösteren parlak bir enerji geçidi (portal) açılır.
* **03:10** – Uzay aracı istasyondan ayrılır ve **03:20**'de motorlarını ateşleyerek doğrudan Dünya geçidinin içine uçar.
* **03:30** – Dünya yörüngesine ulaştıklarında erkek astronot sevinç gözyaşlarıyla Mara'ya bakar, ancak **03:36**'da Mara'nın söylediği söz üzerine erkeğin yüzündeki gülümseme donar ve yerini büyük bir üzüntüye bırakır.
* **03:40** – İstasyondaki uzaylı, içi altın renkli ışık ağlarıyla dolan kristale bakarak gözlerini kapatır ve derin bir iç çeker.
* **03:50** – Kokpitteki iki astronot, arkalarında Dünya manzarasıyla birbirlerine gülümseyerek bakarlar.

### 2. KİM (WHO)

* **Ana karakterler:** Mara (kolunda sarı şerit olan kadın astronot) ve yanındaki erkek astronottur (kolunda mavi şerit olan).
* **Diğer karakterler:** İstasyonun içindeki konsolun başında sessizce bekleyen, mor-gri tenli ve koyu cübbeli bir uzaylı görülür.
* **İlişkileri:** **01:20**'de görülen sahildeki çift fotoğrafı ve alyanstan anlaşıldığı kadarıyla Mara ve erkek astronot birbirine aşık bir çift ya da evlidir; uzaylı ise konsolu ve geçidi bekleyen bir gözetmen/aracı konumundadır.

### 3. İSTEK (WANT)

* **Ne istiyorlar:** Uzay istasyonundaki sistemi çalıştırıp Dünya'ya (evlerine) geri dönmek istemektedirler.
* **Ne zaman netleşti:** **01:31**'de bir kriz içinde oldukları ve çözüm aradıkları anlaşılır, ancak tam olarak ne yapmaya çalıştıkları (Dünya'ya bir portal açıp dönmek) ancak **02:54**'te halkanın içinde Dünya belirdiğinde ve **03:20**'de içine uçtuklarında netleşir.

### 4. ENGEL (OBSTACLE)

* Zamanlarının tükeniyor olması (**01:31**) ve geçidi açacak olan konsolun çalışması için içlerinden birinin elini panele basarak kendisinden bir şey (muhtemelen hafızasını/anılarını) feda etmesi gerekliliği önlerindeki engeldir.

### 5. SEÇİM (CHOICE)

* Erkek astronot **02:17**'de Mara'nın yerini almayı teklif etmesine rağmen, Mara **02:24 – 02:47** arasında elini konsola basarak fedakârlığı kendisi yapmayı seçer.

### 6. SON (ENDING)

* **Nasıl bitiyor:** Geçitten geçerek Dünya'ya ulaşırlar.
* **İstediklerini aldılar mı ve bedeli ne oldu:** Evet, Dünya'ya dönmeyi başarırlar; ancak **03:36**'da Mara'nın erkeğe yabancı gibi bakarak fısıldaması, erkeğin yıkılması ve **03:40**'ta kristalin içinde beliren zihin/sinir ağı benzeri ışıklar, Mara'nın bedel olarak anılarını (veya eşini) unuttuğunu gösterir. Bununla birlikte **03:50**'deki son çekimde ikisinin tekrar mutlu şekilde gülümsemesi bu durumun ne kadar kalıcı olduğu konusunda belirsizlik yaratır.

### 7. NE SÖYLENDİ (WHAT WAS SAID)

* **01:31** – Erkek astronot: *"Mara, we are running out of time."* (Mara, zamanımız tükeniyor.)
* **01:34** – Mara: *"I'm trying to find a way. I'm trying to find a way."* (Bir yol bulmaya çalışıyorum. Bir yol bulmaya çalışıyorum.)
* **01:37** – Erkek astronot: *"There has to be another option."* (Başka bir seçenek olmalı.)
* **02:04** – Mara: *"[unclear] just for years."* ("You've seen me just for years" benzeri, ilk kısmı anlaşılmayan bir cümle).
* **02:10** – Erkek astronot: *"Mara, please listen to me. You don't have to do this. Let me take your place."* (Mara, lütfen beni dinle. Bunu yapmak zorunda değilsin. İzin ver senin yerini ben alayım.)
* **03:36** – Mara: *"Who are you?"* veya *"[unclear] you"* ("Who are you?" ya da "For you?" gibi çok kısık bir fısıltı).
* **03:46** – Uzaylı: *"Ahhh..."* (Sözsüz derin bir iç çekiş).

### 8. HİS (FEELING)

* Çiftin eve dönmesine rağmen kadının hafızasını kaybetmesi nedeniyle buruk bir hüzün, ancak son sahnedeki ani gülümseme ve görsel devamlılık kopuklukları yüzünden hafif bir kafa karışıklığı hissettim.

---

### Anlatım ve Akış Tablosu

| # | time | type | what exactly is seen or heard | confidence |
| --- | --- | --- | --- | --- |
| 1 | 00:00 | A1 CONFUSED | Filmin ilk saniyesinde kokpit camının arkasında zaten Dünya görünmektedir, fakat **00:10**'da gemi Jüpiter benzeri bir gezegenin yanındadır ve filmin sonunda Dünya'ya portal ile dönerler. | SURE |
| 2 | 00:30 | A1 CONFUSED | Astronotlar öne doğru bakarken istasyonun kenetlenme noktası arkalarındaki camda görünmektedir; geminin hangi yöne doğru kenetlendiği kafa karıştırıcıdır. | SURE |
| 3 | 01:00 | A1 CONFUSED | Konsoldaki kristal ve el izi tarayıcısının tam olarak ne işe yaradığı ve ne tür bir tehlike/pazarlık olduğu bu aşamada açıklanmadığı için ne olup bittiği belirsizdir. | SURE |
| 4 | 01:16 | A1 CONFUSED | Erkek astronotun kaskı bu çekimde tamamen çıkmış görünürken, **01:30**'daki çekimde kaskı tekrar başındadır. | SURE |
| 5 | 01:34 | A1 CONFUSED | Mara'nın *"I'm trying to find a way"* repliği duyulurken ekranda erkek astronotun profili vardır ve kimin konuştuğu ilk anda görsel olarak anlaşılmaz. | SURE |
| 6 | 01:40 | A2 WOULD STOP | İlk 1 dakika 40 saniye boyunca çok yavaş, diyalogsuz ve birbirini tekrar eden uzay/bakışma çekimleri sürdüğü ve hikâyedeki asıl sorunun ne olduğu hâlâ netleşmediği için burada izlemeyi bırakabilirdim. | LIKELY |
| 7 | 02:04 | A3 LINE UNCLEAR | Mara'nın söylediği cümlenin başı (*"[unclear] just for years"*) boğuktur ve kelimeler net seçilememektedir. | SURE |
| 8 | 03:00 | A1 CONFUSED | Gemi istasyondan henüz **03:10**'da ayrılmasına rağmen, **03:00**'daki çekimde astronotlar kokpitte arkalarında açılmış portal ve Dünya ile görünürler. | SURE |
| 9 | 03:36 | A3 LINE UNCLEAR | Mara'nın fısıldadığı kısa replik (*"Who are you?"* veya *"For you?"*) çok kısık seslidir ve tam olarak hangi kelimenin söylendiği net değildir. | SURE |
| 10 | 03:46 | A4 SOUND OFF | Uzaylı gözlerini kapattığında, görüntüsüne uymayan şekilde sıradan bir erkek insan sesiyle yüksek bir *"Ahhh"* iç çekişi duyulur. | SURE |
| 11 | 03:50 | A1 CONFUSED | **03:38**'de erkek astronot Mara'nın tepkisiyle yıkılmış ve gözyaşı dökerken, **03:50**'deki son çekimde ikisi de hiçbir sorun yokmuş gibi birbirine mutlu şekilde gülümser. | SURE |

---

# 2. İZLEME FORMU  *(Gemini tarafından yazıldı — insan izleyici değil)*

Filmin mevcut taslağı için **İZLEME FORMU** kapsamındaki detaylı teknik ve anlatısal değerlendirme aşağıdadır. Doğrudan `NOTLAR.md` dosyasına ekleyebileceğiniz yapılandırılmış cevapları ve zaman damgalı tespitleri içerir.

## A · Sahibin Sekiz Sorusu (Taslak, Sesli, Baştan Sona)

```text
1. Ne olduğunu anladım mı?                       kısmen — anlamadığım an: 02:10 - 03:09
   (Erkek astronot 02:14'te "Bunu yapmak zorunda değilsin, senin yerini almama izin ver" diyerek 
   el izi paneline basmanın tek taraflı bir feda/geride kalma gerektirdiğini ima ediyor; ancak 02:46'da 
   butona basıldıktan hemen sonra 03:00'da İKİSİ BİRDEN geminin kokpitinde yan yana ve güvende görünüyor. 
   Feda edilen şeyin ne olduğu ve neden ikisinin de kurtulduğu anlaşılmıyor.)

2. Karakter baştan sona aynı kişi mi?            hayır — koptuğu an: 01:16, 03:40 ve 03:50
   - 01:16 - 01:19: Erkek astronotun sol ön plandaki omuz üstü çekiminde KASKI YOK (çıplak kulağı, 
     saçı ve sakalı görünüyor), hemen bir sonraki konuşma planında (01:30) kaskı tekrar başında.
   - 03:40 - 03:49: Uzaylının kafa/boynuz yapısı ve yüz hatları, 00:50 ve 01:50'deki daha ince/keskin 
     uzaylı tasarımından farklılaşarak daha geniş bir kafatasına dönüşüyor.
   - 03:50 - 03:59: Kadın astronotun (Mara) sol kolunda önceki planlarda olmayan bir ABD bayrağı 
     yaması ve mavi dijital bileklik beliriyor; erkek astronotun kolundaki mavi şerit kayboluyor.

3. Saçma bir şey gördüm mü?                      00:00, 00:10, 01:18, 03:00, 03:10
   - 00:00 - 00:09: Eve (Dünya'ya) dönmeye çalışan ekibin daha filmin ilk saniyesinde kokpit camının 
     arkasında zaten Dünya var. Ayrıca koltukları ön cama sırtı dönük şekilde konumlanmış.
   - 00:10 - 00:19: Gemi sağdaki istasyona doğru giderken burnu sol alta bakıyor (yan/geri kayarak uçuyor).
   - 01:18: Kadın astronot kaskının içindeyken nefes veriyor ama buhar/duman kaskın DIŞINDAN (sol 
     taraftan) çıkıyor.
   - 03:00 - 03:09: Kokpit camından bakıldığında halka portalın içinde Dünya görünürken, halkanın 
     dışındaki arka planda da dev bir Dünya zaten duruyor.
   - 03:10 - 03:19: Gemi istasyondan ayrılıp portala doğru giderken tasarım tamamen değişiyor (burun 
     kısmı küt bir kapsüle dönüşüyor) ve Dünya görüntüsü halka portalın sınırlarından dışarı taşıyor.

4. Oyunculuk: beden işi taşıyor mu, ağır iş ağır mı, tepki gerçek mi?   sahte duran an: 01:37, 02:04, 03:36
   - 01:37 - 01:39: Erkek astronot "There has to be another option" derken ağzı tamamen kapalı, 
     dudakları hiç kıpırdamıyor.
   - 02:04 - 02:06: Mara konuşurken yüz ifadesi ve dudak hareketi yapay/bozuk.
   - 03:36 - 03:38: Mara'nın dudakları kıpırdamadan replik duyuluyor.

5. Diyalog: her repliği anladım mı, doğal mı?    anlaşılmayan / yapay duran replik: 01:33, 02:04, 03:36
   - 01:33 - 01:37: "I'm trying to find a way" repliği arka arkaya iki kez tekrarlanıyor (01:34 ve 01:36).
   - 02:04 - 02:06: Mara'nın repliği bozuk AI fonetiği yüzünden anlaşılmıyor ("He'll see me just for years" / 
     "In-see-mish-is for years" gibi anlamsız bir ses çıkıyor).
   - 03:36 - 03:37: Mara anlamsız ve bağlam dışı şekilde "Her you" / "Are you?" diyor.

6. Ses: müzik ya da efekt bir sesi bastırıyor mu; ses kesik, eksik ya da yanlış mı?   00:18, 00:21, 00:41, 02:55, 03:46
   - 00:18, 00:21 - 00:29, 00:41 - 00:48, 02:55, 03:15, 03:21: Uzay vakumunda gerçekleşen dış 
     çekimlerde çok yüksek sesli rüzgâr/geçiş (whoosh), roket iticisi, metalik kenetlenme ve yıldırım 
     sesleri var (vakumda dış ses hatası).
   - 03:46: Uzaylı karakter tamamen sıradan bir insan erkek sesiyle iç çekiyor ("Haaah").

7. Sıkıldığım an                                 00:50 - 01:15 ve 01:40 - 02:00
   (Uzaylı ile karşılaşılan 00:50 - 00:59 planında hiçbir etkileşim veya diyalog olmadan 10 saniye 
   boyunca sabit bakışılıyor; 01:40 - 01:59 arasındaki dış istasyon ve uzaylı planları gerilimi 
   yükseltmek yerine anlatıyı duraksatıyor.)

8. Son bana bir şey hissettirdi mi?              Kısmi bir rahatlama hissi var (03:31'deki oyunculuk 
   ifadesi başarılı), ancak "fedakârlık" çatışması boşa düştüğü (ikisi de hiçbir bedel ödemeden 
   kurtulduğu) için dramatik etkisi zayıf kalıyor.

→ Karar: kurguyu değiştir / sesi düzelt / çekimi yeniden üret

```

---

## B · Dış İzleyici Simülasyonu (Ön Bilgisiz İlk İzleme Perspektifi)

Hikâyeyi, konuyu veya karakterleri önceden hiç bilmeyen bir dış izleyicinin filmi izledikten sonra vereceği doğal yanıtlar:

1. **Ne oldu? Baştan anlatır mısın?**

İki astronot uzaydaki büyük halka şeklinde bir istasyona kenetlendi. İçeride mor tenli bir uzaylı ve ortada parlayan piramit/elmas gibi bir taş vardı. Bir fotoğraf ve yüzüğe baktılar, aralarında bir zaman baskısı ve tartışma geçti. Erkek olan "Senin yerine ben yapayım" dedi ama kadın elini taşın yanındaki panele bastı. Bunun üzerine istasyonun halkasında Dünya'ya açılan bir geçit (portal) oluştu, gemilerine binip içinden geçerek Dünya'ya döndüler.

2. **Ana karakter ne istiyordu?**

Fotoğraftaki güzel günlerine, yani evlerine (Dünya'ya) geri dönmek istiyorlardı.

3. **Onu ne zorladı?**

Zamanlarının tükeniyor olması ve portalı açmak için birinin kendini feda etmesi gerekiyormuş gibi duran o el izi mekanizması zorladı; ama neden zorladığını tam anlamadım çünkü sonunda ikisi de gemiye binebildi.

4. **Sonunda ne oldu — istediğini aldı mı?**

Evet, portal açıldı ve ikisi birlikte gemiyle geçitten geçip Dünya'ya ulaştılar.

5. **Konuşmaları anladın mı? Anlamadığın ya da kimin söylediğini çıkaramadığın bir şey oldu mu?**

Kadının ortalarda (02:04 civarı) söylediği cümleyi hiç anlamadım, kelimeler birbirine girdi. Bir de 01:34'te kadın "I'm trying to find a way" cümlesini iki kere üst üste söyledi ve hemen ardından adam konuşurken ağzı hiç oynamadı. Sonda da (03:36) kadın dudaklarını kıpırdatmadan "Are you?" gibi kopuk bir şey dedi.

6. **Nerede kafan karıştı? (an ya da sahne tarifi)**

* **00:00:** Filmin en başında zaten arkalarında Dünya varken neden Jüpiter'e gidip Dünya'ya portal açmaya çalıştıklarını anlamadım.
* **02:00:** Uzaylı bir anda sahneden kayboldu, sonra 03:40'ta tekrar ortaya çıktı.
* **02:15 - 03:00:** Adam "Sen yapma, senin yerini ben alayım" deyince kadının orada kalacağını ya da öleceğini sandım ama düğmeye basıp hiçbir şey olmamış gibi beraber gemiye bindiler.

7. **Nerede bırakmak istedin? (an ya da "hiç")**

**01:40 - 02:00** arasında; konuşma başladıktan sonra tekrar uzun uzun sabit duran istasyonu ve hiçbir şey yapmadan taşa bakan uzaylıyı izlediğimiz kısımda tempo çok düştü.

8. **Tek kelimeyle nasıldı?**

**Kopuk** (görsel atmosferi etkileyici ama hikâye mantığı ve diyalogları kopuk).

---

## KAYIT (`NOTLAR.md` → İZLEME)

Aşağıdaki tabloyu doğrudan `NOTLAR.md` dosyanıza kopyalayabilirsiniz:

```markdown
| tarih | kim (A / B1 / B2 / B3) | sürüm (taslak_xx) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-10-16 | A | taslak_01 | kısmen (02:10-03:09 feda mantığı boşta) | hayır (01:16 kask yok, 03:40 uzaylı değişiyor, 03:50 ABD bayrağı) | 00:00'da arkada Dünya var; 00:10 gemi yan uçuyor; 01:18 kask dışından nefes buharı; 03:00 portal dışında da Dünya var | 01:37 ve 03:36 dudak senkronu yok; 02:04 yüz/ağız bozuk | 01:34 replik tekrarı; 02:04 bozuk telaffuz; 03:36 bağlam dışı "Her you" | 00:18, 00:21, 00:41, 02:55, 03:21 vakumda dış ses; 03:46 insan iç çekişi | 00:50-01:15 ve 01:40-02:00 | Kısmi rahatlama ama bedel ödenmediği için katarsis zayıf |
| 2026-10-16 | B1 | taslak_01 | İki astronot istasyona kenetlendi, uzaylı ve taş vardı, kadın butona bastı, portal açıldı ve Dünya'ya döndüler | Eve (Dünya'ya) ve eski hayatlarına dönmek | Zamanın bitmesi ve butona basma kararı (ama bedeli anlaşılmadı) | Evet, ikisi de kurtulup Dünya'ya döndü | 02:04 hiç anlaşılmadı; 01:34 iki kez tekrarlandı; 01:38'de adamın ağzı oynamadı; 03:36 kopuktu | 00:00'da Dünya'nın zaten arkada olması; 02:15'te "yerini alayım" deyip 03:00'da ikisinin de gemide olması | 01:40 - 02:00 arası durağan planlar | Kopuk |

```

### Öncelikli Aksiyon Özeti (Yeniden Üretim & Kurgu İçin)

1. **Anlatı / Kurgu Düzeltmesi:** "Fedakârlık" repliği (*"Let me take your place"* - 02:17) ile finalde ikisinin birden kokpitte olması (03:00) birbiriyle çelişiyor. Ya diyalog *"Bunu çalıştırırsak geri dönüşü olmayabilir"* gibi ortak bir riske çevrilmeli ya da final kokpit planlarında (03:00, 03:30, 03:50) gemide yalnızca kurtulan karakter yer almalı.
2. **Yeniden Üretilecek Çekimler (Çekim Listesi):**
   * **00:00 - 00:09:** Kokpit camının arkasındaki Dünya kaldırılıp yerine derin uzay / Jüpiter konulmalı.
   * **01:16 - 01:19:** Kasksız erkek astronot ve kask dışından çıkan nefes buharı hatası düzeltilmeli.
   * **02:00 - 02:09 & 03:30 - 03:39:** Bozuk İngilizce seslendirmeler (*"He'll see me just for years"*, *"Her you"*) ve dudak senkronu hataları temizlenmeli.
   * **03:00 - 03:19:** Portal açıldıktan sonra hem portalın içinde hem de portalın dışındaki uzayda aynı anda iki Dünya görünmesi hatası giderilmeli.
3. **Ses Miksajı:** Uzay boşluğundaki dış çekimlerde (00:18, 00:21, 00:41, 02:55, 03:15, 03:21) açık atmosferik roket/metal sesleri ya tamamen kesilmeli ya da boğuklaştırılarak (low-pass filter ile gövde titreşimi/iç kabin uğultusu gibi) fizik kurallarına uygun hale getirilmeli; 01:34'teki çift replik tekrarı kurguda kesilmeli.

---

# 3. SÜREKLİLİK

Paylaştığınız şablonda `WHAT SHOULD BE IN THIS VIDEO` ve `CUT LIST` bölümleri örnek değerlerle (placeholder) bırakıldığı için videodaki 24 klibin tamamını (her 10. saniyedeki kesmeleri) inceledim.

Şablondaki kurallara göre **Türkçe açıklamalı özet** ve doğrudan kopyalayıp `NOTLAR.md` iş akışınızda kullanabileceğiniz **İngilizce standart tablo** aşağıdadır:

### 📋 Tespit Edilen Süreklilik Hataları (Türkçe Özet)

* **Kesme 1 (`00:10.0` · C01 → C02):**
  * **S4 (WORLD JUMP):** `00:09`'da kokpit camının tam karşısında mavi-beyaz bulutlu bir gezegen (Dünya benzeri) varken, `00:10`'daki dış çekimde geminin yanında turuncu-kahverengi kuşaklı bir gaz devi (Jüpiter benzeri) ve uzay istasyonu beliriyor; mavi gezegen kayboluyor.
  * **S3 (DIRECTION FLIP):** `00:10`'da geminin burnu sola/öne dönükken ve istasyon sağ arkada kalırken, gemi geri geri istasyona doğru yaklaşıyor.
* **Kesme 2 (`00:20.0` · C02 → C03):**
  * **S3 (DIRECTION FLIP):** `00:19`'da geminin burnu sola dönük ve istasyon sağdayken, `00:20`'de geminin burnu sağa dönük şekilde soldan sağa doğru istasyonun kenetlenme portuna yaklaşıyor.
  * **S1 / S4 (LOOK / WORLD JUMP):** `00:19`'da geminin burnunda büyük yuvarlak bir kenetlenme halkası/sensör varken, `00:20`'de burun sivri ve pürüzsüz bir koniye dönüşüyor. Ayrıca arka plandaki gaz devinin sol altında bir uydu beliriyor.
* **Kesme 3 (`00:30.0` · C03 → C04):**
  * **S1 (LOOK JUMP):** Erkek astronotun sağ kolundaki tek kalın mavi şerit (`00:09`), `00:30`'da iki mavi şeride dönüşüyor. Göğsündeki yuvarlak arma tasarım değiştiriyor.
* **Kesme 5 (`00:50.0` · C05 → C06):**
  * **S1 (LOOK JUMP):** `00:39`'da erkek astronotun göğsünde yuvarlak bir arma ve sağ kolunda iki mavi şerit varken, `00:50`'de göğsündeki arma mavi üçgen armaya (kadınınkiyle aynı) ve kolundaki şerit tekrar tek kalın mavi şeride dönüyor.
* **Kesme 6 (`01:00.0` · C06 → C07):**
  * **S4 / S5 (WORLD / STATE RESET):** `00:59`'da konsolun tam arkasında uzaylı karakter dururken ve konsolun ön yüzünde el izi paneli yokken, `01:00`'de konsolun üzerinde parlayan bir el izi paneli beliriyor ve arka planda uzaylı görünmüyor.
* **Kesme 7 (`01:10.0` · C07 → C08):**
  * **S5 (STATE RESET):** `01:09`'da konsolun ortasında parlayan kristal ve yükselen saydam koruyucu kalkan varken, `01:10`'da konsolun üstü tamamen düz metalik bir kapakla kapalı (kristal, kalkan ve el izi paneli kaybolmuş).
* **Kesme 8 (`01:20.0` · C08 → C09):**
  * **S1 (LOOK JUMP):** `01:19`'da soldaki erkek astronotun kaskı yokken ve kask çemberi görünmezken, `01:20`'de fotoğrafı tutan astronotun kaskı takılı ve eldiven bileklerinde siyah kayışlar var.
* **Kesme 9 (`01:30.0` · C09 → C10):**
  * **S5 (STATE RESET):** `01:29`'da ellerde fotoğraf ve yüzük varken, `01:30`'da eller aşağıda/boş ve arka plandaki konsolun üzerinde kristal tekrar açıkta duruyor (`01:10`'da kapalıydı).
* **Kesme 10 (`01:40.0` · C10 → C11):**
  * **S4 (WORLD JUMP):** `00:49`'daki kenetlenmede gemi solda, istasyon halkası geminin arkasında/sağında ve gezegen görünmezken; `01:40`'ta istasyon solda, halka sağda ve gaz devi sağ tarafta yer alıyor.
* **Kesme 13 (`02:10.0` · C13 → C14):**
  * **S1 (LOOK JUMP):** `02:09`'da erkek astronotun üzerinde siyah omuz askıları (harness), göğsünde mavi üçgen arma ve göbeğinde yuvarlak metal mekanizma varken; `02:10`'da siyah askılar kaybolup beyaz askılara dönüşüyor, üçgen arma yuvarlak armaya dönüşüyor ve göbekteki mekanizma kayboluyor.
  * **S5 (STATE RESET):** `02:09`'da konsolun üzerinde duran kristal, `02:10`'da tamamen kayboluyor ve yerinde düz parlayan halkalı el izi yüzeyi kalıyor.
* **Kesme 14 (`02:20.0` · C14 → C15):**
  * **S1 (LOOK JUMP):** `02:19`'da erkek astronotun omuzlarında siyah askı yokken, `02:20`'de sol ön planda görünen erkek astronotun siyah askıları geri geliyor. Kadının sağ eldiveninin iç kısmında siyah parmak uçları beliriyor.
  * **S5 (STATE RESET):** `02:19`'da konsolun üzerinde kristal yokken ve erkek astronot elini konsolun üstüne koymuşken, `02:20`'de kristal konsolun üzerinde tekrar beliriyor ve erkeğin eli orada değil.
* **Kesme 16 (`02:40.0` · C16 → C17):**
  * **S1 (LOOK JUMP):** `02:29`'da kadının sağ eli konsolun üzerindeyken bileğinde saat/cihaz yokken, `02:40`'taki yakın çekimde sol kolun üzerinde altın/bronz çerçeveli yuvarlak bir bilek göstergesi beliriyor ve sol el kullanılıyor.
* **Kesme 17 (`02:50.0` · C17 → C18):**
  * **S4 (WORLD JUMP):** `01:49`'daki dış çekimde istasyonun ana gövdesi solda ve halka sağdayken, `02:50`'de görüntü yatay olarak ters dönmüş gibi halka solda, kenetlenmiş gemi ve gezegen sağda duruyor (gezegenin altındaki uydu ise üstte bir uydu ve altta bir uydu olmak üzere değişiyor).
* **Kesme 18 (`03:00.0` · C18 → C19):**
  * **S4 (WORLD JUMP):** `02:59`'da gemi istasyonun yan tarafına (halkanın dışına ve dik açıyla) kenetlenmiş durumdayken, `03:00`'te kokpit camından bakıldığında gemi doğrudan halkanın tam karşısında (merkez ekseninde) duruyor ve sağ arkada zaten mavi Dünya görünüyor.
* **Kesme 19 (`03:10.0` · C19 → C20):**
  * **S4 (WORLD JUMP):** `03:09`'da gemi doğrudan portal halkasına doğru bakarken, `03:10`'da gemi soldaki istasyon kenetlenme portundan ayrılıp sağdaki halkaya doğru ilerliyor ve mavi gezegen hem halkanın içinde hem de halkanın dışına taşacak şekilde arkasında duruyor.
* **Kesme 20 (`03:20.0` · C20 → C21):**
  * **S4 (WORLD JUMP):** `03:19`'da gemi soldan sağa doğru, halkanın yanından geçecek bir açıyla ilerlerken ve sol altta gezegen yokken; `03:20`'de gemi kameradan uzaklaşarak doğrudan halkanın merkezine giriyor ve sol alt köşede küçük bir halkalı gezegen (Satürn benzeri) ile uyduları beliriyor.
* **Kesme 21 (`03:30.0` · C21 → C22):**
  * **S2 (LIGHT JUMP):** `03:29`'da ekran tamamen bembeyaz bir ışıkla kaplanmışken, `03:30`'da aniden normal aydınlatmalı kokpit içine kesiliyor.
* **Kesme 22 (`03:40.0` · C22 → C23):**
  * **S1 (LOOK JUMP):** Daha önceki sahnelerde (`01:59`) mor tenli, dikey gözbebekli ve koyu altın/siyah düz yakalı olan uzaylı, `03:40`'ta gri/kahverengi tenli, daha geniş kemikli başlı, turuncu gözlü ve katmanlı omuz zırhlı farklı bir tasarıma dönüşüyor. Ayrıca önündeki kristalin içinde takımyıldız benzeri parlayan ağ çizgileri beliriyor.
* **Kesme 23 (`03:50.0` · C23 → C24):**
  * **S1 (LOOK JUMP):** `03:39`'da kadın astronotun sol kolunda iki altın şerit varken, `03:50`'de sol kolundaki şeritlerin üzerinde Amerikan bayrağı peçi ve bileğine yakın mavi ışıklı bir ekran beliriyor.

### 📄 Standart Çıktı (İngilizce — Kopyalamaya Hazır)

```text
FINDINGS
| # | time | type | what exactly is seen or heard (cut number · before → after) | confidence |
|---|------|------|-------------------------------------------------------------|------------|
| 1 | 00:10.0 | S4 | Cut 1 · Blue-and-white Earth-like planet directly in front of the cockpit window → Orange-banded gas giant on the left and a space station on the right; blue planet is gone | SURE |
| 2 | 00:20.0 | S3 | Cut 2 · Spacecraft nose points left while moving backward toward the station on the right → Spacecraft nose points right while moving left-to-right toward the station on the right | SURE |
| 3 | 00:20.0 | S1 | Cut 2 · Spacecraft has a large circular black sensor/docking ring on its blunt nose → Spacecraft has a pointed, closed white nose cone | SURE |
| 4 | 00:30.0 | S1 | Cut 3 · Male astronaut (left) has a single thick blue band on his right arm and a dark circular chest patch (at 00:09) → Male astronaut has a double blue band on his right arm and a white/blue circular chest patch | SURE |
| 5 | 00:50.0 | S1 | Cut 5 · Male astronaut has a circular chest patch and double blue arm band (at 00:39) → Male astronaut has a blue triangular chest patch and a single thick blue arm band | SURE |
| 6 | 01:00.0 | S5 | Cut 6 · The alien stands directly behind the pedestal and the front rim of the pedestal has no handprint pad → A glowing handprint pad appears on the front of the pedestal and the alien is gone from the background | SURE |
| 7 | 01:10.0 | S5 | Cut 7 · Glowing octahedron crystal sits on the pedestal behind a raised transparent shield → The pedestal top is completely flat and closed with a metal cover; crystal and shield are gone | SURE |
| 8 | 01:20.0 | S1 | Cut 8 · Male astronaut on the left is not wearing a helmet (bare head visible at 01:19) → In the POV/close-up shot holding the photo, a helmet visor reflection is visible behind the photo and the gloves have black wrist straps | LIKELY |
| 9 | 01:30.0 | S5 | Cut 9 · Pedestal was closed at 01:19 and astronaut was holding a photo at 01:29 → Hands are lowered/empty and the glowing crystal is back on top of the open pedestal in the background | SURE |
| 10 | 01:40.0 | S4 | Cut 10 · At 00:49 the ship was docked on the left side of the port with the station ring behind it and no planet visible → Station hub is on the left, ship is docked in the center pointing right, and the gas giant is on the right | SURE |
| 11 | 02:10.0 | S1 | Cut 13 · Male astronaut wears black webbing harness straps, a blue triangle chest patch, and a round abdominal dial → Black harness straps and abdominal dial disappear (replaced by white suit straps), and chest patch changes to a round emblem | SURE |
| 12 | 02:10.0 | S5 | Cut 13 · Glowing crystal sits on the center of the pedestal between the astronauts → Crystal is gone; pedestal top is flat with a glowing ring and handprint symbol | SURE |
| 13 | 02:20.0 | S1 | Cut 14 · Male astronaut has no black harness straps and places his all-white gloved right hand on the flat pedestal → Male astronaut in foreground left wears black harness straps again, and the crystal is back on the pedestal | SURE |
| 14 | 02:40.0 | S1 | Cut 16 · Female astronaut holds her right hand over the pedestal with no wrist gauge (at 02:29) → A left hand with a gold-rimmed circular wrist gauge and gold cuff ring reaches onto the pedestal | SURE |
| 15 | 02:50.0 | S4 | Cut 17 · At 01:49 the station ring was on the right of the hub and the ship pointed right → The station ring is now on the left of the hub, the docked ship points left, and a second small moon appears above the gas giant's limb | SURE |
| 16 | 03:00.0 | S4 | Cut 18 · The ship is docked perpendicular to the station hub outside the portal ring → From inside the cockpit, the ship is positioned out in free space facing directly into the front of the portal ring, with Earth already visible in the background sky to the right | SURE |
| 17 | 03:10.0 | S4 | Cut 19 · Cockpit view looks straight into the portal ring → Exterior shot shows the ship undocking from a side module on the left and flying left-to-right toward the ring, while Earth extends outside the ring's perimeter in the background | SURE |
| 18 | 03:20.0 | S4 | Cut 20 · Ship flies left-to-right in profile with black starry space in the lower left → Ship flies away from the camera into the ring, and a ringed Saturn-like planet with moons appears in the lower left background | SURE |
| 19 | 03:30.0 | S2 | Cut 21 · Screen is completely filled with a blinding white portal flash → Hard cut to normal interior cockpit lighting with no flash dissipation | SURE |
| 20 | 03:40.0 | S1 | Cut 22 · In earlier shots (01:59) the alien had purple skin, vertical slit pupils, a narrow ridged cranium, and a flat gold-trimmed collar → Alien now has grey-brown skin, a wider flared crest, orange round irises, layered shoulder armor, and the crystal has internal constellation lines | SURE |
| 21 | 03:50.0 | S1 | Cut 23 · Female astronaut has two gold bands on her left upper arm and a plain white forearm (at 03:39) → An American flag patch appears over the gold bands on her left arm and a glowing blue wrist display appears on her left forearm | SURE |

CUTS WITH NOTHING FOUND
4 (00:40.0), 11 (01:50.0), 12 (02:00.0), 15 (02:30.0)

COULD NOT CHECK
- Cut 3 (00:30.0), Cut 4 (00:40.0), Cut 5 (00:50.0), Cut 10 (01:40.0), Cut 11 (01:50.0), Cut 17 (02:50.0), Cut 21 (03:30.0), Cut 22 (03:40.0), Cut 23 (03:50.0): Treated as interior/exterior or location cuts; without your exact SAME/NEW labels from the CUT LIST, checked both S1 and spatial/state continuity across the sequence.

Nothing found does not mean clean. A human must still watch this video.

```

---

# 4. TARAMA

FINDINGS

| # | time | type | what exactly is seen or heard | confidence |
| --- | --- | --- | --- | --- |
| 1 | 00:18.0 - 00:19.0 | T8 | Loud whooshing and engine rumble sound heard in exterior deep-space vacuum shot. | SURE |
| 2 | 00:20.0 - 00:29.0 | T7 | White gas/smoke puffs out from the bottom of the ship and billows/hangs like smoke in atmosphere instead of dispersing rapidly in vacuum. | SURE |
| 3 | 00:20.0 - 00:29.0 | T8 | Engine thruster sounds and mechanical rumbles heard in exterior vacuum shot. | SURE |
| 4 | 00:30.0 - 00:39.0 | T6 | The male astronaut's chest patch changes from a circular emblem with a triangle inside (seen at 00:00-00:09) to a circular blue globe/grid patch; his shoulder stripe also shifts position. | SURE |
| 5 | 00:40.0 - 00:49.0 | T8 | Loud hissing, heavy metallic clanking, and mechanical latching sounds heard in exterior vacuum shot during docking. | SURE |
| 6 | 00:50.0 - 00:59.0 | T6 | The male astronaut's chest patch disappears completely (blank white suit), and the female astronaut's triangular chest patch is on her left chest with gold arm stripes. | SURE |
| 7 | 01:00.0 - 01:09.0 | T6 | The glowing crystal on the console changes from bright translucent amber/gold (at 00:59) to a dark, nearly opaque black octahedron. | SURE |
| 8 | 01:16.0 - 01:19.0 | T6 | The male astronaut appears in the left foreground without a helmet and wearing a dark grey/green collar instead of his white pressure suit, while the female astronaut directly across from him still has her white suit and helmet on. | SURE |
| 9 | 01:20.0 - 01:29.0 | T1 | A second, smaller deformed thumb/finger structure protrudes from the inner side of the right glove holding the ring keychain. | LIKELY |
| 10 | 01:30.0 - 01:39.0 | T6 | The male astronaut is back in his white suit and helmet; his chest now has the blue triangle patch that previously belonged to the female astronaut. | SURE |
| 11 | 01:30.0 - 01:39.0 | T11 | At 01:34-01:37, the female astronaut's voice ("I'm trying to find a way") is heard while the camera is on the male astronaut, and the over-the-shoulder view of the other astronaut shows no jaw/mouth movement. | LIKELY |
| 12 | 01:40.0 - 01:49.0 | T6 | In the exterior shot, the docked ship is facing left into the station hub, whereas in 00:20-00:29 it approached and docked facing right; the background planet has also switched sides relative to the station ring. | SURE |
| 13 | 02:04.0 - 02:06.0 | T11 | The female astronaut's mouth moves as if speaking, and distorted/reversed gibberish audio ("em see missions for years") plays that does not match clear lip sync. | SURE |
| 14 | 02:10.0 - 02:19.0 | T6 | The male astronaut's chest patch changes again from the blue triangle (at 01:39) back to a circular emblem; his right glove has a dark grey/black wrist strap not present in earlier shots. | SURE |
| 15 | 02:20.0 - 02:29.0 | T6 | The female astronaut's right glove has black fingertips and dark grey panelling, whereas in 01:10-01:15 her right glove was solid white. | SURE |
| 16 | 02:30.0 - 02:39.0 | T6 | The male astronaut's chest patch changes back to the blue triangle emblem. | SURE |
| 17 | 02:40.0 - 02:49.0 | T6 | The astronaut's left arm reaching for the console has a gold metallic wrist band and a watch-like dial on the forearm sleeve, plus black-tipped fingers, matching neither the earlier male nor female suit sleeves consistently. | SURE |
| 18 | 02:50.0 - 02:59.0 | T8 | Loud electrical crackling, rumbling, and musical chime/hum heard in exterior space shot as the portal opens. | SURE |
| 19 | 03:00.0 - 03:09.0 | T11 | Earth is already visible in the background outside the cockpit *around* the outside of the station ring before the ship has even flown through the portal inside the ring. | SURE |
| 20 | 03:10.0 - 03:19.0 | T6 | The ship undocking from the station is now a blunt-nosed cylindrical pod without a cockpit canopy or wings, completely different from the sleek fighter-like ship with a glass canopy that docked at 00:20-00:49. | SURE |
| 21 | 03:10.0 - 03:19.0 | T8 | Thruster whooshing sounds heard in exterior vacuum shot. | SURE |
| 22 | 03:10.0 - 03:19.0 | T11 | Earth is seen filling the space behind the entire station ring rather than only being visible *through* the portal aperture. | SURE |
| 23 | 03:20.0 - 03:29.0 | T6 | The ship changes shape again into a long, angular cruiser with dual rear engines, matching neither the original ship (00:10) nor the cylindrical pod (03:10). | SURE |
| 24 | 03:20.0 - 03:29.0 | T8 | Loud jet/rocket engine roaring heard in exterior vacuum shot. | SURE |
| 25 | 03:20.0 - 03:29.0 | T11 | At 03:20 Earth is clearly visible inside the ring; at 03:24 a white energy wall forms *in front* of Earth, and behind the white flash a faint gas giant/planet appears inside the ring while Saturn and Jupiter-like planets sit in the left background simultaneously. | SURE |
| 26 | 03:30.0 - 03:39.0 | T6 | Both astronauts now wear identical blue triangle chest patches. | SURE |
| 27 | 03:40.0 - 03:49.0 | T6 | The alien's head ridges, eye size/colour, and collar/shoulder armour design change significantly compared to 00:50-00:59 and 01:50-01:59; the crystal now has a glowing constellation/network pattern inside. | SURE |
| 28 | 03:50.0 - 03:59.0 | T6 | A US flag patch and a glowing blue digital wrist display appear on the female astronaut's left arm, which were not there in any previous shot (including 03:30-03:39). | SURE |

CLEAN WINDOWS

| shot (by start time) | longest range with nothing found |
| --- | --- |
| 00:00.0 | 00:00.0 - 00:09.9 |
| 00:10.0 | 00:10.0 - 00:17.5 |
| 01:10.0 | 01:10.0 - 01:15.9 |
| 01:50.0 | 01:50.0 - 01:59.9 |
| 02:00.0 | 02:00.0 - 02:03.9 |

COULD NOT CHECK

* High-speed/sub-second finger or facial micro-artifacts (<1s): Video was processed in standard video mode (1 fps sampling), so sub-second glitches between whole seconds could not be verified.
* Exact camera lock-off rules (T14) and specific "WHAT SHOULD BE" parameters: The template block was left with placeholder values (`<e.g. ...>`), so T6, T7, T8, and T11 were evaluated against standard physical consistency and internal shot-to-shot continuity.

Nothing found does not mean clean. A human must still watch this video.
