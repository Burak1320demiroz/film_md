# 🖼️ BLACK_ACCORD — Prompt grubu G07 (çekimler C73–C84 · bölüm B7 TEK SESİN SONU) · tur 1

> Yazan: goruntu-yonetmeni (faz 5, tur 1, G07). Kaynak: `BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md` (sahip planı; "plandan asla dışarı çıkma") + `NOTLAR.md` KARARLAR (18.10.2026) + `PROMPTLAR/G01.md` (tur 1c) kalıbı + `ODA/F5_fable_birlestirme_1_G01.md` kararları.
> **Plan C73-C84 için promptsuzdur:** yalnız plan malzemesi kullanıldı: planın çekim cümlesi · A01-A13 İngilizce kimlik cümleleri (G01 KİMLİK CÜMLELERİ tablosundan kelime kelime) · plan kadraj kelimeleri · stil cümlesi · sabit oturma düzeni · nesne durumu (A10-A13) · §5 replikler. Objektif mm yok. Referans anahtarı rolleri G01 ROL SÖZLÜĞÜ'nden (1 clerk · 2 military envoy · 4 mineral envoy · 5 trade consul · 6 station host · 7 chamber).
> Ortak görünüm cümlesi her Görsel'in sonunda (plan); video promptlarına eklenmez (G01 ile aynı, NOTLAR KARARLAR). Mekân ışığı ve ortam sesi G01'deki SALON cümleleri. Model sesi AÇIK: replikler `: <line>` biçiminde, ikinci replik (kadraj dışı) videoya yazılmaz; o sırada kadrajdaki konuşmacının ağzı kapalıdır.
> **Başlangıç durumu (plan nesne devamlılığı, C73'te):** Nem · Vekh · Ishra · Silex · Orun alıcıları çıkmış, masada; Nith'inki takılı. Blaster Vekh'in sağ kalçasında değil, masada (C68'den beri); Vekh'te kılıf cümlesi yazılmaz. Nith ayakta (C65'ten beri), Nem ayakta (C06'dan beri). K1 C10-C74 Orun'un koltuğunun önünde; C75'te ışığı açılır; C78'de masanın merkezine gider; **cyan yayın ışığı C79'da** (plan A10 "C78 sonrası": pilot C79'un sınadığı "yayın durumuna geçiş"; C78 K1'i merkezde amber ışıkla bitirir, C79 amberle başlar cyanla biter, C80-C84 cyan). K2 C82'de K1'in yanına gelir.
> **Plan pilotu C79** (plan: "C79 küçük sabit nesnenin yayın durumuna geçmesini sınar"): Flow iş emrinde referanslardan, C01 ve C61'den hemen sonra üretilir.
> Prompt gövdesine çekim kodu, referans kodu (K1, K2, A10), başlık satırı, "Clip n of N" yazılmaz. Her blok ≤4.300 karakter.

---

## C73 — Nith hattı kesiyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C73.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: T06 okunacak ekran yok: "dış aktarımı kapatmak" = masaya gömülü basit fiziksel kumandaya basmak, küçük soluk lamba söner (A07 "simple physical controls"). Plan: salonun yaşam sistemi ve yörüngesi normal kalır → ışık ve cam görüntüsü sabit. Nith ayakta. R133 Nith (1,0 s, ~3,4'te biter); R134 Vekh kadraj dışı, kurguda. Plan sessizlik (C73) müzik katmanında, kurguda.

### Görsel
```text
Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 7 (chamber): take the far ivory-black head chair, the panoramic window and the room geometry from it. Medium view of Nith standing upright behind the far ivory-black head chair, seen from the near left corner of the table. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. His right hand hovers just above a simple physical control built into the table edge in front of him, a small pale lamp lit beside it; his left arm hangs at his side. One rigid black hexagonal table stands before the broad panoramic curved window behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push from the table corner toward Nith as his right hand lowers onto the simple physical control; at about 1 s he speaks calmly through his gold throat mesh in a smooth low male voice: No uncertified message leaves my station. 3-7 s: He finishes by about 3.5 s and his mouth closes; the small pale lamp beside the control goes dark under his hand while the room lights and the black-hole view behind him hold steady. Only Nith speaks in this shot. 7-10 s: His hand lifts from the control, his ice-blue eyes turn slowly toward frame-left and the push eases closer, the brow ridge and crest remaining fixed. Sound: quiet chamber ventilation and distant table resonance.
```

## C74 — Kendi kaydı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C74.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "yeni cihaz aramak yerine Orun'un mevcut küpüne döner" → K1 kadrajda, zaten masada (C10'dan beri), Orun'un koltuğunun önünde; Nem küpe yalnız bakar, eller kadraj altında (kapma yok, T01 yok). Alıcısı çıkmış (sağ şakak çıplak). R135 Nem (1,0 s, ~4,6'da biter). K1 yanındaki gümüş şerit = Orun'un alıcısı (C69).

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Close three-quarter view of Nem standing at her near position, seen from slightly to her right front across the black hexagonal table, her head turned toward frame-right. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. Two arms, stable upright proportions, delicate but practical hands, resting on the table edge below the crop. Her eyes are fixed on the table at frame-right, where a single palm-sized black octagonal body with one pale amber triangular light rests on the table surface, and beside it lies a single thin silver strip, a translation receiver and not a life-support part. Behind her stand the smaller pewter clerk chair and the dark stone-metal ribs. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-5 s: The camera begins a slow push as Nem's head and eyes move from the far end of the table to the black octagonal body at frame-right; at about 1 s she speaks in a precise steady adult female voice: You never use his network for your own accounts. She finishes by about 4.6 s with her eyes fixed on it. 5-8 s: Her mouth closes; the pale amber triangular light stays unchanged and her shoulders settle a fraction. Only Nem speaks in this shot. 8-10 s: The push eases closer while the gold side light moves across her cheek ridges. Sound: quiet chamber ventilation and distant table resonance.
```

## C75 — Bağımsız hat

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C75.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K1 özel kanal ışığı açılır (A10, T01 + T09).** Tek parmak ucu K1'in üstüne değer (kavrama yok); ışık soluk amberden daha parlak, sabit sıcak amber olur (cyan değil; cyan C79). YEDEK (planın kendi çözümü: "karmaşık parmak hareketi gerekirse kesmeyle sadeleşir"): kare K1'i parlak ışıkla gösterir, video yalnız kamera + konuşma. Kare kapısı: parmak + gövde ayrılıyor mu. R136 Orun (1,0 s, ~4,4'te biter); R137 Silex kadraj dışı, kurguda. Orun'un alıcısı K1'in yanında (C69).

### Görsel
```text
Reference 5 (trade consul): take his face and coat from it. Reference 7 (chamber): take the ochre-brown chair position, the table and the room geometry from it. Close three-quarter portrait of Orun seated at the ochre-brown chair position behind the black hexagonal table, seen from the front with his right temple toward the camera. Orun is an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. His right temple is bare. Two arms, substantial but not exaggerated build. On the table in front of his seat rests a single palm-sized black octagonal body with one pale amber triangular light, and beside it lies a single thin silver strip, a translation receiver and not a life-support part. His right forearm rests on the table and the index finger of his open right hand is raised a finger's width above the top of the black octagonal body. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle drift toward Orun as his raised right index fingertip lowers onto the top of the black octagonal body and touches it; the pale amber triangular light swells to a brighter steady amber; at about 1 s he speaks in a husky baritone voice, quick and polished, with dry humour: Would you? My relay reaches my ships directly. 3-6 s: The fingertip lifts away and his hand returns to the table beside it while the amber light stays steady; he finishes by about 4.4 s. Only Orun speaks in this shot. 6-8 s: His mouth closes and his amber eyes lift from the black octagonal body toward frame-left. 8-10 s: The drift eases closer and the gold light edges his bark-like facial plates. Sound: quiet chamber ventilation and distant table resonance.
```

## C76 — Paranın yolu

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C76.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: İki yüzlü plan (SK1 varsayılanı): model sesi yalnız Nem (R138, 1,0 s, ~5,0'da biter); Orun arkadan ve flu, yanıtı R139 kadraj dışı, kurguda. Nem küpü kapmaz: eller masa kenarında, kadraj altında. Referans 5 yalnız Orun'un ceketi için. Kare kapısı: Orun'un arkası kimlik (ceket) tutuyor mu.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 5 (trade consul): take his coat from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Over-the-shoulder two-shot along the black hexagonal table. In the left foreground, slightly out of focus, Orun sits at the ochre-brown chair position, seen from behind. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. Two arms, substantial but not exaggerated build. On the table beside his sleeve rests a single palm-sized black octagonal body with one pale amber triangular light. At frame-right, in sharp focus, Nem stands at her near position facing the camera in three-quarter view, her eyes fixed on Orun. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. Her hands rest on the table edge below the crop. Behind her stand the smaller pewter clerk chair and the dark stone-metal ribs. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold light from the camera side and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-5 s: The camera begins a gentle drift over Orun's shoulder toward Nem; at about 1 s she speaks in a precise steady adult female voice: Then let the truth travel the way your money does. Her chin lifts slightly, her eyes stay on Orun and her hands stay on the table edge; she finishes by about 5 s. 5-7 s: Her mouth closes; Orun's shoulders draw back a little in the soft foreground while the pale amber light beside his sleeve stays steady. Only Nem speaks in this shot. 7-10 s: The drift continues and eases closer to Nem, whose eyes stay level as the gold light moves across her cheek ridges. Sound: quiet chamber ventilation and distant table resonance.
```

## C77 — Risk Orun'da

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C77.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Nith ayakta, eller masa kenarında kadraj altında (jest yok, T01 yok). C73 ve C80'den farklı kadraj: önden, göz hizasının altından. R140 Nith (1,0 s, ~5,4'te biter); R141 Nem kadraj dışı, kurguda.

### Görsel
```text
Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 7 (chamber): take the far ivory-black head chair, the panoramic window and the room geometry from it. Close portrait of Nith standing behind the far ivory-black head chair, seen from the front slightly below eye level. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. His ice-blue eyes look down the table toward frame-left, both hands resting on the table edge below the crop. The broad panoramic curved window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-6 s: The camera begins a slow push toward Nith as he leans a fraction forward over the table; at about 1 s he speaks calmly through his gold throat mesh in a smooth low male voice: Open that channel and every protected contract you own is gone. He finishes by about 5.4 s with his ice-blue eyes level. 6-8 s: His mouth closes and his chin lifts slightly; the brow ridge and crest remain fixed. Only Nith speaks in this shot. 8-10 s: The push eases closer while a controlled gold reflection edges one side of his face. Sound: quiet chamber ventilation and distant table resonance.
```

## C78 — Açık karar

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C78.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K1 masanın merkezine itilir (A10, T01).** Avuç K1'in yan yüzüne yaslı, kavrama yok; K1 masa yüzeyinde kayar, durur; ışık amber kalır (cyan C79'da). YEDEK (planın çözümü): kare K1'i merkezde gösterir, video yalnız kamera + konuşma. Kare kapısı: avuç + gövde ayrılıyor mu. R142 Orun (1,0 s, ~4,6'da biter); R143 Ishra kadraj dışı, kurguda.

### Görsel
```text
Reference 5 (trade consul): take his face and coat from it. Reference 7 (chamber): take the ochre-brown chair position, the table and the room geometry from it. Close three-quarter portrait of Orun seated at the ochre-brown chair position behind the black hexagonal table, seen from his right front, his face turned toward frame-left where the table centre lies. Orun is an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. His right temple is bare. Two arms, substantial but not exaggerated build. On the table in front of his seat rests a single palm-sized black octagonal body with one pale amber triangular light, and his open right palm lies flat against its side. A single thin silver strip, a translation receiver and not a life-support part, lies beside it. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a gentle drift as Orun's open right palm pushes the black octagonal body smoothly along the table surface away from his seat toward frame-left; at about 1 s he speaks in a husky baritone voice, quick and polished, with dry humour: Then I will finally own something I didn't buy. 4-7 s: The black octagonal body slides to the centre of the table and stops, its pale amber triangular light still lit; his palm withdraws to the table edge and he finishes by about 4.6 s. Only Orun speaks in this shot. 7-10 s: His mouth closes, his amber eyes follow the black octagonal body and the drift eases closer, the gold light edging his coat collar. Sound: quiet chamber ventilation and distant table resonance.
```

## C79 — Kaynak yayında (PLAN PİLOTU)

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C79.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **Plan pilotu** ("küçük sabit nesnenin yayın durumuna geçmesini sınar"). Tek değişen şey K1'in üçgen ışığı: soluk amber → cyan, şekil ve gövde sabit (T09); ekran yok (T06). Eller kadraj altında. Nem'in ağzı kadrajda (R144, 1,0 s, ~4,2'de biter); R145 Silex kadraj dışı, kurguda. Işık: kamera tarafından (C11 ile aynı kamera yönü, karşı uçtan; cam kameranın arkasında, yazılmaz). Pilot sorusu: PİLOT'ta değil; kare kapısı: K1 gövdesi kenar bozulması, ışığın tek ve üçgen kalması.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Low close view across the black hexagonal table from its far side. In the foreground at the centre of the table, sharply focused, rests a single palm-sized black octagonal body with one pale amber triangular light. Behind it Nem stands at her near position, her upper body and face softly focused but readable, her head level and her eyes on the camera. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. Her hands rest on the table edge below the crop. Behind her stand the smaller pewter clerk chair and the dark stone-metal ribs. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold light from the camera side and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push toward the black octagonal body and Nem; at about 1 s she speaks in a precise steady adult female voice: Original voices. Original faces. No substituted lines. As she begins, the single triangular light on the black octagonal body changes from pale amber to cyan, keeping its triangular shape. 3-7 s: The cyan light holds steady and a faint cyan reflection settles on the black table surface around the body; she finishes by about 4.2 s and her mouth closes. Only Nem speaks in this shot. 7-10 s: The push eases closer and the cyan glow edges her silver cheek ridges while her eyes stay level on the camera. Sound: quiet chamber ventilation and distant table resonance.
```

## C80 — Yalanın son savunması

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C80.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: BT §A "murderers" model sesi repliğinde → red gelirse R146 kayda (metin değişmez). Nith ayakta; C08 (sağ önden) ve C77 (önden alttan) kadrajlarından farklı: sol önden göz hizası. K1 cyan: gövde kadrajda değil, yalnız masa merkezinden gelen soluk cyan yansıma ceketin alt kenarında. R146 Nith (1,0 s, ~3,8'de biter); R147 Vekh kadraj dışı, kurguda.

### Görsel
```text
Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 7 (chamber): take the far ivory-black head chair, the panoramic window and the room geometry from it. Close three-quarter portrait of Nith standing behind the far ivory-black head chair, seen from his left front at eye level. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. His chin is slightly lowered and his ice-blue eyes look toward frame-right with cold composure; both hands rest on the table edge below the crop. A faint cyan glow from the table centre touches the lower edge of his ivory coat. The broad panoramic curved window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow lateral drift across Nith as his head turns a fraction toward frame-left; at about 1 s he speaks calmly through his gold throat mesh in a smooth low male voice: They won't trust murderers asking for peace. He finishes by about 3.8 s. 4-7 s: His mouth closes; his chin lifts slightly and his ice-blue eyes hold level while the faint cyan glow stays on the lower edge of his coat. Only Nith speaks in this shot. 7-10 s: The drift eases closer, the brow ridge and crest remaining fixed. Sound: quiet chamber ventilation and distant table resonance.
```

## C81 — Başlangıç

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C81.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: "Açık kayıt alanı" = masanın merkezi, K1 cyan ışıkla yumuşak odakta kare altında; ekran yok (T06). Nem ayakta; C74 ve C79'dan farklı kadraj: sağ önden, hafif yukarıdan. Eller kadraj altında. R148 Nem (1,0 s, ~3,8'de biter); R149 Orun kadraj dışı, kurguda.

### Görsel
```text
Reference 1 (clerk): take her face and coat from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Close three-quarter portrait of Nem standing at her near position, seen from her right front and slightly from above, looking down at the table centre. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. Her right temple is bare. Two arms, stable upright proportions, delicate but practical hands, resting on the table edge below the crop. At the bottom of the frame, softly focused, a single palm-sized black octagonal body with one cyan triangular light rests at the centre of the black hexagonal table. Behind her stand the smaller pewter clerk chair and the dark stone-metal ribs. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow push toward Nem as she looks down at the black octagonal body at the table centre; at about 1 s she speaks in a precise steady adult female voice: Then we begin with what we did. She finishes by about 3.8 s. 3-7 s: Her mouth closes; she lifts her gaze slowly from the table centre to the far end of the table and her shoulders square a fraction. Only Nem speaks in this shot. 7-10 s: The push eases closer and the cyan glow rests on her silver cheek ridges. Sound: quiet chamber ventilation and distant table resonance.
```

## C82 — Arşiv korunacak

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C82.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K2 K1'in yanına bırakılır (A11, T01).** Levha açık sağ avuçta başlar (C12 ile aynı yöntem), avuç iner, levha K1'in yanında masaya oturur, avuç kayar; K1 ve K2 birbirine dönüşmez, temas yok. YEDEK (planın çözümü): kare K2'yi K1'in yanında gösterir, video yalnız kamera + konuşma. Kare kapısı: el + levha ayrılıyor mu · levha kenarı ametist yüzden ayrışıyor mu · K2 ↔ K1 birbirinden ayrı mı. R150 Silex (1,0 s, ~5,6'da biter); R151 Nith kadraj dışı, kurguda. Silex'in alıcısı masada (C68), K2'nin yerinde.

### Görsel
```text
Reference 4 (mineral envoy): take its face, facets, mantle and receiver position from it. Reference 7 (chamber): take the pale silver-violet chair position, the table and the room geometry from it. Close three-quarter portrait of Silex seated behind the black hexagonal table at the pale silver-violet chair position, seen from the front with the right temple toward the camera. Silex is an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. The right temple is bare. Subtle internal violet translucency, restrained expression, no changing crystal growth. At frame-left, on the table a short reach from Silex's right hand, rests a single palm-sized black octagonal body with one cyan triangular light. Silex's right forearm extends from the pale-silver sleeve over the table, and on the open right palm, a hand's width above the table surface and a palm's width from the black octagonal body, rests a single flat frosted-purple pentagonal recording slab small enough to rest in one palm. A single thin silver strip, a translation receiver and not a life-support part, lies on the table in front of Silex's seat. The panoramic window curves behind and beside Silex. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle drift toward Silex as the open right palm, carrying the flat frosted-purple pentagonal recording slab, moves toward the black octagonal body and lowers; at about 1 s the narrow central mouth seam moves and Silex speaks in a clean, genderless voice with a light harmonic tone, calm and observant: My copy goes with the broadcast. No one deletes the source. 3-6 s: The palm lowers until the slab rests flat on the table surface beside the black octagonal body, a gap of a palm's width between them, and the palm slides away from it; Silex finishes by about 5.6 s. Only Silex speaks in this shot. 6-8 s: The hand withdraws to the table edge and the mouth seam closes. 8-10 s: The facets on the face catch the gold light and the cyan glow as the drift eases closer. Sound: quiet chamber ventilation and distant table resonance.
```

## C83 — Nith'in hamlesi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C83.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **Tek engelleme hareketi (plan), T01.** Nith'in kolu K1'e uzanır; Orun'un önkolu yolu kapatır, kol-kol teması yok (el kaynaşması riski). Kare kapısı: iki karakter kimliği (Orun ceket + yüz, Nith krest + boğaz ağı) · iki kol ayrı mı. İki yüz: model sesi yalnız Orun (R152, 1,0 s, ~3,8'de biter); Nith'in yanıtı R153 kadraj dışı, kurguda → Nith'in ağzı kapalı. K1 merkezde, cyan ışık. YEDEK (plan: "karmaşık el hareketi gerekirse kesmeyle sadeleşir"): kare engeli gösterir, video yalnız kamera + konuşma.

### Görsel
```text
Reference 5 (trade consul): take his face and coat from it. Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 7 (chamber): take the ochre-brown and ivory-black chair positions, the table and the room geometry from it. Medium two-shot from the near side of the black hexagonal table. At frame-left, Orun sits at the ochre-brown chair position in three-quarter profile facing frame-right. Orun is an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. His right temple is bare. Two arms, substantial but not exaggerated build. His right forearm rests on the table edge beside him. At frame-right of centre, Nith stands behind the far ivory-black head chair, his right arm just beginning to rise from his side toward the table centre. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. In the lower middle of the frame, at the centre of the table, rests a single palm-sized black octagonal body with one cyan triangular light. The broad panoramic curved window stands behind both of them. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow push as Nith's right arm extends across the table toward the black octagonal body; at about 1 s Orun speaks in a husky baritone voice, quick and polished, with dry humour: You don't get to edit this one. As he speaks, his right forearm rises from the table edge and sweeps across, stopping level between Nith's open hand and the black octagonal body without touching either; he finishes by about 3.8 s. 4-7 s: The forearm holds as a firm horizontal line and Nith's open hand halts short above the table; Orun's mouth closes. Only Orun speaks in this shot and Nith's mouth stays closed. 7-10 s: Nith's hand draws slowly back while his ice-blue eyes stay fixed on the black octagonal body and the push eases closer. Sound: quiet chamber ventilation and distant table resonance.
```

## C84 — Masaya dön

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C84.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Vekh masadaki silahı eline almaz (plan); blaster C68'den beri masada, Vekh'in boş koltuğunun önünde, kıpırdamaz; Vekh'in elleri açık ve boş, silahtan uzakta. Kılıf cümlesi yazılmaz (blaster masada). Nith kadrajda değil (kadraj dışı, frame-left); model sesi Vekh (R154, 1,0 s, ~4,4'te biter); R155 Nem kadraj dışı, kurguda. Kare kapısı: blaster kılıfta mı yoksa masada mı (masada olmalı), Vekh'in alıcısı yok.

### Görsel
```text
Reference 2 (military envoy): take his face and armour from it. Reference 7 (chamber): take the bronze-red chair position, the table and the room geometry from it. Medium view of Vekh standing upright beside the bronze-red chair, seen from across the table in three-quarter view, his amber eyes directed toward frame-left. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. His body is upright with two arms and two legs. He wears bronze formal military armour over dark-red clothing. His right temple is bare. Both of his hands hang open and empty at his sides. On the black table surface in front of the bronze-red chair, at frame-right in the foreground, lies a single compact dark blaster, motionless. At the centre of the table, behind it, rests a single palm-sized black octagonal body with one cyan triangular light. The broad panoramic curved window curves behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a slow lateral drift as Vekh takes one firm step out from his chair toward the table centre, his hands open and empty at his sides; at about 1 s he speaks in a low rough controlled voice: Sit down. You can answer for every word. He finishes by about 4.4 s. 4-7 s: He comes to rest between frame-left and the black octagonal body, squarely facing frame-left; the dark blaster stays motionless on the table behind him. Only Vekh speaks in this shot. 7-10 s: His shoulders square and his amber eyes hold on frame-left while the drift eases closer and the gold light moves along his bronze armour. Sound: quiet chamber ventilation and distant table resonance.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (G01 ile aynı):** Return silent videos **KAPALI** · Visible watermarking **KAPALI**.
> **Sıra notu:** C79 plan pilotudur: referanslar (G01 sıra 1-9) ve G01 C01, G06 C61'den **hemen sonra** üretilir (aşağıdaki 1-2). Pilot kararından sonra kalan G07 satırları. Kareler videodan önce, kare onaylanmadan video yok.
> Frames to Video'ya referans eklenmez (yalnız kare); referanslar yalnız kare üretiminde, kare promptunun sırasıyla yüklenir.
> **Kare kapısı (G07):** filigran/logo · istenmeyen yazı · el kaynaşması · yüz bozulması · kimlik kayması · **alıcılar çıkmış mı** (Nem · Vekh · Orun · Silex sağ şakağı çıplak, Nith'te takılı) · **blaster masada mı** (C84) · **K1 ışık durumu** (C73-C78 soluk amber/amber · C79 amber → cyan · C80-C84 cyan) · **parmak/avuç + gövde ayrılıyor mu** (C75 C78) · **el + levha ayrılıyor mu, K1-K2 ayrı mı** (C82) · **iki kol temasta değil mi** (C83) · ekranda okunacak yüzey yok (C73 C79).
> **Ses:** model sesi R133 · R135 · R136 · R138 · R140 · R142 · R144 · R146 · R148 · R150 · R152 · R154 (ağız kadrajda); kurguda R134 · R137 · R139 · R141 · R143 · R145 · R147 · R149 · R151 · R153 · R155. Şiddet kelimeli model sesi: C80 "murderers" (red gelirse R146 kayda).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C79 kare | `kare/C79.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) · **PLAN PİLOTU** (C01 ve C61'den sonra) | 2 | |
| 2 | C79 | `ham/C79_d1.mp4` | Frames to Video | kare/C79.png · **PLAN PİLOTU: K1 ışığı amber → cyan** | 2 | |
| 3 | C73 kare | `kare/C73.png` | Görsel | ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 4 | C74 kare | `kare/C74.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 5 | C75 kare | `kare/C75.png` | Görsel | ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 6 | C76 kare | `kare/C76.png` | Görsel | ref/1.NEM_v1.png · ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 7 | C77 kare | `kare/C77.png` | Görsel | ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 8 | C78 kare | `kare/C78.png` | Görsel | ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 9 | C80 kare | `kare/C80.png` | Görsel | ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 10 | C81 kare | `kare/C81.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 11 | C82 kare | `kare/C82.png` | Görsel | ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 12 | C83 kare | `kare/C83.png` | Görsel | ref/5.ORUN_v1.png · ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 13 | C84 kare | `kare/C84.png` | Görsel | ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 14 | C73 | `ham/C73_d1.mp4` | Frames to Video | kare/C73.png | 2 | |
| 15 | C74 | `ham/C74_d1.mp4` | Frames to Video | kare/C74.png | 2 | |
| 16 | C75 | `ham/C75_d1.mp4` | Frames to Video | kare/C75.png | 2 | |
| 17 | C76 | `ham/C76_d1.mp4` | Frames to Video | kare/C76.png | 2 | |
| 18 | C77 | `ham/C77_d1.mp4` | Frames to Video | kare/C77.png | 2 | |
| 19 | C78 | `ham/C78_d1.mp4` | Frames to Video | kare/C78.png | 2 | |
| 20 | C80 | `ham/C80_d1.mp4` | Frames to Video | kare/C80.png | 2 | |
| 21 | C81 | `ham/C81_d1.mp4` | Frames to Video | kare/C81.png | 2 | |
| 22 | C82 | `ham/C82_d1.mp4` | Frames to Video | kare/C82.png | 2 | |
| 23 | C83 | `ham/C83_d1.mp4` | Frames to Video | kare/C83.png | 2 | |
| 24 | C84 | `ham/C84_d1.mp4` | Frames to Video | kare/C84.png | 2 | |

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · tur 1 · G07)

> Q1: işaret yalnız Nem'de (A01 "one small cobalt throat light", ceket cümlesinde birebir) ve Nith/Silex/Orun/Vekh'te alıcı konumu: sağ şakak, çıkarıldığı için "right temple is bare" (Nith'te takılı, "at his right temple"). `the only marking` plan dışı (G01 kararı). Kolda işaret yok.
> Q3 (tüm çekimler): ORTAK GÖRÜNÜM "cold charcoal and pewter shadows, warm gold black-hole reflections" ışık/yansıma taşıyor → `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` G01'de not edildi; C73-C84'te su/gezegen/ses çelişkisi yok. C79-C84 cyan K1 yansıması "warm gold" ile aynı karede: cyan çok küçük, K1'den gelen lokal yansıma olarak yazıldı; sahip planı (A10).
> Q5 (tüm çekimler): `plume · smoke · drip · wet · bubbles` yok.
> Q6: ekran/gösterge adı yok; C73 "simple physical control" + "small pale lamp" (biçim); C79/C81 K1 ışığı üçgen lamba; yazı kilidi ortak görünüm cümlesindeki "without lettering".
> Q7 (tüm çekimler): her `Reference n` yalnız o tek görünüşte görüneni istiyor (yüz, giysi/zırh, koltuk, masa); alıcı ve K1/K2 sayfada yok / sayfada takılı olduğundan Reference cümleleri alıcıyı almıyor, alıcı durumu metinle yazıldı. C76'da Reference 5 yalnız ceket.
> Q8 (tüm çekimler): model sesi AÇIK film; "Sound:" ortam cümlesi G01 SALON cümlesi; ses kelimesi plan stilinde. Zıt iki istek yok.

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C73 | 4 (cam Nith'in arkasında yazılı) · 6 (kumanda + lamba biçimle) | Nith'te kolda işaret yok; alıcı takılı, birebir |
| C74 | 2 (Nem kimliği + K1 biçimi + A12 şerit) · 4 (Nem'in arkası: sandalye + kaburga) | Eller kadraj altında; cam kadrajda değil |
| C75 | 2 (K1 biçim + ölçü; A12 şerit) · 4 (cam Orun'un arkasında ve yanında) | Alıcı sağ şakakta çıplak; ışık "swells" soluk amber → parlak amber (cyan değil) |
| C76 | 2 (Orun arkadan: yalnız ceket + beden; Nem tam) · 4 (Nem'in arkası: sandalye + kaburga; Orun'un önü kameraya dönük değil) | SK1 varsayılanı; Orun yüz cümleleri yazılmadı (arkadan) |
| C77 | 4 (cam Nith'in arkasında) | Eller kadraj altında (jest yok) |
| C78 | 2 (K1 biçim + ölçü + taraf: Orun'un önünde, avuç yan yüze yaslı) · 4 | Kavrama yok; ışık amber (cyan C79) — FILM §2 S78 "cyan" satırı ile plan A10 "C78 sonrası" arasında Fable kararı bekler |
| C79 | 2 (K1 biçim + ölçü; Nem kimliği) · 4 (Nem'in arkası: sandalye + kaburga; cam kamera arkasında) · 6 (ekran yok, lamba) | Pilot: tek değişen K1 ışığı; amber → cyan |
| C80 | 4 (cam Nith'in arkasında) | Cyan K1 kadrajda değil; yalnız yansıma |
| C81 | 2 (K1 cyan, kadraj altında yumuşak odak) · 4 (Nem'in arkası: sandalye + kaburga) | Ekran yok; "açık kayıt alanı" = masa merkezi |
| C82 | 2 (K1 + K2 biçim + ölçü + taraf; A12 şerit; "mouth seam" M) · 4 (cam Silex'in arkasında ve yanında) | K2 avuçta başlar, kare "bırakılmış" hâli göstermez; K1-K2 aralık yazılı |
| C83 | 2 (Orun + Nith kimlik parçaları; K1 cyan) · 4 (cam ikisinin arkasında) | İki kol temasta değil (kaynaşma riski); Nith'in ağzı kapalı (SK1) |
| C84 | 2 (Vekh zırh cümlesi kılıfsız: blaster masada; blaster biçim + taraf) · 4 (cam arkasında) | Nith kadraj dışı; Reference 2 blaster kılıfı sağ kalçada gösterir, anahtar yalnız yüz ve zırhı istiyor |
