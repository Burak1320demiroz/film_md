# 🔋 LOW POWER — Düşük Güç | PART B

## AI Production Bible — Self-Contained Prompts
### PART B: Sahne 13-24 (12 sahne) | 16:9 Yatay | Görsel + Video + Diyalog + Müzik
### _"Bir şeyin yaşaması için senin yaşaman gerekmiyor."_

> **PART B süresi:** 12 sahne × 10s = 120 saniye (2:09 – 4:09)
> **Bible'lar:** `LOW_POWER_PART_A.md` — World, Station, Character, Camera,
> Lighting, Physics, Negative. Tekrar yazılmadı; promptlar yine self-contained.

---

## 🔗 PART A'DAN DEVREDEN DURUMLAR

Bu 5 durum Part B boyunca korunur. Her sahne promptunda ilgili olan tekrarlanır.

```
1. ANAHTAR:        SOL konumda. S20'ye kadar çevrilmez.
2. BORDO CEKET:    Üzerinde. S21'de suit altına giriyor, çıkarılmıyor.
3. SERA SARARMASI: 4 sıra ölü. S16'da 4 → 9 sıraya büyüyor.
4. TOHUM KASASI:   Alt rafta, mühürlü. S22'de etiketlenip yerine konuyor.
5. NEFES BUĞUSU:   Hab soğuyor. Her sahnede biraz daha belirgin.
                   S13'te zar zor → S21'de her nefeste net.
```

**PART A SON KARESİ:** Dim amber ışıkta dokunulmamış metal anahtar, el kadraj dışında.
**PART B İLK KARESİ:** Karanlık koridor, sera kapısının altından sızan yeşil çizgi.
**KÖPRÜ:** Işık geçişi — amber (2400K) → yeşil.

---

## ⚡ IŞIK DÜŞÜŞ TABLOSU (Part B'nin görsel saati)

```
S13-S19   Tavan panelleri ÇOK LOŞ. Acil amber işaret ışıkları devrede.
S20       ANAHTAR ÇEVRİLİR. Tavan panelleri SÖNER.
S21-S24   Hab KARANLIK. Tek ışık kaynakları: acil kırmızı şerit,
          Selin'in kask lambası, ve sera kapısından sızan YEŞİL.
          Sera ise hiç kısılmaz — tam güçte, parlak, canlı.
```

> Filmin görsel argümanı budur: insan kararırken bitki aydınlık kalır.

---

# 🎬 PROMPTLAR (S13-S24)

---

## 🎬 SAHNE 13 (S13) — KARANLIK

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
corridor. EXACTLY ONE human character in frame.

SCENE:
A woman stands in a corridor where the lights have failed, facing a closed
hatch with a single line of green light glowing beneath it.

ENVIRONMENT:
The living module corridor of a small Mars station — narrow, exactly 1.4
meters wide, low 2.1 meter ceiling crossed by exposed pipes and cable runs,
walls of scuffed pale grey-white composite panels with fine red dust in
every seam. The ceiling LED panels are almost entirely OFF — only a faint
residual grey glow remains. Two small AMBER emergency indicator lamps are
set low on the walls, casting weak pools near the floor. At the far end of
the corridor: a CLOSED HATCH, and beneath it, spilling out across the deck
in a hard bright bar, a LINE OF GREEN LIGHT roughly 4cm tall — the only
saturated colour in the frame, coming from the greenhouse on the other
side. Twelve sleeping berth curtains line the walls, all drawn, all dark.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m, lean with visible muscle loss; warm
light-brown skin with visible pore texture and an indoor pallor; broad
forehead, defined jawline, dark brown eyes with deep fatigue lines
beneath, thick natural eyebrows, thin cracked lips, an old 3cm burn scar
on the back of her left hand; dark brown hair going grey at the temples,
cut short and pulled back, unwashed; no makeup, no airbrushing).
EQUIPMENT STATE: NO helmet, NO suit, NO gloves — indoors and unsuited. She
wears a faded grey-beige thermal coverall with a faded abstract mission
patch and an old worn MAROON FLEECE JACKET, a thin cord and small metal tag
at her neck. She stands in the middle of the dark corridor, seen from
behind and slightly to the side, small in frame, facing the closed hatch.
Her arms hang at her sides. The green bar of light from under the hatch
lights her shoes and the bottom of her trousers; the rest of her is in
near-darkness, edged faintly by the amber floor lamps.

CAMERA:
50mm, f/2.0, ISO 3200, camera fixed at approximately 3 meters behind her
at chest height, centred in the corridor for one-point perspective.
Moderate depth of field — she and the hatch both readable. Physically
accurate perspective, correct architectural proportions.

LIGHTING:
Three motivated sources, all weak. (1) The GREEN LIGHT BAR under the hatch
(the greenhouse LEDs beyond it) — a hard, bright, sharply defined strip
across the deck, the brightest and only saturated element. (2) Two small
AMBER emergency lamps (2200K) low on the walls, weak pools near the floor.
(3) Faint residual grey from the nearly-dead ceiling panels. Extremely
low-key, most of the frame in deep shadow. Skin retains pore texture where
lit. 0% bloom, no glow filter, no light haze in the air.

PHYSICS:
0.38g. Pressurized interior, COLD — her breath is faintly visible as
vapour. She stands with real weight. Clothing hangs naturally. Settled red
dust remains in the seams.

NEGATIVE:
No bloom, no glow filter, no soft focus, no volumetric light shafts or
god rays from under the hatch — the green light is a hard defined bar on
the floor, not a beam in the air. No airbrushed skin, no plastic or waxy
texture, no smoothed skin. No face morphing. EXACTLY ONE human — no
duplicates, no clones, no second person, no figure behind any curtain. NO
READABLE TEXT, letters, digits or symbols on any surface. Green appears
ONLY as the light bar from the greenhouse — nowhere else in frame. No
ceiling lights turning back on. No equipment appearing — no helmet, no
suit, no gloves. No floating objects. Corridor locked at 1.4 meters wide
and 2.1 meters high. Static stable environment. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat corridor. No dialogue. Exactly one human
character.

A woman stands alone in a dark corridor, looking at the only light left in
the station — a green line under a closed door.

0s — Fixed lockoff, 50mm, f/2.0, camera at 3 meters behind her at chest
height, centred in the corridor. A 44-YEAR-OLD WOMAN (warm light-brown
skin with visible pore texture and an indoor pallor, broad forehead,
defined jawline, dark brown eyes with deep fatigue lines beneath, thick
eyebrows, thin cracked lips, dark brown hair going grey at the temples,
cut short and pulled back) stands in the middle of a narrow corridor,
1.4 meters wide with a 2.1 meter ceiling, seen from behind and small in
frame. EQUIPMENT STATE: NO helmet, NO suit, NO gloves at 0s and for the
entire take. She wears a faded grey-beige thermal coverall and an old worn
MAROON FLEECE JACKET, a thin cord and metal tag at her neck. The ceiling
panels are almost entirely dead — only faint residual grey. Two small
AMBER emergency lamps sit low on the walls. At the far end, beneath a
closed hatch, a hard bright BAR OF GREEN LIGHT about 4cm tall spills
across the deck — the only saturated colour anywhere.

3s — She exhales. Her breath condenses into clearly visible vapour that
drifts a short distance and dissipates. She does not move otherwise.

6s — She takes two slow, grounded, weighted steps toward the hatch,
slightly lighter than an Earth stride but fully in contact with the deck.
The green bar grows marginally wider in frame as she approaches. The dark
berth curtains pass on either side.

8s — She stops a metre short of the hatch. The green light now reaches her
knees. She does not reach for the handle.

10s — She stands still, facing the closed hatch and its line of green
light. Camera never moves. No cuts.

Audio: A low, struggling fan hum, quieter and less steady than earlier —
the system is under-powered. An irregular heater tick with long gaps. Her
two soft footfalls on the deck. Her single audible exhale at 3 seconds.
Very faintly beneath: a thin distant hiss of sand against the hull. No
music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person,
no figure behind any curtain. 0% bloom, no glow filter, no soft focus, no
volumetric light shafts or god rays under the hatch — the green light stays
a hard defined bar on the floor, never a beam in the air. Photorealistic
skin pores, fatigue lines and cracked lips retained — no airbrushing, no
plastic texture, no smoothed or waxy skin, no face morphing. Clothing
identical to the description — the maroon jacket stays on. NO EQUIPMENT
APPEARING — no helmet, no suit, no gloves materialize at any point. NO
READABLE TEXT, letters, digits or symbols on any surface. Green appears
ONLY as the light bar from the greenhouse and nowhere else. THE CEILING
LIGHTS DO NOT COME BACK ON and the hatch does NOT open. 0.38g walking —
grounded contact steps with weight, no floating, no gliding, no bouncing,
no moonwalking. Corridor width locked at 1.4 meters, ceiling at 2.1 meters
— no proportion drift. Settled dust stays settled. Static stable
environment. No text overlay, no title card, no end card, no credits, no
watermark, no subtitles. No CGI aesthetic, no Unreal Engine look, no video
game aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 14 (S14) — VİRAL ARA #2: MAVİ GÜN BATIMI

> 🏆 **FİLMİN İMZA KARESİ.** Kapak fotoğrafı adayı. Doğrulanmış bilim:
> Mars'ta gökyüzü gündüz kahve-tarçın, gün batımında güneşin çevresi MAVİ olur.
> Toz kırmızı ışığı saçar, mavi ışık doğrudan geçer — Dünya'nın tam tersi.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars surface at
sunset. EXACTLY ONE human character in frame.

SCENE:
A suited figure stands alone on the Martian surface watching the sun set —
and around that sun, the sky is BLUE.

ENVIRONMENT:
The Martian surface outside a small station at sunset, during a dust storm.
The ground is red-brown regolith with scattered angular basalt pebbles,
fading into brown haze within a hundred meters. The sky occupies the upper
two thirds of the frame and it is divided by a real optical phenomenon:
across most of the sky the colour is BUTTERSCOTCH BROWN, dark caramel-tan,
heavy with suspended dust — but immediately AROUND AND ABOVE THE SETTING
SUN, in a soft circular region roughly 25 degrees across, the sky turns a
distinct COOL DESATURATED BLUE-GREY, deepening toward slate blue nearest
the sun. The transition between the brown sky and the blue halo is gradual
and smooth, not a hard edge. The SUN itself sits low on the horizon as a
small, PALE WHITE-BLUE DISC with soft indistinct edges, about two thirds
the apparent size it would have from Earth, dimmed by dust. The blue
region is the brightest part of the sky. In the mid-distance, low and
dark: the half-buried pale modules of the station and the dust-covered
solar field, silhouetted.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m; warm light-brown skin with visible pore
texture and an indoor pallor; broad forehead, defined jawline, dark brown
eyes with deep fatigue lines beneath, thick eyebrows, thin cracked lips;
dark brown hair going grey at the temples, cut short and pulled back; no
makeup, no airbrushing). EQUIPMENT STATE: helmet worn and sealed, gloves
on, suit fully closed — all already in place and unchanged. She wears a
dirty WHITE-BEIGE surface EVA suit with faded ORANGE accent bands at
shoulders, elbows and waist, KNEES AND GLOVES permanently stained
rust-red, three abstract chest indicators with no text, a compact
white-beige back unit with orange banding, and an integrated helmet with a
FULLY TRANSPARENT SEAMLESS VISOR revealing her whole face. She stands in
the lower left third of frame, SMALL — occupying about one sixth of the
frame height — seen from behind and slightly to the side, arms at her
sides, completely still, facing the setting sun. Her helmet is tilted very
slightly upward. Her face is partly readable in profile through the clear
visor: eyes open, mouth relaxed. The blue light from the sky falls on the
front of her white suit; the brown sky light falls on her back.

CAMERA:
32mm Cooke anamorphic, f/4, ISO 400, camera fixed at approximately 12
meters behind and to her left, at 1.5 meters height, composing her small
against the vast divided sky. Deep focus — figure, station silhouette and
sky all sharp. Physically accurate perspective, realistic scale — one
1.68m human against a horizon.

LIGHTING:
One motivated source with two colour behaviours, both physically real.
(1) The setting sun, low, as a pale WHITE-BLUE disc — its direct light is
cool and desaturated, falling on the front of her suit and picking out a
cool rim along her helmet and shoulder. (2) The surrounding BROWN SKY
acting as a wide warm ambient fill from every other direction, casting a
dull red-brown wash on the ground and on her back. Shadows are WEAK and
SOFT-EDGED — dust scatters light from all directions — and stretch long
across the regolith away from the sun. Low contrast, moderate saturation
only in the blue region. 0% bloom, no glow filter, no lens flare, no sun
star, no god rays.

PHYSICS:
0.38g. Atmospheric pressure 0.6% of Earth's — far too thin to move
anything. NOTHING flaps, nothing is blown, no fabric ripples, no dust is
driven horizontally past her. Suspended dust drifts slowly and settles
downward. The pressurized suit is rigid. She stands with real weight.

NEGATIVE:
NO EARTH SUNSET — the sky near the sun is BLUE and the rest of the sky is
BROWN; this is the reverse of Earth and must not be inverted. No orange or
red sunset glow around the sun, no pink clouds, no golden hour warmth near
the sun. No blue sky away from the sun. No clouds of any kind. No bloom,
no glow filter, no lens flare, no sun star, no god rays, no light shafts.
No violent wind, no flapping suit fabric, no flying debris, no horizontal
dust streaks. No green anywhere. EXACTLY ONE human — no duplicates, no
clones, no second person. No readable text, letters, digits or symbols on
any surface. No rising or floating dust — dust settles downward. Visor
always visible and fully transparent, face readable through it. No
equipment appearing or disappearing, no helmet materializing. Static
stable terrain. Not miniature, not toy-like. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look. Photorealistic with 35mm anamorphic
film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars surface at sunset. No dialogue. Exactly one human
character. THE FILM'S SIGNATURE SHOT.

A suited figure stands still on Mars and watches a sunset where the sky
around the sun turns blue.

0s — Fixed lockoff, 32mm Cooke anamorphic, camera at 12 meters behind and
to her left, 1.5 meters height. A 44-YEAR-OLD WOMAN (warm light-brown skin
with visible pore texture, broad forehead, defined jawline, dark brown eyes
with deep fatigue lines beneath, thick eyebrows, thin cracked lips, dark
brown hair going grey at the temples, cut short and pulled back) stands
SMALL in the lower left third of frame, about one sixth of the frame
height, seen from behind, arms at her sides, facing the horizon.
EQUIPMENT STATE: helmet worn and sealed at 0s and for the entire take,
gloves on, suit closed — nothing is put on or removed. She wears a dirty
WHITE-BEIGE surface EVA suit with faded ORANGE accent bands, KNEES AND
GLOVES permanently stained rust-red, a compact back unit with orange
banding, and an integrated helmet with a FULLY TRANSPARENT SEAMLESS VISOR
revealing her face in profile. The sky fills the upper two thirds: mostly
BUTTERSCOTCH BROWN, dark caramel-tan, thick with dust — but around the low
setting sun, a soft circular region about 25 degrees across is COOL
DESATURATED BLUE-GREY, deepening to slate blue nearest the sun, blending
gradually into the brown with no hard edge. The sun is a small PALE
WHITE-BLUE DISC with soft edges. The dark half-buried station and buried
solar field sit silhouetted in the mid-distance.

3s — The sun descends very slightly toward the horizon. The blue region
around it deepens and contracts marginally, the brown of the surrounding
sky darkening. The long weak shadows across the regolith lengthen a little
further away from the sun. Nothing else in the frame moves.

6s — She tilts her helmet up a few degrees, following the sun. The
movement is small, slow and entirely deliberate. Cool blue light shifts
across the front of her white suit and along the rim of her helmet. Her
face stays readable in profile through the clear visor.

8s — She lowers her arms fully and settles, standing completely still.
Suspended dust drifts slowly downward across the frame.

10s — The small figure, the divided sky, the blue sun. Camera never moves.
No cuts.

Audio: Her breathing inside the helmet, close, slow and steady — the
dominant sound and almost the only one. Beneath it a very faint, thin,
MUFFLED hiss of suspended sand, low and distant with high frequencies
absent. No wind howl, no roar, no music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person.
NO EARTH SUNSET — the sky immediately around the sun is BLUE and the rest
of the sky is BROWN, and this relationship must never invert: no orange or
red glow around the sun, no pink clouds, no golden warmth near the sun, no
blue sky away from the sun, no clouds of any kind. No bloom, no glow
filter, no lens flare, no sun star, no god rays, no light shafts. NO
VIOLENT WIND — the atmosphere is 0.6% of Earth's: no flapping or rippling
suit fabric, no flying debris, no horizontal dust streaking past her, no
figure bracing. All suspended dust drifts slowly DOWNWARD under 0.38g and
settles — no rising dust, no hovering particles, no anti-gravity behavior,
no frame-rate variance on particle motion. No green anywhere.
Photorealistic skin retained through the clear visor — no airbrushing, no
plastic texture, no smoothed skin, no face morphing. Visor ALWAYS visible,
fully transparent, no tint, no HUD graphics, no invented reflections. Suit
detail identical to the description — rust-red knee and glove staining
stays. NO EQUIPMENT APPEARING OR DISAPPEARING, no helmet materializing, no
gear state change mid-shot. No readable text, letters, digits or symbols on
any surface. Static stable terrain — no melting, warping or swimming
ground. Not miniature, not toy-like — she reads as exactly 1.68m against
the horizon. No text overlay, no title card, no end card, no credits, no
watermark, no subtitles. No CGI aesthetic, no Unreal Engine look, no video
game aesthetic. Photorealistic with 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 15 (S15) — BORDO CEKET

> ⚠️ **TASARIM NOTU:** Planda "yakasında başka birinin adı" yazıyordu.
> Ders 13 (metin yasağı) nedeniyle bu, **farklı bir işleme amblemle**
> çözüldü: ceketin yakasındaki amblem, Selin'in kendi tulumundakinden
> FARKLI bir şekil. Harf yok, ama ceketin ona ait olmadığı anlaşılıyor.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
sleeping berth. EXACTLY ONE human character in frame.

SCENE:
A woman sits on a bunk holding the collar of the maroon jacket she is
wearing, looking at an embroidered insignia that is not hers.

ENVIRONMENT:
A sleeping berth in the living module — a tight recess barely wider than a
single bunk, low ceiling with exposed pipes, walls of scuffed pale
grey-white composite panels with fine red dust in the seams. The privacy
curtain is drawn behind her. A small warm amber reading lamp is clipped
beside the bunk, the only light source. The bunk mattress is thin and
worn. Beside her on the blanket, folded: nothing else — the berth is
almost bare.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m, lean with visible muscle loss; warm
light-brown skin with visible pore texture and an indoor pallor; broad
forehead, defined jawline, dark brown eyes with deep fatigue lines
beneath, thick natural eyebrows, thin cracked lips, an old 3cm burn scar
on the back of her left hand; dark brown hair going grey at the temples,
cut short and pulled back, unwashed; no makeup, no airbrushing).
EQUIPMENT STATE: NO helmet, NO suit, NO gloves — indoors and unsuited. She
sits on the edge of the bunk, shoulders forward, wearing a faded grey-beige
thermal coverall and, over it, the old worn MAROON FLEECE JACKET, clearly
slightly too large for her — the shoulders sit wide, the cuffs reach past
her wrists. On her COVERALL CHEST: a faded abstract mission patch, a
simple rounded shape. On the COLLAR OF THE MAROON JACKET, turned up
between her fingers: a small embroidered insignia of a CLEARLY DIFFERENT
SHAPE — angular where hers is rounded — worn and frayed at the edges. NO
letters, NO text, NO numbers on either insignia; they are abstract
embroidered shapes only, and the difference between them is purely
geometric. She holds the collar with both hands, thumbs on the insignia,
head bent to look at it. Her expression is quiet and closed.

CAMERA:
85mm, f/2.0, ISO 2000, camera fixed at approximately 1 meter, slightly
high angle, framing her bent head, her hands and the turned-up collar
insignia together. Shallow depth of field — the insignia and her hands
razor-sharp, her face slightly soft above, the berth soft behind.

LIGHTING:
One motivated source: the small warm amber reading lamp (2700K) clipped
beside the bunk, close, low and directional — it lights her hands and the
collar insignia hard from the side and leaves most of her face and the
berth in deep shadow. A very faint cool grey residual spill from the
corridor edges the far side of her shoulder. Extremely low-key. Skin
retains full pore and fatigue texture where lit. 0% bloom, no glow filter.

PHYSICS:
0.38g. Cold, pressurized interior — her breath is faintly visible. The
fleece fabric is soft and creases naturally under her fingers with real
compression. Her hands contact the collar with a clear structural
boundary. Clothing hangs under gravity.

NEGATIVE:
No bloom, no glow filter, no soft focus. No airbrushed skin, no plastic or
waxy texture, no smoothed skin — pore texture, fatigue lines, cracked lips
and the burn scar remain visible. No face morphing. EXACTLY ONE human — no
duplicates, no clones, no second person, no photograph of a person, no
portrait, no face on any surface. NO READABLE TEXT, letters, digits,
numbers, names or symbols on either insignia, on the patch, or on any
surface — both insignia are abstract embroidered shapes and differ only in
geometry. No green anywhere. No hand-fabric merging, no phasing, no extra
fingers. No equipment appearing — no helmet, no suit, no gloves. No
floating objects. Static stable environment. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat sleeping berth. No dialogue. Exactly one
human character.

A woman turns up the collar of a jacket she is wearing, looks at an
insignia that does not match her own, and lets it fall.

0s — Fixed lockoff, 85mm, f/2.0, camera at 1 meter, slightly high angle,
shallow depth of field. A 44-YEAR-OLD WOMAN (warm light-brown skin with
visible pore texture and an indoor pallor, broad forehead, defined
jawline, dark brown eyes with deep fatigue lines beneath, thick eyebrows,
thin cracked lips, an old burn scar on the back of her left hand, dark
brown hair going grey at the temples, cut short and pulled back) sits on
the edge of a bunk in a tight sleeping berth, shoulders forward.
EQUIPMENT STATE: NO helmet, NO suit, NO gloves at 0s and for the entire
take. She wears a faded grey-beige thermal coverall with a faded ROUNDED
abstract patch on the chest, and over it an old worn MAROON FLEECE JACKET
that is clearly too large — wide shoulders, cuffs past her wrists. A small
warm amber reading lamp beside the bunk is the only light. The drawn
privacy curtain is behind her.

2s — She raises both hands and turns up the collar of the maroon jacket
between her fingers, the fleece creasing with real compression under her
thumbs. A small embroidered insignia on the collar comes into the amber
light: an ANGULAR shape, worn and frayed — clearly a different geometry
from the rounded patch on her own chest. No letters, no text on either.

5s — She holds the collar still and looks at the insignia, her head bent,
her thumbs resting on it. She does not speak. Her breath is faintly
visible in the cold air.

7s — She closes her eyes for about one second, then opens them.

9s — She lets the collar go. The fleece falls back into place and the
insignia turns away out of the light.

10s — She sits still, hands in her lap, looking at nothing. Camera never
moves. No cuts.

Audio: A low, struggling fan hum and an irregular heater tick with long
gaps. The soft dry rustle of fleece fabric as she turns the collar and
releases it. Her breathing, quiet and close. No music. No dialogue. No
subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person,
NO photograph of a person, no portrait, no face appearing on any surface,
no flashback, no other figure. 0% bloom, no glow filter, no soft focus —
the amber lamp is sharp and directional with clear falloff and deep
shadows. Photorealistic skin pores, fatigue lines, cracked lips and the
burn scar retained — no airbrushing, no plastic texture, no smoothed or
waxy skin, no face morphing. NO READABLE TEXT, letters, digits, numbers,
names or symbols on either insignia, the patch, or any surface — both
insignia stay abstract embroidered shapes differing only in geometry, and
neither changes shape during the shot. No green anywhere. NO EQUIPMENT
APPEARING — no helmet, no suit, no gloves materialize. Her hands keep clear
structural contact with the fleece — no hand-fabric merging, no phasing,
no extra fingers. Fabric creases and falls under 0.38g with real weight —
nothing floats. Clothing identical to the description — the maroon jacket
stays on her body throughout and is never removed. Static stable
environment. No text overlay, no title card, no end card, no credits, no
watermark, no subtitles. No CGI aesthetic, no Unreal Engine look, no video
game aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 16 (S16) — ÖLÜM

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
greenhouse. EXACTLY ONE human character in frame.

SCENE:
A woman stands before a hydroponic rack where nine rows of plants have
died, her hand resting on a yellowed leaf.

ENVIRONMENT:
The greenhouse module of a small Mars station, 6 by 4 meters. Four tiers
of vertical hydroponic racks line both walls. Most rows are still dense
and green — lettuce, climbing beans, dwarf wheat — lit from beneath each
shelf by sharp, defined MAGENTA-WHITE LED strips whose light bounces off
the foliage so the room reads GREEN. But on the upper rack directly before
her, a section of NINE ROWS is DEAD: leaves collapsed, dry, and turned a
pale sickly YELLOW-BROWN, stems drooping over the tray edge, the nutrient
channel behind them empty and dry with a white mineral crust. The
boundary between the dead section and the living rows beside it is sharp
and obvious. Below, on the lowest shelf, sits a plain sealed grey metal
SEED CASE, 30 by 20 cm, unmarked. The air is warm and faintly humid.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m, lean with visible muscle loss; warm
light-brown skin with visible pore texture and an indoor pallor; broad
forehead, defined jawline, dark brown eyes with deep fatigue lines
beneath, thick natural eyebrows, thin cracked lips, an old 3cm burn scar
on the back of her left hand; dark brown hair going grey at the temples,
cut short and pulled back, unwashed; no makeup, no airbrushing).
EQUIPMENT STATE: NO helmet, NO suit, NO gloves — bare hands, indoors. She
wears a faded grey-beige thermal coverall and an old worn MAROON FLEECE
JACKET, a thin cord and metal tag at her neck. She stands facing the dead
section in three-quarter view, close to the rack. Her BARE RIGHT HAND is
raised and her fingers rest under one collapsed yellow-brown leaf,
supporting it from below rather than gripping it — the leaf lies across her
fingers, dry and limp. Her face is lit green from the living rows to her
left and pale yellow-brown from the dead section ahead. Her expression is
still and absorbed, without drama.

CAMERA:
50mm, f/2.0, ISO 800, camera fixed at approximately 1.6 meters, chest
height, framing her face and the dead rack section together with living
green foliage filling the left edge of frame. Shallow depth of field — her
face, hand and the dead leaves sharp; the far racks soft.

LIGHTING:
Two motivated sources, both from the LED strips. (1) The MAGENTA-WHITE LED
strip under the shelf holding the dead rows — sharp and defined, raking
across the dry collapsed leaves and picking out their brittle texture,
reading pale yellow-brown. (2) The strips under the living rows to her
left, bouncing off dense foliage into a strong GREEN fill on that side of
her face and jacket. The colour split across her face — green on one side,
dead yellow-brown on the other — is the point of the image. 0% bloom, no
glow filter, only real humidity in the air.

PHYSICS:
0.38g. Warm, humid, pressurized. The dead leaf is dry, brittle and stiff —
it rests across her fingers without draping like fresh foliage would. Her
fingers contact it with a clear structural boundary and the leaf bends
slightly under its own weight where unsupported. Living leaves hang and
curve naturally under gravity. Nothing floats.

NEGATIVE:
No bloom, no glow filter, no soft focus glow — LED strips are sharp
defined lines, not halos. No airbrushed skin, no plastic or waxy texture,
no smoothed skin — pore texture, fatigue lines, cracked lips and the burn
scar remain visible. No face morphing. EXACTLY ONE human — no duplicates,
no clones, no second person. NO READABLE TEXT, letters, digits or symbols
on the seed case, trays, patch or any surface. No hand-leaf merging, no
phasing, no extra fingers — the dry leaf rests ON her fingers with a clear
boundary. No equipment appearing — no helmet, no suit, no gloves. NO
REVIVING PLANTS — the dead section stays dead and yellow-brown, and does
not green, grow or move. No floating leaves or droplets. Green appears
only inside this room. Static stable environment — no morphing foliage, no
swimming texture. No text overlay, no title card, no end card, no credits,
no watermark, no subtitles. No CGI aesthetic, no Unreal Engine look.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat greenhouse. No dialogue. Exactly one
human character.

A woman holds a dead leaf on a rack where nine rows have failed, and lets
it go.

0s — Fixed lockoff, 50mm, f/2.0, camera at 1.6 meters, chest height. A
44-YEAR-OLD WOMAN (warm light-brown skin with visible pore texture and an
indoor pallor, broad forehead, defined jawline, dark brown eyes with deep
fatigue lines beneath, thick eyebrows, thin cracked lips, an old burn scar
on the back of her left hand, dark brown hair going grey at the temples,
cut short and pulled back) stands close to a hydroponic rack in a warm
green greenhouse. EQUIPMENT STATE: NO helmet, NO suit, NO gloves at 0s and
for the entire take — bare hands. She wears a faded grey-beige thermal
coverall and an old worn MAROON FLEECE JACKET. To her left, dense living
green foliage under sharp MAGENTA-WHITE LED strips fills the frame edge.
Directly before her, on the upper rack, a section of NINE ROWS is DEAD —
leaves collapsed, dry, pale yellow-brown, stems drooping over the tray
edge, the channel behind them dry with white mineral crust. The boundary
between dead and living is sharp. Her face is lit green on one side and
pale yellow-brown on the other.

2s — She raises her bare right hand and slides her fingers UNDER one
collapsed yellow-brown leaf, supporting it from below without gripping.
The dry leaf rests across her fingers, stiff and brittle, bending slightly
under its own weight where unsupported.

5s — She holds it there, unmoving, looking at it. Her expression stays
still and absorbed, without drama. The living rows beside her are
motionless.

8s — She withdraws her fingers slowly. The dead leaf drops back against
the tray edge and settles — falling downward at roughly two and a half
times slower than on Earth, but unmistakably falling, and coming to rest.

10s — She stands looking at the dead section, hand back at her side.
Camera never moves. No cuts.

Audio: A soft continuous water circulation hum and the faint trickle of
nutrient solution through plastic channels. A gentle electrical hum from
the LED strips. The dry papery rustle of the brittle leaf as she supports
it and as it drops. Her breathing, quiet and slow. No music. No dialogue.
No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person.
0% bloom, no glow filter, no soft focus glow — the LED strips stay sharp
defined lines of light, never halos; only real humidity haze is present.
Photorealistic skin pores, fatigue lines, cracked lips and the burn scar
retained — no airbrushing, no plastic texture, no smoothed or waxy skin,
no face morphing. Clothing identical to the description — the maroon
jacket stays on. NO EQUIPMENT APPEARING — no helmet, no suit, no gloves
materialize. NO READABLE TEXT, letters, digits or symbols on the seed case,
trays, patch or any surface. NO REVIVING PLANTS — the nine dead rows stay
dead, dry and yellow-brown for the entire take and never green, grow,
straighten or move on their own; the living rows stay still. Her fingers
keep clear structural contact with the leaf — no hand-leaf merging, no
phasing, no extra fingers, no leaf passing through skin. 0.38g — the leaf
falls downward and comes to rest, living leaves hang under gravity,
nothing floats or hovers. Green appears only inside this room. Static
stable environment — no morphing foliage, no swimming texture. No text
overlay, no title card, no end card, no credits, no watermark, no
subtitles. No CGI aesthetic, no Unreal Engine look, no video game
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 17 (S17) — TOZ ŞEYTANI

> 🔬 **GERÇEK BİLİM:** Mars'ta geçen toz şeytanları güneş panellerini
> kısmen temizler. Bu "temizlik olayı" (cleaning event) Opportunity'ye
> yıllar kazandırdı. Filmde YANLIŞ UMUT beati olarak kullanılıyor —
> gerçekten olur, ama yetmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars solar
field. EXACTLY ONE human character in frame.

SCENE:
A narrow dust devil crosses the solar field behind a suited figure,
sweeping one row of panels partly clean.

ENVIRONMENT:
The solar field of a small Mars station: forty panels in a 5-by-8 grid,
each 1.6 by 1.0 meters, on low frames above red-brown regolith, all buried
under uniform red dust. Crossing the field diagonally in the mid-distance,
roughly 30 meters behind the figure: a DUST DEVIL — a narrow, tall,
vertical column of lifted red dust, about 3 meters wide at its base and
rising some 25 meters, leaning slightly, its edges soft but its column
form clearly defined and coherent, NOT a wall and NOT a wide storm front.
Where it has already passed, along ONE ROW of panels, the dust is
noticeably THINNER — those panels read darker and slightly mottled
compared to the uniform red of the rest, though still far from clean. The
sky is BUTTERSCOTCH BROWN, dark caramel-tan, thick with suspended dust,
NEVER blue. The sun is a dull pale orange disc, low and left, dimmed to a
smudge.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m; warm light-brown skin with visible pore
texture and an indoor pallor; broad forehead, defined jawline, dark brown
eyes with deep fatigue lines beneath, thick eyebrows, thin cracked lips;
dark brown hair going grey at the temples, cut short and pulled back).
EQUIPMENT STATE: helmet worn and sealed, gloves on, suit fully closed —
all already in place and unchanged. She wears a dirty WHITE-BEIGE surface
EVA suit with faded ORANGE accent bands, KNEES AND GLOVES permanently
stained rust-red, three abstract chest indicators with no text, a compact
back unit with orange banding, and an integrated helmet with a FULLY
TRANSPARENT SEAMLESS VISOR. She stands in the foreground, turned to watch
the dust devil, her body half-turned toward camera so her face is clearly
readable through the visor. Her expression is the sharpest it has been in
the film: alert, leaning slightly forward, genuinely hopeful for the first
time — mouth slightly open, eyes wide and tracking.

CAMERA:
32mm Cooke anamorphic, f/4, ISO 500, camera fixed at approximately 8
meters, at 1.5 meters height, composing her in the left foreground with
the dust devil and the partly cleared panel row behind her on the right.
Deep focus — figure, panels and dust column all readable.

LIGHTING:
A single motivated source: the storm-dimmed sun (3400K), low and left,
heavily diffused. Shadows WEAK and SOFT-EDGED. A red-brown ambient cast
over everything. The partly cleared panel row is slightly DARKER than the
dust-covered ones around it, not brighter — it absorbs rather than
reflects under this dim scattered light. Low saturation, low contrast.
0% bloom, no glow filter, no lens flare.

PHYSICS:
0.38g. Atmospheric pressure 0.6% of Earth's. The dust devil is a genuine
convective vortex — it lifts fine dust in a coherent rotating column, but
it does NOT knock anything over, does NOT push the figure, does NOT tear
at her suit and does NOT produce a shockwave. The lifted dust falls back
downward and settles. Panels remain firmly mounted.

NEGATIVE:
No blue sky, no clear sky, no bright sunlight, no hard shadows, no lens
flare, no bloom, no glow filter. NO TORNADO — the dust devil is a narrow
coherent column, not a funnel cloud, not a wall of dust, not a storm front,
and it does NOT topple panels, push the figure, or create a blast. No
flapping suit fabric, no flying debris. NO FULLY CLEANED OR MIRROR-LIKE
PANELS — the swept row is only THINNER in dust, still matte and still
partly covered. No green anywhere. EXACTLY ONE human — no duplicates, no
clones, no second person. No readable text, letters, digits or symbols on
any surface. Lifted dust falls back downward and settles — no permanently
rising dust, no hovering particles. Visor always visible and fully
transparent. No equipment appearing or disappearing, no helmet
materializing. Static stable terrain. Not miniature, not toy-like. No text
overlay, no title card, no end card, no credits, no watermark, no
subtitles. No CGI aesthetic, no Unreal Engine look. Photorealistic with
35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars solar field. No dialogue. Exactly one human
character. FALSE HOPE BEAT.

A dust devil crosses the panel field and partly clears one row. A suited
figure watches, hopeful — then reads what it actually amounts to.

0s — Fixed lockoff, 32mm Cooke anamorphic, camera at 8 meters, 1.5 meters
height. A 44-YEAR-OLD WOMAN (warm light-brown skin with visible pore
texture, broad forehead, defined jawline, dark brown eyes with deep
fatigue lines beneath, thick eyebrows, thin cracked lips, dark brown hair
going grey at the temples, cut short and pulled back) stands in the left
foreground, half-turned toward camera so her face is readable through the
visor. EQUIPMENT STATE: helmet worn and sealed at 0s and for the entire
take, gloves on, suit closed. She wears a dirty WHITE-BEIGE surface EVA
suit with faded ORANGE accent bands, KNEES AND GLOVES permanently stained
rust-red, a compact back unit with orange banding, and an integrated
helmet with a FULLY TRANSPARENT SEAMLESS VISOR. Behind her: forty solar
panels in a 5-by-8 grid, all buried under uniform red dust. In the
mid-distance, about 30 meters back, a NARROW COHERENT DUST DEVIL — a
vertical rotating column of lifted red dust, 3 meters wide at its base and
about 25 meters tall, leaning slightly — moves diagonally across the field.
The sky is BUTTERSCOTCH BROWN, never blue; the sun a dull pale orange
smudge low and left.

2s — The dust devil tracks along one row of panels. Dust lifts from those
panels into the rotating column. The panels stay firmly mounted; nothing
is toppled, nothing flies, and she is not pushed — the column passes
without force.

4s — She turns her head to follow it, leaning very slightly forward. Her
mouth opens a little and her eyes widen and track — the sharpest, most
alert expression in the film, genuinely hopeful.

6s — The dust devil moves off the field and begins to break up, its column
thinning and losing coherence. Behind it, ONE ROW of panels is now
noticeably THINNER in dust — darker and slightly mottled compared to the
uniform red of the other thirty-odd panels — but still matte, still partly
covered, nowhere near clean.

8s — She looks along the whole field: one partly swept row, and every
other row still buried. Her posture settles back. The alertness leaves her
face and the flat, patient look returns.

10s — She stands still, facing the field. Lifted dust drifts back downward
and settles onto the swept row. Camera never moves. No cuts.

Audio: Her breathing inside the helmet, close and steady, quickening
slightly around 4 seconds and settling again by 9 seconds. As the dust
devil passes, a very faint, thin, MUFFLED low rush — quiet, distant, high
frequencies absent, far weaker than an Earth equivalent. No wind howl, no
roar, no tornado sound. No music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person.
No blue sky, no clear sky, no bright sunlight, no hard shadows, no lens
flare, no bloom, no glow filter. NO TORNADO — the dust devil stays a
narrow coherent rotating column, never a funnel cloud, never a wall of
dust, never a storm front; it does NOT topple or damage panels, does NOT
push, stagger or knock down the figure, does NOT tear at her suit and
produces NO shockwave or blast. No flapping or rippling suit fabric, no
flying debris. NO FULLY CLEANED OR MIRROR-LIKE PANELS — the swept row
becomes only THINNER in dust, staying matte and partly covered, and NO
panel ever becomes clean, reflective or blue-black. All lifted dust falls
back DOWNWARD under 0.38g and settles — no permanently rising dust, no
hovering particles, no anti-gravity behavior, no frame-rate variance on
particle motion. No green anywhere. Photorealistic skin retained through
the clear visor — no airbrushing, no plastic texture, no smoothed skin, no
face morphing. Visor ALWAYS visible, fully transparent, no tint, no HUD
graphics. Suit detail identical — rust-red knee and glove staining stays.
NO EQUIPMENT APPEARING OR DISAPPEARING, no helmet materializing. No
readable text, letters, digits or symbols on any surface. Static stable
terrain. Not miniature, not toy-like. No text overlay, no title card, no
end card, no credits, no watermark, no subtitles. No CGI aesthetic, no
Unreal Engine look, no video game aesthetic. Photorealistic with 35mm
anamorphic film grain.
```

---

## 🎬 SAHNE 18 (S18) — FIRTINA

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars surface at
storm peak. EXACTLY ONE human character in frame.

SCENE:
The dust storm reaches its peak. A suited figure stands in it, untouched
by any force, while the sun disappears entirely.

ENVIRONMENT:
The Martian surface outside a small station at the height of a global dust
storm. Visibility has collapsed to roughly 25 meters — beyond that the
world is a featureless wall of DARK RED-BROWN. The ground immediately
around the figure is red-brown regolith with a few basalt pebbles; it
fades out within a few paces. The sky is no longer distinguishable from
the ground: there is no horizon line anywhere in frame, only a continuous
graded field of dark brown, slightly lighter high in the frame. THE SUN IS
NOT VISIBLE AT ALL — no disc, no bright patch, no direction, only a very
faint overall gradient. Suspended dust fills the entire volume of the
frame as a dense uniform haze. Barely discernible at the edge of
visibility, roughly 20 meters away: the faint dark suggestion of a station
module, more a change of density than a shape.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m; warm light-brown skin with visible pore
texture and an indoor pallor; broad forehead, defined jawline, dark brown
eyes with deep fatigue lines beneath, thick eyebrows, thin cracked lips;
dark brown hair going grey at the temples, cut short and pulled back).
EQUIPMENT STATE: helmet worn and sealed, gloves on, suit fully closed. She
wears a dirty WHITE-BEIGE surface EVA suit with faded ORANGE accent bands,
KNEES AND GLOVES permanently stained rust-red, a compact back unit with
orange banding, and an integrated helmet with a FULLY TRANSPARENT SEAMLESS
VISOR revealing her whole face — the visor now carrying a heavier film of
fresh dust with two recently wiped arc marks. She stands upright in the
centre of frame, arms at her sides, facing slightly away from camera, her
white suit the only light-toned object in an entirely red-brown world. SHE
IS NOT BRACED, NOT LEANING, NOT SHIELDING HER FACE — she stands perfectly
straight and still, because nothing is pushing her. Her face through the
visor is calm and unhurried.

CAMERA:
32mm Cooke anamorphic, f/4, ISO 800, camera fixed at approximately 5
meters, 1.5 meters height. Shallow effective depth due to atmospheric
extinction — she is sharp, everything past 10 meters dissolves into brown.
Physically accurate perspective.

LIGHTING:
A single, entirely DIFFUSE source: the sun, completely hidden, its light
scattered by suspended dust into a shadowless ambient field. There is NO
directional light anywhere in frame. Her suit is lit evenly from all
directions with almost NO shadow — only the faintest darkening under her
chin and back unit. This shadowless flatness is correct for a dust storm
peak and is the visual signature of the shot. Very low saturation, very
low contrast. 0% bloom, no glow filter, no lens flare, no sun.

PHYSICS:
0.38g. Atmospheric pressure 0.6% of Earth's — the storm carries almost NO
force. Nothing is blown at her, nothing strikes her, her suit does not
move. Suspended dust drifts slowly and settles; it does not streak
horizontally past the camera. The storm is defined by DENSITY, not by
motion or violence.

NEGATIVE:
NO EARTH SANDSTORM — no horizontal dust streaks blasting past, no wall of
dust rolling in, no figure staggering, leaning, bracing or shielding her
face, no flapping or rippling suit fabric, no flying debris, no sand
blasting her visor. No blue sky, no clear sky, no visible sun, no bright
patch, no hard shadows, no directional light, no lens flare, no bloom, no
glow filter. No horizon line. No green anywhere. EXACTLY ONE human — no
duplicates, no clones, no second person, no figure emerging from the dust.
No readable text, letters, digits or symbols. Suspended dust drifts slowly
and settles downward — no violent motion, no anti-gravity behavior. Visor
always visible and fully transparent, face readable through it. No
equipment appearing or disappearing, no helmet materializing. Not
miniature, not toy-like. No text overlay, no title card, no end card, no
credits, no watermark, no subtitles. No CGI aesthetic, no Unreal Engine
look. Photorealistic with 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars surface at storm peak. No dialogue. Exactly one
human character.

The storm peaks. The sun vanishes. Nothing dramatic happens — and that is
the threat.

0s — Fixed lockoff, 32mm Cooke anamorphic, camera at 5 meters, 1.5 meters
height. A 44-YEAR-OLD WOMAN (warm light-brown skin with visible pore
texture, broad forehead, defined jawline, dark brown eyes with deep
fatigue lines beneath, thick eyebrows, thin cracked lips, dark brown hair
going grey at the temples, cut short and pulled back) stands upright in the
centre of frame, arms at her sides, facing slightly away from camera.
EQUIPMENT STATE: helmet worn and sealed at 0s and for the entire take,
gloves on, suit closed. She wears a dirty WHITE-BEIGE surface EVA suit with
faded ORANGE accent bands, KNEES AND GLOVES permanently stained rust-red,
a compact back unit with orange banding, and an integrated helmet with a
FULLY TRANSPARENT SEAMLESS VISOR carrying a heavy film of fresh dust and
two recently wiped arc marks. Around her, visibility has collapsed to
about 25 meters: a featureless dark red-brown field with NO horizon line
and NO visible sun. Her white suit is the only light-toned object in
frame. The light is completely diffuse and SHADOWLESS.

3s — The ambient light dims further and evenly as the storm thickens. The
faint dark suggestion of a station module at the edge of visibility, about
20 meters off, fades out of sight entirely. SHE DOES NOT MOVE and is not
pushed — nothing strikes her, her suit does not ripple.

6s — She raises one gloved hand and wipes a single slow arc across her
visor, clearing a band of fresh dust. Her face becomes more readable
through the cleared arc. She lowers the hand.

8s — Fine dust begins settling onto the cleared band almost immediately,
drifting slowly downward, dimming it again.

10s — She stands perfectly straight and still in a world with no horizon,
no sun and no shadow. Camera never moves. No cuts.

Audio: Her breathing inside the helmet, close, slow and steady — by far
the dominant sound. Beneath it, a very faint, thin, MUFFLED, continuous
hiss of suspended sand, low and distant with high frequencies absent, and
NOTHING ELSE. The soundscape is quieter than the viewer expects. No wind
howl, no roar, no rumble, no gale. No music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person,
no figure emerging from the dust. NO EARTH SANDSTORM — the atmosphere is
0.6% of Earth's and carries almost no force: no horizontal dust streaks
blasting past the lens, no rolling wall of dust, no gust fronts, no figure
staggering, leaning, bracing or shielding her face, no flapping or
rippling suit fabric, no flying debris, no sand blasting her visor. NO
VISIBLE SUN, no bright patch, no directional light, no hard shadows, no
horizon line, no blue sky, no lens flare, no bloom, no glow filter — the
light stays completely diffuse and shadowless, and that flatness is
correct. Suspended dust drifts SLOWLY and settles DOWNWARD under 0.38g —
no violent motion, no rising dust, no hovering particles, no anti-gravity
behavior, no frame-rate variance on particle motion. No green anywhere.
Photorealistic skin retained through the clear visor — no airbrushing, no
plastic texture, no smoothed skin, no face morphing. Visor ALWAYS visible,
fully transparent, no tint, no HUD graphics. Suit detail identical —
rust-red knee and glove staining stays. NO EQUIPMENT APPEARING OR
DISAPPEARING, no helmet materializing. Her glove keeps clear structural
contact with the visor when wiping — no merging, no phasing. No readable
text, letters, digits or symbols. Not miniature, not toy-like. No text
overlay, no title card, no end card, no credits, no watermark, no
subtitles. No CGI aesthetic, no Unreal Engine look, no video game
aesthetic. Photorealistic with 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 19 (S19) — VİRAL ARA #3: TEK IŞIK

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars station
exterior at night in a storm. NO human character in frame.

SCENE:
The half-buried station sits in total red darkness. One window is lit —
and it is green.

ENVIRONMENT:
The exterior of a small Mars station during a dust storm at night. Seven
pale white-beige cylindrical modules lie half-buried in red-brown
regolith, connected by low tunnels, all of them coated in dust and reduced
by darkness to faint dark ridges — the outlines are barely readable. The
entire frame is DARK RED-BROWN, nearly black at the edges, with suspended
dust filling the air as a dense haze that softens every contour. There is
NO sun, NO stars, NO moons, NO horizon line — the sky and the ground merge
into one continuous dark field. Only ONE thing in the entire frame emits
light: a SMALL RECTANGULAR WINDOW, roughly 60 by 40 cm, set in the side of
one module — and the light coming through it is SATURATED GREEN. It is the
greenhouse. The green light spills a short distance onto the dusty
regolith directly beneath the window and onto the module's flank,
illuminating a small patch of red ground into a strange olive tone where
the two colours mix. Everything beyond a few meters from that window is
lost in dark red-brown.

SUBJECT:
No human character. The subject of the image is the single green window in
the dark.

CAMERA:
32mm Cooke anamorphic, f/2.8, ISO 1600, camera fixed at approximately 35
meters from the station, at 1.5 meters height, composing the station low
and small across the lower third of frame with the dark storm filling
everything above. Deep focus. Physically accurate perspective, realistic
scale relationships.

LIGHTING:
One motivated source: the greenhouse LEDs behind the small window,
producing SATURATED GREEN light. It is sharp and directional where it
leaves the window — a defined patch on the ground and a defined wash on
the module flank with clear falloff — and it dies out completely within a
few meters. Everything else in the frame is unlit, in deep near-black
red-brown ambient. The extreme contrast between the single green window
and the surrounding darkness IS the image. 0% bloom, no glow filter, no
light beam or god ray in the dust, no halo around the window.

PHYSICS:
0.38g. Atmospheric pressure 0.6% of Earth's. Suspended dust hangs as a
dense haze and settles slowly downward. NOTHING is blown, nothing moves
with force. The station is static and firmly seated in the regolith.

NEGATIVE:
No human character in frame. No bloom, no glow filter, no halo around the
window, no volumetric light beam or god ray reaching out into the dust —
the green light is a defined patch with clear falloff, not a searchlight.
No stars, no moons, no sun, no horizon line, no blue sky, no clear sky. No
other lit windows — exactly ONE window is lit and every other window and
surface is dark. No exterior lamps, no beacons, no blinking lights. Green
appears ONLY as the light from this one window. No violent wind, no flying
debris, no dust streaking horizontally. No readable text, letters, digits
or symbols on the modules. Suspended dust settles downward. Static stable
terrain and structures — no morphing modules, no proportion drift. Not
miniature, not toy-like. No text overlay, no title card, no end card, no
credits, no watermark, no subtitles. No CGI aesthetic, no Unreal Engine
look. Photorealistic with 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars station exterior at night in a storm. No dialogue.
NO human character.

One green window burns in a dead red darkness. Nothing else moves.

0s — Fixed lockoff, 32mm Cooke anamorphic, f/2.8, camera at 35 meters from
the station, 1.5 meters height, the station low and small across the lower
third of frame. Seven pale white-beige modules lie half-buried in
red-brown regolith, dust-coated and reduced by darkness to faint dark
ridges. The whole frame is DARK RED-BROWN, near black at the edges, with
suspended dust filling the air as a dense haze. There is NO sun, NO stars,
NO moons, NO horizon — sky and ground merge into one dark field. A SINGLE
SMALL RECTANGULAR WINDOW, about 60 by 40 cm, in the side of one module
emits SATURATED GREEN light, spilling a defined patch onto the dusty ground
below it and a defined wash across the module's flank, mixing red and green
into a strange olive tone on the regolith.

3s — Suspended dust drifts slowly downward and across the green patch,
very slightly modulating its brightness as it passes — the only movement
anywhere in the frame. The station itself is completely static.

6s — A faint, brief movement crosses INSIDE the green window: an
indistinct dark shape passing behind the glass, unreadable as a person,
gone within a second. The green light is momentarily interrupted and
returns.

8s — Stillness returns. The dust keeps settling. The green patch on the
ground holds steady.

10s — The single green window in the dark red world. Camera never moves.
No cuts.

Audio: A very faint, thin, MUFFLED continuous hiss of suspended sand,
low and distant with high frequencies absent — quieter than expected and
almost the only sound. No wind howl, no roar, no gale, no interior sound,
no machinery, no breathing. Near silence. No music. No dialogue. No
subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
NO HUMAN CHARACTER in frame — the shape crossing behind the glass at 6
seconds stays indistinct, unreadable and never resolves into a person,
face or figure. 0% bloom, no glow filter, no halo around the window, no
volumetric light beam or god ray reaching into the dust — the green light
stays a defined patch with clear falloff, never a searchlight. NO STARS,
no moons, no sun, no horizon line, no blue sky, no clear sky. NO OTHER LIT
WINDOWS — exactly ONE window is lit for the entire take, no other window
or surface lights up, no exterior lamps, no beacons, no blinking lights,
and the green window NEVER goes out. Green appears ONLY as the light from
this one window. No violent wind, no flying debris, no horizontal dust
streaking — suspended dust drifts slowly and settles DOWNWARD under 0.38g,
no rising dust, no hovering particles, no anti-gravity behavior, no
frame-rate variance on particle motion. No readable text, letters, digits
or symbols on the modules. Static stable terrain and structures — no
morphing modules, no proportion drift, no melting or swimming ground. Not
miniature, not toy-like. No text overlay, no title card, no end card, no
credits, no watermark, no subtitles. No CGI aesthetic, no Unreal Engine
look, no video game aesthetic. Photorealistic with 35mm anamorphic film
grain.
```

---

## 🎬 SAHNE 20 (S20) — SEÇİM

> 🏆 **FİLMİN DORUK NOKTASI.** Doruk bir patlama değil, bir kolun
> hareketi. Part A'nın S12'sinde dokunulmayan anahtar burada çevriliyor.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
control module. EXACTLY ONE human character in frame.

SCENE:
A woman's hand closes on the metal switch she refused to touch, and throws
it to the right.

ENVIRONMENT:
The control module of a small Mars station, tight in on the instrument
panel. The TWO SMALL IDENTICAL UNLABELLED DIALS sit at the edges of frame
and between them, filling the centre: the SINGLE HEAVY TWO-POSITION
MECHANICAL TOGGLE SWITCH — a worn bare-metal lever with visible scratches
and finger-polish, now pushed fully to its RIGHT position. Above and
behind, out of focus, the dim amber backlight of the large gauge. The
ceiling LED panels are DEAD — no white light remains; the only illumination
is the amber gauge lamp and a low red emergency strip that has just come
on along the base of the panel. Fine red dust sits in the panel seams.

SUBJECT:
The RIGHT HAND, forearm and lower face of a 44-year-old woman — warm
light-brown skin with visible pore texture, fine knuckle lines, short
unpainted nails, dry cracked skin. Her hand is CLOSED FIRMLY around the
metal lever, thumb and forefinger gripping it, the lever held hard over in
its right position, her tendons and knuckles showing real tension and the
skin of her fingers slightly flattened where it presses the metal. The
cuff of her MAROON FLEECE JACKET is at her wrist. In the upper part of
frame, softly out of focus: her jaw and mouth, lips pressed closed, and
one eye catching the amber light. EQUIPMENT STATE: NO helmet, NO suit, NO
gloves — bare hand.

CAMERA:
85mm, f/2.0, ISO 2000, camera fixed at approximately 0.7 meters, low angle
just below switch level — the identical framing to the Part A closing
shot, deliberately matched. Very shallow depth of field — the lever and her
gripping fingers razor-sharp, her face soft above.

LIGHTING:
Two motivated sources. (1) The dim amber gauge backlight (2400K) from the
side, raking hard across the metal lever and her gripping hand, picking out
scratches on the metal and tendons on her hand. (2) A LOW RED EMERGENCY
STRIP (1900K) newly lit along the base of the panel, adding a hard red
underlight from below — this red is new to the frame and marks the moment
the habitat dropped to emergency power. Extremely low-key, high contrast.
0% bloom, no glow filter.

PHYSICS:
0.38g. Cold interior. The switch is a heavy mechanical lever and her grip
shows the force needed to hold it over. Clear structural contact boundary
between skin and metal, with visible slight flattening of the fingertips.

NEGATIVE:
No bloom, no glow filter, no soft focus glow on the metal. No airbrushed
skin, no plastic or waxy texture — knuckle lines, tendons, dry cracked skin
and pore texture remain visible. EXACTLY ONE human — no duplicates, no
second hand, no extra fingers, no phantom digits. THE SWITCH IS IN ITS
RIGHT POSITION and her hand is in FIRM CONTACT with it — no air gap, no
merging, no phasing, no finger passing through metal. NO READABLE TEXT,
letters, digits, numbers or labels on the switch, dials or panel — the two
dials stay identical and unlabelled. No green anywhere. No white ceiling
light — the ceiling panels are dead. No equipment appearing — no glove, no
suit, no helmet. Static stable environment. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat control module with a spoken log entry.
Exactly one human character. The speaker is off screen in this framing —
her mouth is soft and out of focus, so treat the line as recorded voice
with NO lip-sync requirement.

A hand takes the switch and throws it. The white lights die. A red strip
comes on.

0s — Fixed lockoff, 85mm, f/2.0, camera at 0.7 meters, low angle just
below switch level, very shallow depth of field — the identical framing to
the previous switch shot. Filling the centre of frame: a SINGLE HEAVY
TWO-POSITION MECHANICAL TOGGLE SWITCH, a worn bare-metal lever with
scratches and finger-polish, sitting in its LEFT position. Two small
identical unlabelled dials sit at the edges of frame. Behind, out of
focus, the dim amber backlight of a large gauge. The ceiling panels give a
weak residual white. Softly out of focus in the upper frame: the jaw and
mouth of a 44-year-old woman, and the cuff of a MAROON FLEECE JACKET.
EQUIPMENT STATE: NO helmet, NO suit, NO gloves at any point — bare hand.

2s — Her bare RIGHT HAND enters frame from the upper right — warm
light-brown skin with visible pore texture, fine knuckle lines, short
unpainted nails, dry cracked skin — and closes FIRMLY around the metal
lever. Thumb and forefinger grip it. Tendons and knuckles show real
tension. The fingertips flatten slightly against the metal with a clear
contact boundary.

4s — She pushes the lever fully over from LEFT to RIGHT in one firm,
committed movement. The lever travels and seats hard in its right position
with a heavy mechanical action.

5.5s — The residual white ceiling light DIES OUT completely. A LOW RED
EMERGENCY STRIP lights along the base of the panel, throwing a hard red
underlight up across her hand and the metal. The frame's colour changes
from amber-and-grey to amber-and-red, continuously, within the take.

7s — Her voice comes in as a quiet recorded log, flat and steady, while her
out-of-focus mouth stays soft and unreadable: "Greenhouse gets the rest."

9s — Her hand stays closed on the lever, not letting go, holding it there.

10s — The switch in its right position, her hand still on it, red and amber
light across the metal. Camera never moves. No cuts.

Audio: A single heavy mechanical CLUNK as the lever seats at 4 seconds. A
soft electrical drop as the white lighting dies, followed by the low steady
hum of an emergency circuit. Clean dialogue only — one speaker, her voice
quiet, close and clearly dominant, recorded log, NO reply and NO second
voice at any point. Beneath: a thin distant hiss of sand against the hull.
No music. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves,
and the lighting change from white to red happens continuously within the
single take. EXACTLY ONE human — no duplicates, no second hand entering
frame, no second person, no reply voice, no simultaneous speech, no extra
fingers, no phantom digits. The spoken line is OFF-SCREEN RECORDED VOICE:
her mouth stays soft and out of focus, no clear lip movement is required
or shown, and no in-focus talking mouth appears at any point. THE HAND
MAKES FIRM CONTACT with the switch — no air gap once gripped, no merging,
no phasing, no finger passing through metal. THE SWITCH MOVES EXACTLY ONCE,
from LEFT to RIGHT, and then stays in its RIGHT position — it does not
return, flip back, or move again. 0% bloom, no glow filter, no soft focus
glow on the metal. Photorealistic skin — knuckle lines, tendons, dry
cracked skin and pore texture retained, no airbrushing, no plastic
texture, no smoothed or waxy skin. NO EQUIPMENT APPEARING — no glove, no
suit, no helmet materializes. NO READABLE TEXT, letters, digits, numbers
or labels on the switch, dials or panel — the dials stay identical and
unlabelled. No green anywhere. THE WHITE CEILING LIGHT DOES NOT COME BACK
ON after it dies. 0.38g — real weight and tension, nothing floats. Static
stable environment. No text overlay, no title card, no end card, no
credits, no watermark, no subtitles. No CGI aesthetic, no Unreal Engine
look, no video game aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 21 (S21) — BEDEL

> ⚠️ **DERS 37 KRİTİK SAHNESİ:** Filmin TEK ekipman durum değişikliği
> burada, ekranda gerçekleşiyor. Kask bu sahnede TAKILMAYA BAŞLIYOR.
> Diğer tüm sahnelerde durum sabittir; burada değişim kasıtlı ve görünür.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
living module. EXACTLY ONE human character in frame.

SCENE:
In a habitat that has gone dark and cold, a woman lifts her helmet to put
it on indoors.

ENVIRONMENT:
The living module of a small Mars station after main power has been cut.
The ceiling LED panels are DEAD. The only lighting is a LOW RED EMERGENCY
STRIP running along the base of one wall, casting hard red light upward
across the panels and floor, and leaving the upper half of the room in
near-darkness. The walls are scuffed pale grey-white composite panels,
now reading dull red, with fine dust in the seams. The twelve berth
curtains are all drawn and dark. The air is visibly cold — a faint haze of
condensation hangs near the floor. Her surface EVA suit's lower half and
back unit are already on her body; the HELMET is held in her hands.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m, lean with visible muscle loss; warm
light-brown skin with visible pore texture and an indoor pallor; broad
forehead, defined jawline, dark brown eyes with deep fatigue lines
beneath, thick natural eyebrows, thin cracked lips, an old 3cm burn scar
on the back of her left hand; dark brown hair going grey at the temples,
cut short and pulled back; no makeup, no airbrushing). EQUIPMENT STATE —
TRANSITIONAL: she is WEARING the dirty WHITE-BEIGE surface EVA suit with
faded ORANGE accent bands and the compact back unit, with the MAROON
FLEECE JACKET VISIBLE AT HER COLLAR AND CUFFS UNDERNEATH the suit — she
has kept it on and put the suit on over it. HER HELMET IS NOT YET ON: she
holds it in BOTH HANDS at chest height, its FULLY TRANSPARENT SEAMLESS
VISOR facing her, her fingers gripping the rim with clear contact. Her
face is fully exposed and unobstructed. Her breath is CLEARLY visible as
vapour with every exhale. Her expression is composed and matter-of-fact —
she is performing a practical step, not a farewell.

CAMERA:
50mm, f/2.0, ISO 3200, camera fixed at approximately 2 meters, chest
height, framing her from the waist up with the dark module behind her.
Shallow depth of field — her face and the helmet sharp, the module soft.

LIGHTING:
One motivated source: the LOW RED EMERGENCY STRIP (1900K) at floor level,
throwing a hard, directional, upward red light across her suit, her jaw
and the underside of the helmet in her hands, leaving her eye sockets and
the top of the frame in deep shadow. This underlight is harsh and
unflattering and is the correct look. A very faint cool residual grey
edges her far shoulder. Extremely low-key, high contrast. Skin retains
full pore and fatigue texture. 0% bloom, no glow filter.

PHYSICS:
0.38g. The habitat is now COLD — her exhaled breath condenses into clearly
visible vapour that drifts and dissipates. The helmet is a solid object
with real weight in her hands; her fingers show contact pressure on its
rim. The suit is stiff and does not drape.

NEGATIVE:
No bloom, no glow filter, no soft focus. No airbrushed skin, no plastic or
waxy texture, no smoothed skin — pore texture, fatigue lines, cracked lips
and the burn scar remain visible. No face morphing. EXACTLY ONE human — no
duplicates, no clones, no second person. THE HELMET IS OFF AND HELD IN HER
HANDS in this image — it is not on her head, and it does not appear on her
head. No hand-helmet merging, no phasing, no extra fingers. No white
ceiling light — the panels are dead. No green anywhere. No readable text,
letters, digits or symbols on the suit, the helmet or any surface. No
floating objects. Static stable environment. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat living module. No dialogue. Exactly one
human character. THE FILM'S ONLY ON-SCREEN EQUIPMENT STATE CHANGE.

In a dark, freezing habitat, a woman puts her helmet on indoors and seals
it.

0s — Fixed lockoff, 50mm, f/2.0, camera at 2 meters, chest height. A
44-YEAR-OLD WOMAN (warm light-brown skin with visible pore texture and an
indoor pallor, broad forehead, defined jawline, dark brown eyes with deep
fatigue lines beneath, thick eyebrows, thin cracked lips, an old burn scar
on the back of her left hand, dark brown hair going grey at the temples,
cut short and pulled back) stands in a dark living module. EQUIPMENT STATE
AT 0s: she is WEARING the dirty WHITE-BEIGE surface EVA suit with faded
ORANGE accent bands and the compact back unit, with her MAROON FLEECE
JACKET visible at the collar and cuffs UNDERNEATH the suit. HER HELMET IS
OFF and held in BOTH HANDS at chest height, its FULLY TRANSPARENT SEAMLESS
VISOR facing her — her face is fully exposed. The ceiling panels are dead;
the only light is a LOW RED EMERGENCY STRIP at floor level throwing hard
red light upward. Her breath condenses into clearly visible vapour.

2s — She exhales. The vapour is dense and obvious in the cold. She looks
down at the helmet in her hands for a moment.

4s — She raises the helmet and lowers it over her head in one smooth,
practised, deliberate movement. Her hands stay in clear contact with the
rim throughout — the helmet is a solid object with weight and never passes
through her head or hair.

6.5s — She brings both hands to the collar ring and rotates it until it
seats, then presses down twice to confirm the seal. HER FACE REMAINS FULLY
VISIBLE AND READABLE through the clear visor from this moment on.

8.5s — The visor fogs briefly from the inside with her first enclosed
breath and clears again as the suit system cycles.

10s — She stands in the red light, helmet on and sealed, face readable
through the clear visor, breathing steadily. Camera never moves. No cuts.

Audio: A low emergency circuit hum, thinner and colder than the earlier
habitat sound. Two solid mechanical clicks as the collar ring seats and
locks. The muted internal rhythm of her suit pump starting up, and her
breathing shifting from open-air to close, enclosed, helmet-internal
acoustics at 6.5 seconds. Very faintly beneath: a thin distant hiss of sand
against the hull. No music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves,
and the entire helmet-donning action happens continuously within the single
take. EXACTLY ONE human character — no duplicates, no clones, no second
person. EQUIPMENT STATE CHANGE IS DELIBERATE AND MUST BE SHOWN IN FULL:
the helmet starts OFF in her hands and ends ON and sealed, and the
transition is a continuous physical action — the helmet NEVER teleports
onto her head, never materializes, never cuts from off to on, and never
passes through her head or hair. The MAROON FLEECE JACKET stays visible at
her collar and cuffs under the suit throughout and is never removed. HER
FACE STAYS READABLE at all times — exposed before the helmet, and through
the FULLY TRANSPARENT SEAMLESS VISOR after; visor always visible, no tint,
no reflective coating, no HUD graphics, no invented reflections. 0% bloom,
no glow filter, no soft focus — the red emergency strip is hard, upward
and directional with clear falloff and deep shadows. Photorealistic skin
pores, fatigue lines, cracked lips and the burn scar retained under red
light — no airbrushing, no plastic texture, no smoothed or waxy skin, no
face morphing. Her hands keep clear structural contact with the helmet rim
and collar ring — no hand-helmet merging, no phasing, no extra fingers.
NO WHITE CEILING LIGHT comes back on. No green anywhere. No readable text,
letters, digits or symbols on the suit, helmet or any surface. Breath
vapour condenses, drifts and dissipates naturally under 0.38g — nothing
floats or hangs. Static stable environment. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look, no video game aesthetic. Photorealistic
with 35mm film grain.
```

---

## 🎬 SAHNE 22 (S22) — TOHUM

> 🎯 **FİLMİN TEMATİK CÜMLESİ BU SAHNEDE SÖYLENİR.**

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
greenhouse. EXACTLY ONE human character in frame.

SCENE:
A suited woman seals a metal seed case and places it back on the lowest
shelf of the greenhouse, where the light will keep reaching it.

ENVIRONMENT:
The greenhouse module of a small Mars station — the ONLY brightly lit room
left in the station. Four tiers of vertical hydroponic racks, dense with
living green lettuce, climbing beans and dwarf wheat, lit from beneath each
shelf by sharp, defined MAGENTA-WHITE LED strips at FULL power, their
light bouncing off the foliage so the room reads strongly GREEN. The
nine-row dead section on the upper rack is still there, dry and
yellow-brown. White nutrient channels carry solution; condensation
droplets cling to the fittings. Through the small rectangular window in
the wall: flat dark red-brown — the storm outside, featureless. On the
LOWEST SHELF sits the plain sealed grey metal SEED CASE, 30 by 20 cm,
unmarked, its latch closed.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m; warm light-brown skin with visible pore
texture and an indoor pallor; broad forehead, defined jawline, dark brown
eyes with deep fatigue lines beneath, thick eyebrows, thin cracked lips;
dark brown hair going grey at the temples, cut short and pulled back).
EQUIPMENT STATE: helmet WORN AND SEALED, gloves on, suit closed — indoors
but suited, because the habitat is now unheated. The MAROON FLEECE JACKET
is visible at her collar under the suit. She kneels on one knee at the
lowest shelf, both gloved hands on the metal seed case, having just closed
its latch. Her face is fully readable through the FULLY TRANSPARENT
SEAMLESS VISOR — lit green from the racks above and around her. Her
expression is settled and clear: not grief, not resignation, but the
particular calm of someone who has finished arranging something.

CAMERA:
50mm, f/2.0, ISO 800, camera fixed at approximately 1.5 meters, low angle
at 0.6 meters height, level with the lowest shelf, framing her kneeling
figure, her gloved hands and the seed case together with green foliage
filling the upper frame. Shallow depth of field — her face, hands and the
case sharp; the upper racks soft.

LIGHTING:
One motivated source family: the MAGENTA-WHITE LED grow strips under every
shelf, at full power — sharp, defined, directional strips whose light
bounces off dense foliage into a strong GREEN fill across her visor, her
face and the white suit. The white suit takes the green cast strongly.
This is the brightest and most saturated lighting in the entire film, and
it directly follows the darkest scenes — the contrast is the point. 0%
bloom, no glow filter, only real humidity haze.

PHYSICS:
0.38g. The greenhouse is warm (22°C) and humid while the rest of the
station is freezing. Her gloved hands press the metal case with clear
contact. Leaves hang and curve under gravity. Nothing floats.

NEGATIVE:
No bloom, no glow filter, no soft focus glow — LED strips are sharp
defined lines, not halos. No airbrushed skin, no plastic or waxy texture,
no smoothed skin — pore texture, fatigue lines and cracked lips remain
visible THROUGH the clear visor. No face morphing. EXACTLY ONE human — no
duplicates, no clones, no second person. NO READABLE TEXT, letters,
digits, numbers or labels on the seed case, trays, suit or any surface —
the case stays plain and unmarked. NO EQUIPMENT STATE CHANGE — the helmet
is ON and sealed throughout and is never removed. No hand-case merging, no
phasing, no extra fingers. Visor always visible and fully transparent.
Through the window: no blue sky, no sun, no stars — only flat dark
red-brown. No reviving of the dead rows. Static stable environment — no
morphing foliage, no swimming texture. No text overlay, no title card, no
end card, no credits, no watermark, no subtitles. No CGI aesthetic, no
Unreal Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat greenhouse with a spoken log entry.
Exactly one human character. Her face is visible through a clear visor in
medium framing — LIP-SYNC REQUIRED.

A suited woman seals a seed case, puts it where the light will reach it,
and says what it is for.

0s — Fixed lockoff, 50mm, f/2.0, camera at 1.5 meters, low angle at 0.6
meters height, level with the lowest shelf. A 44-YEAR-OLD WOMAN (warm
light-brown skin with visible pore texture, broad forehead, defined
jawline, dark brown eyes with deep fatigue lines beneath, thick eyebrows,
thin cracked lips, dark brown hair going grey at the temples, cut short and
pulled back) kneels on one knee at the shelf. EQUIPMENT STATE: helmet WORN
AND SEALED at 0s and for the entire take, gloves on, suit closed — nothing
is put on or removed. Her MAROON FLEECE JACKET is visible at her collar
under the suit. Both gloved hands rest on a plain grey metal SEED CASE, 30
by 20 cm, unmarked. Around and above her, four tiers of dense living green
foliage under sharp MAGENTA-WHITE LED strips at FULL power fill the frame
with strong green light. The nine dead rows on the upper rack remain dry
and yellow-brown. Through a small window: flat dark red-brown.

2s — She closes the latch on the seed case with her gloved thumb — a small,
firm, definite movement with a clear contact boundary and an audible catch.

4s — She lifts the case, slides it fully onto the lowest shelf directly
beneath a grow light strip, and squares it against the shelf edge with both
hands so it sits straight.

6s — She says quietly and evenly, her face readable through the clear
visor, her lip movements matching the words precisely for the full line:
"You'll open these. I won't. I didn't plant them for me."

9s — Her mouth closes and stays still. She rests one gloved hand flat on
top of the case for a moment, then lifts it away.

10s — She kneels in the green light beside the seed case on the shelf.
Camera never moves. No cuts.

Audio: Clean dialogue only — one speaker, her voice quiet, close and
clearly dominant, slightly enclosed by the helmet, recorded as a log with
NO reply and NO second voice at any point. A small metallic catch as the
latch closes, and a soft scrape as the case slides onto the shelf. Beneath:
a soft water circulation hum, the faint trickle of nutrient solution, and
a gentle electrical hum from the LED strips. No music. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change — the camera is locked off and never moves.
EXACTLY ONE human character — no duplicates, no clones, no second person,
no reply voice, no simultaneous speech. LIP-SYNC: her lip movements match
the spoken words precisely for the entire line and are clearly visible
through the transparent visor; her mouth is closed and still before the
line begins and after it ends — no mouth movement without audio, no audio
without matching mouth movement, no sync drift. NO EQUIPMENT STATE CHANGE
— the helmet stays ON and sealed for the entire take, never removed, never
materializing. Visor ALWAYS visible, fully transparent, no tint, no HUD
graphics, no invented reflections. 0% bloom, no glow filter, no soft focus
glow — the LED strips stay sharp defined lines of light, never halos; only
real humidity haze. Photorealistic skin pores, fatigue lines and cracked
lips retained through the visor — no airbrushing, no plastic texture, no
smoothed or waxy skin, no face morphing. NO READABLE TEXT, letters,
digits, numbers or labels appear on the seed case, trays, suit or any
surface at any point — the case stays plain and unmarked, and NO label or
writing is added to it. Her gloves keep clear structural contact with the
case and latch — no merging, no phasing, no extra fingers. 0.38g — the case
has real weight, leaves hang under gravity, nothing floats. NO REVIVING
PLANTS — the dead rows stay dead. Through the window: no blue sky, no sun,
no stars, only flat dark red-brown. Static stable environment — no morphing
foliage, no swimming texture. No text overlay, no title card, no end card,
no credits, no watermark, no subtitles. No CGI aesthetic, no Unreal Engine
look, no video game aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 23 (S23) — VİRAL ARA #4: İKİ DÜNYA

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
greenhouse interior. NO human character in frame.

SCENE:
Inside the greenhouse: green living foliage in the foreground, and through
the window behind it, the dead red storm.

ENVIRONMENT:
The interior of the greenhouse module. The FOREGROUND and both sides of the
frame are filled with dense LIVING GREEN foliage on hydroponic racks —
lettuce leaves, bean vines and dwarf wheat, wet and turgid, lit from
beneath by sharp defined MAGENTA-WHITE LED strips at full power so the
whole foreground reads saturated GREEN. Condensation beads on the leaves
and on the white plastic channels. Set in the wall behind the racks: the
SMALL RECTANGULAR WINDOW, roughly 60 by 40 cm, thick-glassed and set deep
in the panel. Through it: flat, featureless DARK RED-BROWN — the dust storm
outside, with no horizon, no sun, no stars, no detail of any kind. A thin
film of red dust has settled on the OUTSIDE of the glass. The composition
places the green living foreground and the dead red rectangle in direct
opposition, sharing the frame, separated by a few centimetres of glass.

SUBJECT:
No human character. The subject is the confrontation between the two
colours: living green inside, dead red outside.

CAMERA:
50mm, f/2.0, ISO 640, camera fixed at approximately 1.2 meters inside the
greenhouse, level with the window, shooting past the foliage toward it.
Shallow depth of field — the nearest leaves and the window frame sharp, the
mid-rack foliage soft. Physically accurate perspective.

LIGHTING:
Two motivated sources in direct opposition. (1) The MAGENTA-WHITE LED grow
strips under the shelves — sharp, defined, directional, bouncing off the
foliage into a strong saturated GREEN across the entire interior. (2) A
weak, flat, DIFFUSE dark red-brown ambient coming through the window from
the storm — almost no light at all, contributing only a dull glow to the
rectangle itself and a faint red rim on the window frame. The green
interior is far brighter than the red exterior. 0% bloom, no glow filter,
no light beams in the humid air beyond real haze.

PHYSICS:
0.38g. Warm (22°C) and humid inside; freezing and airless outside.
Condensation beads cling to leaves and fittings by surface tension. Leaves
hang and curve under gravity. Outside the glass, suspended dust hangs as
uniform haze; nothing is blown past the window.

NEGATIVE:
No human character in frame, no figure, no reflection of a person in the
glass. No bloom, no glow filter, no soft focus glow, no god rays or light
beams in the air beyond real humidity haze. NO READABLE TEXT, letters,
digits or symbols on the trays, channels, window frame or any surface.
Through the window: no blue sky, no clear sky, no sun, no stars, no
horizon, no Earth, no visible landscape features — only flat featureless
dark red-brown. No green outside the window. No red light inside the
greenhouse beyond the faint rim on the window frame. No wind, no flying
debris, no dust streaking past the glass. No floating leaves or droplets —
0.38g, everything hangs and rests. Static stable environment — no morphing
foliage, no swimming texture, no growing plants. No text overlay, no title
card, no end card, no credits, no watermark, no subtitles. No CGI
aesthetic, no Unreal Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat greenhouse interior. No dialogue. NO
human character.

Green life in the foreground, red death through the glass, a few
centimetres apart.

0s — Fixed lockoff, 50mm, f/2.0, camera at 1.2 meters inside the
greenhouse, level with the window, shooting past foliage toward it. The
foreground and both frame edges are filled with dense LIVING GREEN
foliage — lettuce leaves, bean vines, dwarf wheat, wet and turgid — lit
from beneath by sharp defined MAGENTA-WHITE LED strips at full power, so
the whole interior reads saturated GREEN. Condensation beads on leaves and
white plastic channels. Set in the wall behind: a SMALL RECTANGULAR WINDOW,
60 by 40 cm, thick-glassed, showing flat featureless DARK RED-BROWN
outside — no horizon, no sun, no stars, no detail. A thin film of red dust
sits on the outside of the glass.

3s — A single condensation droplet on a foreground leaf swells, releases
and falls straight DOWNWARD out of frame — slowly, about two and a half
times slower than on Earth, but unmistakably falling. Nothing else moves
inside.

6s — Outside the glass, the dark red-brown shifts very slightly in density
as suspended dust drifts past — a faint, slow modulation with no direction
and no streaking. The rectangle stays featureless.

8s — A leaf in the foreground settles a few millimetres under its own
weight, the only movement in the interior.

10s — The green interior and the red rectangle, held in the same frame.
Camera never moves. No cuts.

Audio: A soft continuous water circulation hum and the faint trickle of
nutrient solution through plastic channels, close and warm. A gentle
electrical hum from the LED strips. A single small liquid tick as the
droplet lands off frame. Through the wall, very faintly and distantly: a
thin muffled hiss of sand. No music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change, no focus racking to another subject — the
camera is locked off and never moves. NO HUMAN CHARACTER in frame at any
point — no figure, no hand, no silhouette, no reflection of a person in the
glass, no one passing behind the racks. 0% bloom, no glow filter, no soft
focus glow, no god rays or light beams in the air beyond real humidity
haze — the LED strips stay sharp defined lines. NO READABLE TEXT, letters,
digits or symbols on the trays, channels, window frame or any surface.
THROUGH THE WINDOW: no blue sky, no clear sky, no sun, no stars, no
horizon, no Earth, no landscape features, no moving clouds — only flat
featureless dark red-brown, and nothing is blown past the glass. No green
outside the window and no red light inside the greenhouse beyond a faint
rim on the window frame. Liquid obeys 0.38g — droplets cling by surface
tension or fall DOWNWARD, never float, never hover, never rise. Leaves hang
and curve under gravity. Static stable environment — no morphing foliage,
no swimming texture, no growing or animating plants, no writhing vines. No
text overlay, no title card, no end card, no credits, no watermark, no
subtitles. No CGI aesthetic, no Unreal Engine look, no video game
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 24 (S24) — FİNAL: DEVRETME

> 🏁 **FİLMİN SON KARESİ.** Ölüm gösterilmez. Karartma yapılmaz —
> post-prodüksiyonda eklenir [DERS 1 + DERS 34].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Mars habitat
corridor. EXACTLY ONE human character in frame.

SCENE:
A suited woman sits on the floor of a dark corridor with her back against
the wall, facing the green light coming from under the greenhouse door.

ENVIRONMENT:
The living module corridor of a small Mars station, now almost entirely
dark. The ceiling panels are dead. A single LOW RED EMERGENCY STRIP runs
along the base of one wall, giving a weak red underlight that dies out
within a metre. The walls are scuffed pale grey-white panels reading dull
red, fine dust in the seams; twelve berth curtains drawn and dark. At the
far end, roughly 4 meters away: the CLOSED GREENHOUSE HATCH, and beneath
it a hard, bright BAR OF SATURATED GREEN LIGHT about 4cm tall spilling
across the deck toward her — brighter and more saturated than anything
else in frame, reaching perhaps two metres down the corridor before fading.

SUBJECT:
A 44-YEAR-OLD WOMAN (1.68m; warm light-brown skin with visible pore
texture and an indoor pallor; broad forehead, defined jawline, dark brown
eyes with deep fatigue lines beneath, thick eyebrows, thin cracked lips;
dark brown hair going grey at the temples, cut short and pulled back).
EQUIPMENT STATE: helmet WORN AND SEALED, gloves on, suit closed, MAROON
FLEECE JACKET visible at her collar under the suit. She SITS ON THE DECK
with her back against the corridor wall, knees drawn up loosely, gloved
hands resting on her knees, in profile to camera. Her helmeted head is
turned toward the far hatch and its green light. Her face is fully
readable through the FULLY TRANSPARENT SEAMLESS VISOR: eyes open, mouth
relaxed, expression calm and unafraid — settled rather than defeated. The
green light from the distant hatch reaches her boots and lower legs; the
red emergency strip edges her back and shoulder. Her face is lit only
faintly, catching a trace of green.

CAMERA:
50mm, f/2.0, ISO 3200, camera fixed at approximately 2.5 meters, LOW angle
at 0.5 meters height — near deck level, so the green bar of light runs
along the floor plane toward the lens and she is seen almost at eye level
with the light. Moderate depth of field — she and the distant hatch both
readable. Physically accurate perspective.

LIGHTING:
Two motivated sources. (1) The BAR OF GREEN LIGHT under the distant
greenhouse hatch — sharp, defined, running along the deck with clear
falloff, the brightest and most saturated element, reaching her boots. (2)
The LOW RED EMERGENCY STRIP on the near wall, a weak hard red rim on her
back and shoulder. Everything else is deep near-black. The two colours
never mix on her body: green ahead, red behind. Extremely low-key, very
high contrast. Skin retains pore texture where lit. 0% bloom, no glow
filter, no light beams in the air.

PHYSICS:
0.38g. The corridor is freezing; the suit is sealed. She sits with real
weight, her back and hips in contact with wall and deck. The suit is stiff
and does not drape. Settled dust remains in the seams.

NEGATIVE:
No bloom, no glow filter, no soft focus, no volumetric light beams or god
rays from under the hatch — the green light is a hard defined bar on the
deck. No airbrushed skin, no plastic or waxy texture, no smoothed skin —
pore texture, fatigue lines and cracked lips remain visible through the
clear visor. No face morphing. EXACTLY ONE human — no duplicates, no
clones, no second person, no figure at the hatch. NO SIGNS OF DEATH — she
is alive, upright against the wall, eyes open, breathing; no slumping, no
closed eyes, no blood, no injury, no distress. NO EQUIPMENT STATE CHANGE —
helmet on and sealed throughout. Visor always visible and fully
transparent. NO READABLE TEXT, letters, digits or symbols on any surface.
Green appears ONLY as the light bar from the greenhouse. No white ceiling
light. No floating objects. Corridor locked at 1.4 meters wide, 2.1 meters
high. Static stable environment. No text overlay, no title card, no end
card, no credits, no watermark, no subtitles. No CGI aesthetic, no Unreal
Engine look. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 10 seconds. Mars habitat corridor. No dialogue. Exactly one human
character. THE FINAL SHOT OF THE FILM.

A suited woman sits in the dark and watches the one light she chose to
keep on.

0s — Fixed lockoff, 50mm, f/2.0, camera at 2.5 meters, LOW angle at 0.5
meters height near deck level. A 44-YEAR-OLD WOMAN (warm light-brown skin
with visible pore texture, broad forehead, defined jawline, dark brown eyes
with deep fatigue lines beneath, thick eyebrows, thin cracked lips, dark
brown hair going grey at the temples, cut short and pulled back) SITS ON
THE DECK with her back against the corridor wall, knees drawn up loosely,
gloved hands on her knees, in profile to camera. EQUIPMENT STATE: helmet
WORN AND SEALED at 0s and for the entire take, gloves on, suit closed,
MAROON FLEECE JACKET visible at her collar under the suit — nothing is put
on or removed. The ceiling panels are dead. A LOW RED EMERGENCY STRIP on
the near wall rims her back. Four meters away at the end of the corridor,
beneath the closed greenhouse hatch, a hard bright BAR OF SATURATED GREEN
LIGHT about 4cm tall runs along the deck toward the lens, reaching her
boots. Her helmeted head is turned toward it. Her face is fully readable
through the clear visor.

3s — She breathes slowly and steadily inside the helmet. Her chest rises
and falls visibly. Her eyes stay open, fixed on the green light. Nothing
else in the corridor moves.

6s — She shifts her shoulders very slightly against the wall, settling
more comfortably, and her gloved hands relax further onto her knees. The
movement is small and unhurried.

8s — Her mouth relaxes slightly — not a smile, but the tension leaving her
jaw. The green light holds steady on the deck and on her boots.

10s — She sits in the dark corridor, sealed, alive, watching the green
line under the door. The camera never moves. The shot ends on this held
frame. No cuts.

Audio: Her breathing inside the helmet — close, slow, steady, and by far
the dominant sound. The thin cold hum of an emergency circuit. Very
faintly and distantly, through the wall, a thin muffled hiss of sand. From
behind the greenhouse hatch, extremely faint: the soft water circulation
hum, still running. No music. No dialogue. No subtitles.

Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no jump cuts, no camera teleportation,
no angle change — the camera is locked off and never moves. THE SHOT ENDS
ON THE HELD FRAME: NO fade to black, NO fade out, NO dissolve, NO title
card, NO end card, NO credits, NO text fading in — the take simply ends.
EXACTLY ONE human character — no duplicates, no clones, no second person,
no figure appearing at the hatch, no door opening. NO SIGNS OF DEATH — she
stays alive, upright against the wall, eyes open and breathing for the
entire take; no slumping, no head dropping, no closing eyes, no blood, no
injury, no convulsion, no distress. NO EQUIPMENT STATE CHANGE — the helmet
stays ON and sealed throughout, never removed, never materializing. Visor
ALWAYS visible, fully transparent, no tint, no HUD graphics, no invented
reflections. 0% bloom, no glow filter, no soft focus, no volumetric light
beams or god rays under the hatch — the green light stays a hard defined
bar on the deck with clear falloff. Photorealistic skin pores, fatigue
lines and cracked lips retained through the visor — no airbrushing, no
plastic texture, no smoothed or waxy skin, no face morphing. NO READABLE
TEXT, letters, digits or symbols on any surface. Green appears ONLY as the
light bar from the greenhouse and NEVER goes out or dims. No white ceiling
light comes on. 0.38g — she sits with real weight and contact, nothing
floats. Corridor locked at 1.4 meters wide and 2.1 meters high — no
proportion drift. Settled dust stays settled. Static stable environment. No
text overlay, no watermark, no subtitles. No CGI aesthetic, no Unreal
Engine look, no video game aesthetic. Photorealistic with 35mm film grain.
```

---

# 🎶 MÜZİK — PART B

### 🎼 Enstrümantasyon Mimarisi (Part B yayı)

**Tema:** "From Arithmetic to Release" (Hesaptan Bırakışa)
**Referans:** Jóhann Jóhannsson (*Arrival*), Max Richter (*Ad Astra*), Hildur Guðnadóttir.
**Tempo:** 58 BPM sabit. Filmin tamamı boyunca hızlanmaz — bu kasıtlıdır.

```
KATMAN 1  Sub-bass drone (35-45Hz) — fırtınanın sürekli varlığı. S13-S19.
KATMAN 2  Prepared piano, tek notalar, geniş aralıklarla — güç göstergesi.
          Her nota arası uzuyor: sistemin yavaşlaması.
KATMAN 3  Solo çello, düşük register, arşe basıncı duyulur — Selin.
KATMAN 4  Yüksek yaylı doku (violin harmonics) — SADECE sera sahnelerinde.
          Filmin tek "yukarı" sesi. S16, S22, S23.
KATMAN 5  MUTLAK SESSİZLİK — S20'de anahtar çevrildiğinde müzik TAMAMEN
          kesilir ve S21 boyunca geri gelmez. 20 saniyelik müziksizlik.
```

### 📊 Part B Müzik Matrisi

| Sahne | Katmanlar | Dinamik |
|---|---|---|
| S13-S15 | 1 + 2 | Seyrek prepared piano, uzayan aralıklar |
| S16 | 1 + 3 + 4 | Çello girer; sera dokusu ilk kez duyulur |
| S17 | 1 + 2 (hızlanan) | Tek "umut" anı — tempo değil, yoğunluk artar |
| S18-S19 | 1 (yalnız) | Sadece drone. Melodi yok. |
| **S20** | **KESİLME** | Anahtar sesiyle birlikte TAM SESSİZLİK |
| S21 | — | Müziksiz. Sadece nefes ve devre uğultusu. |
| S22 | 3 + 4 | Çello ve yaylılar birlikte — filmin tek "tam" anı |
| S23-S24 | 4 (yalnız) → fade | Yüksek yaylı doku, yavaşça sönerek biter |

### 🎧 SUNO / UDIO PROMPTU (Part B)

```
[Genre: Minimal Cinematic Score, Ambient Chamber, Sparse Post-Classical]
[Tempo: 58 BPM, constant, never accelerating]
[Mood: Cold, patient, resolved, quietly hopeful, unsentimental]
[Instruments: sub-bass drone, prepared piano, solo cello with audible bow
pressure, high violin harmonics, no percussion]

[Section A - Dark Corridors]
(35Hz sub-bass drone, continuous and unmoving)
(Single prepared piano notes with long widening gaps between them)
[No drums] [No percussion]

[Section B - The Dead Rows]
(Solo cello enters low, audible bow pressure, unhurried)
(Faint high violin harmonics appear above, thin and distant)

[Section C - False Hope]
(Prepared piano notes cluster closer together, intensity rises without
tempo change, then thins out again and fails)

[Section D - The Storm]
(Everything drops away except the sub-bass drone. No melody. Two full
minutes of near-emptiness compressed into thirty seconds)

[Section E - Silence]
[No instruments] [Complete silence] [No sound]

[Section F - The Seed Case]
(Solo cello returns warm and full, joined by sustained high violin
harmonics — the only moment both are present)

[Section G - Held]
(High violin harmonics alone, sustained, slowly thinning)
[Ending: harmonics fade to nothing, no resolution chord, no final swell]
```

### 🎵 GOOGLE FLOW (LYRIA) ZAMAN KODLU PROMPT — Part B

```
STRUCTURE (2:00 total, covering film time 2:09 - 4:09):

0:00 - 0:30 [DARK CORRIDORS]: 35Hz sub-bass drone, sparse prepared piano
             single notes with widening gaps. Cold, patient, no melody yet.
0:30 - 0:50 [THE DEAD ROWS]: Solo cello enters in low register with
             audible bow pressure. Thin high violin harmonics above.
0:50 - 1:00 [FALSE HOPE]: Piano notes cluster and intensify without any
             tempo change, then thin out and fail. No resolution.
1:00 - 1:15 [THE STORM]: All instruments drop away. Sub-bass drone alone.
1:15 - 1:35 [SILENCE]: COMPLETE SILENCE. No instruments, no drone, no
             sound of any kind for twenty seconds.
1:35 - 1:50 [THE SEED CASE]: Solo cello returns warm and full, joined by
             sustained high violin harmonics — the only full moment.
1:50 - 2:00 [HELD]: High violin harmonics alone, sustained, thinning
             slowly to nothing. No resolution chord, no swell, no ending.

TEMPO: 58 BPM constant throughout. Never accelerates.
KEY: D minor, unresolved — never reaches a tonic cadence.
REFERENCE: Jóhannsson "Arrival" meets Hildur Guðnadóttir sparse cello.
TAGS: [Instrumental] [No Vocals] [No Percussion] [Sparse] [Unresolved]
```

---

# 📊 FİLM ÖZET TABLOSU

```
BAŞLIK:        LOW POWER — Düşük Güç
FORMAT:        16:9 yatay, 3-5 dakika formatı
SÜRE:          Hook 9s + 24 sahne × 10s = 249 saniye = 4 dakika 09 saniye
SAHNE:         25 (Part A: 13, Part B: 12)
VİRAL ARA:     4 (S5, S14, S19, S23)
DİYALOG:       5 sahne (S2, S10, S11, S20, S22) — 20 sahne sessiz
               Hepsi tek konuşmacı kayıt. Karşılıklı diyalog YOK.
KARAKTER:      1 (Dr. Selin Aras — promptlarda isimsiz, Ders 34)
MEKAN:         Mars, Hellas İstasyonu, Sol 187
RENK:          Kızıl-kahve (Mars) + Yeşil (sera). Üçüncü renk YOK.
               Mavi sadece S14'te (gün batımı) — bilimsel gerçek.
KAPAK ADAYI:   S14 — mavi gün batımı
İMZA SAHNE:    S20 — anahtarın çevrilmesi
TEMA:          "Bir şeyin yaşaması için senin yaşaman gerekmiyor."

ÜRETİM:        25 imaj + 25 video
MALİYET:       25 × 8s × ~$0.15 ≈ $30 (sıfır retry) / gerçekçi ~$90
KLİP SÜRESİ:   Promptlar 10s yazıldı. Veo native 8s — ya 8s+extend,
               ya da ilk satırı "8 seconds" yapıp son beat'i sil
               (film 3:21'e iner, yine 3-5 dk formatında).
```

---

# ⚠️ BU FİLMİN DÖRT KRİTİK ÜRETİM RİSKİ

```
1. MAVİ GÖKYÜZÜ (tüm dış sahneler) — EN YÜKSEK RİSK
   Model "gezegen yüzeyi" = mavi gök öğrenmiş. Her dış promptta üç kez
   tekrarlandı. S14 ise ÇİFT tehlike: orada mavi VAR ama sadece güneşin
   çevresinde, gerisi kahve. Model bunu Dünya gün batımına çevirmeye
   çalışacak — o promptta "NO EARTH SUNSET" ayrıca yazıldı.

2. DÜNYA FIRTINASI (S17, S18)
   Çırpınan kumaş, savrulan karakter, uçuşan enkaz, uğultu — hepsi
   yanlış. Atmosfer %0.6. S17'de ayrıca "NO TORNADO", S18'de
   "NO EARTH SANDSTORM" negatifleri var.

3. TOZUN YÖNÜ (S6, S7, S17)
   Serinin diğer filmleri vakumda — orada toz uzaya gider. Burada TERSİ:
   toz düşer ve yere oturur. Filmin trajedisi tam olarak budur.

4. EKİPMAN DURUMU (Ders 37)
   Film boyunca 3 durum var: suitsiz iç (S1-S3, S8-S16, S20),
   suitli dış (S4-S7, S14, S17-S18), suitli iç (S21-S24).
   TEK ekranda geçiş S21'de. Diğer 24 sahnede durum SABİT ve her
   promptta açıkça beyan edildi.
```
