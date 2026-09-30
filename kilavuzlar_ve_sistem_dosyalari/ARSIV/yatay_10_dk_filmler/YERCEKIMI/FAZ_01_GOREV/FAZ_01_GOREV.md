# 🌍 YERÇEKİMİ — FAZ 1 / GOREV

## S1–S12 PROMPTLARI | 0:00 – 1:36 | Perde I | 16:9 Yatay

### _"Aşağısı yok. Ta ki geri gelene kadar."_

> **Bu dosya ADIM 4'tür.** Plan: `../00_PLAN.md` · Bible + 120 sahne
> haritası: `../README.md` · Referans: `../REFERANS_PAKETI.md` (ADIM 3,
> 29.08.2026'da yazıldı — sayfa/panel eşlemesi orada §1 sonunda;
> **üretim RA · RC · RB · RD sayfaları onaylanıp seed'leri yazılmadan
> başlamaz**).
>
> ✅ **KAPSAM: S1–S12 TAM.** (29.08: S1–S10 ilk part olarak yazıldı,
> S11–S12 aynı gün eklendi ve faz kapandı.)
>
> ⛔ Her prompt **self-contained**'dır (AGENTS kural ③). Kimse "Bible'a
> bak" demez; yüz ve giysi tarifi her imaj promptunda tam tekrarlanır.
> Uzunluk bandı: video 2.000–2.600 karakter (KILAVUZ_REHBERI §7);
> image bandı gözlem [prompt_kontrol.py başlık yorumu].
>
> **TEMA: FEDAKÂRLIK** — motife döndüğü sahneler: S8 (durmuş saat, bu
> partta) · S30 · S43 · S84 (sonraki partlar) · tek cümle 00_PLAN §TEMA.

---

# 📎 REFERANS LEJANDI — her sahne başlığının altındaki 🎯 satırı

```
Sayfalar `../REFERANS_PAKETI.md` §3'te; her sayfa 4 panel (p1-p4).
  RA  MÜHENDİS (A) KASKLI   p1 3/4 tam boy · p2 profil · p3 SIRT · p4 yüz CU
  RB  EKİPMAN (A+B)         p1 bilekler saat+halka · p2 HALKA MERDİVENİ
                            6/6→1/6 · p3 kanca + mandal eldiveni · p4 MMU
                            kumanda kolu, şerit 2/4
  RC  KOMUTAN (B) MMU'LU    p1 3/4 tam boy · p2 SIRT/çerçeve · p3 ⭐ A+B
                            yan yana · p4 yüz CU
  RD  PLATFORM + MEKİK      p1 SAĞLAM geniş · p2 HASARLI (S16'dan sonra) ·
                            p3 panel/mandal CU · p4 mekik 3/4, burnu ekran-sola

🎯 SATIRININ OKUNUŞU:
  YÜKLE  = Flow'a "malzeme/ingredient" olarak eklenen sayfa(lar) — TAMAMI
           yüklenir, tek panel kırpılmaz (model bütün panelleri görür)
  ÇAPA   = bu sahnenin kadrajına en yakın panel — start frame imajı
           üretilirken görsel kılavuz
  DURUM  = o sahnede geçerli sayaç/hasar hâli (halka N/6 · MMU N/4 ·
           sağlam/hasarlı) — prompt gövdesindeki sayıyla AYNI olmalı
KURAL: yüklenen sayfa promptu değiştirmez; prompt zaten self-contained.
       Sayfa KİMLİĞİ kilitler, metin kelimeyi. İki insanlı sahnede RA + RC
       birlikte yüklenir; KARIŞMA KİLİDİ cümlesi promptta zaten gömülü.
       Perde I'de RA/RB/RC/RD dışında sayfa gerekmez (RE F3'te başlar).
```

---

# 🔒 FAZ KİLİTLERİ — S1–S120 boyunca geçerli, bu dosyada karara bağlandı

## KİLİT 1 — ZİNCİR KARARI: SAHNE = KENDİ START FRAME'İ (bilinçli sapma [D74])

```
FORMAT KARTI "start/end frame zinciri" der: sahne n'in bitiş karesi
= sahne n+1'in başlangıç karesi. 26.08.2026'dan beri ACI_YAYI §3 ise
ardışık iki sahnede ≥1 ölçek kademesi VE ≥45° açı farkı ister.
İkisi aynı anda sağlanamaz: aynı kare hem bitiş hem başlangıçsa
kurulum DEĞİŞEMEZ.

EMSAL: bu formatın referans filmi THE SECOND SHIP zinciri fiilen
uygulamadı (her sahne kendi kurulumu, END FRAME yalnız 2/10 sahnede);
7-9 dk formatının tek filmi THE SLOW STONE zinciri REDDETTİ.

KARAR: her sahne için TEK imaj promptu = o sahnenin START FRAME'i.
Video I2V modunda üretilir (VEO §6B: statik öğe yeniden tarif
edilmez, "maintain the subject from the first frame" + kısa çapa).
END FRAME imajı yalnız kadraj içeriğinin 8 s'de fiziksel olarak
değiştiği sahnede yazılır — bu partta YOK.
Devamlılık zincirle değil ÇAPAYLA kurulur: REFERANS_PAKETI master
imajları + her imaj promptunda kelimesi kelimesine aynı karakter bloğu.
İmaj sayısı: sahne başına 1 (faz 12 imaj / 12 video; 15 değil).
```

## KİLİT 2 — KASK TAKVİMİ VE DİYALOG YERLEŞİMİ

```
A (mühendis): kask KAPALI S1–S47. Bu partta 10/10 kapalı.
B (komutan):  kask KAPALI 44/44 sahne.
İNSAN REPLİĞİ yalnız şu iki yerleşimde [SES_VE_DIYALOG §2]:
  ① kadrajda ağız yokken (sırttan / OTS / el inserti / geniş, yüz küçük)
  ② MACHINE ve KONTROL sesleri her zaman kadraj dışı
Bu partta EKRANDA OKUNAN AĞIZ: 0 kare. Geniş çekim repliklerinde
"no lip-sync required" notu prompta yazılır (şablon checklist'i).
```

## KİLİT 3 — S1–S12 KURULUM DİZİSİ (README haritasından REVİZE)

```
README'nin F1 tablosu KUR sütununda ardışık çiftlerde 2+ kademe
atlıyordu (A→E = EWS→ECU). ACI_YAYI §3 tam 1 kademe ister; şok bandı
(2+ kademe) filmde ≤2 ve S94 · S102'ye ayrılmış. Dizi düzeltildi:

 S1  EWS  üst açı 25°     A  hook / kapak anı        24mm · 40 m
 S2  WS   göz hizası      B  panel, mekik, ikinci bilgi 24mm · 9 m
 S3  MS   OTS (B sırtı)   C  komutan girer, replik    35mm · 1,5 m
 S4  CU   3/4 cephe vizör D  KONTROL repliği          85mm · 0,9 m
 S5  ECU  tepeden mandal  E  ikinci bilgi: onarım     100mm · 0,35 m
 S6  CU   B'nin eli/kol   E' MMU yakıt şeridi 2/4     85mm · 0,8 m
 S7  MS   B sırttan 3/4   C' puf + espri              50mm · 2 m
 S8  CU   üstten bilekler E' saat + halka (tohum)     85mm · 0,5 m
 S9  MS   A 3/4 arkadan   C' son mandal + AI          50mm · 2,5 m
 S10 WS   göz hizası      B  kancalanma, iki replik   24mm · 9 m
 S11 EWS  üst açı         A  ironi (KISIM 2)
 S12 WS   göz hizası      B' statik (KISIM 2)
Her ardışık çift: tam 1 kademe + ≥45°. Açı tipi: üst · göz hizası ·
OTS · tepe = 4. README F1 tablosu bu diziyle güncellendi.
```

## KİLİT 4 — IŞIK VE EKRAN YÖNÜ HARİTASI (plan katmanı; prompta cümle olarak iner)

```
KUŞBAKIŞI: platform (13 m kafes) ekranda soldan sağa uzanır; alet
gövdesi (4 m silindir) platformun EKRAN-SOL ucunda; açık panel alet
gövdesinin kameraya bakan yüzünde. Mekik platformun 40 m EKRAN-SAĞ
ötesinde, BURNU EKRAN-SOLA bakar, kargo kapakları açık. Dünya her
yatay kadrajda ALT üçte birde; uzay siyahı üstte.
ANA KAMERA TARAFI (S1 S2 S4 S5 S8 S9 S10): güneş üst EKRAN-SAĞ,
  sert beyaz; Dünya'dan mavi-beyaz yumuşak dolgu ALTTAN.
TERS TARAF (S3 S6 S7 — kamera B'nin arkasında, platforma bakar):
  güneş üst EKRAN-SOL; dolgu yine alttan.
Gölgeler her kadrajda mutlak siyah, keskin kenar. Lens küresel.
```

---

# 🎨 ÜRETİM SIRASI VE İMAJ BÜTÇESİ

```
S1–S10 = 10 imaj (start frame) · 10 video (I2V)

ÖNERİLEN SIRA (referans paketi kilitlendikten sonra):
  0) REFERANS_PAKETI: A 3 açı (kasklı) · B 3 açı (MMU'lu) · platform
     master · mekik master — seed kilidi
  1) S5 · S8  → el insertleri, yüz yok: giysi/eldiven dokusunun testi
  2) S2 · S10 → geniş, geometri testi (platform · mekik burnu · Dünya)
  3) S4       → A ilk yüz. ⛔ TETİK SAHNE [D68]: yüz master ile yan
                yana doğrulanmadan iki-figürlü sahne üretilmez
  4) S1       → kapak anı; 2-3 hook varyantı [HOOK §7]
  5) S6 · S7 · S9 → tek figür, orta plan
  6) S3       → iki figür aynı karede (partın en pahalı sahnesi)

SES: on sahne SESSİZ üretilir; telsiz/AI/nefes post'ta
     (ElevenLabs + MUZIK_VE_SES.md). Audio satırı promptta yine
     yazılır — modelin ağız/tempo davranışını yönlendirir.
```

## 🗣️ REPLİK DEFTERİ — saniyeler FORMÜLLE [D122]: (n−1) × 8 + TIMELINE ofseti

| S#  | saniye | konuşan | REGISTER | kanal                          | replik                                     |
| :-: | :----: | ------- | :------: | ------------------------------ | ------------------------------------------ |
| S3  |  0:19  | B       |  HUMAN   | kask telsizi, sırttan          | "Last one, then home."                     |
| S4  |  0:26  | KONTROL |  HUMAN   | uzak telsiz bandı, kadraj dışı | "Servicing crew, you are go to close out." |
| S7  |  0:52  | B       |  HUMAN   | kask telsizi, sırttan          | "Half of this tank goes to storytelling."  |
| S9  |  1:09  | SUIT AI | MACHINE  | kask içi sentetik              | "PANEL SEALED. OXYGEN NINETY-ONE PERCENT." |
| S10 |  1:13  | A       |  HUMAN   | kask telsizi, geniş/yüz küçük  | "Closing out."                             |
| S10 |  1:16  | B       |  HUMAN   | kask telsizi, geniş/yüz küçük  | "Copy. Take the long way back."            |

Sayı söyleyen tek replik MACHINE'de [D82]. Ekranda rakam 0 (halka
segment doluluğu ile). Kasksız replik 0.

---

## 🎬 SAHNE 1 — HOOK / KAPAK ANI: AŞAĞISI YOK

`0:00 – 0:08` · 24mm · kadro A · üst açı 25°, EWS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** + **RD** · ÇAPA: RA p1 (tam boy, figür
> kadrajın ≤%10'u) + RD p1 (SAĞLAM platform) · DURUM: halka 6/6 · panel
> kapağı yarı kapalı · mekik kadraj DIŞI (RD p4 yüklenmez)

_"Altında hiçbir şey yokken bu insan neden bu kadar sakin?"_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera hiç hareket etmez.
  İŞLEV: 0. kare sınavı — sağ üçte birde küçük astronot, sol üçte
  ikide dönen gezegen; el ZATEN kapağı kapatmanın ortasında
  (hareketin ortasında açılış, HOOK §2.2). 0:05 = KAPAK ANI karesi.
  0:03 YENİ BİLGİ [D71]: serbest bir cıvata düz çizgide süzülüp
  kadrajdan çıkar — sıfır-g kanıtı, "bir şey yanlış" hissi.
  ⭐ Ölçek: figür kadraj yüksekliğinin ≤%10'u (1:10 kontrastı).
  Ses: müzik YOK — tek sakin nefes + taşıyıcı cızırtısı.
```

### 📸 IMAGE PROMPT

```
SCENE:
Opening frame of a film, seen from high above a small orbital service
platform: one astronaut, tiny in the right third of frame, is already
halfway through closing a hinged panel cover on a grey instrument
cylinder, while the sunlit curve of Earth fills the left two thirds and
the bottom of the frame.

ENVIRONMENT:
Hard vacuum in low orbit. Earth's blue-white surface, streaked with
cloud bands, curves across the lower and left frame; black space with a
few hard pinpoint stars in the upper right. The platform is a
thirteen-metre white lattice truss with ORANGE handrails, and at its end
a four-metre grey cylindrical instrument body with an open access panel
on the side facing the camera. A single loose bolt rests near the panel
edge. No spacecraft in frame.

SUBJECT:
Exactly one human figure. A 38-year-old woman flight engineer, 1.70
metres tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the hairline,
dark chestnut jaw-length hair tucked behind both ears. Warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring on her LEFT wrist, a steel
mechanical watch on a black strap over her RIGHT glove cuff, its hands
stopped. Her back silhouette is flat: smooth off-white shell fabric, one
vertical spine seam, a low webbing waist belt, and no pack, tank, hose
or cable. Her helmet is a rigid white shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear, zero
tint, no mirror coating, and her face is fully readable through it. She
floats along the truss, feet free, an orange-and-white tether line
running straight from her hip to the rail; her right hand holds the
panel cover half closed, her left hand grips the rail. She occupies
about one tenth of the frame height.

CAMERA:
Shot on a 24mm lens, extreme wide shot, from a fixed position 40 metres
away above the platform, high-angle looking down, camera pitched down 25
degrees. Deep focus. Physically accurate perspective, true scale between
the small figure, the truss and the planet.

COMPOSITION: 16:9 horizontal. The platform sits in the screen-right
third with the astronaut at eight percent of frame height, boots at
forty percent; Earth's lit curve fills the screen-left two thirds, its
horizon crossing at seventy percent of frame height. The bottom fifth
carries only unlit lattice. LIGHTING: Hard white sun from the upper
screen-right; soft blue-white bounce from Earth below and to the left;
shadows on the truss absolute black with razor edges. No haze, no lens
flare.

PHYSICS:
Zero gravity. The tether is straight and taut. Nothing hangs, nothing
settles; the loose bolt sits still with no force on it. The free bolt
crosses the full width of frame in about six seconds on one straight
line, moving a little more than its own length every second and never
slowing. NEGATIVE: Exactly one human figure — no second person, no
reflection of a person. Stripes stay ORANGE; the visor stays clear
glass. 0% bloom, no glow filter, no lens flare, no soft focus. No
readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign; no title card, no caption, no watermark. No CGI
or video-game look. Photorealistic, 35mm film grain. Output: 16:9, 4K,
no text, no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, suit, framing and lighting from the first frame.

MOTION — 8 seconds, 24mm, extreme wide shot, fixed lockoff 40 metres
away above the platform, high-angle looking down, camera pitched down 25
degrees, no cuts, absolutely no camera movement:

SETUP: the camera is locked off high above a small orbital service
platform; the sunlit curve of Earth fills the left two thirds and the
bottom of frame, black space with hard pinpoint stars in the upper
right. The white lattice truss with ORANGE handrails and its grey
instrument cylinder sit in the right third. One woman flight engineer in
a warm off-white suit with ORANGE stripes, clear visor, flat back, tiny
at one tenth of frame height, floats at the open panel with an
orange-and-white tether running straight to the rail.

0s — The shot opens mid-action: her right hand is already pushing the
hinged panel cover closed, her left hand on the rail, feet free. Earth's
cloud bands creep very slowly across the lower frame.
2s — A single loose bolt near the panel edge is nudged free. It turns
end over end and drifts screen-right in a dead straight line at constant
speed, never slowing, never curving.
4s — The bolt leaves the frame at the right edge. She does not look at
it. The cover reaches the cylinder wall; her whole body drifts a few
centimetres against the taut tether as she pushes.
6s — She presses the cover flat with the heel of her glove and holds it
there. Her helmet turns a few degrees toward the panel's edge. A loose
strand of hair lifts inside the helmet.
8s — She holds the cover down, still, one slow exhale. Earth keeps
turning beneath her. No cuts.

Audio: hard vacuum — no exterior sound at all. Inside the helmet, one
slow calm breath in and out; a faint radio carrier hiss. No voice, no
music.

Every free object drifts in a straight line at constant speed — never
hovering, never stopping on its own. Her body is never rigid: small
drift, small counter-motion at the hips, hair lifting. Exactly one human
figure — no second person, no reflection. Single unbroken take, no cuts,
no zoom, no push-in, no camera shake. 0% bloom, no glow filter, no lens
flare. No readable text, letters, digits or symbols on any display,
surface, patch or sign; no subtitles, no caption, no title card, no
watermark. Photorealistic, 35mm film grain. [PHYSICS + NEGATIVE bibles
apply throughout]
```

---

## 🎬 SAHNE 2 — İKİNCİ BİLGİ: BU BİR ONARIM

`0:08 – 0:16` · 24mm · kadro A · göz hizası, WS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** + **RD** · ÇAPA: RA p2 (profil) + RD p1
> (SAĞLAM geniş: platform + mekik aynı kadraj) · DURUM: kapak kapalı,
> iki mandal açık · mekik burnu EKRAN-SOLA, kargo kapakları açık (RD p4)

_"Bugün son gün."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit.
  İŞLEV: S1'in ikinci bilgisi [HOOK §3] — geniş kadraj işi anlatır:
  kapatılan panel, açık kargo kapaklı mekik, kancalı halat. Sorunun
  cevabı değil, bağlamın taksidi.
  ⭐ Mekik yönelimi: burnu EKRAN-SOLA bakar, kargo kapakları açık —
  her mekik cümlesinde tekrarlanır (uzamsal §5.1).
  Kadroda B YOK (kadro-2 bütçesi 14 sahne; S2 listede değil).
```

### 📸 IMAGE PROMPT

```
SCENE:
A wide lateral view at eye level with the platform: a lone woman
astronaut, full body, floats at a closed access panel on a grey
instrument cylinder in the left-centre of frame; a winged shuttle sits
far off in the right third, nose pointing screen-left, cargo bay doors
open; Earth's sunlit limb fills the lower third.

ENVIRONMENT:
Hard vacuum in low orbit. A thirteen-metre white lattice truss with
ORANGE handrails runs across the middle of frame from left to right; the
four-metre grey instrument cylinder sits at its screen-left end, its
hinged access cover now closed with two latch levers still open. Forty
metres beyond the truss to the screen-right, a white thirty-seven-metre
shuttle hangs in the black, nose pointing screen-left, its cargo bay
doors open and their white inner faces catching sun. Below everything,
Earth's cloud-streaked blue-white curve; above, black space with hard
pinpoint stars.

SUBJECT:
Exactly one human figure. A 38-year-old woman flight engineer, 1.70
metres tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the hairline,
dark chestnut jaw-length hair tucked behind both ears. Warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring on her LEFT wrist, a steel
mechanical watch on a black strap over her RIGHT glove cuff, its hands
stopped. Her back silhouette is flat: smooth off-white shell fabric, one
vertical spine seam, a low webbing waist belt, and no pack, tank, hose
or cable. Her helmet is a rigid white shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear, zero
tint, no mirror coating, and her face is fully readable through it. Seen
in full profile facing screen-left, both gloves flat on the closed
cover, legs trailing free, tether line straight from hip to rail.

CAMERA:
Shot on a 24mm lens, wide shot, from a fixed position 9 metres away
level with the truss, eye-level, horizon of the Earth limb perfectly
horizontal. Deep focus. Physically accurate perspective, true scale:
figure, truss, shuttle.

COMPOSITION: 16:9 horizontal. The platform runs across the lower half,
its top edge at fifty percent of frame height; the woman stands at
thirty-eight percent of frame width, her boots at forty-four percent and
her helmet at seventy-two percent of frame height. The shuttle sits
small in the screen-right quarter. LIGHTING: Hard white sun from the
upper screen-right; soft blue-white bounce from Earth below; razor-edged
black shadows across the truss; the shuttle's cargo doors a bright white
plane. No haze, no lens flare.

PHYSICS:
Zero gravity. Tether taut and straight. Her legs float slightly apart;
nothing hangs.

NEGATIVE:
Exactly one human figure — no crew in the shuttle, no second person.
Stripes stay ORANGE; the visor stays clear glass. 0% bloom, no glow
filter, no lens flare. No readable text, letters, digits, numbers or
symbols on any display, surface, patch or sign — no markings on the
shuttle; no title card, no caption, no watermark. No CGI look.
Photorealistic, 35mm film grain. Output: 16:9, 4K, no text, no
watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, suit, framing and lighting from the first frame.

MOTION — 8 seconds, 24mm, wide shot, fixed lockoff 9 metres away,
eye-level with the truss, no cuts, absolutely no camera movement:

SETUP: the camera is locked off level with a thirteen-metre white
lattice truss that crosses the frame; the grey instrument cylinder with
its closed access cover sits screen-left, the white shuttle far in the
right third with its nose pointing screen-left and cargo doors open,
Earth's sunlit limb across the lower third, black space above. One woman
flight engineer in a warm off-white suit with ORANGE stripes, clear
visor, flat back, floats in full profile at the cover, tether straight
to the rail.

0s — Both her gloves are flat on the closed cover, holding it seated.
Her legs trail slightly apart. Earth's cloud bands creep beneath.
2s — She lifts her right glove off the cover and reaches up to the upper
latch lever, fingers closing around it with a clear grip.
4s — Her body swings a few centimetres in the opposite direction as she
pulls, the tether going taut and holding her. Her helmet tilts toward
the latch.
6s — The lever turns a quarter turn under her hand. Her left glove
slides along the rail to steady the drift.
8s — She stays on the latch, still, one slow breath; far to the right
the shuttle has not moved. No cuts.

Audio: hard vacuum — no exterior sound. Inside the helmet a slow steady
breath and a faint radio carrier hiss. No voice, no music.

Every free object keeps continuous momentum in a straight line; nothing
hovers, nothing settles. Her body is never rigid: drift, counter-drift,
small hip rotation, hair lifting inside the helmet. The shuttle keeps
its nose pointing screen-left and never moves. Exactly one human figure
— no second person, no crew, no reflection. Single unbroken take, no
cuts, no zoom, no pan, no camera shake. 0% bloom, no glow filter, no
lens flare. No readable text, letters, digits or symbols on any display,
surface, patch or sign — no markings on the shuttle; no subtitles, no
caption, no watermark. Photorealistic, 35mm film grain. [PHYSICS +
NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 3 — KOMUTAN

`0:16 – 0:24` · 35mm · kadro 2 · OTS (B'nin omzundan), MS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RC** + **RA** + **RD** · ÇAPA: RC p2 (B'nin
> sırtı/çerçeve — ön plan) + RA p1 (A arka plan) + RD p3 (panel) ·
> DURUM: ⭐ KLON KAPISI — RC p3 (A+B yan yana) yüklü sayfada görünür;
> üretimde iki figür ayrışmıyorsa sahne değil SAYFA yeniden üretilir

_"Last one, then home."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera B'nin ARKASINDA — ağız yok.
  İŞLEV: ikinci karakter girer; sıfır-g'de İKİ gövde aynı karede
  (kadro-2 bütçesinden 1/14). İki gövdeye AYRI hareket cümlesi
  (tek dönüş vektörü riski, 00_PLAN §Risk ①).
  KARIŞMA KİLİDİ promptta gömülü. Ters taraf: güneş üst EKRAN-SOL.
  MMU pufu: ince, düz, keskin koni — alev/duman YOK.
  Replik 0:19 — B, telsiz, sırttan.
```

### 📸 IMAGE PROMPT

```
SCENE:
Over the shoulder of a big man in a thruster frame, seen from behind in
the left foreground, soft and out of focus, looking past him to a woman
astronaut sharp in the mid-background who works at a panel on a grey
instrument cylinder; Earth's limb runs along the bottom of frame.

ENVIRONMENT:
Hard vacuum in low orbit. Between the two figures, a white lattice truss
with ORANGE handrails leads screen-left to the four-metre grey
instrument cylinder, whose hinged access cover is closed with one latch
lever already turned. Earth's cloud-streaked blue-white curve fills the
lower quarter; black space with hard pinpoint stars above.

SUBJECT:
Exactly two human figures, human count 2. FOREGROUND, back to camera,
blurred: a 52-year-old man mission commander, 1.85 metres tall, broad
and heavy, in a warm off-white pressure suit with NAVY reinforcement
stripes on shoulders, knees and glove cuffs, a rigid white aluminium
thruster frame on his back as deep as a forearm, two control arms
reaching forward like armrests, eight small nozzles at its corners,
spherical helmet with an optically clear visor. Only his right shoulder,
the back of his helmet and one corner of the frame are in shot.
MID-BACKGROUND, sharp: a 38-year-old woman flight engineer, 1.70 metres
tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the hairline,
dark chestnut jaw-length hair tucked behind both ears. Warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring on her LEFT wrist, a steel
mechanical watch on a black strap over her RIGHT glove cuff, its hands
stopped. Her back silhouette is flat: smooth off-white shell fabric, one
vertical spine seam, a low webbing waist belt, and no pack, tank, hose
or cable. Her helmet is a rigid white shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear, zero
tint, no mirror coating, and her face is fully readable through it. She
faces the panel three-quarter away, right hand on the lower latch lever,
tether straight to the rail. The two suits differ in reinforcement
colour — orange for the woman, navy for the man — and never swap; only
the man carries the rigid thruster frame on his back; he is 15 cm
taller.

CAMERA:
Shot on a 35mm lens, medium shot, over-the-shoulder from a fixed
position 1.5 metres behind the man, at his shoulder height. Shallow
focus on the woman; his shoulder and helmet soft.

COMPOSITION: 16:9 horizontal. His shoulder and frame fill the
screen-right third and the lower half; she reads small in the
screen-left third at twenty percent of frame height, her helmet at
fifty-five percent. The upper quarter carries only black space.
LIGHTING: Hard white sun from the upper screen-left; blue-white bounce
from Earth below; his helmet rim and frame edges catch the sun, black
razor shadows across the truss.

PHYSICS:
Zero gravity. Two separate bodies: he hangs free with no tether; she is
tethered. Nothing hangs, nothing settles.

NEGATIVE:
Exactly two human figures, no third. No face on the foreground man —
back of helmet only. 0% bloom, no glow filter, no lens flare. No
readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign; no caption, no watermark. Photorealistic, 35mm
film grain. Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain both subjects, suits, framing and lighting from the first
frame.

MOTION — 8 seconds, 35mm, medium shot, over-the-shoulder, fixed lockoff
1.5 metres behind the man at his shoulder height, no cuts, absolutely no
camera movement:

SETUP: the camera is locked off behind a big man in a warm off-white
suit with NAVY stripes and a rigid white thruster frame on his back; his
right shoulder and the back of his helmet fill the left foreground,
soft. Past him, sharp, a woman flight engineer in the same off-white
suit with ORANGE stripes, clear visor, flat back, works at a closed
panel on a grey instrument cylinder at the screen-left end of a white
truss. Earth's limb along the bottom, black space above. The two suits
never swap colours; only the man has the frame; he is the taller.

0s — She is turning the lower latch lever with her right hand, her left
hand on the rail. He hangs still, his frame's control arm just visible
at the frame edge.
2s — His gloved hand nudges the control arm. From the nearest corner
nozzle, one short thin white plume, a straight sharp cone that thins to
nothing in half a second. His whole body eases forward a few centimetres
and stops; her body does not react to it — she keeps turning the lever,
her own small drift against the tether separate from his.
3s — On the radio, his voice, unhurried and warm, says: "Last one, then
home." He is seen from behind; no mouth in frame.
5s — The lever seats. She lifts her right glove and rests the palm on
the cover, a small nod inside the helmet.
7s — He rotates very slowly, no more than ten degrees, then stops with a
second, shorter plume from the opposite corner.
8s — Both hold. No cuts.

Audio: hard vacuum — no exterior sound, not even at the thruster plume.
Only the radio band: faint carrier hiss, his single spoken line at 3
seconds heard only — never shown as text, two slow breaths. No music.

The two bodies move independently, each with its own drift and its own
small rotation; they never share one motion. Exactly two human figures,
human count 2, no third. The line is heard only — no subtitles, no
captions, no on-screen speaker. Single unbroken take, no cuts, no zoom,
no camera shake. 0% bloom, no glow filter, no lens flare. No readable
text, letters, digits or symbols on any display, surface, patch or sign;
no watermark. Photorealistic, 35mm film grain. [PHYSICS + NEGATIVE
bibles apply throughout]
```

---

## 🎬 SAHNE 4 — VİZÖR

`0:24 – 0:32` · 85mm · kadro A · 3/4 cephe, CU · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** · ÇAPA: **RA p4** (yüz CU — bu sahne o
> panelin sinematik hâlidir) · DURUM: kask kapalı, vizörde Dünya
> yansıması alt üçte bir · ⛔ TETİK SAHNE [D68]: üretilen yüz RA p4 ile
> YAN YANA doğrulanmadan S3 ve S10 üretilmez

_"Yüz ilk kez okunur. Sakin."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit.
  İŞLEV: göz bütçesi [KARAKTER §1] — vizör içi ışık, göz yönü.
  Vizörün alt üçte birinde Dünya'nın soluk kısmi yansıması: vizörün
  CAM olarak okunmasını sağlayan tek işaret; ayna değil, tonlama
  değil [D37 · D57].
  Replik 0:26 — KONTROL, uzak telsiz, kadraj dışı. A konuşmaz.
  ⛔ Yüz REFERANS master ile yan yana doğrulanmadan S3 üretilmez.
```

### 📸 IMAGE PROMPT

```
SCENE:
Close-up, three-quarter front, of a woman astronaut's helmet and face in
hard sunlight: she is looking down and to the screen-left at a panel out
of frame, calm, a faint partial reflection of Earth's blue curve lying
across the lower third of her clear visor.

ENVIRONMENT:
Hard vacuum in low orbit. Behind her helmet, out of focus, black space
and the soft blue-white edge of Earth in the lower corners; one ORANGE
handrail crosses the lower frame edge, soft.

SUBJECT:
Exactly one human figure. A 38-year-old woman flight engineer, 1.70
metres tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the hairline,
dark chestnut jaw-length hair tucked behind both ears. Warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring on her LEFT wrist, a steel
mechanical watch on a black strap over her RIGHT glove cuff, its hands
stopped. Her back silhouette is flat: smooth off-white shell fabric, one
vertical spine seam, a low webbing waist belt, and no pack, tank, hose
or cable. Her helmet is a rigid white shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear, zero
tint, no mirror coating, and her face is fully readable through it.
Framed from the collar ring up; eyes open, lids relaxed, mouth closed;
the tips of her hair lift very slightly inside the helmet.

CAMERA:
Shot on an 85mm lens, close-up, from a fixed position 0.9 metres away,
three-quarter front, at eye-level with her face. Shallow depth of field:
face and visor sharp, background soft.

COMPOSITION: 16:9 horizontal. Her helmet fills the central half of frame
width; her collar ring sits at twelve percent of frame height and the
crown of the helmet at ninety percent, her eyes on the upper-third line
at sixty-four percent. Earth's reflection lies in the lower third of the
glass. LIGHTING: Hard white sun from the upper screen-right, one sharp
key across the right side of her face inside the helmet; blue-white
Earth bounce fills the shadow side softly; the visor carries a faint
transparent reflection of Earth's curve in its lower third, never
opaque, never mirrored. No haze, no lens flare.

PHYSICS:
Zero gravity: hair tips drift, no strand hangs.

NEGATIVE:
Exactly one human figure, no reflection of another person in the visor.
Identical bone structure and eye spacing; the scar stays on her LEFT
temple; stripes stay ORANGE. The visor stays clear, no tint, no HUD
graphics. 0% bloom, no glow filter, no lens flare, no waxy or smoothed
skin. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign; no caption, no name label, no
watermark. Photorealistic, 35mm film grain. Output: 16:9, 4K, no text,
no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, suit, framing and lighting from the first frame.

MOTION — 8 seconds, 85mm, close-up, fixed lockoff 0.9 metres away,
three-quarter front at eye-level, shallow depth of field, no cuts,
absolutely no camera movement:

SETUP: the camera is locked off on the helmet and face of a woman flight
engineer in a warm off-white suit with ORANGE stripes; her clear,
untinted visor carries a faint transparent reflection of Earth's blue
curve in its lower third; hard sun keys the right side of her face,
blue-white bounce fills the left; black space and the soft edge of Earth
behind her.

0s — Her eyes are down and to the screen-left, on the panel out of
frame. Breathing slow and even; the faint reflection of Earth drifts a
hair's width across the glass as the planet turns.
2s — On the radio, distant and thin through the band, a man's voice says
calmly: "Servicing crew, you are go to close out." The voice is
off-screen; her mouth stays closed.
4s — Her eyes lift from the panel to the horizon beyond the frame edge,
hold there for a moment, one slow blink. The sunlit edge of her cheek
shifts as her head turns a few degrees.
6s — Her eyes drop back to the work. A single strand of hair lifts and
settles inside the helmet, weightless. One small swallow.
8s — She holds, calm, eyes on the panel. No cuts.

Audio: hard vacuum — no exterior sound. Inside the helmet, slow even
breathing, a faint carrier hiss, and the distant radio line at 2 seconds
heard only — never shown as text. No music.

Her face keeps identical bone structure and eye spacing throughout — no
morphing; the scar stays on her LEFT temple. The visor stays a distinct
clear glass surface with no tint, no HUD, no opaque reflection. Exactly
one human figure; no second face appears in the glass. She never speaks:
mouth closed, no lip movement. Single unbroken take, no cuts, no zoom,
no push-in, no camera shake. 0% bloom, no glow filter, no lens flare, no
waxy skin. No readable text, letters, digits or symbols on any display,
surface, patch or sign; no subtitles, no caption, no watermark.
Photorealistic, 35mm film grain. [PHYSICS + NEGATIVE bibles apply
throughout]
```

---

## 🎬 SAHNE 5 — MANDAL

`0:32 – 0:40` · 100mm makro · kadro A (yalnız el) · tepeden, ECU · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RB** + **RD** · ÇAPA: **RB p3** (mandal
> eldiveni + kanca) + RD p3 (panel/mandal CU) · DURUM: üst mandal
> çeyrek tur, cıvata başı çıkık → gömülü · RA YÜKLENMEZ (yüz yok —
> sayfa yüklenirse model yüz ekleyebilir)

_"Bir onarımın sesi: eldivenin içinden."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit, mandala tepeden.
  İŞLEV: el bütçesi [KARAKTER §4.1] + ses mimarisi: vakumda ses YOK,
  mandalın oturuşu eldivenden BOĞUK tık olarak gelir, temas kesilince
  anında söner (Freemantle kuralı).
  Alet YOK — çıplak eldivenle mandal kolu (D37/D43 devre dışı).
```

### 📸 IMAGE PROMPT

```
SCENE:
Extreme close-up looking straight down at a gloved hand gripping a latch
lever on a closed grey panel cover: the lever is caught mid-turn, a
captive bolt head beside it not yet flush.

ENVIRONMENT:
Hard vacuum in low orbit. The frame is filled by the grey painted panel
cover of an instrument cylinder — matte, micro-scratched, a seam line
where the cover meets the housing, one captive bolt head with a raised
rim sitting a few millimetres proud, and a hinged latch lever of dull
steel. At the top edge of frame, out of focus, a sliver of ORANGE
handrail and black space.

SUBJECT:
Exactly one human figure, hand only — no face in frame. The glove
belongs to a 38-year-old woman flight engineer, 1.70 metres tall, slim
and upright, in a warm off-white pressure suit with ORANGE reinforcement
stripes on shoulders, knees and glove cuffs, a soft chest panel with
three small coloured lights and no numerals, a six-segment amber oxygen
ring on her LEFT wrist, a steel mechanical watch on a black strap over
her RIGHT glove cuff, its hands stopped, a flat back — smooth shell
fabric, one vertical spine seam, a low webbing waist belt — with no
pack, tank, hose or cable, and a rigid white helmet shell with a flat
rectangular front glass measuring 24 by 16 centimetres, held in a
visible bright metal frame the width of a finger; the glass is optically
clear with zero tint and no mirror coating. In frame: her RIGHT glove,
off-white with an ORANGE cuff stripe, the black watch strap crossing the
cuff, fingers closed around the lever with a clear structural boundary
between glove and steel, thumb along the lever's spine.

CAMERA:
Shot on a 100mm macro lens, extreme close-up, from a fixed position 0.35
metres away, aimed straight down at the latch, top-down. Shallow depth
of field: lever, bolt head and glove fingers sharp.

COMPOSITION: 16:9 horizontal. The latch and the glove fill the central
sixty percent of frame width, the latch arm crossing between thirty-five
and sixty-five percent of frame height. The outer eighth on both sides
carries only out-of-focus panel. LIGHTING: Hard white sun raking from
the screen-right, throwing a razor-edged black shadow of the lever
across the cover; faint blue-white bounce in the shadow. Every scratch
on the paint and every seam of the glove fabric visible. No haze, no
lens flare.

PHYSICS:
Zero gravity. The hand presses with visible effort; the glove fabric
creases at the knuckles; no dust, nothing floats in frame.

NEGATIVE:
Exactly one human figure, hand only — no face, no second hand of another
person. The glove and the lever keep a clear boundary — no merging, no
extra fingers. 0% bloom, no glow filter, no lens flare. No readable
text, letters, digits, numbers or symbols on any display, surface, patch
or sign — no stencil on the cover, no markings on the glove; no caption,
no watermark. Photorealistic, 35mm film grain. Output: 16:9, 4K, no
text, no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, glove, framing and lighting from the first frame.

MOTION — 8 seconds, 100mm macro, extreme close-up, fixed lockoff 0.35
metres away, top-down straight at the latch, no cuts, absolutely no
camera movement:

SETUP: the camera is locked off looking straight down at a grey painted
panel cover; a dull steel latch lever sits mid-turn under an off-white
glove with an ORANGE cuff stripe and a black watch strap across the
cuff; a captive bolt head beside the lever stands a few millimetres
proud. Hard sun rakes from the screen-right; the lever's shadow is a
razor-edged black bar across the paint.

0s — The fingers are closed around the lever, thumb along its spine, the
glove fabric creased at the knuckles under load.
2s — The lever turns a quarter turn, slowly, the black shadow bar
sweeping with it across the cover. The raised bolt head sinks until its
rim is flush with the paint.
4s — The lever seats with a small hard stop; the glove flexes once
against the resistance and holds.
5s — The fingers release one at a time, little finger first, the thumb
last, and the hand lifts two centimetres off the lever.
7s — The open palm lays itself flat on the cover for a moment, feeling
the seated latch through the glove rather than looking.
8s — The hand rests there, still. No cuts.

Audio: hard vacuum — no exterior sound. Inside the suit: one dull,
muffled thud carried through the glove when the lever seats, and one
smaller click when the bolt goes flush, each cut off the instant contact
ends; a slow breath; a faint carrier hiss. No voice, no music.

The glove and the steel keep a clear structural boundary in every frame
— no merging, no phasing, no extra fingers; the lever never deforms. No
dust, nothing floats into frame. Exactly one human figure, hand only; no
face ever enters frame. Single unbroken take, no cuts, no zoom, no
camera shake. 0% bloom, no glow filter, no lens flare. No readable text,
letters, digits or symbols on any display, surface, patch or sign — no
stencil on the cover; no subtitles, no caption, no watermark.
Photorealistic, 35mm film grain. [PHYSICS + NEGATIVE bibles apply
throughout]
```

---

## 🎬 SAHNE 6 — YAKIT ŞERİDİ

`0:40 – 0:48` · 85mm · kadro B (yalnız el ve kol) · CU · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RB** · ÇAPA: **RB p4** (MMU kumanda kolu,
> LACİVERT manşet, şerit 2/4) · DURUM: yakıt şeridi **2/4** (S27'de 1/4,
> S34'te 0/4 — bu sahnede DEĞİŞMEZ) · RC YÜKLENMEZ (yüz yok)

_"Yarısı gitmiş bile."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit. Ters taraf: güneş üst
  EKRAN-SOL.
  İŞLEV: ÇEHOV 3 kurulumu — MMU yakıt şeridi 4 segmentin 2'si yanık.
  Rakam YOK; doluluk okunur. Yüz yok, replik yok: sessiz insert.
  Kadroda B'nin yalnız eli ve kumanda kolu; A kadraj dışı.
```

### 📸 IMAGE PROMPT

```
SCENE:
Close-up of a gloved hand resting on the forward control arm of a
back-mounted thruster frame: on the arm, a short strip of four amber
light segments, two lit and two dark; beyond, out of focus, the blue
curve of Earth.

ENVIRONMENT:
Hard vacuum in low orbit. The control arm is a white aluminium tube with
a moulded grip at its end, reaching forward from a rigid white thruster
frame whose corner and one small nozzle show at the upper right of
frame, soft. Along the top face of the arm, a small recessed strip of
four square amber light segments: the two nearest the grip lit steadily,
the two beyond them dark. No numerals, no markings. Background: black
space, hard pinpoint stars, and the soft blue-white curve of Earth in
the lower third.

SUBJECT:
Exactly one human figure, hand and forearm only — no face in frame. The
glove belongs to a 52-year-old man mission commander, 1.85 metres tall,
broad and heavy, wearing a warm off-white pressure suit with NAVY
reinforcement stripes on shoulders, knees and glove cuffs, a soft chest
panel with three small coloured lights and no numerals, a rigid white
aluminium thruster frame on his back as deep as a forearm with two
control arms reaching forward like armrests and eight small nozzles at
its corners, and a rigid white helmet shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear with
zero tint and no mirror coating. In frame: his RIGHT glove, off-white
with a NAVY cuff stripe, closed loosely around the grip, thumb resting
on a small round knob at the grip's top; the forearm of the suit leads
out of frame to the screen-left.

CAMERA:
Shot on an 85mm lens, close-up, from a fixed position 0.8 metres away,
from the screen-right side of the arm, slightly above it. Shallow depth
of field: glove, grip and the amber strip sharp.

COMPOSITION: 16:9 horizontal. The control arm runs from the lower
screen-left to the centre; the four-segment strip sits at forty-five
percent of frame height and thirty percent of frame width, filling a
tenth of frame width. The upper third carries only soft suit fabric.
LIGHTING: Hard white sun from the upper screen-left, a sharp key along
the top of the arm and the glove knuckles; blue-white bounce from Earth
below fills the underside; the two lit segments are small, steady,
sharp-edged amber lights, no halo. No haze, no lens flare.

PHYSICS:
Zero gravity. The arm and the hand are still; nothing hangs.

NEGATIVE:
Exactly one human figure, hand and forearm only — no face. The strip
carries no numerals, no letters, no gauge markings — light segments
only. 0% bloom, no glow filter, no lens flare, no halo around the amber
segments. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign; no caption, no watermark.
Photorealistic, 35mm film grain. Output: 16:9, 4K, no text, no
watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, glove, framing and lighting from the first frame.

MOTION — 8 seconds, 85mm, close-up, fixed lockoff 0.8 metres away from
the screen-right side of the control arm, slightly above it, shallow
depth of field, no cuts, absolutely no camera movement:

SETUP: the camera is locked off on a gloved hand resting on the forward
control arm of a white thruster frame; the glove is off-white with a
NAVY cuff stripe; along the top of the arm a recessed strip of four
square amber light segments, two lit steadily near the grip, two dark
beyond; hard sun from the upper screen-left; the soft blue curve of
Earth in the lower background, black space and hard stars above.

0s — The hand rests loosely on the grip, thumb on the small round knob.
The two amber segments hold steady; the two dark ones stay dark. The
background Earth creeps very slowly.
2s — The thumb rolls the knob a few degrees forward. Far outside the
frame a thruster fires: the whole arm, and the glove with it, eases
forward about two centimetres and then stops.
4s — The hand tightens on the grip for a moment and relaxes. The amber
segments do not change: still two lit, two dark, steady and sharp-edged.
6s — The thumb rolls the knob back. The arm settles the last centimetre
and is still. A faint tremor runs once through the glove fingers.
8s — Hand at rest, two amber segments lit, two dark. No cuts.

Audio: hard vacuum — no exterior sound. Inside the suit: one slow
unhurried breath, a faint radio carrier hiss, and a soft click carried
through the glove when the knob rolls, cut off the instant the thumb
stops. No voice, no music.

The amber strip stays exactly two lit and two dark for the whole shot —
no flicker, no extra segment, no numerals, no gauge markings. The glove
keeps a clear boundary with the grip — no merging, no extra fingers.
Exactly one human figure, hand and forearm only; no face ever enters
frame. Single unbroken take, no cuts, no zoom, no camera shake. 0%
bloom, no glow filter, no halo, no lens flare. No readable text,
letters, digits or symbols on any display, surface, patch or sign; no
subtitles, no caption, no watermark. Photorealistic, 35mm film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 7 — ESPRİ

`0:48 – 0:56` · 50mm · kadro B · sırttan 3/4, MS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RC** + **RD** · ÇAPA: **RC p2** (sırt/çerçeve —
> 8 lüle, iki kumanda kolu) + RD p1 (truss ucu ekran-solda) · DURUM: B
> tek, A kadraj DIŞI (RA yüklenmez) · MMU pufu ince düz koni

_"Half of this tank goes to storytelling."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera B'nin arkasında — ağız yok.
  İŞLEV: B'nin tonu (rutini espriyle taşıyan); ÇEHOV 3'ün sesli
  yarısı. Ters taraf: güneş üst EKRAN-SOL.
  Kadroda yalnız B; platform kenarı EKRAN-SOLDAN kadraja girer, A
  kadraj dışı (kadro-2 bütçesi korunur).
  Replik 0:52 — B, telsiz, sırttan. MMU pufu ince düz koni.
```

### 📸 IMAGE PROMPT

```
SCENE:
Medium shot from behind and slightly to one side of a big astronaut in a
back-mounted thruster frame, hanging free above the sunlit curve of
Earth; the end of a white lattice truss enters from the screen-left
edge, no one on it.

ENVIRONMENT:
Hard vacuum in low orbit. Earth's cloud-streaked blue-white curve fills
the lower third; black space with hard pinpoint stars above. At the
screen-left edge, the end of a thirteen-metre white lattice truss with
an ORANGE handrail, empty. No spacecraft in frame.

SUBJECT:
Exactly one human figure. A 52-year-old man mission commander, 1.85
metres tall, broad and heavy: wide bony face, thick dark brows, deep
lines at the eye corners, olive-brown skin with visible pores, short
greying stubble, short dense salt-and-pepper hair, dark brown eyes, a
small old notch in his RIGHT earlobe. Warm off-white pressure suit with
NAVY reinforcement stripes on shoulders, knees and glove cuffs, a soft
chest panel with three small coloured lights and no numerals, and a
rigid white aluminium thruster frame on his back, as deep as a forearm,
with two control arms reaching forward like armrests and eight small
nozzles at its corners. His helmet is a rigid white shell 32 centimetres
across with a flat rectangular front glass 24 by 16 centimetres in a
visible bright metal frame two centimetres wide; the glass is optically
clear, zero tint, no mirror coating, and his face is fully readable
through it. Seen three-quarter from behind: the thruster frame fills the
centre of frame, the back of his helmet above it, his gloves on both
control arms, legs trailing free; he is angled screen-left, so that only
the edge of his cheek shows past the helmet rim and his mouth is hidden.

CAMERA:
Shot on a 50mm lens, medium shot, from a fixed position 2 metres behind
him and a little to the screen-right, level with his shoulders. Deep
focus.

COMPOSITION: 16:9 horizontal. His back fills the screen-left half from
twenty to eighty-five percent of frame height; the thruster frame reads
across the middle third. The screen-right third carries only black space
and one thin plume cone. LIGHTING: Hard white sun from the upper
screen-left, rimming the frame tubes, the helmet and his left shoulder;
blue-white bounce from Earth below lights the underside of the frame;
razor-edged black shadows on the suit. No haze, no lens flare.

PHYSICS:
Zero gravity. He hangs with no tether; the frame and body are one rigid
unit, the legs free.

NEGATIVE:
Exactly one human figure; no one on the truss. Stripes stay NAVY; the
visor stays clear glass. 0% bloom, no glow filter, no lens flare. No
readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — no markings on the frame; no caption, no
watermark. Photorealistic, 35mm film grain. Output: 16:9, 4K, no text,
no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, suit, thruster frame, framing and lighting from
the first frame.

MOTION — 8 seconds, 50mm, medium shot, fixed lockoff 2 metres behind the
man and a little to the screen-right, level with his shoulders, no cuts,
absolutely no camera movement:

SETUP: the camera is locked off behind a big man in a warm off-white
suit with NAVY stripes and a rigid white thruster frame on his back,
seen three-quarter from behind, angled screen-left, his gloves on both
control arms; the empty end of a white truss with an ORANGE rail enters
from the screen-left edge; Earth's sunlit curve fills the lower third,
black space above; hard sun from the upper screen-left.

0s — He hangs still, legs trailing free, gloves resting on the control
arms. Earth creeps beneath him. Only the edge of his cheek shows past
the helmet rim.
2s — His right thumb moves on the control. From the lower left corner of
the frame behind him, one short thin white plume, a straight sharp cone
that thins to nothing in half a second. He begins to rotate very slowly
to the screen-left, his legs swinging a beat behind his torso.
4s — On the radio, dry and amused, his voice says: "Half of this tank
goes to storytelling." He is seen from behind; no mouth in frame.
6s — At about ten degrees of rotation a second, shorter plume from the
opposite corner stops the turn. His legs drift on for a moment and
settle. One glove lifts off the control arm and taps the frame tube
twice, idly.
8s — He hangs still again, a little more turned to the screen-left than
before. No cuts.

Audio: hard vacuum — no exterior sound, not even at the plumes. Only the
radio band: faint carrier hiss, one slow breath, and his spoken line at
4 seconds heard only — never shown as text. No music.

The plumes are thin, straight, sharp cones that vanish instantly. His
rotation starts and stops only with a plume, never on its own. The frame
and suit stay one rigid unit; legs and gloves move freely. Exactly one
human figure; no one appears on the truss. The line is heard only — no
subtitles, no captions, no on-screen speaker. Single unbroken take, no
cuts, no zoom, no camera shake. 0% bloom, no glow filter, no lens flare.
No readable text, letters, digits or symbols on any display, surface,
patch or sign; no watermark. Photorealistic, 35mm film grain. [PHYSICS +
NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 8 — SAAT

`0:56 – 1:04` · 85mm · kadro A (yalnız eldivenler) · ray hizası, CU · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RB** · ÇAPA: **RB p1** (manşetler: saat ve
> halka) · DURUM: halka **6/6** (RB p2 merdiveninin ilk basamağı) ·
> saat DURMUŞ, kadran rakamsız · RA YÜKLENMEZ (yüz yok)

_"Durmuş bir saat, dolu bir halka."_

```
⛔⛔ 31.08.2026 · PROJE SAHİBİ BU SAHNEYİ İPTAL ETTİ — ÜRETİLMEYECEK
════════════════════════════════════════════════════════════════
Sebep: iki kadraj denemesi de görsel modelin politika filtresini
geçmedi (tepeden makro → ray hizası, ard arda eldivenler). Prompt
kusuru değil; kompozisyon bir politika kategorisiyle çakışıyor.

⛔ HİÇBİR ŞEY SİLİNMEDİ. Sahne dosyada duruyor, promptları geçerli,
   numaralandırma DEĞİŞMEDİ (film 120 sahne). Bu blok yalnız NOTTUR.

📋 S8 NE TAŞIYORDU — yeniden yuvalanması gerekenler:

  ① ÇEHOV 2 TOHUMU (durmuş saat) → ⚠️ ZİNCİR KOPMUYOR
     Saat dört sahnede görünüyor: S8 · S30 · S70 · S117.
     S8 giderse tohum S30'a düşer (0:56 → 3:52, 2:56 gecikme).
     S30 zaten "sağda DURMUŞ saat" diyor — ekim orada da tam.
     ⚠️ BEDEL: tohum artık ilk perdenin AÇILIŞINDA değil, YARA
        sahnesinin içinde ekiliyor; S117'nin ödemesi hâlâ çalışır
        ama "en baştan beri oradaydı" hissi zayıflar.

  ② HALKA 6/6 İLK OKUMA → 🔴 EN GERÇEK KAYIP
     Halka takvimi: S8 6/6 · S19 4/6 · S30 3/6 · S46 2/6 · S71 1/6.
     S8 gidince ilk KASITLI okuma S19'da 4/6 olur — izleyici
     sayacın DOLU hâlini hiç görmez, düşüşü ölçemez.
     ✅ ÇÖZÜM ADAYI: 6/6 okumasını S5'e (mandal ECU) ya da S9'a
        (halka zaten kadraj kenarında, odak dışı) taşı — S9'da
        odağa alınırsa ölçek yayı bozulmadan kazanılır.

  ③ ÖLÇEK YAYINDA CU BASAMAĞI → 🔴 YUVA BOŞ KALIRSA İHLAL
     S7 MS(3) → S8 CU(4) → S9 MS(3). Yuva boşalırsa S7 → S9
     aynı kademede kalır; ACI_YAYI §3 (≥1 kademe + ≥45°) düşer
     ve prompt_kontrol bunu BLOCK olarak yakalar.
     ✅ Yuvaya CU ölçeğinde başka bir sahne konursa sorun yok.
        Aday: kanca/karabina CU'su (S10'da kullanılan kancanın
        ekimi + F3-F4'ün halat sayacına bağlanır).

  ④ TEMA → ✅ ETKİLENMİYOR
     Motif sahneleri S30 · S43 · S84 · S117 (00_PLAN B3 · README
     S117 satırı · F10 KİLİT 51 — üçü de aynı listeyi veriyor).
     ⚠️ AMA bu dosyanın 20. satırı "S8 (durmuş saat)" diyerek
        S8'i motif sayıyor — BU SATIR BAYAT, üç kaynakla çelişiyor.
        Karar verilince düzeltilecek [kural ①].

  ⑤ IZGARA → ✅ SİLİNMEDİĞİ SÜRECE HİÇBİR ŞEY KAYMAZ
     Sahne silinip 119'a inilirse: F1 = 88 s olur, F2 1:28'de
     başlar, S9-S120 arası 112 sahne yeniden numaralanır, feda
     %35,0 / orta nokta %50 / doruk %78 yüzdeleri kayar, replik
     defterleri ve MUZIK_ALTERNATIFLERI'nin bütün ölçü sayıları
     yeniden türetilir. ⛔ Bu YOL SEÇİLMEDİ — sahne duruyor.

📌 KARAR BEKLEYEN TEK SORU: yuvaya ne konacak?
   (a) yeni bir CU sahnesi  (b) bu sahne başka kadrajla tekrar
   (c) yuva bilinçle boş — o zaman S7/S9 ölçekleri revize edilir
```

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit, ray hizasında, ray boyunca.
  İŞLEV: TOHUM [FINAL §3] + ÇEHOV 2 kurulumu + kişisel eşya bütçesi
  [KARAKTER §4.4]: durmuş kurmalı saat, 2 sn görünür, BAKIŞLA
  VURGULANMAZ — yüz kadraj dışı. Yanında oksijen halkası 6/6 yanık
  (rakam yok, doluluk var — Kart 5 çözümü).
  TEMA sahnesi (S8): fedakârlık motifinin taşıyıcı nesnesi ilk kez.

⚠️ 31.08.2026 · KADRAJ DEĞİŞTİ — POLİTİKA REDDİ
  ÖNCE: tepeden makro, iki manşet rayda YAN YANA, yüz yok.
  ⛔ Görsel model bu kadrajı ÜRETMEDİ (politika reddi). Sebep içerik
     değil KOMPOZİSYON: yan yana iki kol + tepeden makro + yüzsüz
     izolasyon, bir politika kategorisinin görsel imzasıyla çakışıyor.
     Önce yalnız SÖZCÜKLER değişti (bilek→ön kol, kayış→bant) —
     yetmedi; kadrajın kendisi değişti.
  SONRA: kamera RAY HİZASINDA, ray BOYUNCA bakar. İki eldiven yan yana
     DEĞİL, ray üstünde ARD ARDA (farklı derinlikte): önde sağ manşet
     (saat), onun ötesinde sol manşet (halka). Aralarında 25 cm ray var.
  ⭐ AKIŞ BOZULMADI: aynı iki nesne aynı karede, aynı 2 saniye, aynı
     bakışsızlık, aynı CU kademesi (ölçek yayı S7 MS → S8 CU → S9 MS
     bozulmadı), aynı E' kurulum ailesi, aynı ışık tarafı.
  ⭐ KAZANÇ: nesneler artık ard arda olduğu için saat ÖNDE ve NET,
     halka arkada hafif yumuşak — hangisinin filmin konusu olduğu
     kadrajla söyleniyor. Eski kadrajda ikisi eşitti.
  ⛔ "tepe" açı tipi fazda KAYBOLMADI: S5 (mandal, ECU tepeden) taşıyor.
```

### 📸 IMAGE PROMPT

```
SCENE:
Close-up along an ORANGE handrail on a spacecraft, camera at the height
of the rail and looking down its length: an astronaut's gloved right
hand grips the rail in the near foreground with a steel mechanical
watch on the suit cuff, its hands stopped; a quarter of a metre further
along the same rail her other glove grips it too, an amber ring of six
lit segments set into that cuff. She is working her way along the rail.

ENVIRONMENT:
Hard vacuum in low orbit. The rail is a white-painted tube with an
ORANGE grip sleeve, micro-scratched, running away from the lens toward
the upper screen-left. Beyond it, out of focus, the grey painted cover
of an instrument cylinder and a sliver of black space at the top edge.

SUBJECT:
Exactly one human figure, an astronaut moving along a handrail, seen
only where she touches it; the rest of her runs out of the top of frame
and is outside the shot. The gloves belong to a 38-year-old woman flight
engineer, 1.70 metres tall, slim and upright, in a warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring set into her LEFT glove cuff,
a steel mechanical watch on a black band around her RIGHT glove cuff,
its hands stopped, a flat back — smooth shell fabric, one vertical spine
seam, a low webbing waist belt — with no pack, tank, hose or cable, and
a rigid white helmet shell with a flat rectangular front glass measuring
24 by 16 centimetres, held in a visible bright metal frame the width of
a finger; the glass is optically clear with zero tint and no mirror
coating. In frame: her RIGHT glove closed round the rail in the near
foreground, lower screen-right, fingers wrapped over the ORANGE sleeve,
its padded arm running out of the top of frame, the steel watch on its
black band riding on the cuff — scratched crystal, plain dial with no
numerals, hour and minute hands both stopped. A quarter of a metre
further along the rail and higher in frame, her LEFT glove closed round
the same rail, its cuff carrying a slim ring of six square amber light
segments, all six lit steadily, no numerals. The two gloves are apart,
at different distances from the lens, each doing its own work on the
rail.

CAMERA:
Shot on an 85mm lens, close-up, from a fixed position 0.5 metres from
the near glove, at eye-level with the rail, looking along its length.
Shallow depth of field: the near cuff and the watch razor sharp, the
far cuff and its ring a little softer but still readable.

COMPOSITION: 16:9 horizontal. The rail runs diagonally from the lower
screen-right to the upper screen-left. The near glove and the watch sit
at thirty percent of frame width and thirty percent of frame height;
the far glove and the ring sit at sixty-five percent of frame width and
sixty percent of frame height. Between them, a clear run of ORANGE
rail. The upper screen-right quarter carries only out-of-focus grey
cover. LIGHTING: Hard white sun from the upper screen-right, catching
the watch crystal as one small hard highlight; blue-white bounce fills
the shadow side of the gloves; the six segments are small, steady,
sharp-edged amber lights with no halo. No haze, no lens flare.

PHYSICS:
Zero gravity. The gloves rest without weight; the free tail of the
watch band floats a few millimetres off the cuff instead of hanging.

NEGATIVE:
Exactly one human figure, an astronaut at work on a handrail. The two
gloves stay apart at different depths and never lie together, never
touch each other and are never crossed. Both gloves are intact, clean
and undamaged; the suit sleeves are unbroken and sealed at both cuffs.
No second person's hand. The watch dial carries no numerals, no letters,
no brand; the ring carries no numerals. 0% bloom, no glow filter, no
lens flare, no halo. No readable text, letters, digits, numbers or
symbols on any display, surface, patch or sign; no caption, no
watermark. Photorealistic, 35mm film grain. Output: 16:9, 4K, no text,
no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, gloves, watch, ring, framing and lighting from
the first frame.

MOTION — 8 seconds, 85mm, close-up, fixed lockoff 0.5 metres from the
near glove, at eye-level with the rail, looking along its length,
shallow focus, no cuts, absolutely no camera movement:

SETUP: the camera looks along an ORANGE handrail running from the lower
screen-right to the upper screen-left. Near foreground: an astronaut's
off-white gloved right hand on the rail, ORANGE cuff stripe, padded arm
leaving the top of frame, a steel mechanical watch on a black band on
that cuff, its hands stopped. A quarter of a metre along the rail and
higher in frame, her other glove holds the same rail, six amber
segments lit in that cuff. Between them, clear ORANGE rail. Hard sun
upper screen-right, one hard highlight on the watch crystal.

0s — Both gloves hold the rail, apart, at their own depths. The watch
hands do not move. The six segments hold steady. The band's free tail
floats a few millimetres off the cuff.

2s — The near glove closes on the rail until the fabric creases at the
knuckles and holds two seconds; the far glove does not move. Watch and
ring sit still in the same light. Nothing turns toward the watch.

4s — The near fingers open one at a time; the band's free tail drifts
up a few more millimetres and stays. The run of bare rail between the
two gloves never closes.

6s — One tiny fleck of dust crosses the frame on a dead straight line,
screen-left to screen-right, at constant speed, and leaves.

8s — Both gloves still on the rail, still apart, watch stopped, six
segments lit. No cuts.

Audio: hard vacuum — no exterior sound. Inside the suit: two slow
breaths, a faint radio carrier hiss, and the glove fabric creaking as
the grip tightens. No voice, no music.

The watch hands never move; the dial stays plain with no numerals; the
six segments stay lit and steady. The gloves keep a clear boundary with
the rail — no merging, no extra fingers. Nothing hangs; the band's tail
floats. Exactly one human figure, an astronaut at work on a handrail,
seen only where she touches it, the rest of her out of frame above; the
gloves stay apart at different depths, never lie together, never touch,
are never crossed; both sleeves sealed at the cuffs; no second person's
hand. Single unbroken take, no cuts, no zoom, no camera shake. 0%
bloom, no glow filter, no halo, no lens flare. No readable text,
letters, digits or symbols on any display, surface, patch or sign; no
subtitles, no caption, no watermark. Photorealistic, 35mm film grain.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 9 — KAPANIŞ CIVATASI

`1:04 – 1:12` · 50mm · kadro A · 3/4 arkadan, MS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** + **RD** · ÇAPA: **RA p3** (SIRT — düz,
> D79 kanıtı; bu sahne o panelin sinematik hâlidir) + RD p3 (panel) ·
> DURUM: alt mandal oturur, kapak MÜHÜRLÜ · halka 6/6 kadraj kenarında

_"PANEL SEALED. OXYGEN NINETY-ONE PERCENT."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera A'nın arkasında 3/4 — ağız yok.
  İŞLEV: ÇEHOV 1 kurulumu — suit AI'ın rutin oksijen anonsu; sayı yalnız
  MACHINE seste [D82], ekranda rakam 0; halka 6/6 (kadraj kenarında,
  odak dışı — vurgu yok). Replik 1:09 — SUIT AI, MACHINE, kask içi. A
  konuşmaz.
```

### 📸 IMAGE PROMPT

```
SCENE:
Medium shot, three-quarter from behind, of a woman astronaut at a closed
grey panel cover on an instrument cylinder, her right glove on the last
latch lever, Earth's sunlit limb in the lower right of frame.

ENVIRONMENT:
Hard vacuum in low orbit. The four-metre grey instrument cylinder fills
the screen-left half of frame, its hinged access cover closed, the upper
latch lever already seated, the lower one under her hand. A white
lattice truss with an ORANGE handrail runs out of frame to the
screen-right. Earth's cloud-streaked blue-white curve in the lower
right; black space with hard pinpoint stars above.

SUBJECT:
Exactly one human figure. A 38-year-old woman flight engineer, 1.70
metres tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the hairline,
dark chestnut jaw-length hair tucked behind both ears. Warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring on her LEFT wrist, a steel
mechanical watch on a black strap over her RIGHT glove cuff, its hands
stopped. Her back silhouette is flat: smooth off-white shell fabric, one
vertical spine seam, a low webbing waist belt, and no pack, tank, hose
or cable. Her helmet is a rigid white shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear, zero
tint, no mirror coating, and her face is fully readable through it. Seen
three-quarter from behind, framed from the knees up, her flat back to
camera, helmet turned to the panel so only the edge of her cheek shows
and her mouth is hidden; right glove on the lower latch lever, left
glove on the rail, tether straight from hip to rail, legs trailing free.

CAMERA:
Shot on a 50mm lens, medium shot, from a fixed position 2.5 metres
behind her and a little to the screen-right, at her shoulder height.
Deep focus.

COMPOSITION: 16:9 horizontal. She stands at forty-five percent of frame
width, waist at fifteen percent and helmet at seventy-eight percent of
frame height; the panel and its last latch fill the screen-right third.
The bottom sixth carries only lattice. LIGHTING: Hard white sun from the
upper screen-right, rimming her helmet and right shoulder, a razor-edged
black shadow of her body across the grey cover; blue-white bounce from
Earth below fills the shadow side. No haze, no lens flare.

PHYSICS:
Zero gravity. Tether taut; legs free; nothing hangs.

NEGATIVE:
Exactly one human figure — no second person. Her back stays flat with no
pack, tank, hose or cable; stripes stay ORANGE; the visor stays clear
glass. 0% bloom, no glow filter, no lens flare. No readable text,
letters, digits, numbers or symbols on any display, surface, patch or
sign — no stencil on the cover; no caption, no watermark.
Photorealistic, 35mm film grain. Output: 16:9, 4K, no text, no
watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, suit, framing and lighting from the first frame.

MOTION — 8 seconds, 50mm, medium shot, fixed lockoff 2.5 metres behind
the woman and a little to the screen-right, at her shoulder height, no
cuts, absolutely no camera movement:

SETUP: the camera is locked off three-quarter behind a woman flight
engineer in a warm off-white suit with ORANGE stripes, clear visor, flat
back, framed from the knees up at a closed grey panel cover on an
instrument cylinder that fills the screen-left half; her right glove on
the lower latch lever, left glove on an ORANGE rail, tether straight to
the rail; Earth's sunlit limb in the lower right, black space above;
hard sun from the upper screen-right rims her helmet.

0s — Her right glove is closed on the lower latch lever, her helmet
turned to the panel so only the edge of her cheek shows.

2s — She turns the lever a quarter turn; her body swings a few
centimetres the other way against the taut tether, then settles. The
lever seats.

4s — Inside her helmet, a flat synthetic voice says evenly: "PANEL
SEALED. OXYGEN NINETY-ONE PERCENT." No mouth in frame; she does not
react to it beyond a slow exhale.

5s — She lifts her right glove off the lever and pats the cover once,
flat-palmed, and leaves the hand resting there.

7s — Her helmet turns a few degrees to the screen-right, toward the rail
and the camera side, the edge of her cheek catching the sun; her legs
drift and settle.

8s — She holds at the sealed panel, still. No cuts.

Audio: hard vacuum — no exterior sound. Inside the helmet: a dull
muffled thud through the glove as the lever seats, one slow exhale, a
faint carrier hiss, and the flat synthetic announcement at 4 seconds
heard only — never shown as text. No music.  Her back stays flat with no
pack, tank, hose or cable; stripes stay ORANGE; the visor stays clear
glass. Her body is never rigid: drift, counter-drift, legs settling,
small helmet turn. She never speaks: mouth hidden, no lip movement.
Exactly one human figure — no second person. The announcement is heard
only — no subtitles, no captions. Single unbroken take, no cuts, no
zoom, no camera shake. 0% bloom, no glow filter, no lens flare. No
readable text, letters, digits or symbols on any display, surface, patch
or sign — no stencil on the cover; no watermark. Photorealistic, 35mm
film grain. [PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 10 — İKİ SES

`1:12 – 1:20` · 24mm · kadro 2 · göz hizası, WS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** + **RC** + **RD** · ÇAPA: RC p3 (⭐ A+B
> yan yana — boy/renk/sırt farkı) + RD p1 (SAĞLAM geniş) + RD p4 (mekik)
> · DURUM: A kancayı takar, B uzakta küçük · mekik burnu EKRAN-SOLA · ⛔
> S4 tetik sahnesi geçmeden üretilmez [D68]

_"Closing out." — "Copy. Take the long way back."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit, geniş. İŞLEV: iki ses, iki
  gövde, tek kadraj (kadro-2 bütçesinden 2/14): A rayda kancayı takar, B
  uzakta küçük. Yüzler küçük ve dönük — "no lip-sync required" (şablon
  checklist'i). İki gövdeye AYRI hareket; B'nin pufu ince düz koni.
  Mekik burnu EKRAN-SOLA. Replikler 1:13 (A) · 1:16 (B), telsiz.
```

### 📸 IMAGE PROMPT

```
SCENE:
A wide lateral view at eye level with the platform: a woman astronaut in
full body at the left-centre clips a tether karabiner to an ORANGE
handrail; far to the screen-right, small, a big man in a back-mounted
thruster frame hangs free between the truss and a winged shuttle whose
nose points screen-left; Earth's sunlit limb fills the lower third.

ENVIRONMENT:
Hard vacuum in low orbit. A thirteen-metre white lattice truss with
ORANGE handrails crosses the middle of frame from left to right; the
four-metre grey instrument cylinder with its sealed access cover sits at
its screen-left end. Forty metres beyond the truss to the screen-right,
a white thirty-seven-metre shuttle hangs in the black, nose pointing
screen-left, its cargo bay doors open and their white inner faces
catching sun. Earth's cloud-streaked blue-white curve below; black space
with hard pinpoint stars above.

SUBJECT:
Exactly two human figures, human count 2, far apart. LEFT-CENTRE, full
body: a 38-year-old woman flight engineer, 1.70 metres tall, slim and
upright: oval face, soft defined jawline, light wheat-toned skin with
visible pores, thin straight nose, dark hazel eyes, a short vertical
pale scar on her LEFT temple near the hairline, dark chestnut jaw-length
hair tucked behind both ears. Warm off-white pressure suit with ORANGE
reinforcement stripes on shoulders, knees and glove cuffs, a soft chest
panel with three small coloured lights and no numerals, a six-segment
amber oxygen ring on her LEFT wrist, a steel mechanical watch on a black
strap over her RIGHT glove cuff, its hands stopped. Her back silhouette
is flat — no pack, tank, hose or cable. Her helmet is a rigid white
shell with a flat rectangular front glass measuring 24 by 16
centimetres, held in a visible bright metal frame the width of a finger;
the glass is optically clear, zero tint, no mirror coating, and her face
is fully readable through it. Seen in profile facing screen-right, both
gloves on a karabiner at the rail, legs trailing free. FAR SCREEN-RIGHT,
small: a 52-year-old man mission commander, 1.85 metres tall, broad and
heavy, in the same warm off-white suit with NAVY reinforcement stripes
and a rigid white aluminium thruster frame on his back, as deep as a
forearm, with two control arms reaching forward and eight small nozzles
at its corners, spherical helmet with an optically clear visor, hanging
free, turned three-quarter away. The two suits differ in reinforcement
colour — orange for the woman, navy for the man — and never swap; only
the man carries the rigid thruster frame; he is 15 cm taller.

CAMERA:
Shot on a 24mm lens, wide shot, from a fixed position 9 metres away
level with the truss, eye-level, Earth's horizon perfectly horizontal.
Deep focus, true scale between the two figures, the truss and the
shuttle.

COMPOSITION: 16:9 horizontal. The platform runs across the lower half;
she stands at thirty percent of frame width with boots at forty-two
percent and helmet at seventy percent of frame height, and he reads as a
small figure at eighty percent of frame width and fifteen percent of
frame height. LIGHTING: Hard white sun from the upper screen-right;
blue-white bounce from Earth below; razor-edged black shadows across the
truss; the shuttle's cargo doors a bright white plane. No haze, no lens
flare.

PHYSICS:
Zero gravity. Her tether straight; he hangs with no tether; nothing
hangs or settles.

NEGATIVE:
Exactly two human figures, no third, no crew in the shuttle. Stripes
never swap; only the man has the frame; both visors clear glass. 0%
bloom, no glow filter, no lens flare. No readable text, letters, digits,
numbers or symbols on any display, surface, patch or sign — no markings
on the shuttle; no caption, no watermark. Photorealistic, 35mm film
grain. Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain both subjects, suits, framing and lighting from the first
frame.

MOTION — 8 seconds, 24mm, wide shot, fixed lockoff 9 metres away,
eye-level with the truss, no cuts, absolutely no camera movement:

SETUP: the camera is locked off level with a white lattice truss
crossing the frame; a woman flight engineer in a warm off-white suit
with ORANGE stripes, clear visor, flat back, full body at the
left-centre in profile facing screen-right, both gloves on a karabiner
at the ORANGE rail; far screen-right, small, a big man in the same suit
with NAVY stripes and a rigid white thruster frame on his back hangs
free between the truss and the white shuttle, nose pointing screen-left,
cargo doors open; Earth's sunlit limb across the lower third, black
space above; hard sun from upper screen-right. Faces are small and
turned away — no lip-sync required.

0s — Her gloves are on the karabiner at the rail. He hangs still, far
screen-right.
1s — On the radio, her voice, quiet and even, says: "Closing out." Her
face is small and in profile; no lip movement needed.
2s — The karabiner gate snaps shut under her thumb. She pushes off the
rail gently with her left hand and begins to move hand over hand along
the rail to the screen-right, her legs trailing a beat behind, the
tether sliding along with her.
4s — On the radio, his voice, warm and unhurried, says: "Copy. Take the
long way back." He is small and turned away; no lip movement needed. One
short thin white plume from a corner of his frame; he eases a metre to
the screen-left and stops — two bodies, two motions.
6s — She reaches the next rail post and pauses, one glove on it, her
body drifting past and swinging back. He hangs still.
8s — She holds at the post, mid-way along the truss; he hangs far right;
the shuttle has not moved. No cuts.

Audio: hard vacuum — no exterior sound, even at the plume. Only the
radio band: faint carrier hiss, two spoken lines at 1 and 4 seconds
heard only — never shown as text, two slow breaths. No music.

The two bodies move independently and never share one motion. The
shuttle keeps its nose pointing screen-left and never moves. Exactly two
human figures, human count 2, no third, no crew. Stripes never swap;
only the man has the frame. Lines heard only — no subtitles, no
captions, no on-screen speaker. Single unbroken take, no cuts, no zoom,
no pan, no camera shake. 0% bloom, no glow filter, no lens flare. No
readable text, letters, digits or symbols on any display, surface, patch
or sign; no watermark. Photorealistic, 35mm grain. [PHYSICS + NEGATIVE
bibles apply throughout]
```

---

## 🎬 SAHNE 11 — İRONİ

`1:20 – 1:28` · 24mm · kadro 2 · üst açı 25°, EWS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** + **RC** + **RD** · ÇAPA: RD p1 (SAĞLAM geniş,
> üstten) + RC p3 (iki figür ayrışması) · DURUM: iki figür kadrajın ≤%10'u ·
> ⭐ gökte İNCE PARILTI ÇİZGİSİ — kadrajın üst SOL köşesinde, uzakta, zayıf

_"İzleyici görür. Onlar görmez."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera hiç hareket etmez.
  İŞLEV: BİLGİ ASİMETRİSİ / DRAMATİK İRONİ açılır [HOOK §3.1] —
  taşıyıcı ARKA PLAN HAREKETİ: gökte ince, güneşte parlayan bir çizgi
  sekiz saniyede biraz uzar. İki figür çalışmaya devam eder, başını
  kaldırmaz. Enkaz teması S11'e kadar kadraj dışıydı [D71]; burada
  girer ama YALNIZ uzak ve küçük — reveal değil, ipucu.
  Kadro 2 (bütçeden 3/14): iki figür ayrı uçlarda, iki ayrı hareket.
```

### 📸 IMAGE PROMPT

```
SCENE:
From high above the orbital service platform, the same framing as the
opening: the white lattice truss in the right third of frame with two
tiny astronauts on it, the sunlit curve of Earth filling the left two
thirds and the bottom — and, in the upper left corner of the black, far
beyond the platform, a thin faint line of sunlit specks like a scratch
of light on the dark.

ENVIRONMENT:
Hard vacuum in low orbit. Earth's cloud-streaked blue-white surface
curves across the lower and left frame; black space with a few hard
pinpoint stars in the upper right. The platform: a thirteen-metre white
lattice truss with ORANGE handrails, at its end a four-metre grey
cylindrical instrument body with its access cover sealed. In the upper
left, very small and far, a straight thin line of tiny sunlit points,
parallel to one another. No spacecraft in frame.

SUBJECT:
Exactly two human figures, human count 2, both tiny at one tenth of
frame height, far apart on the truss. Near the middle of the truss: a
38-year-old woman flight engineer, 1.70 metres tall, slim and upright,
in a warm off-white pressure suit with ORANGE reinforcement stripes on
shoulders, knees and glove cuffs, a soft chest panel with three small
coloured lights and no numerals, a six-segment amber oxygen ring on her
LEFT wrist, a steel mechanical watch on a black strap over her RIGHT
glove cuff; her back silhouette flat — no pack, tank, hose or cable; a
rigid white helmet shell with a flat rectangular front glass measuring
24 by 16 centimetres, held in a visible bright metal frame the width of
a finger; the glass is optically clear with zero tint and no mirror
coating; one glove on a rail post, tether line straight to the rail.
Near the truss's screen-right end: a 52-year-old man mission commander,
1.85 metres tall, broad and heavy, in the same off-white suit with NAVY
reinforcement stripes and a rigid white aluminium thruster frame on his
back with two forward control arms and eight small corner nozzles,
spherical helmet with an optically clear visor, hanging free beside the
truss. The two suits differ in reinforcement colour — orange for the
woman, navy for the man — and never swap; only the man carries the
frame.

CAMERA:
Shot on a 24mm lens, extreme wide shot, from a fixed position 40 metres
away above the platform, high-angle looking down, camera pitched down 25
degrees. Deep focus. Physically accurate perspective, true scale between
the tiny figures, the truss and the planet.

COMPOSITION: 16:9 horizontal. The platform sits in the screen-right
third, the two figures each under seven percent of frame height at forty
percent of frame height. The debris line runs across the upper third
from the screen-left edge to sixty percent of frame width. LIGHTING:
Hard white sun from the upper screen-right; soft blue-white bounce from
Earth below and to the left; shadows on the truss absolute black. The
distant line of specks is lit by the same sun — bright, sharp, no halo.
No haze, no lens flare.

PHYSICS:
Zero gravity. Her tether straight; he hangs free. The distant line is
still in this frame. The debris line grows from a hairline to about a
fifth of frame width across the shot; the two figures do not move
relative to the platform. NEGATIVE: Exactly two human figures, no third.
Stripes never swap; only the man has the frame. The distant specks are
sharp points — no glow, no streak blur. 0% bloom, no glow filter, no
lens flare. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign; no title card, no caption, no
watermark. Photorealistic, 35mm film grain. Output: 16:9, 4K, no text,
no watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain both subjects, the platform, the framing and the lighting from
the first frame.

MOTION — 8 seconds, 24mm, extreme wide shot, fixed lockoff 40 metres
away above the platform, high-angle looking down, camera pitched down 25
degrees, no cuts, absolutely no camera movement:

SETUP: the camera is locked off high above the platform; Earth's sunlit
curve fills the left two thirds and the bottom, black space in the upper
right; the white truss with ORANGE rails in the right third with two
tiny figures — a woman flight engineer in an off-white suit with ORANGE
stripes and a flat back at a rail post near the middle, tethered; a big
man in the same suit with NAVY stripes and a rigid white thruster frame
on his back hanging free near the screen-right end. In the upper left
corner of the black, far away, a thin faint straight line of sunlit
specks.

0s — Both figures are at work: her glove on the rail post, his gloves on
his control arms. The distant line of specks is faint and short. Earth's
cloud bands creep beneath.
2s — The line of specks grows very slightly longer and a little
brighter, still tiny, still far. Neither figure looks up.
4s — She moves one post along the rail, hand over hand, to the
screen-right, her legs trailing a beat behind; separately, one short
thin white plume from his frame and he eases half a metre and stops.
6s — The line of specks is now clearly longer than at 0s — a fine bright
scratch on the dark — still unnoticed; both helmets stay down on their
work.
8s — Both figures hold; the line hangs there in the upper left, brighter
than when the shot began. No cuts.

Audio: hard vacuum — no exterior sound. Inside the helmets, two slow
calm breaths on the radio band and a faint carrier hiss. No voice, no
music.

The two figures move independently and never share one motion. The
distant specks stay sharp points in a straight line — no glow, no blur,
no flare — and never come near the platform in this shot. Exactly two
human figures, human count 2, no third. Single unbroken take, no cuts,
no zoom, no camera shake. 0% bloom, no glow filter, no lens flare. No
readable text, letters, digits or symbols on any display, surface, patch
or sign; no subtitles, no caption, no watermark. Photorealistic, 35mm
film grain. [PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🎬 SAHNE 12 — STATİK

`1:28 – 1:36` · 24mm · kadro A · göz hizası, WS · fixed lockoff

> 🎯 **REFERANS** · YÜKLE: **RA** + **RD** · ÇAPA: RA p1 (tam boy) + RD p1
> (SAĞLAM geniş; mekik burnu EKRAN-SOLA) · DURUM: KONTROL bandı statiğe
> döner — ses olayı, görsel değişim yok · çizgi üst SOL köşede, A'nın
> ARKASINDA (o mekiğe bakar) · B kadraj DIŞI

_"Ses kesilir. Başını kaldırır — yanlış yöne."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 8,0 s. Kamera sabit.
  İŞLEV: FAZ KAPANIŞI — KONTROL'ün taşıyıcısı çatırdayıp düz statiğe
  iner; A başını kaldırır ama MEKİĞE bakar (ekran-sağ), çizgi
  arkasındadır (ekran üst-sol): ironi bir kademe daha sıkılır.
  Replik YOK (KONTROL'ün S13 iptal repliği bir sonraki fazın ilk
  sahnesindedir). Tepki çapası: baş kalkar, eldiven kaskın yanına gider.
```

### 📸 IMAGE PROMPT

```
SCENE:
A wide lateral view at eye level with the platform: a lone woman
astronaut, full body, mid-way along the truss with one glove on a rail
post, her helmet turned to the screen-right where a winged shuttle hangs
far off, nose pointing screen-left, cargo bay doors open; Earth's sunlit
limb fills the lower third; in the upper left of the black behind her,
faint and far, a thin line of sunlit specks.

ENVIRONMENT:
Hard vacuum in low orbit. A thirteen-metre white lattice truss with
ORANGE handrails runs across the middle of frame from left to right; the
four-metre grey instrument cylinder with its sealed access cover sits at
its screen-left end. Forty metres beyond the truss to the screen-right,
a white thirty-seven-metre shuttle hangs in the black, nose pointing
screen-left, its cargo bay doors open and their white inner faces
catching sun. Earth's cloud-streaked blue-white curve below; black space
with hard pinpoint stars above; in the upper left corner, a short faint
straight line of tiny sunlit points.

SUBJECT:
Exactly one human figure. A 38-year-old woman flight engineer, 1.70
metres tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the hairline,
dark chestnut jaw-length hair tucked behind both ears. Warm off-white
pressure suit with ORANGE reinforcement stripes on shoulders, knees and
glove cuffs, a soft chest panel with three small coloured lights and no
numerals, a six-segment amber oxygen ring on her LEFT wrist, a steel
mechanical watch on a black strap over her RIGHT glove cuff, its hands
stopped. Her back silhouette is flat: smooth off-white shell fabric, one
vertical spine seam, a low webbing waist belt, and no pack, tank, hose
or cable. Her helmet is a rigid white shell with a flat rectangular
front glass measuring 24 by 16 centimetres, held in a visible bright
metal frame the width of a finger; the glass is optically clear, zero
tint, no mirror coating, and her face is fully readable through it. Seen
in profile facing screen-right, right glove on a rail post, left glove
free at her side, legs trailing, tether line straight to the rail; her
helmet lifted, looking at the distant shuttle.

CAMERA:
Shot on a 24mm lens, wide shot, from a fixed position 9 metres away
level with the truss, eye-level, Earth's horizon perfectly horizontal.
Deep focus; true scale: figure, truss, shuttle.

COMPOSITION: 16:9 horizontal. The platform runs across the lower half;
she stands at thirty-five percent of frame width, boots at forty-two
percent and helmet at seventy-two percent of frame height, her head
tipped toward the screen-right quarter where the shuttle sits small.
LIGHTING: Hard white sun from the upper screen-right; soft blue-white
bounce from Earth below; razor-edged black shadows across the truss; the
distant specks sharp and bright, no halo. No haze, no lens flare.

PHYSICS:
Zero gravity. Tether taut and straight; legs float apart; nothing hangs.

NEGATIVE:
Exactly one human figure — no second person, no crew in the shuttle.
Stripes stay ORANGE; the visor stays clear glass; her back stays flat.
0% bloom, no glow filter, no lens flare. No readable text, letters,
digits, numbers or symbols on any display, surface, patch or sign — no
markings on the shuttle; no title card, no caption, no watermark.
Photorealistic, 35mm film grain. Output: 16:9, 4K, no text, no
watermark.
```

### 🎥 VIDEO PROMPT — 8 saniye, tek kesintisiz çekim

```
Maintain the subject, suit, framing and lighting from the first frame.

MOTION — 8 seconds, 24mm, wide shot, fixed lockoff 9 metres away,
eye-level with the truss, no cuts, absolutely no camera movement:

SETUP: the camera is locked off level with the white truss crossing the
frame; a woman flight engineer in a warm off-white suit with ORANGE
stripes, clear visor, flat back, full body in profile facing
screen-right, one glove on a rail post, tether straight to the rail; the
white shuttle far in the right third with its nose pointing screen-left
and cargo doors open; Earth's sunlit limb across the lower third, black
space above; in the upper left corner of the black, faint and far, a
thin line of sunlit specks behind her.

0s — She is moving hand over hand along the rail to the screen-right,
her legs trailing a beat behind her.
2s — The steady radio carrier hiss breaks up into rough, uneven static.
She stops mid-reach, one glove on the post, and holds.
4s — The static flattens into a dead, even tone. She lifts her helmet
and turns her face to the screen-right, to the distant shuttle, and
holds there — the line of specks is behind her, in the upper left, and
she does not turn that way.
6s — Her free left glove rises and touches the side of her helmet, a
small radio-check gesture, then lowers. Her legs drift and settle.
8s — She holds at the post, looking at the shuttle; in the upper left
the faint line is a fraction longer than at 0s. No cuts.

Audio: hard vacuum — no exterior sound. Inside the helmet: her slow
breathing, and the radio band — a steady carrier hiss at 0 seconds that
breaks into rough static at 2 seconds and flattens into a dead even tone
by 4 seconds, then nothing but that tone. No voice, no music.

Her body is never rigid: drift, counter-drift, legs settling, helmet
turn. The shuttle keeps its nose pointing screen-left and never moves.
The distant specks stay sharp points, no glow, and never come near the
platform in this shot. Exactly one human figure — no second person.
Single unbroken take, no cuts, no zoom, no pan, no camera shake. 0%
bloom, no glow filter, no lens flare. No readable text, letters, digits
or symbols on any display, surface, patch or sign; no subtitles, no
caption, no watermark. Photorealistic, 35mm film grain. [PHYSICS +
NEGATIVE bibles apply throughout]
```

---

# 🔗 FAZ SONU BAĞLANTI NOTU

```
Bu fazın son karesi (S12 · 1:36): A ray direğinde, başı mekiğe dönük
(EKRAN-SAĞ); telsiz bandı düz statik; çizgi üst SOL köşede, arkasında;
mekik burnu EKRAN-SOL; güneş üst EKRAN-SAĞ; halka 6/6; platform SAĞLAM.
Sonraki faza köprü: SES KÖPRÜSÜ — S12'nin düz statiği S13'te aynı
bantta "geri gelir" ve KONTROL'ün iptal repliğine açılır.
S13'ün ilk karesi: MS, A'nın omzundan (OTS), aynı direk, aynı ışık.
Renk sıcaklığı devri: L1 gündüz → L1 gündüz (F2 aynı ışık).
Faz 2 dosyası: `../FAZ_02_DALGA/FAZ_02_DALGA.md`.
```

---

# ✅ FAZ 1 TESLİM KONTROLÜ

```
□ 12 sahne · 12 image (start frame) · 12 video (I2V) — zincir kararı KİLİT 1
□ Karakter çapa bloğu: A 8 tam blokta, B 3 tam blokta kelimesi kelimesine
  (el insertlerinde S5 · S6 · S8 ve uzak S11'de kısaltılmış sürüm — yüz
  kadraj dışı/okunmaz, kimlik giysi/eldivenle taşınır)
□ [BIBLE] etiketi 0 · Türkçe gövde 0 · özel ad 0
□ Her video: "Maintain ... from the first frame" + No cuts + negatif
□ Replikli sahnelerde "heard only — never shown as text"; geniş çekimde
  "no lip-sync required" (S10)
□ Ekranda okunan ağız: 0/12 · kasksız: 0/12 · rakam: 0
□ Ardışık kurulum çiftleri: 11/11 tam 1 kademe + ≥45° (KİLİT 3)
☑ prompt_kontrol.py koşuldu (29.08.2026): ⛔ 0 BLOCK · kurulum/açı/
  tema/D79/yönelim kapıları temiz · video 2.145-2.600 bant içi ·
  image 2.404-3.343 — bandın ÜSTÜNDE ama betik bunu GÖZLEM sayar
  (bant karara bağlı; emsaller Holding Field 3.417-4.017 · Third Dune
  2.732-4.154, hepsi üretildi). Bilinçli: image promptu çapa bloğunu
  tam taşır; kısaltma sırası gerekirse ENVIRONMENT → LIGHTING → SCENE.
  İlk koşudaki iki bulgu kapatıldı: iki-figürlü sahnelerde "human
  count 2" imzası eklendi · S10 video 2.651 → bant içine kırpıldı.
  S11-S12 eklenince (24 prompt) yine GO; betik NOT: "kurulum sayısı 9 —
  üst bant 6" — bilinçli, gerekçe README §Camera bloğunda [D74]
  (mesafe varyantı ayrı imza sayılıyor; bant tek film içindir, faz
  bir üretim paketidir).
```
