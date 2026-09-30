# 🎬 THE_SLOW_RAIN — BÖLÜM 1  (S0 – S11)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_SLOW_RAIN_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③). ⭐ self-contained ≠ Bible'ın
> tamamı — yalnız `IN FRAME:` satırındaki tarif edilir [D214].
>
> ⭐ **YENİ REJİM:** ilk satır `IN FRAME:` (㉖) · POZİTİF gövde IMAGE 100-250 / VIDEO 120-300 kelime (①) ·
> NEGATIVE = §5.1 çekirdek (image 7 · video 8) + ≤3 sahneye özel (㉗) · video tek satır `START FRAME:`.
> ⭐ **OMNI katmanı:** CAMERA `In a single continuous shot.` ile biter · AUDIO her klipte dolu · tırnak 0.
> ⭐ **Promptta `Scene n of 48` = S + 1.** Dönüş ve küme işaretleri de bu numarayı kullanır.
> ⭐ **NOVUM sayı cümlesi** (damla: bilye boyu · seyrek · yavaş koşu temposu) novum sahnelerinde birebir; öteki dış sahnelerde kısa hâli.
> ⭐ **KANAT / KIZAK / SIRT** cümleleri birebir (PLAN Bible): S0-S14 kanat sırtta · S15-S28 kızak · S29+ sırt düz.
> ⛔ Replik yok — film sessiz tasarımlı; AUDIO her promptta ortamın ses yasası.
>
> Bölüm sınırı ardışık bir çifttir: S11 (I · WS · az 45°) ↔ S12 (G · EWS · az 270°) · 1 kademe · 135° ✅
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_8_dk_filmler/THE_SLOW_RAIN`

---

## 🎬 SAHNE 0 — İLK DAMLA

```
SÜRE: 10 s · ZAMAN: 0:00,0 · VURUŞ: açılış imajı · S0 SORUSU · ⭐VİRAL
KURULUM: A · ilk kullanım · 75mm · CU · eye-level close-up, frontal · IN FRAME: face · hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · hands
Scene 1 of 48.
One large drop, the size of a marble, is a hand's width above her raised right glove; three more drops are on their way down behind it.

Her right glove is raised palm-up at chest height, the ribbed sleeve running down into the lower left of the frame, her helmet and shoulders just behind the hand. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. The dark door frame of the base dome fills the left of the frame past her shoulder. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. Large sparse drops the size of marbles, few enough to count, fall through the frame at a slow jogging pace, far slower than rain on Earth, none streaking, none hanging still.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 75mm lens on a fixed locked-off tripod 1.6 m in front of her, camera height 1.55 m, eye-level close-up, frontal.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · hands
Scene 1 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The drop lands on the raised glove and flashes into a white puff that rises to knee height and falls back as dry snow within two seconds; the glove stays raised for the whole take.

TIMELINE: 0.0s — her right glove is raised palm-up, the first drop a hand's width above it, her eyes on the drop. 1.0s — the drop meets the glove and flashes into a white puff; her brows lift and she blinks once, her hand's grip tightens as the glove holds; the puff falls back as dry snow. 4.0s — two more drops come down past the glove at the same slow pace, one of them landing and puffing; she keeps the glove up through the last second, her eyes following the next drop.

CAMERA: 75mm lens on a fixed locked-off tripod 1.6 m in front of her, camera height 1.55 m, eye-level close-up, frontal, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 1 — SÜZÜLÜŞ

```
SÜRE: 10 s · ZAMAN: 0:10,0 · VURUŞ: kurulum · S1 ikinci bilgi
KURULUM: C · ilk kullanım · 24mm · WS · low angle wide shot · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 2 of 48.
She is already off the ridge lip, her wing rig open to twice her arm-span, gliding level over the lakebed at one steady rate.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. her wing rig open, two taut dark smoke-grey membranes on a rigid pale grey spar frame spanning twice her arm-span, held by a chest harness with one steel buckle, the only thing on her back, the back of the suit under it one continuous smooth panel, seen from below and behind at the moment she clears the ridge lip. Above her only the amber haze; below, the pale-dusted lakebed. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m below the ridge lip, camera height 0.40 m, low angle wide shot looking up, three-quarter rear.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 2 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She glides on her open wings at one steady rate, losing height slowly, about a body-length every two seconds, no flapping.

TIMELINE: 0.0s — she is already airborne past the ridge lip, wings open and level, the membranes taut on their spars. 3.0s — she banks a hand's width to the left and the whole glide follows it, height dropping at one steady rate. 7.0s — she glides on out over the lakebed at the same rate through the last second, wings level, the membranes taut.

CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m below the ridge lip, camera height 0.40 m, low angle wide shot looking up, three-quarter rear, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The folding wing rig stays the only thing on her back, and under it the back of the suit is one continuous smooth panel from collar to hip.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 2 — ÇENTİĞİN ÜSTÜ

```
SÜRE: 10 s · ZAMAN: 0:20,0 · VURUŞ: kurulum · SAYAÇ 1 kurulur · ⭐VİRAL
KURULUM: R · ilk kullanım · 35mm · MS · eye-level medium shot, three-quarter front · IN FRAME: face · hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · hands · torso
Scene 3 of 48.
She lands at the base door with both boots and one glove flat on the door pane; behind the pane a white frost line stands one finger above a single scratched notch.

her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim, the wing rig folded flat along her spine, her right glove flat on the door's clear pane. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. Through the pane a dim interior wall carries a horizontal white frost line with one plain scratched notch below it. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · hands · torso
Scene 3 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She comes down onto both boots at the door and the wings fold; her glove stays flat on the pane beside the frost line for the rest of the take.

TIMELINE: 0.0s — she is already dropping onto the door step, wings half-folded, one glove reaching for the pane. 2.0s — both boots take the ground, knees bending under it, and the glove lands flat on the pane; her eyes find the frost line above the notch and lock there. 6.0s — she leans on the pane, shoulders rising once with a slow breath, the glove pressed flat through the last second.

CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 3 — SÖNÜK GÖSTERGE

```
SÜRE: 10 s · ZAMAN: 0:30,0 · VURUŞ: KATALİZÖR
KURULUM: J · ilk kullanım · 75mm · CU · high angle close-up looking down · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 4 of 48.
Her right glove rests on the cold socket cover, fingers closing and easing on its latch; the single round lamp beside the socket is unlit.

Only her slim dark segmented glove and ribbed pale grey sleeve are in frame, the brushed-steel wrist ring where the glove meets the sleeve, the glove on a matte grey socket cover set into the wall. One plain round lamp sits in the socket rim, unlit; white frost crusts the wall around the cover.
LIGHT: one warm ceiling panel inside, soft and steady, the frost on the walls lit evenly, no glare.
CAMERA: 75mm lens on a fixed locked-off tripod 1.2 m from the object, camera height 1.60 m, high angle close-up looking down thirty degrees, frontal.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 4 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The glove works the latch a finger's width at a time without opening it; the lamp stays unlit through the last frame.

TIMELINE: 0.0s — the glove is already on the cover, fingers closed on the latch, the sleeve drawn taut. 3.0s — the fingers ease and close again on the latch; frost crackles off the cover edge under the glove. 7.0s — the glove keeps working the latch at the same slow rate through the last second, the lamp beside it dark.

CAMERA: 75mm lens on a fixed locked-off tripod 1.2 m from the object, camera height 1.60 m, high angle close-up looking down thirty degrees, frontal, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Inside the pressurised base at about one atmosphere, gravity is 0.38 g; the frost on the walls is real ice and any meltwater drips fall fast.
AUDIO: near silence inside — a faint crackle of frost, her breathing inside the helmet, no hum. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 4 — HARİTA

```
SÜRE: 10 s · ZAMAN: 0:40,0 · VURUŞ: tartışma · tohum (%8)
KURULUM: R · dönüş · 35mm · MS · eye-level medium shot, three-quarter front · IN FRAME: face · hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · hands · torso
Scene 5 of 48.
Her right glove is on a raised relief map on the wall, one finger on the far side of a dark oval; an empty wall rack with two open clips hangs at the right edge of the frame.

her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim, the wing rig folded along her spine, her right glove on a raised relief map cast in the wall. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. The map is a plain cast relief with no marks: a dark oval basin and a small raised block on its far rim; at the frame's right edge an empty wall rack with two open clips.
LIGHT: one warm ceiling panel inside, soft and steady, the frost on the walls lit evenly, no glare.
CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front. — the same position, height and lens as Scene 3.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · hands · torso
Scene 5 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Her finger crosses the dark oval of the map from near rim to far rim and stops on the raised block; it stays there through the last second.

TIMELINE: 0.0s — her glove is on the map, one finger at the near rim of the oval, her eyes on the far rim. 3.0s — the finger crosses the oval at one steady rate and lands on the raised block on the far rim; her helmet tilts a hand's width toward it. 7.0s — the finger stays on the block; her shoulders rise once with a slow breath and drop; the empty rack hangs at the frame edge.

CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 3. In a single continuous shot.
PHYSICS: Inside the pressurised base at about one atmosphere, gravity is 0.38 g; the frost on the walls is real ice and any meltwater drips fall fast.
AUDIO: near silence inside — a faint crackle of frost, her breathing inside the helmet, no hum. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 5 — PERDE YARI YOLDA

```
SÜRE: 10 s · ZAMAN: 0:50,0 · VURUŞ: tartışma
KURULUM: B · ilk kullanım · 24mm · WS · high angle wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 6 of 48.
She stands at the ridge lip in full profile; the rain front hangs over the lakebed as a band of pale beads halfway between the haze and the ridge height.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. On her back a folding wing rig, two dark smoke-grey membranes folded flat along her spine on a pale grey spar frame, held by one steel chest buckle, the only thing on her back. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The old station in the left third, a low dark module barely taller than she is, one door, a flat roof.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod on the ridge 6.0 m behind and above her, camera height 3.0 m, high angle wide shot looking down, full profile.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 6 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She stays at the lip with her helmet on the far station while the band of drops keeps descending at one steady rate, no faster.

TIMELINE: 0.0s — she is standing at the lip, helmet toward the far station, the band of drops hanging over the lakebed. 4.0s — her shoulders rise once with a slow breath and drop; the band of drops has come down a little, still above the ridge height. 8.0s — she keeps her helmet on the station through the last second; the drops go on descending at the same rate.

CAMERA: 24mm lens on a fixed locked-off tripod on the ridge 6.0 m behind and above her, camera height 3.0 m, high angle wide shot looking down, full profile, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 6 — ATLAYIŞ

```
SÜRE: 10 s · ZAMAN: 1:00,0 · VURUŞ: tartışma → eylem
KURULUM: B · küme S5 · 24mm · WS · high angle wide shot, full profile · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 7 of 48.
Her right glove pulls the chest buckle twice, she takes two steps and goes off the lip, and the wings open as she drops out of the frame.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. On her back a folding wing rig, two dark smoke-grey membranes folded flat along her spine on a pale grey spar frame, held by one steel chest buckle; the rig is the only thing on her back and under it the back of the suit is one continuous smooth panel. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The old station in the left third, a low dark module barely taller than she is, one door, a flat roof.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod on the ridge 6.0 m behind and above her, camera height 3.0 m, high angle wide shot looking down, full profile. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 6.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 7 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Her glove tugs the buckle exactly twice, she steps off the lip, and the wings open to twice her arm-span as she drops away below.

TIMELINE: 0.0s — she is at the lip, right glove on the chest buckle, weight already on the front boot. 2.0s — the glove tugs the buckle twice, then she takes two steps and leaves the lip; the wings open as she falls. 5.0s — she drops away below the lip on open wings at one steady rate through the last second.

CAMERA: 24mm lens on a fixed locked-off tripod on the ridge 6.0 m behind and above her, camera height 3.0 m, high angle wide shot looking down, full profile, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 6. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The folding wing rig stays the only thing on her back, and under it the back of the suit is one continuous smooth panel from collar to hip.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 7 — PERDENİN ALTINDAN

```
SÜRE: 10 s · ZAMAN: 1:10,0 · VURUŞ: tartışma · novum doğrulama
KURULUM: G · ilk kullanım · 24mm · EWS · low angle extreme wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 8 of 48.
She glides in full profile under the rain front toward the station; one drop lands on her left wing and flashes into a white puff.

A single figure gliding low in full profile, her wing rig open, two dark smoke-grey membranes on a pale grey spar frame spanning twice her arm-span, held by one steel chest buckle, the only thing on her back, in her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim. The band of drops hangs above her. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The old station in the left third, a low dark module barely taller than she is, one door, a flat roof. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 8 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
One drop meets the left wing membrane and flashes into a white puff that falls away in her wake as dry snow, and she glides on at one steady rate.

TIMELINE: 0.0s — she is already gliding low from right to left under the band of drops, wings level. 3.0s — a drop lands on the upper surface of her left wing and flashes into a white puff; the glide does not change. 6.0s — the puff falls away in her wake as dry snow while she glides on toward the station at the same rate through the last second.

CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 8 — SERT İNİŞ

```
SÜRE: 10 s · ZAMAN: 1:20,0 · VURUŞ: tartışma
KURULUM: G · küme S7 · 24mm · EWS · low angle extreme wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 9 of 48.
She comes down hard onto the flat station roof on one knee and both gloves; the tip of her left wing drags on the frost and splits at its last spar.

A single figure landing on the low station roof, her wing rig open, two dark smoke-grey membranes on a pale grey spar frame spanning twice her arm-span, held by one steel chest buckle, the only thing on her back, her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The old station in the left third, a low dark module barely taller than she is, one door, a flat roof.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 8.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 9 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She lands on one knee and both gloves on the roof and the left wing-tip scrapes the frost and splits; she stays down on the knee, the split tip trailing.

TIMELINE: 0.0s — she is already dropping onto the roof, wings flaring, one knee coming down first. 2.0s — the knee and both gloves take the roof, the left wing-tip drags across the frost and splits along its last spar. 5.0s — she stays down on one knee and both gloves through the last second, shoulders rising with a heavy breath, the split tip lying on the frost.

CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 8. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 9 — DONMUŞ KAPI

```
SÜRE: 10 s · ZAMAN: 1:30,0 · VURUŞ: tartışma · ironi asimetri anı
KURULUM: I · ilk kullanım · 24mm · WS · eye-level wide shot, three-quarter front · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 10 of 48.
Her shoulder is against the frozen station door and she works a pale grey wing-spar into its seam; the door is open a hand's width at the cut, and past her shoulder the band of drops hangs lower over the lakebed than before, seen past her shoulder.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. On her back a folding wing rig, two dark smoke-grey membranes folded flat along her spine on a pale grey spar frame, held by one steel chest buckle; the rig is the only thing on her back and under it the back of the suit is one continuous smooth panel. The station door is a dark panel crusted with frost along its seam; past her the lakebed and, above it, the band of drops. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 6.0 m from the station door, camera height 1.20 m, eye-level wide shot, three-quarter front.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 10 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She works the door open a hand's width, shoulder and spar together, the frost along the seam breaking away a finger at a time; the band of drops past her keeps descending.

TIMELINE: 0.0s — her shoulder is already against the door, the spar in the seam, her rear boot braced on the frost. 3.0s — the frost along the seam cracks and the door gives a finger's width; she resets the spar and leans in again, shoulders dropping into the push. 7.0s — the door is a hand's width open and she keeps pushing at the same rate through the last second; past her shoulder the band of drops has come lower.

CAMERA: 24mm lens on a fixed locked-off tripod 6.0 m from the station door, camera height 1.20 m, eye-level wide shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The folding wing rig stays the only thing on her back, and under it the back of the suit is one continuous smooth panel from collar to hip.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 10 — KANAT İŞARETİ

```
SÜRE: 10 s · ZAMAN: 1:40,0 · VURUŞ: tartışma · MUHATAP geçmiş karar
KURULUM: K · ilk kullanım · 35mm · MS · eye-level medium shot, full profile · IN FRAME: hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands · torso
Scene 11 of 48.
Her right glove rests on the frosted core on the shelf, two fingers on a scratched mark of two short lines like a pair of wings, then closes on the near carry handle.

Only her slim dark segmented glove and ribbed pale grey sleeve are in frame, the brushed-steel wrist ring where the glove meets the sleeve, resting on a matt dark-metal cylinder the size of a small keg with a carry handle on each side. The core sits on a frosted metal shelf; two short scratched lines like a pair of wings are cut into its side under the glove.
LIGHT: dim grey-blue inside the station, the amber haze fill spilling in through the open door.
CAMERA: 35mm lens on a fixed locked-off tripod 3.0 m from the shelf, camera height 1.40 m, eye-level medium shot, full profile.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands · torso
Scene 11 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The glove rests on the scratched wing-mark for two full seconds, then slides to the carry handle and closes on it.

TIMELINE: 0.0s — the glove is already on the core, two fingers over the scratched wing-mark. 2.0s — the fingers stay on the mark for two seconds; then the glove slides along the frosted metal to the carry handle. 6.0s — the glove closes on the handle and takes the weight, the sleeve drawing taut through the last second.

CAMERA: 35mm lens on a fixed locked-off tripod 3.0 m from the shelf, camera height 1.40 m, eye-level medium shot, full profile, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Inside the unheated station at about one atmosphere, gravity is 0.38 g; frost coats every surface and nothing drips.
AUDIO: near silence inside — a faint crackle of frost, her breathing inside the helmet, no hum. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 11 — AĞIRLIK

```
SÜRE: 10 s · ZAMAN: 1:50,0 · VURUŞ: tartışma
KURULUM: I · dönüş · 24mm · WS · eye-level wide shot, three-quarter front · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 12 of 48.
She stands in the station doorway with the core at hip height, knees bent, the wing rig swaying at her back; past the door the band of drops hangs lower.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. On her back a folding wing rig, two dark smoke-grey membranes folded flat along her spine on a pale grey spar frame, held by one steel chest buckle, the only thing on her back. She holds a matt dark-metal cylinder the size of a small keg with a carry handle on each side by both handles at hip height. The station door frame around her; past it the band of drops. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 6.0 m from the station door, camera height 1.20 m, eye-level wide shot, three-quarter front. — the same position, height and lens as Scene 10.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 12 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She lifts the core from knee height to hip height and holds it there, knees bent, the lift slowing in its last hand's width; the wing rig sways once at her back.

TIMELINE: 0.0s — she is already bent at the knees in the doorway, both gloves on the handles, the core off the floor. 3.0s — the core rises to hip height, the last hand's width slower than the first; her shoulders drop into the weight and the wing rig sways once at her back. 7.0s — she keeps the core at hip height through the last second, knees bent, breath lifting her shoulders once.

CAMERA: 24mm lens on a fixed locked-off tripod 6.0 m from the station door, camera height 1.20 m, eye-level wide shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 10. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---
