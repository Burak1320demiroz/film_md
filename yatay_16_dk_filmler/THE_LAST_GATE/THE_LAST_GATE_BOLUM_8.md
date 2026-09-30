# 🎬 THE_LAST_GATE — BÖLÜM 8  (K85 – K96 · S22 – S25)

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
KURULUM İSKELETİ: L J K L J N A K P A O L
ölçülen DÖNÜŞ: 3/12 — aynı harf = birebir aynı CAMERA satırı
⛔ K01–K04 harf taşımaz: kurgu bloklarıdır, kendi görüntüsü üretilmez.
```
---

# 📍 SAHNE 22 — ÜÇLÜ SON ARAÇTA  (3 klip · 14:00–14:30)

## 🎬 KLİP 85 — S22 · 1/3 · KURULUM — ÜÇÜ İÇERİDE

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso · back
Clip 85 of 96.

The pilot comes into the last transfer pod and the three of them are in one frame with clear space between them: the engineer beside the inner hatch and the tall systems engineer at the right-hand control seat. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap. On the right chest is a textless three-winged pilot badge in embossed embroidery, and on the left upper arm a textless circular survey patch.
LIGHT: Low warm seat lighting and one cold strip above the inner hatch, with a pale glow from the gate field entering through the small window; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 35mm lens on a locked-off camera 2.0 m from the seat row, camera height 1.40 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso · back
Clip 85 of 96.

The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved pod interior frame with the engineer and the tall engineer already aboard.
CAMERA: 35mm lens on a locked-off camera 2.0 m from the seat row, camera height 1.40 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — the pilot pulls herself in through the hatch and takes a handhold, her grip tightening on the rail as the mass comes with her.
3.0-7.0 s — she crosses to the left-hand seat; the other two hold their own places.
7.0-10.0 s — all three are settled with clear space between them and the pod has not moved.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A short easing breath over the pod's own hum. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 86 — S22 · 2/3 · EYLEM — SON HAZIRLIK

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 86 of 96.
CONTINUOUS ACTION: all three are already in their own seats with the inner hatch still open.

Three harness latches close one after another on three separate seats, and the inner hatch of the pod travels shut and seats across the hatchway; the seat order from the front is left, middle and right. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap. On the right chest is a textless three-winged pilot badge in embossed embroidery, and on the left upper arm a textless circular survey patch.
LIGHT: Low warm seat lighting and one cold strip above the inner hatch, with a pale glow from the gate field entering through the small window; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Exactly three harnesses close on exactly three seats and the seat order never changes.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 86 of 96.
CONTINUOUS ACTION: all three are already in their own seats with the inner hatch still open.

START FRAME: the approved macro frame on the seat row with the three harnesses still open.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus.
TIMELINE:
0.0-3.0 s — the inner hatch travels across and seats with one movement.
3.0-7.0 s — the first and second harness latches close on their own seats.
7.0-10.0 s — the third closes and all three stay down; nothing reopens.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Three separate belt latches and one pressure confirmation. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. Exactly three harnesses close on exactly three seats and the seat order never changes.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 87 — S22 · 3/3 · TERSLIK — TAKİPÇİLER SIĞAMAZ

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 87 of 96.
CONTINUOUS ACTION: the pod hatch is already sealed and the pod is still seated in its cradle.

On the gate axis one interceptor comes up on the opening and its own width is plainly greater than what is left of it; the craft breaks off and turns away, and the long command ship is already far outside the frame of the opening. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Low warm seat lighting and one cold strip above the inner hatch, with a pale glow from the gate field entering through the small window; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 24mm lens on a locked-off camera 60 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The pursuing craft turn away because they cannot fit, never by choice — neither one touches the ring.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 87 of 96.
CONTINUOUS ACTION: the pod hatch is already sealed and the pod is still seated in its cradle.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved gate-axis frame with one interceptor closing on the narrowed opening.
CAMERA: 24mm lens on a locked-off camera 60 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the interceptor closes and its profile comes up against the edge.
3.0-7.0 s — the overlap is unmistakable; the craft rolls off the line and turns away.
7.0-10.0 s — it holds that turn away and the opening keeps drawing in.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A withdrawal advisory on the enemy channel, then a command voice with no reply. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The pursuing craft turn away because they cannot fit, never by choice — neither one touches the ring.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 23 — YEREL BIRAKMA  (3 klip · 14:30–15:00)

## 🎬 KLİP 88 — S23 · 1/3 · TERSLIK — UZAKTAN BAĞLANTI KESİLİR

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso · hands
Clip 88 of 96.

Inside the last pod a link indicator goes out and stays out while a four-fingered hand works the handheld unit and gets nothing back; the plain mechanical release lever is in the same frame, within the engineer's reach from her middle seat. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap. On the right chest is a textless three-winged pilot badge in embossed embroidery, and on the left upper arm a textless circular survey patch.
LIGHT: Low warm seat lighting and one cold strip above the inner hatch, with hard sunlight from screen left outside along the rail; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 35mm lens on a locked-off camera 2.0 m from the seat row, camera height 1.40 m, eye-level medium shot, deep focus — the same position, height and lens as Clip 85.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso · hands
Clip 88 of 96.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved pod interior frame with the link indicator still lit and the lever unmoved.
CAMERA: 35mm lens on a locked-off camera 2.0 m from the seat row, camera height 1.40 m, eye-level medium shot, deep focus — the same position, height and lens as Clip 85.
TIMELINE:
0.0-3.0 s — the indicator goes dark and the handheld unit is worked once.
3.0-7.0 s — it is worked again and still nothing comes back; the indicator stays dark.
7.0-10.0 s — the hand comes off the unit and every eye goes to the mechanical lever, her shoulders dropping as the load takes up.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A radio tone cutting off, then a translated adult voice. The line spoken is "Use the local release." and nothing else.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 89 — S23 · 2/3 · KARAR — YEREL BIRAKMA

### 📸 IMAGE PROMPT

```
IN FRAME: hands
Clip 89 of 96.
CONTINUOUS ACTION: the link indicator is already dark and the handheld unit has already failed twice.

From her middle seat the engineer reaches the plain mechanical release lever and pulls it down through its full travel in one movement, and the four pod cradle latch indicators change to their open state. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. Each figure keeps its own station in the frame and no two of them overlap. On the left chest is a textless compass-form survey badge, and on the right upper arm a textless patch with two parallel bars.
LIGHT: Low warm seat lighting and one cold strip above the inner hatch, with hard sunlight from screen left outside along the rail; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus — the same position, height and lens as Clip 86.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. These are the four latches of this pod only, and the outer hatch stays sealed with everyone harnessed.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: hands
Clip 89 of 96.
CONTINUOUS ACTION: the link indicator is already dark and the handheld unit has already failed twice.

START FRAME: the approved macro frame on the lever with all four latch indicators still closed.
CAMERA: 100mm lens on a locked-off camera 0.55 m from the glove, camera height 1.20 m, high-angle extreme close-up, shallow focus — the same position, height and lens as Clip 86.
TIMELINE:
0.0-3.0 s — her glove closes on the lever and takes up the slack in it, her grip tightening on the rail as the mass comes with her.
3.0-7.0 s — the lever comes down through its full travel and stops hard at the end.
7.0-10.0 s — the four latch indicators change to open together and hold there.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A mechanical lever through its travel, then four latch answers. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. These are the four latches of this pod only, and the outer hatch stays sealed with everyone harnessed.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 90 — S23 · 3/3 · SONUC — SON AYRILMA

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 90 of 96.
CONTINUOUS ACTION: the four cradle latches of this pod are already in their open state.

The last transfer pod comes off the rail and runs out along the same open lane on its own thrusters, following the identical centre line the others took; its outer shape is unchanged from the pod berthed at the start. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Low warm seat lighting and one cold strip above the inner hatch, with hard sunlight from screen left outside along the rail; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 32mm lens on a locked-off camera 20 m out along the rail, camera height 0.8 m above the rail line, low-angle wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly one pod separates and the rail it left stays empty afterwards. The pod keeps its full mass as it leaves, with no weightless flick, no sudden jump and no rubbery deflection.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 90 of 96.
CONTINUOUS ACTION: the four cradle latches of this pod are already in their open state.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved rail frame with the last pod still seated and its latches open.
CAMERA: 32mm lens on a locked-off camera 20 m out along the rail, camera height 0.8 m above the rail line, low-angle wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the pod lifts clear of the cradle and its thrusters come up.
3.0-7.0 s — it takes the open lane on the same line as the others.
7.0-10.0 s — it holds that line and rate and the rail it left is empty.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. A thrust vibration from inside the pod, with the score outside it. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Exactly one pod separates and the rail it left stays empty afterwards. The pod keeps its full mass as it leaves, with no weightless flick, no sudden jump and no rubbery deflection.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 24 — GEÇİŞ VE KAPANIŞ  (3 klip · 15:00–15:30)

## 🎬 KLİP 91 — S24 · 1/3 · TERSLIK — TERK EDİLEN GÖVDE

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 91 of 96.

Seen from the aft quarter of the last pod, the damaged aft drive structure of the abandoned hull breaks away in separate rigid pieces on straight paths, while the forward pressurised section stays whole and still holds the line between the pod and the pursuing craft. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Hard sunlight from screen left, a pale even glow from the narrowing gate field filling the centre of the frame, and a copper wash from the banded planet far behind; nothing in frame blooms.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No fireball, no flash and no shockwave — the forward pressurised section stays whole.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 91 of 96.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved wide frame off the pod's aft quarter with the hull still intact aft.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the aft structure parts along one line and the pieces separate.
3.0-7.0 s — each piece goes on in a straight path, turning slowly on its own axis.
7.0-10.0 s — the forward section stays whole and unmoved and keeps blocking the line.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Radio and breathing from inside the pod only; nothing at all is heard from outside. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No fireball, no flash and no shockwave — the forward pressurised section stays whole.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 92 — S24 · 2/3 · DORUK — SON ARAÇ GEÇER

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 92 of 96.
CONTINUOUS ACTION: the last pod is already on the common approach line with the opening still ahead of it.

On the established axis the last transfer pod passes entirely through the narrowed opening — nose, body and aft end — with a thin margin of clear space all round it and no contact of any kind with the field edge. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Hard sunlight from screen left, a pale even glow from the narrowing gate field filling the centre of the frame, and a copper wash from the banded planet far behind; nothing in frame blooms.
CAMERA: 24mm lens on a locked-off camera 60 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The pod never touches the field edge and is never marked or scored by it — the shot holds until the aft end is clear.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 92 of 96.
CONTINUOUS ACTION: the last pod is already on the common approach line with the opening still ahead of it.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved gate-axis frame with the last pod closing on the narrowed opening.
CAMERA: 24mm lens on a locked-off camera 60 m back on the gate axis, camera height on the gate axis, eye-level extreme wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the nose of the pod enters the opening with clear space all round it.
3.0-7.0 s — the body passes through and the margin holds all the way round.
7.0-10.0 s — the aft end clears the edge completely; the shot is not cut until it does.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. Breathing held for a moment, then the thrust note softening. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The pod never touches the field edge and is never marked or scored by it — the shot holds until the aft end is clear.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 93 — S24 · 3/3 · SONUC — GEÇİT KAPANIR

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 93 of 96.
CONTINUOUS ACTION: the last pod has already cleared the opening completely.

On the same circle centre the active opening goes to nothing: the bright edge closes the last of the way in and the whole area is dark, while the fixed outer ring stands exactly as it always did. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: Hard sunlight from screen left, a pale even glow from the narrowing gate field filling the centre of the frame, and a copper wash from the banded planet far behind; nothing in frame blooms.
CAMERA: 50mm lens on a locked-off camera 120 m back on the gate axis, camera height on the gate axis, eye-level wide shot, deep focus.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The opening never reopens in this shot and no craft crosses after it has closed.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 93 of 96.
CONTINUOUS ACTION: the last pod has already cleared the opening completely.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved gate frame with the opening reduced to its smallest and still bright.
CAMERA: 50mm lens on a locked-off camera 120 m back on the gate axis, camera height on the gate axis, eye-level wide shot, deep focus.
TIMELINE:
0.0-3.0 s — the bright edge closes the last of the distance to the centre.
3.0-7.0 s — the area goes dark all at once and stays dark.
7.0-10.0 s — the outer ring holds unchanged; nothing reopens and nothing crosses.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. The radio noise cutting out, then one moment of complete quiet. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. The opening never reopens in this shot and no craft crosses after it has closed.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

# 📍 SAHNE 25 — SELAM  (3 klip · 15:30–16:00)

## 🎬 KLİP 94 — S25 · 1/3 · KURULUM — YENİ GÖKYÜZÜ

### 📸 IMAGE PROMPT

```
IN FRAME: none
Clip 94 of 96.

On the neutral side an enormous pale blue ringed planet stands across the frame with its rings tilted open, and the transfer pods spread out of their line into an even cluster in front of it, each one holding its own shape and spacing. The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.
LIGHT: A broad pale blue wash from the ringed planet filling the frame with cold white cabin light on the near surfaces; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus — the same position, height and lens as Clip 91.

NEGATIVE: Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. This is a different planet with a different colour and ring geometry, never the earlier planet changed.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: none
Clip 94 of 96.

The escape axis runs screen-left to screen-right and the ship's nose points to screen right for the whole film.

START FRAME: the approved final wide frame with the ringed planet across the frame and the pods still in line.
CAMERA: 24mm lens on a locked-off camera 40 m from the hull, camera height on the approach axis, eye-level extreme wide shot, deep focus — the same position, height and lens as Clip 91.
TIMELINE:
0.0-3.0 s — the pods hold their line against the blue limb and the rings.
3.0-7.0 s — they open out of the line into an even cluster, each keeping its own path.
7.0-10.0 s — the cluster holds its spread and nothing closes back up.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. The score resolving for the first time over a low interior fan. No dialogue in this shot.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 0 human characters in frame, no people, no figures, no silhouettes of people. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. This is a different planet with a different colour and ring geometry, never the earlier planet changed.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 95 — S25 · 2/3 · TEPKI — SELAM

### 📸 IMAGE PROMPT

```
IN FRAME: face · hands
Clip 95 of 96.
CONTINUOUS ACTION: the pods have already opened out into their even cluster.

At the window of the first transfer pod the adult crew lead raises one open hand and holds it there, her grey shoulder stripe readable beside her; one other seated adult is visible harnessed in the next seat. The crew lead wears a white pressure suit with a grey shoulder stripe and a short visor frame. The other adults wear the same white main suit with measured blue and grey duty panels and closed helmets. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. The two figures keep separate halves of the frame and never overlap. On the chest is a textless rectangular duty badge in embossed embroidery.
LIGHT: A broad pale blue wash from the ringed planet filling the frame with cold white cabin light on the near surfaces; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 85mm lens on a locked-off camera 1.0 m from the window, camera height 1.35 m, eye-level close-up, shallow focus.

NEGATIVE: Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · hands
Clip 95 of 96.
CONTINUOUS ACTION: the pods have already opened out into their even cluster.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved window frame with the crew lead at the glass and her hand still down.
CAMERA: 85mm lens on a locked-off camera 1.0 m from the window, camera height 1.35 m, eye-level close-up, shallow focus.
TIMELINE:
0.0-3.0 s — she comes to the glass and her helmet turns toward the lens.
3.0-7.0 s — her open hand comes up flat against the window and stops.
7.0-10.0 s — she holds the hand there; the adult in the next seat stays seated and harnessed.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. No dialogue at all, only a soft radio carrier under the score.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 2 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```

## 🎬 KLİP 96 — S25 · 3/3 · FINAL — KARŞILIK

### 📸 IMAGE PROMPT

```
IN FRAME: face · torso · hands
Clip 96 of 96.
CONTINUOUS ACTION: the crew lead's open hand is already up at the window of the other pod.

In the last pod the pilot raises one open hand in answer; the engineer sits in the middle seat and the tall systems engineer in the right-hand seat, and the rings of the pale blue planet show as a thin curve reflected across all three clear visors. The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt. The visor is optically clear glass with zero tint, the face fully readable through it at every head angle. A single diagonal scuff runs across the outer plate of the pilot's left forearm. Each figure keeps its own station in the frame and no two of them overlap. On the right chest is a textless three-winged pilot badge in embossed embroidery, and on the left upper arm a textless circular survey patch.
LIGHT: A broad pale blue wash from the ringed planet filling the frame with cold white cabin light on the near surfaces; faces stay readable behind the clear visors and no surface blooms.
CAMERA: 35mm lens on a locked-off camera 2.0 m from the seat row, camera height 1.40 m, eye-level medium shot, deep focus.

NEGATIVE: Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. No title card, no end card, no logo, no credit roll and no closing plate appears at any point in this shot, and the image holds to the last frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT

```
IN FRAME: face · torso · hands
Clip 96 of 96.
CONTINUOUS ACTION: the crew lead's open hand is already up at the window of the other pod.

The visor is optically clear glass with zero tint, the face fully readable through it at every head angle.

START FRAME: the approved pod interior frame with all three harnessed and the pilot's hand still down.
CAMERA: 35mm lens on a locked-off camera 2.0 m from the seat row, camera height 1.40 m, eye-level medium shot, deep focus.
TIMELINE:
0.0-3.0 s — she sees the raised hand through the window and her own hand starts up.
3.0-7.0 s — her open hand comes up flat and holds; the other two stay in their seats.
7.0-10.0 s — nothing else moves for the last stretch of the shot and the hand stays up.
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet. No dialogue at all, only breathing and the resolved score.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly 3 human characters in suits, and exactly one tall figure with two arms, two legs and one head, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or numerals on any surface in frame — every badge and patch is textless — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated microgravity with continuous one-way momentum, never stopping in mid-air, never swirling like liquid, structures static, no melting or warping. No title card, no end card, no logo, no credit roll and no closing plate appears at any point in this shot, and the image holds to the last frame.

Output: 16:9, 4K, 10 seconds, no text, no watermark.
```
