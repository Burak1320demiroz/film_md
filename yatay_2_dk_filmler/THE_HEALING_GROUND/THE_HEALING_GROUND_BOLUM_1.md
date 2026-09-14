# 🎬 THE HEALING GROUND — BÖLÜM 1  (S0 – S6)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_HEALING_GROUND_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF
> YAPMAZ — her prompt tek başına çalışır (AGENTS §2 kural ③).
>
> Izgara: 9 s hook + 13 × 10 s = 139 s. Sahne başlangıcı(n) = 9 + (n−1) × 10.
> Bölüm sınırı ardışık bir çifttir: S6 (F · MS · azimut 180°) ↔ S7 (E · WS ·
> tepe −90°) → ölçek 1 kademe, açı 82°. Denetimi klasör modu yapar:
> `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <film klasörü>`

```
NOVUM TAŞIYICISI:  ölçüm diski × iki eldivenle zemine bastırma jesti →
                   diskin kenarından ince beyaz bir buhar yakası kalkıyor ve
                   soluk örtü diskin üstüne yürüyüp onu kapatıyor
TEK KARE (ONERME §4①): S0 · 0:08 — soluk ovada koyu ölçüm diskinin üstü
                   yarıya kadar soluk bir örtüyle kapanmış; açıkta kalan
                   kenarında buhar yakası hâlâ dik; eldiven bir el yanda.
```

---

## 🎬 SAHNE 0 — THE LAST DISC

```
SÜRE: 9 s · başlangıç 0,0 s   ·   VURUŞ: açılış imajı + katalizör (0:07)
KURULUM: C · 35mm · MS · ALT AÇI 22° · kamera 0,45 m yükseklikte · 4,0 m
⭐ KAPAK ANI: 0:04   ·   VARLIK KADEMESİ: K1 (çevresel tepki)
```

### 📸 GÖRSEL PROMPT

```
Scene 1 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. A man in his
fifties, grey hair, deep lines at the outer eyes, sealed in a matte dark
slate-grey pressure suit. A bold ochre-yellow band is wrapped all the way
around the RIGHT forearm and all the way around the RIGHT thigh. The
helmet is a plain rounded shell with four small box-shaped lamps across
the brow, all four unlit; the visor is optically clear glass with zero
tint, zero mirror coating and zero reflection of the environment, and his
face is fully readable through it at every head angle. The back of the
suit is one continuous smooth panel from collar to hip, carrying nothing,
and his back silhouette is flat. A flat chest module sits at the centre
of his chest with a plain hinged cover and one recessed metal latch. A
fine white vapour plume, about as long as his forearm, stands from a vent
below his RIGHT hip. Fixed wear that never moves: a thin pale scratch
along the LEFT forearm SLEEVE of the suit, a pale scuffed patch on the
RIGHT knee panel, and the lower edge of the ochre band on the right thigh
rubbed dull. No bare skin anywhere — none above the collar, none at the
wrists between glove and sleeve, none at the ankles between boot and leg;
every seam is closed and every seal ring is visible.

ACTION: He is down on one knee, already halfway through the movement,
pressing a dark blued-steel disc the width of his palm flat into the
floor with both gloves stacked on it. The glove's ribbed segments tighten
and lift over the knuckles as he presses.

ENVIRONMENT: A dead-flat plain running to a hard unbroken horizon. The
floor is a fine pale mat the colour of dry bone, a few centimetres deep
over hard water ice, one continuous crust with no seams, no rocks and no
dunes. Behind him, receding to the horizon in the left third of the
frame, a row of low white domes, evenly spaced, each about the size of a
dinner plate. The air is a still dense nitrogen-methane mix. Above him
there is only unbroken amber-brown haze — no sun disc, no beam, no bright
spot anywhere in the sky.

CAMERA: Shot on a 35mm lens from a fixed position four metres away, low
angle, camera height 0.45 metres, three-quarter view of the kneeling
figure. Horizon level and in the lower third. Physically accurate
perspective, realistic scale relationships.

LIGHTING: Soft shadowless daylight arriving from the whole sky dome;
shadows shallow and soft-edged, never black. A low rim of sky-light
separates his shoulders and helmet from whatever is behind him; his
silhouette never merges with the background. 0% bloom, no glow filter,
no lens flare.

PHYSICS: Gravity 0.38 g. A thin white collar of vapour has just risen
around the rim of the disc, standing straight up about half the height of
his glove; it is made of a few dozen separate motes and the horizon stays
visible through it.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person. 0% bloom, no glow filter, no soft focus — every surface
keeps visible texture. No readable text, letters, digits, numbers or
symbols on any display, surface, patch or sign — not on the suit, not on
the equipment, and not on the ground or any natural surface in frame.
Nothing in this world has been measured, labelled or annotated by anyone:
no scale marks, no graduation ticks, no engraved characters of any kind.
No HUD overlay, no lens data, no name label, no subtitle, no lower third,
no watermark. No hovering, no floating particles, no liquid anywhere. No
Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 1 of 14. Duration 9 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character — no clones, no second person, no reflection or
shadow of anyone else. A man in his fifties, grey hair, deep lines at the
outer eyes, in a matte dark slate-grey pressure suit; an ochre-yellow band
around the RIGHT forearm and RIGHT thigh. Visor optically clear, zero tint,
zero mirror coating, face fully readable. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing. No bare skin
anywhere — none above the collar, none at the wrists between glove and
sleeve, none at the ankles between boot and leg.

WORLD: a dead-flat plain to a hard horizon; the floor is a fine pale mat the
colour of dry bone, one continuous crust, no seams, no rocks. A
row of low white domes recedes behind him in the left third of the frame.
Above him only unbroken amber-brown haze — no sun disc, no beam, no bright
spot.

CAMERA: lockoff, 35mm, four metres away, low angle, camera height 0.45
metres, three-quarter view. Camera never moves, pans, tilts or zooms.

TIMELINE:
0.0s — he is already halfway down onto one knee, both gloves stacked on a dark
blued-steel disc the width of his palm, pressing it flat into the pale floor.
His shoulders drop below the line of his hips and the rear boot loads before
he leans.
2.0s — a thin white collar of vapour rises straight up around the rim of the
disc, half the height of his glove. Two breaths per press, the second one
shorter than the first.
4.0s — he takes his gloves off it and sits back on his heel; the disc lies
flat and dark against the pale mat.
5.5s — the pale floor begins to move: from every side it draws in over the
edge of the disc, a slow even creep, and the vapour collar leans inward.
8.0s — the disc is gone. A low white dome stands where it was, and his glove
is still resting one hand's width from it.

AUDIO: a dense low wind bed, close and heavy; the dry contact of a glove on
frozen crust; a soft hiss as the vapour collar rises and falls. No music. No
dialogue in this scene.

PHYSICS: gravity 0.38 g. The vapour rises straight and falls straight back as
fine dry snow within two seconds; it never curls and never hangs.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic.

Output: 16:9, no text, no watermark. No cuts.
```

---

## 🎬 SAHNE 1 — THE LINE

```
SÜRE: 10 s · başlangıç 9,0 s   ·   VURUŞ: kurulum + ⭐TOHUM (0:15-0:17)
KURULUM: A · 24mm · EWS · GÖZ HİZASI · kamera 1,60 m · 40 m
VARLIK KADEMESİ: K0
```

### 📸 GÖRSEL PROMPT

```
Scene 2 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. A man in his
fifties, grey hair, deep lines at the outer eyes, sealed in a matte dark
slate-grey pressure suit. A bold ochre-yellow band is wrapped all the way
around the RIGHT forearm and all the way around the RIGHT thigh. The
helmet is a plain rounded shell with four small box-shaped lamps across
the brow, all four unlit; the visor is optically clear glass with zero
tint, zero mirror coating and zero reflection of the environment. The
back of the suit is one continuous smooth panel from collar to hip,
carrying nothing, and his back silhouette is flat. A fine white vapour
plume, about as long as his forearm, stands from a vent below his RIGHT
hip. Fixed wear that never moves: a thin pale scratch along the LEFT
forearm SLEEVE of the suit, a pale scuffed patch on the RIGHT knee panel,
and the lower edge of the ochre band on the right thigh rubbed dull. No
bare skin anywhere — none above the collar, none at the wrists between
glove and sleeve, none at the ankles between boot and leg.

ACTION: He stands in the lower centre of the frame, small against the
plain, his head turned to look along the row behind him.

ENVIRONMENT: A dead-flat plain running to a hard unbroken horizon in
every direction. The floor is a fine pale mat the colour of dry bone, one
continuous crust with no seams, no rocks, no ridges and no dunes. A row
of low white domes runs from his boots back into the distance and shrinks
to nothing at the horizon, evenly spaced, each about the size of a dinner
plate. Far off in the background right third of the frame, standing alone
on the horizon line, one thin dark vertical rod, no taller than a man's
arm, with no dome around its base — it is the only other upright thing in
this world. Above him there is only unbroken amber-brown haze: no sun
disc, no beam, no bright spot anywhere in the sky.

CAMERA: Shot on a 24mm lens from a fixed position forty metres away, eye
level, camera height 1.60 metres, frontal. Horizon level and in the lower
third of the frame; above him there is only haze. Physically accurate
perspective, realistic scale relationships, correct sense of distance.

LIGHTING: Soft shadowless daylight from the whole sky dome; shadows
shallow, soft-edged, never black. A low rim of sky-light separates his
shoulders and helmet from whatever is behind him; his silhouette never
merges with the background. 0% bloom, no glow filter, no lens flare.

PHYSICS: Gravity 0.38 g. The air is dense and still; nothing is raised by
wind, no fabric flutters, no dust is lifted anywhere in the frame.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person. 0% bloom, no glow filter, no soft focus — every surface
keeps visible texture. No readable text, letters, digits, numbers or
symbols on any display, surface, patch or sign, and none on the ground or
any natural surface in frame. No scale marks, no graduation ticks, no
engraved characters of any kind. No HUD overlay, no lens data, no name
label, no subtitle, no watermark. No canyon walls, no hills, no rock
formations, no mountains — the plain is flat to the horizon on all sides.
No hovering particles, no liquid. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 2 of 14. Duration 10 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character — no clones, no second person, no reflection or
shadow of anyone else. A man in his fifties, grey hair, deep lines at the
outer eyes, in a matte dark slate-grey pressure suit; an ochre-yellow band
around the RIGHT forearm and RIGHT thigh. Visor optically clear, zero tint,
zero mirror coating, face fully readable. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing. No bare skin
anywhere — none above the collar, none at the wrists between glove and
sleeve, none at the ankles between boot and leg. A fine white vapour plume, about as long as his forearm, stands from a
vent below his RIGHT hip.

WORLD: a dead-flat plain to a hard horizon; the floor is a fine pale mat the
colour of dry bone, one continuous crust, no seams, no rocks. A
row of low white domes runs from his boots back into the distance and shrinks
to nothing at the horizon. Above him there is only unbroken amber-brown haze —
no sun disc, no beam, no bright spot.

CAMERA: lockoff, 24mm, forty metres away, eye level, camera height 1.60
metres, frontal. Horizon level, lower third. Camera never moves, pans, tilts
or zooms.

TIMELINE:
0.0s — he is standing up out of the kneel, still finishing the movement, small
in the lower centre of the frame.
3.0s — he turns his head and looks along the row of domes running back from
his boots to the horizon.
6.0s — he takes two slow steps along that row, screen-right, staying level
with the horizon line.
6.5s — far off on the horizon line, in the background right third of the
frame, one thin dark vertical rod stands alone with no dome around its base.
It is simply there; he does not look at it and the camera does not move.
9.0s — he stops. The vapour plume at his right hip leans once and settles.

AUDIO: a wide low wind bed, further off than the last shot; two muffled boot
contacts; no high frequencies. The first low sustained music tone enters at
6.0s, very quiet. No dialogue.

PHYSICS: gravity 0.38 g; the air is dense and still. Wind moves nothing: no
fabric flutter, no raised dust, nothing pushed.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic. No canyon walls, no hills, no rock formations — the plain is flat to the
horizon.

Output: 16:9, no text, no watermark. No cuts.
```

---

## 🎬 SAHNE 2 — WHAT THE BOOT LEAVES

```
SÜRE: 10 s · başlangıç 19,0 s   ·   VURUŞ: tartışma · 🎭 MOTİF (kinesik)
KURULUM: B · 100mm makro · ECU · ÜST AÇI (high angle) · kamera 0,90 m · 0,7 m
VARLIK KADEMESİ: K1  ·  KURAL DOĞRULAMA #1 (ikinci nesne: bot izi)
```

### 📸 GÖRSEL PROMPT

```
Scene 3 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. Only one boot
and the lower leg of the man are in shot: a matte dark slate-grey
pressure suit leg, sealed, with a pale scuffed patch on the RIGHT knee
panel just at the top edge of frame. The boot sole is deeply lugged. No
bare skin anywhere — none above the collar, none at the wrists between
glove and sleeve, none at the ankles between boot and leg; every seam is
closed and the ankle seal ring is visible.

ACTION: The boot has just lifted clear of the floor and hangs a hand's
width above its own print.

ENVIRONMENT: Extreme close view of the floor: a fine pale mat the colour
of dry bone, a few centimetres deep over hard water ice, one continuous
crust with a fine felted texture and no seams. In the print left by the
boot, the crust has already begun to swell upward into a smooth low white
blister that is filling the tread pattern from underneath. A thin white
collar of vapour stands around the print, no higher than a thumb.

CAMERA: Shot on a 100mm macro lens from a fixed position seventy
centimetres from the ground, high angle looking down at the floor, camera
height 0.90 metres. Shallow depth of field, the far crust falling out of
focus. Physically accurate perspective.

LIGHTING: Soft shadowless daylight from the whole sky dome; the shadow
under the boot is shallow and soft-edged, never black. A low rim of
sky-light separates the boot from the floor behind it. 0% bloom, no glow
filter, no lens flare.

PHYSICS: Gravity 0.38 g. The vapour is made of a few dozen separate motes
rising straight; the crust stays visible through it. Nothing hovers.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person, no other limb in frame. 0% bloom, no glow filter, no
soft focus — the crust keeps visible texture. No readable text, letters,
digits, numbers or symbols on any surface, patch or sign, and none on the
ground or any natural surface in frame. No scale marks, no graduation
ticks, no engraved characters of any kind. No HUD overlay, no lens data,
no name label, no subtitle, no watermark. No liquid, no wet surface, no
droplets. No hovering particles. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 3 of 14. Duration 10 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character in frame — no clones, no second person, no
reflection or shadow of anyone else. Only one boot and the lower leg are in
shot: a matte dark slate-grey pressure suit leg, sealed, a pale scuffed patch
on the RIGHT knee panel at the top edge of frame, the boot sole deeply lugged.
The back of the suit is one continuous smooth panel from collar to hip,
carrying nothing. No bare skin anywhere — none above the collar, none at the
wrists between glove and sleeve, none at the ankles between boot and leg; the
ankle seal ring is visible.

WORLD: extreme close view of the floor — a fine pale mat the colour of dry
bone over hard water ice, one continuous felted crust with no seams and no
rocks.

CAMERA: lockoff, 100mm macro, seventy centimetres from the ground, high
angle looking down at the floor, camera height 0.90 metres. Camera never moves, pans,
tilts or zooms.

TIMELINE:
0.0s — the boot is already lifting, hanging a hand's width above a fresh tread
print in the pale crust. The rear boot loads and the knee bends before he
lifts.
1.5s — a thin white collar of vapour stands up out of the print, no higher
than a thumb, and leans nowhere.
3.0s — the print begins to fill from underneath: the crust swells into a
smooth low white blister and the tread pattern disappears into it.
6.0s — the blister stops rising. The floor where he stepped is flat white and
featureless again, as if nothing had been set down on it.
7.5s — the boot comes back down beside it, deliberately, and holds. The same
swelling starts again at once around the new print.

AUDIO: a dense low wind bed, quieter and closer than the wide shot; a crisp
dry crunch as the boot leaves the crust; a fine papery hiss as the blister
rises. No music under this scene. No dialogue here.

PHYSICS: gravity 0.38 g. The vapour is a few dozen separate motes rising
straight and falling straight back as dry snow within two seconds. The blister
rises at a steady creep and never overshoots.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic. No wet surface, no droplets.

Output: 16:9, no text, no watermark. No cuts.
```

---

## 🎬 SAHNE 3 — THE COUNT OF ONE

```
SÜRE: 10 s · başlangıç 29,0 s   ·   VURUŞ: tartışma · 🎒 eşya · 👁️ göz #2
KURULUM: D · 75mm · CU · TAM PROFİL · GÖZ HİZASI · kamera 1,55 m · 2,0 m
VARLIK KADEMESİ: K0
```

### 📸 GÖRSEL PROMPT

```
Scene 4 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. A man in his
fifties, grey hair, deep lines at the outer eyes, sealed in a matte dark
slate-grey pressure suit, seen in full profile. The helmet is a plain
rounded shell with four small box-shaped lamps across the brow, all four
unlit; the visor is optically clear glass with zero tint, zero mirror
coating and zero reflection of the environment, and his face is fully
readable through it in profile. A flat chest module sits at the centre of
his chest with a plain hinged cover and one recessed metal latch. The
back of the suit is one continuous smooth panel from collar to hip,
carrying nothing. A thin pale scratch runs along the LEFT forearm SLEEVE
of the suit. No bare skin anywhere — none above the collar, none at the
wrists between glove and sleeve, none at the ankles between boot and leg.

ACTION: He holds a dark blued-steel disc the width of his palm flat on
his open right glove, at chest height, and is turning it over with his
left thumb. His eyes are down on it, not on the horizon.

ENVIRONMENT: Behind him, thrown far out of focus, the pale plain and one
low white dome; above that, unbroken amber-brown haze with no sun disc
and no bright spot.

CAMERA: Shot on a 75mm lens from a fixed position two metres away, eye
level, camera height 1.55 metres, full profile — the lens is square to
the side of his helmet. Shallow depth of field. Physically accurate
perspective.

LIGHTING: Soft shadowless daylight from the whole sky dome; shadows
shallow and soft-edged, never black. A low rim of sky-light separates his
helmet and shoulder from whatever is behind him; his silhouette never
merges with the background. 0% bloom, no glow filter, no lens flare, no
reflection on the visor glass.

PHYSICS: Gravity 0.38 g. The disc is a solid rigid object with a clear
structural boundary against the glove — no merging, no phasing, no extra
fingers.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person, no reflected face in the visor. 0% bloom, no glow
filter, no soft focus on the face. No readable text, letters, digits,
numbers or symbols on any display, surface, patch or sign — the disc
carries no mark, no engraving, no number and no stamp of any kind. No
scale marks, no graduation ticks. No HUD overlay, no lens data, no name
label, no subtitle, no lower third, no watermark. No liquid, no droplets.
No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film
grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 4 of 14. Duration 10 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character — no clones, no second person, no reflection or
shadow of anyone else. A man in his fifties, grey hair, deep lines at the
outer eyes, in a matte dark slate-grey pressure suit; an ochre-yellow band
around the RIGHT forearm and RIGHT thigh. Visor optically clear, zero tint,
zero mirror coating, face fully readable. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing. No bare skin
anywhere — none above the collar, none at the wrists between glove and
sleeve, none at the ankles between boot and leg. He is seen in full profile. A flat chest module sits at the centre of
his chest with a plain hinged cover and one recessed metal latch.

WORLD: behind him, far out of focus, the pale plain and one low white dome;
above that, unbroken amber-brown haze with no sun disc, no beam and no bright
spot.

CAMERA: lockoff, 75mm, two metres away, eye level, camera height 1.55
metres, full profile — square to the side of his helmet. Camera never moves, pans,
tilts or zooms.

TIMELINE:
0.0s — he is already lifting a dark blued-steel disc the width of his palm out
of the chest module; his grip tightens on it before it comes free.
2.5s — he lays the disc flat on his open right glove at chest height and turns
it over once with his left thumb. His eyes go down to it.
5.0s — he closes his glove around it and holds. His mouth stays closed and
does not move at any point in this shot.
7.0s — he puts it back inside the chest module and presses the cover shut; the
recessed latch clicks flat.
9.0s — he lifts his head and looks ahead, out of frame past the lens.

AUDIO: a dense low wind bed, distant; slow breathing inside the helmet, close
and dry; the hard click of the latch at 7.0s. One quiet sustained low music
tone continues underneath. No dialogue here.

PHYSICS: gravity 0.38 g. The disc is rigid and keeps a clear structural
boundary against the glove — no merging, no phasing, no extra fingers.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic. No reflected face in the visor; the disc carries no mark, no engraving
and no stamp.

Output: 16:9, no text, no watermark. No cuts.
```

---

## 🎬 SAHNE 4 — UNDER THE SHEET

```
SÜRE: 10 s · başlangıç 39,0 s   ·   VURUŞ: K2 · 🔁 Kuleshov #1 · R1 (41,0 s)
KURULUM: B · 100mm makro · ECU · ÜST AÇI (high angle) · kamera 0,90 m · 0,7 m
VARLIK KADEMESİ: K2 (PARÇA — yalnız kadrajın gördüğü kenar; SAYI YAZILMAZ)
```

### 📸 GÖRSEL PROMPT

```
Scene 5 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. Only one glove
is in shot, resting open on the floor at the bottom edge of frame: a
matte dark slate-grey pressure glove with ribbed segments across the
knuckles and a closed seal ring at the wrist. No bare skin anywhere —
none at the wrist between glove and sleeve, none above the collar, none
at the ankles between boot and leg.

ACTION: The glove is still. Nothing is being held.

ENVIRONMENT: Extreme close view of a fresh low white dome in the pale
crust, the size of a dinner plate, smooth and featureless. At the near
edge of the dome, a hand's width of pale translucent rim has slid clear
of the crust and lies there, thin as a folded glove, its outer edge bent
down onto the floor. Frost has lifted along the short line it moved and
is settling again. Nothing else of it is visible: the rest is under the
crust and stays under the crust.

CAMERA: Shot on a 100mm macro lens from a fixed position seventy
centimetres from the ground, high angle looking down at the floor, camera
height 0.90 metres. Shallow depth of field. Physically accurate
perspective.

LIGHTING: Soft shadowless daylight from the whole sky dome; the shadow
under the raised rim is shallow and soft-edged, never black. A low rim of
sky-light separates the pale rim from the crust behind it. 0% bloom, no
glow filter, no lens flare.

PHYSICS: Gravity 0.38 g. Lifted frost is a few dozen separate motes and
settles again within half a second; nothing hangs in the air.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person. Only one pale rim in frame and no other creature
anywhere — the plain around it is empty crust. 0% bloom, no glow filter,
no soft focus — every surface keeps visible texture. No readable text,
letters, digits, numbers or symbols on any surface, and none on the
ground or any natural surface in frame. No HUD overlay, no lens data, no
name label, no subtitle, no watermark. No liquid, no wet surface, no
droplets, no slime. No hovering particles. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 5 of 14. Duration 10 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character — no clones, no second person, no reflection or
shadow of anyone else. Only one glove and forearm are in shot: a matte dark
slate-grey pressure glove, ribbed segments across the knuckles, a closed seal
ring at the wrist. The back of the suit is one continuous smooth panel from
collar to hip, carrying nothing. No bare skin anywhere — none at the wrist
between glove and sleeve, none above the collar, none at the ankles between
boot and leg. The glove rests open on the floor at the bottom edge of frame.

WORLD: extreme close view of a fresh low white dome in the pale crust, the
size of a dinner plate, smooth and featureless, over hard water ice.

CAMERA: lockoff, 100mm macro, seventy centimetres from the ground, high
angle looking down at the floor, camera height 0.90 metres. Camera never moves, pans,
tilts or zooms.

TIMELINE:
0.0s — the dome sits still and smooth; the open glove rests on the crust at
the bottom edge of frame and does not move at any point.
2.0s — his recorded voice plays back from the chest module, off-screen only — no
mouth in frame, no on-screen speaker — flat and tired: "The last one's gone under. Same as the others."
4.5s — at the near edge of the dome the crust parts and a hand's width of pale
translucent rim slides clear of it, thin as a folded glove.
6.0s — it pauses mid-motion for a breath, then continues, moving a finger's
width further into the open. Fine frost lifts and resettles along the line it
passes.
8.5s — it settles back slowly under the crust and the surface closes smooth
again. The glove has not moved.

AUDIO: a dense low wind bed, very quiet; a dry sliding sound like a hand under
a sheet; the recorded line at 2.0s, heard only, never shown as text, with a
faint playback filter on it. No music under this scene.

PHYSICS: gravity 0.38 g. Lifted frost is a few dozen separate motes and
settles within half a second. The rim moves with unequal acceleration and
never snaps back.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic. Only one pale rim in frame, no other creature anywhere. No subtitles, no
captions, no wet surface, no slime.

Output: 16:9, no text, no watermark. No cuts.
```

---

## 🎬 SAHNE 5 — HOLDING IT DOWN

```
SÜRE: 10 s · başlangıç 49,0 s   ·   VURUŞ: tırmandırma (yetkin çözüm başarısız)
KURULUM: A · 24mm · EWS · GÖZ HİZASI · kamera 1,60 m · 40 m
VARLIK KADEMESİ: K1  ·  🚶 tam boy yürüyüş bütçesi
```

### 📸 GÖRSEL PROMPT

```
Scene 6 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. A man in his
fifties, grey hair, deep lines at the outer eyes, sealed in a matte dark
slate-grey pressure suit. A bold ochre-yellow band is wrapped all the way
around the RIGHT forearm and all the way around the RIGHT thigh. The
visor is optically clear glass with zero tint, zero mirror coating and
zero reflection of the environment. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing, and his
back silhouette is flat. A fine white vapour plume, about two thirds the
length of his forearm, stands from a vent below his RIGHT hip. Fixed wear
that never moves: a thin pale scratch along the LEFT forearm SLEEVE of
the suit, a pale scuffed patch on the RIGHT knee panel.

ACTION: He stands in the lower centre of the frame with his weight
forward on one boot, pinning a dark blued-steel disc to the floor under
the sole. His shoulders are low and his rear boot is loaded.

ENVIRONMENT: A dead-flat plain running to a hard unbroken horizon in
every direction. The floor is a fine pale mat the colour of dry bone, one
continuous crust with no seams, no rocks and no dunes. A row of low white
domes runs back from him into the distance. Above him there is only
unbroken amber-brown haze: no sun disc, no beam, no bright spot anywhere.

CAMERA: Shot on a 24mm lens from a fixed position forty metres away, eye
level, camera height 1.60 metres, frontal. Horizon level and in the lower
third of the frame; above him there is only haze. Physically accurate
perspective, realistic scale relationships.

LIGHTING: Soft shadowless daylight from the whole sky dome; shadows
shallow and soft-edged, never black. A low rim of sky-light separates his
shoulders and helmet from whatever is behind him; his silhouette never
merges with the background. 0% bloom, no glow filter, no lens flare.

PHYSICS: Gravity 0.38 g. A ring of white vapour stands around the pinned
boot, no higher than his knee, made of a few dozen separate motes; the
horizon stays visible through it.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person. 0% bloom, no glow filter, no soft focus. No readable
text, letters, digits, numbers or symbols on any surface, patch or sign,
and none on the ground or any natural surface in frame. No scale marks,
no graduation ticks. No HUD overlay, no lens data, no name label, no
subtitle, no watermark. No canyon walls, no hills, no rock formations —
the plain is flat to the horizon on all sides. No liquid, no hovering
particles. No Unreal Engine look, no CGI aesthetic. Photorealistic with
35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 6 of 14. Duration 10 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character — no clones, no second person, no reflection or
shadow of anyone else. A man in his fifties, grey hair, deep lines at the
outer eyes, in a matte dark slate-grey pressure suit; an ochre-yellow band
around the RIGHT forearm and RIGHT thigh. Visor optically clear, zero tint,
zero mirror coating, face fully readable. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing. No bare skin
anywhere — none above the collar, none at the wrists between glove and
sleeve, none at the ankles between boot and leg. A fine white vapour plume, about two thirds the length of his forearm,
stands from a vent below his RIGHT hip.

WORLD: a dead-flat plain to a hard horizon; the floor is a fine pale mat the
colour of dry bone, one continuous crust, no seams, no rocks. A
row of low white domes runs back from him into the distance. Above him only
unbroken amber-brown haze — no sun disc, no beam, no bright spot.

CAMERA: lockoff, 24mm, forty metres away, eye level, camera height 1.60
metres, frontal. Horizon level, lower third. Camera never moves, pans, tilts
or zooms.

TIMELINE:
0.0s — he is mid-stride, already setting a dark blued-steel disc down on the
crust in front of his boot.
2.0s — he puts the sole of that boot on the disc and leans into it; his
shoulders drop below the line of his hips and the rear boot loads before he
leans.
4.0s — a ring of white vapour stands up around the pinned boot, no higher than
his knee, and the crust begins to swell around the sole.
7.0s — he steps off and back. The crust closes over the place at once and keeps
the tread shape on top of the new dome.
9.5s — he stands still with his arms down. Two breaths per press, the second
one shorter than the first.

AUDIO: a wide low wind bed; the load of a boot on frozen crust; a long soft
hiss while the vapour ring stands. One low music tone underneath. No dialogue here.

PHYSICS: gravity 0.38 g. Low gravity reduces weight, not mass: his shoulders
and rear boot pay for the disc. Vapour rises straight and falls back as dry
snow within two seconds.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic. No canyon walls, no hills, no rock formations — the plain is flat to the
horizon.

Output: 16:9, no text, no watermark. No cuts.
```

---

## 🎬 SAHNE 6 — SOMETHING CROSSES

```
SÜRE: 10 s · başlangıç 59,0 s   ·   VURUŞ: orta nokta (bahis yükselir)
KURULUM: F · 50mm · MS · OMUZ ÜSTÜ (over-the-shoulder, arkadan) · kamera 1,60 m · 2,4 m
VARLIK KADEMESİ: K3 (SİLUET — pus içinde, anatomi SAYISI yazılmaz)
⛔ D139 · prompt_kontrol ⑮: kamera arkada → POZİTİF sırt yüzeyi cümlesi ZORUNLU
```

### 📸 GÖRSEL PROMPT

```
Scene 7 of 14. Photorealistic live-action still, 35mm film grain.

SUBJECT: Exactly one human character in frame — no duplicates, no clones,
no second person, no reflection or shadow of anyone else. A man in his
fifties in a matte dark slate-grey pressure suit, seen from behind at the
right edge of frame, his head and right shoulder filling the near
foreground. The back of the suit is one continuous smooth panel from
collar to hip, unbroken, carrying nothing — a single smooth surface with
one flat vertical seam down its centre and no housing, no unit and no
fitting of any kind on it. A bold ochre-yellow band is wrapped all the
way around the RIGHT forearm. No bare skin anywhere — none above the
collar, none at the wrists between glove and sleeve, none at the ankles
between boot and leg.

ACTION: He stands still, facing away from the lens, looking out across
the plain.

ENVIRONMENT: Past his shoulder, the pale plain runs flat to a hard
horizon under unbroken amber-brown haze; no sun disc, no beam, no bright
spot. In the middle distance, screen-left of his shoulder, a low wide
flat shape lies on the crust — an outline only, softened by haze and
distance, its edges unresolved. Two low white domes sit between it and
the camera.

CAMERA: Shot on a 50mm lens from a fixed position two point four metres
behind him, over-the-shoulder framing, camera height 1.60 metres, the
lens looking past his right shoulder. Shallow depth of field: his
shoulder sharp, the plain and the flat shape softer. Physically accurate
perspective.

LIGHTING: Soft shadowless daylight from the whole sky dome; shadows
shallow and soft-edged, never black. A low rim of sky-light separates his
shoulder and helmet from whatever is behind him; his silhouette never
merges with the background. 0% bloom, no glow filter, no lens flare.

PHYSICS: Gravity 0.38 g. The air is dense and still; nothing is raised by
wind anywhere in the frame.

NEGATIVE: Single unbroken frame, exactly one human character, no clones,
no second person. Only one flat shape on the plain and no other creature
anywhere. No backpack, no tank, no hose, no cable and no rear housing —
the back is one continuous smooth panel. 0% bloom, no glow filter, no
soft focus on the shoulder. No readable text, letters, digits, numbers or
symbols on any surface, patch or sign, and none on the ground in frame.
No HUD overlay, no lens data, no name label, no subtitle, no watermark.
No liquid, no hovering particles. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Scene 7 of 14. Duration 10 seconds. Photorealistic live-action, 35mm film grain.
Exactly one human character in frame — no clones, no second person, no
reflection or shadow of anyone else. A man in his fifties in a matte dark
slate-grey pressure suit, seen from behind at the right edge of frame, head
and right shoulder in the near foreground. The back of the suit is one
continuous smooth panel from collar to hip, unbroken, carrying nothing — a single flat vertical seam, no housing, unit or fitting on it. An ochre-yellow band is wrapped around the RIGHT forearm. No
bare skin anywhere — none above the collar, none at the wrists between glove
and sleeve, none at the ankles between boot and leg.

WORLD: past his shoulder the pale crust runs flat to a hard horizon under
unbroken amber-brown haze; no sun disc, no beam, no bright spot. Two low white
domes sit between the camera and the far plain.

CAMERA: lockoff, 50mm, two point four metres behind him,
over-the-shoulder framing, camera height 1.60 metres, looking past his right
shoulder. Camera never moves, pans, tilts or zooms.

TIMELINE:
0.0s — he is already still, facing away from the lens, and the plain beyond
him is empty.
2.5s — in the middle distance, screen-left of his shoulder, a low wide flat
shape comes into the open and crosses the crust, an outline only, softened by
haze — it moves the way a ray moves over a seabed.
5.0s — it pauses mid-motion for a breath, then continues. Fine frost lifts and
resettles along the line it passes.
7.0s — it reaches the nearest of the white domes, slows, and stops on top of
it. The outline settles and stops moving.
9.0s — his helmet turns a few degrees to keep it in view. Nothing else in the
frame moves.

AUDIO: a low wind bed; a long dry sliding sound, low and close, in time with
the shape; slow breathing inside the helmet. A low music layer enters at 2.5s. No dialogue here.

PHYSICS: gravity 0.38 g. The shape has mass: frost lifts where it passes and
settles again within half a second. It moves with unequal acceleration, never
in a perfect repeating cycle and never with a snap.

NEGATIVE: single unbroken take, no cuts, no angle change. Exactly one human
character. 0% bloom, no glow filter, no soft focus. No readable text, letters
or digits anywhere in frame. No HUD overlay, no name label, no subtitle, no
watermark. No liquid, no hovering particles, no CGI aesthetic. Only one flat shape on the plain, no other creature anywhere. No
backpack, no tank, no hose, no cable, no rear housing.

Output: 16:9, no text, no watermark. No cuts.
```
