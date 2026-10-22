# 🎬 BLACK_ACCORD — Kara Uzlaşma

```
FILM           BLACK_ACCORD
FORMAT         yatay 16:9
HEDEF_SURE     16:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/BLACK_ACCORD/
URETIM         sahip planı: görseller GPT Image (başlangıç karesi, "Görsel girdisi o klip için üretilmiş başlangıç karesidir"), video 10 s görselden video (plan: "kullanılan arayüzün mevcut oran, süre ve ses seçenekleri uygulanır") · ön plan konuşmacısı videoda konuşur (model sesi), ikinci ses kurguda (plan) → Flow/Gemini "Return silent videos" KAPALI · QA Gemini uygulaması
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `FIZIK_IDDIASI yok`: plan zaman farkını kurmaca sayar — "Bu oran hesaplanmış bir astrofizik sonucu veya NASA verisi olarak sunulmaz; dramatik
> dünya kurulumudur." Kara delik görünüşü planın görsel dayanağıdır (NASA — Black Hole Anatomy), iddia değildir. Görüntüde uzay fiziği
> `uretim_hatti/UZAY_FIZIGI_GORUNTU_KILAVUZU.md` ile yazılır (vakumda ses yok — plan da aynısını söyler).
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md` (sahibin verdiği plan, 18.10.2026, birebir; düzenlenmez).**
> **Sahip talimatı (18.10.2026): "plandan asla dışarı çıkma".** Bu dosyada olay, sıra, kadraj türü, özne, eylem, nesne durumu, oturma düzeni,
> 171 replik, ses davranışı, müzik ve kapak **planın kendisidir**. Fable'ın eklediği yalnız biçimdir: sütunlar, referans numaraları
> (A01→1 … A09→9), §5 saniye/süre tahmini, kaynak sütunu (planın "ön planda bir konuşmacı" kuralından), §6 yatak/geçiş tablosu.
> Hat kuralıyla plan çatışırsa: SÖZLEŞME/ARAÇ (film_dogrula M) yalnız biçim olarak uygulanır, içerik değişmez; HİPOTEZ/TERCİH plan lehine
> bırakılır ve `NOTLAR.md` KARARLAR'a yazılır; plan içi çelişki sahibe sorulur (`ODA/DURUM.md` SAHİP CEVAPLARI · K satırları).
> Faz 1-4 ajan turu açılmadı (THE_FURNACE_GATE yolu; `ODA/DURUM.md` AŞILAN KAPILAR).

---

## 1. HİKÂYE

```
LOGLINE   Kara deliğin yakınındaki tarafsız bir istasyonda dört uygarlığın elçileri barış görüşürken, genç bir dil uzmanı resmî tercümanın barış cümlelerini savaş emirlerine dönüştürdüğünü fark eder.
AMAÇ      Nem (plan: "İlk başta görevini doğru yapmak; sonra özgün sözün duyulmasını sağlamak."): yanlış aktarıma itiraz eder (sahne 4, 6), kaynağı ister (21), Silex'in bağımsız kaydını dinletir (25-26), alıcısını çıkarıp Vekh'e onun dilinde konuşur (61), Orun'dan özel kanalı açmasını ister (76), kaynak sesler dört filoya gider (79-85).
ENGEL     Nith ve resmî röle (plan): söz hakkı reddi (5) · "niyeti tercüme etmek" (15) · kaynaklar sertifikadan sonra silinir (22) · filoların barış çağrıları masaya sunulmaz (38-41) · "Do not draw your weapon." → "Draw your weapon." ve Vekh'in silahı (58-59) · dış bağlantıyı keser (73) · küpe uzanır (83).
KARAR     Sahne 61: Nem alıcısını çıkarıp Vekh'e onun kendi dilinde konuşur; sahne 64-69: Vekh, Ishra, Silex ve Orun alıcılarını çıkarır; sahne 70: Nem onları aklamaz ("He changed the words. You sent the ships."); sahne 78: Orun K1'i masanın merkezine iter ve özel kanalı açık bırakır (plan).
SONUÇ     Kaynak sesler ve Silex'in bağımsız kaydı dört filoya ulaşır; Vekh filosuna çekilme emri verir (86), Ishra tahliye koridorlarını açtırır (87), Vekh filosunun silahları söner (90), koridor açılır (91); son kaynak cümle Vekh'in: "We will not fire." (95); istasyon kara deliğin önünde, Nem'in sesi: "That is what he said." (96).
BEDEL     Kaybedilen günler ve canlar geri gelmez (plan: "We can't recover those days.") · Orun korunan sözleşmelerini ve servetini (77-78) · elçiler makamlarını tehlikeye atar (71, 86) · sahne 94
TEK SORU  "Masadaki herkes aynı cümleyi duyduğunu sanıyorsa gerçeği nasıl kanıtlayacak?" (plan, 60. saniye)
SEÇİM     Fable: sahip planı (tek aday, aday turu açılmadı) · 18.10.2026 · gerekçe: BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md + ODA/DURUM.md SAHİP CEVAPLARI
SAHİP     ONAY (planı kendisi verdi; talimat: "plandan asla dışarı çıkma") · 18.10.2026
```

İlk cümle (plan): VEKH: "We did not fire first." · OFFICIAL RELAY: "We fired first." — "Bir tek not sözcüğü kaybolur."
Gösterim kuralı (plan "Önemli gösterim kuralı"): senaryodaki İngilizce, izleyicinin özgün anlamı duyduğu dublaj katmanıdır; resmî rölenin nötr
İngilizcesi kritik bozulma örneklerinde ikinci ve ayrı bir ses olarak verilir. Etiketler görüntü modeline yazdırılmaz.
Kara deliğin işi (plan): istasyon olay ufkunun dışında; istasyonda 1 dakika = dış filoların saatinde 12 saat (kurmaca oran); C37 yerel altı dakika ↔ dışarıda üç gün.
Nith'in suçunu kara delik işlemez; karakterler geçmişi geri almaz, olay ufkunun içinden haber almaz, içine girip çıkmaz.
Çözümün kurulumları (plan): K1 C10'da, K2 C12'de; kaynakların silindiği C22'de öğrenilir; Nem'in canlı dil yetkinliği C61'de görünür;
sonunda yeni kurtarma gemisi, enerji çekirdeği, gizli canlı ya da zaman sıfırlaması gelmez.

Kadro (plan "Kadronun dramatik işleri ve sesleri", birebir):

| Konuşmacı | Ses | İstek | Görünür karar / durum |
|---|---|---|---|
| NEM | Kadın sesli yetişkin dil uzmanı; açık, kesin, sıcak ama çekingen olmayan. | İlk başta görevini doğru yapmak; sonra özgün sözün duyulmasını sağlamak. | C06 sonrası çoğunlukla ayakta. Alıcısı C61'de çıkar. |
| VEKH | Derin, hafif pürüzlü erkek sesi; askerî kesinlik, az bağırma. | Kendi halkını korumak, suçlamayı reddetmek. | Silahı C59 elde, C68 masada. Kendi bombardıman emrini kabul eder. |
| ISHRA | Kadın sesli su kökenli elçi; yumuşak rezonans, kontrollü kırılganlık. | Yaralı gemilerine geçit ve güvenli tahliye. | C67'de yalnız çeviri alıcısını çıkarır; su başlığı ve yaşam desteği sabit. |
| SILEX | Cinsiyetsiz, temiz, hafif harmonik tını; sakin gözlem. | Ölçüm ve bağımsız kayıt üzerinden ne olduğunu anlamak. | Kendi sertifikasyon payını kabul eder. K2'nin sahibi; alıcı C68'de çıkar. |
| ORUN | Kısık bariton, hızlı ve cilalı; kuru mizah. | Önce kârını korumak; sonunda bağımsız kanalını açmayı seçmek. | K1'in sahibi; alıcı C69'da çıkar. Silah satışını inkâr etmez. |
| NITH | Düşük, düzgün, neredeyse kusursuz erkek sesi; öfke yerine sakin küçümseme. | Resmî dil kanalını vazgeçilmez ve kârlı tutmak. | Alıcısını çıkarmaz. C65 ayağa kalkar; C84'te durdurulur, canlı kalır. |
| OFFICIAL RELAY | Duygusuz ve cinsiyetsiz resmî ses; Nith ve Silex'ten açıkça farklı. | Nith'in kurduğu resmî aktarım katmanı. | Kritik bozulma örneklerinde özgün cümleden sonra ayrı duyulur. |

Dört filo Vekh, Ishra, Silex ve Orun'un temsil ettiği yapılara aittir. Nem'in ayrı filosu yoktur. Anonim arşiv subayı C38'de yalnız ses olarak duyulur (plan).

Sekiz bölüm (plan): B1 C01-C12 KAYIP KELİME · B2 C13-C24 KİMİN TERCÜMESİ? · B3 C25-C36 SAVAŞIN ARŞİVİ · B4 C37-C48 DIŞARIDA ÜÇ GÜN ·
B5 C49-C60 BARIŞIN KÂRI · B6 C61-C72 KULAKLIKLAR ÇIKIYOR · B7 C73-C84 TEK SESİN SONU · B8 C85-C96 ASLIYLA AYNI.

## 2. TRETMAN

<!-- kaynak: plan "Tam çekim ve diyalog senaryosu" (sahne = klip, başlık + "Plan:" cümlesi birebir; replikler §5). "Ne değişir" planın bölüm "Dramatik değişim" satırı ve nesne/karakter durum tablosundan; plan dışı satır yok ("—"). -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S01 | 0:00–0:10 | C01 İlk kelime kayboluyor — Yakın / Vekh. Vekh'in bronz zırhlı yüzü; camın ardında dev kara delik. Sözü bittikten sonra resmî röle cümleyi değiştirir. | B1 KAYIP KELİME — bir olumsuzluk silinir; tercüme hatası savaş itirafına dönüşür (plan) |
| S02 | 0:10–0:20 | C02 Suçlama — Yakın / Ishra. Ishra'nın saydam su başlığının içinde gözleri daralır; yanlış sürüme tepki verir. | — |
| S03 | 0:20–0:30 | C03 Dışarıdaki filolar — Çok geniş / uzay. Daha uzak bölgede dört farklı filo; birkaç silah hattı aydınlanır. İstasyon olay ufkunun dışındadır. | — |
| S04 | 0:30–0:40 | C04 Kâtibin itirazı — Yakın / Nem. Nem kaynak ses ile resmî aktarımın ayrıldığını fark eder; başını kaldırır. | — |
| S05 | 0:40–0:50 | C05 Söz hakkı — Yakın / Nith. Nith baş koltukta sesini yükseltmeden Nem'i durdurur. | — |
| S06 | 0:50–1:00 | C06 İlk açık suçlama — Orta / Nem. Nem ayağa kalkar; kara deliğin ışığı yüzünün bir yanını aydınlatır. | Nem ayakta (plan: C06 sonrası çoğunlukla ayakta) |
| S07 | 1:00–1:10 | C07 İki düşman — İkili / Vekh-Ishra. Masanın karşılıklı iki yanında biri inkâr ederken diğeri bunu yeni yalan sanır. | — |
| S08 | 1:10–1:20 | C08 Makinenin otoritesi — Yakın / Nith. Nith resmî sistemin tarafsızlığını savunur. | — |
| S09 | 1:20–1:30 | C09 Kimin onayı? — Yakın / Nem. Nem sertifikalı kayıt levhasından Nith'e döner. | — |
| S10 | 1:30–1:40 | C10 Tüccarın küpü — Orta / Orun. Orun küçük sekizgen özel ticaret rölesini masaya bırakır; K1'in soluk ışığı görünür. | K1 masada (plan: C10–C74 bekleme) |
| S11 | 1:40–1:50 | C11 Silinen şey — Yakın / Nem. Nem tartışmayı tek eksik sözcüğe indirir. | — |
| S12 | 1:50–2:00 | C12 Test önerisi — Yakın / Silex. Silex masaya kendi bağımsız kayıt taşını koyar; K2 burada kurulur. | K2 masada (plan) |
| S13 | 2:00–2:10 | C13 Boş eller — Orta / Vekh. Vekh boş ellerini masanın üzerinde açar. Silahı hâlâ kemerindedir. | B2 KİMİN TERCÜMESİ? — Nem bir dil hatasıyla değil, niyeti yeniden yazan resmî bir sistemle karşı karşıyadır (plan) |
| S14 | 2:10–2:20 | C14 Görülen ile duyulan — Yakın / Ishra. Ishra boş ellere, sonra kendi alıcısına bakar. | — |
| S15 | 2:20–2:30 | C15 Niyet bahanesi — Yakın / Nith. Nith hatayı reddetmek yerine sistemi gerekçelendirir. | — |
| S16 | 2:30–2:40 | C16 Emirleri kim yazıyor? — Yakın / Nem. Nem sorgulayan kişi haline gelir; sakinliğini korur. | — |
| S17 | 2:40–2:50 | C17 Kara deliğin camı — Geniş / salon. Altı koltuk sabit düzende. Kara deliğin bükülmüş diski büyük camın arkasında; kısa sessizlik. | — |
| S18 | 2:50–3:00 | C18 Anlama karşı hak — Yakın / Vekh. Vekh'in hedefi artık yalnız karşı elçi değildir. | — |
| S19 | 3:00–3:10 | C19 Kısa geçmiş — Yakın / Ishra. Ishra, önceki çağrının sözcüklerini hatırlar; su başlığının düzeyi sabittir. | — |
| S20 | 3:10–3:20 | C20 Yanlış karşılık — Yakın / Vekh. Vekh o çağrıyı nasıl aldığını söyler. | — |
| S21 | 3:20–3:30 | C21 Arşivi aç — Yakın / Nem. Nem resmî özet yerine kaynağı ister. | — |
| S22 | 3:30–3:40 | C22 Uygun kayıt yok — Yakın / Nith. Nith özgün seslerin saklanmadığını açıklar. | kaynakların silindiği öğrenilir (plan) |
| S23 | 3:40–3:50 | C23 Bağımsız kayıt — Yakın / Silex. Silex, C12'den beri masadaki K2 taşını avucuna alır. | K2 Silex'in elinde (plan) |
| S24 | 3:50–4:00 | C24 Cümleden önce cevap — Yakın / Nem. Nem iki sesin sırasını dinler: resmî tehdit, özgün söz bitmeden başlatılmıştır. | — |
| S25 | 4:00–4:10 | C25 Eski kayıt — Orta / Silex. Silex bağımsız gözlemci olarak sakladığı eski Ishra çağrısını açar. Ses Ishra'nındır; yeni oyuncu gösterilmez. | B3 SAVAŞIN ARŞİVİ — bağımsız kayıt, eski bir yas ve barış çağrısının tehdide çevrildiğini gösterir (plan) |
| S26 | 4:10–4:20 | C26 Tehdide çevrilmiş yas — Yakın / Vekh. Eski resmî sürüm dinlenir; Vekh kendi saldırı gerekçesini tanır. | — |
| S27 | 4:20–4:30 | C27 Kim kimi vurdu? — Yakın / Vekh. Vekh kendi sorumluluğuna ilk kez yaklaşır. | — |
| S28 | 4:30–4:40 | C28 Kayıtları kim sağlıyor? — Yakın / Orun. Orun K1 küpünü kendisine çeker; çıkarını korumaya çalışır. | — |
| S29 | 4:40–4:50 | C29 Doğru soru — Yakın / Nem. Nem Orun'un yüzüne bakar. | — |
| S30 | 4:50–5:00 | C30 Tüccarın cevabı — Yakın / Orun. Orun maddiyatçı cevabını saklamaz. | — |
| S31 | 5:00–5:10 | C31 Dört donanma — Çok geniş / uzay. Dört filo karşılıklı dizilmiştir. Birkaç küçük sivil gemi arada bekler. | — |
| S32 | 5:10–5:20 | C32 Kim kazandı? — Yakın / Nem. Nem gelir akışını sorar. | — |
| S33 | 5:20–5:30 | C33 Acele etme — Yakın / Nith. Nith geçici anlaşmayla konuyu kapatmaya çalışır. | — |
| S34 | 5:30–5:40 | C34 Hangi geçmiş? — Yakın / Ishra. Ishra önerideki asıl koşulu gösterir. | — |
| S35 | 5:40–5:50 | C35 Elindeki tek ses — Yakın / Nith. Nith gerçek bir bağımlılığı tehdit olarak kullanır. | — |
| S36 | 5:50–6:00 | C36 Ortak vicdan — Yakın / Nem. Nem bütün masaya seslenir. | — |
| S37 | 6:00–6:10 | C37 İki saat — Detay / kurgu grafiği. Yerel altı dakika ile dış filo zamanındaki üç gün sade bir grafikle karşılaştırılır; yazılar sonradan eklenir. | B4 DIŞARIDA ÜÇ GÜN — zaman farkı ve tutulmuş mesajlar, tartışmanın dışarıdaki bedelini gösterir (plan) |
| S38 | 6:10–6:20 | C38 Geç gelen çağrı — Geniş / dış mesaj. Vekh filosundan bekleyen kayıt açılır; subayın yüzü gösterilmez. | — |
| S39 | 6:20–6:30 | C39 Neden bekletildi? — Yakın / Nem. Nem mesajın alındığı halde sunulmadığını görür. | — |
| S40 | 6:30–6:40 | C40 İstasyon ve uçurum — Çok geniş / manzara. İstasyon kara deliğin ışık yayı önünde küçüktür. Bütün yapısı olay ufkunun dışındadır. | — |
| S41 | 6:40–6:50 | C41 Kesilen teklifler — Yakın / Silex. Silex diğer filoların da bekleyen barış mesajlarını bulur. | — |
| S42 | 6:50–7:00 | C42 Bahane — Yakın / Nith. Nith gecikmeyi çekim alanına bağlar. | — |
| S43 | 7:00–7:10 | C43 Ayıklanan sözcükler — Yakın / Nem. Nem doğanın etkisi ile kasıtlı sansürü ayırır. | — |
| S44 | 7:10–7:20 | C44 Bekleyen yaralılar — Orta / Ishra. Ishra başını eğer; sivillerin bekleme haberini düşünür. | — |
| S45 | 7:20–7:30 | C45 Bekletmenin bedeli — Yakın / Vekh. Vekh eski öfkesini Nith'e çevirir; silah hâlâ kemerdedir. | — |
| S46 | 7:30–7:40 | C46 Tarafsızlığın faturası — Yakın / Nith. Nith otorite diliyle kendini savunur. | — |
| S47 | 7:40–7:50 | C47 Kimin ödediği — Yakın / Nem. Nem Orun'un baştan beri mevcut K1 küpüne bakar. | — |
| S48 | 7:50–8:00 | C48 Son uyarı — Yakın / Orun. Orun kayıtlarını açmak istemez. | — |
| S49 | 8:00–8:10 | C49 Başarısızlık geliri — Detay / K1 ve Orun. Orun'un küpü açılır; rakam tablosu yerine yüzü ve sesi kanıtı taşır. | B5 BARIŞIN KÂRI — Nith'in başarısız görüşmelerden kazandığı açığa çıkar; yanlış bir emir fiziksel şiddete yaklaşır (plan) |
| S50 | 8:10–8:20 | C50 Paranın yönü — Yakın / Silex. Silex para bağlantısını doğrular. | — |
| S51 | 8:20–8:30 | C51 Kârın adı — Yakın / Nem. Nem doğrudan Nith'e döner. | — |
| S52 | 8:30–8:40 | C52 Kesinlik satıcısı — Yakın / Nith. Nith tarafsızlık maskesini kısmen bırakır. | — |
| S53 | 8:40–8:50 | C53 Emir vermedim — Yakın / Nith. Nith verdiği kararlarla gerçek saldırılar arasına mesafe koymaya çalışır. | — |
| S54 | 8:50–9:00 | C54 İzin gibi — Yakın / Nem. Nem sözcükleri emir gibi sunmanın sonucunu söyler. | — |
| S55 | 9:00–9:10 | C55 Kaç teklif? — Yakın / Silex. Silex gizlenen barış çağrılarının sayısını değil seçilme nedenini açığa çıkarır. | — |
| S56 | 9:10–9:20 | C56 Sürecin gereği — Yakın / Nith. Nith denetimindeyken dışarı çıkmayacağını sandığı konuşmada kibirli cevabını verir. | — |
| S57 | 9:20–9:30 | C57 İki tarafı silahlandırmak — İkili / Ishra-Orun. Ishra Orun'a döner; ittifaklar değişir. | — |
| S58 | 9:30–9:40 | C58 Susturulmuş söz — Yakın / Nem. Nem silah çekilmemesini söyler; resmî ses yine anlamı tersine çevirir. | — |
| S59 | 9:40–9:50 | C59 Silah çekiliyor — Orta / Vekh. Vekh yanlış emirle blasterini çıkarır, Orun'a çevirir. Ateş etmeden duraksar. | W1 blaster Vekh'in elinde (plan) |
| S60 | 9:50–0:00 | C60 Hedefin önüne geçmek — Orta / Nem. Nem hedef çizgisine girer; elleri açıktır. | — |
| S61 | 0:00–0:10 | C61 Nem çıkarıyor — Yakın / Nem. Nem tercüman alıcısını çıkarıp masaya koyar; Vekh'e onun kendi dilinde konuşur. | B6 KULAKLIKLAR ÇIKIYOR — elçiler resmî sesi bırakır (plan) · Nem'in alıcısı masada (plan); Nem'in canlı dil yetkinliği görünür (plan) |
| S62 | 0:10–0:20 | C62 Gördüğüne inan — Yakın / Vekh. Vekh Nem'in açık ellerine bakar; namlu biraz aşağı iner. | namlu biraz aşağı (plan) |
| S63 | 0:20–0:30 | C63 Tek doğru soru — Yakın / Nem. Nem Vekh'in alıcısına bakar. | — |
| S64 | 0:30–0:40 | C64 Vekh çıkarıyor — Orta / Vekh. Vekh alıcısını çıkarır; silah aşağıdadır; Nem'in doğrudan sözünü dinler. | Vekh'in alıcısı çıktı; silah aşağıda (plan) |
| S65 | 0:40–0:50 | C65 Nith'in korkusu — Yakın / Nith. Nith ayağa kalkar; masadaki denetimi kaybolmaya başlar. | Nith ayakta (plan) |
| S66 | 0:50–1:00 | C66 İlk kez dinlemek — Yakın / Nem. Nem diğer elçilere sırayla bakar; kısa manuel çevirilere başlar. | — |
| S67 | 1:00–1:10 | C67 Ishra çıkarıyor — Yakın / Ishra. Ishra başlığın dış yuvasındaki tercüman alıcısını çıkarır; yaşam desteği yerinde kalır. | Ishra'nın alıcısı çıktı; su başlığı ve yaşam desteği sabit (plan) |
| S68 | 1:10–1:20 | C68 Silah masada — Orta / Vekh-Silex. Vekh blasterini masaya bırakır. Silex kendi alıcısını K2'nin yanına koyar. | blaster masada; Silex'in alıcısı K2'nin yanında (plan) |
| S69 | 1:20–1:30 | C69 Orun da çıkarıyor — Yakın / Orun. Orun kendi alıcısını K1'in yanına bırakır. | Orun'un alıcısı K1'in yanında; masada beş alıcı, Nith'inki takılı (plan) |
| S70 | 1:30–1:40 | C70 Aklamak değil — Yakın / Nem. Nem suçların yalnız sisteme yıkılmasını önler. | — |
| S71 | 1:40–1:50 | C71 Bedel — Yakın / Ishra. Ishra kendi siyasi geleceğini tehlikeye atacak gerçeği düşünür. | — |
| S72 | 1:50–2:00 | C72 Yanıt — Yakın / Nem. Nem makamın korunmasını insanların yaşamasından üstün tutmaz. | — |
| S73 | 2:00–2:10 | C73 Nith hattı kesiyor — Orta / Nith. Nith resmî dış aktarımı kapatır. Salonun yaşam sistemi ve yörüngesi normal kalır. | B7 TEK SESİN SONU — resmî dış bağlantı kesilir (plan) |
| S74 | 2:10–2:20 | C74 Kendi kaydı — Yakın / Nem. Nem yeni cihaz aramak yerine Orun'un mevcut küpüne döner. | — |
| S75 | 2:20–2:30 | C75 Bağımsız hat — Yakın / Orun. Orun K1'in özel kanal ışığını açar. | K1 özel bağlantı açılır (plan) |
| S76 | 2:30–2:40 | C76 Paranın yolu — İkili / Nem-Orun. Nem küpü kapmaz; Orun'dan açıkça ister. | — |
| S77 | 2:40–2:50 | C77 Risk Orun'da — Yakın / Nith. Nith ekonomik korumayı çekmekle tehdit eder. | — |
| S78 | 2:50–3:00 | C78 Açık karar — Yakın / Orun. Orun K1'i masanın merkezine iter ve özel kanalı açık bırakır. | K1 masanın merkezinde (plan); cyan yayın ışığı "C78 sonrası" (plan A10) — C79 yayın durumuna geçiş (plan pilotu) |
| S79 | 3:00–3:10 | C79 Kaynak yayında — Detay / K1 ve Nem. Nem kaynak ses ve görüntünün dört filo ağına değiştirilmeden gitmesini ister. | — |
| S80 | 3:10–3:20 | C80 Yalanın son savunması — Yakın / Nith. Nith elçileri kendi suçlarıyla susturmaya çalışır. | — |
| S81 | 3:20–3:30 | C81 Başlangıç — Yakın / Nem. Nem açık kayıt alanına bakar. | — |
| S82 | 3:30–3:40 | C82 Arşiv korunacak — Yakın / Silex. Silex K2 kayıt taşını K1'in yanına bırakır; bağımsız kopyayı yayına ekler. | K2 K1'in yanında (plan) |
| S83 | 3:40–3:50 | C83 Nith'in hamlesi — Orta / Nith-Orun. Nith küpe uzanır; Orun önkoluyla yolunu kapatır. Tek engelleme hareketi. | — |
| S84 | 3:50–4:00 | C84 Masaya dön — Orta / Vekh. Vekh Nith ile merkez arasına girer; masadaki silahı eline almaz. | Nith durdurulur, canlı kalır (plan) |
| S85 | 4:00–4:10 | C85 Dört filoya — Geniş / yeni masa düzeni. Nith etkisiz biçimde arka plandadır. Nem merkezde; dört elçi kendi kaydına döner. | B8 ASLIYLA AYNI — özgün sesler ve açık çekilme emirleri ulaşır (plan) |
| S86 | 4:10–4:20 | C86 Vekh'in emri — Yakın / Vekh. Vekh doğrudan kendi filosuna konuşur; silahı masada hareketsiz kalır. | — |
| S87 | 4:20–4:30 | C87 Ishra'nın emri — Yakın / Ishra. Ishra önce hastane gemilerine geçit açılmasını ister. | — |
| S88 | 4:30–4:40 | C88 Silex'in emri — Yakın / Silex. Silex kendi ittifakının gemilerine ve arşivine seslenir. | — |
| S89 | 4:40–4:50 | C89 Orun'un emri — Yakın / Orun. Orun ticaret filosuna kâr yerine hayatta kalanları taşıma görevi verir. | — |
| S90 | 4:50–5:00 | C90 Silahlar sönüyor — Çok geniş / uzay. Vekh filosunun silah hatları söner; formasyon karşı taraftan açılır. Yeni savaş başlamaz. | Vekh filosunun silah hatları söner (plan) |
| S91 | 5:00–5:10 | C91 Koridor açılıyor — Çok geniş / sonuç. Ishra'nın beyaz-teal gemileri koridor açar; küçük tıbbi/sivil gemiler aradan geçer. | koridor açılır (plan) |
| S92 | 5:10–5:20 | C92 Başka bir tercüman — Yakın / Nith-Nem. Nith son sözü almaya çalışır; Nem kısaca karşılık verir. | — |
| S93 | 5:20–5:30 | C93 Yerine değil yanında — İkili / Ishra-Nem. Ishra Nem'e yeni bir makam önerir; Nem göz hizasını eşit tutar. | — |
| S94 | 5:30–5:40 | C94 Geçen günler — Geniş / cam ve masa. Silex ile Nem kara deliğin ışığı önünde; diğerleri arka planda küçük kalır. | — |
| S95 | 5:40–5:50 | C95 İlk cümlenin karşılığı — Yakın / Vekh. Vekh açık kaynak kaydına son kez konuşur. Araya değiştirilmiş ses girmez. | — |
| S96 | 5:50–6:00 | C96 Olduğu gibi — Çok geniş / final. Aynı istasyon kara deliğin ışık yayı önünde; filolar ayrılmış, açık koridor kalmıştır. | — |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

<!-- kaynak: plan "Referanslar ve sabit sahne düzeni" A01-A09 (dokuz tam referans görsel promptu), numara sırası korundu: A01→1 … A09→9. Plan referansları tek görünüştür (single-subject three-quarter … reference); hat panel kalıbı (KIMLIK §7 P17, HİPOTEZ) uygulanmadı — plan korundu. Özne başına tek dosya kuralı (M) tek görünüşle karşılanır. A10-A13 plan "dört nesne briefi"dir: referans görseli yok, aşağıda NESNE DURUMU. Hat biçimindeki prompt metinleri PROMPTLAR/G01.md REFERANS PROMPTLARI'nda (plan metni birebir). -->
| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Nem — TEK SAYFA (plan A01; plan tek görünüş: single-subject three-quarter waist-up): yetişkin kadın sesli uzaylı dil uzmanı; mat lavanta-fildişi yüz plakaları, yüksek gümüş yanak sırtları, iki koyu mor göz, dar dikey ağız çizgisi; saç ve insan kulağı yok; koyu kalay rengi sade kâtip ceketi, tek kobalt boğaz ışığı; SAĞ şakakta ayrı ince gümüş tercüman alıcısı (çıkarılabilir, solunum cihazı değil) | `1.NEM_v1.png` | v1 | | ⬜ | C04 · C06 · C09 · C11 · C16 · C21 · C24 · C29 · C32 · C36 · C39 · C43 · C47 · C51 · C54 · C58 · C60 · C61 · C63 · C66 · C70 · C72 · C74 · C76 · C79 · C81 · C85 · C92 · C93 · C94 |
| 2 | Vekh — TEK SAYFA (plan A02, tek görünüş): bronz üniformalı askerî elçi; pas kırmızısı sert böceksi yüz plakaları, iki amber göz, kısa sabit yan çene plakaları, ortada koyu solunum dikişi; bronz resmî askerî zırh, altında koyu kırmızı giysi; SAĞ kalçada tek kompakt koyu blaster kılıfı; SAĞ şakakta ince çıkarılabilir gümüş alıcı | `2.VEKH_v1.png` | v1 | | ⬜ | C01 · C07 · C13 · C18 · C20 · C26 · C27 · C45 · C59 · C62 · C64 · C68 · C84 · C86 · C95 |
| 3 | Ishra — TEK SAYFA (plan A03, tek görünüş): suda yaşayan elçi; inci-teal deri, iki koyu yan göz, kısa simetrik solungaç yüzgeçleri; omuz yakasına inen rijit saydam su dolu başlık, sabit görünür su düzeyi, sade yaşam destek bağlantıları; koyu teal resmî giysi, soluk inci omuz kenarı; başlığın SAĞ dış yuvasında ayrı küçük gümüş alıcı (solunum ve su sisteminden ayrı) | `3.ISHRA_v1.png` | v1 | | ⬜ | C02 · C07 · C14 · C19 · C34 · C44 · C57 · C67 · C71 · C87 · C93 |
| 4 | Silex — TEK SAYFA (plan A04, tek görünüş): mor mineral yüzlü gözlemci elçi; buzlu ametist yüz, birkaç geniş sabit faset, iki koyu faset göz, dar orta konuşma dikişi; fasetler sürekli canlı yüzey (uçuşan parça değil); soluk gümüş sade diplomatik pelerin; hafif iç mor saydamlık; SAĞ şakakta ince ayrı gümüş alıcı. K2'nin sahibi | `4.SILEX_v1.png` | v1 | | ⬜ | C12 · C23 · C25 · C41 · C50 · C55 · C68 · C82 · C88 · C94 |
| 5 | Orun — TEK SAYFA (plan A05, tek görünüş): Ticaret Birliği elçisi ve silah tüccarı; katmanlı kabuk benzeri yosun yeşili yüz plakaları, iki yatay amber göz, geniş katlı alt çene; koyu metalik kenarlı pahalı okra-kahve resmî ceket, küçük rijit yaka; SAĞ şakakta ince çıkarılabilir gümüş alıcı. K1'in sahibi | `5.ORUN_v1.png` | v1 | | ⬜ | C10 · C28 · C30 · C48 · C49 · C57 · C69 · C75 · C76 · C78 · C83 · C89 |
| 6 | Nith — TEK SAYFA (plan A06, tek görünüş): kara delik istasyonunun ev sahibi, resmî dil ağının sahibi; parlak kapkara yüz, tek sabit kemik beyazı orta alın sırtı, iki dar buz mavisi göz, sade altın boğaz ağı, alçak iki çatallı kafa sırtı; uzun fildişi resmî ceket, siyah iç paneller, ölçülü altın şerit; SAĞ şakakta küçük gümüş alıcı (hiç çıkarmaz) | `6.NITH_v1.png` | v1 | | ⬜ | C05 · C08 · C15 · C22 · C33 · C35 · C42 · C46 · C52 · C53 · C56 · C65 · C73 · C77 · C80 · C83 · C85 · C92 |
| 7 | Görüşme salonu — TEK SAYFA (plan A07, boş mekân master): tek rijit siyah altıgen masa, geniş kavisli panoramik cam; tam altı sabit koltuk: kameraya bakan uzak baş koltuk fildişi-siyah (Nith, saat 12), saat yönünde bronz-kırmızı (Vekh 2) · teal (Ishra 4) · yakın tarafta daha küçük kalay kâtip koltuğu (Nem 6) · soluk gümüş-mor (Silex 8) · okra-kahve (Orun 10); masaya gömülü sade kişisel tercüman hoparlörleri ve basit fiziksel kumandalar; camdan aynı uzak kara delik gölgesi ve merceklenmiş altın yığılma diski; koyu taş-metal kaburgalar | `7.ACCORD_CHAMBER_v1.png` | v1 | | ⬜ | C01 · C02 · C04 · C05 · C06 · C07 · C08 · C09 · C10 · C11 · C12 · C13 · C14 · C15 · C16 · C17 · C18 · C19 · C20 · C21 · C22 · C23 · C24 · C25 · C26 · C27 · C28 · C29 · C30 · C32 · C33 · C34 · C35 · C36 · C39 · C41 · C42 · C43 · C44 · C45 · C46 · C47 · C48 · C49 · C50 · C51 · C52 · C53 · C54 · C55 · C56 · C57 · C58 · C59 · C60 · C61 · C62 · C63 · C64 · C65 · C66 · C67 · C68 · C69 · C70 · C71 · C72 · C73 · C74 · C75 · C76 · C77 · C78 · C79 · C80 · C81 · C82 · C83 · C84 · C85 · C86 · C87 · C88 · C89 · C92 · C93 · C94 · C95 |
| 8 | Kara delik ve istasyon — TEK SAYFA (plan A08, dış master): tek dev kara delik, gerçekten karanlık gölge; parlak eğik altın yığılma diski, merceklenmiş üst/alt yaylar, bir yanı daha parlak; olay ufkunun dışında ve disk malzemesinden uzak küçük istasyon: kompakt altıgen çekirdek, altı kısa kalkanlı kol, küçük soğuk mavi pencereler; tek kara delik | `8.BLACK_HOLE_STATION_v1.png` | v1 | | ⬜ | C01 · C03 · C31 · C38 · C40 · C90 · C91 · C96 |
| 9 | Dört filo — TEK SAYFA (plan A09, dış master): dış bölgede birbirinden ayrık dört filo: pas kırmızısı kama savaş gemileri (Vekh) · inci-beyaz ve teal yelpaze gemiler (Ishra) · gümüş fasetli gemiler (Silex) · okra halka biçimli ticaret taşıyıcıları (Orun); açık bir koridor boyunca karşılıklı; koridor kenarında birkaç küçük tıbbi gemi; aynı tek kara delik arka planda | `9.FOUR_FLEETS_v1.png` | v1 | | ⬜ | C03 · C31 · C38 · C90 · C91 · C96 |

```
SHA-256: shasum -a 256 ~/film_medya/BLACK_ACCORD/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
Plan sırası (plan: "Önce altı karakter ve salon, sonra dış kara delik ve filo masterı hazırlanır."): 1-6 → 7 → 8 → 9.
Plan eşlemesi: A01→1.NEM · A02→2.VEKH · A03→3.ISHRA · A04→4.SILEX · A05→5.ORUN · A06→6.NITH · A07→7.ACCORD_CHAMBER ·
  A08→8.BLACK_HOLE_STATION · A09→9.FOUR_FLEETS · A10-A13 nesne briefi (görsel yok).
Yükleme (KIMLIK §3): çekim başına en çok 3 referans; plan C01 üç (A02 · A07 · A08), C02-C06 iki.

ORTAK GÖRÜNÜM (plan stil cümlesi birebir — her Görsel ve (sahip 18.10.2026, tur 2) her Video promptunun sonunda; C01-C06'da plan metninin ardına):
  Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
SAHNE DÜZENİ (plan, sabit — "Geniş planlarda bu yerler korunur."):
  Nith cam önündeki baş koltukta (saat 12) · Vekh saat 2 · Ishra saat 4 · Nem saat 6, yakın taraftaki küçük kâtip yeri · Silex saat 8 ·
  Orun saat 10. Nem C06'dan sonra çoğunlukla ayakta. Panoramik camın ardında tek kara delik; istasyon olay ufkunun dışında.
  "Konuşmacı yakın planlarında bir veya iki ayrıntılı yüz yeterlidir; öteki kişilerin arkaları veya flu siluetleri kullanılabilir." (plan)
TÜRLERİN FARKI (plan): "Altı türün farkı sadece ten rengi değildir: baş yapısı, göz yerleşimi, ağız/boğaz ve solunum şekli de ayrılır."
F5 G01 (18.10.2026, PROMPTLAR/G01.md tur 1b) — birebir kopya:
ROL SÖZLÜĞÜ (C07-C12 ve G02-G08 referans anahtarındaki parantez, birebir):
  1 clerk · 2 military envoy · 3 aquatic envoy · 4 mineral envoy · 5 trade consul · 6 station host · 7 chamber · 8 black hole and station · 9 four fleets.
  NOT: C01-C06'da planın kendi rol kelimeleri çekime göre değişir (C01 "the single foreground alien" · "bronze seat and room geometry" · "distant view"; C04 "the single foreground clerk" …);
  bunlar plan cümlesidir, sözlükle birleştirilmez. Özne adı: gövdede planın adları (Nem · Vekh · Ishra · Silex · Orun · Nith); tutamaç yok.

MEKÂN IŞIĞI (Görsel'de; C01-C06'da plan cümlesi zaten kendi ışığını taşır, ek yazılmaz):
  SALON (iç hacim) — Warm gold side light and cool readable face shadows.   (plan C04)
  SALON, uzak uç kamera (cam kameranın arkasında, kadrajda değil) — Warm gold light from the camera side and cool readable face shadows.   (Fable, eleştiri turu 1; cam kadrajdaysa SALON cümlesi)
  DIŞ — The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow.   (plan A08 kelimeleri)
  DIŞ DÜNYA (her dış görselde; T18) — Keep one black hole with its lensed golden disk, realistic stable silhouettes.   (plan C03)

ORTAM SESİ (model sesi AÇIK film — aynı mekânın VİDEO promptunda; C01-C06'da plan kendi ses cümlesini taşır, aynen kalır):
  SALON — Sound: quiet chamber ventilation and distant table resonance.   (plan C01 · C04 kelimeleri)
  DIŞ — Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.   (plan C03 birebir)

SES KİMLİĞİ (model sesi — her replikte aynı kelimeler; plan C01-C06 ses kelimeleri + plan kadro tablosu "Ses" sütunu; konuşan kadrajdaysa ağzı yalnız kendi cümlesinde hareket eder, öteki yanıt kadraj dışı):
  Nem   — a precise steady adult female voice                                  (plan C04)
  Vekh  — a low rough controlled voice                                          (plan C01)
  Ishra — a clear restrained female voice with a soft resonant quality         (plan C02)
  Silex — a clean, genderless voice with a light harmonic tone, calm and observant   (plan tablosu)
  Orun  — a husky baritone voice, quick and polished, with dry humour          (plan tablosu)
  Nith  — a smooth low male voice; speaks calmly through his gold throat mesh  (plan C05)
  OFFICIAL RELAY — duygusuz, cinsiyetsiz resmî ses; kurguda eklenir, video promptuna yazılmaz (C01'de plan, röleyi "separate off-screen sound layer" diye anar).
  Replik kalıbı: "<ses cümlesi>: <line>"  (plan: "… voice: 'line'" → tek tırnak yerine iki nokta).

KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6 — plan stil cümlesi "cold charcoal and pewter shadows, warm gold black-hole reflections" ışık/yansıma taşıyor. SALON ve DIŞ ışığıyla aynı yönde
  (sıcak altın kara delik yansıması, soğuk gölge); C01-C12'de çelişen su/gezegen/ses yok → cümle sahibin, değişmedi.
```

### NESNE DURUMU (plan "Nesne devamlılığı", birebir)

| Plan | Nesne | Durum |
|---|---|---|
| A10 | K1 ÖZEL TİCARET RÖLESİ | Avuç boyu tek siyah sekizgen gövde; tek amber üçgen ışık. C10–C74 bekleme; C75 özel bağlantı açılır; C78 sonrası cyan yayın ışığı. Orun'a ait. |
| A11 | K2 BAĞIMSIZ KAYIT TAŞI | Silex'e ait tek düz, buzlu mor beşgen kayıt levhası. C12 masada; C23 elde; C82'de K1'in yanına gelir. |
| A12 | TERCÜMAN ALICISI | İnce gümüş tek şerit. Nem C61, Vekh C64, Ishra C67, Silex C68, Orun C69 çıkarır. Nith takılı bırakır. Yaşam destek parçası değildir. |
| A13 | W1 BLASTER | Vekh'in sağ kalça kılıfında başlar; C59'da çekilir, C64'te aşağı iner, C68'de masaya bırakılır. Sonrasında ateşlenmez veya yer değiştirmez. |

Ishra'nın su başlığına takılı işitsel alıcı çıkar; başlık, su veya solunum hattı çıkarılmaz. C69 sonrası Nem, Vekh, Ishra, Silex ve Orun'un beş ayrı alıcısı masadadır. Nith'inki takılıdır. Blaster C68'den sonra masada kalır. K1 ve K2 birbirine dönüşmez. (plan)
Görsel promptlar yalnız yüzü değil başlangıç durumunu da tutar: alıcı takılı mı, silah nerede, kim ayakta, K1 hangi kişinin önünde? (plan)

DURUM CÜMLELERİ (Fable, 18.10.2026 — plan A12/A13 durumundan; G06-G08 farklı yazmıştı, film boyu birebir bu cümleler):
- alıcı çıktıktan sonra (Nem C61+, Vekh C64+, Silex C68+, Orun C69+): "His right temple is bare." / "Her right temple is bare." / "Silex's right temple is bare."
- Ishra C67+: "The external socket at the right side of the dome is empty."
- masadaki alıcı görünüyorsa: "a single thin silver strip, a translation receiver and not a life-support part" (§3 KİMLİK A12) + yeri ("lies on the table in front of <ad>")
- Vekh'in blasteri C68+: "a single compact dark blaster" masada, kimseye dönük değil; "holstered" cümlesi yazılmaz; kalça kadrajdaysa aşağıdaki boş kılıf cümlesi geçerli.
- K1 ışığı (eleştiri turu 1 sonrası, 18.10.2026): C10-C74 "one pale amber triangular light" (plan A10 "bekleme"; C49 "küpü açılır" ışığı değiştirmez → sahibe SK5) ·
  C75 özel bağlantı açılır: soluk amber → "one steady amber triangular light" · C76-C78 "one steady amber triangular light" · C79 steady amber → cyan (plan pilotu) ·
  C80+ "one cyan triangular light" (plan A10 "C78 sonrası cyan").
- K2 yeri (plan A11 "C12 masada; C23 elde; C82'de K1'in yanına gelir" + C68 "alıcısını K2'nin yanına koyar"): C12-C22 Silex'in koltuğunun önünde masada ·
  C23-C25 Silex'in açık sağ avucunda · C26-C81 yine Silex'in önünde masada (C68'de alıcı yanına konur) · C82 avuçtan K1'in yanına, bir avuç arayla ·
  C83+ masanın merkezinde K1'in yanında — merkez kadrajdaysa ikisi birlikte görünür ("K1 ve K2 birbirine dönüşmez").
- Ayakta/oturan (plan): Nem C06+ çoğunlukla ayakta · Nith C65-C84 ayakta, C85+ oturur (plan C84 Vekh: "Sit down.") · Vekh C84'te Nith ile merkez arasında ayakta,
  C85+ oturur · Ishra hep oturur; C93'te Nem Ishra'nın göz hizasına iner (plan: "Nem göz hizasını eşit tutar").
- Blaster çekildikten sonra (C59 çekiş sonrası, C62, C64, C68, C84+) kalça kadrajdaysa: "The holster at his right hip is empty."
- Dış planlar (C31 C38 C90 C91; C03 plan metni aynen): "the rust-red wedge ships at frame-left and the pearl-white and teal fan vessels at frame-right" ·
  istasyon görünüyorsa (C40 C96) "small in the lower right third" · Vekh filosunun silah şeritleri C03'ten C90'a kadar yanık (C31 C38'de "lit"), C90'da söner ·
  C90 sonunda açılan koridor C91'de açık başlar.

### KİMLİK CÜMLELERİ (16.10.2026 · pilot ayrı koşulmadı → F5 G01 yazdı 18.10.2026, planın A01-A13 cümleleri birebir · Görsel promptta BİREBİR; C01-C06 plan metnidir, kimlik bloğu taşımaz)

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | Nem · özne | Nem is an adult nonhuman linguistic clerk. |
| 1 | Nem · yüz | Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. |
| 1 | Nem · kemik | Her face has distinctly alien bone geometry, without human ears or hair. |
| 1 | Nem · ceket + işaret | She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. |
| 1 | Nem · alıcı | A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. |
| 1 | Nem · beden | Two arms, stable upright proportions, delicate but practical hands. |
| 2 | Vekh · özne | Vekh is an adult nonhuman military envoy. |
| 2 | Vekh · yüz | Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. |
| 2 | Vekh · beden | His body is upright with two arms and two legs. |
| 2 | Vekh · zırh (kalça görünmeyen kadraj) | He wears bronze formal military armour over dark-red clothing. |
| 2 | Vekh · zırh + blaster (kalça görününce) | He wears bronze formal military armour over dark-red clothing, with a single compact dark blaster holstered at the right hip. |
| 2 | Vekh · alıcı | A thin removable silver translation receiver is fixed at the right temple, separate from his anatomy. |
| 3 | Ishra · özne | Ishra is an adult aquatic alien diplomat. |
| 3 | Ishra · yüz | Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. |
| 3 | Ishra · başlık | A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. |
| 3 | Ishra · giysi | Her dark-teal formal suit has pale pearl shoulder edging. |
| 3 | Ishra · alıcı | A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. |
| 4 | Silex · özne | Silex is an adult nonhuman envoy with a stable living-mineral anatomy. |
| 4 | Silex · yüz | A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. |
| 4 | Silex · faset | The facets are continuous biological surfaces, not floating shards. |
| 4 | Silex · pelerin | Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. |
| 4 | Silex · alıcı | A thin separate silver translation receiver rests at the right temple. |
| 4 | Silex · doku | Subtle internal violet translucency, restrained expression, no changing crystal growth. |
| 5 | Orun · özne | Orun is an adult nonhuman trade consul. |
| 5 | Orun · yüz | Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. |
| 5 | Orun · ceket | He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. |
| 5 | Orun · beden | Two arms, substantial but not exaggerated build. |
| 5 | Orun · alıcı | A thin removable silver translation receiver rests at the right temple. |
| 6 | Nith · özne | Nith is an adult nonhuman diplomatic station host. |
| 6 | Nith · yüz | A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. |
| 6 | Nith · baş sırtı | A low two-pronged cranial crest is part of the same stable head. |
| 6 | Nith · ceket | He wears a long ivory formal coat over black inner panels, with restrained gold trim. |
| 6 | Nith · alıcı | A small silver translation receiver remains at his right temple. |
| 7 | Salon · masa + cam | One rigid black hexagonal table stands before a broad panoramic curved window. |
| 7 | Salon · altı koltuk | Exactly six distinct fixed chair positions surround it: the far head chair facing the camera has ivory and black host colours; clockwise from it are bronze-red, teal, a smaller near-side pewter clerk chair, pale silver-violet, and ochre-brown. |
| 7 | Salon · masa donanımı | Discreet personal translation speakers and simple physical controls are built into the table. |
| 7 | Salon · cam manzarası | Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. |
| 7 | Salon · kaburgalar | Dark stone-metal ribs, readable cold shadows, warm disk reflections. |
| 8 | Kara delik | The black-hole shadow is truly dark. |
| 8 | Disk | A bright tilted golden accretion disk and its gravitationally lensed upper and lower arcs wrap around the shadow, with one side visibly brighter. |
| 8 | İstasyon | The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. |
| 9 | Filolar | Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. |
| 9 | Koridor + tıbbi gemiler | They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. |
| A10 | K1 özel ticaret rölesi (Orun'a ait) | a single palm-sized black octagonal body with one pale amber triangular light |
| A11 | K2 bağımsız kayıt taşı (Silex'e ait) | a single flat frosted-purple pentagonal recording slab small enough to rest in one palm |
| A12 | Tercüman alıcısı | a single thin silver strip, a translation receiver and not a life-support part |
| A13 | W1 blaster (Vekh) | a single compact dark blaster holstered at the right hip |

```
Kadrajda görünen her parça çekimin Görsel promptuna kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (5/5 filmde
kimlik kayması, ARASTIRMA/16 Y1-Y3). İşaret: sayı + taraf + konum + "the only marking". Nesne: biçim + ölçü + taraf.
Bu filmde cümleler planın A01-A13 ve C01-C06 kelimelerinden seçilir; plana yeni sıfat eklenmez (sahip talimatı).
film_dogrula DERS Y2: referansı eklenen çekimde hiçbir parçası birebir geçmeyen özneyi gösterir (uyarı).
```

## 4. ÇEKİM LİSTESİ

<!-- kaynak: plan C01-C96 (klip = çekim, aynı numara). "Anlatacağı TEK bilgi" = plan başlığı + plan "Plan:" cümlesi BİREBİR. "Ekranda görünen" = plan cümlesinin
     kadraj/özne sonrası kısmı birebir; yalnız zihinsel fiil taşıyan 10 satırda (C04 C19 C21 C44 C71 C72 C76 C79 C87 C89) görünmeyen cümlecik düştü ya da
     "ister" → "talep eder" oldu (film_dogrula M; plan cümlesi soldaki sütunda tam). Kadraj = plan kadraj türü + özne (C01-C06 kamerası plan video promptundan).
     Taraf = plan sabit düzeni. Flow modu: plan "Görsel girdisi o klip için üretilmiş başlangıç karesidir" → hepsi görselden video. Referans: plan C01-C06 EKLE
     listesi birebir; diğerleri plan öznesinden (konuşan/görünen elçi + 7.ACCORD_CHAMBER; dış planlar 8 · 9). Risk: ARIZA T kodu + BT + planın kendi çözümü.
     Grup = plan bölümü: G01 C01-C12 · G02 C13-C24 · G03 C25-C36 · G04 C37-C48 · G05 C49-C60 · G06 C61-C72 · G07 C73-C84 · G08 C85-C96. Zincir yok (aşağıda). -->
| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | İlk kelime kayboluyor — plan: Yakın / Vekh. Vekh'in bronz zırhlı yüzü; camın ardında dev kara delik. Sözü bittikten sonra resmî röle cümleyi değiştirir. | Vekh'in bronz zırhlı yüzü; camın ardında dev kara delik. Sözü bittikten sonra resmî röle cümleyi değiştirir. | Yakın · Vekh · restrained slow push toward Vekh (plan) | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | ILK_30 §6 açılış · ilk 2 s insan sesi yok → Vekh repliği 2,0 s'den · röle sesi ayrı katman, kurguda (plan) · BT §A 'fire' model sesi repliğinde → red gelirse replik kayda (plan: 'ayrı hazırlanıp kurguda eklenir'), metin değişmez · plan pilotu (C01 · C61 · C79) | 2.VEKH · 7.ACCORD_CHAMBER · 8.BLACK_HOLE_STATION | G01 | ✍️ | — | — | — |
| C02 | Suçlama — plan: Yakın / Ishra. Ishra'nın saydam su başlığının içinde gözleri daralır; yanlış sürüme tepki verir. | Ishra'nın saydam su başlığının içinde gözleri daralır; yanlış sürüme tepki verir. | Yakın · Ishra · hold the close view (plan) | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | ILK_30 §6 · T05 su başlığı, sabit su düzeyi ve yaşam destek bağlantıları (plan A03) | 3.ISHRA · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C03 | Dışarıdaki filolar — plan: Çok geniş / uzay. Daha uzak bölgede dört farklı filo; birkaç silah hattı aydınlanır. İstasyon olay ufkunun dışındadır. | Daha uzak bölgede dört farklı filo; birkaç silah hattı aydınlanır. İstasyon olay ufkunun dışındadır. (ses: Diyalog yok. Ortam, gerilim ve ölçek için nefes alanı.) | Çok geniş · uzay · slow lateral drift through the wide formation (plan) | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | ILK_30 §6 · T13 vakumda motor/patlama sesi yok (plan) · T18 tek kara delik (plan) · büyük savaş başlamaz, yeni gemi grubu girmez (plan) | 8.BLACK_HOLE_STATION · 9.FOUR_FLEETS | G01 | ✍️ | — | — | — |
| C04 | Kâtibin itirazı — plan: Yakın / Nem. Nem kaynak ses ile resmî aktarımın ayrıldığını fark eder; başını kaldırır. | Nem başını kaldırır. | Yakın · Nem · very small push (plan) | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C05 | Söz hakkı — plan: Yakın / Nith. Nith baş koltukta sesini yükseltmeden Nem'i durdurur. | Nith baş koltukta sesini yükseltmeden Nem'i durdurur. | Yakın · Nith · hold the close camera (plan) | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C06 | İlk açık suçlama — plan: Orta / Nem. Nem ayağa kalkar; kara deliğin ışığı yüzünün bir yanını aydınlatır. | Nem ayağa kalkar; kara deliğin ışığı yüzünün bir yanını aydınlatır. | Orta · Nem · quiet low-angle camera (plan) | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | kalkma tek ve kontrollü (plan) · Nith yanıtı kadraj dışı, kurguda (plan) | 1.NEM · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C07 | İki düşman — plan: İkili / Vekh-Ishra. Masanın karşılıklı iki yanında biri inkâr ederken diğeri bunu yeni yalan sanır. | Masanın karşılıklı iki yanında biri inkâr ederken diğeri bunu yeni yalan sanır. | İkili · Vekh-Ishra | Vekh saat 2 (bronz-kırmızı koltuk) · Ishra saat 4 (teal koltuk) | 10 | Frames to Video | T15/T16 iki yüz: model sesi yalnız Vekh; Ishra'nın yanıtı kurguda → Ishra arkadan ya da flu, ağzı kapalı (plan: 'ön planda bir konuşmacı yeterlidir' · 'öteki kişilerin arkaları veya flu siluetleri') · plan içi çelişki: 'masanın karşılıklı iki yanında' ↔ sabit düzen (Vekh saat 2 · Ishra saat 4 komşu) → sabit düzen korunur, sahibe SK2 | 2.VEKH · 3.ISHRA · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C08 | Makinenin otoritesi — plan: Yakın / Nith. Nith resmî sistemin tarafsızlığını savunur. | Nith resmî sistemin tarafsızlığını savunur. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C09 | Kimin onayı? — plan: Yakın / Nem. Nem sertifikalı kayıt levhasından Nith'e döner. | Nem sertifikalı kayıt levhasından Nith'e döner. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C10 | Tüccarın küpü — plan: Orta / Orun. Orun küçük sekizgen özel ticaret rölesini masaya bırakır; K1'in soluk ışığı görünür. | Orun küçük sekizgen özel ticaret rölesini masaya bırakır; K1'in soluk ışığı görünür. | Orta · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T01 küpü masaya bırakma (plan: karmaşık parmak hareketi gerekirse kesmeyle sadeleşir) · T09 K1: avuç boyu tek siyah sekizgen gövde, tek amber üçgen ışık (plan A10) | 5.ORUN · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C11 | Silinen şey — plan: Yakın / Nem. Nem tartışmayı tek eksik sözcüğe indirir. | Nem tartışmayı tek eksik sözcüğe indirir. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C12 | Test önerisi — plan: Yakın / Silex. Silex masaya kendi bağımsız kayıt taşını koyar; K2 burada kurulur. | Silex masaya kendi bağımsız kayıt taşını koyar; K2 burada kurulur. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | T01 kayıt taşını masaya koyma · T09 K2: tek düz buzlu mor beşgen levha (plan A11) | 4.SILEX · 7.ACCORD_CHAMBER | G01 | ✍️ | — | — | — |
| C13 | Boş eller — plan: Orta / Vekh. Vekh boş ellerini masanın üzerinde açar. Silahı hâlâ kemerindedir. | Vekh boş ellerini masanın üzerinde açar. Silahı hâlâ kemerindedir. | Orta · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T09 silah hâlâ kemerde (plan) · röle sesi kurguda, Vekh yalnız kendi cümlesinde konuşur (plan) | 2.VEKH · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C14 | Görülen ile duyulan — plan: Yakın / Ishra. Ishra boş ellere, sonra kendi alıcısına bakar. | Ishra boş ellere, sonra kendi alıcısına bakar. | Yakın · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | — | 3.ISHRA · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C15 | Niyet bahanesi — plan: Yakın / Nith. Nith hatayı reddetmek yerine sistemi gerekçelendirir. | Nith hatayı reddetmek yerine sistemi gerekçelendirir. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C16 | Emirleri kim yazıyor? — plan: Yakın / Nem. Nem sorgulayan kişi haline gelir; sakinliğini korur. | Nem sorgulayan kişi haline gelir; sakinliğini korur. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C17 | Kara deliğin camı — plan: Geniş / salon. Altı koltuk sabit düzende. Kara deliğin bükülmüş diski büyük camın arkasında; kısa sessizlik. | Altı koltuk sabit düzende. Kara deliğin bükülmüş diski büyük camın arkasında; kısa sessizlik. (ses: Diyalog yok. Ortam, gerilim ve ölçek için nefes alanı.) | Geniş · salon | salon geniş: plan sabit düzeni (Nith 12 cam önü · Vekh 2 · Ishra 4 · Nem 6 · Silex 8 · Orun 10); cam Nith'in arkasında | 10 | Frames to Video | T15 kişi sayısı: altı koltuk sabit düzende (plan) · T18 tek kara delik, bükülmüş disk camın arkasında (plan) | 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C18 | Anlama karşı hak — plan: Yakın / Vekh. Vekh'in hedefi artık yalnız karşı elçi değildir. | Vekh'in hedefi artık yalnız karşı elçi değildir. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | — | 2.VEKH · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C19 | Kısa geçmiş — plan: Yakın / Ishra. Ishra, önceki çağrının sözcüklerini hatırlar; su başlığının düzeyi sabittir. | Ishra konuşur; su başlığının düzeyi sabittir. | Yakın · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | — | 3.ISHRA · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C20 | Yanlış karşılık — plan: Yakın / Vekh. Vekh o çağrıyı nasıl aldığını söyler. | Vekh o çağrıyı nasıl aldığını söyler. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | — | 2.VEKH · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C21 | Arşivi aç — plan: Yakın / Nem. Nem resmî özet yerine kaynağı ister. | Nem resmî özet yerine kaynağı talep eder. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C22 | Uygun kayıt yok — plan: Yakın / Nith. Nith özgün seslerin saklanmadığını açıklar. | Nith özgün seslerin saklanmadığını açıklar. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C23 | Bağımsız kayıt — plan: Yakın / Silex. Silex, C12'den beri masadaki K2 taşını avucuna alır. | Silex, C12'den beri masadaki K2 taşını avucuna alır. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | T01 taşı avucuna alma · T09 K2 (plan A11) | 4.SILEX · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C24 | Cümleden önce cevap — plan: Yakın / Nem. Nem iki sesin sırasını dinler: resmî tehdit, özgün söz bitmeden başlatılmıştır. | Nem iki sesin sırasını dinler: resmî tehdit, özgün söz bitmeden başlatılmıştır. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G02 | ✍️ | — | — | — |
| C25 | Eski kayıt — plan: Orta / Silex. Silex bağımsız gözlemci olarak sakladığı eski Ishra çağrısını açar. Ses Ishra'nındır; yeni oyuncu gösterilmez. | Silex bağımsız gözlemci olarak sakladığı eski Ishra çağrısını açar. Ses Ishra'nındır; yeni oyuncu gösterilmez. | Orta · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | kadrajda konuşan yok: eski Ishra kaydı + Nem kadraj dışı, Silex'in ağzı kapalı (plan: 'yeni oyuncu gösterilmez') · T09 K2 | 4.SILEX · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C26 | Tehdide çevrilmiş yas — plan: Yakın / Vekh. Eski resmî sürüm dinlenir; Vekh kendi saldırı gerekçesini tanır. | Eski resmî sürüm dinlenir; Vekh kendi saldırı gerekçesini tanır. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | eski röle kaydı kurguda; Vekh yalnız kendi cümlesinde konuşur | 2.VEKH · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C27 | Kim kimi vurdu? — plan: Yakın / Vekh. Vekh kendi sorumluluğuna ilk kez yaklaşır. | Vekh kendi sorumluluğuna ilk kez yaklaşır. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | BT §A 'shelled' model sesi repliğinde → red gelirse kayda (plan yolu), metin değişmez | 2.VEKH · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C28 | Kayıtları kim sağlıyor? — plan: Yakın / Orun. Orun K1 küpünü kendisine çeker; çıkarını korumaya çalışır. | Orun K1 küpünü kendisine çeker; çıkarını korumaya çalışır. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T01 küpü kendine çekme · T09 K1 | 5.ORUN · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C29 | Doğru soru — plan: Yakın / Nem. Nem Orun'un yüzüne bakar. | Nem Orun'un yüzüne bakar. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | BT §A 'weapons' model sesi repliğinde → red gelirse kayda | 1.NEM · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C30 | Tüccarın cevabı — plan: Yakın / Orun. Orun maddiyatçı cevabını saklamaz. | Orun maddiyatçı cevabını saklamaz. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | — | 5.ORUN · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C31 | Dört donanma — plan: Çok geniş / uzay. Dört filo karşılıklı dizilmiştir. Birkaç küçük sivil gemi arada bekler. | Dört filo karşılıklı dizilmiştir. Birkaç küçük sivil gemi arada bekler. (ses: Diyalog yok. Ortam, gerilim ve ölçek için nefes alanı.) | Çok geniş · uzay | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | T13 · T18 · dört filo karşılıklı, küçük sivil gemiler arada (plan) | 8.BLACK_HOLE_STATION · 9.FOUR_FLEETS | G03 | ✍️ | — | — | — |
| C32 | Kim kazandı? — plan: Yakın / Nem. Nem gelir akışını sorar. | Nem gelir akışını sorar. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C33 | Acele etme — plan: Yakın / Nith. Nith geçici anlaşmayla konuyu kapatmaya çalışır. | Nith geçici anlaşmayla konuyu kapatmaya çalışır. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C34 | Hangi geçmiş? — plan: Yakın / Ishra. Ishra önerideki asıl koşulu gösterir. | Ishra önerideki asıl koşulu gösterir. | Yakın · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | — | 3.ISHRA · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C35 | Elindeki tek ses — plan: Yakın / Nith. Nith gerçek bir bağımlılığı tehdit olarak kullanır. | Nith gerçek bir bağımlılığı tehdit olarak kullanır. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C36 | Ortak vicdan — plan: Yakın / Nem. Nem bütün masaya seslenir. | Nem bütün masaya seslenir. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G03 | ✍️ | — | — | — |
| C37 | İki saat — plan: Detay / kurgu grafiği. Yerel altı dakika ile dış filo zamanındaki üç gün sade bir grafikle karşılaştırılır; yazılar sonradan eklenir. | Yerel altı dakika ile dış filo zamanındaki üç gün sade bir grafikle karşılaştırılır; yazılar sonradan eklenir. | Detay · kurgu grafiği | — | 10 | Frames to Video | T06 grafik: yazılar görüntü modeline yazdırılmaz, sonradan eklenir (plan) · iki ses kadraj dışı | — | G04 | ✍️ | — | — | — |
| C38 | Geç gelen çağrı — plan: Geniş / dış mesaj. Vekh filosundan bekleyen kayıt açılır; subayın yüzü gösterilmez. | Vekh filosundan bekleyen kayıt açılır; subayın yüzü gösterilmez. | Geniş · dış mesaj | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | subayın yüzü gösterilmez (plan) · T13 · T18 · iki ses kadraj dışı · okuma: 'Geniş / dış mesaj' = Vekh filosunun dış görüntüsü üstünde kayıt (Fable okuması, sahibe SK3) | 9.FOUR_FLEETS · 8.BLACK_HOLE_STATION | G04 | ✍️ | — | — | — |
| C39 | Neden bekletildi? — plan: Yakın / Nem. Nem mesajın alındığı halde sunulmadığını görür. | Nem mesajın alındığı halde sunulmadığını görür. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C40 | İstasyon ve uçurum — plan: Çok geniş / manzara. İstasyon kara deliğin ışık yayı önünde küçüktür. Bütün yapısı olay ufkunun dışındadır. | İstasyon kara deliğin ışık yayı önünde küçüktür. Bütün yapısı olay ufkunun dışındadır. (ses: Diyalog yok. Ortam, gerilim ve ölçek için nefes alanı.) | Çok geniş · manzara | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | T13 · T18 · istasyon küçük, bütün yapısı olay ufkunun dışında (plan) | 8.BLACK_HOLE_STATION | G04 | ✍️ | — | — | — |
| C41 | Kesilen teklifler — plan: Yakın / Silex. Silex diğer filoların da bekleyen barış mesajlarını bulur. | Silex diğer filoların da bekleyen barış mesajlarını bulur. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | — | 4.SILEX · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C42 | Bahane — plan: Yakın / Nith. Nith gecikmeyi çekim alanına bağlar. | Nith gecikmeyi çekim alanına bağlar. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C43 | Ayıklanan sözcükler — plan: Yakın / Nem. Nem doğanın etkisi ile kasıtlı sansürü ayırır. | Nem doğanın etkisi ile kasıtlı sansürü ayırır. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C44 | Bekleyen yaralılar — plan: Orta / Ishra. Ishra başını eğer; sivillerin bekleme haberini düşünür. | Ishra başını eğer. | Orta · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | — | 3.ISHRA · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C45 | Bekletmenin bedeli — plan: Yakın / Vekh. Vekh eski öfkesini Nith'e çevirir; silah hâlâ kemerdedir. | Vekh eski öfkesini Nith'e çevirir; silah hâlâ kemerdedir. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T09 silah hâlâ kemerde (plan) | 2.VEKH · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C46 | Tarafsızlığın faturası — plan: Yakın / Nith. Nith otorite diliyle kendini savunur. | Nith otorite diliyle kendini savunur. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C47 | Kimin ödediği — plan: Yakın / Nem. Nem Orun'un baştan beri mevcut K1 küpüne bakar. | Nem Orun'un baştan beri mevcut K1 küpüne bakar. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | T09 K1 masada (plan) | 1.NEM · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C48 | Son uyarı — plan: Yakın / Orun. Orun kayıtlarını açmak istemez. | Orun kayıtlarını açmak istemez. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | — | 5.ORUN · 7.ACCORD_CHAMBER | G04 | ✍️ | — | — | — |
| C49 | Başarısızlık geliri — plan: Detay / K1 ve Orun. Orun'un küpü açılır; rakam tablosu yerine yüzü ve sesi kanıtı taşır. | Orun'un küpü açılır; rakam tablosu yerine yüzü ve sesi kanıtı taşır. | Detay · K1 ve Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | rakam tablosu yok; yüz ve ses kanıtı taşır (plan) · T06 · T09 K1 açılır | 5.ORUN · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C50 | Paranın yönü — plan: Yakın / Silex. Silex para bağlantısını doğrular. | Silex para bağlantısını doğrular. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | — | 4.SILEX · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C51 | Kârın adı — plan: Yakın / Nem. Nem doğrudan Nith'e döner. | Nem doğrudan Nith'e döner. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C52 | Kesinlik satıcısı — plan: Yakın / Nith. Nith tarafsızlık maskesini kısmen bırakır. | Nith tarafsızlık maskesini kısmen bırakır. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C53 | Emir vermedim — plan: Yakın / Nith. Nith verdiği kararlarla gerçek saldırılar arasına mesafe koymaya çalışır. | Nith verdiği kararlarla gerçek saldırılar arasına mesafe koymaya çalışır. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | BT §A 'fire' model sesi repliğinde → red gelirse kayda | 6.NITH · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C54 | İzin gibi — plan: Yakın / Nem. Nem sözcükleri emir gibi sunmanın sonucunu söyler. | Nem sözcükleri emir gibi sunmanın sonucunu söyler. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C55 | Kaç teklif? — plan: Yakın / Silex. Silex gizlenen barış çağrılarının sayısını değil seçilme nedenini açığa çıkarır. | Silex gizlenen barış çağrılarının sayısını değil seçilme nedenini açığa çıkarır. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | — | 4.SILEX · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C56 | Sürecin gereği — plan: Yakın / Nith. Nith denetimindeyken dışarı çıkmayacağını sandığı konuşmada kibirli cevabını verir. | Nith denetimindeyken dışarı çıkmayacağını sandığı konuşmada kibirli cevabını verir. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C57 | İki tarafı silahlandırmak — plan: İkili / Ishra-Orun. Ishra Orun'a döner; ittifaklar değişir. | Ishra Orun'a döner; ittifaklar değişir. | İkili · Ishra-Orun | Ishra saat 4 (teal koltuk) · Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T15/T16 iki yüz: model sesi yalnız Ishra; Orun yanıtı kurguda → Orun arkadan ya da flu, ağzı kapalı (plan) | 3.ISHRA · 5.ORUN · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C58 | Susturulmuş söz — plan: Yakın / Nem. Nem silah çekilmemesini söyler; resmî ses yine anlamı tersine çevirir. | Nem silah çekilmemesini söyler; resmî ses yine anlamı tersine çevirir. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | BT §A 'weapon' model sesi repliğinde · röle sesi kurguda, Nem yalnız kendi cümlesinde konuşur | 1.NEM · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C59 | Silah çekiliyor — plan: Orta / Vekh. Vekh yanlış emirle blasterini çıkarır, Orun'a çevirir. Ateş etmeden duraksar. | Vekh yanlış emirle blasterini çıkarır, Orun'a çevirir. Ateş etmeden duraksar. | Orta · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T01 blaster çekme + Orun'a çevirme, ateş etmeden duraksar (plan) · T09 W1 sağ kalça kılıfından (plan A13) | 2.VEKH · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C60 | Hedefin önüne geçmek — plan: Orta / Nem. Nem hedef çizgisine girer; elleri açıktır. | Nem hedef çizgisine girer; elleri açıktır. | Orta · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | Nem hedef çizgisinde, elleri açık (plan) · Nith yanıtı kadraj dışı | 1.NEM · 7.ACCORD_CHAMBER | G05 | ✍️ | — | — | — |
| C61 | Nem çıkarıyor — plan: Yakın / Nem. Nem tercüman alıcısını çıkarıp masaya koyar; Vekh'e onun kendi dilinde konuşur. | Nem tercüman alıcısını çıkarıp masaya koyar; Vekh'e onun kendi dilinde konuşur. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | plan pilotu · T01 + BT §A 'bedenden çıkarma': alıcı ayrı ince gümüş şerit, yaşam destek parçası değil (plan A12) · T09 alıcı masada | 1.NEM · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C62 | Gördüğüne inan — plan: Yakın / Vekh. Vekh Nem'in açık ellerine bakar; namlu biraz aşağı iner. | Vekh Nem'in açık ellerine bakar; namlu biraz aşağı iner. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T09 namlu biraz aşağı iner (plan) · Nem yanıtı kadraj dışı | 2.VEKH · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C63 | Tek doğru soru — plan: Yakın / Nem. Nem Vekh'in alıcısına bakar. | Nem Vekh'in alıcısına bakar. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C64 | Vekh çıkarıyor — plan: Orta / Vekh. Vekh alıcısını çıkarır; silah aşağıdadır; Nem'in doğrudan sözünü dinler. | Vekh alıcısını çıkarır; silah aşağıdadır; Nem'in doğrudan sözünü dinler. | Orta · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T01 + BT §A alıcı çıkarma · T09 silah aşağıda (plan) · Nem'in iki yanıtı kadraj dışı | 2.VEKH · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C65 | Nith'in korkusu — plan: Yakın / Nith. Nith ayağa kalkar; masadaki denetimi kaybolmaya başlar. | Nith ayağa kalkar; masadaki denetimi kaybolmaya başlar. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | Nith ayağa kalkar (plan) · Ishra yanıtı kadraj dışı | 6.NITH · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C66 | İlk kez dinlemek — plan: Yakın / Nem. Nem diğer elçilere sırayla bakar; kısa manuel çevirilere başlar. | Nem diğer elçilere sırayla bakar; kısa manuel çevirilere başlar. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C67 | Ishra çıkarıyor — plan: Yakın / Ishra. Ishra başlığın dış yuvasındaki tercüman alıcısını çıkarır; yaşam desteği yerinde kalır. | Ishra başlığın dış yuvasındaki tercüman alıcısını çıkarır; yaşam desteği yerinde kalır. | Yakın · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | T01 + BT §A alıcı: başlığın dış yuvasından; başlık, su ve solunum hattı yerinde (plan A12) · T05 | 3.ISHRA · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C68 | Silah masada — plan: Orta / Vekh-Silex. Vekh blasterini masaya bırakır. Silex kendi alıcısını K2'nin yanına koyar. | Vekh blasterini masaya bırakır. Silex kendi alıcısını K2'nin yanına koyar. | Orta · Vekh-Silex | Vekh saat 2 (bronz-kırmızı koltuk) · Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | T01 iki el eylemi aynı çekimde (blaster masaya · Silex alıcısı K2'nin yanına; plan: gerekirse kesmeyle sadeleşir) · BT §A 'shelled' model sesi · Ishra kadraj dışı | 2.VEKH · 4.SILEX · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C69 | Orun da çıkarıyor — plan: Yakın / Orun. Orun kendi alıcısını K1'in yanına bırakır. | Orun kendi alıcısını K1'in yanına bırakır. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T01 + BT §A alıcı · T09 K1 · Silex yanıtı kadraj dışı | 5.ORUN · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C70 | Aklamak değil — plan: Yakın / Nem. Nem suçların yalnız sisteme yıkılmasını önler. | Nem suçların yalnız sisteme yıkılmasını önler. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C71 | Bedel — plan: Yakın / Ishra. Ishra kendi siyasi geleceğini tehlikeye atacak gerçeği düşünür. | Ishra konuşur. | Yakın · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | — | 3.ISHRA · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C72 | Yanıt — plan: Yakın / Nem. Nem makamın korunmasını insanların yaşamasından üstün tutmaz. | Nem konuşur. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G06 | ✍️ | — | — | — |
| C73 | Nith hattı kesiyor — plan: Orta / Nith. Nith resmî dış aktarımı kapatır. Salonun yaşam sistemi ve yörüngesi normal kalır. | Nith resmî dış aktarımı kapatır. Salonun yaşam sistemi ve yörüngesi normal kalır. | Orta · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | T01 masadaki fiziksel kumandaya basma (A07 'simple physical controls') · Nith dış aktarımı kapatır: okunacak ekran yok (T06) · salonun yaşam sistemi ve yörüngesi normal (plan) | 6.NITH · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C74 | Kendi kaydı — plan: Yakın / Nem. Nem yeni cihaz aramak yerine Orun'un mevcut küpüne döner. | Nem yeni cihaz aramak yerine Orun'un mevcut küpüne döner. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C75 | Bağımsız hat — plan: Yakın / Orun. Orun K1'in özel kanal ışığını açar. | Orun K1'in özel kanal ışığını açar. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T01 ışığı açma · T09 K1 özel kanal ışığı (plan A10) | 5.ORUN · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C76 | Paranın yolu — plan: İkili / Nem-Orun. Nem küpü kapmaz; Orun'dan açıkça ister. | Nem küpü kapmaz; Orun'dan açıkça talep eder. | İkili · Nem-Orun | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) · Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T15/T16 iki yüz: model sesi yalnız Nem; Orun yanıtı kurguda → Orun arkadan ya da flu, ağzı kapalı (plan) · Nem küpü kapmaz (plan) | 1.NEM · 5.ORUN · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C77 | Risk Orun'da — plan: Yakın / Nith. Nith ekonomik korumayı çekmekle tehdit eder. | Nith ekonomik korumayı çekmekle tehdit eder. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | — | 6.NITH · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C78 | Açık karar — plan: Yakın / Orun. Orun K1'i masanın merkezine iter ve özel kanalı açık bırakır. | Orun K1'i masanın merkezine iter ve özel kanalı açık bırakır. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | T01 K1'i masanın merkezine itme · T09 C78 sonrası cyan yayın ışığı (plan A10) | 5.ORUN · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C79 | Kaynak yayında — plan: Detay / K1 ve Nem. Nem kaynak ses ve görüntünün dört filo ağına değiştirilmeden gitmesini ister. | Nem konuşur; kaynak ses ve görüntünün dört filo ağına değiştirilmeden gitmesini talep eder. | Detay · K1 ve Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | plan pilotu · T09 K1 yayın durumu · T06 okunacak ekran yok | 1.NEM · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C80 | Yalanın son savunması — plan: Yakın / Nith. Nith elçileri kendi suçlarıyla susturmaya çalışır. | Nith elçileri kendi suçlarıyla susturmaya çalışır. | Yakın · Nith | Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | BT §A 'murderers' model sesi repliğinde → red gelirse kayda | 6.NITH · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C81 | Başlangıç — plan: Yakın / Nem. Nem açık kayıt alanına bakar. | Nem açık kayıt alanına bakar. | Yakın · Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | — | 1.NEM · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C82 | Arşiv korunacak — plan: Yakın / Silex. Silex K2 kayıt taşını K1'in yanına bırakır; bağımsız kopyayı yayına ekler. | Silex K2 kayıt taşını K1'in yanına bırakır; bağımsız kopyayı yayına ekler. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | T01 taşı bırakma · T09 K2 K1'in yanına (plan A11) | 4.SILEX · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C83 | Nith'in hamlesi — plan: Orta / Nith-Orun. Nith küpe uzanır; Orun önkoluyla yolunu kapatır. Tek engelleme hareketi. | Nith küpe uzanır; Orun önkoluyla yolunu kapatır. Tek engelleme hareketi. | Orta · Nith-Orun | Orun saat 10 (okra-kahve koltuk) · Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | T01 tek engelleme hareketi: Nith uzanır, Orun önkoluyla yolu kapatır (plan) · iki yüz: model sesi yalnız Orun; Nith yanıtı kurguda, ağzı kapalı | 5.ORUN · 6.NITH · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C84 | Masaya dön — plan: Orta / Vekh. Vekh Nith ile merkez arasına girer; masadaki silahı eline almaz. | Vekh Nith ile merkez arasına girer; masadaki silahı eline almaz. | Orta · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T09 Vekh masadaki silahı eline almaz (plan) | 2.VEKH · 7.ACCORD_CHAMBER | G07 | ✍️ | — | — | — |
| C85 | Dört filoya — plan: Geniş / yeni masa düzeni. Nith etkisiz biçimde arka plandadır. Nem merkezde; dört elçi kendi kaydına döner. | Nith etkisiz biçimde arka plandadır. Nem merkezde; dört elçi kendi kaydına döner. | Geniş · yeni masa düzeni | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | T15 kişi sayısı: Nem merkezde, Nith arka planda, dört elçi (plan) · ≤3 referans: diğerleri arka/flu (plan) | 1.NEM · 6.NITH · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C86 | Vekh'in emri — plan: Yakın / Vekh. Vekh doğrudan kendi filosuna konuşur; silahı masada hareketsiz kalır. | Vekh doğrudan kendi filosuna konuşur; silahı masada hareketsiz kalır. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | T09 silah masada hareketsiz (plan) | 2.VEKH · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C87 | Ishra'nın emri — plan: Yakın / Ishra. Ishra önce hastane gemilerine geçit açılmasını ister. | Ishra önce hastane gemilerine geçit açılmasını talep eder. | Yakın · Ishra | Ishra saat 4 (teal koltuk) | 10 | Frames to Video | — | 3.ISHRA · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C88 | Silex'in emri — plan: Yakın / Silex. Silex kendi ittifakının gemilerine ve arşivine seslenir. | Silex kendi ittifakının gemilerine ve arşivine seslenir. | Yakın · Silex | Silex saat 8 (soluk gümüş-mor koltuk) | 10 | Frames to Video | — | 4.SILEX · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C89 | Orun'un emri — plan: Yakın / Orun. Orun ticaret filosuna kâr yerine hayatta kalanları taşıma görevi verir. | Orun ticaret filosuna kâr yerine hayatta kalan herkesi taşıma görevi verir. | Yakın · Orun | Orun saat 10 (okra-kahve koltuk) | 10 | Frames to Video | BT §A 'weapons' model sesi repliğinde → red gelirse kayda | 5.ORUN · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C90 | Silahlar sönüyor — plan: Çok geniş / uzay. Vekh filosunun silah hatları söner; formasyon karşı taraftan açılır. Yeni savaş başlamaz. | Vekh filosunun silah hatları söner; formasyon karşı taraftan açılır. Yeni savaş başlamaz. (ses: Diyalog yok. Ortam, gerilim ve ölçek için nefes alanı.) | Çok geniş · uzay | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | T13 · T18 · Vekh filosunun silah hatları söner, formasyon açılır; yeni savaş başlamaz (plan) | 8.BLACK_HOLE_STATION · 9.FOUR_FLEETS | G08 | ✍️ | — | — | — |
| C91 | Koridor açılıyor — plan: Çok geniş / sonuç. Ishra'nın beyaz-teal gemileri koridor açar; küçük tıbbi/sivil gemiler aradan geçer. | Ishra'nın beyaz-teal gemileri koridor açar; küçük tıbbi/sivil gemiler aradan geçer. (ses: Diyalog yok. Ortam, gerilim ve ölçek için nefes alanı.) | Çok geniş · sonuç | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | T13 · T18 · beyaz-teal gemiler koridor açar, küçük tıbbi/sivil gemiler geçer (plan) | 8.BLACK_HOLE_STATION · 9.FOUR_FLEETS | G08 | ✍️ | — | — | — |
| C92 | Başka bir tercüman — plan: Yakın / Nith-Nem. Nith son sözü almaya çalışır; Nem kısaca karşılık verir. | Nith son sözü almaya çalışır; Nem kısaca karşılık verir. | Yakın · Nith-Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) · Nith saat 12 (cam önündeki baş koltuk, fildişi-siyah) | 10 | Frames to Video | iki yüz: model sesi yalnız Nith; Nem yanıtı kurguda → Nem arkadan ya da flu, ağzı kapalı (plan) | 1.NEM · 6.NITH · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C93 | Yerine değil yanında — plan: İkili / Ishra-Nem. Ishra Nem'e yeni bir makam önerir; Nem göz hizasını eşit tutar. | Ishra Nem'e yeni bir makam önerir; Nem göz hizasını eşit tutar. | İkili · Ishra-Nem | Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) · Ishra saat 4 (teal koltuk) | 10 | Frames to Video | iki yüz: model sesi yalnız Ishra; Nem yanıtı kurguda, ağzı kapalı; Nem göz hizasını eşit tutar (plan) | 1.NEM · 3.ISHRA · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C94 | Geçen günler — plan: Geniş / cam ve masa. Silex ile Nem kara deliğin ışığı önünde; diğerleri arka planda küçük kalır. | Silex ile Nem kara deliğin ışığı önünde; diğerleri arka planda küçük kalır. | Geniş · cam ve masa | Silex saat 8 (soluk gümüş-mor koltuk) · Nem saat 6 (yakın taraf, küçük kalay kâtip yeri; C06'dan sonra çoğunlukla ayakta) | 10 | Frames to Video | T15 Silex ile Nem önde, diğerleri arka planda küçük (plan) · Nem yanıtı kurguda | 4.SILEX · 1.NEM · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C95 | İlk cümlenin karşılığı — plan: Yakın / Vekh. Vekh açık kaynak kaydına son kez konuşur. Araya değiştirilmiş ses girmez. | Vekh açık kaynak kaydına son kez konuşur. Araya değiştirilmiş ses girmez. | Yakın · Vekh | Vekh saat 2 (bronz-kırmızı koltuk) | 10 | Frames to Video | BT §A 'fire' model sesi repliğinde → red gelirse kayda · araya değiştirilmiş ses girmez (plan) | 2.VEKH · 7.ACCORD_CHAMBER | G08 | ✍️ | — | — | — |
| C96 | Olduğu gibi — plan: Çok geniş / final. Aynı istasyon kara deliğin ışık yayı önünde; filolar ayrılmış, açık koridor kalmıştır. | Aynı istasyon kara deliğin ışık yayı önünde; filolar ayrılmış, açık koridor kalmıştır. | Çok geniş · final | dört filo ayrı gruplar, açık koridor; istasyon olay ufkunun dışında (plan A08 · A09) | 10 | Frames to Video | T13 · T18 · Nem VO kurguda · başlık son dış görüntünün üzerine eklenebilir (plan) | 8.BLACK_HOLE_STATION · 9.FOUR_FLEETS | G08 | ✍️ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10; toplam = HEDEF_SURE.
  Plan: "Her video için hedef 10 saniyelik tek sürekli yatay plandır." · "96 × 10 saniye = 960 saniye = 16:00."
Flow modu: Frames to Video · Ingredients to Video · Text to Video (yalnız kimliksiz çekim).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir"; BT = BILINEN_TUZAKLAR.
KADRAJ DIŞI REPLİK (bütün film, plan: "Bir klipte ön planda bir konuşmacı oynatmak yeterlidir. İkinci replik dinleyenin tepkisi veya masadaki nesne
  üzerinde kadraj dışı verilebilir." · "Kaynak ile resmî röleyi aynı hareketli ağza söyletme"): §5 Kaynak "kadraj dışı · makine · kayıt" olan
  replik videoda üretilmez; o sırada kadrajdaki kişinin ağzı kapalıdır, dinler (REPLIK §3). İki yüzlü planda (C07 C57 C76 C83 C92 C93 C94)
  yanıtı kurguda olan elçi arkadan ya da flu (plan) — iki yüzün de konuşması sahibin SK1 kararına bağlı (ODA/DURUM.md).
PLAN PİLOTU (plan: "İlk küçük deneme için C01, C61 ve C79 anlamlıdır."): C01 iki ses katmanı · C61 yabancı yüzün sakin konuşması + alıcının çıkarılması ·
  C79 küçük sabit nesnenin yayın durumuna geçmesi. Referanslardan sonra ilk üretilen üç çekim (Flow iş emri).
Zincir: plan zincir istemez ("Görüntüde düz kesmeler toplamı korur") → Zincir · Baş. · Bitiş "—"; SAHNELEME.md §5 "zincir yok".
Grup: PROMPTLAR/<Grup>.md (12 çekim). Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
```

### AÇILIŞ — ilk 30 saniye (`uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §2 · plan "İlk 10, 30 ve 60 saniye" tablosundan, Fable)

| Saniye | Çekim | Sorun ya da beklenmedik hareket | İnsan (beden · el · yüz) | Replik · ekran yazısı | Kapak bağı | Sesi kapalı okunur mu |
|---|:--:|---|---|---|---|:--:|
| 0-10 | C01 | "We did not fire first" cümlesi resmî sesle "We fired first" olur (plan) | yüz: Vekh yakın, arkasında kara delik | Vekh (model sesi, 2,0 s'den) + röle (kurguda) · görüntüde yazı yok | kapak üçlüsünden Vekh + kara delik (plan kapak fikri) | hayır — bilgi iki seste; altyazıyla evet |
| 10-20 | C02 | Ishra aldığı itirafa tepki verir; gözleri daralır (plan) | yüz: Ishra, su başlığında | Ishra: Then you came here to boast about it? | kapak üçlüsünden Ishra | tepki evet; söz altyazıyla |
| 20-30 | C03 | dışarıda dört filo; birkaç silah hattı aydınlanır (plan) | — | yok | kara delik (kapak arka planı) | evet |

```
İlk 30 s'de yok: logo · "sunar" kartı · siyah ekran · karartmadan açılma · saf manzara · görüntüde yazı ·
  kalabalık · hızlı kamera · karmaşık el-nesne teması · kusurlu ama "gerekli" çekim.
Plan korundu (sahip talimatı; ILK_30 TERCİH/HİPOTEZ): C01'de iki replik (Vekh + röle; kılavuz F4 "C01'de en çok bir kısa replik") ve plan video promptundaki
  "a low tense score" (kılavuz "müzik C01'de girmiyor"). İlk 2 s insan sesi yok kuralı planla çelişmez: plan saniye vermez, Vekh 2,0 s'den.
Plan "SOURCE / OFFICIAL RELAY grafik etiketleri kurgu katmanında kullanılabilir" ↔ kılavuz "ilk 30 s'de görüntüde yazı yok": görüntü modeline yazı
  yok (ikisi aynı); kurgu etiketi planın seçeneği → F8'de sahip.
C03 saf manzara değil: tehlike olayı (silah hatları aydınlanır), plan.
```

## 5. REPLİKLER

<!-- kaynak: plan senaryo, 171 replik BİREBİR (konuşan etiketi planın kendisi). Kaynak: planın "ön planda bir konuşmacı" kuralı → klibin plan öznesi olan ilk canlı
     konuşmacı = model sesi (ağız kadrajda), aynı klipte aynı kişinin ikinci cümlesi de; geri kalanı kurguda (kadraj dışı · makine = OFFICIAL RELAY · kayıt = eski kayıt
     ve filo mesajı · voice-over = C96). Saniye ve süre Fable tahmini (2,5 kelime/sn + cümle arası 0,2 s; ilk replik 1,0 s'de, C01'de 2,0 s; aradaki boşluk 0,6 s);
     ölçülmedi — plan: "Diyalog için gerçek okuma süresi ölçülmeli." -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R001 | C01 | 2,0 | VEKH / ORIGINAL | model sesi (ağız kadrajda) | HUMAN | We did not fire first. | 2,0 |
| R002 | C01 | 4,6 | OFFICIAL RELAY / FALSE | makine | MACHINE | We fired first. | 1,2 |
| R003 | C02 | 2,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | Then you came here to boast about it? | 3,2 |
| R004 | C04 | 2,0 | NEM | model sesi (ağız kadrajda) | HUMAN | That's not what he said. | 2,0 |
| R005 | C04 | 4,6 | SILEX | kadraj dışı | HUMAN | Which word did it change? | 2,0 |
| R006 | C05 | 2,0 | NITH | model sesi (ağız kadrajda) | HUMAN | The clerk does not address the council. | 2,8 |
| R007 | C06 | 2,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Your translator just declared a war. | 2,4 |
| R008 | C06 | 5,0 | NITH | kadraj dışı | HUMAN | Wars aren't started by clerks misunderstanding a sentence. | 3,2 |
| R009 | C07 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | I denied the attack. | 1,6 |
| R010 | C07 | 3,2 | ISHRA | kadraj dışı | HUMAN | I heard you claim it. | 2,0 |
| R011 | C08 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | The relay has no nation. It cannot take sides. | 3,8 |
| R012 | C08 | 5,4 | ISHRA | kadraj dışı | HUMAN | It just spoke like an enemy. | 2,4 |
| R013 | C09 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Who certified it? | 1,2 |
| R014 | C09 | 2,8 | NITH | kadraj dışı | HUMAN | This chamber. | 0,8 |
| R015 | C10 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | Every delay costs money. Shall we argue more efficiently? | 3,8 |
| R016 | C10 | 5,4 | VEKH | kadraj dışı | HUMAN | You can count money after we count bodies. | 3,2 |
| R017 | C11 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | One word vanished. Not. Everything after it became a confession. | 4,4 |
| R018 | C11 | 6,0 | SILEX | kadraj dışı | HUMAN | An absence with a very precise effect. | 2,8 |
| R019 | C12 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | Then test a sentence none of us can mistake. | 3,6 |
| R020 | C12 | 5,2 | NITH | kadraj dışı | HUMAN | This chamber is not a laboratory. | 2,4 |
| R021 | C13 | 1,0 | VEKH / ORIGINAL | model sesi (ağız kadrajda) | HUMAN | My hands are empty. | 1,6 |
| R022 | C13 | 3,2 | OFFICIAL RELAY / FALSE | makine | MACHINE | My weapons are ready. | 1,6 |
| R023 | C14 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | His hands are empty. Why did I hear a threat? | 4,2 |
| R024 | C14 | 5,8 | VEKH | kadraj dışı | HUMAN | Because someone wanted you afraid of me. | 2,8 |
| R025 | C15 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | The system translates intent, not primitive sounds. | 2,8 |
| R026 | C15 | 4,4 | NEM | kadraj dışı | HUMAN | Whose intent? The speaker's, or yours? | 2,6 |
| R027 | C16 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Then it isn't translating. It's issuing orders in our voices. | 4,2 |
| R028 | C16 | 5,8 | SILEX | kadraj dışı | HUMAN | And charging us to obey them. | 2,4 |
| R029 | C18 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | My intent belongs to me. | 2,0 |
| R030 | C18 | 3,6 | NITH | kadraj dışı | HUMAN | Not once it threatens another state. | 2,4 |
| R031 | C19 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | At the last summit, we asked for an evacuation corridor. | 4,0 |
| R032 | C19 | 5,6 | NEM | kadraj dışı | HUMAN | The source should still say that. | 2,4 |
| R033 | C20 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | I received a demand for our undefended coast. | 3,2 |
| R034 | C20 | 4,8 | ISHRA | kadraj dışı | HUMAN | Our wounded were on that coast. | 2,4 |
| R035 | C21 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Play the source, not the certified version. | 2,8 |
| R036 | C21 | 4,4 | NITH | kadraj dışı | HUMAN | The certified version is the only legal record. | 3,2 |
| R037 | C22 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Sources are discarded after certification. To prevent confusion. | 3,4 |
| R038 | C22 | 5,0 | VEKH | kadraj dışı | HUMAN | You destroyed the evidence and called it clarity. | 3,2 |
| R039 | C23 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | My recorder kept both channels. It doesn't require your permission. | 4,2 |
| R040 | C23 | 5,8 | NITH | kadraj dışı | HUMAN | Private recordings have no standing here. | 2,4 |
| R041 | C24 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | That reply was loaded before he finished speaking. | 3,2 |
| R042 | C24 | 4,8 | SILEX | kadraj dışı | HUMAN | A prepared answer to an unheard sentence. | 2,8 |
| R043 | C25 | 1,0 | ISHRA / RECORDED ORIGINAL | kayıt | HUMAN | We request a pause to recover our dead. | 3,2 |
| R044 | C25 | 4,8 | NEM | kadraj dışı | HUMAN | Listen to what the relay delivered instead. | 2,8 |
| R045 | C26 | 1,0 | OFFICIAL RELAY / FALSE RECORDING | kayıt | MACHINE | We request time to prepare another attack. | 2,8 |
| R046 | C26 | 4,4 | VEKH | model sesi (ağız kadrajda) | HUMAN | That was the message we answered. | 2,4 |
| R047 | C27 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | We shelled the harbour after that message. | 2,8 |
| R048 | C27 | 4,4 | ISHRA | kadraj dışı | HUMAN | There were no guns in that harbour. | 2,8 |
| R049 | C28 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | War makes every old recording look like evidence. | 3,2 |
| R050 | C28 | 4,8 | SILEX | kadraj dışı | HUMAN | Only if you burn the source. | 2,4 |
| R051 | C29 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | And what does it make your weapons shipments? | 3,2 |
| R052 | C29 | 4,8 | ORUN | kadraj dışı | HUMAN | I sold what your governments requested. | 2,4 |
| R053 | C30 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | Legal. Both sides paid. | 1,8 |
| R054 | C30 | 3,4 | ISHRA | kadraj dışı | HUMAN | Were our deaths included in the price? | 2,8 |
| R055 | C32 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Who collected the fee for every translated threat? | 3,2 |
| R056 | C32 | 4,8 | ORUN | kadraj dışı | HUMAN | You already know whose seal is on it. | 3,2 |
| R057 | C33 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Sign the provisional accord. We can audit the past afterward. | 4,2 |
| R058 | C33 | 5,8 | NEM | kadraj dışı | HUMAN | After you erase what happened here? | 2,4 |
| R059 | C34 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | Your accord requires us to keep using your relay. | 3,6 |
| R060 | C34 | 5,2 | NITH | kadraj dışı | HUMAN | Continuity prevents another misunderstanding. | 1,6 |
| R061 | C35 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Without it, you have no common language. | 2,8 |
| R062 | C35 | 4,4 | NEM | kadraj dışı | HUMAN | We also have no reason to trust yours. | 3,2 |
| R063 | C36 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | We lack a common language. Not a reason to listen. | 4,2 |
| R064 | C36 | 5,8 | SILEX | kadraj dışı | HUMAN | Begin with the words he took away. | 2,8 |
| R065 | C37 | 1,0 | SILEX | kadraj dışı | HUMAN | Six minutes in this chamber. Three days on the fleet clock. | 4,6 |
| R066 | C37 | 6,2 | ISHRA | kadraj dışı | HUMAN | Three days of unanswered calls. | 2,0 |
| R067 | C38 | 1,0 | FLEET MESSAGE / ARCHIVE | kayıt | HUMAN | Third day. No reply. The ceasefire window is closing. | 4,0 |
| R068 | C38 | 5,6 | VEKH | kadraj dışı | HUMAN | That is my admiral. Why was it withheld? | 3,4 |
| R069 | C39 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | When did that arrive? | 1,6 |
| R070 | C39 | 3,2 | NITH | kadraj dışı | HUMAN | When it became relevant. | 1,6 |
| R071 | C41 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | All four fleets requested a pause. None reached this table. | 4,2 |
| R072 | C41 | 5,8 | NEM | kadraj dışı | HUMAN | Only their threats were considered relevant. | 2,4 |
| R073 | C42 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Signals distort near a black hole. | 2,4 |
| R074 | C42 | 4,0 | SILEX | kadraj dışı | HUMAN | Not selectively by diplomatic meaning. | 2,0 |
| R075 | C43 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Gravity didn't remove only ceasefires. Someone chose what we heard. | 4,2 |
| R076 | C43 | 5,8 | NITH | kadraj dışı | HUMAN | Someone must decide which messages matter. | 2,4 |
| R077 | C44 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | My hospital ships have been waiting for an answer. | 3,6 |
| R078 | C44 | 5,2 | ORUN | kadraj dışı | HUMAN | My supply ships received no clearance either. | 2,8 |
| R079 | C45 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | You spent their last days choosing our words. | 3,2 |
| R080 | C45 | 4,8 | NITH | kadraj dışı | HUMAN | I kept your delegations alive to negotiate. | 2,8 |
| R081 | C46 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Neutrality is expensive. | 1,2 |
| R082 | C46 | 2,8 | NEM | kadraj dışı | HUMAN | You keep presenting us with the bill. | 2,8 |
| R083 | C47 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Orun. Show us who keeps paying when talks fail. | 3,8 |
| R084 | C47 | 5,4 | ORUN | kadraj dışı | HUMAN | Showing you will cost me everything. | 2,4 |
| R085 | C48 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | Those accounts are private. | 1,6 |
| R086 | C48 | 3,2 | NEM | kadraj dışı | HUMAN | So were the graves. | 1,6 |
| R087 | C49 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | Every failed summit renews his security contracts. | 2,8 |
| R088 | C49 | 4,4 | VEKH | kadraj dışı | HUMAN | So peace would end his income. | 2,4 |
| R089 | C50 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | I certified it. His contracts kept it running. | 3,4 |
| R090 | C50 | 5,0 | NEM | kadraj dışı | HUMAN | A war that pays for its own witness. | 3,2 |
| R091 | C51 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | You profit every time they misunderstand each other. | 3,2 |
| R092 | C51 | 4,8 | NITH | kadraj dışı | HUMAN | You brought the hatred. I gave it grammar. | 3,4 |
| R093 | C52 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | I sell certainty. They pay to hear that they're right. | 4,2 |
| R094 | C52 | 5,8 | ISHRA | kadraj dışı | HUMAN | Even when the answer is a lie. | 2,8 |
| R095 | C53 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | I never ordered a single ship to fire. | 3,2 |
| R096 | C53 | 4,8 | VEKH | kadraj dışı | HUMAN | You only made us hear an order. | 2,8 |
| R097 | C54 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | You made every reply sound like permission. | 2,8 |
| R098 | C54 | 4,4 | NITH | kadraj dışı | HUMAN | Permission was what you came here seeking. | 2,8 |
| R099 | C55 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | How many ceasefire offers did you suppress? | 2,8 |
| R100 | C56 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | As many as the process required. | 2,4 |
| R101 | C56 | 4,0 | NEM | kadraj dışı | HUMAN | Your process needed them to keep dying. | 2,8 |
| R102 | C57 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | You armed the ships that trapped our wounded. | 3,2 |
| R103 | C57 | 4,8 | ORUN | kadraj dışı | HUMAN | I know. | 0,8 |
| R104 | C58 | 1,0 | NEM / ORIGINAL | model sesi (ağız kadrajda) | HUMAN | Do not draw your weapon. | 2,0 |
| R105 | C58 | 3,6 | OFFICIAL RELAY / FALSE | makine | MACHINE | Draw your weapon. | 1,2 |
| R106 | C59 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | You both chose this. | 1,6 |
| R107 | C59 | 3,2 | ORUN | kadraj dışı | HUMAN | And shooting me would serve him again. | 2,8 |
| R108 | C60 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Look at my hands. Stop listening to the speaker. | 3,8 |
| R109 | C60 | 5,4 | NITH | kadraj dışı | HUMAN | Step aside. The general has heard enough. | 3,0 |
| R110 | C61 | 4,0 | NEM / VEKH'S LANGUAGE | model sesi (ağız kadrajda) | HUMAN | My hands are empty. I am not your enemy. | 3,8 |
| R111 | C62 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | The relay told me to draw. | 2,4 |
| R112 | C62 | 4,0 | NEM | kadraj dışı | HUMAN | I told you not to. | 2,0 |
| R113 | C63 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Who should decide what you meant? | 2,4 |
| R114 | C63 | 4,0 | VEKH | kadraj dışı | HUMAN | My voice should still belong to me. | 2,8 |
| R115 | C64 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | Say it again. | 1,2 |
| R116 | C64 | 2,8 | NEM / VEKH'S LANGUAGE | kadraj dışı | HUMAN | I am not your enemy. | 2,0 |
| R117 | C64 | 5,4 | NEM | kadraj dışı | HUMAN | Now you heard me. Not his correction. | 3,0 |
| R118 | C65 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Without me, this room becomes noise. | 2,4 |
| R119 | C65 | 4,0 | ISHRA | kadraj dışı | HUMAN | Then we will learn to hear it. | 2,8 |
| R120 | C66 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | For once, let them hear what the noise is saying. | 4,0 |
| R121 | C66 | 5,6 | SILEX | kadraj dışı | HUMAN | One voice at a time. Without substitutions. | 3,0 |
| R122 | C67 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | Translate his words. Not what you think he deserves. | 3,8 |
| R123 | C67 | 5,4 | NEM | kadraj dışı | HUMAN | That is all translation ever owed you. | 2,8 |
| R124 | C68 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | I ordered the harbour shelled. That part was mine. | 3,8 |
| R125 | C68 | 5,4 | ISHRA | kadraj dışı | HUMAN | Then you will answer for that order. | 2,8 |
| R126 | C69 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | I sold to both sides. No machine signed those invoices. | 4,2 |
| R127 | C69 | 5,8 | SILEX | kadraj dışı | HUMAN | Keep that sentence in the source record. | 2,8 |
| R128 | C70 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | He changed the words. You sent the ships. | 3,4 |
| R129 | C70 | 5,0 | VEKH | kadraj dışı | HUMAN | Then record our orders too. As we give them. | 3,8 |
| R130 | C71 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | I closed the evacuation lanes. Telling them could cost me my command. | 5,0 |
| R131 | C72 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Then let them live long enough to choose. | 3,2 |
| R132 | C72 | 4,8 | ISHRA | kadraj dışı | HUMAN | Open a channel they can actually hear. | 2,8 |
| R133 | C73 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | No uncertified message leaves my station. | 2,4 |
| R134 | C73 | 4,0 | VEKH | kadraj dışı | HUMAN | The messages are ours. Not your property. | 3,0 |
| R135 | C74 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | You never use his network for your own accounts. | 3,6 |
| R136 | C75 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | Would you? My relay reaches my ships directly. | 3,4 |
| R137 | C75 | 5,0 | SILEX | kadraj dışı | HUMAN | Beyond his certification. Beyond his edits. | 2,6 |
| R138 | C76 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Then let the truth travel the way your money does. | 4,0 |
| R139 | C76 | 5,6 | ORUN | kadraj dışı | HUMAN | It was never meant for an open broadcast. | 3,2 |
| R140 | C77 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | Open that channel and every protected contract you own is gone. | 4,4 |
| R141 | C77 | 6,0 | NEM | kadraj dışı | HUMAN | What are the contracts worth without survivors? | 2,8 |
| R142 | C78 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | Then I will finally own something I didn't buy. | 3,6 |
| R143 | C78 | 5,2 | ISHRA | kadraj dışı | HUMAN | A choice. Let that be the first. | 3,0 |
| R144 | C79 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Original voices. Original faces. No substituted lines. | 3,2 |
| R145 | C79 | 4,8 | SILEX | kadraj dışı | HUMAN | The source travels with every translated line. | 2,8 |
| R146 | C80 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | They won't trust murderers asking for peace. | 2,8 |
| R147 | C80 | 4,4 | VEKH | kadraj dışı | HUMAN | They don't have to trust us to hear us. | 3,6 |
| R148 | C81 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Then we begin with what we did. | 2,8 |
| R149 | C81 | 4,4 | ORUN | kadraj dışı | HUMAN | Before he can call this another error. | 2,8 |
| R150 | C82 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | My copy goes with the broadcast. No one deletes the source. | 4,6 |
| R151 | C82 | 6,2 | NITH | kadraj dışı | HUMAN | You would destroy every agreement we built. | 2,8 |
| R152 | C83 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | You don't get to edit this one. | 2,8 |
| R153 | C83 | 4,4 | NITH | kadraj dışı | HUMAN | This room exists because I keep it neutral. | 3,2 |
| R154 | C84 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | Sit down. You can answer for every word. | 3,4 |
| R155 | C84 | 5,0 | NEM | kadraj dışı | HUMAN | Alive. There will be no corrected version. | 3,0 |
| R156 | C85 | 1,0 | NEM | model sesi (ağız kadrajda) | HUMAN | Tell your fleets what you mean. I'll preserve what you say. | 4,6 |
| R157 | C85 | 6,2 | SILEX | kadraj dışı | HUMAN | And the record will remain public. | 2,4 |
| R158 | C86 | 1,0 | VEKH | model sesi (ağız kadrajda) | HUMAN | I order my fleet to withdraw. I will answer for the harbour. | 5,0 |
| R159 | C87 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | Open the evacuation lanes. All ships, stand down. | 3,4 |
| R160 | C88 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | Suspend the relay. Preserve every unaltered recording. | 3,0 |
| R161 | C88 | 4,6 | SILEX | model sesi (ağız kadrajda) | HUMAN | No translation replaces the words it claims to carry. | 3,6 |
| R162 | C89 | 1,0 | ORUN | model sesi (ağız kadrajda) | HUMAN | No more weapons deliveries. My ships will carry survivors. | 3,8 |
| R163 | C89 | 5,4 | ORUN | model sesi (ağız kadrajda) | HUMAN | Send their arrival times without a security surcharge. | 3,2 |
| R164 | C92 | 1,0 | NITH | model sesi (ağız kadrajda) | HUMAN | They'll build another translator. | 1,6 |
| R165 | C92 | 3,2 | NEM | kadraj dışı | HUMAN | Then they'll keep the original. | 2,0 |
| R166 | C93 | 1,0 | ISHRA | model sesi (ağız kadrajda) | HUMAN | Will you speak for us? | 2,0 |
| R167 | C93 | 3,6 | NEM | kadraj dışı | HUMAN | Beside you. Never instead of you. | 2,6 |
| R168 | C94 | 1,0 | SILEX | model sesi (ağız kadrajda) | HUMAN | We can't recover those days. | 2,0 |
| R169 | C94 | 3,6 | NEM | kadraj dışı | HUMAN | We can stop wasting the next one. | 2,8 |
| R170 | C95 | 1,0 | VEKH / ORIGINAL | model sesi (ağız kadrajda) | HUMAN | We will not fire. | 1,6 |
| R171 | C96 | 1,0 | NEM / VO | kadraj dışı (voice-over) | HUMAN | That is what he said. | 2,0 |

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        model sesi (ağız kadrajda) → replik video promptuna BİREBİR yazılır, model konuşmayı videoda üretir (sahip kararı 12.10.2026);
        ≤ 5 s; klip sesi yalnız replik penceresinde filme girer (timeline klip_sesi), kurgu kaydı yedek
Kayıt: HUMAN | MACHINE (OFFICIAL RELAY) · bant: 16 dk 40-70 replik
Sayım: 171 replik = 88 model sesi + 83 kurguda (kadraj dışı 76 · makine 3 = röle C01 C13 C58 · kayıt 3 = C25 C26 C38 · voice-over 1 = C96). 90 klipte söz, 6 klipte yok (C03 C17 C31 C40 C90 C91).
Bant dışı gerekçesi: 171 replik sahibin planıdır ("Altı farklı uzaylı türü · 171 kısa İngilizce replik"); sahip talimatı "plandan asla dışarı çıkma".
Ses profilleri: §1 kadro tablosu (plan "Ses" sütunu). Plan: "Karakter başına aynı ses niyeti ve mümkünse aynı ses kaynağı korunmalı." ·
  "Belirli bir video modelinin altı karakteri her seferinde aynı sesle üretebildiği varsayılmaz." → bir konuşmacının model sesi tutmazsa
  o konuşmacının satırları kayda geçer (REPLIK §1, P18); metin değişmez.
Şiddet kelimeli model sesi replikleri (BT §A, red riski): R001 C01 · C27 · C29 · C53 · C57 ('wounded') · C58 · C68 · C80 · C89 · C95 — red gelirse yalnız o replik kayda
  geçer (plan: "Bu ikinci ses gerekirse ayrı hazırlanıp kurguda eklenir"); metin değişmez.
Kurguda eklenecek 83 replik = kayıt listesi (ses/R<nnn>.wav, No sütunuyla). Kim/hangi araçla kaydedileceği sahibin (REPLIK §1).
```

## 6. SES PLANI — model sesi yalnız §5 "model sesi" replikleri için; ortam, efekt, müzik ve kurgu replikleri ayrı katman

<!-- kaynak: plan "Müzik ve çevre sesi" bölüm tablosu birebir; katman ve köprü sütunları plan cümlelerinden. -->
| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| B1 00:00–02:00 | replik · oda yatağı (Y1) · az müzik | kadraj dışı yanıt J/L ("İkinci replik … kadraj dışı verilebilir") | plan: "İlk kaynak ve yanlış resmî cümle net. Az müzik; suskunluk şüpheyi büyütür." |
| B2 02:00–04:00 | replik · oda yatağı · küçük bas nabzı | aynı | plan: "Testlerde sakin oda sesi. "Intent" savunması sırasında küçük bas nabzı." |
| B3 04:00–06:00 | replik · eski kayıt (farklı yerleşim) · oda yatağı · müzik | aynı | plan: "Eski özgün kayıt ile değiştirilmiş sürüm farklı ses yerleşiminde." |
| B4 06:00–08:00 | replik · filo çağrısı (kayıt) · oda yatağı · müzik boşluğu | aynı | plan: "Saat farkında boşluk açılır; filo çağrısı boğulmadan duyulur." |
| B5 08:00–10:00 | replik · oda yatağı · daralan müzik · kısa sert vurgu (C59) | aynı | plan: "Maddi çıkarlar açılırken ritim daralır. Silah çekilince kısa, sert vurgu." |
| B6 10:00–12:00 | replik (çıplak) · oda yatağı · sıcaklaşan müzik | aynı | plan: "Alıcılar çıktığında resmî sesin varlığı azalır; yüz yüze sesler çıplaklaşır." |
| B7 12:00–14:00 | replik · oda yatağı · sessizlik (C73) · K1 sıcak küçük ton (C75) | aynı | plan: "Dış bağlantı kapanınca sessizlik; K1 açıldığında sıcak, küçük bir ton." |
| B8 14:00–16:00 | emirler · kaynak ses · ölçülü tema · dış yatak (Y2) | aynı | plan: "Emirler ve kaynak ses ön planda. Finalde gösterişli zafer yerine tamamlanan, ölçülü bir tema." |

```
Ortam: iç hacim (salon) hava taşır — oda yatağı, havalandırma (plan C01 "Quiet chamber ventilation") · dış vakum: plan "Kara delik görüntüsünün
  dış vakum planlarında hava içindeymiş gibi motor gürültüsü veya patlama sesi gerekmiyor; müzik ve soyut gerilim dokusu kullanılabilir."
Plan: "İlk cümle müziğin altında kaybolmaz. Resmî sesin soğuk tınısı, karakterlerin canlı sesinden ayrılır. Masadaki özel röle ve kayıt taşının
  sesleri kısa ve tutarlı kalır."
Plan: "Gerekirse sözün sonu bir sonraki dinleme veya manzara planına ses köprüsüyle taşınır; 96 görüntü aralığının toplamı korunur."
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt listesi: §5 Kaynak ≠ model sesi olan 83 satır · efekt listesi F4 ses-tasarimcisi (açılmadı; plan efekt listesi vermez → F8'de, plan ses davranışıyla)
```

### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | Görüşme salonu (iç hacim) | C01-C02 · C04-C30 · C32-C37 · C39 · C41-C89 · C92-C95 | quiet chamber ventilation and distant table resonance in a large stone-metal room (plan C01 · C04 kelimeleri) | replik altında, F8 | `O01.wav` |
| Y2 | Dış uzay (vakum) | C03 · C31 · C38 · C40 · C90 · C91 · C96 | restrained ominous score and abstract low-frequency tension as non-diegetic design (plan C03) | müzikle, F8 | `O02.wav` |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| bütün 95 kesme | kesme | kadraj dışı yanıt J/L; aynı mekânda Y1 kesintisiz | plan: "Görüntüde düz kesmeler toplamı korur. Ses köprüleri, görüntü sürelerini değiştirmeden yapılabilir." |
| C02→C03 · C03→C04 · C30→C31 · C31→C32 · C37→C38 · C38→C39 · C39→C40 · C40→C41 · C89→C90 · C91→C92 · C95→C96 | kesme | Y1 ↔ Y2 1-2 s çapraz | iç ↔ dış mekân değişimi (GECIS §2); plan "ses köprüsü" |

## 7. MÜZİK PLANI

```
OKUMA        İzleyici bu filmi kara deliğin yanındaki bir diplomasi gerilimi olarak okumalı; sonu zafer marşı değil, onur ve rahatlama (plan müzik briefi).
MÜZİKSİZ     00:00–02:00 az müzik, suskunluk şüpheyi büyütür · 12:00 dış bağlantı kapanınca sessizlik (C73) (plan)
VURUŞ/SUSMA  ~02:20 "intent" savunmasında küçük bas nabzı (C15) · 09:40 silah çekilince kısa sert vurgu (C59) · 10:00-11:30 alıcılar çıktıkça sıcak ve yakın,
             yüksek değil (C61-C69) · 12:20 K1 açılınca sıcak küçük ton (C75) · 14:00-16:00 ölçülü tema (plan) — faz 8'de gerçek kesme noktalarıyla
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md (plan: "Bölümler aynı tını ve motifle hazırlanabilir.")
```

### MÜZİK PROMPTU — Flow Music'e yapıştırılır (plan müzik briefi birebir, 18.10.2026)
```text
Create a restrained instrumental score for a sixteen-minute alien political thriller in eight connected movements. The setting is a diplomatic chamber near a supermassive black hole. Begin with near-silence, low pressure-like tones and a tiny unresolved interval. Leave generous intelligible space for six distinct dialogue voices and a cold official relay. Build through suspicion, contradictory recordings, the cost of lost time and a brief threat of violence. When the characters remove their receivers, let the sound become warmer and more immediate rather than louder. Develop a small clear motif for a source voice being heard without alteration. Resolve with dignity and relief, not a triumphant battle march. Sparse bowed textures, subtle glass resonance, low strings and restrained synthesis. Entirely instrumental, original themes, no vocals.
```
