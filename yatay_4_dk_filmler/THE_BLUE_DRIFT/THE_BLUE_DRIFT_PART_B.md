# 🔵 THE BLUE DRIFT — Mavi Süzülüş | PART B

## AI Production Bible — Self-Contained Prompts
### PART B: Sahne 13-24 (12 sahne) | 16:9 Yatay | Yakalayış
### _"Onları kurtaran şey, hiçbir şey yapmamalarıydı."_

> **PART B süresi:** 12 sahne × 10s = 120 saniye (2:09 – 4:09)
> **Toplam film:** 25 sahne = 249 saniye = 4 dakika 09 saniye
> **PART A:** `THE_BLUE_DRIFT_PART_A.md` (S0-S12 + Bible'lar + çapa blokları)
> **Plan:** `THE_BLUE_DRIFT_PLAN.md` — QA SPEC, risk kartları, A4 kararları orada

---

## ⚠️ PART B ÜRETİM NOTLARI

```
① İNSANSIZ SAHNELER (S13 · S15 · S21 · S24 — 4 sahne / 8 prompt) —
   Part A üretim notu ① aynen geçerli: NEGATIVE kısa, boş kadraj
   pozitif, insan sayısı imzası "Human count in this frame: zero —
   both crew are inside the dead lander" biçiminde. Yapısal red
   gelirse KILAVUZ §7 merdiveni.

② UZUNLUK BANDI — Part A üretim notu ② aynen geçerli (çapa blokları
   kısaltılamaz; kapatma yolu: red alan promptun NEGATIVE'i tek Style
   satırına iner; 3 red / 0 başarı → 3 satırlık prob).
   → prompt_kontrol 17.08.2026: 24 prompt · 0 BLOCK · FIX yalnız
     uzunluk — image 1.807-2.646 · video 2.373-3.406 · TAVAN (4.300)
     aşımı SIFIR · uzunluk dışı bulgu SIFIR (yönelim/çapa/yasak
     kelime temiz).

③ ⭐ HİÇBİR ŞEY YAPMAMA KİLİDİ (bu partın kendi tuzağı): S15'in son
   pufundan sonra LANDER TARAFINDA HİÇBİR ŞEY ATEŞLEMEZ — jet yok,
   düzeltme yok, ışık değişimi yok; ölü araçta hareket eden tek şey
   2 saniyelik amber nabızdır. Model ölü araca düzeltme jeti çizerse
   filmin tezi ölür. Bu kilit S16-S21 arası her promptun gövdesinde
   VE negatifinde yazılıdır ("the lander fires nothing").

④ MOTOR YASAĞI TERSİ: S20'nin 3.0 saniyesinden sonra GEMİ DE
   ateşlemez — son fren darbesinden yakalayışa kadar iki gövde de ölü
   süzülür (S20 geç yarısı · S21 · S22). İlk ihlal kurguda değil
   promptta yakalanır — üç sahnenin negatifinde "no engine, no
   thruster fires on either craft" yazılıdır. (S24 füzyon tahriki
   yanaşmadan SONRADIR — yasağın dışında.)

⑤ EKSEN AİLESİ [Black Cradle liman bakışı emsali · D104]: dış
   yaklaşma sahneleri eksen-üstüdür — S17·S19·S20 kokpit CAMINDAN
   dead-on (gemi kadraj merkezinde büyür/ıraksar/büyür; üçlü merdiven,
   tek değişken mesafe+motor durumu) · S21 hangar İÇİNDEN dead
   NOSE-ON (araç burnu kameraya dönük süzülerek girer — Black
   Cradle'ın tail-on'unun aynadaki tersi). Yanal kalan dış kareler
   statiktir ve yön taşımaz: S13 · S15 (araç yakını) · S24 (final).

⑥ AMBER NABIZ SÜREKLİLİĞİ: verici nabzı S10'da başlar, periyodu TAM
   2 saniyedir ve S21'in gölge geçişine kadar hiçbir sahnede ritim
   değiştirmez. S21'de kızak kolları kapanırken nabız SÜRER (kalp
   atışı doruğun içinden geçer). S22'den itibaren verici kadraj
   dışıdır; S24'te mesafeden görünmez.

⑦ PERDE PART B'DE YOK: balistik yörünge plazma yaprağının üstündedir
   — S13-S22 arası hiçbir karede aurora yok. Tek istisna S24: uydunun
   gece yüzünde UZAK bir taç, artık yalnız manzara (açılış-kapanış
   çifti).

⑧ İBRE TAKVİMİ [D78 ①]: kabin basınç ibresi üç durumda görünür —
   S14 needle high (%100 yakını) · S16 needle at the 40% tick (KERTE
   sayıyı sesle doğrular — çift kanal) · S22 needle slowly RISING
   (hangar basınçlanıyor — nefesin dönüşü). Ara değer üretilmez;
   başka sahnede ibre kadraja alınmaz.
```

---

## ⚓ PART B ÇAPA EKLERİ — KANONİK BLOKLAR

> Part A çapa kuralı aynen geçerli: blok kelimesi kelimesine
> kopyalanır, sahneye özel durum bloktan SONRA ayrı cümleyle gelir.

```
MAIN SHIP — TAM BLOK (S17 · S19 · S20 · S24): the main ship — a
135-metre INTERSTELLAR transfer vessel, fifteen times the lander's
length, satin steel-blue with sparse thin white position lines: a
closed sensor dome at the bow, six cylindrical habitat modules in
three tandem pairs wrapped in dark quilted insulation, a long open
hexagonal truss spine carrying an OPEN CATCH BAY at midships — a
12-metre hangar slot, 7 metres wide and 5 metres deep, flanked by two
machined yoke arms, four open clamps along its rails and four small
WHITE frame lights marking the corners of its mouth — two dark
knife-edge radiator wings, and an aft fusion drive block with four
deeply recessed nozzles; it does not rotate
   ORAN CÜMLESİ (lander ile aynı karedeyse, bloktan sonra): the
   lander is one-fifteenth of its length — this time the cathedral
   comes to the moth

CATCH BAY DETAY SÜRÜMÜ (S21 — tam bloğun ALT KÜMESİDİR, çelişen
kelime içermez): the open catch bay of the main ship — a 12-metre
hangar slot recessed in the satin steel-blue hexagonal truss spine,
7 metres wide and 5 metres deep, flanked by two machined yoke arms,
four open clamps along its rails, and four small WHITE frame lights
marking the corners of its mouth; its interior lit a warm
amber-white — the only warm-lit space in this cold blue world

LANDER — ÖLÜ SÜRÜM (Part A ile birebir aynı — S13 · S15 · S21): the
lander — the same 9-meter angular lifting-body craft in FLIGHT
CONFIGURATION, all four landing legs folded away, its belly line
clean, satin steel-blue with one thin SIGNAL-WHITE chevron line down
each flank, every thruster cold and every window dark — DEAD, the
only light on it the 40-cm beacon dome on its left shoulder line
pulsing warm amber once every 2 seconds

ARKADAN SÜRÜM (yüz görünmeyen kabin sahneleri — Part A S6/S9-S11 ile
aynı kural: tam karakter bloğunun alt kümesi, yüz satırları düşer,
suit satırları birebir kalır):
   PİLOT: the pilot, man, 1.83 m, matte cobalt-blue hard-shell suit
   with thin inlaid TEAL accent lines on the shoulder plates and
   forearms, low-profile cobalt-blue helmet CLOSED
   MÜHENDİS: the engineer, woman, 1.69 m, matte cobalt-blue
   hard-shell suit with thin inlaid AMBER accent lines on the
   shoulder plates and forearms, low-profile cobalt-blue helmet
   CLOSED

TAM KARAKTER BLOKLARI (S23 — yüzler görünür; Part A ile birebir aynı,
kask cümlesi yerine BARE-HEADED gelir):
   PILOT: the pilot — man, mid-forties, 1.83 m, broad-shouldered and
   lean, warm tan skin with visible pores, dark brown eyes, a broad
   nose once broken at the bridge, short black hair greying at the
   temples, a thin old scar on his left cheekbone; matte cobalt-blue
   hard-shell suit, dark graphite flex-weave joints, machined
   articulation rings, thin inlaid TEAL accent lines on the shoulder
   plates and forearms, finely scuffed with use
   ENGINEER: the engineer — woman, mid-thirties, 1.69 m, wiry, pale
   cool-toned skin with visible pores and faint freckles, grey-green
   eyes, a small notch scar splitting her left eyebrow, dark auburn
   hair in a near-shaved crop; same matte cobalt-blue hard-shell
   suit, dark graphite flex-weave joints, machined articulation
   rings, thin inlaid AMBER accent lines on the shoulder plates and
   forearms, finely scuffed with use

DOĞRULAMA (PART B blok sayımı): MAIN SHIP tam 8 (S17·S19·S20·S24) ·
CATCH BAY detay 2 (S21) · LANDER ölü 6 (S13·S15·S21) · PİLOT arkadan
10 (S14·S16·S17·S19·S20) + S18 kol/S22 · MÜHENDİS arkadan 10 + S18
kol/S22 · TAM karakter çifti 2 (S23) · D79 sırt kilidi insanlı 16
promptun 16'sında (vizör kilidi kasklı 14'ünde; S23 çiftinde yerine
KASKSIZ KİLİT).
```

---

# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART B: S13-S24)

---

## 🎬 SAHNE 13 (S13) — DÖNÜŞ SORUNU

> 🎯 **REFERANS:** **RA** p3 (ölü durum)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dead
spacecraft slowly rolling in orbit above a blue giant. Human count in
this frame: zero — both crew are inside the dead lander.

SCENE: Exterior, camera fixed in space 15 meters from the craft.
Center: the lander — the same 9-meter angular lifting-body craft in
FLIGHT CONFIGURATION, all four landing legs folded away, its belly
line clean, satin steel-blue with one thin SIGNAL-WHITE chevron line
down each flank, every thruster cold and every window dark — DEAD, the
only light on it the 40-cm beacon dome on its left shoulder line
pulsing warm amber once every 2 seconds. The craft is caught mid-roll,
canopy nose at screen-left, notched tail at screen-right, its long
hull tilted a few degrees off level — visibly turning, slowly. Behind
it, black space and hard sharp stars; below: the blue giant — a deep
sapphire gas giant banded with darker indigo latitude stripes, a faint
violet haze at its pole, its sunlit curve washing every shadow with a
soft blue albedo fill; its curve fills the lower third of the frame,
lifting the craft's shadow side out of pure black. Hard white sunlight
rims the upper chines from frame left.

CAMERA & LIGHT: 32mm spherical lens, fixed 15 meters away. Sources:
hard white sunlight from frame left, blue albedo fill from below, the
amber beacon pulse.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are inside the dead lander. The lander fires
nothing — no jet, no thruster, no engine light; it is dead except the
beacon. 0% bloom, no glow filter, no soft focus — the beacon is a
hard warm point, not a haze. The hull stays satin — never glossy. No
landing leg, no leg well, no open gear door visible. No readable text
anywhere. No subtitles, no title card, no watermark. Hull static — no
melting, no warping. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera in space, no camera movement. Human count in
this frame: zero — both crew are inside the dead lander. One
synthetic radio voice speaks; no human speaks.

SCENE: Exterior, camera fixed 15 meters from the craft, 32mm spherical
lens. Center: the lander — the same 9-meter angular lifting-body craft
in FLIGHT CONFIGURATION, all four landing legs folded away, its belly
line clean, satin steel-blue with one thin SIGNAL-WHITE chevron line
down each flank, every thruster cold and every window dark — DEAD, the
only light on it the 40-cm beacon dome on its left shoulder line
pulsing warm amber once every 2 seconds. Canopy nose at screen-left,
notched tail at screen-right. Behind it, hard sharp stars; below: the
blue giant — a deep sapphire gas giant banded with darker indigo
latitude stripes, a faint violet haze at its pole, its sunlit curve
washing every shadow with a soft blue albedo fill, lifting the shadow
side. Hard white sunlight rims the chines from frame left.

TIMELINE:
0.0s — The dead craft rolls slowly and steadily — 1 degree per
second, constant, no wobble. Beacon pulse. The star-field slides
behind it almost imperceptibly.
3.0s — A calm neutral synthetic voice over the radio, level, in
Turkish: "Saniyede bir derece dönüyorsunuz. Böyle kavrayamam."
6.0s — Pulse. The roll continues unchanged — the craft can do
nothing about it.
9.0s — Pulse. Silence. Hold on the slowly turning hull.

AUDIO: Hard vacuum silence outside; the synthetic line arrives as a
radio channel over the shot, thin and clear — heard only, never
shown as text. A soft click marks each beacon pulse on the channel.
No music.

PHYSICS: Ballistic drift, constant 1-degree-per-second roll, no
correction, no wobble. Beacon period exactly 2 seconds. Stars stay
sharp fixed points — no streaks, no trails.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside
the dead lander. The lander fires nothing — no jet, no thruster, no
engine light; dead except the beacon. 0% bloom, no glow filter, no
soft focus. The hull stays satin — never glossy. The spoken line is
heard only — no subtitles, no captions; the synthetic voice is
radio-only — no body, no avatar, no third figure. No landing leg
visible. No readable text anywhere. Hull static — no melting, no
warping. The background is identical in every frame — same planet,
same sky, same horizon, same ridges: nothing in it changes, appears or
disappears during the shot. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 14 (S14) — SON İTİCİ

> 🎯 **REFERANS:** **RD** p3 ⭐ (pirinç valf makro) · **RD** p2 · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dark
dead spacecraft cabin; a gloved hand on a brass valve lever. Exactly
2 human figures in frame, seen from behind — this film has exactly
two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back,
angled slightly down toward the center console. Left: the pilot, man,
1.83 m, matte cobalt-blue hard-shell suit with thin inlaid TEAL accent
lines on the shoulder plates and forearms, low-profile cobalt-blue
helmet CLOSED — leaning toward the console, his right glove closed
around a 30-cm BRASS VENT-VALVE LEVER set low between the seats, a
purely mechanical handle with a worn knurled grip. Right: the
engineer, woman, 1.69 m, matte cobalt-blue hard-shell suit with thin
inlaid AMBER accent lines on the shoulder plates and forearms,
low-profile cobalt-blue helmet CLOSED — her helmet turned toward the
12-cm mechanical pressure dial on the right panel: an unnumbered arc
scale with ten tick marks, phosphor face, needle high. The panel
around them is dead and dark; alive only: the pale backlight of the
12-cm mechanical attitude sphere — still slowly turning — the phosphor
dial, and the small amber repeater lamp mid-pulse. Through the canopy
above the console: black space, hard stars, the blue curve of the
giant low in the glass. COCKPIT: two high-backed machined seat shells
— thin TEAL piping down the left seat back, AMBER down the right — a
machined console spine between them, canted side consoles, a ribbed
overhead arch carrying six guarded toggles and two recessed teal strip
lights, and a three-pane wraparound canopy in machined graphite
frames. The overhead strips and the floor rim light are dark.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: sphere backlight, phosphor dial, amber pulse, faint
blue planet-light. The brass lever catches a dull warm edge from the
amber lamp.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. No readable text, letters or
digits anywhere — unnumbered dial, abstract segments. No subtitles, no
watermark. Hand contacts keep clear structural boundaries — no
merging, no extra fingers. No CGI aesthetic. Photorealistic with 35mm
film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One synthetic radio voice and one human
radio voice speak, one at a time; no mouth is ever visible.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens, angled slightly down toward the center console. Left
seat: the pilot, man, 1.83 m, matte cobalt-blue hard-shell suit with
thin inlaid TEAL accent lines on the shoulder plates and forearms,
low-profile cobalt-blue helmet CLOSED, its collar seal ring visible.
Right seat: the engineer, woman, 1.69 m, matte cobalt-blue hard-shell
suit with thin inlaid AMBER accent lines on the shoulder plates and
forearms, low-profile cobalt-blue helmet CLOSED, its collar seal ring
visible. Teal = pilot, amber = engineer — never identical, never
duplicated. Between the seats, low: a 30-cm BRASS VENT-VALVE LEVER,
purely mechanical, worn knurled grip. Right panel: the 12-cm
mechanical pressure dial, unnumbered arc scale, ten tick marks, needle
high. The dead panel's only lights: attitude sphere backlight — the
sphere still turning slowly — phosphor dial, amber repeater lamp
pulsing every 2 seconds. COCKPIT: two high-backed machined seat shells
— thin TEAL piping down the left seat back, AMBER down the right — a
machined console spine between them, canted side consoles, a ribbed
overhead arch carrying six guarded toggles and two recessed teal strip
lights, and a three-pane wraparound canopy in machined graphite
frames.

TIMELINE:
0.0s — Still, dark cabin; the amber pulse; the sphere turns slowly.
2.0s — A calm neutral synthetic voice through static, level, in
Turkish: "Havanız iticinizdir. Ben sayarım, sen çevir."
5.5s — The pilot's right glove reaches down and closes around the
brass lever — a deliberate, weighted grip, clear structural contact.
7.5s — The pilot's voice over the suit radio, quiet, in Turkish:
"Say."
9.0s — His glove holds the lever, ready. The engineer's helmet is
fixed on the dial. Hold.

AUDIO: Near-silent dead cabin: two slow breaths on the suit channel,
the soft click of each amber pulse, the two radio lines — one speaker
at a time, heard only, never shown as text. No music.

PHYSICS: Zero gravity — both bodies harnessed, seated posture,
movements deliberate and controlled; no free-floating limbs. The
attitude sphere turns at a constant slow rate — the roll continues.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. No readable text anywhere —
unnumbered dial only. The spoken lines are heard only — no subtitles,
no captions; one speaker at a time; the synthetic voice is radio-only
— no body, no avatar, no third figure. No mouth is readable in frame.
Hand contacts keep clear structural boundaries. Nothing fires in this
scene — no jet, no thruster. The background is identical in every
frame — same planet, same sky, same horizon, same ridges: nothing in
it changes, appears or disappears during the shot. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 15 (S15) — VİRAL #3: NEFES

> 🎯 **REFERANS:** **RA** p3 + p4 (vent port kıç detayda) — puf fiziği prompt metninden

> ⛔ ÜRETİM KAPISI 2 [D74 — kaydı PART_A sonuna]: 6 düz puf × 1.5 s,
> kristal, kıvrım yok. Tutmazsa GERİ ÇEKİLME (plan 🏭): puflar kadraj
> dışına alınır, despin duran küre + KERTE sesiyle anlatılır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dead
spacecraft flying on its own breath: a straight white plume of
freezing air against a blue giant. Human count in this frame: zero —
both crew are inside the dead lander.

SCENE: Exterior, camera fixed in space 12 meters from the craft.
Center: the lander — the same 9-meter angular lifting-body craft in
FLIGHT CONFIGURATION, all four landing legs folded away, its belly
line clean, satin steel-blue with one thin SIGNAL-WHITE chevron line
down each flank, every thruster cold and every window dark — DEAD, the
only light on it the 40-cm beacon dome on its left shoulder line
pulsing warm amber once every 2 seconds. Canopy nose at screen-left,
notched tail at screen-right, hull tilted mid-roll. From a small round
vent port on its near flank beside the side hatch, caught at full
length: ONE short straight plume of snow-white freezing air — cabin
air flashing to ice crystals in vacuum, a tight straight fan no longer
than 2 meters, angled against the hull's roll. No curl, no billow — a
straight, fast, thinning line of bright crystals. Behind the craft:
the blue giant — a deep sapphire gas giant banded with darker indigo
latitude stripes, a faint violet haze at its pole, its sunlit curve
washing every shadow with a soft blue albedo fill; its curve fills the
lower half of the frame; hard white sunlight rims the chines from
frame left; hard stars above.

CAMERA & LIGHT: 32mm spherical lens, fixed 12 meters away. Sources:
hard sunlight frame left, blue albedo fill from the giant, the amber
pulse; the plume's crystals catch the sunlight as bright points.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are inside the dead lander. The plume is
straight and short — no curling smoke, no billowing, no flame, no
fire, no engine light: it is freezing air, not exhaust; no thruster
fires anywhere. 0% bloom, no glow filter, no soft focus. The hull
stays satin — never glossy. No landing leg visible. No readable text
anywhere. No subtitles, no title card, no watermark. Crystals travel
in straight lines with constant momentum — never hovering, never
swirling. Hull static — no melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera in space, no camera movement. Human count in
this frame: zero — both crew are inside the dead lander. No one
speaks.

SCENE: Exterior, camera fixed 12 meters from the craft, 32mm spherical
lens. Center: the lander — the same 9-meter angular lifting-body craft
in FLIGHT CONFIGURATION, all four landing legs folded away, its belly
line clean, satin steel-blue with one thin SIGNAL-WHITE chevron line
down each flank, every thruster cold and every window dark — DEAD, the
only light on it the 40-cm beacon dome on its left shoulder line
pulsing warm amber once every 2 seconds. Canopy nose at screen-left,
notched tail at screen-right, rolling slowly. On its near flank beside
the side hatch: a small round vent port. Behind: the blue giant — a
deep sapphire gas giant banded with darker indigo latitude stripes, a
faint violet haze at its pole, its sunlit curve washing every shadow
with a soft blue albedo fill; its curve fills the lower half of frame;
hard sunlight rims the chines from frame left; hard stars above.

TIMELINE (six breaths):
0.5s — First puff: a short straight fan of snow-white ice crystals
fires from the vent port, 1.5 seconds long, angled against the roll —
straight, tight, thinning to nothing. The hull's slow roll eases
slightly.
2.0s — Second puff. The beacon pulses through the crystal fan — amber
light through white ice.
3.5s — Third puff. The roll is visibly slower now.
5.0s — Fourth puff, shorter.
6.5s — Fifth puff, shorter still. The star-field behind the craft has
almost stopped sliding.
8.0s — Sixth and last puff — a breath's worth of crystals. The hull
settles: the roll is gone. The craft hangs still.
10.0s — Only the amber pulse. Hold on the stilled craft.

AUDIO: Hard vacuum silence — the puffs are perfectly silent outside
the hull. No voices, no music. Total quiet under total motion.

PHYSICS: Each puff is vented cabin air freezing instantly: a
straight, fast fan of ice crystals, 1.5 seconds, constant momentum,
dispersing in straight lines — no curl, no billow. Each puff slows
the constant roll a step; after the sixth the roll is exactly zero.
Beacon period exactly 2 seconds. Stars stay sharp points.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside
the dead lander. The puffs are freezing air, not exhaust — no flame,
no fire, no engine light, no thruster fires anywhere; between and
after the puffs the lander fires nothing. 0% bloom, no glow filter, no
soft focus. The hull stays satin — never glossy. Crystals move in
straight lines with continuous momentum — never hovering, never
swirling, never curling like smoke. No landing leg visible. No
readable text anywhere. No subtitles, no title card, no watermark.
Hull static — no melting, no warping. The background is identical in
every frame — same planet, same sky, same horizon, same ridges:
nothing in it changes, appears or disappears during the shot. No
Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film
grain. No speech, no voice, no radio chatter, no callout, no music, no
score — this scene is wordless. No unnamed prop: nothing appears in or
vanishes from a hand, and no clipboard, tablet, screen or tool exists
that this prompt does not name.
```

---

## 🎬 SAHNE 16 (S16) — BEDEL

> 🎯 **REFERANS:** **RD** p2 (duran küre · ibre — açı metinden: %40) · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dark
dead spacecraft cabin; the price of stillness on a phosphor dial.
Exactly 2 human figures in frame, seen from behind — this film has
exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back,
angled slightly toward the right panel. Left: the pilot, man, 1.83 m,
matte cobalt-blue hard-shell suit with thin inlaid TEAL accent lines
on the shoulder plates and forearms, low-profile cobalt-blue helmet
CLOSED — his right glove back on his knee, the brass lever below now
untouched. Right: the engineer, woman, 1.69 m, matte cobalt-blue
hard-shell suit with thin inlaid AMBER accent lines on the shoulder
plates and forearms, low-profile cobalt-blue helmet CLOSED — her
helmet toward the 12-cm mechanical pressure dial: unnumbered arc
scale, ten tick marks, phosphor face — the needle now resting at the
FOURTH tick from the bottom, the swept arc above it plainly empty. The
12-cm mechanical attitude sphere at panel center is STOPPED —
perfectly still for the first time since the failure. The amber
repeater lamp mid-pulse. Through the canopy: black space and hard
stars — motionless now — and the blue curve of the giant low in the
glass. COCKPIT: two high-backed machined seat shells — thin TEAL
piping down the left seat back, AMBER down the right — a machined
console spine between them, canted side consoles, a ribbed overhead
arch carrying six guarded toggles and two recessed teal strip lights,
and a three-pane wraparound canopy in machined graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: sphere backlight, phosphor dial, amber pulse, faint
blue planet-light. Dim, cold, absolutely still.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. No readable text, letters or
digits anywhere — the dial is unnumbered. Nothing fires — no jet, no
thruster; the lander fires nothing. No subtitles, no watermark. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One synthetic radio voice speaks; no
human speaks.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens. Left seat: the pilot, man, 1.83 m, matte cobalt-blue
hard-shell suit with thin inlaid TEAL accent lines on the shoulder
plates and forearms, low-profile cobalt-blue helmet CLOSED, its collar
seal ring visible. Right seat: the engineer, woman, 1.69 m, matte
cobalt-blue hard-shell suit with thin inlaid AMBER accent lines on the
shoulder plates and forearms, low-profile cobalt-blue helmet CLOSED,
its collar seal ring visible. Teal = pilot, amber = engineer — never
identical, never duplicated. Panel: the 12-cm attitude sphere STOPPED
dead still; the 12-cm pressure dial's needle at the fourth tick of its
unnumbered ten-tick arc; the amber repeater lamp pulsing every 2
seconds. Through the canopy: hard stars, perfectly motionless, and the
blue curve of the giant. COCKPIT: two high-backed machined seat shells
— thin TEAL piping down the left seat back, AMBER down the right — a
machined console spine between them, canted side consoles, a ribbed
overhead arch carrying six guarded toggles and two recessed teal strip
lights, and a three-pane wraparound canopy in machined graphite
frames.

TIMELINE:
0.0s — Absolute stillness. The sphere does not move. The stars do
not move. The amber lamp pulses.
3.0s — A calm neutral synthetic voice through faint static, level,
in Turkish: "Dönüş sıfır. Kabin yüzde kırk."
6.0s — Neither figure moves. The pilot's gloves rest on his knees.
The dial needle holds at the fourth tick.
9.0s — Pulse. Hold on the still cabin — the price paid, the work
done, nothing left to do.

AUDIO: Near-silence: two slow breaths on the suit channel, the soft
click of each amber pulse, the single static-washed synthetic line —
heard only, never shown as text. No music.

PHYSICS: Zero gravity, zero rotation — for the first time since the
failure nothing in the frame moves except breathing shoulders. Both
bodies harnessed, seated posture, no free-floating limbs.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. No readable text anywhere — the
dial is unnumbered. The spoken line is heard only — no subtitles, no
captions; the synthetic voice is radio-only — no body, no avatar, no
third figure. No mouth is readable in frame. Nothing fires — no jet,
no thruster; the lander fires nothing. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 17 (S17) — İPTAL

> 🎯 **REFERANS:** **RB** p1·p2 (gemi 200 m) · **RD** p1 · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Through a
dead spacecraft's windshield: a giant rescue ship, too fast, pulling
away. Exactly 2 human figures in frame, seen from behind — this film
has exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back;
the central canopy pane (1.4 × 0.5 m) dominates the frame. Through the
glass, dead ahead at 200 meters: the main ship — a 135-metre
INTERSTELLAR transfer vessel, fifteen times the lander's length, satin
steel-blue with sparse thin white position lines: a closed sensor dome
at the bow, six cylindrical habitat modules in three tandem pairs
wrapped in dark quilted insulation, a long open hexagonal truss spine
carrying an OPEN CATCH BAY at midships — a 12-metre hangar slot, 7
metres wide and 5 metres deep, flanked by two machined yoke arms, four
open clamps along its rails and four small WHITE frame lights marking
the corners of its mouth — two dark knife-edge radiator wings, and an
aft fusion drive block with four deeply recessed nozzles; it does not
rotate. The lander is one-fifteenth of its length — this time the
cathedral comes to the moth. The great hull is caught at the first
instant of its wave-off: two short straight cold-gas jets flare at its
flank, and its long axis is beginning to slide toward the UPPER LEFT
of the glass. In the foreground, from behind: left, the pilot, man,
1.83 m, matte cobalt-blue hard-shell suit with thin inlaid TEAL accent
lines on the shoulder plates and forearms, low-profile cobalt-blue
helmet CLOSED; right, the engineer, woman, 1.69 m, matte cobalt-blue
hard-shell suit with thin inlaid AMBER accent lines on the shoulder
plates and forearms, low-profile cobalt-blue helmet CLOSED, its collar
seal ring visible. The dead panel below the glass: stopped attitude
sphere, phosphor dial, amber repeater lamp mid-pulse. COCKPIT: two
high-backed machined seat shells — thin TEAL piping down the left seat
back, AMBER down the right — a machined console spine between them,
canted side consoles, a ribbed overhead arch carrying six guarded
toggles and two recessed teal strip lights, and a three-pane
wraparound canopy in machined graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: hard sunlight rimming the distant ship, blue albedo
fill from the giant below the glass, sphere backlight, phosphor dial,
amber pulse.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. The lander fires nothing — no
jet, no thruster on the near craft; the only jets are the distant
ship's two short straight wave-off puffs. No readable text anywhere.
No subtitles, no watermark. No CGI aesthetic. Photorealistic with 35mm
film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One synthetic radio voice and one human
radio voice speak, one at a time; no mouth is ever visible.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens; the 1.4 × 0.5 m central canopy pane dominates the
frame. Through the glass, dead ahead at 200 meters: the main ship — a
135-metre INTERSTELLAR transfer vessel, fifteen times the lander's
length, satin steel-blue with sparse thin white position lines: a
closed sensor dome at the bow, six cylindrical habitat modules in
three tandem pairs wrapped in dark quilted insulation, a long open
hexagonal truss spine carrying an OPEN CATCH BAY at midships — a
12-metre hangar slot, 7 metres wide and 5 metres deep, flanked by two
machined yoke arms, four open clamps along its rails and four small
WHITE frame lights marking the corners of its mouth — two dark
knife-edge radiator wings, and an aft fusion drive block with four
deeply recessed nozzles; it does not rotate. The lander is
one-fifteenth of its length — this time the cathedral comes to the
moth. Foreground, from behind: left, the pilot, man, 1.83 m, matte
cobalt-blue hard-shell suit with thin inlaid TEAL accent lines,
low-profile cobalt-blue helmet CLOSED; right, the engineer, woman,
1.69 m, same suit with thin inlaid AMBER accent lines, low-profile
cobalt-blue helmet CLOSED, its collar seal ring visible. Teal = pilot,
amber = engineer — never identical. Dead panel: stopped sphere,
phosphor dial, amber lamp pulsing every 2 seconds. COCKPIT: two
high-backed machined seat shells — thin TEAL piping down the left seat
back, AMBER down the right — a machined console spine between them,
canted side consoles, a ribbed overhead arch carrying six guarded
toggles and two recessed teal strip lights, and a three-pane
wraparound canopy in machined graphite frames.

TIMELINE:
0.0s — The great ship fills the center of the glass, growing
slightly — too fast.
2.0s — A calm neutral synthetic voice through static, level, in
Turkish: "Kapanma hızlı. Iraksıyorum. Bir yörünge daha."
4.5s — Two short straight cold-gas jets flare at the ship's flank;
its long axis begins to slide smoothly toward the UPPER LEFT of the
glass, shrinking as it goes.
7.0s — The pilot's voice over the suit radio, flat and quiet, in
Turkish: "Bekleriz."
9.0s — The ship is a shrinking shape in the upper-left of the glass.
Neither figure has moved. The amber lamp pulses. Hold.

AUDIO: Near-silence: two slow breaths, the amber pulse clicks, the
two radio lines — one speaker at a time, heard only, never shown as
text. No music.

PHYSICS: Zero gravity, zero rotation on the lander — it fires nothing
and holds perfectly still; all relative motion in the glass belongs
to the SHIP. The ship's jets are short straight cold-gas puffs that
thin to nothing within a second. Stars stay sharp points.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. The lander fires nothing — no jet,
no thruster on the near craft. The spoken lines are heard only — no
subtitles, no captions; one speaker at a time; the synthetic voice is
radio-only — no body, no avatar, no third figure. No mouth is readable
in frame. No readable text anywhere. The background is identical in
every frame — same planet, same sky, same horizon, same ridges:
nothing in it changes, appears or disappears during the shot. No CGI
aesthetic. Photorealistic with 35mm film grain. Beyond the stated line
there is no other voice, no background chatter, no music, no score. No
unnamed prop: nothing appears in or vanishes from a hand, and no
clipboard, tablet, screen or tool exists that this prompt does not
name.
```

---

## 🎬 SAHNE 18 (S18) — BEKLEYİŞ

> 🎯 **REFERANS:** **RD** p2·p3 (konsol + valf) · **RE** (yalnız kol/eldiven)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close on a
dead spacecraft's center console: two gloved hands side by side,
doing nothing. Exactly 2 human figures present, visible only as their
forearms and gloves — this film has exactly two humans total.

SCENE: 85mm close view, camera fixed 0.8 meters above the center
console, looking down at a shallow angle. On the dark console rest two
gloved hands, side by side, not touching, perfectly still: the left
glove and forearm carry thin inlaid TEAL accent lines — the pilot,
man, 1.83 m, matte cobalt-blue hard-shell suit; the right glove and
forearm carry thin inlaid AMBER accent lines — the engineer, woman,
1.69 m, same matte cobalt-blue hard-shell suit. Machined articulation
rings at both wrists, finely scuffed with use. Between and beyond the
gloves: the brass vent-valve lever, untouched; the stopped attitude
sphere's pale backlight; the small amber repeater lamp caught
mid-pulse, its warm light lying across both gloves. At the top of the
frame, the lower edge of the canopy: through it a sliver of the blue
giant — a deep sapphire gas giant banded with darker indigo latitude
stripes, a faint violet haze at its pole, its sunlit curve washing
every shadow with a soft blue albedo fill — and across that sliver
runs its TERMINATOR, the soft edge between its lit and dark side,
where earlier the glass held only sunlit blue: the orbit has moved on.
COCKPIT: two high-backed machined seat shells — thin TEAL piping down
the left seat back, AMBER down the right — a machined console spine
between them, canted side consoles, a ribbed overhead arch carrying
six guarded toggles and two recessed teal strip lights, and a
three-pane wraparound canopy in machined graphite frames.

CAMERA & LIGHT: 85mm spherical lens, fixed 0.8 meters from the
console. Sources: amber pulse (warm, periodic), sphere backlight,
faint blue planet-light through the glass sliver.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures present,
visible only as forearms and gloves — no faces, no third hand, no
extra fingers, no duplicates. Teal lines = pilot, amber lines =
engineer — never identical. 0% bloom, no soft focus — the amber lamp
is a hard point, not a haze. No readable text anywhere. No subtitles,
no watermark. Glove-console contact keeps a clear structural boundary
— no merging. Nothing fires — the lander fires nothing. No CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera above the center console, no camera movement.
Exactly 2 human figures present, visible only as their forearms and
gloves — this film has exactly two humans total. No one speaks.

SCENE: 85mm spherical lens, fixed 0.8 meters above the dark center
console, shallow downward angle. Two gloved hands rest side by side on
the console, not touching, perfectly still: left glove and forearm
with thin inlaid TEAL accent lines — the pilot, man, matte cobalt-blue
hard-shell suit; right glove and forearm with thin inlaid AMBER accent
lines — the engineer, woman, same matte cobalt-blue hard-shell suit.
Machined articulation rings at both wrists, finely scuffed. Beyond
them: the untouched brass vent-valve lever, the stopped attitude
sphere's pale backlight, the amber repeater lamp. At the top of frame,
a sliver of windshield: a sliver of the blue giant — a deep sapphire
gas giant banded with darker indigo latitude stripes, a faint violet
haze at its pole, its sunlit curve washing every shadow with a soft
blue albedo fill, its terminator line crossing the glass — the orbit
moving on, one slow proof of passing time. COCKPIT: two high-backed
machined seat shells — thin TEAL piping down the left seat back, AMBER
down the right — a machined console spine between them, canted side
consoles, a ribbed overhead arch carrying six guarded toggles and two
recessed teal strip lights, and a three-pane wraparound canopy in
machined graphite frames.

TIMELINE:
0.0s — Stillness. The amber lamp pulses; its warm wash slides over
both gloves and dies.
2.0s — Pulse. Neither hand moves.
4.0s — Pulse. The engineer's fingers flex once — a small, controlled
motion — and settle again.
6.0s — Pulse. In the canopy sliver, the terminator's soft edge
has crept almost imperceptibly.
8.0s — Pulse. Two still hands, side by side, waiting.
10.0s — Pulse, and hold. Doing nothing is the work.

AUDIO: The quietest scene in the film: two slow breaths on the suit
channel, the soft click of each amber pulse — nothing else. The radio
carrier hiss runs continuous and unbroken under it. No voices, no
music.

PHYSICS: Zero gravity, zero rotation. Hands rest with deliberate
placement — harnessed bodies off-frame hold them steady; no drifting,
no floating. Amber pulse period exactly 2 seconds.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures present, visible only as
forearms and gloves — no faces, no third hand, no extra fingers, no
duplicates. 0% bloom, no soft focus — the amber lamp is a hard point.
No readable text anywhere. No subtitles, no captions, no watermark.
Glove-console contact keeps a clear structural boundary — no merging.
Nothing fires — no jet, no thruster; the lander fires nothing. No CGI
aesthetic. Photorealistic with 35mm film grain. No speech, no voice,
no radio chatter, no callout, no music, no score — this scene is
wordless. No unnamed prop: nothing appears in or vanishes from a hand,
and no clipboard, tablet, screen or tool exists that this prompt does
not name.
```

---

## 🎬 SAHNE 19 (S19) — İKİNCİ KESİŞİM

> 🎯 **REFERANS:** **RB** p3 · **RC** p1 (açık ağız dead-on) · **RD** p1 · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Through a
dead spacecraft's windshield: the rescue ship returns, its catch bay
open and facing us. Exactly 2 human figures in frame, seen from
behind — this film has exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back;
the central canopy pane (1.4 × 0.5 m) dominates the frame. Through the
glass, returning from the upper left and now near center at 200
meters: the main ship — a 135-metre INTERSTELLAR transfer vessel,
fifteen times the lander's length, satin steel-blue with sparse thin
white position lines: a closed sensor dome at the bow, six cylindrical
habitat modules in three tandem pairs wrapped in dark quilted
insulation, a long open hexagonal truss spine carrying an OPEN CATCH
BAY at midships — a 12-metre hangar slot, 7 metres wide and 5 metres
deep, flanked by two machined yoke arms, four open clamps along its
rails and four small WHITE frame lights marking the corners of its
mouth — two dark knife-edge radiator wings, and an aft fusion drive
block with four deeply recessed nozzles; it does not rotate. The
lander is one-fifteenth of its length — this time the cathedral comes
to the moth. This time the ship is oriented with its open catch bay
FACING the camera: the four white corner lights read as a perfect
rectangle, a warm amber-white light spilling faintly from the bay's
interior — the only warm-lit space in the cold blue frame. Foreground,
from behind: left, the pilot, man, 1.83 m, matte cobalt-blue
hard-shell suit with thin inlaid TEAL accent lines on the shoulder
plates and forearms, low-profile cobalt-blue helmet CLOSED; right, the
engineer, woman, 1.69 m, same suit with thin inlaid AMBER accent
lines, low-profile cobalt-blue helmet CLOSED — her glove lifted,
pointing at the glass. Dead panel below: stopped sphere, phosphor
dial, amber repeater lamp. COCKPIT: two high-backed machined seat
shells — thin TEAL piping down the left seat back, AMBER down the
right — a machined console spine between them, canted side consoles, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy in machined
graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: hard sunlight rimming the ship, warm bay light in its
mouth, blue albedo fill, sphere backlight, amber pulse.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. The lander fires nothing — no
jet, no thruster on the near craft. No readable text anywhere. No
subtitles, no watermark. No CGI aesthetic. Photorealistic with 35mm
film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One human radio voice speaks; nothing
else.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens; the 1.4 × 0.5 m central canopy pane dominates the
frame. Through the glass at 200 meters, centered: the main ship — a
135-metre INTERSTELLAR transfer vessel, fifteen times the lander's
length, satin steel-blue with sparse thin white position lines: a
closed sensor dome at the bow, six cylindrical habitat modules in
three tandem pairs wrapped in dark quilted insulation, a long open
hexagonal truss spine carrying an OPEN CATCH BAY at midships — a
12-metre hangar slot, 7 metres wide and 5 metres deep, flanked by two
machined yoke arms, four open clamps along its rails and four small
WHITE frame lights marking the corners of its mouth — two dark
knife-edge radiator wings, and an aft fusion drive block with four
deeply recessed nozzles; it does not rotate. The lander is
one-fifteenth of its length — this time the cathedral comes to the
moth. Its open catch bay FACES the camera: four white corner lights in
a perfect rectangle, warm amber-white light in its mouth. Foreground,
from behind: left, the pilot, man, 1.83 m, matte cobalt-blue
hard-shell suit with thin inlaid TEAL accent lines, low-profile
cobalt-blue helmet CLOSED; right, the engineer, woman, 1.69 m, same
suit with thin inlaid AMBER accent lines, low-profile cobalt-blue
helmet CLOSED, its collar seal ring visible. Teal = pilot, amber =
engineer — never identical. Dead panel: stopped sphere, phosphor dial,
amber lamp pulsing every 2 seconds. COCKPIT: two high-backed machined
seat shells — thin TEAL piping down the left seat back, AMBER down the
right — a machined console spine between them, canted side consoles, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy in machined
graphite frames.

TIMELINE:
0.0s — The ship hangs centered in the glass, growing very slowly,
bay-first — patient this time.
3.0s — The engineer's glove lifts and points at the glass, at the
rectangle of four white lights.
5.0s — Her voice over the suit radio, quiet, in Turkish: "İşte
orada. Ağzı açık."
7.5s — The pilot's helmet nods once, slowly. His hands stay on his
knees.
9.5s — The bay's warm mouth grows a fraction. The amber lamp pulses.
Hold.

AUDIO: Near-silence: two slow breaths, the amber pulse clicks, her
single quiet line — heard only, never shown as text. No music.

PHYSICS: Zero gravity, zero rotation on the lander — it fires nothing
and holds still; all relative motion belongs to the ship, closing
slowly and centered. Stars stay sharp points.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. The lander fires nothing — no jet,
no thruster on the near craft. The spoken line is heard only — no
subtitles, no captions. No mouth is readable in frame. No readable
text anywhere. The background is identical in every frame — same
planet, same sky, same horizon, same ridges: nothing in it changes,
appears or disappears during the shot. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 20 (S20) — ÖLÜ SÜZÜLME: TERSİ

> 🎯 **REFERANS:** **RB** p3 (60 m dolduran gövde) · **RC** p1 · **RD** p1 · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Through a
dead spacecraft's windshield: the giant rescue ship at sixty meters,
its own engines dark, coming on in silence. Exactly 2 human figures
in frame, seen from behind — this film has exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back;
the central canopy pane (1.4 × 0.5 m) dominates the frame. Through the
glass the main ship now FILLS most of the view at 60 meters: the main
ship — a 135-metre INTERSTELLAR transfer vessel, fifteen times the
lander's length, satin steel-blue with sparse thin white position
lines: a closed sensor dome at the bow, six cylindrical habitat
modules in three tandem pairs wrapped in dark quilted insulation, a
long open hexagonal truss spine carrying an OPEN CATCH BAY at midships
— a 12-metre hangar slot, 7 metres wide and 5 metres deep, flanked by
two machined yoke arms, four open clamps along its rails and four
small WHITE frame lights marking the corners of its mouth — two dark
knife-edge radiator wings, and an aft fusion drive block with four
deeply recessed nozzles; it does not rotate. The lander is
one-fifteenth of its length — this time the cathedral comes to the
moth. The open bay is centered in the glass, its warm amber-white
mouth wide, the truss detail sharp — and EVERY thruster on the great
hull is dark: caught the instant after its final braking puff, it
comes on dead-drifting. Foreground, from behind: left, the pilot, man,
1.83 m, matte cobalt-blue hard-shell suit with thin inlaid TEAL accent
lines on the shoulder plates and forearms, low-profile cobalt-blue
helmet CLOSED; right, the engineer, woman, 1.69 m, same suit with thin
inlaid AMBER accent lines, low-profile cobalt-blue helmet CLOSED, its
collar seal ring visible. Dead panel below: stopped sphere, phosphor
dial, amber repeater lamp mid-pulse. COCKPIT: two high-backed machined
seat shells — thin TEAL piping down the left seat back, AMBER down the
right — a machined console spine between them, canted side consoles, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy in machined
graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: hard sunlight rimming the great hull, warm bay light,
blue albedo fill, sphere backlight, amber pulse.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. NOTHING fires on either craft
— no engine, no thruster, no jet: both hulls dead-drift. No readable
text anywhere. No subtitles, no watermark. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One synthetic radio voice speaks; no
human speaks.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens; the 1.4 × 0.5 m central canopy pane dominates the
frame. Through the glass at 60 meters, filling most of the view: the
main ship — a 135-metre INTERSTELLAR transfer vessel, fifteen times
the lander's length, satin steel-blue with sparse thin white position
lines: a closed sensor dome at the bow, six cylindrical habitat
modules in three tandem pairs wrapped in dark quilted insulation, a
long open hexagonal truss spine carrying an OPEN CATCH BAY at midships
— a 12-metre hangar slot, 7 metres wide and 5 metres deep, flanked by
two machined yoke arms, four open clamps along its rails and four
small WHITE frame lights marking the corners of its mouth — two dark
knife-edge radiator wings, and an aft fusion drive block with four
deeply recessed nozzles; it does not rotate. The lander is
one-fifteenth of its length — this time the cathedral comes to the
moth. Its open bay is centered, warm-mouthed, dead ahead. Foreground,
from behind: left, the pilot, man, 1.83 m, matte cobalt-blue
hard-shell suit with thin inlaid TEAL accent lines, low-profile
cobalt-blue helmet CLOSED; right, the engineer, woman, 1.69 m, same
suit with thin inlaid AMBER accent lines, low-profile cobalt-blue
helmet CLOSED, its collar seal ring visible. Teal = pilot, amber =
engineer — never identical. Dead panel: stopped sphere, phosphor dial,
amber lamp pulsing every 2 seconds. COCKPIT: two high-backed machined
seat shells — thin TEAL piping down the left seat back, AMBER down the
right — a machined console spine between them, canted side consoles, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy in machined
graphite frames.

TIMELINE:
0.0s — On the ship's flank, one last SHORT straight cold-gas puff —
the final braking burn, thinning to nothing within a second.
2.0s — A calm neutral synthetic voice through faint static, level,
in Turkish: "Altmış metre. Motorlarım kapalı. Geliyorum."
3.0s — From this moment NOTHING fires on either craft. The great
hull grows in the glass in absolute silence — 0.3 meters per second,
patient as a tide.
6.5s — The bay's warm rectangle widens; truss shadows sharpen.
Neither figure moves.
9.5s — The ship's structure reaches the edges of the glass. The
amber lamp pulses. Hold.

AUDIO: Near-silence: two slow breaths, the amber pulse clicks, the
single static-washed synthetic line — heard only, never shown as
text. No music — only the radio carrier hiss, continuous.

PHYSICS: Zero gravity, zero rotation on the lander; the ship closes
at a constant 0.3 m/s after its final puff and fires nothing more.
Constant closing rate — no acceleration, no jerk. Stars stay sharp
points.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. After 3.0s nothing fires on either
craft — no engine, no thruster, no jet. The spoken line is heard only
— no subtitles, no captions; the synthetic voice is radio-only — no
body, no avatar, no third figure. No mouth is readable in frame. No
readable text anywhere. The background is identical in every frame —
same planet, same sky, same horizon, same ridges: nothing in it
changes, appears or disappears during the shot. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 21 (S21) — YAKALAYIŞ (DORUK · hangar İÇİNDEN)

> 🎯 **REFERANS:** **RC** p3 ⭐ (hangar içi kadraj — birebir) · **RC** p1 · **RA** p3

> ⛔ ÜRETİM KAPISI 1 [D74 — kaydı PART_A sonuna]: filmin en ağır
> geometrisi — ölü araç + gölge geçişi + nicelik (2 kol · 4 kelepçe ·
> 4 çerçeve ışığı · pay 1.5 m) + mavi-üstü-mavi testi. Araç DEAD
> NOSE-ON girer (Black Cradle tail-on'unun aynadaki tersi).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. From
inside a great ship's open hangar bay: a dead spacecraft drifting in,
nose first, crossing from cold blue into warm light. Human count in
this frame: zero — both crew are inside the dead lander.

SCENE: Camera fixed inside the catch bay, mounted low on its rear
wall, looking straight out through the open mouth. Framing the view:
the open catch bay of the main ship — a 12-metre hangar slot recessed
in the satin steel-blue hexagonal truss spine, 7 metres wide and 5
metres deep, flanked by two machined yoke arms, four open clamps along
its rails, and four small WHITE frame lights marking the corners of
its mouth; its interior lit a warm amber-white — the only warm-lit
space in this cold blue world. Beyond the mouth: black space, hard
stars, and the blue giant — a deep sapphire gas giant banded with
darker indigo latitude stripes, a faint violet haze at its pole, its
sunlit curve washing every shadow with a soft blue albedo fill, its
curve filling the lower third of the opening. Centered in the mouth,
already halfway across the threshold, DEAD NOSE-ON with its canopy
nose pointing straight at the camera: the lander — the same 9-meter
angular lifting-body craft in FLIGHT CONFIGURATION, all four landing
legs folded away, its belly line clean, satin steel-blue with one thin
SIGNAL-WHITE chevron line down each flank, every thruster cold and
every window dark — DEAD, the only light on it the 40-cm beacon dome
on its left shoulder line pulsing warm amber once every 2 seconds. The
bay's shadow line lies across its hull mid-length: the forward half
already in warm amber-white bay light, the aft half still rimmed in
cold blue planetshine — one hull, two worlds. The clearance to the
yoke arms on either side reads plainly: 1.5 meters of margin.

CAMERA & LIGHT: 32mm spherical lens, fixed low on the bay's rear
wall. Sources: warm amber-white bay interior light, cold blue albedo
fill and hard sunlight beyond the mouth, the amber beacon pulse.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are inside the dead lander. NOTHING fires on
either craft — no engine, no thruster, no jet; the lander is dead
except the beacon. 0% bloom, no glow filter, no soft focus. Exactly
two yoke arms, exactly four clamps, exactly four white corner lights
— no extra structure. The hulls stay satin — never glossy. No landing
leg visible. No readable text anywhere. No subtitles, no title card,
no watermark. Hulls static — no melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the hangar bay, no camera movement.
Human count in this frame: zero — both crew are inside the dead
lander. One synthetic radio voice speaks two words; no human speaks.

SCENE: Camera fixed low on the rear wall of the catch bay, looking
straight out through the open mouth, 32mm spherical lens. The frame:
the open catch bay of the main ship — a 12-metre hangar slot recessed
in the satin steel-blue hexagonal truss spine, 7 metres wide and 5
metres deep, flanked by two machined yoke arms, four open clamps along
its rails, and four small WHITE frame lights marking the corners of
its mouth; its interior lit a warm amber-white — the only warm-lit
space in this cold blue world. Beyond the mouth: black space, hard
stars, the blue giant — a deep sapphire gas giant banded with darker
indigo latitude stripes, a faint violet haze at its pole, its sunlit
curve washing every shadow with a soft blue albedo fill, its curve low
in the opening. Approaching the mouth DEAD NOSE-ON, canopy nose
pointing straight at the camera: the lander — the same 9-meter angular
lifting-body craft in FLIGHT CONFIGURATION, all four landing legs
folded away, its belly line clean, satin steel-blue with one thin
SIGNAL-WHITE chevron line down each flank, every thruster cold and
every window dark — DEAD, the only light on it the 40-cm beacon dome
on its left shoulder line pulsing warm amber once every 2 seconds.

TIMELINE:
0.0s — The dead craft hangs centered in the mouth, growing at 0.3
meters per second — a slow, inevitable arrival. Beacon pulse.
2.5s — Its canopy nose crosses the threshold; the bay's warm light
climbs the nose while the tail stays rimmed in cold blue — the
shadow line slides slowly aft along the hull.
5.0s — The hull fills the mouth, 1.5 meters of clearance to each
yoke arm. Beacon pulse — warm amber inside warm light now.
7.0s — The two machined yoke arms swing inward together and CLOSE
around the hull rails with a firm, singular seating — one clean
mechanical grip, no bounce.
8.5s — A calm neutral synthetic voice, close and clear now, in
Turkish: "Tuttum."
10.0s — The dead craft rests in the arms, fully in warm light, the
cold blue world framed small beyond its tail. Hold.

AUDIO: Hard vacuum silence outside — the arms' closing is FELT as a
deep structural transmission through the camera mount, not heard as
open sound. Then the close synthetic word on the closed comms channel
— carrier hiss only — heard only, never shown as text. No music.

PHYSICS: Constant 0.3 m/s closure, zero rotation on both hulls,
nothing firing anywhere. The yoke arms close at one steady rate and
seat without rebound. Clearance to each arm: 1.5 meters. Beacon
period exactly 2 seconds throughout.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside
the dead lander. NOTHING fires on either craft — no engine, no
thruster, no jet, no sparks; the capture is silent and mechanical.
Exactly two yoke arms, exactly four clamps, exactly four white corner
lights — no extra structure appears. 0% bloom, no glow filter, no soft
focus. The hulls stay satin — never glossy. No landing leg visible.
The spoken word is heard only — no subtitles, no captions; the
synthetic voice is radio-only — no body, no avatar, no third figure.
No readable text anywhere. Hulls static — no melting, no warping. The
background is identical in every frame — same planet, same sky, same
horizon, same ridges: nothing in it changes, appears or disappears
during the shot. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 22 (S22) — NEFESİN DÖNÜŞÜ

> 🎯 **REFERANS:** **RD** p2 (yükselen ibre — açı metinden) · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dead
spacecraft cabin waking into warm light; a pressure needle beginning
to climb. Exactly 2 human figures in frame, seen from behind — this
film has exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back.
Left: the pilot, man, 1.83 m, matte cobalt-blue hard-shell suit with
thin inlaid TEAL accent lines on the shoulder plates and forearms,
low-profile cobalt-blue helmet CLOSED — his helmet bowed slightly
forward. Right: the engineer, woman, 1.69 m, matte cobalt-blue
hard-shell suit with thin inlaid AMBER accent lines on the shoulder
plates and forearms, low-profile cobalt-blue helmet CLOSED — her
helmet turned toward the 12-cm mechanical pressure dial: unnumbered
arc scale, ten tick marks, phosphor face — the needle caught just
ABOVE the fourth tick, on its way up. The stopped attitude sphere
holds still; the amber repeater lamp mid-pulse. Through the canopy: no
more stars — the warm amber-white interior of the hangar bay fills the
glass, the machined face of a yoke arm crossing its upper corner. Warm
light lies across the dead panel for the first time in the film.
COCKPIT: two high-backed machined seat shells — thin TEAL piping down
the left seat back, AMBER down the right — a machined console spine
between them, canted side consoles, a ribbed overhead arch carrying
six guarded toggles and two recessed teal strip lights, and a
three-pane wraparound canopy in machined graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: warm bay light through the glass (dominant, new),
phosphor dial, amber pulse.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. No readable text anywhere —
the dial is unnumbered. Nothing fires — no jet, no thruster on either
craft. No subtitles, no watermark. No CGI aesthetic. Photorealistic
with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the cabin, no camera movement. Exactly
2 human figures in frame, both seen from behind — this film has
exactly two humans total. One human whisper on the radio; nothing
else.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens. Left seat: the pilot, man, 1.83 m, matte cobalt-blue
hard-shell suit with thin inlaid TEAL accent lines on the shoulder
plates and forearms, low-profile cobalt-blue helmet CLOSED, its collar
seal ring visible. Right seat: the engineer, woman, 1.69 m, matte
cobalt-blue hard-shell suit with thin inlaid AMBER accent lines on the
shoulder plates and forearms, low-profile cobalt-blue helmet CLOSED,
its collar seal ring visible. Teal = pilot, amber = engineer — never
identical, never duplicated. Panel: stopped attitude sphere; the 12-cm
pressure dial, unnumbered ten-tick arc, needle at the fourth tick;
amber repeater lamp pulsing every 2 seconds. Through the canopy: the
warm amber-white hangar interior, a machined yoke arm crossing the
upper corner of the glass. COCKPIT: two high-backed machined seat
shells — thin TEAL piping down the left seat back, AMBER down the
right — a machined console spine between them, canted side consoles, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy in machined
graphite frames.

TIMELINE:
0.0s — Four deep, evenly spaced structural THUDS carry through the
hull — one, two, three, four — the clamps seating, felt more than
heard.
3.0s — A low, rising hiss begins: the bay pressurizing around them.
Warm light strengthens through the glass.
5.0s — The pressure dial's needle stirs, then begins to climb slowly
and steadily off the fourth tick — the air they spent, coming back.
7.5s — The pilot's whisper over the suit radio, head bowed slightly
forward, in Turkish: "Nefes al."
10.0s — The needle is still climbing. The amber lamp pulses. Hold.

AUDIO: Four deep clamp thuds through the structure; the long soft
pressurization hiss rising under everything; two slow breaths; the
whispered line — heard only, never shown as text. The radio carrier
runs unbroken. No music until the last second: one warm, quiet major
chord begins under the hiss.

PHYSICS: Zero gravity still inside the cabin; bodies harnessed,
seated. The needle climbs at one slow steady rate. Nothing fires.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable; the whisper is radio audio — no mouth is readable in frame,
the bowed helmet physically hides the jaw. 0% bloom, no soft focus. No
readable text anywhere. The whispered line is heard only — no
subtitles, no captions. Nothing fires — no jet, no thruster on either
craft. The background is identical in every frame — same planet, same
sky, same horizon, same ridges: nothing in it changes, appears or
disappears during the shot. No CGI aesthetic. Photorealistic with 35mm
film grain. Beyond the stated line there is no other voice, no
background chatter, no music, no score. No unnamed prop: nothing
appears in or vanishes from a hand, and no clipboard, tablet, screen
or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 23 (S23) — İLK YÜZLER

> 🎯 **REFERANS:** **RE** p4 ⭐ (iki yüz) + p1·p2 — kasksızlık sahne kilidinden, referans YÜZ içindir

> [D69] Sahne GİRİŞ değil — mekânın İÇİNDE başlar; ışık loş değil
> sıcak ve yönlü; arka planda figür yeri yok (raf duvarı).
> Kasksız TEK sahne — tam karakter blokları + BARE-HEADED.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A warm
pressurized hangar deck; two travelers bare-headed for the first
time. Exactly 2 human figures in frame — this film has exactly two
humans total.

SCENE: Inside the main ship's pressurized hangar deck — a clean,
warm-lit compartment walled with equipment racks; no doorway, no
corridor, no other figures possible. Standing at a rack, facing
three-quarters to camera, BARE-HEADED: the pilot — man, mid-forties,
1.83 m, broad-shouldered and lean, warm tan skin with visible pores,
dark brown eyes, a broad nose once broken at the bridge, short black
hair greying at the temples, a thin old scar on his left cheekbone;
matte cobalt-blue hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use. Beside him,
BARE-HEADED: the engineer — woman, mid-thirties, 1.69 m, wiry, pale
cool-toned skin with visible pores and faint freckles, grey-green
eyes, a small notch scar splitting her left eyebrow, dark auburn hair
in a near-shaved crop; same matte cobalt-blue hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
AMBER accent lines on the shoulder plates and forearms, finely
scuffed with use. Their two cobalt-blue helmets rest side by side on
the rack shelf, visors forward, plainly visible. Between them, seated
in a wall berth: the slim sample case, lid open — inside, the 40-cm
core of milky blue-white nitrogen ice, its thin darker bands catching
the warm light. Both faces are tired, calm, lit warm and directional
from a single overhead strip.

CAMERA & LIGHT: 35mm spherical lens, fixed 3 meters away at chest
height. Single warm directional overhead strip; soft racks shadow;
the first warm-lit human skin in the film.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures; the rack wall leaves no
room for anyone. Both are fully BARE-HEADED — no helmet worn, no
half-worn helmet, no open visor; the two helmets sit on the rack.
Teal lines = pilot, amber lines = engineer — never identical. The
suits have NO back-mounted unit — both back silhouettes are flat. 0%
bloom, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture, no face morphing. No readable text
anywhere. No subtitles, no watermark. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera on the hangar deck, no camera movement.
Exactly 2 human figures in frame — this film has exactly two humans
total. Not one word is spoken.

CHARACTERS (both BARE-HEADED): The pilot — man, mid-forties, 1.83 m,
broad-shouldered and lean, warm tan skin with visible pores, dark
brown eyes, a broad nose once broken at the bridge, short black hair
greying at the temples, a thin old scar on his left cheekbone; matte
cobalt-blue hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use. The engineer —
woman, mid-thirties, 1.69 m, wiry, pale cool-toned skin with visible
pores and faint freckles, grey-green eyes, a small notch scar
splitting her left eyebrow, dark auburn hair in a near-shaved crop;
same matte cobalt-blue hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines
on the shoulder plates and forearms, finely scuffed with use. Teal =
pilot, amber = engineer — never identical, never duplicated.

SCENE: The main ship's warm pressurized hangar deck, walled with
equipment racks — no doorway in frame, no room for other figures.
Their two cobalt-blue helmets rest side by side on a rack shelf. In a
wall berth between them: the open sample case with the 40-cm milky
blue-white ice core, thin darker bands in the warm light. Camera
fixed 3 meters away, 35mm spherical lens, chest height; single warm
directional overhead strip.

TIMELINE:
0.0s — The engineer stands at the berth, one bare hand resting on the
case's rim, looking down at the core — the thing they carried through
all of it.
3.0s — The pilot draws a long breath — his first shown breath of ship
air — shoulders rising and settling slowly.
5.5s — She looks up from the core to him. He looks back. No words.
8.0s — A small, tired nod from the pilot — barely a movement.
10.0s — Both still, faces warm-lit, helmets side by side on the
shelf. Hold.

AUDIO: Warm ship-tone: soft ventilation, a low deck hum, two people
breathing real air. NO radio filter anymore — open-air acoustics for
the first time. Not one word. The quiet major chord from the previous
scene resolves and fades.

PHYSICS: Ship's deck gravity feel — grounded stances, weighted arms,
ordinary Earth pace, real time.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures. Both are fully BARE-HEADED throughout — no
helmet worn, no half-worn helmet, no open visor; the two helmets stay
on the rack shelf. The suits have NO back-mounted unit — both back
silhouettes are flat. 0% bloom, no soft focus. Photorealistic skin
with pores — no airbrushing, no face morphing, identical bone
structure throughout. Not one word is spoken — no subtitles, no
captions. No readable text anywhere. The background is identical in
every frame — same planet, same sky, same horizon, same ridges:
nothing in it changes, appears or disappears during the shot. No CGI
aesthetic. Photorealistic with 35mm film grain. No speech, no voice,
no radio chatter, no callout, no music, no score — this scene is
wordless. No unnamed prop: nothing appears in or vanishes from a hand,
and no clipboard, tablet, screen or tool exists that this prompt does
not name.
```

---

## 🎬 SAHNE 24 (S24) — FİNAL: MANZARA

> 🎯 **REFERANS:** **RB** p1·p2 · **RC** p2 (kenetli) · **RA** p3

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A great
ship leaving a blue giant behind, a small craft asleep in its hangar
bay. Human count in this frame: zero — both crew are aboard the main
ship.

SCENE: Very wide exterior, camera fixed in space 300 meters away.
Crossing the frame: the main ship — a 135-metre INTERSTELLAR transfer
vessel, fifteen times the lander's length, satin steel-blue with
sparse thin white position lines: a closed sensor dome at the bow, six
cylindrical habitat modules in three tandem pairs wrapped in dark
quilted insulation, a long open hexagonal truss spine carrying an OPEN
CATCH BAY at midships — a 12-metre hangar slot, 7 metres wide and 5
metres deep, flanked by two machined yoke arms, four open clamps along
its rails and four small WHITE frame lights marking the corners of its
mouth — two dark knife-edge radiator wings, and an aft fusion drive
block with four deeply recessed nozzles; it does not rotate. Its bow
points toward the upper right of frame. In the bay at midships, held
in the closed yoke arms, the small steel-blue shape of the lander
rests in warm light — the moth home in its cathedral. The aft fusion
drive burns with a steady hard white light. Below and behind: the blue
giant — a deep sapphire gas giant banded with darker indigo latitude
stripes, a faint violet haze at its pole, its sunlit curve washing
every shadow with a soft blue albedo fill; its curve fills the lower
left of the frame, and before it hangs the frost moon as a thin blue
crescent — on its dark night side, a faint arc of blue-violet auroral
light crowns the zenith, distant and harmless now, just geography.
Hard stars everywhere else.

CAMERA & LIGHT: 32mm spherical lens, fixed 300 meters away. Sources:
hard white sunlight from frame left, the fusion drive's steady white
light, warm bay light at midships, soft blue planetshine on the
crescent.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are aboard the main ship. 0% bloom, no glow
filter, no soft focus — the drive light is hard and steady, no lens
flare. The hulls stay satin — never glossy. The distant aurora is
blue-violet only — never green. No readable text anywhere. No
subtitles, no title card, no watermark. Hulls static — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with
35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera in space, no camera movement. Human count in
this frame: zero — both crew are aboard the main ship.

SCENE: Very wide exterior, camera fixed 300 meters away, 32mm
spherical lens. Crossing the frame, bow toward the upper right: the
main ship — a 135-metre INTERSTELLAR transfer vessel, fifteen times
the lander's length, satin steel-blue with sparse thin white position
lines: a closed sensor dome at the bow, six cylindrical habitat
modules in three tandem pairs wrapped in dark quilted insulation, a
long open hexagonal truss spine carrying an OPEN CATCH BAY at midships
— a 12-metre hangar slot, 7 metres wide and 5 metres deep, flanked by
two machined yoke arms, four open clamps along its rails and four
small WHITE frame lights marking the corners of its mouth — two dark
knife-edge radiator wings, and an aft fusion drive block with four
deeply recessed nozzles; it does not rotate. In the warm bay at
midships, the small steel-blue lander rests in the closed yoke arms —
the moth home in its cathedral. Below and behind: the blue giant — a
deep sapphire gas giant banded with darker indigo latitude stripes, a
faint violet haze at its pole, its sunlit curve washing every shadow
with a soft blue albedo fill; its curve fills the lower left; before
it, the frost moon as a thin blue crescent, a faint blue-violet
auroral arc crowning its dark side — just geography now. Hard stars.

TIMELINE:
0.0s — The fusion drive burns steady hard white; the ship slides very
slowly toward the upper right, shrinking by degrees.
3.0s — The warm point of the bay and its small sleeping cargo catch
the sun once as the angle shifts.
6.0s — The crescent moon and its faint auroral crown hold still —
distant, silent, past.
10.0s — The ship is smaller now, its drive a clean white star among
the real ones. Hold, and end.

AUDIO: Hard vacuum silence — total quiet. No voices. The film's final
music: a single sustained warm chord, fading to nothing by 9 seconds;
the last second is silent.

PHYSICS: Steady low-thrust departure — constant slow recession, no
acceleration visible within the shot. The drive light is steady, not
flickering. Stars stay sharp fixed points.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are aboard
the main ship. 0% bloom, no glow filter, no soft focus, no lens flare.
The hulls stay satin — never glossy. The distant aurora is blue-violet
only — never green. No readable text anywhere. No subtitles, no title
card, no watermark. Hulls static — no melting, no warping. The
background is identical in every frame — same planet, same sky, same
horizon, same ridges: nothing in it changes, appears or disappears
during the shot. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. No speech, no voice, no radio
chatter, no callout, no music, no score — this scene is wordless. No
unnamed prop: nothing appears in or vanishes from a hand, and no
clipboard, tablet, screen or tool exists that this prompt does not
name.
```

---

# 🎵 MÜZİK

> Üç cue; kurallar GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU §7-19'a göre.
> Ayrı MUZIK dosyası açılırsa §17 künyesi ve tam cue promptları oraya
> taşınır, bu bölüm işaretçiye iner (iki yerde tutulan prompt ayrışır).

```
CUE A — "KIRAĞI"    S0-S8   · 88 BPM · soğuk, geniş, düşük yaylı +
        cam armonikler; S2'de girer (hook + S1 müziksiz), S7
        kalkışında tek tam tepe, S8'in sonunda kesilir.
CUE B — "SÜZÜLÜŞ"   S9-S20  · 60 BPM · en seyrek doku: uzun tek
        notalar, amber nabzın 2 s ritmini ASLA taklit etmez (nabız
        perküsyon değildir). S13-S15 hafif tırmanır, S17 iptalinde
        yarım kalır, S18 MÜZİKSİZDİR (yalnız nabız + nefes + taşıyıcı
        hışırtısı [D83]), S19-S20 tek uzun kreşendo.
CUE C — "KAVUŞMA"   S21-S24 · 72 BPM · S21 MÜZİKSİZ başlar (yakalayış
        saf sessizlik + "Tuttum."), S22'nin son saniyesinde TEK sıcak
        majör akor doğar, S23'te çözülür, S24'te tek sürekli akor —
        9. saniyede biter, son saniye sessiz. Fade-out yok.

KURGUYU BAĞLAYAN ÜÇ KARAR:
· Müzik S20'nin sonunda susar; S21 müziksizdir — doruğun sesi
  sessizlik + tek kelimedir.
· "Müziksiz" sahne SESSİZ sahne DEĞİLDİR [D83]: S18 ve S21'de telsiz
  taşıyıcı hışırtısı + nefes + nabız clicki kesme sınırlarında
  KESİNTİSİZ sürer; klip sınırında ölü hava 0.0 sn.
· Sahne sınırları ölçü çizgisine oturur: CUE A 4 ölçü/sahne · CUE B
  2,5 ölçü/sahne · CUE C 3 ölçü/sahne.
```

---

# 📊 FİLM ÖZET TABLOSU

```
FİLM:        THE BLUE DRIFT — Mavi Süzülüş
FORMAT:      16:9 yatay · 3-5 dk klasörü · 25 sahne (standart, sapma yok)
SÜRE:        Hook 9s + 24 × 10s = 249 s = 4:09
DOSYA:       PLAN + PART_A (S0-S12) + PART_B (S13-S24); KAPAK +
             REFERANS_PAKETI sırada
İNSAN:       tam 2 (pilot TURKUAZ · mühendis AMBER) + gövdesiz AI
             (KERTE — ana gemide) · karede insan: 0 → 7 sahne
             (S7·S8·S12·S13·S15·S21·S24) · 2 → 18 sahne (S18'de
             yalnız kol/eldiven görünür, sayı yine 2)
REPLİK:      16 replik / 13 sahne (S2·S6·S9·S10·S11·S13·S14·S16·S17·
             S19·S20·S21·S22) — 12 sahne konuşmasız · MACHINE 10
             (KERTE: S2·S6·S9·S11·S13·S14·S16·S17·S20·S21) · HUMAN 6
             (pilot 4: S6·S14·S17·S22 · mühendis 2: S10·S19) · sayı
             söyleyen HER replik KERTE'nin [D82] · S9 repliği YARIDA
             KESİLİR (tasarım) · S9-S11 arası bağlantı kopukluğu
             karşılıklı atışmayı yapısal olarak kapatır · kasksız
             sahnede (S23) tek kelime YOK · S13·S21 replikleri
             kadrajda insan OLMADAN duyulur (en güvenli biçim)
KASK:        insan görünen 18 sahnenin 17'sinde KAPALI · yalnız S23
             kasksız (basınçlı hangar güvertesi; kasklar rafta
             GÖRÜNÜR) · ara durum yok · arıza sonrası suitler mühürlü
             kalır (kabin havası S15'te harcanır — mantık zinciri)
SIRT/VİZÖR:  sırt ünitesi YOK (düz siluet) — insanlı 36 promptun
             36'sında negatifte · vizör kilidi kasklı 34'ünde; S23
             çiftinde yerine KASKSIZ KİLİT (yarı takılı kask / açık
             vizör yasak) [Ders 79]
SAYAÇLAR:    ① perde tabanı taç→70°→60°→50°→45°→40° (yüzey geri
             sayımı, monotonik) · ② kabin basınç ibresi — S14 yüksek ·
             S16 4. çentik=%40 · S22 yükselir (sönen yol görünür,
             [D78 ①]) · ③ duruş küresi: döner (S9-S14) → DURUR (S16)
             · ④ amber verici nabzı TAM 2 s (S10→S21, ritim sabit) —
             dördü de metinsiz, sayılar yalnız KERTE'nin sesinde
             (çift kanal [D78])
HİÇBİR ŞEY YAPMAMA KİLİDİ: S15'in son pufundan sonra lander tarafında
             hiçbir şey ateşlemez (S16-S21 gövde + negatif)
MOTOR YASAĞI TERSİ: S20 3.0s'den sonra GEMİ de ateşlemez (S20-S22) —
             yakalayış çift-ölü süzülmeyle biter; S24 füzyon tahriki
             yanaşma sonrası, yasak dışı
KAMERA:      25/25 sabit lockoff · lens 24/32/35/85mm küresel ·
             kadraj aileleri: S0↔S24 açılış-kapanış çifti ·
             S17↔S19↔S20 eksen merdiveni (cam, dead-on: 200 m iptal →
             200 m dönüş → 60 m) · S9↔S16 (panel ölür ↔ küre durur) ·
             S21 hangar içi DEAD NOSE-ON (Black Cradle tail-on'unun
             aynadaki tersi)
YERÇEKİMİ:   S0-S7 yüzey 0.4g · S8 geçiş · S9-S22 yörünge 0g
             (kayışlı, D23 0 kare) · S23 gemi güvertesi ·
             yörüngede ALBEDO DOLGUSU VAR ve MAVİ (fizik imzası —
             beyaz/sıfır/mavi üçlemesinin kapanışı)
DORUK:       S21 (YAKALAYIŞ) — kollar 7.0 s'de kapanır, sahne İÇİNDE
             tamamlanır · %84-88, bant içinde · sahibi KERTE
             ("Tuttum.") — edilgen doruk filmin tezidir; insanın
             doruğu S22'de geri gelen nefestir
CENTRAL CHOICE: S14 — kabin havasını itki olarak harcamak ("Say.");
             bedel S16'da ibrede GÖRÜLÜR (%40) · S17 iptali geminin
             kararıdır, pilot onaylar ("Bekleriz."), bedeli S18
             bekleyişi taşır
VİRAL:       S4 (perde) · S7 (kalkış) · S15 (nefes) · S21 (yakalayış)
             — KESİLEMEZ
SICAK RENK:  AMBER ailesi yalnız — mühendis çizgisi · S7 kalkış
             jetleri · verici nabzı (S10→S21) · hangar içi ışık
             (S21→S23) — filmde AÇIK ALEV 0 kare, patlama 0 kare,
             arıza sessiz ve karanlık
MÜZİKSİZ:    S18 ve S21 — ama D83 gereği SESSİZ DEĞİL: taşıyıcı
             hışırtısı + nefes + nabız clicki kesintisiz
KAPAK ADAYI: S21 (hangar ağzında ölü araç, gölge çizgisi gövdede)
             veya S0 (yarım gök dev altında iki lamba havuzu) —
             THE_BLUE_DRIFT_KAPAK.md (sırada)
RİSK:        5/9 ⚠️ tam eşikte (kask · ikinci figür · sayaç ·
             parçacık-dar · diyalog) · kartlarda olmayan iki risk:
             MAVİ-ÜSTÜ-MAVİ (beş mavi skalası + amber istisna +
             HAZIR DÜŞÜŞ) ve AURORA KLİŞESİ (yeşil yasak, 10 s tek
             dalga)
ÜRETİM:      25 imaj + 25 video · 10s klip = Veo 8s + 2s extend
ÜRETİM SIRASI: S21 (yakalayış geometrisi + mavi-üstü-mavi) → S15
             (nefes pufları — yeni malzeme) → S4 (aurora kilidi) →
             S0 (planetshine paleti) — kapı kayıtları PART_A sonuna
             TEK SATIR [D74]
```

---

## 🚪 KURGU KAPISI (Ders 70/72 — teslimden önce)

```
□ Klip sayısı = 25 (plan ile birebir)
□ Toplam süre = 249 s ± 2 s
□ Ekran metni = 0.0 sn — kapak çıktısı / başlık kartı kurguya EKLENMEZ
  (D70/72 zinciri 7 vakaya ulaştı; bu film 8. olmayacak)
□ CENTRAL CHOICE (S14) kurguda VAR: "Say." + valf kavrayışı ekranda;
  bedel S16'da ibrede okunuyor
□ DORUK (S21) kurguda VAR: kollar 7.0 s'de sahne içinde kapanıyor,
  "Tuttum." duyuluyor
□ Ders 79: insanlı 36 promptun çıktısında sırt ünitesi 0 kare · vizör
  yansıması 0 kare · S23'te yarı takılı kask 0 kare
□ Hiçbir şey yapmama kilidi: S15 son pufu → S21 arası lander'da
  ateşleme 0 kare
□ Motor yasağı tersi: S20 3.0s → S22 arası gemide ateşleme 0 kare
□ Amber nabız: S10→S21 her karede TAM 2 s periyot — ritim kayması yok
□ İbre takvimi: S14 yüksek → S16 %40 → S22 yükselen; ara değer 0 kare
□ Duruş küresi: S16'dan itibaren DURMUŞ — sonradan dönen küre 0 kare
□ Perde tabanı monotonik: taç→70°→60°→50°→45°→40°→kenar — geri düşüş
  yok; Part B'de aurora 0 kare (tek istisna S24 uzak taç)
□ Aurora rengi: yeşil 0 kare — yalnız mavi-menekşe
□ Nicelik: 2 kızak kolu · 4 kelepçe · 4 beyaz çerçeve ışığı · 6 puf
□ Yıldızlar her karede keskin nokta — iz/yay 0 kare
□ Müziksiz sahneler (S18 · S21) müziksiz AMA taşıyıcı yatak kesintisiz
  [D83 — klip sınırında ölü hava 0.0 sn]
□ Ses mimarisi [D82]: sayı söyleyen her replik KERTE'de kaldı mı ·
  insan ağzı okunan kare 0 · S9 kesik repliği kesik mi (tamamlanmış
  cümle çıkarsa yeniden üretim değil, KURGU hatasıdır) · comms
  filtresi kask durumunu izliyor (S23 açık-hava akustiği, filtresiz)
□ RAW FOOTAGE: 25 klip × 10 s = 250 s · TRIM BUDGET: 1 s (Hook 9 s
  için tek kırpma) — başka kırpma yok [D100]
```




