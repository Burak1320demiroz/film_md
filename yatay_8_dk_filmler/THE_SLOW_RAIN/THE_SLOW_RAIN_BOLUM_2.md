# 🎬 THE_SLOW_RAIN — BÖLÜM 2  (S12 – S23)

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
> Bölüm sınırı ardışık bir çifttir: S23 ↔ S24 🕰️ KÜME (aynı kurulum R, işaretli devam klibi — QA yarımı S23↔S24 sınırı bilinçli küme)
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_8_dk_filmler/THE_SLOW_RAIN`

---

## 🎬 SAHNE 12 — ÇATIYA

```
SÜRE: 10 s · ZAMAN: 2:00,0 · VURUŞ: tartışma → deneme
KURULUM: G · ilk kullanım · 24mm · EWS · low angle extreme wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 13 of 48.
She stands on the station roof in full profile strapping the core high on her chest; her right glove tugs the buckle twice.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. On her back a folding wing rig, two dark smoke-grey membranes folded flat along her spine on a pale grey spar frame, held by one steel chest buckle, the only thing on her back. a matt dark-metal cylinder the size of a small keg with a carry handle on each side is strapped high on her chest under the buckle. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The old station in the left third, a low dark module barely taller than she is, one door, a flat roof.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile. — the same position, height and lens as Scene 9.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 13 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Her glove tugs the buckle exactly twice over the strapped core, then she straightens and steps to the roof edge, wings still folded.

TIMELINE: 0.0s — she is already on the roof, the core against her chest, both gloves on the harness strap. 3.0s — the strap draws tight over the core; her glove tugs the buckle twice. 7.0s — she straightens under the weight and takes two steps toward the roof edge through the last second, wings folded.

CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 9. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 13 — ÇAKILMA

```
SÜRE: 10 s · ZAMAN: 2:10,0 · VURUŞ: DENEME 1 · sahte umut düşer
KURULUM: G · küme S12 · 24mm · EWS · low angle extreme wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 14 of 48.
She goes off the roof edge with the core on her chest; the wings open, cannot hold the air, and she drops at twice the glide rate to the frost.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. her wing rig open, two dark smoke-grey membranes on a pale grey spar frame spanning twice her arm-span, held by one steel chest buckle, the only thing on her back, the core strapped on her chest. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The old station in the left third, a low dark module barely taller than she is, one door, a flat roof.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 13.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 14 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The wings open and cannot hold the air: she drops at twice the glide rate and meets the lakebed frost on her side, one wing folding under her.

TIMELINE: 0.0s — she is already off the roof edge, wings opening, the core on her chest. 2.0s — the wings take no lift and she drops at twice the glide rate, one wing folding under her as she meets the frost on her side. 5.0s — she lies where she landed, one wing bent under her, the core against her chest; her shoulders rise with a slow heavy breath through the last second.

CAMERA: 24mm lens on a fixed locked-off tripod on the lakebed 16 m from the old station, camera height 0.50 m, low angle extreme wide shot looking up, full profile, deep focus, fixed lockoff — absolutely zero camera movement. Continues the previous clip from its exact last frame — the same position, height and lens as Scene 13. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 14 — YERDE

```
SÜRE: 10 s · ZAMAN: 2:20,0 · VURUŞ: tepki · ironi kapanışı
KURULUM: N · ilk kullanım · 24mm · WS · low angle wide shot, full profile · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 15 of 48.
She sits up on one hip on the frost, the core strap half undone, one wing bent under her; the band of drops hangs at her head height.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. One wing of the rig is bent under her hip, the other open flat on the frost; a matt dark-metal cylinder the size of a small keg with a carry handle on each side is on her lap, its strap half undone. The band of drops just above her helmet. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 7.0 m from her, camera height 0.30 m, low angle wide shot, full profile.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 15 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She sits up from lying to one hip and works the core strap loose one buckle at a time; her helmet lifts to the drops above and locks there.

TIMELINE: 0.0s — she is lying on her side on the frost, one wing under her, the core strap still buckled. 2.0s — she pushes up onto one hip, shoulders lifting into the push and dropping, and her helmet lifts to the drops just above her; it stays there. 5.0s — her gloves work the core strap loose one buckle at a time through the last second, the helmet on the drops.

CAMERA: 24mm lens on a fixed locked-off tripod 7.0 m from her, camera height 0.30 m, low angle wide shot, full profile, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 15 — KANATLAR YERE

```
SÜRE: 10 s · ZAMAN: 2:30,0 · VURUŞ: ORTA NOKTA ÖNCESİ SEÇİM (K)
KURULUM: O · ilk kullanım · 50mm · MS · high angle medium shot looking down · IN FRAME: hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands · torso
Scene 16 of 48.
The wing rig lies flat on the frost with the core strapped onto its upper surface, and her gloves cinch the strap over the core; the empty back harness lies beside it.

Seen from above: the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top; both her gloves are on the strap, her helmet and shoulders at the top of the frame, the empty back harness with its steel buckle on the frost beside the rig. Frost around the rig, dusted pale grey. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands · torso
Scene 16 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Her gloves cinch the strap over the core a notch at a time, the strap drawing tight across the metal; the harness stays on the frost beside the rig.

TIMELINE: 0.0s — both gloves are already on the strap over the core, the wing rig flat under it. 3.0s — the strap draws a notch tighter; her gloves stop a palm's width off the buckle for two seconds, then close on it and pull. 7.0s — she keeps cinching at the same rate through the last second, shoulders dropping into each pull, the harness on the frost beside her.

CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 16 — ÇEKİŞ

```
SÜRE: 10 s · ZAMAN: 2:40,0 · VURUŞ: ilerleme
KURULUM: P · ilk kullanım · 24mm · WS · eye-level wide shot, three-quarter front · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 17 of 48.
The sled strap over her right shoulder, she hauls the sled toward the base dome in the right third; the sled trails a body-length back.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. A strap runs from her right shoulder back to the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 9.0 m from her, camera height 1.50 m, eye-level wide shot, three-quarter front.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 17 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She hauls the sled toward the dome at one steady rate, leaning into the strap until her shoulders sit below her hips, the sled trailing a body-length back.

TIMELINE: 0.0s — she is already leaning into the strap, weight on the front boot, the sled trailing a body-length back. 4.0s — her shoulders drop below her hips into the haul; the sled slides on the frost at the same rate. 8.0s — she keeps hauling toward the dome through the last second, nothing in her grip relaxing.

CAMERA: 24mm lens on a fixed locked-off tripod 9.0 m from her, camera height 1.50 m, eye-level wide shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 17 — KABUK

```
SÜRE: 10 s · ZAMAN: 2:50,0 · VURUŞ: ilerleme · tırmanış
KURULUM: O · dönüş · 50mm · MS · high angle medium shot looking down · IN FRAME: hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands · torso
Scene 18 of 48.
Seen from above, two drops land on the wet dark wing membrane of the sled and a dusting of dry snow clings where the membrane is wet; her gloves stay on the strap at the top of the frame.

Seen from above: the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top; her gloves and the strap at the top of the frame. Frost dusting pale grey around the sled. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. Large sparse drops the size of marbles, few enough to count, fall through the frame at a slow jogging pace, far slower than rain on Earth, none streaking, none hanging still.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal. — the same position, height and lens as Scene 16.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands · torso
Scene 18 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Two drops land on the wet membrane at a slow jogging pace and leave two dark wet rings that hold dry snow; she keeps hauling.

TIMELINE: 0.0s — the sled is already sliding under the strap, the membrane dark and wet in two places. 3.0s — a drop lands on the membrane and spreads into a dark ring; dry snow clings to the wet ring. 7.0s — a second drop lands and rings; her gloves keep the strap moving at the same rate through the last second.

CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 16. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 18 — KAZIMA

```
SÜRE: 10 s · ZAMAN: 3:00,0 · VURUŞ: DENEME 2
KURULUM: P · dönüş · 24mm · WS · eye-level wide shot, three-quarter front · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 19 of 48.
She stands over the sled scraping the crusted wing surface with a pale grey spar, one stroke every two seconds; fresh drops are already landing where she has cleared.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. She holds a pale grey wing-spar in both gloves over the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top. Drops descending around her. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 9.0 m from her, camera height 1.50 m, eye-level wide shot, three-quarter front. — the same position, height and lens as Scene 17.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 19 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She scrapes the crust off the wing surface with the spar at one steady rate, the fourth stroke slower than the first, and fresh drops land where she has cleared.

TIMELINE: 0.0s — she is already bent over the sled, the spar on the membrane, weight on the front boot. 3.0s — the spar drags a strip of crust off the membrane; a drop lands on the cleared strip. 7.0s — the fourth stroke comes slower than the first and she keeps scraping through the last second, shoulders low.

CAMERA: 24mm lens on a fixed locked-off tripod 9.0 m from her, camera height 1.50 m, eye-level wide shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 17. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 19 — KESİM

```
SÜRE: 10 s · ZAMAN: 3:10,0 · VURUŞ: SEÇİM (K) · ⭐ tema indeksi
KURULUM: O · dönüş · 50mm · MS · high angle medium shot looking down · IN FRAME: hands · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands · torso
Scene 20 of 48.
Seen from above, a hooked cutter on her left wrist parts the crusted outer section of the wing membrane along its spar; the cut section falls onto the frost and lies there in the centre of the frame.

Seen from above: the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top; her left glove with a small hooked cutter on its wrist is on the membrane, her right glove on the spar. Frost dusting pale grey around the sled. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal. — the same position, height and lens as Scene 18.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands · torso
Scene 20 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The wrist cutter parts the outer wing section along its spar within the first two seconds; the cut section drops onto the frost and stays there while she takes up the strap again.

TIMELINE: 0.0s — the cutter is already hooked into the membrane at the spar, her right glove holding the section. 1.5s — the membrane parts along the spar, her shoulders dropping into the cut, and the cut section falls flat onto the frost, dark on pale. 4.0s — the cut section lies where it fell in the centre of the frame; her gloves go back to the strap and pull through the last second.

CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 18. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 20 — UZAKTA YERE

```
SÜRE: 10 s · ZAMAN: 3:20,0 · VURUŞ: tırmanış · muhatap ortam
KURULUM: Q · ilk kullanım · 24mm · WS · eye-level wide shot, back to the lens · IN FRAME: full body · back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body · back
Scene 21 of 48.
Her back to the lens, she hauls the sled toward the dome; in the near foreground drops are landing and spreading into dark patches on the frost.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. the back of the suit is one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing; the strap from her shoulder to the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top behind her. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 9.0 m behind her, camera height 1.50 m, eye-level wide shot, her back to the lens.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body · back
Scene 21 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She hauls on toward the dome at one steady rate while the dark patches at the near edge keep spreading, one drop landing every few seconds.

TIMELINE: 0.0s — she is already hauling away from the lens, the sled trailing her, dark patches on the frost in the near foreground. 3.0s — a drop lands in the foreground and spreads into a new dark patch; her stride breaks for one step and resumes, her shoulders sitting below her hips in the strap, two breaths per stride. 7.0s — she keeps hauling toward the dome through the last second; the patches go on spreading at one steady rate.

CAMERA: 24mm lens on a fixed locked-off tripod 9.0 m behind her, camera height 1.50 m, eye-level wide shot, her back to the lens, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
The back of the suit stays one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 21 — GERİDE KALAN

```
SÜRE: 10 s · ZAMAN: 3:30,0 · VURUŞ: ilerleme
KURULUM: O · dönüş · 50mm · MS · high angle medium shot looking down · IN FRAME: hands · torso · legs · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands · torso · legs
Scene 22 of 48.
Seen from above, the cut wing section lies on the frost in the lower third of the frame while she and the sled pass through the upper third without her helmet turning to it.

Seen from above: the cut dark smoke-grey wing section flat on the frost in the lower third; above it her boots, legs and the strap, and the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top sliding past. Frost dusting pale grey. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal. — the same position, height and lens as Scene 20.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands · torso · legs
Scene 22 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The cut section stays where it lies while she and the sled leave the top of the frame at one steady rate; her helmet never turns back.

TIMELINE: 0.0s — the cut section lies in the lower third; her boots and the sled are already crossing the upper third. 4.0s — the sled slides on past the section at the same rate; a drop lands beside the section and rings. 8.0s — she and the sled leave the top of the frame through the last second; the cut section stays in the lower third.

CAMERA: 50mm lens on a fixed locked-off tripod 2.2 m from the sled, camera height 1.90 m, high angle medium shot looking down thirty-five degrees, frontal, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 20. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 22 — ÇUKUR

```
SÜRE: 10 s · ZAMAN: 3:40,0 · VURUŞ: tırmanış · beden bedeli
KURULUM: N · ilk kullanım · 24mm · WS · low angle wide shot, full profile · IN FRAME: legs · torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: legs · torso
Scene 23 of 48.
Her right boot is in a pool of dark liquid to the knee and the suit leg above it is dark and wet with dry snow clinging to it; she works the boot back out a hand's width at a time.

A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim. Her right leg is in a flat dark pool to the knee, the suit leg above it dark and wet, pale dry snow clinging to the wet cloth of the suit. A flat dark matte pool in the frost; the strap and the sled trailing back. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 24mm lens on a fixed locked-off tripod 7.0 m from her, camera height 0.30 m, low angle wide shot, full profile. — the same position, height and lens as Scene 15.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: legs · torso
Scene 23 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She works the right boot out of the pool a hand's width at a time, leaning back on the strap, the wet leg dark to the knee.

TIMELINE: 0.0s — her right boot is already in the pool to the knee, her weight back on the left boot, both gloves on the strap. 3.0s — the boot comes up a hand's width and the liquid runs off it; the rear boot loads and the knee bends before she pulls again, the glove's segments tightening on the strap. 7.0s — she keeps working the boot out at the same rate through the last second, the wet leg dark, dry snow clinging to it.

CAMERA: 24mm lens on a fixed locked-off tripod 7.0 m from her, camera height 0.30 m, low angle wide shot, full profile, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 15. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs. The dark liquid stays flat and matte, no ripples, no waves, no flow.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 23 — YARI YOL

```
SÜRE: 10 s · ZAMAN: 3:50,0 · VURUŞ: ilerleme · BÖLÜM 1 sonu (S23↔S24 sınır çifti = küme)
KURULUM: R · ilk kullanım · 35mm · MS · eye-level medium shot, three-quarter front · IN FRAME: face · torso · legs · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face · torso · legs
Scene 24 of 48.
She walks toward the dome dragging the sled, the right leg stiffer than the left, and breaks the crust on that leg with one strike of the spar.

her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim, her right leg dark and wet to the knee with dry snow crusted on it, the strap over her right shoulder. Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair. An unbroken amber haze sky, no sun disc, no horizon glow. A flat dark lakebed of pale-dusted ice to a soft horizon at eye level. The base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window. Large sparse drops the size of marbles fall through the frame at a slow jogging pace, far slower than rain on Earth.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front. — the same position, height and lens as Scene 5.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face · torso · legs
Scene 24 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She walks on toward the dome at one steady rate, the right leg stiffer than the left, and strikes the crust on that leg once with the spar without stopping.

TIMELINE: 0.0s — she is already walking toward the dome, the strap taut over her shoulder, the right leg swinging stiff. 3.0s — the spar comes down once on the crusted leg and a plate of crust falls off; her stride does not stop. 7.0s — she keeps walking at the same rate through the last second, shoulders rising once with a breath.

CAMERA: 35mm lens on a fixed locked-off tripod 3.5 m from her, camera height 1.50 m, eye-level medium shot, three-quarter front, deep focus, fixed lockoff — absolutely zero camera movement. — the same position, height and lens as Scene 5. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible. No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.

Output: 16:9, no text, no watermark.
```

---
