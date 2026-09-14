# 🔬 18 — OYUNCULUK VE KARAKTER ARAŞTIRMA PROMPTLARI (11.09.2026)

> **Ne bu dosya:** oyunculuk hattı için kurulacak DÖRT kılavuzun
> (`OYUNCULUK_YAZIM` · `KARAKTER_KARTI_VE_DAVRANIS` · `IKI_KISI_VE_AYRILIK` ·
> `DIYALOG_SAHNESI_VE_MUHATAP`) yazılmasından ÖNCE kapatılması gereken dört
> açık soru için dört derin araştırma promptu. Her biri **on cümledir**, her
> cümle **tek satırdır** ve **salt prompt** çalışır — kopyala, araştırma
> aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-17'nin gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahip kararı (11.09.2026) — oyunculuk üzerine dört
> kılavuz. Tetikleyen ölçüm: ⑩ OYUNCULUK koşulan on filmin onu 2,0-6,3
> bandında, dördü `THE CHOICE IS INVISIBLE` (T10 · D202); Character Bible
> karakter taşımıyor (`06` §1.4); iki insanlı planlarda AYRILIK yazılıyor
> ama ekranda okunup okunmadığını ölçen mercek yok; replik tablosu SATIRI
> yazıyor, iki replik ARASINI kimse yazmıyor. Ölçüm tarafı tam
> (`10_OYUNCULUK` rubriği · `DIALOGUE_CRITIQUE`), yazım tarafı boş.
>
> **KOŞU KAYDI:** ✅ **11.09.2026 koşuldu → 4/4 rapor geldi.** Ham metinler BİREBİR
> `TUR15_HAM_RAPORLAR/` altında (her dosyanın başında koşulan prompt), süzme
> `04_ARASTIRMA_BULGULARI.md` §TUR 15 (43 giren · 14 girmeyen sınıfı · 4 çapraz çift).
> ⚠️ Kaynak listeleri araştırma aracından BOŞ geldi; zincir yazar+yıl ile yeniden
> kuruldu — yeniden koşulacaksa kaynak listesi İSTENİR.
> ✅ Süzmeden sonra dört kılavuz yazıldı (aynı gün): `KARAKTER_KARTI_VE_DAVRANIS` ·
> `IKI_KISI_VE_AYRILIK` · `DIYALOG_SAHNESI_VE_MUHATAP` · `OYUNCULUK_YAZIM`.

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR 15 (süzme kaydı) →
         ancak oradan dört yeni kılavuza ve dokundukları yerlere
         (KARAKTER_VE_DUYGU · SES_VE_DIYALOG · FILM_PLAN/QA_SPEC şablonu ·
         10_OYUNCULUK rubriği · DIALOGUE_CRITIQUE). Süzme kaydı İKİ liste
         tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ BU ARAŞTIRMA "İYİ OYUNCULUK ÖRNEKLERİ" DERLEMESİ DEĞİLDİR.
   Aranan şey hayranlık değil MEKANİZMA + EŞİK + TEST: bir bedenin niyeti
   neden okuttuğu, hangi büyüklükte okunmaz kaldığı, hangi büyüklükte
   abartı olduğu. "Şöyle oynayın" diyen ama neden/ne kadar/nasıl ölçüldü
   demeyen kaynak süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) ÖLÇÜLMÜŞ — deneysel / korpus / göz izleme / hakemli ölçüm
   (b) UYGULAMA — yönetmen, oyuncu, koreograf, yapım notu, kuram kitabı
   (c) ÖNERİ    — raporun kendi tasarım önerisi
   Kaynaksız (a) düşer; (b) ancak iki bağımsız uygulayıcı aynı şeyi
   söylüyorsa iner; (c) yalnız ⬜ HİPOTEZ etiketiyle iner.

⛔ ÖNCEKİ TURLARLA ÇAKIŞMA — yeniden istenmeyenler ("ZATEN VAR").
   • Bedenden duygu okuma hiyerarşisi (öfke/üzüntü/mutluluk iyi, korku/
     iğrenme zayıf · yüz-beden çelişkisinde beden kazanır · dorukta yüz
     ayırt etmez · görünür nefes) → TUR 11. 1 numaralı prompt DUYGU
     sormaz, NİYET ve KARAR sorar.
   • "Umursamadım"ın üç sebebi (istek · bedel · muhatap), akuzmatik ses,
     bedenleştirme, çıkarılabilir an → TUR 4. İstenmez.
   • Replik kalitesi ölçütleri, on-the-nose, alt metin, bilgi=silah,
     konuşma İngilizcesi, çeviri kokusu, hakem güvenilirliği → TUR 6.
     4 numaralı prompt SATIRI değil, iki satır ARASINI sorar.
   • Muhatap tipolojisi (kayıt cihazı · cevapsız telsiz · nesne · hayali
     · monolog), konuşma yoğunluğu ve ters-U eğrisi, 10 s'ye sığan kelime
     tavanı, lip-sync MCU tabanı → TUR 13. İstenmez.
   • Mizahın tehlike SONRASINA yerleşimi (uyarma transferi), yetkinlik +
     sıcaklık → TUR 14. İstenmez.
   • Göz bütçesi, Kuleshov döngüsü sayıları, el/yürüyüş/eşya yüzdeleri →
     KARAKTER_VE_DUYGU'nun kaynağı (araştırmalar/2.md). İstenmez.
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer,
   kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "En yavaş jest en önemli anda", "reddedilen seçenek kadrajda olmalı",
   "sessizlik cevaptır", "alışkanlık seçimde kırılır" bu deponun
   TASARIM ADAYLARIDIR, kanıtlanmış yasa değil — dördü de sorulara
   tarafsız ve İKİ YÖNLÜ yazıldı (abartının çöktüğü vakalar, donukluğun
   işe yaradığı vakalar, sessizliğin "donma" okunduğu eşik de istenir).
   Üretim kısıtları hipotez değil FİLTREDİR ve her promptun dokuzuncu
   cümlesinde açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — dört çift.
   1 ↔ 2 : 2'nin karar mimarisi (alternatif görünür mü, deneme sayısı,
           bedel gecikmesi) ile 1'in "önce/sonra gövde" eşiği AYNI vuruşu
           iki düzeyde tarif eder; sayılar tutmuyorsa hiçbiri inmez.
   1 ↔ 4 : 4'ün "dinleyenin bedeni" bulgusu 1'in kanal tablosuna
           oturmalı — dinleyen kadrajı bir niyet kanalıdır ya da değildir.
   2 ↔ 3 : 3'ün "iki figürü ayıran asgari fark" listesi 2'nin karakter
           kartı satırlarından çıkmalı; çıkmıyorsa kart eksiktir.
   3 ↔ 4 : 3'ün SÖZSÜZ cevap tipolojisi (uyma/ret/erteleme/karşı teklif)
           ile 4'ün SÖZLÜ cevap tipolojisi aynı iskelet olmalı; iki rapor
           iki farklı tipoloji getirirse ikisi de inmez, çelişki kayda geçer.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Niyet, tereddüt, karar ve sonrası BEDENDE** | D202'nin çözümü tek cümle ("mikro-beden zorunlu"); efor için kanal sözlüğü var (D169), niyet için yok; TIMELINE NEREDE/NE yazıyor, NASIL sormuyor; "durur ve bekler" manken üretiyor (ADAY-26/41/84/85) | `OYUNCULUK_YAZIM_KILAVUZU` (kurulacak) · QA_SPEC ÇAPA ÜÇLÜSÜ · `prompt_kontrol` niyet kanalı kapısı adayı |
| 2 | **Karakter kartı ve davranış tutarlılığı** | Character Bible süreklilik şartnamesi, karakter değil (`06` §1.4); Karakter sütunu 2-4 platosu; dikeyde "seçim" bir duruş değişikliği (`05` §2.4); ilk/son eylem farkı hiç ölçülmedi | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU` (kurulacak) · FILM_PLAN KARAKTER KARTI bloğu · QA_SPEC davranış şeridi |
| 3 | **İki kişi: fark, sözsüz cevap, mesafe** | 20/97 filmde iki insan, AYRILIK ~10 planda tek satır; "onay + karar = tek kişi iki gövde" (`06` §1.5); ⑩'da iki kişilik kategori yok; PROB A koşulmadı; kim solda kilidi tutmadı (Third Dune) | `IKI_KISI_VE_AYRILIK_KILAVUZU` (kurulacak) · B5b AYRILIK KARTI · ⑩ rubriğine iki-kişi satırı (kart G yaması) |
| 4 | **Diyalog sahnesi: hamle, cevap, dinleyen, değişim** | Replik tablosu satırı yazıyor (register · süre · işlev), iki replik ARASI yazılı değil; sessizliğin cevap olduğu eşik, eylemle cevap, dinleyenin kadrajı hiçbir kılavuzda yok; replikli üretilmiş beş filmde ses merceği repliği yanlış duydu, kimse dinleyeni okumadı | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU` (kurulacak) · REPLİK TABLOSU'na HAMLE/CEVAP/DEĞİŞİM · `DIALOGUE_CRITIQUE` T9 adayı |

> ⚠️ **1 ile 4, 2 ile 3 birbirini denetler** (yukarıdaki çapraz okuma). Bir
> raporun getirdiği eşik ötekinde tutmuyorsa kılavuza ancak ⬜ HİPOTEZ
> etiketiyle iner, sayısız iner.

---

# 1️⃣ NİYET BEDENDE — tereddüt, karar, sonrası ve tempo nasıl okunur, nasıl yazılır

```
Bir insanın NİYETİNİN, TEREDDÜDÜNÜN ve KARARININ yüz görünmeden ve tek kelime söylenmeden yalnız gövdesinden okunabildiğini gösteren deneysel çalışmaları topla: uzanma ve kavrama kinematiğinden niyet okuma (hareketin hızı, yörüngesi ve el açıklığından "ne yapacak" tahmini), hareket öncesi hazırlık işaretleri (ağırlık aktarımı, bakışın eli kaç milisaniye öncelediği, gövdenin hedefe dönmesi), gözlemcinin doğruluk oranı ve hangi ipucunun belirleyici olduğu — her sayıyı kaynağı, tarihi ve türüyle ver.
TEREDDÜDÜN hareket biçimini sayıyla tanımla: durma-yeniden başlama, yarım uzanma, hız düşüşü, yanlış başlangıç ve geri çekilme gibi kalıpların her birini gözlemcinin kaç milisaniyelik bir duraklamada "kararsızlık" olarak okuduğunu, hangi eşiğin altında duraklamanın hiç fark edilmediğini ve hangi eşiğin üstünde abartı ya da "donma" olarak okunduğunu belgele.
Bir kararın ÖNCESİ ile SONRASI arasında gövdede hangi ölçülebilir fark oluşur — duruş, omuz hattı, ağırlık merkezi, el gerginliği, baş yönü, nefes — ve izleyicinin "karar verdi" demesi için bu farkın ne kadar büyük olması gerektiğine dair algı eşiği çalışmaları, oyuncu ve yönetmen tanıklıkları ve sahne pratiği var mı, iki yönlü sor: farkın hiç okunmadığı vakalar ile fazla büyük olup melodram okunduğu vakalar.
Bir olaydan (çaba, kayıp, korku, başarısızlık) SONRA gövdenin o olayı kaç saniye "taşıdığını" araştır: duruşun nötre dönme süresi, kurguda tepkinin bir sonraki plana taşınması, izleyicinin ani sıfırlanmayı (bir planda çökmüş, sonrakinde dimdik) fark edip etmediği ve bunu devamlılık hatası mı yoksa zaman atlaması mı olarak okuduğu — ölçülmüş çalışma, kurgu kuramı ve yapım notu ayrı ayrı.
DURGUNLUK ile DONUKLUK ayrımını ölç: canlı bir bedenin hareketsiz dururken sergilediği mikro-hareketler (postural salınım, göz kırpma, nefesle omuz/göğüs hareketi, parmak mikro-ayarı) hangi genlik ve frekanstadır, bunların yokluğu izleyicide "manken, cansız, yapay" okuması üretiyor mu, tekinsiz vadi ve yapay hareket algısı literatürü bunu hangi eşikte ölçmüştür ve tersine, tamamen hareketsiz bir figürün bilinçli olarak güçlü çalıştığı belgelenmiş vakalar hangileridir.
TEMPO'yu araştır: jest hızının anlam taşıdığına (yavaşlayan jest ağırlık, hızlanan jest telaş) dair ölçüm var mı, bir film boyunca jest hızının değişmemesinin izleyici tarafından fark edilip "düz" okunduğu belgelenmiş mi, en yavaş ya da en uzun tutulan jestin dramatik ağırlıkla ilişkisi kuramda ya da ölçümde nasıl tarif edilmiş ve bu kuralın tersine işlediği (en önemli anın en hızlı jestle geçtiği) vakalar var mı.
Oyunculuk ve hareket kuramlarının (Stanislavski hedef-engel, Meisner tepki, Laban çaba nitelikleri, Lecoq, Michael Chekhov psikolojik jest, Delsarte) niyeti bedene çeviren SOMUT ve SAYILABİLİR yönergelerini topla — "önce dur sonra git", "nesneye bak, sonra ele bak", "ağırlığı arka ayağa al" gibi sahne yönetmeni talimatlarının belgelenmiş biçimleri ve hangi kaynağın hangi talimatı verdiği.
Metinden ve görselden video üreten modellerde (Veo 3.x, Kling, Runway, Sora, Hailuo, Omni ve benzerleri) beden dili ile jest ZAMANLAMASININ metinle ne ölçüde kontrol edilebildiğini araştır: "hesitates", "slowly", "stops, then reaches", "holds still" gibi ifadelerin çıktıda ölçülmüş etkisi, insan hareketi ve zamanlama üzerine yayınlanmış benchmark sonuçları, modellerin nedensiz dolgu jesti ya da donuk figür üretme eğiliminin belgelenip belgelenmediği ve hangi ifade biçimlerinin (fiil, süre, sayı, olumsuz cümle) işe yarayıp hangilerinin yaramadığı.
Kritik kısıt: hedef sahneler on saniyelik kesmesiz tek plandır, kamera sabittir, kadrajda tek ya da iki insan vardır, yüz çoğu zaman kapalı bir kask vizörünün ardında ya da kadrajdan uzaktadır, basınç giysisi parmakları ve boyun dönüşünü kısıtlar ve söz çoğu zaman yoktur — bu yüzden yüz mimiğine, kamera hareketine, sahne içi kesmeye ve diyaloga dayanan çözümleri işaretleyip ele; gövde, el, baş yönü, tempo ve nesneye mesafeyle çalışanları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KANAL tablosu — kanal (tereddüt / bırakma / ağırlık / bakış / tempo / mesafe / kalıntı duruş), ölçülebilir değişkeni, izleyicinin okuma eşiği (alt ve üst), kaynağı, türü ve tarihi; (b) her kanal için sayı içeren İngilizce tek satırlık "ÖNCE / SONRA" örnek çifti; (c) motor tablosu — motor, işe yarayan ifade biçimi, yaramayan ifade biçimi, ölçüm kaynağı; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ KARAKTER KARTI — bu insan kim, film boyunca neden böyle davranıyor

```
Sözsüz ya da az sözlü kısa filmlerde izleyicinin ekrandaki figürü bir "karakter" olarak kurmasını sağlayan EN AZ bilgi kümesini araştır: rol, istek, alışkanlık, sınır, korku ve baskı altındaki tepki gibi özniteliklerden hangilerinin karakter algısı ürettiğine dair anlatıbilim, film kuramı (tanıma / hizalanma / bağlanma ayrımı gibi modeller) ve zihin kuramı çalışmaları ne söylüyor, hangi öznitelik yokken izleyici figürü "kamera taşıyıcısı" ya da "figüran" olarak okuyor — kaynağı, tarihi ve türüyle.
ALIŞKANLIK ya da MOTİF JESTİNİ ölç: bir karaktere ait tekrarlayan kişisel jestin (sahne işi, tik, ritüel) karakterleştirme etkisi, izleyicinin bunu kaç tekrarda "o kişiye ait" olarak kaydettiği, tekrarın hangi noktada anlamsız dolguya dönüştüğü, ve o alışkanlığın bir kez KIRILMASININ dramatik işaret olarak nasıl ve hangi filmlerde kullanıldığı — kuram, yapım notu ve varsa ölçüm.
KARAR MİMARİSİNİ araştır: bir eylemin izleyici tarafından "seçim" olarak okunması için reddedilen seçeneğin de görünür olması gerekiyor mu, alternatifin kadrajda bulunmasıyla bulunmamasının etkisi ölçülmüş mü, seçimden önce kaç başarısız deneme gerilimi kurar ve kaçından sonra bıkkınlık üretir, seçimin bedelinin seçimden ne kadar sonra görünmesi gerektiğine dair kural ya da ölçüm var mı — iki yönlü sor: alternatifsiz "seçim"in yine de çalıştığı vakalar da istenir.
TUTARLILIĞI ölç: karakter davranışının tutarlılığı ile "bu insan bunu yapmaz" tepkisi arasındaki ilişki, hangi davranış ihlallerinin izleyiciyi kopardığı ve hangilerinin gelişme olarak okunduğu, karakter inandırıcılığı ya da tutarlılığı için yayınlanmış herhangi bir ölçme aracı (anlatı araştırması, etkileşimli drama, oyun karakterleri için) var mı, maddeleri neler ve hakemler arası uyuşması ölçülmüş mü.
YAY ile AN arasındaki farkı süreye bağla: kısa filmde karakter değişiminin "karakter anı" (tek bir dönüş) ile klasik yay arasında nasıl konumlandığı, bir dakikalık, dört dakikalık ve yirmi dakikalık işlerin taşıyabildiği değişim miktarı, ilk eylem ile son eylem arasındaki farkın izleyici tarafından okunup okunmadığı ve "hiç değişmedi" ile "sebepsiz değişti" eleştirilerinin hangi yapısal eksiklikten doğduğu — örnek, eleştiri kanıtı ve varsa ölçüm.
DUYGUNUN KAYNAĞINI sor: bir tepkinin sahnedeki bir OLAYA bağlı olmasıyla olaysız gelmesi (takvime bağlı, sebepsiz duygu) arasındaki fark izleyicide nasıl okunuyor, "sebepsiz duygu" ve "gecikmiş tepki" tespitleri eleştiride ve algı çalışmalarında nasıl tarif edilmiş, tepkinin olaydan ne kadar önce ya da sonra gelmesi kabul edilebilir ve hangi noktada yapaylık okunuyor.
İSİMSİZ ve YÜZSÜZ kahramanı araştır: adı hiç geçmeyen ve yüzü kask, maske ya da mesafe yüzünden okunmayan karakterlerle izleyici bağının kurulduğu belgelenmiş vakalar ve ölçümler, hangi ikame kanalların (ekipman, alışkanlık, kişisel nesne, yürüyüş, karar) işe yaradığı, hangilerinin başarısız olduğu ve bu figürlerin "karakter" değil "avatar" okunduğu eleştirilerin ortak sebebi.
TEK KİŞİLİK anlatıda karakterin iç yaşamının dışa vurumunu incele: karakterin kendi geçmiş kararı, kendi bedeni ve bir nesneyle ilişkisi üzerinden kurulduğu filmlerde (denizde, uzayda, çölde yalnız kalan kahramanlar) bu üç kanalın kaç sahneye yayıldığını, hangi sırayla açıldığını, eleştirinin karakteri "boş" ya da "dolu" bulduğu vakaların farkını ve karakterin bir şeyi ANLADIĞI anın bedenle nasıl gösterildiğini zaman damgasıyla belgele.
Kritik kısıt: hedef filmlerde okunur metin, isim, dış ses ve geriye dönüş yoktur, yüz çoğu zaman kask arkasındadır, her sahne on saniyelik kesmesiz tek plandır ve kadrajda bir ya da iki insan vardır — bu yüzden diyaloga, anlatıcıya, ekran metnine, yüz mimiğine ve çok karakterli tepkiye dayanan karakterleştirme çözümlerini işaretleyip ele; ekipman, jest, nesne, karar ve mesafeyle kurulanları öncelikle.
Çıktıyı üç yapı ve iki liste olarak ver: (a) "KARAKTER KARTI" için asgari öznitelik listesi — her satırın adı, izleyiciye hangi kanalla ulaştığı, kaç sahnede kurulması gerektiği, kaynağı ve etiketi; (b) karar mimarisi tablosu — alternatif görünürlüğü, başarısız deneme sayısı bandı, bedel gecikmesi, kaynağı; (c) bulunan tutarlılık ve inandırıcılık ölçme araçlarının maddeleri aynen; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 3️⃣ İKİ KİŞİ — fark, sözsüz cevap, mesafe ve ayrılığın bedeli

```
İki kişilik SÖZSÜZ bir sahnede anlaşmazlığın nasıl kurulduğunu araştır: kişilerarası mesafe bantları, gövde yönelimi (yüz yüze, aynı yöne, zıt yöne), temas ve temas reddi, statü işlemleri, baskınlık ve yakınlık okumaları — izleyicinin iki figür arasındaki ilişkiyi yalnız mesafe ve duruştan hangi doğrulukla okuduğuna dair deneysel çalışmalar, hangi değişkenin (mesafe mi, yönelim mi, yükseklik mi) en güçlü olduğu ve sayıların kaynağı, tarihi, türü.
Bir isteğe ya da teklife verilen SÖZSÜZ CEVABIN türlerini çıkar — uyma, reddetme, erteleme, karşı teklif, görmezden gelme — her türün beden işaretlerini (yarım jest, geri çekilen el, duraklama, yön değiştirme, nesneyi bırakma) ve konuşma analizindeki "tercih edilmeyen cevap" gecikmesinin beden karşılığını belgele: izleyici kaç saniyelik gecikmeyi "ret" olarak okur, kaç saniyeden sonra "anlamadı" ya da "donma" olur.
İki figürün izleyici tarafından iki AYRI kişi ve iki ayrı irade olarak okunması için gereken asgari görsel ve davranışsal farkı ölç: benzer giysili iki figürün hangi noktada "aynı kişi" ya da "ikiz" okunduğu, sinema ve tiyatroda iki figürü ayrıştırma pratikleri (siluet, ölçek, tempo, alışkanlık jesti, taşınan nesne), ve iki figürün aynı anda aynı şeyi yapmasının izleyicide "tek irade" okuması ürettiğine dair kanıt.
İki kişilik sahnenin BLOKLAMASINI araştır: kim nesneye yakın, kim önde ya da arkada, yükseklik farkı, kadrajın iki yarısının kullanımı gibi mizansen kurallarının kaynakları (sahne yönetimi kitapları, yönetmen notları, görsel kompozisyon kuramı), ekran yönü ve 180 derece hattının iki figürde ihlal edildiğinde izleyicinin "yer değiştirdiler" okuması yapıp yapmadığı ve bunun ölçülüp ölçülmediği.
İLİŞKİNİN MESAFE OLARAK anlatıldığı vakaları incele: film boyunca iki figür arasındaki mesafenin ve yönelimin değişimiyle yakınlaşma ya da kopuşun taşındığı iki kişilik filmler, dans ve mim işleri, sessiz sinema örnekleri — mesafe eğrisi ölçülmüş mü, izleyici bu değişimi fark ediyor mu, yakınlaşmanın hangi hızda "kazanılmış" hangi hızda "sebepsiz" okunduğu.
Sözsüz ya da az sözlü iki kişilik anlaşmazlığın ÇÖZÜM tiplerini ve bedelini araştır: biri boyun eğer, ikisi de değişir, çözülmez ama eyleme dönüşür, bir üçüncü nesne kararı verir — hangisinin izleyicide tatmin ya da hatırlanma ürettiği, çözümün bir bedel taşımadığında nasıl okunduğu, kısa filmde iki kişilik bir anlaşmazlığın kurulup çözülmesi için gereken sahne ve saniye bütçesinin ölçülmüş ya da önerilmiş değeri.
Yapay zekâ video üretiminde aynı kadrajda İKİ insanın belgelenmiş arızalarını topla: kimlik sızması ve karışması, bir figürün kopyalanması, taraf değiştirme, bir figürün kaybolması, iki figürün aynı jesti senkron yapması — benchmark ve değerlendirme çalışmalarında ölçülmüş oranlar, iki figürü ayrı tutan prompt stratejilerinin (ayrı ve zıt tarif, konum kilidi, referans görsel, tek figürlü klip + kurgu) ölçülmüş etkileri ve motorlar arası farklar.
İki insanın fiziksel etkileşimini (tutma, itme, çekme, sarılma) tarif eden promptların motorlarda reddedilme ya da bozulma davranışını ve temassız anlaşmazlık için belgelenmiş çözümleri (nesne üzerinden mücadele, mesafe, sırt dönme) araştır — iki yönlü: temasın sorunsuz üretildiği vakalar da istenir.
Kritik kısıt: hedef sahneler on saniyelik kesmesiz tek plandır, kamera sabittir, iki insan da basınç giysili ve kasklıdır (yüz çoğu zaman kapalıdır), söz varsa çoğu zaman telsizden ve kadraj dışından gelir, okunur metin yoktur — bu yüzden yüz mimiğine, karşılıklı çekim kesmesine, fiziksel kavgaya ve diyalog yoğunluğuna dayanan çözümleri işaretleyip ele; mesafe, yönelim, temas reddi ve ortak nesneyle kurulanları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) CEVAP TİPİ tablosu — tip, beden işareti, okuma eşiği, sayı içeren İngilizce tek satırlık örnek, kaynak; (b) MESAFE ve YÖNELİM tablosu — değişken, izleyicinin ilişki okuması, eşik, kaynak, tarih, tür; (c) yapay zekâ İKİ-KİŞİ tablosu — arıza, ölçülmüş oran, işe yarayan strateji, motor, kaynak; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 4️⃣ DİYALOG SAHNESİ — hamle, cevap, dinleyen ve değişim

```
Diyalog sahnesini tek tek REPLİK olarak değil DEĞİŞ-TOKUŞ birimi olarak inceleyen kaynakları topla: konuşma analizinde bitişik çiftler (soru-cevap, teklif-kabul ya da ret), tercih edilmeyen cevabın gecikme ve yumuşatma yapısı, sıra alma boşluklarının milisaniye cinsinden ölçülmüş süreleri, ve dramatik yazımda "vuruş" modellerinin (hamle → tepki → değişim) tanımları — hangi kaynak, hangi tarih, hangi tür.
SESSİZLİĞİN CEVAP olarak okunmasını ölç: bir replik cevapsız kaldığında izleyici bunu kaç saniyelik boşluktan sonra "cevap vermedi" olarak okur, kaç saniyeden sonra "kurgu hatası" ya da "donma" olur, cevapsız çağrı, cevap vermeyen alıcı ve geciken cevap vakalarının dramaturjisi hangi filmlerde nasıl kurulmuş ve izleyici tepkisi ölçülmüş mü.
EYLEMLE CEVAP verilen sahneleri araştır: bir söze sözle değil bir eylemle (nesneyi bırakmak, sırtını dönmek, işe devam etmek) cevap verilen sahnelerin izleyici tarafından cevap olarak okunma koşulları, eylemin sözden ne kadar sonra gelmesi gerektiği ve bu kalıbın kuramda nasıl adlandırıldığı — örnek ve varsa ölçüm.
DİNLEYENİ ölç: diyalog sırasında izleyicinin gözünün konuşana mı dinleyene mi gittiğine dair göz izleme çalışmaları, tepki planının ölçülmüş etkisi, dinleyenin bedenindeki değişimin anlam üretimi (nötr bir dinleyen yüzüne ya da gövdesine komşu repliğin anlamının atfedilmesi), ve konuşan kadraj dışındayken sahnenin tamamen dinleyenin yüzü ya da gövdesi üzerine kurulduğu filmlerin belgelenmiş etkisi.
SÖZ ile JEST arasındaki zamansal ilişkiyi araştır: jestin sözü kaç milisaniye öncelediği ya da izlediği, söz ile beden çeliştiğinde izleyicinin hangisine inandığı, sonradan eklenen sesle (dublaj, post-senkron) bu ilişkinin hangi koşullarda korunduğu ve hangi gecikmenin fark edildiği — konuşma-jest literatürü ve ses post-prodüksiyon kaynakları ayrı ayrı.
DEĞİŞİMİ tanımla: bir diyalog sahnesinin "işe yaradığını" söyleyen ölçüt ne — sahne sonunda bilgi, güç, mesafe ya da niyet durumunun değişmesi — değişim üretmeyen diyalogun eleştiride nasıl adlandırıldığı, senaryo değerlendirme pratiğinde sahne düzeyinde değişimi ölçen yayınlanmış bir araç ya da soru seti var mı ve maddeleri neler.
AZ REPLİKLİ sahneyi ölç: sahne başına bir ya da iki replikle çalışan filmlerde bir değiş-tokuşun kaç sahneye yayıldığı, bir repliğin cevabının başka bir sahnede gelmesinin etkisi, iki üç kelimelik repliklerin taşıdığı yük ve bir filmdeki toplam replik sayısı ile izleyici bağı arasında ölçülmüş bir ilişki olup olmadığı — iki yönlü: az repliğin "boş" okunduğu vakalar da istenir.
ÜRETİM tarafını sor: tek klipte tek konuşmacı kısıtı altında karşılıklı diyalogun iki ayrı klipte üretilip kurguda birleştirilmesinin belgelenmiş yöntemleri, sesin sonradan eklendiği durumda dinleyen tepkisinin senkronu, ve yapay zekâ video modellerinde konuşan-dinleyen sahnelerinin ölçülmüş arızaları — dinleyenin ağzının oynaması, yanlış figürün konuşması, dinleyenin boş bakışı, iki figürün aynı anda konuşması — hangi motorda hangi oranda ve hangi prompt biçimiyle azaldığı.
Kritik kısıt: hedef sahneler on saniyelik kesmesiz tek plandır, kamera sabittir, tek klipte tek konuşmacı vardır, her replik beş saniyenin altındadır, ağız çoğu zaman kadrajda değildir (kask, telsiz, arkadan çekim), altyazı ve okunur metin yoktur — bu yüzden hızlı karşılıklı kesmeye, uzun tiratlara, üst üste konuşmaya ve altyazıya dayanan çözümleri işaretleyip ele; kadraj dışı ses + dinleyen kadrajı, sessiz cevap ve eylemle cevapla çalışanları öncelikle.
Çıktıyı üç yapı ve iki liste olarak ver: (a) DEĞİŞ-TOKUŞ BİRİMİ şablonu — hamle, cevap tipi (söz / sessizlik / eylem / makine), değişim — ve her cevap tipi için ölçülmüş süre eşiği ile kaynağı; (b) DİNLEYEN KADRAJI tablosu — hangi koşulda konuşan yerine dinleyen gösterilir, etkisi, kaynak, tarih, tür; (c) yapay zekâ KONUŞAN-DİNLEYEN tablosu — arıza, oran, işe yarayan biçim, motor, kaynak; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TUR15_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil). Prompt metinleri her ham
   dosyanın başına birebir kopyalanır (Tur 7 usulü).
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR 15 açılır ve İKİ liste yazılır:
   GİRDİ (bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
   Her sayı ÜÇ etiketten birini taşır: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ.
   TUR 4/6/11/13/14'te zaten inen bulgular "ZATEN VAR" etiketiyle geçer.
3. ⛔ Raporlar ÇAPRAZ OKUNUR (1↔2 · 1↔4 · 2↔3 · 3↔4). Tutmayan eşik
   kılavuza İNMEZ, çelişki kayda geçer. Özellikle 3↔4: iki cevap
   tipolojisi TEK iskelete indirilemiyorsa iki kılavuz da o bölümü
   ⬜ HİPOTEZ olarak taşır.
4. Ancak ondan sonra dört kılavuz yazılır — sırası: KARAKTER_KARTI →
   IKI_KISI → DIYALOG_SAHNESI → OYUNCULUK_YAZIM (her biri bir öncekinin
   kartını kullanır). Şablon/rubrik/betik dokunuşları (FILM_PLAN ·
   QA_SPEC · 10_OYUNCULUK · DIALOGUE_CRITIQUE · prompt_kontrol) ayrı
   iştir ve kart G/P usulüyle işlenir; kılavuz onların METNİNİ hazırlar.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Niyet, tereddüt ve cevap eşikleri laboratuvar uyaranlarıyla ya da insan
eliyle çekilmiş, kesmeli, yüzü açık yapımlarla ölçülmüştür; on saniyelik
sabit plan, kapalı vizör ve yapay zekâ üretimi altında hiçbir eşik
üretimde sınanmadan bağlayıcı değildir. Motor tabloları en hızlı
bayatlayan kısımdır (TUR 12 emsali). ⛔ Dört kılavuzun ilk gerçek sınavı,
ÇAPA ÜÇLÜSÜ yazılmış ilk filmin ⑩ mod D koşusudur — o koşu yapılmazsa
bu tur bir varsayım olarak kalır.
