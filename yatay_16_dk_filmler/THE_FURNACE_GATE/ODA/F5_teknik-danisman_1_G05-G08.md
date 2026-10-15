**Okunamayan ya da açılmayan kısımlar (görev metni gereği):**
- `GOSTERIM_COZUMLERI.md` 141. satırdan sonrası okunmadı. Yalnız §1–§5'in başı okundu.
- `FILM.md` §6 ve sonrası, G01 C01–C12, G02–G04, `ODA/*`, `NOTLAR.md` ve `DURUM.md` açılmadı. Gerekçe girdisi olduklarından bilerek açılmadı. Kalanı kapsam dışı.
- `SMOKE_TEST.md` açılmadı. P9, P17 ve P18 yalnız `FLOW_GERCEKLERI.md` ve `GECIS_VE_SES_SUREKLILIGI.md` üzerinden anıldı.

Eserin kendisi tam okundu: G05–G08 (C49–C96), G01 başlık ve REFERANS PROMPTLARI, FILM.md §3 §4 §5.

### B1 · CİDDİ · Sürekli temas ve temas sırasında hareket: 13 çekimde
KANIT
- G06 C65: `the white glove pulls the orange lever down in one firm arc around its fixed hinge` ve `7-10 s: … the glove stays wrapped around the grip`. C67 ve C71 aynı kalıp.
- G05 C60: `her glove, closed around the broad blue lever, pulls it steadily toward her`.
- G06 C70 son vuruş: `The glove closes the last short distance and settles onto the grip`. Temas anı ekranda.
- Aynı sınıf: C51 (anahtar çevirme), C56 (başparmak çevirir), C58 (iki eldivenle indirme), C77 (tether çekme), C78, C79, C83 ve C88 (anahtar çevirme).
- `GOSTERIM_COZUMLERI.md` İlke 5: "Sürekli temas kısa; temas sırasında hareket küçük" (≤3 s).
- Aynı dosya İlke 2: kurulu temas "büyük hareketli 10 s'lik çekimde bozuldu" (STOLEN_SKY S03 ve S58).

NEDEN: Eldiven 10 s kola sarılı kalıp kolla birlikte hareket ediyor. Depo bu durumda temas cümlesinin tutmadığını gösteriyor (COUNTED_TURN 22/25 → 7 🔴).

ARIZA: T01

ÖNERİ
- C60, C65, C67, C71 ve anahtar çekimlerinde hareketi ekrandan al. Başlangıç karesi işin sonucunu gösterir: kol alt durdurucuda, anahtar yeni konumda, eldiven tutar ve kıpırdamaz (GOSTERIM §1 "el temas kurulu başlar ve kıpırdamaz").
- Video yalnız kamera itişi ve sonuç ışığıdır: kol tabanında camgöbeği lamba, çekirdeğin amber parlaması. Çekiş kesmeyle atlanır, tık sesi kurguda.
- C70'te 8-10 vuruşunda eldiven kola değmez, bir avuç yanında durur. C71 zaten kolu tutarak başlıyor.
- Önce C60 denenir. Bozulursa aynı prompt yeniden gönderilmez.

### B2 · CİDDİ · Vakumda kıvılcım, çekimin taşıyıcı anı
KANIT
- G05 C52 `4-7 s: … releases one brief blue-white pulse that strikes the glass support, and a few tiny incandescent sparks fly off in straight lines and fade within a short distance`.
- Pus ve duman çıkarsa yedek yalnız notta (G05 C52 Not), birincil plan olarak yazılmamış.
- GOSTERIM §1 vakumda kıvılcım satırı: "Olay taşıyıcı an yapılmaz"; kaynak kadraj dışı, yalnız sonuç görünür.
- STATIC_VEIL S07: `without vapor … no vapor plumes` yazılıyken pus çıktı.
- Aynı sınıf, daha hafif: G08 C89 `its two rear engines glowing steady bright blue`. C57'deki `faint blue standby glow` ile çelişiyor.

NEDEN: Kıvılcım parçacığı ve atım ışını vakumda duman ya da pus doğurur. Bu, kayıtlı bir hata sınıfı.

ARIZA: T03 · T13

ÖNERİ
- C52'de yedeği birincil yap: tek parlak ışık sıçraması desteğin üstünde, parçacık yok.
- C89'da motor ışığı `faint blue glow` olsun. Parlak mavi yalnız C96'da, uzakta bir ışık noktası olarak kalsın.

### B3 · CİDDİ · Aynı klipte iki konuşan, iki ağız, şeffaf vizör: C86 · C88 · C95
KANIT
- FILM.md §4 C86: `iki replik ağız kadrajda (Rhea → Leon); finalin duygusal merkezi`. C88 ve C95'te de aynı ibare.
- G08 C86 `0-3 s: … her lips move only for her own line … You came back. 3-7 s: … his lips move only for his own line … We're not finished.`
- Ağız kapalı cümlesi ve farklı ses tarifi var. Tek konuşan ise değil.
- `GECIS_VE_SES_SUREKLILIGI.md` §2.5: Omni sesi başka klipte taklit edemez.
- GOSTERIM Örnek C: konuşan kadraj dışı, dinleyenin ağzı görünmez.

NEDEN: Üç klipte ardışık iki dudak senkronu var. Model iki ağzı birden oynatırsa ya da sesi yanlış ağza verirse finalin duygusal merkezi bozulur. Yedek kayıt ses içindir, yanlış hareket eden ağzı kurtarmaz.

ARIZA: T15 · yeni (iki ağız kadrajda)

ÖNERİ
- F7'de önce C86 denenir.
- Ağız ya da ses karışırsa GOSTERIM Örnek C'ye geçilir. Konuşan başına tek yüz, öteki flu kabuk kenarında, cevap kadraj dışından (C86'da R85, C88'de R88, C95'te R93 `model sesi (kadraj dışı)`).
- Bu karar sahipte, çünkü kompozisyon planın.

### B4 · CİDDİ · Referans paneli istenen durumu göstermiyor (SMOKE P17 yanlış panel riski)
KANIT
- G05 C59 görsel: `using the cradle close panel` ve `one broad hinged retaining latch stands raised open`.
  - FILM.md §3 `cradle close panel (mandal kulp üstünde kapalı)`.
  - G01 10.CEKIRDEK: `the broad retaining latch closed over the core's rigid carry handle`.
- G06 C64 görsel: `using the wide room panel` ve `the broad blue lever is already pulled down … the input cradle, which holds the portable core latched`.
  - FILM.md §3 `wide room panel (üç kol dik, yuva boş)`.
- G08 C91: `its two giant gantry clamp arms standing open … using the gate open panel`.
  - G01 5.FOUNDRY ikinci panel: `a heavy mechanical catch seated at the gate rim, the clamps still locked`.
  - G06 C72 aynı sorunun hafifi: port çenesi açık yazılı, panel kilitli gösteriyor.
- 1.LEON, 2.RHEA ve 10.CEKIRDEK 5 panelli. 10.CEKIRDEK'te açık ve yanık çekirdek aynı sayfada.

NEDEN: Görsel model paneli kopyalar. C59'un tek hareketi mandalın kapanması, ama kare mandalı kapalı çizebilir.

ARIZA: T05 · T09

ÖNERİ
- Sayfalar henüz üretilmedi (Onay ⬜), şimdi düzelt.
- 10.CEKIRDEK'e `cradle open panel` ekle: mandal kalkık, çekirdek oturmuş. C59 onu alsın.
- C91'de `clamps open panel` kullan.
- C64'te kamerayı turuncu kola daralt. Mavi ve teal kol kadraj dışında kalsın, mavi kolun durumu metinde yazılmasın.

### B5 · CİDDİ · Rhea'nın bilek bağlantısı: sayfada sağ, C56'da sol
KANIT
- G05 C56 görsel: `sits on the pearl sleeve of her left forearm`; sağ eldivenin başparmağı anahtarı çeviriyor.
- G01 2.RHEA: `an unmarked ivory wrist-link on her right wrist`.
- G01 başlık: `Bilek bağlantısı Rhea'nın SAĞ bileğinde … (1.LEON · 2.RHEA sayfalarında sabit)`. G01 C02, C04 ve C10 de `right forearm`.
- G05 başlık: `Rhea'nın bilek bağlantısı SOL ön kolunda (… benim seçimim, birleştirmede C04 · C10 · C37 · C93 ile hizalanır)`.

NEDEN: Yazar hizalanacağını varsayıyor, ama hizalanacağı yer zaten sağ. C56 referansı da hareketi de ters çeviriyor.

ARIZA: T09 · T11

ÖNERİ
- C56'yı sağ ön kola ve sol eldivene çevir.
- G05 başlık notunu düzelt.

### B6 · CİDDİ · Dış gök cümlesi üç sürümde, 10 dış klipte yok
KANIT
- G01 başlık: `Everything hangs in deep black space with sparse stars.`
- G05 ve G06: `Deep black space with sparse stars surrounds the foundry.` (yalnız C52 · C57 · C62 · C68 · C72).
- G07 ve G08: `§3'te ayrı bir gök cümlesi yok, gaz devi ışık cümlesinin içinde`. C74, C80, C81, C84, C85, C87, C89, C91, C92 ve C96'da yok.
- FILM.md §3'te cümle hiç tanımlı değil.

NEDEN: Aynı dünya cümlesi her dış çekimde birebir yazılmadığında gök ve renk sıcaklığı kesmede sıçrar.

ARIZA: T18

ÖNERİ
- FILM.md §3 ORTAK GÖRÜNÜM'e tek `DIŞ DÜNYA` satırı ekle: `Deep black space with sparse stars surrounds the foundry.`
- G07 ve G08 dış kare promptlarına birebir, ışık cümlesinin önüne yaz.
- G01 dış çekimleri de bu cümleye çek.

### B7 · CİDDİ · FILM.md §5 Saniye sütunu dört replikte vuruşla çelişiyor
KANIT
- §5: `R82 | C84 | 1.5 | … Contact. | 1.0`.
  - G07 C84: `4-8 s: … says: Contact.`
  - G07 Not: `FILM.md §5 R82 Saniye 1.5 → ~6.0 olmalı`.
  - G07 İş emri: dış replikli klipte klip sesi yalnız replik penceresinde (±0,5 s) açık.
- R61 (C58) 1,5 ↔ G05 C58 `4-7 s … Core seated`.
- R62 (C60) 1,5 ↔ `3-7 s … Gate feed on`.
- R59 (C56) 1,5 ↔ `2-7 s`.
- R94 (C96) 1,0 ↔ G08: C95→C96 çaprazı 1,5 s, ses köprüsü replikle çakışıyor.
- Notlarda "çekilebilir" yazıyor, FILM.md güncellenmemiş.

NEDEN: C84 dış klip. Pencere 1,5 s'ye göre kurulursa "Contact." sesi kesilir. R94'ün ilk sözcüğü çaprazın altında kalır.

ARIZA: yeni

ÖNERİ
- §5'i güncelle: R82 → 6,0, R61 → 5,0, R62 → 3,5, R59 → 2,5, R94 → 1,5.
- G05–G08 notlarındaki "çekilebilir/olmalı" ifadelerini kapat.

### B8 · CİDDİ · Büyük harfli `EMP` iki referans sayfası promptunda
KANIT
- G01 2.RHEA: `one small matte-grey fictional EMP puck`.
- G01 15.ARACLAR: `one small matte-grey fictional EMP puck with an amber indicator`.
- BILINEN §C: `EVA` (kısaltma, 10 promptta) sırta basıldı (THE_PAYLOAD).

NEDEN: Üç harfli büyük kısaltma cihazın üstüne yazı olarak basılabilir. 15.ARACLAR 22 çekimin referansı. Bu kelime için yazılı bir yedek yok.

ARIZA: T06

ÖNERİ: `EMP puck` → `pulse-emitter disc`. FILM.md §3 kaydı prompt olmadığından kalabilir.

### B9 · KÜÇÜK · `body` / `dead` / `dies`: başlıklar "yok" diyor, promptlarda var
KANIT
- G06 başlık: `body · dead · blood · wound hiçbir promptta geçmez`.
  - G06 C63 görsel: `using the side full-body panel`; C65 ve C67 aynı.
  - G06 C63 video: `Lock it before the core dies`.
- G07 başlık: `body sözcüğü ve türevleri hiçbir promptta geçmez`.
  - G07 C73 `front full-body panel`, C77, C79.
  - G07 C82 `rigid graphite rectangular body`.
- G05 C49 `Starboard release is still dead`, C49 C58 C60 görsel `full-body panel`.
- G08 aynı sorunu `full-length` ile çözmüş. G01'de koşullu yedek var.

NEDEN: BILINEN §A "kelime hiç yazılmaz" diyor. Yedek olduğu için KÜÇÜK, ama dört grup tutarsız.

ARIZA: BILINEN §A

ÖNERİ
- Tüm gruplarda `full-length` kullan, C82'de `body` yerine `casing` yaz.
- Replikleri sahip onayıyla değiştir: "still dead" → "still locked", "before the core dies" → "before the core fails". Aksi hâlde kurgu yedeği kalır.

### B10 · KÜÇÜK · Vizörde hareketli ışık deseni (HUD riski)
KANIT
- G07 C73 `a slow red glow rising and falling on the wall and across her clear visor`.
- G07 C75 `the amber reflections of the rail lamps sliding across her visor`.
- G07 C82 `its light flickering over his clear visor`.
- G06 C63 Not: `vizör yansıması istenmedi (HUD riski)`.
- GOSTERIM §4: model vizöre HUD ve yazı basmaya yatkın. ARIZA T06 (kayıt: SIGNAL_KEEPERS K11 🔴).

NEDEN: Aynı film, aynı risk; yalnız bir grup kaçınmış.

ARIZA: T06

ÖNERİ: Işık duvarda, konsolda ve kapakta kalsın. Vuruş cümlelerinden `visor` çıksın.

### B11 · KÜÇÜK · Rijit yapı hareketinde kamera politikası tutarsız
KANIT
- G06 C62 `The camera begins a slow lateral drift … while the three rigid shutters start to slide outward`.
- G06 C72 `a slow pull back and upward while the starboard jaw starts to rotate`. C68 de kayıyor.
- G07 C74 Not: `Kamera sabit: rijit kayma kamera hareketiyle karışmasın`. C80, C84, C85, C87, C89, C91 ve C92 sabit.
- FILM.md §4 C62, C68 ve C72'de kamera hareketi yok.

NEDEN: Dev yapı ve kamera birlikte hareket edince hangisinin kaydığı belirsizleşir. Bu çekimler G06'nın kendi risk sırasında ilk denenecekler.

ARIZA: T07 · T09

ÖNERİ: C62, C68 ve C72'de kamera kilitli olsun. Ritim hareket eden devin kendisinden gelir.

### B12 · KÜÇÜK · Mıknatıslı botlar yanında asılan, yatan tether
KANIT
- G07 C77 görsel: `a gentle slack curve hanging between her hand and the anchor`.
- G08 C87: `a slack navy safety tether … lies coiled on the boot plate`.
- Aynı karede `fixed magnetic boot plate`.

NEDEN: Tether yerçekimi varmış gibi sarkıyor, botlar ise mıknatısla duruyor.

ARIZA: T08

ÖNERİ: C77'de `floating in a loose curve`, C87'de `clipped at one end, drifting loose` yaz.

### B13 · KÜÇÜK · C55'te ekran üzerinde rota şekli
KANIT: G05 C55 görsel `above it a flat cyan interface surface shows an abstract route shape: one straight glowing line running into a small ring`.

NEDEN: BILINEN §B sıra 2 çözümü "yazısız tasarım (ışık çubuğu, dolu yuva)". Halka ve çizgi okunacak ekran gibi, sayı ve işaret çağırır. C88 aynı durumu tekrar kullanıyor.

ARIZA: T06

ÖNERİ: `one steady cyan light bar` yaz. C88 aynı çubuğu kullanır.

### B14 · KÜÇÜK · C90 kamera geometrisi kendisiyle çelişiyor
KANIT
- G08 C90 görsel: kamera `behind and slightly left of the man's seat, looking forward` ve `seen from behind-left … so that his left cheek and pale scar are readable through the clear visor`.
- FILM.md §4 C90: `Leon ağız kadrajda`.

NEDEN: Arkadan bakan kamera yüzü ve yarayı göstermez. İki istek birbirini yalanlıyor.

ARIZA: yeni (PROMPT_HATA_ATLASI A05)

ÖNERİ: `left cheek and scar readable` ifadesini çıkar. R89 telsiz kalıbıyla yazılsın: ağız görünmez, ses kask içinden.

### B15 · KÜÇÜK · Görünmeyen yüze ait yara belirteci kimlik tabanında kalmış
KANIT
- G07 C76 `a pale left-temple scar … seen in right profile`.
- C79 `shows the right side of his face in profile`.
- C82 `three-quarter view from his right front`.
- G01 başlık: görünmeyen parçalar çıkarılır.
- G05 C55 yarayı çıkarmış.

NEDEN: Görünmeyen yüzün yarasını yazmak modelin yarayı görünen yüze çizmesine (yansıma hatası) davetiye.

ARIZA: T16

ÖNERİ: C76, C79 ve C82 kimlik cümlelerinden `a pale left-temple scar` çıksın.

### B16 · KÜÇÜK · C91→C92 aynı ölçek ve benzer açı
KANIT
- G08 C91 `Wide view on a 24 mm lens from a slightly oblique side angle, the camera level with the gate`.
- G08 C92 `Wide view … on a 24 mm lens, the camera level with the exit gate and some distance off its axis`.
- `GECIS_VE_SES_SUREKLILIGI.md` §1.5: ölçek bir basamak değişir ya da açı ≥30° döner.

NEDEN: Aynı kapı, aynı geniş ölçek ve aynı soldan sağa hareket. Kesme zıplama gibi okunur.

ARIZA: yeni

ÖNERİ: C92'yi 50 mm orta planda, dudaktaki tug üzerinde çek.

### B17 · KÜÇÜK · C58'de efor sabitlik sözcüğüyle siliniyor
KANIT: G05 C58 video `she lowers the core straight down toward the open cradle in one steady motion, both gloves staying on the top carry handle without regripping`.

NEDEN: PROMPT_HATA_ATLASI A01: sabitlik sözcüğü yükün bedelini siler. Çekirdek "tuğ'dan değerli" bir yük.

ARIZA: T02

ÖNERİ: `one steady motion` çıksın. Bir beden izi yazılsın: `her forearms dip a few centimeters as the casing's weight comes onto the cradle`.

### B18 · KÜÇÜK · 10 s'lik vuruş planı doğrulanmamış süreye dayanıyor; G07 EKLE satırı modu kaydırabilir
KANIT
- FILM.md künye `KLIP_SURESI ölçülmedi`.
- FLOW_GERCEKLERI §1: Frames to Video Veo 4·6·8 s; Omni "var, yalnız Flow web · süre ?".
- G05 İş emri "Gemini görselden video 10 s", G07 "Gemini Omni 1.1 Flash 10 s".
- Kritik olay son 2 saniyede olan klipler: C70 (8-10), C74 (7-10), C84 (8-10), C85 (7-10), C91 (7-10).
- G07 EKLE: `başlangıç karesi: kare/C73.png · referans (yükleme sırası): ref/2.RHEA_v1.png …`. G07'nin kendi başlığına göre referans eklenirse mod Ingredients'e kayar.

NEDEN: Süre 8 s çıkarsa son vuruştaki olaylar kesilir. EKLE satırı yanlış yüklemeye açık.

ARIZA: yeni (mod ↔ model)

ÖNERİ
- G07 EKLE satırlarını G05, G06 ve G08'deki gibi KARE/VİDEO diye ikiye böl.
- İlk F7'de zaten önizleme olan C74 ve C84 ile süreyi ölç. 8 s çıkarsa kritik olayları 0-6 s'e al.

### B19 · KÜÇÜK · FILM.md §3 "Kullanan çekimler" gerçek EKLE ile örtüşmüyor
KANIT
- §3 10.CEKIRDEK C53 · C55 · C56 · C78 · C79 · C86 · C95'i listeliyor.
- §3 15.ARACLAR C50 · C55 · C79 · C86 · C95'i listeliyor.
- §3 5.FOUNDRY ve 6.ARK C86'yı, 5.FOUNDRY C93'ü listeliyor.
- G05, G07 ve G08 bunları çıkarmış.

NEDEN: "Referans değişirse kullanan çekimlerin kareleri yeniden üretilir" kuralı bayat listeye dayanıyor.

ARIZA: yeni

ÖNERİ: §3 ve §4 Referans sütunlarını gerçek EKLE'ye çek.

KORU: Telsiz repliklerde konuşanın yüzü hiçbir klipte kadrajda değil (C49 arkadan; C51 · C56 · C60 · C65 · C67 · C71 yalnız eldiven; C52 · C57 · C61 · C62 · C66 · C69 · C72 kimse yok). İki konuşanlı klipte `while his mouth stays closed` ve farklı ses tarifi var (C86 · C88 · C93 · C95 · C96). Ortam ses cümlesi mekân başına birebir (KOKPİT 7 · KOMUTA 9 · KONTROL 14 · İSKELE 2). C74 · C80 · C84 · C85 · C87 · C89 · C91 · C92'de kamera kilitli. Replikler R52–R95 için FILM.md §5 ile birebir.

KAPSAM DIŞI: C65 · C67 · C71 aynı çerçevede aynı kol çekişini üç kez yapıyor (H01, dramaturg). C86'da Rhea'nın iskeleden kokpite kesmeyle geçişi ve tether'in nerede ayrıldığı ekranda yok (devamlılık).

```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 8 · KÜÇÜK 11
KARAR    TUR KAPANABİLİR
GİRDİ    /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/PROMPTLAR/G05.md · G06.md · G07.md · G08.md (tam)
         PROMPTLAR/G01.md (satır 1–176: başlık + REFERANS PROMPTLARI) + yalnız arama için G01 C01–C12 satırları, G02–G04 satırları
         FILM.md §3 §4 §5 (satır 157–465)
         /Users/dai/github/apex_md/film_md/uretim_hatti/ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md · ARIZA_LISTESI.md · ILK_30_SANIYE_KILAVUZU.md · FLOW_GERCEKLERI.md · PROMPT_HATA_ATLASI.md · GECIS_VE_SES_SUREKLILIGI.md · GOSTERIM_COZUMLERI.md (satır 1–140)
         EKSİK: yok (açılamayan dosya olmadı; açılmayanlar başta yazılı)
YAPILMADI  ≤4.300 karakter sayımı (araç yok; göz kararı 2.000–3.400). Kare ve video üretilmedi, bütün riskler kâğıt üzerinde. SMOKE P9/P17/P18 açılmadı. Açılış C01–C03 bu görevin kapsamında değil.
```
