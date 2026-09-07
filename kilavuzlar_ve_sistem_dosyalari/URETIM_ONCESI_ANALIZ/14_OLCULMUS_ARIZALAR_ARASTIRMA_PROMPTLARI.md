# 🔬 14 — ÖLÇÜLMÜŞ ARIZALAR ARAŞTIRMA PROMPTLARI (04.09.2026)

> **Ne bu dosya:** deponun **ölçülmüş** dört arızasına vuran dört derin
> araştırma promptu. Seçim ölçütü tekti: zayıflık depoda bir dosya ve
> satırla ölçülmüş mü, ve araştırma o soruyu gerçekten kapatabilir mi.
> Her biri **altı cümledir** ve **salt prompt** çalışır — kopyala,
> araştırma aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı
> prompt yeniden koşulacaksa aynı metin koşulmalı (07-13 ile aynı gerekçe).
>
> **Neden ŞİMDİ:** sahibin isteği (04.09.2026) — *"daha iyi filmler için
> en gerekli dört araştırma."* Dört arıza, dört ölçüm:
> ① `06_HIKAYE_HATTI_TESHISI` §0: *"depo hikâye yazmıyor, novum gösterisi
> yazıyor"* · `05` §2: on sekiz dikey film aynı filmi yazdı. Vuruş
> haritaları çok karakterli, diyaloglu filmlerden çevrildi; sahneyi
> sahneye bağlayan mekanizma hiçbir kılavuzda yok.
> ② `KURGU_VE_TESLIM` §0: Unbroken City'de S9 doruk kurguya girmedi,
> Last Shift'te 27 klibin ~17'si ekranda kaldı · `FINAL` §0②: düşük final
> skorlarının çoğu KURGUNUN puanıdır. Yazmayı anlatan on kılavuz var,
> birleştirmeyi anlatan yok.
> ③ Ders 79 vizörün şeffaf ve yüzün okunur olmasını ŞART koşuyor;
> `DIKEY_MIKRO_DRAMA` §6.1 ise "kırılgan insan duygusu + fotogerçekçi
> insan" kutusunun güveni ~%50 düşürdüğünü ölçtü. Duygunun tek doğal
> kanalı hem zorunlu hem en cezalı.
> ④ `04` §T4.2: plan bütçesinin %78'i üretime, %22'si hikâyeye ·
> `01_DERS_ETKINLIK` §288: ders etkinliği "ölçülemedi" · her kılavuzda
> ⚙️ damgalı sınanmamış satırlar. Kural eklemek değil, SİLMEK gerek.
>
> **KOŞU KAYDI:** ✅ dört prompt 04.09.2026'da koşuldu → dört rapor geldi
> (TUR 11 · TUR 8 hâlâ dosya 11'e rezerve ve boş).
> Ham metinler: `TUR11_HAM_RAPORLAR/` (TAM metin, kaynak listeleri dâhil).
> Süzme: `04_ARASTIRMA_BULGULARI.md` §TUR 11.

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04 §TUR 11 (süzme kaydı) → ancak oradan kılavuza.
   İki liste: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ TUR 9 VE 10'UN DERSİ: SORU CEVABIN BİÇİMİNİ DAYATMAZ.
   TUR 10'da prompt beş kanca tipini raporun önüne koydu, rapor onları
   sıraladı ve bunu "belgelenmiş" diye sundu. TUR 9'da "çapa/kayma
   riski" sütunları dört raporda tek promptun yankısı çıktı. Bu dosyanın
   promptları envanter İSTER, listeyi VERMEZ. Kendi kısıtlarımız yalnız
   son iki cümlede, FİLTRE olarak durur.

⛔ SAYI ÜÇ ETİKETLE GELİR: ÖLÇÜLMÜŞ (deney/göz izleme/benchmark) ·
   İKİNCİL (eleştiri, yapım notu, topluluk testi) · ÖNERİ (raporun
   kendi tasarımı). Etiketsiz sayı inmez; TUR 9 bunun bedelini ödedi.

⛔ "ZATEN VAR" KAPISI AÇIK. Sessiz izleme oranı, dramatik ironi,
   Zeigarnik, Raskin'in karakter anı, Wistia/TikTok terk eğrileri,
   Chion'un akuzmatik sesi, el/POV vekili — hepsi 04'te kayıtlı ya da
   elenmiş. İkinci kez inmez; süzme "ZATEN VAR" etiketiyle geçer.

⛔ RAPORLAR ÇAPRAZ OKUNUR — üç çift.
   1 ↔ 2 : sahne zinciri ile kurgu — yazılan bağın kurguda koptuğu vaka.
   3 ↔ 4 : yüz riski ile motorun yüz davranışı — aynı cezanın iki yüzü.
   2 ↔ 4 : klip kırpma ile zamansal tutarlılık — kırpılan klipte ne bozulur.
```

**Hangi prompt hangi ölçülmüş arızaya vurur:**

| # | Konu | Ölçülmüş arıza | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Sahne zinciri — ileri itki** | 06 §0 · 05 §2 (18/18 aynı film) | `SENARYO_VE_VIRAL` §2 vuruş haritası · `ONERME_VE_NOVUM` · 06'nın kapalı döngüsü |
| 2 | **Kurgu kaybı** | KURGU §0 (doruk kurguya girmedi) · FINAL §0② | `KURGU_VE_TESLIM` · `KURGU_RITMI_VE_IHRAC` · D62/D72 |
| 3 | **Duygu kanalı — yüz hem şart hem cezalı** | D79 ↔ DIKEY §6.1 | `KARAKTER_VE_DUYGU` · DIKEY §4.2 · `SHORTS_SISTEM_PROMPTU` |
| 4 | **Kural temizliği — motor davranışı** | T4.2 %78/%22 · 01_DERS_ETKINLIK "ölçülemedi" | her kılavuzun ⚙️ satırları · `IMAGE_VIDEO_PROMPT_TEMPLATES` · `prompt_kontrol` |

---

# 1️⃣ SAHNE ZİNCİRİ — İZLEYİCİ NEDEN DÖRDÜNCÜ SAHNEYİ İZLER

```
Tek karakterli, replik ve okunur metin içermeyen, kesmesiz sabit planlardan kurulu kısa anlatılarda sahneden sahneye İLERİ İTKİYİ neyin ürettiğini anlatı kuramı (Bordwell'in hipotez kurma modeli, Sternberg'in merak-gerilim-sürpriz üçlüsü, Brewer ve Lichtenstein'ın yapısal duygu modeli) ve ölçülmüş izleyici çalışmaları düzeyinde çıkar. Sahne sınırında kurulan bağ tiplerinin envanterini yap: bir sahnenin sonunda açılan sorunun tipleri (eylemin sonucu, nesnenin akıbeti, mekânın sırrı, bedenin sınırı, zamanın dolması), bir sonraki sahnenin bu soruya verdiği cevap tipleri (kısmi cevap, cevap yerine yeni soru, cevabın ertelenmesi, cevabın yanlış çıkması) ve her tipin hangi filmde hangi sahne çiftinde kullanıldığını zaman damgasıyla belgele. Örneklem olarak All Is Lost, Gravity, Moon, Buried, 127 Hours, Wall-E'nin ilk yarısı, The Red Turtle ve ödüllü diyalogsuz kısa filmleri al; her birinde ardışık sahne çiftlerini "bu sahnenin sonunda izleyici ne bilmiyor ve bir sonraki sahnede ne öğreniyor" diye tek tek sök, sahne sayısı ve süre payıyla. Karşı yönü eşit ağırlıkla araştır: itkinin KOPTUĞU yerleri — izleyici ve eleştiri korpusunda "hiçbir şey olmuyor", "art arda güzel kareler", "durum ama hikâye değil" şikâyetlerinin çıktığı sahne dizilerinde hangi bağın eksik olduğunu, ve tersine bağın fazla belirgin olduğu (tahmin edilebilir) dizilerde şikâyetin nasıl değiştiğini. Kritik kısıt: hedef filmlerde tek insan vardır, her sahne kesmesiz 8-10 saniyelik sabit plandır, replik ve okunur metin yoktur, ikinci bir insan ne kadrajda ne seste bulunabilir — bu yüzden diyalogla, ikinci karakterle, montajla ya da metinle kurulan bağ tiplerini işaretleyip ele; tek figürün eylemi, tek nesnenin durumu ve çevrenin kalıcı değişimiyle kurulanları öncelikle. Çıktıyı tablo olarak ver: bağ tipi, açılan soru tipi, cevap tipi, film ve sahne çifti (zaman damgalı), kaynak ve ölçüm türü (izleyici ölçümü, eleştiri ya da raporun kendi çıkarımı ayrı etiketle), tek figürlü sessiz karşılığı ve sahne sonu ile sahne başı için tek satırlık İngilizce plan ifadesi; ayrıca 6 sahnelik ve 25 sahnelik iki format için "hangi sahne sonunda hangi soru açık kalmalı" şablonu.
```

---

# 2️⃣ KURGU KAYBI — YAZILAN FİLM İLE TESLİM EDİLEN FİLM

```
Plan sayısı kısıtlı ve sahne içi kesme içermeyen filmlerin montaj gramerini çıkar: tek plan sekans geleneği (Tarr, Sokurov, Angelopoulos, Tsai Ming-liang), planlar arası sert kesmeyle kurulan filmler (Ozu, Akerman, Kiarostami) ve kesmesiz 8-10 saniyelik kliplerden birleştirilen çağdaş AI kısa filmleri — her birinde ortalama plan süresi, plan sayısı, planlar arası geçiş tipi dağılımı (sert kesme, ses köprüsü, kararma, eşleşen hareket) ve kesme anının hareketin neresine düştüğü ölçülsün. Kesilen sahne problemini belgele: yapım notları, yönetmen anlatıları ve kurgu literatüründe (Murch'ün altı ölçütü, Pearlman'ın ritim modeli) yazılı senaryoda var olup kurguda düşen sahnelerin hangi gerekçelerle düştüğünü sınıflandır — süre, tempo, tekrar, bilgi fazlalığı, teknik kusur — ve özellikle DORUK ya da BEDEL sahnesinin kesildiği belgelenmiş vakaları ve sonuçlarını topla. Sahne içi kesme olmadığında ritmin nereden geldiğini araştır: kadraj içi hareketin süresi, ses tasarımının plan sınırını yumuşatması ya da vurgulaması, plan uzunluklarının dizisi (uzun-kısa-uzun) ve izleyicinin sabit planda dikkatini ne zaman kaybettiğine dair göz izleme ya da terk ölçümleri. Karşı yönü araştır: sahne sayısını korumanın filmi UZATIP zayıflattığı vakalar ile kesmenin filmi kurtardığı vakaları yan yana koy ve "her sahne kalsın" ile "acımasız kes" arasındaki kararın hangi ölçütle, hangi filmde nasıl verildiğini belgele. Kritik kısıt: hedef filmler 6 ile 120 arasında kesmesiz 8-10 saniyelik klipten kurulur, klip içinde kesme yapılamaz, klipler yalnız SIRALANIR ve baştan ya da sondan KIRPILIR, geçişte jenerik ya da kart yoktur — bu yüzden klip içi kesmeye, hızlı kurguya ya da metne dayanan montaj tekniklerini işaretleyip ele; yalnız klip sırası, klip kırpma, ses köprüsü ve plan uzunluk dizisiyle çalışanları öncelikle. Çıktıyı tablo olarak ver: teknik ya da vaka, film ve kaynak, ölçülen değer (plan süresi, kesme konumu, düşen sahne oranı), sahne içi kesmesiz yapıda uygulanabilirlik ve tek satırlık İngilizce kurgu notu; ayrıca "kesilemez sahne listesi" için ölçüt şablonu ve 6, 25 ve 120 klip için birer plan uzunluk dizisi örneği.
```

---

# 3️⃣ DUYGU KANALI — YÜZ HEM ŞART HEM CEZALI

```
Yüzün güvenilmez ya da kısıtlı olduğu anlatılarda duygunun hangi kanallardan taşındığını ölçülmüş düzeyde çıkar: maske tiyatrosu (Noh, commedia dell'arte, Lecoq pedagojisi), pantomim ve fiziksel tiyatro, kasklı ve maskeli sinema oyunculuğu (Alien'daki giysi sahneleri, Gravity ve The Martian'ın kask içi planları, Darth Vader ve Judge Dredd gibi yüzü kapalı figürler), animasyonda "beden önce, yüz sonra" ilkesi ve hareket yakalamada gövde verisinin yüz verisinden ayrı ölçüldüğü çalışmalar. İzleyicinin duyguyu bedenden okuduğuna dair deneysel kanıtı topla: yüz gizliyken duruş, omuz hattı, baş yönelimi, el ve nefes ritminden duygu tanıma doğruluğu üzerine psikoloji çalışmaları (Aviezer, de Gelder ve beden ifadesi literatürü), hangi duyguların bedenden yüksek, hangilerinin düşük doğrulukla okunduğu ve bu okumanın kaç saniyede gerçekleştiği. Yapay yüzün bedelini ayrıca ölçülü belgele: fotogerçekçi insan yüzünde tekinsiz vadi, güven kaybı ve "bu yapay" tespiti üzerine çalışmalar, hangi mikro hareketlerin (göz kırpma, dudak, deri dokusu) tespiti tetiklediği ve yüz kadrajda küçükken ya da kısmen kapalıyken bu cezanın nasıl değiştiği. Karşı yönü eşit ağırlıkla araştır: yüzü tamamen kapatmanın izleyici bağını KOPARDIĞI belgelenmiş vakalar (kasklı karakterlerin empati alamadığı yapımlar, maskeli figürün "nesne" okunması) ile yüzün küçük bir payla görünmesinin yeterli olduğu vakalar — bağ için yüzün asgari payı neyle ölçüldü. Kritik kısıt: hedef filmlerde tek insan vardır, her sahne kesmesiz 8-10 saniyelik sabit plandır, replik yoktur, karakter basınç giysisi içindedir ve vizör şeffaf olmak zorundadır (yüz görünür ama kadrajın küçük bir payıdır ve fotogerçekçi yüz en yüksek yapay-tespit riskini taşır) — bu yüzden yüz yakın planına, diyaloğa ya da ikinci karakterin tepkisine dayanan teknikleri işaretleyip ele; gövde, el, nefes, duruş ve giysinin fiziksel tepkisiyle (vizör buğusu, eldivenin sıkılması, omzun düşmesi) çalışanları öncelikle. Çıktıyı iki tablo olarak ver: (a) duygu başına taşıyıcı kanal, ölçülmüş tanıma doğruluğu ve süresi, kaynak, 8-10 saniyelik sabit planda uygulanabilirlik ve tek satırlık İngilizce hareket ifadesi; (b) yapay yüz cezası — tetikleyici, kaynak, kadraj payıyla ilişkisi ve kaçınma yolu; ayrıca "yüz kadrajın kaçta kaçı olmalı" sorusu için ölçülmüş bant ya da açıkça "ölçülmedi" kaydı.
```

---

# 4️⃣ KURAL TEMİZLİĞİ — HANGİ ÜRETİM KURALI GERÇEK, HANGİSİ HURAFE

```
Metinden ve imajdan video üreten difüzyon modellerinin (Veo 3 ailesi, Sora, Kling, Runway Gen-4, Wan, Hunyuan) prompt davranışını ÖLÇÜLMÜŞ düzeyde çıkar: prompt uzunluğu ile talimata uyum arasındaki ilişki, talimatın prompt içindeki konumunun (baş, orta, son) etkisi, negatif prompt ya da "no X" cümlelerinin gerçekten neyi değiştirdiği ve hangi modellerde hiç işlemediği, sayı ve miktar ifadelerinin ("three", "hundreds of") ne kadar tutturulduğu — hakemli benchmark çalışmaları (VBench, EvalCrafter, T2V-CompBench ve benzerleri), model kartları ve tekrarlanabilir topluluk testleriyle. Zamansal tutarlılığın sınırlarını belgele: 8-10 saniyelik klipte nesne kimliğinin, sayının ve geometrinin kaç saniye korunduğu, hangi nesne sınıflarının (ince çizgi, tekrar eden birim, yazı, yüz, kumaş) daha erken bozulduğu, imajdan videoda başlangıç karesinin ne kadar çapa olduğu ve metinden videoya göre farkı — sayısal ölçümle. Yaygın "prompt bilgeliği"nin sınanmış olup olmadığını ayır: "sinematik kelimesi yazma", "kamera markası yazma", "negatif prompt uzun olsun", "35mm film grain gerçekçilik verir", "fizik kuralını cümleyle yazınca model uyar" gibi topluluk kurallarından hangisinin kontrollü testle doğrulandığını, hangisinin yalnız anlatı olduğunu her iddia için kanıt türüyle göster. Karşı yönü araştır: kural eklemenin sonucu KÖTÜLEŞTİRDİĞİ ölçülmüş vakalar — aşırı uzun prompt, çelişen talimatlar, çok sayıda negatif, sayısal kilit yığını — ve modelin bu durumda neyi seçip neyi düşürdüğüne dair bulgular. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz 8-10 saniyelik sabit planlı kliplerdir, prompt gövdesi 2.000-2.600 karakter bandında yazılır ve içinde metin yasağı, bloom yasağı, parçacık fiziği, ekipman durumu ve karakter kilidi gibi zorunlu bloklar taşır — bu yüzden her bulguyu bu uzunluk ve bu blok yapısı için yorumla ve özellikle "bu bloğun ölçülmüş bir etkisi var mı, yoksa yalnız yer mi kaplıyor" sorusuna her blok için ayrı cevap ver. Çıktıyı tablo olarak ver: iddia ya da kural, model ve sürüm, ölçüm yöntemi ve örneklem, sonuç (doğrulandı, çürütüldü ya da ölçülmedi), etki büyüklüğü ve hedef sistemde SİLİNEBİLİR mi; ayrıca "ölçülmemiş ama yaygın" kuralların ayrı listesi ve her biri için deponun kendi başına koşabileceği asgari test tarifi (kaç klip, hangi değişken, hangi ölçüt).
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TUR11_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil; prompt metni başa birebir).
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR 11 açılır: GİRDİ · GİRMEDİ · ZATEN VAR.
   Her sayı ÖLÇÜLMÜŞ · İKİNCİL · ÖNERİ etiketinden birini taşır.
3. ⛔ ÇAPRAZ OKUMA (1↔2 · 3↔4 · 2↔4). Tutmayan sayı İNMEZ.
   ⛔ Ve 4'ün "silinebilir" listesi tek başına silmeye YETMEZ: her
      aday kural önce 01_DERS_ETKINLIK'te kendi filmine bakılarak
      sınanır; deponun ölçtüğü bir ders dış benchmark'la silinmez.
4. Ancak ondan sonra kılavuzlar düzenlenir. 1 → SENARYO §2 ve 06'nın
   döngü kaydı; 2 → KURGU_VE_TESLIM ve KURGU_RITMI; 3 → KARAKTER_VE_DUYGU
   ve DIKEY §4.2; 4 → ⚙️ satırların SİLİNMESİ ya da ölçüm etiketi alması.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dördü de yayınlanmış film sayısının
sıfır olmasını çözmez. Bu dört tur deponun HİPOTEZLERİNİ iyileştirir,
ölçüme çevirmez; ölçüm yalnız ilk gerçek izleyiciyle gelir
(`08_YAYIN_PERFORMANS_TABLOSU`). 3 ve 4'ün en güçlü bulguları bile
deponun kendi klibinde koşulmadan kural sayılmaz.
