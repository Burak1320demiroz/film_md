# 🖼️ THE_FURNACE_GATE — Prompt grubu G03 (çekimler C25–C36)

> Yazan: goruntu-yonetmeni (faz 5, tur 1). Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K25–K36 (sahibin planı, birebir) + `FILM.md` §3 · §4 · §5. Bu dosya yeniden tasarım değil, **biçim çevirisidir**:
> kompozisyon, olay, kamera hareketi, tasarım ve replik planındır; yalnız hat biçimi uygulandı (numaralı referans anahtarı · 10 s vuruş planı · olumsuz blok yok · zincir/atıf dili yok ·
> araç/oran/süre etiketi yok · ortak görünüm + mekân ışığı + mekân ortam sesi cümlesi birebir · model sesi replikleri video promptunda).
> Prompt gövdesine çekim kodu, referans kodu, "Clip n of N", başlık satırı YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. **Karakter adı prompta yazılmaz** (`the man` / `the woman`; büyük harfli ad kadraja basılır, BILINEN_TUZAKLAR §C).
> Kelime güvenliği (BILINEN_TUZAKLAR §A): "body", "dead", "blood", "wound", milliyet hiçbir promptta geçmez (torso · casing · hull yazıldı). FILM.md §3'ün `front / side / back full-body panel` adları, aynı panelleri gösteren
> `full-length panel` olarak yazıldı (sayfada etiket yok, model yalnız görseli okur; panel kimliği değişmedi). Her blok ≤4.300 karakter.
>
> **Referans dosyaları (`FILM.md` §3) ve rol etiketleri (bu grupta):** `ref/1.LEON_v1.png` "man" · `ref/2.RHEA_v1.png` "woman" · `ref/4.KOKPIT_v1.png` "tug cockpit" · `ref/5.FOUNDRY_v1.png` "foundry" · `ref/6.ARK_v1.png` "ark" ·
> `ref/10.CEKIRDEK_v1.png` "core" · `ref/11.DRONE_v1.png` "drone" · `ref/12.KONTROL_ODASI_v1.png` "control room" · `ref/15.ARACLAR_v1.png` "tools". Referans sayfalarının promptları G01'dedir (bu grupta yazılmaz).
> **Paneller (FILM.md §3 adlarıyla; çekimde her referanstan yalnız TEK panel):** ref 1 → front full-body (C27) · side full-body (C29) · back full-body (C33 · C36) ·
> ref 2 → front full-body (C26 · C34) · `harness with core panel` (C27 · C31 · C33 · C36) · ref 4 → `wide interior panel` (C36) · ref 5 → `wide exterior panel` (C35) · ref 6 → `side view panel` (C35 · C36) ·
> ref 10 → `cradle close panel` (C25) · `vault wide panel` (C26-C32) · ref 11 → `drone front panel` (C29 · C32) · `drone side panel` (C30) · ref 12 → `wide room panel` (C33) · `console close panel` (C34) · ref 15 → `emp puck panel` (C31).
> **Ortak sabitler (FILM.md §3, birebir):** ORTAK GÖRÜNÜM her görsel ve video promptunun SONUNDA. MEKÂN IŞIĞI görselde "The light is …" kalıbıyla: KASA (C25-C32) · KONTROL ODASI (C33 · C34) · DIŞ (C35) · KOKPİT (C36).
> ORTAM SESİ video promptunda, vuruşlardan sonra, ortak görünümden önce: KASA · KONTROL ODASI · DIŞ · KOKPİT cümleleri FILM.md §3'ten.
> **KASA ışığı — tek kontrollü sapma:** FILM.md KASA cümlesinin ikinci yarısı ("the warm amber glow of the core's glass center") çekirdeğin kadrajda olduğu C25 · C26 · C27 · C31'de birebir yazıldı. Çekirdeğin kasada ve kadrajda olmadığı C28 · C29 · C30 · C32'de yalnız
> ilk yarı ("low amber lamps on graphite walls") birebir yazıldı, çekirdek ışığı çıkarıldı: boş beşikli karede "çekirdeğin parlayan merkezi" ışığı, T09'a (tek çekirdek, boş beşikte kopya yok) karşı zıt iki istek olurdu. Fable kararı: FILM.md §3'e "KASA (çekirdek kadrajda yokken)" varyantı eklenebilir.
> **Kasa haritası (C25-C32, kameradan okunur):** giriş kapısı kasanın SOL duvarında (kadrajın solu), saklama beşikleri karşı (uzak) duvarda (kadrajın sağı), kırmızı acil lamba kapının üstünde, tek ağır sandık kapıdan birkaç adım içeride cıvatalı.
> Sandık sabit cümlesi (C29 · C30 · C31, birebir): "a heavy rectangular graphite storage crate bolted to the grated floor, as tall as a crouching person's shoulders, with plain unmarked faces and a dark steel top edge". Sandık hiçbir referansta yok; tutarlılığı yalnız bu cümle taşır.
> **Ses tarifleri (FILM.md §3 SES KİMLİĞİ, her replikte aynı):** Leon `a low, dry adult man's voice, calm and guarded` · Rhea `a clear, quick adult woman's voice, precise and controlled` · telsiz eki `softened by a light suit-radio filter`.
> Konuşan kadrajdaysa ağzı yalnız kendi cümlesinde hareket eder, diğerinin ağzı kapalı yazıldı. Replik biçimi: iki nokta (`… says: <line>`); iki biçim de `film_dogrula` için geçerli, SMOKE P9 karar verir.
> **Replik saniyeleri `FILM.md` §5 ile uyumlu** (hiçbiri geçiş aralığına, ilk/son 1 s'ye düşmüyor); §5'te değişiklik gerekmez.
> **Referans çıkarmaları (FILM.md §4 başlığı izin veriyor, gerekçeli):** C27 ve C28'den 15.ARACLAR (araçlar giysi sayfalarında zaten var, kadrajda ayrı araç yok) · C33 ve C34'ten 10.CEKIRDEK (çekirdek `harness with core panel`'den gelir; C34'te kadrajda yok) · C36'dan 5.FOUNDRY ve 10.CEKIRDEK (kanopide yalnız ark gövdesi; çekirdek `harness with core panel`'den).
> **T01 uyarlaması (tek):** C31'de planın "glove presses the pad" hareketi için eldiven ilk karede pedin ÜSTÜNDE başlar (temas kurulu); C33'te de pede eldiven ilk karede oturur. Plan metni değişmedi, yalnız temas başlangıç karesine alındı.
> **Vuruş iskeletleri çekimden çekime farklı** (tempo düzlüğü, PROMPT_HATA_ATLASI karantina): C25 0-3·3-8·8-10 · C26 0-4·4-8·8-10 · C27 0-4·4-7·7-10 · C28 0-4·4-6·6-10 · C29 0-4·4-7·7-10 · C30 0-3·3-6·6-10 ·
> C31 0-4·4-8·8-10 · C32 0-4·4-6·6-10 · C33 0-4·4-7·7-10 · C34 0-4·4-8·8-10 · C35 0-4·4-7·7-10 · C36 0-4·4-8·8-10. Her ilk vuruş hareketle başlar, hiçbir son vuruş donmaz.

---

## C25 — Çekirdeği tutan mandal açılır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · VİDEO (Frames to Video): yalnız kare/C25.png
```

> Not: Plan K25. Replik R27 (Rhea, telsiz, kadraj dışı, 1.5 s): "Release catch." — 0-3 s vuruşunda. Kadrajda kimse yok, el yok; tek hareket mandalın dışa dönmesi.
> Menteşe tarafı kadrajın SOLUNDA yazıldı (asimetrik işaret): ref 10 `cradle close panel`'de menteşe solda olmalı; sayfada ters çıkarsa Görsel promptundaki "frame-left" tek kelimeyle ayrılır.
> Boş kadrajda telsiz sesi kişi çağırabilir (A08/A10): ses "from out of frame" + telsiz filtresiyle yazıldı; kadrajda zamir yok.

### Görsel
```text
Reference 10 (core): take the graphite vault wall, the open storage cradle with its single hinged retaining latch, and the compact rectangular graphite core with its ivory corner guards, amber glass center and rigid carry handle from it, using the cradle close panel. Close view on an 85 mm lens, the camera at the height of the cradle and a short way in front of it, level and looking straight at it. The open storage cradle holds the compact rectangular graphite power core, its ivory corner guards at the corners of the casing, its amber glass center glowing and its single rigid carry handle running across the top. One broad retaining latch, hinged at frame-left, rests closed across the carry handle. Every edge of the casing is intact and the core sits fully seated. Plain graphite vault walls recede softly behind the cradle. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: the camera begins a slow, steady push-in toward the cradle, and from out of frame a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says: Release catch. 3-8 s: the single retaining latch starts to rotate outward on its hinge, lifting clear of the rigid carry handle, then swings on away from the core. 8-10 s: it reaches its hinge stop and stands open beside the cradle as the push-in arrives at its closest point, while the core, its handle and its casing stay seated and unmoved. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C26 — Çekirdek beşikten kalkar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · VİDEO (Frames to Video): yalnız kare/C26.png
```

> Not: Plan K26. Replik R28 (Leon, telsiz, kadraj dışı, 1.5 s): "Careful. That's worth more than the tug." — 0-4 s vuruşunun sonunda; kadrajdaki kadının ağzı kapalı (video promptunda yazılı).
> T01/T02: iki eldiven kavrayışı ilk karede kurulu; tek kısa dikey kaldırma, yeniden kavrama ve gövde dönüşü yok. T09: tek çekirdek, göğüs askısı BOŞ (çekirdek askıya girmez; kaldırma askının altında biter).
> Beşiğin tutucu mandalı C25'in sonundaki gibi açık (kadrajın solunda). Ref 2 front full-body paneli askının boş hâlini taşır. Efor: omuz ve kol kadrajda, sabitlik sözcüğü yok (PROMPT_HATA_ATLASI A01 · A02).

### Görsel
```text
Reference 2 (woman): take her face, braid, pearl suit and chest harness from it, using the front full-length panel. Reference 10 (core): take the graphite vault, the open storage cradle and the core with its ivory corner guards, amber glass center and rigid carry handle from it, using the vault wide panel. Medium shot on a 50 mm lens, the camera at chest height facing the woman across the open storage cradle, which sits at the lower center of the frame: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, stands bending slightly forward over it. She wears white gloves, and the badge sits on her left chest. Her gaze is lowered through the clear visor to the core, her lips closed and the small scar on her right chin visible. One white glove is already wrapped around the core's rigid carry handle and the other white glove is cupped under the casing's edge, the compact graphite core still seated in the cradle with its amber glass center glowing; the cradle's retaining latch stands open at frame-left. The carry harness on her chest is empty. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow push-in toward her as she draws a short breath and braces her arms under the core, her shoulders beginning to take its weight and her lips staying closed, and from out of frame a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says: Careful. That's worth more than the tug. 4-8 s: she lifts the single core straight up out of the cradle in one slow, effortful lift, both gloves keeping the same grips as the casing clears its supports. 8-10 s: the lift ends with the core held just clear above the empty cradle, its amber center lighting her visor, her torso square to the camera, her mouth closed and her chest harness empty. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C27 — Çekirdek göğüs askısında güvende, kırmızı lamba yanar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · VİDEO (Frames to Video): yalnız kare/C27.png
```

> Not: Plan K27. Replik R29 (Rhea, ağız kadrajda, 1.5 s): "The core is secure." — 0-4 s vuruşunda; Leon'un ağzı kapalı. Leon solda (kapıda), Rhea sağda, boş beşikler arkada.
> T09: çekirdek Rhea'nın göğüs askısında kilitli; beşik boş. T01: eldiven askının mandalı üzerinde ilk karede; video yalnız tek basışı yazar. Kırmızı lamba kapının üstünde zaten var, sönük başlar ve parlar ("rising").
> Kamera ve harita C28 ile aynı yerde: karşı duvara bakar, kapı solda. Ref 15 çıkarıldı (başlık notu).

### Görsel
```text
Reference 1 (man): take his face, ivory suit, navy shoulders, orange upper-arm bands and helmet from it, using the front full-length panel. Reference 2 (woman): take her face, braid, pearl suit, helmet and the chest harness with the locked core from it, using the harness with core panel. Reference 10 (core): take the graphite vault walls, the empty rigid storage cradles and the low amber lamps from it, using the vault wide panel. Medium-wide two-shot on a 35 mm lens, the camera at chest height at the middle of the vault's near wall, facing the far wall. At frame-right an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet stands in front of the empty rigid storage cradles on the far wall, the compact graphite core locked into her rigid chest carry harness with its amber glass center glowing. She wears white gloves; one glove already rests on a broad latch at the upper edge of the harness, and her badge sits on her left chest. Her clear visor is turned in three-quarter toward the man. At frame-left an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet stands in the open doorway in the vault's left wall, turned toward her. He wears white gloves, and his badge sits on his left chest. A red emergency lamp on the wall above the doorway glows only faintly. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow push-in as the woman presses the harness latch once with her glove, keeping her eyes on the man, and says in a clear, quick adult woman's voice, precise and controlled: The core is secure. Her lips shape each word clearly while the man's mouth stays closed. 4-7 s: the man turns his helmet slowly away from her toward the red emergency lamp above the doorway as the lamp brightens from a faint glow to a steady red. 7-10 s: the red light spreads across his visor and the doorway frame, and the woman's gaze follows his toward the lamp, her mouth closed, as the push-in ends on the two of them. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C28 — Boş kasa, kırmızı lamba atmaya başlar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · VİDEO (Frames to Video): yalnız kare/C28.png
```

> Not: Plan K28. Replik R30 (Leon, telsiz, kadraj dışı, 1.5 s): "That woke the security grid." — 0-4 s vuruşunun sonunda. Kadrajda kimse yok; zamir yazılmadı (A08).
> T09: beşikler BOŞ, giriş açık; kapı geometrisi değişmez. Kamera C27 ile aynı yerde (karşı duvara bakar, kapı solda), insanlar kadraj dışında. Işık: KASA'nın ilk yarısı + kırmızı lamba (çekirdek ışığı çıkarıldı, dosya başı notu).
> Ref 15 çıkarıldı (başlık notu). Ref 10 sayfasında çekirdek beşikte görünse bile metin "beşikler boş" der; kare üretiminde beşikte çekirdek çıkarsa kare yeniden alınır.

### Görsel
```text
Reference 10 (core): take the graphite vault walls, the rigid storage cradles and the low amber lamps from it, using the vault wide panel. Wide symmetrical view on a 24 mm lens, the camera at chest height at the center of the vault's near wall and looking straight across the room at the far wall. The rigid storage cradles on the far wall at frame-right stand open and empty, their retaining latches swung out beside them. At frame-left the open doorway in the vault's left wall shows a dim corridor beyond, and a single red emergency lamp on the wall above it glows a dull, steady red. Amber lamps run along the graphite walls above a clean grated floor, and the room is quiet and empty. The light is low amber lamps on graphite walls, with one dull red emergency lamp above the doorway. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow push-in along the room's center line, and from out of frame a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says: That woke the security grid. 4-6 s: the red emergency lamp above the doorway starts to pulse slowly, its red light swelling and fading across the doorway frame. 6-10 s: the pulses carry on, washing the near floor grating and the empty storage cradles with a faint red glow in slow waves, while the doorway, the amber lamps and the walls stay fixed as the push-in draws toward its end. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C29 — Drone kapıda, Leon siperde

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/10.CEKIRDEK_v1.png · ref/11.DRONE_v1.png · VİDEO (Frames to Video): yalnız kare/C29.png
```

> Not: Plan K29. Replik R31 (Leon, ağız kadrajda, 1.5 s): "Down." — 0-4 s vuruşunda; yüz geniş planda küçük ama görünür (sandığın üstünde, ¾ kapıya dönük). Leon sandığın ARKASINDA çömelmiş başlar ve çömelmiş kalır.
> Drone kapının hemen DIŞINDA başlar ("at the doorway"), video kapı açıklığına kısa süre ilerletir. Drone rijit; ateş yok; egzoz/duman yazılmadı (jetler anılmaz). Kırmızı şerit içeri dönük.
> Sandık referanslarda yok: dosya başındaki sabit cümle C30 ve C31 ile birebir. Çömelme (A04): kısa, tek duruş; Leon'un hareketi yalnız kaskın hafifçe inmesi.
> Işık: KASA'nın ilk yarısı + drone şeridinin kırmızı ışığı (çekirdek kadrajda yok).

### Görsel
```text
Reference 1 (man): take his face, ivory suit, navy shoulders, orange upper-arm bands and helmet from it, using the side full-length panel. Reference 10 (core): take the graphite vault walls, the grated floor and the low amber lamps from it, using the vault wide panel. Reference 11 (drone): take the rigid compact graphite rectangular casing, the narrow red sensor strip and the short front emitter from it, using the drone front panel. Wide shot on a 35 mm lens, the camera at chest height at the middle of the vault's near wall, facing the far wall. Right of center in the frame an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet crouches low behind a heavy rectangular graphite storage crate bolted to the grated floor, as tall as a crouching person's shoulders, with plain unmarked faces and a dark steel top edge. He wears white gloves; his helmet and shoulders rise above the crate's top edge and his clear visor is turned in three-quarter toward the doorway. At frame-left, just beyond the open doorway in the vault's left wall, one rigid sentry drone hovers level, its narrow red sensor strip aimed inward across the room toward the crate. The rigid storage cradles on the far wall stand empty. The light is low amber lamps on graphite walls, with a thin red glow from the drone's sensor strip. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow drift to the right, and the sentry drone starts to slide forward toward the doorway opening on a level path while the man lowers his helmet a little behind the crate's top edge and says in a low, dry adult man's voice, calm and guarded: Down. 4-7 s: the drone slides on until it fills the doorway opening, its red strip casting a thin red line across the floor grating toward the crate, and the man's mouth stays closed as his visor follows it. 7-10 s: the thin red light climbs the front of the crate and reaches his visor as the drone completes its short advance into the doorway, while he stays crouched behind the crate. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C30 — Drone sandığın kenarına tek atım yapar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · ref/11.DRONE_v1.png · VİDEO (Frames to Video): yalnız kare/C30.png
```

> Not: Plan K30. Replik yok (konuşma/ses tarifi yazılmadı). Atış ve insan tepkisi ayrı planlarda: kadrajda insan yok, sandığın arkasında kimse anılmaz.
> Tek kısa kurgusal atım sandığın üst kenarına; küçük kıvılcımlar bir avuç genişliğinde söner, patlama yok. Kasa basınçlıdır (kıvılcım havada), vakum değil. "Fire/shot" yerine "pulse" · "line of aim". Drone C29'daki kapı konumunda, sandık sabit cümleyle C29 ile aynı.
> Işık: KASA'nın ilk yarısı + şeridin zayıf kırmızı ışığı.

### Görsel
```text
Reference 10 (core): take the graphite vault wall, the grated floor and the low amber lamps from it, using the vault wide panel. Reference 11 (drone): take the rigid compact graphite rectangular casing, the short front emitter and the narrow red sensor strip from it, using the drone side panel. Close side view on an 85 mm lens, the camera at the height of the emitter and a few steps to the side of the drone's path. The rigid sentry drone hovers level in profile at frame-left in the vault's doorway, its matte scratched graphite flank filling the left third of the frame and its short front emitter pointing toward frame-right, the narrow red sensor strip glowing faintly at its front end. At frame-right a heavy rectangular graphite storage crate bolted to the grated floor, as tall as a crouching person's shoulders, with plain unmarked faces and a dark steel top edge, stands a short distance ahead of the emitter with its top edge in the line of aim. The vault wall and its low amber lamps glow softly out of focus behind. The light is low amber lamps on graphite walls, with a thin red glow from the drone's sensor strip. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: the camera begins a slow glide forward along the drone's flank toward its emitter as a faint blue-white glow gathers at the emitter tip. 3-6 s: the emitter releases one brief fictional blue-white pulse across the gap into the crate's top edge, and a few small sparks jump from the dark steel and fade within a hand's width. 6-10 s: the glow at the emitter dies away and the struck edge of the crate glows dull orange for a moment before darkening, while the drone stays level and rigid and the glide carries on to the emitter. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C31 — Rhea EMP diskine basar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C31.png
```

> Not: Plan K31. Replik R32 (Rhea, ağız kadrajda, 1.5 s): "Keep your visor down." — 0-4 s vuruşunda. EMP kurgusal; yalnız göstergenin parlaması, patlama/darbe yok (etki C32'de).
> T01 uyarlaması: eldiven ilk karede pedin üzerinde (dosya başı notu). Disk "yakındaki metal desteğe" takılı: kadrajın sağında dikey grafit destek; hangi koldan uzandığı yazılmadı (kadraja bakan gövdede sağ/sol karışmasın), kol omuzdan desteğe uzanır.
> T09: çekirdek askıda, amber merkez yanık. Işık: KASA tam cümle (çekirdek kadrajda). Sandık sabit cümleyle C29 · C30 ile aynı.

### Görsel
```text
Reference 2 (woman): take her face, braid, pearl suit, helmet and the chest harness with the locked core from it, using the harness with core panel. Reference 10 (core): take the graphite vault walls, the grated floor and the low amber lamps from it, using the vault wide panel. Reference 15 (tools): take the small matte grey puck with its amber indicator and broad flat activation pad from it, using the emp puck panel. Medium shot on a 50 mm lens, the camera at chest height in front of a crouching figure: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet crouches behind a heavy rectangular graphite storage crate bolted to the grated floor, as tall as a crouching person's shoulders, with plain unmarked faces and a dark steel top edge, which crosses the lower left of the frame. She wears white gloves, her badge sits on her left chest, and the compact graphite core sits locked in her rigid chest carry harness with its amber glass center glowing. Her clear visor is turned in three-quarter toward frame-left. At frame-right a vertical graphite support strut rises beside her, and a small matte grey EMP puck is attached to it at shoulder height, its single broad flat activation pad facing her and its amber indicator dark; one white glove is already resting on the pad, the pearl sleeve reaching it from her shoulder. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow push-in as the woman turns her visor toward frame-left and says in a clear, quick adult woman's voice, precise and controlled: Keep your visor down. 4-8 s: her glove presses the puck's broad activation pad in one firm press, her arm and shoulder tensing, and the puck's amber indicator begins to brighten. 8-10 s: the amber indicator reaches a bright steady glow that tints the strut and the crate's top edge while she stays low behind the crate and the push-in ends. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C32 — Drone devre dışı kalır, zemine iner

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · ref/11.DRONE_v1.png · VİDEO (Frames to Video): yalnız kare/C32.png
```

> Not: Plan K32. Replik yok (konuşma/ses tarifi yazılmadı). Parçalanma yok: "casing and shape intact" pozitif yazıldı. Kırmızı şerit titreşerek başlar, söner; drone ızgara zemine yavaşça iner (ayak/zemin teması yalnız iniş anında, drone yatay kalır).
> Disk kadrajın dışında; "faint amber reflection from the puck" kadraj dışı küçük bir ışık kaynağı olarak yazıldı (diskin kendisi görünmez, ref 15 eklenmedi). Kamera kapıya karşıdır (C29-C31'den ters açı, aynı kasa).
> Ref 11 `drone front panel` başlangıç durumu (şerit yanık) taşır; son durum (karanlık, ızgarada bütün) metindedir.

### Görsel
```text
Reference 10 (core): take the graphite vault walls, the grated floor and the low amber lamps from it, using the vault wide panel. Reference 11 (drone): take the rigid compact graphite rectangular casing, the narrow red sensor strip, the two recessed maneuver jets and the short front emitter from it, using the drone front panel. Medium shot on a 35 mm lens, the camera at chest height inside the vault facing the open doorway in its left wall: the rigid sentry drone hovers level at the center of the frame just inside the doorway, its matte scratched graphite casing facing the camera, its narrow red sensor strip flickering unevenly and its two recessed jets dark, about a meter above the grated floor. A faint amber reflection from a small light out of frame at frame-right glints along its flank. The doorway's frame and the vault wall with its low amber lamps stand softly around it. The light is low amber lamps on graphite walls, with a flickering red glow from the drone's sensor strip. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow push-in toward the doorway as the drone's red sensor strip flickers unevenly and the drone sags a little in the air. 4-6 s: the red strip fades out and the drone, its casing and shape intact, begins to sink slowly toward the grated floor. 6-10 s: the drone settles gently onto the grating, level, its strip dark, as the faint amber glint slides along its graphite flank and the push-in ends. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C33 — Yerel override kilitli

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C33.png
```

> Not: Plan K33. Replik R33 (Rhea, ağız kadrajda, 1.5 s): "Local override is locked out." — 0-4 s vuruşunun sonunda; Leon pencerede arkadan ¾, ağzı görünmez, yeni hareketi yok.
> T09: çekirdek Rhea'nın askısında, giriş yuvası boş; üç kol dik (mavi · teal · turuncu, görselde bir kez nesneye bağlı yazıldı, videoda renk adı tekrarlanmaz, §C). Uyarı lambası kırmızı başlar ve kırmızı kalır; pencerede üç kepenk kısmen kapalı.
> T01 uyarlaması: eldiven ilk karede pedin üzerinde. Pad ve kol yüzeyleri yazısız ("unmarked"). Leon arkadan olduğu için yalnız görünen kimlik parçası yazıldı (kimlik tabanının yüz ve rozet kısmı çıkarıldı). Ref 10 çıkarıldı (başlık notu).

### Görsel
```text
Reference 1 (man): take his ivory suit, navy shoulders, orange upper-arm bands and helmet from it, using the back full-length panel. Reference 2 (woman): take her face, braid, pearl suit, helmet and the chest harness with the locked core from it, using the harness with core panel. Reference 12 (control room): take the pressurized control room, the reinforced rear window, the low console with its empty rectangular core input slot and the three upright levers from it, using the wide room panel. Wide shot on a 28 mm lens, the camera at chest height in a front corner of the control room, looking diagonally across it. The reinforced rear window fills the left side of the frame and shows the distant exit iris with its three rigid shutters partly closed. At frame-left, beside the window, an adult 38-year-old olive-skinned man in an ivory pressure suit with navy shoulders, orange upper-arm bands, and a fully clear closed ivory helmet stands in rear three-quarter, white-gloved hands at his sides, watching the iris. At frame-right the low console stands with its empty rectangular core input slot and its three upright levers: one broad blue gate-power lever, one broad teal port-clamp release lever and one separate orange gate-catch lever. At the console stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, the compact graphite core locked in her chest harness with its amber glass center glowing. She wears white gloves, her badge sits on her left chest, and her clear visor is turned in three-quarter toward the man. One white glove already rests on a broad, flat, unmarked local-control pad on the console, a small fixed warning lamp above it glowing red. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow dolly toward the console as the woman presses the flat pad once with her glove, the small warning lamp above it staying red, and says in a clear, quick adult woman's voice, precise and controlled: Local override is locked out. 4-7 s: she keeps her glove on the pad, her eyes dropping to the red lamp, while the dolly passes the three upright levers and the man stays at the window watching the iris. 7-10 s: the dolly ends close on her glove and the red lamp, the steady red glow on her visor, the empty core slot beside the pad and the levers still upright. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C34 — Teal kol kilide takılır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C34.png
```

> Not: Plan K34. Replik R34 (Rhea, telsiz, yüz kadraj dışı, 1.5 s): "And the clamp motor has no feed." — 0-4 s vuruşunun sonunda; ses kadraj dışından, telsiz filtreli. Kadrajda yalnız eldiven, kol ve kol bileği; yüz yok.
> T01: eldiven kolu ilk karede tutuyor; hareket tek küçük dirençli çekiş, sonra durma; kol bükülmez ("straight and rigid" pozitif yazıldı). Kol ayırt edici sözcüğü: plandaki "clamp-A" harfi çıkarıldı (§C, kadraja yazı olarak basılabilir), "teal port-clamp release lever" nesneye bağlı yazıldı.
> Eldiven kadrajın sağ-alt kenarından girer (tutan kadrajda, A07). Diğer iki kol dik ve flu (renk adı yok). Ref 10 çıkarıldı (başlık notu). Çekim başına ref 12 `console close panel`.

### Görsel
```text
Reference 2 (woman): take the white glove and the pearl sleeve with its graphite wrist joint from it, using the front full-length panel. Reference 12 (control room): take the low console, the broad teal port-clamp release lever with its fixed hinge and its end stop, and the console surface from it, using the console close panel. Tight insert on a 100 mm lens, the camera level with the console surface and a short way in front of the lever: the broad teal port-clamp release lever stands upright at frame-center on its single fixed hinge, its end stop visible beside it and a fixed mechanical lock block set against its base. A right white glove is already wrapped around the lever's grip, and the pearl sleeve with its graphite wrist joint enters from the bottom edge at frame-right, continuing out of the frame. Behind the lever the console's other two levers stand upright and softly out of focus, and the console surface carries only plain, unmarked shapes. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow slide to the left along the console edge as the glove tightens around the lever and pulls it down a few degrees in one small, resisted movement until it jams against the lock, and from out of frame a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says: And the clamp motor has no feed. 4-8 s: the glove keeps its pull against the lock, the forearm under the sleeve straining and the cuff creasing at the wrist, while the lever stays straight and rigid at its jammed angle. 8-10 s: the pull eases and the lever settles straight against the lock as the slide ends. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C35 — Çıkış kepenkleri biraz daha kapanır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C35.png
```

> Not: Plan K35. Replik R35 (Leon, telsiz, kadraj dışı, 2.5 s): "The way out is getting smaller." — 0-4 s vuruşunun sonunda. Kadrajda insan yok. Dış (vakum) klip: Y1 yatağı, klip sesi yalnız replik penceresinde (F8, FILM.md §6 T13).
> T09: üç rijit kepenk, iki kelepçe kolu kilitli. Başlangıç karesi kepenklerin KISMEN kapalı hâli (daralma videoda olur); plan cümlesindeki "now narrow the exit farther" sonuç hâli kareye alınmadı (video ne yapacaksa o henüz olmamıştır).
> Kadraj ark'ın burun yarısına kurulu (kıç kadraj dışı): kıç sancak portundaki tug, plan referans listesinde olmadığı için kadraja sokulmadı. G01 C12, G04 C44 gibi kıç görünen dış planlarda tug'ın kadraja girip girmeyeceği Fable'ın devamlilik kararıdır. Gök/ışık cümlesi (DIŞ) birebir.

### Görsel
```text
Reference 5 (foundry): take the black C-shaped foundry cradle, the circular exit gate with its three rigid radial sliding shutters, the heavy blast ribs and the two gantry clamp arms from it, using the wide exterior panel. Reference 6 (ark): take the long ivory segmented ark hull with its graphite dorsal rails and cryo-habitat blocks from it, using the side view panel. Wide exterior view on a 24 mm lens from outside the foundry, level with the ark's axis and framed on the forward half of the long ivory ark. The ark's rigid hull runs from the left edge of the frame toward frame-right, held by two rigid gantry clamp arms gripping opposite flanks, its nose pointing at the huge circular exit gate at frame-right, whose three rigid radial sliding shutters stand partly closed around a wide circular opening. Beyond the gate lies open space, and the black C-shaped foundry cradle frames the hull. At the left edge of the frame heavy blast ribs hold back the glow of the furnace trench. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow lateral drift to the right along the ark as the three rigid shutters start to slide inward along their radial tracks, and from out of frame a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says: The way out is getting smaller. 4-7 s: the shutters keep sliding inward, each advancing a short distance, and the circular opening narrows while every blade and its outer ring keeps its shape. 7-10 s: the shutters slide the last short distance and stop at their narrower setting as the drift ends, and the ark and both clamp arms stay rigid and locked. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C36 — Kokpitte kaçış seçeneği

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C36.png
```

> Not: Plan K36. Replikler R36 (Leon, ağız kadrajda, 1.0 s): "We can undock. The ark can't." — 0-4 s vuruşu · R37 (Rhea, ağız kadrajda, 4.0 s): "Then find another way." — 4-8 s vuruşunun başı. Konuşmayan kişinin ağzı kapalı yazıldı.
> Kamera kokpitin arkasından, iki koltuğun ortasından (plandaki diğer kokpit çekimleri gibi: ark kanopide önde, Leon solda, Rhea sağda). Yüzler ¾ profilde; çekirdeğin amber merkezi Rhea'nın gövdesinin kenarında. Arkadan görünümde Rhea'nın sağ çene yarası ve Leon'un sol şakak yarası gizli kalabilir: kare onayında yaraların yanlış yüze basılmadığı kontrol edilir.
> T09: çekirdek askıda, tug ark'a bağlı (kanopide ark gövdesi temas mesafesinde). "Without operating them": Leon'un eldivenleri uyluklarında, kumandada değil; hareket yalnız kask dönüşü. Ref 5 ve 10 çıkarıldı (başlık notu).

### Görsel
```text
Reference 1 (man): take his ivory suit, navy shoulders, orange upper-arm bands and closed helmet from it, using the back full-length panel. Reference 2 (woman): take her pearl suit, navy waist, teal upper-arm bands, closed helmet and the chest harness with the locked core from it, using the harness with core panel. Reference 4 (tug cockpit): take the two seats, the low graphite console with its short dual controls, the ivory overhead shell and the broad canopy with its two graphite mullions from it, using the wide interior panel. Reference 6 (ark): take the long ivory segmented hull with its graphite dorsal rails from it, using the side view panel. Medium two-shot on a 35 mm lens from behind and slightly above the two seats, the camera at the center of the cockpit at shoulder height. At frame-left an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet sits in the navy pilot seat, his helmet turned in three-quarter down toward the short dual controls at his left, his white gloves resting on his thighs. At frame-right an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet sits in the engineer seat, her helmet turned in three-quarter toward him, her white gloves in her lap, the compact graphite core locked in her chest harness with its amber glass center glowing at the edge of her torso. Through the broad canopy ahead the long ivory hull of the ark fills the view at close range, the tug docked against it. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: the camera begins a slow push-in between the two seats as the man, his gloves resting on his thighs and his helmet turned toward his controls, says in a low, dry adult man's voice, calm and guarded: We can undock. The ark can't. The woman's mouth stays closed, and at the end of the beat he turns his helmet toward her. 4-8 s: the woman, her helmet turned toward him, says in a clear, quick adult woman's voice, precise and controlled: Then find another way. His gaze stays on her and his mouth stays closed. 8-10 s: her lips close as the push-in finishes on the two helmets turned toward each other, the hull of the ark behind them. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir, klibin içinde) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini görselden video 10 s ile hedefler (FILM.md künye); Omni'nin Frames to Video süresi, repliği videoda üretmesi ve kredisi SMOKE P11 · P14 · P18'de ölçülür (`FLOW_GERCEKLERI.md` §1 · §4); ölçüm gelmeden videolar (sıra 13-24) koşulmaz. Kredi sütunu bu yüzden boş.
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kaynak kare yok: on iki kare yalnız referans sayfalarından üretilir, aralarında sıra bağımlılığı yoktur (sıra 1-12 herhangi bir sırayla koşulabilir).
> Önkoşul: `ref/1`, `2`, `4`, `5`, `6`, `10`, `11`, `12`, `15` sayfaları onaylanmış olmalı (G01 iş emri) ve sayfalarda bu grubun kullandığı paneller bulunmalı (dosya başındaki panel listesi). Yoksa ilgili sayfa v2'ye çıkar, ikinci dosya açılmaz.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C25 | `kare/C25.png` | Görsel | ref/10.CEKIRDEK_v1.png (beşik yakın paneli) | 2 | |
| 2 | C26 | `kare/C26.png` | Görsel | ref/2.RHEA_v1.png (önden tam boy paneli) · ref/10.CEKIRDEK_v1.png (kasa geniş paneli; bu sırayla) | 2 | |
| 3 | C27 | `kare/C27.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/2.RHEA_v1.png (çekirdekli askı paneli) · ref/10.CEKIRDEK_v1.png (kasa geniş paneli; bu sırayla) | 2 | |
| 4 | C28 | `kare/C28.png` | Görsel | ref/10.CEKIRDEK_v1.png (kasa geniş paneli) | 2 | |
| 5 | C29 | `kare/C29.png` | Görsel | ref/1.LEON_v1.png (yandan tam boy paneli) · ref/10.CEKIRDEK_v1.png (kasa geniş paneli) · ref/11.DRONE_v1.png (drone ön paneli; bu sırayla) | 2 | |
| 6 | C30 | `kare/C30.png` | Görsel | ref/10.CEKIRDEK_v1.png (kasa geniş paneli) · ref/11.DRONE_v1.png (drone yan paneli; bu sırayla) | 2 | |
| 7 | C31 | `kare/C31.png` | Görsel | ref/2.RHEA_v1.png (çekirdekli askı paneli) · ref/10.CEKIRDEK_v1.png (kasa geniş paneli) · ref/15.ARACLAR_v1.png (EMP diski paneli; bu sırayla) | 2 | |
| 8 | C32 | `kare/C32.png` | Görsel | ref/10.CEKIRDEK_v1.png (kasa geniş paneli) · ref/11.DRONE_v1.png (drone ön paneli; bu sırayla) | 2 | |
| 9 | C33 | `kare/C33.png` | Görsel | ref/1.LEON_v1.png (arkadan tam boy paneli) · ref/2.RHEA_v1.png (çekirdekli askı paneli) · ref/12.KONTROL_ODASI_v1.png (geniş oda paneli; bu sırayla) | 2 | |
| 10 | C34 | `kare/C34.png` | Görsel | ref/2.RHEA_v1.png (önden tam boy paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 11 | C35 | `kare/C35.png` | Görsel | ref/5.FOUNDRY_v1.png (geniş dış paneli) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 12 | C36 | `kare/C36.png` | Görsel | ref/1.LEON_v1.png (arkadan tam boy paneli) · ref/2.RHEA_v1.png (çekirdekli askı paneli) · ref/4.KOKPIT_v1.png (geniş iç panel) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 13 | C25 | `ham/C25_d1.mp4` | Frames to Video | kare/C25.png (replik R27 telsiz) | 2 | |
| 14 | C26 | `ham/C26_d1.mp4` | Frames to Video | kare/C26.png (replik R28 telsiz, kadındaki ağız kapalı) | 2 | |
| 15 | C27 | `ham/C27_d1.mp4` | Frames to Video | kare/C27.png (replik R29 ağız kadrajda: dudak senkronu dinlenir, Leon'un ağzı kapalı) | 2 | |
| 16 | C28 | `ham/C28_d1.mp4` | Frames to Video | kare/C28.png (replik R30 telsiz, kadrajda kimse yok) | 2 | |
| 17 | C29 | `ham/C29_d1.mp4` | Frames to Video | kare/C29.png (replik R31 ağız kadrajda, geniş planda küçük yüz) | 2 | |
| 18 | C30 | `ham/C30_d1.mp4` | Frames to Video | kare/C30.png (replik yok) | 2 | |
| 19 | C31 | `ham/C31_d1.mp4` | Frames to Video | kare/C31.png (replik R32 ağız kadrajda) | 2 | |
| 20 | C32 | `ham/C32_d1.mp4` | Frames to Video | kare/C32.png (replik yok) | 2 | |
| 21 | C33 | `ham/C33_d1.mp4` | Frames to Video | kare/C33.png (replik R33 ağız kadrajda) | 2 | |
| 22 | C34 | `ham/C34_d1.mp4` | Frames to Video | kare/C34.png (replik R34 telsiz, yüz kadrajda yok) | 2 | |
| 23 | C35 | `ham/C35_d1.mp4` | Frames to Video | kare/C35.png (replik R35 telsiz; dış vakum klibi, klip sesi yalnız replik penceresinde) | 2 | |
| 24 | C36 | `ham/C36_d1.mp4` | Frames to Video | kare/C36.png (replik R36 + R37 ağız kadrajda, iki konuşan sırayla) | 2 | |

> Sıra: 1-12 kareler (sırası serbest) → ancak sonra videolar. Üretim önceliği önerisi: C30 (atım ve kıvılcım) ve C32 (drone inişi) planın "önce zor planlar" listesinde; önce sınanmaları iyi olur (sıra 6 → 18, sıra 8 → 20).
> Replik doğrulaması video dinlenirken: R27 (C25 0-3 s) · R28 (C26 0-4 s) · R29 (C27 0-4 s) · R30 (C28 0-4 s) · R31 (C29 0-4 s) · R32 (C31 0-4 s) · R33 (C33 0-4 s) · R34 (C34 0-4 s) · R35 (C35 0-4 s) · R36 (C36 0-4 s) · R37 (C36 4-8 s).
> Metin `FILM.md` §5 ile birebir; farklı duyulursa `NOTLAR.md` TARAMA/ANLATIM satırına tek cümleyle. Ses kimliği ölçümü: Leon (C26 · C28 · C29 · C35 · C36) ve Rhea (C25 · C27 · C31 · C33 · C34 · C36) tonları klipten klibe karşılaştırılır (SMOKE P18); tutmazsa yedek kurgu kaydıdır.
