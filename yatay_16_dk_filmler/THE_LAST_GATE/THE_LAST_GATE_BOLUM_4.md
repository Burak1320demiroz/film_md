# 🎬 THE_LAST_GATE — BÖLÜM 4  (K37 – K48 · S10 – S12)

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
KURULUM İSKELETİ: G E B N A C B A I A M J
ölçülen DÖNÜŞ: 3/12 — aynı harf = birebir aynı CAMERA satırı
⛔ K01–K04 harf taşımaz: kurgu bloklarıdır, kendi görüntüsü üretilmez.
```
---

# 📍 SAHNE 10 — LİMAN BAĞLANTILARI  (4 klip · 6:00–6:40)

## 🎬 KLİP 37 — S10 · 1/4 · KURULUM — TOPLU HAZIRLIK

### 📸 IMAGE PROMPT

```
IN FRAME: full body
Clip 37 of 96.

The crew lead's team has the bays open and is settling adult astronauts into the seats of a berthed transfer pod: seven adults are already in their own seats along the pod with their harnesses down, and the crew lead stands at the pod door working the next harness. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film. The crew lead wears a white pressure suit with a grey shoulder stripe and a short visor frame. The other adults wear the same white main suit with measured blue and grey duty panels and closed helmets. Each figure keeps its own station in the frame and no two of them overlap. Every badge and patch is textless, a single geometric motif in embossed embroidery, with nothing written on any of them.
LIGHT: Cool white bay lamps along the module spine on the near side, and outside cold white port lamps with a copper wash from the banded planet below; every white surface keeps visible texture and nothing blooms.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.

NEGATIVE: Exactly 8 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Seven adults are each seated in one separate seat with clear space between the seats, and one more stands alone at the door.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: full body
Clip 37 of 96.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved spine frame at the open pod door with seven seats already filled.
CAMERA: 24mm lens on a locked-off camera 9.0 m from the spine, camera height 2.60 m, high-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the crew lead brings the next harness down over a seated adult and it takes.
3.0-7.0 s — two of the seated adults check their own latches; nobody stands up.
7.0-10.0 s — every one of them stays in a seat and the pod door stays open.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Local direction on the crew channel and harness latches closing, spaced and dull. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 8 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Seven adults are each seated in one separate seat with clear space between the seats, and one more stands alone at the door.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 38 — S10 · 2/4 · EYLEM — YAŞAM HATLARI

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 38 of 96.
CONTINUOUS ACTION: the pod seats are already filled and their harnesses are already down.

The two pressure panels of the port transfer tunnel close in turn and both show their closed state, and the service line valves beside them are shut off one after the other. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cool white bay lamps along the module spine on the near side, and outside cold white port lamps with a copper wash from the banded planet below; every white surface keeps visible texture and nothing blooms.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No air escapes anywhere and no volume is vented while people are aboard.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 38 of 96.
CONTINUOUS ACTION: the pod seats are already filled and their harnesses are already down.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved detail frame with both pressure panels still open and the valves still open.
CAMERA: 85mm lens on a locked-off camera 3.0 m from the mechanism, camera height 1.30 m, eye-level close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the first pressure panel travels shut and seats.
3.0-7.0 s — the second follows it and both closed states come up together.
7.0-10.0 s — the valves turn off in order beside them and nothing reopens.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Valves, a panel seating, then the remaining interior fan carried through the hull. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No air escapes anywhere and no volume is vented while people are aboard.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 39 — S10 · 3/4 · EYLEM — GÖBEK BAĞLARI

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 39 of 96.
CONTINUOUS ACTION: both pressure panels are already shut and their valves already closed.

Two countable groups of umbilical lines — one power, one fluid — are drawn back into the same two sockets they came out of by mechanical reels, each group keeping its own bundle shape. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cool white bay lamps along the module spine on the near side, and outside cold white port lamps with a copper wash from the banded planet below; every white surface keeps visible texture and nothing blooms.
CAMERA: 35mm lens on a locked-off camera 8.0 m from the subject, camera height 0.9 m, low-angle wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly two umbilical groups, no more — no line multiplies, whips or coils like a rope.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 39 of 96.
CONTINUOUS ACTION: both pressure panels are already shut and their valves already closed.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved low wide frame with both umbilical groups still connected and slack.
CAMERA: 35mm lens on a locked-off camera 8.0 m from the subject, camera height 0.9 m, low-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the reels take up and the slack comes out of both groups at once.
3.0-7.0 s — each group draws straight back toward its own socket, keeping its bundle.
7.0-10.0 s — both groups are home in their sockets and the reels stop.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A mechanical take-up carried through structure, with a radio bridge over the wide frame. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly two umbilical groups, no more — no line multiplies, whips or coils like a rope.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 40 — S10 · 4/4 · SONUC — TAŞIYICI KENETLER

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 40 of 96.
CONTINUOUS ACTION: both umbilical groups are already drawn back into their sockets.

Along one axis of the port cradle six main carrying locks release in order, each one swinging clear of the hull and showing its open state; until the sixth is clear the enormous hull does not move at all. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cool white bay lamps along the module spine on the near side, and outside cold white port lamps with a copper wash from the banded planet below; every white surface keeps visible texture and nothing blooms.
CAMERA: 32mm lens on a locked-off camera 20 m out along the rail, camera height 0.8 m above the rail line, low-angle wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly six carrying locks, no more and no fewer, and the hull does not begin to move in this shot.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 40 of 96.
CONTINUOUS ACTION: both umbilical groups are already drawn back into their sockets.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved rail frame along the cradle with all six carrying locks closed on the hull.
CAMERA: 32mm lens on a locked-off camera 20 m out along the rail, camera height 0.8 m above the rail line, low-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the first two locks swing clear and show open.
3.0-7.0 s — three more follow along the same axis, each with the same travel.
7.0-10.0 s — the sixth releases and the hull stays exactly where it is, not moving yet.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Six heavy strikes spaced along the cradle, then one flight clearance tone. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly six carrying locks, no more and no fewer, and the hull does not begin to move in this shot.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 11 — ÖLÇEĞİN KARŞILIĞI  (4 klip · 6:40–7:20)

## 🎬 KLİP 41 — S11 · 1/4 · BELIRIS — DEV GEMİ HAREKET EDİYOR

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 41 of 96.

The enormous prison hull comes slowly out of its cradle and its whole outer shape is readable at once: six long outer ribs along a dark central pressure body, with the port cradle around it, a stretch of the shallow dock arc beyond and the banded copper limb of the gas giant filling the background. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Hard sunlight from screen left, a broad copper wash from the banded planet filling the whole background, and small cold lamps along the port structures; shadow edges stay razor-sharp and nothing in frame blooms.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The hull moves as one rigid body with no flexing and no part detaching — no exterior engine roar.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 41 of 96.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved main scale frame with the hull still seated in its cradle.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the hull begins to translate out of the cradle, slowly and in one direction.
3.0-7.0 s — a clear gap opens between hull and cradle along its whole length.
7.0-10.0 s — it keeps that same slow rate; nothing accelerates and nothing rotates.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. An interior drive vibration carried through the hull as the sound bridge, no exterior rumble. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The hull moves as one rigid body with no flexing and no part detaching — no exterior engine roar.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 42 — S11 · 2/4 · MUCADELE — HASSAS PİLOTAJ

### 📸 IMAGE PROMPT

```
IN FRAME: back · torso · hands
Clip 42 of 96.
CONTINUOUS ACTION: the hull is already translating out of the cradle at a steady rate.

Over the pilot's shoulder both her gloves make small separate corrections on the console while a port reference column stands in the same view beyond the glass, holding its distance from the hull's aft quarter. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. A single diagonal scuff runs across the outer plate of the pilot's left forearm. On the right chest is a textless three-winged pilot badge in embossed embroidery, and on the left upper arm a textless circular survey patch.
LIGHT: Hard sunlight from screen left, a broad copper wash from the banded planet filling the whole background, and small cold lamps along the port structures; shadow edges stay razor-sharp and nothing in frame blooms.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The controls never become heavy or stiff like a steering wheel — the difficulty is timing only.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: back · torso · hands
Clip 42 of 96.
CONTINUOUS ACTION: the hull is already translating out of the cradle at a steady rate.

The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing.

START FRAME: the approved over-shoulder frame with the reference column already in view beyond the glass.
CAMERA: 35mm lens on a locked-off camera 1.5 m behind the seat, camera height 1.45 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — her left glove trims one control a short way and stops.
3.0-7.0 s — a proximity tone comes up; her right glove trims a second control the other way.
7.0-10.0 s — she holds both hands on the controls and the column keeps its distance.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A proximity tone and one short controlled breath. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The controls never become heavy or stiff like a steering wheel — the difficulty is timing only.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 43 — S11 · 3/4 · EYLEM — SON YAPIDAN SIYRILMA

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 43 of 96.
CONTINUOUS ACTION: the hull is already most of the way out with the aft rib still inside the arch.

The aft rib of the enormous hull passes the last arch of the port with clear space on both sides; the two rigid shapes never touch and the gap between them can be read from the start of the shot to the end. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Hard sunlight from screen left, a broad copper wash from the banded planet filling the whole background, and small cold lamps along the port structures; shadow edges stay razor-sharp and nothing in frame blooms.
CAMERA: 35mm lens on a locked-off camera 8.0 m from the subject, camera height 0.9 m, low-angle wide shot, deep focus — the same position, height and lens as Clip 39.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Neither shape deforms, scrapes or bends — the gap never closes to contact.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 43 of 96.
CONTINUOUS ACTION: the hull is already most of the way out with the aft rib still inside the arch.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved side frame with the aft rib still inside the last arch and clear space visible.
CAMERA: 35mm lens on a locked-off camera 8.0 m from the subject, camera height 0.9 m, low-angle wide shot, deep focus — the same position, height and lens as Clip 39.
TIMELINE:
0.0-3.0 s — the rib moves along the arch with the gap holding.
3.0-7.0 s — the rib clears the arch completely and the gap opens out.
7.0-10.0 s — the hull runs on clear; the proximity tone stops and nothing has touched.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A proximity tone cutting out, then structure noise settling. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Neither shape deforms, scrapes or bends — the gap never closes to contact.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 44 — S11 · 4/4 · SONUC — GEZEGEN ÖLÇEĞİ

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 44 of 96.
CONTINUOUS ACTION: the aft rib has already cleared the last arch of the port.

The prison hull is fully clear of the port and the frame belongs to the planet: the banded copper limb and one large pale storm run from edge to edge behind it, with the hull and the dock structures sharing the same environment reference. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Hard sunlight from screen left, a broad copper wash from the banded planet filling the whole background, and small cold lamps along the port structures; shadow edges stay razor-sharp and nothing in frame blooms.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus — the same position, height and lens as Clip 41.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The hull is never inside an atmosphere and never flies through nearby cloud.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 44 of 96.
CONTINUOUS ACTION: the aft rib has already cleared the last arch of the port.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved extreme wide frame with the hull just clear of the port structures.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus — the same position, height and lens as Clip 41.
TIMELINE:
0.0-3.0 s — the hull moves out across the banded limb at the same steady rate.
3.0-7.0 s — the whole shape comes into open space with the storm band behind it.
7.0-10.0 s — it holds that line and the planet behind it does not change.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. The music opening out for the first time, then an alarm returning under it. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The hull is never inside an atmosphere and never flies through nearby cloud.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 12 — TAKİP VE KAPANIŞ EMRİ  (4 klip · 7:20–8:00)

## 🎬 KLİP 45 — S12 · 1/4 · KURULUM — KISA RAHATLAMA

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso
Clip 45 of 96.

The three of them look over the working flight systems from their stations, and the engineer lets out the first small easing of the film — a shoulder dropping and a breath going out behind a clear visor. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap.
LIGHT: Cold instrument light from the consoles below on the near side, outside hard sunlight from screen left with a copper wash from the banded planet, and on the command ship a narrow cold overhead strip with a dim red console edge; no surface blooms.
CAMERA: 50mm lens on a locked-off camera 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso
Clip 45 of 96.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved three-console frame with all systems already lit.
CAMERA: 50mm lens on a locked-off camera 3.0 m from the consoles, camera height 2.20 m, high-angle medium shot, deep focus.
TIMELINE:
0.0-3.0 s — all three read their own stations; nothing needs correcting.
3.0-7.0 s — the engineer's shoulders come down and her breath goes out.
7.0-10.0 s — the three hold their stations and the moment is allowed to sit.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. The flight systems settling into a steady bed, then a short filtered line. The line spoken is "The cells are open." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 46 — S12 · 2/4 · TERSLIK — TAKİP

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 46 of 96.
CONTINUOUS ACTION: the prison hull is already running clear of the port ahead of them.

Three pursuing craft form up on the prison hull's stern quarter: the long command ship and one interceptor leaving the port together, joined by the smaller interceptor already in flight — three distinct shapes, one long and two short, one of the short pair with a narrow black nose and the other with two side attachments. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Cold instrument light from the consoles below on the near side, outside hard sunlight from screen left with a copper wash from the banded planet, and on the command ship a narrow cold overhead strip with a dim red console edge; no surface blooms.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus — the same position, height and lens as Clip 44.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly three pursuing craft, no fleet and no repeated copies of the same shape.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 46 of 96.
CONTINUOUS ACTION: the prison hull is already running clear of the port ahead of them.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved wide frame with the command ship and one interceptor still at the port.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus — the same position, height and lens as Clip 44.
TIMELINE:
0.0-3.0 s — the command ship and the first interceptor come off the port together.
3.0-7.0 s — the second interceptor closes in from screen left and joins them.
7.0-10.0 s — the three hold one formation and no fourth shape appears.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A command channel carrier and the rhythm building under it. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly three pursuing craft, no fleet and no repeated copies of the same shape.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 47 — S12 · 3/4 · EYLEM — KOMUTANIN HEDEFİ

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso
Clip 47 of 96.
CONTINUOUS ACTION: the three pursuing craft are already in formation off the hull's stern quarter.

On the command bridge the commanding officer sets a hand flat on the console rail and marks the drive section of the fleeing hull as the target; the dark red arm band stays the darkest value in the frame. The commanding officer wears sharp-edged white military pressure armour with one dark red band running the full length of the left arm and a narrow visor. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. On the chest is a textless angular rank patch in embossed embroidery.
LIGHT: Cold instrument light from the consoles below on the near side, outside hard sunlight from screen left with a copper wash from the banded planet, and on the command ship a narrow cold overhead strip with a dim red console edge; no surface blooms.
CAMERA: 50mm lens on a locked-off camera 1.4 m from the console rail, camera height 1.15 m, low-angle medium shot, shallow focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso
Clip 47 of 96.
CONTINUOUS ACTION: the three pursuing craft are already in formation off the hull's stern quarter.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved command-bridge frame, the officer at the rail with the target not yet set.
CAMERA: 50mm lens on a locked-off camera 1.4 m from the console rail, camera height 1.15 m, low-angle medium shot, shallow focus.
TIMELINE:
0.0-3.0 s — the officer reads the rail and the hand comes onto it.
3.0-7.0 s — the flat hand moves once across the rail and the target mark settles on the drive section.
7.0-10.0 s — the hand stays down and the mark holds where it was put.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A flat filtered command voice on the ship channel. The line spoken is "Disable the drives. Keep the prisoners alive." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 48 — S12 · 4/4 · SONUC — KAPATMA EMRİ

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 48 of 96.
CONTINUOUS ACTION: the target mark is already set on the drive section of the fleeing hull.

A gloved hand in white armour closes one guarded control on the command rail and the state of the distant ring field changes on the plain circular readout beside it: a wide open circle begins to draw in toward its own centre while the outer ring holds its size. The commanding officer wears sharp-edged white military pressure armour with one dark red band running the full length of the left arm and a narrow visor. On the chest is a textless angular rank patch in embossed embroidery.
LIGHT: Cold instrument light from the consoles below on the near side, outside hard sunlight from screen left with a copper wash from the banded planet, and on the command ship a narrow cold overhead strip with a dim red console edge; no surface blooms.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.

NEGATIVE: Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The readout is plain circular geometry only, with nothing written or numbered on it.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 48 of 96.
CONTINUOUS ACTION: the target mark is already set on the drive section of the fleeing hull.

START FRAME: the approved macro frame on the guarded control with the circular readout still wide open.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the guard over the control lifts and the hand closes on it, her grip tightening on the rail as the mass comes with her.
3.0-7.0 s — the control goes over and the inner circle on the readout starts drawing inward.
7.0-10.0 s — the hand comes off; the inner circle keeps closing and the outer ring does not change.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. One heavy control closing, then a flat filtered command voice. The line spoken is "Close the gate." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character in a suit, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. The readout is plain circular geometry only, with nothing written or numbered on it.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```
