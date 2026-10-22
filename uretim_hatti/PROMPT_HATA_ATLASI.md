# PROMPT HATA ATLASI — örnek kataloğu

> **Tarih:** 07.10.2026 · **Kaynak:** `ARASTIRMA/qa_prompt_analizi_20261006/` (12 film · 698 tekil 🔴/🟠 bulgu; her biri prompt alıntısı ve hükümle). Dış kaynak yalnız `ARASTIRMA/04_SUZME_20261007.md` R6'nın KABUL satırları (birebir cümle ve URL: §F).
> **Ne için:** ekranda görülen kusurun promptun hangi kalıbından doğduğunu gerçek örnekle göstermek. Yazara "bunu yazma, şunu yaz"; denetçiye kök neden ve kanıt.
> **Kim okur:** `goruntu-yonetmeni` yazarken · `devamlilik` ve `teknik-danisman` denetlerken · planlanan rapor-prompt karşılaştırma skill'i (AGENTS §7, ⑬ UYUM'un işi).
> **Ne değildir:** kural listesi, kapı ya da kontrol listesi değildir. Yeni zorunluluk getirmez, yeni kapı açmaz (AGENTS §1 ④) ve regex'le denetlenmez. `BILINEN_TUZAKLAR.md` ile `ARIZA_LISTESI.md`'yi tekrarlamaz; aynı konuda oraya bağlanır.

**Okuma.** Hüküm sınıfları `GOREV.md`'den gelir: 🅐 model sapması (prompt önlüyordu, tutmadı) · 🅑 boşluk (gerekli cümle o promptta yoktu) · 🅑+ davet (prompt kusuru kendisi çağırdı) · 🅒 QA yanıldı · 🅓 eşlenemedi.
- 🅑 "cümle yoktu" demektir, "eklenseydi düzelirdi" demek değildir: aynı cümle başka klipte yazılıyken 🅐 çıktı (A02 · A03 · A14). En güvenilir girdiler 🅑+ olanlardır, çünkü çıkarılacak bir sözcüğü gösterirler.
- Örneklerin çoğu mod V ya da geçersiz rapordan gelir; 🔴/🟠 satırların %56'sı böyle. Rapor alanındaki etiket bunu söyler. Denetçi böyle bir bulguda önce 🅒 olasılığına bakar (`QA_OKUMA_KILAVUZU.md` §4).

**Kanıt eşiği:** girdi, iki ayrı filmde kayıtlı vaka ister (AGENTS §1 ④). Tek filmde görülen kalıp §KARANTİNA'da tek satır olarak durur; ikinci film gelince sahibe sorularak girdiye çıkar.
**Emeklilik:** girdi bugünkü üretim modeline aittir. Model değişince kalıp yeniden sınanır ve sınanana kadar KARANTİNA'ya iner. Analizde model sürümü kayıtlı değil: GUNES_MEZARI · BRITTLE_EDGE · INWARD_FALL'ın üretim defteri boş.
**Birleştirme:** iki girdi aynı kök nedene inerse birleşir; örnekleri korunur. KANIT satırlarında film adları `THE_` öneksiz yazılır.

## Girdi şablonu
```text
### Ann · kalıbın kısa adı — tür (OZET_topla sayısı) · baskın hüküm
- KALIP: promptta yazılan şey, birebir biçimiyle
- BELİRTİ: ekranda ya da QA raporunda görülen
- KÖK NEDEN: model bu metni neden böyle okuyor
- GERÇEK ÖRNEK: FİLM · sahne/klip · rapor (mercek, geçerlilik) · zaman · "promptun birebir alıntısı" → şiddet · hüküm
- DÜZELTME (bunu yaz): ✗ yazılmayan → ✓ yazılan
- DOĞRULANDIĞI KANIT: hangi filmlerde kayıtlı · düzeltme sınandı mı
- KİM YAKALAR: film_dogrula M · devamlilik · teknik-danisman · yalnız insan
```

## Girdiler (14)

### A01 · Sabitlik sözcüğü eforu siler — efor/beden · 🅑+
- **KALIP:** yük taşıyan eylemde `smoothly` · `stable cadence` · `at the same rate` · `does not change` · `without friction` · `minimal recoil`.
- **BELİRTİ:** ağır iş kolay ve hızı değişmeden yapılır; ⑧ EFOR "beden bedel ödemiyor" der.
- **KÖK NEDEN:** model istenen sabitliği verir. Prompt, yükün bedelini kendi sözcüğüyle siler.
- **GERÇEK ÖRNEK:** THE_INWARD_FALL · K11 · ⑧ EFOR (geçerli) · — · "his hands advance smoothly to the next rung, establishing a stable upward cadence" → 🔴 🅑+ (tutuş kaybı silindi).
- **DÜZELTME:** ✗ yük altındaki bedende sabitlik ya da kolaylık sözcüğü → ✓ sabitlik yalnız kamerayı ya da yük taşımayan şeyi niteler; bedende yükün tek görünür izi yazılır (A02).
- **DOĞRULANDIĞI KANIT:** 6 film: INWARD_FALL K11 · STATIC_VEIL S10 `without friction, moving smoothly` · STILL_POINT S12 `absorbs minimal recoil` · LAST_TOW K04 `at the same rate`, K05 `her stride does not change` · GUNES_MEZARI K05 `the same walking cadence for the whole clip` · SLOW_RAIN S17-S19 `at the same rate through the last second` (27 video). Düzeltme sınanmadı.
- **KİM YAKALAR:** teknik-danisman (faz 5, T02) · yalnız insan (klipte).

### A02 · Efor ya yazılmamış ya kadrajda görünmüyor — efor/beden 126 satır (🔴 90) · 11 film · 🅑 63
- **KALIP:** ağır iş yalnız zarfla anlatılır (`forcefully` · `firmly` · `full arm strength`) ya da hiç anlatılmaz; kadraj `IN FRAME: hands`.
- **BELİRTİ:** ağırlık, direnç ve yorgunluk okunmuyor. 12 filmin en kalabalık türü bu.
- **KÖK NEDEN:** model eforu yalnız görünen bedenden okur. Zarf bir şey göstermez; kadrajda yalnız el varsa omuz ve nefes görünmez.
- **GERÇEK ÖRNEK:** THE_STATIC_VEIL · S04 · ⑧ EFOR (geçerli, mod D) · — · "twists the beacon forcefully" · "lowers their head in frustration" → 🔴 🅑 (omuz desteği ve hız düşüşü yok).
- **DÜZELTME:** ✗ `twists … forcefully` → ✓ efor kadraja sığar: omuz ve gövde kadrajda, çekim kısa, tek büyük beden hareketi (ARIZA T02). Yazılacaksa tek oran cümlesi yazılır (COUNTED_RIVET: `stops dead for a full second`). Kadrajda yalnız el varsa efor yazılmaz, çekim listesi değişir.
- **DOĞRULANDIĞI KANIT:** sonuç karışık. Lehte (korelasyon): COUNTED_RIVET oran cümlesi 11/24 → ⑧ 0 satır · SLOW_RAIN 7/48 → 0 ↔ STATIC_VEIL 0/12 → 12 satır; GUNES_MEZARI K14 `IN FRAME: hands` → kapanma kadraj kararı. Aleyhte: cümle yazılıyken de 🅐 çıktı (LAST_GATE K15 K19 K83 K89 · STOLEN_SKY S66 S79 · INWARD_FALL K04 K06 · STILL_POINT S08). Mod V'deki ⑧ 1g varsayar: STILL_POINT'te ⑧'in 8 🔴'sinin 5'i 🅒.
- **KİM YAKALAR:** teknik-danisman (faz 3, T02: zor beden hareketi kısa ve bölünmüş mü) · yalnız insan.

### A03 · Temas cümlesi yazılı, el yine kaynaşıyor — el-nesne kaynaşması 43 satır (🔴 18) · 9 film · 🅐 29
- **KALIP:** `Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.` Temas anı kadrajın içinde, videonun ortasında.
- **BELİRTİ:** parmak tokaya erir, eldiven kola ya da ekrana girer, fazla parmak çıkar.
- **KÖK NEDEN:** model temas anını çözemiyor ve cümle bunu değiştirmiyor. Cümle yalnız eli kapsıyor; kayış ↔ toka, halat ↔ halka gibi nesne-nesne teması kapsam dışı.
- **GERÇEK ÖRNEK:** THE_LISTENING_WORLD · S8 · ① KARE (geçerli) · 1:24 · "Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers." → 🟠 🅐 (el buzla kaynaştı).
- **DÜZELTME:** ✗ temas cümlesini uzatmak, tek makroda birden çok el → ✓ temas başlangıç karesinde zaten kurulu olur, video temastan sonrasını ister; temas anı kesmeyle atlanır ya da kadraj dışında kalır (BILINEN_TUZAKLAR §B sıra 1 · ARIZA T01).
- **DOĞRULANDIĞI KANIT:** 04 R9 KABUL: "temas cümlesini ayrıntılandırmak kaynaşmayı önlemez" (depo ölçümü). Cümle yazılıyken çıktı: LAST_GATE 8 satır (K89 🔴 "kol avuçtan geçti") · STOLEN_SKY 15 · SLOW_RAIN S15 🔴 · COUNTED_RIVET K01 · BRITTLE_EDGE S06. Cümle şablondan düştüğü klipte de çıktı (LAST_GATE K28 K51 K78 · STOLEN_SKY S09): cümle kusuru belirlemiyor.
- **KİM YAKALAR:** teknik-danisman (faz 3, T01; sahneleme deltası) · yalnız insan (kare ve klip).

### A04 · İki katı cisim birleşiyor, ayak zemine geçiyor — zemine geçme 21 satır (🔴 15) · 3 film · 🅑 14 · 🅑+ 5
- **KALIP:** iki nesnenin birleşmesini ya da birinin ötekinin altına veya içinden geçmesini istemek; ya da ayak-zemin, gövde-çerçeve sınırını hiç yazmamak.
- **BELİRTİ:** kalkanlar kaynaşır, kanat gövdeye girer, bot rampada kayar ya da zemine gömülür, bacak geriye bükülür.
- **KÖK NEDEN:** prompt birleşmeyi bizzat istiyor (🅑+) ya da bacak ve gövde temasını hiç tanımlamıyor (🅑). Temas cümlesi yalnız eli kapsıyor.
- **GERÇEK ÖRNEK:** THE_STOLEN_SKY · S48 · ① KARE (TEKRAR, mod V) · — · "the two shields swing together and lock edge to edge into one wider curve" → 🔴 🅑+ (S40'ta aynı kalıp, 🔴).
- **DÜZELTME:** ✗ `lock edge to edge into one wider curve` · `one wing folding under her` · sert çizgili kapıdan `steps through` → ✓ iki nesne ayrı kalır, yalnız kenarları değer; geniş beden-zemin teması kısa tutulur ya da bölünür (BILINEN_TUZAKLAR §B sıra 10).
- **DOĞRULANDIĞI KANIT:** 3 film: STOLEN_SKY 17 satır (S20 `walks at the ramp` 🔴 · S32 · S55 · S60 · S61 · S75: ayak sınırı yazılı değil) · SLOW_RAIN S13 🔴 🅑+ · S27 🔴 `boots dug in` · LAST_GATE K66 🔴 `She never rises or falls` · K85 🟠. Düzeltme sınanmadı.
- **KİM YAKALAR:** teknik-danisman (T01 · T10) · yalnız insan.

### A05 · Aynı promptta birbirini yalanlayan iki istek — 12 filmin hepsinde "kendi kusurları" listesinde · 🅑+
- **KALIP:** aynı blokta zıt iki ifade: ışık konisi + "saçılma yok" · tek kaynak + ikinci bir konum · `locked-off tripod` + hızlanan araç · başka sahneden kopya kamera + bu sahnenin eylemi.
- **BELİRTİ:** model birini seçer ya da ikisini karıştırır: vakumda pus konisi, kaynaksız ışık, istenmeyen kurulum, kamera kayması.
- **KÖK NEDEN:** motor iki isteği birden yerine getiremez ve hangisinin kazanacağı belirsizdir.
- **GERÇEK ÖRNEK:** THE_STATIC_VEIL · S11 · ⑪ IŞIK (geçerli, mod D) · — · "a powerful, concentrated amber beam that projects a razor-sharp conical light path across the dark basalt crater floor with zero atmospheric scattering" → 🔴 🅑+ (hacimsel pus).
- **DÜZELTME:** ✗ zıt iki istek → ✓ çelişki tasarımla çözülür: vakumda koni yerine ışığın düştüğü yüzey; tek kaynak yazıldıysa ikinci kaynak yok; araçtaki kamera araca bağlanır (`it moves only as the craft moves`); kamera cümlesi o çekimin kendi eyleminden yazılır.
- **DOĞRULANDIĞI KANIT:** bulguya bağlı 🅑+ 6 filmde: STATIC_VEIL S11 · S03 S07 (kamera kaskta, eylem kalçada) · GUNES_MEZARI K09 (lamba hem yerde hem göğüs hizasında) · STOLEN_SKY S54 🔴 (kâğıt planda yanan simge) · STILL_POINT S09 S11 (hareketli araçta tripod) · INWARD_FALL K12 K18 K19 🔴 (yakın plan ↔ 15 m derinlik; başka mekândan kopya kamera) · SIGNAL_KEEPERS K11 (A11). STOLEN_SKY S26'da `it moves only as the craft moves` yazılıydı; QA kameranın araçla gitmesini kusur saydı, hüküm 🅒. Mekanik sayım (50 film): "deri yok" ↔ `real skin pores` 784 prompt, ekran ↔ metin yasağı 265 prompt; bunlara bağlanmış 🔴/🟠 bulgu yok.
- **KİM YAKALAR:** devamlilik (Çelişki maddesi) · teknik-danisman. `film_dogrula` yalnız "insan yok + kişi" çiftini yakalar (A08).

### A06 · Görsel ile video aynı anı anlatmıyor — görsel işin sonunu ya da başka bir tutuşu gösteriyor · 🅑+
- **KALIP:** IMAGE eylemin bitmiş hâlini (`rests … on the level terrace` · `floats free`) ya da başka bir fiili (`grips`) tarif eder; VIDEO öncesini ya da başka bir eylemi ister (`crest the terrace lip` · `push hard` · `taps`).
- **BELİRTİ:** eylem atlanır ya da geri sarılır ("kurtarma çekimi atlanmış"); el kumandaya karışır; figür havada asılı kalır.
- **KÖK NEDEN:** görselden videoda başlangıç karesi olayı çoktan yaşamıştır. Video karede olmayan bir durum ya da nesne isteyince model onu ya ekler ya da kayar.
- **GERÇEK ÖRNEK:** THE_BRITTLE_EDGE · S10 · ⑦ AKSİYON (mod V) · — · IMAGE "rests securely on the level regolit terrace" ↔ VIDEO "rear wheels crest the terrace lip" → 🔴 🅑+.
- **DÜZELTME:** kural goruntu-yonetmeni §Görsel prompt'ta: kare hareketin başındaki durağan anı gösterir. ✓ görseldeki tutuş fiili videonun ilk fiiliyle aynı olur; ✗ video karede olmayan nesne istemez (INWARD_FALL K04 `both hands resting lightly on the side safety cables`; karede kablo yok).
- **DOĞRULANDIĞI KANIT:** 5 film: BRITTLE_EDGE S10 (planın D179 kuralı yazılıyken çiğnendi) · STILL_POINT S15 🔴 · S12 🟠 · S08 🟠 · LISTENING_WORLD S5 🟠 (0:54, kavrar ↔ dokunur) · INWARD_FALL K04 🔴 · SLOW_RAIN S1 🔴 (`gliding level` ↔ `losing height slowly`). Dış kaynak: Vertex G10 · Runway V1c (aşağıda). Düzeltme üretimde sınanmadı.
- **KİM YAKALAR:** devamlilik (faz 5, görsel ↔ video, ÖLÜMCÜL adayı).

### A07 · Tutanı olmayan nesne, gövdesiz el — 🅑+
- **KALIP:** nesne için `held above it`, el için `hangs … above` denir ama tutan ya da kol yazılmaz; `IN FRAME: hands` kadrajında kolun girdiği kenar yok.
- **BELİRTİ:** havada asılı küre ya da eldiven, "hayali kavrama", masada çıkarılmış eldivenler.
- **KÖK NEDEN:** model yazılmayan bağlantıyı kurmaz; nesneyi ya askıda bırakır ya bağımsız parça olarak çizer.
- **GERÇEK ÖRNEK:** THE_SIGNAL_KEEPERS · K23 · ⑭ HAREKET (geçerli) · — · "the sphere is clear of the seat and held above it, and the fingertips come off the ring" → 🔴 🅑+ (el boşluğu kavradı).
- **DÜZELTME:** kural goruntu-yonetmeni §Görsel prompt'ta (tutan kadrajdadır; yalnız eller görünüyorsa kolun hangi kenardan girdiği yazılır). ✗ `held above it` → ✓ tutan el ve kolun girdiği kenar aynı cümlede.
- **DOĞRULANDIĞI KANIT:** 2 film: SIGNAL_KEEPERS K23 · STOLEN_SKY S82 🔴 (3 mercek) `The cobalt glove hangs a finger above the centred T-handle` · S54 🟠 `looking down at three pairs of gloves`. STOLEN_SKY'de `IN FRAME: hands` olan 17 klibin hiçbirinde kol-gövde bağı yazılı değil. Düzeltme sınanmadı.
- **KİM YAKALAR:** devamlilik (Tutan ve bağlantı).

### A08 · "İnsan yok" kadrajında kişi göndermesi — 🅑 · 🅑+
- **KALIP:** aynı promptta `IN FRAME: none` ya da `No human figures in frame.`, yanında `her` · `the astronaut` · `Exactly one human character` · `breathing inside the helmet` ya da sahibi belirsiz bir `fingertip`.
- **BELİRTİ:** insansız planlanan kareye kişi girer; kime ait olduğu belirsiz parmak görünür.
- **KÖK NEDEN:** zamir, kişi sayısı ve nefes bir beden çağırır; model "insan yok"u değil, bedeni çizer.
- **GERÇEK ÖRNEK:** THE_STATIC_VEIL · S0 · ⑭ HAREKET (M1) + ⑫ HOOK (geçerli) · 0:07-0:09 · görsel "No human figures in frame." ↔ NEGATIVE "Exactly one human character, no duplicates, no second person." → astronot insansız hook karesine girdi (tabloda şiddet yazılı değil).
- **DÜZELTME:** ✗ insansız klipte zamir, kişi sayısı, nefes, kask sesi → ✓ mesafe ve ışık bir nesneye göre yazılır; ses yalnız nesnenin ya da ortamın sesidir.
- **DOĞRULANDIĞI KANIT:** bulgulu 2 film: STATIC_VEIL S0 · SIGNAL_KEEPERS K10 🟠 🅑 (`IN FRAME: none` + "one narrow fingertip comes across and taps the piece once"). Aynı kalıp, bulgusuz: BRITTLE_EDGE S00 · LAST_TOW K01 K02 K31 K33 K37 (`camera 2.4 m from her`) · GUNES_MEZARI K24 `One slow breath off frame` · STOLEN_SKY'de 19 insansız klipte kask nefesi.
- **KİM YAKALAR:** `film_dogrula` M (`INSANSIZ` + `KISI`; `IN FRAME:` etiketi `META`) · devamlilik (sahipsiz parmağı M yakalamaz).

### A09 · Sahne numarası, başka çekime atıf, film geneli ifade — meta sayaç 37/50 film · 1.595 prompt
- **KALIP:** `Scene 60 of 96.` · `Clip 13 of 48.` · `— the same position, height and lens as Scene 7` · `continues the previous clip from its exact last frame` · `for the whole film`.
- **BELİRTİ:** yanlış kurulum gelir (objektif, mesafe); kafiye çifti kırılır. Eski bir vakada sahne kodu kadraja basıldı (BILINEN_TUZAKLAR §C, `S04`).
- **KÖK NEDEN:** model yalnız bu promptu görür; atıf ya boşa düşer ya da tahmin ettirir. Dört filmde etiket 1'den, atıf 0'dan sayıyor, yani atıf başka bir klibi gösteriyor.
- **GERÇEK ÖRNEK:** THE_STATIC_VEIL · S08 · ⑨ KADRAJ (geçerli) · — · "continues the previous clip from its exact last frame — the same position, height and lens as Scene 7" → 🟠 🅑+ ("Scene 7" etiketi S6'nın; S6'nın 50 mm kurulumu geldi, S08 85 mm'ydi).
- **DÜZELTME:** kural goruntu-yonetmeni §Her promptta YOK'ta. ✓ objektif, mesafe, yükseklik ve açı o promptta tam yazılır; kare bağlantısı kod bloğunun dışındaki EKLE satırında durur.
- **DOĞRULANDIĞI KANIT:** atıf yanlış kurulumu çağırdı: STATIC_VEIL S08 · INWARD_FALL K17 🔴 🅑+ (`Tight canted view …` ↔ "Clip 9 ile aynı" orta plan). Kayık numara: BRITTLE_EDGE (`as Scene 0` diye bir etiket yok) · STATIC_VEIL · LISTENING_WORLD · STILL_POINT. Bu 12 filmde etiketin kadraja basıldığı kayıt yok; basılma kanıtı eski filmlerden.
- **KİM YAKALAR:** `film_dogrula` M (`META` · `SIRA_NO` · `ATIF` · `FILM_GENELI` · `ZINCIR_DIL`) · devamlilik (aynı kurulum iki promptta tam ve aynı yazılmış mı).

### A10 · Konuşma çağrıştıran ses betimi — ses / konuşma · 🅑+
- **KALIP:** AUDIO'da `names her sister` · `a radio channel opening on static` · `A targeting advisory on the radio` · `a command voice`, yanında `No dialogue in this shot.`
- **BELİRTİ:** promptta olmayan replik, filmde olmayan ad; AUDIO cümlesinin kendisi seslendirilir.
- **KÖK NEDEN:** model betimi seslendirir; "No dialogue" bunu durdurmuyor.
- **GERÇEK ÖRNEK:** THE_LAST_GATE · K18 · PART1'in 13 içerikli raporundan 9'u (mod V) · — · "one word spoken close inside the helmet — the pilot names her sister and nothing more is said. No dialogue in this shot." → raporlar "Elena." duydu; filmde böyle bir ad yok (Lina).
- **DÜZELTME:** ✗ konuşma, telsiz ya da duyuru betimi → ✓ AUDIO yalnız ortam ve temas sesini yazar; söylenecek replik varsa betim değil **metnin kendisi** birebir yazılır (21.10.2026: diyalog kurguda eklenmez, replik model sesiyle — `REPLIK_VE_KLIP_SESI` §3). Eski filmde replik kurguda eklenir. Ağız kadrajdaki replik istisnası goruntu-yonetmeni'de (`she says, "<line>"`; tırnak ↔ iki nokta sorusu PROB, SMOKE P9). Görsel prompta ses cümlesi girmez (GUNES_MEZARI K03 K10 IMAGE).
- **DOĞRULANDIĞI KANIT:** 2 film: LAST_GATE K18 · K56 · K57 · K87 (`Withdrawal advisory on enemy channel.` cümlesinin kendisi duyuldu) · STOLEN_SKY S61 🟠 🅑+ · S10 (01:47 "Roger, system secure") · S83: dört `radio channel` klibinin üçünde konuşma üretildi. Karşı not: LAST_TOW'da konuşma betimi yokken ve `No dialogue` 48/48 klipte yazılıyken de replik duyuldu (1:18 · 3:01, 7 rapor); kapanma her durumda KURGU, model sesi atılır (AGENTS §2).
- **KİM YAKALAR:** `film_dogrula` M kısmen (`KONUSMA`: `spoken` · `names her` · `voice` yakalanır; `radio channel` · `advisory` · `order` yakalanmaz) · devamlilik · yalnız insan (sesli izleme).

### A11 · Tekrarlanan ayırt edici sözcük yazıya dönüşüyor — istenmeyen yazı 10 satır (🔴 8) · 7 film
- **KALIP:** kumanda belirsiz anılır (`a control detail`) ve kök sözcük tekrarlanır: `release` K30'da 6, filmde 132 kez; `selector` 10, `T-handle` 28 kez.
- **BELİRTİ:** konsol ve panelde `SUIT RELEASE` · `EXTRA RELEASE` · `500` · `SELECTOR` yazısı.
- **KÖK NEDEN:** çok tekrarlanan kısa sözcük büyük harfli etiket gibi davranır; "büyük harfli jeton yok" kuralı küçük harfli tekrarı kapsamıyor.
- **GERÇEK ÖRNEK:** THE_LAST_GATE · K30 · ① KARE + ⑤ ARKA PLAN (mod V) · — · "A gloved hand confirms on a control detail ... releases the berth" → 🔴 🅑.
- **DÜZELTME:** kural BILINEN_TUZAKLAR §C'de (ayırt edici sözcük her seferinde bir nesneye bağlanır, büyük harfli etiket yok). ✓ kumanda bir kez somut nesne olarak tarif edilir, kök sözcük tekrarlanmaz; okunacak gösterge isteniyorsa yazısız tasarlanır (§B sıra 2).
- **DOĞRULANDIĞI KANIT:** 2 film: LAST_GATE K30 · STOLEN_SKY S81/S84 🟠 🅑+ ⑤ (geçerli) `A T-handle selector stands centred`. Aynı filmlerde büyük harfli `CGI` ve `Clip n of N` basılmadı. Yasak 96/96 klipte yazılıyken de yazı çıktı: LAST_TOW K07 rün · K36 `58 1 (U)` (🅐). Vizöre ışık deseni + "yansıma yok" isteği: SIGNAL_KEEPERS K11 🔴 1:47 HUD (🅑+).
- **KİM YAKALAR:** teknik-danisman (T06 · §C) · yalnız insan (sözcük tekrarını sayan bir araç yok).

### A12 · PHYSICS şablonu tozu bizzat tarif ediyor — parçacık/duman/toz 38 satır (🔴 14) · 8 film
- **KALIP:** PHYSICS'te `Dust lifts and never settles` (BRITTLE_EDGE 24/24) ya da `Lifted dust rises in a flat arc and lands without settling again` (LAST_TOW 48/48); aynı promptta `never hovering` ya da `No dust … hanging in the air`.
- **BELİRTİ:** vakumda asılı toz, temasta toz bulutu, havada duran kıvılcım.
- **KÖK NEDEN:** model yazılan toz davranışını çizer; yasak cümlesiyle çelişki bu yüzden 🅑+'dır.
- **GERÇEK ÖRNEK:** THE_BRITTLE_EDGE · S00 · ① KARE (geçerli, mod D) · 0:06 · "PHYSICS: Gravity is 0.16 g in hard vacuum. Dust lifts and never settles" ↔ NEG "no airborne smoke clouds" → 🔴 🅑+.
- **DÜZELTME:** ✗ PHYSICS satırında toz ya da parçacık davranışı → ✓ hiç yazılmaz; toz kaldıran eylem filmin taşıyıcı anı olmaz (BILINEN_TUZAKLAR §B sıra 4). "Doğal sonucunu yaz" önerisi çürütüldü (§Çürütülenler).
- **DOĞRULANDIĞI KANIT:** 2 filmde şablon düzeyinde: BRITTLE_EDGE tek cümle → 4 satır · LAST_TOW K15 K25 K34 🔴 🅑+ (K25 geçerli). Cümle `PROMPT_HATA_ONLEME_KILAVUZU` §3.1 vakum şablonunda da var (BRITTLE_EDGE analizi). Yasak yazılıyken de toz çıktı: LAST_TOW K21 K32 · LISTENING_WORLD S0 (🅐). Kesici klibinde yasak cümlesi yoktu: LAST_TOW K04 K13 🔴 🅑.
- **KİM YAKALAR:** devamlilik (Çelişki: "toz kalkar ve hiç inmez" + "havada asılı kalmaz") · teknik-danisman (T03).

### A13 · Harita promptta yok: ışığın ve sabit nesnenin ekran tarafı — ışık 64 (🔴 24) · yön/180° 19 (🔴 10)
- **KALIP:** ışık tarafsız yazılır (`Harsh low-angle lunar sunlight` · `Low-angle solar illumination glints off …`); uçurumun, pilonun, terasın tarafı yazılmaz ya da karaktere göre yazılır (`at her left`).
- **BELİRTİ:** kesmede anahtar ışık saat 10'dan 2'ye döner; kafiye aynalanır; teras taraf değiştirir.
- **KÖK NEDEN:** harita yalnız planda duruyor; model tarafı her klipte yeniden seçer.
- **GERÇEK ÖRNEK:** THE_BRITTLE_EDGE · S02 · ⑪ IŞIK (geçerli, mod D) · — · "Low-angle solar illumination glints off the crystalline facets" → 🔴 🅑 (anahtar ışık 10→2).
- **DÜZELTME:** ✓ anahtar ışığın tarafı ve sabit nesnenin ekran tarafı her promptta aynı kelimelerle yazılır (goruntu-yonetmeni §Görsel prompt; devamlilik "Taraf ve yön"). `from screen left` kameraya göreli bir ifadedir: kamera tarafı değişirse yazı da değişir.
- **DOĞRULANDIĞI KANIT:** 2 film: BRITTLE_EDGE (önlenebilir 15 bulgunun 8'i bu iki eksik bilgiden) · STATIC_VEIL S11 🔴 🅑+ (`On screen-right, the astronaut …`; pilonun tarafı 12 promptun hiçbirinde yok) + S05 S10 ışık 🅑. Aleyhte: taraf yazılıyken de sıçradı (LAST_TOW K10 9→3; LAST_GATE'te ışık satırlarının 8/12'si 🅐). Işık yönü saat kadranıyla 12 filmin hiçbirinde yazılmadı; etkisi ölçülmedi.
- **KİM YAKALAR:** devamlilik (taraf, yön, ışık tutarlılığı) · yalnız insan (kesmedeki sıçrama klipte görülür).

### A14 · Olumsuz cümle ve şişkin NEGATIVE bloğu — NEGATIVE promptun ortanca %40,5'i (50 film, 2.913 prompt)
- **KALIP:** her sahneye kopyalanan 7-9 çekirdek cümle (`0% bloom, no glow, no soft focus` · `no watermark` · `no engine sound from outside`), çoğu zaman istenen parlaklığın ya da sesin hemen yanında.
- **BELİRTİ:** yazılı yasağa rağmen bloom, vakumda ses, toz, filigran. Sahneye özel cümle yalnız 1-3.
- **KÖK NEDEN:** olumsuz cümle istenmeyeni durdurmuyor, dış kaynaklar ters etki de bildiriyor. Kısaltılan blok bazen sahneye özel kilidi de götürüyor.
- **GERÇEK ÖRNEK:** THE_LAST_GATE · K53 · ⑪ IŞIK (mod V) · — · "0% bloom, no glow ... nothing blooms" → 🔴 🅐 (vakumda huzme ve parıltı).
- **DÜZELTME:** ✗ olumsuz blok ya da "no X ekle" önerisi → ✓ blok yazılmaz (yeni hatta `NEGATIVE:` etiketi M ile yakalanır). İstenmeyeni çağıran pozitif sözcük çıkarılır (`beam` · `hovering` · `flashes` · `bright edges` · `radio channel`); istenen pozitif yazılır: "kamera sarsıntısı yok" → "sabit kamera" (04 R6).
- **DOĞRULANDIĞI KANIT:** yasak yazılıyken aynı kusur (🅐): bloom 6 filmde (LAST_GATE · STOLEN_SKY · SLOW_RAIN · GUNES_MEZARI · LISTENING_WORLD · LAST_TOW), vakum sesi LAST_GATE K31 K32 K53'te, filigran 7 filmde. Ters etki depoda ayrıştırılmadı; dışta Runway V1a ve Luma V2a KABUL, Veo için PROB (SMOKE P13). Kısa insansız blok kilidi düşürdü (GUNES_MEZARI K02 · SIGNAL_KEEPERS K07, 🅑) ama aynı kilit yazılıyken de kusur çıktı (LAST_GATE K26 🔴 · LISTENING_WORLD S6, 🅐). Uzunluk: §Ölçüm notu.
- **KİM YAKALAR:** `film_dogrula` M (`NEGATIVE:` etiketi `META`'da; 4.300 karakter tavanı) · teknik-danisman ("no X ekle" önerisi yasak).

## KARANTİNA — tek filmde kayıtlı (ikinci film gelirse girdiye çıkar)
- 3-4-3 saniyelik TIMELINE iskeleti ve "hold" bitişi → tempo düzlüğü · LAST_GATE 87/92 klip · ⑩ 🔴 🅑+.
- `The two figures keep separate halves of the frame` / `In one two-sided frame` → bölünmüş ekran · LAST_GATE K65 🔴 · K34 🔴 · 🅑+.
- Kalabalığa tek "aynı giysi" cümlesi + tek sıra → klon yürüyüş · LAST_GATE K37 🟠 · K58 🔴 · 🅑+.
- Kişi sayısı çelişkisi `Exactly 3 human characters in suits, and exactly one tall figure` → fazla kişi · LAST_GATE K35/K36 🟠 🅑+.
- Mikrogravitede 1g deyimi (`holds his ground` · `stands alone`) → zemine basan figür · LAST_GATE K15 🔴 🅑+ · K73 🔴 🅑.
- Tek makroda üç çift eldiven → fazla parmak riski · LAST_GATE K86 🔴 🅑+.
- `IN FRAME: hands · torso` kırpması kask cümlesini düşürdü, kadraj genişleyince kask kayboldu · GUNES_MEZARI K13 🔴 ×2 🅑 (ikinci vaka belirsiz: LAST_GATE K85 🟠).
- Zihinsel ifade (`contemplates the permanent loss of life telemetry`) → karar okunmuyor · STATIC_VEIL S08 ⑫ 🟠 🅑. M yalnız çekim listesinde yakalar (`ZIHINSEL`).
- PHYSICS satırındaki sayı sesli okundu (`3.1 bar`) · SIGNAL_KEEPERS K19 3:00-3:12 (🔴/🟠 yok).

## Dış kaynak — yalnız 04 süzmesinin KABUL satırları (birebir cümle ve URL: 04 §F)
- **Vertex · "Prompt for motion only" (G10):** "Not recommended : Re-describe the character, the background, or the lighting depicted in the image. Redundant prompts confuse the model and lead to poor results." docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice · Runway desteği (V1c): "Reiterating elements that exist within the image in high detail can lead to reduced motion or unexpected results in the output." → A06; goruntu-yonetmeni §Video prompt zaten böyle yazıyor.
- **Runway · olumsuz ifade (V1a):** "Negative phrasing is not supported and may produce unpredictable or even opposite results." help.runwayml.com Gen-4 Video Prompting Guide (30.07.2026) → A14.
- **Luma (V2a):** "Ray is a "positive only" model. Negative prompting is counterproductive." lumalabs.ai learning-hub (27.02.2026) → A14.
- **Sora (V4a · V4b):** "Treat each shot as a creative unit" · "Shorter prompts give the model more creative freedom." · "Longer, more detailed prompts restrict the model's creativity." developers.openai.com/cookbook …/sora2_prompting_guide → A09 · §Ölçüm notu.
- Veo için olumsuz ifadenin etkisi resmî belgede bulunmadı: **PROB**, SMOKE P13 (`no dust in the air` ↔ `the air is perfectly clear`).

## Çürütülenler — yazılmaz, kaynak gösterilmez
- "Runway: then / next / after that kullanma": RED (V1b ❌). Rehberin doğru örneği "The man extends his arm to shake hands, then nods politely."; asıl uyarı karmaşıklık.
- "Fiziksel olayın doğal sonucunu prompta yazmak fiziği düzeltir": RED (V11a ❌, T2VPhysBench arxiv 2505.00337): "prompt refinement through providing hints can even produce negative impacts."
- "Soyut akıl yürütme yazma" önerisinin Sora'ya atfı: RED (V4c ∅: OpenAI rehberinde yok).

## Ölçüm notu — atlas "daha uzun yaz" demez
- Prompt uzunluğu ile hata arasında Spearman +0,26, 47 film (ARIZA Q06): uzun prompt biraz daha çok hatayla birlikte görülüyor. 50 filmde ortalama prompt 2.325 karakter; NEGATIVE ortanca %40,5 (`denetim_cikti.txt`).
- Bu yüzden atlasın düzeltmeleri cümle eklemez: çelişkiyi ve daveti çıkarır, kadrajı ya da çekimi değiştirir. Sora'nın kısa/uzun prompt cümlesi (V4b) bu yönle uyumlu; `film_dogrula`'daki 4.300 karakter tavanı değişmez.

## Sayılar — %17 ile %56 karşılaştırılamaz
- **05.10.2026 (49 film, yalnız 🔴):** "ölümcül hatanın ~%17'si prompt metninden". Bu analiz hatayı **düzeldiği yere** göre sınıfladı (ARIZA §T son satırı · AGENTS §0).
- **06.10.2026 (12 film, 🔴 + 🟠):** "gerçek kusurun %56'sı prompta bağlı" = (🅑 180 + 🅑+ 68) / (🅐 + 🅑 + 🅑+) 443. Bu analiz promptun **boşluğuna ve davetine** göre sınıfladı.
- Soru, payda ve film kümesi farklı; aynı bulgu hem 🅑 hem "hareket" olabilir. README'deki ikinci %56 ("🔴/🟠 satırların %56'sı geçersiz raporlardan") başka bir orandır.
- Tek sınıflama sözleşmesi: `QA_OKUMA_KILAVUZU.md` §1 (v1.0). Bundan sonra her yüzde sözleşme sürümü, sütun ve paydayla birlikte yazılır.
