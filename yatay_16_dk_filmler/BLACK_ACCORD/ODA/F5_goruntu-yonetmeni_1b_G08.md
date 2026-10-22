# 🖼️ BLACK_ACCORD — Prompt grubu G08 (çekimler C85–C96 · bölüm B8 ASLIYLA AYNI) · tur 1b

> Yazan: goruntu-yonetmeni (faz 5, tur 1b; Fable kararları `ODA/F5_fable_birlestirme_2_G02-G08.md` "ORTAK" + "G08" bölümleri; RED satırlarına dokunulmadı). Önceki sürüm: `ODA/F5_goruntu-yonetmeni_1_G08.md`. Kaynak: `BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md` (sahip planı; "plandan asla dışarı çıkma") + `NOTLAR.md` KARARLAR (18.10.2026).
> **Plan C85-C96 için promptsuzdur;** yalnız plan malzemesi kullanıldı: planın çekim cümlesi · A01-A13 İngilizce cümleleri (FILM §3 KİMLİK CÜMLELERİ, kadrajdaki parça birebir) · sabit düzen · nesne durumu · G01 örneği (C07-C12) · ROL SÖZLÜĞÜ · MEKÂN IŞIĞI · ORTAM SESİ · SES KİMLİĞİ · **DURUM CÜMLELERİ** (FILM §3, film boyu birebir).
> **Başlangıç durumu (DURUM CÜMLELERİ):** alıcı çıkmış → "Her/His/Silex's right temple is bare." · Ishra "The external socket at the right side of the dome is empty." · masadaki şerit görünüyorsa A12 cümlesi + yeri · blaster masada, kılıf cümlesi yazılmaz (kalça kadrajda değil) · K1 "one cyan triangular light" (C80+) · K2 K1'in yanında, bir avuç arayla (C83+) · Nith C85+ oturur, Vekh C85+ oturur, Ishra oturur (C93'te Nem Ishra'nın göz hizasına iner) · dış planlarda kırmızı kama gemileri frame-left, beyaz-teal yelpaze gemileri frame-right, istasyon "small in the lower right third", C90'da Vekh filosunun silah şeritleri yanık başlar ve söner, C91 açık koridorla başlar.
> **Işık (ORTAK 4):** cam kadrajda → "Warm gold side light and cool readable face shadows." (G08'de kamera hiçbir yerde uzak uçta değil; "from the camera side" yok.)
> **Ortak görünüm** her Görsel'in sonunda; video promptlarına eklenmez (plan yalnız Görsel'de; NOTLAR KARARLAR). Model sesi AÇIK: replikler `<ses cümlesi>: <line>`. Kod / başlık / "Clip n of N" yok. Her blok ≤4.300 karakter. Vuruş iskeleti çekimden çekime değişir; son vuruş çekimdeki kişinin ya da planın nesnesinin küçük hâlidir.
> **Model sesi dağılımı (FILM §5):** C85 R156 Nem · C86 R158 Vekh · C87 R159 Ishra · C88 R160+R161 Silex · C89 R162+R163 Orun · C92 R164 Nith · C93 R166 Ishra · C94 R168 Silex · C95 R170 Vekh. Kurguda (kadraj dışı; kadrajdaki ağız kapalı): R157 Silex (C85) · R165 Nem (C92) · R167 Nem (C93) · R169 Nem (C94) · R171 Nem VO (C96). C90 · C91: söz yok.
> **Şiddet kelimeli model sesi:** C89 "weapons" · C95 "fire" (BT §A, red riski) — red gelirse yalnız o replik kayda geçer, metin değişmez.

---

## C85 — Dört filoya

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C85.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Geniş / yeni masa düzeni. Nith etkisiz biçimde arka plandadır. Nem merkezde; dört elçi kendi kaydına döner." Dört elçi arkadan/profilden küçük (plan: "arkaları veya flu siluetleri"; ≤3 referans). Plan eylemi = dört elçinin dönüşü (birincil, 1. deneme). Videoda başka ek hareket yok. Masadaki beş alıcı (plan C69) kalır.
> **YEDEK (deneme 2 = planın kendi çözümü):** elçiler kare başında dönmüş. Kare promptunda tek cümle değişir: `all four looking toward Nem` → `all four already turned toward the personal translation speaker in front of their own seat`; video 0-4 s'deki dönüş cümlesi çıkar, yalnız push + Nem'in konuşması kalır.
> Kare kapısı: kişi sayısı (Nem + Nith + dört elçi = 6) · masada K1 cyan, K2 yanında, blaster, beş şerit okunuyor mu · Nem'in sağ şakağı çıplak mı · kamera hangi koltuk tarafından bakıyor, cam nerede.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 6 (station host): take his face, crest and coat from it. Reference 7 (chamber): take the black hexagonal table, the six chair positions, the panoramic window and the room geometry from it. Wide view from the near right side of the room, slightly elevated, across the black hexagonal table toward the far head chair. In the centre of the frame Nem stands at her near position, turned three-quarter toward the camera, her head lifted toward the whole table and her mouth closed, the smaller pewter clerk chair behind her. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. One rigid black hexagonal table stands before a broad panoramic curved window. Exactly six distinct fixed chair positions surround it: the far head chair facing the camera has ivory and black host colours; clockwise from it are bronze-red, teal, a smaller near-side pewter clerk chair, pale silver-violet, and ochre-brown. On the table lie a single compact dark blaster in front of the bronze-red seat, completely still; at the centre a single palm-sized black octagonal body with one cyan triangular light, and a single flat frosted-purple pentagonal recording slab small enough to rest in one palm beside it, a palm's width apart; and five thin silver strips, each a translation receiver and not a life-support part, one in front of each of Nem, Vekh, Ishra, Silex and Orun. At the far head chair Nith sits upright and still, small in the background, his hands below the table edge. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. Around the table Vekh in bronze formal military armour over dark-red clothing, Ishra in her rigid transparent water-filled head dome and dark-teal suit, Silex in a simple pale-silver diplomatic mantle and Orun in an expensive ochre-brown formal coat sit small, in profile or seen from behind, all four looking toward Nem. Through the window behind Nith, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow gentle push toward Nem as she lifts her chin; Vekh, Ishra, Silex and Orun turn their heads and shoulders away from her toward the personal translation speaker in front of their own seat, while Nith stays seated and still; at about 1 s Nem's mouth moves and a precise steady adult female voice says: Tell your fleets what you mean. I'll preserve what you say. 4-8 s: She finishes by about 5.6 s and her mouth closes; the four envoys hold their turned positions, and the blaster, the octagonal body and the recording slab stay motionless on the table. 8-10 s: Nem's gaze moves along the four envoys one after another and her shoulders ease with a quiet breath. Every mouth except Nem's stays closed. Sound: quiet chamber ventilation and distant table resonance.
```

## C86 — Vekh'in emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C86.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Vekh doğrudan kendi filosuna konuşur; silahı masada hareketsiz kalır." Bakış objektife (= filo). Silah kadrajın alt kenarında masada, kimseye dönük değil; eller kadraj altında. T09: silah videoda yer değiştirmez. R158 Vekh 1,0 s (5,0 s → 6.0 s).
> Kare kapısı: blaster alt kenarda okunuyor mu · sağ şakak çıplak mı · kamera hangi koltuktan, cam nerede.

### Görsel
```text
Reference 2 (military envoy): take his face and armour from it. Reference 7 (chamber): take the bronze-red chair position, the black hexagonal table, the panoramic window and the room geometry from it. Close three-quarter portrait of Vekh seen from the front with his right temple toward the camera, seated upright at the bronze-red chair position behind the black hexagonal table, his amber eyes level with the lens and his mouth closed. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. His body is upright with two arms and two legs. He wears bronze formal military armour over dark-red clothing. His right temple is bare. At the lower edge of the frame, on the black table surface, a single compact dark blaster lies completely still, its barrel along the table edge and pointing at no one; his hands rest below the crop. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-2 s: The camera begins a slow push toward Vekh as he draws one steady breath and looks straight into the lens; at about 1 s his jaw plates move and a low rough controlled voice says: I order my fleet to withdraw. I will answer for the harbour. 2-7 s: He continues with minimal natural jaw-plate movement and finishes by about 6 s, while the blaster at the lower edge of the frame lies motionless on the table. 7-10 s: His mouth closes; his shoulders ease a fraction and his chin lowers slightly, his amber eyes steady on the lens. Sound: quiet chamber ventilation and distant table resonance.
```

## C87 — Ishra'nın emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C87.png · referans (yükleme sırası, kare üretiminde): ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Ishra önce hastane gemilerine geçit açılmasını ister." Bakış objektife. Alıcı çıkmış (C67): soket boş; kubbe, su düzeyi ve yaşam destek bağlantıları sabit (plan). R159 Ishra 1,0 s (3,4 s → 4.4 s). Ağız tarifi yok (plan C02 kalıbı: "she answers in … voice: <line>").
> Kare kapısı: **Ishra'nın ağzı suyun içinden okunuyor mu** · soket boş, kubbe/su düzeyi sabit mi · göz asimetrisi/yansıma.

### Görsel
```text
Reference 3 (aquatic envoy): take her face, dome and suit from it. Reference 7 (chamber): take the teal chair position, the panoramic window and the room geometry from it. Close three-quarter portrait of Ishra seated at the teal chair position, seen from her right front so the water level and the right side of the dome stay readable, her two dark lateral eyes level with the lens. Ishra is an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. The external socket at the right side of the dome is empty. Reflections on the dome are restrained so that the face stays readable. The panoramic window curves behind and beside her. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-5 s: The camera begins a slow push toward Ishra as she lifts her gaze to the lens; at about 1 s she answers in a clear restrained female voice with a soft resonant quality: Open the evacuation lanes. All ships, stand down. She finishes by about 4.4 s. 5-8 s: Her face settles; her chin lifts a fraction, the dome, its water level and the fixed life-support geometry staying steady. 8-10 s: Her gaze moves slowly off the lens toward the far end of the table while a soft gold reflection slides along the outer edge of the dome. Sound: quiet chamber ventilation and distant table resonance.
```

## C88 — Silex'in emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C88.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Silex kendi ittifakının gemilerine ve arşivine seslenir." Bakış objektife. Alıcı çıkmış (C68). Aynı klipte aynı kişinin iki cümlesi model sesi: R160 1,0 s (3,0 s → 4.0 s) · R161 4,6 s (3,6 s → 8.2 s). İki vuruş (0-4.5 · 4.5-10): ikinci cümle ikinci vuruşta biter. Zamir yok ("Silex's").
> Kare kapısı: faset yüzeyi sabit mi (uçuşan parça yok) · şakak çıplak mı.

### Görsel
```text
Reference 4 (mineral envoy): take Silex's face, facets and mantle from it. Reference 7 (chamber): take the pale silver-violet chair position, the panoramic window and the room geometry from it. Close three-quarter portrait of Silex seated at the pale silver-violet chair position, seen from the front, Silex's dark faceted eyes level with the lens and the mouth seam closed. Silex is an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. Silex's right temple is bare. Subtle internal violet translucency, restrained expression, no changing crystal growth. The panoramic window curves behind and beside Silex. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4.5 s: The camera begins a slow push toward Silex as Silex lifts a calm gaze to the lens; at about 1 s the narrow central mouth seam moves and a clean, genderless voice with a light harmonic tone, calm and observant, says: Suspend the relay. Preserve every unaltered recording. 4.5-10 s: After a brief pause the mouth seam moves again at about 4.6 s and the same voice says: No translation replaces the words it claims to carry. It finishes by about 8.2 s, the mouth seam closes, and the facets catch the gold light while Silex's gaze stays level. Sound: quiet chamber ventilation and distant table resonance.
```

## C89 — Orun'un emri

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C89.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Orun ticaret filosuna kâr yerine hayatta kalanları taşıma görevi verir." Bakış objektife. Alıcı çıkmış (C69). İki cümle aynı kişi, model sesi: R162 1,0 s (3,8 s → 4.8 s) · R163 5,4 s (3,2 s → 8.6 s). İki vuruş (0-5 · 5-10). BT §A "weapons" repliğinde → red gelirse kayda. Eller kadraj altında.

### Görsel
```text
Reference 5 (trade consul): take his face and coat from it. Reference 7 (chamber): take the ochre-brown chair position, the panoramic window and the room geometry from it. Close three-quarter portrait of Orun seated at the ochre-brown chair position, seen from the front, his two horizontal amber eyes level with the lens and his mouth closed; his hands rest below the crop. Orun is an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. Two arms, substantial but not exaggerated build. His right temple is bare. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-5 s: The camera begins a slow push toward Orun as his amber eyes settle on the lens; at about 1 s his broad folded lower jaw moves and he speaks in a husky baritone voice, quick and polished, with dry humour: No more weapons deliveries. My ships will carry survivors. He finishes by about 4.8 s. 5-10 s: At about 5.4 s he speaks again in the same voice: Send their arrival times without a security surcharge. He finishes by about 8.6 s and his mouth closes; his heavy lids lower a fraction and his amber eyes shift from the lens to the side. Sound: quiet chamber ventilation and distant table resonance.
```

## C90 — Silahlar sönüyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C90.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Plan: "Vekh filosunun silah hatları söner; formasyon karşı taraftan açılır. Yeni savaş başlamaz." Diyalog yok. Dış plan tarafı FILM §3: kırmızı kama gemileri frame-left, beyaz-teal yelpaze gemileri frame-right. Kare: Vekh gemilerinin silah şeritleri yanık; video söndürür ve formasyonu açar (C91 koridoru açık başlar). "Yeni savaş başlamaz" olumlu (diğer gruplar yerinde).
> Kare kapısı: **silah şeritleri 1080p'de seçiliyor mu** (seçilmiyorsa Görsel'de `their weapon-light strips still lit` → `bright red weapon-light strips along every hull, still lit`).

### Görsel
```text
Reference 8 (black hole and station): take the single black hole, its lensed golden disk and the small station from it. Reference 9 (four fleets): take the four ship families, the open corridor and the tiny medical craft from it. Extreme wide exterior of the four separated outer fleet groups facing one another across the open corridor. Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. The rust-red wedge ships at frame-left have their weapon-light strips still lit and the pearl-white and teal fan vessels at frame-right face them, with the silver faceted ships and ochre merchant carriers farther out. All ships remain outside the event horizon and away from disk material. The small diplomatic station is a distant silhouette. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. The black-hole shadow is truly dark. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-2 s: A slow lateral drift begins past the wide formation while the rust-red weapon-light strips still glow. 2-6 s: The strips on the rust-red wedge ships go dark group by group while all other fleet groups and the medical craft hold their positions. 6-10 s: The rust-red formation opens, its wedge ships separating and drawing back from the corridor on the side that faces the white-teal fleet, leaving the corridor wide open. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.
```

## C91 — Koridor açılıyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C91.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Plan: "Ishra'nın beyaz-teal gemileri koridor açar; küçük tıbbi/sivil gemiler aradan geçer." Plan "Çok geniş" kalır; C90'dan farklı açı: daha yüksekten, koridorun boyuna bakış (tarafı aynı: kırmızı frame-left, beyaz-teal frame-right). Koridor C90'ın bittiği gibi açık başlar (durum geri sarılmaz); Vekh gemilerinin silah şeritleri sönük. Video: yelpaze gemileri sıralarını açık tutar, küçük gemiler koridordan geçer. Ses: DIŞ ortam cümlesi birebir.

### Görsel
```text
Reference 8 (black hole and station): take the single black hole, its lensed golden disk and the small station from it. Reference 9 (four fleets): take the four ship families, the corridor and the tiny medical craft from it. Extreme wide exterior from a higher vantage, looking down the length of the wide open corridor between the separated outer fleet groups. Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical and civilian craft waiting at its edge. The rust-red wedge ships at frame-left have their weapon-light strips dark, and the pearl-white and teal fan vessels at frame-right hold open ranks along the corridor. All ships remain outside the event horizon and away from disk material. The small diplomatic station is a distant silhouette. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. The black-hole shadow is truly dark. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: A slow descending drift begins down the length of the corridor as the pearl-white and teal fan vessels ease outward along its edge, holding it open. 3-7 s: The tiny medical and civilian craft leave the corridor edge and move into the open corridor, travelling between the two fleets while the rust-red ships stay dark and every other fleet group holds its position. 7-10 s: The leading small craft pass the middle of the corridor between the fleets, the rest following in a loose line. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.
```

## C92 — Başka bir tercüman

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C92.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Nith son sözü almaya çalışır; Nem kısaca karşılık verir." Model sesi yalnız Nith (R164 1,0 s, 1,6 s → 2.6 s); Nem'in R165'i kurguda → Nem arkadan, hafif flu. Nem'in başı planın A01 kelimesiyle ("without human ears or hair"). Nith oturur (C85+), alıcısı takılı. Reference sırası = EKLE sırası (1, 6, 7).
> Kare kapısı: Nem'in ensesi/başı saçsız mı · Nith'in yüz kimliği · cam Nith'in arkasında mı.

### Görsel
```text
Reference 1 (clerk): take her coat from it. Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 7 (chamber): take the far ivory-black head chair, the black hexagonal table, the panoramic window and the room geometry from it. Over-the-shoulder close view down the black hexagonal table. In the left foreground, slightly out of focus, Nem stands at her near position seen from behind and slightly from her left side, her head turned toward the far end of the table. Nem is an adult nonhuman linguistic clerk. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat. Two arms, stable upright proportions, delicate but practical hands. At frame-right, in sharp focus, Nith sits upright at the far head chair facing the camera, his mouth closed. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. The panoramic window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. A controlled gold reflection edges one side of his face. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push over Nem's shoulder toward Nith; at about 1 s his chin lifts a little and he says calmly through his gold throat mesh in a smooth low male voice: They'll build another translator. 3-6 s: The gold throat mesh goes still; Nem's shoulders square a fraction and her head tilts slightly toward him as she listens from behind. 6-10 s: Nith's ice-blue eyes lower to the table and shift aside while the gold reflection slides along his brow ridge and crest, his facial ridge and crest staying fixed. No other voice speaks. Sound: quiet chamber ventilation and distant table resonance.
```

## C93 — Yerine değil yanında

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C93.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Ishra Nem'e yeni bir makam önerir; Nem göz hizasını eşit tutar." Ishra oturur (teal koltuk), Nem onun göz hizasına iner (plan: "göz hizasını eşit tutar"; DURUM merdiveni). Model sesi yalnız Ishra (R166 1,0 s, 2,0 s → 3.0 s); Nem'in R167'si kurguda → Nem'in ağzı kapalı. Ishra'nın soketi boş, Nem'in sağ şakağı çıplak.
> Kare kapısı: iki göz aynı yükseklikte mi · Ishra'nın ağzı okunuyor mu · soket boş, su düzeyi sabit mi · cam masanın ötesinde mi.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 3 (aquatic envoy): take her face, dome and suit from it. Reference 7 (chamber): take the teal and pewter chair positions, the black hexagonal table, the panoramic window and the room geometry from it. Medium two-shot in profile from the side of the table at eye height. At frame-left Ishra sits at the teal chair position facing frame-right, seen from her right side so the empty external socket and the water level stay readable; at frame-right Nem has lowered herself beside the table corner, knees slightly bent and torso inclined, facing frame-left with her dark-violet eyes at the same height as Ishra's and her mouth closed. They face each other a pace apart, their hands below the crop. Ishra is an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. The external socket at the right side of the dome is empty. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. The panoramic window glows beyond the table. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle lateral drift along the pair; at about 1 s Ishra answers in a clear restrained female voice with a soft resonant quality: Will you speak for us? 3-6 s: Ishra's face settles; Nem keeps her eyes level with Ishra's, her head steady and her mouth closed, as she listens. 6-10 s: Nem's shoulders settle a fraction while Ishra's gaze lowers slightly, the dome and its water level staying fixed and the gold light sliding across Nem's cheek ridges. No other voice speaks. Sound: quiet chamber ventilation and distant table resonance.
```

## C94 — Geçen günler

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C94.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Silex ile Nem kara deliğin ışığı önünde; diğerleri arka planda küçük kalır." Kamera odanın yakın ucundan cama doğru, hafif yüksekten; cam masanın ötesinde parlıyor, ışığı iki figürün omuzlarını kenarlıyor (FILM §3 sabit düzen: cam Nith'in arkasında). Silex ve Nem üç-çeyrek profil. Model sesi yalnız Silex (R168 1,0 s, 2,0 s → 3.0 s); R169 Nem kurguda → Nem'in ağzı kapalı. Alıcılar çıkmış.
> Kare kapısı: ikisi önde, diğer dördü küçük mü (kişi sayısı 6) · iki şakak çıplak mı · cam konumu.

### Görsel
```text
Reference 4 (mineral envoy): take Silex's face, facets and mantle from it. Reference 1 (clerk): take her face and coat from it. Reference 7 (chamber): take the pale silver-violet and pewter chair positions, the black hexagonal table, the panoramic window and the room geometry from it. Wide view from the near end of the room toward the window, slightly elevated. In the left half of the frame, in the foreground, Silex sits at the pale silver-violet chair position and Nem stands beside it at her near position, the smaller pewter clerk chair behind her, both turned in three-quarter profile with their mouths closed. Silex is an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. Silex's right temple is bare. Subtle internal violet translucency, restrained expression, no changing crystal growth. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. Nith in an ivory formal coat, Vekh in bronze formal military armour, Ishra in her transparent water-filled head dome and Orun in an ochre-brown formal coat sit small and soft-focus at their fixed positions on the far side of the table. The broad panoramic curved window glows beyond the table. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon, their golden light edging the two figures' shoulders. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow push toward Silex and Nem; at about 1 s the narrow central mouth seam of Silex moves and a clean, genderless voice with a light harmonic tone, calm and observant, says: We can't recover those days. 4-7 s: Silex's mouth seam closes; Nem turns her head slightly toward Silex with her mouth closed while the four distant envoys stay small and still. 7-10 s: Nem's shoulders ease and her gaze lowers a fraction as the gold window light shifts across the facets of Silex's face and her cheek ridges. No other voice speaks. Sound: quiet chamber ventilation and distant table resonance.
```

## C95 — İlk cümlenin karşılığı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C95.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Vekh açık kaynak kaydına son kez konuşur. Araya değiştirilmiş ses girmez." C86'dan farkı: daha yakın, hafif alttan, düz karşıdan; masa ve silah kadraj altında. R170 Vekh 1,0 s (1,6 s → 2.6 s). BT §A "fire" repliğinde → red gelirse kayda. Araya başka ses girmez (plan).
> Kare kapısı: şakak çıplak mı · yüz C01'deki Vekh ile aynı mı · cam arkasında mı.

### Görsel
```text
Reference 2 (military envoy): take his face and armour from it. Reference 7 (chamber): take the bronze-red chair position, the panoramic window and the room geometry from it. Tight head-and-shoulders portrait of Vekh seen straight from the front, slightly from below, seated upright at the bronze-red chair position, his amber eyes level with the lens and his mouth closed. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. His body is upright with two arms and two legs. He wears bronze formal military armour over dark-red clothing. His right temple is bare. The table and his hands lie below the crop. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push toward Vekh as he draws one steady breath and holds his amber eyes on the lens; at about 1 s his jaw plates move and a low rough controlled voice says: We will not fire. 3-8 s: His mouth closes; his jaw plates settle and the gold side light edges his bronze armour while his eyes stay steady. 8-10 s: His shoulders ease and his gaze slides slowly from the lens to the side. No other voice joins his. Sound: quiet chamber ventilation and distant table resonance.
```

## C96 — Olduğu gibi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C96.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Plan: "Aynı istasyon kara deliğin ışık yayı önünde; filolar ayrılmış, açık koridor kalmıştır." Final dış plan; Nem VO (R171) kurguda, videoda söz yok; başlık sonradan (plan). İstasyon "small in the lower right third" (FILM §3); kırmızı gemiler frame-left, beyaz-teal frame-right; silah şeritleri sönük, koridor geniş. Son vuruş donmaz: küçük gemiler koridorun sonuna varır. Ses: DIŞ ortam cümlesi birebir.

### Görsel
```text
Reference 8 (black hole and station): take the single black hole, its lensed golden disk and the small station from it. Reference 9 (four fleets): take the four ship families, the open corridor and the tiny medical craft from it. Breathtaking extreme wide exterior of the small diplomatic station small in the lower right third, tiny against the bright lensed golden arc of the black hole, with the four fleet groups drawn apart into four distant clusters around a wide open corridor. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. Each group has one clear dominant design family: rust-red wedge warships with their weapon-light strips dark at frame-left, pearl-white and teal fan-shaped vessels at frame-right, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. All ships remain outside the event horizon and away from disk material. The black-hole shadow is truly dark. A bright tilted golden accretion disk and its gravitationally lensed upper and lower arcs wrap around the shadow, with one side visibly brighter. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow, steady pull back from the small station, widening the view of the lensed golden arc. 4-7 s: The four fleet groups drift slightly further apart in their separated positions while a few tiny medical craft glide along the open corridor. 7-10 s: The station's small cold-blue windows keep glowing steadily as the tiny medical craft reach the far end of the corridor and the brighter side of the golden disk gains a fraction of light. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları:** Return silent videos **KAPALI** · Visible watermarking **KAPALI** (G01 ile aynı). Frames to Video'ya referans eklenmez (yalnız kare); referanslar yalnız kare üretiminde, tabloda yazılan sırayla yüklenir.
> **Önkoşul:** `ref/1`-`ref/9` onaylı (G01 REFERANS PROMPTLARI) ve G01 pilot kararı (C01 · G06 C61 · G07 C79) verilmiş olmalı; G08 bölüm 8 olduğundan sonda üretilir.
> **Deneme 2 = YEDEK kuralı (T01/T15 çekimleri):** C85 satırında yazılı; planın kendi çözümü (elçiler kare başında dönmüş), C85 notundaki tek cümle değişimiyle.
> **Kare kapısı (her kare):** filigran/logo · istenmeyen yazı · el kaynaşması · yüz bozulması / göz asimetrisi · kimlik kayması · **alıcı durumu** (Nem/Vekh/Ishra/Silex/Orun şakağı çıplak, Ishra soketi boş, Nith'inki takılı) · **Ishra'nın ağzı suyun içinden okunuyor mu** (C87 C93) · **blaster masada, kimseye çevrik değil** (C85 C86) · **K1 cyan, K2 yanında** (C85) · **silah şeritleri 1080p'de seçiliyor mu** (C90) · **kamera hangi koltuktan, cam nerede** (C85 C86 C92 C93 C94) · kişi sayısı (C85 C94) · **profil yüz çizgisi** (C93 C94).
> **Ses:** model sesi (ağız kadrajda) R156 · R158 · R159 · R160 · R161 · R162 · R163 · R164 · R166 · R168 · R170; kurguda R157 · R165 · R167 · R169 · R171. C90 C91 C96: yalnız soyut skor (T13), yatak Y2 kurguda. Şiddet kelimeli replik: C89 "weapons" · C95 "fire" (red gelirse kayda).

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
| 13 | C85 | `ham/C85_d1.mp4` | Frames to Video | kare/C85.png · **Deneme 2 = YEDEK** (planın kendi çözümü: elçiler kare başında dönmüş; kare promptunda `all four looking toward Nem` → `all four already turned toward the personal translation speaker in front of their own seat`, video yalnız push + Nem'in konuşması) | 2 | |
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

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · G08 tur 1b)

> Q1: Kolun/göğsün göründüğü çekim yok. Nem'in tek işareti (boğaz ışığı) A01 kelimeleriyle ("one small cobalt throat light") C85, C93, C94'te yazılı; `the only marking` plan dışı olduğundan yazılmadı. C92'de Nem arkadan (boğaz ışığı görünmez, cümle kesildi).
> Q3 (tüm çekimler): ORTAK GÖRÜNÜM ışık/yansıma taşıyor → `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` FILM §3'te Fable'da; G08'de çelişen su/gezegen/ses yok. Salon ışığı: cam kadrajda olan her çekimde "Warm gold side light" (uzak uç cümlesi G08'de kullanılmadı).
> Q5 (tüm çekimler): `plume · smoke · drip · wet · bubbles` yok; Ishra'nın başlığındaki su plan gereği katı hâl ("constant visible water level"); silah şeritleri lamba şeridi.
> Q7 (tüm çekimler): her `Reference n` yalnız o tek görünüşte görüneni istiyor; alıcı çıkmış olduğundan alıcı istenmedi; Reference sırası = EKLE sırası (C92 dahil).
> Q8: model sesi AÇIK film; zıt iki istek yok. Kadraj dışı repliklerde kadrajdaki ağzın kapalı kalması olumlu yazıldı. Ishra ve Nith için ağız fiili yok (Ishra: plan C02 kalıbı + "Her face settles"; Nith: "The gold throat mesh goes still").

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C85 | 2 (K1 "one cyan triangular light" + K2 "beside it, a palm's width apart" = DURUM CÜMLELERİ; şeritler A12 cümlesi + yeri; Nith oturur C85+) · 4 · 6 (masada ekran yok) | Dönüş planın eylemi (birincil); 7-10 s'deki Silex/Nith ek hareketleri çıkarıldı; 2. deneme YEDEK iş emrinde |
| C86 | 2 (Vekh gövde cümlesi eklendi; blaster masada, kılıf cümlesi yok) · 4 · vuruş iskeleti 0-2/2-7/7-10, son vuruş beden hâli | Sağ şakak çıplak = plan C64 |
| C87 | 2 · 5 (ağız fiili kalktı: plan C02 kalıbı) · vuruş 0-5/5-8/8-10 · replik 4.4 s | Ağız suyun içinden: kare kapısı (SK4) |
| C88 | 2 ("its" → "Silex's", zamir yok) · vuruş 0-4.5/4.5-10, "finishes by about 8.2 s" | İki cümle iki vuruşta |
| C89 | 2 · vuruş 0-5/5-10, "finishes by about 8.6 s" | "weapons" model sesinde (red gelirse kayda) |
| C90 | 2 (dış plan tarafı frame-left/frame-right) · vuruş 0-2/2-6/6-10, son vuruş formasyon açılır | Silah şeritleri 1080p'de seçiliyor mu: kare kapısı |
| C91 | 2 · 4 · plan "Çok geniş" korundu, C90'dan farklı açı (yüksekten koridor boyu) · koridor açık başlar, durum geri sarılmaz | Küçük gemilerin geçişi planın eylemi |
| C92 | 2 (Reference sırası = EKLE; Nem arkadan A01 "without human ears or hair") · 5 ("His mouth closes" → "The gold throat mesh goes still") · vuruş 0-3/3-6/6-10 | Nem'in referansı tek görünüşlü, arka görünüş metinle |
| C93 | 2 (Nem "Her right temple is bare."; Ishra oturur, Nem göz hizasına iner) · 4 (cam "glows beyond the table") · 5 (Ishra ağız fiili kalktı) · vuruş 0-3/3-6/6-10 | Profil yüz çizgisi kare kapısı |
| C94 | 2 · 4 (kamera yakın uçtan cama, cam masanın ötesinde, ışık omuzları kenarlıyor) · vuruş 0-4/4-7/7-10 | Diğer dördü masanın karşı yanında küçük/flu (plan) |
| C95 | 2 (Vekh gövde cümlesi eklendi) · vuruş 0-3/3-8/8-10, son vuruş bakış kayar | "fire" model sesinde (red gelirse kayda) |
| C96 | 2 (istasyon "small in the lower right third"; kırmızı frame-left, beyaz-teal frame-right) · vuruş 0-4/4-7/7-10, son vuruş küçük gemiler koridorun sonuna varır | Nem VO kurguda |
