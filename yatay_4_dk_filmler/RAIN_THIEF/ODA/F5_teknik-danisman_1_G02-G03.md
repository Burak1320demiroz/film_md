TEKNİK DANIŞMAN · RAIN_THIEF · Faz 5 · tur 1 · G02 (C09-C16) + G03 (C17-C24, C21Y)

Dosyamda numaralı soru listesi yok. Kontrol listesini çekim çekim cevapladım (en altta). Kare ve video yok, yalnız metin değerlendirildi. Plan "plandan asla dışarı çıkma" olduğu için plan cümlesini değiştiren düzeltmelere "sahip kararı" yazdım.

### B1 · CİDDİ · 10 s vuruş planı ölçülmemiş klip süresine dayanıyor
YER       G02/G03 bütün Video blokları; `FILM.md:7`
KANIT     `KLIP_SURESI    ölçülmedi` · FLOW_GERCEKLERI.md:30 "Karelerden video … 4 · 6 · 8 s" (Omni kareden video "süre ?") · G03 C23 Video "8-10 s: One continuous slow pullback. The market receives rain for the first time; Tula's cup begins to fill"
ETKİ      Klip 8 s çıkarsa sonuç vuruşları kesilir. Son vuruşu tam 8 s'de başlayan çekimler: C11 C12 C15 C18 C20 C21 C22 C23 C24 (9/16). Kalan 7/16 çekimin son vuruşu 8 s'den önce başlayıp 10'a uzanır.
DOĞDUĞU   araç
KURAL     FILM.md:18 SMOKE P14 [ARAÇ]
ARIZA     yeni
DÜZELTME  İlk pilot denemede (C21_d1 ya da C23_d1) `ffprobe` ile süreyi ölç. Süre <10 s ise bütün vuruşları yeniden ölçekle; sonuç anlarını 7 s'ye çek.

### B2 · CİDDİ · C21 ve C21Y1: parmak-toka teması ve ponço çıkarma kadrajda duruyor
YER       G03 C21 Görsel/Video; C21Y Y1 Görsel/Video
KANIT     C21 "Left fingers touch the single white oval breakaway neck clasp" · "opens the single clasp with the left hand and slips the shoulders forward out of the loose poncho" · Y1 "Left fingers touch the clasp." · Y1 Video "Kett's left fingers close gently on the single white oval clasp. 3-7 s: The clasp opens in one small motion"
ETKİ      Yedek bile temas anını makro çekiyor. En sık bozulan hata olan "parmak tokaya erir" (BILINEN_TUZAKLAR.md:47) yedekte de kalıyor. Asıl C21 ayrıca "bedenden bir şey çıkarma" tuzağına giriyor (:21).
DOĞDUĞU   kare · hareket
KURAL     BILINEN_TUZAKLAR.md:21, :47 (kayıtlı vaka, kural kapısı değil); T01 çaresi "temas anı gösterilmez, kesmeyle atlanır". Plan §10 yalnız "toka detayı" ister, temas istemez.
ARIZA     T01 · T05
DÜZELTME  Yedekte Y1 Görsel `Left fingers touch the clasp.` → `The clasp hangs open; the left hand is lowered out of frame.`, Y1 Video 0-3 s `…as Kett's left fingers close gently on the single white oval clasp.` → `…toward the open clasp.`, 3-7 s `The clasp opens in one small motion and the loose …` → `The loose …`. Böylece açılış anı kesmeyle atlanır. Asıl C21'i pilot cevaplar; bozulursa aynı promptu yeniden gönderme, doğrudan Y1/Y2'ye geç.

### B3 · CİDDİ · C21: ORTAK HAREKET "costume state'i koru" der, çekim ponçoyu çıkarır
YER       G03 C21 Video
KANIT     "Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side." ↔ "slips the shoulders forward out of the loose poncho … At the end Kett is without the poncho"
ETKİ      Zıt istek. Model "costume state"i koruyup ponçoyu çıkarmayabilir. C18'de aynı cümledeki "prop placement" çekirdeğin yuvaya taşınmasıyla, C11'de pulun cebe girmesiyle çelişir.
DOĞDUĞU   metin
KURAL     FILM.md:152 ORTAK HAREKET (plan §7 birebir) [SÖZLEŞME/plan]
ARIZA     T05
DÜZELTME  Sahip kararı. Yalnız C21 Video'da `costume state, ` sil (daha kısa). Önce planın birebir hâli denenir; ponço yerinde kalırsa sebep bu cümledir.

### B4 · CİDDİ · C18: çekirdeğin yuvaya girişi ve elin bırakması 8 s boyunca kadrajda
YER       G03 C18 Video 0-8 s
KANIT     "Kett lowers the core straight into the matching socket until it locks with a single mechanical seating action. 5-8 s: The right hand releases it and moves away."
ETKİ      Üç parmaklı el, silindir ve oluklu yuva yakın planda birleşiyor. Çekirdek ele yapışabilir, ikiye çoğalabilir, yuvaya gömülebilir. Bu çekim çekirdek devamlılığının (C18-C24) tek kanıtı.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:47 + FILM.md:185 risk sütunu "tek çekirdek, tek yuva; çekirdek kırılmaz"
ARIZA     T01
DÜZELTME  Frames to Video'da bitiş karesi ver (FLOW_GERCEKLERI.md:30; davranışı ölçülmedi, §9): `kare/C18_son.png` = çekirdek yuvada, el uzakta. Olmazsa kurguda 5 s'den sonra kes ve C19'a geç (çekirdeğin oturması sol vuruşta yarım kalır).

### B5 · CİDDİ · C11: küçük pulun cebe girişi çekimin tek olayı
YER       G02 C11 Video 3-8 s
KANIT     "uses the left hand to tuck the orange token into the belt pocket." · Görsel "Left fingers rest on one small orange boarding token at the belt beside an open pocket."
ETKİ      Küçük nesne, üç parmak ve küçük cep: pul parmağa kaynayabilir, kaybolabilir ya da çoğalabilir. Sağ elde ikinci nesne (çekirdek) de var.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:47
ARIZA     T01
DÜZELTME  Kare kapısına ekle: pul parmak uçlarından ayrı ve net, cep açık. Kaynaşırsa kurguda pul cebe girmeden (≈5 s) kes. Cebe giriş kesmeyle atlanır; C12 pulsuz başlar.

### B6 · CİDDİ · C09: "kısa bölüm" ile "6 m çatıya ulaş" aynı vuruşta
YER       G02 C09 Video, satır 34
KANIT     "0-4 s: Track gently upward as Kett climbs a short section of the fixed service ladder … 7-10 s: … Kett reaches the six-meter roof level; the core stays in the right hand."
ETKİ      Kett 95 cm boyunda, 6 m çıkması ≈6 boy eder. Tek elle, 10 s'de bu mesafe için model ya hızlandırır ya da sıçratır. Sonuç cümlesi "short section"la çelişiyor ve sahnenin iddiasını aşıyor.
DOĞDUĞU   metin
KURAL     FILM.md:35 FILM §5 vuruş planı (Devamlılık satırı son vuruşta sabit kalanlar içindir)
ARIZA     T02 · T10
DÜZELTME  `Kett reaches the six-meter roof level; the core stays in the right hand.` → `The core stays in the right hand.` (çatıya varış kurguyla C10'a bağlanır). Ek paragrafta `with the alien crowd below and the bridge and the reservoir above` → `…and the roofs and the reservoir above` ("bridge" hiçbir yerde tanımlı değil, B18'e bak).

### B7 · CİDDİ · C13: kayış 6 s'e yayılmış, ardından 4 s yalnız olumsuz cümle
YER       G02 C13 Video, satır 133
KANIT     "0-6 s: Show one simple seated slide down the existing sloped rust-orange canopy … 6-10 s: Limit the height to the established short drop. Do not add a jump, flip, camera cut or second stunt."
ETKİ      2 m'den kısa bir kayış 6 s sürerse süzülme gibi okunur. Son 4 s'de olumlu eylem yok, olumsuz cümle tutmuyor ve model boşluğu kendi eylemiyle doldurur.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:48; yasak listesi ("no X" ölçüldü, tutmuyor)
ARIZA     T08 · T02 · T10
DÜZELTME  İlk deneme: `0-6 s:` → `0-4 s:` ve `6-10 s:` → `4-10 s:`. İkinci deneme gerekirse (aynı prompt değil): `Do not add a jump, flip, camera cut or second stunt.` → `Kett settles upright on the landing.`

### B8 · CİDDİ · C12: Kett'in repliği sürerken Vorr'un ağzı kapalı yazılmamış
YER       G02 C12 Video, satır 106
KANIT     "5-8 s: Hold his face while Kett's brief reply is heard off-screen." (C23'te aynı durum için `Mara's mouth stays closed` yazılmış)
ETKİ      Vorr'un yüzü kadrajda tutulurken model dudağı oynatmayı sürdürebilir. Seyirci Kett'in cümlesini Vorr'un ağzından duyar (başka ağızdan konuşma).
DOĞDUĞU   metin
KURAL     Kontrol listesi "Model sesi repliği (a)"; C23 emsali
ARIZA     yeni
DÜZELTME  `Hold his face while` → `Hold his face, mouth closed, while` (+2 kelime, cümle başka şeyi uzatmıyor).

### B9 · CİDDİ · C19: kadraj dışı konsol, çekirdek ve çark adıyla yazılmış
YER       G03 C19 Görsel ek paragraf (satır 73) ve Video (satır 80)
KANIT     "Existing blue distribution pipes connect the console to the large transparent water reservoir arc overhead" · "Kett and the console are off-screen." · "the core is in the socket and the wheel is closed, both just outside the frame." · Video "End with him within a few steps of the console, within reaching distance. Keep the camera on Vorr alone."
ETKİ      Anılan nesne kadraja girer: konsol/çark geri planda belirir ya da son beat'te Kett ve konsol kadraja gelir. Vorr "tek başına" kalmaz.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md §C (prompt'taki kelime kadraja basılıyor)
ARIZA     T15 · yeni
DÜZELTME  `connect the console to the large transparent water reservoir arc overhead` → `lead to the large transparent water reservoir arc overhead`. Devamlılık cümlesindeki `the core is in the socket and the wheel is closed, both just outside the frame.` kaldır (Görsel ve Video'da). Video'daki `within reaching distance` aynı kalır.

### B10 · CİDDİ · C20: boyun, boğma ve vurma kelimeleri üç yerde
YER       G03 C20 Görsel satır 97 ve 99; Video satır 106
KANIT     "never Kett's neck or body" · "Vorr grips only the poncho fabric; there is no contact with the neck or the wrist." · "No choking, lifting or striking."
ETKİ      Büyük bir figür küçüğü yakasından tutuyor. Şiddet sözcüğü olumsuz blokta yazılsa bile red nedeni olabiliyor. `body` listede açıkça var.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:19 [kayıtlı vaka]; `choking`/`striking` listede yok, yakın anlamda. Planın kendi cümleleri, HİPOTEZ plan lehine, sahip kararı.
ARIZA     yeni
DÜZELTME  Red gelirse sırayla: `No choking, lifting or striking.` sil → `never Kett's neck or body` sil → `no contact with the neck or the wrist` sil. Kalan `grips only the back collar fabric` yeter. (`body` ayrıca bütün kimlik cümlelerinde var, ölçülmedi; kapak olarak yalnız C20'de olumsuz bağlamda.)

### B11 · CİDDİ · Mavi tentenin "tam açık" durumu hiçbir referans sayfasında panel değil
YER       G02 C15 Görsel (satır 173) ve not (satır 169); C14, C16, C12
KANIT     C15 not: "R07 sayfasındaki 'folded blue delivery canopy' satırı çelişeceği için yazılmadı … açık tente plan metniyle tarif edilir." C14 "the folded reinforced blue delivery canopy". C12 Ref 7'den hem "the short rust-orange canopy" hem "the folded blue delivery canopy".
ETKİ      Tente üç durumda (katlı → uzayan → tam açık) geçiyor ve yalnız katlı durum referansta var. C15 karesi C14 sonundan farklı bir nesne üretir. C12'de turuncu ve mavi tente tek tentede birleşebilir (SMOKE P17 yanlış panel).
DOĞDUĞU   referans
KURAL     FILM.md:101-102 (durum paneli tek sayfada); kontrol listesi T05 · T09
ARIZA     T09 · T05
DÜZELTME  `7.CATILAR_v2`: "fully extended blue canopy" paneli ekle, sürüm artar. Sürüm artmazsa C15 ve C16 karesine ek kapı: "tente tam açık, iki sahanlığı bağlıyor". C12'de iki tentenin renk karışması için kare kapısında ayrı bakılır.

### B12 · CİDDİ · ORTAK GÖRÜNÜM'deki gezegen yakın planlarla çelişiyor
YER       G02 C14 Görsel; G03 C18, C21, C21Y1, C21Y2 Görsel
KANIT     "one pale ringed planet" (ORTAK GÖRÜNÜM) ↔ C21 "Soft background shows only Vorr's right hand gripping the loose back fabric." ↔ C18 "Behind the socket the copper console fills the soft background."
ETKİ      Gezegen kadraja basılır: yakın planda yüzün ya da elin yanında asılı bir daire.
DOĞDUĞU   metin
KURAL     FILM.md:165-166 "Işık, su, gezegen … çekim cümlesine gider (DERS Y6)" [HİPOTEZ]; plan §6 birebir
ARIZA     T04
DÜZELTME  Sahip kararı: yalnız bu beş promptta `one pale ringed planet, ` sil. Önce planın hâli, kare kapısında gezegen çıkarsa o promptta silinir.

### B13 · CİDDİ · 9 ağız kadrajda replikte dudak senkronu ve altyazı riski
YER       G02 C10 C12 (R11) C14; G03 C19 C20 C21 C22 C23 (R18) C24
KANIT     FILM.md:230+ "ağız kadrajda — temiz replik ayrı kayıt" (HUMAN) · `Return silent videos AÇIK` · Dialogue blokları `1. KETT: "…"`
ETKİ      Video sessiz, ses kurguda sonradan kaydediliyor. Dudaklar kayıtla eşleşmez. Tırnaklı metin altyazı olarak basılabilir (`KETT:` büyük harfli etiket, BILINEN_TUZAKLAR §C `ORION` emsali). Ölçülmedi.
DOĞDUĞU   seçim · kurgu
KURAL     BILINEN_TUZAKLAR.md:72-77; kontrol listesi "Ağız kadrajdaki replik"
ARIZA     yeni
DÜZELTME  Kare kapısı/deneme notu: altyazı ve etiket yazısı var mı. F8'de kaydı denemedeki ağız açık/kapalı kalıbına göre zamanla. C10 yan profil, C22 baş eğik: bu ikisi en az görünür dudak. C14 (Mara'nın dikey ağzı, "shouts") en riskli; `shouts` → `calls` daha az geniş ağız açar (aynı uzunlukta).

### B14 · CİDDİ · C23 (pilot): bir klipte beş durum değişimi, Mara hem kadrajda hem ekran dışı
YER       G03 C23 Görsel + Video, satır 213 ve 222
KANIT     "Mara stands beside Tula." ↔ "Hold on Tula's reaction while Mara answers from just off-screen. Mara's mouth stays closed while her answer comes from just off-screen." · "5-8 s: Background aliens lift faces or hands in small independent gestures … 8-10 s: One continuous slow pullback … Tula's cup begins to fill"
ETKİ      Yağmur başlaması, çiçek açılması, fincan dolması, 8 türün bağımsız jestleri ve geri çekilme tek klipte; 10 figür var (T15). Mara kadrajda kapalı ağızla sessizce dururken sesi duyulur (dublaj gibi okunur).
DOĞDUĞU   anlatım · hareket
KURAL     Pilot sorusu C23; FILM.md:195 risk sütunu
ARIZA     T15 · T03 · T01
DÜZELTME  İlk deneme plan metniyle. Bozulursa ikinci denemede (aynı prompt değil) `Background aliens lift faces or hands in small independent gestures.` sil. Mara için sahip kararı: `Mara stands beside Tula.` → `Mara stands beside Tula, facing the sky.` (ağız görünmez, ek malzeme yok).

### B15 · KÜÇÜK · "status glow" ve "activation pulse" gösterge çağrıştırır
YER       G03 C18 Video satır 57; C22 Video satır 196
KANIT     "A dim blue status glow appears" · "a soft blue activation pulse travels into the existing public pipes"
ETKİ      `status` ekran/gösterge getirir; R08 "no electronic screen or readable writing" ile çelişir.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:48
ARIZA     T06
DÜZELTME  `A dim blue status glow appears` → `A dim blue glow appears` (daha kısa).

### B16 · KÜÇÜK · Sessiz filmde ses ve "dialogue" kelimeleri
YER       G02 C11 satır 83; C16 satır 205; G03 C17 satır 34
KANIT     "Let the engine fade without dialogue." · "His weight produces heavy metallic footsteps." · "No dialogue, no new machinery materializes."
ETKİ      Ses isteği silent çıktıda boşa gider, `dialogue` repliksiz klipte ağız hareketi tetikleyebilir. Egzoz/motor görseli üretebilir.
DOĞDUĞU   metin
KURAL     DERS Y13; yazarın kendi önerisi
ARIZA     T13
DÜZELTME  C11 `Let the engine fade without dialogue.` → `Let the skiff fade into the distance.` · C16 `His weight produces heavy metallic footsteps.` → `His weight shows in each heavy step.` · C17 `No dialogue, no new machinery materializes.` → `No new machinery materializes.`

### B17 · KÜÇÜK · C24: derinlik sırası iki yerde farklı
YER       G03 C24 Görsel satır 240 ve 242
KANIT     "Coatless Kett stands on the far side of the console … Vorr stands a few paces away on the near side" ↔ "Kett in front on the right, Vorr soft on the left"
ETKİ      Hangisinin kameraya yakın olduğu belirsiz; "near" olan "soft" (bulanık) yazılmış.
DOĞDUĞU   metin
KURAL     kontrol listesi T11
ARIZA     T11
DÜZELTME  `on the far side of the console` ve `on the near side` sil; Kamera satırı derinliği taşısın.

### B18 · KÜÇÜK · Atıf ve tanımsız kelimeler
YER       G02 C14 satır 147; G03 C23 satır 213; C17 satır 25; G02 C09 satır 27
KANIT     "the same brass awning lever previously shown" · "Return to the established market flower stall … the same previously empty cup" · "No black hole." · "the bridge and the reservoir above"
ETKİ      Referanssız atıf boşa gider. `No black hole` olumsuz cümle tutmuyor ve kara delik çağrıştırabilir. `bridge` tanımsız.
DOĞDUĞU   metin
KURAL     film_dogrula ATIF regex'i `previous shot` yakalar, `previously` yakalamaz (araç satır 57); G03'te C05'te aynı tür atıf M düzeltmesi yapılmıştı.
ARIZA     yeni
DÜZELTME  `previously shown` sil; `Return to the established market flower stall, same layout` → `At the market flower stall, same layout`; `the same previously empty cup` → `the same empty cup`; C17 `No black hole.` sil (sahip kararı, plan cümlesi).

KORU: G02/G03 hiçbir çekim kodunu, referans kodunu ya da "Clip n of N" metnini prompt gövdesine yazmamış. Dialogue blokları `film_dogrula M` ile uyumlu.

### Kontrol listesi, çekim çekim

| Çekim | T01 temas | Sıvı/duman (T03·T13) | Yazı/ekran (T06) | Durum/panel (T05·T09) | Kişi (T15) | Zor hareket (T02·T10) | Açılış |
|:--:|---|---|---|---|---|---|---|
| C09 | sol el-basamak 10 s, sağ el-çekirdek | yok | yok | yok | 1 + arka kalabalık | tek elle 6 m: B6 | — |
| C10 | yok | camın arkasında yağmur; yansıma ölçülmedi | "no readable signage" | yok | 1 + 2 uzak silüet | yok | — |
| C11 | sol el-pul-cep: B5 | yok | yok | pul cebe giriyor | 1 | yok | — |
| C12 | yok | yok | yok | iki tente: B11 | 2 (Vorr + Kett arkadan, hikâye şart) | Vorr bir adım | — |
| C13 | sol el-kumaş, kalça-kumaş | yok | yok | çekirdek gövdede | 1 | oturarak kayış: B7 | — |
| C14 | el-pirinç kol | yok | yok | tente katlı → açılıyor: B11 | 1 | yok | — |
| C15 | ayak-kumaş (dalma) | yok | yok | tam açık: B11 | 1 + 3 aşağıda | koşu | — |
| C16 | yok | yok | yok | tente uzak: B11 | 1 + uzak Kett | merdiven çıkışı | — |
| C17 | yok | rezervuarda su | "by shape rather than by writing" | çark kapalı | 1 küçük | yok | — |
| C18 | el-çekirdek-yuva: B4 | yok | "status glow": B15 | çekirdek elde → yuvada | 1 (yalnız el) | yok | — |
| C19 | yok | yok | yok | yok | 1 | yürüyüş + replik | — |
| C20 | el-ponço kumaşı (kurulu başlar) | yok | yok | ponço gerilir | 2 (hikâye şart) | yok | — |
| C21 | parmak-toka, el-kumaş: B2 | yok | yok | ponço çıkıyor: B3 | 1 + Vorr eli | yok | — |
| C22 | iki el-çark 5 s | boru "pulse" | "activation pulse": B15 | Ref 2 (ponçosuz) | 1 | çark yarım tur, tüm gövde ağırlığı | — |
| C23 | yok | yağmur, fincan dolumu | yok | çiçek açılıyor | 10 (B14) | yok | — |
| C24 | Vorr eli-ponço, açık avuç-yağmur | yağmur | yok | yok | 2 | yok | — |

Diğer kontroller:
- T08: C15'te "floating amber jelly alien" (C23'te de) "realistic consistent downward gravity" ile aynı kadrajda. Tür olduğu için bulgu yazmadım, kare kapısında Kett'in süzülmediğine bak.
- Mod ↔ model: bütün çekimler Frames to Video, malzemeden video/uzatma yok; Quality ile çakışma yok. Yedek Y1/Y2 için de aynı. C21Y her klibin yalnız ilk ≈5 s'sini kullanır.
- Kesme sürekliliği: ardışık aynı-mekân çiftlerinde ölçek/açı farkı var (C09 geniş yan → C10 yanal orta → C11 orta yakın; C19 orta → C20 yandan orta iki kişilik → C21 çok yakın). C10→C11 tek zayıf nokta: C11'in kamera tarafı yazılmamış. Bütün klipler durağan kareden başlıyor (Frames to Video), ortak görünüm cümlesi eksik prompt yok.
- Meta etiket/kod: gövdede çekim kodu ve referans kodu yok.

KAPSAM DIŞI: plan S21 "göğsündeki beyaz tokayı açar" ↔ kimlik cümlesi "neck clasp at the center front of the neck" (devamlilik).
KAPSAM DIŞI: C14 pazar yerinde yer tentesi → C15 çatı sahanlıklarını bağlayan köprü (M1 → M2 coğrafyası, devamlilik/dramaturg).

ÖZET     ÖLÜMCÜL 0 · CİDDİ 14 · KÜÇÜK 4
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok; yazar 14 CİDDİ bulguya KABUL/RED cevabı verir)
GİRDİ    `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/RAIN_THIEF/PROMPTLAR/G02.md`, `G03.md`; `FILM.md` (§1-§5, §3 kimlik cümleleri, satır 1-292); `RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md` (C09-C24 bölümleri, §8); `ODA/F5_yazim_karari.md`; `SAHNELEME.md` (şablon, boş); `uretim_hatti/ELESTIRI_PROTOKOLU.md`; `BILINEN_TUZAKLAR.md`; `ARIZA_LISTESI.md` T bölümü; `FLOW_GERCEKLERI.md` §1; `araclar/film_dogrula.py` (ATIF regex)
YAPILMADI  kare yok, video yok; hareket için "görülmedi". `ILK_30_SANIYE_KILAVUZU` §6 açılış kontrolü bu gruplarda uygulanmadı (açılış C01-C03, G01'de). FILM.md satır 293-373 okunmadı.
