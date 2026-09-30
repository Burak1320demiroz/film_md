# 🎬 THE_STOLEN_SKY — BÖLÜM 8  (S84 – S95) · BİR DAKİKALIK GÖKYÜZÜ

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
> Bölüm sınırı ardışık bir çifttir: S95 son sahne — kafiye S00 (aynı harf A, aynı CAMERA cümlesi)
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_16_dk_filmler/THE_STOLEN_SKY`

---
## 🎬 SAHNE 84 — KORİDOR KARARI

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 14:00,0 · VURUŞ: DORUK · MERKEZÎ SEÇİM (%88) — kol koridora çevrilir, saldırı söner (replik 8 post-dub) · SEK22
KURULUM: L · dönüş S82 · 50mm · MCU · low angle (slight) · fixed · IN FRAME: hands · HACİM: IC · İNSAN: 1 · REPLİK: post-dub 841,5 s · Mara · konuşan (opak, ağız yok)
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 85 of 96.
The cobalt glove is closed on the centred T-handle between the short thick pipe on the left and the long thin pipe on the right, the small amber lamp on the short pipe's cap is lit full, and the lamp at the long pipe is dark.

From slightly below eye height at the tank's control housing. In the centre the T-handle selector in its guide, centred, dark cobalt gloves with a small wrist control on the left forearm — the right glove closed on the handle. On the left the short thick pipe's squared cap with a small amber lamp lit full; on the right the long thin pipe with a small lamp at its base, dark. Under the handle the open lock latch. Above the housing a small window slit showing the curved amber Veyra command ship, seamless hull small over the amber lattice. The readout panel on the right lit with two plain ship outlines and one long band.
LIGHT: amber through the small window on the glove, the cap's lamp a full amber point, cold plate lamps from above.
CAMERA: medium close-up, 50mm spherical lens, low angle, camera slightly below eye height at 1.1 m looking up at the hand and the control, 1.4 m from them, fixed, absolutely zero camera movement. — the same position, height and lens as Scene 83. In a single continuous shot.
NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The handle moves once, in one direction, and never returns to the centre. No mouth, no invented on-screen speaker.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 85 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The glove drives the T-handle from the centre to the long pipe's side in one continuous movement that seats with a single hard click, the cap's amber lamp goes dark the instant the handle seats and the long pipe's lamp lights, and the glove leaves the handle.

TIMELINE: 0.0s — the glove closed on the centred handle. 0.5s — the glove drives the handle along its guide to the long pipe's side in one continuous movement, the forearm cording. 2.5s — the handle seats with a single hard click; the cap's amber lamp goes dark in the same instant; the long pipe's lamp lights. 4.5s — the handle held seated. 7.0s — the glove opens and leaves the handle, rising out of frame. 9.5s — the handle seated, its lamp lit, the cap's lamp dark.

CAMERA: medium close-up, 50mm spherical lens, low angle, camera slightly below eye height at 1.1 m looking up at the hand and the control, 1.4 m from them, fixed, absolutely zero camera movement. — the same position, height and lens as Scene 83. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. one long mechanical travel ending in a single hard click, a falling tone and a rising tone; breathing inside the helmet. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The handle moves once, in one direction, and never returns to the centre. No mouth, no invented on-screen speaker.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 85 — YİRMİ SANİYELİK BAŞLANGIÇ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 14:10,0 · VURUŞ: İSTEK — mandal tetiklenir (TIK = 14:10,000); depo nabzı; modül kulede kalır · SEK22
KURULUM: C · dönüş S66 · 35mm · MCU · OTS · fixed · IN FRAME: back (near shoulder), hands · HACİM: IC · İNSAN: 2 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: back (near shoulder), hands
Scene 86 of 96.
Past the cobalt shoulder the off-white glove rests on the spring latch under the seated T-handle, the handle sits at the long pipe's side with its lamp lit, and the tank's slots hold a steady amber light.

Over the near cobalt shoulder, the back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate, the shoulder filling the left edge. Past it off-white gloves with teal forearms, the right glove resting on the small spring latch under the T-handle, which sits seated at the long pipe's side with its small lamp lit. Beside the handle the strapped module. Above the housing the tank's narrow slots holding a steady amber light.
LIGHT: the tank's steady amber through its slots, cold plate lamps from above, a cold lamp on the engineer's chest.
CAMERA: over-the-shoulder medium close-up, 35mm spherical lens, camera just behind and above the near figure's shoulder at head height, 1.8 m from the far subject, fixed, absolutely zero camera movement. — the same position, height and lens as Scene 67. In a single continuous shot.
NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The module is not removed, it stays strapped to the housing. The pulse keeps one beat and never speeds up in this clip.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: back (near shoulder), hands
Scene 86 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The glove pulls the spring latch with a single sharp tick in the first second and the tank's amber light gives its first pulse at that tick, the light then pulses at one steady beat while the glove withdraws and the module stays strapped, and the engineer steps back out of frame.
The back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate.

TIMELINE: 0.0s — the glove on the latch, the tank's light steady. 0.8s — the glove pulls the latch with a single sharp tick, the forearm tightening; the tank's light dims and returns in one pulse at that tick. 2.0s — the light pulses again, and again, one steady beat. 3.5s — the glove withdraws; the module stays strapped, untouched. 6.0s — the engineer's forearms move back out of frame. 9.5s — the pulse steady, nothing else moving.

CAMERA: over-the-shoulder medium close-up, 35mm spherical lens, camera just behind and above the near figure's shoulder at head height, 1.8 m from the far subject, fixed, absolutely zero camera movement. — the same position, height and lens as Scene 67. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet. one sharp tick, then a low pulse at one steady beat, boots stepping back. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The module is not removed, it stays strapped to the housing. The pulse keeps one beat and never speeds up in this clip.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 86 — ÇATIDAN AYRILIŞ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 14:20,0 · VURUŞ: İSTEK — iki adımda rampa, K-1 ayrılır; gökte HAZIRLIK belirtileri, açıklık YOK · SEK22
KURULUM: F · dönüş S83 · 28mm · MLS · eye level · fixed · IN FRAME: full body · HACİM: YUZEY · İNSAN: 2 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 87 of 96.
The commander and the engineer stand on the roof two steps from the boat's swaying ramp, and the lattice above the tower is whole with a pale light beginning to rise from the tower's top.

Medium long shot at eye height on the tower's flat roof. In the centre a dark cobalt hard-shell suit with a pale grey mark on the left shoulder plate and, a step back, an off-white hard-shell suit with teal forearms and a flat rectangular module frame on the back; every helmet squared with one flat pane, fully opaque matte black, in a thick dark rim; both at the foot of the boat's open ramp, its lip swaying two steps from them. a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, hovering a hull-height up, nose pointing along the roof. Above, the amber lattice, whole; from the tower's emitter a pale column of light beginning to rise into it.
LIGHT: amber from the lattice above, the pale column from the emitter, the ramp's underside dark.
CAMERA: medium long shot, 28mm spherical lens, camera at eye height on a fixed tripod, 4.0 m from the figures, absolutely zero camera movement. — the same position, height and lens as Scene 84. In a single continuous shot.
NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The lattice does not open in this clip, it trembles and stays whole. Exactly two figures climb the ramp, no third.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 87 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The two climb the ramp in two steps each a second apart, the ramp seals, the boat turns onto its exit line leaning right and leaves the roof, and in the sky the pale column from the tower thickens and the lattice lines above it tremble without opening.

TIMELINE: 0.0s — both at the ramp's foot, the ramp swaying. 1.0s — the commander takes two steps up the ramp; at 2.0 the engineer follows with two steps. 3.5s — the ramp swings up and seals; bright points strike the roof edge where they stood, fragments dropping straight down. 5.0s — the boat turns onto its exit line, leaning right, and slides away from the roof. 7.0s — the pale column from the tower's emitter thickens and reaches the lattice; the lattice lines above it tremble. 9.5s — the boat small against the sky, the lattice trembling above the tower and still whole, no gap in it.

CAMERA: medium long shot, 28mm spherical lens, camera at eye height on a fixed tripod, 4.0 m from the figures, absolutely zero camera movement. — the same position, height and lens as Scene 84. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. boots on the ramp at two beats, a ramp seal, one ring at full pitch and short jets, impacts on plate, a rising field hum from the tower. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The lattice does not open in this clip, it trembles and stays whole. Exactly two figures climb the ramp, no third.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 87 — KORİDOR AÇILIR

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 14:30,0 · VURUŞ: DORUK başlangıcı (%91) — İLK KARE 14:30,000: koridor AÇIK ve GEÇİLEBİLİR; E-1 banda girer · SEK23
KURULUM: A · dönüş S13 · 24mm · WS · low angle · lockoff · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 88 of 96.
In this first frame the lattice already holds one clean straight gap two ship-widths wide running upward from above the tower, held open by a pale column of light from the tower's emitter, and every other cell of the lattice is whole.

Low and wide across black basalt rooftops. On the left the tall service tower; from its top emitter a pale column of light rises straight up into high in the sky a wide amber lattice of straight lines spaced no wider than two ship-lengths, and along that column the lattice is parted: one clean straight gap two ship-widths wide with hard amber edges, running upward from above the tower. Everywhere else the lattice whole. Lower right, two heavy hangar doors set into the slope, closed. beyond the lattice, lower and smaller, the lensed bright ring of the black hole hangs at a fixed place, never pulsing, above the far end of the gap.
LIGHT: amber from the lattice, the pale column brighter than the lattice, the ring's key above the gap's far end, shadows soft but deep.
CAMERA: wide shot, 24mm spherical lens, low angle, camera low at knee height on a fixed locked-off tripod, 6.0 m from the nearest subject, absolutely zero camera movement. — the same position, height and lens as Scene 14. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The gap is a straight band with hard edges, not a hole, not a glow, and it never changes width. Only one ship rises in this clip.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 88 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The two hangar doors open and the single-band evacuation ship rises out of them, it climbs and enters the parted gap so that the gap's amber edges are on both sides of it, and the gap holds the same width the whole time while the rest of the lattice stays whole.

TIMELINE: 0.0s — the gap open above the tower, the hangar doors closed. 1.0s — the two hangar doors slide apart; the single-band ship rises out of them, nose pointing up, dust falling straight off its hull. 4.0s — it climbs; at 5.5 its nose enters the parted gap and the amber edges are on both sides of it. 7.5s — it climbs inside the gap, the gap unchanged in width, the pale column holding beside it. 9.5s — the ship small inside the gap, the lattice whole everywhere else.

CAMERA: wide shot, 24mm spherical lens, low angle, camera low at knee height on a fixed locked-off tripod, 6.0 m from the nearest subject, absolutely zero camera movement. — the same position, height and lens as Scene 14. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. a deep field hum from the tower, two hangar doors sliding, a large engine climbing away. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The gap is a straight band with hard edges, not a hole, not a glow, and it never changes width. Only one ship rises in this clip.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 88 — BİRİNCİ GEMİ ÇIKAR

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 14:40,0 · VURUŞ: İSTEK — E-1 kafes sınırını geçer, sıçrar (sıçrama yalnız dışarıda) · SEK23
KURULUM: M · ilk kullanım · 28mm · MS · from below-behind · rising · IN FRAME: back (craft tail) · HACİM: YUZEY→VAKUM · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: back (craft tail)
Scene 89 of 96.
From below and behind, the single-band ship climbs inside the parted gap with the lattice's hard amber edges on both sides, its tail one continuous flat surface, and the boundary of the lattice is still ahead of it.

From below and behind a wide evacuation ship with one broad horizontal white band along its grey hull, nose pointing up, its tail one continuous flat surface carrying three engine bells, climbing inside the parted gap; the lattice's hard amber edges run past on both sides, two ship-widths apart. Ahead and above, the last line of the lattice, and beyond it the lensed bright ring, larger.
LIGHT: amber from the two lattice edges on both flanks, the ring's key ahead, the engine bells bright, the tail dark.
CAMERA: medium shot tracking upward from below and behind the craft, 28mm spherical lens, camera 9.0 m behind the craft's tail, the camera rises with it. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The flash happens only after the whole ship is above the last lattice line. No second ship, no fighter.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: back (craft tail)
Scene 89 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The ship crosses the last line of the lattice so the lattice is entirely below it, the sound thins to nothing, and a short flash at its tail is followed by the ship being gone with the ring hanging where it was.
The craft's tail is one continuous flat surface carrying only its engine rings.

TIMELINE: 0.0s — the ship climbing inside the gap. 2.5s — the last line of the lattice slides down past the tail; the lattice is entirely below. 4.0s — the amber edges drop away beneath. 6.0s — a short flash at the tail, the length of the ship, and the ship is gone. 7.5s — the ring hangs where the ship was, the lattice small below. 9.5s — nothing moves.

CAMERA: medium shot tracking upward from below and behind the craft, 28mm spherical lens, camera 9.0 m behind the craft's tail, the camera rises with it. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air. From the moment the volume changes, above the lattice the air is gone, no sound outside, shadows absolute black, any fragment keeps a straight line.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. After the transition, no exterior sound at all; only the radio hiss and breathing carried inside the hull. three engines climbing, the sound thinning to nothing as the air thins, then one short jump tone carried inside the hull perspective only. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The flash happens only after the whole ship is above the last lattice line. No second ship, no fighter.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 89 — İKİNCİ GEMİYE ATEŞ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 14:50,0 · VURUŞ: HASIM — avcı koridorun kenarından E-2'nin sağ denge yüzeyini sıyırır · SEK23
KURULUM: P · dönüş S77 · 28mm · WS · side · fixed · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 90 of 96.
Seen from the side, the double-band ship climbs inside the parted gap with its right stabiliser whole, and a curved fighter hangs outside the gap's amber edge, above the lattice, with its nose pointing down at the ship.

Wide from the side at hull height. In the centre a second evacuation ship with two vertical white bands on its grey hull, nose pointing up, climbing inside the parted gap, its right stabiliser whole; the gap's hard amber edges on both sides of it. Above and to the far side, outside the gap and above the lattice, a curved seamless Veyra fighter with an amber-lit edge, nose pointing down at the ship, not entering the gap. Black basalt rooftops far below; the ring's light off the top edge of frame.
LIGHT: amber from the gap edges on the ship's flanks, the fighter's edge bright above, the rooftops dim below.
CAMERA: wide shot from the side, 28mm spherical lens, camera at hull height on a fixed tripod, 30 m from the craft, absolutely zero camera movement. — the same position, height and lens as Scene 78. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The fighter never enters the gap. The ship keeps climbing, it does not fall.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 90 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
Bright points from the fighter cross the gap's edge, one grazes the right stabiliser leaving a dark scorch along it, the ship yaws and rolls once and steadies, and it keeps climbing inside the gap at a slower rate than before.

TIMELINE: 0.0s — the ship climbing, the fighter above outside the gap. 1.5s — three bright points leave the fighter's nose and cross the gap's edge. 2.5s — one grazes the right stabiliser; a dark scorch is left along it, small fragments falling straight down. 3.5s — the ship yaws and rolls once, its nose swinging a hand off the vertical, and steadies. 6.0s — it keeps climbing inside the gap, slower than before, the scorch dark on the stabiliser. 9.5s — the ship higher in the gap, the fighter still outside the edge.

CAMERA: wide shot from the side, 28mm spherical lens, camera at hull height on a fixed tripod, 30 m from the craft, absolutely zero camera movement. — the same position, height and lens as Scene 78. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. three heavy cracks, a graze on a hull, a large engine faltering and recovering, the fighter's low tone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The fighter never enters the gap. The ship keeps climbing, it does not fall.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 90 — K-1 ARAYA GİRER

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 15:00,0 · VURUŞ: BEDEL (araç) — K-1 ateş hattı ile E-2 arasına; arka çıkıntı kopar (DENEME P5) · SEK23
KURULUM: P · küme (Z) S89 · 28mm · WS · side · fixed · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 91 of 96.
The double-band ship climbs inside the parted gap with a dark scorch on its right stabiliser, the fighter hangs outside the gap's edge, and the boxy boat with the steel clamp is below them, leaning right, its rear sensor stub still whole.

The last frame of the previous clip, unchanged: wide from the side at hull height. In the upper centre a second evacuation ship with two vertical white bands on its grey hull, a dark scorch along its right stabiliser, nose pointing up, climbing inside the parted gap between its hard amber edges. Above and to the far side, outside the gap, a curved seamless Veyra fighter with an amber-lit edge, nose pointing down at it. Below them, inside the gap, a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, nose pointing up, leaning right, a short sensor stub on its tail whole.
LIGHT: amber from the gap edges, the fighter's edge bright, the boat's clamp catching a hard edge.
CAMERA: wide shot from the side, 28mm spherical lens, camera at hull height on a fixed tripod, 30 m from the craft, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 90. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The torn stub falls as one piece and does not return. The fighter never enters the gap; only three craft in frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 91 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The boat climbs into the line between the fighter and the ship, bright points from the fighter meet the boat's tail and tear the sensor stub off as one piece, the ship above keeps climbing, and the boat yaws and corrects.

TIMELINE: 0.0s — the ship climbing, the fighter outside the gap, the boat below. 1.5s — the boat climbs into the line between the fighter's nose and the ship, its hull now between them. 3.5s — three bright points from the fighter meet the boat's tail; the stub tears off as one piece and falls away turning on one axis; a raw bright stump is left. 5.5s — the ship above keeps climbing, untouched. 7.0s — the boat yaws from the impact and its left jets fire and correct it. 9.5s — the boat level except for its lean, the ship higher, the fighter still outside the edge.

CAMERA: wide shot from the side, 28mm spherical lens, camera at hull height on a fixed tripod, 30 m from the craft, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 90. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. three heavy cracks, metal tearing off a hull, one ring at full pitch and jets, a large engine above. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The torn stub falls as one piece and does not return. The fighter never enters the gap; only three craft in frame.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 91 — İKİNCİ GEMİ KURTULUR

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 15:10,0 · VURUŞ: İSTEK — E-2 sınırı aşar, sıçrar; K-1 tek başına tırmanır · SEK23
KURULUM: F · dönüş S86 · 28mm · MLS · eye level · fixed · IN FRAME: none · HACİM: YUZEY · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 92 of 96.
The double-band ship's underside fills the upper frame just below the last lattice line with the dark scorch on its right stabiliser, and the boxy boat is small below it inside the gap, leaning right, with the steel clamp and the raw stump on its tail.

Medium long shot at hull height looking up the parted gap. Filling the upper frame the underside of a second evacuation ship with two vertical white bands on its grey hull, a dark scorch along its right stabiliser, nose pointing up, a ship-length below the last line of the lattice, the gap's amber edges on both sides. Small below it, inside the gap, a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, the rear sensor stub torn off, a raw bright stump left on the tail, nose pointing up, leaning right. The ring's light beyond the last line.
LIGHT: amber from the gap edges, the ring's key beyond the last line, the ship's engine bells bright, its underside dark.
CAMERA: medium long shot, 28mm spherical lens, camera at eye height on a fixed tripod, 4.0 m from the figures, absolutely zero camera movement. — the same position, height and lens as Scene 87. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The flash happens only after the whole ship is above the last line. The gap does not change width in this clip.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 92 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The ship crosses the last lattice line, a short flash the length of its hull follows and it is gone, and the boat climbs on alone inside the gap with its left jets firing every few seconds to hold its line against the lean.

TIMELINE: 0.0s — the ship a ship-length below the last line, the boat small below. 2.0s — the ship's nose crosses the last line; at 3.0 its tail is above it. 4.0s — a short flash the length of its hull, and the ship is gone; the ring hangs where it was. 5.5s — the boat climbs on alone inside the gap, leaning right. 7.0s — its left jets fire once and its line straightens, then it leans again. 9.5s — the boat higher in the gap, the gap still open at the same width.

CAMERA: medium long shot, 28mm spherical lens, camera at eye height on a fixed tripod, 4.0 m from the figures, absolutely zero camera movement. — the same position, height and lens as Scene 87. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. a large engine thinning away above, one short jump tone, then one ring at full pitch and short jets alone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The flash happens only after the whole ship is above the last line. The gap does not change width in this clip.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 92 — SON TIRMANIŞ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 15:20,0 · VURUŞ: FİZİKSEL DORUK (%97) — daralan açıklıktan bütün gövde dışarı; hasarlı itki görünür (KAPAK ADAYI) · SEK23
KURULUM: X · dönüş S28 · 35mm · MS · front-low · rising · IN FRAME: none · HACİM: YUZEY→VAKUM · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 93 of 96.
From the front lower quarter, the boat's whole hull is in frame with the steel clamp on its right ring and the raw stump on its tail, leaning right, and above it the parted gap has narrowed to one and a half ship-widths with the lattice closing in from both sides.

From the front lower quarter of a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, nose pointing up, a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, the rear sensor stub torn off, a raw bright stump left on the tail, leaning right, the whole hull in frame. Above it the parted gap, now one and a half ship-widths wide, its hard amber edges closer on both sides than before; beyond the gap's far end the lensed bright ring, large. The lattice everywhere else whole.
LIGHT: amber from the two closing edges on the hull's flanks, the ring's key from above, the left jets and one ring bright, the clamp catching a hard edge.
CAMERA: medium shot tracking upward from the front lower quarter of the craft, 35mm spherical lens, low angle, camera 10 m ahead of and below the craft, the camera rises with it. — the same position, height and lens as Scene 29. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The whole hull is outside the lattice before the clip ends. The gap narrows and does not close in this clip.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 93 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The boat climbs into the narrowing gap with its jets firing, the hull shakes as the edges close to one ship-width, and before the clip ends the tail crosses the final lattice line so the whole boat is outside.

TIMELINE: 0.0s — the boat climbing, the edges a ship-width and a half apart. 2.0s — the jets fire and stay lit; the hull shakes; the edges close to one ship-width. 4.5s — the hull holds its line, the edges a hand from each flank. 6.5s — the nose crosses the final lattice line. 8.0s — the tail crosses the final line; the whole boat is outside. 9.5s — the boat above the lattice.

CAMERA: medium shot tracking upward from the front lower quarter of the craft, 35mm spherical lens, low angle, camera 10 m ahead of and below the craft, the camera rises with it. — the same position, height and lens as Scene 29. In a single continuous shot.
PHYSICS: Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air. From the moment the volume changes, above the lattice the air is gone, no sound outside, shadows absolute black, any fragment keeps a straight line.
AUDIO: Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet. After the transition, no exterior sound at all; only the radio hiss and breathing carried inside the hull. one ring at full pitch and jets, the hull shaking, the air thinning to nothing. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The whole hull is outside the lattice before the clip ends. The gap narrows and does not close in this clip.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 93 — KAPANAN GÖKYÜZÜ

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 15:30,0 · VURUŞ: İSTEK — İLK KARE 15:30,000: koridor KAPANIR; K-1 dışarıda, sıçrar · SEK24
KURULUM: Q · ilk kullanım · 24mm · WS · looking back down · fixed · IN FRAME: none · HACİM: VAKUM · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 94 of 96.
From outside the lattice looking back down, the boat is in the foreground already above the lattice with the stump and the clamp, and below it the parted gap is still open, one ship-width wide, over the dark planet.

Wide from outside the lattice looking back down. In the foreground a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, the rear sensor stub torn off, a raw bright stump left on the tail, a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, nose pointing away from the planet, leaning right, its rings and jets dark against space. Below it a wide amber lattice of straight lines spaced no wider than two ship-lengths, spread over the dark curve of the planet, and in it one straight gap a ship-width wide, still open. Far below in the gap a few small bright points rising. The ring's light falls from beyond the top of frame.
LIGHT: the ring's key from beyond the top of frame on the boat's upper hull, amber from the lattice below on its underside, shadows absolute black with razor edges.
CAMERA: wide shot looking back down from outside the lattice, 24mm spherical lens, high angle, camera 40 m from the craft, fixed, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The gap closes fully and stays closed. No point of light passes through the whole lattice.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 94 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
In the first three seconds the gap closes from both edges until the lattice is whole, the rising bright points stop at the lattice and go out, a short flash the length of the boat follows and the boat is gone, and the whole lattice and the planet remain for the last three seconds.

TIMELINE: 0.0s — the gap open below the boat, the bright points rising in it. 0.5s — the gap's two edges move together at one speed; at 2.5 they meet and the lattice is whole. 3.5s — the rising bright points meet the whole lattice and go out on it. 5.5s — a short flash the length of the boat, and the boat is gone. 7.0s — the whole lattice over the dark planet, unbroken. 9.5s — nothing moves.

CAMERA: wide shot looking back down from outside the lattice, 24mm spherical lens, high angle, camera 40 m from the craft, fixed, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Hard vacuum in orbit above the planet; no air and no sound outside the hulls, shadows absolute black with razor edges, any released fragment keeps a straight line and its own rotation axis.
AUDIO: No exterior sound at all; only the radio hiss and breathing carried inside the hull. no exterior sound; inside the hull perspective a radio hiss and breathing, one short jump tone, then the hiss alone. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. The gap closes fully and stays closed. No point of light passes through the whole lattice.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 94 — BOŞ KOLTUK

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 15:40,0 · VURUŞ: BEDEL ⭐ FİNAL (%98) — üç kişi, dört koltuk; Mara boş koltuğun kemerini kapatır (S18 kafiyesi) · SEK24
KURULUM: G · dönüş S30 · 24mm · MLS · cabin rear · craft-fixed · IN FRAME: torso, hands (seated) · HACİM: KABIN0G · İNSAN: 3 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: torso, hands (seated)
Scene 95 of 96.
Four seats can be counted in the cabin and three are filled — orange front-left, off-white front-right, cobalt rear-left — and in the empty rear-right seat the two halves of an open belt drift a hand apart.

From the rear of the cabin, level. Front-left seat: a burnt-orange hard-shell suit with white bands on both upper arms, gloves resting on the grips. Front-right seat: an off-white hard-shell suit with teal forearms and a flat rectangular module frame on the back. Rear-left seat: a dark cobalt hard-shell suit with a pale grey mark on the left shoulder plate with a long pale scrape across the left chest plate, both gloves on her lap; every helmet squared with one flat pane, fully opaque matte black, in a thick dark rim. Rear-right seat: empty, its two belt halves drifting a hand apart above the seat, turning slowly. Through the flat forward pane, stars, and small at the pane's edge the lensed bright ring.
LIGHT: cold blue-white cabin lamps from above, the stars in the pane the only outside light, the empty seat lit the same as the others.
CAMERA: medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves. — the same position, height and lens as Scene 31. In a single continuous shot.
NEGATIVE: Exactly 3 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly four seats and exactly three occupants, the fourth seat stays empty. No helmet turns to the empty seat, only the glove moves.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: torso, hands (seated)
Scene 95 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
For three seconds nothing moves but the drifting belt halves, then the cobalt right glove reaches across, gathers the two halves and latches them with a single click over the empty seat, and the glove stays resting on the closed belt to the end.

TIMELINE: 0.0s — three seated torsos still, the two belt halves drifting a hand apart over the empty seat. 3.0s — the cobalt right glove leaves the lap and reaches across the gap between the rear seats, slowly. 5.0s — the glove gathers the two belt halves and brings them together. 6.0s — the latch closes with a single click over the empty seat. 7.0s — the glove stays resting on the closed belt; the other two torsos do not turn. 9.5s — the glove on the belt, the empty seat belted, nothing else moving.

CAMERA: medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves. — the same position, height and lens as Scene 31. In a single continuous shot.
PHYSICS: Microgravity inside a cabin pressurised at one atmosphere; the one loose object drifts in a straight line while turning slowly on its own axis, the three figures strapped in.
AUDIO: A steady cabin hum and breathing inside the helmets, exterior sound muffled. a steady cabin hum, one belt latch click, three breathing rhythms inside three helmets, no fourth. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly four seats and exactly three occupants, the fourth seat stays empty. No helmet turns to the empty seat, only the glove moves.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 95 — ÜÇ IŞIK

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: 15:50,0 · VURUŞ: KAPANIŞ İMAJI (%100) — kafiye S00: aynı harf, üç gemi, gezegen ve halka küçük · SEK24
KURULUM: A · dönüş S87 · 24mm · WS · low angle · lockoff · IN FRAME: none · HACİM: VAKUM · İNSAN: 0 · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 96 of 96.
Three human craft share one frame side by side — the single-band ship, the scorched double-band ship, and the boat with its clamp and its stump — and the planet and the ring are small in the frame's corner.

Wide across open space. In the centre, level and a hull-length apart, three human craft with their noses pointing the same way, away from the planet: a wide evacuation ship with one broad horizontal white band along its grey hull; a second evacuation ship with two vertical white bands on its grey hull, a dark scorch along its right stabiliser; and a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, the rear sensor stub torn off, a raw bright stump left on the tail. Small in the lower corner the dark planet under its thin amber lattice, and beside it, smaller, the lensed bright ring. Stars everywhere else.
LIGHT: the ring's key from the corner as one hard rim on each hull, shadows absolute black with razor edges.
CAMERA: wide shot, 24mm spherical lens, low angle, camera low at knee height on a fixed locked-off tripod, 6.0 m from the nearest subject, absolutely zero camera movement. — the same position, height and lens as Scene 88. In a single continuous shot.
NEGATIVE: Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly three craft, no fourth and no fighter. The planet and the ring do not move or grow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 96 of 96. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
The three craft hold their line for three seconds, then move away from the camera together at one speed so that they shrink to three points of light, while the planet and the ring stay exactly where they are.

TIMELINE: 0.0s — three craft side by side, still relative to the camera. 3.0s — all three engine bells brighten together and the craft begin to move away at one speed. 5.5s — they shrink, still level with each other, a hull-length apart. 8.0s — three small shapes with three warm points; the planet and the ring unchanged in the corner. 9.8s — three points of light still moving, the clip ends on the movement.

CAMERA: wide shot, 24mm spherical lens, low angle, camera low at knee height on a fixed locked-off tripod, 6.0 m from the nearest subject, absolutely zero camera movement. — the same position, height and lens as Scene 88. In a single continuous shot.
PHYSICS: Hard vacuum in orbit above the planet; no air and no sound outside the hulls, shadows absolute black with razor edges, any released fragment keeps a straight line and its own rotation axis.
AUDIO: No exterior sound at all; only the radio hiss and breathing carried inside the hull. no exterior sound; a faint radio hiss and one breathing rhythm carried inside a hull, nothing else. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, the empty deck and sky are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. Exactly three craft, no fourth and no fighter. The planet and the ring do not move or grow.

Output: 16:9, no text, no watermark.
```

---
