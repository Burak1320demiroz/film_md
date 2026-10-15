# 🖼️ THE_FURNACE_GATE — Prompt grubu G04 (çekimler C37–C48)

> Yazan: goruntu-yonetmeni (tur 1). Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K37–K48 + `FILM.md` §3 (sabit cümleler) · §4 (çekim listesi) · §5 (replikler).
> Bu dosya yeniden tasarım değil, biçim çevirisidir: kompozisyon, olay ve hareket yönü planın kendisi; cümleler olabildiğince planın İngilizcesi.
> Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. Olumsuz yasak listesi yazılmaz. ≤4.300 karakter.
> Zincir yok (`FILM.md` §4 Zincir sütunu "—"); her çekim kendi başlangıç karesiyle Frames to Video. `EKLE` satırı iki parçalıdır: KARE (görsel üretimi için referanslar) · VİDEO (yalnız kare;
> Frames to Video'ya referans eklenmez, yoksa mod Ingredients'e kayar).
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında `Reference <No> (<rol>): …` diye adlandırılır, çekim hangi
> paneli kullanacaksa `using the … panel` der (çekim başına her referanstan yalnız TEK panel; panel adları `FILM.md` §3). Her video promptu 10 s'yi 2-4 vuruşa böler (0'da başlar, 10'da biter,
> boşluksuz, vuruş ≥2 s, son vuruş donmaz; ilk vuruş hareketle başlar).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** `FILM.md` §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir; MEKÂN IŞIĞI cümlesi her görsel promptta
> `The light is …` sarmalayıcısıyla (kelimeler §3'teki gibi); ORTAM SESİ cümlesi o mekânın her video promptunda birebir (ortak görünümden hemen önce). Bu grubun on iki çekiminde de §5 Kaynak = model sesi:
> replik video promptuna birebir `says: <line>` biçiminde yazılır (tırnaklı biçim SMOKE P9'a kadar yedek), konuşanın sesi `FILM.md` §3 SES KİMLİĞİ kelimeleriyle tarif edilir, replik vuruşun SON cümlesidir
> (sonraki vuruş etiketi repliğin bittiğini gösterir), konuşmayan kişinin ağzı o vuruşta kapalı yazılır. Telsiz ekidir `softened by a light suit-radio filter`; voice-over `as a calm voice-over`.
> **Ortak cümleler bu grupta birebir (`FILM.md` §3 KİMLİK TABANI):** adlar yerine `the man` / `the woman`;
> erkek tabanı `an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet`;
> kadın tabanı `an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet`;
> eldivenler kadrajdaysa ayrı cümle `white gloves`. Taraf dili ekran tarafıdır (plan: "Leon solda, Rhea sağda"): pilot koltuğu kare solunda, mühendis koltuğu kare sağında; her kişinin kendi kumandası yanında.
> **Kokpit kamerası:** kamera koltuklara bakar (yüzler okunur); çekirdek yalnız kadrajdaysa yazılır. Kanopi ve ark yalnız plan istediği çekimlerde (C41 · C46) arka planda görünür; öbür kokpit çekimlerinde arka plan
> fildişi tavan kabuğudur.
> **Kelime güvenliği (BILINEN_TUZAKLAR §A):** `body` sözcüğü ve türevleri hiçbir promptta geçmez (yerine torso / shoulders / figure); egzoz ve kıvılcım yerine ışık atımı yazılır. Tek istisna repliklerin kendi metni (R38 `dead`, aşağıda risk).
> **Çıkarılan plan kalıpları** (NOTLAR KARARLAR sapma 3): "Use the attached reference images only…", "Create one film still, not a reference sheet", "horizontal 16:9", "Animate the uploaded scene still as the first frame", "10 seconds",
> "No readable text…" olumsuz kuyruğu, "No spoken dialogue…", "No new people…", "Continuity overrides…" bloğu, "Generate only appropriate…" ses satırı, "Exactly N visible adults" etiketi (yerine `the two of them are the only people in the cockpit`).

---

## C37 — Rhea bilek bağlantısını kanopiye çevirir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C37.png (referans eklenmez)
```

> Not: Replik R38, Rhea, ağız kadrajda, 1.5-5.5 s (4.0 s); vuruş 2-7 s'in son cümlesi. Leon kadraj dışı. `FILM.md` §4 referansında 10.CEKIRDEK de var; ÇIKARILDI: çekirdek 2.RHEA'nın
> `harness with core panel`ında askıda kilitli gelir, ayrı çekirdek sayfası aynı nesneye ikinci tasarım çağırır. Plan "no readable map" olumsuzu pozitife çevrildi: bilek bağlantısında yalnız tek düz camgöbeği durum ışığı
> (15.ARACLAR bilek bağlantısı işaretsiz, ekran yok). Kanopi kadraj dışı: bilek kamera yönüne (kanopiye) açılır. Kare hareketin başı: kol konsol kenarında, bilek henüz açılmadı.
> Risk: replik `dead` sözcüğü taşıyor (makine bağlamı, planın repliği); red gelirse replik kurguda eklenir (kayıt yedek) ve bu vuruştan çıkarılır.

### Görsel
```text
Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and the navy waist, the blue-gold badge, and the graphite core-carry harness with the locked core from it, using the harness with core panel. Reference 4 (cockpit): take the engineer seat, the ivory overhead shell, the low graphite console with its soft cyan lights and the small unmarked wrist-link socket from it, using the engineer side panel. Reference 15 (accessories): take the ivory unmarked wrist-link with its broad physical toggle and single cyan status light from it, using the wrist-link panel. Medium shot on a 50 mm lens at eye level with the camera facing a seated woman: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She sits at frame-right in the engineer seat, framed from the top of her helmet to her waist, her head turned slightly toward frame-left, her green eyes lowered to the wrist-link and her mouth closed. She wears white gloves. The locked graphite core with its amber glass center rides in the harness over her chest. Her forearm rests across the console's edge at the bottom of the frame, and the ivory wrist-link on her wrist glows with one plain, soft cyan status light, its broad physical toggle unmarked. Behind her the ivory overhead shell and the engineer seat's headrest fall softly out of focus. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow push-in toward her begins as she lifts her forearm from the console's edge, the wrist-link's soft cyan light rising with it. 2-7 s: She angles the wrist-link outward toward the broad canopy ahead of her while the push carries on, the cyan light staying plain and unmarked on her white glove; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: The gate drive is dead. The capture locks are still powered. 7-10 s: The push eases closer while she keeps the wrist-link angled toward the canopy and her eyes follow it, her breathing slow and steady, the locked core riding steady on her harness. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C38 — Leon, kadraj dışındaki Rhea'ya bakar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C38.png (referans eklenmez)
```

> Not: Replik R39, Leon, ağız kadrajda, 1.5-5.0 s; Rhea kadraj dışında (sağda). `FILM.md` §4 Risk gereği plan ışık kaynağı kokpite uyarlandı: plan "cryo green lights … from the nearby ark corridor" kokpitte yok →
> ark kanopinin dışında, vizörün üst kenarında yumuşak yeşil yansıma (yalnız renk lekesi; şekil tarif edilmedi, HUD/yazı çağırmasın). Ark ve foundry kadrajda olmadığı için 5.FOUNDRY · 6.ARK ÇIKARILDI.
> Yara sol şakakta: baş kare sağına dönük, yara yüzün sağ kenarında. Vuruşlar: 0-2 · 2-6 · 6-10 (replik 2-6 s içinde).

### Görsel
```text
Reference 1 (man): take his face with the short dark brown hair, neat beard and pale left-temple scar, and his ivory pressure suit with the navy shoulders and the clear ivory helmet from it, using the face close-up panel. Reference 4 (cockpit): take the navy pilot seat, the ivory overhead shell and the amber lamps from it, using the pilot side panel. Close-up on an 85 mm lens at eye level with the camera facing a seated man: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits at frame-left in the navy pilot seat, framed from the top of his helmet to the middle of his chest, his head turned slightly toward frame-right, his brown eyes fixed on someone out of frame at frame-right and his mouth closed; his pale left-temple scar shows at the frame-right edge of his face behind the clear visor. A faint green glow from the ark outside the canopy lies as a soft reflection across the upper edge of his clear visor. Behind him the ivory overhead shell and one amber lamp fall softly out of focus. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow, small camera drift toward frame-right begins while his eyes stay on the engineer seat out of frame, the faint green reflection sliding across his visor. 2-6 s: The drift carries on and his lips move only for his own line; he says in a low, dry adult man's voice, calm and guarded: How did a ship full of people become scrap? 6-10 s: His mouth closes and his brow draws slightly together, his eyes still on the seat out of frame, the drift slowing gently as the green reflection fades from the visor. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C39 — Rhea gerçeği söyler

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C39.png (referans eklenmez)
```

> Not: Replik R40, Rhea, ağız kadrajda, 1.5-4.0 s; Leon kadraj dışı. 10.CEKIRDEK ÇIKARILDI: plan "yüz + teal bant" istiyor, kadraj baştan omuzlara kadar, çekirdek kadrajda değil (kadrajda olmayan tarif edilmez).
> Plan "restrained push" tek kamera hareketi: kamera 3 vuruşun hepsinde yavaş itişte (ilk vuruş zaten hareketli). Kare Leon'un yakın planının ters açısı: Rhea baş hafif sola dönük, yara sağ çenede
> (kare solundaki çene kenarı). Teal bant sol üst kolda, kadrajın sağ altında.

### Görsel
```text
Reference 2 (woman): take her face with the green eyes and the small right-chin scar, her pearl pressure suit with the teal upper-arm bands and the blue-gold badge, and the clear pearl helmet from it, using the face close-up panel. Reference 4 (cockpit): take the engineer seat's headrest, the ivory overhead shell and the amber lamps from it, using the engineer side panel. Close-up on an 85 mm lens at eye level with the camera facing a seated woman: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She sits in the engineer seat with her head in the right half of the frame, framed from the top of her helmet down to her upper arms. Her face is turned slightly toward frame-left in three-quarter view, her mouth closed and her green eyes steady and guarded behind the clear visor; her small right-chin scar shows at the frame-left edge of her chin. A narrow pale teal band circles her left upper arm at the lower frame-right edge. Behind her the ivory overhead shell and one amber lamp fall softly out of focus. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow, restrained camera push-in toward her face begins while her guarded eyes stay on the pilot seat out of frame at frame-left and a slow breath lifts her shoulders. 2-6 s: The push carries on and her lips move only for her own line; she says in a clear, quick adult woman's voice, precise and controlled: I wrote the original cargo classifier. 6-10 s: Her mouth closes and her expression settles, the tension leaving her brow and jaw until her look is steady and resolved, while the push closes in a little further and the teal band stays at the lower edge of the frame. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C40 — Tasarım ile suistimal ayrımı

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C40.png (referans eklenmez)
```

> Not: İki replik, ikisi ağız kadrajda: R41 Rhea 1.0-4.0 s (vuruş 0-4 s'in son cümlesi) → R42 Leon 4.5-6.0 s (vuruş 4-7 s'in son cümlesi); her vuruşta öteki kişinin ağzı kapalı yazıldı.
> 10.CEKIRDEK ÇIKARILDI (çekirdek 2.RHEA `harness with core panel`ında). İki kişilik çekim: kimlikler tek özne sayfalarından (plan R03 ikili sayfa kaldırıldı), Leon solda, Rhea sağda; medyum iki kişide ikisi için
> `front full-body`/`harness with core` panelleri (giysi işaretleri okunsun; yüz bu ölçekte küçük). Plan "core between their sightlines": çekirdek Rhea'nın göğsünde, bakış hattının hemen altında.
> Plan "Rhea remains still": son vuruşta `remains still` yazılmadı (film_dogrula DONMA uyarısı); yerine yalnız nefesi hareket eder.

### Görsel
```text
Reference 1 (man): take his face, his ivory pressure suit with the navy shoulders and orange upper-arm bands, the blue-gold hawk badge and the white gloves from it, using the front full-body panel. Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and navy waist, and the graphite core-carry harness with the locked core from it, using the harness with core panel. Reference 4 (cockpit): take the 2 seats, the ivory overhead shell, the low graphite console and its soft cyan lights from it, using the wide interior panel. Medium two-shot on a 35 mm lens at eye level with the camera facing the seats; the two of them are the only people in the cockpit. At frame-left in the navy pilot seat sits an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, and at frame-right in the engineer seat sits an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Both are framed from the top of their helmets to their waists with a forearm's width of space between the seats. The man's helmet is turned toward her and his brown eyes are on her face; her helmet is turned slightly toward him, her green eyes meeting his and her mouth closed. Both wear white gloves resting on their thighs. The locked graphite core with its amber glass center rides in the harness over her chest, just below the line between their eyes. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow, small push-in begins toward the space between the two seats as the man's helmet stays turned toward the woman, his eyes on hers and his mouth closed; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: It had a human-safety veto. Someone removed it. 4-7 s: The push carries on while the woman keeps her eyes on his and her mouth closed; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: You knew the architecture. 7-10 s: The push eases closer between them, his eyes on hers, only her breathing moving as the locked core rises and falls gently with it, both mouths closed. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C41 — Rhea bakışını ark'a çevirir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C41.png (referans eklenmez)
```

> Not: Replik R43, Rhea, ağız kadrajda, 1.5-5.0 s (vuruş 2-7 s'in son cümlesi); bakış dönüşü cümlenin ortasında. 10.CEKIRDEK ÇIKARILDI (çekirdek `harness with core panel`ında).
> Plan "captured ark visible through canopy behind": ark kanopide Rhea'nın arkasında, planın ekran düzeni korunur. Rhea karenin sol üçte birinde: bakışı Leon'dan (kare solu, kadraj dışı) ark'a (kare sağı) dönebilsin.
> Kanopinin ötesi dış çekimdir: MEKÂN IŞIĞI kokpit cümlesi + dış (DIŞ) cümlesi birebir iki ayrı cümlede (T18). Ark ve kradle rijit kalır, kapılar kadraj dışı.

### Görsel
```text
Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and navy waist, and the graphite core-carry harness with the locked core from it, using the harness with core panel. Reference 4 (cockpit): take the engineer seat, the ivory overhead shell and the broad canopy with its 2 fixed graphite mullions from it, using the wide interior panel. Reference 5 (foundry): take the black C-shaped cradle with its heavy blast ribs from it, using the wide exterior panel. Reference 6 (colony ark): take the long ivory segmented hull with its 6 low cryo-habitat blocks from it, using the side view panel. Medium shot on a 50 mm lens at eye level with the camera facing a seated woman: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She sits in the engineer seat in the left third of the frame, framed from the top of her helmet to her waist, her face turned in three-quarter view toward frame-left with her green eyes on the pilot seat out of frame and her mouth closed. She wears white gloves resting on her thighs. The locked graphite core with its amber glass center rides in the harness over her chest. Behind her at frame-right the broad canopy, crossed by one fixed graphite mullion, shows the long ivory hull of the colony ark running toward its bow at the right edge of the frame, with the black foundry cradle curving away beyond it. The light inside is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy; the light outside is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow push-in toward her begins as her eyes rest on the pilot seat out of frame at frame-left, a slow breath lifting the harness with the locked core. 2-7 s: Her eyes turn slowly from frame-left toward the ark beyond the canopy at frame-right, her head following by only a few degrees, and her lips move only for her own line; she says in a clear, quick adult woman's voice, precise and controlled: I didn't know what they'd done. Now I do. 7-10 s: Her mouth closes and her eyes rest on the ark's long hull beyond the glass while the push eases closer, the ark, the cradle and the canopy mullion staying rigid. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C42 — Leon tether bağlantısını kavrar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/4.KOKPIT_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C42.png (referans eklenmez)
```

> Not: Replik R44, Rhea, TELSİZ: kadraj dışı, Leon'un ağzı kapalı (tırnaksız `says:` biçimi; telsiz eki `softened by a light suit-radio filter`). Replik 1.5-6.0 s → vuruş 2-7 s'in son cümlesi; kavrama replikten SONRA,
> son vuruşta (öncesi tepki, sonrası gevşeme). T01 temas: eldiven tether bloğunun üstünde KURULU başlar, hareket tek yavaş sıkma ve gevşeme; el-nesne kaynaşırsa (d1) sıkmayı kaldır, yalnız çene ve omuz gevşemesi kalsın.
> Plan "tether anchor attached to his harness": `1.LEON` sayfasında tether kemerde (`FILM.md` §3) → "belt", kare sol yanında (pilot kumandalarının yanı = "controls-side"); eldiven sağ el (kare solu). Kolu ve gövdesi kadrajda (tutanı kadrajda).
> Cross-grup: G02 C14 (Leon tether bağlantısı) aynı tarafı tarif etmeli (kemerin kare sol yanı / Leon'un sağ kalçası); devamlilik bakar.

### Görsel
```text
Reference 1 (man): take his face, his ivory pressure suit with the navy shoulders, orange upper-arm bands and blue-gold hawk badge, and the white gloves from it, using the front full-body panel. Reference 4 (cockpit): take the navy pilot seat, the short twin pilot controls and the ivory overhead shell from it, using the pilot side panel. Reference 15 (accessories): take the coiled navy safety tether with its rigid silver magnetic anchor block from it, using the tether panel. Medium close-up on a 50 mm lens at eye level with the camera facing a seated man: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits at frame-left in the navy pilot seat, framed from the top of his helmet to his waist, his head tilted slightly down, his brown eyes lowered toward his belt and his mouth closed. He wears white gloves. At the frame-left side of his waist the rigid silver magnetic anchor block of his coiled navy safety tether is clipped to his belt, and his right glove rests on it, the forearm angled down from his elbow beside the short twin pilot controls at the edge of the frame; his other glove lies on his thigh. Behind him the ivory overhead shell falls softly out of focus. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow, small camera drift toward frame-right begins while his glove rests on the silver anchor block and his eyes stay lowered. 2-7 s: The drift carries on and his jaw tightens, his mouth staying closed, while a clear, quick adult woman's voice from out of frame, precise and controlled and softened by a light suit-radio filter, says: At Dione, you cut the tether with me on the other end. 7-10 s: His glove closes once around the anchor block in a slow squeeze, then loosens and settles back on it, his shoulders lowering with one slow breath as the drift eases. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C43 — "Güven kaybolmuş" — iki kişi, iki replik

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C43.png (referans eklenmez)
```

> Not: İki replik, ikisi ağız kadrajda: R45 Leon 1.0-3.0 s (vuruş 0-3 s'in son cümlesi) → R46 Rhea 3.5-5.5 s (vuruş 3-7 s'in son cümlesi); konuşmayan kişinin ağzı kapalı. 10.CEKIRDEK ÇIKARILDI (askı+çekirdek
> `harness with core panel`ında). Plan "without dramatic grabbing or movement" olumsuzu pozitife çevrildi: yalnız küçük, yavaş kask dönüşü; eldivenler uyluklarda kalır. Kare hareketin başı: Leon henüz dönmedi, ikisi öne bakar.

### Görsel
```text
Reference 1 (man): take his face, his ivory pressure suit with the navy shoulders and orange upper-arm bands, the blue-gold hawk badge and the white gloves from it, using the front full-body panel. Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and navy waist, and the graphite core-carry harness with the locked core from it, using the harness with core panel. Reference 4 (cockpit): take the 2 seats, the ivory overhead shell, the low graphite console and its soft cyan lights from it, using the wide interior panel. Medium two-shot on a 35 mm lens at eye level with the camera facing the seats; the two of them are the only people in the cockpit. At frame-left in the navy pilot seat sits an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, and at frame-right in the engineer seat sits an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Both are framed from the top of their helmets to their waists with a forearm's width of space between the seats. Both helmets face the camera, the man's brown eyes lowered a little toward the low console in front of him and the woman's green eyes looking straight ahead, both mouths closed. Both wear white gloves resting on their thighs. The locked graphite core with its amber glass center rides in the harness over her chest. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow, small push-in begins as the man's helmet turns slowly toward the woman, his gloves staying on his thighs and her mouth closed; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: The ship was breaking apart. 3-7 s: The push carries on while his eyes stay on her and his mouth stays closed; the woman keeps her eyes ahead and her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: I survived. The trust didn't. 7-10 s: Her eyes come around slowly to meet his as the push eases closer between them, both mouths closed and both gloves resting on their thighs. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C44 — Fırın çukuru parlar, gövde bütün kalır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C44.png (referans eklenmez)
```

> Not: Replik R47, Leon, VOICE-OVER (kadrajda kimse yok), 1.5-4.0 s → vuruş 0-4 s'in son cümlesi; sesin sahibi tarif edilir (`as a calm voice-over`), kadrajda insan ve zamir yok (A08).
> EKLENDİ: 3.KESTREL (`bow collar locked panel`). Tug ark'ın kıç SANCAK portuna C06'da yanaştı, C80'e kadar orada (`FILM.md` §3 Sabit tasarım); burun sağda/kıç solda dış görünüş ark'ın sancak yanını gösterir
> → tug karede olmalı; plan listesinde yok, devamlılık için eklendi (küçük, kıç ucunda, rijit). Dış çekim: gök/ışık cümlesi DIŞ birebir (T18). Plan "exhaust pulse" vakumda gaz yerine ışık atımı olarak yazıldı
> (BILINEN §B sıra 4: duman/buhar yazılmaz); atım kaburgaların arkasında kalır, gövdenin altını aydınlatır. "Brighter" göreli sözcük karede "bright orange"; parlama videoda yükselir. Üç kepenk kısmen kapalı (kapı C62'de açılır).
> Motorlar karanlık (ark C89'dan önce çıkış yakması yapmaz).

### Görsel
```text
Reference 3 (tug): take the wedge-shaped ivory salvage hull with its single narrow orange bow band and the locked bow collar from it, using the bow collar locked panel. Reference 5 (foundry): take the black C-shaped cradle, its 2 rigid gantry clamp arms, the heavy blast ribs, the orange furnace trench and the huge curved blue gas giant from it, using the wide exterior panel. Reference 6 (colony ark): take the long ivory segmented hull with its 6 low cryo-habitat blocks and its 2 big blue rear engines from it, using the side view panel. Wide rear three-quarter view on a 24 mm lens, the camera level with the ark's hull axis, slightly behind and beside its stern: the long ivory colony ark lies in the black C-shaped foundry cradle, held by 2 rigid gantry clamp arms on opposite flanges, its stern with the 2 dark rear engines at frame-left and its bow at frame-right toward the exit iris, whose 3 rigid radial shutters stand partly closed. 1 small salvage tug is docked at the ark's starboard stern port, small against the hull. Behind the stern at frame-left, heavy blast ribs rise like a wall between the ark and the orange furnace trench, which glows bright orange; the ark's hull is intact, its underside catching only a faint orange edge-light. A huge curved blue gas giant fills the far background. The frame holds only the structures and the two ships. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow lateral drift toward frame-right along the ark's length, the ark, the tug, the 2 clamp arms, the blast ribs and the shutters all staying rigid, while the orange furnace glow behind the ribs at frame-left begins to climb and a low, dry adult man's voice, calm and guarded, as a calm voice-over, says: I'm not making that choice again. 4-7 s: A low pulse of orange furnace light rises behind the blast ribs and washes across the underside of the ark's intact hull, brightening its ivory segments for a moment while the drift carries on. 7-10 s: The pulse fades back to a steady glow behind the ribs, the hull's underside dimming again as the drift continues along the ark. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C45 — Rhea çekirdeğin amber merkezine dokunur

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/10.CEKIRDEK_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C45.png (referans eklenmez)
```

> Not: Replik R48, Rhea, ağız kadrajda, 1.5-6.0 s (4.5 s, tavan 5 s içinde); vuruş 2-7 s'in son cümlesi, dokunuş repliğin başında (2. vuruş başı), geri çekilme 3. vuruşta. Bu çekimde çekirdek
> kahraman olduğu için 10.CEKIRDEK KALIR (`core object panel`: kasa, fildişi köşe korumaları, tek üst kulp, amber cam merkez); askı ve kimlik 2.RHEA `harness with core panel`ından.
> T01 temas: eldiven kasanın üstünde KURULU başlar, tek kısa kayma ve tek dokunuş, söküm yok (kasa kapalı kalır). Eldiven sol el (kare sağı); kolu ve gövdesi kadrajda. Plan "amber center guard" = amber cam merkez kapağı.
> Risk: parmak amber cama kaynaşırsa (d1) dokunuşu eldivenin kasa kenarına bıraktığı kareye indir.

### Görsel
```text
Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and navy waist, and the graphite core-carry harness from it, using the harness with core panel. Reference 4 (cockpit): take the engineer seat, the ivory overhead shell and the low graphite console from it, using the engineer side panel. Reference 10 (power core): take the compact rectangular graphite casing with its ivory corner guards, the single rigid top carry handle and the amber glass center from it, using the core object panel. Medium shot on a 50 mm lens at eye level with the camera facing a seated woman: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She sits in the engineer seat, framed from the top of her helmet to her waist, her head tilted slightly down and her green eyes on the core, her mouth closed. She wears white gloves. The locked graphite core rides in the harness over her chest, and her left glove rests flat on the frame-right edge of its casing just beside the amber glass center, the forearm angled up from her elbow beside the harness; her other glove lies on her thigh. Behind her the ivory overhead shell falls softly out of focus. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow push-in begins as her glove glides a short way across the graphite casing toward the amber glass center. 2-7 s: Her fingertip touches the glass cover of the amber center once, and her eyes lift from the core toward the front as the push carries on; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: This core can force the gate open. The overload will consume it. 7-10 s: Her glove draws back to rest on the casing's edge, her eyes ahead and her mouth closed, the push easing closer while the casing, the corner guards and the carry handle stay exactly as they are. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C46 — Ark'ın pruvası, foundry tarafı: iki ayrı işaret

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C46.png (referans eklenmez)
```

> Not: Replik R49, Rhea, ağız kadrajda, 1.5-6.5 s (5.0 s, tavan 5 s; sınırda): vuruş 2-7 s'in son cümlesi; Leon'un ağzı kapalı. İki işaret zamanda ayrık (plan): Rhea cümlesinin sonunda ark pruvasına (kare sağı),
> Leon son vuruşta foundry tarafına (kare solu); dış kollar. 10.CEKIRDEK ÇIKARILDI (`harness with core panel`ında). Kare hareketin başı: eller uylukta, işaret yok. Plan "through canopy": kanopi iki koltuğun arkasında,
> sağda ark gövdesi (pruva sağ kenara), solda siyah kradle (foundry tarafı, plan ark burnu SAĞDA / fırın SOLDA ile aynı yön). Kanopinin ötesi dış çekim: kokpit ve DIŞ cümleleri birebir (T18).
> Ağız okunurluğu: Rhea'nın başı hafifçe Leon'a dönük. Risk: 5.0 s repliğin ağız senkronu tavanda; tutmazsa metin kurguda eklenir (kayıt yedek).

### Görsel
```text
Reference 1 (man): take his face, his ivory pressure suit with the navy shoulders and orange upper-arm bands, the blue-gold hawk badge and the white gloves from it, using the front full-body panel. Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and navy waist, and the graphite core-carry harness with the locked core from it, using the harness with core panel. Reference 4 (cockpit): take the 2 seats, the ivory overhead shell, the broad canopy with its 2 fixed graphite mullions and the low graphite console from it, using the wide interior panel. Reference 5 (foundry): take the black C-shaped cradle with its heavy blast ribs from it, using the wide exterior panel. Reference 6 (colony ark): take the long ivory segmented hull with its 6 low cryo-habitat blocks from it, using the side view panel. Medium two-shot on a 35 mm lens at eye level with the camera facing the seats; the two of them are the only people in the cockpit. At frame-left in the navy pilot seat sits an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, and at frame-right in the engineer seat sits an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Both are framed from the top of their helmets to their waists. Both sit upright with white gloves resting on their thighs, their helmets angled slightly toward each other, their mouths closed. The locked graphite core with its amber glass center rides in the harness over her chest. Behind them the broad canopy, crossed by 2 fixed graphite mullions, shows the long ivory hull of the colony ark running to the right edge of the frame and, at the left edge, the black C-shaped foundry cradle curving away. The light inside is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy; the light outside is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow push-in between the two seats begins as the woman's helmet turns a little toward the man, her gloves resting on her thighs. 2-7 s: The push carries on while the man's mouth stays closed; as her sentence nears its end, the woman's outer glove lifts and points once along the canopy toward the ark's bow at frame-right, then lowers; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: I feed the gate and release port. You take starboard from the ark. 7-10 s: The man's helmet turns toward the canopy and his outer glove lifts and points once toward the foundry cradle at frame-left while the push eases closer, the woman's glove back on her thigh and her mouth closed. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C47 — Leon kararını verir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/4.KOKPIT_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C47.png (referans eklenmez)
```

> Not: Replik R50, Leon, ağız kadrajda, 1.5-4.0 s → vuruş 2-6 s'in son cümlesi; baş sallama replikten sonra, son vuruşta (karar cümlenin ardından onaylanır), tek ve ölçülü. Plan "hands resting on controls":
> iki eldiven kare alt kenarında kısa çift kumandada KURULU başlar, kolları kadrajda; hareket yalnız baş sallama ve kamera itişi. Plan "controlled determined face" fiziksel tarife çevrildi (çene sıkı, bakış sabit).
> Yara sol şakakta: baş hafif sağa dönük, yara yüzün sağ kenarında.

### Görsel
```text
Reference 1 (man): take his face with the short dark brown hair, neat beard and pale left-temple scar, and his ivory pressure suit with the navy shoulders and the clear ivory helmet from it, using the face close-up panel. Reference 4 (cockpit): take the navy pilot seat, the short twin pilot controls and the ivory overhead shell from it, using the pilot side panel. Medium close-up on an 85 mm lens at eye level with the camera facing a seated man: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits in the navy pilot seat, framed from the top of his helmet down to his hands, his head level with a slight turn toward frame-right, his brown eyes steady, his jaw set and his mouth closed; his pale left-temple scar shows at the frame-right edge of his face behind the clear visor. He wears white gloves, and both gloves rest on the short twin pilot controls at the lower edge of the frame, his forearms rising from them to his elbows. Behind him the ivory overhead shell falls softly out of focus. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow push-in toward his face begins while his gloves rest on the short twin controls and his steady eyes stay on the engineer seat out of frame at frame-right. 2-6 s: The push carries on and his lips move only for his own line; he says in a low, dry adult man's voice, calm and guarded: We lose the core. We take everyone. 6-10 s: His mouth closes and his chin dips once in a restrained nod and rises again, his jaw set and his gloves steady on the controls, the push easing closer to the end. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C48 — Kavşakta iki rota

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png · VİDEO (Frames to Video): başlangıç karesi: kare/C48.png (referans eklenmez)
```

> Not: Replik R51, Rhea, ağız kadrajda, 1.5-3.5 s → vuruş 0-4 s'in son cümlesi; Leon'un ağzı kapalı. T11 TERS TARAF (plan kapı coğrafyası, `FILM.md` §3): Rhea köprü kapısında KARE SOLU (yakın plan önünde),
> Leon komuta kapısında KARE SAĞI (uzakta, küçük); `7.KORIDOR` `junction panel`ı bu düzeni verir (yükleme köprüsü kapısı solda, komuta kapısı uzak sağda). 10.CEKIRDEK ÇIKARILDI (geniş planda çekirdek küçük, `harness with core panel`ında).
> Rhea ağız kadrajda ama plan geniş: ağzın okunması için Rhea ön plana alındı (kare yüksekliğinin yaklaşık yarısı); ağız senkronu zayıf çıkarsa çekim orta-geniş yapılır. İki rota da açık (plan "already-open route").
> Kriyo penceresi ışık cümlesi için kadrajda duvarda yazılı (yolcu yüzü yok, pencere yalnız yumuşak yeşil). İki kısa adım zemine basar; ayak-zemin geniş temas değil (T10).

### Görsel
```text
Reference 1 (man): take his face, his ivory pressure suit with the navy shoulders and orange upper-arm bands, the blue-gold hawk badge and the white gloves from it, using the front full-body panel. Reference 2 (woman): take her face, her pearl pressure suit with the teal upper-arm bands and navy waist, and the graphite core-carry harness with the locked core from it, using the harness with core panel. Reference 7 (corridor): take the ivory walls, the graphite grating, the fixed navy handrails, the amber emergency lamps, the cryo observation window and the 2 rectangular doorways from it, using the junction panel. Wide shot on a 28 mm lens at eye level, the camera standing in the pressurized ark corridor with the junction ahead: ivory walls, graphite grating floor, fixed navy handrails and amber emergency lamps along the ceiling. At frame-left a rectangular doorway stands open onto the loading-bridge route, and far at frame-right a rectangular doorway stands open onto the ark command route; in the wall between them a cryo observation window glows faintly green. In the foreground at frame-left, beside the loading-bridge doorway, stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, about half the frame's height, seen in three-quarter view with her helmet turned toward the far doorway; the locked graphite core with its amber glass center rides in her harness. Far down the corridor at frame-right, beside the command doorway, stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, small in the frame, his helmet turned toward her. Both wear white gloves, their arms at their sides, and both mouths are closed. The two of them are the only people in the corridor. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow push-in along the corridor begins as the woman's helmet turns from the far doorway toward the man and his helmet turns toward her across the junction, their eyes meeting; his mouth stays closed while her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: No one gets cut loose. 4-7 s: The push carries on as each takes one short step toward their own open doorway, the woman toward the loading-bridge doorway at frame-left and the man toward the command doorway at frame-right, each boot landing flat on the graphite grating. 7-10 s: Each helmet turns toward the open doorway ahead as the stepping boot settles, the push easing closer along the corridor, both mouths closed. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini görselden video 10 s ile hedefler (`THE_FURNACE_GATE_16MIN_96_CLIPS.md` §7). Başlangıç karesi yalnız Flow web'de; Omni/Gemini süresi ve ses davranışı
> SMOKE P11 · P14 · P18'de ölçülür (`uretim_hatti/FLOW_GERCEKLERI.md` §1 · §9); ölçüm gelmeden videolar koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9. Veo 3.1'de klip 4/6/8 s'dir.
> **Bu grupta on iki çekimin hepsi replikli** (C37-C48): replik klipte yanlış ya da bozuk duyulursa o klibin sesi kurguda eklenir (timeline `ses` parçası; `FILM.md` §5 kaydı yedek). C42 ve C44'ün sesi telsiz/voice-over, kalanı ağız kadrajda.
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kare üretimi için panel adı parantezde. Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C37 kare | `kare/C37.png` | Görsel | ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/4.KOKPIT_v1.png (mühendis yan paneli) · ref/15.ARACLAR_v1.png (bilek bağlantısı paneli; bu sırayla) | 2 | |
| 2 | C38 kare | `kare/C38.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/4.KOKPIT_v1.png (pilot yan paneli; bu sırayla) | 2 | |
| 3 | C39 kare | `kare/C39.png` | Görsel | ref/2.RHEA_v1.png (yüz yakın paneli) · ref/4.KOKPIT_v1.png (mühendis yan paneli; bu sırayla) | 2 | |
| 4 | C40 kare | `kare/C40.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/4.KOKPIT_v1.png (geniş iç panel; bu sırayla) | 2 | |
| 5 | C41 kare | `kare/C41.png` | Görsel | ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/4.KOKPIT_v1.png (geniş iç panel) · ref/5.FOUNDRY_v1.png (geniş dış panel) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 6 | C42 kare | `kare/C42.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/4.KOKPIT_v1.png (pilot yan paneli) · ref/15.ARACLAR_v1.png (tether paneli; bu sırayla) | 2 | |
| 7 | C43 kare | `kare/C43.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/4.KOKPIT_v1.png (geniş iç panel; bu sırayla) | 2 | |
| 8 | C44 kare | `kare/C44.png` | Görsel | ref/3.KESTREL_v1.png (burun yakası kilitli paneli) · ref/5.FOUNDRY_v1.png (geniş dış panel) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 9 | C45 kare | `kare/C45.png` | Görsel | ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/4.KOKPIT_v1.png (mühendis yan paneli) · ref/10.CEKIRDEK_v1.png (çekirdek nesne paneli; bu sırayla) | 2 | |
| 10 | C46 kare | `kare/C46.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/4.KOKPIT_v1.png (geniş iç panel) · ref/5.FOUNDRY_v1.png (geniş dış panel) · ref/6.ARK_v1.png (yan görünüş paneli; bu sırayla) | 2 | |
| 11 | C47 kare | `kare/C47.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/4.KOKPIT_v1.png (pilot yan paneli; bu sırayla) | 2 | |
| 12 | C48 kare | `kare/C48.png` | Görsel | ref/1.LEON_v1.png (önden tam boy paneli) · ref/2.RHEA_v1.png (askı + çekirdek paneli) · ref/7.KORIDOR_v1.png (kavşak paneli; bu sırayla) | 2 | |
| 13 | C37 | `ham/C37_d1.mp4` | Frames to Video | kare/C37.png | 2 | |
| 14 | C38 | `ham/C38_d1.mp4` | Frames to Video | kare/C38.png | 2 | |
| 15 | C39 | `ham/C39_d1.mp4` | Frames to Video | kare/C39.png | 2 | |
| 16 | C40 | `ham/C40_d1.mp4` | Frames to Video | kare/C40.png | 2 | |
| 17 | C41 | `ham/C41_d1.mp4` | Frames to Video | kare/C41.png | 2 | |
| 18 | C42 | `ham/C42_d1.mp4` | Frames to Video | kare/C42.png | 2 | |
| 19 | C43 | `ham/C43_d1.mp4` | Frames to Video | kare/C43.png | 2 | |
| 20 | C44 | `ham/C44_d1.mp4` | Frames to Video | kare/C44.png | 2 | |
| 21 | C45 | `ham/C45_d1.mp4` | Frames to Video | kare/C45.png | 2 | |
| 22 | C46 | `ham/C46_d1.mp4` | Frames to Video | kare/C46.png | 2 | |
| 23 | C47 | `ham/C47_d1.mp4` | Frames to Video | kare/C47.png | 2 | |
| 24 | C48 | `ham/C48_d1.mp4` | Frames to Video | kare/C48.png | 2 | |

> Öncelik: temas taşıyan iki çekim (C42 tether sıkma · C45 çekirdek dokunuşu) ve iki kişilik ağız senkronu çekimleri (C40 · C43 · C46) önce denenir; C46 (5.0 s replik) ve C48 (geniş planda ağız) ağız okunurluğunun sınır vakalarıdır.
> Komşu grup denetimi: C36 (G03) → C37 ve C48 → C49 (G05) kesmeleri `FILM.md` §6 GEÇİŞ'te Y2 sürer / Y3→Y8 çaprazlar; C36'nın kokpit kamerası (Leon solda, Rhea sağda, yüzler okunur) bu grupla aynı ekran düzeninde olmalı.
