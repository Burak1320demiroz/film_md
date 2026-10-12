# 🔬 07 — İLK 30 SANİYE: GENEL KILAVUZ İÇİN BEŞ DERİN ARAŞTIRMA PROMPTU (12.10.2026)

> **Durum:** ✅ KOŞULDU — 12.10.2026. Ham: `ham/16_ILK30_OLCUM_ACILIS_HAM.md` · `17_ILK30_VAAT_TESLIM_HAM.md` · `18_ILK30_SOZSUZ_ACILIS_HAM.md` · `19_ILK30_YAPAY_ZEKA_ILK_IZLENIM_HAM.md` · `20_ILK30_ON_TEST_TESHIS_HAM.md` · süzme: `08_SUZME_20261012.md` · kılavuz: `uretim_hatti/ILK_30_SANIYE_KILAVUZU.md`.
>
> **Neden:** sahip 12.10.2026'da şunu dedi: "filmlerdeki ilk 30 saniye için bir araştırma yapalım … her filmde hook güçlü yapıp ekranda tutmak olmalı, amaç o." Ardından "5 araştırma promptu hazırla" ve "biz genel kılavuz için lazım" dedi.
>
> **Hedef ürün:** her yeni filme uygulanan tek bir genel kılavuz, taslak adıyla `uretim_hatti/ILK_30_SANIYE_KILAVUZU.md`. Kılavuz film adı taşımaz; her format (2 · 4 · 8 · 16 dk, dikey shorts) için geçerlidir. Senarist, yonetmen, goruntu-yonetmeni, ses-tasarimcisi, kapak-tasarimcisi, kurgucu ve izleyici ajanları onu okur. Mekanik kısmı `film_dogrula.py`'ye kontrol olarak iner.
>
> **Bu araştırmalar kılavuzu yazmaz.** Kılavuz, süzülmüş dış kaynak ve kanalın kendi tutma verisiyle yazılır. Her promptun cevabı kılavuzun bir bölümünü besler:
>
> | # | konu | kılavuzda doldurduğu bölüm | okuyan ajanlar |
> |:--:|---|---|---|
> | 1 | **ÖLÇÜLMÜŞ GERÇEKLER VE AÇILIŞ BİÇİMLERİ** — ilk 30 saniyede kayıp neye bağlı, hangi açılış biçimi ölçüldü | §1 Sayılar · §2 Açılış biçimleri ve saniye iskeleti | senarist · yonetmen · kurgucu |
> | 2 | **KAPAKTAKİ VAAT İLK 30 SANİYEDE** — tıklatan görüntü ne zaman, nasıl teslim edilir | §3 Vaat-teslim kuralı | kapak-tasarimcisi · yonetmen · yayin · senarist |
> | 3 | **SÖZSÜZ ANLAŞILAN AÇILIŞ** — anadili İngilizce olmayan izleyici: görüntü, yazı, altyazı, dublaj, ilk saniyelerin sesi | §4 Evrensel okunurluk · §5 İlk saniyelerin sesi | diyalog-yazari · ses-tasarimcisi · kurgucu · yayin |
> | 4 | **YAPAY ZEKÂ FİLMİNİN İLK İZLENİMİ** — kusur algısı, insan yüzü, güvenilir açılış çekimi, üretim önceliği | §6 Açılışın üretimi (çekim seçimi, deneme sayısı, kare kapısı) | goruntu-yonetmeni · teknik-danisman · devamlilik · cekim-yaz §F7 |
> | 5 | **AÇILIŞI SINAMAK VE OKUMAK** — emsal dökümü, yayından önce ön test, yayından sonra teşhis, filmden filme deney | §7 Ön test · §8 Yayın sonrası teşhis ve deney defteri | izleyici · paketleme §F10 · yayin |
>
> **Depoda bugün olan (kılavuzun çıkış noktası):**
> - Ajan kuralı H08 "yavaş açılış": ilk karede bir sorun ya da beklenmedik hareket (senarist, yonetmen).
> - Eski hattın `kilavuzlar_ve_sistem_dosyalari/HOOK_VE_ILK_SAHNE_KILAVUZU.md` dosyası (09.08.2026). Kendi §0'ı "hipotez, ölçülmüş sonuç değil" diyor. Donmuş hattın parçasıdır; okunur, düzenlenmez.
> - `05/2` izlenme süresinin bütününü sordu. `06_SUZME` ilk 30 saniye ilkelerini "uygulama düzeyi" bulup değişiklik yapmadı.
> - `03/5` tutma verisinin **nasıl ölçüleceğini** sordu (Studio, API). Buradaki 5 numara yalnız ilk 30 saniyenin **teşhisini** sorar.
> - **Yeni olan:** kanalın ilk gerçek "Giriş" verisi (sahibin Studio ekranı, 12.10.2026). Bu veri araca verilmez, süzmede kullanılır.
>
> **Nasıl koşulur:** 01, 03 ve 05'teki kuralla aynı.
> - Her prompt tek başına çalışır. Kod bloğunu derin araştırma aracına yapıştır, başka bir şey verme.
> - Depo, film adı ve kanal adı verilmez. Emsal kanal ve film adları dış bilgi olduğu için promptta kalır.
> - **SINAMA SETİ araca verilmez.** Cevap gelince süzmede kullanılır.
>
> **Sıra:** beşi bağımsız. ⭐ 1 numara önce koşulsun; kılavuzun iskeleti ondan çıkar. Sonra 2 ve 4 gelsin: kanalın iki filmi arasındaki farkın en güçlü iki adayı vaat teslimi ve açılış kusurudur.
>
> **Sahibin yapıştırdığı öneri metni** (12.10.2026, kaynağı belirtilmemiş bir model cevabı) araştırılacak iddialar listesidir, kanıt değildir. İddiaları her promptun SINAMA SETİ'nde ayrı satırda durur.

---

# 1️⃣ ÖLÇÜLMÜŞ GERÇEKLER VE AÇILIŞ BİÇİMLERİ — ilk 30 saniyede kayıp neye bağlı

```
YouTube'da yatay uzun videoların (2-16 dakika) ilk 30 saniyesindeki izleyici kaybını neyin belirlediğine dair Ekim 2026 itibarıyla ÖLÇÜLMÜŞ kanıtı araştır. Önce YouTube'un kendi kaynaklarını tara: YouTube Yardım'daki "kitleyi elde tutma" ve "önemli anlar" (giriş, sıçrama, düşüş) sayfaları, Creator Insider, YouTube Culture & Trends, Think with Google ve YouTube çalışanlarının kayıtlı açıklamaları. Bunlar "Giriş" (30. saniyede kalan oran) ölçütü hakkında ne söylüyor, hangi oranı "tipik" sayıyor, tipik aralığı kanalın kendi videolarıyla mı yoksa benzer videolarla mı kıyaslıyor? Trafik kaynağının (ana sayfa, önerilen videolar, arama, dış kaynak, oynatma listesi, bildirim, reklamla gösterim) ilk 30 saniye tutmasına etkisini ve ana sayfadaki sessiz otomatik önizlemenin (üzerine gelince ya da akışta oynatma) izlenme sayımına ve tutma eğrisinin başına nasıl yansıdığını sor. İlk 5, 10 ve 30 saniyedeki tipik düşüşün büyüklüğünü veren, örneklemi ve yöntemi yazılı bağımsız çalışmaları topla: analitik şirketleri, akademik çalışmalar, tutma eğrisini açıkça paylaşan yaratıcılar. Her biri için tarih, örneklem büyüklüğü, video uzunluğu, kategori ve bağlantı ver.
Açılış biçimlerinin etkisini ayrı ayrı sor ve her biri için ölçüm olup olmadığını açıkça yaz: (a) hareketin ortasından başlama (soğuk açılış, in medias res); (b) ileri sıçrama (doruktan 5-8 saniye, sonra "X saat önce"); (c) kurulum çekimiyle açılış (geniş manzara, mekân tanıtımı); (d) karakterin yüzü ya da bedeniyle açılış; (e) kanal logosu, "sunar" kartı, jenerik ya da başlık kartının en başta olması ve başlığın 25-30. saniyeye ertelenmesi; (f) ilk saniyede soru kuran tek replik ya da kısa ekran yazısı (geri sayım, uyarı, mesaj); (g) ilk 30 saniyede en az bir "yükselme" (yeni tehdit, cevapsız soru, bedel). Bunları dizilerin ilk bölümleri ve soğuk açılışları, akış platformlarının (Netflix, Prime Video) ilk dakika ve otomatik oynatma verisi, fragman araştırmaları, kısa film festivalleri ve video reklam araştırmalarıyla (ilk 5 saniye, atlanabilir reklamda dikkat) karşılaştır. Reklam ve Shorts bulgularının organik uzun video izleyicisine taşınıp taşınamayacağını ayrıca tartış.
Kritik kısıt: kullanım yeri, bir kanalın her yeni filmine uygulanacak GENEL bir ilk 30 saniye kılavuzudur. Filmler yatay YouTube kısa filmleridir (2, 4, 8, 16 dakika); her çekim tam 10 saniyedir ve bu değişmez, yani ilk 30 saniye tam üç çekimdir; ritim kesme sıklığıyla değil çekim içi hareket, ölçek değişimi ve sesle kurulur. Filmler Google Flow'da (Veo ailesi) üretilen fotogerçekçi bilimkurgu filmleridir; replikler video modelinin kendisince seslendirilebilir, başlık ve yazı kurguda eklenir. Kanal küçüktür (birkaç bin abone) ve izleyicinin çoğu anadili İngilizce olmayan ülkelerdendir (Hindistan, Türkiye, Endonezya, Özbekistan). Atlanabilir reklam, Shorts ya da TikTok verisini organik uzun video için kanıt sayma; her satırda taşınabilirliği "düşük / orta / yüksek" diye işaretle. Daha kısa çekim, hızlı kesme ya da 10 saniyeden farklı çekim süresi gerektiren önerileri "hat dışı" diye işaretle ama silme; aynı amaca 10 saniyelik üç çekim içinde nasıl ulaşılacağını ÖNERİ olarak ekle.
Çıktıyı iki tablo ve dört liste olarak ver: (a) ÖLÇÜM tablosu — iddia, sayı, örneklem, uzunluk ve kategori, trafik kaynağı, tarih, kaynak, etiket; (b) AÇILIŞ BİÇİMİ tablosu — biçim (a-g), beklenen etki, ölçüm var mı, hangi bağlamda ölçüldü, uzun videoya taşınabilirlik, 10 saniyelik üç çekimde nasıl uygulanır, etiket. Etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (yaratıcı, ajans ya da danışman raporu) · ÖNERİ (senin çıkarımın) olsun. ÖLÇÜLMÜŞ dediğin her satıra birebir alıntı ve bağlantı ver; veremiyorsan o satırı ÖLÇÜLMÜŞ yazma. "Videoların %X'i ilk 30 saniyede izleyicisini kaybeder" türünden bloglar arasında dolaşan sayıları ilk kaynağına kadar izle; izleyemiyorsan "kaynaksız dolaşan sayı" diye ayrı listele. Aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) kanıt gücüne göre sıralı en çok 8 genel kural, her biri tek cümle ve etiketli; (2) saniye iskeleti önerisi (0-3, 3-10, 10-20, 20-30 aralıklarında ne olmalı), her aralık için dayandığı kaynak ya da "ÖNERİ"; (3) kaynaksız dolaşan sayılar; (4) bağlantılı tam kaynak listesi. Belgede olmayan sayı, ölçüt adı ya da tarih uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bunları açıklamalı

```
KANALIN KENDİ VERİSİ (sahibin Studio ekranı, 12.10.2026; "Giriş" = 30. saniyede kalan oran):
  THE_INWARD_FALL %51 · THE_STILL_POINT %16 · THE_OLD_ROAD %17
  aynı kanal, aynı tür; trafik kaynağı, yayın tarihi ve gösterim sayısı BİLİNMİYOR → üç video tek başına nedensellik kanıtı değil
İKİ FİLMİN PLANDAKİ AÇILIŞI (ikisi de 4 dk, 24 × 10 s, dönen istasyon, repliksiz, yüzü gizleyen vizör):
  INWARD_FALL  0-10 s düşen pim yana sapar (fiziksel anomali, LS) · 10-20 s teknisyen pime uzanır, gövdesi itilir (CU)
               · 20-30 s vizörde alarm (MCU) → sorun 0. saniyede, insan 10. saniyede, kapak anı 00:20'de
  STILL_POINT  0-10 s kopan turuncu anahtar uzaya fırlar (MCU, el) · 10-20 s istasyon aşırı geniş plan (mekân)
               · 20-30 s Nora eğri güvertede yürür (MS, yeni sorun yok) → insan bedeni 20. saniyede, kapak anı ≈2:50'de
  ⚠️ PLAN metni; yayımlanan videoların ilk 30 saniyesi kare kare doğrulanmadı (sahipten video ya da ekran kaydı gerekir)
DEPO ARIZASI: H08 "yavaş açılış" 10/52 rapor (ilk 10-20 s manzara, sorun yok)
TUTMA EĞRİSİ ÇÖZÜNÜRLÜĞÜ: API'de 100 nokta → 2 dk 1,2 s · 4 dk 2,4 s · 8 dk 4,8 s · 16 dk 9,6 s (16 dk'da ilk 30 s ≈ 3 nokta)
SAHİBİN YAPIŞTIRDIĞI ÖNERİDEKİ İDDİALAR (doğrulanacak):
  "Atla butonu 5. saniyede çıkıyor, karar orada" → yalnız atlanabilir reklam için doğru; organik izleyiciye taşınır mı?
  0-3 ilk görüntü · 3-10 sorun · 10-25 gerilim · 25-30 başlık iskeleti → hangi kaynakla?
  "logo / presents / kararmış ekranla açma" · "başlık sahneden sonra, sert kesmeyle" · "doruktan 5-8 s + '48 saat önce'"
CEVAPTAN BEKLENEN: %51 ile %16 arasındaki farkı açıklayabilecek ölçülmüş bir değişken var mı (sorunun ilk saniyesi ·
  insanın ilk saniyesi · kapak anının ilk 30 saniyede olması · trafik kaynağı) · "tipik giriş oranı" için ölçülmüş referans
  · logo ve başlık ertelemesinin ölçülmüş etkisi · 10 s × 3 çekimlik açılışa uyan saniye iskeleti.
```

---

# 2️⃣ KAPAKTAKİ VAAT İLK 30 SANİYEDE — tıklatan görüntü ne zaman ve nasıl teslim edilir

```
YouTube'da küçük resim (kapak) ve başlığın verdiği vaadin videonun ilk saniyelerinde teslim edilmesinin izleyici tutmasına etkisini Ekim 2026 itibarıyla araştır. YouTube'un resmî kaynaklarında (Yardım sayfaları, Creator Insider, YouTube blogu, "Test & Compare" ya da "Test and compare" belgeleri, öneri sistemi açıklamaları, memnuniyet anketi ve "ilgilenmiyorum" sinyalleri) şunları bul: başlık ve kapak testinin kazananı tıklama oranına mı izlenme süresi payına mı göre seçiliyor; YouTube'un "tıklatıp hayal kırıklığı yaratma" (clickbait) hakkında söyledikleri; vaat ile içerik arasındaki uyumsuzluğun öneri dağıtımına etkisi. Ardından bağımsız ölçümleri topla: kapak-içerik uyumsuzluğunun erken terk oranına etkisini ölçen akademik çalışmalar ve yöntemi yazılı yaratıcı deneyleri, aynı videoda kapak değişince giriş oranının değiştiği yayımlanmış örnekler, tıklama oranı ile ilk 30 saniye tutması arasındaki ilişki (ters ilişki var mı). Her biri için tarih, örneklem ve bağlantı ver.
Vaat teslim etmenin biçimlerini ayrı ayrı sor: (a) kapaktaki anın kendisi ilk 10 saniyede; (b) kapak anı ilk 30 saniye içinde; (c) kapak anından kısa bir parça önce gösterilip (ileri sıçrama) film baştan anlatılır; (d) kapak anı filmin sonunda, ilk 30 saniyede yalnız aynı dünya, aynı karakter ve aynı tehlike; (e) kapak filmde olmayan bir kompozisyon. Her birinin gerilimi "harcayıp harcamadığını", spoiler riskini ve tutma ile memnuniyete etkisini kanıtla tartış. Başlığın açılış repliğiyle ya da ilk ekran yazısıyla aynı soruyu sormasının etkisini, başlık ve kapakta vaat edilen nesnenin ya da yüzün açılışta aynı açıdan ve aynı ışıkta görünmesinin tanınmaya etkisini de sor. Kapak anının senaryo aşamasında seçilmesi ile üretimden sonra seçilmesini karşılaştıran uygulayıcı pratiklerini topla.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kılavuzdur. Filmler 2-16 dakikalık yatay fotogerçekçi bilimkurgu kısa filmleridir; ilk 30 saniye tam üç adet 10 saniyelik çekimdir ve bu değişmez. Kapak, filmle aynı referans görsellerinden ayrı bir görsel olarak üretilir ve film başına 2-3 kapak adayı YouTube'un kendi kapak testiyle sınanır. Kanal küçüktür, izleyicinin çoğu anadili İngilizce olmayan ülkelerdendir; başlık ve kapak yazısı İngilizcedir. Sonucu filmin hikâyesine değil kılavuza dönüştür: "kapak anı ilk 30 saniyede nerede, nasıl görünmeli" sorusunun genel cevabını ver.
Çıktıyı iki tablo ve üç liste olarak ver: (a) VAAT tablosu — bulgu, ölçüt (tıklama oranı, giriş oranı, ortalama izlenme, memnuniyet), sayı, örneklem, tarih, kaynak, etiket; (b) TESLİM BİÇİMİ tablosu — biçim (a-e), gerilime etkisi, spoiler riski, tutmaya etkisi, ölçüm var mı, 10 saniyelik üç çekimde nasıl uygulanır, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver, veremiyorsan ÖLÇÜLMÜŞ yazma; aynı kaynağa dayanan iki iddiayı iki kanıt sayma; kapak tasarımı (renk, yazı, yüz ifadesi) bu promptun konusu değil, yalnız vaat-içerik bağıyla ilgili kısmını al. Listeler: (1) kapak anı ile açılış arasında denetlenebilir en çok 6 kural (her biri "evet/hayır" ile kontrol edilebilir biçimde); (2) bilinen yanlışlar ve kaynaksız iddialar; (3) bağlantılı tam kaynak listesi. Belgede olmayan sayı ya da özellik adı uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN VERİSİ: INWARD_FALL giriş %51 · STILL_POINT %16 (1 numaradaki not geçerli: üç video, karıştırıcılar bilinmiyor)
KAPAK ANI ↔ AÇILIŞ (iki filmin KAPAK dosyası):
  INWARD_FALL  aday A = S01 · 00:20 (pimin sapması + merdivene tutunuş) → kapak anı İLK 30 SANİYEDE
  STILL_POINT  kapak anı = S17 "Durgun Nokta" (≈2:50), plan B = S15 → ilk 30 saniyede kapakta görünen an YOK;
               başlık "She Had to Stop Spinning to Escape" vaadi 2:30 sonra teslim
YENİ HAT: KAPAK_VE_YAYIN şablonu F6.3 "vaat ilk üç klipte görünür" maddesini taşıyor; kanıtı bu araştırma olacak
  örnek (THE_MAYDAY_SEA): aday A = C01/C22 (okyanus + kapsül) → okyanus 0. saniyede, kapsül 3:30'da
ESKİ HAT: PAKETLEME_VE_VAAT_KILAVUZU "kapak anı senaryoda seçilir, üretimden sonra aranmaz"
DIŞ SAYI: gösterim = kapak 1 saniyeden uzun ve en az %50 görünür (answer/7577430)
CEVAPTAN BEKLENEN: kapak anının ilk 30 saniyede olmasının ölçülmüş bir etkisi var mı · kapak testi izlenme süresi payına
  göre seçiyorsa vaat teslimi kapak seçimini nasıl etkiler · ileri sıçrama kapak vaadini teslim etmiş sayılır mı ·
  kılavuza girecek "evet/hayır" kontrolleri.
```

---

# 3️⃣ SÖZSÜZ ANLAŞILAN AÇILIŞ — anadili İngilizce olmayan izleyici için görüntü, yazı, altyazı, dublaj ve ilk saniyelerin sesi

```
Anadili İngilizce olmayan izleyicilerin (özellikle Hindistan, Türkiye, Endonezya, Özbekistan) İngilizce yatay YouTube videolarının ilk 30 saniyesini nasıl izlediğine ve neyle terk ettiğine dair Ekim 2026 itibarıyla kanıt araştır. YouTube'un resmî kaynaklarından şunları bul: çok dilli ses izleri ve otomatik dublajın (hangi diller, hangi kanallara açık, dudak senkronu) izlenme ve tutmaya etkisi için açıklanan sayılar; otomatik çevrilen başlık ve açıklamalar; otomatik ve çevrilmiş altyazıların kullanım oranı ve tutmaya etkisi; bu ülkelerde cihaz dağılımı (mobil, televizyon, masaüstü) ve sesi kapalı izleme oranı için yayımlanmış veriler. Bağımsız ölçümleri topla: altyazının ikinci dilde izleyicinin anlamasına ve görüntüye ayırdığı dikkate etkisi (göz izleme çalışmaları), ekran yazısının okunma süresi (kelime başına saniye, mobil ve televizyonda en küçük okunur yazı boyu), diyalog yoğunluğunun açılışta terk etmeye etkisi, sözsüz anlatımın (sessiz sinema, diyalogsuz animasyon kısa filmleri, görsel hikâye anlatımı araştırmaları) dil engelini nasıl aştığı. Tarih, örneklem, ülke ve bağlantıyla ver.
İlk saniyelerin sesini ayrıca sor: ilk 1-3 saniyede ses (sessizlik, sert efekt, nefes, alarm, replik, müzik) ile dikkat ve terk arasındaki ilişkiye dair ölçüm; ana sayfa önizlemesinin sessiz oynaması nedeniyle ilk saniyelerin sesi olmadan da çalışması gerektiği iddiası; müziğin açılıştaki rolü (hemen başlaması mı, sessizlikten sonra girmesi mi); açılışta tek bir İngilizce replik ya da kısa ekran yazısının (geri sayım, uyarı, mesaj) anadili İngilizce olmayan izleyici için yardımı mı engeli mi. Ses kaydı olmadan, yalnız görüntüyle "bir sorun var" bilgisinin ilk 10 saniyede nasıl verildiğine dair sinema ve reklam pratiğinden yöntemleri topla.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kılavuzdur. Filmler 2-16 dakikalık yatay fotogerçekçi bilimkurgu kısa filmleridir; ilk 30 saniye tam üç adet 10 saniyelik çekimdir. Karakterler çoğunlukla basınç giysili ve kasklıdır; yüz vizör ardındadır, dudak her zaman görünmez. Replikler İngilizcedir ve ya video modelinin kendisince ya da ayrı kayıtla seslendirilir; altyazı, ekran yazısı ve başlık kurguda eklenir, görsel üretim aşamasında görüntüye yazı konmaz. Diyalogsuz miks (müzik ve efekt) ayrı dışa aktarılabilir. Ülke ve cihaz verisi yoksa bunu açıkça söyle, genel küresel veriyi o ülkelerin verisi gibi sunma.
Çıktıyı üç tablo ve üç liste olarak ver: (a) KİTLE tablosu — ülke ya da bölge, cihaz payı, sesi kapalı izleme, altyazı kullanımı, dil, tarih, kaynak, etiket; (b) METİN VE DİL tablosu — araç (altyazı, ekran yazısı, çok dilli ses, otomatik dublaj, çevrilmiş başlık), ölçülen etki, koşul, sınır, kaynak, etiket; (c) İLK SANİYELERİN SESİ tablosu — ses türü, ölçülen ya da bildirilen etki, bağlam, taşınabilirlik, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; reklam ve Shorts verisini ayrı işaretle; aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) "sesi kapalı ve İngilizce bilmeyen izleyici ilk 30 saniyeyi anlıyor mu" sorusu için uygulanabilir bir test yöntemi (adımlar, kaç kişi, neye bakılır); (2) kılavuza girecek en çok 8 kural (ekran yazısı uzunluğu ve süresi, altyazı, açılış repliği sayısı, ilk ses); (3) bağlantılı tam kaynak listesi. Belgede olmayan sayı, dil sayısı ya da özellik adı uydurma.
```

### 🧪 SINAMA SETİ

```
KİTLE (sahibin Studio ekranı, 12.10.2026): çoğunluk Hindistan, Türkiye, Endonezya, Özbekistan; oranlar BİLİNMİYOR
SÖZSÜZ OLAN İKİ FİLM: INWARD_FALL ve STILL_POINT ikisi de repliksiz (0 replik), giriş %51 ↔ %16
  → aradaki fark diyalog miktarı değil; sözsüz anlatım tek başına açılışı kurtarmıyor
YENİ HAT: 06.10'dan beri REPLIK varsayılan "var"; 12.10'dan beri replikler model sesi (video promptunda birebir)
  örnek (THE_MAYDAY_SEA): ilk replik 10. saniyede (C02, telsizden erkek çağrı), 18 replik
06_SUZME (07.10) KABUL: çok dilli ses ekleyen kanallarda izlenme süresinin %25'ten fazlası birincil dil dışından;
  otomatik dublaj herkese açık, 27 dil · RED: "dublajlı videolar %60 daha uzun izlenir" (kaynak yok)
  açık iş: kurgu.py diyalogsuz miks (M&E) dışa aktarma
SAHİBİN YAPIŞTIRDIĞI ÖNERİ: "diyalog az görüntü çok · ekran yazısı kısa · altyazı mutlaka" → hangi kanıtla?
CEVAPTAN BEKLENEN: açılışta kaç replik ve kaç kelime ekran yazısı · altyazı tutmayı ölçülmüş biçimde etkiliyor mu ·
  ilk saniye sesinin sessiz önizlemeyle ilişkisi · sözsüz anlaşılırlık testi için ucuz yöntem.
```

---

# 4️⃣ YAPAY ZEKÂ FİLMİNİN İLK İZLENİMİ — kusur algısı, insan yüzü ve güvenilir açılış çekimi

```
Yapay zekâ ile üretilmiş fotogerçekçi videolarda izleyicinin ilk saniyelerde neyi fark ettiğini ve bunun izlemeyi bırakmaya etkisini Ekim 2026 itibarıyla araştır. Şunları topla: insanların yapay video ve görüntüyü kaç saniyede ve hangi ipuçlarından tanıdığına dair algı çalışmaları (yüz bozulması, el, yazı, fizik, ışık titremesi, filigran ve logo); "tekinsiz vadi" ve yapay yüzlere tepki çalışmaları; 2024-2026'da "yapay zekâ çöpü" (AI slop) tepkisini ölçen anket ve platform verileri; YouTube'un "değiştirilmiş ya da sentetik içerik" etiketinin izleyici davranışına etkisi için açıklanan bilgi; yapay zekâ ile yapıldığı bilinen kısa filmlerin izleyici yorumlarında açılışa dair şikâyetlerin sistemli incelemesi varsa onu. Ayrıca açılışta insan yüzünün ya da insan bedeninin bulunmasının dikkat, duygusal bağ ve tutma üzerindeki etkisini ölçen çalışmaları (göz izleme, reklam araştırmaları, video tutma analizleri) bul ve yüzü görünen karakter ile yüzü gizli (kask, vizör, sırtı dönük) karakter arasındaki farka dair kanıtı ayrı sor.
Üretim tarafını sor: yapay zekâ ile film yapan profesyonellerin ve stüdyoların (yayımlanmış vaka çalışmaları, festival filmleri, Runway AI Film Festival, Google Flow ve Veo ile yapılmış tanıtımı yapılan kısa filmler, yöntemini anlatan yaratıcılar) açılış çekimlerini nasıl seçtiği ve ürettiği: hangi çekim türleri video modellerinde daha güvenilir (geniş plan, yavaş kamera hareketi, tek özne, yüz yakın planı, el-nesne teması, kalabalık) ve hangileri riskli; açılış çekimlerine diğer çekimlerden daha fazla deneme ayırma, en temiz çekimlerle açma ve kusurlu çekimleri ortaya kaydırma pratikleri; filigran, logo ya da yazı artığı gibi ilk karede görünen kusurların izleyiciye etkisi. Google Veo ailesi için açılış çekimine özgü bilinen sınırları (ilk karelerde kayma, başlangıç görselinden sapma, ilk saniyede donma ya da sıçrama) resmî belge ve bağımsız testlerle ayrıca topla.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kılavuzdur. Filmler Google Flow'da bir başlangıç görseli ve tek bir İngilizce hareket promptuyla üretilen, her biri tam 10 saniyelik çekimlerden oluşur; ilk 30 saniye üç çekimdir. Tohum sabitleme, ince ayar, LoRA ve API dışı araç yoktur; her yeniden üretim kredi harcar. Karakterler genellikle basınç giysili ve kasklıdır; vizör filmden filme şeffaf (yüz görünür) ya da aynalı (yüz gizli) olabilir. Daha kısa çekim ya da çekim içinde kesme gerektiren çözümleri "hat dışı" işaretle ama silme. Algı çalışmalarının çoğu durağan görüntüyle yapıldıysa bunu belirt; video için genelleme yapma.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KUSUR ALGISI tablosu — kusur türü, fark edilme süresi ya da oranı, terk etmeye etkisi, durağan mı video mu, kaynak, etiket; (b) İNSAN VE YÜZ tablosu — açılış türü (yüz yakın plan, yüzü gizli insan, beden ya da el, insansız manzara, insansız nesne), ölçülen etki, bağlam, kaynak, etiket; (c) GÜVENİLİR AÇILIŞ ÇEKİMİ tablosu — çekim türü, video modelinde risk düzeyi, risk nedeni, ilk 30 saniyede kullanılabilir mi, düşük riskli karşılığı, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; firma tanıtım yazısını ÖLÇÜLMÜŞ sayma; aynı kaynağa dayanan iki iddiayı iki kanıt sayma. Listeler: (1) açılış çekimleri için üretim kuralları önerisi (çekim seçimi, deneme sayısı, kare onay ölçütleri, ilk karede aranacak kusurlar listesi), en çok 8 madde; (2) doğrulanabilir bulgular ile kaynaksız iddiaların ayrımı ve bağlantılı tam kaynak listesi. Belgede olmayan sürüm adı, sayı ya da özellik uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN VERİSİ: INWARD_FALL giriş %51 · STILL_POINT %16
YÜZ: ikisinde de yüz GİZLİ (INWARD_FALL yarı aynalı altın vizör · STILL_POINT opak siyah vizör)
  → "erken insan yüzü" iddiası bu ikiliyi açıklamaz; fark insanın (beden ve el) görünme saniyesinde olabilir: 10 s ↔ 20 s
  örnek (THE_MAYDAY_SEA): şeffaf vizör, yüz 10. saniyede (C02), 0-10 s insansız okyanus (C01)
AÇILIŞ KUSURU (qa_prompt_analizi_20261006, Gemini mercekleri):
  STILL_POINT  🔴 sağ alt köşe logosu / filigran 240 saniye boyunca, 0. saniyeden itibaren (iki mercek; yazılı yasak tutmadı)
               · S00-S02 🟠 kilitli kamera yavaş kaydı (00:03 · 00:12 · 00:22)
  INWARD_FALL  ilk üç çekimde 🔴 bulgu yok (en erken 🔴 S04)
  → açılış kusuru, giriş farkının ikinci güçlü adayı
YENİ HAT: cekim-yaz §F7 ve SABLON iş emri "watermark KAPALI" adımını taşıyor · F7'de "kare onaylanmadan video yok"
  · öncelikli zor planlar listesi var ama "açılışın üç çekimi ayrı kalite kapısından geçer" kuralı YOK
SAHİBİN YAPIŞTIRDIĞI ÖNERİ: "yüzün değiştiği, şeklin eridiği kareler sonraya · ilk 30 s en temiz çekimler · erken insan yüzü"
CEVAPTAN BEKLENEN: filigran ve ilk kare kusurunun terk etmeye etkisi ölçülmüş mü · yüz mü beden mi · açılış çekimi için
  kaç deneme ve hangi onay ölçütü · Veo'da ilk kareye özgü bilinen sınırlar.
```

---

# 5️⃣ AÇILIŞI SINAMAK VE OKUMAK — emsal dökümü, yayından önce ön test, yayından sonra teşhis

```
Kısa film açılışlarını yayından önce sınamanın ve yayından sonra okumanın yöntemlerini Ekim 2026 itibarıyla araştır; üç bölüm halinde. (A) EMSAL DÖKÜMÜ: YouTube'da yüksek izlenen bilimkurgu ve gerilim kısa filmlerinin (DUST, Omeleto, ALTER, Short of the Week seçkileri, festival ödüllü kısa filmler) ve 2024-2026'da çok izlenen yapay zekâ ile üretilmiş kısa filmlerin ilk 30 saniyesini saniye saniye dök: 0-3, 3-10, 10-20, 20-30 saniyede ne görünüyor; ilk sorun, ilk insan, ilk replik ya da yazı, ilk müzik kaç saniyede; başlık kartı kaç saniyede ya da hiç var mı; logo var mı. Yalnız bağlantısı verilebilen ve zaman damgası doğrulanabilen örnekleri al; izlenme sayısını tarihle yaz; yaratıcının tutma verisini açıkça paylaştığı örnekleri ayrıca işaretle. Dizi soğuk açılışlarını ve sinema fragmanlarının ilk 10 saniyesini (fragmanın başındaki kısa "fragman öncesi fragman" pratiği dahil) karşılaştırma için ekle.
(B) YAYINDAN ÖNCE ÖN TEST: bir açılışı yayımlamadan sınamanın yolları ve geçerlilikleri: hikâye taslağı ya da animatikle izleyici testi, küçük ücretli izleyici panelleri ve kitle testi hizmetleri, liste dışı bağlantıyla küçük grup testi, açılışı ayrı bir Shorts olarak yayımlayıp "izlendi / kaydırıldı" oranına bakmak, zorunlu seçim (iki açılıştan hangisi), "X saniyede ne anladın" soruları. Her yöntem için maliyet, gereken kişi sayısı, neyi ölçtüğü, organik YouTube davranışını ne kadar öngördüğü ve bunu gösteren kanıt var mı yaz. YouTube'un kendi aracının yalnız başlık ve kapağı mı test ettiğini, video içeriğini (açılışı) test etmenin resmî bir yolu olup olmadığını doğrula.
(C) YAYINDAN SONRA TEŞHİS: tutma eğrisinin ilk 30 saniyesini okuma: normal ilk düşüş ile anormal düşüş nasıl ayırt edilir; farklı trafik kaynaklarından gelen videoları karşılaştırmanın doğru yolu; YouTube Studio'nun "tipik" karşılaştırmasının neye göre hesaplandığı; yayımlanmış bir videonun başını Studio düzenleyicisiyle kırpmanın mümkün olup olmadığı ve istatistiklere etkisi; yeniden yükleme ile düzenleme arasındaki resmî ve uygulayıcı görüşleri. Son olarak, filmden filme bir açılış değişkenini sınamak için deney tasarımını sor: tek değişkenli değişiklik, karıştırıcıların (yayın günü, kapak, trafik kaynağı, uzunluk) kaydı, küçük kanalda anlamlı fark için kaç film ve kaç görüntüleme gerektiği.
Kritik kısıt: kullanım yeri, her yeni filme uygulanan GENEL bir kılavuzdur. Kanal küçüktür (birkaç bin abone), haftada en çok birkaç film yayımlanır, izleyicinin çoğu anadili İngilizce olmayan ülkelerdendir. Filmler 2-16 dakikalık yatay fotogerçekçi bilimkurgu kısa filmleridir; ilk 30 saniye tam üç adet 10 saniyelik çekimdir. Üretim hattında yayından önce yalnız metinle çalışan bir "izleyici" yapay zekâ ajanı ve üretilmiş karelerden yapılan bir animatik vardır; ücretli panel bütçesi yoktur ya da çok küçüktür. Bu yüzden ücretsiz ve az emekli yöntemleri öne al, pahalı olanları "hat dışı" işaretle ama silme. Yapay zekâ ajanının izleyici yerine geçmesini öneren kaynakları ayrı işaretle ve geçerliliğine dair kanıt varsa ver.
Çıktıyı üç tablo ve iki liste olarak ver: (a) EMSAL tablosu — film, kanal, bağlantı, tarih ve izlenme, 0-3 / 3-10 / 10-20 / 20-30 saniyede ne var, ilk sorun saniyesi, ilk insan saniyesi, ilk replik ya da yazı saniyesi, başlık saniyesi, logo; (b) ÖN TEST tablosu — yöntem, maliyet, kişi sayısı, neyi ölçer, organik davranışı öngörme kanıtı, kaynak, etiket; (c) TEŞHİS tablosu — eğri belirtisi, olası neden, nasıl doğrulanır, ne yapılır, kaynak, etiket. Etiketler ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ olsun; ÖLÇÜLMÜŞ satıra birebir alıntı ve bağlantı ver; emsal tablosunda kendin izleyip doğrulayamadığın zaman damgasını yazma, "doğrulanmadı" de. Listeler: (1) filmden filme açılış deneyi için bir kayıt şablonu (alanlar ve her alanın örnek cümlesi) ve en küçük örneklem önerisi; (2) bağlantılı tam kaynak listesi. Belgede olmayan özellik, sayı ya da izlenme değeri uydurma.
```

### 🧪 SINAMA SETİ

```
KANALIN VERİSİ: INWARD_FALL %51 · STILL_POINT %16 · OLD_ROAD %17 → üç nokta; karıştırıcı kaydı YOK
  (trafik kaynağı, yayın günü, kapak testi sonucu, gösterim) → deney defteri bu yüzden gerekli
HATTAKİ ÖN TEST ARAÇLARI: izleyici ajanı (F1 logline · F3 metin animatiği · F7 kare animatiği · F9 kapak 160×90)
  · kurgu.py görsel parça animatiği · ANLATIM_TESTI (eski hat) · paketleme §F10 geri besleme "not yazılır, kural yazılmaz"
DIŞ SAYI: tutma eğrisi API'de 100 nokta (4 dk → 2,4 s); "Giriş" ölçütü answer/9314415; 03/5 ölçüm yolunu sordu
SAHİP KANITI EKSİK: iki filmin yayımlanmış ilk 30 saniyesi (ekran kaydı ya da video) → kareler.py ile sahne sahne fark
SAHİBİN YAPIŞTIRDIĞI ÖNERİ: "Studio → Analytics → Kitleyi elde tutma → Giriş" · "hedef her filmi %51 seviyesine taşımak"
  · "doruk sahnesinden 5-8 s başa, ardından '48 saat önce'" → emsallerde bu kalıp ne sıklıkta, ölçüm var mı?
CEVAPTAN BEKLENEN: emsallerin ilk 30 saniyesinde ortak iskelet (sorun / insan / başlık saniyeleri) · ücretsiz ön testlerden
  hangisi organik davranışı öngörüyor · Shorts testi geçerli mi · tek değişkeni sınamak için kaç film gerekir ·
  kılavuz §8 deney defteri şablonu.
```
