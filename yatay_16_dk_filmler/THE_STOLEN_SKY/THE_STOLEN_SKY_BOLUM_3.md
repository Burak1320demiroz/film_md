# 🎬 THE_STOLEN_SKY — BÖLÜM 3  (S24 – S35) · ALÇAKTAN GİT

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_STOLEN_SKY_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③). ⭐ self-contained ≠ Bible'ın
> tamamı — yalnız `IN FRAME:` satırındaki tarif edilir [D214].
>
> ⭐ **YENİ REJİM:** ilk satır `IN FRAME:` (㉖) · POZİTİF gövde IMAGE 100-250 / VIDEO 120-300 kelime (①) ·
> NEGATIVE = §5.1 çekirdek (image 7 · video 8) + ≤3 sahneye özel (㉗) · video tek satır `START FRAME:`.
> ⭐ **OMNI 1.1 Flash I2V katmanı:** CAMERA `In a single continuous shot.` ile biter · PHYSICS + AUDIO her klipte dolu · tırnak 0.
> ⭐ **Promptta `Scene n of 96` = S + 1.** Dönüş ve küme işaretleri de bu numarayı kullanır.
> ⭐ **VİZÖR TAMAMEN OPAK** (SAPMA 3) — `IN FRAME:` satırına `face` YAZILMAZ, D79 vizör cümlesi HİÇ girmez.
> ⭐ **KÜME (Z) klipleri:** imaj promptu önceki klibin SON KARESİNİ tarif eder; üretimde OMNI zincirine
>   gerçek son kare verilir, imaj promptu yalnız yedek/animatik içindir (Z: S13 S35 S37 S41 S48 S49 S72 S74 S82 S90).
> ⭐ **YÖN NESNE-GÖRELİ** [D174]: pusula ve ekran koordinatı yok — halka/kafes konumu kadrajdaki nesneye göre yazılır.
> ⛔ İnsansız sahnelerde NEGATIVE kısadır (<900 karakter) ve "no human figures" kalıbı YAZILMAZ [KART 10].
> ⛔ Replikler klipte ÜRETİLMEZ (post-dub, 8 replik); saniyesi sahne bilgi bloğunda, promptta değil.
> ⛔ Silah ADLANDIRILMAZ (short tool · long tool · a short burst of four bright points); kan · yara · ceset 0 kelime [KART 12].
>
> Bölüm sınırı ardışık bir çifttir: S35 (O · MLS · from behind) ↔ S36 (F · MLS · eye level) · açı tipi değişir ✅
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_16_dk_filmler/THE_STOLEN_SKY`

---
## 🎬 SAHNE 24 — DAR UÇUŞ YOLU

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 4:00,0 · VURUŞ: İSTEK — alçak koridor, iki bilezik sağlam (PART 2 açılışı) · SEK07
KURULUM: H · ilk kullanım · 28mm · MLS · rear-quarter tracking · IN FRAME: back (craft tail) · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: back (craft tail)
Scene 25 of 96.
The assault boat flies level between a steel pipe run and a black rock face with both rear thrust rings whole and turning, the amber lattice above the corridor and the ring's light lying on the rock face ahead.

From behind and a little to one side of a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing down a narrow corridor that runs between a stack of steel pipes on one side and a sheer black basalt face on the other; both thrust rings whole and turning at the same speed, the tail one continuous flat surface carrying only the two rings. The corridor narrows ahead and bends. Above it high in the sky a wide amber lattice of straight lines spaced no wider than two ship-lengths; the ring's light lies as a pale band on the rock face ahead.
LIGHT: amber from the lattice above, a paler band of ring light on the rock face, the hull's white-blue lamp and the two rings the brightest points.
CAMERA: medium long tracking shot from behind and slightly to one side of the craft, 28mm spherical lens, camera at hull height 8.0 m behind the craft, the camera keeps pace with it. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The boat touches neither the pipes nor the rock, no sparks, no scrape.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: back (craft tail)
Scene 25 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The boat accelerates so that the pipe shadows cross its hull faster each second, the corridor closes in on both flanks, and at the bend the boat banks to follow it without touching either side.
The craft's tail is one continuous flat surface carrying only its engine rings.

TIMELINE: 0.0s — the boat level in the corridor, both rings turning. 2.0s — the rings brighten and the boat draws ahead, the pipe shadows crossing its hull faster. 4.0s — the pipe stack and the rock face close to within a hull-width on each flank. 6.5s — the corridor bends; the boat banks, one wing tip dipping, and follows the bend. 9.0s — the boat level again beyond the bend, the walls still close, the rings still turning at the same speed.

CAMERA: medium long tracking shot from behind and slightly to one side of the craft, 28mm spherical lens, camera at hull height 8.0 m behind the craft, the camera keeps pace with it. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. two thrust rings at one steady pitch, wind tearing past the pipes, no impacts. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The boat touches neither the pipes nor the rock, no sparks, no scrape.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 25 — TAKİPÇİLER

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 4:10,0 · VURUŞ: HASIM — kıskaç kurulur (tam olarak iki avcı) · SEK07
KURULUM: E · dönüş S19 · 24mm · WS · high angle (slight) · lockoff · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 26 of 96.
Exactly two curved fighters descend from above the corridor, one behind the boxy boat and one ahead of it, both still higher than the boat, and the boat flies level between them.

Wide from slightly above the corridor. In the centre a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing along the corridor, level. Above and behind it one a curved seamless Veyra fighter with an amber-lit edge, nose pointing the same way; above and ahead a second identical fighter, nose pointing the same way, both descending. Steel pipes on one flank, black rock on the other; above everything high in the sky a wide amber lattice of straight lines spaced no wider than two ship-lengths; the ring small above the rock's crest.
LIGHT: amber from the lattice above, the fighters' amber edges bright, the boat's white-blue lamp cold.
CAMERA: wide shot, 24mm spherical lens, high angle, camera slightly above head height at 2.2 m on a fixed locked-off tripod, 7.0 m from the nearest subject, absolutely zero camera movement. — the same position, height and lens as Scene 20. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly two fighters, no third craft appears at any point.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 26 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The rear fighter settles behind the boat, the front fighter overtakes and drops into the corridor ahead, then turns in place until its nose points back at the boat and the corridor is blocked.

TIMELINE: 0.0s — both fighters descending, the boat level between them. 2.0s — the rear fighter levels off two hull-lengths behind the boat and holds there. 3.5s — the front fighter passes over the boat and drops into the corridor four hull-lengths ahead. 6.0s — the front fighter turns in place, its nose swinging round until it points straight back at the boat, its curved hull filling the corridor. 8.5s — it hangs there, nose to the boat, the rear fighter holding behind; the boat still level between them.

CAMERA: wide shot, 24mm spherical lens, high angle, camera slightly above head height at 2.2 m on a fixed locked-off tripod, 7.0 m from the nearest subject, absolutely zero camera movement. — the same position, height and lens as Scene 20. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. the boat's two rings, and over them a second engine tone, lower and continuous, from the fighters. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly two fighters, no third craft appears at any point.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 26 — ÖNÜ KAPALI

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 4:20,0 · VURUŞ: ENGEL — atış avcının kalkanında sapar, hendeğe dalış · SEK07
KURULUM: G · dönüş S14 · 24mm · MLS · cabin rear · craft-fixed · IN FRAME: torso, hands (seated) · HACİM: KABIN · İNSAN: 1 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: torso, hands (seated)
Scene 27 of 96.
Through the flat forward pane a curved fighter hangs nose-on to the boat blocking the corridor, the convex face of its amber shield toward the boat, and below the pane's lower edge the dark mouth of a service trench opens in the corridor floor.

From the rear of the cabin. In the front-left seat a burnt-orange hard-shell torso with white bands on both upper arms, a squared helmet with one flat pane, fully opaque matte black, in a thick dark rim, gloves on the two control grips. Through the flat forward pane, four hull-lengths ahead, a curved seamless Veyra fighter with an amber-lit edge hangs nose-on to the boat, a curved amber shield face on its front with its convex side to the boat. Below the pane's lower edge a dark squared trench mouth opens in the corridor floor. Steel pipes and black rock pass on either side.
LIGHT: cold blue-white cabin lamps, amber through the pane from the fighter's shield face, the grips lit flat.
CAMERA: medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves. — the same position, height and lens as Scene 15. In a single continuous shot.
NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The fighter is not hit and does not vanish, it stays whole above the trench.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: torso, hands (seated)
Scene 27 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
Four bright points leave the boat's nose, meet the shield face-on and glance off into the rock in under half a second, then the orange gloves push both grips forward and the pane's horizon slides up as the boat dives into the trench mouth.

TIMELINE: 0.0s — the fighter nose-on in the pane, the gloves on the grips. 1.5s — a short burst of four bright points leaves the boat's nose and crosses the gap. 2.0s — the four points meet the shield face-on and glance off into the rock face, no glow lingering; the fighter has not moved. 4.5s — the orange gloves push both grips forward, the forearms tightening; the pane's horizon slides up. 6.5s — the trench mouth rises to fill the pane, dark sides closing in; one cold warning lamp on the panel lights, unmarked. 9.0s — the pane shows only trench and a strip of sky, the fighter gone above.

CAMERA: medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves. — the same position, height and lens as Scene 15. In a single continuous shot.
PHYSICS: Gravity is 0.9 g inside a cabin pressurised at one atmosphere; loose objects fall fast and settle within two seconds, nothing hangs in the air.
AUDIO: A steady cabin hum and breathing inside the helmets, exterior sound muffled. four sharp cracks, a glancing clatter, then the cabin hum climbing as the boat dives, one soft warning tone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The fighter is not hit and does not vanish, it stays whole above the trench.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 27 — DAR HENDEĞE DALIŞ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 4:30,0 · VURUŞ: HASIM — avcı üstte kalır, hendek ağzı parçalanır · SEK07
KURULUM: N · ilk kullanım · 28mm · MS · low angle · fixed · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 28 of 96.
The boxy boat is already half inside the trench mouth under a steel pipe bridge, and the curved fighter, wider than the trench mouth, hangs above it and cannot follow.

Low at ground height beside the trench. In the lower half a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing into the trench, its rear half still outside under a bridge of steel pipes that spans the mouth. In the upper half a curved seamless Veyra fighter with an amber-lit edge, nose pointing down at the mouth, its curved hull clearly wider than the opening. Black basalt on both sides; the lattice a band across the top edge of frame.
LIGHT: amber from the lattice band above, the fighter's edge bright, the trench interior dark, the boat's rings lit cold.
CAMERA: medium shot, 28mm spherical lens, low angle, camera low at ground height on a fixed tripod, 12 m from the craft, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The fighter never enters the trench and never shrinks, it stays wider than the mouth.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 28 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The boat slides fully into the trench, the fighter fires down at the mouth and the steel lip breaks into pieces that fall straight down into the trench, and the fighter stays above, too wide to enter.

TIMELINE: 0.0s — the boat half in, the fighter above. 1.5s — the boat slides the rest of the way in, the rings disappearing under the pipe bridge. 3.0s — three bright points leave the fighter's nose and strike the steel lip of the mouth; sparks and torn plate fall straight down into the trench. 5.5s — a second group of three points; a section of the pipe bridge bends and a fragment drops. 8.0s — the fighter holds above the mouth, nose down, not entering; small pieces still settling. 9.5s — the mouth still, the fighter still above it.

CAMERA: medium shot, 28mm spherical lens, low angle, camera low at ground height on a fixed tripod, 12 m from the craft, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. two groups of three heavy cracks, steel tearing, fragments ringing on the trench floor, the fighter's low engine tone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The fighter never enters the trench and never shrinks, it stays wider than the mouth.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 28 — DÜŞEN BORU

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 4:40,0 · VURUŞ: ENGEL — kopma, düşüş ve kaçınma aynı klipte · SEK07
KURULUM: X · ilk kullanım · 35mm · MS · front-low · rising · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 29 of 96.
Inside the covered trench a large service pipe crosses the ceiling ahead of the boat with its bracket already sparking, and the pipe has not yet moved.

From the front lower quarter of a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing down the trench, both thrust rings turning. The trench is covered: steel ribs overhead, black basalt sides. Ahead a service pipe as thick as the boat's hull crosses the ceiling on two brackets; one bracket is sparking, sparks falling straight down. Beyond the pipe the trench continues into darkness.
LIGHT: the boat's white-blue lamp and rings lighting the ribs from below, the bracket's sparks the brightest point, no sky light.
CAMERA: medium shot tracking upward from the front lower quarter of the craft, 35mm spherical lens, low angle, camera 10 m ahead of and below the craft, the camera rises with it. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The pipe falls by swinging on its far bracket, it does not vanish and does not float.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 29 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The sparking bracket parts, one end of the pipe drops and swings down across the trench, the boat banks hard and passes under the falling end with a hull-width to spare, and the pipe end hits the floor behind it.

TIMELINE: 0.0s — the bracket sparking, the pipe still fixed. 1.5s — the bracket parts; the near end of the pipe drops and begins to swing down across the trench on its far bracket. 3.0s — the boat banks hard, one wing tip down, and drives under the swinging pipe end with a hull-width to spare, the camera rising with it. 5.0s — the boat is past; the pipe end reaches the floor behind it with a heavy impact, dust rising and thinning. 7.5s — the boat levels, both rings turning, the trench ahead clear. 9.5s — the boat still level, the fallen pipe a dark bar far behind.

CAMERA: medium shot tracking upward from the front lower quarter of the craft, 35mm spherical lens, low angle, camera 10 m ahead of and below the craft, the camera rises with it. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. a bracket snapping, a long metal swing, a heavy impact behind, the two rings steady. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The pipe falls by swinging on its far bracket, it does not vanish and does not float.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 29 — SAĞ TARAFTAKİ HASAR

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 4:50,0 · VURUŞ: BEDEL (araç) — sağ bilezik eğilir (kalıcı hasar doğar) · SEK08
KURULUM: W · dönüş S17 · 35mm · MS · profile · short side track · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 30 of 96.
In profile the boat leaves the trench with its right thrust ring whole and turning, and a curved fighter hangs above it with its nose pointed down at the ring.

In profile at hull height: a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing along the corridor as it climbs out of the trench mouth, the right thrust ring nearest the camera, whole and turning. Above it a curved seamless Veyra fighter with an amber-lit edge, nose pointing down at the ring. Black basalt below, steel pipes behind; the lattice a band across the top of frame, the ring's light above the fighter.
LIGHT: amber from the lattice band above, the fighter's edge bright, the right thrust ring lit by its own cold glow.
CAMERA: medium shot, 35mm spherical lens, profile, camera at chest height, 2.5 m from the subject, a short sideways track that settles and holds. — the same position, height and lens as Scene 18. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The engine does not stop and nothing explodes, the ring only bends and the boat only yaws.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 30 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
One bright point from the fighter strikes the right thrust ring, the ring bends out of line and stops turning while its exhaust now points sideways, and the boat yaws to the right and keeps yawing without correcting, all in one short sideways track that settles and holds.

TIMELINE: 0.0s — the ring whole and turning, the fighter above; the camera sliding sideways with the boat. 1.5s — one bright point leaves the fighter's nose and strikes the right thrust ring; sparks and a piece of the ring's rim fall straight down. 2.5s — the ring bends out of line and stops turning, its exhaust now pointing sideways; the camera settles and holds. 4.0s — the boat yaws to the right, its nose swinging away from the corridor line. 6.5s — the yaw continues, the left ring still turning, the bent right ring fixed at its new angle. 9.5s — the boat still drifting right, uncorrected.

CAMERA: medium shot, 35mm spherical lens, profile, camera at chest height, 2.5 m from the subject, a short sideways track that settles and holds. — the same position, height and lens as Scene 18. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. one heavy crack, a metal shriek, and from then on a new grinding note from the bent ring under the engine tone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The engine does not stop and nothing explodes, the ring only bends and the boat only yaws.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 30 — ASİMETRİK KONTROL

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 5:00,0 · VURUŞ: BEDEL (araç) — savrulma durur, kabin sağa eğik kalır · SEK08
KURULUM: G · dönüş S26 · 24mm · MLS · cabin rear · craft-fixed · IN FRAME: torso, hands (seated) · HACİM: KABIN · İNSAN: 4 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: torso, hands (seated)
Scene 31 of 96.
The whole cabin is tilted to the right with four seated torsos leaning the same way, the pilot's gloves on the two grips, the graphite gunner in the rear-right seat.

From the rear of the cabin, the frame tilted to the right. Front-left seat: a burnt-orange hard-shell suit with white bands on both upper arms, gloves on the two grips. Front-right seat: an off-white hard-shell suit with teal forearms and a flat rectangular module frame on the back, both gloves on a hold bar. Rear-left seat: a dark cobalt hard-shell suit with a pale grey mark on the left shoulder plate with a long pale scrape across the left chest plate, one glove on a hold bar. Rear-right seat: a graphite-grey hard-shell suit with broad mustard chest plates and a long dark tool pressed against the seat frame; every helmet squared with one flat pane, fully opaque matte black, in a thick dark rim. Through the pane the corridor sliding sideways, tilted.
LIGHT: cold blue-white cabin lamps, a strip of amber through the pane, one cold warning lamp on the panel.
CAMERA: medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves. — the same position, height and lens as Scene 27. In a single continuous shot.
NEGATIVE: Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The cabin never returns fully to level, the slight right lean remains at the end.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: torso, hands (seated)
Scene 31 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The pilot's left glove pushes the left grip forward and the right glove rolls the other grip, the tilt eases from steep to slight over four seconds and stops there, and the four torsos settle at the same slight lean without straightening fully.

TIMELINE: 0.0s — the cabin tilted right, four torsos leaning right. 1.0s — the pilot's left glove pushes the left grip forward, the forearm tightening; the right glove rolls the other grip. 3.0s — the tilt eases; the corridor in the pane slides back toward level but stops short. 5.0s — the tilt settles at a slight right lean and holds; the warning lamp stays lit. 6.5s — the four torsos settle at the same slight lean, gloves easing on the hold bars, the gunner's tool still pressed to the seat frame. 9.5s — the cabin steady at its slight lean.

CAMERA: medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves. — the same position, height and lens as Scene 27. In a single continuous shot.
PHYSICS: Gravity is 0.9 g inside a cabin pressurised at one atmosphere; loose objects fall fast and settle within two seconds, nothing hangs in the air.
AUDIO: A steady cabin hum and breathing inside the helmets, exterior sound muffled. the grinding note of the bent ring under the engine, one warning tone, four breathing rhythms inside the helmets. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The cabin never returns fully to level, the slight right lean remains at the end.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 31 — SERVİS HAVUZUNA İNİŞ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 5:10,0 · VURUŞ: İSTEK — çatılı havuza sürtünerek iniş · SEK08
KURULUM: N · dönüş S27 · 28mm · MS · low angle · fixed · IN FRAME: none · HACİM: YUZEY→IC · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 32 of 96.
The boat comes in tilted to the right under the flat roof of a dry service pit at the tower's base, its bent right thrust ring visible, and it has not yet touched the floor.

Low at ground height across a dry service pit walled in black basalt at the base of the tower, a flat roof of steel plate over it. a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing into the pit, tilted to the right, its right thrust ring bent out of line and still, the left ring turning; it is a hull-height above the pit floor, under the roof's edge. Beyond the pit the tower's base wall, and above the roof's edge a strip of amber lattice.
LIGHT: amber daylight from the open side of the pit, the roof's shadow over most of the space below, the boat's rings and lamp cold.
CAMERA: medium shot, 28mm spherical lens, low angle, camera low at ground height on a fixed tripod, 12 m from the craft, absolutely zero camera movement. — the same position, height and lens as Scene 28. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The boat stays whole, the skid grinds and nothing breaks off.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 32 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The boat drops the last hull-height, its landing skid grinds along the metal floor throwing sparks that fall straight down, it slides two hull-lengths and stops crooked, and the dust it raised settles within two seconds.

TIMELINE: 0.0s — the boat a hull-height above the floor, tilted right. 1.5s — it drops; the right skid touches first and grinds along the metal, sparks falling straight down. 3.5s — the left skid comes down; the boat slides forward two hull-lengths, shedding speed, still crooked. 6.0s — it stops crooked; the left ring winds down; dust rises off the floor and settles within two seconds. 8.0s — the boat sits still, the bent right ring fixed, the left ring stopping. 9.5s — nothing moves in the pit.

CAMERA: medium shot, 28mm spherical lens, low angle, camera low at ground height on a fixed tripod, 12 m from the craft, absolutely zero camera movement. — the same position, height and lens as Scene 28. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. After the transition, a closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. a long skid on metal, sparks, the engine winding down, then the pit's echo taking over the outside sound. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The boat stays whole, the skid grinds and nothing breaks off.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 32 — ARAÇTAN AYRILMA

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 5:20,0 · VURUŞ: İSTEK — dördü zeminde, hasarlı K-1 havuzda kalır (FAZ FARKI) · SEK08
KURULUM: B · dönüş S22 · 40mm · MS · eye level · fixed · IN FRAME: full body · HACİM: IC · İNSAN: 4 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 33 of 96.
The ramp is down with the commander on it one step from the floor, the engineer a step back, the gunner in the hatch, the pilot still seated inside the forward pane.

Medium shot at eye height inside the covered pit: a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing at the pit wall, crooked, the bent right ring in view, the ramp down. On the ramp a dark cobalt hard-shell suit with a pale grey mark on the left shoulder plate, one step from the floor; a step back an off-white hard-shell suit with teal forearms and a flat rectangular module frame on the back; in the hatch a graphite-grey hard-shell suit with broad mustard chest plates and a long dark tool; seated inside the forward pane a burnt-orange hard-shell suit with white bands on both upper arms; every helmet squared with one flat pane, fully opaque matte black, in a thick dark rim. Black basalt pit walls.
LIGHT: cold work lamps under the roof, a wedge of amber from the open side of the pit, the hull's white-blue lamp lit.
CAMERA: medium shot, 40mm spherical lens, camera at eye height on a fixed tripod, 3.0 m from the figure, absolutely zero camera movement. — the same position, height and lens as Scene 23. In a single continuous shot.
NEGATIVE: Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No two figures step down in the same second. The bent right ring stays bent in every frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 33 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The commander steps down first, the engineer one second later, the gunner two seconds after that, the pane's lamps go dark as the pilot shuts the panel, and the pilot walks down last so that four figures stand on the floor by the end.

TIMELINE: 0.0s — the commander one step from the floor, the others up the ramp. 1.0s — she steps onto the floor and moves two paces clear. 2.0s — the engineer steps down. 4.0s — the gunner comes down the ramp with the long tool held across the front. 5.5s — the lamps inside the forward pane go dark one by one as the pilot's gloves shut the panel. 7.5s — the pilot comes down the ramp last. 9.5s — four figures stand on the pit floor beside the crooked boat, the bent ring still in view.

CAMERA: medium shot, 40mm spherical lens, camera at eye height on a fixed tripod, 3.0 m from the figure, absolutely zero camera movement. — the same position, height and lens as Scene 23. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. boots on the ramp at four different beats, panel switches clicking off, the pit's closed echo; breathing inside the helmets. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No two figures step down in the same second. The bent right ring stays bent in every frame.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 33 — HASARIN SINIRI

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 5:30,0 · VURUŞ: BEDEL (araç) — panel açılır, bilezik sıkışmış, kelepçe yeri ölçülür · SEK09
KURULUM: D · dönüş S21 · 50mm · MCU · high angle (slight) · fixed · IN FRAME: hands, torso · HACİM: IC · İNSAN: 1 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands, torso
Scene 34 of 96.
The boat's right side panel is closed under the orange glove on its latch, a dark impact scar across the panel, and the bent edge of the right thrust ring shows just beyond the panel's corner.

Slightly above eye height looking down at a burnt-orange hard-shell torso with white bands on both upper arms, a squared helmet with one flat pane, fully opaque matte black, in a thick dark rim, crouched at the boat's grey flank. Under the right glove a squared side panel, closed, its latch under the fingers, a dark impact scar across it. Just beyond the panel's corner the bent rim of the right thrust ring, fixed out of line. The pit floor below, dusty metal.
LIGHT: a cold work lamp on the pilot's chest lighting the panel flat, the pit dim beyond, no warm source.
CAMERA: medium close-up, 50mm spherical lens, high angle, camera slightly above eye height at 1.7 m looking down at the hands and the object, 1.4 m from them, fixed, absolutely zero camera movement. — the same position, height and lens as Scene 22. In a single continuous shot.
NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No tool comes out and nothing is repaired, the ring stays bent.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands, torso
Scene 34 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The panel opens on the jammed ring mechanism, the orange glove pushes the ring and it does not turn, two fingers measure a span across the mechanism where a clamp would seat, and the panel closes again with the ring still bent.

TIMELINE: 0.0s — the glove on the latch. 1.0s — the latch turns and the panel swings open: a ring mechanism inside, its collar jammed against a bent guide. 3.0s — the glove pushes the collar; the forearm tightens, the collar does not move. 5.0s — the glove lets go; two fingers spread across the mechanism, measuring one span where the guide meets the collar. 7.0s — the glove closes the panel; the latch clicks. 8.5s — the pilot rises off the crouch, the rear boot loading first. 9.5s — the panel shut, the bent rim still showing beyond its corner.

CAMERA: medium close-up, 50mm spherical lens, high angle, camera slightly above eye height at 1.7 m looking down at the hands and the object, 1.4 m from them, fixed, absolutely zero camera movement. — the same position, height and lens as Scene 22. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. a latch, a panel hinge, a glove pushing on metal that does not move, the latch again; breathing inside the helmet. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No tool comes out and nothing is repaired, the ring stays bent.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 34 — İSTASYONA GEÇİŞ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 5:40,0 · VURUŞ: İSTEK — eski servis koridoru, aralıkta Veyra kavisi · SEK09
KURULUM: O · ilk kullanım · 28mm · MLS · from behind · walking pace · IN FRAME: back, full body · HACİM: IC · İNSAN: 4 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: back, full body
Scene 35 of 96.
Four suited backs walk away down a squared worn corridor, the cobalt commander leading, and at the corridor's end a door gap shows a sliver of curved amber surface.

From behind four walking figures in a squared worn human corridor of grey plate and exposed conduit. Leading, the back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate; after her the off-white back is one continuous surface from collar to hip carrying only one flat rectangular module frame the size of a chest plate; then the burnt-orange back is one continuous surface from collar to hip carrying only one narrow flat unit no thicker than a hand; last, nearest the camera, the back of the graphite-grey suit is one continuous sculpted surface from collar to hip carrying nothing, the long tool across the front. At the corridor's far end a door stands ajar and through the gap a sliver of smooth curved amber surface catches light.
LIGHT: cold conduit lamps along the ceiling every few paces, a thread of amber from the door gap at the end.
CAMERA: medium long shot following behind the walking figures, 28mm spherical lens, camera at shoulder height 3.5 m behind the last figure, the camera moves forward at their walking pace. In a single continuous shot.
NEGATIVE: Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The four backs stay in the same order the whole way, nobody passes anybody.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: back, full body
Scene 35 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The four walk at one steady pace and the camera keeps that pace behind them, the leading cobalt figure stops at the door gap and raises one flat glove for the others to slow, and the curved amber surface beyond the gap comes into focus.
The back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate.

TIMELINE: 0.0s — four backs walking, the camera following at their pace. 3.0s — the leading cobalt figure reaches the door gap and stops; her left glove rises flat, palm back, at shoulder height. 4.5s — the three following slow and stop one after another, the graphite back last. 6.5s — the cobalt helmet turns to the gap; beyond it the curved amber surface is clear, smooth, unmarked. 9.5s — four still backs, the raised glove still up.

CAMERA: medium long shot following behind the walking figures, 28mm spherical lens, camera at shoulder height 3.5 m behind the last figure, the camera moves forward at their walking pace. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. four sets of boots on plate at one pace, a far low curved hum growing as they near the door. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The four backs stay in the same order the whole way, nobody passes anybody.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 35 — YENİ CEPHE

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 5:50,0 · VURUŞ: HASIM — devriye önde, işaretleyici halkası arkada aydınlanır (iki tehdit) · SEK09
KURULUM: O · küme (Z) S34 · 28mm · MLS · from behind · walking pace · IN FRAME: back, full body · HACİM: IC · İNSAN: 4 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: back, full body
Scene 36 of 96.
The four backs stand still at the door gap with the commander's flat glove raised, and through the gap the curved amber hall is empty, the marker ring in its corner dark.

The last frame of the previous clip, unchanged: from behind, four still figures at the corridor's end — leading, the back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate, her left glove raised flat at shoulder height; after her the off-white, orange and graphite backs. Through the door gap a curved amber station hall, smooth and unmarked, empty; in its far corner a marker ring set into the wall, dark.
LIGHT: cold conduit lamps behind the figures, amber from the station hall through the gap on the raised glove and the helmet.
CAMERA: medium long shot following behind the walking figures, 28mm spherical lens, camera at shoulder height 3.5 m behind the last figure, the camera moves forward at their walking pace. continues the previous clip from its exact last frame — the same position, height and lens as Scene 35. In a single continuous shot.
NEGATIVE: Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly one tall figure enters the hall and it stays beyond the door gap.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: back, full body
Scene 36 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
One tall shielded figure walks into the hall from one side, the marker ring in the far corner lights amber a moment later, and the cobalt helmet turns from figure to ring and back.
The back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate.

TIMELINE: 0.0s — four still backs, the raised glove, the empty hall. 1.5s — a tall pale-ceramic figure walks into the hall from the side, the lower leg bending backward, a curved amber shield on its forearm, convex face forward. 4.0s — in the far corner the marker ring lights amber. 5.5s — the cobalt helmet turns to the lit ring. 7.5s — the helmet turns back to the figure; the raised glove closes into a fist. 9.5s — four backs still.

CAMERA: medium long shot following behind the walking figures, 28mm spherical lens, camera at shoulder height 3.5 m behind the last figure, the camera moves forward at their walking pace. continues the previous clip from its exact last frame — the same position, height and lens as Scene 35. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. a long stride on the curved floor with a different rhythm from human boots, then the ring's rising two-note tone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 4 human characters in suits and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly one tall figure enters the hall and it stays beyond the door gap.

Output: 16:9, no text, no watermark.
```

---
