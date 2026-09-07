# 🔬 13 — GİRİŞ VE FİNAL ARAŞTIRMA PROMPTLARI (04.09.2026)

> **Ne bu dosya:** filmlerin **nasıl açılması ve nasıl bitmesi**
> gerektiğini — ilk plan, son plan, ikisinin çifti ve süre bandına göre
> bütçesi — dış bilgiyle kurmak için hazırlanmış dört derin araştırma
> promptu. Her biri **altı cümledir** ve **salt prompt** çalışır —
> kopyala, araştırma aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı
> prompt ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki
> turun sonucu karşılaştırılamaz (07-12'nin gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin isteği (04.09.2026) — *"film girişleri ve
> sonları nasıl olmalı."* Depoda dört gerçek kesişiyor:
> ① `HOOK` §0③ kanca skoru bütün satırlarda aynı bantta PLATO yapıyor;
> §4 tipolojisindeki beş hook tipinden bugüne dek yalnız biri (görsel
> reveal) kullanıldı ve §2.1'in 0. kare / 120 px testi **hiç koşulmadı**.
> ② `05_DIKEY_HAT_TESHISI` §2.5: on sekiz dikey finalin hepsi tek
> kişiye ait — "final birine ait olmak zorunda" hükmü var, ama tek-insan
> kısıtı altında **muhatabın nasıl kurulacağı** hiçbir kılavuzda yazılı
> değil.
> ③ TUR 1'in hook araştırması yalnız DİKEY hattı ölçtü. Yatay bantların
> (2-4 · 3-5 · 7-9 · 10-20 dk) açılış ve kapanış BÜTÇESİ (kaç saniye,
> kaç sahne) hiçbir kılavuzda yok; `FINAL` §2 karar kuralında 10-20 dk
> satırı bile bulunmuyor.
> ④ `HOOK` §6① "hook sorusu ile kapanış imajı aynı cümlenin iki
> yarısıdır" der; ama çiftin NASIL kurulduğu — ilk ile son kare arasında
> ne değişir, kafiye mi döngü mü — belgesiz. Döngünün ÜRETİM kuralları
> `SENARYO_VE_VIRAL` §5'te; DRAMATURJİ tarafı boş.
>
> **KOŞU KAYDI:** ✅ dört prompt 04.09.2026'da koşuldu → dört rapor geldi.
> Ham metinler: `TUR10_HAM_RAPORLAR/`. Süzme: `04_ARASTIRMA_BULGULARI.md`
> §TUR 10. Kural indiği yer: `../ACILIS_KAPANIS_CIFTI_KILAVUZU.md` (açıldı)
> + `../HOOK_VE_ILK_SAHNE_KILAVUZU.md` §1.1 · §2.6 · §4 · §8 +
> `../FINAL_VE_PAYLASIM_KILAVUZU.md` §2 · §2.1 · §2.2 · §3 · §4.1 · §7 · §8.
> ⚠️ **"ZATEN VAR" kapısı en çok bu turda çalıştı:** raporların terk eğrisi,
> tamamlanma eşiği, döngü ve Raskin bulguları TUR 1 ve TUR 4'te zaten
> inmiş ya da elenmişti; ikinci kez inmediler (süzme kaydı §T10.1).

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR n (süzme kaydı) →
         ancak oradan HOOK_VE_ILK_SAHNE · FINAL_VE_PAYLASIM ·
         SENARYO_VE_VIRAL_KAMERA §5 · DIKEY_MIKRO_DRAMA §5 ·
         03_PLAN_ONCESI (yeni madde gerekirse).
   Süzme kaydı iki liste tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ BU ARAŞTIRMA "İYİ AÇILIŞLAR LİSTESİ" DEĞİLDİR.
   Aranan şey ilham panosu değil MEKANİZMA + ZAMAN DAMGASI: figür kaç
   saniyede belirir, soru kaç saniyede kadraja girer, son plan kaç saniye
   tutulur, doruk sonrası toplam sürenin yüzde kaçıdır. Kaynak "şöyle
   açılır güzel olur" diyor ama ölçmüyorsa, bulgu "GİRMEDİ" yazılır.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) filmden ÖLÇÜLMÜŞ zaman damgası (saniye, yüzde),
   (b) PLATFORM istatistiği (terk eğrisi, tamamlanma — örneklem ve
       tarih ile),
   (c) raporun kendi TASARIM ÖNERİSİ.
   TUR 1'in dersi: (b) sınıfındaki sayıların bir kısmı "matematiksel
   modelleme" çıktı ve depoya GİRMEDİ. Bu turda (b) örneklemsiz gelirse
   aynı muameleyi görür.

⛔ TUR 1 VE TUR 4 İLE ÇAKIŞMA — yeniden istenmeyenler.
   • Dikey ilk-3-saniye tutundurma yüzdeleri (TUR 1) → 4 yalnız YATAY
     bantlar için ister.
   • Final tipi → davranış eşlemesi (FINAL §2 · Xi 2024) → 2 bunu
     tekrarlamaz, ANLAM düzeyinde sorar ("bitti" hissi neyle verilir).
   • Dramatik ironi / bilgi eşitliği (HOOK §3.1) → istenmez.
   • Çıkarılabilir an (08 ①) → istenmez.
   Rapor bunları yine de getirirse süzme kaydı "ZATEN VAR" etiketiyle
   geçer, kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Az kurulum iyidir", "muğlak final iyidir", "döngü şarttır" bu
   deponun uygulamalarıdır, kanıtlanmış yasa değil — sorular iki yönlü
   sorulur (in medias res'in kafa karışıklığıyla TERK ürettiği vakalar,
   döngünün uzun formda TERS TEPTİĞİ vakalar da istenir). Üretim
   kısıtları (tek insan · kesmesiz 8-10 s plan · başlık/jenerik/okunur
   metin yok · dikeyde replik yok · vizör açılmaz · ilk kare = kapak)
   hipotez değil FİLTREDİR ve promptlara açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — üç çift.
   1 ↔ 3  : 1'in ölçtüğü açılış zamanları ile 3'ün çiftlerindeki ilk
            kare tarifleri aynı film için tutmalı.
   2 ↔ 3  : 2'nin son plan tutma süresi ile 3'ün son kare tarifi.
   4 ↔ 1/2: 4'ün band bütçeleri 1 ve 2'nin tek tek ölçümleriyle
            çelişiyorsa bütçe İNMEZ, çelişki kayda geçer.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Açılış planı — ilk imge doktrini + kesmesiz açılış grameri** | Beş hook tipinden biri kullanıldı; ilk planın bilgi bütçesi (kaç öğe, hangi sırada) yazılı değil; kesme olmadan kurulum neyle taşınır belgesiz | `HOOK` §2 (S0 kilitleri) · §4 tipoloji · `03_PLAN_ONCESI` |
| 2 | **Kapanış planı — son imge tipolojisi + muhatap + sonrası bütçesi** | Final "birine ait olmalı" ama tek-insan filminde muhatap çözümü yok; doruk sonrası bütçe tanımsız; "bitti" hissinin somut sinyalleri yazılı değil | `FINAL` §2-§4 · `05` §2.5'in çözüm satırı · `KURGU_VE_TESLIM` kırpma bütçesi |
| 3 | **Açılış-kapanış çifti — kafiye, döngü, aradaki değişim** | §6① çift kuralı var, çiftin mekanizması yok; kafiye ile döngünün süre bandına göre ayrımı belgesiz; ilk kare hem kapak hem dönüş karesi — yükü nasıl taşır | `HOOK` §6 · `SENARYO_VE_VIRAL` §5 · `DIKEY_MIKRO_DRAMA` §5 · `TEMA_MUHENDISLIGI` (tema→çift) |
| 4 | **Süre bandına göre giriş/çıkış bütçesi** | Yatay bantların terk eğrisi, açılış ve kapanış bütçesi (saniye + sahne) hiçbir kılavuzda yok; 10-20 dk satırı `FINAL` §2'de bile yok; hook tipi × final tipi × band eşleşmesi tanımsız | `FINAL` §2 karar kuralı (band satırları) · `HOOK` §1 · `KILAVUZ_REHBERI` §2 format kartları · `YAYIN_VE_PERFORMANS` |

---

# 1️⃣ AÇILIŞ PLANI — İLK İMGE DOKTRİNİ VE KESMESİZ AÇILIŞ GRAMERİ

```
Sinemanın "ilk imge" geleneğini mekanizma düzeyinde çıkar: film kuramı ve senaryo pedagojisinde (Bordwell'in açılış ekspozisyonu, McKee, Truby, Raskin'in kısa film parametreleri) ilk kadrajın taşıdığı işlevler — mekân, karakter, ton, kural ihlali, soru — nelerdir ve her işlev için ilk planın hangi süreyle, hangi ölçekte ve hangi bilgiyle yüklendiğini ölçülmüş örneklerle (Touch of Evil, Gravity'nin uzun açılışı, Children of Men, 2001, Arrival, Moon, Ad Astra, The Martian, All Is Lost) belgele. Zaman damgasıyla ölç: her örnekte insan figürü kaç saniyede belirir, ilk "yanlış" ya da soru kaç saniyede kadraja girer, ilk geri dönülmez eylem kaç saniyede gelir ve ilk kesme kaç saniyede — özellikle kesmesiz uzun açılışların kurulumu kesme olmadan hangi araçlarla (kadraj içi hareket, ışık değişimi, ses girişi, ölçek şahidi, karakterin bir işi yapıyor olması) taşıdığını ayır. Ödüllü ve yüksek izlenmeli bilimkurgu kısa filmlerinde (Oscar adayı kısa filmler, Sundance, DUST ve Omeleto kanallarının en çok izlenenleri) açılışı aynı ölçülerle sök ve festival programcılarının ilk bir-iki dakikada karar verdiğine dair belgelenmiş ifadeleri, hangi açılış hatasının eleme sebebi sayıldığını topla. Ekspozisyon ekonomisini iki yönlü araştır: evren inşasının tamamını öne alıp çatışmayı sona bırakan filmlerin "hiçbir şey olmuyor" şikâyeti aldığına dair izleyici ve eleştiri kanıtı ile, tersine, sıfır kurulumla açılıp bağlam borcunu sonra ödeyen in medias res açılışların hangi koşulda kafa karışıklığıyla terk ürettiğine dair kanıtı yan yana koy. Kritik kısıt: hedef filmler tek insan karakterlidir, her sahne kesmesiz 8-10 saniyelik plandır, başlık kartı, jenerik, okunur metin ve altyazı yoktur, dikey formatta replik de yoktur ve ilk kare aynı zamanda akıştaki KAPAK karesidir (küçük boyutta okunmak zorundadır) — bu yüzden kalabalık, diyaloglu ekspozisyon, başlık kartı ve hızlı kesmeye dayanan açılış tekniklerini işaretleyip ele, tek sabit planda ve tek figürle çalışanları öncelikle. Çıktıyı tablo olarak ver: açılış işlevi, film/kısa film örneği ve saniye ölçümleri (figür, soru, geri dönülmez eylem, ilk kesme), kesmesiz tek planda taşıyıcı araç, küçük boyutta okunurluk notu ve plana yazılacak tek satırlık İngilizce açılış kadrajı ifadesi; ayrıca ilk planın taşıması gereken bilgi için bir "açılış bilgi bütçesi" şablonu ekle (kaç öğe, hangi sırada, hangisi ertelenir).
```

---

# 2️⃣ KAPANIŞ PLANI — SON İMGE TİPOLOJİSİ, MUHATAP VE SONRASI BÜTÇESİ

```
Sinema ve kısa filmde son planın tipolojisini çıkar: ilk kadraja dönüş, karakterin kadraj dışına bakışı, nesne eki, geri çekilen ya da tutulan geniş plan, karartma, donma, çıkıp giden figür, boş kalan kadraj — her tipin hangi filmde kullanıldığını, son planın kesmeye ya da karartmaya kadar kaç saniye tutulduğunu ve karakterin son kareyi hangi konumda (sırtı dönük, yüzü görünür, kadraj dışı, hareketsiz, hareket hâlinde) terk ettiğini ölçerek belgele. Doruk sonrası bütçeyi ölç: doruk anından son kareye kadar geçen süre uzun metrajda, ödüllü kısa filmlerde ve yüksek izlenmeli platform kısa filmlerinde toplam sürenin yüzde kaçıdır, Raskin ve Cooper-Dancyger gibi kısa film kuramcıları bu "sonrası"na ne kadar yer verir ve hangi filmler doğrudan dorukta biterek bu bütçeyi sıfırlar, örnekleriyle. Sonun kime ait olduğunu araştır: kazanılan ya da kaybedilen şeyin izleyicide karşılık bulması için son kadrajda ya da kadraj dışında bir muhatabın (ikinci kişi, ses, nesne, iz, seyircinin kendisi) bulunması gerektiğine dair dramaturji kuramı ve izleyici tepkisi kanıtı — tek kişilik anlatılarda (All Is Lost, Gravity, Moon, Cast Away, 127 Hours, Buried) muhatap kimdir ve son kadraj onu nasıl gösterir ya da ima eder, tek tek belgele. Kapalı, açık ve muğlak sonlar arasındaki farkı davranış değil ANLAM düzeyinde sök: izleyicinin "bitti" hissini hangi somut sinyaller verir (kadraj boşalması, sesin kesilmesi, ışık değişimi, karakterin duruşu, tempo düşüşü), muğlak sonun aldatılmışlık hissine döndüğü eşik hangi değişkenle (açık soru sayısı, tohum bilginin varlığı, son planın süresi) ilişkilendirilmiş ve iyi ile kötü muğlak sonu ayıran eleştiri kanıtı nedir. Kritik kısıt: hedef filmler tek insan karakterlidir, ikinci insan kadrajda ya da seste bulunamaz, jenerik ve son kartı yoktur (son kare filmin fiilen son karesidir ve dikeyde ilk kareye döngüyle bağlanır), her sahne kesmesiz 8-10 saniyelik plandır ve vizör açılarak yüz gösterilemez — bu yüzden ikinci kişiye, jenerik müziğine, yüz açılışına ve montaj sekansına dayanan kapanışları işaretleyip ele, tek figür ve tek planla çalışan "muhatap" çözümlerini öncelikle. Çıktıyı iki tablo olarak ver: (a) son plan tipi, film örneği, tutma süresi, karakter konumu, sonrası bütçesi yüzdesi, tek planda uygulanabilirlik ve tek satırlık İngilizce kapanış kadrajı ifadesi; (b) tek kişilik anlatıda muhatap çözümü, örneği, kadrajda mı kadraj dışında mı olduğu, replik ve metin olmadan kurulup kurulamadığı ve tek satırlık İngilizce ifadesi.
```

---

# 3️⃣ AÇILIŞ-KAPANIŞ ÇİFTİ — KAFİYE, DÖNGÜ VE ARADAKİ DEĞİŞİM

```
İlk ve son kadrajın birbirine kafiyeli olduğu filmleri sistemli olarak sök: aynı mekânın, aynı kompozisyonun ya da aynı nesnenin filmin başında ve sonunda farklı anlamla gösterildiği vakalarda (görsel kafiye, ayna kompozisyon, "aynı plan farklı anlam") ilk ile son kare arasında tam olarak NE değişir — karakter konumu, nesne durumu, ışık yönü, kadraj ölçeği, ses — ve bu değişim temayı nasıl taşır; ilk ve son kareleri yan yana koyan karşılaştırma çalışmalarından ve yapım notlarından en az yirmi çift belgele. Kafiye ile döngüyü ayır: kusursuz döngü (son karenin ilk kareye kesintisiz akması, kısa video platformlarında tekrar izleme için) ile kafiye (son karenin ilk kareyi anlam değişimiyle yankılaması, uzun formda) hangi süre bandında hangisinin doğru olduğuna, döngünün uzun formda ya da kafiyenin kısa formda ters teptiğine dair platform verisi, eleştiri ve yapım deneyimi topla. Çiftin dramaturjik yükünü ölç: son karenin ilk kareye göre değişimi izleyiciye "bir şey oldu" hissini replik ve metin olmadan hangi somut değişkenle verir, değişimin fazla küçük (fark edilmez) ya da fazla büyük (bağ kopar) olduğu eşiklere dair algı çalışması ya da yapım kararı var mı ve tek karakterli anlatılarda değişim karakterin gövdesinde mi, nesnede mi, çevrede mi taşınıyor — örneklerle sınıflandır. Tohum ve ödeme ilişkisini çifte bağla: ilk kadrajda yer alan hangi tür öğe (nesne, iz, ışık durumu, ses) son kadrajda ödeme olarak geri gelir, ilk kadrajda öğenin görünürlüğü (merkezde mi, kenarda mı, kaç saniye) ile son kadrajdaki tanınırlığı arasında hangi ilişki belgelenmiş ve izleyicinin başa sarıp doğrulama davranışını tetikleyen çift örnekleri hangileridir. Kritik kısıt: hedef filmler tek insan karakterlidir, her sahne kesmesiz 8-10 saniyelik plandır, okunur metin, başlık ve jenerik yoktur, dikey formatta döngü zorunludur ve ilk kare aynı zamanda kapak karesidir — bu yüzden kafiyeyi montajla, yazıyla ya da ikinci karakterle kuran çiftleri işaretleyip ele; tek figür, tek nesne ya da ışık değişimiyle kurulan çiftleri öncelikle ve ilk karenin hem kapak hem dönüş karesi olma yükünü nasıl taşıdığını açıkla. Çıktıyı tablo olarak ver: film/kısa film çifti, ilk kare tarifi, son kare tarifi, değişen değişkenler, taşınan tema, kafiye mi döngü mü, süre bandı, tek figür ve tek planda uygulanabilirlik notu ve çift için tek satırlık İngilizce "OPENING FRAME / CLOSING FRAME" ifadesi; ayrıca ilk ve son kadraj planlanırken doldurulacak bir "çift kartı" şablonu ekle.
```

---

# 4️⃣ SÜRE BANDINA GÖRE GİRİŞ VE ÇIKIŞ BÜTÇESİ

```
Beş süre bandı için (bir dakikanın altındaki dikey kısa, iki-dört dakika, üç-beş dakika, yedi-dokuz dakika ve on-yirmi dakika) izleyicinin nerede terk ettiğini belgele: kısa video platformlarında ilk saniyelerin, uzun form videoda ilk otuz saniye ve ilk dakikanın terk eğrileri, süre uzadıkça eğrinin biçiminin nasıl değiştiği ve kapanışa yaklaşırken görülen ikinci düşüşün varlığı — platform yaratıcı raporları, analitik firmaları ve akademik çalışmalardan, her sayının kaynağı, tarihi ve örneklem büyüklüğüyle. Her band için açılış bütçesini ölç: ilk dramatik hamleye (soru, ihlal, geri dönülmez eylem) kadar geçen sürenin toplam süreye oranı ödüllü ve yüksek izlenmeli kısa filmlerde band band nedir ve aynı hikâyenin farklı sürelerde anlatıldığı vakalar (kısa filmden uzun metraja uyarlanan Whiplash, Lights Out, Mama gibi örnekler) açılış oranını nasıl değiştirdi. Her band için kapanış bütçesini ölç: doruktan son kareye kadar sürenin oranı band band nedir, kısa bantlarda dorukta bitme ile uzun bantlarda sonrası bölümünün gerekli olduğuna dair kuram (Raskin, Cooper-Dancyger, Save the Cat'in kısa form uyarlamaları) ve platform verisi nedir ve uzun formda finalin izleyicinin yatırımını boşa çıkarma riskinin süreyle nasıl büyüdüğüne dair kanıt var mı. Süre bandına göre açılış ve final tipi eşleşmesini araştır: hangi hook tipi (ölçek şoku, yanlışlık kompozisyonu, in medias res, yetkinlik süreci, ses-önce) ve hangi final tipi (kapalı, muğlak, ters dönüş, döngü) hangi süre bandında belgelenmiş olarak daha iyi tamamlanma, tekrar izleme ya da paylaşım alıyor ve aynı tipin bir bantta çalışıp diğerinde çalışmadığı vakalar nelerdir. Kritik kısıt: hedef filmler tek insan karakterlidir, sahneler kesmesiz 8-10 saniyelik sabit planlardan kuruludur (kısa bantta bir elin parmağı kadar sahne, uzun bantlarda on beşten fazla), başlık kartı, jenerik ve okunur metin yoktur, dikeyde replik de yoktur ve döngü zorunludur — bu yüzden her bütçe önerisini saniye yanında SAHNE SAYISI cinsinden de ver ve hızlı kesmeye, başlık kartına, diyaloglu özet sahnesine dayanan çözümleri işaretleyip ele. Çıktıyı band başına bir satır olan tablo olarak ver: süre bandı, terk eğrisinin kritik noktaları ve kaynağı, açılış bütçesi (saniye ve sahne sayısı), ilk dramatik hamlenin en geç yeri, kapanış bütçesi (saniye ve sahne sayısı), önerilen hook tipi ve final tipi eşleşmesi ile dayanağı ve her band için tek satırlık İngilizce "OPENING BUDGET / CLOSING BUDGET" plan satırı; ölçülmüş zaman damgası, platform istatistiği ve raporun kendi tasarım önerisini ayrı etiketle.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TURn_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil). 12 ile aynı gün gelirse AYRI
   klasör, AYRI tur numarası; prompt metinleri ham dosyaların başına
   birebir kopyalanır (Tur 7 usulü).
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR n açılır ve İKİ liste yazılır:
   GİRDİ (hangi bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
   Her sayı ÜÇ etiketten birini taşır: ÖLÇÜLMÜŞ · PLATFORM · ÖNERİ.
   TUR 1 ve TUR 4'te zaten inen bulgular "ZATEN VAR" etiketiyle geçer.
3. ⛔ Raporlar ÇAPRAZ OKUNUR (1↔3 açılış zamanı-ilk kare · 2↔3 son plan
   süresi-son kare · 4↔1/2 band bütçesi-tek tek ölçüm). Tutmayan sayı
   kılavuza İNMEZ, çelişki kayda geçer.
4. Ancak ondan sonra kılavuzlar düzenlenir: HOOK §2/§4 (açılış bilgi
   bütçesi · tip seçimi), FINAL §2 (10-20 dk satırı · sonrası bütçesi ·
   muhatap çözümü), SENARYO_VE_VIRAL §5 / DIKEY_MIKRO_DRAMA §5 (çift
   kartı), 03_PLAN_ONCESI (gerekirse yeni madde). HOOK §0③'ün plato
   ölçütü değişmez: kanca skoru aynı bantta kalırsa bu turun kuralları
   da çalışmıyor demektir.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Filmden ölçülen zaman damgaları rapor yazarının ölçümüdür ve ikinci bir
okumayla doğrulanmadan bağlayıcı değildir; platform istatistikleri
örneklemsiz gelirse TUR 1'deki gibi düşer; sinema örneklerinin tamamı
çok karakterli ve kesmeli yapımlardır — tek insan, kesmesiz plan ve
metinsiz kapanış kısıtı altında hiçbir bulgu üretimde test edilmeden
kural sayılmaz. İlk uygulamada ④ HİKAYE (kanca · final sütunları) ve
gerçek yayın verisi (`08_YAYIN_PERFORMANS_TABLOSU`) ile sınanır; yayın
verisi geldiği gün bu turun bütün sayıları o veriye teslim olur.
