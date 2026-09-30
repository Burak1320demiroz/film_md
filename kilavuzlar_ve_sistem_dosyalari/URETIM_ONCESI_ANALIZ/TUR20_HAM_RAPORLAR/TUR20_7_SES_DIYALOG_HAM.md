# 🧾 TUR 20 · RAPOR 7 — HAM (16.09.2026)

> **Koşulan prompt:** `23_OMNI_1_1_FLASH_I2V_ARASTIRMA_PROMPTLARI.md` §7 SES ve DİYALOG — yerel ses, replik sözdizimi, dudak senkronu ve altyazı riski (altı cümle, aşağıda birebir).
> **Rapor başlangıcı (araçtan, ilk 200 karakter — başlık gövdeye yapışık geldi):** GOOGLE GEMINI OMNI 1.1 FLASH MODELİNDE YEREL SES ÜRETİMİ VE YAZILIMSAL SÖZDİZİMİ ANALİZİ: UZAY BİLİMKURGU YAPIMLARI İÇİN MÜHENDİSLİK REHBERİ
> **Yapıştırma sırası:** 6/9 (sahip dokuz raporu tek mesajda, tırnaklı ve virgülle ayrılmış dizi olarak yapıştırdı; dosya PROMPT numarasıyla adlandırıldı).
> **Durum:** BİREBİR — düzeltilmedi, kısaltılmadı; metin oturum kaydından programla kesildi (elle kopyalanmadı), yalnız dizi ayırıcıları (`"` · `", "`) atıldı. Bölüm başlıkları ve paragraf kırılmaları VAR; `[cite: …]` artıkları. Kaynak listesi VAR (sonda, alan adı düzeyinde).
> **Doğrulama ve süzme:** `00_KUNYE.md` §🔎 (16.09.2026 canlı kaynak kontrolü) · `../04_ARASTIRMA_BULGULARI.md` §TUR 20.

## 📋 KOŞULAN PROMPT — birebir

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modelinin (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde yerel ses üretimini araştır: ses efekti, ortam sesi, müzik ve konuşmanın promptla nasıl istendiği ve ne kadar uyulduğu, ses ile görüntü eşzamanlılığı, sesin kapatılabilmesi ya da sessiz klip istenebilmesi — resmî belgeler ve örnek promptlar, bağımsız testler ve sistematik kullanıcı raporları; sürüm, tarih ve kaynakla.
Konuşma sözdizimini birebir sök: repliğin tırnak içinde mi yazılacağı, "says:", "speaks the line", "says in a low voice" gibi kalıplar arasındaki fark, iki nokta üst üstenin ve tırnağın ekrana gömülü altyazı ya da yazı üretme riski ve bunu önleyen cümleler ("no subtitles", "heard only, never shown as text"), on saniyeye sığan kelime sayısı, konuşma hızı ve duraklama tarifi, duygu ve vurgu kelimelerinin etkisi, konuşmanın klibin hangi saniyesinde başlayacağının yönetilebilmesi — iki yönlü, işe yarayan ve yazı üreten örneklerle.
Dudak senkronunu ve sesin sahibini sor: senkronun hangi çekim ölçeğinde (yakın, orta yakın, orta, geniş) ve hangi yüz açısında çöktüğü, kapalı kask, maske ya da görünmeyen ağızla konuşma istenirse ne üretildiği, sesin kadrajdaki doğru kişiye bağlanması, telsiz, kayıt cihazı ya da kadraj dışı ses gibi kaynağı görünmeyen sesin tarifi, aynı karakterin sesinin ardışık kliplerde aynı kalıp kalmadığı ve sesi sabitlemenin belgelenmiş yolu.
Ortam ve efekt katmanını sor: "Audio:", "SFX:", "Ambient:" gibi etiketlerin etkisi, kaç ses katmanının güvenle üretildiği, eylem ile sesi bağlayan cümle biçimleri ("as the latch clicks"), istenmeden eklenen müziği kapatmanın yolu, vakum ya da ince atmosfer gibi sesi taşımayan ortamların tarifi (boğuk dış ses, yalnız giysi içi nefes ve fan) ve modelin buna uyup uymadığı; ayrıca çığlık, ağlama, argo ve sert sesin politika reddi ürettiği ve üretmediği vakalar, birebir mesaj metniyle.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli uzay bilimkurgu planlarıdır; karakter çoğu klipte konuşmaz, replik yalnız basınçlı iç mekânda, kasksız ve orta yakın planda klip içinde üretilir, kapalı vizörde replik klip içinde üretilmez ve sesi sonradan eklenir, tek konuşmacı ve replik başına beş saniyeden kısa, kadrajda hiçbir yazı ve altyazı olamaz, dış ses anlatıcı yoktur — bu yüzden altyazıya, çok konuşmacılı diyaloğa, dış sese ya da sonradan dudak senkronu aracına dayanan çözümleri işaretleyip ele.
Çıktıyı üç tablo ve iki liste olarak ver: (a) SÖZDİZİMİ tablosu — İngilizce birebir kalıp, dudak senkronu sonucu, altyazı ya da ekran yazısı riski, kelime sınırı, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) SENKRON tablosu — çekim ölçeği ve yüz durumu (açık, profil, kasklı, kapalı vizör), senkron sonucu, arıza biçimi, kaynak ve etiket; (c) SES KATMANI tablosu — katman (konuşma, efekt, ortam, müzik, sessizlik), İngilizce kalıp, uyum, istenmeyen yan etki, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin (özellikle Veo 3.1) bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

## 📄 RAPOR — birebir

GOOGLE GEMINI OMNI 1.1 FLASH MODELİNDE YEREL SES ÜRETİMİ VE YAZILIMSAL SÖZDİZİMİ ANALİZİ: UZAY BİLİMKURGU YAPIMLARI İÇİN MÜHENDİSLİK REHBERİ
1. Model Mimarisi, Sistem Erişimi ve Yerel Ses Katmanının Çalışma İlkeleri
Google DeepMind tarafından geliştirilen ve gemini-omni-1.1-flash model kimliğiyle sunulan multimodal video üretim mimarisi, yapay zeka destekli video sentezinde geleneksel yaklaşımlardan temel bir kopuşu temsil etmektedir. Geleneksel video üretim sistemlerinde (örneğin Google Veo 3.1) görsel kareler sentezlendikten sonra ses katmanı ikincil bir işleme adımı olarak eklenirken veya ayrı bir harici modelle birleştirilirken, Gemini Omni 1.1 Flash mimarisi Interactions API üzerinde metin, görsel, video ve ses jetonlarını (tokens) eşzamanlı olarak işleyen yerel (native) bir multimodal difüzyon mimarisi kullanmaktadır. Bu teknik yapı, görseldeki piksel hareketleri ile frekans düzeyindeki ses dalga formlarının tek bir ortak gizil alanda (latent space) hizalanmasını sağlamaktadır.   

Model, 30 Haziran 2026 tarihindeki açık önizleme sürecinin ardından 27 Ağustos 2026 tarihinde genel kullanıma sunulmuş ve Google Flow, Gemini API (Google AI Studio) ile YouTube ekosisteminde varsayılan model haline getirilmiştir. Temel üretim adımında 3 ila 10 saniyelik tekil klipler üretebilen sistem, varsayılan 720p çözünürlükten 360p taslak seviyesine ya da 1080p ve 4K yükseltme (upscaling) katmanlarına kadar geniş bir çözünürlük yelpazesini desteklemektedir. Çoklu etkileşim oturumlarında (previous_interaction_id) önceki 10 saniyelik görsel ve işitsel bağlamı koruyarak sahneleri 10'ar saniyelik adımlarla 40 saniyeye kadar kesintisiz uzatabilme yeteneğine sahiptir.   

Google Veo 3.1 ile Gemini Omni 1.1 Flash arasındaki mimari ayrımın doğru yapılması kritik önem taşımaktadır. Veo 3.1 modelleri yüksek görsel estetik ve karmaşık kamera hareketlerine odaklanan bağımsız bir difüzyon motoruyken, Gemini Omni 1.1 Flash konuşarak düzenleme (conversational editing) ve görsel ile işitsel öğelerin milisaniye düzeyindeki senkronizasyon yetkinliği ile ayrışmaktadır.   

Yerel ses sentezleme mekanizması, istem içerisinde tanımlanan konuşma (speech), ses efektleri (SFX) ve ortam seslerini (ambient) görsel hareketlerle zaman uyumlu biçimde üretmektedir. Kullanıcı istemde herhangi bir ses tanımı yapmadığı takdirde model görsel içeriğe uygun ortam seslerini otomatik olarak türetmekte; sessiz bir klip elde etmek için ise açıkça negatif veya kısıtlayıcı komutların verilmesi gerekmektedir.   

2. Konuşma Sözdizimi, Metin İletim Riski ve Ekran Yazısı Engelleme
Gemini Omni 1.1 Flash modelinin metin ayrıştırma motoru (text parser), istem içerisindeki noktalama işaretlerini iki farklı üretim modunu tetiklemek üzere kodlamıştır. Model mimarisindeki en kritik ayrım, iki nokta üst üste (:) ile tırnak işareti ("") kullanımında ortaya çıkmaktadır:   

İki Nokta Üst Üste (:) Kullanımı: İstem içerisinde bir eylemin veya karakterin ardından kullanılan iki nokta üst üste imi (A male astronaut says: Reactor status clear), modelin konuşma sentezleme modülünü (speech synthesizer) aktif hale getirir. Bu kullanım, görseldeki karakterin ağız hareketleriyle tam senkronize biçimde ses dalga formu üretilmesini sağlar.   

Tırnak İşareti ("") Kullanımı: Karakter repliğinin tırnak işaretleri arasına alınması (A male astronaut says: "Reactor status clear"), modelin görsel metin oluşturma motorunu (on-screen text renderer) tetikler. Model, tırnak içerisindeki ifadeyi işitsel bir replik olarak sentezlemek yerine, görsel karelerin alt kısmına gömülü altyazı (burned-in subtitles) veya ekran yazısı olarak çizer.   

Ekrana istenmeyen altyazı veya grafik metin gömülmesini kesin olarak engellemek adına istem sözdiziminden tırnak işaretleri tamamen çıkarılmalı ve komut dizisine doğrudan engelleyici kalıplar eklenmelidir. Kullanılması gereken standart negatif ve pozitif koruma ifadeleri şunlardır: no subtitles, no on-screen text, speech heard only as audio, never shown as text.   

Modelin 10 saniyelik bir klip süresi içerisindeki konuşma sentezleme kapasitesi, doğal insan konuşma temposu olan saniyede ortalama 2,5 ila 3 kelime metriğine dayanmaktadır. 10 saniyelik tam bir klipte en fazla 20-25 kelimelik diyalog sentezlenebilirken, repliğin 5 saniyenin altına sığması gereken durumlarda replik uzunluğu kesinlikle 8 ile 12 kelime arasında tutulmalıdır. İstem uzunluğunun genel optimum aralığı (sweet spot) 30 ila 80 kelimedir; 100 kelimenin üzerindeki istemlerde modelin tutarlılığı düşmektedir.   

Konuşmanın temposu ve vurgusu istem içerisindeki nitelik zarflarıyla yönetilir. says in a low, breathless voice: veya speaks the line: ifadeleri ses sentezleyicinin tonalitesini değiştirir. Repliğin klibin hangi saniyesinde başlayacağı Dialogue (starting at 00:02): şeklinde zamansal etiketlerle veya eylem koşuluna bağlanarak (after checking the monitor, the astronaut says:) kontrol edilmektedir.   

Uygulanabilir İstem Örnekleri
İşlevsel, Altyazısız ve Temiz Ses Üreten İstem:

A photorealistic medium close-up shot of a male astronaut inside a pressurized spaceship cockpit. In a single continuous shot with a fixed camera, he looks directly ahead. The astronaut says in a calm low voice: Life support parameters are stabilizing. Ambient atmospheric hum inside the cabin. No subtitles, no on-screen text, speech heard only as audio, never shown as text.

[cite: 4, 9, 15, 16]

Ekrana Altyazı Gömen Hatalı İstem (Altyazı Tuzağı):

A photorealistic medium close-up shot of a male astronaut inside a pressurized spaceship cockpit. The astronaut says: "Life support parameters are stabilizing."

[cite: 8]

3. Dudak Senkronizasyonu, Çekim Ölçeği ve Karakter Sesi Sabitleme Mekanizmaları
Gemini Omni 1.1 Flash modelinin görsel dudak senkronizasyonu (lip-sync) başarısı, kadrajdaki yüz piksellerinin yoğunluğu ve geometri çözünürlüğü ile doğrudan ilişkilidir. Çekim ölçeği ve yüz açısına göre senkronizasyon performansı şu şekilde şekillenmektedir:   

Yakın Çekim (Close-Up - CU) ve Orta Yakın Çekim (Medium Close-Up - MCU): Dudak senkronizasyonunun en yüksek doğrulukta çalıştığı ölçeklerdir. Model, fonem-görsel eşleşmesini ağız hareketlerine yüksek hassasiyetle aktarır. Kasksız diyalog üretimi için ideal çerçeve MCU'dur.   

Orta Çekim (Medium Shot - MS): Senkronizasyon kabul edilebilir düzeydedir; ancak hızlı konuşmalarda ağız piksellerindeki detay kaybı nedeniyle mikro kaymalar gözlemlenir.   

Geniş Çekim (Wide Shot - WS): Senkronizasyon tamamen çöker. Yüz pikselleri alt çözünürlük seviyesine düştüğü için model ağız hareketlerini sentezleyemez; ses kadrajdan bağımsız bir dış ses gibi duyulur.   

Yüz Açıları (Ön, Profil, Yan): Cepheden (frontal) çekimlerde senkron mükemmelken, 90 derece profil çekimlerinde ağız kenarı piksel bükülmeleri (warping) ve zamansal takılmalar yaşanır.   

Ağız bölgesinin kapalı olduğu durumlarda (örneğin astronot kaskı kapalı vizörü veya maske) model görsel olarak ağız hareketi üretemez. Bu durumda istemde konuşma istendiğinde model vizör üzerinde saydam yüz morfları veya piksel bozulmaları oluşturmaya çalışır ya da vizör sabit kalırken ses üretir, bu da inandırıcılığı yok eder. Bu nedenle kapalı vizörlü uzay giysisi planlarında kask içinden canlı diyalog üretilmemeli, bu sahneler istem düzeyinde diyalogsuz (No dialogue) üretilmeli ve yalnızca giysi içi ortam sesleri eklenmelidir.   

Kadraj dışından gelen sesler (örneğin telsiz konuşması veya kayıt cihazı) için konuşma sözdizimi değil, ses efekti sözdizimi kullanılmalıdır: SFX: Distorted voice over crackling radio comms speaker: Mission Control to Eagle, report status. Bu tanımlama, modelin kadrajdaki karakterin ağzını oynatmasını engeller ve sesi akustik olarak filtrelenmiş bir dış kaynak gibi sahneye yerleştirir.   

Gemini Omni 1.1 Flash, kullanıcı tarafından yüklenen harici ses dosyaları üzerinden ses klonlama (voice cloning) özelliğini desteklememektedir. Ses tonunun ardışık kliplerde sabit kalmasının belgelenmiş tek yolu, etkileşimli oturum mimarisini (previous_interaction_id) ve sahne uzatma (scene extension) parametrelerini kullanmaktır. Model, zincirleme yapılan üretim turlarında önceki klipte üretilen ses jeneratör durumunu (audio generator state) belleğinde tutarak aynı karakterin ses rengini sonraki klibe aktarmaktadır. Bağımsız başlatılan yeni promptlarda aynı karakter sesini sabitlemek mümkün değildir.   

4. Ses Katmanı Yönetimi, Akustik Simülasyon ve Güvenlik Filtreleri
İstem metninde yer alan Dialogue:, SFX:, Ambient:, Music: etiketleri, modelin işitsel difüzyon kanalını ayrıştırarak katman bazlı sentez yapmasını sağlar. Model, en fazla 3 işitsel katmanı (örneğin Konuşma + Efekt + Ortam Sesi) birbirini bastırmadan ve frekans karmaşası yaratmadan eşzamanlı olarak üretebilmektedir. 4. bir katman (özellikle müzik) eklendiğinde konuşma anlaşılırlığı düşmektedir. Visual eylem ile sesi bağlamak için zaman bağlaçları kullanılmalıdır: as the airlock latch clicks, at the exact moment the console button flashes.   

Müzik içermeyen diyalog ve efekt odaklı sinematik planlarda modelin varsayılan olarak arka plana dramatik müzik ekleme eğilimi bulunmaktadır. Müziği tamamen bastırmak için şu ifadeler isteme eklenmelidir: No background music, no musical score, muted background, diegetic foley sounds only.   

Uzay ortamlarında (vakum veya basınçsız ince atmosfer) ses iletimi gerçekleşmediğinden, modelin gerçekçi fizik simülasyonu yapması için özel akustik tanımlamalar yazılmalıdır: Ambient: Muffled exterior acoustics, absolute vacuum outside, internal helmet breathing and suit ventilation fan sound only. No external ambient noise. Model bu tür detaylı akustik talimatlara yüksek oranla uymaktadır.   

Modelin ses sentezleme motoru, Google'ın Yüksek Riskli İçerik ve Zararlı Materyal politikaları doğrustusunda filtre sistemine tabidir:   

Reddedilen Vakalar (Policy Refusal): Çığlık, panik dolu şiddetli ağlama, aşırı argo, küfür veya kendine zarar verme sesleri istendiğinde üretim durdurulur. Model tarafından döndürülen birebir hata mesajı şudur:   

Generation blocked: The prompt contains audio or speech instructions that violate Google's Generative AI Safety Policy regarding Graphic Violence, Harmful Content, or Harassment.

[cite: 4, 8, 16]

Reddedilmeyen (Onaylanan) Vakalar: Dramatik gerilim içeren uzay bilimkurgu replikleri, fısıltılı korku ifadeleri veya mekanik arıza uyarıları politikayı ihlal etmez ve sorunsuz üretilir. Onaylanan örnek istem: The astronaut says in a tense whispered tone: Pressure is dropping, we have five seconds.   

Yüklenen Videolarda Konuşma Değiştirme Yasağı: Model kartı belgesinde açıkça belirtildiği üzere, kullanıcı tarafından yüklenen insan içerikli videolara sonradan diyalog ekleme veya mevcut konuşmayı değiştirme yeteneği kısıtlanmıştır.   

5. Uzay Bilimkurgu Prodüksiyon Kısıtları ve Geçersiz Yöntemlerin Elenmesi
Ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden üretilen 10 saniyelik, kesmesiz, sabit kameralı, fotogerçekçi, uzay bilimkurgu planları çerçevesinde teknik çözümler değerlendirilmiş ve elenen yöntemler gerekçelendirilmiştir:

Ekrana Gömülü Altyazı / Yazı Çözümleri: Tırnak işareti kullanımıyla ekrana yazdırılan altyazılar sinematik fotogerçekçiliği bozduğu için elenmiştir.   

Çok Konuşmacılı Diyaloglar: Tek bir 10 saniyelik klipte birden fazla karakterin konuşması, seslerin birbirine karışmasına ve dudak senkronizasyonunun kaymasına yol açtığı için elenmiştir.

Dış Ses (Voiceover) Anlatıcı: Sahne içi gerçekçiliği (diegetic realism) korumak adına anlatıcı dış sesler reddedilmiş, yalnızca kadraj içi karakter konuşması veya filtrelenmiş telsiz efekti kabul edilmiştir.   

Harici Dudak Senkronizasyonu Araçları (Post-hoc Lip Sync): Üretimin Gemini Omni 1.1 Flash'ın yerleşik yetenekleriyle tek pasajda (single pass) tamamlanması istendiğinden, yapım sonrası harici araçlar kapsama dahil edilmemiştir.

Önerilen Prodüksiyon İş Akışı
Senaryo A: Basınçlı İç Mekan (Kask Yok / Vizör Açık, MCU Çekim)
Tek karakter, maksimum 8-10 kelimelik replik (< 5 saniye), iki nokta üst üste sözdizimi, altyazı engelleyici kalıplar.
Uygulanabilir İstem Template:

Photorealistic medium close-up shot of a male astronaut inside a pressurized space station interior. Single continuous shot, default fixed camera. The astronaut says in a quiet serious tone: Reactor core temperature has reached critical mass. SFX: Low humming console pass, soft rhythmic beep. Ambient: Pressurized cabin air ventilation. No background music. No subtitles, no on-screen text, speech heard only as audio, never shown as text.

[cite: 4, 9, 15, 16]

Senaryo B: Basınçsız Dış Mekan / Kapalı Vizörlü Kask
Klip içinde diyalog sentezlenmez (No dialogue). Yalnızca giysi içi akustik foley üretilir. Konuşma gerekiyorsa kurguda harici ses olarak eklenir.
Uygulanabilir İstem Template:

Photorealistic medium close-up shot of an astronaut in a space suit with a fully sealed dark visor, floating outside the space station. Single continuous shot, fixed camera. No dialogue. SFX: Heavy mechanical breathing inside helmet, internal suit air circulation fan. Ambient: Muffled vacuum silence. No background music. No subtitles, no on-screen text.

[cite: 4, 9, 15, 16]

6. Yapılandırılmış Karşılaştırma ve Analiz Tabloları
(a) SÖZDİZİMİ TABLOSU (Dialogue Syntax & Text Rendering Risk)
İngilizce Birebir Kalıp    Dudak Senkronu Sonucu    Altyazı / Ekran Yazısı Riski    Kelime Sınırlaması    Sürüm    Kaynak    Etiket
A male astronaut says: Reactor status clear.    
Tam senkronize sesli konuşma üretir.

YOK. Ekran yazısı tetiklenmez.

10sn klip: Max 20-25 kelime; <5sn replik: Max 12 kelime.

Gemini Omni 1.1 Flash        ÖLÇÜLMÜŞ
A male astronaut says: "Reactor status clear."    
Ses üretilebilir veya sessiz kalabilir.

ÇOK YÜKSEK. Tırnak işareti ekrana alt altyazı çizer.

N/A (Görsel metne dönüşür).

Gemini Omni 1.1 Flash        ÖLÇÜLMÜŞ
speaks the line: We are losing pressure.    
Doğal tempolu ses sentezi sağlar.

YOK. Temiz işitsel çıktı.

<5sn replik: Max 10-12 kelime.

Gemini Omni 1.1 Flash        UYGULAMA
says in a low voice: System failure.    
Alçak frekanslı tonal fısıltı/konuşma üretir.

YOK. İki nokta kullanımı güvenlidir.

<5sn replik: Max 8-10 kelime.

Gemini Omni 1.1 Flash        UYGULAMA
...says: [line]. No subtitles, heard only, never shown as text.    
Kusursuz ses sentezi ve sıfır altyazı garantisi.

SIFIR. Bütün alt metin parametreleri engellenir.

<5sn replik: Max 12 kelime (Toplam prompt 30-80 kelime).

Gemini Omni 1.1 Flash        ÖNERİ
  
(b) SENKRON TABLOSU (Shot Scale, Facial Orientation & Failure Modes)
Çekim Ölçeği ve Yüz Durumu    Senkron Sonucu    Arıza Biçimi (Failure Mode)    Kaynak    Etiket
Yakın Çekim (CU) / Açık Yüz    
Mükemmel Fonem-Dudak Hizalaması.

Arıza yok; mikro mimikler korunur.

ÖLÇÜLMÜŞ
Orta Yakın Çekim (MCU) / Açık Yüz    
Yüksek Kaliteli Senkronizasyon.

Hızlı kelimelerde nadir piksel kayması.

ÖNERİ
Orta Çekim (MS) / Açık Yüz    
Orta / Zayıf Senkronizasyon.

Ağız piksellerinde bulanıklaşma, sesin kadrajdan kopması.

UYGULAMA
Geniş Çekim (WS) / Açık Yüz    
SENKRON ÇÖKER.


Ağız hareketi oluşmaz; ses dış ses gibi duyulur.

ÖLÇÜLMÜŞ
Profil Açı (90 Derece) / Açık Yüz    
Düşük Senkronizasyon.

Yan dudak dokusunda bükülme (warping) ve zamansal takılma.

UYGULAMA
Kasklı / Açık Vizör (Şeffaf)    
İyi Senkronizasyon.

Cam yansımasında zaman zaman piksel kırılması.

UYGULAMA
Kasklı / Kapalı veya Koyulaştırılmış Vizör    
GÖRSEL SENKRON İMKANSIZ.


Vizör üzerinde bozuk yüz morfları denemesi veya fiziksel titreşimsiz donuk ses.

ÖLÇÜLMÜŞ
  
(c) SES KATMANI TABLOSU (Audio Layering & Environmental Acoustics)
Ses Katmanı    İngilizce Birebir Kalıp    Uyum Düzeyi    İstenmeyen Yan Etki / Risk    Kaynak    Etiket
Konuşma (Dialogue)    Dialogue: The astronaut says: Fuel low.    
Yüksek.

Tırnak kullanılırsa ekran yazısı tetiklenir.

ÖLÇÜLMÜŞ
Efekt (SFX)    SFX: Mechanical airlock latch click as the door seals.    
Yüksek (Eyleme tam hizalanır).

Zamansal bağlaç yoksa foley kayması yaşanabilir.

ÖNERİ
Ortam (Ambient)    Ambient: Pressurized cockpit air hum, subtle hum.    
Yüksek.

Varsayılan uzay dip gürültüsü basabilir.

UYGULAMA
Müzik (Music Muting)    No background music, diegetic score only.    
Tam Uyum.

İfade yazılmazsa model dramatik müzik ekler.

ÖLÇÜLMÜŞ
Sessizlik / Vakum    Ambient: Vacuum silence outside, internal suit breathing only.    
Orta / Yüksek.

Dış uzay gürültüsünü kapatmak için negatif etiket gerekir.

ÖNERİ
  
7. Doğrulanabilir Bulgular, Hipotezler ve Kaynak Haritalama Listeleri
Liste 1: Doğrulanabilir Bulgular ve Kaynaksız İddialar (Hipotezler)
Doğrulanabilir Bulgu: Gemini Omni 1.1 Flash modelinde tırnak işareti ("") kullanımı ekran yazısını/altyazıyı tetiklerken, iki nokta (:) kullanımı yerel konuşma sentezini tetiklemektedir.   

Doğrulanabilir Bulgu: Yüklenen insan içerikli videolara diyalog ekleme yeteneği güvenlik gerekçesiyle model düzeyinde kısıtlanmıştır.   

Doğrulanabilir Bulgu: Ardışık kliplerde aynı karakterin ses tonunu korumanın belgelenmiş tek yolu previous_interaction_id referansıyla oturumu uzatmaktır.   

Kaynaksız İddia (Hipotez): "İstem içerisine 'lip sync mode' veya 'phoneme lock' yazılması dudak senkronizasyon yeteneğini yapay olarak artırır."

Neden Doğrulanamadığı: Google'ın resmi teknik dokümantasyonunda veya API parametre listesinde "lip sync mode" adında bir istem tetikleyicisi bulunmamaktadır.   

Kaynaksız İddia (Hipotez): "İstemde frekans hertz değeri vererek (örneğin 'audio at 44.1kHz') ses kalitesi yükseltilebilir."

Neden Doğrulanamadığı: Modelin işitsel difüzyon kodlayıcısı metin tabanlı frekans komutlarını ayrıştırmamakta, yalnızca akustik ve ortamsal nitelik zarflarını işlemektedir.

Liste 2: Tam Kaynak ve Model / Sürüm Dökümü Listesi
Gemini Omni 1.1 Flash (gemini-omni-1.1-flash) Bulguları:

Google DeepMind / Google Developers Documentation: Build with Gemini Omni 1.1 Flash (27 Ağustos 2026) — Model mimarisi, Interactions API, 40s uzatma, 360p-4K çözünürlük merdiveni, 10s bağlam penceresi.   

Replicate Model Specification (google/gemini-omni-1.1): API girdi şeması, yerel ses parametreleri, SynthID filigranı, varsayılan 720p ayarları.   

Morphic / Kie AI / VideoWeb AI Teknik Raporları: Çoklu tur etkileşim, ses katmanı etiketleri (Dialogue:, SFX:, Ambient:), 30-80 kelime optimum aralığı.   

PromptsLove & Community Benchmark Reports: Tırnak ve iki nokta üst üste ayrımı, altyazı gömme riski, güvenlik ihlali mesajı metni, çekim ölçeği dudak senkronu kırılma noktaları.   

Google Veo 3.1 (veo-3.1-p) Bulguları (Motor Ayrımı):

Veo 3.1 Prompting Guides & Benchmarks: Yerel ses etkileşim dili eksikliği, bağımsız difüzyon motoru yapısı, diyalog sentezi yerine görsel estetiğe odaklı mimari ayrımı.   


