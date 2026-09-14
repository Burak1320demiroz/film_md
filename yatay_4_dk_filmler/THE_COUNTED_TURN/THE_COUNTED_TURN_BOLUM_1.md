# 🎬 THE_COUNTED_TURN — BÖLÜM 1  (S0 – S12)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_COUNTED_TURN_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③).
>
> Bölüm sınırı ardışık bir çifttir: bu dosyanın SON sahnesi (S12) ile bölüm 2'nin
> İLK sahnesi (S13) ≥1 ölçek kademesi VE ≥45° ayrılır — MCU→EWS 4 kademe · 90°.
> Köprü tipi EYLEM SÜREKLİLİĞİ: S12'de başlayan baş kaldırma S13'te tamamlanır.
> Denetim: `python3 .../prompt_kontrol.py yatay_4_dk_filmler/THE_COUNTED_TURN`
>
> ⚠️ **BİLİNÇLİ SAPMA [D74] — video prompt uzunluğu.** Band 2.000-2.600, tavan
> ~4.300. Bu filmin video promptları ~2.700-3.100 bandında. Sebep aritmetiktir
> ve `KILAVUZ_REHBERI` §5'te yazılıdır: negatif çekirdek tek başına 1.641
> karakter, sahneye ait TEK KELİME yazılmadan. Kısaltma seçeneği çekirdeği
> kesmekti; kesilmedi. D79 kask/vizör bloğu video promptlarında YALNIZ kask ya
> da sırt kadrajın konusu olduğu sahnelerde taşınır (IMAGE promptlarında 25/25).
>
> ⛔ İNSANSIZ SAHNE (S6): `NEGATIVE:` bloğu YAZILMAZ, tek pozitif `Style:`
> satırına indirilir — insansız sahne + uzun yokluk listesi YAPISAL RED
> profilidir (red defteri vaka 2; bu çözüm ilk denemede GEÇTİ).

---

## 🎬 SAHNE 0 — BIRAKILAN ŞEY

```
SÜRE: 9 s   ·   VURUŞ: açılış imajı · HOOK   ·   KURULUM: A (85 mm · 0,70 m · ECU · tepeden-aşağı 35°)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 1 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 85 mm spherical lens, zero point seven metres from the deck seam, height one point one metres, a high-angle view tilted thirty-five degrees toward the deck. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
A gloved hand is open just above the welded deck seam and a single bolt has just left the palm. The bolt is already off the vertical: it travels sideways as it falls, on a line that plainly does not match the taut band end hanging beside it. Two bolts of the same kind already lie in the seam. The nearest stainless pin stands empty.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Only her forearms and gloves are in frame, opened flat and held still after the release.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
Weight here comes only from the ring's turning and depends on direction; nothing anywhere is weightless. A released object never falls vertically and never rises — it drifts to one side and reaches the seam about a hand-span and a half out from vertical, in a little under two seconds. The hanging band end is in balance and hangs vertically; the falling bolt does not, and the two are visibly not parallel.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 9 seconds. Scene 1 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 85 mm spherical lens, zero point seven metres from the deck seam, height one point one metres, a high-angle view tilted thirty-five degrees toward the deck. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (9 s):
0s — the glove is closed around the bolt, held over the seam.
3s — the fingers open; the bolt leaves the palm and immediately starts moving sideways as it drops.
6s — the bolt reaches the seam about a hand-span and a half out from vertical and settles beside the two already there; it does not roll.
9s — the glove is still open in the same place; nothing else moves. No cuts.

AUDIO:
Hard vacuum — no airborne sound. Only what travels through the structure: the bolt touching the seam is one dry tap that runs around the ring and returns as a long many-times-reflected tail. Breathing and a suit fan under it. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 1 — SAYIM BAŞLAR

```
SÜRE: 10 s   ·   VURUŞ: KATALİZÖR   ·   KURULUM: C (50 mm · 4,00 m · MS · göz hizası)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 2 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 50 mm spherical lens, four metres to the side of the worker at eye level, height one point four five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
The worker stands on the deck mid-run, a heavy woven band gathered in both gloves, the row of stainless pins running away from her along the seam. Past the rail the star field shows through the unplated rib gap.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Mid-stride, weight coming onto the leading boot, shoulders square to the line of pins.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
One single strike passes through the structure and the ring steps up its rate. Walking the same way the ring turns makes her heavier: this step lands earlier and harder than a step should, the knee folds under it, and the boot meets the deck flat.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. The star field is made of individual separate points — no star trails, no streaks, no smearing.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 2 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 50 mm spherical lens, four metres to the side of the worker at eye level, height one point four five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — she stands still, band in both gloves, looking along the row of pins.
2s — one dry strike passes through the deck; her boots register it and her head comes up a fraction.
5s — behind her the star field is visibly moving faster past the rail than it was, and the star field sweeps half way around the frame during the shot.
10s — she takes one step; it lands early and hard, the knee folds, and she holds there. No cuts.

AUDIO:
Hard vacuum. One dry structural strike at two seconds, running around the ring and returning as a long reflected tail. Breathing and a suit fan under it. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. The star field is made of individual separate points — no star trails, no streaks, no smearing.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 2 — SARKMA · ilk ölçü

```
SÜRE: 10 s   ·   VURUŞ: SAYAÇ kurulur   ·   KURULUM: G (50 mm · 2,50 m · MCU · alçak 0,40 m)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 3 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera low beside the seam, 50 mm spherical lens, two point five metres from the pin at height zero point four metres, a low-angle view angled very slightly upward. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
A single stainless pin stands up from the welded seam. The woven band runs from this pin to the next one three metres away and hangs between them in a shallow curve; at its lowest point it hangs about a finger's width below the top of the pin. The worker's helmet and shoulder are at the frame edge, looking at it, her gloves nowhere near it.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Crouched at the frame edge, hands resting on her own knees, well clear of the band.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
The band is under tension and dead straight where it leaves each pin; it sags only between them. How deep it sags is set by the local weight, and the local weight is set by how fast the ring is turning. Nothing here is floating and nothing is being pulled.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 3 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera low beside the seam, 50 mm spherical lens, two point five metres from the pin at height zero point four metres, a low-angle view angled very slightly upward. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — the pin, the band and the shallow sag, held.
3s — the helmet at the frame edge tilts a few degrees toward the lowest point of the band.
6s — nothing changes; the sag stays exactly where it is and the hands stay on the knees.
10s — she is still looking at it, unmoved. No cuts.

AUDIO:
Hard vacuum. Breathing and a suit fan only, close and steady. No structural strike in this shot. No music change.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 3 — TEK KLİPS

```
SÜRE: 10 s   ·   VURUŞ: TOHUM · Çehov kurulumu   ·   KURULUM: A (85 mm · 0,70 m · ECU · tepeden-aşağı 35°)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 4 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 85 mm spherical lens, zero point seven metres from the deck seam, height one point one metres, a high-angle view tilted thirty-five degrees toward the deck. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 0. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
Macro on the closing pin. A gloved hand brings one anodised orange clip down onto the pin and closes it over the woven band; the clip seats easily. Behind the hand the row of clips on the right hip is still full — a line of short orange shapes standing up along the rail.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. One glove holds the band down against the pin, the other closes the clip in a single movement.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
The ring is still turning slowly and the local weight is low, so one clip is enough to hold the band on the pin and it closes without effort. The clip is either open or closed — there is no half-closed state at any point.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 4 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 85 mm spherical lens, zero point seven metres from the deck seam, height one point one metres, a high-angle view tilted thirty-five degrees toward the deck. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 0. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — the band lies over the pin, uncaptured; the clip is in the glove above it.
3s — the clip comes down onto the pin.
5s — it closes in one movement and stays closed; the band is captured.
10s — the hands withdraw a little and hold; the full row of clips on the hip stays in frame. No cuts.

AUDIO:
Hard vacuum. The clip closing arrives through the structure as one short dry click with a long reflected tail. Glove-on-band friction is carried through the body, dull and close. Breathing and a suit fan. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 4 — TERS YÖN

```
SÜRE: 10 s   ·   VURUŞ: kural keşfi ①   ·   KURULUM: C (50 mm · 4,00 m · MS · göz hizası)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 5 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 50 mm spherical lens, four metres to the side of the worker at eye level, height one point four five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 1. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
The worker walks back the other way along the deck, empty-handed, going to fetch the spool. The star field shows past the rail behind her and the row of pins she has already worked runs away past her shoulder.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Mid-stride again, but the body riding high, the leading boot hanging longer before it lands.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
Walking against the ring's turning makes her lighter: the same stride now floats, the boot comes down late and softly, and the knee does not fold. Same deck, same person, same stride as before — only the direction has changed.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. The star field is made of individual separate points — no star trails, no streaks, no smearing.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 5 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 50 mm spherical lens, four metres to the side of the worker at eye level, height one point four five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 1. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — she turns and starts back the other way.
3s — the first step hangs and lands late; the knee stays straight.
6s — the second step does the same and the body stays high through it.
10s — a third step, identical, and she keeps going. No cuts.

AUDIO:
Hard vacuum. Boots meeting the deck arrive through the structure as soft dull contacts with long reflected tails, spaced further apart than a normal walk. Breathing and a suit fan. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. The star field is made of individual separate points — no star trails, no streaks, no smearing.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 5 — SARKMA · ikinci ölçü

```
SÜRE: 10 s   ·   VURUŞ: SAYAÇ · kadraj çifti   ·   KURULUM: G (50 mm · 2,50 m · MCU · alçak 0,40 m)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 6 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera low beside the seam, 50 mm spherical lens, two point five metres from the pin at height zero point four metres, a low-angle view angled very slightly upward. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 2. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
The same fixed framing as Scene 2: the same stainless pin, the same span of woven band between it and the next pin. The only thing different is the sag — the band now hangs noticeably lower below the top of the pin than it did. The worker's helmet and shoulder are again at the frame edge, gloves nowhere near the band.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Crouched at the frame edge exactly as before, hands on her own knees.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
The ring has turned faster since this span was last looked at, so the local weight has risen and the band sags deeper. The band is still under tension and dead straight where it leaves each pin. Nothing is being pulled and nothing is floating.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 6 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera low beside the seam, 50 mm spherical lens, two point five metres from the pin at height zero point four metres, a low-angle view angled very slightly upward. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 2. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — the pin and the deeper sag, held.
3s — the helmet at the frame edge holds still; only the eyes move down the curve.
6s — nothing changes; the sag stays exactly where it is.
10s — she remains crouched, hands on her knees. No cuts.

AUDIO:
Hard vacuum. Breathing and a suit fan only, a little heavier than before. No structural strike. No music change.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 6 — KABURGA GÖZÜ

```
SÜRE: 10 s   ·   VURUŞ: viral ara #1 · ölçek   ·   KURULUM: F (50 mm · 6,00 m · MWS · göz hizası)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 7 of 25. NO human anywhere in frame.

CAMERA:
Locked-off camera, 50 mm spherical lens, six metres from the unplated rib gap at eye level, height one point five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
No human anywhere in frame. The unplated rib gap in the ring's inner skin, two and a half metres wide, with bare structural ribs on either side and the star field beyond it. The ribs are perfectly still; the star field moves steadily past them, always the same way. Beyond the rib gap there is only the star field — nothing else is built out there.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
The gap is the only opening in the inner skin. The ribs do not move at all; only the sky beyond them does, because the ring is turning under it. During the shot the star field sweeps half way around the frame. The star field is made of individual separate points — no trails, no streaks.

Style: photorealistic hard science fiction, one locked-off take, 35mm film grain, hard axial light with black shadows and clean metal surfaces, and the deck around it is empty and unlit.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 7 of 25. NO human anywhere in frame.

CAMERA:
Locked-off camera, 50 mm spherical lens, six metres from the unplated rib gap at eye level, height one point five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — the rib gap and the star field, held.
3s — the star field has moved a clear distance past the near rib.
6s — it keeps moving at exactly the same rate; the ribs have not moved at all.
10s — the same, unbroken; half the frame's width of sky has passed. No cuts.

AUDIO:
Hard vacuum — no airborne sound at all. Only a faint constant suit fan and no breathing in this shot. No music change.

Style: photorealistic hard science fiction, one locked-off take, 35mm film grain, hard axial light with black shadows and clean metal surfaces, and the deck around it is empty and unlit.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 7 — MAKARA SÖKÜLÜR

```
SÜRE: 10 s   ·   VURUŞ: eşik · geri dönüş zorlaşır   ·   KURULUM: B (32 mm · 14,00 m · WS · göz hizası)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 8 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 32 mm spherical lens, fourteen metres along the deck at eye level, height one point five five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
Wide along the deck. The worker stands beside a heavy cable spool seated in a cradle bolted to the deck, the row of pins running away past her. The deck curves up and out of frame on both sides and the same deck closes over the top of the frame with nothing standing on it. The deck horizon stays level and unbroken; the largest thing behind her is the far curve of the ring itself.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Braced with both gloves on the spool, feet apart, shoulders low.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
Lifting here is easy but stopping is not: the ring's turning has taken weight off the spool but none of its mass. It comes out of the cradle slowly, and when it reaches the deck it has to be stopped by the body, not by its own weight.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 8 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 32 mm spherical lens, fourteen metres along the deck at eye level, height one point five five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — both gloves are on the spool, still seated in its cradle.
3s — the spool comes free and starts down, slowly.
6s — it reaches the deck; her shoulder line drops as she stops it and stays down.
10s — the spool sits on the deck, the cradle is empty, and she is still braced over it. No cuts.

AUDIO:
Hard vacuum. The spool leaving the cradle and meeting the deck arrive through the structure as two low contacts with long reflected tails. Breathing, heavier now, and a suit fan. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 8 — İLK YÜK

```
SÜRE: 10 s   ·   VURUŞ: efor ①   ·   KURULUM: E (85 mm · 1,20 m · CU · tepeden-aşağı 50°)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 9 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 85 mm spherical lens, one point two metres from the gloves, height zero point nine five metres, a high-angle view tilted fifty degrees toward the gloves. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
Macro on the gloves. Both gloves close on the heavy woven band where it lies on the deck; the band comes off the deck by the width of a hand and holds there. The nearest stainless pin and the welded seam stay in frame beside the hands.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Both gloves gripping the band, wrists straight, the raised knuckle ridges of the gloves pressed deep, the stitched cuff seams pulled tight.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
The band is heavy and stays heavy: the ring's turning has reduced what it weighs but not what it takes to start or stop it. It comes up slowly and holds exactly where it is stopped.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 9 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 85 mm spherical lens, one point two metres from the gloves, height zero point nine five metres, a high-angle view tilted fifty degrees toward the gloves. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — the band lies flat on the deck; both gloves settle onto it.
3s — the gloves close; the knuckle ridges deepen and the cuff seams pull tight.
6s — the band comes off the deck by the width of a hand.
10s — it holds there, dead still, and the shoulder line has dropped. No cuts.

AUDIO:
Hard vacuum. Glove-on-band friction carried through the body, dry and close. Breathing, working and audible. A suit fan under it. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 9 — AYNI YÜK, DEVAM

```
SÜRE: 10 s   ·   VURUŞ: efor ② birikme   ·   KURULUM: E (85 mm · 1,20 m · CU · tepeden-aşağı 50°)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 10 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 85 mm spherical lens, one point two metres from the gloves, height zero point nine five metres, a high-angle view tilted fifty degrees toward the gloves. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. This shot continues the previous clip from its exact last frame — the same position, height and lens as Scene 8. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
This shot continues from the exact last frame of the previous one: the same gloves, the same band held a hand's width off the deck, the same pin and seam beside them. The band now moves toward the pin, which stands at the near edge of frame.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Both gloves still gripping the band, wrists straight, knuckle ridges deep, cuff seams tight; the shoulder line already low.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
Moving the band sideways costs as much as lifting it did, because the mass has not changed. Once the shoulder line drops it does not come back up.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 10 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 85 mm spherical lens, one point two metres from the gloves, height zero point nine five metres, a high-angle view tilted fifty degrees toward the gloves. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. This shot continues the previous clip from its exact last frame — the same position, height and lens as Scene 8. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — exactly the last frame of the previous shot: band held, gloves closed.
3s — the band travels toward the pin; the gloves do not re-grip.
6s — it arrives level with the pin and stops there.
10s — the shoulder line has dropped another degree and stays down. No cuts.

AUDIO:
Hard vacuum. The same dry glove-on-band friction, continuing without a break from the previous clip. Breathing heavier. A suit fan. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No dust, no smoke, no exhaust, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 10 — OTURMAYAN KLİPS

```
SÜRE: 10 s   ·   VURUŞ: BAŞARISIZ DENEME   ·   KURULUM: B (32 mm · 14,00 m · WS · göz hizası)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 11 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera, 32 mm spherical lens, fourteen metres along the deck at eye level, height one point five five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 7. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
Wide along the deck. The worker walks against the ring's turning with the band in one glove and a clip in the other, coming up on a pin. The deck curves up and out of frame on both sides and closes over the top with nothing standing on it; the far curve of the ring is the largest thing behind her.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Riding high on the stride, arm extended, trying to press the band down onto the pin as she passes it.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
Walking against the turning has taken weight off her and she cannot put enough down through the band: instead of dropping into the pin the band lifts off it. The clip never reaches a closed position.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 11 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera, 32 mm spherical lens, fourteen metres along the deck at eye level, height one point five five metres. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The same position, height and lens as Scene 7. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — she comes up on the pin, riding high on the stride.
3s — she presses the band toward the pin; the band lifts off it instead.
6s — the glove pauses in the air and comes back a little.
10s — she has stopped walking and stands there, band still in hand. No cuts.

AUDIO:
Hard vacuum. Soft, widely spaced boot contacts through the structure. One short band-on-metal scrape, then nothing. Breathing and a suit fan. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 11 — ÜSTÜMDEKİ GÜVERTE

```
SÜRE: 10 s   ·   VURUŞ: viral ara #2 · ⭐VİRAL   ·   KURULUM: D (50 mm · 3,00 m · EWS · alttan-yukarı 60°)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 12 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera low on the deck, 50 mm spherical lens, three metres from the worker at height zero point three five metres, a low-angle view tilted sixty degrees toward the deck closing overhead twenty-four metres away. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
Low on the deck, tilted up. The worker is at the bottom edge of frame, head back. Above her the deck curves up on both sides and closes overhead twenty-four metres away, and the line of dark woven band she has already laid runs along it from one side to the other. Nothing is standing on that deck. The star field moves past behind the closing curve.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Head back, face fully readable through the clear window, the brows lifting and staying lifted.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
There is no occlusion inside the ring: the ceiling is the same deck seen from underneath, and her own line of band is up there because she put it there. During the shot the star field sweeps about two thirds of the way around the frame.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. The star field is made of individual separate points — no star trails, no streaks, no smearing. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 12 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera low on the deck, 50 mm spherical lens, three metres from the worker at height zero point three five metres, a low-angle view tilted sixty degrees toward the deck closing overhead twenty-four metres away. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — her head is down, working.
2s — the head comes back and the eyes go up the curve.
4s — the brows lift and stay lifted; they do not come back down.
10s — she holds the look; overhead her own line of band runs the length of the curve. No cuts.

AUDIO:
Hard vacuum. Breathing, slower now, and a suit fan. No structural strike in this shot. No music change.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. The star field is made of individual separate points — no star trails, no streaks, no smearing. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 12 — YARIYI GEÇMEK

```
SÜRE: 10 s   ·   VURUŞ: dönüşü olmayan nokta   ·   KURULUM: H (35 mm · 1,50 m · MCU · omuz üstü)
```

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Hard science fiction, the inner deck of a ring station under construction. Scene 13 of 25. EXACTLY ONE human character in frame.

CAMERA:
Locked-off camera just behind the worker's shoulder, 35 mm spherical lens, one point five metres away at height one point six metres, eye level, an over-the-shoulder framing. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

SCENE:
Just behind her shoulder. Her back fills the near left of frame — one continuous smooth panel from collar to hip, unbroken, carrying nothing on it. Past her shoulder the welded seam and its pins run away along the deck and lift out of frame with the curve, the dark line of laid band running with them.

ENVIRONMENT:
The deck is bare machined aluminium, bright and clean, still being built — no grime, no rust, no staining. A long welded seam runs along it and stainless pins stand up from the seam every three metres. Beyond the rail the deck curves upward on both sides and closes overhead.

SUBJECT:
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on the deck. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with zero tint and zero mirror coating, and the face is fully readable through it at every head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from the rail in a single line. Standing, looking along the line of her own work; the head begins to come up at the very end of the shot.

LIGHTING:
One hard source comes in along the ring's axis and grazes the deck. No fill light and no bounce; every shadow is completely black with a razor edge. Highlights roll off smoothly and keep texture instead of clipping to white. This direction never changes anywhere in the film.

PHYSICS:
She has passed the halfway point of the ring, so going back is now longer than going on. This is geometry, not a feeling: the line behind her and the line ahead of her are the same deck.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot, 0 cuts, 10 seconds. Scene 13 of 25. EXACTLY ONE human character.

CAMERA:
Locked-off camera just behind the worker's shoulder, 35 mm spherical lens, one point five metres away at height one point six metres, eye level, an over-the-shoulder framing. Circular bokeh, no lens flare, Super 35 field of view. No pan, no tilt, no dolly, no zoom. The ring turns one way only: the star field slides out past the far end of the rail and the welded seam leans the same way. Nothing ever crosses back.

MOTION (10 s):
0s — her back and shoulder fill the near frame; the seam runs away past her.
3s — nothing moves except the star field far past the curve.
6s — her weight shifts once from one boot to the other.
10s — her head starts to come up, and the shot ends on that movement. No cuts.

AUDIO:
Hard vacuum. One boot shift carried through the structure with a long reflected tail. Breathing and a suit fan. No music.

NEGATIVE:
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit: the back is one continuous smooth panel from collar to hip, unbroken, carrying nothing. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; the face is fully readable through it in every frame, at every head angle. No dust, no smoke, no exhaust, no sparks and no flame anywhere. On the deck curving overhead no one is standing and nothing is moving.

Output: 16:9, no text, no watermark.
```

---
