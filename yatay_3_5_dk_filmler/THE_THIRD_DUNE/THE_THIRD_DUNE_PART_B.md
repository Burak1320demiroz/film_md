# 🏜️ THE THIRD DUNE — Üçüncü Tepe | PART B

## AI Production Bible — Self-Contained Prompts
### PART B: Sahne 13-24 (12 sahne) | 16:9 Yatay | Görsel + Video + Diyalog
### _"Geri dönebilmek için, gitmene sebep olan şeyi bırakman gerekebilir."_

> **PART B süresi:** 12 sahne × 10s = 120 saniye (2:09 → 4:09)
> **Toplam film:** 25 sahne = 249 saniye = 4 dakika 09 saniye
> **PART A:** `THE_THIRD_DUNE_PART_A.md` (S0-S12) — **Bible'lar orada**
> **Plan:** `THE_THIRD_DUNE_PLAN.md` · **Müzik/ses:** `THE_THIRD_DUNE_MUZIK.md`

---

# 📖 BÖLÜM 1 — BIBLE REFERANSI + PART B'YE ÖZEL ÇAPALAR

> ⚠️ Tüm Bible'lar (World · Ship · Character · Camera · Lighting · Physics
> · Negative · Dust State · Spatial Lock) **PART A BÖLÜM 1'dedir** ve
> burada TEKRARLANMAZ — bir bilgi iki yerde durursa ayrışır.
> **Ama promptlar yine self-contained'dır** [kural ③]: aşağıdaki bloklar
> her prompta birebir kopyalanmıştır, hiçbir prompt bu dosyaya ya da
> PART A'ya atıf yapmaz.

## ⚓ PART A'DAN DEVRALINAN ÇAPA BLOKLARI (birebir aynı)

```
① ÇİFT BLOK        → S13 · S14 · S16 · S17 · S19 · S20 · S23  (7 sahne)
② TOZ CÜMLESİ      → S13 seviye 3 · diğer 6 sahne seviye 4
④ TEK KOL SÜRÜMÜ   → S15 (yalnız eldivenler ve levha kadrajda)
⑤ HOPPER TAM BLOK  → S13 · S14 · S19 · S21 · S22
⑦ THIRD DUNE       → S13 · S14 · S18 · S21 · S22 · S24
⑨ STORM FRONT      → S16 · S18 · S20 · S21 · S22 · S23 · S24
⑩ GÖMÜLME EKİ      → S13 · S14 · S19'a kadar; S21'de KALKAR
   ⚠️ S19'un sonunda gövde düzelir. S20'den itibaren "tilted 9 degrees"
      cümlesi HİÇBİR promptta geçmez — eğim kapatılmıştır.
```

## ⚓ PART B'DE AÇILAN YENİ ÇAPA BLOKLARI

### ⑬ CABIN — kokpit (S16 · S20 · S23)

```
the cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays, no glowing graphics and no screens of any kind, and at
its centre a 14-centimetre mechanical bubble level with one bubble
inside an engraved centre ring
```

### ⑭ CARGO RACK — 12 yuvalı raf (S13 · S17)

```
the cargo rack — twelve identical slots in three rows of four, each
sized for one 60 by 40 by 30 centimetre grey composite case with
recessed handles and machined corner blocks; every empty slot stays
visibly open
```

### ⑮ PORT FORWARD LEG — iskele ön bacağı (S19 · S21)

```
the port forward leg — a telescoping strut ending in a 1.2-metre round
sand pad, with a manual pump handle folded out at its knuckle and a
9-centimetre bubble level set into the strut face
```

> ⚠️ **PART A'nın SHIP BIBLE'ına ek:** "Her bacakta elle çalıştırılan
> POMPA KOLU" satırı **"+ strut yüzünde 9 cm kabarcık göstergesi"** ile
> genişletildi. Gerekçe: gövdeyi seviyeye getiren kişi göstergeyi
> GÖRMEK zorundadır; kabin göstergesi kokpitte, o ise dışarıdadır.
> İki gösterge iki AYRI nesnedir, ikisi de sabit konumludur — kimlik
> karışması yok [Ders 58]. Kabin göstergesi 14 cm (uçuş aleti), bacak
> göstergesi 9 cm (yer bakım aleti).

### ⑦b THIRD DUNE — KISMİ SÜRÜM (S14 · S21 · S22; yalnız kayma yüzü kadrajda)

> Tam blok tepenin sırtını ve rüzgâr üstü yamacını da tarif eder; bu üç
> sahnede ikisi de kadraj DIŞINDA. Kısmi sürüm tam bloğun ALT KÜMESİDİR
> ve çelişen tek kelime içermez — "arka plan sürümü" mantığının aynısı.

```
the steep 33-degree slip face of the third dune
```

### ⑯ SCOOP PLATE — kazı levhası (S14 · S15)

```
a 90-centimetre curved bone-white composite scoop plate with two grip
cutouts
```

### ⑰ BLAST BOWL — kalkış çanağı (S22 · S24)

```
the blast bowl — a 14-metre-wide shallow circular depression scoured
into the sand, its rim slumping inward
```

### ⑱ ABANDONED CASES — bırakılan kasalar (S18 · S22 · S24)

```
eleven identical 60 by 40 by 30 centimetre grey composite cases with
recessed handles and machined corner blocks, standing upright on the
sand in a single straight line
```

---

## 🔢 PART B'NİN SAYAÇ TAKVİMİ — üçü de bu bölümde okunur

```
① TOZ SEVİYESİ   S13 seviye 3 → S14'ten itibaren seviye 4. Geri gitmez.
② KABARCIK       S16 halkanın DIŞINDA (9°) → S19'da halkanın İÇİNE
                 girer (0°) → S20 içeride sabit.
                 ⭐ Tek karede iki uç: kazınmış halka (hedef) ↔
                   kabarcığın yeri (gerçek) [D78 ①]
③ 12 YUVALI RAF  S13'te 12 yuvanın 12'si DOLU → S17'de 11 kasa çıkar,
                 1 kalır, 11 YUVA BOŞ VE GÖRÜNÜR → S23'te tek kasa
                 jeoloğun dizinde.
                 ⭐ Boş yuvanın kendisi göstergedir — sönmüş segmentin
                   yuvasının katı nesne hâli.

⛔ Bu üç kanalın hiçbiri metin, rakam, ekran ya da ışıklı grafik
   İÇERMEZ. Filmde tek bir okunabilir karakter yoktur.
```

## 🧍 PART B İNSAN SAYIMI (HUMAN COUNT LOCK)

```
2 insan → S13 · S14 · S16 · S17 · S19 · S20 · S23      (7 sahne)
1 insan → S15  (yalnız eldivenler, ön kollar ve levha kadrajda)
0 insan → S18 · S21 · S22 · S24                        (4 sahne)

FİLM TOPLAMI: 2 insan × 19 sahne · 1 insan × 2 sahne (S10, S15) ·
              0 insan × 4 sahne = 25 ✅
KASK: 8/8 insanlı sahnede KAPALI. Kasksız sahne SIFIR.
```

---

# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART B: S13-S24)

> ⚡ **Her prompt tamamen bağımsızdır.** Bible'lara bakmanıza gerek yok.
> ⛔ Kod bloğunun İÇİNİ kopyalayın; Türkçe başlık eklemeyin, iki promptu
> birleştirmeyin.

---

## 🎬 SAHNE 13 (S13) — ENVANTER

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Medium-wide
surface view beside a grounded vehicle, desert planet. Exactly 2 human
figures in frame.

SCENE: Two astronauts stand under the raised port side of a tilted
vehicle, both looking up at a landing leg that is not touching the
ground. Filling the frame width: the hopper — an 11-metre low
hexagonal-section surface lander, 6 metres wide and 3.2 metres tall, no
rocket silhouette: a broad flat hull with crisp recessed panel seams, a
short forward canopy blended into the deck, four corner LIFT NOZZLE pods
that pivot from straight-down to rearward, four telescoping landing legs
ending in 1.2-metre round sand pads, and a wide side cargo hatch; matte
bone-white ceramic panels over an anthracite structural frame, one thin
anthracite stripe running the length of each flank. Its starboard flank
is buried in the dune's slip face up to the hull midline; the starboard
legs and pads are completely under the sand; the hull is tilted 9
degrees to starboard and the port forward leg hangs 40 centimetres clear
of the surface. The side cargo hatch is already open, showing the edge
of the cargo rack — twelve identical slots in three rows of four, each
holding one 60 by 40 by 30 centimetre grey composite case; every slot is
full.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar, both faces fully
readable. The taller lean one is the geologist — woman, early forties,
1.78 m, deep copper-brown skin with visible pores, broad cheekbones,
black eyes, a nose bridge crooked from an old break, very short black
hair greying, inlaid ICE-BLUE bands on shoulders and forearms. The
shorter stocky one is the engineer — man, mid-thirties, 1.66 m,
thick-shouldered, pale heavily freckled skin with visible pores,
grey-green eyes, a short red-brown beard, cropped red hair, a
2-centimetre white scar on his left cheekbone, inlaid DEEP-VIOLET bands
on shoulders and forearms. Dust state: plate grooves packed with orange
sand, knees coated, helmet shells lightly dusted; the 3-cm sealed strip
under each left shoulder plate stays clean bone white and both visors
stay spotless.

ENVIRONMENT: Pale yellow-beige sky. Light directionless, shadows gone,
the world one warm orange-grey value. A thin flowing layer of sand runs
across the ground below knee height.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 25 metres from the
vehicle at 1.6 metres height. Flat diffuse light; the bone-white hull is
the only bright value in the frame.

SPATIAL LOCK: The vehicle fills the frame with its buried starboard side
toward the right and the raised port side toward the camera. Both
figures stand left of centre under the hanging leg, angled camera-right.
Grains drift screen-left to screen-right along the hull.

PHYSICS: Gravity 1.1g. The hull rests on three pads only; the fourth
hangs free and carries no load. Wind-driven grains keep depositing
against the buried flank and settle within 3 seconds.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— no duplicates, no background figures, no one inside the hatch. Nobody
enters, climbs or boards, and the hatch does not move. The vehicle is
intact and whole, only buried and tilted — no wreckage, damage, debris,
scorching, fire or smoke. Exactly four legs, four nozzle pods and twelve
cargo slots — no extras. Neither suit has a back-mounted unit — no
backpack, tank, hose, cable or rear housing; both back silhouettes are
flat. Each visor is optically clear — zero tint, zero mirror coating,
zero reflection, no sand on the glass. 0% bloom, no soft focus; skin
keeps pores, no face morphing. No readable text, digits or hull
markings; no lit displays; no subtitles, no watermark. Sand is granular
under 1.1g — never swirling or flowing like water. No heat-haze shimmer;
terrain static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 25 metres from the vehicle at 1.6 metres height, 35mm
spherical lens, no camera movement. Exactly 2 human figures.

SCENE: Filling the frame width, the hopper — an 11-metre low
hexagonal-section surface lander, 6 metres wide and 3.2 metres tall, no
rocket silhouette: a broad flat hull with crisp recessed panel seams, a
short forward canopy blended into the deck, four corner LIFT NOZZLE pods
that pivot from straight-down to rearward, four telescoping landing legs
ending in 1.2-metre round sand pads, and a wide side cargo hatch; matte
bone-white ceramic panels over an anthracite structural frame, one thin
anthracite stripe running the length of each flank. Its starboard flank
is buried in the dune's slip face up to the hull midline; the starboard
legs and pads are completely under the sand; the hull is tilted 9
degrees to starboard and the port forward leg hangs 40 centimetres clear
of the surface. The side cargo hatch is already open, showing twelve
full cargo slots in three rows of four. Pale yellow-beige sky, light
directionless, shadows gone.

CHARACTERS: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar, both faces fully
readable. The taller lean one is the geologist — woman, early forties,
1.78 m, deep copper-brown skin with visible pores, broad cheekbones,
black eyes, a nose bridge crooked from an old break, very short black
hair greying, inlaid ICE-BLUE bands on shoulders and forearms. The
shorter stocky one is the engineer — man, mid-thirties, 1.66 m,
thick-shouldered, pale heavily freckled skin with visible pores,
grey-green eyes, a short red-brown beard, cropped red hair, a
2-centimetre white scar on his left cheekbone, inlaid DEEP-VIOLET bands
on shoulders and forearms. Dust state: plate grooves packed with orange
sand, knees coated, helmet shells lightly dusted; the 3-cm sealed strip
under each left shoulder plate stays clean bone white and both visors
stay spotless.

TIMELINE: 0.0s — Both are already standing under the hanging leg, helmets tipped up at it. 3.0s — The engineer reaches up and pushes the 1.2-metre sand pad with one flat glove. It swings 5 centimetres and stops — the leg carries no load. 6.0s — The geologist turns her helmet along the hull line toward the buried starboard flank and holds there. 9.0s — Neither moves. Grains keep arriving along the buried side and settle within 3 seconds. No cuts.

AUDIO: Directionless wind hiss, heavy and close. A dull hollow knock as
a glove meets the pad, then the creak of an unloaded strut swinging.
Ticks of grains on the hull and helmet shells. Faint suit-fan hum. Two
sets of breathing on an open radio channel, no words. No music.

PHYSICS: Gravity 1.1g. The hull rests on three pads only; the fourth is
free and unloaded, so a light push moves it and it stops without
rebound. The vehicle does not settle during the shot. Real time,
ordinary Earth pace — no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — no duplicates, no background figures, no one inside the
hatch. Nobody enters, climbs or boards, and the hatch does not move. The
vehicle is intact and whole, only buried and tilted — no wreckage,
damage, debris, scorching, fire or smoke. Exactly four legs, four nozzle
pods and twelve cargo slots — no extras. Neither suit has a back-mounted
unit — no backpack, tank, hose, cable or rear housing; both back
silhouettes are flat. Each visor is optically clear — zero tint, zero
mirror coating, zero reflection, no sand on the glass. 0% bloom, no soft
focus; skin keeps pores, no face morphing. No readable text, digits or
hull markings; no lit displays; no subtitles, no watermark. Glove-pad
contact keeps a clear boundary — no merging, no extra fingers. Sand is
granular under 1.1g — never swirling or flowing like water. No heat-haze
shimmer; terrain static. Real time, no slow motion. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 14 (S14) — KAZI

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close working
view at the foot of a buried vehicle, desert planet. Exactly 2 human
figures in frame.

SCENE: Two astronauts dig into the bank of sand covering a landing leg.
The engineer drives a 90-centimetre curved bone-white composite scoop
plate with two grip cutouts into the slope with both hands; the
geologist kneels beside the opening hauling the loosened sand back with
her forearms. A pit about 1.2 metres across has been opened against the
hull and the curved rim of a 1.2-metre round sand pad has just come into
view at its bottom. Behind them the bone-white flank of the hopper rises
out of the sand, its panel seams and one thin anthracite stripe visible
above the bank.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar, both faces fully
readable. The taller lean one is the geologist — woman, early forties,
1.78 m, deep copper-brown skin with visible pores, broad cheekbones,
black eyes, a nose bridge crooked from an old break, very short black
hair greying, inlaid ICE-BLUE bands on shoulders and forearms. The
shorter stocky one is the engineer — man, mid-thirties, 1.66 m,
thick-shouldered, pale heavily freckled skin with visible pores,
grey-green eyes, a short red-brown beard, cropped red hair, a
2-centimetre white scar on his left cheekbone, inlaid DEEP-VIOLET bands
on shoulders and forearms. Dust state: every forward surface orange with
packed sand, plate grooves overflowing, a crust of sand on both gloves,
helmet shells and shoulder tops dusted; the 3-cm sealed strip under each
left shoulder plate stays clean bone white and both visors stay
spotless.

ENVIRONMENT: Pale yellow-beige sky. Light directionless, shadows gone,
the world one warm orange-grey value. Above and behind, the steep
33-degree slip face of loose uncompacted sand rises out of frame.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 4 metres from the pit
at 1.1 metres height. Flat diffuse light; the only bright values are the
bone-white hull, the scoop plate and the exposed pad rim.

SPATIAL LOCK: The hull and the slip face occupy the right two thirds of
the frame; the pit and both figures sit left of centre, angled
camera-right. Grains drift screen-left to screen-right over the rim of
the pit.

PHYSICS: Gravity 1.1g. Every scoop lifts a discrete mass of dry grains
that separates in the air and lands as a spreading fan, coming to rest
within 3 seconds. The pit walls stand at the 33-degree angle of repose.
Glove-to-plate and plate-to-sand contacts keep clear structural
boundaries.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— no duplicates, no background figures. The vehicle is intact and whole,
only buried — no wreckage, damage, debris, scorching, fire or smoke.
Exactly one scoop plate and one exposed sand pad in frame. Neither suit
has a back-mounted unit — no backpack, tank, hose, cable or rear
housing; both back silhouettes are flat. Each visor is optically clear —
zero tint, zero mirror coating, zero reflection, no sand on the glass.
0% bloom, no soft focus; skin keeps pores, no face morphing. No readable
text, digits or hull markings; no subtitles, no watermark. Hand-tool and
tool-sand contacts keep clear structural boundaries — no merging, no
extra fingers. Sand is discrete granular matter under 1.1g — thrown
grains separate in flight and land as spreading fans; never swirling,
never flowing like water, never splashing. No heat-haze shimmer; terrain
static apart from the digging. No CGI aesthetic. Photorealistic with
35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 4 metres from the pit at 1.1 metres height, 35mm
spherical lens, no camera movement. Exactly 2 human figures.

SCENE: A pit about 1.2 metres across dug into a bank of sand against the
bone-white flank of a vehicle; panel seams and one thin anthracite
stripe are visible above the bank, and the steep 33-degree slip face of
loose uncompacted sand rises out of frame behind. Pale yellow-beige sky,
light directionless, shadows gone.

CHARACTERS: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar, both faces fully
readable. The taller lean one is the geologist — woman, early forties,
1.78 m, deep copper-brown skin with visible pores, broad cheekbones,
black eyes, a nose bridge crooked from an old break, very short black
hair greying, inlaid ICE-BLUE bands on shoulders and forearms. The
shorter stocky one is the engineer — man, mid-thirties, 1.66 m,
thick-shouldered, pale heavily freckled skin with visible pores,
grey-green eyes, a short red-brown beard, cropped red hair, a
2-centimetre white scar on his left cheekbone, inlaid DEEP-VIOLET bands
on shoulders and forearms. Dust state: every forward surface orange with
packed sand, plate grooves overflowing, a crust of sand on both gloves,
helmet shells and shoulder tops dusted; the 3-cm sealed strip under each
left shoulder plate stays clean bone white and both visors stay
spotless.

TIMELINE:
0.0s — The engineer is already mid-stroke, driving a 90-centimetre
curved bone-white composite scoop plate with two grip cutouts into the
sand bank with both hands and levering a load out.
2.5s — He swings the load clear and throws it screen-left. The grains
separate in the air and land as a spreading fan, coming to rest within 3
seconds.
5.0s — The geologist, kneeling, hauls the loose spoil back from the rim
with both forearms, clearing the working face. Real progress: the pit is
visibly deeper than at zero.
8.0s — At the bottom of the pit the curved rim of a 1.2-metre round sand
pad comes clear of the sand for the first time. Both stop for a beat and
look at it. No cuts.

AUDIO: Directionless wind hiss. The hard grinding bite of a composite
plate driven into dry sand, then the dry rush of a thrown load landing.
Heavy breathing on an open radio channel, effort with no words. Ticks of
grains on both helmet shells. Faint suit-fan hum. No music.

PHYSICS: Gravity 1.1g — the thrown load falls faster than it would on
Earth and lands hard, spreading rather than splashing. Every scoop is a
discrete mass of dry grains that separates in flight. Pit walls stand at
the 33-degree angle of repose. Real time, ordinary Earth pace, no slow
motion — this must not read as a slow-motion digging shot.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — no duplicates, no background figures. The vehicle is
intact and whole, only buried — no wreckage, damage, debris, scorching,
fire or smoke. Exactly one scoop plate in frame. Neither suit has a
back-mounted unit — no backpack, tank, hose, cable or rear housing; both
back silhouettes are flat. Each visor is optically clear — zero tint,
zero mirror coating, zero reflection, no sand on the glass. 0% bloom, no
soft focus; skin keeps pores, no face morphing. No readable text, digits
or hull markings; no subtitles, no watermark. Hand-tool and tool-sand
contacts keep clear structural boundaries — no merging, no extra
fingers. Sand is discrete granular matter under 1.1g — thrown grains
separate in flight and land as spreading fans; never swirling, never
billowing, never flowing or splashing like water. No heat-haze shimmer;
terrain static apart from the digging. Real time, no slow motion. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 15 (S15) — ⭐ AKIŞKAN KUM · **1 NUMARALI ÜRETİM KAPISI**

> ⛔ **BU SAHNE GEÇİLMEDEN DİĞER 24 SAHNE ÜRETİLMEZ.** Sınav tek bir
> şey: kum **granüler** çökecek — blok kayar, taneye dağılır, yayılır,
> DURUR. Sıvı gibi akarsa, girdap yaparsa, dalga olursa ya da havada
> donarsa [Ders 39] konsept revize edilir. Kapının sonucu PLAN
> dosyasına yazılır [D74: kaydı olmayan kapı, koşulmamış kapıdır].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Extreme close
detail of collapsing sand, desert planet. Exactly 1 human figure in
frame — only two gloved hands, both forearms and the scoop plate they
hold are within the frame.

SCENE: The upper wall of a freshly dug pit is failing. A block of dry
ocher sand about 40 centimetres across has sheared away from the rim
along a clean straight break line and is breaking apart into individual
grains as it travels down the pit wall. Below it, the curved rim of a
1.2-metre round bone-white sand pad is already half covered again by the
arriving material. The failure is granular and blocky, not fluid: a
sheared slab, a spreading front of separate grains, a stopping fan — no
wave, no current, no splash.

SUBJECT: Two gloved hands and both forearms of the engineer — matte
bone-and-sand ceramic hard shell with ribbed forearm plates over dark
anthracite pressure weave, machined scraper cuffs at the wrists, inlaid
DEEP-VIOLET accent bands along the forearms, the plate grooves
overflowing with orange sand and a crust of sand on both gloves. They
grip a 90-centimetre curved bone-white composite scoop plate with two
grip cutouts, held still and slightly lifted, no longer working. Nothing
else of him is in frame.

ENVIRONMENT: Pale yellow-beige light with no visible sun. Shadows gone;
the light is completely directionless and the pit wall is modelled only
by the texture of the sand itself.

CAMERA & LIGHT: 85mm spherical lens, fixed camera 2 metres from the pit
wall at 0.6 metres height, shallow depth of field so the far rim falls
soft. Every grain in the failing block is individually resolved.

SPATIAL LOCK: The pit wall and the failing block fill the left two
thirds of the frame; the sand pad and the gloved hands sit lower right.
The material travels screen-left to screen-right down the wall.

PHYSICS: Gravity 1.1g. Dry sand holds at a 33-degree angle of repose;
past that the slope fails. Failure is granular: a slab shears along a
break line, disintegrates into discrete grains, spreads into a fan and
comes to rest. The whole event takes 3 seconds and then the surface is
completely still again.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 1 human figure
— no second person, no other hands, no figure in the background. The
sand is discrete granular matter under 1.1g: a sheared slab breaking
into separate grains. It is NOT a fluid — no wave, no crest, no current,
no eddy, no vortex, no splash, no spray, no droplets, no foam, no
ripples travelling through it, and it never flows, pours or streams like
water, oil, smoke or fabric. Nothing hovers, nothing hangs, nothing
freezes in mid-air. The sand pad is intact and whole — no damage, no
debris. The suit has no back-mounted unit and nothing hangs from the
forearms — no hose, no cable, no tether. 0% bloom, no soft focus — every
grain keeps edge and texture. No readable text, digits or markings; no
subtitles, no watermark. Hand-tool contact keeps a clear structural
boundary — no merging, no extra fingers. No heat-haze shimmer; the
surrounding terrain is static apart from the described failure. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 2 metres from the pit wall at 0.6 metres height, 85mm
spherical lens, shallow depth of field, no camera movement. Exactly 1
human figure in frame — only two gloved hands, both forearms and the
scoop plate they hold are within the frame.

SCENE: The upper wall of a freshly dug pit in dry ocher sand, and at the
bottom of it the curved rim of a 1.2-metre round bone-white sand pad,
newly uncovered and still clear. Pale yellow-beige light, no visible
sun, shadows gone, the wall modelled only by the texture of the sand.
Two gloved hands and both forearms of the engineer are in the lower
right — matte bone-and-sand ceramic hard shell with ribbed forearm
plates over dark anthracite pressure weave, machined scraper cuffs at
the wrists, inlaid DEEP-VIOLET accent bands along the forearms, the
plate grooves overflowing with orange sand and a crust of sand on both
gloves — gripping a 90-centimetre curved bone-white composite scoop
plate with two grip cutouts.

TIMELINE:
0.0s — The pad rim is clear and the wall is still. The gloved hands lift
the scoop plate back for another stroke.
2.0s — A clean straight break line opens along the top of the pit wall.
A slab of sand about 40 centimetres across shears away along it as a
single block.
3.5s — The slab disintegrates into individual grains as it travels down
the wall, spreads into a widening fan and pours over the pad rim.
5.5s — The movement stops. Within three seconds of the break the surface
is completely still again, and the pad rim that was clear at zero is
half covered. Nothing is flowing anywhere in frame.
8.0s — The gloved hands stop. The scoop plate is lowered until its edge
rests on the sand, and it does not move again. No cuts.

AUDIO: Directionless wind hiss. A short dry granular slump — a dense
crackling collapse, three seconds long, ending flat with no tail. Not a
splash, not a rush of water, not a rockfall. Then only wind and one long
breath on an open radio channel. No words, no music.

PHYSICS: Gravity 1.1g. Dry sand holds at a 33-degree angle of repose;
past that the slope fails. The failure is granular in three stages: a
slab shears along a break line, disintegrates into discrete grains,
spreads into a fan and comes to rest. Total duration 3 seconds, then
complete stillness. Real time, ordinary Earth pace — this must not read
as a slow-motion shot.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 1
human figure — no second person, no other hands, no figure entering
frame. The sand is discrete granular matter under 1.1g: a sheared slab
breaking into separate grains. It is NOT a fluid — no wave, no crest, no
current, no eddy, no vortex, no whirlpool, no splash, no spray, no
droplets, no foam, no surface ripples travelling through it, and it
never flows, pours or streams like water, oil, lava, smoke or fabric.
Nothing hovers, hangs or freezes in mid-air, and nothing keeps moving
after the 3 seconds. The sand pad is intact and whole. The suit has no
back-mounted unit and nothing hangs from the forearms — no hose, no
cable, no tether. 0% bloom, no soft focus — every grain keeps edge and
texture. No readable text, digits or markings; no subtitles, no
watermark. Hand-tool contact keeps a clear structural boundary — no
merging, no extra fingers. No heat-haze shimmer; the surrounding terrain
is static apart from the described failure. Real time, no slow motion,
no speed ramp. No CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 16 (S16) — TARTI

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Cockpit
interior seen from directly behind two seated figures. Exactly 2 human
figures in frame, both from behind.

SCENE: The cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays and no screens, and at its centre a 14-centimetre
mechanical bubble level with one bubble inside an engraved centre ring.
The bubble is not in the ring: it has run to the edge of its glass and
sits jammed against the rim, well outside the engraving. Through the
window: a wall of ocher sand rising steeply on the right, and along the
left edge a 2-kilometre-high wall of suspended ocher dust spanning the
full width of the horizon, its base dark and its crest lit.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. Seen from behind,
their faces are not in frame. The taller lean one on the right is the
geologist — woman, early forties, 1.78 m, inlaid ICE-BLUE bands on
shoulders and forearms. The shorter stocky one on the left is the
engineer — man, mid-thirties, 1.66 m, thick-shouldered, inlaid
DEEP-VIOLET bands on shoulders and forearms. Dust state: every forward
surface orange with packed sand, plate grooves overflowing, a crust of
sand on both gloves, helmet shells and shoulder tops dusted; the 3-cm
sealed strip under each left shoulder plate stays clean bone white.

ENVIRONMENT: The cabin is dim. The only light source is the orange
daylight coming through the forward window; it falls on both helmet
backs and on the mechanical panel. Nothing in the cabin emits light.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 1.2 metres behind the
seats at 1.3 metres height, centred between the two headrests so the
window and the bubble level are both fully visible between them.

SPATIAL LOCK: The sand wall fills the right side of the window and the
dust wall the left, matching every exterior shot. The engineer sits
screen-left, the geologist screen-right.

PHYSICS: Gravity 1.1g. The whole cabin is tilted 9 degrees to starboard
with the vehicle; both seated bodies and the bubble sit consistently
with that tilt. The horizon seen through the window is tilted by the
same amount.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— no duplicates, no third seat, no one else in the cabin, no reflected
face. Both are seen from behind; no mouth or face is visible. No
readable text, letters, digits or symbols anywhere; the panel is purely
mechanical — no lit displays, no screens, no HUD, no illuminated
indicators. No subtitles, no watermark. Neither suit has a back-mounted
unit — no backpack, tank, hose, cable or rear housing; both back
silhouettes are flat. Each visor is optically clear — zero tint, zero
mirror coating, zero reflection, and the window glass carries no
reflection. 0% bloom, no soft focus — every surface keeps texture. No
heat-haze shimmer through the window; terrain static. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 1.2 metres behind the seats at 1.3 metres height, 35mm
spherical lens, no camera movement. Exactly 2 human figures, both seen
from behind.

SCENE: The cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays and no screens, and at its centre a 14-centimetre
mechanical bubble level with one bubble inside an engraved centre ring.
The bubble sits jammed against the rim of its glass, well outside the
engraving. Through the window: a wall of ocher sand rising steeply on
the right, and along the left edge a 2-kilometre-high wall of suspended
ocher dust spanning the full width of the horizon, its base dark and its
crest lit. The cabin is dim; the only light is orange daylight through
the window and nothing inside emits light.

CHARACTERS: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. Seen from behind,
neither face is in frame. The taller lean one on the right is the
geologist — woman, early forties, 1.78 m, inlaid ICE-BLUE bands on
shoulders and forearms. The shorter stocky one on the left is the
engineer — man, mid-thirties, 1.66 m, thick-shouldered, inlaid
DEEP-VIOLET bands on shoulders and forearms. Dust state: every forward
surface orange with packed sand, a crust of sand on both gloves, helmet
shells and shoulder tops dusted; the 3-cm sealed strip under each left
shoulder plate stays clean bone white.

TIMELINE:
0.0s — Both sit still in the tilted cabin, helmets level, facing the
window. The bubble sits hard against the rim and does not move.
2.5s — The engineer's gloved hand comes up and taps one physical toggle
twice, then returns to his knee. Nothing lights up; the panel is
mechanical.
5.5s — Neither of them moves for a long beat. Outside the window the
dust wall on the left has visibly thickened against the sky.
8.5s — The geologist's helmet turns two degrees toward the bubble level
and stays there. No cuts.

AUDIO: A muffled version of the outside world, the wind reduced and its
high frequencies cut by the hull. A close, dry cabin tone and a faint
suit-fan hum. Two mechanical toggle clicks. Then, from the cabin
speaker, a calm neutral synthetic voice, off-screen and bodiless, says
in Turkish: "Dort lulede kaldirma marji negatif. Ikinci cephe yirmi
dakika." After a clear pause, a man's voice over the closed-helmet radio
channel, filtered to a narrow band, answers in Turkish: "Kutle mi, sure
mi? Ikisi birden yok." No music.

PHYSICS: Gravity 1.1g. The cabin is tilted 9 degrees to starboard with
the vehicle; both seated bodies, the bubble and the horizon through the
window all sit consistently with that tilt. Nothing shifts or settles
during the shot. Real time, ordinary Earth pace — no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — no duplicates, no third seat, no one else in the cabin,
no reflected face. Both are seen from behind throughout; no mouth or
face is ever visible. The two spoken lines are heard only — never shown
as text, no subtitles, no captions, no transcript — and they never
overlap: one speaker at a time with a clear pause between them. The
synthetic voice is off-screen only — no body, face, avatar or third
figure. No readable text, letters, digits or symbols anywhere; the panel
is purely mechanical — no lit displays, no screens, no HUD, no
illuminated indicators. Neither suit has a back-mounted unit — no
backpack, tank, hose, cable or rear housing; both back silhouettes are
flat. Each visor is optically clear — zero tint, zero mirror coating,
zero reflection — and the window glass carries no reflection. 0% bloom,
no soft focus. No heat-haze shimmer; terrain static. Real time, no slow
motion. No CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 17 (S17) — ⭐ CENTRAL CHOICE: RAF · **3 NUMARALI ÜRETİM KAPISI**

> ⚠️ **A4 KARARI [D69]:** dar hacimde iki insan, deponun en pahalı klon
> tipi. AZALTIM: jeolog TAM BOY, mühendis yalnız OMUZ + ÖN KOL olarak
> kadrajın sağ kenarında, gövdesi kadraj DIŞINDA. Kadrajda tam boy TEK
> gövde vardır. Klon çıkarsa mühendis sahneden tamamen çıkarılır ve
> repliği telsizden gelir — maliyet 0 saniye, sahne silinmez.
> ⛔ **SEÇİM EKRANDA TAMAMLANMAK ZORUNDA** [D72 kurgu kapısı]: son kasa
> 8,5. saniyede kadrajı terk eder ve 11 boş yuva görünür kalır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
cargo bay beside an open hatch, desert planet. Exactly 2 human figures
in frame — one full length, and at the right edge only the other's
shoulder and forearm, his body outside the frame.

SCENE: A woman stands full length in front of a loading rack, one grey
case held in both gloved hands, half lifted out of its slot. The rack
behind her: twelve identical slots in three rows of four, each sized for
one 60 by 40 by 30 centimetre grey composite case with recessed handles
and machined corners. Seven slots are already empty and stay visibly
open; five still hold cases. To her left the wide side hatch stands open
onto flat ocher sand, and three grey cases already stand upright on the
sand outside it. At the right edge of frame, only a shoulder plate and a
forearm belong to a second person; his body is outside the frame.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. The full-length one
is the geologist — woman, early forties, 1.78 m, lean, deep copper-brown
skin with visible pores, broad cheekbones, black eyes, a nose bridge
crooked from an old break, very short black hair greying, inlaid
ICE-BLUE bands on shoulders and forearms; her face is readable through
the visor and she is turned toward the rack, not toward camera. The
shoulder and forearm at the right edge carry inlaid DEEP-VIOLET bands.
Dust state: every forward surface orange with packed sand, plate grooves
overflowing, a crust of sand on both gloves, helmet shells and shoulder
tops dusted; the 3-cm sealed strip under each left shoulder plate stays
clean bone white and her visor stays spotless.

ENVIRONMENT: The bay is dim and lit only by the orange daylight flooding
in through the open hatch. Nothing inside emits light. Fine sand has
drifted across the bay floor by the hatch sill.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 3 metres from the rack
at 1.5 metres height. Hard-edged daylight from the hatch on the left,
deep shadow at the back of the bay.

SPATIAL LOCK: The open hatch and the sand outside occupy the left third
of the frame; the rack fills the centre and right. The geologist stands
between them, facing screen-right toward the rack. Cases travel
screen-right to screen-left, from the rack out through the hatch.

PHYSICS: Gravity 1.1g. A 28-kilogram case is genuinely heavy: her stance
widens and her forearms load visibly when she takes its weight.
Glove-case contact keeps a clear structural boundary.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— one full length and one partial shoulder and forearm at the frame
edge; no third figure, no duplicate, no clone, no second full body, no
reflected face, and no one standing outside the hatch. Nobody enters,
climbs or boards, and the hatch does not move — it is already open. The
rack has exactly twelve slots in three rows of four; empty slots stay
visibly open. 0% bloom, no soft focus. Neither suit has a back-mounted
unit — no backpack, tank, hose, cable or rear housing; both back
silhouettes are flat. Her visor is optically clear — zero tint, zero
mirror coating, zero reflection, no sand on the glass. No readable text,
letters, digits or labels anywhere on the cases, the rack or the hull;
no lit displays; no subtitles, no watermark. Hand-case contact keeps a
clear boundary — no merging, no extra fingers. Sand is granular under
1.1g — never swirling or flowing like water. No heat-haze shimmer; the
bay is static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 3 metres from the rack at 1.5 metres height, 35mm
spherical lens, no camera movement. Exactly 2 human figures — one full
length, and at the right edge only the other's shoulder and forearm, his
body outside the frame.

SCENE: A dim cargo bay lit only by orange daylight through a wide open
side hatch on the left. Filling the centre and right, a loading rack:
twelve identical slots in three rows of four, each sized for one 60 by
40 by 30 centimetre grey composite case with recessed handles and
machined corners. Seven slots are already empty and stay visibly open;
five still hold cases. Outside the hatch, on flat ocher sand, three grey
cases already stand upright. At the right edge of frame a shoulder plate
and forearm with inlaid DEEP-VIOLET bands belong to a second person
whose body is outside the frame.

CHARACTERS: The geologist — woman, early forties, 1.78 m, lean, deep
copper-brown skin with visible pores, broad cheekbones, black eyes, a
nose bridge crooked from an old break, very short black hair greying;
matte bone-and-sand ceramic hard-shell suit, ribbed sand-shedding chest
and thigh plates over dark anthracite pressure weave, a machined collar
ring, scraper cuffs, finely scuffed, inlaid ICE-BLUE bands on shoulders
and forearms; low-profile helmet CLOSED with one seamless wraparound
visor of optically clear glass and a short rigid dust collar, her face
readable through it, turned toward the rack and never toward camera.
Dust state: every forward surface orange with packed sand, plate grooves
overflowing, a crust of sand on both gloves, helmet shell and shoulder
tops dusted; the 3-cm sealed strip under her left shoulder plate stays
clean bone white and her visor stays spotless.

TIMELINE: 0.0s — She is already lifting a case clear of its slot with both gloved hands, stance wide, forearms loaded with its weight. 2.5s — She carries it two steps screen-left and pushes it out through the hatch. It drops onto the sand and stands upright with the others. One more slot is empty. 5.0s — Without pausing she takes the next case and repeats the move. Her helmet never turns back toward the rack she is emptying. 8.5s — The last case leaves her hands and goes out through the hatch. In the rack behind her exactly one case remains, and eleven empty slots stand open around it. She stops with both hands still raised. 10.0s — She has not moved. No cuts.

AUDIO: A muffled version of the outside wind, its high frequencies cut
by the hull. The hard scrape of a case dragged from a metal slot, then
the flat thud of it landing on sand — repeated, evenly, without hurry.
Heavy breathing on an open radio channel. Then, over the closed-helmet
radio channel, a woman's voice filtered to a narrow band says in
Turkish: "Kirk gun burada kaliyor. Biz kalmiyoruz." No music.

PHYSICS: Gravity 1.1g — each 28-kilogram case is genuinely heavy: her
stance widens, her forearms load, and the case falls fast and lands hard
without bouncing. Glove-case contact keeps a clear structural boundary.
Real time, ordinary Earth pace — no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — one full length and one partial shoulder and forearm at
the frame edge; no third figure, no duplicate, no clone, no second full
body at any point, no reflected face, no one outside the hatch. Nobody
enters, climbs or boards, and the hatch does not move. The rack has
exactly twelve slots and exactly one case remains at the end; empty
slots stay visibly open. The spoken line is heard only — never shown as
text, no subtitles, no captions; one speaker only and no mouth is
readable in frame. 0% bloom, no soft focus. Neither suit has a
back-mounted unit — no backpack, tank, hose, cable or rear housing; both
back silhouettes are flat. Her visor is optically clear — zero tint,
zero mirror coating, zero reflection, no sand on the glass. No readable
text, letters, digits or labels on the cases, rack or hull; no lit
displays; no watermark. Cases stay whole — nothing opens, breaks or
spills. Sand is granular under 1.1g — never swirling or flowing like
water. Real time, no slow motion. No CGI aesthetic. Photorealistic with
35mm film grain.
```

---

## 🎬 SAHNE 18 (S18) — BIRAKILAN

> 🔇 **FİLMİN SESSİZLİK SAHNESİ.** Müzik S17'nin 7. saniyesinde biter;
> bu 10 saniye boyunca müzik YOKTUR. ⛔ Müziksiz ≠ sessiz: ortam yatağı
> burada filmin EN GÜÇLÜ seviyesindedir (-18 dBFS) [DERS 83].
> Ayrıntı: `THE_THIRD_DUNE_MUZIK.md` §A.2 · §B.1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Ground-level
view of abandoned equipment on open sand, desert planet. Exactly 0 human
figures in frame — no crew, no figure anywhere.

SCENE: Eleven identical 60 by 40 by 30 centimetre grey composite cases
with recessed handles and machined corners stand upright on the sand in
a single straight line, exactly where they were set down. They are the
only straight line in a landscape made entirely of curves. Against the
upwind side of each case a small wedge of ocher sand has already begun
to bank; the downwind side of each is scoured clean. Ten metres behind
the line, the bone-white flank of a vehicle rises out of a bank of sand,
its panel seams and one thin anthracite stripe readable. Along the left
horizon: a 2-kilometre-high wall of suspended ocher dust spanning the
full width of the horizon, its base dark and its crest lit.

ENVIRONMENT: Pale yellow-beige sky. Light completely directionless,
shadows gone, the world one warm orange-grey value. A thin flowing layer
of sand streams across the ground below knee height and breaks around
the base of every case.

CAMERA & LIGHT: 50mm spherical lens, fixed camera 6 metres from the
nearest case at 0.5 metres height, low enough that the line of cases
runs across the frame at eye level with the sand. Flat diffuse light;
the grey cases are the darkest values and the hull the brightest.

SPATIAL LOCK: The line of cases runs from the lower left of the frame
toward the middle right. The vehicle sits in the background right third.
The dust wall lies along the left horizon. Sand streams screen-left to
screen-right and banks on the left side of every case.

PHYSICS: Gravity 1.1g. Wind-driven grains strike each case, lose their
energy and deposit on its upwind side; the lee side stays scoured. All
moving grains settle within 3 seconds of the wind dropping.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 0 human figures
— no crew, no figure, no silhouette, no shadow anywhere in frame.
Exactly eleven cases, all identical, all upright, in one straight line —
no extras, no scattered cases, none tipped over, none open, none broken,
nothing spilled. The vehicle is intact and whole — no wreckage, damage,
debris, scorching, fire or smoke. No readable text, letters, digits or
labels anywhere on the cases or the hull; no subtitles, no watermark.
Sand is discrete granular matter under 1.1g — grains bank on the upwind
side and settle within 3 seconds; never swirling, curling or flowing
like water or smoke. Nothing is blown over and no case moves. No
heat-haze shimmer, no mirage; terrain static. No mirrored composition,
no direction reversal. No CGI aesthetic. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 6 metres from the nearest case at 0.5 metres height,
50mm spherical lens, no camera movement. Exactly 0 human figures — no
crew, no figure anywhere in frame.

SCENE: Eleven identical 60 by 40 by 30 centimetre grey composite cases
with recessed handles and machined corners stand upright on ocher sand
in a single straight line — the only straight line in a landscape made
of curves. Ten metres behind them the bone-white flank of a vehicle
rises out of a bank of sand, its panel seams and one thin anthracite
stripe readable. Along the left horizon a 2-kilometre-high wall of
suspended ocher dust spans the full width of the horizon, its base dark
and its crest lit. Pale yellow-beige sky, light directionless, shadows
gone. A thin flowing layer of sand streams across the ground below knee
height.

TIMELINE:
0.0s — Nothing is happening and nothing will. The eleven cases stand
where they were left. Sand streams past them screen-left to
screen-right, breaking around each one.
3.0s — On the upwind side of the nearest case the small wedge of banked
sand grows by a visible amount. Its downwind side stays scoured clean.
6.0s — The wedge on the second case reaches the top of its lowest corner
block. No case moves; the wind cannot shift 28 kilograms.
9.0s — Held. The line is still straight, the wall on the left is nearer,
and the sand keeps arriving. No cuts.

AUDIO: The wind is at its fullest here and it is the only thing in the
mix — a broad dry granular hiss with individual grain collisions inside
it, and a very low slow rumble beneath from the left. A fine irregular
patter of grains striking hard composite. No voices, no breathing, no
suit fan — there is no one here. No music of any kind in this shot.

PHYSICS: Gravity 1.1g. Wind-driven grains strike each case, lose their
energy and deposit on the upwind side; the lee side stays scoured. A
28-kilogram case cannot be moved by a 25 metre per second wind. All
airborne grains settle within 3 seconds. Real time, ordinary Earth pace
— no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 0
human figures — no crew, no figure, no silhouette, no shadow and no one
entering frame at any point. Exactly eleven cases, all identical, all
upright, in one straight line — no extras, none tipped over, none open,
none broken, nothing spilled, and none of them moves. The vehicle is
intact and whole — no wreckage, damage, debris, scorching, fire or
smoke. No readable text, letters, digits or labels anywhere; no
subtitles, no watermark. Sand is discrete granular matter under 1.1g —
grains bank on the upwind side and settle within 3 seconds; never
swirling, curling or flowing like water or smoke. Nothing is blown over.
No heat-haze shimmer, no mirage; terrain static. No direction reversal —
sand streams screen-right throughout. Real time, no slow motion. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 19 (S19) — SEVİYE

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close
mechanical detail at a landing leg, desert planet. Exactly 2 human
figures in frame — one crouched at the leg, and one gloved hand and
forearm of the other steadying the strut.

SCENE: A man crouches at the knuckle of a landing leg working a pump.
The port forward leg — a telescoping strut ending in a 1.2-metre round
sand pad, with a manual pump handle folded out at its knuckle and a
9-centimetre bubble level set into the strut face. The strut has
extended: its polished inner section now shows 40 centimetres of clean
bone-white metal where it was previously retracted, and the sand pad at
its foot is pressed down into the sand, taking load. In the bubble level
on the strut face the bubble sits exactly inside the engraved centre
ring. Entering from the right edge, one gloved hand and forearm of a
second person steadies the strut.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. The crouched one is
the engineer — man, mid-thirties, 1.66 m, stocky and thick-shouldered,
pale heavily freckled skin with visible pores, grey-green eyes, a short
red-brown beard, cropped red hair, a 2-centimetre white scar on his left
cheekbone, inlaid DEEP-VIOLET bands on shoulders and forearms; his face
is readable through the visor, angled down at the pump. The hand at the
right edge carries an inlaid ICE-BLUE band along its forearm. Dust
state: every forward surface orange with packed sand, plate grooves
overflowing, a crust of sand on both gloves, helmet shell and shoulder
tops dusted; the 3-cm sealed strip under his left shoulder plate stays
clean bone white and his visor stays spotless.

ENVIRONMENT: Pale yellow-beige light, no visible sun, shadows gone. The
bone-white hull rises behind the leg, and a thin flowing layer of sand
streams past the pad.

CAMERA & LIGHT: 85mm spherical lens, fixed camera 2.5 metres from the
leg at 0.8 metres height, so the pump handle, the strut and the bubble
level are all in the same frame. Shallow depth of field; the bubble and
its engraved ring are the sharpest things in the image.

SPATIAL LOCK: The leg and the strut run up the centre of the frame with
the hull behind on the right. The engineer crouches screen-left of the
leg; the second hand enters from the right edge. Sand streams
screen-left to screen-right past the pad.

PHYSICS: Gravity 1.1g. The extended strut now carries real load: the pad
has pressed a shallow ring into the sand around its rim. The bubble is a
mechanical liquid level and reads the hull's attitude directly.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— one crouched and one hand and forearm at the frame edge; no third
figure, no duplicate, no second full body, no reflected face. The
vehicle is intact and whole — no wreckage, damage, debris, scorching,
fire or smoke. Exactly one leg, one pad, one pump handle and one bubble
level in frame — no extras. No readable text, letters, digits or scale
markings on the level, strut or hull — the ring is a plain engraved
circle with no numbers; no lit displays; no subtitles, no watermark.
Neither suit has a back-mounted unit — no backpack, tank, hose, cable or
rear housing; both back silhouettes are flat. His visor is optically
clear — zero tint, zero mirror coating, zero reflection, no sand on the
glass. 0% bloom, no soft focus. Hand-tool contacts keep clear boundaries
— no merging, no extra fingers. Sand is granular under 1.1g — never
swirling or flowing like water. No heat-haze shimmer; terrain static. No
CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 2.5 metres from the leg at 0.8 metres height, 85mm
spherical lens, shallow depth of field, no camera movement. Exactly 2
human figures — one crouched at the leg, and one gloved hand and forearm
of the other steadying the strut.

SCENE: The port forward leg — a telescoping strut ending in a 1.2-metre
round sand pad, with a manual pump handle folded out at its knuckle and
a 9-centimetre bubble level set into the strut face. At the start the
strut is short, the pad hangs clear carrying no load, and the bubble
sits jammed against the rim of its glass, outside the engraved ring. The
bone-white hull rises behind the leg. Pale yellow-beige light, no
visible sun, shadows gone; a thin flowing layer of sand streams past.

CHARACTERS: The engineer — man, mid-thirties, 1.66 m, stocky and
thick-shouldered, pale heavily freckled skin with visible pores,
grey-green eyes, a short red-brown beard, cropped red hair, a
2-centimetre white scar on his left cheekbone; matte bone-and-sand
ceramic hard-shell suit, ribbed sand-shedding chest and thigh plates
over dark anthracite pressure weave, a machined collar ring, scraper
cuffs, finely scuffed, inlaid DEEP-VIOLET bands on shoulders and
forearms; low-profile helmet CLOSED with one seamless wraparound visor
of optically clear glass and a short rigid dust collar, his face
readable, angled down at the pump. Entering from the right edge, one
gloved hand and forearm with an inlaid ICE-BLUE band steadies the strut.
Dust state: every forward surface orange with packed sand, a crust of
sand on both gloves, helmet shell dusted; the 3-cm sealed strip under
his left shoulder plate stays clean bone white and his visor stays
spotless.

TIMELINE: 0.0s — He is already working the pump handle, short hard strokes with both gloved hands, his shoulders loading on every downstroke. 3.0s — The strut extends visibly: clean bone-white inner metal appears below the knuckle a few centimetres at a time, and the pad closes the gap to the ground. 6.0s — The pad meets the sand and takes load, pressing a shallow ring into the surface around its rim. The pumping slows. 8.5s — In the bubble level on the strut face the bubble travels across its glass and settles exactly inside the engraved centre ring. His hands stop on the handle. No cuts.

AUDIO: Directionless wind hiss. The ratcheting clack of a hand pump
under load, evenly spaced, then slowing. A dry crunch as the pad takes
the sand. Heavy breathing on an open radio channel. Then, over the
closed-helmet radio channel, a man's voice filtered to a narrow band
says in Turkish: "Kabarcik halkanin icinde. Seviye tuttu." No music.

PHYSICS: Gravity 1.1g. The pump extends the strut against the full
weight of the vehicle, so each stroke costs visible effort. Once the pad
takes load the hull rotates back toward level and the bubble follows it
directly. Real time, ordinary Earth pace — no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — one crouched, one hand and forearm at the frame edge; no
third figure, no duplicate, no second full body, no reflected face. The
vehicle is intact and whole — no wreckage, damage, debris, scorching,
fire or smoke. Exactly one leg, one pad, one pump handle and one bubble
level — no extras; the leg never detaches or breaks. No readable text,
letters, digits or scale markings on the level, strut or hull — the ring
is a plain engraved circle with no numbers; no lit displays; no
subtitles, no watermark. The spoken line is heard only — never shown as
text, no captions; one speaker only and no mouth is readable in frame.
Neither suit has a back-mounted unit — no backpack, tank, hose, cable or
rear housing; both back silhouettes are flat. His visor is optically
clear — zero tint, zero mirror coating, zero reflection, no sand on the
glass. 0% bloom, no soft focus. Hand-tool contacts keep clear boundaries
— no merging, no extra fingers. Sand is granular under 1.1g — never
swirling or flowing like water. No heat-haze shimmer; terrain static.
Real time, no slow motion. No CGI aesthetic. Photorealistic with 35mm
film grain.
```

---

## 🎬 SAHNE 20 (S20) — KAPAK

> ⚠️ **EĞİM KAPANDI.** S20'den itibaren "tilted 9 degrees" cümlesi
> hiçbir promptta geçmez. Kabin düz, kabarcık halkanın içinde, camdan
> görünen ufuk yatay.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Cockpit
interior seen from directly behind two seated figures. Exactly 2 human
figures in frame, both from behind.

SCENE: The cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays and no screens, and at its centre a 14-centimetre
mechanical bubble level with one bubble inside an engraved centre ring.
The bubble now sits exactly inside the engraving. Both figures are
strapped in, the harness straps drawn tight across their chest plates.
The engineer's gloved hand rests on a row of physical toggles. Through
the window the horizon is level, and along the left edge a
2-kilometre-high wall of suspended ocher dust spanning the full width of
the horizon, its base dark and its crest lit, is closer than it has been
in any previous shot. On the geologist's knees sits one 60 by 40 by 30
centimetre grey composite case with recessed handles and machined
corners.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. Seen from behind,
their faces are not in frame. The taller lean one on the right is the
geologist — woman, early forties, 1.78 m, inlaid ICE-BLUE bands on
shoulders and forearms. The shorter stocky one on the left is the
engineer — man, mid-thirties, 1.66 m, thick-shouldered, inlaid
DEEP-VIOLET bands on shoulders and forearms. Dust state: every forward
surface orange with packed sand, plate grooves overflowing, a crust of
sand on both gloves, helmet shells and shoulder tops dusted; the 3-cm
sealed strip under each left shoulder plate stays clean bone white.

ENVIRONMENT: The cabin is dim. The only light source is the orange
daylight coming through the forward window. Nothing in the cabin emits
light.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 1.2 metres behind the
seats at 1.3 metres height, centred between the two headrests so the
window, the bubble level and the case on her knees are all visible.

SPATIAL LOCK: The dust wall fills the left side of the window, matching
every exterior shot. The engineer sits screen-left, the geologist
screen-right.

PHYSICS: Gravity 1.1g and the vehicle is now level: both seated bodies
sit square, the bubble is centred and the horizon through the window is
horizontal.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— no duplicates, no third seat, no one else in the cabin, no reflected
face. Both are seen from behind; no mouth or face is visible. The cabin
is level — nothing is tilted. No readable text, letters, digits or
symbols anywhere; the panel is purely mechanical — no lit displays, no
screens, no HUD, no illuminated indicators. No subtitles, no watermark.
Exactly one case in the cabin. Neither suit has a back-mounted unit — no
backpack, tank, hose, cable or rear housing; both back silhouettes are
flat. Each visor is optically clear — zero tint, zero mirror coating,
zero reflection — and the window glass carries no reflection. 0% bloom,
no soft focus. No heat-haze shimmer through the window; terrain static.
No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 1.2 metres behind the seats at 1.3 metres height, 35mm
spherical lens, no camera movement. Exactly 2 human figures, both seen
from behind.

SCENE: The cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays and no screens, and at its centre a 14-centimetre
mechanical bubble level with one bubble inside an engraved centre ring.
The bubble sits exactly inside the engraving. Through the window the
horizon is level, and along the left edge a 2-kilometre-high wall of
suspended ocher dust spanning the full width of the horizon, its base
dark and its crest lit, is closer than in any previous shot. On the
geologist's knees sits one 60 by 40 by 30 centimetre grey composite
case. The cabin is dim; the only light is orange daylight through the
window and nothing inside emits light.

CHARACTERS: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. Seen from behind,
neither face is in frame. The taller lean one on the right is the
geologist — woman, early forties, 1.78 m, inlaid ICE-BLUE bands on
shoulders and forearms. The shorter stocky one on the left is the
engineer — man, mid-thirties, 1.66 m, thick-shouldered, inlaid
DEEP-VIOLET bands on shoulders and forearms. Dust state: every forward
surface orange with packed sand, a crust of sand on both gloves, helmet
shells and shoulder tops dusted; the 3-cm sealed strip under each left
shoulder plate stays clean bone white.

TIMELINE:
0.0s — The geologist pulls her harness strap tight across her chest
plate with one gloved hand and the buckle seats with a hard click.
3.0s — The engineer's gloved hand travels along a row of physical
toggles, throwing four of them one after another. Each moves with a
mechanical throw; nothing lights up.
6.0s — Both settle back. The bubble at the centre of the panel stays
exactly inside its engraved ring and does not drift.
9.0s — Through the window the wall on the left has closed further. Both
sit still, helmets level. No cuts.

AUDIO: A muffled version of the outside wind, its high frequencies cut
by the hull. The hard snap of a harness buckle. Four mechanical toggle
throws, evenly spaced. A faint suit-fan hum and two sets of breathing on
an open radio channel. Then, from the cabin speaker, a calm neutral
synthetic voice, off-screen and bodiless, says in Turkish: "Dort lule
hazir. Kalkis sende." No music.

PHYSICS: Gravity 1.1g and the vehicle is level: both seated bodies sit
square, the bubble stays centred and the horizon through the window
stays horizontal for the whole shot. Real time, ordinary Earth pace — no
slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — no duplicates, no third seat, no one else in the cabin,
no reflected face. Both are seen from behind throughout; no mouth or
face is ever visible. The cabin stays level — nothing tilts at any
point. The spoken line is heard only — never shown as text, no
subtitles, no captions; the synthetic voice is off-screen only, with no
body, face, avatar or third figure, and no mouth visible in frame. No
readable text, letters, digits or symbols anywhere; the panel is purely
mechanical — no lit displays, no screens, no HUD, no illuminated
indicators. Exactly one case in the cabin. Neither suit has a
back-mounted unit — no backpack, tank, hose, cable or rear housing; both
back silhouettes are flat. Each visor is optically clear — zero tint,
zero mirror coating, zero reflection — and the window glass carries no
reflection. 0% bloom, no soft focus. No heat-haze shimmer; terrain
static. Real time, no slow motion. No CGI aesthetic. Photorealistic with
35mm film grain.
```

---

## 🎬 SAHNE 21 (S21) — ⭐ VİRAL #4 · DORUK: KALKIŞ · **2 NUMARALI ÜRETİM KAPISI**

> ⛔ **DORUK BU SAHNENİN İÇİNDE TAMAMLANIR** [kontrol listesi B1]: dört
> lülenin ateşlemesi, kum çanağının açılması, düz seviyede yükselme,
> bacakların katlanması ve ileri hızlanma — beşi de 10 saniyenin içinde.
> ⛔ **KALKIŞ SIRASI DEĞİŞMEZ:** ① lüleler ateşler ② araç DÜZ SEVİYEDE
> yükselir ③ 20 m'de bacaklar katlanır ④ lüleler geriye eğilir ve araç
> ekran sağına hızlanır. Araç ASLA burnu yukarı kalkmaz — roket değildir.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Wide exterior
view of a vertical lift-off, desert planet. Exactly 0 human figures in
frame — no crew, no figure anywhere.

SCENE: A vehicle is lifting straight off loose sand. The hopper — an
11-metre low hexagonal-section surface lander, 6 metres wide and 3.2
metres tall, no rocket silhouette: a broad flat hull with crisp recessed
panel seams, a short forward canopy blended into the deck, four corner
LIFT NOZZLE pods that pivot from straight-down to rearward, four
telescoping landing legs ending in 1.2-metre round sand pads, and a wide
side cargo hatch; matte bone-white ceramic panels over an anthracite
structural frame, one thin anthracite stripe running the length of each
flank. The hull hangs about 8 metres above the surface, perfectly level,
its long axis horizontal — it is not tipped nose-up and it is not
standing on its tail. All four corner nozzle pods point straight down
and each drives a short hard column of gas into the sand. Beneath the
vehicle the loose sand has been blown outward into a broad shallow bowl,
and from the rim of that bowl a curtain of individual grains is
travelling outward and downward in flat ballistic arcs. Its starboard
side is clear of the dune now; behind it the steep 33-degree slip face
of the third dune stands untouched.

ENVIRONMENT: Pale yellow-beige sky, light directionless, shadows gone.
Along the left horizon a 2-kilometre-high wall of suspended ocher dust
spanning the full width of the horizon, its base dark and its crest lit.

CAMERA & LIGHT: 32mm spherical lens, fixed camera 60 metres from the
vehicle at 2 metres height. Flat diffuse light; the bone-white hull is
the brightest value and the four gas columns are colourless and
transparent, not luminous.

SPATIAL LOCK: The vehicle sits centre-right of frame with the dune
behind it on the right and the dust wall along the left horizon. The
blown sand travels outward from directly beneath the hull in every
direction.

PHYSICS: Gravity 1.1g. Four cold gas columns fluidise and eject the
loose bed beneath the hull; ejected grains follow flat ballistic arcs
and every one of them lands and stops within 3 seconds. No fireball, no
flame, no smoke — the columns are clear compressed gas, visible only by
the sand they move.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 0 human figures
— no crew, no figure, no silhouette, no one at the hatch or on the sand.
The vehicle is intact and whole, level and horizontal — it is never
tipped nose-up, never vertical, never standing on its tail, and it is
not a rocket. Exactly four legs and four corner nozzle pods, all four
pointing straight down — no extras, none firing sideways. No fire, no
flame, no fireball, no orange glow, no smoke, no soot, no mushroom
cloud, no shockwave ring, no lens flare — the gas columns are clear and
transparent. No wreckage, crash damage or debris; nothing falls off the
vehicle. No readable text, digits or hull markings; no subtitles, no
watermark. Ejected sand is discrete granular matter under 1.1g — flat
ballistic arcs settling within 3 seconds; never swirling, curling,
billowing, mushrooming or flowing like water or smoke. No heat-haze
shimmer; the dune behind is static and undisturbed. No mirrored
composition, no direction reversal. No CGI aesthetic. Photorealistic
with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 60 metres from the vehicle at 2 metres height, 32mm
spherical lens, no camera movement. Exactly 0 human figures — no crew,
no figure anywhere in frame.

SCENE: The hopper — an 11-metre low hexagonal-section surface lander, 6
metres wide and 3.2 metres tall, no rocket silhouette: a broad flat hull
with crisp recessed panel seams, a short forward canopy blended into the
deck, four corner LIFT NOZZLE pods that pivot from straight-down to
rearward, four telescoping landing legs ending in 1.2-metre round sand
pads, and a wide side cargo hatch; matte bone-white ceramic panels over
an anthracite structural frame, one thin anthracite stripe running the
length of each flank. It stands level on loose ocher sand, its long axis
horizontal, clear of the dune. Behind it on the right the steep
33-degree slip face of the third dune; along the left horizon a
2-kilometre-high wall of suspended ocher dust spanning the full width of
the horizon, its base dark and its crest lit. Pale yellow-beige sky,
light directionless.

TIMELINE:
0.0s — All four corner nozzle pods, pointing straight down, fire
together. Four short hard columns of clear gas strike the sand and the
loose bed beneath the hull blows outward into a widening shallow bowl,
grains leaving on flat ballistic arcs.
2.5s — The vehicle rises, perfectly level, its long axis staying
horizontal. It does not tip, does not pitch nose-up and does not stand
on its tail. The ejected grains reach their range and land, settling
within 3 seconds.
5.5s — At about 20 metres the four telescoping legs fold up into the
belly one after another and their 1.2-metre pads seat flush against the
hull. From this point no leg and no open leg well is visible.
8.0s — All four nozzle pods pivot from straight-down to rearward. The
downward columns cut off, the vehicle stops climbing and accelerates
forward, moving screen-left to screen-right and still perfectly level.
10.0s — It is smaller and further right, still horizontal, still
climbing away. No cuts.

AUDIO: A hard flat roar of compressed gas, four sources close together,
starting instantly with no ignition boom and no explosion. Under it the
dense granular rush of a sand bed being thrown outward, then that sound
falling away as the vehicle climbs. Four mechanical thuds as the legs
seat home. The roar changes character but does not stop when the nozzles
pivot. No voices. No music.

PHYSICS: Gravity 1.1g. Four cold gas columns fluidise and eject the
loose bed beneath the hull; ejected grains follow flat ballistic arcs
and land within 3 seconds. The vehicle stays level throughout because
all four nozzles are matched — this is a four-corner lift, not a rocket
launch. No combustion: the columns are clear compressed gas, visible
only through the sand they move. Real time, ordinary Earth pace — no
slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom, no camera
movement even as the vehicle climbs. Exactly 0 human figures — no crew,
no figure, no silhouette, no one at the hatch. The vehicle is intact and
whole and stays level and horizontal for the entire shot — it never tips
nose-up, never goes vertical, never stands on its tail, never rolls, and
it is not a rocket. Exactly four legs and four corner nozzle pods; after
the legs fold, no leg, no pad and no open leg well is visible in any
frame. No fire, no flame, no fireball, no orange glow, no exhaust plume
of smoke, no soot, no mushroom cloud, no shockwave ring, no ignition
explosion, no lens flare — the gas columns are clear and transparent.
Nothing falls off the vehicle; no debris, no fragments, no panels shed.
No readable text, digits or hull markings; no subtitles, no watermark.
Ejected sand is discrete granular matter under 1.1g — flat ballistic
arcs settling within 3 seconds; never swirling, curling, billowing,
mushrooming, rolling or flowing like water or smoke. No dust devils. No
heat-haze shimmer; the dune behind stays static and undisturbed. No
direction reversal — the vehicle accelerates screen-right only. Real
time, no slow motion, no speed ramp. No CGI aesthetic. Photorealistic
with 35mm film grain.
```

---

## 🎬 SAHNE 22 (S22) — ÇANAK

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Ground-level
view of an empty landing site, desert planet. Exactly 0 human figures in
frame — no crew, no figure anywhere.

SCENE: What the vehicle left behind. The blast bowl — a 14-metre-wide
shallow circular depression scoured into the sand, its rim slumping
inward — fills the centre of the frame, its floor swept clean of ripples
and its edges already failing inward in small granular tongues. Outside
the bowl, untouched by it, stand eleven identical 60 by 40 by 30
centimetre grey composite cases with recessed handles and machined
corners, upright on the sand in a single straight line. There is no
vehicle in frame. Behind everything rises the steep 33-degree slip face
of the third dune, and along the left edge of frame the leading base of
a 2-kilometre-high wall of suspended ocher dust spanning the full width
of the horizon, its base dark and its crest lit, has entered the shot.

ENVIRONMENT: Pale yellow-beige sky, light completely directionless,
shadows gone. A thin flowing layer of sand streams across the ground
below knee height and pours over the rim of the bowl.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 8 metres from the near
rim of the bowl at 0.8 metres height, low enough that the bowl reads as
a depression and the line of cases stands against the sky. Flat diffuse
light; the grey cases are the darkest values in frame.

SPATIAL LOCK: The bowl occupies the centre and lower half of the frame;
the line of cases runs across the right half; the dune stands behind on
the right; the dust wall enters from the left edge. Sand streams
screen-left to screen-right and pours over the left rim of the bowl.

PHYSICS: Gravity 1.1g. The bowl's rim stands steeper than the 33-degree
angle of repose and is failing inward in small granular tongues that
shear, spread and stop. Wind-driven grains are refilling the bowl from
the upwind side.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 0 human figures
— no crew, no figure, no silhouette, no shadow. No vehicle anywhere in
frame. Exactly eleven cases, all identical, all upright, in one straight
line — none tipped, none open, none broken, nothing spilled. No fire, no
flame, no smoke, no soot, no scorching and no burn marks anywhere in the
bowl — it is a mechanically scoured depression, not a blast crater. No
readable text, letters, digits or labels; no subtitles, no watermark.
Sand is discrete granular matter under 1.1g — the rim fails in tongues
that shear, spread and stop within 3 seconds; never swirling, curling or
flowing like water or smoke. No heat-haze shimmer, no mirage; terrain
static apart from the rim failures. No mirrored composition, no
direction reversal. No CGI aesthetic. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 8 metres from the near rim of the bowl at 0.8 metres
height, 35mm spherical lens, no camera movement. Exactly 0 human figures
— no crew, no figure anywhere in frame.

SCENE: The blast bowl — a 14-metre-wide shallow circular depression
scoured into the sand, its rim slumping inward — fills the centre of the
frame, its floor swept clean of ripples. Outside it stand eleven
identical 60 by 40 by 30 centimetre grey composite cases with recessed
handles and machined corners, upright on the sand in a single straight
line. There is no vehicle in frame. Behind everything rises the steep
33-degree slip face of the third dune; along the left edge the leading
base of a 2-kilometre-high wall of suspended ocher dust spanning the
full width of the horizon, its base dark and its crest lit, has entered
the shot. Pale yellow-beige sky, light directionless, shadows gone.

TIMELINE:
0.0s — Stillness. The bowl is empty and swept clean; the eleven cases
stand outside it; sand streams screen-left to screen-right and pours
over the left rim.
3.0s — A section of the upwind rim fails: a tongue of sand shears loose,
breaks into grains, spreads across the bowl floor and stops within 3
seconds. The bowl is a few centimetres smaller than it was.
6.0s — A second, smaller failure runs down the far rim. The swept floor
begins to take its first wind ripples.
9.0s — Held. The dust wall on the left edge has advanced across a
measurable fraction of the frame width, and the nearest case now stands
against it. No cuts.

AUDIO: The wind at full strength — a broad dry granular hiss with
individual grain collisions inside it, and a low slow rumble beneath
from the left, closer than before. Two short dry granular slumps as the
rim fails. A fine patter of grains striking hard composite. No voices,
no breathing, no engine — the vehicle is gone.

PHYSICS: Gravity 1.1g. The bowl's rim stands steeper than the 33-degree
angle of repose and fails inward in granular tongues that shear, spread
and stop. Wind-driven grains refill the bowl from the upwind side and
begin rebuilding ripples on its swept floor. Real time, ordinary Earth
pace — no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 0
human figures — no crew, no figure, no silhouette and no one entering
frame. No vehicle anywhere in frame at any point. Exactly eleven cases,
all identical, all upright, in one straight line — none tipped, none
open, none broken, nothing spilled, and none of them moves. No fire, no
flame, no smoke, no soot, no scorching, no burn marks and no embers
anywhere in the bowl — it is a mechanically scoured depression, not a
blast crater. No readable text, letters, digits or labels; no subtitles,
no watermark. Sand is discrete granular matter under 1.1g — the rim
fails in tongues that shear, spread and stop within 3 seconds; never
swirling, curling, billowing or flowing like water or smoke. No
heat-haze shimmer, no mirage; terrain static apart from the described
rim failures. No direction reversal — sand streams screen-right
throughout. Real time, no slow motion. No CGI aesthetic. Photorealistic
with 35mm film grain.
```

---

## 🎬 SAHNE 23 (S23) — TEK KASA

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Cockpit
interior seen from directly behind two seated figures, in flight.
Exactly 2 human figures in frame, both from behind.

SCENE: The cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays and no screens, and at its centre a 14-centimetre
mechanical bubble level with one bubble inside an engraved centre ring.
Through the window there is no ground close by: far below, an ocher sand
field combed into long parallel ridges, and crossing them at an angle a
single larger ridge that breaks their rhythm. The horizon is high and
flattening. On the geologist's knees, held under one gloved hand, sits
one 60 by 40 by 30 centimetre grey composite case with recessed handles
and machined corners — the only case in the cabin.

SUBJECT: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. Seen from behind,
their faces are not in frame. The taller lean one on the right is the
geologist — woman, early forties, 1.78 m, inlaid ICE-BLUE bands on
shoulders and forearms. The shorter stocky one on the left is the
engineer — man, mid-thirties, 1.66 m, thick-shouldered, inlaid
DEEP-VIOLET bands on shoulders and forearms. Dust state: every forward
surface orange with packed sand, plate grooves overflowing, a crust of
sand on both gloves, helmet shells and shoulder tops dusted; the 3-cm
sealed strip under each left shoulder plate stays clean bone white.

ENVIRONMENT: The cabin is dim. The only light source is the daylight
coming through the forward window, cleaner and paler now than on the
ground. Nothing in the cabin emits light.

CAMERA & LIGHT: 35mm spherical lens, fixed camera 1.4 metres behind the
seats at 1.3 metres height, centred between the two headrests so the
window, the panel and the case on her knees are all visible.

SPATIAL LOCK: The window fills the upper centre of the frame. The
engineer sits screen-left, the geologist screen-right, her gloved hand
on the case. The diagonal ridge crosses the parallel ridges in the lower
part of the window.

PHYSICS: Gravity 1.1g and the vehicle is level and in forward flight:
both seated bodies sit square, the bubble stays centred, the case rests
under its own weight on her knees and does not float.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures
— no duplicates, no third seat, no one else in the cabin, no reflected
face. Both are seen from behind; no mouth or face is visible. Exactly
one case in the cabin, resting under its own weight — nothing floats,
nothing is weightless. No readable text, letters, digits or symbols
anywhere — the panel is purely mechanical, with no lit displays, no
glowing graphics, no screens, no HUD and no illuminated indicators. No
subtitles, no watermark. Neither suit has a back-mounted unit — no
backpack, tank, hose, cable or rear housing; both back silhouettes are
flat. Each visor is optically clear — zero tint, zero mirror coating,
zero reflection — and the window glass carries no reflection. 0% bloom,
no soft focus. No heat-haze shimmer through the window; the terrain
below is static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 1.4 metres behind the seats at 1.3 metres height, 35mm
spherical lens, no camera movement. Exactly 2 human figures, both seen
from behind.

SCENE: The cabin seen from directly behind both seats — a 2.4-metre-wide
two-seat cockpit, the two seats side by side, a single wide forward
window 1.6 metres across and 0.45 metres tall spanning both seats; the
panel is entirely mechanical, rows of physical toggles and levers with
no lit displays and no screens, and at its centre a 14-centimetre
mechanical bubble level with one bubble inside an engraved centre ring.
Through the window, far below, an ocher sand field combed into long
parallel ridges, and crossing them at an angle a single larger ridge
that breaks their rhythm. On the geologist's knees, under one gloved
hand, sits one 60 by 40 by 30 centimetre grey composite case — the only
case in the cabin. The cabin is dim; the only light is pale daylight
through the window.

CHARACTERS: Both wear the same suit: matte bone-and-sand ceramic hard
shell, ribbed sand-shedding chest and thigh plates over dark anthracite
pressure weave, a machined collar ring, scraper cuffs, finely scuffed;
low-profile helmets CLOSED, each with one seamless wraparound visor of
optically clear glass and a short rigid dust collar. Seen from behind,
neither face is in frame. The taller lean one on the right is the
geologist — woman, early forties, 1.78 m, inlaid ICE-BLUE bands on
shoulders and forearms. The shorter stocky one on the left is the
engineer — man, mid-thirties, 1.66 m, thick-shouldered, inlaid
DEEP-VIOLET bands on shoulders and forearms. Dust state: every forward
surface orange with packed sand, a crust of sand on both gloves, helmet
shells and shoulder tops dusted; the 3-cm sealed strip under each left
shoulder plate stays clean bone white.

TIMELINE:
0.0s — Both sit still, helmets level, facing the window. Far below, the
parallel ridges slide slowly past.
3.0s — The horizon in the window flattens by a visible amount as the
vehicle climbs. The bubble at the centre of the panel stays inside its
engraved ring.
6.0s — The single diagonal ridge crosses the lower part of the window
and moves out of it, and neither of them turns to follow it.
9.0s — The geologist's gloved hand, resting on the case on her knees,
closes slightly on its recessed handle and stays there. Nothing else
moves. No cuts.

AUDIO: A steady muffled flight tone through the hull, low and even, with
no wind hiss and no grain ticks for the first time in the film. A faint
suit-fan hum. Two sets of slow breathing on an open radio channel,
unhurried. No words. No music.

PHYSICS: Gravity 1.1g and the vehicle is level and in forward flight:
both seated bodies sit square, the bubble stays centred, and the case
rests under its own weight on her knees — nothing floats or drifts. Real
time, ordinary Earth pace — no slow motion.

NEGATIVE: Fixed locked-off single take — no cuts, pans, zoom. Exactly 2
human figures — no duplicates, no third seat, no one else in the cabin,
no reflected face. Both are seen from behind throughout; no mouth or
face is ever visible. Exactly one case in the cabin, resting under its
own weight — nothing floats, nothing is weightless, nothing drifts. No
readable text, letters, digits or symbols anywhere; the panel is purely
mechanical — no lit displays, no screens, no HUD, no illuminated
indicators. No subtitles, no watermark. Neither suit has a back-mounted
unit — no backpack, tank, hose, cable or rear housing; both back
silhouettes are flat. Each visor is optically clear — zero tint, zero
mirror coating, zero reflection — and the window glass carries no
reflection. 0% bloom, no soft focus. The terrain below is static — no
melting, no warping, no swimming texture. Real time, no slow motion. No
CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 24 (S24) — FİNAL: İZ

> 🔁 **AÇILIŞ-KAPANIŞ ÇİFTİNİN İKİNCİ YARISI.** S0 ile aynı lens (24mm),
> aynı bakış açısı (30° aşağı), aynı tarak deseni, aynı çapraz sırt.
> ⚠️ **BİLİNÇLİ TEK FARK — YÜKSEKLİK:** S0 400 m, S24 **200 m**.
> Gerekçe açıkça yazılır: kapanış karesinin göstermesi gereken şey
> (14 m çanak + on bir kasa) 400 metreden okunamaz. Kadraj ailesi aynı
> kalır, ölçek okunur hâle gelir. Bu, ölçek dizisindeki ikinci ve son
> bilinçli sapmadır [uzamsal kılavuz §4.3].
> 🎵 Müzik 4:07'de CÜMLE ORTASINDA kesilir; son 2 saniye yalnız ortam
> yatağıdır. Fade YOK, kadans YOK.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. High aerial
view of a desert planet, the same look-down composition as the film's
opening but from half the height. Exactly 0 human figures in frame — no
crew, no figure anywhere.

SCENE: An endless field of ocher sand seen from 200 metres up. Long
parallel sand ridges run across the whole frame in the same regular comb
pattern, crests combed with 8-centimetre ripples. In the right third a
single larger ridge still cuts across that rhythm at a 30-degree angle.
But the bone-white corner that protruded from its flank is gone: where
it was there is now the blast bowl — a 14-metre-wide shallow circular
depression scoured into the sand, its rim slumping inward — a clean
round scar in a landscape of long curves. Beside it, outside the bowl,
eleven identical 60 by 40 by 30 centimetre grey composite cases with
recessed handles and machined corners stand upright on the sand in a
single straight line: eleven tiny dark specks, the only straight line in
the world. There is no vehicle anywhere in frame. Along the left edge
the leading base of a 2-kilometre-high wall of suspended ocher dust
spanning the full width of the horizon, its base dark and its crest lit,
has crossed into the shot and reached the first speck in the line.

ENVIRONMENT: Dry nitrogen-argon atmosphere at 0.8 of Earth pressure. Sky
pale yellow-beige, rusting to orange at the horizon. Light completely
directionless, shadows gone, the world one warm orange-grey value. Fine
sand drifts steadily across every ridge crest.

CAMERA & LIGHT: 24mm spherical lens, fixed high aerial position, 200
metres above the sand, angled 30 degrees down — the same lens and the
same angle as the opening shot of the film, from half the height. Flat
diffuse light; the grey specks are the darkest values in frame.

SPATIAL LOCK: The crossing ridge, the bowl and the line of specks sit in
the right third of the frame, exactly where the bone-white corner sat in
the opening shot. The dust wall enters along the left edge. Sand drifts
screen-left to screen-right everywhere in frame.

PHYSICS: Gravity 1.1g. Wind-driven grains are refilling the bowl from
its upwind rim and banking against the upwind face of every speck in the
line. Suspended dust settles within 40 seconds; surface grains within 3.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 0 human figures
— no crew, no figure, no silhouette, no shadow. No vehicle, no aircraft,
no contrail and no exhaust trail anywhere in frame. Exactly eleven
specks, all identical, all upright, in one straight line — none tipped,
none scattered. No bone-white object protrudes from the ridge any more.
No fire, no smoke, no scorching, no burn marks in the bowl. No readable
text, letters or digits; no subtitles, no title card, no watermark. Sand
is discrete granular matter under 1.1g — never swirling, curling or
flowing like water or smoke; the dust wall creeps and never mushrooms.
No heat-haze shimmer, no mirage; terrain static. No mirrored composition
— the crossing ridge and the bowl never appear on the left side of
frame. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off aerial camera, 24mm spherical lens, 200 metres above the
sand, angled 30 degrees down — the same lens and angle as the film's
opening shot, from half the height. No camera movement. Exactly 0 human
figures — no crew, no figure anywhere in frame.

SCENE: An endless ocher sand field. Long parallel ridges run across the
frame in a regular comb pattern, crests combed with 8-centimetre
ripples. In the right third a single larger ridge still cuts that rhythm
at a 30-degree angle, but the bone-white corner that protruded from its
flank is gone. In its place: the blast bowl — a 14-metre-wide shallow
circular depression scoured into the sand, its rim slumping inward — and
beside it, outside the bowl, eleven identical grey composite cases
standing upright in a single straight line, eleven tiny dark specks, the
only straight line in the world. There is no vehicle anywhere in frame.
Along the left edge the leading base of a 2-kilometre-high wall of
suspended ocher dust spanning the full width of the horizon, its base
dark and its crest lit, has crossed into the shot. Pale yellow-beige
sky, light directionless, shadows gone.

TIMELINE:
0.0s — Stillness at scale. Sand drifts steadily across every crest
screen-left to screen-right. The bowl and the line of eleven specks sit
in the right third.
3.0s — The base line of the dust wall advances across the sand from the
left, swallowing one rippled ridge as it comes. The ridge does not blow
away; it simply disappears behind the dust.
6.0s — The wall's edge reaches the first speck in the line. The speck
does not move — it is simply not there any more, covered.
9.0s — Held. Ten specks remain visible, the bowl is taking its first
wind ripples, and the wall keeps coming. No cuts.

AUDIO: A broad dry granular hiss of wind over sand, wide and distant,
with individual grain collisions inside it. Beneath it a very low slow
rumble, closer than in the opening shot. No voices, no engine, no
breathing. No music.

PHYSICS: Gravity 1.1g. Grains follow individual ballistic arcs and
settle within 3 seconds; suspended dust settles within 40. The wall
advances at 15 metres per second — it creeps, it does not billow, roll
or mushroom. Real time, ordinary Earth pace — no slow motion.

NEGATIVE: Fixed locked-off camera, single unbroken take — no cuts, pans,
zoom, no camera movement. Exactly 0 human figures — no crew, no figure,
no silhouette, no one entering frame. No vehicle, no aircraft, no
contrail and no exhaust trail anywhere at any point. Exactly eleven
specks in one straight line at the start — none tipped, none scattered,
and they disappear only by being covered, never by moving. No bone-white
object protrudes from the ridge. No fire, no smoke, no scorching in the
bowl. No readable text, letters or digits; no subtitles, no title card,
no end card, no credits, no watermark — the take ends on the held frame
and no text ever appears. Sand is discrete granular matter under 1.1g —
never swirling, curling or flowing like water or smoke; the wall creeps
and never mushrooms. No heat-haze shimmer, no mirage; terrain static. No
direction reversal — drift and the wall both run screen-left to
screen-right. Real time, no slow motion. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

---

# 📋 PART B ÖZET TABLOSU

| # | Sahne | Lens | Kamera (mesafe / yükseklik) | İnsan | Toz | Replik |
|---|---|:--:|---|:---:|:---:|:---:|
| S13 | ENVANTER | 35mm | 25 m / 1.6 m | 2 | 3 | — |
| S14 | KAZI | 35mm | 4 m / 1.1 m | 2 | 4 | — |
| S15 | ⭐ AKIŞKAN KUM | 85mm | 2 m / 0.6 m | **1** | 4 | — |
| S16 | TARTI | 35mm | kabin, 1.2 m arkadan | 2 | 4 | ÇOBAN + MÜHENDİS |
| S17 | ⭐ CENTRAL CHOICE | 35mm | 3 m / 1.5 m | 2 | 4 | JEOLOG |
| S18 | BIRAKILAN 🔇 | 50mm | 6 m / 0.5 m | **0** | — | — |
| S19 | SEVİYE | 85mm | 2.5 m / 0.8 m | 2 | 4 | MÜHENDİS |
| S20 | KAPAK | 35mm | kabin, 1.2 m arkadan | 2 | 4 | ÇOBAN |
| S21 | ⭐ DORUK — KALKIŞ | 32mm | 60 m / 2 m | **0** | — | — |
| S22 | ÇANAK | 35mm | 8 m / 0.8 m | **0** | — | — |
| S23 | TEK KASA | 35mm | kabin, 1.4 m arkadan | 2 | 4 | — |
| S24 | FİNAL — İZ | 24mm | **200 m havadan**, 30° aşağı | **0** | — | — |

```
PART B DOĞRULAMASI
□ 12 sahne bloğu (S13-S24), numara atlaması yok                       ✅
□ süre: 12 × 10 s = 120 s · film toplamı 129 + 120 = 249 s            ✅
□ 12 IMAGE + 12 VIDEO = 24 prompt                                     ✅
□ insan sayımı: 2×7 · 1×1 (S15) · 0×4 (S18·S21·S22·S24)               ✅
□ kask: 8/8 insanlı sahnede KAPALI, kasksız sahne SIFIR               ✅
□ toz seviyesi: S13 = 3 · S14-S23 = 4 — monotonik, geri gitmiyor      ✅
□ replik: 5 (S16 ×2 · S17 · S19 · S20) / 4 sahne · 8 sahne sessiz     ✅
□ ağız kadrajda: 0 replik (kokpit arkadan, dış sahnelerde eğik/kısmi) ✅
□ eğim kapanışı: "tilted 9 degrees" S20'den sonra HİÇBİR promptta yok ✅
□ üç sayaç kanalı da okundu: toz 3→4 · kabarcık dışarıda→içeride ·
  raf 12 dolu → 1 dolu + 11 BOŞ YUVA                                  ✅
□ hiçbir promptta ekran / gösterge ışığı / rakam / metin yok          ✅
□ hiçbir promptta biniş-iniş hareketi yok [D69] — kapak S13'te ZATEN
  açık, S17 bölmenin İÇİNDE başlıyor                                  ✅
□ ateş / alev / duman: S21 kalkışta bile SIFIR — lüleler şeffaf gaz   ✅
```

---

# 🎞️ FİLM ÖZET TABLOSU — 25 SAHNE

| # | Sahne | Bölüm | İnsan | Replik | Vuruş |
|---|---|:--:|:---:|:---:|---|
| S0 | HOOK — HARMAN | A | 2 | — | açılış imajı |
| S1 | GEVŞEK ZEMİN | A | 2 | ÇOBAN | **katalizör 0:14** |
| S2 | KERTİK'TEN AYRILIŞ | A | 2 | — | kurulum |
| S3 | ⭐ SALTASYON | A | 2 | — | **viral #1** |
| S4 | AVUÇ | A | 2 | MÜHENDİS | tartışma |
| S5 | HAT | A | 2 | — | tartışma |
| S6 | ⭐ DUVAR | A | 2 | — | **viral #2** |
| S7 | SIRT | A | 2 | — | sahte zafer |
| S8 | ÜÇ | A | 2 | JEOLOG | bahis yükselir |
| S9 | İNİŞ | A | 2 | — | — |
| S10 | İZ YOK | A | 1 | — | — |
| S11 | KÖŞE | A | 2 | MÜHENDİS | — |
| S12 | ⭐ ÜÇÜNCÜ TEPE | A | 2 | ÇOBAN | **orta nokta · viral #3** |
| S13 | ENVANTER | B | 2 | — | teşhis |
| S14 | KAZI | B | 2 | — | umut |
| S15 | ⭐ AKIŞKAN KUM | B | 1 | — | **umut-önce-düşüş** |
| S16 | TARTI | B | 2 | ÇOBAN+MÜH. | **her şeyin kaybı** |
| S17 | ⭐ RAF | B | 2 | JEOLOG | **CENTRAL CHOICE** |
| S18 | BIRAKILAN 🔇 | B | 0 | — | bedel görülür |
| S19 | SEVİYE | B | 2 | MÜHENDİS | onarım |
| S20 | KAPAK | B | 2 | ÇOBAN | eşik |
| S21 | ⭐ KALKIŞ | B | 0 | — | **DORUK · viral #4** |
| S22 | ÇANAK | B | 0 | — | çözülme |
| S23 | TEK KASA | B | 2 | — | insan anı |
| S24 | FİNAL — İZ | B | 0 | — | **kapanış imajı** |

```
SÜRE     Hook 9 s + 24 × 10 s = 249 s = 4:09
İNSAN    2 × 19 sahne · 1 × 2 sahne · 0 × 4 sahne = 25
REPLİK   10 / 9 sahne — 4 MACHINE (ÇOBAN) · 6 HUMAN · ağız kadrajda 0
SESSİZ   16 sahne
VİRAL    S3 · S6 · S12 · S21  ⛔ KESİLEMEZ
KAMERA   25/25 sabit lockoff · 0 kesme · 0 kamera hareketi
ÜRETİM   25 imaj + 25 video (10 s klip = Veo 8 s + 2 s extend, Hook 9 s)
```

---

# 🚪 KURGU KAPISI — teslimden önce işaretlenir

> [DERS 70 · 72 · 81 · 83] Cold Burn'de bu kapının DÖRT maddesi birden
> delindi ve bu depoda ilk kez oldu. Aşağıdaki liste PLAN dosyasındaki
> kapıyla birebir aynıdır ve teslimden önce tek tek işaretlenir.

```
□ klip sayısı = 25 (S0-S24, numara atlaması yok)
□ toplam süre 249 s ± 2 s
□ ekran metni 0,0 sn — başlık kartı YOK; kapak çıktısı kurguya
  EKLENMEZ (ayrı dosyadır, klip zincirine karışmaz)
□ CENTRAL CHOICE (S17) kurguda VAR ve seçim ekranda TAMAMLANIYOR —
  son kasa 8,5. saniyede kadrajı terk ediyor, 11 boş yuva görünüyor
□ DORUK (S21) kurguda VAR ve kalkış sırası eksiksiz: lüleler →
  çanak → düz yükselme → bacakların katlanması → ileri hızlanma
□ dört viral ara (S3 · S6 · S12 · S21) kurguda VAR — KESİLEMEZ
□ sahne SIRASI plana birebir eşit; yer değiştirme yok [D81]
□ ortam ses yatağı 249 s boyunca KESİNTİSİZ — hiçbir klip sınırında
  dijital sıfır yok; S18'in 12 saniyesi MÜZİKSİZ ama yatak -18 dBFS
  ile TAM GÜÇTE [D83]
□ dialogue ledger doğrulandı: 10 replik · 4 MACHINE (gövdesiz, ekran
  dışı, nefessiz, cızırtısız) · 6 HUMAN (kask telsizi EQ'su, nefesli)
  · ağız kadrajda 0 [D82]
□ toz seviyesi monotonik: 2 → 3 → 4, geri gitmiyor
□ araç ve tepe 25/25 sahnede ekran SAĞINDA, yön hiç ters dönmedi
□ eğim: S12-S19 arası 9°, S20'den sonra 0° — geri dönmüyor
```

---

# 🏭 ÜRETİM SIRASI — dört kapı

> ⛔ Kapıların SONUCU bu dosyaya yazılır. Kaydı olmayan kapı, koşulmamış
> kapıdır [DERS 74]. Cold Burn'de dört kapının dördünün de kaydı yoktu.

```
1. S15  AKIŞKAN KUM   → kum granüler mi çöküyor, sıvı gibi mi akıyor?
   ⛔ BU KAPI GEÇİLMEDEN DİĞER 24 SAHNE ÜRETİLMEZ.
   SONUÇ: ______________________  tarih: __________

2. S21  KALKIŞ        → dört lüle · radyal çanak · DÜZ SEVİYEDE
   yükselme · bacakların katlanması · ateş/alev SIFIR.
   Araç burnu yukarı kalkarsa ya da alev çıkarsa prompt V2.
   SONUÇ: ______________________  tarih: __________

3. S17  KARGO BÖLMESİ → klon sıcak noktası [D69]. Klon çıkarsa mühendis
   sahneden çıkarılır, repliği telsizden gelir (maliyet 0 s).
   SONUÇ: ______________________  tarih: __________

4. S12  ÜÇÜNCÜ TEPE   → ölçek: 40 m tepe ↔ 11 m araç ↔ 1.78 m insan
   aynı karede, oran cümleyle yazılı.
   SONUÇ: ______________________  tarih: __________
```

---

## 📌 SONRAKİ ADIM

**AŞAMA 4.5 — `THE_THIRD_DUNE_REFERANS_PAKETI.md`**
Cold Burn emsali: metin çapası tek başına aracı ve suiti sabitlemedi
(D79 ×4). Paketin taşıyacağı altı varlık: jeolog · mühendis (**ikisi de
ARKADAN görünüm dahil** — D79'un ikinci savunma hattı) · araç · üçüncü
tepe · kabin · 12 yuvalı kargo rafı.
⛔ Bu paket onaylanmadan AŞAMA 5 (üretim) başlamaz.

Yazım tamam: **PLAN + PART_A + PART_B + KAPAK + MUZIK.**
