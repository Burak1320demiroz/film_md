# 🛰️ THE SECOND SHIP — FAZ 3 / İMDAT · KISIM 3

## S21–S30 PROMPTLARI | 3:20 – 5:00 | Perde I | 16:9 Yatay
### _"Cevap veren herkes ölür."_

> Plan: `00_PLAN.md` · Bible + harita: `README.md` · Anlatı: `../01_SENARYO.md`
> Faz kilitleri (kask · diyalog kadrajı · 10s yolu) + 📎 REFERANS
> lejandı: `../FAZ_01_TRANSIT/FAZ_01_TRANSIT.md`
>
> ✅ **KAPSAM: S21–S30 TAM.** 05.08.2026 yapısı: 10 faz × 10 sahne =
> 100 sahne = 16:40. S30, F4'e eylem sürekliliği + ışık geçişini kurar —
> `../FAZ_04_TARLA/FAZ_04_TARLA.md` o geçişten açılır.
> Bu faz **PERDE DÖNÜŞÜ 1** ile biter: gemiden ayrılıp siluete yürüyüş.
>
> ⛔ Her prompt **self-contained**'dır (AGENTS.md kural ③). Uzunluk
> bandı (README §6, 06.08.2026 revizyonu): **imaj 1.700–2.300 ·
> video 1.950–2.600** karakter.

---

# 🔒 FAZ 3'E ÖZEL KARARLAR

## KARAR 1 — GECE IŞIK KİLİDİ (fazın tamamı)

```
İniş gece oldu; F3'ün on sahnesi de GECE geçer. Işık envanteri sabit:
  ① Tek büyük soluk ay — daima SOL ÜSTTEN, 7000K, sert ve alçak.
  ② Kask lambaları — her insanda iki dar, sert beyaz koni.
  ③ Geminin kokpit penceresinden soluk amber sızıntı.
Başka ışık kaynağı YOK. Şafak F4'ün ilk sahnesinde (S31) doğar —
oradaki ışık geçişinin çalışması için F3'ün gecesi tavizsiz kalmalı.
```

## KARAR 2 — HASAR ENVANTERİ KİLİTLİ (S13 çapası)

```
Gemi her dış sahnede AYNI hasarı taşır, fazlasını değil:
1.2 m camlaşmış dairesel delik (sağ arka bölme) · çökmüş SAĞ ana
bacak · tam 4° sağa yatış · 60 m sürtünme oluğu. "wrecked/destroyed"
yazılmaz [Ders 38] — gemi hasarlı ama BÜTÜN. Delik referansı: FAZ_02
S13 END FRAME karesi.
```

## KARAR 3 — ÇIPLAK TEN SADECE S22'DE

```
Ç7 kurulumu (eldiven ritüeli) bu fazdadır. Çıplak ten filmde üç kez
görünür: S22 (kurulum) · S80 (eldiven düşer) · S81 (temas). Başka
hiçbir sahnede eldiven çıkmaz. S22'de süre İÇ SAYAÇLA kilitli: ten
tam 4 saniye açıkta kalır — prompta saniye damgalarıyla yazılmıştır.
```

## 10 SANİYE YOLU (FAZ_01 · KİLİT 3 uygulaması)

```
B yolu (1 sahne):  S27  → kadrajda sadece zemin dokusu + tek titreşim
A yolu (9 sahne):  S21 S22 S23 S24 S25 S26 S28 S29 S30
```

---

# 🎨 ÜRETİM SIRASI VE İMAJ BÜTÇESİ

```
S21–S30 = 10 video · 12 imaj  (S29 · S30 END FRAME imajı da alır —
tilt ufka varıyor / pull-back kadrajı genişletiyor)

ÖNERİLEN SIRA (kolaydan zora):
  1) S27 → makro zemin, kadro 0. Gece zemin dokusunun testi.
  2) S28 → zemin + tek bot (kimlik yükü düşük)
  3) S29 → sırttan siluet + ufuk (END FRAME'i S30 kompozisyonunu besler)
  4) S22 · S24 · S25 → tek kişilik Kaptan sahneleri
  5) S21 · S23 · S26 · S30 → iki insan (fazın pahalı sahneleri;
     FAZ_01 S3/S4 yüz doğrulaması geçerli)

SES: on sahnenin onu da SESSİZ üretilir. Nefes, telsiz, girdap ve
     diyalog post'ta (ElevenLabs + `MUZIK_VE_SES.md`).
```

---

## 🎬 SAHNE 21 — İLK ADIM

`3:20 – 3:30` · 32mm · kadro 2 · yavaş push-in · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan) + R4/S19-END (arka planda yatık gemi)

_"0.9g. Neredeyse ev gibi."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: çok yavaş push-in.
  İŞLEV: gezegen fiziksel olarak sunuluyor — yaşanabilir gibi görünen,
  yaşanamaz bir yer. Yürüyüş neredeyse normal, sadece fazla yumuşak.
  ⭐ S20'nin oturmuş tozundan eylem sürekliliği: kapak o sessizliğin
     içinde açılmış, ikisi de çoktan dışarıdadır.
  ⛔ DERS 69 — İNİŞ HAREKETİ KADRAJA ALINMAZ (0 kez).
     Karakter ya gemidedir ya gemi dışındadır; aradaki hareket
     kesmeyle atlanır. Bu sahne inişin SONRASIDIR: ikisi de zeminde,
     gemiden ayrılmış. Basamakta duran, inen, binen figür YAZILMAZ.
     Gerekçe: klonun ürediği tek sahne tipi bu — Stone Sky S10-B,
     Starless Circle S14 (gemi merdiveni, `two identical astronauts`),
     Unbroken City (loş giriş). Üçünün koşulu burada bir aradaydı:
     iki figür + gemi kapağı + gece.
  ⚠️ DERS 69 ② — "boş" sıfatı tutmuyor, BOŞLUK NESNEYLE kanıtlanır:
     kapağın ağzı karanlık, alt basamağı çıplak, üzerinden tek bir
     lamba konisi geçiyor. Model sıfatı değil nesneyi çiziyor.
  ⚠️ KARIŞMA KİLİDİ gömülü: turuncu/teal + 13 cm.
  ⚠️ DERS 32 ÖLÇEK KİLİDİ (07.08.2026, R3): gemi kadrajda küçük
     kalıyordu. R1 metre oranı ("deck 8 m = 4×") tutmadı — model dünya
     ölçüsü hesaplayamıyor. R2 "figürün en az 2 katı" TERS TEPTİ —
     model gemiyi TAM 2 kat çizdi, insanlar dev göründü. R3: sayısal
     oran YOK; ölçek İNSAN tarafından kurulur: ① figürler devasa
     gövdenin dibinde MİNİK (`figures look TINY at its base`),
     ② üst güverte kadraj üstünden kırpılır, ③ gövde iki yan kenardan
     taşar, ④ kapak ağzı 2.2 m, ⑤ negatif çift yönlü: `no small ship
     and no giant people`. Sonraki gemi promptlarına AYNEN kopyala.
```

### 📸 IMAGE PROMPT

```
SCENE:
Two suited crew stand on a dark basalt plain at night, clear of their
crashed ship, helmet lamps cutting two cones.

ENVIRONMENT:
A wide dark basalt plain at night, near-black sky, one large pale moon
upper LEFT lighting everything grey-blue at 7000K. Directly behind
the figures the 31-meter cargo courier LOOMS as a towering wall of
metal: hull past both frame sides, upper deck cropped by the top of
frame, so massive the two figures look TINY at its base. It rests
tilted exactly 4
degrees right, right main leg collapsed, not skids, faint amber
cockpit spill, a dim amber spill from its open 2.2-meter airlock
hatch — mouth dark and empty, bottom step bare. Fine dust lies
settled.

SUBJECT:
Exactly two figures on the ground, six meters clear of the hull. LEFT:
a 41-year-old woman pilot, 1.68 m, slim — high cheekbones, light olive
skin, dark grey-green eyes, a fine faded white scar splitting her LEFT
eyebrow, dark brown hair in a tight low bun, dark grey-blue pressure
suit with ORANGE worn reinforcement. RIGHT: a 33-year-old man flight
engineer, 1.81 m, broad-shouldered — light brown skin, short black
stubble, a 2 cm burn scar on his RIGHT cheekbone, TEAL GREEN
reinforcement, oversized back tool module. Orange for her, teal for
him, never swapped; his head sits 13 cm higher. Both helmeted, visors
transparent, helmet lamps on.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position nine meters away
at chest height, both figures and the hatch in frame. The two figures
read as small human silhouettes at the base of the huge hull.

LIGHTING:
Night. Hard grey-blue moonlight from the upper LEFT; two narrow hard
white helmet-lamp cones; dim amber spill from the airlock. Soft-edged
shadows from the thin atmosphere.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly two figures —
no third person, no duplicate. Both stand on open ground: nobody on
the hatch, on its step or in its opening, which stays dark and empty.
Orange stays on the woman, teal on the man; scars stay LEFT eyebrow /
RIGHT cheekbone; no morphing, no face swap. Visors stay clear,
uncoated glass — no tint, no mirror coating. The ship keeps its fixed
damage: one OPEN circular hole (no glass, no pane), collapsed right
leg, 4-degree tilt. No small ship and no giant people: the figures
stay tiny against the massive hull, which spans past both frame sides.
Dust lies settled, never hovers. No bloom, no glow
filter, no lens flare. No readable text, digits or markings; no
captions, no HUD, no watermark. No bare head. Photorealistic, 35mm
anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, one very slow push-in from nine
to seven meters, no cuts:

SETUP: the camera creeps forward at a constant rate at chest height,
framing two suited figures on open ground with
their crashed cargo ship behind them. No pan, no tilt, no shake.
FRAME: a dark basalt plain at night, one large pale moon upper LEFT at
7000K, near-black sky. The 31-meter cargo courier LOOMS directly
behind the figures as a towering wall of metal: hull past both frame
sides, upper deck cropped by the top of frame, so massive the two
figures look TINY at its base, tilted exactly 4
degrees right, right main leg collapsed, not skids, faint amber
cockpit spill, a dim amber spill from its open 2.2-meter airlock
hatch — mouth dark and empty. Exactly two suited figures on the dust six meters
clear of the hull: a 41-year-old woman pilot, 1.68 m, slim, ORANGE
worn reinforcement on a dark grey-blue suit, a fine faded scar
splitting her LEFT eyebrow, dark brown hair in a low bun; and a
33-year-old man, 1.81 m, broad- shouldered, TEAL GREEN reinforcement,
short black stubble, a 2 cm burn scar on his RIGHT cheekbone,
oversized back tool module. Both in integrated helmets, visors
transparent, lamps lit.

0s — Both stand still on the dust, side by side, the ship behind them,
their lamp cones lying on the ground ahead. The empty hatch mouth is
dark, its bare bottom step crossed by one cone.
2s — The woman takes one slow step forward — the boot lands a touch
too softly, the fall a fraction slower than Earth — and a small puff
of dust rises and settles at once.
5s — The man follows a pace behind her, heavier, his step raising a
slightly larger puff that also falls straight back down.
7s — Both lamp cones sweep slowly outward across the plain, left and
right, and stop on the darkness ahead.
10s — They hold, two lit cones on the empty plain, the tilted ship
behind them. No cuts.

Every step obeys 0.9g: boots land softly but with weight, dust rises
low and settles at once, never hovers, never swirls. Both stay on open
ground: neither climbs, mounts, descends or stands on the hatch or its
step, and nothing appears in its opening. Orange stays on the woman,
teal on the man; the 13 cm height difference holds; scars stay LEFT
eyebrow / RIGHT cheekbone; both faces keep identical bone structure —
no morphing. Visors stay clear, uncoated glass — no tint, no mirror
coating. Neither speaks: mouths closed. The ship's damage stays fixed
— one hole, collapsed right leg, 4-degree tilt. Through the whole
push-in the figures stay tiny at the base of the massive hull, which
stays past both frame sides — the ship never shrinks, the people never
grow. Exactly two figures.
Constant-rate push-in only: no cuts, no transitions, no shake, no
zoom. No bloom, no glow filter, no lens flare. No readable text or
digits; no captions, no HUD, no watermark. No bare head.
Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 22 — ELDİVEN

`3:30 – 3:40` · 85mm · kadro 1 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 (KAPTAN master — bilek halkası bu sahnenin çapası)

_"Dört saniye."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  ⭐ ÇEHOV 7 BURADA KURULUYOR — filmin merkez halkası. Şu anda zararsız
     bir alışkanlık; S80'de eldiven yine düşecek, S81'de bu çıplak el
     bedeli ödeyecek.
  ⭐ KARAR 3: çıplak ten TAM 4 SANİYE açıkta (4s–8s arası). Saniye
     damgaları prompta gömülü.
  ⭐ KİLİT 2 rahat: konuşma yok. 85mm el + yüz kenarda flu.
```

### 📸 IMAGE PROMPT

```
SCENE:
Close on a woman pilot's hands at an open hull panel at night: her
right glove detached at the wrist ring, bare fingers testing a
connector — an old, private habit.

ENVIRONMENT:
An open access panel in the flank of a crashed cargo ship at night:
dark grey-brown panelling, grey repair patches, a shallow recess
holding abstract amber indicator points and a row of connectors.
Around the recess, dust and fine scratches; beyond it the dark plain
falls out of focus. Hard grey-blue moonlight from the upper LEFT; her
helmet lamps light the recess in two overlapping white pools.

SUBJECT:
The gloved LEFT hand and bare RIGHT hand of a 41-year-old woman pilot
fill the frame at chest height. The right glove hangs from her
forearm, detached at its visible wrist ring; her bare hand — light
olive skin, short clean nails, visible pore texture — rests two
fingers on a connector housing. The dark grey-blue suit sleeve carries
ORANGE worn reinforcement at the elbow; her forearm panel shows slow
abstract sliding segments. At the frame's soft right edge, her
helmeted profile is out of focus, visor transparent, eyes down on the
work.

CAMERA:
Shot on an 85mm lens from a fixed position one point two meters away,
f/2.8, at chest height, shallow depth of field — hands sharp, face
soft. True human scale.

LIGHTING:
Night. Two hard white helmet-lamp pools on the recess; grey-blue 7000K
moonlight rims her shoulder; abstract amber points glow low. Skin
keeps texture; nothing blooms.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly one figure — no second person, no second pair of hands. The
bare hand keeps five fingers, correct anatomy, clear boundaries — it
never merges with or melts into any surface. Reinforcement stays
ORANGE. The visor stays clear, uncoated glass — no tint, no mirror
coating, no reflection that hides what is behind it. The panel shows
abstract light only — no readable text, letters or digits. No sparks,
no arc, no flame. No bloom, no glow filter, no lens flare, no waxy
skin. No captions, no HUD, no watermark. No bare head. Photorealistic,
35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 85mm, fixed lockoff one point two meters away, no
cuts, no camera movement:

SETUP: the camera is locked off at chest height on an open hull panel,
f/2.8, shallow depth of field — the recess and her hands sharp, her
helmeted profile soft at the right edge. It never moves. FRAME: at
night, lit by two hard white helmet-lamp pools and grey-blue 7000K
moonlight from the upper LEFT: the hands of a 41-year-old woman pilot
at a recess of abstract amber indicator points and connectors. Dark
grey-blue suit sleeves with ORANGE worn reinforcement; the RIGHT glove
shows a visible detachable ring at the wrist; her forearm panel slides
slow abstract segments. Her out-of-focus profile watches from the
frame edge, visor transparent.

0s — Both hands gloved. Her left hand steadies the panel edge; her
right thumb hooks the wrist ring of the right glove.
2s — She twists the ring a quarter turn and draws the glove off in one
practised motion; it hangs from the forearm by its tether.
4s — BARE SKIN, second one: her bare fingers settle on the connector
housing and press, testing its seat — light olive skin, pore texture
sharp in the lamp light.
6s — BARE SKIN, second three: two fingers walk one connector to the
left, press again, hold. The amber points do not change.
8s — BARE SKIN ends at exactly four seconds: she slides the glove back
over the hand and seats the wrist ring with a firm quarter turn.
10s — Both hands gloved again, resting still on the panel edge. No
cuts.

The bare hand stays anatomically correct for every frame: five
fingers, clear boundaries, never merging with or sinking into any
surface, never deforming the panel. The glove comes off and returns
exactly once — no second removal, no vanishing glove, no extra hands.
Reinforcement stays ORANGE; the visor stays a distinct glass surface;
her soft profile never sharpens, never morphs. Exactly one figure.
Camera locked: no cuts, no transitions, no shake, no zoom. Abstract
light only on all panels — no readable text, letters or digits; no
sparks, no flame. No bloom, no glow filter, no lens flare, no waxy
skin. No captions, no HUD, no watermark. The visor stays clear,
uncoated glass — no tint, no mirror coating, no reflection that hides
what is behind it. No bare head. Photorealistic, 35mm anamorphic film
grain.
```

---

## 🎬 SAHNE 23 — TAMİR EDİLEBİLİR

`3:40 – 3:50` · 50mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan) + R4/S19-END (gemi + delik kadrajda)

_"Her şey tamir edilir."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: Mühendis'in yayı burada başlar — inancının tek cümlesi.
  Film bu cümleyi S64-S68 bandında kıracak.
  ⚠️ KADRO BÜTÇESİ: `2` işaretli 23 sahnenin 6.'sı.
  ⭐ KİLİT 2: 50mm · 4 m · konuşan Mühendis gövdeye dönük, ağız
     profilde küçük [Ders 35]. 1 replik, post'ta.
  ⚠️ Ders 38: hasar tarifi S13 envanteriyle birebir; abartma yok.
  ⚠️ DERS 32 ÖLÇEK KİLİDİ (07.08.2026, S21-R3 dili): gemi kadrajda
     küçük çıkıyordu. Bu kadraj BÖĞÜR yakın planı — gövde figürlerin
     arkasında TÜM kadrajı dolduran metal duvardır, iki yandan ve
     üstten taşar, GEMİNİN TAMAMI ASLA GÖRÜNMEZ. Sayısal oran yazma
     (S21-R2 dersi: "2 katı" yazınca model gemiyi tam 2 kat çizdi).
```

### 📸 IMAGE PROMPT

```
SCENE:
Two suited crew read the damage on their crashed ship at night: the
engineer close to the open circular hole, the pilot a step behind.

ENVIRONMENT:
The right flank of a grounded 31-meter cargo courier at night — a
towering wall of metal behind the figures, running past both frame
sides and above the top of frame, the full ship never in view —
tilted exactly 4 degrees right, right main leg
collapsed, not skids. On the upper right rear bay, a 1.2-meter
perfectly circular hole with a clean, polished, faintly pearlescent
edge — no burn, no tear. Dark grey-brown panelling, mismatched grey
patches, faded orange stripes. One large pale moon upper LEFT.

SUBJECT:
Exactly two figures. FOREGROUND RIGHT, close to the hull: a 33-year-
old man flight engineer, 1.81 m, broad-shouldered — light brown skin,
short black stubble, a 2 cm burn scar on his RIGHT cheekbone, TEAL
GREEN worn reinforcement on a dark grey-blue suit, oversized back tool
module, closed sheath on his left hip — head turned up toward the
hole, helmet lamps on its rim. A step behind LEFT: a 41-year-old woman
pilot, 1.68 m, slim — light olive skin, a fine faded scar splitting
her LEFT eyebrow, dark brown hair in a low bun, ORANGE reinforcement.
Orange for her, teal for him, never swapped; his head sits 13 cm
higher. Both visors transparent.

CAMERA:
Shot on a 50mm lens from a fixed position four meters away at chest
height, both figures and the hole in frame, the hull filling
everything behind them. The two figures stand small against the wall
of panelling; the hole reads as 1.2 meters against the humans.

LIGHTING:
Night. Grey-blue 7000K moonlight from the upper LEFT; four hard white
helmet-lamp pools on the hull; the polished rim catches them as a thin
clean sheen, never a glow.

NEGATIVE:
The hole is open and empty — no glass, no pane, no cover, no window.
Single unbroken take, no cuts, no camera shake. Exactly two figures.
Orange stays on the woman, teal on the man; scars stay LEFT eyebrow /
RIGHT cheekbone; no morphing, no face swap. Visors stay clear,
uncoated glass — no tint, no mirror coating, no reflection that hides
what is behind them. No small ship, no giant people: the hull stays a
towering wall past both frame sides and the top of frame; the whole
ship is never visible. Damage stays fixed: one circular hole, collapsed
right leg, 4-degree tilt — no extra damage. No handheld tool; the
sheath stays closed. No sparks, no fire. No bloom, no glow filter, no
lens flare. No readable text, digits or markings; no captions, no
watermark. No bare head. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff four meters away, no cuts, no
camera movement:

SETUP: the camera is locked off at chest height framing the right
flank of the crashed ship, the circular hole high in frame, two suited
figures below it. It never moves for the whole ten seconds. FRAME:
night, one large pale moon upper LEFT at 7000K. The 31-meter hull is
a towering wall of metal filling the frame behind the figures, past
both frame sides and the top of frame, the full ship never in view,
tilted exactly 4 degrees right, right main leg collapsed, not skids;
a 1.2-meter perfectly circular open hole, polished edge, in the right
rear bay. FOREGROUND RIGHT: a 33-year-old man flight engineer, 1.81 m,
broad-shouldered, TEAL GREEN worn reinforcement, short black stubble,
a 2 cm burn scar on his RIGHT cheekbone, oversized back tool module.
Behind LEFT: a 41-year-old woman pilot, 1.68 m, slim, ORANGE
reinforcement, a fine faded scar splitting her LEFT eyebrow, dark
brown hair in a low bun. Both helmeted, visors transparent, helmet
lamps lit.

0s — His lamps track slowly along the hull from the engine section
toward the hole; hers hold steady on the collapsed leg.
3s — He lays a gloved palm flat on the panelling beside the hole —
feeling the structure rather than looking at it — and holds it there.
5s — He turns his head toward her, face in three-quarter profile, and
speaks one short line; his lips move briefly, small amplitude.
7s — She answers with a single slow nod, saying nothing. Her lamps
stay on the leg.
10s — He takes the palm off the hull and both hold, lamps steady on
the wound. No cuts.

His palm keeps a clear boundary against the hull — it never merges,
never sinks, never deforms the panel; the rim of the hole is never
touched. The damage stays fixed: one circular hole, collapsed right
leg, 4-degree tilt — nothing new breaks, nothing vents. Orange stays
on the woman, teal on the man; the 13 cm height difference holds;
scars stay LEFT eyebrow / RIGHT cheekbone; both faces keep identical
bone structure — no morphing, no face swap. Visors stay clear,
uncoated glass — no tint, no mirror coating, no reflection that hides
what is behind them. No handheld tool appears. Exactly two figures.
The hull stays a close towering wall past both frame sides and the
top of frame — the ship never shrinks, the people never grow, the
whole ship never comes into view.
Camera locked: no cuts, no transitions, no shake, no zoom. No bloom,
no glow filter, no lens flare. No readable text or digits; no
subtitles, no captions, no watermark. No bare head. Photorealistic,
35mm anamorphic film grain. The hole is open and empty — no glass, no
pane, no cover, no window.
```

---

## 🎬 SAHNE 24 — ANTEN

`3:50 – 4:00` · 50mm · kadro 1 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 (KAPTAN master) + R4/S19-END (gövde arka planda)

_"Tereddüt yok."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: kusurun eşiği. "DO NOT ANSWER" uyarısı iki dakika önce
  duyuldu; elleri hızlı ve düzgün — hatırlamıyor ya da önemsemiyor.
  ⭐ Anten: ince katlanır kafes direk — "dish/radar" yazılmaz, model
     çanak klişesine kaçmasın. Tepesinde TEK soluk amber nokta.
  ⭐ Konuşma yok; sahnenin tamamı el işi. [Ders 37: ekipman sahne
     başında kadrajda — sonradan belirmez.]
```

### 📸 IMAGE PROMPT

```
SCENE:
A woman pilot raises a thin folding lattice mast from a hull recess at
night — the emergency antenna, deployed without a moment of
hesitation.

ENVIRONMENT:
The flank of a grounded 31-meter cargo courier at night, tilted
exactly 4 degrees right: dark grey-brown panelling, grey repair
patches, an open shallow recess at chest height holding the folded
mast and abstract amber indicator points. The dark basalt plain
behind, one large pale moon upper LEFT, near-black sky.

SUBJECT:
A 41-year-old woman pilot, 1.68 m, slim, in three-quarter view from
her right, both gloved hands on a thin folding lattice mast that is
already half-raised from the recess — a spare, skeletal column of dark
metal, hinged in sections, its tip carrying one small dull amber
point. High cheekbones, light olive skin, sharp jawline, dark grey-
green eyes, a fine faded white scar splitting her LEFT eyebrow, dark
brown hair in a tight low bun. Dark grey-blue pressure suit with
ORANGE worn reinforcement, three abstract chest indicators, integrated
helmet with a fully transparent seamless visor, right glove with a
visible detachable wrist ring.

CAMERA:
Shot on a 50mm lens from a fixed position three meters away at chest
height, figure and mast both in frame. True 1.68-meter human scale
against the hull.

LIGHTING:
Night. Grey-blue 7000K moonlight from the upper LEFT rims her helmet
and shoulders; her two helmet lamps pool hard white on the recess; the
mast tip's amber point glows low and steady.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly one figure. Her face keeps identical bone structure — no
morphing; the scar stays on her LEFT eyebrow. Reinforcement stays
ORANGE. The visor stays clear, uncoated glass — no tint, no mirror
coating, no reflection that hides what is behind it. The mast is a
thin lattice column only — no dish, no bowl, no rotating radar, no
cables whipping. Hands never merge with mast or hull. Abstract light
only — no readable text, letters or digits. No sparks, no flame. No
bloom, no glow filter, no lens flare. No captions, no HUD, no
watermark. No bare head. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff three meters away, no cuts,
no camera movement:

SETUP: the camera is locked off at chest height on the flank of the
crashed ship, framing an open recess, a folded lattice mast and the
woman working it. It never moves for the whole ten seconds. FRAME:
night, one large pale moon upper LEFT at 7000K, near-black sky, the
tilted grey-brown hull crossing the frame. A 41-year-old woman pilot,
1.68 m, slim — light olive skin, a fine faded scar splitting her LEFT
eyebrow, dark brown hair in a tight low bun, dark grey-blue suit with
ORANGE worn reinforcement, three abstract chest indicators, integrated
helmet with a fully transparent seamless visor, helmet lamps lit. The
folded mast lies in its recess, its tip carrying one small dull amber
point.

0s — Her hands are already working: she frees the mast's first hinge
with one firm pull. No hesitation, no glance over her shoulder.
2s — She raises the mast through its arc; the sections unfold one
after another with clean mechanical certainty, her hands moving to
each hinge in turn.
5s — The mast locks upright with a visible seat — a small, definite
settling of metal into metal. Its amber tip point steadies.
7s — She presses two fingers on a recess control; a second abstract
amber point wakes beside the first and holds steady.
10s — She rests both hands on the recess edge and looks up along the
standing mast. Mouth closed throughout. No cuts.

The mast unfolds exactly once and stays upright — it never bends,
never sways, never telescopes back, never becomes a dish or radar. Her
hands keep clear boundaries against mast and hull — no merging, no
melting. Her face keeps identical bone structure — no morphing; the
scar stays on her LEFT eyebrow; reinforcement stays ORANGE; the visor
stays a distinct glass surface. She never speaks. Exactly one figure.
Camera locked: no cuts, no transitions, no shake, no zoom. Abstract
light only — no readable text, letters or digits anywhere. No sparks,
no flame. No bloom, no glow filter, no lens flare. No captions, no
HUD, no watermark. The visor stays clear, uncoated glass — no tint, no
mirror coating, no reflection that hides what is behind it. No bare
head. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 25 — ÇAĞRI

`4:00 – 4:10` · 85mm · kadro 1 · yavaş push-in · **A yolu**
📎 **REFERANS:** R1 (KAPTAN master)

_"Sesi alçak. Fısıltıya yakın."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: 1.8 m → 1.4 m push-in.
  ⭐ ÇEHOV 5 BURADA KURULUYOR — filmin motoru. Bu çağrı bir gemiyi
     çağıracak (S58) ve o gemi vurulmak üzere gelecek. Kaptan'ın
     bedeli bu on saniyede doğuyor.
  ⭐ HAREKET İMZASI 2. tekrar: cümle biterken sol el göğse gider
     (kurulum S9 · doruk S81).
  ⭐ KİLİT 2 çözümü: baş öne, ağız sol ön kola dönük — 85mm'de ağız
     hattı OKUNMAZ. Replik post'ta; dudak genliği küçük.
```

### 📸 IMAGE PROMPT

```
SCENE:
Close on a woman pilot at night, head bowed to her forearm panel,
sending a distress call in a voice that is almost a whisper.

ENVIRONMENT:
Beside the standing lattice mast at the flank of a crashed cargo ship
at night: dark grey-brown panelling out of focus, one small dull amber
point at the mast tip above, the dark plain beyond. One large pale
moon upper LEFT at 7000K; her helmet lamps angled down, pooling on her
raised forearm.

SUBJECT:
A 41-year-old woman pilot in a tight three-quarter close-up from her
right, chest-up, her head bowed toward her raised LEFT forearm so her
mouth is angled down and away from the lens. High cheekbones, light
olive skin, sharp jawline, thin lips, dark grey-green eyes lowered, a
fine faded white scar splitting her LEFT eyebrow, dark brown hair in a
tight low bun. Dark grey-blue pressure suit with ORANGE worn
reinforcement, three abstract chest indicators — a slow blue pulse, an
amber bar, a green dot — integrated helmet with a fully transparent
seamless visor carrying a faint amber reflection. Her left forearm
panel shows slow abstract sliding segments, one of them pulsing
evenly: a transmission running.

CAMERA:
Shot on an 85mm lens from a fixed position one point eight meters
away, f/2.8, slightly above her eye line looking down, shallow depth
of field. Accurate perspective, no distortion.

LIGHTING:
Night. Hard white helmet-lamp pool on the forearm panel keys her face
from below; grey-blue 7000K moonlight rims her helmet from the upper
LEFT. High contrast; skin keeps pore texture.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one figure —
no second person, no reflected face. Her face keeps identical bone
structure — no morphing; the scar stays on her LEFT eyebrow.
Reinforcement stays ORANGE. The visor stays clear, uncoated glass — no
tint, no mirror coating, no reflection that hides what is behind it.
All panels show abstract light only — no readable text, letters or
digits. No bloom, no glow filter, no lens flare, no waxy skin. No
captions, no subtitles, no name label, no HUD, no watermark. No bare
head. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 85mm, one slow push-in from 1.8 to 1.4 meters, no
cuts:

SETUP: the camera creeps forward at a constant, almost imperceptible
rate, slightly above her eye line looking down, f/2.8, shallow depth
of field. No pan, no tilt, no shake. FRAME: night. A 41-year-old woman
pilot chest-up, head bowed toward her raised LEFT forearm, mouth
angled down and away from the lens — high cheekbones, light olive
skin, dark grey-green eyes, a fine faded white scar splitting her LEFT
eyebrow, dark brown hair in a tight low bun. Dark grey-blue suit with
ORANGE worn reinforcement, three abstract chest indicators, integrated
helmet with a fully transparent seamless visor. Her forearm panel
slides slow abstract segments, one pulsing evenly. Hard white lamp
light from below, grey-blue 7000K moon rim from the upper LEFT.

0s — She watches the pulsing segment a moment, then begins to speak
into the bowed helmet — lips moving briefly, small amplitude, mouth
turned from the lens.
3s — The line continues, measured and procedural. Mid-sentence her
voice visibly softens: her jaw slows, the movements shrink almost to
nothing.
5s — She finishes the line nearly motionless — the last words landing
like a whisper. The pulsing segment keeps its even beat.
7s — Her RIGHT hand stays at the forearm; her LEFT hand rises and
presses flat over the three chest indicators, and holds there.
10s — The push-in has closed. She stands still, head bowed, left hand
on her chest, the segment still pulsing. No cuts.

Her mouth is never square to the lens; lip movement stays brief and
small; she never shouts. Her face keeps identical bone structure and
eye spacing — no morphing; the scar stays on her LEFT eyebrow.
Reinforcement stays ORANGE. The visor stays clear, uncoated glass — no
tint, no mirror coating, no reflection that hides what is behind it.
The panels show abstract light only — no readable text, letters,
digits or waveform graphics at any second. Exactly one figure.
Constant-rate push-in only: no cuts, no transitions, no shake, no
angle change. No bloom, no glow filter, no lens flare, no waxy skin.
No subtitles, no captions, no name label, no HUD, no watermark. No
bare head. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 26 — BEKLEME

`4:10 – 4:20` · 32mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan) + R4/S19-END (gövde arkada)

_"Cevap yok."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: bekleyiş. Hiçbir şey söylemiyorlar; telsiz boş.
  ⚠️ GİZLİ KURULUM: ikisi de gövdeye ve zemine DAYANIYOR. Dokuma'nın
     kuralı sessizce işliyor — seyirci kuralı henüz bilmiyor. Kadraj
     bunu VURGULAMAZ; sadece kaydeder.
  ⚠️ KADRO BÜTÇESİ: `2` işaretli 23 sahnenin 7.'si.
  ⭐ Konuşma yok. Kask lambaları KAPALI — sahnenin tek ışığı ay ve
     kokpit sızıntısı. Fazın en karanlık karesi.
```

### 📸 IMAGE PROMPT

```
SCENE:
Two suited crew sit on the ground with their backs against their
crashed ship at night, waiting for an answer that does not come.

ENVIRONMENT:
The base of a grounded 31-meter cargo courier at night, hull tilted
exactly 4 degrees right, right main leg collapsed, not skids. Dark
grey-brown panelling rises behind them; a faint amber spill from the
cockpit window high above; the thin lattice mast stands at the edge of
frame, one dull amber point at its tip. Dark basalt plain runs to an
empty horizon; one large pale moon upper LEFT, near-black sky.

SUBJECT:
Exactly two figures seated on the dust, backs against the hull, legs
out, helmets on, lamps OFF. LEFT: a 41-year-old woman pilot, 1.68 m,
slim — light olive skin, a fine faded white scar splitting her LEFT
eyebrow, dark brown hair in a tight low bun, ORANGE worn reinforcement
on a dark grey-blue suit. RIGHT, half a meter apart: a 33-year-old
man, 1.81 m, broad-shouldered — light brown skin, short black stubble,
a 2 cm burn scar on his RIGHT cheekbone, TEAL GREEN reinforcement,
oversized back tool module forcing him slightly forward off the hull.
Orange for her, teal for him, never swapped. Both visors transparent,
both faces turned up toward the sky.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position seven meters away
at seated eye level, both figures small against the hull. True human
scale against the 31-meter ship.

LIGHTING:
Night. Grey-blue 7000K moonlight from the upper LEFT is the key — low,
hard, raking; the amber cockpit spill warms one edge of the hull.
Faces read dim through the visors. Deep shadow everywhere else.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly two figures.
Orange stays on the woman, teal on the man; scars stay LEFT eyebrow /
RIGHT cheekbone; no morphing, no face swap. Visors stay clear,
uncoated glass — no tint, no mirror coating, no reflection that hides
what is behind them. Helmet lamps stay OFF. Damage stays fixed — hole,
collapsed leg, 4-degree tilt. Dust lies settled. No bloom, no glow
filter, no lens flare. No readable text or digits; no captions, no
watermark. No bare head. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff seven meters away,
no cuts, no camera movement:

SETUP: the camera is locked off at seated eye level, framing two
figures at the base of the tilted hull. It never moves for the whole
ten seconds. Almost nothing happens; the stillness is the scene.
FRAME: night, one large pale moon upper LEFT at 7000K. The 31-meter
hull rises dark behind two seated figures, backs against the
panelling, legs out on the dust, helmet lamps OFF. LEFT: a 41-year-old
woman pilot, 1.68 m, ORANGE worn reinforcement, a fine faded scar
splitting her LEFT eyebrow, dark brown hair in a low bun. RIGHT: a
33-year-old man, 1.81 m, broad-shouldered, TEAL GREEN reinforcement,
short black stubble, a 2 cm burn scar on his RIGHT cheekbone. Both
visors transparent, faces up toward the sky. A faint amber cockpit
spill above; the lattice mast's single amber point at frame edge.

0s — Both sit motionless. Their breathing is the only movement — slow
rises of the chest indicators' dim glow.
3s — His head rolls slowly from the sky toward the dark horizon, then
back. She does not move at all.
5s — A thin, weak drift of low dust crosses the base of frame and
settles. The mast's amber point holds steady — no answer arrives.
8s — Her gloved fingers curl once against the dust beside her hip and
go still again.
10s — Both hold, leaned into the ship, faces up, silent. No cuts.

Neither figure speaks at any second: mouths closed, no lip movement.
Neither stands, neither gestures; the scene stays seated and still.
Orange stays on the woman, teal on the man; the 13 cm difference holds
even seated; scars stay LEFT eyebrow / RIGHT cheekbone; both faces
keep identical bone structure — no morphing. Visors stay clear,
uncoated glass — no tint, no mirror coating, no reflection that hides
what is behind them. Helmet lamps stay OFF — no cone of light appears.
The ground never moves, never bulges, never glows — nothing under them
is shown reacting. Dust falls and settles, never hovers. Exactly two
figures. Camera locked: no cuts, no transitions, no shake, no zoom. No
bloom, no glow filter, no lens flare. No readable text or digits; no
captions, no watermark. No bare head. Photorealistic, 35mm anamorphic
film grain.
```

---

## 🎬 SAHNE 27 — GİRDAP

`4:20 – 4:30` · 100mm · kadro 0 · fixed lockoff · **B yolu (retime)**
📎 **REFERANS:** yok — kadro 0 makro zemin; referanssız üret

_"Dakikada dört vuruş."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  ⭐ FİLMİN SAATİ BURADA BAŞLIYOR. Girdap ritmi dakikada 4 — yani
     sahneye TEK vuruş düşer (4. saniyede). Ritim S76'da dakikada
     11'e çıkacak; seyirci saymayacak ama hissedecek.
  ⭐ SES POST'TA. Kadrajda vuruşu temsil eden şey: toz zerrelerinin
     TEK, kısa, senkron titremesi. Işık değişmez, zemin AÇILMAZ.
  ⭐ B yolu güvenli: kadrajda insan yok, tek hareket mikro ölçekte.
```

### 📸 IMAGE PROMPT

```
SCENE:
An extreme close view of the planet's surface at night: settled dust
on dark basalt, utterly still — the frame that will carry the
world's hidden heartbeat.

ENVIRONMENT:
A patch of dark basalt ground no wider than a meter, seen from
directly above at close range. Fine grey dust lies settled in
drifts and pockets; hairline fracture lines cross the stone; a few
small angular pebbles sit half-buried. Nothing else — no boot
prints, no equipment, no horizon, no sky.

SUBJECT:
No figures. The subject is the surface itself: the grain of the
settled dust, sharp and dry in raking light; the fracture lines
running like old scars; the faint tonal shift where dust thins over
bare stone. Every particle rests. The composition is even and
patient — nothing draws the eye to any single point, because in the
video the whole field will tremble once, together.

CAMERA:
Shot on a 100mm macro lens from a fixed position ninety centimeters
above the ground, square to the surface, f/4 — the whole field in
crisp focus. True macro scale: dust grains resolve individually.

LIGHTING:
Night. One hard, low grey-blue key at 7000K rakes across the frame
from the upper LEFT — moonlight — throwing long micro-shadows from
every grain and pebble. No other source; deep soft black in the
shadow pockets.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly zero figures — no hand, no boot, no equipment, no shadow of
a person. The ground is solid stone and dust: no cracks opening, no
veins glowing, no light from below, no movement of any kind in the
still frame. Nothing emits light. No bloom, no glow filter, no lens
flare. No readable text, letters, digits or symbols; no captions, no
HUD, no watermark. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 100mm macro, fixed lockoff ninety centimeters
above the ground, no cuts, no camera movement:

SETUP: the camera is locked off square to a patch of dark basalt
ground seen from directly above, f/4, the whole field in crisp
focus. It never moves, never racks focus, for the whole ten seconds.
FRAME: settled fine grey dust over dark stone, hairline fracture
lines, a few half-buried angular pebbles. One hard, low grey-blue
7000K key rakes from the upper LEFT, throwing long micro-shadows
from every grain. No horizon, no sky, no figures.

0s — Absolute stillness. Every dust grain rests; the micro-shadows
are motionless.
4s — ONE deep, slow beat passes through the ground: every loose
grain in the frame trembles at the same instant — a single, short,
synchronized shiver, no grain travelling anywhere — and the field
falls still again within half a second. The stone itself does not
move. The light does not change.
6s — Stillness again, exactly as before. The fracture lines are
unchanged; nothing has opened, nothing glows. The micro-shadows
stand exactly where the raking key light left them.
8s — The frame holds its silence. A single grain near a pebble,
unsettled by the beat, tips and comes to rest.
10s — Total stillness to the final frame. No second beat arrives.
No cuts.

There is exactly ONE tremor in the whole shot, at the fourth second
— never a second one, never a rhythm visible on screen. The grains
shiver in place and settle at once: no grain floats, hovers, swirls
or migrates; no wave rolls across the field; the ground never
cracks, never opens, never bulges, never glows; no light comes from
below; no vein appears; the pebbles never shift and the fracture
lines never widen. Exactly zero figures. Camera locked: no
cuts, no transitions, no shake, no zoom, no push-in, no focus rack.
No bloom, no glow filter, no lens flare. No readable text, letters,
digits or symbols; no captions, no HUD, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 28 — KABARAN ZEMİN

`4:30 – 4:40` · 100mm · kadro 1 · fixed lockoff · **A yolu**
📎 **REFERANS:** R2 (MÜHENDİS — kadrajda bot ve bacak; suit kimliği kilitler)

_"Botuyla eziyor. Geçiyor."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  ⭐ ÇEHOV 3 BURADA KURULUYOR. Filmin en pahalı ihmali: gemi şu anda
     zemine kök salmaya başladı ve bunu gören adam önemsemedi.
     Ateşleme: S74 — gemi kabuk içinde.
  ⚠️ Kabartı EZİLDİKTEN SONRA 10 saniye içinde GERİ KABARMAZ —
     kopyalama saatler ölçeğinde işler; anlık büyüme yazmak Novum'un
     zaman kuralını bozar [00_PLAN kopyalama süreleri].
  ⭐ Kadrajda yüz yok — bot, bacak, suit. Kimlik yükü minimum.
```

### 📸 IMAGE PROMPT

```
SCENE:
At the foot of a crashed ship's landing leg at night, the ground has
swelled into a low raised outline — the exact shape of the foot pad
that rests beside it.

ENVIRONMENT:
The base of the collapsed RIGHT landing leg of a grounded cargo ship
at night: a heavy dark strut angling down into a wide flat foot pad
half-sunk in grey dust. Dark basalt ground around it, hairline
fractures, settled dust. The tilted hull rises out of focus above; one
large pale moon upper LEFT at 7000K; a hard white helmet-lamp pool
lights the ground from frame right.

SUBJECT:
No faces. In the center of frame, beside the foot pad, the ground
itself: a low, smooth swelling raised two knuckles high out of the
dust, tracing the pad's outer outline — the same curve, the same
straight edge, offset a hand's width from the metal. It looks neither
dug nor piled: the surface is continuous, as if the ground had risen
from beneath. At frame RIGHT, the lower leg and heavy boot of a
33-year-old man flight engineer stand in the lamp light — dark grey-
blue suit shin with TEAL GREEN worn reinforcement at the knee, scuffed
boot sole flat on the dust.

CAMERA:
Shot on a 100mm lens from a fixed position one point five meters away,
low, just above ground level, f/4 — pad, swelling and boot all sharp.
True scale: the swelling reads small, easy to dismiss.

LIGHTING:
Night. Hard white helmet-lamp pool from frame right rakes the swelling
into clear relief; grey-blue 7000K moonlight fills faintly from the
upper LEFT. Long micro-shadows on the dust.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one partial
figure — boot and shin only, no second person. The swelling does not
move, grow, crack, open or glow in this frame; no veins, no light from
below. Reinforcement stays TEAL GREEN. Boot keeps a clear boundary
against the ground. No bloom, no glow filter, no lens flare. No
readable text or digits; no captions, no HUD, no watermark. No bare
head. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 100mm, fixed lockoff one point five meters away,
low above ground level, no cuts, no camera movement:

SETUP: the camera is locked off just above the ground at the foot of
the collapsed right landing leg, f/4 — the wide foot pad, the raised
outline in the dust beside it, and a man's boot at frame right, all
sharp. It never moves for the whole ten seconds. FRAME: night. The
heavy strut and half-sunk foot pad of the landing leg; beside the pad,
a low smooth swelling two knuckles high, tracing the pad's outline in
the grey dust. At frame RIGHT, the shin and boot of a 33-year-old man
flight engineer — dark grey-blue suit, TEAL GREEN worn reinforcement
at the knee, scuffed sole. Hard white helmet-lamp light from frame
right, grey-blue 7000K moonlight from the upper LEFT.

0s — The swelling sits still in the raking lamp light, its curve
matching the pad's edge exactly. The boot stands flat.
2s — The boot lifts, moves over the swelling and comes down on it — a
full, weighted step that flattens the near half back into the dust.
4s — The boot grinds once, a short quarter-twist under weight,
crushing the rest flat. Fine dust squeezes out from under the sole and
settles at once.
6s — The boot lifts away and sets down beyond the frame edge; the
flattened ground holds its new shape — pressed, cracked dust, nothing
more.
8s — The frame holds on the flattened patch and the untouched foot
pad. Nothing rises. Nothing moves.
10s — Still frame to the end: pad, pressed dust, silence. No cuts.

The flattened ground NEVER re-swells, never breathes, never cracks
open, never glows — within these ten seconds it stays exactly as the
boot left it. Dust squeezed from under the sole falls and settles at
once, never hovers. Only one partial figure appears — boot, shin,
nothing more; no face, no second person. Reinforcement stays TEAL
GREEN. The boot keeps a clear boundary — never merges with the ground.
Camera locked: no cuts, no transitions, no shake, no zoom, no push-in.
No bloom, no glow filter, no lens flare. No readable text or digits;
no captions, no HUD, no watermark. Exactly one figure in frame — no
duplicates, no second person. No bare head. Photorealistic, 35mm
anamorphic film grain.
```

---

## 🎬 SAHNE 29 — UFUKTAKİ SİLUET

`4:40 – 4:50` · 32mm · kadro 1 · yavaş tilt · **A yolu**
📎 **REFERANS:** R1 (KAPTAN — sırttan; suit kimliği kilitler)

_"Aynı sınıf. Aynı biçim."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: yavaş yukarı tilt —
  zeminden ufka.
  İŞLEV: ilk gerçek tuhaflık. Bir enkaz sahasında hiçbir şey dik
  durmaz — ufuktaki siluet DİK duruyor. Ve tanıdık.
  ⭐ Siluet CANTOR'un kendi biçimidir (kutu gövde, dar burun) ama
     MAT KEMİK GRİSİ ve dimdik. "Ama CANTOR burada." tuhaflığı
     seyircinin kafasında kurulur, kimse söylemez.
  ⭐ Siluet IŞIK YAYMAZ [Ders 3/29]: sadece ay ışığını yansıtır.
  🎞️ END FRAME alır (tilt ufka varmış olur).
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
At the start of a slow upward tilt at night: the dusty ground before a
standing woman's boots, her long moon-shadow reaching toward the dark
horizon.

ENVIRONMENT:
Dark basalt plain at night, fine settled dust, hairline fractures. One
large pale moon upper LEFT at 7000K throws a long, soft-edged human
shadow diagonally across the frame from the boots at the bottom edge.
Scattered small angular pebbles sit half-buried in the dust, each
dragging its own long thin shadow. Near-black sky not yet in frame;
the dark plain runs away into haze.

SUBJECT:
At the bottom edge of frame, the boots and lower shins of a 41-year-
old woman pilot, seen from behind — dark grey-blue pressure suit legs
with ORANGE worn reinforcement at the knees, scuffed boots planted a
shoulder-width apart in the dust. Her lamp is off; only moonlight
shapes the scene. The dust around her boots is unmarked except for the
twin print trails arriving from off frame. The rest of the frame is
ground: grain, fracture lines, and the long shadow pointing at the
unseen horizon.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position two meters behind
her at hip height, tilted DOWN toward the ground at the start of the
move. Physically accurate perspective, true human scale.

LIGHTING:
Night. Grey-blue 7000K moonlight from the upper LEFT, hard and low,
raking the dust; the shadow deep and soft-edged. No other source —
helmet lamps off.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one partial
figure — boots and shins from behind, no face, no second person.
Reinforcement stays ORANGE. Nothing on the ground moves, glows or
swells. No bloom, no glow filter, no lens flare. No readable text or
digits; no captions, no HUD, no watermark. No bare head.
Photorealistic, 35mm anamorphic film grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
At the end of the slow upward tilt: past the woman's shoulder, on the
far night horizon, a ship stands UPRIGHT — the same familiar boxy
class as her own, but bone-grey and perfectly still.

ENVIRONMENT:
Dark basalt plain running to a distant horizon under a near-black sky;
one large pale moon upper LEFT at 7000K; thin haze low over the
ground. The plain between is empty — no wreck, no rock large enough to
read.

SUBJECT:
Over the right shoulder of a 41-year-old woman pilot seen from behind
— helmet, shoulder and back in the near frame, dark grey-blue suit
with ORANGE worn reinforcement, dark brown low bun visible through the
transparent visor's edge — the horizon carries one small, distinct
silhouette: a boxy cargo ship of the same class as her own, narrow
bow, twin aft bays, standing perfectly UPRIGHT on the flat plain. It
is matte bone-grey, a single tone, carrying no stripe, no marking, no
window light, no colour of any kind. It does not lean, and nothing
around it explains how it stands.

CAMERA:
Shot on the same 32mm anamorphic lens from the same position two
meters behind her, now level at shoulder height, her figure on the
left third, the silhouette small on the horizon right of center. True
scale: the distant ship reads kilometers away.

LIGHTING:
Night. Grey-blue 7000K moonlight from the upper LEFT; the silhouette
is lit only by that moon — a pale grey shape against darker sky,
reflecting light, never emitting it.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one figure in
the near frame; the distant shape is a ship silhouette, not a person.
The silhouette never glows, never shows lit windows, never moves.
Reinforcement stays ORANGE; the visor stays a distinct glass surface.
No bloom, no glow filter, no lens flare. No readable text or digits;
no captions, no HUD, no watermark. The visor stays clear, uncoated
glass — no tint, no mirror coating, no reflection that hides what is
behind it. No bare head. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, one slow upward tilt from a
fixed position two meters behind the woman, no cuts:

SETUP: the camera stands fixed at hip height behind a standing woman
and performs ONE continuous, constant-rate upward tilt for the whole
ten seconds — from the ground at her boots up past her shoulder to the
far horizon. No dolly, no pan, no zoom, no shake. FRAME: night on a
dark basalt plain. One large pale moon upper LEFT at 7000K. A 41-year-
old woman pilot from behind — dark grey-blue pressure suit, ORANGE
worn reinforcement, integrated helmet with transparent visor, dark
brown low bun, helmet lamp off. Fine dust, hairline fractures, her
long soft moon-shadow.

0s — The frame holds her boots and the dust, her shadow running ahead
of her. The tilt begins, slow and even.
3s — The tilt climbs her suit legs and back; the plain opens out
beyond her, empty and moonlit, haze low at its far edge.
6s — Her shoulder and helmet enter the lower frame; on the horizon,
right of center, a small pale silhouette rises into view: a boxy cargo
ship, standing perfectly upright.
8s — The tilt eases to a stop at shoulder height: the silhouette sits
clear on the horizon — same class as her own ship, matte bone-grey,
single-toned, windowless, motionless, upright.
10s — The frame holds: her still figure on the left, the standing grey
twin far ahead. She does not move. No cuts.

The tilt runs at one constant rate and stops once — it never reverses,
never overshoots, never becomes a zoom. The distant silhouette never
moves, never lights up, never emits: it reflects moonlight only, matte
bone-grey, no stripe, no marking, no window glow. The woman stays
still throughout: no step, no turn, no speech. Reinforcement stays
ORANGE; the visor stays a distinct glass surface. Exactly one figure.
No cuts, no transitions, no shake. No bloom, no glow filter, no lens
flare. No readable text or digits; no captions, no HUD, no watermark.
The visor stays clear, uncoated glass — no tint, no mirror coating, no
reflection that hides what is behind it. No bare head. Photorealistic,
35mm anamorphic film grain.
```

---

## 🎬 SAHNE 30 — FAZ KAPANIŞI: EŞİK

`4:50 – 5:00` · 32mm · kadro 2 · yavaş pull-back · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan, sırttan) + R4/S19-END (gemi kadraj kenarında)

_"Yürümeye başlıyorlar."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: yavaş geriye açılma
  (pull-back) — kamera yükselerek genişler.
  ▶ PERDE DÖNÜŞÜ 1 — EŞİK. Gemiden ayrılmak = eşiği geçmek. Bundan
    sonra hikaye hayatta kalma değil, ANLAMA hikayesi.
  ⚠️ KADRO BÜTÇESİ: `2` işaretli 23 sahnenin 8.'si.
  ⭐ BAĞLANTI → F4: yürüyüş kesilmez; S31 aynı yürüyüşü ŞAFAKTA devam
     ettirir (eylem sürekliliği + ışık geçişi). END FRAME kilitlenir.
  🎞️ END FRAME alır (kadraj genişlemiş, figürler küçülmüş).
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
Two suited figures walk away from their crashed ship into the night,
toward a distant upright silhouette on the horizon.

ENVIRONMENT:
Dark basalt plain at night, one large pale moon upper LEFT at 7000K,
near-black sky. At the LEFT edge of frame, the stern of the grounded
31-meter cargo courier: tilted exactly 4 degrees right, collapsed
right leg, faint amber cockpit spill. Ahead, far on the horizon right
of center, the small bone-grey silhouette of an upright ship of the
same class. Fine dust, long soft moon-shadows.

SUBJECT:
Exactly two figures seen from behind, mid-stride, a meter apart,
already ten meters from their ship. LEFT: a 41-year-old woman pilot,
1.68 m, slim — dark grey-blue pressure suit with ORANGE worn
reinforcement, integrated helmet, dark brown low bun behind the
transparent visor. RIGHT: a 33-year-old man, 1.81 m, broad-shouldered
— TEAL GREEN reinforcement, oversized back tool module. Orange for
her, teal for him, never swapped; his helmet rides 13 cm higher.
Helmet lamps on, two cones ahead of them; two clean boot-print trails
behind them in the dust.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position six meters behind
them at head height, at the start of a slow rising pull-back. True
human scale between the 31-meter hull and the far horizon.

LIGHTING:
Night. Grey-blue 7000K moonlight from the upper LEFT; two hard white
lamp cones on the dust ahead; the amber cockpit spill warm at the
frame's left edge.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly two figures.
Orange stays on the woman, teal on the man; no morphing, no face swap.
Visors stay clear, uncoated glass — no tint, no mirror coating, no
reflection that hides what is behind them. The distant silhouette
never glows or moves. Ship damage stays fixed. Dust settles, never
hovers. No bloom, no glow filter, no lens flare. No readable text or
digits; no captions, no HUD, no watermark. No bare head.
Photorealistic, 35mm anamorphic film grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
The same walk ten seconds later, seen from higher and farther back:
two small lit figures on a vast dark plain, their crashed ship
shrinking at the frame's edge, the upright silhouette waiting on the
horizon.

ENVIRONMENT:
The dark basalt plain opened wide by the risen camera: the grounded
courier now small at the lower LEFT, its 4-degree tilt and amber
cockpit spill still readable, the 60-meter drag groove running to it.
The horizon higher in frame; the bone-grey upright silhouette still
small, right of center. One large pale moon upper LEFT, near-black
sky, thin low haze.

SUBJECT:
The same two figures, now farther into the plain and smaller in frame,
still mid-stride, a meter apart: the woman with ORANGE worn
reinforcement on the left, the man with TEAL GREEN reinforcement and
the oversized back module on the right, his helmet 13 cm higher. Two
helmet-lamp cones sweep the dust ahead of them; their double boot-
print trail runs back toward the ship. No other mark disturbs the
plain between them and the horizon.

CAMERA:
Shot on the same 32mm anamorphic lens, now eleven meters behind and
three meters above the ground, looking slightly down the line of their
walk — the end of one continuous rising pull-back. True scale: figures
small, world large.

LIGHTING:
Night, unchanged. Grey-blue 7000K moonlight from the upper LEFT; lamp
cones ahead of the figures; amber spill at the distant ship.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly two figures.
Orange stays on the woman, teal on the man. The distant silhouette
never glows or moves. Ship damage fixed: hole, collapsed leg, 4-degree
tilt, groove. No bloom, no glow filter, no lens flare. No readable
text or digits; no captions, no HUD, no watermark. No bare head.
Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, one slow rising pull-back from
six to eleven meters behind two walking figures, no cuts:

SETUP: the camera starts six meters behind two walking figures at head
height and pulls straight back and gently up for the whole ten seconds
— one continuous, constant-rate move to eleven meters back and three
meters up. No pan, no tilt beyond the rise, no zoom, no shake. FRAME:
night on a dark basalt plain, one large pale moon upper LEFT at 7000K.
LEFT edge: the grounded 31-meter courier, tilted exactly 4 degrees
right, faint amber cockpit spill. On the far horizon, right of center,
a small upright bone-grey ship silhouette. Two suited figures from
behind: the woman, 1.68 m, ORANGE worn reinforcement, dark grey-blue
suit; the man, 1.81 m, broad-shouldered, TEAL GREEN reinforcement,
oversized back module. Helmet lamps on.

0s — They walk away from camera in step, lamp cones ahead, boot prints
unrolling behind them. The pull-back begins.
3s — The frame widens; their ship's stern slides fully into the left
edge, tilted and dim. They do not look back.
6s — Rising, the camera opens the plain: the drag groove, the double
print trail, the empty dark between them and the horizon silhouette.
8s — The figures are small now, two moving points of lamp-light on a
vast floor of moonlit dust, the upright silhouette holding its place
far ahead.
10s — The pull-back eases to a stop; they keep walking away inside the
still frame. No cuts.

The two figures never stop, never turn around, never speak; their pace
stays even, their boot falls soft under 0.9g, raised dust settling at
once. Orange stays on the woman, teal on the man; the height
difference holds; no morphing. The distant silhouette never moves,
never lights, never grows faster than the walk explains. The ship's
damage stays fixed. Exactly two figures. One constant-rate pull-back
only: no cuts, no transitions, no shake, no zoom, no speed ramp. No
bloom, no glow filter, no lens flare. No readable text or digits; no
captions, no HUD, no watermark. No bare head. Photorealistic, 35mm
anamorphic film grain.
```

---

# ✅ FAZ 3 DENETİM TABLOSU

| # | Lens | Kadro | Hareket | 10s yolu | Diyalog | İmaj | Risk |
|---|---|:---:|---|:---:|:---:|:---:|---|
| S21 | 32mm | **2** | yavaş push-in | A | — | 1 | yüz karışması · toz fiziği [D12] |
| S22 | 85mm | 1 | lockoff | A | — | 1 | **çıplak el anatomisi** [D11] |
| S23 | 50mm | **2** | lockoff | A | 1 replik | 1 | hasar abartma [D38] · dudak [D35] |
| S24 | 50mm | 1 | lockoff | A | — | 1 | çanak/radar klişesi · el-yüzey [D43] |
| S25 | 85mm | 1 | push-in | A | 1 replik | 1 | dudak senkron [D35] · korku imzası |
| S26 | 32mm | **2** | lockoff | A | — | 1 | zemin tepkisi sızması (yasak) |
| S27 | 100mm | 0 | lockoff | B | — | 1 | çift vuruş / dalga sızması |
| S28 | 100mm | 1 | lockoff | A | — | 1 | geri kabarma (yasak) · bot-zemin [D11] |
| S29 | 32mm | 1 | yavaş tilt | A | — | 2 | siluet parlaması [D3/29] |
| S30 | 32mm | **2** | pull-back | A | — | 2 | geçiş çapası → S31 · figür küçülünce yüz bozulması |

```
KADRO DENETİMİ
  `2` işaretli sahne: 4 (S21, S23, S26, S30) — F3 bütçesi TAM ✅
  Film geneli `2` sayacı: 8 / 23 kullanıldı (S5 S8 S12 S16 S21 S23 S26 S30)
  Üç figürlü sahne: 0 / 5 ✅   Bekçi: bu fazda YOK ✅

SÜRE DENETİMİ
  10 sahne × 10.0 s = 100 s = 1:40 · S21 başlangıcı 3:20 ✅ FAZ TAM

ÇEHOV DENETİMİ
  ÇEHOV 7 (eldiven ritüeli)   → S22'de kuruldu ✅ (ateşleme: S80-S81)
  ÇEHOV 5 (imdat çağrısı)     → S25'te kuruldu ✅ (ateşleme: S58)
  ÇEHOV 3 (kabaran zemin)     → S28'de kuruldu ✅ (ateşleme: S74)
  GİRDAP SAATİ (dakikada 4)   → S27'de başladı ✅ (hızlanma: S76)
  HAREKET İMZASI 2. tekrar    → S25'te ✅ (S9 → S25 → S81)
  SİLUET (dik ikiz)           → S29'da görüldü ✅ (çözülme: F4 tarla)
  PERDE DÖNÜŞÜ 1              → S30'da ✅ (eşik geçildi)
```

---

# ⏭️ SONRAKİ ADIM

```
✅ Faz 3 TAM — 10 sahne · 12 imaj · 10 video promptu
→ ../FAZ_04_TARLA/FAZ_04_TARLA.md (S31–S40) · S31, S30'un yürüyüşünü
  ŞAFAKTA sürdürür (eylem sürekliliği + ışık geçişi: gece → 4400K)
□ Üretim sonrası: her sahnenin PLAN beati kurguda okunuyor mu
   [Ders 68 ③ — süre değil, BEAT sayılır]
```
