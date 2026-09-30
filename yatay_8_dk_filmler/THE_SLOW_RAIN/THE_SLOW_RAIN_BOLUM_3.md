# 🎬 THE_SLOW_RAIN — BÖLÜM 3  (S24 – S35)

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
> Bölüm sınırı ardışık bir çifttir: S35 (Y · CU · az 90°) ↔ S36 (O · MS · az 0°) · 1 kademe · 90° ✅
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_8_dk_filmler/THE_SLOW_RAIN`

---

## 🎬 SAHNE 24 — DAMLALARIN ARASINDA

```
SÜRE: 10 s · ZAMAN: 4:00,0 · VURUŞ: ORTA NOKTA · novum 4. nesne · ⭐VİRAL
KURULUM: R · küme S23 · 35mm · MS · eye-level medium shot, three-quarter front · IN FRAME: face · torso · legs · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · torso · legs
Scene 25 of 48.
Large sparse drops, few enough to count, fall past her at shoulder height at a slow jogging pace; three meet her helmet rim in the take, each flashing into a white puff.

her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim, a thin white rime along the top edge of the helmet rim, the strap over her right shoulder. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 24.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · torso · legs
Scene 25 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Three drops meet the helmet rim in the take and each flashes into a white puff that falls back as dry snow within two seconds; she keeps walking at the same rate.

TIMELINE: 0.0s — she is already walking between the drops, one drop a hand's width above the helmet rim. 1.5s — the drop meets the rim and puffs white; she blinks and her jaw sets; the puff falls away as dry snow. 5.0s — a second and a third drop meet the rim and puff; she keeps walking at the same rate through the last second, eyes ahead.

CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 24. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 25 — VİZÖR

```
SÜRE: 10 s · ZAMAN: 4:10,0 · VURUŞ: tepki · ⭐ tema indeksi · ⭐VİRAL
KURULUM: S · ilk kullanım · 75mm · CU · eye-level close-up, frontal · IN FRAME: face · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face
Scene 26 of 48.
A band of white rime, two fingers wide, sits along the top edge of the helmet rim above the clear pane, and the back of her right glove wipes it once.

Close on the helmet: the low hard off-white shell, the single flat front pane inside its thick dark rim, a band of white rime two fingers wide along the top edge of the rim. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. The pale lakebed and the amber haze past her shoulder. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 75mm lens on a fixed locked-off tripod 1.4 m in front of her visor, camera height 1.60 m, eye-level close-up, frontal.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face
Scene 26 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The back of the glove wipes the rime off the top of the rim once, and by the last frame the band is back to the same width.

TIMELINE: 0.0s — the rime is already on the rim; her right glove is rising toward it, her eyes narrowed under it. 2.0s — the back of the glove wipes across the rim once and the rime comes away; she blinks. 6.0s — the rime creeps back along the rim to the same width through the last second while her eyes go back to the way ahead.

CAMERA: 75mm lens on a fixed locked-off tripod 1.4 m in front of her visor, camera height 1.60 m, eye-level close-up, frontal, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 26 — KIZAK KAYAR

```
SÜRE: 10 s · ZAMAN: 4:20,0 · VURUŞ: SAHTE YENİLGİ
KURULUM: T · ilk kullanım · 35mm · MS · high angle medium shot, three-quarter rear · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 27 of 48.
The sled slides over the lip of a dark pool and the core goes a hand deep into the liquid; her boots slide on the frost as she leans back on the strap.

Seen from above and behind: A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. the back of the suit is one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing; the strap from her shoulder to the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top at the pool lip. A flat dark matte pool in the frost below the lip. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 27 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The sled slides over the lip and the core sinks a hand deep; she leans back on the strap and her boots cut grooves in the frost.

TIMELINE: 0.0s — the sled is already tipping over the pool lip, the strap taut, her weight back. 2.0s — the core goes a hand deep into the liquid and the sled stops on the lip; her boots slide and cut two grooves in the frost. 6.0s — she keeps leaning back on the strap through the last second, boots dug in, the liquid flat around the core.

CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The back of the suit stays one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 27 — ÇAKILI

```
SÜRE: 10 s · ZAMAN: 4:30,0 · VURUŞ: DENEME 3
KURULUM: T · küme S26 · 35mm · MS · high angle medium shot, three-quarter rear · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 28 of 48.
She hauls on the strap and the sled does not come; the wing frame is under the surface and only one pale spar tip shows above the flat dark liquid.

Seen from above and behind: A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. the back of the suit is one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing; the strap from her shoulder into the pool, one pale spar tip and the core's top showing above the liquid. The flat dark matte pool below the lip. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 27.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 28 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She hauls on the strap three times and the sled does not move, the third pull shorter than the first; the spar tip stays where it is.

TIMELINE: 0.0s — she is already leaning back on the taut strap, both gloves on it. 3.0s — she pulls again; the strap stays taut and nothing comes; her shoulders drop. 7.0s — the third pull is shorter than the first and she keeps the strap taut through the last second, boots dug in.

CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 27. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The back of the suit stays one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 28 — BELE KADAR

```
SÜRE: 10 s · ZAMAN: 4:40,0 · VURUŞ: tırmanış · beden bedeli
KURULUM: T · küme S27 · 35mm · MS · high angle medium shot, three-quarter rear · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 29 of 48.
She stands waist-deep in the flat dark liquid beside the sunk sled, seen from above and behind, both gloves on the core strap.

Seen from above and behind: A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. the back of the suit is one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing; she is in the pool to the waist, the suit dark and wet below and crusted pale above, both gloves on the core strap. The flat dark pool around her to its far edge. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 28.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 29 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She works the core strap free a buckle at a time while waist-deep, every move slowed by the liquid; the sled stays under.

TIMELINE: 0.0s — she is already in the pool to the waist beside the sled, both gloves on the core strap. 3.0s — the first buckle gives; she moves her gloves to the second, each move slower than it would be in air. 7.0s — she keeps working the strap at the same slow rate through the last second, the liquid flat at her waist.

CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 28. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The back of the suit stays one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 29 — KAYIŞI KESER

```
SÜRE: 10 s · ZAMAN: 4:50,0 · VURUŞ: HER ŞEYİN KAYBI (bedel) · ⭐VİRAL
KURULUM: Y · ilk kullanım · 75mm · CU · eye-level close-up, full profile · IN FRAME: face · hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · hands · torso
Scene 30 of 48.
Her left glove is on the chest strap buckle with two fingers straightened and stopped a finger's width short of it; the core is against her chest and the pale wing spar lies under the liquid beside her.

In full profile close: her chest plates and the teal band, the strap buckle, a matt dark-metal cylinder the size of a small keg with a carry handle on each side against her chest, her left glove at the buckle with a small hooked cutter on its wrist, two fingers straightened. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. Beside her the flat dark liquid with one pale spar tip under its surface; beyond it the far edge of the lakebed. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 75mm lens on a fixed locked-off tripod 1.5 m from her chest, camera height 1.40 m, eye-level close-up, full profile.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · hands · torso
Scene 30 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The two fingers hold a finger's width off the buckle for two seconds, then the wrist cutter parts the strap without the tap; the core comes into both arms against her chest and the cut strap-end hangs from the buckle while the spar stays under the liquid.

TIMELINE: 0.0s — the cutter is already at the strap, two fingers straightened a finger's width off the buckle, her lips parted, eyes on the buckle, shoulders high. 2.0s — the fingers stay stopped for two seconds; then the cutter parts the strap and her eyes close for one blink. 4.0s — both arms close around the core against her chest, the cut strap-end swinging from the buckle; her shoulders drop and stay down through the last second, the spar under the liquid beside her.

CAMERA: 75mm lens on a fixed locked-off tripod 1.5 m from her chest, camera height 1.40 m, eye-level close-up, full profile, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 30 — BATIŞ

```
SÜRE: 10 s · ZAMAN: 5:00,0 · VURUŞ: bedel sonrası · KESİLEMEZ
KURULUM: T · dönüş · 35mm · MS · high angle medium shot, three-quarter rear · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 31 of 48.
The wing frame goes under at one steady rate at the left edge of the frame while she crawls up the pool lip on knees and one elbow, the core under her chest.

Seen from above and behind: A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. the back of the suit is one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing; the suit dark and wet to the chest, a matt dark-metal cylinder the size of a small keg with a carry handle on each side under her chest as she crawls; at the left edge one pale spar tip going under. The pool lip and the pale frost beyond. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear. — the same position, height and lens as Scene 29.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 31 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She crawls up the lip on knees and one elbow with the core under her, and the spar tip goes under the surface at one steady rate at the frame edge.

TIMELINE: 0.0s — she is already on the lip on both knees and one elbow, the core under her chest, the spar tip showing at the frame edge. 3.0s — she gains a knee's length up the lip; the spar tip is lower in the liquid. 7.0s — she keeps crawling at the same rate through the last second; the spar tip is nearly under.

CAMERA: 35mm lens on a fixed locked-off tripod 4.0 m from the pool edge, camera height 2.20 m, high angle medium shot looking down twenty degrees, three-quarter rear, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 29. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The back of the suit stays one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 31 — AYAĞA

```
SÜRE: 10 s · ZAMAN: 5:10,0 · VURUŞ: toparlanma
KURULUM: V · ilk kullanım · 24mm · WS · eye-level wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 32 of 48.
She rises from her knees to her feet with the core hugged to her chest, the wet suit crusted white to the chest, and her first steps are half a boot shorter than before.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. The suit dark and wet to the chest under a pale crust of dry snow; a matt dark-metal cylinder the size of a small keg with a carry handle on each side hugged to her chest in both arms. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m from her, camera height 1.50 m, eye-level wide shot, full profile.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 32 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She rises from her knees to her feet under the core, the crust on the suit cracking as she straightens, and walks on with steps half a boot shorter than before.

TIMELINE: 0.0s — she is already on one knee with the core against her chest, the other boot planted. 3.0s — she rises to her feet and the crust across the suit cracks; the first step is half a boot short. 7.0s — she keeps walking at the same short pace through the last second, the core hugged to her chest.

CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m from her, camera height 1.50 m, eye-level wide shot, full profile, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 32 — HER YERDE

```
SÜRE: 10 s · ZAMAN: 5:20,0 · VURUŞ: tırmanış · ortam kalıcı
KURULUM: V · küme S31 · 24mm · WS · eye-level wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 33 of 48.
Drops land a body-length ahead of her and a body-length in her wake, each leaving a dark ring, as she walks on with the core against her chest.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. The suit crusted pale to the chest; a matt dark-metal cylinder the size of a small keg with a carry handle on each side hugged to her chest. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles, few enough to count, fall through the frame at a slow jogging pace, far slower than rain on Earth, none streaking, none hanging still.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m from her, camera height 1.50 m, eye-level wide shot, full profile. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 32.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 33 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Drops land a body-length ahead of her and in her wake at one steady rate, each spreading a dark ring on the frost, and she keeps walking at the same pace.

TIMELINE: 0.0s — she is already walking, a drop landing a body-length ahead of her and ringing dark. 4.0s — another lands in her wake and rings; her helmet stays on the way ahead. 8.0s — she keeps walking at the same pace through the last second while the drops go on landing.

CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m from her, camera height 1.50 m, eye-level wide shot, full profile, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 32. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 33 — ŞERİT DARALIR

```
SÜRE: 10 s · ZAMAN: 5:30,0 · VURUŞ: SEÇİM (K) · ortamın değişimi
KURULUM: V · küme S32 · 24mm · WS · eye-level wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 34 of 48.
The pools have joined on both sides of a narrowing strip of dry frost; she turns onto the strip and keeps walking, liquid flat on both sides.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. The suit crusted pale to the chest; a matt dark-metal cylinder the size of a small keg with a carry handle on each side hugged to her chest. A strip of pale frost three strides wide between two flat dark pools. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m from her, camera height 1.50 m, eye-level wide shot, full profile. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 33.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 34 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She turns onto the narrowing dry strip in one movement and keeps walking along it at the same pace, the liquid flat on both sides.

TIMELINE: 0.0s — she is already at the head of the strip, the pools joined on her left and right. 2.0s — she turns onto the strip in one step, her weight going to the left boot first. 6.0s — she keeps walking the strip at the same pace through the last second, liquid flat on both sides.

CAMERA: 24mm lens on a fixed locked-off tripod 8.0 m from her, camera height 1.50 m, eye-level wide shot, full profile, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 33. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 34 — SICAK

```
SÜRE: 10 s · ZAMAN: 5:40,0 · VURUŞ: umut-önce · keşif
KURULUM: O · ilk kullanım · 50mm · MS · high angle medium shot looking down · IN FRAME: hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands · torso
Scene 35 of 48.
Seen from above, the core stands on the frost with both her gloves on it, and the frost around its base has gone dark in a ring the width of her boot while one thin white puff rises off it.

Seen from above: a matt dark-metal cylinder the size of a small keg with a carry handle on each side standing on the frost with both her gloves on its top, her helmet and shoulders at the top of the frame. A ring of dark bare bedrock the width of her boot around the core's base, a thin white puff rising off it. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal. — the same position, height and lens as Scene 22.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands · torso
Scene 35 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The dark ring around the core's base widens a finger's width and a thin white puff rises to knee height straight up and falls back as dry snow within two seconds; her gloves stay on the core.

TIMELINE: 0.0s — both gloves are already on the top of the core, the dark ring around its base a boot wide. 2.0s — a thin white puff rises straight up off the ring to knee height and falls back as dry snow; her shoulders rise twice with fast breaths. 6.0s — the ring widens a finger's width and her gloves stay on the core through the last second, the breaths slowing.

CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 22. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 35 — GÖĞSE

```
SÜRE: 10 s · ZAMAN: 5:50,0 · VURUŞ: UMUT-ÖNCE-DÜŞÜŞ · ⭐ · ⭐VİRAL
KURULUM: Y · ilk kullanım · 75mm · CU · eye-level close-up, full profile · IN FRAME: face · hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · hands · torso
Scene 36 of 48.
In full profile close, the core is pressed to her chest with both arms and the pale crust on the front of the suit comes off in flakes, one every second, falling away below the frame.

In full profile close: her chest plates and the teal band under a pale crust, a matt dark-metal cylinder the size of a small keg with a carry handle on each side pressed to her chest in both arms. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. The pale lakebed and the amber haze past her shoulder. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 75mm lens on a fixed locked-off tripod 1.5 m from her chest, camera height 1.40 m, eye-level close-up, full profile. — the same position, height and lens as Scene 30.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · hands · torso
Scene 36 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Flakes of crust drop off the front of the suit one after another at one steady rate while she holds the core to her chest and her arms open a hand's width wider.

TIMELINE: 0.0s — the core is already pressed to her chest, both arms closed on it, the crust whole across the front of the suit. 2.0s — the first flake drops off the chest plate; her eyes close and her lips loosen with a long breath. 5.0s — flakes keep dropping at the same rate through the last second, her arms opening a hand's width wider, the core against her chest.

CAMERA: 75mm lens on a fixed locked-off tripod 1.5 m from her chest, camera height 1.40 m, eye-level close-up, full profile, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 30. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---
