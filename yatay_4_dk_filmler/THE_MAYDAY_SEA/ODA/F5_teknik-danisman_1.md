## THE_MAYDAY_SEA · Faz 5 tur 1 · teknik-danisman eleştirisi (G01 · G02 · G03)

### B1 · CİDDİ · C05: iki sert temas tek klipte, ikisi de kadrajda
KANIT    C05 Video: "3-7 s: The ring meets the socket edge to edge, and the station's single clamp turns on its hinge, swinging down from above toward the ring". 0-3 s'de de "the pod's ring begins a short straight movement toward the socket".
NEDEN    Halka-soket ve kelepçe-halka teması aynı 10 saniyede kadrajda. Model parçaları kaynaştırır ya da kelepçeyi halkadan geçirir. C19'un dayandığı bağ da kurulmamış olur.
ARIZA    T01 (PROMPT_HATA_ATLASI A03: nesne-nesne teması kapsam dışı; A04: "lock edge to edge" STOLEN_SKY S48'de 🔴 çıktı)
ÖNERİ    Başlangıç karesi halkayı soketle zaten temasta, kelepçeyi açık gösterir. Video tek hareket olur: "0-3 s: The camera is fixed and the clamp begins to swing down on its hinge toward the seated ring. 3-7 s: …closes around the ring. 7-10 s: …seats and locks." Halka ilerlemesi ve "meets the socket edge to edge" silinir. Temas C04→C05 kesmesinde atlanır.

### B2 · CİDDİ · G02 panel anahtarları, G01'deki çok panelli sayfalara göre güncellenmemiş
KANIT    G02 başlığı: "7.GOZLEM_ODASI, 6.KORIDOR, 4.OKYANUS tek görünüm". C09-C16'da ref 4 · 6 · 7 panel adı olmadan anılıyor, 9 yerde. Örnek C09: "Reference 7 (observation room): take the reinforced window … from it."
- C13: "using the head-and-shoulders portrait panel", ama çekim ¾ profil. G01 sayfa 1'de `three-quarter portrait panel` var.
- C14 notu: "4.OKYANUS sayfasında alt görünüş paneli yok". G01 sayfa 4'te `Underside panel` var.
- C16: "using the left and centre panels". Centre, duvara tırmanan şerit. Sayfa 9'da çekimin tam karşılığı `Wreck-cord panel` var.
- C11: ref 4 panelsiz. Sayfa 4'ün wreck fleet metni mekiği kanatsız çiziyor, C11 metni ise "short swept wings" istiyor.

NEDEN    Panel seçilmeyen çok panelli sayfadan model rastgele panel alır (SMOKE P17). Bu en çok öncelikli deneme C14'ü ve yara yanağı C13'ü vurur. C11'de kapsüle benzeyen kanatsız mekik geri gelir.
ARIZA    T05 · T09 · T16
ÖNERİ    Her referansa tek panel:
- C09: ref 7 `window close panel`.
- C10: ref 6 `floor-edge close panel`.
- C11: ref 4 `wreck fleet panel` + ref 7 `wide interior panel`.
- C12: ref 7 `console close panel`.
- C13: ref 1 `three-quarter portrait panel` + ref 7 `wide interior panel`.
- C14: ref 4 `underside panel`.
- C15: ref 4 `living network panel` + ref 9 `membrane panel`.
- C16: ref 4 `wreck fleet panel` + ref 9 yalnız `wreck-cord panel`.

Ayrıca sayfa 4 wreck fleet metnindeki mekiğe "short swept wings" eklenir. G02 başlığı ve iş emri satır 1-8 buna göre düzeltilir. C13 kimlik cümlesine G01/G03'teki "graphite joint seals" ve "white gloves" eklenir; başlık "aynı kelimelerle" diyor, C13 kısa kalmış.

### B3 · CİDDİ · Kokpit sol/sağ: kol frame-left, alıcı frame-right, yüz kameraya dönük; el ve omuz yanları çelişiyor
KANIT    C18 Görsel: "stands upright at the left edge of the console at frame-left, beside her left shoulder" (yüz "plainly visible … in three-quarter view"). C20 Görsel: "A left white glove is already wrapped around the orange grip". C23 Görsel: "In the right foreground her right white glove already rests on the receiver's broad physical toggle" (yüz sol yarıda görünür).
NEDEN    Kamera kadının karşısındaysa onun sağı frame-left'tir. Frame-left'teki kol kadının sağında, frame-right'taki alıcı solundadır. Üç prompt tersini ister. Model kolu ve alıcıyı yer değiştirir ya da eli gövdenin üstünden çapraz uzatır. C20 kameranın kadının arkasında olduğunu varsayan tek prompt, C18 ve C23 önünde. G03 notu yalnız C18'i işaretliyor.
ARIZA    T11 · T01
ÖNERİ    Ekran düzenini (kol solda, alıcı sağda, yüz önde) koru, yanları çevir:
- C18: "beside her left shoulder" → "beside her right shoulder".
- C20: "A left white glove" → "A right white glove".
- C23: "her right white glove" → "her left white glove".

Kamera kadının sağ-önünde sabitlenir. C18 ve C23 ref 1 `three-quarter portrait panel` kullanır, yara cümlesi geri gelir. FILM.md §4 C20/C23 plan cümleleri ("sol"/"sağ beyaz eldiven") güncellenir.

### B4 · CİDDİ · Durum panelleri: kapsül halkalı/halkasız ve kokpit kol/anahtar durumları anılan panelde yok, sayfa 2 kendi içinde çelişiyor
KANIT    Sayfa 2: "In every panel the pod has … At the front, a sacrificial dark-grey cylindrical docking ring sits on four short rigid mounts" ↔ "Nose after separation panel: … with the dark docking ring gone".
- C21: "using the side view panel" (halkalı durum), ama karede boşluk açılmış ve burun çıplak.
- C22: "using the rear-above panel" (halka durumu yazılı değil), ama çekim halkasız.
- `nose after separation panel` hiçbir çekimde anılmıyor.
- C23: "using the receiver switch-on panel", ama aynı karede "the broad silver lever with its orange grip lies pulled down against its stop" (`lever pulled panel` anılmıyor).

NEDEN    Filmin bedeli olan halkasız kapsülün iki karesi (C21, C22) halkalı durumu referanstan kopyalar. C23 kolun çekilmiş hâlini panelsiz çizer. Sayfa 2'nin "her panelde … ön tarafta halka" cümlesi halkasız panelle çakışır (A05).
ARIZA    T05 · T09
ÖNERİ    Sayfa 2 cümlesini durum bazlı böl: "In the first three panels the ring sits on its four mounts; in the nose-after-separation panel and the rear-above panel the ring is gone and the four bare mounts surround the sealed hatch." Altıncı panel eklenir: `side view after separation panel` (tam yan, halkasız). C21 ref 2 için onu anar, C22 halkasız `rear-above panel`da kalır. Sayfa 3'e tek panel eklenir: kol çekilmiş ve anahtar açık geniş iç. C23 yalnız onu anar.

### B5 · CİDDİ · G01'de replik, vuruşun son cümlesi değil (C02 ×2, C06, C07, C08)
KANIT    C02: "plays a tired man's voice, softened by a light radio filter: Mayday. Please. Come closer. Her lips stay closed and her eyes stay on the canopy at frame-left". Aynı klipte: "she says in a calm, professional voice: Rescue vessel. I hear you. Her lips move with the sentence."
- C06: "…has no power. Her lips stay closed behind the clear visor while her helmet begins to turn".
- C07: "…Come closer. The transmitter module stays dark and gives no sound".
- C08: "…Then who is calling? Her lips move with the question."

NEDEN    Tırnaksız iki nokta biçiminde repliğin bittiği yeri yalnız sonraki vuruş etiketi gösterir. Araya giren cümle konuşmanın devamı sanılır ya da seslendirilir (A10: model betimi seslendirir). Asıl kapalı-ağız talimatı da böylece konuşmanın içinde kaybolur. G02 ve G03 "replik vuruşun SON cümlesidir" kuralına uyuyor, G01 uymuyor.
ARIZA    T16 (A10)
ÖNERİ    Aynı cümleleri repliğin önüne al, sözcük sayısı değişmez. Örnek C02: "Her lips stay closed and her eyes stay on the canopy while the receiver's cyan status lamp pulses; at about 1 s the small receiver plays a tired man's voice, softened by a light radio filter: Mayday. Please. Come closer." İkinci vuruş: "Her lips move with the sentence as at about 5 s she says in a calm, professional voice: Rescue vessel. I hear you." C06, C07 ve C08 aynı biçimde düzenlenir.

### B6 · CİDDİ · Ses kimliği: Mara 6, AI 8 ayrı klipte; yedek yalnız R07 · R10 · R17'yi kapsıyor
KANIT    FILM §5 Mara: R01 C01 · R03 C02 · R08 C08 · R11 C13 · R14 C18 · R18 C24. AI: R04 C03 · R05 C04 · R06 C06 · R09 C11 · R12 C15 · R13 C16 · R15 C19 · R16 C22. Yedek yalnız: "C02 klibinin sesi … C07/C12/C23'e".
- Mara tarifi kayıyor: C02 "in a calm, professional voice" · C12 "a calm adult woman's voice with a light radio filter" · C23 "a calm woman's voice, softened by a light radio filter".
- AI tarifi kayıyor: C03, C04, C06, C19, C22 "calm adult man's voice" · C11, C15, C16 "calm, plain adult male voice".

NEDEN    "That's my voice" (C13), C13'te üretilen Mara'nın C02/C12 sesiyle eşleşmesine bağlı. C13 için yedek yok. AI sekiz klipte sekiz ayrı ses çıkabilir. C06 (AI) → C07 (çağrı) kesmesinde izleyici iki erkek sesini ayıramayabilir.
ARIZA    T16 (BILINEN_TUZAKLAR §B sıra 11: ses kimliği)
ÖNERİ    (1) Her konuşana tek sabit tembr cümlesi, duygu eki ayrı:
- Mara: "an adult woman's voice, warm and low" + professional | hesitant | firm.
- AI: "a calm adult man's voice, even and unhurried". C11, C15, C16 bu kalıba geçer.
- CALLER: "a tired man's voice". C02 ve C07'de aynı.
- C12 ve C23'te Mara tarifi C02'nin birebiri.

(2) SMOKE P18'e iki karşılaştırma eklenir: C02 ↔ C13 Mara tonu, C03 ↔ C22 AI tonu. Tutmazsa yedek, o konuşanın bütün satırlarına genişler (replik tek kaynaktan).

### B7 · CİDDİ · C19 ve C21: kelepçe ve su halkası aynı halkayı aynı yerde sarıyor, "sıkılaşma" rijit halkada gösterilemez
KANIT    C19 Görsel: "The station's single broad rigid hinged clamp … is closed around the ring from above. One coherent, smooth, glossy dark teal ribbon … is already wrapped once around the ring in a single wet loop". Video: "the single ribbon of water begins to tighten around the rigid ring". C21: "locked in the station's single broad clamp, held by one smooth wet loop of dark teal water".
NEDEN    Halkanın hangi bandını kelepçe, hangisini su sardığı yazılı değil. Model suyu kelepçenin içinden geçirir ya da halkayı sıkışmış, bükülmüş çizer. Rijit halkada "tighten" yalnız halkanın deforme olmasıyla görünür.
ARIZA    T01 · yeni (A05)
ÖNERİ    İki karede de yer ver: "the clamp holds the socket-side end of the ring, the wet loop circles the middle band of the ring, a band of bare dark metal visible between them". C19 videosunda "tighten" yerine: "the water gathers at the loop's base on the station side and the loop's glossy surface brightens, its size unchanged".

### B8 · CİDDİ · Vakumda ses (T13): replik taşıyan yedi dış klipte klibin kendi sesi filme giriyor
KANIT    FILM §6: "her replik taşıyan parça timeline'da klip_sesi: true, klip_kazanc_db −3…−6 (klibin kendi uğultusu yatağın altında kalır)". Dış mekânda replik taşıyanlar: C01 · C03 · C04 · C15 · C19 · C22 · C24. C22 Video: "as it accelerates smoothly toward frame-right … its two rear thrusters glowing a little brighter".
NEDEN    Model itici ve metal hareketine motor ya da gıcırtı sesi koyar. Ortam cümlesi yazılıyken de koyuyor (BILINEN_TUZAKLAR §B sıra 3, 51 satır; SINIF 🅐1: ses satırı yazılıyken 4 🔴, yazılmamışken de 4 🔴). −3…−6 dB yalnız kısar, silmez.
ARIZA    T13
ÖNERİ    C22 videosunda "accelerates smoothly" ve "glowing a little brighter" yerine "pulls away at a steady pace; the two rear thrusters keep their shape". F8'de bu yedi klipte klip_sesi yalnız FILM §5 replik penceresinde (±0,5 s) açık, kalan süre kapalı. kurgu.py aralık desteklemiyorsa pencere kesilip `ses` parçası olarak yerleştirilir.

### B9 · KÜÇÜK · C04 son vuruş duruyor, geçiş tablosu "hareket üstünde" diyor
KANIT    C04 Video: "7-10 s: The glide eases and the ring comes to a smooth stop just short of the socket, a thin gap still open". FILM §6 GEÇİŞ: "C04→C05 … hareket üstünde: sola kayma → temas".
NEDEN    Klip durağan kareyle biter, kesme fotoğraftan fotoğrafa olur (GECIS_VE_SES_SUREKLILIGI §0).
ARIZA    yeni
ÖNERİ    "…the glide slows but keeps moving, the ring still closing on the socket". C05'in ilk vuruşu zaten hareketli (B1).

### B10 · KÜÇÜK · C22: halkasız burun arkadan görünmeyen bir ayrıntı olarak isteniyor
KANIT    C22 Görsel: "from behind and above the pod … nose pointing toward frame-right and away from the camera … At the far end of the nose sits a flat sealed inner hatch set among four short bare mounts."
NEDEN    Bu açıdan burun kadrajda okunmaz. Model burnu kameraya çevirir ya da halkayı geri çizer.
ARIZA    T05
ÖNERİ    Cümleyi sil. Halka bedeli C21 (halka istasyonda) ve C24 (halka portta) ile okunur.

### B11 · KÜÇÜK · Sayfa 1 iki bilinen red kalıbına yakın (yedi klibin tek kapısı)
KANIT    G01 sayfa 1: "a 34-year-old deep-space rescue pilot with light olive skin, grey eyes, a short straight black bob … a small pale scar along her right cheekbone" ve "a close view of her two white gloves side by side, one seen from the back of the hand and one from the palm".
NEDEN    İlki kimlik yığını (BILINEN_TUZAKLAR §A satır 8, HİPOTEZ, RED 15; RISING SNOW S2'de "kesin yaş + yara izi" sökülünce geçti). İkincisi yan yana iki el, yakın, yüzsüz kadraj kalıbı (YERCEKIMI S8, RED 13, kelimeyle çözülmedi). Her ikisi de kanıtlı eşleşme değil, kalıp benzerliği.
ARIZA    yeni
ÖNERİ    İlk deneme "34-year-old" ve "light olive skin" olmadan yazılır ("an adult woman … grey eyes … a small pale scar"). Eldiven paneli tek eldiven olur: "one white glove with its sleeve cuff and burnt-orange band, seen from the back of the hand". Panel adı `glove panel` olur (C20 zaten "take the white glove" diyor). Ret gelirse gün, araç ve birebir mesaj NOTLAR RED'e yazılır.

### B12 · KÜÇÜK · "lever" kök sözcüğü nesneye bağlanmadan tekrar ediyor
KANIT    C18 Video: "eyes fixed on the lever … her gaze stays on the lever … her eyes still on the lever … the lever stays upright" (4×). C20 Video: "the lever starting to rock … pulls the rigid lever … the lever reaches the mechanical stop". G03 başlığı "kol her yerde '…with its orange grip' diye bir nesneye bağlı" diyor, video vuruşları değil.
NEDEN    Kısa ayırt edici sözcüğün tek başına tekrarı kumandaya yazı olarak basılabilir (A11: `release` K30'da 6 kez, ekranda "SUIT RELEASE").
ARIZA    T06 (A11)
ÖNERİ    Tam ad yalnız görselde kalır. Video vuruşlarında "it" ya da "the orange grip". Promptta "lever" ≤2.

### B13 · KÜÇÜK · C18: nefes istemi, zorunlu ortam cümlesiyle çelişiyor
KANIT    C18 Video: "draws one controlled, urgent breath" · "her breathing quick but steady" ↔ aynı promptun ortam cümlesi "close, calm breathing inside the helmet".
NEDEN    Aynı promptta zıt iki nefes istemi (A05). Ortam cümlesi birebir kalmak zorunda, değişecek olan vuruş.
ARIZA    yeni (A05)
ÖNERİ    "draws one controlled breath" · "her breathing steady".

### B14 · KÜÇÜK · C24: son replik 8,5. saniyeye uzanıyor, Omni kareden-video süresi ölçülmedi
KANIT    C24 Not: "söz yaklaşık 8,5. saniyeye uzanır". FILM §5 R18: saniye 4.0, süre 4.5. FLOW_GERCEKLERI §1: "Omni karelerden video kaç s: BİLİNMİYOR → ÖLÇÜLECEK P6".
NEDEN    Klip 8 s çıkarsa filmin son cümlesi ortasından kesilir. Replik saati sondan taşan tek klip bu.
ARIZA    yeni (FLOW_GERCEKLERI §9)
ÖNERİ    Vuruşları 0-3 · 3-8 · 8-10 yap. Replik 3 s'de başlar, 7,5 s'de biter.

### B15 · KÜÇÜK · G02 EKLE satırı kare ve video referanslarını tek satırda karıştırıyor
KANIT    G02: "EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası): ref/7.GOZLEM_ODASI_v1.png" ↔ G01 ve G03: "KARE (Görsel): … · VİDEO (Frames to Video): yalnız kare/…".
NEDEN    Referans Frames to Video adımına yüklenirse mod Ingredients'e kayar (G03 başlığı) ve başlangıç karesinin anlamı değişir.
ARIZA    yeni (FLOW_GERCEKLERI §1)
ÖNERİ    G02 EKLE satırlarını G01 biçimine çevir (KARE ve VİDEO ayrı).

KORU: C20 Görsel "A left white glove is already wrapped around the orange grip" ve C23 "her right white glove already rests on the receiver's broad physical toggle". Temas ilk karede kurulu, video tek hareket (A03 DÜZELTME). B3 yalnız el yanını değiştirir.
KORU: C10 Görsel "the level floor grate fills the bottom foreground, so it is plain which way is down" ve "a fixed handrail support". Aynı kadrajdaki iki yerçekimi rejimini ayıran işaret bu (T08).
KORU: Gövde taramasında (rg) şunlar çıktı:
- ORTAK GÖRÜNÜM cümlesi 48/48 promptta birebir.
- ORTAM SESİ cümlesi 24/24 video promptunda, doğru mekânla birebir.
- BILINEN_TUZAKLAR §A kelimeleri (body, dead, blood, wound…) prompt gövdelerinde 0.
- Çekim ve referans kodu, büyük harfli jeton ve karakter adı gövdelerde 0.
- En uzun satır 3.300 karakterin altında.

KAPSAM DIŞI: FILM.md §3 (satır 101) ve §4 Risk sütunları kaldırılan kaynak-kare bağımlılıklarını (C16←C11 · C19←C05 · C21←C19 · C22←C21) hâlâ anıyor; bu devamlilik işi.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 8 · KÜÇÜK 7
KARAR    TUR KAPANABİLİR. B1-B8 CİDDİ olduğundan yazarın KABUL/RED cevabı gerekir.
GİRDİ    Eleştirilen eser:
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/PROMPTLAR/G01.md` (referans promptları 1-9, C01-C08 ve iş emri)
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/PROMPTLAR/G02.md`
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/PROMPTLAR/G03.md`

Bağlam (tamamı okundu):
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/FILM.md` (§1-§7)
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/NOTLAR.md`
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/ODA/DURUM.md`
- `/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/THE_MAYDAY_SEA/ODA/SAHIP_PLANI.md` (yalnız satır 480-569)

Bilgi tabanı:
- `/Users/dai/github/apex_md/film_md/uretim_hatti/ELESTIRI_PROTOKOLU.md`
- `/Users/dai/github/apex_md/film_md/uretim_hatti/BILINEN_TUZAKLAR.md`
- `/Users/dai/github/apex_md/film_md/uretim_hatti/ARIZA_LISTESI.md`
- `/Users/dai/github/apex_md/film_md/uretim_hatti/FLOW_GERCEKLERI.md`
- `/Users/dai/github/apex_md/film_md/uretim_hatti/PROMPT_HATA_ATLASI.md`
- `/Users/dai/github/apex_md/film_md/uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md`

YAPILMADI  Şunlar yapılmadı:
- Klip ve kare yok. Hareket ve ses tahminleri ölçüm değil, kayıtlı arıza kalıplarından çıkarım.
- `SMOKE_TEST.md` P18 satırı çok uzun olduğundan okunamadı. P9 ve P17 yalnız FLOW_GERCEKLERI üzerinden kullanıldı.
- `kurgu.py`'nin klip_sesi aralık desteği doğrulanmadı (B8 öneri koşulu).
- NOTLAR DENEMELER'de gerçek deneme yok. "Aynı sebeple iki kez bozulan çekim" kuralı uygulanamadı.
- ODA/F5_* önceki sürümleri ve devamlilik/denetci çıktıları görülmedi (bağımsızlık).
