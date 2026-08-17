# ☄️ THE WAKING GROUND — REFERANS PAKETİ VE FİLM KAPAĞI

## Karakter · Halat · Yüzey · Faz · Araç · Sonda — **her varlık için TEK referans sayfası**
### 6 birleşik referans sayfası + 1 kapak = 7 görsel

> ⚠️ **BU DOSYA SAHNE PROMPTLARINDAN ÖNCE ÜRETİLİR.**
> Bu film 60 sahne ve **start/end frame zinciri** kullanıyor: her sahnenin
> başlangıç karesi bir öncekinin bitiş karesidir. Zincirde çapa kilitlenmezse
> sapma birikir ve 3. fazda yüz kayar — geri dönüşü yoktur.
> `KILAVUZ_REHBERI.md` §2.4: *"Referans paketi EN BAŞTA hazırlanır."*
>
> Üretim sırası: **bu dosya → seed'leri kilitle → faz dosyaları.**
>
> Tüm promptlar Ders 34 uyumlu: **karakter adı hiçbir promptta geçmez.**
> Milliyet ifadesi de geçmez (kılavuz §7 — doğrulanmış üretim reddi).
> Bible'daki "Lübnan asıllı Kanadalı" tanımı SADECE bu dosyada ve README'de
> kalır; promptlarda yalnızca fiziksel tarif kullanılır.

---

# 📋 ÜRETİM SIRASI VE SEED TAKİP TABLOSU

| # | Referans sayfası | İçindekiler | Öncelik | Seed | Durum |
|---|---|---|:---:|---|:---:|
| **RK** | KARAKTER SAYFASI | 5 panel: ön yüz · sol profil · vizör ardı · tam boy FAZ 1 temiz · tam boy FAZ 4 tozlu | 🔴 ZORUNLU | | ☐ |
| **RH** | HALAT VE ANKRAJ SAYFASI | 4 panel: zıpkın ankrajı · GERGİN halat · GEVŞEK halat · harness + eldiven kavrama | 🔴 ZORUNLU | | ☐ |
| **RY** | YÜZEY SAYFASI | 4 panel: siyah kabuk makro · buz yaması · don sınırı · taze jet çukuru | 🔴 ZORUNLU | | ☐ |
| **RF** | FAZ ATLASI | 5 panel: AYNI manzara, 5 fazda — filmin omurgası | 🔴 ZORUNLU | | ☐ |
| **RV** | KESTREL SAYFASI | 3 panel: dış + zıpkın bağları · airlock · karot rafı | 🟡 GEREKLİ | | ☐ |
| **RM** | MERIDIAN SAYFASI | 4 panel: buzda gömülü · serbest · ölü zıpkın kablosu · amber durum ışığı | 🔴 ZORUNLU | | ☐ |
| **KP** | FİLM KAPAĞI | tek sürüm, **metinsiz** | 🔴 ZORUNLU | | ☐ |

```
ÜRETİM SIRASI — BU SIRAYLA:

  RK  →  yüz ve suit kilitlenir      (onaylanmadan HİÇBİR ŞEYE başlama)
  RH  →  halat ve ankraj dili        (her karede var — ikinci en kritik)
  RY  →  yüzey malzemesi
  RF  →  5 fazın ışığı ve gökyüzü    (RY onaylandıktan sonra)
  RM  →  MERIDIAN                    (Faz 3'ün duygusal merkezi)
  RV  →  KESTREL
  KP  →  kapak, RK kilitlendikten SONRA
```

---

# 🔗 SAHNE → SAYFA EŞLEME

> Sahne üretiminde ilgili SAYFANIN TAMAMI referans olarak yüklenir.
> Tek panel yüklemekten daha güçlü bir çapadır — model tüm panelleri görür.

| Faz | Sahneler | Yüklenecek sayfalar |
|---|---|---|
| **FAZ 1 — Donmuş** | S1-S12 | RK · RH · RY · RF(panel 1) · RV |
| **FAZ 2 — Terleme** | S13-S24 | RK · RH · RY · RF(panel 2) |
| **FAZ 3 — Açılan** | S25-S36 | RK · RH · **RM** · RF(panel 3) |
| **FAZ 4 — Patlama** | S37-S48 | RK · RH · **RM** · RY(panel 4) · RF(panel 4) · RV |
| **FAZ 5 — Kuyruk** | S49-S60 | RK · RF(panel 5) · RV |

**Özel sahneler:**

```
S4   ilk yüz yakın çekimi      → RK panel 1 ve 3 kritik
S21  ilk jet                    → RY panel 4 + RF panel 4
S29  MERIDIAN bulunuyor         → RM panel 1 (buzda gömülü hâli)
S32  temas (100mm makro)        → RM panel 2 ve 4
S39  ankraj kopuyor             → RH panel 2 ve 3 (gergin → gevşek)
S42  🏆 imza çekim              → RM panel 2 + RF panel 4
S52  ters kar                   → RF panel 5
S57  kalkış (zıpkınlar kopuyor) → RV panel 1
```

---

# 👤 BÖLÜM 1 — KARAKTER SAYFASI `RK` 🔴

> **Filmin en kritik varlığı.** 60 sahnenin ve 75 imajın yüz çapası bu tek
> görselde. ⚠️ En yüksek çözünürlükte üret. Paneller birbirinden saparsa
> sayfayı at ve yeniden üret — sahne üretimine geçme.

```
Photorealistic cinematic CHARACTER REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FIVE CLEAN PANELS separated by thin neutral mid-grey gutters: a TOP ROW of three equal portrait panels, and a BOTTOM ROW of two equal full-figure panels. Every panel shows THE SAME ONE WOMAN — no other individuals appear anywhere on the sheet. Neutral studio-style lighting throughout for reference use.

THE PERSON — IDENTICAL IN ALL FIVE PANELS: a 41-YEAR-OLD WOMAN, 1.66 metres, slight and wiry — a field scientist's build, durable rather than muscular. Warm mid-brown skin with clearly visible pore texture and natural subsurface scattering; no airbrushing, no smoothing, no beauty retouching. Sharp, high cheekbones. Dark brown eyes, almost black, with pronounced lines at the outer corners. Thick, naturally arched dark eyebrows. A straight narrow nose. A thin upper lip and a fuller lower lip. A PALE HEALED BURN SCAR ABOUT 3 CM LONG ON HER LEFT TEMPLE, smooth and slightly lighter than the surrounding skin. A small flat scar just above her right eyebrow. Visible fatigue shadowing under both eyes. No makeup, no jewellery. HAIR: dark brown going grey at the temples, pulled back into a tight braid and completely contained — not a single loose strand anywhere.

PANEL 1 — TOP LEFT, FACE FRONT, NO HELMET: head and shoulders, facing the camera straight on, neutral expression, mouth closed, eyes level with the lens. Only the collar ring of a dirty-white surface suit is visible at the base of the panel, with a burnt-orange band along its edge. 85mm look, sharp focus across the whole face.

PANEL 2 — TOP CENTRE, FACE LEFT PROFILE, NO HELMET: exact 90-degree left profile, head and shoulders, looking straight ahead out of the panel, neutral expression. THE PALE BURN SCAR ON THE LEFT TEMPLE IS FULLY VISIBLE AT THIS ANGLE and must read clearly. The sharp cheekbone catches the light; the hairline and the tight braid read clearly. Same dirty-white collar ring with burnt-orange edge at the base.

PANEL 3 — TOP RIGHT, FACE THROUGH THE VISOR: close-up seen through a FULLY TRANSPARENT SEAMLESS HELMET VISOR — the glass is perfectly clear with no tint, no coating and no reflection obscuring her, so her entire face is completely readable and skin texture is visible through the glass. Neutral alert expression, mouth closed. The helmet is a one-piece dirty-white shell with a narrow burnt-orange band around the visor rim and a single narrow light housing at its upper right. A faint film of breath condensation sits at the very bottom edge of the glass. Slight three-quarter angle.

PANEL 4 — BOTTOM LEFT, FULL FIGURE, PHASE 1 CLEAN: standing upright, full body with headroom, arms relaxed at her sides, three-quarters to camera, face readable through the clear visor. SUIT — THIS EXACT CONFIGURATION REPEATS IN EVERY SCENE OF THE FILM: a DIRTY-WHITE base, a used cream-grey white rather than pure white, with BURNT-ORANGE accents at both shoulder caps (6 cm bands), a chest cross-strap, both knee panels and both glove wrist bands. Three abstract chest indicators in a triangle — left a slow blue oval pulse, centre a green bar, right a WHITE RING — with NO letters and NO numbers. On the LEFT forearm a core-sampling control panel showing abstract amber segments. On the RIGHT forearm a single VERTICAL LIGHT BAR, shown here FULL and bright. A heavy industrial WAIST HARNESS with two carabiner attachment points and burnt-orange stitching. Thick articulated dirty-white gloves with DARK GREY worn grip pads on the palms and fingertips. Flat-soled dirty-white boots with a burnt-orange heel band — NO magnetic soles. DUST STATE: CLEAN — the suit carries only faint use-wear, and NO black dust anywhere.

PANEL 5 — BOTTOM RIGHT, FULL FIGURE, PHASE 4 HEAVILY DUSTED: the same woman in the same pose, the same suit in the identical configuration, face readable through the clear visor, expression tired and set. DUST STATE: fine BLACK-GREY dust has settled over the FRONT-FACING surfaces only — across the chest, the front of both thighs, both knee panels, the tops of the forearms and the backs of both gloves, dulling the dirty-white to a smudged charcoal grey. The backs of the shoulders and the visor glass itself stay clear. The dust is a fine matte powder that clings, not a crust and not mud. This panel and panel 4 must be directly comparable — SAME face, SAME suit, ONLY the dust level differs.

Camera and light across the sheet: soft even neutral key at 5000K with gentle fill, mid-grey seamless background in every panel, shadows soft but present. Every skin texture, pore, scar, fabric weave, strap, buckle and dust grain stays fully visible.

Negative: the five panels show ONE person only — no second individual, no other model, no crowd, no reflection of another figure. The face, hair, build, scars and suit are IDENTICAL across every panel — no drifting, no morphing, no age or feature change between panels. NO black dust anywhere in panels 1-4. NO visor tint, no mirrored coating, no HUD graphics, no display overlay on the glass. NO text, letters, numbers, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No airbrushing, no waxy or plastic skin, no beauty filter, no makeup, no jewellery, no loose hair. No weapon, no tool in her hands — both hands empty in every panel. No stylisation, no illustration, no CGI look, no video game render. Photorealistic with 35mm film grain.
```

---

# 🪢 BÖLÜM 2 — HALAT VE ANKRAJ SAYFASI `RH` 🔴

> **Bu filmin fiziksel dili.** Halat 60 sahnenin neredeyse hepsinde karede.
> Ders 26 (halat fiziği) ve Ders 23 (sıfır-g katılığı) bu sayfayla yönetilir.
> Gergin ve gevşek hâlin **aynı kadrajda karşılaştırılması** kritik: S39'da
> ankraj koptuğunda seyirci farkı anında hissetmeli.

```
Photorealistic cinematic EQUIPMENT REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FOUR EQUAL PANELS in a 2×2 grid, separated by thin neutral mid-grey gutters. NO faces and NO full figures anywhere on the sheet — only gloved hands and a waist harness appear, in panel 4.

THE ENVIRONMENT — IDENTICAL IN ALL PANELS: the surface of a comet nucleus. An ABSOLUTELY BLACK crust of loose fine dust, darker than charcoal, roughly 4 percent reflectance, with a fine granular texture and shallow irregular ridges. Hard directional sunlight at 5800K from the upper left as a small brilliant point source — no atmosphere, so shadows are ABSOLUTELY BLACK with razor-sharp edges and there is NO fill light of any kind. Pure black space above with sharp non-twinkling stars.

THE HARDWARE — IDENTICAL IN ALL PANELS: a HARPOON ANCHOR, 40 cm long, matte BURNT ORANGE, a blunt cylindrical shaft with three short splayed barbs at its buried end and a steel eyelet at its exposed head, fired into the black crust so that roughly two thirds is driven in and one third stands proud, with a small raised collar of displaced black dust around its entry point. The TETHER: an 8 mm STEEL-POLYMER LINE in pale grey, its braided outer sheath clearly visible, worn and slightly fuzzed in places from use.

PANEL 1 — TOP LEFT, THE ANCHOR: close detail of the harpoon anchor driven into the black crust, seen from a low angle at 0.6 metres, 85mm look. The tether runs from its eyelet out of the top right of the frame, TAUT and dead straight. The disturbed dust around the entry point sits in a raised collar exactly where it was pushed, undisturbed since. Sharp black shadow thrown to the lower right by the hard sunlight.

PANEL 2 — TOP RIGHT, TETHER TAUT: a length of the same 8 mm pale grey tether crossing the frame from lower left to upper right above the black crust, 50mm look from 2 metres. THE LINE IS PERFECTLY STRAIGHT — under this gravity a loaded tether shows no visible sag at all, reading as a drawn geometric line against the black ground. It hangs roughly 30 cm above the surface, its hard-edged shadow falling on the crust below and slightly offset, proving the gap. Every fibre of the braid is sharp.

PANEL 3 — BOTTOM LEFT, TETHER SLACK: the SAME tether, the SAME framing, camera distance and lens as panel 2, now UNLOADED. The line has fallen into wide, slow, lazy curves — long shallow arcs with big radii, floating between 20 cm and 1.5 metres above the crust, some sections drifting upward rather than down. Nothing sags in a heavy catenary the way rope does on Earth; it is loose, weightless and lazily curved, its shadow on the crust below broken into separate curved segments. This panel and panel 2 must be directly comparable — SAME rope, SAME framing, ONLY the tension differs.

PANEL 4 — BOTTOM RIGHT, HARNESS AND GRIP: close detail at 0.5 metres, 85mm look, of a heavy industrial WAIST HARNESS in dirty white with burnt-orange stitching and TWO steel carabiner attachment points, one carabiner clipped closed around the pale grey tether and the second hanging free and open. Two thick articulated dirty-white GLOVES with dark grey worn grip pads grasp the tether above the carabiner, one hand above the other in a hauling grip, the fingers wrapped fully around the line with a clear structural boundary at every contact point. Only the hands, forearms and the harness at the waist are in frame — no face, no helmet, no full body.

Negative: NO faces, NO helmets, NO full figures anywhere on the sheet. The tether NEVER passes through the ground, through rock or through itself, and never clips into any surface — rigid-body collision at every point. In panel 2 the taut line has NO sag and NO curve. In panel 3 the slack line NEVER hangs in a heavy Earth-like catenary and NEVER lies flat on the ground. The harpoon anchor is IDENTICAL in every panel — same length, same orange, same barbs, same entry collar. NO glow, no shimmer, no emitted light from any surface; the orange anchor is matte painted metal catching hard sunlight. NO fill light — every shadow is absolutely black with a sharp edge. NO dust hanging motionless in the air. NO text, letters, numbers, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare. Photorealistic with 35mm anamorphic film grain.
```

---

# 🪨 BÖLÜM 3 — YÜZEY SAYFASI `RY` 🔴

> Filmin görsel imzası: **%4 albedo siyah kabuk ile beyaz buhar arasındaki
> aşırı kontrast.** Bu sayfa siyahın ne kadar siyah olduğunu kilitler.

```
Photorealistic cinematic MATERIAL AND TERRAIN REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FOUR EQUAL PANELS in a 2×2 grid, separated by thin neutral mid-grey gutters. NO people, figures, bodies or hands anywhere on the sheet.

THE MATERIAL — CONSISTENT IN ALL PANELS: the surface of a comet nucleus, one of the darkest surfaces in the solar system at roughly 4 percent reflectance — DARKER THAN CHARCOAL, darker than asphalt, a matte lightless black-grey. It is covered in a loose fine-grained organic dust layer between 5 and 40 cm deep, granular and slightly clumped, with shallow ridges, small collapse pits and fine fracture lines. Beneath the dust in places lies BRIGHT WHITE WATER ICE. Hard directional sunlight at 5800K from a small brilliant point source at the upper left; no atmosphere, so shadows are ABSOLUTELY BLACK with razor-sharp edges, there is NO fill light and NO haze of any kind. Pure black space with sharp non-twinkling stars above every horizon.

PANEL 1 — TOP LEFT, BLACK CRUST MACRO: extreme close detail of the dust crust filling the panel, 100mm macro look at 0.25 metres, raking hard sunlight from the left at a very low angle so that every grain, clump and micro-ridge throws its own hard black shadow. The material must read as LOOSE DRY GRANULAR DUST, not as solid rock and not as soot — individual grains and small aggregates are resolvable. The overall tone stays extremely dark: the brightest lit grain is still a dark grey, and the shadows are pure black.

PANEL 2 — TOP RIGHT, EXPOSED ICE PATCH: the same black crust, but here the dust layer has been torn open across roughly one third of the panel to reveal BRIGHT WHITE WATER ICE beneath — a hard, granular, slightly translucent ice surface with a rough frosted texture and small sharp-edged crystal facets, sitting 10 to 20 cm below the level of the surrounding dust. The boundary between black dust and white ice is ragged and irregular, with loose dark grains scattered across the ice edge. The contrast between the two materials is extreme and is the point of the panel: near-black beside near-white in the same hard light. 50mm look from 1.5 metres, deep focus.

PANEL 3 — BOTTOM LEFT, THE FROST LINE: a wide low view across the surface, 50mm look from 3 metres at 0.4 metre height, showing a VISIBLE BOUNDARY running across the terrain: on the near side a pale WHITE FROST COATING lies over the black dust like a thin even rime, and on the far side the crust is BARE BLACK with no frost at all. The boundary itself is a soft-edged but clearly readable line, a few centimetres wide, meandering across the ground. A few thin wisps of white vapour rise vertically from cracks on the bare side — narrow, structured, straight streams moving upward and outward, never curling and never billowing.

PANEL 4 — BOTTOM RIGHT, FRESH JET PIT: the aftermath of a vent opening — a fresh PIT in the crust roughly 3 metres across, its rim broken into angular slabs of black crust tipped outward, exposing bright white ice down inside the cavity. Fine dark grains and small ice fragments are suspended just above the rim, all of them travelling slowly UPWARD and OUTWARD in straight lines, never falling back. From the centre of the pit a narrow column of white-grey vapour and dust rises with SHARP STRUCTURED EDGES — a column, not a cone, not a mist. 28mm anamorphic look from 12 metres at 1.5 metre height, deep focus, the pit and the base of the column both sharp.

Negative: NO people, figures, bodies, hands, tools or equipment anywhere on the sheet. The crust NEVER glows, never emits light, never shimmers; it is the darkest surface in the frame in every panel and must never read as mid-grey rock. NO fill light, NO ambient bounce — shadows are absolutely black with sharp edges. The vapour is MATTER, not light: it reflects hard sunlight and casts its own shadow, and it NEVER glows, flares or blooms. NO fire, no flame, no orange heat, no combustion, no engine glow — this is sublimation, ice turning directly to gas. NO swirling, curling, billowing or smoke-like motion; no vortices, no fog banks, no atmospheric haze, no aerial perspective. Suspended particles are always moving upward and outward in straight lines, never hovering, never falling back to the ground, never frozen in place. NO liquid water anywhere. NO text, letters, numbers, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare. Photorealistic with 35mm anamorphic film grain.
```

---

# 🌗 BÖLÜM 4 — FAZ ATLASI `RF` 🔴

> **Filmin omurgası.** Bu filmde değişen karakter değil DÜNYADIR: 5 faz =
> dünyanın 5 hali. Bu tek sayfa, aynı manzarayı beş fazda gösterir ve
> ışık/gökyüzü ilerlemesini kilitler. RY onaylanmadan üretme.

```
Photorealistic cinematic ENVIRONMENT PROGRESSION SHEET, 16:9, maximum resolution. A single frame divided into FIVE EQUAL VERTICAL PANELS side by side, separated by thin neutral mid-grey gutters. NO people, figures, bodies or vehicles anywhere on the sheet.

THE SAME LOCATION IN ALL FIVE PANELS — IDENTICAL COMPOSITION, IDENTICAL CAMERA: a wide view across the black dust surface of a comet nucleus from 25 metres at 1.5 metre height, 28mm anamorphic look, deep focus. The SAME terrain features appear in every panel in the SAME positions: a low ridge of black crust running across the middle distance, one prominent boulder-sized crust block at the left, an irregular white ice patch at the lower right, and the horizon two thirds of the way down the frame. ONLY THE LIGHT, THE SKY AND THE ACTIVITY CHANGE from panel to panel. The sun is a hard directional source from the upper left throughout, at 5800K.

PANEL 1 — PHASE ONE, FROZEN: the sun is a SMALL BRILLIANT POINT, not a disc, throwing weak but absolutely hard light. Long shadows stretch across the crust, their interiors pure black with razor edges. The sky is PURE BLACK, dense with sharp non-twinkling stars. Nothing moves. No vapour anywhere. The ice patch is dull, dry and frost-free. This panel is almost monochrome: black ground, white ice, black sky.

PANEL 2 — PHASE TWO, SWEATING: the same view, the sun visibly brighter but still a hard point. THIN WHITE VAPOUR now leaks from two narrow cracks near the ridge — straight, structured, vertical wisps rising and dispersing upward, no curling. A pale frost coating has appeared on the shaded side of the ridge. The sky is still pure black with sharp stars. Shadows remain absolutely black.

PANEL 3 — PHASE THREE, OPENING: the sun is now strong, close to becoming a small disc. The ice patch at the lower right has GROWN and brightened as dust has blown off it, and the crust around it has visibly retreated, exposing a shallow depression. Localised white vapour hangs in loose vertical columns over three separate vents. The stars in the sky are very slightly dimmed. Where sunlight strikes exposed ice, it scatters into COOL BLUE-WHITE tones — the first colour in the film that is neither black nor white.

PANEL 4 — PHASE FOUR, ERUPTION: the sun is a BLINDING DISC, its light so strong that lit crust surfaces blow out toward white while shadows stay absolutely black — extreme contrast with no midtones at all. THREE VIOLENT JETS erupt from the terrain: narrow-based columns of white-grey vapour and dust, 2 to 5 metres wide at their feet and rising 150 to 250 metres, with SHARP STRUCTURED EDGES, not misty and not cone-shaped. Fresh black pits have opened at their bases, their rims broken into outward-tipped slabs. Fine dust streams upward across the whole frame in straight lines. The sky behind is still black but the stars are now hard to see through the dust.

PANEL 5 — PHASE FIVE, TAIL: the same terrain, quiet again, with fresh pits and a lowered surface where ice has gone. THE SKY IS NO LONGER BLACK: a thin coma envelops everything, scattering the sunlight into a faint MILKY BLUE-WHITE glow across the whole sky, and the stars have faded to a few dim points. For the first time in the sheet the light is SOFT — shadows still exist and still have direction, but their edges are diffused and their interiors are no longer pure black. Above and behind, a TAIL crosses the sky from horizon to horizon as a broad, faintly structured pale band. Fine dust drifts UPWARD across the frame like inverted snow.

Negative: NO people, figures, bodies, vehicles, tethers or equipment anywhere on the sheet. The terrain features are IDENTICAL in position and shape in all five panels — the ridge, the block and the ice patch never move, never change form and never morph; only light, sky and activity differ. The jets in panel 4 are MATTER, not light: they reflect hard sunlight, cast shadows and NEVER glow, flare or bloom. NO fire, no flame, no orange, no combustion, no engine exhaust anywhere. NO swirling, curling or billowing; vapour rises in straight structured columns and dust always travels upward and outward, never falling back and never hovering motionless. In panels 1 to 4 there is NO fill light and NO atmospheric haze — shadows are absolutely black with razor edges. The softening in panel 5 comes only from the coma and must still preserve full surface texture: dust grains, crust ridges and ice facets stay visible. NO text, letters, numbers, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare, no god rays. Photorealistic with 35mm anamorphic film grain.
```

---

# 🛰️ BÖLÜM 5 — MERIDIAN SAYFASI `RM` 🔴

> Filmin duygusal merkezi ve S42'nin imza görüntüsü. 71 yıl önce buraya
> inmiş, ankrajı tutmamış, buzun yuttuğu bir sonda. Noor'un aynası.

```
Photorealistic cinematic OBJECT REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into FOUR EQUAL PANELS in a 2×2 grid, separated by thin neutral mid-grey gutters. NO people, figures, bodies or hands anywhere on the sheet.

THE OBJECT — IDENTICAL DESIGN IN ALL PANELS: a 1.4-METRE ROBOTIC SCIENCE PROBE from an earlier era, not a crewed vehicle. A squat box-shaped body on THREE short splayed legs with small flat pads. Its body is wrapped in MULTI-LAYER INSULATION FOIL that was once gold: now dulled to a tarnished brass-brown, deeply wrinkled, creased and torn open in several places, with the darker layers beneath showing through the tears. WHITE ICE CRYSTALS have grown along its edges and seams, fusing the foil to the surface it rests on. A SINGLE SOLAR PANEL WING extends from one side, its visible portion CRACKED across two cells, its dark blue-black cells dulled by a film of black dust. A fired HARPOON projects from a launcher on the body, its thin steel cable running out and ending LOOSE and unattached a short distance away — the anchor never held. A SINGLE SMALL AMBER STATUS LIGHT sits on the upper face of the body: a dim point, not a lamp, illuminating nothing around it.

PANEL 1 — TOP LEFT, BURIED IN ICE (Phase 3 state): the probe seen from 2.5 metres at low angle, 50mm look, inside a hollow in a comet nucleus. ROUGHLY HALF THE PROBE IS ENCASED IN ICE — the lower body, two of the three legs and 60 percent of the solar wing are frozen into a mass of granular white water ice, its surface rough and frosted, so the machine appears to be growing out of the ice rather than standing on it. The exposed upper body, the torn foil and the top of the solar wing stand clear. Hard directional sunlight at 5800K from the upper left, absolutely black shadows with razor edges, no fill light. Black space above with sharp stars.

PANEL 2 — TOP RIGHT, FREE (Phase 4 state): the SAME probe, SAME three-quarter angle, SAME lens and distance as panel 1, now COMPLETELY FREE OF ICE — the ice that held it has sublimated away and the machine floats clear against black space, its three legs hanging with nothing beneath them, a few loose ice crystals and dark grains drifting upward past it in straight lines. Its foil, tears, cracked panel, fired harpoon and loose cable are IDENTICAL to panel 1 in every detail. The body is tilted a few degrees out of level, as an object that has just been released and has no weight to settle it. This panel and panel 1 must be directly comparable — SAME object, ONLY the ice differs.

PANEL 3 — BOTTOM LEFT, THE DEAD CABLE: detail at 1 metre, 85mm look, following the probe's fired harpoon cable from the launcher on its body out across the black crust. The cable is a thin steel line, dulled and slightly kinked, running roughly 3 metres and ENDING LOOSE — its harpoon head lies on the surface where it landed, barbs closed and clean, having never penetrated the crust. No entry hole, no disturbed collar of dust around the head: it simply lies there. Hard black shadows, extreme contrast between the pale cable and the near-black ground.

PANEL 4 — BOTTOM RIGHT, FOIL AND STATUS LIGHT MACRO: extreme close detail at 0.4 metres, 100mm macro look, of the probe's upper body where the tarnished gold-brown insulation foil meets the small AMBER STATUS LIGHT. Every crease, crumple, scuff and micro-tear in the foil is razor-sharp; ice crystals have grown into the deepest folds and along one torn edge, fused into the material. The status light is a small dim amber point roughly 8 mm across, lit but WEAK: it does not illuminate the foil around it, casts no glow and throws no light onto anything — it is simply a small coloured point in an otherwise hard-lit surface. Black dust has settled into the creases.

Negative: NO people, figures, bodies, hands or tools anywhere on the sheet. The probe design is IDENTICAL in all panels — same size, same three legs, same foil damage, same cracked panel, same fired harpoon; no drifting, no morphing, no added antennas, wheels, cameras or instruments between panels. The probe is 1.4 metres and must never read as a large vehicle or as a toy. The amber status light NEVER glows, blooms, flares or illuminates its surroundings — a dim point only. NO other light on the probe, NO interior lighting, NO screens, NO holograms. NO fire, no smoke, no exhaust. NO readable text, letters, numbers, symbols, flags, mission patches, logos or markings anywhere on the probe or its cable. The ice NEVER glows or shimmers; it is granular frosted water ice catching hard sunlight with clear falloff. NO fill light — shadows are absolutely black with sharp edges. NO liquid water, no melting, no dripping. Suspended particles in panel 2 travel upward in straight lines and never hover or fall. NO text, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare. Photorealistic with 35mm anamorphic film grain.
```

---

# 🚀 BÖLÜM 6 — KESTREL SAYFASI `RV` 🟡

> Noor'un iniş aracı. Bir gemi değil, bir kabin. Mikro yerçekiminde
> **üzerinde durmaz — bağlıdır.** Üç zıpkın kablosu her dış çekimde gergin.

```
Photorealistic cinematic VEHICLE REFERENCE SHEET, 16:9, maximum resolution. A single frame divided into THREE PANELS separated by thin neutral mid-grey gutters: ONE LARGE PANEL filling the left two thirds, and TWO STACKED SQUARE PANELS on the right. NO people, figures, bodies or hands anywhere on the sheet.

THE CRAFT — IDENTICAL DESIGN IN ALL PANELS: a 6-METRE-TALL compact single-crew surface lander — a cabin, not a ship. A squat vertical body on THREE SPLAYED LEGS with a 3-metre spread, each leg ending in a wide flat pad. Its hull is DIRTY-WHITE panelling, a used cream-grey white, with BURNT-ORANGE accent bands — the same colour language as the surface suit. From each landing pad a FIRED HARPOON is driven into the black crust below, and each harpoon cable runs TAUT AND DEAD STRAIGHT from pad to ground: in this gravity the craft is TETHERED DOWN, not resting under its own weight. On the upper hull sits a single CIRCULAR AIRLOCK HATCH with a BURNT-ORANGE manual locking lever. On one flank, a folding CORE STORAGE RACK with FOUR slots, ONE of them filled by a sealed grey cylinder. FOUR cold-white LED units (5500K) are mounted around the body, all aimed DOWNWARD. A 1.2-METRE DISH ANTENNA is mounted high on the hull, angled up and away toward deep space, and it NEVER changes direction in any panel.

PANEL 1 — LEFT, LARGE, EXTERIOR ON THE SURFACE: the full craft on the black dust crust of a comet nucleus, three-quarter front view from 15 metres at 1.2 metre height, 28mm anamorphic look, deep focus. All three legs, all three taut harpoon cables and their entry points in the crust are clearly visible. The four downward LEDs throw a defined ISLAND OF COLD WHITE LIGHT on the black ground around the craft, with a sharp falloff edge beyond which the crust returns to near-black. Hard directional sunlight at 5800K from the upper left rakes the hull; shadows are absolutely black with razor edges and there is no fill light. Pure black sky with sharp non-twinkling stars. The craft must read as exactly 6 metres tall — physically accurate engineering proportions, never miniature, never toy-like.

PANEL 2 — TOP RIGHT, AIRLOCK HATCH DETAIL: close view at 1.2 metres, 50mm look, of the circular airlock hatch on the upper hull, CLOSED. A recessed circular pressure door roughly 0.8 metres across, set into dirty-white panelling with a burnt-orange band running around its rim, with a single heavy BURNT-ORANGE manual locking lever in the closed position and a ring of evenly spaced latching dogs around the frame. Fine black dust has settled into the recessed seams. Hard sunlight from the left, black shadow to the right.

PANEL 3 — BOTTOM RIGHT, CORE STORAGE RACK: close view at 1 metre, 50mm look, of the folding sample rack on the craft's flank: a simple bracketed frame with FOUR cylindrical slots side by side. THREE SLOTS ARE EMPTY, showing their bare padded interiors. ONE SLOT holds a sealed grey sample cylinder about 40 cm long with a plain matte finish and a simple mechanical clamp closed over it. Black dust has settled on the upper edges of the rack. Hard directional sunlight from the upper left, absolutely black shadows inside the empty slots.

Negative: NO people, figures, bodies or hands in any panel. The craft design, size, leg spread, hatch, rack and antenna are IDENTICAL in every panel — no proportion drift, no added or removed hardware. The three harpoon cables are ALWAYS TAUT and dead straight, never slack, never sagging, and they never pass through the ground or through the craft. The dish antenna points the SAME direction in every panel. NO engine glow, no exhaust, no flame, no thruster light — the craft is completely inert. The LED light is a defined cone with a sharp falloff edge, never a soft glow, never a volumetric god-ray beam, never a bloom halo. NO readable text, letters, numbers, symbols, flags, mission patches, logos or markings anywhere on the hull. NO screens or holographic displays. NO fill light — shadows are absolutely black with razor edges. NO dust hanging motionless in the air. NO text, labels, captions, arrows, callouts, panel titles or watermarks anywhere on the sheet or in the gutters. No bloom, no glow filter, no lens flare. Not miniature, not toy-like, not a CGI or video game render. Photorealistic with 35mm anamorphic film grain.
```

---

# 🖼️ BÖLÜM 7 — FİLM KAPAĞI `KP` 🔴

> ⚠️ **README'DEKİ KAPAK PROMPTU DÜZELTİLDİ.**
> Mevcut README'deki kapak promptu, başlık metnini görselin İÇİNE
> gömüyor (`FILM TITLE TEXT: "THE WAKING GROUND"…`). Bu, Ders 34 ile
> çelişiyor: görsel modeller metni güvenilir üretmez, harf bozulması
> kapağı çöpe atar. Aşağıdaki sürüm **metinsizdir**; tipografi
> post-prodüksiyonda eklenir.
>
> **Merak boşluğu:** Kadın kadranın küçük bir köşesinde, arkasında 200
> metrelik sessiz bir buz jeti. Ölçek farkı sorunun kendisi: "bu insan
> orada ne yapıyor?"

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels, 16:9 landscape. NO TEXT ANYWHERE IN THE IMAGE. YouTube thumbnail optimized — must read at 120 pixels wide.

LEFT THIRD — THE HUMAN: A 41-year-old woman in a dirty-white and burnt-orange surface suit, seen from behind and slightly to the side, occupying the LEFT 30% of the frame and only ONE THIRD of the frame height — deliberately small. She is anchored to a black dust-covered surface by a TAUT PALE GREY TETHER running from her waist harness down to a BURNT-ORANGE HARPOON ANCHOR driven into the ground. Her helmet is turned upward and to the right. Through her FULLY TRANSPARENT SEAMLESS VISOR her face is visible in profile: warm mid-brown skin with visible pore texture, sharp high cheekbones, a dark almost-black eye wide open, lips parted, a pale healed burn scar on her left temple. Her helmet light is on — a narrow cool white cone.

RIGHT TWO THIRDS — THE EVENT: Erupting from the black surface roughly 40 metres behind and to the right of her: a COLOSSAL SILENT ICE JET — a column of white-grey vapour and dust blasting upward and slightly toward the viewer, 200 metres tall, its base a fresh black pit in the crust with outward-tipped slabs at its rim. THE COLUMN'S EDGES ARE SHARP AND STRUCTURED, not soft mist, backlit by a small brilliant white sun low behind it. Fine dust particles stream upward in straight lines across the entire right side of the frame. Above everything: pure black space with sharp non-twinkling stars.

COLOR — TWO VALUES ONLY: ABSOLUTE BLACK crust, darker than charcoal at 4 percent reflectance, against BRILLIANT WHITE jet and backlit vapour at 6500K. One accent only: the burnt orange of her suit bands and the harpoon anchor. Cool white helmet beam at 5500K. No other colours — no teal, no green, no amber sky. Extreme two-value contrast; increase final saturation by 15% so the orange accent survives at thumbnail scale.

COMPOSITION: the tiny anchored human at lower left against the huge jet at right — THE SCALE RELATIONSHIP IS THE IMAGE. Deep focus: both the figure and the jet are sharp, nothing is soft. The UPPER LEFT QUADRANT is kept clean and dark — open negative space reserved for the title added later in post. LOWER-RIGHT CORNER completely empty — no detail, no elements; YouTube's duration badge covers this zone.

TECHNICAL: no text, letters, numbers, logo or watermark anywhere. The jet must read as MASS AND MATERIAL, never as light or fog — it reflects sunlight and casts shadow, it does not emit. 0% bloom, 0% glow filter, 0% soft focus, no lens flare, no god rays. No fire, no flame, no orange heat, no combustion — this is sublimation. No fill light: every shadow is absolutely black with a razor edge. Exactly one person, no duplicate, no second figure, no reflection of another person. The tether stays taut and dead straight and never passes through the ground. Photorealistic skin pores and suit fabric weave retained — no airbrushing, no plastic skin. Must survive the postage-stamp test at 120 pixels wide: the tiny human and the huge jet must both still read. Not CGI, not Unreal Engine, not video game. Photorealistic with 35mm anamorphic film grain.
```

## ✍️ POST-PRODÜKSİYON TİPOGRAFİSİ

```
BAŞLIK:        THE WAKING GROUND        (3 kelime — kılavuz sınırı)
FONT:          Bebas Neue / Impact / Oswald Bold — ultra kalın sans-serif
BOYUT:         60-80 punto, geniş harf aralığı
KONUM:         ÜST SOL çeyrek — jetin üstüne değil, boş siyah göğe
RENK:          Saf beyaz
OKUNABİLİRLİK: Siyah gökyüzünde dış çizgi gerekmez, ama 2 px ince beyaz
               kontur + hafif drop shadow jetin beyazına taşarsa kurtarır
KONTRAST:      Metin ile arka alan arasında minimum 4.5:1 (WCAG)
ALT BAŞLIK:    YOK. "A COMET FILM" gibi bir alt başlık merak boşluğunu
               KAPATIR — kapak kılavuzu §4 buna karşı.
               (README'deki eski kapakta bu alt başlık vardı, kaldırıldı.)
YASAK ALAN:    Sağ alt köşe tamamen boş (süre rozeti)
FİNAL EXPORT:  1280×720, 72 DPI, JPEG %85 (Squoosh)
```

---

# ⚠️ ÜRETİM NOTLARI

```
1. ÇOK PANELLİ SAYFANIN BEDELİ — EN YÜKSEK RİSK
   Tek karede 3-5 panel üretmek panel başına çözünürlük düşürür ve
   modelin panelleri karıştırma ihtimalini artırır.
   ZORUNLU KONTROL — RK sayfasında:
     • 5 panelde de AYNI kişi mi? (elmacık, kaş, sol şakak yanık izi,
       kaş üstü yara, örgü)
     • Panel 4 TEMİZ, panel 5 TOZLU mu? (karışmışsa at)
     • Suit konfigürasyonu 4 ve 5'te birebir aynı mı?
       Özellikle: SAĞ ön koldaki tek dikey gerginlik çubuğu var mı?
   Sapma varsa sayfayı at ve yeniden üret. Sahne üretimine BAŞLAMA.

2. SAYFA KAYMAYA DEVAM EDERSE — PANEL AYIRMA PLANI
   Model tutarlı 5 panel veremiyorsa RK'yı üç ayrı üretime böl
   (yüzler / tam boy temiz / tam boy tozlu), aynı seed ile.
   RF için de aynısı geçerli: 5 fazı tek karede tutamıyorsa
   panel 1'i üret, onu referans vererek 2'yi, sonra 3'ü... zincirle.

3. SİYAHIN SİYAHLIĞI — BU FİLMİN İMZASI
   Model %4 albedoyu sürekli açmak isteyecek; kabuk orta gri bir kayaya
   dönerse filmin tüm görsel kimliği gider. RY panel 1'de kontrol:
   en aydınlık tane bile KOYU GRİ olmalı, gölgeler saf siyah.
   Açıksa at ve yeniden üret.

4. JET = MADDE, IŞIK DEĞİL
   En sık beklenen hata: jetin ışık yayan bir efekt olarak üretilmesi
   (bloom, hale, turuncu ısı). Jetler süblimleşmedir: beyaz-gri madde,
   güneş ışığını YANSITIR, kendi gölgesini atar. Her sayfada negatifte
   tekrarlandı. Işıldayan jet çıkarsa at.

5. HALATIN İKİ HÂLİ AYNI OLURSA SAYFA İŞE YARAMAZ
   RH panel 2 ve 3'ün tek farkı gerginliktir. Model ikisini de aynı
   çizerse (ikisi de düz veya ikisi de sarkık) sayfa çöpe gider —
   çünkü S39'un tüm dramatik etkisi bu farkın öğrenilmiş olmasına dayanır.

6. TOZ YERE DÜŞERSE
   0.0004g'de toz geri düşmez: yavaş, sürekli, YUKARI gider. Model
   Dünya alışkanlığıyla tozu yere indirmeye çalışır. RY panel 4 ve
   RF panel 4-5'te kontrol edilecek ilk şey budur.

7. SAYFALARDA YAZI ÇIKMASI
   Referans sayfası formatı modelde "panel başlığı / etiket / ok"
   refleksi tetikliyor. Altı promptun da negatifinde ayrıca yasaklandı.
   Gutter'larda bile yazı olmayacak — çıkarsa at.

8. MERIDIAN'DA AMBLEM ÇIKMASI
   Model eski bir sondaya bayrak, misyon yaması ve seri numarası
   eklemeye çalışır. Bu hem Ders 13 ihlali hem politika riski
   (gerçek kurum sembolü). RM negatifinde açıkça yasaklandı.

9. SAHNE ÜRETİMİNDE KULLANIM
   Faz dosyaları yazılırken her sahnenin başına "YÜKLENECEK REFERANS"
   satırı konur (yukarıdaki eşleme tablosundan). İlgili SAYFANIN
   TAMAMINI yükle — tek panel yüklemekten daha güçlü bir çapadır.

10. START/END FRAME ZİNCİRİYLE İLİŞKİSİ
    Bu formatta sahne başlangıç karesi bir öncekinin bitiş karesidir
    (`kilavuzlar/KESINTISIZ_VIDEO_URETIM_TEKNIGI.md`). Referans sayfaları
    zincirin YERİNE geçmez — zincir devamlılığı, sayfalar KİMLİĞİ taşır.
    Zincir kopduğunda (faz geçişleri) yeniden çapa olarak sayfalar kullanılır.
```

---

# 📋 SONRAKİ ADIMLAR

```
✅ README.md              ← Bible'lar + 60 sahne haritası
✅ REFERANS_PAKETI.md     ← bu dosya (6 sayfa + kapak)
□ 01_FAZ_1_DONMUS.md      → S1-S12, IMAGE + VIDEO promptları
□ 02_FAZ_2_TERLEME.md     → S13-S24
□ 03_FAZ_3_ACILAN.md      → S25-S36
□ 04_FAZ_4_PATLAMA.md     → S37-S48
□ 05_FAZ_5_KUYRUK.md      → S49-S60
□ MUZIK_VE_SES.md         → 480 saniyelik yay
                             (GOOGLE_FLOW_MUSIC §17 künyesiyle;
                              8s sahne → 60/90/120 BPM hizası)
```
