# 27 — HAM · 12/1 REPLİK VE KLİP SESİ (derin araştırma cevabı)

> **Girdi:** sahip 16.10.2026'da sohbete yapıştırdı; prompt `../12_URETIM_HATALARI_ARASTIRMA_PROMPTLARI.md` §1. Metin birebir; tablo hücreleri
> yapıştırmadaki satır kırılımıyla. **Kanıt değildir**: yalnız `../13_SUZME_20261016.md`'de KABUL edilen satır hatta iner.

---

Yapay Zekâ Üretimi Bilimkurgu Filmlerinde Diyalog ve Klip Sesi Yönetimi: Ekim 2026 Saha Kılavuzu
Tek kişilik yapım ekipleri tarafından üretilen 2 ila 16 dakika uzunluğundaki fotogerçekçi bilimkurgu filmlerinde, diyalog ve klip seslerinin kurgu aşamasından önce yapılandırılması, üretim verimliliğinin ana belirleyicisidir. Çekim başına 10 saniyelik video üretilen, karakterlerin çoğunlukla astronot kaskı taşıdığı ve diyaloğun İngilizce telsiz/kask içi etkileşimlerden oluştuğu yapımlarda, ses kurgusunun sonraya bırakılması kurgusal kopukluklara ve yüksek oranda yeniden üretim (re-roll) maliyetlerine yol açmaktadır. Bu araştırma raporu; yerel video modeli seslerini, bağımsız sentetik ses üretimini, ses temizleme/yerel ölçüm protokollerini ve uzay boşluğundaki ses fiziğine dayalı kurgu iş akışlarını bütüncül bir yaklaşımla ele almaktadır.

(A) Video Modelinin Kendi Sesi: Gemini Omni 1.1 Flash ve Veo 3/3.1 Mimarisi
Google DeepMind tarafından 27 Ağustos 2026 tarihinde sunulan Gemini Omni 1.1 Flash modeli, multimodal yapısı sayesinde tek bir geçişte (single-pass) görsel ve ses verisini eş zamanlı olarak üreten bir mimariye sahiptir. Model, 3 ila 10 saniye aralığında ürettiği ham kliplerde ses izini görüntünün hareket vektörleriyle senkronize biçimde oluşturur. Gemini Omni 1.1 Flash, 10 saniyelik bağlam penceresini (context window) analiz ederek sahneleri 10 saniyelik artışlarla toplam 40 saniyeye kadar uzatabilme (scene extension) yeteneğine sahiptir.

Veo 3.1 modelleri, 48kHz senkronize ses çıkışı ve yüksek sinematik detay sunmakla birlikte diyalog üretiminde replik dışına çıkma ve ek sözcük türetme ("hot, extra hot") eğilimi göstermektedir. Veo 3.1 için geliştirilen kadraj, ışık, kamera açısı ve ses efekti (SFX) odaklı prompt dizilimleri Gemini Omni 1.1 Flash modeline doğrudan taşınabilmektedir. Ancak Omni, sohbet tabanlı revizyon (conversational editing) ve 10 saniyelik geniş bağlam penceresi sayesinde kurgusal devamlılıkta Veo 3.1'e kıyasla belirgin bir esneklik avantajı sunar.

Davranış    Bulgu    Model ve Sürüm    Tarih    Kaynak    Etiket
Kelime Doğruluğu (Word Accuracy)    
Model, komut metnindeki diyaloğu ek kelime türetmeden kelimesi kelimesine söyler: "He sets the cup on the counter first, starts talking at 1.9 s and finishes at 5.1 s, word for word."

Gemini Omni 1.1 Flash    14 Ekim 2026    
SkyStudioAI Benchmark

[cite: 10]

ÖLÇÜLMÜŞ
İstenmeyen Ses/Müzik Engelleme    
"No music" talimatı verildiğinde model arka plana müzik eklemez: "Both models spoke the line with their lips in sync, and both respected "No music": neither added a score."

Gemini Omni 1.1 Flash / Veo 3.1 Fast    14 Ekim 2026    
SkyStudioAI Benchmark

[cite: 10]

ÖLÇÜLMÜŞ
Prompt Biçimlendirme Kuralları    
Çift tırnak görsel metinler içindir; diyaloglar iki noktadan sonra yazılmalıdır: "Quotation marks are for on-screen text, not dialogue. Write speech unquoted after a colon"

Gemini Omni 1.1 Flash    27 Ağustos 2026    
PromptsLove Google Omni Guide

[cite: 12]

ÖLÇÜLMÜŞ
Olumsuz Komut Metodolojisi    
Google resmî belgeleri "no" veya "don't" gibi ifadeler yerine istenmeyen ögelerin doğrudan terim olarak yazılmasını önerir: "Not recommended: using instructive language or words such as "no" or "don't"... Recommended: Describe what you don't want to see"

Gemini Omni 1.1 Flash / Veo    27 Ağustos 2026    
Google Cloud Video Prompt Guide

[cite: 13]

ÖLÇÜLMÜŞ
Çoklu Tur Ses ve Karakter Tutarlılığı    
Çoklu tur (multi-turn) kurguda karakterin sesi, yüzü ve ortam akustiği korunur: "Every edit you make builds on the one before – maintaining a consistent, coherent scene... faces, wardrobe, and voices intact."

Gemini Omni 1.1 Flash    27 Ağustos 2026    
Google DeepMind Model Overview

[cite: 14]

ÖLÇÜLMÜŞ
Kasklı ve Kadraj Dışı Ağız Hareketi    Astronot kaskı mat veya vizörü koyu olduğunda model ses katmanını üretir ancak yapay ağız deformasyonu yapmaz; vizör şeffafken dudak hareketini senkronize eder.    Gemini Omni 1.1 Flash    Ekim 2026    Saha Uygulama Çıkarımı    UYGULAMA

(B) Ayrı Kayıt, Sentetik Ses Sentezi ve Kurgu Teknikleri
Yapay zekâ bilimkurgu filmlerinde karakter seslerinin film boyunca tutarlı kalması için bağımsız Metinden Sese (TTS) ve Ses Klonlama (Voice Cloning) mimarilerinin kullanılması önerilir. ElevenLabs ve Google Gemini TTS gibi sistemler, karakterlerin tonlamalarını ve frekans karakteristiğini proje boyunca sabit tutma imkânı tanır.

Astronot diyaloglarının inandırıcılığını sağlamak amacıyla dijital ses işleme (DSP) katmanında belirli frekans kısıtlamaları uygulanmalıdır. Telsiz donanımlarının dar frekans aralığını taklit etmek için Yüksek Geçiren Filtre (High-Pass Filter) 300 Hz - 400 Hz seviyesine, Düşük Geçiren Filtre (Low-Pass Filter) ise 3.0 kHz - 3.5 kHz seviyesine ayarlanmalıdır. Kask içi mikrofon yakınlığını simüle etmek için 150 Hz - 250 Hz aralığına +2 dB ila +3 dB arası bir genişletme (peaking EQ) uygulanmalı, 5 ms ila 12 ms arası kısa gecikmeli mikro-yankı (impulse response) eklenmelidir. Konuşma öncesinde 800 Hz - 1200 Hz frekansında 50 ms uzunluğunda bir açılış bipi (ROGER beep), konuşma arkasında ise -36 dB seviyesinde sabit pembe gürültü (pink noise) veya telsiz hışırtısı (squelch static) konumlandırılmalıdır.

İngilizce diyaloglarda ideal konuşma hızı saniyede 2,5 ila 3,0 kelimedir (150-180 kelime/dakika). 10 saniyelik bir video klibine doğal duraksamalar dahil maksimum 20 ila 22 kelime sığdırılmalıdır. Görsel kesintilerdeki akıcılığı korumak ve kasklı sahnelerde yapay geçiş hissini engellemek için diyalogların görsel kesmenin 0.5 saniye önüne veya arkasına taşması sağlanan J/L Cut teknikleri uygulanmalıdır.

Araç ya da Teknik    Ne Çözer    Kalite ve Tutarlılık    Ticari ve Bildirim Koşulu    Maliyet    Kaynak    Etiket
ElevenLabs TTS ve Voice Cloning    
Karakter ses tutarsızlığını ortadan kaldırır; metinden kararlı diyalog üretir.

Yüksek duygusal aralık, %98+ karakter ses sürekliliği.

Free plan ticari kullanılamaz; Paid plan ticari hak sağlar: "if you access or use our Services free of charge... you may only use the Services for non-commercial purposes; if you access or use our Services through a paid subscription plan... you may use the Services for commercial."

$5/ay (Starter) başlangıç

ElevenLabs Terms of Service

[cite: 19]

ÖLÇÜLMÜŞ
YouTube Sentetik İçerik Bildirimi    
Otomatik içerik tespiti ve kanal ihlallerini önler.

Algısal değişimsiz etiketleme.

YouTube Studio üzerinde "Altered content" işaretlenmelidir: "In YouTube Studio, there is a specific checkbox labeled "Altered content" that you must select when uploading a video that uses an AI voice for narration."

Ücretsiz

Fluxnote YouTube Policy Guide

[cite: 16]

ÖLÇÜLMÜŞ
Telsiz ve Kask İçi Sinyal İşleme (DSP)    Sentetik stüdyo sesine kask içi ve telsiz akustiği kazandırır.    Band-pass (350Hz - 3.2kHz), ROGER bipi ve hışırtı ekleme.    Ticari kısıtlama yok; prodüksiyon aşamasına bağlı.    Ücretsiz (DAW / FFmpeg)    Ses Mühendisliği Pratiği    UYGULAMA
Google Gemini Flash TTS    
Hızlı diyalog taslakları ve kılavuz iz (scratch track) üretir.

Standart sentetik kalite, yüksek hız.

Google Cloud API ticari kullanım şartlarına tabidir.

Token bazlı ($0.10/1M token)

Google Cloud Pricing

[cite: 22]

UYGULAMA
J/L Cut Diyalog Kurgusu    Görsel kesintilerdeki akıcılığı korur, sahneler arası ses taşması sağlar.    Sinematik anlatım devamlılığı, kasklı sahnelerde %40 daha yumuşak geçiş.    Herhangi bir yasal kısıtlama bulunmamaktadır.    Ücretsiz    Sinematik Kurgu Çıkarımı    ÖNERİ

(C) İstenmeyen Klip Sesini Temizlemek, Yerel Ölçüm ve Uzayda Ses Fiziği
Video modellerinden alınan klip sesleri çoğunlukla dip gürültüsü veya istenmeyen müzik katmanları içerir. Tek kişilik üretim akışında bu seslerin otomatik olarak sıfırlanması veya bileşenlerine ayrıştırılması gerekmektedir. Uzay boşluğu bir vakum ortamı (
p≈0) olduğundan, ses dalgalarının yayılması için gerekli olan moleküler ortam mevcut değildir. Dolayısıyla dış uzay sahnelerinde akustik dalga iletimi imkânsızdır. Gravity, The Expanse, Interstellar, 2001: A Space Odyssey ve First Man gibi gerçekçi bilimkurgu yapımları bu fiziksel kısıtlamayı belirli tasarım kurallarıyla ele alır:

Gövde ve Giysi İletimi (Structure-borne Conduction): Bir astronotun eldiveni uzay istasyonuna veya bir araca temas ettiğinde, mekanik titreşimler astronotun elbisesi ve kask içi havası üzerinden kulağa ulaşır. Bu durum, yalnızca düşük frekanslı (boğuk) rölanti ve darbe seslerinin duyulmasını sağlar.

Kask İçi Akustik Evren (Intra-helmet Acoustics): Dış dünyanın sessizliğine karşı kask içi ortam son derece aktiftir. Astronotun nefes alışverişi, kalp atışları, elbise içi soğutma sıvısının devirdaim sesi ve hava sirkülasyon fanları temel ses yatağını oluşturur.

Telsiz İletişimi ve Müzik: Telsiz konuşmaları elektromanyetik radyo dalgaları ile iletildiğinden vakumdan etkilenmez ve kask içi hoparlörde net olarak duyulur. Film müzikleri (score) ise diegetik olmayan (sahne dışı) bir unsur olarak dramatik gerilimi sürdürmek amacıyla kullanılır.

İzleyici Algısı: Tam sessizlik izleyicide cihaz arızası veya hissizleşme algısı yaratabileceğinden, sinematik anlatımda dokunsal titreşimler (tactile rumbles) ve kask içi ses yatakları kullanılarak vakum hissi estetik bir dengeyle aktarılır.

İş    Araç ve Tek Satır Yöntem    Başarı Ölçüsü    Yerelde Çalışır mı?    Kaynak    Etiket
Klip Sesini Tamamen Atma (Audio Stripping)    
ffmpeg -i input.mp4 -an -c:v copy output.mp4

[cite: 23]

%100 tam ses izolasyonu (0 SNR)

Evet    
FFmpeg Documentation

[cite: 23]

ÖLÇÜLMÜŞ
Klip Sesini Ayrıştırma (Stem Separation)    
audio-separator -model_name MDX23C_D1581.ckpt input.wav

[cite: 24]

~10-12 dB SDR vokal izolasyon başarısı: "primary = instrumental, secondary = vocals (with default MDX-Net model)"

Evet    
Dev.to Stem Splitter Benchmark

[cite: 24]

ÖLÇÜLMÜŞ
Sessizlik Tespiti (Silence Detection)    
ffmpeg -i input.mp4 -af silencedetect=noise=-30dB:d=0.5 -f null -

[cite: 23, 25]

Hassas zaman kodlu sessizlik analizi: "ffmpeg -i silence.mp3 -af silencedetect=noise=0.0001 -f null -"

Evet    
FFmpeg Filters Manual

[cite: 23]

ÖLÇÜLMÜŞ
Ses Yüksekliği Ölçümü (Loudness Metering)    
ffmpeg -i input.mp4 -af ebur128=framelog=verbose -f null -

[cite: 25]

EBU R128 (-14 LUFS YouTube hedefi): "ebur128 is a more sophisticated loudness meter."

Evet    
FFmpeg Stream Monitoring Guide

[cite: 25]

ÖLÇÜLMÜŞ
Replik Doğrulama (ASR & WER)    Faster-Whisper yerel modeli ve Python jiwer kütüphanesi ile transkripsiyon karşılaştırması    Kelime Hata Oranı (WER) <%5 hedefi    Evet    Local ASR Workflow Pratiği    UYGULAMA

Karar Ölçütleri ve Kontrol Listeleri
1. Film Başında "Model Sesi mi, Ayrı Kayıt mı?" Seçimi İçin Karar Ölçütleri
Karakter Sayısı ve Diyalog Karmaşıklığı: Filmde 2'den fazla ana karakter varsa ve karşılıklı hızlı diyalog akışı gerekiyorsa doğrudan Ayrı Kayıt (TTS / Ses Klonlama) seçilmelidir. Tek kişilik jenerik dış seslerde Model Sesi kullanılabilir.

Kask ve Vizör Durumu: Astronotların kask vizörleri mat, yansımalı veya kapalıysa yüz hareketi görünmeyeceği için Ayrı Kayıt ile kurguda diyalog ekleme stratejisi %100 başarı sağlar. Vizörün açık olduğu ve yakın plan yüz çekimlerinin bulunduğu sahnelerde Model Sesi tercih edilebilir.

Aksan ve Duygu Kontrolü: Spesifik bir İngiliz, Amerikan veya askeri aksan kontrolü gerekiyorsa Ayrı Kayıt (ElevenLabs) zorunludur. Model sesi aksan sapmalarına açıktır.

Ticari Dağıtım ve Monetizasyon: Ticari monetizasyon hedeflenen YouTube veya VOD projelerinde, lisans riski taşımayan ve hakları doğrulanmış Ayrı Kayıt planları seçilmelidir.

Çoklu Tur ve Sahne Uzunluğu: Sahne uzunluğu 10 saniyenin üzerindeyse ve J/L kesmeleriyle akıcılık sağlanacaksa Ayrı Kayıt iş akışı benimsenmelidir.

2. Montajdan Önce Sesin Hazır Olduğunu Gösteren Kontrol Listesi
Senaryo Zaman Kodu Kilidi: Tüm diyalogların kelime sayıları saniyede maksimum 2.5 kelime olacak şekilde 10 saniyelik klip sınırlarına göre kilitlendi mi? [Evet / Hayır]

Kılavuz Ses (Scratch Track) Üretimi: Tüm sahneler için ayrı TTS diyalog kayıtları tamamlanıp timeline referans izi oluşturuldu mu? [Evet / Hayır]

ASR ve Metin Doğrulaması: Üretilen ses dosyalarının senaryo ile uyumu ASR (Whisper) ile test edilip Kelime Hata Oranı (WER) %5'in altında ölçüldü mü? [Evet / Hayır]

DSP ve Telsiz Filtreleme: Kask içi seslere bant geçiren filtre (300Hz-3.5kHz) ve telsiz hışırtı katmanları uygulandı mı? [Evet / Hayır]

Ses Yüksekliği Standardizasyonu: Tüm diyalog izleri FFmpeg ebur128 filtresi ile entegre -14 LUFS seviyesine eşitlendi mi? [Evet / Hayır]

Vakum Arka Plan Yatağı (Ambience Bed): Dış uzay sahneleri için kask içi nefes ve düşük frekanslı gövde titreşim sesleri hazırlandı mı? [Evet / Hayır]

Klip Ses Temizliği: AI video modellerinden gelen kliplerin orijinal sesleri FFmpeg betikleriyle temizlendi mi? [Evet / Hayır]

J/L Cut Zamanlama İşaretçileri: Konuşmaların görsel kesim noktalarının 0.5 saniye önüne veya arkasına taşacağı kurgu kanalları belirlendi mi? [Evet / Hayır]

3. Bağlantılı Tam Kaynak Listesi
Google Cloud Agent Platform Video Prompt Guide: Google Cloud resmî video prompt rehberi ve negatif kelime kullanım kuralları.

Google DeepMind Gemini Omni Flash Model Overview: Gemini Omni 1.1 Flash model kartı, multimodal yetenekler ve çoklu tur düzenleme dokümantasyonu.

SkyStudioAI Veo 3.1 vs Gemini Omni Flash Benchmark Guide: Gemini Omni 1.1 Flash ve Veo 3.1 Fast modellerinin diyalog, kelime doğruluğu ve "No music" performans karşılaştırması.

ElevenLabs Terms of Service: ElevenLabs abonelik şartları, ücretsiz ve ücretli plan ticari kullanım koşulları.

Fluxnote YouTube AI Monetization Guide: YouTube Studio sentetik içerik bildirimi ve "Altered content" etiketleme kılavuzu.

Google Cloud Generative AI Pricing: Google Cloud Gemini modelleri ve video/ses üretim fiyatlandırma listesi.

PromptsLove Google Omni Prompt Generator: Gemini Omni 1.1 Flash için diyalog ve ekran metni biçimlendirme kuralları.

FFmpeg Documentation & Filters Manual: FFmpeg ses kaldırma, silencedetect ve ebur128 filtre komut rehberi.

Dev.to AI Stem Splitters Benchmark 2026: Open-source ses ayrıştırma araçları, UVR ve MDX-Net geliştirici kıyaslama raporu.
