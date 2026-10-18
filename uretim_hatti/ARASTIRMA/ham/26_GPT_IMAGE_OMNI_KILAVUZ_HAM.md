# 26 — HAM · GPT Image + Gemini Omni 1.1 Flash Film Üretim Kılavuzu (sahibin yapıştırdığı metin)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı ("klavuzlara bir güncelleme atalım"). Metin birebir aşağıda; düzenlenmedi.
> **Kanıt değildir.** Hatta inen satırlar yalnız `../11_SUZME_20261016.md`'de KABUL edilenlerdir.

---

GPT Image + Gemini Omni 1.1 Flash
Film Üretim Kılavuzu
Apex AI Cinema | 15 Ekim 2026 | 24 bölüm | 38 kopyalanabilir şablon

Türkçe uygulama notları ve İngilizce üretim promptları. GPT Image kareleri, Omni image-to-video, devamlılık, ses, kurgu ve yayın.

İçindekiler
Hızlı başlangıç: önce çalışan 30 saniye
Doğrulanmış özellikler ve arayüzde kontrol edilecekler
Süre hesabı: ham video ile bitmiş film
Senaryoyu üretilebilir çekimlere çevir
Kimlik, görünüm ve sahne durumlarını sabitle
Mekânı ve coğrafyayı bir kez kur
Referansların rolü ve doğru yükleme
GPT Image: film karesi promptunu kur
Kareyi düzelt: tek kusura odaklan
Omni'de görselden videoya uygulama
Omni hareket promptu ve kamera dili
G0-G1 devamlılığı ve sahne uzatma
Kamera ekseni, bakış ve tepki planı
Zor hareketleri üretilebilir hâle getir
Tam örnek: dört çekimde yanaşma
Diyalog: yerel ses veya ayrı ses kaydı
Sorunu hangi aşamada çözmelisin?
Kurgu, en-boy oranı ve yayın dosyası
Dosyalar, sürümler ve üretim maliyeti
2 dakika tek kamera ve 16 dakika uzun film
Yeni film için kullanacağın ana çalışma promptu
Bir sahneyi tamamlanmış sayma ölçütü
Sabit EVA kimlik blokların
Kısa sözlük ve kaynaklar
01. Hızlı başlangıç: önce çalışan 30 saniye
Bu kılavuz, GPT Image ile tutarlı film kareleri hazırlayıp Gemini Omni 1.1 Flash ile onları hareketlendirmek için yazıldı. Ana örnekler Apex AI Cinema'nın yatay uzay filmlerine dayanır. Aynı yöntem korku, fantastik ve tarihî filmlere de uygulanabilir. Uygulama notları Türkçe; modele verilecek örnek promptlar ve film replikleri İngilizcedir.

Ana çalışma düzeni

Hikâye ve çekim kartı -> karakter/mekân/nesne referansları -> GPT Image ile sahnenin başlangıç kompozisyonu -> Omni ile hareket -> seçilen kullanılabilir bölüm -> ses ve kurgu -> bitmiş film.

İlk hedef bütün referans arşivini büyütmek değildir. Aynı projeden üç planı sesleriyle birleştirip çalışan kısa bir bölüm çıkarmaktır. Böylece yüz, mekanik tasarım, ritim ve model davranışını gerçek bir sahnede görürsün.

Bir cümlede kahraman, hedef, engel ve sonucu yaz. Filmin sonunda neyin değiştiğini belirle.
Bir karakter referansı, bir ana mekân geniş planı ve gerekli tek önemli nesneyi hazırla.
Üç plan seç: nerede olduğumuzu gösteren geniş plan, tek önemli hareket, hareketin sonucunu veya karakter tepkisini gösteren plan.
Üç başlangıç görselini GPT Image ile oluştur. Görsellerdeki kimlik, el/nesne teması ve başlangıç durumunu kontrol et.
Omni'de her görsel için ayrı hareket iste. Gerçek video süresini ve dosya oranını kontrol et.
Klipleri yan yana koy, geçici diyalog ve ortam sesi ekle. Tek seferde izleyip olayın anlaşılır olup olmadığına bak.
Çalışan örnekleri referans alarak filmin kalanını üret. Aynı sorunu tekrar tekrar çoğaltma.
Buradaki yöntemler önerilen üretim alışkanlıklarıdır; modelin her isteği tam karşılayacağına dair garanti değildir. Ürün özellikleri sonraki bölümde kaynaklarıyla ayrılmıştır. Bu kılavuz hazırlanırken yeni film klipleri üretilip performans testi yapılmadı.

Üç soruluk seçim

Bu planda kim var? Hangi olay veya bilgi değişiyor? Sonraki planın başlangıcıyla uyumlu mu? Üçü de açıksa küçük kozmetik kusurlar yüzünden sahneyi baştan tasarlama.

02. Doğrulanmış özellikler ve arayüzde kontrol edilecekler
Kılavuzun doğrulama tarihi 15 Ekim 2026. Kullanıcının 'Omni Flash 1.1' diye andığı modelin resmî adı Gemini Omni 1.1 Flash. GPT Image ifadesi görsel üretim ailesi için kullanılıyor; belirli bir API sürümüne geçiş veya model değiştirme önerisi yapılmıyor.

Konu    Resmî kaynakta görülen    Bu iş akışına etkisi
Video modeli    Gemini Omni 1.1 Flash. S1    Model adını üretim kaydına yaz.
Süre ve ses    10 saniyelik video ve yerel ses üretimi tanıtılıyor. S1    Ham kaynak süresini yine dosyadan kontrol et.
Görsel referans    Beşe kadar fotoğraftan video desteği belirtiliyor. S1    Bu sayı, beş zaman anahtarı veya beş sabit kamera açısı demek değildir.
Video düzeltme    Sahne uzatma, video düzenleme ve çok turlu düzenleme tanıtılıyor; erişim plan/bölgeye göre değişebiliyor. S1    Kullandığın hesapta bulunan işlevle ilerle.
Oran    Yüklenen referansın oranının videoya yansıyacağı açıklanıyor. S2    Yanlış oranlı kaynak görseli videodan önce düzelt.
GPT Image    Referansın rolünü belirtme ve düzenlerken korunacak ayrıntıları açıkça söyleme resmî prompt rehberinde örnekleniyor. S3    Kimlik ve mekânı her seferinde yeniden tarif etmekle yetinme; doğru dosyaları da ekle.
Aşağıdakileri bu kaynaklardan evrensel özellik olarak doğrulamadım: bütün arayüzlerde ayrı başlangıç/bitiş karesi yuvaları, kesin kare kilidi, sabit seed, her hesap için aynı günlük kota, sabit üretim süresi, belirli bir çözünürlük veya fps seçeneği. Bunları varsayarak film planı kurma.

API ve sohbet arayüzü ayrımı

Bir API parametresinin belgede bulunması, sohbet ekranında aynı ayarın bulunduğu anlamına gelmez. API kullanıyorsan gerçek model kimliğini ve o modele ait güncel şemayı ayrıca kontrol et. Buradaki temel yöntem web arayüzüyle de uygulanabilir. S4

Birden fazla görsel yüklemek ile bir görseli zorunlu ilk, başka bir görseli zorunlu son kare yapmak farklı kontrollerdir. İkinci işlevi ancak seçtiğin Omni arayüzü açıkça sunuyorsa kullan. Promptta 'exact final frame' yazmak yeni bir ürün özelliği oluşturmaz.

03. Süre hesabı: ham video ile bitmiş film
Hedef    10 sn kesintisiz final parçası    8 sn final parçası
2 dakika    12 parça    15 parça
4 dakika    24 parça    30 parça
16 dakika    96 parça    120 parça
Bu tablo finalde gerçekten kullanılan süreler içindir. Modelden 10 saniye almak, her dosyanın bütününün kullanılabilir olduğu anlamına gelmez. Baştaki hazırlık, sondaki bozulma veya gereksiz bekleme kesildiğinde toplam azalır.

Örnek hesap

24 ham klip x 10 sn = 240 sn kaynak. Her klipten 2 sn çıkarırsan 24 x 8 = 192 sn, yani 03:12 kalır. Ortalama 8 sn kullanılabilir bölümle 04:00 doldurmak için 30 kaynak gerekir. Bu bir planlama örneğidir; model için ölçülmüş başarı oranı değildir.

Mevcut 24 x 10 formatını aynen koruyacaksan her final parçayı gerçekten 10 saniyeye tamamla. Eksik bir hareket için uyumlu devam üretimi veya olayın sonucunu gösteren ek plan kullanabilirsin. Sırf süre doldurmak için bozuk görüntüyü uzatmak, aynı hareketi döngüye almak veya bütün filmi yavaşlatmak ritmi bozar.

Kurguya serbestlik tanıyorsan 10 saniyeyi kaynak üretim bütçesi olarak düşün. Bir tepki 3 saniye, bir yaklaşma 7 saniye kullanılabilir. Önce istenen toplam süreyi hesapla, sonra buna yetecek kullanılabilir kaynak üret. 24 çekim fikriyle 24 kesintisiz final parçasını aynı şey sayma.

FORMUL-01 | Kullanılabilir süre planı

target_seconds = 240
average_usable_seconds = 8
estimated_source_count = ceil(240 / 8) = 30

final_duration = sum(used_clip_durations)
                - transition_overlaps
                + added_title_or_credit_duration
Bindirmeli geçişler toplam süreyi azaltabilir. Başlık ve jenerik yeni klipse süreyi artırır. Kesin dört dakika için son başlığı mevcut son planın içine yerleştirmek ve düz kesmelerle çalışmak daha kolaydır.

Bir klibin teknik olarak 10 saniye olması, içinde 10 saniyelik olay bulunduğunu göstermez. Görüntü değişmiyorsa konuşma yeni bilgi vermeli veya beklemenin dramatik bir nedeni olmalı.

04. Senaryoyu üretilebilir çekimlere çevir
Önce amaç ve sonuç, sonra görüntü sayısı. 'Gemi istasyona gider' yerine 'Pilota kalan tek dönüş yolunun bu istasyon olduğunu göstermek' gibi bir amaç yaz. Aynı amacı tekrar eden planları ayıkla.

Kart alanı    Yazılacak bilgi
Çekim / süre    C01; hedef kullanılabilir süre; ham kaynak hedefi.
Dramatik işlev    Yeni bilgi, karar, tehlike, hareket veya sonuç.
Karakter / nesne    Hangi görünüm ve durum referansları kullanılacak?
Başlangıç    Görüntüde zaten mevcut olan durum.
Ana değişim    Bu klipte gerçekleşecek tek baskın olay.
Bitiş    Sonraki çekimin ihtiyaç duyduğu durum.
Kamera    Plan ölçeği, yön, sabit veya tek baskın hareket.
Ses    Konuşmacı, kısa replik, yerel ses veya post prodüksiyon seçimi.
Dosyalar    GPT Image girdileri; Omni girdileri; seçilen sonuç.
KART-01 | Doldurulabilir çekim kartı

SHOT_ID: C01
STORY_PURPOSE: [what changes for the viewer]
TARGET_USABLE_DURATION: [seconds]
CHARACTERS_AND_STATES: [reference IDs]
START_STATE: [what is already true]
PRIMARY_ACTION: [one main action]
END_STATE: [what must be true next]
CAMERA: [framing, angle, movement]
DIALOGUE: [speaker + English line]
AUDIO_MODE: [native / post-production]
GPT_IMAGE_INPUTS: [actual attached references]
OMNI_INPUTS: [approved shot image; optional role references]
CONTINUITY_NOTES: [screen direction, light, props]
Her klipte tek baskın olay demek kadrajın donması demek değildir. Oyuncu bir kontrolü çevirirken hafif kamera yaklaşması olabilir. Sorun, aynı klipte kapıyı açma, yürüme, oturma, kask çıkarma ve kalkış istemektir.

Bir aksiyon dizisinin en az bir geniş yerleşim planı olsun. Mekanik detayın arkasından sonucu veya karakter tepkisini göster. Birbirine benzeyen beş düğme yakın planı olayın ilerlediğini hissettirmeyebilir.

Bilgi dağıtımı

Açılışta görünür tehlike veya anlaşılır soru; ortada değişen plan; son bölümde kararın sonucu. İzleyicinin anlaması gereken kritik bilgiyi yalnızca bir göz kırpmasına veya belirsiz ışık değişimine bağlama.

05. Kimlik, görünüm ve sahne durumlarını sabitle
Her karakterin yüzünü, saçını, yaş aralığını, beden oranını ve kıyafetini kısa bir kimlik bloğunda sabitle. Metin ile onaylı görsel birlikte çalışır. Sadece aynı adı kullanmak, aynı yüzün geleceğini garanti etmez.

Referans türü    Sabit kalacaklar    Durumla değişebilecekler
İnsan    Yüz, yaş, ten, beden, takım kesimi, bant/rozet tasarımı    Bakış, ifade, poz; önceden tanımlı kask açık/kapalı sürümü
Uzaylı    Baş silüeti, göz sayısı/konumu, deri, kıyafet    Bakış ve tek hareket; yeni uzuv veya yüz şekli yok
Mekân    Kapı, pencere, koltuk, platform ve panel yerleşimi    Aynı mekânın ışık/hasar sürümü
Araç    Burun, motor, kapı ve bağlantı geometrisi    Motor açık/kapalı, ayrık/bağlı durum
Nesne    Boyut, malzeme, menteşe, tutma noktası    Kapalı/açık, katlı/açılmış, boş/dolu
Durumu dosya isminde de ayır: HATCH_CLOSED_v01, HATCH_OPEN_v01; COLLAR_OPEN_v01, COLLAR_LOCKED_v01. Aynı prompta iki zıt durumu eşit ağırlıkta referans vermek başlangıç karesini belirsizleştirir.

REF-01 | Genel karakter referansı

Create a character reference sheet for one original adult astronaut.
Show the same character in a full-body front view, a three-quarter view,
and a clear head-and-shoulders portrait on a neutral grey background.
Preserve one consistent face, age, skin tone, hairstyle and body shape.
Outfit: [fixed suit description and badge geometry].
Neutral expression, even lighting, readable proportions and materials.
No labels, captions, added emblems or watermark.
This is a reference sheet, not a frame from the finished film.
Çok panelli kart, tasarımı incelemek içindir. Son video girdisi olarak oyuncunun aynı anda üç kez göründüğü bu kartı kullanma. İlgili görünümü ayrı kaynak olarak hazırla veya film karesini bu karttan türet.

Sohbeti çalışma belleği gibi kullan
Her sahne grubunun başında gerekli referansları yeniden ekle ve görevlerini belirt. Uzun sohbetin her ayrıntıyı kusursuz koruyacağını varsayma. Başka bir modele geçerken GPT Image'ın konuşma geçmişi Omni'ye taşınmaz.

Sabit kimlik bloğunu bir kez doğru yazıp kopyala. Her planda yeni sıfatlar ekleyerek karakteri fark etmeden değiştirme. Kıyafet değişiyorsa yeni durum sürümü oluştur; eski referansı sessizce yenileme.

06. Mekânı ve coğrafyayı bir kez kur
Önce boş mekân geniş planı, gerekiyorsa ters açı ve ana nesne detayı hazırla. Kimin nerede durduğunu, giriş/çıkışın yerini ve ana ışığın yönünü belirle. Yakın planlar bu coğrafyadan türesin.

REF-02 | Mekân referansı

Create an empty location reference for one compact orbital control room.
Horizontal 16:9. Two fixed seats face a curved forward window.
A round doorway is on the rear wall; one waist-height console is on the right.
Keep all architecture coherent, with a clear floor and fixed proportions.
Cool blue Earth light enters from the forward window.
Amber practical lights remain inside the room.
Photorealistic cinematic materials, readable shadows, fine film grain.
No people, readable lettering, added logos or watermark.
REF-03 | Araç ve mekanizma referansı

Create a three-quarter reference view of one compact rescue spacecraft.
One short rigid nose docking collar, one small side hatch,
and two fixed rear engines. The hatch is CLOSED in this reference.
Make the docking collar and hatch hinge clearly readable.
Coherent graphite-and-ivory geometry, neutral dark background.
No people, captions, readable markings, extra arms or extra engines.
Yeni kamera açısında modelin görmediği bir duvarı uydurması gerekebilir. O duvar sonraki sahnelerde önemliyse ters açı referansını baştan oluştur. Her yakın planda kapının başka duvara taşınmasına izin verme.

Dev gezegen ölçeği için ortak bir yerleşim belirle: gezegenin eğri ufku, geminin göreli büyüklüğü ve ışık yönü. Her planda 'dev gezegen' demek tek başına aynı coğrafyayı korumaz. Hangi çekimde gezegenin görünmeyeceğini de açıkça yaz.

Dünya ışığı ile yerleşimi eşleştir

Dünya kadrajın solundaysa yüzlerde baskın mavi ışığın nedensiz biçimde sağa geçmesini önle. Ters açıya geçtiğinde ekranın sağı/solu değişebilir; ışığın dünyadaki gerçek yönünü takip et.

07. Referansların rolü ve doğru yükleme
Dosya adını prompta yazmak dosyayı modele yüklemek değildir. 'Reference 1' ifadesi ancak gerçekten eklediğin görseli işaret ediyorsa işe yarar. Her üretimde yükleme sırasını ve rolünü açık tut.

Aşama    Örnek gerçek girdiler    Görev
GPT Image    1: karakter; 2: mekân; 3: nesne durumu    Bunlardan tek bir temiz film karesi oluşturmak.
Omni temel akış    Onaylı C01_START görseli    Karedeki kompozisyonu hareketlendirmek.
Omni ek referans    Arayüz uygunsa gerekli tek yüz veya nesne referansı    Kimliği/tasarımı desteklemek; ikinci sahne eklemek değil.
REF-04 | GPT Image için rol tanımı

Use the attached references in this order:
Image 1: character identity and fixed outfit.
Image 2: location architecture and light direction.
Image 3: the prop in its CLOSED starting state.
Create ONE cinematic film frame combining these roles.
Do not reproduce a contact sheet or combine several camera angles.
REF-05 | Omni'ye birden fazla görsel gerekiyorsa

Image 1 is the primary composition for this shot.
Image 2 is an identity reference only; do not introduce another person.
Keep the scene, framing and starting state from Image 1.
Use Image 2 only to preserve the same face and outfit.
Generate one continuous shot, not a montage.
Başlangıç görseli ile yardımcı kimlik referansının farklı oranları veya ışıkları varsa önce tek görselle dene. Referans sayısını artırmak her sorunu çözmez. Aynı kişinin farklı yaşlarda iki yüzünü veya açık/kapalı aynı nesneyi rol belirtmeden birlikte verme.

Bir referansın görevi palet veya malzemeyse bunu söyle; o referansın içindeki başka karakterleri kadraja taşımak gerekmez. Bu rol ayrımı OpenAI'ın resmî görsel prompt rehberindeki yaklaşımıyla uyumludur. S3

08. GPT Image: film karesi promptunu kur
Görsel promptu o anın fotoğrafını tarif eder. Hikâyenin tamamını veya hareketin bütün aşamalarını tek kareye doldurma. Başlangıçta açık mı kapalı mı, el nesneye zaten değiyor mu, iki araç arasındaki mesafe nedir: bunlar net olsun.

IMG-01 | Ana başlangıç karesi şablonu

Use the attached references according to their stated roles.
Create ONE photorealistic cinematic film still, horizontal 16:9.
SCENE: [location, time and current light state].
CHARACTERS: [fixed identity blocks; exactly who is visible].
FRAMING: [wide / medium / close-up; camera direction].
STARTING STATE: [what is already true before the action].
PLACEMENT: [screen positions, gaze and contact points].
VISIBLE DETAILS: [only the important props and their current states].
LIGHT: [one coherent direction and palette].
LOOK: natural skin and materials, restrained anamorphic character,
fine 35 mm film grain and readable shadows.
Preserve reference faces, outfits and set geometry.
No added readable text, subtitles, unrelated emblems or watermark.
IMG-02 | Doğru başlangıç örneği: kapak henüz kapalı

Use the character and closed-hatch references.
Horizontal 16:9 cinematic medium shot at eye level.
The adult engineer is already braced beside the exterior service hatch.
Her right glove already grips the hatch handle. Both feet are stable.
The hatch is fully CLOSED and its single top hinge is clearly visible.
Her face and closed visor match the reference exactly.
Cool blue planet light, restrained amber practical light.
No opening motion yet, no additional tools, no added text.
'Kapıyı açar, içeri girer, pilota bakar' bir başlangıç karesi tarifi değildir. Kapalı kapı ve tutulan kol başlangıçtır; açılma videonun hareketidir. Sonraki çekim kapı açıkken içeride başlayabilir.

Kadrajda hareket payı bırak
Bir kolun döneceği yer, karakterin yürüyeceği boşluk veya geminin yaklaşacağı aralık başlangıç karesinde bulunmalı. El kadrajın dışında ama hareket el gerektiriyorsa model onu sonradan uydurmak zorunda kalır. Önemli temas noktasını görünür kur.

Ağır karanlıkta yüz ve nesne okunmuyorsa videoya geçmeden düzelt. Çok yoğun grain veya her yerde sis yerine malzeme, silüet ve seçilebilir gölgeler iste. Son film dokusunun bir kısmını kurgu sonunda tutarlı biçimde ekleyebilirsin.

09. Kareyi düzelt: tek kusura odaklan
Başlangıç görselindeki hata videoda çoğalabilir. Yanlış yüz, fazla el, hatalı menteşe, olmayan bağlantı noktası veya yanlış kapak durumunu video promptuyla telafi etmeye çalışma.

EDIT-01 | Yerel nesne düzeltmesi

Edit the supplied frame. Change only the service hatch:
make it fully closed, matching the attached closed-state reference.
Preserve the character's face, body, glove contact, camera angle,
lighting, background architecture and every other object.
Do not restyle the image or add new equipment.
EDIT-02 | Kimliği geri getirme

Edit the supplied film frame using the attached identity reference.
Restore only the character's original facial identity and hair.
Keep the existing pose, expression, helmet, suit, lighting,
camera framing and background unchanged.
Do not replace the location or change the shot's starting state.
EDIT-03 | Yeni bakış açısı

Create a new camera angle of the SAME established scene.
Use the attached master shot for world layout and light direction,
and the character reference for identity.
New framing: [specified camera position and shot size].
Current story state: [unchanged props and positions].
Do not mirror the set or move the doorway to a different wall.
Yeni bir kamera açısı istemek her pikselin sabit kalacağı küçük bir düzeltme değildir. Mekân perspektifi değişir. Bu nedenle yeni açıyı ana yerleşimle karşılaştır; yalnızca yüzün benzediğine bakma.

Düzeltme sınırı

Aynı yapısal hata iki kontrollü düzeltmede kalıyorsa bunu bir çalışma tercihi olarak yeniden tasarla: hareketi böl, başka açı seç veya sonucu kesmeyle göster. Bu sayı model kuralı değildir; üretimin sonsuz tekrara dönmesini önleyen pratik bir sınırdır.

Bir düzeltmede hem yüzü, hem ışığı, hem takımı, hem mekânı değiştirirsen neyin işe yaradığını ayıramazsın. Yüz doğruysa onu yeniden tasarım konusu yapma.

10. Omni'de görselden videoya uygulama
Gemini'nin resmî yardım akışı bilgisayarda video oluşturmayı açmayı, görsel eklemeyi ve prompt göndermeyi açıklıyor. Arayüz adları zamanla değişebilir; hesabında görünen video oluşturma bölümünü kullan. Referans eklenen içerikte oran kaynağı takip ettiği için görseli önceden doğru oranda hazırla. S2

Onaylı başlangıç görselini aç; doğru dosya ve sürüm olduğundan emin ol.
Video oluşturma bölümünde o tek film karesini yükle. Çok panelli karakter kartını onun yerine koyma.
Aşağıdaki hareket promptlarından uygun olanı ekle. Görselde zaten görülen bütün sahneyi uzun bir roman gibi yeniden tarif etme.
Ses seçimini açık yaz: yerel ses mi, sadece ortam sesi mi, konuşmayı kurgu sırasında mı ekleyeceksin?
Çıktıyı indir; sadece küçük oynatıcı ön izlemesine dayanarak karar verme.
Normal hızda baştan sona izle. Yüz, temas, nesne durumu ve hareketin sonucuna bak. Geçerli bölümün giriş/çıkışını not et.
Kılavuzdaki START adı, görselin planlanan başlangıç kompozisyonu olduğunu anlatır. Ayrı bir kare kilitleme kontrolü yoksa birebir ilk kare veya son kare eşleşmesi garanti edilmez. Kompozisyon belirgin sapıyorsa daha kısa ve açık hareket isteğiyle yeniden dene.

Omni'nin düzenleme özelliği hesabında bulunuyorsa iyi bir videonun belirli kusurunu düzeltmeyi deneyebilirsin. Her düzenlemeden sonra çevredeki yüz ve nesneleri de yeniden kontrol et. İstenen yerel değişim, diğer piksellerin kesin korunacağı anlamına gelmez.

Dışarıdan araç adı taşıma

Veo, Flow veya başka bir serviste gördüğün düğme, seed veya başlangıç/bitiş yöntemi Omni'de de varmış gibi davranma. Kullanılan model ve arayüz aynı olmalı.

11. Omni hareket promptu ve kamera dili
Video promptunun ana işi zaman içindeki değişimi tanımlamaktır. Başlangıç fotoğrafı mekânı ve kimliği taşır; prompt ana hareketi, kamera davranışını, bitiş durumunu ve sesi tarif eder.

VID-01 | Genel image-to-video şablonu

Use the supplied film frame as the visual basis for one continuous shot.
Target duration: 10 seconds. Horizontal 16:9.
PRIMARY ACTION: [one clear action from the visible starting state].
CAMERA: [locked / one slow movement].
END STATE: [the useful result to hold briefly].
Preserve the existing faces, outfits, prop geometry and light direction.
Keep all established contact points physically coherent.
No cuts, extra people, new equipment or added captions.
AUDIO: [native dialogue / ambience only / post-production speech].
VID-02 | Kapak açılma örneği

One continuous 10-second shot from the supplied frame.
Keep the camera locked. The engineer's glove already holds the handle.
She opens only the existing hatch on its single visible hinge,
then holds it open. Her boots remain braced and her body stays in place.
Preserve her face, closed visor, gloves and all surrounding geometry.
No walking, extra hinge, new tool or passenger compartment reveal.
Audio: restrained suit and hinge sounds only; no speech or music.
İstek    Kamera davranışı    Pratik kullanım
Locked camera    Kamera konumu ve yönü sabit    Mekanik temas veya önemli nesne detayı.
Slow push-in    Kamera konuya yavaşça yaklaşır    Karar veya tehdit; konu ayrıca az hareket eder.
Pan    Kamera bulunduğu yerden yön değiştirir    Aynı geniş mekânda başka şeyi göstermek.
Tracking    Kamera özneyle birlikte yer değiştirir    Kısa kontrollü hareket veya araç yaklaşması.
Pull-back    Kamera uzaklaşır    Ölçek, coğrafya veya sonucun açılması.
Kamera ve özne hareketini ayrı yaz. 'Kamera sabit, astronot platforma doğru süzülüyor' nettir. Aynı anda yörünge dönüşü, hızlı zoom, kesme, pan ve koşu istemek sahnenin kontrolünü zorlaştırır.

Odak uzunluğu ve film dokusu yaratıcı yönlendirmedir. '35 mm film look' ile '35 mm lens' aynı şey değildir. Bir planda üç farklı lens isteme; istediğin kadraj ve bakış açısını öne çıkar.

12. G0-G1 devamlılığı ve sahne uzatma
A. Aynı hareketi sürdürmek
Onaylı videonun son kullanılabilir, net karesini çıkar. Son dosya karesi bozuk veya hareket bulanıksa daha erken temiz kareyi seç. Bu kareyi sonraki klibin kompozisyon referansı yap. Hareketin yönünü ve o anda gerçekleşmiş durumları açıkça yaz.

CONT-01 | Aynı açıdan devam

Continue the same scene from the supplied clean end frame.
Keep the same camera position, character identity and light direction.
Current state: [what has already happened].
Next action: [one continuation, without repeating the previous action].
Do not reset the prop, reopen a closed hatch or change the environment.
End with [the next clear state].
B. Yeni çekime kesmek
Yeni açı için bozuk bir son kareyi tek kaynak yapma. Ana karakter ve mekân referanslarına geri dön; önceki olayın sonucunu yeni karede koru. 'Kapak zaten açık, mühendis içeride' gibi açık bir durum yaz.

CONT-02 | Kesmeyle yeni açı

Create the next shot of the established scene using the original references.
The previous action has already finished: [state].
New camera angle: [angle and shot size].
Keep the same identities, set layout, lighting and prop states.
This is a new shot, not a reset of the story.
C. Başlangıç ve bitiş görseliyle çalışma
Seçtiğin arayüz Omni için iki ayrı kare rolünü açıkça sunuyorsa G0 başlangıç ve G1 bitiş olarak kullan; önce kısa bir sahnede dene. G0 ve G1 aynı karakteri, aynı mekânı ve tek makul değişimi göstermeli. Aksi durumda beş referans yükleme desteğini bu özellik yerine sayma.

Durum    Uygulanabilir yol
Yalnızca bir görsel girdisiyle çalışıyorsun    G0'ı görsel temel yap; hareketi ve istenen sonucu tarif et.
İki görsel var ama ayrı zaman rolleri yok    İkisini zorunlu ilk/son kare gibi sunma. Ana kompozisyon ve tasarım referansı rollerini açıkla.
Başlangıç/bitiş kontrolleri gerçekten mevcut    G0-G1 geçişini dene; hareketin ortasını ve son durumunu yine kontrol et.
Uzatma özelliği mevcut    Seçilen sahneyi uzatmayı dene; yüz, yön ve ses devamlılığını yeniden izle.
Arka arkaya her yeni klibi bir öncekinin giderek bozulan karesinden üretmek kaliteyi sürükleyebilir. Orijinal referansları koru; açı değişiminde veya kimlik sapmasında temiz kaynaklara dön. Kesin sıçramasız tek çekim zorunlu değilse anlamlı bir kesme çoğu zaman daha verimlidir.

13. Kamera ekseni, bakış ve tepki planı
Karakterin sağa baktığı yakın plandan sonra karşısındaki kişiyi de aynı yöne baktırırsan konuşma ilişkisi kopabilir. Önce mekânın geniş planında iki kişinin yerini kur. Çekimler arasında bu dünya yerleşimini koru; sadece ekranın solunu ezberleme.

Şema öğesi    Konum / anlam
A ve B    Karşılıklı konuşan karakterler; aralarındaki hat eksen.
Kamera 1 ve Kamera 2    Eksenin aynı tarafında; bakış ilişkisi daha kolay korunur.
Diğer taraf    Eksen aşılırsa yeni coğrafyayı görünür biçimde kur.
Şema: A-B konuşma ekseninin aynı tarafındaki kamera konumları bakış ilişkisini korumayı kolaylaştırır. Eksen aşılacaksa yeni coğrafyayı görünür biçimde kur.

Ters açı çekildiğinde ekranın sağı ve solu doğal olarak değişebilir. 'Soldaki kişi hiçbir zaman sağa geçmesin' gibi mekanik bir kural yerine kimin kimin karşısında olduğunu, pencereyi ve ışık yönünü takip et.

CAM-01 | Tepki planı istemi

Use the established character and location references.
Create a medium close-up of the listener, looking toward the speaker
just off-camera to the LEFT, matching the established conversation axis.
The new information has already been heard.
Starting expression: clear concern, without exaggerated crying.
Same face, outfit, helmet state and light direction.
Hands out of frame; no new prop or screen text.
Bir emir, tehdit veya büyük açıklamadan sonra dinleyen kişinin tepkisi izleyiciye olayın ağırlığını anlatır. Sadece konuşan kişiye ve makine detayına kesmek, sahnenin insan tarafını eksik bırakabilir.

Her sahneye otomatik bir tepki klibi ekleme. Tepki yeni bir karar veya anlam yaratıyorsa kullan. Aynı yüzün aynı ifadeyle art arda görünmesi süre doldurmaya dönüşebilir.

14. Zor hareketleri üretilebilir hâle getir
Hareket    Başlangıç karesini nasıl kur?    Videoda iste
Yürüme    Zemin düzlemi, iki ayak, temas gölgeleri ve gidilecek boşluk görünür.    Sabit veya basit takip kamerasıyla kısa, doğal birkaç adım.
Kol/mandal çevirme    El kolu zaten tutuyor; tek mekanizma ve yön okunuyor.    Bir dönüş ve bitişte sabit tutuş.
Kapı açma    Kişi yerinde, el kolda, kapı kapalı, menteşe görünür.    Yalnızca kapının tek menteşeden açılması.
İçeri geçme    Önceki planda kapı açılmış.    Gerekirse kesmeyle kişinin zaten içeride olduğu yeni plan.
Kask durumu    İstenen açık/kapalı sürüm referansla kurulmuş.    Durumu sabit tut; çıkarma hareketi gerekiyorsa ayrı test et.
EVA geçişi    Kısa mesafe, kontrollü yön, tek emniyet bağı, hedef platform görünür.    Tek yavaş yer değiştirme; yakalama ve yürüme ayrı plan olabilir.
Uzaylı oyunculuğu    Baş, göz, kıyafet ve poz ilk karede doğru.    Bir açık eylem: baş çevirme veya bakışı yöneltme.
Kenetlenme    İki araç tek geniş planda anlaşılmış; bağlantı biçimi sabit.    Yaklaşma, temas ve sonuç için uygun ayrı planlar.
Yürüyüş kayıyorsa
Önce görseli kontrol et: ayaklar zemine değiyor mu, perspektif doğru mu, gidilecek alan var mı? Gövdenin kamerayla sabit kalması istenirken ayaklara uzun yürüyüş yazmak tutarsızlık yaratabilir. Kamerayı sabitle, mesafeyi kısalt ve birkaç adımlık deneme yap. Hâlâ sorun varsa varışa kes veya farklı kadraj kullan.

ACT-01 | Kısa yürüyüş

One continuous shot. Keep the camera fixed.
The character takes two short natural steps forward on the visible floor.
Each foot plants before the other advances, with coherent contact shadows.
Preserve body proportions, clothing and the stationary room geometry.
No sliding backward, camera orbit, running or additional action.
Uzay yürüyüşü ve mekanizma
Dış uzayda hareketi zeminde yürüme gibi tarif etme. Aracın veya platformun göreli hareketini, kişinin tutunma noktasını ve emniyet bağının ucunu belirt. Gerçekleşmiş bir temastan başlamak, aynı klipte yaklaşma-tutma-kilitlenme istemekten daha kolay kontrol edilir.

Bir çekme kolu, motor veya emniyet bağı hikâyede önemliyse referans tasarımında baştan bulunsun. Kriz anında yeni bir cihazın ortaya çıkması hem devamlılığı hem de dramatik çözümün inandırıcılığını zayıflatır.

Uzaylı tasarımı
İlk üretimde tek, okunabilir bir baş silüeti ve sabit kıyafet seç. Çok sayıda bağımsız dokunaç veya sürekli biçim değiştirme gerekiyorsa önce o hareketin küçük bir denemesini yap. Karakterin kişiliğini ses, duruş ve karar üzerinden kurabilirsin; her planda anatomisini yeniden icat etme.

15. Tam örnek: dört çekimde yanaşma
Bu bölüm yeni bir filmin tamamı değildir; aynı olayın referans, başlangıç durumu, hareket ve sonuçla nasıl üretileceğini gösteren bağımsız bir örnektir. Varsayım: R01 tek gemi, R02 istasyon ve sabit halka, R03 pilotun onaylı kokpit görünümü. Bu dosyaları önce gerçekten üretip yüklemelisin.

C01 - Nerede olduğumuzu göster
EX-01-I | C01 / GPT Image

Use Image 1 for the spacecraft and Image 2 for the station.
One horizontal 16:9 cinematic exterior wide shot.
The small ivory spacecraft is on the LEFT, facing the station on the RIGHT.
The station's one fixed docking collar is visible.
A huge blue planet curves below both objects, lit from frame-left.
A clear safe gap remains between craft and station.
Both structures match the reference geometry. No added text.
EX-01-V | C01 / Omni

One continuous 10-second shot from the supplied composition.
Hold the wide camera. The spacecraft makes a slow controlled approach
toward the station, ending with a visible gap still remaining.
Keep the planet, light direction and station geometry stable.
No contact, extra engine or cut. Ambience only; no speech or music.
C02 - Tek teması göster
EX-02-I | C02 / GPT Image

Use the same vehicle and station references.
Horizontal 16:9 close exterior view of their EXISTING docking collars.
The two collars are already precisely aligned, with a small visible gap.
Both rigid surfaces, attachment shapes and surrounding hulls are clear.
No people, moving arms or open hatch. Same cool planet light.
EX-02-V | C02 / Omni

Use a locked close camera for one continuous shot.
The spacecraft moves a short straight distance until the two existing
collars meet flush, then holds still.
Preserve the rigid metal geometry and the visible alignment.
No impact bounce, folding arm, hatch opening or new object.
Audio: one restrained contact sound; no speech or music.
C03 - İnsan sonucunu ver
EX-03-I | C03 / GPT Image

Use the pilot's approved COCKPIT outfit reference and the cockpit reference.
One horizontal 16:9 medium close-up at eye level.
The pilot is already seated and secured, looking toward the console.
Starting expression: calm relief after successful docking.
Same face, hairstyle, outfit and helmet state as this interior reference.
A stable station hull is visible outside. No readable screen text.
EX-03-V | C03 / Omni

Keep the camera fixed. The seated pilot gives one clear relieved nod.
The cockpit and station outside stay stationary relative to each other.
Preserve the reference face and outfit; no helmet removal or new action.
Audio: low cockpit ambience only. Dialogue will be added in editing.
Post prodüksiyon repliği: 'We're connected.' Ekran yazısı gerekirse tek kısa teyit ekle. İyi bir görüntüde sırf bu repliği üretmek için yüzü tekrar oynatmak zorunda değilsin.

C04 - Bağlantıyı geniş planda doğrula
EX-04-I | C04 / GPT Image

Use the same spacecraft and station geometry.
Horizontal 16:9 exterior wide shot AFTER docking.
The existing nose collar is already connected flush to the station collar.
The ship remains left, station right, the same blue planet below.
Show a clear rigid connection and stable spacing.
No new ship, towing cable, loose arm or atmosphere fire.
EX-04-V | C04 / Omni

Use a very slow pull-back on the already docked assembly.
Keep both rigid structures fixed relative to each other.
The pull-back reveals the scale of the planet and station.
No renewed approach, separation or change to the docking joint.
Ambience only; no speech or music.
Dört planın iş bölümü

C01 coğrafya; C02 hareket; C03 insan tepkisi; C04 sonucun kanıtı. Aynı kenetlenme olayını dört kez tekrarlamak yerine her plan farklı bir bilgi taşır.

16. Diyalog: yerel ses veya ayrı ses kaydı
Omni'nin yerel ses desteği olduğu için iki yöntem de değerlendirilebilir. Film boyunca aynı oyuncu sesinin korunması için hangisinin senin çıktılarında daha iyi çalıştığını kısa pilotta dinle. Metinle ses tarifi vermek, aynı sesin her klipte kesin tekrarlanacağı bir kimlik kilidi değildir.

Yöntem    Ne zaman yararlı?    Kontrol edilecek
Omni içinde konuşma    Kısa, tek konuşmacılı bir replik; görüntüyle doğal uyum istendiğinde.    Doğru kişi, doğru kelimeler, telaffuz, ton ve gereksiz konuşma.
Ayrı ses kaydı    Uzun filmde aynı sesi sürdürme, telsiz, iç ses, görüntü dışında konuşma.    Sesin karakterle ve mekânla uyumu; kesmelerde ritim.
Karma yöntem    Ortam/mekanik sesini klipten, ana diyalogu ayrı kayıttan almak.    İki farklı ortamın ve müziğin üst üste binmemesi.
AUD-01 | Omni içinde tek replik

Use the supplied cinematic frame for one continuous shot.
The pilot holds his position at the controls.
One speaker only: the pilot, with a calm adult male voice,
clear neutral English and a light helmet-radio character.
He says exactly: "Hold position. We're almost there."
The other visible character does not speak.
No narration, extra words, subtitles or music.
Preserve the existing faces, outfits and cockpit geometry.
AUD-02 | Konuşmayı sonra eklemek

One continuous shot from the supplied frame.
[Describe the primary action and camera.]
Audio: low cockpit ambience and one restrained control click only.
No speech, narration or music. Dialogue will be added in editing.
Preserve the faces, helmet states, props and light direction.
Bu ses kısıtları bir istektir. Çıktıda istenmeyen konuşma veya müzik varsa video düzgün olsa bile sesi kullanmak zorunda değilsin; kurgu sırasında ilgili sesi değiştir. Her seferinde tüm görüntüyü yeniden üretmek gerekmeyebilir.

10 saniyede 12 kelimelik bir replik rahat okunabilir; yine de aksan, duraklar ve duygunun süresi değişir. Kabaca 2-2,5 kelime/saniye üzerinden ilk planı yap, kesin giriş/çıkışı gerçek kayıtta ayarla. Promptta milisaniyelik konuşma takvimi vermeyi senkron garantisi sayma.

Ses köprüsü
Sonraki planın repliğini kesmeden az önce başlatmak veya önceki ortam sesini yeni görüntünün altında sürdürmek geçişi yumuşatır. Sürekli bir gemi/oda ortamı, ayrı ayrı üretilen klipleri aynı mekâna bağlar. Müziği konuşmanın üstüne değil, sahnenin karar ve sonuçlarına göre yerleştir.

Bir sesle anlattığın bilgiyi görüntüde duyulması için ağız yakın planına mecbur değilsin. Telsiz ve iç ses, kasklı karakterli uzay filmlerinde doğal seçeneklerdir. Başka kişilerin sesi gibi duyulan istemsiz cümleleri son dinlemede ayıkla.

17. Sorunu hangi aşamada çözmelisin?
Belirti    Önce bak    İlk düzeltme
Yüz daha ilk karede farklı    GPT Image karesi ve doğru kimlik girdisi    Kimliği görselde yerel düzenlemeyle geri getir.
Yüz hareket içinde değişiyor    Omni hareket ve kamera karmaşıklığı    Hareketi sadeleştir, daha kısa kullanılabilir bölüm seç veya yeni açı kur.
Ayaklar kayıyor    Zemin, temas ve yürüyüş mesafesi    Kısa adım ve sabit kamera; gerekirse varışa kes.
Kapı/miğfer biçim değiştiriyor    Başlangıç geometrisi ve çoklu eylem    Nesne durumunu sabitle; hareketi ayrı plana böl.
El fazlalaşıyor veya nesne eriyor    Temas noktasının ilk karede görünmesi    Önceden tutulmuş pozdan başla, tek çevirme iste.
İki kişi tek yüze benziyor    Karışan veya yetersiz rol referansları    Kimlikleri ayrı kaynaklarla kur; kalabalık yerine daha sade kadraj.
Işık/gezegen yönü sıçrıyor    Mekân ana planı ve ekran coğrafyası    Yeni kareyi aynı dünya yerleşiminden oluştur.
Sonraki klip eylemi baştan alıyor    Başlangıç/bitiş durum kartı    Gerçekleşmiş olayı yeni ilk kareye işle.
Ek konuşma veya yanlış kelime    Ses seçimi ve konuşmacı sayısı    Tek konuşmacı iste veya ana sesi ayrı kaydet.
Oran yanlış    Gerçek kaynak görselin piksel ölçüsü    Görseli doğru tuvale getir, sonra video üret.
Sahne güzel ama anlaşılmıyor    Çekimin dramatik amacı    Geniş yerleşim, tepki veya sonucu ekle; süslü promptu büyütme.
Süre eksik    Kırpılan kullanılabilir toplam    Gerekli ek planı/uzatmayı üret; ham süreyi final süre sayma.
FIX-01 | Omni'de sınırlı düzeltme istemi

Edit the selected video if this editing feature is available.
Correct only [specific visible issue].
Preserve the existing action, faces, timing, camera movement,
lighting, sound choice and every other object.
Do not restyle the scene or introduce a new shot.
Düzenlemenin iyi olup olmadığını sadece düzeltilen nesneden anlama. Yüzün başka birine dönüşmediğini, hareketin süresinin kaymadığını ve sesin değişmediğini de kontrol et.

Öncelik sırası

Önce hikâyeyi bozan hata: yanlış kişi, yanlış olay, bozuk temas veya yanlış durum. Sonra dikkat çeken görsel kusur. Küçük grain farkı veya arka plan pürüzü, çalışan bir sahneyi sonsuz yeniden üretime sokmamalı.

Bir değişikliği denediğinde neyi değiştirdiğini tek cümleyle kaydet. Tüm promptu her turda yeniden yazmak yerine kontrollü düzeltme yap. Sorun çözülmüyorsa çekim dilini değiştir.

18. Kurgu, en-boy oranı ve yayın dosyası
Önce bütün filmi basit kesmeler ve geçici sesle birleştir. Başlangıç, hedef, engel, karar ve sonuç anlaşılır mı? Bu aşamadan önce her kareyi son renk ve efekt düzeyine taşımak gereksiz tekrar yaratabilir.

Gerçek oranı ölç
Dosya    Gerçek oran    Sonuç
1920 x 1080    16:9    Yatay film örneği.
1080 x 1920    9:16    Dikey film/promosyon örneği.
1536 x 1024    3:2    16:9 değildir; promptta yatay yazması yetmez.
1024 x 1536    2:3    9:16 değildir; istenen tuvale uyarlanmalı.
1536 x 1024 görseli merkezden 1536 x 864'e kırpmak 16:9 verir: üstten ve alttan 80'er piksel gider. 1024 x 1536 görseli 864 x 1536'ya kırpmak 9:16 verir: iki yandan 80'er piksel gider. Önemli el/yüz kesiliyorsa tuvali uygun yönde genişlet veya kadrajı yeniden kur. Görseli esnetip oranı zorlamak beden ve nesneleri bozar.

Renk ve ses bütünlüğü
Sahne grubu içinde aynı beyaz dengesini, siyah seviyesini ve atmosfer hissini koru. Her klibe ayrı ağır efekt uygulamak yerine ortak bir son görünüm kullan. Tekrarlanan ortam sesini sürekli bir katman olarak kur; konuşmaları telefon hoparlöründe de dinle.

YouTube'un resmî önerileri MP4/H.264 gibi yaygın seçenekleri ve kaynakla aynı kare hızında yüklemeyi içerir. Örnek ses ayarı 48 kHz'dir. Kendi dosyalarının gerçek fps değerini öğren; Omni'nin her dosyasını varsayılan olarak 24 fps sayma. S5

TECH-01 | Dosyanın gerçek özelliklerini gör / isteğe bağlı

ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,avg_frame_rate,r_frame_rate:format=duration \
  -of json "C01_VIDEO_v01.mp4"
Bu komut dosyayı değiştirmez; oran, kare hızı ve süre bilgisini gösterir. FFprobe belgeleri seçilecek alanları ve çıktı biçimini açıklar. İstersen aynı değerleri kurgu programının dosya özelliklerinden de okuyabilirsin. S7

Yatay film ve dikey tanıtım
16:9 filmin tamamını merkezden dikey kırpmak her sahnede işe yaramaz. İki karakter karşılıklıysa birinin yüzü veya önemli mekanizma dışarıda kalabilir. Tanıtım için ayrı kısa kadraj/kapak düzeni hazırlamak daha kontrollüdür.

1280 x 720 tuvalden tam 9:16 merkez kırpma matematiksel olarak 405 x 720'lik sütun alır. Kapak boyutu 1280 x 720 kalacak ama ana tasarım ortada dikey görünsün istiyorsan önemli yüzleri ve film adını bu dar orta kompozisyonda tasarla; yanlarda düşük ayrıntılı koyu uzatma kullan. Bu, uygulamanın bütün arayüz kaplamaları için evrensel safe area ölçüsü değildir. Yükleme ön izlemesini ayrıca kontrol et.

Film adı ve kapak metnini post prodüksiyonda eklemek yazım, hizalama ve farklı platform düzenlerini yönetmeyi kolaylaştırır. Kaynak görsellerde rastgele yazı oluşmasını isteme; gereken rozet veya simge geometrisini koru.

YouTube, gerçekçi görünümlü ve anlamlı biçimde AI ile üretilen/değiştirilen içerikler için açıklama ölçütleri yayımlar. Yüklemedeki AI use alanını gerçek üretimine göre değerlendir; yalnızca açıklamaya bir AI cümlesi eklemek bu alanın yerine geçmez. S6

19. Dosyalar, sürümler ve üretim maliyeti
Klasör / örnek dosya    İşlev
refs/CHAR_A_FRONT_v01.png    Onaylı kimlik ve görünüm.
refs/ROOM_MASTER_v01.png    Mekânın ana yerleşimi.
refs/HATCH_CLOSED_v01.png    Nesnenin belirli durumu.
frames/C01_START_v03.png    Seçilen çekimin başlangıç kompozisyonu.
clips/C01_VIDEO_v02.mp4    Bir video denemesi; eskisini ezmez.
selects/C01_KEEP.mp4    Kurguda kullanılacak seçili kaynak.
audio/CHAR_A_LINE_01.wav    Tek replik veya karakter ses dosyası.
edit/FILM_ROUGHCUT_v01.mp4    İlk izlenebilir film sürümü.
export/FILM_FINAL_16x9.mp4    Yayın dosyası.
log/SHOT_LOG.csv    Kaynak, deneme ve karar kaydı.
LOG-01 | Basit çekim kaydı / CSV başlığı

shot_id,image_version,video_version,actual_model,aspect_ratio,raw_seconds,usable_in,usable_out,attempt_count,cost_units,status,note
C01,START_v03,VIDEO_v02,[model label],16:9,10,0.5,8.5,2,[actual units],KEEP,[one useful note]
Şablondaki alanları kendi gerçek ölçümlerinle doldur. Günlük kota, kredi bedeli ve kullanım hakkı arayüzdeki plana göre değişebilir; bu kılavuz sabit fiyat veya günlük üretim sayısı vermiyor. Bir denemenin arayüzde gösterilen bedelini ve gerçek kullanılabilir süresini kaydet.

Maliyet hesabını yalnızca başarıyla seçtiğin kliplere göre yapma. Bütün denemeleri say. Farklı modların birim bedeli farklıysa her satırın gerçek bedelini topla; tek bir evrensel sayı ile çarpma.

FORMUL-02 | Maliyet ve verim notu

total_cost = sum(actual_cost_of_every_attempt)
selected_usable_seconds = sum(usable_out - usable_in)
cost_per_selected_second = total_cost / selected_usable_seconds

Track image attempts and video attempts separately.
Küçük sahne gruplarıyla bitir
Önce kısa pilot, sonra örneğin altı planlık bir bölüm üretip kurgula. Kaynakları indir, seçimi yap ve çalışan bölümün üstüne ilerle. 96 kliplik filmin bütününü üretip ilk kez sonda izlemek, aynı hatayı çok sayıda dosyada keşfetmene yol açabilir.

Sadece dosyaya vFINAL yazmak bitmiş film oluşturmaz. Tek parça dışa aktarılmış, sesi anlaşılır ve baştan sona izlenmiş sürüm gerçek tamamlanma ölçütüdür.

20. 2 dakika tek kamera ve 16 dakika uzun film
2 dakika / tek kamera
10 saniyelik final parçalarıyla 12 bölüm planlayabilirsin. Kameranın konumunu, lens hissini ve kadrajı tek ana görselle sabitle. Özne, dış pencere manzarası, ışık veya konuşmanın anlamı değişebilir; kamera her klipte yeniden keşfedilmez.

SPEC-01 | Sabit kamera devam şablonu

Continue the established fixed-camera scene.
The camera position, lens framing and horizon stay unchanged.
Current story state: [state].
Primary change in this segment: [action or new external event].
Preserve all existing identities, props and architecture.
No camera pan, zoom, orbit or cut.
Audio: [chosen dialogue and ambience plan].
Sabit kamerada seyircinin dikkatini taşıyan bilgi akışıdır. Tek kadrajı korumak için hikâyeyi on iki kez aynı bakışa indirme. Aynı açıdaki devamlar bozuluyorsa temiz ana görsele ve doğru durum referansına dön.

16 dakika / iki veya üç karakter
96 adet 10 saniyelik final parçası toplam 16 dakikadır. Uzunluğu yalnızca plan sayısını artırarak kurma. Hikâyeyi hedef, ilk engel, yeni çözüm, önemli keşif, plan değişikliği, kriz, karar ve sonuç gibi bölümlere ayır.

Her sahne grubu için ayrı mekân durumu ve ses devamlılığı tut. Karakterin kıyafeti veya aracın hasarı değişiyorsa hangi bölümde değiştiğini kaydet. Dört dakikalık üretimde çalışan kimlik ve sahne dilini önce doğrula; sonra daha uzun yapıya ölçekle.

Diyaloglu bir odadan EVA aksiyonuna geçince aynı hareket ve ses promptunu taşımak doğru değildir. Hikâye kimliği sabit kalır; çekimin fiziksel koşulları için ayrı durum kartı kullan.

21. Yeni film için kullanacağın ana çalışma promptu
Aşağıdaki metni yeni bir film planlarken kullanabilirsin. Bu bir planlama promptudur; karakter dosyalarını kendiliğinden yüklemez ve video üretildiği anlamına gelmez. Gerçek dosyaları belirtilen adımlarda sen eklersin.

MASTER-01 | Kopyalanabilir film üretim yöneticisi promptu

Act as my practical AI-film production director.
My workflow is GPT Image for still images and Gemini Omni 1.1 Flash
for image-to-video. Production notes must be in Turkish.
All generation prompts and movie dialogue must be in English.

DEFAULT PROJECT
Horizontal 16:9, four minutes, 24 final segments of ten seconds.
Original adult characters; no children.
For space stories: coherent white suit designs, large readable planetary
scale, and a motivated docking scene when it belongs in the plot.
Use my supplied fixed identity blocks verbatim when I designate them locked.

FIRST: DESIGN THE STORY
Give me one clear premise, the opening hook, the character goal,
the changing obstacle, a meaningful decision, and the completed ending.
Each shot must add information, action or consequence.
Do not rely on tiny eye movements, perfect silence, invisible timing,
or frame-exact mechanical coincidence to explain the story.

SECOND: BUILD THE REFERENCES
List only the necessary character, location, vehicle and prop-state assets.
Separate closed/open, folded/deployed, inactive/active versions.
State which files must actually be attached for each image request.

THIRD: WRITE SHOT CARDS
For every shot provide its purpose, start state, one primary action,
end state, visible characters, camera and light direction.
Then provide a GPT Image still prompt and a separate Omni motion prompt.
The still describes the state BEFORE the motion, not the finished result.
Use a master geography shot and meaningful reaction/result coverage.

FOURTH: SPECIFY VIDEO INPUTS
Default to the approved single shot image as the visual basis.
If extra references are useful, assign each an explicit role.
Do not treat multiple images as guaranteed first/last-frame controls.
Do not invent model parameters, exact frame locks or quota figures.

FIFTH: PLAN SOUND AND EDITING
Choose native speech or post-production speech for each shot.
Keep dialogue short enough to record naturally; use one consistent cast.
Track actual usable duration, not just raw generated seconds.
Keep the required total film duration after trims and transitions.

WORK IN SMALL GROUPS
Begin with a three-shot pilot, then build the remaining scene groups.
When an action is too complex, simplify, split it or cut to its result.
After two controlled failed corrections, propose a different shot design.
Use reasonable stated assumptions for routine decisions.
Do not add new forms, repeated approval questions or needless variants.
Do not claim an image or video was generated unless it actually was.

OUTPUT
1. Story and ending.
2. Necessary reference list and prompts.
3. Shot table with start/action/end states.
4. First three complete still + motion prompts as the pilot.
5. Remaining shot prompts by scene group.
6. Dialogue/audio plan, continuity notes and duration arithmetic.
7. Publication title/cover ideas consistent with the film's actual opening.

MY NEW FILM IDEA:
[Write the idea here, or ask for one original concept.]
22. Bir sahneyi tamamlanmış sayma ölçütü
Seçim ekranında normal hızda izle. Hemen ardından bir sonraki planla birlikte izle. Tek başına güzel duran bir klip, yanlış yöne bakan karakter veya sıfırlanmış kapak yüzünden ardışık sahnede çalışmayabilir.

Kimlik ve olay: doğru kişi, doğru ana hareket veya bilgi var mı?
Devamlılık: başlangıç/bitiş, nesne durumu, bakış ve ışık bir sonraki planla uyumlu mu?
İzlenebilirlik: konuşma duyuluyor ve kullanılan süre olayın ritmine hizmet ediyor mu?
Bu üç madde sağlanıyorsa sonucu seç ve ilerle. Sorun yalnızca küçük bir arka plan ayrıntısıysa yeniden üretim yerine kurgu içindeki etkisini değerlendir. Kullanıcıya filmi anlatan ana neden-sonuç zinciri görünür kalmalı.

Teslimden önce    Bakılacak gerçek sonuç
Tek parça izleme    Açılış, amaç, değişen plan ve final anlaşılır.
Süre    Dosyanın gerçek toplamı hedefle eşleşir.
Ses    Kişiler ayırt edilir; kesmelerde anlamsız müzik/konuşma sıçraması yoktur.
Görüntü    Kimlik ve önemli nesne biçimleri dikkat dağıtacak şekilde değişmez.
Yayın kopyası    Doğru oran, okunaklı başlık, hedef platformda kontrol edilmiş ön izleme.
Bitiş kararı

Kılavuzun amacı daha çok senaryo ve kontrol listesi üretmek değil, izlenebilir tek bir filmi tamamlamaktır. Bir sorunu çözdükten sonra aynı bölümü yeni bir neden olmadan baştan açma.

23. Sabit EVA kimlik blokların
Aşağıdaki dört metin senin daha önce sabit tutulmasını istediğin EVA kimlik tarifleridir. Bu karakterleri kullanırken ilgili bloğu aynen kopyala. Bunlar bütün G02-G06 sahnelerinin tam promptu değildir; burada mevcut olan kimlik bloklarıdır.

LOCK-KAYA-V | KAYA_KIMLIK / yüz görünür

a man in his late fifties with a lined, weathered face visible through the large clear visor of his round white helmet, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a red band around the top of each sleeve at the shoulder, white gloves with red cuffs, and a boxy white thruster pack with smooth, unmarked faces on his back, set in an open tubular grab frame; a red tether line runs from a clip at the centre of his waist to a steel safety hook
LOCK-KAYA-H | KAYA_KIMLIK / yüz görünmez

a man in his late fifties in a round white helmet with a large clear visor, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a red band around the top of each sleeve at the shoulder, white gloves with red cuffs, and a boxy white thruster pack with smooth, unmarked faces on his back, set in an open tubular grab frame; a red tether line runs from a clip at the centre of his waist to a steel safety hook
LOCK-IPEK-V | IPEK_KIMLIK / yüz görünür

a woman in her late twenties with a smooth, narrow face visible through the large clear visor of her round white helmet, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a blue band around the top of each sleeve at the shoulder, white gloves with blue cuffs, and a slim, flat white life‑support pack on her back; a blue tether line runs from a clip at the centre of her waist to a steel safety hook
LOCK-IPEK-H | IPEK_KIMLIK / yüz görünmez

a woman in her late twenties in a round white helmet with a large clear visor, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a blue band around the top of each sleeve at the shoulder, white gloves with blue cuffs, and a slim, flat white life‑support pack on her back; a blue tether line runs from a clip at the centre of her waist to a steel safety hook
Bu metinler dış uzay yürüyüşüne aittir. İç mekân için başka bir kıyafet/ekipman durumu gerekiyorsa ayrıca adlandırılmış bir referans sürümü oluştur. Sabit bloğu fark ettirmeden değiştirme; rozet eklemek istiyorsan yeni bir tasarım durumu olarak kaydet. Işık veya mekân cümlesi aynı kalacak bir seri varsa onu da ayrı sabit blok olarak tut.

24. Kısa sözlük ve kaynaklar
Terim    Bu kılavuzdaki anlamı
Referans    Kimlik, tasarım, mekân veya durum için tekrar kullanılan kaynak görsel.
Başlangıç kompozisyonu    Hareketten önce planlanan görüntü; ürünün kesin kare kilidi vaadi değildir.
Durum    Açık/kapalı, bağlı/ayrık gibi hikâyede gerçekleşmiş fiziksel koşul.
Master plan    Sahnenin coğrafyasını ve kişilerin ilişkisini kuran geniş çekim.
Tepki planı    Bilgi/olay alan kişinin buna verdiği anlamlı karşılığı gösteren çekim.
Insert    Bir nesne veya mekanik ayrıntıya odaklanan çekim.
Kullanılabilir bölüm    Ham videonun kurguda gerçekten seçilen giriş-çıkış aralığı.
Rough cut    Son renk ve efektlerden önce baştan sona izlenebilir ilk kurgu.
Ürün özellikleri için resmî sayfalar kullanıldı. Şablonlar, çekim örnekleri ve çalışma tercihleri bu kılavuz için özgün olarak hazırlandı. Açıklanan ürün özelliği ile önerilen üretim yöntemi aynı tür kanıt değildir. Kaynaklar 15 Ekim 2026 tarihinde kontrol edildi.

S1 - Google - Gemini Omni / video generation
https://gemini.google/overview/video-generation/
Model adı; 10 saniye; yerel ses; beşe kadar görsel; tanıtılan düzenleme/uzatma işlevleri ve erişim farkları.

S2 - Google Help - Generate videos with Gemini Apps
https://support.google.com/gemini/answer/16126339?hl=en
Görsel yükleme akışı, referans oranı ve uygulama içindeki düzenleme/indirme yaklaşımı.

S3 - OpenAI Docs - Image prompting
https://developers.openai.com/api/docs/guides/image-prompting
Referans rollerini açıklama, kimlik ve düzenleme sırasında korunacak öğeleri belirtme. Belirli bir yeni modele geçiş önerisi olarak kullanılmadı.

S4 - OpenAI Docs - Image generation
https://developers.openai.com/api/docs/guides/image-generation
Görsel üretim ve çok adımlı düzenleme API bağlamı. Sohbet arayüzünün parametre listesi olarak ele alınmadı.

S5 - YouTube Help - Recommended upload encoding settings
https://support.google.com/youtube/answer/1722171?hl=en
Yayın dosyası ve kare hızı için temel resmî öneriler.

S6 - YouTube Help - Disclosing use of GenAI content
https://support.google.com/youtube/answer/14328491?hl=en
Gerçekçi sentetik içerik açıklaması ve AI use alanı.

S7 - FFmpeg - ffprobe documentation
https://ffmpeg.org/ffprobe.html
Dosyayı değiştirmeden teknik özellikleri okuyan isteğe bağlı komut.
