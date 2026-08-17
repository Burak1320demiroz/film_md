# 🎯 THE SLOW STONE — REFERANS PAKETİ VE FİLM KAPAĞI

## Karakter · Araç · Üs · Mineral — **her bölüm için TEK referans sayfası**
### 4 birleşik referans sayfası + 1 kapak = 5 görsel

> ⚠️ **BU DOSYA SAHNE PROMPTLARINDAN ÖNCE ÜRETİLİR.**
> 48 sahnelik bir filmde karakter, araç ve mekan çapası önceden
> kilitlenmezse 3. kısımda yüz kayar ve geri dönüşü olmaz.
> Üretim sırası: bu dosya → seed'leri kilitle → sonra kısım dosyaları.
>
> Tüm promptlar Ders 34 uyumlu: **karakter adı hiçbir promptta geçmez.**

---

# 📋 ÜRETİM SIRASI VE SEED TAKİP TABLOSU

| # | Referans sayfası | İçindekiler | Öncelik | Seed | Durum |
|---|---|---|:---:|---|:---:|
| **RK** | KARAKTER SAYFASI | 5 panel: ön yüz · profil · vizör ardı · tam boy temiz · tam boy kalın kabuk | 🔴 ZORUNLU | | ☐ |
| **RM** | MİNERAL SAYFASI | 3 panel: kabuk makro · kazınmış kesit · oluşum tarlası | 🔴 ZORUNLU | | ☐ |
| **RT** | TALLOW SAYFASI | 4 panel: dış SAĞLAM · dış hasarlı+gömülü · nozul · kokpit | 🔴 ZORUNLU | | ☐ |
| **RI** | İSTASYON GRİ SAYFASI | 4 panel: dış görünüm · iç karanlık · iç aydınlık · dört kanca | 🔴 ZORUNLU | | ☐ |
| **KP** | FİLM KAPAĞI | tek sürüm, metinsiz | 🔴 ZORUNLU | | ☐ |

```
ÜRETİM SIRASI (değişmedi, sadece kısaldı):
  RK  →  yüz ve suit kilitlenir       (bu onaylanmadan sahneye BAŞLAMA)
  RM  →  mineral dili kilitlenir
  RT  →  araç kilitlenir
  RI  →  üs kilitlenir
  KP  →  kapak, karakter kilitlendikten SONRA
```

---

# 🔁 ESKİ KOD → YENİ SAYFA DÖNÜŞÜMÜ

> Kısım dosyalarındaki (`01`–`04`) **“YÜKLENECEK REFERANS: R3 · R16”**
> satırları geçerliliğini koruyor. Karşılıkları:

| Eski | Neydi | Yeni yer |
|---|---|---|
| R1 · R2 · R3 · R4 · R5 | karakter (yüz, profil, vizör, temiz, kabuklu) | **RK** panel 1-5 |
| R6 · R7 · R8 · R9 | TALLOW (temiz, gömülü, nozul, kokpit) | **RT** panel 1-4 |
| R10 · R11 · R12 · R13 | İstasyon (dış, karanlık, aydınlık, kanca) | **RI** panel 1-4 |
| R14 · R15 · R16 | mineral (makro, kesit, tarla) | **RM** panel 1-3 |
| K-A · K-B | kapak | **KP** (+ Plan B varyant notu) |

```
PRATİKTE: sahne üretiminde ilgili SAYFANIN TAMAMINI yüklüyorsun.
Model o sayfadaki tüm panelleri görüyor ve tutarlılık artıyor —
tek panel yüklemekten daha güçlü bir çapa.

Panel bazında yüklemek istersen: sayfayı üret, panelleri kırpıp
ayrı dosya olarak kaydet. Kırpılmış paneller eski R kodlarıyla
birebir eşleşir.
```

---

# 👤 BÖLÜM 1 — KARAKTER SAYFASI `RK` 🔴

> **Filmin en kritik varlığı.** 48 sahnenin yüz çapası bu tek görselde.
> ⚠️ Bunu **en yüksek çözünürlükte** üret. Yüz panelleri birbirinden
> saparsa sayfayı at ve yeniden üret — sahne üretimine geçme.

```
Photorealistic cinematic CHARACTER REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FIVE CLEAN PANELS separated by thin neutral mid-grey gutters: a TOP ROW of three equal portrait panels, and a BOTTOM ROW of two equal full-figure panels. Every panel shows THE SAME ONE WOMAN — no other individuals appear anywhere on the sheet. Neutral studio-style lighting throughout for reference use.

THE PERSON — IDENTICAL IN ALL FIVE PANELS: a 36-YEAR-OLD WOMAN, 1.72 metres, broad-shouldered and solidly built. Deep brown skin with clearly visible pore texture and natural subsurface scattering — no airbrushing, no smoothing, no beauty retouching. Broad high cheekbones. A rounded jaw and softly squared chin. Dark brown eyes, calm and steady, with pronounced laugh lines at the outer corners. Thick natural eyebrows with a slight arch, the left sitting marginally higher than the right. A small old healed piercing mark on her left nostril with NO jewellery in it. A single vertical crack in her lower lip from dry air. Faint dark shadowing under both eyes. No makeup. HAIR: black, very short cropped, tightly coiled natural texture close to the scalp, with a few sparse grey strands at both temples.

PANEL 1 — TOP LEFT, FACE FRONT, NO HELMET: head and shoulders, facing the camera straight on, neutral expression, mouth closed, eyes level with the lens. Only the collar ring of a sand-grey surface suit is visible at the base of the panel, with a worn mustard-yellow band along its edge. 85mm look, sharp focus across the whole face.

PANEL 2 — TOP CENTRE, FACE LEFT PROFILE, NO HELMET: exact 90-degree left profile, head and shoulders, looking straight ahead out of the panel, neutral expression. The broad cheekbone catches the light; the healed nostril mark is clearly visible at this angle; the hairline and head shape read clearly. Same sand-grey collar ring with mustard-yellow edge at the base.

PANEL 3 — TOP RIGHT, FACE THROUGH THE VISOR: close-up seen through a FULLY TRANSPARENT SEAMLESS HELMET VISOR — the glass is perfectly clear with no tint, no coating and no reflection obscuring her, so her entire face is completely readable, skin texture visible through the glass. Neutral alert expression, mouth closed. The helmet is a sand-grey integrated shell with a worn mustard-yellow band around the visor rim, the visor a single seamless curved pane. A faint film of breath condensation sits at the very bottom edge of the glass. Slight three-quarter angle.

PANEL 4 — BOTTOM LEFT, FULL FIGURE, PART 1 CLEAN: standing upright, full body with headroom, arms relaxed at her sides, three-quarters to camera, face readable through the clear visor. SUIT — THIS EXACT CONFIGURATION REPEATS IN EVERY SCENE OF THE FILM: sand-grey base with WORN MUSTARD-YELLOW reinforcement panels at the shoulders, knees and elbows, their edges scuffed pale from use. Three abstract chest indicators in a triangle — a slow blue pulse, an amber bar, a green dot — with NO letters or numbers. A measurement panel on the left forearm showing abstract drifting segments. On the right hip, a compact tool holster holding a SCRAPER — a flat blade about 20cm long with a worn grip. Integrated sand-grey helmet with a mustard-yellow band at the visor rim. Flat-soled boots. MINERAL STATE: CLEAN — only fine rust-brown dust on the boots and lower legs, and NO white mineral crust anywhere.

PANEL 5 — BOTTOM RIGHT, FULL FIGURE, PART 4 HEAVY CRUST: the same woman in the same pose, the same suit in the identical configuration, face readable through the clear visor, expression tired and set. MINERAL STATE: a thick BONE-WHITE crystalline crust, 1-2cm thick, has built up on the upper surfaces only — across both shoulders, over the back unit, on the tops of the forearms, on the backs of both gloves, and as a rough uneven layer across the TOP OF THE HELMET. The crust is matte, faintly pearlescent, with visible crystal grain and fine cracks running through it where movement has broken it. Undersides and the visor glass itself stay clear. Rust-brown dust beneath the white on the legs. This panel and panel 4 must be directly comparable — SAME face, SAME suit, ONLY the mineral level differs.

Camera and light across the sheet: soft even neutral key at 5000K with gentle fill, mid-grey seamless background in every panel, shadows soft but present. Every skin texture, pore, fabric weave, scuff, dust grain and crystal facet stays fully visible.

Negative: the five panels show ONE person only — no second individual, no other model, no crowd, no reflection of another figure. The face, hair, build and suit are IDENTICAL across every panel — no drifting, no morphing, no age or feature change between panels. NO white mineral crust anywhere in panels 1-4. The crust in panel 5 NEVER glows, emits light, shimmers or sparkles — it is matte stone catching light with clear falloff — and never touches the visor glass. No visor tint, no mirrored coating, no HUD graphics, no display overlay on the glass. NO text, letters, numbers, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No airbrushing, no waxy or plastic skin, no beauty filter, no makeup, no jewellery, no glasses. No weapon. No stylisation, no illustration, no CGI look, no video game render. Photorealistic with 35mm film grain.
```

---

# 🪨 BÖLÜM 2 — MİNERAL SAYFASI `RM` 🔴

> Filmin Novum'u. Bu tek sayfa 48 sahnenin görsel kimliğini belirler.
> **RK'dan hemen sonra üretilir** — mineral dili kilitlenmeden mekan yok.

```
Photorealistic cinematic MATERIAL REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into THREE CLEAN PANELS separated by thin neutral mid-grey gutters: a TOP ROW of two equal square panels, and beneath them ONE FULL-WIDTH WIDE PANEL. NO people, figures or bodies anywhere on the sheet.

THE MATERIAL — CONSISTENT IN ALL THREE PANELS: a BONE-WHITE mineral crust with a faint pearlescent sheen, built from densely packed interlocking crystal grains roughly 1-3mm across whose facets catch light at slightly different angles, so the surface always reads as textured MATTE STONE rather than a smooth shell. Fine hairline fracture lines run across it in irregular networks. It grows in overlapping rounded lobes, one layer over another, like slow accretion rings. A faint rust-brown tint shows in the deepest crevices where dust has settled between crystals.

PANEL 1 — TOP LEFT, CRUST TEXTURE MACRO: extreme close detail of the crust surface, filling the panel. Every crystal facet, grain boundary and fracture line is razor-sharp. In one area the crust has grown in visible overlapping lobes; one corner shows a fresh chipped edge, brighter and sharper than the weathered surface around it. 100mm macro look at 0.25 metres, raking pale orange-tinted light at 4200K from the left at a low angle throwing every facet into relief. The material must read as matte stone, not gemstone.

PANEL 2 — TOP RIGHT, SCRAPED CROSS-SECTION — THE PROOF OF THE NOVUM: the same crust, but scraped open. The upper and outer parts of the panel stay thick bone-white crust with visible grain and fracture lines. Through the middle runs a rough scraped channel about 8cm wide where a blade has chipped the crust away in flakes, its broken edges bright and sharp. At the base of the channel, exposed and CLEARLY VISIBLE: the original surface underneath — a dark rust-brown basalt rock face in PERFECT condition, every micro-ridge, pit and grain sharp and undamaged, as if sealed the day it was covered. The contrast between the weathered white crust above and the pristine dark surface below is the point of the panel. Loose white flakes and mineral dust lie scattered around the channel. 100mm macro look at 0.3 metres, raking 4200K light from the upper left reaching down into the channel.

PANEL 3 — BOTTOM, FULL WIDTH, THE FORMATION FIELD: a wide rust-brown basalt plain under a pale orange-beige sky, scattered with HUNDREDS OF BONE-WHITE MINERAL FORMATIONS of varying size. The formations are not random — each has grown over something and taken its shape, so the field reads as a landscape of covered objects: low rounded lumps the size of a crate, elongated ridges, short irregular pillars between one and two metres tall. A few in the middle distance have a disquietingly familiar UPRIGHT silhouette — the general proportions of a standing figure — but they are softened and rounded by growth, with NO readable detail, NO face, NO limbs and NO equipment: only shape. Rust-brown dust gathers at their bases. The field recedes to a low horizon under a small dim orange-yellow star roughly 60 percent the apparent size of the Sun seen from Earth, low in the sky. Two small moons are faintly visible — one a small disc, one a bright point. 32mm anamorphic look, f/11, from 40 metres at 1.0 metre height, deep focus from the nearest formation to the horizon, pale orange-tinted 4200K daylight at roughly half Earth brightness from low left, long soft-edged shadows stretching across the plain.

Negative: the mineral NEVER glows, emits light, shimmers or sparkles like gemstone in ANY panel — it is matte crystalline rock reflecting light with clear falloff. No internal light, no translucency in panels 1 and 2. The exposed basalt in panel 2 is NOT wet, NOT shiny, NOT glowing — simply undamaged and sharply detailed. In panel 3, NO readable human or body detail resolves in any formation — the upright shapes stay ambiguous, rounded and unresolved, with NO faces, NO limbs, NO visible equipment. NO people, figures, bodies, hands or tools anywhere on the sheet. NO text, letters, numbers, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare, no bokeh sparkle, no fog banks. Static stable geometry. Photorealistic with 35mm anamorphic film grain.
```

---

# 🚀 BÖLÜM 3 — TALLOW SAYFASI `RT` 🔴

```
Photorealistic cinematic VEHICLE REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FOUR EQUAL PANELS in a 2×2 grid, separated by thin neutral mid-grey gutters. NO people, figures or bodies in any panel.

THE CRAFT — IDENTICAL DESIGN IN ALL PANELS: a 24-METRE MODERN single-crew long-range survey lander. A lifting-body airframe with a rounded nose, a broad underside heat shield and SHORT SWEPT DELTA WINGS on both flanks. Clean matte WHITE-GREY composite hull panels with FLUSH seams and worn MUSTARD-YELLOW accent stripes along the spine and around the airlock — the same colour language as the pilot's suit. Modern but NOT sterile: micro-scratching along panel edges, heat staining on the underside, dust settled in the seams. RETRACTABLE TRICYCLE LANDING GEAR — a nose leg and two main legs with wide flat pads, 7-metre main-gear spread. A circular airlock hatch on the upper hull. A single fusion thrust nozzle at the stern. DAMAGE STATE — APPLIES TO PANELS 2 AND 3 ONLY (panel 1 shows the craft INTACT, before the strike), then FIXED FOR THE ENTIRE FILM: the RIGHT MAIN LANDING LEG has collapsed, so the whole craft sits at EXACTLY 6 DEGREES tilt to the right; the OUTER THIRD OF THE RIGHT WING is torn away in a ragged composite fracture with laminate layers exposed and a scorched puncture at the wing root; a 40-METRE SKID GOUGE runs through the basalt behind the craft where the belly dragged in, and the lower right hull is scoured back to bare composite; the stern thrust nozzle is INTACT and undamaged.

PANEL 1 — TOP LEFT, EXTERIOR INTACT AND CLEAN (the baseline — this is the craft BEFORE the strike): standing level on a rust-brown basalt plain under a pale orange-beige sky, three-quarter front view from ground level, nose leg and both main legs extended and clear of the ground, BOTH DELTA WINGS WHOLE AND UNDAMAGED, the hull unmarked. NO tilt — it sits level. MINERAL STATE: CLEAN — only rust-brown dust on the landing pads, NO white crust anywhere. 32mm anamorphic look, f/8, from 25 metres at 1.2 metre height, deep focus, the full craft in frame with the plain behind it. Physically accurate engineering proportions — a 24-metre vehicle, never miniature, never toy-like.

PANEL 2 — TOP RIGHT, EXTERIOR DAMAGED AND HEAVILY ENCASED: the SAME craft, SAME plain, SAME three-quarter front view — now carrying the full damage state above AND two thirds swallowed by mineral growth. A thick BONE-WHITE crystalline crust has grown up over the lower two thirds of the hull in uneven rounded lobes that follow its shape. ALL THREE LANDING LEGS AND THE LOWER FUSELAGE ARE COMPLETELY GONE beneath a continuous white mass that merges the craft with the ground — it looks like it is growing out of the plain rather than standing on it. The SURVIVING LEFT WING has become a solid white crusted slab, its aerofoil shape swollen and softened; the torn stump of the right wing is crusted over at its fracture but the ragged laminate edge still reads. The upper third of the hull and the airlock hatch are still exposed white-grey composite, with white crust creeping around the hatch rim. The THRUST NOZZLE MOUTH at the stern is PARTLY OCCLUDED by crust growing across its opening — clearly readable as a problem. Same camera and framing as panel 1 so the two panels compare directly.

PANEL 3 — BOTTOM LEFT, NOZZLE DETAIL: close detail of the stern thrust nozzle seen from below and behind. The nozzle mouth is roughly 1.5 metres across, dark heat-stained metal with visible radial fluting inside its bell. Around and across its opening, BONE-WHITE crystalline crust has grown inward from the rim, narrowing the aperture by roughly a third — uneven rounded lobes of matte mineral with visible crystal grain, and some fresh fracture lines where a tool has already chipped at one edge. Below, the matte white-grey composite hull with its worn mustard-yellow accent stripe; beyond, rust-brown basalt ground with white crust creeping across it. 100mm macro look, f/5.6, from 1.5 metres, low angle looking up into the bell, sharp focus on the exact line where mineral meets machined metal.

PANEL 4 — BOTTOM RIGHT, COCKPIT INTERIOR: the single-crew cockpit seen from the rear over the EMPTY pilot seat. A tight functional space — the pilot could touch every surface from the seat. One centre-mounted pilot seat in worn dark grey padding with visible wear on the armrests. A curved console arc at waist height carrying physical toggle switches, two rotary dials and four flat display panels showing ABSTRACT DRIFTING LIGHT SEGMENTS in amber and pale blue. A wide curved forward windscreen 2 metres across, scratched at its edges from years of dust, showing rust-brown ground and pale orange-beige sky beyond. Clean white composite wall panels with worn mustard-yellow trim at the flush seams. Exposed cable runs along the ceiling. A narrow storage rack on the right wall holding survey equipment in fitted slots, one slot empty. The whole interior sits at a visible 6-DEGREE TILT to the right — seat, console line and the horizon through the windscreen all lean consistently. 32mm look, f/4, from 2 metres behind the seat at chest height, pale orange 4200K daylight through the windscreen as the main source plus faint amber and blue spill from the console.

Light across the exterior panels: pale orange-tinted daylight at 4200K from a small dim star, roughly half the brightness of Earth daylight, soft-edged shadows — correct for a thin atmosphere — with every hull plate seam, scrape, dust grain and crystal facet staying visible.

Negative: NO people, figures, bodies or hands in any panel; the pilot seat in panel 4 is EMPTY. The crust NEVER glows, emits light or shimmers — matte mineral only, light reflects with clear falloff. NO white crust at all in panel 1, and NO damage in panel 1 — both wings whole, no tilt, hull unmarked. Panels 2 and 3 carry the damage exactly as described and identically to each other. NO fire, smoke, engine glow, exhaust or heat light in any panel — the craft is completely inert throughout. NO readable text, letters, numbers, symbols, logos or markings anywhere — on the hull, in the cockpit, on any display or panel; abstract light segments only. NO holographic projections. The 6-degree tilt is exact and consistent in every panel that shows it. NO text, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare. Not miniature, not toy-like, not a CGI or video game render. Photorealistic with 35mm anamorphic film grain.
```

---

# 🏠 BÖLÜM 4 — İSTASYON GRİ SAYFASI `RI` 🔴

```
Photorealistic cinematic ARCHITECTURE AND INTERIOR REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FOUR EQUAL PANELS in a 2×2 grid, separated by thin neutral mid-grey gutters. NO people, figures, bodies or silhouettes in any panel.

THE STRUCTURE: a MODERN PREFABRICATED MODULAR RESEARCH OUTPOST from an earlier expedition, sealed for fourteen years. FOUR HEXAGONAL MODULES docked around a central connecting node in a four-lobed plan, 18 metres across the whole footprint and 3.5 metres tall. Each module is a clean white composite shell with flush panel seams and mustard-yellow seam trim — the same colour language as the survey lander and the surface suit. A collapsed folding solar array lies across the roof of one module; a slim communications mast rises from the node. The interior carries the same clean white composite panelling with mustard-yellow trim.

PANEL 1 — TOP LEFT, EXTERIOR: the outpost standing on a rust-brown basalt plain under a pale orange-beige sky, COMPLETELY COVERED by a thick bone-white crystalline crust grown over it across fourteen years. From a distance it reads as a natural mineral formation, and only its GEOMETRY betrays it: beneath the rounded crust lobes, the four-lobed plan, the STRAIGHT EDGES and the SQUARE CORNERS of the modules are unmistakably manufactured — nature does not make right angles. The collapsed solar array shows as a long flat crusted slab across one module roof, the mast as a thin crusted spike. One module face carries a faint RECTANGULAR SEAM where a hatch frame lies buried beneath. The crust is matte, faintly pearlescent, in uneven rounded lobes with visible crystal grain and fine fracture lines, merging seamlessly into the ground at the base. Scattered across the plain behind it: dozens of other white rounded mineral shapes of varying sizes, some low and lumpy, some standing like short pillars — all of them irregular, none of them straight-edged. 32mm anamorphic look, f/8, from 20 metres at 1.2 metre height, pale orange-tinted 4200K daylight at roughly half Earth brightness, soft-edged shadows, full crust texture everywhere.

PANEL 2 — TOP RIGHT, INTERIOR DARK: the interior of the same outpost, sealed for fourteen years, lit ONLY by a single narrow cool white torch beam (5500K) entering from the lower left. A hexagonal central node roughly 8 metres across with a flat low ceiling. Everything is coated in a THIN POWDERY WHITE FILM — a fine dusting of mineral over every horizontal surface, much lighter than the thick crust outside, because the aerosol could not reach in here. The beam sweeps across a round communal table and one sleeping berth, leaving most of the room in deep near-black shadow. Dust motes drift visibly inside the beam. 32mm look, f/2.8, ISO 3200, from 3 metres at chest height, shallow depth in the lit area with everything beyond falling to black. No ambient fill — the unlit parts of the room are genuinely dark.

PANEL 3 — BOTTOM LEFT, INTERIOR LIT: the SAME room with power restored, lit by a single recovered ceiling panel throwing pale warm-white light (3500K) across the whole space at low intensity — dim but even, the light of a system running on reserve power. Now fully visible: FOUR sleeping berths recessed into the flat panelled walls, privacy curtains hanging slack and pale with dust, three drawn and one pushed open. A round communal table at the centre with a single drinking vessel, a small hand tool and a folded square of fabric still resting on it, exactly where they were left. A wall panel showing ABSTRACT SLOW PULSING LIGHT PATTERNS in amber. A row of FOUR EMPTY WALL HOOKS beside the hatch, all four bare. The thin powdery white film still coats every horizontal surface, undisturbed except for one clean handprint on the table edge. 32mm look, f/4, ISO 1600, from 3.5 metres at chest height, taking in the table, the berths and the hook row together.

PANEL 4 — BOTTOM RIGHT, THE FOUR HOOKS: tight detail of the row of FOUR WALL HOOKS mounted side by side on a clean white composite wall panel beside the hatch frame. Simple bent metal, spaced evenly about 30cm apart, each with a small worn patch on the wall beneath it where something used to hang and rub. ALL FOUR HOOKS ARE EMPTY. A thin powdery white mineral film coats the tops of the hooks and the wall around them. The mustard-yellow seam trim runs along the panel edge, dulled by dust. 100mm macro look, f/4, from 0.8 metres, level with the hooks and straight on, sharp across the full row so all four read equally, dim warm-white 3500K light from above and slightly left throwing four small soft shadows down the wall.

Negative: NO people, figures, bodies, silhouettes or remains in any panel; the berths are empty and the room is unoccupied. NO clothing or equipment hanging on any hook — all four stay completely bare. NO readable text, letters, numbers, symbols, name plates or labels on any panel, display, object or surface — abstract pulsing light only. The mineral crust and the dust film NEVER glow or shimmer. No doors, windows or markings visible on the exterior of the outpost — everything is buried. No volumetric god-ray beams — the torch light in panel 2 is a defined cone with clear falloff. NO text, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare. Static stable geometry, nothing morphing. Photorealistic with 35mm film grain.
```

---

# 🖼️ BÖLÜM 5 — FİLM KAPAĞI `KP` 🔴

> Metinsiz üretilir [Ders 34] — tipografi post-prodüksiyonda.
> Kaynak: `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`
>
> **Merak boşluğu:** Kadının kaskında ve omuzlarında taş büyüyor.
> Arkasında bir tarla dolusu beyaz şekil — biri fazlasıyla insan biçimli.
> Seyirci "bu ne?" diye soruyor ve cevap filmde.

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels, 16:9 landscape. NO TEXT ANYWHERE IN THE IMAGE. YouTube thumbnail optimized — must read at 120 pixels wide.

SUBJECT — FILLS THE FRAME: A 36-year-old woman in extreme close-up, head and shoulders filling at least 60% of the total frame area, positioned in the RIGHT HALF, her body angled slightly left. HER EYES SIT ON THE UPPER THIRD LINE and stare directly into the camera — steady, unblinking, neither afraid nor calm.

Her face is seen through a FULLY TRANSPARENT SEAMLESS VISOR with no tint and no obscuring reflection: deep brown skin with clearly visible pore texture and no airbrushing, broad high cheekbones, rounded jaw, dark brown eyes, thick eyebrows, laugh lines at the outer corners, a small old healed piercing mark on her left nostril, a vertical crack in her lower lip. Black very short cropped tightly coiled hair with grey strands at the temples. Mouth closed, jaw set.

THE HOOK — CRUST ON HER: a rough BONE-WHITE crystalline crust, one to two centimetres thick, has grown across the TOP OF HER HELMET and over BOTH SHOULDERS, with fine fracture lines running through it where movement has broken it. The crust stops cleanly at the visor rim — the glass over her face is completely clear. Matte, faintly pearlescent, visible crystal grain. She is being buried while still alive and still looking at you.

BACKGROUND — LEFT THIRD: a rust-brown plain scattered with white mineral formations of varying size, thrown soft by shallow depth of field and desaturated to roughly 65%. One formation in the mid-distance has an unmistakably upright, human-like silhouette, rounded and unresolved with no face and no limbs. The UPPER LEFT is clean, uncluttered pale sky — open negative space reserved for the title added later in post.

COLOR — TWO COLORS ONLY: BONE-WHITE crust and RUST-BROWN plain dominate. One accent only: the worn mustard-yellow band at her visor rim. No other colors, no blue, no teal, no green. Increase final saturation by 20% so both survive at thumbnail scale.

LIGHT: pale orange-tinted daylight at 4200K from the low left, soft-edged shadows — correct for a thin atmosphere — but every surface keeps full texture: skin pores, crystal grain, dust. Sharp focus on the eyes; they are the sharpest thing in the image. 0% bloom, no glow filter, no lens flare, no vignette.

COMPOSITION: face 60%+ of frame, right of centre; eyes on the upper third line; 30-40% clean negative space in the upper left; LOWER-RIGHT CORNER completely empty — no detail, no elements, YouTube's duration badge covers this zone.

NEGATIVE: no text, letters, numbers, logo or watermark anywhere. The crust NEVER glows, shimmers or sparkles — matte stone only. No crust on the visor glass. No visor tint, no HUD. No bodies, no faces in the background formations — the upright shape stays ambiguous and unresolved. Exactly one person in focus, no duplicate, no reflection of another figure. No airbrushed or plastic skin. Not CGI, not Unreal Engine, not video game. Photorealistic with 35mm anamorphic film grain.
```

## 🔄 PLAN B VARYANTI (ayrı dosya değil — aynı prompta 4 değişiklik)

> Kılavuz §7: 48 saat sonra CTR %4'ün altındaysa devreye alınır.
> Yukarıdaki prompta şu dört müdahale yapılır, gerisi aynı kalır:

```
1. ÖZNE DEĞİŞİR:  Kadın çıkar. Yerine sağ yarıda, kare yüksekliğini
   dolduran TEK BİR DİK OLUŞUM (≈1.8 m) gelir — silueti ayakta duran
   bir insanınki, ama yüz/el/ekipman YOK, yalnızca şekil.
2. KANCA DEĞİŞİR: Alçak yıldız oluşumun ARKASINDA. Işık üst kısmın
   yarı saydam bölgesinden GEÇİYOR; taşın İÇİNDE soğuk MAVİ-BEYAZ bir
   saçılma ve derinde bulanık, çözünmeyen daha koyu bir çekirdek var.
   Alt üçte iki opak mat beyaz kalır.
3. PALET DEĞİŞİR:  kemik beyazı + hardal yerine → PAS KAHVE ova +
   SOĞUK MAVİ-BEYAZ iç saçılma. Başka renk yok.
4. NEGATİFE EKLENİR: saçılma taşın DIŞINA taşmaz, hale yapmaz, yere
   ışık düşürmez; god ray yok, lens flare yok.
   Kompozisyon kuralları (üst sol boşluk, sağ alt köşe boş) aynen kalır.
```

## ✍️ POST-PRODÜKSİYON TİPOGRAFİSİ

```
BAŞLIK:        THE SLOW STONE          (3 kelime — kılavuz sınırı)
FONT:          Bebas Neue / Impact / Oswald Bold — ultra kalın sans-serif
BOYUT:         60-80 punto, geniş harf aralığı
KONUM:         ÜST SOL çeyrek — yüzün/oluşumun üstüne değil, boş göğe
RENK:          Saf beyaz
OKUNABİLİRLİK: 3-4 px KALIN siyah dış çizgi + belirgin drop shadow
               ⚠️ İnce gölge yetmez [kılavuz §3]
KONTRAST:      Metin ile arka alan arasında minimum 4.5:1 (WCAG)
ALT BAŞLIK:    YOK — açıklayıcı alt başlık merak boşluğunu kapatır
YASAK ALAN:    Sağ alt köşe tamamen boş (süre rozeti)
FİNAL EXPORT:  1280×720, 72 DPI, JPEG %85 (Squoosh)
```

---

# ⚠️ ÜRETİM NOTLARI

```
1. ÇOK PANELLİ SAYFANIN BEDELİ — EN YÜKSEK RİSK
   Tek karede 3-5 panel üretmek panel başına çözünürlük düşürür ve
   modelin panelleri birbirine karıştırma ihtimalini artırır.
   ZORUNLU KONTROL — RK sayfasında:
     • 5 panelde de AYNI kişi mi? (kaş, burun izi, çene, saç dokusu)
     • Panel 4 TEMİZ, panel 5 KABUKLU mu? (karışmışsa at)
     • Suit konfigürasyonu 4 ve 5'te birebir aynı mı?
   Sapma varsa sayfayı at ve yeniden üret. Sahne üretimine BAŞLAMA.

2. SAYFA KAYMAYA DEVAM EDERSE — PANEL AYIRMA PLANI
   Model tutarlı 5 panel veremiyorsa: RK'yı üç ayrı üretime böl
   (yüzler / tam boy temiz / tam boy kabuklu), aynı seed'i kullan.
   Bölünmüş paneller eski R1-R5 kodlarıyla birebir eşleşir; kısım
   dosyalarındaki referans satırları yine geçerli kalır.

3. MİNERALİN PARLAMASI
   Model "kristal" görünce ışıldatmak istiyor. Bu filmin minerali MAT
   TAŞTIR. Her sayfada "never glows, never shimmers, never sparkles"
   negatifi var — üretimde ilk kontrol edilecek şey budur.
   Tek istisna: kapak Plan B varyantındaki arkadan ışıklı yarı saydam
   bölge — o da taşın DIŞINA taşmıyor.

4. OLUŞUMLARDA YÜZ ÇIKMASI
   RM panel 3'te ve kapakta insan biçimli şekiller var. Model bunlara
   yüz, el, ekipman eklemeye çalışacak. Negatiflerde tekrarlandı:
   "no faces, no limbs, no equipment — shape only".
   Yüz çıkarsa at ve yeniden üret.

5. SAYFALARDA YAZI ÇIKMASI
   Referans sayfası formatı modelde "panel başlığı / etiket / ok"
   refleksi tetikliyor. Dört promptun da negatifinde ayrıca yasaklandı.
   Gutter'larda bile yazı olmayacak — çıkarsa at.

6. SAHNE ÜRETİMİNDE KULLANIM
   Kısım dosyaları "R3 · R16" gibi eski kodlar veriyor. Karşılığı:
   ilgili SAYFANIN TAMAMINI yükle (R3 → RK, R16 → RM).
   Sayfanın tamamını yüklemek tek panelden daha güçlü bir çapadır.
```
