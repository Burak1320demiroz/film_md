# 🧷 THE SECOND SHIP — Referans Paketi

## ADIM 3 — Kimlik Çapası Master Referans İmajları
### 4 master referans: Kaptan · Mühendis · Bekçi · CANTOR | 16:9 Yatay

> **Bu dosyanın amacı:** 120 sahne / 150 imaj boyunca karakter ve gemi
> kimliğinin KAYMASINI önlemek. Her fazın çapa imajı **bu dosyadaki master
> referanstan** üretilir, bir önceki fazın çıktısından DEĞİL
> (faz başı kimlik yenileme protokolü — README §FORMAT KARARLARI madde 5).
>
> **Kullanım kuralı:**
> 1. Master referans bir kez üretilir, beğenilen imajın **seed'i kaydedilir**.
> 2. Faz dosyalarındaki her image prompt, karakter tarifini buradaki
>    SUBJECT bloğundan **kelimesi kelimesine** kopyalar (Bible atfı yasak —
>    prompt self-contained'dır, AGENTS.md kural ③).
> 3. İki karakterli sahnelerde KARIŞMA KİLİDİ cümlesi eklenir (aşağıda).
> 4. Ad prompt gövdesine YAZILMAZ [Ders 34/45] — burada da yazılmadı.

---

## 📸 REFERANS 1 — KAPTAN (master, 3/4 ön, tam boy)

> Seed: `________` · Üretim tarihi: `__.__.____` · Durum: ☐ üretildi

```
SCENE:
Master identity reference plate — a 41-year-old woman pilot stands at
rest for a full-body reference, facing three-quarter front, arms held
slightly away from her body, expression neutral and composed.

ENVIRONMENT:
Bare dark basalt plain under a pale grey-green sky, horizon empty, one
large pale moon as a faint daytime disk. Fine settled dust. No
structures, no wreckage.

SUBJECT:
A naturally beautiful woman with a symmetrical face and high
cheekbones. Light olive skin with visible pore texture and natural
subsurface scattering. Sharp jawline, thin lips, dark grey-green eyes.
A fine, faded white scar splits her LEFT eyebrow in two. No makeup.
Dark brown hair in a tight low bun, subtle silver strands at the
temples. She is 1.68 m tall, slim and graceful, with an upright
posture. She wears a dark grey-blue pressure suit with
ORANGE worn reinforcement panels on the shoulders, elbows and knees. On
the chest sit three abstract indicators — a slow blue pulse, an amber
bar, a green dot — purely abstract light, no text. Her left forearm
carries an abstract panel of slowly sliding segments. Integrated helmet
with a fully transparent, seamless visor; her face reads clearly through
the glass. The right glove shows a visible detachable ring at the wrist.
Hands empty.

CAMERA:
Shot on a 50mm lens from a fixed position four meters away, f/5.6, eye
level, full body in frame. Physically accurate perspective, true
1.68 m human scale against the ground.

LIGHTING:
Soft orange daylight from a small orange star, 4400K. Soft-edged
shadows from a thin atmosphere. Every surface keeps its texture — suit
scuffs, skin pores, and a visor reflection that matches the sky.

NEGATIVE:
Exactly one figure in frame — no duplicates, no extra people. No
readable text, letters, digits or symbols on any panel or surface. The
visor stays a distinct transparent glass surface and never disappears.
No bloom, no glow filter, no lens flare, no waxy skin, no airbrushing,
no face morphing. No subtitles, no captions, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

---

## 📸 REFERANS 2 — MÜHENDİS (master, 3/4 ön, tam boy)

> Seed: `________` · Üretim tarihi: `__.__.____` · Durum: ☐ üretildi

```
SCENE:
Master identity reference plate — a 33-year-old man flight engineer
stands at rest for a full-body reference, facing three-quarter front,
arms relaxed and held slightly away from his body, expression neutral.

ENVIRONMENT:
Bare dark basalt plain under a pale grey-green sky, horizon empty, one
large pale moon as a faint daytime disk. Fine settled dust. No
structures, no wreckage.

SUBJECT:
A handsome man with strong, symmetrical features and a defined
jawline. Light brown skin with visible pore texture. Short, neat,
three-day black stubble. Straight nose, full lips, dark brown eyes. On
his RIGHT cheekbone, a 2 cm old burn scar — a subtle, shiny mark that
suits his rugged look. Black hair, very short and dense. He is 1.81 m
tall, athletic, muscular and broad-shouldered. He
wears a dark grey-blue pressure suit with TEAL GREEN worn
reinforcement panels on the shoulders,
elbows and knees. His back unit is visibly larger than standard — a
bulky tool module. On his left hip sits a closed cutting-tool sheath,
tool stowed and not visible. On the chest sit three abstract indicators
— a slow blue pulse, an amber bar, a green dot — purely abstract light,
no text. Integrated helmet with a fully transparent, seamless visor; his
face reads clearly through the glass. Hands empty.

CAMERA:
Shot on a 50mm lens from a fixed position four meters away, f/5.6, eye
level, full body in frame. Physically accurate perspective, true
1.81 m human scale against the ground.

LIGHTING:
Soft orange daylight from a small orange star, 4400K. Soft-edged
shadows from a thin atmosphere. Every surface keeps its texture — suit
scuffs, skin pores, stubble, and a visor reflection that matches the
sky.

NEGATIVE:
Exactly one figure in frame — no duplicates, no extra people. No
readable text, letters, digits or symbols on any panel or surface. The
visor stays a distinct transparent glass surface and never disappears.
No bloom, no glow filter, no lens flare, no waxy skin, no airbrushing,
no face morphing. No subtitles, no captions, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

### ⚠️ KARIŞMA KİLİDİ — iki karakterli her sahne promptuna eklenecek cümle

```
The two human suits differ in reinforcement colour — orange for the
woman, teal for the man — and never swap; their heights differ by 13 cm
in every frame: the woman is 1.68 m, slim and graceful; the man is
1.81 m, athletic and broad-shouldered. The woman wears a tight low bun
and has no facial hair; the man has very short black hair and neat
three-day stubble.
```

---

## 📸 REFERANS 3 — BEKÇİ (master, mühürlü, tam boy)

> Seed: `________` · Üretim tarihi: `__.__.____` · Durum: ☐ üretildi
> ⚠️ "alien" kelimesi promptta KULLANILMAZ (model çizgi filme çeker).
> ⚠️ S103 yüz imajı bu referanstan ÜRETİLMEZ — ayrı seed, ayrı prompt
> (Faz 9 dosyasında, 8 varyasyon bütçesiyle).

```
SCENE:
Master identity reference plate — a tall sealed figure in an unfamiliar
white pressure suit stands utterly motionless for a full-body reference,
facing three-quarter front, long arms hanging straight at its sides.

ENVIRONMENT:
Smooth, polished bare basalt ground — dustless, texture like honed
stone. Pale grey-green sky, horizon empty, one large pale moon faintly
visible. Nothing else in frame.

SUBJECT:
The figure stands exactly 2.10 m tall. Its pressure suit is sealed,
seamless and flawlessly pearl-white — no wear, no dust, no scratches, no
panel lines, no markings of any kind. The proportions follow a human
skeleton, but the ARMS are long: the fingertips reach knee level. Each
glove has THREE FINGERS and a thumb. The helmet is smooth and
featureless, with a single opaque dark grey-green visor — nothing is
visible behind it, no face, no light. The back is flat, with no
protrusions or equipment. The suit reads as a rigid shell: it does not
wrinkle, fold or ripple like fabric. The stance is perfectly still and
symmetrical, weight evenly planted, boots in full contact with the
polished ground.

CAMERA:
Shot on a 50mm lens from a fixed position five meters away, f/5.6, from
slightly below eye level so the full 2.10 m height reads clearly, full
body in frame. Physically accurate perspective and true scale.

LIGHTING:
Soft orange daylight from a small orange star, 4400K, about seventy
percent of Earth brightness. Soft-edged shadows from a thin atmosphere.
The pearl-white shell shows subtle, clean specular response — bright but
never glowing, never emitting light.

NEGATIVE:
Exactly one figure in frame — no duplicates, no extra people. Rigid,
fixed anatomy: identical limb count, silhouette, height and shoulder
width — no morphing, no shape-shifting. The visor is opaque and never
becomes transparent. The suit stays clean: no dust, no wear, no added
texture. No readable text, letters, digits or symbols anywhere. No
bloom, no glow filter, no lens flare. No subtitles, no captions, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

---

## 📸 REFERANS 4 — CANTOR (master dış, hasarlı taban durumu)

> Seed: `________` · Üretim tarihi: `__.__.____` · Durum: ☐ üretildi
> ⚠️ Hasar S14'te oluşur ve film sonuna dek SABİTTİR — master referans bu
> yüzden HASARLI durumdur (S25-S120, ~100 sahne bunu kullanır).
> **S1-S13 (hasar öncesi) için:** aynı prompttan DAMAGE STATE paragrafı
> çıkarılır, gemi uçuştadır, iniş takımı kapalıdır.

```
SCENE:
Master exterior reference plate — a 31-meter two-crew long-range cargo
courier ship sits grounded on a dark basalt plain, seen in three-quarter
front view from its right side, so the full damage state reads clearly.

ENVIRONMENT:
Dark basalt plain, fine settled dust. Behind the ship, a 60-meter drag
groove marks its landing path. Pale grey-green sky, one large pale moon
as a faint daytime disk. Empty horizon.

SUBJECT:
A boxy, rectangular hull in dark grey-brown panelling, visibly repaired
over years: mismatched replacement patch panels in three distinct grey
tones. Protruding external pipe runs
along the flanks. The hull tapers forward into a narrow cockpit; two
large cargo bays sit aft. At the rear, one single fusion drive nozzle
and four small maneuvering thrusters. Three-legged landing gear with a
9-meter footprint. Thin faded orange accent stripes. Dust, heat staining
and fine scratches everywhere — a used, commercial, working vehicle.
DAMAGE STATE, permanent: the upper surface of the RIGHT rear cargo bay
carries a 1.2-meter perfectly circular hole with clean, glassy, faintly
pearlescent edges — no burn marks, no debris, no blast deformation.
The RIGHT main landing leg is collapsed, and the whole hull
rests tilted at exactly 4 degrees to the right.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position about fifty-five
meters away, slightly elevated three-quarter angle. Correct engineering
proportions, realistic scale relationships, true 31-meter length.

LIGHTING:
Soft orange daylight, 4400K. Soft-edged shadows.
Every panel seam, patch tone and scratch keeps its
texture; the glassy hole edge shows a clean, subtle pearlescent sheen —
never a glow.

NEGATIVE:
The ship's silhouette and proportions stay fixed — no extra engines, no
added antennas, no redesign. The hole stays exactly 1.2 meters, exactly
circular; the tilt stays exactly 4 degrees. No readable text, letters,
digits or markings on the hull. No people in frame. No bloom, no glow
filter, no lens flare. No subtitles, no captions, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

---

## 🎭 GOOGLE FLOW KARAKTER KARTLARI

> Flow'un "Karakter oluştur" ekranı üç alan ister: **ad**, **Karakter
> Bilgileri** (davranış — Flow ajanı sahne üretirken kullanır) ve
> **gövde imajı** (dikey, Nano Banana 2). Aşağıdaki kartlar bu üç alanı
> doldurur.
>
> **Kurallar:**
> - Ad alanına GERÇEK AD YAZILMAZ (Ders 34/45 — etiket olarak ekrana
>   sızabilir). Rol etiketi kullan: `KAPTAN` / `MUHENDIS` / `BEKCI`.
> - "Ses seçin" alanı ÖNEMSİZ: sahneler sessiz üretilir, tüm ses
>   ElevenLabs + post'ta yapılır (README ses kuralı, MUZIK_VE_SES.md).
> - Gövde imajı DİKEY üretilir (Flow standardı); film sahneleri yine
>   16:9 üretilir — dikey imaj sadece kimlik çapasıdır.
> - Karakter Bilgileri alanı İngilizce yazılır: Flow bu metni sahne
>   promptlarına karıştırır, dil tutarlılığı kaymayı azaltır.

### 🎭 FLOW KARTI 1 — KAPTAN

**Ad alanı:** `KAPTAN`

**Karakter Bilgileri (davranış alanı):**

```
A 41-year-old woman cargo pilot. Procedural, calm and economical under
pressure — she never panics, never shouts; when she is afraid she
LOWERS her voice to a near-whisper. Her movements are measured and
slow. When making a decision she places her left hand flat on her
chest indicator — a habitual tic. She speaks briefly and precisely.
VISUAL CONTINUITY (never changes in any scene): a naturally beautiful,
symmetrical face with high cheekbones, light olive skin, sharp
jawline, dark grey-green eyes, a fine faded white scar splitting her
LEFT eyebrow in two, dark brown hair in a tight low bun with subtle
silver strands at the temples, 1.68 m tall, slim and graceful. She always
wears a dark grey-blue pressure suit with ORANGE worn reinforcement
panels on shoulders, elbows and knees, an integrated helmet with a
fully transparent seamless visor that never disappears, and a right
glove with a detachable wrist ring. Chest indicators are abstract
lights only — never text, letters or digits.
```

**Gövde imaj promptu (dikey, Nano Banana 2):**

```
Vertical full-body photorealistic reference of a strikingly beautiful
41-year-old woman pilot standing at rest, facing three-quarter front,
arms held slightly away from her body, expression calm and confident.
A symmetrical face with high cheekbones. Light olive skin with visible
pore texture and natural subsurface scattering. Sharp jawline, thin
lips, dark grey-green eyes. A fine, faded white scar splits her LEFT
eyebrow in two. No makeup, natural beauty. Dark brown hair in a tight
low bun, subtle silver strands at the temples. She is 1.68 m tall,
slim and graceful, with an upright posture. She wears a dark grey-blue pressure suit with ORANGE
worn reinforcement panels on the shoulders, elbows and knees. On the
chest sit three abstract indicators — a slow blue pulse, an amber bar,
a green dot — purely abstract light, no text. Her left forearm carries
an abstract panel of slowly sliding segments. Integrated helmet with a
fully transparent, seamless visor; her face reads clearly through the
glass. The right glove shows a visible detachable ring at the wrist.
Hands empty. Background: bare dark basalt ground fading to a pale
grey-green sky, nothing else in frame. Soft orange daylight, 4400K,
soft-edged shadows; every surface keeps its texture. Full body from
helmet to boots in frame. No readable text, letters or digits
anywhere. No bloom, no glow filter, no waxy skin, no airbrushing, no
face morphing. Photorealistic, 35mm film grain.
```

### 🎭 FLOW KARTI 2 — MÜHENDİS

**Ad alanı:** `MUHENDIS`

**Karakter Bilgileri (davranış alanı):**

```
A 33-year-old man flight engineer. He thinks with his hands — he
touches a problem before he understands it. When he is afraid he
SPEEDS UP and talks more, the exact opposite of his captain. His creed
is "everything can be repaired." His movements are quick and slightly
careless. VISUAL CONTINUITY (never changes in any scene): a handsome face with
strong symmetrical features and a defined jawline, light brown skin,
short neat three-day black stubble, straight nose, full lips, dark
brown eyes, a subtle 2 cm shiny burn scar on his RIGHT cheekbone, very
short dense black hair, 1.81 m tall, athletic, muscular and
broad-shouldered. He always wears a dark grey-blue
pressure suit with TEAL GREEN worn reinforcement panels on shoulders,
elbows and knees, a visibly larger back unit (tool module), a closed
cutting-tool sheath on his left hip, and an integrated helmet with a
fully transparent seamless visor that never disappears. Chest
indicators are abstract lights only — never text, letters or digits.
```

**Gövde imaj promptu (dikey, Nano Banana 2):**

```
Vertical full-body photorealistic reference of a handsome, athletic
33-year-old man flight engineer standing at rest, facing three-quarter
front, arms held slightly away from his body, expression calm and
confident. Strong, symmetrical features with a defined jawline. Light
brown skin with visible pore texture. Short, neat, three-day black
stubble. Straight nose, full lips, dark brown eyes. On his RIGHT
cheekbone, a 2 cm old burn scar — a subtle, shiny mark that suits his
rugged look. Black hair, very short and dense. He is 1.81 m tall,
muscular and broad-shouldered with an athletic build. He wears a dark
grey-blue pressure suit with TEAL GREEN worn reinforcement panels on
the shoulders, elbows and knees. His back unit is visibly larger than
standard — a bulky tool module. On his left hip sits a closed
cutting-tool sheath, tool stowed and not visible. On the chest sit
three abstract indicators — a slow blue pulse, an amber bar, a green
dot — purely abstract light, no text. Integrated helmet with a fully
transparent, seamless visor; his face reads clearly through the glass.
Hands empty. Background: bare dark basalt ground fading to a pale
grey-green sky, nothing else in frame. Soft orange daylight, 4400K,
soft-edged shadows; every surface keeps its texture. Full body from
helmet to boots in frame. No readable text, letters or digits
anywhere. No bloom, no glow filter, no waxy skin, no airbrushing, no
face morphing. Photorealistic, 35mm film grain.
```

### 🎭 FLOW KARTI 3 — BEKÇİ

**Ad alanı:** `BEKCI`
⚠️ Karakter Bilgileri ve imaj promptunda "alien" kelimesi KULLANILMAZ.

**Karakter Bilgileri (davranış alanı):**

```
A tall sealed figure in an unfamiliar white pressure suit. It moves
VERY SLOWLY and continuously — it never stops and starts, it finishes
one motion by flowing into the next. It is patient, deliberate and
never aggressive; it reads as weary, not threatening. It knows only
eight words of human language, heard from an old automated recording,
and speaks them in a processed, slightly distorted human voice.
VISUAL CONTINUITY (never changes in any scene): exactly 2.10 m tall.
Sealed, seamless, flawlessly pearl-white pressure suit — no wear, no
dust, no panel lines, no markings. Human skeletal proportions but LONG
ARMS: fingertips reach knee level. Each glove has THREE FINGERS and a
thumb. Smooth featureless helmet with a single opaque dark grey-green
visor — nothing is ever visible behind it. Flat back, no protrusions.
The suit is a rigid shell and never wrinkles or ripples like fabric.
Its anatomy is fixed: identical limb count, silhouette, height and
shoulder width in every frame — no morphing, no shape-shifting.
```

**Gövde imaj promptu (dikey, Nano Banana 2):**

```
Vertical full-body photorealistic reference of a tall sealed figure in
an unfamiliar white pressure suit, standing utterly motionless, facing
three-quarter front, long arms hanging straight at its sides. The
figure stands exactly 2.10 m tall. Its pressure suit is sealed,
seamless and flawlessly pearl-white — no wear, no dust, no scratches,
no panel lines, no markings of any kind. The proportions follow a
human skeleton, but the ARMS are long: the fingertips reach knee
level. Each glove has THREE FINGERS and a thumb. The helmet is smooth
and featureless, with a single opaque dark grey-green visor — nothing
is visible behind it, no face, no light. The back is flat, with no
protrusions or equipment. The suit reads as a rigid shell: it does not
wrinkle, fold or ripple like fabric. The stance is perfectly still and
symmetrical, weight evenly planted, boots in full contact with the
ground. Background: smooth, polished bare basalt ground — dustless,
like honed stone — fading to a pale grey-green sky, nothing else in
frame. Soft orange daylight, 4400K, soft-edged shadows; the pearl-
white shell shows subtle, clean specular response — bright but never
glowing. Full body from helmet to boots in frame. Rigid fixed anatomy,
no morphing, no shape-shifting; the visor stays opaque. No readable
text anywhere. No bloom, no glow filter. Photorealistic, 35mm film
grain.
```

### 🚀 CANTOR — Flow'da karakter DEĞİL

```
Gemi, Flow'un karakter sistemine EKLENMEZ (karakter sistemi figürler
içindir; gemiyi karakter yapmak siluet kaymasına davetiye çıkarır).
CANTOR için: REFERANS 4 promptuyla normal imaj üret, beğenilen kareyi
sahne promptlarında "malzeme/ingredient" veya start frame olarak kullan.
Hasarsız hali (S1-S13) için REFERANS 4 notundaki gibi DAMAGE STATE
paragrafı çıkarılır.
```

---

## 📋 PAKETİN KALAN KALEMLERİ (00_PLAN.md kapsamı — henüz yazılmadı)

```
☑ Kaptan master (3/4 ön)          ← bu dosya, REFERANS 1
☐ Kaptan profil + sırt açıları
☑ Mühendis master (3/4 ön)        ← bu dosya, REFERANS 2
☐ Mühendis profil + sırt açıları
☑ Bekçi master (mühürlü, 3/4 ön)  ← bu dosya, REFERANS 3
☐ Bekçi profil + sırt açıları
☐ Bekçi YÜZÜ (S103 — tek imaj, AYRI seed, Faz 9 dosyasıyla birlikte)
☑ CANTOR dış master (hasarlı)     ← bu dosya, REFERANS 4
☐ CANTOR dış (hasarsız, uçuş — S1-S13)
☐ CANTOR iç (kokpit + borç çubuğu)
☐ Kule dış / Kule iç master
☐ Kopya tarlası master (S42 afiş karesi ayrı çalışılır)
☐ Işık varyasyonları: gece / şafak / kule içi
```
