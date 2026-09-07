# 🔬 12 — UZAY ÜSSÜ VE İSTASYON MİMARİSİ ARAŞTIRMA PROMPTLARI (04.09.2026)

> **Ne bu dosya:** filmlerdeki uzay üslerini ve istasyonlarını — yörüngede
> ve yüzeyde, dıştan ve içten — **astronota göre doğru ölçekte** ve
> **gerçek mimari mantıkla** yazabilmek için hazırlanmış dört derin
> araştırma promptu. Her biri **altı cümledir** ve **salt prompt** çalışır —
> kopyala, araştırma aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı
> prompt ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki
> turun sonucu karşılaştırılamaz (07/08/09/10/11'in gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin isteği (04.09.2026) — *"uzay üsleriyle ilgili
> yeni bir kılavuz; ölçekler astronotlara göre doğru, genel mimari ve
> yapılar doğru olmalı."* Depoda dört gerçek kesişiyor:
> ① `KILAVUZ_REHBERI` §3 ortam kartları yalnız DIŞ fiziği tutar (vakum ·
> ince atmosfer · kalın atmosfer · itki yerçekimi); **basınçlı İÇ hacim
> için kart yok** — mikro yerçekiminde "yukarı" nedir, ışık nereden gelir,
> duvar neyle kaplıdır yazılı değil.
> ② `DERSLER` **Ders 32** (The Ring Walker — yapı oranları sahneler arası
> kayıyor) çözümü ölçüyü prompta YAZDIRIR; **Ders 138** ise ölçüyü prompt
> gövdesinden ÇIKARIR (model sayıyı yüzeye etiket olarak basıyor). İki
> ders aynı anda uygulanamıyor; ortak birim (gövde boyu) hiçbir yerde
> tanımlı değil.
> ③ `UZAMSAL_HARITA` §4.6 ölçek kilidi kesir dizisini kurar ama kesirin
> hangi gerçek mesafeye ve hangi yapı boyutuna denk geldiği belgesiz —
> THE_COLD_BURN'ün ölçek kayması (dok kapısı genişte dev, yakında oyuncak)
> bu boşluktan çıktı.
> ④ THE_HOLLOW_STATION, THE_RING_WALKER, THE_COLD_WELD gibi filmler
> istasyon/üs anatomisini her seferinde sıfırdan uydurdu; ortak bir
> "istasyon bible"ı yok, dolayısıyla ② DEVAMLILIK merceği yapı için neyi
> kilitleyeceğini bilmiyor.
>
> **KOŞU KAYDI:** ✅ dört prompt 04.09.2026'da koşuldu → dört rapor geldi.
> Ham metinler: `TUR9_HAM_RAPORLAR/` (TAM metin + kaynak listeleri).
> Süzme: `04_ARASTIRMA_BULGULARI.md` §TUR 9.
> Kural indiği yer: `../UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` (açıldı)
> + `../KILAVUZ_REHBERI.md` §3.10 ve §3.7 + `../UZAMSAL_HARITA` §4.6 +
> `DERSLER/05` Ders 32 + `02_RISK_KARTLARI` KART 13 + `prompt_kontrol.py`.
> ⚠️ **Turun sayısal verimi düşüktü:** raporların ölçülerinin büyük kısmı
> denetimde düştü (kafes kirişi · Canadarm2 · Stanford torusu · House Rock ·
> KRUSTY · gezici · FSH · gölge katsayısı). Düşenler süzme kaydında adıyla
> durur. TUR 8 boştur ve 11'in koşusuna rezervedir.

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR n (süzme kaydı) →
         ancak oradan kurulacak UZAY_USSU kılavuzuna ve dokunduğu yerlere
         (UZAMSAL_HARITA §4.6 · Ders 32 · KILAVUZ_REHBERI §3 ortam kartı ·
         IMAGE_VIDEO_PROMPT_TEMPLATES ENVIRONMENT/SPATIAL LOCK).
   Süzme kaydı iki liste tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ BU ARAŞTIRMA "GÜZEL İSTASYON GÖRSELLERİ" DERLEMESİ DEĞİLDİR.
   Aranan şey ilham panosu değil ÖLÇÜ + KAYNAK + ORAN: bir öğenin kaç
   metre olduğu, bunun kaç astronot boyu ettiği ve neden o biçimde
   olduğu. Kaynak "şöyle görünür" diyor ama ölçü ve gerekçe vermiyorsa,
   bulgu süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   Bu turun raporları üç farklı cinsten sayı karıştıracak:
   (a) UÇMUŞ donanımın belgeli ölçüsü (ISS modülü, Apollo iniş aracı),
   (b) KÂĞIT ÜSTÜ programın konsept ölçüsü (Artemis habitatı, Gateway),
   (c) raporun kendi TASARIM ÖNERİSİ.
   Üçü aynı şey değildir; süzme kaydında ayrı etiket taşır (Tur 5
   kuralının genişletilmiş hâli). (c) hiçbir zaman "gerçek" diye inmez.

⛔ ÖLÇÜ PROMPT GÖVDESİNE GİRMEZ [Ders 138].
   Dört promptun dördü de çıktıyı NESNE-GÖRELİ birimle ister ("about
   four body-lengths", "hatch a head taller than her"). Metre cinsinden
   sayı SPEC kilit listesine iner, gövdeye inmez. Bu, Ders 32 ile
   Ders 138'in uzlaştığı tek biçimdir; kılavuz kurulurken 32'nin
   "door height = 2.1m" örneği bu birime ÇEVRİLİR.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Sinema iç mekânı büyütür" bu deponun tahminidir, ölçülmüş yasa değil
   — 3 numaralı prompt bunu iki yönlü sorar (büyütülen VE küçültülen
   vakalar). Üretim kısıtları (tek insan · kesmesiz 8-10 s sabit plan ·
   hareketsiz kamera · okunur metin/rakam/ölçek işareti yok · bloom yok ·
   parçacık süzülmez · çevre statik) hipotez değil FİLTREDİR ve
   promptlara açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — üç çift.
   1 ↔ 4  : dış ölçü ↔ mesafe-kesir tablosu (aynı modül iki raporda
            farklı boyla geçerse sayı İNMEZ).
   1 ↔ 3  : kapak açıklığı ve tutamak aralığı iki raporda da geçer —
            tutmayan sayı çelişki kaydına.
   2 ↔ 3  : yüzey habitatının DIŞ çapı ile İÇ koridor/tavan ölçüsü
            birbirini kapsamalı (iç > dış ise rapor hatalı).
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Yörünge istasyonu — dış anatomi + astronot-göreli oran** | İstasyon "bible"ı yok; hangi dış öğe sayılabilir çapa, hangisi kayar bilinmiyor; dönen istasyonun tek kadrajda döndüğü nasıl okunur yazılı değil | kurulacak UZAY_USSU kılavuzu §dış · `SAHNE_DEVAMLILIK` (yapı kilidi) · `YANASMA_VE_KENETLENME` |
| 2 | **Yüzey üssü (Ay/Mars) — yapı sistemleri + araziye oturma** | Üs yerleşim grameri (habitat-pist-güç-anten mesafeleri) yok; insansız kadrajda üssün "yaşadığı" nasıl okunur (KART 10) tanımsız | kurulacak UZAY_USSU kılavuzu §yüzey · `UZAMSAL_HARITA` kuşbakışı harita · `KILAVUZ_REHBERI` §3.1/§3.2 |
| 3 | **Basınçlı iç mekân — ergonomi, yerel dikey, malzeme** | İç hacim ortam kartı YOK; gerçek iç mekân etiket/ekranla kaplı, depo metni yasaklıyor — inandırıcılık neyle korunur bilinmiyor | `KILAVUZ_REHBERI` §3'e yeni İÇ HACİM kartı · `02_RISK_KARTLARI` KART 5 · `IMAGE_VIDEO_PROMPT_TEMPLATES` ENVIRONMENT |
| 4 | **Ölçek kanıtı grameri — tek sabit planda büyüklük** | §4.6 kesirlerinin gerçek mesafe karşılığı yok; Ders 32 ↔ 138 çelişkisi; vakumda atmosferik perspektif yokken ölçek şahidi ne | `UZAMSAL_HARITA` §4.6 · `DERSLER` Ders 32 revizyonu · `SINEMATOGRAFIK_TEKNIK` (odak/alan derinliği) |

---

# 1️⃣ YÖRÜNGE İSTASYONU — DIŞ ANATOMİ VE ASTRONOT-GÖRELİ ÖLÇEK

```
Gerçek yörünge istasyonlarının dıştan görünür anatomisini birincil kaynaklardan (NASA Reference Guide to the ISS, ESA ve Roscosmos teknik dokümanları, NTRS, uçuş fotoğrafları) ölçüleriyle çıkar: Salyut, Skylab, Mir, ISS'in tek tek modülleri (Zarya, Zvezda, Destiny, Kibo, Columbus, düğüm modülleri, Cupola), bütünleşik kafes kirişi, güneş kanatları, radyatörler, robot kol, Quest ve Poisk hava kilitleri, kenetlenme portları ile Tiangong ve planlanan Gateway, Axiom, Starlab, Orbital Reef için çap, uzunluk, kanat açıklığı, kapak ve port açıklığı, tutamak aralığı değerlerini ver. Her ölçüyü kasklı basınç giysili astronotun ayakta boyuna göre orana çevir (sırt ünitesinin derinliğini ayrı ver): modül çapı kaç gövde boyu, kapak açıklığı kaç, kafes kiriş segmenti kaç, güneş kanadı kaç, tutamak aralığı kaç el genişliği — ve gerçek EVA fotoğraflarında ölçeği en güvenilir okutan eşleşmeleri (robot kol ucundaki astronot ile güneş kanadı, kapak önündeki astronot, kiriş üzerinde yürüyen astronot) örnekleriyle belgele. Silüet tipolojisi çıkar: kafes-ve-modül (ISS), tek gövdeli silindir (Skylab), yıldız biçimli modül kümesi (Mir), tek hat (Tiangong) ve uçmamış dönen biçimler (von Braun tekerleği, Stanford torusu, O'Neill silindiri, halatlı dönüş) — dönen tipler için hangi yarıçap ve devir hangi yapay yerçekimini verir, Coriolis rahatsızlık eşiği kaç devirdir ve kamera sabitken bir yapının döndüğü tek kadrajda hangi ipuçlarıyla (pencere süpürmesi, gölge kayması, kablo eğriliği) okunur, kaynak göstererek açıkla. Yüzey ve yaşlanma katmanını ayrıca belgele: çok katmanlı yalıtım örtülerinin (altın/gümüş kapton) görünümü, beyaz beta kumaşı, mikrometeorit çukurları, ultraviyole sararması, itici lekesi, radyatör beyazlığı, sarı tutamak geleneği — hangi yüzeyler yıllarla nasıl değişir ki yirmi yıllık istasyon yeni istasyondan tek bakışta ayırt edilsin. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz, 8-10 saniyelik sabit planlı AI videodur; hiçbir yüzeyde okunur yazı, bayrak, logo, rakam ya da ölçek işareti bulunamaz, parlama ve bloom sıfırdır (güneş sert bir nokta kaynaktır), yalıtım örtüsü dalgalanamaz ve serbest süzülen enkaz yasaktır — bu yüzden hangi öğelerin büyük, geometrik ve SAYILABİLİR olduğu için (n güneş kanadı, n radyatör, hizada n modül, n port) devamlılık çapası sayılabileceğini, hangilerinin (kablo demeti, örtü kırışığı, anten kümesi) sahneden sahneye kaydığını öncelik sırasıyla ayır. Çıktıyı tablo olarak ver: öğe, gerçek ölçüsü ve kaynağı, astronot-göreli oranı, ait olduğu silüet tipi, sayılabilir çapa değeri, üretimde kayma riski sınıfı ve nesne-göreli birimle yazılmış tek satırlık İngilizce prompt ifadesi; ayrıca her silüet tipi için bir "anatomi kartı" şablonu ekle (modül sayısı, kanat sayısı, radyatör sayısı, port sayısı ve tarafı).
```

---

# 2️⃣ YÜZEY ÜSSÜ (AY / MARS) — YAPI SİSTEMLERİ VE ARAZİYE OTURMA

```
Ay ve Mars yüzey üslerinin yapı sistemlerini gerçek programlar ve uçuş adayı konseptlerden ölçüleriyle çıkar: Apollo iniş aracının yüzeydeki boyutları ölçek referansı olarak, Artemis Base Camp öğeleri (yüzey habitatı, basınçlı gezici, arazi aracı), ESA Moon Village ve SOM tasarımları, NASA 3D-Printed Habitat yarışmasının finalistleri ve regolit sinterleme yapıları, Mars Ice Home, şişirilebilir habitat soyu (TransHab, BEAM, B330, LIFE), lav tüpü ve skylight yerleşimleri, regolit setiyle gömülü modüller, kaynak üretim tesisleri, iniş pisti ve püskürtü seti, kutup güneş kuleleri ve reaktör alanları için çap, yükseklik, duvar kalınlığı, koruma katmanı kalınlığı ve öğeler arası mesafeleri kaynağıyla ver. Her ölçüyü kasklı basınç giysili astronotun ayakta boyuna göre orana çevir — habitat çapı kaç gövde boyu, hava kilidi ve suitport açıklığı kaç, merdiven basamak aralığı kaç, gezici yüksekliği kaç, set yüksekliği kaç, iniş pistinin habitata uzaklığı kaç gövde boyu — ve atmosfersiz yüzeydeki ölçek şahidi sorununu belgele: Apollo mürettebatının krater ve tepe uzaklıklarını neden yanlış tahmin ettiğine dair kayıtlı vakalar ile bir üssün büyüklüğünü uzaktan okutan gerçek görsel ipuçları. Biçimlerin yapısal gerekçesini açıkla: basınç kabının neden silindir, küre ya da torus istediği, radyasyon için regolit koruma kalınlığının ne olduğu, on dört günlük ay gecesinin ısıl döngüsü ile kutup bölgesinin alçak güneş açısının gölgeleri nasıl uzattığı, toz kontrolünün (suitport, hava kilidi ön odası) yerleşimi nasıl belirlediği, Mars'ta düşük basınç ve toz fırtınasının dış yüzeyi nasıl kararttığı — ve yıllar geçmiş bir üssün nasıl göründüğü: aşınmış patikalar, kablo hatları, Ay'da hiç silinmeyen ve Mars'ta tozla örtülen araç izleri. Yerleşim gramerini çıkar: gerçek planlarda habitat, iniş pisti, güç alanı, anten, depo ve "avlu" hangi mesafe ve yön mantığıyla dizilir (püskürtü, görüş hattı, kablo uzunluğu, acil dönüş yolu) ve bir üssün işlevi kadrajda hiç insan yokken yalnız iz, yol, kablo ve nesne dizilimiyle nasıl anlaşılır. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz, 8-10 saniyelik sabit planlı AI videodur; vakumda gölge mutlak siyah ve keskindir, toz asılı kalamaz, ince atmosferde toz yavaş ama kesin çöker, hiçbir yüzeyde okunur yazı, bayrak, logo ya da ölçek işareti olamaz ve bloom sıfırdır — bu yüzden hangi üs öğelerinin sert kenarlı, geometrik ve sayılabilir olduğu için güvenli devamlılık çapası olduğunu, hangilerinin (şişirilebilir yumuşak kabuk, kablo ağı, örtü, gevşek regolit yığını) sahneden sahneye "nefes aldığını" ya da eridiğini sınıflandır. Çıktıyı tablo olarak ver: öğe, gerçek ya da konsept ölçüsü ve kaynağı (uçmuş donanım, kâğıt üstü program ve raporun kendi önerisi ayrı etiketle), astronot-göreli oranı, geçerli ortam (Ay, Mars, ikisi), sayılabilir çapa değeri, kayma riski sınıfı, nesne-göreli birimle tek satırlık İngilizce prompt ifadesi; ayrıca kuşbakışı bir "üs haritası" şablonu ekle — öğeler arası tipik mesafeler gövde boyu cinsinden, güneş yönü ve gölge uzunluğu sütunlarıyla.
```

---

# 3️⃣ BASINÇLI İÇ MEKÂN — ERGONOMİ, YEREL DİKEY, MALZEME

```
Gerçek basınçlı iç hacimlerin ergonomisini ölçüleriyle belgele: ISS laboratuvar modüllerinin standart raf sistemi (bir rafın yükseklik, genişlik ve derinliği, bir duvarda kaç raf), dört duvarlı yerleşimde ışıkla tanımlanan "yerel dikey" geleneği ile Rus segmentinin zemin-tavan ayrımı ve renk düzeni, düğüm kapaklarının biçimi ve açıklığı, tutamak boyu ve aralığı, ayak sabitleyiciler, cırt bant alanları, mürettebat kabininin hacmi, Cupola pencere düzeni, kablo ve hortum yoğunluğu, Skylab'ın büyük iç hacmi, Mir'in kalabalığı ve Tiangong'un temizliği — her satır birincil kaynağa (NASA/ESA dokümanları, iç çekim fotoğrafları, mürettebat anlatıları) dayansın. Yerçekimli habitat iç mekânlarını ayrı çıkar: yüzey habitatı prototipleri ve analog tesisler (HERA, HI-SEAS, MDRS, Aquarius, Concordia, Mars-500, HDU) için koridor genişliği, tavan yüksekliği, ranza, mutfak, hava kilidi ön odası ölçüleri ve mikro yerçekimi iç mekânından farkları (zemin, merdiven, mobilya, "yukarı"nın anlamı) — böylece film her ortam için doğru iç mekân gramerini seçebilsin. Gerçeklik işaretlerini çıkar: deneyimli bir gözün "gerçek istasyon" ile "dekor"u ayırt ettiği ipuçları (dağınıklık yoğunluğu, kablo kelepçeleri, tutamak aşınması, etiket yoğunluğu, panel renk paleti, aydınlatma renk sıcaklığı, fan sesi düzeyi) ve gerçek modüllerin baskın renkleri; özellikle gerçek iç mekânın etiket ve ekranla kaplı olduğu gerçeğini, ekranlar kapalı, salt geometrik desenli ya da hiç yokken inandırıcılığın hangi öğelerle (renk kodlu panel, sayılabilir raf, geometri, aşınma) korunabileceğini araştır. Sinema kalibrasyonu yap: Gravity, Interstellar, The Martian, Ad Astra, For All Mankind, Moon, Europa Report, 2001 ve Apollo 13'te koridor genişliği, kapak boyu, tavan yüksekliği ve raf ölçüsü gerçeğe göre ne kadar büyütüldü, sadeleştirildi ya da tam tersine daraltıldı, yapımcılar bunu hangi algısal gerekçeyle yaptı, eleştiri ve yapım notlarından ölçülü karşılaştırma ver. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz, 8-10 saniyelik hareketsiz kameralı AI videodur; hiçbir ekran, panel, etiket ya da yüzeyde okunur yazı, rakam ve sembol olamaz, bloom sıfırdır ve derinlik yalnız geometri ve ışıkla okunmak zorundadır — bu yüzden yoğun panel dizilerinin, ince kabloların ve tekrar eden rafların sahneden sahneye nasıl bozulduğunu (sayı değişimi, birleşme, erime) belirt, hangi iç mekân öğelerinin büyük, geometrik, sayılabilir ve yüksek kontrastlı olduğu için güvenli çapa olduğunu önceliklendir ve mikro yerçekiminde "yukarı"yı bir promptta nasıl tarif etmek gerektiğini yaz. Çıktıyı tablo olarak ver: öğe, gerçek ölçüsü ve kaynağı, astronot-göreli oranı, yerçekimi rejimi (mikro ya da yüzey), gerçeklik işareti değeri, kayma riski sınıfı ve nesne-göreli birimle tek satırlık İngilizce prompt ifadesi; ayrıca modül başına bir "iç mekân kartı" şablonu ekle (duvar başına raf sayısı, tutamak sayısı, kapak tipi, ışık sıcaklığı, palet).
```

---

# 4️⃣ ÖLÇEK KANITI GRAMERİ — TEK SABİT PLANDA BÜYÜKLÜK

```
Gerçek yaklaşma ve EVA görüntülerinden (Mekik, Soyuz, Dragon ve Cygnus yanaşma videoları, robot kol kameraları, Apollo yüzey filmi, Chang'e iniş kamerası) bir istasyon modülünün, kafes kirişin ya da yüzey habitatının görünür boyutunun mesafeyle nasıl büyüdüğünü ölç: bilinen odak uzaklığında bin metre, iki yüz metre, elli metre, on metre ve iki metreden hedef kare yüksekliğinin kaçta kaçını kaplar, mesafe-kesir tablosu kur ve her satırın kaynağını ver. İnsanı cetvel olarak kalibre et: kasklı basınç giysili astronotun ayakta boyu, kol erişimi, eldivenli elin tutamağa oranı, regolitteki ayak izinin boyu — ve algı literatüründen boyut sabitliği ile tanıdık-boyut ipuçları (insan figürü, kapak, tutamak, basamak) üzerine bulguları topla; atmosferik perspektif ve pusun bulunmadığı vakumda hangi ipuçlarının çalıştığını, Apollo mürettebatının mesafe yanılgılarının neyi öğrettiğini açıkla. Sinema gramerini sök: Gravity, Interstellar, 2001, Ad Astra, The Martian ve First Man tek karede istasyon ya da üssün büyüklüğünü hangi araçlarla kanıtladı — ön plandaki insan, tekrar eden birim (raf, panel, pencere, tutamak), kadrajı taşan kenar, gölge uzunluğu, ışığın gövde üzerinde katettiği yol, yavaş dönen yapının paralaksı, nokta kaynak güneş — ve bunlardan hangileri kamera hareketi ya da kesme gerektirir, hangileri tek kilitli planda çalışır. Bozulma vakalarını belgele: eleştiri ve VFX çözümlemelerinden ölçeğin kırıldığı örnekler (fazla büyük kapak, sahneler arasında küçülen araç, yanlış alan derinliğinin ürettiği "maket" ve tilt-shift etkisi, yumuşak gölgenin cüceleştirmesi) ve derin netlik, sert gölge ile yüzey doku sıklığının neden "büyük" okuttuğuna dair optik ve algısal açıklama. Kritik kısıt: hedef üretim tek insan karakterli, kesmesiz, hareketsiz kameralı 8-10 saniyelik AI videodur; hiçbir yüzeyde okunur ölçü, rakam, çentik ya da işaret olamaz ve ölçü sayısı prompt gövdesine yazılamaz (model onu yüzeye etiket olarak basıyor), bu yüzden her ölçek ifadesi nesne-göreli birimle ("yaklaşık dört gövde boyu") verilmeli ve yaklaşma dizilerinde hedef sahneden sahneye yönelimi sabit kalarak yalnız büyümelidir. Çıktıyı üç parça ver: yapı tipi başına (modül, kafes kiriş, habitat, kapak) 24, 35 ve 50 mm eşdeğer odaklarda mesafe-kesir tablosu; hangi ipucunun hangi mesafe bandında boyutu kanıtladığını gösteren bir "ölçek şahidi merdiveni"; ve nesne-göreli birimle yazılmış tek satırlık İngilizce prompt ifadeleriyle bir bozulma kontrol listesi.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TURn_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil). Tur numarası koşu günü verilir;
   prompt metinleri ham dosyaların başına birebir kopyalanır (Tur 7 usulü).
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR n açılır ve İKİ liste yazılır:
   GİRDİ (hangi bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
   Her sayı ÜÇ etiketten birini taşır: UÇMUŞ · KONSEPT · ÖNERİ.
3. ⛔ Raporlar ÇAPRAZ OKUNUR (1↔4 dış ölçü-kesir · 1↔3 kapak/tutamak ·
   2↔3 dış çap-iç ölçü). Tutmayan sayı kılavuza İNMEZ, çelişki kayda
   geçer. Ders 32'nin "door height = 2.1m" örneği 4'ün nesne-göreli
   birimine çevrilmeden Ders 32 revize edilmez.
4. Ancak ondan sonra kılavuz kurulur: UZAY_USSU_VE_ISTASYON_MIMARISI_
   KILAVUZU.md (dış · yüzey · iç · ölçek kanıtı — dört bölüm, dört
   prompta bire bir). KILAVUZ_REHBERI §3'e İÇ HACİM ortam kartı ancak
   3'ün süzmesi bitince açılır. İstasyon/üs içeren ilk yeni film planı,
   süzme bitmeden yazılmaz.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Uçmuş donanımın ölçüleri birincil kaynaktan gelir ve bağlayıcıdır; konsept
programların ölçüleri revizyona açıktır; sinema karşılaştırmaları ikincil
kaynaktan (eleştiri, yapım notu, VFX çözümlemesi) gelir ve **sayısal iddia
olarak bağlayıcı değildir.** Mesafe-kesir tablosu (4) odak uzaklığı
bilinmeyen kaynaklardan türetilirse etiketlenir, kural sayılmaz. Kılavuza
inen hiçbir oran üretimde test edilmeden kilit sayılmaz; ilk uygulamada
① KARE (ölçek satırı) ve ② DEVAMLILIK (yapı kilidi) skorlarıyla sınanır.
