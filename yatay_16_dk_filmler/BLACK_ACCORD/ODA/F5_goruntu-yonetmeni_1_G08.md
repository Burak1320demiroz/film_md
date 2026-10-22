# 🖼️ BLACK_ACCORD — Prompt grubu G08 (çekimler C85–C96 · bölüm B8 ASLIYLA AYNI) · tur 1

> Yazan: goruntu-yonetmeni (faz 5, tur 1). Kaynak: `BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md` (sahip planı; "plandan asla dışarı çıkma") + `NOTLAR.md` KARARLAR (18.10.2026) + `ODA/F5_fable_birlestirme_1_G01.md` film içi kararlar.
> **Plan C85-C96 için promptsuzdur;** yalnız plan malzemesi kullanıldı: planın çekim cümlesi · A01-A13 İngilizce cümleleri (FILM §3 KİMLİK CÜMLELERİ, kadrajdaki parça birebir) · sabit düzen · nesne durumu · G01 örneği (C07-C12) · ROL SÖZLÜĞÜ · MEKÂN IŞIĞI · ORTAM SESİ · SES KİMLİĞİ.
> **Başlangıç durumu (plan "Görsel promptlar … başlangıç durumunu da tutar"):** C85'te Nem, Vekh, Ishra, Silex ve Orun alıcıları çıkmış (plan C61/C64/C67/C68/C69), Nith'inki takılı; blaster masada (C68); K1 masanın merkezinde, cyan yayın ışığı (C78); K2 K1'in yanında (C82). Bu yüzden **alıcı cümlesi** ("rests at her right temple" vb.) bu grupta yazılmaz; yerine "right temple is bare" / "external socket … is empty" (A12 nesne cümlesi kelimeleriyle) yazılır. Diğer kimlik cümleleri birebir. K1'in "pale amber triangular light"ı plan nesne durumu gereği "now glows cyan" olur. Vekh'in blasterli zırh cümlesi (kılıf kalçada) bu grupta yazılmaz: silah masadadır, kılıf cümlesi çelişirdi → kalça görünmeyen zırh cümlesi.
> **Ortak görünüm cümlesi** her Görsel'in sonunda; video promptlarına eklenmez (plan yalnız Görsel'de; NOTLAR KARARLAR). Model sesi AÇIK: replikler `<ses cümlesi>: <line>`. Kod / başlık / "Clip n of N" yok. Her blok ≤4.300 karakter.
> **Model sesi dağılımı (FILM §5):** C85 R156 Nem · C86 R158 Vekh · C87 R159 Ishra · C88 R160+R161 Silex · C89 R162+R163 Orun · C92 R164 Nith · C93 R166 Ishra · C94 R168 Silex · C95 R170 Vekh. Kurguda (kadraj dışı, videoda üretilmez; kadrajdaki kişinin ağzı kapalı): R157 Silex (C85) · R165 Nem (C92) · R167 Nem (C93) · R169 Nem (C94) · R171 Nem VO (C96). C90 · C91: söz yok.
> **Şiddet kelimeli model sesi:** C89 "weapons" · C95 "fire" (BT §A, red riski) — red gelirse yalnız o replik kayda geçer, metin değişmez.

---

## C85 — Dört filoya

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C85.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Geniş / yeni masa düzeni. Nith etkisiz biçimde arka plandadır. Nem merkezde; dört elçi kendi kaydına döner." Dört elçi arkadan/profilden küçük (plan: "öteki kişilerin arkaları veya flu siluetleri"; ≤3 referans). "Kendi kaydına" = her elçinin koltuğu önündeki kişisel tercüman hoparlörü (A07 kelimesi). Başlangıçta hepsi Nem'e bakar, video onları çevirir. R157 Silex kurguda: Silex'in ağzı kapalı.
> Kare kapısı: kişi sayısı (Nem + Nith + dört elçi = 6) · masada K1 cyan, K2, blaster, beş alıcı okunuyor mu · Nem'in sağ şakağı çıplak mı · kamera hangi koltuk tarafından bakıyor, cam nerede.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 6 (station host): take his face, crest and coat from it. Reference 7 (chamber): take the black hexagonal table, the six chair positions, the panoramic window and the room geometry from it. Wide view from the near right side of the room, slightly elevated, across the black hexagonal table toward the far head chair. In the centre of the frame Nem stands at her near position, turned three-quarter toward the camera, her head lifted toward the whole table and her mouth closed, the smaller pewter clerk chair behind her. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. One rigid black hexagonal table stands before a broad panoramic curved window. Exactly six distinct fixed chair positions surround it: the far head chair facing the camera has ivory and black host colours; clockwise from it are bronze-red, teal, a smaller near-side pewter clerk chair, pale silver-violet, and ochre-brown. On the table lie a single compact dark blaster in front of the bronze-red seat, completely still; at the centre a single palm-sized black octagonal body whose triangular light now glows cyan, with a single flat frosted-purple pentagonal recording slab small enough to rest in one palm beside it; and five separate thin silver strips, translation receivers and not life-support parts. At the far head chair Nith sits upright and still, small in the background, his hands below the table edge. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. Around the table Vekh in bronze formal military armour over dark-red clothing, Ishra in her rigid transparent water-filled head dome and dark-teal suit, Silex in a simple pale-silver diplomatic mantle and Orun in an expensive ochre-brown formal coat sit small, in profile or seen from behind, all four looking toward Nem. Through the window behind Nith, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow gentle push toward Nem as she lifts her chin; Vekh, Ishra, Silex and Orun turn their heads and shoulders away from her toward the personal translation speaker in front of their own seat, while Nith stays seated and still; at about 1 s Nem's mouth moves and a precise steady adult female voice says: Tell your fleets what you mean. I'll preserve what you say. 3-7 s: She finishes by about 5.5 s and her mouth closes; the four envoys hold their turned positions, and the blaster, the cyan-lit octagonal body and the recording slab stay motionless on the table. 7-10 s: The push continues; Silex's head lifts a little toward the centre of the table with its mouth closed, and Nith's gaze lowers to the table while the gold side light slides across Nem's cheek ridges. Every mouth except Nem's stays closed. Sound: quiet chamber ventilation and distant table resonance.
```

## C86 — Vekh'in emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C86.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Vekh doğrudan kendi filosuna konuşur; silahı masada hareketsiz kalır." Bakış objektife (= filo). Silah kadrajın alt kenarında masada, namlu masa kenarı boyunca kimseye dönük değil; eller kadraj altında (T01 yok). T09: silah videoda yer değiştirmez. R158 Vekh 1,0 s (5,0 s). "withdraw / harbour" şiddet kelimesi değil.
> Kare kapısı: blaster alt kenarda okunuyor mu ve kimseye çevrik mi · sağ şakak çıplak mı · kamera hangi koltuktan, cam nerede.

### Görsel
```text
Reference 2 (military envoy): take his face and armour from it. Reference 7 (chamber): take the bronze-red chair position, the black hexagonal table, the panoramic window and the room geometry from it. Close three-quarter portrait of Vekh seen from the front with his right temple toward the camera, seated upright at the bronze-red chair position behind the black hexagonal table, his amber eyes level with the lens and his mouth closed. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. He wears bronze formal military armour over dark-red clothing. His right temple is bare. At the lower edge of the frame, on the black table surface, a single compact dark blaster lies completely still, its barrel along the table edge and pointing at no one; his hands rest below the crop. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push toward Vekh as he draws one steady breath and looks straight into the lens; at about 1 s his jaw plates move and a low rough controlled voice says: I order my fleet to withdraw. I will answer for the harbour. 3-7 s: He continues with minimal natural jaw-plate movement and finishes by about 6 s, while the blaster at the lower edge of the frame lies motionless on the table. 7-10 s: His mouth closes; the push eases closer and the gold side light edges his bronze armour, his amber eyes steady on the lens. Sound: quiet chamber ventilation and distant table resonance.
```

## C87 — Ishra'nın emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C87.png · referans (yükleme sırası, kare üretiminde): ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Ishra önce hastane gemilerine geçit açılmasını ister." Bakış objektife. Alıcı çıkmış (C67): soket boş; kubbe, su düzeyi ve yaşam destek bağlantıları sabit (plan). R159 Ishra 1,0 s (3,4 s).
> Kare kapısı: **Ishra'nın ağzı suyun içinden okunuyor mu** · soket boş, kubbe/su düzeyi sabit mi · göz asimetrisi/yansıma.

### Görsel
```text
Reference 3 (aquatic envoy): take her face, dome and suit from it. Reference 7 (chamber): take the teal chair position, the panoramic window and the room geometry from it. Close three-quarter portrait of Ishra seated at the teal chair position, seen from her right front so the water level and the right side of the dome stay readable, her two dark lateral eyes level with the lens and her mouth closed. Ishra is an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. The external socket at the right side of the dome is empty. Reflections on the dome are restrained so that the face stays readable. The panoramic window curves behind and beside her. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow push toward Ishra as she lifts her gaze to the lens; at about 1 s her mouth moves behind the clear dome and a clear restrained female voice with a soft resonant quality says: Open the evacuation lanes. All ships, stand down. 4-7 s: She finishes by about 4.5 s and her mouth closes; her chin lifts a fraction, the dome, its water level and the fixed life-support geometry staying steady. 7-10 s: The push eases closer while a soft gold reflection slides along the outer edge of the dome and her eyes hold on the lens. Sound: quiet chamber ventilation and distant table resonance.
```

## C88 — Silex'in emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C88.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Silex kendi ittifakının gemilerine ve arşivine seslenir." Bakış objektife. Silex'in alıcısı çıkmış (C68): sağ şakak çıplak. Aynı klipte aynı kişinin iki cümlesi model sesi (NOTLAR KARARLAR): R160 1,0 s (3,0 s) · R161 4,6 s (3,6 s; "finishes by about 8 s"). Cinsiyetsiz özne: "Silex's", zamir yok.
> Kare kapısı: faset yüzeyi sabit mi (uçuşan parça yok) · şakak çıplak mı.

### Görsel
```text
Reference 4 (mineral envoy): take its face, facets and mantle from it. Reference 7 (chamber): take the pale silver-violet chair position, the panoramic window and the room geometry from it. Close three-quarter portrait of Silex seated at the pale silver-violet chair position, seen from the front, its dark faceted eyes level with the lens and its mouth seam closed. Silex is an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. Silex's right temple is bare. Subtle internal violet translucency, restrained expression, no changing crystal growth. The panoramic window curves behind and beside Silex. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow push toward Silex as it lifts its gaze to the lens; at about 1 s the narrow central mouth seam moves and a clean, genderless voice with a light harmonic tone, calm and observant, says: Suspend the relay. Preserve every unaltered recording. 4-8 s: After a brief pause the mouth seam moves again at about 4.6 s and the same voice says: No translation replaces the words it claims to carry. It finishes by about 8 s. 8-10 s: The mouth seam closes; the facets catch the gold light as the push eases closer. Sound: quiet chamber ventilation and distant table resonance.
```

## C89 — Orun'un emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C89.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Orun ticaret filosuna kâr yerine hayatta kalanları taşıma görevi verir." Bakış objektife. Alıcı çıkmış (C69): şakak çıplak. İki cümle aynı kişi, model sesi: R162 1,0 s (3,8 s) · R163 5,4 s (3,2 s; 8,6'da biter). İki vuruş (0-5 · 5-10): ikinci cümle ikinci vuruşa düşer. BT §A "weapons" repliğinde → red gelirse kayda. Eller kadraj altında.

### Görsel
```text
Reference 5 (trade consul): take his face and coat from it. Reference 7 (chamber): take the ochre-brown chair position, the panoramic window and the room geometry from it. Close three-quarter portrait of Orun seated at the ochre-brown chair position, seen from the front, his two horizontal amber eyes level with the lens and his mouth closed; his hands rest below the crop. Orun is an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. Two arms, substantial but not exaggerated build. His right temple is bare. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-5 s: The camera begins a slow push toward Orun as his amber eyes settle on the lens; at about 1 s his broad folded lower jaw moves and he speaks in a husky baritone voice, quick and polished, with dry humour: No more weapons deliveries. My ships will carry survivors. He finishes by about 4.8 s. 5-10 s: At about 5.4 s he speaks again in the same voice: Send their arrival times without a security surcharge. He finishes by about 8.6 s and his mouth closes; the push eases closer as the gold light slides across his bark-like facial plates. Sound: quiet chamber ventilation and distant table resonance.
```

## C90 — Silahlar sönüyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C90.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Plan: "Vekh filosunun silah hatları söner; formasyon karşı taraftan açılır. Yeni savaş başlamaz." Diyalog yok. Kare: Vekh gemilerinin silah şeritleri hâlâ yanık (C03 sahnesinin kelimesi); video söndürür. "Yeni savaş başlamaz" olumlu yazıldı (diğer gruplar yerinde kalır). Ses: FILM §3 DIŞ ortam cümlesi birebir.

### Görsel
```text
Reference 8 (black hole and station): take the single black hole, its lensed golden disk and the small station from it. Reference 9 (four fleets): take the four ship families, the open corridor and the tiny medical craft from it. Extreme wide exterior of the four separated outer fleet groups facing one another across the open corridor. Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. The rust-red wedge ships are at one side with their weapon-light strips still lit; the white-teal fan vessels are opposite, with the silver faceted ships and ochre merchant carriers farther out. All ships remain outside the event horizon and away from disk material. The small diplomatic station is a distant silhouette. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. The black-hole shadow is truly dark. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: A slow lateral drift begins past the wide formation while the rust-red weapon-light strips still glow. 3-7 s: The strips on the rust-red wedge ships go dark group by group while all other fleet groups and the medical craft hold their positions. 7-10 s: The rust-red formation opens, its wedge ships separating and drawing back from the corridor on the side that faces the white-teal fleet, as the drift continues. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.
```

## C91 — Koridor açılıyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C91.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Plan: "Ishra'nın beyaz-teal gemileri koridor açar; küçük tıbbi/sivil gemiler aradan geçer." Diyalog yok. Başlangıç: koridor görünür ama dar, tıbbi/sivil gemiler kenarda bekliyor, Vekh gemilerinin silah şeritleri sönük (C90 sonucu). Video koridoru genişletir, küçük gemiler geçer. Ses: DIŞ ortam cümlesi birebir.

### Görsel
```text
Reference 8 (black hole and station): take the single black hole, its lensed golden disk and the small station from it. Reference 9 (four fleets): take the four ship families, the corridor and the tiny medical craft from it. Extreme wide exterior of the separated outer fleet groups around a visible but narrow open corridor. Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across the corridor, with a few tiny medical and civilian craft waiting at its edge. The pearl-white and teal fan-shaped vessels flank one side of the corridor in close ranks; the rust-red wedge ships stand opposite with their weapon-light strips dark. All ships remain outside the event horizon and away from disk material. The small diplomatic station is a distant silhouette. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. The black-hole shadow is truly dark. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: A slow lateral drift begins past the wide formation as the pearl-white and teal fan vessels start to slide apart along the corridor edge, widening it. 3-7 s: The tiny medical and civilian craft leave the corridor edge and move into the widened corridor, travelling between the two fleets while the rust-red ships stay dark and every other fleet group holds its position. 7-10 s: The small craft continue steadily through the open corridor as the drift carries on past the station silhouette. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.
```

## C92 — Başka bir tercüman

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C92.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Nith son sözü almaya çalışır; Nem kısaca karşılık verir." Model sesi yalnız Nith (R164 1,0 s, 1,6 s); Nem'in R165'i kurguda → Nem arkadan, hafif flu, ağzı görünmez (plan: "öteki kişilerin arkaları"). Nem'in yüz cümleleri yazılmaz (arkadan); özne + kemik (saç/kulak yok) + ceket + beden. Ceket cümlesi boğaz ışığı kısmı olmadan: arkadan görünmez. Nith oturur (C84 sonrası), alıcısı takılı.
> Kare kapısı: Nem'in ensesi/başı saçsız mı · Nith'in yüz kimliği · cam Nith'in arkasında mı.

### Görsel
```text
Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 1 (clerk): take her coat from it. Reference 7 (chamber): take the far ivory-black head chair, the black hexagonal table, the panoramic window and the room geometry from it. Over-the-shoulder close view down the black hexagonal table. In the left foreground, slightly out of focus, Nem stands at her near position seen from behind and slightly from her left side, her head turned toward the far end of the table. Nem is an adult nonhuman linguistic clerk. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat. Two arms, stable upright proportions, delicate but practical hands. At frame-right, in sharp focus, Nith sits upright at the far head chair facing the camera, his mouth closed. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. The panoramic window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. A controlled gold reflection edges one side of his face. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push over Nem's shoulder toward Nith; at about 1 s his chin lifts a little and he says calmly through his gold throat mesh in a smooth low male voice: They'll build another translator. 3-7 s: His mouth closes; Nem's shoulders square a fraction and her head tilts slightly toward him as she listens from behind. 7-10 s: The push continues; Nith's ice-blue eyes lower to the table and shift aside while the gold reflection slides along his brow ridge and crest, his facial ridge and crest staying fixed. No other voice speaks. Sound: quiet chamber ventilation and distant table resonance.
```

## C93 — Yerine değil yanında

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C93.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Ishra Nem'e yeni bir makam önerir; Nem göz hizasını eşit tutar." İkili, profil: ikisi de ayakta, gözler aynı yükseklikte (plan: eşit göz hizası). Model sesi yalnız Ishra (R166 1,0 s, 2,0 s); Nem'in R167'si kurguda → Nem'in ağzı kapalı. Alıcılar çıkmış: Ishra'nın soketi boş, Nem'in şakağı çıplak. Ishra'nın ağzı suyun içinden okunuyor mu → kare kapısı.
> Kare kapısı: iki göz aynı yükseklikte mi · Ishra'nın ağzı okunuyor mu · soket boş, su düzeyi sabit mi · cam arka planda mı.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 3 (aquatic envoy): take her face, dome and suit from it. Reference 7 (chamber): take the teal and pewter chair positions, the black hexagonal table, the panoramic window and the room geometry from it. Medium two-shot in profile from the side of the table at eye height. At frame-left Ishra stands at the teal chair position facing frame-right, seen from her right side so the empty external socket and the water level stay readable; at frame-right Nem stands at her near position facing frame-left, her dark-violet eyes at the same height as Ishra's, her mouth closed. They face each other across the corner of the table, a pace apart, their hands below the crop. Ishra is an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. The external socket at the right side of the dome is empty. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her temples are bare. The panoramic window curves behind them. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle lateral drift along the pair; at about 1 s Ishra's mouth moves behind the clear dome and a clear restrained female voice with a soft resonant quality says: Will you speak for us? 3-7 s: Ishra's mouth closes; Nem keeps her eyes level with Ishra's, her head steady and her mouth closed, as she listens. 7-10 s: The drift continues; Nem's shoulders settle a fraction while the dome and its water level stay fixed and the gold light slides across Nem's cheek ridges. No other voice speaks. Sound: quiet chamber ventilation and distant table resonance.
```

## C94 — Geçen günler

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C94.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Silex ile Nem kara deliğin ışığı önünde; diğerleri arka planda küçük kalır." Silex (saat 8) oturur, Nem (saat 6) ayakta, yan yana, pencere ve disk ışığı ikisinin arkasında. Model sesi yalnız Silex (R168 1,0 s, 2,0 s); R169 Nem kurguda → Nem'in ağzı kapalı. Diğer dördü küçük, arkadan/profilden, flu (≤3 referans). Alıcılar çıkmış: iki şakak çıplak.
> Kare kapısı: ikisi önde, diğer dördü küçük mü (kişi sayısı 6) · iki şakak çıplak mı.

### Görsel
```text
Reference 4 (mineral envoy): take its face, facets and mantle from it. Reference 1 (clerk): take her face and coat from it. Reference 7 (chamber): take the pale silver-violet and pewter chair positions, the black hexagonal table, the panoramic window and the room geometry from it. Wide view from the near right side of the room across the black hexagonal table. In the left half of the frame, in the foreground, Silex sits at the pale silver-violet chair position and Nem stands beside it at her near position, the smaller pewter clerk chair behind her, both turned three-quarter toward the camera with their mouths closed. Silex is an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. Silex's right temple is bare. Subtle internal violet translucency, restrained expression, no changing crystal growth. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. Nith in an ivory formal coat, Vekh in bronze formal military armour, Ishra in her transparent water-filled head dome and Orun in an ochre-brown formal coat sit small and soft-focus at their fixed positions in the background, seen from behind or in profile. The broad panoramic curved window glows behind Silex and Nem. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon, their golden light edging the two figures' shoulders. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push toward Silex and Nem; at about 1 s the narrow central mouth seam of Silex moves and a clean, genderless voice with a light harmonic tone, calm and observant, says: We can't recover those days. 3-7 s: Silex's mouth seam closes; Nem turns her head slightly toward Silex with her mouth closed while the four distant envoys stay small and still. 7-10 s: The push continues as the gold window light shifts across the facets of Silex's face and Nem's cheek ridges. No other voice speaks. Sound: quiet chamber ventilation and distant table resonance.
```

## C95 — İlk cümlenin karşılığı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C95.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Vekh açık kaynak kaydına son kez konuşur. Araya değiştirilmiş ses girmez." C86'dan farkı: daha yakın, hafif alttan, düz karşıdan; masa ve silah kadraj altında (kadrajda olmayan tarif edilmez). R170 Vekh 1,0 s (1,6 s). BT §A "fire" repliğinde → red gelirse kayda. Araya başka ses girmez (plan): "No other voice joins his."
> Kare kapısı: şakak çıplak mı · yüz C01'deki Vekh ile aynı mı · cam arkasında mı.

### Görsel
```text
Reference 2 (military envoy): take his face and armour from it. Reference 7 (chamber): take the bronze-red chair position, the panoramic window and the room geometry from it. Tight head-and-shoulders portrait of Vekh seen straight from the front, slightly from below, seated upright at the bronze-red chair position, his amber eyes level with the lens and his mouth closed. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. He wears bronze formal military armour over dark-red clothing. His right temple is bare. The table and his hands lie below the crop. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push toward Vekh as he draws one steady breath and holds his amber eyes on the lens; at about 1 s his jaw plates move and a low rough controlled voice says: We will not fire. 3-7 s: His mouth closes; his jaw plates settle and his shoulders ease a fraction while his eyes stay steady. 7-10 s: The push continues and eases closer as the gold side light edges his bronze armour. No other voice joins his. Sound: quiet chamber ventilation and distant table resonance.
```

## C96 — Olduğu gibi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C96.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Plan: "Aynı istasyon kara deliğin ışık yayı önünde; filolar ayrılmış, açık koridor kalmıştır." Final dış plan; Nem VO (R171) kurguda, videoda söz yok; başlık sonradan (plan). Silah şeritleri sönük, koridor geniş. Son vuruş yavaş geri çekilmeyi sürdürür (donmaz). Ses: DIŞ ortam cümlesi birebir.

### Görsel
```text
Reference 8 (black hole and station): take the single black hole, its lensed golden disk and the small station from it. Reference 9 (four fleets): take the four ship families, the open corridor and the tiny medical craft from it. Breathtaking extreme wide exterior of the small diplomatic station in the lower left, tiny against the bright lensed golden arc of the black hole, with the four fleet groups drawn apart into four distant clusters around a wide open corridor. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. Each group has one clear dominant design family: rust-red wedge warships with their weapon-light strips dark, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. All ships remain outside the event horizon and away from disk material. The black-hole shadow is truly dark. A bright tilted golden accretion disk and its gravitationally lensed upper and lower arcs wrap around the shadow, with one side visibly brighter. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow, steady pull back from the small station, widening the view of the lensed golden arc. 3-7 s: The four fleet groups drift slightly further apart in their separated positions while a few tiny medical craft glide along the open corridor. 7-10 s: The pull back continues past the whole formation as the station's small cold-blue windows keep glowing steadily and the brighter side of the golden disk gains a fraction of light. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları:** Return silent videos **KAPALI** · Visible watermarking **KAPALI** (G01 ile aynı). Frames to Video'ya referans eklenmez (yalnız kare); referanslar yalnız kare üretiminde, tabloda yazılan sırayla yüklenir.
> **Önkoşul:** `ref/1`-`ref/9` onaylı (G01 REFERANS PROMPTLARI) ve G01 pilot kararı (C01 · G06 C61 · G07 C79) verilmiş olmalı; G08 bölüm 8 olduğundan sonda üretilir.
> **Kare kapısı (her kare, ILK_30 §6 + G01 maddeleri):** filigran/logo · istenmeyen yazı · el kaynaşması · yüz bozulması / göz asimetrisi · kimlik kayması · **alıcı durumu** (Nem/Vekh/Ishra/Silex/Orun şakağı çıplak, Ishra soketi boş, Nith'inki takılı) · **Ishra'nın ağzı suyun içinden okunuyor mu** (C87 C93) · **blaster masada, kimseye çevrik değil** (C85 C86) · **K1 cyan, K2 yanında** (C85) · **kamera hangi koltuktan, cam nerede** (C85 C86 C92 C93 C94) · kişi sayısı (C85 C94).
> **Ses:** model sesi (ağız kadrajda) R156 · R158 · R159 · R160 · R161 · R162 · R163 · R164 · R166 · R168 · R170; kurguda R157 · R165 · R167 · R169 · R171. C90 C91: yalnız soyut skor (T13), yatak Y2 kurguda. Şiddet kelimeli replik: C89 "weapons" · C95 "fire" (red gelirse kayda).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C85 kare | `kare/C85.png` | Görsel | ref/1.NEM_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 2 | C86 kare | `kare/C86.png` | Görsel | ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 3 | C87 kare | `kare/C87.png` | Görsel | ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 4 | C88 kare | `kare/C88.png` | Görsel | ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 5 | C89 kare | `kare/C89.png` | Görsel | ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 6 | C90 kare | `kare/C90.png` | Görsel | ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png (bu sırayla) | 2 | |
| 7 | C91 kare | `kare/C91.png` | Görsel | ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png (bu sırayla) | 2 | |
| 8 | C92 kare | `kare/C92.png` | Görsel | ref/1.NEM_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 9 | C93 kare | `kare/C93.png` | Görsel | ref/1.NEM_v1.png · ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 10 | C94 kare | `kare/C94.png` | Görsel | ref/4.SILEX_v1.png · ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 11 | C95 kare | `kare/C95.png` | Görsel | ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 12 | C96 kare | `kare/C96.png` | Görsel | ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png (bu sırayla) | 2 | |
| 13 | C85 | `ham/C85_d1.mp4` | Frames to Video | kare/C85.png | 2 | |
| 14 | C86 | `ham/C86_d1.mp4` | Frames to Video | kare/C86.png | 2 | |
| 15 | C87 | `ham/C87_d1.mp4` | Frames to Video | kare/C87.png | 2 | |
| 16 | C88 | `ham/C88_d1.mp4` | Frames to Video | kare/C88.png | 2 | |
| 17 | C89 | `ham/C89_d1.mp4` | Frames to Video | kare/C89.png | 2 | |
| 18 | C90 | `ham/C90_d1.mp4` | Frames to Video | kare/C90.png | 2 | |
| 19 | C91 | `ham/C91_d1.mp4` | Frames to Video | kare/C91.png | 2 | |
| 20 | C92 | `ham/C92_d1.mp4` | Frames to Video | kare/C92.png | 2 | |
| 21 | C93 | `ham/C93_d1.mp4` | Frames to Video | kare/C93.png | 2 | |
| 22 | C94 | `ham/C94_d1.mp4` | Frames to Video | kare/C94.png | 2 | |
| 23 | C95 | `ham/C95_d1.mp4` | Frames to Video | kare/C95.png | 2 | |
| 24 | C96 | `ham/C96_d1.mp4` | Frames to Video | kare/C96.png | 2 | |

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · G08 tur 1)

> Q1: Kolun/göğsün göründüğü çekim yok. Nem'in tek işareti (boğaz ışığı) A01 kelimeleriyle ("one small cobalt throat light") C85, C93, C94'te yazılı; `the only marking` plan dışı olduğundan yazılmadı. C92'de Nem arkadan (boğaz ışığı görünmez, cümle kesildi).
> Q3 (tüm çekimler): ORTAK GÖRÜNÜM ışık/yansıma taşıyor → `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` G01'de zaten Fable'da; bu grupta çelişen su/gezegen/ses yok (salon ve dış ışık aynı yönde).
> Q5 (tüm çekimler): `plume · smoke · drip · wet · bubbles` yok; Ishra'nın başlığındaki su plan gereği katı hâl ("constant visible water level"); silah şeritleri lamba şeridi.
> Q7 (tüm çekimler): her `Reference n` yalnız o tek görünüşte görüneni istiyor; alıcı çıkmış olduğundan Nem/Vekh/Ishra/Silex/Orun anahtarlarında alıcı istenmedi (sayfada takılı görünür).
> Q8: model sesi AÇIK film (ortam sesi cümleleri yazılı); zıt iki istek yok. Kadraj dışı repliklerde kadrajdaki ağzın kapalı kalması **olumlu** yazıldı ("her mouth stays closed" / "No other voice speaks").

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C85 | 2 (Nem, Nith tam kimlik; K1 "pale amber" → "now glows cyan" = plan nesne durumu C78; alıcı cümlesi → "right temple is bare" = plan C61; beş alıcı = A12 cümlesi) · 4 (pencere Nith'in arkası yazılı, kişilerin arkası: sandalyeler) · 6 (masada ekran yok; "personal translation speakers" biçimle) | Dört elçi küçük; kimlik cümleleri yerine kısa kimlik kelimeleri (plan: "arkaları veya flu siluetleri"); ≤3 referans |
| C86 | 2 (zırh cümlesi kalçasız sürüm; blaster masada: A13 "a single compact dark blaster", kılıf cümlesi çelişirdi) · 4 (cam arkasında ve yanında) | Sağ şakak çıplak = plan C64; alıcı istenmedi |
| C87 | 2 (soket boş = plan C67; kubbe/su/yaşam destek cümleleri birebir) · 4 | Ağız suyun içinden: kare kapısı maddesi (tasarım boşluğu SK4) |
| C88 | 2 (alıcı cümlesi → "right temple is bare") · 4 | Cinsiyetsiz zamir yok |
| C89 | 2 (alıcı → "right temple is bare") · 4 | "weapons" model sesinde (red gelirse kayda); iki cümle iki vuruş |
| C90 | 2 (Kara delik · Disk · İstasyon · Filolar · Koridor+tıbbi parçaları) · 4 (dış: ardında kara delik) | "weapon-light strips" = plan C03 kelimesi; "Yeni savaş başlamaz" olumlu (diğer gruplar yerinde kalır) |
| C91 | 2 (tıbbi + sivil gemiler plan C91 cümlesinden) · 4 | Koridor "visible but narrow" başlar: plan "koridor açar" eylemi videoda olur (plan A09 "open corridor" kelimesi korundu) |
| C92 | 2 (Nem arkadan: yüz ve boğaz ışığı cümlesi yazılmadı; Nith tam) · 4 (cam Nith'in arkasında, Nem'in arkası: kamera) | Nem'in referansı tek görünüşlü; arka görünüş metinle (plan kararı) |
| C93 | 2 (Ishra soket boş; Nem "temples are bare") · 4 | Eşit göz hizası için ikisi ayakta (plan: "göz hizasını eşit tutar"); Ishra'nın ağzı kare kapısı |
| C94 | 2 (Silex ve Nem tam; alıcı → "temple is bare") · 4 (cam ikisinin arkasında; diğerlerinin arkası: kimlik kelimeleri) | Diğer dört: küçük/flu (plan) |
| C95 | 2 · 4 | Masa ve silah kadraj altı; "fire" model sesinde (red gelirse kayda) |
| C96 | 2 (Kara delik · Disk · İstasyon · Filolar · Koridor) · 4 | Nem VO kurguda; video söz taşımaz; ortak görünüm "warm gold black-hole reflections" DIŞ ışığıyla aynı yönde |
