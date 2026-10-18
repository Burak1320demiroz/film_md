# 🔬 17 — AJAN SİSTEMİ: YENİDEN DÜZENLEMEDEN ÖNCE DÖRT DERİN ARAŞTIRMA PROMPTU (16.10.2026)

> **Durum:** ⏳ KOŞULMADI. Cevaplar `ham/34…37_*_HAM.md`'ye birebir girer → süzme `18_SUZME_<tarih>.md` → güncellemeler sahip onayıyla.
> **16.10.2026 akşam:** sahip "araştırma kalsın şimdilik, sen hazırla direkt yeni güncellemeyi" dedi. Güncelleme araştırmasız yapıldı
> (`AGENTS.md` §0 HAT v2 · §1 ⑨ · §1b · §2 · §2b). Bu promptlar koşulursa süzme o güncellemeyi sınar: KABUL olanlar kalır, RED olanlar
> sahibe geri alma önerisi olarak gider.
>
> **Neden:** Üç kaynak aynı yeri gösteriyor:
> - `16_QA_PROMPT_DERSLERI_20261016.md`: 5 film, 269 bulgu. Gerçek kusurun %71'i prompta bağlı; yazılı kurallar 5/5 filmde uygulanmadı.
> - `11_SUZME_20261016.md` §B: ajan çağrısı sonucu belirlemedi; üretim ve montaj hattın dışında yapıldı.
> - Sahibin getirdiği dış eleştiri (16.10.2026): "hikâye ve prompt hazırlığı uzun, üretim → seçim → kurgu bağı zayıf; Fable teslimi sahiplenmeli, kadro 1 + 6 role insin".
>
> Sahip 16.10.2026'da "yeni eklemeleri yapmadan önce 4 tane derin araştırma promptu hazırla, sonra güncellemeleri yapalım" dedi.
>
> **Hedef ürünler** (her prompt bir güncellemeyi besler):
>
> | # | konu | beslediği güncelleme | depodaki kanıt | okuyan |
> |:--:|---|---|---|---|
> | 1 | **AJAN KADROSU VE ORKESTRASYON:** kaç ajan, hangi roller, yazar ↔ eleştirmen ayrımı, paralel mi sıralı mı | `AGENTS.md` kadro bölümü · `.claude/agents/*` birleştirme/askıya alma · `/yeni-film` akışı | 18 ajan; 50 çağrı → "Kopuk", 7 çağrı → anlaşıldı · paralel gruplar arası kelime kayması (G03 ↔ G04) · F7-F8 ajanları hiç çağrılmadı | Fable · sahip |
> | 2 | **ÜRETİM KAYDI VE MEDYA ALIMI:** hangi referans, hangi deneme, hangi aralık; durum takibi; medyanın hatta girmesi | `NOTLAR` DENEMELER şablonu · `DURUM.md` · `/medya-denetle` skill'i · `kareler.py`/`kurgu.py` alım komutu | `~/film_medya` 5/5 boş · DENEMELER 5/5 boş · DURUM F7'de kaldı · QA numaraları plan numarası değil | Fable · sahip · kurgucu |
> | 3 | **PİLOT, ANİMATİK VE KURGUCUNUN ERKEN ROLÜ** | F3 sonrası pilot fazı (11 §D K8) · kurgucunun F3 eleştirisi · `SMOKE_TEST.md`'nin yerine film başına küçük deney | SMOKE 19 maddenin 0'ı koşuldu · bir film 96 prompt yazıldıktan sonra 0 kare · kusurların 109/269'u başlangıç karesinde | yonetmen · kurgucu · Fable · sahip |
> | 4 | **KURAL TÜRLERİ, TALİMAT UYUMU VE MEKANİK DENETİM** | `AGENTS.md` kural sınıflaması · ajan dosyalarının sadeleşmesi · `film_dogrula` uyarıları · `ELESTIRI_PROTOKOLU` | yazılı kural 5/5 filmde çiğnendi (24/24 promptta yasak ses cümlesi) · ajan dosyaları tarihli eklerle büyüyor · değerlendirme raporlarında uydurma yüzdeler | Fable · tüm ajanlar · sahip |
>
> **Depoda bugün olan (tekrar sorulmaz):**
> - Ajan tanımları `.claude/agents/` (18) · akış `AGENTS.md` · `/yeni-film`.
> - `KABUL_LISTELERI.md` · `ELESTIRI_PROTOKOLU.md` · `QA_OKUMA_KILAVUZU.md` (sınıflama sözleşmesi v1.0) · `PROMPT_HATA_ATLASI.md`.
> - 16.10 kılavuzları: GPT_IMAGE_OMNI · REPLIK · KIMLIK · UZAY_FIZIGI · SECIM_VE_KURGU.
> - Araçlar `film_dogrula.py` · `kurgu.py` · `kareler.py`.
>
> **Nasıl koşulur:** 01-14 ile aynı kural.
> - Her prompt tek başına çalışır. Kod bloğunu derin araştırma aracına yapıştır, başka bir şey verme.
> - Depo, film adı ve kanal adı verilmez. **SINAMA SETİ araca verilmez**; cevap gelince süzmede kullanılır.
>
> **Sıra:** dördü bağımsız. Önerilen sıra:
> 1. ⭐ **2 numara.** Ucuz, hemen uygulanır ve diğer üçünün ölçümünü mümkün kılar. Kayıt olmadan hiçbir değişikliğin işe yarayıp yaramadığı bilinemez.
> 2. **4 numara.** Neyin kapı, neyin öneri olacağını belirler.
> 3. **1 ve 3 numara.**

---

# 1️⃣ AJAN KADROSU VE ORKESTRASYON — kaç ajan, hangi rol, nasıl bağlanır

```
Büyük dil modeli ajanlarından oluşan çok ajanlı sistemlerin yaratıcı ve çok adımlı üretim işlerinde nasıl kurulduğunu Ekim 2026 itibarıyla araştır. Kullanım yeri: tek bir insanın yaptığı yapay zekâ kısa film üretimi. Bir ana ajan (orkestra şefi) iş akışını yürütür ve faz kapılarını onaylar; uzman alt ajanlar hikâye, çekim listesi, görüntü promptu, ses, kurgu, kapak ve yayın metni yazar ya da bunları eleştirir. Ortam: Anthropic'in Claude Code aracı. Ana ajan alt ajanları başlatır; alt ajanlar kendi bağlamlarında çalışır, dosya okur/yazar ve başka ajan başlatamaz.
Dört bölüm var.
(A) KADRO BÜYÜKLÜĞÜ VE ROL BÖLÜMÜ: Ajan sayısı ile sonuç kalitesi arasındaki ilişkiye dair ölçülmüş bulgular nelerdir? Hangi koşulda ajan eklemek kaliteyi artırır, hangisinde yalnız maliyeti ve koordinasyon hatasını artırır? Şu kaynakları tara:
  - Anthropic'in çok ajanlı araştırma sistemi yazısı ve Claude Code alt ajan/skill/hook belgeleri.
  - Cognition'ın "çok ajan kurma" uyarısı.
  - Çok ajanlı sistemlerin neden başarısız olduğunu sınıflayan çalışmalar ("Why Do Multi-Agent LLM Systems Fail?" ve benzerleri).
  - MetaGPT, ChatDev, AutoGen, CAMEL gibi rol tabanlı çerçeveler.
  - "Daha çok ajan" ve örnekleme/oylama çalışmaları.
  Rollerin birleştirilmesi (ör. ses tasarımcısı, besteci ve kurgucunun tek "kurgu ve ses" rolünde toplanması) ile ayrı tutulması arasında kanıt var mı? Uzmanlığın ayrı ajandan mı, aynı ajana verilen ayrı kontrol listesinden mi geldiği konusunda ne biliniyor?
(B) YAZAR ↔ ELEŞTİRMEN: Aynı modelin kendi çıktısını eleştirmesi ile ayrı bağlamda çalışan bağımsız bir eleştirmen arasındaki farka dair ölçümler nelerdir? Şu literatürü tara: self-refine, "LLM'ler akıl yürütmeyi henüz kendi kendine düzeltemez" türü çalışmalar, eleştirmen modeller, tartışma (debate), LLM-as-judge güvenilirliği ve önyargıları. Eleştirinin işe yaraması için ne gerekiyor: kanıt (alıntı, zaman, konum), önem derecesi, en küçük düzeltme önerisi? Eleştiri turlarının kaçıncısından sonra verim düşüyor? Eleştirmenin, yazarın uymadığı açık bir kuralı kaçırma oranına dair veri var mı?
(C) PARALEL Mİ SIRALI MI, ORTAK DURUM: Birbirine bağımlı parçaların (aynı karakterin ardışık çekimleri, aynı nesnenin durum değişimi) farklı ajanlara paralel yazdırılmasının tutarlılığa etkisi nedir? Ortak durum için hangi düzenler kullanılıyor: ortak dosya ya da blackboard, tek doğruluk kaynağı, sözleşme (schema), yazımdan sonra birleştirme geçişi? Bağlam aktarımında bilgi kaybı nasıl ölçülüyor ve azaltılıyor? Ana ajanın "teslimi sahiplenmesi" (durum takibi, iş listesi, kaldığı yerden sürdürme) için önerilen yapılar nelerdir?
(D) SÜREÇ DENETİMİ VE MALİYET: Bir faz kapısında "zorunlu adımlar yapıldı mı, kabul edilen düzeltme gerçekten uygulandı mı" denetimi ayrı bir ajanla mı yapılmalı, yoksa deterministik bir betik ve dosya farkı (diff) ile mi? Çağrı bütçesi, model seçimi (büyük ve küçük modelin hangi rolde yettiği) ve bağlam boyutunun maliyet/kalite dengesi hakkında yayımlanmış veriler nelerdir?
Kritik kısıt: kullanım yeri GENEL bir ajan sistemi tasarımıdır, belirli bir filme ait değildir. Sistem hâlihazırda 1 ana ajan ve 18 alt ajandan oluşuyor; çoğu metin aşamasında çalışıyor. Üretim (görsel ve video) insan tarafından web arayüzlerinde yapılıyor; ajanlar videoyu izleyemiyor, yalnız çıkarılmış kareleri ve ölçümleri okuyabiliyor. Film başına ajan çağrısı bütçesi vardır. Kadro azaltma önerisi gelirse, hangi rolün ne kaybettireceğini de yaz.
Çıktıyı üç tablo ve üç liste olarak ver:
  (a) KADRO tablosu: düzen (tek ajan + araçlar, az sayıda geniş rol, çok sayıda dar rol, yazar + bağımsız eleştirmen, oylama), ne zaman işe yarıyor, bilinen başarısızlık biçimi, ölçülen etki, kaynak, etiket.
  (b) ELEŞTİRİ tablosu: eleştiri biçimi (öz eleştiri, bağımsız eleştirmen, tartışma, kontrol listeli eleştirmen, kanıt zorunlu eleştirmen), yakaladığı ve kaçırdığı, tur sayısı etkisi, kaynak, etiket.
  (c) ORTAK DURUM tablosu: düzen (ortak dosya, şema, birleştirme geçişi, sıralı yazım, kilit), çözdüğü tutarlılık sorunu, maliyeti, kaynak, etiket.
Etiketler: ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da şirket pratiği) · ÖNERİ (senin çıkarımın).
  - ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; veremiyorsan ÖLÇÜLMÜŞ yazma.
  - Aynı kaynağa dayanan iki iddiayı iki kanıt sayma.
  - Firma tanıtım yazısını ÖLÇÜLMÜŞ sayma.
Listeler:
  (1) Bir ajan rolünü "kalsın / birleşsin / askıya alınsın" diye ayırmak için en çok 8 soru, her biri evet/hayır.
  (2) Ana ajanın her faz kapısında tutması gereken en küçük durum kaydının alanları.
  (3) Bağlantılı tam kaynak listesi.
Belgede olmayan sayı, oran ya da araç özelliği uydurma.
```

### 🧪 SINAMA SETİ

```
KADRO (16.10.2026): 1 ana ajan (orkestra şefi, kapıları onaylar) + 18 alt ajan.
  - Model: 7 Opus, 11 Sonnet.
  - 14/18 ajan metin fazlarında (F1-F6) çalışıyor.
  - 3 ajan yalnız klip zinciri için var; zincirin dayandığı araç özelliği hiç ölçülmedi.
  - 6 ajan hem yazar hem eleştirmen.
  - Çağrı bütçesi film başına 50.
SONUÇ ↔ ÇAĞRI: 2 dk film 50/50 çağrı (tam döngü) → izleyici "Kopuk". 4 dk film 7 çağrı → "baştan sona anlaşıldı".
  Anlaşılmayı belirleyen, diyaloğun filme girip girmemesiydi.
PARALEL YAZIM: 16 dk filmde görüntü promptları 8 grupta, paralel ajanlarla yazıldı.
  - Rozet konumu cümlesi G03'te 4 çekimde var, G04'te 0/12.
  - Rozet kaymalarının 4/4'ü G04'te.
  - 4 dk filmde yazı kilidi G01'de var, G02-G03'te düştü.
ELEŞTİRMEN KAÇIRMASI: devamlılık ajanı F5'te "rozet görsellerde tutarlı" dedi (konum cümlesinin yokluğunu çelişki saymadı).
  Bir filmde 24/24 video promptunda ajan dosyasının açıkça yasakladığı ses cümlesi var; F5 eleştirisi ve süreç denetçisi geçirdi.
F7-F8: seçim, kurgu, kare denetimi ajanlarının hiçbiri 4 üretilmiş filmde çağrılmadı; montaj hattın dışında yapıldı.
DIŞ ELEŞTİRİ (sahibin getirdiği): 1 ana + 6 rol (hikâye · yönetmen · görsel üretim · kurgu ve ses · paketleme · bağımsız izleyici/QA).
  Bağımsız işler paralel, ortak bağlamlı işler sıralı.
CEVAPTAN BEKLENEN: ajan sayısı ↔ kalite ölçümü · bağımsız eleştirmenin öz eleştiriden üstünlüğüne dair veri ·
  paralel yazımda tutarlılık için düzen · süreç denetiminde betik ↔ ajan · rol birleştirmenin bedeli.
```

---

# 2️⃣ ÜRETİM KAYDI VE MEDYA ALIMI — hangi referans, hangi deneme, hangi aralık

```
Film, animasyon ve görsel efekt yapımlarında çekimlerin, denemelerin (take), sürümlerin ve kullanılan girdilerin nasıl kayda geçirildiğini, ve bunun tek kişilik yapay zekâ film üretimine nasıl küçültülebileceğini Ekim 2026 itibarıyla araştır.
Dört bölüm var.
(A) STÜDYO PRATİĞİ:
  - Üretim takip sistemlerinin veri modeli: ShotGrid/Flow Production Tracking, ftrack, Kitsu, CGWire ve benzerleri (proje → sekans → çekim → görev → sürüm/deneme).
  - Sürüm ve dosya adlandırma kuralları.
  - "Seçilen deneme" ve "kullanılan aralık" (in/out) kaydı.
  - Kurgu ile üretim arasındaki geri dönüş: EDL, OTIO (OpenTimelineIO), seçim listesi.
  - Script supervisor'ın süreklilik defteri. Her çekimde hangi elde ne olduğu, kask/giysi durumu, kapı açık/kapalı, yara, ışık nasıl not edilir; bu "durum" bilgisi sonraki çekimlere nasıl taşınır.
(B) YAPAY ZEKÂ ÜRETİMİNDE KÖKEN KAYDI:
  - Bir görselin ya da videonun hangi promptla, hangi referans görsellerle, hangi model ve sürümle üretildiğini sonradan bulmanın yolları.
  - C2PA / İçerik Kimlik Bilgileri: OpenAI ve Google çıktılarında bulunuyor mu, hangi alanları taşıyor, yerelde nasıl okunur.
  - SynthID, EXIF/XMP meta verisi, web arayüzünden indirilen dosyanın adı ve tarihi.
  - ComfyUI gibi araçların prompt/iş akışını dosyaya gömmesi; buna karşılık web arayüzünde (ChatGPT, Gemini, Google Flow) bu bilginin kaybolması.
  - Web arayüzü kullanan tek kişi için en az zahmetli kayıt yolu: dosya adı kuralı, klasör düzeni, ekran görüntüsü, sohbet bağlantısı.
(C) MEDYA ALIMI VE OTOMATİK DÖKÜM:
  - Yerelde ffprobe, ffmpeg ve Python ile bir klasöre bırakılan klipleri otomatik tanıma: süre, çözünürlük, fps, ses var mı.
  - Plan çekimiyle eşleme.
  - Temas sayfası ve kare çıkarma, çekim sınırı tespiti (PySceneDetect), mükerrer/yakın kopya tespiti (algısal hash).
  - Hazır bir montajı (tek video dosyası) çekimlere geri bölme ve her parçayı plan çekimine eşleme: içerik tabanlı eşleme, kare benzerliği, kesme listesi çıkarma.
  - Bu işlerde yayımlanmış doğruluk değerleri ve bilinen hatalar.
(D) DURUM TAKİBİ VE KALDIĞI YERDEN SÜRDÜRME:
  - Çok adımlı bir üretimin "şu an hangi aşamada, ne eksik" durumunu dosyalardan otomatik çıkarmak için kullanılan yapılar: durum makinesi, görev listesi, makefile benzeri bağımlılık grafiği.
  - Kayıt tutma yükü ile tutarlılık arasındaki denge: hangi alanlar zorunlu, hangileri isteğe bağlı olmalı.
  - Kayıt boş kaldığında sistemin bunu nasıl fark edip uyarması gerektiği.
Kritik kısıt: kullanım yeri GENEL bir kayıt ve medya alımı kılavuzu ile bir yerel araçtır. Filmler 2-16 dakika, 12-96 çekim, her çekim 10 saniye; film başına 5-15 referans görseli ve çekim başına 1-4 deneme vardır. Üretimi tek kişi web arayüzlerinden yapar (ChatGPT/GPT Image ile kare, Gemini uygulaması ya da Google Flow ile video) ve kurguyu kendi programında yapar. Kayıtları okuyacak olan, videoyu izleyemeyen ama dosya, kare ve ölçüm okuyabilen bir yapay zekâ asistanıdır. Asıl sorun şudur: kayıt şablonu var ama hiç doldurulmuyor; üretim ve montaj sistemin klasörlerinin dışında yapılıyor; sonradan "bu karede hangi referans yüklenmişti" sorusu cevaplanamıyor. Bu yüzden yöntemin insan için ek iş yükünü dakika cinsinden tahmin et ve en az yükle en çok bilgiyi kurtaran sırayı ver.
Çıktıyı üç tablo ve üç liste olarak ver:
  (a) KAYIT ALANI tablosu: alan (çekim, deneme no, prompt sürümü, yüklenen referanslar, model/sürüm, kullanılan aralık, durum notu, ret nedeni), kim doldurur (insan / otomatik), zahmeti, ne zaman gerekli olur, stüdyo karşılığı, kaynak, etiket.
  (b) KÖKEN tablosu: araç ya da kaynak (C2PA, SynthID, EXIF/XMP, dosya adı, sohbet bağlantısı), hangi bilgiyi taşır, OpenAI/Google çıktısında var mı, yerelde okuma yolu, kaynak, etiket.
  (c) OTOMATİK ALIM tablosu: iş (klip tanıma, plan eşleme, montajı bölme, kopya tespiti, temas sayfası), araç ve tek satır yöntem, doğruluk ya da bilinen hata, kaynak, etiket.
Etiketler: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ.
  - ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver.
  - Aynı kaynağa dayanan iki iddia tek kanıttır.
  - Firma tanıtımı ÖLÇÜLMÜŞ değildir.
Listeler:
  (1) Tek kişi için zorunlu en çok 6 kayıt alanı, gerekçesiyle.
  (2) Medya klasöre bırakıldığında otomatik çalışacak alım adımlarının sırası.
  (3) Bağlantılı tam kaynak listesi.
Belgede olmayan meta veri alanı, araç özelliği ya da doğruluk oranı uydurma.
```

### 🧪 SINAMA SETİ

```
5 FİLMİN KAYIT DURUMU (16.10.2026):
  - ~/film_medya/<FILM>/{ref,kare,ham,ses,cikti} 5/5 boş.
  - NOTLAR DENEMELER/İŞARETLEME 5/5 yalnız şablon satırı (bir filmde tek satır "taslak montaj").
  - timeline.json 5/5 şablon; montaj hat dışında yapıldı, kurgu.py kullanılmadı.
  - DURUM.md 4 filmde F7'de kaldı (montaj ve QA bitmiş olduğu hâlde); FLOW_KREDI 0.
SONUÇ: QA × prompt analizinde 269 bulgunun hiçbiri için hangi denemenin ve hangi referansın kullanıldığı bilinmiyor.
  - Yüz/giysi kaymasında "model mi tutmadı, referans mı yüklenmedi" ayrılamadı (🅐 ↔ 🅑 koşullu).
  - Bir filmde prompt sürümü hiç belirlenemedi.
NUMARA KAYMASI:
  - Bir filmin montajında plan çekimi C05 yoktu; QA'nın C05… numaraları aslında C06….
    Değerlendirme raporu, NOTLAR ve 2 kılavuz yanlış numarayı kullandı.
  - Başka bir filmde QA numaraları Gemini'nin kendi kesme sayımıydı; 24 plan çekiminin 5'i montajda yoktu, sıra değişmişti.
  - İçerikle eşleme her filmde elle yapıldı.
HATTAKİ ARAÇ: kareler.py (cikar · kucult · kapak · kare · dikis SSIM/PSNR · kuyruk donma) · kurgu.py (kontrol · liste --zaman/--kesmeler ·
  taslak · yukseklik) · kurulu değil: PySceneDetect, OpenCV, scikit-image, Whisper.
REFERANS KURALI: <No>.<AD> adlandırma, promptta "Reference <No> (rol)" anahtarı, çekim başına ≤3 referans önerisi.
CEVAPTAN BEKLENEN: C2PA'nın ChatGPT/Gemini çıktılarında gerçekten bulunup bulunmadığı ve neyi taşıdığı · montajı çekimlere geri bölmenin
  güvenilir yolu · stüdyo deneme kaydının en küçük biçimi · kayıt yükünün dakika tahmini · boş kayıtta sistemin uyarı biçimi.
```

---

# 3️⃣ PİLOT, ANİMATİK VE KURGUCUNUN ERKEN ROLÜ — riskli anı önce üretmek

```
Film, animasyon ve oyun yapımında "en riskli parçayı önce dene" yaklaşımlarının yapay zekâ ile video üretimine nasıl uyarlanabileceğini Ekim 2026 itibarıyla araştır.
Dört bölüm var.
(A) ÖN GÖRSELLEŞTİRME VE ANİMATİK:
  - Previs, animatik ve storyboard'un üretim maliyetine ve yeniden çekim oranına etkisine dair yayımlanmış veriler.
  - Animasyon stüdyolarında kurgucunun hikâye makarası (story reel) aşamasındaki rolü.
  - Oyun yapımında dikey kesit (vertical slice) ve prototip.
  - "Teknik test çekimi" ve kamera/ışık testleri.
  - Bunların hangi riski erken yakaladığı ve maliyeti.
(B) KURGUCU ÇEKİMDEN ÖNCE: Kurgucunun ön hazırlıkta çekim listesini okuması nelere yarar?
  - Kapsama (coverage): tepki planı, insert, ara plan, kesme noktası.
  - Kurguda kurtarma payı.
  - Süre ve ritim tahmini.
  - Bir çekimin "tek başına iyi ama yanındakiyle çelişen" olma riskini önceden görmek.
  - Kurgucunun çekim listesinde baktığı somut sorular.
  - Sabit süreli (10 saniyelik) yapay zekâ klipleriyle kapsama planlaması: her sahnede kaç kurtarma planı gerekir, uzun ve durağan planlar izleyicide ne zaman sıkılma yaratır.
(C) YAPAY ZEKÂ VİDEOSUNDA PİLOT:
  - Görselden videoya modellerle (Google Veo / Gemini Omni, OpenAI Sora, Runway, Kling) çalışan yapımcıların, filmin tamamının promptlarını yazmadan önce az sayıda çekimi üretip denemesine dair pratikler.
  - Kaç çekimle pilot yapılır, hangi çekimler seçilir (en riskli an, açılış, iki karakterin aynı nesneyle teması, kimlik), neyin ölçüldüğü.
  - Pilot sonucuna göre plana nasıl geri dönüldüğü.
  - Deneme başına kullanılabilir klip oranı ve kredi maliyetine dair yayımlanmış ya da uygulayıcı verileri.
  - Pilotun "her filmde aynı uzun kontrol listesi"ne dönüşüp hiç koşulmaması riskine karşı ne yapılıyor: deneyi küçük ve filme özgü tutmak.
(D) DURMA KURALI: Bir çekim için kaç denemeden sonra yeniden üretim yerine kurgu çözümüne, plan değişikliğine ya da çekimi atmaya geçilmeli? Yayımlanmış ya da uygulayıcı karar kuralları nelerdir?
Kritik kısıt: kullanım yeri GENEL bir iş sırası tasarımıdır. Filmler 2-16 dakika, yatay, fotogerçekçi yapay zekâ bilimkurgu; çekim başına 10 saniye kuralı vardır (değiştirmeyi önerme; kanıt varsa ayrı satırda yaz). Karakterler çoğunlukla kasklı astronotlar. Üretim tek kişi tarafından web arayüzlerinde, kredi bütçesiyle yapılır. Bugünkü sıra: hikâye → tretman → çekim listesi → ses planı → bütün promptlar → kapak → üretim → kurgu. Yani ilk gerçek görüntü, metin işi bittikten sonra geliyor. Önerdiğin pilotun bu sıranın neresine gireceğini, kaç çekim ve ne kadar kredi/zaman gerektirdiğini açık yaz.
Çıktıyı üç tablo ve üç liste olarak ver:
  (a) ERKEN TEST tablosu: yöntem (previs, animatik, story reel, dikey kesit, test çekimi, yapay zekâ pilotu), yakaladığı risk, maliyeti, ölçülen etki, kaynak, etiket.
  (b) KURGUCU SORULARI tablosu: çekim listesinde bakılan soru, yakaladığı sorun, örnek, kaynak, etiket.
  (c) PİLOT tablosu: çekim türü (açılış, kimlik, temas, kalabalık/iki karakter, vakum fiziği, diyalog), neden pilot, ne ölçülür, başarı ölçütü, kaynak, etiket.
Etiketler: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ.
  - ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver.
  - Aynı kaynağa dayanan iki iddia tek kanıttır.
  - Firma tanıtımı ve sosyal medya iddiası ÖLÇÜLMÜŞ değildir.
Listeler:
  (1) 3 çekimlik pilotu seçmek için en çok 6 ölçüt.
  (2) Pilot sonrası "plana devam / planı değiştir / hikâyeyi değiştir" kararı için tek sayfalık karar ağacı.
  (3) Bağlantılı tam kaynak listesi.
Belgede olmayan maliyet, oran ya da araç özelliği uydurma.
```

### 🧪 SINAMA SETİ

```
SIRA VE MALİYET:
  - 2 dk film F1-F6 tam döngü: 50/50 ajan çağrısı, ilk kare F7'de.
  - 16 dk film: 96 çekimin promptu yazıldı (F5 kapandı), o anda 0 kare.
  - Üretimden sonra ikinci parçasında 4/5 koltuk "hatası" tasarlanmış ters açı çıktı, ama izleyici yine kafası karıştı.
DENEY LİSTESİ: SMOKE_TEST P1-P19 (zincir, 10 s yolu, referans anahtarı, panel sayfası, vuruş planı, model sesi …).
  19'unun hiçbiri koşulmadı; dört film bu deneyler olmadan üretildi.
QA × PROMPT (269 bulgu):
  - 109'u başlangıç karesinde doğdu, 55'i hareketle, 33'ü sesle, 17'si kurguda.
  - "QA yanıldı" sayılanların bir kısmı tasarımın gerçek izleyici bedeli; bunlar çekim listesi sorunu:
    · kıpırtısız bekleyen karakter "sahte"
    · 10 s boş kasa planı "kafa karıştırıcı"
    · kilitli dış plan "sıkıcı"
    · 4 dk filmde yanaşma dört plan sürüyor, tempo düşüyor
  - 2 dk filmde iki ardışık plan birbirini yalanladı; prompt bunu bizzat istiyordu (plan sorunu, seçim değil).
KURGUCU BUGÜN: yalnız F8'de yazar, F4'te müzik planını eleştirir; F3 çekim listesine bakmıyor; komut çalıştıramıyor.
11_SUZME K8 (sahibe soruldu, cevapsız): F3 kapanınca 3 çekimlik pilot; F4-F5 bundan sonra.
CEVAPTAN BEKLENEN: animatik/previs'in yeniden çekim oranına etkisine dair veri · yapay zekâ videosunda pilot pratiği ve kullanılabilir
  klip oranı · kurgucunun çekim listesinde sorduğu somut sorular · kaç denemeden sonra durulacağı.
```

---

# 4️⃣ KURAL TÜRLERİ, TALİMAT UYUMU VE MEKANİK DENETİM — yazılı kural neden uygulanmıyor

```
Büyük dil modeli ajanlarına verilen uzun talimat dosyalarındaki kuralların neden uygulanmadığını ve kuralların nasıl düzenlenip denetlenmesi gerektiğini Ekim 2026 itibarıyla araştır.
Dört bölüm var.
(A) TALİMAT UYUMU:
  - Talimat sayısı ve uzunluğu arttıkça uyumun düşmesine dair ölçümler: IFEval, çok kısıtlı talimat çalışmaları ("curse of instructions" ve benzerleri), "lost in the middle", sistem promptu uzunluğu.
  - Kuralın talimat dosyasındaki yerinin etkisi: başta, sonda, tarihli ek olarak.
  - Kuralın örnekle (iyi/kötü örnek) ya da gerekçeyle verilmesinin etkisi.
  - Anthropic'in ve OpenAI'ın talimat yazımı ve ajan tanımı için resmî önerileri (Claude Code alt ajan tanımları, CLAUDE.md, skills).
(B) KURAL TÜRLERİ: Bir üretim sistemindeki kuralları şu türlere ayırmanın yöntemleri ve yararı nedir?
  - Sahibin sözleşmesi (ör. "her çekim 10 saniye").
  - Doğrulanmış araç sınırı.
  - Ölçülmemiş hipotez.
  - Yaratıcı tercih (ör. "tam üç hashtag").
  Buna benzer ayrımlar: yazılım mühendisliğinde lint seviyeleri (error/warning/info), mimari karar kayıtları (ADR), havacılıkta zorunlu ve önerilen prosedür. Hangi tür kural "kapı" (geçmeden ilerlenmez) olmalı, hangisi uyarı ya da öneri? Kural emekliliği nasıl yapılır: süre, kanıt, gözden geçirme?
(C) KONTROL LİSTESİ VE MEKANİK DENETİM:
  - Kontrol listelerinin etkisine dair kanıt: cerrahi güvenlik kontrol listesi, havacılıkta READ-DO ↔ DO-CONFIRM, madde sayısı sınırları.
  - Yazılı bir kuralın üretilen metinde uygulanıp uygulanmadığını denetlemek için deterministik kontroller (regex, şema, zorunlu alan) ile LLM-as-judge karşılaştırması: doğruluk, yanlış alarm, maliyet, önyargı.
  - Prompt metinlerini "lint"lemek için kullanılan araçlar ve pratikler (prompt as code, prompt testleri, değerlendirme setleri).
  - Bir kontrolün "uyarı" olarak mı "ret" olarak mı çalışmasının uyuma etkisi; uyarı yorgunluğu.
(D) KANITLI ELEŞTİRİ VE RAPOR DÜRÜSTLÜĞÜ:
  - Yapay zekâ değerlendirme ve QA raporlarında uydurma sayılar (kaynaksız yüzdeler, "kök neden" tahminleri) nasıl önlenir: kaynak alıntısı zorunluluğu, yapılandırılmış çıktı, belirsizlik etiketi.
  - Bir bulgunun konum (zaman, çekim), kanıt (alıntı) ve en küçük düzeltmeyle yazılmasının yararına dair ölçümler.
  - Raporlarda "bulunamadı" ile "temiz" ayrımı.
Kritik kısıt: kullanım yeri GENEL bir kural düzeni ve denetim tasarımıdır. Sistem: bir ana ajan ve uzman alt ajanlar; her alt ajanın 40-130 satırlık Türkçe talimat dosyası var, yanında ortak kural dosyaları (bilinen tuzaklar, arıza listesi, kabul listeleri, eleştiri protokolü) ve her ajanın okuması gereken birkaç kılavuz bulunuyor. Sahibin kararları zamanla ajan dosyalarına tarihli ekler olarak giriyor ve dosyalar büyüyor. Bazı kurallar Python ile mekanik olarak denetleniyor, çoğu ajanın okuyup uygulamasına bırakılmış. Asıl sorun şudur: kural yazılı olduğu hâlde ajanın ürettiği metinde uygulanmıyor ve eleştirmen ajan da bunu yakalamıyor. Öneri "daha çok kural yaz" olmamalı; azaltma, sınıflama ve mekanikleştirme yönünde ölçülmüş kanıt ara.
Çıktıyı üç tablo ve üç liste olarak ver:
  (a) TALİMAT UYUMU tablosu: etken (kural sayısı, dosya uzunluğu, konum, örnek, gerekçe, tarihli ek), uyuma etkisi, model ve sürüm, kaynak, etiket.
  (b) KURAL TÜRÜ tablosu: tür, örnek, nasıl uygulanır (kapı / uyarı / öneri), nasıl emekli edilir, benzer alan (lint, ADR, havacılık), kaynak, etiket.
  (c) DENETİM tablosu: denetim yolu (regex/şema, zorunlu alan, LLM-as-judge, kontrol listeli eleştirmen, insan), neyi yakalar, doğruluk ve yanlış alarm, maliyet, kaynak, etiket.
Etiketler: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ.
  - ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver.
  - Aynı kaynağa dayanan iki iddia tek kanıttır.
  - Firma tanıtımı ÖLÇÜLMÜŞ değildir.
Listeler:
  (1) Bir ajan talimat dosyasını sadeleştirmek için en çok 8 adım.
  (2) Bir kuralın "kapı mı, uyarı mı, öneri mi" olacağına karar vermek için en çok 6 soru.
  (3) Bağlantılı tam kaynak listesi.
Belgede olmayan oran, eşik ya da model davranışı uydurma.
```

### 🧪 SINAMA SETİ

```
KURAL VAR, UYGULANMADI (16_QA_PROMPT_DERSLERI §C):
  - "Asimetrik işaret hangi taraftaysa yazılır · sayılabilir öğe rakamla" (ajan dosyası satır 38, 12.10): 5/5 filmde yetersiz;
    16 dk filmin G04 grubunda 0/12.
  - "Model sesi KAPALI filmde ses tarifi yazılmaz" (aynı dosya satır 65): bir filmde 24/24 video promptunda ses cümlesi.
    F5 eleştirmeni ve süreç denetçisi geçirdi.
  - "Son vuruş donmaz": 6 çekimde donuyor.
  - "Aynı promptta zıt istek yok": 5/5 filmde var.
  - Yazı kilidinin yazılı olduğu çekimlerde yazı bulgusu 0, yazılı olmayanlarda 7 (7/7 prompta bağlı).
  - Rozet konumu yazılı 4 çekimde kayma 0, yazılmayan 12'de 4.
DOSYALAR:
  - Ajan dosyaları 40-127 satır (toplam 1.265); "(12.10.2026, …)" biçiminde tarihli sahip ekleri birikiyor.
  - En uzun: görüntü yönetmeni 127 satır; kendi içinde çelişki var ("karede olanı yeniden tarif etme" ↔ "ortak görünüm cümlesi her video promptunda birebir").
KURAL TÜRLERİ KARIŞIK:
  - Sahip sözleşmesi (10 s, commit yalnız sahip, medya repoda değil).
  - Ölçülmemiş hipotez (panel sayfası, ≤4 zincir halkası, 10 s vuruş planı; deneyleri koşulmadı).
  - Yaratıcı tercih (tam 3 hashtag, tek kesintisiz müzik, replik bandı).
  - Hepsi aynı kabul listesinde kapı.
MEKANİK DENETİM BUGÜN: film_dogrula.py (biçim, 10 s, meta etiket, uzunluk ≤4.300, bazı yasak kelimeler). İşaret tarafı, ses cümlesi,
  ortak cümle içeriği denetlenmiyor.
RAPOR DÜRÜSTLÜĞÜ: QA değerlendirme raporlarında kaynaksız kök neden yüzdeleri (%40 / %35); "dış izleyici" satırları AI simülasyonu;
  promptlara bakılmadan yazılan iki kök neden çürüdü.
CEVAPTAN BEKLENEN: talimat sayısı/uzunluğu ↔ uyum ölçümü · regex ↔ LLM-as-judge karşılaştırması · kural türü ayrımının pratik
  karşılıkları · kontrol listesi madde sınırı · rapor uydurmasını azaltan biçim.
```

---

> **Cevap gelince:** her cevap `ham/34_AJAN_KADROSU_HAM.md` · `35_URETIM_KAYDI_HAM.md` · `36_PILOT_KURGUCU_HAM.md` · `37_KURAL_DENETIM_HAM.md`'ye birebir girer.
> Süzme `18_SUZME_<tarih>.md`: kaynak doğrulama → KABUL / RED / PROB / NOT / SAHİP.
> Güncellemeler süzmeden sonra ve sahip onayıyla yapılır.
> Yeni kural yalnız iki filmde kayıtlı kanıtla girer (AGENTS §1 ④).
