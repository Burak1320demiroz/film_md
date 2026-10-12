# 🔬 03 — BEŞ KILAVUZ İÇİN BEŞ DERİN ARAŞTIRMA PROMPTU (07.10.2026)

> **Durum:** ✅ KOŞULDU — 07.10.2026. Ham: `ham/06_KUSUR_KAYNAGI_HAM.md` · `07_HAKEM_DOGRULAMA_HAM.md` · `08_FLOW_OLGULARI_HAM.md` · `09_GOSTERIM_HAM.md` · `10_IZLEYICI_VERISI_HAM.md` · süzme: `04_SUZME_20261007.md` (70 alt iddia doğrulandı: 52 ✅ · 11 ◐ · 3 ❌ · 4 ∅; indirmeler sahip onayı bekliyor).
>
> **Neden:** sahip 07.10.2026'da beş yeni kılavuz istedi ve önce dış araştırma yapılmasına karar verdi.
>
> | # | Kılavuz (taslak ad) | Doldurduğu açık |
> |:--:|---|---|
> | 1 | `PROMPT_HATA_ATLASI.md` | 698 bulguluk analiz yalnız oturum klasöründe duruyor; ortak katalog yok |
> | 2 | `QA_OKUMA_KILAVUZU.md` | QA yanılgısı %31; 🅐-🅓 sınıfları tek tanımlı değil; planlanan rapor-prompt karşılaştırma skill'i |
> | 3 | `FLOW_GERCEKLERI.md` | araç bilgisi raporlara dağılmış; "ölçülmüş" etiketlerin ~⅓'ü tutmadı (02_SUZME §A) |
> | 4 | `GOSTERIM_COZUMLERI.md` | ölümcül hataların ~%45'i neyin gösterildiğinden; T arızalarının "nasıl"ı beş ajana dağılmış |
> | 5 | `IZLEYICI_VERISI.md` | 225 video yayında, hiçbirinin izleyici verisi ölçülmedi |
>
> **Bu araştırmalar kılavuzu yazmaz.** Kılavuz, depo kanıtı ve süzülmüş dış kaynakla yazılır. 1 ve 2 numaranın asıl kaynağı deponun kendi analizidir; dış araştırma bunlara yalnız yöntem ve sınıflama getirir.
>
> **Nasıl koşulur:** her prompt **tek başına** çalışır.
> - Kod bloğunu kopyala ve derin araştırma aracına yapıştır. Başka hiçbir şey verme: depo, film adları ve raporlar verilmez.
> - **SINAMA SETİ araca verilmez.** Cevap geldiğinde süzmede kullanılır (01'deki kuralla aynı).
>
> **Sıra:** beşi bağımsız. ⭐ 3 numara (Flow) en ucuzu ve en acil olanı: bugün açık bir soruyu (4K, gerçek klip süresi, "Flow Music") kapatıyor.
>
> **01'de zaten sorulanlar burada tekrar edilmez:**
> - tek promptun okunuşu (çelişki, olumsuz cümle, etiket, atıf, uzunluk) → 01/2;
> - başlangıç karesi ve ilk-son kare → 01/1, 01/3;
> - Gemini'nin görme sınırı ve yanılgı oranları → 01/5.
>
> Yeni promptlar bunların **üstüne** kurulur: atıf yöntemi, sınıflama sözleşmesi, olgu dökümü, kurgu çözümü, izleyici verisi.

| # | konu | kapattığı yer |
|:--:|---|---|
| 1 | **KUSUR NEREDEN DOĞDU** — promptu modelden ayırma yöntemi, kusur taksonomileri, resmî kılavuz yasakları, atlas yöntemi | `PROMPT_HATA_ATLASI.md` · goruntu-yonetmeni · devamlilik · `film_dogrula.py` |
| 2 | **YAPAY ZEKÂ HAKEMİNİN BULGUSUNU DOĞRULAMA** — altın set, uyum, kalibrasyon, kök neden sınıflaması, zaman eşlemesi | `QA_OKUMA_KILAVUZU.md` · rapor-prompt karşılaştırma skill'i · klip-sec |
| 3 | **GOOGLE FLOW OLGU DÖKÜMÜ** — modeller, modlar, süre, çözünürlük, kredi, ses, görsel, müzik, değişim günlüğü | `FLOW_GERCEKLERI.md` · SMOKE_TEST · cekim-yaz iş emri · ses-muzik |
| 4 | **ZOR ANI KESMEYLE GÖSTERMEK** — el-nesne, kişi-kişi temas, tutulan nesne, iki benzer figür | `GOSTERIM_COZUMLERI.md` · yonetmen · teknik-danisman · goruntu-yonetmeni · kurgucu |
| 5 | **İZLEYİCİ VERİSİ** — YouTube Studio/Analytics ölçütleri, dışa aktarma, tutma eğrisini okuma, A/B kapak, tahmin ↔ gerçek | `IZLEYICI_VERISI.md` · paketleme §F10 · yayin |

---

# 1️⃣ KUSUR NEREDEN DOĞDU — promptu modelden ayırmak ve bir hata atlası kurmak

```
Metinden-videoya ve görselden-videoya üretim modellerinde (Google Veo 3.1 ve Ekim 2026 itibarıyla varsa sonrası, aynı ekosistemdeki Imagen ve Gemini görsel modelleri; karşılaştırma için Sora 2, Kling 2.x, Runway Gen-4, Luma Ray, Hailuo ve Wan) ekranda görülen bir kusurun PROMPTTAN mı yoksa MODELDEN mi doğduğunu ayırt etmenin yöntemlerini araştır: aynı promptla tekrar üretim, tek bir ifadeyi çıkarıp ya da ekleyip karşılaştırma ("en küçük çift" prompt), karşı-olgusal prompt, prompt yeniden yazıcısını (prompt enhancer / rewriter) kapatma, aynı promptu farklı modellerde koşma; bu yöntemlerin akademik değerlendirme çalışmalarında (prompt uyumu, kompozisyon, sayma, uzamsal ilişki, fizik ve el-nesne etkileşimi kıyaslamaları) ve uygulayıcı testlerinde nasıl kullanıldığı, tohum sabitlenemediğinde kaç denemeyle güvenilir sonuç verdiği — makale, kıyaslama belgesi, resmî belge ve yöntemi yazılı bağımsız testlerle; model, sürüm, tarih ve bağlantıyla.
Kusur taksonomilerini topla: yayımlanmış yapay video kusur sınıflamaları (görsel kalite, zamansal tutarlılık, fizik, el-nesne etkileşimi, kişi sayısı ve kimlik, istenmeyen yazı ve logo, prompt uyumu, başlangıç görseline sadakat) hangi sınıfı hangi nedene bağlıyor; promptla düzeltilebilen ve düzeltilemeyen sınıflar ayrılmış mı; bir sınıflamanın iki ayrı çalışmada aynı sonucu vermesi için tanımlar nasıl yazılmış (ölçüt, sınır vakası, örnek) ve sınıflayıcılar arası uyum ölçülmüş mü.
Resmî prompt kılavuzlarının yasaklarını karşılaştır: Google (Veo, Flow, Vertex AI, Gemini görsel), OpenAI (Sora), Runway, Kling ve Luma'nın kendi prompt rehberleri neyi açıkça yazmamayı söylüyor — olumsuz cümle ve olumsuz istem alanı, sahne ya da çekim numarası, başka klibe ya da önceki sahneye gönderme, film geneli ya da hikâye özeti, aynı promptta birbirini yalanlayan iki özellik (örneğin "gözenekleri görünen deri" ile "açıkta deri yok"), konuşma ya da replik tarifi, uzun teknik etiket listeleri, görsel ile video promptunun farklı başlangıç durumu anlatması — ve bunların her birinin hangi kusura yol açtığına dair ölçüm ya da belgelenmiş örnek var mı; yasakların hangisi birden çok üreticide ortak, hangisi tek üreticiye özgü.
Hata atlası yöntemini ayrıca sor: makine öğrenmesi hata analizinde, yazılım hata kataloglarında ve üretim kalitesinde (hata türü ve etkisi analizi) bir "hata atlası" ya da "arıza kataloğu" girdisinin nasıl yazıldığı (kalıp, belirti, kök neden, gerçek örnek, düzeltme, düzeltmenin doğrulandığı kanıt), atlasın zamanla kural listesine dönüşüp şişmesini önleyen pratikler (emeklilik, birleştirme, yalnız tekrar eden vakayı alma), bir kalıbın kaç bağımsız örnekten sonra "kanıtlı" sayıldığı ve atlasın kullanıcılarına (yazara mı denetçiye mi) nasıl sunulduğu.
Kritik kısıt: kullanım yeri, Google Flow web arayüzünde bir başlangıç görseli ve tek bir İngilizce hareket promptuyla üretilen 4-8 saniyelik fotogerçekçi uzay bilimkurgu klipleridir; karakterler basınç giysili ve kasklıdır; tohum sabitleme, model ince ayarı, LoRA, ControlNet ve API dışı araç YOKTUR ve her yeniden üretim kredi harcar — bu yüzden bu araçları gerektiren yöntemleri "hat dışı" diye işaretle ama silme, arayüzde ve az krediyle uygulanabilir olanları öne al; daha uzun ve daha ayrıntılı prompt öneren çözümleri ölçüm yoksa ÖNERİ say, çünkü kullanıcının kendi kayıtlarında prompt uzunluğu hatayı azaltmamıştır.
Çıktıyı üç tablo ve iki liste olarak ver: (a) ATIF YÖNTEMİ tablosu — yöntem, neyi ayırt eder, gereken deneme sayısı, kredi maliyeti, arayüzde uygulanabilir mi, kaynak ve etiket; (b) TAKSONOMİ tablosu — kusur sınıfı, tanım, sınır vakası, promptla düzeltilebilir mi, hangi çalışmada, sınıflayıcı uyumu varsa değeri, kaynak ve etiket; (c) YASAK tablosu — prompt kalıbı, hangi üreticinin kılavuzu yasaklıyor (birebir alıntıyla), yol açtığı kusur, ölçüm var mı, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda iki liste: (1) atlas girdisi için önerdiğin şablon (alanlar ve her alanın bir örnek cümlesi), (2) doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bunları açıklamalı

```
DEPONUN ÖLÇÜMÜ (06.10.2026 · 12 film · ~300 ham rapor · 698 tekil bulgu):
  gerçek kusurun %56'sı (248/443) prompta bağlandı (🅑 boşluk + 🅑+ davet) · %31 QA yanılgısı
  mekanik denetim, 50 film / 2.913 prompt:
    NEGATIVE bloğu promptun ortalama %40'ı
    "real skin pores" + "No bare skin" aynı promptta: 19 film, 784 prompt
    "Scene n of N": 37 film
    başka çekime atıf · film geneli ifade · konuşma tarifi · "IN FRAME: none" + her/his →
      bugün film_dogrula.py metin_kontrol() yakalıyor (eski 2.913 promptta kalibre edildi)
  görsel ↔ video çelişkisi: görsel işin BİTMİŞ hâlini gösteriyor, video hareketi istiyor → "hareket atlandı" 🔴
    THE_BRITTLE_EDGE S10 · THE_INWARD_FALL K19-K20 · THE_STILL_POINT S00/S08 · THE_LISTENING_WORLD S5
  tutanı olmayan nesne: THE_STOLEN_SKY S82 havada eldiven (3 mercek) · THE_SIGNAL_KEEPERS K23 küre
ÇELİŞEN İKİ SAYI: 05.10 analizi "ölümcül teknik hatanın ~%17'si prompt METNİNDEN, ~%45'i NEYİN gösterildiğinden" ·
  06.10 analizi "%56 prompt". Sınıflamalar farklı: biri hatanın doğduğu yere, öteki prompt boşluğu/davetine göre.
ESKİ ÖLÇÜM: prompt uzunluğu ↔ hata, Spearman +0,26 (47 film) — uzun prompt yardım etmedi (ARIZA Q06).
DEPO KURALI: hata kural olmaz (AGENTS §1 ④) — atlas örnek kataloğudur, yeni kapı değildir.
CEVAPTAN BEKLENEN: tek kredili arayüzde "prompt mu model mi" ayrımı hangi yöntemle, kaç denemeyle yapılır ·
  deponun yakaladığı kalıplardan hangileri resmî kılavuzlarda da yasak · atlas girdisi nasıl yazılır ki
  kural listesine dönmesin · %17 ile %56'yı yan yana koyabilecek tek taksonomi var mı.
```

---

# 2️⃣ YAPAY ZEKÂ HAKEMİNİN BULGUSUNU DOĞRULAMA — altın set, uyum, sınıflama, zaman eşlemesi

```
Yapay zekâ ile üretilmiş videoların başka bir çok kipli modelle ("hakem": Gemini, GPT, Claude) denetlendiği iş akışlarında, hakemin raporundaki bulguları gerçeğe karşı doğrulamanın ve kök nedene göre sınıflamanın yöntemlerini araştır: küçük bir altın etiket setiyle hakemin kesinlik ve duyarlılığını ölçmek (kaç video ve kaç bulgu yeterli, güven aralığı nasıl verilir), insan-hakem uyumu (Cohen kappa, Krippendorff alfa) ve bunun iki insan arasındaki uyumla karşılaştırılması, hakemin kendi verdiği güven derecesinin (emin / muhtemel / emin değil) gerçek doğrulukla örtüşmesi (kalibrasyon) ve kalibrasyonun nasıl ölçüldüğü, aynı videoya ait birden çok rapordaki tekrar eden bulguları birleştirme (zaman penceresi, nesnenin farklı adlarla anılması, kümeleme) — makale, kıyaslama, resmî değerlendirme kılavuzları ("LLM-as-a-judge", "VLM-as-a-judge", insan değerlendirme protokolleri) ve yöntemi yazılı uygulayıcı raporlarıyla; tarih ve bağlantıyla.
Kök neden sınıflamasını sök: bir bulguyu "üretim modelinin sapması", "prompt boşluğu (istenmediği için gelmedi)", "prompt daveti (promptun kendisi çağırdı)", "hakem yanılgısı" ve "eşlenemedi" gibi sınıflara ayırırken kullanılabilecek karar ağaçları ya da kök neden yöntemleri (beş neden, hata ağacı, hata türü ve etkisi analizi, olay sonrası değerlendirme şablonları), sınıflar arasındaki sınır vakalarının nasıl yazıldığı, iki analizin farklı sınıflama kullandığında sayılarının neden karşılaştırılamadığı ve tek bir sınıflama sözleşmesinin nasıl kurulup sürümlendiği, aynı bulguyu iki kişinin bağımsız sınıflayıp uyumu ölçmenin en ucuz yolu.
Zaman eşlemesini ayrıca sor: rapordaki zaman damgasını kurgu karar listesindeki (EDL, timeline) çekime çevirirken çıkan tipik hatalar (sıfırdan ya da birden sayma kayması, aralık verildiğinde başlangıcın mı bitişin mi alınacağı, kesme anına düşen bulgu, hakemin zaman damgası sapmasının tipik büyüklüğü, kare hızı ve dışa aktarma farkı) ve bunları önleyen pratikler; "geçersiz" sayılan raporlardan (eksik girdiyle, yanlış belgeyle, plansız ya da puan şişirmesiyle koşmuş) yine de güvenilir sinyal çıkarmanın belgelenmiş yolları ve bu sinyalin ağırlığının nasıl düşürüldüğü.
Kritik kısıt: kullanım yeri, 1-16 dakikalık fotogerçekçi uzay bilimkurgu kısa filmleridir; hakem Gemini uygulamasıdır ve raporlar zaman kodlu bir bulgu tablosu biçimindedir (numara · zaman · tür · ne görülüyor · güven); bulgular tek kişi tarafından elle ya da basit betiklerle sınıflanır; etiketleme platformu, ücretli değerlendirme aracı, ikinci bir insan değerlendirici ve model eğitimi YOKTUR — bunları gerektiren yöntemleri "hat dışı" diye işaretle ama silme, tek kişinin elle ya da betikle uygulayabileceklerini öne al; Gemini'nin video görme sınırlarını (kare örnekleme, uydurma oranı) yeniden araştırma, yalnız doğrulama ve sınıflama yöntemine odaklan.
Çıktıyı üç tablo ve iki liste olarak ver: (a) DOĞRULAMA tablosu — yöntem, neyi ölçer, gereken örnek sayısı, tek kişiyle uygulanabilir mi, kaynak ve etiket; (b) SINIFLAMA tablosu — sınıf, karar kuralı (evet/hayır sorusu), sınır vakası, en çok karıştırıldığı sınıf, kaynak ve etiket; (c) EŞLEME tablosu — hata türü (sayma kayması, aralık, kesme anı, zaman damgası sapması, nesne adı farkı, tekrar eden bulgu), belirtisi, önleme yolu, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, blog yazısını ve başka alanın (metin değerlendirme) bulgusunu videoya taşırken bunu açıkça yaz, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda iki liste: (1) tek kişilik bir karşılaştırma oturumu için adım adım protokol önerin (girdi, sıra, kayıt biçimi, durma koşulu), (2) doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
DEPONUN KAYDI:
  773 ham rapor · 2.049 🔴/🟠 satır · bu satırların %56'sı "geçersiz" sayılan raporlardan
  12 film · 698 tekil bulgu · sınıflar: 🅐 model sapması · 🅑 prompt boşluğu · 🅑+ prompt daveti · 🅒 QA yanıldı · 🅓 eşlenemedi
  QA yanılgısı %31 (214 bulgu) — örnekler: doğru fizik kusur sayıldı (GUNES_MEZARI 0,90 bar "vakum" · THE_FALLING_WORLD 0,30 g
    "floaty") · post'ta eklenen başlık kartı "yazı" 🔴 (14 film) · yanlış SPEC'le koşu (THE_LAST_TOW bölüm 1, 10 rapor)
  eski analiz betiğinde bulunan eşleme hataları (06.10.2026, düzeltilmedi, eski hat):
    sahne numarası sıfırdan sayılınca bir kayma · zaman aralığında bitişin alınması ·
    bir filmde dosya adından bölüm numarasının yanlış okunması · alt klasörlerin hiç okunmaması
  nesne adı farkı: rover → "buggy" · gümüş bant → "duct tape" (BILINEN_TUZAKLAR §D)
  iki analiz, iki sınıflama: 05.10 "%17 prompt metni / %45 neyin gösterildiği" ↔ 06.10 "%56 prompt"
YENİ HAT: ortak bulgu tablosu "# · time · type · what · confidence (SURE/LIKELY/UNSURE)" ·
  zaman → çekim: kurgu.py liste --zaman · kesme listesi: kurgu.py liste --kesmeler ·
  planlanan skill: QA çıktısı → zaman → çekim → o çekimin promptu → 🅐/🅑/🅑+/🅒/🅓 → NOTLAR.md
CEVAPTAN BEKLENEN: tek kişi için en küçük anlamlı altın set · SURE/LIKELY/UNSURE kalibrasyonu nasıl ölçülür ·
  beş sınıfın evet/hayır karar ağacı ve sınır vakaları · geçersiz rapordan sinyal almanın kuralı ·
  zaman eşleme hatalarının tam listesi (deponun bulduğu dördünü kapsıyor mu).
```

---

# 3️⃣ GOOGLE FLOW OLGU DÖKÜMÜ — yalnız resmî kaynak, Ekim 2026

```
Google Flow'un (labs.google/flow) Ekim 2026 itibarıyla güncel hâlini yalnız resmî kaynaklardan (Flow yardım merkezi ve SSS, Google ve Google DeepMind blogları, Veo ve görsel model kartları, Vertex AI ve Gemini API belgeleri, Google AI plan ve fiyat sayfaları, sürüm notları) çıkararak bir olgu dökümü hazırla: kullanılabilen video modelleri ve sürüm adları (Veo 3.1 Lite / Fast / Quality ve varsa sonrası), modlar (metinden video, karelerden video, malzemelerden / referanstan video, uzatma, sahne kurucu ve varsa diğerleri) ve her modun hangi modelde açık olduğu, klip süresi seçenekleri, kare hızı, çözünürlük ve büyütme seçenekleri (720p, 1080p, 4K — Flow arayüzünde mi yalnız API'de mi, hangi sürede, ek kredi ister mi), en-boy oranları (16:9, 9:16), başlangıç ve bitiş karesi desteği, referans görsel sayısı ve türleri, ses üretimi ve sessiz çıktı ayarı, kredi maliyeti ve plan kotaları, görünür filigran ve SynthID, indirme biçimleri, dosyaların saklanma süresi, ticari kullanım koşulları, içerik politikası ve reddedilen istek türleri; her satır için resmî sayfanın birebir alıntısı, bağlantısı ve sayfanın görülme tarihi.
Görsel tarafı ayrıca sor: Flow içinde ya da aynı Google hesabıyla kullanılabilen görsel üretim ve düzenleme modelleri (Imagen, Gemini görsel modelleri ve sürüm adları), çözünürlükleri ve en-boy oranları, referans görselle düzenleme ve kimlik koruma özellikleri, Flow'a başlangıç karesi olarak verilen görselin çözünürlüğü ya da en-boyu videodan farklı olduğunda resmî belgenin ne dediği.
Müzik ve sesi ayrıca sor: Google'ın müzik üretim araçları (Flow içinde ya da ayrı ürün: Lyria, MusicFX, Music AI Sandbox, YouTube içindeki araçlar ya da güncel adı ne ise) bugün var mı, nereden ve hangi planla erişiliyor, çıktı biçimi ve süresi, ticari kullanım ve saklama koşulları; "Flow Music" adında resmî bir Google ürünü var mı, yoksa yok mu — yoksa bunu açıkça yaz.
Değişimi ayrıca sor: Flow ve Veo'nun özellik ve fiyat değişikliklerini hangi resmî sayfalar duyuruyor (sürüm notu, değişiklik günlüğü, blog), son on iki ayda hangi değişiklikler olmuş (süre, kredi, mod, model adı, çözünürlük), birbiriyle çelişen resmî sayfalar var mı (örneğin aynı model için farklı süre) ve hangisi daha yeni.
Kritik kısıt: bu bir olgu dökümüdür, kılavuz ya da öneri listesi değildir; kullanım yeri tek kişinin Google Flow web arayüzünde ücretli bir planla fotogerçekçi uzay bilimkurgu klipleri üretmesidir; API yalnız karşılaştırma için anılır — API'ye özgü bir özelliği Flow'da varmış gibi yazma, ikisini ayrı sütunda göster; üçüncü taraf blog, forum ve video kaynaklarını yalnız UYGULAMA etiketiyle ve resmî kaynakla çeliştiği yerde ayrıca işaretleyerek kullan; bölgeye ya da plana göre değişen özellikleri ayrıca belirt.
Çıktıyı dört tablo ve iki liste olarak ver: (a) VİDEO tablosu — özellik, Flow'daki değer, API'deki değer, model ve sürüm, resmî alıntı, bağlantı, görülme tarihi, etiket; (b) GÖRSEL tablosu — aynı sütunlar; (c) MÜZİK VE SES tablosu — araç, erişim, plan, çıktı, ticari kullanım, saklama, alıntı, bağlantı, etiket; (d) DEĞİŞİM tablosu — tarih, ne değişti, önceki değer, yeni değer, kaynak; etiketler RESMİ (resmî Google sayfasında birebir alıntıyla) · UYGULAMA (üçüncü taraf ya da kullanıcı raporu) · BİLİNMİYOR (resmî kaynakta yok) olsun, RESMİ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı RESMİ yazma, iki resmî sayfa çelişiyorsa ikisini de alıntıla ve tarihlerini yaz; sonunda iki liste: (1) yalnız kullanıcının kendi denemesiyle ölçülebilecek açık sorular (gerçek klip süresi, kare hızı, dışa aktarılan dosyanın çözünürlüğü, sessiz ayarının etkisi), (2) bağlantılı tam kaynak listesi — belgede olmayan model adı, sayı ya da fiyat uydurma.
```

### 🧪 SINAMA SETİ

```
DOĞRULANMIŞ (02_SUZME §A, 06.10.2026):
  Flow Veo klibi 4/6/8 s · ilk+son kare Lite, Fast, Quality ve Omni Flash 1.1'de · kredi Lite 10 · Fast 20 · Quality 100 ·
  "Return silent videos" ayarı var ("all video generations are silent"; üretimde mi sonra mı atıldığı yazmıyor) ·
  24 fps ve 1080p/4K yalnız API belgesinde, 1080p/4K yalnız 8 s · iki Flow sayfası Quality süresinde çelişiyor ·
  Gemini API 1 fps varsayılan, videoMetadata fps var, Gemini uygulamasında ayar yok
DEPONUN DOĞRULANMAMIŞ VARSAYIMLARI:
  eski hat "aracın verdiği 8/10 s klip" (10 s resmî kaynakta yok) ·
  ses-muzik skill'i "Flow Music'te üretim; ücretli plan gerekir; dosyalar 14 gün içinde silinebilir" ·
  FILM.md künyesi KLIP_SURESI "ölçülmedi" · SMOKE_TEST P1-P8 koşulmadı
SAHİBİN SORUSU (07.10.2026): "süre belirlemem gerekiyor mu, 4K diye"
CEVAPTAN BEKLENEN: 4K Flow arayüzünde var mı · "Flow Music" resmî bir ürün mü, adı ne · Quality süre çelişkisinin
  güncel cevabı · Omni Flash 1.1 hâlâ var mı · hangi satır yalnız kendi denememizle ölçülebilir (SMOKE_TEST'e gider).
```

---

# 4️⃣ ZOR ANI KESMEYLE GÖSTERMEK — temas, tutulan nesne, iki benzer figür

```
Yapay zekâ video modellerinin (Google Veo 3.1 ve Ekim 2026 itibarıyla varsa sonrası; karşılaştırma için Sora 2, Kling, Runway, Luma, Hailuo ve Wan) en çok bozduğu fiziksel anları araştır — el ile nesne teması (kavrama, takma, çevirme, kol çekme, kablo ya da konnektör takma), iki kişi arasındaki temas (tutma, itme, kask ya da omuz değmesi, birinin ötekinin donanımına dokunması), havada tutulan ya da taşınan nesne, ağır iş ve efor, benzer giyimli iki kişinin aynı karede olması, sıfır yerçekiminde süzülme: her birinin güncel modellerde ölçülmüş bozulma oranı ya da sıklığı ve bozulma biçimi (parmak kaynaşması, nesnenin elden ya da gövdeden geçmesi, üçüncü bir kişinin belirmesi, kimliğin iki kişi arasında karışması, tutanı olmayan nesne, eforsuz ağır iş), bozulmayı artıran koşullar (çekim süresi, kamera hareketi, temasın kadrajdaki büyüklüğü, temasın çekimin içinde başlaması ya da sürmesi, iki figürün örtüşmesi) — kıyaslama makaleleri (el-nesne etkileşimi, çok özneli üretim, fiziksel sağduyu), resmî belge ve yöntemi yazılı bağımsız testlerle; model, sürüm, tarih ve bağlantıyla.
Film zanaatinin cevabını topla: dublörlükte, tehlikeli ya da yapılamayan eylemlerde ve fiziksel temasta kullanılan klasik kurgu ve kadraj teknikleri — hareket üstünde kesme, ayrıntı (insert) çekimi, tepki çekimi, temas noktasını kadraj dışında ya da önde bir nesnenin arkasında bırakma, omuz üstü ve tekli çekim kapsaması, eylemin öncesini ve sonrasını gösterip anın kendisini atlama (eliptik kurgu), sesle tamamlanan temas, Kuleşov etkisi; bunların seyircinin olayı "gördüm" sanmasını sağladığına dair algı ve kurgu araştırmaları (olay sınırları, kurgu körlüğü, süreklilik kurgusu, kesmeden sonra bilginin okunma süresi), bir ayrıntı ya da tepki çekiminin okunabilmesi için en kısa süre.
Uygulamayı ayrıca sor: yapay zekâ ile film yapan ekiplerin ve stüdyoların bu anları nasıl sahnelediğine dair belgelenmiş yöntemler (çekim başına tek özne, karakterlere ayrı renk ya da işaret, temas anını iki çekime bölme, durum değişimini kesmeye koyma, sürekli temasın süresini kısa tutma, başlangıç görselinde temasın zaten kurulmuş olması) ve bu yöntemlerin sonuçları; gerçek uzay yürüyüşü görüntülerinin (ajansların kask kamerası ve dış kamera kayıtları) kadraj, ölçek ve süre alışkanlıkları ve bunların yapay görüntüyü inandırıcı kılmak için nasıl kullanılabildiği.
Kritik kısıt: kullanım yeri, Google Flow'da başlangıç görseli ve hareket promptuyla üretilen 4-8 saniyelik fotogerçekçi uzay bilimkurgu klipleridir; karakterler basınç giysili ve kasklıdır, yüz yalnız vizörün ardından görünür; kurguda yalnız kesme, kırpma ve ses miksi vardır; VFX kompoziti, rotoskop, kare rötuşu, hareket yakalama, ara kare üretimi ve hız rampası YOKTUR — bu araçları gerektiren çözümleri "hat dışı" diye işaretle ama silme, kadraj, kesme ve sesle uygulanabilenleri öne al; "promptta temas cümlesini daha ayrıntılı yaz" tipi çözümleri ölçüm yoksa ÖNERİ say, çünkü kullanıcının kendi kayıtlarında ayrıntılı temas cümlesi bozulmayı önlememiştir.
Çıktıyı üç tablo ve iki liste olarak ver: (a) BOZULMA tablosu — an türü, ölçülmüş oran ya da sıklık, bozulma biçimi, artıran koşul, model ve sürüm, kaynak ve etiket; (b) ÇÖZÜM tablosu — an türü, kadraj çözümü, kurgu çözümü, ses çözümü, seyircinin anı okuduğuna dair kanıt, en kısa okunur süre, kaynak ve etiket; (c) UYGULAMA tablosu — ekip ya da yapım, kullandığı yöntem, sonuç, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge, hakemli çalışma ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu, yapım röportajı) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, film kuramı kitaplarındaki genel ilkeyi ölçüm sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda iki liste: (1) her an türü için "önce → kesme → sonra" biçiminde en çok üç çekimlik örnek dizi, (2) doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
DEPONUN KAYDI:
  el-nesne kaynaşması 49 filmin 21'inde (ARIZA T01) · temas cümlesi 25 promptun 22'sinde yazılıyken 7 ölümcül hata
  ölümcül teknik hataların ~%45'i NEYİN gösterildiğinden, ~%17'si prompt metninden (05.10.2026)
  vakalar: THE_LAST_GATE 00:51 eldivenler kablo konnektörünün içine geçiyor · 01:02 ayaktaki astronotun eli oturanın
    omuz kemerinden geçiyor 🔴 · 02:43 kol mili eldivenin avucundan geçiyor · 01:14 kapsül egzozu vakumda duman gibi ·
    THE_SECOND_SHIP S30 üçüncü beyaz figür beliriyor · THE_STOLEN_SKY S82 tutanı olmayan eldiven ·
    THE_SIGNAL_KEEPERS K23 hayali kavrama · THE_STATIC_VEIL 1:13 vakumda kıvılcımdan duman ve pus
  ARIZA_LISTESI kapanma yeri: el-nesne → KADRAJ / KURGU ("cümle yazmak tutmadı") · BILINEN_TUZAKLAR §B
YAZILMAKTA OLAN FİLM (HELMET_TO_HELMET, 07.10.2026) — kasklı iki kişi, kask kaska ve kask-çelik teması:
  öncesi → kesme → sonrası · sürekli temas ≤3 s · dinleyenin tekli çekimi, öteki yalnız flu kask kenarı ·
  kamera boş taraftan ¾ önde · iki giysiye farklı renk omuz bandı ve eldiven · kişi-kişi temas iki olaya indirildi ·
  çanta tutuşu ≤2 s sabit insert · durum değişimi (kanca, kol) kesmede
CEVAPTAN BEKLENEN: bu kalıpların hangisi algı ya da kurgu araştırmasıyla destekli, hangisi yalnız uygulama ·
  insert ve tepki çekimi için en kısa okunur süre · iki benzer figürde kimlik karışmasını en çok ne azaltır ·
  4-8 s klipte temas çekim içinde başlarsa bozulma gerçekten artıyor mu.
```

---

# 5️⃣ İZLEYİCİ VERİSİ — YouTube'dan ne alınır, nasıl okunur, tahminle nasıl kıyaslanır

```
YouTube Studio ve YouTube Analytics API'nin Ekim 2026 itibarıyla güncel hâliyle, uzun biçimli (1-16 dakika) kısa film yayımlayan bir kanalın izleyici verisini toplamanın ve okumanın yolunu araştır: gösterim ve gösterim tıklama oranı, ortalama izleme süresi, ortalama izlenme yüzdesi, izleyici tutma eğrisi (mutlak ve göreli tutma, "benzer videolara göre" karşılaştırması), "kilit anlar" (giriş, sıçrama, düşüş, en çok tekrar izlenen bölüm) ve bunların resmî tanımları; tutma verisinin hangi çözünürlükte (eğri noktası sayısı ya da saniye aralığı) ve hangi izlenme sayısından sonra gösterildiği; Studio'dan dışa aktarma (gelişmiş mod, CSV) ve API'deki karşılığı (rapor türü, boyut ve ölçüt adları — örneğin geçen video süresi oranına göre izleyici izleme oranı ve göreli tutma performansı), API'nin izin ve kota koşulları; kapak ve başlık A/B testi özelliğinin ("Test ve karşılaştır") nasıl çalıştığı, kazananı hangi ölçütle seçtiği ve ne kadar gösterim ya da süre gerektirdiği; fotogerçekçi yapay zekâ ya da değiştirilmiş içerik bildirimi etiketinin dağıtıma, gösterime ve tıklamaya etkisine dair resmî açıklama ya da ölçüm — resmî YouTube yardım sayfaları, YouTube blogu ve Creator Insider, API belgeleri ve yöntemi yazılı bağımsız analizlerle; tarih ve bağlantıyla.
Okumayı ayrıca sor: tutma eğrisindeki bir düşüşün içerikten mi (sahne, ritim, anlatının kopması, ses) yoksa dış etkenden mi (trafik kaynağı karışımı, öneri ya da arama, cihaz, ilk 48 saatteki kitle, yerleşik oynatıcı) geldiğini ayırmanın yolları; tek bir videonun verisinin neden kural sayılamayacağı ve kaç video, kaç izlenmeden sonra videolar arası karşılaştırmanın anlam kazandığı; kısa film, bilimkurgu ve yapay zekâ ile üretilmiş film kanalları için yayımlanmış tutma ve tıklama oranı aralıkları (yalnız yöntemi ve örneklemi yazılı kaynaklar); yaratıcıların yayın sonrası değerlendirme yöntemleri ve bunların ne kadarının ölçümle doğrulandığı.
Bağlantıyı ayrıca sor: yayın öncesi tahminlerin (yapay zekâ modeline videoyu izletip "nerede kafan karıştı, nerede bırakırdın" diye sormak, hikâyeyi bilmeyen birkaç kişiye ön gösterim, kapak testi) yayın sonrası gerçek tutma verisiyle karşılaştırıldığı çalışmalar ya da uygulamalar; ön gösterim ve test izleyicisinin bırakma anını gerçek izleyiciye göre ne kadar iyi tahmin ettiği ve bu karşılaştırmanın nasıl kayda geçirilebileceği.
Kritik kısıt: kanal tek kişilik, 16:9 uzay bilimkurgu kısa filmleri ve dikey kesimler yayımlıyor; yüzlerce video yayında ama hiçbirinin verisi düzenli kaydedilmemiş; veri sahibin elle dışa aktarmasıyla ya da basit bir betikle API'den alınır; ücretli analiz aracı, üçüncü taraf tarayıcı eklentisi ve reklam bütçesi YOKTUR — bunları gerektiren yöntemleri "hat dışı" diye işaretle ama silme; YouTube'un öneri algoritması hakkında resmî kaynağı olmayan iddiaları ÖLÇÜLMÜŞ sayma; Shorts ile uzun video ölçütlerinin farklı olduğu yerleri ayrı satırda göster.
Çıktıyı dört tablo ve iki liste olarak ver: (a) ÖLÇÜT tablosu — ölçüt, resmî tanım (birebir alıntı), Studio'da nerede, API'de rapor/boyut/ölçüt adı, en düşük veri eşiği, uzun video / Shorts farkı, kaynak ve etiket; (b) DIŞA AKTARMA tablosu — veri, Studio adımları, API çağrısı, dosya biçimi, kaynak ve etiket; (c) OKUMA tablosu — düşüş ya da sıçrama türü, olası iç neden, olası dış neden, ayırt etme yöntemi, kaynak ve etiket; (d) KIYAS tablosu — içerik türü, ölçüt, aralık, örneklem ve yöntem, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi ve örneklemi yazılı bağımsız ölçüm) · UYGULAMA (yaratıcı ya da danışman raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, örneklemi belirsiz "ortalama tutma oranı" iddialarını ölçüm sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda iki liste: (1) film başına tek satırlık bir kayıt şablonu önerisi (hangi sütunlar, hangi günde alınır: 48 saat, 7 gün, 28 gün), (2) doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan ölçüt adı, eşik ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN KAYDI:
  225 video yayında (apexaic/DIS_SAYILAR.md §1) · deponun performans tablosu boş · hiçbir filmin tutma verisi ölçülmedi
  kanalın en iyi iki sonucu sessiz başlıklıydı (KANAL_KIMLIGI §3) · aynı hafta 7 yükleme birbirini kaldırmadı
  YouTube'da yapay zekâ bildirimini sahip kendisi yapar (06.10.2026)
YENİ HAT F10 (paketleme): düşüş saniyesi → kurgu.py liste --zaman → çekim → NOTLAR.md satırı ·
  "tek filmin verisi kural olmaz; iki filmde tekrar ederse sahibe sorulur"
YAYIN ÖNCESİ TAHMİN (bugün var, hiç kıyaslanmadı): ANLATIM_TESTI (Gemini, plansız, "where would you stop") ·
  IZLEME_FORMU (sahip + ≥2 dış izleyici) · izleyici ajanı (metin, kare ve kapak modları)
CEVAPTAN BEKLENEN: Studio'dan hangi dosya hangi ölçütle alınmalı · tutma eğrisini çekime çevirmeye yetecek çözünürlük
  var mı (16 dk filmde bir eğri noktası kaç saniye) · A/B kapak testi kaç gösterim ister · anlatı testi ile gerçek
  bırakma noktası nasıl kıyaslanır · film başına kayıt satırı hangi günlerde alınır.
```

---

## 📥 SONUÇ GELDİĞİNDE — kayıt zinciri

1. **Kaydet.** Ham cevap olduğu gibi `ham/06_KUSUR_KAYNAGI_HAM.md` · `07_HAKEM_DOGRULAMA_HAM.md` · `08_FLOW_OLGULARI_HAM.md` · `09_GOSTERIM_HAM.md` · `10_IZLEYICI_VERISI_HAM.md` adlarıyla yazılır. Düzenlenmez.
2. **Süz (ana ajan) → `04_SUZME_<tarih>.md`.**
   - Her ÖLÇÜLMÜŞ ya da RESMİ satır için alıntı ve bağlantı aranır; bulunamazsa satır UYGULAMA'ya iner.
   - Satırlar o promptun SINAMA SETİ'ne karşı okunur: depo vakasını açıklayan → KABUL · çelişen → RED + gerekçe · ilgisiz → NOT.
   - 01'in süzmesinde 16 iddianın yalnız 8'inin alıntısı sayfada çıktı (02_SUZME §A). Etiket, alıntı ve bağlantıyla doğrulanmadan hiçbir sayı kılavuza girmez.
3. **Kılavuzu yaz (sahip onayıyla).**
   - Her kılavuz `uretim_hatti/<AD>.md`, tek sayfa (≤150-200 satır) olur.
   - Kuraldan çok örnek içerir; her girdi bir depo kanıtına ya da süzülmüş dış kaynağa bağlanır.
   - Okuyacak ajanlar `AJAN_GOREVLERI.md` AJAN HARİTASI'na eklenir.
   - 3 numara bir olgu sayfasıdır, kılavuz değil: ajanlar araç bilgisini yalnız oradan alır.
4. **Depo kanıtı önce.**
   - 1 ve 2 numaranın asıl kaynağı 06.10.2026'daki 12 filmlik analizdir. Bu analiz yalnız oturum klasöründe duruyor.
   - Kılavuz yazılmadan önce analiz metni (yalnız metin) `ARASTIRMA/` altına alınır. Bu sahip kararıdır.
5. **Kural değil.** Atlas ve gösterim kataloğu yeni kapı açmaz (AGENTS §1 ④). Mekanik kontrole dönüşecek bir kalıp önce `film_dogrula.py`'de eski promptlarla kalibre edilir.
6. **Durum satırı:** bu dosyanın başındaki satır ✅ KOŞULDU + tarih + ham dosya yollarıyla güncellenir.
