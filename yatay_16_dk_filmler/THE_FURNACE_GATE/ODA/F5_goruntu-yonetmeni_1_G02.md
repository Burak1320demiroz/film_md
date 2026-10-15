# 🖼️ THE_FURNACE_GATE — Prompt grubu G02 (çekimler C13–C24)

> Yazan: goruntu-yonetmeni (tur 1). Denetleyen: devamlilik · teknik-danisman.
> Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K13-K24 + `FILM.md` §3 · §4 · §5. Bu dosya yeniden tasarım değil, biçim çevirisidir:
> kompozisyon, olay, replik ve tasarım planın kendisi; cümleler olabildiğince planın İngilizcesi. Plan kalıpları çıkarıldı: "Use the attached reference
> images only…", "Create one film still, not a reference sheet", "horizontal 16:9 / 10 seconds", "Animate the uploaded scene still as the first frame",
> "Preserve the existing faces…", olumsuz kuyruk ("No readable text…", "No new people…", "No spoken dialogue…") ve "Continuity overrides…" paragrafı
> (durum bilgisi, kadrajdaki nesne için pozitif cümleye çevrildi). Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı,
> referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Zincir yok (plan zincir kurmaz); her çekim kendi başlangıç karesiyle Frames to Video. `EKLE` satırı iki parçalıdır: KARE (görsel üretimi için
> referanslar, yükleme sırasıyla) · VİDEO (yalnız kare; Frames to Video'ya referans eklenmez, yoksa mod Ingredients'e kayar).
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında
> `Reference <No> (<rol>): …` diye adlandırılır. Her video promptu 10 s'yi 2-4 vuruşa böler (0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s,
> son vuruş donmaz; ilk vuruş hareketle başlar).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** FILM.md §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir;
> MEKÂN IŞIĞI cümlesi her görsel promptta `The light is …` sarmalayıcısıyla (kelimeler FILM.md §3'teki gibi); ORTAM SESİ cümlesi o mekânın her
> video promptunda birebir (ortak görünümden hemen önce). Bu filmde bütün replikler model sesi (Flow'da ses AÇIK): replik video promptuna birebir
> `says: <line>` biçiminde yazılır (tırnaklı biçim SMOKE P9'a kadar yedek), konuşanın sesi ve kaynağı FILM.md §3 SES KİMLİĞİ kelimeleriyle tarif edilir.
> Ağız kadrajda repliklerde konuşanın dudağı yalnız kendi cümlesinde oynar, öteki kişinin ağzı kapalı yazılır; telsiz repliklerde konuşan kadraj
> dışıdır (`out of frame`) ve ses `softened by a light suit-radio filter` ekini taşır.
> **Ortak cümleler bu grupta birebir (FILM.md §3 KİMLİK TABANI):** adam `an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet` ·
> kadın `an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet`.
> Adlar (Leon, Rhea) prompt gövdesine yazılmaz (büyük harfli ad kadraja basılır, BILINEN §C): `the man` / `the woman`. Rozet tarafı (asimetrik) torsonun
> göründüğü her karede ayrı cümleyle yazılır: `His badge sits on his left chest.` Kadının askısı bu grupta her karede boş (çekirdek C26'da beşikten çıkar).
> **Gök cümlesi (T18; bu grupta C16 ve C18'de birebir, G01/diğer gruplarla hizalanmak üzere Fable'a önerilir):**
> `Deep black space with sparse stars surrounds the foundry, and a huge curved blue gas giant fills the far background.`
> **Panel adları (FILM.md §3'ten; G01 sayfaları; çekim başına her referanstan yalnız TEK panel):** 1.LEON ve 2.RHEA `front full-body panel` (geniş) ·
> `side full-body panel` (C17, yürüyüş) · `face close-up panel` (orta/yakın) · 7.KORIDOR `junction panel` · `wide corridor panel` · 9.KOPRU `interior tunnel panel` ·
> `exterior intact panel` · 10.CEKIRDEK `vault wide panel` · 11.DRONE `drone front panel` · 12.KONTROL_ODASI `wide room panel` · `console close panel` ·
> 15.ARACLAR `tether panel` · `emp puck panel` · `cutter panel` · 5.FOUNDRY `wide exterior panel`. Panel adlandırması G01 yazarının sayfalarıyla aynı kalmalı.
> **Kelime güvenliği (BILINEN §A · §C):** `body` ve türevleri geçmez (drone için `housing`); gri disk "EMP" diye anılmaz (büyük harfli kısaltma kadraja basılır;
> `emp puck panel` yalnız referans cümlesinde); kol adları her seferinde bir nesneye bağlanır (`the blue gate-power lever` · `the teal clamp-release lever` ·
> `the orange gate-catch lever`), "A" harfi kodu yazılmaz; kumanda ve gösterge `unmarked` / `abstract`.

---

## C13 — Rhea yükleme köprüsü kapısını işaret eder

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png · VİDEO (Frames to Video): yalnız kare/C13.png
```

> Not: Replik R13 (Rhea, ağız kadrajda, 1.5–5.5 s) birinci vuruşun içinde; Leon'un ağzı kapalı. Plan "Rhea points once": tek kol hareketi — kalkar, uzanır, son vuruşta iner (donmaz).
> Rhea, Leon'un bir adım önüne alındı ki işaret eden kolu onun önünden geçmesin; "Leon solda, Rhea sağda" korunur. Kavşak 7.KORIDOR `junction panel` yönüyle aynı:
> yükleme köprüsü kapısı solda, komuta kapısı uzak sağda. Askı boş (T09). Birinci vuruşta kamera ileri süzülür (kesme fotoğraftan açılmasın). Kriyo penceresi sağ duvarda,
> koridor ışığındaki yeşil durum ışığının kaynağı olarak görünür.

### Görsel
```text
Reference 1 (man): take his face, the clear closed helmet and the ivory suit from it, using the front full-body panel. Reference 2 (woman): take her face, the clear closed helmet, the pearl suit and the empty core-carry harness from it, using the front full-body panel. Reference 7 (corridor): take the ivory walls, the graphite grating, the navy handrails, the amber emergency lamps and the two doorways from it, using the junction panel. Wide view down the ark's pressurized corridor on a 28 mm lens at eye level, the camera about 7 m from the junction. The corridor has ivory walls, a graphite grating floor, fixed navy handrails and amber emergency lamps along the ceiling; at frame-left an open rectangular doorway in the side wall leads to the sealed foundry loading bridge, far away at frame-right a second rectangular doorway leads to the ark command bridge, and a side observation window in the right-hand wall glows faintly green. Exactly 2 adults stand at the junction between the two doorways, boots on the grating, both seen from the front in three-quarter view. At the left of the frame stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest. To the right of him in the frame, a pace nearer the camera, stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. Their arms hang at their sides, both mouths are closed, and her helmet is turned slightly toward the loading-bridge doorway at frame-left. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-6 s: The camera eases slowly forward along the corridor while the woman's arm rises from her side; as it extends toward the loading-bridge doorway at frame-left, one white-gloved finger leading, the man's lips stay closed and her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: The core first. Then we separate the gate from its automation. 6-10 s: Her arm lowers in one smooth motion back to her side and her helmet turns from the doorway toward the man, whose eyes follow the doorway; the camera keeps easing forward, the doorway at frame-left growing slightly larger. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C14 — Leon tether bağlantısını kavrar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/7.KORIDOR_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C14.png
```

> Not: Replik R14 (Leon, ağız kadrajda, 1.5–3.5 s) birinci vuruşun içinde. T01: eldiven kareden itibaren tether bağlantı bloğunun üstünde (temas kurulu); video yalnız tek kısa kavrama
> ve gevşemeyi ister. Hangi elin kullanıldığı yazılmadı (tether'in kemerdeki yeri 1.LEON ve 15.ARACLAR sayfasına bağlı; yazıya taraf basmak G01 sayfasıyla çatışabilir). Leon, kare solunda
> köprü kapısına bakar: sol ¾ önden, sol şakak yarası görünür. YEDEK (kavrama el-nesne kaynaşırsa): kavrama vuruşu çıkar, eldiven bloğa dayalı kalır, yalnız kask ve göz hareketi.
> Tether'in sonraki kullanımı (aile çatışması ve final kurtarma) bu çekimle erken kurulur (plan devamlılık notu).

### Görsel
```text
Reference 1 (man): take his face and the clear closed helmet from it, using the face close-up panel. Reference 7 (corridor): take the ivory wall, the graphite grating and the open loading-bridge doorway with its navy handrail from it, using the junction panel. Reference 15 (tools): take the coiled navy safety tether with its single rigid silver magnetic anchor block from it, using the tether panel. Medium close-up on a 50 mm lens at eye level, the camera about 2 m from him, framing him from the top of his helmet down to below his belt. Exactly 1 adult stands at the right of the frame beside the open loading-bridge doorway, which shows as a squared opening in the ivory wall at frame-left: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest. He is seen in three-quarter view from his left front with his helmet turned toward frame-left, so that his pale left-temple scar and his brown eyes show plainly behind the clear visor, and his mouth is closed. A compact graphite plasma cutter with a short blue tip is clipped to his belt, and the coiled navy safety tether hangs from the same belt with its single rigid silver magnetic anchor block; one white glove already rests on that anchor block. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera starts a slow push toward his helmet and shoulders while his white glove, already on the anchor block, tightens once around it in a short, firm grip; his lips move only for his own line and he says in a low, dry adult man's voice, calm and guarded: And keep a way back. 4-7 s: His fingers open and the glove relaxes at his belt beside the anchor block as the push continues and his eyes follow the edge of the doorway at frame-left. 7-10 s: The push closes further on his clear visor, his chest rising with a slow breath, the cutter and the tether staying clipped to the belt. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C15 — Rhea gri diski avuca alır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C15.png
```

> Not: Replik R15 (Rhea, ağız kadrajda, 1.5–5.0 s) birinci vuruşun içinde. FILM.md §4'teki 10.CEKIRDEK çıkarıldı: askı boş, çekirdek kadrajda yok; sayfa kareye çekirdek çağırabilir (T09).
> Askı boşluğu 2.RHEA sayfası + metinle taşınır. Gri disk "EMP" diye anılmaz (§C), panel adı `emp puck panel` yalnız referans cümlesinde. T01: avuç önceden açık ve diskin altında,
> disk hâlâ klipste; video yalnız diski klipsten avuca alır, ardından avuç hafifçe kare soluna (Leon'un durduğu yön) döner. Hangi elin avuç olduğu yazıldı (sağ), disk kemerde yazılı tarafsız.
> YEDEK (el-nesne kaynaşırsa): disk karede zaten avucunda başlar, video yalnız avucun dönüşünü ister. Rhea'nın sağ çene yarası: kadın kameraya yüzü dönük, bakış kare soluna.

### Görsel
```text
Reference 2 (woman): take her face and the clear closed helmet from it, using the face close-up panel. Reference 7 (corridor): take the ivory wall, the graphite grating and the navy handrail from it, using the wide corridor panel. Reference 15 (tools): take the small matte-grey puck with its amber indicator and the compact graphite plasma cutter from it, using the emp puck panel. Medium shot on a 35 mm lens at eye level, the camera about 3 m from her, framing her from the top of her helmet down to mid-thigh. Exactly 1 adult stands in the ark corridor with her front toward the camera: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. A compact graphite plasma cutter with a short blue tip and a small matte-grey puck with one amber indicator are secured to her belt. Her right white glove is already at her belt, the palm open and turned up beneath the puck, the fingertips curled lightly around its lower edge, while the puck is still clipped in place; her left arm hangs at her side. Her eyes are directed at a partner out of frame at frame-left, and her mouth is closed. Behind her stand the ivory wall, a fixed navy handrail and the graphite grating. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera drifts slowly in toward her as her open white glove draws the grey puck smoothly out of its belt clip into the open palm; her lips move only for her own line and she says in a clear, quick adult woman's voice, precise and controlled: Keep this for a sentry. Not for a door. 5-8 s: The puck lies in the open palm with its amber indicator glowing, and her forearm turns the palm a little toward frame-left as her eyes follow it. 8-10 s: The camera keeps drifting in on the palm and the puck while her chest rises with a slow breath, the cutter staying clipped to her belt and the harness staying empty. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C16 — Drone köprü camının önünden kayar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/9.KOPRU_v1.png · ref/11.DRONE_v1.png · VİDEO (Frames to Video): yalnız kare/C16.png
```

> Not: Replik R16 (Leon, telsiz, 1.5–3.0 s) birinci vuruşun içinde; kadrajda kimse yok, ses kadraj dışı. Kamera köprünün içinde, cam yanına bakar; köprü ekseni karede soldan sağa
> (ark ucu solda, foundry ucu sağda, 9.KOPRU yönü). Drone ilk karede sağda (foundry ucu), sola doğru kayar; rijit, jetler ve yayıcı sönük (plan "no firing" → pozitif tarif; vakumda plume yok, T13).
> Drone tarifinde `body` yerine `housing` (BILINEN §A). Mekân köprü içi: ışık ve ortam sesi KÖPRÜ İÇİ cümleleri; camın ötesi gök cümlesiyle (yukarıda, C18 ile birebir). Kareye insan zamiri girmez (A08).
> Köprü sağlam (plan).

### Görsel
```text
Reference 9 (loading bridge): take the square graphite pressure tunnel with its reinforced glass side, the waist-high rail and the grated floor edge from it, using the interior tunnel panel. Reference 11 (drone): take the rigid graphite sentry drone with its narrow red sensor strip from it, using the drone front panel. Wide view from inside the intact enclosed loading bridge on a 24 mm lens at chest height, looking out through one of its reinforced glass sides. The tunnel runs across the frame: its ark end recedes at frame-left and its foundry end lies at frame-right, a waist-high rail and the grated floor edge fill the bottom foreground, and fixed glass mullions divide the window. The tunnel is empty. Outside the glass, a few meters away near the foundry end at frame-right, one autonomous industrial sentry drone hovers: a rigid compact graphite rectangular housing of matte scuffed metal with one narrow horizontal red sensor strip across its front, glowing and facing the glass, two recessed maneuvering jets unlit, and one short forward emitter dark. Deep black space with sparse stars surrounds the foundry, and a huge curved blue gas giant fills the far background. The loading bridge is intact. The light is cool blue light through the reinforced glass sides and amber guide lamps along the rails. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow push toward the glass while the drone starts to slide leftward along the outside of the window, its red sensor strip glowing steadily at the glass, and a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, out of frame, says: Security is still awake. 4-8 s: The drone glides on across the middle of the window at an even, slow pace and passes behind a glass mullion, its rigid housing keeping its shape and its emitter dark, the red strip throwing a faint red reflection along the pane and the rail while the amber guide lamps glint on the glass. 8-10 s: The drone drifts into the left half of the window as the push closes slightly, its two jets unlit, the rail and the grated floor edge staying fixed in the foreground. The only ambient sound is a thin pressurized tunnel hum with a faint creak of rigid metal. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C17 — İkisi kapalı köprüde iki dikkatli adım atar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/9.KOPRU_v1.png · VİDEO (Frames to Video): yalnız kare/C17.png
```

> Not: Replik R17 (Rhea, ağız kadrajda, 1.5–3.5 s) birinci vuruşun içinde; Leon'un ağzı kapalı. Yürüyüş soldan sağa, kamera yandan iç yüzeye yaslı takip eder: ikisi profilde, Leon geride (solda),
> Rhea bir adım önde (sağda) — "Leon solda, Rhea sağda" korunur. 1.LEON ve 2.RHEA `side full-body panel`. Rhea konuşurken kaskını hafifçe geriye, Leon'a çevirir (ağız okunur kalsın).
> T10: iki kısa adım, koşu yok; adımlar vuruşlara bölündü (0-4 · 4-8 · 8-10). Ark kapağı uzak solda küçük bir dikdörtgen, foundry kapısı sağda açık. Köprü sağlam; askı boş.

### Görsel
```text
Reference 1 (man): take his face, the clear closed helmet and the ivory suit from it, using the side full-body panel. Reference 2 (woman): take her face, the clear closed helmet, the pearl suit and the empty core-carry harness from it, using the side full-body panel. Reference 9 (loading bridge): take the square graphite pressure tunnel, the reinforced glass sides, the waist-high rails, the grated floor and the amber guide lamps from it, using the interior tunnel panel. Wide side-on view inside the intact enclosed loading bridge on a 20 mm lens at chest height, the camera against the tunnel wall about 3 m from the pair. The tunnel runs across the frame: its ark hatch lies far away at frame-left as a small distant rectangle, and an open rectangular foundry doorway stands at frame-right a few paces ahead of the pair. Exactly 2 adults stand near the foundry end in profile facing frame-right, boots on the grated floor. At the left of the frame stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest. A pace ahead of him, at his right in the frame, stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. Their arms hang at their sides, both mouths are closed, and her helmet is turned slightly back toward him. The loading bridge is intact. The light is cool blue light through the reinforced glass sides and amber guide lamps along the rails. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera tracks slowly to the right at the pair's pace while the woman takes a careful first step toward the open foundry doorway with her helmet turned slightly back toward the man; his lips stay closed while her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Stay inside the pressure line. 4-8 s: The man matches her with one careful step as she plants her second step on the grating, the rails and glass frames sliding past behind them. 8-10 s: The pair reaches the threshold of the open foundry doorway at frame-right as the camera finishes its slow track, the grated floor and rails still gliding by. The only ambient sound is a thin pressurized tunnel hum with a faint creak of rigid metal. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C18 — Köprünün altında acil tug soketi

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/9.KOPRU_v1.png · VİDEO (Frames to Video): yalnız kare/C18.png
```

> Not: Replik R18 (Leon, telsiz, 1.5–4.5 s) birinci vuruşun içinde; kadrajda kimse yok. FILM.md §4'teki 3.KESTREL çıkarıldı: tug kadrajda değil, referans kareye tug çağırabilir; soket tarifi 9.KOPRU
> `exterior intact panel` + metinle. Soket ve iskele finalin yolu (C77 · C83-C87, 14.ISKELE): burada aynı tasarım sözcükleriyle (yuvarlak soket · tek geniş menteşeli yaka kelepçesi açık · manyetik bot plakası ·
> pille çalışan amber kılavuz lambalar) yazıldı. Dış çekim (vakum): ışık DIŞ cümlesi, gök cümlesi yukarıdaki; T13: bu çekimde klip sesi yalnız replik penceresinde açılır (F8). Ark ucu karenin sol kenarında,
> köprü sağlam. Tilt ilk karede zaten görünen sokete doğru iner ve yan hava kilidini açar.

### Görsel
```text
Reference 9 (loading bridge): take the square graphite pressure tunnel with its reinforced glass sides and its rigid end platform from it, using the exterior intact panel. Exterior wide view on a 24 mm lens, the camera about 40 m from the bridge's foundry end and level with the bridge. The intact telescoping loading bridge crosses the upper half of the frame as a square graphite tunnel with reinforced glass sides, its ivory ark end at the far left edge and its rigid foundry end platform at frame-right where it meets the huge black foundry control spine. Directly below the foundry end, in the lower third of the frame, a short rigid railed catwalk with a fixed magnetic boot plate and amber battery guide lamps runs from a small side airlock hatch in the spine to a small round tug docking socket with one broad hinged collar clamp, open. All surfaces are unmarked. Deep black space with sparse stars surrounds the foundry, and a huge curved blue gas giant fills the far background. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera starts a slow downward tilt from the bridge's foundry end; the end platform rises out of the top of the frame and the catwalk and the round socket climb toward the middle, while a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, out of frame, says: An emergency socket below us. Good to know. 5-8 s: The tilt continues past the socket's open collar clamp and the catwalk rail, and the small side airlock hatch comes into view where the catwalk meets the black foundry spine. 8-10 s: The tilt slows to a gentle drift as the airlock, the catwalk and the socket come together in the middle of the frame with the intact bridge still above them; every structure stays rigid. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C19 — Kontrol odasına ilk bakış

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C19.png
```

> Not: Replik R19 (Rhea, ağız kadrajda, 1.5–4.0 s) birinci vuruşun içinde; Leon'un ağzı kapalı. FILM.md §4'teki 10.CEKIRDEK çıkarıldı: giriş yuvası boş (T09), çekirdek bu odada henüz yok;
> yuva şekli 12.KONTROL_ODASI `wide room panel` sayfasında. Üç kol dik (mavi · teal · turuncu, etiket yok, T06); iris arka camda üç kepenk kısmen kapalı. İkisi kare solunda, köprü kapısının hemen içinde
> (R13: köprü kapısı solda); Leon kapıya yakın (solda), Rhea onun sağında. Dolly konsola doğru; figürler kadrajın solunda kalır, Rhea konuşurken yüzü okunur. Plan "kaptan olmayan konsol" = odada kimse konsolda değil.

### Görsel
```text
Reference 1 (man): take his face, the clear closed helmet and the ivory suit from it, using the front full-body panel. Reference 2 (woman): take her face, the clear closed helmet, the pearl suit and the empty core-carry harness from it, using the front full-body panel. Reference 12 (control room): take the low console with its empty rectangular input cradle, the 3 upright levers, the rear reinforced window and the cyan abstract console lights from it, using the wide room panel. Wide view of the foundry gate-control room on a 24 mm lens at eye level, the camera inside the room facing the rear reinforced window. A low console stands across the middle of the room with an empty rectangular input cradle at its centre; on fixed hinges with visible end stops stand 3 unmarked levers upright: a broad blue gate-power lever and a broad teal clamp-release lever side by side near the cradle, and a separate orange gate-catch lever set a little apart. Beyond the console the rear window shows the exit iris, a ring of 3 rigid radial shutters partly closed against deep black space. At the left of the frame, just inside the doorway to the loading bridge, exactly 2 adults stand side by side, both in three-quarter view turned toward the console. Nearer the doorway stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest. At his right in the frame stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. Their arms hang at their sides and their mouths are closed. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera begins a slow dolly forward toward the unoccupied console while the woman turns her helmet slightly toward the levers; the man's lips stay closed while her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Gate power here. Clamp release beside it. 5-8 s: The dolly continues and the 3 upright levers and the empty input cradle grow larger in the lower centre of the frame, the cyan console lights glowing softly, the two figures remaining at the doorway at the left of the frame. 8-10 s: The dolly closes on the console, the exit iris in the rear window growing slightly larger above it, the levers and the cradle staying exactly in place. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C20 — Leon iki kelepçe koluna bakar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/5.FOUNDRY_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C20.png
```

> Not: Replik R20 (Leon, ağız kadrajda, 1.5–4.0 s) birinci vuruşun içinde. FILM.md §4'e 5.FOUNDRY eklendi (plan R01 + R13): pencerenin ötesindeki ark ve iki gantri kolu büyük bir tasarım nesnesi,
> sayfa 12'de yok; `wide exterior panel` (iki kelepçe kilitli). Geometri: kontrol odası ark'ın port yanında, yakın kol port flanşını tutar (pencerenin sağ yarısı, büyük), karşı kol gövdenin öbür yanında
> daha derinde ve küçük (pencerenin sol yarısı; C68 "opposite clamp visible locked deeper behind" ile aynı). Leon kare sağında, ¾ sol önden, bakışı sola: önce yakın kol, sonra uzak kol (göz hattı kaskın sola
> dönüşüyle uyumlu). Küçük bakış dönüşü ikinci vuruşta, replik birinci vuruşta (bakış dönüşü + dudak senkronu aynı anda istenmedi). Kollar kilitli ve rijit (iki kol ark'ı tutar).

### Görsel
```text
Reference 1 (man): take his face and the clear closed helmet from it, using the face close-up panel. Reference 5 (foundry): take the long white colony ark held in the black cradle by its 2 enormous rigid gantry clamp arms from it, using the wide exterior panel. Reference 12 (control room): take the rear reinforced window frame and the cool blue gate light from it, using the wide room panel. Medium shot on a 50 mm lens at eye level, the camera inside the gate-control room beside the rear reinforced window, about 2.5 m from him. The window fills the left two thirds of the frame. Beyond the glass the long ivory colony ark lies across the view, held by 2 enormous rigid gantry clamp arms on opposite hull flanges: a near arm gripping the hull flange at the right of the window, large and sharp, and a second arm gripping the opposite flange on the far side of the hull at the left of the window, smaller and deeper behind it; both arms are locked on the ark. Exactly 1 adult stands at the right of the frame at the window, framed from his head to his waist: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest. He is seen in three-quarter view from his left front with his helmet turned toward frame-left, so that his pale left-temple scar and his brown eyes show plainly behind the clear visor, his gaze directed through the glass at the near arm, his mouth closed. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera starts a slow, small push toward him as his gaze rests on the near gantry arm; his lips move only for his own line and he says in a low, dry adult man's voice, calm and guarded: Two clamps. Releasing one won't free her. 4-7 s: His helmet turns a few degrees further toward frame-left and his eyes sweep across the window along the ark's hull from the near arm to the far arm. 7-10 s: His gaze reaches the far arm as the push continues, his chest rising with a slow breath, while the 2 arms and the ark stay locked and rigid. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C21 — Turuncu mandal kolu yerinde

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C21.png
```

> Not: Replik R21 (Rhea, ağız kadrajda, 1.5–5.0 s) birinci vuruşun içinde. Repliğin son kelimesi "dies" — metin planın kendisi, değişmez; sahne ölümü değil mandal/güç anlatır (BILINEN §A listesinde yok, ama ret gelirse
> ilk bakılacak kelime). T01 el temassız (bilinçli): eldiven mandal kolunun tutamağının bir avuç yukarısında ve yanında; video eli hareket ettirmez, yalnız kamera kayar. Kol şimdi çekilmez (sonucu C65'te).
> Kamera sağa kayar; mandal kolunun sabit menteşesi ve uç durdurucusu parallaxla görünür. Kol, 12.KONTROL_ODASI `console close panel` ile aynı: menteşe ve durdurucu görünür, etiket yok (T06).
> Hangi gözün/yarının ne olduğu: Rhea'nın sağ çene yarası kameraya dönük (yüz önden ¾).

### Görsel
```text
Reference 2 (woman): take her face and the clear closed helmet from it, using the face close-up panel. Reference 12 (control room): take the low console, the orange gate-catch lever with its fixed hinge and end stop, and the rear window from it, using the console close panel. Medium shot on a 50 mm lens at eye level, the camera inside the gate-control room about 2.5 m from the console, framing from her head to her waist. Exactly 1 adult stands behind the low console at the left of the frame, seen from the front in three-quarter view, her eyes on the lever, her mouth closed: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. In the right half of the frame the separate orange gate-catch lever stands upright on the console on its fixed hinge, with a visible end stop at its base; her right white glove hovers a hand's width above the lever's grip, the fingers open. The broad blue gate-power lever and the broad teal clamp-release lever also stand upright, farther along the console, and the rear window behind her glows as a soft blur. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-6 s: The camera begins a slow, even slide sideways to the right along the console; the woman's eyes stay on the orange lever and her glove stays a hand's width above its grip while her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: This catch holds the gate open, even if power dies. 6-10 s: The slide continues and the lever's fixed hinge and the end stop at its base come into view as the parallax shifts the rear window behind it; the lever stays upright, her glove drifts no closer, and her shoulders rise once with a slow breath. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C22 — Leon Rhea'ya döner, Rhea bakışını kaçırır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/12.KONTROL_ODASI_v1.png · VİDEO (Frames to Video): yalnız kare/C22.png
```

> Not: İki replik: R22 (Leon → Rhea, ağız kadrajda, 1.0–2.5 s) birinci vuruşta, R23 (Rhea, ağız kadrajda, 3.0–4.5 s) ikinci vuruşta; her vuruşta öteki kişinin ağzı kapalı. Vuruş sınırı 3 ve 6 s
> (replik pencereleri ve geçiş aralığı dışında). "Suspicious / composed" fiziksel ifadeyle yazıldı (kaş, bakış yönü); zihinsel fiil yok. Leon kare solunda, Rhea sağında; ikisi de yüzü okunur:
> Leon'un sağ yanağı kameraya, Rhea'nın sağ çene yarası kameraya dönük (Rhea konsola/kare sağına bakar). Kol sıraları konsolun önünde, belden yukarı kadraj; üç kol dik. Kamera yavaş yaklaşır.
> Rhea bakışını kaçırması replikten ÖNCE değil sonra başlar: ikinci vuruşta gözleri Leon'dan konsola kayar, ardından konuşur.

### Görsel
```text
Reference 1 (man): take his face and the clear closed helmet from it, using the face close-up panel. Reference 2 (woman): take her face and the clear closed helmet from it, using the face close-up panel. Reference 12 (control room): take the low console with its 3 upright levers and the cool blue window light from it, using the console close panel. Close two-shot on a 50 mm lens at eye level, the camera inside the gate-control room about 1.8 m from the pair, framing both from the top of their helmets down to their waists, with the low console edge and the tops of its 3 upright unmarked levers (blue, teal and orange) along the bottom of the frame. Exactly 2 adults stand side by side at the console, both seen from the front in three-quarter view. At the left of the frame stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest; his brow is drawn down, his gaze fixed forward on the levers, his mouth closed. At the right of the frame stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty; her face is relaxed, her eyes directed at the console toward frame-right, her mouth closed. Behind them the rear window glows as a soft blur. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow drift closer while the man turns his helmet slightly toward the woman; the woman's lips stay closed while his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: You know this place. 3-6 s: The woman's eyes slide away from him toward the console as the drift continues; the man's lips stay closed while her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: I know machines. 6-10 s: The man's helmet stays turned toward her, his brow lowered, while she keeps her eyes on the console; the drift closes slightly on the pair, both chests rising with a slow breath. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C23 — Kesici kasa mandalına dayalı

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · ref/15.ARACLAR_v1.png · VİDEO (Frames to Video): yalnız kare/C23.png
```

> Not: Replik R24 (Rhea, ağız kadrajda, 1.5–4.0 s) birinci vuruşta. T01: kesici ucu kareden itibaren tek küçük mandalda (temas kurulu, uç sönük); video yalnız kısa mavi parıltıyı ve mandalın ayrılmasını ister.
> Kapı geometrisi sabit (kapı kanadı, çerçeve, dikiş yerinde kalır; C24 açık kapıyla başlar, açılma kesmede). Kasa ışığı cümlesindeki "çekirdeğin amber cam merkezinin sıcak ışığı" kapı kenarındaki ince bir
> amber ışık dikişi olarak kadrajda taşınır (çekirdek beşikte, kasada; bu karede görünmez, "kasada çekirdek duruyor" durumu bu ışıkla). Leon kadrajda yok (plan). Kıvılcım/duman yazılmadı (BILINEN §B 4):
> yalnız kısa, sınırlı mavi parıltı. YEDEK (el-nesne kaynaşırsa): kesme sonucu elsiz insert olarak ayrı çekime taşınır (GOSTERIM_COZUMLERI), burada yalnız kesici ucu mandala değerken biter.
> Kesici insana karşı kullanılmaz.

### Görsel
```text
Reference 2 (woman): take her face and the clear closed helmet from it, using the face close-up panel. Reference 10 (core and vault): take the graphite vault walls and the low amber lamps from it, using the vault wide panel. Reference 15 (tools): take the compact graphite plasma cutter with its short blue tip from it, using the cutter panel. Medium shot on a 40 mm lens at eye level, the camera about 2.5 m from her, framing her from the top of her helmet down to her waist. Exactly 1 adult stands at the left of the frame at the entrance of the prototype vault, seen in three-quarter view from her right front with her helmet turned toward frame-right, her mouth closed: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. In the right half of the frame the heavy graphite vault door stands closed in its squared frame, with a hairline seam of warm amber light along its edge and one small metal latch at chest height. Her right white glove holds the compact graphite plasma cutter, its short blue tip unlit and already pressed against the latch. The walls around the entrance are graphite with low amber lamps. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera eases slowly in on the latch while the woman's lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: The contract core is in here. 4-7 s: The cutter's tip flares into one short, contained blue glow and cuts through the small metal latch, its two halves parting, while the vault door, its frame and the hairline amber seam stay exactly where they are. 7-10 s: The blue glow fades back to an unlit tip as the camera keeps easing in, the parted latch halves resting against the door's edge and her glove lowering the cutter slightly. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C24 — Güç çekirdeği ikisinin arasında

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · VİDEO (Frames to Video): yalnız kare/C24.png
```

> Not: İki replik: R25 (Leon, ağız kadrajda, 1.0–2.5 s) birinci vuruşta, R26 (Rhea, ağız kadrajda, 3.0–4.5 s) ikinci vuruşta; her vuruşta öteki kişinin ağzı kapalı. Geniş planda iki konuşan: dudak okunurluğu
> sınırda (risk, aşağıda); yüzler kameraya ¾ dönük ve çekirdeğe bakıyor. Kapı kanadı kare kenarında açık (C23'te kapalıydı, kesmeyle açıldı); yakın kare C23'ten sonra, hareket yok. Çekirdek tek (T09): açık üstlü
> beşikte, geniş menteşeli tutucu mandal taşıma kulpunun üstünde KAPALI (C25'in ilk karesiyle aynı durum). Askı boş. Leon solda, Rhea sağda, çekirdek aralarında.

### Görsel
```text
Reference 1 (man): take his face, the clear closed helmet and the ivory suit from it, using the front full-body panel. Reference 2 (woman): take her face, the clear closed helmet, the pearl suit and the empty core-carry harness from it, using the front full-body panel. Reference 10 (core and vault): take the graphite vault walls, the low amber lamps, the open-topped storage cradle and the compact rectangular power core with its amber glass center from it, using the vault wide panel. Wide view inside the prototype vault on a 24 mm lens at eye level, the camera just inside the open doorway about 5 m from the cradle, the opened heavy graphite door leaf at the edge of the frame. The vault has graphite walls with low amber lamps. At the centre of the frame, in an open-topped storage cradle, sits the single unused portable power core: a compact rectangular graphite casing with ivory corner guards, one rigid top carry handle with the broad hinged retaining latch resting closed over it, and an amber glass center that glows warmly; it is the only core in the vault. Exactly 2 adults stand inside the vault on either side of the core, their bodies in three-quarter view toward the camera and their heads lowered toward the core. At the left of the core stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His badge sits on his left chest. At the right of the core stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her badge sits on her left chest and her harness is empty. Their arms hang at their sides and their mouths are closed. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a restrained push forward between the two toward the core; the woman's lips stay closed while the man's lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: There's our fortune. 3-6 s: The push continues; the man's lips stay closed while the woman's lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: There's their chance. 6-10 s: The push closes further on the amber core between them, its glass center glowing steadily on the graphite walls and on both helmets, the two standing on either side of the cradle with their gaze on the core. The only ambient sound is a close, low electrical hum inside a sealed vault. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini görselden video 10 s ile hedefler (`THE_FURNACE_GATE_16MIN_96_CLIPS.md` §7). Omni'de başlangıç karesi yalnız Flow web'de; süre ve ses davranışı
> SMOKE P11 · P14 · P18'de ölçülür (`uretim_hatti/FLOW_GERCEKLERI.md` §1 · §9); ölçüm gelmeden videolar koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9. Veo 3.1'de klip 4/6/8 s'dir.
> **Replikli klipler (bu grupta C13–C24, hepsi):** SMOKE P18 sonucuna bağlı. Replik klipte yanlış ya da bozuk duyulursa o klibin sesi kurguda eklenir (timeline `ses` parçası; kayıt FILM.md §5 yedek). Dış (vakum) klip C18'de
> klip sesi yalnız replik penceresinde (1.0–5.0 s) açık tutulur (T13; FILM.md §6).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kare üretimi için panel adı parantezde.
> Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C13 kare | `kare/C13.png` | Görsel | ref/1.LEON_v1.png (ön tam boy paneli) · ref/2.RHEA_v1.png (ön tam boy paneli) · ref/7.KORIDOR_v1.png (kavşak paneli; bu sırayla) | 2 | |
| 2 | C14 kare | `kare/C14.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/7.KORIDOR_v1.png (kavşak paneli) · ref/15.ARACLAR_v1.png (tether paneli; bu sırayla) · **el-nesne teması: ilk denenir** | 2 | |
| 3 | C15 kare | `kare/C15.png` | Görsel | ref/2.RHEA_v1.png (yüz yakın paneli) · ref/7.KORIDOR_v1.png (geniş koridor paneli) · ref/15.ARACLAR_v1.png (gri disk paneli; bu sırayla) · **el-nesne teması: ilk denenir** | 2 | |
| 4 | C16 kare | `kare/C16.png` | Görsel | ref/9.KOPRU_v1.png (iç tünel paneli) · ref/11.DRONE_v1.png (ön panel; bu sırayla) | 2 | |
| 5 | C17 kare | `kare/C17.png` | Görsel | ref/1.LEON_v1.png (yan tam boy paneli) · ref/2.RHEA_v1.png (yan tam boy paneli) · ref/9.KOPRU_v1.png (iç tünel paneli; bu sırayla) | 2 | |
| 6 | C18 kare | `kare/C18.png` | Görsel | ref/9.KOPRU_v1.png (dış sağlam panel) | 2 | |
| 7 | C19 kare | `kare/C19.png` | Görsel | ref/1.LEON_v1.png (ön tam boy paneli) · ref/2.RHEA_v1.png (ön tam boy paneli) · ref/12.KONTROL_ODASI_v1.png (geniş oda paneli; bu sırayla) | 2 | |
| 8 | C20 kare | `kare/C20.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/5.FOUNDRY_v1.png (geniş dış panel) · ref/12.KONTROL_ODASI_v1.png (geniş oda paneli; bu sırayla) | 2 | |
| 9 | C21 kare | `kare/C21.png` | Görsel | ref/2.RHEA_v1.png (yüz yakın paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 10 | C22 kare | `kare/C22.png` | Görsel | ref/1.LEON_v1.png (yüz yakın paneli) · ref/2.RHEA_v1.png (yüz yakın paneli) · ref/12.KONTROL_ODASI_v1.png (konsol yakın paneli; bu sırayla) | 2 | |
| 11 | C23 kare | `kare/C23.png` | Görsel | ref/2.RHEA_v1.png (yüz yakın paneli) · ref/10.CEKIRDEK_v1.png (kasa geniş paneli) · ref/15.ARACLAR_v1.png (kesici paneli; bu sırayla) · **el-nesne teması: ilk denenir** | 2 | |
| 12 | C24 kare | `kare/C24.png` | Görsel | ref/1.LEON_v1.png (ön tam boy paneli) · ref/2.RHEA_v1.png (ön tam boy paneli) · ref/10.CEKIRDEK_v1.png (kasa geniş paneli; bu sırayla) | 2 | |
| 13 | C13 | `ham/C13_d1.mp4` | Frames to Video | kare/C13.png | 2 | |
| 14 | C14 | `ham/C14_d1.mp4` | Frames to Video | kare/C14.png · **el-nesne teması: ilk denenir** | 2 | |
| 15 | C15 | `ham/C15_d1.mp4` | Frames to Video | kare/C15.png · **el-nesne teması: ilk denenir** | 2 | |
| 16 | C16 | `ham/C16_d1.mp4` | Frames to Video | kare/C16.png | 2 | |
| 17 | C17 | `ham/C17_d1.mp4` | Frames to Video | kare/C17.png | 2 | |
| 18 | C18 | `ham/C18_d1.mp4` | Frames to Video | kare/C18.png | 2 | |
| 19 | C19 | `ham/C19_d1.mp4` | Frames to Video | kare/C19.png | 2 | |
| 20 | C20 | `ham/C20_d1.mp4` | Frames to Video | kare/C20.png | 2 | |
| 21 | C21 | `ham/C21_d1.mp4` | Frames to Video | kare/C21.png | 2 | |
| 22 | C22 | `ham/C22_d1.mp4` | Frames to Video | kare/C22.png | 2 | |
| 23 | C23 | `ham/C23_d1.mp4` | Frames to Video | kare/C23.png · **el-nesne teması: ilk denenir** | 2 | |
| 24 | C24 | `ham/C24_d1.mp4` | Frames to Video | kare/C24.png | 2 | |

> Öncelikli önizleme (G02 içinde): C14 · C15 · C23 (el-nesne teması, BILINEN §B sıra 1). Biri iki denemede aynı sebeple bozulursa prompta cümle eklenmez; çekim yaklaşımı değişir
> (GOSTERIM_COZUMLERI ilke 8): C14 kavrama vuruşu çıkar, C15 disk avucta başlar, C23 kesme sonucu ayrı elsiz insert çekime taşınır. İki konuşanlı geniş plan C24 ve profilde konuşan C17 dudak okunurluğu
> için kare onayında ayrıca bakılır.
