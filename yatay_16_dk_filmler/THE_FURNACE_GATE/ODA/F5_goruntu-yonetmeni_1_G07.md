# 🖼️ THE_FURNACE_GATE — Prompt grubu G07 (çekimler C73–C84)

> Yazan: goruntu-yonetmeni (tur 1). Denetleyen: devamlilik · teknik-danisman.
> Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K73–K84 + §13 devamlılık; replikler FILM.md §5 (R74–R82). Bu dosya yeniden tasarım değil, biçim çevirisidir:
> olay, kompozisyon, kol/anahtar durumları ve hareket yönü planın kendisi; tek bilinçli fark: temas gerektiren hareketlerde kare temasla başlar (plan §7 "el zaten kolu tutar" ilkesi).
> Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur.
> Olumsuz yasak listesi yazılmaz (plan kuyruğu "No readable text…", "No new people…", "No spoken dialogue…" çıkarıldı; "unmarked" pozitif sıfattır). ≤4.300 karakter.
> Zincir yok (FILM.md §4 Zincir "—"); her çekim kendi başlangıç karesiyle Frames to Video. `EKLE` satırındaki referanslar KARE (Görsel) üretimi içindir;
> Frames to Video'ya yalnız `kare/Cxx.png` yüklenir (referans eklenirse mod Ingredients'e kayar).
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında
> `Reference <No> (<rol>): …` diye adlandırılır, çekim başına her referanstan TEK panel. Her video promptu 10 s'yi 2-4 vuruşa böler
> (0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s, son vuruş donmaz; ilk vuruş hareketle başlar).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** FILM.md §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir;
> MEKÂN IŞIĞI cümlesi her görsel promptta `The light is …` sarmalayıcısıyla (kelimeler FILM.md §3'teki gibi); ORTAM SESİ cümlesi o mekânın her video promptunda
> birebir (ortak görünümden hemen önce). Bu filmde bütün replikler model sesi: replik video promptuna birebir `says: <line>` biçiminde yazılır, konuşanın sesi
> FILM.md §3 SES KİMLİĞİ kelimeleriyle tarif edilir, replik vuruşun SON cümlesidir (sonraki vuruş etiketi repliğin bittiğini gösterir); ağız kadrajda çekimde
> konuşanın dudağı yalnız kendi cümlesinde oynar, telsiz çekimde ses `softened by a light suit-radio filter` ile kadraj dışından gelir.
> **Ortak cümleler (FILM.md §3, bu grupta birebir):** kimlik tabanı iki karakter için tek parça (`one person is in the frame: …` sarmalayıcısıyla), eklenen "askı boş" ayrı cümle ·
> dış mekân ışığı C74 C80 C81 C84'te aynı kelimelerle (T18; §3'te ayrı bir gök cümlesi yok, gaz devi ışık cümlesinin içinde) ·
> `body` sözcüğü ve türevleri hiçbir promptta geçmez (BILINEN_TUZAKLAR §A); plan "body stays anchored" → "boots stay planted".
> **Panel adları** FILM.md §3'te sabit: 1.LEON `face close-up panel` · `side full-body panel`; 2.RHEA `front full-body panel` · `face close-up panel`; 3.KESTREL `side view panel`;
> 4.KOKPIT `pilot side panel`; 5.FOUNDRY `bridge and socket panel`; 6.ARK `stern panel` · `port side panel`; 9.KOPRU `exterior intact panel` · `end platform panel`;
> 10.CEKIRDEK `core spent panel`; 11.DRONE `drone front panel`; 12.KONTROL_ODASI `levers down panel`; 13.KOMUTA `lever B down panel`; 14.ISKELE `catwalk wide panel` · `socket close panel`;
> 15.ARACLAR `tether panel` · `wrist-link panel`; 3.KESTREL `three-quarter panel` (C81).

---

## C73 — Kurtarma bitti sanılırken köprü alarmı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C73.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png · ref/12.KONTROL_ODASI_v1.png
```

> Not: Replik R74 (Rhea, ağız kadrajda, 1.5–5.5 s → birinci vuruş 0-6 s içinde). Kırmızı köprü uyarı lambası karede zaten var, söner durumda (video onu eklemez, atıma geçirir);
> yeri yükleme köprüsü kapısının yanı (FILM.md §3 sayfa 12: kapı SOLDA), Rhea o yöne döner. Çekirdek `core spent panel` (sönük, yanık, yuvada mandallı), üç kol aşağıda (mavi · teal · turuncu),
> askı boş (plan K73 devamlılık). Arka pencere yalnız soğuk mavi ışık taşır: çıkış irisi ve ark kadrajda çizilmez (plan bu çekim için R05/R06/R07 vermedi; kapı açık ve kelepçeler açık kuralı bu yüzden tetiklenmez).
> Sağ çene yarası: Rhea önden ve hafif sağından görünür; dönüş sola olduğu için başlangıç karesi yarayı gösterir.

### Görsel
```text
Reference 2 (woman): take her face, braid, pearl suit and empty chest harness from it, using the front full-body panel. Reference 10 (core): take the spent core with its heat-scored graphite casing and dark glass centre from it, using the core spent panel. Reference 12 (control room): take the low console, its three levers and the room from it, using the levers down panel. Medium shot on a 50 mm lens at eye level inside the foundry gate-control room, the camera facing the low control console. One person is in the frame: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She stands behind the console at the centre of the frame, seen from the front and slightly from her right, her chest harness empty and one gloved hand resting flat on the console edge. In the console's input cradle in front of her sits the single spent core, latched, its casing heat-scored but intact and its glass centre dark. The broad blue gate-power lever, the broad teal port-release lever and the orange gate-catch lever all stand pulled down at their stops. At frame-left the closed door to the loading bridge shows a small reinforced hatch window, and in the wall beside it one round red bridge-warning lamp sits dark; behind her the reinforced rear window glows with cool blue light. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-6 s: The camera begins a slow push-in toward the woman at the console. The round red bridge-warning lamp at frame-left starts to pulse, a slow red glow rising and falling on the wall and across her clear visor, and she turns her helmet and shoulders toward it while one glove stays resting on the console edge; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Gate is locked open. The bridge is still on purge control. 6-10 s: The turn finishes with her gaze fixed on the pulsing lamp and her shoulders squared to the wall, the lamp keeps pulsing and the push-in eases closer, while the spent core, the three lowered levers and the hatch window stay exactly in place. The only ambient sound is a deep industrial machinery hum through thick walls. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C74 — Yükleme köprüsü geri çekilir

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C74.png · referans (yükleme sırası): ref/9.KOPRU_v1.png
```

> Not: ÖNCELİKLİ ÖNİZLEME (plan §13: "K74 rigid bridge retract"). Replik yok, kadrajda kimse yok (zamir ve "no people" cümlesi yazılmaz, A08). Plan kare durumu: orta segment zaten hafifçe geri çekiliyor, uç kapaklar kapalı,
> aradaki boşluk ilk karede var ("hareket rijit geri çekilme"). Bu yüzden `exterior retracted panel` (son durum, geniş boşluk) yerine `exterior intact panel` alındı, dar boşluk metinle verilir;
> yoksa model sayfadaki geniş boşlukla başlar ve "boşluğu genişlet" hareketi okunmaz. Köprü ark'ın PORT yanında (FILM.md §3): ark ucu solda, foundry ucu sağda, acil soket foundry ucunun altında (C75-C84 önceden kurulur).
> Kamera sabit: rijit kayma kamera hareketiyle karışmasın; ilk vuruş hareketle başlar (segment zaten kayıyor). Cam esnemez, kırılmaz. Dış ses T13: klip sesi yok, yatak Y1.

### Görsel
```text
Reference 9 (bridge): take the rigid square graphite pressure tunnel with its reinforced glass sides and waist-high rails, the two end platforms and the small emergency tug socket below the foundry end from it, using the exterior intact panel. Exterior wide view on a 24 mm lens, the camera in open space about 40 m away, level with the loading bridge and looking straight at its side. The sealed square telescoping bridge runs across the frame: its ark-side end platform sits at frame-left, where the pale ivory hull of the ark curves away behind it, and its foundry-side end platform sits at frame-right against the black foundry control spine; both end hatches are closed. The centre tunnel section has already begun to slide toward the foundry housing at frame-right, and a narrow dark vacuum gap has opened between its left end and the ark-side end platform. Below the foundry end, one small round emergency tug socket with its short catwalk hangs under the bridge. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera stays locked off in the wide frame while the single rigid centre section of the bridge slides to the right into its foundry housing, the narrow gap beside the ark-side end platform beginning to widen. 3-7 s: The section keeps sliding rightward in one straight line at an even pace, the dark gap opening wider until stars and the blue light of the gas giant show through it, while the glass sides stay flat and unbroken and both end platforms with their closed hatches remain fixed. 7-10 s: The section slides the last stretch into the housing and eases to rest, leaving a wide vacuum gap between the two rigid end platforms. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C75 — Rhea karşıda kalır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C75.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/9.KOPRU_v1.png
```

> Not: Replik R75 (Rhea, ağız kadrajda, 1.5–3.0 s → birinci vuruş 0-3 s). Plan "foundry-side end platform seen through its closed hatch window: Rhea inside, vacuum gap and ark end beyond" geometrisi belirsiz;
> çözüm: kamera platformun içinde, ark'a bakan kapalı kapağa doğru; Rhea sağda ¾ profil, kapak penceresi solda ve pencereden boşluk + uzaktaki ark ucu görünür (yüz açık, dudak okunur, bakış boşluğa gider).
> Plan "plants one glove on the fixed hatch rim": temas hareketi olduğu için sol eldiven kare başında kapak çerçevesine hafifçe yaslıdır, video onu düz basar (geniş düz yüzey, rijit çerçeve; plan §7 ilkesi).
> Rhea sola baktığı için sağ çene yarası ¾'te kısmen görünür; yara tarifi kimlik tabanında birebir kalır. Köprü geri çekilmiş, uç kapaklar kapalı, askı boş (plan K75 devamlılık).

### Görsel
```text
Reference 2 (woman): take her face, braid and pearl suit from it, using the face close-up panel. Reference 9 (bridge): take the foundry-side end platform with its closed round-windowed hatch, rails, grated floor and reinforced glass sides from it, using the end platform panel. Medium shot on a 35 mm lens at eye level inside the foundry-side end platform of the retracted loading bridge, the camera looking along the platform toward its closed ark-facing hatch. One person is in the frame: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She stands at the right of the frame in three-quarter view with her head turned toward the hatch at frame-left, her chest harness empty and her left glove resting flat on the fixed rim of the hatch. The hatch is closed, its small round reinforced window level with her visor; through the window a short dark vacuum gap is visible and, far beyond it, the ark's end hatch and ivory hull. The light is cool blue light through the reinforced glass sides and amber guide lamps along the rails. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow push-in along the platform as she presses her left glove firmly flat against the fixed hatch rim and turns her gaze through the hatch window across the gap; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: The bridge is gone. 3-7 s: She leans a little of her weight onto the glove, her helmet tilting slightly toward the window as her eyes follow the dark gap out to the far ark end, the amber reflections of the rail lamps sliding across her visor as the camera moves closer. 7-10 s: The push-in carries the camera nearer to the hatch window and the distant ivory hull framed in it while she lets out a slow breath and her shoulders drop slightly. The only ambient sound is a thin pressurized tunnel hum with a faint creak of rigid metal. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C76 — Pilot terk etmeyi reddeder

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C76.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png
```

> Not: Replik R76 (Leon, ağız kadrajda, 1.5–4.5 s → birinci vuruş 0-5 s). Geometri: kamera kabin ekseninde, pilot koltuğunun sağında; Leon solda sağ profil, kanopi ve açık kapı sağda (13.KOMUTA: kanopi önde, pilot koltuğu solda).
> "Tug-access yönü" ark'ın sancak kıç servis bloğu (FILM.md §3 ve plan §5: tug portu sancakta) = Leon'un sağı = kamera tarafı; kask kanopiden kameraya doğru döner, dudak ve yüz açılır.
> Sol şakak yarası sağ profilde görünmez (kimlik tabanı birebir kaldı); 1.LEON `face close-up panel` yüzü taşır. B kolu aşağı ve mandallı (`lever B down panel`); kapı tamamen açık, kelepçe kolu kadrajda yok.
> Kısa kanopi manzarası: yalnız açık kapı ve yıldız alanı; ark kıç motorları ya da foundry yapıları çizilmez.

### Görsel
```text
Reference 1 (man): take his face, beard, ivory suit and clear helmet from it, using the face close-up panel. Reference 13 (command bridge): take the navy pilot seat, the console, the lowered silver clamp-release lever and the forward canopy from it, using the lever B down panel. Close shot on an 85 mm lens at eye level from the centre line of the cabin, the camera beside the pilot seat on its right. One person is in the frame: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits in the navy pilot seat at the left of the frame, seen in right profile with his gloved hands on the console controls and his helmet facing frame-right toward the broad forward canopy, where the exit gate stands fully open, its three rigid shutters drawn back around a plain starfield. The single broad silver clamp-release lever beside the pilot console is pulled down at its latched stop, low at the right edge of the frame. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera begins a slow push-in toward him as he makes one decisive turn of his helmet away from the canopy toward the side of the cabin where the tug-access route lies, bringing his face round to three-quarter view; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: Get to the emergency socket. I'm coming back. 5-10 s: The turn settles with his gaze set past the camera and his jaw tightening, his gloves staying on the console controls as the push-in eases closer, the silver lever staying down and the open gate staying in the canopy at frame-right. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C77 — Mühendis acil iskelede bekler

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C77.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/14.ISKELE_v1.png · ref/15.ARACLAR_v1.png
```

> Not: Replik R77 (Rhea, ağız kadrajda, 1.5–4.5 s → birinci vuruş 0-5 s). Plan "Wide" ama ağız kadrajda: dudak okunsun diye Rhea karede yüksekliğin üçte ikisini kaplar (kamera ~4 m), "wide" geniş tam boy olarak korundu.
> Tether: kemerden raydaki mühür bloğuna (gümüş manyetik blok) bağlı; sağ eldiven kare başında tether'ı zaten tutuyor, video yalnız gevşekliği alıp hattı geriyor (tek kısa çekiş, el-nesne yeni temas kurmaz).
> Plan "body stays anchored" → "boots stay planted" (BILINEN_TUZAKLAR §A: `body`). Tug henüz yanaşmadı (plan K77 devamlılık): soket boş, kelepçe açık. Askı boş. Dış ses T13: vakum, ses kaskın içinden; F8'de klip sesi yalnız replik penceresinde.
> Rhea ¾ sağa dönük: sağ çene yarası görünür.

### Görsel
```text
Reference 2 (woman): take her face, braid, pearl suit and empty chest harness from it, using the front full-body panel. Reference 14 (service catwalk): take the short rigid catwalk with its rails, the fixed magnetic boot plate, the tether anchor, the round tug docking socket with its open hinged collar clamp, the amber guide lamps and the heavy blast ribs from it, using the catwalk wide panel. Reference 15 (accessories): take the coiled navy safety tether with its rigid silver magnetic anchor block from it, using the tether panel. Wide full-figure shot on a 35 mm lens at eye level, the camera about 4 m from her along the exterior catwalk so that she fills two thirds of the frame height. One person is in the frame: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She stands outside at the centre-left of the frame in three-quarter view toward frame-right, her boots on the fixed magnetic boot plate and her chest harness empty; a navy safety tether runs from her belt back to its silver magnetic block fixed on the rail anchor at frame-left, and her right glove already grips the tether a short length from her belt, a gentle slack curve hanging between her hand and the anchor. At the end of the catwalk at frame-right the small round tug docking socket stands empty with its single broad hinged collar clamp open; heavy blast ribs rise on the far side of the catwalk, and open black space with stars lies beyond the rails. The light is amber battery guide lamps along the catwalk, cold starlight, and a distant orange furnace glow beyond the blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: The camera begins a slow glide along the catwalk toward her as her right glove draws back one short length along the tether, taking up the slack so that the line lifts and straightens between her hand and the rail anchor, her boots staying planted on the magnetic plate; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Socket ready. I can't hold this position forever. 5-10 s: The tether comes taut and steady with the silver block fixed on the rail anchor, and she turns her head toward the empty socket at the end of the catwalk while the amber guide lamps glow along the rails and the glide continues. The only ambient sound is close breathing inside a sealed helmet over a low, steady pressure tone. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C78 — Ark güvenli beklemeye alınır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C78.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/13.KOMUTA_v1.png · ref/15.ARACLAR_v1.png
```

> Not: Replik R78 (Leon, ağız kadrajda, 1.5–4.0 s → birinci vuruş 0-4 s; anahtar tıkı repliğin ardından, 4-7 s). FILM.md §4 referansından 10.CEKIRDEK çıkarıldı: çekirdek kontrol odasındaki yuvada, komutada yok (plan bu çekime R11 vermiş ama
> kare durumu "core absent from the bridge"; referans çekirdeği komuta köprüsüne çizdirir). Kamera kanopi tarafında, geriye (kıça) bakar: kabin sağı karede SOLA düşer, bilek bağlantısı yuvası solda, gümüş B kolu (aşağı, mandallı) sağ kenarda;
> Leon sağ koltukta değil, pilot koltuğunda (kabin solu = karenin sağı) ve yuvaya doğru döner: sol şakak yarası görünür. Plan "broad toggle": bilek bağlantısının geniş fiziksel anahtarı (15.ARACLAR `wrist-link panel`);
> eldiven kare başında anahtarın üstünde (temas kurulu), video yalnız çevirir. Gemi kendiliğinden yola çıkmaz (plan K78 devamlılık): çıkış rotası yüklü, station-keep seçili, hareket yok.

### Görsel
```text
Reference 1 (man): take his face, beard, ivory suit and clear helmet from it, using the face close-up panel. Reference 13 (command bridge): take the navy pilot seat, the console and the lowered silver clamp-release lever from it, using the lever B down panel. Reference 15 (accessories): take the unmarked ivory wrist-link with its broad physical toggle and cyan status light from it, using the wrist-link panel. Medium shot on a 50 mm lens at eye level, the camera facing aft from the canopy side of the ark's command bridge. One person is in the frame: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits in the navy pilot seat at the right of the frame, seen in three-quarter view from his front-left with his helmet turned toward frame-left, where the unmarked ivory wrist-link sits seated in its cradle on the console, its cyan status light steady; the fingers of his glove rest on the wrist-link's single broad physical toggle. The broad silver clamp-release lever beside the pilot console is pulled down at its latched stop at the right edge of the frame. The light is cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow push-in toward him as he keeps his gaze on the wrist-link's steady cyan light, his gloved fingers resting on its broad toggle; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: Ark on hold. Exit course stays armed. 4-7 s: His glove presses the broad toggle over with one firm short motion and the toggle seats in its new position, the cyan light staying steady and every other control staying fixed. 7-10 s: His glove eases away from the toggle and rests on the console edge beside the cradle as his shoulders settle and the push-in carries the camera a little closer to his visor. The only ambient sound is soft bridge ventilation and quiet, steady console electronics. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C79 — Pilot küçük gemisine döner

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C79.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/4.KOKPIT_v1.png · ref/6.ARK_v1.png
```

> Not: Replik R79 (Leon, ağız kadrajda, 1.5–3.0 s → birinci vuruş 0-3 s). FILM.md §4 referansından 5.FOUNDRY, 10.CEKIRDEK ve 15.ARACLAR çıkarıldı: kanopide yalnız ark gövde duvarı görünür (foundry kadrajda değil),
> çekirdek tug'da yok (plan "core absent"; referans onu çizdirir), yanaşma-bırakma anahtarı kokpitin kendi öğesi (4.KOKPIT `pilot side panel`), bilek bağlantısı eylemde yok.
> Kamera kokpitin arkasında, koltuk çizgisinde hafif sağda; Leon solda sağ ¾ arkadan, vizörden sağ yüz profili okunur (kokpitte Leon solda kuralı korunur; bu açıyla ağız profilde kalır, risk notu). Sağ koltuk boş.
> Tug hâlâ ark portunda (plan K79 devamlılık): kanopide ark gövde duvarı ve tug burun yakası ark'ın yuvarlak sancak portuna kilitli. Anahtar eldiven altında kare başında (temas kurulu), video yalnız çevirir; tug bu çekimde ayrılmaz (C80'in işi).

### Görsel
```text
Reference 1 (man): take his face, beard, ivory suit and clear helmet from it, using the side full-body panel. Reference 4 (cockpit): take the navy pilot seat, the low graphite console, the short paired controls, the broad unmarked docking-release toggle and the broad canopy with its two fixed graphite mullions from it, using the pilot side panel. Reference 6 (ark): take the ivory hull wall with its small round starboard maintenance port from it, using the stern panel. Wide view on a 24 mm lens at seated eye level, the camera at the rear of the tug cockpit, slightly right of centre between the seats and looking forward. One person is in the frame: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits in the navy pilot seat at the left of the frame, seen from behind and to his right so that his clear visor shows the right side of his face in profile, his helmet turned toward the console, his right glove resting on the broad unmarked docking-release toggle in front of him. The engineer's seat at the right of the frame is empty. Through the broad canopy the pale hull wall of the ark fills the forward view close ahead, its small round maintenance port at the centre with the tug's bow collar locked into it. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow push-in from the rear of the cockpit toward the pilot seat as he turns his helmet a little toward the console in profile; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: Not this time. 3-7 s: His right glove, already resting on the broad docking-release toggle, flips it over once with a short firm motion, and his shoulder shifts slightly with the effort. 7-10 s: His glove lifts away from the toggle and settles on the control stick beside it while the push-in carries the camera closer to his shoulder; the ark's hull stays fixed in the canopy ahead. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C80 — Tug ark'tan ayrılır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C80.png · referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/6.ARK_v1.png
```

> Not: Replik yok, kadrajda kimse yok (zamir ve "no people" cümlesi yazılmaz). Plan kare durumu: tug yakası zaten açılmış (kelepçe açık), ark sancak portundan ince bir boşluk, gövdeler bütün. Tug burnu sağda (3.KESTREL `side view panel`: burun sağda),
> ark gövde duvarı sağ üçte birde, port kıç yakınında (FILM.md §3 sayfa 6 `stern panel`). Plan "no stretching hoses" olumsuz çıkarıldı: kadrajda hortum yok, iki halka sert ve yuvarlak tarif edilir.
> Kamera sabit: rijit kayma kamera hareketiyle karışmasın. Boşluk tug uzunluğu kadar açılır, tug kadrajdan çıkmaz. Dış ses T13: klip sesi yok, yatak Y1. Gaz devi dış mekân ışığı cümlesinin içinde (ayrı gök cümlesi eklenmedi).

### Görsel
```text
Reference 3 (tug): take the compact tug's ivory wedge hull, graphite underside, narrow orange nose band, smoked-blue canopy, two rear thrusters and four radiator fins from it, using the side view panel. Reference 6 (ark): take the ivory hull wall with its small round tug maintenance port near the stern from it, using the stern panel. Side view on a 50 mm lens, the camera about 50 m away and level with the docking axis. The compact tug floats at the left of the frame with its nose pointing to frame-right, its round bow collar unlatched with the single broad hinged clamp swung open, and a thin dark gap separates the collar from the ark's small round starboard maintenance port, which sits in the pale ivory hull wall filling the right third of the frame. Both hulls are intact. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera stays locked off at the docking axis while the rigid tug begins to slide to the left, its open collar drawing clear of the ark's round maintenance port and the thin gap starting to widen. 3-7 s: The tug keeps drifting leftward in one straight line at a slow even pace, the gap opening to about the length of the tug's hull while both collar rings keep their round shape. 7-10 s: The tug glides the last stretch to the left with its nose still pointing at the ark, the wide gap between the two rings letting starlight and blue glow pass between them. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C81 — Köprünün altından kurtarma uçuşu

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C81.png · referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png
```

> Not: Replik yok, kadrajda kimse yok. Kare durumu planın kendisi: tug geri çekilmiş köprünün altında, acil soket önde (foundry kontrol omurgası yanı), ark arkada hareketsiz; plan devamlılığı gereği ark'ın iki gantri çenesi AÇIK ve gövdeden uzak yazıldı
> (5.FOUNDRY `bridge and socket panel` köprüyü sağlam gösterir; geri çekilmiş durum metinle verilir: orta segment foundry gövdesinde, iki uç platform arasında kısa vakum boşluğu, kapaklar kapalı).
> Hareket: kamera tug'u soldan sağa takip eder, tek yay; gemi geometrisi rijit. Tug köprünün altından geçer, sokete yaklaşır ama yanaşmaz (C84'ün işi). Dış ses T13: klip sesi yok, yatak Y1.

### Görsel
```text
Reference 3 (tug): take the compact tug's ivory wedge hull, orange nose band, smoked-blue canopy and rear thrusters from it, using the three-quarter panel. Reference 5 (station): take the black foundry control spine, the sealed loading bridge and the small round emergency tug socket below its foundry end from it, using the bridge and socket panel. Reference 6 (ark): take the ivory ark's port flank and its loading-bridge connection from it, using the port side panel. Wide view of the foundry's side on a 35 mm lens, the camera about 120 m away and level with the loading bridge. The black foundry control spine fills the right of the frame, with the small round emergency tug socket on its lower flank, and the sealed loading bridge extends to frame-left above it in its retracted state: its centre section is drawn into the foundry housing, and a short dark vacuum gap separates two rigid end platforms with closed hatches. The long ivory ark hangs motionless behind the bridge at frame-left, its two gantry clamp jaws open and clear of the hull. The small ivory tug floats below the bridge at the left-centre of the frame, its nose pointing to frame-right toward the socket. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a smooth lateral track to the right, following the small tug as it lifts away from its position below the retracted bridge and starts a single curved flight path toward the emergency socket. 3-7 s: The tug sweeps along the smooth arc beneath the bridge, the track keeping it in the left-centre of the frame while the foundry spine and the round socket slide steadily closer at frame-right; the ark, the bridge and the open clamp jaws keep their exact shapes. 7-10 s: The arc flattens as the tug nears the socket and its pace eases slightly, the round socket growing larger ahead of its nose as the track slows with it. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C82 — Güvenlik ateşinden geçer

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C82.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/4.KOKPIT_v1.png · ref/11.DRONE_v1.png
```

> Not: Replik R80 (Leon, ağız kadrajda, 1.5–4.0 s → birinci vuruş 0-4 s; atım ikinci vuruşta). Geometri C76 ile aynı mantık: kamera kabin ekseninde pilot koltuğunun sağında, Leon solda ¾ sağ önden, kanopi sağda; drone kanopinin sağ kenarında uzak, küçük (11.DRONE `drone front panel`:
> kırmızı şerit tug'a dönük). Plan "pulse passes outside the canopy without hitting it": atım cama değmeden dışından geçer, kokpit ve Leon sağlam (plan: yaralanma/kırılma yok); kare başında drone zaten orada, video onu eklemez.
> Eldiven kare başında kumanda kolunda (temas kurulu), video yalnız küçük bir giriş yapar. Tug serbest uçuşta (plan K82 devamlılık); kanopi arkasında gökte yalnız yıldız alanı, foundry yapıları çizilmez.
> Replikli ve sahne sesli klip: atım sesi kurguda; F8'de klip sesi yalnız replik penceresinde.

### Görsel
```text
Reference 1 (man): take his face, beard, ivory suit and clear helmet from it, using the face close-up panel. Reference 4 (cockpit): take the navy pilot seat, the short paired controls, the low graphite console and the broad canopy with its two fixed graphite mullions from it, using the pilot side panel. Reference 11 (drone): take the rigid graphite rectangular body with its single narrow horizontal red sensor strip and short forward emitter from it, using the drone front panel. Medium shot on a 50 mm lens at eye level from the centre line of the tug cockpit, the camera beside the pilot seat on its right. One person is in the frame: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits in the navy pilot seat at the left of the frame in three-quarter view from his right front, his right glove on the short control stick and his helmet turned toward the broad canopy at frame-right. Outside the canopy dark space with stars fills the glass, and at its far right edge a small distant graphite sentry drone floats with its red sensor strip turned toward the tug. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow push-in toward him as he looks out through the canopy at the distant sentry, its red sensor strip brightening; his lips move only for his own line, and he says in a low, dry adult man's voice, calm and guarded: Keep your head behind the blast rib. 4-7 s: From the drone at the right edge, one brief blue-white pulse streaks across the dark outside the canopy and passes beyond the glass, its light flickering over his clear visor and the console. 7-10 s: He makes one small restrained input on the control stick, the glove easing it a short distance, and the starfield beyond the canopy shifts a few degrees as the tug adjusts its course. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C83 — Rhea portu hazırlayıp korunur

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C83.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/14.ISKELE_v1.png · ref/15.ARACLAR_v1.png
```

> Not: Replik R81 (Rhea, ağız kadrajda, 1.5–3.0 s → birinci vuruş 0-3 s; anahtar çevrilir çevrilmez lambalar parlar, replik hemen ardından). Rhea ağır patlama kaburgasının arkasında, kaburganın kenarı sol ön planda omzunu örter (siper korunur);
> ¾ sağa dönük: sağ çene yarası görünür. Anahtar: soket gövdesindeki geniş, işaretsiz pil-güç anahtarı, eldiven kare başında üstünde (temas kurulu). Tether kemerden raydaki bloğa bağlı, gevşek. Askı boş; tug henüz yanaşmadı (plan K83 devamlılık), soket yakası açık,
> amber kılavuz lambalar sönük başlar, video parlatır. Doğrudan alev yok (14.ISKELE: kaburgalar korur). Dış ses T13: vakum, ses kaskın içinden; F8'de klip sesi yalnız replik penceresinde.

### Görsel
```text
Reference 2 (woman): take her face, braid, pearl suit and empty chest harness from it, using the face close-up panel. Reference 14 (service catwalk): take the round tug socket housing with its open hinged collar clamp, the amber battery guide lamps, the rails and the heavy blast ribs from it, using the socket close panel. Reference 15 (accessories): take the coiled navy safety tether with its rigid silver magnetic anchor block from it, using the tether panel. Medium shot on a 50 mm lens at eye level on the exterior catwalk. One person is in the frame: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She stands at the left of the frame in three-quarter view toward frame-right, sheltered behind a heavy fixed blast rib whose edge crosses the left foreground and partly covers her left shoulder; her chest harness is empty, and a navy safety tether runs from her belt back to its silver magnetic block fixed on the rail anchor behind her. Her right glove already rests on the broad unmarked battery-power toggle of the tug socket housing on the rail directly beside her at frame-right, the socket's single broad hinged collar clamp open and its amber guide lamps dim. The light is amber battery guide lamps along the catwalk, cold starlight, and a distant orange furnace glow beyond the blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera begins a slow push-in as her right glove flips the broad battery-power toggle over in one short motion and the amber guide lamps along the socket and rails brighten; her lips move only for her own line, and she says in a clear, quick adult woman's voice, precise and controlled: Emergency collar live. 3-7 s: The amber glow holds at its brighter level along the collar and the rails as her glove draws back from the toggle and she tucks her shoulder deeper behind the blast rib. 7-10 s: Her helmet leans a little further into the rib's cover while the push-in finishes closing on her, the tether staying anchored behind her. The only ambient sound is close breathing inside a sealed helmet over a low, steady pressure tone. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C84 — İkinci yanaşma yaklaşması

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C84.png · referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/14.ISKELE_v1.png
```

> Not: ÖNCELİKLİ ÖNİZLEME (plan §13: "K84/K85 ikinci docking"). Replik R82 (Leon, telsiz, kadraj dışı tug'dan): FILM.md §5 saniyesi 1.5 ama "Contact." temas anıyla anlam taşır; video promptunda ikinci vuruşa (4-8 s, boşluk kapanırken) yazıldı,
> son 1 s'ye düşmez. **FILM.md §5 R82 Saniye 1.5 → ~6.0 olmalı (Flow'dan ölçülür; dış klip, klip sesi yalnız replik penceresinde, T13).** Plan: tug soldan sağa tek yanaşma ekseninde, temas son vuruşta, kelepçe AÇIK kalır
> (kapama C85'in işi). Kadrajda kimse yok (Rhea siperde, kadraj dışı; zamir ve "no people" cümlesi yazılmaz). Dış mekân ışığı (soket dışı = DIŞ, Y1); iskele lambaları soketin yanında amber. Kamera sabit; hareket rijit kayma.

### Görsel
```text
Reference 3 (tug): take the compact tug's ivory wedge hull, graphite underside, narrow orange nose band, smoked-blue canopy and rear thrusters from it, using the side view panel. Reference 14 (service catwalk): take the small round emergency tug socket with its open hinged collar clamp, the short rigid catwalk with rails and the amber battery guide lamps from it, using the socket close panel. Side view on a 50 mm lens, the camera about 40 m away and level with the docking axis. The compact tug floats at the left of the frame with its nose pointing to frame-right, its round bow collar aligned with the foundry's small round emergency socket at the right of the frame, a short dark gap between the two rings and one broad hinged clamp standing open on the collar. Amber guide lamps glow along the short catwalk and rails beside the socket, and the black flank of the foundry rises behind it. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera stays locked off in side view while the rigid tug begins to slide to the right along the single docking axis, its bow collar closing on the socket ring. 4-8 s: The tug keeps moving rightward at a slow even pace until only a narrow dark strip remains between the two rings, and as the gap closes a low, dry adult man's voice, calm and guarded, softened by a light suit-radio filter, comes over the tug's radio, out of frame, and says: Contact. 8-10 s: The two collar rings meet and rest against each other, the hinged clamp still standing open while the amber guide lamps glow steadily along the rails. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini Omni 1.1 Flash 10 s ile hedefler. Omni'de başlangıç karesi yalnız Flow web'de; Omni süresi ve ses davranışı SMOKE P11 · P14 · P18'de ölçülür
> (`uretim_hatti/FLOW_GERCEKLERI.md` §1 · §9); ölçüm gelmeden videolar koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9. Veo 3.1'de klip 4/6/8 s'dir.
> **Replikli klipler (bu grupta C73 C75 C76 C77 C78 C79 C82 C83 C84):** SMOKE P18 sonucuna bağlı. Replik klipte yanlış ya da bozuk duyulursa o klibin sesi kurguda eklenir (timeline `ses` parçası).
> Dış (vakum) replikli klipler C77 · C83 · C84: klip sesi yalnız replik penceresinde (±0,5 s), kalan süre Y1/Y9 yatağı (FILM.md §6, T13).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kare üretimi için panel adı parantezde.
> **FILM.md §4 Referans sütunundan çıkarılanlar (gerekçe çekim Not'unda):** C78 → 10.CEKIRDEK · C79 → 5.FOUNDRY, 10.CEKIRDEK, 15.ARACLAR.
> Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C73 kare | `kare/C73.png` | Görsel | ref/2.RHEA_v1.png (`front full-body panel`) · ref/10.CEKIRDEK_v1.png (`core spent panel`) · ref/12.KONTROL_ODASI_v1.png (`levers down panel`; bu sırayla) | 2 | |
| 2 | C74 kare | `kare/C74.png` | Görsel | ref/9.KOPRU_v1.png (`exterior intact panel`) · **ÖNCELİKLİ ÖNİZLEME** | 2 | |
| 3 | C75 kare | `kare/C75.png` | Görsel | ref/2.RHEA_v1.png (`face close-up panel`) · ref/9.KOPRU_v1.png (`end platform panel`; bu sırayla) | 2 | |
| 4 | C76 kare | `kare/C76.png` | Görsel | ref/1.LEON_v1.png (`face close-up panel`) · ref/13.KOMUTA_v1.png (`lever B down panel`; bu sırayla) | 2 | |
| 5 | C77 kare | `kare/C77.png` | Görsel | ref/2.RHEA_v1.png (`front full-body panel`) · ref/14.ISKELE_v1.png (`catwalk wide panel`) · ref/15.ARACLAR_v1.png (`tether panel`; bu sırayla) | 2 | |
| 6 | C78 kare | `kare/C78.png` | Görsel | ref/1.LEON_v1.png (`face close-up panel`) · ref/13.KOMUTA_v1.png (`lever B down panel`) · ref/15.ARACLAR_v1.png (`wrist-link panel`; bu sırayla) | 2 | |
| 7 | C79 kare | `kare/C79.png` | Görsel | ref/1.LEON_v1.png (`side full-body panel`) · ref/4.KOKPIT_v1.png (`pilot side panel`) · ref/6.ARK_v1.png (`stern panel`; bu sırayla) | 2 | |
| 8 | C80 kare | `kare/C80.png` | Görsel | ref/3.KESTREL_v1.png (`side view panel`) · ref/6.ARK_v1.png (`stern panel`; bu sırayla) | 2 | |
| 9 | C81 kare | `kare/C81.png` | Görsel | ref/3.KESTREL_v1.png (`three-quarter panel`) · ref/5.FOUNDRY_v1.png (`bridge and socket panel`) · ref/6.ARK_v1.png (`port side panel`; bu sırayla) | 2 | |
| 10 | C82 kare | `kare/C82.png` | Görsel | ref/1.LEON_v1.png (`face close-up panel`) · ref/4.KOKPIT_v1.png (`pilot side panel`) · ref/11.DRONE_v1.png (`drone front panel`; bu sırayla) | 2 | |
| 11 | C83 kare | `kare/C83.png` | Görsel | ref/2.RHEA_v1.png (`face close-up panel`) · ref/14.ISKELE_v1.png (`socket close panel`) · ref/15.ARACLAR_v1.png (`tether panel`; bu sırayla) | 2 | |
| 12 | C84 kare | `kare/C84.png` | Görsel | ref/3.KESTREL_v1.png (`side view panel`) · ref/14.ISKELE_v1.png (`socket close panel`; bu sırayla) · **ÖNCELİKLİ ÖNİZLEME** | 2 | |
| 13 | C73 | `ham/C73_d1.mp4` | Frames to Video | kare/C73.png | 2 | |
| 14 | C74 | `ham/C74_d1.mp4` | Frames to Video | kare/C74.png · **ÖNCELİKLİ ÖNİZLEME: önce üretilir** | 2 | |
| 15 | C75 | `ham/C75_d1.mp4` | Frames to Video | kare/C75.png | 2 | |
| 16 | C76 | `ham/C76_d1.mp4` | Frames to Video | kare/C76.png | 2 | |
| 17 | C77 | `ham/C77_d1.mp4` | Frames to Video | kare/C77.png | 2 | |
| 18 | C78 | `ham/C78_d1.mp4` | Frames to Video | kare/C78.png | 2 | |
| 19 | C79 | `ham/C79_d1.mp4` | Frames to Video | kare/C79.png | 2 | |
| 20 | C80 | `ham/C80_d1.mp4` | Frames to Video | kare/C80.png | 2 | |
| 21 | C81 | `ham/C81_d1.mp4` | Frames to Video | kare/C81.png | 2 | |
| 22 | C82 | `ham/C82_d1.mp4` | Frames to Video | kare/C82.png | 2 | |
| 23 | C83 | `ham/C83_d1.mp4` | Frames to Video | kare/C83.png | 2 | |
| 24 | C84 | `ham/C84_d1.mp4` | Frames to Video | kare/C84.png · **ÖNCELİKLİ ÖNİZLEME: önce üretilir** | 2 | |

> Öncelikli önizleme (plan §13 "Ön üretim denemesi"): C74 (rijit köprü geri çekilmesi) ve C84 (ikinci docking yaklaşması; C85 G08'de) tüm 96 çekimden önce sınanır. Bir hareket kararsız çıkarsa daha basit başlangıç karesi düzenlenir
> (boşluk daha geniş, aralık daha kısa), hareket eklenmez. Kare tarafında bu grubun riskli üçü: C75 (ark ucu kapak penceresinden görünür mü), C79 (Leon sağ ¾ arkadan, ağız profilde), C77 (geniş planda dudak).
