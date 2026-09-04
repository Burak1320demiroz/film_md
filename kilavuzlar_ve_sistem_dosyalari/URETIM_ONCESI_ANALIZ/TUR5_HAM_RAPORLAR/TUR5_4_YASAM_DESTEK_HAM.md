# TUR 5 · HAM RAPOR 4/4 — YAŞAM DESTEK ÜNİTESİ VE GÖĞÜS MODÜLÜ

> Koşulan prompt: `../09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` §4
> Koşu: 03.09.2026 · dış derin araştırma modeli · HAM ÇIKTI — düzeltilmez
> Süzme: `../04_ARASTIRMA_BULGULARI.md` §TUR 5

---

Uzay Giysisi Yaşam Destek Donanımlarının Dıştan Görünür Anatomisi ve Yapay Zekâ Video Sentezinde Devamlılık Çapaları
Giriş ve Konseptüel Çerçeve
İnsanlı uzay uçuşları tarihinde, araç dışı etkinlik (Extravehicular Activity - EVA) ve araç içi etkinlik (Intravehicular Activity - IVA) için tasarlanan uzay giysileri, yalnızca astronotu çevreleyen yalıtılmış kumaş bütünleri değil, mikro kütleçekimi, aşırı termal dalgalanmalar ve vakum ortamında insan fizyolojisini koruyan, kendi başına otonom minyatür uzay araçlarıdır. Tarihsel süreçte Apollo görevlerinden günümüz Uluslararası Uzay İstasyonu (ISS) operasyonlarına kadar uzay giysileri, mühendislik zorunluluklarının dış siluete doğrudan yansıdığı katı bir "form işlevi takip eder" ilkesiyle tasarlanmıştır. Bu bağlamda, NASA'nın Extravehicular Mobility Unit (EMU) sistemi, Rus tasarımı Orlan ve Sokol giysileri ile Artemis programı için geliştirilen xEMU, farklı operasyonel felsefelerin görsel çıktısı olan ikonik siluetlere sahiptir.

Günümüzde, sinematik görselleştirme, uzay simülasyonları ve Üretken Yapay Zekâ (Generative AI) tabanlı video sentezleme süreçlerinde (Sora, Seedance 2.0, Kling, Runway Gen-3 gibi difüzyon modelleri) bu uzay giysilerinin fotogerçekçi ve uzamsal olarak tutarlı bir şekilde üretilmesi, ciddi bir algoritmik darboğaz yaratmaktadır. Yapay zekâ video modelleri, sahneler arası geçişlerde ve karmaşık kamera hareketlerinde uzamsal ve zamansal dikkati (temporal attention) sürdürmekte zorlanır. Bu durum, ince hortum ağları, küçük etiketler veya karmaşık mekanik valfler gibi detayların kadreler ilerledikçe şekil değiştirmesine (morphing), kaybolmasına veya mantıksız anatomik noktalara kaymasına (drifting/hallucination) neden olmaktadır. Bu rapor, yaşam destek modüllerinin (PLSS, DCM, SOP, SAFER vb.) mekanik mimarisini, sayısal göstergelerini ve arıza görselliklerini derinlemesine analiz ederek, AI video üretiminde sahneden sahneye kaymayı önleyecek güvenilir geometrik öğeleri (devamlılık çapaları) sistematik bir yaklaşımla yapılandırmaktadır.

NASA EMU: Dıştan Görünür Yaşam Destek Anatomisi ve Geometrik Hacimler
1982 yılında Uzay Mekiği görevleri için tanıtılan ve sonrasında modülerleştirilerek ISS'te kullanılmaya başlanan EMU, Hamilton Sundstrand ve ILC Dover ortaklığında geliştirilmiş iki parçalı, yarı sert bir uzay giysisidir. Dıştan bakıldığında giysinin anatomisi, omuzları ve göğsü kaplayan Sert Üst Gövde (Hard Upper Torso - HUT) etrafında şekillenen büyük geometrik hacimlerle tanımlanır.

Sırt Ünitesi (PLSS) ve İkincil Oksijen Paketi (SOP)
Birincil Yaşam Destek Sistemi (Primary Life Support System - PLSS), astronotun sırtında taşıdığı ve EMU'nun otonomisini sağlayan ana modüldür. Oksijen sirkülasyonu, karbondioksit filtreleme (lityum hidroksit - LiOH aracılığıyla), güç sağlama ve sıvı soğutma giysisine (LCVG) su pompalama gibi kritik işlevler bu ünitenin içinde gerçekleşir.

PLSS, dışarıdan bakıldığında devasa, dikdörtgen prizma şeklinde ve beyaz Termal Mikrometeoroid Giysi (TMG) kumaşıyla kaplı bir zırh bloğu olarak görünür. Apollo döneminden günümüze evrilen bu modülün boyutları yaklaşık 66 cm (26 inç) yükseklik, 46−48 cm (18-19 inç) genişlik ve tabanda 24−25 cm (9.5-10 inç) derinliktedir. Sırttan omuz hizasına kadar yükselen bu rijit yapı, astronotun profil siluetini neredeyse iki katına çıkararak ona bir "insan-makine" hibriti görünümü verir.

PLSS'nin hemen altında, ünitenin alt çerçevesine entegre edilmiş olan İkincil Oksijen Paketi (Secondary Oxygen Pack - SOP) yer alır. SOP, birincil oksijen sisteminde bir arıza yaşanması veya giyside basınç kaybı olması durumunda otomatik olarak devreye girerek astronota 30 dakikalık acil durum oksijeni sağlayan iki adet yüksek basınçlı tank barındırır. Geometrik olarak SOP, PLSS ana bloğunun altına asılmış, yanlara doğru hafif kavisli, ana gövdeden marjinal olarak daha dar ancak yine beyaz TMG kumaşıyla kaplı bağımsız bir alt modül olarak ayırt edilir.

Göğüs Kontrol Modülü (DCM) ve İletişim Arayüzleri
Astronotun tüm bu yaşam destek sistemini yönettiği mekanik arayüz, göğüs hizasına monte edilmiş Gösterge ve Kontrol Modülü (Display and Control Module - DCM) adlı yapıdır. Kalın ve basınçlı EVA eldivenleriyle manipüle edilebilecek büyüklükte tasarlanmış mekanik anahtarlar, valfler ve göstergeler barındıran bu birim, küçük, metalik gümüş rengi ve siyah yüzeyli açılı bir kutu görünümündedir.

DCM üzerindeki fiziksel arayüzlerin konumlandırılması ve yapay zekâ üretimindeki kilit özellikleri şunlardır:

Bağlantı Soketleri ve Renk Kodları: Göğüs kutusunun alt ve yan kısımlarında, giysiyi hava kilidindeyken uzay aracının sistemlerine bağlayan Servis ve Soğutma Göbeği (Service and Cooling Umbilical - SCU) girişleri bulunur. Bu soketler, uzamsal körlük veya karmaşa anında yanlış hortum bağlantısını önlemek için parlak ve keskin renk kodlarıyla donatılmıştır. Sıvı soğutma (LCVG) ve oksijen hatlarının girişleri, belirgin kırmızı, mavi ve yeşil dairesel metal kilit halkaları (locking rings) ile çevrilidir.

Hortum Güzergâhları: Sırt çantasından (PLSS) çıkıp kolların altından dolanarak DCM'ye bağlanan kalın, yalıtımlı oksijen ve su hortumları, dış siluette astronotun gövdesini saran mekanik damarlar gibi görünür.

Kask Vizör Donanımı (EVVA) ve Entegre Aydınlatma
EMU'nun şeffaf polikarbonat "balon" kaskı, doğrudan uzay boşluğunun termal ve radyasyon tehlikelerine maruz bırakılamayacağı için dışına Araç Dışı Vizör Donanımı (Extravehicular Visor Assembly - EVVA) takılır. Dış siluetin zirvesini oluşturan bu devasa küre, AI üretimi için çok güçlü bir geometrik çapadır.

Altın Vizör: Güneşin kör edici ışığını ve zararlı radyasyonunu filtrelemek için tasarlanmış, tamamen ayna gibi yansıtıcı, metalik altın kaplamalı ana vizördür.

Termal ve Şeffaf Katmanlar: Altın vizörün altında termal koruma sağlayan ikincil bir şeffaf vizör bulunur. Ek olarak, istenmeyen açılardan gelen ışığı fiziksel olarak kesmek için astronotun manuel olarak indirebildiği opak beyaz "yan siperlikler" (blinders) mevcuttur.

Lambalar ve TV Kamerası: Vizör montürünün sol ve sağ üst köşelerinde, dış mekânı aydınlatmak için dört adet çıkıntılı halojen/LED kask lambası (head lamps) ve genellikle sağ kenara tutturulmuş, lensi belirgin bir dış yayın TV kamerası bulunur.

SAFER Acil İtki Paketi
Özellikle ISS etrafındaki operasyonlarda kullanılan Simplified Aid For EVA Rescue (SAFER), astronotun güvenlik kordonunun kopması halinde uzayda sürüklenmesini engellemek için tasarlanmış bağımsız bir soğuk gaz itki jetpack'idir.

Boyut ve Siluet: Yaklaşık 50×50×25 cm (20 x 20 x 10 inç) boyutlarındadır ve PLSS/SOP grubunun alt kenarlarını ve yanlarını saran geniş bir "U" şeklinde tasarlanmıştır. Ağırlığı dolu halde yaklaşık 38 kg'dır (83−85 lbs).

Görsel Bileşenler: Üzerinde X, Y ve Z yönlerine bakan dörderli gruplar halinde toplam 24 adet küçük, metalik soğuk gaz (GN2 - Azot) lülesi (thruster) bulunur. Her bir lüle, astronota yaklaşık 3−5 lbf (pound-kuvvet) itki sağlar. Dışarıdan bakıldığında bu modül, düz beyaz TMG kumaşının aksine, koruyucu metalik kalkanlar (shrouds) ve siyah delikli lüleleriyle daha endüstriyel, köşeli bir görünüm sergiler.

Karşılaştırmalı Siluet Analizi ve Hikâye Durumu Uygunluğu
Film ve video yapımında, giysinin dış geometrisi anlatılan hikâyenin psikolojik tonunu belirler. Farklı ulusların ve dönemlerin mühendislik felsefeleri, bu siluetlerin hangi hikâye durumuna (story situation) oturduğunu doğrudan tanımlar.

Giysi Tipi    Mimari Karakteristik    Görsel Siluet Özeti    İdeal Sinematik Hikâye Durumu
NASA EMU    Yarı-sert, modüler, önden kontrollü, 4.3 psi basınç.    Belirgin metal kilit halkaları olan, omuzları geniş, devasa sırt çantalı hibrit zırh.    Rutin Yapı/Onarım EVA'sı: Alet kullanımı ve çoklu mürettebat etkileşiminin olduğu standart dış operasyonlar.
Rus Orlan-MKS    Sırttan kapılı (rear-entry hatch), yekpare gövde-kask entegrasyonu, 5.8 psi.    Kaskın gövdeye sabit olduğu, pürüzsüz poliüretan kaplı, boyunsuz ve monolitik devasa görünüm.    Uzun ve İzole EVA: Karanlıkta tek başına çalışan, dış dünyadan tamamen soyutlanmış, otonom astronot teması.
Artemis xEMU / AxEMU    Yüksek mobilite rulmanları, sırttan giriş, gelişmiş toz koruması.    Koyu gri, kırmızı ve lacivert vurgulu (Prada weave), eklemleri insan gibi kıvrılabilen atletik yapı.    Gezegensel Keşif: Ay veya Mars yüzeyinde yürüyüş, diz çökme ve jeolojik numune toplama sahneleri.
Sokol KV-2    Kabin içi (IVA), PLSS yok, önden V-şekilli flap.    Yumuşak kasklı, karından çıkan kalın hortumlara bağımlı, yeşilimsi/beyaz ince tulum.    Kabin İçi / Acil Çıkış: Dar koridorlarda hayatta kalma çabası, fırlatma sarsıntısı ve klostrofobik panik sekansları.

Orlan Serisinin İzolasyon Hissi
Rus NPP Zvezda tarafından tasarlanan Orlan serisinin (güncel MKS modeli) en belirgin farkı, sırt çantasının aynı zamanda astronotun giysiye girdiği kapı (hatch) olmasıdır. EMU'daki modüler kilit halkalarının aksine, Orlan yekpare bir gövdeye sahiptir; kask omuzlarla birleşiktir ve astronot kafasını kaskın içinde çevirir. Daha yüksek çalışma basıncı (5.8 psi) nedeniyle kol ve bacak körükleri çok daha sert, hacimli ve pürüzsüz (poliüretan kaplı) görünür. Bu yapısal katılık, AI videolarında "soğuk, otonom ve yalnız uzay yürüyüşçüsü" hissiyatını mükemmel yansıtır.

Sokol KV-2'nin Klostrofobik Hortum Bağımlılığı
Soyuz uzay araçlarında kullanılan Sokol KV-2, bir kurtarma (rescue) giysisidir. Otonom bir sırt çantası (PLSS) yoktur; astronot yaşam desteği için tamamen kabine uzun hortumlarla (umbilical) bağlıdır. Göğsün tam ortasında bulunan, astronotun manuel olarak çevirebildiği dairesel, mavi anodize alüminyum basınç regülatörü, giysinin imza detayıdır (nominal basınç 0.4 atm, acil durum basıncı 0.27 atm). Karın bölgesinden çıkan bu karmaşık, çelik kordonlu hortum ağı, izleyicide "araca göbek bağıyla bağlı olma" psikolojisini ve olası bir acil durumdaki çaresizliği görselleştirmek için idealdir.

Sayısal Göstergeler, Telemetri ve Uyarı Konvansiyonları
Uzay giysileri, devasa bir veri akışı yönetir. Bu verilerin mürettebata nasıl sunulduğu, sinematik bir sahnede inandırıcılığın (verisimilitude) temel taşıdır. Film yapımcıları genellikle kaskın içine yüzer HUD'lar (Head-Up Display) koysalar da, gerçekte NASA EMU arayüzü son derece pragmatik, fiziksel ve analog-dijital karışımı bir yapıdadır.

Analog ve Dijital Gösterim Biçimleri
DCM'nin ön yüzünde bulunan metin ve etiketler, astronot kaskın içinden doğrudan göremediği için ayna görüntüsü (ters) olarak basılmıştır. Astronot, bileğindeki aynayı kullanarak (wrist mirror) bu yazıları okur.

Oksijen Basıncı: Oksijen basıncı dijital bir ekrana bırakılamayacak kadar kritiktir; bu nedenle DCM üzerinde doğrudan basınca duyarlı çalışan, analog ibreli mekanik bir kadran (gauge) bulunur. Tüm güç sistemleri arızalansa bile bu kadran çalışmaya devam eder. Kadran yeşil (güvenli), sarı (düşük) ve kırmızı (kritik) dilimlere ayrılmıştır.

Kalan Süre ve Telemetri (12-Karakter LCD): DCM'nin üst eğimli yüzeyinde, astronotun çenesini eğdiğinde aynaya ihtiyaç duymadan okuyabildiği 12-karakterlik, segmentli bir alfanümerik LCD/LED ekran yer alır. "Mode Selector Switch" adı verilen küçük bir kol ileri-geri itilerek, bu panelde kalan tahmini oksijen süresi, pil voltajı, soğutma suyu sıcaklığı gibi 16 farklı kritik veri izlenebilir. Dış kameradan bakıldığında bu ekranın soluk yeşil veya sarımtırak şekilde parlaması, sahnenin endüstriyel gerçekçiliğini artırır.

Uyarı Renkleri ve Ses Alarmları (C&W Sistemi)
NASA'nın İkaz ve Uyarı (Caution and Warning - C&W) konvansiyonlarına göre, tehlike durumları belirli eşiklerde görsel ve işitsel alarmları tetikler.

Sarı Uyarı Işığı (Caution): Karbondioksit (CO2) birikimi 8.0 mm Hg (baseline) veya 12.4 mm Hg (gelişmiş) seviyesini aştığında ya da düşük öncelikli bir sensör arızası yaşandığında, DCM üzerinde sarı renkli uyarı lambası yanıp sönmeye (flashing) başlar.

Kırmızı Uyarı Işığı (Warning): Oksijen basıncı kritik bir hızla düşüyorsa (high pressure drop rate) veya mutlak basınç 0.23 atm altına inmişse, kırmızı LED uyarı ışığı şiddetle yanıp söner. Bu durumda giysi, otonom olarak SOP valflerini patlatarak acil durum oksijenini sisteme basar.

Ses Konvansiyonu: Kask içindeki iletişim başlığı (Snoopy Cap) aracılığıyla duyulan alarm sesi standart bir düdük veya bip sesi değildir. C&W sisteminin imza sesi, astronotun dikkatini hemen çeken, dalgalı, frekansı gidip gelen bir "warble" (ötme/titreme) tonudur. Ekip ayrıca test aşamalarında kesintisiz (steady) tonları da duyar. Düşük CO2 uyarısı düşük frekanslı bir warble ile bildirilirken, ani basınç kaybı kulak tırmalayan, yüksek frekanslı agresif bir warble ile karakterizedir.

Arıza Görselliği: Dış Kamera Perspektifinden Felaket Anları
Bir uzay senaryosunda işlerin ters gitmesi, dışarıdan gözlemlenebilen çok spesifik ve vizüel semptomlar doğurur. Bu tarihsel vakalar, yapay zekâ videolarında gerilimi artırmak için görsel tetikleyici olarak kullanılmalıdır.

Termal/Soğutma Arızası ve Aşırı Efor: Vizör Buğusu
Eğer LCVG içindeki sıvı akışı durursa veya astronotun metabolik ısı üretimi sistemin kapasitesini aşarsa, kaskın içi saniyeler içinde ölümcül bir seraya dönüşür. Bu durum uzay yürüyüşlerinin ilk dönemlerinde ciddi kazalara ramak kalmasına neden olmuştur.

Gemini 4 (Ed White): Amerika'nın ilk uzay yürüyüşünde Ed White, giysinin (G4C) vakum altında balon gibi şişip sertleşmesi nedeniyle kapsüle geri dönmekte inanılmaz zorlanmış, kalbi aşırı yorulmuş ve ciddi bir fiziksel tükenmişlik (exhaustion) yaşamıştır.

Gemini 9A (Eugene Cernan): Astronot Cernan, sırtındaki manevra ünitesini (AMU) giymeye çalışırken öngörülenin 4-5 katı efor sarf etmiş ve nabzı dakikada 180 atıma (bpm) ulaşmıştır. Metabolik ısı ve solunum hızı o kadar artmıştır ki, soğutma sistemi çökerek vizörün iç yüzeyini tamamen yoğun bir buğuyla (fog) kaplamış ve astronot geçici olarak tamamen kör olmuştur. Benzer bir olay Gemini 11 görevinde Richard Gordon'un sağ gözünü yakan ter ve vizör buğusuyla tekrarlanmıştır.

Görsel Çıktı: Dışarıdan bakıldığında, şeffaf vizörün iç yüzeyinde opak, süt beyazı bir yoğunlaşma tabakası; sıvı damlacıkları ve karanlıkta kalındığında kaskın iç yüzeyinde ince, kristalize bir buz/kırağı (frost) katmanı görünmelidir. Astronotun yüzü ancak gölgeli, terden sırılsıklam olmuş silik bir form olarak seçilebilir.

Su Seperatörü Arızası: Parmitano Vakası
2013 yılındaki EVA 23 sırasında İtalyan astronot Luca Parmitano'nun başına gelen olay, mikro kütleçekiminde sıvı davranışının ne kadar tehlikeli olabileceğini kanıtlamıştır. PLSS içindeki döner su ayırıcı (rotary separator) tıkandığında, soğutma suyu astronotun havalandırma hortumu (vent loop) üzerinden doğrudan kaskının arkasına pompalanmıştır.

Görsel Çıktı: Dünyadaki gibi aşağı akmayan su, yüzey gerilimi (surface tension) nedeniyle Parmitano'nun kafa tasına, kulaklıklarına (Snoopy cap) ve gözlerine yapışarak amorf, devasa, titrek bir sıvı kütlesi (blob) oluşturmuştur. Dış kameradan çekilen bir yapay zekâ videosunda kaskın içini dolduran ve ışığı mercek gibi kıran devasa bir su balonu yaratmak, bu arızanın en çarpıcı yansıması olacaktır.

Süblimatör Venting: Buhar Jeti Bulutu
EMU'nun atık ısıyı uzaya tahliye etme yöntemi, suyun gözenekli bir plakada buzlandırılıp vakumda doğrudan süblimleşmesine (buharlaşmasına) dayanır.

Görsel Çıktı: Aşırı ısınma veya acil durum tahliyesi (venting) yaşandığında, PLSS'nin yan/arka kısmındaki egzoz valflerinden dışarıya doğru güçlü bir "buhar jeti" fırlatılır. NASA NTRS belgelerine göre, vakumda hızla genleşen bu mikroskobik buz kristalleri bulutu, PLSS'den yaklaşık 3 feet (90 cm) uzağa kadar görünür bir "steam cloud" (buhar bulutu) olarak kalır ve ardından yavaşça dağılır. Sinematik sahnelerde bu beyaz jet akımı, cihazın mekanik solunumunu vurgulamak için kusursuz bir detaydır.

Yapay Zekâ (AI) Video Üretiminde Devamlılık Yönetimi
Seedance 2.0, Sora veya Luma gibi video modellerinin gizli difüzyon uzayı (latent diffusion space), büyük, katı ve iyi tanımlanmış geometrileri (küp, küre) kadreler boyunca taşıma konusunda üstün performans gösterirken; topolojik olarak birbiriyle kesişen ince kabloları, metinleri veya ağ yapılarını saniyeler içinde bozma (morphing) eğilimindedir. Bu fenomen, özellikle uzay giysisi üretirken astronotun kordonlarının uzay boşluğunda yılan gibi birbirine girmesine veya vizördeki yazıların uzaylı rünlerine dönüşmesine yol açar.

Video sahnelerinde sırt donanımının kaymasını önlemek ve inandırıcılığı sağlamak için kullanılacak görsel öğeler, AI algısının önceliklerine göre aşağıdaki tabloda kategorize edilmiştir.

AI Devamlılık Riski    Nesne Sınıfı    Karakteristik Özellik    Prompt Stratejisi / Yönetimi
DÜŞÜK RİSK (Güvenilir Çapalar)    Kask Küresi ve Altın Vizör    Kusursuz küresel form. Çevre yansıması AI tarafından iyi tolere edilir.    Modelin mekânın ışığını vizöre yansıtmasına izin verin. Sabit geometridir.
DÜŞÜK RİSK (Güvenilir Çapalar)    PLSS Sırt Prizması ve SAFER Bloğu    Kalın, sert kenarlı 26x18x10 inç dikdörtgen prizma ve U-şekilli blok.    Hacimsel ifadeler kullanın (massive rectangular block). Sayılabilir lüleler (24 distinct thrusters) modelin dikkati odaklamasına yardımcı olur.
DÜŞÜK RİSK (Güvenilir Çapalar)    DCM (Göğüs Kutusu)    Göğüste sabit, açılı metalik kutu.    Keskin köşeleri AI'ın karakter bütünlüğünü korumasına (anchor) olanak tanır.
ORTA RİSK (Kısa Süreli Planlar)    Renk Kodlu Soketler ve Kamera Lambaları    Kırmızı/mavi SCU kilit halkaları. Kasktaki 4 adet lamba.    AI renkleri kolay öğrenir ancak pan hareketlerinde sayıları artabilir (halüsinasyon). Çok spesifik promptlama gerekir.
YÜKSEK RİSK (Kayma Tehlikesi)    Uzun Hortumlar ve İnce Kordonlar    Sokol'un göbek bağları, EMU LCVG oksijen hortumları.    AI hortumların bağlantı topolojisini unutur. Uçları havada süzülebilir. Dar açılı ve statik çekimler tercih edilmelidir.
YÜKSEK RİSK (Kaçınılmalı)    Küçük Etiketler ve Ters Yazılar    DCM üzerindeki yazılar ve 12-karakterli dijital panel.    Metinler saniyeler içinde bozulur. Yazı yerine "parlayan yeşil dijital ekran" (glowing digital interface) gibi soyut ışık tabanlı ifadeler kullanılmalıdır.

AI Prompt ve Siluet Varyasyonları Sentez Tablosu
Yapay zekâ video oluşturma platformlarında (Seedance 2.0'ın "Özne + Eylem + Çevre + Kamera + Stil + Kısıtlar" şeklindeki 6 adımlı formülü dikkate alınarak), uzay giysisinin her bir dış modülünün inşası için gerekli olan parametreler, İngilizce prompt ifadeleri ve aynı sahnede iki karakteri yalnızca sırttan çekilmiş bir açıda birbirinden ayırt ettirecek varyant önerileri aşağıda sistematize edilmiştir.

Modül    Konum ve Boyut    Renk ve Doku Özellikleri    İşlevsel Rol    İngilizce Devamlılık Çapası (Anchor Prompt)    Karakter Ayrımı İçin Sırttan Siluet Varyantı
PLSS    Sırttan bel hizasına. 66×46×24 cm.    Mat beyaz termal kumaş (TMG), dikişli, rijit köşeler.    Yaşam destek sirkülasyonu, LiOH filtresi, su soğutma.    massive rectangular white life-support backpack covered in thick quilted thermal fabric    Karakter A: Omuzlarda kırmızı komutan şeritleri (Apollo xEMU stili). Karakter B: Düz beyaz (Klasik EMU).
SOP    PLSS alt çerçevesine asılı.    Beyaz kumaş, PLSS'ye göre daha yuvarlak hatlı ve dar.    30 dk acil oksijen kaynağı.    curved white backup-oxygen module seamlessly attached to the bottom edge of the main backpack    Karakter A: Sırtında belirgin çıkıntılı SOP var (EVA modu). Karakter B: SOP çıkarılmış, daha kısa ve küt bir sırt çantası.
SAFER    PLSS/SOP'un alt yanlarını saran U-profil.    Beyaz/metalik gövde, siyah koruyuculu soğuk gaz lüleleri.    Otonom acil durum kurtarma itkisi.    U-shaped rigid maneuvering thruster pack attached below the backpack with small metallic gas nozzles    Karakter A: Alt ve yan kenarlardan taşan, köşeli SAFER itki modülü takılı. Karakter B: Yalnızca yuvarlak hatlı kumaş (SOP) silueti.
EVVA    Omuzlardan boyun kilidiyle çıkan dev küre.    Yansıtıcı altın vizör, şeffaf dış kubbe, yanda beyaz siperlikler.    Radyasyon, kör edici ışık ve mikrometeoroid koruması.    large spherical helmet featuring a highly reflective gold sun-visor mirroring the dark space environment    Karakter A: Kask omuzlardan ayrı ve dönebilir (EMU kilit mekanizması). Karakter B: Kask ve omuzlar yekpare birleşmiş (Orlan-MKS kapı tasarımı).
Lamba / Kamera    Kask üstü sağ ve sol tepe köşeleri.    Beyaz dikdörtgen kutucuklar, sarı halojen ışıma, siyah lens.    Keşif aydınlatması ve TV yayını.    four distinct box-shaped headlamps and a side-mounted TV camera attached symmetrically to the helmet rim    Karakter A: Kaskın tepesinde 4 lamba ve belirgin dikdörtgen anten/kamera çıkıntısı. Karakter B: Tepesi tamamen pürüzsüz düz kask.
DCM & SCU    Göğüs ortası (HUT üzeri).    Gümüş metal kutu, kırmızı/mavi halkalı soketler.    LSS kontrolü, oksijen basıncı okuma, telemetri ekranı.    chest-mounted angular metallic control module featuring an analog pressure gauge and glowing LCD    Sırt siluetinden doğrudan görünmez ancak profilden bakıldığında: Karakter A göğsü şişkin ve düzleştirilmiş; Karakter B (IVA) ince hatlı.
IVA Valfi (Sokol)    Karın merkezi, esnek kumaş üzeri.    Anodize mavi dairesel alüminyum basınç düğmesi.    Kabin içi manuel basınç kontrolü (0.4/0.27 atm).    central blue anodized aluminum circular pressure regulator valve on the chest of a soft spacesuit    Karakter A: Sırt çantası olmayan, göbekten çıkan ince çelik kordonlarla sandalyeye bağlı V-flap siluet.

Sonuç
Uzay giysilerinin araç dışı ve araç içi yaşam destek anatomisi, sadece teknolojik bir yalıtım katmanı olmanın çok ötesindedir. NASA EMU'sunun mekanik olarak doğrudan analog göstergeler (DCM) kullanan 4.3 psi'lık tasarımı, Orlan'ın izolasyonu simgeleyen sırttan kapılı ve daha rijit 5.8 psi'lık mimarisi ile Sokol'un sadece bir göbek bağına dayanan klostrofobik kabin içi yapısı, her biri kendi operasyonel gerçekliğinin fiziksel dışavurumudur.

Film yapımcıları ve Üretken Yapay Zekâ tasarımcıları için, bu geometrik zorunlulukları anlamak elzemdir. Yapay zekâ video difüzyon modelleri (Sora, Seedance 2.0 vb.) karmaşık topolojileri işlerken zamansal tutarlılık sorunları (drifting) yaşasa da, PLSS gibi 26 inçlik rijit blokları, altın vizörlü devasa küreleri ve SAFER'ın belirgin lüle yapısını önceliklendirilmiş devamlılık çapaları (anchors) olarak prompt içine entegre etmek, halüsinasyon riskini minimize eder. Öte yandan, Gemini görevlerindeki vizör buğulanması (Cernan ve White vakaları), C&W sisteminin kritik arızalarda tetiklediği şiddetli warble sesine eşlik eden kırmızı flaşörler ve Parmitano'nun kaskında biriken ölümcül su kütlesi gibi tarihsel vakalar; bir simülasyon veya filmin gerçekçilik katsayısını artıran paha biçilmez arıza görsellikleridir. Sonuç itibarıyla uzay giysisi, üzerinde taşıdığı her bir lüle, soket, hortum ve uyarı göstergesiyle, etrafındaki boşlukla sürdürülen hayatta kalma mücadelesinin en net görsel kanıtıdır.

---

## KAYNAK LİSTESİ (rapor sonunda verildiği hâliyle)

cyberraiden.wordpress.com — Image Generation Prompt Structure for OpenAI's Sora - Cyber Raiden
reddit.com — which AI video tool actually keeps a character consistent? trying to
mangomindbd.com — Seedance 2.0 Complete Guide | AI Video Prompts That Actually Work
en.wikipedia.org — Extravehicular Mobility Unit - Wikipedia
en.wikipedia.org — Primary life support system - Wikipedia
americaspace.com — NASA Hedges On Critical Suit Battery Resupply - AmericaSpace
nasa.gov — One Small Step - NASA
iamchaitanya.wordpress.com — Space Suits! | iamchaitanya - WordPress.com
files.eric.ed.gov — Suited for Spacewalking. Teacher's Guide with Activities for Physical
scifiinterfaces.com — Sci-fi Spacesuits: Interface Locations
scribd.com — EMU Independent Orbiter Assessment Report | PDF | Nature - Scribd
science.gov — redlich-peterson isotherm model: Topics by Science.gov
scribd.com — 1988 Space Shuttle News Manual | PDF - Scribd
slideshare.net — Reference Guide To The International Space Station | PDF
science.howstuffworks.com — How Space Suits Work - Science | HowStuffWorks
grokipedia.com — Simplified Aid For EVA Rescue - Grokipedia
en.wikipedia.org — Orlan space suit - Wikipedia
newspaceeconomy.ca — The Spacesuit: A History of Personal Spacecraft
newspaceeconomy.ca — Analysis of the Spacesuit Market - New Space Economy
research-repository.rmit.edu.au — Towards a Martian Mechanical Counter Pressure Spacesuit
fastcompany.com — NASA's new Prada-designed space suit will go to the moon
dokumen.pub — Handbook of Life Support Systems for Spacecraft and
suzymchale.com — Spacesuits | RuSpace - Suzy McHale
researchgate.net — Pre-space era full pressure suits. Photos are from the Zvezda museum
catacombs.space1999.net — Moonbase Spacesuit in real life- Space: 1999 Continuity Guide
scribd.com — Seedhouse E. Life Support Systems For Humans in Space 2020 | PDF
fliphtml5.com — In-Flight Carbon Dioxide Exposures and Related Symptoms
archive.org — Full text of "NASA Technical Reports Server (NTRS) 19850008580
scribd.com — ISS EVA Systems Checklist 2005 | PDF | Extravehicular Activity | Nasa
reddit.com — On March 18, 1965, Alexey Leonov stepped outside of Voskhod-2 to
en.wikipedia.org — List of spacewalks and moonwalks 1965–1999 - Wikipedia
reddit.com — The helmet filled with water that almost drowned Luca Parmitano
ntrs.nasa.gov — General Disclaimer One or more of the Following Statements may
ntrs.nasa.gov — III _) 44
lumenfall.ai — FLUX.2 [max] vs Wan 2.5 (Preview) — AI Image Model Comparison
fr.scribd.com — 155553main Eva 115 F C | PDF - Scribd
github.com — Seedance_2.0_Complete_Prompting_Guide.md - GitHub
