# 🖼️ THE_FURNACE_GATE — Prompt grubu G08 (çekimler C85–C96)

> Yazan: goruntu-yonetmeni. Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K85-K96 (kompozisyon, olay ve hareket yönü planın kendisi) + `FILM.md` §3 (kimlik tabanı, mekân ışığı,
> ortam sesi, ses kimliği) · §4 · §5 (R83-R95). Bu dosya yeniden tasarım değil, biçim çevirisidir.
> Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. Olumsuz yasak listesi yazılmaz. ≤4.300 karakter.
> Zincir yok; her çekim kendi başlangıç karesiyle Frames to Video. `EKLE` satırı iki parçalıdır: KARE (görsel üretimi için referanslar, yükleme sırasıyla) ·
> VİDEO (yalnız kare; Frames to Video'ya referans eklenmez, yoksa mod Ingredients'e kayar).
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında `Reference <No> (<rol>): …` diye adlandırılır;
> çekim başına her referanstan yalnız TEK panel (panel adları FILM.md §3'te sabit). Her video promptu 10 s'yi 2-4 vuruşa böler (0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s, son vuruş donmaz; ilk vuruş hareketle başlar).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi) + 13.10.2026 (replikler videoda):** FILM.md §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir;
> MEKÂN IŞIĞI cümlesi her görsel promptta `The light is …` sarmalayıcısıyla (kelimeler §3'teki gibi); ORTAM SESİ cümlesi o mekânın her video promptunda birebir (ortak görünümden hemen önce).
> Bu grupta 13 replik (R83-R95, 9 çekim) model sesi: `says: <line>` biçiminde, konuşanın sesi §3 SES KİMLİĞİ kelimeleriyle, telsizde `, softened by a light suit-radio filter, out of frame`;
> replik vuruşun SON cümlesidir; alıcı/telsiz sesinde kadrajdaki kişinin ağzı kapalı yazılır, ağız kadrajdaysa konuşan yalnız kendi cümlesinde dudak oynatır, öteki ağzı kapalı.
> **Ortak cümleler (birebir):** kimlik tabanı `the man` / `the woman` (§3 KİMLİK TABANI; ad yazılmaz — tek istisna §3 voice-over cümlesi `Leon's low, dry voice as a calm voice-over`, C94) ·
> dış (vakum) çekimde gök ve ışık cümlesi (T18) = §3 MEKÂN IŞIĞI DIŞ: `The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs.`
> (§3'te ayrı bir gök cümlesi yok; DIŞ ışık cümlesi gök cümlesi sayıldı).
> **Panel adı ↔ kırmızı kelime:** §3'teki `front full-body panel` · `side full-body panel` adlarındaki `body` BILINEN_TUZAKLAR §A kırmızı kelimesidir; promptlarda aynı paneller `the full-length front panel` · `the full-length side panel` diye tarif edildi
> (G01 sayfa üreticisi panel adını değiştirmez; yalnız prompt metni bu iki panel için farklı sözcük kullanır). İş emri tablosunda panel adı Türkçe.
> **Kokpit kamera kurulumu (bu grupta iki tür, her çekimde tam yazılı):** ÖN = kamera kabinin önünde, konsolun hemen üstünde, iki koltuğa dönük; yüzler, göğüs askısı ve dudaklar okunur, kanopi çerçevenin kenarlarında ışık taşır (C86 · C88 · C95) ·
> ARKA-YAN = kamera koltukların arkasında ve yanında, kanopiden dışarı bakar; yarım profil yüz + kanopide ark görünür (C90 · C93). Kokpitte dış ışığın rengi çekimden çekime değişir (foundry turuncusu · ark motor mavisi · soğuk yıldız · gaz devi mavisi):
> §3 KOKPİT cümlesi birebir kalır, ardına tek cümle `Here the outside light …` eklenir.
> **Plan kalıpları çıkarıldı:** "Use the attached reference images only…", "Create one film still, not a reference sheet", "Exactly 2 visible adults", olumsuz kuyruk ("No readable text, letters, numbers…", "No new people, faces in cryo pods…", "No spoken dialogue, narration, music or subtitles"),
> "Continuity overrides the reference image's initial pose…" paragrafı (durumlar yalnız kadrajda görünen nesne için pozitif cümleye çevrildi), "Do not add an offscreen object…", "after K65", "Animate the uploaded scene still as the first frame", "Horizontal 16:9, 10 seconds",
> "Generate only appropriate close breathing, suit-radio chirps…".
> Kelime güvenliği (BILINEN_TUZAKLAR §A): `body`, `dead`, `blood`, `wound` ve türevleri hiçbir promptta geçmez; patlama/duman/alev yerine ışık atımı ve parıltı yazılır (vakumda egzoz yok, §B sıra 4).
> **Referans kararları (FILM.md §4 "fazla görünen referansı grup yazarı gerekçeyle çıkarır"):** C86 · 5, 6, 10, 15 çıkarıldı (çekirdek bu karede yok, askı boş; kanopi dışı yalnız turuncu ışık; araç yok) ·
> C93 · 5 çıkarıldı (serbest uzay, foundry kadrajda değil) · C95 · 10, 15 çıkarıldı (askı boş, araç yok). Diğer çekimlerde §4 listesi korundu (plan R03 → 1 + 2).
> **Ses (T13):** Y1 dış kliplerde (C85 · C87 · C89 · C91 · C92 · C96) klip sesi kurguda AÇILMAZ; replikli olanlarda (C85 · C87 · C96) klibin sesi yalnız replik penceresinde (±0,5 s). C95→C96 karışımı (çapraz 1,5 s) R94 (1,0-2,0 s) ile çakışır: kurgucu ses köprüsünü 1,0 s'den önce bitirir ya da R94'ü 1,5 s'ye kaydırır.

---

## C85 — Kurtarma bağlantısı kilitlenir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/14.ISKELE_v1.png · VİDEO (Frames to Video): yalnız kare/C85.png
```

> Not: Kadrajda insan yok; temas (iki yaka) ilk karede kurulu, kelepçe AÇIK; videoda tek hareket kelepçenin dönüp kapanması (yakalar kıpırdamaz, el yok). Kamera sabit. Replik R83 telsiz, Rhea, 1,5-2,5 s (vuruş 0-3 s).
> Tug yakası metinle taşınır (plan yalnız R15 yükler); model yakayı bozarsa yeniden denemede 3.KESTREL `bow collar open panel` eklenir. Tug solda burnu sağa (önceki yanaşma yönü), soket sağda. Plandaki "Continuity overrides" cümlesi: yakalar temasta, kelepçe açık başlar.

### Görsel
```text
Reference 14 (service catwalk and socket): take the round emergency tug socket collar with its single broad hinged clamp, the railed catwalk and the amber battery guide lamps from it, using the socket close panel. Close view on a 50 mm lens at the height of the joint, the camera about 1.5 m from it and square to its side: two round collars already touch at the vertical seam in the centre of the frame, the wedge-shaped tug's plain round bow collar entering from frame-left and the emergency socket's round collar projecting from the foundry hull at frame-right. The socket's one broad hinged clamp stands open above its latch plate at the top of the seam, raised on its hinge at frame-right and angled up and away from the joint. Behind the joint a short stretch of the catwalk's railing and a row of small amber battery guide lamps fall softly out of focus against the black of space. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera stays fixed on the joint while the one broad hinged clamp begins to swing down from its open position on its hinge, the two collars staying pressed together; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, out of frame, says: Hard seal. 3-7 s: The clamp keeps swinging down in one steady arc and crosses the seam between the collars. 7-10 s: The clamp reaches its latch plate and seats against it in a last short turn of the hinge, the rims of both collars staying flush and the tug, the socket and the catwalk behind them rigid. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C86 — İki kardeş yeniden birlikte

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): yalnız kare/C86.png
```

> Not: Finalin duygusal merkezi. Kamera ÖN kurulumu: iki yüz, vizörler ve boş göğüs askısı okunur; Leon karenin solunda, Rhea sağında. Replikler R84 (Rhea, 1,0-2,5 s, vuruş 0-3) ve R85 (Leon, 3,0-4,5 s, vuruş 3-7); dudak yalnız kendi cümlesinde oynar, öteki ağzı kapalı.
> Askı boş (çekirdek kontrol odasındaki yuvada), bu yüzden 10.CEKIRDEK ve 15.ARACLAR çıkarıldı; kanopi dışı yalnız foundry'nin turuncu ışığı, 5 ve 6 çıkarıldı. Rhea'nın geçişi kesmede (kapanmış bağlantı üzerinden); karede iki kişi baştan oturuyor. Kare hareketin başı: kimse ötekine dönmemiş, Rhea ileri/aşağı bakıyor.
> Paneller: 1.LEON ve 2.RHEA `front full-body panel` (promptta `full-length front panel`, bkz. dosya başı).

### Görsel
```text
Reference 1 (the man): take his face, short dark brown hair, neat beard, pale left-temple scar, ivory suit with navy shoulders and orange upper-arm bands, and the closed clear ivory helmet from it, using the full-length front panel. Reference 2 (the woman): take her face, pearl suit with navy waist and teal upper-arm bands, graphite chest harness and the closed clear pearl helmet from it, using the full-length front panel. Reference 4 (tug cockpit): take the two-seat cockpit with its navy pilot seat on the left and engineer seat on the right, the low graphite console, the ivory overhead shell and the broad canopy with its two fixed graphite mullions from it, using the wide interior panel. Wide view inside the tug cockpit on a 28 mm lens at seated eye height, the camera at the front of the cabin just above the console, looking back at the two seats. Two adults sit side by side: on the left, an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet; on the right, an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Both sit upright and relaxed with their white gloves resting on their thighs, both helmets closed and both faces readable behind the clear visors; the man looks ahead toward the console and the woman looks slightly down, her graphite chest harness empty. The canopy curves around them, its two fixed mullions framing the glass at the edges of the frame. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Here the outside light is the warm orange glow of the foundry. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The woman lets out one slow exhale, her shoulders easing down, and turns her helmet toward the man beside her while his mouth stays closed; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: You came back. 3-7 s: The man turns his helmet toward her while her mouth stays closed; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: We're not finished. 7-10 s: Their eyes stay on each other while he lets out a slow breath in turn and his shoulders lower, both remaining seated, the camera keeping its wide steady frame. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C87 — Foundry bağlantısından ayrılma

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/14.ISKELE_v1.png · VİDEO (Frames to Video): yalnız kare/C87.png
```

> Not: Kadrajda insan yok. Tug solda burnu sağa, soket sağda; yaka açık ve ince bir aralık (hareket aralığı genişletir). Tether (plan devamlılık notu: iskelede bırakılır) karede gevşek sarılı, kanca iskele çapasında, tug'a bağlı DEĞİL; videoda yerinde kalır, tug hortum/tether çekmez.
> Kamera sabit; tug karenin sol yarısında olduğu için sola çekilirken kadrajda kalır. Replik R86 telsiz, Rhea, 1,5-4,5 s (vuruş 0-5 s). Dış klip: klip sesi yalnız replik penceresinde (T13).

### Görsel
```text
Reference 3 (the tug): take the wide wedge-shaped ivory hull, the dark graphite lower hull, the narrow orange bow stripe, the smoked blue-grey canopy and the round bow collar from it, using the side view panel. Reference 14 (service catwalk and socket): take the round emergency tug socket projecting from the foundry hull, the short railed catwalk, the magnetic boot plate, the single tether anchor and the amber battery guide lamps from it, using the catwalk wide panel. Side view on a 35 mm lens, the camera level with the tug's bow collar and about 20 m off to the side: the wedge-shaped tug at frame-left with its nose pointing right, and at frame-right the round emergency socket projecting from the foundry hull. The tug's bow collar is already unlatched and sits a thin gap away from the socket collar. Behind the socket the short railed catwalk runs back with a row of small amber battery guide lamps along it, and a slack navy safety tether, clipped at one end to the catwalk's rail anchor, lies coiled on the boot plate, not attached to the tug. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera stays fixed on the side view while the tug begins to draw straight back from the socket along its single docking axis, its unlatched collar sliding away so that the thin gap starts to widen; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, out of frame, says: We're clear. I still have the ark link. 5-8 s: The tug keeps drifting backward toward frame-left, the gap between the two collars opening wider, while the slack tether, the catwalk and the lamps stay exactly where they are. 8-10 s: The tug draws back until a clear gap about the width of its collar separates it from the socket, still moving gently away at the end. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C88 — Yolcu gemisine çıkış komutu

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C88.png
```

> Not: El-nesne teması ilk karede kurulu (eldiven anahtarın üstünde, anahtar üst konumda); videoda tek geniş anahtar tek kısa hareketle çevrilir. Arayüzde yazı yok: bilek bağlantısı işaretsiz, tek camgöbeği ışık. Yeni cihaz icat edilmez (plan §13.7): bu, K55-K56'da kurulan bilek bağlantısıdır.
> Kamera ÖN kurulumu, bel üstü iki kişi. Replikler R87 (Rhea, 1,0-2,5 s, vuruş 0-3) ve R88 (Leon, 3,0-4,0 s, vuruş 3-7). Askı boş. Dış ışık: foundry turuncusu.

### Görsel
```text
Reference 1 (the man): take his face, short dark brown hair, neat beard, pale left-temple scar, ivory suit with navy shoulders and orange upper-arm bands, and the closed clear ivory helmet from it, using the face close-up panel. Reference 2 (the woman): take her face, pearl suit with navy waist and teal upper-arm bands, graphite chest harness and the closed clear pearl helmet from it, using the face close-up panel. Reference 4 (tug cockpit): take the low graphite console with its short dual controls, the fixed wrist-link cradle at its right end, the ivory overhead shell and the canopy mullions from it, using the wide interior panel. Reference 15 (tools): take the unmarked ivory wrist-link with its one broad physical toggle and its cyan status light from it, using the wrist-link panel. Medium two-shot on a 50 mm lens at seated eye height, the camera at the front of the cabin just above the console, looking back at the two seats and framing both from the waist up. Two adults sit side by side: on the left, an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, his helmet turned a few degrees toward the woman, both white gloves resting on the short dual controls, ready; on the right, an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, her harness empty and her white glove already resting on the broad physical toggle of the ivory wrist-link seated in its cradle at the right end of the console, the toggle at its upper position and the link's single cyan status light lit, with no markings or readable display anywhere on it. Both helmets are closed, both faces readable behind the clear visors, both mouths closed. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Here the outside light is the warm orange glow of the foundry. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The woman's white glove presses the one broad toggle of the wrist-link over in a single short throw, her wrist turning with it, while the man's gloves stay ready on the dual controls and his mouth stays closed; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Sending the ark through. 3-7 s: The toggle settles at the end of its throw and the wrist-link's cyan light steadies, the camera easing in very slightly; her mouth stays closed, and the man's lips move only for his own line as he says in a low, dry adult man's voice, calm and guarded: Take everyone. 7-10 s: Her glove draws back from the toggle and her shoulders ease, while his gloves settle on the dual controls and his eyes lift toward the canopy. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C89 — Ark çıkışa ilerler

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C89.png
```

> Not: Kadrajda insan yok; replik yok. Dev yapılar rijit; ark soldan sağa tek düz rota (kaçış yönü), burun sağda. Ark C89'dan önce çıkış yakması yapmaz (plan §13.6): motorlar yalnız parlar, egzoz/duman yazılmaz. İki gantri kolu AÇIK ve ark'tan uzak, üç kepenk tamamen açık (plan devamlılığı).
> Tug "bir süre yerinde" kalır; yalnız son vuruşta ilk kıpırtı (C90 tug'ın kokpitinden başlar). Foundry referansında `clamps open panel` seçildi (kollar ark'ın iki yanında); kapı durumu metinde (üç kepenk tamamen açık) — panel kısmen kapalı kepenk gösterirse yeniden denemede `gate open panel`e geçilir.

### Görsel
```text
Reference 3 (the tug): take the wide wedge-shaped ivory hull with its dark graphite lower hull and narrow orange bow stripe from it, using the side view panel. Reference 5 (foundry): take the black C-shaped cradle, the two giant gantry clamp arms in their open state, the huge circular exit gate with its three rigid radial shutters, and the heavy blast ribs from it, using the clamps open panel. Reference 6 (the ark): take the long ivory segmented cylindrical hull, the grey dorsal rails, the six low rectangular cryo-habitat blocks, the two large blue rear engines and the long narrow forward canopy from it, using the side view panel. Wide exterior side view on a 24 mm lens, the camera level with the ark and far off to the side: the long ivory colony ark floats free at the centre of the black C-shaped foundry cradle with its nose pointing right toward the huge circular exit gate at frame-right, whose three rigid shutters are fully open; the two giant gantry clamp arms stand open on either side of the hull, clear of it. The ark's two large rear engines at frame-left glow bright blue. The small wedge-shaped tug sits on station at the lower left, behind and below the ark's stern. Far behind at frame-left the orange furnace trench glows beyond heavy blast ribs. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera stays fixed and wide while the long ivory ark begins to glide forward along a straight line toward the open gate at frame-right, its two rear engines glowing steady bright blue, and the small tug stays on station at the lower left. 3-7 s: The ark keeps gliding rightward on the same straight course, moving out from between the two open gantry arms, every hull block and the whole ring of the open gate staying rigid. 7-10 s: The ark's nose draws closer to the open gate as the slow glide carries it on, and the tug at the lower left begins to creep forward in its wake. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C90 — Tug ark'ın ardından hızlanır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C90.png
```

> Not: Kamera ARKA-YAN kurulumu: Leon'un koltuğunun arkasında ve solunda; sol yanağı ve sol şakak yarası yarım profilde, ağzı kısmen okunur (replik sırasında kaskını birkaç derece Rhea'ya çevirir). Rhea sağ koltukta, onun ötesinde.
> Replik R89, Leon, 1,5-3,0 s (vuruş 0-3 s). Tek hareket: Leon itiş kolunu kısa bir yay boyunca ilerletir; ileri görünüm kanopide yavaşça akar, tug ark'ı izler. Kanopide ark'ın iki mavi motoru ve uzakta açık kapı; dış ışık: ark motorlarının serin mavisi. Askı boş (kadrajda görünmez).
> Paneller: 1.LEON ve 2.RHEA `side full-body panel` (promptta `full-length side panel`, bkz. dosya başı).

### Görsel
```text
Reference 1 (the man): take his face, short dark brown hair, neat beard, pale left-temple scar, ivory suit with navy shoulders and orange upper-arm bands, and the closed clear ivory helmet from it, using the full-length side panel. Reference 2 (the woman): take her face, pearl suit with navy waist and teal upper-arm bands and the closed clear pearl helmet from it, using the full-length side panel. Reference 4 (tug cockpit): take the two-seat cockpit, the short dual controls, the low graphite console and the broad canopy with its two fixed graphite mullions from it, using the wide interior panel. Reference 5 (foundry): take the huge circular exit gate with its three rigid shutters fully open from it, using the gate open panel. Reference 6 (the ark): take the ivory stern and the two large blue rear engines from it, using the stern panel. Wide view inside the tug cockpit on a 28 mm lens at seated eye height, the camera behind and slightly left of the man's seat, looking forward through the broad canopy. Two adults sit side by side facing forward: on the left, an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, seen from behind-left in three-quarter profile so that his left cheek and pale scar are readable through the clear visor, both white gloves resting on the short dual controls with one on the thrust control at its rear stop; on the right, an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, seen in three-quarter profile beyond him, her white gloves in her lap. Ahead through the canopy's two fixed mullions, the ivory ark's two large rear engines glow blue in open space, and its long hull recedes toward the fully open exit gate in the distance. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Here the outside light through the canopy is the cool blue glow of the ark's engines. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The man's glove on the thrust control begins to push it forward along its short arc, his forearm and shoulder moving with it, as his helmet turns a few degrees toward the woman and he says in a low, dry adult man's voice, calm and guarded: Stay behind her hull. 3-7 s: The control travels on through the middle of its arc and the forward view through the canopy begins to move gently ahead as the tug follows the ark; the woman stays seated beside him, watching the ark. 7-10 s: The control reaches the end of its arc and his glove settles on it while the tug glides on behind the ark, the forward view still moving gently ahead. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C91 — Büyük gemi kapıdan çıkar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C91.png
```

> Not: Kadrajda insan yok; replik yok. Plan "side-wide gate": hafif eğik yan açı (açıklık geniş elips okunur, üç kepenk görünür). Hareket yalnız ark'ın kıç motor bölümünün kapıdan çıkması; gövde blokları (altı) ve sabit açıklık korunur. Kapıdaki mekanik mandal oturmuş, kepenkler tamamen açık, iki gantri kolu açık ve ark'tan uzak (plan devamlılığı).
> Plan ön üretim denemesi listesinde K91 var (büyük ark geçişi): ilk denenecek çekimlerden biri. Karar kararsız çıkarsa daha küçük yer değiştirme (yalnız son motor bölümü) ile yeniden dene.

### Görsel
```text
Reference 5 (foundry): take the huge circular exit gate with its three rigid radial shutters fully slid open and the mechanical catch seated, the black C-shaped cradle with its two giant gantry clamp arms standing open, and the heavy blast ribs from it, using the gate open panel. Reference 6 (the ark): take the long ivory segmented cylindrical hull, the grey dorsal rails, the six low rectangular cryo-habitat blocks and the two large blue rear engines from it, using the side view panel. Wide view on a 24 mm lens from a slightly oblique side angle, the camera level with the gate and far off to the side: the huge circular exit gate stands at the centre-right of the frame with its three rigid shutters fully open and the aperture reading as a wide ellipse, and the long ivory colony ark passes through it from left to right with its nose pointing right, its whole hull with the six cryo-habitat blocks already beyond the gate in open space and only the stern engine section with the two large blue rear engines still inside the aperture. At frame-left inside the foundry the two giant gantry clamp arms stand open and clear, and the orange furnace trench glows beyond the heavy blast ribs. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera stays fixed as the long ivory ark glides on to the right through the open aperture, its hull blocks moving together as one rigid piece. 3-7 s: The stern engine section slides up to the edge of the aperture and begins to clear it, the two large blue rear engines gliding out past the ring of the gate. 7-10 s: The last of the stern clears the gate and the ark drifts on into open space at frame-right, the open gate, its three shutters and the clamp arms staying exactly in place behind it. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C92 — Tug da kurtulur; purge arkada kalır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C92.png
```

> Not: Kadrajda insan yok; replik yok. Purge, vakumda duman/alev değil, kaburgaların arkasında tek, sınırlı turuncu ışık atımı olarak yazıldı (BILINEN_TUZAKLAR §B sıra 4); iki gemiden uzak, gövdelere değmez, patlama ve çöküş yok. Kare hareketin başı: fırın ışığı sabit ve loş, tug dudakta.
> Kamera sabit, kapının dışından; kapı karenin solunda, gemiler soldan sağa (kaçış yönü). Dış klip: klip sesi kurguda açılmaz (replik yok, Y1 yatağı).

### Görsel
```text
Reference 3 (the tug): take the wide wedge-shaped ivory hull, the dark graphite lower hull, the narrow orange bow stripe and the smoked blue-grey canopy from it, using the side view panel. Reference 5 (foundry): take the huge circular exit gate with its three rigid radial shutters fully open, the mechanical catch seated and the heavy blast ribs inside it from it, using the gate open panel. Reference 6 (the ark): take the long ivory segmented cylindrical hull, the grey dorsal rails, the six low rectangular cryo-habitat blocks and the two large blue rear engines from it, using the side view panel. Wide view from outside the foundry on a 24 mm lens, the camera level with the exit gate and some distance off its axis: at frame-left the huge circular exit gate stands seen at a three-quarter angle with its three rigid shutters fully open, and through the open aperture a steady, dim orange furnace glow shows behind the heavy blast ribs inside the foundry. The small wedge-shaped tug, nose pointing right, sits at the outer lip of the gate just beyond the aperture; farther ahead at frame-right the long ivory ark travels away toward open space, its two large rear engines glowing blue. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera stays fixed as the small tug at the outer lip of the open gate begins to pull ahead out of the aperture toward frame-right, its nose leading, while the long ivory ark keeps travelling on far ahead. 3-7 s: The tug moves fully clear of the gate's aperture, and behind the fixed blast ribs inside the foundry the orange furnace light starts to swell in one contained pulse, far from both ships. 7-10 s: The tug glides on away from the gate toward the ark as the orange pulse reaches its height behind the ribs and then softens, the gate, the ribs and the ark's course unchanged. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C93 — Yolcuların güvenlik teyidi

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/6.ARK_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C93.png
```

> Not: Kamera ARKA-YAN kurulumu, sağ taraftan: Rhea kameraya en yakın (karenin sağı), sağ yanağı ve sağ çene yarası okunur; Leon onun ötesinde (karenin solu). Ark kanopide, omzunun üstünden, serbest uzayda küçük ve sakin. Gösterge okunmaz: bilek bağlantısı işaretsiz, tek camgöbeği ışık.
> Replik R90, Rhea, 1,5-4,0 s (vuruş 0-4 s). Plan 5.FOUNDRY'yi listeler; serbest uzayda foundry kadrajda olmadığı için çıkarıldı. Dış ışık: soğuk yıldız ışığı (plan "cool starlight"). Kare hareketin başı: Rhea'nın sağ omzu hafif kalkık, Leon'un eldivenleri kumandada gevşek.

### Görsel
```text
Reference 1 (the man): take his face, short dark brown hair, neat beard, pale left-temple scar, ivory suit with navy shoulders and orange upper-arm bands, and the closed clear ivory helmet from it, using the face close-up panel. Reference 2 (the woman): take her face, pearl suit with navy waist and teal upper-arm bands, graphite chest harness and the closed clear pearl helmet from it, using the face close-up panel. Reference 4 (tug cockpit): take the low graphite console with its short dual controls, the fixed wrist-link cradle at its right end, the ivory overhead shell and the broad canopy with its two fixed graphite mullions from it, using the wide interior panel. Reference 6 (the ark): take the long ivory segmented hull and the two large blue rear engines from it, using the side view panel. Reference 15 (tools): take the unmarked ivory wrist-link with its one broad physical toggle and its cyan status light from it, using the wrist-link panel. Medium two-shot on a 50 mm lens at seated eye height, the camera at the right side of the cabin just behind the woman's seat, looking forward-left across her toward the man. Two adults sit side by side facing the canopy: on the right of the frame, nearest the camera, an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, her helmet turned a little toward the ivory wrist-link seated in its cradle at the right end of the console so that her right cheek, her right-chin scar and her mouth are readable through the clear visor, her right shoulder raised slightly, the link's single cyan indicator lit with no readable display or marking on it; on the left of the frame beyond her, an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, seen in three-quarter profile with both white gloves loose on the short dual controls. Through the canopy ahead of them, over the woman's shoulder, the long ivory ark floats in open space among sparse stars, its two large rear engines glowing blue. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Here the outside light is cool white starlight. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The woman's helmet turns slightly further toward the ivory wrist-link and her eyes settle on its steady cyan light as she checks it, her raised right shoulder beginning to ease, while the man's mouth stays closed; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: All four thousand sleeper signals stable. 4-7 s: A slow breath leaves her and her right shoulder drops, relaxing fully, the camera easing in very slightly. 7-10 s: The man's white gloves tighten a little on the dual controls and settle, steadying them, his eyes on the ark ahead through the canopy, while her shoulder stays relaxed and her gaze lifts from the wrist-link to the canopy. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C94 — Çalınan çekirdeğin son hâli

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C94.png
```

> Not: Kadrajda insan yok; el yok. Sönük, yanık çekirdek AYNI yuvada kilitli (C58'de oturdu, C69'da tükendi); tug'a geri dönmez. Üç kol aşağıda ve kilitli (mavi kapı-güç, turuncu mandal, teal kelepçe A), turuncu mandal kolu yuvanın yanında. Hiçbir şey ısınmaz, parlamaz ya da hareket etmez: video yalnız yavaş kamera itişidir, çekirdeğin camı karanlık kalır.
> Replik R91: Leon voice-over, 1,5-3,0 s (vuruş 0-4 s); konuşan kadrajda yok, §3 voice-over cümlesi birebir (tek adlı cümle). Panel: 10.CEKIRDEK `core spent panel`, 12.KONTROL_ODASI `levers down panel`.

### Görsel
```text
Reference 10 (the spent core): take the compact rectangular graphite casing with ivory corner guards, the single rigid top carry handle and the dark glass centre, heat-scored and scorched, from it, using the core spent panel. Reference 12 (gate-control room): take the low console, the matching rectangular input cradle with its broad retaining latch, the small bus connector, and the three hinged levers in their down positions from it, using the levers down panel. Close view on a 50 mm lens, the camera about 50 cm from the console edge and slightly above the cradle, looking down at it at a gentle angle: the spent portable core sits latched in its input cradle at the centre of the frame, its graphite casing heat-scored dark, its glass centre dark, the broad retaining latch closed over the casing. At frame-right beside the cradle the orange gate-catch lever stands down at its lower stop next to the blue gate-power lever and the teal clamp lever, all three levers down and latched. The wall behind the console falls into soft shadow, and along the far edge a strip of the room's rear window carries a cool blue glow. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera starts a slow, steady push in toward the latched core, amber lamp reflections gliding across its scorched casing; Leon's low, dry voice as a calm voice-over says: No core. No payday. 4-7 s: The push continues across the heat-scored edge of the casing and the ivory corner guards, the reflections shifting with the camera's parallax. 7-10 s: The push closes in on the dark glass centre of the core until it fills the middle of the frame, a faint amber lamp reflection sliding across it, while the casing, the latch and the three levers stay rigid. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C95 — Yeni ortaklık

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): yalnız kare/C95.png
```

> Not: Kamera ÖN kurulumu, yakın iki kişi (85 mm, baş-göğüs); Leon karenin solunda, Rhea sağında; iki yüz ve ağız okunur. Replikler R92 (Leon, 1,0-2,5 s, vuruş 0-3) ve R93 (Rhea, 3,0-5,0 s, vuruş 3-7); dudak yalnız kendi cümlesinde oynar. Askı boş: göğüs askısının üst kenarı karenin altında.
> 10.CEKIRDEK ve 15.ARACLAR çıkarıldı (askı boş, araç yok). Dış ışık: gaz devinin yumuşak mavisi (plan "blue planet light"). Kare hareketin başı: Leon'un yüzü nötr ve yorgun, Rhea ileri bakıyor; yarım gülümseme ve bakış buluşması videoda. Yakın plan şeffaf vizörde yüz: risk notu, §4 Risk sütununda zaten "iki replik ağız kadrajda".

### Görsel
```text
Reference 1 (the man): take his face, short dark brown hair, neat beard, pale left-temple scar, ivory suit with navy shoulders and orange upper-arm bands, and the closed clear ivory helmet from it, using the face close-up panel. Reference 2 (the woman): take her face, pearl suit with navy waist and teal upper-arm bands, graphite chest harness and the closed clear pearl helmet from it, using the face close-up panel. Reference 4 (tug cockpit): take the ivory overhead shell, the canopy mullions and the console edge from it, using the wide interior panel. Close two-shot on an 85 mm lens at seated eye height, the camera at the front of the cabin near the console, looking back at the two seats, framed from the tops of the helmets to the chest. Two adults sit side by side: on the left, an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet; on the right, an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, the top edge of her empty graphite chest harness crossing the bottom of the frame. Both helmets are closed, both faces calm and readable behind the clear visors, both mouths closed, the man's expression neutral and tired and the woman looking ahead. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Here the outside light is the soft blue glow of the huge curved blue gas giant, resting on both visors. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The man's mouth eases into a small tired half-smile as his shoulders drop a little, while her mouth stays closed; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: Terrible salvage margin. 3-7 s: The woman's eyes come across to meet his and the corners of her eyes soften while his mouth stays closed; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Good day to be thieves. 7-10 s: Their eyes stay on each other as both faces ease into a calm, tired warmth and each lets out a slow breath, the camera keeping its close steady frame. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C96 — Özgür iki gemi

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C96.png
```

> Not: Final aşırı geniş; kadrajda kimse yok, iki telsiz replik (R94 Rhea 1,0-2,0 s · R95 Leon 2,5-4,5 s, ikisi de 0-5 s vuruşunda). Yeni tehdit, gezegen ya da gemi yok: ark ve tug aynı güvenli rotada, soldan sağa (kaçış yönü), uzaktaki foundry küçük ve solda, kapısı açık. Gaz devi arkada, ışık cümlesindeki aynı dev mavi gezegen.
> Ark'ın motorları yalnız parlar (egzoz yok). Dış klip: klip sesi yalnız replik penceresinde (T13). C95→C96 karışım notu dosya başında. Film adı/son kart bu klibin içinde olabilir (plan §12) — kurguda eklenir, promptta yazı yok.

### Görsel
```text
Reference 3 (the tug): take the wide wedge-shaped ivory hull, the dark graphite lower hull, the narrow orange bow stripe and the smoked blue-grey canopy from it, using the side view panel. Reference 5 (foundry): take the distant black C-shaped cradle with its open exit gate from it, using the gate open panel. Reference 6 (the ark): take the long ivory segmented cylindrical hull, the grey dorsal rails, the six low rectangular cryo-habitat blocks and the two large blue rear engines from it, using the side view panel. Extreme wide exterior view on a 14 mm lens, the camera far out in open space, level with the two ships. The long ivory colony ark travels at the centre-right of the frame with its nose pointing right, its two large rear engines glowing blue, and the small wedge-shaped tug flies close behind its stern at the same height, both on the same straight course. At the far left the distant black C-shaped foundry lies small, its exit gate open and a warm orange glow behind its heavy blast ribs. An immense curved blue gas giant fills the background behind them. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera begins a slow pullback while the ivory ark and the small tug glide together toward frame-right on the same course, the tug keeping its place behind the ark's stern; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, out of frame, says: Where now? A low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, out of frame, says: Somewhere they can wake up. 5-10 s: The pullback continues, widening the frame so the two ships grow smaller against the huge blue gas giant while the distant foundry shrinks further at the far left, both ships still sliding steadily toward frame-right on the same course. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini ile görselden video 10 s hedefler (`FILM.md` künye URETIM). Omni süresi ve ses davranışı SMOKE P11 · P14 · P18'de ölçülür (`uretim_hatti/FLOW_GERCEKLERI.md`); ölçüm gelmeden videolar koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9.
> **Replikli klipler (bu grupta C85 · C86 · C87 · C88 · C90 · C93 · C94 · C95 · C96):** replik klipte yanlış ya da bozuk duyulursa o klibin sesi kurguda eklenir (timeline `ses` parçası); kurgu kaydı yedek.
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde, panel adı parantezde. Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.
> **Önce denenecek (plan §13 ön üretim denemesi):** C85 (ikinci yanaşma kelepçesi) ve C91 (büyük ark kapıdan geçişi); kararsız çıkarsa aynı eylem daha küçük yer değiştirmeyle yeniden denenir, prompta cümle eklenmez.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C85 kare | `kare/C85.png` | Görsel | ref/14.ISKELE_v1.png (soket yakın paneli) | 2 | |
| 2 | C86 kare | `kare/C86.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/2.RHEA_v1.png (önden tam boy paneli) · ref/4.KOKPIT_v1.png (geniş iç panel; bu sırayla) | 2 | |
| 3 | C87 kare | `kare/C87.png` | Görsel | ref/3.KESTREL_v1.png (yan görünüş paneli) · ref/14.ISKELE_v1.png (iskele geniş paneli; bu sırayla) | 2 | |
| 4 | C88 kare | `kare/C88.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/2.RHEA_v1.png (yüz yakın paneli) · ref/4.KOKPIT_v1.png (geniş iç panel) · ref/15.ARACLAR_v1.png (bilek bağlantısı paneli; bu sırayla) | 2 | |
| 5 | C89 kare | `kare/C89.png` | Görsel | ref/3.KESTREL_v1.png (yan görünüş paneli) · ref/5.FOUNDRY_v1.png (kelepçeler açık paneli) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 6 | C90 kare | `kare/C90.png` | Görsel | ref/1.LEON_v1.png (yandan tam boy paneli) · ref/2.RHEA_v1.png (yandan tam boy paneli) · ref/4.KOKPIT_v1.png (geniş iç panel) · ref/5.FOUNDRY_v1.png (kapı açık paneli) · ref/6.ARK_v1.png (kıç paneli; bu sırayla) | 2 | |
| 7 | C91 kare | `kare/C91.png` | Görsel | ref/5.FOUNDRY_v1.png (kapı açık paneli) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 8 | C92 kare | `kare/C92.png` | Görsel | ref/3.KESTREL_v1.png (yan görünüş paneli) · ref/5.FOUNDRY_v1.png (kapı açık paneli) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 9 | C93 kare | `kare/C93.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/2.RHEA_v1.png (yüz yakın paneli) · ref/4.KOKPIT_v1.png (geniş iç panel) · ref/6.ARK_v1.png (yan görünüş paneli) · ref/15.ARACLAR_v1.png (bilek bağlantısı paneli; bu sırayla) | 2 | |
| 10 | C94 kare | `kare/C94.png` | Görsel | ref/10.CEKIRDEK_v1.png (tükenmiş çekirdek paneli) · ref/12.KONTROL_ODASI_v1.png (kollar aşağıda paneli; bu sırayla) | 2 | |
| 11 | C95 kare | `kare/C95.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/2.RHEA_v1.png (yüz yakın paneli) · ref/4.KOKPIT_v1.png (geniş iç panel; bu sırayla) | 2 | |
| 12 | C96 kare | `kare/C96.png` | Görsel | ref/3.KESTREL_v1.png (yan görünüş paneli) · ref/5.FOUNDRY_v1.png (kapı açık paneli) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 13 | C85 | `ham/C85_d1.mp4` | Frames to Video | kare/C85.png · **önce denenir (plan §13)** | 2 | |
| 14 | C86 | `ham/C86_d1.mp4` | Frames to Video | kare/C86.png | 2 | |
| 15 | C87 | `ham/C87_d1.mp4` | Frames to Video | kare/C87.png | 2 | |
| 16 | C88 | `ham/C88_d1.mp4` | Frames to Video | kare/C88.png | 2 | |
| 17 | C89 | `ham/C89_d1.mp4` | Frames to Video | kare/C89.png | 2 | |
| 18 | C90 | `ham/C90_d1.mp4` | Frames to Video | kare/C90.png | 2 | |
| 19 | C91 | `ham/C91_d1.mp4` | Frames to Video | kare/C91.png · **önce denenir (plan §13)** | 2 | |
| 20 | C92 | `ham/C92_d1.mp4` | Frames to Video | kare/C92.png | 2 | |
| 21 | C93 | `ham/C93_d1.mp4` | Frames to Video | kare/C93.png | 2 | |
| 22 | C94 | `ham/C94_d1.mp4` | Frames to Video | kare/C94.png | 2 | |
| 23 | C95 | `ham/C95_d1.mp4` | Frames to Video | kare/C95.png | 2 | |
| 24 | C96 | `ham/C96_d1.mp4` | Frames to Video | kare/C96.png | 2 | |
