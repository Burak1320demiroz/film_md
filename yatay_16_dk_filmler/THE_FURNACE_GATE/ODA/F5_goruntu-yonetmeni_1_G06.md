# 🖼️ THE_FURNACE_GATE — Prompt grubu G06 (çekimler C61–C72)

> Yazan: goruntu-yonetmeni (tur 1). Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K61–K72 + `FILM.md` §3 / §4 / §5.
> Bu dosya yeniden tasarım değil, biçim çevirisidir: kompozisyon, olay, replik ve hareket yönü planın kendisi; cümleler olabildiğince planın İngilizcesi.
> Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Zincir yok (plan zincir kurmaz); her çekim kendi başlangıç karesiyle Frames to Video. `EKLE` satırı iki parçalıdır: KARE (görsel üretimi için referanslar) ·
> VİDEO (yalnız kare; Frames to Video'ya referans eklenmez, yoksa mod Ingredients'e kayar).
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında `Reference <No> (<rol>): …` diye adlandırılır;
> her referanstan çekim başına yalnız TEK panel. Her video promptu 10 s'yi 3 vuruşa böler (0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s, son vuruş donmaz; ilk vuruş hareketle başlar;
> sınırlar çekimden çekime değişir: 0-4/4-7/7-10 · 0-3/3-8/8-10 · 0-5/5-8/8-10 · 0-3/3-6/6-10 · 0-3/3-7/7-10 · 0-4/4-8/8-10).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** FILM.md §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir; MEKÂN IŞIĞI cümlesi her görsel promptta
> `The light is …` sarmalayıcısıyla (kelimeler FILM.md §3'teki gibi); ORTAM SESİ cümlesi o mekânın her video promptunda birebir (ortak görünümden hemen önce). Bu filmde bütün replikler model sesi:
> replik video promptuna birebir `says …: <line>` biçiminde yazılır (SMOKE P9'a kadar tırnaklı biçim yedek), konuşanın sesi SES KİMLİĞİ kelimeleriyle tarif edilir (telsizde
> `, softened by a light suit-radio filter`), replik vuruşun SON cümlesidir. Ağız kadrajda olan repliklerde (C63 · C64 · C70) dudak yalnız kendi cümlesinde oynar; telsiz repliklerinde
> konuşanın yüzü kadrajda değildir (C61 · C62 · C66 · C69 · C72 kimse yok; C65 · C67 · C71 yalnız eldiven ve kol).
> **Ortak cümleler (FILM.md §3, birebir):**
> kimlik tabanı Leon `an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet` ·
> kimlik tabanı Rhea `an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet` ·
> ses Leon `a low, dry adult man's voice, calm and guarded` · ses Rhea `a clear, quick adult woman's voice, precise and controlled` ·
> dış gök cümlesi (C62 · C68 · C72 birebir) `Deep black space with sparse stars surrounds the foundry.`
> **Panel adları (FILM.md §3'ten; çekim başına her referanstan yalnız TEK panel):** 1.LEON `side full-body panel` · `face close-up panel` · `glove panel` · 2.RHEA `face close-up panel` · `side full-body panel` ·
> 5.FOUNDRY `wide exterior panel` · `gate open panel` · 6.ARK `side view panel` · 10.CEKIRDEK `cradle close panel` · `core overheating panel` ·
> 12.KONTROL_ODASI `wide room panel` · `console close panel` · `gate-catch pawl panel` · 13.KOMUTA `wide bridge panel` · `pilot console panel`.
> **Kelime güvenliği (BILINEN_TUZAKLAR §A · §C):** `body` · `dead` · `blood` · `wound` hiçbir promptta geçmez (`hull` · `casing` · `end stop` yazıldı). Kollar harf/ad etiketiyle anılmaz (plandaki "clamp-A" · "release-B" · "gate-catch"
> kök sözcükleri kadraja yazı olarak basılabilir): kol rengiyle ve konumuyla anılır (`the broad teal lever` · `the broad silver lever` · `the orange gate-catch lever` — "gate-catch" yalnız turuncu kola bağlı, tek başına durmaz).
> Plan olumsuzları ("no new cable or arc" · "nothing changes position" · "no activation until the next shot") pozitife çevrildi ya da çıkarıldı ("next shot" çekime atıftır).
> **Sabit tasarım (FILM.md §3):** ark burnu SAĞDA · çekirdek kontrol odası giriş yuvasında mandallı (C58'den beri) · mavi kol C60'tan beri aşağıda · turuncu kol C65'te iner · teal kol C67'de iner · gümüş kol C71'de iner ·
> port çenesi C68'de, sancak çenesi C72'de açılır · kapı C62'de açılır, C63'ten sonra tamamen açık, mekanik mandal C65'te oturur · tug ark'ın kıç sancak portunda (C80'e kadar): C62 · C68 · C72 kadrajları ark'ın ön kısmında, kıç ve tug kadraj dışında.

---

## C61 — Enerji kontak şeritleri boyunca ilerler

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C61.png
```

> Not: Replik R63 (Leon, telsiz, 1,5 s; kadrajda kimse yok). Çekirdek mandallı ve parlak (plan override); mavi/turuncu/teal kollar kadraj dışında bırakıldı (plan: yalnız kadrajdaki nesnenin durumu yazılır).
> Plandaki "heavy bus contacts / contact strips" = yuva kenarında çekirdek tabanından küçük işaretsiz bara konnektörüne uzanan ağır sabit metal şeritler (12.KONTROL_ODASI `console close panel`).
> "No new cable or arc" pozitife çevrildi (ışık yalnız mevcut şeritlerde yürür, her kontak biçimini korur). Vuruşlar 0-4 · 4-7 · 7-10 (replik 1,5-3,0 s ilk vuruşta).

### Görsel
```text
Reference 10 (core): take the compact graphite casing with its ivory corner guards, the single rigid carry handle, the amber glass center and the closed hinged retaining latch from it, using the cradle close panel. Reference 12 (control room): take the low console surface, the rectangular input cradle rim and the small unmarked bus connector beside it from it, using the console close panel. Close view on a 100 mm lens with shallow depth of field, the camera 50 cm from the cradle and slightly above it, looking down at the portable core seated in the control room's input cradle: its one broad retaining latch is closed over the rigid carry handle and its amber glass center glows bright. Heavy fixed metal contact strips run along the cradle rim from the core's base to the small unmarked bus connector beside it, and the surrounding console metal is plain, unmarked and unchanged. Soft cyan console lights glow out of focus behind the cradle. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera starts a slow push toward the base of the core while its amber glow steadies and one contained amber-cyan pulse of light begins at the cradle rim beneath the casing; a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from out of frame: I have clamp power. 4-7 s: The push continues as the pulse travels along the heavy contact strips toward the small bus connector, staying inside the existing strips and leaving every contact and the casing as they are. 7-10 s: The pulse reaches the bus connector and settles there as a soft cyan glow while the push closes in slightly more, the core, the strips, the connector and the cradle keeping their exact shapes. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C62 — Dev kapının üç kepenki dışa kayar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C62.png
```

> Not: Replik R64 (Rhea, telsiz, 1,5 s); kadrajda kimse yok. Dış (vakum, T13): F8'de klip sesi yalnız replik penceresinde (1,5-3,0 s ±0,5) açık tutulur. Başlangıç 5.FOUNDRY `wide exterior panel` ile aynı durum
> (kepenkler kısmen kapalı, iki kelepçe kilitli); hareket eden tek şey üç kepenk, ark ve iki kol sabit. Kadraj ark'ın ön kısmı: kıçtaki tug (sancak portu) ve kıç kadraj dışında. Kamera yüksek ¾, ark'ın sancak yanından
> (burun sağda). Vuruşlar 0-3 · 3-8 · 8-10 (replik 1,5-3,0 s ilk vuruşta).

### Görsel
```text
Reference 5 (foundry): take the black C-shaped foundry cradle, the two rigid gantry clamp arms, the circular exit gate with its three radial sliding shutters, the heavy blast ribs and the orange furnace trench from it, using the wide exterior panel. Reference 6 (ark): take the long ivory segmented hull with its grey dorsal rails from it, using the side view panel. Wide exterior view on a 24 mm lens from a high three-quarter angle above the ark's starboard flank. The forward part of the long ivory ark fills the left and center of the frame in the foreground, its nose pointing to frame-right, held at its flanges by two rigid gantry clamp arms, one on each side of the hull, their broad jaws closed. Ahead at frame-right stands the huge circular exit gate: a ring of three rigid radial sliding shutters, still partly closed around a narrowed round opening of deep black space. At frame-left behind the ark the orange furnace trench glows beyond the heavy blast ribs. Deep black space with sparse stars surrounds the foundry. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow lateral drift to the right across the foundry while the three rigid shutters start to slide outward along their radial tracks, the narrow round opening at the center of the ring beginning to widen; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: Gate drive is moving. 3-8 s: The three shutters keep sliding outward in unison along their established tracks, the opening growing and more of the sparse starfield appearing beyond it, while the ark and both clamp arms stay fixed. 8-10 s: The shutters reach the outer ends of their tracks and the opening stands wide, the drift easing as the open ring settles toward the right of the frame. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C63 — Leon açık çıkışı kanopide görür

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C63.png
```

> Not: Replik R65 (Leon, ağız kadrajda, 1,5-4,5 s; 3,0 s ≤5). Repliğin "dies" sözcüğü plan metni, birebir korunur (§A kelime listesinde yok ama yakın: ret gelirse sahibe sorulur, kelimeyi biz değiştirmeyiz).
> Kompozisyon çözümü: yüzü görünen ve kapıyı gören tek düzen = kamera köprünün SOL duvarında, Leon sol profil ¾ (sol şakak yarası görünür), kanopi ve açık kapı kadraj solunda önünde; arkada boş lacivert
> navigasyon koltuğu. Gümüş kol dik (plan override), eldivenler konsol kenarında kolla temassız (C71'e kadar kimse dokunmaz). Plan "Medium Leon at bridge canopy": vizör yansıması istenmedi (HUD riski, BILINEN §B 2).
> Vuruşlar 0-5 · 5-8 · 8-10 (replik 1,5-4,5 s ilk vuruşta).

### Görsel
```text
Reference 1 (man): take his face, the short dark brown hair, the neat beard, the ivory pressure suit with navy shoulders and orange upper-arm bands, the blue-gold hawk badge and the clear ivory helmet from it, using the side full-body panel. Reference 13 (command bridge): take the wide forward canopy, the navy pilot seat, the pilot console with its single broad silver lever and the cyan interface lights from it, using the wide bridge panel. Medium shot on a 35 mm lens at eye level, the camera at the bridge's left wall, level with his helmet, looking across at his left profile: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, sits in the navy pilot seat of the ark's emergency command bridge, seen in left three-quarter profile with his face directed forward to the wide canopy at frame-left and his eyes fixed on it, his scar plainly visible behind the clear visor. Through the canopy ahead the exit gate stands fully open, a wide ring of retracted shutters around ordinary sparse stars. In front of him at frame-left the pilot console carries the single broad silver lever, upright at its side; his white gloves rest on the console edge, clear of the lever. Behind him the ivory shell of the bridge and the empty navy navigation seat are softly out of focus. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera begins a slow push forward along his left profile toward his visor and the open canopy beyond while he keeps his eyes on the open gate; his lips move only for his own line as he says in a low, dry adult man's voice, calm and guarded: Clear aperture. Lock it before the core dies. 5-8 s: The push continues as he draws one steady breath, his chest rising and his gaze staying on the open aperture ahead. 8-10 s: The push closes a little more on his visor and the unchanged open aperture beyond the canopy, his gloves resting on the console edge. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C64 — Rhea turuncu mandal koluna hazırlanır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C64.png
```

> Not: Replik R66 (Rhea, ağız kadrajda, 1,5-2,5 s). Eldiven ilk karede kolda (T01); kol bu çekimde kımıldamaz. Plandaki "no activation until the next shot" çekime atıf olduğu için çıkarıldı, yerine "the lever stays upright".
> Yara sağ çenede: kamera Rhea'nın sağ önünde, sağ eldiven kolda, yüz kadraj soluna dönük → sağ yanak kameraya. Askı boş, çekirdek yuvada mandallı, mavi kol aşağıda, turuncu dik (tutulu), teal dik (plan override).
> 12 `wide room panel` üç kolu dik ve yuvayı boş gösterir: durum farkı metinde açıkça yazıldı. Vuruşlar 0-3 · 3-6 · 6-10 (replik 1,5-2,5 s ilk vuruşta).

### Görsel
```text
Reference 2 (woman): take her face, the dark copper braid, the pearl pressure suit with its navy waist, teal upper-arm bands and blue-gold geometric-sun badge, and the clear pearl helmet from it, using the face close-up panel. Reference 12 (control room): take the low console with its levers and input cradle, the rear window and the cool blue gate light from it, using the wide room panel. Medium shot on a 50 mm lens at chest height, the camera in the control room at her right front: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, stands at the console in the right half of the frame, seen in three-quarter view from her right front with her head turned toward frame-left, so that her small right-chin scar shows plainly behind the clear visor. Her chest harness is empty. Her white-gloved right hand already grips the upright orange gate-catch lever at the console's edge, her elbow bent and her boots set shoulder-width on the deck. Beside it the broad blue lever is already pulled down to its stop and the broad teal lever stands upright; the plain, unmarked levers sit beside the input cradle, which holds the portable core latched, its amber glass center glowing. Beyond the console at frame-left the rear window shows the exit gate fully open, a wide ring of ordinary sparse stars. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow lateral slide along the console while Rhea shifts her weight, setting her boots a little wider and tightening her right glove on the upright orange lever; her lips move only for her own line as she says in a clear, quick adult woman's voice, precise and controlled: Mechanical catch. 3-6 s: She settles into a braced stance, knees flexing slightly and shoulders squaring toward the lever, her eyes lifting to the open gate in the window while the lever stays upright in her grip. 6-10 s: Her breathing steadies as the slide carries on past her and her glove stays wrapped around the lever's grip. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C65 — Turuncu kol aşağı iner, kapı açık kilitlenir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C65.png
```

> Not: Replik R67 (Rhea, telsiz, 1,5-2,5 s; yüz kadraj dışı, yalnız eldiven ve kol). Eldiven ilk karede kolda (T01, kurulu temas; C64 ile aynı sağ eldiven); hareket kolun tek yayı, temas değişmez.
> Kol kadraj sağından giren kol ağızlığı (C64 ile aynı yerleşim: Rhea kadrajın sağında, kol solda). "Then hold" donma olarak yazılmadı: son vuruşta eldiven sarılı kalır, kamera kaymaya devam eder.
> Kolun harf/ad etiketi yok (BILINEN §C). Vuruşlar 0-3 · 3-7 · 7-10 (replik 1,5-2,5 s ilk vuruşta, kol durdurucuya varırken).

### Görsel
```text
Reference 2 (woman): take the white glove and the pearl pressure-suit sleeve from it, using the side full-body panel. Reference 12 (control room): take the console surface and the broad orange gate-catch lever with its fixed hinge and end stop from it, using the console close panel. Close view on a 100 mm lens, the camera 40 cm from the console and level with the lever's grip, looking at the lever from slightly in front of it: the broad, plain, unmarked orange gate-catch lever stands upright at its upper stop on a fixed hinge, hinge and end stop plainly visible at its base, and a white right glove is already wrapped around its grip, the pearl sleeve entering from the right edge of the frame. Only the glove and forearm are in frame. Out of focus behind the lever: the plain console surface and the cool blue light of the rear window. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow drift toward frame-left along the console while the white glove pulls the orange lever down in one firm arc around its fixed hinge; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: Catch engaged. 3-7 s: The lever reaches its lower locking end stop and seats against it with a small settle, the hinge turning only through that one arc and the glove following the lever down. 7-10 s: The drift carries on past the seated lever as the glove stays wrapped around the grip and the cool blue window light slides along the lever's top edge. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C66 — Mandal dişlisi çentikte oturur

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C66.png
```

> Not: Replik R68 (Leon, telsiz, 1,5-3,0 s); kadrajda kimse yok. El yok, hiçbir parça kımıldamaz: hareket yalnız kamera itişi ve pencere ışığının dişli halka üzerinde kayması (plan "nothing changes position" pozitife çevrildi:
> mandal, çentik ve halka olduğu yerde kalır). Mandal dişlisi 12 `gate-catch pawl panel`. Arka plandaki pencerede kapı tamamen açık (plan override), flu. Vuruşlar 0-4 · 4-8 · 8-10 (replik 1,5-3,0 s ilk vuruşta).

### Görsel
```text
Reference 12 (control room): take the window-side gate support with its toothed ring and the broad mechanical pawl seated in its notch from it, using the gate-catch pawl panel. Tight close view on a 100 mm lens, the camera 40 cm from the support and level with the pawl: one broad mechanical pawl sits seated in its fixed notch on the gate support's rigid toothed ring beside the control room's rear window, the ring, the notch and the pawl's hinge pin plainly visible in plain unmarked metal, the support standing alone in the frame. Out of focus behind it the rear window shows the exit gate fully open, a wide ring of ordinary sparse stars, in cool blue light. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow, restrained push toward the seated pawl while the cool blue window light drifts gently across the ring's toothed edge; a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from out of frame: It'll hold without power. 4-8 s: The push continues, the pawl's broad face and the ring's teeth growing larger in the frame while the pawl stays seated in its notch. 8-10 s: The push slows as it closes on the notch, the pawl, the notch and the ring staying exactly where they are as the soft light drifts across them. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C67 — Teal kol aşağı iner, birinci kilit bırakılır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C67.png
```

> Not: Replik R69 (Rhea, telsiz, 1,5-3,0 s; yüz kadraj dışı). Eldiven ilk karede teal kolda (T01); sağ eldiven, kol kadraj sağından girer (C64 · C65 ile aynı yerleşim). Plandaki "powered indicator cyan" = kol tabanında küçük camgöbeği
> gösterge lambası (yazı/rakam yok). Kolun harf/ad etiketi yok. Kamera C65'ten farklı (itiş; C65 kayma) ki ardışık yakınlar jump cut gibi okunmasın. Vuruşlar 0-3 · 3-6 · 6-10 (replik 1,5-3,0 s ilk vuruşta).

### Görsel
```text
Reference 2 (woman): take the white glove and the pearl pressure-suit sleeve from it, using the side full-body panel. Reference 12 (control room): take the console surface and the broad teal lever with its fixed hinge and end stop from it, using the console close panel. Close view on a 100 mm lens, the camera 40 cm from the console and level with the lever's grip, looking at the lever from slightly in front of it: the broad, plain, unmarked teal lever stands upright on its fixed hinge, hinge and end stop plainly visible at its base, and a white right glove is already wrapped around its grip, the pearl sleeve entering from the right edge of the frame. A small cyan indicator lamp glows steadily beside the lever's base. Only the glove and forearm are in frame. Out of focus behind the lever: the plain console surface and the cool blue light of the rear window. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow push toward the lever's hinge while the white glove pulls the teal lever down in one firm arc around its fixed hinge; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: Port clamp releasing. 3-6 s: The lever reaches its lower end stop and latches there with a small settle, the glove following it down and the cyan indicator beside its base glowing steadily. 6-10 s: The push carries on over the latched lever as the glove stays wrapped around the grip and the cool window light slides along the lever's edge. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C68 — Port çenesi dışa döner

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C68.png
```

> Not: Replik yok (plan "—"); kadrajda kimse yok. Dev yapı hareketi (T09): yalnız port çenesi döner, ark, sancak kolu ve kapı sabit. Dış (vakum, T13): replik penceresi yok, Y1 yatağı. Kamera yüksek ~45°, burun SAĞDA
> (FILM.md §3 sabit tasarım), port yanı kadrajın üst yarısında, sancak kolu "deeper behind" = alt yarıda, objektiften uzak. Port yanında kısa kapalı yükleme köprüsü C74'e kadar durur: üst-sol kenarda tek cümleyle yazıldı
> (planın K68 kadrajı köprüyü anmaz; 6.ARK port yanı köprü bağlantısını taşır). Kıç ve tug (sancak portu) kadraj dışı. Başlangıç 5.FOUNDRY `gate open panel` (kapı tamamen açık, mandal oturmuş).
> Vuruşlar 0-3 · 3-8 · 8-10.

### Görsel
```text
Reference 5 (foundry): take the black foundry structure, the gantry clamp arms with their broad rigid gripping jaws, the fully open exit gate with its seated mechanical catch and the heavy blast ribs from it, using the gate open panel. Reference 6 (ark): take the long ivory segmented hull with its grey dorsal rails and its hull flanges from it, using the side view panel. High wide view on a 24 mm lens, the camera above the ark's dorsal rails and looking down across the hull at about 45 degrees, the long ivory hull running from the left of the frame to the right with its nose toward frame-right and its port flank along the upper half of the frame. In the upper foreground the port gantry clamp arm reaches in from the foundry structure with its broad rigid gripping jaw closed around the ark's flange. Across the hull, lower in the frame and farther from the lens, the opposite starboard clamp arm holds its flange with its jaw closed. A short closed loading bridge joins the port flank to the foundry's control spine at the upper-left edge of the frame. At the far right edge the exit gate stands fully open, its three shutters retracted into the ring, ordinary sparse stars beyond. Deep black space with sparse stars surrounds the foundry. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow drift to the right above the hull while the port clamp's broad jaw starts to rotate outward from the flange it grips, a first thin gap opening between the jaw and the hull. 3-8 s: The jaw keeps swinging outward in one steady arc around its hinge, the gap widening until the jaw stands clear of the flange, while the starboard arm across the hull stays locked and the ark stays where it is. 8-10 s: The jaw reaches the end of its swing, fully open and clear of the hull, as the drift slows; the ark, the starboard arm, the bridge and the open gate stay exactly in place. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C69 — Çekirdeğin parlaması zirve yapıp söner

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C69.png
```

> Not: Replik R70 (Rhea, telsiz, 1,5-3,0 s); kadrajda kimse yok. 10.CEKIRDEK `core overheating panel` (amber merkez çok parlak, kasa ısı izli) başlangıç durumunun kendisi. Patlama/erime yok:
> plan "no explosion or molten morphing" pozitife çevrildi (kenarlar, köşe korumaları ve mandal keskin ve rijit kalır). Parlama zirveden sönük kor seviyesine iner; C73'te çekirdek "sönük ve yanık" (kare onu taşır).
> Vuruşlar 0-4 · 4-7 · 7-10 (replik 1,5-3,0 s ilk vuruşta, parlama yükselirken).

### Görsel
```text
Reference 10 (core): take the compact graphite casing with its ivory corner guards, the rigid carry handle, the intensely bright amber glass center and the darkened heat scoring on the casing from it, using the core overheating panel. Reference 12 (control room): take the low console surface and the rectangular input cradle rim from it, using the console close panel. Close view on a 100 mm lens with shallow depth of field, the camera 40 cm from the core and level with its glass center: the portable core sits latched in the control room's input cradle, its one broad retaining latch closed over the rigid carry handle; its amber glass center glows intensely bright, and the graphite casing around it carries darkened heat scoring while every edge, corner guard and the latch keep their sharp rigid shape. The cradle rim and the console surface are plain and unmarked, with cyan console lights glowing softly out of focus behind. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera starts a slow push toward the glass center while the amber glow swells, brightening across the casing's heat scoring; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: The core is going. 4-7 s: The glow reaches its peak brilliance and then begins to soften, the amber light dropping and warming toward a deeper orange while the casing, the handle and the latch keep their exact shape. 7-10 s: The glow keeps sinking toward a faint ember in the glass center as the push closes in slightly more, the heat scoring on the casing standing out darker against it. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C70 — Leon sancak lambasını kontrol eder, eldivenini kola koyar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C70.png
```

> Not: Replik R71 (Leon, ağız kadrajda, 1,5-3,0 s). TEMAS UYARISI: plan "sets his glove on the grip" temas kurmayı ister (T01/§B sıra 1). Çözüm: eldiven ilk karede kolun bir kısa uzanım yanında konsol kenarında, temas YALNIZ son vuruşta
> (8-10 s) ve kısa; replik ilk vuruşta. Kare temaslı kurulursa video yalnız lamba bakışını isteyebilir (C71 zaten kurulu temasla başlar): deneme bozulursa bu yedek uygulanır. Kamera Leon'un sol önünde → sol şakak yarası görünür,
> yüz kadraj soluna dönük (C63 ile aynı ekran yönü: Leon kanopiye/sola bakar), kol kadraj solunda önde. Sol eldiven (C71 ile aynı). Vuruşlar 0-3 · 3-8 · 8-10 (replik 1,5-3,0 s ilk vuruşta).

### Görsel
```text
Reference 1 (man): take his face with the pale left-temple scar, the neat beard, the short dark brown hair, the ivory pressure suit with navy shoulders, orange upper-arm bands and blue-gold hawk badge, and the clear ivory helmet from it, using the face close-up panel. Reference 13 (command bridge): take the pilot console with its single broad silver lever, the unmarked wrist-link cradle and the cyan interface lights from it, using the pilot console panel. Medium shot on a 50 mm lens at chest height, the camera ahead of and to the left of his seat, looking back at him in three-quarter view: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, sits in the navy pilot seat of the ark's emergency command bridge, his face turned toward frame-left and slightly down so that his scar shows plainly behind the clear visor, his eyes on the console. At frame-left in the foreground the single broad silver lever stands upright on its fixed hinge at the side of the pilot console, one small cyan readiness lamp lit at its base. His white left glove rests on the console edge a short reach from the lever's grip, fingers relaxed. Behind him the ivory shell of the bridge and the empty navy navigation seat are softly out of focus. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera starts a slow, small push toward Leon as his gaze moves to the cyan readiness lamp at the base of the silver lever; his lips move only for his own line as he says in a low, dry adult man's voice, calm and guarded: Starboard motor live. 3-8 s: He keeps his eyes on the steady lamp, one slow breath lifting his chest, while the push continues and his left glove begins to ease along the console edge toward the lever's grip. 8-10 s: The glove closes the last short distance and settles onto the grip as the push eases, the lever standing upright under his glove. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C71 — Gümüş kol aşağı iner, ikinci kilit çekilir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C71.png
```

> Not: Replik R72 (Leon, telsiz, 1,5-2,5 s; yüz kadraj dışı, yalnız eldiven ve kol). Eldiven ilk karede kolda (T01, kurulu temas): C70'in son vuruşunda kurulan temasın devamı değil, ayrı üretilen kare. Sol eldiven; kol kadraj sağından girer
> (C70 yerleşimi: kol kadrajın solunda, Leon sağda). 1.LEON `glove panel`. Plandaki "release-B" etiketi kadraja yazı basabileceği için kol rengiyle anıldı. Kamera yayı C65/C67'den farklı (sola yay). Vuruşlar 0-3 · 3-6 · 6-10
> (replik 1,5-2,5 s ilk vuruşta).

### Görsel
```text
Reference 1 (man): take the white glove and the ivory pressure-suit sleeve from it, using the glove panel. Reference 13 (command bridge): take the pilot console and the single broad silver lever with its fixed hinge and end stop from it, using the pilot console panel. Close view on a 100 mm lens, the camera 40 cm from the console and level with the lever's grip: the single broad, plain, unmarked silver lever stands upright on its fixed hinge at the side of the pilot console, hinge and end stop plainly visible at its base, and a white left glove is already wrapped around its grip, the ivory sleeve entering from the right edge of the frame. Only the glove and forearm are in frame. A small cyan readiness lamp glows steadily beside the lever's base, and the cyan interface lights of the console glow out of focus behind it. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow arc to the left around the console while the white glove pulls the silver lever down in one firm arc around its fixed hinge; a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from out of frame: Starboard releasing. 3-6 s: The lever reaches its lower end stop and latches there with a small settle, the glove following it down. 6-10 s: The arc carries on past the latched lever as the glove stays wrapped around the grip and the cyan lamp at its base glows steadily. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C72 — Sancak çenesi açılır, ark tamamen serbest

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C72.png
```

> Not: Replik R73 (Leon, telsiz, 1,5-4,0 s; kadrajda kimse yok). Dış (vakum, T13): F8'de klip sesi yalnız replik penceresinde (1,0-4,5 s) açık. Kamera C68 ile aynı yüksek ~45° kurulum (burun sağda, port yanı üstte), bu kez ikisi birlikte
> ("both flanks"): port çenesi zaten açık (C68), sancak çenesi hâlâ flanşı kavrıyor ("still near hull" = kapalı, yatırılmış değil) ve bu çekimde dışa döner. Ark yerinde (station-keep). Köprü üst-sol kenarda sağlam
> (C74'e kadar). Kıç ve tug kadraj dışı. 5.FOUNDRY `gate open panel` (kapı tamamen açık, mandal oturmuş); iki çene açık paneli (`clamps open panel`) bitiş durumudur, başlangıç için alınmadı.
> Vuruşlar 0-4 · 4-7 · 7-10 (replik 1,5-4,0 s ilk vuruşta).

### Görsel
```text
Reference 5 (foundry): take the black foundry structure, the gantry clamp arms with their broad rigid gripping jaws, the fully open exit gate with its seated mechanical catch and the heavy blast ribs from it, using the gate open panel. Reference 6 (ark): take the long ivory segmented hull with its grey dorsal rails and its hull flanges from it, using the side view panel. High wide view on a 24 mm lens, the camera above the ark's dorsal rails and looking down across the hull at about 45 degrees, both flanks in view: the long ivory hull runs from the left of the frame to the right with its nose toward frame-right, its port flank along the upper half of the frame and its starboard flank along the lower half. In the upper foreground the port gantry clamp arm stands open, its broad rigid jaw swung outward and clear of the ark's flange. Across the hull, lower in the frame and farther from the lens, the starboard clamp arm still has its broad rigid jaw closed around the ark's flange. A short closed loading bridge joins the port flank to the foundry's control spine at the upper-left edge of the frame. At the far right edge the exit gate stands fully open, its three shutters retracted into the ring, the mechanical catch seated. Deep black space with sparse stars surrounds the foundry. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow pull back and upward while the starboard jaw starts to rotate outward from the hull flange it grips; a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from out of frame: Both clear. Come back to the ark. 4-7 s: The starboard jaw keeps rotating outward in one steady arc, a clear gap opening between the jaw and the flange, while the port arm stays swung open and the ark stays exactly on its station. 7-10 s: The starboard jaw reaches the end of its swing and stands clear of the hull, both clamp arms now open on either side of the ark, and the pullback eases as the ark floats free in the middle of the frame with the open gate ahead of it. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini görselden video 10 s ile hedefler (FILM.md künye); Omni süresi ve ses davranışı SMOKE P11 · P14 · P18'de ölçülür (`uretim_hatti/FLOW_GERCEKLERI.md`); ölçüm gelmeden videolar koşulmaz.
> Replik biçimi (iki nokta ↔ tırnak) SMOKE P9. **Replikli klipler (bu grupta C61 · C62 · C63 · C64 · C65 · C66 · C67 · C69 · C70 · C71 · C72; yalnız C68 repliksiz):** replik klipte yanlış ya da bozuk duyulursa o klibin sesi kurguda
> eklenir (timeline `ses` parçası; kurgu kaydı yedek). Dış (vakum) klipler C62 · C68 · C72: klip sesi yalnız replik penceresinde (T13).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kare üretimi için panel adı parantezde. Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C61 kare | `kare/C61.png` | Görsel | ref/10.CEKIRDEK_v1.png (beşik yakın paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 2 | C62 kare | `kare/C62.png` | Görsel | ref/5.FOUNDRY_v1.png (geniş dış panel) · ref/6.ARK_v1.png (yan görünüm paneli; bu sırayla) | 2 | |
| 3 | C63 kare | `kare/C63.png` | Görsel | ref/1.LEON_v1.png (yandan tam boy paneli) · ref/13.KOMUTA_v1.png (geniş köprü paneli; bu sırayla) | 2 | |
| 4 | C64 kare | `kare/C64.png` | Görsel | ref/2.RHEA_v1.png (yüz yakın paneli) · ref/12.KONTROL_ODASI_v1.png (geniş oda paneli; bu sırayla) | 2 | |
| 5 | C65 kare | `kare/C65.png` | Görsel | ref/2.RHEA_v1.png (yandan tam boy paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 6 | C66 kare | `kare/C66.png` | Görsel | ref/12.KONTROL_ODASI_v1.png (mandal dişlisi paneli) | 2 | |
| 7 | C67 kare | `kare/C67.png` | Görsel | ref/2.RHEA_v1.png (yandan tam boy paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 8 | C68 kare | `kare/C68.png` | Görsel | ref/5.FOUNDRY_v1.png (kapı açık paneli) · ref/6.ARK_v1.png (yan görünüm paneli; bu sırayla) | 2 | |
| 9 | C69 kare | `kare/C69.png` | Görsel | ref/10.CEKIRDEK_v1.png (çekirdek aşırı ısı paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 10 | C70 kare | `kare/C70.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/13.KOMUTA_v1.png (pilot konsolu paneli; bu sırayla) | 2 | |
| 11 | C71 kare | `kare/C71.png` | Görsel | ref/1.LEON_v1.png (eldiven paneli) · ref/13.KOMUTA_v1.png (pilot konsolu paneli; bu sırayla) | 2 | |
| 12 | C72 kare | `kare/C72.png` | Görsel | ref/5.FOUNDRY_v1.png (kapı açık paneli) · ref/6.ARK_v1.png (yan görünüm paneli; bu sırayla) | 2 | |
| 13 | C61 | `ham/C61_d1.mp4` | Frames to Video | kare/C61.png | 2 | |
| 14 | C62 | `ham/C62_d1.mp4` | Frames to Video | kare/C62.png | 2 | |
| 15 | C63 | `ham/C63_d1.mp4` | Frames to Video | kare/C63.png | 2 | |
| 16 | C64 | `ham/C64_d1.mp4` | Frames to Video | kare/C64.png | 2 | |
| 17 | C65 | `ham/C65_d1.mp4` | Frames to Video | kare/C65.png | 2 | |
| 18 | C66 | `ham/C66_d1.mp4` | Frames to Video | kare/C66.png | 2 | |
| 19 | C67 | `ham/C67_d1.mp4` | Frames to Video | kare/C67.png | 2 | |
| 20 | C68 | `ham/C68_d1.mp4` | Frames to Video | kare/C68.png | 2 | |
| 21 | C69 | `ham/C69_d1.mp4` | Frames to Video | kare/C69.png | 2 | |
| 22 | C70 | `ham/C70_d1.mp4` | Frames to Video | kare/C70.png | 2 | |
| 23 | C71 | `ham/C71_d1.mp4` | Frames to Video | kare/C71.png | 2 | |
| 24 | C72 | `ham/C72_d1.mp4` | Frames to Video | kare/C72.png | 2 | |

> Risk sırası (öneri, sahip kararı değil): önce **C68 ve C72** (dev yapı + yüksek ¾ kompozisyon, burun sağda; çene dönüşü tek hareket) ve **C70** (eldivenin son vuruşta kola oturması, temas) denenir; ikisi de bozuk çıkarsa
> kompozisyon/temas düzenlenir, prompt cümlesi eklenmez (PROMPT_HATA_ATLASI A03). **C65 · C67 · C71** (eldiven kolu çeker) kurulu temasla başlar; kaynaşma görülürse kol çekimi kesmeye bölünür (kol üst durdurucuda biter / alt durdurucuda başlar).
