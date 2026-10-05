# 🎬 THE_LAST_GATE — BÖLÜM 3  (K25 – K36 · S07 – S09)

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
KURULUM İSKELETİ: D C G E G J A B F G V I
ölçülen DÖNÜŞ: 1/12 — aynı harf = birebir aynı CAMERA satırı
⛔ K01–K04 harf taşımaz: kurgu bloklarıdır, kendi görüntüsü üretilmez.
```
---

# 📍 SAHNE 07 — EKİP VE HAZIRLIK  (4 klip · 4:00–4:40)

## 🎬 KLİP 25 — S07 · 1/4 · KURULUM — TANITIM

### 📸 IMAGE PROMPT

```
IN FRAME: face · hands
Clip 25 of 96.

The tall systems engineer is read in one clear frame: an adult face with two symmetrical bony plates behind a clear helmet, and a four-fingered hand closing around a hand tool at the rail. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film. The tall systems engineer stands a head and a half above the humans in white elongated armour with copper joints and two neck rings, four fingers on each hand, and two symmetrical bony plates on the face behind a clear helmet. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. On the chest is a textless three-part technical badge in embossed embroidery.
LIGHT: Cool white bay lamps along the module spine with a colder pool at the local control socket; the white suits and the copper joints keep surface detail and no surface blooms.
CAMERA: 85mm lens on a locked-off camera 1.2 m from the helmet, camera height 1.55 m, eye-level close-up, shallow focus.

NEGATIVE: Exactly 0 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Exactly four fingers on each hand, two neck rings and two face plates, with no extra limb and no second tall figure.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · hands
Clip 25 of 96.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved close frame of the tall engineer with the hand tool already at the rail.
CAMERA: 85mm lens on a locked-off camera 1.2 m from the helmet, camera height 1.55 m, eye-level close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the head turns a short way and the two face plates come into the light.
3.0-7.0 s — the four-fingered hand closes on the tool and takes its weight.
7.0-10.0 s — the hand holds the tool still and the head stays where it turned to.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A translated adult voice from the suit unit, single channel and level. The line spoken is "We needed a pilot." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Exactly four fingers on each hand, two neck rings and two face plates, with no extra limb and no second tall figure.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 26 — S07 · 2/4 · EYLEM — ÜÇ GÖREV

### 📸 IMAGE PROMPT

```
IN FRAME: back · torso · hands
Clip 26 of 96.
CONTINUOUS ACTION: the three of them have just closed up around the panel with the tall engineer at the rail.

Over the pilot's shoulder a plain outline plan of the ship shows three separate points picked out on the same map: the bridge route forward, the cell control amidships and the flight interlock aft; three gloved hands are on the panel edge at once. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap. On the left upper arm is a textless circular survey patch.
LIGHT: Cool white bay lamps along the module spine with a colder pool at the local control socket; the white suits and the copper joints keep surface detail and no surface blooms.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The ship plan is plain outline geometry with nothing written, numbered or labelled on it.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: back · torso · hands
Clip 26 of 96.
CONTINUOUS ACTION: the three of them have just closed up around the panel with the tall engineer at the rail.

The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing.

START FRAME: the approved over-shoulder frame of the outline ship plan with three hands already at its edge.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — one hand sets a mark on the forward point and holds.
3.0-7.0 s — a second hand marks amidships and a four-fingered hand marks the aft point.
7.0-10.0 s — all three marks stay lit together and no hand moves again.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Three short work confirmations on the local channel, nothing explained. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The ship plan is plain outline geometry with nothing written, numbered or labelled on it.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 27 — S07 · 3/4 · EYLEM — EKİP SORUMLUSU

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 27 of 96.
CONTINUOUS ACTION: the three task points are already marked on the plan and the work has just been shared out.

The crew lead and five adult astronauts work the bay latches down one side of the spine, one person to one latch, each anchored on their own boot locks; the grey shoulder stripe marks the crew lead at the near end. The crew lead wears a white pressure suit with a grey shoulder stripe and a short visor frame. The other adults wear the same white main suit with measured blue and grey duty panels and closed helmets. Each figure keeps its own station in the frame and no two of them overlap. Every badge and patch is textless, a single geometric motif in embossed embroidery, with nothing written on any of them.
LIGHT: Cool white bay lamps along the module spine with a colder pool at the local control socket; the white suits and the copper joints keep surface detail and no surface blooms.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.

NEGATIVE: Exactly 6 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Six separate adults at six separate latches, spaced apart with clear deck between them, each one working only their own latch.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 27 of 96.
CONTINUOUS ACTION: the three task points are already marked on the plan and the work has just been shared out.

START FRAME: the approved spine frame with six adults spaced at six latches, none of them moving yet.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the crew lead starts the nearest latch alone and turns it a short way.
3.0-7.0 s — a second later the next one along starts hers, then the third, each one behind the last.
7.0-10.0 s — all six keep working their own latch and nobody leaves a station.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Six latches turning out of step, then a short filtered line. The line spoken is "We can move the others." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 6 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Six separate adults at six separate latches, spaced apart with clear deck between them, each one working only their own latch.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 28 — S07 · 4/4 · SONUC — YEREL KONTROL

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 28 of 96.
CONTINUOUS ACTION: the six bay latches are already turning further down the spine and the connector is already in his hand.

A four-fingered hand seats a service connector into a local control socket and two prepared interlocks release one after the other; the connector body is the same plain type seen on the transfer pods. The tall systems engineer's hand has four fingers and wears white elongated armour with copper joints at the wrist.
LIGHT: Cool white bay lamps along the module spine with a colder pool at the local control socket; the white suits and the copper joints keep surface detail and no surface blooms.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus.

NEGATIVE: Exactly 0 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 28 of 96.
CONTINUOUS ACTION: the six bay latches are already turning further down the spine and the connector is already in his hand.

START FRAME: the approved detail frame of the local control socket with the connector held just clear of it.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the connector goes into the socket and seats with one short push.
3.0-7.0 s — the first interlock releases, then the second, each one a separate state change.
7.0-10.0 s — both stay released and the connector stays seated.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Relay clicks, then one short confirmation tone. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 08 — DİKKAT DAĞITMA  (4 klip · 4:40–5:20)

## 🎬 KLİP 29 — S08 · 1/4 · KURULUM — GÖRÜŞ HATTI

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 29 of 96.

In one master frame the two guards hold the left end of the compartment, the pilot brings a maintenance shield into their sightline at centre, and the engineer and the tall systems engineer wait at the bridge door on the right; two short reports go into the panelling above the shield. The guard wears white protective pressure gear with a single red mark on one upper arm. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap.
LIGHT: Cool white corridor light on the near side, and outside hard sunlight from screen left with a broad copper wash from the banded planet filling the background; shadow edges stay razor-sharp and nothing blooms.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus — the same position, height and lens as Clip 27.

NEGATIVE: Exactly 4 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Both shots go into the upper panelling only and never toward a person — no figure touches another.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 29 of 96.

START FRAME: the approved master frame with the guards left, the shield at centre and the bridge door right.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus — the same position, height and lens as Clip 27.
TIMELINE:
0.0-3.0 s — the pilot rolls the shield a short way along its rail into the sightline.
3.0-7.0 s — two separate reports mark the panelling well above the shield edge.
7.0-10.0 s — every figure holds its own side of the frame; nobody crosses.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Two short reports in the compartment and shield rail friction. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 4 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Both shots go into the upper panelling only and never toward a person — no figure touches another.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 30 — S08 · 2/4 · EYLEM — KENDİ ARACINI BIRAKMA

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 30 of 96.
CONTINUOUS ACTION: the maintenance shield is already holding the sightline at her back.

A gloved hand confirms on a control detail that the small service craft is sealed and unmanned, then releases the berth: the four small berth clamps are commanded open and their four state marks change together. The pilot wears heavy white gloves over a satin off-white ceramic forearm plate with one champagne-gold frame line at the wrist joint. A single diagonal scuff runs across the outer plate of the pilot's left forearm.
LIGHT: Cool white corridor light on the near side, and outside hard sunlight from screen left with a broad copper wash from the banded planet filling the background; shadow edges stay razor-sharp and nothing blooms.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Exactly four berth clamps release, not six, and the six main cradle locks are not touched.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 30 of 96.
CONTINUOUS ACTION: the maintenance shield is already holding the sightline at her back.

START FRAME: the approved macro frame of the berth control with all four clamp marks in the closed state.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the glove checks the seal state and holds on it.
3.0-7.0 s — the same hand commands the release and the four clamp marks change state together.
7.0-10.0 s — the hand comes off the control and the four marks stay changed.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Four soft releases carried through structure, then a short filtered line. The line spoken is "Send my shuttle empty. Draw them off." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Exactly four berth clamps release, not six, and the six main cradle locks are not touched.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 31 — S08 · 3/4 · EYLEM — DİKKAT DAĞITMA

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 31 of 96.
CONTINUOUS ACTION: the empty craft has already left the berth and is already clear of the hull.

The empty white service craft runs out along a side inspection corridor of the port; a small dark interceptor that had been holding station off the berth leaves that line and turns onto the craft's track, plainly the shorter of the two shapes with a narrow black nose. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cool white corridor light on the near side, and outside hard sunlight from screen left with a broad copper wash from the banded planet filling the background; shadow edges stay razor-sharp and nothing blooms.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No atmospheric engine sound and no exhaust trail in vacuum — the efflux is a straight narrow cone that thins and is gone.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 31 of 96.
CONTINUOUS ACTION: the empty craft has already left the berth and is already clear of the hull.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved wide frame with the empty craft at centre and the interceptor still on station.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the empty craft holds its line out along the corridor.
3.0-7.0 s — the interceptor comes off station and swings onto the same track behind it.
7.0-10.0 s — both hold that line, the interceptor closing very slowly.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A radio bridge from inside the hull and the music rising, no engine sound from outside. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No atmospheric engine sound and no exhaust trail in vacuum — the efflux is a straight narrow cone that thins and is gone.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 32 — S08 · 4/4 · BEDEL — KAÇIŞ ARACININ KAYBI

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 32 of 96.
CONTINUOUS ACTION: the interceptor is already on the empty craft's track and closing.

One single shot from the interceptor takes out the drive section of the empty service craft: a small bright scar opens on the drive housing, a short straight jet of propellant leaves it and thins to nothing, and the craft goes on along its old track with separate loose parts drifting beside it. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cool white corridor light on the near side, and outside hard sunlight from screen left with a broad copper wash from the banded planet filling the background; shadow edges stay razor-sharp and nothing blooms.
CAMERA: 35mm lens on a locked-off camera 8.0 m from the subject, camera height 0.9 m, low-angle wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No fireball, no shockwave and no expanding cloud — the craft is unmanned and nobody is aboard it.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 32 of 96.
CONTINUOUS ACTION: the interceptor is already on the empty craft's track and closing.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved side frame with the empty craft filling the frame and the interceptor behind it.
CAMERA: 35mm lens on a locked-off camera 8.0 m from the subject, camera height 0.9 m, low-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the single shot crosses and marks the drive housing.
3.0-7.0 s — a straight propellant jet leaves the housing and thins out to nothing.
7.0-10.0 s — the craft keeps exactly the motion it had, its loose parts drifting with it.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A radio link inside the helmet cutting out mid-carrier, nothing from outside. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No fireball, no shockwave and no expanding cloud — the craft is unmanned and nobody is aboard it.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 09 — KÖPRÜ  (4 klip · 5:20–6:00)

## 🎬 KLİP 33 — S09 · 1/4 · KURULUM — KÖPRÜ EŞİĞİ

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 33 of 96.

The engineer opens the bridge service door and the three of them come through it on the corridor line they were already on; approaching guard traffic is audible from the far side of the compartment they came from. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The tall systems engineer stands a head and a half above the humans in white elongated armour with copper joints and two neck rings, four fingers on each hand, and two symmetrical bony plates on the face behind a clear helmet. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap.
LIGHT: Cold instrument light from three consoles below, a colder pool at the bridge service door, and a wide copper wash from the banded planet through the forward glass; faces stay readable behind the clear visors.
CAMERA: 50mm lens on a locked-off camera 2.4 m along the corridor axis, camera height 1.50 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 33 of 96.

START FRAME: the approved corridor frame at the bridge service door, the door still closed.
CAMERA: 50mm lens on a locked-off camera 2.4 m along the corridor axis, camera height 1.50 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — the engineer works the door release and the panel travels open.
3.0-7.0 s — the pilot goes through first on the rail, the tall engineer after her.
7.0-10.0 s — the engineer follows and all three are through; the door stands open.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A lock releasing, then guard movement from the far end. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 34 — S09 · 2/4 · MUCADELE — GECİKTİRME

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 34 of 96.
CONTINUOUS ACTION: all three have just come through the bridge service door at his back.

In one two-sided frame the tall systems engineer closes an intermediate bulkhead panel and the two guards are left on the far side of it, both plainly on their feet and both anchored; the panel seats and holds. The guard wears white protective pressure gear with a single red mark on one upper arm. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap.
LIGHT: Cold instrument light from three consoles below, a colder pool at the bridge service door, and a wide copper wash from the banded planet through the forward glass; faces stay readable behind the clear visors.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Both guards stay upright and unharmed on the far side — no figure is struck, caught or vented out. The panel never passes through a body and no body passes through the panel — the panel closes in clear space.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 34 of 96.
CONTINUOUS ACTION: all three have just come through the bridge service door at his back.

START FRAME: the approved two-sided frame with the intermediate panel still open and both guards beyond it.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the four-fingered hand takes the panel control and the panel starts across.
3.0-7.0 s — the panel travels shut with both guards clearly standing on the far side.
7.0-10.0 s — the panel seats; one flat metal strike comes from the far side and nothing gives.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A panel seating, then a flat strike on its far face. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Both guards stay upright and unharmed on the far side — no figure is struck, caught or vented out. The panel never passes through a body and no body passes through the panel — the panel closes in clear space.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 35 — S09 · 3/4 · EYLEM — PİLOT KOLTUĞU

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso · hands
Clip 35 of 96.
CONTINUOUS ACTION: the intermediate panel is already shut at their backs and the bridge is already open ahead.

The pilot settles into the pilot's seat and closes her harness latch, and the engineer and the tall systems engineer take their own consoles at the left and right edges of the frame, each anchoring on a handhold rather than sitting under weight. The engineer wears a white technical suit with cobalt shoulder and forearm panels. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, a single neck ring and heavy white gloves. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap. On the right chest is a textless three-winged pilot badge in embossed embroidery, and on the left upper arm a textless circular survey patch.
LIGHT: Cold instrument light from three consoles below, a colder pool at the bridge service door, and a wide copper wash from the banded planet through the forward glass; faces stay readable behind the clear visors.
CAMERA: 50mm lens on a locked-off camera 2.6 m from the pilot's seat on the starboard side, camera height 1.45 m, three-quarter front medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso · hands
Clip 35 of 96.
CONTINUOUS ACTION: the intermediate panel is already shut at their backs and the bridge is already open ahead.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved front three-quarter seat frame with the pilot's seat still empty.
CAMERA: 50mm lens on a locked-off camera 2.6 m from the pilot's seat on the starboard side, camera height 1.45 m, three-quarter front medium shot, deep focus.
TIMELINE:
0.0-3.0 s — she brings herself into the seat on the handholds and squares up.
3.0-7.0 s — the harness latch closes across her and takes up.
7.0-10.0 s — the other two settle at their consoles and all three hold their stations.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A harness latch, then the fans and system hum coming up. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 36 — S09 · 4/4 · SONUC — KONTROL ALINDI

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso
Clip 36 of 96.
CONTINUOUS ACTION: she is already in the pilot's seat with her harness closed.

The pilot takes flight authority at the main console and the two consoles either side of her come live; through the forward glass the port structures stand still, nothing yet moving. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap.
LIGHT: Cold instrument light from three consoles below, a colder pool at the bridge service door, and a wide copper wash from the banded planet through the forward glass; faces stay readable behind the clear visors.
CAMERA: 50mm lens on a locked-off camera 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso
Clip 36 of 96.
CONTINUOUS ACTION: she is already in the pilot's seat with her harness closed.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved three-console frame with the main console not yet live.
CAMERA: 50mm lens on a locked-off camera 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot, deep focus.
TIMELINE:
0.0-3.0 s — her hand closes the authority control and the main console comes up.
3.0-7.0 s — the two side consoles come live in turn to either side of her.
7.0-10.0 s — all three hold lit and the port beyond the glass has not moved.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. Nothing changes course without contact: whatever moves has been gripped, pushed against or thrust, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Consoles coming up in sequence, then a short filtered line. The line spoken is "We have the ship." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```
