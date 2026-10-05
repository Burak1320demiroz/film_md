# 🎬 THE_LAST_GATE — BÖLÜM 6  (K61 – K72 · S16 – S18)

> Bölüm 1 ile aynı kurallar: **yalnız sahne blokları**, her prompt
> self-contained, sahne başlığı `##` ile.
>
> ⛔ **Bölüm 2 "devamı" değildir, ikinci yarıdır.** "Bölüm 1'deki gibi" atfı
> yasak; model bu dosyayı tek başına okuyor. ⭐ 14.09.2026: karakter bloğunun
> yalnız `IN FRAME:` satırındaki kısmı yazılır (tamamı değil — D214 · ㉖); iskelet
> bölüm 1 ile aynı: IN FRAME · tek kilit üçüncü satırda · §5.1 çekirdek + ≤3 ·
> videoda `START FRAME:` tek satır (`IMAGE_VIDEO_PROMPT_TEMPLATES.md` V3).
>
> ⛔ İLK SAHNE, bölüm 1'in SON sahnesiyle ardışık çifttir: ≥1 ölçek kademesi
> VE ≥45° açı farkı. Bu tek çift, film ikiye bölündüğünde denetimin
> kör kaldığı yerdir — klasör modu tam bunun için yazıldı.
>
> ⛔ **Sahne numarası RAKAMLA yazılır.** `## 🎬 SAHNE ⬜` başlığı sayaçtan da,
> klasör modundan da düşer: ikisi de `SAHNE <rakam>` arar (kural ②).

> ⭐ **22.09.2026 · ÇOK KLİPLİ SAHNE:** birim başlığı `## 🎬 KLİP n` · sahne başlığı tek `#` ile
> `# 📍 SAHNE n — AD  (k klip · aralık)` · son kare zinciri YOK — her klip kendi IMAGE promptundan ·
> sahnenin 2.+ klibi `CONTINUOUS ACTION:` taşır · kapı ㉜ (`COK_KLIPLI_SAHNE_KILAVUZU.md`).

```
NOVUM TAŞIYICISI: etkin açıklığın parlak kenarı × geminin sabit dairesel kesiti → gemi artık geçemez
TEK KARE: K69 — geminin dairesel kesiti, etkin açıklığın parlak kenarı ile tek karede çakışır
KURULUM İSKELETİ: I J C Q F G F E Q C E C
ölçülen DÖNÜŞ: 3/12 — aynı harf = birebir aynı CAMERA satırı
⛔ K01–K04 harf taşımaz: kurgu bloklarıdır, kendi görüntüsü üretilmez.
```
---

# 📍 SAHNE 16 — YAKLAŞMA YETMİYOR  (4 klip · 10:00–10:40)

## 🎬 KLİP 61 — S16 · 1/4 · KURULUM — DARALAN HEDEF

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso
Clip 61 of 96.

Through the forward glass the ring stands larger than before and its opening is plainly much narrower; all three are at their stations and the escape axis and the hull's forward profile are unchanged. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap.
LIGHT: Cold instrument light from the consoles below, a wide copper wash from the banded planet through the forward glass, and a pale even glow from the gate field far down the axis; no surface blooms.
CAMERA: 50mm lens on a locked-off camera 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso
Clip 61 of 96.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved three-console frame with the ring larger beyond the glass.
CAMERA: 50mm lens on a locked-off camera 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot, deep focus.
TIMELINE:
0.0-3.0 s — the ring holds beyond the glass and the opening edge keeps drawing in.
3.0-7.0 s — the pilot reads the clearance and her hand stops on the console.
7.0-10.0 s — nobody speaks again; the three hold and the edge keeps moving.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A flat machine voice over the console bed. The line spoken is "Clearance decreasing." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 62 — S16 · 2/4 · EYLEM — PROFİL KARŞILAŞTIRMASI

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 62 of 96.
CONTINUOUS ACTION: the clearance advisory has just come up on the bridge beside her.

A gloved hand holds two plain circles side by side on a console surface — the ship's fixed cross-section and the current opening — and the second circle is now only a little larger than the first. The engineer wears white technical forearm panels in cobalt over white gloves.
LIGHT: Cold instrument light from the consoles below, a wide copper wash from the banded planet through the forward glass, and a pale even glow from the gate field far down the axis; no surface blooms.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The two circles are plain outline geometry with no numbers, scale marks or text of any kind.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 62 of 96.
CONTINUOUS ACTION: the clearance advisory has just come up on the bridge beside her.

START FRAME: the approved macro frame on the console surface with both plain circles already drawn.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the hand squares the two circles against one another.
3.0-7.0 s — the outer circle draws in a visible amount while the inner one does not change.
7.0-10.0 s — the hand holds still and the gap between the two circles keeps closing.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A short measurement tone and one held breath. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The two circles are plain outline geometry with no numbers, scale marks or text of any kind.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 63 — S16 · 3/4 · MUCADELE — SON HIZLANMA

### 📸 IMAGE PROMPT

```
IN FRAME: back · torso · hands
Clip 63 of 96.
CONTINUOUS ACTION: the two circles are already almost the same size on the console beside her.

Over the pilot's shoulder she commits both gloves to the remaining drive and holds them there; beyond the glass one drive plume runs straight and steady on the starboard side and the port side stays dark. The pilot wears a satin off-white ceramic suit with champagne-gold frame lines at the joints, a single neck ring and heavy white gloves. The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. A single diagonal scuff runs across the outer plate of the pilot's left forearm. On the left upper arm is a textless circular survey patch.
LIGHT: Cold instrument light from the consoles below, a wide copper wash from the banded planet through the forward glass, and a pale even glow from the gate field far down the axis; no surface blooms.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Only one drive plume appears — the damaged side never lights again.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: back · torso · hands
Clip 63 of 96.
CONTINUOUS ACTION: the two circles are already almost the same size on the console beside her.

The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing.

START FRAME: the approved over-shoulder frame with the starboard plume already lit and the port side dark.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — she pushes both controls forward and holds them.
3.0-7.0 s — the starboard plume lengthens a little; the port side stays completely dark.
7.0-10.0 s — she keeps the controls forward and a damage advisory comes up; nothing improves.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A short drive load, then a damage advisory. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Only one drive plume appears — the damaged side never lights again.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 64 — S16 · 4/4 · SONUC — DOKUZ YÜZ METRE

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 64 of 96.
CONTINUOUS ACTION: the single working drive is already at full command and the closing rate is already set.

Straight down the gate axis the bright edge of the opening has drawn in much further and the ship's forward profile would still pass through it, but the edge is closing faster than the ship is closing the distance; the dark gate structure runs past every edge of the frame. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cold instrument light from the consoles below, a wide copper wash from the banded planet through the forward glass, and a pale even glow from the gate field far down the axis; no surface blooms.
CAMERA: 85mm lens on a locked-off camera 2600 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The outer ring never shrinks and the opening never widens again.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 64 of 96.
CONTINUOUS ACTION: the single working drive is already at full command and the closing rate is already set.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved gate-axis frame with the opening already much narrower than before.
CAMERA: 85mm lens on a locked-off camera 2600 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the bright edge keeps moving inward all round at the same rate.
3.0-7.0 s — the frame holds; the dark structure beyond the opening does not change and the edge does not stop.
7.0-10.0 s — the opening holds its new smaller width and keeps drawing in.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A short silence with helmet breathing coming forward in the mix. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The outer ring never shrinks and the opening never widens again.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 17 — MİKROGRAVİTEDE TEHLİKE  (4 klip · 10:40–11:20)

## 🎬 KLİP 65 — S17 · 1/4 · KURULUM — PANELE GEÇİŞ

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 65 of 96.

In one frame the engineer deliberately releases her boot locks from the deck grating and takes a controlled push off the handrail toward a service panel, with the target handhold beside that panel visible in the same shot; the pilot is anchored in frame at the near rail. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. A single diagonal scuff runs across the outer plate of the pilot's left forearm. The two figures keep separate halves of the frame and never overlap. Every badge and patch is textless, a single geometric motif in embossed embroidery, with nothing written on any of them.
LIGHT: Even cool white ceiling light in the pressurised service compartment with a colder pool at the panel and one warmer light low near the deck; the white suits keep panel detail and the shadows stay shallow.
CAMERA: 50mm lens on a locked-off camera 2.4 m along the corridor axis, camera height 1.50 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. She leaves the surface by her own push only — nothing lifts her and nothing falls.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 65 of 96.

START FRAME: the approved compartment frame with the engineer still locked to the grating.
CAMERA: 50mm lens on a locked-off camera 2.4 m along the corridor axis, camera height 1.50 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — both boot locks release with two separate clicks and her soles come off the grating.
3.0-7.0 s — she pushes off the handrail and travels in a straight line across the compartment.
7.0-10.0 s — she keeps exactly that line and rate toward the target handhold.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Two lock clicks and one short direction on the local channel. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. She leaves the surface by her own push only — nothing lifts her and nothing falls.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 66 — S17 · 2/4 · TERSLIK — GÖVDE DARBESİ

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 66 of 96.
CONTINUOUS ACTION: the engineer is already travelling in a straight line across the compartment with her boots off the grating.

An external hit shakes the hull and the engineer's line across the compartment is broken: her hand passes wide of the target handhold and she goes on drifting straight with the momentum she already had, while the pilot stays anchored at the rail. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. A single diagonal scuff runs across the outer plate of the pilot's left forearm. The two figures keep separate halves of the frame and never overlap. Every badge and patch is textless, a single geometric motif in embossed embroidery, with nothing written on any of them.
LIGHT: Even cool white ceiling light in the pressurised service compartment with a colder pool at the panel and one warmer light low near the deck; the white suits keep panel detail and the shadows stay shallow.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.

NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. She never rises or falls — she keeps the motion she was given and the direction it was given in. No change of gravity occurs in this shot — the movement comes only from the vehicle's own acceleration.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 66 of 96.
CONTINUOUS ACTION: the engineer is already travelling in a straight line across the compartment with her boots off the grating.

START FRAME: the approved wide interior frame with the engineer mid-compartment and the target rail beyond her.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.
TIMELINE:
0.0-2.0 s — the hull takes the hit and everything in frame shifts the same way at once.
2.0-6.0 s — her reaching hand passes outside the handhold and closes on nothing.
6.0-10.0 s — she drifts on straight past it, turning slowly on her own axis.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A structural strike and one short breath. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. She never rises or falls — she keeps the motion she was given and the direction it was given in. No change of gravity occurs in this shot — the movement comes only from the vehicle's own acceleration.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 67 — S17 · 3/4 · KARAR — BAĞIN KARŞILIĞI

### 📸 IMAGE PROMPT

```
IN FRAME: torso · hands
Clip 67 of 96.
CONTINUOUS ACTION: the engineer is already drifting past the target rail, turning slowly on her own axis.

The pilot stays anchored at the handrail and holds her existing safety line out into the engineer's reach; the engineer takes it once and uses the controlled tension to bring herself back onto the nearby handhold, both ends of the line visible the whole time. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. A single diagonal scuff runs across the outer plate of the pilot's left forearm. The two figures keep separate halves of the frame and never overlap. Every badge and patch is textless, a single geometric motif in embossed embroidery, with nothing written on any of them.
LIGHT: Even cool white ceiling light in the pressurised service compartment with a colder pool at the panel and one warmer light low near the deck; the white suits keep panel detail and the shadows stay shallow.
CAMERA: 50mm lens on a locked-off camera 2.4 m along the corridor axis, camera height 1.50 m, eye-level medium shot, deep focus — the same position, height and lens as Clip 65.

NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The line stays continuously attached at both ends, never stretches and never leaves the frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: torso · hands
Clip 67 of 96.
CONTINUOUS ACTION: the engineer is already drifting past the target rail, turning slowly on her own axis.

START FRAME: the approved compartment frame with the safety line already extended and not yet caught.
CAMERA: 50mm lens on a locked-off camera 2.4 m along the corridor axis, camera height 1.50 m, eye-level medium shot, deep focus — the same position, height and lens as Clip 65.
TIMELINE:
0.0-3.0 s — the line is held out and stays connected at its anchor.
3.0-7.0 s — the engineer's glove closes on it once and the line takes up.
7.0-10.0 s — she pulls herself onto the handhold and holds there, the line still anchored, her shoulders dropping as the load takes up.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Suit movement, breathing, and one short filtered line. The line spoken is "Take the line." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The line stays continuously attached at both ends, never stretches and never leaves the frame.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 68 — S17 · 4/4 · SONUC — BAĞIMSIZ GÜÇ

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 68 of 96.
CONTINUOUS ACTION: the engineer is already back on the handhold with the safety line still anchored.

A four-fingered hand reads a bank of plain pod power indicators one at a time and each one shows the same independent state; in the corner of the frame the same gate reference stands, its opening drawn in another clear step since the last time it was seen. The tall systems engineer's hand has four fingers and wears white elongated armour with copper joints at the wrist.
LIGHT: Even cool white ceiling light in the pressurised service compartment with a colder pool at the panel and one warmer light low near the deck; the white suits keep panel detail and the shadows stay shallow.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus.

NEGATIVE: Exactly 0 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 68 of 96.
CONTINUOUS ACTION: the engineer is already back on the handhold with the safety line still anchored.

START FRAME: the approved detail frame on the pod power panel with the indicators already lit.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the hand moves along the first indicators and each holds its own state.
3.0-7.0 s — it reaches the last of them and they all hold together.
7.0-10.0 s — the hand comes off the panel, the states hold, and the opening in the corner keeps closing.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Panel contacts, then a translated adult voice. The line spoken is "The transfer pods have independent power." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 18 — KAÇIŞIN BİÇİMİ DEĞİŞİYOR  (4 klip · 11:20–12:00)

## 🎬 KLİP 69 — S18 · 1/4 · TERSLIK — GEMİ ARTIK SIĞMAZ

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 69 of 96.

On the same gate axis the closed-in opening is now plainly smaller than the ship's fixed cross-section: the circular profile of the central pressure body overlaps the bright edge all the way round and cannot be put through it. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cold instrument light from the consoles below, a pale even glow from the gate field down the axis, and cool white bay lamps where the module spine opens off the bridge; no surface blooms.
CAMERA: 85mm lens on a locked-off camera 2600 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Turning the ship or shedding outer structure never makes the fixed central body smaller.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 69 of 96.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved gate-axis frame with the opening already close to the ship's own profile.
CAMERA: 85mm lens on a locked-off camera 2600 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the edge draws in past the width of the ship's profile.
3.0-7.0 s — the overlap is unmistakable all the way round the circle.
7.0-10.0 s — the frame holds on that overlap and the edge keeps closing.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Console silence, then one short filtered line. The line spoken is "We will not fit." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Turning the ship or shedding outer structure never makes the fixed central body smaller.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 70 — S18 · 2/4 · KARAR — ROTAYI SABİTLEME

### 📸 IMAGE PROMPT

```
IN FRAME: back · torso · hands
Clip 70 of 96.
CONTINUOUS ACTION: the ship's profile is already wider than the opening ahead of it.

Over the pilot's shoulder she brings the ship off the line that led into the ring and holds it on a course parallel to the pod exit lane instead; beyond the glass the ring slides off centre and stays off centre. The pilot wears a satin off-white ceramic suit with champagne-gold frame lines at the joints, a single neck ring and heavy white gloves. The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. A single diagonal scuff runs across the outer plate of the pilot's left forearm. On the left upper arm is a textless circular survey patch.
LIGHT: Cold instrument light from the consoles below, a pale even glow from the gate field down the axis, and cool white bay lamps where the module spine opens off the bridge; no surface blooms.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The ship never strikes or grazes the gate structure and never enters the opening.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: back · torso · hands
Clip 70 of 96.
CONTINUOUS ACTION: the ship's profile is already wider than the opening ahead of it.

The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing.

START FRAME: the approved over-shoulder frame with the ring still centred beyond the glass.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — she takes the course control and eases it over.
3.0-7.0 s — the ring moves off the centre of the glass and the shaking in the cockpit drops away.
7.0-10.0 s — she holds the new course and the ring stays off centre.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A drive command, then the cockpit vibration settling. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The ship never strikes or grazes the gate structure and never enters the opening.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 71 — S18 · 3/4 · EYLEM — YENİ ÇÖZÜM

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 71 of 96.
CONTINUOUS ACTION: the ship is already holding the course parallel to the pod exit lane.

A gloved hand rests beside the same plain mechanical release lever on the flank of a berthed transfer pod and then touches the four small thruster nozzles under it — the identical pod design seen berthing at the start of the film, found again as a physical object. The engineer wears white technical forearm panels in cobalt over white gloves. The pilot wears heavy white gloves over a satin off-white ceramic forearm plate with one champagne-gold frame line at the wrist joint. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Only gloved hands and forearms are in frame; the two pairs keep separate halves of the frame and never overlap.
LIGHT: Cold instrument light from the consoles below, a pale even glow from the gate field down the axis, and cool white bay lamps where the module spine opens off the bridge; no surface blooms.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus — the same position, height and lens as Clip 68.

NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 71 of 96.
CONTINUOUS ACTION: the ship is already holding the course parallel to the pod exit lane.

START FRAME: the approved detail frame on the pod flank with the release lever and nozzles in place.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus — the same position, height and lens as Clip 68.
TIMELINE:
0.0-3.0 s — the hand comes onto the flank beside the release lever and stops there, her grip tightening on the rail as the mass comes with her.
3.0-7.0 s — it moves down to the four nozzles and rests against them one at a time.
7.0-10.0 s — the hand stays on the last nozzle and neither lever nor nozzle moves.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Glove contacts on metal, then a short filtered line. The line spoken is "The pods will fit." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 72 — S18 · 4/4 · SONUC — KALKAN FİKRİ

### 📸 IMAGE PROMPT

```
IN FRAME: back · torso · hands
Clip 72 of 96.
CONTINUOUS ACTION: the pod release lever and its thruster nozzles have just been checked by hand.

Over a shoulder a plain three-part diagram is turned flat: the pursuing craft aft, the ship's own mass in the middle and the pod exit lane in front, with the middle shape sitting directly between the other two. The pilot wears a satin off-white ceramic suit with champagne-gold frame lines at the joints, a single neck ring and heavy white gloves. The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. A single diagonal scuff runs across the outer plate of the pilot's left forearm. The two figures keep separate halves of the frame and never overlap.
LIGHT: Cold instrument light from the consoles below, a pale even glow from the gate field down the axis, and cool white bay lamps where the module spine opens off the bridge; no surface blooms.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus — the same position, height and lens as Clip 70.

NEGATIVE: Exactly 2 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The diagram is plain outline geometry only, with nothing written or numbered on it.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: back · torso · hands
Clip 72 of 96.
CONTINUOUS ACTION: the pod release lever and its thruster nozzles have just been checked by hand.

The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing.

START FRAME: the approved over-shoulder frame with the three-part diagram already open.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus — the same position, height and lens as Clip 70.
TIMELINE:
0.0-3.0 s — a four-fingered hand turns the diagram flat to the lens.
3.0-7.0 s — the middle shape is moved once into line between the other two and stays there.
7.0-10.0 s — the arrangement holds and the hand comes away from it.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Panel contact, then a translated adult voice. The line spoken is "Keep the hull between us and them." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The diagram is plain outline geometry only, with nothing written or numbered on it.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```
