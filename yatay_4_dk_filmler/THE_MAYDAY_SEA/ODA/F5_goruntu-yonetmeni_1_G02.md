# 🖼️ THE_MAYDAY_SEA — Prompt grubu G02 (çekimler C09–C16)

> Yazan: goruntu-yonetmeni (tur 1). Denetleyen: devamlilik · teknik-danisman.
> Kaynak: `ODA/SAHIP_PLANI.md` §6 K09-K16 + §8 tutarlılık listesi. Bu dosya yeniden tasarım değil, biçim çevirisidir:
> kompozisyon, olay, ışık, tasarım ve hareket yönü planın kendisi; cümleler olabildiğince planın İngilizcesi.
> Prompt gövdesine çekim kodu, anahtar kare kodu, "Clip n of N", başlık satırı, referans kodu
> YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. Olumsuz yasak listesi yazılmaz. ≤4.300 karakter.
> Zincir yok (plan zincir kurmaz); her çekim kendi başlangıç karesiyle Frames to Video. Referanslar yalnız kare üretiminde
> kullanılır (Frames to Video'ya referans eklenmez); `EKLE` satırı başlangıç karesini ve karenin referanslarını taşır.
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun
> başında `Reference <No> (<rol>): …` diye adlandırılır. Her video promptu 10 s'yi 2-4 vuruşa böler (0'da başlar, 10'da biter,
> boşluksuz, vuruş ≥2 s, son vuruş donmaz; ilk vuruş hareketle başlar).
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** FILM.md §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun
> sonunda birebir; MEKÂN IŞIĞI cümlesi her görsel promptta (ilk harfi büyük, kelimeler FILM.md §3'teki gibi); ORTAM SESİ cümlesi
> o mekânın her video promptunda birebir (ortak görünümden hemen önce). Bu filmde bütün replikler model sesi: replik video
> promptuna birebir `says: <line>` biçiminde yazılır (SABLON; tırnaklı biçim SMOKE P9'a kadar yedek), konuşanın sesi ve kaynağı
> tarif edilir, replik vuruşun SON cümlesidir (sonraki vuruş etiketi repliğin bittiğini gösterir).
> Çıkarılan plan kalıpları: "Create one film still, not a reference sheet or collage" (yerine `Render one single continuous scene:`),
> "Animate the uploaded scene still as the first frame", "10 seconds / 16:9" etiketi, "Preserve the referenced face, suit, vessel…"
> genel cümlesi, "No cuts, new characters, written text or subtitles" ve "No dialogue or music…All spoken lines will be added in the edit"
> kuyruğu, "Audio:" satırları (ses: FILM.md §6 yatak + §3 ORTAM SESİ), olumsuz kalıplar ("No head, face or body" · "No branching tentacles or
> humanoid shape" · "No giant contraction or opening mouth" · "No creature emerges") → pozitif tarif.
> Kelime güvenliği (BILINEN_TUZAKLAR §A): `body` sözcüğü ve türevleri hiçbir promptta geçmez; `tentacle` geçmez (yerine tek kordon / şerit).
> **Referans panelleri (FILM.md §3):** 1.MARA `head-and-shoulders portrait panel` · 7.GOZLEM_ODASI, 6.KORIDOR, 4.OKYANUS tek görünüm ·
> 8.AKSESUARLAR `left object` (alıcı) · 9.CANLI_SU `left panel` (zar ve kılcal ağ) · `centre panel` (duvara tırmanan şerit). Çekim başına her referanstan
> yalnız TEK panel ya da nesne anılır (C16 iki panel anar: şerit ve zar aynı çekimde gerekli).
> **Kimlik cümlesi (C13; G01/G03 aynı kelimelerle yazar):** `in an ivory-white pressure suit with dark navy shoulder armor and a closed round ivory
> helmet with a completely clear visor`; yaş/ten/saç yığını yalnız referans sayfasında (BILINEN_TUZAKLAR §A son satır).
> **Dış uzay gök cümlesi (C15; T18):** `The ocean hangs in deep black space with sparse stars.`

---

## C09 — Camın dışında boş kask

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası): ref/7.GOZLEM_ODASI_v1.png
```

> Not: Kaskın içi boş kalmalı (baş/yüz üretilmesin); replik yok. Plan "No head, face or body" olumsuzu pozitife çevrildi ("hollow, dark inside…
> only dark water behind the visor"). Kask 7.GOZLEM_ODASI'ndaki terk edilmiş kaskla aynı (fildişi, lacivert kenar); Mara'nın kendi kapalı
> kaskı bu çekimde yok. Kask soldan merkeze sürüklenir: karede sol üçte birde. Kabarcıklar planın videosunda "bir iz"; karede de var (video karede
> olmayan nesne istemesin). Camın sağ kenarında amber tavan lambası yansıması mekân ışığını (amber · cyan) kadrajda taşır.

### Görsel
```text
Reference 7 (observation room): take the reinforced window with its black vertical frame, the dark blue water beyond the glass and the abandoned ivory helmet from it. Render one single continuous scene: a close view through the observation room's reinforced window on a 50 mm lens at eye level. An old ivory helmet with a dark navy rim floats in the dark blue water beyond the glass in the left third of the frame, its scratched clear visor angled toward the camera so that the hollow, dark inside of the helmet is plainly visible, with only dark water behind the visor; a few tiny bubbles rise beside it. The window's black vertical edge runs along frame-right, with a few pale mineral streaks on the glass and a faint amber reflection of the room's ceiling lamp. Far below, at the bottom of the frame, the faint silhouette of an old ship lies in the deep water. Faint amber emergency lamps from above, cool cyan light from the wet floor and the window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: The camera stays locked off at the window while the old helmet begins to drift slowly out of the left third of the frame through the dark blue water, turning by only a degree or two as the tiny bubbles beside it rise in a thin trail. 3-7 s: The drift carries the helmet toward the center of the frame, its rigid shell rotating only a few degrees so that the scratched visor keeps facing the camera and the hollow dark inside stays readable. 7-10 s: The helmet reaches the center of the frame and keeps gliding on slowly with one last slight turn, the bubble trail thinning out behind it, while the window's black edge and the ship silhouette below stay in place. The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C10 — Su, tabanla bağını koruyarak duvara tırmanır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C10.png · referans (yükleme sırası): ref/6.KORIDOR_v1.png · ref/9.CANLI_SU_v1.png
```

> Not: ÖNCELİKLİ ÖNİZLEME (plan §8: "K10'da tek su şeridi duvara tırmanmalı"). Şerit ilk karede zaten duvarda (plan: "su şeridi zaten yukarıdadır");
> videoda yapılan tek şey biraz daha yükselmek. Plan olumsuzu ("No branching tentacles or humanoid shape") pozitife çevrildi: tek sürekli kordon,
> yuvarlak sabit çap. İç mekânda normal yerçekimi: ızgara zemin ve korkuluk desteği aşağı yönünü gösterir; ihlal yalnız şeridin kendisi. İri dalga yok.
> Replik yok; kimse kadrajda değil.

### Görsel
```text
Reference 6 (corridor): take the dark graphite wall, the level grated floor, the handrail support and the shallow dark teal puddle at the right floor edge from it. Reference 9 (living water): take the glossy dark teal ribbon of water climbing a scratched vertical metal wall from it, using the centre panel. Render one single continuous scene: a low close view on a 35 mm lens, the camera 30 cm above the floor, looking across the corridor at its right-hand graphite wall. The wall rises through the upper two thirds of the frame with a fixed handrail support jutting from it near the top, and the level floor grate fills the bottom foreground, so it is plain which way is down. The shallow dark teal puddle lies along the foot of the wall, and from it one smooth, thick, glossy dark teal liquid ribbon already climbs a short distance up the wall, to about a third of the frame height: one continuous cord with round wet edges and a constant rounded diameter, its base visibly merging into the puddle. Cool cyan reflections run along its wet surface. Faint amber emergency lamps from above, cool cyan light from the wet floor and the window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: The camera stays low and locked off; the single dark teal ribbon begins to creep upward along the vertical wall, its glossy rounded edge advancing slowly while its base stays visibly joined to the puddle on the floor. 3-7 s: The ribbon climbs a further short distance up the wall as one continuous cord of constant rounded diameter, the puddle at its base rippling softly as it feeds the climb. 7-10 s: The ribbon creeps a little higher at a slowing pace, still one smooth cord joined to the puddle, cool cyan reflections sliding along its wet surface, while the floor grate, the handrail support and the wall stay fixed. The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C11 — Pencerenin altında batık gemi filosu

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C11.png · referans (yükleme sırası): ref/4.OKYANUS_v1.png · ref/7.GOZLEM_ODASI_v1.png
```

> Not: Replik R09: AI, kadraj dışı, oda alıcısından, 4.0–6.5 s (vuruş 4-8 s içinde). Hiçbir gemi Mara'nın kapsülüne benzemez (kapsül kanatsız,
> tekne biçimli, turuncu burun şeritli): plandaki "small white shuttle", kapsülden ayırmak için kısa süpürme kanatlı yazıldı (tek bilinçli ek).
> Keşif gövdesi C16'da aynı sözcüklerle tekrar tarif edilir (corroded narrow survey hull · dark canopy · small broken antenna housing); plan
> C16←C11 kare bağımlılığı bu yüzden kaldırıldı. Tilt'in mantığı: karede pencerenin üst kısmı ve yakın enkazlar; konsol kenarı altta, tilt'te yükselir.
> Gövdeler çökmez, yakınlaşmaz; yalnız asılı parçacıklar sürüklenir.

### Görsel
```text
Reference 4 (ocean): take the dark ocean water, the style of the old wrecks and the black containment-frame edge from it. Reference 7 (observation room): take the broad reinforced window, the low wet console and the room's amber ceiling light from it. Render one single continuous scene: a wide view from inside the observation room on a 24 mm lens at eye level, the camera facing the broad reinforced window, the upper part of the pane filling the frame and the low console edge showing along the bottom. The room is empty. The dark water beyond the glass holds wrecks at separate depths, each with its own shape: a corroded narrow survey hull with a dark canopy and a small broken antenna housing at mid-depth, a broad broken freight pod deeper at frame-right, and a small white shuttle with short swept wings closest to the glass at frame-left. Dozens of small hull silhouettes recede in the water below them, and far down, seen through the translucent ocean, one straight black containment-frame edge. Faint amber emergency lamps from above, cool cyan light from the wet floor and the window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-4 s: The camera starts a slow downward tilt from the near wrecks, the small white shuttle and the corroded survey hull sliding up out of the frame while the hulls below them rise into view. 4-8 s: The tilt continues, the broad freight pod and dozens of smaller hull silhouettes opening up beneath them as the scale of the fleet widens, and a calm, plain adult male voice from the room's receiver, out of frame, says: Those are ships. Dozens of them. 8-10 s: The tilt carries down to the deepest silhouettes and the black containment-frame edge far below, the console edge rising into the bottom of the frame; every hull stays rigid and separate and only small suspended particles drift in the water. The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C12 — Alıcıdan Mara'nın cümlesi gelir

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C12.png · referans (yükleme sırası): ref/7.GOZLEM_ODASI_v1.png · ref/8.AKSESUARLAR_v1.png
```

> Not: Replik R10 (OCEAN = Mara'nın C02 cümlesi), 4.5–6.5 s, alıcıdan, kadın sesi, hafif telsiz filtresi; kadrajda kimse yok. Omni aynı sesi başka klipte
> garanti etmez: SMOKE P18 ölçer, tutmazsa kurguda C02 kaydı yedek (NOTLAR KARARLAR). Alıcı bağımsız güçlü (ana verici enerjisiz kalır); kumandalarda yazı yok
> (düz, işaretsiz). Gösterge karede loş yanar, videoda parlar. Şerit 9.CANLI_SU'dan değil metinden gelir (çekimin referansı FILM.md §4'te 7 · 8); biçim
> değiştirmeden küçük dalgacık yapar.

### Görsel
```text
Reference 7 (observation room): take the wet graphite console, the cool blue water light of the window and the dim cyan lamp from it. Reference 8 (accessories): take the small battery-powered receiver with its matte-black casing, silver speaker grille, single cyan indicator and broad physical toggle from it, using the left object. Render one single continuous scene: a tight insert on a 100 mm lens with shallow depth of field, the camera 40 cm in front of the receiver and slightly above it, the receiver centered in the frame on the observation-room console. Its matte-black casing, silver speaker grille, single cyan indicator and broad physical toggle are sharp, with plain, unmarked controls; the indicator glows dimly. A narrow dark teal liquid ribbon lies along the console's rear edge behind the receiver, its glossy surface carrying a blue reflection of the water in the window, which glows as a soft blur in the background. The receiver is intact and powered on its own. Faint amber emergency lamps from above, cool cyan light from the wet floor and the window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-4 s: A small slow push begins toward the speaker grille while the single cyan indicator starts to brighten steadily, as if the receiver were picking up a signal. 4-7 s: The push continues and the indicator glows brighter; the casing and the toggle stay fixed while the thin teal ribbon along the rear edge makes one small ripple that keeps its shape, and from the speaker grille a calm adult woman's voice with a light radio filter says: Rescue vessel. I hear you. 7-10 s: The push eases closer to the grille, the indicator glowing at its brightest and the ribbon's ripple fading along its length. The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C13 — Mara sesini tanır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C13.png · referans (yükleme sırası): ref/1.MARA_v1.png · ref/7.GOZLEM_ODASI_v1.png
```

> Not: Ağız kadrajda replik (R11), 1.5 s, 5.0–6.5 s (vuruş 3-7 s içinde); dudak yalnız kendi cümlesinde oynar. Yara sağ elmacıkta: Mara karenin solunda, burnu
> kadrajın sağına doğru ¾ dönük olduğunda kamera onun sağ yanağını görür. Açı C08'den farklı (¾ profil → ön, soldan sağa küçük yay; plan: benzer yakın planlar
> üst üste gelmez). Yüz 1.MARA portre panelinden; çekim ¾ profil istiyor, 1.MARA sayfasına ¾ profil paneli eklenirse (FILM.md §3 izin veriyor) panel adı buraya yazılır.
> Eller kadraj altında; vizör berrak.

### Görsel
```text
Reference 1 (woman): take her face, her grey eyes, the small pale scar on her right cheekbone, her ivory pressure suit and her closed round ivory helmet with the completely clear visor from it, using the head-and-shoulders portrait panel. Reference 7 (observation room): take the broad reinforced window, the dark console edge and the amber ceiling light from it. Render one single continuous scene: a medium close-up on an 85 mm lens at eye level, a three-quarter profile of the woman standing in the observation room at the left of the frame, in an ivory-white pressure suit with dark navy shoulder armor and a closed round ivory helmet with a completely clear visor. She is turned three-quarters toward frame-right, so her right cheekbone with its small pale scar and her grey eyes show plainly through the clear visor; her eyes are directed at the receiver out of frame at frame-right, and her mouth is closed. Behind her the broad window carries a soft cyan water reflection; along the bottom edge a thin dark liquid line runs beside the console. Her hands are below the frame. A faint amber ceiling light separates the helmet from the background. Faint amber emergency lamps from above, cool cyan light from the wet floor and the window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: A slow, small camera arc begins to move to the right around her, starting from the three-quarter angle, while she stays planted with her eyes fixed on the receiver out of frame. 3-7 s: The arc carries the camera toward a clearer front view while her eyes widen slightly and her breathing catches once; her lips move only for her own line as she says: That's my voice. 7-10 s: The arc finishes at a nearly frontal angle as she draws a slow, shallow breath, her expression subtle, her face unchanged in identity and her eyes still on the receiver. The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C14 — Okyanusun alt yüzeyinde damar benzeri ağ

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C14.png · referans (yükleme sırası): ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png
```

> Not: ÖNCELİKLİ ÖNİZLEME (plan §8: "K14'te ağ suyla aynı hacimde okunmalı"). Okunurluk için derinlik ipucu eklendi: yakındaki çizgiler parlak, derindekiler silik,
> ağ aynı su hacminin içinde. 4.OKYANUS sayfasında alt görünüş paneli yok; ağ dokusu 9.CANLI_SU sol panelinden, kavisli alt yüz biçimi 4.OKYANUS metninden geliyor.
> 4.OKYANUS'a alt görünüş (su altı zar) paneli eklenirse (FILM.md §3) bu çekim ona bağlanabilir. Plan olumsuzu ("No separate animal, face, eye or mouth" · "No creature
> emerges") pozitife çevrildi; ışık atımı video boyunca tek geniş daldan yürür, ayrı biçim doğmaz. Replik yok.

### Görsel
```text
Reference 4 (ocean): take the dark teal seawater, the thick translucent curved hanging underside and the straight black containment frame beams from it. Reference 9 (living water): take the broad translucent membrane with its fixed branching network of faint cyan-gold capillary lines from it, using the left panel. Render one single continuous scene: a wide underwater view on a 24 mm lens, the camera inside the dark teal water just above the ocean's translucent curved underside, looking along it. A broad continuous membrane curves away across the lower two thirds of the frame, carrying a fixed, branching network of faint cyan-gold capillary lines over an immense area; seen through the clear water, the lines glow brighter where they lie closer and fainter where they lie deeper, so the network sits inside the same water volume. Small old wrecks lie caught against that same network. In the far background one straight black containment beam crosses the frame, and beyond the water's curved edge deep space with sparse stars is visible. Soft cyan-gold glow from the capillary network, deep teal falloff. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: The camera begins a slow lateral track from left to right along the translucent underside, the small wrecks nearer the lens sliding past faster than the network behind them. 3-7 s: The track continues and parallax opens more of the branching capillary network and more small wrecks caught in it to the right, while a soft cyan-gold pulse of light starts in one broad branch at the left and travels along it. 7-10 s: The pulse runs on through the finer branches toward the right and fades as the track slows, while the membrane, the far black beam and the curved edge of the water keep their shape. The only ambient sound is a deep, slow waterborne resonance with no rhythm. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C15 — Tek ışık atımı bütün okyanusu geçer

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C15.png · referans (yükleme sırası): ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png
```

> Not: Replik R12: AI, kadraj dışı, 4.0–7.5 s (vuruş 4-8 s içinde, replik 3.5 s). Kapsül istasyonun kuru, sağa bakan portuna yanaşık (burnu sola, istasyona dönük),
> kadrajda küçük bir nokta; atım soldan sağa ve sağ kenarda istasyonun yanında söner. Plan olumsuzu ("No giant contraction or opening mouth") pozitife çevrildi:
> oval dış çizgi, üç çerçeve, istasyon ve kapsül aynı yer ve biçimde kalır. Dış gök cümlesi G01/G03'teki dış çekimlerle aynı olmalı: "The ocean hangs in deep black space
> with sparse stars." Kimse kadrajda değil.

### Görsel
```text
Reference 4 (ocean): take the flattened oval ocean, its three black rectangular containment frames, the thin cyan field boundary, the wrecks below the surface and the half-submerged graphite station at the right rim from it. Reference 9 (living water): take the branching cyan-gold capillary network from it, using the left panel. Render one single continuous scene: an extreme wide exterior on a 14 mm lens, the camera far from the ocean and level with it. The flattened oval ocean fills the central two thirds of the frame inside three rigid black rectangular containment frames at separate depths, a thin continuous cyan field boundary outlining the water. Beneath the rippled surface the immense branching cyan-gold network is faintly visible throughout the whole water volume, and old wrecks lie below the surface. The graphite research station sits fixed on the right rim with its lower half in the water, and the ivory rescue pod is docked to its dry right-facing port as a tiny speck, its nose pointing left toward the station. The ocean hangs in deep black space with sparse stars. Cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-4 s: The camera stays locked at a great distance; at the ocean's left edge a broad, gradual cyan-gold glow begins to rise in the network beneath the rippled surface. 4-8 s: The glow becomes one wide, slow band of cyan-gold light that moves rightward through the whole branching network, brightening each line as it passes while the surface ripples stay small, and a calm, plain adult male voice over the comms channel, out of frame, says: No separate organism. The ocean itself is alive. 8-10 s: The band of light reaches the right side of the ocean beside the station and the docked pod and fades there, the network dimming behind it, while the oval outline, the three frames, the station and the pod keep their exact shapes and places. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C16 — Canlı su eski geminin antenine bağlanır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C16.png · referans (yükleme sırası): ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png
```

> Not: Replik R13: AI, kadraj dışı, 4.0–7.0 s (vuruş 3-7 s içinde). Plan kaynak kare bağımlılığı (C11) kaldırıldı: keşif gövdesi C11'de aynı sözcüklerle
> tarif ediliyor, tasarım metinle taşınır (THE_PLANET_THIEF C08 dersi). Mekanik onarım/dönüşüm yok: enkaz ve anten sabit, yalnız ışık atımı tek kordonda
> yürür. Kordon karede zaten bağlı (video bağlanmayı yapmaz, atımı yürütür). Beden, yüz, ayrı canavar yok. Yeni mitoloji açıklaması eklenmez.

### Görsel
```text
Reference 4 (ocean): take the dark teal ocean water and the style of the old corroded wrecks from it. Reference 9 (living water): take the broad translucent membrane with its cyan-gold capillary lines and the single glossy liquid cord from it, using the left and centre panels. Render one single continuous scene: a close underwater view on a 35 mm lens, the camera about 6 m from the wreck at the level of its hull, looking slightly down at its stern. One old corroded survey spacecraft with a narrow rigid hull, a dark canopy and a small broken antenna housing lies trapped in the dark teal water at the right of the frame. At frame-left a broad membrane carries a fine cyan-gold capillary network, and from it one single coherent glossy liquid cord crosses the water to the wreck, already attached to the antenna housing and to the communications compartment beneath it. The rest of the capillary network recedes into the soft teal distance, and sparse particles hang in the water. Soft cyan-gold glow from the capillary network, deep teal falloff. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: The camera begins a slow push toward the point where the single glossy cord meets the wreck's antenna housing and communications compartment, sparse particles drifting through the water. 3-7 s: The push continues and a faint cyan-gold pulse of light starts at the membrane and travels along the one cord toward the old housing, and a calm, plain adult male voice over the comms channel, out of frame, says: It has been using their calls as bait. 7-10 s: The pulse reaches the antenna housing and sinks into the compartment as a soft glow while the push closes in slightly more, the hull, the canopy and the antenna housing staying exactly as they are. The only ambient sound is a deep, slow waterborne resonance with no rhythm. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler klipten gelir; FILM.md başlığı) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Mod ↔ model:** plan Gemini Omni Flash 1.1 ile 10 s hedefler (`ODA/SAHIP_PLANI.md` §3). Omni'de başlangıç karesi yalnız Flow web'de; Omni süresi ve ses davranışı SMOKE P11 · P14 · P18'de ölçülür
> (`uretim_hatti/FLOW_GERCEKLERI.md` §1 · §9). Veo 3.1'de klip 4/6/8 s'dir; 10 s yolu ölçülene kadar videolar koşulmaz.
> **Replikli klipler (bu grupta C11 · C12 · C13 · C15 · C16):** SMOKE P18 sonucuna bağlı. Replik klipte yanlış ya da bozuk duyulursa o klibin sesi kurguda eklenir (timeline `ses` parçası); C12 için C02 kaydı yedektir (NOTLAR KARARLAR).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kare üretimi için panel notu parantezde.
> Sıra, bu grup içindedir; birleştirmede yeniden numaralanır.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C09 kare | `kare/C09.png` | Görsel | ref/7.GOZLEM_ODASI_v1.png | 2 | |
| 2 | C10 kare | `kare/C10.png` | Görsel | ref/6.KORIDOR_v1.png · ref/9.CANLI_SU_v1.png (orta panel; bu sırayla) · **ÖNCELİKLİ ÖNİZLEME: plan §8 zor plan** | 2 | |
| 3 | C11 kare | `kare/C11.png` | Görsel | ref/4.OKYANUS_v1.png · ref/7.GOZLEM_ODASI_v1.png (bu sırayla) | 2 | |
| 4 | C12 kare | `kare/C12.png` | Görsel | ref/7.GOZLEM_ODASI_v1.png · ref/8.AKSESUARLAR_v1.png (sol nesne; bu sırayla) | 2 | |
| 5 | C13 kare | `kare/C13.png` | Görsel | ref/1.MARA_v1.png (baş-omuz portre paneli) · ref/7.GOZLEM_ODASI_v1.png (bu sırayla) | 2 | |
| 6 | C14 kare | `kare/C14.png` | Görsel | ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png (sol panel; bu sırayla) · **ÖNCELİKLİ ÖNİZLEME: plan §8 zor plan** | 2 | |
| 7 | C15 kare | `kare/C15.png` | Görsel | ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png (sol panel; bu sırayla) | 2 | |
| 8 | C16 kare | `kare/C16.png` | Görsel | ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png (sol ve orta panel; bu sırayla) | 2 | |
| 9 | C09 | `ham/C09_d1.mp4` | Frames to Video | kare/C09.png | 2 | |
| 10 | C10 | `ham/C10_d1.mp4` | Frames to Video | kare/C10.png · **ÖNCELİKLİ ÖNİZLEME: önce üretilir** | 2 | |
| 11 | C11 | `ham/C11_d1.mp4` | Frames to Video | kare/C11.png | 2 | |
| 12 | C12 | `ham/C12_d1.mp4` | Frames to Video | kare/C12.png | 2 | |
| 13 | C13 | `ham/C13_d1.mp4` | Frames to Video | kare/C13.png | 2 | |
| 14 | C14 | `ham/C14_d1.mp4` | Frames to Video | kare/C14.png · **ÖNCELİKLİ ÖNİZLEME: önce üretilir** | 2 | |
| 15 | C15 | `ham/C15_d1.mp4` | Frames to Video | kare/C15.png | 2 | |
| 16 | C16 | `ham/C16_d1.mp4` | Frames to Video | kare/C16.png | 2 | |

> Öncelikli önizleme (plan §8 "Önce dört zor planı dene"): C10 ve C14 bu grupta; (C01 ve C21 G01/G03'te) tüm 24 çekimden önce sınanır. Bir hareket kararsız çıkarsa daha basit başlangıç karesi düzenlenir (şerit zaten yukarıda · ağ zaten görünür), hareket eklenmez.
