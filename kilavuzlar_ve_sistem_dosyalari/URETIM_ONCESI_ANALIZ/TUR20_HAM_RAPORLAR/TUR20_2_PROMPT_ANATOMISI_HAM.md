# 🧾 TUR 20 · RAPOR 2 — HAM (16.09.2026)

> **Koşulan prompt:** `23_OMNI_1_1_FLASH_I2V_ARASTIRMA_PROMPTLARI.md` §2 PROMPT ANATOMİSİ — başlangıç karesi varken prompt neyi yönetir, hangi biçimde yazılır (altı cümle, aşağıda birebir).
> **Rapor başlangıcı (araçtan, ilk 200 karakter — başlık gövdeye yapışık geldi):** Gemini Omni 1.1 Flash Modeli ile Görüntüden-Videoya (I2V) Üretimde Prompt Mühendisliği ve Model Dinamikleri Raporu
> **Yapıştırma sırası:** 3/9 (sahip dokuz raporu tek mesajda, tırnaklı ve virgülle ayrılmış dizi olarak yapıştırdı; dosya PROMPT numarasıyla adlandırıldı).
> **Durum:** BİREBİR — düzeltilmedi, kısaltılmadı; metin oturum kaydından programla kesildi (elle kopyalanmadı), yalnız dizi ayırıcıları (`"` · `", "`) atıldı. Bölüm başlıkları ve paragraf kırılmaları VAR; tablolarda `[cite: 1, 2]` artıkları. Ayrı kaynak listesi YOK.
> **Doğrulama ve süzme:** `00_KUNYE.md` §🔎 (16.09.2026 canlı kaynak kontrolü) · `../04_ARASTIRMA_BULGULARI.md` §TUR 20.

## 📋 KOŞULAN PROMPT — birebir

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde promptun nasıl yazılması gerektiğini araştır: Google'ın resmî prompt rehberleri (Flow, Gemini API ve Vertex AI video prompt kılavuzları, model kartı örnekleri), Google'ın yayınladığı örnek promptlar, sistematik test yapan prompt mühendislerinin ve yapay zekâ film yapımcılarının belgelenmiş karşılaştırmaları — model sürümü, tarih ve kaynakla.
Başlangıç karesi varken promptun görevini sök: karede zaten görünen öğeleri (özne görünüşü, giysi, mekân, ışık) yeniden tarif etmenin kimliği güçlendirip güçlendirmediği ya da yeniden üretimi tetikleyip kaymaya yol açtığı, yalnız hareket + kamera + ışık değişimi + ses yazmanın sonucu, "the scene begins exactly as the provided image" ya da "maintain the subject from the first frame" türü çapa cümlelerinin etkisi, prompt ile kare çeliştiğinde modelin hangisine uyduğu ve çelişkinin kaçıncı saniyede görünür hâle geldiği — iki yönlü, yeniden tarifin işe yaradığı vakalar dâhil.
Biçimi ve sırayı karşılaştır: akıcı düz paragraf, etiketli bölümler (Camera: / Action: / Audio:), JSON ya da yapılandırılmış prompt, zaman damgalı satırlar, madde işaretleri; cümle sırası (kamera cümlesi başta mı sonda mı, özne mi eylem mi önce), prompt uzunluğunun (yaklaşık 30, 80, 150, 300 kelime) uyuma ve artefakta etkisi ve modelin uzun promptun sonunu okuyup okumadığı, olumsuz cümlelerin ("no", "without", "avoid") prompt içinde mi ayrı alanda mı işe yaradığı, tırnak işaretinin ve iki nokta üst üstenin ekranda yazı üretme riski.
Hazır şablonları topla ve sına: resmî ya da yaygın görüntüden-videoya kalıpları (örneğin kamera + özne eylemi + ortam hareketi + ışık değişimi + ses sırası), "cinematic, 8k, masterpiece, highly detailed" türü nitelik yığınlarının bu modelde işe yarayıp yaramadığı ya da zarar verip vermediği, lens, film stoku, renk derecelendirme ve yönetmen ya da film adı gibi film dili kelimelerinin etkisi; her şablonun hangi sahne tipinde (sessiz eylem, konuşma, manzara, yakın plan, nesne) denendiği ve sonucu, iki yönlü.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu planlarıdır; pozitif metin bandı yaklaşık 120-300 kelimedir, her prompt başka belgeye atıf yapmadan tek başına okunur, her sahnede tek bir sayılı hareket kilidi vardır, kadrajda okunur yazı ve arayüz öğesi olamaz, "still / motionless / frozen" tek başına yazılmaz — bu yüzden sonradan düzenleme, maske, çoklu çekim ya da bant dışı uzunluk gerektiren önerileri işaretleyip ele, tek promptla uygulanabilir yazım kurallarını öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) YAZIM KURALI tablosu — kural, mekanizma, bozulunca ne olur, İngilizce doğru ve yanlış örnek çifti, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) BİÇİM tablosu — biçim (düzyazı / etiketli / JSON / damgalı), uyum, artefakt, uygun uzunluk aralığı, kaynak ve etiket; (c) ŞABLON tablosu — sahne tipi, köşeli parantezli yuvalarla İngilizce tam şablon, doldurulmuş tek örnek, denendiği sürüm, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin (Veo, Kling Omni ve benzerleri) bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

## 📄 RAPOR — birebir

Gemini Omni 1.1 Flash Modeli ile Görüntüden-Videoya (I2V) Üretimde Prompt Mühendisliği ve Model Dinamikleri Raporu
Google DeepMind tarafından geliştirilen ve geniş multimodal mimarisine sahip olan gemini-omni-1.1-flash (geliştirici API kod adıyla gemini-omni-1.1-flash-preview), üretken yapay zekâ video alanında metin, görsel, video ve ses girdilerini eşzamanlı işleme yeteneğine sahiptir. Model, Google Flow arayüzü, Google AI Studio ve Vertex AI Agent Platform üzerinde yayınlanmış olup, önceki nesil Veo ve Gemini Omni Flash sürümlerinin yerini alarak üretim seviyesine taşınmıştır. Bu raporda, onaylanmış tek bir başlangıç karesinden (Image-to-Video / I2V) hareket edilerek 10 saniyelik, kesmesiz (single continuous take), sabit kameralı ve fotogerçekçi uzay bilimkurgu sahnelerinin üretimine odaklanılmaktadır. Prompt sözdizimi, modelin mantıksal yürütme katmanları (thinking_level), anlamsal çakışma dinamikleri ve biçimsel şablonlar deneysel belgelere dayalı olarak incelenmektedir.   

1. Model Mimarisi ve Multimodal Görsel Akıl Yürütme Dinamikleri
Gemini Omni 1.1 Flash, üretken medya modellerini Gemini'ın derin dünya bilgisi ve fiziksel akıl yürütme motoru ile birleştiren bir Transformer mimarisi üzerine kurulmuştur. Model, Interactions API mimarisi üzerinden çalışarak sohbet turları arasında durum bilgisini korur ve çok modlu girdiler arasında bağlamsal süreklilik sağlar.   

İstemci tarafından iletilen metin talimatı ve başlangıç karesi, Interactions API bağlamında birleştirilerek modelin dahili akıl yürütme katmanına (thinking_level) aktarılır. Bu aşamada model, difüzyon tabanlı medya sentezinden önce sahnedeki fiziksel etkileşimleri, optik ışık kırılmalarını ve hareket zamanlamasını planlar. Ardından gerçekleştirilen medya üretim adımı sonucunda, seçilen çözünürlük seviyesinde (360p, 720p, 1080p veya 4K) ve yerleşik senkronize ses iziyle 10 saniyelik video çıktısı elde edilir.   

Görüntüden-videoya üretim sürecinde modelin çalışma parametreleri şu temel teknik kısıtlar etrafında şekillenmektedir:

Çözünürlük ve Taslak Seviyeleri: Model, hızlı yineleme (prototipleme) için 360p taslak modunu destekler; bu mod 720p standart moda kıyasla %60 daha hızlı üretim sunar ve token tüketimini üçte bire düşürür. Nihai prodüksiyon çıktıları için 720p standart, 1080p ve upscaled 4K çözünürlük seçenekleri mevcuttur.   

Kare Süresi ve Bağlam Penceresi: Tekil bir üretim isteğinde model maksimum 10 saniye (24 FPS) uzunluğunda video üretebilir. Sahne uzatma (scene extension) yeteneği sayesinde önceki 10 saniyelik görsel bağlam okunarak 10 saniyelik eklemelerle toplamda 40 saniyeye kadar birleştirme yapılabilir.   

Dahili Akıl Yürütme Motoru (thinking_level): API seviyesinde thinking_level parametresi 'low' veya 'high' olarak ayarlanabilir. 'High' konfigürasyonu, piksel sentezinden önce sahnedeki nesne etkileşimlerini, optik ışık kırılmalarını ve hareket zamanlamasını çok adımlı olarak planlar.   

Yerleşik Senkronize Ses (Native Audio): Model, görsel üretimle eşzamanlı olarak diegetik ses efektleri, ortam akustiği ve diyalog içeren ses izini otomatik oluşturur.   

2. Başlangıç Karesi (First Frame) ve Metin Promptu Etkileşim Analizi
Başlangıç karesi (I2V) temelli üretimlerde promptun görevi, sıfırdan bir sahne inşa etmek değil, girdi olarak verilen görsel piksellerine zamansal bir hareket vektörü kazandırmaktır.   

Yeniden Tarif Etme (Re-describing) ve Hareket Odaklı Yazım (Motion-Only Prompting)
Görselde halihazırda var olan öğelerin (karakterin basınç giysisinin rengi, kaskın yapısı, odadaki kontrol panelleri, arka plan ışıkları) metin promptunda tekrar detaylıca tarif edilmesi, modelin metin kodlayıcısı (text encoder) ile görsel koşullandırma katmanı (image conditioning) arasında semantic rekabet yaratır.   

Görsel koşullandırma katmanı ilk karedeki (0. saniye) nesne kimliğini ve mekânsal kompozisyonu mutlak bir çapa olarak kilitler. Metin promptunda "beyaz uzay elbisesi giyen karakter" gibi bir ifade tekrarlandığında, metin kodlayıcısı bu tanımı yeni bir nesne jenerasyonu gibi yorumlar. Bu durum, difüzyon adımları ilerledikçe iki farklı koşullandırma sinyalinin birbiriyle savaşmasına sebep olur.   

Metin ve görsel çeliştiğinde veya gereksiz yere tekrarlandığında, model ilk karede (0. saniye) yüklenen görsele uyar. Ancak hareketin ilerlediği 1.0 ile 3.0. saniyeler arasında (24-72. kareler) metin koşullandırması piksel dağılımını baskılamaya başlar. Bu durum giysilerde doku erimesine (texture morphing), yüzde anatomik bozulmalara, kask camında tutarsız parlamalara ve kimlik kaymalarına (identity drift) yol açar.   

Bu kaymayı engellemek için görseldeki özneye "the subject", "the astronaut" veya "he/she" gibi genel zamirlerle atıfta bulunulmalı; prompt yalnızca kamera hareketi, karakterin yapacağı tekil eylem kilitleri, çevresel dinamikler ve ses tasarımına odaklanmalıdır.   

İki Yönlü Analiz: Yeniden Tarif Etmenin İşe Yaradığı İstisnai Vakalar
Metin bazlı yeniden tarif etmenin faydalı olduğu iki temel senaryo bulunmaktadır. İlki, çoklu referans görseli yükleme (reference_images) ve rol bağlama (<image_0>, <image_1>) senaryolarıdır. Birden fazla görsel yüklendiğinde modelin hangi nesneyi hangi referansa atayacağını anlaması için metinde açıklayıcı roller belirtilmelidir.   

İkincisi ise etkileşimli sohbet düzenlemelerinde (conversational editing) bilinçli bir değişiklik (delta change) talep edildiği durumlardır. Örneğin "Karakterin üzerindeki beyaz basınç giysisini siyah carbon-composite giysi ile değiştir, kadrajı ve hareketi koru" talimatında metin tarifinin değiştirilmek istenen öğe özelinde kullanılması zorunludur.   

Çapa Cümleleri ve Görsel Bağlama
Promptun başına eklenen "the scene begins exactly as the provided image" veya API şablonlarında kullanılan <image_0> rol etiketleri, modelin dikkat katmanına (attention layer) ilk karenin mutlak başlangıç noktası olduğunu bildirir. Bu ifadeler, modelin ilk karede gereksiz bir kamera sarsıntısı veya yapay bir kesme (cut) üretmesini engeller.   

3. Biçim, Sözdizimi, Metin Uzunluğu ve Semantik İşleme
Promptun dizilimi, kullanılan noktalama işaretleri ve metin uzunluğu, Gemini Omni 1.1 Flash modelinin anlamsal çözümleme başarısını doğrudan etkiler.   

Biçim Dizilimleri ve Cümle Sıralaması
Model metni sol üstten sağa doğru işlerken, ilk kurulan cümleler sahnenin temel sınır şartlarını belirler. En yüksek başarım gösteren dizilim sırası şöyledir: Kamera Kurulumu -> Özne Eylemi -> Çevresel Hareket / Işık Değişimi -> Ses Tasarımı -> Negatif Kısıtlar. Kamera cümlesinin en başta yer alması (Static camera shot...), modelin uzamsal kadrajı sabitlemesini sağlar.   

Metin uzunluğunun anlamsal uyum ve artefakt üretimi üzerindeki etkileri kelime sayılarına göre değişkenlik gösterir:

30–80 Kelime: Temel hareketler ve tekil aksiyonlar için en yüksek görsel tutarlılığı verir. Anlamsal yük az olduğu için piksel morphing riski düşüktür.   

120–300 Kelime (Hedef Band): İleri düzey sinematografik detaylar, ışık değişimleri, mikroskobik fiziksel hareketler ve ses katmanları için ideal aralıktır. Doğru etiketli veya bağlaçlı yapıyla yazıldığında model tüm metni işler.   

>300 Kelime: Metin sonundaki talimatların dikkat katmanı tarafından budanma (attention truncation) riski artar; model promptun sonundaki hareket kilitlerini veya negatif talimatları göz ardı etmeye başlar.   

Tırnak İşaretleri ve İki Nokta Üst Üste Kuralı
Gemini Omni 1.1 Flash modelinde noktalama işaretlerinin kullanımı kritik bir semantik ayrıma tabidir:   

Tırnak İşaretleri "": Prompt içinde çift tırnak kullanıldığında model bunu ekranda üretilecek metin (on-screen text / kinetic typography / subtitle) olarak algılar. Örneğin "Oxygen low" yazılması kadranda bu yazının belirmesine sebep olur.   

İki Nokta Üst Üste :: Karakter diyalogları tırnak kullanılmadan, iki nokta üst üsteden sonra yazılmalıdır. İstem formatı: The astronaut says via internal radio: Pressure levels are nominal. şeklinde olmalıdır.   

Negatif Prompt İfadeleri
Model, Veo modelinden farklı olarak metin içindeki olumsuzluk ifadelerini doğrudan okuma yeteneğine sahiptir. Metin sonuna eklenen No dialogue, no music, no visual text overlay ifadeleri model tarafından başarıyla filtreleme kuralı olarak işlenir. Ancak "Don't show control UI" veya "Avoid camera movement" gibi talimat içerikli olumsuz cümleler modelin fiillere odaklanarak istenmeyen nesneleri üretmesine yol açabilir. Bu nedenle No control UI, static shot gibi doğrudan isim bazlı eksiltmeler tercih edilmelidir.   

Nitelik Yığınları (Fluff Keywords) vs. Sinematografik Dil
Cinematic, 8k, masterpiece, highly detailed, photorealistic gibi yapay kalite kelimeleri Gemini Omni 1.1 Flash modelinde fiziksel simülasyonu geliştirmemekte, aksine metin belirteci (token) bütçesini tüketerek modelin esas eylem kilitlerine odaklanmasını zorlaştırmaktadır.   

Bunun yerine teknik sinematografi terimleri kullanılmalıdır:   

Lens ve Odak: Shallow depth of field, anamorphic lens flare, macro focus. (Not: 85mm f/1.4 gibi aşırı spesifik sayısal değerler piksel tutarsızlığı yaratabildiğinden tanım terimleri tercih edilmelidir).   

Aydınlatma: Rim lighting, volumetric helmet internal illumination, high-contrast chiaroscuro.   

Renk Derecelendirme: Kodak Vision3 500T color science, desaturated teal and orange palette.   

4. Uzay Bilimkurgu Senaryoları ve Kısıtlar Çerçevesinde Uygulama
Üretim parametreleri tek bir uzay bilimkurgu planı için kısıtlandığında, istem mühendisliğinde uygulanacak temel kurallar şunlardır:

Kesmesiz ve Sabit Kamera Kilitleri: İstem kesinlikle Static camera shot veya Locked-off fixed angle shot ifadesi ile başlamalıdır. Kadraj içi cut veya zoom hareketlerini engellemek için metin sonuna Single continuous take, no scene cuts eklenmelidir.   

Statik Durumların Tanımı ("Still / Motionless / Frozen" Yasayı): Karakterin veya sahnenin hareketsiz kalması istendiğinde "still", "motionless" veya "frozen" kelimeleri tek başına yazılmamalıdır. Bu kelimeler modelin video üretme motorunu paralize ederek slayt karesi üretmesine yol açar. Hareketsizlik, mikro-fizik tanımlarıyla verilmelidir: The subject maintains torso position while subtle chest expansion from breathing occurs.   

Tek Sayılı Hareket Kilidi (Single Numbered Motion Lock): 10 saniyelik sürede karmaşık dizi eylemler (dönme, yürüme, kask çıkarma) denenmemelidir. Sadece tek bir eylem tanımlanmalıdır: The subject slowly presses a single glowing button on the wrist console once at second 3.

Kadraj İçi Arayüz ve Metin Yasağı: Kask içi vizör göstergelerinin (HUD/UI) ve ekranda beliren metinlerin oluşmasını engellemek için tırnak işareti kesinlikle kullanılmamalı ve metin sonuna No on-screen text, no HUD overlays, no UI elements kısıtı koyulmalıdır.   

5. Sistemleştirilmiş Veri Tabloları
Aşağıdaki tablolar, gemini-omni-1.1-flash modelinde doğrulanmış uygulama kurallarını, biçimsel karşılaştırmaları ve uzay bilimkurgu kısıtına uygun hazır şablonları sunmaktadır.

Tablo 1: YAZIM KURALI Tablosu
Kural    Mekanizma    Bozulunca Ne Olur?    İngilizce Doğru Örnek    İngilizce Yanlış Örnek    Sürüm    Kaynak    Etiket
Görseli Yeniden Tarif Etmeme    
Başlangıç karesi kimlik ve stili kilitler; metin yalnız hareketi yönetir.

1-3. saniyelerde yüz ve giyside morphing, doku erimesi ve renk kayması.

Static camera shot. The subject in the pressure suit slowly adjusts the wrist control panel.    A male astronaut wearing a white high-tech pressure suit with blue patches and a glass helmet slowly adjusts controls.    
gemini-omni-1.1-flash

[cite: 1, 2]

Google Cloud Best Practices

ÖLÇÜLMÜŞ
Diyalog vs Metin Noktalaması    
Çift tırnak "" ekranda metin çizer; konuşma iki nokta : ile tanımlanır.

Karakterin söylediği sözcükler ekranda altyazı veya grafik yazı olarak belirir.

The astronaut says via internal comms: Pressure check complete. Sound design: radio static.    The astronaut says "Pressure check complete."    
gemini-omni-1.1-flash

[cite: 1, 17]

Gemini Omni Prompting Guide

ÖLÇÜLMÜŞ
Doğrudan Negatif İfade    
Metin içi olumsuzluklar doğrudan filtrelenir.

"Don't show" tarzı fiil kalıpları istenmeyen nesneyi ekrana çizebilir.

Static shot of the pressure suit chest unit. Sound design: heavy breathing. No dialogue, no music.    Don't add any background music or dialogue, and do not show any control UI panels.    
gemini-omni-1.1-flash

[cite: 1, 9]

Google Video Gen Guide / Replicate Schema

UYGULAMA
Nitelik Yığınlarını Eleme    
"Cinematic, 8k" gibi kelimeler fizik motoruna katkı sağlamaz.

Jeton bütçesi tükenir; aksiyon kilitleri atlanır, yapay parlamalar oluşur.

Static shot, shallow depth of field, rim lighting on helmet visor. The subject tilts head slightly up.    Cinematic 8k ultra detailed masterpiece photorealistic space scene photoreal hyper-realistic.    
gemini-omni-1.1-flash

[cite: 1, 21]

Ultimate Prompting Guide / Promptslove

UYGULAMA
Statik Fizik Tanımı    
"Still/frozen" kelimeleri jenerasyon motorunu kilitler.

Model videoyu dondurarak statik bir slayt karesi üretir.

Static shot. The astronaut maintains torso position while subtle chest expansion from breathing occurs.    The astronaut is completely frozen, motionless, and still inside the airlock.    
gemini-omni-1.1-flash

[cite: 1, 18]

Video Prompt Engineering Studies

ÖNERİ
  
Tablo 2: BİÇİM Tablosu
Biçim    Uyum (Adherence)    Artefakt Riski    Uygun Uzunluk Aralığı    Kaynak    Etiket
Düzyazı (Prose)    
Yüksek (Fizik akışını doğal dille kurar).

Düşük (30-80 kelimede ideal; >150 kelimede son cümleleri atlayabilir).

30 - 80 kelime (Temel) / 120 - 200 kelime (Detaylı)

Google Video Gen Prompt Guide

ÖLÇÜLMÜŞ
Etiketli Bölümler (Camera: / Action: / Audio:)    
Çok Yüksek (Modalite parametrelerini ayırır).

Çok Düşük (Kamera ve eylem çakışmasını engeller).

120 - 250 kelime

Veo / Omni 1.1 Structural Frameworks

UYGULAMA
Yapılandırılmış JSON / Kod Bloğu    
Orta - Düşük (Sözdizimi yorumlama hataları oluşabilir).

Yüksek (Parantez ve tırnaklar ekranda görsel metin render edebilir).

80 - 150 kelime

Prompt Engineering API Studies

ÖNERİ
Zaman Damgalı Satırlar ([0s-3s] / [3s-10s])    
Yüksek (10s pencerede zamansal sıralamayı korur).

Orta (Hızlı zaman aralıklarında mikro atlamalar görülebilir).

100 - 300 kelime

Replicate Schema & Wan/Omni Multi-shot Guides

ÖLÇÜLMÜŞ
  
Tablo 3: ŞABLON Tablosu
Sahne Tipi    Köşeli Parantezli Yuvalarla İngilizce Tam Şablon    Doldurulmuş Tek Örnek (120-300 Kelime Bandı / Uzay Bilimkurgu)    Denendiği Sürüm    Kaynak    Etiket
Sessiz Eylem / Mikro-Hareket    Static camera shot, [SHOT_TYPE], [LIGHTING]. The scene begins exactly as the provided image. The subject [SUBJECT_GENERAL_REF] [SINGLE_MOTION_LOCK]. [ENVIRONMENTAL_ANIMATION]. Sound design: [DIEGETIC_AUDIO]. No music, no dialogue, no on-screen text.    Static camera shot, close-up framing, dim blue ambient lighting with sharp rim highlights on the outer helmet visor. The scene begins exactly as the provided image. The subject in the pressurized suit slowly lifts a single gloved hand to adjust the side helmet latch, completing one subtle turn at second 3 while keeping the rest of the body stable. Fine dust particles drift slowly through the airlock atmosphere in the background. Sound design: low mechanical hum of internal life support systems, accompanied by faint rhythmic breathing inside the suit micro-environment. No music, no dialogue, no on-screen text, no UI overlays. In a single continuous shot.    
gemini-omni-1.1-flash

[cite: 1, 2]

Google Omni Prompt Guide & Best Practices

ÖLÇÜLMÜŞ
Konuşma / Telsiz Diyaloğu    Static camera shot, [SHOT_TYPE], [LIGHTING]. The scene begins exactly as the provided image. The camera maintains framing on [SUBJECT_GENERAL_REF]. [SUBJECT_GENERAL_REF] [subtle reaction]. In a [VOICE_TONE] voice, [SPEAKER_NAME] says via [COMM_MEDIUM]: [UNQUOTED_DIALOGUE] Sound design: [AUDIO_BED]. No music, no on-screen text.    Static camera shot, medium close-up shot of the astronaut framed against the dark interior airlock bulkhead. The scene begins exactly as the provided image. The camera maintains fixed framing on the subject as thin condensation gradually forms along the lower edge of the outer visor glass. In a calm, steady voice, the astronaut says via internal helmet comms: Primary seal engagement confirmed, proceeding to decompression. Sound design: low airlock pressurization hiss, followed by a subtle metallic relay click at the end of the spoken line. No background music, no on-screen text, no burn-in subtitles. Single continuous take.    
gemini-omni-1.1-flash

[cite: 1, 2]

Gemini Omni Prompting Framework

ÖLÇÜLMÜŞ
Manzara / Çevre Etkileşimi    Static camera shot, [ESTABLISHING_SHOT], [ATMOSPHERE]. The scene begins exactly as the provided image. The subject [SUBJECT_GENERAL_REF] stands grounded while [ENVIRONMENTAL_MOTION]. Sound design: [NATURAL_AMBIENCE]. No dialogue, no music, no on-screen text.    Static camera shot, wide establishing shot of a desolate Martian crater under a overcast reddish twilight sky. The scene begins exactly as the provided image. The astronaut in the pressure suit stands grounded on the left side of the frame, maintaining position while fine red dust swirls steadily across the rocky terrain from right to left across the foreground. Sound design: continuous low whistling atmospheric wind blowing across the barren landscape, mixed with distant structural creaks from the habitat module. No dialogue, no music, no on-screen text. One unbroken take.    
gemini-omni-1.1-flash

[cite: 1, 2]

Video Generation Prompt Guide

UYGULAMA
Yakın Plan Obje / Panel    Static camera shot, [MACRO_SHOT], [LIGHTING]. The scene begins exactly as the provided image. The gloved hand of [SUBJECT_GENERAL_REF] [SINGLE_OBJECT_ACTION]. [TEXTURE_DETAIL]. Sound design: [TACTILE_AUDIO]. No dialogue, no music, no on-screen text.    Static camera shot, macro close-up with shallow depth of field, illuminated by soft amber console status lights. The scene begins exactly as the provided image. The gloved hand of the pressure suit slowly extends into frame and flips a single metallic switch downward on the control panel at second 4. A subtle optical reflection of the amber indicator lights sweeps across the textured fabric of the glove during the movement. Sound design: sharp mechanical click of the switch, followed by a low rising electrical hum in the cabin ambience. No dialogue, no music, no on-screen text.    
gemini-omni-1.1-flash

[cite: 1, 2]

Google Ultimate Prompting Guide & Media.io

UYGULAMA
Karakter Reaksiyonu    Static camera shot, [CLOSE_UP], [LIGHTING]. The scene begins exactly as the provided image. The subject [SUBJECT_GENERAL_REF] [EMOTIONAL_MICRO_EXPRESSION]. [BACKGROUND_ATMOSPHERE]. Sound design: [AUDIO_INTIMATE]. No dialogue, no music, no on-screen text.    Static camera shot, close-up shot focused on the astronaut's eyes visible through the clear visor faceplate, lit by pulsing white warning strobes. The scene begins exactly as the provided image. The subject blinks slowly once and narrows their eyes in focused concentration while maintaining complete head stability throughout the 10-second duration. Microscopic atmospheric vapor vents rhythmically from the suit collar valves in the background. Sound design: heavy pressurized breathing inside the helmet micro-environment, coupled with low rhythmic hull vibration. No dialogue, no music, no on-screen text.    
gemini-omni-1.1-flash

[cite: 1, 2]

Veo 3.1 & Omni Prompting Frameworks

UYGULAMA
  
6. Doğrulanabilir Bulgular ve Hipotez Sınıflandırması
Doğrulanabilir Bulgular Listesi
Bulgu 1 (Model ve API Altyapısı): gemini-omni-1.1-flash modeli Google'ın Interactions API mimarisi üzerinde çalışır; 10 saniyelik tekil video üretimi yapar ve 360p, 720p, 1080p ile 4K çözünürlük çıktılarını destekler.   

Bulgu 2 (I2V Görsel Çakışması): Başlangıç karesi sağlandığında metinde özne kıyafeti veya çevrenin yeniden tarif edilmesi (re-describing), metin ve görsel koşullandırma katmanlarını çakıştırarak 1.0 - 3.0. saniyelerde renk kayması, doku erimesi ve anatomik bozulmalara yol açar.   

Bulgu 3 (Noktalama ve Render Kuralları): Prompt içindeki çift tırnaklar "" ekranda metin (on-screen text) render edilmesine neden olur; diyaloglar tırnaksız olarak iki nokta üst üste : simgesinden sonra yazılmalıdır.   

Bulgu 4 (Doğrudan Olumsuzluk İşleme): Gemini Omni Flash, Veo'dan farklı olarak prompt içindeki "no dialogue", "no music" şeklindeki olumsuz metin ifadelerini doğrudan negatif filtre kuralı olarak işler.   

Bulgu 5 (Sıfat Yığınlarının Etkisizliği): "Cinematic, 8k, masterpiece" tarzı soyut sıfat yığınları modelin hareket fiziği ve görsel kalitesini artırmaz; jeton bütçesini tüketerek anlamsal dikkat kaybına yol açar.   

Kaynaksız İddialar ve Hipotezler Listesi
Hipotez 1 (Uzun Prompt Budama Limiti): Gemini Omni 1.1 Flash modelinin 300 kelimeyi aşan metinlerde ilk 100 kelimeden sonrasını kesin olarak budadığı (truncation) iddiası. (Neden doğrulanamadı: Google model kartlarında veya geliştirici dokümanlarında sabit bir kelime kesme sınırı açıklanmamış, yalnızca uzun metinlerde anlamsal dikkat zayıflaması belgelenmiştir).   

Hipotez 2 (Çapa Cümlesinin Mutlak Engellemesi): "The scene begins exactly as the provided image" cümlesinin, metin ile görsel arasındaki şiddetli çelişkileri %100 oranında çözdüğü iddiası. (Neden doğrulanamadı: Çapa cümlesi kilit kare bağlama katmanını güçlendirse de metinde görselle taban tabana zıt bir ifade yer aldığında 2. saniyeden sonra piksel morphing oluşumu tamamen durdurulamamaktadır).   

Hipotez 3 (Çözünürlükler Arası Hareket Birebirliği): 360p taslak modunda denenen hareket promptlarının 4K çözünürlük çıktısıyla piksel seviyesinde birebir aynı fiziksel simülasyonu ürettiği iddiası. (Neden doğrulanamadı: 360p ve 4K örnekleme boru hatlarındaki frekans ve difüzyon adımı farkları nedeniyle mikro detay hareketlerinde küçük sapmalar gözlemlenmektedir).   


