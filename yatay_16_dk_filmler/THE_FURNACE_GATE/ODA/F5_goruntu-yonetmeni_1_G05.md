# 🖼️ THE_FURNACE_GATE — Prompt grubu G05 (çekimler C49–C60)

> Yazan: goruntu-yonetmeni (tur 1). Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K49–K60 + `FILM.md` §3 / §4 / §5.
> Bu dosya yeniden tasarım değil, biçim çevirisidir: kompozisyon, olay, replik ve hareket yönü planın kendisi; cümleler olabildiğince planın İngilizcesi.
> Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Zincir yok (plan zincir kurmaz); her çekim kendi başlangıç karesiyle Frames to Video. `EKLE` satırı iki parçalıdır: KARE (görsel üretimi için referanslar) ·
> VİDEO (yalnız kare; Frames to Video'ya referans eklenmez, yoksa mod Ingredients'e kayar).
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında `Reference <No> (<rol>): …` diye adlandırılır;
> her referanstan çekim başına yalnız TEK panel. Her video promptu 10 s'yi 2-3 vuruşa böler (0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s, son vuruş donmaz; ilk vuruş hareketle başlar).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** FILM.md §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir; MEKÂN IŞIĞI cümlesi her görsel promptta
> `The light is …` sarmalayıcısıyla (kelimeler FILM.md §3'teki gibi); ORTAM SESİ cümlesi o mekânın her video promptunda birebir (ortak görünümden hemen önce). Bu filmde bütün replikler model sesi:
> replik video promptuna birebir `says …: <line>` biçiminde yazılır, konuşanın sesi SES KİMLİĞİ kelimeleriyle tarif edilir (telsizde `, softened by a light suit-radio filter`),
> replik vuruşun SON cümlesidir. Ağız kadrajda olan repliklerde (C50 · C53 · C54 · C55 · C58) dudak yalnız kendi cümlesinde oynar; telsiz repliklerinde (C49 · C51 · C52 · C56 · C57 · C60)
> konuşanın yüzü kadrajda değildir (C49 Leon arkadan; C51 · C56 · C60 yalnız eldiven ve kol; C52 · C57 kimse yok). C59 replik taşımaz.
> **Ortak cümleler (FILM.md §3, birebir):** Leon kimlik tabanı `an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet` ·
> Rhea kimlik tabanı `an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet` ·
> ses Leon `a low, dry adult man's voice, calm and guarded` · ses Rhea `a clear, quick adult woman's voice, precise and controlled` ·
> dış gök cümlesi (C52 · C57; G06 C62 · C68 · C72 ile aynı) `Deep black space with sparse stars surrounds the foundry.`
> **Kimlik tabanı modüler kullanılır:** kadrajda olmayan parça yazılmaz (kural: "kadrajda olmayan tarif edilmez"). C49 Leon arkadan: yüz, sakal, yara, rozet çıkarıldı (kalan sözcükler tabanla birebir); C55 Leon sağ ¾ ön: sol şakak yarası kameradan uzak yanda, çıkarıldı;
> C56 · C60 yalnız kol ve eldiven: taban yerine "pearl sleeve · white glove".
> **Panel adları (FILM.md §3'ten; çekim başına her referanstan yalnız TEK panel):** 1.LEON `back full-body panel` · `face close-up panel` · `glove panel` · 2.RHEA `front full-body panel` · `harness with core panel` ·
> 3.KESTREL `bow collar locked panel` · 5.FOUNDRY `wide exterior panel` · 6.ARK `stern panel` · 9.KOPRU `exterior intact panel` · 10.CEKIRDEK `core object panel` · `cradle close panel` · 11.DRONE `drone front panel` ·
> 12.KONTROL_ODASI `wide room panel` · `console close panel` · 13.KOMUTA `wide bridge panel` · `pilot console panel` · 15.ARACLAR `wrist-link panel`.
> **Kelime güvenliği (BILINEN_TUZAKLAR §A · §C):** `body` · `blood` · `wound` · `corpse` hiçbir promptta geçmez (`hull` · `casing` · `chassis` yazıldı); `dead` yalnız C49 repliğinin kendisinde geçer (aşağıda risk). Kollar harf/ad etiketiyle anılmaz
> (plandaki "release-B" · "clamp-A" kök sözcükleri kadraja yazı olarak basılabilir): kol rengiyle anılır (`the broad blue gate-power lever` · `the broad teal port-clamp release lever` · `the orange mechanical gate-catch lever` · `the broad silver clamp-release lever`).
> Plan olumsuzları ("No readable text…" kuyruğu · "Do not add an offscreen object…") pozitife çevrildi ya da çıkarıldı; "Use the attached reference images only…" yerine `Reference <No> (<rol>)` anahtarı; "Animate the uploaded scene still as the first frame" ve ses/olumsuz kuyruğu çıkarıldı.
> **Sabit düzen (G05 içinde ve G07 C78 ile uyumlu):** ark acil komutada pilot koltuğu SOLDA, gümüş sancak-kelepçe kolu pilotun sol (dış) yanında, bilek bağlantısı yuvası sağda (navigasyon yanı) · kontrol odasında kamera sağ (soket hava kilidi) duvardan odaya bakar: Rhea karenin SAĞINA, konsola doğru döner (sağ çene yarası kameraya),
> pencere sağda, yükleme köprüsü kapısı arkada/solda · Rhea'nın bilek bağlantısı SOL ön kolunda (FILM.md §3 yan yazmıyor; benim seçimim, birleştirmede C04 · C10 · C37 · C93 ile hizalanır) · eldiven işleri sağ elle.

---

## C49 — Leon acil komuta köprüsünde

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C49.png
```

> Not: Replik R52 (Leon, telsiz, 1,5–5,0 s → ilk vuruş 0-5 s; yüzü arkadan, ağzı görünmez). Geniş plan, kamera koltuğun arkasında, kısa dolly ileri (plan). Gümüş kol karede dik (T09), pilotun sol/dış yanında = karenin solu.
> Eller kare başında kucakta (kamera arkada, kucak görünmez); eldivenlerin kumandaya konması videoda, gövde ve koltuk sırtı yarı örter. Risk: temas kaynaşırsa tek eldiven kumandada başlayacak şekilde kare yeniden üretilir (video yalnız ikinci eldiveni koyar).
> Kapı kanopide, planın "kepenkler kısmen kapalı" durumu; kapı dışında ark/ışık sabitleri yok (iç mekân).

### Görsel
```text
Reference 1 (man): take his ivory pressure suit, navy shoulders, orange upper-arm bands, compact ivory life-support pack and round ivory helmet from it, using the back full-body panel. Reference 13 (command bridge): take the two-seat emergency command bridge with its navy seats, ivory shell, broad forward canopy, cyan interface lights and the single broad silver clamp-release lever from it, using the wide bridge panel. Wide view on a 24 mm lens, the camera 1.5 m behind the pilot chair at the height of its headrest, looking straight forward through the canopy. At the left of the frame an adult 38-year-old olive-skinned man sits in the navy pilot chair, seen from behind, in an ivory pressure suit with navy shoulders and orange upper-arm bands, and a round ivory helmet; his white gloves rest low in his lap and his boots rest side by side on the deck below the chair. At the right of the frame the navigation seat and its console stand empty. The single broad silver clamp-release lever stands upright at the left side of the pilot console, beside his chair. Through the broad canopy ahead hangs the huge circular exit gate, its three rigid radial shutters partly closed against the starfield. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: A slow, short dolly begins forward behind the pilot chair while the man settles into the seat and plants his boots on the deck, his shoulders squaring toward the console; his face stays turned away from the camera, and a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from inside his helmet: I'm on the ark. Starboard release is still dead. 5-8 s: The dolly keeps closing as both white gloves come up out of his lap and settle on the pilot console's paired controls, the broad silver clamp-release lever beside his chair staying upright. 8-10 s: The dolly slows a little closer behind the chair, his gloves resting on the controls and the three exit-gate shutters staying partly closed in the canopy ahead. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C50 — Rhea yeniden güç odasında

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C50.png
```

> Not: Replik R53 (Rhea, ağız kadrajda, 1,5–5,0 s → ilk vuruş 0-5 s; yüz ve ağız net, vizör şeffaf). FILM.md §4 referansından 15.ARACLAR çıkarıldı: orta plan bel üstü, kemer araçları kadrajda değil (araç tasarımı 2.RHEA sayfasında).
> T09: çekirdek göğüs askısında, giriş yuvası boş, üç kol dik. Bakış çekirdekten mavi kola: kare başında gözler çekirdeğe inik. Hareket yalnız bakış ve çok küçük itiş.

### Görsel
```text
Reference 2 (woman): take her face, pearl pressure suit, navy waist, teal upper-arm bands, badge and the graphite harness with the core locked in it from it, using the harness with core panel. Reference 10 (core): take the compact rectangular graphite casing with ivory corner guards, the single rigid top carry handle and the amber glass center from it, using the core object panel. Reference 12 (control room): take the low console, the empty rectangular core input cradle, the broad blue gate-power lever, the broad teal port-clamp release lever and the orange mechanical gate-catch lever from it, using the wide room panel. Medium shot on a 50 mm lens at chest height, the camera 2 m from her, framed from her waist to the top of her helmet. An adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, stands inside the foundry gate-control room in three-quarter view turned toward frame-right, her right cheek and chin toward the camera, her face and mouth plainly readable behind the clear visor. The core sits locked in the harness on her chest with its amber glass center facing out, and her eyes are lowered to it. At frame-right in front of her the low console holds the empty rectangular core input cradle; the broad blue gate-power lever, the broad teal port-clamp release lever and the orange mechanical gate-catch lever all stand upright. Behind the console the rear window gives cool blue gate light. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: A slow, small push-in begins toward her as her lowered eyes lift from the core on her chest and her helmet turns a few degrees toward the broad blue gate-power lever on the console; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: I'll feed the captured bus. Keep main thrust off. 5-10 s: The push-in closes slowly as her gaze settles on the broad blue lever and she draws one steady breath, the core on her chest rising slightly with it, the empty cradle and the three levers staying where they are. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C51 — Yardımcı yönetim devreye alınır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C51.png
```

> Not: Replik R54 (Leon, telsiz, 1,5–3,0 s → ilk vuruş 0-4 s; yüz kadraj dışı). T01: sağ eldiven kare başında anahtarın üstünde (temas kurulu); video anahtarı yukarı çevirir, eldiven yeni konumda anahtarın üstünde kalır (temas bitmez).
> Kamera pilotun sağ omzunun arkasında ve üstünde: sağ ön kol karenin sağından girer (kolun girdiği kenar yazılı). Gümüş kol bu kadrajda görünmez (yan yazılmadı; "yalnız kadrajdaki nesne"). Kontrol yazısız: anahtar ve camgöbeği ışık soyut.

### Görsel
```text
Reference 1 (man): take his white glove and ivory suit sleeve from it, using the glove panel. Reference 13 (command bridge): take the pilot console with its one broad backup-power toggle and the cyan interface lights from it, using the pilot console panel. Close view on an 85 mm lens, the camera 50 cm above and behind the pilot's right shoulder, looking forward at the console. His right white glove and ivory sleeve enter from the right edge of the frame and already rest on one broad backup-power toggle at the console's edge, the toggle in its down position. The abstract cyan interface lights of the console glow at a low level around it, and the console's surface is plain and unmarked. Only his glove and sleeve are in the frame. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow push toward the console while the white glove flips the broad backup-power toggle up in one smooth motion and the abstract cyan console lights around it start to strengthen; a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from out of frame: Backup control is live. 4-7 s: The push continues as the cyan lights brighten to a steady, stronger glow, the glove staying on the toggle in its new position. 7-10 s: The push eases closer to the toggle, the stronger cyan glow steady across the console's edge. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C52 — Güvenlik yükleme hattını kesmeye başlar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/9.KOPRU_v1.png · ref/11.DRONE_v1.png · VİDEO (Frames to Video): yalnız kare/C52.png
```

> Not: Replik R55 (Rhea, telsiz, 1,5–3,5 s → ilk vuruş 0-4 s; kadrajda kimse yok). Dış (vakum, T13): F8'de klip sesi yalnız replik penceresinde (1,5–3,5 s ±0,5) açık tutulur, kalan süre Y1 yatağı.
> Plan: tek kısa atım dış cam desteğine, köprü kırılmaz. Vakumda kıvılcım riski (GOSTERIM_COZUMLERI): kıvılcım düz çizgide uçup kısa mesafede sönen küçük akkor noktalar olarak yazıldı; pus, duman, toz yazılmadı.
> d1'de hacimsel pus çıkarsa yedek: atım kadraj dışında, yalnız desteğin üstünde tek parlak ışık sıçraması. Köprü kare başında sağlam; drone foundry (sağ) ucunda, kırmızı şerit cam desteğe dönük. 11.DRONE `drone front panel` kırmızı şeridi taşır; drone ¾ yazıldı.

### Görsel
```text
Reference 9 (loading bridge): take the rigid telescoping square graphite pressure tunnel, its fixed glass sides, the waist-high rails and the fixed outer glass supports from it, using the exterior intact panel. Reference 11 (drone): take the compact rigid graphite rectangular casing, the single narrow horizontal red sensor strip, the two recessed maneuvering jets and the short forward emitter from it, using the drone front panel. Wide side view on a 35 mm lens, the camera 50 m from the bridge and level with it, looking across the intact loading bridge. The ivory flank of the colony ark with the bridge's ark hatch is at the left edge of the frame, the rigid bridge spans the middle of the frame, and the graphite foundry control spine with the bridge's foundry hatch is at the right edge. Heavy blast ribs stand at the far left. One security drone, seen in three-quarter view, holds position 8 m off the bridge near its foundry end, its single red sensor strip aimed at a fixed outer glass support of the tunnel. A huge curved blue gas giant fills the far background. Deep black space with sparse stars surrounds the foundry. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow lateral drift to the right along the intact bridge while the drone holds its position near the foundry end, its single red sensor strip steady on the fixed outer glass support; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: They're sealing the loading route. 4-7 s: The drift continues as the drone's short forward emitter releases one brief blue-white pulse that strikes the glass support, and a few tiny incandescent sparks fly off in straight lines and fade within a short distance. 7-10 s: The sparks die out and the drone keeps its red strip aimed at the support, while the support, the glass sides and the whole bridge keep their rigid shape as the drift slows. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C53 — Rhea siper alır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C53.png
```

> Not: Replik R56 (Rhea, ağız kadrajda, 1,5–4,0 s → ilk vuruş 0-4 s). FILM.md §4 referansından 10.CEKIRDEK çıkarıldı: çekirdek kadrajda küçük ve kenarda, tasarımı 2.RHEA `harness with core panel`inde. Plan "doorway pressure bulkhead closed behind her" harfi harfine: kamera önde, konsol kameranın önünde alçak,
> Rhea konsolun arkasında çömelmiş (kask, omuz ve göğüsteki çekirdek kenar üstünde), kapalı basınç perdesi arkasında. "Yakın darbe" sözcüğü `near hit` yazıldı (impact/patlama yok): kapı penceresinin ötesinde tek mavi-beyaz ışık çakması. Risk: geniş planda ağız küçük; yüz okunmazsa kamera 2 m'ye yaklaştırılır (orta-geniş).

### Görsel
```text
Reference 2 (woman): take her face, pearl pressure suit, navy waist, teal upper-arm bands and the graphite harness with the core locked in it from it, using the harness with core panel. Reference 12 (control room): take the low fixed console, the sealed loading-bridge doorway with its pressure bulkhead door and the cool blue window light from it, using the wide room panel. Wide view on a 28 mm lens at crouch height, the camera 3 m from her. An adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, crouches in the center of the frame behind the fixed low console that crosses the lower third of the frame, her helmet, shoulders and the core locked in the harness on her chest rising above its edge; her face and mouth are plainly readable behind the clear visor and her gaze is straight ahead. Behind her in the far wall the sealed pressure bulkhead door of the loading-bridge doorway stands closed, a small round window set in it showing the dark tunnel beyond. The rear window at the right edge of the frame gives cool blue gate light. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow, small push-in begins toward her as she crouches steady behind the console, her lips moving only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: I'm inside. Stay on your station. 4-7 s: Beyond the small round window of the sealed door behind her, one bright blue-white flash of a near hit lights the doorway and washes briefly across the walls and the console, and she presses lower behind the console, only the top of her helmet staying above its edge. 7-10 s: The flash fades back to the steady amber light as the push-in slows, the sealed door staying closed and the console standing fixed. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C54 — Pilotun tepki ve güveni

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C54.png
```

> Not: Replik R57 (Leon, ağız kadrajda, 1,5–2,5 s → ilk vuruş 0-3 s; yüz ve ağız net). Plan "fixed rail" için kare başında sağ eldiven konsolun yakın kenarındaki sabit korkuluğun üstünde (temas kurulu): video yalnız kavramanın sıkılaşmasını ve omuz yerleşmesini ister, kumandaya gitmez ("gemiyi hareket ettirmek yerine").
> Korkuluk 13.KOMUTA sayfasında yazılı değil; plan videosu onu istediği için karede yer alır (yeni tasarım öğesi, birleştirmede sayfa notu). Gümüş kol Leon'un sol (dış) yanında = karenin sağ kenarı (G07 C78 ile aynı). Sol şakak yarası kameraya dönük (kafa karenin soluna döner).

### Görsel
```text
Reference 1 (man): take his face, ivory pressure suit with navy shoulders and the fully clear closed ivory helmet from it, using the face close-up panel. Reference 13 (command bridge): take the navy pilot chair, the ivory shell and the single broad silver clamp-release lever from it, using the pilot console panel. Close-up on an 85 mm lens at eye level, the camera 1 m in front of the pilot chair above the console's near edge, looking back at him. An adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, sits upright in the navy pilot chair, framed from the chest up in three-quarter view with his head turned slightly toward frame-left, so that the pale scar on his left temple faces the camera; his face and mouth are plainly readable behind the clear visor and his eyes look past the camera toward frame-left, where the exit gate lies beyond the canopy. His right white glove already rests on a fixed navy grab rail along the console's near edge at the lower left of the frame, its ivory sleeve entering from the left edge. The single broad silver clamp-release lever stands upright beside him at the right edge of the frame. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow, small push-in begins as his head tilts a few degrees toward his suit radio, his lips moving only for his own line, and he says in a low, dry adult man's voice, calm and guarded: I'm here. 3-7 s: The push-in continues while his right glove tightens its grip on the fixed rail and his shoulders settle, his eyes returning to the gate beyond the canopy, the console controls and the broad silver lever beside him staying as they are. 7-10 s: The push-in slows closer as his chest rises on one steady breath, his glove firm on the rail and his eyes fixed on the gate. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C55 — Çıkış rotası önceden hazırlanır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · VİDEO (Frames to Video): yalnız kare/C55.png
```

> Not: Replik R58 (Leon, ağız kadrajda, 1,5–4,0 s → ilk vuruş 0-4 s; yüz ve ağız net). FILM.md §4 referansından 10.CEKIRDEK ve 15.ARACLAR çıkarıldı: çekirdek komutada yok (Rhea'nın askısında), yuva boş ve işaretsiz, bilek bağlantısı tasarımı bu çekimde görünmez (G07 C78 yuvaya bağlantı koyar; burada yuva boş).
> T06: camgöbeği rota şekli soyut (düz çizgi + küçük halka), yazı/rakam yok. Kamera konsolun sağ ucunda, boyunca pilot koltuğuna bakar (G07 C78'in kanopi tarafı kamerasından farklı açı, C54'ten ölçek ve açı farkı). Leon sağ ¾ ön, sağ yanı kameraya: sol şakak yarası kadrajda yok.
> Temas kare başında kurulu (sağ eldiven sağdaki kumandada); video tek kısa girdi ve yerleşme ister. Rota şekli videoda sabit kalır (K88'de yeniden kullanılacak durum sonradan icat edilmez).

### Görsel
```text
Reference 1 (man): take his face, ivory pressure suit, navy shoulders, orange upper-arm bands and the fully clear closed ivory helmet from it, using the face close-up panel. Reference 13 (command bridge): take the pilot console with its paired short controls, the unmarked wrist-link docking cradle and the cyan interface lights from it, using the pilot console panel. Medium shot on a 50 mm lens at eye level, the camera 2 m away at the right-hand end of the pilot console, looking along the console toward the pilot chair, framed from his waist up. An adult 38-year-old olive-skinned man with short dark brown hair, brown eyes and a neat beard, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, sits in the navy pilot chair at the left of the frame, seen in three-quarter view from his right front and facing frame-right toward the console, his face and mouth readable behind the clear visor and his eyes on the console. In the right foreground the unmarked wrist-link docking cradle sits empty on the console beside him, and above it a flat cyan interface surface shows an abstract route shape: one straight glowing line running into a small ring. His right white glove already rests on the right-hand one of the paired short controls, while the other control stands fixed. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow, small push-in begins along the console as his right glove makes one short, smooth input on the control, pressing it forward a few centimeters; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: Straight exit course loaded. Holding until release. 4-7 s: The glove eases the control back to center and settles, the paired control beside it staying fixed and the cyan route shape holding steady. 7-10 s: His helmet turns slightly toward the canopy as the push-in closes a little further, his glove resting on the control. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C56 — Uzaktan ark bağlantısı korunur

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C56.png
```

> Not: Replik R59 (Rhea, telsiz, 1,5–6,5 s → vuruş 2-7 s; yüz kadraj dışı, yalnız ön kol ve eldiven). FILM.md §4 referansından 10.CEKIRDEK çıkarıldı: çekirdek yalnız kadraj kenarında yumuşak, tasarımı 2.RHEA `harness with core panel`inde.
> Bilek bağlantısı SOL ön kolda; geniş anahtarı sağ eldivenin başparmağı çevirir (kare başında başparmak anahtarın üstünde, temas kurulu; sağ eldiven kadraja karenin solundan girer). T06: tek düz camgöbeği lamba, rakam ve yazı yok.
> Çekirdek karenin sağ üst kenarında göğüs askısında, amber cam merkez.

### Görsel
```text
Reference 2 (woman): take her pearl sleeve, white glove and the graphite harness with the core locked in it from it, using the harness with core panel. Reference 12 (control room): take the cyan abstract console lights and the amber lamps of the room from it, using the console close panel. Reference 15 (accessories): take the unmarked ivory wrist-link with its broad physical toggle and single cyan status lamp from it, using the wrist-link panel. Close view on a 100 mm lens with shallow depth of field, the camera 40 cm from her, a little above her left forearm. The unmarked ivory wrist-link sits on the pearl sleeve of her left forearm, which rises across her chest from the lower right of the frame, in the center of the frame, its single cyan lamp lit steadily and its one broad toggle in the off position; her right white glove enters from the left edge of the frame and rests its thumb on the toggle. At the upper right edge of the frame, out of focus, the amber glass center of the core sits locked in the graphite harness on her chest. Behind her the control room blurs into soft amber and cyan lights. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: A slow push begins toward the wrist-link while her right glove's thumb starts to press the broad toggle over. 2-7 s: The thumb flips the toggle to its engaged position, the single cyan lamp holding steady, and a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: I've kept the route link. We can send her through from the tug. 7-10 s: The push settles closer to the wrist-link, the glove resting on the engaged toggle and the core in the harness glowing amber at the edge of the frame. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C57 — Ark'ın motorları hazırdır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png · VİDEO (Frames to Video): yalnız kare/C57.png
```

> Not: Replik R60 (Leon, telsiz, 1,5–3,5 s → ilk vuruş 0-4 s; kadrajda kimse yok). Dış (vakum, T13): F8'de klip sesi yalnız replik penceresinde (1,5–3,5 s ±0,5) açık tutulur, kalan süre Y1 yatağı. Kamera ark'ın sancak-kıç çeyreğinde (tug sancak portunda görünür, kıç solda, gövde sağda kapıya uzanır).
> Motorlar hazır beklemede (mavi, soluk), egzoz/itme yazılmadı: yalnız nozul içi mavi parıltı yumuşar. İki kelepçe kolu kilitli. T18: dış gök ve ışık cümleleri G06 ile birebir.

### Görsel
```text
Reference 3 (tug): take the compact ivory wedge hull, dark graphite underside, narrow orange nose band, smoked-blue canopy and the locked bow collar from it, using the bow collar locked panel. Reference 5 (foundry): take the black C-shaped processing cradle, the two gantry clamp arms, the circular exit gate with its three radial shutters and the blast ribs from it, using the wide exterior panel. Reference 6 (ark): take the long ivory segmented hull, the two large blue rear engines and the small round starboard tug port near the stern from it, using the stern panel. Wide view on a 24 mm lens, the camera 150 m off the ark's starboard stern quarter and level with its hull, looking at the stern of the long colony ark. Its two large rear engines carry a faint blue standby glow, the compact tug sits docked at the small round starboard tug port near the stern, and both enormous rigid gantry clamp arms stay locked on the hull flanges. The long ark recedes toward frame-right to the exit gate, whose three rigid radial shutters stand partly closed. Heavy blast ribs rise at frame-left. A huge curved blue gas giant fills the far background. Deep black space with sparse stars surrounds the foundry. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow lateral drift to the left along the stern while the faint blue standby glow in both rear engines dips slightly and starts to ease; a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, says from out of frame: Station-keep ready. Main burn waiting. 4-7 s: The drift continues as the two glows settle together to a low, steady idle, the ark's hull, the docked tug and both gantry clamp arms staying completely rigid in place. 7-10 s: The drift slows as the two engines glow a low, even blue, the hull staying exactly where it is against the clamps and the tug locked at its port. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C58 — Çekirdek girişe hazırlanır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C58.png
```

> Not: Replik R61 (Rhea, ağız kadrajda; §5 saniyesi 1,5 ama "Core seated." çekirdek oturduktan sonra söylenir → vuruş 4-7 s, çekirdeğin yuvaya oturduğu vuruş; birleştirmede §5 saniyesi ≈5,0'a çekilebilir). T09: askı boş (2.RHEA `front full-body panel`), çekirdek tek rijit üst kulpundan iki eldivenle tutulur
> (plan "rigid handles": tasarımda tek kulp var, iki eldiven yan yana tek kulpta; yeniden kavrama yok). Başlangıçta çekirdek yuvanın bir avuç üstünde hizalı; hareket tek düz iniş. Üç kol dik.

### Görsel
```text
Reference 2 (woman): take her face, pearl pressure suit, navy waist, teal upper-arm bands, white gloves and the empty graphite core-carry harness from it, using the front full-body panel. Reference 10 (core): take the compact rectangular graphite casing with ivory corner guards, the single rigid top carry handle and the amber glass center from it, using the core object panel. Reference 12 (control room): take the low console, the rectangular core input cradle with the small bus connector beside it and the cyan abstract console lights from it, using the console close panel. Medium shot on a 50 mm lens at chest height, the camera 2 m from her, framed from her waist to the top of her helmet. An adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, stands at the console in three-quarter view turned toward frame-right, her right cheek and chin toward the camera, her face and mouth plainly readable behind the clear visor and her eyes lowered to the cradle; the harness on her chest is empty. Both of her white gloves grip the single rigid top carry handle of the core, side by side, holding the core level one hand's width above the open rectangular input cradle in the console at frame-right, its amber glass center facing her. Beside the cradle the broad blue gate-power lever, the broad teal port-clamp release lever and the orange mechanical gate-catch lever stand upright. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow, small push-in begins as she lowers the core straight down toward the open cradle in one steady motion, both gloves staying on the top carry handle without regripping. 4-7 s: The core meets the cradle and sits fully down in it with a soft settle, and her lips move only for her own line; she says in a clear, quick adult woman's voice, precise and controlled: Core seated. 7-10 s: The push-in closes slowly as her gloves stay on the handle and she draws one steady breath, the empty harness on her chest and the three levers beside the cradle staying as they are. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C59 — Çekirdek tutucu kilidi

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C59.png
```

> Not: Replik yok, el yok, kimse kadrajda değil (video promptunda konuşma ya da ses tarifi yazılmaz). Yuvadaki tek hareket menteşeli mandalın kulbun üstüne inip sabit durdurucuda kapanması (plan: "casing stays rigid"). Mandal tasarımı 10.CEKIRDEK `cradle close panel`inde KAPALI görünür; karede mandal AÇIK (kalkık) istenir, prompt bunu açıkça söyler (panel yalnız tasarım için).
> Kamera yuvanın 40° önünde ve üstünde, aşağı bakar; C58 (orta, ön) ve C60 (yandan, kol hizası) ile ölçek ve açı farkı.

### Görsel
```text
Reference 10 (core): take the compact rectangular graphite casing with ivory corner guards, the rigid top carry handle, the amber glass center and the design of the broad hinged retaining latch from it, using the cradle close panel. Reference 12 (control room): take the console, the rectangular core input cradle with the small bus connector beside it and the cyan abstract console lights from it, using the console close panel. Close view on an 85 mm lens, the camera 60 cm above the console and 40 degrees in front of the cradle, looking down at it. The power core sits fully seated in the rectangular input cradle, its amber glass center glowing steadily, and one broad hinged retaining latch stands raised open above the casing, clear of the rigid top carry handle. The small unmarked bus connector sits beside the cradle, and the broad blue, teal and orange levers stand upright at the edge of the frame, softly out of focus. Behind the console the control room blurs into amber and cyan lights. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow, small push-in begins toward the seated core as the broad hinged latch starts to swing down from its raised position toward the carry handle. 3-7 s: The latch swings smoothly through its arc and lands over the carry handle, the casing and the cradle staying rigid. 7-10 s: The latch closes against its fixed end stop over the handle, the amber glass center glowing steadily, as the push-in eases closer. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C60 — Kapı gücü açılır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C60.png
```

> Not: Replik R62 (Rhea, telsiz, 1,5–3,0 s; "Gate feed on." kol durdurucuya inince söylenir → vuruş 3-7 s, §5 saniyesi ≈3,5'a çekilebilir; yüz kadraj dışı, yalnız sağ eldiven ve inci kol). T01: eldiven kare başında mavi kolu kavramış (temas kurulu), video yalnız kolu aşağı çeker; çekirdek yuvada mandallı ve aktif (C59 sonrası), amber merkez düşük parlaklıkta, videoda güçlenir.
> Kamera konsolun sağ ucunda, kol hizasında (C59'dan açı farkı ≥30°). Mavi kol tek hareketli öğe; turuncu ve teal kol dik, kadraj kenarında. Askı boş (kolun kapsamında görünmez).

### Görsel
```text
Reference 2 (woman): take her white glove and pearl sleeve from it, using the front full-body panel. Reference 10 (core): take the compact rectangular graphite casing with ivory corner guards, the rigid top carry handle with the closed hinged latch over it and the amber glass center from it, using the cradle close panel. Reference 12 (control room): take the console with the broad blue gate-power lever, the rectangular core input cradle and the cyan abstract console lights from it, using the console close panel. Close view on an 85 mm lens at lever height, the camera 70 cm from the console at its right-hand end, looking along it. Her right white glove and the pearl sleeve of her pressure suit enter from the right edge of the frame and already close around the broad blue gate-power lever, which stands upright. The power core sits latched in the rectangular input cradle beside the lever, the latch closed over its carry handle and its amber glass center glowing at a low level. The broad teal port-clamp release lever and the orange mechanical gate-catch lever stand upright further along the console, softly out of focus. Only her glove and sleeve are in the frame. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow, small push-in begins as her glove, closed around the broad blue lever, pulls it steadily toward her and the lever starts to tilt down on its hinge. 3-7 s: The lever travels down to its fixed end stop and the amber glass center of the core in the cradle beside it strengthens to a brighter glow; a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says from out of frame: Gate feed on. 7-10 s: The push-in eases closer as the glove stays closed around the lever at the bottom of its travel and the amber glow holds steady across the cradle and the console. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini görselden video 10 s ile hedefler. Süre ve ses davranışı SMOKE P11 · P14 · P18'de ölçülür (`uretim_hatti/FLOW_GERCEKLERI.md` §1 · §9); ölçüm gelmeden videolar koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9.
> **Replikli klipler (bu grupta C49 · C50 · C51 · C52 · C53 · C54 · C55 · C56 · C57 · C58 · C60):** SMOKE P18 sonucuna bağlı; bozuk duyulan klibin sesi kurguda eklenir (timeline `ses` parçası, FILM.md §5 kaydı yedek). C49 repliği `dead` sözcüğü taşır (makine bağlamı, planın repliği): red gelirse replik kurguda eklenir ve bu vuruştan çıkarılır.
> **Dış klipler (C52 · C57):** klip sesi yalnız replik penceresinde (±0,5 s) açık tutulur, kalan süre Y1 yatağı (T13).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kare üretimi için panel adı parantezde. Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.
> **Öneri (risk sırası, zorunlu değil):** el-nesne teması taşıyan C58 · C60 · C51 · C56 ve vakumda kıvılcımlı C52 önce denenir.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C49 kare | `kare/C49.png` | Görsel | ref/1.LEON_v1.png (arkadan tam boy paneli) · ref/13.KOMUTA_v1.png (geniş köprü paneli; bu sırayla) | 2 | |
| 2 | C50 kare | `kare/C50.png` | Görsel | ref/2.RHEA_v1.png (askı çekirdekli panel) · ref/10.CEKIRDEK_v1.png (çekirdek nesne paneli) · ref/12.KONTROL_ODASI_v1.png (geniş oda paneli; bu sırayla) | 2 | |
| 3 | C51 kare | `kare/C51.png` | Görsel | ref/1.LEON_v1.png (eldiven paneli) · ref/13.KOMUTA_v1.png (pilot konsol paneli; bu sırayla) | 2 | |
| 4 | C52 kare | `kare/C52.png` | Görsel | ref/9.KOPRU_v1.png (dış sağlam panel) · ref/11.DRONE_v1.png (drone ön paneli; bu sırayla) | 2 | |
| 5 | C53 kare | `kare/C53.png` | Görsel | ref/2.RHEA_v1.png (askı çekirdekli panel) · ref/12.KONTROL_ODASI_v1.png (geniş oda paneli; bu sırayla) | 2 | |
| 6 | C54 kare | `kare/C54.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/13.KOMUTA_v1.png (pilot konsol paneli; bu sırayla) | 2 | |
| 7 | C55 kare | `kare/C55.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/13.KOMUTA_v1.png (pilot konsol paneli; bu sırayla) | 2 | |
| 8 | C56 kare | `kare/C56.png` | Görsel | ref/2.RHEA_v1.png (askı çekirdekli panel) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli) · ref/15.ARACLAR_v1.png (bilek bağlantısı paneli; bu sırayla) | 2 | |
| 9 | C57 kare | `kare/C57.png` | Görsel | ref/3.KESTREL_v1.png (burun yakası kilitli panel) · ref/5.FOUNDRY_v1.png (geniş dış panel) · ref/6.ARK_v1.png (kıç paneli; bu sırayla) | 2 | |
| 10 | C58 kare | `kare/C58.png` | Görsel | ref/2.RHEA_v1.png (önden tam boy paneli, askı boş) · ref/10.CEKIRDEK_v1.png (çekirdek nesne paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 11 | C59 kare | `kare/C59.png` | Görsel | ref/10.CEKIRDEK_v1.png (beşik yakın paneli; mandal AÇIK istenir) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 12 | C60 kare | `kare/C60.png` | Görsel | ref/2.RHEA_v1.png (önden tam boy paneli) · ref/10.CEKIRDEK_v1.png (beşik yakın paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 13 | C49 | `ham/C49_d1.mp4` | Frames to Video | kare/C49.png | 2 | |
| 14 | C50 | `ham/C50_d1.mp4` | Frames to Video | kare/C50.png | 2 | |
| 15 | C51 | `ham/C51_d1.mp4` | Frames to Video | kare/C51.png | 2 | |
| 16 | C52 | `ham/C52_d1.mp4` | Frames to Video | kare/C52.png | 2 | |
| 17 | C53 | `ham/C53_d1.mp4` | Frames to Video | kare/C53.png | 2 | |
| 18 | C54 | `ham/C54_d1.mp4` | Frames to Video | kare/C54.png | 2 | |
| 19 | C55 | `ham/C55_d1.mp4` | Frames to Video | kare/C55.png | 2 | |
| 20 | C56 | `ham/C56_d1.mp4` | Frames to Video | kare/C56.png | 2 | |
| 21 | C57 | `ham/C57_d1.mp4` | Frames to Video | kare/C57.png | 2 | |
| 22 | C58 | `ham/C58_d1.mp4` | Frames to Video | kare/C58.png | 2 | |
| 23 | C59 | `ham/C59_d1.mp4` | Frames to Video | kare/C59.png | 2 | |
| 24 | C60 | `ham/C60_d1.mp4` | Frames to Video | kare/C60.png | 2 | |
