# 🎬 SUSMAYAN_NOBETCI — BÖLÜM 1  (S0 – S11)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `SUSMAYAN_NOBETCI_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③). ⭐ self-contained ≠ Bible'ın
> tamamı — yalnız `IN FRAME:` satırındaki tarif edilir [D214].
>
> ⭐ **YENİ REJİM:** ilk satır `IN FRAME:` (㉖) · POZİTİF gövde IMAGE 100-250 / VIDEO 120-300 kelime (①) ·
> NEGATIVE = §5.1 çekirdek (image 7 · video 8) + ≤3 sahneye özel (㉗) · video tek satır `START FRAME:`.
> ⭐ **OMNI katmanı:** CAMERA "In a single continuous shot." ile biter · AUDIO "No dialogue. No music." · tırnak 0.
> ⭐ **Promptta "Scene n of 48" = S + 1.** Dönüş ve küme işaretleri de bu numarayı kullanır.
> ⛔ İnsansız sahnelerde NEGATIVE kısadır (<900 karakter) ve "no human figures" kalıbı YAZILMAZ —
> yapısal red profili [red defteri #2 · COLD BURN S8].
> ⛔ Replikler klipte ÜRETİLMEZ (post-dub); saniyesi sahne bilgi bloğunda, promptta değil.
>
> Bölüm sınırı ardışık bir çifttir: S11 (I · MS) ↔ S12 (C · CU) · 1 kademe · mekân değişir.
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_8_dk_filmler/SUSMAYAN_NOBETCI`

---

## 🎬 SAHNE 0 — MOTOR YANAR, GÖVDE AYRILIR

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:00,0 · VURUŞ: Açılış · HOOK · kural
KURULUM: A · ilk kullanım · 35mm · MS · OTS · IN FRAME: hands, back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands, back
Scene 1 of 48.
Far beyond the canopy a small shuttle drifts whole with a straight white cone burning at its tail; her right glove rests a palm above the main engine lever and does not touch it.

From back of her right shoulder: helmet and shoulder fill the left third, her right glove open a palm above the main engine lever. The back of her suit is one continuous ribbed surface from collar to hip, closed and smooth, the two shoulder caps wrapping over its upper edge. She wears a worn off-white quilted pressure suit with broad padded shoulder caps, one safety-orange band on the left upper arm and heavy dark-grey gloves. The cabin is short and boxy: a three-panel canopy and a left console at hip height with a plain half-round gauge and a hinged release cover. Through the canopy: A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame. Far out a small shuttle drifts, its cone steady.
LIGHT: an even neutral 4500K panel in the cabin ceiling; outside the canopy hard sunlight from the upper left, the shadow side of every surface out there pure black.
CAMERA: 35mm lens on a fixed locked-off mount at shoulder height, 1 m back from her right shoulder, over-the-shoulder medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No explosion, no fireball, no flame and no smoke anywhere in the frame. No beam, no tracer and no visible projectile crosses the frame. No back-mounted unit, tank, hose or rear housing on her suit.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands, back
Scene 1 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Three seconds in, the shuttle's hull parts at its middle seam and the two halves move apart, turning; her glove never touches the lever.

TIMELINE: 0.0s — the shuttle drifts with its cone burning and her glove stays open a palm above the lever. 3.0s — a single white point the size of a fist flashes at the seam for a quarter of a second and leaves no afterglow, the hull parts into two halves that move apart and keep turning about once every three seconds, and a short cone of ice crystals spreads from the seam in straight lines and thins out within two seconds. 5.0s — her fingers stay spread above the lever and the two halves keep opening across the canopy at the same rate.

CAMERA: 35mm lens on a fixed locked-off mount at shoulder height, 1 m back from her right shoulder, over-the-shoulder medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Her back stays one continuous ribbed surface from collar to hip, closed and smooth, the shoulder caps wrapping over its upper edge. hard vacuum and zero gravity: the cone is a straight sharp shape that thins fast, the halves keep the spin they gained and never slow, nothing in the cabin falls.
AUDIO: a steady low cabin hum and her slow breathing inside the helmet; no exterior sound at all, the hull parts in silence. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No explosion, no fireball, no flame and no smoke anywhere in the frame. No beam, no tracer and no visible projectile crosses the frame. No back-mounted unit, tank, hose or rear housing on her suit.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 1 — PENCEREDE FENER

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:10,0 · VURUŞ: Kurulum · muhatap
KURULUM: B · ilk kullanım · 50mm · CU · profil · IN FRAME: face · REPLİK: 12,0 s · yetişkin (telsiz · post-dub)
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: face
Scene 2 of 48.
Her face is turned to the canopy and holds there; far outside, one of three small lit windows on the long ship carries a swinging hand lamp.

In profile from her right, a woman in her mid-forties with a broad square jaw and set lines at rest. Her helmet is a rounded hard off-white shell in a raised bronze collar ring, two small square lamps in the brow and a single flat front pane inside a thick dark-grey rim; a soft neutral 4500K fill from inside the rim lights her face, fully readable through the clear pane. She wears a worn off-white quilted pressure suit with broad padded shoulder caps, one safety-orange band on the left upper arm and heavy dark-grey gloves. Past the canopy frame the long ship is a small pale cylinder, three tiny windows lit warm in its midsection, one of them carrying a swinging lamp.
LIGHT: a soft neutral 4500K fill from inside the helmet rim on her face, the cabin at her back darker, one hard sunlit edge on the canopy frame.
CAMERA: 50mm lens on a fixed locked-off mount at eye height, 1 m from the right side of her helmet, side-on profile close-up, absolutely zero camera movement. In a single continuous shot.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No mouth movement and no speaking; her lips stay closed.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: face
Scene 2 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Her eyes stay on the far windows for the whole clip; her right glove reaches the lamp switch once and the cabin light answers with a single flash.

TIMELINE: 0.0s — she holds on the far window, breathing slowly, the swinging lamp a small point beyond the canopy frame. 3.0s — her eyes stay on it while her right glove comes up out of the lower frame to the lamp switch. 6.0s — she turns the switch once, the cabin light flashes bright and drops back, and she keeps watching the window with the lamp still swinging.

CAMERA: 50mm lens on a fixed locked-off mount at eye height, 1 m from the right side of her helmet, side-on profile close-up, absolutely zero camera movement. In a single continuous shot.
PHYSICS: zero gravity: her forearm floats a hand's width as it rises, the suit fabric moves slowly and settles, nothing falls.
AUDIO: a low cabin hum, her breathing inside the helmet, one short burst of radio static from the helmet speaker, no words. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No mouth movement and no speaking; her lips stay closed.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 2 — HAT KAYIYOR

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:20,0 · VURUŞ: Kurulum · engel
KURULUM: I · ilk kullanım · 35mm · MS · göz hizası · IN FRAME: torso · REPLİK: 25,0 s · yetişkin (telsiz · post-dub)
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: torso
Scene 3 of 48.
The tug is level with the long ship's docking ring and the ring already sits a body-length off its approach line, to the right of the tug's nose.

The tug is a short boxy hull about six body-lengths long: a three-panel canopy at the front, a plain ring on its nose with four clamp seats, one main engine at the tail, four corner thruster clusters and an orange-banded capsule in a cradle on its left flank. Through its canopy the pilot's small suited torso shows, too far for face detail. The long ship is a plain cylinder two and a half times the tug's length, three small windows at its midsection and a docking ring at the near end. A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame. One small steady white light hangs above that edge on the right and blinks once every two seconds.
LIGHT: hard sunlight from the upper left: the top faces of both hulls are bright, their shadow sides pure black, one cool sheen from the planet's edge along the tug's belly.
CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No tilt-shift look and no miniature read on either hull. No engine plume of any kind on the tug.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: torso
Scene 3 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The tug keeps its speed and its nose stays pointed at the long ship while the ring slides further off the approach line; no engine lights.

TIMELINE: 0.0s — the tug drifts toward the long ship on the right, nose steady, the ring a body-length off the line. 4.0s — the gap widens as the ring slides further right; the tug's main engine stays dark and nothing fires. 7.0s — the tug keeps drifting past at the same rate and the ring keeps sliding away from its nose.

CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: hard vacuum and zero gravity: both hulls hold a constant speed with no thrust, nothing accelerates, nothing drifts sideways on its own.
AUDIO: faint radio carrier hiss on the channel, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No tilt-shift look and no miniature read on either hull. No engine plume of any kind on the tug.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 3 — KANATLAR AÇIK

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:30,0 · VURUŞ: Kuralın kanıtı ①
KURULUM: C · ilk kullanım · 50mm · CU · üst açı · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 4 of 48.
On the console screen both radiator wings of the satellite are folded out, and at the right edge of the image the shuttle's rear half is still burning.

Her left glove rests at the edge of the console, two fingers on the frame of a palm-sized grey screen. The screen shows a grey image against black: a boxy satellite with one long straight rail housing, two flat radiator wings and one white sensor light, with no markings, no numbers and no frame lines. At the right edge of the image the shuttle's rear half tumbles with its cone still burning. Beside the screen on the console are the plain half-round gauge with its needle at three quarters, a closed hinged release cover and a stub thruster lever.
LIGHT: an even neutral 4500K panel overhead, the grey screen throwing a faint flat light on the back of her glove, no reflection on the console face.
CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings, numbers, scale marks or icons on the screen or the gauge.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 4 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Both wings stay folded out for the whole clip and the burning half is never struck.

TIMELINE: 0.0s — the wings are out, the rear half tumbles with its cone burning, her two fingers rest on the screen frame. 4.0s — the half keeps turning at the same rate and keeps burning while her fingers stay where they are. 7.0s — the wings are still out, the half still burns, and her glove does not move.

CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot.
PHYSICS: zero gravity in the cabin: her forearm floats a hand's width above the console; on the screen the tumbling half keeps a constant rate.
AUDIO: a low cabin hum, her breathing inside the helmet, a faint click as her fingers settle on the screen frame. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings, numbers, scale marks or icons on the screen or the gauge.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 4 — KANATLAR KAPANIR

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:40,0 · VURUŞ: Kuralın kanıtı ②
KURULUM: C · küme S3 · 50mm · CU · üst açı · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 5 of 48.
The satellite's two wings are folding back along its body while the shuttle's rear half still burns at the right edge of the screen.

Her left glove rests at the edge of the console, two fingers on the frame of the palm-sized grey screen. The screen shows a grey image against black: a boxy satellite with one long straight rail housing, two flat radiator wings and one white sensor light, with no markings, no numbers and no frame lines. The wings are halfway folded back along the body. At the right edge the shuttle's rear half tumbles with its cone still burning. The gauge beside the screen sits at three quarters and the release cover stays closed.
LIGHT: an even neutral 4500K panel overhead, the grey screen throwing a faint flat light on the back of her glove, no reflection on the console face.
CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot. continues the previous clip from its exact last frame — the same position, height and lens as Scene 4.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings, numbers or icons on the screen. No explosion, no fireball, no flame and no smoke on the screen or in the cabin.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 5 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The wings finish folding and three seconds later the burning half is struck and its cone goes out.

TIMELINE: 0.0s — the wings fold the rest of the way along the body and lock flat while the half keeps burning. 3.0s — a single white point the size of a fist flashes at the seam for a quarter of a second and leaves no afterglow on the screen, the half parts again into two pieces that move apart and keep turning, and its cone goes out with the piece that carries it. 6.0s — the pieces drift toward the right edge of the image, and her fingers stay on the screen frame.

CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot. continues the previous clip from its exact last frame — the same position, height and lens as Scene 4.
PHYSICS: zero gravity: the pieces keep the spin they gained and never slow; in the cabin her forearm floats a hand's width above the console.
AUDIO: a low cabin hum, her breathing inside the helmet, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings, numbers or icons on the screen. No explosion, no fireball, no flame and no smoke on the screen or in the cabin.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 5 — PENCERE KAÇAR

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:50,0 · VURUŞ: Katalizör (%10)
KURULUM: A · dönüş S0 · 35mm · MS · OTS · IN FRAME: hands, back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands, back
Scene 6 of 48.
Her right glove is a palm from the engine lever with the fingers straight, and the long ship's ring is already sliding across the canopy to the right.

From just back of her right shoulder: the back of her helmet and her right shoulder in the left third, her right glove raised a palm from the main engine lever, fingers straight. The back of her suit is one continuous ribbed surface from collar to hip, closed and smooth, the two shoulder caps wrapping over its upper edge. She wears a worn off-white quilted pressure suit with broad padded shoulder caps, one safety-orange band on the left upper arm and heavy dark-grey gloves. The cabin is short and boxy: a three-panel canopy and a left console at hip height with a plain half-round gauge and a hinged release cover. Through the canopy: A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame. The long ship's near ring crosses the canopy toward the right.
LIGHT: an even neutral 4500K panel in the cabin ceiling; outside the canopy hard sunlight from the upper left, shadow sides pure black.
CAMERA: 35mm lens on a fixed locked-off mount at shoulder height, 1 m back from her right shoulder, over-the-shoulder medium shot, deep focus, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 1.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No engine plume and no thruster flash anywhere in the frame. No back-mounted unit, tank, hose or rear housing on her suit.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands, back
Scene 6 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
Her glove holds a palm from the lever for eight seconds and never closes on it; the ring leaves the canopy on the right.

TIMELINE: 0.0s — her glove hangs a palm from the lever, fingers straight, while the ring slides across the canopy. 4.0s — the fingers spread wider and stay open as the ring reaches the right edge of the canopy. 8.0s — the ring passes out of the canopy, her glove stays where it is and her shoulders rise once with a slow breath.

CAMERA: 35mm lens on a fixed locked-off mount at shoulder height, 1 m back from her right shoulder, over-the-shoulder medium shot, deep focus, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 1.
PHYSICS: Her back stays one continuous ribbed surface from collar to hip, closed and smooth, the shoulder caps wrapping over its upper edge. zero gravity: her forearm floats, the suit fabric moves slowly; outside, the ships hold a constant speed with no thrust.
AUDIO: a low cabin hum and her breathing inside the helmet, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No engine plume and no thruster flash anywhere in the frame. No back-mounted unit, tank, hose or rear housing on her suit.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 6 — KAÇIŞ KAPAĞI

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 1:00,0 · VURUŞ: Tartışma · TOHUM
KURULUM: C · dönüş S3 · 50mm · CU · üst açı · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 7 of 48.
Her left thumb taps the hinged release cover twice and leaves it standing open.

Her left glove is over the console, the thumb on the hinged release cover beside the stub thruster lever. The screen shows a grey image against black: a boxy satellite with one long straight rail housing, two flat radiator wings and one white sensor light, with no markings, no numbers and no frame lines. The plain half-round gauge beside it holds its needle at three quarters. The cover is closed at the start, its small hinge bright where the paint has worn.
LIGHT: an even neutral 4500K panel overhead, the grey screen throwing a faint flat light across the back of her glove.
CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 4.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings or numbers on the gauge or the screen.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 7 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The thumb taps the cover twice, lifts it fully open, and then the glove pulls the stub thruster lever back once.

TIMELINE: 0.0s — the thumb comes down on the closed cover and taps it twice, the second tap slower than the first. 3.0s — the thumb hooks under the cover and lifts it until it stands fully open, and it stays open. 6.0s — the glove moves to the stub lever and pulls it back once, holding it there while the cabin trembles faintly.

CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 4.
PHYSICS: zero gravity: the cover stays where it is lifted; a short cold-gas burst outside is felt only as a faint tremble through the hull.
AUDIO: a low cabin hum, two soft taps through the glove, a short muffled hiss through the hull and her breathing inside the helmet. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings or numbers on the gauge or the screen.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 7 — GERI ÇEKILME

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 1:10,0 · VURUŞ: AYRILIK
KURULUM: I · dönüş S2 · 35mm · MS · göz hizası · IN FRAME: torso · REPLİK: 73,0 s · yetişkin (telsiz · post-dub)
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: torso
Scene 8 of 48.
The tug is backing away from the long ship, its four corner thrusters pointing forward, and the gap between the two hulls is already four tug-lengths.

The tug is a short boxy hull about six body-lengths long: a three-panel canopy at the front, a plain ring on its nose with four clamp seats, one main engine at the tail, four corner thruster clusters and an orange-banded capsule in a cradle on its left flank. Through its canopy the pilot's small suited torso shows, no face detail at this distance. The long ship is a plain cylinder two and a half times the tug's length, three small windows at its midsection and a docking ring at the near end. One of its three small windows carries a fast blinking lamp. A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame. One small steady white light hangs above that edge on the right and blinks once every two seconds.
LIGHT: hard sunlight from the upper left, the top faces of both hulls bright and their shadow sides pure black, one cool sheen from the planet's edge along the tug's belly.
CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 3.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No vapour cloud, no mist and no curling gas. No tilt-shift look and no miniature read on either hull.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: torso
Scene 8 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The gap grows steadily for ten seconds and the lamp in the long ship's window blinks faster than it did.

TIMELINE: 0.0s — short straight cold-gas cones snap from the tug's forward thruster clusters and vanish within a quarter of a second, and the tug moves away from the long ship. 4.0s — the gap keeps opening at the same rate; the lamp in the window blinks faster. 7.0s — another pair of short cones fires and dies, the tug keeps backing away, and the lamp keeps blinking.

CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 3.
PHYSICS: hard vacuum and zero gravity: each cold-gas cone is a straight transparent shape gone within a quarter second, no cloud and no curl; between bursts the tug holds a constant speed.
AUDIO: faint radio carrier hiss, one short burst of radio static from the speaker, no words, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No vapour cloud, no mist and no curling gas. No tilt-shift look and no miniature read on either hull.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 8 — KENARIN ARDI

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 1:20,0 · VURUŞ: Kurulum · harita
KURULUM: Y · ilk kullanım · 24mm · WS · göz hizası · IN FRAME: none · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 9 of 48.
The satellite's light sits a quarter of the frame height above the planet's edge on the right, and a second, fainter light waits just above the edge on the far left.

A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame. One small steady white light hangs above that edge on the right and blinks once every two seconds. On the far left, close above the edge, a second small light waits, dimmer and steady: a rescue ship holding out of the satellite's view. Between them the long ship and the tug are two small pale shapes near the middle of the frame, the tug on the left, its nose toward the other.
LIGHT: hard sunlight from the upper left; every hull is a bright edge against black, the planet's rim a thin bright band along the bottom.
CAMERA: 24mm lens on a fixed locked-off mount level with the tug, 400 m from the long ship, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.

NEGATIVE: Human count zero in this frame, no figure in the cockpit, no silhouette in any window. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any hull, panel, display or sign — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no waxy texture. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No stars anywhere in the frame. No tilt-shift look and no miniature read on any hull.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 9 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The satellite's light blinks once every two seconds and stays a quarter of the frame height above the edge for the whole clip.

TIMELINE: 0.0s — the two small ships hold their places, the satellite's light blinks on the right, the rescue light sits still on the left. 4.0s — the satellite's light blinks again at the same interval while the planet's edge stays exactly where it is. 8.0s — the ships drift a hair closer to the edge and the satellite's light blinks once more, unchanged in height.

CAMERA: 24mm lens on a fixed locked-off mount level with the tug, 400 m from the long ship, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: hard vacuum and zero gravity: nothing accelerates, no plumes anywhere, all four objects hold a constant drift.
AUDIO: faint radio carrier hiss, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, no figure in the cockpit, no silhouette in any window. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any hull, panel, display or sign — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no waxy texture. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No stars anywhere in the frame. No tilt-shift look and no miniature read on any hull.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 9 — BUĞU

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 1:30,0 · VURUŞ: Saat başlar
KURULUM: F · ilk kullanım · 50mm · MS · göz hizası · IN FRAME: none · REPLİK: 94,0 s · yetişkin (telsiz · post-dub)
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 10 of 48.
Three small windows in the long ship's midsection: all three are lit, two of them fogged along their inner edges.

The long ship is a plain cylinder two and a half times the tug's length, three small windows at its midsection and a docking ring at the near end. The frame holds its midsection: three small windows in a row, each lit warm from inside, the inner glass of the left and middle ones already fogged at the edges, a hand lamp swinging in the middle one. The hull around them is pale and scuffed, with a shallow line of worn paint under the windows. Beyond the hull: A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame.
LIGHT: hard sunlight from the upper left across the hull, the shadowed lower half pure black, the only other light the warm glow from inside the three windows.
CAMERA: 50mm lens on a fixed locked-off mount level with the windows, 12 m from the long ship's windows, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.

NEGATIVE: Human count zero in this frame, no figure in the cockpit, no silhouette in any window. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any hull, panel, display or sign — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no waxy texture. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No figure, silhouette or face visible in any window. No stars anywhere in the frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 10 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
All three windows stay lit and the fog on the inner glass stays exactly as it is; the lamp in the middle window swings at a steady rate.

TIMELINE: 0.0s — the lamp swings in the middle window, the fog holds along the inner edges of two windows. 4.0s — the lamp swings back the other way at the same rate; the hull drifts a little in frame and the windows stay lit. 8.0s — the lamp keeps swinging and the lit windows keep their places as the hull drifts on.

CAMERA: 50mm lens on a fixed locked-off mount level with the windows, 12 m from the long ship's windows, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: hard vacuum and zero gravity outside; inside the lit windows the lamp swings on its cord at a constant rate and never stops.
AUDIO: faint radio carrier hiss, one short burst of radio static from the channel, no words, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Human count zero in this frame, no figure in the cockpit, no silhouette in any window. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any hull, panel, display or sign — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no waxy texture. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No figure, silhouette or face visible in any window. No stars anywhere in the frame.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 10 — HORTUM HAZIR

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 1:40,0 · VURUŞ: Plan
KURULUM: C · dönüş S6 · 50mm · CU · üst açı · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 11 of 48.
A coiled air hose hangs from the console bracket beside a short steel bar, and the hinged release cover stands open.

Her left glove works at the console: a coiled pale air hose in her fingers, its end clipped into a bracket beside a short steel prying bar. The screen shows a grey image against black: a boxy satellite with one long straight rail housing, two flat radiator wings and one white sensor light, with no markings, no numbers and no frame lines. The half-round gauge holds its needle at three quarters, and the hinged release cover stands open beside it.
LIGHT: an even neutral 4500K panel overhead, a faint flat screen light on the back of her glove, no reflection on the console face.
CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 7.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings or numbers on the gauge or the screen.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 11 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The glove clips the hose end into the bracket, then the thumb taps the open release cover twice and leaves it open.

TIMELINE: 0.0s — the glove holds the coiled hose against the bracket and presses its end into the clip. 3.0s — the clip closes on the hose, the coil settles against the console and stays there. 6.0s — the glove moves to the open release cover and the thumb taps it twice, the second tap slower, then rests beside it.

CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 7.
PHYSICS: zero gravity: the hose coil floats slightly and holds its shape once clipped, nothing falls.
AUDIO: a low cabin hum, a dry click as the clip closes, two soft taps, and her breathing inside the helmet. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No markings or numbers on the gauge or the screen.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 11 — DÖNÜŞ YOLU

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 1:50,0 · VURUŞ: Tartışma sonu
KURULUM: I · dönüş S7 · 35mm · MS · göz hizası · IN FRAME: torso · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: torso
Scene 12 of 48.
The tug's nose is pointed back at the long ship and the gap is closing; behind them three small pieces of wreckage tumble the same way.

The tug is a short boxy hull about six body-lengths long: a three-panel canopy at the front, a plain ring on its nose with four clamp seats, one main engine at the tail, four corner thruster clusters and an orange-banded capsule in a cradle on its left flank. Through its canopy the pilot's small suited torso shows, no face detail at this distance. The long ship is a plain cylinder two and a half times the tug's length, three small windows at its midsection and a docking ring at the near end. Between and beyond them three small pale pieces of wreckage tumble slowly toward the long ship. A flat black sky with no stars. The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame. One small steady white light hangs above that edge on the right and blinks once every two seconds.
LIGHT: hard sunlight from the upper left, bright top faces and pure black shadow sides, one cool sheen from the planet's edge along the tug's belly.
CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 8.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No vapour cloud, no mist and no curling gas. No tilt-shift look and no miniature read on any hull.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: torso
Scene 12 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The tug closes on the long ship at a steady rate while the three pieces of wreckage keep tumbling at about one turn every three seconds.

TIMELINE: 0.0s — short straight cold-gas cones snap from the tug's rear clusters and vanish, and the tug begins closing the gap. 4.0s — the tug holds its course, nose on the long ship; the three pieces keep tumbling at the same rate, drifting toward it. 8.0s — the gap is visibly smaller, the pieces are nearer the long ship, and nothing has changed direction.

CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot. — the same position, height and lens as Scene 8.
PHYSICS: hard vacuum and zero gravity: cold-gas cones are straight and gone within a quarter second; the wreckage keeps the spin it gained and never slows.
AUDIO: faint radio carrier hiss, no exterior sound. No dialogue. No music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the hull or any panel in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, no melting or warping. No vapour cloud, no mist and no curling gas. No tilt-shift look and no miniature read on any hull.

Output: 16:9, no text, no watermark.
```

---
