# 🎬 THE_FALLING_WORLD — BÖLÜM 1  (S0 – S11)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_FALLING_WORLD_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③). ⭐ self-contained ≠ Bible'ın
> tamamı — yalnız `IN FRAME:` satırındaki tarif edilir [D214].
>
> ⭐ **YENİ REJİM:** ilk satır `IN FRAME:` (㉖) · POZİTİF gövde IMAGE 100-250 / VIDEO 120-300 kelime (①) ·
> NEGATIVE = §5.1 çekirdek (image 7 · video 8) + ≤3 sahneye özel (㉗) · video tek satır `START FRAME:`.
> ⭐ **OMNI katmanı:** CAMERA `In a single continuous shot.` ile biter · AUDIO her klipte dolu · tırnak 0.
> ⭐ **Promptta `Scene n of 48` = S + 1.** Dönüş ve küme işaretleri de bu numarayı kullanır.
> ⭐ **VİZÖR TAMAMEN OPAK** — `IN FRAME:` satırına `face` YAZILMAZ, D79 vizör cümlesi HİÇ girmez [PLAN D74 ③].
> ⭐ **KONUM KİLİDİ** her iki-figürlü promptta: BEYAZ solda, TURUNCU sağda, merkez çizgisi geçilmez.
> ⛔ İnsansız sahnelerde NEGATIVE kısadır (<900 karakter) ve "no human figures" kalıbı YAZILMAZ —
> yapısal red profili [red defteri #2 · KART 10].
> ⛔ Replikler klipte ÜRETİLMEZ (post-dub); saniyesi sahne bilgi bloğunda, promptta değil.
>
> Bölüm sınırı ardışık bir çifttir: S11 (F · MLS · eye level · 180°) ↔ S12 (I · WS · high angle · 45°) · 1 kademe · mekân değişir ✅
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_8_dk_filmler/THE_FALLING_WORLD`

---

## 🎬 SAHNE 0 — BİLEK

```
SÜRE: 10 s (VARSAYIM · ffprobe ⬜ K3) · ZAMAN: 0:00,0 · VURUŞ: Açılış imajı · HOOK (in medias res)
KURULUM: A · ilk kullanım · 24mm · MLS · low angle · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 1 of 48.
Both of his boots are braced against the plate edge and his glove is already closed around the other man's hard wrist cuff, and the thin yellow line between their belts hangs slack.

Left third: a man in a dirty off-white hard-shell suit with cobalt-blue shoulder caps and heavy dark-grey gloves, a short flat tool clipped along the outside of his left forearm, lying low with both boots braced on a rock plate edge. Right third: a second man sunk to the waist in a dark open crack, his suit burnt orange with black upper arms. Both panes are flat, set in thick dark-grey rims, and fully opaque matte black. A thin yellow line runs slack between their belts and a small grey crate hangs from the orange belt. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: one hard sun out of frame to the upper left, shadow edges soft, thin dust holding a faint glow at every edge.
CAMERA: 24mm lens on a fixed locked-off mount at ground level, 6 m from the crevasse edge, low angle medium long shot, deep focus, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No fabric, no cloth, no flapping or billowing material — both suits are hard shells. No wind, no rain, no liquid, no flame and no explosion anywhere in the frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 1 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The closed grip holds for the whole clip while the sunk man is drawn a hand higher and the slack yellow line never goes tight.

TIMELINE: 0.0s — the off-white glove is closed on the orange wrist cuff, both boots pressed into the plate edge, dust sliding past them into the crack. 4.0s — the off-white shoulders pull back, the orange man rises about a hand, and his free glove finds the plate rim; the yellow line between the belts stays slack. 8.0s — the grip is still closed, the orange man is a hand higher again, and two thin dust columns keep falling into the crack at the same steady rate.

CAMERA: 24mm lens on a fixed locked-off mount at ground level, 6 m from the crevasse edge, low angle medium long shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: a two metre fall takes about 1.17 seconds, dust rises in columns and settles slowly but certainly, and every broken piece keeps its rotation axis.
AUDIO: a low muffled rumble with no high frequencies, two separate breathing rhythms inside two helmets, dust sliding on rock. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No fabric, no cloth, no flapping or billowing material — both suits are hard shells. No wind, no rain, no liquid, no flame and no explosion anywhere in the frame.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 1 — SANDIK KAYIYOR

```
SÜRE: 10 s · ZAMAN: 0:10,0 · VURUŞ: Kurulum — hat ailesi tanıtılır (TOHUM: alet)
KURULUM: B · ilk kullanım · 50mm · CU · high angle · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 2 of 48.
Two different lines are in the same frame and they never touch: a thin grey strap holding the crate and a thicker yellow line running away to the left.

Close on the orange belt: a grey sample crate the size of two fists hangs from a thin grey strap hooked to a dark belt ring, sliding a finger's width towards the crack. A yellow line twice as thick as the strap runs from the same belt away to the left edge of frame. An off-white glove comes in from the left and pulls a short flat tool free from a clip on the outside of a left forearm; the tool is a flat bar the length of a hand with a blunt squared end. Dust runs past the belt in thin grey threads. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge.
LIGHT: one hard sun out of frame to the upper left, the belt ring bright on top and pure shadow underneath.
CAMERA: 50mm lens on a fixed locked-off mount at chest height, 1.2 m from the crate on his belt, high angle close-up, deep focus, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No third line, no extra cable and no rope that was not named. No fabric, no cloth, no flapping or billowing material — both suits are hard shells.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 2 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The grey strap slides while the flat tool is drawn clear and turned in the glove, and the yellow line stays still.

TIMELINE: 0.0s — the crate hangs from the grey strap and the off-white glove is closing on the tool clip. 3.5s — the tool comes free of the clip and turns once in the glove; at the same time the grey strap slides another finger's width and the crate swings out from the belt. 7.5s — the glove has the tool held flat and steady, the crate is still swinging, and the yellow line has not moved at all.

CAMERA: 50mm lens on a fixed locked-off mount at chest height, 1.2 m from the crate on his belt, high angle close-up, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the crate swings with a long slow period and settles back towards the belt, and loose dust falls about one glove-width in the first second.
AUDIO: a low muffled rumble, one set of breathing close in the helmet, small metal on metal as the clip lets go. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No third line, no extra cable and no rope that was not named. No fabric, no cloth, no flapping or billowing material — both suits are hard shells.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 2 — KAYIŞ AYRILIR

```
SÜRE: 10 s · ZAMAN: 0:20,0 · VURUŞ: Kurulum — kural kurulur (bir hat ayrılır, biri kalır)
KURULUM: B · küme S1 · 50mm · CU · high angle · IN FRAME: hands · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands
Scene 3 of 48.
The flat tool closes on the grey strap and only the grey strap: the yellow line stays in frame, untouched and slack, for the whole shot.

Close on the orange belt again: the grey sample crate hangs from its thin grey strap, the strap stretched thin over the belt ring. An off-white glove holds a short flat bar the length of a hand against the strap, a finger's width from the ring. The yellow line runs from the same belt out to the left edge of frame, slack and untouched. Dust threads fall past the ring. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge.
LIGHT: one hard sun out of frame to the upper left, the stretched strap a bright line, the belt ring in hard shadow beneath it.
CAMERA: 50mm lens on a fixed locked-off mount at chest height, 1.2 m from the crate on his belt, high angle close-up, deep focus, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 2. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No third line, no extra cable and no rope that was not named. Every damaged surface stays dry metal — dented shell, bent rim, torn seam and nothing else.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands
Scene 3 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The grey strap parts and drops away with the crate while the yellow line stays slack in frame and nothing else on the belt moves.

TIMELINE: 0.0s — the flat bar is held against the stretched grey strap a finger's width from the ring. 2.5s — the strap parts and the two ends spring apart; the crate drops straight down and leaves the bottom of frame within half a second. 6.0s — the empty grey end swings once from the ring and hangs, the yellow line is still slack across the frame, and the off-white glove draws the flat bar back out of frame to the left.

CAMERA: 50mm lens on a fixed locked-off mount at chest height, 1.2 m from the crate on his belt, high angle close-up, deep focus, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 2. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the crate falls about one glove-width in its first second and one arm-length in its second, and the loose strap end swings with a long slow period.
AUDIO: a low muffled rumble, one set of breathing close in the helmet, a short dry snap and then nothing falling. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No third line, no extra cable and no rope that was not named. Every damaged surface stays dry metal — dented shell, bent rim, torn seam and nothing else.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 3 — SIRTTAKİ GEMİ

```
SÜRE: 10 s · ZAMAN: 0:30,0 · VURUŞ: Kurulum — hedef ilan edilir · MÜZİK ilk giriş 2 s
KURULUM: A · dönüş S0 · 24mm · MLS · low angle · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 4 of 48.
An empty hook swings on the off-white belt where the crate was, and far ahead on a rock ridge a small ship stands on three legs.

Two men run away from the crack towards the rover at the right edge of frame. Left of centre: a dirty off-white suit with cobalt-blue shoulder caps, a short flat tool on the outside of the left forearm, an empty dark hook swinging on the belt. Right of centre: a burnt-orange suit. Both front panes are fully opaque matte black. A thin yellow line trails slack between their belts. Mid-frame a four-wheeled open-cage rover, its nose pointing away from camera; beyond it a low rock ridge carries a small ship on three legs. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: one hard sun out of frame to the upper left, shadow edges soft, thin dust holding a faint glow at every edge.
CAMERA: 24mm lens on a fixed locked-off mount at ground level, 6 m from the crevasse edge, low angle medium long shot, deep focus, absolutely zero camera movement. — the same position, height and lens as Scene 1. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 4 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The empty hook keeps swinging on the off-white belt through the whole run and the small ship on the ridge never changes size.

TIMELINE: 0.0s — both men are running away from camera in long low strides, the empty hook swinging at the off-white belt. 4.0s — the yellow line between them draws out and goes slack again as their strides fall out of step; dust lifts a glove-width at every boot and settles in their tracks. 8.5s — they are closer to the rover and smaller in frame, the hook still swinging, the ship on the ridge exactly the same size as at the start.

CAMERA: 24mm lens on a fixed locked-off mount at ground level, 6 m from the crevasse edge, low angle medium long shot, deep focus, absolutely zero camera movement. — the same position, height and lens as Scene 1. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: each stride carries them far and holds them off the ground for most of a second; the fourth stride is shorter than the first and the dust each boot lifts settles slowly but certainly.
AUDIO: a low muffled rumble, two breathing rhythms out of step, dull boot impacts through thin air. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 4 — MAKARA

```
SÜRE: 10 s · ZAMAN: 0:40,0 · VURUŞ: Kurulum — ortak hat ilk kez adlandırılır
KURULUM: C · ilk kullanım · 35mm · MS · eye level · IN FRAME: back · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: back
Scene 5 of 48.
The yellow line is wound onto a reel between the two seats until no slack is left hanging outside the cage.

Inside an open-cage rover whose nose points away from camera, from the side of the two seats: two backs fill the frame. On the left, The back of his suit is one continuous ribbed surface from collar to hip, and one angular dark box is mounted flat on it, its upper edge under the cobalt-blue shoulder caps. On the right, The back of his suit is one continuous ribbed surface from collar to hip, and one narrow dark rectangle stands on it, tall and thin, clear of the black upper arms. Between the seats a hand-sized reel holds a thin yellow line; a loop of it still hangs outside the cage bars. The cage is open tube frame with a low dash and one small orange indicator.
LIGHT: the same outside sun from the upper left falling through the open cage, one small orange indicator on the wrist block.
CAMERA: 35mm lens on a fixed mount inside the rover cage at seat height, 1.5 m from the right seat, eye level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No third line, no extra cable and no rope that was not named. No back-mounted tank, hose or cable — each back unit is one closed integral box.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: back
Scene 5 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The reel turns and takes in the yellow line until the last loop lifts off the cage bar, and both backs stay square to camera.

TIMELINE: 0.0s — the yellow loop hangs outside the cage bar and the reel between the seats is still. 3.0s — the off-white glove turns the reel and the line comes in a hand-length at a time; the loop shortens and lifts clear of the bar. 7.0s — the last of the slack is on the reel, the line runs straight from reel to two belts, and the rover begins to move so both backs press back into the seats.

CAMERA: 35mm lens on a fixed mount inside the rover cage at seat height, 1.5 m from the right seat, eye level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Both backs stay one continuous ribbed surface from collar to hip with their units mounted flat on them. His forearm tightens at every half turn of the reel. Gravity is 0.30 g: the hanging loop swings with a long slow period as it is taken in, and the two bodies settle back into the seats without bouncing.
AUDIO: a dull structural vibration carried through the frame into both suits, two breathing rhythms, a ratchet turning. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No third line, no extra cable and no rope that was not named. No back-mounted tank, hose or cable — each back unit is one closed integral box.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 5 — ARKADAKİ ZEMİN

```
SÜRE: 10 s · ZAMAN: 0:50,0 · VURUŞ: Katalizöre giriş
KURULUM: E · ilk kullanım · 24mm · WS · high angle · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 6 of 48.
Three separate plates drop out of the road back from the rover, one after another, and none of them comes back up.

High and wide over a straight rock road: a four-wheeled open-cage rover the length of two men runs away from camera along it, two small suited figures in the cage, the off-white one at the wheel on the left and the burnt-orange one on the right. A thin yellow line runs between their belts. Behind the rover the road surface is flat plates with dark seams between them. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: one hard sun out of frame to the upper left, shadow edges soft, thin dust holding a faint glow at every edge.
CAMERA: 24mm lens on a fixed locked-off mount above the road, 25 m from the rover, high angle wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No wind, no rain, no liquid, no flame and no explosion anywhere in the frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 6 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The rover pulls away along the road while three plates behind it drop one after another and three dust columns stand up where they were.

TIMELINE: 0.0s — the rover is running away from camera, the road behind it whole. 3.0s — one plate back from the rover tilts and drops out of the road; a single dust column stands up in its place and begins to fall back. 6.5s — a second and then a third plate go the same way, each one nearer the rover than the last, three dust columns now standing at different heights; the rover keeps its speed and does not turn.

CAMERA: 24mm lens on a fixed locked-off mount above the road, 25 m from the rover, high angle wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: each plate takes about a second to fall out of sight, the dust rises in columns and never hangs, and the rover settles slowly between bumps.
AUDIO: a low muffled rumble with road noise carried through it, three separate deep collapses behind, two breathing rhythms. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No wind, no rain, no liquid, no flame and no explosion anywhere in the frame.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 6 — DEVRİLEN KULE

```
SÜRE: 10 s · ZAMAN: 1:00,0 · VURUŞ: Katalizör
KURULUM: E · küme S5 · 24mm · WS · high angle · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 7 of 48.
A lattice tower falls across the road ahead of the rover and the rover leaves the road to the right before it lands.

High and wide over the same straight rock road: the four-wheeled open-cage rover runs away from camera with two small suited figures in it, off-white at the wheel on the left, burnt orange on the right. Ahead of the rover a slim lattice service tower three times the height of a man stands at the roadside, leaning. To the right of the road the ground steps down into a wide quarry cut. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: one hard sun out of frame to the upper left, shadow edges soft, thin dust holding a faint glow at every edge.
CAMERA: 24mm lens on a fixed locked-off mount above the road, 25 m from the rover, high angle wide shot, deep focus, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 6. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 7 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The tower comes down across the road and the rover is already turning off to the right when it lands.

TIMELINE: 0.0s — the tower leans further and the rover holds the centre of the road. 3.5s — the tower comes down across the road ahead, turning as it falls and keeping the same rotation all the way; the rover swings right and leaves the road. 7.0s — the tower lands and a long low dust column stands up along it, while the rover is already down the step and running into the quarry cut on the right.

CAMERA: 24mm lens on a fixed locked-off mount above the road, 25 m from the rover, high angle wide shot, deep focus, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 6. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the tower takes about three seconds to come down and holds its rotation axis the whole way, and the dust it raises falls slowly but certainly.
AUDIO: a low muffled rumble, a long structural groan and then one deep impact, two breathing rhythms sharpening. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 7 — KIRMIZI KALAN İŞARET

```
SÜRE: 10 s · ZAMAN: 1:10,0 · VURUŞ: Katalizör — sorunun ADI konur
KURULUM: C · dönüş S4 · 35mm · MS · eye level · IN FRAME: hands, torso · REPLİK: R1 · 74 s · TURUNCU (post-dub)
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: hands, torso
Scene 8 of 48.
The small control block on the left wrist opens and one red point comes up on it and stays red for the rest of the shot.

Inside the open-cage rover, from the side of the two seats: a burnt-orange torso fills the right of frame, black upper arms, a dark grey collar ring under a helmet whose flat front pane is fully opaque matte black. His left wrist carries a small flat control block the size of two fingers, its cover shut. The off-white shoulder and cobalt-blue cap of the second man cross the left edge. The cage is open tube frame, the dash low and plain, the road jolting past beyond the bars.
LIGHT: the same outside sun from the upper left falling through the open cage, one small orange indicator on the wrist block.
CAMERA: 35mm lens on a fixed mount inside the rover cage at seat height, 1.5 m from the right seat, eye level medium shot, deep focus, absolutely zero camera movement. — the same position, height and lens as Scene 5. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No fabric, no cloth, no flapping or billowing material — both suits are hard shells. No third line, no extra cable and no rope that was not named.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: hands, torso
Scene 8 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The cover on the wrist block is flicked open and a single red point comes up and holds red while the glove works it twice more.

TIMELINE: 0.0s — the orange glove reaches across and lifts the cover of the wrist block. 3.0s — one red point the size of a fingertip comes up on the block and stays; the glove presses it once and it does not change. 7.0s — the glove presses it twice more in a slower rhythm, the red point still steady, and the orange helmet turns a little towards the left edge of frame while the cage keeps jolting.

CAMERA: 35mm lens on a fixed mount inside the rover cage at seat height, 1.5 m from the right seat, eye level medium shot, deep focus, absolutely zero camera movement. — the same position, height and lens as Scene 5. In a single continuous shot.
PHYSICS: His forearm tightens against the stiffness of the cover. Gravity is 0.30 g: the rover jolts settle slowly, and both bodies move against the seats with a long soft rebound.
AUDIO: a dull structural vibration through the frame, two breathing rhythms, one short radio line from the other suit carried flat and thin. No dialogue in the clip. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No fabric, no cloth, no flapping or billowing material — both suits are hard shells. No third line, no extra cable and no rope that was not named.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 8 — DAR YOL

```
SÜRE: 10 s · ZAMAN: 1:20,0 · VURUŞ: Tartışma bandı
KURULUM: F · ilk kullanım · 35mm · MLS · eye level · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 9 of 48.
The rover comes down a road one and a half rover-widths wide with a rock wall on one side and open drop on the other.

Low and level, looking back along a quarry road: the road runs between a sheer rust-brown rock wall on the left and an open drop on the right, its whole width about one and a half times the length of the rover. A four-wheeled open-cage rover comes towards camera down it, two suited figures in the cage, the off-white one at the wheel on the left and the burnt-orange one on the right, a thin yellow line between their belts. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: the same hard sun from the upper left, cut by the quarry wall into one bright slice along the right side of the road.
CAMERA: 35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 9 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The rover comes on down the narrow road and neither wheel leaves the width between the wall and the drop.

TIMELINE: 0.0s — the rover is far down the road and coming on, the wall hard on the screen-left side and the drop open on the screen-right side. 4.0s — it closes towards camera and the gap between its right wheels and the drop stays the width of a glove; small stones come off the wall and cross the road behind it. 8.0s — it is close enough to fill the middle of frame, still centred, dust standing in a low column where the stones came down.

CAMERA: 35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the falling stones take about a second to cross the road and the dust they raise rises in a column and settles slowly but certainly.
AUDIO: a low muffled rumble closed in by the wall, road noise doubled back off the rock, two breathing rhythms. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 9 — BÜKÜLEN TEKERLEK

```
SÜRE: 10 s · ZAMAN: 1:30,0 · VURUŞ: Tartışma — ZAAF başlar (araç hasarı kalıcı)
KURULUM: G · ilk kullanım · 50mm · CU · low angle · IN FRAME: none · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: none
Scene 10 of 48.
A falling rock strikes the left rear wheel and the wheel stays bent out of line for the rest of the shot.

Close and low on the left rear wheel of a moving four-wheeled rover: a heavy open wheel with a deep tread and a dark hub, the tube frame of the cage above it, the quarry road surface running past beneath. To the left the rust-brown rock wall goes up out of frame; to the right the road edge and the open drop. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge.
LIGHT: the hard sun cut by the quarry wall into one bright slice along the top of the wheel, the hub in deep shadow.
CAMERA: 50mm lens on a fixed mount on the rover frame at wheel height, 2.5 m from the left rear wheel, low angle close-up, deep focus, absolutely zero camera movement. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No miniature read, no tilt-shift, no shallow depth of field on any structure. No wind, no rain, no liquid, no flame and no explosion anywhere in the frame. Every damaged surface stays dry metal — dented shell, bent rim, torn seam and nothing else.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: none
Scene 10 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
A rock comes down onto the wheel, the rim bends out of line, and the bent wheel keeps turning out of line for the rest of the clip.

TIMELINE: 0.0s — the wheel is turning true, the road running past beneath it. 2.5s — a rock the size of a helmet comes down out of the top of frame onto the wheel; the rim bends out of line and the wheel jumps sideways a glove-width. 6.0s — the rover slides and then straightens, and the bent wheel goes on turning with a visible wobble at every revolution, the same wobble at the same rate to the end of the clip.

CAMERA: 50mm lens on a fixed mount on the rover frame at wheel height, 2.5 m from the left rear wheel, low angle close-up, deep focus, absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the rock falls about one glove-width in its first second and one arm-length in its second, and it keeps its rotation axis as it comes down.
AUDIO: a low muffled rumble, one hard dull impact through the frame, then a repeating knock at the wheel. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No miniature read, no tilt-shift, no shallow depth of field on any structure. No wind, no rain, no liquid, no flame and no explosion anywhere in the frame. Every damaged surface stays dry metal — dented shell, bent rim, torn seam and nothing else.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 10 — KAPANAN DÖNÜŞ

```
SÜRE: 10 s · ZAMAN: 1:40,0 · VURUŞ: Tartışma — geri dönüş biter
KURULUM: F · dönüş S8 · 35mm · MLS · eye level · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 11 of 48.
A rock column comes down across the road back from the rover and closes the whole width between the wall and the drop.

Low and level, looking back along the quarry road: the rock wall on the left, the open drop on the right, the road one and a half rover-lengths wide between them. The four-wheeled open-cage rover has passed camera and runs away down the road, two suited figures in the cage, the off-white one at the wheel on the left and the burnt-orange one on the right. Standing out of the wall in their wake is a rock column three times the height of a man. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: the same hard sun from the upper left, cut by the quarry wall into one bright slice along the right side of the road.
CAMERA: 35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement. — the same position, height and lens as Scene 9. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 11 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The rock column comes down across the road back from the rover and fills the road from wall to drop.

TIMELINE: 0.0s — the rover is running away down the road and the column stands whole out of the wall. 3.0s — the column separates at its base, turns once as it comes down and keeps the same rotation, and lands across the road from the wall to the drop edge. 7.0s — dust stands up along it in three columns and begins to fall, the road back from the rover is closed wall to drop, and the rover does not slow.

CAMERA: 35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement. — the same position, height and lens as Scene 9. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the column takes about three seconds to come down and holds its rotation axis, and the dust rises in columns and settles slowly but certainly.
AUDIO: a low muffled rumble, one long tearing crack and a deep landing carried back off the wall, two breathing rhythms. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 11 — AÇILAN YOL

```
SÜRE: 10 s · ZAMAN: 1:50,0 · VURUŞ: Tartışma sonu ◆ BÖLÜM 1 BİTER
KURULUM: F · küme S10 · 35mm · MLS · eye level · IN FRAME: full body · REPLİK: —
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: full body
Scene 12 of 48.
The road widens ahead of the rover and the rover turns off it onto a tilted metal landing set into the wall.

Looking back along the quarry road: rock wall left, open drop right. Further down, the wall steps back and the road opens to twice its width; a tilted metal landing is set into the wall with a plain handrail and a closed service door behind it. The four-wheeled open-cage rover runs away from camera towards the opening, two suited figures in the cage, off-white at the wheel on the left, burnt orange on the right, its left rear wheel wobbling once every turn. The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust drifted along every edge. The horizon is close and slightly curved under a deep brown-violet sky with no clouds. One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing, never growing.
LIGHT: the same hard sun from the upper left, cut by the quarry wall into one bright slice along the right side of the road.
CAMERA: 35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 11. In a single continuous shot.
NEGATIVE: Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: full body
Scene 12 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suits, helmets, light and scene carried from the frame, nothing re-described.
The rover carries the wobble in its left rear wheel all the way to the opening and turns off the road onto the tilted landing.

TIMELINE: 0.0s — the rover runs away down the road, the left rear wheel wobbling once every turn. 4.0s — the road opens out and the tilted metal landing comes clear of the wall; the rover swings towards it and the wobble goes on at the same rate. 8.0s — the front wheels are up on the landing and the frame tips with the tilt, the handrail passing close on the left, the closed service door still shut beyond it.

CAMERA: 35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement. continues the previous clip from its exact last frame — the same position, height and lens as Scene 11. In a single continuous shot.
PHYSICS: Gravity is 0.30 g: the tilting rover settles onto the landing slowly and without bouncing, and the dust its wheels lift stands in low columns and falls back.
AUDIO: a low muffled rumble, road noise giving way to metal under the wheels, two breathing rhythms. No dialogue. No music.
NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters, no duplicates, no third person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No face, no eyes and no mouth behind either pane, and both panes stay fully opaque. No miniature read, no tilt-shift, no shallow depth of field on any structure. No other vehicle, no other ship and no structure that was not named.

Output: 16:9, no text, no watermark.
```

---

