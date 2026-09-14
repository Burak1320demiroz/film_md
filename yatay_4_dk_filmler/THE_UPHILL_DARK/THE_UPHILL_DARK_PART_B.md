# 🟠 THE UPHILL DARK — Yokuş Yukarı Karanlık | PART B

## AI Production Bible — Self-Contained Prompts
### PART B: Sahne 13-24 (12 sahne) | 16:9 Yatay | 2:09 – 4:09
### _"Son on altı metre kartuşla değil, bırakmakla kapanır."_

---

## ⚠️ PART B ÜRETİM NOTLARI

```
① BIBLE'LAR PART A'DADIR — ama promptlar yine SELF-CONTAINED'dır.
   Hiçbir prompt "[BIBLE'a bak" demez; her blok tek başına çalışır.
   Çapa blokları ve sayısal kilitler: THE_UPHILL_DARK_PART_A.md · Bölüm 1.

② ÜRETİM SIRASI — PART B'nin iki kapısı önce koşulur:
   KAPI 1 = S19 (yük atma)  ·  KAPI 2 = S21 (temas)
   İkisi de temiz çıkmadan PART B'nin kalan 10 sahnesi üretilmez.

③ DURUM BLOKLARI [D84 ②]:
   blok 4: S13-S18  (2 → 0 kartuş · yük DOLU · yanal dönüş 46 → 12 m
                     bu blokta biter — kayış 2:25–2:47, freni S16'da)
   blok 5: S19-S24  (0 kartuş · yük YOK · kayış gevşek · standoff 12 m)
   ⛔ Blok sınırı S19'dadır ve tek yönlüdür: S19'dan sonraki hiçbir
      karede karot tüpü YOKTUR. Bloklar aynı oturumda üretilir.

④ KONUM DEFTERİ (yuvaya kalan mesafe, sahne başında):
   S13 56 m · S14 56 m · S15 51 m · S16 37 m · S17 22 m · S18 16 m
   S19 16 m · S20 14 m · S21 4 m · S22-S24 0 m (kenetli)

⑤ REPLİK YOK. Anlaşma iki kez EL İŞARETİYLE olur (S13 ve S19) ve
   işaretin ANLAMI hiçbir yere yazılmaz — ekranda yazı 0.0 saniyedir.
```

### ⚠️ UZUNLUK BANDI — BİLİNÇLİ SAPMA

```
prompt_kontrol.py (17.08.2026, turkuaz kaplama turu sonrası): ⛔ 0 BLOCK ·
⚠️ FIX (yalnız uzunluk) — video 2.528-3.909 · tavan 4.300, hepsi altında. Gerekçe
ve İLK RED PROTOKOLÜ: THE_UPHILL_DARK_PART_A.md · §ÜRETİM NOTLARI.

⚠️ Dosyanın en uzun promptu S19'dur (3.909) ve aynı zamanda KAPI 1'dir —
   yani ilk üretilecek karedir. Red gelirse ilk hamle D89 mühür bloğunu
   tek cümleye indirmek, ikinci hamle NEGATIVE'i yarıya kısmaktır;
   TEK MÜHÜR SAYIMI cümlesi tamamen silinmez (S19 bir ÇIKARMA sahnesidir
   ve o cümle olmadan model en yakın mührü — kaskı — açar).
```

---

# 🎬 PROMPTLAR (PART B: S13-S24)

> ⚡ **Her prompt tamamen bağımsızdır.** Sadece istediğiniz sahnenin
> 📸 veya 🎥 bloğunu kopyalayıp yapıştırın.

---

## 🎬 SAHNE 13 (S13) — ARİTMETİK

> 🎯 **REFERANS:** **RE** p4 ⭐ (iki yüz yakın — klon kapısı) · **RD** p1 (arkada pencere + omurga)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin, tight two-shot from ahead. Exactly 2 human figures
in frame — this film has exactly 2 humans in total.

SCENE: Two helmeted heads and shoulders side by side, seen from ahead and
slightly above. At screen-left the pilot, a lean 54-year-old man, 1.75
metres, weathered pale olive skin with visible pore texture, a THICK GREY
MOUSTACHE and no beard, close-cropped grey hair receding at the temples,
and a 2-centimetre shiny burn scar on the BONE OF HIS RIGHT CHEEK below the
outer corner of his right eye; the rest of his face is completely unmarked.
At screen-right the engineer, a compact 33-year-old woman, 1.58 metres,
very dark brown skin, her head COMPLETELY SHAVED to 2 millimetres of
stubble, a broad flat nose, and a pale 4-centimetre surgical line along the
BONE OF HER RIGHT JAW; the rest of her face is completely unmarked. Both
wear matte BURNT-ORANGE hard-shell pressure suits with crisp recessed seams
and machined aluminium collar rings — his shoulder band charcoal grey, hers
bone white. Both helmets are sealed: single curved optically clear panes in
2-centimetre brushed-metal frames, each frame's lower seal ring visible at
the collar, one thin specular line along each pane's upper edge, both faces
fully readable through the glass. His gloved right hand is raised into
frame between them, held flat and open with the palm facing up.

ENVIRONMENT: Unpressurised cabin in hard vacuum, 0.220 g of thrust
acceleration. Behind them the wide curved window shows the ship's graphite
truss and, high at the top edge, a small pool of warm-white light.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.2 metres ahead of the heads.
Dim amber console light from below; a faint warm-white spill from the
window above; absolute black between them.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no duplicate, no clone, no reflected face in either visor.
Pilot LEFT, engineer RIGHT. The two are unmistakably different people:
different height, skin, head and face. Both backs flat, no back-mounted
unit; both visors optically clear, zero tint, zero mirror coating, faces
fully readable. Scars stay on his right cheekbone and her right jawline. 0%
bloom, no glow filter, no soft focus. No readable text, letters, digits,
numbers or HUD graphics. No subtitles, no title card, no watermark.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 2.2 metres ahead of two seated helmeted heads inside a
small spacecraft cabin, no camera movement. Exactly 2 human figures in
frame — this film has exactly 2 humans in total.

SCENE: Two helmeted heads and shoulders side by side, seen from ahead and
slightly above. At screen-left the pilot, a lean 54-year-old man with a
THICK GREY MOUSTACHE, close-cropped grey hair and a 2-centimetre shiny burn
scar on the BONE OF HIS RIGHT CHEEK; at screen-right the engineer, a
compact 33-year-old woman, very dark brown skin, her head COMPLETELY SHAVED
to 2 millimetres of stubble, with a pale 4-centimetre surgical line along
the BONE OF HER RIGHT JAW. Both wear matte BURNT-ORANGE hard-shell pressure
suits with machined collar rings — his shoulder band charcoal grey, hers
bone white. Both helmets are sealed: single curved optically clear panes in
2-centimetre brushed-metal frames, seal rings visible at both collars, both
faces fully readable through the glass. Behind them the window shows the
ship's graphite truss and a small pool of warm-white light high at the top
edge.

TIMELINE:
0.0s — Both faces are still, looking up and out of frame at the light
above. Neither speaks; no mouth moves at any point in this shot.
2.5s — He raises his gloved right hand into the space between them, held
flat and open with the palm up, and holds it there.
5.0s — He closes the hand into a fist, slowly and deliberately, and lowers
it out of frame.
7.0s — She turns her head to him. He does not turn to her. Her jaw sets;
her eyes drop once and come back up.
10.0s — Both faces return to the light above. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady,
with the close sound of two people breathing inside sealed helmets. No
voice, no radio, no music, no dialogue of any kind.

PHYSICS: 0.220 g of thrust acceleration; the raised arm has weight and
moves at ordinary human speed. Real time, no slow motion.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no clone,
no reflected face in either visor, no autonomous reflection. Pilot LEFT,
engineer RIGHT — never swapped. The two remain unmistakably different
people; both faces keep identical bone structure throughout — no morphing,
no feature drift. Scars stay on his right cheekbone and her right jawline.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; neither opens, lifts or is removed. No mouth moves and
no one speaks — no lip movement, no talking face, no invented speaker. The
hand keeps rigid anatomy — exactly five fingers, no extra digits, no
merging with the helmet or console. 0% bloom, no glow filter, no soft
focus. No readable text, letters, digits, numbers or HUD graphics. No
subtitles, no captions, no dialogue text, no title card, no watermark.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 14 (S14) — SON ÇİFT

> 🎯 **REFERANS:** **RD** p1 · p3 (seçici BEŞİNCİ dişte) · **RE** p1 · p2 · **RB** p4 (pencerenin üst kenarında kolun altı)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats:
the pilot in the LEFT seat, a lean 54-year-old man with a thick grey
moustache; the engineer in the RIGHT seat, a compact 33-year-old woman with
a completely shaved head. Both strapped into tight five-point harnesses in
matte BURNT-ORANGE hard-shell pressure suits with crisp recessed seams,
graphite flex-weave at the joints and machined aluminium rings at the
shoulders — his shoulder bands charcoal grey, hers bone white, a
12-centimetre machined tool block on HER LEFT FOREARM only. Both backs
flat, both helmets sealed, each visor a single curved optically clear pane
in a 2-centimetre brushed-metal frame with its lower seal ring visible at
the collar. Her gloved right hand grips the machined six-detent selector at
the console's left cheek, its stubby arm standing at the FIFTH detent.
Through the wide curved window above them: the ship's open graphite truss
spine filling the upper frame, and near the top edge the underside of a
lattice boom with a small pool of warm-white light beneath it. A
40-centimetre brass lanyard hangs from the window frame, straight down and
taut.

ENVIRONMENT: Unpressurised cabin in hard vacuum, 0.220 g of thrust
acceleration. Fine grit rests still in the floor seams.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Dim amber
console segments underlight both figures; a faint warm-white spill from
above through the window; hard starlight from screen-left.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable. Exactly SIX detents on the selector. The lanyard hangs straight
down. 0% bloom, no glow filter, no soft focus. No readable text, letters,
digits, numbers, icons or screen graphics. No holograms. No subtitles, no
title card, no watermark. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache and a
2-centimetre burn scar on the bone of his right cheek; the engineer in the
RIGHT seat, a compact 33-year-old woman with a completely shaved head and a
pale 4-centimetre line along the bone of her right jaw. Both strapped into
tight harnesses in matte BURNT-ORANGE hard-shell pressure suits — his
shoulder bands charcoal grey, hers bone white, a 12-centimetre tool block
on HER LEFT FOREARM only. Both backs FLAT, both helmets sealed: each visor
a single curved optically clear pane in a 2-centimetre brushed-metal frame,
its seal ring visible at the collar, both faces fully readable. Her gloved
right hand is on the six-detent selector. Through the window above them,
the ship's truss spine and, near the top edge, the underside of a lattice
boom with a small pool of warm-white light beneath it. A brass lanyard
hangs from the window frame, straight down.

TIMELINE:
0.0s — Stillness. Her hand rests on the selector arm at the fifth detent.
3.0s — Her glove tightens on the arm. The pilot's head turns to her once
and back.
6.0s — She presses the arm down. A hard white jet fires from the base ring
below frame and holds.
6.2s — Both bodies settle 2 centimetres deeper into the padding; the
harness webbing goes taut across both chests; the lanyard stiffens; grit in
the floor seams jumps once and resettles.
9.5s — Through the window the truss spine has begun sliding steadily
downward.
10.0s — The jet is still burning as the shot ends. Hold.

AUDIO: One continuous low hull-conducted engine drone. A hard double knock
and a sustained hiss carried through the frame, still running as the shot
ends. No voice, no music.

PHYSICS: The main motor is fixed thrust and cannot be throttled; the
cartridge adds thrust for four seconds, raising acceleration from 0.220 g
to 0.260 g, so everyone briefly weighs more and the capsule leaves at 1.6
metres per second relative to the ship.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; no helmet opens, lifts or is removed. Exactly SIX
detents; no case is ejected in this shot. Both faces keep identical bone
structure
— no morphing. The lanyard never floats, drifts or swings sideways; nothing
in the cabin floats. The jet is a straight sharp cone — no billowing, no
smoke, no sparks, no explosion. 0% bloom, no glow filter, no soft focus. No
readable text, letters, digits, numbers, icons or screen graphics. No
subtitles, no dialogue text, no title card, no watermark. Photorealistic
with 35mm film grain.
```

---

## 🎬 SAHNE 15 (S15) — OMURGA

> 🎯 **REFERANS:** **RA** p4 (omurga akışı) · **RB** p4 (yanaşma kolu bağlamda) · **RC** p1 · p2 (raf: 1 dolu / 5 boş)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Exterior view in
vacuum, 35 metres from a small spacecraft climbing beside a huge hull.
Exactly 2 human figures exist in this film and both are sealed inside the
capsule — no figure is visible in frame.

SCENE: The ship's open hexagonal graphite truss spine fills the right half
of the frame from top to bottom — machined grey members with bolted nodes,
cable runs clipped along them, clean machined joints, the black
depth of the lattice showing between the members. At screen-left, about
forty metres out from the hull and small against it: the ferry capsule — a 5.2-metre
truncated cone standing nose-UP, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush rivet rows, a 60-centimetre docking probe
with three alignment vanes on its nose pointing at the TOP of frame, one
wide curved window in the upper cone, forty white core tubes under a
BURNT-ORANGE strap on its starboard side, four scorched nozzles in the base
ring, and a six-socket cartridge rack low on its port flank with FIVE
sockets empty and scorched and ONE still loaded. Near the top of frame, the
underside of a 12-metre lattice berth boom crosses the shot, a pool of
warm-white light beneath its outer pad.

ENVIRONMENT: Hard vacuum, absolute black sky, sharp stars, 0.220 g of
thrust acceleration.

CAMERA & LIGHT: 50mm spherical lens, fixed 35 metres out. Hard parallel
starlight from screen-left rakes the truss members and the capsule's flank;
the lattice throws a set of razor-sharp black shadow bars across the hull
behind it. The warm-white pool above is the only other light.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible outside
the hull. Exactly SIX cartridge sockets with exactly FIVE empty, exactly
FOUR base nozzles, exactly FORTY core tubes, exactly ONE probe with THREE
vanes. 0% bloom, no glow filter, no lens flare, no soft focus. No readable
text, letters, digits, numbers, insignia or watermark. No subtitles, no
title card. No atmospheric haze, no light scattering in vacuum.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 35 metres off a small spacecraft in vacuum, no camera
movement. Exactly 2 human figures exist in this film and both are sealed
inside the capsule — no figure is visible in frame.

SCENE: The ship's open hexagonal graphite truss spine fills the right half
of frame from top to bottom — machined grey members with bolted nodes,
cable runs clipped along them, the black depth of the lattice showing
between the members. At screen-left, about forty metres out from the hull
and drifting slowly closer to it: the ferry
capsule, a 5.2-metre truncated cone standing nose-UP, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams, a 60-centimetre docking
probe with three alignment vanes on its nose pointing at the TOP of frame,
one wide curved window in the upper cone, forty white core tubes under a
BURNT-ORANGE strap on its starboard side, and a six-socket cartridge rack
with FIVE sockets empty and ONE loaded. Near the top of frame the underside
of a 12-metre lattice berth boom crosses the shot, a pool of warm-white
light beneath its outer pad.

TIMELINE:
0.0s — The capsule climbs steadily up-frame at a slow walking pace, its
nose and probe pointing at the top of frame throughout; it neither pitches
nor rolls.
0.5s — A spent white cartridge case, punched out a moment ago, tumbles
down past the capsule, already fast, and leaves the bottom of frame.
3.0s — The truss members slide down past it one after another, each bolted
node passing at the same steady rate, their shadow bars sweeping down
across the hull behind.
7.0s — The warm-white pool at the top of frame is measurably larger and
lower than it was, and a faint warm rim appears along the top of the
capsule's probe.
10.0s — Still climbing at exactly the same rate. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
nothing else — vacuum carries no sound between the hulls. No voice, no
music.

PHYSICS: The capsule is climbing at a constant 1.6 metres per second
relative to the ship after its cartridge burn, and is also drifting slowly
inboard at about one metre per second — the long slide that will end
beneath the berth. The spent case is unpowered and falls at 2.16 metres per
second squared. 0.220 g of thrust acceleration throughout.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible outside the hull. Exactly SIX sockets
with FIVE empty, FOUR base nozzles, FORTY core tubes. The capsule only
rises up-frame — no descent, no drift toward the exhaust below, no
direction reversal, no pitch, no roll, no mirrored composition. No
cartridge fires in this shot; the single falling case is already spent and
only falls. 0% bloom, no glow
filter, no lens flare, no soft focus. No readable text, letters, digits,
numbers, insignia or watermark. No subtitles, no title card. No atmospheric
haze. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 16 (S16) — GERİ İÇERİ

> 🎯 **REFERANS:** **RD** p1 (kordon yana yatar) · **RE** p1 · p2 · **RA** p4 (pencerede yakın küre + cıvatalı düğümler)
>
> ⚠️ İÇ sahne: kapsül dışı (RC) kadraja girmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats:
the pilot in the LEFT seat, a lean 54-year-old man with a thick grey
moustache; the engineer in the RIGHT seat, a compact 33-year-old woman with
a completely shaved head. Both strapped into five-point harnesses in matte
BURNT-ORANGE hard-shell pressure suits with crisp recessed seams and
machined aluminium rings at the shoulders — his shoulder bands charcoal
grey, hers bone white, a 12-centimetre machined tool block on HER LEFT
FOREARM only. Both backs flat, both helmets sealed, each visor a single
curved optically clear pane in a 2-centimetre brushed-metal frame with its
lower seal ring visible at the collar. His gloved left hand is closed
around a short machined translation grip on the console's left edge.
Through the wide curved window above them the ship's hull is close and
filling most of the glass: bolted truss nodes and the lower curve of a polished bright-metal propellant sphere, close enough that individual fastener heads and turquoise accent lines read. The 40-centimetre brass lanyard hangs from the window
frame, dead straight DOWNWARD and taut — the capsule is coasting sideways
at constant speed, so nothing swings.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust
acceleration; a slow steady sideways coast toward the hull.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Dim amber
console segments underlight both figures; a growing pool of warm-white
light from above through the window's upper edge; hard starlight from
screen-left through the last clear corner.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable. The lanyard hangs straight down and taut — never floating, never
loose, never coiled. 0% bloom, no glow filter, no soft focus. No readable
text, letters, digits, numbers, icons or screen graphics. No holograms. No
subtitles, no title card, no watermark. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache and a
2-centimetre burn scar on the bone of his right cheek; the engineer in the
RIGHT seat, a compact 33-year-old woman with a completely shaved head and a
pale 4-centimetre line along the bone of her right jaw. Both strapped into
harnesses in matte BURNT-ORANGE hard-shell pressure suits with machined
rings at the shoulders — his shoulder bands charcoal grey, hers bone white,
a 12-centimetre tool block on HER LEFT FOREARM only. Both backs flat, both
helmets sealed, each visor a single curved optically clear pane in a
2-centimetre brushed-metal frame with its seal ring visible at the collar.
His gloved left hand is closed around a short machined translation grip on
the console's left edge. Through the window above them the ship's hull is
close: bolted truss nodes and the lower curve of a polished bright-metal propellant sphere. A brass lanyard hangs from the window frame.

TIMELINE:
0.0s — The hull in the window is already sliding slowly toward screen-left
and growing — the long inboard drift begun during the climb is ending its
run. The lanyard hangs dead vertical.
3.0s — Fastener heads, the turquoise accent stripe and the polished cradle ring on the sphere come into clear detail. Nothing outside rises or falls.
5.5s — His gloved left hand tips the translation grip. Small manoeuvring
jets rattle outside the frame; the lanyard swings 20 degrees toward
screen-left and holds there, taut, while the slide outside slows.
8.5s — The rattle stops; the lanyard settles dead vertical in two small
decaying movements. The hull is stationary, filling the window directly
overhead.
10.0s — Hold.

AUDIO: One continuous low hull-conducted engine drone, plus a long flat
rattle of small thrusters carried through the frame in the last third of
the shot. No voice, no music.

PHYSICS: The capsule has been drifting inboard at about one metre per
second since the last climb began; only the braking pulse happens in this
shot, ending a 34-metre slide directly beneath the berth. There is no
gravity component across the thrust axis, so the drift costs no height.
Vertical acceleration stays at 0.220 g throughout.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; no helmet opens or is removed. The view outside moves
only sideways — nothing outside rises or falls in this shot. The two hulls
never touch, clip or intersect. The lanyard swings only sideways and stays
taut — never floating, never slack, never coiled, never drifting in zero
gravity. Nothing in the cabin floats. 0% bloom, no glow filter, no soft
focus. No readable text, letters, digits, numbers, icons or screen
graphics. No holograms. No subtitles, no dialogue text, no title card, no
watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 17 (S17) — SON KARTUŞ

> 🎯 **REFERANS:** **RC** p2 (kartuş rafı makro — boş yuva içi, ejektör çubuğu, is)
>
> ⚠️ Bu bir DIŞ detay çekimidir; kabin sayfası (RD) yüklenmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Tight exterior
detail of a small spacecraft's flank in vacuum. Exactly 2 human figures
exist in this film and both are sealed inside this capsule — no figure is
visible in frame.

SCENE: A tight view of the port flank of the ferry capsule from 4 metres —
matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush
rivet rows, its ceramic panels clean and well kept along every edge. Filling the centre of
the frame: the cartridge rack, a machined frame holding SIX cylindrical
sockets in one horizontal row, each 0.3 metres across, with a hinged
retaining bar across them. FIVE sockets are EMPTY, showing their dark
machined interiors, the ejector rod at the back of each and the scorching
around each mouth; the SIXTH still holds a white cylindrical cartridge
seated flush. Above the rack, the lower curve of the hull rises out of
frame; below it, the edge of the base ring and one scorched nozzle throat.
In the background at screen-right, 12 metres away and softly out of focus,
the ship's hull: bolted truss members and clean white quilted insulation.

ENVIRONMENT: Hard vacuum, absolute black sky in the gap between the hulls,
0.220 g of thrust acceleration.

CAMERA & LIGHT: 85mm spherical lens, fixed 4 metres off the flank, shallow
depth with the rack sharp. Hard parallel starlight from screen-left picks
out every socket rim and leaves the interiors in absolute black; a faint
warm-white spill from high above.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly SIX sockets in one row, exactly FIVE empty and ONE
loaded — no seventh socket, no missing socket. 0% bloom, no glow filter, no
lens flare, no soft focus. No readable text, letters, digits, numbers,
labels, insignia or watermark on the rack, the hull or anywhere else. No
subtitles, no title card. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 4 metres off the flank of a small spacecraft in vacuum,
no camera movement. Exactly 2 human figures exist in this film and both are
sealed inside this capsule — no figure is visible in frame.

SCENE: A tight view of the ferry capsule's port flank — matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush rivet rows, its ceramic panels clean and well kept along every edge. Filling the centre of frame: the
cartridge rack, a machined frame holding SIX cylindrical sockets in one
horizontal row with a hinged retaining bar across them. FIVE sockets are
empty, showing dark machined interiors, ejector rods and scorched mouths;
the SIXTH still holds a white cylindrical cartridge seated flush. Above,
the hull curves out of frame; below, the base ring and one scorched nozzle
throat. In the background at screen-right, 12 metres away and softly out of
focus, the ship's hull.

TIMELINE:
0.0s — Stillness. Five dark sockets and one white cartridge.
1.5s — The retaining bar snaps back on its hinge. Two short hard white jets
fire from ports high above the frame, out of shot, and a fine shudder runs
through the hull.
2.0s — The whole frame lightens by a few millimetres of settle as the craft
loses weight; a loose scrap of tape on the rack frame lifts and lies back
down.
5.5s — The jets cut out. The sixth cartridge is fired dry: its case is
punched out of the socket sideways, clears the hull, and immediately begins
falling toward the bottom of frame, tumbling and accelerating away.
7.0s — SIX empty sockets in a row, all scorched. Nothing is left in the
rack.
10.0s — Hold on the empty rack.

AUDIO: One continuous low hull-conducted engine drone. The metallic snap of
the retaining bar, then a hard double knock and a four-second hiss carried
through the hull, then a single hollow clack as the case is ejected. No
voice, no music.

PHYSICS: The retro cartridge pushes against the direction of travel for
four seconds, dropping net acceleration from 0.220 g to 0.179 g and killing
the last 1.6 metres per second of climb. The ejected case is unpowered and
falls away at 2.16 metres per second squared — 1.1 metres in the first
second.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. No figure visible anywhere. Exactly SIX sockets, exactly ONE case
ejected in this shot, ending with exactly SIX empty sockets. The falling
case accelerates continuously downward and never floats, hovers, freezes or
drifts sideways. No jet is visible inside this frame — no billowing, no
smoke, no sparks, no explosion, no debris field. 0% bloom, no glow filter,
no lens flare, no soft focus. No readable text, letters, digits, numbers,
labels, insignia or watermark anywhere. No subtitles, no title card.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 18 (S18) — ON ALTI METRE

> 🎯 **REFERANS:** **RB** p1 (kollar açık, 16 m alttan) · **RC** p1 (gövde + yük)
>
> ⚠️ Durum tek panelde yok: gövde/yük p1'den, ALTI BOŞ YUVA dili p3'ten alınır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Deep space, 40
metres out from a docking berth on a huge ship's flank. Exactly 2 human
figures exist in this film and both are sealed inside the small capsule —
no figure is visible in frame.

SCENE: In the upper half of frame, a 12-metre lattice berth boom stands out
from the ship's flank at screen-right, carrying a flat structural pad at
its outer end. Set into the UNDERSIDE of that pad and facing straight down:
a 2.0-metre machined capture ring with a 40-centimetre conical throat and
THREE curved capture arms standing fully open at 120-degree spacing, ringed
by a continuous recessed warm-white light channel that lays a clean pool of
3400K light straight down into empty space. Sixteen metres directly below
that pool, alone in the black: the ferry capsule — a 5.2-metre truncated
cone standing nose-UP, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe, its
60-centimetre docking probe with three alignment vanes pointing straight up
at the ring, one wide curved window in the upper cone with two helmeted
heads dimly visible behind the glass, forty white core tubes under a
BURNT-ORANGE strap on its starboard side, and a six-socket cartridge rack
with ALL SIX sockets empty and scorched. The gap between the probe tip and
the ring is the whole subject of the frame.

ENVIRONMENT: Hard vacuum, absolute black sky, sharp stars, 0.220 g of
thrust acceleration.

CAMERA & LIGHT: 24mm spherical lens, fixed 40 metres out, the boom above
and the capsule below both in frame with the empty gap between them. The
warm-white channel lights the top of the capsule's probe and nose; hard
starlight from screen-left; absolute black everywhere else.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible outside
the hull. Exactly THREE capture arms, all open; exactly SIX cartridge
sockets, all empty; exactly FORTY core tubes; exactly ONE probe with THREE
vanes. The probe and the ring do not touch — a clear 16-metre gap. The
light channel is a thin recessed line, not a lamp and not a halo. 0% bloom,
no glow filter, no lens flare, no soft focus. No readable text, letters,
digits, numbers, insignia or watermark. No subtitles, no title card.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 40 metres out from a docking berth in vacuum, no camera
movement. Exactly 2 human figures exist in this film and both are sealed
inside the small capsule — no figure is visible in frame.

SCENE: In the upper half of frame, a 12-metre lattice berth boom stands out
from the ship's flank at screen-right, carrying a flat structural pad at
its outer end with a 2.0-metre machined capture ring set into its
UNDERSIDE, a 40-centimetre conical throat at its centre, THREE curved
capture arms standing fully open at 120-degree spacing, and a continuous
recessed warm-white light channel laying a clean pool of 3400K light
straight down into empty space. Sixteen metres directly below that pool,
alone in the black: the ferry capsule, a 5.2-metre truncated cone standing
nose-UP, its 60-centimetre docking probe pointing straight up at the ring,
one wide curved window with two helmeted heads dimly visible behind the
glass, forty white core tubes under a BURNT-ORANGE strap, and a cartridge
rack with ALL SIX sockets empty and scorched.

TIMELINE:
0.0s — Nothing moves anywhere in frame. The capsule hangs exactly 16 metres
below the ring, matched to the ship, neither rising nor falling.
4.0s — Behind the window, one helmeted head turns to the other. Nothing
else in the frame changes at all.
7.0s — A single fleck of ice falls down the gap past the capsule,
accelerating, and leaves the bottom of frame — the only motion in ten
seconds.
10.0s — The gap is still exactly 16 metres. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
nothing else. No voice, no music, no cartridge, no thruster.

PHYSICS: The capsule's fixed-thrust motor exactly matches the ship's 0.220
g, so the 16-metre gap does not change by a single centimetre. With no
cartridges left, nothing aboard can change that. The falling fleck is
unpowered and accelerates away at 2.16 metres per second squared.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible outside the hull. Exactly THREE capture
arms and all THREE stay open — none closes or folds. Exactly SIX empty
sockets, FORTY core tubes, ONE probe. The capsule does not rise, fall,
pitch, roll or drift at any point in this shot, and the 16-metre gap never
changes. No jet, no cartridge, no thruster fires anywhere. The light
channel is a thin recessed line — not a lamp, not a halo, never glowing.
The falling fleck accelerates continuously and never hovers or freezes. 0%
bloom, no glow filter, no lens flare, no soft focus. No readable text,
letters, digits, numbers, insignia or watermark. No subtitles, no title
card. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 19 (S19) — 🎬 VİRAL #3 · ⭐ MERKEZİ SEÇİM: BIRAKMAK

> 🎯 **REFERANS:** **RC** p1 → p3 ⭐ (dolu → boş kızak: filmin bedeli) · **RC** p4 (kayış tokası) · **RD** p4 (turuncu kol + kordon) · **RE** p2 (mühendis)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin, angled across from the left seat toward the right.
Exactly 2 human figures in frame — this film has exactly 2 humans in total.

SCENE: The camera looks across the cabin past the left shoulder of the
pilot — a lean 54-year-old man with a thick grey moustache, strapped into
his harness at screen-left, dark and mostly in silhouette. In the centre
and right of frame, the engineer in the RIGHT seat: a compact 33-year-old
woman, very dark brown skin, her head COMPLETELY SHAVED to 2 millimetres of
stubble, a pale 4-centimetre surgical line along the BONE OF HER RIGHT JAW.
Both wear matte BURNT-ORANGE hard-shell pressure suits with crisp recessed
seams and machined aluminium rings at the shoulders and wrists — hers with
bone-white shoulder bands and a 12-centimetre machined tool block on HER
LEFT FOREARM. Both backs flat; both helmets sealed, each visor a single
curved optically clear pane in a 2-centimetre brushed-metal frame with its
lower seal ring visible at the collar, her face fully readable through the
glass. Both her gloved hands are closed around the BURNT-ORANGE two-handed
lever on the console's right cheek, its hinged steel safety collar folded
back and clipped off. Above and behind her, the lower right corner of the
wide curved window shows the top row of the cargo rack outside: eight
sealed white core tubes and the taut burnt-orange strap across them. Higher
in the same window, the ship's hull and a pool of warm-white light.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust acceleration.

CAMERA & LIGHT: 35mm spherical lens, fixed at the pilot's shoulder height.
Dim amber console light from below on her face; warm-white spill from the
window above; absolute black in the cabin corners.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, her face fully
readable. Both her hands keep rigid anatomy on the lever — five fingers per
hand, no extra digits, no merging with the metal. Exactly ONE orange lever,
exactly FORTY core tubes outside. 0% bloom, no glow filter, no soft focus.
No readable text, letters, digits, numbers, icons or screen graphics. No
subtitles, no title card, no watermark. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera at shoulder height inside a small spacecraft cabin,
looking across from the left seat toward the right, no camera movement.
Exactly 2 human figures in frame — this film has exactly 2 humans in total.

SCENE: At screen-left, dark and mostly in silhouette, the pilot strapped
into his harness — a lean 54-year-old man with a thick grey moustache. In
the centre and right of frame the engineer in the RIGHT seat: a compact
33-year-old woman, very dark brown skin, her head COMPLETELY SHAVED, a pale
4-centimetre surgical line along the BONE OF HER RIGHT JAW. Both wear matte
BURNT-ORANGE hard-shell suits, hers with bone-white shoulder bands and a
tool block on HER LEFT FOREARM. Both backs FLAT; both helmets sealed —
optically clear panes in brushed-metal frames, seal rings visible at the
collars, her face fully readable. On the console's right cheek stands a
BURNT-ORANGE two-handed lever, its safety collar folded back. Above and
behind her, the window's lower right corner shows the top row of the cargo
rack outside: eight sealed white core tubes under a taut burnt-orange
strap.

TIMELINE:
0.0s — She is looking up and to screen-right, at the tubes in the window
corner. She does not speak; no mouth moves at any point.
2.5s — She turns her head once to the pilot. He does not move and does not
turn his head. She turns back.
4.0s — Both her gloved hands close around the orange lever.
5.0s — She pulls it through its full travel. Outside in the window corner
the burnt-orange strap whips open and away, and the eight visible tubes
drop straight down out of the window in the same instant, gone.
5.4s — Both bodies press 3 centimetres deeper into their seat padding as
the craft, now lighter, accelerates harder.
6.5s — In the window the ship's hull begins sliding steadily DOWNWARD, and
the pool of warm-white light comes down with it.
7.5s — At the frame's left edge the pilot's gloved hand twists a small
guarded lever; a thin locking wire snaps and the engine note drops one
clear step. The extra weight eases off both bodies.
10.0s — Her hands stay on the lever; the hull keeps sliding down the
glass. Hold.

AUDIO: One continuous low hull-conducted engine drone. A heavy mechanical
clack as the lever hits its stop, then a dull thud as the clamp releases;
at 7.5 seconds a thin wire-snap, and the drone drops one clear step in
pitch and stays there. No voice, no music.

PHYSICS: Releasing 900 kilograms lifts the capsule's acceleration to
0.277 g against the ship's unchanged 0.220 g: everyone gets heavier and
the craft begins to climb. Two seconds later the pilot's one-shot vent
trims the motor back to an exact match at the lighter mass, and the climb
settles to a constant 1.1 metres per second. The released tubes fall away
as one mass at 2.16 metres per second squared.

EXACTLY ONE SEAL OPENS IN THIS SHOT AND IT IS THE CARGO CLAMP OUTSIDE THE
HULL. Every other seal stays closed: both helmets on and locked, both
collar rings closed, all four gloves on. No bare skin appears at any
second.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face. Pilot LEFT, engineer RIGHT — never swapped. Both backs
flat, no back-mounted unit; visors optically clear, zero tint, zero mirror
coating. Her hands keep rigid anatomy on the lever — five fingers per
hand, no merging into the metal. The tubes leave together as one mass and
fall straight down, accelerating — never scattering, floating, hovering or
coming back. No fire, no sparks, no blast, no debris cloud: the clamp
released, nothing broke. Nothing in the cabin floats. 0% bloom, no glow
filter, no soft focus. No readable text, letters, digits, numbers or
icons. No subtitles, no title card, no watermark. Photorealistic with 35mm
film grain.
```

---

## 🎬 SAHNE 20 (S20) — HAFİF

> 🎯 **REFERANS:** **RD** p1 · **RE** p1 · p2 · **RB** p1 (pencereyi dolduran halka, kollar AÇIK) · **RC** p3 (pencere köşesinde BOŞ kızak)
>
> ⚠️ S19 sonrası: yük yok — RC p1 (yüklü) bu sahneden itibaren yüklenmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats:
the pilot in the LEFT seat, a lean 54-year-old man with a thick grey
moustache; the engineer in the RIGHT seat, a compact 33-year-old woman with
a completely shaved head. Both strapped into five-point harnesses in matte
BURNT-ORANGE hard-shell pressure suits with crisp recessed seams and
machined aluminium rings at the shoulders — his shoulder bands charcoal
grey, hers bone white, a 12-centimetre machined tool block on HER LEFT
FOREARM only. Both backs flat, both helmets sealed, each visor a single
curved optically clear pane in a 2-centimetre brushed-metal frame with its
lower seal ring visible at the collar. His gloved left hand rests on a
short machined translation grip at the console's left edge; at the
console's centre a small guarded lever stands with its locking wire
freshly snapped, the two bright wire ends hanging. Through the wide curved
window above them, close overhead: the underside of a flat structural pad, a 2.0-metre
machined capture ring facing straight down with THREE curved capture arms
standing open around it, and the warm-white light channel around its rim
filling the top of the window. In the window's lower right corner, the
cargo rack outside is EMPTY: bare moulded sockets and one slack
burnt-orange strap hanging loose.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust
acceleration — matched again since the vent.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Warm-white
light from the ring above now falls across both helmets and the console;
dim amber segments from below; the blue from beneath is gone.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable. Exactly THREE capture arms, all open. The cargo rack is empty —
not one core tube remains anywhere. 0% bloom, no glow filter, no soft
focus. No readable text, letters, digits, numbers, icons or screen
graphics. No holograms. No subtitles, no title card, no watermark.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache and a
2-centimetre burn scar on the bone of his right cheek; the engineer in the
RIGHT seat, a compact 33-year-old woman with a completely shaved head and a
pale 4-centimetre line along the bone of her right jaw. Both strapped into
harnesses in matte BURNT-ORANGE hard-shell pressure suits — his shoulder
bands charcoal grey, hers bone white, a 12-centimetre tool block on HER
LEFT FOREARM only. Both backs FLAT, both helmets sealed: each visor a
single curved optically clear pane in a 2-centimetre brushed-metal frame,
its seal ring visible at the collar, both faces fully readable. Through the
window above them, close overhead:
the underside of a flat structural pad, a 2.0-metre machined capture ring
facing straight down with THREE open capture arms, and a warm-white light
channel around its rim. In the window's lower right corner, the cargo rack
outside is empty, its slack burnt-orange strap hanging loose.

TIMELINE:
0.0s — The ring above is sliding steadily down toward them at a slow
walking pace, growing in the window. Both faces are up. Nothing else moves.
3.0s — The warm-white light from the ring reaches the console and both
visors; the amber segments pale inside it.
6.0s — The ring fills the top third of the window, still coming at the
same steady rate.
7.0s — His gloved left hand closes on the translation grip at the
console's left edge and eases it back. A long flat rattle of small
thrusters runs through the frame; both harness straps press forward a
fraction.
9.5s — The rattle stops. The ring's approach has slowed to a bare crawl.
10.0s — Hold, faces up, the warm light full on both visors.

AUDIO: One continuous low hull-conducted engine drone, and a flat dry
thruster rattle from 7.0 to 9.5 seconds. No voice, no music.

PHYSICS: The main motor was vented to an exact thrust match at the moment
the cargo fell away, so the capsule coasts up at a constant 1.1 metres per
second. The small thrusters burn the last of their axial budget to brake
that to 0.20 metres per second — a gentle deceleration of about 0.03 g.
Nothing else changes weight.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; no helmet opens or is removed. Exactly THREE capture
arms, all THREE open. The ring only ever approaches — no reversal, no drop
away, no drift sideways. The cargo rack stays empty: not one core tube
reappears. His hand keeps rigid anatomy on the grip — five fingers, no
merging with the metal. Nothing in the cabin floats. 0% bloom, no glow
filter, no soft focus. No readable text, letters, digits, numbers, icons or
screen graphics. No subtitles, no dialogue text, no title card, no
watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 21 (S21) — ⭐ DORUK: TEMAS

> 🎯 **REFERANS:** **RB** p1 → p2 ⭐ (temas: kollar açıktan kapalıya) · **RB** p3 (oluklar + konik boğaz) · **RC** p1 (burun + prob, üç kanat)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Tight exterior
view of a docking socket with a capsule's nose rising into it. Exactly 2
human figures exist in this film and both are sealed inside the capsule
below — no figure is visible in frame.

SCENE: Filling the upper two thirds of the frame, seen from 6 metres
below and slightly to one side: the underside of a flat structural pad
carrying a 2.0-metre machined capture ring that faces straight DOWN — its
brushed metal face worn pale and polished smooth by use, shallow guide
grooves cut radially into it, a 40-centimetre conical throat at its centre
with a chamfered scuffed lip and darkness inside. THREE curved capture arms
1.1 metres long stand open around the ring at 120-degree spacing, hinge
pins and actuator rods clearly visible. A continuous recessed warm-white
light channel runs around the rim at 3400K. Rising into the lower third of
frame: the nose of the ferry capsule — matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush rivet rows, its 60-centimetre docking
probe with THREE alignment vanes standing straight up, the probe tip 1.8
metres below the throat and dead centred on it. Behind everything, the
ship's hull and absolute black space with sharp stars.

ENVIRONMENT: Hard vacuum, 0.220 g of thrust acceleration carried by both
craft, closing rate 0.20 metres per second.

CAMERA & LIGHT: 50mm spherical lens, fixed 6 metres below the socket and
slightly to one side, so the ring, all three open arms and the rising nose
read together. The warm-white channel is the key light, falling straight
down onto the probe tip and the vanes; hard starlight from screen-left rims
the pad's edge; absolute black in the throat.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly THREE capture arms, all open in this frame; exactly ONE
probe with exactly THREE vanes; exactly ONE conical throat. Probe and ring
do not touch yet — a clear 30-centimetre gap, no contact, no overlap, no
clipping, no phasing, no merging. The light channel is a thin recessed
line, not a lamp and not a halo. 0% bloom, no glow filter, no lens flare,
no soft focus. No readable text, letters, digits, numbers, insignia or
watermark. No subtitles, no title card. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 6 metres below a docking socket in vacuum, no camera
movement. Exactly 2 human figures exist in this film and both are sealed
inside the capsule below — no figure is visible in frame.

SCENE: Filling the upper two thirds of frame, seen from below: the
underside of a flat structural pad carrying a 2.0-metre machined capture
ring facing straight DOWN — brushed metal worn pale and polished by use,
radial guide grooves, a 40-centimetre conical throat at its centre with a
chamfered scuffed lip. THREE curved capture arms 1.1 metres long stand open
around the ring at 120-degree spacing, hinge pins and actuator rods
visible, ringed by a continuous recessed warm-white light channel at 3400K.
Rising into the lower third of frame: the nose of the ferry capsule, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams, its 60-centimetre
docking probe with THREE alignment vanes standing straight up, dead centred
on the throat. Behind everything, the ship's hull and absolute black space.

TIMELINE:
0.0s — The probe rises toward the throat at the pace of a slow crawl, dead
centred, neither pitching nor rolling. The gap is just under two metres.
4.0s — The gap has closed to one metre. The pool of warm light slides down
the probe's shaft and onto the capsule's nose.
7.5s — The three vanes touch the ring's radial guide grooves and slide
along them with a faint scrape, correcting the last centimetres of
alignment.
8.8s — The probe tip seats to full depth in the throat. Contact: the two
machined faces meet with a clear structural boundary and a visible
1-centimetre seam between them; a ring of dust and paint flakes is knocked
loose and immediately falls straight down out of frame.
9.4s — The THREE capture arms swing inward together and fold closed over
the probe's collar, all three seating home at the same instant, actuator
rods drawing in.
10.0s — Everything is rigid. Hold on the closed arms.

AUDIO: One continuous low hull-conducted engine drone. At 8.8 seconds a
single hard metallic knock, deep and short, felt more than heard; at 9.4
seconds three overlapping mechanical clacks. Then the drone alone. No
voice, no music.

PHYSICS: Closing rate is exactly 0.20 metres per second — the speed of a
slow crawl. The contact is a rigid-body collision between two machined
metal faces: no deformation, no bounce, no merging. The knocked-loose dust
is unpowered and falls away at 2.16 metres per second squared.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no slow motion, no speed ramp. No figure visible anywhere. Exactly
THREE capture arms and all THREE close together — none stays open, none
jams, none bends. Exactly ONE probe with THREE vanes, ONE throat. Probe and
ring keep a clear rigid structural boundary at every frame — no merging, no
phasing, no melting, no clipping through metal. The probe only rises — no
descent, no bounce, no reversal, no drift sideways. No fire, no sparks, no
explosion, no debris field, no structural damage — this is a clean docking.
The falling dust accelerates continuously downward and never hovers. 0%
bloom, no glow filter, no lens flare, no soft focus. No readable text,
letters, digits, numbers, insignia or watermark. No subtitles, no title
card. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 22 (S22) — AĞIRLIK

> 🎯 **REFERANS:** **RB** p2 (kenetli halka pencereyi doldurur) · **RD** p1 · **RE** p1 · p2

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats:
the pilot in the LEFT seat, a lean 54-year-old man with a thick grey
moustache; the engineer in the RIGHT seat, a compact 33-year-old woman with
a completely shaved head. Both still strapped into their five-point
harnesses in matte BURNT-ORANGE hard-shell pressure suits with crisp
recessed seams and machined aluminium rings at the shoulders and wrists —
his shoulder bands charcoal grey, hers bone white, a 12-centimetre machined
tool block on HER LEFT FOREARM only. Both backs flat, both helmets sealed,
each visor a single curved optically clear pane in a 2-centimetre
brushed-metal frame with its lower seal ring visible at the collar, both
faces fully readable through the glass. His gloved right hand rests flat on
her left forearm plate, metal on metal, with a clear boundary between the
two shells. Through the wide curved window above them there is no longer
any sky: the window is filled edge to edge by the machined underside of a
capture ring and the folded arms of a docking socket, lit warm white at
3400K. The 40-centimetre brass lanyard hangs from the window frame, dead
straight down and taut.

ENVIRONMENT: Unpressurised cabin in vacuum, docked and rigid; 0.220 g of
thrust acceleration now carried through the ship's structure.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Warm-white
light from the socket above is now the key on both helmets and shoulders;
dim amber console segments from below; no blue anywhere.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable; neither helmet is open, lifted or removed and no bare skin shows
above either collar. His hand and her forearm keep a clear structural
boundary — no merging, no phasing, five fingers, no extra digits. The
lanyard hangs straight down. 0% bloom, no glow filter, no soft focus. No
readable text, letters, digits, numbers, icons or screen graphics. No
subtitles, no title card, no watermark. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache and a
2-centimetre burn scar on the bone of his right cheek; the engineer in the
RIGHT seat, a compact 33-year-old woman with a completely shaved head and a
pale 4-centimetre line along the bone of her right jaw. Both still strapped
into harnesses in matte BURNT-ORANGE hard-shell pressure suits — his
shoulder bands charcoal grey, hers bone white, a 12-centimetre tool block
on HER LEFT FOREARM only. Both backs FLAT, both helmets sealed: each visor
a single curved optically clear pane in a 2-centimetre brushed-metal frame,
its seal ring visible at the collar, both faces fully readable. Through the
window above them there is no sky at all: it is filled edge to edge by the
machined underside of a capture ring and the folded arms of a docking
socket, lit warm white. A brass lanyard hangs from the window frame.

TIMELINE:
0.0s — A short hard jolt runs through the whole cabin as the capture
completes. The lanyard jumps 8 centimetres upward, then falls back and
settles dead straight down in two small decaying movements.
2.5s — The engine note through the hull changes character: the same low
drone, but bigger and further away, coming now through the larger
structure.
4.0s — Neither of them moves. Both faces stay tilted up at the filled
window. Neither speaks; no mouth moves at any point.
6.0s — His gloved right hand lifts off the armrest, crosses the gap and
settles flat on her left forearm plate, metal on metal, and stays there.
8.5s — She closes her eyes for two seconds and opens them again. Her hand
does not move.
10.0s — Hold.

AUDIO: One continuous low hull-conducted drone that changes character at
2.5 seconds — deeper, larger, more distant. A dull structural knock at 0.0
seconds and a soft double tap of glove on plate at 6.0. No voice, no music,
no dialogue of any kind.

PHYSICS: The two craft are now one rigid structure under 0.220 g of thrust
acceleration carried through the ship. The lanyard rebounds once under the
capture jolt and returns to vertical. Arms have weight and move at ordinary
human speed.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; no helmet opens or is removed and no bare skin shows
above either collar. No embrace, no unbuckling, no standing, no leaving the
seats, no hatch opening. His hand and her forearm keep a clear structural
boundary — no merging, no phasing, five fingers, no extra digits. No mouth
moves and no one speaks. Nothing in the cabin floats. 0% bloom, no glow
filter, no soft focus. No readable text, letters, digits, numbers, icons or
screen graphics. No subtitles, no dialogue text, no title card, no
watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 23 (S23) — 🎬 VİRAL #4: BOŞ KIZAK

> 🎯 **REFERANS:** **RC** p3 ⭐ (boş kızak — bedelin görüntüsü) · **RC** p4 (karşılaştırma: dolu hâli) · **RB** p2 (sağda kapalı kollar)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Tight exterior
view of a docked capsule's upper hull in vacuum. Exactly 2 human figures
exist in this film and both are sealed inside this capsule — no figure is
visible in frame.

SCENE: The upper cone of the ferry capsule fills the left two thirds of the
frame — matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and
flush rivet rows, the worn metal frame of its wide curved window running
across the top of the shot. Bolted to the upper cone on the starboard side:
the cargo cradle, now EMPTY — a machined rack of FORTY empty moulded
sockets in five rows of eight, their pale interiors clean where the tubes
sat and grey-dusted at the edges where they did not, the clamp bar swung
back and hanging open on its hinge. One wide BURNT-ORANGE strap is still
attached at one end to its machined buckle and hangs straight DOWN along
the flank, slack and unloaded, its free end clear of the rack. It is the only warm saturated colour anywhere in the frame. Above and behind, at
screen-right, the ship's hull and the folded arms of a docking socket
clamped over the capsule's probe, lit warm white.

ENVIRONMENT: Hard vacuum, docked and rigid, 0.220 g of thrust acceleration
carried through the ship's structure.

CAMERA & LIGHT: 50mm spherical lens, fixed 6 metres off the flank.
Warm-white light from the socket above falls across the empty rack and
picks out every vacant socket; hard starlight from screen-left; absolute
black inside each empty socket.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly FORTY empty sockets in five rows of eight, exactly ONE
slack orange strap, exactly ONE clamp bar. Not one core tube remains
anywhere — not one, not a fragment. No damage, no tear, no scorch mark, no
debris — the cradle was released, not destroyed. 0% bloom, no glow filter,
no lens flare, no soft focus. No readable text, letters, digits, numbers,
labels, barcodes, insignia or watermark. No subtitles, no title card.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 6 metres off the flank of a docked capsule in vacuum, no
camera movement. Exactly 2 human figures exist in this film and both are
sealed inside this capsule — no figure is visible in frame.

SCENE: The upper cone of the ferry capsule fills the left two thirds of
frame — matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and
flush rivet rows, the worn metal frame of its wide curved window across the
top of the shot. Bolted to the upper cone on the starboard side: the cargo
cradle, now EMPTY — FORTY empty moulded sockets in five rows of eight,
their pale interiors clean where the tubes sat and grey-dusted at the edges
where they did not, the clamp bar swung back and hanging open. One wide
BURNT-ORANGE strap hangs straight down along the flank from its machined
buckle, slack and unloaded — the only warm saturated colour in frame. At
screen-right the ship's hull and the folded arms of a docking socket
clamped over the capsule's probe, lit warm white.

TIMELINE:
0.0s — Stillness. Forty empty sockets, one loose strap hanging straight
down, absolute black inside every socket.
3.0s — The strap's free end swings 5 centimetres and settles again, moved
by nothing but the structure's own faint vibration. Nothing else moves.
6.0s — Far below and behind, a single point of light crosses the black gap
between the hulls and is gone: a fleck of debris falling away.
10.0s — Hold on the empty rack.

AUDIO: One continuous low hull-conducted drone, deep and large, carried
through the docked structure. Nothing else. No voice, no music.

PHYSICS: The docked structure is under 0.220 g of thrust acceleration; the
loose strap hangs straight down under its own weight and its small swing
decays quickly. There is no air to move anything.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. No figure visible anywhere. Exactly FORTY empty sockets, exactly
ONE slack orange strap. Not one core tube reappears at any point — not one,
not a fragment. The strap hangs downward and swings only slightly — it
never floats, never rises, never coils, never drifts in zero gravity. No
damage, no tear, no scorch, no fire, no sparks, no debris cloud on the
hull. 0% bloom, no glow filter, no lens flare, no soft focus. No readable
text, letters, digits, numbers, labels, barcodes, insignia or watermark. No
subtitles, no title card. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 24 (S24) — FİNAL: GEÇİT

> 🎯 **REFERANS:** **RA** p1 · p2 · p3 (S0 ile birebir aynı kadraj) · **RB** p2 (yuvada kenetli nokta) · **RC** p3 (boş kızak)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Deep space, 600
metres off the flank of a burning interstellar ship — the same distance,
lens and framing as the film's first shot. Exactly 2 human figures exist in
this film and both are sealed inside the small capsule — no figure is
visible in frame.

SCENE: The crossing ship crosses the frame vertically, bow at the TOP and
stern at the bottom — a 210-metre interstellar vessel under constant burn:
a sleek 26-metre ceramic-white ice shield with a turquoise rim stripe at the bow, three habitat drums wrapped in clean white multi-layer insulation quilting, each ringed by a thin turquoise band, four polished bright-metal 9-metre propellant spheres, a
12-metre lattice berth boom standing out from its port flank, a long open
graphite truss spine, two dead-black knife-edge radiator wings, a 30-metre
satin pearl-grey conical shadow shield and an armoured drive block with three
recessed nozzles at the stern. From those nozzles, three pale blue-white
exhaust cones merge into one straight, sharply defined 400-metre lance that
leaves the BOTTOM of frame and thins away — exactly as long, as straight
and as bright as it was four minutes ago. The single change anywhere in the
frame: under the outer pad of the berth boom, one fortieth of the ship's
length, sits the ferry capsule — a 5.2-metre truncated cone docked nose-UP
into the socket, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe, its cargo cradle EMPTY with
one slack BURNT-ORANGE strap hanging down its flank.

ENVIRONMENT: Hard vacuum. Absolute black sky, sharp pinpoint stars, no
haze. Everything under 0.220 g of thrust acceleration.

CAMERA & LIGHT: 24mm spherical lens, fixed 600 metres out, the ship's axis
vertical in frame — identical to the opening shot. Hard parallel starlight
from screen-left at 6500K, absolute black shadows with razor-sharp edges;
the blue lance lights the underside of the drive block from below; a
pinpoint of warm white at the berth.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly THREE habitat drums, FOUR propellant spheres, TWO
radiator wings, THREE engine nozzles, ONE capsule. The exhaust is a
straight sharp lance — it never billows, curls or mushrooms. The cargo
cradle is empty — not one core tube remains. 0% bloom, no glow filter, no
lens flare, no soft focus. No readable text, letters, digits, numbers,
insignia or watermark. No subtitles, no end card, no credits, no title.
No nebula, no atmospheric haze. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 600 metres out in vacuum — the same distance, lens and
framing as the film's first shot. No camera movement. Exactly 2 human
figures exist in this film and both are sealed inside the small capsule —
no figure is visible in frame.

SCENE: The crossing ship crosses the frame vertically, bow at the TOP and
stern at the bottom — a 210-metre interstellar vessel under constant burn:
a sleek 26-metre ceramic-white ice shield with a turquoise rim stripe at the bow, three habitat drums wrapped in clean white multi-layer insulation quilting, each ringed by a thin turquoise band, four polished bright-metal 9-metre propellant spheres, a
12-metre lattice berth boom standing out from its port flank, a long open
graphite truss spine, two dead-black knife-edge radiator wings, a 30-metre
satin pearl-grey conical shadow shield and an armoured drive block with three
recessed nozzles. Three pale blue-white exhaust cones merge into one
straight, sharply defined 400-metre lance leaving the BOTTOM of frame. The
single change from the opening: under the outer pad of the berth boom, one
fortieth of the ship's length, the ferry capsule sits docked nose-UP into
the socket, its cargo cradle EMPTY with one slack BURNT-ORANGE strap
hanging down its flank.

TIMELINE:
0.0s — Absolute stillness. The ship burns exactly as it burned before.
4.0s — A flake of frost breaks off the lowest propellant sphere and falls
toward the bottom of frame, accelerating, exactly as one did at the
beginning; it passes the drive block and is gone into the blue.
8.0s — Nothing has changed anywhere on the ship: same burn, same length of
lance, same lights, same attitude. The small docked capsule does not move.
10.0s — Hold on the last frame.

AUDIO: One continuous low hull-conducted engine drone, deep and steady,
thinning slowly toward the end of the shot but never stopping. No voice, no
music at the final second.

PHYSICS: The ship's acceleration is unchanged at 0.220 g and will stay
unchanged for months. The docked capsule is now part of the structure and
does not move relative to it. The falling flake is unpowered and
accelerates away at 2.16 metres per second squared.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible anywhere. Exactly THREE habitat drums,
FOUR propellant spheres, TWO radiator wings, THREE engine nozzles, ONE
capsule. The exhaust is a straight sharp lance — never billowing, curling,
mushrooming or bending; it does not shrink, brighten or cut out at any
point. The docked capsule never detaches, moves or drifts. The cargo cradle
stays empty — not one core tube reappears. The falling flake accelerates
continuously downward and never hovers or freezes. 0% bloom, no glow
filter, no lens flare, no soft focus. No readable text, letters, digits,
numbers, insignia or watermark. No subtitles, no end card, no credits, no
title card, no fade to black with text. The take ends on the held frame.
Photorealistic with 35mm film grain.
```

---

# 📋 PART B ÖZET TABLOSU

| # | Sahne | Lens | İç/Dış | Konum | Kartuş | Kilit olay |
|---|---|---|---|---|---|---|
| S13 | ARİTMETİK | 50mm | iç | 56 m | 2 | el işareti: düz avuç → yumruk |
| S14 | SON ÇİFT | 35mm | iç | 56 m | 2→1 | beşinci kartuş (2:25); kovan S15'te |
| S15 | OMURGA | 50mm | dış | 51 m | 1 | omurga aşağı akıyor; kovan düşer; içeri kayış başladı |
| S16 | GERİ İÇERİ | 35mm | iç | 37 m | 1 | 34 m'lik kayışın FRENİ; gövde tepede durur |
| S17 | SON KARTUŞ | 85mm | dış | 22 m | 1→0 | altı yuva boş — sayaç sıfır |
| S18 | ON ALTI METRE | 24mm | dış | 16 m | 0 | ⛔ dip: 10 saniye hiçbir şey olmaz |
| **S19** | 🎬 **MERKEZİ SEÇİM** | 35mm | iç | 16 m | 0 | ⭐ kol çekilir · yük düşer · gövde kayar · pilot valfi kırpar — TEK KARE |
| S20 | HAFİF | 35mm | iç | 14 m | 0 | seyir 1.1 m/s; son 3 sn RCS freni |
| **S21** | ⭐ **DORUK: TEMAS** | 50mm | dış | 4 m | 0 | prob boğaza girer (8.8 s'de), üç kol kapanır |
| S22 | AĞIRLIK | 35mm | iç | 0 | 0 | kordon sıçrar ve sarkar; tek dokunuş |
| S23 | 🎬 **VİRAL #4** | 50mm | dış | 0 | 0 | kırk boş yuva, gevşek turuncu kayış |
| S24 | FİNAL: GEÇİT | 24mm | dış | 0 | 0 | S0'ın aynısı — tek fark yuvadaki nokta |

**PART B: 12 sahne · 2:09–4:09 · 0 replik · 0 kesme · 12/12 sabit lockoff**

---

## 🎞️ KURGU KAPISI [D72 · D101] — teslimden ÖNCE koşulur

```
① CLIP COUNT   = 25 klip   (kurguda kaç segment var?)
①b SHOT COUNT  = 25 çekim  (sahne = çekim, sahne içi kesme yok)
①c SCENE COUNT = 25 sahne
   ⛔ Üçü eşittir — film sabit ızgaralıdır, tek satır yeter [D101].
② RUNTIME      = 249 s ± 2 s   (Hook 9 s + 24 × 10 s)
③ EKRAN METNİ  = 0.0 s — jenerik, başlık kartı ve KAPAK ÇIKTISI dahil
   ⚠️ Bu zincirin depoda 7 vakası var. Kapak AYRI dosyadır; kurguya
      giren tek harf yoktur.
④ CENTRAL CHOICE (S19) kurguda VAR ve seçim ekranda TAMAMLANIYOR:
   kol çekiliyor + yük düşüyor + gövde kayıyor, üçü de aynı klipte
⑤ ASL          = 249 / 25 = 9.96 s — hedef bant 9.5-10.5 s
⑥ EN KISA ÇEKİM TESTİ: planın en kısası 9.0 s (S0); kurgudaki en kısa
   segment de 9.0 s mi?
⑦ KIRPMA BÜTÇESİ [D100]: RAW 25 × 10 s = 250 s · TRIM 1 s (yalnız S0)
   Başka hiçbir klip kırpılmaz; kırpma gerekiyorsa kayıt buraya yazılır.
⑧ SES YATAĞI [D83]: motor uğultusu 25 klibin 25'inde SÜREKLİDİR ve
   kesme sınırlarında ölmez. Kurguda tek bir sessizlik yoktur.
```

---

## 🚪 KAPI KAYITLARI [D74] — PART B

```
| kapı | tarih | deneme | sonuç | karar |
|------|-------|--------|-------|-------|
| KAPI 1 — S19 yük atma       |  |  |  |  |
| KAPI 2 — S21 temas          |  |  |  |  |
| blok 4 (S13-S18) oturumu    |  |  |  |  |
| blok 5 (S19-S24) oturumu    |  |  |  |  |
| prompt_kontrol.py PART_B    |  |  |  |  |
| KURGU KAPISI (8 madde)      |  |  |  |  |
```

---

## ➡️ İLGİLİ DOSYALAR

**Plan:** `THE_UPHILL_DARK_PLAN.md` · **Part A:** `THE_UPHILL_DARK_PART_A.md`
**Referans:** `THE_UPHILL_DARK_REFERANS_PAKETI.md` · **Kapak:** `THE_UPHILL_DARK_KAPAK.md`
