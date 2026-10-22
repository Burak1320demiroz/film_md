DEVAMLILIK F5 · RAIN_THIEF G01 (C01-C08) · tur 1

KORU (kelime kelime karşılaştırıldı, sapma 0):
- G01 `KİMLİK CÜMLELERİ` tablosu FILM.md §3 tablosuyla aynı. Her Görsel promptundaki Kett, Mara, Vorr, Tula, çekirdek ve R06 cümleleri bu tabloyla birebir (8/8).
- ORTAK GÖRÜNÜM 8/8 Görsel'de FILM §3 ile birebir.
- ORTAK HAREKET 8/8 Video'da birebir. C03 ve C05'te "spoken lines" cümlesinin atılması repliksiz çekim olduğu için tutarlı.
- `Reference <No>` anahtarları EKLE satırlarıyla ve FILM §4 Referans sütunuyla 8/8 aynı. Numara-rol eşlemesi çekimler arasında sabit: 1 Kett, 3 Mara, 4 Vorr, 5 Tula, 6 market, 9 core.
- Çekirdek C01, C03, C04, C06'da sağ elde, C05'te sağ el gövdeyi tutuyor. Gemi sol, kule sağ (C03, C06). Ekran yönü sol→sağ (C01, C02 "Kett off-screen right", C03).

## 8 SORU TABLOSU

| Çekim | 1 işaret | 2 kimlik birebir | 3 ortak cümle | 4 açıklığın ardı | 5 akışkan | 6 ekran + kilit | 7 referans rolü | 8 ses · zıt istek |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| C01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C02 | — | ❌ (B7) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C03 | ✅ | ❌ (B14) | ✅ | ❌ (B15) | ✅ | ✅ | ✅ | ❌ (B3) |
| C04 | ✅ | ✅ | ✅ | ✅ | ❌ (B16) | ❌ (B17) | ✅ | ✅ |
| C05 | — | ❌ (B5, B18) | ❌ (B11) | ✅ | ✅ | ✅ | ❌ (B4) | ✅ |
| C06 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C07 | — | ✅ | ❌ (B11) | ✅ | ✅ | ✅ | ✅ | ✅ |
| C08 | — | ✅ | ❌ (B11) | ✅ | ✅ | ✅ | ✅ | ✅ |

C03'te işaret ✅ çünkü Kett küçük figür. Toka "giysi" cümlesinde geçiyor, "center front … only marking" cümlesi yok. Bu yüzden C03'te toka birebir ama işaret cümlesi eksik. Kadrajda okunabilir olmayacağından bulgu yazmadım.

Not: Soru 8 için C01, C02, C04, C06, C07, C08'deki `Voice:` satırları ses tarifidir. Flow "Return silent videos AÇIK" iken bunlar etkisizdir. ORTAK HAREKET onları "performance cues" olarak çerçevelediği için ❌ saymadım. Zıt istek yalnız C03'te var.

Çekim sınırı: ❌ hücresi olmayan satır yok. Sapmaların büyük kısmı sahip planı metninden geliyor (C05 ve C06 Görsel, C03 ses cümlesi, C08 "established places"). Düzeltmelerde plan lehine gerekçeli RED mümkündür; karar Fable/sahibin.

---

### B1 · CİDDİ · C05: Görselde damla zaten bırakılmış, Video "bırak" diyor
YER       C05 Görsel (ilk paragraf) ↔ C05 Video 0-3 s
KANIT     Görsel: "A single suspended drop hangs above the pale alien flower." Ek: "Below the drop, the one pale closed alien flower sits in a cracked ceramic pot". Video: "0-3 s: Release exactly one small drop from the side test valve onto the flower."
ETKİ      Başlangıç karesinde damla valften çoktan ayrılmış. Model ya bırakma anını atlar ya ikinci bir damla üretir ("Only one drop" bozulur); C05'in tek bilgisi (tek damla, tek yaprak) bulanır.
DOĞDUĞU   kare (metin)
KURAL     devamlilik.md:59-62 görsel ↔ video başlangıç durumu [TERCİH]; plan C05 Görsel/Video cümleleri aynı çelişkiyi taşıyor
ARIZA     T14 (aksiyonun hedefi/izi) / yeni (başlangıç durumu)
DÜZELTME  Görsel: `A single suspended drop hangs above the pale alien flower.` → `A single drop forms at the tip of the side test valve above the pale alien flower.` (Video 0-3 s aynen kalır). Plan cümlesi olduğundan sahibe bildirilir.

### B2 · CİDDİ · C06: Görselde karar bakışı bitmiş, Video önce başka yöne baktırıyor
YER       C06 Görsel ↔ C06 Video 3-10 s
KANIT     Görsel: "Kett's gaze turns toward the tower." Video: "3-10 s: Kett glances once toward the left-hand skiff, answers the short reply, then turns shoulders toward the right-hand tower."
ETKİ      Görsel, 3-10 s vuruşunun SONUCUNU (kuleye bakış) gösteriyor. Model skiff bakışını atlar ya da bakışı geri sarar. Kararın "sol→sağ" okunuşu (FILM §1 KARAR) zayıflar.
DOĞDUĞU   kare / hareket
KURAL     devamlilik.md:59-62 [TERCİH]; ORTAK HAREKET "One principal physical action … at most" (FILM.md:152)
ARIZA     yeni (görsel ↔ video başlangıç durumu); T11 yön
DÜZELTME  Görsel: `Kett's gaze turns toward the tower.` → `Kett looks straight ahead.` Video'da bakış-cevap-dönüş tek 7 s vuruşta üç eylem ve bir kamera itişi içeriyor; istenirse `3-6 s: Kett glances once toward the left-hand skiff and answers the short reply. 6-10 s: He turns shoulders toward the right-hand tower; …` (plan cümlesi bölünür, kelime eklenmez).

### B3 · CİDDİ · C03: sessiz-dönüş filminde Video'ya "audio" istemi
YER       C03 Video 5-10 s
KANIT     "Atmospheric crowd audio only; no dialogue, no subtitles." Flow iş emri: "Return silent videos AÇIK (SK2: model sesi kullanılmaz)". FILM §6: "model sesi kullanılmaz".
ETKİ      Aynı üretimde hem sessiz dönüş hem kalabalık sesi isteniyor (zıt istek). Model kalabalığa konuşma/ağız animasyonu da ekleyebilir. Ses zaten §6 S3 ve Y1 yatağında kurguda kuruluyor.
DOĞDUĞU   metin (sahip planından gelen cümle)
KURAL     goruntu-yonetmeni.md:118 (Q8) [TERCİH]; FILM.md:294-295 [SÖZLEŞME]
ARIZA     T13 / yeni (zıt istek)
DÜZELTME  Sil: `Atmospheric crowd audio only; no dialogue, no subtitles. ` (plan cümlesi; sahip/Fable onayı gerekir). "no dialogue" olumlu karşılığı gerekmiyor; ORTAK HAREKET zaten "No built-in captions, subtitles, music".

### B4 · CİDDİ · C05: Reference 5 hiçbir şey vermiyor, kadraja olmayan kişiyi çağırıyor, ref 6 yok
YER       C05 Görsel başı + EKLE satırı
KANIT     "Reference 5 (Tula): the pale flower belongs to Tula's flower stall, and Tula herself, with her plain small copper cup, stays outside this macro frame." EKLE: "ref/1.KETT_v1.png · ref/5.TULA_v1.png · ref/9.CEKIRDEK_v1.png". Ek paragraf: "a small flower stall, with a dry coin-operated water spout" (tezgâh/çiçek ref 6'da, ref 5 sayfasında çiçek yok: G01 REF 5 promptu "Holds one plain small copper cup in both hands").
ETKİ      Tula'nın tam boy görseli makro üretimine yüklenip Tula ve fincanını anıyor → ikinci fincan ya da fazla kişi riski (T15; FILM "tek fincan"). Çiçek ve tezgâh için gereken ref 6 yok.
DOĞDUĞU   metin / referans seçimi (plan R05 listesi)
KURAL     goruntu-yonetmeni.md:117 (Q7) [TERCİH]; DERS Y2
ARIZA     T15 / T04
DÜZELTME  `Reference 5 (Tula): … stays outside this macro frame.` → `Reference 6 (market): take the small flower stall and its one pale closed alien flower from it.`; EKLE'de `ref/5.TULA_v1.png` → `ref/6.PAZAR_v1.png`; FILM §4 C05 Referans ve iş emri satır 17 aynı şekilde. Plan R05 diyor; RED edilirse en az "Tula herself … cup" kısmı silinir.

### B5 · CİDDİ · C05: "üç parmak" ile "başparmak" sayısı belirsiz
YER       C05 Görsel (ilk paragraf ve ek paragraf)
KANIT     "left thumb resting on its tiny side test valve" ↔ "Kett has cobalt-blue skin and three fingers on each hand."
ETKİ      El makro kadrajın tek öznesi. "Üç parmak" + ayrı "thumb" 3 mü 4 mü (başparmak dahil mi) belirsiz; kare kapısındaki "parmak sayısı" ölçütü doğrulanamaz, fazla/eksik parmak ve kaynaşma riski artar (T01).
DOĞDUĞU   metin
KURAL     FILM.md:162-163 sayılabilir ölçü [TERCİH]; BILINEN_TUZAKLAR.md:47 #1 [TERCİH]
ARIZA     T01
DÜZELTME  `Kett has cobalt-blue skin and three fingers on each hand.` → `Kett has cobalt-blue skin and three fingers on each hand, one of them the thumb.` (FILM §3 tablo satırı "Kett · eller (makro)" de aynı değişir.)

### B6 · KÜÇÜK · C05: eller var, kolun kadraja girişi yazılı değil
YER       C05 Görsel (ek paragraf)
KANIT     "Extreme close-up of Kett's cobalt-blue hands holding the same transparent storm core" ve Video 7-10 s "Kett's face stays out of frame" (kolun nereden girdiğine dair cümle yok)
ETKİ      Gövdesiz eller: tutan bağlantısı belirsiz, "havada asılı eldiven" tipi hata (THE_STOLEN_SKY S82).
DOĞDUĞU   metin
KURAL     devamlilik.md:63-67 [TERCİH]
ARIZA     T01
DÜZELTME  Ek paragrafa: `Kett's forearms enter the frame from the lower edge.`

### B7 · CİDDİ · C02: "iki bulanık uzaylı" ile "sekiz siluet" ve "kalabalık / açılmış koridor" çelişiyor
YER       C02 Görsel (iki paragraf)
KANIT     Kamera: "with two blurred aliens of different species in the background". Ek: "Eight different nonhuman crowd silhouettes stand in layered depth, the nearest two parting as blurred shapes behind Vorr." Plan Görsel: "planted in a crowded dry copper market aisle" ↔ ek "Vorr stands in the open corridor that the crowd has cleared".
ETKİ      Göğüs-üstü alçak açıda sekiz silüet sığmaz; model 2 yerine kalabalık ya da tersine boş koridor üretir. Video "without changing species or number" için sayı belirsiz (T15).
DOĞDUĞU   metin
KURAL     devamlilik.md:52 sayı [TERCİH]
ARIZA     T15
DÜZELTME  `Eight different nonhuman crowd silhouettes stand in layered depth, the nearest two parting as blurred shapes behind Vorr.` → `Two blurred nonhuman silhouettes of different species part behind Vorr.`

### B8 · CİDDİ · C04: Kett'in ekran tarafı ve yönü hiçbir yerde yok
YER       C04 Görsel (ilk paragraf ve ek) + Video
KANIT     "Beside Tula, Kett pauses with the weather core still in the right hand." (taraf ve bakış yönü yazılı değil; C01/C03 "left to right", C02 "Kett off-screen right")
ETKİ      Kett sağa koşarken (C01-C03) C04'te sola bakan ya da sağdan gelen biçimde üretilirse 180° yön atlar. FILM §6 GEÇİŞ C03→C04: "Kett sağa ilerler → Tula'nın yanında yavaşlar".
DOĞDUĞU   metin
KURAL     FILM.md:162-163 / ARIZA T11 (taraf ve yön) [TERCİH]
ARIZA     T11
DÜZELTME  Ek paragrafa: `Kett stands at Tula's left, facing screen right, and Tula faces him.` (taraf kararı Fable'ın; amaç C01-C03 yönünü sürdürmek).

### B9 · CİDDİ · C07/C08: pirinç kolun tarafı ve işaret eden kol yazılı değil; C08 "established places" boş atıf
YER       C07 Görsel; C08 Görsel (ilk paragraf); C14 (G02) bu kolu "previously shown" diye yeniden kullanıyor
KANIT     C07: "A brass manual awning lever is clearly visible beside Mara's hip." / "Mara points upward along a thick blue service pipe". C08: "Brass awning lever and folded blue canopy remain in their established places." C14 Görsel (G02): "One hand rests on the same brass awning lever previously shown."
ETKİ      Kol C07'de kurulup C14'te tepe nokta olacak; tarafı/şekli iki yerde bağlanmıyor. C08'deki atıf (model önceki çekimi hatırlamaz) hiçbir şey kilitlemiyor. İşaret eden elin hangisi olduğu belirsiz: C14'te "bir el kolda" hangi el.
DOĞDUĞU   metin
KURAL     FILM.md:162-163 "Nesne: biçim + ölçü + taraf" [TERCİH]; devamlilik.md:49,51 (taraf) [TERCİH]
ARIZA     T09 / T11
DÜZELTME  C07: `beside Mara's hip` → `beside Mara's left hip` ve `Mara points upward` → `Mara points upward with her right arm`. C08: `remain in their established places` → `stay beside Mara's left hip and above the stall`. (Sol/sağ seçimi Fable'ın; C14 aynı seçimi kullanır. Ölçü planda yok, sahibe sorulur.)

### B10 · CİDDİ · M1 dış çekimlerde ana ışık yönü hiç yazılı değil
YER       C01-C08 Görsel promptları; FILM §3 ORTAK GÖRÜNÜM ve SAHNE DÜZENİ
KANIT     Yalnız "warm late-afternoon copper and mustard palette" (ORTAK GÖRÜNÜM) ve "warm late-afternoon sky" (R06 cümlesi). Hiçbir prompt güneş/ışık yönü ya da gölge tarafı yazmıyor. Video: "Preserve … light direction" (korunacak bir yön yok). Video'larda ORTAK GÖRÜNÜM hiç yok (0/8).
ETKİ      Sekiz bağımsız kare güneşi rastgele taraftan alır; C01→C02→C03 açılış kesmeleri arasında gölge tarafı zıplar (T18).
DOĞDUĞU   metin
KURAL     devamlilik.md:50 [TERCİH]; GECIS_VE_SES_SUREKLILIGI §1 (aynı mekân kesmeleri)
ARIZA     T18
DÜZELTME  FILM §3 SAHNE DÜZENİ M1'e tek cümle ve M1 Görsel promptlarına aynen: `A low warm sun shines from the upper left, so soft shadows fall toward screen right.` (yön seçimi Fable'ın; plan dışı yeni cümle olduğundan sahibe bildirilir.)

### B11 · KÜÇÜK · ORTAK GÖRÜNÜM yakın ve makro kadrajda gezegen ve ışık taşıyor (Y6)
YER       C05, C07, C08 Görsel (ORTAK GÖRÜNÜM)
KANIT     "warm late-afternoon copper and mustard palette … one pale ringed planet" — C05 "Extreme close-up", C07 "Medium close portrait", C08 "close foreground composition". FILM.md:165-166: "Işık, su, gezegen, ses mekân ya da çekim cümlesine gider (DERS Y6)."
ETKİ      Makroda gezegen ya da gök parçası kadraja basılabilir; FILM'in kendi kuralı ORTAK GÖRÜNÜM'de çiğneniyor.
DOĞDUĞU   metin (plan §6 ORTAK GÖRÜNÜM)
KURAL     FILM.md:165-166 DERS Y6 [TERCİH]; plan §6 birebir
ARIZA     T18
DÜZELTME  G01 başındaki öneri (FILM'e Fable karar verir): `one pale ringed planet, ` sil ve `warm late-afternoon copper …` → `warm copper …`. Plan lehine kalırsa yalnız C05, C07, C08'den `one pale ringed planet, ` silinir.

### B12 · KÜÇÜK · Video son vuruşları kısıt listesine dönüyor, C01'de replik vuruş sınırını aşıyor
YER       C01 Video 5-10 s; C02 8-10 s; C04 8-10 s; C05 7-10 s; C07 7-10 s; FILM §5 R01
KANIT     C01: "5-10 s: Stay in this one continuous shot. Kett keeps running left to right and the tracking move carries on. The poncho stays fastened, the core stays in the right hand, and the air stays dry." C07: "7-10 s: End with the brass awning lever still visible. The lever does not move yet and the awning stays folded." §5 R01: saniye 2.2, süre 3.5 (2,2-5,7 s) ↔ vuruş "0-5 s: … Kett says the single assigned line". G01 başlık notu: "Replik R01 1,0-4,5 s".
ETKİ      5/8 çekimde son 2-5 s'de yeni eylem yok, hareket donuk kalabilir (H10). C01 hook çekimi. R01 5 s sınırını 0,7 s aşıyor ve G01 notu §5'le uyuşmuyor.
DOĞDUĞU   metin
KURAL     devamlilik.md:43-44 [TERCİH]
ARIZA     H10
DÜZELTME  C01: `5-10 s: Stay in this one continuous shot. Kett keeps running left to right and the tracking move carries on.` → `5-10 s: Kett keeps running left to right and the tracking move slowly eases closer.` (plan cümlesi sahibe sorulur). Not'taki "1,0-4,5 s" → "2,2-5,7 s" (§5 ile aynı). Vuruş iskeleti yine de çeşitli (3 farklı iskelet, en çok 2/8 aynı); sorun iskelet değil içerik.

### B13 · KÜÇÜK · C02: kadrajda olmayan ayak için fiil
YER       C02 Video 0-5 s
KANIT     Görsel: "Chest-up low-angle portrait." Video: "A short steady push toward Vorr as he plants one heavy foot". Görsel zaten "planted".
ETKİ      Göğüs üstü kadrajda ayak görünmez; model kamerayı indirir ya da ayağı kadraja sokar, kadraj kayar.
DOĞDUĞU   metin
KURAL     devamlilik.md:66 [TERCİH]
ARIZA     T07
DÜZELTME  `as he plants one heavy foot and shouts` → `as he shouts`.

### B14 · KÜÇÜK · C03: "escape skiff" — özne yeniden adlandırılıyor
YER       C03 Görsel ek paragraf son cümle
KANIT     "the escape skiff is at the left" ↔ R06: "one small orange commuter skiff"
ETKİ      Aynı nesne iki adla; model ikinci bir gemi (kaçış) ekleyebilir (C06'da tek turuncu gemi).
DOĞDUĞU   metin
KURAL     FILM.md:162-163 "özne yeniden adlandırılmaz" [TERCİH]
ARIZA     T09
DÜZELTME  `the escape skiff is at the left` → `the orange commuter skiff is at the left`.

### B15 · KÜÇÜK · C03: seraların yeri yazılı değil
YER       C03 Görsel ek paragraf ve Video 0-5 s
KANIT     "Sealed luxury greenhouse terraces receive rain inside" (konum yok; iskele "far left", kule "upper right"); Video: "crane upward … to reveal the reservoir and private greenhouse rainfall"
ETKİ      Çekimin tek bilgisi (kuru kamu, ıslak sera) için seraların kadrajda nerede olacağı model keyfine kalır; G02 C10 camın ardındaki bahçe bu konumla bağlanamaz.
DOĞDUĞU   metin
KURAL     goruntu-yonetmeni.md:114 (Q4) [TERCİH]
ARIZA     T11
DÜZELTME  Ek paragrafa: `The sealed greenhouse terraces sit at the upper center, between the dock and the tower.` (konum Fable'ın).

### B16 · KÜÇÜK · C04: olumsuz su cümlesi su çağırıyor
YER       C04 Video 8-10 s
KANIT     "The spout releases no water."
ETKİ      "water" kelimesi dolu bir musluk akışı çağırabilir (Tula'nın fincanı tam bu çekimde boş kalmalı; C23'te dolacak).
DOĞDUĞU   metin
KURAL     goruntu-yonetmeni.md:115 (Q5: hedef hâl olumlu yazılır) [TERCİH]; BILINEN_TUZAKLAR.md:19 [TERCİH]
ARIZA     T03
DÜZELTME  `The spout releases no water.` → `The spout stays dry and closed.`

### B17 · KÜÇÜK · C04: "No written prices" fiyat yazısı çağırıyor
YER       C04 Görsel (ilk paragraf sonu)
KANIT     "No written prices in the image." (kadrajda sikkeyle çalışan sayaç: "dry coin-operated copper spout")
ETKİ      Kelimenin kendisi tabela/rakam çağırır (BILINEN_TUZAKLAR §C). Yazı kilidi ORTAK GÖRÜNÜM'de zaten var.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:62-78 §C [TERCİH]; goruntu-yonetmeni.md:116 (Q6) [TERCİH]
ARIZA     T06
DÜZELTME  `No written prices in the image.` → `The spout and the stall surfaces are plain and unmarked.`

### B18 · KÜÇÜK · C05: çekirdeğe üç ayrı ad ve aşırı dolu makro kadraj
YER       C05 Görsel (iki paragraf)
KANIT     "the same transparent storm core" / "the dark base of the capsule" / "A single eighteen-centimeter transparent weather-control core". Ayrıca "Three silver ribs and the dark base of the capsule are clearly visible" ↔ Kamera: "filling the frame with the core's side test valve, the single drop and a part of the flower pot".
ETKİ      Aynı nesne üç adla (storm core, capsule, weather-control core); valfe dolan makro kare, bütün kaburga ve tabanı ile çiçek saksısını birlikte sığdıramaz, model ya kaburgayı ya valfi bırakır.
DOĞDUĞU   metin
KURAL     FILM.md:162-163 [TERCİH]; devamlilik.md:54 çelişki [TERCİH]
ARIZA     T09
DÜZELTME  `the same transparent storm core` → `the same transparent weather-control core`; `the dark base of the capsule` → `the dark base of the core`; `Three silver ribs and the dark base … are clearly visible.` → `Three silver ribs are visible along the core's side.`

### B19 · KÜÇÜK · C06/C07/C08: kadrajda olmayan "flower stall" cümlede geçiyor
YER       C06, C07, C08 Görsel ek paragraf
KANIT     "Adjacent to the flower stall, a food stall has a folded reinforced blue delivery awning, tension cables and a brass lever." (C07, "No Kett in frame" ve yakın portre; C08 Vorr yakın planı)
ETKİ      Çiçek tezgâhı kadraj dışı ya da odak dışı; model ikinci bir çiçek/Tula tezgâhı ekleyebilir (C07/C08'de "tek saksı" kuralı).
DOĞDUĞU   metin
KURAL     devamlilik.md:52 sayı [TERCİH]
ARIZA     T09
DÜZELTME  C07 ve C08'de: `Adjacent to the flower stall, a food stall` → `A food stall`. C06'da kalabilir (iki tezgâh orada kadrajda).

### B20 · KÜÇÜK · C08: "canopy" — awning/canopy adı çatılardaki ayrı nesneyle çakışıyor
YER       C08 Görsel (iki yer)
KANIT     "Reference 6 (market): take Mara's food stall with its brass lever and folded blue canopy from it." ve "Brass awning lever and folded blue canopy remain …". C06/C07'de aynı nesne "folded … blue (delivery) awning". FILM §3 satır 7 "canopy" sözü pas turuncusu tente ve mavi yük tentesi için kullanılıyor.
ETKİ      Aynı nesne iki ad; FILM §3 "C13 pas turuncusu ≠ C14-C15 mavi yük tentesi" ayrımı kelime düzeyinde bulanıyor.
DOĞDUĞU   metin
KURAL     FILM.md:162-163 [TERCİH]
ARIZA     T09
DÜZELTME  C08: her iki `folded blue canopy` → `folded blue awning`.

### B21 · KÜÇÜK · C08: Vorr'un son vuruştaki bakış hedefi kadrajda yok
YER       C08 Video 7-10 s
KANIT     "7-10 s: Vorr then directs his gaze up toward the blue service route." (Görselde mavi boru yok, Reference 6'dan yalnız "food stall with its brass lever and folded blue canopy" isteniyor; bakış yönü yazılı değil.)
ETKİ      Vorr neye ve hangi tarafa baktığı model keyfinde. FILM §6 GEÇİŞ C08→C09 "Vorr'un yukarı bakışı → Kett tırmanışta" bağı kopar.
DOĞDUĞU   metin
KURAL     devamlilik.md:51,75 (yön, grup geçişi) [TERCİH]
ARIZA     T11 / T14
DÜZELTME  `up toward the blue service route` → `up and to screen right toward the blue service route` (C06'da borular sağ yukarıdaki kuleye gidiyor) ve Görsel ek paragrafa `A thick blue service pipe rises behind the stall.`

### B22 · KÜÇÜK · Referans promptları: referans kodu gövdede, tek görünüş, "may rest"
YER       G01 REFERANS PROMPTLARI: 2.KETT_TULUM; 9.CEKIRDEK; 1.KETT
KANIT     2: "Edit the supplied R01 Kett reference into the exact same adult alien …". 9: "One tiny water drop may rest at the closed side valve." 1: "Three-quarter front standing pose" (tek görünüş); C01 Kett profilde koşuyor, C06'da omuzlar kuleye dönüyor.
ETKİ      "R01" referans kodu gövdeye basılabilir (BILINEN_TUZAKLAR §C ⛔ "referans kodu (R3 · RK1)"). "may rest" valf-damla durumunu belirsiz bırakır (C05 kapalı valf + tek damla). Yan/arka panel yok → C01 ve C06'da profil/sırt kimliği boşta (sahip planı tek görünüş; bildirim).
DOĞDUĞU   metin / referans
KURAL     BILINEN_TUZAKLAR.md:73 [TERCİH]; devamlilik.md:40-42 [TERCİH]
ARIZA     T04 / T16
DÜZELTME  2: `the supplied R01 Kett reference` → `the supplied Kett reference`. 9: `One tiny water drop may rest at the closed side valve.` → `The closed side test valve is dry.` (damla C05'te eklenir). Panel eksikliği için sahip kararı gerekir.

---
ÖZET     ÖLÜMCÜL 0 · CİDDİ 9 (B1 B2 B3 B4 B5 B7 B8 B9 B10) · KÜÇÜK 13 (B6 B11 B12 B13 B14 B15 B16 B17 B18 B19 B20 B21 B22)
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok). CİDDİ'lerin yazar tarafından düzeltilmesi ya da gerekçeyle reddedilmesi beklenir. B1, B2, B3, B4 plan metninden geliyor; RED gerekçesi "plan lehine" olabilir ama kararı sahip ve Fable verir.
GİRDİ    uretim_hatti/ELESTIRI_PROTOKOLU.md, uretim_hatti/BILINEN_TUZAKLAR.md, uretim_hatti/ARIZA_LISTESI.md (H/T kodları), .claude/agents/devamlilik.md, goruntu-yonetmeni.md (8 soru, satır 108-118), yatay_4_dk_filmler/RAIN_THIEF/FILM.md (§1-§7 tamamı), PROMPTLAR/G01.md (tamamı: REFERANS PROMPTLARI, KİMLİK CÜMLELERİ, C01-C08 Görsel ve Video, FLOW İŞ EMRİ), RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md (satır 224-358, C01-C08 plan istemleri), PROMPTLAR/G02.md satır 138-159 (yalnız C14 kolu için). G01 sonundaki yazarın "8 SORU" tablosunu gördüm ama değerlendirmede dayanak yapmadım.
YAPILMADI  Kare denetimi (kare/ref dosyası verilmedi). ILK_30_SANIYE_KILAVUZU §6 açılış karesi kontrolü (kare yok). Karakter uzunluk sayımı (yazarın beyanı doğrulanmadı). G02/G03 prompt denetimi (kapsam dışı; B9 ve B15 yalnız oradan gelen bağlara işaret ediyor). `film_dogrula.py` çalıştırılmadı.

Dosya: /Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/RAIN_THIEF/PROMPTLAR/G01.md
