# 🛰️ THE SECOND SHIP — FAZ 1 / TRANSİT · KISIM 1

## S1–S10 PROMPTLARI | 0:00 – 1:40 | Perde I | 16:9 Yatay
### _"Cevap veren herkes ölür."_

> **Bu dosya ADIM 4'tür** — `REFERANS_PAKETI.md` (ADIM 3) kilitlendikten
> sonra yazılan ilk prompt dosyası.
> Plan: `00_PLAN.md` · Bible + sahne haritası: `README.md` ·
> Anlatı akışı: `01_SENARYO.md` · Ses: `MUZIK_VE_SES.md`
>
> ✅ **KAPSAM: S1–S10 TAM.** 05.08.2026 revizyonu: film 10 faz × 10
> sahne = 100 sahne = 16:40; eski S3 ve S11 kesildi, numaralar kaydı
> (eşleme tablosu: `../01_SENARYO.md` başında). S10, F2'ye ışık
> geçişini kurar — `../FAZ_02_VURULMA/FAZ_02_VURULMA.md` o geçişten
> açılır.
>
> ⛔ Her prompt **self-contained**'dır (AGENTS.md kural ③). Hiçbir prompt
> "BIBLE'a bak" demez; kıyafet ve yüz tarifi her sahnede tam tekrarlanır.
> Uzunluk bandı (README §6): **imaj 1.700–2.100 · video 2.000–2.600**
> karakter. On sahnenin 22 promptu da bu bandın içindedir.

---

# 📎 REFERANS LEJANDI — sahne kartlarındaki "REFERANS" satırı

```
R1  = KAPTAN master           REFERANS_PAKETI.md · REFERANS 1
R2  = MÜHENDİS master         REFERANS_PAKETI.md · REFERANS 2
R3  = BEKÇİ master (mühürlü)  REFERANS_PAKETI.md · REFERANS 3
R4  = CANTOR dış (hasarlı)    REFERANS_PAKETI.md · REFERANS 4
R4b = CANTOR dış (hasarsız)   R4 promptundan DAMAGE STATE paragrafı
                              çıkarılarak üretilir (S1–S11 dönemi)
yok = kadro 0 / soyut sahne — referans imaj EKLEMEDEN üret

KURAL: sahneyi üretirken satırda yazan referans imaj(lar)ını Flow'a
"malzeme/ingredient" olarak ekle. Prompt zaten self-contained —
referans metni değil, KİMLİĞİ kilitler. İki insanlı sahnede iki master
birlikte eklenir; KARIŞMA KİLİDİ cümlesi promptta zaten gömülüdür.
Kokpit iç mekân çapası: fazın ilk üretilen kokpit karesi (S6) sonraki
kokpit sahnelerine start frame / malzeme olarak verilir.
```

---

# 🔒 FAZ KİLİTLERİ — S1–S100 boyunca geçerli, bu dosyada karara bağlandı

> Bu üç karar faz dosyalarında ilk kez burada veriliyor. Sonraki faz
> dosyaları bunları **tartışmaz, uygular.**

## KİLİT 1 — GEMİ İÇİNDE DE KASK TAKILIDIR

```
KARAR: Kokpit ve servis koridoru sahnelerinde (S3–S9, S12, S14–S16, S18)
       iki insan da kaskları TAKILI, vizör tam şeffaf hâlde görünür.

NEDEN (üç gerekçe, ikisi teknik biri anlatısal):
 ① REFERANS_PAKETI'ndeki dört çapa imajının üçü kasklıdır. 150 imajın
    tamamı o plakalardan üretilecek — kasksız kokpit sahnesi, kimlik
    çapasının dışına çıkan tek sahne grubu olurdu [Ders 55].
 ② Kask "sonradan belirirse" Ders 37 (ekipman durum geçişi) tetiklenir.
    Film hiçbir yerde kask TAKMA anını göstermiyor; kaskı baştan takılı
    tutmak bu geçişi tamamen ortadan kaldırır. Bedeli sıfır.
 ③ S14'te gövde deliniyor ve kargo bölmesi basıncını kaybediyor. İki
    insanın o sahnede zaten mühürlü olması, hayatta kalmalarını
    açıklayan tek şeydir. Karar anlatıyı da taşıyor.

UYGULAMA: "integrated helmet with a fully transparent, seamless visor;
the face reads clearly through the glass" cümlesi HER insan promptunda
aynen geçer [Ders 5]. Vizörde daima konsolun soluk amber yansıması var —
vizörün cam yüzey olarak okunmasını sağlayan tek işaret budur.
```

## KİLİT 2 — İNSAN DİYALOĞU YÜZ OKUNMAYAN KADRAJDA GEÇER

```
Bekçi'nin lip-sync riski sıfır (opak vizör). İnsanların DEĞİL —
vizör şeffaf ve ses post'ta ekleniyor [Ders 35 · Ders 40].

KURAL: bir insan konuşuyorsa sahne şu ikisinden biridir:
   (a) 50mm veya daha geniş, ≥3 m — ağız kadrajda küçük kalır
   (b) baş 3/4 çevrik / konsola dönük — ağız hattı okunmaz
85mm'de konuşan insan YOK. S8 85mm'dir ve orada ikisi de DİNLER.
S9'da Kaptan konuşur: başı konsola dönük yazıldı, ağız hattı kapalı.
```

## KİLİT 3 — 10 SANİYE NASIL ELDE EDİLİYOR (README §1b, sahne bazında)

```
A yolu = 8 s üret → extend → 10.00 s'ye kırp   (varsayılan)
B yolu = 8 s klibi optik akışlı 0.8× retime = 10 s (bedava)

FAZ 1 DAĞILIMI — sahne kartlarında da yazılı:
  B yolu (2 sahne):  S1 · S6  → kadrajda sadece toz/soyut ışık var
  A yolu (8 sahne):  S2 S3 S4 S5 S7 S8 S9 S10
  Gerekçe: B yolu insan hareketini ve kamera kaydırmasını da yavaşlatır;
  8 sahnenin 8'inde ya bir el ya bir kadraj ya bir ışık cephesi hareket
  ediyor — 0.8× orada ağır çekim olarak okunur [Ders 12 · Ders 44].
  (S10'un ışığı BÜYÜYOR; geçiş temposu S11'e bağlanır, retime edilmez.)
```

---

# 🎨 ÜRETİM SIRASI VE İMAJ BÜTÇESİ

```
S1–S10 = 10 video · 12 imaj  (S2 · S10 END FRAME imajı da alır —
kadraj içeriği 10 saniyede fiziksel olarak değişen iki sahne bunlar)

ÖNERİLEN SIRA (kolaydan zora, kimlik riski en sonda):
  1) S6  → tek soyut nesne, kadro 0. Kokpit malzemesinin testi.
  2) S1  → kadro 0, hareketsiz. Kule ölçek belirsizliğinin testi.
  3) S2 · S10 → dış/yörünge + tarama dili
  4) S3 → KAPTAN ilk yüz. ⛔ TETİK SAHNE [Ders 68]
  5) S4 → MÜHENDİS ilk yüz. ⛔ TETİK SAHNE
  6) S7 · S9 → tek kişilik kokpit
  7) S5 · S8 → iki insan aynı karede (fazın en pahalı iki sahnesi)

⛔ TETİK KAPISI [Ders 68 çözüm maddesi ②]: S3 ve S4 üretilip yüzler
   REFERANS_PAKETI plakalarıyla YAN YANA doğrulanmadan S5 ve S8
   üretilmez. İki insanlı sahnede kayan bir yüzü düzeltmek, tek
   insanlı sahnede düzeltmenin iki katına mal olur.

SES: on sahnenin onu da SESSİZ üretilir. Diyalog, anons ve DOKUMA
     girdabı post'ta (ElevenLabs + `MUZIK_VE_SES.md`).
```

---

## 🎬 SAHNE 1 — HOOK: DİK ÇİZGİ

`0:00 – 0:10` · 32mm · kadro 0 · fixed lockoff · **B yolu (retime)**
📎 **REFERANS:** yok — kadro 0; ölçeksiz gece düzlüğü, referans imaj EKLEME (ölçek sızdırır)

_"Ne olduğu belli değil — ve bu yüzden bırakamıyorsun."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera hiç hareket etmez.
  İŞLEV: filmin sorusu ilk saniyede sorulur ve cevaplanmaz.
  Bu çizgi Kule'dir (400 m) — seyirci bunu S48'de öğrenecek.
  ⭐ SAHNENİN TEK KURALI: ÖLÇEK OKUNMAMALI. Kadrajda boyu bilinen
     hiçbir nesne olamaz — gemi, figür, ışık, krater, kaya yok.
     Zemin dokusu bilerek ölçeksiz: eşit, ince, tekrarlı grain.
```

### 📸 IMAGE PROMPT

```
SCENE:
Opening frame of a film. The night side of a rocky planet: one
flawless white vertical line stands on a dark textured surface, and
nothing in frame explains how large it is.

ENVIRONMENT:
A dark basalt plain in deep night, seen from far away. The ground is
an even, fine, repeating grain with no landmark, no crater and no
object of known size anywhere. Dust lies settled. The sky is
near-black; one large pale moon hangs high, small and cold.

SUBJECT:
A single perfectly straight white vertical line rising from the
ground in the middle third of frame — seamless, uniform in width,
narrowing almost imperceptibly as it rises, its top passing out of
the upper frame edge. Smooth pearl-white, with no panel line, no
seam, no window, no marking and no light of its own. It meets the
ground in one clean unbroken contact edge: no rubble, no foundation,
no dust piled against it.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position far away, at eye
level with the horizon, framed so the viewing distance stays
deliberately unreadable. The line is perfectly plumb in frame.

LIGHTING:
Night. One large pale moon at 7000K, very low in level, rakes from
the LEFT. The ground reads in near-silhouette with faint texture; the
line carries an even soft sheen down its left face and deep grey on
its right — reflected light only, never emitted.

PHYSICS:
0.9g. Nothing moves but a thin weak drift of low dust across the base
of frame. Dust falls and comes to rest, never hovers.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly zero figures — no people, no vehicle, no ship, no creature,
no structure but the single line. No object of known size anywhere:
no rocks, no craters, no lights, no debris that could read as scale.
The line never glows, never emits, never pulses. No bloom, no glow
filter, no lens flare. No readable text, letters, digits or symbols;
no captions, no title card, no watermark. The ground is static.
Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts, no camera movement:

SETUP: 32mm anamorphic lens, fixed lockoff far away, eye level with
the horizon, camera absolutely still for the entire ten seconds.
FRAME: the night side of a rocky planet. A dark basalt plain of even
fine grain fills the lower two thirds; near-black sky with one large
pale grey-blue moon high in frame; one flawless white vertical line
stands in the middle third, seamless and uniform, its top leaving the
upper frame edge, its base meeting the ground in one clean contact
edge. Moonlight rakes from the LEFT at 7000K, very low level.

0s — The frame is completely still. The white line reads as an even
soft sheen on its left face, deep grey on its right; the plain is
almost silhouette.
3s — A thin, weak veil of low dust drifts slowly across the base of
frame from left to right, no more than a hand's width of the image,
grain-textured and dry. The line does not change.
6s — The dust veil thins and begins to settle back toward the
ground. The horizon haze breathes very faintly. Nothing else moves.
8s — The last dust comes to rest. The line is exactly as it was at
0s, same width, same brightness, same position, perfectly plumb.
10s — Absolute stillness holds to the final frame. No cuts.

The white line never moves, never grows, never shortens, never
glows, never pulses. It is lit only by moonlight and emits nothing.
The ground is static: nothing rises from it, nothing sinks into it.
Sound exists but is muffled and low — thin atmosphere, not vacuum.
Exactly zero figures in frame. No object of known size enters frame
at any second — no ship, no light, no debris, no creature. No cuts,
no transitions, no camera shake, no zoom, no push-in. No bloom, no
glow filter, no lens flare. No readable text, letters, digits or
symbols; no subtitles, no captions, no title card, no watermark.
All dust obeys 0.9g, falls and comes to rest, never hovers, never
swirls, never flows like liquid. Photorealistic, 35mm anamorphic
film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 2 — DÜNYANIN KURALI

`0:10 – 0:20` · 32mm · kadro 0 · çok yavaş yanal kaydırma · **A yolu**
📎 **REFERANS:** yok — kadro 0; yörünge deseni, referanssız üret

_"Hepsi ikişer."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: çok yavaş yanal kaydırma.
  İŞLEV: Novum'un ilk ipucu bilinçaltına bırakılıyor. Kimse fark
  etmiyor, kimse söylemiyor — kadraj da vurgulamıyor.
  ⭐ KRİTİK: enkaz alanları IŞIK YAYMAZ. Ay ışığını yansıtan soluk gri
     lekelerdir [Ders 3/29]. Çift olan lekeler birbirinin AYNISI —
     aynı hat, aynı boy, farklı olgunluk.
  🎞️ END FRAME imajı alır (kadraj 10 saniyede kayıyor).
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
A downward view of a planet's night surface from high above: hundreds
of small pale patches lie scattered on dark ground, and most of them
are not single but PAIRED.

ENVIRONMENT:
The night side of a rocky planet from high altitude, the ground
filling the frame with no horizon and no sky. Dark basalt plains cut
by wide shallow valleys and dry fracture lines, with hundreds of
small pale grey patches scattered across them — old wreck fields.

SUBJECT:
No figures, no vehicle, no active object. The subject is the pattern
itself: most patches are not alone but sit in PAIRS, and each pair
holds two patches of identical outline and identical length, set a
short distance apart on the same axis, one slightly more complete
than the other. A few pairs show one full shape beside a shape that
is only a raised outline swelling from the ground. All of it is matte
bone-grey stone, dusted, half sunk, with no colour of its own.

CAMERA:
Shot on a 32mm anamorphic lens looking straight down from very high
altitude, wide enough that dozens of patches read at once. True
altitude falloff — never a miniature or a tabletop model.

LIGHTING:
Night. One large pale moon lights the surface from the LEFT at 7000K,
very low in level. Every patch is lit only by that moonlight and
throws a long soft-edged shadow to the right. Nothing emits light.

PHYSICS:
0.9g. The surface is completely static. Dust lies settled. No growth,
no movement, no change of any kind within the frame.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly zero figures — no people, no ship, no creature, no active
machinery. The patches never glow, never emit, never shimmer, never
pulse; matte bone-grey stone only, never the colour of an original.
Growth is never visible in real time; the ground is static. No city,
no road, no building, no geometric grid — these are scattered wrecks,
not a settlement. No bloom, no glow filter, no lens flare. No
readable text, letters, digits or symbols; no captions, no HUD, no
map overlay, no watermark. Photorealistic, 35mm anamorphic grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
The same downward view of the same night surface, the frame slid a
short distance to the LEFT along the same axis after ten seconds.

ENVIRONMENT:
The night side of a rocky planet from very high altitude, ground
filling the whole frame, no horizon and no sky. Dark basalt plains,
wide shallow valleys, dry fracture lines. A new stretch of plain has
entered from the left edge and carries the same scatter of small pale
grey patches; the clusters that opened the shot now sit near the
right edge. Thin atmosphere, faint haze in the deepest valleys.

SUBJECT:
No figures, no vehicle, no active object. Again the pattern: most
patches sit in PAIRS of identical outline and identical length on a
shared axis, one member slightly more complete than the other, and at
least one pair where the second member is only a raised outline
swelling from the stone. Matte bone-grey, dusted, half sunk, carrying
no colour of an original, no marking and no light.

CAMERA:
Shot on a 32mm anamorphic lens looking straight down from the same
very high altitude, same framing width, dozens of patches in frame.
Physically accurate perspective and true altitude falloff — never a
miniature or a tabletop model.

LIGHTING:
Night, unchanged. One large pale moon from the LEFT at 7000K, very
low in level; every patch throws a long soft-edged shadow to the
right. Nothing in frame emits light.

PHYSICS:
0.9g. The surface is completely static. Dust lies settled. No growth,
no movement, no change within the frame.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly zero figures — no people, no ship, no creature, no active
machinery. The patches never glow, never emit, never shimmer, never
pulse; matte bone-grey stone only, never the colour of an original.
Growth is never visible in real time. No city, no road, no building,
no geometric grid. No bloom, no glow filter, no lens flare. No
readable text, letters, digits or symbols; no captions, no HUD, no
map overlay, no watermark. Photorealistic, 35mm anamorphic grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, one very slow lateral track,
no cuts:

SETUP: the lens looks straight down at a planet's night surface from
very high altitude. The camera slides sideways to the LEFT at a
constant, extremely slow rate for the whole ten seconds — no other
movement, no tilt, no roll, no zoom, no altitude change.
FRAME: dark basalt plains with wide shallow valleys and dry fracture
lines, filling the frame with no horizon and no sky. Hundreds of
small pale grey patches lie scattered across the stone, most of them
in PAIRS: two patches of identical outline and identical length on a
shared axis, one slightly more complete than the other. One large
pale moon lights everything from the LEFT at 7000K, very low level;
every patch throws a long soft-edged shadow to the right.

0s — The plain is still. Several pairs sit in the middle of frame,
each twin matching its partner in shape and length.
3s — The slow leftward slide carries new ground in from the left
edge: another cluster, again paired, again matched.
6s — A pair enters where one member is complete and the other is
only a raised outline swelling from the stone — the same shape,
unfinished. The camera does not stop, does not push in on it.
8s — More paired patches pass. The first clusters approach the right
edge of frame.
10s — The slide continues at exactly the same rate to the final
frame, more pairs entering left. No cuts.

Nothing in frame emits light: every pale patch is lit only by
moonlight, matte bone-grey stone, never glowing, never shimmering,
never carrying the colour of an original. Growth is never visible in
real time — no patch changes shape, rises or completes itself during
the shot; the ground is static. Exactly zero figures, zero ships,
zero active machinery. Constant-rate lateral track only: no cuts, no
transitions, no camera shake, no zoom, no tilt, no speed ramp. No
bloom, no glow filter, no lens flare. No readable text, letters,
digits or symbols; no subtitles, no captions, no HUD, no map overlay,
no targeting graphic, no watermark. Photorealistic, 35mm anamorphic
film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 3 — KAPTAN

`0:20 – 0:30` · 85mm · kadro 1 · çok yavaş push-in · **A yolu**
📎 **REFERANS:** R1 (KAPTAN master) — Flow'a REFERANS 1 imajını ekle

_"Yorgun ama sakin bir yüz."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: 1.6 m → 1.2 m push-in.
  İŞLEV: yetkinlik sessizlikle kuruluyor. Konuşmuyor, konuşması
  gerekmiyor. Bakışı ekranda, ilgisiz.
  ⛔ TETİK SAHNE [Ders 68 ②]: bu sahne üretilip yüz REFERANS 1
     plakasıyla yan yana doğrulanmadan S5 ve S8 üretilmez.
  ⭐ KİLİT 2 gereği burada KONUŞMA YOK — 85mm'de ağız okunuyor.
```

### 📸 IMAGE PROMPT

```
SCENE:
Close on a woman pilot's face in the cockpit of a small cargo ship,
her eyes on a display off to the side, her expression unreadable.

ENVIRONMENT:
The cramped cockpit of a two-crew cargo courier in shallow focus
behind her: dark grey-brown panelling, exposed pipe runs, grey repair
patches, consoles carrying abstract light only. Black window beyond.

SUBJECT:
A 41-year-old woman pilot in a tight three-quarter close-up from her
left: a naturally beautiful, symmetrical face with high cheekbones,
light olive skin, sharp jawline, thin lips, dark grey-green eyes, a
fine faded white scar splitting her LEFT eyebrow in two, no makeup,
two faint lines across her forehead, dark brown hair in a tight low
bun with silver strands at the temples. Dark grey-blue pressure suit
with ORANGE worn reinforcement at the shoulder; integrated helmet
with a fully transparent, seamless visor — her face reads clearly
through the glass and a soft amber console reflection slides across
it. Her eyes are off to frame right, calm and disengaged.

CAMERA:
Shot on an 85mm lens from a fixed position one point six meters away,
f/2.8, at eye level, shallow depth of field with the cockpit soft
behind her. Accurate perspective, no distortion.

LIGHTING:
Interior practical light only, pale amber at 2800K from console
strips below and to frame right, raking up across her cheekbone and
leaving her left side in soft shadow. Skin keeps its pore texture.

PHYSICS:
Normal interior gravity. Only breathing and a slow blink move.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly one figure — no second person, no reflected extra face. Her
face keeps identical bone structure and eye spacing — no morphing;
the scar stays on her LEFT eyebrow. Reinforcement stays ORANGE. The
visor stays a distinct glass surface and never vanishes. Her mouth
stays closed — no dialogue, no lip movement. No bloom, no glow
filter, no lens flare, no waxy skin. No readable text, digits or
symbols — abstract light only; no captions, no name label, no HUD,
no watermark. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 85mm, one very slow push-in from 1.6 to 1.2
meters, no cuts:

SETUP: a tight three-quarter close-up of a seated woman pilot from
her left, at eye level, f/2.8, the cockpit soft behind her. The
camera creeps forward at a constant, almost imperceptible rate for
the whole ten seconds. No pan, no tilt, no roll, no shake.
FRAME: a 41-year-old woman pilot — symmetrical face, high
cheekbones, light olive skin with visible pores, sharp jawline, thin
lips, dark grey-green eyes, a fine faded white scar splitting her
LEFT eyebrow, dark brown hair in a tight low bun with silver strands
at the temples. Dark grey-blue pressure suit with ORANGE worn
reinforcement at the shoulder; integrated helmet with a fully
transparent seamless visor, her face clear through the glass, a soft
amber console reflection sliding on it. Pale amber 2800K console
light rakes up from below frame right; black window beyond.

0s — She is completely still, eyes off to frame right on a display,
expression flat and unhurried. Only her breathing moves her chest.
3s — The push-in begins to read. Amber indicator light shifts very
slightly across the visor as a segment slides on the console below.
5s — She blinks once, slowly, and her eyes track a short distance
across the display and settle again. Her expression does not change.
8s — The push-in has closed to a tighter frame; the scar through her
left eyebrow and the pore texture of her skin now read clearly. She
does not look at the camera.
10s — She holds, still watching, still unimpressed. No cuts.

She never speaks: her mouth stays closed, no dialogue, no lip
movement, no jaw motion. Her face keeps identical bone structure, eye
spacing and nose shape from first frame to last — no morphing, no age
change. The scar stays on the LEFT eyebrow. Reinforcement panels stay
ORANGE. The visor stays a distinct transparent glass surface in every
frame and never disappears. Exactly one figure in frame — no second
person, no crew, no face reflected in the visor. Constant-rate
push-in only: no cuts, no transitions, no camera shake, no angle
change, no camera teleportation. No bloom, no glow filter, no lens
flare, no waxy skin, no airbrushing. All displays show abstract
sliding light only — no readable text, letters, digits or symbols.
No subtitles, no captions, no name label, no lower third, no HUD, no
lens data, no watermark. Photorealistic, 35mm anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 4 — MÜHENDİS

`0:30 – 0:40` · 50mm · kadro 1 · fixed lockoff · **A yolu**
📎 **REFERANS:** R2 (MÜHENDİS master) — Flow'a REFERANS 2 imajını ekle

_"Elleriyle düşünen adam."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: iki karakterin farkı ilk kez görülüyor — biri okur, biri
  dokunur. Bu fark S68'de birini ölüme, diğerini eve götürecek.
  ⛔ TETİK SAHNE [Ders 68 ②]: yüz REFERANS 2 plakasıyla doğrulanmadan
     S5 ve S8 üretilmez.
  ⭐ ALET YOK: kesici alet kılıfında KAPALI kalır. Bağlantıyı çıplak
     eldivenle çeviriyor — böylece Ders 37 (ekipman belirmesi) ve
     Ders 43 (aletin değdiği yeri eritmesi) riskleri devre dışı.
  ⭐ "Kulağını dayamak" kaskla yapılıyor: kaskın yan yüzünü boruya
     bastırıyor. KİLİT 1 bozulmadan beat korunuyor.
```

### 📸 IMAGE PROMPT

```
SCENE:
A man flight engineer works a pipe coupling with his gloved hands in
the narrow service corridor of a small cargo ship, listening to the
line through the side of his helmet.

ENVIRONMENT:
A cramped service corridor barely wider than a man's shoulders, both
walls dense with pipe runs, cable bundles, bolted covers and grey
repair patches. Dust and scratches everywhere; recessed strip lights
at knee height and above; readouts abstract only.

SUBJECT:
A 33-year-old man flight engineer, 1.81 meters tall, athletic and
broad-shouldered, filling the corridor, seen three-quarter from his
right: strong symmetrical features, light brown skin, short neat
three-day black stubble, dark brown eyes, a 2 cm shiny old burn scar
on his RIGHT cheekbone, very short dense black hair. Dark grey-blue
pressure suit with TEAL GREEN worn reinforcement, oversized back tool
module, closed cutting-tool sheath on his left hip, integrated helmet
with a fully transparent seamless visor. Both gloved hands grip a
ring collar on a horizontal pipe at chest height with a clear
boundary; his head is tilted so the SIDE of his helmet rests on it.

CAMERA:
Shot on a 50mm lens from a fixed position two point five meters away
down the corridor, f/4, at chest height. True 1.81-meter scale.

LIGHTING:
Interior practical light only, pale amber at 2800K from strips above
and at knee height. His visor carries a soft amber reflection.

PHYSICS:
Normal interior gravity. Hands press with visible weight.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly one figure — no second person, no reflected face. His face
keeps identical bone structure — no morphing; the burn scar stays on
his RIGHT cheekbone. Reinforcement stays TEAL GREEN. The visor stays
a distinct glass surface and never vanishes. No handheld tool
appears — the sheath stays closed, its tool stowed and invisible.
Hands never merge with or melt any surface; the pipe never deforms.
No bloom, no glow filter, no lens flare, no waxy skin. No readable
text or digits; no captions, no name label, no HUD, no watermark.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff two point five meters away,
no cuts, no camera movement:

SETUP: the camera is locked off down the length of a narrow service
corridor at chest height, f/4. It never moves for the whole ten
seconds.
FRAME: a 33-year-old man flight engineer, 1.81 m, athletic and
broad-shouldered, filling the corridor three-quarter from his right —
strong symmetrical features, defined jawline, light brown skin with
visible pores, short neat three-day black stubble, dark brown eyes, a
2 cm shiny burn scar on his RIGHT cheekbone, very short dense black
hair. Dark grey-blue suit with TEAL GREEN worn reinforcement on
shoulders, elbows and knees, oversized back tool module, closed
cutting-tool sheath on his left hip, integrated helmet with a fully
transparent seamless visor. Walls dense with pipe runs, cable
bundles, bolted covers and grey repair patches; pale amber 2800K
strip light from above and knee height.

0s — Both gloved hands are on a ring collar at chest height. He turns
it a quarter turn, slowly and with visible effort, shoulders loading
against the resistance.
3s — He stops, tilts his head and presses the SIDE of his helmet flat
against the pipe, holding completely still, listening through the
shell. His eyes go unfocused.
5s — He lifts his head off the pipe, takes the collar again and turns
it a short way further, a little harder this time.
8s — He lets go and lays the flat of one gloved palm across the pipe
for a moment, feeling it rather than looking at it.
10s — He takes the hand back and holds, satisfied. No cuts.

He never speaks: mouth closed, no dialogue, no lip movement. No
handheld tool ever appears — the sheath stays closed and its tool
stays stowed and invisible for every frame; no object materialises in
his hands. His fingers keep a clear boundary: hands never merge with,
sink into or melt a surface, and the pipe never deforms.
His face keeps identical bone structure and eye spacing from first
frame to last — no morphing; the burn scar stays on the RIGHT
cheekbone. Reinforcement stays TEAL GREEN. The visor stays a distinct
transparent glass surface and never disappears. Exactly one figure in
frame. Camera locked off: no cuts, no transitions, no shake, no zoom,
no push-in, no angle change. No bloom, no glow filter, no lens flare,
no waxy skin. All readouts show abstract sliding light only — no
readable text, letters, digits or symbols; no captions, no name
label, no HUD, no watermark. Photorealistic, 35mm grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 5 — İLK DİYALOG

`0:40 – 0:50` · 50mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan aynı karede) — iki master birlikte + KARIŞMA KİLİDİ promptta

_"Durmuyoruz."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: görev tanımı = filmin ilk kilidi. Bu rotada durmak yok.
  ⚠️ KADRO BÜTÇESİ: bu, `2` işaretli 23 sahnenin 1.'si. Faz 1'de iki
     tane var (S5, S8) — kısmın bütçesi tam doluyor.
  ⚠️ KARIŞMA KİLİDİ bloğu prompta gömülü (turuncu/teal + 13 cm).
  ⭐ KİLİT 2: 50mm · 3.5 m · ikisi de öne dönük → ağız kadrajda küçük.
     Replikler post'ta; dudak hareketi kısa ve düşük genlikli yazıldı.
  ⛔ S3 ve S4 doğrulanmadan üretilmez.
```

### 📸 IMAGE PROMPT

```
SCENE:
A woman pilot and a man flight engineer sit side by side in a cargo
ship cockpit on a routine course check, neither looking at the other.

ENVIRONMENT:
The cramped cockpit of a two-crew cargo courier seen from behind and
between the seats: dark grey-brown panelling, pipe runs, grey repair
patches, two worn seats, consoles carrying abstract light only. Black
window with the dark curve of a planet at the bottom edge; between
the seats a short abstract amber bar sits lit.

SUBJECT:
Exactly two figures. LEFT seat: a 41-year-old woman pilot, 1.68 m,
slim — high cheekbones, light olive skin, sharp jawline, dark
grey-green eyes, a fine faded white scar splitting her LEFT eyebrow,
dark brown hair in a low bun, dark grey-blue suit with ORANGE worn
reinforcement. RIGHT seat: a 33-year-old man, 1.81 m,
broad-shouldered — light brown skin, short three-day stubble, a 2 cm
burn scar on his RIGHT cheekbone, very short black hair, the same
suit with TEAL GREEN reinforcement and an oversized back tool module.
Orange for her, teal for him, never swapped; his head sits 13 cm
higher. Both helmeted, visors transparent, facing front.

CAMERA:
Shot on a 50mm lens from a fixed position three point five meters
behind and between the seats, f/4, at head height, both figures and
the window in frame. True scale.

LIGHTING:
Interior practical light only, pale amber at 2800K from the consoles
below, keying both faces from underneath.

PHYSICS:
Normal interior gravity. Both seated with weight.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly two figures — no third person, no duplicate, no reflected
face. Orange stays on the woman, teal on the man, never swapped; the
13 cm height gap holds. Her scar stays on her LEFT eyebrow,
his on his RIGHT cheekbone; neither face borrows the other's. Both
faces keep identical bone structure — no morphing, no face swap. Both
visors stay distinct glass surfaces and never vanish. No bloom, no
glow filter, no lens flare. No readable text or digits — abstract
light only; no captions, no name label, no watermark.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff three point five meters
away, no cuts, no camera movement:

SETUP: the camera is locked off behind and between the two cockpit
seats at head height, f/4. It never moves for the whole ten seconds.
FRAME: exactly two seated figures. LEFT seat, a 41-year-old woman
pilot, 1.68 m, slim — high cheekbones, light olive skin, dark
grey-green eyes, a fine faded white scar splitting her LEFT eyebrow,
dark brown hair in a tight low bun, dark grey-blue suit with ORANGE
worn reinforcement. RIGHT seat, a 33-year-old man flight engineer,
1.81 m, broad-shouldered — light brown skin, short three-day black
stubble, dark brown eyes, a 2 cm burn scar on his RIGHT cheekbone,
very short black hair, dark grey-blue suit with TEAL GREEN worn
reinforcement and an oversized back tool module. Both in integrated
helmets with fully transparent seamless visors, both facing forward.
Pale amber 2800K console light from below; black window ahead with
sparse hard stars and the dark planet curve at the bottom edge.

0s — Both sit still, facing their own consoles. She watches a slow
sliding segment; he moves one gloved finger along a control.
3s — She speaks a short line without turning her head, her lips
moving briefly and with small amplitude, eyes forward.
5s — He answers, also without turning, one short movement of the
mouth, then taps the control twice with a clear, weighted contact.
7s — She gives a single small nod. Neither of them looks at the
other at any point.
10s — Both settle back to their consoles and hold, the amber bar
between the seats steady. No cuts.

The two suits never swap colour: ORANGE stays on the woman, TEAL
stays on the man in every frame, and the 13 cm height difference
between their heads holds throughout. Her scar stays on her LEFT
eyebrow, his on his RIGHT cheekbone; neither face takes on the
other's features. Both faces keep identical bone structure, eye
spacing and nose shape from first frame to last — no morphing, no
face swap. Both visors stay distinct transparent glass surfaces and
never disappear. Exactly two figures in frame — no third person, no
duplicate, no reflected extra face. Camera locked off: no cuts, no
transitions, no shake, no zoom, no push-in, no angle change, no
camera teleportation. No bloom, no glow filter, no lens flare, no
waxy skin. All consoles show abstract sliding light only — no
readable text, letters, digits or symbols; no subtitles, no captions,
no name label, no lower third, no HUD, no watermark. Photorealistic,
35mm anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 6 — BORÇ ÇUBUĞU

`0:50 – 1:00` · 100mm · kadro 0 · fixed lockoff · **B yolu (retime)**
📎 **REFERANS:** yok — kadro 0 kokpit makro; bu karenin çıktısı sonraki kokpit sahnelerinin iç-mekân çapası olur

_"Neden buradalar."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: tek nesneyle tüm sosyoloji. Bu insanlar keşif için değil,
  BORÇ için uçuyor. Film bunu bir daha hiç yorumlamayacak —
  çarpma sonrasında da yanmaya devam edecek, S100'de kalkarken hâlâ yanacak.
  ⭐ KADRO 0 — iki insan kadrajın DIŞINDA. Koltuklar görünür,
     omuz/kol girmez.
  ⭐ RAKAM YOK [Ders 13]: çubuk soyut. 10 saniyede kısalma bir kıl
     payıdır; "geri sayım" gibi okunmamalı.
  ⭐ Bu, kokpit malzemesinin ilk testi — fazın İLK üretilen sahnesi.
```

### 📸 IMAGE PROMPT

```
SCENE:
A macro view of one small abstract amber bar of light on a worn
console between the two seats of a cargo ship cockpit.

ENVIRONMENT:
The console gap between two crew seats in a cramped cargo courier
cockpit. In sharp focus: a scuffed dark grey-brown console face, its
paint worn to bare metal along one edge, fine scratches, dust settled
in the seams, a bolted access cover. Behind it the padded flanks of
two worn seats fall into blur; beyond them the cockpit is dark.

SUBJECT:
No figures. Set into the console face, a single recessed slot roughly
twenty centimeters long holds one continuous bar of soft amber light,
filled from the left and dark on its right portion, with a clean
sharp boundary between lit and unlit. The light is a smooth
continuous strip: no divisions, no ticks, no marks, no graduations of
any kind. It sits slightly below the console surface so its own edge
casts a hairline shadow. Nothing else in frame is lit from within.

CAMERA:
Shot on a 100mm macro lens from a fixed position eighty centimeters
away, f/2.8, level with the console face, very shallow depth of field
so only the slot and the console face around it are sharp.

LIGHTING:
Interior practical light only. The amber bar at 2800K is the
brightest thing in frame and lights the scratched console face around
it with a soft, tight falloff. Everything beyond thirty centimeters
falls into darkness.

PHYSICS:
Normal interior gravity. Nothing moves in frame. Dust lies settled in
the seams.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly zero figures — no hand, no shoulder, no arm, no reflection of
a person anywhere. The amber bar carries no readable text, no
letters, no digits, no numerals, no percentage, no tick marks, no
scale, no graduations, no icon and no symbol: it is a plain
continuous strip of light. Nothing else in frame emits light. No
bloom, no glow filter, no lens flare, no starburst, no holographic
projection, no floating interface, no HUD, no gauge graphic. No
captions, no watermark. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 100mm macro, fixed lockoff eighty centimeters
away, no cuts, no camera movement:

SETUP: the camera is locked off level with a cockpit console face,
f/2.8, very shallow depth of field. It never moves, never breathes,
never racks focus for the whole ten seconds.
FRAME: a scuffed dark grey-brown console face between two worn crew
seats — paint worn to bare metal along one edge, fine scratches, dust
settled in the seams, a bolted access cover, protruding pipework
soft behind. Set into the face, a recessed slot about twenty
centimeters long holds one continuous strip of soft amber light at
2800K, lit from the left, dark on the right, with a clean sharp
boundary between the two. The seats fall away into blur; the rest of
the cockpit is dark. No people.

0s — Total stillness. The amber strip is the only light source in
frame, its sharp boundary standing a third of the way along the slot.
4s — The boundary creeps to the right by a hair's width — so little
that it reads as attention rather than movement. Nothing else
changes. The strip does not flicker, blink or pulse.
7s — A faint cold blue spill from an off-frame indicator brightens
very slightly along the top edge of the console, then steadies.
10s — The frame holds exactly as it began: the same scratched
console, the same settled dust, the same amber strip, its boundary a
hair further right. No cuts.

No figure ever enters frame — no hand, no arm, no shoulder, no
reflection of a person, no one reaches toward the console. The amber
strip stays a plain continuous band of light: no readable text, no
letters, no digits, no numerals, no percentage, no tick marks, no
scale, no graduations, no icon, no symbol appears on or near it at
any second. It never flickers, never blinks, never pulses, never
turns red, never empties. Nothing else in frame emits light. Camera
locked off: no cuts, no transitions, no shake, no zoom, no push-in,
no focus rack, no angle change. No bloom, no glow filter, no lens
flare, no starburst, no holographic projection, no floating
interface, no HUD, no gauge graphic. No subtitles, no captions, no
title card, no watermark, no lens data. Photorealistic, 35mm
anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 7 — SİNYAL

`1:00 – 1:10` · 50mm · kadro 1 · yavaş push-in · **A yolu**
📎 **REFERANS:** R2 (MÜHENDİS master) + S6 kokpit karesi (iç mekân çapası)

_"Zayıf, döngüsel, çok eski."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: 3.0 m → 2.2 m push-in.
  İŞLEV: Kuleyle ilk temas. Ses geliyor, kaynak görünmüyor.
  ⭐ SİNYAL GÖRÜNTÜSÜ: ekranda soyut, KENDİNİ BİREBİR TEKRAR EDEN
     bir desen. Döngü sahne içinde iki kez tamamlanır — seyirci
     "aynı şey yine" der. Dalga formu tanınabilir olmalı ama
     rakam/harf taşımamalı [Ders 13].
  ⭐ Mühendis konuşmuyor (KİLİT 2 rahat: 50mm, ama gerek de yok).
```

### 📸 IMAGE PROMPT

```
SCENE:
A man flight engineer leans toward a side console in a cargo ship
cockpit, opening the gain on a weak repeating signal.

ENVIRONMENT:
The cramped cockpit of a two-crew cargo courier seen across the
right-hand console: dark grey-brown panelling, pipe runs, grey repair
patches, a worn seat. The console carries a wide low display showing
one abstract pattern — a soft amber trace that runs across the panel,
dips, doubles back and repeats identically, no scale, no grid.

SUBJECT:
A 33-year-old man flight engineer seated and leaning forward, seen
three-quarter from his left: strong symmetrical features, light brown
skin, short neat three-day black stubble, dark brown eyes, a 2 cm
shiny old burn scar on his RIGHT cheekbone, very short dense black
hair. Dark grey-blue suit with TEAL GREEN worn reinforcement,
oversized back tool module, closed cutting-tool sheath on his left
hip, integrated helmet with a fully transparent seamless visor, face
clear through the glass and lit from below. His right gloved hand
rests on a sliding control; eyes on the trace.

CAMERA:
Shot on a 50mm lens from a fixed position three meters away, f/4, at
shoulder height slightly to his left, display and face both readable.

LIGHTING:
Interior practical light only. The wide amber display at 2800K keys
his face from below through the visor, throwing his shadow onto the
dark ceiling.

PHYSICS:
Normal interior gravity. Seated with weight.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly one figure — no second person, no reflected face. His face
keeps identical bone structure — no morphing; the burn scar stays on
his RIGHT cheekbone. Reinforcement stays TEAL GREEN. The visor stays
a distinct glass surface. The display shows one
plain repeating amber trace only: no readable text, no letters, no
digits, no frequency numbers, no grid, no scale, no icon, no symbol,
no map, no targeting graphic, no holographic projection, no floating
interface. His hand never merges into the control. No bloom, no glow
filter, no flare. No captions, no watermark.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, one slow push-in from 3.0 to 2.2 meters,
no cuts:

SETUP: the camera starts three meters from a seated man at shoulder
height, slightly to his left, f/4, with the wide console display and
his face both readable. It creeps forward at a constant slow rate for
the whole ten seconds. No pan, no tilt, no shake.
FRAME: a 33-year-old man flight engineer leaning toward a side
console — strong symmetrical features, light brown skin with visible
pores, short three-day black stubble, dark brown eyes, a 2 cm shiny
burn scar on his RIGHT cheekbone, very short dense black hair. Dark
grey-blue suit with TEAL GREEN worn reinforcement, oversized back
tool module, closed cutting-tool sheath on his left hip, integrated
helmet with a fully transparent seamless visor, face clear through
the glass. On the console, one soft amber trace runs across a wide
low display, dips, doubles back and repeats. Black window beyond.

0s — He is leaning in, eyes down on the trace. The amber line runs
its shape once and starts again from the same point, identical.
3s — His right gloved hand slides the short control a small distance;
the trace grows slightly stronger and cleaner but keeps exactly the
same shape and the same rhythm.
5s — The pattern completes and repeats a second time, beat for beat
identical to the first. He goes completely still, watching it happen.
7s — He lifts his eyes off the display for a moment toward the black
window, then drops them back to the trace.
10s — The push-in has closed; his face fills more of frame, still lit
from below by the amber trace still repeating. No cuts.

He never speaks: mouth closed, no dialogue, no lip movement. The
display carries one plain repeating amber trace only — no readable
text, no letters, no digits, no numerals, no frequency readout, no
grid, no scale, no ruler, no icon, no symbol, no map, no targeting
graphic; no holographic projection and no floating interface appears
at any second. His face keeps identical bone structure and eye
spacing from first frame to last — no morphing; the burn scar stays
on his RIGHT cheekbone. Reinforcement stays TEAL GREEN. The visor
stays a distinct transparent glass surface and never disappears. His
hand keeps a clear boundary against the control and never merges into
it. Exactly one figure in frame. Constant-rate push-in only: no cuts,
no transitions, no shake, no angle change. No bloom, no glow filter,
no lens flare, no waxy skin. No captions, no name label, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 8 — ANONS

`1:10 – 1:20` · 85mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan aynı karede) — iki master birlikte ekle

_"QUARANTINE. DO NOT LAND. DO NOT ANSWER. NO ONE COMES HOME."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  ⭐ ÇEHOV 1 BURADA KURULUYOR. Bekçi'nin bildiği TEK insan dili bu
     sekiz kelimedir; filmdeki beş Bekçi repliğinin beşi de bu
     cümleden kesilecek (S43 · S60 · S66 · S86 · S99).
  ⚠️ ANONS POST'TA. Sahne sessiz üretilir; kadrajda anonsu temsil
     eden tek şey konsoldaki yavaş amber nabız.
  ⭐ KİLİT 2 SEBEBİ: 85mm'de iki yüz de okunuyor → burada KİMSE
     KONUŞMUYOR. İkisi de dinliyor, ikisi de tepki vermiyor.
     Tepkisizlik oyunculuk değil, KADRAJ kararı: hiç kimse dönmüyor.
  ⚠️ KADRO BÜTÇESİ: `2` işaretli 23 sahnenin 2.'si.
  ⛔ S3 ve S4 doğrulanmadan üretilmez.
```

### 📸 IMAGE PROMPT

```
SCENE:
Two crew sit motionless in a cargo ship cockpit while an old recorded
warning plays through the cabin, and neither of them reacts.

ENVIRONMENT:
The cramped cockpit of a two-crew cargo courier, compressed by the
lens: dark grey-brown panelling, pipe runs, grey repair patches. On
the console between them one short amber strip sits mid-pulse — the
only sign that a transmission is playing.

SUBJECT:
Exactly two figures. LEFT foreground, sharp: a 41-year-old woman
pilot in profile from her right — high cheekbones, light olive skin,
sharp jawline, dark grey-green eyes, a fine faded white scar
splitting her LEFT eyebrow, dark brown hair in a tight low bun,
1.68 m, ORANGE worn reinforcement on a dark grey-blue suit.
RIGHT edge behind her, slightly soft: a 33-year-old man, 1.81 m,
broad-shouldered — light brown skin, short three-day black stubble,
a 2 cm burn scar on his RIGHT cheekbone, very short black hair, TEAL
GREEN reinforcement on the same suit.
Orange for her, teal for him, never swapped; his head sits 13 cm
higher. Both helmeted, visors fully transparent, staring forward,
mouths closed.

CAMERA:
Shot on an 85mm lens from a fixed position three meters away, f/2.8,
at head height, the woman sharp in the left foreground and the man
soft at the right edge.

LIGHTING:
Interior practical light only, pale amber at 2800K from the consoles
below, keying both faces from underneath through their visors.

PHYSICS:
Normal interior gravity. Both seated, completely still.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly two figures — no third person, no duplicate, no reflected
face. Neither speaks: mouths closed, no lip movement. Orange stays on
the woman, teal on the man, never swapped; the 13 cm height gap
holds. Her scar stays on her LEFT eyebrow, his on his RIGHT
cheekbone. Both faces keep identical bone structure — no morphing, no
face swap. Both visors stay distinct glass surfaces and never vanish.
No bloom, no glow filter, no lens flare, no waxy skin. No readable
text or digits; no captions, no dialogue caption, no watermark.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 85mm, fixed lockoff three meters away, no cuts,
no camera movement:

SETUP: the camera is locked off at head height in a cramped cockpit,
f/2.8, long-lens compression: a woman sharp in the left foreground, a
man soft at the right edge behind her. It never moves for the whole
ten seconds.
FRAME: LEFT foreground, a 41-year-old woman pilot in profile from her
right — high cheekbones, light olive skin, sharp jawline, dark
grey-green eyes, a fine faded white scar splitting her LEFT eyebrow,
dark brown hair in a tight low bun, 1.68 m, dark grey-blue suit with
ORANGE worn reinforcement. RIGHT edge behind her, softer, a
33-year-old man flight engineer, 1.81 m, broad-shouldered — light
brown skin, short three-day black stubble, a 2 cm burn scar on his
RIGHT cheekbone, very short black hair, dark grey-blue suit with TEAL
GREEN worn reinforcement. Both in integrated helmets with fully
transparent seamless visors. Pale amber 2800K console light from
below; one short amber strip pulses slowly. Black window ahead.

0s — Both sit completely still, facing forward. The amber strip
pulses once, slow and even, lifting the light on her cheek a little.
3s — The strip pulses again on the same slow beat. Neither of them
moves. Her eyes stay forward, unfocused.
5s — He turns his head a few degrees toward the console strip — the
only movement in the shot — and stops there.
7s — She blinks once. She does not turn, does not look at him, does
not look at the console. Her hands stay flat on the armrests.
10s — The strip pulses a final time and both hold, still facing
forward, still silent. No cuts.

Neither figure speaks at any second: both mouths stay closed, no
dialogue, no lip movement, no jaw motion, no reaction, no startle.
The two suits never swap colour: ORANGE stays on the woman, TEAL
stays on the man, and the 13 cm height difference holds. Her scar
stays on her LEFT eyebrow, his on his RIGHT cheekbone; neither face
takes on the other's features. Both faces keep identical bone
structure from first frame to last — no morphing, no face swap. Both
visors stay distinct glass surfaces and never vanish. Exactly two
figures — no third person, no duplicate. Camera locked off: no cuts,
no transitions, no shake, no zoom, no angle change. No console light
flashes red, strobes or alarms. No bloom, no glow filter, no lens
flare, no waxy skin. No readable text, letters, digits or symbols
anywhere; no captions, no dialogue caption, no name label, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 9 — KARAR

`1:20 – 1:30` · 50mm · kadro 1 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 (KAPTAN master) + S6 kokpit karesi

_"İki yüz yıllık bir şamandıra."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: kusur burada doğuyor — ama henüz kusur gibi görünmüyor.
  Doğru refleks, yanlış gezegen. Rota değişmiyor.
  ⭐ HAREKET İMZASI İLK KEZ: karar verirken sol elini göğüs
     göstergesine koyuyor. Bu tik S25'te tekrarlanacak, S81'de
     doruğa çıkacak. Faz 1'in en önemli tek jesti budur.
  ⭐ KİLİT 2 UYGULAMASI: replik başı konsola dönükken söyleniyor;
     ağız hattı kadrajda okunmuyor, dudak senkron riski düşüyor.
  ⭐ Anonsu temsil eden amber nabız bu sahnede SÖNÜYOR — S8 ile
     görsel bağ budur.
```

### 📸 IMAGE PROMPT

```
SCENE:
A woman pilot shuts off an old warning transmission in a cargo ship
cockpit, says one short thing to nobody, and does not change course.

ENVIRONMENT:
The cramped cockpit of a two-crew cargo courier seen from her right
side: dark grey-brown panelling, pipe runs, grey repair patches, a
worn seat. On the console in front of her one short amber strip
pulses slowly, with sliding segments around it, all abstract light.
Low between the seats a separate short amber bar burns steady.

SUBJECT:
A 41-year-old woman pilot, 1.68 m, slim, seated three-quarter from
her right, her head turned down and away toward the console so her
mouth is angled from the lens. High cheekbones, light olive skin,
sharp jawline, thin lips, dark grey-green eyes, a fine faded white
scar splitting her LEFT eyebrow in two, dark brown hair in a tight
low bun. Dark grey-blue pressure suit with ORANGE worn reinforcement,
three abstract chest indicators, integrated helmet with a fully
transparent seamless visor, and a right glove with a visible
detachable wrist ring. Her right hand rests flat on the console.

CAMERA:
Shot on a 50mm lens from a fixed position two point eight meters
away, f/4, at shoulder height on her right, her hand on the console
and her turned face both in frame. True human scale.

LIGHTING:
Interior practical light only, pale amber at 2800K from the console,
keying her from below and leaving the ceiling dark.

PHYSICS:
Normal interior gravity. Her arm carries its own mass as it moves.

NEGATIVE:
Single unbroken take, no cuts, no transitions, no camera shake.
Exactly one figure — no second person, no reflected face. Her face
keeps identical bone structure — no morphing; the scar stays on her
LEFT eyebrow. Reinforcement stays ORANGE. The visor stays a distinct
glass surface and never vanishes. Her hand keeps a clear boundary
against the console and never merges into or melts it. No console
light flashes red, strobes or alarms. No readable text or digits —
abstract light only. No bloom, no glow filter, no lens flare, no waxy
skin. No captions, no name label, no watermark.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff two point eight meters away,
no cuts, no camera movement:

SETUP: the camera is locked off at shoulder height on her right,
f/4, hand and turned face both in frame. It never moves.
FRAME: a 41-year-old woman pilot, 1.68 m, slim, seated three-quarter
from her right, head angled down toward the console — high
cheekbones, light olive skin, sharp jawline, dark grey-green eyes, a
fine faded white scar splitting her LEFT eyebrow, dark brown hair in
a tight low bun. Dark grey-blue suit with ORANGE worn reinforcement,
three abstract chest indicators, integrated helmet with a fully
transparent seamless visor, right glove with a detachable wrist ring.
On the console one short amber strip pulses slowly; low between the
seats a separate steady amber bar. Pale amber 2800K key from below.

0s — Her right hand rests flat on the console beside the pulsing
amber strip. Her head is down and away, mouth angled from the lens.
2s — She presses two fingers down on the console. The pulsing strip
goes dark and stays dark; the steady amber bar between the seats is
unaffected and keeps burning.
4s — Still looking down and away, she says one short line, her lips
moving briefly and with small amplitude, her mouth turned from the
lens the whole time.
6s — She lifts her right hand off the console, the arm carrying its
own weight, and lets it fall to the armrest.
8s — She places her LEFT hand flat over the three abstract indicators
on her chest and holds it there — a small habitual gesture.
10s — She takes the hand away, settles back and faces forward again.
Nothing on the console changes. No cuts.

Her head stays turned down and away while she speaks; her mouth is
never square to the lens. The pulsing strip, once dark, never
returns, never blinks, never flashes red, never alarms; the steady
amber bar between the seats never dims and never goes out. Her face
keeps identical bone structure and eye spacing from first frame to
last — no morphing; the scar stays on her LEFT eyebrow. Reinforcement
stays ORANGE. The visor stays a distinct glass surface and never
vanishes. Her hand keeps a clear boundary against the console and
never merges into or melts the surface. Exactly one figure in frame.
Camera locked off: no cuts, no transitions, no shake, no zoom, no
angle change. No bloom, no glow filter, no lens flare, no waxy skin.
All consoles show abstract light only — no readable text, letters,
digits or symbols; no captions, no name label, no HUD, no watermark.
Photorealistic, 35mm anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```


---

## 🎬 SAHNE 10 — FAZ KAPANIŞI: IŞIK

`1:30 – 1:40` · 32mm · kadro 0 · fixed lockoff · **A yolu**
📎 **REFERANS:** yok — kadro 0 yörünge; END FRAME kilitlenir → F2 S11'in start frame'i olur

_"Yavaş. Sessiz. Ve tam onlara doğru."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit; büyüyen tek şey ışık.
  İŞLEV: faz kapanışı + F2'ye IŞIK GEÇİŞİ. S11 aynı ışıkla açılır;
  bu yüzden END FRAME kilitlenir ve F2 S11'in start frame'i bu
  kompozisyonun devamı olarak üretilir.
  ⭐ Işık GERÇEK bir kaynaktır: yayar, ama bloom/filtre yok — keskin
     merkez, hızlı düşüş [Ders 41 ayrımı]. Patlama değil, açılma.
  ⭐ Yükselmez, hareket etmez — sadece BÜYÜR. Ses yok.
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
Seen from space, on the dark night side of a rocky planet, a single
point of white light has just opened on the surface — small, still
and silent.

ENVIRONMENT:
The night hemisphere of a rocky planet filling the lower two thirds
of frame as a vast dark curve, its basalt plains barely readable in
faint moonlight, a scatter of pale grey wreck patches just visible.
Above the limb, a thin band of atmospheric haze, then black space
with sparse hard stars. One large pale moon far to the upper LEFT.

SUBJECT:
No figures, no ship in frame. On the dark surface, slightly below
center frame, one small point of clean white light has opened. It is
tiny at this distance but unmistakably artificial: perfectly steady,
perfectly white, with a sharp bright core and a tight, fast falloff
into the surrounding dark ground. It does not flicker, does not
pulse, does not move. Around it the night plain stays black; the
light claims only a small circle of ground.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position in high orbit,
level with the planet's limb, the point of light placed just below
center. True planetary scale — the light is small and the world is
enormous. Physically accurate perspective.

LIGHTING:
Night. Faint grey-blue moonlight at 7000K from the upper left barely
lifts the surface. The white point is the brightest thing in frame:
a real emissive source with a hard core and rapid falloff — no haze
ring, no rays, no streaks.

PHYSICS:
Nothing moves. The planet is static, the stars are static, the light
is steady.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly zero figures, zero ships, zero vehicles in frame. The light
does not flicker, blink, pulse, sweep or move; it has no beam, no
column, no rays, no lens flare, no starburst, no halo ring. No bloom,
no glow filter. No explosion, no fire, no smoke. No readable text,
letters, digits or symbols; no captions, no title card, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
The same view from space ten seconds later: the point of white light
on the night surface has grown into a wide, steady disc of light —
still silent, still rising nowhere.

ENVIRONMENT:
The same night hemisphere filling the lower two thirds of frame as a
vast dark curve, thin haze band above the limb, black space and
sparse hard stars above, one large pale moon far upper LEFT. The
frame, the angle and the distance are identical to the opening.

SUBJECT:
No figures, no ship. The white light, slightly below center, has
widened into a broad, perfectly circular disc of clean white light
lying on the surface — many times its opening size, its edge still
sharp, its core still steady. It lifts a faint rim of terrain detail
around its circumference: low ridges catching white on their inner
faces. It has not risen, not moved sideways, not thrown a beam — it
has only grown. The rest of the night plain stays black.

CAMERA:
Shot on the same 32mm anamorphic lens from the same fixed position in
high orbit, level with the limb, framing unchanged. True planetary
scale; the disc is large now but the world is still larger.

LIGHTING:
Night, unchanged. Faint grey-blue moonlight from the upper left. The
white disc is a real emissive source: hard-edged, steady, with rapid
falloff past its rim — no haze ring, no rays, no streaks.

PHYSICS:
Nothing else has changed. Planet static, stars static, the disc
steady at its new size.

NEGATIVE:
Single unbroken take, no cuts, no camera movement, no camera shake.
Exactly zero figures, zero ships. The disc does not flicker, pulse,
sweep or move; no beam, no column, no rays, no lens flare, no
starburst, no halo ring. No bloom, no glow filter. No explosion, no
fire, no smoke, no shockwave. No readable text, letters, digits or
symbols; no captions, no title card, no HUD, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff in high orbit,
no cuts, no camera movement:

SETUP: the camera is locked off in space, level with the planet's
limb. It never moves, never zooms, never drifts, for the whole ten
seconds.
FRAME: the night hemisphere of a rocky planet fills the lower two
thirds as a vast dark curve, basalt plains barely readable, pale grey
wreck patches faint. A thin haze band above the limb, black space and
sparse hard stars above, one large pale moon far upper LEFT. Slightly
below center, on the dark surface, one small point of clean white
light stands steady.

0s — The point of light is small, sharp-cored and perfectly still,
the brightest thing in the frame. Nothing else on the planet is lit;
the wreck patches stay faint grey in the moonlight.
3s — The light begins to widen — slowly, evenly, without flicker —
into a growing circle of white on the surface. It does not rise, does
not move, does not throw a beam.
6s — The circle keeps growing at the same calm rate; a faint rim of
terrain detail appears around its edge, low ridges catching white on
their inner faces. The stars and the moon are unchanged.
8s — The disc is now many times its opening size, its edge still
sharp, its core still steady, the growth still silent and even.
10s — The disc holds at its widest, dominating the night surface
below center frame, perfectly steady. No cuts.

The light only grows in place: it never flickers, never pulses,
never sweeps, never rises off the ground, never becomes a beam or a
column, never throws rays, never produces a lens flare, a starburst
or a halo ring. No explosion, no fire, no smoke, no shockwave, no
debris. Exactly zero figures and zero ships in frame. Camera locked
off: no cuts, no transitions, no shake, no zoom, no drift. No bloom,
no glow filter. No readable text, letters, digits or symbols; no
captions, no title card, no HUD, no watermark. Photorealistic, 35mm
anamorphic film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

# ✅ FAZ 1 DENETİM TABLOSU

| # | Lens | Kadro | Hareket | 10s yolu | Diyalog | İmaj | Risk |
|---|---|:---:|---|:---:|:---:|:---:|---|
| S1 | 32mm | 0 | lockoff | B | — | 1 | ölçek okunması |
| S2 | 32mm | 0 | yavaş yanal | A | — | 2 | leke parlaması [D3/29] |
| S3 | 85mm | 1 | push-in | A | — | 1 | **yüz çapası** |
| S4 | 50mm | 1 | lockoff | A | — | 1 | **yüz çapası** · el-yüzey [D11/43] |
| S5 | 50mm | **2** | lockoff | A | 2 replik | 1 | yüz karışması |
| S6 | 100mm | 0 | lockoff | B | — | 1 | rakam sızması [D13] |
| S7 | 50mm | 1 | push-in | A | — | 1 | ekran metni [D13] |
| S8 | 85mm | **2** | lockoff | A | — | 1 | yüz karışması · altyazı [D40] |
| S9 | 50mm | 1 | lockoff | A | 1 replik | 1 | dudak senkron [D35] |
| S10 | 32mm | 0 | lockoff | A | — | 2 | bloom/ışın [D3/41] · geçiş çapası |

```
KADRO DENETİMİ
  `2` işaretli sahne: 2 (S5, S8) — fazın bütçesi (2) TAM dolu ✅
  Film geneli `2` sayacı: 2 / 23 kullanıldı
  Üç figürlü sahne: 0 / 5 ✅   Bekçi: bu fazda YOK ✅

SÜRE DENETİMİ
  10 sahne × 10.0 s = 100 s = 1:40 · S1 başlangıcı 0:00 ✅ FAZ TAM

ÇEHOV DENETİMİ
  ÇEHOV 1 (sekiz kelimelik anons) → S8'de kuruldu ✅ (ateşleme: S43+)
  BORÇ ÇUBUĞU (sosyoloji nesnesi) → S6'da kuruldu ✅ (S100'de hâlâ yanar)
  HAREKET İMZASI (sol el göğüste) → S9'da kuruldu ✅ (S25 · S81)
  KULE (dik çizgi)                → S1'de gösterildi, adlandırılmadı ✅ (cevap: S48)
  NOVUM İMA (çift enkazlar)       → S2'de bırakıldı ✅ (fiziksel kanıt: S28)
  IŞIK GEÇİŞİ                     → S10 END FRAME kilitli; F2 S11 o ışıkla açılır ✅
```

---

# ⏭️ SONRAKİ ADIM

```
✅ Faz 1 TAM — 10 sahne · 12 imaj · 10 video promptu
→ ../FAZ_02_VURULMA/FAZ_02_VURULMA.md (S11–S20) · S11, S10'un END
  FRAME ışığından açılır
□ Üretim sonrası: her sahnenin PLAN beati kurguda okunuyor mu
   [Ders 68 ③ — süre değil, BEAT sayılır]
```
