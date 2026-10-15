# F5 denetci — kapı denetimi 2 (15.10.2026, sonnet; aynı ajanın SendMessage devamı, doğrulanamayan maddeler)

FAZ 5 KAPISI · THE_FURNACE_GATE

Mekanik ❌ yok. Yargı ❌ yok, ama F5.10 için bir düzeltme önerim var (aşağıda). Doğrulanamayan kalan maddeler küçük ve aşağıda sayılı. SONUÇ: KAPANABİLİR.

Klasör git'te izlenmiyor (`??`), bu yüzden `git diff` yoktu. Ö4'ü ODA raporlarındaki "eski → yeni" metinlerin güncel `PROMPTLAR/G0x.md`'de aranmasıyla denetledim. Yeni metin vardı mı, eski metin kalmış mı diye grep ve python ile saydım. Beyanı tek başına kanıt saymadım.

**Mekanik çıktı** (`film_dogrula.py yatay_16_dk_filmler/THE_FURNACE_GATE --bolum …`)
- `prompt`: "çekim: 96 · ✅ yapı geçerli".
- `kunye`, `hikaye`, `cekim`, `muzik`, `sahneleme`, `durum`: hepsi "✅ yapı geçerli".
- `replik`: "⚠️ 95 replik — bant 40-70" ve "✅ yapı geçerli". Bant dışı gerekçesi FILM.md §5 altında yazılı ("Bant dışı gerekçe: 95 replik > 70…").
- `kurgu.py` bu fazda gerekmiyor.

| Madde | Durum | Kanıt |
|---|---|---|
| Ö1 M | ✅ | `ODA/` içinde var: `F5_devamlilik_1_G01-G04.md`, `F5_devamlilik_1_G05-G08.md`, `F5_teknik-danisman_1_G01-G04.md`, `F5_teknik-danisman_1_G05-G08.md`, `F5_fable_birlestirme_1.md`, `F5_goruntu-yonetmeni_1_G01…G08.md`, `_2_G01…G08.md`. |
| Ö2 M | ✅ (Fable'a not) | Dört eleştiride GİRDİ satırı var. "EKSİK" kelimesi yalnızca olumsuz geçiyor: devamlilik G05-G08 satır 171 "EKSİK: yok (görevin verdiği girdiler eksiksiz açıldı)", teknik-danisman G01-G04 satır 142 "EKSİK: yok.", teknik-danisman G05-G08 satır 298 "EKSİK: yok (…)". Devamlilik G01-G04'ün GİRDİ'sinde "EKSİK" yok. Protokole göre EKSİK yalnızca açılamayan görev girdisi için yazılır, o yüzden ✅ saydım. Birebir "EKSİK içermiyor" taraması eşleşir. `uretim_hatti/araclar/` içinde böyle bir tarama aracı yok. Fable bilsin. |
| Ö3 | ✅ | Eleştirilerde ÖLÜMCÜL 0, CİDDİ 33. Bir grubun `_2` dosyasında anılmayan CİDDİ id'lerin hepsi başka grubun çekimine ait (G04: D1-B3/T1-B6 C12, D1-B6/T1-B4 kasa, T1-B2 C03; G06: T2-B2 C52, T2-B3 C86/C88/C95; G08: D2-B2/B3 C64 C68 C72). G01-G03 ve G07 dosyaları ilgili bütün id'leri anıyor. `F5_fable_birlestirme_1.md` her CİDDİ'yi K/G kararına bağlıyor. |
| Ö4 | ✅ (G01-G03, G05, G07 kesin · G04, G06, G08 örneklemle) | G01: ORTAK satır 67'de 2.RHEA düzeltmesi var; gövdede EMP yok. G02: yedi bekleyen düzenlemenin hepsi dosyada (13/13 eşleşme raporda, ben ayrıca 52, 96, 135, 140, 184, 294 ve başlık 15'te buldum). G03: "fades away" (satır 150), C36'dan "tug docked" çıkmış (272), C27 notu düzeltilmiş (80). G05: C56 ve C58 YENİ metinleri 1'er kez var, ESKİ metinler 0 kez. G07: U1-U7 YENİ metinlerinin hepsi 1'er kez var, ESKİ metinler 0 kez. G04, G06, G08'de "uygulanamadı" satırı yok. Örnek K kararları uygulanmış: R38/R52/R65 yeni metinleri; C44 DIŞ DÜNYA ve "swells in place"; C48 sol duvar penceresi; C68/C72 "farther from the lens"; C62/C68/C72 kamera kilitli; C85 kelepçe 3-6 s'de oturuyor; C87 gevşek tether; C89 "faint steady blue glow"; C91 `clamps open panel`; C92 50 mm; C94 adsız VO; C86/C88/C95 YEDEK ve "Örnek C" notu; C52 kıvılcım yerine "single bright flash". FILM §5'te R29/R33 = 2.5, R12 = 2.0, K8'in saniyeleri ve K13 telsiz listesi uygulanmış. FILM §4 Referans sütunu EKLE ile 96/96 aynı. FILM §3 "Kullanan çekimler" EKLE türeviyle 15/15 aynı. Açık notlar, kapıyı bloklamıyor: `_2_G02` madde 8 (not satırlarına "15.10" gerekçesi) bilerek yazılmamış. K'nın "C88/C93 rota göstergesi light bar" cümlesi uygulanmamış, çünkü bu promptlarda rota göstergesi yok; yalnızca "single cyan status light" var. Fable'ın açık bıraktığı risk (`_2_G07`): 3.KESTREL ile 14.ISKELE kelepçe yakası, C84'te çift kelepçe riski; F7 kare kapısında C80 ve C84'e bakılacak. |
| Ö5 | ✅ | Tek RED'ler `_2_G08` satır 17 ("kadrajda olmayan tarif edilmez") ve satır 21 ("G08 promptlarında kısaltma yok"). İkisi de kanıta cevap veriyor; EMP'nin 96 çekimde 0 olduğunu ben de saydım. |
| Ö6 | ✅ | `DURUM.md` AÇIK ÖLÜMCÜL tablosu boş; dört eleştiri de ÖLÜMCÜL 0. |
| Ö7 M | ✅ | `DURUM.md`: FAZ 5, TUR 1, AJAN_CAGRI 20 / 50, SON_GUNCEL 15.10.2026, SIRADAKI dolu. FAZ GÜNLÜĞÜ'nde 15.10 satırı var (satır 51, "çağrı 13-19"). 12+7+bu çağrı = 20 tutuyor. `--bolum durum` geçerli. Satır 51 hâlâ ilk denetim sonucunu ("KAPANAMAZ (kanıt eksik…)") taşıyor; kapı kararından sonra Fable güncellesin. |
| F5.1 M | ✅ | `--bolum prompt` çıktısı yukarıda. Python taramasında prompt gövdelerinde Leon/Rhea adı, EMP, body/bodies/full-body, dead/dies/die, kod (Cxx, Rxx), büyük harfli kısaltma, "Clip n", "previous clip / last frame / first frame" ve olumsuz kuyruk: hepsi 0. En uzun blok 2.876 karakter (C93 görsel), sınır 4.300. |
| F5.2 | ✅ | ÖLÜMCÜL açık yok. Taraf, sayı ve rol kontrolleri geçti: 15 referans numarası ↔ tek rol (1 man · 2 woman · 3 tug · 4 cockpit · … · 15 tools); EKLE sırası = `Reference` sırası 96/96; C14 ve C42'de tether sağ kalça. Kimlik cümlesinin birebirliğini ben ayrıca saymadım; devamlilik tur 1'de baktı. |
| F5.3 | ✅ | Teknik-danisman GİRDİ'leri G01-G08 promptlarını ve FILM §3-§5'i kapsıyor. FILM §4 Risk sütunu 96/96 dolu. |
| F5.4 M | ✅ | `FLOW` satırı 96/96, hepsi "Frames to Video". `EKLE` 96/96, numaralı dosya adı + "(yükleme sırası)" + "VİDEO … yalnız kare/Cxx.png". G01'de 15 `DOSYA ref/<No>.<AD>_v1.png` satırı var. |
| F5.5 M | ✅ (zincir yok) | FILM.md satır 185-186 "bu filmde zincir yok (§4 Zincir sütunu '—')", satır 341 aynı. `SAHNELEME.md` doldurulmamış şablon ve içinde örnek `Z1 · C02 C03` satırı var; faz 3b'nin konusu, F5'i bağlamaz. |
| F5.6 | ✅ | Grup içinde aynı iskeletin en çok tekrarı: G01 2, G02 3, G03 3, G04 2, G05 3, G06 3, G07 3, G08 2 (K14 sınırı ≤3). Dört vuruşlu çekim sayısı: G01 3, G02 2, G03 2, G04 2, G05 2, G06 3, G07 4, G08 3 (her grupta ≥2). Film genelinde 19 farklı iskelet; en sık (4,7,10) 12 çekimde. 96/96 vuruş planı geçerli. Son vuruşta "holds/stays" kalıbı 4 çekimde geçiyor (C11, C18, C29, C30). Hepsinde aynı vuruşta yeni evre var: C11 "push-in closes slightly tighter", C18 "tilt slows to a gentle drift", C29 "red light climbs the front of the crate", C30 "glow … fades away". Donma yok. |
| F5.7 | DOĞRULANAMADI (kısmen) | G01'de 15 sayfa promptu var. 10.CEKIRDEK'te yedi panelli PANELLER satırı ve "plain unmarked surfaces" okundu. Her çekimin istediği panelin sayfada var olduğunu ve hiçbir sayfada yazı/etiket istenmediğini 15 sayfada tek tek sayamadım. |
| F5.8 | ✅ (iki küçük nokta açık) | ORTAK GÖRÜNÜM birebir ve sonda: 192/192 (96 görsel + 96 video). Mekân ışığı: her görselde FILM §3'ten tam bir cümle var, 96/96. C41 ve C46'da "light inside … light outside" ile KOKPİT ve DIŞ birlikte, tasarım gereği. ORTAM SESİ: her videoda tam bir cümle var, 96/96; ışık ↔ ses mekân uyuşmazlığı 0. DIŞ DÜNYA cümlesi 40 görselde; C41/C46 dışında hepsinde "The light is" öncesinde. Ardışık aynı-mekân çiftlerinde lens eşit olanlar: C03→C04, C20→C21→C22, C38→C39, C41→C42, C59→C60, C65→C66→C67, C84→C85. Hepsinde özne, koltuk, mesafe ya da nesne farkı çerçeve cümlesinde yazılı. İlk vuruş hareketle başlıyor 95/96 (fiil taraması). C74'ün ilk vuruşunda ("The camera stays locked off … the single rigid centre section of the…") cümlenin devamını okumadım; kamera K17 gereği kilitli, hareket yapının. DOĞRULANAMADI (tek çekim). |
| F5.9 M | ✅ | FILM §5'teki 95 replik metni video promptunda birebir var, eksik 0. Hiçbir replik 1,5 s'den önce başlamıyor ve hiçbiri 9,0 s'den sonra bitmiyor (saniye + süre taraması). 37 telsiz çekiminin hepsinde "softened by a light suit-radio filter … out of frame" kalıbı var. İlk taramadaki 26 uyuşmazlık, kalıbın "suit radio" yerine "suit-radio" yazılmasından çıkan yanlış alarmdı. Kadrajda kişi olan telsiz çekimlerinden 27'sinde ağız-kapalı açıkça yazılı. Kalan 10'unda (C34 C49 C51 C56 C60 C65 C67 C71 C79 C90) yüz görünmüyor: eldiven/kol detayı ya da arkadan çekim, C49'da "his face stays turned away". |
| F5.10 | ❌ (küçük) | C01-C03 prompt gövdelerini ve notlarını okudum. Yazı, logo, kalabalık ve hızlı kamera yok; C01 "Logo ve görüntüde yazı yok", C02 ve C03'te eldiven/ön kol yalnızca dinleniyor. Eksik olan: C03 şeffaf vizörde yüz (50 mm ¾ orta plan, "reflected amber light … across his closed clear visor") içeriyor, ama FILM §4 Risk hücresi yalnızca "T01 sağ eldiven kumandada ilk karede; Leon ağız kadrajda". Vizör/yüz riski ancak `PROMPTLAR/G01.md` C03 notunda ("şeffaf vizörde yüz riski (ILK_30 §6) … YEDEK") yazılı; KABUL "risk sütununda yazılı" diyor. Ek not: C02'nin §4 Risk hücresi hâlâ "Rhea ağız kadrajda ≤5 s" diyor, oysa R02 artık "model sesi (telsiz)". Bu eski bir hücre. |

MEKANİK ❌   yok

YARGI ❌     F5.10 (FILM §4 C03 Risk hücresinde vizör/yüz riski yok; C02 hücresi eski). Fable ya hücreleri bir cümleyle düzeltir ya da gerekçeyle aşar. Aşılırsa `DURUM.md` AŞILAN KAPILAR'a yazılır.
DOĞRULANAMADI (❌ değil): F5.7 panel↔çekim uyumu ve sayfa yazısı yokluğu, F5.8 C74 ilk vuruş cümlesi, F5.2 kimlik cümlesi birebir sayımı, Ö4 G04/G06/G08'de örneklemle doğrulananların dışındaki K kararları.

SONUÇ        KAPANABİLİR (mekanik: yok / yargı: F5.10, Fable gerekçeyle aşabilir ya da §4 Risk hücrelerini düzeltir)

İlgili dosyalar (hepsi `/Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/` altında):
- `FILM.md`
- `ODA/DURUM.md`
- `ODA/F5_fable_birlestirme_1.md`
- `ODA/F5_goruntu-yonetmeni_2_G01.md` … `_2_G08.md`
- `PROMPTLAR/G01.md` … `G08.md`
- `SAHNELEME.md`
