**OKUNMAYAN / EKSİK KISIMLAR**
- `FILM.md` satır 508-625 (§6 GEÇİŞ tablosu, §7 MÜZİK PLANI) okunmadı. Görev yalnız §3 §4 §5'i istiyordu.
- Sahip planı `THE_FURNACE_GATE_16MIN_96_CLIPS.md`, `NOTLAR.md`, `SAHNELEME.md`, `timeline.json` ve `ODA/*` açılmadı. Öteki eleştirmenlerin çıktıları bağımsızlık için açılmadı.
- `FLOW_GERCEKLERI.md` yalnız grep satırlarıyla görüldü, tamamı okunmadı.
- `SMOKE_TEST.md` okunmadı.
- Prompt uzunluğu için `^.{3300,}$` taraması hiç satır bulmadı. Bu sonuca güvenmiyorum, bu yüzden 4.300 sınırı için bulgu yazmadım.

G01 (487 satır), G02, G03, G04 ve `FILM.md` 1-507 baştan sona okundu. `body` ve `EMP` listeleri okurken tutuldu, dosya genelinde ayrı grep koşmadım. Listeler eksik olabilir.

---

### B1 · CİDDİ · Gri diskin büyük harfli "EMP" kısaltması referans sayfalarına ve C31 karesine yazılmış
KANIT    G01 `2.RHEA`: "one small matte-grey fictional EMP puck and a coiled navy safety tether". G01 `15.ARACLAR`: "one small matte-grey fictional EMP puck with an amber indicator". G03 C31 Görsel: "a small matte grey EMP puck is attached to it at shoulder height". G02 başlığı bunu yasaklıyor: "gri disk 'EMP' diye anılmaz (büyük harfli kısaltma kadraja basılır". BILINEN §C: "`EVA` (kısaltma, 10 promptta) | sırta basıldı".
NEDEN    Diskin tasarımı sayfa 15 ve sayfa 2'den geliyor. Üstüne "EMP" yazılırsa C15, C31 ve diski gösteren bütün kareler aynı yazıyı taşır.
ARIZA    T06 · BILINEN §C
ÖNERİ    Sayfa 2, sayfa 15 ve C31 Görsel'de "EMP puck" yerine "small matte-grey fictional disc" yaz. Referanslar henüz üretilmedi, bu yüzden panel adı `emp puck panel` de FILM §3'te `grey disc panel` olur. C15 ve C31'deki "using the emp puck panel" ona göre değişir.

### B2 · CİDDİ · C03 açılışı: şeffaf vizörde yüz, 5,0 s dudak senkronu ve vizörde kayan yansıma bir arada
KANIT    C03 Görsel: "a soft band of reflected amber light, the glow of the foundry gate beyond the canopy, lies across his closed clear visor". C03 Video: "the band of reflected amber light drifts gently across his clear visor" ve "the push-in ends a little closer on his face". FILM §5 R03: 5,0 s, ağız kadrajda. ILK_30 §6: "şeffaf vizörde yüz yakın planı açılışta yüksek risklidir". ARIZA_LISTESI/PROMPT_HATA_ATLASI A11 kanıtı: "Vizöre ışık deseni … SIGNAL_KEEPERS K11 🔴 1:47 HUD".
NEDEN    Üç risk 20-30. saniyede üst üste biniyor: yüz bozulması, yansımanın yazı ya da HUD'a dönmesi, ağız senkronu. Bu çekim açılışın kapak anı parçası.
ARIZA    ILK_30 §6 · T06 · T16
ÖNERİ    Yansıma yalnız karede kurulur, videoda kaymaz. Son itiş aynı ölçekte biter, "closer on his face" çıkar. Kare kapısı yüzü kabul etmezse düşük riskli karşılık: Leon arkadan ya da omuz üstü ¾, ağız görünmez, replik aynı kalır.
Açılış sonucu: C01 (geniş, yavaş yanal kayma, insan yok, el teması yok) ve C02 (geniş iki kişi, arkadan, yavaş itiş) ILK_30 §6'nın düşük riskli seçimleri. Başka açılış bulgusu yok (C01 için B11, C02 için B8).

### B3 · CİDDİ · Temasın değiştiği an kare içinde isteniyor, beş çekimde yedek yok
KANIT    C26 Video: "she lifts the single core straight up out of the cradle in one slow, effortful lift, both gloves keeping the same grips as the casing clears its supports". C34 Video: "pulls it down a few degrees in one small, resisted movement until it jams against the lock", sonra 4-8 s "the forearm under the sleeve straining and the cuff creasing at the wrist". C31: "her glove presses the puck's broad activation pad in one firm press". C04: "her left thumb presses the one broad toggle over to its far end stop". C33: "presses the flat pad once with her glove".
GOSTERIM_COZUMLERI §1: "Kaldırma (yuvadan çıkma) kesmede". İlke 5: "Sürekli temas kısa; temas sırasında hareket küçük". İlke 2: kurulu temas "büyük hareketli 10 s'lik çekimde bozuldu" (STOLEN_SKY S03).
YEDEK notu C14, C15, C23, C42 ve C45'te var. C04, C26, C31, C33 ve C34'te yok.
C04'te ayrıca üç temas üst üste: bilek birimi ↔ yuva, sol eldiven ↔ sağ kol üstündeki anahtar, başparmak bastırması. Hepsi beyaz eldiven ve fildişi birim.
NEDEN    Temas cümlesi ve ilk karede kurulu temas eli kaynaşmaktan korumuyor (A03). C26 ve C34'te temas on saniye boyunca değişiyor.
ARIZA    T01 · T02 · A03
ÖNERİ    C26: kaldırma kareden çıkar. Klip, eldivenler çekirdekte, omuzlar yükü alırken ve nefesle biter. Kaldırmayı C26→C27 kesmesi atlar, C28'in boş beşiği sonucu taşır. C34: kol karede zaten birkaç derece çekilmiş ve kilide dayalı başlar. Videoda yalnız kol gerilmesi, kıvrılan manşet ve kamera kayması kalır. C04, C31 ve C33: "bastırma/çevirme vuruşu çıkar, eldiven üstte kalır" yedeği G02'deki biçimle eklenir.

### B4 · CİDDİ · Boş kasa kareleri çekirdek içeren sayfa paneline bağlı (kopya çekirdek, kopya askı)
KANIT    G01 `10.CEKIRDEK`: "one core resting in an open cradle with a single broad hinged retaining latch, and an empty matching rigid carry harness lying beside the cradle". C27, C28, C29, C30 ve C32 hep `vault wide panel`'i kullanıyor. C28 Görsel: "The rigid storage cradles … stand open and empty". G03 C28 notu kendisi kabul ediyor: "Ref 10 sayfasında çekirdek beşikte görünse bile … beşikte çekirdek çıkarsa kare yeniden alınır". Sayfa 10'un beş paneli arasında boş kasa paneli yok.
NEDEN    Çekirdek C26'da beşikten çıkıp Rhea'nın askısına giriyor. Referans her seferinde beşiğe çekirdek, yanına da ikinci bir askı koyacak (T09).
ARIZA    T09
ÖNERİ    Sayfa 10'a `vault empty panel` ekle: iki beşik açık ve boş, mandallar dışarıda, askı yok. Sayfa henüz üretilmedi, maliyet sıfır. C27-C32 bu paneli alır. C24-C26 `vault wide panel` ile kalır.

### B5 · CİDDİ · Kokpit yönü: ön kameradan pilot "solda" ve kanopi oturanın "arkasında"
KANIT    FILM §3 ve G01 `4.KOKPIT`: "an eye-level wide view from behind the two seats looking forward; the navy pilot seat stands at frame-left". G04 başlığı: "kamera koltuklara bakar (yüzler okunur)" ve "pilot koltuğu kare solunda, mühendis koltuğu kare sağında". C41 Görsel: "Behind her at frame-right the broad canopy … shows the long ivory hull of the colony ark". C46 Görsel: "Behind them the broad canopy". G03 C36 Görsel arkadan: "from behind and slightly above the two seats". G04 C36→C37 notu bunu aynı düzende istiyor: "bu grupla aynı ekran düzeninde olmalı".
NEDEN    Koltuklar kanopiye bakar. Yüzleri gören kameranın arkasında kanopi kalır, kanopiyi arkalarında göstermek fiziksel olarak çelişir. Arkadan çekimde (C02, C36) pilot solda, önden çekimde (C37-C47) sağda olmalı. İki çekim tipi arasında koltuk ya da kanopi yönü değişir.
ARIZA    T11 · T04
ÖNERİ    Tek kural yaz: yüz görünen kokpit çekimlerinde pilot kare sağında, Leon'un bakışı kare soluna gider. Önden çekimlerde kanopi arka plan olmaz. C41 ve C46 gibi kanopi gereken çekimler arka ¾ (C36 gibi) kurulur. G01 C03 ve C04 de aynı kuralla düzeltilir.

### B6 · CİDDİ · C12'de tug yok, oysa sancak kıç portunda kenetli olmalı
KANIT    C12 Görsel: "from the ark's starboard rear quarter, level with the stern … The frame holds only the ark, the foundry structure and the planet." Referanslar yalnız 5 ve 6. FILM §3: "tug ark'ın kıç SANCAK portuna bir kez yanaşır, C80'e kadar orada". G04 C44 Görsel aynı yönde tug'ı koyuyor: "1 small salvage tug is docked at the ark's starboard stern port". G03 C35 notu kararı Fable'a bırakıyor.
NEDEN    C06'da kenetlenen tug C12'de kayboluyor, C44'te geri geliyor. Sayfa 6'nın `stern panel`i boş portu gösteriyor.
ARIZA    T09
ÖNERİ    C12'ye `3.KESTREL` (bow collar locked panel) ekle. "The frame holds only the ark, the foundry structure and the planet" yerine C44'teki tug cümlesini ve "the two ships" yaz. FILM §3 sayfa 3'ün "kullanan çekimler"ine C12 ve C44 eklenir.

### B7 · CİDDİ · Ses kimliği 51 replikten 38'inde ağız kadrajda, kurgu yedeği o satırlarda senkronu bozar
KANIT    BILINEN §B sıra 11: "replik tek kaynaktan, modelin ürettiği ses kullanılmaz". FILM §5: "kurgu kaydı yedek". G01 FLOW notu: "model aynı sesi iki klipte tutamazsa … yedek yöntemi (kurguda eklenen kayıt) uygulanır". R01-R51'de telsiz ya da VO yalnız 13 satır (R01, R05, R08, R12, R16, R18, R27, R28, R30, R34, R35, R44, R47). Kalan 38'i ağız kadrajda. FILM §5 ağız kadrajdayı "son çare" diye anıyor.
NEDEN    İki sesin 96 klipte aynı kalması model sesiyle garanti değil. Yedek kayıt telsiz ve VO satırlarında sorunsuz. Ağız kadrajdaki satırda ses değişirse ya klip yeniden üretilir ya da kayıt dudakla kayar.
ARIZA    T16 (ses kimliği) · BILINEN §B 11
ÖNERİ    SMOKE P18 ölçütünü şöyle yaz: Leon için C03 · C07 · C11, Rhea için C02 · C08 · C13 karşılaştırılır. Tutmazsa yüzü okunması şart olmayan satırlar (B8'deki geniş ve arkadan çekimler) telsiz ya da kask içi kaynağa çevrilir, yedek kayıt oraya yerleşir. Bu karar §4 Risk sütununa şimdiden yazılır.

### B8 · KÜÇÜK · Yüzü okunmayan geniş ve arkadan çekimlerde dudak koreografisi isteniyor
KANIT    C13 Görsel: "the camera about 7 m from the junction". C24: "about 5 m from the cradle", iki konuşan. C02: "from behind and slightly above … a little right of centre" ile "her helmet is seen in right profile with the clear visor and the scar visible" bir arada. C36 arkadan, iki konuşan. G04 C48 notu: "ağız senkronu zayıf çıkarsa çekim orta-geniş yapılır".
NEDEN    Arkadan çekimde yüz profile dönmeden ağız görünmez. Model ya yüzü büyütür ya konuşmayanın ağzını oynatır.
ARIZA    yeni (dudak senkronu)
ÖNERİ    C13, C17, C19, C24, C33 ve C36'da "ağız kadrajda" etiketi, prompttaki "lips move only for her own line" ifadesiyle birlikte kaldırılır. Konuşan telsiz ya da kask içi yazılır (B7). C02'de ya arka ¾ kalır ve dudak cümlesi çıkar ya da kamera sağ-yandan alınır.

### B9 · KÜÇÜK · Vizörde hareket eden ya da solan ışık yansıması dört çekimde daha var
KANIT    C08: "the dim green pod lights glow steadily across her visor". C27: "the red light spreads across his visor and the doorway frame". C33: "the steady red glow on her visor". C38 Görsel: "A faint green glow from the ark outside the canopy lies as a soft reflection across the upper edge of his clear visor". C38 Video: "sliding across his visor" ve "fades from the visor".
NEDEN    Vizörde ışık deseni 1:47'de HUD üretti (A11). C38'in yeşil kaynağı da tutarsız: ark yeşil yanmıyor, dış ışık yıldız ve fırın turuncusu.
ARIZA    T06 · T05
ÖNERİ    Yansıma karede kurulur, videoda kaymaz ve solmaz. C38'de yeşil yansıma yerine kokpitin amber ya da camgöbeği ışığı yazılır.

### B10 · KÜÇÜK · `body` kelimesi promptlarda, başlıklar "geçmez" dediği halde
KANIT    G01 C02 ve C07: "using the back full-body panel". G02 C13, C17, C19: "full-body panel". G02 C24: "their bodies in three-quarter view toward the camera". G04 C40, C42, C43, C46, C48: "using the front full-body panel". G04 başlığı: "`body` sözcüğü ve türevleri hiçbir promptta geçmez". G02 başlığı: "`body` ve türevleri geçmez". G03 aynı paneli `full-length` yazmış. BILINEN §A sıra 1 `body`'yi listeliyor.
NEDEN    Kelime reddi açılışın C02 karesini de etkiler. Çözümü bilinen ve bedava, önceden yapılabilir.
ARIZA    yeni (BILINEN §A)
ÖNERİ    FILM §3 panel adları `front/back/side full-length panel` olur. G01, G02 ve G04 buna göre değişir. G02 C24'te "bodies" yerine "torsos".

### B11 · KÜÇÜK · Açılış C01'de karakter adı prompt gövdesinde
KANIT    G01 C01 Video: "Leon's low, dry voice as a calm voice-over says". G02 başlığı: "Adlar (Leon, Rhea) prompt gövdesine yazılmaz (büyük harfli ad kadraja basılır, BILINEN §C)". BILINEN §C: "`ORION` (büyük harfli ad) | göğüs kutusuna yazıldı". G04 C44 aynı VO'yu adsız yazıyor.
NEDEN    Kadrajda kimse yokken ad hem yazı olarak basılabilir hem de insan çağırabilir (A08). Açılışta yazı kare kapısını düşürür.
ARIZA    T06 · A08
ÖNERİ    "Leon's low, dry voice" yerine "a low, dry adult man's voice, calm and guarded, as a calm voice-over" yaz. FILM §3 SES KİMLİĞİ'ndeki VO tarifi de aynı biçime geçer.

### B12 · KÜÇÜK · Taşıyıcı olay son saniyede ve 10 s'lik Frames to Video ölçülmedi
KANIT    C05: "the two collars meet gently in the last second". C06: "8-10 s: The clamp seats against the collar rim and locks home at its latch". C25: "8-10 s: it reaches its hinge stop". FLOW_GERCEKLERI: Frames to Video "4 · 6 · 8 s", Omni "süre ?"; "10 s yalnız Omni Flash Ingredients". GOSTERIM dizi A: "tırabzana bir avuç kala çekim biter".
NEDEN    Süre 8 s çıkarsa bu üç payoff kesilir. C05'te iki katı gövdenin teması kare içinde kalır (A04).
ARIZA    T01 · A04
ÖNERİ    C05 temas olmadan, "a thin gap remains" ile biter. Temas C06'nın ilk karesindedir. C06 kilitleme 5-8 s'ye, C25 durma 5-8 s'ye çekilir. Son vuruş kamera sürüklenmesiyle sürer.

### B13 · KÜÇÜK · Altı klipte ilk replik 1,0 s'de, geçiş aralığının sınırında
KANIT    FILM §5: R10 (C11) · R22 (C22) · R25 (C24) · R36 (C36) · R41 (C40) · R45 (C43), hepsi 1,0 s. G01 C11 Video: "At about 1 s his lips move". FILM §6: "J/L 1 s". G03 başlığı: "hiçbiri geçiş aralığına, ilk/son 1 s'ye düşmüyor".
NEDEN    Model sesi isteneni genelde erken verir. Konuşma kesme çaprazına düşer.
ARIZA    yeni
ÖNERİ    İlk satırlar 1,5 s'ye, ikinci satırlar 0,5 s sonraya alınır (R11 5,0 · R23 3,5 · R26 3,5 · R37 4,5 · R42 5,0 · R46 4,0). FILM §5 ve vuruş etiketleri güncellenir.

### B14 · KÜÇÜK · Kriyo penceresinin yeri üç farklı
KANIT    G01 `7.KORIDOR` ve C07: pencere sol duvarda, köprü kapısı da sol duvarda. G02 C13: "a side observation window in the right-hand wall glows faintly green", köprü kapısı solda. G04 C48: "in the wall between them a cryo observation window glows faintly green".
NEDEN    Koridorun aynı yönünde pencere bir yerde sol, bir yerde sağ, bir yerde kapıların arasında.
ARIZA    T11 · T04
ÖNERİ    C13'ten pencere çıkar (kavşakta zaten pencerenin önündeyiz), ışık cümlesi kalır. C48'de pencere sol duvara alınır.

### B15 · KÜÇÜK · Leon'un tether bağlantı yeri C14 ve C42'de çelişebilir
KANIT    G02 C14 notu: "Hangi elin kullanıldığı yazılmadı". C14 Görsel: Leon "from his left front", "one white glove already rests on that anchor block". G04 C42 Görsel: "At the frame-left side of his waist … his right glove rests on it". G04 C42 notu: "G02 C14 aynı tarafı tarif etmeli".
NEDEN    Sol yandan ¾ çekimde sağ kalça uzak yanda kalır. Sayfa 1 tarafı söylemiyor. Cutter ve tether her karede yer değiştirebilir.
ARIZA    T09
ÖNERİ    Sayfa 1'e "coiled tether on his left hip, cutter on his right hip" yaz. C14 ve C42'de "his left glove". C42 önden çekim olduğundan blok kare sağında görünür.

### B16 · KÜÇÜK · Boş kadrajda "crouching person" ölçü cümlesi
KANIT    G03 C30 Görsel: "a heavy rectangular graphite storage crate … as tall as a crouching person's shoulders". Aynı cümle C29 ve C31'de de var. FILM §4 C30: "insan yok".
NEDEN    İnsansız kadrajda kişi göndermesi beden çağırır (A08).
ARIZA    T15 · A08
ÖNERİ    "as tall as a crouching person's shoulders" yerine "about 1.2 m high". Üç çekimde birebir aynı kalır.

### B17 · KÜÇÜK · "rises" fiili vakumda alev ya da duman çağırabilir
KANIT    G01 C12 Video: "one contained pulse of orange furnace light rises behind the blast ribs". G04 C44 Video: "A low pulse of orange furnace light rises behind the blast ribs".
NEDEN    T03 hâlâ ağır bir sınıf (22/49 film). Yükselen turuncu ışık hacimli alev ya da pus olarak çizilebilir.
ARIZA    T03 · A12
ÖNERİ    "rises" yerine "swells in place". Kaburga kenarlarının aydınlanması aynı kalır.

### B18 · KÜÇÜK · Replik metninde `dead` ve `dies`
KANIT    FILM §5 R38 (C37): "The gate drive is dead. The capture locks are still powered." R21 (C21): "even if power dies". BILINEN §A sıra 1 `dead`'i listeliyor. G02 C21 notu `dies` için "listede yok" diyor.
NEDEN    Replik video prompta birebir giriyor. Kelime reddi gelirse klip düşer, yedek kayıt devreye girer.
ARIZA    yeni (BILINEN §A)
ÖNERİ    R38 "The gate drive has no power. The capture locks are still powered." R21 "even if power fails". Sahibin "plan farklarını düzelterek başla" kararı bunu kapsıyor.

### B19 · KÜÇÜK · Dış çekimlerde gök cümlesi dört biçimde
KANIT    G01 başlığı: "`Everything hangs in deep black space with sparse stars.`". G02 C16 ve C18: "Deep black space with sparse stars surrounds the foundry, and a huge curved blue gas giant fills the far background." G03 C35 Görsel'de gök cümlesi yok: "Beyond the gate lies open space". G04 C44'te yalnız "A huge curved blue gas giant fills the far background."
NEDEN    Aynı dünyanın dış kareleri arasında renk sıcaklığı ve gezegen sıçraması riski (T18).
ARIZA    T18
ÖNERİ    FILM §3'e tek dış gök cümlesi yazılır (G02'deki biçim). C35 ve C44 dahil bütün dış karelere birebir girer.

---

KORU: C14, C15, C42 ve C45 notlarındaki "YEDEK" satırları (kavrama ya da dokunuş çıkar, eldiven nesne üstünde kalır). Bunlar GOSTERIM ilke 2'nin uygulaması.
KORU: C12 ve C44'te "exhaust" kelimesinin atılıp olayın fırın ışığı olarak yazılması (T03).
KORU: Her mekânın ortak görünüm ve ortam sesi cümlelerinin her video promptunda birebir olması (kesme sürekliliği). Telsiz klipte kadrajdaki kişinin ağzının kapalı yazılması da aynı şekilde korunmalı (C26, C27, C29).

BULGU YOK (çekim kodu · "Clip n of N" · referans kodu · olumsuz blok · vuruş iskeleti): okuduğum prompt gövdelerinde görmedim. Vuruşlar 2-4 aralıkta, ilk vuruş hareketle başlıyor, son vuruş donmuyor. Tam metin taraması koşulmadı.

KAPSAM DIŞI: 95 replik, 70'lik bandı aşıyor (FILM §5 bant dışı gerekçesi var). Bu bir hikâye ve diyalog konusu.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 7 · KÜÇÜK 12
KARAN    TUR KAPANABİLİR (ÖLÜMCÜL yok). B1-B7 için yazar cevabı gerekir.
GİRDİ    `/Users/dai/github/apex_md/film_md/uretim_hatti/ELESTIRI_PROTOKOLU.md`, `BILINEN_TUZAKLAR.md` (tam), `ARIZA_LISTESI.md` (tam), `ILK_30_SANIYE_KILAVUZU.md` (tam), `PROMPT_HATA_ATLASI.md` (satır 28-163), `GOSTERIM_COZUMLERI.md` (satır 28-147), `FLOW_GERCEKLERI.md` (yalnız grep satırları). Eser: `/Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/FILM.md` satır 1-507 (§1-§5 ve §6 başı), `PROMPTLAR/G01.md`, `G02.md`, `G03.md`, `G04.md` (tam). EKSİK: yok. Görevin istediği her dosya açıldı.
YAPILMADI  Kelime taraması (`body`, `EMP`, ad, `dead`) tüm dosya genelinde grep ile yapılmadı. Karakter sayımı yapılamadı (3300+ taraması boş döndü). Kulakla ses dinleme ve kare incelemesi yok, çünkü kare ve klip henüz üretilmedi. G05-G08 kapsam dışı.
