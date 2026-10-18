# THE_FURNACE_GATE

KAYNAK: `ODA/HAM_QA_RAPORU.md` (16.10.2026 14:22, takipsiz). Dört bölüm de var: Anlatım Testi (1-9 + A1-A4 tablosu) · İzleme Formu A (sahibin sekiz sorusu) + B ("Dış İzleyici Simülasyonu") · Süreklilik · Tarama. İzlenen: `taslak_01`, 2. parça (C25-C48), 4:00 = 24 × 10 s, parça içi 00:00 = C25 başı. `ODA/QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU.md` yok. **Bulgu satırı 71 / tekil 44.** Satırlar: ANL tablo 8 · İZ-A 22 · İZ-B 9 · SÜR 25 · TAR 7. Anlatım'ın düz metin içindeki tekrar anışları (§2 "03:57 üçüncü astronot", §8) ve SÜR "kontrol edilemedi" notu satır sayılmadı, tablodaki satırla birleşti.

PROMPT SÜRÜMÜ: Üretimde **`PROMPTLAR/G03.md` (C25-C36) + `PROMPTLAR/G04.md` (C37-C48)** kullanılmış. Sahibin paketi `THE_FURNACE_GATE_16MIN_96_CLIPS.md` K25-K48 kullanılmamış. Kanıtlar:
1. QA 02:02'de "The gate drive **has no power**. The capture locks are still powered." duyuyor. Bu, PROMPTLAR/G04 C37'deki R38 metni (sahip 14.10'da değiştirdi). Paket K37'de "The gate drive **is dead**." yazıyor.
2. Paketin bütün video promptları "No spoken dialogue, narration, music or subtitles; these are added in the edit." diyor. QA ise klibin içinde dudakla oynayan konuşma duyuyor (TAR#1: "kadının dudakları … ikinci seferde konuşuyor"). Model sesi takılmaları da var ("and release port" ×2, "we lose the core" ×2). Bunlar ancak PROMPTLAR'daki `says …: <line>` satırlarından çıkabilir.
3. Kokpit tarafları PROMPTLAR K19'a uyuyor. Paket her K'da "Leon seat left, Rhea seat right", K37'de "Medium Rhea seated right" diyor. QA ise C37'de kadını solda, C38'de erkeği sağda, C40 ve C43'te kadını solda/erkeği sağda, C47'de erkeği sağda görüyor. Demek ki başlangıç kareleri de PROMPTLAR Görsel'inden üretilmiş.
4. C42: QA "kemer tokası" görüyor. PROMPTLAR'da "clipped to his belt", pakette "attached to his harness" yazıyor.
5. `git diff PROMPTLAR/G04.md`: çalışma kopyasındaki tek fark, C37 bloğundan sonra eklenmiş "37 ve 38 imageleri hazır videolar yokkk" sahip notu (dosya 15.10 18:04, QA 16.10 14:22). Değişiklik **QA'dan önce** yapılmış ve prompt metnine dokunmuyor. Sahibin üretimi bu dosyadan yürüttüğünü de gösteriyor. Alıntılar HEAD (265be58) = çalışma kopyası metnidir.
6. NOTLAR DENEMELER yalnız şablon satırlarını taşıyor: deneme no, prompt sürümü ve yüklenen ref kaydı yok. Sürüm "p1" varsayıldı.

Yöntem notları:
- **Eşleme:** Rapor zamanı = parça başı + 10 s'lik sıra. İçerik çapası her çekimde doğrulandı: R27 00:01 … R51 03:52 replikleri ve görüntü tarifi sıradaki çekimin promptuna uyuyor. Komşuya kayan yok. NOTLAR'daki çekim eşlemesi doğru. `timeline.json` şablon hâlinde ("FILM_ADI"). Montaj hat dışında yapılmış, `kurgu.py` kullanılamadı. `~/film_medya/THE_FURNACE_GATE/` altındaki kare/, ham/, ref/ boş: başlangıç karesi açılamadı. "kare" hükümleri rapor tarifine ve promptun kareyi tanımlamasına dayanıyor.
- **Kaynak geçerliliği (QA_OKUMA §4):**
  - TARAMA 240 s'lik videoya koşulmuş ve "WHAT SHOULD BE IN THIS VIDEO" boş kalmış → geçersiz (`>90 s` · `ne olmalı`).
  - SÜREKLİLİK 240 s, kesme listesi verilmemiş ("videodan tespit edilerek") → geçersiz (`>90 s`).
  - İZ-A "sahibin" formu olarak geliyor, ama 3. soruda Arapça "تركيب" belirteci var. Yapay zekâ yazımı olabilir.
  - İZ-B açıkça "simülasyon", NOTLAR ise bunu "B1" diye kaydetmiş.
  - Sonuç: **giysi, arma ve koltuk bulgularının tamamı yalnız SÜR'den geliyor.** İnsan doğrulaması hiçbir satırda yok (NOTLAR: "doğrulanacak"), sınıflar geçici.
- **Rapor içi çelişkiler:**
  - SÜR#2 C27 göğsünü "small glowing square module" diye anlatıyor, SÜR#8 aynı C27 için "wide rectangular chest box" diyor.
  - SÜR#1 00:10.0'da çekirdeği "free in mid-air" görüyor, TAR ise C26 için 00:10-00:12'yi temiz sayıyor.
  - TAR C42 temiz aralığı "02:50.0-02:50.0" (0 s), ama C42 için tarama satırı yok.
- **Sınıf ilkesi:**
  - Plan ya da F5 K-kararıyla bilinçli kurulan şey 🅒 sayıldı: boş kasa K28, vizör repliği R32, VO C44, kilitli kamera K17, K19 ters açı. Anlatım maliyeti gerçek olabilir ama bu çekim listesi konusu, prompt yazımı değil.
  - Promptun kendi kelime alışkanlığı ("slow", "belt") 🅑+ sayıldı.
  - Birleştirme ±2 s + aynı nesne kuralıyla yapıldı. İki tekile bölünen ham satırlar: SÜR#3, #8, #9, #14, #15, #16, #24 · ANL#6 · İZ-A1, A6c · İZ-B4, B5b, B5c.
- **Tabloya girmeyen gözlemler (QA kusur demedi):**
  - ANL §1 "çekilen kol kıvılcım çıkararak bozulur": C34 promptunda kıvılcım yok.
  - ANL 00:50 "lazer ve enerji atışları" (çoğul): C30 "one brief fictional blue-white pulse" istiyor.
  - ANL "bileğindeki ekrana bakarak" (C37): bkz. kusur K6.
- **NOTLAR kontrolü:** Eşleme doğru. Ama KARARLAR (16.10) madde (6) "C37–C47 … koltuk değiştirmesi (`seats from the front panel` kuralına kilitlenecek: önden çekimde pilot sağda, Rhea solda)" yanlış okuma. C37, C38, C40, C43, C45 ve C47 bu kurala zaten uyuyor. Altı S3 satırının dördü K19'un tasarladığı ön ↔ arka ¾ ters açısı, biri C42'nin gerçek hatası, biri de onun kesmedeki yansıması (#20 #26 #28 #37 #41).

## BULGULAR

| # | çekim | rapor (bölüm · zaman) | bulgu (≤15 kelime) | tür | sınıf | promptta ne yazıyor — Görsel / Video | doğduğu yer | not |
|:--:|:--:|---|---|---|:--:|---|---|---|
| 1 | C26 | ANL#1 00:17 · TAR#1 00:12-00:19 · İZ-A5 · İZ-B5 | "Careful" kadında; "worth more than the tug" önce erkek, sonra kadın tekrarlıyor | replik tekrarı/ses | 🅐 | V: "her lips staying closed, and from out of frame a low, dry adult man's voice … says: Careful. That's worth more than the tug." | ses | kadrajda tek kişi + kadraj dışı model sesi; 00:17 kurguda atılır |
| 2 | C26 | SÜR#1 00:10 · İZ-A3 00:11-00:20 · İZ-A4 00:11 | Çekirdek havada asılı, eller bırakıyor, ağırlık yok | yerçekimi/fizik | 🅐 | G: "the compact graphite core still seated in the cradle" / V: "her shoulders beginning to take its weight" · "both gloves keeping the same grips" | hareket | SÜR kesmede havada der, TAR 00:10-00:12 temiz: çelişki |
| 3 | C26→C27 | SÜR#2 00:20 · İZ-A3 00:20 · İZ-B6 00:20 | Ellerdeki büyük kutu göğüste küçük modüle dönüşüyor | ekipman/nesne biçimi | 🅑 | C26 G: "the core … from it, using the vault wide panel" / C27 G: "the compact graphite core locked into her rigid chest carry harness" — ölçü YOK | kare | çekirdek iki çekimde iki ayrı sayfadan (ref 10 ↔ ref 2 askı paneli) |
| 4 | C28 | SÜR#3 · ANL#2 00:30 · İZ-A3/A6/A7 00:30-00:39 · İZ-B6/B7 | 10 s boş kasa; ses kadraj dışından; karakterler nerede belirsiz | hikâye/anlatım | 🅒 | G: "and the room is quiet and empty" / V: "from out of frame a low, dry adult man's voice … says: That woke the security grid." | — | plan K28 "No visible people"; anlatım maliyeti gerçek → çekim listesi |
| 5 | C28 | SÜR#3 00:30 | Kasada sandık yok | dünya/arka plan | 🅑 | G: "using the vault empty panel and the vault door and crate panel" — sandık cümlesi YOK | kare | C29-C31'de sabit sandık cümlesi var, C28'de yok |
| 6 | C29 | SÜR#4 00:40 · SÜR#6 00:50 · ANL#3 00:40 | Açık kapının ardında karlı/kayalık gezegen yüzeyi | dünya/arka plan | 🅑 | G: "At frame-left, just beyond the open doorway, one rigid sentry drone hovers level" — kapı ardı YOK | kare | C28'de yazılı: "shows a dim corridor beyond"; başka çekim yetmez |
| 7 | C30 | SÜR#5 00:50 · SÜR#9 01:10 | Drone'da yalnız C30'da çıkıntılı silindir namlu | ekipman/nesne biçimi | 🅑 | G: "its short front emitter pointing toward frame-right" / V: "a faint blue-white glow gathers at the emitter tip" — biçim/ölçü YOK | kare | C29/C32 önden, C30 yandan; üçünde de yalnız "short front emitter" |
| 8 | C32 | SÜR#9 01:10 | Drone kapıdan yeniden içeri süzülüyor (durum sıfırlanması) | durum sıfırlanması | 🅒 | C30 G: "hovers level in profile at frame-left in the vault's doorway" / C32 G: "hovers level at the center of the frame just inside the doorway" | — | drone C29-C32 boyunca kapı ağzında tasarlanmış; insan doğrulaması ? |
| 9 | C31 | SÜR#7 01:00 (LIKELY) | Kadının arkasında uzun koridor; dron görünmüyor | dünya/arka plan | 🅑 | G: "crouches behind a heavy rectangular graphite storage crate … which crosses the lower left of the frame" — arka plan YOK | kare | NOTLAR "kabul / açı değişimi"; mimari çapa yok |
| 10 | C31 | SÜR#8 01:00 · SÜR#10 01:20 | Sol kolda kalın teal bant yerine iki ince koyu şerit | giysi/işaret/arma/bant | 🅑 | G: "teal upper-arm bands" · "her left white glove is already resting on the pad" — sayı/genişlik/kol YOK | kare | C27 ve C33'te tek geniş bant görülmüş |
| 11 | C31 | SÜR#8 01:00 | Göğüs kutusu C27'dekinden küçük | ekipman/nesne biçimi | 🅑 | G: "the compact graphite core sits locked in her rigid chest carry harness" — ölçü YOK | kare | SÜR#2 C27'yi "small" diyor: rapor içi çelişki |
| 12 | C31 | ANL#4 01:02 · İZ-A5 01:02 | "Keep your visor down" bağlamsız; vizörler zaten kapalı | hikâye/anlatım | 🅒 | V: "she says … Keep your visor down." / G: "a fully clear closed pearl helmet" | — | plan R32; EMP parlaması K5'le görüntüden çıkarıldı |
| 13 | C32 | TAR#2 01:14-01:16 · İZ-A3 01:15 | İnen dronun üstünde kırmızı tepe lambası ("polis sireni") | ekipman/nesne biçimi | 🅑+ | G: "hovers level at the center of the frame just inside the doorway" / V: "the red lamp above the doorway pulses slowly over it" | hareket | kapı üstü lamba dronun tam üstünde; inişte açılıyor ya da kaynaşıyor |
| 14 | C33 | TAR#3 01:26-01:29 | Kamera kadına itiyor ("sabit olmalıydı") | kamera/kadraj | 🅒 | V: "the camera begins a slow dolly toward the console" | — | QA'ya "ne olmalı" verilmedi; itiş istenmiş (NOTLAR: kabul) |
| 15 | C33 | İZ-A4 01:22 | Panele basış çok mekanik, ifadesiz | diğer (oyunculuk) | 🅑 | V: "the woman presses the flat pad once with her glove" · "her eyes dropping to the red lamp" — tepki YOK | hareket | fiziksel tepki işareti yazılmamış |
| 16 | C34 | SÜR#11 01:30 | Yakında üç kolun ucu da teal; C33'te gri/teal/turuncu | ekipman/nesne biçimi | 🅑 | G: "Behind the lever the console's other two levers stand upright and softly out of focus" — renk YOK | kare | renk bilerek çıkarılmış ("renk adı yok"); C33'te mavi kol griye dönmüş |
| 17 | C35 | İZ-A7 01:40-01:50 | Durağan dış gemi planı sıkıcı | kamera/kadraj | 🅒 | V: "the camera stays locked on the ark and the gate" | — | K17 bilinçli: rijit dev yapıda kilitli kamera |
| 18 | C36 | SÜR#14 02:10 | Leon'un omzu beyaz (lacivert olmalı) | giysi/işaret/arma/bant | 🅐 | G: "in an ivory pressure suit with navy shoulders, orange upper-arm bands" · "using the back full-length panel" | kare | arkadan kare; insan doğrulaması ? |
| 19 | C36 | SÜR#14 02:10 | Leon sağ kolda iki turuncu şerit, C38'de tek bant | giysi/işaret/arma/bant | 🅑 | G: "orange upper-arm bands" — sayı/kol YOK | kare | ref sayfası: "narrow burnt-orange bands on both upper arms" |
| 20 | C36→C37 | SÜR#12 02:00 | Kadın sağ koltuktan sol koltuğa geçiyor | yön/180°/koltuk | 🅒 | C36 G: "from behind and slightly above the two seats … At frame-left an adult 38-year-old olive-skinned man" / C37 G: "She sits at frame-left in the engineer seat" | — | K19 ters açı; fiziksel koltuk aynı; NOTLAR hata saymış |
| 21 | C36 | SÜR#13 02:00 | Rhea sol kolda iki ince teal şerit, göğüste rozet yok | giysi/işaret/arma/bant | 🅑 | G: "teal upper-arm bands, a blue-gold geometric-sun badge" — bant sayısı, rozet konumu YOK | kare | arkadan çekimde önden panel ("harness with core panel") |
| 22 | C37 | İZ-A3 02:02 | Konuşurken kask içinde ağız kenarında yeşil ışık yanıp sönüyor | ışık | 🅑+ | V: "the wrist-link's soft cyan light rising with it" · "the cyan light staying plain and unmarked on her white glove" | hareket | yansımaysa davet; konuşma artefaktıysa 🅐 — insan doğrulaması ? |
| 23 | C38-C47 | İZ-B7 02:10+ | Kokpitte yavaş bakışma ve konuşma; tempo düşüyor | hikâye/anlatım | 🅑+ | C43 V: "A slow, small push-in begins as the man's helmet turns slowly" · "Her eyes come slowly around to meet his" | hareket | "slow" bu on videoda çekim başına 1-4 kez; kısmen çekim listesi |
| 24 | C39 | SÜR#15 02:20 · SÜR#16 02:30 · ANL#5 02:20 | Göğüsteki çekirdek yok; sonraki çekimde geri geliyor | ekipman/nesne biçimi | 🅑 | G: "framed from the top of her helmet down to her upper arms" · "using the face close-up panel" — çekirdek YOK | kare | not "kadraj omuzlara kadar" der; metin kollara kadar |
| 25 | C39 | SÜR#15 02:20 · SÜR#16 02:30 | Güneş arması göğüsten sol omza kayıyor | giysi/işaret/arma/bant | 🅑 | G: "her pearl pressure suit with the teal upper-arm bands and the blue-gold badge" — konum YOK | kare | G04'ün 12 çekiminde "badge sits on … left chest" yok |
| 26 | C40→C41 | SÜR#17 02:40 | Kadın soldan sağ (sancak) koltuğa geçiyor | yön/180°/koltuk | 🅒 | C40 G: "At frame-left in the engineer seat sits" / C41 G: "the camera behind and slightly to the left of the engineer seat" | — | K19 arka ¾; QA'nın "sancak" dediği zaten Rhea'nın koltuğu |
| 27 | C41 | SÜR#18 02:40 | Arma yine sol omuzda | giysi/işaret/arma/bant | 🅑 | G: "a blue-gold geometric-sun badge" · "using the left-profile close-up panel" — konum YOK | kare | sol profil panelinde göğüs rozeti yok |
| 28 | C42 | SÜR#19 02:50 · SÜR#21 03:00 | Leon sol koltukta; önden planda sağda olmalıydı | yön/180°/koltuk | 🅐 | G: "He sits at frame-right in the navy pilot seat" · "At the frame-left side of his waist, on his right hip" | kare | sahnedeki tek gerçek taraf hatası; SÜR#21 bunun yansıması |
| 29 | C42 | SÜR#20 02:50 | Kuş arması göğüs ortasında, büyük, sarı-altın | giysi/işaret/arma/bant | 🅑 | G: "his ivory pressure suit with the navy shoulders, orange upper-arm bands and blue-gold hawk badge" — konum/ölçü YOK | kare | G03 C27'de "his badge sits on his left chest" vardı |
| 30 | C42 | ANL#6 02:50 · İZ-A6 02:51 · İZ-B5 | Kadraj dışı kadın sesi telsizsiz, "iç ses" gibi; kimin konuştuğu belirsiz | replik tekrarı/ses | 🅐 | V: "a clear, quick adult woman's voice from out of frame, precise and controlled and softened by a light suit-radio filter, says" | ses | filtre istenmiş, duyulmamış; kadraj dışı olması tasarım |
| 31 | C42 | ANL#6 02:50 | Leon'un "kemer"le işi anlaşılmıyor; tether bağı okunmuyor | hikâye/anlatım | 🅑+ | G: "anchor block of his coiled navy safety tether is clipped to his belt" / V: "his eyes lift a little from his belt" | anlatım | "belt" üç kez; anlamı taşıyan nesne tether |
| 32 | C42 | İZ-A4 02:51 | Kemer tutarken aşırı abartılı yüz buruşturma | diğer (oyunculuk) | 🅑 | V: "his jaw tightens and his mouth stays closed" — yoğunluk YOK | hareket | — |
| 33 | C44 | TAR#4 03:14-03:18 · İZ-A3 03:15 | Vakumda gövdede atmosferik turuncu alev ve duman | parçacık/duman/alev | 🅑+ | V: "A low pulse of orange furnace light swells in place behind the blast ribs and washes across the underside of the ark's intact hull" | hareket | zayıf: C35'te aynı "swells in place" alev üretmedi |
| 34 | C44 | İZ-A6 03:11 | Vakum dış planında patlama/motor uğultusu | ortama aykırı ses | 🅐 | V: "The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static." | ses | iş emri: klip sesi yalnız replik penceresinde; montaj hat dışı |
| 35 | C44 | İZ-A6 03:11 · İZ-B5 | Replik telsizsiz "stüdyo kaydı"; kim, nereden konuşuyor belirsiz | replik tekrarı/ses | 🅒 | V: "a low, dry adult man's voice, calm and guarded, as a calm voice-over, says: I'm not making that choice again." | — | plan "LEON (VO)"; voice-over tasarım |
| 36 | C44 | SÜR#22 03:10 | Motorların arkasında dev turuncu yapı, alttan kafes | dünya/arka plan | 🅒 | G: "Behind the stern at frame-left, heavy blast ribs stand like a wall between the ark and the orange furnace trench, which glows bright orange" | — | fırın çukuru kıçın arkasında (FILM §3); C35 kıçı göstermiyordu |
| 37 | C45→C46 | SÜR#23 03:30 | Erkek sol, kadın sağ koltuğa geçiyor | yön/180°/koltuk | 🅒 | C45 G: "She sits at frame-left in the engineer seat" / C46 G: "At frame-left in the navy pilot seat, seen from behind, sits" | — | K19 arka ¾ |
| 38 | C46 | SÜR#24 03:30 | Göğüs/çekirdek kutusu görünmüyor | ekipman/nesne biçimi | 🅑 | G: "the graphite core-carry harness from it, using the left-profile close-up panel" — çekirdek YOK | kare | not "arkadan çekirdek görünmez" der; sol profil göğsü gösteriyor |
| 39 | C46 | SÜR#24 03:30 | Sağ kolda iki ince teal şerit | giysi/işaret/arma/bant | 🅑 | G: "teal upper-arm bands" · "seen in left profile with her mouth and cheek readable" — sayı/kol YOK | kare | sol profilde sağ kol görünmemeli; QA'nın tarafı da şüpheli |
| 40 | C46 | ANL#7 03:31 · TAR#5 03:32-03:35 · İZ-A5 03:33 · İZ-B5 | Başa "Seven's even" eklenmiş; "and release port" iki kez | replik tekrarı/ses | 🅐 | V: "she says … I feed the gate and release port. You take starboard from the ark." — "Seven's even" YOK | ses | vuruş aşırı yüklü (2 işaret + 5,0 s replik) — katkı olası |
| 41 | C46→C47 | SÜR#25 03:40 | Erkek sol koltuktan sağa geçiyor | yön/180°/koltuk | 🅒 | C46 G: "At frame-left in the navy pilot seat, seen from behind" / C47 G: "He sits in the navy pilot seat in the right half of the frame" | — | K19; arkadaki "pencerede gezegen" promptta yok, QA kusur demedi |
| 42 | C47 | TAR#6 03:41-03:44 · İZ-A5 03:41 · İZ-B5 | "We lose the core" iki kez söyleniyor | replik tekrarı/ses | 🅐 | V: "he says in a low, dry adult man's voice, calm and guarded: We lose the core. We take everyone." | ses | paralel yapının ilk yarısı yinelenmiş; kurguda kesilir |
| 43 | C48 | ANL#8 03:55 · TAR#7 03:56-03:59 · İZ-A1/A2/A3 · İZ-B4/B6 | Soldaki kapıdan kadının kopyası çıkıyor: üç kişi | klon/fazla kişi | 🅐 | G: "The two of them are the only people in the corridor." / V: "the woman toward the loading-bridge doorway at frame-left" | hareket | kadın açık kapının hemen yanında başlıyor (BILINEN §B9: kadraj) |
| 44 | C48 (parça sonu) | İZ-A1 · İZ-A8 · İZ-B4 | Çekirdeğin kapıyı açması gösterilmeden film bitiyor | hikâye/anlatım | 🅒 | V: "each takes one short, slow step toward their own open doorway" | — | QA yalnız 2. parçaya koştu; çözüm C58-C72'de |

### Ek A — kişi görünen çekimlerde koltuk/taraf ve işaret cümleleri (birebir, Görsel)

| çekim | kamera yönü | koltuk/taraf cümlesi | işaret cümlesi (bant · rozet · çekirdek) | QA ne gördü | hüküm |
|:--:|---|---|---|---|---|
| C27 | "at the middle of the vault's near wall, facing the far wall" | "At frame-right an adult 34-year-old olive-skinned woman …" · "At frame-left an adult 38-year-old olive-skinned man … stands in the open doorway in the vault's left wall" | "teal upper-arm bands, a blue-gold geometric-sun badge" · "her badge sits on her left chest" · "his badge sits on his left chest" · "the compact graphite core locked into her rigid chest carry harness" | SÜR#8: kalın teal bant, geniş göğüs kutusu (referans an) | tutmuş |
| C31 | "in front of a crouching figure" | "Her clear visor is turned in three-quarter toward frame-left." · "At frame-right a vertical graphite support strut rises beside her" | "teal upper-arm bands" · "her badge sits on her left chest, and the compact graphite core sits locked in her rigid chest carry harness" | sol kolda iki ince koyu şerit, küçük kutu | #10 #11 🅑 (rozet yazılı, kayma yok) |
| C33 | "in a front corner of the control room, looking diagonally across it" | "At frame-left, beside the window, an adult 38-year-old olive-skinned man … stands in rear three-quarter" · "At the console stands an adult 34-year-old …" | "her badge sits on her left chest" · "the compact graphite core locked in her chest harness" | iki kolda tek geniş teal bant (referans an) | tutmuş |
| C36 | "from behind and slightly above the two seats" | "At frame-left an adult 38-year-old … sits in the navy pilot seat" · "At frame-right an adult 34-year-old … sits in the engineer seat" | erkek: "navy shoulders, orange upper-arm bands, a blue-gold hawk badge" · kadın: "teal upper-arm bands, a blue-gold geometric-sun badge" · rozet konumu YOK | taraf ✓; Leon beyaz omuz + iki turuncu şerit; Rhea iki ince şerit, rozet yok | #18 🅐 · #19 #21 🅑 |
| C37 | "at eye level with the camera facing a seated woman" | "She sits at frame-left in the engineer seat" | "her pearl pressure suit with the teal upper-arm bands and the navy waist, the blue-gold badge" · konum YOK | kadın solda ✓; tek geniş bant, sol göğüste güneş arması | tutmuş (konum yazılmadan) |
| C38 | "at eye level with the camera facing a seated man" | "He sits at frame-right in the navy pilot seat" | "navy shoulders, orange upper-arm bands, a blue-gold hawk badge" · konum YOK | erkek sağda ✓; lacivert omuz, tek bant, sol göğüste kuş | tutmuş (konum yazılmadan) |
| C39 | "at eye level with the camera facing a seated woman" | "She sits in the engineer seat with her head in the left half of the frame" | "A narrow pale teal band circles her left upper arm at the lower frame-right edge." · "the blue-gold badge" konum YOK · çekirdek YOK | çekirdek yok; arma sol omuzda | #24 #25 🅑 (bant yazılı, bant kayması yok) |
| C40 | "at eye level with the camera facing the seats" | "At frame-left in the engineer seat sits … and at frame-right in the navy pilot seat sits …" | "The locked graphite core with its amber glass center rides in the harness over her chest" · rozet konumu YOK | kadın sol/erkek sağ ✓; çekirdek ve göğüs arması var | tutmuş |
| C41 | "behind and slightly to the left of the engineer seat" | "She sits in the engineer seat in the right third of the frame, seen in left profile from behind and to the left" | "a blue-gold geometric-sun badge" · "using the left-profile close-up panel" · konum YOK | kadın sağda (✓ tasarım); arma sol omuzda | #26 🅒 · #27 🅑 |
| C42 | "at eye level with the camera facing a seated man" | "He sits at frame-right in the navy pilot seat" · "At the frame-left side of his waist, on his right hip" | "his ivory pressure suit with the navy shoulders, orange upper-arm bands and blue-gold hawk badge" · konum/ölçü YOK | erkek SOL koltukta ✗; büyük sarı-altın kuş göğüs ortasında | #28 🅐 · #29 🅑 |
| C43 | "at eye level with the camera facing the seats" | "At frame-left in the engineer seat sits … and at frame-right in the navy pilot seat sits …" | "The locked graphite core with its amber glass center rides in the harness over her chest." · rozet konumu YOK | erkek sağ, kadın sol ✓ | tutmuş |
| C45 | "at eye level with the camera facing a seated woman" | "She sits at frame-left in the engineer seat" | "The locked graphite core rides in the harness over her chest" · rozet konumu YOK | kadın sol, göğüste güneş arması + kare kutuda çekirdek ✓ | tutmuş |
| C46 | "behind the seats and slightly to the left, looking forward over the pilot's left shoulder" | "At frame-left in the navy pilot seat, seen from behind, sits … and at frame-right in the engineer seat sits …" | "teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness" · çekirdek YOK | erkek sol/kadın sağ (✓ tasarım); çekirdek yok, sağ kolda iki ince şerit | #37 🅒 · #38 #39 🅑 |
| C47 | "at eye level with the camera facing a seated man" | "He sits in the navy pilot seat in the right half of the frame" | "navy shoulders, orange upper-arm bands, a blue-gold hawk badge" · konum YOK | erkek sağda ✓ | #41 🅒 |
| C48 | "standing in the pressurized ark corridor with the junction ahead" | "In the foreground at frame-left, beside the loading-bridge doorway, stands …" · "Far down the corridor at frame-right, beside the command doorway, stands …" | "the locked graphite core with its amber glass center rides in her harness" · "The two of them are the only people in the corridor." | taraf ✓; klon ✗ | #43 🅐 |

Rozet konumu yazılı 4 çekimde (C26 C27 C31 C33) rozet kayması **0**. Yazılı olmayan 12 çekimde (C36 + G04) **4** (C36 C39 C41 C42). Bant sayısı/kolu yalnız C39'da yazılı ve orada bant kayması yok. Sayısız "bands" yazılan çekimlerde 4 bant kayması var (C31 · C36 ×2 · C46). Küçük örnek, insan doğrulaması yok, ama yön belirgin.

## ÖZET

- **Sınıf (tekil 44):** 🅐 9 · 🅑 18 · 🅑+ 5 · 🅒 12 · 🅓 0.
- **🅑 oranı:** (18 + 5) / (9 + 18 + 5) = 23 / 32 = **%71,9** (sözleşme v1.0, sütun "sınıf", payda 🅐+🅑+🅑+). Yalnız geçerli ya da yarı geçerli kaynaklı (ANL/İZ) tekillerde: (5 + 5) / 17 = %59. Giysi/koltuk satırlarının hepsi geçersiz kaynaktan (SÜR 240 s) geliyor.
- **En sık 5 tür:**
  1. giysi/işaret/arma/bant 8 (🅐 1 · 🅑 7)
  2. ekipman/nesne biçimi 7 (🅑 6 · 🅑+ 1)
  3. yön/180°/koltuk 5 (**4'ü 🅒**, 1 🅐)
  4. hikâye/anlatım 5
  5. replik tekrarı/ses 5 (🅐 4 · 🅒 1)
- **Doğduğu yer:** kare 18 · hareket 8 · ses 5 · anlatım 1 · — 12.
- **Ses grubunda müdahale yeri prompt değil.** Beş 🅐 ses bulgusu (#1 #30 #34 #40 #42) ve C48 klonu (#43, kadraj) kurguda, kaynak seçiminde ve kadrajda çözülür. Hat dışı montaj klip sesini kapatmamış.

## PROMPT METNİNİN KENDİ KUSURLARI (24 çekimin Görsel + Video'su baştan sona okundu)

- **K1 · İşaret konumu cümlesi G03'te var, G04'te yok.**
  - G03: C26 · C27 · C31 · C33 "her badge sits on her left chest", C27 ayrıca "his badge sits on his left chest".
  - G04: 0/12, hem tur 1'de hem tur 1b'de.
  - Hat kuralı 12.10'dan beri var: `.claude/agents/goruntu-yonetmeni.md:38` "Asimetrik işaret hangi taraftaysa yazılır … Sayılabilir öğe rakamla yazılır". Uygulanmadı.
  - F5 devamlılık raporu "Rozet (sol göğüs) … görsellerde tutarlı" dedi: yokluğu çelişki saymadı.
- **K2 · Sayısız bant ve kelime kayması.**
  - Kadın, ref 2 sayfası: "narrow muted-teal bands on both upper arms" → kimlik tabanı "teal upper-arm bands" → C39 "A narrow pale teal band circles her left upper arm".
  - Erkek, ref 1 sayfası: "narrow burnt-orange bands on both upper arms" → "orange upper-arm bands".
  - Düşen ya da değişen kelimeler: *narrow · muted- · burnt- · on both · one*; eklenen *pale*. Model "tek geniş bant" ile "iki ince şerit" arasında gidip geliyor.
- **K3 · Rozet tarifi kısalıyor.** Ref sayfası: "a round blue-and-gold badge showing an abstract geometric sun on her left chest". Kimlik: "a blue-gold geometric-sun badge" (*round* ve *left chest* düştü). C37 anahtarı yalnız "the blue-gold badge" diyor.
- **K4 · Çekirdeğin ölçüsü hiçbir çekimde yok, kaynak paneli değişiyor.**
  - Tek sıfat "compact".
  - Panel: C25 `cradle close` → C26 `vault wide` (ref 10) → C27/C31/C33… `harness with core` (ref 2) → C45 `core object` (ref 10).
  - C39 · C41 · C46'da göğüs kadrajda, ama çekirdek cümlesi yok ve yüz/profil paneli seçilmiş. C39 notu "kadraj omuzlara kadar" diyor, metin ise "down to her upper arms".
- **K5 · Kokpit tarafı belgeler arasında çelişiyor.**
  - PROMPTLAR K19 kendi içinde tutarlı: "She sits at frame-left in the engineer seat", "He sits at frame-right in the navy pilot seat".
  - FILM §4 Taraf sütunu plan değerinde kalmış: C37 "orta Rhea sağ koltukta", C40/C43 "Leon solda, Rhea sağda", C38 "bakış sağa (Rhea kadraj dışı)". Paket de her K'da "Leon seat left, Rhea seat right" diyor.
  - Taraf yalnız frame-left/right ile yazılmış; sabit mimari çapa yok (GPT_IMAGE_OMNI §116).
  - Sahne içinde ön ↔ arka ¾ geçişi (C40→C41→C42, C45→C46→C47) her kesmede ekran yerini çeviriyor.
  - Sonuç: QA 4 yanlış alarm verdi, NOTLAR 16.10 kararı tasarımı hata sandı.
- **K6 · Ekran daveti (C37).** "its broad physical toggle unmarked and its face still turned toward her": cihazın *face*'i ekran gibi okunuyor. ANL: "bileğindeki ekrana bakarak". Notta "ekran ve harita yok" yazıyordu.
- **K7 · Işık kaynağı özneye biniyor.**
  - C32: "hovers level at the center of the frame just inside the doorway" + "The round red emergency lamp glows dull red on the wall above the doorway" + "the red lamp above the doorway pulses slowly over it" → tepe lambası (#13).
  - C37: "the wrist-link's soft cyan light rising with it" konuşma sırasında yüzün önünde (#22).
- **K8 · Vakum dış planında ateş çağıran fiiller (C44).** "the orange furnace trench, which glows bright orange" · "swells in place" · "washes across the underside of the ark's intact hull". Olumlu fiziksel kilit (katı kenarlı ışık, yanan yüzey yok) yazılmamış.
- **K9 · Anlamı taşıyan nesne yerine genel kelime (C42).** "is clipped to his belt" · "his brown eyes lowered toward his belt" · "his eyes lift a little from his belt". Dione repliğini taşıması gereken nesne tether; izleyici "kemer tokası" okudu.
- **K10 · Aşırı yüklü vuruş (C46).** "2-7 s: … the woman's outer glove lifts and points once … then the man's helmet turns … his outer glove lifts and points once … and lowers; her lips move only for her own line, and she says …". İki sıralı işaret ve 5,0 s'lik R49 (FILM §5) aynı 5 s'lik vuruşta. Notun kendisi "tavanda; sınırda" diyor.
- **K11 · "slow" yoğunluğu.** 24 video promptunun 23'ünde var (C35 hariç); C38-C47'de çekim başına 1-4 kez. C43'te dört kez: "A slow, small push-in begins as the man's helmet turns slowly", "Her eyes come slowly around", "One slow breath". Tempo kaybı (#23).
- **K12 · Açıklığın ardı ve arka plan çapası çekimden çekime düşüyor.**
  - C28 "the open doorway in the vault's left wall shows a dim corridor beyond" → C29 "just beyond the open doorway": kapının ardı yok.
  - C31'de arka plan yalnız ışık cümlesiyle anlatılıyor.
  - C28'de sandık yok, oysa kasa haritasına göre ("sandık kapıdan birkaç adım içeride") kadrajda olmalı.
- **K13 · Kadraj dışı replik, kadrajda tek kişi.** C26 "her lips staying closed, and from out of frame a low, dry adult man's voice …" ve C42 aynı yapıda. Model sesi alıcı sesini kadrajdaki ağza verebiliyor (REPLIK §1 riski). C26'da iki cümlelik R28 ikiye bölündü ve tekrar edildi.
- **K14 · Panel ile açı uyuşmuyor.** C36 arkadan çekim, ama kadın için "using the harness with core panel" (önden panel). C34 eldiven için "front full-length panel" (askı boş) kullanıyor; zararsız.
- **K15 · Zihinsel ifade.** C39 V: "her guarded eyes" · "until her look is steady and resolved"; C47: "his steady eyes". Küçük.
- **Temiz olanlar:** Meta etiket, kişi adı ve "EMP" gövdelerde 0. Uzunluk: Görsel 1.172-2.772 karakter (en uzun C46, 5 referans), Video 794-1.147; hepsi ≤4.300. Referans anahtarı 24/24, roller ROL SÖZLÜĞÜ ile birebir. Aynı replik iki promptta yok. Replik tekrarını çağıran yapı yalnız R50'nin paralel kuruluşu ("We lose the core. We take everyone.").

## HAT KURALLARI BU FİLMDE (C25-C48)

| kural | kaç çekimde yazılı | yine de bulgu (tekil) |
|---|---|---|
| ORTAK GÖRÜNÜM cümlesi birebir | 48/48 blok (24 G + 24 V) sonunda birebir | 0 (stil/ışık kesme bulgusu yok) |
| "Reference <No>" anahtarı | 24/24 Görsel; roller ROL SÖZLÜĞÜ ile birebir | 2. Panel seçimi (yüz/profil) çekirdeği düşürdü: #24 #38 |
| asimetrik işaret (hangi kol, kaç bant) | bant kol+sayı 1/24 (C39) · rozet konumu 4/24 (G03; G04 0/12) | 8 giysi tekili (#10 #18 #19 #21 #25 #27 #29 #39). Rozet kaymalarının 4/4'ü konum yazılmayan çekimde |
| koltuk/taraf | kişi görünen 18 çekimin 18'inde konum cümlesi; kokpit 11/11 | 5 S3 satırı → 4 🅒 (K19 ters açı) + 1 🅐 (C42) |
| 10 s vuruş planı | 24/24 (0→10, boşluksuz, 2-4 vuruş) | 2 dolaylı: #23 tempo · #40 aşırı yüklü vuruş katkısı |
| model sesi / replik satırı | 22/24 (C30, C32 replik yok); telsiz eki 7 (C25 C26 C28 C34 C35 C36 C42), VO 1 (C44) | 5 ses tekili: 4 🅐 (#1 #30 #40 #42) + 1 🅒 (#35) |
| vakum ses/parçacık kuralı | dış 2/2 (C35, C44) "non-diegetic pressure tone"; iş emri C44 "klip sesi yalnız replik penceresinde" | 2: #33 alev/duman (🅑+) · #34 vakum sesi (🅐, montaj kuralı uygulanmadı) |
| yazı/bayrak olumlu kilidi ("the only marking") | "the only marking" 0/24 · "unmarked/plain" 6 çekim (C29 C30 C31 C33 C34 C37) | yazı/bayrak/yeni arma 0; arma yer/ölçü kayması 3 (#25 #27 #29) |

## DERS ADAYLARI (aday; karar sahibin)

1. **Prompt yazarken: kol bandını ve rozeti sayı ve tarafla, referans sayfasının kelimeleriyle yaz** ("one narrow muted-teal band around each upper arm" · "the round blue-and-gold sun badge on her left chest"). Bu ek cümleyi kolun ya da göğsün göründüğü her çekimde tekrarla.
   - Dayandığı: #10 #19 #21 #25 #27 #29 #39. Bu filmde ≤7 bulguyu kapatırdı.
   - Zaten hat kuralı: `goruntu-yonetmeni.md:38` (12.10) + `KIMLIK_VE_REFERANS_KILAVUZU` (16.10). Kural var, uygulanmadı. Müdahale yeri devamlılığın F5 kontrolü: "işaret konumu cümlesi her çekimde var mı" maddesi.
2. **Prompt yazarken: göğüs kadrajdaysa taşınan nesnenin durumunu ve ölçüsünü metne yaz.** Yüz ya da profil paneli seçilse bile; çekirdek tek bir referans panelinden gelsin.
   - Dayandığı: #3 #11 #24 #38. 4 bulguyu kapatırdı.
   - Yeni. T09 "durum merdiveni" yalnız var/yok diyordu, kadraj/panel ilişkisine bakmıyordu.
3. **Prompt yazarken: kapının/pencerenin ardını ve kişinin arkasındaki duvarı her çekimde aynı sabit mimari cümleyle yaz.** Komşu çekimde yazılı olması yetmez.
   - Dayandığı: #5 #6 #9. 3 bulguyu kapatırdı.
   - Kısmen hat kuralı: `GPT_IMAGE_OMNI_KILAVUZU` §116 "sabit mimari çapa" (16.10, bu promptlardan sonra).
4. **Prompt yazarken: ışık kaynağını öznenin tam üstüne ya da konuşan ağzın önüne koyma; hareketle oraya taşıma.**
   - Dayandığı: #13 #22. 2 bulguyu kapatırdı.
   - Yeni (K11 "vizörde kayan ışık yok"un genişlemesi).
5. **Prompt yazarken: anlam taşıyan nesneyi kendi adı ve okunur parçasıyla öne çıkar; genel giysi kelimesini (belt) tekrar etme.**
   - Dayandığı: #31. 1 bulguyu kapatırdı. Yeni.
6. **Prompt yazarken: diyalog vuruşuna tek taşıyıcı olay koy.** ≥4 s'lik replikte jestleri ayrı vuruşa al; "slow"u çekim başına bire indir.
   - Dayandığı: #23 · #40 (🅐, yalnız katkı).
   - #23'ü kapatırdı. #40 ve #42'deki takılmanın müdahale yeri kurgu: aynı klibin başka denemesi, sonra kayıt (`REPLIK_VE_KLIP_SESI_KILAVUZU` §3).
   - Kısmen hat kuralı (K9 taşıyıcı olay).
7. **Prompt yazarken (ve FILM §4 Taraf sütununda): kokpit tarafını kamera yönüyle birlikte yaz** ("seen from the front: the woman at frame-left in the engineer seat"). §4, NOTLAR ve prompt aynı kuralı taşısın. Aynı sahnede ön ↔ arka ¾ geçişini en aza indir.
   - Dayandığı: #20 #26 #37 #41 (QA ve NOTLAR yanılgısı) · #28.
   - Model bulgusu kapatmaz; 4 yanlış alarmı ve yanlış KARARLAR maddesini önlerdi. #28 (🅐) için müdahale yeri kare kapısında taraf denetimi.
   - Kısmen hat kuralı: `SECIM_VE_KURGU` §61 "Eksen aşılacaksa yeni coğrafya görünür kurulur" (16.10).
8. **Prompt yazarken: kadrajda tek kişi varken kadraj dışı repliği model sesine yazma; FILM §5 Kaynak'ı kayıt ya da telsiz kaydı yap.**
   - Dayandığı: #1 #30 (ikisi de 🅐). Müdahale yeri F4 Kaynak seçimi + kurgu, prompt değil.
   - Aynı ailede #34 vakum sesi: hat dışı montajda klip izi kapalı başlar, yalnız replik penceresi açılır.
   - Zaten hat kuralı: `REPLIK_VE_KLIP_SESI_KILAVUZU` §1 · §2 madde 6-7 · §4 (16.10).
