# 🎬 THE LEANING ROOM — BÖLÜM 1  (S0 – S5)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_LEANING_ROOM_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF
> YAPMAZ — her prompt tek başına çalışır (AGENTS §2 kural ③).
>
> Bölüm sınırı ardışık bir çifttir: bu dosyanın son sahnesi (S5, yakın plan ·
> omuz üstü) ile bölüm 2'nin ilk sahnesi (S6, orta plan · profil) bir ölçek
> kademesi ve bir açı tipi ayrılır. Denetimi klasör modu yapar:
> `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_2_4_dk_filmler_uzay/THE_LEANING_ROOM`

---

## 🎬 SAHNE 0 — THE ROOM AT CRUISE

```
SÜRE: 10,0 s  ·  BAŞLANGIÇ: 0:00  ·  VURUŞ: açılış imajı + hook
KURULUM: A — 24mm · extreme wide shot · eye level · h 1,20 m · 6,4 m
YATMA: 4° → 0°   ·   EŞYA: 6   ·   İNSAN: 1
```

### 📸 GÖRSEL PROMPT

```
Scene 1 of 12. Photorealistic, 16:9.

SUBJECT:
A woman in her late thirties, tall and square-shouldered, brown skin, black
hair drawn back into a low flat knot at the nape with no loose strands. High
cheekbones, a straight nose, a wide mouth, a matte dark red on the lips and no
other makeup. She wears a long charcoal wool coat-dress, single-breasted, cut
to the ankle, buttoned to the collarbone, with a narrow standing collar; the
wool has a visible flat weave and no pattern of any kind. The sleeves are
pushed back to the elbow and her forearms are bare. On her left wrist a plain
wide band of brushed brass with no face and no dial. Flat black leather shoes.
The back of the coat-dress is one continuous panel of charcoal wool from
collar to hem, unbroken, carrying nothing. Her hands are bare, the nails short
and unpainted. She is calm and unhurried; she is working, not enduring. She
stands in the middle of the room, mid-stride, walking to the deep armchair.

ENVIRONMENT:
The main saloon of a private long-range ship. Matte walnut panelling, a dark
woven floor, one low table, one deep armchair, a settee, recessed shelves. A
curved strip of glass forms the bow wall in the depth of the frame. A long
window runs the whole starboard wall on screen-right, and the star field
outside it is sharp and black. There are no screens, no dials and no gauges
anywhere in the ship. Set into the near edge of the table is a brass hand
wheel and one row of unmarked brass levers. Six loose objects lie on the
table: a brass key on a leather tag, a flat river stone, a folded pair of
dark glasses, a rolled charcoal wool scarf, a solid brass sphere the size of
a plum, and an empty shallow brass dish.

THE LAMP:
A single heavy brass pendant lamp hangs from a ceiling rail over the middle
of the table on a braided cord. The shade is matte brass and fully closed; it
drops a hard-edged pool of warm light on the table and makes no halo. The
cord is taut and perfectly straight. Right now the lamp does not hang vertical: it
is tilted four degrees over toward the starboard window on screen-right, and
it is completely still.

CAMERA:
Shot on a 24mm lens from a fixed position at the aft corner of the room on
the port side, camera height 1.20 m, 6.4 m from her, eye level, extreme wide
shot taking in the whole saloon on the diagonal. Physically accurate
perspective, correct engineering proportions.

LIGHTING:
A distant yellow star sits low off the starboard beam and throws a warm amber
light in through the starboard window on screen-right, raking across the room
so that every shadow lies long toward screen-left. The lamp adds a small
warm pool on the table. Spherical lens rendering, no horizontal streak.

PHYSICS:
Weight in this room comes only from the ship's drive and the floor is square
to the thrust axis. Everything except the lamp is square and level: the table
edge is parallel to the floor, the six objects sit still, her stride is
normal walking weight at one quarter of Earth gravity.

NEGATIVE:
Exactly 1 human character in frame — no duplicates, no clones, no second
person, no reflected figure, no shadow of anyone else. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible texture.
Photorealistic skin pores and fine lines retained — no airbrushing, no plastic
or waxy texture, no smoothed skin, no face morphing. No readable text,
letters, digits, numbers or symbols on any surface, plate or sign — not on the
clothing, not on the fittings, not on the brass, not on the panelling, not on
the glass and not on any object in the frame. Nothing in this room has been
measured, labelled, marked out or annotated by anyone: no scale marks, no
graduation ticks, no engraved or painted characters of any kind. No subtitles,
no captions, no title card, no watermark, no HUD overlay, no lens data, no
camera metadata, no name label. No mirrors and no mirrored surfaces. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers. All loose objects keep real weight — never
hovering, never frozen mid-air, never flowing like liquid. Room static and
stable — no melting surfaces, no warping topology, no swimming texture. No
lens flare, no anamorphic streak, no starburst. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 1 of 12. Duration 10 seconds. Single unbroken take, no cuts.

CAMERA:
Fixed lockoff, 24mm, camera height 1.20 m, 6.4 m from her, eye level, extreme
wide shot of the whole saloon on the diagonal. The camera does not move, pan,
tilt, zoom or track at any point.

ANCHOR:
The saloon of a private long-range ship: walnut panelling, a low table with
six loose objects, a deep armchair, the starboard window on screen-right, a
heavy brass pendant lamp on a braided cord over the table, and a calm woman in her late thirties, brown skin, black hair in a low flat knot,
in a long charcoal wool coat-dress buttoned to the collarbone.

TIMELINE:
0.0 s — The lamp hangs tilted four degrees over toward the starboard window on
screen-right, cord taut, completely still. She is mid-stride in the room.
2.5 s — She reaches the armchair and sits, unhurried, facing screen-right.
4.0 s — The lamp begins to come back to vertical, one slow continuous
movement, no swing and no overshoot.
7.0 s — It arrives exactly vertical and stops. The cord gives one dry tick
against the brass stem.
10.0 s — She lays her right hand flat on the brass hand wheel in the table
edge. Everything in the room is square and still. No cuts.

PHYSICS:
Weight comes only from the ship's drive, so the lamp hangs along the direction
the drive pushes. It moves once and stops: it never swings and never trembles.
Walking weight is one quarter of Earth gravity and the six objects do not
move. The tilt is toward screen-right only, with no direction reversal.

AUDIO:
A low hull-borne hum, thin and steady. One dry tick of cord against brass at
7.0 seconds. Her shoes on the woven floor. No music in the first two seconds.
No speech.

NEGATIVE:
Exactly 1 human character in frame — no second person, no clones, no reflected
figure. 0% bloom, no glow filter, no soft focus. No readable text, letters,
digits or symbols on any surface in frame. No subtitles, no title card, no watermark. Photorealistic skin texture, no waxy rendering.
Loose objects keep real weight, never hovering, never frozen. Rigid contact, no merging,
no extra fingers. No mirrors, no lens flare.
Photorealistic with 35mm film grain.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 1 — THE FIRST MASS

```
SÜRE: 10,0 s  ·  BAŞLANGIÇ: 0:10  ·  VURUŞ: katalizör (0:13) ✅ ≤0:15
KURULUM: D — 28mm · wide shot · high angle (−28°) · h 2,25 m · 5,2 m
YATMA: 0°   ·   EŞYA: 6   ·   İNSAN: 1
```

### 📸 GÖRSEL PROMPT

```
Scene 2 of 12. Photorealistic, 16:9.

SUBJECT:
A woman in her late thirties, tall and square-shouldered, brown skin, black
hair drawn back into a low flat knot at the nape with no loose strands. High
cheekbones, a straight nose, a wide mouth, a matte dark red on the lips and no
other makeup. She wears a long charcoal wool coat-dress, single-breasted, cut
to the ankle, buttoned to the collarbone, with a narrow standing collar; the
wool has a visible flat weave and no pattern of any kind. The sleeves are
pushed back to the elbow and her forearms are bare. On her left wrist a plain
wide band of brushed brass with no face and no dial. Flat black leather shoes.
The back of the coat-dress is one continuous panel of charcoal wool from
collar to hem, unbroken, carrying nothing. Her hands are bare, the nails short
and unpainted. She is calm and unhurried; she is working, not enduring. She
sits well back in the deep armchair, facing screen-right, her right hand
resting on the brass hand wheel in the table edge.

ENVIRONMENT:
The main saloon of a private long-range ship seen from above: matte walnut
panelling, a dark woven floor, one low table, one deep armchair, a settee. A
curved strip of glass forms the bow wall in the depth of the frame. A long
window runs the whole starboard wall on screen-right. Beyond that window, held
in the right third of the frame, the near edge of a pale blue-white ice world
has just come into view, small and hard-edged and clearly a long way off.
There are no screens, no dials and no gauges anywhere in the ship. Six loose
objects lie on the table: a brass key on a leather tag, a flat river stone, a
folded pair of dark glasses, a rolled charcoal wool scarf, a solid brass
sphere the size of a plum, and an empty shallow brass dish.

THE LAMP:
A single heavy brass pendant lamp hangs from a ceiling rail over the middle of
the table on a braided cord. The shade is matte brass and fully closed and
drops a hard-edged pool of warm light on the table, making no halo. The cord
is taut and straight and the lamp hangs exactly vertical, completely still.

CAMERA:
Shot on a 28mm lens from a fixed position high on the aft bulkhead, camera
height 2.25 m, 5.2 m from her, high angle looking down and forward across the
room at twenty-eight degrees, wide shot. Physically accurate perspective,
correct engineering proportions.

LIGHTING:
The warm amber of a distant yellow star is fading out of the starboard window
on screen-right and a cold blue-white edge is entering from the same side as
the ice world rises. The two colours meet across the walnut floor. Shadows are
softening as they change hands. Spherical lens rendering, no horizontal streak.

PHYSICS:
Weight comes only from the ship's drive and the floor is square to the thrust
axis. Every horizontal in the room is level and the lamp is exactly vertical:
the ship is running straight. The six objects sit still.

NEGATIVE:
Exactly 1 human character in frame — no duplicates, no clones, no second
person, no reflected figure, no shadow of anyone else. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible texture.
Photorealistic skin pores and fine lines retained — no airbrushing, no plastic
or waxy texture, no smoothed skin, no face morphing. No readable text,
letters, digits, numbers or symbols on any surface, plate or sign — not on the
clothing, not on the fittings, not on the brass, not on the panelling, not on
the glass and not on any object in the frame. Nothing in this room has been
measured, labelled, marked out or annotated by anyone: no scale marks, no
graduation ticks, no engraved or painted characters of any kind. No subtitles,
no captions, no title card, no watermark, no HUD overlay, no lens data, no
camera metadata, no name label. No mirrors and no mirrored surfaces. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers. All loose objects keep real weight — never
hovering, never frozen mid-air, never flowing like liquid. Room static and
stable — no melting surfaces, no warping topology, no swimming texture. No
lens flare, no anamorphic streak, no starburst. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 2 of 12. Duration 10 seconds. Single unbroken take, no cuts.

CAMERA:
Fixed lockoff, 28mm, camera height 2.25 m, 5.2 m from her, high angle looking
down and forward at twenty-eight degrees, wide shot. The camera does not move,
pan, tilt, zoom or track at any point.

ANCHOR:
The same saloon seen from above: the low table with six loose objects, the
deep armchair, the starboard window on screen-right, the brass pendant lamp on
a braided cord, and a calm woman in her late thirties, brown skin, black hair in a low flat knot,
in a long charcoal wool coat-dress buttoned to the collarbone, sitting well back with her right hand flat on
the brass hand wheel.

TIMELINE:
0.0 s — The lamp hangs exactly vertical and still. Warm amber light is fading
out of the starboard window on screen-right.
3.0 s — The near edge of a pale blue-white ice world enters the starboard
window in the right third of the frame, small, hard-edged and far off. Cold
light begins to replace the amber across the floor.
5.5 s — Her head turns a few degrees to follow it. Her hand does not move.
8.0 s — The ice world holds in the right third, drifting very slowly across
the window. The lamp has not moved at all.
10.0 s — Her shoulders settle. The lamp is still exactly vertical. No cuts.

PHYSICS:
Weight comes only from the ship's drive. The ship is running straight, so the
lamp stays exactly vertical and the six objects do not move. The ice world
drifts at a slow constant rate, never jumping and never accelerating, holding
in the right third and moving screen-right to screen-left across the window.
The light is on her screen-right side and rims that side of her face; she does
not turn into it and the ship does not swing its bow to it. No direction
reversal.

AUDIO:
A low hull-borne hum, thin and steady, unchanged throughout. Wool moving
against leather when her head turns. No speech.

NEGATIVE:
Exactly 1 human character in frame — no second person, no clones, no reflected
figure. 0% bloom, no glow filter, no soft focus. No readable text, letters,
digits or symbols on any surface in frame. No subtitles, no title card, no watermark. Photorealistic skin texture, no waxy rendering.
Loose objects keep real weight, never hovering, never frozen. Rigid contact, no merging,
no extra fingers. No mirrors, no lens flare.
Photorealistic with 35mm film grain.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 2 — THE ROOM IS SQUARE

```
SÜRE: 10,0 s  ·  BAŞLANGIÇ: 0:20  ·  VURUŞ: tartışma · TOHUM (0:22-0:24)
KURULUM: B — 50mm · medium shot · profile · h 1,10 m · 3,0 m
YATMA: 0°   ·   EŞYA: 6   ·   İNSAN: 1
⭐ TEMA MOTİFİ: oda kusursuz kare
⭐ EŞ KADRAJ ÇİFTİNİN KAYNAĞI [D153]: S6 ve S9'un imajları BU sahnenin
   ONAYLI karesinden image-edit ile türetilir, ≤3 maddelik fark listesiyle.
```

### 📸 GÖRSEL PROMPT

```
Scene 3 of 12. Photorealistic, 16:9.

SUBJECT:
A woman in her late thirties, tall and square-shouldered, brown skin, black
hair drawn back into a low flat knot at the nape with no loose strands. High
cheekbones, a straight nose, a wide mouth, a matte dark red on the lips and no
other makeup. She wears a long charcoal wool coat-dress, single-breasted, cut
to the ankle, buttoned to the collarbone, with a narrow standing collar; the
wool has a visible flat weave and no pattern of any kind. The sleeves are
pushed back to the elbow and her forearms are bare. On her left wrist a plain
wide band of brushed brass with no face and no dial. Flat black leather shoes.
The back of the coat-dress is one continuous panel of charcoal wool from
collar to hem, unbroken, carrying nothing. Her hands are bare, the nails short
and unpainted. She is calm and unhurried; she is working, not enduring. She
sits in full profile facing screen-right, her right hand resting on the brass
hand wheel, her eyes open and steady on the window.

ENVIRONMENT:
The main saloon of a private long-range ship: matte walnut panelling on
screen-left, a dark woven floor, the low table across the foreground. A long
window runs the whole starboard wall on screen-right and a pale blue-white ice
world fills it, sharp-edged, cratered, without atmosphere. A curved strip of
glass forms the bow wall further back in the depth of the frame. There are no
screens, no dials and no gauges anywhere in the ship. Six loose objects lie on
the table: a brass key on a leather tag, a flat river stone, a folded pair of
dark glasses, a rolled charcoal wool scarf, a solid brass sphere the size of a
plum, and an empty shallow brass dish. Every horizontal in the room is level
and every vertical is plumb; the room is perfectly square.

THE LAMP:
A single heavy brass pendant lamp hangs from a ceiling rail over the table on
a braided cord, in the upper left quarter of the frame. The shade is matte
brass and fully closed. The cord is taut and straight and the lamp hangs
exactly vertical, completely still. High on the brass stem, near the ceiling
rail, there is one old dent in the metal, dulled and darkened with age, the
brass around it worn smooth. Nothing draws attention to it; the cold light
simply passes across it.

CAMERA:
Shot on a 50mm lens from a fixed position at the aft end of the room on the
centre line, camera height 1.10 m, 3.0 m from her, eye level, medium shot in
full profile. Physically accurate perspective.

LIGHTING:
Hard, level, cold blue-white light comes in through the starboard window on
screen-right off the ice world and lays every shadow flat toward screen-left.
The walnut goes almost grey under it. The lamp's own warm pool survives only
on the table top. Spherical lens rendering, no horizontal streak.

PHYSICS:
Weight comes only from the ship's drive and the floor is square to the thrust
axis. The ship is running straight, so the lamp is exactly vertical and the
six objects sit still. Her weight in the chair is one quarter of Earth
gravity: the wool falls in long soft folds and the leather is barely
compressed.

NEGATIVE:
Exactly 1 human character in frame — no duplicates, no clones, no second
person, no reflected figure, no shadow of anyone else. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible texture.
Photorealistic skin pores and fine lines retained — no airbrushing, no plastic
or waxy texture, no smoothed skin, no face morphing. No readable text,
letters, digits, numbers or symbols on any surface, plate or sign — not on the
clothing, not on the fittings, not on the brass, not on the panelling, not on
the glass and not on any object in the frame. Nothing in this room has been
measured, labelled, marked out or annotated by anyone: no scale marks, no
graduation ticks, no engraved or painted characters of any kind. No subtitles,
no captions, no title card, no watermark, no HUD overlay, no lens data, no
camera metadata, no name label. No mirrors and no mirrored surfaces. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers. All loose objects keep real weight — never
hovering, never frozen mid-air, never flowing like liquid. Room static and
stable — no melting surfaces, no warping topology, no swimming texture. No
lens flare, no anamorphic streak, no starburst. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 3 of 12. Duration 10 seconds. Single unbroken take, no cuts.

CAMERA:
Fixed lockoff, 50mm, camera height 1.10 m, 3.0 m from her, eye level, medium
shot in full profile. The camera does not move, pan, tilt, zoom or track at
any point.

ANCHOR:
The same saloon: walnut panelling on screen-left, the low table across the
foreground, the starboard window on screen-right filled by a pale blue-white
ice world, the brass pendant lamp in the upper left quarter of the frame with
one old dulled dent high on its stem, and a calm woman in her late thirties, brown skin, black hair in a low flat knot,
in a long charcoal wool coat-dress buttoned to the collarbone, in full profile facing
screen-right.

TIMELINE:
0.0 s — Every horizontal in the room is level. The lamp hangs exactly vertical
and still.
2.0 s — Cold light crosses the brass stem and the old dent reads for a moment
as a dull hollow in the metal, then the light moves on. She does not look at
it.
4.5 s — She blinks once, slowly. Her eyes stay on the window.
7.0 s — Her thumb moves a few millimetres on the brass wheel and stops.
10.0 s — Nothing else in the room has moved. The lamp is still exactly
vertical. No cuts.

PHYSICS:
Weight comes only from the ship's drive. The ship is running straight, so the
lamp stays exactly vertical for the whole shot: it never swings, never sways
and never trembles, and the six objects do not move. Her weight is one quarter
of Earth gravity and the wool hangs in long soft folds. The ice world stays on
screen-right; the light is on her screen-right side and rims that side of her
face and she does not turn into it. No direction reversal.

AUDIO:
A low hull-borne hum, thin and steady. Her breathing, slow and even, close.
One faint creak of leather at seven seconds. No speech.

NEGATIVE:
Exactly 1 human character in frame — no second person, no clones, no reflected
figure. 0% bloom, no glow filter, no soft focus. No readable text, letters,
digits or symbols on any surface in frame. No subtitles, no title card, no watermark. Photorealistic skin texture, no waxy rendering.
Loose objects keep real weight, never hovering, never frozen. Rigid contact, no merging,
no extra fingers. No mirrors, no lens flare.
Photorealistic with 35mm film grain.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 3 — THE ROAD

```
SÜRE: 10,0 s  ·  BAŞLANGIÇ: 0:30  ·  VURUŞ: tartışma · varış sayacı ①
KURULUM: F — 50mm · close-up · over-the-shoulder · h 1,15 m · 1,1 m
YATMA: 0°   ·   EŞYA: 6   ·   İNSAN: 1
⛔ D139: kamera arkada → sırt için POZİTİF yüzey cümlesi prompta girer.
```

### 📸 GÖRSEL PROMPT

```
Scene 4 of 12. Photorealistic, 16:9.

SUBJECT:
A woman in her late thirties, tall and square-shouldered, brown skin, black
hair drawn back into a low flat knot at the nape with no loose strands. High
cheekbones, a straight nose, a wide mouth, a matte dark red on the lips and no
other makeup. She wears a long charcoal wool coat-dress, single-breasted, cut
to the ankle, buttoned to the collarbone, with a narrow standing collar; the
wool has a visible flat weave and no pattern of any kind. The sleeves are
pushed back to the elbow and her forearms are bare. On her left wrist a plain
wide band of brushed brass with no face and no dial. Flat black leather shoes.
The back of the coat-dress is one continuous panel of charcoal wool from
collar to hem, unbroken, carrying nothing. Her hands are bare, the nails short
and unpainted. She is calm and unhurried; she is working, not enduring. We see
her from behind and slightly to the port side: the shoulder and the back of
the head fill the lower left of the frame, the knot of hair sharp, the wool of
her back one clean unbroken surface with nothing on it and nothing attached.

ENVIRONMENT:
The main saloon of a private long-range ship. Past her shoulder, filling the
upper right of the frame, is the curved strip of glass that forms the bow
wall. Beyond it the star field is black and hard. Well off the centre of that
glass, high and small, sits one pale point of light that is not a star: it
carries a thin bright ring around it, only just resolvable. The near edge of
the starboard window shows at the right margin of the frame. There are no
screens, no dials and no gauges anywhere in the ship. Her right hand is on the
brass hand wheel set into the table edge, the fingers already turned a few
degrees over.

THE LAMP:
The braided cord and the lower part of the heavy brass pendant lamp cross the
top edge of the frame, taut, straight and exactly vertical, its hard-edged
warm pool falling out of shot onto the table below.

CAMERA:
Shot on a 50mm lens from a fixed position 1.1 m behind her port shoulder,
camera height 1.15 m, over-the-shoulder close-up with her shoulder in the
lower left and the bow glass beyond. Physically accurate perspective.

LIGHTING:
The cold blue-white of the ice world is falling away behind at the right
margin and no longer reaches the bow glass, which is dark. The lamp's warm
pool spills up from below onto her collar and the back of her neck. The pale
ringed point beyond the glass is small and clean and casts nothing into the
room. Spherical lens rendering, no horizontal streak.

PHYSICS:
Weight comes only from the ship's drive and the lamp is exactly vertical: the
ship is still running straight. Her hand turns the wheel a few degrees and
holds it there; nothing in the room answers yet.

NEGATIVE:
Exactly 1 human character in frame — no duplicates, no clones, no second
person, no reflected figure, no shadow of anyone else. The back of the
coat-dress is one continuous panel of charcoal wool from collar to hem,
unbroken, carrying nothing: no pack, no harness, no strap, no housing. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible texture.
Photorealistic skin pores and fine lines retained — no airbrushing, no plastic
or waxy texture, no smoothed skin, no face morphing. No readable text,
letters, digits, numbers or symbols on any surface, plate or sign — not on the
clothing, not on the fittings, not on the brass, not on the panelling, not on
the glass and not on any object in the frame. Nothing in this room has been
measured, labelled, marked out or annotated by anyone: no scale marks, no
graduation ticks, no engraved or painted characters of any kind. No subtitles,
no captions, no title card, no watermark, no HUD overlay, no lens data, no
camera metadata, no name label. No mirrors and no mirrored surfaces. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers. All loose objects keep real weight — never
hovering, never frozen mid-air, never flowing like liquid. Room static and
stable — no melting surfaces, no warping topology, no swimming texture. No
lens flare, no anamorphic streak, no starburst. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 4 of 12. Duration 10 seconds. Single unbroken take, no cuts.

CAMERA:
Fixed lockoff, 50mm, camera height 1.15 m, 1.1 m behind her port shoulder,
over-the-shoulder close-up with her shoulder in the lower left of the frame
and the bow glass beyond. The camera does not move, pan, tilt, zoom or track
at any point.

ANCHOR:
The same saloon. Past her shoulder, in the upper right of the frame, the
curved bow glass with a hard black star field and, well off centre and high,
one pale point of light that is not a star, carrying a thin bright ring around
it. The braided cord of the brass pendant lamp crosses the top of the frame.
In the lower left, a calm woman seen from behind, black hair in a low flat knot, the wool of her
back one continuous panel from collar to hem, unbroken, carrying nothing, her right hand on the brass hand wheel.

TIMELINE:
0.0 s — The lamp cord at the top of the frame hangs exactly vertical. The pale
ringed point sits high and off centre in the bow glass on screen-right.
3.0 s — Her hand closes on the brass wheel.
5.0 s — She turns the wheel through a few degrees, one smooth continuous
movement, and holds it there.
7.5 s — The lamp cord has not answered yet. Her shoulder stays square.
10.0 s — She holds the wheel exactly where she put it. Nothing else moves.
No cuts.

PHYSICS:
Weight comes only from the ship's drive. The ship is still running straight
and the cord stays taut and exactly vertical; the lamp never swings, never
sways and never trembles. The pale ringed point holds its place high and off
centre on screen-right and does not grow. Her shoulders stay square to the
frame and do not rotate. No direction reversal.

AUDIO:
A low hull-borne hum, thin and steady, rising by one small step in pitch as
the wheel turns and staying there. Brass turning against brass. Her breathing.
No speech.

NEGATIVE:
Exactly 1 human character in frame — no second person, no clones, no reflected
figure. The back of the coat-dress is one continuous panel of charcoal wool
from collar to hem, unbroken, carrying nothing. 0% bloom, no glow filter, no soft focus. No readable text, letters,
digits or symbols on any surface in frame. No subtitles, no title card, no watermark. Photorealistic skin texture, no waxy rendering.
Loose objects keep real weight, never hovering, never frozen. Rigid contact, no merging,
no extra fingers. No mirrors, no lens flare.
Photorealistic with 35mm film grain.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 4 — THE LAMP ANSWERS

```
SÜRE: 10,0 s  ·  BAŞLANGIÇ: 0:40  ·  VURUŞ: NOVUM KURULUM · viral ara ①
KURULUM: E — 85mm · extreme close-up · eye level · h 1,05 m · 2,1 m
YATMA: 0° → 4°   ·   EŞYA: 6 (anahtar 8 cm kayar)   ·   İNSAN: 0
⛔ KART 10 — İNSANSIZ SAHNE: NEGATIVE bloğu TAM METİN DEĞİL, kısa ve
   pozitif. Boş kadraj VARLIK olarak tarif edilir [D59 · Cold Burn S8].
⛔ D157③ — NOVUM SAHNESİ: kadrajda taşıyıcıdan başka HİÇBİR ŞEY hareket
   etmez. Rakip olay yok.
```

### 📸 GÖRSEL PROMPT

```
Scene 5 of 12. Photorealistic, 16:9.

SUBJECT:
A single heavy brass pendant lamp hanging from a ceiling rail on a braided
cord, filling the frame. The shade is matte brass, fully closed, with a
hammered surface and a worn lip. The cord is taut and perfectly straight. High on
the brass stem, near the top of the frame, there is one old dent in the metal,
dulled and darkened with age. The lamp hangs exactly vertical and is
completely still.

ENVIRONMENT:
The main saloon of a private long-range ship, empty of people. Behind the lamp
and thrown well out of focus: matte walnut panelling on screen-left, and on
screen-right the long starboard window with a hard black star field beyond it
and no world in view. Below the lamp, at the bottom edge of the frame, the
edge of the low table with a brass key on a leather tag lying on it. The room
around the lamp is quiet and settled and the air in it is perfectly still.
There are no screens, no dials and no gauges anywhere in the ship.

CAMERA:
Shot on an 85mm lens from a fixed position 1.6 m over on the port side, camera
height 1.05 m, 2.1 m from the lamp, eye level, extreme close-up on the lamp
with a shallow depth of field. Physically accurate perspective.

LIGHTING:
The lamp is the only light source in the frame. Its own hard-edged warm pool
falls below onto the table and rakes up across the hammered brass of the
shade, leaving the top of the stem dim. The starboard window behind is dark.
No halo of any kind around the shade. Spherical lens rendering, no horizontal
streak.

PHYSICS:
Weight in this room comes only from the ship's drive, so the lamp hangs along
whatever direction the drive pushes. At this moment the ship is running
straight and the lamp is exactly vertical.

Style: photorealistic, 35mm film grain, natural contrast, visible metal
texture, 0% bloom, no glow filter, no soft focus, no lens flare, no readable
text or letters or digits or symbols on any surface in the frame, no
watermark. Human count 0: the room is empty and no figures are in frame.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 5 of 12. Duration 10 seconds. Single unbroken take, no cuts.

CAMERA:
Fixed lockoff, 85mm, camera height 1.05 m, 2.1 m from the lamp, eye level,
extreme close-up on the lamp with a shallow depth of field. The camera does
not move, pan, tilt, zoom or track at any point.

ANCHOR:
A heavy brass pendant lamp on a braided cord fills the frame: matte closed
shade, hammered surface, worn lip, and one old dulled dent high on the stem.
Below it at the bottom edge, the edge of a low table with a brass key on a
leather tag. Behind and well out of focus, walnut panelling on screen-left and
the starboard window on screen-right. The room is empty of people and still.

TIMELINE:
0.0 s — The lamp hangs exactly vertical, completely still.
2.5 s — It begins to lean over toward screen-right, one slow continuous
movement, the cord staying taut and perfectly straight.
4.5 s — The lean stops at four degrees off vertical and holds there, with no
swing back, no overshoot and no oscillation.
6.5 s — The brass key on the table below begins to slide screen-right.
8.0 s — The key has travelled a hand's width screen-right and comes to rest
against the table rail. It does not slide back.
10.0 s — The lamp is still leaning four degrees over toward screen-right and
is completely motionless. No cuts.

PHYSICS:
Weight comes only from the ship's drive, so the lamp hangs along whatever
direction the drive pushes; when the ship steers, part of the thrust goes
sideways and down tilts screen-right by exactly that much. The lamp moves once
and stops. The key slides because the floor is no longer square to down,
travels a hand's width in about one and a half seconds and stops hard against
the rail. Everything that moves moves screen-right; nothing else moves at all.

AUDIO:
A low hull-borne hum, thin and steady, thickening very slightly as the lean
starts. The braided cord creaking once as it takes the new angle. Brass
sliding on wood, then one small knock as the key meets the rail. No speech.

Style: photorealistic, 35mm film grain, natural contrast, visible metal
texture, 0% bloom, no glow filter, no soft focus, no lens flare, no readable
text or letters or digits or symbols on any surface in frame, no watermark,
rigid contact with real collision and no merging. Human count 0: the room is
empty and no figures are in frame.

Output: 16:9, no text, no watermark.
```

---

## 🎬 SAHNE 5 — THE TIGHT CUT

```
SÜRE: 10,0 s  ·  BAŞLANGIÇ: 0:50  ·  VURUŞ: bahis yükselir
KURULUM: F — 50mm · close-up · over-the-shoulder · h 1,15 m · 1,1 m
YATMA: 4° → 22°   ·   EŞYA: 6 → 5   ·   İNSAN: 1
⛔ BÖLÜM SINIRI: bu sahne ile S6 arasında bir ölçek kademesi (close-up →
   medium shot) ve bir açı tipi (over-the-shoulder → profile) değişir.
⛔ D139: kamera arkada → sırt için POZİTİF yüzey cümlesi prompta girer.
```

### 📸 GÖRSEL PROMPT

```
Scene 6 of 12. Photorealistic, 16:9.

SUBJECT:
A woman in her late thirties, tall and square-shouldered, brown skin, black
hair drawn back into a low flat knot at the nape with no loose strands. High
cheekbones, a straight nose, a wide mouth, a matte dark red on the lips and no
other makeup. She wears a long charcoal wool coat-dress, single-breasted, cut
to the ankle, buttoned to the collarbone, with a narrow standing collar; the
wool has a visible flat weave and no pattern of any kind. The sleeves are
pushed back to the elbow and her forearms are bare. On her left wrist a plain
wide band of brushed brass with no face and no dial. Flat black leather shoes.
The back of the coat-dress is one continuous panel of charcoal wool from
collar to hem, unbroken, carrying nothing. Her hands are bare, the nails short
and unpainted. She is calm and unhurried; she is working, not enduring. We see
her from behind and slightly to the port side: her shoulder and the back of
her head fill the lower left of the frame, the wool of her back one clean
unbroken surface with nothing on it and nothing attached. Her right forearm is
extended, the hand well over on the brass wheel.

ENVIRONMENT:
The main saloon of a private long-range ship. Past her shoulder, filling the
upper right of the frame, the curved strip of glass that forms the bow wall,
with a hard black star field beyond it and the pale ringed point still high
and off centre, a little larger than before. At the right margin of the frame
the near edge of the starboard window, and beyond it a dusty orange world
running past, banded and soft-edged. There are no screens, no dials and no
gauges anywhere in the ship. The braided cord and lower body of the brass
pendant lamp cross the top of the frame, taut and straight and leaning well
over toward screen-right, twenty-two degrees off vertical, completely still.

CAMERA:
Shot on a 50mm lens from a fixed position 1.1 m behind her port shoulder,
camera height 1.15 m, over-the-shoulder close-up with her shoulder in the
lower left and the bow glass beyond. Physically accurate perspective.

LIGHTING:
Warm orange light from the dusty world enters wide through the starboard
window at the right margin and fills the whole frame from screen-right,
turning the walnut copper and putting a hard rim along her shoulder and the
edge of her jaw. The bow glass stays dark. Spherical lens rendering, no
horizontal streak.

PHYSICS:
Weight comes only from the ship's drive. Part of that thrust is now going
sideways, so down has tilted twenty-two degrees over toward screen-right: the
lamp hangs along that new direction, not along the wall. The floor and table
are unchanged and still square to the ship. Her weight has risen slightly and
the wool of her sleeve hangs a little more toward screen-right than before.

NEGATIVE:
Exactly 1 human character in frame — no duplicates, no clones, no second
person, no reflected figure, no shadow of anyone else. The back of the
coat-dress is one continuous panel of charcoal wool from collar to hem,
unbroken, carrying nothing: no pack, no harness, no strap, no housing. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible texture.
Photorealistic skin pores and fine lines retained — no airbrushing, no plastic
or waxy texture, no smoothed skin, no face morphing. No readable text,
letters, digits, numbers or symbols on any surface, plate or sign — not on the
clothing, not on the fittings, not on the brass, not on the panelling, not on
the glass and not on any object in the frame. Nothing in this room has been
measured, labelled, marked out or annotated by anyone: no scale marks, no
graduation ticks, no engraved or painted characters of any kind. No subtitles,
no captions, no title card, no watermark, no HUD overlay, no lens data, no
camera metadata, no name label. No mirrors and no mirrored surfaces. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers. All loose objects keep real weight — never
hovering, never frozen mid-air, never flowing like liquid. Room static and
stable — no melting surfaces, no warping topology, no swimming texture. No
lens flare, no anamorphic streak, no starburst. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 6 of 12. Duration 10 seconds. Single unbroken take, no cuts.

CAMERA:
Fixed lockoff, 50mm, camera height 1.15 m, 1.1 m behind her port shoulder,
over-the-shoulder close-up with her shoulder in the lower left of the frame
and the bow glass beyond. The camera does not move, pan, tilt, zoom or track
at any point.

ANCHOR:
The same saloon, over her port shoulder: the curved bow glass in the upper
right with one pale ringed point high and off centre, the starboard window at
the right margin with a dusty orange world running past, the brass lamp cord
across the top of the frame, and in the lower left a woman seen from behind,
the wool of her back one continuous panel from collar to hem, carrying
nothing.

TIMELINE:
0.0 s — The lamp cord leans four degrees over toward screen-right, taut and
still. Warm orange light fills the frame from screen-right.
2.0 s — She opens the wheel further, one smooth continuous movement.
3.5 s — The lamp goes out to twenty-two degrees off vertical over a second and
a half and stops there, no overshoot and no oscillation.
6.0 s — At the lower edge of the frame a rolled wool scarf slides screen-right
off the table and drops out of shot.
10.0 s — The lamp is still leaning at twenty-two degrees and is completely
motionless. Her shoulder has not turned. No cuts.

PHYSICS:
Weight comes only from the ship's drive. Part of it now goes sideways, so down
has tilted twenty-two degrees over toward screen-right and the lamp hangs
along that new direction, moving once and stopping. The scarf slides because
the floor is no longer square to down, leaves the table in under a second and
falls at real weight, never hovering. The light is on her screen-right side
and she does not turn into it. No direction reversal.

AUDIO:
A low hull-borne hum, thicker and lower than before, settling at the new
level. Brass turning against brass, the cord creaking as it takes the angle,
and a soft fall out of frame. No speech.

NEGATIVE:
Exactly 1 human character in frame — no second person, no clones, no reflected
figure. The back of the coat-dress is one continuous panel of charcoal wool
from collar to hem, unbroken, carrying nothing. 0% bloom, no glow filter, no soft focus. No readable text, letters,
digits or symbols on any surface in frame. No subtitles, no title card, no watermark. Photorealistic skin texture, no waxy rendering.
Loose objects keep real weight, never hovering, never frozen. Rigid contact, no merging,
no extra fingers. No mirrors, no lens flare.
Photorealistic with 35mm film grain.

Output: 16:9, no text, no watermark.
```
