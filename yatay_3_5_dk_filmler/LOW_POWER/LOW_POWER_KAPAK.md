# 🖼️ LOW POWER — KAPAK FOTOĞRAFI PROMPTLARI

## 1280×720 px | YouTube Thumbnail | A + Plan B Sürümleri
### Kaynak kılavuz: `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`

---

## 🎯 TASARIM KARARI — NEDEN BU KOMPOZİSYON

Filmin en özgün görseli S14'tür: **mavi Mars gün batımı** — bilimsel olarak
gerçek, kütüphanedeki 29 filmin hiçbirinde yok, ve "bu gerçek mi?" merakını
anında tetikliyor. Ama S14 geniş bir çekim: figür karenin altıda birini
kaplıyor. Kapak kılavuzu ise yüzün **%60'ını** istiyor (§2 — yüz içeren
kapaklar %25-40 daha yüksek CTR alıyor).

**Çözüm: ikisini birleştirdim.** Kapak S14'ün ANINI kullanıyor ama S14'ün
KADRAJINI kullanmıyor — yüz yakın çekimde, mavi gün batımı arkasında ve
vizörde. Filmden bir kare değil, filmin bir anının kapak için yeniden
çerçevelenmiş hali. Vaat edilen görüntü filmde gerçekten var.

```
RENK DİSİPLİNİ (kılavuz §3 — maksimum 2-3 renk):
  KAPAK A:  kahve-kızıl + soğuk mavi        → 2 renk
  KAPAK B:  kahve-kızıl + yeşil             → 2 renk
Filmin kendi paleti zaten iki renk. Kapak da öyle.
```

> ⚠️ **Metin görselde ÜRETİLMEYECEK.** Görsel modeller harfleri güvenilir
> üretmiyor ve bozuk bir harf tüm kapağı çöpe atıyor. Ayrıca Ders 34
> (jenerik metni halüsinasyonu) promptta film adı geçmesini riskli kılıyor.
> Her iki sürüm de **metinsiz** üretilir, tipografi post-prodüksiyonda eklenir.

---

# 🅰️ KAPAK A — ANA SÜRÜM (Mavi Gün Batımı)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels, 16:9
landscape format. NO TEXT ANYWHERE IN THE IMAGE. YouTube thumbnail
optimized — maximum impact at 120 pixels wide.

SUBJECT — FILLS THE FRAME:
A 44-year-old woman in a Mars surface suit, in extreme close-up. Her head
and shoulders fill at least 60% of the total frame area, positioned in the
RIGHT HALF of the frame, her body angled slightly left. HER EYES SIT ON THE
UPPER THIRD LINE of the frame. She is NOT looking at the camera — she is
looking slightly up and to the left, at something outside the frame, and
the viewer wants to know what.

Her face, seen through a FULLY TRANSPARENT SEAMLESS HELMET VISOR with no
tint and no obstruction: warm light-brown skin with visible pore texture and
real skin detail, NO airbrushing, NO smoothing. An indoor pallor from months
without sunlight. Broad forehead, defined jawline. Dark brown eyes, WIDE
OPEN, catchlights sharp and visible, deep fatigue lines and shadowing
beneath them. Thick natural eyebrows. Thin lips, dry and cracked, SLIGHTLY
PARTED. Dark brown hair going grey at the temples, cut short and pulled
back.

Her expression: QUIET AWE — the face of an exhausted person seeing something
unexpectedly beautiful. Not screaming, not panicking, not smiling. Eyes wide
and still, mouth just open. The emotion must read instantly at thumbnail
scale.

She wears a dirty WHITE-BEIGE surface EVA suit with a faded ORANGE accent
band visible at the shoulder, and rust-red Martian dust permanently staining
the suit fabric. A thin film of fine red dust sits on the outside of the
visor with two wiped arc marks cleared across it.

BACKGROUND — THE HOOK:
Behind her and to the LEFT, occupying the left third of the frame: the
Martian sky at sunset during a dust storm, showing a real optical phenomenon
that is the reverse of Earth. Most of the visible sky is DARK BUTTERSCOTCH
BROWN, caramel-tan, heavy with suspended dust. But around the low setting
sun, a soft circular region turns a distinct COOL DESATURATED BLUE-GREY,
deepening toward slate blue nearest the sun. The transition from brown to
blue is gradual and smooth, never a hard edge. The SUN sits low as a small
PALE WHITE-BLUE DISC with soft indistinct edges, dimmed by dust, safe to
look at. The horizon is a low dark line of red-brown regolith. The
background is thrown slightly soft by shallow depth of field and
DESATURATED to roughly 70% so it never competes with her face.

The same blue region is REFLECTED as a curved cool band across the surface
of her visor glass, over her forehead and one eye — the reflection matches
the real background exactly in shape and position.

COLOR — TWO COLORS ONLY:
- WARM BROWN-RED: dominant, on her suit, her face, and most of the sky
- COOL DESATURATED BLUE: the region around the sun and the visor reflection
One accent only: the small faded ORANGE band on her shoulder.
NO other colors. NO green, NO teal, NO purple, NO magenta. Two-value
contrast: warm face against the cool blue region. Increase final saturation
by 20% so both survive at thumbnail scale.

LIGHTING:
Two motivated sources. (1) The pale white-blue setting sun, low and to the
left, throwing COOL directional light across the left side of her face and
a hard cool rim along her helmet edge and shoulder. (2) The surrounding
brown sky acting as a wide warm ambient fill, giving a dull red-brown wash
to the right side of her face. Shadows are soft-edged, correct for a dust
storm. Sharp directional light with clear falloff. 0% bloom, 0% glow filter,
0% soft focus, no lens flare, no sun star, no god rays.

COMPOSITION:
- Face occupies 60%+ of the frame, positioned right of center
- Eyes on the upper third line
- 30-40% of the frame is clean, uncluttered sky — open negative space in
  the UPPER LEFT, reserved for the title added later in post
- LOWER-RIGHT CORNER completely empty — no face, no detail, no elements.
  YouTube's duration badge covers this zone.

TECHNICAL:
- No text, no letters, no numbers, no logo, no watermark, no subtitles
- Photorealistic, 35mm anamorphic film grain
- Sharp focus on the eyes — they are the sharpest thing in the image
- Must survive the postage-stamp test: at 120 pixels wide the emotion on
  the face and the blue region must both still read instantly
- No CGI aesthetic, no Unreal Engine look, no video game render

NEGATIVE:
NO EARTH SUNSET — the sky near the sun is BLUE and the rest is BROWN; this
relationship must never invert. No orange or red glow around the sun, no
pink clouds, no golden hour warmth near the sun, no blue sky away from the
sun, no clouds of any kind. No bloom, no glow filter, no lens flare, no sun
star, no god rays. No green anywhere. No visor tint, no reflective coating,
no HUD graphics — the visor is fully transparent and her face is completely
readable through it. No airbrushed or plastic skin. No second person, no
duplicate character, no reflection of another figure in the visor. No
readable text, letters, digits or symbols on the suit or any surface. Not
miniature, not toy-like.
```

---

# 🅱️ KAPAK B — PLAN B SÜRÜMÜ (Tek Yeşil Pencere)

> Kılavuz §7: yayından 48 saat sonra CTR %4'ün altındaysa, önceden
> hazırlanmış farklı palette bir Plan B kapağı devreye alınır.
> Bu sürüm S19'a dayanıyor ve **filmin temasını tek karede** anlatıyor.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels, 16:9
landscape format. NO TEXT ANYWHERE IN THE IMAGE. NO human character.
YouTube thumbnail optimized — maximum impact at 120 pixels wide.

SUBJECT — A SINGLE LIT WINDOW IN TOTAL DARKNESS:
The exterior of a small half-buried Mars station at night during a dust
storm, seen from roughly 20 meters. Pale white-beige cylindrical habitat
modules lie half-buried in red-brown regolith, coated in dust and reduced by
darkness to faint dark ridges — barely readable outlines, deliberately
almost lost.

Positioned in the RIGHT HALF of the frame, slightly above center: ONE SMALL
RECTANGULAR WINDOW, roughly 60 by 40 cm, set in the side of one module. It
is the ONLY source of light in the entire image, and the light coming
through it is SATURATED GREEN. The window is small in the frame but it is
unmistakably the subject — everything else exists to be dark around it.

The green light spills a short, sharply defined distance out of the window:
a defined patch on the dusty regolith directly beneath it, and a defined
wash across the module's flank, mixing red ground and green light into a
strange olive tone where they overlap. Beyond a few meters the light dies
completely. A thin film of red dust sits on the outside of the glass.

ENVIRONMENT:
The entire rest of the frame is DARK RED-BROWN, near black at the edges,
with suspended dust filling the air as a dense haze that softens every
contour. There is NO sun, NO stars, NO moons, NO horizon line — the sky and
the ground merge into one continuous dark field. The darkness is heavy,
grainy and real, never a flat black.

COLOR — TWO COLORS ONLY:
- DARK RED-BROWN: the entire frame, near black at the edges
- SATURATED GREEN: the single window and its short spill
NO other colors. NO blue, NO orange, NO white, NO teal. The image is an
extreme two-value contrast: one small saturated green rectangle against a
very large dark red field. Increase final saturation by 20% so the green
survives at thumbnail scale.

LIGHTING:
One motivated source only: the greenhouse LEDs behind the small window. The
light is sharp and directional where it leaves the glass, with clear falloff
and a defined edge, and it dies out entirely within a few meters. Everything
else is unlit ambient darkness. 0% bloom, 0% glow filter, no halo around the
window, no volumetric light beam or god ray reaching into the dust — the
green light is a defined patch, never a searchlight.

COMPOSITION:
- The lit window sits in the RIGHT HALF, slightly above center
- Roughly 60% of the frame is empty dark space — the negative space IS the
  subject, and the UPPER LEFT is kept completely clean for the title added
  later in post
- LOWER-RIGHT CORNER completely empty and dark — no elements at all.
  YouTube's duration badge covers this zone.

TECHNICAL:
- No text, no letters, no numbers, no logo, no watermark, no subtitles
- Photorealistic, 35mm anamorphic film grain
- Sharp focus on the window and its spill
- Must survive the postage-stamp test: at 120 pixels wide the single green
  rectangle in the dark must still read instantly as the only living thing
- No CGI aesthetic, no Unreal Engine look, no video game render

NEGATIVE:
No human character, no figure, no silhouette, no face, no reflection of a
person in the glass. No stars, no moons, no sun, no horizon line, no blue
sky, no clear sky. No other lit windows — exactly ONE window is lit and
every other window and surface is dark. No exterior lamps, no beacons, no
blinking lights, no vehicle. No bloom, no glow filter, no halo, no
volumetric beam, no god rays. Green appears ONLY as the light from this one
window. No violent wind, no flying debris, no dust streaking horizontally.
No readable text, letters, digits or symbols on the modules. Not miniature,
not toy-like. No flat digital black — the darkness carries grain and depth.
```

---

# ✍️ POST-PRODÜKSİYON TİPOGRAFİSİ (her iki sürüm için ortak)

```
BAŞLIK:        LOW POWER              (2 kelime — kılavuz sınırı 0-3)
FONT:          Bebas Neue / Impact / Oswald Bold — ultra kalın sans-serif
BOYUT:         60-80 punto, geniş harf aralığı (wide tracking)
KONUM:         ÜST SOL çeyrek — yüzün/pencerenin üstüne değil, boş alana
RENK:          Saf beyaz
OKUNABİLİRLİK: 3-4 px KALIN siyah dış çizgi (outline) + belirgin drop shadow
               ⚠️ İnce gölge yetmez. Renk körlüğü için sadece renge güvenme;
               parlaklık farkı ve dış hat zorunlu (kılavuz §3).
KONTRAST:      Metin ile arkasındaki alan arasında minimum 4.5:1 (WCAG)
ALT BAŞLIK:    YOK. "A MARS SURVIVAL FILM" gibi açıklayıcı bir alt başlık
               merak boşluğunu KAPATIR — kılavuz §4 buna karşı.
YASAK ALAN:    Sağ alt köşe tamamen boş (YouTube süre rozeti bölgesi)
FİNAL EXPORT:  1280×720 px, 72 DPI, JPEG %85 (Squoosh ile optimize)
```

---

# 🧪 A/B TEST PLANI (kılavuz §7)

```
LANSMAN:     Kapak A ile yayına gir (yüz + mavi gün batımı)
İZLE:        İlk 48 saat CTR
KARAR:
  CTR ≥ %5   → Kapak A kalır. Başarılı.
  CTR %3-4   → Kapak A kalır, başlık metni denenir (konum/boyut).
  CTR < %3   → Kapak B'ye geç (tek yeşil pencere).

POSTA PULU TESTİ (yayın öncesi zorunlu):
Görseli 120 piksel genişliğe küçült.
  Kapak A: yüzdeki duygu ve mavi bölge hâlâ okunuyor mu?
  Kapak B: yeşil dikdörtgen hâlâ tek canlı şey gibi duruyor mu?
Okunmuyorsa yeniden üret — büyük ekranda güzel olması hiçbir şey ifade etmez.
```

---

# ⚠️ ÜRETİM NOTLARI

```
1. KAPAK A'NIN EN BÜYÜK RİSKİ: MODEL DÜNYA GÜN BATIMI YAPAR
   Eğitim verisinde gün batımı = turuncu/pembe. Mars'ta ilişki TERSTİR:
   güneşin çevresi mavi, gökyüzünün gerisi kahve. Prompta "NO EARTH SUNSET"
   negatifi ve ilişkinin asla ters çevrilmemesi ayrıca yazıldı.
   → İlk kontrol edilecek şey budur. Turuncu bir gün batımı çıktıysa at.

2. KAPAK B'NİN EN BÜYÜK RİSKİ: MODEL KAREYİ AYDINLATIR
   Model karanlık kareyi "hatalı" sayıp ortam ışığı ekleme eğiliminde.
   Kadrenin %60'ı gerçekten karanlık kalmalı. Ay ışığı, yıldız, ikinci
   pencere, dış lamba eklendiyse at.

3. HER İKİSİNDE: METİN ÜRETİLMEMELİ
   Promptların ilk satırında "NO TEXT ANYWHERE" var. Yine de harf çıkarsa
   yeniden üret — post-prodüksiyonda temizlemeye çalışma.

4. DÜRÜSTLÜK NOTU — ABARTILI DUYGU KONUSU
   Kılavuz §2 CTR için "abartılı duygu" (şok, dehşet) öneriyor. Bunu
   bilinçli olarak UYGULAMADIM. Selin sakin ve ölçülü bir karakter; kapakta
   çığlık atan bir yüz koyarsak izleyici filmde onu bulamaz ve ilk 30
   saniyede bırakır. Yüksek CTR + düşük retention, algoritma için düşük
   CTR'dan daha kötüdür.
   Onun yerine "sessiz huşu" seçildi — 120 pikselde okunuyor, ve filmde
   gerçekten var olan bir an (S14).
```
